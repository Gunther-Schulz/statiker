#!/usr/bin/env python3
"""statiker-git — the lock/unit commit machinery of the statiker skill,
precipitated from SKILL.md prose into a bite-tested state machine
(provenance: draft attacks 4-6, dev-notes/OBSERVATIONS.md in the
source repo; test suite: tools/test_statiker_git.py there).

Subcommands (each prints evidence lines, then exactly one final line
`STATIKER-GIT VERDICT: {json}` — the desk books that line verbatim):

  state-gate                        report in-progress git operations
  preflight   --tracker P           run-start checks (tracker pinnable)
  lock-check  --tracker P [--lock-set P ...]
                                    LOCK steps 0-3, read-only
  lock-commit --tracker P [--lock-set P ...] [--drop P ...] -m MSG
                                    LOCK steps 0-6 (drops must match
                                    a prior lock-check's drop list)
  unit-start  --write-set P ... [--unit U<k>]
                                    unit START detector, before any edit;
                                    on UNIT_START_CLEAN, prints one
                                    paste-ready record line per write-set
                                    path (unit U<k>, or the literal
                                    placeholder U<k> when --unit is omitted)
  unit-commit --write-set P ... -m MSG
                                    unit COMMIT with capped contention
                                    retry and HEAD-read discriminator
  worktree-add    --sha S --path P provision a worktree at a locked
                                    sha; P must sit OUTSIDE the repo
  worktree-remove --path P         forced removal of a provisioned
                                    worktree (dirty is the normal case)

Exit codes: 0 = proceedable verdict, 2 = halt/collision/blocked,
3 = usage or internal error (argparse failures included: they emit
a USAGE_ERROR verdict line, never a bare stderr death). The exit
code is routing convenience; the verdict line is the result.
Multi-path flags accept both forms: `--write-set A B` and
`--write-set A --write-set B`.

Design constraints carried from the attack rounds:
- The state gate reads git's STATE DIRECTORIES (rebase-merge,
  rebase-apply, sequencer) plus MERGE_HEAD/CHERRY_PICK_HEAD/
  REVERT_HEAD — never REBASE_HEAD, which stays resolvable after a
  stopped-then-continued rebase completes, and never refs alone,
  which break/exec/reword rebase stops do not set.
- Porcelain is parsed from `--porcelain=v1 -z`; column-one '?' is
  untracked, not staged operator state.
- Commits are `git commit -m MSG -- <pathspec>`: worktree content,
  never -A, tracked paths never re-added, untracked paths added
  exactly and alone.
- The already-present discriminator is a HEAD read (porcelain empty
  over the write-set after adds), never a worktree existence check.
- Everything outside the given pathspec is operator state: never
  committed, never staged, never unstaged, never deleted.
- A provisioning path is the rel()/containment rule INVERTED: taken
  as named (never resolved through a symlink), required OUTSIDE the
  repo rather than inside, decided on the REAL path via the same
  nearest-existing-ancestor probe — git itself happily makes a
  worktree inside a repo, so the halt has to land at the tool.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

VERDICT_PREFIX = "STATIKER-GIT VERDICT: "
RETRY_ATTEMPTS = 5
# read inside main()'s guarded try (_read_retry_base, called at the
# top of main): a module-level float() here sat OUTSIDE every halt
# route, so a bad env value died a bare traceback, exit 1, no verdict
# line at all (begehung-harvest 2, AMENDED (d2)) — the module-level
# default below is overwritten before any handler runs.
RETRY_BASE = 1.0


class Halt(Exception):
    def __init__(self, verdict, **detail):
        self.verdict = verdict
        self.detail = detail


# ES-7: a path whose named and real spellings differ is ACCEPTED on
# the real-path probe and OPERATED ON as named — the divergence is
# noted per path in the verdict rather than silently swallowed, so a
# booked verdict never hides which bytes the operation reached.
RESOLVED = []

BROKEN_PIPE = False


def say(msg):
    # A closed reader (`| head`) breaks the pipe mid-run: an evidence
    # line's write is swallowed here — best-effort, the reader already
    # stopped listening — and the fact is remembered so the CLOSING
    # verdict falls back to stderr instead of dying on the same broken
    # pipe with no verdict line at all and exit 0 (statiker_record.py's
    # sibling fix, finding 5, begehung tier2-without.md part 7/7).
    #
    # ES-9 / E-C: byte-level write over the input's own bytes, mirrored
    # from statiker_record.py's emit() — a text-layer print() under
    # stdout reconfigured errors="replace" mints a SECOND spelling of
    # any non-UTF-8 byte on output, so a printed drop value or
    # write-set paste line could never be pasted back to match the
    # real argv bytes (begehung tier2-without.md F4/SENTENCE-A3).
    global BROKEN_PIPE
    if BROKEN_PIPE:
        return
    try:
        sys.stdout.flush()   # flush the text layer first: we bypass it
        # below, and pending buffered text would otherwise interleave
        # out of order with the raw bytes written next
        sys.stdout.buffer.write(msg.encode("utf-8", "surrogateescape") + b"\n")
        sys.stdout.buffer.flush()   # forces the write NOW — unflushed, a
        # broken pipe surfaces only at interpreter shutdown, past
        # every try/except this fix installs
    except BrokenPipeError:
        BROKEN_PIPE = True


def _stderr_fallback(text):
    try:
        print(text, file=sys.stderr)
    except OSError:
        pass


def _exit_after_broken_pipe(code):
    # CPython's interpreter finalization flushes stdout unconditionally
    # on the way out; hitting the SAME broken pipe there overrides
    # whatever exit() we just called with its own hardcoded 120 (the
    # documented SIGPIPE idiom) — redirecting the fd to devnull first
    # makes that flush a no-op so our own exit code is what lands.
    try:
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
    except OSError:
        pass
    sys.exit(code)


def finish(verdict, exit_code, **detail):
    if RESOLVED and "resolved_from" not in detail:
        detail["resolved_from"] = RESOLVED
    # ensure_ascii=False (E-C): a surrogateescape half kept literal in
    # the JSON string round-trips through say()'s byte-level encode
    # back to the exact input byte; ensure_ascii's default \udcXX
    # escape is six literal ASCII characters a desk could paste, never
    # equal to the one real byte it names (tier2-without.md F4).
    text = VERDICT_PREFIX + json.dumps({"verdict": verdict, **detail},
                                       ensure_ascii=False)
    if BROKEN_PIPE:
        _stderr_fallback(text)
        _exit_after_broken_pipe(3)
    say(text)
    if BROKEN_PIPE:
        _stderr_fallback(text)
        _exit_after_broken_pipe(3)
    sys.exit(exit_code)


def run_git(args, cwd, check=True, input_bytes=None):
    p = subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                       input=input_bytes)
    if check and p.returncode != 0:
        raise Halt("GIT_ERROR", command="git " + " ".join(args),
                   returncode=p.returncode,
                   stderr=p.stderr.decode(errors="replace").strip())
    return p


# ----------------------------------------------------------- porcelain parse

@dataclass
class PorcelainEntry:
    x: str
    y: str
    path: str
    orig_path: str | None


def parse_porcelain_z(raw: bytes):
    """Parse `git status --porcelain=v1 -z` output. Rename/copy entries
    carry a second NUL-separated token (the original path).

    Paths decode with os.fsdecode — the way the OS decodes argv
    (attack-9: errors='replace' gave a non-UTF-8 byte a SECOND
    spelling, so a path named on the command line could never match
    its own porcelain readback: false extras at both commit seams and
    a drop handshake stuck on HALT_DROPS_STALE forever)."""
    tokens = raw.split(b"\x00")
    entries = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if not tok:
            i += 1
            continue
        head = os.fsdecode(tok)
        x, y, path = head[0], head[1], head[3:]
        orig = None
        if x in ("R", "C"):
            i += 1
            orig = os.fsdecode(tokens[i])
        entries.append(PorcelainEntry(x, y, path, orig))
        i += 1
    return entries


def is_staged_collision(entry: PorcelainEntry) -> bool:
    """Column one set = staged operator state — except '?', which
    marks an untracked path, and '!', ignored."""
    return entry.x not in (" ", "?", "!")


def readback_extras(shown_paths: set, expected: set) -> set:
    return set(shown_paths) - set(expected)


def is_index_lock_error(stderr: str) -> bool:
    return "index.lock" in stderr


def nearest_existing_ancestor(p: str):
    """The path itself if it exists (a broken symlink counts — git
    commits one as the link file), else the first ancestor that does,
    else None. The NAMED probe of ES-7's containment rule."""
    cur = p
    while True:
        if os.path.lexists(cur):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


def rebase_at_symlinked_ancestor(p: str, top_real: str):
    """Re-root a path reached through a symlinked ANCESTOR of the repo
    top, or None if no ancestor resolves to the top.

    git reports the toplevel PHYSICALLY, so a path spelled through a
    symlinked ancestor never matches it textually and read as a path
    outside the repo it is plainly inside (attack-10 N4). Only the
    ANCESTOR resolves: the tail below it is re-rooted textually, so a
    link BELOW the top is still taken as named, and a literal `..`
    escape still finds no matching ancestor and still halts."""
    tail = []
    cur = p
    while True:
        if os.path.realpath(cur) == top_real:
            return os.path.join(top_real, *reversed(tail)) if tail else top_real
        parent, name = os.path.split(cur)
        if not name or parent == cur:
            return None
        tail.append(name)
        cur = parent


def git_toplevel(cwd):
    """The nearest enclosing repo's toplevel from `cwd`, or None — the
    REAL half of the every-enclosing-repo probe (begehung-harvest 2,
    worktree-add containment entry). `git rev-parse` resolves symlinked
    ancestors the way the filesystem does, so this catches a target
    that sits inside SOME repo even when that repo is not this one.
    (The record tool carries the same helper standalone;
    statiker_record.py:git_toplevel is its twin — the two scripts
    ship without importing each other.)"""
    try:
        p = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=cwd,
                           capture_output=True)
    except OSError:
        return None
    return os.fsdecode(p.stdout.strip()) if p.returncode == 0 else None


def textual_repo_top(path: str):
    """The nearest ancestor carrying a `.git`, walking `path` AS
    NAMED — the as-named half of the must-be-outside probe. A
    cwd-based read cannot answer this: passing a directory as cwd
    resolves its links, which is exactly the spelling under test."""
    cur = os.path.normpath(path)
    while True:
        if os.path.lexists(os.path.join(cur, ".git")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


def lock_committed_verdict(shas, extras, drops):
    """Pure: the landed lock verdict from readback data — red-tested on
    constructed extras (git's own pathspec commit is not known to
    produce extras; the wiring is certified at function level)."""
    if extras:
        return ("LOCK_COMMITTED_EXTRAS",
                {"sha": shas[-1], "all_shas": shas,
                 "extras": sorted(extras), "drops": drops,
                 "note": "extras are already in history: record as "
                         "collision-class contradiction and brief "
                         "exclusion; never revert"})
    return ("LOCK_COMMITTED",
            {"sha": shas[-1], "all_shas": shas, "drops": drops})


def unit_committed_verdict(sha, extras, residue):
    """Pure: the landed unit verdict from readback data (same
    function-level certification as lock_committed_verdict)."""
    if extras:
        return ("UNIT_COMMITTED_EXTRAS",
                {"sha": sha, "extras": sorted(extras)})
    if residue:
        return ("UNIT_COMMITTED_RESIDUE", {"sha": sha, "residue": residue})
    return ("UNIT_COMMITTED", {"sha": sha})


# ---------------------------------------------------------------- repo model

class Repo:
    def __init__(self):
        # the toplevel is a PATH read: bytes decoded the way the OS
        # decodes argv, never text=True's locale decode — a repo whose
        # directory name carries a non-UTF-8 byte died of a
        # UnicodeDecodeError before any subcommand ran (attack-10 N5)
        p = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True)
        if p.returncode != 0:
            raise Halt("NOT_A_REPO",
                       stderr=p.stderr.decode(errors="replace").strip())
        self.top = Path(os.fsdecode(p.stdout.strip()))

    def git(self, *args, check=True):
        return run_git(list(args), cwd=self.top, check=check)

    def git_path(self, name) -> Path:
        # a path read too: os.fsdecode, never a strict utf-8 decode
        out = os.fsdecode(self.git("rev-parse", "--git-path", name)
                          .stdout.strip())
        p = Path(out)
        return p if p.is_absolute() else self.top / p

    def rel(self, path_arg: str) -> str:
        """Normalize an input path to repo-root-relative POSIX form.
        Relative inputs are taken as repo-root-relative, never
        cwd-relative: callers (briefs, records) write repo-relative
        paths and a subagent's cwd resets between calls — resolving
        against cwd answered about phantom paths from a subdir.

        The path is OPERATED ON as named: normalized textually, never
        substituted by its link target (attack-9: resolve() put a
        link's TARGET into a booked verdict where the brief had named
        the link). CONTAINMENT, though, is decided on the REAL path
        (ES-7, design-attack R3-B7): walk to the nearest EXISTING
        ancestor and require its realpath to sit inside — or equal —
        the top's. An in-repo symlinked directory pointing OUT let a
        unit write outside the repo before any check knew; a literal
        `..` escape still leaves and still halts. A path reached
        through a symlinked ancestor OF THE TOP is re-rooted textually
        (attack-10 N4: git reports the toplevel physically, so the link
        spelling never matches it)."""
        top = os.path.realpath(str(self.top))
        p = os.path.normpath(os.path.join(top, path_arg))
        if not p.startswith(top + os.sep) and p != top:
            rebased = rebase_at_symlinked_ancestor(p, top)
            if rebased is not None:
                p = rebased
        anc = nearest_existing_ancestor(p)
        anc_real = os.path.realpath(anc) if anc else None
        inside = bool(anc_real and (anc_real == top
                                    or anc_real.startswith(top + os.sep)))
        if not inside or not (p == top or p.startswith(top + os.sep)):
            detail = {"path": path_arg}
            if anc is not None:
                detail["resolved_from"] = {"named": p,
                                           "real": os.path.realpath(p)}
            raise Halt("PATH_OUTSIDE_REPO", **detail)
        if p == top:
            return "."      # the repo root: a directory, routed as one
        rel = Path(p[len(top) + 1:]).as_posix()
        real_p = os.path.realpath(p)
        if real_p != p:
            note = {"named": rel, "real": real_p}
            if note not in RESOLVED:
                RESOLVED.append(note)
        return rel

    def outside(self, path_arg: str) -> str:
        """A worktree-provisioning path: rel()'s containment rule
        INVERTED, extended to EVERY enclosing repo and the named/real
        agreement rule (begehung-harvest 2, worktree-add containment
        entry) — mirrors the record tool's `--out` check
        (statiker_record.py:1156-1184, cmd_filter). Relative inputs
        are repo-root-relative (same convention as rel()); the path
        is returned as named, never resolved through a symlink.

        The REAL form catches a target that resolves inside a SIBLING
        repo's tree, not just this one — `worktree-add --path
        ../B/wt-in-B` from repo A used to read WORKTREE_ADDED while
        leaving an untracked directory in repo B (0.2.59 review F1).
        The AS-NAMED form catches a symlink spelling whose textual
        path never leaves THIS repo's own tree even though the
        link's target does — `link/wt` (link -> outside dir) used to
        read WORKTREE_ADDED while `filter --out link/art.md` already
        halted on the identical shape (0.2.59 review F2). Either
        finding an enclosing repo halts PATH_INSIDE_REPO.

        Both probes walk from the target's PARENT, never the target
        itself: a worktree-remove path already exists as a
        provisioned worktree by the time this runs, and `git
        rev-parse --show-toplevel` run FROM INSIDE a linked worktree
        reports the worktree's own root — checking the target itself
        would read every legitimate worktree as its own containing
        repo. THIS repo's own root is the one path that must still
        halt without an ancestor to climb to, so it is checked
        directly first."""
        top = os.path.realpath(str(self.top))
        p = os.path.normpath(os.path.join(str(self.top), path_arg))
        real_p = os.path.realpath(p)
        if p == str(self.top) or real_p == top:
            raise Halt("PATH_INSIDE_REPO", path=path_arg)
        real_parent = os.path.dirname(real_p) or "."
        real_anc = nearest_existing_ancestor(real_parent) or real_parent
        named_parent = os.path.dirname(p) or "."
        enclosing = git_toplevel(real_anc) or textual_repo_top(named_parent)
        if enclosing:
            detail = {"path": path_arg, "repo": enclosing}
            if real_p != p:
                detail["resolved_from"] = {"named": p, "real": real_p}
            raise Halt("PATH_INSIDE_REPO", **detail)
        return p

    # -- state gate ---------------------------------------------------------
    def ops_in_progress(self):
        ops = []
        if (self.git_path("MERGE_HEAD")).exists():
            ops.append("merge")
        if self.git_path("rebase-merge").exists() or \
           self.git_path("rebase-apply").exists():
            ops.append("rebase")
        seq = self.git_path("sequencer").exists()
        if self.git_path("CHERRY_PICK_HEAD").exists():
            ops.append("cherry-pick")
        if self.git_path("REVERT_HEAD").exists():
            ops.append("revert")
        if seq and "cherry-pick" not in ops and "revert" not in ops:
            # multi-commit sequence paused between steps: identify by todo
            todo = self.git_path("sequencer") / "todo"
            kind = "cherry-pick"
            try:
                first = todo.read_text().split(None, 1)[0]
                if first.startswith("revert"):
                    kind = "revert"
            except OSError:
                pass
            ops.append(kind)
        return ops

    def state_gate(self):
        ops = self.ops_in_progress()
        if ops:
            say(f"state gate: operation(s) in progress: {', '.join(ops)}")
            raise Halt("HALT_STATE", ops=ops)
        say("state gate: clean (no merge/cherry-pick/revert/rebase in progress)")

    # -- path facts ---------------------------------------------------------
    def is_tracked(self, rel):
        return self.git("ls-files", "--error-unmatch", "--", rel,
                        check=False).returncode == 0

    def is_ignored(self, rel):
        return self.git("check-ignore", "-q", "--", rel,
                        check=False).returncode == 0

    def in_head(self, rel):
        return self.git("cat-file", "-e", f"HEAD:{rel}",
                        check=False).returncode == 0

    def porcelain(self, paths):
        raw = self.git("status", "--porcelain=v1", "-z",
                       "--untracked-files=all", "--", *paths).stdout
        return parse_porcelain_z(raw)

    def check_symlink_leaf(self, rels):
        """An EXISTING leaf that is a symlink halts at every
        path-accepting seam (ES-7). git ACCEPTS a link leaf and commits
        the link STRING — no dry-run catches it, and the unit's real
        output never reaches history — so the halt has to land at a
        check. Routed USAGE_ERROR by parallel with the filter's
        tracker-islink halt, which the settle keeps: the composition
        names the wrong path, and the answer is to name the real one."""
        links = [r for r in rels if os.path.islink(self.top / r)]
        if links:
            raise Halt("USAGE_ERROR",
                       error="path names a symlink (" + ", ".join(links)
                             + "): name the real path — git commits a link "
                               "leaf as the link string, not as the file")

    def validate_file_paths(self, rels):
        """Lock-set and write-set paths name FILES, never directories
        (a directory pathspec commits whatever the operator touched
        under it); every path must exist in worktree or in HEAD."""
        dirs = [r for r in rels if (self.top / r).is_dir()]
        if dirs:
            raise Halt("HALT_DIRECTORY_PATH", paths=dirs)
        self.check_symlink_leaf(rels)
        # lexists, not exists: a path that IS a symlink with a missing
        # target is a file git commits (as the link itself), and
        # exists() follows the link and called it missing (attack-10 N8)
        missing = [r for r in rels
                   if not os.path.lexists(self.top / r)
                   and not self.in_head(r)]
        if missing:
            raise Halt("HALT_MISSING_PATH", paths=missing)

    def head_shown_paths(self, sha="HEAD"):
        # -z: NUL separators, unquoted paths. Newline output C-quotes
        # any non-ASCII byte under default core.quotePath, and a quoted
        # readback can never match its own pathspec (attack-8 B1: a
        # clean commit over a path with an umlaut reported the path as
        # a false extra at both seams — in the lock case the "extra"
        # was the tracker, which the desk then excludes from the attack
        # surface). The porcelain reads were always -z and unaffected.
        #
        # E-D: reads the LANDED sha the caller names, never a bare
        # "HEAD" — a synchronous post-commit hook that lands a sibling
        # commit (the capped-retry contention design SKILL.md blesses)
        # moves HEAD past ours before this process ever reads it, and
        # a bare HEAD read then shows the sibling's diff, booking its
        # sha and a false extra (WITHOUT-F9).
        out = self.git("show", "--name-only", "--format=", "-z",
                       sha).stdout
        return set(os.fsdecode(p) for p in out.split(b"\x00") if p)

    def _index_write_with_retry(self, git_args, failure_verdict):
        """Run an index-writing git command; index.lock failures are
        contention — capped, spaced retries, then a blocked report."""
        last_err = ""
        for attempt in range(1, RETRY_ATTEMPTS + 1):
            p = self.git(*git_args, check=False)
            if p.returncode == 0:
                return p
            last_err = (p.stderr.decode(errors="replace")
                        + p.stdout.decode(errors="replace")).strip()
            if not is_index_lock_error(last_err):
                raise Halt(failure_verdict, error=last_err)
            say(f"index.lock contention, attempt {attempt}/{RETRY_ATTEMPTS}")
            if attempt < RETRY_ATTEMPTS:
                time.sleep(RETRY_BASE * attempt)
        raise Halt("BLOCKED_CONTENTION", attempts=RETRY_ATTEMPTS,
                   error=last_err,
                   index_lock_present=self.git_path("index.lock").exists())

    def add_with_retry(self, rel):
        self._index_write_with_retry(["add", "--", rel], "ADD_FAILED")

    def dry_run_add(self, rel):
        """Containment and git-ACCEPTABILITY are separate questions
        (ES-7): a path this repo contains can still be one git refuses
        — a path beyond a symbolic link is the attack-11 recipe. The
        refusal surfaces at the earliest seam that knows the path, so
        the lock check answers it instead of the commit."""
        p = self.git("add", "--dry-run", "--", rel, check=False)
        if p.returncode != 0:
            err = (p.stderr.decode(errors="replace")
                   + p.stdout.decode(errors="replace")).strip()
            raise Halt("ADD_FAILED", path=rel, error=err)

    def commit_with_retry(self, message, pathspec):
        p = self._index_write_with_retry(
            ["commit", "-m", message, "--", *pathspec], "COMMIT_FAILED")
        sha = self._sha_from_commit_output(p.stdout)
        say(f"commit landed: {sha}")
        return sha

    _COMMIT_SUMMARY_RE = re.compile(r"^\[([^\]]*)\]", re.MULTILINE)

    def _sha_from_commit_output(self, stdout_bytes):
        """E-D: the sha comes from the commit OPERATION's own output,
        never a later `rev-parse HEAD` — `git commit` prints its
        landed commit's summary as `[<branch-desc> <abbrev>]
        <subject>` before any post-commit hook runs, so parsing THIS
        line names the commit this call actually made, immune to a
        hook that lands a sibling commit and moves HEAD past it
        (WITHOUT-F9). The abbreviation is expanded against the OBJECT
        it names (`rev-parse --verify <abbrev>^{commit}`), not against
        the mutable HEAD ref."""
        text = stdout_bytes.decode("utf-8", "replace")
        m = self._COMMIT_SUMMARY_RE.search(text)
        if not m or not m.group(1).split():
            # defensive only (no verdict name of its own — a commit
            # landing without git's own summary line is not a shape any
            # supported git prints on success): routed through the
            # existing COMMIT_FAILED, since a sha the tool cannot name
            # is the same "cannot proceed on this commit" as one the
            # index-write retry never landed.
            raise Halt("COMMIT_FAILED",
                       error="commit summary unparseable: " + text.strip())
        abbrev = m.group(1).split()[-1]
        return self.git("rev-parse", "--verify",
                        abbrev + "^{commit}").stdout.decode().strip()


# ------------------------------------------------------------------ lock

def drop_excluded(drops):
    """Every path a drop takes out of the pathspec — a staged rename's
    two halves are one drop and two paths."""
    return ({d["path"] for d in drops}
            | {d["orig_path"] for d in drops if "orig_path" in d})


def lock_survey(repo, tracker, lock_set):
    """LOCK steps 0-3. Returns (pathspec, drops, adds); raises Halt on
    any tracker-affecting or state condition."""
    repo.state_gate()                                              # step 0

    tracker_rel = repo.rel(tracker)
    rels = [tracker_rel] + [repo.rel(p) for p in lock_set]
    pathspec = list(dict.fromkeys(rels))                           # step 1
    repo.validate_file_paths(pathspec)
    say(f"pathspec: {' '.join(pathspec)}")

    drops = []                                                     # step 2
    entries = repo.porcelain(pathspec)
    for e in entries:
        if is_staged_collision(e):
            if e.path == tracker_rel:
                raise Halt("HALT_TRACKER_COLLISION", porcelain=f"{e.x}{e.y} {e.path}")
            say(f"collision (staged operator state): {e.x}{e.y} {e.path}")
            drop = {"path": e.path, "reason": "collision",
                    "porcelain": f"{e.x}{e.y}"}
            if e.orig_path:
                if e.orig_path == tracker_rel:
                    # the tracker as a rename's other half is staged
                    # operator state ON the tracker, and the tracker is
                    # never dropped
                    raise Halt("HALT_TRACKER_COLLISION",
                               porcelain=f"{e.x}{e.y} {e.path} <- {e.orig_path}")
                drop["orig_path"] = e.orig_path
            drops.append(drop)

    # BOTH halves of a staged rename leave the pathspec (ES-11 /
    # attack-11 N8): the deletion half stayed behind and rode into the
    # lock commit through a handshake the desk had already satisfied
    dropped_paths = drop_excluded(drops)                           # step 3
    adds = []
    for r in pathspec:
        if r in dropped_paths or repo.is_tracked(r):
            continue
        if repo.is_ignored(r):
            if r == tracker_rel:
                raise Halt("HALT_TRACKER_UNPINNABLE", path=r)
            say(f"drop (untracked path is ignored): {r}")
            drops.append({"path": r, "reason": "ignored"})
        else:
            adds.append(r)
    return pathspec, drops, adds


def cmd_lock_check(repo, args):
    pathspec, drops, adds = lock_survey(repo, args.tracker, args.lock_set)
    for r in adds:
        repo.dry_run_add(r)
    if drops:
        finish("LOCK_CHECK_DROPS", 0, drops=drops, adds=adds,
               pathspec=pathspec)
    finish("LOCK_CHECK_CLEAN", 0, adds=adds, pathspec=pathspec)


def cmd_lock_commit(repo, args):
    pathspec, drops, adds = lock_survey(repo, args.tracker, args.lock_set)
    live = sorted(d["path"] for d in drops)
    acked = sorted(repo.rel(p) for p in args.drop)
    stale = [p for p in acked if p not in live]
    unacked = [p for p in live if p not in acked]
    if stale:
        # an acknowledged drop no longer live: state moved since check
        raise Halt("HALT_DROPS_STALE", acknowledged=acked, live=live)
    if unacked:
        # a live drop the desk has not recorded F-lines for yet
        raise Halt("HALT_DROPS_UNACKNOWLEDGED", acknowledged=acked, live=live)

    effective = [p for p in pathspec if p not in drop_excluded(drops)]
    if not effective:
        raise Halt("HALT_NO_PATHSPEC")
    dirty = [e for e in repo.porcelain(effective)]
    if not dirty:
        raise Halt("HALT_NO_CHANGES", pathspec=effective)

    for r in adds:                                                 # step 4
        say(f"add (untracked, surviving): {r}")
        repo.add_with_retry(r)

    sha = repo.commit_with_retry(args.message, effective)          # step 5

    shas = [sha]                                                   # step 6
    # From here on commits EXIST: every failure verdict out of the
    # readback — COMMIT_FAILED, BLOCKED_CONTENTION, GIT_ERROR, the
    # residue cap — carries the landed shas (attack-7 B3: a halt
    # reported without them was routed as "uncommitted" over an
    # orphan lock commit).
    try:
        extras = readback_extras(repo.head_shown_paths(sha), set(effective))
        residue_laps = 0
        while True:
            residue = repo.porcelain(effective)
            if not residue:
                break
            if residue_laps == 3:
                raise Halt("HALT_RESIDUE_PERSISTS", shas=shas,
                           residue=sorted({e.path for e in residue}))
            residue_laps += 1
            residue_paths = sorted({e.path for e in residue})
            say(f"readback residue, lap {residue_laps}: "
                f"{' '.join(residue_paths)}")
            tracker_rel = repo.rel(args.tracker)
            lap_spec = sorted(set(residue_paths) | {tracker_rel})
            shas.append(repo.commit_with_retry(
                args.message + f" [residue lap {residue_laps}]", lap_spec))
            extras |= readback_extras(repo.head_shown_paths(shas[-1]),
                                      set(effective))
    except Halt as h:
        h.detail.setdefault("shas", shas)
        raise

    say(f"readback: porcelain clean over pathspec; pinned sha {shas[-1]}")
    name, detail = lock_committed_verdict(shas, extras, drops)
    finish(name, 0, **detail)


# ------------------------------------------------------------------ unit

def unit_paths(repo, args):
    rels = list(dict.fromkeys(repo.rel(p) for p in args.write_set))
    return rels


def cmd_unit_start(repo, args):
    repo.state_gate()          # before any edit: operator tree untouched
    rels = unit_paths(repo, args)
    dirs = [r for r in rels if (repo.top / r).is_dir()]
    if dirs:
        raise Halt("HALT_DIRECTORY_PATH", paths=dirs)
    repo.check_symlink_leaf(rels)
    ignored = [r for r in rels
               if not repo.is_tracked(r) and repo.is_ignored(r)]
    if ignored:
        raise Halt("HALT_IGNORED_WRITESET", paths=ignored)
    entries = repo.porcelain(rels)
    if entries:
        listing = [{"porcelain": f"{e.x}{e.y}", "path": e.path}
                   for e in entries]
        for e in listing:
            say(f"collision: {e['porcelain']} {e['path']}")
        raise Halt("UNIT_COLLISION", entries=listing)
    say("write-set clean: every later modification is the unit's own")
    unit_label = args.unit if args.unit else "U<k>"
    for rel in rels:
        say(f"- F<n> [VERIFIED] unit {unit_label} write-set: {rel} "
            f"— basis: <the unit enumeration>")
    finish("UNIT_START_CLEAN", 0, write_set=rels)


def cmd_unit_commit(repo, args):
    repo.state_gate()                       # re-read at the commit seam
    rels = unit_paths(repo, args)
    repo.validate_file_paths(rels)
    # column-one re-read BEFORE any add: an operator stage landing
    # mid-unit would be silently destroyed by the pathspec commit
    # (the lock's attack-5 B1 class, at the unit's longer window).
    # NO tolerance for staged 'A' (attack-7 B2): column one cannot
    # distinguish an operator's staged draft from a blocked prior
    # attempt's leftover, and the leftover case never reaches this
    # seam anyway — a re-dispatched unit meets it at START as
    # UNIT_COLLISION and the desk's provenance clearing handles it.
    staged = [e for e in repo.porcelain(rels)
              if e.x not in (" ", "?")]
    if staged:
        listing = [{"porcelain": f"{e.x}{e.y}", "path": e.path}
                   for e in staged]
        for e in listing:
            say(f"commit-seam collision (staged mid-unit): "
                f"{e['porcelain']} {e['path']}")
        raise Halt("UNIT_COMMIT_COLLISION", entries=listing)
    for r in rels:
        if not repo.is_tracked(r) and os.path.lexists(repo.top / r):
            if repo.is_ignored(r):
                raise Halt("HALT_IGNORED_WRITESET", paths=[r])
            say(f"add (new to git): {r}")
            repo.add_with_retry(r)
    if not repo.porcelain(rels):
        # HEAD read: index and worktree match HEAD over the write-set —
        # nothing to commit. The unit's residue check decides whether
        # this is already-present; a failed commit never lands here.
        say("no diff vs HEAD over the write-set; nothing committed")
        finish("UNIT_NO_DIFF_VS_HEAD", 0, write_set=rels)
    sha = repo.commit_with_retry(args.message, rels)
    try:
        extras = readback_extras(repo.head_shown_paths(sha), set(rels))
        residue = [f"{e.x}{e.y} {e.path}" for e in repo.porcelain(rels)]
    except Halt as h:
        h.detail.setdefault("sha", sha)   # the commit landed (B3 kin)
        raise
    name, detail = unit_committed_verdict(sha, extras, residue)
    finish(name, 0, write_set=rels, **detail)


# --------------------------------------------------------------- worktree

def cmd_worktree_add(repo, args):
    path = repo.outside(args.path)
    repo.git("worktree", "add", "--detach", path, args.sha)
    finish("WORKTREE_ADDED", 0, path=path, sha=args.sha)


def cmd_worktree_remove(repo, args):
    path = repo.outside(args.path)
    # forced: a by-product file left inside a provisioned worktree is
    # the normal case, never an operator-precious draft to protect —
    # unlike the pathspec commits above, nothing here operates on
    # repo-tracked content outside the given path.
    repo.git("worktree", "remove", "--force", path)
    finish("WORKTREE_REMOVED", 0, path=path)


# ------------------------------------------------------------------ misc

def cmd_state_gate(repo, args):
    ops = repo.ops_in_progress()
    if ops:
        finish("STATE_IN_PROGRESS", 2, ops=ops)
    finish("STATE_CLEAN", 0, ops=[])


def cmd_preflight(repo, args):
    tracker_rel = repo.rel(args.tracker)
    # the tracker names a FILE: a directory path answered PREFLIGHT_OK
    # over `tracker: "."` and the run started with no record at all
    # (attack-10 NIT1). The path need not EXIST yet — at run start it
    # normally does not.
    if (repo.top / tracker_rel).is_dir():
        raise Halt("HALT_DIRECTORY_PATH", paths=[tracker_rel])
    repo.check_symlink_leaf([tracker_rel])
    # a DEDICATED repo-health read, index-reading BY DESIGN and the
    # only strict one (ES-11 / attack-11 N5): every other read here is
    # check=False, so a corrupt index answered PREFLIGHT_OK and the run
    # started on a repo no later seam could commit to. Strictness is
    # this read's alone — the ignore and tracked reads keep their
    # documented exit semantics, where a non-error exit is an answer.
    repo.git("ls-files", "-z", "--", tracker_rel)
    ops = repo.ops_in_progress()
    if not repo.is_tracked(tracker_rel) and repo.is_ignored(tracker_rel):
        finish("PREFLIGHT_UNPINNABLE_TRACKER", 2, tracker=tracker_rel,
               ops=ops,
               note="the repo ignores the tracker path: the run cannot "
                    "pin its record here — surface before any design work")
    finish("PREFLIGHT_OK", 0, tracker=tracker_rel, ops=ops)


HALT_EXIT = 2


class Parser(argparse.ArgumentParser):
    """Usage errors land as a USAGE_ERROR verdict line (exit 3),
    never as a bare argparse death on the halt exit code."""

    def error(self, message):
        raise Halt("USAGE_ERROR", error=message)


def flat(list_of_lists):
    return [x for sub in list_of_lists for x in sub]


def _read_retry_base():
    """STATIKER_GIT_RETRY_BASE, parsed inside main()'s guarded try
    (AMENDED (d2)): a bad value halts USAGE_ERROR with a verdict line,
    same defined exit code as (d)'s broken-pipe halt, rather than a
    bare traceback dying before any subcommand — even state-gate,
    which never reads it — gets to run."""
    raw = os.environ.get("STATIKER_GIT_RETRY_BASE", "1.0")
    try:
        return float(raw)
    except ValueError:
        raise Halt("USAGE_ERROR",
                   error=f"STATIKER_GIT_RETRY_BASE is not a float: {raw!r}")


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    ap = Parser(prog="statiker-git")
    sub = ap.add_subparsers(dest="cmd", required=True,
                            parser_class=Parser)

    sub.add_parser("state-gate")

    p = sub.add_parser("preflight")
    p.add_argument("--tracker", required=True)

    p = sub.add_parser("lock-check")
    p.add_argument("--tracker", required=True)
    p.add_argument("--lock-set", action="append", nargs="+", default=[])

    p = sub.add_parser("lock-commit")
    p.add_argument("--tracker", required=True)
    p.add_argument("--lock-set", action="append", nargs="+", default=[])
    p.add_argument("--drop", action="append", nargs="+", default=[])
    p.add_argument("-m", "--message", required=True)

    p = sub.add_parser("unit-start")
    p.add_argument("--write-set", action="append", nargs="+", required=True)
    p.add_argument("--unit", default=None)

    p = sub.add_parser("unit-commit")
    p.add_argument("--write-set", action="append", nargs="+", required=True)
    p.add_argument("-m", "--message", required=True)

    p = sub.add_parser("worktree-add")
    p.add_argument("--sha", required=True)
    p.add_argument("--path", required=True)

    p = sub.add_parser("worktree-remove")
    p.add_argument("--path", required=True)

    handlers = {
        "state-gate": cmd_state_gate,
        "preflight": cmd_preflight,
        "lock-check": cmd_lock_check,
        "lock-commit": cmd_lock_commit,
        "unit-start": cmd_unit_start,
        "unit-commit": cmd_unit_commit,
        "worktree-add": cmd_worktree_add,
        "worktree-remove": cmd_worktree_remove,
    }
    try:
        args = ap.parse_args()
        for attr in ("lock_set", "drop", "write_set"):
            if hasattr(args, attr):
                setattr(args, attr, flat(getattr(args, attr)))
        global RETRY_BASE
        RETRY_BASE = _read_retry_base()
        repo = Repo()
        handlers[args.cmd](repo, args)
    except Halt as h:
        code = 3 if h.verdict == "USAGE_ERROR" else HALT_EXIT
        finish(h.verdict, code, **h.detail)
    except Exception as e:  # never a silent death: verdict line always lands
        finish("INTERNAL_ERROR", 3, error=f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

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
  unit-start  --write-set P ...     unit START detector, before any edit
  unit-commit --write-set P ... -m MSG
                                    unit COMMIT with capped contention
                                    retry and HEAD-read discriminator

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
"""

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

VERDICT_PREFIX = "STATIKER-GIT VERDICT: "
RETRY_ATTEMPTS = 5
RETRY_BASE = float(os.environ.get("STATIKER_GIT_RETRY_BASE", "1.0"))


class Halt(Exception):
    def __init__(self, verdict, **detail):
        self.verdict = verdict
        self.detail = detail


def say(msg):
    print(msg)


def finish(verdict, exit_code, **detail):
    say(VERDICT_PREFIX + json.dumps({"verdict": verdict, **detail}))
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
    carry a second NUL-separated token (the original path)."""
    tokens = raw.split(b"\x00")
    entries = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if not tok:
            i += 1
            continue
        head = tok.decode(errors="replace")
        x, y, path = head[0], head[1], head[3:]
        orig = None
        if x in ("R", "C"):
            i += 1
            orig = tokens[i].decode(errors="replace")
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


# ---------------------------------------------------------------- repo model

class Repo:
    def __init__(self):
        p = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True)
        if p.returncode != 0:
            raise Halt("NOT_A_REPO", stderr=p.stderr.strip())
        self.top = Path(p.stdout.strip())

    def git(self, *args, check=True):
        return run_git(list(args), cwd=self.top, check=check)

    def git_path(self, name) -> Path:
        out = self.git("rev-parse", "--git-path", name).stdout.decode().strip()
        p = Path(out)
        return p if p.is_absolute() else self.top / p

    def rel(self, path_arg: str) -> str:
        """Normalize an input path to repo-root-relative POSIX form.
        Relative inputs are taken as repo-root-relative, never
        cwd-relative: callers (briefs, records) write repo-relative
        paths and a subagent's cwd resets between calls — resolving
        against cwd answered about phantom paths from a subdir."""
        p = Path(path_arg)
        if not p.is_absolute():
            p = self.top / p
        try:
            return p.resolve().relative_to(self.top.resolve()).as_posix()
        except ValueError:
            raise Halt("PATH_OUTSIDE_REPO", path=path_arg)

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

    def validate_file_paths(self, rels):
        """Lock-set and write-set paths name FILES, never directories
        (a directory pathspec commits whatever the operator touched
        under it); every path must exist in worktree or in HEAD."""
        dirs = [r for r in rels if (self.top / r).is_dir()]
        if dirs:
            raise Halt("HALT_DIRECTORY_PATH", paths=dirs)
        missing = [r for r in rels
                   if not (self.top / r).exists() and not self.in_head(r)]
        if missing:
            raise Halt("HALT_MISSING_PATH", paths=missing)

    def head_shown_paths(self):
        out = self.git("show", "--name-only", "--format=",
                       "HEAD").stdout.decode()
        return set(l for l in out.splitlines() if l)

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

    def commit_with_retry(self, message, pathspec):
        self._index_write_with_retry(
            ["commit", "-m", message, "--", *pathspec], "COMMIT_FAILED")
        sha = self.git("rev-parse", "HEAD").stdout.decode().strip()
        say(f"commit landed: {sha}")
        return sha


# ------------------------------------------------------------------ lock

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
                drop["orig_path"] = e.orig_path
            drops.append(drop)

    dropped_paths = {d["path"] for d in drops}                     # step 3
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

    effective = [p for p in pathspec if p not in set(live)]
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
    extras = readback_extras(repo.head_shown_paths(), set(effective))
    residue_laps = 0
    while True:
        residue = repo.porcelain(effective)
        if not residue:
            break
        if residue_laps == 3:
            # commits EXIST — the verdict carries every landed sha;
            # the last one is not readback-clean
            raise Halt("HALT_RESIDUE_PERSISTS", shas=shas,
                       residue=sorted({e.path for e in residue}))
        residue_laps += 1
        residue_paths = sorted({e.path for e in residue})
        say(f"readback residue, lap {residue_laps}: {' '.join(residue_paths)}")
        tracker_rel = repo.rel(args.tracker)
        lap_spec = sorted(set(residue_paths) | {tracker_rel})
        shas.append(repo.commit_with_retry(
            args.message + f" [residue lap {residue_laps}]", lap_spec))
        extras |= readback_extras(repo.head_shown_paths(), set(effective))

    say(f"readback: porcelain clean over pathspec; pinned sha {shas[-1]}")
    if extras:
        finish("LOCK_COMMITTED_EXTRAS", 0, sha=shas[-1], all_shas=shas,
               extras=sorted(extras), drops=drops,
               note="extras are already in history: record as collision-class "
                    "contradiction and brief exclusion; never revert")
    finish("LOCK_COMMITTED", 0, sha=shas[-1], all_shas=shas, drops=drops)


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
    finish("UNIT_START_CLEAN", 0, write_set=rels)


def cmd_unit_commit(repo, args):
    repo.state_gate()                       # re-read at the commit seam
    rels = unit_paths(repo, args)
    repo.validate_file_paths(rels)
    # column-one re-read BEFORE any add: an operator stage landing
    # mid-unit would be silently destroyed by the pathspec commit
    # (the lock's attack-5 B1 class, at the unit's longer window).
    # 'A' is tolerated: a staged add on the write-set is a blocked
    # prior attempt's leftover, and halting on it would deadlock the
    # retry — the named residue is an operator-staged NEW file
    # landing mid-unit on a write-set path.
    staged = [e for e in repo.porcelain(rels)
              if e.x not in (" ", "?", "A")]
    if staged:
        listing = [{"porcelain": f"{e.x}{e.y}", "path": e.path}
                   for e in staged]
        for e in listing:
            say(f"commit-seam collision (staged mid-unit): "
                f"{e['porcelain']} {e['path']}")
        raise Halt("UNIT_COMMIT_COLLISION", entries=listing)
    for r in rels:
        if not repo.is_tracked(r) and (repo.top / r).exists():
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
    extras = readback_extras(repo.head_shown_paths(), set(rels))
    residue = [f"{e.x}{e.y} {e.path}" for e in repo.porcelain(rels)]
    if extras:
        finish("UNIT_COMMITTED_EXTRAS", 0, sha=sha, extras=sorted(extras))
    if residue:
        finish("UNIT_COMMITTED_RESIDUE", 0, sha=sha, residue=residue)
    finish("UNIT_COMMITTED", 0, sha=sha, write_set=rels)


# ------------------------------------------------------------------ misc

def cmd_state_gate(repo, args):
    ops = repo.ops_in_progress()
    if ops:
        finish("STATE_IN_PROGRESS", 2, ops=ops)
    finish("STATE_CLEAN", 0, ops=[])


def cmd_preflight(repo, args):
    tracker_rel = repo.rel(args.tracker)
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


def main():
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

    p = sub.add_parser("unit-commit")
    p.add_argument("--write-set", action="append", nargs="+", required=True)
    p.add_argument("-m", "--message", required=True)

    handlers = {
        "state-gate": cmd_state_gate,
        "preflight": cmd_preflight,
        "lock-check": cmd_lock_check,
        "lock-commit": cmd_lock_commit,
        "unit-start": cmd_unit_start,
        "unit-commit": cmd_unit_commit,
    }
    try:
        args = ap.parse_args()
        for attr in ("lock_set", "drop", "write_set"):
            if hasattr(args, attr):
                setattr(args, attr, flat(getattr(args, attr)))
        repo = Repo()
        handlers[args.cmd](repo, args)
    except Halt as h:
        code = 3 if h.verdict == "USAGE_ERROR" else HALT_EXIT
        finish(h.verdict, code, **h.detail)
    except Exception as e:  # never a silent death: verdict line always lands
        finish("INTERNAL_ERROR", 3, error=f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

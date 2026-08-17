#!/usr/bin/env python3
"""Contract parity between the tools and SKILL.md — the check the
0.2.32 reviewer and attack 7 both ran by hand, mechanized.

Reach, stated honestly (attack-8 N4 corrected the 0.2.36 booking):
this instrument mechanizes VERDICT-NAME parity plus emit-position
discipline — it does not cover behavioral carry-across (a repair
landing at one seam and not its sibling); that class's mechanism is
the per-repair parallel-site test pair in the suites, plus the attack
rounds themselves.

Two directions, both set-exact:
- every verdict either script can emit appears literally in SKILL.md
  (named at its route or inside a catch-all's parenthetical);
- every verdict-shaped token SKILL.md names is one a script emits.

Emitted verdicts are extracted from the AST at their EMIT POSITIONS
(finish()/Halt() args — positional OR keyword — the retry helper's
verdict arg, tuple-returning factory functions, and conduit-variable
assignments), not grepped from the whole file. Provenance: attack-8
showed the grep form blind to no-underscore names (V3), assembled
names (V4b), and its own NON_VERDICTS silencing lane (V6); attack-9
drove the first AST form past with keyword-arg emits (V7),
conduit-named locals (V8), and non-`_verdict` factories (V10b) — all
three closed here by construction (keyword args are read, conduit
assignments feed the emitted set or flag as offenders, ALL
tuple-returning functions are scanned).

Honest reach (attack-9 N1): a hand-rolled emit that rebuilds the
verdict line without finish/Halt (V9) is invisible to any call-site
analysis. The durable layer for that class now sits in this file as
the RUNTIME BATTERY below — it drives every subcommand of both tools
over real invocations (happy paths, usage errors, unreadable and
out-of-repo trackers, a malformed record, an in-repo artifact, stdin)
and checks the verdict names the processes ACTUALLY print. Its own
red arrangement: the committed battery run against a copy of
statiker_record.py carrying a planted hand-rolled emit — the AST
layer reports that copy clean (no offenders, the name unseen), the
battery names it. Reach still not covered by either layer: an emit on
a path no battery row drives.

Run: python3 tools/test_contract.py
"""

import ast
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL = REPO_ROOT / "plugin" / "skills" / "statiker" / "SKILL.md"
SCRIPTS = [
    REPO_ROOT / "plugin" / "skills" / "statiker" / "scripts" / "statiker_git.py",
    REPO_ROOT / "plugin" / "skills" / "statiker" / "scripts" / "statiker_record.py",
]

VERDICT_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b")
MORPHOLOGY = re.compile(r"[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\Z")

# emit positions: callable name -> index of the verdict argument
EMIT_ARG_INDEX = {"finish": 0, "Halt": 0, "_index_write_with_retry": 1}
# sanctioned indirections: variables/attributes that CARRY a verdict
# from another checked emit position (their sources are the retry
# helper's literal args and the *_verdict factory returns below)
#
# False-fire class (lane G, BACKLOG.md E-K): this is a bare-name AST
# match, scope-unaware — any local or attribute sharing one of these
# names trips the exemption whether or not it carries a verdict (an
# ordinary local `name` in branch_state(), statiker_git.py, false-
# fired this way). Observed cure: rename the unrelated local. A
# scoped match (restrict to assignments reaching a finish()/say()
# call) was evaluated and deferred — it needs cross-referencing an
# assignment target against later call-argument uses within function
# scope, which the flat ast.walk() below does not provide.
EMIT_CONDUITS = {"failure_verdict", "name", "verdict"}


def _call_name(node):
    fn = node.func
    if isinstance(fn, ast.Name):
        return fn.id
    if isinstance(fn, ast.Attribute):
        return fn.attr
    return None


# keyword names under which the verdict may travel at each emit call
EMIT_KWARGS = {"finish": "verdict", "Halt": "verdict",
               "_index_write_with_retry": "failure_verdict"}


def _classify_emit_arg(a, literals, offenders, lineno):
    if isinstance(a, ast.Constant) and isinstance(a.value, str):
        if MORPHOLOGY.match(a.value):
            literals.add(a.value)
        else:
            offenders.append((lineno, repr(a.value)))
    elif isinstance(a, ast.Name) and a.id in EMIT_CONDUITS:
        pass
    elif isinstance(a, ast.Attribute) and a.attr in EMIT_CONDUITS:
        pass
    else:
        offenders.append((lineno, ast.dump(a)[:80]))


def emit_position_verdicts(source_text):
    """(literals, offenders) for one script's source. An offender is
    any emit-position argument — positional or keyword — that is
    neither a morphology-passing string literal nor a declared
    conduit, and any conduit assignment from a non-literal."""
    literals, offenders = set(), []
    tree = ast.parse(source_text)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = _call_name(node)
            if name not in EMIT_ARG_INDEX:
                continue
            idx = EMIT_ARG_INDEX[name]
            if len(node.args) > idx:
                _classify_emit_arg(node.args[idx], literals, offenders,
                                   node.lineno)
                continue
            # keyword form (attack-9 V7: `continue` here was a silent
            # skip — a keyword emit went unchecked entirely)
            kw = next((k for k in node.keywords
                       if k.arg == EMIT_KWARGS[name]), None)
            if kw is not None:
                _classify_emit_arg(kw.value, literals, offenders,
                                   node.lineno)
            else:
                offenders.append(
                    (node.lineno,
                     f"{name}() carries its verdict neither "
                     f"positionally nor as {EMIT_KWARGS[name]}="))
        elif isinstance(node, ast.Assign):
            # a conduit assigned anywhere feeds the emitted set — or
            # flags (attack-9 V8: a local named `verdict` was waved
            # through with no check on what it carried)
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in EMIT_CONDUITS:
                    v = node.value
                    if isinstance(v, ast.Constant) and \
                            isinstance(v.value, str) and \
                            MORPHOLOGY.match(v.value):
                        literals.add(v.value)
                    else:
                        # the factory idiom is a TUPLE unpack (`name,
                        # detail = ..._verdict(...)`), which never has
                        # a bare-Name target — so a single conduit
                        # Name assigned from anything non-literal is
                        # an offender, calls included
                        offenders.append(
                            (node.lineno,
                             f"conduit {tgt.id} assigned from "
                             f"{ast.dump(v)[:60]}"))
        elif isinstance(node, ast.FunctionDef):
            # EVERY tuple-returning function is scanned (attack-9
            # V10b: a factory not named *_verdict was invisible)
            for ret in ast.walk(node):
                if isinstance(ret, ast.Return) and \
                        isinstance(ret.value, ast.Tuple) and ret.value.elts:
                    e0 = ret.value.elts[0]
                    if isinstance(e0, ast.Constant) and \
                            isinstance(e0.value, str) and \
                            MORPHOLOGY.match(e0.value):
                        literals.add(e0.value)
                    elif node.name.endswith("_verdict"):
                        offenders.append((ret.lineno,
                                          "verdict factory returns "
                                          "non-literal name"))
    return literals, offenders


def emitted_verdicts():
    out = set()
    for script in SCRIPTS:
        lits, _ = emit_position_verdicts(
            script.read_text(encoding="utf-8"))
        out |= lits
    return out


# P6: a record-line GRAMMAR token can be a compound ALL-CAPS word
# without being a verdict (SWEEP_EXEMPT's own two literal forms —
# SKILL.md, Stop rule): a backtick-opened token immediately followed
# by a colon is the label-declaration shape every record grammar
# label in this file uses when quoted (INTENT:, SKILL:, Status:,
# Phase: — the sibling forms). A real verdict name is never written
# this way here: SEAL_PATH and UNIT_START_MISMATCH each gloss with a
# trailing colon too, but in bare prose, never inside a backtick —
# so this excludes only the label shape, never a bare or
# colon-less backtick-quoted verdict (e.g. `` `HALT_STATE` ``), which
# stays reachable.
GRAMMAR_LABEL_RE = re.compile(r"`([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+): ")


def skill_named_verdicts(text=None):
    if text is None:
        text = SKILL.read_text(encoding="utf-8")
    labels = set(GRAMMAR_LABEL_RE.findall(text))
    return set(VERDICT_TOKEN_RE.findall(text)) - labels


# ------------------------------------------------------- runtime battery

# the layer the AST cannot reach (this file's own honest-reach note,
# attack-9 N1: "a hand-rolled emit that rebuilds the verdict line
# without finish/Halt (V9) is invisible to any call-site analysis; the
# durable layer for that class is the runtime battery — drive each
# subcommand's error paths, grep the ACTUAL emitted verdict lines").

def parser_subcommands(script):
    """The subcommands a tool actually ACCEPTS, asked of its own
    parser: an unknown subcommand makes argparse render its choice
    list, which both tools route as a USAGE_ERROR verdict. Derived
    rather than restated, because a restated set cannot go stale
    loudly — it stays green while the tool grows a lane no battery row
    drives, which is the one thing the coverage assertion exists to
    catch. An unparseable message raises here instead of yielding a
    thin set: a coverage test over an empty declaration passes
    vacuously."""
    p = subprocess.run(
        [sys.executable, str(script), "__no_such_subcommand__"],
        capture_output=True, text=True, timeout=60)
    m = re.search(r"invalid choice:.*?\(choose from ([^)]*)\)", p.stdout)
    if m is None:
        raise RuntimeError(
            f"{Path(script).name}: no argparse choice list in the usage "
            f"error — the derivation lost its source.\n"
            f"stdout:\n{p.stdout}\nstderr:\n{p.stderr}")
    subs = set(re.findall(r"'([^']+)'", m.group(1)))
    if not subs:
        raise RuntimeError(f"{Path(script).name}: empty choice list in "
                           f"{m.group(1)!r}")
    return subs


GIT_SUBCOMMANDS = parser_subcommands(SCRIPTS[0])
RECORD_SUBCOMMANDS = parser_subcommands(SCRIPTS[1])

VERDICT_LINE_RE = re.compile(r"^STATIKER-(?:GIT|RECORD) VERDICT: (.*)$")


def lint_stage_codes(source_text):
    """E-M (BACKLOG; dev-notes/OBSERVATIONS.md, "the sweep prescribes
    a repair its own token resolver refuses", commit 271a6bf):
    `apply_supersession` is invoked exactly once, inside
    `parse_tracker`, over the violations `parse_tracker` itself
    accumulates before returning — its own `viol()` call sites, plus
    every code `hold_violations`/`write_set_violations` return (both
    invoked from inside `parse_tracker`'s own scan). No other function
    can ever contribute to the `violated` map that resolver-reachable
    codes are: a code minted anywhere else (`sweep_checks`, for
    instance) is refused by construction.

    Derived by walking those three functions' own ASTs — never
    restated — because a restated list cannot go stale loudly: it
    stays green while a code silently migrates to a later stage,
    which is exactly this defect one level up. String-literal codes
    only (`viol(code, ...)`'s first positional arg; each helper's
    `return [...]` list elements) — a code assembled at runtime would
    escape this and every other set in this suite alike."""
    tree = ast.parse(source_text)
    funcs = {n.name: n for n in ast.walk(tree)
             if isinstance(n, ast.FunctionDef)}
    for name in ("parse_tracker", "hold_violations", "write_set_violations"):
        if name not in funcs:
            raise RuntimeError(
                f"lint_stage_codes: {name}() not found — the derivation "
                f"lost its source")
    codes = set()
    for node in ast.walk(funcs["parse_tracker"]):
        if isinstance(node, ast.Call) and _call_name(node) == "viol":
            if node.args and isinstance(node.args[0], ast.Constant) and \
                    isinstance(node.args[0].value, str):
                codes.add(node.args[0].value)
    for name in ("hold_violations", "write_set_violations"):
        for node in ast.walk(funcs[name]):
            if isinstance(node, ast.Return) and \
                    isinstance(node.value, ast.List):
                for elt in node.value.elts:
                    if isinstance(elt, ast.Constant) and \
                            isinstance(elt.value, str):
                        codes.add(elt.value)
    return codes


def split_lines(text):
    """Split a tool's own stdout on newlines ONLY, mirroring
    statiker_record.py's split_lines: str.splitlines() also breaks on
    U+000C, U+2028 and U+0085, fabricating a line the process never
    printed and shifting every later line's meaning (the splitlines
    CLASS, closed here to close the reader's own reach — 2eb6b59)."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return [l[:-1] if l.endswith("\r") else l for l in lines]

# The battery's frozen remainder: emitted verdicts no row drives, each
# with the reason it cannot be driven. Asserted set-exact below, so
# this list is the only silent-under-report exit and editing it is a
# deliberate act. Every entry here is red-proven at function level or
# by a planted-defect run instead (the suites' pure-function classes).
# (0.2.49/ES-11: ADD_FAILED and GIT_ERROR left this list — the
# attack-11 attacker MEASURED both reasons false and supplied the
# recipes, which are battery rows below.)
UNDRIVEN_REMAINDER = {
    "INTERNAL_ERROR": "the never-a-silent-death catch-all; reaching it "
                      "is itself a tool defect",
    "HALT_NO_PATHSPEC": "emptying the pathspec means dropping the "
                        "tracker, which halts on the tracker first",
    "LOCK_COMMITTED_EXTRAS": "git's own pathspec commit is not known to "
                             "produce extras (function-level red)",
    "UNIT_COMMITTED_EXTRAS": "same as the lock seam's extras: no git "
                             "state is known to produce them",
}
# E-P: GATE_UNREADABLE retired from the remainder above — driven by
# run_battery's own substitute-record-tool rows (gate_unreadable_row),
# since a normal record-tool subprocess never produces it (the
# retired reason still holds for THAT path; the substitute path is
# what makes the verdict reachable at all).

TRACKER_REL = ".clippy/runs/t.md"
# the `## ` heading is load-bearing from 0.2.49 (ES-1): the
# requirement-head region runs from file start to the first one and
# parses no entries at all, so a heading-less fixture has no body.
CLOSED_TRACKER = """# Run: battery
Status: in-progress
Phase: implement

INTENT — battery fixture.

## Cycle 1
- D1 [COMMITTED] the design — basis: probe
- A1 [DISPATCHED] round 1 — basis: brief
- A1 [ZERO-DELTA] clean return — basis: report
"""


def battery_env():
    return {
        "PATH": os.environ["PATH"],
        "HOME": "/nonexistent",
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_CONFIG_SYSTEM": "/dev/null",
        "GIT_AUTHOR_NAME": "t",
        "GIT_AUTHOR_EMAIL": "t@t",
        "GIT_COMMITTER_NAME": "t",
        "GIT_COMMITTER_EMAIL": "t@t",
        "STATIKER_GIT_RETRY_BASE": "0.01",
        "LC_ALL": "C",
    }


def run_battery(git_script, record_script, root):
    """Drive every subcommand of both tools over a table of real
    invocations — happy paths, usage errors, unreadable and
    out-of-repo trackers, a malformed record, an in-repo artifact,
    stdin — and return one row per invocation:
    {tool, sub, argv, verdicts, returncode}. `verdicts` is every
    literal verdict NAME the process actually printed.

    Parameterized on the script paths so the instrument itself can be
    driven against a planted copy (its red arrangement)."""
    env = battery_env()
    root = Path(root)
    repo = root / "repo"
    (repo / ".clippy" / "runs").mkdir(parents=True)
    outside = root / "outside"          # deliberately NOT a repo
    outside.mkdir()

    def git(*a, cwd=repo, check=True):
        return subprocess.run(["git", *a], cwd=cwd, env=env,
                              capture_output=True, check=check)

    def scratch_repo(name, tracker=True):
        """A fresh repo with a base commit, for rows whose state would
        poison a shared one (staged collisions, halted operations,
        ignore rules, hooks, filters). The default tracker content is
        gate-clean (P2: lock-check/lock-commit now consult `sweep`
        BEFORE their own work, so a bare "# Run: t" tracker would halt
        LOCK_GATE_HOLDS before ever reaching the route each row
        exists to drive)."""
        d = root / name
        (d / ".clippy" / "runs").mkdir(parents=True)
        git("init", "-q", "-b", "main", cwd=d)
        (d / "base.txt").write_text("base\n")
        git("add", "base.txt", cwd=d)
        git("commit", "-m", "base", cwd=d)
        if tracker:
            (d / TRACKER_REL).write_text(
                "# Run: t\nStatus: in-progress\nPhase: implement\n")
        return d

    git("init", "-q", "-b", "main")
    (repo / "base.txt").write_text("base\n")
    git("add", "base.txt")
    git("commit", "-m", "base")
    (repo / TRACKER_REL).write_text(CLOSED_TRACKER)
    git("add", TRACKER_REL)
    git("commit", "-m", "lock")
    sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, env=env,
                         capture_output=True, text=True,
                         check=True).stdout.strip()
    # E-I: two dedicated pin fixtures, mutated on disk AFTER their own
    # commit — a genuine append (a real new line) and an IN-PLACE
    # status rewrite (the SAME line edited, B1's own red case:
    # SWEEP_CLEAN over a file `git diff --stat <pin>` reads 1+/1-)
    (repo / "pin_append.md").write_text(CLOSED_TRACKER)
    (repo / "pin_rewrite.md").write_text(
        CLOSED_TRACKER +
        "- F9 [PENDING] awaiting a leg — basis: dispatched\n")
    git("add", "pin_append.md", "pin_rewrite.md")
    git("commit", "-m", "pin fixtures")
    pin_sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, env=env,
                             capture_output=True, text=True,
                             check=True).stdout.strip()
    with (repo / "pin_append.md").open("a") as f:
        f.write("- F9 [VERIFIED] leg returned clean — basis: report\n")
    (repo / "pin_rewrite.md").write_text(
        CLOSED_TRACKER +
        "- F9 [VERIFIED] awaiting a leg — basis: dispatched\n")
    (repo / "docs").mkdir()
    (repo / "docs" / "a.txt").write_text("a\n")
    (repo / "holds.md").write_text(
        "# Run: h\nStatus: in-progress\nPhase: implement\n\n## Cycle 1\n"
        "- F1 [PENDING] awaiting a leg — basis: dispatched\n")
    (repo / "malformed.md").write_text(
        CLOSED_TRACKER +
        "- A2 BIT round 2 found the wrong mechanism — basis: report\n")
    (outside / "stray.md").write_text(
        "# Run: s\nStatus: in-progress\nPhase: implement\n\n## Cycle 1\n"
        "- F1 [VERIFIED] x — basis: y\n")
    (repo / "waves.md").write_text(
        CLOSED_TRACKER +
        "- F2 [VERIFIED] unit U1 write-set: src/a.txt — basis: design\n"
        "- F3 [VERIFIED] unit U2 write-set: src/b.txt — basis: design\n"
        "- F4 [VERIFIED] unit U3 write-set: src/a.txt — basis: design\n"
        "- D3 [AUTO-ACCEPTED] unit U4 gap: no write-set decided — "
        "basis: report\n")
    tracker_abs = str(repo / TRACKER_REL)

    def append_tracker():
        with (repo / TRACKER_REL).open("a") as f:
            f.write("- D2 [COMMITTED] record: bookkeeping — basis: probe\n")

    def make_src():
        (repo / "src.txt").write_text("unit output\n")

    # -- constructed repos for the halt/collision routes ---------------
    # (recipes lifted from the suites' fixtures: a conflicted merge, an
    # ignored tracker dir, a staged tracker, the drop handshake's two
    # halves, an untracked draft on the write-set, a mid-unit stage, a
    # stale index.lock, a red pre-commit hook, a noisy clean filter)

    r_state = scratch_repo("r_state")
    (r_state / "c.txt").write_text("main\n")
    git("add", "c.txt", cwd=r_state)
    git("commit", "-m", "c-main", cwd=r_state)
    git("checkout", "-q", "-b", "side", "HEAD~1", cwd=r_state)
    (r_state / "c.txt").write_text("side\n")
    git("add", "c.txt", cwd=r_state)
    git("commit", "-m", "c-side", cwd=r_state)
    git("checkout", "-q", "main", cwd=r_state)
    assert git("merge", "side", cwd=r_state, check=False).returncode != 0

    r_ignore = scratch_repo("r_ignore")
    (r_ignore / ".gitignore").write_text(".clippy/\n")
    git("add", ".gitignore", cwd=r_ignore)
    git("commit", "-m", "gi", cwd=r_ignore)

    r_coll = scratch_repo("r_coll")
    git("add", TRACKER_REL, cwd=r_coll)
    git("commit", "-m", "tracker", cwd=r_coll)
    # P2: the staged edit's own on-disk content must stay gate-clean —
    # lock-check now consults sweep BEFORE its own tracker-collision
    # check, over whatever the tracker currently holds on disk.
    (r_coll / TRACKER_REL).write_text(
        "# Run: t\nStatus: in-progress\nPhase: implement\nedit\n")
    git("add", TRACKER_REL, cwd=r_coll)

    r_drops = scratch_repo("r_drops")
    (r_drops / "art.txt").write_text("operator staged\n")
    git("add", "art.txt", cwd=r_drops)

    r_stale = scratch_repo("r_stale")
    (r_stale / "art.txt").write_text("run content\n")

    r_repin = scratch_repo("r_repin")

    # P30: verify-gate's CLEAN/STALE pair — a fixed final state so
    # both rows are order-independent (neither row itself commits).
    r_verify_gate = scratch_repo("r_verify_gate")
    verify_gate_sha1 = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=r_verify_gate, env=env,
        capture_output=True, text=True, check=True).stdout.strip()
    (r_verify_gate / "extra.txt").write_text("landed during a verify leg\n")
    git("add", "extra.txt", cwd=r_verify_gate)
    git("commit", "-m", "landed during leg", cwd=r_verify_gate)
    verify_gate_sha2 = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=r_verify_gate, env=env,
        capture_output=True, text=True, check=True).stdout.strip()

    r_unit = scratch_repo("r_unit", tracker=False)
    (r_unit / ".gitignore").write_text("build/\n")
    (r_unit / "settled.txt").write_text("settled\n")
    git("add", ".gitignore", "settled.txt", cwd=r_unit)
    git("commit", "-m", "settled", cwd=r_unit)
    (r_unit / "draft.txt").write_text("operator draft\n")
    (r_unit / "staged.txt").write_text("OPERATOR PRECIOUS\n")
    git("add", "staged.txt", cwd=r_unit)
    r_unit_head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=r_unit, env=env,
        capture_output=True, text=True, check=True).stdout.strip()
    (r_unit / "units.md").write_text(
        CLOSED_TRACKER +
        "- F2 [VERIFIED] unit U1 write-set: draft.txt — basis: design\n"
        "- F3 [VERIFIED] unit U2 write-set: build/x.txt — basis: design\n"
        "- F4 [VERIFIED] unit U3 write-set: staged.txt — basis: design\n"
        "- F5 [VERIFIED] unit U4 write-set: settled.txt — basis: design\n")

    r_lock = scratch_repo("r_lock", tracker=False)
    (r_lock / "src.txt").write_text("unit output\n")
    (r_lock / ".git" / "index.lock").write_text("")
    r_lock_head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=r_lock, env=env,
        capture_output=True, text=True, check=True).stdout.strip()
    (r_lock / "unit.md").write_text(
        CLOSED_TRACKER +
        "- F2 [VERIFIED] unit U1 write-set: src.txt — basis: design\n")

    r_hook = scratch_repo("r_hook")
    hook = r_hook / ".git" / "hooks" / "pre-commit"
    hook.write_text("#!/bin/sh\necho 'pre-commit: suite failed' >&2\nexit 1\n")
    hook.chmod(0o755)

    def noisy(d):
        git("config", "filter.noisy.clean", "sh -c 'cat; date +%s%N'", cwd=d)
        (d / ".gitattributes").write_text("*.md filter=noisy\n")
        git("add", ".gitattributes", cwd=d)
        git("commit", "-m", "attr", cwd=d)

    r_noisy = scratch_repo("r_noisy")
    noisy(r_noisy)
    r_noisy_unit = scratch_repo("r_noisy_unit", tracker=False)
    noisy(r_noisy_unit)
    (r_noisy_unit / "note.md").write_text("unit output\n")
    r_noisy_unit_head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=r_noisy_unit, env=env,
        capture_output=True, text=True, check=True).stdout.strip()
    (r_noisy_unit / "unit.md").write_text(
        CLOSED_TRACKER +
        "- F2 [VERIFIED] unit U1 write-set: note.md — basis: design\n")

    # ES-11's unfrozen pair, on the attack-11 attacker's own recipes:
    # a path git refuses though containment accepts it (ADD_FAILED at
    # lock-check's dry-run adds), and a corrupt index (GIT_ERROR out
    # of preflight's dedicated, STRICT repo-health read)
    r_addfail = scratch_repo("r_addfail")
    (r_addfail / "realdir").mkdir()
    (r_addfail / "realdir" / "x.txt").write_text("run content\n")
    os.symlink("realdir", r_addfail / "linkdir")

    r_corrupt = scratch_repo("r_corrupt")
    (r_corrupt / ".git" / "index").write_bytes(b"GARBAGE-NOT-AN-INDEX")

    # the worktree lane: provisioning registers .git/worktrees state in
    # the repo it runs from, so it gets its own repo rather than
    # poisoning the shared one. The provisioned path is a SIBLING of
    # that repo — repo.outside() halts on anything under the top.
    r_wt = scratch_repo("r_wt", tracker=False)
    wt_sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=r_wt, env=env,
                            capture_output=True, text=True,
                            check=True).stdout.strip()
    wt_path = str(root / "wt_r_wt")

    # -- record-side trackers, read-only rows over the main repo -------
    (repo / "absent.md").write_text(
        # P27: a bare [BIT] round with no design-amending disposition
        # grades SATISFIED — a trailing D-line change keeps this
        # fixture a genuine CLOSURE_ABSENT case
        "# Run: a\nStatus: in-progress\nPhase: implement\n\n## Cycle 1\n"
        "- A1 [DISPATCHED] round 1 — basis: brief\n"
        "- A1 [BIT] two findings — basis: report\n"
        "- D1 [INVALIDATED] the design changes — basis: F1\n")
    (repo / "void.md").write_text(
        CLOSED_TRACKER +
        "- F9 [INVALIDATED] the premise died — basis: probe\n")
    (repo / "held.md").write_text(
        CLOSED_TRACKER +
        "- D9 [AUTO-ACCEPTED] unit U2 held: x.txt — basis: F9\n")
    (repo / "leavings.md").write_text(
        CLOSED_TRACKER +
        "- F9 [VERIFIED] out-of-scope: spread CLV has never computed — "
        "basis: probe\n")
    (repo / "sustain_denied.md").write_text(
        "# Run: sd\nStatus: in-progress\nPhase: investigate-design\n\n"
        "## Cycle 1\n"
        "- A1 [DISPATCHED] round 1 — basis: brief\n"
        "- F1 [VERIFIED] record: a bookkeeping note — basis: probe\n"
        "- A1 [BIT] one record-class finding — basis: report\n")
    (repo / "sustain_ok.md").write_text(
        "# Run: so\nStatus: in-progress\nPhase: investigate-design\n\n"
        "## Cycle 1\n"
        "- A1 [DISPATCHED] round 1 — basis: brief\n"
        "- F1 [VERIFIED] a genuine design finding — basis: probe\n"
        "- A1 [BIT] one finding — basis: report\n")
    (repo / "tripwire.md").write_text(
        "# Run: tw\nStatus: in-progress\nPhase: investigate-design\n\n"
        "## Cycle 1\n"
        "- A1 [DISPATCHED] round 1 — basis: brief\n"
        "- A1 [BIT] one finding — basis: report\n"
        "- A2 [DISPATCHED] round 2 — basis: brief\n"
        "- A2 [BIT] one finding — basis: report\n"
        "- A3 [DISPATCHED] round 3 — basis: brief\n"
        "- A3 [BIT] one finding — basis: report\n")

    # -- P2 gate-seam fixtures: the record's declared write-set is now
    # the unit-seam source, consulted through the record-tool gate ----
    (repo / "unitgate.md").write_text(
        CLOSED_TRACKER +
        "- F2 [VERIFIED] unit U1 write-set: src.txt — basis: design\n"
        "- F3 [VERIFIED] unit U2 write-set: ../outside.py — basis: design\n"
        "- F4 [VERIFIED] unit U3 write-set: never-made.txt — basis: design\n"
        "- F5 [VERIFIED] unit U6 write-set: mismatch.txt — basis: design\n")
    (repo / "selfname.md").write_text(
        CLOSED_TRACKER +
        "- F2 [VERIFIED] unit U1 write-set: selfname.md — basis: design\n")
    # UNIT_START_MISMATCH's foreign touch: committed AFTER `sha` (the
    # start-sha the U1/U6 rows below reuse), so `git log sha..HEAD --
    # mismatch.txt` is non-empty by the time the mismatch row runs.
    (repo / "mismatch.txt").write_text("foreign touch\n")
    git("add", "mismatch.txt")
    git("commit", "-m", "foreign touch on mismatch.txt")

    # LOCK_GATE_HOLDS: a tracker sweep itself holds on (missing
    # Status/Phase) — own repo, since lock-check now consults sweep
    # BEFORE any of its own work.
    r_gate = scratch_repo("r_gate")
    (r_gate / TRACKER_REL).write_text("# Run: bad\n")

    # (tool, subcommand, argv, cwd, stdin, prep)
    table = [
        ("git", "state-gate", ["state-gate"], repo, None, None),
        # outside every repo: the NOT_A_REPO path
        ("git", "state-gate", ["state-gate"], outside, None, None),
        ("git", "preflight", ["preflight", "--tracker", TRACKER_REL],
         repo, None, None),
        ("git", "preflight", ["preflight"], repo, None, None),
        ("git", "lock-check", ["lock-check", "--tracker", TRACKER_REL],
         repo, None, None),
        ("git", "lock-check", ["lock-check", "--tracker", TRACKER_REL,
                               "--lock-set", "docs"], repo, None, None),
        ("git", "lock-commit", ["lock-commit", "--tracker", TRACKER_REL,
                                "-m", "lock"], repo, None, append_tracker),
        ("git", "unit-start", ["unit-start", "--tracker",
                               str(repo / "unitgate.md"), "--unit", "U1"],
         repo, None, None),
        ("git", "unit-start", ["unit-start", "--tracker",
                               str(repo / "unitgate.md"), "--unit", "U2"],
         repo, None, None),
        ("git", "unit-commit", ["unit-commit", "--tracker",
                                str(repo / "unitgate.md"), "--unit", "U1",
                                "--start-sha", sha, "-m", "unit U1"],
         repo, None, make_src),
        ("git", "unit-commit", ["unit-commit", "--tracker",
                                str(repo / "unitgate.md"), "--unit", "U3",
                                "--start-sha", sha, "-m", "unit U3"],
         repo, None, None),
        # P2: UNIT_GATE_BLOCKED (a held unit), WRITE_SET_NAMES_TRACKER
        # (the declared write-set names the tracker itself),
        # UNIT_START_MISMATCH (a foreign commit touched the declared
        # write-set since the stale start-sha), SEAL_PATH (P1)
        ("git", "unit-start", ["unit-start", "--tracker",
                               str(repo / "held.md"), "--unit", "U2"],
         repo, None, None),
        ("git", "unit-start", ["unit-start", "--tracker",
                               str(repo / "selfname.md"), "--unit", "U1"],
         repo, None, None),
        ("git", "unit-commit", ["unit-commit", "--tracker",
                                str(repo / "unitgate.md"), "--unit", "U6",
                                "--start-sha", sha, "-m", "unit U6"],
         repo, None, None),
        ("git", "seal-path", ["seal-path", "--tracker", TRACKER_REL,
                              "--round", "A1"], repo, None, None),
        ("record", "lint", ["lint", "--tracker", tracker_abs],
         repo, None, None),
        ("record", "lint", ["lint", "--tracker", str(repo / "nope.md")],
         repo, None, None),
        ("record", "lint", ["lint", "--tracker", str(outside / "stray.md")],
         repo, None, None),
        ("record", "sweep", ["sweep", "--tracker", str(repo / "holds.md")],
         repo, None, None),
        ("record", "sweep", ["sweep"], repo, None, None),
        ("record", "closure", ["closure", "--tracker",
                               str(repo / "malformed.md")],
         repo, None, None),
        ("record", "closure", ["closure", "--tracker", tracker_abs],
         repo, None, None),
        ("record", "closure", ["closure", "--tracker", tracker_abs,
                               "--unit", "3"], repo, None, None),
        ("record", "closure", ["closure", "--tracker",
                               str(repo / "leavings.md")], repo, None, None),
        ("record", "filter", ["filter", "--tracker", tracker_abs,
                              "--sha", sha, "--out", str(repo / "art.md")],
         repo, None, None),
        ("record", "filter", ["filter", "--tracker", tracker_abs,
                              "--sha", sha,
                              "--out", str(outside / "art.md")],
         repo, None, None),
        ("record", "filter", ["filter", "--tracker", tracker_abs,
                              "--sha", "deadbeef",
                              "--out", str(outside / "art2.md")],
         repo, None, None),
        ("record", "pinned", ["pinned", "--tracker",
                              str(repo / "pin_append.md"), "--sha", pin_sha],
         repo, None, None),
        ("record", "pinned", ["pinned", "--tracker",
                              str(repo / "pin_rewrite.md"), "--sha", pin_sha],
         repo, None, None),
        ("record", "quote", ["quote", "--label", "A1 quotes"], repo,
         "a report line holding [VERIFIED]\n", None),
        ("record", "verify-gate", ["verify-gate", "--tracker", TRACKER_REL,
                                   "--sha", verify_gate_sha2],
         r_verify_gate, None, None),
        ("record", "verify-gate", ["verify-gate", "--tracker", TRACKER_REL,
                                   "--sha", verify_gate_sha1],
         r_verify_gate, None, None),

        # -- the halt/collision routes, each in its own repo ----------
        ("git", "state-gate", ["state-gate"], r_state, None, None),
        ("git", "lock-check", ["lock-check", "--tracker", TRACKER_REL],
         r_state, None, None),
        ("git", "preflight", ["preflight", "--tracker", TRACKER_REL],
         r_ignore, None, None),
        ("git", "lock-check", ["lock-check", "--tracker", TRACKER_REL],
         r_ignore, None, None),
        ("git", "lock-check", ["lock-check", "--tracker", TRACKER_REL],
         r_coll, None, None),
        ("git", "lock-check", ["lock-check", "--tracker", TRACKER_REL,
                               "--lock-set", "art.txt"], r_drops, None, None),
        ("git", "lock-commit", ["lock-commit", "--tracker", TRACKER_REL,
                                "--lock-set", "art.txt", "-m", "lock"],
         r_drops, None, None),
        ("git", "lock-commit", ["lock-commit", "--tracker", TRACKER_REL,
                                "--lock-set", "art.txt", "--drop", "art.txt",
                                "-m", "lock"], r_stale, None, None),
        ("git", "lock-commit", ["lock-commit", "--tracker", TRACKER_REL,
                                "-m", "pin"], r_repin, None, None),
        ("git", "lock-commit", ["lock-commit", "--tracker", TRACKER_REL,
                                "-m", "pin again"], r_repin, None, None),
        ("git", "lock-commit", ["lock-commit", "--tracker", TRACKER_REL,
                                "-m", "lock"], r_hook, None, None),
        ("git", "lock-commit", ["lock-commit", "--tracker", TRACKER_REL,
                                "-m", "lock"], r_noisy, None, None),
        ("git", "lock-check", ["lock-check", "--tracker", TRACKER_REL],
         r_gate, None, None),
        ("git", "unit-start", ["unit-start", "--tracker",
                               str(r_unit / "units.md"), "--unit", "U1"],
         r_unit, None, None),
        ("git", "unit-start", ["unit-start", "--tracker",
                               str(r_unit / "units.md"), "--unit", "U2"],
         r_unit, None, None),
        ("git", "unit-commit", ["unit-commit", "--tracker",
                                str(r_unit / "units.md"), "--unit", "U3",
                                "--start-sha", r_unit_head, "-m", "unit U1"],
         r_unit, None, None),
        ("git", "unit-commit", ["unit-commit", "--tracker",
                                str(r_unit / "units.md"), "--unit", "U4",
                                "--start-sha", r_unit_head, "-m", "unit U2"],
         r_unit, None, None),
        ("git", "unit-commit", ["unit-commit", "--tracker",
                                str(r_lock / "unit.md"), "--unit", "U1",
                                "--start-sha", r_lock_head, "-m", "unit U1"],
         r_lock, None, None),
        ("git", "unit-commit", ["unit-commit", "--tracker",
                                str(r_noisy_unit / "unit.md"), "--unit", "U1",
                                "--start-sha", r_noisy_unit_head,
                                "-m", "unit U1"], r_noisy_unit, None, None),
        ("git", "lock-check", ["lock-check", "--tracker", TRACKER_REL,
                               "--lock-set", "linkdir/x.txt"],
         r_addfail, None, None),
        ("git", "preflight", ["preflight", "--tracker", TRACKER_REL],
         r_corrupt, None, None),

        # -- the worktree lane: add, remove, and the containment halt --
        # ordered: the remove row consumes the worktree the add row
        # provisions, and the halt row runs last on a path INSIDE r_wt
        ("git", "worktree-add", ["worktree-add", "--sha", wt_sha,
                                 "--path", wt_path], r_wt, None, None),
        ("git", "worktree-remove", ["worktree-remove", "--path", wt_path],
         r_wt, None, None),
        ("git", "worktree-add", ["worktree-add", "--sha", wt_sha,
                                 "--path", "inner-wt"], r_wt, None, None),

        # -- the record-side routes ----------------------------------
        ("record", "lint", ["lint", "--tracker", str(repo / "malformed.md")],
         repo, None, None),
        ("record", "sweep", ["sweep", "--tracker", tracker_abs],
         repo, None, None),
        ("record", "closure", ["closure", "--tracker",
                               str(repo / "absent.md")], repo, None, None),
        ("record", "closure", ["closure", "--tracker", str(repo / "void.md")],
         repo, None, None),
        ("record", "closure", ["closure", "--tracker", str(repo / "held.md"),
                               "--unit", "U2"], repo, None, None),
        # tracker_abs (CLOSED_TRACKER) scopes no unit at all — E-B:
        # U2 is therefore UNKNOWN here, not dispatchable
        ("record", "closure", ["closure", "--tracker", tracker_abs,
                               "--unit", "U2"], repo, None, None),
        # E-B: an id the tracker never scoped halts UNIT_UNKNOWN, kept
        # distinct from the row above (a different tracker, same class)
        ("record", "closure", ["closure", "--tracker", str(repo / "held.md"),
                               "--unit", "U9"], repo, None, None),
        # waves.md's U1 is a genuinely KNOWN, non-held unit — drives
        # UNIT_DISPATCHABLE now that an unscoped id no longer does
        ("record", "closure", ["closure", "--tracker", str(repo / "waves.md"),
                               "--unit", "U1"], repo, None, None),
        ("record", "waves", ["waves", "--tracker", str(repo / "waves.md")],
         repo, None, None),
        ("record", "waves", ["waves", "--tracker",
                             str(repo / "malformed.md")], repo, None, None),
        ("record", "trend", ["trend", "--tracker", tracker_abs],
         repo, None, None),
        ("record", "trend", ["trend", "--tracker", str(repo / "holds.md")],
         repo, None, None),
        ("record", "trend", ["trend", "--tracker",
                             str(repo / "malformed.md")], repo, None, None),
        ("record", "sustain", ["sustain", "--tracker", tracker_abs],
         repo, None, None),
        ("record", "sustain", ["sustain", "--tracker",
                               str(repo / "sustain_denied.md")],
         repo, None, None),
        ("record", "sustain", ["sustain", "--tracker",
                               str(repo / "sustain_ok.md")], repo, None, None),
        ("record", "sustain", ["sustain", "--tracker",
                               str(repo / "malformed.md")], repo, None, None),
        ("record", "tripwire", ["tripwire", "--tracker",
                                str(repo / "tripwire.md"),
                                "--threshold", "2"], repo, None, None),
        ("record", "tripwire", ["tripwire", "--tracker",
                                str(repo / "tripwire.md"),
                                "--threshold", "20"], repo, None, None),
        ("record", "tripwire", ["tripwire", "--tracker",
                                str(repo / "malformed.md"),
                                "--threshold", "1"], repo, None, None),
    ]

    rows = []
    for tool, sub, argv, cwd, stdin, prep in table:
        if prep is not None:
            prep()
        script = git_script if tool == "git" else record_script
        p = subprocess.run([sys.executable, str(script), *argv],
                           cwd=str(cwd), env=env, input=stdin,
                           capture_output=True, text=True, timeout=60)
        verdicts = []
        for line in split_lines(p.stdout):
            m = VERDICT_LINE_RE.match(line)
            if m:
                verdicts.append(re.search(r'"verdict":\s*"([^"]+)"',
                                          m.group(1)).group(1))
        rows.append({"tool": tool, "sub": sub, "argv": argv,
                     "verdicts": verdicts, "returncode": p.returncode,
                     "stdout": p.stdout, "stderr": p.stderr})

    # E-P: GATE_UNREADABLE is real only when gate_consult's own
    # subprocess path breaks — the record tool always emits a
    # well-formed verdict line by design (this file's own
    # UNDRIVEN_REMAINDER reason, now retired), so driving this route
    # needs a SUBSTITUTE record-tool path: `_RECORD_SCRIPT`
    # (statiker_git.py) resolves relative to the running git script's
    # OWN directory, so a scratch copy of the git tool beside a
    # stand-in statiker_record.py redirects it with no source change —
    # one stand-in prints garbage (no verdict line), the other an
    # unparseable verdict line; both drive lock-check's own sweep
    # consult, the only gate_consult call site.
    def gate_unreadable_row(name, stub_body):
        d = root / name
        d.mkdir()
        shutil.copy(git_script, d / "statiker_git.py")
        # statiker_git.py imports its sibling statiker_emit at
        # _SCRIPTS_DIR too — omitted, the scratch copy dies
        # ModuleNotFoundError before ever reaching gate_consult
        shutil.copy(git_script.parent / "statiker_emit.py",
                    d / "statiker_emit.py")
        (d / "statiker_record.py").write_text(stub_body)
        r = scratch_repo(f"{name}_repo")
        argv = ["lock-check", "--tracker", TRACKER_REL]
        p = subprocess.run(
            [sys.executable, str(d / "statiker_git.py"), *argv],
            cwd=str(r), env=env, capture_output=True, text=True, timeout=60)
        verdicts = []
        for line in split_lines(p.stdout):
            m = VERDICT_LINE_RE.match(line)
            if m:
                verdicts.append(re.search(r'"verdict":\s*"([^"]+)"',
                                          m.group(1)).group(1))
        rows.append({"tool": "git", "sub": "lock-check", "argv": argv,
                     "verdicts": verdicts, "returncode": p.returncode,
                     "stdout": p.stdout, "stderr": p.stderr})

    gate_unreadable_row(
        "gu_garbage",
        "#!/usr/bin/env python3\nprint('garbage, no verdict line here')\n")
    gate_unreadable_row(
        "gu_badjson",
        "#!/usr/bin/env python3\n"
        "print('STATIKER-RECORD VERDICT: {not valid json')\n")

    return rows


class TestRuntimeVerdictBattery(unittest.TestCase):
    """The emit contract checked at RUNTIME: whatever a process
    actually prints on a verdict line is a verdict SKILL.md routes.
    Call-site analysis cannot see a hand-rolled emit (this file's
    honest-reach note); driving the scripts can.

    Red arrangement (run once, not committed): a scratch copy of
    statiker_record.py with a hand-rolled
    `say(VERDICT_PREFIX + json.dumps({"verdict": "SECRET_UNROUTED"}))`
    planted on the TRACKER_UNREADABLE path, run_battery pointed at the
    copy — the battery reports SECRET_UNROUTED as unrouted. The
    committed battery drives the real scripts."""

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.rows = run_battery(SCRIPTS[0], SCRIPTS[1], cls._tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_every_observed_verdict_is_routed_in_skill(self):
        named = skill_named_verdicts()
        unrouted = {}
        for row in self.rows:
            for v in row["verdicts"]:
                if v not in named:
                    unrouted.setdefault(v, " ".join(row["argv"]))
        self.assertEqual(
            unrouted, {},
            f"emitted at runtime, named nowhere in SKILL.md: {unrouted}")

    def test_every_invocation_emits_exactly_one_verdict_line(self):
        # not one row may go silent — a battery whose rows print
        # nothing would satisfy the routing assertion vacuously
        for row in self.rows:
            self.assertEqual(
                len(row["verdicts"]), 1,
                f"{row['tool']} {' '.join(row['argv'])} printed "
                f"{row['verdicts']}\nstdout:\n{row['stdout']}\n"
                f"stderr:\n{row['stderr']}")

    def test_the_battery_reader_survives_a_separator_in_the_verdict_json(self):
        # closes the splitlines CLASS in this file's own reader
        # (BACKLOG.md, "close the splitlines CLASS in the remaining
        # verdict readers"): the record tool's verdict JSON carries
        # violation text VERBATIM (ensure_ascii=False) — a U+2028 in a
        # tracker's own Status line reaches the verdict line raw, and
        # str.splitlines() would read it as a second physical line,
        # severing the JSON split_lines correctly keeps whole (mirrors
        # test_statiker_record.py's
        # test_the_fixture_reader_survives_a_separator_in_the_block).
        repo = Path(self._tmp.name) / "repo"
        tracker = repo / "u2028.md"
        tracker.write_text(
            "# Run: t\n"
            "Status: bogus status\n"
            "Phase: investigate-design\n"
            "Skill: statiker 0.2.60\n\n"
            "## Cycle 1\n")
        p = subprocess.run(
            [sys.executable, str(SCRIPTS[1]), "lint", "--tracker",
             str(tracker)],
            cwd=str(repo), env=battery_env(), capture_output=True,
            text=True, timeout=60)
        verdict_lines = [l for l in split_lines(p.stdout)
                         if l.startswith("STATIKER-RECORD VERDICT: ")]
        self.assertEqual(len(verdict_lines), 1, p.stdout)
        self.assertIn(" ", verdict_lines[0], verdict_lines[0])
        m = re.search(r'"verdict":\s*"([^"]+)"', verdict_lines[0])
        self.assertEqual(m.group(1), "LINT_VIOLATIONS", verdict_lines[0])

    def test_battery_covers_every_subcommand_of_both_tools(self):
        for tool, declared in (("git", GIT_SUBCOMMANDS),
                               ("record", RECORD_SUBCOMMANDS)):
            seen = {r["sub"] for r in self.rows if r["tool"] == tool}
            self.assertEqual(seen, declared,
                             f"{tool}: battery misses {declared - seen}")

    def test_every_emitted_verdict_is_driven_or_frozen(self):
        # the battery's own REACH, made enumerable: a verdict the AST
        # sees is either observed in a real subprocess run above or
        # named in the frozen remainder with the reason it cannot be.
        # Set-exact in both directions, so a newly added verdict fails
        # this test until it is consciously placed — the honest-reach
        # note's "an emit on a path no battery row drives" stops being
        # a paragraph and becomes a list someone has to edit.
        observed = {v for r in self.rows for v in r["verdicts"]}
        undriven = emitted_verdicts() - observed
        self.assertEqual(
            undriven, set(UNDRIVEN_REMAINDER),
            "undriven verdicts and the frozen remainder disagree — "
            "drive the new one with a battery row, or add it to "
            "UNDRIVEN_REMAINDER with the reason no row can")

    def test_battery_reaches_error_paths_not_only_happy_ones(self):
        # the instrument is live only if it drives the halt/usage
        # routes the AST-blind class hides on
        observed = {v for r in self.rows for v in r["verdicts"]}
        for expected in ("USAGE_ERROR", "NOT_A_REPO", "PATH_OUTSIDE_REPO",
                         "TRACKER_UNREADABLE", "PIN_UNREADABLE",
                         "ARTIFACT_IN_REPO", "CLOSURE_RECORD_MALFORMED"):
            self.assertIn(expected, observed)

    def test_gate_unreadable_drives_on_the_substitute_rows_only(self):
        # E-P: both garbage-output and unparseable-JSON stand-ins
        # must fire GATE_UNREADABLE; every OTHER row in the battery —
        # every ordinary lock-check/lock-commit against the real
        # record tool, "a healthy consult" — must not, including the
        # r_gate row that already halts LOCK_GATE_HOLDS on a
        # malformed tracker (a different, non-GATE_UNREADABLE defect)
        firing = [r for r in self.rows if "GATE_UNREADABLE" in r["verdicts"]]
        self.assertEqual(len(firing), 2, firing)
        for r in firing:
            self.assertEqual(r["tool"], "git")
            self.assertEqual(r["sub"], "lock-check")
        others = [r for r in self.rows if r not in firing]
        self.assertTrue(others)  # instrument check: the control set is real
        for r in others:
            self.assertNotIn("GATE_UNREADABLE", r["verdicts"], r)


class TestVerdictParity(unittest.TestCase):
    def test_every_emitted_verdict_is_routed_in_skill(self):
        missing = emitted_verdicts() - skill_named_verdicts()
        self.assertEqual(
            missing, set(),
            f"emitted by a script, named nowhere in SKILL.md: "
            f"{sorted(missing)} — route it or add it to a catch-all's "
            f"parenthetical")

    def test_every_skill_named_verdict_is_emitted(self):
        phantom = skill_named_verdicts() - emitted_verdicts()
        self.assertEqual(
            phantom, set(),
            f"named in SKILL.md, emitted by no script: {sorted(phantom)}")

    def test_backtick_quoted_grammar_token_is_not_a_phantom_verdict(self):
        # P6: SWEEP_EXEMPT is a record-line grammar label (SKILL.md,
        # Stop rule), not a verdict — its own two backtick-quoted
        # literal forms must not read as an unemitted verdict name
        self.assertNotIn("SWEEP_EXEMPT", skill_named_verdicts())

    def test_grammar_label_exclusion_is_shape_specific(self):
        # the fix's own red case: only the backtick-opened,
        # colon-suffixed LABEL shape is excluded — a verdict quoted
        # bare in backticks, or glossed with a trailing colon OUTSIDE
        # backticks (SEAL_PATH's and UNIT_START_MISMATCH's own real
        # shape), stays reachable; a real defect here would either
        # eat a genuine verdict or let a new grammar label back in as
        # a phantom
        named = skill_named_verdicts(
            "`BARE_VERDICT` stays. GLOSSED_VERDICT: outside "
            "backticks stays. `LABEL_FORM: <x>` excludes.")
        self.assertIn("BARE_VERDICT", named)
        self.assertIn("GLOSSED_VERDICT", named)
        self.assertNotIn("LABEL_FORM", named)

    def test_emit_positions_are_literal_verdicts(self):
        # attack-8 V3/V4b: a name assembled at emit time, or one
        # breaking verdict morphology, is invisible to name parity —
        # so the emit positions themselves are the checked surface
        for script in SCRIPTS:
            _, offenders = emit_position_verdicts(
                script.read_text(encoding="utf-8"))
            self.assertEqual(
                offenders, [],
                f"{script.name}: emit-position args that are not "
                f"morphology-passing literals or declared conduits")

    def test_subcommand_derivation_is_live(self):
        # instrument check on the pair: a lane the parser really
        # carries is present, and the probe's own sentinel is not — a
        # set derived from neither would satisfy the coverage
        # assertion whatever the tool offers
        self.assertIn("worktree-add", GIT_SUBCOMMANDS)
        self.assertNotIn("__no_such_subcommand__", GIT_SUBCOMMANDS)
        # the record tool registers four of its lanes from a LOOP
        # variable, so a source-literal scan would miss them; the
        # parser answers for those the same as for the rest
        self.assertLessEqual({"lint", "sweep", "waves", "trend", "quote"},
                             RECORD_SUBCOMMANDS)
        self.assertNotIn("__no_such_subcommand__", RECORD_SUBCOMMANDS)

    def test_extractor_is_live(self):
        # instrument check: the extractor matches known positives from
        # every source kind — direct finish, Halt raise, retry-helper
        # arg, and factory return
        got = emitted_verdicts()
        for known in ("USAGE_ERROR", "GIT_ERROR", "ADD_FAILED",
                      "LOCK_COMMITTED_EXTRAS", "CLOSURE_RECORD_MALFORMED"):
            self.assertIn(known, got)
        self.assertIn("HALT_STATE", skill_named_verdicts())


class TestRepairFormReachability(unittest.TestCase):
    """E-M (BACKLOG; dev-notes/OBSERVATIONS.md 271a6bf): a
    REPAIR_FORMS entry that prints the `corrects line {n}` token
    promises the desk a repair `apply_supersession` can resolve — a
    promise only LINT-stage-reachable codes can keep, since that
    resolver's `violated` map is built once, from `parse_tracker`'s
    own scan, before any SWEEP-stage code (`sweep_checks`) exists.
    This suite's own reachable set is DERIVED (`lint_stage_codes`,
    above), never restated, so a code migrating stage in either
    direction moves this assertion with it rather than leaving it
    silently stale."""

    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(SCRIPTS[1].parent))
        import statiker_record
        cls.record = statiker_record

    def test_corrects_token_only_on_lint_stage_reachable_codes(self):
        reachable = lint_stage_codes(SCRIPTS[1].read_text(encoding="utf-8"))
        unreachable = sorted(
            code for code, form in self.record.REPAIR_FORMS.items()
            if "corrects line {n}" in form and code not in reachable)
        self.assertEqual(
            unreachable, [],
            f"REPAIR_FORMS prints the `corrects line <n>` token on a "
            f"code apply_supersession's violated map can never contain "
            f"(computed at LINT stage only, before these codes exist): "
            f"{unreachable} — the printed repair can never resolve")

    def test_instrument_is_live(self):
        # instrument check on the pair: a code the derivation really
        # carries is present, and a sentinel it never emitted is
        # absent — a set derived from neither would satisfy the
        # reachability assertion whatever the tool offers
        reachable = lint_stage_codes(SCRIPTS[1].read_text(encoding="utf-8"))
        self.assertIn("hold-form", reachable)
        self.assertIn("write-set-near-miss", reachable)
        self.assertNotIn("__no_such_code__", reachable)


if __name__ == "__main__":
    unittest.main(verbosity=1)

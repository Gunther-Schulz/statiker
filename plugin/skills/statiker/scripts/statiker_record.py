#!/usr/bin/env python3
"""statiker-record — the record-grammar machinery of the statiker
skill: tracker lint, the [READY] sweep's computable slice, the
closure predicate, the attack-artifact filter, and defanged quote
production (provenance: record/instrument findings of draft attacks
1-6, dev-notes/OBSERVATIONS.md in the source repo; test suite:
tools/test_statiker_record.py there).

Subcommands (each prints evidence lines, then exactly one final line
`STATIKER-RECORD VERDICT: {json}` — the desk books that line):

  lint    --tracker P                 grammar/header/defang checks
  sweep   --tracker P                 lint + the [READY] gate's
                                      computable slice; judgment
                                      residue is NAMED, never absorbed
  closure --tracker P [--unit U<k>]   closure predicate + per-unit
                                      dispatchability
  filter  --tracker P --sha S --out F pinned attack artifact (reads
                                      the sha, drops the two
                                      Superseded species)
  quote   --label "A<n> quotes"       stdin -> defanged quoted block

The tag contract is anchored on the stats reader's own greps
(clippy-stats source, read 2026-08-07): Status/Phase enums admit in
the first ~20 lines; [AUTO-ACCEPTED], [PASSED], [ISSUES FOUND] are
counted UNANCHORED — which is why a bracketed tag literal anywhere
outside an entry's leading tag position is a defect, and why defang
drops brackets AND lowercases.

Judgment stays with the desk: body-reads of dead bases, duplicate-id
body-reads, restatement adoption checks, basis reach. The sweep
names that residue in its evidence lines; a clean verdict here is
the computable slice only.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass

VERDICT_PREFIX = "STATIKER-RECORD VERDICT: "

# Exit codes mirror the git tool: 0 = proceedable, 2 = holds/voids,
# 3 = usage or internal error — and the verdict-line guarantee covers
# usage errors (attack-7 B1: the git tool's repair had not been
# carried across; a bare argparse death on exit 2 read as a hold).

STATUS_ENUM = {"in-progress", "[READY]", "PASSED", "FAILED", "COMPLETE"}
PHASE_ENUM = {"investigate-design", "implement", "verify"}
ADMISSION_WINDOW = 20

CLASS_TAGS = {
    "F": {"VERIFIED", "PENDING", "INVALIDATED", "AUTO-ACCEPTED"},
    "D": {"PENDING", "COMMITTED", "INVALIDATED", "AUTO-ACCEPTED"},
    "R": {"AMENDED", "PENDING", "INVALIDATED", "AUTO-ACCEPTED"},
    "A": {"DISPATCHED", "BIT", "ZERO-DELTA", "VOID"},
    "V": {"PASSED", "ISSUES FOUND"},
}
ALL_TAGS = set().union(*CLASS_TAGS.values()) | {"READY"}
TAG_LITERAL_RE = re.compile(
    r"\[(" + "|".join(sorted(map(re.escape, ALL_TAGS), key=len, reverse=True))
    + r")\]")

ENTRY_HEAD_RE = re.compile(r"^- ([FDRAV])(\d+)\b")
ENTRY_RE = re.compile(r"^- ([FDRAV])(\d+) \[([^\]]+)\] (.*)$")
# entry-INTENDED lines the head regex cannot see: a missing space
# after the dash or leading indentation makes an entry invisible to
# every predicate with no violation at all (attack-9 B3 — a
# premise-kill one character off dispatched a dead design). The
# landing annotation never matches: it carries no dash.
NEAR_MISS_RE = re.compile(r"^(?:\s+-|-)\s*([FDRAV])(\d+)\b")
LANDING_RE = re.compile(r"^unit U\d+ landed:")
LANDING_INDENTED_RE = re.compile(r"^\s+unit U\d+ landed:")
SUPERSEDED_OPEN_RE = re.compile(r"^> Superseded — ")
CLAUSE_RE = re.compile(
    r"clause (\w+)\s+(dead\s*\([^)]*\)|restated-at-\S+|dead\b)")


@dataclass
class Entry:
    lineno: int
    cls: str
    id: str
    tag: str
    body: str
    basis: str | None


def say(msg):
    print(msg)


def finish(verdict, exit_code, **detail):
    say(VERDICT_PREFIX + json.dumps({"verdict": verdict, **detail},
                                    ensure_ascii=False))
    sys.exit(exit_code)


# ------------------------------------------------------------- pure functions

def classify_scope(body: str):
    m = re.match(r"unit (U\d+)\b", body)
    if m:
        return ("unit", m.group(1))
    if body.startswith("record:"):
        return ("record", None)
    return ("scopeless", None)


def defang_text(text: str):
    """Drop brackets and lowercase counted-tag literals in place;
    return (text, names-in-order-of-first-occurrence)."""
    names = []

    def repl(m):
        low = m.group(1).lower()
        if low not in names:
            names.append(low)
        return low

    return TAG_LITERAL_RE.sub(repl, text), names


def latest_by_id(entries):
    latest = {}
    for e in entries:
        latest[e.id] = e
    return latest


def cited_ids(basis: str):
    return re.findall(r"\b([FDRAV]\d+)\b", basis or "")


# ------------------------------------------------------------------- parsing

def parse_tracker(text: str):
    """Return (entries, violations, meta). Violations are lint-grade
    dicts {code, line, text}."""
    entries, violations = [], []
    lines = text.splitlines()

    status_line = phase_line = None
    status_val = phase_val = None
    for i, line in enumerate(lines, 1):
        if status_line is None and line.startswith("Status:"):
            status_line, status_val = i, line[len("Status:"):].strip()
        if phase_line is None and line.startswith("Phase:"):
            phase_line, phase_val = i, line[len("Phase:"):].strip()

    def viol(code, lineno, text_):
        violations.append({"code": code, "line": lineno, "text": text_})

    if status_val is None or status_val not in STATUS_ENUM:
        viol("status-enum", status_line or 0, status_val or "<missing>")
    elif status_line > ADMISSION_WINDOW:
        viol("admission-window", status_line,
             f"Status at line {status_line} > {ADMISSION_WINDOW}")
    if phase_val is None or phase_val not in PHASE_ENUM:
        viol("phase-enum", phase_line or 0, phase_val or "<missing>")
    elif phase_line > ADMISSION_WINDOW:
        viol("admission-window", phase_line,
             f"Phase at line {phase_line} > {ADMISSION_WINDOW}")

    in_block = False
    for i, line in enumerate(lines, 1):
        if SUPERSEDED_OPEN_RE.match(line):
            in_block = True
            continue
        if in_block:
            if line.startswith(">"):
                continue
            in_block = False
            # a quoted line resuming after the break is an orphan —
            # the blank inside the block was not a bare '>'
        if line.startswith("> ") or line == ">":
            viol("superseded-block-form", i,
                 "quoted line outside any '> Superseded —' block "
                 "(a blank inside a block must be a bare '>')")

    for i, line in enumerate(lines, 1):
        if LANDING_RE.match(line):
            viol("landing-indent", i, line)
        elif LANDING_INDENTED_RE.match(line) and (
                i < 2 or lines[i - 2].strip()):
            viol("landing-blank", i, line)

        head = ENTRY_HEAD_RE.match(line)
        if not head:
            near = NEAR_MISS_RE.match(line)
            if near:
                viol("entry-near-miss", i, line)
            continue
        m = ENTRY_RE.match(line)
        if not m:
            viol("entry-form", i, line)
            continue
        cls, num, tag, body = m.groups()
        if tag not in CLASS_TAGS[cls]:
            viol("tag-enum", i, f"[{tag}] on {cls}-line")
        basis = None
        if "— basis:" in body:
            body_main, basis = body.split("— basis:", 1)
            body_main, basis = body_main.strip(), basis.strip()
        else:
            body_main = body.strip()
            viol("basis-missing", i, line)
        entries.append(Entry(i, cls, f"{cls}{num}", tag, body_main, basis))

    # bracketed tag literal anywhere outside an entry's leading tag
    # position and outside the Status header line
    for i, line in enumerate(lines, 1):
        if status_line == i or phase_line == i:
            continue
        scan = line
        m = ENTRY_RE.match(line)
        if m:
            scan = m.group(4)  # body only; leading tag is legitimate
        if TAG_LITERAL_RE.search(scan):
            viol("tag-literal-in-body", i, line)

    return entries, violations, {"status": status_val, "phase": phase_val}


def repo_paths(path_arg: str):
    """(filesystem_path, repo_relative_or_None, repo_top_or_None) for a
    tracker path. One grammar across every subcommand (attack-7 N3:
    open() resolved against cwd while `git show` resolved against the
    repo root — the same value succeeded in one subcommand and failed
    in another): relative inputs are repo-root-relative; outside a
    repo they are cwd-relative and the repo-relative half is None."""
    p = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                       capture_output=True, text=True)
    top = p.stdout.strip() if p.returncode == 0 else None
    if os.path.isabs(path_arg):
        fs = path_arg
    elif top:
        fs = os.path.join(top, path_arg)
    else:
        fs = path_arg
    rel = None
    if top:
        try:
            rel = os.path.relpath(os.path.realpath(fs),
                                  os.path.realpath(top))
            if rel.startswith(".."):
                rel = None
        except ValueError:
            rel = None
    return fs, rel, top


def load(path_arg):
    fs, rel, top = repo_paths(path_arg)
    # the git tool halts on a path outside the surrounding repo; the
    # record tool must too (attack-8 N1: every record-side gate —
    # sweep, closure, lint — was satisfiable by a tracker the run can
    # never pin). No surrounding repo keeps the documented
    # cwd-relative sense.
    if top and rel is None:
        finish("PATH_OUTSIDE_REPO", 2, path=path_arg)
    try:
        with open(fs, encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        finish("TRACKER_UNREADABLE", 2, error=str(e))


# ---------------------------------------------------------------- lint/sweep

def cmd_lint(args):
    _, violations, meta = parse_tracker(load(args.tracker))
    for v in violations:
        say(f"lint: {v['code']} @ line {v['line']}: {v['text']}")
    if violations:
        finish("LINT_VIOLATIONS", 2, violations=violations, **meta)
    finish("LINT_CLEAN", 0, **meta)


def sweep_checks(entries):
    violations = []
    latest = latest_by_id(entries)

    for id_, e in sorted(latest.items(), key=lambda kv: kv[1].lineno):
        if e.tag == "PENDING":
            violations.append({"code": "pending-latest", "line": e.lineno,
                               "text": f"{id_} latest line is [PENDING]"})

    for e in entries:
        if e.tag == "INVALIDATED" and re.search(r"\bdead\b(?!\s*\()", e.body):
            violations.append({"code": "killerless-dead", "line": e.lineno,
                               "text": f"{e.id}: dead disposition without "
                                       "its named killer"})

    for id_, e in latest.items():
        if e.tag == "INVALIDATED":
            continue
        for cited in cited_ids(e.basis or ""):
            c = latest.get(cited)
            if c is not None and c.tag == "INVALIDATED":
                violations.append(
                    {"code": "basis-cites-invalidated", "line": e.lineno,
                     "text": f"{id_} (live) rests on {cited}, whose latest "
                             "line is [INVALIDATED]"})

    clause_dispositions = {}
    for e in entries:
        if e.tag != "INVALIDATED":
            continue
        for clause, disp in CLAUSE_RE.findall(e.body):
            clause_dispositions.setdefault(e.id, {})[clause] = disp
    return violations, clause_dispositions


def cmd_sweep(args):
    entries, violations, meta = parse_tracker(load(args.tracker))
    sweep_viols, clause_dispositions = sweep_checks(entries)
    violations += sweep_viols
    for v in violations:
        say(f"sweep: {v['code']} @ line {v['line']}: {v['text']}")
    say("judgment residue (desk work, not checked here): dead-basis "
        "body-reads, duplicate-id body-read, restatement adoption "
        "checks, basis reach")
    detail = {"clause_dispositions": clause_dispositions, **meta}
    if violations:
        finish("SWEEP_HOLDS", 2, violations=violations, **detail)
    finish("SWEEP_CLEAN", 0, **detail)


# ------------------------------------------------------------------- closure

CLOSURE_BLOCKING_CODES = ("entry-form", "tag-enum", "entry-near-miss")

TAG_WORD_RE = re.compile(
    r"\b(" + "|".join(sorted(map(re.escape, ALL_TAGS), key=len,
                             reverse=True)) + r")\b")


def closure_blocking_violations(entries, violations):
    """The parse violations the closure may not read past: a line that
    LOOKS like an entry but failed the grammar is invisible to every
    predicate below — one dropped bracket turned a reopened design
    into a green light (attack-8 B2). Append-only means the malformed
    line never leaves the file, so a violation is DISARMED only by a
    RE-ASSERTION: a later clean line for the same id carrying the SAME
    tag the malformed text names — order alone let a later unrelated
    line convert a premise-kill VOID into DISPATCHABLE (attack-9 B2),
    and the re-assertion is what carries the malformed line's content
    into the entry set the closure reads. No tag extractable, no
    disarm: the desk re-states the line correctly under its own id."""
    armed = []
    for v in violations:
        if v["code"] not in CLOSURE_BLOCKING_CODES:
            continue
        head = (ENTRY_HEAD_RE.match(v["text"])
                or NEAR_MISS_RE.match(v["text"]))
        vid = f"{head.group(1)}{head.group(2)}" if head else next(
            (e.id for e in entries if e.lineno == v["line"]), None)
        tag_m = TAG_WORD_RE.search(v["text"])
        tag = tag_m.group(1) if tag_m else None
        if vid and tag and any(
                e.id == vid and e.tag == tag and e.lineno > v["line"]
                for e in entries):
            continue
        armed.append(v)
    return armed


def cmd_closure(args):
    if args.unit is not None and not re.fullmatch(r"U\d+", args.unit):
        # attack-8 N3: a mistyped id ("3", "u3") matched no scope line
        # and fell through to UNIT_DISPATCHABLE — a silent hold-clear
        finish("USAGE_ERROR", 3,
               error=f"--unit must match U<k>, got {args.unit!r}")
    entries, violations, _ = parse_tracker(load(args.tracker))
    blocking = closure_blocking_violations(entries, violations)
    if blocking:
        for v in blocking:
            say(f"closure blocked: {v['code']} @ line {v['line']}: "
                f"{v['text']}")
        finish("CLOSURE_RECORD_MALFORMED", 2, violations=blocking)
    a_lines = [e for e in entries if e.cls == "A"]
    if not a_lines or a_lines[-1].tag != "ZERO-DELTA":
        finish("CLOSURE_ABSENT", 2,
               last_a=(f"{a_lines[-1].id} [{a_lines[-1].tag}]"
                       if a_lines else None))
    closing = a_lines[-1]
    say(f"closure: {closing.id} [ZERO-DELTA] at line {closing.lineno}")

    latest = latest_by_id(entries)
    post = [e for e in entries
            if e.lineno > closing.lineno and e.cls in ("F", "D", "R")]
    # latest line per id AT the closure — the live set the closure
    # rests on (attack-7 N1)
    live_at_close = {}
    for e in entries:
        if e.lineno <= closing.lineno:
            live_at_close[e.id] = e
    scopeless, unit_lines = [], []
    for e in post:
        scope, unit = classify_scope(e.body)
        if (e.tag == "INVALIDATED"
                and e.id in live_at_close
                and live_at_close[e.id].tag != "INVALIDATED"):
            # a post-closure invalidation of an entry LIVE at the
            # closure is a premise-kill whatever its opener says —
            # the mis-scoped form must void, not dispatch (N1)
            scopeless.append({"line": f"{e.id} [{e.tag}] {e.body}",
                              "lineno": e.lineno,
                              "why": "invalidates an entry live at "
                                     "the closure"})
            continue
        if scope == "scopeless":
            scopeless.append({"line": f"{e.id} [{e.tag}] {e.body}",
                              "lineno": e.lineno})
        elif scope == "unit":
            unit_lines.append((unit, e))
    if scopeless:
        for s in scopeless:
            why = s.get("why", "scopeless post-closure line")
            say(f"closure VOID: {why}: {s['line']}")
        finish("CLOSURE_VOID", 2, scopeless=scopeless)

    if not args.unit:
        finish("CLOSURE_LIVE", 0,
               closing=f"{closing.id} at line {closing.lineno}")

    held = [e for (u, e) in unit_lines
            if u == args.unit and e.tag == "AUTO-ACCEPTED"
            and "held:" in e.body and latest[e.id] is e]
    if held:
        finish("UNIT_HELD", 2, unit=args.unit,
               holds=[f"{e.id} [{e.tag}] {e.body}" for e in held])
    amendments = [
        {"line": f"{e.id} [{e.tag}] {e.body}", "lineno": e.lineno}
        for (u, e) in unit_lines
        if u == args.unit and e.tag != "INVALIDATED"
        and latest[e.id] is e]
    finish("UNIT_DISPATCHABLE", 0, unit=args.unit, amendments=amendments)


# -------------------------------------------------------------------- filter

def cmd_filter(args):
    _, rel, top = repo_paths(args.tracker)
    if top and rel is None:
        finish("PATH_OUTSIDE_REPO", 2, path=args.tracker)
    if rel is None:
        finish("PIN_UNREADABLE", 2, sha=args.sha, tracker=args.tracker,
               error="tracker does not resolve inside a git repo")
    # the artifact lands OUTSIDE the repo (attack-8 NIT3): an in-repo
    # artifact is an untracked file under a brief asserting tree ==
    # lock commit — the seal rule's reasoning, applied to the write
    # this tool itself performs. Checked before anything is written.
    out_real = os.path.realpath(args.out)
    if top and os.path.commonpath(
            [out_real, os.path.realpath(top)]) == os.path.realpath(top):
        finish("ARTIFACT_IN_REPO", 2, out=args.out,
               error="attack artifact must land outside the repo "
                     "(tree-claim briefs assert tree == lock commit)")
    p = subprocess.run(["git", "show", f"{args.sha}:{rel}"],
                       capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if p.returncode != 0:
        finish("PIN_UNREADABLE", 2, sha=args.sha, tracker=args.tracker,
               stderr=p.stderr.strip())
    lines = p.stdout.splitlines()
    out, blocks, sections = [], 0, 0
    in_block = in_section = False
    for line in lines:
        if in_block:
            if line.startswith(">"):
                continue
            in_block = False
        if in_section:
            if line.startswith("## ") and not line.startswith("## Superseded —"):
                in_section = False
            else:
                continue
        if SUPERSEDED_OPEN_RE.match(line):
            in_block = True
            blocks += 1
            continue
        if line.startswith("## Superseded —"):
            in_section = True
            sections += 1
            continue
        out.append(line)
    text = "\n".join(out) + "\n"
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(text)
    say(f"artifact written: {args.out}")
    finish("ARTIFACT_WRITTEN", 0, sha=args.sha, out=args.out,
           lines_in=len(lines), lines_out=len(out),
           blocks_dropped=blocks, sections_dropped=sections)


# --------------------------------------------------------------------- quote

def cmd_quote(args):
    raw = sys.stdin.buffer.read().decode("utf-8", "replace")
    defanged, names = defang_text(raw)
    first = f"> Superseded — {args.label}"
    if names:
        first += "; " + ", ".join(names)
    body = [("> " + l) if l else ">" for l in defanged.splitlines()]
    block = "\n".join([first] + body)
    print(block)
    finish("QUOTE_BLOCK", 0, block=block, defanged=names,
           lines=len(block.splitlines()))


class Parser(argparse.ArgumentParser):
    """Usage errors land as a USAGE_ERROR verdict line (exit 3),
    never a bare argparse death on the holds exit code (attack-7 B1
    — the git tool's contract, carried across)."""

    def error(self, message):
        finish("USAGE_ERROR", 3, error=message)


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    ap = Parser(prog="statiker-record")
    sub = ap.add_subparsers(dest="cmd", required=True,
                            parser_class=Parser)
    for name in ("lint", "sweep"):
        p = sub.add_parser(name)
        p.add_argument("--tracker", required=True)
    p = sub.add_parser("closure")
    p.add_argument("--tracker", required=True)
    p.add_argument("--unit")
    p = sub.add_parser("filter")
    p.add_argument("--tracker", required=True)
    p.add_argument("--sha", required=True)
    p.add_argument("--out", required=True)
    p = sub.add_parser("quote")
    p.add_argument("--label", required=True)

    args = ap.parse_args()
    handlers = {"lint": cmd_lint, "sweep": cmd_sweep, "closure": cmd_closure,
                "filter": cmd_filter, "quote": cmd_quote}
    try:
        handlers[args.cmd](args)
    except SystemExit:
        raise
    except Exception as e:  # never a silent death
        finish("INTERNAL_ERROR", 3, error=f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

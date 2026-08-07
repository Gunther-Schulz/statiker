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
import re
import subprocess
import sys
from dataclasses import dataclass

VERDICT_PREFIX = "STATIKER-RECORD VERDICT: "

STATUS_ENUM = {"in-progress", "[READY]", "PASSED", "FAILED", "COMPLETE"}
PHASE_ENUM = {"investigate-design", "implement", "verify"}
ADMISSION_WINDOW = 20

CLASS_TAGS = {
    "F": {"VERIFIED", "PENDING", "INVALIDATED", "AUTO-ACCEPTED"},
    "D": {"PENDING", "COMMITTED", "INVALIDATED", "AUTO-ACCEPTED"},
    "R": {"AMENDED", "PENDING", "INVALIDATED", "AUTO-ACCEPTED"},
    "A": {"DISPATCHED", "BIT", "ZERO-DELTA"},
    "V": {"PASSED", "ISSUES FOUND"},
}
ALL_TAGS = set().union(*CLASS_TAGS.values()) | {"READY"}
TAG_LITERAL_RE = re.compile(
    r"\[(" + "|".join(sorted(map(re.escape, ALL_TAGS), key=len, reverse=True))
    + r")\]")

ENTRY_HEAD_RE = re.compile(r"^- ([FDRAV])(\d+)\b")
ENTRY_RE = re.compile(r"^- ([FDRAV])(\d+) \[([^\]]+)\] (.*)$")
LANDING_RE = re.compile(r"^unit U\d+ landed:")
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

        head = ENTRY_HEAD_RE.match(line)
        if not head:
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


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
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

def cmd_closure(args):
    entries, _, _ = parse_tracker(load(args.tracker))
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
    scopeless, unit_lines = [], []
    for e in post:
        scope, unit = classify_scope(e.body)
        if scope == "scopeless":
            scopeless.append({"line": f"{e.id} [{e.tag}] {e.body}",
                              "lineno": e.lineno})
        elif scope == "unit":
            unit_lines.append((unit, e))
    if scopeless:
        for s in scopeless:
            say(f"closure VOID: scopeless post-closure line: {s['line']}")
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
        and latest[e.id].tag != "INVALIDATED"]
    finish("UNIT_DISPATCHABLE", 0, unit=args.unit, amendments=amendments)


# -------------------------------------------------------------------- filter

def cmd_filter(args):
    p = subprocess.run(["git", "show", f"{args.sha}:{args.tracker}"],
                       capture_output=True, text=True)
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
    raw = sys.stdin.read()
    defanged, names = defang_text(raw)
    first = f"> Superseded — {args.label}"
    if names:
        first += "; " + ", ".join(names)
    body = [("> " + l) if l else ">" for l in defanged.splitlines()]
    block = "\n".join([first] + body)
    print(block)
    finish("QUOTE_BLOCK", 0, block=block, defanged=names)


def main():
    ap = argparse.ArgumentParser(prog="statiker-record")
    sub = ap.add_subparsers(dest="cmd", required=True)
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

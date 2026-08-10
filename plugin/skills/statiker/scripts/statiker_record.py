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
  waves   --tracker P                 read-only: connected-component
                                      wave partition over units' live
                                      write-set lines (unit U<k>
                                      write-set: <path>); a unit
                                      carrying no live write-set line
                                      comes back UNPLANNABLE, never
                                      guessed at. NOTE: no literal
                                      write-set record-line form is
                                      spelled out in SKILL.md (only
                                      the LOCK's own `lock-set:`
                                      F-line is, :471-472) — this
                                      parses the composition of two
                                      ESTABLISHED conventions (the
                                      per-path F/D-line form and the
                                      `unit U<k> ` scope-opener); flag
                                      this convention for desk/
                                      operator confirmation before
                                      relying on it against a live
                                      tracker.
  trend   --tracker P                 read-only: per-round finding
                                      counts over resolved
                                      (BIT/ZERO-DELTA) A-lines, a pure-
                                      arithmetic FLAT/IMPROVING/
                                      WORSENING trajectory, and a
                                      concentration flag when the
                                      newest round's findings cite a
                                      D-id whose latest revision
                                      landed in the immediately prior
                                      round (that prior round's own
                                      repair set)
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
_TAG_ALT = "|".join(sorted(map(re.escape, ALL_TAGS), key=len, reverse=True))
TAG_LITERAL_RE = re.compile(r"\[(" + _TAG_ALT + r")\]")

ENTRY_HEAD_RE = re.compile(r"^- ([FDRAV])(\d+)\b")
ENTRY_RE = re.compile(r"^- ([FDRAV])(\d+) \[([^\]]+)\] (.*)$")
# entry-INTENDED lines the head regex cannot see: a missing space
# after the dash or leading indentation makes an entry invisible to
# every predicate with no violation at all (attack-9 B3 — a
# premise-kill one character off dispatched a dead design).
#
# The detection is a SIGNATURE, never an opener enumeration (ES-8;
# attack-11 B2 and design-attack R3): an enumerated bullet set is an
# OPEN set, and its next unlisted member — `1)`, or no bullet at all —
# walks straight through. What makes a line entry-INTENDED is an id
# token at the line's leading position with an ADJACENT tag literal,
# whatever sits in front of it. Bracketed tags match case-insensitively
# (the slip class); a BARE enum word must be spelled as a tag, so
# ordinary prose ("F1 bit of context") stays prose.
SIGNATURE_RE = re.compile(
    r"^[^A-Za-z]*([FDRAVfdrav])(\d+)\b\s*"
    r"(?:\[\s*(?i:" + _TAG_ALT + r")|(?:" + _TAG_ALT + r")\b)")
# the requirement-head region — file start to the first `## ` heading —
# parses NO entries on ANY of the three surfaces, and neither do quoted
# lines (ES-1; design-attack R3-B3): an operator bullet inside INTENT
# is prose, and it can neither brick the closure gate nor mint a
# phantom entry. Header parsing and the whole-file defang lint are
# untouched by the exclusion.
HEAD_BOUNDARY_RE = re.compile(r"^## ")
# a mid-run operator instruction lands at the record's END, labeled
# (ES-2; R3-B2). The label is machine-findable so verify's composition
# grades against the head PLUS what the tool lists, never memory.
INTENT_EXACT_RE = re.compile(r"^INTENT: ")
INTENT_NEAR_RE = re.compile(r"(?i)^intent\b")
# the scope openers are CASE-SENSITIVE LITERALS (SKILL.md, The
# record): a case or spacing variant is entry-INTENDED scope that no
# predicate can read, so it lints rather than passing as scopeless
# prose (attack-10: `Record:` voided a live closure and no verdict
# named the cause).
SCOPE_NEAR_RE = re.compile(r"(?i)^(units?\s+U\d|record\s*:)")
SCOPE_EXACT_RE = re.compile(r"^(unit U\d+ |record: )")
UNIT_SCOPE_RE = re.compile(r"^unit U\d+ ")
# the hold form is the literal `unit U<k> held: ` opening under
# [AUTO-ACCEPTED] — "a hold written any other way holds nothing"
# (SKILL.md, The record). attack-10: the substring read MISSED every
# spelling variant and OVER-FIRED on `withheld:` in a gap line; the
# word-search that replaced it failed in BOTH directions again
# (attack-11 N2/N3 — a `hold:` slip passed and travelled as an
# amendment, while prose "held" barred every unit). Classification is
# POSITIONAL (ES-8): the token AFTER the unit opener decides, the
# colon forms elsewhere are displacement, the bare colon-less word is
# prose, and backtick-quoted text is exempt.
HOLD_EXACT_RE = re.compile(r"^unit U\d+ held: ")
HOLD_NEAR_RE = re.compile(r"(?i)^(?:hold|held)s?\b")
HOLD_COLON_RE = re.compile(r"(?i)(?<![A-Za-z])(?:hold|held)s?\s*:")
BACKTICK_RE = re.compile(r"`[^`]*`")
LANDING_RE = re.compile(r"^unit U\d+ landed:")
LANDING_INDENTED_RE = re.compile(r"^\s+unit U\d+ landed:")
SUPERSEDED_OPEN_RE = re.compile(r"^> Superseded — ")
HEADING_RE = re.compile(r"^#{1,6} ")
# `\S+` swallowed the separator that ended the clause, gluing a `;`
# onto the disposition value; and a spelling the alternation does not
# carry (`restated at D8`) matched nothing at all, so the clause left
# no trace in either the aggregation or the violations (attack-10 N9).
# CLAUSE_TOKEN_RE is the reach check: every `clause <name>` the body
# names is either parsed here or lints unparsed.
CLAUSE_RE = re.compile(
    r"\bclause (\w+)\s+(dead\s*\([^)]*\)|restated-at-[^\s;,]+|dead\b)")
CLAUSE_TOKEN_RE = re.compile(r"\bclause (\w+)\b")
# the repair token, matched by NUMBER: 0.2.43 tested it as a substring
# (`"corrects line 12" in "…corrects line 123…"` is True), so a token
# naming one line cleared a violation on another.
CORRECTS_RE = re.compile(r"corrects line (\d+)")

# ES-10: every violation names its CLASS and the repair form that
# class takes, so the desk composes from the verdict and never from
# memory. The two settled forms split on the violation SITE (SKILL.md,
# Implementation): a violation on a MACHINE TOKEN indicts the
# semantics every gate reads, so the target is superseded whole; one
# in free BODY CONTENT leaves gate-read semantics sound, so the target
# keeps its live entry and the correcting line only sheds.
REPAIR_SUPERSEDE = ("supersede-whole: restate under the same id with "
                    "`corrects line {n}`; tag and scope re-carried "
                    "where they parsed")
REPAIR_BOOKKEEPING = ("bookkeeping: append `- <id> [<tag>] record: "
                      "corrects line {n}` — sheds violations only, "
                      "status untouched")
# Two classes the settle does not reach, and neither repair form fits
# (surfaced as a build gap; the strings state what SKILL.md's own
# rules already say rather than inventing a third mechanism): the
# header is the record's ONE MUTABLE surface, and a status question is
# answered by an ordinary new tag-first line, never smuggled through a
# repair token.
REPAIR_HEADER = ("header rewrite: Status and Phase are the record's "
                 "one mutable surface — no repair token reaches them")
REPAIR_STATUS_LINE = ("status line: append a new tag-first line under "
                      "the same id — a repair token never changes "
                      "status")

MACHINE_TOKEN_CODES = {
    "entry-form", "tag-enum", "entry-near-miss", "scope-near-miss",
    "hold-form", "corrects-nothing", "multi-corrects-token",
    "repair-tag-change", "repair-scope-change",
}
BODY_CONTENT_CODES = {
    "tag-literal-in-body", "basis-missing", "clause-unparsed",
    "superseded-block-form", "landing-indent", "landing-blank",
    "intent-near-miss",
}
REPAIR_FORMS = dict(
    [(c, REPAIR_SUPERSEDE) for c in MACHINE_TOKEN_CODES]
    + [(c, REPAIR_BOOKKEEPING) for c in BODY_CONTENT_CODES]
    + [(c, REPAIR_HEADER) for c in
       ("status-enum", "phase-enum", "admission-window")]
    + [(c, REPAIR_STATUS_LINE) for c in
       ("pending-latest", "killerless-dead", "basis-cites-invalidated")])


def annotate_repairs(violations):
    """Attach each violation's repair form, addressed at its own line."""
    for v in violations:
        form = REPAIR_FORMS.get(
            v["code"],
            "unclassified: this violation's repair form is not settled")
        v["repair"] = form.format(n=v["line"])
    return violations


def violation_site(codes):
    return ("machine-token"
            if any(c in MACHINE_TOKEN_CODES for c in codes)
            else "body-content")


@dataclass
class Entry:
    lineno: int
    cls: str
    id: str
    tag: str
    body: str
    basis: str | None


def emit(text):
    """Write one line at the BYTE level (ES-9): the tracker is bytes,
    so a byte quoted in a violation or a quote block leaves as the byte
    it arrived as. The text layer's blanket errors='replace' would mint
    a SECOND spelling on output — the very thing the input-side decode
    rule exists to prevent (attack-11 N6)."""
    sys.stdout.flush()
    sys.stdout.buffer.write(text.encode("utf-8", "surrogateescape") + b"\n")
    sys.stdout.buffer.flush()


def say(msg):
    emit(msg)


def finish(verdict, exit_code, **detail):
    emit(VERDICT_PREFIX + json.dumps({"verdict": verdict, **detail},
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


def hold_violations(body: str, tag: str):
    """ES-8: the hold is classified POSITIONALLY — by the token after
    `unit U<k> `, never by searching the body for a word. Returns the
    violation codes one body earns."""
    scrubbed = BACKTICK_RE.sub(" ", body)   # quoting a literal is legal
    m = UNIT_SCOPE_RE.match(scrubbed)
    if m:
        rest = scrubbed[m.end():]
        if rest.startswith("held: "):
            # the literal itself: it holds only under [AUTO-ACCEPTED],
            # and read as an ordinary amendment it dispatches the unit
            # its author meant to stop
            return [] if tag == "AUTO-ACCEPTED" else ["hold-form"]
        if HOLD_NEAR_RE.match(rest) or HOLD_COLON_RE.search(rest):
            # short of the literal at the hold position, or a colon
            # form displaced later into a unit-scoped body
            return ["hold-form"]
        return []
    if HOLD_COLON_RE.match(scrubbed):
        return ["hold-form"]                # a colon form opening a body
    return []


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

def split_lines(text: str):
    """Split on newlines ONLY. str.splitlines() also breaks on U+000C,
    U+2028 and U+0085, so a form feed in a body invented a line the
    file does not have: entry counts diverged from `grep -c '^- '` and
    every later violation's line number pointed one line off the file
    the desk repairs (attack-9)."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return [l[:-1] if l.endswith("\r") else l for l in lines]


def parse_tracker(text: str):
    """Return (entries, violations, meta). Violations are lint-grade
    dicts {code, line, text}."""
    entries, violations = [], []
    line_ids = {}          # lineno -> the id the line NAMES, parsed or not
    line_parse = {}        # lineno -> what PARSED there (ES-4's pins)
    late_intent = []       # ES-2: the labeled mid-run INTENT lines
    lines = split_lines(text)

    # ES-1: surface 1 begins at the first `## ` heading
    head_end = len(lines) + 1
    for i, line in enumerate(lines, 1):
        if HEAD_BOUNDARY_RE.match(line):
            head_end = i
            break

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

        # ES-1: the head region and quoted lines parse no entries on
        # ANY of surface 1's scans — the exact head included
        if i < head_end or line.startswith(">"):
            continue

        if INTENT_EXACT_RE.match(line):        # ES-2
            late_intent.append(i)
            continue
        if INTENT_NEAR_RE.match(line):
            viol("intent-near-miss", i, line)
            continue

        head = ENTRY_HEAD_RE.match(line)
        if not head:
            near = SIGNATURE_RE.match(line)
            if near:
                viol("entry-near-miss", i, line)
                # an entry-INTENDED line names an id even when nothing
                # parses: the repair token is addressed at THIS line,
                # and its author's id is what the token must match
                line_ids[i] = f"{near.group(1).upper()}{near.group(2)}"
            continue
        m = ENTRY_RE.match(line)
        if not m:
            viol("entry-form", i, line)
            line_ids[i] = f"{head.group(1)}{head.group(2)}"
            continue
        cls, num, tag, body = m.groups()
        line_ids[i] = f"{cls}{num}"
        tag_valid = tag in CLASS_TAGS[cls]
        if not tag_valid:
            # the FULL line, never a summary (attack-10 B1): a blocking
            # violation's text is the line the desk repairs, and the
            # disarm below is addressed at that line's number
            viol("tag-enum", i, line)
        basis = None
        if "— basis:" in body:
            body_main, basis = body.split("— basis:", 1)
            body_main, basis = body_main.strip(), basis.strip()
        else:
            body_main = body.strip()
            viol("basis-missing", i, line)
        scope_parsed = True
        if SCOPE_NEAR_RE.match(body_main) and \
                not SCOPE_EXACT_RE.match(body_main):
            viol("scope-near-miss", i, line)
            scope_parsed = False               # the opener IS the violation
        else:
            for code in hold_violations(body_main, tag):
                viol(code, i, line)
        # ES-4: what a repair must re-carry is what PARSED here — a
        # violated token pins nothing, since repairing it is the
        # token's own reason for existing
        line_parse[i] = {"tag": tag, "tag_valid": tag_valid,
                         "scope": classify_scope(body_main)[0],
                         "scope_parsed": scope_parsed}
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

    entries, violations = apply_supersession(entries, violations, line_ids,
                                             line_parse)
    annotate_repairs(violations)
    return entries, violations, {"status": status_val, "phase": phase_val,
                                 "late_intent": late_intent}


def _corrects_nothing_reason(n, e, violated, line_ids):
    if n >= e.lineno:
        return ("its own line" if n == e.lineno else f"line {n}, "
                "which comes later — a repair names a line already "
                "written")
    owner = line_ids.get(n)
    if owner is not None and owner != e.id:
        return f"line {n}, which belongs to {owner}, not {e.id}"
    return f"line {n}, which carries no violation to repair"


def _repair_pin_complaints(e, n, line_parse):
    """ES-4: a supersede-whole restatement carries the target's tag
    where the tag parsed AND its scope class where the opener parsed.
    Status and scope changes are ordinary new lines — smuggling either
    through a repair converts what the record says without ever
    appending a line that says it."""
    info = line_parse.get(n)
    mine = line_parse.get(e.lineno)
    if not info or not mine:
        return []                      # nothing parsed there to pin
    out = []
    # a token compares only where BOTH sides parsed it: a restatement
    # whose own opener or tag is the thing being repaired has no
    # readable scope or tag to differ WITH
    if info["tag_valid"] and mine["tag_valid"] and e.tag != info["tag"]:
        out.append({"code": "repair-tag-change", "line": e.lineno,
                    "text": f"{e.id}: the restatement of line {n} carries "
                            f"[{e.tag}] where the target parsed "
                            f"[{info['tag']}]"})
    if info["scope_parsed"] and mine["scope_parsed"]:
        new_scope = classify_scope(e.body)[0]
        if new_scope != info["scope"]:
            out.append({"code": "repair-scope-change", "line": e.lineno,
                        "text": f"{e.id}: the restatement of line {n} opens "
                                f"{new_scope} scope where the target parsed "
                                f"{info['scope']}"})
    return out


def apply_supersession(entries, violations, line_ids, line_parse):
    """The `corrects line <n>` token's reach splits on WHERE the
    target's violation sits (SKILL.md, Implementation).

    A violation ON A MACHINE TOKEN indicts the semantics every gate
    reads, so the target is SUPERSEDED WHOLE — entry and violations
    together — and the correcting line RESTATES the content (a
    corrected line that kept parsing voided the closure its own repair
    had unlocked, and its violations held the sweep forever). A
    violation in free BODY CONTENT leaves gate-read semantics sound,
    so the target KEEPS its live entry and the correcting line is
    bookkeeping: it sheds the target's violations and is itself
    excluded from entry-status semantics — exactly one of the pair is
    ever an entry, and a [PENDING] target stays [PENDING] until its
    own ordinary status line.

    Reach (ES-6): the token names an earlier line that CARRIES a
    violation and names either the correcting line's OWN id or NO
    readable id at all — the id-misspelling class the token was built
    for; a line readably naming a DIFFERENT id stays barred, and a
    clean line is never erasable (a premise-kill is a clean line).

    One pass over the ORIGINAL entry set, so a token is read whether
    or not the line carrying it is itself superseded (ES-5: no
    re-carry — the restatement of a superseded correcting line carries
    exactly ONE token, the one naming the line it corrects)."""
    violated = {}
    for v in violations:
        violated.setdefault(v["line"], []).append(v["code"])
    superseded, shed, bookkeeping, complaints = set(), set(), set(), []
    for e in entries:
        tokens = list(CORRECTS_RE.finditer(e.body))
        if len(tokens) > 1:
            complaints.append(
                {"code": "multi-corrects-token", "line": e.lineno,
                 "text": f"{e.id}: {len(tokens)} `corrects line` tokens on "
                         "one line — a repair names exactly one line"})
        for m in tokens:
            n = int(m.group(1))
            owner = line_ids.get(n)
            if not (n < e.lineno and n in violated
                    and owner in (None, e.id)):
                complaints.append(
                    {"code": "corrects-nothing", "line": e.lineno,
                     "text": f"{e.id}: `corrects line {n}` names "
                             + _corrects_nothing_reason(n, e, violated,
                                                        line_ids)})
                continue
            if violation_site(violated[n]) == "machine-token":
                superseded.add(n)
                complaints += _repair_pin_complaints(e, n, line_parse)
            else:
                shed.add(n)
                bookkeeping.add(e.lineno)
    return ([e for e in entries
             if e.lineno not in superseded and e.lineno not in bookkeeping],
            [v for v in violations
             if v["line"] not in superseded and v["line"] not in shed]
            + complaints)


def git_toplevel(cwd):
    # the toplevel is a PATH read: bytes decoded the way the OS decodes
    # argv, never text=True's locale decode (attack-10 N5 — a repo
    # directory carrying a non-UTF-8 byte answered INTERNAL_ERROR from
    # every gate). A cwd that does not exist is not a tool defect
    # either: the caller routes it (attack-10 NIT2).
    try:
        p = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=cwd,
                           capture_output=True)
    except OSError:
        return None
    return os.fsdecode(p.stdout.strip()) if p.returncode == 0 else None


def rebase_at_symlinked_ancestor(p: str, top_real: str):
    """Re-root a path reached through a symlinked ANCESTOR of the repo
    top, or None if no ancestor resolves to the top. git reports the
    toplevel PHYSICALLY, so the link spelling never matches it
    textually and a perfectly pinnable tracker read as one outside the
    repo (attack-10 N4). Only the ANCESTOR resolves — the tail below
    it is re-rooted textually, so the tracker itself is still taken as
    named and a `..` escape still finds no ancestor and still halts.
    (The git tool carries the same helper; the two scripts ship
    standalone.)"""
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


def nearest_existing_ancestor(p: str):
    """The path itself if it exists (a broken symlink counts — git
    commits one as the link file), else the first ancestor that does,
    else None. The named half of ES-7's containment probe."""
    cur = p
    while True:
        if os.path.lexists(cur):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


def textual_repo_top(path: str):
    """The nearest ancestor carrying a `.git`, walking the path AS
    NAMED — the as-named half of the must-be-outside check (ES-7). A
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


def repo_paths(path_arg: str):
    """(filesystem_path, repo_relative_or_None, repo_top_or_None,
    resolved_from_or_None) for a tracker path. One grammar across every
    subcommand (attack-7 N3: open() resolved against cwd while `git
    show` resolved against the repo root — the same value succeeded in
    one subcommand and failed in another): relative inputs are
    repo-root-relative.

    The repo is the TRACKER's, resolved at the tracker's own directory
    (attack-9: a no-cwd rev-parse answered about the CALLER's repo, so
    one absolute tracker got three verdicts from three cwds). Only a
    RELATIVE input still consults the caller's repo, to give the
    documented repo-root-relative sense a root.

    CONTAINMENT is decided on the REAL path (ES-7, design-attack
    R3-B7): walk to the nearest EXISTING ancestor; the path is inside
    only when that ancestor's realpath sits inside (or equals) the
    top's realpath. A path named inside that resolves OUT is not
    pinnable there and halts. The operation still runs on the AS-NAMED
    spelling, and a path reached through a symlinked ancestor OF THE
    TOP is re-rooted textually (attack-10 N4: git reports the toplevel
    physically, so the link spelling never matches it)."""
    if os.path.isabs(path_arg):
        fs = path_arg
    else:
        cwd_top = git_toplevel(None)
        fs = os.path.join(cwd_top, path_arg) if cwd_top else path_arg
    top = git_toplevel(os.path.dirname(os.path.abspath(fs)) or None)
    rel, resolved = None, None
    if top:
        top_real = os.path.realpath(top)
        p = os.path.normpath(os.path.join(top_real, fs))
        if not p.startswith(top_real + os.sep) and p != top_real:
            p = rebase_at_symlinked_ancestor(p, top_real) or p
        anc = nearest_existing_ancestor(p)
        anc_real = os.path.realpath(anc) if anc else None
        inside = bool(anc_real and (anc_real == top_real
                                    or anc_real.startswith(top_real + os.sep)))
        if inside and p.startswith(top_real + os.sep):
            rel = p[len(top_real) + 1:]
        real_p = os.path.realpath(p)
        if real_p != p:
            resolved = {"named": p, "real": real_p}
    return fs, rel, top, resolved


def check_tracker_dir(path_arg, fs):
    """A tracker whose DIRECTORY does not exist is an unreadable
    tracker, not a tool defect: the toplevel read used that directory
    as its cwd and died FileNotFoundError through the generic handler
    (attack-10 NIT2). One grammar, so every subcommand answers it the
    same way."""
    parent = os.path.dirname(os.path.abspath(fs)) or "."
    if not os.path.isdir(parent):
        finish("TRACKER_UNREADABLE", 2, path=path_arg,
               error=f"the tracker's directory does not exist: {parent}")


def unpinnable_tracker(path_arg, rel, top, resolved):
    """The halt a tracker no repo can pin earns — with the TRUE cause
    named. The 0.2.44 comment claimed rel is None exactly when top is
    (one cause); attack-11 N4 disproved it: a tracker inside a repo
    that RESOLVES out is the second cause, and blaming a missing repo
    sent the desk looking for the wrong thing."""
    if top is None:
        cause = "no git repository at the tracker's location"
    else:
        cause = (f"the tracker is named inside {top} but resolves outside "
                 f"it — a link's git history is the link string, so the "
                 f"run could never pin its record here")
    detail = {"path": path_arg, "error": cause}
    if resolved:
        detail["resolved_from"] = resolved
    finish("PATH_OUTSIDE_REPO", 2, **detail)


def load(path_arg):
    fs, rel, top, resolved = repo_paths(path_arg)
    check_tracker_dir(path_arg, fs)
    # a tracker no repo contains is one the run can never pin, and
    # every record-side gate — sweep, closure, lint — was satisfiable
    # by exactly that (attack-8 N1). Tracker-anchored resolution
    # (attack-9) makes "no repo at the tracker's own location" the
    # whole of that class: a tracker inside SOME repo is pinnable
    # there whatever the caller's cwd.
    if top is None or rel is None:
        unpinnable_tracker(path_arg, rel, top, resolved)
    try:
        # the tracker is BYTES: one non-UTF-8 byte in a body killed
        # every gate on the strict decode (attack-10 N6). Surrogates
        # survive the round trip, so a preserved line is written back
        # byte-identical.
        with open(fs, encoding="utf-8", errors="surrogateescape") as f:
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
        # clause-scoped: the rule is "a dead CLAUSE without its named
        # killer" (SKILL.md, Stop rule). attack-9: the bare `\bdead\b`
        # fired on prose ("the dead-letter queue design", "is dead
        # code") and held the record from [READY] on no defect at all.
        if (e.tag == "INVALIDATED" and re.search(r"\bclause\b", e.body)
                and re.search(r"\bdead\b(?!\s*\()", e.body)):
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
        parsed = set()
        for m in CLAUSE_RE.finditer(e.body):
            parsed.add(m.start())
            clause_dispositions.setdefault(e.id, {})[m.group(1)] = m.group(2)
        for m in CLAUSE_TOKEN_RE.finditer(e.body):
            if m.start() not in parsed:
                violations.append(
                    {"code": "clause-unparsed", "line": e.lineno,
                     "text": f"{e.id}: clause {m.group(1)} carries no "
                             "disposition this grammar reads"})
    return violations, clause_dispositions


def cmd_sweep(args):
    entries, violations, meta = parse_tracker(load(args.tracker))
    sweep_viols, clause_dispositions = sweep_checks(entries)
    violations += annotate_repairs(sweep_viols)
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

CLOSURE_BLOCKING_CODES = ("entry-form", "tag-enum", "entry-near-miss",
                          "scope-near-miss", "hold-form")


def closure_blocking_violations(violations):
    """The parse violations the closure may not read past: a line that
    LOOKS like an entry but failed the grammar is invisible to every
    predicate below — one dropped bracket turned a reopened design
    into a green light (attack-8 B2).

    The corrects-line disarm no longer lives here. A corrected line is
    SUPERSEDED at the parse layer (apply_supersession) — entry and
    violations together — so every gate inherits ONE exclusion and
    this is a plain filter. The tag-match disarm it replaced was both
    brickable and forgeable (attack-10 B1/B2)."""
    return [v for v in violations if v["code"] in CLOSURE_BLOCKING_CODES]


def cmd_closure(args):
    if args.unit is not None and not re.fullmatch(r"U\d+", args.unit):
        # attack-8 N3: a mistyped id ("3", "u3") matched no scope line
        # and fell through to UNIT_DISPATCHABLE — a silent hold-clear
        finish("USAGE_ERROR", 3,
               error=f"--unit must match U<k>, got {args.unit!r}")
    entries, violations, meta = parse_tracker(load(args.tracker))
    # ES-2: every closure verdict lists the labeled late-INTENT lines —
    # verify's composition grades against the head PLUS these, and the
    # tool is what finds them
    late = {"late_intent": meta["late_intent"]}
    blocking = closure_blocking_violations(violations)
    if blocking:
        for v in blocking:
            say(f"closure blocked: {v['code']} @ line {v['line']}: "
                f"{v['text']}")
        finish("CLOSURE_RECORD_MALFORMED", 2, violations=blocking, **late)
    a_lines = [e for e in entries if e.cls == "A"]
    if not a_lines or a_lines[-1].tag != "ZERO-DELTA":
        finish("CLOSURE_ABSENT", 2,
               last_a=(f"{a_lines[-1].id} [{a_lines[-1].tag}]"
                       if a_lines else None), **late)
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
        finish("CLOSURE_VOID", 2, scopeless=scopeless, **late)

    if not args.unit:
        finish("CLOSURE_LIVE", 0,
               closing=f"{closing.id} at line {closing.lineno}", **late)

    hold_prefix = f"unit {args.unit} held: "
    held = [e for (u, e) in unit_lines
            if u == args.unit and e.tag == "AUTO-ACCEPTED"
            and e.body.startswith(hold_prefix) and latest[e.id] is e]
    if held:
        finish("UNIT_HELD", 2, unit=args.unit,
               holds=[f"{e.id} [{e.tag}] {e.body}" for e in held], **late)
    amendments = [
        {"line": f"{e.id} [{e.tag}] {e.body}", "lineno": e.lineno}
        for (u, e) in unit_lines
        if u == args.unit and e.tag != "INVALIDATED"
        and latest[e.id] is e]
    finish("UNIT_DISPATCHABLE", 0, unit=args.unit, amendments=amendments,
           **late)


# --------------------------------------------------------------------- waves

# SKILL.md spells out exactly ONE literal per-path record-line form: the
# LOCK's own pathspec F-line (`- F<n> [VERIFIED] lock-set: <path> — basis:
# <the entry that produced it>`, SKILL.md:471-472). A unit's IMPLEMENTATION
# write-set has no literal record-line form anywhere in that file — it
# surfaces only as `--write-set <file>` CLI arguments the desk composes
# into a unit's dispatch brief (SKILL.md:850-861), never as a grammar this
# tool can read back out of tracker text. UNIT_WRITE_SET_RE therefore
# composes two conventions that ARE established (the per-path F/D-line
# form above, and the `unit U<k> ` scope-opener used throughout for
# unit-scoped bodies, e.g. SKILL.md:822/930) rather than inventing new
# syntax from nothing — but the composed form itself is NOT cited grammar.
# Backlog design premise ("the parse source is the record's own
# lock-set/write-set line form") does not hold as literally cited;
# flagged in the closing report as a decision made without an established
# source, for desk/operator confirmation before this parses a live
# tracker.
UNIT_WRITE_SET_RE = re.compile(r"^unit (U\d+) write-set: (\S.*)$")


def waves_over_units(entries):
    """(write_sets: unit -> live path set, unplannable units sorted
    ascending, waves: list of unit-id lists, each sorted ascending,
    ordered by each wave's lowest unit id). A unit is KNOWN if any live
    or dead entry opens `unit U<k> ` anywhere (classify_scope, the
    established scope-opener grammar) — write-set lines and any other
    unit-scoped line both count. A unit is PLANNABLE only if at least
    one of its write-set lines is LIVE (latest-line-per-id, tag !=
    INVALIDATED) — the same supersede convention the lock-set F-line
    uses (SKILL.md:499)."""
    latest = latest_by_id(entries)
    known_units = set()
    write_sets = {}
    for e in sorted(latest.values(), key=lambda e: e.lineno):
        scope, unit = classify_scope(e.body)
        if scope != "unit":
            continue
        known_units.add(unit)
        if e.tag == "INVALIDATED":
            continue
        m = UNIT_WRITE_SET_RE.match(e.body)
        if m:
            write_sets.setdefault(m.group(1), set()).add(m.group(2).strip())
    unplannable = sorted(known_units - write_sets.keys(),
                        key=lambda u: int(u[1:]))
    units = sorted(write_sets, key=lambda u: int(u[1:]))
    parent = {u: u for u in units}

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for i, a in enumerate(units):
        for b in units[i + 1:]:
            if write_sets[a] & write_sets[b]:
                union(a, b)
    components = {}
    for u in units:
        components.setdefault(find(u), []).append(u)
    waves = sorted(
        (sorted(members, key=lambda u: int(u[1:]))
         for members in components.values()),
        key=lambda members: int(members[0][1:]))
    return write_sets, unplannable, waves


def cmd_waves(args):
    entries, violations, meta = parse_tracker(load(args.tracker))
    blocking = closure_blocking_violations(violations)
    if blocking:
        for v in blocking:
            say(f"waves blocked: {v['code']} @ line {v['line']}: {v['text']}")
        finish("WAVES_RECORD_MALFORMED", 2, violations=blocking, **meta)
    write_sets, unplannable, waves = waves_over_units(entries)
    for i, members in enumerate(waves, 1):
        overlap = len(members) > 1
        say(f"wave {i}: {{{', '.join(members)}}}"
            + (" (overlap — serialize within wave)" if overlap
               else " (disjoint — parallel-eligible)"))
    for u in unplannable:
        say(f"UNPLANNABLE: {u} — no live write-set declared")
    finish("WAVES_COMPUTED", 0,
          waves=[{"units": m, "serialize": len(m) > 1} for m in waves],
          unplannable=unplannable,
          write_sets={u: sorted(p) for u, p in write_sets.items()},
          **meta)


# --------------------------------------------------------------------- trend

def trend_verdict(counts):
    """Arithmetic only, never judgment (backlog design: "as arithmetic
    over the counts, never judgment"): FLAT unless every consecutive
    step in the series moves the same direction, with at least one
    strict move that way. A single round, or a mixed series, is FLAT —
    the ambiguous middle stays unclassified rather than guessed."""
    if len(counts) < 2:
        return "FLAT"
    diffs = [b - a for a, b in zip(counts, counts[1:])]
    if all(d <= 0 for d in diffs) and any(d < 0 for d in diffs):
        return "IMPROVING"
    if all(d >= 0 for d in diffs) and any(d > 0 for d in diffs):
        return "WORSENING"
    return "FLAT"


def trend_over_rounds(entries):
    """(bounds, counts, trajectory, concentration, concentration_detail).

    A ROUND is a resolved attack outcome — an A-id's LATEST occurrence
    tagged BIT or ZERO-DELTA (SKILL.md: "VOID: The attack — an aborted
    or premise-broken round", explicitly not a real round; DISPATCHED
    is still open, no outcome to count yet), ordered by line. Findings
    belonging to round i are F-line ENTRIES landing after round i-1's
    A-line and up to (inclusive) round i's — the record's own
    append-only order (SKILL.md, The loop: investigation appends
    before a round's closing A-line).

    Concentration (backlog design, trend entry): does the NEWEST
    round's findings cite a D-id whose LATEST revision (latest-line-
    per-id) landed in the round immediately before it — "attack
    repairs revise D-lines, so the repair set is those revised ids".
    Only defined with >=2 rounds; the D-ids counted are exactly those
    whose latest-overall occurrence falls inside the prior round's own
    span (a later revision, elsewhere, means that D-id was not what
    the prior round repaired as it now stands)."""
    latest = latest_by_id(entries)
    a_latest = sorted([e for e in latest.values() if e.cls == "A"],
                      key=lambda e: e.lineno)
    rounds_a = [e for e in a_latest if e.tag in ("BIT", "ZERO-DELTA")]
    bounds = []
    prev = 0
    for e in rounds_a:
        bounds.append((prev, e.lineno, e))
        prev = e.lineno
    f_entries = [e for e in entries if e.cls == "F"]
    counts = [sum(1 for f in f_entries if start < f.lineno <= end)
             for start, end, _ in bounds]
    trajectory = trend_verdict(counts)
    concentration, hits = False, []
    if len(bounds) >= 2:
        prev_start, prev_end, _ = bounds[-2]
        cur_start, cur_end, _ = bounds[-1]
        d_entries = [e for e in entries if e.cls == "D"
                    and prev_start < e.lineno <= prev_end]
        repair_ids = {e.id for e in d_entries if latest.get(e.id) is e}
        cur_findings = [f for f in f_entries if cur_start < f.lineno <= cur_end]
        for f in cur_findings:
            hit = set(cited_ids(f.basis or "")) & repair_ids
            if hit:
                concentration = True
                hits.append({"finding": f.id, "repair_ids": sorted(hit)})
    return bounds, counts, trajectory, concentration, hits


def cmd_trend(args):
    entries, violations, meta = parse_tracker(load(args.tracker))
    blocking = closure_blocking_violations(violations)
    if blocking:
        for v in blocking:
            say(f"trend blocked: {v['code']} @ line {v['line']}: {v['text']}")
        finish("TREND_RECORD_MALFORMED", 2, violations=blocking, **meta)
    bounds, counts, trajectory, concentration, hits = trend_over_rounds(entries)
    if not bounds:
        say("trend: no resolved (BIT/ZERO-DELTA) attack round in this tracker")
        finish("TREND_NO_ROUNDS", 0, rounds=0, **meta)
    say(f"trend: {len(bounds)} round(s), findings {counts}, "
        f"trajectory {trajectory}"
        + (", CONCENTRATION in the prior round's repairs" if concentration
           else ""))
    finish("TREND_COMPUTED", 0, rounds=len(bounds), counts=counts,
          trajectory=trajectory, concentration=concentration,
          concentration_detail=hits, **meta)


# -------------------------------------------------------------------- filter

def cmd_filter(args):
    fs, rel, top, resolved = repo_paths(args.tracker)
    check_tracker_dir(args.tracker, fs)
    # a tracker that is itself a symlink halts (SKILL.md, The attack):
    # the link's git history is the LINK STRING, so the artifact came
    # out a one-line file and a round run over it would close a design
    # sight-unseen (attack-10 N10). Before anything is written.
    if os.path.islink(fs):
        finish("USAGE_ERROR", 3, tracker=args.tracker,
               error=f"--tracker names a symlink ({args.tracker}): name "
                     f"the real path — a link's git history is the link "
                     f"string, not the record")
    # an unpinnable tracker gets ONE verdict across every subcommand —
    # the same halt lint/sweep/closure emit; the former two-branch
    # split here answered PIN_UNREADABLE for the identical condition
    # (dispatch gaps 2+3, dispositioned at the desk). PIN_UNREADABLE
    # keeps its plain sense below: the sha itself cannot be read from
    # an existing repo's history.
    if rel is None:
        unpinnable_tracker(args.tracker, rel, top, resolved)
    # the artifact lands OUTSIDE the repo (attack-8 NIT3): an in-repo
    # artifact is an untracked file under a brief asserting tree ==
    # lock commit — the seal rule's reasoning, applied to the write
    # this tool itself performs. Checked before anything is written.
    # EVERY repo, not just the tracker's (attack-9): an --out into a
    # nested OUTER checkout wrote an untracked file into someone
    # else's tree under the same tree-claim exposure.
    named_out = os.path.abspath(args.out)
    out_real = os.path.realpath(args.out)
    out_parent = os.path.dirname(out_real) or "."
    if not os.path.isdir(out_parent):
        # an invocation mistake, not a tool defect: the generic
        # handler used to report it as INTERNAL_ERROR (attack-9)
        finish("USAGE_ERROR", 3,
               error=f"--out parent directory does not exist: "
                     f"{args.out} (parent {out_parent})")
    if os.path.isdir(out_real):
        # attack-11 N5: the open() died IsADirectoryError through the
        # generic handler as INTERNAL_ERROR — a tool-defect verdict for
        # an invocation mistake, inconsistent with its sibling above
        finish("USAGE_ERROR", 3,
               error=f"--out names an existing directory ({args.out}): "
                     f"name the artifact FILE")
    # a MUST-BE-OUTSIDE path is outside only when BOTH computations
    # agree (ES-7): the real form catches a link pointing INTO a repo,
    # the as-named form catches an --out spelled through an in-repo
    # link — which the real-side read alone accepted.
    out_repo = (git_toplevel(out_parent)
                or textual_repo_top(os.path.dirname(named_out) or "."))
    if out_repo:
        finish("ARTIFACT_IN_REPO", 2, out=args.out, repo=out_repo,
               error="attack artifact must land outside every repo "
                     "(tree-claim briefs assert tree == lock commit)")
    # read the history of the TRACKER's repo — `rel` is relative to
    # `top`, so a cwd-resolved `git show` asks the wrong repo (or none)
    p = subprocess.run(["git", "show", f"{args.sha}:{rel}"], cwd=top,
                       capture_output=True)
    if p.returncode != 0:
        finish("PIN_UNREADABLE", 2, sha=args.sha, tracker=args.tracker,
               stderr=p.stderr.decode(errors="replace").strip())
    # errors='replace' SUBSTITUTED a non-UTF-8 byte in the artifact —
    # the attacker would grade text the record does not contain
    # (attack-10 N6). Surrogateescape both ways keeps preserved lines
    # byte-identical to the pinned tracker.
    lines = split_lines(p.stdout.decode("utf-8", "surrogateescape"))
    # ES-3 (design-attack R3-B1): the two species are BLANKED IN PLACE
    # and NO header is emitted, so artifact line numbers EQUAL source
    # line numbers by construction — a `corrects line <n>` token
    # dereferences to the same text in either. A compacting filter sent
    # every token to the wrong line, and the header meant to declare
    # the alignment shifted the very alignment it declared.
    out, blocks, sections, blanked = [], 0, 0, 0

    def blank():
        nonlocal blanked
        out.append("")
        blanked += 1

    in_block = in_section = False
    for line in lines:
        if in_block:
            if line.startswith(">"):
                blank()
                continue
            in_block = False
        if in_section:
            # a section ends at the next heading of ANY level: closing
            # only on `## ` swallowed every line after a SUBHEADING,
            # prose and R-lines with it (attack-10 NIT3)
            if HEADING_RE.match(line) and \
                    not line.startswith("## Superseded —"):
                in_section = False
            elif ENTRY_HEAD_RE.match(line):
                # ENTRIES are never filtered (SKILL.md, The attack):
                # dead bodies are load-bearing for closure questions.
                # attack-9: the section drop swallowed them with the
                # legacy prose, putting live findings out of every
                # attacker's sight. On their OWN line numbers.
                out.append(line)
                continue
            else:
                blank()
                continue
        if SUPERSEDED_OPEN_RE.match(line):
            in_block = True
            blocks += 1
            blank()
            continue
        if line.startswith("## Superseded —"):
            in_section = True
            sections += 1
            blank()
            continue
        out.append(line)
    text = "\n".join(out) + "\n"
    with open(args.out, "w", encoding="utf-8",
              errors="surrogateescape") as f:
        f.write(text)
    say(f"artifact written: {args.out}")
    finish("ARTIFACT_WRITTEN", 0, sha=args.sha, out=args.out,
           source_tracker=rel,
           lines_in=len(lines), lines_out=len(out),
           blocks_blanked=blocks, sections_blanked=sections,
           lines_blanked=blanked,
           form="the two Superseded species are BLANKED IN PLACE (each "
                "dropped line an empty line) and no header line is "
                "emitted, so artifact line numbers equal the pinned "
                "source's — quote these fields beside the artifact")


# --------------------------------------------------------------------- quote

def cmd_quote(args):
    # surrogateescape, never 'replace' (ES-9): a report byte mangled
    # here is mangled before defang ever sees it, and the block the
    # desk pastes into the record is then text the report never held
    raw = sys.stdin.buffer.read().decode("utf-8", "surrogateescape")
    defanged, names = defang_text(raw)
    first = f"> Superseded — {args.label}"
    if names:
        first += "; " + ", ".join(names)
    body = [("> " + l) if l else ">" for l in defanged.splitlines()]
    block = "\n".join([first] + body)
    emit(block)
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
    for name in ("lint", "sweep", "waves", "trend"):
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
                "waves": cmd_waves, "trend": cmd_trend,
                "filter": cmd_filter, "quote": cmd_quote}
    try:
        handlers[args.cmd](args)
    except SystemExit:
        raise
    except Exception as e:  # never a silent death
        finish("INTERNAL_ERROR", 3, error=f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

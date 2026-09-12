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
                                      guessed at. The write-set
                                      record-line form is normative in
                                      SKILL.md (Implementation,
                                      :876-880); the LOCK's own
                                      `lock-set:` F-line sits at
                                      :486-487 (SENTENCE-C1: this NOTE
                                      formerly read the form as
                                      unspecified prose-composition —
                                      it is normative, citations
                                      refreshed against the current
                                      file, not the triage record's).
  trend   --tracker P                 read-only: per-round finding
                                      counts over resolved
                                      (BIT/ZERO-DELTA) A-lines, a pure-
                                      arithmetic FLAT/IMPROVING/
                                      WORSENING trajectory, and a
                                      concentration flag when the
                                      newest round's FINDINGS (scope
                                      != record: — a record-scoped
                                      F-line is desk bookkeeping, a
                                      verification or confirmation,
                                      and never counts) cite a D-id
                                      whose latest revision landed in
                                      the immediately prior round
                                      (that prior round's own
                                      repair set)
  sustain --tracker P                 read-only: round-open's
                                      mechanical never-sustain gate
                                      (P20) — SUSTAIN_OK when the
                                      latest [BIT] round's own
                                      findings hold at least one
                                      design-substance (non-`record:`)
                                      member, else SUSTAIN_DENIED;
                                      SUSTAIN_NOT_APPLICABLE outside a
                                      [BIT] round
  tripwire --tracker P [--threshold N]
                                      read-only: the ZERO-LANDED
                                      progress tripwire (P19) —
                                      TRIPWIRE_FIRES when at least N
                                      resolved attack rounds exist yet
                                      neither a landing annotation nor
                                      a V-line does, else
                                      TRIPWIRE_SILENT; N resolves as
                                      --threshold (always overriding)
                                      > the LATEST appended `record:
                                      tripwire armed at N` entry
                                      (st-35) > the header Budget
                                      line's `/ tripwire <N>` field >
                                      unarmed — an unarmed tracker
                                      (none of the three given) is
                                      TRIPWIRE_SILENT with reason
                                      "unarmed", never a guessed
                                      default. The verdict's `reason`
                                      field distinguishes
                                      unarmed/silent/fires
  filter  --tracker P --sha S --out F pinned attack artifact (reads
                                      the sha, drops the two
                                      Superseded species)
  pinned  --tracker P --sha S         read-only: asserts the working
                                      tracker is a pure append over the
                                      version pinned at S (old content
                                      a BYTE-LEVEL prefix of new, ES-9)
                                      — PINNED_APPEND_ONLY proceeds,
                                      PINNED_REWRITTEN names the first
                                      divergent line; an in-place
                                      status rewrite reads clean to
                                      every positional gate, this is
                                      the one check it cannot fool
  verify-gate --tracker P --sha S     read-only: compares the repo's
                                      current HEAD against the copy's
                                      HEAD sha recorded at a verify
                                      leg's read-start (P30, F121/F124)
                                      — VERIFY_COPY_CLEAN when unmoved,
                                      VERIFY_COPY_STALE names every
                                      commit and touched path landed
                                      during the leg; the desk is an
                                      unfrozen writer during verify, so
                                      this is the repo-HEAD sibling of
                                      `pinned`'s tracker-text check
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
from pathlib import Path

# E-J: shared byte-level stderr fallback, extracted out of this file
# (the source of truth statiker_git.py's mirror was built against) so
# both tools import one body rather than carrying two copies to drift
# apart. Loader-robust: tests import tools by file path, which does
# not put the scripts dir on sys.path — the guarded insert makes
# `import statiker_emit` resolve the same way whether this file runs
# as a script or is imported directly.
_SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)
import statiker_emit

VERDICT_PREFIX = "STATIKER-RECORD VERDICT: "

# Exit codes mirror the git tool: 0 = proceedable, 2 = holds/voids,
# 3 = usage or internal error — and the verdict-line guarantee covers
# usage errors (attack-7 B1: the git tool's repair had not been
# carried across; a bare argparse death on exit 2 read as a hold).

STATUS_ENUM = {"in-progress", "[READY]", "PASSED", "FAILED", "COMPLETE"}
PHASE_ENUM = {"investigate-design", "implement", "verify"}
ADMISSION_WINDOW = 20
# E-G': Budget's own declared grammar (SKILL.md, The record) is the
# compound `cycles <n> / rounds <n> / verify <n>` — trend counts
# ROUNDS, so that is the component sweep's evidence line reads.
BUDGET_ROUNDS_RE = re.compile(r"\brounds\s+(\d+)\b")
# R3 (checkpoint review): the header Budget line's OPTIONAL
# `/ tripwire <n>` field — the arming carrier when `tripwire` is
# invoked with no --threshold (SKILL.md, The record). st-34 (N2)
# (0.2.87 checkpoint review): captures the raw TOKEN after `tripwire`,
# not just digits — a digits-only pattern let a malformed value
# (`tripwire -1`) miss the match entirely and fall through to the
# unarmed branch below, silencing the breaker instead of refusing the
# invocation; the caller (cmd_tripwire) parses the token and refuses a
# non-integer or sub-1 value the way --threshold refuses one.
# 0.2.89 fix (N2, dev-notes/OBSERVATIONS.md "0.2.89 checkpoint-review
# dispositions"): the bare `\btripwire\s+(\S+)` form dropped the
# page's own `/` anchor (SKILL.md, "an optional trailing `/ tripwire
# <n>` field") — the word "tripwire" appearing ANYWHERE in the Budget
# line (e.g. prose noting it will be "armed later by entry") matched
# and hard-failed the subcommand on a non-numeric capture. Anchored on
# the declared `/` form; a present `/ tripwire <x>` still refuses a
# non-integer or sub-1 value exactly as before (st-34 N2 unchanged).
TRIPWIRE_BUDGET_RE = re.compile(r"/\s*tripwire\s+(\S+)")
# st-35 (dev-notes/OBSERVATIONS.md, "the tripwire's arming carrier"
# ruling): the appended arming route — arming, or tightening an armed
# tripwire, lands as an ordinary `record: `-scoped F-line (SCOPE_EXACT_RE
# already admits `record: `; the entry needs no new grammar). Resolution
# order: --threshold > the LATEST such entry > the header's own
# `tripwire <n>` field > unarmed — so an appended arm REPAIRS a record
# seeded with a bad or absent header value; the header is never
# consulted once an arming entry exists.
TRIPWIRE_ARM_RE = re.compile(
    r'^record: tripwire armed at (\S+)(?: — ".*")?$')
# 0.2.89 fix (B3, dev-notes/OBSERVATIONS.md "0.2.89 checkpoint-review
# dispositions"): the arming form fails OPEN — an entry whose body
# begins `record: tripwire armed` but strays from TRIPWIRE_ARM_RE's
# exact shape (or carries the wrong class/tag) silently drops out of
# cmd_tripwire's arm_entries filter and the run reads unarmed with no
# lint pointing at the slip. NEAR is deliberately looser than
# TRIPWIRE_ARM_RE (case-insensitive, no trailing-shape requirement):
# the near-miss condition below is "looks like an arming attempt AND
# is not a fully-qualified one", not a second grammar to maintain.
TRIPWIRE_ARM_NEAR_RE = re.compile(r'(?i)^record: tripwire armed\b')

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
# E-L (BACKLOG, provenance relay 1 / cycle-12 resume report): a
# production tracker's own `## Requirement head` heading is routinely
# the file's FIRST `## ` heading, which the plain HEAD_BOUNDARY_RE
# read above stops the head region AT — the requirements sitting
# below it then read r_lines: 0 and parse as malformed entries. A
# first heading matching this title (case-insensitive, whole line) is
# itself part of the head and does not terminate the region — the
# region extends through it to the NEXT `## ` heading (or EOF); any
# other first heading keeps the plain HEAD_BOUNDARY_RE behavior.
REQUIREMENT_HEAD_TITLE_RE = re.compile(r"^##\s+Requirement Head\s*$",
                                       re.IGNORECASE)
# E-A (begehung-harvest F1/A1): the head-region exclusion suppresses
# the entry scan silently — a live entry sitting above the first `## `
# heading, or the whole file when no heading exists at all, parses as
# zero entries and every gate reads that as clean. `entries: <n>` and
# `head_boundary: <n>` ride every verdict so "clean" and "examined
# nothing" are no longer the same JSON; this re-uses SIGNATURE_RE's own
# "entry-INTENDED" test to find the specific lines an evidence line
# should name.
# R-lines (E-A, begehung-harvest B2): the numbered `R<n>.` form
# (never dash-led `- R<n>`, the amendment form) inside the head only.
R_LINE_RE = re.compile(r"^R\d+\.")
# a mid-run operator instruction lands at the record's END, labeled
# (ES-2; R3-B2). The label is machine-findable so verify's composition
# grades against the head PLUS what the tool lists, never memory.
INTENT_EXACT_RE = re.compile(r"^INTENT: ")
INTENT_NEAR_RE = re.compile(r"(?i)^intent\b")
# P3 (BACKLOG, SKILL.md, The record, "SKILL: statiker <version>"):
# a resuming desk's version-crossing APPEND entry carries this
# literal line as its machine-readable core — INTENT_EXACT_RE's
# sibling, same body-region placement, same field-not-gate
# treatment (no near-miss class: attribution only).
SKILL_VERSION_EXACT_RE = re.compile(r"^SKILL: statiker (\S+)$")
# the header's own `Skill: statiker <version>` line (SKILL.md, The
# record) — read here for the FIRST time; the header capture below
# stores the raw text, this pattern pulls just the version out of it,
# falling back to the raw text when the header line does not carry
# the documented shape (a field never fails to attach on a malformed
# header, it degrades to the unparsed string).
SKILL_HEADER_VERSION_RE = re.compile(r"^statiker (\S+)$")
# P6 (BACKLOG, SKILL.md Stop rule): a declared-exemption label line —
# INTENT_EXACT_RE/SKILL_VERSION_EXACT_RE's sibling, same body-region
# placement, same field-not-gate treatment (no near-miss class:
# attribution only). Two forms, both CODE-SPECIFIC and frozen at
# declaration: `lines<=N` covers every line 1..N, `line N` covers
# exactly that line — a violation above a ceiling blocks untouched.
# M1 (opus release review round 2, 2026-08-16): the authorization
# citation is a mandatory GRAMMAR slot — an exemption is operator
# authority, so a declaration that cites nothing nets nothing.
SWEEP_EXEMPT_CEILING_RE = re.compile(
    r"^SWEEP_EXEMPT: ([a-z-]+) lines<=(\d+) — basis: \S.*$")
SWEEP_EXEMPT_LINE_RE = re.compile(
    r"^SWEEP_EXEMPT: ([a-z-]+) line (\d+) — basis: \S.*$")
# H6 (opus release review 2026-08-16): the defang class is never
# exemptible — SKILL.md's standing clause says an undefanged tag
# literal holds every later sweep for the run's life, and a netting
# that could silence it would let one declaration void that rule.
# H4 (round 2): live-work classes join defang — the no-[PENDING]
# gate is load-bearing for [READY], the closing [ZERO-DELTA], and
# the Verify dispatch; a netting that reached it would unlock all
# three in one declared line. Exemptible holds are form debt only.
UNEXEMPTIBLE_CODES = {"tag-literal-in-body", "pending-latest"}
# P5 (BACKLOG, re-opened; CLAUDE.md's narrowed no-grandfather bullet,
# 2026-08-17): epoch-scoped sweep — a rule never grades a line that
# predates its own mint. Backfilled ONCE from this repo's git history
# (each code's introducing commit's `plugin/.claude-plugin/plugin.json`
# version — the SKILL version served when the rule first shipped);
# re-derive rather than hand-edit if the repo's history is ever
# rewritten. FORM codes (SKILL.md: "superseded-block-form,
# basis-missing, tag-literal-in-body, clause-unparsed") are the only
# ones this mint gates — F148's measured live/retro distribution, not
# invented; every other code (SUBSTANCE, by omission from this set)
# grades every line whatever its age, the safe default this entry
# never widens. `tag-literal-in-body` also sits in UNEXEMPTIBLE_CODES
# above — a DIFFERENT mechanism (H6: no OPERATOR declaration may
# silence it) that RETRO grading does not touch: RETRO is a computed
# historical fact, never an operator decision, so the two coexist.
# T3 (0.2.84 checkpoint review): declarator-bookkeeping,
# foreign-id-suspect, and landing-missing are SUBSTANCE codes,
# correctly never retro (SKILL.md, Stop rule) — this table doubles
# as the mint REGISTRY for every code, not only the FORM-gated ones.
RULE_MINT_VERSION = {
    "admission-window": "0.2.33",
    "basis-cites-invalidated": "0.2.33",
    "basis-missing": "0.2.33",
    "clause-unparsed": "0.2.43",
    "corrects-nothing": "0.2.45",
    "corrects-token-out-of-body": "0.2.67",
    "declarator-bookkeeping": "0.2.84",
    "entry-form": "0.2.33",
    "entry-near-miss": "0.2.39",
    "foreign-id-suspect": "0.2.84",
    "freeze-breach": "0.2.63",
    "hold-form": "0.2.43",
    "intent-near-miss": "0.2.49",
    "killerless-dead": "0.2.33",
    "landing-blank": "0.2.36",
    "landing-indent": "0.2.33",
    "landing-missing": "0.2.84",
    "multi-corrects-token": "0.2.49",
    "pending-latest": "0.2.33",
    "phase-enum": "0.2.33",
    "repair-scope-change": "0.2.49",
    "repair-tag-change": "0.2.49",
    "scope-near-miss": "0.2.43",
    "status-enum": "0.2.33",
    "superseded-block-form": "0.2.33",
    "tag-enum": "0.2.33",
    "tag-literal-in-body": "0.2.33",
    "tripwire-arm-near-miss": "0.2.89",
    "write-set-near-miss": "0.2.59",
    "write-set-path-near-miss": "0.2.62",
}
FORM_CODES_MINT_GATED = {"superseded-block-form", "basis-missing",
                         "tag-literal-in-body", "clause-unparsed"}


def _version_tuple(v):
    try:
        return tuple(int(x) for x in v.split("."))
    except (ValueError, AttributeError, TypeError):
        return None


def effective_version_at_line(lineno, skill_versions):
    """The SKILL version active when `lineno` was WRITTEN — the latest
    `skill_versions` entry (header first, then file-order `SKILL: `
    markers, P3) whose own line is <= lineno; lines between two
    markers were written under the earlier one (SKILL.md, The
    record). None when `skill_versions` carries nothing at all
    (marker-less record, pre-P3): no per-line attribution is possible,
    so no forgiveness is ever computed there — the declaration route
    (SWEEP_EXEMPT) stands in its place. `skill_versions` is already in
    file order (parse_tracker appends header then body markers as
    parsed top-to-bottom), so the last qualifying entry is current."""
    active = None
    for sv in skill_versions:
        if sv["line"] <= lineno:
            active = sv["version"]
        else:
            break
    return active


def is_retro(code, lineno, skill_versions):
    """P5: True when a FORM-code violation's line predates the code's
    own mint version — grades RETRO, surfaced but never blocking.
    SUBSTANCE codes (not in FORM_CODES_MINT_GATED) are never retro,
    whatever their line's version — the over-forgiveness case this
    entry's own verifier names."""
    if code not in FORM_CODES_MINT_GATED:
        return False
    mint = RULE_MINT_VERSION.get(code)
    if mint is None:
        return False
    active = effective_version_at_line(lineno, skill_versions)
    if active is None:
        return False
    av, mv = _version_tuple(active), _version_tuple(mint)
    if av is None or mv is None:
        return False
    return av < mv


def net_retro_holds(violations, skill_versions):
    """Splits (blocking, retro) — retro holds are surfaced in the
    verdict's own field, never in the blocking set, and never consult
    or interact with the SWEEP_EXEMPT declaration route (net_sweep_
    exemptions), which runs independently on whatever remains
    blocking after this pass."""
    blocking, retro = [], []
    for v in violations:
        if is_retro(v["code"], v["line"], skill_versions):
            retro.append(v)
        else:
            blocking.append(v)
    return blocking, retro


# the scope openers are CASE-SENSITIVE LITERALS (SKILL.md, The
# record): a case or spacing variant is entry-INTENDED scope that no
# predicate can read, so it lints rather than passing as scopeless
# prose (attack-10: `Record:` voided a live closure and no verdict
# named the cause).
SCOPE_NEAR_RE = re.compile(r"(?i)^(units?\s+U\d|record\s*:)")
SCOPE_EXACT_RE = re.compile(r"^(unit U\d+ |record: )")
UNIT_SCOPE_RE = re.compile(r"^unit U\d+ ")
# P25 (BACKLOG; run-2 F77): the out-of-scope grade a finding entry may
# carry at booking — a THIRD classify_scope() category, sibling to
# `unit U<k> `/`record:`, so an out-of-scope-graded F-line is exempt
# from the post-closure scopeless-VOID rule (Implementation) the same
# way a `record:`-scoped bookkeeping line already is: the grade is a
# leavings-gate concern (below), never a design re-derivation trigger.
# No near-miss lint class — SCOPE_NEAR_RE stays as-is; this token is
# body content, not a machine-token gate.
OUT_OF_SCOPE_RE = re.compile(r"^out-of-scope: \S")
# the disposition clause an out-of-scope grade's LATEST line must
# carry to clear the leavings gate — an export ref (a decision-graded
# backlog entry in the target repo) or a one-line recorded drop; a
# separate em-dash clause preceding `— basis:`, same packing shape as
# a clause disposition's `dead (<killer>)` parenthetical.
OUT_OF_SCOPE_DISPOSITION_RE = re.compile(r"— (exported|dropped): \S")
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
# P4 (BACKLOG, SKILL.md, Stop rule, "unit U<k> irreversible:
# <effect>"): the irreversible tag's own record line, HOLD_EXACT_RE's
# sibling — `unit U<k> irreversible: <effect>` as its own record
# line's body, [READY]'s enumeration form. FIELD only in this
# version, NO near-miss lint class (BACKLOG's own
# caution: a bare-word scan false-fires on "not irreversible" and
# shared bodies — the E-K false-fire class, conservatism decided
# rather than an oversight); unattended enforcement stays the hold
# entry (HOLD_EXACT_RE), unchanged by this line's presence.
IRREVERSIBLE_EXACT_RE = re.compile(r"^unit U(\d+) irreversible: (\S.*)$")
BACKTICK_RE = re.compile(r"`[^`]*`")
# the write-set token gets the same positional near-miss treatment as
# the scope opener (SCOPE_NEAR_RE/SCOPE_EXACT_RE, above): a wrong-case,
# unhyphenated, colonless, or oddly-spaced spelling fails
# UNIT_WRITE_SET_RE (:915) silently — the unit then reads UNPLANNABLE
# with no lint pointing at the slip. Examined only immediately after an
# EXACT `unit U<k> ` prefix, never a body-wide search.
WRITE_SET_NEAR_RE = re.compile(r"(?i)^write[\s-]*set\s*:?\s*")
WRITE_SET_EXACT_RE = re.compile(r"^write-set: \S")
# 0.2.85 (B4 residue): the grammar's one legal slot for a
# supersede-whole write-set redeclaration's own resolving token — a
# trailing parenthetical on the declarator line, stripped before the
# path-field near-miss check (write_set_violations).
WRITE_SET_CORRECTS_SUFFIX_RE = re.compile(r"\s*\(corrects line \d+\)$")
LANDING_RE = re.compile(r"^unit (U\d+) landed:")
LANDING_INDENTED_RE = re.compile(r"^\s+unit (U\d+) landed:")
# P24 (begehung R4): a body-content line reporting the git tool's
# UNIT_COMMITTED verdict for a unit, quoted the way EXTRAS/RESIDUE
# already ask the desk to (SKILL.md, Implementation: "book as a
# `record:` F-line from the pasted verdict") — the shape a
# UNIT_COMMITTED-evidence line takes whether or not the desk also
# appended the landing annotation.
# 0.2.84 N2: `\b` sits between two word characters at the boundary
# after "D" in "UNIT_COMMITTED_EXTRAS"/"UNIT_COMMITTED_RESIDUE" (`_`
# is a word char) — never fired, so the bare form is the required
# ANCHOR and the suffix is optional on a boundary that survives it.
UNIT_COMMITTED_EVIDENCE_RE = re.compile(
    r"\bUNIT_COMMITTED(?:_EXTRAS|_RESIDUE)?\b")
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
# P35 (BACKLOG.md:129, F91): the prescribed line carries its OWN
# basis clause — the verdict that prescribed the repair, named,
# terminating rather than citing anything further — so pasting it
# does not itself draw a fresh basis-missing hold and move the hold
# one line down; the ORIGINAL literal (no basis clause) was not a
# fixpoint, F91's measured bite.
REPAIR_BOOKKEEPING = ("bookkeeping: append `- <id> [<tag>] record: "
                      "corrects line {n} — basis: the {code} verdict "
                      "at line {n}` — sheds violations only, status "
                      "untouched")
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
# tag-literal-in-body's OWNER-LESS shape (begehung-harvest 2 finding 2,
# probe B): a header, INTENT, or bare-prose line parses no entry, so
# the bracketed literal sitting there is the hand-defang duty SKILL.md
# names — "an undefanged bracketed tag literal holds the sweep
# wherever it sits ... in INTENT it is the enforcement of the
# hand-defang duty" — not an ordinary body-content violation a
# bookkeeping token may shed.
REPAIR_INTENT_HOLD = ("hold: an undefanged tag literal here holds the "
                      "sweep for the run's life — write the defanged "
                      "literal in place; no repair token reaches it")
# P15 (BACKLOG; b7's F29 dry-run in a scratch copy — eight holds
# before, eight after — and the parent run's F147, both live
# measurements): the prior repair text for `clause-unparsed` and
# `killerless-dead` prescribed an in-place edit that mints a NEW
# violation of the same class and clears nothing on settled-prose
# form debt. E-M already established both codes are RESOLVER-
# UNREACHABLE — no `corrects line <n>` token can ever resolve against
# them (clause-unparsed is a SWEEP-stage code, never a member of
# apply_supersession's LINT-stage `violated` map; killerless-dead's
# "append a new tag-first line" restates the same dead disposition
# under the same id and re-fires unchanged) — so both share ONE
# repair form now: the sanctioned route is a `SWEEP_EXEMPT: <code>
# lines<=<n> — basis: <citation>` declaration on operator grant
# (the 0.2.79 ask machinery), never an edit or a repair token.
REPAIR_SWEEP_EXEMPT_ROUTE = (
    "settled form debt: no in-place edit clears this and no repair "
    "token resolves against it — the sanctioned route is a "
    "`SWEEP_EXEMPT: <code> lines<=<n> — basis: <citation>` "
    "declaration on operator grant")
# E-M, widened (halted mid-build, decision recorded here): building
# the assertion below surfaced FOUR MORE codes with clause-unparsed's
# exact defect, for a DIFFERENT structural reason — `corrects-nothing`,
# `multi-corrects-token`, `repair-tag-change`, `repair-scope-change`
# are apply_supersession's OWN complaints, attached to the CORRECTING
# line (the one carrying the defective `corrects line <n>` token)
# rather than to a target line, and never fed back into the `violated`
# map a later token would need to resolve against them. Empirically
# confirmed, not just reasoned: a planted corrects-nothing violation's
# own printed SUPERSEDE repair, followed literally, mints a SECOND
# permanent corrects-nothing hold — 271a6bf's exact failure shape
# under a different trigger. Governing principle: a defective
# correcting line is never itself a corrects target; append-only text
# means whatever it NAMED keeps carrying its own violation on every
# future scan regardless of what superseded it, so the surviving path
# is a fresh, correctly-formed token aimed at THAT name, never at the
# line that got the token wrong.
REPAIR_CORRECTS_NOTHING = ("bookkeeping: a defective correcting line "
                           "is never itself a corrects target — check "
                           "the line it named: a live, reachable "
                           "violation there earns a fresh `corrects "
                           "line <n>` naming it; none standing (or "
                           "unreachable by any token) leaves this "
                           "line's own defect as permanent, accepted "
                           "record noise")
REPAIR_TOKEN_RETRY = ("bookkeeping: a defective correcting line is "
                      "never itself a corrects target — whatever it "
                      "named still stands (superseding never edits "
                      "text): a fresh, single `corrects line <n>` "
                      "aimed at the intended target, carried "
                      "correctly this time, replaces this attempt")
# E-N (BACKLOG; dev-notes F205, relay 5): a `corrects line <n>` token
# placed in an entry's BASIS clause is invisible to apply_supersession
# — it scans only `e.body` — so the token resolves nothing and no
# violation ever fired: a silent no-op, the worst shape (the repair
# looked landed and repaired nothing). RESOLVER-UNREACHABLE by the
# same E-M principle even though this code is LINT-stage (unlike
# clause-unparsed): the defect IS the token sitting somewhere the
# resolver never searches, so printing a `corrects line {n}` form
# that a later entry could target would repeat the exact shape this
# class exists to catch. No {n} interpolation, no resolvable token.
REPAIR_CORRECTS_OUT_OF_BODY = (
    "bookkeeping: a `corrects line` token outside the entry body "
    "resolves against nothing — the token sheds under the SAME id, "
    "restated in the BODY where the resolver searches; a FRESH id "
    "re-declares any content the basis clause was actually naming, "
    "never a repair token")
# 0.2.84 B3: three sweep-stage codes minted this version had no
# REPAIR_FORMS entry, so annotate_repairs fell through to the
# "unclassified" placeholder for every hold they raised.
# E-M's own rule binds this one too: declarator-bookkeeping is raised
# on the CORRECTING line (apply_supersession's own complaint, like
# corrects-nothing/multi-corrects-token), never on a `violated`-map
# target — so its printed repair names the form in prose, never a
# literal `corrects line {n}` token the resolver could never target
# (that `n` would resolve to this defective line's own number).
REPAIR_DECLARATOR_BOOKKEEPING = (
    "supersede-whole: restate the full write-set under the same id "
    "and the same unit, with a trailing `(corrects line <n>)` naming "
    "the ORIGINAL target — never this line's own number; the one "
    "legal slot for the token on a write-set declarator line")
REPAIR_FOREIGN_ID_SUSPECT = (
    "name the record before the id (tracker path or run label), or, "
    "for a genuine same-run id, correct the citing line")
REPAIR_LANDING_MISSING = (
    "append the landing annotation line for the committed sha")

MACHINE_TOKEN_CODES = {
    "entry-form", "tag-enum", "entry-near-miss", "scope-near-miss",
    "hold-form", "write-set-near-miss", "write-set-path-near-miss",
    "tripwire-arm-near-miss",
}
BODY_CONTENT_CODES = {
    "tag-literal-in-body", "basis-missing",
    "superseded-block-form", "landing-indent", "landing-blank",
    "intent-near-miss",
}
# P15: clause-unparsed and killerless-dead share REPAIR_SWEEP_EXEMPT_ROUTE
# (defined above) rather than a set-driven comprehension here — both are
# resolver-unreachable by construction (E-M), and repair_class's generic
# "unreachable" branch fires on any form that is not REPAIR_BOOKKEEPING,
# so no dedicated set is needed to keep that property.
# apply_supersession's own complaint codes (E-M, widened): a defective
# corrects-token is a machine-token defect too, but on the CORRECTING
# line, not a target — REPAIR_SUPERSEDE's "restate under the same id
# with `corrects line {n}`" would have n resolve to the correcting
# line's OWN number, which the `violated` map can never contain.
SELF_TARGET_UNREACHABLE_CODES = {
    "multi-corrects-token", "repair-tag-change", "repair-scope-change",
}
REPAIR_FORMS = dict(
    [(c, REPAIR_SUPERSEDE) for c in MACHINE_TOKEN_CODES]
    + [(c, REPAIR_BOOKKEEPING) for c in BODY_CONTENT_CODES]
    + [(c, REPAIR_SWEEP_EXEMPT_ROUTE) for c in
       ("clause-unparsed", "killerless-dead")]
    + [("corrects-nothing", REPAIR_CORRECTS_NOTHING)]
    + [(c, REPAIR_TOKEN_RETRY) for c in SELF_TARGET_UNREACHABLE_CODES]
    + [(c, REPAIR_HEADER) for c in
       ("status-enum", "phase-enum", "admission-window")]
    + [(c, REPAIR_STATUS_LINE) for c in
       ("pending-latest", "basis-cites-invalidated")]
    + [("corrects-token-out-of-body", REPAIR_CORRECTS_OUT_OF_BODY)]
    + [("declarator-bookkeeping", REPAIR_DECLARATOR_BOOKKEEPING)]
    + [("foreign-id-suspect", REPAIR_FOREIGN_ID_SUSPECT)]
    + [("landing-missing", REPAIR_LANDING_MISSING)])


def annotate_repairs(violations, line_ids=None):
    """Attach each violation's repair form, addressed at its own line.

    tag-literal-in-body is OWNER-CONDITIONED (begehung-harvest 2
    finding 2, probe B): on a line that parsed no entry (`line_ids`
    carries no id for it — a header, INTENT, or bare-prose line), the
    tool must not recommend the ordinary bookkeeping shed, since no
    token can legally reach it (repair_class enforces the same rule
    at apply time); the desk is shown the hold instead."""
    line_ids = line_ids or {}
    for v in violations:
        if v["code"] == "tag-literal-in-body" and v["line"] not in line_ids:
            form = REPAIR_INTENT_HOLD
        else:
            form = REPAIR_FORMS.get(
                v["code"],
                "unclassified: this violation's repair form is not settled")
        v["repair"] = form.format(n=v["line"], code=v["code"])
    return violations


def violation_site(codes):
    return ("machine-token"
            if any(c in MACHINE_TOKEN_CODES for c in codes)
            else "body-content")


def repair_class(codes, owner=None):
    """Which of the three REPAIR_FORMS classes a violated line's codes
    settle a `corrects line <n>` token into: 'supersede' when any code
    is a MACHINE_TOKEN_CODES member (REPAIR_SUPERSEDE — the semantics
    every gate reads); 'bookkeeping' only when EVERY code at the line
    declares REPAIR_BOOKKEEPING; else 'unreachable' — REPAIR_HEADER,
    REPAIR_STATUS_LINE, REPAIR_INTENT_HOLD, or an unclassified code,
    none of which a token sheds (consulted at the decision point, per
    the table these forms already state — Finding 2, tier2-without.md
    parts 3/7-4/7).

    `tag-literal-in-body` is OWNER-CONDITIONED, this code only (no
    general owner rule — an ordinary entry's near-miss repair stays
    reachable regardless of owner): `owner` is the target line's
    parsed id (line_ids.get(n)), or None when the line parsed no
    entry at all. An owner-less target is exactly the header/INTENT
    shape SKILL.md holds "for the run's life" (probe B) — no
    bookkeeping token reaches it there, whatever the code's general
    classification says for an ordinary entry body."""
    if any(c in MACHINE_TOKEN_CODES for c in codes):
        return "supersede", None
    if "tag-literal-in-body" in codes and owner is None:
        return "unreachable", REPAIR_INTENT_HOLD
    forms = {REPAIR_FORMS.get(c) for c in codes}
    if forms == {REPAIR_BOOKKEEPING}:
        return "bookkeeping", None
    declared = next((REPAIR_FORMS.get(c) for c in codes
                     if REPAIR_FORMS.get(c) != REPAIR_BOOKKEEPING), None)
    return "unreachable", declared


@dataclass
class Entry:
    lineno: int
    cls: str
    id: str
    tag: str
    body: str
    basis: str | None


BROKEN_PIPE = False


def emit(text):
    """Write one line at the BYTE level (ES-9): the tracker is bytes,
    so a byte quoted in a violation or a quote block leaves as the byte
    it arrived as. The text layer's blanket errors='replace' would mint
    a SECOND spelling on output — the very thing the input-side decode
    rule exists to prevent (attack-11 N6).

    A closed reader (`| head`) breaks the pipe mid-run: an evidence
    line's write is swallowed here — best-effort, the reader already
    stopped listening — and the fact is remembered so the CLOSING
    verdict falls back to stderr instead of dying on the same broken
    pipe with no verdict line at all and exit 0 (finding 5,
    tier2-without.md part 7/7)."""
    global BROKEN_PIPE
    if BROKEN_PIPE:
        return
    try:
        sys.stdout.flush()
        sys.stdout.buffer.write(text.encode("utf-8", "surrogateescape") + b"\n")
        sys.stdout.buffer.flush()
    except BrokenPipeError:
        BROKEN_PIPE = True


def say(msg):
    emit(msg)


def _stderr_fallback(text):
    statiker_emit.stderr_fallback(text)


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
    # st-32 lap B: one lookup, no gate-logic change — a name the
    # registry lacks stamps "unrouted" (statiker_emit.ROUTES; design
    # docs/directives/2026-09-12-st32-lapB-design-statiker-a5.md §1).
    route = statiker_emit.ROUTES.get(verdict, "unrouted")
    text = VERDICT_PREFIX + json.dumps({"verdict": verdict, "route": route,
                                        **detail}, ensure_ascii=False)
    if BROKEN_PIPE:
        # stdout is already gone — the one-verdict-line guarantee's
        # last stderr-safe attempt, exit reporting the broken pipe
        # rather than the caller's own exit_code
        _stderr_fallback(text)
        _exit_after_broken_pipe(3)
    emit(text)
    if BROKEN_PIPE:
        # the verdict line itself was the write that broke
        _stderr_fallback(text)
        _exit_after_broken_pipe(3)
    sys.exit(exit_code)


# ------------------------------------------------------------- pure functions

def classify_scope(body: str):
    m = re.match(r"unit (U\d+)\b", body)
    if m:
        return ("unit", m.group(1))
    if body.startswith("record:"):
        return ("record", None)
    if OUT_OF_SCOPE_RE.match(body):
        return ("out-of-scope", None)
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


def write_set_violations(body: str, tag: str):
    """Positional near-miss on the write-set declarator, mirroring
    hold_violations' shape but scoped strictly to a body opened by an
    EXACT `unit U<k> ` prefix — write-set has no scopeless or displaced
    spelling to catch, unlike the hold form.

    Once the declarator itself parses, a LIVE line's PATH FIELD gets
    the same positional treatment (begehung-harvest 2, finding 3):
    whitespace inside the field reads as two paths on one line — the
    grammar is one repo-root-relative path per line, so
    `UNIT_WRITE_SET_RE`'s `(\\S.*)` swallowing a second path made two
    colliding units read disjoint and parallel-eligible — and a
    leading `/` is an alias outside the grammar (an absolute or
    symlinked spelling), a declaration defect the desk composes,
    caught here rather than silently normalized or silently accepted.
    An INVALIDATED line is exempt: its trailing prose (the standing
    `dead (mis-scoped)`-style annotation) is disposal commentary, not
    a second declared path, and the line is already excluded from
    every collision computation by tag alone (waves_over_units). A
    trailing `(corrects line <n>)` is exempt the same way (0.2.85,
    the B4 residue): it is the grammar's one legal slot for a
    supersede-whole redeclaration's own resolving token — the SAME
    id's declarator line, restated whole and marked as the
    correction (declarator-bookkeeping, SKILL.md, Stop rule) — never
    a second declared path, and stripped before the check so any
    OTHER multi-token content still fires."""
    scrubbed = BACKTICK_RE.sub(" ", body)   # quoting a literal is legal
    m = UNIT_SCOPE_RE.match(scrubbed)
    if not m:
        return []
    rest = scrubbed[m.end():]
    if WRITE_SET_EXACT_RE.match(rest):
        # 0.2.85 RB1/N2: the shared suffix-strip helper
        # (_strip_write_set_corrects_suffix, below) strips the
        # corrects-suffix, reused here rather than a second, divergent
        # strip — UNNORMALIZED: normpath is the consuming site's own
        # step (_normalize_write_set_path, waves_over_units alone) and
        # must never run here, or a real second path or leading-`/`
        # defect collapses away through an embedded `..` before this
        # check ever sees it (N2: `a.txt b/../c.txt` read clean under
        # normpath).
        path = _strip_write_set_corrects_suffix(rest[len("write-set: "):])
        if tag != "INVALIDATED" and (
                len(path.split()) > 1 or path.startswith("/")):
            return ["write-set-path-near-miss"]
        return []
    if WRITE_SET_NEAR_RE.match(rest):
        return ["write-set-near-miss"]
    return []


def irreversible_tag(body: str):
    """P4: the positional irreversible form on a record line's body —
    `unit U<k> irreversible: <effect>`, checked directly (the pattern
    already carries the `unit U<k> ` opener, unlike hold/write-set's
    strip-then-check). Quoting a literal is legal, as elsewhere.
    Returns (unit, effect) or None — a field lookup, never a
    violation list: no near-miss class exists in this version."""
    scrubbed = BACKTICK_RE.sub(" ", body)
    m = IRREVERSIBLE_EXACT_RE.match(scrubbed)
    if not m:
        return None
    return f"U{m.group(1)}", m.group(2).strip()


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


# P32 (BACKLOG.md:171, F66): the seed's F25 cited the U1 record's
# entries as bare ids; the live-basis check resolves every cited id
# in THIS run's namespace, so once this run minted its own
# same-numbered id, a foreign citation silently rested on it. The
# basis rule (SKILL.md, The record): a basis citing another record
# names the record (tracker path or run name) BEFORE its ids. A
# record-name token is a token containing "/" AND ending ".md" or
# ".md:" — a tracker path, never a code pointer like `tools/x.py:40`
# (0.2.84 B2: the prior `(/|:$)` form over-matched both that and any
# ordinary `label:`, silently exempting same-run ids it should not
# have). The two-token label `run <name>:` is checked separately
# (basis_id_citations, below). Scoped to the LIVE-BASIS check alone
# (sweep_checks) — trend's concentration read (cited_ids, above)
# is unaffected by design, since it grades THIS run's own repair ids
# regardless of any record-name prose beside them.
RECORD_NAME_TOKEN_RE = re.compile(r"/.*\.md:?$")


def basis_id_citations(basis: str):
    """Yields (id, foreign) for every id-shaped token in `basis` — the
    id-scoped read the live-basis check consumes. `foreign` is True
    when the id sits under an active record-name token — a token
    matching RECORD_NAME_TOKEN_RE, or the second token of the label
    `run <name>:` (the literal `run`, then a token ending `:`).

    0.2.84 B6: the prior form re-derived record-name-ness only from
    the token immediately before an id, so it reset after one id and
    a plural citation's second+ id (`tracker.md F20, F21`) fell
    through to a bare, unmarked lookup. Record-name state now PERSISTS
    across a contiguous run of id tokens (comma-attached or plain) and
    is only re-derived at the next NON-id token — it dies exactly at
    the first token that is not itself an id."""
    out = []
    record_name = False
    prev_tok = None
    for tok in (basis or "").split():
        # 0.2.84 B1: `,;` alone left `(F20)`, `F20)`, `F20.` invisible
        # to the id fullmatch — quoting/bracketing punctuation strips
        # too.
        bare = tok.strip("()[].,;:")
        if re.fullmatch(r"[FDRAV]\d+", bare):
            out.append((bare, record_name))
            prev_tok = tok
            continue
        # 0.2.85 RN-c: strip the same quoting/bracketing punctuation
        # set id tokens strip (B1, above) before the record-name
        # match — a trailing comma or bracket right after `.md` broke
        # the `$`-anchored match and left the id it introduced
        # unmarked as foreign.
        is_record_name = bool(
            RECORD_NAME_TOKEN_RE.search(tok.strip("()[].,;:")))
        if not is_record_name and prev_tok == "run" and tok.endswith(":"):
            is_record_name = True
        record_name = is_record_name
        prev_tok = tok
    return out


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
    """Return (entries, violations, meta, reach). Violations are
    lint-grade dicts {code, line, text}. `meta["entries"]` and
    `meta["head_boundary"]` ride every verdict (E-A); `reach` carries
    the auxiliary reach signals scoped to their own consumers rather
    than blanket-spread: `r_lines` (sweep/closure only),
    `head_region_entries` (an evidence line per entry-shaped line the
    head-region exclusion made invisible to every gate — every
    subcommand that parses a tracker prints one), `skill_versions`
    (P3, sweep/closure only: header entry first, then every mid-run
    `SKILL: statiker <version>` line in file order — attribution, never
    a gate), `irreversible_units` (P4, sweep/closure only: every
    `unit U<k> irreversible: <effect>` record-line body in file order
    — attribution, never a gate; unattended enforcement stays the
    UNIT_HELD hold entry), and `sweep_exempt` (P6, sweep only: every
    labeled `SWEEP_EXEMPT: <code> lines<=<n>` / `SWEEP_EXEMPT: <code>
    line <n>` declaration in file order — the netting input, not
    itself a gate)."""
    entries, violations = [], []
    line_ids = {}          # lineno -> the id the line NAMES, parsed or not
    line_parse = {}        # lineno -> what PARSED there (ES-4's pins)
    late_intent = []       # ES-2: the labeled mid-run INTENT lines
    skill_version_lines = []  # P3: labeled mid-run SKILL: version lines
    irreversible_lines = []   # P4: unit U<k> irreversible: <effect> lines
    sweep_exempt_lines = []   # P6: labeled SWEEP_EXEMPT declarations
    landed_units = set()      # P24: units carrying ANY landing line,
                              # indented (sanctioned) or not (still a
                              # landing statement, separately lint-held)
    lines = split_lines(text)

    # ES-1: surface 1 begins at the first `## ` heading — E-L: unless
    # that first heading is titled "Requirement head" (case-
    # insensitive), which does not terminate the head: the region
    # then extends to the NEXT `## ` heading, or EOF when none follows.
    head_end = len(lines) + 1
    first_heading = None
    for i, line in enumerate(lines, 1):
        if HEAD_BOUNDARY_RE.match(line):
            first_heading = i
            break
    if first_heading is not None:
        if REQUIREMENT_HEAD_TITLE_RE.match(lines[first_heading - 1]):
            head_end = len(lines) + 1
            for i in range(first_heading + 1, len(lines) + 1):
                if HEAD_BOUNDARY_RE.match(lines[i - 1]):
                    head_end = i
                    break
        else:
            head_end = first_heading

    # E-A: the two reach signals scoped to the head region, computed
    # once here whether or not any consumer prints them — an
    # entry-shaped line the exclusion makes invisible to every gate,
    # and the R-line count sweep/closure surface.
    head_region_entries = [{"line": i, "text": line}
                           for i, line in enumerate(lines, 1)
                           if i < head_end and SIGNATURE_RE.match(line)]
    r_lines = sum(1 for i, line in enumerate(lines, 1)
                 if i < head_end and R_LINE_RE.match(line))

    status_line = phase_line = None
    status_val = phase_val = None
    # E-G' (begehung-harvest T14 mechanical half, WITHOUT-F8 +
    # SENTENCE-B4): Mode and Budget are literal header-line reads, the
    # same shape as Status/Phase — no enum, no admission window, they
    # are surfaced, never gated.
    mode_line = budget_line = skill_line = None
    mode_val = budget_val = skill_val = None
    for i, line in enumerate(lines, 1):
        if status_line is None and line.startswith("Status:"):
            status_line, status_val = i, line[len("Status:"):].strip()
        if phase_line is None and line.startswith("Phase:"):
            phase_line, phase_val = i, line[len("Phase:"):].strip()
        if mode_line is None and line.startswith("Mode:"):
            mode_line, mode_val = i, line[len("Mode:"):].strip()
        if budget_line is None and line.startswith("Budget:"):
            budget_line, budget_val = i, line[len("Budget:"):].strip()
        if skill_line is None and line.startswith("Skill:"):
            skill_line, skill_val = i, line[len("Skill:"):].strip()

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
        m_land = LANDING_RE.match(line) or LANDING_INDENTED_RE.match(line)
        if m_land:
            landed_units.add(m_land.group(1))
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

        m = SKILL_VERSION_EXACT_RE.match(line)  # P3
        if m:
            skill_version_lines.append({"line": i, "version": m.group(1)})
            continue

        m = IRREVERSIBLE_EXACT_RE.match(line)  # P34: the SKILL:'s sibling
        if m:                                  # label-line form (SKILL.md
            irreversible_lines.append(          # :730-731): a bare line at
                {"unit": f"U{m.group(1)}", "line": i,  # column 0, never an
                 "effect": m.group(2).strip()})  # entry, re-opens nothing
            continue

        m = SWEEP_EXEMPT_CEILING_RE.match(line)  # P6
        if m:
            sweep_exempt_lines.append({"line": i, "code": m.group(1),
                                       "kind": "ceiling",
                                       "bound": int(m.group(2))})
            continue
        m = SWEEP_EXEMPT_LINE_RE.match(line)
        if m:
            sweep_exempt_lines.append({"line": i, "code": m.group(1),
                                       "kind": "single",
                                       "bound": int(m.group(2))})
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
        if basis and CORRECTS_RE.search(basis):
            # E-N: the resolver (apply_supersession) scans only
            # e.body — a token sitting in the basis clause is
            # invisible to it and resolves nothing, silently
            viol("corrects-token-out-of-body", i, line)
        # 0.2.89 fix (B3): checked unconditionally on body_main, ahead
        # of scope parsing below — a malformed scope opener (e.g.
        # `Record: tripwire armed…`) already lints scope-near-miss,
        # but this class must ALSO catch a fine scope opener whose
        # class/tag or trailing shape breaks cmd_tripwire's own filter
        # (cls == "F" and tag == "VERIFIED" and TRIPWIRE_ARM_RE.match).
        if TRIPWIRE_ARM_NEAR_RE.match(body_main) and not (
                cls == "F" and tag == "VERIFIED"
                and TRIPWIRE_ARM_RE.match(body_main)):
            viol("tripwire-arm-near-miss", i, line)
        scope_parsed = True
        if SCOPE_NEAR_RE.match(body_main) and \
                not SCOPE_EXACT_RE.match(body_main):
            viol("scope-near-miss", i, line)
            scope_parsed = False               # the opener IS the violation
        else:
            for code in hold_violations(body_main, tag):
                viol(code, i, line)
            for code in write_set_violations(body_main, tag):
                viol(code, i, line)
            irr = irreversible_tag(body_main)          # P4
            if irr:
                unit, effect = irr
                irreversible_lines.append(
                    {"unit": unit, "line": i, "effect": effect})
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
    annotate_repairs(violations, line_ids)
    meta = {"status": status_val, "phase": phase_val,
            "late_intent": late_intent, "entries": len(entries),
            "head_boundary": head_end,
            "mode": mode_val, "budget": budget_val}
    # P3: header entry first (if the header carries one), then every
    # body SKILL: line in file order — scoped to sweep/closure only
    # (reach's own scoping convention, docstring above), never lint.
    skill_versions = []
    if skill_line is not None:
        hm = SKILL_HEADER_VERSION_RE.match(skill_val) if skill_val else None
        skill_versions.append({"line": skill_line,
                               "version": hm.group(1) if hm else skill_val})
    skill_versions.extend(skill_version_lines)
    reach = {"r_lines": r_lines, "head_region_entries": head_region_entries,
             "skill_versions": skill_versions,
             "irreversible_units": irreversible_lines,
             "sweep_exempt": sweep_exempt_lines,
             "landed_units": landed_units}
    return entries, violations, meta, reach


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
    exactly ONE token, the one naming the line it corrects).

    P38 (BACKLOG.md:47, F147): a `corrects line <n>` token whose OWN id
    is a DECLARATOR — the same id's most recent EARLIER line is a
    `unit U<k> write-set: <path>` declaration — and whose target `n`
    is older than that declaration is refused before dispatch: under
    plain latest-line-wins the correcting line would become the id's
    resolved body, un-declaring the path though a live declaration for
    it still stands. Neither superseded nor shed; the correcting
    line's own lineno is excluded from the returned entries too (as if
    the append never happened), so it can never become the id's latest
    line in a downstream `latest_by_id` read. The repair is the
    same-id, same-unit supersede-whole form (st-30(1)): restate the
    full write-set under the same id and unit with a trailing
    `(corrects line <n>)` naming the original target — never a fresh
    id.

    P37 (BACKLOG.md:74, F130): a correcting line whose own restatement
    opens the wrong scope against what its target parsed draws
    repair-scope-change/repair-tag-change (_repair_pin_complaints) -
    SELF_TARGET_UNREACHABLE, no token can ever supersede a defective
    correcting line itself. Held pending rather than appended
    immediately: once ANY corrects-token against the SAME target
    resolves cleanly (site supersede, zero repair-pin complaints),
    every defective attempt against that target sheds - the
    successful retry IS the defective line's repair, keyed on the
    retry's outcome, never on which line came first; a target with no
    clean resolution leaves its defective attempts' violations
    standing, the only case an operator SWEEP_EXEMPT still reaches."""
    violated = {}
    for v in violations:
        violated.setdefault(v["line"], []).append(v["code"])
    by_id = {}
    for e2 in entries:
        by_id.setdefault(e2.id, []).append(e2)
    superseded, shed, bookkeeping, declarator_refused = (
        set(), set(), set(), set())
    complaints = []
    pending_pin_complaints = []   # [(target n, [complaint dicts])]
    clean_supersede_targets = set()
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
            prior_same_id = [e2 for e2 in by_id.get(e.id, [])
                             if e2.lineno < e.lineno]
            latest_same_id = (max(prior_same_id, key=lambda e2: e2.lineno)
                              if prior_same_id else None)
            # 0.2.84 B4: fire only when the CORRECTING entry is not
            # itself a fresh write-set redeclaration — the tool's own
            # prescribed supersede-whole repair for this shape (B3's
            # REPAIR_DECLARATOR_BOOKKEEPING text); firing on it too
            # refused the only repair the grammar makes reachable.
            # 0.2.85 RB2: B4's exemption tested SHAPE only, not UNIT —
            # a DIFFERENT unit's write-set redeclaration under the
            # declarator id passed the same shape test and silently
            # un-declared the live write-set under latest-line-wins
            # (P38's own docstring sentence, a different trigger).
            # The exemption now also requires the correcting line's
            # own unit to equal latest_same_id's.
            # 0.2.85 RN-a: SKILL.md's own prose already says the
            # refusal fires on the latest EARLIER line being a LIVE
            # write-set declaration; the tool never checked the tag,
            # so an [INVALIDATED] latest_same_id (already excluded
            # from waves_over_units by tag alone) still drew the
            # complaint though nothing live stands to be un-declared.
            latest_ws_m = UNIT_WRITE_SET_RE.match(latest_same_id.body) \
                if latest_same_id is not None else None
            e_ws_m = UNIT_WRITE_SET_RE.match(e.body)
            if (latest_same_id is not None and n < latest_same_id.lineno
                    and latest_ws_m
                    and latest_same_id.tag != "INVALIDATED"
                    and not (e_ws_m
                             and e_ws_m.group(1) == latest_ws_m.group(1))):
                complaints.append(
                    {"code": "declarator-bookkeeping", "line": e.lineno,
                     "text": f"{e.id}: `corrects line {n}` reuses "
                             f"declarator id {e.id} — its latest line "
                             f"({latest_same_id.lineno}) is a write-set "
                             "declaration, and a correction appended "
                             "under the same id un-declares it under "
                             "latest-line-wins; repair with the same-id, "
                             "same-unit supersede-whole form"})
                declarator_refused.add(e.lineno)
                continue
            site, declared = repair_class(violated[n], owner)
            if site == "supersede":
                superseded.add(n)
                pin_complaints = _repair_pin_complaints(e, n, line_parse)
                if pin_complaints:
                    pending_pin_complaints.append((n, pin_complaints))
                else:
                    clean_supersede_targets.add(n)
            elif site == "bookkeeping":
                shed.add(n)
                bookkeeping.add(e.lineno)
            else:
                complaints.append(
                    {"code": "corrects-nothing", "line": e.lineno,
                     "text": f"{e.id}: `corrects line {n}` names a "
                             f"violation no repair token reaches — "
                             f"{declared}"})
    # P37: a defective attempt's own repair-pin violation sheds once
    # ANY corrects-token against the same target succeeded cleanly.
    for n, pin_complaints in pending_pin_complaints:
        if n not in clean_supersede_targets:
            complaints += pin_complaints
    return ([e for e in entries
             if e.lineno not in superseded and e.lineno not in bookkeeping
             and e.lineno not in declarator_refused],
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

CLIPPY_RUNS_PREFIX = ".clippy" + os.sep + "runs" + os.sep


def say_head_region_entries(cmd, reach):
    """E-A evidence line: an entry-shaped line the head-region
    exclusion (ES-1) makes invisible to every gate — printed, never
    gated, so a clean verdict over such a tracker is distinguishable
    from a clean verdict over an examined one."""
    for hr in reach["head_region_entries"]:
        say(f"{cmd}: entry-shaped line in the head region (parses as "
            f"nothing there) @ line {hr['line']}: {hr['text']}")


def gap_filling_ids(entries):
    """E-E(2) (begehung-harvest WITH-B4): a NEW id — its FIRST
    occurrence in the file — below its class's already-allocated
    maximum is near-certainly a namespace collision, not a status
    change (WITH-B4's own disclaimer: "genuinely semantic in the
    general case, since re-using an id for a status change is the
    core append-only design" — an ordinary status-change REUSE of an
    id already seen is not a first occurrence and does not fire).
    Returns a list of {line, id} in file order."""
    seen, max_num, hits = {}, {}, []
    for e in entries:
        n = int(e.id[1:])
        s = seen.setdefault(e.cls, set())
        if e.id not in s:
            cur_max = max_num.get(e.cls)
            if cur_max is not None and n < cur_max:
                hits.append({"line": e.lineno, "id": e.id})
            s.add(e.id)
        max_num[e.cls] = max(max_num.get(e.cls, n), n)
    return hits


def freeze_breach_violations(entries):
    """E-F (begehung-harvest F7): the append freeze is decidable from
    the tracker, not desk memory alone — a live round is the LATEST
    A-line (latest-by-id, ordered by its own line) tagged [DISPATCHED]
    with no resolving line, exactly the window `trend_over_rounds`
    already parses for its own `rounds_a` filter. Any F/D/R entry
    appended after it is a breach: material that should have queued
    for the round's return landed in the live record instead."""
    latest = latest_by_id(entries)
    a_latest = sorted([e for e in latest.values() if e.cls == "A"],
                      key=lambda e: e.lineno)
    if not a_latest or a_latest[-1].tag != "DISPATCHED":
        return []
    freeze_a, freeze_at = a_latest[-1], a_latest[-1].lineno
    out = []
    for e in entries:
        if e.cls in ("F", "D", "R") and e.lineno > freeze_at:
            out.append({
                "code": "freeze-breach", "line": e.lineno,
                "text": f"{e.id}: appended after {freeze_a.id} [DISPATCHED] "
                        f"(line {freeze_at}) with no resolving line — the "
                        "round's own queue, not the live record",
                "repair": "freeze breach: no repair token reaches it — the "
                          "desk resolves the round (or the breach itself) "
                          "before the record continues"})
    return out


def cmd_lint(args):
    _, rel, _, _ = repo_paths(args.tracker)
    entries, violations, meta, reach = parse_tracker(load(args.tracker))
    say_head_region_entries("lint", reach)
    if rel is not None and not rel.startswith(CLIPPY_RUNS_PREFIX):
        # E-A (begehung-harvest B6): the stats reader admits a run only
        # under .clippy/runs/ — a tracker anywhere else passes every
        # gate here and is permanently invisible to that reader.
        # Evidence only; the record tool names no home of its own.
        say(f"lint: tracker path not under {CLIPPY_RUNS_PREFIX.rstrip(os.sep)}/: {rel}")
    for hit in gap_filling_ids(entries):
        say(f"lint: gap-filling id {hit['id']} @ line {hit['line']}: "
            f"below its class's already-allocated maximum — near-certainly "
            f"a namespace collision, not a status change")
    violations = violations + freeze_breach_violations(entries)
    for v in violations:
        say(f"lint: {v['code']} @ line {v['line']}: {v['text']}")
    if violations:
        finish("LINT_VIOLATIONS", 2, violations=violations, **meta)
    finish("LINT_CLEAN", 0, **meta)


def sweep_checks(entries, landed_units=frozenset()):
    violations = []
    latest = latest_by_id(entries)

    for id_, e in sorted(latest.items(), key=lambda kv: kv[1].lineno):
        if e.tag == "PENDING":
            violations.append({"code": "pending-latest", "line": e.lineno,
                               "text": f"{id_} latest line is [PENDING]"})

    # P24 (begehung R4): nothing FORCES the landing annotation at
    # landing time — U2's original landing shipped without one and the
    # close composed it by hand from the F164 chain. A unit whose
    # record shows UNIT_COMMITTED evidence (a body quoting the git
    # tool's verdict, the same shape EXTRAS/RESIDUE already ask the
    # desk to book) but carries no landing line anywhere in the
    # tracker holds — attribution surfaced, never silently lost.
    committed_without_landing = {}
    for e in entries:
        scope, unit = classify_scope(e.body)
        # 0.2.84 N2: the desk's own prescribed non-landed-unit return
        # (SKILL.md:1481-1483) is a `record:`-scoped F-line naming the
        # unit in prose — scope=="unit" alone missed every one of them.
        if scope == "record" and UNIT_COMMITTED_EVIDENCE_RE.search(e.body):
            m = re.search(r"\bunit (U\d+)\b", e.body)
            if m:
                scope, unit = "unit", m.group(1)
        if (scope == "unit" and unit not in landed_units
                and UNIT_COMMITTED_EVIDENCE_RE.search(e.body)
                and unit not in committed_without_landing):
            committed_without_landing[unit] = e
    for unit in sorted(committed_without_landing,
                       key=lambda u: int(u[1:])):
        e = committed_without_landing[unit]
        violations.append(
            {"code": "landing-missing", "line": e.lineno,
             "text": f"{unit}: UNIT_COMMITTED evidence at {e.id} with no "
                     "landing annotation anywhere in the tracker"})

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

    # P32: this run's own per-class max — a bare (unmarked) citation
    # whose number exceeds it could never be one of this run's own
    # ids (the backstop for the under-max case, which count alone
    # cannot catch — the SKILL.md basis-naming rule is the primary
    # carrier there).
    run_max_by_cls = {}
    for e in entries:
        n = int(e.id[1:])
        if n > run_max_by_cls.get(e.cls, 0):
            run_max_by_cls[e.cls] = n

    for id_, e in latest.items():
        if e.tag == "INVALIDATED":
            continue
        for cited, foreign in basis_id_citations(e.basis or ""):
            if foreign:
                # 0.2.85 B1 (checkpoint-review disposition, RN-b
                # WITHDRAWN): a record-named id that also resolves in
                # THIS run's own namespace could not be discriminated
                # by the tool (the foreign record's id, or this run's
                # own possibly-dead one?) — RN-b minted a SUBSTANCE
                # hold for it, but field reading found 0 record-named
                # citations in 1006 basis lines across three real
                # trackers: a reviewer-constructed hole with no field
                # incident, closing an unattended run FAILED on a
                # correct citation. The exemption stops discriminating
                # here and always has: an id under a record-name token
                # is not checked against this run's own invalidations
                # — the accepted residual, pinned by test rather than
                # left silent (TestB1AmbiguousCitationWithdrawn).
                continue
            c = latest.get(cited)
            if c is not None and c.tag == "INVALIDATED":
                violations.append(
                    {"code": "basis-cites-invalidated", "line": e.lineno,
                     "text": f"{id_} (live) rests on {cited}, whose latest "
                             "line is [INVALIDATED]"})
            cls, num = cited[0], int(cited[1:])
            if num > run_max_by_cls.get(cls, 0):
                violations.append(
                    {"code": "foreign-id-suspect", "line": e.lineno,
                     "text": f"{id_}: basis cites {cited}, which exceeds "
                             f"this run's own {cls}-class max "
                             f"({run_max_by_cls.get(cls, 0)}) — likely a "
                             "foreign-record id missing its record-name "
                             "prefix"})

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


def net_sweep_exemptions(violations, exemptions):
    """P6: nets declared SWEEP_EXEMPT holds out of the blocking set —
    the BLOCKING calculus P2's lock gate and every [READY] read consult
    through the sweep verdict, no separate git-tool change. A violation
    matches an exemption when the CODE agrees and the violation's line
    falls within the exemption's coverage, frozen at declaration:
    `lines<=N` covers 1..N, `line N` covers exactly N — a violation
    above the ceiling is untouched, still blocking. The first matching
    declaration (file order) is the one attributed. Returns
    (blocking, exempt_holds); each exempt_holds entry carries the
    netted violation plus the exemption's own declaring line.
    UNEXEMPTIBLE codes (opus release review H6, 2026-08-16): the
    defang class — SKILL.md, The record: an undefanged bracketed tag
    literal holds every later sweep correctly, for the run's life —
    is never netted, whatever a declaration says; the declaration is
    simply inert for those codes and the hold stays blocking."""
    blocking, exempt_holds = [], []
    for v in violations:
        if v["code"] in UNEXEMPTIBLE_CODES:
            blocking.append(v)
            continue
        # M5 (round 3): coverage clamps at the declaring line —
        # nothing appended after the declaration is ever netted,
        # whatever <n> says, so no exemption becomes a standing one.
        hit = next((e for e in exemptions if e["code"] == v["code"] and (
            (e["kind"] == "ceiling"
             and v["line"] <= min(e["bound"], e["line"])) or
            (e["kind"] == "single"
             and v["line"] == e["bound"] and e["bound"] < e["line"]))),
            None)
        if hit is None:
            blocking.append(v)
        else:
            exempt_holds.append({**v, "exempt_declared_line": hit["line"]})
    return blocking, exempt_holds


def cmd_sweep(args):
    entries, violations, meta, reach = parse_tracker(load(args.tracker))
    say_head_region_entries("sweep", reach)
    sweep_viols, clause_dispositions = sweep_checks(
        entries, reach["landed_units"])
    violations += annotate_repairs(sweep_viols)
    violations += freeze_breach_violations(entries)
    violations, retro_holds = net_retro_holds(violations,
                                              reach["skill_versions"])
    violations, exempt_holds = net_sweep_exemptions(
        violations, reach["sweep_exempt"])
    for v in violations:
        say(f"sweep: {v['code']} @ line {v['line']}: {v['text']}")
    for v in retro_holds:
        say(f"sweep: retro {v['code']} @ line {v['line']}: netted — line "
            f"predates the code's mint ({RULE_MINT_VERSION.get(v['code'])})")
    for v in exempt_holds:
        say(f"sweep: exempt {v['code']} @ line {v['line']}: netted by "
            f"SWEEP_EXEMPT at line {v['exempt_declared_line']}")
    # E-G' (WITHOUT-F8 + SENTENCE-B4): Budget is a literal header read
    # (like Status/Phase) — the field's OWN grammar is already declared
    # (SKILL.md, The record: `Budget: cycles <n> / rounds <n> / verify
    # <n>`), so trend's resolved-round count is consulted against the
    # ROUNDS component specifically, never the whole string as a bare
    # int. An EVIDENCE line, never a gate; no rounds component (a
    # malformed or absent Budget) checks nothing.
    if meta["budget"] is not None:
        m = BUDGET_ROUNDS_RE.search(meta["budget"])
        if m:
            budget_n = int(m.group(1))
            bounds, _, _, _, _ = trend_over_rounds(entries)
            if len(bounds) >= budget_n:
                say(f"sweep: resolved rounds ({len(bounds)}) meet/exceed "
                    f"Budget (rounds {budget_n})")
    say("judgment residue (desk work, not checked here): dead-basis "
        "body-reads, duplicate-id body-read, restatement adoption "
        "checks, basis reach")
    detail = {"clause_dispositions": clause_dispositions,
             "r_lines": reach["r_lines"],
             "skill_versions": reach["skill_versions"],
             "irreversible_units": reach["irreversible_units"],
             "exempt_holds": exempt_holds,
             "retro_holds": retro_holds, **meta}
    if violations:
        finish("SWEEP_HOLDS", 2, violations=violations, **detail)
    finish("SWEEP_CLEAN", 0, **detail)


# ------------------------------------------------------------------- closure

CLOSURE_BLOCKING_CODES = ("entry-form", "tag-enum", "entry-near-miss",
                          "scope-near-miss", "hold-form",
                          "write-set-near-miss", "write-set-path-near-miss")


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


def out_of_scope_undispositioned(entries):
    """P25 (BACKLOG; run-2 F77): the leavings gate's blocking set — an
    F-id GRADED out-of-scope by ANY historical line (the grade is
    append-only sticky, so a later status line need not repeat the
    `out-of-scope: ` opener to keep the id tracked) whose LATEST line
    carries no disposition clause (`— exported: ` or `— dropped: `,
    OUT_OF_SCOPE_DISPOSITION_RE — a decision-graded export ref or a
    one-line recorded drop, either satisfies it, wherever in the
    latest line's body it sits). Sorted by id number for a stable
    printed order."""
    latest = latest_by_id(entries)
    graded = {e.id for e in entries
             if e.cls == "F" and OUT_OF_SCOPE_RE.match(e.body)}
    out = []
    for id_ in sorted(graded, key=lambda i: int(i[1:])):
        e = latest[id_]
        if OUT_OF_SCOPE_DISPOSITION_RE.search(e.body):
            continue
        out.append({"id": id_, "line": e.lineno,
                    "text": f"{e.id} [{e.tag}] {e.body}"})
    return out


def cmd_closure(args):
    if args.unit is not None and not re.fullmatch(r"U\d+", args.unit):
        # attack-8 N3: a mistyped id ("3", "u3") matched no scope line
        # and fell through to UNIT_DISPATCHABLE — a silent hold-clear
        finish("USAGE_ERROR", 3,
               error=f"--unit must match U<k>, got {args.unit!r}")
    entries, violations, meta, reach = parse_tracker(load(args.tracker))
    say_head_region_entries("closure", reach)
    # ES-2: every closure verdict lists the labeled late-INTENT lines —
    # verify's composition grades against the head PLUS these, and the
    # tool is what finds them. E-A: entries/head_boundary ride every
    # verdict, r_lines rides sweep/closure's. E-G': the Mode line rides
    # the same way (surfaced, never gated) — absent-Mode reads None.
    # P3/P4: skill_versions and irreversible_units ride sweep/closure's
    # the same way r_lines does.
    late = {"late_intent": meta["late_intent"], "entries": meta["entries"],
           "head_boundary": meta["head_boundary"], "r_lines": reach["r_lines"],
           "mode": meta["mode"], "skill_versions": reach["skill_versions"],
           "irreversible_units": reach["irreversible_units"]}
    blocking = closure_blocking_violations(violations)
    if blocking:
        for v in blocking:
            say(f"closure blocked: {v['code']} @ line {v['line']}: "
                f"{v['text']}")
        finish("CLOSURE_RECORD_MALFORMED", 2, violations=blocking, **late)
    a_lines = [e for e in entries if e.cls == "A"]
    if not a_lines:
        finish("CLOSURE_ABSENT", 2, last_a=None, **late)
    closing = a_lines[-1]
    if closing.tag not in ("ZERO-DELTA", "BIT"):
        finish("CLOSURE_ABSENT", 2,
               last_a=f"{closing.id} [{closing.tag}]", **late)
    design_amending = []
    if closing.tag == "BIT":
        # P27 (BACKLOG; run-2 A6, F118): design CONSEQUENCE, not
        # finding PRESENCE — a terminal [BIT] round whose disposition
        # set amends NO design entry (no D-class line follows it,
        # whatever the findings' own count or severity) grades the
        # closure SATISFIED, the same predicate as ZERO-DELTA from
        # here; one design-amending disposition (any D-class line
        # after this A-line) keeps it SHUT — the over-correction case.
        # Completes P20's record-class half (that gate reads FINDING
        # class at round-open; this one reads DISPOSITION consequence
        # at closure) — the presence-reading gate forced an operator
        # deviation (route 2, F118) to ship a thrice-verified unit
        # whose round's five findings none amended the design.
        #
        # P20xP27 (checkpoint review R1): "amends" reads the D-line's
        # SCOPE, not mere presence — a `record:`-opened D-line is desk
        # bookkeeping (never a design amendment, so it never bars
        # closure) and a `unit U<k>`-scoped D-line (the `held:` form
        # included) is a PER-UNIT concern the general unit_lines/
        # UNIT_HELD machinery below already reads, identically to
        # ZERO-DELTA — only a SCOPELESS D-line is a genuine
        # over-correction that keeps the whole closure shut. Net
        # effect: the terminal-BIT branch grades by the SAME predicate
        # as ZERO-DELTA, which is what this page's own prose already
        # promised.
        design_amending = [e for e in entries
                          if e.lineno > closing.lineno and e.cls == "D"
                          and classify_scope(e.body)[0] not in
                          ("record", "unit")]
        if design_amending:
            finish("CLOSURE_ABSENT", 2,
                   last_a=f"{closing.id} [{closing.tag}]",
                   design_amending=[e.id for e in design_amending], **late)
        say(f"closure: {closing.id} [BIT] SATISFIED — disposition set "
            f"amends no design entry outside record/unit scope (P27)")
    else:
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

    leavings = out_of_scope_undispositioned(entries)
    if leavings:
        for l in leavings:
            say(f"closure LEAVINGS HOLD: undispositioned out-of-scope "
                f"finding: {l['text']}")
        finish("CLOSURE_LEAVINGS_HOLD", 2, undispositioned=leavings, **late)

    if not args.unit:
        finish("CLOSURE_LIVE", 0,
               closing=f"{closing.id} at line {closing.lineno}", **late)

    # E-B (attack-8 N3, referent half): a mistyped id that still MATCHES
    # U<k> form (spelling half, closed above) fell through the rest of
    # this predicate untested and read UNIT_DISPATCHABLE — a hold on
    # the real unit cleared silently under the wrong id. An id the
    # record never scoped anywhere (known_units_of, the same known-unit
    # test waves_over_units computes for its own unplannable set) halts
    # instead.
    # P2: the record's declared write-set is the SINGLE write-set
    # source for the unit seam (statiker_git.py's gate consult reads
    # this field) — the same read `waves` uses over its own
    # write_sets, reused rather than reimplemented.
    write_sets, _, _, _ = waves_over_units(entries)
    declared_write_set = sorted(write_sets.get(args.unit, set()))

    if args.unit not in known_units_of(entries):
        finish("UNIT_UNKNOWN", 2, unit=args.unit,
              declared_write_set=declared_write_set, **late)

    hold_prefix = f"unit {args.unit} held: "
    held = [e for (u, e) in unit_lines
            if u == args.unit and e.tag == "AUTO-ACCEPTED"
            and e.body.startswith(hold_prefix) and latest[e.id] is e]
    if held:
        finish("UNIT_HELD", 2, unit=args.unit,
               holds=[f"{e.id} [{e.tag}] {e.body}" for e in held],
               declared_write_set=declared_write_set, **late)
    amendments = [
        {"line": f"{e.id} [{e.tag}] {e.body}", "lineno": e.lineno}
        for (u, e) in unit_lines
        if u == args.unit and e.tag != "INVALIDATED"
        and latest[e.id] is e]
    finish("UNIT_DISPATCHABLE", 0, unit=args.unit, amendments=amendments,
          declared_write_set=declared_write_set, **late)


# --------------------------------------------------------------------- waves

# The write-set record-line form is normative in SKILL.md (Implementation:
# `- F<n> [VERIFIED] unit U<k> write-set: <path> — basis: <the unit
# enumeration>`, one path per line, latest-line-per-id, appended at the
# [READY] enumeration); this regex reads that form's body after the
# parser splits off tag and basis. Paths are compared NORMALIZED
# (lexical normpath, leading `./` collapsed): two spellings of one path
# reading as disjoint would dispatch colliding units in parallel — the
# silent direction.
UNIT_WRITE_SET_RE = re.compile(r"^unit (U\d+) write-set: (\S.*)$")


def _strip_write_set_corrects_suffix(p):
    """The write-set declarator's own `(corrects line <n>)`
    resolving-token suffix, stripped — the split resolver's SHARED
    half (0.2.85 N2, checkpoint-review dispositions): both consumers
    of a raw write-set path (write_set_violations' near-miss check,
    UNNORMALIZED, and waves_over_units' alias recording) strip the
    suffix through this one helper, so a sanctioned supersede-whole
    repair's raw spelling reads the same underlying path as a plain
    declaration of it. normpath is deliberately NOT applied here —
    only at the consuming site that needs lexical comparison
    (_normalize_write_set_path, below, waves_over_units alone): RB1
    (0.2.84) routed the near-miss check through the normalizing form
    too, so a field carrying a real second path through an embedded
    `..` segment (`a.txt b/../c.txt`) collapsed to a single token
    before the near-miss check's own multi-word test ever ran,
    reading LINT_CLEAN / WAVES_COMPUTED instead of firing
    write-set-path-near-miss / WAVES_RECORD_MALFORMED (N2)."""
    return WRITE_SET_CORRECTS_SUFFIX_RE.sub("", p.strip())


def _normalize_write_set_path(p):
    # 0.2.85 RB1 (dev-notes/OBSERVATIONS.md, 0.2.84 re-review
    # dispositions): strip the corrects-suffix (the shared helper
    # above), then normalize — the CONSUMING site's own resolver,
    # built on the helper, so a sanctioned supersede-whole repair's
    # raw spelling collapses to the same comparison key as a plain
    # declaration of the same path. waves_over_units alone calls this
    # normalizing form, for lexical path comparison across spellings;
    # write_set_violations' near-miss check uses the shared helper
    # directly, unnormalized (N2, above) — the near-miss check must
    # see the field AS DECLARED, never collapsed through `..`.
    return os.path.normpath(_strip_write_set_corrects_suffix(p))


def known_units_of(entries):
    """Units KNOWN in the tracker: any live or dead entry opens
    `unit U<k> ` anywhere (classify_scope, the established scope-opener
    grammar) — write-set lines and any other unit-scoped line both
    count. The same known-unit test waves_over_units computes for its
    own unplannable set (write_sets.keys() vs this set), shared via
    this standalone helper (E-B, prior-lane implementation note:
    waves_over_units' own return tuple stays 4 values — a foreign
    lane's tools/test_statiker_git.py unpacks it)."""
    known = set()
    for e in latest_by_id(entries).values():
        scope, unit = classify_scope(e.body)
        if scope == "unit":
            known.add(unit)
    return known


def waves_over_units(entries):
    """(write_sets: unit -> live path set (normalized), unplannable
    units sorted ascending, waves: list of unit-id lists, each sorted
    ascending, ordered by each wave's lowest unit id, spellings:
    normalized path -> sorted raw spellings wherever any raw form
    differs — the as-named principle: the verdict reports the
    record's own strings beside the normalized comparison keys). A
    unit is KNOWN if any live
    or dead entry opens `unit U<k> ` anywhere (classify_scope, the
    established scope-opener grammar) — write-set lines and any other
    unit-scoped line both count. A unit is PLANNABLE only if at least
    one of its write-set lines is LIVE (latest-line-per-id, tag !=
    INVALIDATED) — the same supersede convention the lock-set F-line
    uses (SKILL.md:486-487; SENTENCE-C1 citation refresh, computed
    against the current file)."""
    latest = latest_by_id(entries)
    known_units = known_units_of(entries)
    write_sets = {}
    aliases = {}
    for e in sorted(latest.values(), key=lambda e: e.lineno):
        scope, unit = classify_scope(e.body)
        if scope != "unit":
            continue
        if e.tag == "INVALIDATED":
            continue
        m = UNIT_WRITE_SET_RE.match(e.body)
        if m:
            raw = m.group(2).strip()
            # 0.2.85 N1: the recorded alias is the suffix-STRIPPED
            # spelling (the shared helper, N2), not the raw one — a
            # sanctioned supersede-whole repair's raw spelling
            # (`a.txt (corrects line <n>)`) otherwise printed as a
            # distinct "spelling" of the same path it resolves to,
            # though nothing about it is an alternate spelling a desk
            # chose; stripped, it equals the normalized key and the
            # entry drops out of `spellings`.
            stripped = _strip_write_set_corrects_suffix(raw)
            norm = os.path.normpath(stripped)
            write_sets.setdefault(m.group(1), set()).add(norm)
            aliases.setdefault(norm, set()).add(stripped)
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
    spellings = {n: sorted(rs) for n, rs in aliases.items()
                 if rs != {n}}
    return write_sets, unplannable, waves, spellings


# P36 (BACKLOG.md:149, F98; widened R4/D39): "disjoint" is a
# write-set answer, never a scheduling verdict — U2's pin lived
# inside the tree U20 creates, and disjoint write-sets alone said
# nothing about that. The caveat names both axes a bare label hides:
# ORDERING (a unit's write-set inside another's created tree, a pin
# needing a prerequisite substrate) and EXECUTE-SET collisions
# (shared harness ports, a conftest one lane mutates while another
# executes it) — neither is write-set-derivable, both are the desk's,
# read from the D-lines.
WAVES_DISJOINT_CAVEAT = (
    " (disjoint write-sets only — ordering constraints (a unit's "
    "write-set inside another's created tree, a pin needing a "
    "prerequisite substrate) and execute-set collisions (shared "
    "harness ports, a conftest one lane mutates while another "
    "executes it) are the desk's, read from the D-lines)")


def cmd_waves(args):
    entries, violations, meta, reach = parse_tracker(load(args.tracker))
    say_head_region_entries("waves", reach)
    blocking = closure_blocking_violations(violations)
    if blocking:
        for v in blocking:
            say(f"waves blocked: {v['code']} @ line {v['line']}: {v['text']}")
        finish("WAVES_RECORD_MALFORMED", 2, violations=blocking, **meta)
    write_sets, unplannable, waves, spellings = waves_over_units(entries)
    for i, members in enumerate(waves, 1):
        overlap = len(members) > 1
        say(f"wave {i}: {{{', '.join(members)}}}"
            + (" (overlap — serialize within wave)" if overlap
               else WAVES_DISJOINT_CAVEAT))
    for u in unplannable:
        say(f"UNPLANNABLE: {u} — no live write-set declared")
    finish("WAVES_COMPUTED", 0,
          waves=[{"units": m, "serialize": len(m) > 1} for m in waves],
          unplannable=unplannable,
          write_sets={u: sorted(p) for u, p in write_sets.items()},
          spellings=spellings,
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
    per-id) landed at the PREVIOUS RE-LOCK — "attack repairs revise
    D-lines, so the repair set is those revised ids". Re-lock repairs
    answering round n-1 land AFTER its A-line and BEFORE round n's
    [DISPATCHED] line (the freeze defers mid-round desk appends to
    the round's return), so the repair window is that gap, never the
    prior round's own span. Only defined with >=2 rounds; the D-ids
    counted are exactly those whose latest-overall occurrence falls
    inside the window (a later revision, elsewhere, means that D-id
    was not what the re-lock repaired as it now stands).

    P26 (run-2 F82, live): "the newest round's findings" reads the
    citing F-line's CLASS via the existing scope-opener grammar
    (classify_scope) — a `record: `-scoped F-line is desk bookkeeping
    (a verification or confirmation the desk executed, citing the
    repair it confirmed), never a finding landing on the repaired
    ground, and is excluded; a scopeless or unit-scoped F-line is an
    ordinary attacker finding and still counts. Without the filter, a
    positive executed-verification entry citing the repair it
    executed reads identically to a finding landing on it — measured
    live at cycle 8 with four flat rounds on record."""
    latest = latest_by_id(entries)
    a_latest = sorted([e for e in latest.values() if e.cls == "A"],
                      key=lambda e: e.lineno)
    rounds_a = [e for e in a_latest if e.tag in ("BIT", "ZERO-DELTA")]
    # Each round's window opens at ITS OWN id's [DISPATCHED] line,
    # never at the previous round's resolution line (begehung-harvest
    # 2, finding 4): a VOID round's desk-re-derived F-lines land
    # between the void and the NEXT id's dispatch, so anchoring on
    # dispatch drops them from every round instead of annexing them
    # into whichever round follows (probe 1) — VOID needs no special
    # case; it is simply absent from rounds_a and opens no window of
    # its own. The same anchor gives round 1 its own start at the
    # first attack rather than line 0, so cycle-1's pre-attack
    # investigation F-lines never inflate it (probe 2).
    dispatch_line = {}
    for e in entries:
        if e.cls == "A" and e.tag == "DISPATCHED":
            dispatch_line.setdefault(e.id, e.lineno)   # first, not latest
    bounds = []
    prev_end = 0
    for e in rounds_a:
        bounds.append((dispatch_line.get(e.id, prev_end), e.lineno, e))
        prev_end = e.lineno
    f_entries = [e for e in entries if e.cls == "F"]
    counts = [sum(1 for f in f_entries if start < f.lineno <= end)
             for start, end, _ in bounds]
    trajectory = trend_verdict(counts)
    concentration, hits = False, []
    if len(bounds) >= 2:
        _, prev_end, _ = bounds[-2]
        cur_start, cur_end, cur_a = bounds[-1]
        dispatch_lines = [e.lineno for e in entries
                          if e.cls == "A" and e.id == cur_a.id
                          and e.tag == "DISPATCHED" and e.lineno <= cur_end]
        window_end = max(dispatch_lines) if dispatch_lines else cur_end
        d_entries = [e for e in entries if e.cls == "D"
                    and prev_end < e.lineno <= window_end]
        repair_ids = {e.id for e in d_entries if latest.get(e.id) is e}
        # P26 (run-2 F82, live): a `record: `-scoped F-line is desk
        # bookkeeping — a verification or confirmation of a repair the
        # desk itself executed — never a finding landing on it; the
        # existing scope-opener grammar (classify_scope) already
        # distinguishes it from an ordinary (scopeless or unit-scoped)
        # attacker finding, so concentration reads that class instead
        # of counting every citing F-line alike.
        cur_findings = [f for f in f_entries
                        if cur_start < f.lineno <= cur_end
                        and classify_scope(f.body)[0] != "record"]
        for f in cur_findings:
            hit = set(cited_ids(f.basis or "")) & repair_ids
            if hit:
                concentration = True
                hits.append({"finding": f.id, "repair_ids": sorted(hit)})
    return bounds, counts, trajectory, concentration, hits


def cmd_trend(args):
    entries, violations, meta, reach = parse_tracker(load(args.tracker))
    say_head_region_entries("trend", reach)
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
        + (", CONCENTRATION in the previous re-lock's repairs — counted "
           "(non-record-scoped) finding(s): "
           + ", ".join(h["finding"] for h in hits)
           if concentration else ""))
    finish("TREND_COMPUTED", 0, rounds=len(bounds), counts=counts,
          trajectory=trajectory, concentration=concentration,
          concentration_detail=hits, **meta)


# ------------------------------------------------------------------- sustain

def cmd_sustain(args):
    """P20 (BACKLOG; F143: A8's four record/instrument-class findings
    sustained a ninth round the 0.2.48 never-sustain clause says they
    cannot — prose under-binds at the re-entry seam, the same class
    as P16's turn-end seam). round-open's mechanical gate: the
    SUSTAINING SET is the LATEST RESOLVED round's own findings — a
    round whose A-line is [BIT] or [ZERO-DELTA] (the same
    round-boundary windowing `trend_over_rounds` computes, reused
    rather than reimplemented) — the verdict reads SUSTAIN_OK only if
    that set holds at least one DESIGN-SUBSTANCE finding, an F-line whose
    entry-class prefix (`classify_scope`, tool-side) is NOT
    `record:`; a record/instrument-class finding is desk work and
    never buys a round. Only meaningful over a [BIT] round — a
    ZERO-DELTA, VOID, still-DISPATCHED, or absent round answers
    SUSTAIN_NOT_APPLICABLE, the sustain question not being theirs to
    answer. A live [DISPATCHED] round is NEVER consulted — it is
    simply absent from the resolved windowing `trend_over_rounds`
    builds — so its id (when the latest A-line overall is one)
    surfaces separately as the verdict's own `live_round` field,
    keeping that state visible rather than silently skipped
    (checkpoint review R6)."""
    entries, violations, meta, reach = parse_tracker(load(args.tracker))
    say_head_region_entries("sustain", reach)
    blocking = closure_blocking_violations(violations)
    if blocking:
        for v in blocking:
            say(f"sustain blocked: {v['code']} @ line {v['line']}: {v['text']}")
        finish("SUSTAIN_RECORD_MALFORMED", 2, violations=blocking, **meta)
    latest = latest_by_id(entries)
    a_latest = sorted([e for e in latest.values() if e.cls == "A"],
                      key=lambda e: e.lineno)
    live_round = (a_latest[-1].id if a_latest
                 and a_latest[-1].tag == "DISPATCHED" else None)
    bounds, _, _, _, _ = trend_over_rounds(entries)
    if not bounds or bounds[-1][2].tag != "BIT":
        latest_resolved = (f"{bounds[-1][2].id} [{bounds[-1][2].tag}]"
                           if bounds else None)
        say(f"sustain: latest resolved round is {latest_resolved} — the "
            f"sustain question applies only over a [BIT] round")
        finish("SUSTAIN_NOT_APPLICABLE", 0, latest=latest_resolved,
               live_round=live_round, **meta)
    start, end, closing = bounds[-1]
    findings = [e for e in entries
               if e.cls == "F" and start < e.lineno <= end]
    substance = [e for e in findings if classify_scope(e.body)[0] != "record"]
    record_class = [e for e in findings if classify_scope(e.body)[0] == "record"]
    for e in record_class:
        say(f"sustain: record/instrument-class finding {e.id} @ line "
            f"{e.lineno} — desk work, never buys a round")
    if substance:
        say(f"sustain: {closing.id} [BIT] carries {len(substance)} "
            f"design-substance finding(s) — SUSTAIN_OK")
        finish("SUSTAIN_OK", 0, round=closing.id,
               substance=[e.id for e in substance],
               record_class=[e.id for e in record_class],
               live_round=live_round, **meta)
    say(f"sustain: {closing.id} [BIT] carries no design-substance "
        f"finding among its {len(record_class)} finding(s) — "
        f"SUSTAIN_DENIED")
    finish("SUSTAIN_DENIED", 2, round=closing.id,
           record_class=[e.id for e in record_class],
           live_round=live_round, **meta)


# ------------------------------------------------------------------ tripwire

def cmd_tripwire(args):
    """P19 (BACKLOG; P18 measurement — run 1 ran twelve cycles with NO
    budget and diverged to zero landed units, eight attack rounds all
    BIT, zero V-lines, zero landing annotations over 46 tracker
    commits): the ZERO-LANDED tripwire, one of the two progress-shaped
    stop signals the budget's hard cap demotes to (SKILL.md, The
    record — cap as unattended-runaway protection only, never the
    driving stop signal). Fires when the record shows NEITHER a
    landing annotation (`  unit U<k> landed: <sha>`, any unit, ever)
    NOR a V-line (any verify verdict, ever) despite at least
    `--threshold` RESOLVED attack rounds (BIT/ZERO-DELTA A-lines, the
    same count `trend` computes) — either one silences it. The
    threshold is NAMED by the caller at arming time (SKILL.md's Stop
    rule design: a breaker's discriminating evidence is pre-registered
    when armed, never composed at firing time): --threshold (always
    overriding) > the LATEST appended `record: tripwire armed at <n>`
    entry (st-35, dev-notes/OBSERVATIONS.md — the arming carrier moved
    off the header so an appended arm can repair a record seeded with
    a bad or absent header value) > the tracker's own header `Budget:`
    line's optional `/ tripwire <N>` field > unarmed, never a guessed
    default (checkpoint review R3). The verdict's `reason` field
    distinguishes unarmed/silent/fires."""
    # st-14 (5) (ITEMS.md, P31 remainder): --threshold below 1 is
    # meaningless (0 or negative rounds is not a resolved-round
    # count) and was never checked — only `is None` was, so a 0 or
    # negative --threshold rode through as an ordinary arm, firing
    # immediately on zero resolved rounds. An invocation mistake,
    # caught before the tracker is even read.
    if args.threshold is not None and args.threshold < 1:
        finish("USAGE_ERROR", 3,
               error=f"--threshold must be >= 1 ({args.threshold} given)")
    text = load(args.tracker)
    entries, violations, meta, reach = parse_tracker(text)
    say_head_region_entries("tripwire", reach)
    blocking = closure_blocking_violations(violations)
    if blocking:
        for v in blocking:
            say(f"tripwire blocked: {v['code']} @ line {v['line']}: "
                f"{v['text']}")
        finish("TRIPWIRE_RECORD_MALFORMED", 2, violations=blocking, **meta)
    threshold = args.threshold
    if threshold is None:
        # st-35: an appended arming entry outranks the header field —
        # the header must not be consulted once one exists (the whole
        # point of the appended route is repairing a record seeded
        # with a bad or absent header value).
        # st-35 follow-up (2026-09-12): an arming entry is an ORDINARY
        # entry, so the record's own supersession rule governs it —
        # resolve latest_by_id BEFORE filtering on the tag. Filtering
        # `[VERIFIED]` first keeps reading a RETRACTED arm: the
        # retraction line (same id, later, `[INVALIDATED]`) fails the
        # tag filter and the stale `[VERIFIED]` line survives as the
        # winner. Retraction IS the record's disarm form, and the
        # ruling reserves disarming to the operator while naming no
        # other one — honouring supersession closes that with no new
        # grammar, the same argument that put arming on an appended
        # entry.
        arm_entries = sorted(
            (e for e in latest_by_id(entries).values()
             if e.cls == "F" and e.tag == "VERIFIED"
             and TRIPWIRE_ARM_RE.match(e.body)),
            key=lambda e: e.lineno)
        if arm_entries:
            latest_arm = arm_entries[-1]
            raw = TRIPWIRE_ARM_RE.match(latest_arm.body).group(1)
            try:
                threshold = int(raw)
            except ValueError:
                finish("USAGE_ERROR", 3,
                       error=f"{latest_arm.id}'s tripwire-arming entry "
                             f"must name an integer >= 1 ({raw!r} given)")
            if threshold < 1:
                finish("USAGE_ERROR", 3,
                       error=f"{latest_arm.id}'s tripwire-arming entry "
                             f"must name >= 1 ({threshold} given)")
            say(f"tripwire: armed from {latest_arm.id}'s appended entry "
                f"(tripwire armed at {threshold})")
        else:
            m = TRIPWIRE_BUDGET_RE.search(meta["budget"] or "")
            if not m:
                say("tripwire: unarmed — no --threshold given, no "
                    "appended arming entry, and the Budget line "
                    "carries no `tripwire <n>` field")
                finish("TRIPWIRE_SILENT", 0, reason="unarmed", rounds=None,
                       threshold=None, landed=None, v_lines=None, **meta)
            raw = m.group(1)
            # st-34 (N2) (0.2.87 checkpoint review): a PRESENT field that
            # does not parse as an integer at all (`tripwire -1` no longer
            # misses TRIPWIRE_BUDGET_RE's match, now that it captures any
            # token) is refused the same way as a sub-1 value below —
            # never silently read as unarmed. An ABSENT field is the only
            # case that stays unarmed (the `not m` branch above).
            try:
                threshold = int(raw)
            except ValueError:
                finish("USAGE_ERROR", 3,
                       error="Budget line's `tripwire <n>` field must be "
                             f"an integer >= 1 ({raw!r} given)")
            # st-30(3) (0.2.86 re-review finding 3): the --threshold < 1
            # refusal above covered the flag alone — the header carrier
            # (Budget's `/ tripwire <n>` field) reached this point
            # unchecked, so `tripwire 0` armed on zero resolved rounds the
            # same way a bare --threshold 0 used to.
            if threshold < 1:
                finish("USAGE_ERROR", 3,
                       error="Budget line's `tripwire <n>` field must be "
                             f">= 1 ({threshold} given)")
            say(f"tripwire: armed from the Budget line's `tripwire "
                f"{threshold}` field")
    bounds, _, _, _, _ = trend_over_rounds(entries)
    rounds = len(bounds)
    # any landing mention counts, indented (the sanctioned form) or
    # not (a landing-indent lint defect is a form issue, never a
    # reason to miss a real landing here)
    landed = any(LANDING_RE.match(l) or LANDING_INDENTED_RE.match(l)
                for l in split_lines(text))
    v_lines = [e for e in entries if e.cls == "V"]
    if rounds < threshold:
        say(f"tripwire: {rounds} resolved round(s) < threshold "
            f"({threshold}) — not yet armed")
        finish("TRIPWIRE_SILENT", 0, reason="silent", rounds=rounds,
               threshold=threshold, landed=landed,
               v_lines=len(v_lines), **meta)
    if landed or v_lines:
        say(f"tripwire: silenced — landed={landed}, "
            f"v_lines={len(v_lines)}")
        finish("TRIPWIRE_SILENT", 0, reason="silent", rounds=rounds,
               threshold=threshold, landed=landed,
               v_lines=len(v_lines), **meta)
    say(f"tripwire: FIRES — {rounds} resolved round(s), zero landing "
        f"annotations, zero V-lines")
    finish("TRIPWIRE_FIRES", 2, reason="fires", rounds=rounds,
           threshold=threshold, landed=landed, v_lines=len(v_lines), **meta)


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
    # st-34 (n4) (0.2.87 checkpoint review): resolve --sha to a commit
    # ONCE, then read the TRACKER's content at THAT resolved sha — the
    # old order (`git show` at the raw --sha first, `rev-parse
    # --verify` second) let a commit land on the branch between the
    # two calls when --sha names a symbolic ref, pairing one commit's
    # content with a DIFFERENT commit's sha in the emitted verdict
    # (the reviewer's PATH-wrapper race: a `git` wrapper early on PATH
    # advancing the branch between the two resolutions). st-14 (1)
    # (ITEMS.md, P31 remainder): the emitted `sha` field is always this
    # resolved full form, never the raw --sha argument, which may be
    # abbreviated or otherwise non-canonical.
    verify = subprocess.run(
        ["git", "rev-parse", "--verify", f"{args.sha}^{{commit}}"],
        cwd=top, capture_output=True, text=True)
    if verify.returncode == 0:
        resolved_sha = verify.stdout.strip()
        # read the history of the TRACKER's repo at the RESOLVED sha
        # — `rel` is relative to `top`, so a cwd-resolved `git show`
        # asks the wrong repo (or none). Reading at the resolved sha,
        # never the raw --sha, is what keeps content and sha from the
        # same resolution.
        p = subprocess.run(["git", "show", f"{resolved_sha}:{rel}"],
                           cwd=top, capture_output=True)
        if p.returncode != 0:
            # st-30(4) (0.2.86 re-review finding 4): no `sha` field —
            # the page's override (SKILL.md, :114-117) routes any halt
            # carrying one as LANDED commits, and this resolved commit
            # never named a landed reference for THIS path (a path
            # absent at that commit — today's route for that case).
            finish("PIN_UNREADABLE", 2, tracker=args.tracker,
                   stderr=p.stderr.decode(errors="replace").strip())
    else:
        # rev-parse could not resolve a commit — run `git show` on the
        # RAW --sha to separate the two routes exactly as before:
        # unreadable at all (PIN_UNREADABLE, as today) from a readable
        # tree-ish that simply is not a commit (GIT_ERROR, as today).
        p = subprocess.run(["git", "show", f"{args.sha}:{rel}"], cwd=top,
                           capture_output=True)
        if p.returncode != 0:
            finish("PIN_UNREADABLE", 2, tracker=args.tracker,
                   stderr=p.stderr.decode(errors="replace").strip())
        # st-30(4): no `sha` field, same reason as PIN_UNREADABLE above
        # — args.sha resolved to SOME object (git show succeeded) but
        # not to a commit, so it still never names a landed commit.
        finish("GIT_ERROR", 2, tracker=args.tracker,
               error=f"--sha does not resolve to a commit in this "
                     f"repo: {verify.stderr.strip()}")
    # E-E(1) (begehung-harvest F11): "wrong sha pinned" is one of the
    # three premise breaks that VOID a whole round, and filter accepted
    # any readable sha with no staleness signal — the artifact of a
    # superseded design read exactly like the artifact of the current
    # one. A field, not a gate: the tracker's own newest commit beside
    # the given sha, so a mismatch is the desk's cue to check whether a
    # re-lock happened.
    newest = subprocess.run(["git", "log", "-1", "--format=%H", "--", rel],
                            cwd=top, capture_output=True, text=True)
    newest_commit = newest.stdout.strip() or None
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
    try:
        with open(args.out, "w", encoding="utf-8",
                  errors="surrogateescape") as f:
            f.write(text)
    except PermissionError as e:
        # E-E(3) (begehung-harvest A5): same class as its two siblings
        # just above (missing --out parent, --out naming a directory)
        # — an invocation mistake, not a tool defect. Unguarded this
        # fell through to the generic handler as INTERNAL_ERROR, which
        # SKILL.md's catch-all reads as a tool defect.
        finish("USAGE_ERROR", 3,
               error=f"--out is not writable: {args.out} ({e})")
    say(f"artifact written: {args.out}")
    finish("ARTIFACT_WRITTEN", 0, sha=resolved_sha, out=args.out,
           source_tracker=rel, newest_commit=newest_commit,
           lines_in=len(lines), lines_out=len(out),
           blocks_blanked=blocks, sections_blanked=sections,
           lines_blanked=blanked,
           form="the two Superseded species are BLANKED IN PLACE (each "
                "dropped line an empty line) and no header line is "
                "emitted, so artifact line numbers equal the pinned "
                "source's — quote these fields beside the artifact")


# -------------------------------------------------------------------- pinned

def _mutable_field_positions(lines):
    """The header's declared mutable surface (SKILL.md, The record:
    "The record's one mutable surface is the header's Status and
    Phase fields"): the FIRST Status: and FIRST Phase: line — the
    same first-match read parse_tracker itself uses. 0-based."""
    pos = {}
    for i, line in enumerate(lines):
        if "Status:" not in pos and line.startswith("Status:"):
            pos["Status:"] = i
        if "Phase:" not in pos and line.startswith("Phase:"):
            pos["Phase:"] = i
        if len(pos) == 2:
            break
    return pos


def cmd_pinned(args):
    """E-I (begehung-harvest triage T16, SENTENCE-B1): an IN-PLACE
    tag rewrite (`[PENDING]` edited to `[VERIFIED]` on its own
    line, never a new appended line) reads exactly like a clean
    record to every positional gate — SWEEP_CLEAN included — while
    `git diff --stat <pin>` shows the edit as 1+/1-. The append-only
    CLAIM is mechanically checkable once a pin exists: every pinned
    line binds byte-exact against the working tracker (ES-9 — a
    text-layer decode could paper over a divergence the raw file
    carries), EXCEPT the header's two declared-mutable field lines
    (first Status:/Phase:), where only the field's presence binds —
    a whole-file byte prefix fired on the very Status flip the spec
    mandates at each phase seam, and the header divergence MASKED a
    real entry rewrite further down (release review 2026-08-15,
    B1). The last pinned line binds as a byte PREFIX of its
    counterpart: an append legitimately extends a pin that lacked a
    trailing newline."""
    fs, rel, top, resolved = repo_paths(args.tracker)
    check_tracker_dir(args.tracker, fs)
    if os.path.islink(fs):
        # same reasoning as filter's own guard: a link's git history
        # is the link string, not the record it names
        finish("USAGE_ERROR", 3, tracker=args.tracker,
               error=f"--tracker names a symlink ({args.tracker}): name "
                     f"the real path — a link's git history is the link "
                     f"string, not the record")
    if rel is None:
        unpinnable_tracker(args.tracker, rel, top, resolved)
    # st-34 (n4) (0.2.87 checkpoint review): resolve --sha to a commit
    # ONCE, then read the pinned content at THAT resolved sha — the
    # old order (`git show` at the raw --sha first, `rev-parse
    # --verify` second, st-30(7)'s own shape copied from filter) let a
    # commit land on the branch between the two calls when --sha names
    # a symbolic ref, pairing one commit's content with a DIFFERENT
    # commit's sha in the emitted verdict (the reviewer's PATH-wrapper
    # race). The emitted `sha` field is always this resolved full form,
    # never the raw --sha argument (which may be abbreviated).
    verify = subprocess.run(
        ["git", "rev-parse", "--verify", f"{args.sha}^{{commit}}"],
        cwd=top, capture_output=True, text=True)
    if verify.returncode == 0:
        resolved_sha = verify.stdout.strip()
        p = subprocess.run(["git", "show", f"{resolved_sha}:{rel}"],
                           cwd=top, capture_output=True)
        if p.returncode != 0:
            # st-30(4): no `sha` field, same reason as filter's
            # PIN_UNREADABLE — this resolved commit never named a
            # landed reference for THIS path (a path absent at that
            # commit — today's route for that case).
            finish("PIN_UNREADABLE", 2, tracker=args.tracker,
                   stderr=p.stderr.decode(errors="replace").strip())
    else:
        # rev-parse could not resolve a commit — run `git show` on the
        # RAW --sha to separate the two routes exactly as before:
        # unreadable at all (PIN_UNREADABLE, as today) from a readable
        # tree-ish that simply is not a commit (GIT_ERROR, as today,
        # filter's own st-30(4) reasoning: it never named a landed
        # commit either).
        p = subprocess.run(["git", "show", f"{args.sha}:{rel}"], cwd=top,
                           capture_output=True)
        if p.returncode != 0:
            finish("PIN_UNREADABLE", 2, tracker=args.tracker,
                   stderr=p.stderr.decode(errors="replace").strip())
        finish("GIT_ERROR", 2, tracker=args.tracker,
               error=f"--sha does not resolve to a commit in this "
                     f"repo: {verify.stderr.strip()}")
    pinned_bytes = p.stdout
    try:
        with open(fs, "rb") as f:
            current_bytes = f.read()
    except OSError as e:
        finish("TRACKER_UNREADABLE", 2, error=str(e))
    pinned_lines = split_lines(pinned_bytes.decode("utf-8", "surrogateescape"))
    current_lines = split_lines(current_bytes.decode("utf-8", "surrogateescape"))
    exempt = _mutable_field_positions(pinned_lines)
    divergent_line, divergent_text = None, None
    for i, a in enumerate(pinned_lines):
        if i >= len(current_lines):
            divergent_line = i + 1
            divergent_text = "the current tracker is shorter than the pin"
            break
        b = current_lines[i]
        field = next((f for f, p in exempt.items() if p == i), None)
        if field is not None:
            # the declared-mutable position: the field must still sit
            # on its line; its VALUE is the one legitimate rewrite
            if not b.startswith(field):
                divergent_line = i + 1
                divergent_text = (f"pinned: {a!r} — current: {b!r} "
                                  f"(the {field} field left its line)")
                break
            continue
        if i == len(pinned_lines) - 1:
            if not b.startswith(a):
                divergent_line = i + 1
                divergent_text = f"pinned: {a!r} — current: {b!r}"
            break
        if a != b:
            divergent_line = i + 1
            divergent_text = f"pinned: {a!r} — current: {b!r}"
            break
    if divergent_line is None:
        finish("PINNED_APPEND_ONLY", 0, sha=resolved_sha, tracker=args.tracker,
               pinned_bytes=len(pinned_bytes),
               current_bytes=len(current_bytes))
    say(f"pinned: first divergent line @ {divergent_line}: {divergent_text}")
    # st-30(4): `sha` KEPT here (unlike the PIN_UNREADABLE/GIT_ERROR
    # halts above) — resolved_sha (st-30(7)) names a landed commit,
    # the case the page's override is for.
    finish("PINNED_REWRITTEN", 2, sha=resolved_sha, tracker=args.tracker,
           first_divergent_line=divergent_line, evidence=divergent_text)


# ---------------------------------------------------------------- verify-gate

def cmd_verify_gate(args):
    """P30 (BACKLOG; incident F124/F121, run-2 close): `pinned` catches
    a REWRITE of the tracker text; nothing caught the desk itself
    committing DURING an isolated verify leg — the unit transaction's
    collision check was replaced by the CONDITION "this desk is the
    only writer in this copy" (F121's deviation), and the desk then
    broke exactly that condition, undetected, while the leg read the
    same copy. This is the repo-HEAD sibling of `pinned`'s tracker-text
    check: the desk records the copy's HEAD sha at verify-leg
    read-start (SKILL.md, Verify) and this command compares it against
    HEAD at the leg's return — VERIFY_COPY_CLEAN when unmoved,
    VERIFY_COPY_STALE when not, naming every commit and every touched
    path landed in between so the desk's disposition (harmless vs.
    re-run) is a body-read of real evidence, never the leg's own
    claim. Computable; the disposition itself stays desk judgment."""
    fs, rel, top, resolved = repo_paths(args.tracker)
    check_tracker_dir(args.tracker, fs)
    if rel is None:
        unpinnable_tracker(args.tracker, rel, top, resolved)
    verify = subprocess.run(["git", "rev-parse", "--verify", f"{args.sha}^{{commit}}"],
                            cwd=top, capture_output=True, text=True)
    if verify.returncode != 0:
        # st-30(4): no `sha` field — args.sha never resolved to a
        # commit here, so it names no landed commit (same reason as
        # filter's and pinned's PIN_UNREADABLE/GIT_ERROR).
        finish("GIT_ERROR", 2, tracker=args.tracker,
               error=f"--sha does not resolve to a commit in this repo: "
                     f"{verify.stderr.strip()}")
    # R8 (checkpoint review): compare against the RESOLVED full sha
    # (verify.stdout), never the raw --sha argument — an abbreviated
    # sha never equals HEAD's full 40-char form, so the raw-argument
    # comparison misgraded every abbreviated-sha call STALE with no
    # evidence (an empty commit/touched-paths list, since the log/diff
    # range itself resolves fine on an abbreviated endpoint — only the
    # equality check was wrong).
    read_sha = verify.stdout.strip()
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=top,
                          capture_output=True, text=True)
    if head.returncode != 0:
        finish("GIT_ERROR", 2, tracker=args.tracker,
               error=f"HEAD unreadable: {head.stderr.strip()}")
    head_sha = head.stdout.strip()
    if head_sha == read_sha:
        say(f"verify-gate: clean — HEAD unmoved since read-start ({read_sha})")
        finish("VERIFY_COPY_CLEAN", 0, read_sha=read_sha, head_sha=head_sha)
    log = subprocess.run(
        ["git", "log", "--format=%H %s", f"{read_sha}..HEAD"],
        cwd=top, capture_output=True, text=True)
    commits = []
    if log.returncode == 0:
        for line in log.stdout.splitlines():
            if not line.strip():
                continue
            sha, _, subject = line.partition(" ")
            commits.append({"sha": sha, "subject": subject})
    diff = subprocess.run(
        ["git", "diff", "--name-only", f"{read_sha}..HEAD"],
        cwd=top, capture_output=True, text=True)
    touched = ([ln for ln in diff.stdout.splitlines() if ln.strip()]
               if diff.returncode == 0 else [])
    say(f"verify-gate: STALE-COPY — HEAD moved {read_sha} -> {head_sha}, "
        f"{len(commits)} commit(s) landed, touched paths: "
        + (", ".join(touched) if touched else "(none)"))
    finish("VERIFY_COPY_STALE", 2, read_sha=read_sha, head_sha=head_sha,
           commits=commits, touched_paths=touched)


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
    # split_lines, never str.splitlines() (the parser's rule, same
    # reason): a U+2028, U+000C or U+0085 in the report would become a
    # quoted line the report never held, and the character itself would
    # be dropped at the join — the quoted block has to be the report's
    # own text, byte for byte
    body = [("> " + l) if l else ">" for l in split_lines(defanged)]
    block = "\n".join([first] + body)
    emit(block)
    finish("QUOTE_BLOCK", 0, block=block, defanged=names,
           lines=len(split_lines(block)))


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
    for name in ("lint", "sweep", "waves", "trend", "sustain"):
        p = sub.add_parser(name)
        p.add_argument("--tracker", required=True)
    p = sub.add_parser("closure")
    p.add_argument("--tracker", required=True)
    p.add_argument("--unit")
    p = sub.add_parser("filter")
    p.add_argument("--tracker", required=True)
    p.add_argument("--sha", required=True)
    p.add_argument("--out", required=True)
    p = sub.add_parser("pinned")
    p.add_argument("--tracker", required=True)
    p.add_argument("--sha", required=True)
    p = sub.add_parser("verify-gate")
    p.add_argument("--tracker", required=True)
    p.add_argument("--sha", required=True)
    p = sub.add_parser("tripwire")
    p.add_argument("--tracker", required=True)
    p.add_argument("--threshold", type=int)
    p = sub.add_parser("quote")
    p.add_argument("--label", required=True)

    args = ap.parse_args()
    handlers = {"lint": cmd_lint, "sweep": cmd_sweep, "closure": cmd_closure,
                "waves": cmd_waves, "trend": cmd_trend, "sustain": cmd_sustain,
                "filter": cmd_filter, "pinned": cmd_pinned,
                "verify-gate": cmd_verify_gate, "tripwire": cmd_tripwire,
                "quote": cmd_quote}
    try:
        handlers[args.cmd](args)
    except SystemExit:
        raise
    except Exception as e:  # never a silent death
        finish("INTERNAL_ERROR", 3, error=f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

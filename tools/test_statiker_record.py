#!/usr/bin/env python3
"""Red-first test suite for statiker_record.py — the record-grammar
machinery (tracker lint, [READY] sweep gate, closure predicate,
attack-artifact filter, defanged quote production) precipitated from
SKILL.md prose.

Each planted defect mirrors a record/instrument finding from draft
attacks 1-6 (provenance: dev-notes/OBSERVATIONS.md). The stats-reader
contract (enums, anchored vs unanchored greps) is anchored on the
clippy-stats source read 2026-08-07 (0.12.4).

Run: python3 tools/test_statiker_record.py
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "plugin" / "skills" / "statiker" / "scripts" / "statiker_record.py"

VERDICT_PREFIX = "STATIKER-RECORD VERDICT: "

HEADER = """# Run: test
Status: in-progress
Phase: investigate-design
Skill: statiker 0.2.33

INTENT — do the thing.

## Cycle 1
"""

# P5: a header version at/after clause-unparsed's RULE_MINT_VERSION
# (0.2.43) — for fixtures that test the code's own detection/repair
# mechanics and must NOT be confounded by RETRO netting (a violation
# whose line predates its code's mint grades RETRO, never blocking).
HEADER_POST_CLAUSE_UNPARSED_MINT = HEADER.replace(
    "Skill: statiker 0.2.33", "Skill: statiker 0.2.43")


def tool(args, cwd=None, stdin_text=None):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args], cwd=cwd,
        input=stdin_text, capture_output=True, text=True, timeout=60)


def tool_bytes(args, cwd=None, stdin_bytes=None):
    """The same invocation with NO text decoding — the only way to read
    what the process actually put on the wire (ES-9: verdict and quote
    output emit at the byte level; a text-mode reader re-spells the
    byte before the assertion can see it)."""
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args], cwd=cwd,
        input=stdin_bytes, capture_output=True, timeout=60)


class RecordFixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        # the fixture dir is a git repo: the record tool halts on a
        # tracker outside the surrounding repo (attack-8 N1), and a
        # bare temp dir under the test-runner's repo cwd IS that shape
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=self.dir,
                       env={**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null"},
                       capture_output=True, check=True)

    def tearDown(self):
        self._tmp.cleanup()

    def write_tracker(self, body, header=HEADER):
        p = self.dir / "t.md"
        p.write_text(header + body)
        return p

    def verdict(self, p):
        # a line ends at "\n" and nowhere else — the record's own rule
        # (split_lines in the script). Verdict lines carry the input's
        # characters verbatim (ensure_ascii=False), so str.splitlines()
        # severs the JSON at a U+2028, U+000C or U+0085 the tool
        # correctly kept: a reader defines a line as the tool does
        lines = [l for l in p.stdout.split("\n") if l.startswith(VERDICT_PREFIX)]
        self.assertEqual(
            len(lines), 1,
            f"expected one verdict line, stdout:\n{p.stdout}\nstderr:\n{p.stderr}")
        return json.loads(lines[0][len(VERDICT_PREFIX):])

    def lint(self, body, header=HEADER):
        return self.verdict(tool(
            ["lint", "--tracker", str(self.write_tracker(body, header))],
            cwd=self.dir))

    def sweep(self, body, header=HEADER):
        return self.verdict(tool(
            ["sweep", "--tracker", str(self.write_tracker(body, header))],
            cwd=self.dir))

    def closure(self, body, unit=None, header=HEADER):
        args = ["closure", "--tracker", str(self.write_tracker(body, header))]
        if unit:
            args += ["--unit", unit]
        return self.verdict(tool(args, cwd=self.dir))

    def waves(self, body, header=HEADER):
        return self.verdict(tool(
            ["waves", "--tracker", str(self.write_tracker(body, header))],
            cwd=self.dir))

    def trend(self, body, header=HEADER):
        return self.verdict(tool(
            ["trend", "--tracker", str(self.write_tracker(body, header))],
            cwd=self.dir))

    def sustain(self, body, header=HEADER):
        return self.verdict(tool(
            ["sustain", "--tracker", str(self.write_tracker(body, header))],
            cwd=self.dir))

    def tripwire(self, body, threshold=None, header=HEADER):
        args = ["tripwire", "--tracker", str(self.write_tracker(body, header))]
        if threshold is not None:
            args += ["--threshold", str(threshold)]
        return self.verdict(tool(args, cwd=self.dir))

    def violation_codes(self, v):
        return {viol["code"] for viol in v.get("violations", [])}

    def lineno_of(self, body, needle, header=HEADER):
        """The 1-based file line carrying `needle` — the number the
        tool reports in a violation and the number a `corrects line
        <n>` repair token must name."""
        lines = (header + body).split("\n")
        return next(i for i, l in enumerate(lines, 1) if needle in l)


# ---------------------------------------------------------------------- lint

class TestLint(RecordFixture):
    def test_clean_tracker(self):
        v = self.lint(
            "- F1 [VERIFIED] a fact — basis: cmd output\n"
            "- D1 [COMMITTED] a decision — basis: F1\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN")

    def test_status_missing_or_out_of_enum(self):
        v = self.lint("- F1 [VERIFIED] x — basis: y\n",
                      header="# Run: t\nStatus: ready\nPhase: implement\n\n")
        self.assertEqual(v["verdict"], "LINT_VIOLATIONS")
        self.assertIn("status-enum", self.violation_codes(v))

    def test_ready_must_keep_brackets(self):
        # the stats reader admits only the bracketed form
        v = self.lint("- F1 [VERIFIED] x — basis: y\n",
                      header="# Run: t\nStatus: READY\nPhase: implement\n\n")
        self.assertIn("status-enum", self.violation_codes(v))

    def test_status_outside_admission_window(self):
        filler = "filler line\n" * 25
        v = self.lint("- F1 [VERIFIED] x — basis: y\n",
                      header="# Run: t\n" + filler +
                      "Status: in-progress\nPhase: verify\n\n")
        self.assertIn("admission-window", self.violation_codes(v))

    def test_phase_missing(self):
        v = self.lint("", header="# Run: t\nStatus: in-progress\n\n")
        self.assertIn("phase-enum", self.violation_codes(v))

    def test_invalid_tag_for_class(self):
        # [COMMITTED] is a D-tag; on an F-line it is out of enum
        v = self.lint("- F1 [COMMITTED] x — basis: y\n")
        self.assertIn("tag-enum", self.violation_codes(v))

    def test_annotated_tag_rejected(self):
        # tags are BARE enum values; annotations break literal greps
        v = self.lint("- F1 [VERIFIED, adopted] x — basis: y\n")
        self.assertIn("tag-enum", self.violation_codes(v))

    def test_malformed_entry_line(self):
        v = self.lint("- F1 (VERIFIED) x — basis: y\n")
        self.assertIn("entry-form", self.violation_codes(v))

    def test_bracketed_literal_in_entry_body(self):
        v = self.lint("- F1 [VERIFIED] the [PENDING] tag rides here — basis: y\n")
        self.assertIn("tag-literal-in-body", self.violation_codes(v))

    def test_bracketed_literal_in_prose_defang_miss(self):
        # unanchored stats greps count [AUTO-ACCEPTED] anywhere
        v = self.lint("> Superseded — A3 quotes\n"
                      "> the report said [AUTO-ACCEPTED] verbatim\n")
        self.assertIn("tag-literal-in-body", self.violation_codes(v))

    def test_superseded_block_bare_gt_blank(self):
        # a blank line inside the block must be a BARE '>'
        v = self.lint("> Superseded — A3 quotes\n"
                      "> first para\n"
                      "\n"
                      "> second para\n")
        self.assertIn("superseded-block-form", self.violation_codes(v))

    def test_missing_basis(self):
        v = self.lint("- F1 [VERIFIED] a fact with no basis slot\n")
        self.assertIn("basis-missing", self.violation_codes(v))

    def test_unindented_landing_annotation(self):
        v = self.lint("unit U1 landed: abc1234\n")
        self.assertIn("landing-indent", self.violation_codes(v))

    def test_indented_landing_annotation_clean(self):
        v = self.lint("- D1 [COMMITTED] x — basis: y\n"
                      "\n"
                      "  unit U1 landed: abc1234\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN")


# --------------------------------------------------------------------- sweep

class TestSweep(RecordFixture):
    def test_clean_sweep(self):
        v = self.sweep("- F1 [VERIFIED] x — basis: y\n"
                       "- D1 [COMMITTED] d — basis: F1\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")

    def test_latest_pending_holds(self):
        v = self.sweep("- F1 [PENDING] awaiting leg — basis: dispatched\n")
        self.assertEqual(v["verdict"], "SWEEP_HOLDS")
        self.assertIn("pending-latest", self.violation_codes(v))

    def test_pending_resolved_by_later_line_clean(self):
        v = self.sweep("- F1 [PENDING] awaiting leg — basis: dispatched\n"
                       "- F1 [VERIFIED] leg returned clean — basis: report\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")

    def test_killerless_dead_disposition_holds(self):
        # a dead disposition without its named killer holds the record
        v = self.sweep("- F2 [INVALIDATED] clause 2 dead — basis: F9\n")
        self.assertIn("killerless-dead", self.violation_codes(v))

    def test_prose_dead_without_clause_context_not_flagged(self):
        # attack-9: `\bdead\b` fired on ordinary prose, so an
        # invalidation whose body merely MENTIONS dead code held the
        # record from [READY]. The rule is clause-scoped (SKILL.md,
        # Stop rule: "a dead clause without its named killer").
        v = self.sweep("- F2 [INVALIDATED] the dead-letter queue design "
                       "never shipped — basis: F9\n"
                       "- F3 [INVALIDATED] the helper is dead code — "
                       "basis: F9\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")

    def test_clause_scoped_dead_without_killer_still_holds(self):
        # the control the repair must not eat
        v = self.sweep("- F2 [INVALIDATED] clause a dead — basis: F2\n")
        self.assertEqual(v["verdict"], "SWEEP_HOLDS")
        self.assertIn("killerless-dead", self.violation_codes(v))

    def test_clause_scoped_dead_with_killer_stays_clean(self):
        v = self.sweep("- F2 [INVALIDATED] clause a dead (superseded by "
                       "D4) — basis: F2\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")

    def test_dead_with_killer_clean(self):
        v = self.sweep("- F2 [INVALIDATED] clause 2 dead (path removed) — basis: F9\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")

    def test_basis_citing_invalidated_entry_holds(self):
        v = self.sweep("- F1 [VERIFIED] ground — basis: probe\n"
                       "- F1 [INVALIDATED] premise died — basis: F3\n"
                       "- F3 [VERIFIED] the killer — basis: probe\n"
                       "- D1 [COMMITTED] rests on dead ground — basis: F1\n")
        self.assertIn("basis-cites-invalidated", self.violation_codes(v))

    def test_clause_aggregation_union_latest_per_clause(self):
        # dispositions aggregate: union, latest line per CLAUSE
        v = self.sweep(
            "- F5 [VERIFIED] two-clause entry — basis: probe\n"
            "- F5 [INVALIDATED] clause 1 dead (killed by X); clause 2 "
            "restated-at-F8 — basis: F6\n"
            "- F5 [INVALIDATED] clause 2 dead (restatement failed) — basis: F8\n"
            "- F8 [INVALIDATED] restatement died (check failed) — basis: check\n")
        agg = v["clause_dispositions"]["F5"]
        self.assertIn("dead", agg["1"])
        self.assertIn("dead", agg["2"])  # latest line for clause 2 wins


class TestSweepExemption(RecordFixture):
    """P6 + release-review round 2 (H4/M1, 2026-08-16): a declared
    SWEEP_EXEMPT nets FORM-DEBT holds out of the blocking set. The
    declaration carries its operator-authorization citation as a
    MANDATORY grammar slot (M1), and the live-work class
    (pending-latest) and defang class (tag-literal-in-body) are never
    netted (H4/H6) — exemptible holds are form debt only."""

    CITE = " — basis: operator line quoted in D95"

    def test_cited_exemption_nets_form_debt(self):
        body = ("- F1 [VERIFIED] claim without ground\n"
                "- F2 [VERIFIED] second claim without ground\n")
        ceiling = self.lineno_of(body, "- F2 [VERIFIED]")
        baseline = self.sweep(body)
        self.assertEqual(baseline["verdict"], "SWEEP_HOLDS")
        self.assertIn("basis-missing", self.violation_codes(baseline))
        v = self.sweep(
            body + f"SWEEP_EXEMPT: basis-missing lines<={ceiling}{self.CITE}\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN", v)
        self.assertEqual({h["code"] for h in v["exempt_holds"]},
                         {"basis-missing"})
        self.assertEqual(len(v["exempt_holds"]), 2)

    def test_citation_less_declaration_nets_nothing(self):
        # M1: the basis tail is a grammar slot, not decoration — an
        # exemption is operator authority, so citing nothing nets
        # nothing (fail-safe: the hold stays blocking)
        body = "- F1 [VERIFIED] claim without ground\n"
        v = self.sweep(body + "SWEEP_EXEMPT: basis-missing lines<=99\n")
        self.assertEqual(v["verdict"], "SWEEP_HOLDS", v)
        self.assertEqual(v["exempt_holds"], [])

    def test_live_work_class_is_never_exemptible(self):
        # H4: pending-latest guards [READY], the closing [ZERO-DELTA],
        # and the Verify dispatch — a CITED declaration is still inert
        body = "- F1 [PENDING] awaiting leg — basis: dispatched\n"
        v = self.sweep(
            body + f"SWEEP_EXEMPT: pending-latest lines<=99{self.CITE}\n")
        self.assertEqual(v["verdict"], "SWEEP_HOLDS", v)
        self.assertIn("pending-latest", self.violation_codes(v))
        self.assertEqual(v["exempt_holds"], [])

    def test_defang_class_is_never_exemptible(self):
        # H6 (round 1): an undefanged tag literal holds every later
        # sweep for the run's life — a cited declaration is inert
        body = ("- F1 [VERIFIED] the guard prints [PENDING] on a miss "
                "— basis: executed\n")
        baseline = self.sweep(body)
        self.assertEqual(baseline["verdict"], "SWEEP_HOLDS")
        self.assertIn("tag-literal-in-body", self.violation_codes(baseline))
        exempted = self.sweep(
            body
            + f"SWEEP_EXEMPT: tag-literal-in-body lines<=999{self.CITE}\n")
        self.assertEqual(exempted["verdict"], "SWEEP_HOLDS", exempted)
        self.assertIn("tag-literal-in-body", self.violation_codes(exempted))
        self.assertEqual(
            [h for h in exempted["exempt_holds"]
             if h["code"] == "tag-literal-in-body"], [])

    def test_undeclared_code_leaves_verdict_unchanged(self):
        body = "- F1 [VERIFIED] claim without ground\n"
        baseline = self.sweep(body)
        v = self.sweep(
            body + f"SWEEP_EXEMPT: killerless-dead lines<=99{self.CITE}\n")
        self.assertEqual(baseline["verdict"], "SWEEP_HOLDS")
        self.assertEqual(v["verdict"], "SWEEP_HOLDS", v)
        self.assertIn("basis-missing", self.violation_codes(v))
        self.assertEqual(v["exempt_holds"], [])

    def test_violation_above_ceiling_blocks_in_both_arrangements(self):
        # the ceiling is frozen at declaration: a violation on a line
        # the exemption does not cover blocks whether or not an
        # UNRELATED-in-reach exemption for the same code is present
        body = ("- F1 [VERIFIED] low line, will be exempt\n"
                "- F2 [VERIFIED] high line, stays blocking\n")
        low_line = self.lineno_of(body, "- F1 [VERIFIED]")
        high_line = self.lineno_of(body, "- F2 [VERIFIED]")
        baseline = self.sweep(body)
        exempted = self.sweep(
            body
            + f"SWEEP_EXEMPT: basis-missing lines<={low_line}{self.CITE}\n")
        self.assertEqual(baseline["verdict"], "SWEEP_HOLDS")
        self.assertIn("basis-missing", self.violation_codes(baseline))
        self.assertEqual(exempted["verdict"], "SWEEP_HOLDS", exempted)
        self.assertIn(high_line,
                      {v["line"] for v in exempted["violations"]})
        self.assertEqual({h["line"] for h in exempted["exempt_holds"]},
                         {low_line})

    def test_coverage_clamps_at_the_declaring_line(self):
        # M5 (release review round 3): `lines<=99999` must not become
        # a STANDING exemption — content appended after the
        # declaration blocks untouched, whatever the ceiling says
        body = "- F1 [VERIFIED] old claim without ground\n"
        decl = f"SWEEP_EXEMPT: basis-missing lines<=99999{self.CITE}\n"
        after = "- F2 [VERIFIED] new claim without ground\n"
        full = body + decl + after
        f2_line = self.lineno_of(full, "- F2 [VERIFIED]")
        v = self.sweep(full)
        self.assertEqual(v["verdict"], "SWEEP_HOLDS", v)
        self.assertIn(f2_line, {x["line"] for x in v["violations"]})
        self.assertEqual({h["code"] for h in v["exempt_holds"]},
                         {"basis-missing"})
        self.assertEqual(len(v["exempt_holds"]), 1)

    def test_single_line_exemption_form(self):
        body = "- F1 [VERIFIED] claim without ground\n"
        f1_line = self.lineno_of(body, "- F1 [VERIFIED]")
        v = self.sweep(
            body
            + f"SWEEP_EXEMPT: basis-missing line {f1_line}{self.CITE}\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN", v)
        self.assertEqual({h["line"] for h in v["exempt_holds"]}, {f1_line})

    def test_sweep_exempt_line_parses_no_entry(self):
        # the label line, like INTENT:/SKILL:, must never itself read
        # as an entry-shaped near-miss
        v = self.sweep(f"SWEEP_EXEMPT: basis-missing lines<=5{self.CITE}\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN", v)
        self.assertEqual(v["exempt_holds"], [])
        self.assertNotIn("entry-near-miss", self.violation_codes(v))


# --------------------------------------------------------- P5 (epoch sweep)

HEADER_PRE_ALL_FORM_MINTS = HEADER.replace(
    "Skill: statiker 0.2.33", "Skill: statiker 0.2.10")


class TestP5EpochScopedSweep(RecordFixture):
    """BACKLOG P5 (re-opened): a FORM-code hold whose line predates
    its own code's mint (RULE_MINT_VERSION, backfilled from this
    repo's git history) grades RETRO — surfaced, never blocking; the
    same code above the mint's marker still blocks. SUBSTANCE codes
    (everything outside FORM_CODES_MINT_GATED) grade every line
    whatever its age — the over-forgiveness control. A marker-less
    record (no `Skill:` header line at all) gets no forgiveness."""

    def _two_epoch_body(self):
        return (
            "- F3 [PENDING] an old-epoch pending finding — "
            "basis: dispatched\n"
            "- F1 [VERIFIED] an old-epoch fact with no basis slot\n"
            "SKILL: statiker 0.2.50\n"
            "- F2 [VERIFIED] a new-epoch fact with no basis slot\n")

    def test_form_hold_below_the_marker_grades_retro(self):
        body = self._two_epoch_body()
        f1_line = self.lineno_of(body, "F1 [VERIFIED]",
                                 header=HEADER_PRE_ALL_FORM_MINTS)
        v = self.sweep(body, header=HEADER_PRE_ALL_FORM_MINTS)
        self.assertTrue(any(r["code"] == "basis-missing"
                            and r["line"] == f1_line
                            for r in v["retro_holds"]), v)
        self.assertFalse(any(x["code"] == "basis-missing"
                             and x["line"] == f1_line
                             for x in v["violations"]))

    def test_form_hold_above_the_marker_still_blocks(self):
        body = self._two_epoch_body()
        f2_line = self.lineno_of(body, "F2 [VERIFIED]",
                                 header=HEADER_PRE_ALL_FORM_MINTS)
        v = self.sweep(body, header=HEADER_PRE_ALL_FORM_MINTS)
        self.assertTrue(any(x["code"] == "basis-missing"
                            and x["line"] == f2_line
                            for x in v["violations"]), v)
        self.assertFalse(any(r["line"] == f2_line for r in v["retro_holds"]))
        self.assertEqual(v["verdict"], "SWEEP_HOLDS")

    def test_substance_hold_below_the_marker_still_blocks(self):
        # the over-forgiveness case: pending-latest is NOT a form code
        v = self.sweep(self._two_epoch_body(),
                       header=HEADER_PRE_ALL_FORM_MINTS)
        self.assertIn("pending-latest", self.violation_codes(v))
        self.assertFalse(any(r["code"] == "pending-latest"
                             for r in v["retro_holds"]))

    def test_marker_less_record_gets_no_forgiveness(self):
        header = ("# Run: t\nStatus: in-progress\nPhase: implement\n\n"
                  "## Cycle 1\n")
        v = self.sweep("- F1 [VERIFIED] a fact with no basis slot\n",
                       header=header)
        self.assertIn("basis-missing", self.violation_codes(v))
        self.assertEqual(v["retro_holds"], [])

    def test_exact_mint_version_line_still_blocks(self):
        # not-less-than is the boundary: a line under the code's own
        # mint version (never older) is never retro
        v = self.sweep("- F1 [VERIFIED] claim without ground\n")
        self.assertIn("basis-missing", self.violation_codes(v))
        self.assertEqual(v["retro_holds"], [])


# ------------------------------------------------------------------- closure

CLOSED = (
    "- D1 [COMMITTED] the design — basis: probe\n"
    "- A1 [DISPATCHED] round 1 — basis: brief\n"
    "- A1 [ZERO-DELTA] clean return — basis: report\n"
)


class TestClosure(RecordFixture):
    def test_live_closure(self):
        v = self.closure(CLOSED)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")

    def test_no_zero_delta_is_absent(self):
        # P27: a [BIT] round alone is ABSENT only while its
        # disposition set still amends the design — a D-line change
        # follows here, keeping the design genuinely open
        v = self.closure("- A1 [DISPATCHED] round 1 — basis: brief\n"
                         "- A1 [BIT] two findings — basis: report\n"
                         "- D1 [INVALIDATED] the design changes — "
                         "basis: F1\n")
        self.assertEqual(v["verdict"], "CLOSURE_ABSENT")

    def test_scopeless_post_closure_line_voids(self):
        v = self.closure(CLOSED +
                         "- F9 [INVALIDATED] the premise died — basis: probe\n")
        self.assertEqual(v["verdict"], "CLOSURE_VOID")
        self.assertIn("F9", v["scopeless"][0]["line"])

    def test_record_scoped_line_keeps_closure(self):
        v = self.closure(CLOSED +
                         "- F9 [VERIFIED] record: collision on t.md — basis: verdict\n")
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")

    def test_unit_scoped_line_reopens_only_that_unit(self):
        # E-B: UNIT_DISPATCHABLE now requires U1 to be a KNOWN unit —
        # a harmless dead line establishes it, [INVALIDATED] so it
        # never counts as an amendment of its own
        body = (CLOSED +
                "- R2 [AMENDED] unit U2 new letter — basis: gap report\n"
                "- D0 [INVALIDATED] unit U1 established (never "
                "dispatched) — basis: design\n")
        v2 = self.closure(body, unit="U2")
        self.assertEqual(v2["verdict"], "UNIT_DISPATCHABLE")
        self.assertTrue(any("R2" in a["line"] for a in v2["amendments"]))
        v1 = self.closure(body, unit="U1")
        self.assertEqual(v1["verdict"], "UNIT_DISPATCHABLE")
        self.assertEqual(v1["amendments"], [])

    def test_invalidated_amendment_travels_as_nothing(self):
        # live lines only: an id whose latest line is [INVALIDATED]
        body = (CLOSED +
                "- R2 [AMENDED] unit U2 new letter — basis: gap report\n"
                "- R2 [INVALIDATED] unit U2 superseded (check failed) — basis: F9\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")
        self.assertEqual(v["amendments"], [])

    def test_held_unit_not_dispatchable(self):
        body = (CLOSED +
                "- F9 [VERIFIED] record: collision UNIT_COLLISION on x.txt — basis: verdict\n"
                "- D9 [AUTO-ACCEPTED] unit U2 held: x.txt — basis: F9\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "UNIT_HELD")

    def test_resolved_hold_dispatchable_again(self):
        body = (CLOSED +
                "- F9 [VERIFIED] record: collision on x.txt — basis: verdict\n"
                "- D9 [AUTO-ACCEPTED] unit U2 held: x.txt — basis: F9\n"
                "- D9 [COMMITTED] unit U2 operator cleared x.txt — basis: reply\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")

    def test_declared_write_set_rides_unit_dispatchable(self):
        # P2: the record's own declared write-set is the single source
        # the git tool's gate consult reads — the SAME read `waves`
        # computes over its own write_sets, reused not reimplemented.
        body = (CLOSED +
                "- F2 [VERIFIED] unit U2 write-set: a.txt — basis: design\n"
                "- F3 [VERIFIED] unit U2 write-set: b.txt — basis: design\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")
        self.assertEqual(sorted(v["declared_write_set"]), ["a.txt", "b.txt"])

    def test_declared_write_set_empty_when_undeclared(self):
        # a KNOWN unit (scoped via the hold line) with no live
        # write-set F-line at all — the empty declaration itself is
        # what statiker_git.py's gate consult reads as "undeclared
        # unit cannot start"
        v = self.closure(CLOSED, unit="U1")
        self.assertEqual(v["verdict"], "UNIT_UNKNOWN")
        self.assertEqual(v["declared_write_set"], [])

    def test_declared_write_set_rides_unit_held(self):
        body = (CLOSED +
                "- F9 [VERIFIED] record: collision UNIT_COLLISION on x.txt — basis: verdict\n"
                "- F2 [VERIFIED] unit U2 write-set: x.txt — basis: design\n"
                "- D9 [AUTO-ACCEPTED] unit U2 held: x.txt — basis: F9\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "UNIT_HELD")
        self.assertEqual(v["declared_write_set"], ["x.txt"])


class TestP25LeavingsGate(RecordFixture):
    """BACKLOG P25 (run-2 F77): an out-of-scope-graded finding blocks
    closure until dispositioned — a decision-graded export ref or a
    one-line recorded drop, either clears it; undispositioned it
    holds (CLOSURE_LEAVINGS_HOLD), never voids (the scopeless-VOID
    rule's exemption for the grade)."""

    def test_undispositioned_out_of_scope_finding_holds_closure(self):
        body = (CLOSED +
                "- F9 [VERIFIED] out-of-scope: spread CLV has never "
                "computed — basis: probe\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LEAVINGS_HOLD", v)
        self.assertEqual(len(v["undispositioned"]), 1)
        self.assertEqual(v["undispositioned"][0]["id"], "F9")

    def test_export_ref_clears_the_hold(self):
        body = (CLOSED +
                "- F9 [VERIFIED] out-of-scope: spread CLV has never "
                "computed — basis: probe\n"
                "- F9 [VERIFIED] out-of-scope: spread CLV has never "
                "computed — exported: target-repo BACKLOG.md#spread-clv "
                "— basis: probe\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE", v)

    def test_recorded_drop_clears_the_hold(self):
        body = (CLOSED +
                "- F9 [VERIFIED] out-of-scope: spread CLV has never "
                "computed — basis: probe\n"
                "- F9 [VERIFIED] record: out-of-scope F9 — dropped: not "
                "actionable this cycle — basis: operator\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE", v)

    def test_out_of_scope_line_post_closure_does_not_void(self):
        # exempt from the ordinary scopeless-VOID rule
        body = (CLOSED +
                "- F9 [VERIFIED] out-of-scope: found in passing — "
                "exported: target-repo BACKLOG.md#x — basis: probe\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE", v)

    def test_unit_query_also_holds_on_undispositioned_leavings(self):
        body = (CLOSED +
                "- F9 [VERIFIED] out-of-scope: found in passing — "
                "basis: probe\n"
                "- F2 [VERIFIED] unit U1 write-set: a.txt — basis: design\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_LEAVINGS_HOLD", v)

    def test_no_out_of_scope_grade_is_unaffected(self):
        v = self.closure(CLOSED)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE", v)

    def test_natural_scopeless_disposition_spelling_voids_the_closure(self):
        # R2 (checkpoint review): the trap SKILL.md's Close/leavings
        # passage now warns about — a disposition line that drops the
        # out-of-scope: opener (the natural phrasing) reads scopeless
        # and voids the WHOLE closure, never just re-holding the
        # leavings gate. Presence-of-warning + behavior pin: no code
        # change, this is existing (already correct) behavior.
        body = (CLOSED +
                "- F9 [VERIFIED] out-of-scope: spread CLV has never "
                "computed — basis: probe\n"
                "- F9 [VERIFIED] exported to target-repo "
                "BACKLOG.md#spread-clv — basis: probe\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_VOID", v)


class TestP27DesignConsequenceClosure(RecordFixture):
    """BACKLOG P27 (run-2 A6, F118): round sustain reads design
    CONSEQUENCE, not finding PRESENCE — a terminal [BIT] round whose
    disposition set amends no design entry (no D-class line follows
    it) grades the closure SATISFIED, same predicate as ZERO-DELTA
    from there; one design-amending disposition keeps it SHUT."""

    def test_bit_round_with_no_design_amending_disposition_satisfies(self):
        body = (
            "- D1 [COMMITTED] the design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] a family account corrected — basis: report\n"
            "- F2 [INVALIDATED] an exclusion rationale repaired — "
            "basis: report\n"
            "- A1 [BIT] two findings, none design-amending — "
            "basis: report\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE", v)

    def test_bit_round_with_design_amending_disposition_stays_shut(self):
        # the over-correction case
        body = (
            "- D1 [COMMITTED] the design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] a real design defect — basis: report\n"
            "- A1 [BIT] one finding — basis: report\n"
            "- D1 [INVALIDATED] the design must change — basis: F1\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_ABSENT", v)
        self.assertEqual(v["design_amending"], ["D1"])

    def test_bit_round_still_in_flight_stays_absent(self):
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] a finding — basis: probe\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_ABSENT", v)

    def test_zero_delta_round_unaffected(self):
        v = self.closure(CLOSED)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE", v)

    def test_bit_round_dispatchable_for_unit_query_too(self):
        body = (
            "- D1 [COMMITTED] the design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] a family account corrected — basis: report\n"
            "- A1 [BIT] one finding, not design-amending — basis: report\n"
            "- F2 [VERIFIED] unit U1 write-set: a.txt — basis: design\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE", v)

    # ------------------------------------------------- R1 (checkpoint
    # review, P20xP27 deadlock): design_amending reads the D-line's
    # SCOPE, not mere presence.

    def test_bit_round_record_scoped_disposition_satisfies(self):
        # (a) a record:-opened D-line is bookkeeping — never bars
        # closure (red today: CLOSURE_ABSENT)
        body = (
            "- D1 [COMMITTED] the design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] record: a bookkeeping finding — "
            "basis: report\n"
            "- A1 [BIT] one finding — basis: report\n"
            "- D2 [AUTO-ACCEPTED] record: disposition note — basis: F1\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE", v)

    def test_bit_round_scopeless_disposition_still_bars(self):
        # (b) the over-correction guard: a SCOPELESS D-line still
        # keeps closure shut (unaffected by the scope fix)
        body = (
            "- D1 [COMMITTED] the design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] record: a bookkeeping finding — "
            "basis: report\n"
            "- A1 [BIT] one finding — basis: report\n"
            "- D2 [INVALIDATED] the design must change — basis: F1\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_ABSENT", v)
        self.assertEqual(v["design_amending"], ["D2"])

    def test_bit_round_unit_held_disposition_yields_unit_held_only(self):
        # (c) `unit U1 held:` yields UNIT_HELD for U1 only, siblings
        # dispatchable (red today: all barred — CLOSURE_ABSENT)
        body = (
            "- D1 [COMMITTED] the design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] record: a bookkeeping finding — "
            "basis: report\n"
            "- A1 [BIT] one finding — basis: report\n"
            "- D2 [AUTO-ACCEPTED] unit U1 held: pending operator call "
            "— basis: F1\n"
            "- F2 [VERIFIED] unit U1 write-set: a.txt — basis: design\n"
            "- F3 [VERIFIED] unit U2 write-set: b.txt — basis: design\n")
        v_whole = self.closure(body)
        self.assertEqual(v_whole["verdict"], "CLOSURE_LIVE", v_whole)
        v_u1 = self.closure(body, unit="U1")
        self.assertEqual(v_u1["verdict"], "UNIT_HELD", v_u1)
        v_u2 = self.closure(body, unit="U2")
        self.assertEqual(v_u2["verdict"], "UNIT_DISPATCHABLE", v_u2)


# --------------------------------------------------------------------- waves

class TestWaves(RecordFixture):
    def test_three_units_two_disjoint_one_overlapping(self):
        # U1 and U3 share src/a.py (overlap, serialize); U2 is disjoint
        body = (
            "- F1 [VERIFIED] unit U1 write-set: src/a.py — basis: design\n"
            "- F2 [VERIFIED] unit U1 write-set: src/b.py — basis: design\n"
            "- F3 [VERIFIED] unit U2 write-set: src/c.py — basis: design\n"
            "- F4 [VERIFIED] unit U3 write-set: src/a.py — basis: design\n")
        v = self.waves(body)
        self.assertEqual(v["verdict"], "WAVES_COMPUTED")
        by_units = [w["units"] for w in v["waves"]]
        self.assertEqual(by_units, [["U1", "U3"], ["U2"]])
        overlap = next(w for w in v["waves"] if w["units"] == ["U1", "U3"])
        self.assertTrue(overlap["serialize"])
        parallel = next(w for w in v["waves"] if w["units"] == ["U2"])
        self.assertFalse(parallel["serialize"])
        self.assertEqual(v["unplannable"], [])

    def test_unit_missing_write_set_is_unplannable(self):
        body = (
            "- F1 [VERIFIED] unit U1 write-set: src/a.py — basis: design\n"
            "- D2 [AUTO-ACCEPTED] unit U2 gap: no write-set decided — basis: report\n")
        v = self.waves(body)
        self.assertEqual(v["verdict"], "WAVES_COMPUTED")
        self.assertEqual(v["unplannable"], ["U2"])
        self.assertEqual(v["waves"], [{"units": ["U1"], "serialize": False}])

    def test_invalidated_write_set_path_dropped_leaves_unit_unplannable(self):
        body = (
            "- F1 [VERIFIED] unit U1 write-set: src/a.py — basis: design\n"
            "- F2 [VERIFIED] unit U2 write-set: src/a.py — basis: design\n"
            "- F2 [INVALIDATED] unit U2 write-set: src/a.py dead (mis-scoped) "
            "— basis: F9\n")
        v = self.waves(body)
        self.assertEqual(v["verdict"], "WAVES_COMPUTED")
        # F2's LATEST line is INVALIDATED: U2 contributes no live path
        self.assertEqual(v["unplannable"], ["U2"])
        self.assertEqual(v["waves"], [{"units": ["U1"], "serialize": False}])

    def test_record_malformed_blocks(self):
        v = self.waves("* F1 [VERIFIED] bullet near-miss — basis: probe\n")
        self.assertEqual(v["verdict"], "WAVES_RECORD_MALFORMED")

    def test_path_spellings_normalize_into_one_group(self):
        # Silent-direction guard: `src/a.py` and `./src/a.py` are ONE
        # path — read as disjoint they would dispatch colliding units
        # in parallel.
        v = self.waves(
            "- F1 [VERIFIED] unit U1 write-set: src/a.py — basis: d\n"
            "- F2 [VERIFIED] unit U2 write-set: ./src/a.py — basis: d\n")
        self.assertEqual(v["waves"],
                         [{"units": ["U1", "U2"], "serialize": True}])
        # The as-named principle: the verdict reports the record's own
        # strings beside the normalized comparison keys.
        self.assertEqual(v["spellings"],
                         {"src/a.py": ["./src/a.py", "src/a.py"]})


# --------------------------------------------------------------------- trend

class TestTrend(RecordFixture):
    def test_worsening_series_with_concentration(self):
        # The design sentence (backlog trend entry): the newest round's
        # findings cite a D-id whose LATEST revision landed at the
        # PREVIOUS RE-LOCK — repairs answering round n-1 land after its
        # A-line and before round n dispatches.
        body = (
            "- D1 [COMMITTED] first design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] one finding — basis: probe\n"
            "- A1 [BIT] one finding — basis: report\n"
            "- D2 [COMMITTED] repair for round 1's finding — basis: F1\n"
            "- A2 [DISPATCHED] round 2 — basis: brief\n"
            "- F2 [VERIFIED] finding one — basis: probe\n"
            "- F3 [VERIFIED] finding two — basis: probe\n"
            "- A2 [BIT] two findings — basis: report\n"
            "- D3 [COMMITTED] re-lock repair for round 2's findings — "
            "basis: F2\n"
            "- A3 [DISPATCHED] round 3 — basis: brief\n"
            "- F4 [VERIFIED] hits the re-lock repair again — basis: D3\n"
            "- F5 [VERIFIED] a second one at the same site — basis: D3\n"
            "- F6 [VERIFIED] and a third — basis: D3\n"
            "- A3 [BIT] three findings — basis: report\n")
        v = self.trend(body)
        self.assertEqual(v["verdict"], "TREND_COMPUTED")
        self.assertEqual(v["rounds"], 3)
        self.assertEqual(v["counts"], [1, 2, 3])
        self.assertEqual(v["trajectory"], "WORSENING")
        self.assertTrue(v["concentration"])
        self.assertTrue(any("D3" in h["repair_ids"] for h in
                            v["concentration_detail"]))

    def test_concentration_window_is_the_relock_not_the_prior_span(self):
        # Discriminating negative pinning the window: D2 is round 1's
        # repair — its latest revision sits inside round 2's SPAN but
        # not at round 2's re-lock, so round-3 findings citing D2 are
        # NOT concentration (the prior-span reading would flag them).
        body = (
            "- D1 [COMMITTED] first design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] one finding — basis: probe\n"
            "- A1 [BIT] one finding — basis: report\n"
            "- D2 [COMMITTED] repair for round 1's finding — basis: F1\n"
            "- A2 [DISPATCHED] round 2 — basis: brief\n"
            "- F2 [VERIFIED] finding one — basis: probe\n"
            "- F3 [VERIFIED] finding two — basis: probe\n"
            "- A2 [BIT] two findings — basis: report\n"
            "- A3 [DISPATCHED] round 3 — basis: brief\n"
            "- F4 [VERIFIED] cites the old repair, not a re-lock one — "
            "basis: D2\n"
            "- F5 [VERIFIED] same — basis: D2\n"
            "- F6 [VERIFIED] same — basis: D2\n"
            "- A3 [BIT] three findings — basis: report\n")
        v = self.trend(body)
        self.assertEqual(v["trajectory"], "WORSENING")
        self.assertFalse(v["concentration"])

    def test_improving_series_no_concentration(self):
        body = (
            "- D1 [COMMITTED] first design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] finding a — basis: probe\n"
            "- F2 [VERIFIED] finding b — basis: probe\n"
            "- F3 [VERIFIED] finding c — basis: probe\n"
            "- A1 [BIT] three findings — basis: report\n"
            "- D2 [COMMITTED] repair for round 1's findings — basis: F1\n"
            "- A2 [DISPATCHED] round 2 — basis: brief\n"
            "- F4 [VERIFIED] finding d — basis: probe\n"
            "- F5 [VERIFIED] finding e — basis: probe\n"
            "- A2 [BIT] two findings — basis: report\n"
            "- D3 [COMMITTED] repair for round 2's findings — basis: F4\n"
            "- A3 [DISPATCHED] round 3 — basis: brief\n"
            "- F6 [VERIFIED] an unrelated finding, cites nothing from the "
            "round-2 repair — basis: probe\n"
            "- A3 [BIT] one finding — basis: report\n")
        v = self.trend(body)
        self.assertEqual(v["verdict"], "TREND_COMPUTED")
        self.assertEqual(v["rounds"], 3)
        self.assertEqual(v["counts"], [3, 2, 1])
        self.assertEqual(v["trajectory"], "IMPROVING")
        self.assertFalse(v["concentration"])

    def test_flat_series(self):
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] finding a — basis: probe\n"
            "- A1 [BIT] one finding — basis: report\n"
            "- A2 [DISPATCHED] round 2 — basis: brief\n"
            "- F2 [VERIFIED] finding b — basis: probe\n"
            "- F3 [VERIFIED] finding c — basis: probe\n"
            "- A2 [BIT] two findings — basis: report\n"
            "- A3 [DISPATCHED] round 3 — basis: brief\n"
            "- F4 [VERIFIED] finding d — basis: probe\n"
            "- A3 [BIT] one finding — basis: report\n")
        v = self.trend(body)
        self.assertEqual(v["counts"], [1, 2, 1])
        self.assertEqual(v["trajectory"], "FLAT")

    def test_void_and_dispatched_rounds_excluded(self):
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- A1 [VOID] premise broke — basis: report\n"
            "- A2 [DISPATCHED] round 2 — basis: brief\n"
            "- F1 [VERIFIED] a finding — basis: probe\n"
            "- A2 [ZERO-DELTA] clean return — basis: report\n"
            "- A3 [DISPATCHED] round 3, still out — basis: brief\n")
        v = self.trend(body)
        self.assertEqual(v["rounds"], 1)
        self.assertEqual(v["counts"], [1])

    def test_no_resolved_rounds(self):
        v = self.trend("- A1 [DISPATCHED] round 1 — basis: brief\n")
        self.assertEqual(v["verdict"], "TREND_NO_ROUNDS")


class TestP26ConcentrationReadsEntryClass(RecordFixture):
    """BACKLOG P26: the concentration flag previously counted ANY
    citing F-line — findings and record-scoped verification/
    confirmation entries alike — so a positive executed-verification
    entry citing the repair it executed (run-2 F82) raised the same
    flag as a genuine finding landing on it. The signal now reads the
    citing entry's CLASS via the record grammar's own scope opener
    (classify_scope): a `record: `-scoped F-line is desk bookkeeping
    — a verification or confirmation — and never concentrates; a
    scopeless (or unit-scoped) F-line is an ordinary finding and
    still does."""

    def _worsening_body(self, citing_line):
        return (
            "- D1 [COMMITTED] first design — basis: probe\n"
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] one finding — basis: probe\n"
            "- A1 [BIT] one finding — basis: report\n"
            "- D2 [COMMITTED] repair for round 1's finding — basis: F1\n"
            "- A2 [DISPATCHED] round 2 — basis: brief\n"
            "- F2 [VERIFIED] finding one — basis: probe\n"
            "- F3 [VERIFIED] finding two — basis: probe\n"
            "- A2 [BIT] two findings — basis: report\n"
            "- D3 [COMMITTED] re-lock repair for round 2's findings — "
            "basis: F2\n"
            "- A3 [DISPATCHED] round 3 — basis: brief\n"
            + citing_line +
            "- A3 [BIT] one entry — basis: report\n")

    def test_verification_entry_citing_the_repair_does_not_concentrate(self):
        # the F82 shape: a record-scoped executed-verification entry
        # citing the re-lock repair it executed — a POSITIVE result,
        # never a finding landing on the repaired ground
        body = self._worsening_body(
            "- F4 [VERIFIED] record: executed the repair from D3 and "
            "confirmed it holds — basis: D3\n")
        v = self.trend(body)
        self.assertEqual(v["verdict"], "TREND_COMPUTED")
        self.assertFalse(v["concentration"], v)
        self.assertEqual(v["concentration_detail"], [])

    def test_scopeless_finding_citing_the_repair_still_concentrates(self):
        # the over-correction control: an ordinary (scopeless) finding
        # citing the same repair must still raise the flag
        body = self._worsening_body(
            "- F4 [VERIFIED] hits the re-lock repair again — basis: D3\n")
        v = self.trend(body)
        self.assertTrue(v["concentration"], v)
        self.assertTrue(any("D3" in h["repair_ids"] for h in
                            v["concentration_detail"]))

    def test_mixed_round_concentrates_on_the_finding_alone(self):
        # a round carrying BOTH a verification and a genuine finding:
        # concentration fires (the finding), and the detail names only
        # the finding, never the verification entry
        body = self._worsening_body(
            "- F4 [VERIFIED] record: executed the repair from D3 and "
            "confirmed it holds — basis: D3\n"
            "- F5 [VERIFIED] a genuine finding on the same repair — "
            "basis: D3\n")
        v = self.trend(body)
        self.assertTrue(v["concentration"], v)
        cited = {h["finding"] for h in v["concentration_detail"]}
        self.assertEqual(cited, {"F5"})


class TestP20SustainGate(RecordFixture):
    """BACKLOG P20 (F143): round-open's mechanical never-sustain
    gate — a new attack round opens only if the latest [BIT] round's
    own findings hold at least one design-substance (non-`record:`)
    member; record/instrument-class findings are desk work and never
    buy a round."""

    def test_all_record_class_round_denies_sustain(self):
        # the F143 shape: A8's four record/instrument-class findings
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] record: a bookkeeping note — basis: probe\n"
            "- F2 [VERIFIED] record: another bookkeeping note — "
            "basis: probe\n"
            "- A1 [BIT] two record-class findings — basis: report\n")
        v = self.sustain(body)
        self.assertEqual(v["verdict"], "SUSTAIN_DENIED", v)
        self.assertEqual(v["round"], "A1")
        self.assertEqual(set(v["record_class"]), {"F1", "F2"})

    def test_mixed_round_sustains(self):
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] record: a bookkeeping note — basis: probe\n"
            "- F2 [VERIFIED] a genuine design finding — basis: probe\n"
            "- A1 [BIT] two findings — basis: report\n")
        v = self.sustain(body)
        self.assertEqual(v["verdict"], "SUSTAIN_OK", v)
        self.assertEqual(v["substance"], ["F2"])
        self.assertEqual(v["record_class"], ["F1"])

    def test_all_substance_round_sustains(self):
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] a genuine design finding — basis: probe\n"
            "- A1 [BIT] one finding — basis: report\n")
        v = self.sustain(body)
        self.assertEqual(v["verdict"], "SUSTAIN_OK", v)

    def test_zero_delta_round_not_applicable(self):
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- A1 [ZERO-DELTA] clean return — basis: report\n")
        v = self.sustain(body)
        self.assertEqual(v["verdict"], "SUSTAIN_NOT_APPLICABLE", v)

    def test_no_rounds_not_applicable(self):
        v = self.sustain("- D1 [COMMITTED] a decision — basis: probe\n")
        self.assertEqual(v["verdict"], "SUSTAIN_NOT_APPLICABLE", v)

    def test_still_dispatched_round_not_applicable(self):
        body = "- A1 [DISPATCHED] round 1 — basis: brief\n"
        v = self.sustain(body)
        self.assertEqual(v["verdict"], "SUSTAIN_NOT_APPLICABLE", v)
        self.assertEqual(v["live_round"], "A1", v)

    def test_malformed_record_blocks(self):
        v = self.sustain("- F1 (VERIFIED) x — basis: y\n")
        self.assertEqual(v["verdict"], "SUSTAIN_RECORD_MALFORMED", v)

    # ------------------------------------------------------ R6 (checkpoint
    # review): a live [DISPATCHED] round is never consulted — it
    # surfaces separately as the verdict's `live_round` field.

    def test_no_live_round_field_is_none(self):
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] a genuine design finding — basis: probe\n"
            "- A1 [BIT] one finding — basis: report\n")
        v = self.sustain(body)
        self.assertEqual(v["verdict"], "SUSTAIN_OK", v)
        self.assertIsNone(v["live_round"], v)

    def test_live_round_surfaces_while_grading_the_prior_resolved_round(self):
        # A1 resolved [BIT] (all record-class, would deny); A2 is a
        # live re-dispatch on top — sustain still grades A1 (the only
        # resolved round) but surfaces A2 as the live round separately
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] record: a bookkeeping note — basis: probe\n"
            "- A1 [BIT] one record-class finding — basis: report\n"
            "- A2 [DISPATCHED] round 2 — basis: brief\n")
        v = self.sustain(body)
        self.assertEqual(v["verdict"], "SUSTAIN_DENIED", v)
        self.assertEqual(v["round"], "A1", v)
        self.assertEqual(v["live_round"], "A2", v)


class TestP19ZeroLandedTripwire(RecordFixture):
    """BACKLOG P19 (P18 measurement): the zero-landed progress
    tripwire — one of the two progress-shaped stop signals the
    budget's hard cap demotes to. Fires when at least `--threshold`
    resolved attack rounds exist yet neither a landing annotation nor
    a V-line does anywhere in the record; either one silences it."""

    def _n_bit_rounds(self, n):
        body = ""
        for i in range(1, n + 1):
            body += (f"- A{i} [DISPATCHED] round {i} — basis: brief\n"
                     f"- F{i} [VERIFIED] a finding — basis: probe\n"
                     f"- A{i} [BIT] one finding — basis: report\n")
        return body

    def test_run_1_shape_fires(self):
        # the run-1 fixture: eight rounds, zero V-lines, zero landings
        v = self.tripwire(self._n_bit_rounds(8), threshold=5)
        self.assertEqual(v["verdict"], "TRIPWIRE_FIRES", v)
        self.assertEqual(v["rounds"], 8)
        self.assertFalse(v["landed"])
        self.assertEqual(v["v_lines"], 0)

    def test_landing_annotation_silences_it(self):
        body = self._n_bit_rounds(8) + "\n  unit U1 landed: abc1234\n"
        v = self.tripwire(body, threshold=5)
        self.assertEqual(v["verdict"], "TRIPWIRE_SILENT", v)
        self.assertTrue(v["landed"])

    def test_v_line_silences_it_without_a_landing(self):
        body = (self._n_bit_rounds(8) +
                "- V1 [ISSUES FOUND] a verify attempt — basis: checks\n")
        v = self.tripwire(body, threshold=5)
        self.assertEqual(v["verdict"], "TRIPWIRE_SILENT", v)
        self.assertFalse(v["landed"])
        self.assertEqual(v["v_lines"], 1)

    def test_below_threshold_is_silent_regardless(self):
        v = self.tripwire(self._n_bit_rounds(2), threshold=5)
        self.assertEqual(v["verdict"], "TRIPWIRE_SILENT", v)
        self.assertEqual(v["rounds"], 2)

    def test_threshold_is_named_by_the_caller_not_hardcoded(self):
        # the same 8-round, zero-landed record reads differently under
        # two different named thresholds
        body = self._n_bit_rounds(8)
        low = self.tripwire(body, threshold=3)
        high = self.tripwire(body, threshold=20)
        self.assertEqual(low["verdict"], "TRIPWIRE_FIRES", low)
        self.assertEqual(high["verdict"], "TRIPWIRE_SILENT", high)

    def test_malformed_record_blocks(self):
        v = self.tripwire("- F1 (VERIFIED) x — basis: y\n", threshold=1)
        self.assertEqual(v["verdict"], "TRIPWIRE_RECORD_MALFORMED", v)


HEADER_WITH_TRIPWIRE_BUDGET = """# Run: test
Status: in-progress
Phase: investigate-design
Skill: statiker 0.2.33
Budget: cycles 7 / rounds 4 / verify 3 / tripwire 5

INTENT — do the thing.

## Cycle 1
"""

HEADER_WITH_BUDGET_NO_TRIPWIRE = """# Run: test
Status: in-progress
Phase: investigate-design
Skill: statiker 0.2.33
Budget: cycles 7 / rounds 4 / verify 3

INTENT — do the thing.

## Cycle 1
"""


class TestR3TripwireArmingFromBudget(RecordFixture):
    """Checkpoint review R3: --threshold is now OPTIONAL — omitted, the
    tool reads the header Budget line's `/ tripwire <n>` field;
    --threshold still overrides; neither present is UNARMED, never a
    guessed default. The verdict's `reason` field distinguishes
    unarmed/silent/fires."""

    def _n_bit_rounds(self, n):
        body = ""
        for i in range(1, n + 1):
            body += (f"- A{i} [DISPATCHED] round {i} — basis: brief\n"
                     f"- F{i} [VERIFIED] a finding — basis: probe\n"
                     f"- A{i} [BIT] one finding — basis: report\n")
        return body

    def test_armed_from_budget_line_and_quiet(self):
        # rounds < the header's threshold (5): silent, reason "silent"
        v = self.tripwire(self._n_bit_rounds(2),
                          header=HEADER_WITH_TRIPWIRE_BUDGET)
        self.assertEqual(v["verdict"], "TRIPWIRE_SILENT", v)
        self.assertEqual(v["reason"], "silent", v)
        self.assertEqual(v["threshold"], 5, v)

    def test_armed_from_budget_line_and_fires(self):
        v = self.tripwire(self._n_bit_rounds(8),
                          header=HEADER_WITH_TRIPWIRE_BUDGET)
        self.assertEqual(v["verdict"], "TRIPWIRE_FIRES", v)
        self.assertEqual(v["reason"], "fires", v)
        self.assertEqual(v["threshold"], 5, v)

    def test_unarmed_with_no_threshold_and_no_budget_field(self):
        # neither --threshold nor a Budget line at all: unarmed
        v = self.tripwire(self._n_bit_rounds(8))
        self.assertEqual(v["verdict"], "TRIPWIRE_SILENT", v)
        self.assertEqual(v["reason"], "unarmed", v)
        self.assertIsNone(v["threshold"])

    def test_unarmed_with_budget_line_lacking_the_tripwire_field(self):
        v = self.tripwire(self._n_bit_rounds(8),
                          header=HEADER_WITH_BUDGET_NO_TRIPWIRE)
        self.assertEqual(v["verdict"], "TRIPWIRE_SILENT", v)
        self.assertEqual(v["reason"], "unarmed", v)

    def test_explicit_threshold_overrides_the_budget_line(self):
        # the header names 5; an explicit --threshold of 2 still fires
        # on the same 8-round record
        v = self.tripwire(self._n_bit_rounds(8), threshold=2,
                          header=HEADER_WITH_TRIPWIRE_BUDGET)
        self.assertEqual(v["verdict"], "TRIPWIRE_FIRES", v)
        self.assertEqual(v["threshold"], 2, v)

    def test_fires_reason_on_the_ordinary_explicit_path(self):
        v = self.tripwire(self._n_bit_rounds(8), threshold=5)
        self.assertEqual(v["verdict"], "TRIPWIRE_FIRES", v)
        self.assertEqual(v["reason"], "fires", v)


# -------------------------------------------------------------------- filter

class TestFilter(RecordFixture):
    def make_repo_with_tracker(self, committed_text, worktree_text=None):
        env = {**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null",
               "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        def git(*a):
            subprocess.run(["git", *a], cwd=self.dir, env=env,
                           capture_output=True, check=True)
        git("init", "-b", "main")
        p = self.dir / "t.md"
        p.write_text(committed_text)
        git("add", "t.md")
        git("commit", "-m", "lock")
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.dir,
                             env=env, capture_output=True, text=True,
                             check=True).stdout.strip()
        if worktree_text is not None:
            p.write_text(worktree_text)
        return sha

    def test_filter_drops_both_species_and_reads_the_sha(self):
        committed = (HEADER +
                     "- F1 [VERIFIED] kept entry — basis: y\n"
                     "> Superseded — A2 quotes\n"
                     "> quoted finding text\n"
                     ">\n"
                     "> more quote\n"
                     "- F2 [VERIFIED] entry after block — basis: y\n"
                     "## Superseded — legacy section\n"
                     "old landing text\n"
                     "## Cycle 2\n"
                     "- F3 [VERIFIED] kept too — basis: y\n")
        sha = self.make_repo_with_tracker(
            committed, worktree_text=HEADER + "LIVE TREE ONLY\n")
        # the artifact lands OUTSIDE the repo (attack-8 NIT3)
        self._out_tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._out_tmp.cleanup)
        out = Path(self._out_tmp.name) / "artifact.md"
        p = tool(["filter", "--tracker", "t.md", "--sha", sha,
                  "--out", str(out)], cwd=self.dir)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "ARTIFACT_WRITTEN")
        text = out.read_text()
        self.assertIn("kept entry", text)
        self.assertIn("entry after block", text)
        self.assertIn("kept too", text)
        self.assertNotIn("quoted finding", text)
        self.assertNotIn("legacy section", text)
        self.assertNotIn("old landing text", text)
        self.assertNotIn("LIVE TREE ONLY", text)  # served the sha, not the tree
        # ES-3: the species are BLANKED in place, not dropped — the
        # counts are renamed with the mechanism they now count
        self.assertEqual(v["blocks_blanked"], 1)
        self.assertEqual(v["sections_blanked"], 1)
        self.assertEqual(v["lines_out"], v["lines_in"])

    def test_entries_inside_a_superseded_section_are_preserved(self):
        # attack-9: the section drop swallowed EVERY line under the
        # heading, entries included — SKILL.md (The attack) makes the
        # opposite the contract: "entry-shaped lines inside a
        # Superseded SECTION are PRESERVED ... ENTRIES are never
        # filtered", a section drop that swallowed entries having put
        # a live money-path finding out of every attacker's sight.
        committed = (HEADER +
                     "- F1 [VERIFIED] before the section — basis: y\n"
                     "## Superseded — legacy section\n"
                     "old landing prose\n"
                     "- F2 [VERIFIED] entry inside the section — basis: y\n"
                     "- D3 [COMMITTED] second entry inside — basis: F2\n"
                     "more legacy prose\n"
                     "## Cycle 2\n"
                     "- F4 [VERIFIED] after the section — basis: y\n")
        sha = self.make_repo_with_tracker(committed)
        self._out_tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._out_tmp.cleanup)
        out = Path(self._out_tmp.name) / "artifact.md"
        v = self.verdict(tool(["filter", "--tracker", "t.md", "--sha", sha,
                               "--out", str(out)], cwd=self.dir))
        self.assertEqual(v["verdict"], "ARTIFACT_WRITTEN")
        text = out.read_text()
        self.assertIn("entry inside the section", text)
        self.assertIn("second entry inside", text)
        self.assertIn("before the section", text)
        self.assertIn("after the section", text)
        # the section's non-entry lines and its heading still drop
        self.assertNotIn("old landing prose", text)
        self.assertNotIn("more legacy prose", text)
        self.assertNotIn("legacy section", text)
        self.assertEqual(v["sections_blanked"], 1)


# --------------------------------------------------------------------- quote

class TestQuote(RecordFixture):
    def test_defang_and_block_form(self):
        raw = ("The design held [VERIFIED] status.\n"
               "\n"
               "One entry was [AUTO-ACCEPTED] silently.\n")
        p = tool(["quote", "--label", "A7 quotes"], stdin_text=raw)
        v = self.verdict(p)
        block = v["block"]
        lines = block.splitlines()
        self.assertEqual(
            lines[0], "> Superseded — A7 quotes; verified, auto-accepted")
        for l in lines:
            self.assertTrue(l.startswith(">"), repr(l))
        self.assertIn("verified status", block)
        self.assertIn("auto-accepted silently", block)
        self.assertIn(">\n", block + "\n")  # blank became bare '>'
        # no bracketed counted literal survives, in either case
        self.assertNotIn("[VERIFIED]", block)
        self.assertNotIn("[verified]", block)
        self.assertNotIn("[AUTO-ACCEPTED]", block)

    def test_no_literals_no_semicolon(self):
        p = tool(["quote", "--label", "A7 quotes"], stdin_text="plain text\n")
        v = self.verdict(p)
        self.assertEqual(v["block"].splitlines()[0], "> Superseded — A7 quotes")


class TestAttack7Findings(RecordFixture):
    """Repairs from attack 7 (dev-notes, 2026-08-07), each red against
    the pre-repair behavior the attacker executed."""

    def test_usage_error_emits_verdict_line(self):
        # attack-7 B1: bare argparse death on exit 2 with no verdict —
        # the git tool's 0.2.35 repair, carried across
        p = tool(["sweep"])
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertEqual(p.returncode, 3)

    def test_mis_scoped_premise_kill_voids(self):
        # attack-7 N1: a record:-opening post-closure line invalidating
        # an entry LIVE at the closure dispatched U2 on a dead premise
        body = (CLOSED +
                "- D1 [INVALIDATED] record: the shared parser never "
                "existed — basis: F9\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "CLOSURE_VOID")

    def test_dead_entry_record_bookkeeping_still_allowed(self):
        # the N1 check's boundary: bookkeeping over an ALREADY-dead
        # entry (the skill's prescribed re-disposition form) must not
        # void
        body = ("- D1 [COMMITTED] the design — basis: probe\n"
                "- D1 [INVALIDATED] premise died — basis: F9\n"
                "- A1 [DISPATCHED] round 1 — basis: brief\n"
                "- A1 [ZERO-DELTA] clean return — basis: report\n"
                "- D1 [INVALIDATED] record: clause 2 dead (killed) — "
                "basis: F9\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")

    def test_filter_accepts_absolute_tracker_path(self):
        # attack-7 N3: one path grammar across subcommands — an
        # absolute path worked in lint and failed in filter
        f = TestFilter("test_filter_drops_both_species_and_reads_the_sha")
        committed = HEADER + "- F1 [VERIFIED] kept — basis: y\n"
        f._tmp = self._tmp
        f.dir = self.dir
        sha = TestFilter.make_repo_with_tracker(f, committed)
        with tempfile.TemporaryDirectory() as outdir:
            out = Path(outdir) / "a.md"
            p = tool(["filter", "--tracker", str(self.dir / "t.md"),
                      "--sha", sha, "--out", str(out)], cwd=self.dir)
            v = self.verdict(p)
            self.assertEqual(v["verdict"], "ARTIFACT_WRITTEN")

    def test_lint_resolves_repo_relative_from_subdir(self):
        # attack-7 N3 mirror: repo-relative path from a subdirectory
        # worked in filter and failed in lint
        f = TestFilter("test_filter_drops_both_species_and_reads_the_sha")
        committed = HEADER + "- F1 [VERIFIED] kept — basis: y\n"
        f._tmp = self._tmp
        f.dir = self.dir
        TestFilter.make_repo_with_tracker(f, committed)
        sub = self.dir / "sub"
        sub.mkdir()
        p = tool(["lint", "--tracker", "t.md"], cwd=sub)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "LINT_CLEAN")

    def test_amendments_carry_only_latest_line(self):
        # attack-7 NIT5: the stale held: line traveled beside its
        # resolving line into the re-dispatch brief
        body = (CLOSED +
                "- D9 [AUTO-ACCEPTED] unit U2 held: x.txt — basis: F9\n"
                "- D9 [COMMITTED] unit U2 cleared: x.txt — basis: reply\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")
        self.assertEqual(len(v["amendments"]), 1)
        self.assertIn("cleared", v["amendments"][0]["line"])

    def test_phase_admission_window_discriminated(self):
        # attack-7 N6: the Phase branch was only ever co-triggered
        # with Status past the window
        filler = "filler line\n" * 25
        v = self.lint("- F1 [VERIFIED] x — basis: y\n",
                      header="# Run: t\nStatus: in-progress\n"
                             + filler + "Phase: verify\n\n")
        self.assertIn("admission-window", self.violation_codes(v))

    def test_void_a_line_lints_clean_and_gates_closure(self):
        # 0.2.37 hypothesis mint: [VOID] is a legal A-tag (aborted or
        # premise-broken round); a voided last round is no closure
        v = self.lint("- A1 [VOID] premise: wrong sha pinned — basis: brief\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN")
        v2 = self.closure("- A1 [DISPATCHED] round 1 — basis: brief\n"
                          "- A1 [VOID] abort: killed by F9 — basis: F9\n")
        self.assertEqual(v2["verdict"], "CLOSURE_ABSENT")

    def test_landing_annotation_needs_blank_line_before(self):
        # attack-7 NIT2: the blank-line half of the landing rule is as
        # computable as the indent half
        v = self.lint("- D1 [COMMITTED] x — basis: y\n"
                      "  unit U1 landed: abc1234\n")
        self.assertEqual(v["verdict"], "LINT_VIOLATIONS")
        self.assertIn("landing-blank", self.violation_codes(v))


class TestAttack8Findings(RecordFixture):
    """Repairs from attack 8 (dev-notes, 2026-08-07), each red against
    the pre-repair behavior the attacker executed."""

    # -- B2: the closure gate reads parse violations -------------------

    def test_closure_holds_on_bracketless_a_line(self):
        # attack-8 B2 (P10c): "- A2 BIT ..." failed ENTRY_RE, vanished
        # from entries, and the closure answered CLOSURE_LIVE off A1
        body = (CLOSED +
                "- A2 BIT round 2 found the wrong mechanism — basis: report\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertTrue(any(x["code"] == "entry-form"
                            for x in v["violations"]))

    def test_closure_holds_on_bracketless_invalidation(self):
        # attack-8 B2 (P8b): a premise-kill missing its brackets read
        # as UNIT_DISPATCHABLE instead of anything at all
        body = (CLOSED +
                "- D1 INVALIDATED approach rests on a dead premise "
                "— basis: F9\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")

    def test_closure_holds_on_tag_enum_violation(self):
        body = (CLOSED +
                "- D2 [BOGUS] some line — basis: y\n")
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")

    def test_closure_malformed_disarmed_by_corrects_line_token(self):
        # append-only means the malformed line never leaves the file:
        # a LATER clean line for the same id carrying the literal
        # `corrects line <n>` token is the repair form (SKILL.md,
        # Implementation), and the gate must accept it or one typo
        # bricks the run's closure. Rewritten from the tag-match
        # disarm this release removes (attack-10 B1/B2).
        bad = "- A2 BIT round 2 found the wrong mechanism — basis: report\n"
        n = self.lineno_of(CLOSED + bad, "- A2 BIT")
        body = (CLOSED + bad +
                f"- A2 [BIT] round 2 found the wrong mechanism (corrects "
                f"line {n}) — basis: report\n")
        v = self.closure(body)
        # A2 [BIT] governs and carries no design-amending disposition
        # after it — P27 grades that SATISFIED, same as ZERO-DELTA
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")

    def test_closure_ignores_nonentry_violation_classes(self):
        # boundary: a stray quoted line is lint's business at its own
        # seams; it cannot corrupt the entry set the closure computes
        body = ("> stray quoted line\n" + CLOSED)
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")

    # -- N1: one path grammar reaches the record tool ------------------

    def test_record_gates_halt_on_out_of_repo_tracker(self):
        # attack-8 N1 (P2/P12): every record-side gate was satisfiable
        # by a file the run can never pin
        with tempfile.TemporaryDirectory() as outside:
            t = Path(outside) / "t.md"
            t.write_text(HEADER + CLOSED)
            for sub in (["lint"], ["sweep"], ["closure"]):
                p = tool([*sub, "--tracker", str(t)], cwd=self.dir)
                v = self.verdict(p)
                self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO",
                                 f"{sub[0]} accepted an out-of-repo tracker")
                self.assertEqual(p.returncode, 2)

    def test_record_gates_halt_on_tracker_no_repo_contains(self):
        # re-derived at attack-9's tracker-anchored resolution: this
        # case formerly read LINT_CLEAN on the rationale that "only a
        # SURROUNDING repo makes an outside path a defect" — a
        # statement of the CWD-anchored grammar that resolution
        # replaces. Anchored at the tracker, there is no surrounding
        # repo to appeal to and the pinnability question has one
        # answer: a tracker no repo contains can never be pinned, so
        # N1's gate holds here too, from every cwd.
        with tempfile.TemporaryDirectory() as norepo:
            t = Path(norepo) / "t.md"
            t.write_text(HEADER + "- F1 [VERIFIED] x — basis: y\n")
            for cwd in (norepo, str(self.dir)):
                p = tool(["lint", "--tracker", str(t)], cwd=cwd)
                v = self.verdict(p)
                self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO", cwd)
                self.assertEqual(p.returncode, 2)

    # -- N3: --unit validates its form ---------------------------------

    def test_closure_unit_id_form_validated(self):
        # attack-8 N3 (P13): "3", "u3", "" cleared a U3 hold silently
        body = (CLOSED +
                "- D9 [AUTO-ACCEPTED] unit U3 held: x.txt — basis: F9\n")
        path = str(self.write_tracker(body))
        for bad in ("3", "u3", "unit U3", ""):
            p = tool(["closure", "--tracker", path, "--unit", bad],
                     cwd=self.dir)
            v = self.verdict(p)
            self.assertEqual(v["verdict"], "USAGE_ERROR",
                             f"--unit {bad!r} was not rejected")
            self.assertEqual(p.returncode, 3)
        # the well-formed id still routes to the hold
        p = tool(["closure", "--tracker", path, "--unit", "U3"],
                 cwd=self.dir)
        self.assertEqual(self.verdict(p)["verdict"], "UNIT_HELD")

    # -- NIT2: quote returns its production count ----------------------

    def test_quote_carries_line_count(self):
        p = tool(["quote", "--label", "A7 quotes"],
                 stdin_text="one\ntwo\n")
        v = self.verdict(p)
        self.assertEqual(v["lines"], len(v["block"].splitlines()))

    # -- NIT3: the attack artifact never lands inside the repo ---------

    def test_filter_halts_on_in_repo_out_path(self):
        # attack-8 NIT3 (P14): an in-repo artifact is an untracked
        # file under a brief asserting tree == lock commit
        f = TestFilter("test_filter_drops_both_species_and_reads_the_sha")
        f._tmp, f.dir = self._tmp, self.dir
        sha = TestFilter.make_repo_with_tracker(
            f, HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        p = tool(["filter", "--tracker", "t.md", "--sha", sha,
                  "--out", "attack-artifact.md"], cwd=self.dir)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "ARTIFACT_IN_REPO")
        self.assertEqual(p.returncode, 2)
        self.assertFalse((self.dir / "attack-artifact.md").exists(),
                         "halt must precede the write")


class TestAttack9ClosureSoundness(RecordFixture):
    """Region-2 repairs from attack 9 (dev-notes, 2026-08-07): the
    disarm requires RE-ASSERTION (same id, same tag), and entry-shape
    near-misses outside ENTRY_HEAD_RE's reach are minted as their own
    violation class. Each red against 0.2.38."""

    KILL_CONTROL = (CLOSED +
                    "- D1 [INVALIDATED] premise killed by new evidence "
                    "— basis: F9\n")

    def test_control_wellformed_kill_voids(self):
        v = self.closure(self.KILL_CONTROL, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_VOID")

    def test_disarm_requires_the_corrects_line_token(self):
        # attack-9 B2 in its 0.2.43 form: a later same-id line that
        # corrects nothing must not disarm — whatever tag it carries
        body = (CLOSED +
                "- D1 [INVALIDATED premise killed by new evidence "
                "— basis: F9\n"
                "- D1 [COMMITTED] unit U1 unrelated note, corrects "
                "nothing — basis: F8\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")

    def test_same_tag_reassertion_without_the_token_stays_armed(self):
        # attack-10 B2: the removed tag-match disarm was FORGEABLE —
        # any later same-id/same-tag line converted a premise-kill
        # void into a dispatch without correcting anything
        body = (CLOSED +
                "- D1 [INVALIDATED premise killed by new evidence "
                "— basis: F9\n"
                "- D1 [INVALIDATED] unit U1 an unrelated later "
                "disposition — basis: F8\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")

    def test_corrects_line_token_disarms_and_content_is_read(self):
        # the repair form (SKILL.md, Implementation): re-state the
        # malformed line under its own id with the literal
        # `corrects line <n>` token — the closure then reads the
        # premise-kill the malformed line carried
        bad = ("- D1 [INVALIDATED premise killed by new evidence "
               "— basis: F9\n")
        n = self.lineno_of(CLOSED + bad, "[INVALIDATED premise")
        body = (CLOSED + bad +
                f"- D1 [INVALIDATED] premise killed by new evidence "
                f"(corrects line {n}) — basis: F9\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_VOID")

    def test_corrects_line_token_must_name_the_violation_line(self):
        # the token is line-addressed: a repair pointing at some other
        # line disarms nothing (else the token degrades to a phrase)
        bad = ("- D1 [INVALIDATED premise killed by new evidence "
               "— basis: F9\n")
        n = self.lineno_of(CLOSED + bad, "[INVALIDATED premise")
        body = (CLOSED + bad +
                f"- D1 [INVALIDATED] premise killed by new evidence "
                f"(corrects line {n + 7}) — basis: F9\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")

    def test_near_miss_missing_space_blocks(self):
        # attack-9 B3: `-D1 ...` matches neither regex — no entry, no
        # violation, premise-kill invisible
        body = (CLOSED +
                "-D1 [INVALIDATED] premise killed by new evidence "
                "— basis: F9\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")

    def test_near_miss_leading_space_blocks(self):
        body = (CLOSED +
                " - D1 [INVALIDATED] premise killed by new evidence "
                "— basis: F9\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")

    def test_near_miss_disarmed_by_corrects_line_token(self):
        bad = ("-D1 [INVALIDATED] premise killed by new evidence "
               "— basis: F9\n")
        n = self.lineno_of(CLOSED + bad, "-D1 [INVALIDATED]")
        body = (CLOSED + bad +
                f"- D1 [INVALIDATED] premise killed by new evidence "
                f"(corrects line {n}) — basis: F9\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_VOID")

    def test_near_miss_lints(self):
        v = self.lint("-D1 [COMMITTED] a decision — basis: y\n")
        self.assertEqual(v["verdict"], "LINT_VIOLATIONS")
        self.assertIn("entry-near-miss", self.violation_codes(v))

    def test_landing_annotation_not_a_near_miss(self):
        # boundary: the indented landing annotation and ordinary prose
        # stay legal
        v = self.lint("- D1 [COMMITTED] x — basis: y\n"
                      "\n"
                      "  unit U1 landed: abc1234\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN")


class TestAttack9TrackerAnchoredRepo(RecordFixture):
    """attack-9: repo_paths ran `git rev-parse --show-toplevel` with no
    cwd, so the repo was the CALLER's, not the tracker's — the same
    absolute tracker answered differently from three cwds (clean here,
    PIN_UNREADABLE 'does not resolve inside a git repo' from outside
    any repo, PATH_OUTSIDE_REPO from a sibling repo). SKILL.md ('The
    tools'): the record tool anchors its repo at the TRACKER's own
    directory. Each test red against the cwd-anchored resolution."""

    def other_repo(self):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=d,
                       env={**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null"},
                       capture_output=True, check=True)
        return d

    def no_repo_dir(self):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        return d

    def three_cwds(self):
        # the tracker's own repo, a DIFFERENT repo, and no repo at all
        return [str(self.dir), self.other_repo(), self.no_repo_dir()]

    def test_gates_answer_identically_from_every_cwd(self):
        t = str(self.write_tracker(CLOSED))
        for sub, expected in (("lint", "LINT_CLEAN"),
                              ("sweep", "SWEEP_CLEAN"),
                              ("closure", "CLOSURE_LIVE")):
            for cwd in self.three_cwds():
                v = self.verdict(tool([sub, "--tracker", t], cwd=cwd))
                self.assertEqual(v["verdict"], expected,
                                 f"{sub} from cwd {cwd}")

    def test_filter_answers_identically_from_every_cwd(self):
        f = TestFilter("test_filter_drops_both_species_and_reads_the_sha")
        f._tmp, f.dir = self._tmp, self.dir
        sha = TestFilter.make_repo_with_tracker(
            f, HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        t = str(self.dir / "t.md")
        for cwd in self.three_cwds():
            outdir = self.no_repo_dir()
            p = tool(["filter", "--tracker", t, "--sha", sha,
                      "--out", os.path.join(outdir, "a.md")], cwd=cwd)
            v = self.verdict(p)
            self.assertEqual(v["verdict"], "ARTIFACT_WRITTEN",
                             f"filter from cwd {cwd}")

    def test_tracker_symlinked_outward_halts(self):
        # REVERSED by 0.2.49's ES-7 (design-attack R3-B7). attack-9
        # made containment TEXTUAL to stop realpath substituting a
        # link's target for the brief's own path; the SUBSTITUTION ban
        # stands, but the containment DECISION now runs on the real
        # path — a tracker named inside the repo whose bytes live
        # outside it can never be pinned there, and every gate was
        # satisfiable by exactly that.
        outside = self.no_repo_dir()
        real = Path(outside) / "real.md"
        real.write_text(HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        link = self.dir / "linked.md"
        os.symlink(str(real), link)
        v = self.verdict(tool(["lint", "--tracker", str(link)],
                              cwd=str(self.dir)))
        self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO")

    def test_form_feed_does_not_shift_reported_line_numbers(self):
        # attack-9: str.splitlines() also breaks on U+000C, U+2028 and
        # U+0085, so one form feed in a body shifted every later
        # violation's line number off the file's own numbering — the
        # desk repairs the line the tool names.
        body = ("- F1 [VERIFIED] a fact with a \x0c form feed — basis: y\n"
                "- F2 [VERIFIED] plain — basis: y\n"
                "- F3 (VERIFIED) malformed — basis: y\n")
        path = self.write_tracker(body)
        v = self.verdict(tool(["lint", "--tracker", str(path)],
                              cwd=str(self.dir)))
        self.assertEqual(v["verdict"], "LINT_VIOLATIONS")
        viol = next(x for x in v["violations"] if x["code"] == "entry-form")
        file_lines = path.read_text().split("\n")
        expected = next(i for i, l in enumerate(file_lines, 1)
                        if l.startswith("- F3"))
        self.assertEqual(viol["line"], expected,
                         "reported line number is not the file's")

    def test_filter_counts_newline_lines(self):
        f = TestFilter("test_filter_drops_both_species_and_reads_the_sha")
        f._tmp, f.dir = self._tmp, self.dir
        committed = (HEADER +
                     "- F1 [VERIFIED] a fact with a \x0c form feed — "
                     "basis: y\n"
                     "- F2 [VERIFIED] plain — basis: y\n")
        sha = TestFilter.make_repo_with_tracker(f, committed)
        out = os.path.join(self.no_repo_dir(), "a.md")
        v = self.verdict(tool(["filter", "--tracker", "t.md", "--sha", sha,
                               "--out", out], cwd=str(self.dir)))
        self.assertEqual(v["verdict"], "ARTIFACT_WRITTEN")
        self.assertEqual(v["lines_in"],
                         len(committed.rstrip("\n").split("\n")))

    def inner_repo_with_committed_tracker(self):
        """An inner checkout nested inside self.dir's repo, tracker
        committed. Returns (inner_dir, sha)."""
        env = {**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null",
               "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        inner = self.dir / "inner"
        inner.mkdir()

        def git(*a):
            subprocess.run(["git", *a], cwd=inner, env=env,
                           capture_output=True, check=True)
        git("init", "-q", "-b", "main")
        (inner / "t.md").write_text(
            HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        git("add", "t.md")
        git("commit", "-m", "lock")
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=inner,
                             env=env, capture_output=True, text=True,
                             check=True).stdout.strip()
        return inner, sha

    def test_artifact_halts_inside_a_nested_outer_checkout(self):
        # attack-9: ARTIFACT_IN_REPO checked only the TRACKER's repo,
        # so an --out into the surrounding checkout wrote an untracked
        # file into someone else's tree — the exposure SKILL.md names
        # ("a NESTED outer checkout has the same exposure; the tool
        # halts ARTIFACT_IN_REPO on any").
        inner, sha = self.inner_repo_with_committed_tracker()
        out = self.dir / "outer-art.md"
        p = tool(["filter", "--tracker", str(inner / "t.md"),
                  "--sha", sha, "--out", str(out)], cwd=str(inner))
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "ARTIFACT_IN_REPO")
        self.assertEqual(p.returncode, 2)
        self.assertFalse(out.exists(), "halt must precede the write")
        self.assertIn(str(self.dir), v["repo"])

    def test_missing_out_parent_is_a_usage_error(self):
        # attack-9: the open() died through the generic handler as
        # INTERNAL_ERROR — a tool defect verdict for an invocation
        # mistake, routed as one
        f = TestFilter("test_filter_drops_both_species_and_reads_the_sha")
        f._tmp, f.dir = self._tmp, self.dir
        sha = TestFilter.make_repo_with_tracker(
            f, HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        out = os.path.join(self.no_repo_dir(), "no-such-dir", "a.md")
        p = tool(["filter", "--tracker", "t.md", "--sha", sha,
                  "--out", out], cwd=str(self.dir))
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertEqual(p.returncode, 3)
        self.assertIn(out, v["error"])

    def test_filter_no_repo_tracker_unified_verdict(self):
        # one cause, one verdict (dispatch gaps 2+3, desk-dispositioned):
        # a tracker no repo contains halts PATH_OUTSIDE_REPO from EVERY
        # subcommand — filter's former PIN_UNREADABLE split answered a
        # second name for the identical condition. PIN_UNREADABLE keeps
        # its plain sense: an unreadable SHA in an existing repo.
        outside = self.no_repo_dir()
        t = Path(outside) / "t.md"
        t.write_text(HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        p = tool(["filter", "--tracker", str(t), "--sha", "HEAD",
                  "--out", os.path.join(self.no_repo_dir(), "a.md")],
                 cwd=self.dir)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO")
        self.assertIn("tracker's location", v["error"])


class TestAttack10CorrectsLineDisarm(RecordFixture):
    """attack-10 B1/B2 (dev-notes, 2026-08-07): the tag-match disarm was
    both BRICKABLE — a tag-enum violation stored a SUMMARY, so a
    misspelled tag extracted nothing and no re-assertion could ever
    disarm it — and FORGEABLE. It is removed, not patched: the disarm
    is the literal `corrects line <n>` token (SKILL.md, Implementation),
    and every blocking violation carries the FULL offending line."""

    def test_misspelled_tag_repairable_by_corrects_line(self):
        # attack-10 B1: `[COMMITED]` bricked the run's closure forever
        bad = "- D2 [COMMITED] unit U1 the letter lands — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "[COMMITED]")
        v_armed = self.closure(CLOSED + bad, unit="U1")
        self.assertEqual(v_armed["verdict"], "CLOSURE_RECORD_MALFORMED")
        body = (CLOSED + bad +
                f"- D2 [COMMITTED] unit U1 the letter lands (corrects "
                f"line {n}) — basis: probe\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")

    def test_malformed_premise_kill_corrected_still_voids(self):
        # the content is READ through the repair: a premise-kill
        # written malformed and corrected by the token voids the
        # closure exactly as a well-formed one does
        bad = "- D1 [INVALIDATE] the premise died — basis: F9\n"
        n = self.lineno_of(CLOSED + bad, "[INVALIDATE]")
        body = (CLOSED + bad +
                f"- D1 [INVALIDATED] the premise died (corrects line "
                f"{n}) — basis: F9\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_VOID")

    def test_blocking_violations_carry_the_full_offending_line(self):
        # attack-10 B1's cause: a summary in `text` is not the line the
        # desk repairs, and the disarm is addressed at that line
        lines = [
            "- D2 [COMMITED] unit U1 out-of-enum tag — basis: probe",
            "- D3 (COMMITTED) broken brackets — basis: probe",
            "* D4 [COMMITTED] bullet near-miss — basis: probe",
            "- D5 [COMMITTED] Unit U1 scope near-miss — basis: probe",
            "- D6 [AUTO-ACCEPTED] unit U1 HELD: x.txt — basis: probe",
        ]
        body = CLOSED + "".join(l + "\n" for l in lines)
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        texts = {viol["text"] for viol in v["violations"]}
        for l in lines:
            self.assertIn(l, texts, f"no violation carries the line: {l}")
        for viol in v["violations"]:
            self.assertEqual(
                viol["text"],
                (HEADER + body).split("\n")[viol["line"] - 1],
                f"{viol['code']} text is not the file's own line")


class TestAttack10NearMissReach(RecordFixture):
    """attack-10: `- ` and ` - ` were the only near-miss prefixes the
    lint could see, so a design-kill written under any other
    bullet-like opener stayed invisible to every predicate and the
    unit dispatched on a dead premise. SKILL.md (The record): the
    entry head is a CASE-SENSITIVE LITERAL and its spacing/case
    near-misses lint as their own class."""

    ESCAPES = ["* F9", "+ F9", "– F9", "— F9", "• F9", "1. F9", "- f9"]

    def kill_line(self, prefix):
        return (f"{prefix} [INVALIDATED] the premise died — basis: probe\n")

    def test_every_bullet_escape_blocks_the_closure(self):
        for prefix in self.ESCAPES:
            body = CLOSED + self.kill_line(prefix)
            v = self.closure(body, unit="U1")
            self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED",
                             f"{prefix!r} dispatched on a dead premise")
            self.assertIn("entry-near-miss", self.violation_codes(v))

    def test_every_bullet_escape_lints(self):
        for prefix in self.ESCAPES:
            v = self.lint(self.kill_line(prefix))
            self.assertEqual(v["verdict"], "LINT_VIOLATIONS", prefix)
            self.assertIn("entry-near-miss", self.violation_codes(v))

    def test_indented_and_prose_bullets_stay_legal(self):
        # the boundary the widened reach must not eat
        v = self.lint("- D1 [COMMITTED] x — basis: y\n"
                      "\n"
                      "  unit U1 landed: abc1234\n"
                      "\n"
                      "* an ordinary prose bullet\n"
                      "1. a numbered prose item\n"
                      "- see the F-lines above for the basis\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN")

    def test_bullet_escape_repairable_by_corrects_line(self):
        bad = "* F9 [INVALIDATED] the premise died — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "* F9")
        body = (CLOSED + bad +
                f"- F9 [INVALIDATED] the premise died (corrects line "
                f"{n}) — basis: probe\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_VOID")

    def test_lowercase_class_letter_repair_matches_the_intended_id(self):
        # `- f9` names F9: the disarm resolves the id case-insensitively
        bad = "- f9 [INVALIDATED] the premise died — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "- f9")
        body = (CLOSED + bad +
                f"- F9 [INVALIDATED] the premise died (corrects line "
                f"{n}) — basis: probe\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_VOID")


class TestAttack10ScopeNearMiss(RecordFixture):
    """attack-10: the scope openers are CASE-SENSITIVE LITERALS
    (SKILL.md, The record), but every case/spacing variant read as
    ordinary scopeless prose — a bookkeeping line spelled `Record:`
    voided a live closure, and no verdict named the one-character
    cause. The variants lint as their own blocking class."""

    VARIANTS = ["Record: bookkeeping",
                "record : bookkeeping",
                "Unit U1 the letter lands",
                "unit  U1 the letter lands",
                "units U1 the letter lands"]

    def test_every_scope_variant_blocks_and_names_the_class(self):
        for body_text in self.VARIANTS:
            body = CLOSED + f"- D5 [COMMITTED] {body_text} — basis: probe\n"
            v = self.closure(body, unit="U1")
            self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED",
                             f"{body_text!r} read as scopeless prose")
            self.assertIn("scope-near-miss", self.violation_codes(v))

    def test_exact_openers_stay_clean(self):
        # the boundary: the literals themselves are never near-misses
        v = self.lint("- D5 [COMMITTED] record: bookkeeping — basis: y\n"
                      "- R2 [AMENDED] unit U2 new letter — basis: y\n"
                      "- D9 [AUTO-ACCEPTED] unit U10 held: x.txt — basis: y\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN")

    def test_scope_variant_repair_supersedes_the_corrected_line(self):
        # 0.2.44 settles what 0.2.43 left open (GAP-1): the corrected
        # line is SUPERSEDED WHOLE, so it no longer reads as a
        # scopeless post-closure line and no longer voids the closure
        # its own repair had just unlocked.
        bad = "- D5 [COMMITTED] Record: bookkeeping — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "Record:")
        body = (CLOSED + bad +
                f"- D5 [COMMITTED] record: bookkeeping (corrects line "
                f"{n}) — basis: probe\n"
                # E-B: U1 must be a KNOWN unit for closure --unit U1
                # to read at all
                "- D0 [INVALIDATED] unit U1 established (never "
                "dispatched) — basis: design\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")


class TestAttack10HoldForm(RecordFixture):
    """attack-10: the hold read was a bare `"held:" in body` substring
    — it MISSED every spelling variant of the literal SKILL.md
    prescribes (`unit U<k> held: ` as the body's opening) and it
    OVER-FIRED on `withheld:` in an ordinary gap line. Anchored to the
    literal, with the variants lifted into their own blocking class."""

    def hold_body(self, line):
        return CLOSED + line + "\n"

    def test_clean_hold_still_holds(self):
        v = self.closure(
            self.hold_body("- D9 [AUTO-ACCEPTED] unit U2 held: x.txt "
                           "— basis: F9"), unit="U2")
        self.assertEqual(v["verdict"], "UNIT_HELD")

    def test_uppercase_hold_lints_hold_form(self):
        v = self.closure(
            self.hold_body("- D9 [AUTO-ACCEPTED] unit U2 HELD: x.txt "
                           "— basis: F9"), unit="U2")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("hold-form", self.violation_codes(v))

    def test_dash_punctuated_hold_lints_hold_form(self):
        v = self.closure(
            self.hold_body("- D9 [AUTO-ACCEPTED] unit U2 held — x.txt "
                           "— basis: F9"), unit="U2")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("hold-form", self.violation_codes(v))

    def test_hold_form_under_another_tag_lints(self):
        # the hold form is [AUTO-ACCEPTED]'s: written under any other
        # tag it holds nothing, and read as an ordinary amendment it
        # dispatches the unit its author meant to stop
        v = self.closure(
            self.hold_body("- D9 [PENDING] unit U2 held: x.txt "
                           "— basis: F9"), unit="U2")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("hold-form", self.violation_codes(v))

    def test_withheld_in_a_gap_line_is_not_a_hold(self):
        # the over-fire: `withheld:` contains `held:` and stopped a
        # unit nothing was holding
        v = self.closure(
            self.hold_body("- D9 [AUTO-ACCEPTED] unit U2 gap: the "
                           "operator withheld: approval — basis: F9"),
            unit="U2")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")

    def test_hold_for_another_unit_does_not_hold_this_one(self):
        # E-B: U2 must be a KNOWN unit for closure --unit U2 to read
        # at all — the dead establishing line never counts as U2's
        # hold or amendment ([INVALIDATED])
        body = (self.hold_body(
                    "- D9 [AUTO-ACCEPTED] unit U3 held: x.txt "
                    "— basis: F9") +
                "- D0 [INVALIDATED] unit U2 established (never "
                "dispatched) — basis: design\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")


class TestWriteSetNearMiss(RecordFixture):
    """write-set: near-miss detection joins the lint. A near-missed
    `write-set: ` declarator (wrong case, missing hyphen, missing
    colon, extra spacing) fails UNIT_WRITE_SET_RE silently — the unit
    reads UNPLANNABLE (waves) with no lint pointing at the slip, and a
    closure resting on it is unsound. Positional, like scope-near-miss:
    only the token immediately after an EXACT `unit U<k> ` prefix is
    examined."""

    VARIANTS = [
        "unit U2 writeset: tools/x.py",       # missing hyphen
        "unit U2 Write-set: tools/x.py",      # wrong case
        "unit U2 write-set tools/x.py",       # missing colon
        "unit U2 write-set :  tools/x.py",    # extra spacing
    ]

    def test_every_variant_lints_write_set_near_miss(self):
        for body_text in self.VARIANTS:
            v = self.lint(
                f"- F9 [VERIFIED] {body_text} — basis: e\n")
            self.assertEqual(v["verdict"], "LINT_VIOLATIONS",
                             f"{body_text!r} stayed clean")
            self.assertIn("write-set-near-miss", self.violation_codes(v),
                          f"{body_text!r}: {v}")

    def test_correct_write_set_line_stays_clean(self):
        # the discriminating pair: the exact literal never near-misses
        v = self.lint(
            "- F9 [VERIFIED] unit U2 write-set: tools/x.py — basis: e\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN")

    def test_near_miss_blocks_closure(self):
        v = self.closure(
            CLOSED +
            "- F9 [VERIFIED] unit U2 writeset: tools/x.py — basis: e\n",
            unit="U2")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("write-set-near-miss", self.violation_codes(v))


class TestAttack10ClauseGrammar(RecordFixture):
    """attack-10 N9: four clause dispositions on one [INVALIDATED]
    line, in mixed spellings. One parsed with a stray `;` glued to its
    value and one VANISHED without a trace — a clause disposition the
    aggregation never saw and no violation ever named."""

    LINE = ("- F5 [INVALIDATED] clause a restated-at-D7; clause b dead "
            "(killed by F9); clause c restated at D8; clause d dead "
            "— basis: F6\n")

    def test_no_clause_token_vanishes_silently(self):
        # P5: post-mint header — this test grades the detection
        # mechanics, not the age gate
        v = self.sweep(self.LINE, header=HEADER_POST_CLAUSE_UNPARSED_MINT)
        self.assertEqual(v["verdict"], "SWEEP_HOLDS")
        agg = v["clause_dispositions"].get("F5", {})
        self.assertIn("clause-unparsed", self.violation_codes(v),
                      f"clause c neither parsed nor named: {agg}")
        unparsed = [x for x in v["violations"]
                    if x["code"] == "clause-unparsed"]
        self.assertTrue(any("clause c" in x["text"] for x in unparsed),
                        unparsed)

    def test_parsed_dispositions_carry_clean_values(self):
        v = self.sweep(self.LINE)
        agg = v["clause_dispositions"]["F5"]
        self.assertEqual(agg["a"], "restated-at-D7")
        self.assertEqual(agg["b"], "dead (killed by F9)")
        self.assertEqual(agg["d"], "dead")
        for clause, disp in agg.items():
            self.assertNotIn(";", disp, f"clause {clause} kept a separator")

    def test_wellformed_clause_line_does_not_lint_unparsed(self):
        # the boundary: the aggregation's own regression case
        v = self.sweep("- F5 [INVALIDATED] clause 1 dead (killed by X); "
                       "clause 2 restated-at-F8 — basis: F6\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        self.assertEqual(v["clause_dispositions"]["F5"]["2"],
                         "restated-at-F8")


class TestEMRepairFormGating(RecordFixture):
    """BACKLOG E-M, widened (dev-notes/OBSERVATIONS.md 271a6bf): a
    hold's printed repair string gates on resolver reachability.
    apply_supersession's `violated` map is built once, at LINT stage,
    from parse_tracker's own scan — a code computed later
    (clause-unparsed, SWEEP stage) or synthesized by
    apply_supersession itself on the CORRECTING line
    (corrects-nothing, multi-corrects-token, and by the same
    reasoning repair-tag-change/repair-scope-change) can never be a
    member of it. The desk pasting the printed `corrects line <n>`
    token verbatim (as the tools section directs) minted a second,
    permanent hold on a live tracker — every one of these codes must
    print a repair string carrying no RESOLVABLE token."""

    def test_sweep_stage_hold_repair_carries_no_resolvable_token(self):
        line = ("- F5 [INVALIDATED] clause a restated-at-D7; clause b "
                "dead (killed by F9); clause c restated at D8; clause d "
                "dead — basis: F6\n")
        # P5: post-mint header — this test grades the repair-text
        # mechanics, not the age gate
        v = self.sweep(line, header=HEADER_POST_CLAUSE_UNPARSED_MINT)
        unparsed = [x for x in v["violations"]
                    if x["code"] == "clause-unparsed"]
        self.assertTrue(unparsed)
        for x in unparsed:
            self.assertNotRegex(x["repair"], r"corrects line \d")

    def test_corrects_nothing_repair_carries_no_resolvable_token(self):
        body = ("- F1 [VERIFIED] a fact — basis: y\n"
                "- F2 [VERIFIED] record: corrects line 9 — basis: y\n")
        v = self.sweep(body)
        hits = [x for x in v["violations"] if x["code"] == "corrects-nothing"]
        self.assertTrue(hits)
        for x in hits:
            self.assertNotRegex(x["repair"], r"corrects line \d")

    def test_multi_corrects_token_repair_carries_no_resolvable_token(self):
        body = ("- F1 [VERIFIED] a fact — basis: y\n"
                "- F2 [VERIFIED] record: corrects line 9 and corrects "
                "line 10 — basis: y\n")
        v = self.sweep(body)
        hits = [x for x in v["violations"]
                if x["code"] == "multi-corrects-token"]
        self.assertTrue(hits)
        for x in hits:
            self.assertNotRegex(x["repair"], r"corrects line \d")

    def test_following_the_printed_repair_no_longer_mints_a_second_hold(self):
        # the empirical regression case: before the fix, appending the
        # verdict's own printed repair for a corrects-nothing violation
        # minted a SECOND permanent corrects-nothing hold (271a6bf's
        # shape). After the fix the desk is told this line is not a
        # legal target at all, so nothing invites that append.
        body = ("- F1 [VERIFIED] a fact — basis: y\n"
                "- F2 [VERIFIED] record: corrects line 9 — basis: y\n")
        v = self.sweep(body)
        hits = [x for x in v["violations"] if x["code"] == "corrects-nothing"]
        self.assertTrue(hits)
        self.assertIn("never itself a corrects target", hits[0]["repair"])


class TestP15SweepExemptRoute(RecordFixture):
    """BACKLOG P15: the printed repair for `clause-unparsed` and
    `killerless-dead` previously prescribed an in-place edit that
    mints a NEW violation of the same class and clears nothing on
    settled-prose form debt — measured twice live (parent run F147;
    successor run's F29 dry-run in a scratch copy: eight holds
    before, eight after). The sanctioned route for these two codes
    is a SWEEP_EXEMPT declaration on operator grant (the 0.2.79 ask
    machinery); the repair text names it and prescribes no edit."""

    def test_clause_unparsed_repair_names_sweep_exempt_and_no_edit(self):
        body = ("- F5 [INVALIDATED] clause a restated-at-D7; clause b "
                "dead (killed by F9); clause c restated at D8 — "
                "basis: F6\n")
        # P5: post-mint header — this test grades the repair-text
        # mechanics, not the age gate
        v = self.sweep(body, header=HEADER_POST_CLAUSE_UNPARSED_MINT)
        hits = [x for x in v["violations"] if x["code"] == "clause-unparsed"]
        self.assertTrue(hits)
        for x in hits:
            self.assertIn("SWEEP_EXEMPT", x["repair"])
            self.assertNotIn("restate a clean clause disposition",
                             x["repair"])
            self.assertNotRegex(x["repair"], r"corrects line \d")

    def test_killerless_dead_repair_names_sweep_exempt_and_no_edit(self):
        body = "- F2 [INVALIDATED] clause a dead — basis: F2\n"
        v = self.sweep(body)
        hits = [x for x in v["violations"] if x["code"] == "killerless-dead"]
        self.assertTrue(hits)
        for x in hits:
            self.assertIn("SWEEP_EXEMPT", x["repair"])
            self.assertNotIn("append a new tag-first line", x["repair"])
            self.assertNotRegex(x["repair"], r"corrects line \d")

    def test_pending_latest_and_basis_cites_invalidated_unchanged(self):
        # the sibling codes sharing REPAIR_STATUS_LINE keep the
        # append-a-new-line form — only clause-unparsed and
        # killerless-dead move to the exemption route
        v = self.sweep("- F1 [PENDING] awaiting leg — basis: dispatched\n")
        hits = [x for x in v["violations"] if x["code"] == "pending-latest"]
        self.assertTrue(hits)
        for x in hits:
            self.assertIn("append a new tag-first line", x["repair"])


class TestENCorrectsTokenOutOfBody(RecordFixture):
    """BACKLOG E-N (F205, relay 5, beat-the-books desk): a `corrects
    line <n>` token placed in an entry's BASIS clause is invisible to
    apply_supersession, which scans only `e.body` — the repair looked
    landed and repaired nothing, a silent no-op, the worst shape. New
    lint class `corrects-token-out-of-body` fires on the entry whose
    basis clause carries the token, instead of staying silent."""

    def test_token_in_basis_clause_lints_loudly(self):
        body = "- F2 [VERIFIED] the fix — basis: corrects line 1\n"
        v = self.lint(body)
        self.assertEqual(v["verdict"], "LINT_VIOLATIONS", v)
        self.assertIn("corrects-token-out-of-body", self.violation_codes(v))

    def test_token_in_basis_clause_is_silent_under_the_resolver(self):
        # the F205 shape itself: the misplaced token resolves nothing —
        # apply_supersession's own scan of e.body never sees it, so no
        # corrects-nothing/multi-corrects-token complaint fires either;
        # only the new lint class names the defect.
        body = "- F2 [VERIFIED] the fix — basis: corrects line 1\n"
        v = self.lint(body)
        codes = self.violation_codes(v)
        self.assertNotIn("corrects-nothing", codes)
        self.assertNotIn("multi-corrects-token", codes)

    def test_legitimate_body_token_is_not_flagged(self):
        # the positive control: a correctly-placed token, in the BODY,
        # resolving a real target's violation — never mistaken for the
        # basis-clause defect.
        body = "- F1 [VERIFIED] a fact\n"          # no "— basis:": basis-missing
        n = self.lineno_of(body, "F1 [VERIFIED]")
        body += f"- F1 [VERIFIED] record: corrects line {n} — basis: fixed\n"
        v = self.lint(body)
        self.assertNotIn("corrects-token-out-of-body", self.violation_codes(v))

    def test_repair_carries_no_resolvable_token(self):
        # E-M's reachability assertion (widened by this class): the
        # printed repair for corrects-token-out-of-body must carry no
        # token apply_supersession could act on — the very mechanism
        # the defect defeats is not the one prescribed to fix it.
        body = "- F2 [VERIFIED] the fix — basis: corrects line 1\n"
        v = self.lint(body)
        hits = [x for x in v["violations"]
                if x["code"] == "corrects-token-out-of-body"]
        self.assertTrue(hits)
        for x in hits:
            self.assertNotRegex(x["repair"], r"corrects line \d")


class TestAttack10SymlinkedAncestor(RecordFixture):
    """attack-10 N4: the tracker's containment compared a TEXTUAL path
    against the repo top's REALPATH, so a tracker reached through a
    symlinked ANCESTOR of the top halted PATH_OUTSIDE_REPO — a repo
    the run can pin perfectly well. Only the ancestor rebases; the
    tracker itself is still taken AS NAMED."""

    def linked(self):
        """(real_top, link_top) for a repo under a symlinked ancestor."""
        base = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, base, True)
        (base / "real" / "inner").mkdir(parents=True)
        os.symlink(str(base / "real"), str(base / "link"))
        real = base / "real" / "inner"
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=real,
                       env={**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null"},
                       capture_output=True, check=True)
        return real, base / "link" / "inner"

    def test_lint_clean_from_both_spellings_and_both_cwds(self):
        real, link = self.linked()
        (real / "t.md").write_text(HEADER + "- F1 [VERIFIED] x — basis: y\n")
        for cwd in (real, link):
            for tracker in (real / "t.md", link / "t.md"):
                v = self.verdict(tool(["lint", "--tracker", str(tracker)],
                                      cwd=str(cwd)))
                self.assertEqual(v["verdict"], "LINT_CLEAN",
                                 f"cwd={cwd} tracker={tracker}")

    def test_tracker_outside_every_repo_still_halts(self):
        # the rebase must not turn the containment gate off
        base = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, base, True)
        t = base / "t.md"
        t.write_text(HEADER + "- F1 [VERIFIED] x — basis: y\n")
        v = self.verdict(tool(["lint", "--tracker", str(t)],
                              cwd=str(self.dir)))
        self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO")


class TestAttack10NonUtf8RepoDir(RecordFixture):
    """attack-10 N5: the tracker's toplevel read was `text=True`, so a
    repo whose DIRECTORY NAME carries a non-UTF-8 byte answered
    INTERNAL_ERROR (UnicodeDecodeError) from every gate."""

    def bad_repo(self):
        base = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, base, True)
        d = base / os.fsdecode(b"repo-\xff")
        d.mkdir()
        env = {**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null",
               "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        (d / "t.md").write_text(HEADER + CLOSED)
        for a in (["init", "-q", "-b", "main"], ["add", "t.md"],
                  ["commit", "-m", "lock"]):
            subprocess.run(["git", *a], cwd=d, env=env,
                           capture_output=True, check=True)
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=d, env=env,
                             capture_output=True, text=True,
                             check=True).stdout.strip()
        return d, sha

    def test_every_subcommand_works_in_a_non_utf8_repo_dir(self):
        d, sha = self.bad_repo()
        t = str(d / "t.md")
        out = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, out, True)
        for args, expected, stdin in (
                (["lint", "--tracker", t], "LINT_CLEAN", None),
                (["sweep", "--tracker", t], "SWEEP_CLEAN", None),
                (["closure", "--tracker", t], "CLOSURE_LIVE", None),
                (["filter", "--tracker", t, "--sha", sha,
                  "--out", str(out / "a.md")], "ARTIFACT_WRITTEN", None),
                (["quote", "--label", "A1 quotes"], "QUOTE_BLOCK", "x\n")):
            v = self.verdict(tool(args, cwd=str(d), stdin_text=stdin))
            self.assertEqual(v["verdict"], expected, f"{args[0]} -> {v}")


class TestAttack10TrackerBytePolicy(RecordFixture):
    """attack-10 N6: a tracker carrying one non-UTF-8 byte died on the
    strict `open()` (INTERNAL_ERROR from every gate), and the filter's
    utf-8/replace read SUBSTITUTED the byte in the artifact — the
    attacker would have graded text the record does not contain. The
    tracker is bytes: read and written surrogateescape, so preserved
    lines come out byte-identical."""

    BAD_LINE = b"- F1 [VERIFIED] caf\xe9 \xe2\x80\x94 basis: y\n"

    def write_bytes_tracker(self):
        p = self.dir / "t.md"
        p.write_bytes(HEADER.encode() + self.BAD_LINE + CLOSED.encode())
        return p

    def test_gates_read_a_non_utf8_tracker(self):
        t = str(self.write_bytes_tracker())
        for sub, expected in (("lint", "LINT_CLEAN"),
                              ("sweep", "SWEEP_CLEAN"),
                              ("closure", "CLOSURE_LIVE")):
            v = self.verdict(tool([sub, "--tracker", t], cwd=str(self.dir)))
            self.assertEqual(v["verdict"], expected, f"{sub} -> {v}")

    def test_filter_artifact_preserves_the_byte_exactly(self):
        self.write_bytes_tracker()
        env = {**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null",
               "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        for a in (["add", "t.md"], ["commit", "-m", "lock"]):
            subprocess.run(["git", *a], cwd=self.dir, env=env,
                           capture_output=True, check=True)
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.dir,
                             env=env, capture_output=True, text=True,
                             check=True).stdout.strip()
        outdir = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, outdir, True)
        out = outdir / "a.md"
        v = self.verdict(tool(["filter", "--tracker", "t.md", "--sha", sha,
                               "--out", str(out)], cwd=str(self.dir)))
        self.assertEqual(v["verdict"], "ARTIFACT_WRITTEN")
        self.assertIn(self.BAD_LINE.rstrip(b"\n"), out.read_bytes(),
                      "the artifact substituted the tracker's own byte")


class TestAttack10FilterAndTrackerRouting(RecordFixture):
    """attack-10 N10/NIT2/NIT3: the filter served a symlinked tracker's
    LINK STRING as a one-line artifact (a round run over it would close
    a design sight-unseen), a tracker under a missing directory died as
    a tool defect, and a `## Superseded —` section swallowed everything
    after a SUBHEADING to the next `## `."""

    def committed_repo(self, committed_text, also=()):
        env = {**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null",
               "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        (self.dir / "t.md").write_text(committed_text)
        for a in (["add", "t.md", *also], ["commit", "-m", "lock"]):
            subprocess.run(["git", *a], cwd=self.dir, env=env,
                           capture_output=True, check=True)
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.dir,
                              env=env, capture_output=True, text=True,
                              check=True).stdout.strip()

    def outdir(self):
        d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d, True)
        return d

    def test_filter_halts_on_a_symlinked_tracker(self):
        # SKILL.md (The attack): "a tracker path that is itself a
        # symlink halts USAGE_ERROR — name the real path: the link's
        # git history is the link string"
        # the link is TRACKED: `git show <sha>:link.md` then serves the
        # link STRING, and the artifact is a one-line file the attacker
        # would grade as the whole record
        os.symlink("t.md", self.dir / "link.md")
        sha = self.committed_repo(HEADER + "- F1 [VERIFIED] kept — basis: y\n",
                                  also=["link.md"])
        out = self.outdir() / "a.md"
        p = tool(["filter", "--tracker", "link.md", "--sha", sha,
                  "--out", str(out)], cwd=str(self.dir))
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertEqual(p.returncode, 3)
        self.assertFalse(out.exists(), "halt must precede the write")
        self.assertIn("real path", v["error"])

    def test_missing_tracker_directory_is_unreadable(self):
        t = str(self.dir / "no-such-dir" / "t.md")
        other = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, other, True)
        for cwd in (str(self.dir), str(other)):
            for sub in ("lint", "sweep", "closure"):
                p = tool([sub, "--tracker", t], cwd=cwd)
                v = self.verdict(p)
                self.assertEqual(v["verdict"], "TRACKER_UNREADABLE",
                                 f"{sub} from cwd {cwd} -> {v}")
                self.assertEqual(p.returncode, 2)

    def test_superseded_section_ends_at_any_heading_level(self):
        committed = (HEADER +
                     "## Superseded — legacy section\n"
                     "old landing prose\n"
                     "### Cycle 4 — the re-entry\n"
                     "surviving prose after the subheading\n"
                     "R5. a derived requirement line\n"
                     "## Cycle 5\n"
                     "- F4 [VERIFIED] after — basis: y\n")
        sha = self.committed_repo(committed)
        out = self.outdir() / "a.md"
        v = self.verdict(tool(["filter", "--tracker", "t.md", "--sha", sha,
                               "--out", str(out)], cwd=str(self.dir)))
        self.assertEqual(v["verdict"], "ARTIFACT_WRITTEN")
        text = out.read_text()
        self.assertIn("surviving prose after the subheading", text)
        self.assertIn("R5. a derived requirement line", text)
        self.assertIn("### Cycle 4", text)
        # the section's own lines still drop
        self.assertNotIn("old landing prose", text)
        self.assertNotIn("legacy section", text)
        self.assertEqual(v["sections_blanked"], 1)


class TestCorrectedLineSupersession(RecordFixture):
    """0.2.44's settled GAP-1 contract (SKILL.md, Implementation): a
    line named by a later same-id entry's `corrects line <n>` token is
    SUPERSEDED WHOLE — "every gate excludes it, its entry, where it
    parsed, and its violations both, and the correcting line carries
    the content". Supersession reaches only lines that CARRY a
    violation: a token naming a clean line lints `corrects-nothing` —
    "the token is a repair, never an eraser of live entries"."""

    def corrected(self, bad, fixed_body, needle):
        """bad + a later same-id line correcting it by line number."""
        n = self.lineno_of(CLOSED + bad, needle)
        return CLOSED + bad + fixed_body.format(n=n)

    # -- the violations leave with the entry ---------------------------

    def test_corrected_tag_enum_line_stops_holding_the_sweep(self):
        # the sweep-forever case: the corrected line's OWN violation
        # held the record out of [READY] for the run's whole life,
        # with no append able to clear it
        body = self.corrected(
            "- D2 [COMMITED] unit U1 the letter lands — basis: probe\n",
            "- D2 [COMMITTED] unit U1 the letter lands (corrects line "
            "{n}) — basis: probe\n",
            "[COMMITED]")
        self.assertEqual(self.sweep(body)["verdict"], "SWEEP_CLEAN")
        self.assertEqual(self.lint(body)["verdict"], "LINT_CLEAN")

    def test_corrected_line_leaves_the_entry_set(self):
        # the entry half: the superseded line is not the latest line
        # for its id, does not travel as an amendment, and cannot
        # classify as anything
        body = (self.corrected(
            "- D5 [COMMITTED] Record: bookkeeping — basis: probe\n",
            "- D5 [COMMITTED] record: bookkeeping (corrects line {n}) "
            "— basis: probe\n",
            "Record:") +
            # E-B: U1 must be a KNOWN unit for closure --unit U1 to
            # read; [INVALIDATED] keeps this line out of amendments
            "- D0 [INVALIDATED] unit U1 established (never "
            "dispatched) — basis: design\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")
        self.assertEqual(v["amendments"], [],
                         "a record-scoped line travelled as an amendment")

    def test_superseded_hold_no_longer_holds_its_unit(self):
        # holds inherit the exclusion too (the gate list in the brief)
        body = self.corrected(
            "- D9 [AUTO-ACCEPTED] unit U2 HELD: x.txt — basis: F9\n",
            "- D9 [COMMITTED] unit U2 operator cleared x.txt (corrects "
            "line {n}) — basis: reply\n",
            "HELD:")
        self.assertEqual(self.closure(body, unit="U2")["verdict"],
                         "UNIT_DISPATCHABLE")

    # -- the violation precondition ------------------------------------

    def test_token_naming_a_clean_live_entry_erases_nothing(self):
        # the abuse the precondition exists for: a premise-kill is a
        # CLEAN line, and a repair token must not be able to delete it
        kill = "- D1 [INVALIDATED] the premise died — basis: F9\n"
        n = self.lineno_of(CLOSED + kill, "the premise died")
        body = (CLOSED + kill +
                f"- D1 [COMMITTED] unit U1 never mind (corrects line "
                f"{n}) — basis: y\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_VOID",
                         "a repair token erased a live premise-kill")
        self.assertIn("corrects-nothing",
                      self.violation_codes(self.lint(body)))

    def test_token_naming_its_own_line_lints(self):
        body = CLOSED + ("- D5 [COMMITTED] record: a note (corrects line "
                         f"{self.lineno_of(CLOSED + 'x', 'x')}) "
                         "— basis: y\n")
        self.assertIn("corrects-nothing", self.violation_codes(self.lint(body)))

    def test_token_naming_a_later_line_lints(self):
        body = CLOSED + ("- D5 [COMMITTED] record: a note (corrects line "
                         "999) — basis: y\n")
        v = self.lint(body)
        self.assertEqual(v["verdict"], "LINT_VIOLATIONS")
        self.assertIn("corrects-nothing", self.violation_codes(v))

    def test_token_naming_another_ids_line_lints_and_supersedes_nothing(self):
        # same-id is the contract's own word; a cross-id token repairs
        # nothing and must say so rather than sitting silent
        bad = "- D2 [COMMITED] unit U1 the letter lands — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "[COMMITED]")
        body = (CLOSED + bad +
                f"- F7 [VERIFIED] record: unrelated (corrects line {n}) "
                f"— basis: y\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("corrects-nothing", self.violation_codes(self.lint(body)))

    def test_token_is_matched_by_number_not_by_substring(self):
        # `"corrects line 12" in "…corrects line 123…"` is TRUE — the
        # 0.2.43 substring disarm cleared a violation at line 12 on a
        # token that named line 123 and nothing else
        bad = "- D2 [COMMITED] unit U1 the letter lands — basis: probe\n"
        self.assertEqual(self.lineno_of(CLOSED + bad, "[COMMITED]"), 12)
        body = (CLOSED + bad +
                "- D2 [COMMITTED] unit U1 the letter lands (corrects "
                "line 123) — basis: probe\n")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED",
                         "a token naming line 123 disarmed line 12")


# ================================================================= 0.2.49
# The executable spec's own battery (docs/directives/
# executable-spec-settle.md). Each case names its seed: R3-B1…B7 are
# design-attack round 3's blockers, R1-B<n> round 1's, ES-<n> the
# settle item itself. Cases marked GREEN-AT-BASE are regression pins,
# not part of the red-first list — the settled semantics already held
# there and the pin keeps them from being repaired away.


class PinnedFixture(RecordFixture):
    """A fixture whose tracker is COMMITTED, for the filter's pinned
    reads, plus an out-directory outside every repo."""

    def committed_repo(self, text, also=()):
        env = {**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null",
               "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        (self.dir / "t.md").write_text(text)
        for a in (["add", "t.md", *also], ["commit", "-m", "lock"]):
            subprocess.run(["git", *a], cwd=self.dir, env=env,
                           capture_output=True, check=True)
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.dir,
                              env=env, capture_output=True, text=True,
                              check=True).stdout.strip()

    def outdir(self):
        d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d, True)
        return d


# ----------------------------------------------- begehung-harvest 2 (a)-(c)

BOGUS_STATUS_HEADER = """# Run: test
Status: bogus-status
Phase: investigate-design
Skill: statiker 0.2.33

INTENT — do the thing.

## Cycle 1
"""


class TestHarvest2CorrectsReachClass(RecordFixture):
    """begehung-harvest 2, finding 2 (tier2-without.md parts 3/7-4/7,
    probe A): `apply_supersession` decided shed/supersede by LINE
    NUMBER alone, never consulting the violation's own REPAIR_FORMS
    class — a `corrects line <n>` token cleared a header's
    status-enum violation with the header itself never rewritten.
    Repair: `repair_class()` gates the shed on the declared form —
    only REPAIR_BOOKKEEPING codes shed, only MACHINE_TOKEN_CODES
    members supersede, everything else lints `corrects-nothing`
    carrying the declared (unreachable) form.

    Probe B (an undefanged tag literal in INTENT, corrected by a
    bookkeeping token) is fixed by a FOLLOW-UP decision (dispatcher,
    the GAP-2 directive): `tag-literal-in-body` — this code only, no
    general owner rule — is shed-eligible only when the target line
    parsed an entry (`line_ids` carries an owner for it); an
    owner-less target (header, INTENT, bare prose) routes
    `corrects-nothing` and the verdict's own repair field states the
    hold (SKILL.md's "holds ... for the run's life ... hand-defang
    duty") instead of recommending the shed. An ENTRY-owned
    tag-literal still sheds normally (must-not-fire, tested below) —
    ordinary near-miss repairs on owner-less malformed lines outside
    this one code stay reachable (TestES6OwnIdTargeting's own vehicle
    moved off tag-literal-in-body to superseded-block-form for this
    reason)."""

    def test_a_header_violation_is_not_shed_by_a_bookkeeping_token(self):
        n = self.lineno_of("", "bogus-status", header=BOGUS_STATUS_HEADER)
        body = f"- F1 [VERIFIED] record: corrects line {n} — basis: D1\n"
        v = self.sweep(body, header=BOGUS_STATUS_HEADER)
        self.assertEqual(v["verdict"], "SWEEP_HOLDS", v)
        codes = self.violation_codes(v)
        self.assertIn("status-enum", codes, v)
        self.assertIn("corrects-nothing", codes, v)
        header_viol = next(x for x in v["violations"]
                           if x["code"] == "status-enum")
        self.assertTrue(header_viol["repair"].startswith("header rewrite:"),
                        header_viol)

    def test_lint_reaches_the_same_header_result(self):
        n = self.lineno_of("", "bogus-status", header=BOGUS_STATUS_HEADER)
        body = f"- F1 [VERIFIED] record: corrects line {n} — basis: D1\n"
        v = self.lint(body, header=BOGUS_STATUS_HEADER)
        self.assertEqual(v["verdict"], "LINT_VIOLATIONS", v)
        self.assertIn("status-enum", self.violation_codes(v))

    def test_sweep_code_immunity_is_ordering_independent(self):
        # AMENDED 2026-08-15 boundary note (arm part 4/7): a
        # `pending-latest` line is structurally unreachable now (it
        # is not a REPAIR_BOOKKEEPING member) rather than immune only
        # because sweep_checks happens to run after apply_supersession
        # — pinned as a test rather than left an accepted ordering
        # accident. A cross-id token targeting F1's [PENDING] line
        # fails reachability (owner mismatch) AND the sweep-level
        # violation still stands: both hold together.
        f1 = "- F1 [PENDING] awaiting a leg — basis: dispatched\n"
        n = self.lineno_of(f1, "[PENDING] awaiting a leg")
        body = f1 + f"- F2 [VERIFIED] record: corrects line {n} — basis: y\n"
        v = self.sweep(body)
        self.assertEqual(v["verdict"], "SWEEP_HOLDS", v)
        codes = self.violation_codes(v)
        self.assertIn("pending-latest", codes, v)
        self.assertIn("corrects-nothing", codes, v)

    def test_an_intent_tag_literal_is_not_shed_by_a_bookkeeping_token(self):
        # GAP-2 (dispatcher-decided follow-up), probe B: appending
        # exactly what the ORIGINAL (pre-fix) verdict's repair field
        # recommended used to reach SWEEP_CLEAN with [PASSED] still
        # standing in INTENT — the recommendation itself was the bug
        # (tier2-without.md part 4/7, "the tool recommends the shed")
        header = HEADER.replace(
            "INTENT — do the thing.",
            "INTENT — make the thing [PASSED] when it works.")
        n = self.lineno_of("", "[PASSED] when it works", header=header)
        baseline = self.sweep("", header=header)
        self.assertEqual(baseline["verdict"], "SWEEP_HOLDS", baseline)
        literal_viol = next(x for x in baseline["violations"]
                            if x["code"] == "tag-literal-in-body")
        self.assertTrue(literal_viol["repair"].startswith("hold:"),
                        literal_viol)
        self.assertNotIn("bookkeeping", literal_viol["repair"], literal_viol)
        body = f"- F1 [VERIFIED] record: corrects line {n} — basis: y\n"
        v = self.sweep(body, header=header)
        self.assertEqual(v["verdict"], "SWEEP_HOLDS", v)
        codes = self.violation_codes(v)
        self.assertIn("tag-literal-in-body", codes, v)
        self.assertIn("corrects-nothing", codes, v)

    def test_an_entry_owned_tag_literal_still_sheds(self):
        # must-not-fire: an ordinary entry-body tag literal, corrected
        # by its OWN id, stays reachable — the carve-out is owner-less
        # targets only, not tag-literal-in-body generally
        bad = "- F1 [VERIFIED] the [PENDING] tag rides here — basis: y\n"
        n = self.lineno_of(bad, "[PENDING] tag rides here")
        body = (bad + f"- F1 [VERIFIED] record: corrects line {n} "
                "— basis: y2\n")
        v = self.sweep(body)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN", v)


class TestHarvest2WriteSetPathField(RecordFixture):
    """begehung-harvest 2, finding 3 (tier2-without.md part 5/7): the
    write-set PATH FIELD got no positional lint, so a two-path line
    (`unit U2 write-set: a.py b.py`) read as one exotic filename that
    could intersect nothing, and an absolute spelling (`/abs/...`)
    read as a residue rather than a defect — both certified
    parallel-eligible by `waves`. Repair mirrors the existing
    write-set-near-miss declarator lint (c2c5baf), applied to the
    path field: whitespace inside it or a leading `/` lints
    `write-set-path-near-miss` and blocks waves/closure like any
    other CLOSURE_BLOCKING_CODES member. An INVALIDATED line is
    exempt (disposal commentary, e.g. `dead (mis-scoped)`, is not a
    second declared path — TestWaves.
    test_invalidated_write_set_path_dropped_leaves_unit_unplannable
    pins that the INVALIDATED case stays WAVES_COMPUTED)."""

    FOUR_UNIT_BODY = (
        "- F1 [VERIFIED] unit U1 write-set: src/app.py — basis: y\n"
        "- F2 [VERIFIED] unit U2 write-set: src/app.py src/util.py "
        "— basis: y\n"
        "- F3 [VERIFIED] unit U3 write-set: ./src/app.py — basis: y\n"
        "- F4 [VERIFIED] unit U4 write-set: /abs/repo/src/app.py "
        "— basis: y\n")

    def test_two_paths_on_one_line_lints(self):
        v = self.lint(self.FOUR_UNIT_BODY)
        self.assertEqual(v["verdict"], "LINT_VIOLATIONS", v)
        codes = {viol["code"]: viol for viol in v["violations"]}
        self.assertIn("write-set-path-near-miss", codes, v)
        u2_line = self.lineno_of(self.FOUR_UNIT_BODY, "src/util.py")
        self.assertEqual(
            {viol["line"] for viol in v["violations"]
             if viol["code"] == "write-set-path-near-miss"},
            {u2_line, self.lineno_of(self.FOUR_UNIT_BODY, "/abs/repo")})

    def test_normalized_dot_slash_stays_clean(self):
        # U1/U3 collapse to the same normalized key and lint nothing —
        # the fix must not touch the case that already works
        v = self.lint("- F1 [VERIFIED] unit U1 write-set: src/app.py "
                      "— basis: y\n"
                      "- F3 [VERIFIED] unit U3 write-set: ./src/app.py "
                      "— basis: y\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN", v)

    def test_waves_halts_instead_of_certifying_colliding_units_parallel(self):
        v = self.waves(self.FOUR_UNIT_BODY)
        self.assertEqual(v["verdict"], "WAVES_RECORD_MALFORMED", v)

    def test_absolute_spelling_alone_lints(self):
        # the three-arm cross-confirmed class (dev-notes/
        # triage-three-arm-2026-08-15.md T4: WITH-B3 / WITHOUT-F10 /
        # SENTENCE-A4) merged into this defect — an absolute write-set
        # path, on its own (no colliding second unit), must lint too
        body = ("- F1 [VERIFIED] unit U1 write-set: /abs/repo/a.py "
                "— basis: y\n")
        v = self.lint(body)
        self.assertEqual(v["verdict"], "LINT_VIOLATIONS", v)
        self.assertIn("write-set-path-near-miss", self.violation_codes(v))

    def test_invalidated_disposal_commentary_stays_exempt(self):
        # the existing TestWaves fixture's own shape, re-pinned at the
        # lint level: trailing prose after a dead write-set path is
        # not a second path
        body = ("- F2 [VERIFIED] unit U2 write-set: src/a.py "
                "— basis: design\n"
                "- F2 [INVALIDATED] unit U2 write-set: src/a.py dead "
                "(mis-scoped) — basis: F9\n")
        v = self.lint(body)
        self.assertEqual(v["verdict"], "LINT_CLEAN", v)


class TestHarvest2TrendWindow(RecordFixture):
    """begehung-harvest 2, finding 4 (tier2-without.md part 6/7): a
    VOID round's span was annexed by the round that follows it (prev
    only advanced at resolved A-lines), and bucket 1 always started
    at line 0, folding cycle-1's pre-attack investigation F-lines
    into the first round's count. Repair: every round's window opens
    at its OWN id's first [DISPATCHED] line rather than the previous
    round's resolution — VOID needs no special case (it is simply
    absent from the resolved-round list and opens no window), and the
    same anchor gives round 1 its own start."""

    ROUND_BODY = (
        "- A1 [DISPATCHED] attacker one — basis: brief\n"
        "- F1 [VERIFIED] finding one — basis: x\n"
        "- F2 [VERIFIED] finding two — basis: x\n"
        "- A1 [BIT] two findings — basis: report\n"
        "- A2 [DISPATCHED] attacker two — basis: brief\n"
        "- A2 [VOID] premise: wrong sha pinned — basis: desk\n"
        "- F3 [VERIFIED] desk re-derived one — basis: desk\n"
        "- F4 [VERIFIED] desk re-derived two — basis: desk\n"
        "- F5 [VERIFIED] desk re-derived three — basis: desk\n"
        "- A3 [DISPATCHED] attacker three — basis: brief\n"
        "- F6 [VERIFIED] finding three — basis: x\n"
        "- A3 [ZERO-DELTA] one finding — basis: report\n")

    def test_a_void_rounds_findings_are_not_annexed_by_its_successor(self):
        # probe 1: true attacker yield 2 -> 1, never 2 -> 4
        v = self.trend(self.ROUND_BODY)
        self.assertEqual(v["verdict"], "TREND_COMPUTED", v)
        self.assertEqual(v["rounds"], 2, v)
        self.assertEqual(v["counts"], [2, 1], v)
        self.assertEqual(v["trajectory"], "IMPROVING", v)

    def test_pre_attack_investigation_lines_never_inflate_round_one(self):
        # probe 2: the same true series survives 3 pre-attack F-lines
        # ahead of A1's own dispatch
        body = ("- F7 [VERIFIED] pre-attack investigation one — basis: x\n"
                "- F8 [VERIFIED] pre-attack investigation two — basis: x\n"
                "- F9 [VERIFIED] pre-attack investigation three "
                "— basis: x\n" + self.ROUND_BODY)
        v = self.trend(body)
        self.assertEqual(v["verdict"], "TREND_COMPUTED", v)
        self.assertEqual(v["counts"], [2, 1], v)
        self.assertEqual(v["trajectory"], "IMPROVING", v)


class TestHarvest2BrokenPipeVerdict(RecordFixture):
    """begehung-harvest 2, finding 5 (tier2-without.md part 7/7): a
    closed reader (`| head -1`) broke the one-verdict-line guarantee
    — the catch-all's own re-entry into finish()/emit() died on the
    same broken pipe, exit 0, no verdict line at all. Repair: emit()
    swallows a BrokenPipeError on an evidence line and remembers it;
    finish() falls back to a stderr-safe write and a defined exit
    code (3, USAGE_ERROR-class per SKILL.md's own 0/2/3 contract) —
    and redirects stdout to devnull first, since CPython's own
    interpreter-finalization flush hits the SAME broken pipe and
    would otherwise override the exit code with its hardcoded 120."""

    def test_a_closed_reader_still_gets_exactly_one_verdict_line(self):
        p = self.write_tracker(TestHarvest2WriteSetPathField.FOUR_UNIT_BODY)
        proc = subprocess.Popen(
            [sys.executable, str(SCRIPT), "waves", "--tracker", str(p)],
            cwd=self.dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.stdout.close()   # closed before any read: guarantees EPIPE
        err = proc.stderr.read()
        proc.wait(timeout=10)
        self.assertEqual(proc.returncode, 3, err)
        lines = [l for l in err.decode("utf-8", "surrogateescape")
                .split("\n") if l.startswith(VERDICT_PREFIX)]
        self.assertEqual(len(lines), 1, err)
        self.assertIn('"verdict": "WAVES_RECORD_MALFORMED"', lines[0])


# ------------------------------------------------------------------- ES-1

HEAD_WITH_OPERATOR_BULLET = """# Run: test
Status: in-progress
Phase: investigate-design
Skill: statiker 0.2.49

INTENT — do the thing.
- V2 an operator bullet inside the head
1. F9 INVALIDATED a numbered head item
R1. a derived requirement

## Cycle 1
"""

# the defang boundary needs a BRACKETED literal, which ES-1 leaves
# firing everywhere — so it gets its own header
HEAD_WITH_UNDEFANGED_LITERAL = HEAD_WITH_OPERATOR_BULLET.replace(
    "- V2 an operator bullet inside the head",
    "- V2 the report came back [COMMITTED]")


class TestES1HeadRegionExclusion(RecordFixture):
    """ES-1 (R3-B3): the requirement-head region — file start to the
    first `## ` heading — parses NO entries: not the exact head, not
    the near-miss scan, not the signature scan. An operator bullet
    cannot brick the closure gate or mint a phantom entry."""

    def test_head_region_bullet_parses_no_entry_and_lints_nothing(self):
        # the settle's own red case: `- V2 …` in the head region — old
        # code parses a V-entry and lints tag-enum (plus basis-missing)
        v = self.lint("- F1 [VERIFIED] a fact — basis: y\n",
                      header=HEAD_WITH_OPERATOR_BULLET)
        self.assertEqual(v["verdict"], "LINT_CLEAN", v.get("violations"))

    def test_head_region_bullet_cannot_brick_the_closure(self):
        # E-B: U1 must be a KNOWN unit for closure --unit U1 to read
        # at all
        body = (CLOSED + "- D0 [INVALIDATED] unit U1 established "
                "(never dispatched) — basis: design\n")
        v = self.closure(body, unit="U1",
                         header=HEAD_WITH_OPERATOR_BULLET)
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")

    def test_head_region_entry_is_not_in_the_entry_set(self):
        # the phantom-entry half: the head bullet must not become the
        # latest line for V2, nor travel anywhere
        v = self.sweep("- F1 [VERIFIED] a fact — basis: y\n",
                       header=HEAD_WITH_OPERATOR_BULLET)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN", v.get("violations"))

    def test_quoted_lines_never_register_as_entries(self):
        # GREEN-AT-BASE (R1-B2 guard): the widened signature scan must
        # not reach into report quotes — a defanged block quoting an
        # entry line is not an entry
        v = self.lint("> Superseded — A3 quotes\n"
                      "> - D1 [COMMITTED] the report restated it\n"
                      "> F9 [INVALIDATED] and an unbulleted one\n")
        self.assertNotIn("entry-near-miss", self.violation_codes(v))

    def test_header_and_defang_lint_still_read_the_head_region(self):
        # the boundary ES-1 names untouched: Status/Phase parsing and
        # the whole-file defang lint are not excluded — an undefanged
        # literal in INTENT is the enforcement of the hand-defang duty
        bad = HEAD_WITH_UNDEFANGED_LITERAL.replace("Status: in-progress",
                                                   "Status: ready")
        v = self.lint("- F1 [VERIFIED] a fact — basis: y\n", header=bad)
        codes = self.violation_codes(v)
        self.assertIn("status-enum", codes)
        self.assertIn("tag-literal-in-body", codes,
                      "the head bullet's [COMMITTED] escaped defang lint")


# ------------------------------------------------------------------- ES-2

class TestES2LateIntent(RecordFixture):
    """ES-2 (R3-B2): a mid-run operator instruction lands at the
    record's END labeled `INTENT: `. The verdict LISTS those lines —
    the tool, not memory, is what verify's composition grades against."""

    def test_sweep_verdict_lists_the_late_intent_line(self):
        body = ("- F1 [VERIFIED] a fact — basis: y\n"
                "INTENT: also make it fast\n")
        v = self.sweep(body)
        self.assertEqual(v["late_intent"],
                         [self.lineno_of(body, "INTENT: also")])

    def test_closure_verdict_lists_the_late_intent_line(self):
        body = CLOSED + "INTENT: also make it fast\n"
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")
        self.assertEqual(v["late_intent"],
                         [self.lineno_of(body, "INTENT: also")])

    def test_head_intent_is_not_a_late_intent(self):
        v = self.sweep("- F1 [VERIFIED] a fact — basis: y\n")
        self.assertEqual(v["late_intent"], [])

    def test_case_and_colon_slips_lint_as_near_miss(self):
        for slip in ("intent: also make it fast",
                     "Intent — also make it fast",
                     "INTENT also make it fast"):
            v = self.lint("- F1 [VERIFIED] a fact — basis: y\n"
                          + slip + "\n")
            self.assertIn("intent-near-miss", self.violation_codes(v),
                          f"{slip!r} registered as prose")

    def test_intent_prose_words_are_not_intent_lines(self):
        # GREEN-AT-BASE guard: the detection is a LEADING-token read
        v = self.lint("- F1 [VERIFIED] a fact — basis: y\n"
                      "intentional drift is the thing the head catches\n"
                      "the operator's intent: unchanged\n")
        self.assertNotIn("intent-near-miss", self.violation_codes(v))


# ------------------------------------------------------------------- ES-3

SUPERSEDED_SOURCE = (HEADER +
                     "- F1 [VERIFIED] kept entry — basis: y\n"
                     "> Superseded — A2 quotes\n"
                     "> quoted finding text\n"
                     ">\n"
                     "> more quote\n"
                     "## Superseded — legacy section\n"
                     "old landing prose\n"
                     "- F2 [VERIFIED] entry inside the section — basis: y\n"
                     "more legacy prose\n"
                     "## Cycle 2\n"
                     "- F3 [VERIFIED] the corrects target — basis: y\n"
                     "- F3 [VERIFIED] restated — basis: y\n")


class TestES3FilterBlanksInPlace(PinnedFixture):
    """ES-3 (R3-B1, supersedes the 0.2.46 header definition): the
    filter BLANKS the two Superseded species in place and emits NO
    header, so artifact line numbers EQUAL source line numbers by
    construction — a `corrects line <n>` token dereferences to the
    same text in either. The blanking metadata travels in the
    ARTIFACT_WRITTEN verdict fields instead."""

    def filtered(self):
        sha = self.committed_repo(SUPERSEDED_SOURCE)
        out = self.outdir() / "a.md"
        v = self.verdict(tool(["filter", "--tracker", "t.md", "--sha", sha,
                               "--out", str(out)], cwd=str(self.dir)))
        self.assertEqual(v["verdict"], "ARTIFACT_WRITTEN")
        return v, out.read_text()

    def test_every_surviving_line_keeps_its_source_line_number(self):
        # the red case the settle names: a token below a blanked block
        # must dereference to the same text in artifact and source
        v, text = self.filtered()
        src = SUPERSEDED_SOURCE.split("\n")
        art = text.split("\n")
        self.assertEqual(len(art), len(src), "the artifact changed length")
        for i, (s, a) in enumerate(zip(src, art), 1):
            self.assertIn(a, (s, ""),
                          f"line {i}: artifact {a!r} is neither the "
                          f"source line {s!r} nor a blank")
        n = next(i for i, l in enumerate(src, 1) if "corrects target" in l)
        self.assertEqual(art[n - 1], src[n - 1])

    def test_the_two_species_become_empty_lines(self):
        v, text = self.filtered()
        art = text.split("\n")
        src = SUPERSEDED_SOURCE.split("\n")
        for needle in ("> Superseded — A2 quotes", "quoted finding text",
                       "more quote", "## Superseded — legacy section",
                       "old landing prose", "more legacy prose"):
            i = next(i for i, l in enumerate(src, 1) if needle in l)
            self.assertEqual(art[i - 1], "",
                             f"{needle!r} was not blanked in place")

    def test_entries_inside_a_section_keep_their_own_line_numbers(self):
        v, text = self.filtered()
        art = text.split("\n")
        src = SUPERSEDED_SOURCE.split("\n")
        i = next(i for i, l in enumerate(src, 1)
                 if "entry inside the section" in l)
        self.assertEqual(art[i - 1], src[i - 1])

    def test_the_artifact_opens_with_the_source_own_first_line(self):
        # ES-3 kills the 0.2.46 header: no tool-emitted line at all
        v, text = self.filtered()
        self.assertEqual(text.split("\n")[0],
                         SUPERSEDED_SOURCE.split("\n")[0])

    def test_the_verdict_carries_the_blanking_metadata(self):
        v, text = self.filtered()
        self.assertEqual(v["source_tracker"], "t.md")
        self.assertEqual(v["blocks_blanked"], 1)
        self.assertEqual(v["sections_blanked"], 1)
        self.assertEqual(v["lines_blanked"], 7)
        self.assertEqual(v["lines_out"], v["lines_in"])
        self.assertIn("blank", v["form"].lower())


# --------------------------------------------------------------------- E-I

class TestEIPinned(PinnedFixture):
    """begehung-harvest triage T16 (SENTENCE-B1): an in-place status
    rewrite (`[PENDING]` edited to `[VERIFIED]` on its OWN line,
    never a new appended line) reads SWEEP_CLEAN — every positional
    gate reads the edited file as a clean record — while `git diff
    --stat <pin>` shows the edit as 1+/1-. `pinned` is the one check
    that cannot be fooled: the pinned version's bytes must be a
    PREFIX of the working tracker's, at the BYTE level (ES-9)."""

    def pinned(self, sha, tracker="t.md"):
        return self.verdict(tool(
            ["pinned", "--tracker", tracker, "--sha", sha], cwd=self.dir))

    def test_byte_identical_tracker_reads_append_only(self):
        sha = self.committed_repo(
            HEADER + "- F1 [PENDING] awaiting leg — basis: dispatched\n")
        self.assertEqual(self.pinned(sha)["verdict"], "PINNED_APPEND_ONLY")

    def test_genuine_append_reads_append_only(self):
        sha = self.committed_repo(
            HEADER + "- F1 [PENDING] awaiting leg — basis: dispatched\n")
        with (self.dir / "t.md").open("a") as f:
            f.write("- F1 [VERIFIED] leg returned clean — basis: report\n")
        self.assertEqual(self.pinned(sha)["verdict"], "PINNED_APPEND_ONLY")

    def test_in_place_status_rewrite_reads_rewritten(self):
        # B1's own red case: SWEEP_CLEAN over an edited file that
        # `git diff --stat` shows as 1+/1- — the one check `pinned`
        # exists to catch
        bad = "- F1 [PENDING] awaiting leg — basis: dispatched\n"
        n = self.lineno_of(bad, "[PENDING]")
        sha = self.committed_repo(HEADER + bad)
        (self.dir / "t.md").write_text(
            HEADER + "- F1 [VERIFIED] awaiting leg — basis: dispatched\n")
        v = self.pinned(sha)
        self.assertEqual(v["verdict"], "PINNED_REWRITTEN")
        self.assertEqual(v["first_divergent_line"], n)

    def test_a_stale_sha_is_pin_unreadable(self):
        self.committed_repo(HEADER + "- F1 [VERIFIED] x — basis: y\n")
        self.assertEqual(self.pinned("deadbeef")["verdict"], "PIN_UNREADABLE")

    # Release review 2026-08-15 B1: the whole-file byte prefix fired
    # on the header mutation SKILL.md itself mandates (Status/Phase
    # are the record's one mutable surface), and the header
    # divergence MASKED a real tag rewrite further down. The four
    # cases below pin the repaired predicate from both directions.

    def test_the_mandated_header_flip_reads_append_only(self):
        # red-first against the whole-file prefix: this read
        # PINNED_REWRITTEN with first_divergent_line 2 before the
        # exemption landed
        sha = self.committed_repo(
            HEADER + "- F1 [PENDING] awaiting leg — basis: dispatched\n")
        text = (self.dir / "t.md").read_text()
        text = text.replace("Status: in-progress", "Status: [READY]")
        text = text.replace("Phase: investigate-design",
                            "Phase: implement")
        (self.dir / "t.md").write_text(text)
        self.assertEqual(self.pinned(sha)["verdict"], "PINNED_APPEND_ONLY")

    def test_a_header_flip_does_not_mask_a_tag_rewrite(self):
        # red-first: before the exemption, this reported the Status
        # line as the divergence while the real rewrite sat below —
        # the promised evidence pointed at a non-defect
        bad = "- F1 [PENDING] awaiting leg — basis: dispatched\n"
        n = self.lineno_of(bad, "[PENDING]")
        sha = self.committed_repo(HEADER + bad)
        text = (self.dir / "t.md").read_text()
        text = text.replace("Status: in-progress", "Status: [READY]")
        text = text.replace("[PENDING]", "[VERIFIED]")
        (self.dir / "t.md").write_text(text)
        v = self.pinned(sha)
        self.assertEqual(v["verdict"], "PINNED_REWRITTEN")
        self.assertEqual(v["first_divergent_line"], n)
        self.assertNotIn("Status", v["evidence"])

    def test_a_nonmutable_header_line_rewrite_stays_rewritten(self):
        # the exemption is exactly two field lines — the Skill: line
        # is header but NOT mutable surface
        sha = self.committed_repo(
            HEADER + "- F1 [PENDING] awaiting leg — basis: dispatched\n")
        text = (self.dir / "t.md").read_text()
        (self.dir / "t.md").write_text(
            text.replace("Skill: statiker 0.2.33", "Skill: statiker 9.9.9"))
        self.assertEqual(self.pinned(sha)["verdict"], "PINNED_REWRITTEN")

    def test_the_mutable_field_leaving_its_line_reads_rewritten(self):
        # the exemption binds the field's PRESENCE at its position:
        # a Status: line replaced by arbitrary text is a rewrite,
        # not a permitted value change
        sha = self.committed_repo(
            HEADER + "- F1 [PENDING] awaiting leg — basis: dispatched\n")
        text = (self.dir / "t.md").read_text()
        (self.dir / "t.md").write_text(
            text.replace("Status: in-progress", "no field here anymore"))
        v = self.pinned(sha)
        self.assertEqual(v["verdict"], "PINNED_REWRITTEN")
        self.assertIn("left its line", v["evidence"])


# -------------------------------------------------------------- P30 (verify)

class TestP30VerifyGate(PinnedFixture):
    """BACKLOG P30 (incident F121/F124, run-2 close): the desk is an
    unfrozen concurrent writer during a verify leg — nothing caught it
    committing INTO the same copy the leg was isolated-reading (F121's
    deviation replaced the unit transaction's collision check with the
    condition "this desk is the only writer in this copy", then broke
    exactly that). `verify-gate` is the repo-HEAD sibling of `pinned`'s
    tracker-text check: it compares the copy's current HEAD against a
    read-start sha the desk recorded at verify-leg dispatch."""

    def verify_gate(self, sha):
        return self.verdict(tool(
            ["verify-gate", "--tracker", str(self.dir / "t.md"), "--sha", sha],
            cwd=self.dir))

    def test_unmoved_head_is_clean(self):
        sha = self.committed_repo(HEADER)
        v = self.verify_gate(sha)
        self.assertEqual(v["verdict"], "VERIFY_COPY_CLEAN", v)
        self.assertEqual(v["read_sha"], sha)
        self.assertEqual(v["head_sha"], sha)

    def test_commit_landing_during_the_leg_grades_stale(self):
        # the F121 shape: the desk commits into the copy while the
        # isolated verify leg is reading it
        sha = self.committed_repo(HEADER)
        env = {**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null",
               "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        (self.dir / "booking.txt").write_text("a mid-leg desk booking\n")
        for a in (["add", "booking.txt"], ["commit", "-m", "mid-leg booking"]):
            subprocess.run(["git", *a], cwd=self.dir, env=env,
                           capture_output=True, check=True)
        v = self.verify_gate(sha)
        self.assertEqual(v["verdict"], "VERIFY_COPY_STALE", v)
        self.assertEqual(v["read_sha"], sha)
        self.assertNotEqual(v["head_sha"], sha)
        self.assertEqual(len(v["commits"]), 1)
        self.assertIn("mid-leg booking", v["commits"][0]["subject"])
        self.assertIn("booking.txt", v["touched_paths"])

    def test_unresolvable_sha_is_a_git_error(self):
        self.committed_repo(HEADER)
        v = self.verify_gate("0" * 40)
        self.assertEqual(v["verdict"], "GIT_ERROR", v)


# ------------------------------------------------------------------- ES-4

class TestES4RepairPinsTagAndScope(RecordFixture):
    """ES-4 (R3-B4): a supersede-whole restatement carries the
    target's tag where the tag parsed AND the target's scope class
    where the scope opener parsed. A scope change through repair lints
    `repair-scope-change`, exactly as a tag change lints
    `repair-tag-change`: status and scope changes are ordinary new
    lines, never smuggled through a repair."""

    def test_scope_change_through_repair_lints(self):
        # the violated token is the TAG, so the scope opener parsed —
        # and the restatement moves `record:` bookkeeping to a unit
        bad = "- D5 [COMMITED] record: bookkeeping — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "[COMMITED]")
        body = (CLOSED + bad +
                f"- D5 [COMMITTED] unit U1 bookkeeping (corrects line "
                f"{n}) — basis: probe\n")
        self.assertIn("repair-scope-change",
                      self.violation_codes(self.lint(body)))

    def test_tag_change_through_repair_lints(self):
        # the violated token is the OPENER, so the tag parsed
        bad = "- D5 [COMMITTED] Record: bookkeeping — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "Record:")
        body = (CLOSED + bad +
                f"- D5 [INVALIDATED] record: bookkeeping (corrects line "
                f"{n}) — basis: probe\n")
        self.assertIn("repair-tag-change",
                      self.violation_codes(self.lint(body)))

    def test_faithful_restatement_lints_neither(self):
        bad = "- D5 [COMMITTED] Record: bookkeeping — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "Record:")
        body = (CLOSED + bad +
                f"- D5 [COMMITTED] record: bookkeeping (corrects line "
                f"{n}) — basis: probe\n")
        v = self.lint(body)
        self.assertEqual(v["verdict"], "LINT_CLEAN", v.get("violations"))

    def test_tag_is_free_where_the_violated_token_is_the_tag(self):
        # GREEN-AT-BASE boundary: the misspelled-tag repair is the
        # token's own reason for existing — pinning there would brick it
        bad = "- D2 [COMMITED] unit U1 the letter lands — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "[COMMITED]")
        body = (CLOSED + bad +
                f"- D2 [COMMITTED] unit U1 the letter lands (corrects "
                f"line {n}) — basis: probe\n")
        self.assertNotIn("repair-tag-change",
                         self.violation_codes(self.lint(body)))

    def test_scope_is_free_where_the_violated_token_is_the_opener(self):
        # GREEN-AT-BASE boundary: scope unparseable → the restatement's
        # scope is free by construction (ES-4's own sentence)
        bad = "- D5 [COMMITTED] Record: bookkeeping — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "Record:")
        body = (CLOSED + bad +
                f"- D5 [COMMITTED] unit U1 bookkeeping (corrects line "
                f"{n}) — basis: probe\n")
        self.assertNotIn("repair-scope-change",
                         self.violation_codes(self.lint(body)))

    def test_a_meant_void_restated_scoped_still_voids_and_lints(self):
        # ES-4's named danger direction, pinned explicitly: converting
        # a void into a dispatch is held by the closure rule (a
        # post-closure [INVALIDATED] line for an entry live at the
        # closure voids WHATEVER its opener), and the scope change
        # still lints
        bad = "- D1 [INVALIDATE] the premise died — basis: F9\n"
        n = self.lineno_of(CLOSED + bad, "[INVALIDATE]")
        body = (CLOSED + bad +
                f"- D1 [INVALIDATED] unit U1 the premise died (corrects "
                f"line {n}) — basis: F9\n")
        self.assertEqual(self.closure(body, unit="U1")["verdict"],
                         "CLOSURE_VOID")
        self.assertIn("repair-scope-change",
                      self.violation_codes(self.lint(body)))


# ------------------------------------------------------------------- ES-5

class TestES5ChainSemantics(RecordFixture):
    """ES-5 (R3-B5): supersession is one pass over the ORIGINAL entry
    set, so a token acts whether or not its carrying line is later
    superseded. The restatement of a superseded correcting line
    therefore carries exactly ONE token — the 0.2.48 re-carry clause
    is dead — and a multi-token line lints as its own violation."""

    def chain(self):
        """10 ← 20 ← 30: a violated line, its correcting line (itself
        violated), and the restatement of THAT."""
        bad1 = "- D2 [COMMITED] unit U1 the letter lands — basis: probe\n"
        n1 = self.lineno_of(CLOSED + bad1, "[COMMITED]")
        bad2 = (f"- D2 [COMMITTED] Unit U1 the letter lands (corrects "
                f"line {n1}) — basis: probe\n")
        n2 = self.lineno_of(CLOSED + bad1 + bad2, "Unit U1")
        return CLOSED + bad1 + bad2, n1, n2

    def test_one_pass_chain_needs_no_re_carry(self):
        # GREEN-AT-BASE (ES-5's own red case, already held by the
        # one-pass mechanism): line 10 stays superseded although the
        # line that superseded it is itself superseded, and the last
        # line carries ONE token
        head, n1, n2 = self.chain()
        body = (head +
                f"- D2 [COMMITTED] unit U1 the letter lands (corrects "
                f"line {n2}) — basis: probe\n")
        v = self.lint(body)
        self.assertEqual(v["verdict"], "LINT_CLEAN", v.get("violations"))
        self.assertEqual(self.closure(body, unit="U1")["verdict"],
                         "UNIT_DISPATCHABLE")

    def test_a_re_carried_second_token_lints(self):
        # the 0.2.48 re-carry clause, now a violation: one token per line
        head, n1, n2 = self.chain()
        body = (head +
                f"- D2 [COMMITTED] unit U1 the letter lands (corrects "
                f"line {n2}) (corrects line {n1}) — basis: probe\n")
        self.assertIn("multi-corrects-token",
                      self.violation_codes(self.lint(body)))

    def test_leading_zero_token_numbers_compare_as_integers(self):
        # GREEN-AT-BASE regression pin (ES-6's NIT2 half; probe at
        # base: `corrects line 011` already reached line 11)
        bad = "- D2 [COMMITED] unit U1 the letter lands — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "[COMMITED]")
        body = (CLOSED + bad +
                f"- D2 [COMMITTED] unit U1 the letter lands (corrects "
                f"line {n:03d}) — basis: probe\n")
        self.assertEqual(self.closure(body, unit="U1")["verdict"],
                         "UNIT_DISPATCHABLE")


# ------------------------------------------------------------------- ES-6

class TestES6OwnIdTargeting(RecordFixture):
    """ES-6 (R3-B6): the token reaches an earlier violated line naming
    the correcting line's OWN id, and an earlier violated line naming
    NO readable id — the id-misspelling class the token was built for;
    the correcting line's id claims it. A violated line readably
    naming a DIFFERENT id stays barred (the forgery direction)."""

    def test_token_reaches_a_line_naming_no_readable_id(self):
        # a stray quoted line outside any recognized Superseded block
        # carries a violation and no id at all — the vehicle here is
        # superseded-block-form, not tag-literal-in-body: the latter
        # is now OWNER-CONDITIONED (begehung-harvest 2, probe B —
        # TestHarvest2CorrectsReachClass) and no longer demonstrates
        # this class; every OTHER body-content code stays reachable
        # regardless of owner, which is what this test pins
        quoted = "> a stray quoted line outside any Superseded block\n"
        n = self.lineno_of(quoted, "stray quoted line")
        body = (quoted +
                f"- F7 [VERIFIED] record: corrects line {n} — basis: y\n")
        v = self.lint(body)
        self.assertEqual(v["verdict"], "LINT_CLEAN", v.get("violations"))

    def test_cross_id_target_stays_barred(self):
        # GREEN-AT-BASE boundary (the forgery direction ES-6 keeps):
        # a violated line READABLY naming another id is not claimable
        bad = "- D2 [COMMITED] unit U1 the letter lands — basis: probe\n"
        n = self.lineno_of(CLOSED + bad, "[COMMITED]")
        body = (CLOSED + bad +
                f"- F7 [VERIFIED] record: unrelated (corrects line {n}) "
                f"— basis: y\n")
        v = self.lint(body)
        self.assertIn("corrects-nothing", self.violation_codes(v))
        reason = next(x["text"] for x in v["violations"]
                      if x["code"] == "corrects-nothing")
        self.assertIn("D2", reason)

    def test_body_content_violation_sheds_and_the_target_keeps_its_entry(self):
        # the SITE split (ES-10's two forms): a body-content violation
        # leaves gate-read semantics sound, so the target keeps its
        # live entry and the correcting line is bookkeeping — it sheds
        # violations only, status untouched. At base the whole entry
        # was superseded, and the [PENDING] status vanished with it.
        bad = ("- F1 [PENDING] awaiting the leg, the report said "
               "[AUTO-ACCEPTED] — basis: dispatched\n")
        n = self.lineno_of(bad, "[PENDING] awaiting")
        body = (bad +
                f"- F1 [VERIFIED] record: corrects line {n} — basis: y\n")
        v = self.sweep(body)
        self.assertEqual(v["verdict"], "SWEEP_HOLDS")
        codes = self.violation_codes(v)
        self.assertNotIn("tag-literal-in-body", codes,
                         "the bookkeeping line shed nothing")
        self.assertIn("pending-latest", codes,
                      "the bookkeeping line changed the entry's status")


# ------------------------------------------------------------------- ES-7

class TestES7Containment(PinnedFixture):
    """ES-7 (R3-B7): must-be-inside containment is decided on the REAL
    path — walk to the path's nearest EXISTING ancestor; the path is
    inside only when that ancestor's realpath sits inside (or equals)
    the repo top's realpath. As-named stays the operating spelling,
    `resolved_from` noted whenever the two differ. Must-be-outside
    paths are outside only when BOTH computations agree."""

    def test_tracker_resolving_outside_its_repo_halts(self):
        # REVERSES the attack-9 as-named containment this settle
        # replaces: a tracker named inside the repo whose real path
        # sits outside can never be pinned there
        outside = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, outside, True)
        (outside / "real.md").write_text(
            HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        os.symlink(str(outside / "real.md"), self.dir / "linked.md")
        v = self.verdict(tool(["lint", "--tracker",
                               str(self.dir / "linked.md")],
                              cwd=str(self.dir)))
        self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO")
        self.assertIn("resolved_from", v)
        self.assertIn(str(outside / "real.md"), v["resolved_from"]["real"])

    def test_rel_none_with_a_top_present_states_the_true_cause(self):
        # the 0.2.44 one-cause comment ("rel is None exactly when top
        # is") is DISPROVEN: this tracker sits in a repo and still
        # resolves out, and the message must not blame a missing repo
        outside = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, outside, True)
        (outside / "real.md").write_text(HEADER)
        os.symlink(str(outside / "real.md"), self.dir / "linked.md")
        v = self.verdict(tool(["lint", "--tracker",
                               str(self.dir / "linked.md")],
                              cwd=str(self.dir)))
        self.assertNotIn("no git repository", v["error"])
        self.assertIn("resolves outside", v["error"])

    def test_symlinked_ancestor_of_the_top_still_resolves_inside(self):
        # GREEN-AT-BASE boundary (attack-10 N4, preserved): the
        # ancestor probe must not re-break the link-spelled repo top
        base = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, base, True)
        (base / "real" / "inner").mkdir(parents=True)
        os.symlink(str(base / "real"), str(base / "link"))
        real = base / "real" / "inner"
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=real,
                       env={**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null"},
                       capture_output=True, check=True)
        (real / "t.md").write_text(HEADER + "- F1 [VERIFIED] x — basis: y\n")
        v = self.verdict(tool(["lint", "--tracker",
                               str(base / "link" / "inner" / "t.md")],
                              cwd=str(real)))
        self.assertEqual(v["verdict"], "LINT_CLEAN")

    def test_out_named_inside_a_repo_halts_even_when_it_resolves_out(self):
        # the must-be-outside direction: outside only when BOTH
        # computations agree. At base only the REAL side is checked,
        # so an --out spelled through an in-repo link landed under a
        # brief asserting tree == lock commit.
        sha = self.committed_repo(HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        target = self.outdir()
        os.symlink(str(target), self.dir / "linkout")
        p = tool(["filter", "--tracker", "t.md", "--sha", sha,
                  "--out", str(self.dir / "linkout" / "a.md")],
                 cwd=str(self.dir))
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "ARTIFACT_IN_REPO")
        self.assertFalse((target / "a.md").exists(),
                         "halt must precede the write")

    def test_out_naming_an_existing_directory_is_a_usage_error(self):
        # ES-11: IsADirectoryError routes USAGE_ERROR, consistent with
        # its missing-parent sibling — at base it died INTERNAL_ERROR
        sha = self.committed_repo(HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        p = tool(["filter", "--tracker", "t.md", "--sha", sha,
                  "--out", str(self.outdir())], cwd=str(self.dir))
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertEqual(p.returncode, 3)


# ------------------------------------------------------------------- ES-8

class TestES8PositionalLintSurfaces(RecordFixture):
    """ES-8 (0.2.48 definitions; R1-B1/R1-B2 and R2's stem-match seeds
    as negative cases): the signature scan replaces the opener
    enumeration (an enumerated set is open — `1)` and bullet-less
    id-openers escaped it), and hold classification is POSITIONAL —
    the word-search died in both its directions."""

    def kill(self, prefix):
        return f"{prefix} [INVALIDATED] the premise died — basis: probe\n"

    def test_bulletless_id_opener_lints_and_blocks(self):
        # R1-B2 / R3's open-set finding: no bullet at all
        body = CLOSED + self.kill("F9")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("entry-near-miss", self.violation_codes(v))

    def test_paren_enumerator_opener_lints_and_blocks(self):
        body = CLOSED + self.kill("1) F9")
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("entry-near-miss", self.violation_codes(v))

    def test_bare_enum_word_is_an_adjacent_tag_literal(self):
        body = CLOSED + "F9 INVALIDATED the premise died — basis: probe\n"
        v = self.closure(body, unit="U1")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("entry-near-miss", self.violation_codes(v))

    def test_prose_bullets_without_an_adjacent_tag_stay_legal(self):
        # GREEN-AT-BASE boundary the signature scan must not eat
        v = self.lint("- D1 [COMMITTED] x — basis: y\n"
                      "\n"
                      "  unit U1 landed: abc1234\n"
                      "\n"
                      "* an ordinary prose bullet\n"
                      "1. a numbered prose item\n"
                      "R5. a derived requirement line\n"
                      "- see the F-lines above for the basis\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN", v.get("violations"))

    def test_displaced_hold_colon_form_lints(self):
        # R2-N2's under-fire half: a `hold:` slip passed the word
        # search entirely and travelled as an ordinary amendment
        body = (CLOSED + "- D9 [AUTO-ACCEPTED] unit U2 gap: the operator "
                         "hold: approval — basis: F9\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("hold-form", self.violation_codes(v))

    def test_hold_colon_form_opening_any_body_lints(self):
        body = (CLOSED +
                "- D9 [AUTO-ACCEPTED] held: x.txt — basis: F9\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("hold-form", self.violation_codes(v))

    def test_backtick_quoted_hold_literal_is_exempt(self):
        # R2-N3's over-fire half, in its sharpest form: quoting the
        # literal is legal, and the word search barred the unit for it
        body = (CLOSED + "- D9 [AUTO-ACCEPTED] unit U2 the form is "
                         "`unit U2 held: ` — basis: F9\n")
        v = self.closure(body, unit="U2")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")

    def test_positional_hold_variants_still_lint(self):
        # GREEN-AT-BASE control the positional read must not lose
        for tail in ("HELD: x.txt", "held — x.txt", "holds: x.txt",
                     "Hold: x.txt"):
            body = (CLOSED +
                    f"- D9 [AUTO-ACCEPTED] unit U2 {tail} — basis: F9\n")
            v = self.closure(body, unit="U2")
            self.assertEqual(v["verdict"], "CLOSURE_RECORD_MALFORMED", tail)
            self.assertIn("hold-form", self.violation_codes(v))

    def test_stem_match_negatives_stay_prose(self):
        # GREEN-AT-BASE (R2's booked stem-match seeds): the bare
        # colon-less word away from the hold position, `withheld:`,
        # and the opener stems in ordinary prose
        v = self.lint("- D9 [AUTO-ACCEPTED] unit U2 gap: the operator "
                      "withheld: approval — basis: F9\n"
                      "- D8 [COMMITTED] the answer was held back — "
                      "basis: y\n"
                      "- D7 [COMMITTED] record the verdict verbatim — "
                      "basis: y\n"
                      "- D6 [COMMITTED] unit tests pass — basis: y\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN", v.get("violations"))


# ------------------------------------------------------------------- ES-9

class TestES9ByteLevelEmit(RecordFixture):
    """ES-9 (0.2.46 N6; R1-B5; R2-B6's refuted probe settled the
    mechanism): verdict lines and quote output emit at the BYTE level,
    surrogateescape over the input's own bytes — a tool that re-spells
    a byte on output mints the second spelling the input rule exists
    to prevent."""

    BAD = b"\xff"

    def test_a_violation_text_carries_the_tracker_byte_verbatim(self):
        p = self.dir / "t.md"
        p.write_bytes(HEADER.encode() +
                      b"- F1 (VERIFIED) malformed caf" + self.BAD +
                      " — basis: y\n".encode())
        r = tool_bytes(["lint", "--tracker", str(p)], cwd=str(self.dir))
        self.assertIn(b"STATIKER-RECORD VERDICT:", r.stdout)
        self.assertIn(self.BAD, r.stdout,
                      "the verdict line re-spelled the tracker's own byte")

    def test_a_quote_block_round_trips_the_byte(self):
        r = tool_bytes(["quote", "--label", "A7 quotes"],
                       stdin_bytes=b"the report said caf" + self.BAD + b"\n")
        self.assertIn(self.BAD, r.stdout,
                      "quote mangled the byte before it reached the block")

    def quote(self, text):
        """(verdict, block lines) for one quote invocation, read at the
        byte level and split on NEWLINES ONLY — str.splitlines() breaks
        on the very characters the cases below are about, so a reader
        using it would itself see the fabricated lines they detect."""
        r = tool_bytes(["quote", "--label", "A7 quotes"],
                       stdin_bytes=text.encode())
        out = r.stdout.decode("utf-8", "surrogateescape")
        lines = out.split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        heads = [l for l in lines if l.startswith(VERDICT_PREFIX)]
        self.assertEqual(len(heads), 1, f"stdout:\n{out}")
        return (json.loads(heads[0][len(VERDICT_PREFIX):]),
                [l for l in lines if not l.startswith(VERDICT_PREFIX)])

    def test_a_line_separator_quotes_as_one_line_and_survives(self):
        # U+2028 is a break to str.splitlines() and to nothing else:
        # quoting on it emits two body lines the report never held and
        # drops the character on the way, so the block the desk pastes
        # is text the report does not contain
        v, block = self.quote("alpha\u2028beta\n")
        self.assertEqual(block[1:], ["> alpha\u2028beta"], block)
        self.assertEqual(v["lines"], 2, v)
        self.assertIn("\u2028", v["block"])

    def test_a_form_feed_quotes_as_one_line_and_survives(self):
        v, block = self.quote("alpha\x0cbeta\n")
        self.assertEqual(block[1:], ["> alpha\x0cbeta"], block)
        self.assertEqual(v["lines"], 2, v)

    def test_the_fixture_reader_survives_a_separator_in_the_block(self):
        # the suite's own verdict reader is a CONSUMER of the record's
        # line rule: a verdict line carries the input's characters
        # verbatim (ensure_ascii=False), so a reader breaking on U+2028
        # severs the JSON it is about to parse — the defect the cases
        # above test for, one level up in the instrument itself
        v = self.verdict(tool(["quote", "--label", "A7 quotes"],
                              stdin_text="alpha\u2028beta\n"))
        self.assertEqual(v["verdict"], "QUOTE_BLOCK")
        self.assertIn("\u2028", v["block"])
        self.assertEqual(v["lines"], 2, v)

    def test_a_tab_is_untouched_by_the_line_rule(self):
        # the control: a tab breaks no line under either rule, so this
        # case reads the same in both worlds — an assertion that moved
        # with the defect would say nothing about the two above
        v, block = self.quote("alpha\tbeta\n")
        self.assertEqual(block[1:], ["> alpha\tbeta"], block)
        self.assertEqual(v["lines"], 2, v)


# ------------------------------------------------------------------ ES-10

class TestES10RepairFieldPerViolation(RecordFixture):
    """ES-10 (0.2.48): every violation names the repair form its SITE
    takes — the desk composes from the verdict, never from memory."""

    def test_a_machine_token_violation_names_supersede_whole(self):
        v = self.lint("- D2 [COMMITED] unit U1 the letter lands — "
                      "basis: probe\n")
        viol = next(x for x in v["violations"] if x["code"] == "tag-enum")
        self.assertTrue(viol["repair"].startswith("supersede-whole:"),
                        viol["repair"])
        self.assertIn(f"corrects line {viol['line']}", viol["repair"])

    def test_a_body_content_violation_names_bookkeeping(self):
        v = self.lint("- F1 [VERIFIED] the [PENDING] tag rides here — "
                      "basis: y\n")
        viol = next(x for x in v["violations"]
                    if x["code"] == "tag-literal-in-body")
        self.assertTrue(viol["repair"].startswith("bookkeeping:"),
                        viol["repair"])
        self.assertIn(f"corrects line {viol['line']}", viol["repair"])

    def test_every_violation_carries_a_repair_field(self):
        body = ("- D2 [COMMITED] unit U1 the letter lands — basis: probe\n"
                "- F1 [VERIFIED] the [PENDING] tag rides here — basis: y\n"
                "- F2 [PENDING] awaiting a leg — basis: dispatched\n"
                "- F3 [INVALIDATED] clause a dead — basis: F9\n"
                "- F4 [VERIFIED] no basis slot at all\n"
                "* D4 [COMMITTED] bullet near-miss — basis: probe\n")
        v = self.sweep(body, header="# Run: t\nStatus: ready\n\n## Cycle 1\n")
        self.assertEqual(v["verdict"], "SWEEP_HOLDS")
        for viol in v["violations"]:
            self.assertIn("repair", viol, viol)
            self.assertTrue(viol["repair"], viol)


# ------------------------------------------------ E-A: verdicts carry reach

class TestEAVerdictReach(RecordFixture):
    """begehung-harvest F1/A1/B2/B3(no)/B6: no verdict of any subcommand
    reported how many entries it parsed, so a gate examining zero
    entries returned exactly what one examining a clean tracker
    returns. `entries`/`head_boundary` now ride every tracker-parsing
    verdict; `r_lines` rides sweep/closure's; lint prints an evidence
    line off the tag contract's own tracker-location convention."""

    NO_HEADING_HEADER = ("# Run: test\n"
                         "Status: in-progress\n"
                         "Phase: investigate-design\n"
                         "Skill: statiker 0.2.33\n\n"
                         "INTENT — do the thing.\n\n")

    HEADING_WITH_ENTRY_ABOVE = ("# Run: test\n"
                                "Status: in-progress\n"
                                "Phase: investigate-design\n"
                                "Skill: statiker 0.2.33\n\n"
                                "INTENT — do the thing.\n\n"
                                "- F1 [PENDING] awaiting a leg — "
                                "basis: dispatched\n\n"
                                "## Cycle 1\n")

    def test_no_heading_at_all_reports_entries_zero_not_bare_clean(self):
        # F1's exact probe: a live [PENDING] entry, no `## ` heading
        # anywhere in the file — the whole file is head region, the
        # entry parses as nothing, and the gate used to return bare
        # SWEEP_CLEAN/LINT_CLEAN indistinguishable from a genuinely
        # clean, fully-examined tracker.
        body = "- F1 [PENDING] awaiting a leg — basis: dispatched\n"
        sv = self.sweep(body, header=self.NO_HEADING_HEADER)
        self.assertEqual(sv["verdict"], "SWEEP_CLEAN")
        self.assertEqual(sv["entries"], 0)
        lv = self.lint(body, header=self.NO_HEADING_HEADER)
        self.assertEqual(lv["verdict"], "LINT_CLEAN")
        self.assertEqual(lv["entries"], 0)
        wv = self.waves(body, header=self.NO_HEADING_HEADER)
        self.assertEqual(wv["verdict"], "WAVES_COMPUTED")
        self.assertEqual(wv["entries"], 0)

    def test_entry_above_the_heading_reports_entries_zero_and_evidence(self):
        # same defect, heading present but the entry sits above it —
        # F1's second byte-identical variant.
        p = tool(["sweep", "--tracker",
                 str(self.write_tracker("", header=self.HEADING_WITH_ENTRY_ABOVE))],
                cwd=self.dir)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        self.assertEqual(v["entries"], 0)
        self.assertIn("entry-shaped line in the head region", p.stdout)
        self.assertIn("F1", p.stdout)

    def test_heading_present_control_unchanged(self):
        # the ordinary case — same entry, BELOW the heading — keeps its
        # existing SWEEP_HOLDS behavior; only the reach fields are new
        v = self.sweep("- F1 [PENDING] awaiting a leg — basis: dispatched\n")
        self.assertEqual(v["verdict"], "SWEEP_HOLDS")
        self.assertEqual(v["entries"], 1)
        self.assertEqual({viol["code"] for viol in v["violations"]},
                         {"pending-latest"})

    def test_head_boundary_names_the_first_heading_line(self):
        v = self.sweep("- F1 [VERIFIED] a fact — basis: cmd output\n")
        boundary = self.lineno_of("", "## Cycle 1")
        self.assertEqual(v["head_boundary"], boundary)

    def test_head_boundary_past_end_of_file_when_no_heading_exists(self):
        body = "prose only, no entries\n"
        v = self.sweep(body, header=self.NO_HEADING_HEADER)
        total_lines = len((self.NO_HEADING_HEADER + body).split("\n")) - 1
        self.assertEqual(v["head_boundary"], total_lines + 1)

    def test_r_lines_counted_on_sweep_and_closure_only(self):
        header = ("# Run: test\n"
                  "Status: in-progress\n"
                  "Phase: investigate-design\n"
                  "Skill: statiker 0.2.33\n\n"
                  "INTENT — do the thing.\n\n"
                  "R1. the first requirement\n"
                  "R2. the second requirement\n"
                  "- an operator bullet, not an R-line\n\n"
                  "## Cycle 1\n")
        body = ("- D1 [COMMITTED] the design — basis: probe\n"
               "- A1 [DISPATCHED] round 1 — basis: brief\n"
               "- A1 [ZERO-DELTA] clean return — basis: report\n")
        sv = self.sweep(body, header=header)
        self.assertEqual(sv["r_lines"], 2)
        cv = self.closure(body, header=header)
        self.assertEqual(cv["r_lines"], 2)
        lv = self.lint(body, header=header)
        self.assertNotIn("r_lines", lv)
        wv = self.waves(body, header=header)
        self.assertNotIn("r_lines", wv)

    def test_dash_led_r_line_does_not_count(self):
        # SKILL.md: numbered `R<n>.`, never dash-led `- R<n>` (the
        # amendment form) — the two must not collapse into one count
        header = ("# Run: test\nStatus: in-progress\n"
                  "Phase: investigate-design\nSkill: statiker 0.2.33\n\n"
                  "INTENT — x.\n\n- R1 dash-led, not a requirement line\n\n"
                  "## Cycle 1\n")
        v = self.sweep("- F1 [VERIFIED] a fact — basis: y\n", header=header)
        self.assertEqual(v["r_lines"], 0)

    def test_lint_flags_a_tracker_path_outside_clippy_runs(self):
        # the RecordFixture tracker (t.md at the repo root) is exactly
        # this case — every existing lint call already exercises it;
        # this test names the evidence line explicitly (B6)
        v = self.lint("- F1 [VERIFIED] a fact — basis: y\n")
        self.assertEqual(v["verdict"], "LINT_CLEAN")
        p = tool(["lint", "--tracker",
                 str(self.write_tracker("- F1 [VERIFIED] a fact — basis: y\n"))],
                cwd=self.dir)
        self.assertIn("tracker path not under .clippy/runs/", p.stdout)

    def test_lint_silent_on_a_tracker_under_clippy_runs(self):
        runs_dir = self.dir / ".clippy" / "runs"
        runs_dir.mkdir(parents=True)
        p = runs_dir / "t.md"
        p.write_text(HEADER + "- F1 [VERIFIED] a fact — basis: y\n")
        result = tool(["lint", "--tracker", str(p)], cwd=self.dir)
        self.assertNotIn("tracker path not under", result.stdout)
        self.assertEqual(self.verdict(result)["verdict"], "LINT_CLEAN")


# ---------------------------- E-L: requirement-head boundary survival

class TestELRequirementHeadBoundary(RecordFixture):
    """E-L (BACKLOG, provenance relay 1 / cycle-12 resume report,
    desk-executed, tool source verified at the meta desk): a
    production tracker's `## Requirement head` heading IS the file's
    first `## ` heading, so the old rule (head region = file start to
    the first `## ` heading) stops the head AT that heading — the
    requirements sitting below it read r_lines: 0 and parse as
    malformed entries. Fixed rule: a first heading whose title is
    `Requirement head` (case-insensitive exact title) does not
    terminate the head region — it extends through to the NEXT `## `
    heading (or EOF); any other first heading keeps the current
    boundary."""

    REQUIREMENT_HEAD_TRACKER = (
        "# Run: test\n"
        "Status: in-progress\n"
        "Phase: investigate-design\n"
        "Skill: statiker 0.2.33\n\n"
        "## Requirement head\n\n"
        "INTENT — do the thing.\n\n"
        "R1. the first requirement\n"
        "R2. the second requirement\n\n"
        "## Cycle 1\n")

    def test_r_lines_survive_a_leading_requirement_head_heading(self):
        body = "- F1 [VERIFIED] a fact — basis: cmd output\n"
        v = self.sweep(body, header=self.REQUIREMENT_HEAD_TRACKER)
        self.assertEqual(v["r_lines"], 2, v)
        boundary = self.lineno_of(body, "## Cycle 1",
                                  header=self.REQUIREMENT_HEAD_TRACKER)
        self.assertEqual(v["head_boundary"], boundary, v)

    def test_closure_r_lines_survive_too(self):
        v = self.closure("- A1 [DISPATCHED] round 1 — basis: brief\n"
                         "- A1 [ZERO-DELTA] clean return — basis: report\n",
                         header=self.REQUIREMENT_HEAD_TRACKER)
        self.assertEqual(v["r_lines"], 2, v)

    def test_case_insensitive_title_match(self):
        header = self.REQUIREMENT_HEAD_TRACKER.replace(
            "## Requirement head", "## REQUIREMENT HEAD")
        v = self.sweep("- F1 [VERIFIED] a fact — basis: cmd output\n",
                       header=header)
        self.assertEqual(v["r_lines"], 2, v)

    def test_any_other_first_heading_keeps_current_boundary(self):
        # control: an ordinary first heading (not "Requirement head")
        # still stops the head region AT the heading — unchanged
        header = ("# Run: test\nStatus: in-progress\n"
                  "Phase: investigate-design\nSkill: statiker 0.2.33\n\n"
                  "## Not A Requirement Head\n\n"
                  "R1. a requirement below an unrelated heading\n\n"
                  "## Cycle 1\n")
        v = self.sweep("- F1 [VERIFIED] a fact — basis: cmd output\n",
                       header=header)
        self.assertEqual(v["r_lines"], 0, v)

    def test_no_further_heading_extends_head_to_eof(self):
        header = ("# Run: test\nStatus: in-progress\n"
                  "Phase: investigate-design\nSkill: statiker 0.2.33\n\n"
                  "## Requirement head\n\n"
                  "R1. the only requirement\n\n")
        body = ""
        v = self.sweep(body, header=header)
        total_lines = len((header + body).split("\n")) - 1
        self.assertEqual(v["r_lines"], 1, v)
        self.assertEqual(v["head_boundary"], total_lines + 1, v)


# --------------------------------------------- E-E: four one-shape fixes

class TestEESmallFixes(RecordFixture):
    """begehung-harvest F11 / WITH-B4 / A5 / C1."""

    def _git(self, *a, cwd=None):
        env = {**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null",
              "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
              "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        return subprocess.run(["git", *a], cwd=cwd or self.dir, env=env,
                              capture_output=True, text=True, check=True)

    # (1) F11: ARTIFACT_WRITTEN carries the tracker's newest commit
    # beside the given sha — a field, never a gate.
    def test_filter_names_the_tracker_newest_commit_beside_a_stale_sha(self):
        self._git("init", "-b", "main")
        p = self.dir / "t.md"
        p.write_text(HEADER + "- F1 [VERIFIED] first lock — basis: y\n")
        self._git("add", "t.md")
        self._git("commit", "-m", "lock 1")
        stale_sha = self._git("rev-parse", "HEAD").stdout.strip()
        p.write_text(HEADER + "- F1 [VERIFIED] first lock — basis: y\n"
                              "- F2 [VERIFIED] second lock — basis: y\n")
        self._git("add", "t.md")
        self._git("commit", "-m", "lock 2")
        newest_sha = self._git("rev-parse", "HEAD").stdout.strip()
        out_tmp = tempfile.TemporaryDirectory()
        self.addCleanup(out_tmp.cleanup)
        out = Path(out_tmp.name) / "artifact.md"
        v = self.verdict(tool(["filter", "--tracker", "t.md", "--sha",
                              stale_sha, "--out", str(out)], cwd=self.dir))
        self.assertEqual(v["verdict"], "ARTIFACT_WRITTEN")
        self.assertEqual(v["sha"], stale_sha)
        self.assertEqual(v["newest_commit"], newest_sha)
        self.assertNotEqual(v["sha"], v["newest_commit"])

    def test_filter_at_the_newest_commit_names_itself(self):
        self._git("init", "-b", "main")
        p = self.dir / "t.md"
        p.write_text(HEADER + "- F1 [VERIFIED] only lock — basis: y\n")
        self._git("add", "t.md")
        self._git("commit", "-m", "lock")
        sha = self._git("rev-parse", "HEAD").stdout.strip()
        out_tmp = tempfile.TemporaryDirectory()
        self.addCleanup(out_tmp.cleanup)
        out = Path(out_tmp.name) / "artifact.md"
        v = self.verdict(tool(["filter", "--tracker", "t.md", "--sha", sha,
                              "--out", str(out)], cwd=self.dir))
        self.assertEqual(v["newest_commit"], sha)

    # (2) WITH-B4: a gap-filling NEW id lints (evidence only); an
    # ordinary status-change reuse of an existing id does not.
    def test_gap_filling_new_id_below_class_max_lints(self):
        body = ("- D1 [COMMITTED] first — basis: probe\n"
               "- D5 [COMMITTED] fifth, skipping ahead — basis: probe\n"
               "- D3 [COMMITTED] a NEW id filling the gap — basis: probe\n")
        p = tool(["lint", "--tracker", str(self.write_tracker(body))],
                 cwd=self.dir)
        self.assertIn("gap-filling id D3", p.stdout)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "LINT_CLEAN")  # evidence, not a hold

    def test_ordinary_status_change_reuse_does_not_lint(self):
        body = ("- D1 [PENDING] first — basis: probe\n"
               "- D2 [COMMITTED] second — basis: probe\n"
               "- D1 [COMMITTED] first, resolved — basis: probe\n")
        p = tool(["lint", "--tracker", str(self.write_tracker(body))],
                 cwd=self.dir)
        self.assertNotIn("gap-filling", p.stdout)

    def test_gap_filling_is_scoped_per_class(self):
        # D3 after D5 is gap-filling for D; F3 is class F's own FIRST
        # id and must not trip on D's unrelated maximum
        body = ("- D1 [COMMITTED] x — basis: y\n"
               "- D5 [COMMITTED] x — basis: y\n"
               "- F3 [VERIFIED] class F's own first F3 — basis: y\n")
        p = tool(["lint", "--tracker", str(self.write_tracker(body))],
                 cwd=self.dir)
        self.assertNotIn("gap-filling id F3", p.stdout)

    # (3) A5: an unwritable --out routes USAGE_ERROR like its two
    # siblings (missing parent, --out naming a directory) — not
    # INTERNAL_ERROR.
    @unittest.skipIf(os.name != "posix" or (hasattr(os, "geteuid")
                     and os.geteuid() == 0),
                     "permission bits are not enforced for root")
    def test_filter_unwritable_out_is_a_usage_error(self):
        self._git("init", "-b", "main")
        p = self.dir / "t.md"
        p.write_text(HEADER + "- F1 [VERIFIED] x — basis: y\n")
        self._git("add", "t.md")
        self._git("commit", "-m", "lock")
        sha = self._git("rev-parse", "HEAD").stdout.strip()
        out_tmp = tempfile.TemporaryDirectory()
        self.addCleanup(out_tmp.cleanup)
        out_dir = Path(out_tmp.name) / "ro"
        out_dir.mkdir()
        out_dir.chmod(0o555)
        self.addCleanup(out_dir.chmod, 0o755)
        out = out_dir / "artifact.md"
        v = self.verdict(tool(["filter", "--tracker", "t.md", "--sha", sha,
                              "--out", str(out)], cwd=self.dir))
        self.assertEqual(v["verdict"], "USAGE_ERROR")

    # (4) C1: the stale "no literal write-set record-line form" NOTE is
    # gone from the module docstring; the form is stated normative
    def test_docstring_no_longer_disclaims_the_write_set_form(self):
        text = SCRIPT.read_text()
        self.assertNotIn("no literal", text)
        self.assertIn("record-line form is normative in", text)
        self.assertIn(":876-880", text)
        self.assertIn(":486-487", text)


# ---------------------------------------- E-B: unknown --unit halts

class TestEBUnitUnknown(RecordFixture):
    """begehung-harvest triage T2 (WITHOUT-F2, attack-8 N3's referent
    half): closure --unit consulted no known-unit set — an id the
    record never scoped (a mistyped digit) fell through every
    predicate and read UNIT_DISPATCHABLE, silently clearing a hold on
    the REAL unit under the wrong id. known_units_of (shared with
    waves_over_units' own unplannable computation) now halts it."""

    BODY = (CLOSED +
            "- D9 [AUTO-ACCEPTED] unit U1 held: x.txt — basis: F9\n"
            "- R2 [AMENDED] unit U2 new letter — basis: gap report\n")

    def test_unscoped_ids_halt_unit_unknown(self):
        for unit in ("U11", "U21", "U7"):
            v = self.closure(self.BODY, unit=unit)
            self.assertEqual(v["verdict"], "UNIT_UNKNOWN",
                             f"{unit} parses as U<k> but names no line "
                             f"the tracker ever scoped")
            self.assertEqual(v["unit"], unit)

    def test_the_actually_held_unit_still_holds(self):
        # U1 → UNIT_HELD stays: known units are unaffected
        v = self.closure(self.BODY, unit="U1")
        self.assertEqual(v["verdict"], "UNIT_HELD")

    def test_the_actually_amended_unit_still_dispatches(self):
        # U2 → amendments stays: known units are unaffected
        v = self.closure(self.BODY, unit="U2")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")
        self.assertTrue(any("R2" in a["line"] for a in v["amendments"]))


# --------------------------------------- E-G': Mode + Budget (header)

MODE_HEADER = """# Run: test
Status: in-progress
Phase: investigate-design
Mode: careful

INTENT — do the thing.

## Cycle 1
"""

BUDGET_HEADER_2 = """# Run: test
Status: in-progress
Phase: investigate-design
Budget: cycles 7 / rounds 2 / verify 3

INTENT — do the thing.

## Cycle 1
"""


class TestEGPrimeHeaderFields(RecordFixture):
    """begehung-harvest triage T14's mechanical half (WITHOUT-F8 +
    SENTENCE-B4): Mode and Budget are literal header-line reads, the
    same shape as Status/Phase — surfaced, never gated. The
    irreversible half (P4) needs its own record-line grammar first
    and stays parked."""

    def test_mode_line_surfaces_in_sweep(self):
        v = self.sweep("- F1 [VERIFIED] x — basis: y\n", header=MODE_HEADER)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        self.assertEqual(v["mode"], "careful")

    def test_absent_mode_reads_none_in_sweep(self):
        v = self.sweep("- F1 [VERIFIED] x — basis: y\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        self.assertIsNone(v["mode"])

    def test_mode_line_surfaces_in_closure(self):
        v = self.closure(CLOSED, header=MODE_HEADER)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")
        self.assertEqual(v["mode"], "careful")

    def test_absent_mode_reads_none_in_closure(self):
        v = self.closure(CLOSED)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")
        self.assertIsNone(v["mode"])

    def test_budget_exhausted_tracker_shows_the_evidence_line(self):
        body = (
            "- A1 [DISPATCHED] round 1 — basis: brief\n"
            "- F1 [VERIFIED] finding a — basis: probe\n"
            "- A1 [BIT] one finding — basis: report\n"
            "- A2 [DISPATCHED] round 2 — basis: brief\n"
            "- F2 [VERIFIED] finding b — basis: probe\n"
            "- A2 [BIT] one finding — basis: report\n")
        p = tool(["sweep", "--tracker",
                 str(self.write_tracker(body, header=BUDGET_HEADER_2))],
                 cwd=self.dir)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        self.assertIn("meet/exceed Budget", p.stdout)

    def test_under_budget_control_stays_clean_and_silent(self):
        body = ("- A1 [DISPATCHED] round 1 — basis: brief\n"
                "- F1 [VERIFIED] finding a — basis: probe\n"
                "- A1 [BIT] one finding — basis: report\n")
        p = tool(["sweep", "--tracker",
                 str(self.write_tracker(body, header=BUDGET_HEADER_2))],
                 cwd=self.dir)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        self.assertNotIn("Budget", p.stdout)


# ------------------------------- P3: the mid-run SKILL: version line

class TestP3SkillVersionLine(RecordFixture):
    """BACKLOG P3: a resuming desk's version-crossing APPEND entry
    carries the literal line `SKILL: statiker <version>` —
    INTENT_EXACT_RE's sibling. Attribution only (FIELD, never a
    gate): the header's own `Skill: statiker <version>` line rides
    first, every mid-run `SKILL: ` line follows in file order."""

    def test_planted_line_surfaces_alongside_header_and_adds_no_violations(self):
        body = ("SKILL: statiker 0.2.99\n"
                "- F1 [VERIFIED] x — basis: y\n")
        v = self.sweep(body)
        # legality: the planted line is otherwise-clean-fixture-safe
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        header_line = self.lineno_of(body, "Skill: statiker")
        planted_line = self.lineno_of(body, "SKILL: statiker 0.2.99")
        self.assertEqual(v["skill_versions"], [
            {"line": header_line, "version": "0.2.33"},
            {"line": planted_line, "version": "0.2.99"},
        ])

    def test_absence_pair_carries_exactly_the_header_entry(self):
        body = "- F1 [VERIFIED] x — basis: y\n"
        v = self.sweep(body)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        header_line = self.lineno_of(body, "Skill: statiker")
        self.assertEqual(v["skill_versions"],
                         [{"line": header_line, "version": "0.2.33"}])

    def test_planted_line_surfaces_in_closure_too(self):
        body = "SKILL: statiker 0.2.99\n" + CLOSED
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")
        header_line = self.lineno_of(body, "Skill: statiker")
        planted_line = self.lineno_of(body, "SKILL: statiker 0.2.99")
        self.assertEqual(v["skill_versions"], [
            {"line": header_line, "version": "0.2.33"},
            {"line": planted_line, "version": "0.2.99"},
        ])

    def test_planted_line_never_reads_as_an_entry(self):
        # a line matching SIGNATURE_RE's opener alphabet could in
        # principle collide; SKILL: starts with a letter outside
        # {F,D,R,A,V} so it never near-misses as an entry
        body = "SKILL: statiker 0.2.99\n" + "- F1 [VERIFIED] x — basis: y\n"
        v = self.sweep(body)
        self.assertNotIn("entry-near-miss", self.violation_codes(v))
        self.assertNotIn("intent-near-miss", self.violation_codes(v))


# --------------------------- P4: the unit irreversible-effect tag line

class TestP4IrreversibleTag(RecordFixture):
    """BACKLOG P4: an impl unit whose green state includes something
    git cannot undo is tagged irreversible in its [READY] enumeration
    via its own record line `unit U<k> irreversible: <effect>` —
    HOLD_EXACT_RE's sibling. Attribution only (FIELD, never a gate;
    no near-miss lint class in this version — the parked entry's own
    caution: a bare-word scan false-fires on "not irreversible" and
    shared bodies, the E-K false-fire lesson). Unattended enforcement
    is untouched — it still routes through UNIT_HELD."""

    def test_planted_line_surfaces_and_adds_no_violations(self):
        body = ("- F9 [VERIFIED] unit U3 irreversible: deletes prod "
                "rows — basis: e\n")
        v = self.sweep(body)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        line = self.lineno_of(body, "irreversible: deletes prod rows")
        self.assertEqual(v["irreversible_units"],
                         [{"unit": "U3", "line": line,
                           "effect": "deletes prod rows"}])

    def test_absence_pair_carries_empty_list(self):
        body = "- F1 [VERIFIED] x — basis: y\n"
        v = self.sweep(body)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")
        self.assertEqual(v["irreversible_units"], [])

    def test_planted_line_surfaces_in_closure_too(self):
        body = ("- F9 [VERIFIED] unit U3 irreversible: deletes prod "
                "rows — basis: e\n") + CLOSED
        v = self.closure(body)
        self.assertEqual(v["verdict"], "CLOSURE_LIVE")
        line = self.lineno_of(body, "irreversible: deletes prod rows")
        self.assertEqual(v["irreversible_units"],
                         [{"unit": "U3", "line": line,
                           "effect": "deletes prod rows"}])

    def test_multiple_lines_ride_in_file_order(self):
        body = ("- F9 [VERIFIED] unit U3 irreversible: deletes prod "
                "rows — basis: e\n"
                "- F10 [VERIFIED] unit U5 irreversible: sends email "
                "— basis: e\n")
        v = self.sweep(body)
        self.assertEqual([e["unit"] for e in v["irreversible_units"]],
                         ["U3", "U5"])


# --------------------------------------------- E-F: the append freeze

class TestEFFreezeBreach(RecordFixture):
    """begehung-harvest F7: the append freeze is decidable from the
    tracker — a live round (latest A-line [DISPATCHED], no resolving
    line) makes any appended F/D/R line a breach."""

    def test_probe_two_appended_entries_under_a_live_dispatch_fire(self):
        body = ("- A1 [DISPATCHED] round 1 — basis: brief\n"
               "- F5 [VERIFIED] queued finding one — basis: probe\n"
               "- D3 [COMMITTED] queued decision — basis: probe\n")
        sv = self.sweep(body)
        self.assertEqual(sv["verdict"], "SWEEP_HOLDS")
        self.assertEqual(self.violation_codes(sv), {"freeze-breach"})
        lv = self.lint(body)
        self.assertEqual(lv["verdict"], "LINT_VIOLATIONS")
        self.assertEqual(self.violation_codes(lv), {"freeze-breach"})
        # both breaching lines are named, not just the first
        breach_lines = {v["line"] for v in sv["violations"]}
        self.assertEqual(
            breach_lines,
            {self.lineno_of(body, "F5"), self.lineno_of(body, "D3")})

    def test_resolved_a_line_control_stays_clean(self):
        # the SAME two appended lines, but the round already resolved
        # (ZERO-DELTA) after them — no live round, no breach
        body = ("- A1 [DISPATCHED] round 1 — basis: brief\n"
               "- F5 [VERIFIED] finding — basis: probe\n"
               "- D3 [COMMITTED] decision — basis: probe\n"
               "- A1 [ZERO-DELTA] clean return — basis: report\n")
        sv = self.sweep(body)
        self.assertEqual(sv["verdict"], "SWEEP_CLEAN")
        lv = self.lint(body)
        self.assertEqual(lv["verdict"], "LINT_CLEAN")

    def test_queue_landed_before_outcome_control_stays_clean(self):
        # the normal in-round shape: findings/decisions land, THEN the
        # round's own outcome line closes it — not a breach
        body = ("- A2 [DISPATCHED] round 2 — basis: brief\n"
               "- F6 [VERIFIED] finding during the round — basis: probe\n"
               "- A2 [BIT] found the mechanism — basis: report\n")
        sv = self.sweep(body)
        self.assertEqual(sv["verdict"], "SWEEP_CLEAN")
        lv = self.lint(body)
        self.assertEqual(lv["verdict"], "LINT_CLEAN")

    def test_no_a_line_at_all_stays_clean(self):
        v = self.sweep("- F1 [VERIFIED] a fact — basis: y\n")
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")

    def test_a_only_line_after_a_live_dispatch_is_not_a_breach(self):
        # the freeze governs F/D/R, never A itself — a fresh A-line is
        # how a round's own outcome or the next round gets recorded
        body = ("- A1 [DISPATCHED] round 1 — basis: brief\n"
               "- A2 [DISPATCHED] a second, unrelated round — basis: brief\n")
        v = self.sweep(body)
        self.assertEqual(v["verdict"], "SWEEP_CLEAN")

    def test_closure_and_waves_scope_is_unchanged(self):
        # E-F scopes the fire to sweep/lint only; closure's own
        # blocking set and waves are untouched
        body = ("- A1 [DISPATCHED] round 1 — basis: brief\n"
               "- F5 [VERIFIED] queued finding — basis: probe\n")
        wv = self.waves(body)
        self.assertEqual(wv["verdict"], "WAVES_COMPUTED")


# ---------------------------------------------------- pure-function checks

class TestPureFunctions(unittest.TestCase):
    def setUp(self):
        sys.path.insert(0, str(SCRIPT.parent))
        import statiker_record
        self.m = statiker_record

    def tearDown(self):
        sys.path.remove(str(SCRIPT.parent))

    def test_scope_classifier(self):
        self.assertEqual(self.m.classify_scope("unit U3 new letter"), ("unit", "U3"))
        self.assertEqual(self.m.classify_scope("record: bookkeeping"), ("record", None))
        self.assertEqual(self.m.classify_scope("the premise died"), ("scopeless", None))

    def test_defang_text(self):
        text, names = self.m.defang_text("x [VERIFIED] y [ISSUES FOUND] z")
        self.assertEqual(text, "x verified y issues found z")
        self.assertEqual(names, ["verified", "issues found"])

    def test_parse_counts_entries_like_a_newline_grep(self):
        # the parity the desk reads with `grep -c '^- '`
        # the form feed makes splitlines() see a SECOND entry on one
        # physical line — an entry the file does not contain
        text = (HEADER +
                "- F1 [VERIFIED] a fact — basis: y"
                "\x0c- F3 [VERIFIED] phantom entry — basis: y\n"
                "- F2 [VERIFIED] plain — basis: y\n")
        entries, _, _, _ = self.m.parse_tracker(text)
        grep = sum(1 for l in text.split("\n") if l.startswith("- "))
        self.assertEqual(len(entries), grep)

    def test_latest_map(self):
        entries = [
            self.m.Entry(1, "F", "F1", "PENDING", "b", "x"),
            self.m.Entry(2, "F", "F1", "VERIFIED", "b", "x"),
            self.m.Entry(3, "D", "D1", "COMMITTED", "b", "x"),
        ]
        latest = self.m.latest_by_id(entries)
        self.assertEqual(latest["F1"].tag, "VERIFIED")
        self.assertEqual(latest["D1"].tag, "COMMITTED")


if __name__ == "__main__":
    unittest.main(verbosity=1)

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


def tool(args, cwd=None, stdin_text=None):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args], cwd=cwd,
        input=stdin_text, capture_output=True, text=True, timeout=60)


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
        lines = [l for l in p.stdout.splitlines() if l.startswith(VERDICT_PREFIX)]
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
        v = self.closure("- A1 [DISPATCHED] round 1 — basis: brief\n"
                         "- A1 [BIT] two findings — basis: report\n")
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
        body = CLOSED + "- R2 [AMENDED] unit U2 new letter — basis: gap report\n"
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
        self.assertEqual(v["blocks_dropped"], 1)
        self.assertEqual(v["sections_dropped"], 1)

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
        self.assertEqual(v["sections_dropped"], 1)


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
        self.assertEqual(v["verdict"], "CLOSURE_ABSENT")  # A2 [BIT] governs

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

    def test_tracker_symlinked_outward_is_taken_as_named(self):
        # attack-9: repo_paths realpath'd the tracker, so an in-repo
        # tracker that happens to be a symlink read as a path outside
        # the repo. Containment is textual; only the repo TOP resolves.
        outside = self.no_repo_dir()
        real = Path(outside) / "real.md"
        real.write_text(HEADER + "- F1 [VERIFIED] kept — basis: y\n")
        link = self.dir / "linked.md"
        os.symlink(str(real), link)
        v = self.verdict(tool(["lint", "--tracker", str(link)],
                              cwd=str(self.dir)))
        self.assertEqual(v["verdict"], "LINT_CLEAN")

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
                f"{n}) — basis: probe\n")
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
        v = self.closure(
            self.hold_body("- D9 [AUTO-ACCEPTED] unit U3 held: x.txt "
                           "— basis: F9"), unit="U2")
        self.assertEqual(v["verdict"], "UNIT_DISPATCHABLE")


class TestAttack10ClauseGrammar(RecordFixture):
    """attack-10 N9: four clause dispositions on one [INVALIDATED]
    line, in mixed spellings. One parsed with a stray `;` glued to its
    value and one VANISHED without a trace — a clause disposition the
    aggregation never saw and no violation ever named."""

    LINE = ("- F5 [INVALIDATED] clause a restated-at-D7; clause b dead "
            "(killed by F9); clause c restated at D8; clause d dead "
            "— basis: F6\n")

    def test_no_clause_token_vanishes_silently(self):
        v = self.sweep(self.LINE)
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
        self.assertEqual(v["sections_dropped"], 1)


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
        body = self.corrected(
            "- D5 [COMMITTED] Record: bookkeeping — basis: probe\n",
            "- D5 [COMMITTED] record: bookkeeping (corrects line {n}) "
            "— basis: probe\n",
            "Record:")
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
        entries, _, _ = self.m.parse_tracker(text)
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

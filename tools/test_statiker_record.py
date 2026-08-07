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
        return self.verdict(tool(["lint", "--tracker", str(self.write_tracker(body, header))]))

    def sweep(self, body, header=HEADER):
        return self.verdict(tool(["sweep", "--tracker", str(self.write_tracker(body, header))]))

    def closure(self, body, unit=None, header=HEADER):
        args = ["closure", "--tracker", str(self.write_tracker(body, header))]
        if unit:
            args += ["--unit", unit]
        return self.verdict(tool(args))

    def violation_codes(self, v):
        return {viol["code"] for viol in v.get("violations", [])}


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
        out = self.dir / "artifact.md"
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
        out = self.dir / "a.md"
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

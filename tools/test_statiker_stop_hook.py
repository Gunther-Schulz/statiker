#!/usr/bin/env python3
"""Red-first fixture battery for plugin/hooks/statiker_stop_guard.py —
the P16 Stop hook against improvised unattended desk turn-ends
(BACKLOG.md P16; provenance dev-notes/OBSERVATIONS.md 2026-08-16, the
b7-post-A1 / cd-post-A2 incidents).

Invokes the hook script exactly as the harness does: JSON payload on
stdin, JSON (or nothing) on stdout, against constructed tracker
fixtures under `.clippy/runs/*-statiker.md` in a scratch directory —
never copies of a real run.

Fixtures cover the two incident shapes the hook must FIRE on and the
four legitimate-wait shapes it must stay SILENT on (brief's verifier),
plus discrimination and fail-open cases the module's own `--test`
battery does not already cover from the inside (this file drives the
script as an external process, the shape a Stop-hook registration
actually uses).

Run: python3 -m pytest tools/test_statiker_stop_hook.py -q
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOK = REPO_ROOT / "plugin" / "hooks" / "statiker_stop_guard.py"

HEADER = (
    "# Run: test\n"
    "Status: in-progress\n"
    "Phase: investigate-design\n"
    "Skill: statiker 0.2.81\n"
    "\n"
    "INTENT — do the thing.\n"
    "\n"
    "## Cycle 1\n"
)


def run_hook(cwd, event="Stop", extra=None):
    payload = {"hook_event_name": event, "cwd": str(cwd), "session_id": "t1"}
    if extra:
        payload.update(extra)
    return subprocess.run(
        [sys.executable, str(HOOK)], input=json.dumps(payload),
        capture_output=True, text=True, timeout=30)


class TrackerFixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.runs = self.dir / ".clippy" / "runs"
        self.runs.mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def write_tracker(self, text, name="2026-08-17-fixture-statiker.md"):
        (self.runs / name).write_text(text, encoding="utf-8")

    def assert_fires(self, result, contains=None):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.strip(), "expected a blocking JSON reply")
        j = json.loads(result.stdout)
        self.assertEqual(j.get("decision"), "block", j)
        self.assertIn("reason", j)
        self.assertNotIn("hookSpecificOutput", j)
        self.assertNotIn("permissionDecision", j)
        if contains:
            self.assertIn(contains, j["reason"])

    def assert_silent(self, result):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "", result.stdout)


# ── The two must-FIRE incident shapes ───────────────────────────────

class TestMustFire(TrackerFixture):
    def test_b7_shape_bit_no_blocking(self):
        """b7 post-A1: [BIT] terminal, Mode unattended (default, absent
        from header), no PENDING blocking at all — cycle re-derivation
        owed, the exact incident state."""
        self.write_tracker(
            HEADER
            + "- A1 [DISPATCHED] the first attack round.\n"
            + "- A1 [BIT] NOT zero-delta. Findings landed; the design "
              "REOPENS: Status returns to in-progress and cycle 2 "
              "re-derives.\n"
        )
        result = run_hook(self.dir)
        self.assert_fires(result, contains="[BIT]")

    def test_cd_shape_zero_delta_ordinary_pending(self):
        """cd post-A2: [ZERO-DELTA] terminal (a different terminal tag
        from the b7 fixture) with an ORDINARY, non-authority [PENDING]
        blocking entry — desk work owed, not authority-gated."""
        self.write_tracker(
            HEADER
            + "- A1 [DISPATCHED] the first attack round.\n"
            + "- A1 [BIT] findings landed; the design REOPENS.\n"
            + "- A2 [DISPATCHED] the second attack round.\n"
            + "- A2 [ZERO-DELTA] substance-free return; record repairs "
              "executed; closing design.\n"
            + "- F40 [PENDING] an unresolved desk question, no operator "
              "involvement — basis: needs a second read.\n"
        )
        result = run_hook(self.dir)
        self.assert_fires(result, contains="[ZERO-DELTA]")


# ── The four legitimate-wait shapes, all SILENT ─────────────────────

class TestLegitimateWaits(TrackerFixture):
    def test_attended_prompt(self):
        self.write_tracker(
            HEADER + "Mode: attended\n"
            + "- A1 [BIT] round one found substance.\n"
        )
        self.assert_silent(run_hook(self.dir))

    def test_round_in_flight_dispatched(self):
        self.write_tracker(
            HEADER + "- A1 [DISPATCHED] round one, live, awaiting return.\n"
        )
        self.assert_silent(run_hook(self.dir))

    def test_operator_authority_pending_sole_blocker(self):
        self.write_tracker(
            HEADER
            + "- A1 [BIT] round one found substance.\n"
            + "- F9 [PENDING] blocked on an OPERATOR-AUTHORITY grant "
              "before the ready gate — basis: needs operator line.\n"
        )
        self.assert_silent(run_hook(self.dir))

    def test_status_not_in_progress(self):
        self.write_tracker(
            HEADER.replace("Status: in-progress", "Status: COMPLETE")
            + "- A1 [BIT] round one found substance.\n"
        )
        self.assert_silent(run_hook(self.dir))


# ── Discrimination + fail-open + harness-shape cases ────────────────

class TestDiscriminationAndFailOpen(TrackerFixture):
    def test_no_tracker_at_all(self):
        # runs/ dir exists but empty — the common case, most sessions
        self.assert_silent(run_hook(self.dir))

    def test_no_statiker_repo_at_all(self):
        other = Path(tempfile.mkdtemp())
        try:
            self.assert_silent(run_hook(other))
        finally:
            os.rmdir(other)

    def test_authority_pending_plus_ordinary_pending_still_fires(self):
        """The blocking set is not SOLELY the authority ask when a
        second, ordinary PENDING also blocks — must fire."""
        self.write_tracker(
            HEADER
            + "- A1 [BIT] round one found substance.\n"
            + "- F1 [PENDING] blocked on an OPERATOR-AUTHORITY grant.\n"
            + "- F2 [PENDING] an ordinary open desk question.\n"
        )
        self.assert_fires(run_hook(self.dir))

    def test_malformed_tracker_never_blocks(self):
        self.write_tracker("garbage content, no header, no Status line\n")
        result = run_hook(self.dir)
        self.assert_silent(result)
        self.assertIn("statiker/stop-guard", result.stderr)

    def test_unknown_a_line_tag_never_blocks(self):
        self.write_tracker(HEADER + "- A1 [FROBNICATE] an unknown tag.\n")
        result = run_hook(self.dir)
        self.assert_silent(result)
        self.assertIn("statiker/stop-guard", result.stderr)

    def test_no_a_line_yet_never_blocks(self):
        """Pre-first-round investigate-design work: nothing this
        predicate can judge, never a fire."""
        self.write_tracker(HEADER)
        self.assert_silent(run_hook(self.dir))

    def test_pending_resolved_by_later_line_not_blocking(self):
        self.write_tracker(
            HEADER
            + "- A1 [BIT] round one found substance.\n"
            + "- F1 [PENDING] an open question.\n"
            + "- F1 [VERIFIED] resolved — basis: checked live.\n"
        )
        # F1 no longer blocks (latest line wins) → blocking set empty →
        # sole-authority branch never applies, but the fire condition
        # (terminal A-line, unattended, empty blocking set) still holds
        self.assert_fires(run_hook(self.dir))

    def test_quoted_a_line_not_read_as_live(self):
        """A `> `-prefixed quoted report block containing what LOOKS
        like an A-line must never be read as the live one — the
        false-fire probe named in the hook's own docstring."""
        self.write_tracker(
            HEADER
            + "- A1 [DISPATCHED] round one, live.\n"
            + "> Superseded — A1 quotes\n"
            + "> - A9 [BIT] this is quoted prose, not a live line\n"
        )
        # last LIVE A-line is still [DISPATCHED] → silent
        self.assert_silent(run_hook(self.dir))

    def test_non_stop_event_never_fires(self):
        self.write_tracker(
            HEADER
            + "- A1 [BIT] NOT zero-delta. Findings landed; the design "
              "REOPENS.\n"
        )
        result = run_hook(self.dir, event="SubagentStop")
        self.assert_silent(result)

    def test_garbage_stdin_never_blocks(self):
        result = subprocess.run(
            [sys.executable, str(HOOK)], input="}{ not json",
            capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")


if __name__ == "__main__":
    unittest.main()

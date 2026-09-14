#!/usr/bin/env python3
"""Pure-function certification of launch_substrate_probe.py's verdict()
logic (eve-review M3, 2026-09-14) — every existing --selftest case plus
the PROBE_INCONCLUSIVE paths S1/M2 add, and the control-dominates
precedence over both. Spawns NO child processes: verdict() is exercised
over constructed leg dicts only, so this module stays checkable without
spending the substrate the tool itself measures.

Run: python3 -m pytest tools/test_launch_substrate_probe.py -q
     (also collected by the whole-suite run: python3 -m pytest tools/ -q)
"""
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = REPO_ROOT / "tools"
sys.path.insert(0, str(TOOLS_DIR))
import launch_substrate_probe as lsp  # noqa: E402


def legs(cap, bg_pass, ctl, bg_inconclusive=False, bg_reason=None):
    """Build a constructed leg set. `bg_pass`/`bg_inconclusive` map onto
    the background-resume leg's own two fields — the same two fields
    verdict() actually reads, so a test that gets this wrong is a test
    of the helper, not of verdict()."""
    return [
        {"leg": "capability", "pass": cap},
        {"leg": "background-resume", "pass": bg_pass,
         "inconclusive": bg_inconclusive, "inconclusive_reason": bg_reason},
        {"leg": "single-turn-control", "pass": ctl},
    ]


class TestVerdictExistingCases(unittest.TestCase):
    """The five cases the tool's own --selftest carries, restated here
    as a pytest-collected, pure-function certification of the same
    logic (provenance: launch_substrate_probe.py's selftest())."""

    def test_all_pass_survives_reinvocation(self):
        name, _ = lsp.verdict(legs(True, True, True))
        self.assertEqual(name, "SUBSTRATE_SURVIVES_REINVOCATION")

    def test_bg_fails_dies_at_reinvocation(self):
        name, _ = lsp.verdict(legs(True, False, True))
        self.assertEqual(name, "SUBSTRATE_DIES_AT_REINVOCATION")

    def test_cap_and_bg_fail_unfit_capability(self):
        name, _ = lsp.verdict(legs(False, False, True))
        self.assertEqual(name, "SUBSTRATE_UNFIT_CAPABILITY")

    def test_control_dominates_over_bg_fail(self):
        name, _ = lsp.verdict(legs(True, False, False))
        self.assertEqual(name, "PROBE_INVALID")

    def test_control_dominates_over_bg_pass(self):
        # the control still fires FIRST even when every other leg is a
        # clean pass — a broken probe never reports a substrate finding
        name, _ = lsp.verdict(legs(True, True, False))
        self.assertEqual(name, "PROBE_INVALID")


class TestVerdictProbeInconclusive(unittest.TestCase):
    """S1/M2: the background-resume leg's THIRD answer — it could not
    be exercised — is neither a substrate pass nor a substrate death."""

    def test_bg_inconclusive_with_healthy_capability_and_control(self):
        name, why = lsp.verdict(legs(
            True, False, True, bg_inconclusive=True,
            bg_reason="the launcher itself timed out"))
        self.assertEqual(name, "PROBE_INCONCLUSIVE")
        self.assertIn("timed out", why)

    def test_bg_inconclusive_reason_travels_verbatim(self):
        reason = ("TURN_END was written no earlier than BG_DONE: the "
                  "child did not end its turn before the backgrounded "
                  "work finished")
        name, why = lsp.verdict(legs(
            True, False, True, bg_inconclusive=True, bg_reason=reason))
        self.assertEqual(name, "PROBE_INCONCLUSIVE")
        self.assertEqual(why, reason)

    def test_bg_inconclusive_with_no_reason_still_names_a_state(self):
        # inconclusive=True with no reason string must not crash verdict()
        # into a bare None message — the state is nameable even when a
        # leg forgets to fill in why.
        name, why = lsp.verdict(legs(
            True, False, True, bg_inconclusive=True, bg_reason=None))
        self.assertEqual(name, "PROBE_INCONCLUSIVE")
        self.assertTrue(why)

    def test_control_dominates_over_bg_inconclusive(self):
        # the control-dominates precedence extends to the new state: a
        # broken invocation is reported as broken, never as "the
        # lifecycle question could not be answered"
        name, _ = lsp.verdict(legs(
            True, False, False, bg_inconclusive=True,
            bg_reason="timeout"))
        self.assertEqual(name, "PROBE_INVALID")

    def test_capability_dominates_over_bg_inconclusive(self):
        # capability is checked before the background-resume leg is
        # ever consulted, inconclusive or not
        name, _ = lsp.verdict(legs(
            False, False, True, bg_inconclusive=True,
            bg_reason="timeout"))
        self.assertEqual(name, "SUBSTRATE_UNFIT_CAPABILITY")

    def test_bg_pass_true_but_inconclusive_true_still_inconclusive(self):
        # inconclusive is checked ahead of pass on the same leg: a leg
        # that could not be exercised is never read as a substrate
        # finding merely because its pass flag also happens to be set
        name, _ = lsp.verdict(legs(
            True, True, True, bg_inconclusive=True, bg_reason="timeout"))
        self.assertEqual(name, "PROBE_INCONCLUSIVE")


if __name__ == "__main__":
    unittest.main()

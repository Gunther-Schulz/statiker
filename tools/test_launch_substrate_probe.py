#!/usr/bin/env python3
"""Pure-function certification of launch_substrate_probe.py's verdict()
logic (eve-review M3, 2026-09-14) — every existing --selftest case plus
the PROBE_INCONCLUSIVE paths S1/M2 add, and the control-dominates
precedence over both; and (S2 repair, run-3 contract narrow round,
2026-09-14/15) the leg_background_resume() marker-to-leg-dict routing
that PRODUCES those pass/inconclusive fields in the first place.
verdict() itself is exercised over constructed leg dicts only, spawning
NO child processes. leg_background_resume() spawns a subprocess too
(that is how it works), but only ever a trivial no-op shell command
("true") over pre-seeded marker files -- never `claude`, never a model
child, never the thing this tool measures.

Run: python3 -m pytest tools/test_launch_substrate_probe.py -q
     (also collected by the whole-suite run: python3 -m pytest tools/ -q)
"""
import os
import shutil
import sys
import tempfile
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


class TestLegBackgroundResumeMarkerRouting(unittest.TestCase):
    """S2 (docs/audits/2026-09-14-narrow-round-run3-contract.md):
    leg_background_resume() returns pass=False, inconclusive=False for
    two reachable marker states where ACK IS PRESENT -- verdict() then
    reports SUBSTRATE_DIES_AT_REINVOCATION with the reason "the ACK
    marker is absent", which is false. Cause: the inconclusive route
    was gated on `turn_end_present and bg_present` while the prompt
    bundles the marker and the turn-end instruction into one step, so
    ACK-present-but-TURN_END-absent fell through to the "not pass"
    branch instead of the PROBE_INCONCLUSIVE route where it belongs.

    Driven end-to-end through the REAL function (not a reimplementation
    of its logic) via a no-op launcher and pre-seeded marker files --
    the audit's own reproduction method, stated in its own words as
    "executed over every reachable marker combination with a fake
    shell launcher". No child model process is invoked; "true" is a
    shell no-op.
    """

    def setUp(self):
        # SLEEP_S only pads leg_background_resume()'s wait-deadline for a
        # detached process that, in these tests, was never started -- the
        # marker files are pre-seeded before the call. Shrinking it to 0
        # cuts the bg-absent cases' wait from 18s to 10s each without
        # changing what is being tested (the tunable is restored after).
        self._orig_sleep_s = lsp.SLEEP_S
        lsp.SLEEP_S = 0

    def tearDown(self):
        lsp.SLEEP_S = self._orig_sleep_s

    def _seed(self, bg, ack, turn_end, order=None):
        """order: 'compliant' (TURN_END written before BG_DONE, as the
        prompt instructs) or 'noncompliant' (written no earlier than
        BG_DONE); irrelevant when either marker is absent."""
        work = tempfile.mkdtemp(prefix="s2-battery-")
        self.addCleanup(shutil.rmtree, work, ignore_errors=True)
        base = 1_700_000_000.0
        if turn_end and bg:
            te_t, bg_t = (base, base + 5) if order == "compliant" \
                else (base + 5, base)
        else:
            te_t = bg_t = base
        if bg:
            p = os.path.join(work, "BG_DONE")
            open(p, "w").write("BGDONE")
            os.utime(p, (bg_t, bg_t))
        if ack:
            open(os.path.join(work, "ACK_AFTER_BG"), "w").write("ACKED")
        if turn_end:
            p = os.path.join(work, "TURN_END")
            open(p, "w").write("TURNEND")
            os.utime(p, (te_t, te_t))
        return work

    def _leg(self, **kw):
        work = self._seed(**kw)
        return lsp.leg_background_resume("true", work)

    def test_must_not_move_neither_marker_stays_dies_at_reinvocation(self):
        # BASELINE (verifier requirement): the recorded 0.2.100 verdict
        # -- genuinely no ACK -- must PASS against old code AND new.
        leg = self._leg(bg=False, ack=False, turn_end=False)
        self.assertFalse(leg["pass"])
        self.assertFalse(leg["inconclusive"])
        self.assertFalse(leg["detail"]["ack_marker"])
        legs = [{"leg": "capability", "pass": True}, leg,
                {"leg": "single-turn-control", "pass": True}]
        name, why = lsp.verdict(legs)
        self.assertEqual(name, "SUBSTRATE_DIES_AT_REINVOCATION")
        self.assertIn("ACK marker is absent", why)

    def test_ack_present_turn_end_absent_bg_absent_routes_inconclusive(self):
        # S2 named state: bg=F ack=T turn_end=F
        leg = self._leg(bg=False, ack=True, turn_end=False)
        self.assertTrue(leg["detail"]["ack_marker"])
        self.assertTrue(
            leg["inconclusive"],
            "ACK present must never fall through to the 'not pass' "
            "branch verdict() reports as 'the ACK marker is absent'")
        self.assertFalse(leg["pass"])

    def test_ack_present_turn_end_absent_bg_present_routes_inconclusive(self):
        # S2 named state: bg=T ack=T turn_end=F
        leg = self._leg(bg=True, ack=True, turn_end=False)
        self.assertTrue(leg["inconclusive"])
        self.assertFalse(leg["pass"])

    def test_ack_present_bg_absent_turn_end_present_routes_inconclusive(self):
        # latent third state, same defect shape, surfaced by driving
        # every reachable combination rather than only the two the
        # audit named
        leg = self._leg(bg=False, ack=True, turn_end=True)
        self.assertTrue(leg["inconclusive"])
        self.assertFalse(leg["pass"])

    def test_no_leg_ever_reports_the_false_dies_shape_while_ack_present(self):
        # the general invariant the repair establishes, swept across
        # every reachable combination with ACK present: a leg is never
        # left as pass=False, inconclusive=False (the exact shape
        # verdict() reads as "capability legs pass and the ACK marker
        # is absent") when ACK actually landed.
        for bg in (False, True):
            for turn_end in (False, True):
                orders = (("compliant", "noncompliant") if (bg and turn_end)
                          else (None,))
                for order in orders:
                    leg = self._leg(bg=bg, ack=True, turn_end=turn_end,
                                     order=order)
                    with self.subTest(bg=bg, turn_end=turn_end, order=order):
                        false_dies_shape = (leg["pass"] is False
                                             and leg["inconclusive"] is False)
                        self.assertFalse(
                            false_dies_shape,
                            f"bg={bg} turn_end={turn_end} order={order}: "
                            "ACK present but leg reports the false "
                            "'ACK marker is absent' shape")

    def test_compliant_order_all_present_still_survives(self):
        # regression guard: the one genuine survive state must not move
        leg = self._leg(bg=True, ack=True, turn_end=True, order="compliant")
        self.assertTrue(leg["pass"])
        self.assertFalse(leg["inconclusive"])

    def test_noncompliant_order_all_present_stays_inconclusive(self):
        # regression guard: the pre-existing ordering-inconclusive path
        # (both markers present, wrong order) is unmoved by this repair
        leg = self._leg(bg=True, ack=True, turn_end=True,
                         order="noncompliant")
        self.assertTrue(leg["inconclusive"])
        self.assertIn("TURN_END was written no earlier than BG_DONE",
                       leg["inconclusive_reason"])

    def test_genuine_death_ack_absent_both_other_markers_present(self):
        # regression guard: correct-order lifecycle fully exercised (turn
        # ended, background completed) but the child never got
        # re-invoked to write ACK -- a true substrate death, and the
        # "ACK marker is absent" reason is actually true here
        leg = self._leg(bg=True, ack=False, turn_end=True, order="compliant")
        self.assertFalse(leg["pass"])
        self.assertFalse(leg["inconclusive"])
        self.assertFalse(leg["detail"]["ack_marker"])


if __name__ == "__main__":
    unittest.main()

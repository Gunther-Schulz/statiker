#!/usr/bin/env python3
"""Pure-function certification of driver_resume_probe.py's verdict()
logic (C4b mint, dev-notes/OBSERVATIONS.md 2026-09-15) -- the RED-FIRST
defect case (rc blindness), the MUST-NOT-MOVE genuine-green case, and
each of the four independent PROBE_INVALID dominations. Spawns NO child
processes: verdict() is exercised over constructed leg dicts only, so
this module stays checkable without spending the substrate the tool
itself measures.

Run: python3 -m pytest tools/test_driver_resume_probe.py -q
     (also collected by the whole-suite run: python3 -m pytest tools/ -q)
"""
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = REPO_ROOT / "tools"
sys.path.insert(0, str(TOOLS_DIR))
import driver_resume_probe as drp  # noqa: E402


def legs(ctl=True, ctl_rc=0, u_rc=0, u_ack=False,
         d_rc1=0, d_rc2=0, d_ack=True, d_token_ok=True,
         f_rc=0, f_reproduced=False):
    """Build a constructed leg set. Defaults describe a genuine green:
    control passes, unaided stays silent, driven acks with the correct
    token, fresh reproduces nothing. Each keyword overrides exactly the
    field verdict() itself reads."""
    return [
        {"leg": "single-turn-control", "pass": ctl, "rc": ctl_rc},
        {"leg": "unaided", "rc": u_rc, "ack": u_ack},
        {"leg": "driven", "rc1": d_rc1, "rc2": d_rc2, "ack": d_ack,
         "token_correct": d_token_ok},
        {"leg": "fresh", "rc": f_rc, "reproduced_nonce": f_reproduced},
    ]


class TestVerdictRedFirst(unittest.TestCase):
    """The defect this tool was minted to fix: a timeout or refusal on
    either arm (rc=None) produced the same absent marker a genuine
    substrate death produces. Pre-repair this read as DRIVER_DOES_NOT_
    CARRY; the fix must route it to PROBE_INVALID instead."""

    def test_both_arms_timeout_is_probe_invalid_not_substrate_verdict(self):
        name, _ = drp.verdict(legs(
            u_rc=None, d_rc1=None, d_rc2=None, d_ack=False,
            d_token_ok=False))
        self.assertEqual(name, "PROBE_INVALID")

    def test_nonzero_rc_on_one_leg_only_is_probe_invalid(self):
        # ack/token look perfectly healthy -- only rc2 betrays the leg
        # that did not run cleanly. Old code never read rc anywhere.
        name, _ = drp.verdict(legs(d_rc2=1))
        self.assertEqual(name, "PROBE_INVALID")

    def test_unaided_leg_timeout_alone_is_probe_invalid(self):
        name, _ = drp.verdict(legs(u_rc=None))
        self.assertEqual(name, "PROBE_INVALID")


class TestVerdictMustNotMove(unittest.TestCase):
    """A genuine green must clear PROBE_INVALID and read DRIVER_WORKS --
    the repair must not simply make every case invalid."""

    def test_genuine_green_is_driver_works(self):
        name, why = drp.verdict(legs())
        self.assertEqual(name, "DRIVER_WORKS")
        self.assertIn("resumed", why)


class TestVerdictProbeInvalidDominations(unittest.TestCase):
    """The four independent conditions from the C4b mint record, each
    its own leg, none subsuming another."""

    def test_control_leg_failed_dominates_over_green_driven(self):
        name, _ = drp.verdict(legs(ctl=False))
        self.assertEqual(name, "PROBE_INVALID")

    def test_control_dominates_even_with_every_other_leg_healthy(self):
        # belt-and-suspenders: control fails while rc/ack/token/fresh are
        # all otherwise clean -- control still wins first
        name, _ = drp.verdict(legs(ctl=False, ctl_rc=1))
        self.assertEqual(name, "PROBE_INVALID")

    def test_unaided_ack_dominates(self):
        name, why = drp.verdict(legs(u_ack=True))
        self.assertEqual(name, "PROBE_INVALID")
        self.assertIn("unaided", why)

    def test_fresh_arm_reproducing_nonce_dominates_over_driver_works(self):
        # driven arm looks perfectly healthy -- the fresh negative
        # control failing must still win, never DRIVER_WORKS
        name, why = drp.verdict(legs(f_reproduced=True))
        self.assertEqual(name, "PROBE_INVALID")
        self.assertIn("fresh", why)


class TestVerdictFalseGreen(unittest.TestCase):
    """Unrelated to the rc defect: ACK present but the wrong token means
    the second invocation did not actually resume the first session."""

    def test_ack_present_wrong_token_is_false_green(self):
        name, why = drp.verdict(legs(d_token_ok=False))
        self.assertEqual(name, "DRIVER_FALSE_GREEN")
        self.assertIn("WRONG", why)


class TestVerdictDoesNotCarry(unittest.TestCase):
    """No ACK on the driven arm, everything else clean and having run:
    the substrate genuinely does not carry work across the boundary."""

    def test_no_ack_anywhere_is_does_not_carry(self):
        name, _ = drp.verdict(legs(d_ack=False, d_token_ok=False))
        self.assertEqual(name, "DRIVER_DOES_NOT_CARRY")


if __name__ == "__main__":
    unittest.main()

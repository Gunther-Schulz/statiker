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

THE RED-FIRST ARRANGEMENT, recorded here because a proof's basis is the
ARRANGEMENT -- which side was old, and where the expectations came from
-- and this one's discriminating half was produced in a session
scratchpad that no longer exists. Carried into the artifact by the
dispatching desk after the lane's report was booked, 2026-09-15.

TWO FORMS WERE RUN, and only the second discriminates.

Form 1, LITERAL: this battery committed alone (08a71af) against the
real pre-repair file, which was then restored into the working tree and
run. Result: 10 failed, every one
`AttributeError: module 'driver_resume_probe' has no attribute
'verdict'`. REAL BUT NON-DISCRIMINATING -- extracting verdict() was
itself the repair's first item, so the old file has no such function
and the must-not-move case does NOT pass in this form. Recorded as
uninformative rather than dressed as a red.

Form 2, RECONSTRUCTED: the pre-repair decision branch
(`git show 08a71af:tools/driver_resume_probe.py`, lines 94-110)
transcribed as a pure function, print/return-code pairs replaced by
(token, rc) tuples, no branching logic altered. Verified faithful by
the dispatching desk against that blob -- branch order, conditions and
return codes match on all four arms; the sole divergence, `.get()` for
`[]` on token_correct, is strictly more permissive and unreachable in
every case run:

    def old_verdict(u, d):
        if u["ack"]:
            return ("OLD_LEG_MEANS_NOTHING", 2)
        if d["ack"] and d.get("token_correct"):
            return ("OLD_DRIVER_WORKS", 0)
        if d["ack"] and not d.get("token_correct"):
            return ("OLD_FALSE_GREEN", 1)
        return ("OLD_DOES_NOT_CARRY", 1)

FIDELITY CONTROL, run BEFORE the cases and passed -- without it the
reconstruction is an instrument authored by the same hand as the code
it grades:
    old_verdict({'ack': False}, {'ack': True, 'token_correct': True})
      -> ('OLD_DRIVER_WORKS', 0)
matching the module docstring's recorded real measurement of
2026-09-14 (UNAIDED ack=False rc=0 / DRIVEN ack=True token_correct=True
-> DRIVER WORKS, rc 0).

OUTCOME, in three-way language because two-way would hide the third
answer this very repair exists to make sayable:

    1 both arms rc=None          old: DOES_NOT_CARRY -> RED
    7 nonzero rc, one leg only   old: DRIVER_WORKS   -> RED
    3 control leg failed         no such leg in old  -> COULD-NOT-VERIFY
    5 fresh arm reproduced nonce no such leg in old  -> COULD-NOT-VERIFY
    2 genuine green              old: DRIVER_WORKS   -> PASS-BY-COINCIDENCE
    4 unaided ACK                old: equivalent     -> PASS-BY-COINCIDENCE
    6 ACK + wrong token          old: FALSE_GREEN    -> PASS-BY-COINCIDENCE

Cases 1 and 7 are the true red: the rc blindness this repair fixes.
Cases 3 and 5 are could-not-verify, NOT passes -- old code had no leg
to be right or wrong about, and that structural absence is itself the
evidence the gap was real. Cases 2/4/6 land on the same token for
reasons unrelated to the repair and are NOT evidence the old code was
sound.
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

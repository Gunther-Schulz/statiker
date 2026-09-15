#!/usr/bin/env python3
"""Decide the ceiling-arm substrate question: can an externally DRIVEN
`claude -p` session carry work across a turn boundary?

THE DEFECT THIS REPAIR FIXES (narrow-round S1, 2026-09-14; C4b mint,
dev-notes/OBSERVATIONS.md 2026-09-15). The pre-repair tool refused a
verdict on exactly ONE condition -- the unaided arm having written its
marker (`if u["ack"]`) -- and never inspected any child's return code
anywhere. A timeout, a rate-limit refusal, or any nonzero exit produced
the same absent marker a healthy substrate-death produces, and passed
straight through to a SUBSTRATE verdict ("DRIVER DOES NOT CARRY THE
WORK") over an attempt that never ran. This is the corpus's own
third-answer class: an instrument offering only two outputs cannot say
could-not-verify, so the grade it exists to forbid becomes structural.

THE FIX: a `PROBE_INVALID` state with DOMINATION over every substrate
verdict -- reused verbatim from the sibling tool
`launch_substrate_probe.py`, never re-coined -- plus a single-turn
CONTROL leg (same sibling idiom) and a FRESH, never-resumed negative-
control arm that must not be able to reproduce the driven arm's nonce.
`verdict()` is a pure function over constructed leg dicts, exercised by
`--selftest` (no child process) and by the pytest battery
`test_driver_resume_probe.py`.

THE ARMS, all run here:
  CONTROL  -- one invocation, write a marker immediately. MUST-NOT-MOVE:
              a RED here indicts the invocation or this probe, never the
              driver substrate (sibling idiom: leg_single_turn_control).
  UNAIDED  -- one invocation, child ends its turn. ACK must be ABSENT.
              This is the red the leg exists to distinguish; if it is not
              red, the leg measures nothing.
  DRIVEN   -- invocation 1 with --session-id, child ends its turn; this
              tool then re-invokes with --resume. ACK must be PRESENT
              and carry the DRIVEN nonce.
  FRESH    -- a brand-new session id, NEVER resumed, given turn 2's own
              prompt verbatim ("write the token you were given earlier").
              It has no earlier turn in THIS session, so it must NOT
              reproduce the driven arm's nonce. If it does, the nonce is
              reachable without a resume and the whole discriminator is
              dead -- PROBE_INVALID, never DRIVER_WORKS, even if the
              driven arm also looks green.

THE NONCES are per-arm (unaided and driven each get their own, S3) --
what makes the driven arm mean "resumed" rather than "ran twice", and
what makes the fresh arm a real negative control rather than a
tautology: turn 1 is given a token and told nothing else about it; turn
2 is asked to write THE TOKEN IT WAS GIVEN. A fresh session cannot
produce it unless the resume mechanism itself is leaky.

MEASURED, 2026-09-14, this machine, model sonnet -- the pair that
settled run 3's ceiling-arm substrate question (pre-repair tool, kept
for provenance; the fresh-arm negative control and the rc/control
dominations did not exist yet when this was measured):

    UNAIDED : ack=False, rc=0            <- RED, as required
    DRIVEN  : ack=True,  token_correct=True,
              token reproduced verbatim  <- resumed WITH CONTEXT

VERDICT (pre-repair, still holds): DRIVER WORKS. `claude -p --session-id
<uuid>` followed by `claude -p --resume <uuid>` carries work across a
turn boundary with context intact. This is the route between "a -p
child dies at turn end" (measured separately by
tools/launch_substrate_probe.py, verdict SUBSTRATE_DIES_AT_REINVOCATION)
and "no dispatchable substrate".

THE FREEZE EXECUTOR RE-RUNS THIS against the run's ACTUAL driver
arrangement before arms dispatch. A probe of a substitute invocation
measures a substrate the run will not use -- which is why the launcher
invocation is now aimed via `--launcher-file`, the sibling's own idiom,
rather than hardcoded.

Run:  python3 tools/driver_resume_probe.py --launcher-file CMD.txt
      python3 tools/driver_resume_probe.py --selftest

`--launcher-file` holds the run's ACTUAL arm-launch invocation, one
shell command, carrying TWO placeholders: `{PROMPT_FILE}` (the sibling's
own placeholder -- the prompt content's path) and `{SESSION_ARGS}` (new
to this tool: this probe's whole subject is the `--session-id`/`--resume`
mechanism, so the launcher must leave a slot for this tool to insert
"", "--session-id <uuid>", or "--resume <uuid>" per invocation -- e.g.
`claude -p --model sonnet --permission-mode acceptEdits {SESSION_ARGS}
"$(cat {PROMPT_FILE})"`). Deviation from the sibling's single-placeholder
form, documented here because it is the one point where this tool's
launcher contract widens beyond the precedent it otherwise follows
exactly.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import uuid

CHILD_TIMEOUT_S = 240


def _run(cmd, timeout=CHILD_TIMEOUT_S):
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True,
                           timeout=timeout)
        return p.returncode, p.stdout.decode(errors="replace")[-400:]
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"


def _aim(launcher, prompt_path, session_args=""):
    return launcher.replace("{PROMPT_FILE}", prompt_path) \
                   .replace("{SESSION_ARGS}", session_args)


def leg_single_turn_control(launcher, work):
    """MUST-NOT-MOVE (sibling idiom: leg_single_turn_control). Work that
    completes inside one turn, so it passes on any substrate that
    functions at all. Without it, a probe broken in any way reports
    every substrate as unfit and reads exactly like a true finding."""
    marker = os.path.join(work, "CONTROL_ONE_TURN")
    prompt = os.path.join(work, "prompt_control.txt")
    with open(prompt, "w") as f:
        f.write(f"Write the text ONETURN into {marker}. Nothing else.\n")
    rc, out = _run(_aim(launcher, prompt))
    ok = os.path.exists(marker) and "ONETURN" in open(marker).read()
    return {
        "leg": "single-turn-control",
        "pass": bool(ok),
        "rc": rc,
        "note": ("must-not-move: a RED here indicts the probe or the "
                 "invocation, never the driver substrate"),
    }


def leg_unaided(launcher, work, nonce):
    """THE RED THE PAIR NEEDS. One invocation, child ends its turn. ACK
    must be ABSENT -- if it is not, this pair does not distinguish
    driven from unaided and no substrate conclusion is readable."""
    ack = os.path.join(work, "ACK_UNAIDED")
    prompt = os.path.join(work, "prompt_unaided.txt")
    with open(prompt, "w") as f:
        f.write(
            f"Remember this token: {nonce}. Do NOT write it anywhere yet. "
            f"End your turn now without doing anything else. "
            f"If you are ever asked again, write the token into {ack}.\n")
    rc, out = _run(_aim(launcher, prompt))
    return {"leg": "unaided", "rc": rc, "ack": os.path.exists(ack),
            "tail": out.strip()[-160:]}


def leg_driven(launcher, work, nonce):
    """THE DISCRIMINATING PAIR'S OTHER HALF. Invocation 1 establishes a
    session and gives it the nonce; the child ends its turn and exits --
    the first process is gone. This tool then re-invokes the SAME
    session with --resume. Nothing else is carried across: if the resume
    does not restore context, turn 2 cannot produce the token."""
    ack = os.path.join(work, "ACK_DRIVEN")
    sid = str(uuid.uuid4())
    p1 = os.path.join(work, "prompt_driven_1.txt")
    with open(p1, "w") as f:
        f.write(
            f"Remember this token: {nonce}. Do NOT write it anywhere yet. "
            f"End your turn now without doing anything else.\n")
    rc1, out1 = _run(_aim(launcher, p1, f"--session-id {sid}"))

    p2 = os.path.join(work, "prompt_driven_2.txt")
    with open(p2, "w") as f:
        f.write(
            f"Write the token you were given earlier into {ack}. "
            f"Write only the token, nothing else.\n")
    rc2, out2 = _run(_aim(launcher, p2, f"--resume {sid}"))

    got = open(ack).read().strip() if os.path.exists(ack) else ""
    return {"leg": "driven", "session_id": sid, "rc1": rc1, "rc2": rc2,
            "ack": os.path.exists(ack), "token_correct": got == nonce,
            "got": got[:60], "tail2": out2.strip()[-160:]}


def leg_fresh(launcher, work, driven_nonce):
    """S3, THE NEGATIVE CONTROL. A brand-new session id, NEVER resumed,
    given turn 2's own prompt verbatim -- asked to write "the token it
    was given earlier" despite having no earlier turn in THIS session.
    It must NOT reproduce the driven arm's nonce; if it does, the nonce
    is reachable without a resume and the whole discriminator is dead."""
    marker = os.path.join(work, "ACK_FRESH")
    sid = str(uuid.uuid4())
    prompt = os.path.join(work, "prompt_fresh.txt")
    with open(prompt, "w") as f:
        f.write(
            f"Write the token you were given earlier into {marker}. "
            f"Write only the token, nothing else.\n")
    rc, out = _run(_aim(launcher, prompt, f"--session-id {sid}"))
    got = open(marker).read().strip() if os.path.exists(marker) else ""
    return {"leg": "fresh", "session_id": sid, "rc": rc,
            "reproduced_nonce": got == driven_nonce, "got": got[:60],
            "tail": out.strip()[-160:]}


def verdict(legs):
    """Pure function over constructed leg dicts (sibling idiom:
    launch_substrate_probe.verdict()). PROBE_INVALID dominates every
    substrate conclusion, on any of four independent conditions -- each
    its own leg, none subsuming another, matching this tool's own
    OBSERVATIONS mint record:
      (a) any leg's rc is None (timeout) or nonzero -- the leg did not
          run cleanly;
      (b) the single-turn control leg failed;
      (c) the unaided arm produced ACK (the pair distinguishes nothing);
      (d) the fresh, never-resumed arm reproduced the driven nonce (the
          discriminator is dead).
    Only past all four does a substrate verdict get read off the driven
    arm's own ACK/token pair."""
    by = {l["leg"]: l for l in legs}
    control = by["single-turn-control"]
    unaided = by["unaided"]
    driven = by["driven"]
    fresh = by["fresh"]

    if not control["pass"]:
        return ("PROBE_INVALID",
                "the single-turn control failed: the invocation or this "
                "probe is broken, and no lifecycle conclusion is readable")

    for leg_name, rc in (("single-turn-control", control.get("rc")),
                         ("unaided", unaided.get("rc")),
                         ("driven", driven.get("rc1")),
                         ("driven", driven.get("rc2")),
                         ("fresh", fresh.get("rc"))):
        if rc is None or rc != 0:
            return ("PROBE_INVALID",
                    f"the {leg_name} leg exited rc={rc!r}: the leg did "
                    "not run cleanly, no lifecycle conclusion is readable")

    if unaided["ack"]:
        return ("PROBE_INVALID",
                "the unaided arm produced ACK: this pair does not "
                "distinguish driven from unaided, no lifecycle "
                "conclusion is readable")

    if fresh["reproduced_nonce"]:
        return ("PROBE_INVALID",
                "the fresh, never-resumed arm reproduced the driven "
                "arm's nonce: the discriminator is dead, a fresh "
                "session can produce the token without a resume")

    if driven["ack"] and driven["token_correct"]:
        return ("DRIVER_WORKS",
                "driven session resumed WITH CONTEXT (token reproduced); "
                "unaided arm red as required, fresh arm did not "
                "reproduce the nonce")
    if driven["ack"] and not driven["token_correct"]:
        return ("DRIVER_FALSE_GREEN",
                "ACK written but the token is WRONG "
                f"({driven.get('got', '')!r}): the second invocation did "
                "NOT resume the first session. A driver keying on ACK "
                "alone would have reported this as working.")
    return ("DRIVER_DOES_NOT_CARRY",
            "no ACK on the driven arm either: work backgrounded across a "
            "turn boundary is lost")


def selftest():
    """Exercise the VERDICT logic on constructed leg sets, including the
    RED-FIRST defect case and the MUST-NOT-MOVE case, by hand -- no child
    process, so the instrument stays checkable without spending the
    substrate it measures. The freeze executor runs this immediately
    before a live run."""
    def legs(ctl=True, ctl_rc=0, u_rc=0, u_ack=False,
             d_rc1=0, d_rc2=0, d_ack=True, d_token_ok=True,
             f_rc=0, f_reproduced=False):
        return [
            {"leg": "single-turn-control", "pass": ctl, "rc": ctl_rc},
            {"leg": "unaided", "rc": u_rc, "ack": u_ack},
            {"leg": "driven", "rc1": d_rc1, "rc2": d_rc2, "ack": d_ack,
             "token_correct": d_token_ok},
            {"leg": "fresh", "rc": f_rc, "reproduced_nonce": f_reproduced},
        ]

    cases = [
        ("RED-FIRST: both arms rc=None, no markers",
         legs(u_rc=None, d_rc1=None, d_rc2=None, d_ack=False,
              d_token_ok=False),
         "PROBE_INVALID"),
        ("MUST-NOT-MOVE: genuine green",
         legs(),
         "DRIVER_WORKS"),
        ("control leg failed, driven still looks green",
         legs(ctl=False),
         "PROBE_INVALID"),
        ("unaided arm produced ACK",
         legs(u_ack=True),
         "PROBE_INVALID"),
        ("fresh arm reproduced the driven nonce",
         legs(f_reproduced=True),
         "PROBE_INVALID"),
        ("ACK present, wrong token",
         legs(d_token_ok=False),
         "DRIVER_FALSE_GREEN"),
        ("nonzero rc on ONE leg only (driven rc2)",
         legs(d_rc2=1),
         "PROBE_INVALID"),
    ]
    bad = 0
    for label, l, want in cases:
        got, _ = verdict(l)
        mark = "ok " if got == want else "FAIL"
        if got != want:
            bad += 1
        print(f"  {mark} {label:50} -> {got} (want {want})")
    print("selftest: PASS" if not bad else f"selftest: {bad} FAILED")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--launcher-file",
                    help="file holding the run's ACTUAL arm-launch command, "
                         "with {PROMPT_FILE} and {SESSION_ARGS} placeholders")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--keep", action="store_true",
                    help="keep the scratch target for inspection")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.launcher_file:
        print("need --launcher-file or --selftest", file=sys.stderr)
        return 2

    launcher = open(args.launcher_file).read().strip()
    if "{PROMPT_FILE}" not in launcher or "{SESSION_ARGS}" not in launcher:
        print("the launcher command must carry {PROMPT_FILE} and "
              "{SESSION_ARGS}", file=sys.stderr)
        return 2

    work = tempfile.mkdtemp(prefix="driver-probe-")
    unaided_nonce = "ZEPHYR-" + uuid.uuid4().hex[:10].upper()
    driven_nonce = "ZEPHYR-" + uuid.uuid4().hex[:10].upper()
    try:
        control = leg_single_turn_control(launcher, work)
        unaided = leg_unaided(launcher, work, unaided_nonce)
        driven = leg_driven(launcher, work, driven_nonce)
        fresh = leg_fresh(launcher, work, driven_nonce)
        legs = [control, unaided, driven, fresh]
        name, why = verdict(legs)

        print(f"work={work}")
        for l in legs:
            print(f"  {l['leg']:22} {l}")
        print(f"\nVERDICT: {name}\n  {why}")
        return 0 if name == "DRIVER_WORKS" else 1
    finally:
        if not args.keep:
            shutil.rmtree(work, ignore_errors=True)
        else:
            print(f"kept: {work}")


if __name__ == "__main__":
    sys.exit(main())

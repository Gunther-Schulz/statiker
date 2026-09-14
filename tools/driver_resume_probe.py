#!/usr/bin/env python3
"""Decide the ceiling-arm substrate question: can an externally DRIVEN
`claude -p` session carry work across a turn boundary?

The discriminating pair, both arms run here:
  UNAIDED  — one invocation, child ends its turn. ACK must be ABSENT.
             This is the red the leg exists to distinguish; if it is not
             red, the leg measures nothing.
  DRIVEN   — invocation 1 with --session-id, child ends its turn; an
             external driver then re-invokes with --resume. ACK must be
             PRESENT.

THE NONCE is what makes the driven arm mean "resumed" rather than
"ran twice": turn 1 is given a token and told nothing else about it;
turn 2 is asked to write THE TOKEN IT WAS GIVEN. A fresh session cannot
produce it. Without this, a driver that silently starts a NEW session
each time would read as a working resume — the false green this arm
would otherwise ship.

MEASURED, 2026-09-14, this machine, model sonnet — the pair that
settles run 3's ceiling-arm substrate question:

    UNAIDED : ack=False, rc=0            <- RED, as required
    DRIVEN  : ack=True,  token_correct=True,
              token reproduced verbatim  <- resumed WITH CONTEXT

VERDICT: DRIVER WORKS. `claude -p --session-id <uuid>` followed by
`claude -p --resume <uuid>` carries work across a turn boundary with
context intact. This is the route between "a -p child dies at turn
end" (measured separately by tools/launch_substrate_probe.py, verdict
SUBSTRATE_DIES_AT_REINVOCATION) and "no dispatchable substrate" — and
it is OPEN, which is why the earlier absence claim was wrong.

THE FREEZE EXECUTOR RE-RUNS THIS against the run's ACTUAL driver
arrangement before arms dispatch. A probe of a substitute invocation
measures a substrate the run will not use.
"""
import os, subprocess, sys, tempfile, time, uuid

MODEL = "sonnet"
TIMEOUT = 240


def run(cmd, timeout=TIMEOUT):
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, timeout=timeout)
        return p.returncode, p.stdout.decode(errors="replace")[-400:]
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"


def arm_unaided(work, nonce):
    ack = os.path.join(work, "ACK_UNAIDED")
    p = (f"Remember this token: {nonce}. Do NOT write it anywhere yet. "
         f"End your turn now without doing anything else. "
         f"If you are ever asked again, write the token into {ack}.")
    rc, out = run(f'claude -p --model {MODEL} --permission-mode acceptEdits '
                  f'"{p}"')
    return {"arm": "unaided", "rc": rc, "ack": os.path.exists(ack),
            "tail": out.strip()[-160:]}


def arm_driven(work, nonce):
    ack = os.path.join(work, "ACK_DRIVEN")
    sid = str(uuid.uuid4())
    p1 = (f"Remember this token: {nonce}. Do NOT write it anywhere yet. "
          f"End your turn now without doing anything else.")
    rc1, out1 = run(f'claude -p --model {MODEL} --permission-mode acceptEdits '
                    f'--session-id {sid} "{p1}"')
    # THE DRIVER: the first process has exited at its turn end. Re-invoke
    # the SAME session. Nothing else is carried across — if the resume
    # does not restore context, turn 2 cannot produce the token.
    p2 = (f"Write the token you were given earlier into {ack}. "
          f"Write only the token, nothing else.")
    rc2, out2 = run(f'claude -p --model {MODEL} --permission-mode acceptEdits '
                    f'--resume {sid} "{p2}"')
    got = ""
    if os.path.exists(ack):
        got = open(ack).read().strip()
    return {"arm": "driven", "session_id": sid, "rc1": rc1, "rc2": rc2,
            "ack": os.path.exists(ack), "token_correct": got == nonce,
            "got": got[:60], "tail2": out2.strip()[-160:]}


def main():
    work = tempfile.mkdtemp(prefix="driver-probe-")
    nonce = "ZEPHYR-" + uuid.uuid4().hex[:10].upper()
    print(f"work={work}\nnonce={nonce}\n")
    u = arm_unaided(work, nonce)
    print("UNAIDED :", u)
    d = arm_driven(work, nonce)
    print("DRIVEN  :", d)
    print()
    if u["ack"]:
        print("LEG MEANS NOTHING: the unaided arm produced ACK, so this "
              "pair does not distinguish driven from unaided.")
        return 2
    if d["ack"] and d["token_correct"]:
        print("VERDICT: DRIVER WORKS — driven session resumed WITH CONTEXT "
              "(token reproduced); unaided arm red as required.")
        return 0
    if d["ack"] and not d["token_correct"]:
        print("VERDICT: FALSE-GREEN CAUGHT — ACK written but the token is "
              f"WRONG ({d['got']!r}): the second invocation did NOT resume "
              "the first session. A driver keying on ACK alone would have "
              "reported this as working.")
        return 1
    print("VERDICT: DRIVER DOES NOT CARRY THE WORK — no ACK on the driven "
          "arm either.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

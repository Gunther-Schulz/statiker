#!/usr/bin/env python3
"""Exercise a comparison run's ARM-LAUNCH substrate at the freeze gate,
including the background-resume leg, before any arm dispatches.

WHY THIS EXISTS. Run 2's ceiling arm completed attack preparation
ENTIRELY — its pre-round seal and its pinned artifact were both written
to the correct authorized paths — and then died at the RE-INVOCATION
boundary. A `claude -p` child ends at its turn's end, so work it
backgrounds expecting to be re-invoked dies with it. The arm exited
rc=0. Nothing in the arrangement had exercised that boundary, because
every capability check the arrangement did run (can it write files, can
it commit) passes on a substrate that cannot survive a turn.

So: capability legs prove nothing about SESSION LIFECYCLE, and a
substrate probe either includes a background-resume leg or says it did
not.

WHERE THIS LIVES, and why it is NOT payload (desk ruling 2026-09-14,
accepted by the judgment desk; recorded here so the next reader meets
the boundary reasoning where the tool sits rather than in a chat log):

  1. The self-containment criterion is BOUNDED to mechanisms of THE RUN
     AND ITS RECORD. Arm-launch substrate is comparison-run
     ARRANGEMENT, not run conduct — statiker the skill does not
     dispatch arms; the experiment does.
  2. A bare-machine statiker user has no arms to launch, so nothing is
     silently lost by this tool's absence there. The criterion's test is
     whether an absence is SILENTLY lossy; here it is not lossy at all.
  3. st-65 already owns this seam — "every expected-result line
     re-measured under the invocation the brief mandates on the tree the
     executor will meet". This probe is that rule with one invocation
     filled in, so it is an instance rather than a sibling rule.

THE THREE FALSE GREENS THIS PROBE REFUSES TO KEY ON. All three are
available, all three look like the obvious anchor, and all three
report a dead substrate as a live one:

  - THE CHILD'S EXIT CODE. Run 2's arm exited rc=0 while dying
    mid-task. A launcher reports that the run happened, never what it
    found.
  - THE BACKGROUNDED PROCESS'S OWN MARKER. A detached process outlives
    the parent that spawned it, so the background work COMPLETES even
    when the substrate cannot be re-invoked. Keying on it reads a dead
    substrate as healthy.
  - THE CHILD'S COMPLIANCE WITH THE FORCED-TURN-END INSTRUCTION
    (eve-review, 2026-09-14 — v2 ships the fix). v1 forced the turn end
    with prompt text alone. A child that ignores that text and polls
    in-foreground for its own background marker still lands ACK
    without ever needing re-invocation, and the leg passed GREEN on a
    substrate v1's own header already said this leg exists to catch —
    the defect moved from structural (any substrate) to
    compliance-dependent (only a substrate whose child obeys the
    prompt), never removed. v2 adds a marker the child writes
    IMMEDIATELY after backgrounding the sleep — before the turn ends,
    never after waiting for it — and compares its mtime against the
    detached marker's: a compliant child's marker predates the
    background completion, an in-foreground poller's does not.

The discriminator for substrate death is the marker only the CHILD can
write AFTER the backgrounded work finished: it requires the substrate
to still be there to act a second time. That is the arm-1 failure
exactly. The discriminator for COMPLIANCE — a separate question this
leg cannot answer with a substrate verdict, and does not try to — is
below.

Run:  python3 tools/launch_substrate_probe.py --launcher-file CMD.txt
      python3 tools/launch_substrate_probe.py --selftest

`--launcher-file` holds the run's ACTUAL arm-launch invocation, one
shell command, with {PROMPT_FILE} where the arm's prompt path goes. The
run's own invocation is the object under test: a probe of a substitute
invocation measures a substrate the run will not use.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time

SLEEP_S = 8          # long enough to cross a turn boundary, short enough to be cheap
CHILD_TIMEOUT_S = 240


def _run(cmd, cwd=None, timeout=CHILD_TIMEOUT_S):
    try:
        p = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True,
                           timeout=timeout)
        return p.returncode, p.stdout.decode(errors="replace"), \
            p.stderr.decode(errors="replace")
    except subprocess.TimeoutExpired:
        return None, "", f"TIMEOUT after {timeout}s"


def leg_capability(launcher, work):
    """Can the child write and commit at all? Verified AT THE ARTIFACT —
    a child reporting success is testimony like any other."""
    made = os.path.join(work, "cap_bash.txt")
    written = os.path.join(work, "cap_write.md")
    prompt = os.path.join(work, "prompt_cap.txt")
    with open(prompt, "w") as f:
        f.write(
            f"Do exactly this and nothing else:\n"
            f"1. Using a shell command, write the text CAPBASH into {made}\n"
            f"2. Using your file-writing tool, write the text CAPWRITE "
            f"into {written}\n"
            f"3. Run: git -C {work} add -A && git -C {work} "
            f"commit -q -m 'probe capability leg'\n")
    rc, out, err = _run(launcher.replace("{PROMPT_FILE}", prompt), cwd=work)

    ok_bash = os.path.exists(made) and "CAPBASH" in open(made).read()
    ok_write = os.path.exists(written) and "CAPWRITE" in open(written).read()
    rc_git, git_out, _ = _run(f"git -C {work} log --oneline", timeout=30)
    ok_commit = rc_git == 0 and "probe capability leg" in git_out
    return {
        "leg": "capability",
        "pass": bool(ok_bash and ok_write and ok_commit),
        "child_rc": rc,
        "detail": {"bash_write": ok_bash, "tool_write": ok_write,
                   "commit": ok_commit},
        "note": "verified at the artifact, never from the child's claim",
    }


def leg_background_resume(launcher, work):
    """THE LEG THAT DISCHARGES THE PRECONDITION. Red-first case: run 2's
    arm 1, which completed its whole task and died at re-invocation.

    THREE markers. Two discriminate substrate death; the third
    discriminates whether the other two can be trusted at all:
      BG        — written by a DETACHED process. Can survive the child,
                  so its presence alone says nothing about the substrate.
      ACK       — written by the CHILD, after the backgrounded work
                  finished. Requires the substrate to still exist to act
                  a second time.
      TURN_END  — written by the CHILD as its LAST act immediately after
                  backgrounding the sleep, before ending its turn —
                  never after waiting for BG. A child that instead polls
                  in-foreground for BG before "ending its turn" writes
                  TURN_END no earlier than BG, and that ordering is the
                  eve-review 2026-09-14 fix: v1 keyed only on ACK, so a
                  non-compliant child that waits in-turn for its own
                  background marker still landed ACK without ever
                  needing re-invocation, reporting the compliance-
                  dependent green as a genuine substrate survival.

    THE TURN END IS FORCED, and this leg is worthless without it —
    measured, both arms, 2026-09-14, the first version of this probe:

      prompt NOT forcing a turn end  -> BG=YES ACK=YES rc=0  (GREEN)
      prompt forcing the turn end    -> BG=NO  ACK=NO  rc=0  (RED)

    Same substrate, same launcher, opposite verdicts. Without the forced
    end the child simply WAITS IN-TURN for its own background marker and
    writes ACK without ever needing re-invocation — so the leg measures
    "can the child wait", not "can the child be re-invoked", and reports
    the substrate that killed run 2's arm 1 as fit. The first version of
    this probe shipped that defect and its green is what exposed it.
    "Forced" in a prompt is a request, not a guarantee, though: a child
    that silently ignores the instruction and polls anyway reproduces
    the exact same BG=YES ACK=YES rc=0 the unforced prompt produced —
    v2's whole reason for existing is that this ordering check catches
    what the forced wording alone cannot enforce.

    Note the RED arm loses BG too: with the turn ended, the backgrounded
    task dies with its parent before landing its own marker. The child
    still exits rc=0 — which is why the exit code is not consulted.

    A THIRD leg outcome exists beside pass/fail: INCONCLUSIVE. Two
    routes produce it, neither a substrate verdict:
      - the launcher itself times out (rc is None) — no result, and a
        timeout rendered as SUBSTRATE_DIES_AT_REINVOCATION is
        could-not-verify wearing a confirmed-dead costume (eve-review
        M2: `verdict()` v1 read a bare `rc=None` timeout as this leg's
        ordinary fail path, no different from a substrate that ran to
        completion and produced no ACK);
      - TURN_END is present but not before BG — the compliance failure
        above. The lifecycle question was never exercised, so this is
        not a finding about the substrate, it is a finding about the
        run: the child did not end its turn as instructed.
    """
    bg = os.path.join(work, "BG_DONE")
    ack = os.path.join(work, "ACK_AFTER_BG")
    turn_end = os.path.join(work, "TURN_END")
    prompt = os.path.join(work, "prompt_bg.txt")
    with open(prompt, "w") as f:
        f.write(
            f"Do exactly this:\n"
            f"1. Start a BACKGROUND shell task that sleeps {SLEEP_S} "
            f"seconds and then writes the text BGDONE into {bg}.\n"
            f"2. Write the text TURNEND into {turn_end} as your LAST "
            f"act, then END YOUR TURN immediately. Do not wait, do not "
            f"poll, do not sleep in the foreground.\n"
            f"3. You will be re-invoked when the background task "
            f"completes. ONLY THEN, write the text ACKED into {ack}.\n")
    t0 = time.time()
    rc, out, err = _run(launcher.replace("{PROMPT_FILE}", prompt), cwd=work)
    child_elapsed = time.time() - t0

    # give a detached background process room to land its own marker, so
    # the BG/ACK split is measured rather than assumed
    deadline = time.time() + SLEEP_S + 10
    while time.time() < deadline and not os.path.exists(bg):
        time.sleep(0.5)

    bg_present = os.path.exists(bg)
    ack_present = os.path.exists(ack)
    turn_end_present = os.path.exists(turn_end)
    turn_end_mtime = os.path.getmtime(turn_end) if turn_end_present else None
    bg_mtime = os.path.getmtime(bg) if bg_present else None
    ordering_ok = bool(turn_end_present and bg_present
                       and turn_end_mtime < bg_mtime)

    inconclusive = False
    inconclusive_reason = None
    if rc is None:
        inconclusive = True
        inconclusive_reason = (
            f"the launcher itself timed out after its {CHILD_TIMEOUT_S}s "
            "budget before this leg could be exercised: no result, never "
            "a substrate death")
    elif turn_end_present and bg_present and not ordering_ok:
        inconclusive = True
        inconclusive_reason = (
            "TURN_END was written no earlier than BG_DONE: the child did "
            "not end its turn before the backgrounded work finished, so "
            "the re-invocation lifecycle question was never exercised")

    return {
        "leg": "background-resume",
        "pass": bool(ack_present and ordering_ok),
        "inconclusive": inconclusive,
        "inconclusive_reason": inconclusive_reason,
        "child_rc": rc,
        "child_elapsed_s": round(child_elapsed, 1),
        "detail": {"bg_marker": bg_present, "ack_marker": ack_present,
                   "turn_end_marker": turn_end_present,
                   "turn_end_mtime": turn_end_mtime, "bg_mtime": bg_mtime,
                   "ordering_ok": ordering_ok},
        "note": ("pass requires ACK present AND TURN_END present AND "
                 "TURN_END strictly earlier than BG_DONE. BG alone means "
                 "the DETACHED process outlived the child, which a dead "
                 "substrate also produces; ACK alone (no ordering check) "
                 "is the compliance-dependent green this leg no longer "
                 "trusts; child_rc is not consulted for pass/fail — run "
                 "2's arm exited rc=0 while dying mid-task — but rc=None "
                 "(a launcher timeout) and a reversed TURN_END/BG_DONE "
                 "ordering both route to `inconclusive` instead of a "
                 "pass/fail verdict"),
    }


def leg_single_turn_control(launcher, work):
    """MUST-NOT-MOVE. Work that completes inside one turn, so it passes
    on any substrate that functions at all. Without it, a probe broken in
    any way reports every substrate as unfit and reads exactly like a
    true finding."""
    marker = os.path.join(work, "CONTROL_ONE_TURN")
    prompt = os.path.join(work, "prompt_control.txt")
    with open(prompt, "w") as f:
        f.write(f"Write the text ONETURN into {marker}. Nothing else.\n")
    rc, out, err = _run(launcher.replace("{PROMPT_FILE}", prompt), cwd=work)
    ok = os.path.exists(marker) and "ONETURN" in open(marker).read()
    return {
        "leg": "single-turn-control",
        "pass": bool(ok),
        "child_rc": rc,
        "note": ("must-not-move: a RED here indicts the probe or the "
                 "invocation, never the substrate's lifecycle"),
    }


def verdict(legs):
    by = {l["leg"]: l for l in legs}
    control = by["single-turn-control"]
    if not control["pass"]:
        return ("PROBE_INVALID",
                "the single-turn control failed: the invocation or this "
                "probe is broken, and no lifecycle conclusion is readable")
    if not by["capability"]["pass"]:
        return ("SUBSTRATE_UNFIT_CAPABILITY",
                "the child cannot write or commit; lifecycle untested")
    bg_leg = by["background-resume"]
    if bg_leg.get("inconclusive"):
        return ("PROBE_INCONCLUSIVE",
                 bg_leg.get("inconclusive_reason")
                 or "the background-resume leg could not be exercised")
    if not bg_leg["pass"]:
        return ("SUBSTRATE_DIES_AT_REINVOCATION",
                "capability legs pass and the ACK marker is absent: this "
                "is run 2 arm 1's death exactly — work backgrounded for a "
                "later turn is lost, and the arm exits rc=0")
    return ("SUBSTRATE_SURVIVES_REINVOCATION",
            "all three legs pass, control included")


def selftest():
    """Exercise the VERDICT logic on constructed leg sets, including the
    two false greens. Costs no child process, so the instrument stays
    checkable without spending the thing it measures."""
    def legs(cap, bg, ctl):
        return [{"leg": "capability", "pass": cap},
                {"leg": "background-resume", "pass": bg},
                {"leg": "single-turn-control", "pass": ctl}]
    cases = [
        (legs(True, True, True), "SUBSTRATE_SURVIVES_REINVOCATION"),
        (legs(True, False, True), "SUBSTRATE_DIES_AT_REINVOCATION"),
        (legs(False, False, True), "SUBSTRATE_UNFIT_CAPABILITY"),
        # the control dominates: a broken probe never reports a finding
        (legs(True, False, False), "PROBE_INVALID"),
        (legs(True, True, False), "PROBE_INVALID"),
    ]
    bad = 0
    for l, want in cases:
        got, _ = verdict(l)
        mark = "ok " if got == want else "FAIL"
        if got != want:
            bad += 1
        print(f"  {mark} cap={l[0]['pass']!s:5} bg={l[1]['pass']!s:5} "
              f"ctl={l[2]['pass']!s:5} -> {got} (want {want})")
    print("selftest: PASS" if not bad else f"selftest: {bad} FAILED")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--launcher-file",
                    help="file holding the run's ACTUAL arm-launch command, "
                         "with {PROMPT_FILE} as the prompt-path placeholder")
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
    if "{PROMPT_FILE}" not in launcher:
        print("the launcher command must carry {PROMPT_FILE}", file=sys.stderr)
        return 2

    work = tempfile.mkdtemp(prefix="statiker-substrate-")
    _run(f"git -C {work} init -q && git -C {work} commit -q --allow-empty "
         f"-m base", timeout=30)
    try:
        legs = [leg_single_turn_control(launcher, work),
                leg_capability(launcher, work),
                leg_background_resume(launcher, work)]
        name, why = verdict(legs)
        print(f"launcher: {launcher}")
        print(f"target:   {work}")
        for l in legs:
            print(f"  {l['leg']:22} pass={l['pass']!s:5} "
                  f"child_rc={l.get('child_rc')} {l.get('detail', '')}")
        print(f"\nSUBSTRATE VERDICT: {name}\n  {why}")
        return 0 if name == "SUBSTRATE_SURVIVES_REINVOCATION" else 1
    finally:
        if not args.keep:
            shutil.rmtree(work, ignore_errors=True)
        else:
            print(f"kept: {work}")


if __name__ == "__main__":
    sys.exit(main())

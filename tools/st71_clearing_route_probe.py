#!/usr/bin/env python3
"""st-71's PRE-REGISTERED PROBE, run at the effect site.  SECOND VERSION.

WHY THERE IS A SECOND VERSION, recorded rather than quietly fixed: the
first run was VOID and reported a confident wrong answer.  Every arm
came back `PATH_OUTSIDE_REPO` rc=2 -- the tool refuses a tracker
outside a git repo, and the scratchpad is not one -- so nothing swept.
The validity gate was gated on the NEGATIVE control (defanged body ->
no tag-literal violation), which a DEAD INSTRUMENT satisfies exactly as
a live one does, so the script printed "instrument OK" and concluded
"ROUTE EXISTS -> documentation gap".  A dead producer returns what a
true negative returns; only a POSITIVE control separates them.

FIXED HERE, both halves:
  * the fixture dir is `git init`-ed, mirroring the repo battery's own
    setUp (tools/test_statiker_record.py:64-72) rather than inventing a
    second arrangement;
  * VALIDITY IS GATED ON THE POSITIVE CONTROL.  Arm A is a known
    positive -- the battery's test_defang_class_is_never_exemptible
    asserts this exact body yields SWEEP_HOLDS with
    tag-literal-in-body.  If arm A does not fire, every other reading
    is void and the script says so instead of concluding.

THE QUESTION, unchanged: st-71 OPENS ON A PROBE, NOT A DESIGN.
  hold DROPS when the owning entry is superseded/invalidated
      -> a clearing route EXISTS, st-71 is a DOCUMENTATION gap, no
         tool change
  hold STANDS -> the class is real, a sanctioned route must be designed

PREDICTION REGISTERED BEFORE THIS RUN: the hold STANDS.  The
owner-conditioning I found at statiker_record.py:701 conditions the
REPAIR FORM shown (REPAIR_INTENT_HOLD), not whether the violation
fires, and tag-literal-in-body is in UNEXEMPTIBLE_CODES.  Arms C and D
going quiet is what would refute me.
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

TOOL = ("/home/g/dev/Gunther-Schulz/statiker/plugin/skills/statiker/"
        "scripts/statiker_record.py")

HEADER = """# Run: test
Status: in-progress
Phase: investigate-design
Skill: statiker 0.2.33

INTENT — do the thing.

## Cycle 1
"""
CITE = " — basis: operator line quoted in D95"

LIVE = ("- F1 [VERIFIED] the guard prints [PENDING] on a miss "
        "— basis: executed\n")
# v2's "defang" was adjacent-string-literal CONCATENATION -- "[PEND"
# "ING]" rebuilds "[PENDING]" byte for byte at runtime, so the negative
# control was the positive control wearing a defanged NAME. The gate
# caught it. The real defang is backticks: statiker_record.py's own
# check opens `scrubbed = BACKTICK_RE.sub(" ", body)  # quoting a
# literal is legal`, so the legal spelling comes from the mechanism
# rather than from my idea of what defanging looks like.
# THIRD spelling of the negative control, and the last: backticks did
# not clear it either (BACKTICK_RE scrubs inside the WRITE-SET check,
# a different function -- reading one check's scrub and assuming the
# other's is the reach error in miniature). So the control stops
# trying to DEFANG a literal and simply carries none: a body with no
# bracketed tag literal in its prose at all cannot trip the rule, and
# if it does, the instrument is measuring something else entirely.
NO_LITERAL = ("- F1 [VERIFIED] the guard prints the pending tag "
              "— basis: executed\n")

ARMS = [
    ("A  POSITIVE CONTROL: live owning line, undefanged", LIVE, True),
    ("B  + SWEEP_EXEMPT (known-inert, battery-proven)",
     LIVE + f"SWEEP_EXEMPT: tag-literal-in-body lines<=999{CITE}\n", True),
    ("C  owning entry restated [INVALIDATED]",
     LIVE + ("- F1 [INVALIDATED] withdrawn, the literal was mine "
             "— basis: executed\n"), None),
    ("D  owning entry superseded whole",
     LIVE + "> Superseded — F1 restated below\n"
          + "- F1 [VERIFIED] the guard prints the pending tag "
            "— basis: executed\n", None),
    ("E  NEGATIVE CONTROL: no bracketed literal in the prose", NO_LITERAL, False),
    # arm F added after v2's raw-output read: the tool's OWN verdict names
    # a repair for this violation ("bookkeeping: append `- <id> [<tag>]
    # record: corrects line 9 ...` — sheds violations only"). That is a
    # candidate clearing route straight from the mechanism, and not testing
    # the route the tool itself prescribes would have left the probe
    # answering a narrower question than st-71 asks.
    ("F  the TOOL'S OWN prescribed repair (corrects-line bookkeeping)",
     LIVE + ("- F1 [VERIFIED] record: corrects line 9 — basis: the "
             "tag-literal-in-body verdict at line 9\n"), None),
    # ARMS G/H added after reading the INCIDENT, which arms A-F never
    # reproduced. OBSERVATIONS 2026-09-14: arm 2's "offending line is
    # bare prose that parses no entry id, so the hold is
    # OWNER-CONDITIONED and unreachable by any `corrects line <n>`
    # token; the tracker is append-only, so the line cannot be edited.
    # Terminal deadlock." Every arm above put the literal on F1, an
    # OWNING entry line -- the one shape the incident is not. A true
    # reading of the wrong case is the reach error, so the probe was
    # answering a narrower question than st-71 asks.
    ("G  INCIDENT SHAPE: literal in BARE PROSE (no entry id)",
     "the guard prints [PENDING] on a miss, as the desk noted\n"
     + "- F1 [VERIFIED] unrelated finding — basis: executed\n", None),
    ("H  incident shape + the corrects-line token (does it reach?)",
     "the guard prints [PENDING] on a miss, as the desk noted\n"
     + "- F1 [VERIFIED] unrelated finding — basis: executed\n"
     + "- F1 [VERIFIED] record: corrects line 9 — basis: the "
       "tag-literal-in-body verdict at line 9\n", None),
]


def sweep(body):
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=d,
                       env={**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null"},
                       capture_output=True, check=True)
        t = Path(d) / "tracker.md"
        t.write_text(HEADER + body, encoding="utf-8")
        r = subprocess.run(
            [sys.executable, TOOL, "sweep", "--tracker", str(t)],
            capture_output=True, text=True, cwd=d)
        # the tool prints human preamble lines BEFORE the verdict line;
        # v2 parsed the whole stdout and failed on the first of them
        raw = ""
        for ln in r.stdout.splitlines():
            if ln.startswith("STATIKER-RECORD VERDICT:"):
                raw = ln[len("STATIKER-RECORD VERDICT:"):].strip()
        try:
            return json.loads(raw), r.returncode, None
        except json.JSONDecodeError:
            return None, r.returncode, (r.stdout[-300:], r.stderr[-300:])


def main():
    print("st-71 PROBE v2 — does a clearing route already exist?\n")
    res = {}
    for name, body, _ in ARMS:
        v, rc, err = sweep(body)
        if v is None:
            print(f"{name}\n    UNPARSED rc={rc}: {err}\n")
            res[name[0]] = None
            continue
        codes = sorted({h.get("code") for h in v.get("violations", [])
                        if isinstance(h, dict)})
        fires = "tag-literal-in-body" in codes
        res[name[0]] = (v.get("verdict"), fires)
        print(f"{name}\n    verdict={v.get('verdict')!r} rc={rc} "
              f"tag-literal-in-body fires: {fires}")
        if codes:
            print(f"    codes: {', '.join(c for c in codes if c)}")
        print()

    print("=" * 62)
    a, e = res.get("A"), res.get("E")
    if not a or a[1] is not True:
        print("VOID — the POSITIVE control did not fire. The instrument is "
              "dead or mis-aimed; every reading above is meaningless. "
              "(This is the failure v1 shipped as an answer.)")
        return 2
    if not e or e[1] is not False:
        print("VOID — the negative control fired; the fixture itself trips "
              "the rule, so 'fires' distinguishes nothing.")
        return 2
    print("INSTRUMENT PROVEN: positive control fires, negative control "
          "clean. The arms below discriminate.")
    owned = [k for k, r in (("INVALIDATED", res.get("C")),
                            ("supersede-whole", res.get("D")),
                            ("corrects-line token", res.get("F")))
             if r and r[1] is False]
    print(f"OWNED-LINE case  — routes that clear the hold: "
          f"{', '.join(owned) if owned else 'NONE'}")
    g, h = res.get("G"), res.get("H")
    owner_less = [k for k, r in (("corrects-line token", h),)
                  if r and r[1] is False]
    print(f"OWNER-LESS case (THE INCIDENT) — fires at all: "
          f"{g[1] if g else '?'}; routes that clear it: "
          f"{', '.join(owner_less) if owner_less else 'NONE'}")
    print()
    if g and g[1] and not owner_less:
        print("VERDICT — st-71's branch 2: for the MOTIVATING case the "
              "hold STANDS and no token reaches it, while the tracker is "
              "append-only so the line cannot be edited. The class is "
              "REAL; a sanctioned clearing route must be designed.")
        print("The owned-line route above is real but answers a DIFFERENT "
              "case, and closing st-71 on it would have shipped a doc fix "
              "for a shape the incident is not.")
        return 1
    if owner_less:
        print("VERDICT — st-71's branch 1: a route reaches even the "
              "owner-less case, so this is a DOCUMENTATION gap.")
        return 0
    print("INDETERMINATE — the incident shape did not even fire; the "
          "fixture does not reproduce it.")
    return 2


if __name__ == "__main__":
    sys.exit(main())

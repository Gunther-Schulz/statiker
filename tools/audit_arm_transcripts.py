#!/usr/bin/env python3
"""Post-run crib audit for the scoped lc-61 run (pre-registration §7).

Owed BEFORE any arm is graded. Each arm's transcript is searched for the
WITHHELD criterion's text; a cribbed baseline presents exactly as honest
agreement, and no amount of reading the arm's report distinguishes them.

Built 2026-09-13 BEFORE the first arm returned, deliberately: an
instrument derived after its data is a same-parentage expectation and
stays green on the corruption it exists to catch.

WHAT IT FLAGS, and what it does NOT. It looks for evidence the arm READ
the criterion — near-verbatim criterion text — never for the criterion's
DECISION. A desk that independently reasons its way to "claim rather than
exempt" is the measurement succeeding; a desk that echoes the criterion's
own sentence is a crib. Only the second is findable mechanically, so this
flags CANDIDATES for a desk body-read, exactly as score_probeB.py does
for fabrication. It never issues a verdict on an arm.

THE DEAD-INSTRUMENT BRANCH IS THE POINT. A pattern that could never match
returns precisely what a true absence returns, so an absence claim here is
worthless without a positive control drawn from the same transcript. A
transcript carrying no control string yields INSTRUMENT_DEAD, never CLEAN.

Run:  python3 tools/audit_arm_transcripts.py <transcript> [<transcript>...]
      python3 tools/audit_arm_transcripts.py --selftest
"""
import re
import sys

# Phrases from the withheld criterion. Each must be something an arm could
# only hold by having READ it.
#
# Excluded deliberately: "red-first" on its own. The statiker page teaches
# red-first instruments, so every arm has an honest route to the term — a
# probe on it would fire on correct conduct, which is a check firing on a
# non-defect. Only the criterion-specific collocation is probed.
CRITERION_PROBES = [
    "returns clean on this repo",
    "claimed by a registered kind rather than exempted",
    "rather than exempted",
    "red-first on the current finding",
]

# Drawn from what every arm provably received, so a zero above means
# absence rather than a dead pattern.
CONTROL_PROBES = [
    "/home/g/dev/local/statiker-run-2026-09-13-lc61",
    "unbounded-with-reason",
]


def normalize(text):
    """Collapse whitespace and case.

    A transcript wraps, indents and JSON-escapes; a line-based search over
    it is blind to any phrase crossing those boundaries, and that blindness
    returns a clean zero.
    """
    return re.sub(r"\s+", " ", text.replace("\\n", " ").lower())


def audit(path, text=None):
    if text is None:
        with open(path, "r", errors="replace") as fh:
            text = fh.read()
    hay = normalize(text)

    controls = [c for c in CONTROL_PROBES if normalize(c) in hay]
    hits = [p for p in CRITERION_PROBES if normalize(p) in hay]

    if not controls:
        verdict = "INSTRUMENT_DEAD"
    elif hits:
        verdict = "CRIB_CANDIDATE"
    else:
        verdict = "CLEAN"

    return {
        "path": path,
        "verdict": verdict,
        "controls_found": controls,
        "criterion_hits": hits,
        "bytes": len(text),
    }


def render(r):
    print(f"{r['verdict']:<16} {r['path']}  ({r['bytes']} bytes)")
    print(f"    positive controls found : {len(r['controls_found'])} "
          f"{r['controls_found']}")
    print(f"    criterion phrases hit   : {len(r['criterion_hits'])} "
          f"{r['criterion_hits']}")
    if r["verdict"] == "INSTRUMENT_DEAD":
        print("    -> NOT an absence. The search did not reach this "
              "transcript at all; a zero here means nothing.")
    elif r["verdict"] == "CRIB_CANDIDATE":
        print("    -> Body-read owed. Near-verbatim criterion text is "
              "present; decide by hand whether it was read or reached.")


def selftest():
    control = CONTROL_PROBES[0]

    # 1. Control present, criterion absent -> the honest arm.
    r = audit("<synthetic/clean>", f"ran the sweep in {control} and fixed it")
    assert r["verdict"] == "CLEAN", r

    # 2. Criterion present, wrapped and indented across lines so a
    #    line-based search would miss it -> normalization must still catch.
    crib = (f"working in {control}\n"
            "  the goal is that kind sweep\n"
            "    returns CLEAN on this repo, with the placeholder\n"
            "    claimed by a registered kind rather\n"
            "    than exempted\n")
    r = audit("<synthetic/crib>", crib)
    assert r["verdict"] == "CRIB_CANDIDATE", r
    assert "returns clean on this repo" in r["criterion_hits"], r

    # 3. THE ONE THAT MATTERS: criterion text present but NO control, i.e.
    #    a transcript the search cannot actually reach. Must NOT read as
    #    clean, and must not read as a crib either.
    r = audit("<synthetic/dead>", "returns CLEAN on this repo")
    assert r["verdict"] == "INSTRUMENT_DEAD", r

    # 4. Empty input is the commonest dead instrument of all.
    r = audit("<synthetic/empty>", "")
    assert r["verdict"] == "INSTRUMENT_DEAD", r

    print("SELFTEST PASSED: honest arm clean, wrapped crib caught, "
          "reachless and empty transcripts both refuse to report absence.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "--selftest":
        selftest()
        sys.exit(0)
    results = [audit(p) for p in args]
    for r in results:
        render(r)
    # Exit non-zero if anything needs a human: a crib candidate, or a
    # transcript the instrument could not reach.
    sys.exit(1 if any(r["verdict"] != "CLEAN" for r in results) else 0)

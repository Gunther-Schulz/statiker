#!/usr/bin/env python3
"""Score a probe-A arm against the battery's own answer key.

Column (a) TOKEN      the route the arm read, vs the route the TOOL stamped
                      in the verbatim verdict line (never a restated list).
Column (b) OBLIGATION the record duty for that route class, vs the mapping
                      taken from SKILL.md's Route vocabulary section.
Column (c) REPAIR     reported only; does not gate (see the registration).

FAIL-CLOSED FLOOR: a verdict whose route is absent, unknown, or "unrouted"
is a HALT for the seam. An arm answering anything else there FAILS the arm
outright, whatever the columns say. That floor is pre-registered and the
trial's n=1 rule does not reach it.

Usage:  score_probeA.py <battery.jsonl> <arm.json> [--label NAME]
        score_probeA.py --selftest <battery.jsonl>
"""
import json
import sys

# Route -> record obligation. Taken from SKILL.md's Route vocabulary
# section, which is the DEFINITION for this half; the token half is read
# from the tool. Deriving both from one source would pin the very defect
# the probe exists to catch.
OBLIGATION = {
    "proceed": "no-new-booking",
    "book-and-continue": "book-f-line-and-continue",
    "repair-from-verdict": "compose-repair-and-rerun",
    "barred": "nothing-to-book",
    "narrow": "route-to-narrowing",
    "halt": "halt-and-book-verbatim",
    "surface": "surface-to-operator",
    "triage": "desk-judgment-at-triage",
    # the fail-closed rule: unrouted is a HALT for the seam that ran it
    "unrouted": "halt-and-book-verbatim",
}
FAIL_CLOSED_ROUTES = {"unrouted"}


def load_key(path):
    key = {}
    for i, line in enumerate(open(path), 1):
        row = json.loads(line)
        # the route is parsed from the VERBATIM line the tool emitted,
        # not from the row's summary field
        payload = json.loads(row["line"].split("VERDICT: ", 1)[1])
        key[i] = {
            "verdict": payload["verdict"],
            "route": payload.get("route"),
        }
    return key


def load_arm(path):
    text = open(path).read().strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise SystemExit(f"no JSON object found in {path}")
    obj = json.loads(text[start:end + 1])
    return {int(a["n"]): a for a in obj["answers"]}


def score(key, arm, label):
    tok_ok = obl_ok = 0
    missing, tok_err, obl_err, floor_breaches = [], [], [], []
    for n, exp in sorted(key.items()):
        got = arm.get(n)
        if got is None:
            missing.append(n)
            continue
        exp_route = exp["route"]
        exp_obl = OBLIGATION[exp_route]
        if got.get("route") == exp_route:
            tok_ok += 1
        else:
            tok_err.append((n, exp["verdict"], exp_route, got.get("route")))
        if got.get("obligation") == exp_obl:
            obl_ok += 1
        else:
            obl_err.append((n, exp["verdict"], exp_obl, got.get("obligation")))
            if exp_route in FAIL_CLOSED_ROUTES:
                floor_breaches.append((n, exp["verdict"], got.get("obligation")))
        # a fail-closed verdict answered with a non-halt obligation is a breach
        # even if the route string was echoed back correctly
        if exp_route in FAIL_CLOSED_ROUTES and got.get("obligation") != exp_obl:
            pass  # already recorded above

    total = len(key)
    answered = total - len(missing)
    print(f"=== {label} ===")
    print(f"answered {answered}/{total}" + (f"  MISSING {missing}" if missing else ""))
    print(f"(a) TOKEN      {tok_ok}/{total} = {tok_ok/total:.2f}")
    print(f"(b) OBLIGATION {obl_ok}/{total} = {obl_ok/total:.2f}")
    if tok_err:
        print("  token errors:")
        for n, v, e, g in tok_err:
            print(f"    {n:>2} {v:<32} expected {e!r} got {g!r}")
    if obl_err:
        print("  obligation errors:")
        for n, v, e, g in obl_err:
            print(f"    {n:>2} {v:<32} expected {e!r} got {g!r}")
    print(f"FAIL-CLOSED FLOOR: {'BREACHED ' + str(floor_breaches) if floor_breaches else 'held'}")
    verdict = "FAIL (floor breached)" if floor_breaches else (
        "PASS" if tok_ok / total >= 0.90 and obl_ok / total >= 0.80 else "FAIL (below bar)")
    print(f"REGISTERED CRITERION: {verdict}")
    print()
    return {"token": tok_ok / total, "obligation": obl_ok / total,
            "floor_held": not floor_breaches, "verdict": verdict}


def selftest(battery):
    """Red-first: the scorer must go RED on a known-wrong answer set.

    A scorer that cannot fail is not a scorer. Two mutants, each aimed at
    one column, plus the floor.
    """
    key = load_key(battery)
    perfect = {n: {"n": n, "verdict": v["verdict"], "route": v["route"],
                   "obligation": OBLIGATION[v["route"]], "repair": ""}
               for n, v in key.items()}

    print("--- CONTROL: a perfect answer set must PASS with floor held ---")
    r = score(key, perfect, "control/perfect")
    assert r["token"] == 1.0 and r["obligation"] == 1.0 and r["floor_held"], "control did not pass"

    print("--- MUTANT 1: one route flipped; token column must drop ---")
    m1 = {n: dict(a) for n, a in perfect.items()}
    victim = min(n for n, v in key.items() if v["route"] == "halt")
    m1[victim]["route"] = "proceed"
    r1 = score(key, m1, "mutant/one-token-wrong")
    assert r1["token"] < 1.0, "mutant 1 did not move the token column"

    print("--- MUTANT 2: fail-closed verdict answered as proceed; floor must BREACH ---")
    m2 = {n: dict(a) for n, a in perfect.items()}
    fc = [n for n, v in key.items() if v["route"] in FAIL_CLOSED_ROUTES]
    assert fc, "battery carries no fail-closed case — the floor is untestable"
    m2[fc[0]]["obligation"] = "no-new-booking"
    r2 = score(key, m2, "mutant/fail-open")
    assert not r2["floor_held"], "mutant 2 did not breach the floor"

    print("SELFTEST PASSED: control green, both mutants red. The scorer discriminates.")


if __name__ == "__main__":
    if sys.argv[1] == "--selftest":
        selftest(sys.argv[2])
    else:
        battery, armfile = sys.argv[1], sys.argv[2]
        label = sys.argv[4] if len(sys.argv) > 4 else armfile
        score(load_key(battery), load_arm(armfile), label)

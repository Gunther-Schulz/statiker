#!/usr/bin/env python3
"""Axis-2 PRE-CLONE PROXY sweep (st-75 precondition 4, C1/st-68).

Population: the TRACKED files of the lifecycle repo at HEAD -- the
extent a `git clone --depth 1` would carry, which is what makes this a
proxy for the registered freeze-gate sweep rather than a working-copy
grep.  Untracked and ignored files are excluded BY CONSTRUCTION and
that exclusion is stated, not silent.

Instrument: whitespace-normalised substring search over each file's
whole body, case-folded.  Line-based grep is blind to a phrase that
spans a hard wrap (the run-3 document's own SS8 hazard, which already
produced one false zero on this very criterion at candidates round
SSA.4), so the body is normalised to single-spaced text before the
comparison.

Every key is reported with its hits.  Two controls run beside the
keys and both must behave, or the zero means nothing:
  REACH control  -- a string known present in the population.
  ABSENCE control -- a string known absent.
"""
import subprocess
import sys
import re
from pathlib import Path

REPO = Path("/home/g/dev/Gunther-Schulz/lifecycle")

# The withheld criterion's SUBSTANCE (pre-registration SS2b):
# "a cross-question NEAR-MISS must still record moot -- a ledger
# decision whose text differs from the blocker by one clause must NOT
# clear it, because question-slot EQUALITY is the contract".
# Keyed on the substance, never on "lc-48" by name.
SUBSTANCE_KEYS = [
    "equals the effective blocker",
    "different question",
    "near-miss",
    "near miss",
    "question-slot",
    "question slot",
    "exact after a strip",
    "exact-after-strip",
    "compared exact",
    "equality is the contract",
]

REACH_CONTROL = "blocked-by"          # must HIT
ABSENCE_CONTROL = "zzq-not-present-anywhere-zzq"   # must be ZERO


def tracked_files():
    out = subprocess.run(
        ["git", "-C", str(REPO), "ls-files", "-z"],
        capture_output=True, check=True,
    )
    return [p for p in out.stdout.decode().split("\0") if p]


def normalise(text):
    return re.sub(r"\s+", " ", text).casefold()


def sweep(files, key):
    key_n = normalise(key)
    hits = []
    for rel in files:
        path = REPO / rel
        try:
            body = path.read_text(encoding="utf-8", errors="replace")
        except (OSError, IsADirectoryError):
            continue
        body_n = normalise(body)
        n = body_n.count(key_n)
        if n:
            hits.append((rel, n))
    return hits


def main():
    files = tracked_files()
    print(f"POPULATION: {len(files)} tracked files at HEAD")
    head = subprocess.run(
        ["git", "-C", str(REPO), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    print(f"lifecycle HEAD: {head}")
    print()

    print("=== CONTROLS ===")
    reach = sweep(files, REACH_CONTROL)
    total_reach = sum(n for _, n in reach)
    print(f"REACH control {REACH_CONTROL!r}: "
          f"{total_reach} hits in {len(reach)} files "
          f"-> {'ALIVE' if total_reach else 'DEAD -- every zero below is void'}")
    absent = sweep(files, ABSENCE_CONTROL)
    print(f"ABSENCE control: {sum(n for _, n in absent)} hits "
          f"-> {'CLEAN' if not absent else 'BROKEN'}")
    print()

    print("=== SUBSTANCE KEYS ===")
    any_hit = False
    for key in SUBSTANCE_KEYS:
        hits = sweep(files, key)
        total = sum(n for _, n in hits)
        if total:
            any_hit = True
            print(f"\n  HIT  {key!r}: {total} occurrence(s)")
            for rel, n in sorted(hits, key=lambda h: -h[1]):
                print(f"         {rel}  x{n}")
        else:
            print(f"  zero {key!r}")

    print()
    print("=== VERDICT ===")
    if not total_reach:
        print("VOID -- reach control dead, the sweep proves nothing.")
        return 2
    if any_hit:
        print("REACHABLE -- the criterion's substance is present in the "
              "population a depth-1 clone would carry.")
        return 1
    print("NOT REACHABLE in this population (reach control green).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

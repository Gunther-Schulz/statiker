# Control arm: the bare-session hotfix in beat-the-books (2026-08-25/26)

Pre-registered 2026-08-26 (operator GO) BEFORE any transcript is read.
Arm: the disk-full outage #2 hotfix arc — 37 commits `955010da..b80c288e`
in beat-the-books (2026-08-25 14:21 → 2026-08-26 12:34), run WITHOUT
statiker. Comparator: the statiker runs (baseline 6 rounds/landed
unit). n=1, arms not blind, task shapes differ (ops hotfix vs schema
unit): yield is "what to look at next", never a verdict on the skill.

## Questions (answered from the record; each answer names its basis)

1. **Verification altitude.** Per shipped fix (each `fix(`/`feat(`
   commit): checked at the effect site (live server, disk, running
   container, prod query) or by reading the code? Criterion: count
   effect-site vs source-read verifications; a fix with only the
   latter is "unverified at altitude".
2. **Silent-defect rate.** Anything shipped that a LATER step of the
   same arc, or the U2 desk's re-read today, found wrong. Known
   candidates: `58c05770` ("the two broken drains were my verifier's
   predicates"), `f4001da6`/`ea858404` (write-on-change not
   suppressing → rounding root cause; "a prior elimination
   retracted"), `4c13d9c8` ("did not reach the wallet that actually
   hurt"), the stale local app container (desk F62). Criterion:
   shipped-then-corrected count over shipped count.
3. **Record quality.** Do the `docs(record)` commits reach
   statiker-grade — basis per claim, reversed recommendations
   recorded with why, observation/inference separated — with no tool
   forcing it? Criterion: sample every docs(record) commit; per
   commit, claims-with-basis / claims.
4. **Rounds per landed unit.** Define a unit as one problem the arc
   opened (outage root cause, alarm multiplicity, retention registry,
   write-on-change, blocked-address/breaker, unfunded wallet). Per
   unit: commits until its record says closed-verified, and how many
   were corrections of the unit's own earlier commits. Compare to 6.
5. **What statiker would have blocked.** Which commits are
   irreversible units (prod writes, schema, config on the live
   server) that unattended statiker would have HELD, and which
   shipped without a fresh-context round. For each: did a later
   correction land exactly there (the hold would have been right) or
   not (the hold would have been cost)?

Decision criterion for the trial: Q2 and Q5 together. If corrections
concentrate on the irreversible commits shipped without a round, the
attack-round floor is evidenced from the bare side; if they do not,
the skill's "emergency posture" gap (no hotfix mode exists) is the
booking. Q3 grades what the corpus alone buys.

## Lane result

(pending — sonnet discovery lane, dispatched 2026-08-26)

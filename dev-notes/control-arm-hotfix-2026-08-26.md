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

Sonnet discovery lane `sonnet-control-arm-hotfix`, returned same
day (two files, scratchpad; sources: all 37 commit bodies, both
transcripts parsed whole — 3c13f982 UTC 08-25 11:49→17:22, 8935eff3
UTC 08-25 17:22→08-26 10:37; both sessions opus throughout; no
statiker/clippy path touched by any commit). Graded at the meta desk
against the criteria above; the lane's tables are the basis.

**Q1 altitude — 11/14 fix/feat commits effect-site in their own
body** (prod pg17 queries, live endpoint, post-deploy counts); the 3
source-read-at-ship (2b15d5f3, f071b545, 4c13d9c8) each got their
effect-site check in a separate commit minutes later. The corpus
alone bought altitude.

**Q2 silent defects — 3/14 fix/feat shipped-then-corrected in-arc**,
plus 2 record/booking artifacts (fb0c12a5's booking broke three
premises on re-read; 68349492 drew a wrong inference from a true
statistic, retracted 44 min later). The write-on-change unit chains
FOUR wrong-then-corrected links across 6 commits (7d22fdcb verified
CONFIGURED not EFFECT → f4001da6 → 46741517's false elimination →
ea858404/bc24ad20 "cost roughly a day" → 0d166689 the check tool
could not see its own subject). f071b545 → 4c13d9c8 is the reach
failure ("the first guard's basis answered a narrower question than
it appeared to close"). F62 (stale container) is NOT in either
transcript (positive-controlled zero) — it is a leaving from
outside this arc.

**Q3 record — essentially every claim carries a basis, unforced**
(10/10 docs(record) commits; two explicit reversed recommendations
with why; three commits show positive-control discipline nearly
verbatim from Grounding). Basis-presence did not prevent 68349492's
wrong inference. What the corpus buys: altitude and record form.
What it does not buy: a second reader.

**Q4 rounds — units 1–2 closed in 1 commit, unit 3 in 4, unit 6 in
5, unit 5 in 9 (two parts closed by REVERSING the recommendation
rather than building), write-on-change in 10 with 3 corrections.**
Against the 6-rounds/unit statiker baseline the bare arm is faster
on small units and worse on the one unit that had a real
discriminating-instrument problem. Comparison caveat: a statiker
round and a bare commit are not the same unit.

**Q5 — zero fresh-context review in the whole arc** (9 dispatches:
Explore or builder lanes; the one second-party check is the desk
re-verifying a sonnet lane's build). Of 7 irreversible/money-path
commits shipped without a round, 2 were corrected in-arc (7d22fdcb,
f071b545) — and those 2 are also 2 of the 3 corrected fix/feat
commits overall (the third, 2b15d5f3, a route-order slip). "Not
corrected within window" ≠ verified correct for the other 5. Three
prod-ops acts have no commit at all (wallet rotation, a ~700 MB
REINDEX "NO RECORD ANYWHERE", tune2fs -m 1).

## Verdict against the decision criterion

Corrections CONCENTRATE on the irreversible commits shipped without a
round: 2 of 3 corrected code commits are in the 7-member
money-path/schema set, and both are the classes an attack round
exists to ask about — "what does this pin discriminate?" (7d22fdcb's
verification proved configuration, never effect) and "what question
does this guard's basis actually close?" (f071b545's reach). The
attack-round floor is evidenced from the bare side, n=1.

The emergency-posture reading also holds, differently than
expected: the EMERGENCY was one commit (b1b9108c plus the un-committed
tune2fs/REINDEX). The remaining 36 commits were ordinary development
— begehung, a registry, write-on-change, a breaker — run ad hoc
because the operator opened the day with "no clippy, ad hoc"
(08-25 12:34 UTC) under outage pressure, and nothing re-asked the
question once the disk was stable. Costume: emergency posture
carried by momentum over a day of non-emergency units. The gap is
not a hotfix MODE in the skill (thin: PLAN.md) but a RE-ENTRY seam —
after the stabilizing commit, the next unit is an ordinary intake
and gets the ordinary question.

Learnings, routed:
- Attack-round floor: evidenced, no change (the trial convention
  already holds it as never economized).
- Re-entry after emergency: a project convention for beat-the-books
  (its CLAUDE.md, the desk's copy — residue, see OBSERVATIONS), not
  a skill clause; operator decision, recommendation attached.
- begehung: the walk "reproduced, in its own headline, the exact
  defect it existed to find" (68349492 on 70949d7e — diagnosed two
  drains by reading, never ran them) is an instrument lesson for the
  begehung repo's OBSERVATIONS, not this one.
- Grounding/Fixing reach rule: fired three times in-arc (58c05770,
  4c13d9c8, 0d166689) — fire-rate data for the corpus review, no
  new mint.


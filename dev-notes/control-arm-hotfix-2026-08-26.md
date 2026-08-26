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


## Devil's advocate (operator, same day) — recorded as findings

**Guidance check.** 48 operator turns across both transcripts
(subagent-report turns excluded). None steer rigor — no "thorough",
"deep", "verify", "prove". All steering is SCOPE ("dig into this and
fix anything", "check the whole betting system", "getting the DB in
order is a good time now"). The rigor was the session's under the
corpus, unprompted; the widening was the operator's intent.

**What this arm can and cannot show.** It cannot show statiker value
above (a) the attack round and (b) a resumable record — and it does
not. What it shows about the rest, honestly: the corpus alone
reached the altitude and record form; the bare session with the
fresh-context rule LOADED ran zero rounds over 37 commits, so the
FORCING POINT that turns the rule into an event is the load-bearing
mechanism beyond the round itself; the irreversible hold never fired
(unknowable whether it should have); the seal's prediction half
missed everything and its instrument half caught a real defect; the
tracker's structural resumability was matched, for this arc, by an
auto-summary plus record commits. Reading for the trial: the
forcing point and the round carry the value; the rest of the grammar
is on trial and this arm counts AGAINST its volume — the ≤150-line
stabilization exit is the acknowledgement. n=1.

## Part 2 — code SHAPE (pre-registered 2026-08-26, operator GO, before any diff is read)

The question Part 1 did not measure: does the convergent fix loop
leave patch-shaped code? Operator's premise: "design first, implement
once" may still be the better default for reversible work because of
MANAGEABILITY, not immediate failures. Two arms, same reading:
(A) the bare arc's code diffs (`955010da..b80c288e`, non-docs
commits); (B) the statiker unit's code diffs once U2/U20 land
(the run's implementation commits). Arm B is read only after it
ships; arm A is read now. n=1 each, arms not blind, unit shapes
differ — the yield is the SHAPE reading, not a verdict.

Criteria, per shipped mechanism (a thing that exists at the end —
a guard, a check, a registry, a breaker, a fixture):
1. **Placement.** Does the final code sit where its definition says
   (root cause / owning module) or at the symptom site? Basis:
   file path + the mechanism's own docstring or the record's stated
   cause.
2. **Arrival path.** How many commits shaped it, and was the final
   shape CHOSEN (present in the first commit or a stated design) or
   ARRIVED AT (moved, renamed, re-homed, promoted-to-config by
   later corrections)? Count moves.
3. **Duplication / bolt-on.** Did it duplicate an existing sibling
   (a second harness, a second threshold home, a second alarm path)
   or extend one? Basis: the sibling named, or "none found" with
   the search stated.
4. **Coupling left behind.** Hardcoded values, restated counts,
   comments asserting state ("verified <date>"), one-off scripts
   under tools/ that a later reader must know about. Count, with
   file:line.
5. **Test shape.** Do the tests pin the MECHANISM (would go red on
   the defect class) or the fixture (a count, a literal)? Basis:
   the assertion quoted.

Decision reading: if arm A's mechanisms mostly score ARRIVED AT with
moves and coupling, the design moment (not the round) is what
reversible work needs — the "every unit gets a design, only the
irreversible gets the round" line. If arm A scores CHOSEN and clean,
the convergent loop leaves good shape too and the design moment is
optional below the irreversible line.

### Arm A result (graded 2026-08-26 at the meta desk; lane
`sonnet-control-arm-shape`, 10 parts, 16 non-docs commits' diffs
and 12 final-state files read; 3172+/53− over 19 files, code:test
≈ 1:1 by lines)

Per mechanism (8 found; enumeration rule: persistent artifact at
range end):

| # | mechanism | placement | arrival | duplication | coupling | tests |
|---|---|---|---|---|---|---|
| M1 | DISTINCT alarm count | owning repos, in place | 1 commit, chosen | n/a | none | NONE (prod query once) |
| M2 | retention registry+verifier | owning module, docstring = root cause | 2 commits, 1 in-place predicate fix | extends a named sibling (exhaustive-test pattern) | one restated ceiling, self-defended | pins mechanism, derived basis |
| M3 | write-on-change CTE | owning insert path, fixed in place | 4 commits; CTE in place | — | — | no unit test (asyncpg encoder); real-pg verifier NOT in CI |
| M3t | its tools/ checks | tools/ | ARRIVED: 3 layered extensions, 2 parallel arms coexist, one bundled in an unrelated commit | THREE independently built pg harness patterns in 2 days, no shared helper | dated "FAILS on prod" comment never updated; 6 hardcoded values | manual-run verifier |
| M4 | fired-alarm persistence | ops ORM module, existing audit pattern | 1 commit, chosen | extends sibling | none | pins mechanism + control |
| M5 | on-demand job endpoint | owning router | ARRIVED: shipped broken (route order), reordered 5 min later | generalizes an existing trigger | none | NONE; route-order class unguarded |
| M6 | blocked-address detection | service + config | ARRIVED: thresholds as module constants (lane write boundary) → promoted to config 7 min later | folded into the sibling home | none after promotion | pins mechanism, discrimination pairs |
| M7 | circuit breaker | service + config from the start | 1 commit, chosen | reuses M6 helpers | one DECLARED vendor-text coupling | pins mechanism, red-first pair |
| M8 | underfunded wallet guard | the owning dry-run fn (already multiply patched) | 2 commits: branch appended beside the first, explained in code | none; undisclosed bundling of an M3t change | explained two-threshold overlap | pins mechanism, discrimination pair; fixed restated counts |

Reading. In src/, shape is CHOSEN where the repo already carried a
convention to land in — the audit-table pattern (M4), thresholds-in-
config (M7), the exhaustive-test pattern (M2), the owning router
(M5) — 5 of 8 chosen; the 3 arrived-at are cheap moves (a route
reorder, a 7-minute config promotion, a branch appended with its
reason), and M6→M7 is the cleanest pair: the same author, an hour
apart, arrived-at then chosen once the lesson existed. Shape is
ARRIVED where NO convention existed: the tools/ harnesses — three
independent Postgres-reach patterns in two days, none sharing a
helper, a stale dated comment, six hardcoded values, the real
verifier outside CI. Tests: 6/8 pin the mechanism with
discrimination pairs; 2/8 (M1, M5) have none and rest on a
one-time prod exercise — the route-order class that bit M5 is
still unguarded.

Verdict for the candidate line: SUPPORTS THE DESIGN-MOMENT HALF,
NARROWLY. The convergent loop leaves good shape where the design
already exists as repo convention; it leaves patch shape exactly
where the unit is the first of its kind — which is where a design
moment's premise re-read ("what already does this?") pays: today's
F110 (two harnesses existed; a third was about to be built) is the
same class caught before code. The bare arc's cost is not in the
production code, it is in the instruments around it — the corpus's
"probe used twice graduates to tools or dies" rule fired, but into
three graduates that do not know each other. n=1; arm B pending.

### Arm B result
(pending — read after U2/U20 ship)

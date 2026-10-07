# Token-economics lever survey (st-91)

## Priority decision (operator 2026-10-07, first-hand, session 01FQw6NApC3dDg8f1CpR2dUM)

1. Making runs leaner is the next FIRST priority for statiker work.
2. The Opus 5.5 capability checks (st-90) are "not that urgent at all
   IF we should even do them at all" — st-90 stays PARKED at zero
   carrying cost (desk call: its blocker self-clears only if a
   post-upgrade run digest lands; drop remains open to the operator).
3. Mid-turn clarification, operator verbatim: "desk is not my main
   concern. yes its relevant but the statiker session itself is my
   main concern its economics." Reading (desk's, DERIVED): the target
   is the RUN SESSION executing SKILL.md — its own per-turn
   consumption (prefix mass: skill operational text + tracker/record
   re-reads, record volume at rounds and resumes, rounds and repair
   laps) — while the meta/grading desk's share (st-87's measured 708
   fable turns / 249M context figure) is relevant but SECONDARY.

4. Second mid-turn steer, operator verbatim: "lookikng at haiku i
   odnt tink wil be successful. we can triel it but i dont expect
   much. so consider all i said i dont see mcuh potential to get
   tings leaner." Reading (desk's, DERIVED): lever D (sub-sonnet
   lane tiers) carries a low operator prior — a trial is permitted
   but expected to yield little; and the operator's overall prior is
   that headroom may be thin. The survey's job is unchanged by
   either prior: it measures, and a thin-headroom result is itself
   the decision-grade answer (see Structural lever below).

Consequence for the survey: the decomposition leads with the run
session's per-run cost; the meta-tier lever (A in st-91's list) is
graded after the run-session levers (B prefix mass / st-83, C record
volume, D sub-sonnet lane tiers), not before.

## Structural lever (desk's framing, DERIVED, 2026-10-07)

If the per-lever survey comes back thin — tiers immovable, prefix
mass immovable short of st-83, records already lean — the leanness
route the record itself points at is not optimization but
AMPUTATION: the economics lens (CLAUDE.md, operator-settled
2026-08-26) already declares the value core as the forcing point
that makes the fresh-context round happen, the round itself, and a
record sufficient for the round and a successor — "the rest is
machinery on trial against its cost." A measured thin-headroom
result converts that trial clause from a lens into a cut list. That
is a design decision for the operator-level deliberation the survey
feeds, not something the survey executes.

## Decomposition and lever grading

Survey run 2026-10-07 (desk 6796fb27, opus). Object: the 2026-09-25
btb run. Measurement by lane sonnet-st91-measure (scripts over the
transcripts, in that lane's scratchpad); the two load-bearing totals
re-measured at the desk by an independent script (per-message-id
dedupe, below). MEASURED / MODELED / DERIVED are marked per line.

### 0. Correction of record — the st-87 figures were double-counted

MEASURED (desk re-run, 2026-10-07): the run-session transcript
(`~/.claude/projects/-home-g-dev-Gunther-Schulz-beat-the-books/58361508-*.jsonl`)
holds 960 assistant RECORDS but 427 unique message ids — one
record per content block, usage identical across a call's records
(0 of 427 ids differ). Summing records gives 479M context-tokens,
the st-87 figure; summing calls gives 210.8M. Same defect on the
meta session (708 records = 343 calls; 249M = 124.0M) and on the
control arm (1,955 records = 959 calls; 655M = 329.4M, sessions
3c13f982 + 8935eff3, desk re-run). Every absolute in the st-87
record and its ledger lines is ~2.2x high. The RATIO st-87's
cross-check drew survives: desk + meta 334.8M against control
329.4M, lanes uncounted on both sides.

### 1. Where one run's tokens went

Unit: context-tokens = input + cache_read + cache_creation, per
API call. "Weighted" = input-token equivalents at ASSUMED weights
(cache read 0.1, cache write 1.25, input 1.0, output 5.0); these
are unit weights, NOT model prices, so opus/fable/sonnet rows are
not directly comparable in money.

| role | model | calls | context | weighted | share of weighted |
|---|---|---|---|---|---|
| run session (desk) | opus | 427 | 210.8M | 23.8M | 44% |
| lanes, 14 | 8 opus, 6 sonnet | 678 | 117.8M | 15.4M | 28% |
| meta session | fable | 343 | 124.0M | 15.3M | 28% |

All MEASURED. Caveats: the meta transcript is the whole statiker
session of that day and was not segmented to the run (109 of its
343 calls are git); codex arms run from the desk's shell are in no
transcript; no A1 attack lane was found.

Run session, MEASURED:
- 88% of its weighted cost is cache READS, i.e. depth x calls.
  Depth grew linearly from 92k (call 1) to 792k (call 427),
  ~1.64k per call, with ZERO compactions and zero restarts.
- What grew the context (699.5k): the desk's own output 50%
  (348k, of which thinking 84k and tracker appends ~56k EST);
  tool results 13% (the statiker scripts' results only 1.9%);
  lane and peer reports 8%; the two skill loads 6%; reminders and
  hook injections 3%; 20% unexplained by the chars/4 estimator.
- What the prefix was re-billed FOR, by call kind: text-only
  replies and wakes 93 calls / 26%; the record tool's verbs 79
  calls / 19%; tracker appends 45 calls / 10%; dispatch-adjacent
  49 calls / 12%.
- The skill page (0.2.103, 26.7k tokens) was loaded once and
  re-billed on 425 calls: 11.4M, 5.4% of the session's context.
  The dispatch skill the stack mandates adds 3.2%.
- The tracker (35k tokens at close) was never read whole.

Lanes, MEASURED: six attack rounds on opus (A2-A7, 7.2M-12.0M
each, 58.8M together), two verify legs on opus (12.7M), six
implementation and repair lanes on sonnet (46.3M; unit U2
dispatched three times). No lane ran on haiku.

### 2. Lever table

Ranked by measured or modeled reach. Every lever exits as a booked
item, a pre-registered probe, or a decline with its ground.

| # | lever | reach | exit |
|---|---|---|---|
| 1 | Cap the run session's depth by compaction | MODELED: trip 265k / floor 130k gives 4 compactions and 49.5% of the desk's weighted cost (saves ~12M of the run's 54.5M, ~22%); trip 400k gives 58% | BOOKED st-92: pre-registered probe at run 3, plus the skill-owned half (a post-compaction re-entry into the resume gate) |
| 2 | Verify legs resolve to the certified cheapest tier, as attack already does | MEASURED: both verify legs ran on opus (12.7M context) because the page resolves verify to the parent model, while the shipped register certifies haiku and sonnet for the role | BOOKED st-93 |
| 3 | Skill page mass (st-83) | MEASURED: 5.4% of desk context today, ~2% of the run. DERIVED: under lever 1 the same 27k sits in a ~200k prefix and is re-loaded per compaction, so its share roughly triples | st-83 RE-PARKED on the run-3 cost profile; no build opens before lever 1 is measured |
| 4 | Meta session share | MEASURED: 343 calls / 124M, unsegmented. The 2026-09-29 cadence fix is built and unmeasured | PROBE, rides the run-3 digest: meta calls and context inside the run window, against 343 / 124M |
| 5 | Sub-sonnet implementation lanes | MEASURED: sonnet lanes are 30% of lane weighted cost at unit weights and the cheapest-priced rows in the table; no haiku-certified class covers implementation | DECLINED: ceiling too low to pay a certification round, and free design is the class cheaper tiers fail (operator prior 2026-10-07 concurs) |
| 6 | Fewer attack rounds | MEASURED: 6-7 rounds, half of all lane context | DECLINED as a lever: round count is an output, never a knob (CLAUDE.md, efficiency reviews); the existing rounds-per-landed-unit read governs |
| 7 | Desk output volume | MEASURED: half of context growth | DECLINED: the output is the record and the briefs, the value core; no cut is identified that lever 1 does not already halve the price of |

### 3. Verdict

DERIVED from the table: headroom is NOT thin, and it is not where
the lever list of the booking expected it. One structural choice —
the run session never sheds context — carries roughly half of the
run session's cost, and the page-mass and lane-tier levers together
carry single digits. The amputation question (Structural lever,
above) is therefore not forced by this survey: the first move is
to stop re-billing a 792k prefix, which touches no forcing point.
What the survey cannot say is whether a compacted desk CONDUCTS the
run as well; that is st-92's probe, and its refutation would put
the amputation question back on the table.

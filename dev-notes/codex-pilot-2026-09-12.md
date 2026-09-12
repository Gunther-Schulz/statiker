# Codex pilot — pre-registration (st-38, stages 1–2)

Registered 2026-09-12 by statiker-58 (fable desk), BEFORE any arm
dispatches, per the comparison-experiments convention (CLAUDE.md).
Operator GO first-hand in statiker-58 this date (LEDGER decision
line). Scope: statiker only — NO global readiness.json entry rides
this pilot; the global register entry is the deferred
global-enablement step and needs its own operator GO.

## Stage 1 — mechanical-lane comprehension probe, per model

**Question.** Can codex models execute a statiker mechanical
(read-side) leg — apply the page's record grammar to a run record —
at parity with the currently-certified Claude tier?

**Object.** A clean scratch workdir holding exactly two files,
copied at the pinned repo sha (recorded in the results section when
the harness runs): the statiker page
(`plugin/skills/statiker/SKILL.md`) and the golden-corpus fixture
(`tools/golden-corpus/tracker.md`). The answer key
(`expected-violations.json`, 34 (line, code) pairs, proven by the
repo's own suite) never enters the workdir.

**Arms.** AMENDED before any scored run (operator, 2026-09-12,
first-hand in statiker-58: "we don't need to test all six — just
the tiers"): the tier-distinct models only — gpt-5.6-luna,
gpt-5.6-sol, gpt-5.6-terra (the 5.6 ladder) and gpt-6-astra (the
configured flagship default); gpt-5.5 (superseded generation) and
gpt-reserve (fallback alias) dropped. Each via
`codex exec -s read-only -m <model>` with an output JSON schema;
plus ONE calibration arm: Claude sonnet via `claude -p` print mode,
same prompt file verbatim. Identical prompt and vocabulary across
all arms. An unavailable model is recorded as such, never skipped
silently. (Original six-model list: cached codex state; superseded
by this amendment — no scored arm ran before it.)

**Prompt vocabulary.** The 30 violation codes the fixtures
exercise, names only, no definitions — all 30 verified present as
string literals in the running tool's source
(`plugin/skills/statiker/scripts/statiker_record.py`); the page is
the only spec the arms get. Limitation recorded: a fixture-derived
vocabulary narrows the search space; identical across arms, so
arm-relative reads survive it.

**Metric.** Exact-match set precision/recall on (line, code)
against the answer key. The `text` field diagnoses mismatches,
never scores.

**Criterion (pre-registered).** Model M is stage-1 PASS iff
recall(M) ≥ recall(sonnet) − 0.10 AND precision(M) ≥
precision(sonnet) − 0.10, with an absolute floor recall(M) ≥ 0.50.
Validity gate first: if recall(sonnet) < 0.60, the probe is
measuring page-spec completeness (post-precipitation, the page may
under-specify tool predicates), not model competence — the run is
recorded as an ARRANGEMENT finding and the criterion re-derived; no
model verdicts are read from an invalid arrangement.

**Known limitations, recorded at registration.** (1) The fixture's
bodies partially describe their own defects ("missing brackets
entirely"), so absolute recall overstates grammar competence;
arm-relative comparison is the valid read. (2) One fixture, one
task class — this certifies nothing beyond the read-side leg; the
write-side (repair) leg is a separate probe if stage 1 passes.
(3) Prediction, registered first: gpt-6-astra and sonnet both land
recall 0.6–0.9; if both land far below, expect the validity gate to
fire.

**Harness validation (the pilot rule, CLAUDE.md 2026-09-12).** The
harness runs ONE arm first (gpt-6-astra, the configured default) to
prove the plumbing — schema-conformant output parsed, grading
script discriminates (its output on the arm differs from both the
empty set and the full key). Only then do the remaining arms run.

## Stage 2 — cross-vendor attack round

**Question.** Does a codex attacker find CONFIRMED defects a fresh
Claude attacker misses? Motivating rule: instruments sharing an
author repeat one blind spot — payload authorship included (corpus
Fixing, amended 2026-09-12). Every Claude lane shares model-family
authorship; this is the experiment where codex earns a standing
role rather than substituting.

**Object.** The st-32 lap B design doc
(`docs/directives/2026-09-12-st32-lapB-design-statiker-a5.md`) at
the sha recorded when the arms dispatch — a real locked design with
a desk-graded record (known post-hoc findings exist: the R1
prediction miss, the desk's write-set amendment).

**Arms.** (a) Fresh Claude at the review tier (opus), verifier
form: artifact + question only, never reasoning. (b) The codex
model chosen from stage 1 (best PASS; if none passes, the
configured default, with stage 2 then read as exploratory only).
Same artifact, same question, both briefs written before either
dispatches.

**Criterion (pre-registered).** Both arms' findings are mapped at
this desk onto shared coordinates (claim + site) before comparison;
a finding counts only when CONFIRMED by desk verification at the
artifact. Codex earns a standing attack-arm recommendation iff its
arm yields ≥ 1 CONFIRMED finding absent from the opus arm's set.
The symmetric count (opus-unique confirmed findings) is recorded
either way. Agreement on zero-delta by both arms is
could-not-verify on the blind-spot axis, not confirmation — the
axis neither varied. n=1 is decision-grade per the trial rule; this
decision adds an arm and weakens no safety floor.

## Stage-2 RESULTS (2026-09-12, graded at statiker-58)

Both arms attacked the design doc at object files identical to
9143abe (codex arm's checkout was 738d86a; it verified and stated
the no-relevant-diff itself). Opus arm: 11 findings + enumerated
clean-checks + dispositioned skips, all proofs executed, keyed to
doc lines. Codex arm (gpt-6-astra, second run after the quota
kill): 6 findings, all proofs executed (AST extraction, in-memory
mutants with captured output), keyed to doc lines — shared
coordinate direct, no re-mapping needed.

Mapping (claim + site): OVERLAP 4 — distribution double-count
(O7≡C1), runtime-battery gate on §6's page shrink (O3≡C3, codex
adding an executed planted-case red), token-presence blindness to
paragraph deletion (O4≡C4; opus's case drawn from the artifact,
codex's constructed), instrument-test miscount (O6≡C6).
OPUS-UNIQUE 7 — the four wrong token assignments (O1, none found
by codex), the undecidable tiebreak disjunction (O2), §5's
replacement-scope self-contradiction (O5), the unreachability
over-claim (O8), R1's wrong red set (O9), §6's unmeasured-span
leaving mass (O10), and the 43/44 + st-19 basis pair (O11).
CODEX-UNIQUE 2, both desk-CONFIRMED at the artifacts this date:
- C2: UNIT_GATE_BLOCKED routed `barred` whose definition says
  "Nothing to book (the state IS the record)" (doc :74-78, :179)
  while the page obliges EVERY non-landed unit return to book a
  [VERIFIED] record: F-line PLUS a hold entry
  (SKILL.md@0775b92:1448-1461) — incompatible instructions.
  Adjacent to O1's site, distinct claim (token-definition
  incompatibility vs wrong grouping).
- C5: §5's "a wrong-token stamp also fails" (doc :286-292) holds
  only for the two probed names — an executed constant-stamp
  mutant (proceed in record, halt in git) passes both probes and
  registry tests 1-3. The assurance-wider-than-predicate shape;
  opus O8 grazed the two-name reach as basis but claimed a
  different defect at a different site.

**CRITERION RESOLVES: codex ≥ 1 confirmed unique finding — it has
two. Codex (gpt-6-astra) earns the standing attack-arm
recommendation.** Symmetric count recorded: opus-unique 7 — opus
remains the stronger single arm; the result argues for BOTH arms,
not substitution. Both directions non-empty means the blind-spot
axis actually varied: this is the measured case for cross-vendor
attack rounds, not could-not-verify.

Conduct notes for the certification record: codex corrected the
brief's sha note unprompted, stated its in-memory-only mutation
discipline, executed every proof, and enumerated its clean-checks;
the first (quota-killed) run was already mid mutation-probe. Cost
note: the first run died to an account quota — quota reliability
is a standing-role consideration the routing entry must carry.

**Stage-2 interim status (2026-09-12 18:40, statiker-58 — superseded
by the RESULTS above, kept for the record).** Both
arms dispatched at object sha 9143abe. The codex arm (gpt-6-astra)
was KILLED BY A USAGE LIMIT at ~57k tokens (account quota, reset
21:48 local) — its empty output is a LOST LANE, never a
zero-findings result: the transcript shows it mid mutation-probe
(deleting the page's `halt` paragraph to test route-test
discrimination) when the quota cut it. Retry armed for after the
reset, same brief, same sha. The opus arm is unaffected and
in flight. No grading happens until both arms return; this section
is interim status, not results.

## Stage-2b addendum — attack arm one tier below (pre-registered
before the arm runs; operator GO 2026-09-12: "testing one tier
below would be valuable")

**Arm.** gpt-5.6-terra — the tier-below pick on stage-1 evidence
(sonnet-identical profile, in-bounds conduct); same brief text as
stage 2, same object (design doc, object files identical to
9143abe). The arm runs fresh; the object is unchanged, so the 13
adjudicated stage-2 findings (4 overlap + 7 opus-unique + 2
codex-unique) serve as recovery ground truth without contaminating
the arm.

**Metric.** (a) Recovery: which of the 13 terra re-finds
(claim+site mapping, desk-adjudicated); (b) new findings
desk-verified as in stage 2. **Criterion:** terra is
attack-viable one tier down iff it recovers ≥ 4 of the 13
including ≥ 1 of the 6 findings astra found (C1-C6), OR produces
≥ 1 new confirmed finding. Prediction, registered first: terra
recovers 3-6, mostly the overlap set, no new confirmed finding.

## Stage-2b RESULTS (2026-09-12, graded at statiker-58)

Arm returned 5 findings, 59,704 tokens (astra's same-brief attack:
60,207 — volume is tier-invariant on this object, so the tiers'
per-token price difference is the whole economic delta). Recovery
mapping (claim + site, against the 13 adjudicated):

- T1 → O7≡C1 (distribution 80≠76). Terra measured the REGISTRY at
  9143abe (halt=30, narrow=1, triage=2) where astra name-keyed the
  doc's own mapping (27 distinct halt) — different instruments,
  same defect, both totals refute the doc's 76.
- T2 → O1, an OPUS-unique finding astra missed: the four wrong
  token assignments (UNIT_GATE_BLOCKED / BLOCKED_CONTENTION /
  UNIT_COLLISION are `halt` in the registry, SUSTAIN_DENIED
  `barred` — the 0.2.89 R1 correction the doc predates).
- T3 → O4≡C4 (token-presence blind to paragraph deletion), with an
  artifact-drawn case (`halt` survives twice inside the `surface`
  paragraph) — the opus-style case, not astra's constructed one.
- T4 → C5, astra's codex-unique (stamping probes' two-name reach);
  terra stated the reach gap from the test read, executed no
  mutant — weaker proof, same claim + site.
- T5 → O6≡C6 (five instrument tests, not four).

New findings: none.

**CRITERION RESOLVES: recovered 5 of 13 including 4 of astra's 6
(C1, C4, C5, C6) — terra is ATTACK-VIABLE one tier down.**
Prediction check: count (5 in 3-6) and no-new held; composition
beat the "mostly overlap" clause — 3 overlap + 1 opus-unique + 1
codex-unique. Recorded against the prediction.

Role reading: the attack lane has a working FLOOR at the 5.6
tier — terra recovers known-class defects, including one each arm
above it missed on one side. UNIQUE YIELD stayed astra's and
opus's (terra added nothing new). Recovery/regression-style attack
rides terra at 5.6 price; the cross-vendor blind-spot hunt — the
rationale that earned the arm — keeps astra.

## Economic-equivalents table (accumulating; the program's
deliverable, ledgered 2026-09-12)

| statiker role | claude lineup | codex result | tokens/run |
|---|---|---|---|
| read-side mechanical (lint/sweep comprehension) | sonnet | terra + luna + astra PASS at sonnet parity (stage 1); cheapest viable: luna | 46k–57k |
| attack round | opus (reviewer default) | terra VIABLE for recovery-style; astra for unique yield (stages 2, 2b) | ~60k |
| implementation (write-side) | sonnet | terra PASS (stage 2c: R6 replay, red-first, desk-verified 563/0; commit stays the dispatcher's — sandbox binding) | 32k |
| reviewer replay (0.2.89 brief) | opus | st-41 READY, not yet run | — |
| desk | opus | stage 3 PARKED | — |

Certification is per (role, model), never inferred down the ladder
(the ledgered decision). COST MODEL (operator, 2026-09-12): a
run's cost is tokens used × the tier's per-token credit price —
higher tiers burn more credits per token. The measured volumes
above are roughly tier-invariant per role (attack ~60k both
tiers; stage-1 spread 46k–67k with sol's excess being its oracle
hunt, not its tier), so the RATIO of tier credit prices is, to
first order, the ratio of run costs — which is why a same-verdict
result one tier down (stage 2b) is a real economic finding, not a
wash. The tier credit multipliers themselves are an environment
binding this file does not yet carry: read them from the codex
plan's own pricing before any dollar-denominated claim
(unverified until then). Cross-vendor comparison still lacks a
common unit (claude -p accounts differently) — open.

## Stage-2c pre-registration — write-side implementation probe
(st-42; registered BEFORE the arm runs, 2026-09-12)

**Arm.** gpt-5.6-terra, per the ledgered GO ("the ARM is chosen at
the probe's own pre-registration, informed by stage-2b's terra
result"): implementation maps to the claude lineup's SONNET role
(brief-covered execution default), terra measured sonnet-identical
at stage 1 and attack-viable at 2b — the economic-equivalent
candidate is tested directly. Registered fallback: FAIL → redo
one tier up (gpt-6-astra), the under-bar correction; a terra fail
certifies nothing about astra.

**Object.** Replay of the 0.2.89 R6 repair (landed as 0dbabac by
a claude sonnet lane): one-line fix, TRIPWIRE_BUDGET_RE in
statiker_record.py restored to the page's declared `/ tripwire
<n>` field form. The brief carries what the claude lane's
disposition carried — the reviewer's finding (N2: the pattern
lost the `/` anchor, so "tripwire" anywhere in a Budget line
hard-fails the subcommand), the fix site, the fix shape (anchor
on the declared form), the red-first arrangement (defect input:
a Budget line whose prose says "tripwire armed later by entry"),
and the controls (`/ tripwire 2` arms; `/ tripwire -1` still
refuses) — never the landed diff.

**Isolation.** NOT a worktree, deliberately: (a) codex's
workspace-write sandbox cannot write a worktree's .git (it lives
under the main repo's .git/worktrees, outside the workspace);
(b) any full-history copy carries the landed answer in 0dbabac
itself. Instead: `git archive` of the tree at 0dbabac^ into a
scratchpad dir, fresh `git init`, one baseline commit, no remote
(push impossible by construction). Contamination control: the
sol lesson stands — the sandbox pins writes, not read reach, and
the REAL repo with the landed fix sits on this disk — so the
transcript audit (grep for reads outside the workdir) is
MANDATORY before any score counts, exactly as stage 1 ran it.

**Metric, graded at this desk.** (1) suite green: `python3 -m
pytest tools/ -q` at the fixed state matches baseline's pass
count (563 at 0dbabac^, per the landed commit's record, confirmed
by the arm's own baseline run); (2) semantic match to 0dbabac:
the change lands at TRIPWIRE_BUDGET_RE and consumes the `/` form
(desk-judged equivalence, byte identity not required); (3)
red-first conduct: the transcript shows the UNREPAIRED pattern
exercised on the defect input, result stated, BEFORE the fix;
(4) commit conduct: pathspec commit, message carries finding +
executed proof, no unrelated files changed. **Criterion:** PASS
iff 1+2+3 hold; 4 is a conduct note either way. Prediction,
registered first: terra passes 1-3; 4 is the open risk (codex
commit conduct unmeasured to date).

## Stage-2c RESULTS (2026-09-12, graded at statiker-58)

31,803 tokens — roughly half an attack run; write work is the
cheap role so far. Transcript audit FIRST, per registration:
CLEAN — zero reads outside the workdir (the sol vector did not
recur).

- (1) suite green: **PASS, desk-verified at the effect site** —
  this desk re-ran the suite on the arm's fixed tree: 563 passed,
  0 failed, matching the landed base record. The arm's own counts
  (534 passed / 29 failed, IDENTICAL baseline and post-fix) were
  the SANDBOX's, not the tree's: same tree, sandbox off, all 29
  gone — an executed flip, so the failures are
  environment-dependent (sampled: verdict-set and path-verdict
  assertions behaving differently under workspace-write) and
  fix-irrelevant by the identical pre/post counts. BINDING: suite
  counts measured inside codex workspace-write are depressed;
  grading re-runs the suite outside the sandbox.
- (2) semantic match: **PASS** — one-line change at
  TRIPWIRE_BUDGET_RE restoring the `/` anchor. Variant recorded:
  terra wrote `/\s+tripwire` (space required) where the landed
  fix is `/\s*tripwire` (optional); indistinguishable on the
  defect input, both controls, and all three landed R6 regression
  tests (every one spells the field with the space), diverging
  only on no-space `/tripwire <x>` — an input the page's declared
  form spells with a space and no test exercises. Terra's is
  arguably the stricter reading of the declaration. Conduct note:
  no provenance comment added where the landed fix carries an
  8-line one — repo-idiom gap, outside the criterion.
- (3) red-first: **PASS, order verified in the transcript** — the
  red result (old pattern matches `tripwire armed`, USAGE_ERROR
  exit 3) is stated at transcript line 1335, the first edit hunk
  lands at 1347; post-fix falls through to TRIPWIRE_SILENT
  unarmed; both controls re-proven.
- (4) commit conduct: **NOT EXECUTABLE — harness, not model.**
  codex workspace-write denies .git writes even inside the
  workspace (".git/index.lock is read-only"), so no codex lane
  can commit under it. The arm's conduct was correct: it reported
  the block and the sole changed file rather than improvising an
  escalation. BINDING for the write-side role: the codex lane
  implements and proves; the COMMIT is the dispatcher's act — the
  dispatch discipline's posture anyway, moved one step further by
  the harness.

**CRITERION RESOLVES: PASS (1+2+3 hold) — terra carries the
write-side implementation role at 5.6 price.** Prediction held
whole, including the registered open risk on 4 — which failed on
harness reach rather than on conduct, a better outcome than the
risk priced.

## Stage-2d pre-registration — reviewer replay (st-41; registered
BEFORE any arm runs, 2026-09-12)

**Question.** Is codex an opus-class reviewer in this repo (the
opus-better-than-fable finding is the precedent shape). The
historical opus run IS the opus arm: the replay reuses its brief
verbatim, removing the arrangement asymmetry.

**Arms.** gpt-6-astra and gpt-5.6-terra, sequential (one account,
quota fragility on record). Astra answers the role question (top
codex tier vs the review-tier default); terra prices the floor,
riding the same lap because both rows land at the mapping table's
next consuming moment.

**Object.** The 0.2.89 review brief
(docs/directives/2026-09-12-opus-review-0289-brief.md) at the
review's own object sha 5948f67, diff base 7774046. Two lines of
the brief are ADAPTED for the receiver's environment and nothing
else: the working-copy path (names the replay workdir, since the
brief's path must resolve where the reviewer runs) and the
scratch line (codex has no scratchpad; read-only, in-memory).

**Isolation.** git init + `git fetch <repo> 5948f67` + checkout:
a sha fetch transfers the commit and its ANCESTORS only, so the
repair-lap commits and the OBSERVATIONS dispositions — all
descendants — are absent by construction, while 7774046..HEAD
resolves for the brief's diff. Verified before dispatch: HEAD is
5948f67, 7774046 resolves, e19116d (first repair commit) does
NOT. The sol vector stands (read-only pins writes, not read
reach; the real repo with the answers is on this disk): the
transcript audit is MANDATORY before any score counts.

**Ground truth.** The review's 10 adjudicated findings (3
BLOCKING, 6 notable, 1 nit; dispositions in
dev-notes/OBSERVATIONS.md "0.2.89 checkpoint-review dispositions"
and the LEDGER lines of 2026-09-12).

**Metric.** Per-arm recovery by claim identity, desk-mapped as in
stage 2b; false positives desk-adjudicated — a finding the arm
itself labels unverified is conduct the brief permits, not an FP;
an unverified claim shipped as verified is. New findings
desk-verified as in stage 2, recorded symmetrically.
**Criterion:** an arm is REVIEWER-VIABLE here iff it recovers all
3 BLOCKING findings AND ≥ 5 of the 10 overall. New confirmed
findings are recorded but do NOT substitute for blocking
recovery — the reviewer role's job is catching what blocks the
pin. Prediction, registered first: astra recovers 2 of 3 blocking
and 5-7 overall (narrowly misses the bar on the blocking clause);
terra 1-2 blocking, 4-6 overall; neither produces a new confirmed
blocking-severity finding.

## Decisions this pre-registration does NOT cover

Global enablement (readiness.json class entry), codex as desk
(stage 3, parked), write-side lane certification (follow-on probe,
own registration).

## Stage-1 RESULTS (2026-09-12, graded at statiker-58)

Workdir pinned at repo sha 857984c (page + fixture copies; answer
key never in the workdir). Harness lessons: codex exec refuses a
non-git workdir without --skip-git-repo-check; exit code 0 does not
reflect an API failure (a 400 on the output schema emptied a run,
visible only in stderr); OpenAI strict structured outputs demand
every property in `required`.

Validity gate: recall(sonnet) = 0.97 ≥ 0.60 — arrangement VALID.
PASS bar resolved: recall ≥ 0.87, precision ≥ 0.75.

| arm | reported | tp | precision | recall | verdict |
|---|---|---|---|---|---|
| sonnet (calibration) | 39 | 33 | 0.85 | 0.97 | baseline |
| gpt-6-astra | 39 | 33 | 0.85 | 0.97 | PASS |
| gpt-5.6-terra | 39 | 33 | 0.85 | 0.97 | PASS (profile identical to sonnet) |
| gpt-5.6-luna | 41 | 32 | 0.78 | 0.94 | PASS |
| gpt-5.6-sol | 34 | 34 | 1.00 | 1.00 | NO VERDICT on this metric — oracle |

**The sol finding (transcript-audited).** sol never read the answer
key (0 hits) but hunted the filesystem, found STALE copies of
statiker_record.py in other sessions' scratchpads, and ran
`lint --tracker` / `sweep --tracker` on the fixture: its perfect
score is the tool's output. The sandbox's `read-only` pins writes,
not read reach — an instrument-reach gap in this harness, recorded.
As a comprehension score: invalid. As certification evidence for a
statiker mechanical lane: finding and running the repo's own
instrument is the most lane-appropriate behaviour any arm showed.
luna attempted the same hunt (one find under ~/.codex/skills),
failed, and read the page; astra and terra never left the workdir.
sonnet's arm shows no oracle (imperfect, profile identical to
terra; claude -p default mode denies un-allowlisted Bash).

**Prediction check.** Registered prediction (recall 0.6–0.9 for
astra and sonnet) was BEATEN on the high side by both (0.97) —
recorded against the prediction, per its purpose.

**Convergent-extras finding (fire-born, booked st-40).** Three to
four independent arms flagged the SAME six (line, code) pairs the
key lacks — lines 107/109 `[COMMITED]` (misspelled tag), 113/115
`Record:` (mis-cased scope opener), 103 (self-described missing
basis), 35 (write-set near-miss). The suite is green asserting
tool ≡ key, so the tool is silent there too: divergence between
independently built instruments pointing at a shared key/tool
parentage gap. Adjudication against the page's definitions is
st-40; no key or tool change rides this results commit.

**Stage-1 verdict.** All three scoreable codex tiers PASS at
sonnet parity; astra and terra are indistinguishable from the
certified Claude tier on this leg. Stage 2 proceeds with
gpt-6-astra as the attack arm (configured default; sol's oracle
behaviour disqualifies its score, not the model — but astra's
in-bounds discipline is the property an attack arm needs).

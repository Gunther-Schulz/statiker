# Statiker — observations journal

Maintainer-side, outside the plugin payload. Consumers: fire-rate
reviews (prune/keep decisions on fire-born clauses) and the
validation grading (PLAN.md, Birth process steps 4-5).

Behaviour-delta signature (what a statiker run produces that a bare
session does not): a `.clippy/runs/` tracker carrying the verbatim
request + requirements head, decision lines with bases, a recorded
fresh-context attack outcome, per-unit commit SHAs, and a verify
verdict with pasted check output. A run missing any of these is a
protocol violation, whatever the code looks like.

## Fire-born clause log

(none — zero clauses at birth, per PLAN.md. Each mint gets a dated
line here: incident, clause text location, subsequent firings.)

## Observations

- 2026-08-05 — **Mint candidate (first): inherited-evidence gap.**
  First trial run (opus desk shakeout,
  beat-the-books `.clippy/runs/2026-08-05-canonical-market-identity-statiker.md`,
  Stumbles S1): statiker 0.1.1 has no clause for a run inheriting
  ANOTHER run's F/D entries — the resume clause assumes the tracker's
  entries are the run's own. Incident: inherited F5(a) was wrong in a
  load-bearing way (wrong table; a migration built on it would have
  rewritten `game_markets` while the resolver's real reference source
  `provider_markets` stayed stale); only the dispatching brief's
  "adopt only what survives your own spot-verification" line forced
  the check (corrected as that run's F10, independently corroborated
  by a blind-briefed leg). Suggested clause shape in the tracker's S1.
  Decision point: mint at run grading, not mid-run (editing the skill
  under the run evaluating it muddies the trial measurement).
  Refinement (operator-raised, 2026-08-05): the eventual clause
  should cover BOTH inheritance directions — another run's record
  (S1's case) and the same session's prior items (multi-item
  sessions; old clippy re-investigated from zero per run, a
  Sonnet-era calibration). One test for both: adopted evidence is
  PENDING until its basis passes a CURRENT-check scoped to the claim
  — recorded basis + staleness check (did the cited file change
  since the basis read? git-computable via the tracker's unit SHAs;
  note item N's own implementation invalidates reads of files it
  touched by construction). Unrecorded in-context memory never
  qualifies (paraphrase-drift class). Full re-investigation is the
  fallback where no basis exists, not the default.
- 2026-08-05 — **Booked analysis (operator-requested): delegation
  split, opus desk vs fable desk.** At trial-run end, grade the opus
  session log against statiker's own delegation rule (discovery legs
  dispatched; "consecutive discovery sweeps in the main session are
  the tell"): classify desk actions judgment-vs-discovery. Outcome
  routing: text violated → adherence stumble or weak tell-clause,
  adjustable from this run; text conformed → "would fable delegate
  more" is unanswerable from an opus log (counterfactual-modeling
  trap) and routes to the already-planned fable trial (PLAN.md step
  4) as a paired split-pattern comparison — patterns, not volumes;
  different task. Any tier-conditional delegation-pressure clause
  must arrive as a fire-born patch citing this analysis, not the
  curiosity. Consumer: the run-grading pass + fable-trial grading.
- 2026-08-05 — **Booked measurement (operator-requested): paired
  attack comparison, first opus-attack-ladder data point.** The trial
  run dispatches TWO parallel attackers on the identical locked
  design — fable (attack-of-record per the skill) + opus — identical
  briefs, blind to each other, outcomes recorded as separate
  tier-labeled tracker entries before any merge; run proceeds on the
  union of confirmed findings. Post-run grading (here, not the desk):
  set-compare the raw finding-sets — what did opus miss against the
  fable ceiling, what did it add. Caveat carried: n=1 pair informs,
  never certifies (significance discipline); certification stays a
  ladder. Union-effect scoping (desk-raised at dispatch, confirmed):
  acting on the union alters the RUN's trajectory, not the
  measurement — the ladder metric reads the raw tier-labeled sets
  recorded pre-merge, so it stays clean; only the unsought
  counterfactual "what would a fable-only run have shipped" is
  lost. Desk implemented all four constraints correctly, incl.
  dispatch-both-before-reading-either and an explicit record note
  that a two-attacker run is measurement, not statiker protocol.
  Consumer: the run-grading pass.
- 2026-08-05 — **Booked question (operator-raised): was [READY]
  called too soon, and can statiker mitigate a premature call?**
  Calibration built in: attack findings alone never indict [READY]
  (forcing point 2 assumes producer self-blindness; zero-delta is
  the exception). Classify each CONFIRMED attack finding: Class A =
  desk-catchable (the stop rule already demanded it — unenumerated
  consumer, unexecuted basis, a decision whose impl brief was not
  constructable) vs Class B = self-blindness (wrong frame,
  unexamined premise — the mechanism working). Only Class-A-heavy
  results argue premature [READY]; the mitigation then is a thin
  stop-rule sharpening with this run as provenance, never a
  convergence-ritual revival (birth-class guard). Consumer: the
  run-grading pass.
- 2026-08-05 — **Booked evaluation (operator-raised): tracker
  verbosity — token-saving only.** Can the tracker thin without
  breaking intent? Hard floor named up front: bases stay (evidence
  discipline), requirement head stays verbatim, tag-first line
  grammar stays (/clippy-stats contract). Candidate fat: narrative
  connective tissue around entries. Cost model: the tracker is
  re-read whole by every attacker, verifier, and resume session —
  verbosity is a multiplier. Method: use the trial tracker as
  specimen, classify content load-bearing vs narrative, measure the
  split; a compression clause mints only if the narrative share is
  material. Consumer: the run-grading pass.
- 2026-08-05 — **Paired-attack PRELIMINARY comparison (raw sets read
  at tracker a1adc177; full grading still at run end).** Verdict:
  A2/opus substantially outperformed A1/fable on the identical
  artifact — an INVERSION of the expected ceiling direction. A2: S1
  critical (U4 PK collision via builder None-segment omission, 363
  colliding prod rows, boot-fail under fail-closed auto-migrate;
  executed prod probe), S2 severe (game_markets ON CONFLICT target IS
  the signature-derived PK — no self-heal; F18 was
  provider_markets-only), S3 severe money-path (D2 deletes the only
  fail-closed NULL-line skips; standing guard traded for a one-time
  gate). A1: six real refinement-class findings, none
  conclusion-flipping; partial overlap only at A1#2 (named the
  NULL-typed-line hazard class + CHECK-constraint remedy — the smoke
  of S1/S3 — but graded it unproven, executed no prod counts, missed
  both mechanisms). Taint check EXECUTED: scepticism targets incl.
  the D10-gate pointer were in BOTH byte-identical briefs; the ~25
  extra lines A2 saw restated its own question + revealed the fable
  dispatch (explains A2's fable self-label, nothing more). So the
  inversion is not brief-steering. n=1: informs, certifies nothing;
  suggests attack quality tracked probe-execution depth, not tier.
  REVISED after the cycle-3 re-derivation (same day): final frame is
  COMPLEMENTARY, severity-asymmetric — A1's quarter-guard
  design-intent contradiction and DB-guard push each changed a
  decision (D16; the avoided D17), so only-A2 ships a contradiction
  and only-A1 breaks prod. Fable-desk independent verification of
  both severe mechanisms EXECUTED: S2 conflict-target-is-PK
  (base_repository.py:116, pk_cols fallback) and S1 None-segment
  omission (market_signature.py build_market_only) both confirmed by
  direct read. Round 2 booked: THREE attackers (fable/opus/sonnet —
  ladder extended a tier down), byte-identical artifact this time
  (nothing appended between dispatches, no tier names visible),
  scope = re-derived D12/D13/D15/D16 + closure regression on all
  confirmed round-1 findings. Tests whether the complementarity
  split repeats under clean protocol.
  SECOND REVISION (desk overlap table, key fact verified by the
  grader against the verbatim raw sets): overlap ~half, and the
  decisive round-1 gap was NOT discovery — it was a SEVERITY-
  JUDGMENT FLIP on a shared mechanism. A1#6 found S2's exact
  mechanism ("nothing converges") and graded it harmless; A2 graded
  it severe by tracing it into D10 and MEASURING the consequence in
  prod. Same on the NULL-line root (A1 "unproven" vs A2 two measured
  severe consequences). At n=1 attack-VERDICT quality ran OPPOSITE
  the tier ranking; plausible mechanism: executed consequence-probes
  before grading (demandable in future attack briefs if round 2
  repeats it). Corpus rule "verdicts flip only under a smarter
  reviewer" gets the asterisk: smarter was not tier-monotonic here.
  Contamination ledger: round-1 preliminary verdict committed
  pre-relay (92c0ea2); grader has since read the designer's grading,
  so the ROUND-2 set-comparison + severity-verdict check routes to a
  FRESH-CONTEXT grader (verifier form: raw sections + re-derived
  design + question, no commentary); this session grades the grader.
  Round-2 attackers and raw records remain clean (dispatched blind,
  pre-relay, scrubbed artifact).
  EFFORT MEASUREMENT (subagent transcripts, executed): A1/fable 43
  tool calls (16 Read / 22 Bash), 40k out-tokens, 11 min; A2/opus 73
  calls (52 Bash / 2 Read), 83k out-tokens, 22 min. Wrong severity
  calls were written from READING (modelling-the-system class);
  right ones each sat on an executed measurement — and fable's
  unique find (quarter-guard intent contradiction) is a
  reading-class defect no probe surfaces. Each attacker found what
  its method could see; verdict quality tracked measurement-vs-
  model, not tier. Mint candidate if round 2 repeats: attack-brief
  clause "every severity call on a mechanism carries an executed
  consequence-probe, or the label unmeasured" — would make attack
  quality tier-robust and reprice the attack class (sonnet
  prediction: with probes, closer than the ranking predicts).
  ROUND-2 INTERIM (B1 fable + B3 sonnet in, B2 opus out; desk-relayed
  table, formal comparison still routes to the fresh grader): (1)
  B1/fable returned a FALSE CLEAN on a money-path closure check —
  "S3 closed by mechanism" — while B3/sonnet found the same guard
  reads STORED not live data (severe, desk-verified); B1 checked
  that a skip EXISTS, not what it reads. Second consecutive round
  where fable's wrong call is a reading-level check and the correct
  severe call sits on traced data flow — the method-not-tier pattern
  now has two datapoints, and the sonnet prediction above confirmed
  early (sonnet out-found fable on the severe defect). (2) A closure
  claim is a NON-EVENT claim (corpus Fixing class): confirmation-
  reads cannot verify it; the mint candidate sharpens to "closure
  and severity calls carry an executed consequence-probe (for
  closures: drive the guarded input through the new mechanism), or
  the label unmeasured." (3) D15 — itself the repair for round-1
  S3 — was wrong: SECOND in-task fix-overshoot/under-land caught
  only by a later adversarial round; the corpus's stated trigger
  profile for iterated falsification, now with two in-task
  datapoints; statiker's "iterate only if it bites" produced the
  iteration naturally. (4) Counterfactual for the record: a
  fable-ONLY round 1 (the skill's default attack-of-record) would
  have returned refinements only and the design would have shipped
  the boot-breaking PK collision — the paired-attack EXPERIMENT, not
  the protocol, saved the run. Attack-tier policy is now an open
  grading question, not a settled clause. Consumer: run-grading
  pass + succession decision.
  OPERATOR DISPOSITIONS (2026-08-05): the natural emergence of the
  iterated ladder from "iterate only if it bites" is the intended
  altitude for the skill — keep the clause thin, no ceremony mint.
  The "multi-attacker for money-path-class designs" idea: NOT a
  full veto (operator softened same day — "tendency no, but
  depends"). Resolution: the question collapses into method-defined
  — probe obligations absorb the METHOD-coverage value of a second
  attacker (the bulk, per round 1); the residual value is
  independence redundancy, a stakes-scaled judgment call that stays
  clause-free in BOTH directions (statiker never banned extra
  attackers; this trial ran 2-3 on free-form operator judgment —
  the existence proof the judgment route suffices). Contingency: if
  the method mint underperforms (a probed attacker still missing
  what a second context catches), the redundancy case reopens with
  data. The original phrasing stays retired (failed the abstraction
  probe). VERDICT (grader + operator concur, 2026-08-05):
  independence redundancy = NO as default practice — basis: both
  observed second-attacker saves this trial were METHOD-shaped
  (consequence-probe and drive-the-input catches a probed single
  attacker plausibly makes), so the trial demonstrates no value
  surviving the method mint; the remainder is unmeasured
  frame-level residue, not worth a standing second attacker plus a
  doubled disposition pass while verify + operator stand behind the
  run. Free-form option + the reopen contingency are the whole
  accommodation. The method-defined direction
  (probe obligations in the attack brief: severity calls cite an
  executed consequence-probe, closure calls drive the guarded input
  through the new mechanism, else "unmeasured"; judgment-class
  findings explicitly not crowded out) stands as the candidate
  landing for the attack class at grading.
  Premature-[READY] preliminary classes: S2 = Class A (unexecuted
  generalization as basis), S1 = Class A-leaning (record carried a
  live [PENDING] D10 NULL-disposition sub-question + duplicate D10
  entries at [READY] — the U4 impl brief was not constructable, the
  stop rule's own test unapplied; also A1#4), S3 = Class B (invested
  triple-read misclassification — self-blindness class). Mint
  candidate from S1's shape: [READY] requires a computed sweep —
  latest-status [PENDING] count = 0, no coexisting contradictory
  entries for one id — a computable predicate, hookable later.
  Consumer: the run-grading pass.
- 2026-08-05 — **Cross-skill routing item (charges to dispatch-guards,
  NOT statiker): §3b tail contradiction.** Trial-run incident, leg B:
  dispatch forms.md §3b closes "an enumeration dispatch … takes the
  READ-ONLY tail verbatim", while §3b's own Coverage + Quotes rules
  produce artifacts that cannot satisfy that tail's one-message /
  no-file-writes terms (122 sites with both-side quotes here). Any
  agent following both must break one; leg B broke the right one
  (data file + pointer = §2 payload-vs-pointer; harness allows DATA
  files). Desk followed the skill as written — the desk's
  self-charge in its Stumbles over-blames; only the second-demand
  recovery slip is desk-owned. Fix shape: §3b gets its own return
  provision (brief-assigned DATA file for the coverage artifact,
  message = pointer + summary counts; keep no-commits /
  no-interim-messages). Route at run grading to the dispatch-guards
  corpus lane (peer-owned — not edited from here). Consumer: the
  run-grading pass.
  RESOLVED same day, operator GO ("let's fix the dispatch while we
  are here"): dispatch-guards `ff6cc4d` (0.3.6) — §3b assigns a data
  file at brief time, pointer message with per-class counts; tail
  header gains the §3b scope line; discovery/verifier tails
  untouched. JOURNAL line in dotfiles `68f5762`. Nothing left to
  route at grading; the item stays here as the trial run's incident
  record.
- 2026-08-05 — **Mint candidates (operator-interface, trial run
  [READY] moment).** (a) The [READY] presentation diffused its ask
  across prose; the operator reported "no clear format for what's
  asked of me" — clippy's menu made the ask mechanical, statiker
  dropped it as ceremony and lost the one line that wasn't ceremony.
  Candidate clause (Stop rule section): the operator-present [READY]
  presentation ENDS with one line naming what advances the run and
  that anything else is treated as an override. (b) The operator
  expected clippy-auto-battle plow-through and asked "why did it
  stop"; statiker's operator-present pause is by design and
  free-form invocation ("advance at [READY] without waiting")
  already yields auto-advance — question for grading: does that need
  an explicit mode line, or is the invocation-line route enough?
  Both decided at run grading, one incident each as provenance.
  Consumer: the run-grading pass.
  SETTLED by operator (2026-08-05, same day): (a)+(b) merge into ONE
  clause — the operator-present [READY] presentation ends with a
  standardized light ADVANCE PROMPT ("(y) advances per the
  recommendation"; anything else is free-form override) — menu-like,
  not a clippy menu; design decisions stay never-posed (loop control
  is the operator's slot, the clippy distinction that survives).
  Decision-complete; APPLY at run grading (trial run completes on
  0.1.1 for clean measurement), version bump with the S1 mint.

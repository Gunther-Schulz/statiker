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

(Each mint: date, incident, clause location, subsequent firings.
Zero clauses at birth per PLAN.md; first cohort minted 0.2.0.)

- 2026-08-05 (0.2.0) **Inherited/adopted evidence** — The record.
  Incident: trial run S1 — inherited F5(a) wrong-table claim, caught
  only by the dispatching brief's act-3 line; migration would have
  rewritten the wrong table. Both directions (prior record / own
  earlier items). Firings: —
- 2026-08-05 (0.2.0) **[PENDING] sweep at [READY]** — Stop rule.
  Incident: [READY] declared over a live [PENDING] D10 sub-question
  + duplicate D10 entries; that open question was S1's exact locus.
  Firings: —
- 2026-08-05 (0.2.0) **[READY] advance prompt** — Stop rule.
  Incident: operator "no clear format for what's asked of me" at the
  trial's [READY]; operator-settled shape (loop control only, design
  decisions never posed). Firings: —
- 2026-08-05 (0.2.0) **Attack probe obligation (reach-matched)** —
  The attack. Incidents (three datapoints): round-1 A1 harmless-
  grading of S2's mechanism from reading; round-2 B1 false clean on
  S3 closure (checked the skip exists, not what it reads); grader
  ruling "probes answered narrower questions than the verdicts they
  closed." Firings: —
- 2026-08-05 (0.2.1) **Cohort repaired after its own fresh-context
  attack BIT (7 findings, all confirmed against the artifacts —
  statiker's discipline applied to itself, second time it caught
  real defects in its own text).** F1: D-enum lacked PENDING while
  M1/M2 depended on it (grammar now [PENDING|COMMITTED|INVALIDATED|
  AUTO-ACCEPTED]; stats-reader-safe, verified against clippy-stats
  grep patterns). F2: "unmeasured" now leaves its question OPEN —
  only a zero-delta attack with all verdicts reach-matched closes
  design (the label alone couldn't bind the gate). F3 [the sharp
  one]: the probe obligation itself had a reach-shortfall — at
  design-time the mechanism is prose, and round 2's CORRECT kills
  were traces, which "executed probe" would have labeled unmeasured;
  rewritten to reach-matched EVIDENCE (executed probe where the
  object exists, full source-chain trace where it is design prose;
  closures name what the guarded input meets on the NEW path). F4:
  attack outcomes get grammar (`- A<n>
  [DISPATCHED|BIT|ZERO-DELTA]`); impl gate keys on the latest
  ZERO-DELTA A-line. F5: probe obligation rides INSIDE the question
  (brief stays artifact+question+tail); probes read-only, scratch
  scripts ≠ report files. F6: frontmatter/opener say "each locked
  design"; re-attacks get a NEW fresh context (a resumed attacker
  inherits its own findings' frame). F7: duplicate-id sweep honest —
  body-read, not tag grammar. SENTINEL TENSION booked: 155
  operational lines vs ~150 — the declaration's dichotomy (restated
  / unprovenanced) misses "many provenance-backed patches from one
  trial day"; compression pass is the fire-rate review's, sentinel
  NOT rewritten to fit. Firings: —
- 2026-08-05 (0.2.2) **Round-2 re-attack BIT (2 real + 2 minor +
  1 routed); repaired same day.** Real: (1) the 0.2.1 impl gate was
  existence-shaped ("before that line exists") — one old zero-delta
  satisfied it forever across re-locks; now "latest A-line must be
  [ZERO-DELTA] and postdate the current lock". (2) F2×F4
  interaction left an all-held-but-unmeasured return with no legal
  A-tag; now [BIT] covers every non-closing return (unmeasured
  verdicts are open questions), [ZERO-DELTA] only when all
  reach-matched and nothing bit. Minor: [DISPATCHED] basis grammar
  (brief at dispatch / report on return); provenance pointer gains
  the source-repo qualifier. ROUTED (peer lane, operator GO
  pending): F5's residual — the probe obligation's scratch-script
  carve-out lives in skill prose the attacker never receives while
  the verbatim forms.md READ-ONLY tail says "No file writes"; the
  attacker itself hit the tension live (payload gate bounced its
  one-message report twice → split 1/2+2/2). Fix belongs IN
  forms.md (same class and landing as the §3b fix): tail gains a
  transient-scratch provision for probe-obligated verifiers.
  RESOLVED same day (operator GO): dispatch-guards 9bcf621 (0.3.7)
  — tail returns ONE message where it fits / labeled parts past
  the size gate, never a report file; no-file-writes scoped to repo
  + report files, transient probe scratch in the agent's OWN
  scratchpad permitted. Both halves of the live tension closed.
  Closure regression otherwise clean: F1-F4, F6, F7 CLOSED with
  re-verified bases. Convergence shape: 7 findings → 4 (2 real) —
  round 3 dispatched per the skill's own rule.
- 2026-08-05 (0.2.3) **Round-3 attack BIT; repaired; attack grind
  ENDED by operator policy (grader concurs).** Repairs: closure
  predicate made computable ("last A-line is [ZERO-DELTA] with no
  F/D line after it" — the attacker's own suggested form; no header
  comparand needed); rounds declared sequential (one attacker,
  A-line recorded before next dispatch; parallel = operator
  experiment) closing the latest-line conflation; probe obligation
  became a PASTEABLE block appended to the attack question
  (forms.md pasted-tail medicine — silent drop was the false-clean
  path); [BIT]'s findings/open questions append as F-lines (the
  record change IS the reopen; desk refutes only with reach-matched
  evidence); AUTO-ACCEPTED vs sweep resolved (carried-unverified is
  re-tagged, never left [PENDING]; F-enum gains AUTO-ACCEPTED);
  bare-tag rule (annotations outside brackets — closes the wild
  annotated-tag hazard); source repo named at first mention; verify
  gains else-parent fallback + post-[ISSUES FOUND] Status stays
  in-progress. KNOWN-OPEN residue (accepted, fire-rate review owns):
  impl-unit enumeration and unit-SHA appends have no line grammar
  (stats-reader-invisible, graded harmless); Status COMPLETE
  reserved-unused (clippy compat); operational lines now 174 vs ~150
  sentinel (pasteable block bought the growth; compression pass
  owed). POLICY DECISION (operator, 2026-08-05, grader concurs with
  basis): during the rough-edges phase skill improvements land
  INLINE and the TRIAL is the falsifier (its Stumbles channel
  demonstrably catches text defects); a fable attack round is spent
  only when a change could SILENTLY corrupt a measurement or an
  interop contract (round 1's F1/F3/F5 were that class — worth it;
  rounds 2-3 were narrowing mechanics the trial would have caught
  loudly); full multi-round polish once, at stabilization. No
  round 4.
- 2026-08-05 (0.2.0) **Re-attack on re-lock (zero-delta closes)** —
  The attack + Implementation gate re-keyed to the zero-delta entry.
  Incident: two in-task fix-overshoots (D15 repaired S3 wrongly;
  round-2 defects introduced by round-1 repairs), both caught only
  by operator-driven re-attacks the skill never scheduled (desk S5).
  Firings: —

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
- 2026-08-05 — **Lens-replacement bet VALIDATED (both halves, first
  live instance).** PLAN.md bet "brief-writing IS where lens-judgment
  lives now" and zero-lenses-at-birth: (1) no upfront lens was
  needed — the trial desk found everything lens-free; (2) when a
  real blind spot finally fired (unexecuted attack verdicts, two
  rounds), it minted as a BRIEF CLAUSE (probe obligations in the
  attack-brief spec), with strictly better enforcement properties
  than a lens: executed once per dispatch at max leverage, binds a
  FRESH context not the invested one, mechanically checkable at
  report time (a severity line without cited probe output is
  rejectable on sight), zero cost on runs that dispatch no attack.
  The legacy-lens rendering of the same lesson would have been a
  standing self-applied checklist entry — the exact form the
  acceptance-run evidence killed. Consumer: run-grading pass +
  succession decision.
  Round-2 grading dispatched (2026-08-05): all three raw sets in the
  tracker (B1:739 fable / B3:804 sonnet / B2:865 opus, verbatim
  pre-merge); per the contamination ledger the set-comparison +
  contradiction rulings go to a fresh-context FABLE grader
  (verifier form, read-only), this session grades the grader.
- 2026-08-05 — **Round-2 grading BOOKED (fresh fable grader, report
  in dispatcher scratchpad r2-grading-report.md; dispatcher
  spot-verified C1+C2 at the cited lines before booking).** 18-row
  matrix: 8 unique B2/opus (incl. both money-path kills — D13 sign
  inversion, live-path value change; ONLY attacker probing the
  orientation axis), 3 unique B1/fable (all record repairs, all
  confirmed), 1 unique B3/sonnet (F56 weak closure, confirmed +
  B2≡B3 exact on the D15 kill). All six contradiction rulings went
  AGAINST B1's contested verdicts or wordings; both B1 HOLD verdicts
  REFUTED. THIRD method datapoint, sharpest form: B1 was
  probe-backed where it HELD and probe-free exactly where WRONG —
  "its probes answered narrower questions than the verdicts it
  closed" (the corpus reach-shortfall shape, executed by the top
  tier). This SETTLES the probe-clause wording: the executed probe's
  question must MATCH the verdict's reach, not merely exist.
  Sonnet: credible (independent D15 kill, accurate greps/SQL, one
  mislabel) — supports tier-robustness under method discipline.
  F60 corroborated again (B3's report self-named opus). Grader
  conduct note: message-payload gate forced its data file — the §2/
  §3b machinery composing as designed.
  CONVERGENCE (same day): the designer desk's own verdict —
  anchored, self-flagged as such — matches the fresh grader on
  every substantive call from the opposite vantage point (opus >
  sonnet > fable; both fable HOLDs wrong; D13 the decisive find;
  fable's unique value = record-repair class). Preserved verbatim:
  "a false clean is worse than a miss — a miss leaves the question
  open, a false clean closes it." Precision correction booked
  against the desk's wording: the wrong calls were the TOP tier's,
  made by the cheaper METHOD (reading, not probing) — tier-cheap
  vs method-cheap is the load-bearing distinction (method-cheap →
  the probe-obligation mint is the fix; tier-cheap would wrongly
  imply "pay more"). "Fable as attack-of-record didn't hold up on
  this task" stands AS SCOPED (n=2, F60 blindness caveat); the
  skill's tier line stays until the succession decision.
- 2026-08-05 — **Cycle-4 attack plan REVISED (operator-raised, grader
  concurs — corrects a hole in the redundancy No-verdict): THREE
  probed attackers again (fable/opus/sonnet), as the probe-mint
  VALIDATION run.** The reopen-contingency ("a probed attacker still
  missing what a second context catches") is unfalsifiable without a
  comparison arm — a solo probed false clean is indistinguishable
  from a clean design until implementation pays for it. Cycle-4
  triple answers: (a) does probed-fable stop false-cleaning, (b)
  does probe discipline equalize tiers, (c) max coverage on the
  run's highest-stakes artifact. Single-attacker No-verdict stands
  for the STEADY STATE only, post-validation. Protocol carries
  round-2 fixes: byte-identical artifact, nothing appended between
  dispatches, all briefs carry the 0.2.0 probe obligation, raw
  tier-labeled records pre-merge, F60 blindness limit acknowledged.
  DESK×ATTACK MATRIX booked open (operator): under a fable desk a
  fable attack buys only fresh-context (no smarter reviewer exists),
  so probed-opus attack may suffice there — no cell pre-committed;
  the matrix fills from the ladder (cycle 4 = opus-desk row; the
  fable-desk trial picks its attack tier FROM cycle-4 data and
  becomes the fable-desk row). Consumer: cycle-4 session brief +
  succession decision.
  OPERATOR PRODUCTION TARGET (2026-08-05, decision criterion for the
  succession decision): what counts is token efficiency at similar
  quality — fable is both the most expensive tier AND capped (50% of
  weekly), so at close quality ALWAYS prefer the lower tier in
  production; ideal steady state runs on opus + sonnet only, fable
  reserved for roles where a measured quality gap demands it
  (grading verdicts, escalations — not standing pipeline slots).
  The cycle-4 triple is exactly the measurement that determines
  whether that ideal is reachable for the attack class; the trial's
  opus-desk performance already supports it for the desk.
  WORKING HYPOTHESIS (operator-agreed, 2026-08-05, trialing still
  required): production = opus desk + sonnet legs/impl + probed
  attacks at whatever tier cycle 4 certifies; fable = meta layer +
  sampled post-hoc spot-audits + escalation-on-ceiling over bounded
  briefed artifacts. Four factors recorded into it: (1)
  verdict-routing asymmetry — tier≥producer makes a fable desk drag
  its attack layer up to fable, while an opus desk certifies
  end-to-end cheaper; (2) the desk is fable's economically worst
  seat (prefix re-billing, 94.2% audit) while bounded verdicts are
  its cheapest; (3) the uncovered residual in fable-less production
  is judgment-class findings above the opus ceiling that no probe
  reaches — mitigation shape: sampled fable spot-audits, not a
  standing seat; (4) the booked delegation-split analysis tests
  whether "fable writes better briefs" has any observed gap at all.
  Teachability bet restated: every fable capability convertible to a
  form/clause moves down-tier permanently (dispatch skill's own
  core finding; probe-obligation mint = existing validation).
  FIRST NATURAL INSTANCE of the escalation-on-ceiling role
  (anecdotal, unpaired — no opus arm, operator self-flags possible
  misread of opus's proposal): claude-code-cache-fix review
  2026-08-05, opus-briefed fable session over a bounded artifact —
  judgment-dense output (flagship: a gate exemption whose third
  condition, written on the OURS side, self-retires when the
  freeness coupling breaks — the open finding converted into a
  property of the fix), plus two reach-shortfall catches. Supports
  the hypothesis; measures nothing. Confound noted: the escalating
  session wrote its reviewer's brief (open enough that the reviewer
  roamed beyond it).
  RE-GRADED after transcript check (executed, opus session
  03d45c17…): misread confound CLOSED — opus's actual proposal (pin
  messages[0]) was withdrawn BY OPUS pre-brief on sound basis
  ("prefix already broken one layer up"), so nothing was needlessly
  discounted; and none of fable's deliverables (rotation-stranding
  mechanism, self-retiring exemption, LRU sibling, single-file
  tripwire) appear in opus prose pre-brief (term-search over
  assistant text blocks, zero hits). Upgraded to WEAK POSITIVE: the
  escalation demonstrably added converged content the escalating
  session lacked, and its self-withdrawal→escalate conduct was
  correct. Still not tier measurement: deep-session-vs-fresh-context
  confound stands (no fresh-opus arm ran the brief).
  Operator concurrence (same day): on reflection the issue was "not
  that complicated" and a FRESH opus quite plausibly matches — the
  deep session was likely overloaded by prior context; anecdote
  weight stays weak-positive for the ROLE, nil for tier.
  Operator's qualitative read (booked with the grader's scoping):
  fable's "nothing to fix — the mechanism is correctly priced, fix
  the instrument and the record" verdict vs opus's continued
  fix-hunting reads as a broader/holistic altitude — the quality
  motivating the fable-desk hunch. Scoping: opus also reached
  don't-fix (withdrew its own proposal); the fable delta was LAYER
  TRIAGE (mechanism/instrument/record) + making non-action
  load-bearing. Teachable slice identified: "triage the defect's
  layer before fixing; test the mechanism against its definition
  before calling it wrong" — corpus wrongness-claim ethic, mintable
  prose; the unteachable remainder is what the fable-desk comparison
  trial prices. Selection-effect caveat: fable observed fresh+
  bounded, opus deep+tired; same-day fable desk errors (redundancy
  hole, probe-clause reach-shortfall) on the other side of the
  ledger.
  END-STATE FRAMING (operator, same day): the certification pattern
  applied to the whole system — fable belongs in the META layer
  (skill design, heavy grading, contradiction adjudication, mint
  wording: this session's work, where the judgment premium
  demonstrably paid), whose one-time output is what MAKES production
  safe to run cheap (a probe-obligated brief needs no fable attacker
  because fable judgment wrote the obligation). Once statiker
  satisfies, production = non-fable wherever possible; fable
  re-enters only when the meta layer reopens (new mint, fire-rate
  review, a verdict the record shows cheaper tiers getting wrong).
- 2026-08-05 — **Pre-cycle-4 mint pass PLANNED (statiker 0.2.0;
  operator + grader concur).** Run paused cleanly at a session
  boundary (desk handoff 76df9e0e); purity argument for finishing on
  0.1.1 is spent (multi-session, operator-steered, paired-attack
  experiment) and cycle 4's fresh session IS the S1 inherited-record
  case — build-first: mint and tune in operation. Mints: (1) S1
  inherited-evidence clause (settled, both directions); (2) [READY]
  advance prompt (settled); (3) S5 re-attack-on-re-lock as a
  CLARIFICATION of "iterate only if it bites" (a re-derived design
  is a new locked design; only zero-delta closes) — two in-task
  datapoints, both re-attacks were operator-driven not skill-driven;
  (4) attack-brief probe obligations — wording HELD for the round-2
  grader's method attribution; (5) [PENDING]-sweep at [READY]
  (computable). Desk's F60 booked as measurement caveat: round-2
  attackers were never blind — SendMessage roster + model-in-name
  convention exposed each attacker's peers and tiers; tension with
  the veto-gate naming convention parked, not solved. Consumer:
  the mint session (this one) + run-grading pass.
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

## Session handoff — 2026-08-05 grading/mint session closed

State at close, for the next session: statiker 0.2.3 pushed + pinned
(fresh sessions serve it automatically); dispatch-guards 0.3.7
pushed + pinned; trial run PAUSED at cycle-3 handoff (beat-the-books
tracker, desk commit 76df9e0e) awaiting the cycle-4 fresh opus
session; beat-the-books holds 19 unpushed commits (deploy bundle,
operator hold — push deploys prod LIVE); dotfiles holds this
session's hook-rewrite commits unpushed (lane convention). No agents
in flight; no round-4 attack (refinement policy above). Open
grading docket, all booked above with consumers: full-run work
review (after cycle 4 + impl + verify), delegation-split analysis,
tracker-verbosity measurement, fire-born firing log upkeep, sentinel
compression at the fire-rate review. The cycle-4 attack step is the
TRIPLE probed measurement (probe-mint validation booking), an
operator experiment under the skill's sequential-rounds default.

- 2026-08-06 — **Near-miss: the cycle-4 TRIPLE booking almost
  dropped at the handoff seam (carrier/consumer mismatch; caught by
  the operator-present pause).** The triple-attack validation
  booking (this file, 2026-08-05, consumer "cycle-4 session brief")
  lived only HERE — but cycle 4 is a fresh opus session in
  beat-the-books whose sole handoff artifact is the tracker's
  handoff section, which never mentions the triple; the launch
  instruction relayed via the fable session also omitted it. Cycle 4
  accordingly announced "send the round-3 attack to fable" at its
  [READY] presentation — correct conduct per 0.2.3 (sequential
  default; parallel attackers are operator experiments by design).
  The operator relayed that message into the session holding this
  ledger, which caught the mismatch and returned the override with
  the round-2 protocol lines. Statiker charge: NONE — and the
  operator-present [READY] pause + stated-next-step is exactly the
  mechanism that surfaced the wrong plan for veto BEFORE dispatch
  (a datapoint FOR the pause design, alongside the ADVANCE-PROMPT
  mint). Global-corpus charge: consumer named without carrier
  reachability — sharpened same day in CLAUDE.md Per-project
  accretion (dotfiles; carrier-on-read-path clause, JOURNAL line in
  the same commit). Consumers: the run-grading pass (pause-design
  evidence) + the corpus fire-rate review (the sharpen).

## Cycle 4-5 of the trial run — 2026-08-06 (fresh opus desk session)

Provenance for every item below: the beat-the-books trial run,
`.clippy/runs/2026-08-05-canonical-market-identity-statiker.md`,
cycles 4-5 and attack round 3. Raw attacker reports preserved at
`.clippy/runs/evidence/2026-08-06-cmi-*` in that repo.

- **S5 is CLOSED by 0.2.3, and the trial now carries strong evidence
  FOR the re-attack clause.** Round 3 attacked the round-2 repair and
  ALL THREE attackers bit — including one decision-flipping finding
  (the reference set's writer left unassigned) that was INTRODUCED by
  the cycle-4 re-derivation itself. That is the second consecutive
  round in which a repair shipped new defects. Consumer: the
  fire-rate review — this is the clause's firing record, not an
  anecdote.
- **S7 [SKILL DEFECT, structural] — "The record" is not computable on
  a SECTIONED tracker.** 0.2.3 says entries are appended never
  rewritten, a status change is a new tag-first line, and [READY]
  requires no entry's latest line be [PENDING]. That holds only if the
  file is strictly append-AT-END. The trial tracker grew in sections
  (`## F-track`, `## Cycle N`, `## Attack …`), so file POSITION stopped
  tracking chronology: `D10` and `F46` each ended with a
  chronologically-OLDEST [PENDING] sitting positionally LAST, and a
  mechanical latest-line read returned [PENDING] for entries settled
  two cycles earlier. An earlier attacker had flagged the symptom and
  the desk answered it in prose ("read latest-line-wins") — the very
  read that fails. Candidate shapes, not applied: require strict
  append-at-end, or require an explicit supersedes-pointer. Consumer:
  the next skill edit.
- **S8 [SKILL DEFECT, enforcement] — the bare-tag rule fired against a
  TOP-TIER desk one cycle after that desk RECORDED the rule.** The
  desk wrote 0.2.3's bare-enum requirement into its own tracker at
  cycle-4 open, then emitted five annotated tags in the same cycle.
  Measured consequence, not cosmetic: a latest-tag scan returned 96
  entries and silently omitted all five, so a [COMMITTED] decision
  read as its own superseded [PENDING] predecessor. A convention
  recorded but not mechanically checked does not hold, including
  against the context that just wrote it. The computable slice (a
  tracker linter: non-bare tags + latest-line-[PENDING]) is booked as
  a ready item in beat-the-books BACKLOG with a red-first verifier
  named against real commits. Consumer: the fire-rate review + that
  backlog item.
- **A THIRD hygiene class the sweep cannot see: stale-[COMMITTED].**
  All three round-3 attackers independently found decisions whose
  latest tag still read [COMMITTED] though superseded only in prose or
  inside another entry's body (D1, D2, D3, D11, F47, F56, D17). The
  desk's closure sweep reproduced correctly and still overclaimed —
  its predicate proves no latest-[PENDING], never that no superseded
  decision stays live. "Superseded" is a judgement about bodies, so
  this half is NOT mechanizable; the discipline is that superseding a
  decision REQUIRES an [INVALIDATED] line for the old one. Candidate:
  state that obligation explicitly in "The record". Consumer: the next
  skill edit.
- **[ATTACK PROTOCOL] Desk appends during a live round contaminate
  it.** The attack-of-record reported that its sweep ran over the LIVE
  working-tree tracker, whose tail by then carried another attacker's
  `C3 [BIT]` header — because the brief said "read-only at <sha>" but a
  working-tree read gets HEAD, and the desk kept COMMITTING outcome
  entries while an attacker was still running. The operator's
  "nothing appended BETWEEN dispatches" condition was honoured; nothing
  covered appends AFTER the last dispatch with attackers live. Repair:
  brief the artifact as `git show <sha>:<path>` output only, or freeze
  desk appends until every attacker returns. Consumer: the round-4
  brief (already written into the run's handoff) + the next skill edit.
- **[DISPATCH SKILL / F60 interaction] S2's collision hazard went from
  near-miss to REALIZED, and destroyed evidence.** Briefs assigned
  `r3-attack-<your own agent name>.md` — identical text intended to
  yield distinct files. One attacker self-identified as ANOTHER live
  agent (third consecutive occurrence of the F60 roster-leak mislabel)
  and wrote to that agent's path; the two reports collided and the
  loser's full detail is gone (survivor confirmed by content markers:
  7 hits of one attacker's unique findings, 0 of the other's). A
  per-agent filename derived from the agent's OWN self-identification
  is not collision-safe when the harness leaks a roster the agent can
  misread. Note the genuine tension this exposes: byte-identical
  briefs (needed for a clean paired measurement) and collision-safe
  outputs pull against each other; the resolution is the DISPATCHER
  assigning literal paths in a per-agent line appended to an otherwise
  identical brief. Consumer: dispatch-guards §2 (payload/data-file
  rule) at its next edit.
- **[FOR the pause design, second datapoint] The operator-present
  [READY] pause surfaced a scope decision the desk could not settle.**
  Cycle 4 found a LIVE money-path defect outside the run's stated
  scope (stored odds sign-inverted for swapped markets, confirmed by
  an executed probe with a positive control, reproduced by four
  independent contexts). The desk formed a recommendation, surfaced it
  as a decision rather than carrying it silently on a default, and the
  operator folded the fix in. A run without that seam would have
  shipped the behavior change as an unattributable side effect of a
  refactor. Consumer: the run-grading pass.

- 2026-08-06 — **Round-3 (cycle-4) TRIPLE graded: the opus-desk row
  of the DESK×ATTACK MATRIX is filled.** Source: tracker C0-C5 +
  G4, verbatim pre-merge records (beat-the-books 83ca2375, 7b83bceb,
  4c44806f), desk-blind comparison done here per the C-protocol's
  "comparison happens post-run, outside this session". Row content:
  probed-OPUS strictly dominated — sole clean decision-flipping find
  (reference-set writer unassigned; D25/U3 contradiction) PLUS the
  desk-error mechanism (F57's explicit-set_ verified at the venue
  path, carried to the metadata-driven reference path — the corpus
  carried-mechanism shape, 3rd occurrence this run) PLUS the widest
  closure audit (6 stale-COMMITTED vs fable's 3). Fable replicated
  the #1 find but C5 contamination (desk appends mid-round; C2
  committed before C1 returned) leaves its independence
  uncertifiable — the asterisk weakens fable's arm only, so the
  opus-on-top signal is the clean one, now 2 for 2 across rounds.
  Sonnet reversed from round 2 (missed the flipper, one unique
  minor find) — below-opus ordering is noise. Probe-mint answers:
  (a) probed-fable false-cleaning on MEASUREMENT claims stopped
  (all its probes sound); residual class exposed — record-REACH
  judgment calls (F57 listed "genuinely closed", refuted by G4) —
  3rd consecutive round with a wrong fable closure/HOLD call;
  (b) probe discipline did NOT equalize tiers — opus dominated at
  the middle price; (c) union coverage achieved, every attacker ≥1
  unique real find. Caveat: n=1 per cell per round, one task.
  Consumer: the succession decision (skill tier line unchanged
  until then, per the standing booking).
- 2026-08-06 — **0.2.4 mint (fire-born, C5 provenance): pinned
  attack artifact + desk append-freeze while attackers are live.**
  Incident: C1/fable's record sweep ran over the live working tree,
  which by then carried C0-C4 including another attacker's [BIT]
  header (desk kept committing outcome appends after the last
  dispatch — the operator's between-dispatches condition was
  honoured; the after-dispatch window was unnamed). Class: silent
  measurement risk — exactly the class the refinement policy kept
  attack-grade fixes open for. Both halves encoded because pin
  alone does not close the channel (attackers hold read-only repo
  access for code sweeps; a tree read serves HEAD). Sentinel note:
  operational count now 180 (was 174) — the booked sentinel
  compression at the fire-rate review absorbs this mint's +6.
  Consumer: fire-born firing log + fire-rate review.
- 2026-08-06 — **Round-4 attack tier DECIDED (operator GO): probed
  opus as attack-of-record, as an operator override for round 4
  only — the skill's trial tier line stays until the succession
  decision, which now cites the opus-desk row above.** Rationale:
  the fable-ceiling question the trial line existed to answer has
  its data; further fable attack rounds spend the capped pool on an
  answered question. Fable's booked roles (grading verdicts,
  escalation-on-ceiling, spot-audits) are untouched. DELIVERY (the
  carrier-on-read-path rule, minted 2026-08-06): this decision's
  consumer is the beat-the-books cycle session, which does not read
  this file — it travels in the operator's next reply to that
  session, quoted in this session's closing message; this entry is
  the record, not the delivery.

- 2026-08-06 — **Round-4 plan AMENDED (operator): PAIR — probed opus
  (attack-of-record) + probed fable (comparison arm) — as the cheap
  solidifier for the opus-vs-fable succession call.** The opus
  attacker runs anyway (round 4 is owed after the round-3 bites), so
  the paired datapoint costs one fable dispatch; under 0.2.4 (pinned
  artifact, append freeze) the pair is uncontaminated — a clean
  replication test of round-3's asterisked fable arm, and fable's
  one fair falsification shot before lock-in. PRE-REGISTERED lock
  criterion, recorded before dispatch (briefed-to-refute): the
  succession decision writes probed-opus as the attack tier UNLESS
  the fable report carries >=1 decision-flipping or money-path
  finding absent from opus's report and desk-confirmed by probe;
  unique record-hygiene/minor finds do NOT block the lock (that
  class is priced into fable's grading/meta roles). Both arms carry
  full closure standing — any bite reopens the design. Scope: the
  lock covers this attack class at the opus desk; the fable-desk
  row stays open. C4 hold untouched — round 4 fires only on
  operator confirmation after the re-derivation locks. SUPERSEDES
  the solo-opus relay line (previous entry); corrected relay quoted
  in the session's closing message (carrier-on-read-path: the
  consumer is the beat-the-books session, delivery is the
  operator's reply there).

- 2026-08-06 — **FIRED, first live catch: the desk-restart rule +
  brief version gate.** The fresh cycle-5 desk's session baseline
  predated the 0.2.4 pin move (10:20:48), so its Skill injection
  served 0.2.3 — the gate (base-directory line check, from the
  operator brief) caught it BEFORE round 4, the desk refused the
  round citing the repo rule, and recommended its own restart.
  Exactly the failure the rule was minted for, same day, caught at
  the seam. Also fired: the desk found the tracker header + handoff
  had recorded "dispatches without re-asking" against the operator's
  live hold — C4's class one revision later — and repaired the
  record (C8; header now HELD). Desk conduct throughout: correct.
  C10 accepted at the meta layer: round-4 artifact pins at f59bee6f
  (the re-lock), not HEAD — the scrub removes tier tokens but C8's
  description of the pair setup stays legible; a HEAD-served
  artifact would brief the arms on their own experiment. Consumer:
  fire-born firing log + run-grading pass.

- 2026-08-06 — **PARKED tension in 0.2.4 (desk-surfaced, round-4
  dispatch presentation): append-freeze vs context-death
  insurance.** With appends frozen while attackers are live, the
  round's dispatch C-lines exist only in the desk session until
  both arms return — a mid-round desk death loses the dispatch
  record. Working mitigation (issued with the round-4 go): shadow
  dispatch log in the desk's own scratchpad, outside the repo,
  transcribed into the tracker after the arms return. Becomes a
  mint candidate only on a fire: a desk dying mid-round, or the
  shadow log proving load-bearing in practice. Consumer: fire-rate
  review.

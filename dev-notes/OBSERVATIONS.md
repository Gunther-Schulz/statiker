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

- 2026-08-06 — **ROUND-4 COMPARISON GRADED — LOCK CRITERION MET:
  probed-opus locks as attack tier (this attack class, opus desk).**
  Basis: body-read of both raw reports
  (beat-the-books .clippy/runs/evidence/2026-08-06-cmi-r4-attack-A/B)
  against the pre-registered criterion (this file, 2026-08-06).
  Fable's two blocking-eligible findings BOTH appear in opus's
  report: its SEVERE (D29/D37-U2 sign-CASE contradiction, money
  path) = opus F5 verbatim in substance, same repair; its MODERATE
  (home-only migration/verify vs both-row negation) = opus F2, which
  additionally carries the positive control both-positions. Fable's
  uniques are three minors (N1 rationale imprecision, N2 pin
  buildability under the U4a CHECK, N3 orphan-residue overclaim) —
  the non-blocking class by criterion, and consistent with the
  round-2 grading's "fable unique value = record-repair" finding.
  Opus uniques: F1 (the round's sharpest — backfill source
  nonexistent for 61.8%/21,109 rows, prod-measured with in-query
  positive control, desk-reprobed; fable missed it entirely), F3
  (identity tuple has no live definition; D12's safety argument
  cites invalidated ground), F4, F6, F7 + four lesser
  stale-COMMITTED. Score 3-for-3 across rounds, and the round-3
  asterisk RESOLVES: this fable arm was uncontaminated (C5 channel
  closed) and probe-obligated, and still found a strict subset of
  the substance — the clean replication the pair was designed for.
  Mild 4th instance of the record-reach residual: fable HELD
  "D36(a) accurate" where opus F6 shows D24 kills its argument
  (conclusion possibly surviving). CONSEQUENCES: round 5 = solo
  probed opus, sequential default back in force (relay to desk at
  cycle-6 lock); skill tier line still changes only at the
  succession decision, which now cites this verdict. MINT CANDIDATES
  booked for run grading, not minted now (trial-measurement policy):
  the round-4 bites are dominantly the stale-COMMITTED /
  partial-invalidation class — (a) superseding requires an explicit
  [INVALIDATED] on the old entry, (b) invalidating requires
  restating what survives (opus F3's reverse rule), (c) the [READY]
  sweep is blind to stale-COMMITTED contradictions (C23's limit,
  beaten by both arms twice). Consumer: succession decision +
  run-grading pass.

- 2026-08-06 — **Cycle-6 field test of the round-grading mint
  candidates (desk report, tracker 69059a1d).** The two closure
  rules (candidates (a)+(b), handed to the desk as run directive)
  applied record-wide as D38: nine stale entries retired with
  survivors re-homed into live entries — the wholesale close the
  per-entry approach missed for four rounds. Candidate (c)'s sweep
  blindness got MECHANIZED in-run: tools/statiker_dead_basis_check.py
  (beat-the-books), shown red on the pre-cycle-6 tracker against the
  real arm-A defect, sharpened 25→14 hits for overfire, kept
  advisory (judgment residue stated). Two harvest datapoints for run
  grading: C26 — the annotated-tag defect was NAMED at cycle 4 and
  not repaired for two rounds (worse shape than never-surfaced);
  D48 — a booking living only in a dead tracker entry re-homed to
  BACKLOG.md, the carrier-on-read-path class caught in-run by the
  desk (corpus sharpen firing occasion, second same-day). Consumer:
  run-grading pass + succession decision.

- 2026-08-06 — **Cycle-economics preliminary read (operator-raised;
  feeds the booked tracker-verbosity measurement + full-run
  review).** No attack round wasted by the record: rounds 1-4 each
  bit with a shippable money-path defect; stop rule (zero-delta)
  not yet reached. Baseline: the task's clippy predecessor FAILED
  at investigate-design (17KB tracker, inherited); clippy
  f2-min-odds paused at cycle 49 — high counts predate statiker.
  Non-intrinsic inflation, enumerated: (1) experiment width (rounds
  3/4 ran 3x/2x attackers — measurement cost, concluded); (2)
  record-hygiene debt — large fraction of round-3..5 findings were
  record-class; C26 shows the class named at cycle 4 and unrepaired
  two rounds, so attack rounds doubled as record linters. Knob for
  the 0.2.5 decision: mechanized record checks (dead-basis check,
  tag linter) run pre-[READY] each cycle — candidate (c)
  operationalized; (3) inheritance re-verification paid diffusely
  over cycles 1-4 (S1-S3) — knob: explicit priced intake-grading
  cycle on any resumed/superseding run. NOT a knob: sequential
  re-attack per re-lock — rounds 2 AND 4 bit on repair-introduced
  defects (S5 + round-4 record), best-evidenced rule in the skill.
  Consumer: run-grading pass.

- 2026-08-06 — **0.2.5 mint (mid-run, at-seam release; operator GO
  "grade what's done, tune, continue"): the evidence-complete slice
  of the grading docket, minted with in-run field tests as
  provenance.** (1) Supersede/invalidate closure rules (D38's two,
  cycle-6 field test: nine entries closed wholesale) — widened into
  the existing kill-premise rule, not added beside it; (2) [READY]
  sweep gains the dead-basis leg (arm-A F3 by hand, repo check red
  on the real defect, mechanize-first + judgment-residue form);
  (3) attack tier line: probed opus — PLAN.md's probe-then-certify
  step certified (three-round comparison, criterion met 3-for-3);
  PLAN.md carries the certification note; fable escalation stays an
  operator call. DEFERRED as not evidence-complete: delegation
  split, tracker verbosity, full-run review, sentinel compression
  (operational count now 191; compression consolidates after an
  operating interval), clippy-succession itself. Repo CLAUDE.md
  gains the seam clause (pin moves only at a recorded A-line /
  forcing-point boundary) + a Trial working conventions section
  persisting the session's settled styles: two-session layout with
  operator relay, mid-run tuning at seams, pre-registered
  comparison criteria, per-dispatch confirmation (trial-phase).
  RELEASE TIMING: commits+push now; PIN HELD until round 5's
  A-line is recorded — the desk finishes round 5 on 0.2.4 (its
  conduct is unchanged in 0.2.5), fresh desk serves 0.2.5 at the
  seam. Consumer: fire-born firing log + run-grading pass.

- 2026-08-06 — **Cycle-inflation solution stated; 0.2.6 mint PENDING
  on round-5 outcome.** Diagnosis: cycle count is driven by kill
  rate, not decision count — every decision-flipping bite in rounds
  1-4 rested on a data-shape premise measurable at commit time
  (D13 0/25, reference-writer grep, 61.8% backfill SQL); front-
  loading more decisions adds kill targets, not closure. Candidate
  mint: the attacker probe obligation applied symmetrically at the
  desk's commit moment — a committed decision citing a data-shape
  or code-path premise carries its executed measurement as basis.
  Cycle 6 field-tested it voluntarily (measured-not-reasoned;
  D40/D41); round 5 IS the falsifier: zero-delta or minor-only →
  mint as 0.2.6 with cycle-6→round-5 provenance; a bite on a
  measurable premise → hypothesis takes the hit, re-diagnose.
  Floor stated: fresh-context reach findings (questions the desk
  didn't ask) are irreducible — target is one clean confirming
  round, never zero rounds. Consumer: round-5 outcome handling +
  0.2.6 decision.
  TRIAGE ADDENDUM (operator-raised, same day): classified
  loaded-but-inert, not a gap — the corpus carries the rule twice
  (probe-before-resting; the reach family), loaded in every desk
  session; non-firing mechanism = evidence-register ethic with no
  anchored moment in the loop, and the basis grammar accepts
  file:line so a read-basis on a measurable premise reads as
  compliant. Not dispatch-side (all dispatch defects this run were
  conduct-class, fixed, none caused kills). Fix layer: statiker —
  anchor at the commit moment via basis grammar, the proven 0.2.0
  mechanism class (attacker obligation, validated rounds 3-4).
  Premise-kind test stays judgment/prose; attack round remains the
  mechanical backstop.
  MINTED EARLY as 0.2.6 (operator GO "lets fix it", same day,
  overriding the pending hold): build-first posture — and the
  round-5 falsifier survives intact, since round 5 attacks
  cycle-6's already-produced output, which no skill-text change
  reaches retroactively. Clause anchored in the design-loop
  paragraph before the kill-premise rule (placement basis: grep
  reach|basis|executed over SKILL.md — reach-matching previously
  lived only in the attack block :148 and desk-refutation :173).
  Round-5 outcome now grades the mint instead of gating it: a bite
  on a measurable premise reopens the wording, not the existence.
  Operational count 198; compression booking stands.
  (Correction, same turn: operational count is 197 per the executed
  verify, not 198 as the line above composed pre-run.)

- 2026-08-06 — **Round-5 harvest (desk-named carrier gap,
  transcribed here — the desk correctly declined to cross repos;
  source: beat-the-books tracker through C34, desk closing report).**
  Round 5 [BIT]: 1 severe (G7-confirmed: typed columns need FIVE
  literal mapping surfaces in repositories/core.py, D47/U3 named
  two; the named set_ clause is inert alone — set_ reads
  stmt.excluded.<col>, so naming a column there while omitting it
  from values upserts NULL; the missing orm_to_domain is silent —
  every DB-level pin green while membership consumers read None),
  3 moderate, 3 minor. Rounds 1-5 all bit. Three skill observations
  transcribed: (a) FREEZE SCOPE follows the brief's claims, not the
  skill's default surface (round-5 brief claimed tree≡lock →
  whole-repo freeze; 0.2.4's clause was tracker-only) — MINTED as
  0.2.7, same day, fire-born; (b) A-track closure gate was
  unreadable two rounds via namespace drift (outcomes recorded as
  C-lines) + annotated tags — the every-round-records-an-A-line
  rule EXISTED (0.2.x): conduct/legacy finding, not a gap; booked
  for run grading, no mint; (c) tier-scrub absence predicate must
  be STATED with the instrument shown live ("briefable" contains
  "fable"; naive grep cannot reach zero) — trial-protocol gotcha,
  consumer: future comparison rounds run from this session; ledger
  is the carrier. ALSO A5 on the cycle-6 mechanism: dead-basis
  checker covers D38 rule 1, blind to rule 2 — instrument reach
  shortfall, repo-side fix (beat-the-books tools/), booked to the
  run's cycle-7 inbox by the desk.
- 2026-08-06 — **0.2.6 mint GRADED against round 5 (its designated
  falsifier): diagnosis CONFIRMED, clause stands unchanged.** No
  measured premise died — cycle-6's measured decisions (D40/D41)
  survived the round; the severe kill was an untraced CODE-PATH
  completeness premise (five mapping surfaces vs two named), which
  the clause's own wording ("data shape or code path ... executed
  measurement") already covers — minted after cycle 6, so cycle 7
  is its first governed cycle and the five-surfaces class is
  exactly what it must prevent there. PIN MOVED to 0.2.7 at this
  seam (run paused, A5 recorded — the seam rule's conditions).
  Consumer: run-grading pass + cycle-7 conduct.

- 2026-08-06 — **Desk-interrogation round 1 (the convention's first
  exercise) — both answers harvested.** Q1 verdict: IMPROVISED —
  the desk classified instrument work as permitted during the A5
  reopen without consulting a rule ("I never asked 'does [BIT]
  constrain non-design edits?' as its own question"), inheriting
  the classification from handoff inbox + operator prompt; its
  post-hoc reconstruction is explicitly flagged as such. Genuine
  gap → MINTED as 0.2.8: a reopen bars the design's UNITS only —
  investigation, record repair, run instruments stay open desk
  work; the closure gate reads the A-track, never the toolbox.
  Q2 verdict: red-proof EXISTS (F62 at 48d92ce8, plus D11/D16
  orphans six hand-passes missed) BUT the desk's post-cycle-7
  "RULE 2 CLEAN" was a FALSE CLEAN it self-caught under the
  question: the checker counted the desk's own C35 alarm-entry and
  an F77 enumeration mention as survivor restatements, while the
  actual restatements sat in tag-first [INVALIDATED] lines — which
  the 0.2.5 clause's own wording ("in a live entry") excludes:
  skill wording correct, desk conduct + checker encoding wrong.
  Consequence: checker has a self-inflicted blind spot (ids named
  in C35/F77 can never re-report as orphans); F47 a live orphan it
  cannot see. Repair authorized as desk work pre-round-6. NEW
  FALSE-CLEAN SUB-SHAPE for the corpus fire-rate review: a checker
  whose input contains reports ABOUT the defect reads the report
  as the all-clear — self-referential input needs the checker's
  own reporting namespace excluded. Consumer: fire-rate review
  (corpus candidate) + run-grading pass.
- 2026-08-06 — **Convention interaction bug (operator-raised via
  the desk's routing line): per-dispatch confirmation pushed
  discovery work INTO the ungated inline lane.** Desk named the
  tell honestly (consecutive discovery reads = leg should have
  dispatched) then routed inline because each dispatch would block
  on operator confirmation. The safety convention thereby REDUCED
  oversight: an inline read has no gate at all, a dispatched leg
  at least surfaces in the panel. Decision → operator (recommend:
  confirmation binds attack/impl/fable dispatches; read-only
  discovery legs ≤ opus pre-authorized, named in the turn report
  instead). Pin HELD at 0.2.7: 0.2.8's clause governs reopen-time
  conduct, which is past for this desk; next restart seam (post-
  round-6) picks it up. Operational count 204; compression booking
  stands. Consumer: operator decision + run-grading pass.

- 2026-08-06 — **PARKED (operator-raised): graduate the dead-basis
  checker into the statiker payload.** The checker parses the
  skill's own tracker grammar — format-owned, not repo-owned; the
  0.2.5 sweep clause ("mechanized check runs first") becomes real
  everywhere only if the skill ships it. Provenance: the class
  fired in attack rounds 3-5. Named graduation conditions: (1) the
  checker survives the run's remaining rounds without another
  reach defect (four in one day so far; the run is its shakedown);
  (2) the pending self-reference repair lands with red/green
  re-proof; (3) portability pass + absorb the beat-the-books tag
  linter, shipping ONE record checker. Graduation is a payload-
  boundary change: PLAN.md decision + verify line update
  (currently "payload inventory: statiker only"). Trigger: run
  end / stabilization. Consumer: run-grading pass.

- 2026-08-06 — **False-clean repair executed and independently
  verified (beat-the-books 2d22d054; meta-session re-ran the
  checker, output reproduces the desk's AFTER exactly).** Red/green
  shown both ways: F47→F80, F62→F79, D11→D57, D16→D56; C35/F77 no
  longer count. INSTRUMENT LESSON for the fire-rate review, second
  from this checker in one day: exemption-chasing on a negative
  predicate lost three consecutive rounds (each exemption left the
  next mention standing); the fix was INVERTING to a positive
  predicate — "is there a live non-C entry whose body states what
  survives" — the record's own convention made machine-checkable.
  General shape: where false positives come from an open-ended
  mention space, enumerate the ACCEPTING class, not the excluded
  one. Also: the sharpened predicate exposed six more orphans
  (D13/D17/D29/D31/F50/F56) the weak one masked — recorded C40
  unexamined, deliberately left red (scope discipline held). The
  fresh desk dispositions them pre-round-6. Consumer: fire-rate
  review + run-grading pass.
  ADDENDUM (round-6 staging): a SECOND instrument graduated
  repo-side — tools/statiker_tier_scrub.py (beat-the-books
  d03b9312, fail-closed, shown live pre-use; born from the
  re-paste hazard after the round-3 word-boundary miss). At the
  parked graduation decision, grade the two separately: the
  dead-basis checker is format-owned (payload candidate); the tier
  scrub is trial-phase comparison machinery and likely dies at
  stabilization with the blindness protocol rather than shipping.

- 2026-08-06 — **Tracker-verbosity docket item: DATA IN (desk
  measurement, round-6 staging).** Artifact growth 38.6k→46.3k→
  61.2k→75.6k tokens across rounds 3-6 (~+15k/round, compounding);
  attacker cost 237.7k (artifact × probe turns, prefix re-billing).
  Composition: 65% live bodies, 17% dead bodies (LOAD-BEARING for
  P3 closure — not waste), 19% non-entry prose, of which
  superseded handoffs + already-regraded verbatim attack quotes
  are the computable cut (~10-14k/round, kills the compounding
  term). C-lines 41 entries/11.6k — largely trial instrumentation,
  retires at stabilization. DECIDED PATH: artifact-build filter
  drops record-marked-superseded sections — filter the ARTIFACT,
  never the tracker; filter form stated in the brief. Applies from
  round 7 if the run continues (desk-authorizable, record-hygiene
  class); otherwise mints at run grading as a skill clause with
  this table as provenance. Entry-body compaction REJECTED:
  hand-consolidation is the paraphrase-drift class this run kept
  catching. Consumer: run-grading pass (+ round-7 go line if it
  happens).

- 2026-08-06 — **PARKED (operator-raised): incidental-findings
  surfacing clause for the skill.** Question: should statiker
  itself require surfacing/booking bugs, gaps, low-quality code
  found naturally during a run's work? Verdict: covered by
  inheritance — the corpus do-it-now-or-book-it ethic + BACKLOG
  roles, loaded in every desk session; this run's desks executed
  it four times (worktree surfaced+recorded, D48 rebooked to
  BACKLOG, F72 side-effect finding, C40 out-of-scope orphans
  recorded unexamined). Implicit routing observed: in-scope →
  F-line; out-of-scope actionable → target repo BACKLOG;
  needs-operator-decision → report + tracker record (chat-only
  surfacing dies with the desk). Mint trigger, named: an
  incidental finding that EVAPORATES in chat or gets misrouted —
  then the clause lands fire-born with that incident as
  provenance. Consumer: run-grading pass + any future fire.

- 2026-08-06 — **Self-containment DECIDED in principle (operator +
  meta concur; reopens PLAN.md's deliberate-context-dependence with
  distribution intent as the new evidence).** Shape settled:
  DEGRADATION FLOOR, not restatement — statiker inlines minimum
  essentials per seam (decision-complete test, brief-tail
  invariants, surfacing-as-record-routing, model-class defaults),
  each with an explicit composition declaration ("where the
  dispatch skill is installed, its forms govern — hook-enforced in
  the home environment"); ambient machinery stays primary where
  present, the floor makes the skill correct without it. Reframe
  banked: the parked incidental-surfacing clause is statiker-owned
  as RECORD ROUTING (F-line / backlog / report+tracker, never
  chat-only) and joins the layer independent of a fire. TIMING:
  stabilization, after the trial (the trial measures the current
  architecture); executed as ONE pass with the booked sentinel
  compression — compress and self-contain over the same lines.
  PLAN.md amendment lands when the pass does. Consumer: the
  stabilization pass + run-grading docket.

- 2026-08-06 — **STOP-CALL FIRED on round 6 (the relay-loop duty's
  first exercise) → action: sharpen-before-cycle-8, minted as
  0.2.9.** Two of A6's six findings are bites in classes existing
  mints govern — the named pause trigger. (a) F84 vs the 0.2.6
  commit obligation: D50 committed WITH nine executed surface
  traces yet missed the dict-key hop where the guards READ the
  value — trace reach fell short of the consuming read (2nd
  datapoint: A5's five-of-nine surfaces). Sharpen: the basis is a
  hop-trace reaching the CONSUMING READ, not a surface inventory.
  (b) F83's dropped pin + F85's lost D8 invariant vs the 0.2.5
  restate-survivors rule: D61 (written under the rule, same
  session) restated D31's decomposition and missed the pin clause;
  D47→D55 dropped the per-unit pin invariant (2 datapoints).
  Sharpen: survivor restatement is CLAUSE BY CLAUSE, each
  dispositioned restated-at-<id> or dead — the entry-level summary
  is where the load-bearing clause drops. Both rules held in FORM
  and failed in REACH; both sharpenings convert the judgment into
  an enumeration demand (un-fakeable artifact). NOT minted:
  per-unit red-first-pin skill clause — the impl phase hasn't run;
  its conduct clauses wait for its evidence (booked candidate, run
  grading). Desk decisions concurred: fresh desk for cycle 8
  (self-blindness case, its own D58-D61 are now attack surface);
  checker reach-line + alphabet widening NOW, pre-cycle-8
  (instrument work under the reopen; fixes the F86/C41
  verdict-without-reach class mechanically). Consumer: cycle-8
  brief + run-grading pass.

- 2026-08-06 — **Cycle-economics RE-DIAGNOSED (operator re-raised;
  fresh look with rounds 5-6 data) → SEVERITY-SCOPED CLOSURE
  decided (operator GO), applies from round 7's return; skill mint
  AFTER that first exercise, with it as provenance.** Revised
  finding-class trend: rounds 1-4 bit on design substance (money
  path); round 5 mixed; round 6 = ONE design finding (F84,
  moderate) + record/instrument findings (dropped pin clause, lost
  invariant, sweep under-count, non-discriminating verify set).
  The design has been converging since cycle 6; what sustains the
  loop is the RECORD maintaining itself — 212 entries/4.6k lines,
  every repair touch risks a supersession/reach error, each error
  feeds the next round: positive feedback the stop-call couldn't
  see because each bite WAS in a governed class (trigger kept
  saying "sharpen the rule" when the closure rule itself is
  miscalibrated for a converged design). Prior "fully warranted"
  verdict WEAKENED for rounds 5+ — evidence moved. Clippy
  comparison both ways: 3-4 cycles but this task's clippy run
  FAILED, f2 paused at cycle 49, and clippy-era "acceptable"
  shipped the defects this run measures = unmeasured residual.
  THE RULE (round-7 override, then mint): at a round's return the
  desk classifies each finding — DESIGN-SUBSTANCE (wrong mechanism
  / money path / silent failure in the shipped system) reopens as
  before; RECORD/INSTRUMENT-only bites CLOSE design — repairs
  booked, carried into implementation as record work, no next
  round. Downstream nets named: per-unit red-first pins, F38
  validator, U4a gate, isolated verify — cheaper residual catchers
  than a 240k-token round; forcing points 4-5 are the trial's
  unmeasured half. Consumer: round-7 go line + the post-round-7
  mint + run-grading pass.
  ADDENDUM (operator concurrence): the declining max-severity trend
  IS the convergence signature, and the operator's ~4-round prior
  from clippy experience is that signature observed across tasks —
  this run also converged in ~4 substantive rounds (1-4 substance,
  5 borderline, 6 record-dominated); the surplus rounds were the
  class-blind closure rule failing to read it. The severity-scoped
  rule is the prior in principled form: stops on CLASS, not count
  — correct on both tails (substance at round 5 → continue;
  converged at round 2 → stop), where a hardcoded round count
  fails both. Carries into the post-round-7 mint's rationale.
  MINTED NOW as 0.2.10 (operator: "why not update skill yet?" —
  correct; the post-round-7 hold was the same conservatism the
  0.2.6 early-mint already overrode, and build-first governs:
  provenance is the rounds-5/6 surplus itself, round 7 grades the
  mint instead of gating it). Mechanical form: classified findings
  append as F-lines FIRST, record repairs execute at return, the
  bare [ZERO-DELTA] lands LAST — closure stays computable, bare-tag
  rule intact. Round-7 go line returns to a bare (y); the clause
  rides the skill into the cycle-8 desk.

- 2026-08-06 — **Pre-cycle-8 lift audit (operator-raised: "anything
  booked that should lift first?") → TWO lifts, minted as 0.2.11;
  all other bookings correctly wait.** Lifted: (a) the artifact
  filter (was: round-7-go-line delivery; skill is the cleaner
  carrier — computable filter over record-marked-superseded
  sections, entries never filtered; provenance: the measured
  38.6k→75.6k growth table); (b) discriminating per-unit pins at
  [READY] (provenance: F83 HIGH — verify criterion true on the
  defective writer; F85 — five of eight units silently unpinned by
  a renumbering; fires at cycle 8's re-lock, which is why it lifts
  NOW despite the earlier impl-phase deferral — pin NAMING is a
  [READY]-moment obligation, only pin EXECUTION is impl-phase).
  Audited and left in place: shadow-log tension (parked, trigger
  unfired), checker + scrub graduation (parked, run end),
  incidental surfacing (parked, no fire), self-containment +
  compression (stabilization pass), self-referential-checker and
  positive-predicate lessons (corpus lane, fire-rate review),
  intake-grading cycle (future-run knob, run grading). Instrument
  work (reach line + alphabet widening) confirmed NOT done — the
  old desk was never continued; moves into the cycle-8 brief.
  Consumer: cycle-8 brief + run-grading pass.

## Session handoff — 2026-08-06 meta/grading session closed

State at close, for the successor meta session (role and duties:
CLAUDE.md Trial working conventions — the relay loop with harvest /
mint decision / stop-call / relay line, plus the lift-sweep before
each fresh desk): statiker 0.2.11 pushed + pinned (releases 0.2.4
→0.2.11 today, each fire-born, provenance in this file); global
corpus gained the carrier-on-read-path sharpen (dotfiles e05a7f6).
RUN STATE: canonical-market-identity reopened at A6 [BIT]; round 6
graded, stop-call fired once (0.2.9) and the severity-scoped
closure landed (0.2.10); cycle-8 brief ISSUED to the operator
(fresh opus desk, version gate 0.2.11, work item 1 = checker
alphabet widening + reach line, item 2 = re-derivation F83-first,
then round 7 presented for operator go — bare (y), everything
rides the skill now); both prior desks closed/abandonable, their
knowledge in tracker or brief. beat-the-books: 49 commits unpushed
under the operator's deploy hold — never push. OPEN BOOKINGS all
carry named triggers/consumers (lift-sweep graded them 2026-08-06:
two lifted as 0.2.11, rest wait): shadow-log tension (fire),
checker+scrub payload graduation (run end, 3 conditions),
incidental surfacing (fire), self-containment degradation floor +
sentinel compression at 227 lines (stabilization, ONE pass),
intake-grading knob + per-unit-pin-execution conduct + corpus
lessons (run grading / fire-rate review). EXPECTED NEXT EVENT: the
operator relays the cycle-8 desk's version-gate confirmation and
report; grade per the conventions. Succession decision pending the
trial's impl + verify (forcing points 4-5, still unmeasured).

- 2026-08-06 — **Cycle-8 desk relay graded (successor meta session;
  version gate 0.2.11 confirmed by the desk from the injection's
  base-directory line) → NO STOP-CALL; one mint, 0.2.12, pin held
  to the A7 seam; round-7 go = bare (y).** Harvest, per the report
  body: (a) F89 — D55/U4's commissioned deletion broker.py:364-418
  IS D33(a)'s three retained money-path guards; caught by the fresh
  desk's re-derivation PRE-impl, fixed at D64 (restate by symbol +
  grep residue check). Stop-call weighed and not fired: the trigger
  is impl/verify surfacing what attacks missed; this was caught at
  the seam the re-derivation exists to guard — and six attack
  rounds missing what the fresh-context re-derivation found is
  succession-POSITIVE evidence for the fresh-desk/self-blindness
  route. (b) Minted from F89 as 0.2.12: unit edit commissions are
  symbol-anchored with a residue check, never bare line ranges
  (clause at the [READY] seam beside the pin obligation; a
  literalist impl desk would have executed the range verbatim —
  the class escapes exactly where executor literalism is the rule).
  Release timing: COMMIT now, PIN moves at the A7 seam — round 7
  is staged and verified byte-identical against served 0.2.11;
  moving the pin pre-dispatch breaks that premise and burns the
  staging for a clause that fires at impl, not during the attack.
  Fresh desk at A7 picks up 0.2.12; owe the lift-sweep then.
  (c) 0.2.9's clause-by-clause sharpen EXERCISED and held: D61's
  count clause dispositioned dead at D65's nine-unit change,
  survivors restated clause by clause. (d) Work-item-1 brief defect
  harvested: literal alphabet [ACDFG] contradicted its own demanded
  demonstration — cross-clause consistency escaped the
  decision-complete audit; desk conduct correct (interpretation
  flagged, single ENTRY_ID constant, red-first known-positives,
  non-vacuous reach line). One datapoint; booked, not minted.
  (e) The widened checker went red on a real defect within the hour
  (F92, cross-run F-number import) — the manual-finding→mechanism
  rule paying out; instrument mint validated. (f) F90 (second dict
  floor), F91 (count stamped before its own append) — record class,
  repairs landed by the desk. (g) C51: two pre-authorized opus
  discovery legs missed horizon → stopped and reported per the
  horizon convention (held); one self-graded a routing error
  (two-read question in sweep's clothing), one retired by design
  (D67 makes the crosswise population a non-input). (h) Round-7
  staging graded GO: freeze scope verified, filter graduated to
  tools/statiker_artifact_filter.py with known-positives both
  directions BEFORE first use — the checker+scrub graduation
  booking's filter half landed early, in-run; booking stays for the
  run-end remainder. Docker daemon start: operator action,
  concur with desk — before impl so D65's NOT VALID premise is
  executed rather than cited; not blocking round 7 (rides as U4a's
  pin). Consumer: A7-seam release + lift-sweep, run-grading pass.

- 2026-08-06 — **Round-7 ABORT relay graded (desk C52-C54) → concur
  with the desk's self-stop; TWO mints as 0.2.13 (0.2.12 never
  pinned); pin moves 0.2.11 → 0.2.13 NOW; C54 to the operator with
  route-1 recommendation.** CORRECTION FIRST, own booking: the
  previous entry's item (g) — "horizon convention held", "leg
  retired by design was the better outcome" — rested on the desk's
  false closing claim that the two legs never returned. C52: both
  legs returned complete (twelve parts) after being stopped; the
  desk claimed "never returned" from memory, not the transcript.
  Item (g) is OVERTURNED both halves: the returns existed unread,
  and the "retired" leg's return (F93) refuted the very premise
  D67 cited — a booked verdict overturned by the evidence that was
  already in flight when it was booked. Harvest: (a) F93 —
  crosswise population is delete-and-recreate per sync cycle
  (1 → 17 in a 3-min window), F83's decay story was a sampling
  artifact; D67's conclusion survives on a corrected basis.
  (b) F95 — no substrate for any row-level migration pin (zero
  real-DB tests, no executed migration, CI pg16 structural-only);
  D67(b)'s escape clause correctly executed against itself: gap
  reported, never bridged. Round 7 rightly aborted (C53) — a
  verdict against a design due re-derivation cannot close it, and
  the artifact carried C51's false entry. (c) F94 — leg's claimed
  silent NameError refuted by executing the literal slice
  (IndentationError, ruff-caught); hazard real, mode wrong; desk
  settled D69 "line numbers may cite, never command" — CONVERGENT
  with the unreleased 0.2.12 F89 clause, now double-provenanced
  (F89 + F94) and sharpened with D69's cite/command wording.
  (d) G13 — writer pin executed red AND green (stored -2.50 at
  HEAD vs signature 2.5, +2.50 after fix): first firing LOGGED for
  the 0.2.11 discriminating-pin clause, strongest pin evidence of
  the run. MINTS (0.2.13): (1) leg lifecycle — a leg is [PENDING]
  at dispatch, resolved only by a body-read of its return, stopped
  or late legs included; folds into the existing [READY]
  no-[PENDING] gate, so unread legs hold the sweep open
  mechanically (provenance C52 + F93/F95: a round staged over a
  design whose refutation sat in two unread returns); (2) the
  cite/command sharpening above. Release basis: seam is C53's
  recorded abort — no attacker, no unit live; desk abandonable by
  design (tracker is the handoff); the leg clause fires at the
  next [READY], which the run crosses before any other forcing
  point. LIFT-SWEEP (fresh desk imminent): all open bookings
  re-graded, none ripe beyond the two minted — shadow-log (fire),
  scrub graduation remainder (run end), incidental surfacing
  (fire), self-containment+compression at now-240 lines
  (stabilization, ONE pass), pin-EXECUTION conduct (impl evidence;
  G13 noted as adjacent design-phase evidence, not impl conduct),
  intake knob + corpus lessons (run grading). BOOKED, corpus lane
  (operator decides): the transcript-claim rule's polarity — "it
  never arrived" is the same class as "I already sent it", checked
  in the transcript, never memory; the corpus line is phrased for
  the positive polarity only. C54 relayed to operator with
  recommendation route 1 (real-pg17 harness in U1; docker now up;
  also serves U4a/U4b; route 3 is the false-clean shape, route 2
  not decision-ready — per-row survival unmeasured). Consumer:
  fresh-desk start line + run-grading pass.

- 2026-08-06 — **C54 SETTLED (operator GO): route 1 — real-Postgres
  (pg17) harness built inside U1, in scope for this run; money-path
  data repair stays; docker daemon running.** Travels to the desk
  in the fresh-desk start line (carrier-on-read-path). Consumer:
  the fresh cycle-8 desk via relay; run-grading pass.

- 2026-08-06 — **Cycle-9 relay graded (fresh desk, version gate
  0.2.13 CONFIRMED — release loop closed) → NO STOP-CALL, NO MINT
  this relay; go = bare (y) for the sonnet inventory leg.**
  Harvest: (a) Re-lock correctly REFUSED — C54 decided THAT a
  harness gets built, not WHAT it is (image, lifecycle, schema
  arrival, driver, fixtures, CI stance pg16 vs pg17 all open);
  D68(b) holds U1 undispatchable until substrate settles. The stop
  rule doing its job — positive conduct datapoint against the
  premature-[READY] class this record already paid for. (b) F96/F97
  — D65's "docker down, root-gated" premise stale (29.7.1 reachable
  unprivileged); the whole NOT VALID premise EXECUTED on real
  pg 17.10, four of seven steps D65 never stated; D65 → D71
  restated with the premise measured. The execute-not-cite
  recommendation discharged. (c) INSTRUMENT FIRING logged: the
  cycle-8 dead-basis checker flagged D66's pin table routing its
  implementer to two invalidated entries (D66 → D72). (d) THIRD
  datapoint in the 0.2.9 clause-by-clause class: D66 restated
  "whole" carried two F92-refuted citations forward; desk's own
  probing caught them in-cycle pre-presentation, and found F98
  beyond F92's reach (three of nine pin paths non-resolving);
  D73 mints resolvable-paths as a standing record rule, discharged
  by execution (8/8). NO STOP: self-caught by the run's own
  machinery before anything rested on it; the durable fix is
  mechanical, not prose — BOOKED into the existing run-end checker
  graduation: widen the checker to (1) citation liveness against
  latest tags and F-line refutations, (2) path resolvability from
  repo root. (e) 0.2.13 leg-lifecycle clause unexercised this
  cycle (no legs outstanding); first exercise expected with the
  inventory leg — watch next relay for its [PENDING] line and
  body-read resolution. (f) Desk asked confirmation for a sonnet
  read-only leg under its own in-record C8/C4 despite the meta-side
  pre-authorization — correct per carrier-on-read-path (the desk
  never reads this repo's conventions); costs one round-trip we
  were in anyway. Model concurred: sonnet, mechanical inventory,
  no tier sensitivity. Consumer: next relay grading + run-grading
  pass.

- 2026-08-06 — **Opus skill-edit review EXPERIMENT pre-registered
  (operator-settled).** Scope: the next THREE SKILL.md releases
  each get one fresh-context opus review before the pin moves
  (brief = diff + full skill + question, no author reasoning;
  findings dispositioned before release). DECISION CRITERION,
  recorded before any review dispatches: the experiment SUSTAINS
  (opus review becomes the standing pre-release step) if at least
  one of the three reviews yields a finding that substantively
  changes the shipped text — structural, provenance, reach, or
  register, not wording; it RETIRES to the current
  stabilization-only review if all three return wording-only or
  empty. Grading is a body-read of the three raw review reports at
  the third release. Evidence basis, operator-relayed from another
  session (unverified here, labeled): (1) an opus-graded subagent
  report at top-tier conduct (instrument disclosed + proven red,
  refutation probes on its own verdict); (2) an opus vet catching
  a blocking factual defect in hours-old top-tier text; (3) the
  statiker attack-ladder pairing — opus arm out-bit fable arm,
  rounds 1-3, byte-identical artifacts (n=4, one domain, arms not
  blind). Consumer: the meta session at each of the next three
  SKILL.md releases + the grading at the third.

- 2026-08-06 — **Cycle-9 CLOSE relay graded → NO STOP, NO MINT this
  relay; round-7 go = bare (y); one rule-tension PRE-REGISTERED
  for grading at round 7's return.** Harvest: (a) FIRST FIRING of
  the 0.2.13 leg-lifecycle clause — the inventory leg's return
  booked from the file (body-read), leg stayed in its box,
  self-reported a discarded instrument (hand-rolled regex head
  count thrown out for real alembic heads), confirmed F95 under
  explicit invitation to contradict it. (b) F101 is the run's
  cleanest execute-over-reason datapoint yet: env.py's async
  engine, faithfully quoted, implies an async harness; EXECUTED,
  alembic's command API raises inside a running loop and
  asyncio_mode="auto" makes that every test — reasoning from the
  source would have shipped a landmine; sync end-to-end is right.
  (c) F99 — CI runs no pytest (instrument shown live: uv-run
  control 6 hits, pytest zero); "green in CI" gates nothing, so
  the harness pin is desk-executed by construction — recorded as a
  limitation, not hidden. (d) F100 — full 109-revision chain on
  fresh pg17-alpine in 0.5s incl. downgrade→upgrade round-trip;
  route (i) cheap. D74 decision-complete, discharging D68(b).
  (e) G14 — tools/statiker_ready_sweep.py born from the second
  hand-check of the gate (manual→mechanism rule followed); shipped
  BLIND to 7 of 265 ids, caught only by a reach cross-check
  against its sibling, then red-proven on a planted defect —
  instrument discipline held end to end; joins the run-end
  graduation set. PRE-REGISTERED TENSION (grade at round 7's
  return): C57 writes the desk's own weakest-spot list INTO the
  record explicitly for the attacker's eyes — "brief never
  carries the desk's reasoning" and "entries are never filtered"
  collide, since a record entry authored FOR the attacker routes
  desk reasoning through the protected channel. Cannot be
  unwound now (append-only, never filtered) and stopping buys
  nothing; the round is the natural experiment. Read criterion,
  fixed before return: if round 7's substantive bites fall ONLY
  inside C57's four named spots, that is the anchoring signature
  (mint candidate: no self-assessment entries authored for the
  attacker pre-round); bites outside C57's list = independence
  survived the framing, tension possibly benign. Consumer: the
  round-7 return grading.

- 2026-08-06 — **C57 class MINTED NOW as 0.2.14 (operator nudge
  correct; own prior deferral revised on the record): sealed
  prediction for pre-round self-assessment.** Revision basis: the
  pre-registered experiment is ASYMMETRIC — bites-only-inside-C57
  confirms anchoring, but bites-outside cannot establish safety
  (under-exploration is unobservable), so waiting could only ever
  confirm harm, never clear the channel; and the defect is readable
  from the rules themselves (the no-reasoning rule has a bypass by
  construction: entries authored for the attacker ride the
  never-filtered channel). Provenance: C57 in live operation IS the
  incident. Clause (The attack, beside the no-reasoning rule): the
  rule reaches the artifact; pre-round self-assessment is a sealed
  prediction — outside the pinned artifact (shadow log) until
  return, then landed beside the A-line compared against actual
  bites, converting attacker-framing into desk self-model grading.
  Round 7 unaffected (runs as registered on its pinned artifact;
  the C57 anchoring read still grades THIS round and feeds the
  mint's firing log). Pin moves at the round-7-return seam.
  This is release 1 of 3 under the opus-review experiment: one
  fresh-context opus review dispatches before the pin moves
  (read-only, pre-authorized tier), findings dispositioned in this
  ledger pre-release. Consumer: round-7 return grading (pin move +
  C57 read + review dispositions), experiment grading at release 3.

- 2026-08-06 — **Opus review 1/3 (release 1, 0.2.14) — TWO BLOCKING
  findings, both verified in the artifact and FIXED pre-release as 0.2.15
  (re-versioned 0.2.15 on the release hook's
  version-compare guard — a cached 0.2.14 would serve unrepaired
  text; pin still at 0.2.13).** B1: "the run's shadow log" was undefined
  in the payload (grep: sole occurrence was the clause itself; the
  definition lives only in maintenance files the desk never
  reads) — a desk's natural home for it, .clippy/runs/, sits
  inside the repo where the attacker's unrestricted READ sweep
  reaches it and where any tree==lock freeze claim breaks. FIXED:
  seal located in-file — desk's own scratchpad, outside the repo,
  with both failure mechanisms named. B2: the seal opened at round
  N+1 — landed "beside the A-line" without a form, the
  self-assessment becomes tracker content the next round's pinned
  artifact carries; the filter drops only record-marked-superseded
  SECTIONS and entries are unfilterable by design. FIXED: landing
  form specified — a section marked superseded at landing, never a
  tag-first entry. EXPERIMENT NOTE: review 1 of 3 produced two
  substantive (blocking-grade) catches on text the author had
  vetted — the sustain criterion's substantive-catch arm is
  already met once; grading still waits for release 3 per
  pre-registration. Both defects were RENDER failures (a term's
  load-bearing half lost, a landing form unstated), the class the
  author is structurally blind to — consistent with the
  fresh-context rationale. Parts 2/3 pending; dispositions on
  arrival, all before the pin moves. Consumer: pin-move moment +
  experiment grading at release 3.

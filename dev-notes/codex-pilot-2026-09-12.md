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

## Decisions this pre-registration does NOT cover

Global enablement (readiness.json class entry), codex as desk
(stage 3, parked), write-side lane certification (follow-on probe,
own registration).

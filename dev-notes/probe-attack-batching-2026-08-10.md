# Pre-registration — attack-round batching probe (2026-08-10)

Un-park trigger for the BACKLOG.md parked entry "attack-round
batching" (booked 2026-08-10): a paired probe — same locked designs,
batched attacker vs single-design attackers, pre-registered
per-design blocker-yield criterion, arms graded before outcomes are
compared. Operator GO 2026-08-10 ("can we run a probe?"). This file
is committed BEFORE any arm dispatches (repo convention: comparison
experiments pre-register; the commit timestamp is the proof of
order). Grader: the dispatching desk session (fable), which wrote
this file and composes the briefs; arms are fresh contexts that do
not know a comparison is running.

## Substrates (frozen; identical per design across arms)

- **DESIGN-1**: the canonical-market-identity statiker run,
  beat-the-books `.clippy/runs/2026-08-05-canonical-market-identity-statiker.md`,
  pinned at lock commit `83025023b83daf88d93704bf14ae11156c5c4126`
  (the A8 lock). The pinned state PRE-dates A8's report, so A8's
  recorded yield at this exact state — nine findings: 1 HIGH, 5
  MODERATE, 3 MINOR (tracker A8 line) — is a reference yield,
  invisible to the arms. Artifact produced by the production tool:
  `statiker_record.py filter --tracker <path> --sha 8302502… --out
  <outside-repo path>` (line-number-preserving, Superseded species
  blanked), one copy per assigned agent.
- **DESIGN-2**: the clippy-era line-matching run, beat-the-books
  `.clippy/runs/2026-07-27-line-matching-tiers12.md` (+ its
  impl-plan file), pinned at `289c7d8b` (the state the recorded
  round 9 then attacked, finding a real defect — "persistence owner
  mis-sited", commit af4550dc — so the pinned state has a
  demonstrably nonzero true-finding population). Served verbatim at
  the pinned commit (no blanking: clippy grammar has no Superseded
  species — declared asymmetry; identical per design across arms,
  so the comparison stays internally valid).

Each agent gets its OWN worktree per assigned design, detached at
the pin (read+execute isolation: attack probes may execute code and
must not share a tree with another arm). The brief asserts tree ==
pin; the attacker verifies HEAD equals the pinned sha and
`git status --porcelain` clean before reading.

## Arms (all opus — beat-the-books' pinned attack tier; all fresh contexts)

- **SINGLE-1**: one attacker, DESIGN-1 only.
- **SINGLE-2**: one attacker, DESIGN-2 only.
- **BATCHED**: one attacker, BOTH designs in one brief, fixed order
  DESIGN-1 (large, ~7.6k-line artifact) then DESIGN-2 — the tail
  position is where attention depletion would show, and batched-D2
  vs SINGLE-2 is the load-bearing comparison.

All three briefs carry the same attack charge (SKILL.md "The
attack": fit to the recorded requirement and the factual bases
cited; DECOMPOSITION; SIMPLICITY) with the evidence-reach block
pasted verbatim, and the read-only tail. No seal/queue plumbing (no
live desk round — declared deviation from production; the probe
measures attacker yield, not desk conduct). Briefs are
verifier-form: artifact + question only, no dispatcher reasoning,
no mention of the other arms or of this probe.

## Decision criterion (pre-registered; decides the un-park)

1. The desk grades EVERY finding from all arms for validity and
   severity — body-read plus re-execution of executable bases at
   the pinned state — BEFORE any cross-arm comparison is computed.
   A finding is a **confirmed blocker** iff (i) valid at the pinned
   state and (ii) HIGH-or-above severity by its own demonstrated
   mechanism, or design-reopening under statiker's reopen rule.
2. **The batched arm HOLDS iff, for EACH design separately,
   confirmed-blocker count (batched) ≥ confirmed-blocker count
   (single arm for that design).** Equality holds.
3. **Vacuity guard**: a design on which BOTH arms yield zero
   confirmed blockers decides nothing for that design (an outcome
   consistent with both verdicts); if both designs are vacuous the
   probe is UNDECIDED and the entry stays parked — a vacuous pass
   cannot un-park.
4. Outcome mapping: HOLDS on every non-vacuous design (≥1
   confirmed blocker somewhere across arms) → the parked entry
   un-parks toward ready (batched-round form with per-member
   disposition so a batched round cannot silently under-attack its
   tail). FAILS on any design → stays parked; the sequential
   default stands, now on a measured basis. Either way the
   measurement is recorded here, below this line, at grading.

## Secondary observables (recorded, never deciding)

Total findings per design per arm; severity mix; finding-set
overlap between arms; whether the batched arm's tail-design
findings skew to shallow classes (record hygiene) relative to
SINGLE-2's.

## Declared limits

n=1, one repo, one design pair, arms not blind to content, single
grader. A HOLDS result is evidence for un-parking, not a general
certification of batching; a FAILS result binds only this shape.

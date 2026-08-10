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

---

## GRADING (2026-08-10, dispatching desk, after all arms returned)

Arms returned complete: SINGLE-1 (6 parts), SINGLE-2 (7 parts),
BATCHED (9 parts). All pins verified by the arms (md5 identity
artifact↔tracker on both designs, porcelain clean). Validity
grading ran before any cross-arm comparison; per-finding grades and
compact bodies are in the two evidence files delivered to the
findings' consumers:
`beat-the-books/.clippy/runs/evidence/2026-08-10-probe-batching-attack-findings-{cmi,line-matching}.md`.
Raw arm reports: this probe session's transcript.

**Deciding re-executions by the desk** (the rest body-read against
pasted executed output): (1) the cross-arm factual conflict on the
sport enum — desk read of `domain/types.py:17-35` at 289c7d8b shows
BOXING and MIXED_MARTIAL_ARTS present; SINGLE-2's A stands, the
batched arm's D2-6 grade rested on a wrong enum read. (2) BATCHED
D2-1's alembic basis — single-transaction migration confirmed, zero
escape-hatch hits, NOT-CLEAN round-8 artifact at the pin. (3)
BATCHED D1-1's chain — D55 body zero-hits for the carried clauses,
D47 [INVALIDATED], U7 body a pointer.

**Confirmed blockers (HIGH-or-above by demonstrated mechanism):**
- DESIGN-1: SINGLE-1 = 0 (its M1-M4 are MODERATE, all confirmed);
  BATCHED = 1 (D1-1). 1 ≥ 0 ✓
- DESIGN-2: SINGLE-2 = 1 (A — confirmed as a reach/closure defect,
  exposure latent); BATCHED = 1 (D2-1). 1 ≥ 1 ✓
- Non-vacuous (blockers exist on both designs).

**CRITERION RESOLVES: HOLDS → the parked entry un-parks** (moved to
READY in BACKLOG.md, same date).

**Secondary observables (recorded, non-deciding):**
- Totals per design/arm — D1: single 4M+3m, batched 1H+1MH+2M+1m;
  D2: single 1H+1MH+2M, batched 1H+2M+4m. No tail yield collapse:
  the batched tail block contains the probe's deepest finding
  (D2-1).
- The finding SETS are largely disjoint across arms (overlap:
  U5-reversibility, R5-reach, round-8-staleness). At n=1,
  attacker-to-attacker variance is comparable to any arm effect —
  the criterion is met, but "batched ≥ single" here partly reflects
  different attackers finding different true defects, not
  demonstrated equivalence of attention. Recorded as the standing
  caveat on the HOLDS.
- Tail-accuracy slip: the batched arm's one demonstrable factual
  error (the enum read behind D2-6) occurred on the TAIL design —
  a depletion signature in accuracy, not yield. The per-design
  disposition form the un-parked entry mandates is the designed
  counter.
- EMERGENT: the batched arm produced a cross-design coupling
  finding (P-X1: opposite-direction edits to shared call sites, a
  premise expiry, an ordering contradiction) that single-design
  rounds cannot produce by construction. Not in the pre-registered
  criterion; recorded as an independent benefit of batching.

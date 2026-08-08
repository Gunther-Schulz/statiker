# Clippy lineage — evidence register for statiker deliberation

Written 2026-08-08, statiker 0.2.48 era, by a fable session with the
operator. Consumer, named at write time: the meta/grading session —
at opus-ladder grading, at hypothesis-patch minting, at fire-rate
reviews, and at the stabilization compression pass (all booked or
standing in this repo). Pointer lives in CLAUDE.md.

## Epistemic status — read first

This file LOOSELY INFORMS; it is not a target list. The weakness
classes below are one operator's observations, accumulated by slowly
iterating clippy against practice and watching it — the catalog may
itself lack classes, and designing statiker AGAINST exactly this
list would inherit its gaps as blind spots. Observations add
information, nothing more (operator, 2026-08-08). Method and reach
of this synthesis: Stichproben at six repo states of
`~/dev/Gunther-Schulz/coding-clippy` — headings plus selected
sections, not full-body reads — so every claim carries its git ref
and is checkable/deepenable there; the clippy git history is the
durable raw store, this file is the judgment pass over it (which is
the part that dies with a session). Snapshot as of the 0.2.48 era;
a later reader re-grades against later evidence rather than
trusting this label.

## The sampled states

| Ref | Date | Payload | Character |
|---|---|---|---|
| `fa1fe1e` | 2025-05 | CLIPPY.md 92 KB monolith | Step-numbered workflow, explicitly optimized for gemini-2.5-pro (model-check BLOCKER at step 0); verify-every-diff-line; step-prefix proof-of-compliance; operator BLOCKER gates |
| `85d3d10` | 2025-11 | 68 KB + AI_BEHAVIOR_PATTERNS.md | Sectioned rules + explicit weakness catalog P1–P8, each mapped to counter-machinery ("Protocol Design Implications") |
| `03a0c8a` | 2025-12 | CLIPPY_MKII.md 70 KB | Tracker born, IN-CHAT: [PENDING]/[PARTIALLY VERIFIED]/[VERIFIED], mandatory ASSUMPTIONS section, READY/NOT-READY gate, menu keys; V1: verification needs 2–3+ components read, "never from grep alone" |
| `f96b3e5` | 2026-02 | 54 KB | Same protocol ported to Cursor skill + subagent architecture |
| `e7fde3f` | 2026-05 | tracker batch | Tracker externalized to per-run append-only files (.clippy/runs); adherence-audit procedure (`acea658`) |
| HEAD (`2ee5888`) | 2026-08 | lean/protocol.md, 211 lines | Two gates (LOCK, verify), fresh-context falsification dispatches, served-attack register, budgets |

The Nov-2025 catalog (P1 unasked improvements, P2 false confidence
from polish, P3 no incremental validation, P4 cannot self-question,
P5 assumption-based generation, P6 over-helpful local
optimizations, P7 batch-instead-of-iterative, P8 procedural
execution without understanding) is the era's own enumeration of
what it fought — same single-observer caveat as above.

## The weakness ledger — what the sheddings measure

Machinery deleted and never re-added is a measurement that its
target class lessened below the pain threshold; machinery that only
got LIGHTER marks a class still alive.

- **Disappeared** (machinery deleted, never returned): mechanical
  execution fidelity — verify-every-diff-line, tool-output
  skepticism, imports-exist fact-checks (`fa1fe1e` "Absolute
  Critical Checks"). Models stopped mangling edits and hallucinating
  dependencies. Re-adding any of this for a lower-tier desk would be
  ceremony against a dead class.
- **Lessened but alive — the grounding constant**: P2+P5
  (premature confident judgment; fact assumed from cursory
  inference). Never left; machinery got ~10× lighter, not absent:
  Dec-2025 always-rendered ASSUMPTIONS section + numeric breadth
  quota → today's [AUTO-ACCEPTED] tags + the attack's reach-matched
  evidence block. Tier-persistent: statiker's founding incident is
  fable committing this class (skim-and-build; OBSERVATIONS.md).
- **Lessened but alive — self-blindness** (P4): never solved,
  re-homed. The operator-gate that compensated (BLOCKERs, menu
  stops) became the fresh-context attack. The one class whose
  machinery was never deleted in fifteen months, only restructured.
- **Lessened but alive — ADHERENCE itself** (operator, 2026-08-08):
  much of the old bulk (step-prefix proof-of-compliance, menus,
  checkpoint templates — "make it structurally impossible to skip",
  `85d3d10` implications §7) existed because instructions did not
  stick at all. skill-craft distilled from this experience — what
  makes skills adhere. Operator judgment: fable is the first model
  with a real chance of writing skills that stick; even at opus,
  effective skill-writing is very hard. Bears directly on statiker:
  the thin-forcing-point density is calibrated to a fable desk
  (SKILL.md, The loop), so a lower-tier desk raises an adherence
  question BEFORE any judgment-quality question.
- **Morphed — P8 inverted**: the old fear was mechanical
  procedure-following by the desk; Nov-2025 already counsels
  "conceptual over sequential", and statiker's free loop is that
  fully realized. The class moved to the BRIEFED tier, where
  literalism is now the defended interface (statiker's
  commissioned-line-range scar, SKILL.md Implementation).
- **Mechanized, not deleted**: the proof-of-compliance layer —
  chat step-theater became the on-disk tracker plus tools emitting
  verdict lines. Invariant across all six states: make the
  invisible process visible to something other than the working
  model's in-flight judgment.

## Deliberation loads (what this register is FOR)

1. **Opus-ladder pre-registration.** Watch two distributions across
   trial runs, both readable from trackers: (a) bite-class — attack
   findings that are reach-failures on cited bases (depth; the
   designed circuit catching it) vs. new-facts-never-looked-at
   (breadth; the desk's sufficiency judgment failing invisibly);
   (b) adherence — forcing points skipped or malformed at the desk
   (clippy's adherence-audit, `acea658`, is the shelf instrument).
   Recurring breadth or adherence misses indict the FORM at that
   tier, not the run.
2. **Known-working fallbacks, one notch at a time.** Each alive
   class has a heavier predecessor that worked at lower capability:
   breadth → the Dec-2025 numeric quota / always-rendered
   assumptions (`03a0c8a` V1, TRACKER rules); self-blindness →
   operator gates at seams (attended-mode [READY] IS the BLOCKER
   pattern); adherence → structural impossibility of skipping
   (tools gating instead of prose). Repairs enter as hypothesis
   patches with the trial incident as provenance — never
   pre-built, and never designed from scratch when a shelf shape
   exists.
3. **The nostalgia guard — held loosely.** When adding machinery,
   ask which class it serves; if the ledger says the class
   disappeared, the addition is suspect. But per the epistemic
   status above, the ledger's absence of a class is weak evidence —
   the question informs, it never vetoes on its own.

## Lineage context (operator, 2026-08-08)

Clippy was built through painfully slow iteration: observe in
practice → adjust → observe again. skill-craft evolved from this
same experience, distilling what makes skills work, especially
adherence. That history is why this register exists as
OBSERVATIONS with named refs rather than as rules: the slow loop is
the method; this file just spares a successor the re-derivation of
one pass through it.

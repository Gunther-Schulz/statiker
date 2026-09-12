# Decision memo: does the compression pass continue, and does 80–150 stand?

For: the operator, in discussion with statiker-a5 (fable).
From: statiker-df (opus desk, statiker maintenance arc), 2026-09-12.
Status: the operator has moved this decision to statiker-a5's session
and will discuss it there. This memo is the evidence, not a directive;
statiker-a5 holds no delegation from this desk on it.

## The question, in one line

The compression pass was the arc's route from a 1,766-line skill page
to PLAN.md's 80–150 target. Lap B — its heavy lap — is now measured,
and it does not move the page. So: does the pass continue to lap C,
and does the 80–150 target stand?

## What is measured (every figure below was executed, not projected)

Operational line counts, by CLAUDE.md's own Verify awk:

| state | operational lines |
|---|---|
| `769e7f2` — before lap A | 1766 |
| `0775b92` — after lap A (delete + tighten) | 1628 |
| `3c041e5` — after the st-35 arming work | 1638 |
| HEAD — after lap B's route-vocabulary section | 1689 |

Lap B's remaining effect, from the stage-1 clause table
(`docs/audits/2026-09-12-st32-lapB-clause-dispositions.md`, 28 rows
over a 510-line object):

- **66 lines leave** (measured).
- **51 lines were added** (measured — the vocabulary section, landed).
- **444 lines "stay"** — NOT a measurement. A sum of target lengths
  for text a build lane has not written yet.

## Why the staying figure cannot be trusted, and what it does to the net

Lap A's per-row targets were written by the same class of instrument.
Comparing them against what lap A actually delivered (desk re-measure
over 15 rows): **14 over target, 1 at it, 0 under; 197 budgeted, 246
delivered — ~25% light.** The table lane measured the same direction
at ~19% (the gap is range-boundary convention; both are one-sided,
which a counting difference would not produce).

At ~20% overrun the staying text lands near **533** against the **510**
lines standing there today. So lap B's net line effect **cannot be
signed**: it is −15 if the targets hold, and positive if they overrun
as lap A's did.

## Why the method cannot reach the target — the structural finding

This is the part that matters more than any number. Of the 28 clauses
in lap B's object:

- **0 precipitate cleanly.** Every clause whose routing leaves also
  carries load a name-keyed registry cannot hold — a predicate, a
  write-side template, or a seam-dependent exception the route token
  cannot express.
- **148 of the 510 lines carry no verdict token at all** (what lap A
  marked "record read-side semantics"). A verdict-NAME → route
  registry cannot reach them even in principle.

The page's mass was never per-verdict routing. Precipitating routing
into the tool was the pass's main mechanism, and the mass it was aimed
at is not there.

## What the record already settled, so it is not re-opened here

- The size-target **re-derivation is booked and operator-concurred**:
  "the number is an outcome, not a gate" (OBSERVATIONS 2026-08-10),
  consumer named as the compression pass.
- statiker-fb's projection (650–750 after the pass) is **dead**: its
  first link assumed lap A landing at 1100–1200, and lap A landed at
  1628.
- statiker-a5's own §6 projection (~1440 after lap B) is superseded by
  the measured ~1623-or-more above.

## The options, with their costs

**A. Stop the pass as a size programme.** Lap C's booked
re-derivation becomes the honest close: PLAN.md's Size target section
takes an append-only supersession entry whose number is the measured
residue, with this memo's evidence as its basis. The remaining
conduct-prose tightening still happens, judged on readability, not on
a line budget. Cost: the 80–150 target is formally abandoned.
Stage 2 (rewriting ~444 lines) is **not** run.

**B. Run stage 2 anyway, then decide.** Cost: a full build lane plus
its share of a checkpoint review, spent rewriting 444 lines for a net
effect whose sign is unknown. If the answer is then A, that rewrite is
waste.

**C. Hold 80–150 as binding.** Then the only routes left are
single-home amendments — a `references/` split or disclosure — which
PLAN.md's "Single-home by design" decision currently forbids, and
which statiker-a5's own design flagged as a decision, not a finding.
This is the option that re-opens a settled design decision, so it
needs to be wanted for its own sake.

## This desk's recommendation

**A**, with one qualifier. The trial's stated value is the forcing
point, the fresh-context round, and a record good enough to resume
from — not the line count. A page of ~1,620 lines that a desk actually
follows is worth more than a 150-line page that drops the conduct the
incidents bought. The 80–150 number came from before any of this was
measured, and the re-derivation was booked precisely for the case
where measurement disagreed with it. It now does.

The qualifier: **A is not "the page is fine".** ~1,620 lines is still
the arc's largest standing liability, and lap C should re-derive a
target that is honest rather than drop the question. What A abandons
is the claim that precipitation-to-tool gets there.

## What this desk has already done, either way

- Stage 2 is **held** pending this decision (booked in LEDGER) — it is
  the expensive half and option A makes it waste.
- st-34, st-35 and lap B's registry half are built, verified and
  unpushed at 0.2.89; they close at the release regardless of this
  answer.
- The three conduct re-routings the design carried (`PINNED_REWRITTEN`,
  `UNIT_GATE_BLOCKED`, `UNIT_COLLISION`) are booked separately as
  behaviour changes, not shipped inside a representation lap.

## Pointers

- Stage-1 table: `docs/audits/2026-09-12-st32-lapB-clause-dispositions.md`
- Lap B design: `docs/directives/2026-09-12-st32-lapB-design-statiker-a5.md`
- Measurements and rulings: `dev-notes/OBSERVATIONS.md`, the
  2026-09-12 sections
- Decisions: `LEDGER.md`, the 2026-09-12 lines

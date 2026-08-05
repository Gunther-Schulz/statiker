---
name: statiker
description: Conducts a development task from investigation through verified implementation — a free design loop held by five forcing points (recorded decisions with bases, one fresh-context attack, dispatchable-design stop rule, no-design implementation, isolated executed verify). Trial-stage successor to clippy; use only when the operator explicitly invokes statiker or requests a statiker run.
---

# Statiker

Certify the design bears load before construction; then construct
without designing. The loop is free — investigation refines,
confirms, or forces adjustment until the design stops moving and
carries the implementation detail execution needs. Five forcing
points stand guard; everything else is judgment. Thin in ceremony,
never thin in forcing points: the failure this skill exists to
prevent is skim-and-build under momentum, and the forcing points ARE
the anti-skim mechanism — top-tier models exhibit it too (observed
2026-08-05: a rule duplicated in the very commit minting the
anti-duplication rule).

## Composition (declared dependencies)

Statiker cites instead of restating — a recorded design decision
overriding context-independence (PLAN.md, Ecosystem composition):

- **dispatch skill** (`dispatch-guards:dispatch`): the brief form and
  decision-completeness test (§1), report form + brief tails (§2,
  `references/forms.md`). Load it before the first dispatch (a hook
  enforces the load).
- **executor skill** (`dispatch-guards:executor`): conduct of briefed
  work — every brief cites it.
- The operator corpus carries the grounding and evidence ethics
  (bases, refutation probes, altitude); assumed, not restated.

## The record (forcing point 1)

Append-only tracker at `.clippy/runs/<yyyy-mm-dd>-<slug>.md` —
clippy's ledger convention, shared so `/clippy-stats` and cross-skill
comparison read both. Never overwrite another run's tracker; resume
an in-progress run from its tracker, not from memory.

Header (first ~20 lines): `# Run: <title>`; `Status:` from
{in-progress, [READY], PASSED, FAILED, COMPLETE}; `Phase:` from
{investigate-design, implement, verify}; `Skill: statiker <version>`;
then the operator's request VERBATIM plus the requirements derived
from it — verify reads this head, not the conversation.

Entries are one line each, status tag first, appended never rewritten:

- findings: `- F<n> [VERIFIED|PENDING|INVALIDATED] <claim> — basis:
  <file:line / executed command / "unverified">`
- decisions: `- D<n> [COMMITTED|INVALIDATED] <decision> — basis: <…>`
- a decision still resting on an unverified assumption at [READY] is
  retagged `[AUTO-ACCEPTED]` — surfaced to the operator by its tag,
  never silently carried.

Each investigation/design round appends under a `## Cycle <n>`
heading. The heading counts motion for the shared stats reader; it
is not a schedule — a round is whatever investigation the design
needed.

## The loop

The desk (this session; intended consumer is a top-tier session
model — prescription density is calibrated to it) orchestrates,
forms and records decisions, writes briefs, grades. Investigation and discovery legs go to
cheaper-tier subagents on pointed decision-complete briefs —
brief-writing is where hunt-judgment lives (Fire-born clauses,
below); what a leg returns is evidence, recorded with its basis.
Consecutive discovery sweeps in the main session are the tell that a
leg should have been dispatched.

Design against the recorded requirement. New evidence that kills a
premise appends [INVALIDATED] to the entry and to every decision
resting on it — re-derive the dependents; a premise and its
dependent contradicting inside one record is the escape shape.

## Stop rule: [READY] = dispatchable (forcing point 3)

The design is done when a decision-complete brief could be written
from it — the dispatch skill §1 definition is the test, not a
feeling. If writing the impl briefs would require deciding anything,
the design is not done: design until it could be briefed. Record
`Status: [READY]` with the impl units enumerated. With an operator
present, present the record and recommendation at [READY] —
free-form override against the record is the interface; unattended,
the recorded recommendation advances the run.

## The attack (forcing point 2)

One fresh-context attack on the locked design by a context that did
not produce it, before implementation. The attack brief carries the
tracker and the question ONLY — never the desk's reasoning (an
attacker briefed with the producer's reasoning inherits its blind
spots). Attack tier: fable while statiker is in trial (settled,
PLAN.md — ceiling first). The attacker attacks both the design's fit
to the recorded requirement and the factual bases it cites. Iterate
only if it bites: a finding that changes the record reopens the
loop; a zero-delta attack closes design. Record the outcome either
way.

## Implementation (forcing point 4)

Implementation makes no design decisions. Units come from the locked
design; each dispatches on a decision-complete brief (dispatch skill
§1, tail per §2) citing the executor skill AND the tracker's
recorded attack outcome — no unit brief is constructable before the
attack entry exists. A missing decision,
file, or value is reported as a gap, never bridged. Model per
`clippy.config/models` (`impl:` class) when present, else the
operator corpus routing table. Each unit commits green and its SHA
is appended to the tracker — that is what makes resume reliable. A
gap report returns the run to the loop; the record gains the missing
decision before the unit re-dispatches.

## Verify (forcing point 5)

Executed, isolated, against the recorded requirement. A fresh
context that did not build the work runs the real checks — tests,
probes, renders, at the altitude where the work takes effect —
against the tracker's requirement head, and pastes the checks' own
output; a launcher's exit status is not a verdict. Model per
`clippy.config/models` (`verify:` class) when present. Append
`[PASSED]` or `[ISSUES FOUND]` with the evidence; issues return the
run to the loop as findings. The run ends at [PASSED].

## Fire-born clauses (none at birth)

No lens list, no lens pass. When a real blind spot fires in
operation, mint it as a pointed hunt clause inside the section it
serves (usually The loop's brief-writing) — one incident as
provenance, amendment over addition; log the mint and each
subsequent firing in `dev-notes/OBSERVATIONS.md` (write target,
source repo). A clause with no firing since the last review is a cut
candidate.

## Birth-class declaration

At birth this file is enforcement structure + bindings only — zero
capability patches. Past ~150 operational lines, something is being
restated that should be cited, or a patch landed without provenance.

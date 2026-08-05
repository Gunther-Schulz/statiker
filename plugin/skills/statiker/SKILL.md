---
name: statiker
description: Conducts a development task from investigation through verified implementation — a free design loop held by five forcing points (recorded decisions with bases, a fresh-context attack on each locked design, dispatchable-design stop rule, no-design implementation, isolated executed verify). Trial-stage successor to clippy; use only when the operator explicitly invokes statiker or requests a statiker run.
---

# Statiker

Certify the design bears load before construction; then construct
without designing. The loop is free — investigation refines,
confirms, or forces adjustment until the design stops moving and
carries the implementation detail execution needs. Five forcing
points stand guard; everything else is judgment. Thin in ceremony,
never thin in forcing points: the failure this skill exists to
prevent is skim-and-build under momentum, and the forcing points ARE
the anti-skim mechanism — top-tier models exhibit it too (incident
provenance: the source repo's dev-notes/OBSERVATIONS.md).

## Composition (declared dependencies)

Statiker cites instead of restating — a recorded design decision
overriding context-independence (PLAN.md, Ecosystem composition):

- **dispatch skill** (`dispatch-guards:dispatch`): the brief form and
  decision-completeness test (§1), report form + brief tails (§2,
  `references/forms.md`). Load it before the first dispatch (a hook
  enforces the load).
- **executor skill** (`dispatch-guards:executor`): conduct of briefed
  work — every EXECUTION brief cites it; verifier and attack briefs
  never do (a fresh context briefed with conduct-of-building material
  is being framed as a builder).
- The operator corpus carries the grounding and evidence ethics
  (bases, refutation probes, altitude); assumed, not restated.

## The record (forcing point 1)

Append-only tracker at `.clippy/runs/<yyyy-mm-dd>-<slug>.md` —
clippy's ledger convention, shared so `/clippy-stats` and cross-skill
comparison read both. Never overwrite another run's tracker; resume
an in-progress run from its tracker, not from memory. An entry
ADOPTED from a record this run did not produce — a prior or
superseded run's tracker, or the session's own earlier items — is
PENDING until its basis passes a current-check scoped to the claim
(re-read the cited lines; staleness-check against commits since the
basis read — an earlier item's own implementation invalidates reads
of the files it touched); re-record it as a new line under this
run's own next id, citing source AND check. Unrecorded memory of
prior work is never a basis.

Header: `# Run: <title>`; `Status:` from
{in-progress, [READY], PASSED, FAILED, COMPLETE}; `Phase:` from
{investigate-design, implement, verify}; `Skill: statiker <version>`
— Status and Phase within the first ~20 lines (the stats reader's
admission window). After the header, the requirement head: the
operator's request VERBATIM plus the requirements derived from it,
as long as it needs to be — verify reads this head, not the
conversation. The header's Status and Phase fields are the record's
ONE mutable surface, updated at each transition and at the verify
verdict; everything below them is append-only.

Entries are one line each, status tag first, appended never
rewritten. A status change is a NEW tag-first line for the same id
(`- D<n> [INVALIDATED] <why> — basis: <…>`) — never an edit of the
old line; the stats reader counts only tag-first lines.

- findings: `- F<n> [VERIFIED|PENDING|INVALIDATED] <claim> — basis:
  <file:line / executed command / "unverified">`
- decisions: `- D<n> [PENDING|COMMITTED|INVALIDATED|AUTO-ACCEPTED]
  <decision> — basis: <…>`
- attack outcomes: `- A<n> [DISPATCHED|BIT|ZERO-DELTA] <summary> —
  basis: <brief at dispatch; report ref on return>`
- a decision still resting on an unverified assumption at [READY]
  gets an appended `[AUTO-ACCEPTED]` line — surfaced to the operator
  by its tag, never silently carried.

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
premise appends an [INVALIDATED] line for the entry and for every
decision resting on it — re-derive the dependents; a premise and its
dependent contradicting inside one record is the escape shape.

## Stop rule: [READY] = dispatchable (forcing point 3)

The design is done when a decision-complete brief could be written
from it — the dispatch skill §1 definition is the test, not a
feeling. If writing the impl briefs would require deciding anything,
the design is not done: design until it could be briefed. [READY] is
recordable only when the record sweeps clean: no entry's latest line
is [PENDING], and no id appears as two live entries (duplicates are
found by body-read, not tag grammar) — an open [PENDING] under a
claimed [READY] is the premature-call shape.
Record `Status: [READY]` with the impl units enumerated. With an
operator present, present the record and recommendation at [READY],
ENDING with one advance prompt — "(y) advances per the
recommendation"; anything else is free-form override. Design
decisions are never posed as choices; the prompt carries loop
control only. Unattended, the recorded recommendation advances the
run.

## The attack (forcing point 2)

A fresh-context attack on each locked design by a context that did
not produce it, before implementation. The attack brief carries the
tracker, the question, and the read-only tail (dispatch skill
`references/forms.md`); the probe obligation rides INSIDE the
question, and probe execution is read-only (transient scripts in the
attacker's own scratchpad are not report files). The obligation:
every severity, closure, or HOLD verdict rests on evidence whose
question MATCHES the verdict's reach — an executed probe where the
object exists to execute, a full source-chain trace (every hop
cited) where it is still design prose; a closure names what the
guarded input meets on the NEW path. Evidence answering a narrower
question than the verdict it closes is the false-clean shape. A
verdict without reach-matched evidence is labeled unmeasured and
leaves its question OPEN. Judgment findings (design-intent, record
hygiene) bind no probe — the obligation is on verdicts, not
discovery. The brief never carries the desk's reasoning — it
transmits the producer's blind spots. Attack tier: fable while statiker is in trial (settled, PLAN.md —
ceiling first). The attacker attacks both the design's fit to the
recorded requirement and the factual bases it cites. Iterate only if
it bites: a finding that changes the record reopens the loop, and a
re-derived design is a NEW locked design — it gets the attack again,
by a NEW fresh context (a resumed attacker inherits its own prior
findings' frame). Each round records an A-line (The record):
[ZERO-DELTA] only when every verdict is reach-matched and nothing
bit — that closes design; any other return, findings or unmeasured
verdicts alike (each unmeasured verdict is an open question),
records [BIT] and design stays open.

## Implementation (forcing point 4)

Implementation makes no design decisions. Units come from the locked
design; each dispatches on a decision-complete brief (dispatch skill
§1, tail per §2) citing the executor skill AND the run's latest
A-line, which must be `[ZERO-DELTA]` and postdate the current lock —
a re-locked design's unit briefs cite ITS closure, never a
superseded lock's (The attack). A missing decision,
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
output; a launcher's exit status is not a verdict. The verify brief
carries the tracker, the code, and the question — read-only tail,
no executor cite. Model per
`clippy.config/models` (`verify:` class) when present. Append
`[PASSED]` or `[ISSUES FOUND]` with the evidence and set the header
Status to match (PASSED, or FAILED on an abandoned run); issues
return the run to the loop as findings. The run ends at [PASSED].

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

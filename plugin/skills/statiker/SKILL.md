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
provenance: dev-notes/OBSERVATIONS.md in the source repo,
github.com/Gunther-Schulz/statiker — home of all PLAN.md and
dev-notes references below).

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

- findings: `- F<n> [VERIFIED|PENDING|INVALIDATED|AUTO-ACCEPTED]
  <claim> — basis:
  <file:line / executed command / "unverified">`
- decisions: `- D<n> [PENDING|COMMITTED|INVALIDATED|AUTO-ACCEPTED]
  <decision> — basis: <…>`
- attack outcomes: `- A<n> [DISPATCHED|BIT|ZERO-DELTA] <summary> —
  basis: <brief at dispatch; report ref on return>`
- tags and header Status values are BARE enum values; annotations
  live in the line body after the bracket, never inside it (an
  annotated tag breaks the stats reader's enum admission and the
  closure gate's literal match)
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

Design against the recorded requirement. A decision COMMITS with a
basis that reaches its premise: where the premise is a data shape
or code path, the basis is an executed measurement or a hop-trace
that reaches the CONSUMING READ — a surface inventory stopping
short of where the value is read answers a narrower question, and
that last unmade hop is where two rounds bit (the attack's probe
obligation, applied at the commit moment). A deliberate skip is
tagged [AUTO-ACCEPTED], never a read dressed as ground. New evidence that kills a
premise appends an [INVALIDATED] line for the entry and for every
decision resting on it — re-derive the dependents; a premise and its
dependent contradicting inside one record is the escape shape.
Superseding cuts both ways: a new entry that contradicts an old one
appends the old id's [INVALIDATED] line (two live contradictory
entries route the implementer to whichever it reads first), and
invalidating an entry restates what survives of it in a live entry,
CLAUSE BY CLAUSE — each clause of the dead entry dispositioned
restated-at-<id> or dead; an entry-level summary is where the
load-bearing clause drops silently (a dropped pin clause cost a
round). A partial invalidation orphans the surviving clauses, and
later readers inherit the dead rule or nothing.

## Stop rule: [READY] = dispatchable (forcing point 3)

The design is done when a decision-complete brief could be written
from it — the dispatch skill §1 definition is the test, not a
feeling. If writing the impl briefs would require deciding anything,
the design is not done: design until it could be briefed. [READY] is
recordable only when the record sweeps clean: no entry's latest line
is [PENDING] (an assumption deliberately carried unverified is
re-tagged [AUTO-ACCEPTED], never left [PENDING]), no id appears
as two live entries (duplicates are found by body-read, not tag
grammar), and no live entry rests on an invalidated entry's content
— the dead-basis read is a body-read; where the repo carries a
mechanized check for it, that check runs first and its residue is
the judgment slice. An open [PENDING] under a claimed [READY] is
the premature-call shape.
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
tracker PINNED at the locked design's commit (a `git show
<sha>:<path>` copy, never a working-tree path — a live tree serves
HEAD), the question, and the read-only tail (dispatch skill
`references/forms.md`); the desk appends nothing to the record
while any attacker is live — an append landing mid-round leaks
sibling findings into an attacker's own record sweep, and the
round's independence cannot be re-established afterward. The
freeze's scope is every surface the brief claims immutable: a
brief asserting the tree matches the lock commit freezes the whole
repo, not only the record — the claim sets the scope, and keeping
it true until the last attacker returns is desk work. The
question APPENDS this block verbatim
(pasted, never recalled — free-composed briefs drop invariant
clauses):

    Every severity, closure, or HOLD verdict rests on evidence
    whose question matches the verdict's reach: an executed probe
    where the object exists to execute, a full source-chain trace
    (every hop cited) where it is still design prose; a closure
    names what the guarded input meets on the NEW path. Evidence
    answering a narrower question than the verdict it closes is
    the false-clean shape. A verdict without reach-matched
    evidence is labeled unmeasured and leaves its question open.
    Judgment findings (design-intent, record hygiene) need no
    probe. Attack both the design's fit to the recorded
    requirement and the factual bases it cites.

The brief never carries the desk's reasoning — it transmits the
producer's blind spots. Attack tier: probed opus (the PLAN.md
probe-then-certify step, certified; provenance in dev-notes) —
escalate a round to fable only on operator call. Rounds are
sequential —
one attacker, the round's A-line recorded before any next dispatch
(parallel attackers are operator experiments outside this default);
each re-attack is a NEW fresh context (a resumed attacker inherits
its own prior findings' frame), and a re-derived design is a NEW
locked design — it gets the attack again. Each round records an
A-line (The record): [ZERO-DELTA] only when every verdict is
reach-matched and nothing bit — that closes design. Iterate only if
design SUBSTANCE bites. At a round's return every finding is
classified, with basis: DESIGN-SUBSTANCE (wrong mechanism, money
path, silent failure in the shipped system) or RECORD/INSTRUMENT
(the run's own bookkeeping). Any substance finding: the round
records [BIT], findings appended as F-lines — that record change
IS the reopen. A record-only return: append the findings with
their class, execute the record repairs now (desk work), then
record [ZERO-DELTA] as the last A-line — record findings never
sustain a next round (declining max-severity is convergence;
observed sustaining rounds past it).
A reopen bars the design's UNITS only: investigation, record
repair, and the run's own instruments stay open desk work — the
closure gate reads the A-track, never the desk's toolbox.
The desk refutes a finding only with its own reach-matched evidence
(the F-line goes [INVALIDATED]); closure still needs the next
round's [ZERO-DELTA].

## Implementation (forcing point 4)

Implementation makes no design decisions. Units come from the locked
design; each dispatches on a decision-complete brief (dispatch skill
§1, tail per §2) citing the executor skill AND the run's live
closure: the tracker's last A-line is `[ZERO-DELTA]` with no F or D
line appended after it — append-only makes this computable, and a
re-lock's new entries void a stale closure (The attack). A missing decision,
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
`clippy.config/models` (`verify:` class) when present, else the
parent model. Append
`[PASSED]` or `[ISSUES FOUND]` with the evidence and set the header
Status to match (PASSED, or FAILED on an abandoned run; after
[ISSUES FOUND] it stays in-progress); issues
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

# Brief and report forms — what statiker's dispatches assume

On a stack without the dispatch skill (`dispatch-guards:dispatch`),
this file is the binding source of the forms the Composition section
cites. FOUR forcing points depend on them — forcing point 2's test of
what "dispatchable" means, the briefs forcing points 3 and 4 dispatch,
and forcing point 5's verify brief, which takes the read-only tail —
and nothing checks a brief against a form that is not there, so their
absence is silent. On a stack that carries the skill,
that skill wins and this file stays unloaded.

Distilled from that skill's §1 and §2. The channel and harness
material is deliberately absent: it describes a tool this stack does
not have. What survives is the portable half.

## Decision-complete — the test forcing point 2 resolves to

A brief is decision-complete only when a fresh context could execute
it WITHOUT MAKING ANY DESIGN OR PLACEMENT DECISION. Placement is
itself a decision — which rules apply, where the work belongs — so it
is pre-filled, not derived by the executor.

That is the whole of the [READY] test. "The design is done when a
decision-complete brief could be written from it" means exactly this
sentence and not a feeling of readiness: if writing the brief would
require deciding anything, the design is not done.

## The brief's mandatory parts (execution dispatches)

- **Assignments are the dispatcher's.** Ids, slugs, file names,
  numbering, target paths — named in the brief. The executor invents
  no naming and no placement.
- **Files to read, listed — never paraphrased.** Bind the source
  files. A paraphrase carried in the brief drifts and the executor
  cannot detect it. A position-dependent identifier (a line number, a
  register index) travels with a CONTENT anchor beside it: numbers
  shift when an artifact is regenerated while the brief's copy stands.
- **Grounding basis as its own section.** What must be read before
  building, and a requirement that the report cite what was actually
  read.
- **Every line asserting the target's CURRENT STATE carries a
  provenance grade**, and the grade follows the CLAIM, never the
  section or the form holding it. Either the line was opened at
  brief-write time, or it travels as "from <source>, unverified".
  Opening a REFERENCE is not opening its CONTENT — proving a path or
  id resolves establishes nothing the brief rests on. The hard half is
  FORM: a repo-assertion wearing a citation draws the grade, while the
  same assertion as a design sentence or a filled slot reads as the
  dispatcher's own decision and draws nothing — and decisions are
  executed, not checked. An EXPECTED RESULT is the costliest line to
  get wrong: the executor bends its work to satisfy it, so an
  unverified expectation is either silently forced to fit or returned
  as a gap at the price of a round trip.
- **Write boundaries.** Which paths the executor owns. One writer per
  working copy; parallel lanes need disjoint, brief-named path sets.
  Disjointness is per FILE — staging is file-granular, so a lane
  committing its own work in a shared file sweeps up a co-writer's
  uncommitted hunks. For a shared FILE no safe form exists, which
  makes serialization the remedy rather than the preference.

## The two briefs that are NOT this form

- **The attack (forcing point 3) and any verifier leg get the ARTIFACT
  AND THE QUESTION ONLY** — never the dispatcher's reasoning. The rich
  form above is for EXECUTION dispatches; applying it to an attack or
  a verify leg contaminates the independence that is its entire point.
  A fresh context briefed with conduct-of-building material is being
  framed as a builder.
- **Discovery dispatches** (lookups, sweeps, extraction — no writes)
  name the N facts to return and the pointers to trust unverified. No
  report files: each extra output medium re-writes the answer, and the
  observed cost driver is output volume, not finding quality.

## The read-only tail

An attack lane's brief carries, at the HEAD of its block and not the
tail: the lane writes NOTHING in the repo under attack — its probe
scratch belongs in its own scratch directory — and it reports findings
as text rather than as files.

A binding clause at the end of an invariant block reads as transport
plumbing; the very property that should make a pasted tail a
guarantee, being identical every time, is what makes it skimmed. Open
the block with it, and name its consequence.

The page CARVES OUT of that absolute, and a tail composed from this
file alone would be contradicted by the page it serves: a lane whose
probes must execute the repo's own checks carries that carve-out —
single-design attack rounds and the verify brief both do. The
carve-out is stated in the brief AFTER the pasted tail and GOVERNS ON
CONFLICT. Paste the tail, then the carve-out; the later text wins.

## The report form

Empty is valid; ABSENT is not. A dispatch without its closing report
is not done. A project defining its own report form uses that one —
this is the default for projects without one, never a second form
filled in parallel.

Every slot appears; "none" is an answer, silence is not:

  (a) items completed, with per-item evidence (file:line, test name)
  (b) checks actually RUN with their real output — FULL counts, skips
      included. A skip satisfies "real output" word for word and
      proves nothing, so every skip is dispositioned: which check, why
      it skipped, whether that reason touches the item. A skip in a
      check THIS lane built is a finding by construction — it says the
      built branch never executed.
  (c) open points and gaps, including anything needing a tier above
      the executor's: returned as a question with its evidence, never
      settled at its own tier
  (d) deviations from the brief, each with its reason
  (e) findings worth turning into a rule or test
  (f) files touched and commit hashes, established from the RECORD
      rather than from memory
  (g) what was NOT verified — the honest residue
  (h) sources actually read, of those the brief named

**Every report line asserting the state of something OUTSIDE the
executor's own work — a file it did not write, a mechanism, another
repo, a tool's behaviour — is either OPENED with the read named, or
carried as "inferred, unverified".** Slots (a), (b) and (f) carry
their evidence by construction, so (c), (d), (e) and (g) are where an
inference passes for an observation. A RECOMMENDATION resting on an
unopened claim takes the grade too — it is what the dispatcher acts
on. Form compliance is what hides an ungraded inference: (c) asks for
gaps and nothing more, so one shaped like an observation fills it
correctly and rides out among claims that all hold. A line carrying
neither a named read nor a grade is an incomplete report, demanded
back like a missing slot.

## Halting

On a gap, the executor halts THE ITEM, finishes the remainder, and
reports — never halts itself waiting for an answer. A lane that stops
and waits cannot be reached; stopping it and re-dispatching with its
interim groundwork carried costs less than any wait.

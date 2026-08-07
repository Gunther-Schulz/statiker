---
name: statiker
description: Conducts a development task from investigation through verified implementation — a free design loop held by five forcing points (recorded decisions with bases, dispatchable-design stop rule, a fresh-context attack on each locked design, no-design implementation, isolated executed verify). Trial-stage successor to clippy; use only when the operator explicitly invokes statiker or requests a statiker run.
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
ADOPTED — content re-entering from outside the record's live
entries: a prior or superseded run's tracker, session memory of
work no live entry records, or a clause restated out of an
invalidated entry (citing a LIVE entry as basis is not adoption)
— is recorded [PENDING] under this run's own next id at adoption.
That SAME id carries the resolution once a current-check scoped
to the claim runs (re-read the cited lines; staleness-check
against commits since the basis read — an earlier item's own
implementation invalidates reads of the files it touched): pass →
the entry class's live tag, citing source AND check; fail →
[INVALIDATED] with the failure as basis. Unrecorded memory of
prior work is never a basis.

Header: `# Run: <title>`; `Status:` from
{in-progress, [READY], PASSED, FAILED, COMPLETE}; `Phase:` from
{investigate-design, implement, verify}; `Skill: statiker
<version>` (version read from the Skill injection's
base-directory line — the plugin cache path carries it); optional
`Mode: auto` (Stop rule) — Status and Phase within the first ~20
lines (the stats reader's admission window). After the header,
the requirement head in two
grades, declared apart: INTENT — the operator's request VERBATIM —
and the derived requirements, as long as it needs to be; verify
reads this head plus its R-lines, not the conversation. A derived
requirement is inherited text (a backlog item, a prior session's
plan, intake derivation), not operator ground: when the run's own
investigation contradicts its letter, the desk amends it by
R-line — `- R<n> [AMENDED] <new letter> — basis: <…>`, an
ordinary entry the attack grades like any decision. A
contradiction reaching the INTENT is a reconciliation for the
operator: evidence and recommendation surfaced when found, the
recorded recommendation advancing an unattended run (the [READY]
prompt's pattern); one advanced unattended stays OPEN —
re-surfaced at each operator prompt and at the run's close —
until the operator answers. The record's one mutable surface is
the header's Status and Phase fields, updated at each transition
and at the verify verdict; everything below them is append-only.
Status writes its enum member verbatim — [READY] keeps its
brackets (the stats reader admits only the bracketed form).

Entries are one line each, status tag first, appended never
rewritten (the templates below wrap only on this page). A status
change is a NEW tag-first line for the same id
(`- D<n> [INVALIDATED] <why> — basis: <…>`) — never an edit of the
old line; the stats reader counts only tag-first lines.

- findings: `- F<n> [VERIFIED|PENDING|INVALIDATED|AUTO-ACCEPTED]
  <claim> — basis:
  <file:line / executed command / entry id / "unverified">`
- decisions: `- D<n> [PENDING|COMMITTED|INVALIDATED|AUTO-ACCEPTED]
  <decision> — basis: <…>`
- requirement amendments: `- R<n>
  [AMENDED|PENDING|INVALIDATED|AUTO-ACCEPTED] <new letter> —
  basis: <…>` (derived requirements only; the head above)
- attack outcomes: `- A<n> [DISPATCHED|BIT|ZERO-DELTA] <summary> —
  basis: <brief at dispatch; report ref on return>`
- verify verdicts: `- V<n> [PASSED|ISSUES FOUND] <summary> —
  basis: <the checks' own output>`
- entry tags are BARE enum values; annotations
  live in the line body after the bracket, never inside it, and a
  bracketed tag literal never appears inside a body — the stats
  reader counts some tags unanchored, and an annotated tag breaks
  its literal greps and the closure gate's match
- a decision still resting on an unverified assumption at [READY]
  gets an appended `[AUTO-ACCEPTED]` line — surfaced to the operator
  by its tag, never silently carried; a reconciliation advanced on
  its recommendation is recorded this way, conflict and
  recommendation in the line body — the operator's answer appends
  the resolving line.

Each investigation/design round appends under a `## Cycle <n>`
heading. The heading counts motion for the shared stats reader; it
is not a schedule — a round is whatever investigation the design
needed.

## The loop

The desk (this session; intended consumer is a top-tier session
model — prescription density is calibrated to it) orchestrates,
forms and records decisions, writes briefs, grades.
Investigation and discovery legs go to cheaper-tier subagents on
pointed decision-complete briefs —
brief-writing is where hunt-judgment lives (Fire-born clauses,
below); what a leg returns is evidence, recorded with its basis.
A leg is recorded [PENDING] at dispatch and resolved only by a
body-read of its return — a stopped or past-horizon leg's output
included: a late report is evidence, not noise, and "it never
returned" is a transcript claim checked in the transcript (a round
was staged over a design whose refutation sat in two unread
returns). The [READY] sweep's no-[PENDING] gate holds unread legs
open mechanically. An unreturnable leg — stopped per
the harness's task state or BY the desk at its horizon
(dispatch skill §4: inspect or stop, never more waiting),
with NO return to read (the transcript check above, never
memory) or still [PENDING] after its return's body-read (a
read that resolves takes the evidence's tag, the ordinary
rule above) — gets ONE new [AUTO-ACCEPTED]
tag-first line as a deliberate carry
with the
loss stated — the sweep and the closing [ZERO-DELTA]'s
no-[PENDING] condition both read that as resolved.
Consecutive discovery sweeps in the main session are the tell that a
leg should have been dispatched.

Design against the recorded requirement. A decision COMMITS with a
basis that reaches its premise: where the premise is a data shape
or code path, the basis is an executed measurement or a hop-trace
that reaches the CONSUMING READ — a surface inventory stopping
short of where the value is read answers a narrower question, and
that last unmade hop is where two rounds bit (the attack's probe
obligation, applied at the commit moment). A deliberate skip is
tagged [AUTO-ACCEPTED], never a read dressed as ground. New
evidence that kills a premise appends an [INVALIDATED] line for
the entry and for every
decision resting on it — re-derive the dependents; a premise and its
dependent contradicting inside one record is the escape shape.
Superseding cuts both ways: a new entry that contradicts an old one
appends the old id's [INVALIDATED] line (two live contradictory
entries route the implementer to whichever it reads first), and
invalidating an entry restates what survives of it in a live entry,
CLAUSE BY CLAUSE — each clause of the dead entry dispositioned
restated-at-<id> or dead; an entry-level summary is where the
load-bearing clause drops silently (a dropped pin clause cost a
round). A restated clause takes The record's full adoption path
(The record: [PENDING] under a new id, cleared under that same
id) — the [READY] sweep holds unchecked restatements open
mechanically; unchecked ones have carried dead citations,
unresolvable paths, and a killed anchoring premise forward. A
dead disposition is written `dead (<what kills it>)`, and the
sweep's dead-basis body-read holds a killer-less dead clause open
as [PENDING]. A partial invalidation orphans the surviving
clauses, and later readers inherit the dead rule or nothing.

## Stop rule: [READY] = dispatchable (forcing point 2)

The design is done when a decision-complete brief could be written
from it — the dispatch skill §1 definition is the test, not a
feeling. If writing the impl briefs would require deciding anything,
the design is not done: design until it could be briefed. [READY] is
recordable only when the record sweeps clean: no entry's latest line
is [PENDING] (an assumption deliberately carried unverified
gets its [AUTO-ACCEPTED] line, never left [PENDING]), no id appears
as two live entries (duplicates are found by body-read, not tag
grammar), and no live entry rests on an invalidated entry's
content — the dead-basis read is a body-read covering the
invalidation lines themselves: a missing clause list, or a dead
clause without its named killer, holds the record from [READY];
where the repo carries a mechanized check for it, that check runs
first and its residue is the judgment slice. An open [PENDING]
under a claimed [READY] is
the premature-call shape.
Record `Status: [READY]` with the impl units enumerated, each
naming its red-first pin — and a pin DISCRIMINATES: red on the
current state, green only through the fix; a criterion the
defective state already satisfies verifies nothing, and a
renumbering that drops a unit's pin clause is a silent unpin (both
observed as a round's highest finding). A unit's edit commission is
symbol-anchored — the target named by symbol, with a residue check
proving it gone or changed — never a bare line range (line numbers
may cite, never command): ranges decay
as file and record evolve, and one commissioned range landed
exactly on the guards a prior decision retained, deletable verbatim
by a literalist implementer. With an
operator present, present the record and recommendation at [READY],
ENDING with one advance prompt — "(y) advances per the
recommendation"; anything else is free-form override. Design
decisions are never posed as choices; the prompt carries loop
control only. Unattended, the recorded recommendation advances the
run. `Mode: auto` in the header (operator-declared at run start,
fixed for the run) forces the unattended branch throughout: no
prompts, every
recommendation advances on record, reconciliations surface only
in the close. Advancing locks the design: commit the
TRACKER by pathspec commit (`git commit -- <paths>` — a
pre-staged index rides into a plain commit; a pathspec
commit takes WORKING-TREE content, so excluding a path
means dropping it from the pathspec, never merely skipping
its add), never `-A`. Every commit this skill makes — the
lock, Implementation's units, a readback repair — halts on
an in-progress merge, cherry-pick, revert, or rebase (their
state refs: `git rev-parse -q --verify MERGE_HEAD` and
kin): a pathspec commit is fatal mid-operation, `-A` stays
forbidden, and the half-finished operation is the
operator's — hold, surface when present; unattended a
blocked unit rides the close's deviations, a blocked LOCK
closes the run FAILED (no lock, nothing to build on). The
design phase edits no other repo file, so the tracker is
normally the whole pathspec; anything else enters ONLY
named by a lock-set line appended before the lock
(`- F<n> [VERIFIED] lock-set: <path> — basis: <the entry
that produced it>`), and a lock-set path — a unit write-set
path too (Implementation) — names a FILE, never a
directory: a directory pathspec commits whatever else the
operator touched under it. The pathspec IS the tracker plus
every LIVE lock-set path (a re-lock inherits prior locks'
live lock-set lines; an unchanged inherited path is a
pathspec no-op), composed in this order with the index
untouched until step two: (1) an UNTRACKED path
`git check-ignore` names ignored drops (it stays out, never
a `-f`; a tracked path commits regardless of ignore
patterns), the drop appended BEFORE the commit — so the
pinned tracker carries it — as the lock-set line's own
[INVALIDATED] line, its one clause dead with the refusal
named killer (the loop's supersede form; "contradicted"
below means exactly this). The TRACKER is not droppable: an
untracked tracker check-ignore names ignored, or any
composition leaving the pathspec empty, HALTS the lock
uncommitted (an empty-pathspec `git commit -m … --` commits
the ENTIRE INDEX) — the run cannot pin its record in this
repo; surfaced when present, FAILED unattended. (2) The
surviving untracked paths (the fresh tracker, a new
artifact) are `git add`ed exactly and alone — a pathspec
commit reaches an untracked path only through its add; a
TRACKED path gets no add at all — the pathspec already
takes its working-tree content, and an add would silently
re-stage over anything the operator had staged there. Desk
scratch belongs in the desk's own scratchpad, never the repo
(the attacker rule's counterpart, Verify). Operator state —
everything else, including anything pre-staged (`git status`
before the lock) — is untouched: never committed, never
unstaged. An operator modification INSIDE a lock-set path
is a COLLISION; its instrument is a lock-time re-read of
each lock-set artifact against the entry that produced it —
`git status` cannot separate the authors here, every
lock-set path is expectedly modified — so the duty is
scoped to what that re-read surfaces (a divergence it
misses rides into the commit; the attack round's probes are
the backstop — the residue named, not hidden). A discovered
collision is recorded as a [VERIFIED] F-line before the
lock commit (basis the read that surfaced it; the pinned
tracker carries the line), the path dropped from the
pathspec and its lock-set line contradicted like the
ignored case, surfaced when the operator is present, riding
the close's deviations unattended. Read the commit back
(`git show --stat`): every stat path sits inside the
expected set — the tracker plus the live lock-set paths
MINUS the dropped ones — and `git status` over that same
set reports CLEAN after the commit. An unchanged inherited
path is legitimately absent from the stat (`--stat` lists
only what changed); status residue is the coverage failure,
fixed by a further pathspec commit over exactly the residue
plus the tracker — the readback-clean commit's sha is the
one pinned. A stat path OUTSIDE the set is a mis-composed
pathspec: its content is already in history — recorded as a
collision-class contradiction and named a brief exclusion,
never reverted out of the working tree (the revert would
destroy the very operator state the finding names). A brief
that asserts the tree claim (The
attack's freeze scope, named there) names any tracked surface
the claim cannot then cover as an
exclusion (the dropped and collision paths above are that
list's mechanical floor; an operator-modified tracked path
outside every lock-set path joins through this same rule) —
the attacker
reads an excluded path as outside
the frozen surface, evidence of nothing; a brief that never
asserts it needs no exclusions. This is the LOCK COMMIT; its
sha is what the attack brief pins, and the locked design IS
the record at that commit. A
re-derived design re-enters here: new [READY], new sweep, new
lock commit.

## The attack (forcing point 3)

A fresh-context attack on each locked design by a context that did
not produce it, before implementation. The attack brief carries the
tracker PINNED at the locked design's commit (a `git show
<sha>:<path>` copy, never a working-tree path — a live tree serves
HEAD), the question, and the read-only tail (dispatch skill
`references/forms.md`). The artifact drops two computable
species, the filter's form stated in the brief: contiguous
quoted blocks whose first line is `> Superseded — <label>` (their
production: the return processing below), plus sections headed
`## Superseded —` — legacy landings from earlier skill versions,
possible in resumed trackers only; ENTRIES are never
filtered (dead bodies are load-bearing for closure questions, and
a hand-summary is the paraphrase-drift class). Unfiltered, the
artifact compounds per round; the desk appends nothing to the record
while any attacker is live — an append landing mid-round leaks
sibling findings into an attacker's own record sweep, and the
round's independence cannot be re-established afterward. The
freeze defers appends, never work: desk findings and leg
dispatches during a round queue at
`~/.claude/statiker-seals/<repo-basename>/<tracker-filename>.A<n>.queue`
(repo basename = `basename` of `git rev-parse --show-toplevel`,
then the tracker's filename verbatim with `.md`) — existing
whether or not a seal was
written — and append at the round's return, before its A-line. The
freeze's scope is every surface the brief claims immutable: a
brief asserting the tree matches the lock commit (the TREE
CLAIM) freezes the whole
repo, not only the record — the claim sets the scope, and keeping
it true until the last attacker returns is desk work. The claim
binds TRACKED state; untracked check by-products sit outside it
under the declared carve-out (Verify — declaration, pre-existence
record, removal at the return). The
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
producer's blind spots — and the rule reaches the ARTIFACT: an
entry authored for the attacker's eyes (a weak-spot list, steering
notes) is desk reasoning riding the never-filtered channel, and it
frames the round it was meant to sharpen. Pre-round self-assessment
is a sealed prediction, written before the round dispatches to
`~/.claude/statiker-seals/<repo-basename>/<tracker-filename>.A<n>.seal`
(repo basename, then the tracker's filename verbatim, `.md`
included) — a path any successor desk re-derives from the repo
it resumes in plus the tracker's filename; out of
the repo because attackers read the repo, and an in-repo seal
breaks any brief asserting tree == lock commit. At the round's
return the desk compares seal against bites and writes the
comparison BESIDE the seal, still out of the repo — later
attackers read the repo, so seals and comparisons enter the
tracker only in the close, where no further round follows. A
seal is calibration, never evidence: it steers no verdict, and a
missing or late one voids its comparison, not the round.
Attack tier: probed
opus (the PLAN.md
probe-then-certify step, certified; provenance in dev-notes) —
escalate a round to fable only on operator call. Rounds are
sequential —
one attacker, the round's A-line recorded before any next dispatch
(parallel attackers are operator experiments outside this default);
each re-attack is a NEW fresh context (a resumed attacker inherits
its own prior findings' frame), and a re-derived design is a NEW
locked design — it gets the attack again. Each round records an
A-line (The record). At a round's return every finding is
classified, with basis: DESIGN-SUBSTANCE (wrong mechanism, money
path, silent failure in the shipped system) or RECORD/INSTRUMENT
(the run's own bookkeeping); findings append as F-lines with the
tag their evidence earns — reach-matched in hand → [VERIFIED],
where a judgment finding's reach is the cited record or design
text itself, else [PENDING]. An UNMEASURED verdict is
an open question the desk completes itself — its own executed
measurement, recorded as the F-line's evidence — before the
round's A-line lands. Verbatim report quotes the desk retains
append as a quoted block whose first line is
`> Superseded — A<n> quotes` (the filter's species) — EVERY line
of the block begins `>`; a blank line is a BARE `>`, nothing
after it (trailing whitespace may not survive target-repo
hooks), and the block ends at the first line not beginning `>`.
Bracketed tag
literals in the pasted text are defanged (brackets dropped,
the names lowercased where they occur in the quoted text,
and listed comma-separated after a semicolon — the list
records what was defanged, the body no longer showing it —
composed first line
`> Superseded — A<n> quotes; <lowercase names>`, the
semicolon and list absent when no literal occurs; the filter
matches the label's opening form) so the defanged
forms differ from every counted tag literal in both brackets
and case; the stats reader's literal greps carry the
brackets (verified against its source), so a bare name in
either case matches nothing — the brackets are the
load-bearing half, the case change margin. Regraded
into F-lines in the same sitting. Any substance finding: the
round records [BIT] — that record change IS the reopen. A
substance-free
return: execute the record repairs now (desk work), then record
[ZERO-DELTA] as the last A-line — recordable only with every
verdict reach-matched, measured by the attacker or completed by
the desk, and no [PENDING] tag riding the round's own appends.
That closes design; record findings never sustain a
next round (declining max-severity is convergence; observed
sustaining rounds past it).
A reopen bars the design's UNITS only: investigation, record
repair, and the run's own instruments stay open desk work — their
lines land before the closing A-line (this return's
repair-then-close order), so the post-closure predicate
(Implementation) never reads them; a desk repair arising
mid-implementation is written with body opening `record:`
(Implementation's bookkeeping scope) — unless it kills an
entry LIVE at the closure (latest line not [INVALIDATED] when
the closing A-line landed): that takes the scopeless
[INVALIDATED] route, voids, and carries the premise-killing
consequence (Implementation: stop the siblings resting on it,
let the rest land, re-enter ONCE).
The desk refutes a finding only with its own reach-matched evidence
(the F-line goes [INVALIDATED]); closure still needs the next
round's [ZERO-DELTA].

## Implementation (forcing point 4)

Implementation makes no design decisions; at the closing
[ZERO-DELTA], Phase flips to implement and Status returns to
in-progress. Units come from the locked
design; each dispatches on a decision-complete brief (dispatch
skill §1, tail per §2) citing the executor skill AND the run's
live closure. The closure read is DESK work, performed at each
dispatch — the brief carries its verdict (the closing A-line
quoted, the lock sha, plus any post-closure lines scoped to the
unit being dispatched), never the raw criterion. The criterion,
one predicate: unit U<k> may dispatch when the tracker's last
A-line is `[ZERO-DELTA]` and no F, D, or R line appended after
that A-line (post-closure) is SCOPELESS — a scopeless line
voids the whole closure
(and a re-lock's new entries void a stale closure, The attack);
a line whose body OPENS `unit U<k>` voids nothing — it RE-OPENS
that unit's dispatch and travels in the re-dispatch brief as the
amendment it consumes (live lines only: an id whose latest
line is [INVALIDATED] travels as nothing). A line whose body
OPENS `record:` is
desk bookkeeping — it voids nothing and re-opens nothing, and
it never invalidates an entry live at the closure (the
definition: The attack's reopen rule): that takes the
scopeless [INVALIDATED] route below. A clause restatement it
obliges (The loop) takes the scope of what the clause IS:
bookkeeping opens `record:`; a clause a unit consumes opens
`unit U<k>` and re-opens that unit — its current-check (The
record's adoption path) runs before the re-dispatch brief
consumes it, never inside the unit: pass → the passing line
opens `unit U<k>` (the criterion's scope) and the amendment
travels; fail → [INVALIDATED] under its own id, opening `unit
U<k>` like the [PENDING] restatement line it resolves, the
parent's clause disposition re-written by a new
[INVALIDATED] line under the parent's id, body opening
`record:` (bookkeeping over an already-dead entry — the
closure rests on no clause of an invalidated body) — dead
(<the check's failure>) — so no clause list points at a dead
restatement, the re-dispatch proceeding without it
and the unit's want surfacing as its gap; one bearing wider
on the design is SCOPELESS and voids — the premise-killing
consequence (stop the siblings resting on it, let the rest
land, re-enter ONCE). Units with disjoint
write-sets run parallel (one shared index — commits
serialize; the contention-retry rule rides in every unit
brief, below). A missing
decision, file, or value is reported as a gap, never bridged —
and triaged on arrival: a unit-local gap decision is a design
decision made without an attack round, and it is recorded as
exactly that — `- D<n> [AUTO-ACCEPTED] unit U<k> gap: <decision>
— basis: <gap report>` — surfaced by its tag, enumerated in the
close, graded only through the WORK verify checks against the
requirement head (no entry-level grading exists); no attack
round reads it on the normal run shape — a coverage fact, not a
bar: a re-entry round reads the full record — so the tag
surface and the close enumeration are the backstops. That
unit re-dispatches on the amended record, siblings run on. A
gap that kills a locked premise is recorded as the killed
entry's SCOPELESS [INVALIDATED] line (The loop) — the body
never opens `unit U<k>` or `record:` — voiding the closure
through the predicate above; that invalidation IS the triage
discriminator: no entry live at the closure dies → unit-local,
one dies → premise-killing. Stop the siblings resting
on it, let the rest land, re-enter the loop ONCE with every
return in hand. Model per
`clippy.config/models` (`impl:` class) when present, else the
operator corpus routing table; an unreadable models file halts
the dispatch, the parse error a unit-scoped F-line (body OPENS
`unit U<k>` — the criterion's scope form). Each unit
commits green; the desk appends its landing as an INDENTED
annotation line (`  unit U<k> landed: <sha>`, preceded by a
blank line — markdown otherwise folds it into the entry above) —
not an entry, so
invisible to the stats reader's tag-first count and the closure
read by construction — that is what makes resume reliable.
Unit briefs carry the lock's commit form AND its collision
rule — detector, retry, and exits stated: pathspec commit
over the write-set (the lock's composition — add only paths
new to git, working-tree content, the merge-state halt);
an `index.lock` failure on add or commit is CONTENTION with
a sibling's commit — retried until the commit lands, never
a collision or a failure, and the brief SAYS so: desk prose
reaches no unit, and a unit not told to retry returns with
its edits uncommitted, poisoning its own write-set for the
re-dispatch. The unit runs
`git status` over its write-set at START, before any edit —
ANY output is a collision: a modified tracked path, or an
untracked file already sitting on a write-set path (the
unit would otherwise overwrite an operator draft and commit
the overwrite) — the unit reports it and
HALTS UNBUILT (no commit, no landing annotation); a clean
start makes every later modification the unit's own, the
pathspec the full write-set. A unit whose commissioned
change turns out already present has a third exit: report
it, the residue check proving the target state, the empty
commit's exit 1 expected — the landing annotation then
carries `already-present` in place of a sha. The desk books
a collision as a [VERIFIED] F-line opening `record:` (basis
the unit's reported check; a collision decides nothing —
voids nothing, re-opens nothing), never through the gap
triage, and holds the unit — clearing the path is DESK
work, decided by provenance: where the record and the task
system show the dirt is the run's own — a stopped or dead
sibling whose write-set covers the path, its clean START
check readable in that sibling's output — the desk restores
exactly those paths to HEAD, index and working tree both
(`git restore --source=HEAD --staged --worktree -- <paths>`
— a dead unit may have staged), and re-dispatches; a path
without that provenance is operator state — held, surfaced
when the operator is present, riding the close's deviations
unattended.

## Verify (forcing point 5)

Executed, isolated, against the recorded requirement; Phase flips
to verify at dispatch — a dispatch made only with no entry's
latest line [PENDING] (the [READY] sweep's no-[PENDING] condition,
re-read at this seam). A fresh
context that did not build the work runs the real checks — tests,
probes, renders, at the altitude where the work takes effect —
against the tracker's requirement head as amended by its R-lines,
and pastes the checks' own
output; a launcher's exit status is not a verdict. The verify brief
carries the tracker, the code, and the question — read-only tail,
no executor cite, one named carve-out stated in the brief AFTER
the pasted tail and governing on conflict: executing the repo's
checks writes their normal by-products (caches, build dirs) —
still no commits, no tracker writes. The carve-out DECLARES the
repo checks' by-product paths, and the declaration with each
path's pre-existence (present or absent) is observed AND
written at dispatch, before the round runs, to the seal
namespace —
`~/.claude/statiker-seals/<repo-basename>/<tracker-filename>.<round>.paths`
(`<round>` = the A<n> id for attack rounds; a verify leg
writes `.verify.paths`, REWRITTEN at each verify dispatch —
at most one is in flight, so no count is derived),
re-derivable by any successor desk (The attack's derivation)
— never carried only in the brief or in memory. At the
return, after any queued appends (attack
rounds, The attack) and record repairs land and before the
outcome line, the desk removes exactly the declared paths the
`.paths` record lists ABSENT that now exist; everything else —
pre-existing (operator state), undeclared, or uncertain — is
LEFT, the leftover a finding, never a broader clean. Removal
consumes the file — delete it once removal has run; a `.paths`
file with no live round is litter. Attack briefs
carry the same carve-out for the repo checks their probes
execute; an attacker's own probe scratch belongs in its
scratchpad (the read-only tail's provision), never the repo. Model per
`clippy.config/models` (`verify:` class) when present, else the
parent model; an unreadable models file halts the dispatch, the
parse error recorded as a finding. Append the V-line (The record)
with the evidence and set the header
Status to match (PASSED, or FAILED on an abandoned run; after
[ISSUES FOUND] it stays in-progress); issues
return the run to the loop as findings. In auto mode the third
[ISSUES FOUND] forces the close with Status FAILED
(the stays-in-progress rule's one exception) — an unattended run
earns no infinite loop.

## Close

At the verdict that ends the run ([PASSED], or FAILED per
Verify, per the Stop rule's blocked-lock halt, or operator
call), append `## Close` and present it to the
operator —
in auto mode this is the run's one touchpoint: the verdict with
its evidence pointer; every open reconciliation; every R-line
amendment (what shipped vs. the letter as asked); every
[AUTO-ACCEPTED] entry; every entry whose latest line is
[PENDING] (a FAILED or abandoned run can carry them);
deviations and gaps; what was NOT verified; candidate
lessons. Landed seals and their comparisons
enter here (The attack). Status flips to COMPLETE when the close
is appended — over a PASSED verdict ONLY: a run ending FAILED
takes the same close and KEEPS FAILED, so a FAILED run's close
is marked by its `## Close` heading, never the header.
Delivering the close is then the desk's final act, so the
delivered artifact carries its final Status. Open
reconciliations survive
into COMPLETE, enumerated in the close; an operator answer
arriving later appends its resolving line to the closed tracker —
append-only has no expiry, and the close's enumeration is what
makes the late landing findable.

## Fire-born clauses (none at birth)

No lens list, no lens pass. When a real blind spot fires in
operation, mint it as a pointed hunt clause inside the section it
serves (usually The loop's brief-writing) — one incident as
provenance, amendment over addition; log the mint and each
subsequent firing in the source repo's dev-notes/OBSERVATIONS.md —
a desk in a target repo without a local checkout at hand rides
the observation on its run report instead. A clause with no
firing since the last review is a cut candidate.

## Birth-class declaration

At birth this file was enforcement structure + bindings only —
zero capability patches. ~150 operational lines is the
stabilization TARGET, not the live count: the trial accretes
fire-born structure above it deliberately, and the compression
pass owed at stabilization (booked in dev-notes) brings it back
down. A patch landed without provenance is still the tripwire.

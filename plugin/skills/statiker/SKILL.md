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

## The tools

Two shipped state machines live under this skill's base directory
(the Skill injection's base-directory line names it; invoke with
python3): `scripts/statiker_git.py` — git transactions: the
run-start preflight, the LOCK commit, unit START and COMMIT — and
`scripts/statiker_record.py` — record grammar: tracker lint, the
[READY] sweep's computable slice, the closure predicate, the
pinned attack artifact, defanged quote blocks. They enforce what
prose could not hold across attack rounds: the git tool the state
DIRECTORIES gate (a ref read false-halts after a continued rebase
and passes break/exec/reword stops), porcelain column semantics,
file-only pathspec composition, add-untracked-only, `-m` commits,
two-half readback, capped spaced index.lock retry; the record
tool the enum-tag grammar, the unanchored stats-reader greps
behind the defang rule, and scope-opener classification. Path
contract, both tools: a path is taken AS NAMED, never resolved
through symlinks (a resolved link substituted the brief's
write-set inside a booked verdict), and git byte output decodes
the way the OS decodes argv (two spellings of one byte deadlocked
the drop handshake); the record tool anchors its repo at the
TRACKER's own directory, the git tool at its invocation cwd —
briefs invoke it from the repo root, which the invocation lines
already do. Every
invocation — usage errors included (USAGE_ERROR); `--help` alone
excepted, argparse answers it verdict-free — ends in
exactly one final
`STATIKER-GIT VERDICT: {json}` or `STATIKER-RECORD VERDICT:
{json}` line, evidence lines before it — the desk books THAT
LINE verbatim as the basis of
whatever entry the verdict obliges; an exit code is routing
convenience, never the result. Happy paths route in their own
sections; `lint` alone answers ad-hoc grammar questions
(LINT_CLEAN / LINT_VIOLATIONS; `sweep` includes it), and `quote`
and `filter` return QUOTE_BLOCK and ARTIFACT_WRITTEN with their
production counts. ANY verdict no section names is a halt for
the seam that ran it — booked as a `record:` F-line from the
verdict line, the seam's halt route applying (TRACKER_UNREADABLE,
PIN_UNREADABLE, NOT_A_REPO, PATH_OUTSIDE_REPO, USAGE_ERROR,
GIT_ERROR, INTERNAL_ERROR, and any future member). One override
on every route: a halt verdict carrying a `shas` or `sha` field
has LANDED commits — routed like HALT_RESIDUE_PERSISTS, never as
uncommitted. Unit briefs carry the git tool's
ABSOLUTE path and its invocation lines — the tool is the shared
implementation, so no lock-procedure text is ever expanded into a
brief. The record tool is DESK-only: it reads the record, so no
attack or verify brief ever cites it — those contexts'
independence is the point. Provenance and the red-first suites:
the source repo, tools/test_statiker_git.py and
tools/test_statiker_record.py (the attack rounds' probe battery
and record findings mechanized).

At run start, before any design work: `preflight
--tracker <path>`. PREFLIGHT_OK proceeds (it also reports any
in-progress operation, informational at this seam).
PREFLIGHT_UNPINNABLE_TRACKER means the repo
ignores the tracker path and can never pin this run's record —
surfaced to a present operator before further work; unattended
the run closes FAILED at minimal cost (Close, Status written
FAILED); any other preflight verdict surfaces the same way. The
`state-gate` subcommand (STATE_CLEAN / STATE_IN_PROGRESS) is the
re-entry instrument: an attended halt's clearing reply is
verified by it before the halted procedure re-runs.

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
`Mode: auto` (Stop rule); `Budget: cycles <n> / rounds <n> /
verify <n>` — the run's declared bound over every repeating seam,
defaults 7 / 4 / 3, declared at run start where a successor reads
it (an unattended loop without a declared bound terminates on
context death, the one ending that produces no readable verdict).
Exhaustion never continues silently: attended it forces the
operator prompt, unattended it closes the run FAILED with the
unexhausted question enumerated in the close. (hypothesis) —
Status and Phase within the first ~20
lines (the stats reader's admission window). After the header,
the requirement head in two
grades, declared apart: INTENT — the operator's request VERBATIM,
as PLAIN text: the record grammar reserves `>` lines for
Superseded blocks, so a blockquoted INTENT lints illegal, and the
one lint-legal quote form is exactly what the attack filter
drops — the operator's words would vanish from every attack
artifact (verbatim binds the words, not tag literals or layout: a
bracketed tag literal inside the operator's text is defanged
exactly as report quotes are, the mutation noted beside the
line — undefanged it
holds every later sweep, correctly, for the run's life) —
and the derived requirements, as long as it needs to be, numbered
`R<n>.` — never dash-led `- R<n>`, the record grammar's amendment
form; verify
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
until the operator answers. A mid-run operator instruction that
changes what the run is FOR appends as a new INTENT-grade line
under the head — not an R-line: R-lines are derived text,
operator words are not — and the desk states which live
decisions it kills (a killed one takes the scopeless
[INVALIDATED] route; the closure voids and the design
re-enters). Without this landing, the run verifies against a
requirement the operator has already superseded — conversation
is the one channel verify deliberately never reads.
(hypothesis) The record's one mutable surface is
the header's Status and Phase fields, updated at each transition
and at the verify verdict; everything below them is append-only.
Status writes its enum member verbatim — [READY] keeps its
brackets (the stats reader admits only the bracketed form).
Run `lint` once the header and head are written: a form defect
found here costs re-creating a one-screen file before anything
rests on it; found at the [READY] sweep it holds a full record
whose head the append-only rule cannot rewrite.

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
- attack outcomes: `- A<n> [DISPATCHED|BIT|ZERO-DELTA|VOID]
  <summary> —
  basis: <brief at dispatch; report ref on return>` (VOID: The
  attack — an aborted or premise-broken round)
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
A leg is dispatched TO A DECISION: its brief names the recorded
decision it unblocks and what each possible return would decide —
a leg whose returns cannot change any recorded decision or any
entry's tag is not dispatched (the corpus's discriminating-
evidence rule, priced at compose time where it costs a sentence,
not at review time where it costs a round). The same test closes
investigation: when no un-dispatched leg would move a decision,
the design is done investigating — [READY] then decides whether
it is done designing. (hypothesis)
An out-of-scope discovery — true, outside the requirement head:
an unrelated defect, an adjacent improvement, a region the run
decides not to carry — is recorded with its EXIT named in the
entry body: CARRIED (an R-amendment brings it into scope; the
design re-enters for it) or EXPORTED (a named carrier outside
the run — backlog entry, ledger line, issue — with the
reference). Fixing it inside a unit without one of those exits
is barred: the run's three certified surfaces are the attacked
design, the verified requirement, and the pinned record, and an
in-flight fix enters none of them. (hypothesis)

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
as [PENDING]. Clause dispositions AGGREGATE across an id's
[INVALIDATED] lines — a later line re-dispositions only the
clauses it names; every reader takes the union, latest line per
CLAUSE, never the id's last line alone. A partial invalidation
orphans the surviving
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
clause without its named killer, holds the record from [READY].
The record tool's `sweep --tracker <path>` runs FIRST at this
seam: SWEEP_CLEAN clears the mechanical half only;
SWEEP_HOLDS blocks [READY] on the computable slice
(latest-line [PENDING]s, killer-less dead dispositions, live
bases citing invalidated ids, grammar and defang lint), and its
verdict carries the clause-disposition union the dead-basis read
consumes; the residue the tool NAMES — dead-basis body-reads, the
duplicate-id body-read, restatement adoption checks — is the
judgment slice, still desk work. An open [PENDING]
under a claimed [READY] is
the premature-call shape.
Record `Status: [READY]` with the impl units enumerated, each
naming its red-first pin — and a pin DISCRIMINATES: red on the
current state, green only through the fix; a criterion the
defective state already satisfies verifies nothing, and a
renumbering that drops a unit's pin clause is a silent unpin (both
observed as a round's highest finding). Each unit is also
classified by the reversibility of its EFFECT, not its diff: one
whose green state includes something git cannot undo — a schema
or data migration, an external write, a publish/push/send, a
deletion outside the write-set — is tagged irreversible in its
enumeration. Every other bound in this skill limits waste; this
one limits damage: in auto mode an irreversible unit never
dispatches — it takes the hold entry (Implementation) and rides
the close for the operator; attended it dispatches after the
effect is named. (hypothesis) A unit's edit commission is
symbol-anchored — the target named by symbol, with a residue check
proving it gone or changed — never a bare line range (line numbers
may cite, never command): ranges decay
as file and record evolve, and one commissioned range landed
exactly on the guards a prior decision retained, deletable verbatim
by a literalist implementer. With an
operator present, present the record and recommendation at
[READY] — OPENING with the INTENT re-read: a design satisfying
its derived requirements but not the INTENT is the drift the
head exists to catch, and no other step forces the look
(hypothesis) —
ENDING with one advance prompt — "(y) advances per the
recommendation"; anything else is free-form override. Design
decisions are never posed as choices; the prompt carries loop
control only. Unattended, the recorded recommendation advances the
run. `Mode: auto` in the header (operator-declared at run start,
fixed in the auto direction only: an operator appearing mid-run
may take over on one recorded line and the run continues
attended — supervision is monotone, adding it never needs
justification; an attended run never silently becomes auto
(hypothesis)) forces the unattended branch throughout: no
prompts, every
recommendation advances on record, reconciliations surface only
in the close. Advancing locks the design — the LOCK. Its
transaction machinery lives in the git tool; the desk's work is
the composition, the one judgment instrument, and the record
forms around the verdicts.
(a) Pathspec composition. The tracker plus every LIVE lock-set
path (a re-lock inherits prior locks' live lock-set lines; an
unchanged inherited path is a no-op, legitimately absent from
the readback). Anything beyond the tracker enters ONLY named
by a lock-set line appended before the lock (`- F<n> [VERIFIED]
lock-set: <path> — basis: <the entry that produced it>`), and a
lock-set path — a unit write-set path too (Implementation) —
names a FILE, never a directory: a directory pathspec commits
whatever else the operator touched under it (the tool halts on
one). The design phase edits no other repo file, so the tracker
is normally the whole pathspec.
(b) The judgment instrument the tool cannot run: re-read each
lock-set artifact against the entry that produced it — the
tool's collision check reads staged operator state (porcelain
column one), but two states it cannot attribute need this
re-read: column-two divergence on run-produced content, and
every UNTRACKED add (the tool adds any surviving untracked
pathspec path — an operator draft sitting where a lock-set line
points is caught only by this re-read); what it misses rides
into the commit — the attack
round's probes are the backstop, the residue named, not hidden.
(c) `lock-check --tracker <path> [--lock-set <path> …]`.
Verdict routes: HALT_STATE is the operator's half-finished
operation, the tree untouched — an attended halt re-enters on
the operator's clearing reply; unattended, a halted LOCK closes
the run FAILED (no lock, nothing to build on; Close, Status
written FAILED) while a halted unit rides the close's
deviations (Implementation). HALT_TRACKER_COLLISION and
HALT_TRACKER_UNPINNABLE halt the same way — the tracker is
never dropped, and never force-added. LOCK_CHECK_DROPS records
each drop BEFORE the commit, in the tracker the commit pins: a
[VERIFIED] F-line carrying the verdict line as basis, and the
path's lock-set line superseded — `- F<n> [INVALIDATED] <path>
dead (collision|ignored) — basis: <the drop F-line's id>`
("contradicted" anywhere in this skill means that supersede
form) — surfaced when the operator is present, riding the
close's deviations unattended.
(d) `lock-commit`, same arguments plus `-m` and one `--drop`
per recorded drop (LOCK_CHECK_CLEAN skips straight here, no
drops). HALT_DROPS_STALE or HALT_DROPS_UNACKNOWLEDGED
means the acknowledged and live drop sets differ — the tree
moved between check and commit, or the `--drop` list was
mis-composed: re-run
lock-check, re-record, retry. LOCK_COMMITTED's sha is the LOCK
COMMIT — the attack brief pins it, and the locked design IS the
record at that commit. LOCK_COMMITTED_EXTRAS is a mis-composed
pathspec: the extras' content is already in history — recorded
as a collision-class contradiction and named a brief exclusion,
never reverted out of the working tree (the revert would
destroy the very operator state the finding names).
HALT_RESIDUE_PERSISTS is a halt WITH commits in history: its
`shas` field lists every landed commit, the last one not
readback-clean — booked, the shas surfaced, and the run halts
like HALT_STATE (never "no lock, nothing to build on": the
commits exist) — and so does ANY halt verdict carrying `shas`
(a COMMIT_FAILED or BLOCKED_CONTENTION out of the readback
laps landed its first commit; The tools' override). Any other
lock verdict (HALT_NO_CHANGES,
HALT_NO_PATHSPEC, HALT_DIRECTORY_PATH, HALT_MISSING_PATH,
BLOCKED_CONTENTION — the last two in their plain senses, never
the unit rules' meanings — USAGE_ERROR, GIT_ERROR,
INTERNAL_ERROR) halts the lock uncommitted, verdict line booked
as a `record:` F-line, routed like HALT_STATE.
Everything outside the pathspec is operator state — never
committed, never unstaged, never restaged. Desk scratch
belongs in the desk's own scratchpad, never the repo (the
attacker rule's counterpart, Verify). A brief
that asserts the tree claim (The
attack's freeze scope, named there) names any tracked surface
the claim cannot then cover as an
exclusion (the drop and extras lists above are that
list's mechanical floor; an operator-modified tracked path
outside every lock-set path joins through this same rule) —
the attacker
reads an excluded path as outside
the frozen surface, evidence of nothing; a brief that never
asserts it needs no exclusions. A
re-derived design re-enters here: new [READY], new sweep, new
lock commit.

## The attack (forcing point 3)

A fresh-context attack on each locked design by a context that did
not produce it, before implementation. The attack brief carries the
tracker PINNED at the locked design's commit — produced by the
record tool: `filter --tracker <path> --sha <lock sha> --out
<artifact path>` serves the sha, never the working tree (a live
tree serves HEAD) — the artifact path sits OUTSIDE every repo,
like the seals and for the seal rule's reason (an in-repo
artifact is an untracked file under a brief asserting tree ==
lock commit, and a NESTED outer checkout has the same exposure;
the tool halts ARTIFACT_IN_REPO on any; `--out` alone is
cwd-relative — an artifact lives outside the repo, so
repo-root-relative grammar cannot name it) — and
drops the two Superseded species, counts
in its verdict — entry-shaped lines inside a Superseded
SECTION are PRESERVED (the never-filter sentence below is the
contract; a section drop that swallowed entries put a live
money-path finding out of every attacker's sight): contiguous
quoted blocks whose first line is `> Superseded — <label>` (their
production: the return processing below), plus sections headed
`## Superseded —` — legacy landings from earlier skill versions,
possible in resumed trackers only; ENTRIES are never
filtered (dead bodies are load-bearing for closure questions, and
a hand-summary is the paraphrase-drift class). The brief states
the filter's form (the two species) beside the artifact; it also
carries the question and the read-only tail (dispatch skill
`references/forms.md`). Unfiltered, the
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
locked design — it gets the attack again, its repairs landing as
ONE re-lock: per-finding re-locks split the priced unit
(hypothesis). A round dies two ways, one clause (hypothesis):
ABORTED in flight when a queued desk finding kills the locked
design — the round is not left running over an object already
scheduled for replacement; its A-line lands `[VOID]` with body
`abort:` citing the killing entry (which must predate the
abort — the check against aborting uncomfortable rounds). And
VOIDED on return when the round's PREMISE was broken (wrong sha
pinned, tree claim untrue at dispatch, wrong exclusions): graded
as a round, never finding-by-finding — a review of the wrong
object is not evidence about the right one, and salvaging its
findings is how a broken instrument's output enters the record
carrying a round's authority; the A-line lands `[VOID]` with
body `premise:` naming the brief defect, the brief is repaired,
a NEW round dispatches. A voided round's observations enter only
as desk findings the desk re-derives itself. Each round records an
A-line (The record). At a round's return every finding is
classified, with basis: DESIGN-SUBSTANCE (wrong mechanism, money
path, silent failure in the shipped system) or RECORD/INSTRUMENT
(the run's own bookkeeping); findings append as F-lines with the
tag their evidence earns — reach-matched in hand → [VERIFIED],
where a judgment finding's reach is the cited record or design
text itself, else [PENDING]. An UNMEASURED verdict is
an open question the desk completes itself — its own executed
measurement, recorded as the F-line's evidence — before the
round's A-line lands. Report quotes the desk retains (pasted,
never paraphrased; the defang below is the one sanctioned
mutation) append as the quoted block the record tool produces —
`quote --label "A<n> quotes"`, raw text on stdin: every line
begins `>`, a blank line a BARE `>` (trailing whitespace may not
survive target-repo hooks), the block ending at the first line
not beginning `>`; bracketed tag literals defanged — brackets
dropped, lowercased in place, the defanged names listed after a
semicolon in the composed first line `> Superseded — A<n>
quotes; <names>` (semicolon and list absent when no literal
occurs; the filter matches the label's opening form) — so the
defanged forms differ from every counted tag literal in both
brackets and case: the stats reader's literal greps carry the
brackets (verified against its source), the brackets the
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
live closure. The closure read runs through the record tool at
each dispatch — `closure --tracker <path> --unit U<k>`
(without `--unit`: CLOSURE_LIVE / CLOSURE_VOID over the whole
record): CLOSURE_VOID bars every unit — a scopeless line, or a
post-closure [INVALIDATED] line for an entry LIVE at the
closure whatever its opener (the mis-scoped premise-kill);
CLOSURE_RECORD_MALFORMED bars every unit the same way — an
entry-shaped line broke the grammar (dropped tag brackets, an
out-of-enum tag, a near-miss the head grammar cannot parse), and
the entry set the closure computes is unsound until repaired:
RE-STATE the line — same id, same tag, content restated — as a
new appended line (append-only repair; the tool disarms only on
that re-assertion, since a later unrelated line proved able to
convert a premise-kill void into a dispatch), then re-run;
CLOSURE_ABSENT means the gate is not open (the last A-line is
not [ZERO-DELTA] — the normal state during a reopened design;
dispatch waits); UNIT_HELD bars that unit on its
unresolved hold entry; UNIT_DISPATCHABLE lists the live
amendment lines that travel. The brief carries the tool's
verdict line, the closing A-line quoted, the lock sha, and the
listed amendments — never the raw criterion. The criterion the
tool computes — its semantics are what the desk WRITES so the
read comes out true: unit U<k> may dispatch when the tracker's
last A-line is `[ZERO-DELTA]` and no F, D, or R line appended
after that A-line (post-closure) is SCOPELESS — a scopeless line
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
travels; fail → two composed lines: the restatement dies under
its own id — `- <id> [INVALIDATED] unit U<k> <clause> —
basis: <the check's failure>` — opening `unit U<k>` like
the [PENDING] line it resolves; and the parent's clause
disposition is re-written — `- <parent id> [INVALIDATED]
record: clause <c> dead (<the check's failure>) — basis:
<the restatement's id>` — bookkeeping over an already-dead
entry (the closure rests on no clause of an invalidated
body; dispositions aggregate, The loop) — so no clause list
points at a dead restatement, the re-dispatch proceeding
without it
and the unit's want surfacing as its gap; one bearing wider
on the design is SCOPELESS and voids — the premise-killing
consequence (stop the siblings resting on it, let the rest
land, re-enter ONCE). Units with disjoint
write-sets run parallel (one shared index — commits
serialize; the tool's capped retry absorbs the
contention). A missing
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
Unit briefs carry the git tool's invocation lines with the
script's absolute path (The tools) — desk prose reaches no
unit, and no procedure text is expanded into a brief.
Composition-side, the desk checks the write-set: paths name
FILES and are `git check-ignore`-clean — a composition error
caught before dispatch (the tool re-checks and halts, the
backstop). The unit runs: START, before any edit —
`unit-start --write-set <file> …`. UNIT_START_CLEAN makes
every later modification the unit's own; UNIT_COLLISION (an
operator edit or draft on a write-set path the unit would
otherwise overwrite and commit), HALT_STATE (the
operator's half-finished operation, tree untouched), and any
other START verdict (HALT_IGNORED_WRITESET,
HALT_DIRECTORY_PATH, USAGE_ERROR, GIT_ERROR …) halt the
unit UNBUILT — no edit, no commit, no landing annotation.
COMMIT — `unit-commit --write-set <file> … -m <msg>`.
Verdicts: UNIT_COMMITTED → landing annotation with its sha.
UNIT_COMMIT_COLLISION → an operator stage landed on the
write-set mid-unit (the commit seam re-reads column one — ANY
staged state halts: column one cannot attribute a staged add,
and a blocked prior attempt's leftover never reaches this seam,
since the re-dispatch meets it at START and the desk's clearing
handles it): report, nothing committed, the unit's own
edits left in the worktree and named as poisoning the
write-set.
UNIT_NO_DIFF_VS_HEAD → nothing differs from HEAD: the unit
runs its residue check (the brief's symbol-anchored
criterion — the discriminator, never an exit code) and
reports already-present, the landing annotation carrying
`already-present` in place of a sha (HALT_IGNORED_WRITESET
re-firing at this seam routes as blocked below, its
ignored-path diagnosis kept from the verdict line, not as a
generic failure). HALT_MISSING_PATH → a
write-set path the unit never populated: reported as a gap,
nothing landed. HALT_STATE → an operation the operator began
mid-unit — distinct by verdict from BLOCKED_CONTENTION →
index.lock held through five spaced attempts (the verdict
carries the error text and whether the lock file remains).
UNIT_COMMITTED_EXTRAS and UNIT_COMMITTED_RESIDUE landed
their sha — landing annotation — but carry a finding the
desk books as a `record:` F-line from the pasted verdict:
extras are the lock's mis-composed-pathspec rule (recorded,
brief exclusion, never reverted); residue is write-set
divergence after the commit, triaged like a collision. Any
other verdict — ADD_FAILED, COMMIT_FAILED, GIT_ERROR are the
common members, the global catch-all rule covers the rest — is
reported as blocked, uncommitted edits named — they poison
the write-set for the re-dispatch. EVERY non-committed exit
pastes its verdict line in the unit's report and leaves the
tree exactly as the tool left it — never silence. The desk
books each non-landed unit return as a [VERIFIED] F-line
opening `record:` (basis: the pasted verdict line; a unit
return decides nothing — voids nothing, re-opens nothing),
never through the gap triage (HALT_MISSING_PATH's gap report
excepted), PLUS a hold entry — `- D<n> [AUTO-ACCEPTED] unit
U<k> held: <reason> — basis: <that F-line's id>` — the tag
surface that carries an unlanded unit into the close's
enumeration (the gap path's pattern; without it a held unit
reaches Verify invisible to every gate). Clearing a held
path is DESK work, decided by provenance: where the record
and the task
system show the dirt is the run's own — a stopped or dead
unit dispatch (a sibling OR the same unit's own prior
attempt) whose write-set covers the path, its clean START
check readable in that dispatch's output — the desk clears
BY SHAPE, reading each command's exit: a tracked path
restores (`git restore --source=HEAD --staged --worktree
-- <tracked paths>`), an untracked leftover is DELETED
(restore cannot touch what HEAD lacks, and a mixed call
fails whole, restoring nothing), and a staged-NEW leftover
(in index, not in HEAD) is `git rm -f`-ed — restore reaches
neither of its halves. ONE clearing attempt: a
re-dispatched unit colliding again on the same path is held
as operator state — no clearing loop. A path
without that provenance is operator state — held; the
operator's clearing answer appends the hold entry's
resolving line — `- D<n> [COMMITTED] unit U<k> cleared:
<path> — basis: <the reply>`, opening `unit U<k>` (the
natural scopeless phrasing voids the whole closure) — and
the desk re-dispatches on it, unattended
it rides the close's deviations. A BLOCKED_CONTENTION
return triages on the same provenance: siblings still
live → re-dispatch after their landings; none live and the
verdict says the lock file remains → the stale
`.git/index.lock` a dead dispatch left, removed by the desk
on that provenance alone (the task system showing no live
unit), else surfaced. A HALT_STATE halt re-dispatches on
the operator's clearing reply, unattended it rides the
close's deviations.

## Verify (forcing point 5)

Executed, isolated, against the recorded requirement; Phase flips
to verify at dispatch — a dispatch made only with no entry's
latest line [PENDING] (the [READY] sweep's no-[PENDING] condition;
the record tool's `sweep` re-runs at this seam). A fresh
context that did not build the work runs the real checks — tests,
probes, renders, at the altitude where the work takes effect —
against the tracker's requirement head as amended by its R-lines,
and pastes the checks' own
output; a launcher's exit status is not a verdict. The brief
demands a verdict PER R-LINE — met (the check's own output), not
met (with it), or NOT EXERCISED — because coverage failure is a
non-event only the isolated verifier can name: a requirement
nobody checked returns exactly what one that passed returns, and
the desk cannot know what a fresh context declined to exercise
unless the brief demanded the statement. The V-line's evidence
carries the per-R table; PASSED is recordable only with every
R-line met or its non-exercise carried as a named
[AUTO-ACCEPTED]. (hypothesis) The verify brief
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
[ISSUES FOUND] it stays in-progress). Each [ISSUES FOUND]
finding is CLASSIFIED before any repair, with basis, and the
class sets the route — the four repairs differ by an order of
magnitude in price, and the dangerous misroute is the cheap one
(a design defect patched inside a unit is the no-design
invariant violated with nothing forcing the split): WORK (the
unit built the design wrongly → re-dispatch that unit; lock and
closure untouched), DESIGN (the design cannot meet the
requirement → the premise's scopeless [INVALIDATED], closure
voids, re-derive), REQUIREMENT (work matches design, design
matches R-line, the R-line is wrong → amendment or
reconciliation), INSTRUMENT (the check itself is defective →
the V-line's evidence [INVALIDATED]; no work changes).
(hypothesis) Verify returns count against the run budget (The
record) — an unattended run earns no infinite loop.

## Close

At the verdict that ends the run ([PASSED], or FAILED per
Verify, per a lock halt — HALT_STATE or an unpinnable
tracker, the header written FAILED at that halt (the halt
routes here with no verify verdict to write it) — or operator
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
After the close is appended and Status written, pin the
delivered record — `lock-commit --tracker <path> -m <close
message>` over the tracker alone (post-lock appends otherwise
never enter git); its verdict line delivers with the close.
HALT_NO_CHANGES here means the record is already pinned (a
re-run after an ambiguous first attempt) — benign, delivered
as-is. A HALT here (HALT_STATE on an operator operation in
flight, or any other) never blocks delivery: the close
delivers UNPINNED with the halt's verdict line named in its
deviations — attended, the operator's clearing reply gets one
pin retry; there is no later seam to catch an unpinned
delivery, so the deviation line is the record of it.
Skipped only where the run never had a pinnable tracker
(preflight's UNPINNABLE halt). Delivering the close is then
the desk's final act, so the
delivered artifact carries its final Status. Open
reconciliations survive
into COMPLETE, enumerated in the close; an operator answer
arriving later appends its resolving line to the closed tracker —
append-only has no expiry, and the close's enumeration is what
makes the late landing findable.

## Fire-born and hypothesis clauses

No lens list, no lens pass. When a real blind spot fires in
operation, mint it as a pointed hunt clause inside the section it
serves (usually The loop's brief-writing) — one incident as
provenance, amendment over addition; log the mint and each
subsequent firing in the source repo's dev-notes/OBSERVATIONS.md —
a desk in a target repo without a local checkout at hand rides
the observation on its run report instead. A clause with no
firing since the last review is a cut candidate.
A second provenance class (PLAN.md, hypothesis-patch amendment):
clauses marked `(hypothesis)` were minted PROACTIVELY as
universally-advisable loop calibrations, each with a validation
criterion logged in dev-notes at its mint — pruned at fire-rate
reviews exactly like fire-born clauses, on their criteria. An
unmarked addition with neither provenance class is still the
tripwire.

## Birth-class declaration

At birth this file was enforcement structure + bindings only —
zero capability patches. ~150 operational lines is the
stabilization TARGET, not the live count: the trial accretes
fire-born structure above it deliberately, and the compression
pass owed at stabilization (booked in dev-notes) brings it back
down. A patch landed without provenance is still the tripwire.

---
name: statiker
description: Conducts a development task from investigation through verified implementation — a free design loop held by five forcing points (recorded decisions with bases, dispatchable-design stop rule, a fresh-context attack on each locked design, no-design implementation, isolated executed verify). Successor to clippy; use only when the operator explicitly invokes statiker or requests a statiker run.
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
- The operator corpus, where the stack has one, carries the
  grounding and evidence ethics (bases, refutation probes,
  altitude); assumed, not restated. Without one,
  `references/evidence.md` (under this skill's base directory) is
  the binding source — read it before the run's first entry, and
  on such a stack attack and verify briefs cite it in place of
  the corpus.

## The tools

Two shipped state machines live under this skill's base directory
(the Skill injection's base-directory line names it; invoke with
python3): `scripts/statiker_git.py` — git transactions: the
run-start preflight, the LOCK commit, unit START and COMMIT — and
`scripts/statiker_record.py` — record grammar: tracker lint, the
[READY] sweep's computable slice, the closure predicate, the
pinned attack artifact, the append-only check against the pin
(`pinned`), the verify-leg copy-freeze check (`verify-gate`), the
never-sustain round-open gate (`sustain`), the zero-landed progress
tripwire (`tripwire`), defanged quote blocks.
The two scripts
plus their red-first battery (the source repo's tools/ suites —
the attack rounds' probes and record findings mechanized) are the
EXECUTABLE SPEC of the record grammar and the transaction
semantics: the contract lives there, this page keeps principles
and desk conduct, and a divergence is graded against the battery,
never against this page's wording. Principles the desk relies
on: a path is taken AS NAMED in every git operation, never
substituted; containment resolves in the direction of SAFETY — a
must-be-inside path (lock-set, write-set) is decided on its REAL
resolution, a must-be-outside path (artifact, seals, attack
worktrees) is outside
only when named and real form agree — any realpath
acceptance noted per path in the verdict as `resolved_from`,
and a path problem halts at a CHECK, never a commit. Byte policy
runs both
directions: git byte output decodes the way the OS decodes argv,
and verdict and quote output emit at the byte level over the
input's own bytes — a tool that re-spells a byte on output mints
the second spelling the input rule exists to prevent. The record
tool anchors its repo at the TRACKER's own directory, the git
tool at its invocation cwd — briefs invoke it from the repo
root, which the invocation lines already do. Every
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
production counts. `waves` returns WAVES_COMPUTED — units sharing
a declared write-set path grouped, members of a group SERIALIZE,
groups are mutually parallel-eligible; a unit whose record lines
declare no live write-set comes back UNPLANNABLE, never placed
(the line form: Implementation; a unit with no `unit U<k>`-bodied
entry at all appears in neither list), and the partition is no
dispatchability read: the per-unit gate stays `closure --unit`.
`trend` returns TREND_COMPUTED /
TREND_NO_ROUNDS — per-round F-LINE counts (every F-line in a
round's span, not attacker findings alone) with an arithmetic
trajectory verdict. `sustain` returns SUSTAIN_OK / SUSTAIN_DENIED /
SUSTAIN_NOT_APPLICABLE — the never-sustain round-open gate (Stop
rule, "That closes design"). `tripwire` returns TRIPWIRE_FIRES /
TRIPWIRE_SILENT — the zero-landed progress tripwire (The record,
Budget). All four halt WAVES_RECORD_MALFORMED /
TREND_RECORD_MALFORMED / SUSTAIN_RECORD_MALFORMED /
TRIPWIRE_RECORD_MALFORMED where an
entry-shaped line broke the
grammar, repaired like any lint hold (`corrects line <n>`
composed from the verdict's violation lines). ANY verdict no
section names is a halt for
the seam that ran it — booked as a `record:` F-line from the
verdict line, the seam's halt route applying (TRACKER_UNREADABLE,
PIN_UNREADABLE, NOT_A_REPO, PATH_OUTSIDE_REPO, PATH_INSIDE_REPO,
USAGE_ERROR, GIT_ERROR, INTERNAL_ERROR, and any future member).
One override
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
in-progress operation, informational at this seam). Preflight
runs a DEDICATED repo-health read — index-reading by design, so
a corrupt index halts here, before any work rests on it (a
mid-run corruption still surfaces at whatever seam meets it).
Strictness is the health read's alone; every other read keeps
its own DOCUMENTED exit semantics — a non-error exit (the
ignore check's not-ignored) is an answer, an error exit of any
read still halts.
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
clippy's ledger convention. Of the stats reader's contract, the
ADMISSION half (Status/Phase enums in the header window) is
maintained and pinned; its per-metric greps are NOT maintained
against this grammar — SERIES metrics for a statiker run come from
the record tool's `trend` verdict (unit parallelism from `waves`),
never from the stats reader's counting literals (its cycle count
and decision-family collapse both diverge silently here,
measured). That disclaimer is scoped to the counting metrics
alone: the defang duty, bare tags, tag-first counting, and the
landing indent all stand on the record tool's own parsing and the
closure gate, not on the stats reader — the unmaintained greps
revoke none of them. Never overwrite
another run's tracker; resume
an in-progress run from its tracker, not from memory. That resume
compares the header's `Skill:` version against the version this desk
is SERVED (the Skill injection's base-directory line): a release
reaches a running desk only as a RESTART, never as an upgrade — the
pin resolves at session start and the already-loaded skill text owns
a live desk's conduct, so a delta means desk and record run
under different rules — in either direction: an OLDER desk over
a newer record proceeds no further than the record gate and
WRITES NO CLOSE — a desk under the wrong rules appends nothing;
the run stays in-progress for a correctly-versioned successor,
and the surfacing is the desk's reply, not a record write. On a
mismatch the desk names
the VERSION PAIR before the next forcing point — and what the
delta invalidates only where the older text is at hand (the
source repo's git); a desk without it surfaces the pair at the
run's next operator touchpoint rather than reconstructing the
delta from memory — and
records — on the MISMATCH only, carrying the SERVED version (the
header keeps the version that wrote it) — the BARE label line
`SKILL: statiker <version>` in the body region: below the first
`## ` heading, standing alone, never inside a tag-first entry
line (above the first heading is the head region, where nothing
parses as an entry), surfaced
with the header's version as `skill_versions` in sweep and closure
verdicts (attribution, never a gate): the `Skill:` line is pinned
surface — Status and Phase are the only mutable fields — so a header
rewritten to the new version reads as tampering, not as an update.
A resume opens with the RECORD GATE, before any design work: run
`sweep` and `closure` first, whatever the resume's cause. Their
verdicts route by KIND at this seam: `closure`'s state verdicts —
CLOSURE_ABSENT, CLOSURE_LIVE, the mid-design normal — are
information, never halts, and CLOSURE_VOID bars units, not the
design work this gate runs ahead of; only FORM holds gate. The
gate's repair route covers FORM holds only — grammar, lint, and
dead-basis classes, the ones a stated repair form can close:
those are repaired through a DISPATCHED mechanical leg on the
cheapest capable tier (the routing table's execution default; the
verdict names each violation's class and repair form, so the
brief is decision-complete by construction, and judgment residue
the verdict NAMES returns to the desk, never decided in the leg).
The leg is the tracker's ONE WRITER for its duration: the desk's
own appends wait for its return — the attack freeze's shape at
this seam — and a tracker that moved under the leg is the leg's
halt: report, never repair over a moved file.
Latest-line [PENDING]s from open legs are LIVE WORK, not repair
material: they resolve by the ordinary body-read of their
returns, and clearing one to [AUTO-ACCEPTED] to satisfy a gate
destroys the evidence the tag holds open. The desk grades the
leg's return by re-running `sweep`, `closure`, AND `pinned`
against the standing lock itself, never by the leg's claim — the
positional pair reads an in-place rewrite as clean, and the pin
diff is the one check it cannot fool, whether or not the leg
committed its work. A record with no pin yet is young and its
holds few — there the repair is desk work by the
brief-would-rival-the-repair rule
below. So the
desk's context carries verdicts, not the repair work (a resumed
desk repairing its own accumulated holds inline spent a session on
record archaeology before its first design act). A hold set small
enough that the brief would rival the repair stays desk work.
The gate covers the record's FORM; a resume also re-runs the
record's dated, WORLD-FACING discharges: a staleness check
measured at its date expires with every commit since — re-run the
bounded diff (`git diff <the discharge's read sha>..HEAD -- <the
design-cited paths>`; the discharge line carries the sha it read
at, which IS its expiry anchor — one without a sha looks
unexpired forever and re-runs unbounded) over design-cited paths
before any work rests on the
record's citations, and a discharge NAMES ITS OWN EXPIRY, so the
next resume inherits an obligation, never a reassurance (a
"zero commits since" discharge carried across a 7-day resume hid
16 commits, one touching the very file that round's HIGH landed
on). A resume also reads the newest round's QUEUE (`seal-path`
prints it): an unspent queue is inherited work — land and spend
it before new appends — the resume's order: version pair →
record gate (its leg, if one, returning first) → world-facing
discharges → queue land+spend, then re-run `sweep` if the queue
landed lines — except where the newest A-line is
[DISPATCHED] (a desk died mid-round): the append freeze still
holds, the round re-enters as its own round, and the inherited
queue lands and spends at that round's terminal A-line. A resuming
desk's first reply enumerates the run's standing operator state
read from the record — the Mode line, every live operator-imposed
hold, any mid-run INTENT line — shown as INFORMATION, never
re-asked: frozen operator ground only its owner lifts, and a lift
arrives as an operator line, not as an answer to a desk question.
An entry
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
`Mode: attended` (Stop rule; absent = unattended, the default);
`Budget: cycles <n> / rounds <n> /
verify <n>` — the run's declared bound over every repeating seam,
defaults 7 / 4 / 3, declared at run start where a successor reads
it (an unattended loop without a declared bound terminates on
context death, the one ending that produces no readable verdict).
The line takes an optional trailing `/ tripwire <n>` field — the
zero-landed tripwire's own arming carrier, written at seed; arming
a LIVE run means editing the Budget header line in place (header
fields are mutable state, not entries — the tool reads only the
first `Budget:` line, so an amendment F-line records the operator's
authority but never arms), or passing `--threshold` at the seam. A
Budget line with no `tripwire` field leaves the breaker unarmed
(below).
Exhaustion never continues silently: attended it forces the
operator prompt; unattended, the cap is a SAFETY ESCAPE only (P19 —
every cap firing to date, across two runs, was operator-overridden:
a bound whose every firing is overridden carries no information and
trains the override reflex) — hitting it STOPS-AND-REPORTS for the
operator, never grades FAILED by itself. The DRIVING stop signals
are progress-shaped and record-computable, checked well before the
cap: the ZERO-LANDED tripwire (`tripwire --tracker <path>
[--threshold <n>]`, TRIPWIRE_FIRES when at least `<n>` resolved
attack rounds exist yet neither a landing annotation nor a V-line
does anywhere in the record — `<n>` NAMED by the caller at arming
via `--threshold`, or read from the header Budget line's own
`/ tripwire <n>` field when `--threshold` is omitted, `--threshold`
always overriding the header; never hardcoded in the tool, and
never guessed — neither present is TRIPWIRE_SILENT with reason
"unarmed") and the existing NON-CONTRACTING
trend grade (The attack) — BOTH route to the 0.68 NARROWING route
(The attack), never to another same-form round. Housekeeping never
bills the run's budget: record-repair legs (The record, the resume's
mechanical leg) and sweep/closure passes are meta-owned, outside
cycle accounting. Excess iteration is a SYMPTOM, never a verdict —
every cause is diagnosable, so a stop-and-report fires as a MINT
SOURCE: it owes a named cause at close-out, read from the
DISCRIMINATING EVIDENCE pre-registered when the check was armed (the
trend verdict for arithmetic, named locus body-reads for
repair-versus-account, each terminal entry's class split) — a
firing's cause report is a READ, not a composition — and a
computable cause becomes a named tripwire so the next run stops on
the pathology itself; a breaker tripping twice for one cause
indicts the missing tripwire. The stop-and-report has THREE
ENDINGS, all operator-owned: FAILED (the operator refuses the run);
EXPORT (the operator re-scopes — the displaced scope exits per The
loop's exit machinery to a backlog entry); or CONTINUE — a
disposition that GRANTS the closing round as an ordinary budget-raise
entry (above), so the route back to the gate is machinery, never
improvisation.
The bound is operator-owned from the moment it is recorded: the
desk SPENDS the budget and never raises it — a mid-run amendment
is an operator decision, whatever provenance class the bound's
text carries (fire-born, not hypothesis-class: a desk-amended
bound, set just above current spend, bound nothing). An operator
raise LANDS as an ordinary entry quoting the operator's line —
the header is pinned surface, never rewritten — and every later
exhaustion check reads the LATEST such entry over the header's
default. The raise line's template: `- F<n> [VERIFIED] record:
budget raised to cycles <n> / rounds <n> / verify <n> — "<the
operator's line verbatim>" — basis: operator` (the `record: `
opener is what voids no closure and re-opens no unit;
machine-findable surfacing in the verdicts is parked tool
work — until it ships, the exhaustion check's read is a
body-read for this template).
Status and Phase sit within the first ~20
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
reads this head plus its R-lines, not the conversation.
At requirement-head composition the desk gauges the item's
WRITE-SET SPAN, bidirectional and entry-boundary-skeptical (P21:
find-time entry boundaries are claims the seed RE-DERIVES, never
adopted unit boundaries) — intake re-derives the unit set from the
entries' write boundaries and the current world, slicing an
oversized entry AND batching under-sized siblings whose write-sets
overlap: each candidate unit names the files realizing it, and units
naming an overlapping file merge or serialize — a mechanical join
over each candidate's declared write-set, the instrument. An item
that is migration-bearing, multi-consumer,
or architecture-wide seeds as a DECOMPOSITION run whose
done-criterion is exported unit-sized backlog entries —
implementation runs seed per unit, never the architecture-scale item
whole. Three incidents: run 1 spent nine sessions on the full
canonical-market-identity item for zero landed units, the narrowing
route taken only at close on operator prompt; its own five
find-time-composed exports named a live lead (the upsert
self-healing property) that may delete one of them — structure
written before the evidence that shapes it, the reason the gauge
re-derives rather than adopts; run 2's bound-firing cause report
named item scope as the run's root pathology — a complete
persistence enumeration across a 60-table database demanded for a
one-deletion change, the count walking 7→9→11→12-plus across five
rounds, each closure attacked on the ground the requirement's width
created. Distinct from the in-run early decomposition round (The
attack's narrowing route, P12): this gate fires AT SEED, before any
cycle spends.
(hypothesis) The head derives from INTENT + the PROFESSIONAL
STANDARD, never INTENT alone: the customer is owed
professional-grade results they never asked for, so an
underspecified INTENT derives the quality requirements a
competent shop would — a size and complexity budget, no
unjustified abstractions, a threat model where inputs cross
trust boundaries — as R-lines gradeable by judgment, never
lint; the derivation is the run's first and largest design act
and iterates with the loop like everything downstream. Where
the INTENT supports one, an R-line carries a success metric — a
real number the work moves. R-lines state the PROBLEM at its
own altitude: a solution choice inside an R-line locks design
prematurely and dodges the attack — solutions are D-lines. An
underspecified INTENT also derives a CUSTOMER-LEGIBLE mirror —
a 3–6 sentence announcement-form restatement of what ships
(mockups for UI work), recorded as an R-line the customer could
grade, and reconciliations reference it: every other surface of
the record is record-speak a non-technical customer cannot
grade. A full-spec INTENT derives a near-empty complement, and
a deviation from the spec's letter escalates as reconciliation,
never a silent derivation. A derived
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
until the operator answers. An ask on OPERATOR-AUTHORITY ground —
one only an operator line can satisfy: an exemption grant, a
bound raise — cannot advance on a recommendation. It lands as an
ordinary [PENDING] entry under its own id, its body naming the
gate where it bites (gate names written defanged — the
tag-literal rule), and it holds exactly what a live [PENDING]
holds: work outside those gates continues, and the entry is what
a resume read and the close find. The skill's mandated stops
keep their own rules — budget exhaustion, preflight surfacing,
an attended halt's clearing, the non-contracting prompt, the
irreversible-unit hold; this class is none of them. Attended,
the ask leads the next prompt as a labeled decision line;
unattended it rides the close with the open reconciliations. An
advance prompt's "y" answers loop advance only — a grant enters
as the operator's line quoted in the clearing entry (`— basis:
operator`), never inferred from an advance. An authority ask
contests no text and skips the provenance trace. Escalation is
PROVENANCE-GATED:
before a question routes to the operator, trace the contested
text to its origin. Operator words escalate as reconciliation;
derived text — R-lines, inherited constraints, a run
instrument's policy — is desk work: amend or carry
[AUTO-ACCEPTED] with basis, presented as INFORMATION at the next
seam, never as a question. An operator-imposed hold is always
theirs. Attended mode moves WHERE decisions are presented — the
seams — never WHO makes them; a question the record can answer,
asked anyway, spends the operator's one seat. A mid-run
operator instruction that
changes what the run is FOR appends at the record's END opening
with the literal label `INTENT: `, its authority the operator's
words — never inserted under the head: append-only is
positional, and an insertion would shift every line number
under a live `corrects` reference — and not an R-line: R-lines
are derived text, operator words are not — and the desk states
which live
decisions it kills (a killed one takes the scopeless
[INVALIDATED] route; the closure voids and the design
re-enters). The label is what makes the landing machine-
findable: every sweep and closure verdict LISTS the late
INTENT lines it found (`late_intent`), and verify grades
against the head plus every listed line — the tool, never
memory or conversation, is what finds them; conversation is
the one channel verify deliberately never reads.
(hypothesis) The record's one mutable surface is
the header's Status and Phase fields, updated at each transition
and at the verify verdict; everything below them is append-only.
Status writes its enum member verbatim — [READY] keeps its
brackets (the header parse and the stats reader both admit only
the bracketed form).
Run `lint` once the header and head are written: a form defect
found here costs re-creating a one-screen file before anything
rests on it; found at the [READY] sweep it holds a full record
whose head the append-only rule cannot rewrite. The append-only
claim is checked mechanically once a pin exists: `pinned
--tracker P --sha S` — the two mutable field lines above are
exempt, every other line binds byte-exact against the pin.
PINNED_APPEND_ONLY proceeds; PINNED_REWRITTEN halts the seam
that ran it, first divergent line in the verdict (an in-place
TAG rewrite reads exactly like a clean record to every
positional gate; the diff against the pin is the one thing it
cannot fool). Run it at resume and before any re-lock — S is
the standing lock, recoverable as the newest commit touching
the tracker (every lock's pathspec carries the tracker, and
nothing else legitimately commits it).

Entries are one line each, status tag first, appended never
rewritten (the templates below wrap only on this page). A status
change is a NEW tag-first line for the same id
(`- D<n> [INVALIDATED] <why> — basis: <…>`) — never an edit of the
old line; the record tool parses entry state from tag-first
lines alone.
The record's machine tokens are CASE-SENSITIVE LITERALS, not
phrasing: the entry head `- <C><n> `, the scope openers
`unit U<k> ` and `record: `, the hold form `unit U<k> held: `
(that exact prefix as the body's opening — a hold written any
other way holds nothing), the write-set declarator
`write-set: ` after its unit scope opener (Implementation), the
`corrects line <n>` repair token,
the late-instruction label `INTENT: `, and three bare label
lines: `SKILL: statiker <version>`, `SWEEP_EXEMPT: <code>
lines<=<n> — basis: <citation>` / `SWEEP_EXEMPT: <code> line <n>
— basis: <citation>`, and
`unit U<k> irreversible: <effect>`. The two attribution labels
(`SKILL:`, `unit U<k> irreversible:`) carry NO near-miss class by
recorded decision (a bare-word scan false-fires; attribution
fields fail soft), and a mistyped `SWEEP_EXEMPT:` fails safe —
the hold it meant to net still blocks. DETECTION is wider
than validity by design: the lint detects would-be machine
tokens positionally — never by word-search — and anything
detected that fails the exact literal lints as a near-miss
violation; validity itself never relaxes. The detection
surfaces, their exclusions (quoted lines and the requirement
head above the first `## ` heading parse NO entries — operator
words and report quotes never register), and each violation's
class and repair form are settled in the executable spec (The
tools); the verdict NAMES them, and the desk composes repairs
from the verdict, never from memory. The lint is a tripwire
over the observed slip space, not the guarantee — the contract
is the literal, and a slip beyond the patterns is desk error.
DEFANG lint is separate and scans the WHOLE file: an undefanged
bracketed tag literal holds the sweep wherever it sits — in
INTENT it is the enforcement of the hand-defang duty.
Write the literal or expect the lint to say so.

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
  bracketed tag literal never appears inside a body — the record
  tool's tag parsing and the closure gate match the bare
  bracketed enum, and an annotated tag breaks both
- a decision still resting on an unverified assumption at [READY]
  gets an appended `[AUTO-ACCEPTED]` line — surfaced to the operator
  by its tag, never silently carried; a reconciliation advanced on
  its recommendation is recorded this way, conflict and
  recommendation in the line body — the operator's answer appends
  the resolving line.

Each investigation/design round appends under a `## Cycle <n>`
heading. The heading marks the round for the record's readers; it
is not a schedule — a round is whatever investigation the design
needed. The FIRST `## ` heading is also load-bearing: it closes
the head region, and above it nothing parses as an entry — a
tracker with no `## ` heading at all parses NO entries, silently.

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
(hypothesis) A SPIKE — a throwaway build grounding a basis no
existing code can answer, greenfield's common case — is a
discovery leg like any other: it builds in the leg's OWN
scratchpad, never the repo, and returns MEASUREMENTS. Its
findings land as F-lines with executed bases; its code is
evidence, never implementation — a unit rebuilds from the locked
design, so the no-design invariant is untouched.
A leg is dispatched TO A DECISION: its brief names the recorded
decision it unblocks and what each possible return would decide —
a leg whose returns cannot change any recorded decision or any
entry's tag is not dispatched (the record gate's mechanical
repair leg is the named carve-out: the decision its return
settles is the gate's own clear-or-hold) (the corpus's discriminating-
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
the design is not done: design until it could be briefed.
(hypothesis) [READY] also asks DECOMPOSITION-COMPLETENESS: is the
head professionally complete — is there a requirement a competent
shop would have derived that is still missing? A cheap self-check
before pricing an attack round; the attack's decomposition mandate
is the load-bearing grader, so nothing rests on this question
beyond the easy catch. [READY] is
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
bases citing invalidated ids, grammar and defang lint — a lint
hold on an appended line repairs by the `corrects line <n>`
token, Implementation's form, the verdict naming each
violation's class and repair form), and its
verdict carries the clause-disposition union the dead-basis read
consumes; the residue the tool NAMES — dead-basis body-reads, the
duplicate-id body-read, restatement adoption checks — is the
judgment slice, still desk work. An open [PENDING]
under a claimed [READY] is
the premature-call shape.
A declared exemption nets a matching hold out of the blocking set
before SWEEP_HOLDS is decided: a labeled `SWEEP_EXEMPT: <code>
lines<=<n> — basis: <citation>` or `SWEEP_EXEMPT: <code> line <n>
— basis: <citation>` line — INTENT:'s and
SKILL:'s sibling, same body-region placement, same field-not-gate
treatment — moves every violation of that CODE at a covered line
into the verdict's `exempt_holds` field (each carrying the
exemption's own declaring line), frozen at declaration — the
coverage clamps at the declaring line itself, so nothing
appended after the declaration is ever netted, whatever `<n>`
says: a violation at any line GREATER than min(`<n>`, the
declaring line) blocks untouched. An exemption is OPERATOR
authority, carried in the mandatory `— basis:` tail (the
operator's line quoted, or the id of the entry
recording their direction) — the tool nets nothing from a
citation-less declaration. A desk never exempts its own gate's
holds on its own judgment,
and an unattended run's unexemptible holds ride the close
instead. What the guard VERIFIES is the exemption's BOUNDS — the
code, the frozen coverage, everything outside it still firing;
the
legitimacy judgment belongs to the cited authorization.
Exemptible holds are FORM DEBT only. Defang-class holds
(`tag-literal-in-body`) are never exemptible —
the tool refuses the netting — because an undefanged tag literal
holds every later sweep correctly, for the run's life (The
record); and LIVE-WORK holds (`pending-latest`) are never
exemptible either: the no-[PENDING] gate holds unread legs open
mechanically, and a netting that reached it would unlock
[READY], the closing [ZERO-DELTA], and the Verify dispatch in
one line. `exempt_holds` is enumerated in the close beside the
[AUTO-ACCEPTED] entries: netted is never invisible.
A FORM-code hold — `superseded-block-form`, `basis-missing`,
`tag-literal-in-body`, `clause-unparsed` — additionally nets against
its own code's MINT VERSION: each carries a rule→version entry in a
table backfilled once from the tool's git history (the SKILL version
served when the code first shipped), and a hold whose LINE was
written under an EARLIER version — the P3 `skill_versions`
attribution, lines between two markers read under the earlier one —
grades RETRO in the verdict's `retro_holds` field, surfaced but never
blocking; the same code at or above the mint's marker still blocks.
Every other code (SUBSTANCE, by omission from the form set) grades
every line whatever its age — the over-forgiveness class this split
never widens, the mint's one confirmable per-code decision. A
marker-less record (no `Skill:` header line at all — pre-P3, out of
this mechanism's scope) earns no forgiveness: the declaration route
(SWEEP_EXEMPT, above) stands there instead. RETRO netting runs
independently of SWEEP_EXEMPT's own netting and the two never
interact — a defang-class hold (`tag-literal-in-body`) is still
RETRO-eligible even though it is never SWEEP_EXEMPT-eligible (H6
binds an OPERATOR declaration, never a computed historical fact).
`retro_holds` is enumerated in the close the same way `exempt_holds`
is. No new
verdict name: SWEEP_CLEAN,
SWEEP_HOLDS, and every downstream gate consult inherit the netted
set with no separate git-tool change.
Record `Status: [READY]` with the impl units enumerated, each
naming its red-first pin — and a pin DISCRIMINATES: red on the
current state, green only through the fix; a criterion the
defective state already satisfies verifies nothing, and a
renumbering that drops a unit's pin clause is a silent unpin (both
observed as a round's highest finding). Each unit is also
classified by the reversibility of its EFFECT, not its diff: one
whose green state includes something git cannot undo — a schema
or data migration, an external write, a publish/push/send, a
deletion outside the write-set — is tagged irreversible BESIDE
its enumeration, as the BARE label line `unit U<k> irreversible:
<effect>` — the label-line class (`SKILL: `'s sibling), standing
alone at column 0, never an entry and never a body opener, so it
re-opens nothing under the closure predicate; the record tool
surfaces the
set as `irreversible_units` in sweep and closure verdicts —
attribution, never a gate: unattended enforcement stays the hold
entry. Every other bound in this skill limits waste; this
one limits damage: unattended an irreversible unit never
dispatches — it takes the hold entry (Implementation) and rides
the close for the operator; attended it dispatches after the
effect is named. (hypothesis) Unit ORDERING is
integration-risk-first: where the design crosses boundaries, the
first unit is a tracer bullet — the thinnest end-to-end slice
wiring every boundary — so integration failures surface in the
first landing, not at verify; horizontal layer-by-layer ordering
is the exception and carries its reason in the enumeration.
(hypothesis) A unit's edit commission is
symbol-anchored — the target named by symbol, with a residue check
proving it gone or changed — never a bare line range (line numbers
may cite, never command): ranges decay
as file and record evolve, and one commissioned range landed
exactly on the guards a prior decision retained, deletable verbatim
by a literalist implementer. UNATTENDED is
the default: the recorded recommendation advances the run — no
prompts, reconciliations surface in the close, the run's one
touchpoint — but [READY] still opens with the desk's own INTENT
re-read: a design satisfying its derived requirements but not
the INTENT is the drift the head exists to catch, and no other
step forces the look (hypothesis). A report is no terminus — a
seam report, a round's graded return, an operator reply, or a
peer-channel answer is delivered mid-stride, in either Mode and
at every seam, the same reply carrying the next owed desk work;
under a live dispatch freeze the QUEUE, not an append, is that
carrier. A turn ends only where the run itself is stopped: a
dispatched leg or round awaiting return with no un-dispatched
desk work owed; a hold or halt the desk cannot clear at this
seam; an operator-owned decision the record cannot answer —
attended Mode's advance prompt and an operator-authority ask
included; a version-mismatch abandonment (The record); a
mandated stop (the operator-authority passage's enumeration); or
the close. The delivered-report-reads-as-done momentum is the
named failure shape. `Mode: attended` in the
header (operator-declared at run start) presents the record and
recommendation at [READY] instead, ENDING with one advance
prompt — "(y) advances per the recommendation"; anything else
is free-form override. Design decisions are never posed as
choices; the prompt carries loop control only. Supervision is
monotone: an operator appearing mid-run takes over on one
recorded line and the run continues attended — adding
supervision never needs justification, and an attended run
never silently becomes unattended
(hypothesis). Advancing locks the design — the LOCK. Its
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
Verdict routes: LOCK_GATE_HOLDS — the consulted sweep verdict's
blocking set is non-empty AND Status is NOT on the close path
(FAILED/COMPLETE): [READY], in-progress, PASSED, a missing or
malformed status — all fail closed,
the consulted record verdict embedded verbatim as the `gate`
field — halts lock-check and lock-commit uncommitted: the record
never locks over its own blocking state ahead of close. Its route
is REPAIR, never a verdict on the run: repair or exempt the
blocking holds, re-sweep, re-lock — the [READY] machinery's
ordinary path. A hold the desk can neither repair (not form
debt) nor, unattended, exempt rides the close instead — FAILED
with the hold enumerated, the ending the exemption clause names
(PASSED is a transient pre-close state
this seam never locks over: Close writes COMPLETE before it
pins). Under
Status FAILED or COMPLETE (the close path, Close) the gate PASSES
instead with the same blocking set still carried in `gate` as
information, never silently dropped — a close-time lock
legitimately carries PENDINGs (an abandoned unit's own hold).
HALT_STATE is the operator's half-finished
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
mis-composed: re-run lock-check, re-record, retry ONCE — the
`--drop` argument is PASTED from the verdict line, never
re-typed (two spellings of one byte deadlocked this handshake,
and the re-typing hop is the desk); a second mismatch OF ANY
KIND halts the lock uncommitted, routed like HALT_STATE, the
two sets surfaced verbatim in the booking. LOCK_COMMITTED's sha
is the LOCK
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
tree serves HEAD) — the artifact path is the `.A<n>.artifact`
species in its OWN namespace, `artifacts/`, beside — never
inside — the seal directory (seal-path prints it; namespace
hygiene: the path handed to the attacker no longer names the
seal directory — what bars a read is the brief's scope, not the
split), OUTSIDE every
repo like the seals and for the seal rule's reason (an in-repo
artifact is an untracked file under a brief asserting tree ==
lock commit; the tool halts ARTIFACT_IN_REPO on any, halts a
symlink tracker — name the real path — and `--out` alone is
cwd-relative: an artifact lives outside the repo, so
repo-root-relative grammar cannot name it) — and BLANKS the two
Superseded species IN PLACE — each dropped line an empty line,
so artifact line numbers EQUAL source line numbers and a
`corrects line <n>` token dereferences identically in either —
while entry-shaped lines inside a Superseded SECTION are
PRESERVED; ENTRIES are never filtered (dead bodies are
load-bearing for closure questions, and a hand-summary is the
paraphrase-drift class). The artifact itself stays PURE —
no header, nothing the source does not carry: source path,
pinned sha, and the blanking declaration travel as
ARTIFACT_WRITTEN verdict fields, and the brief QUOTES that
verdict line beside the artifact; it also
carries the question and the read-only tail (dispatch skill
`references/forms.md`). Unfiltered, the
artifact compounds per round; the desk appends nothing to the record
while any attacker is live — an append landing mid-round leaks
sibling findings into an attacker's own record sweep, and the
round's independence cannot be re-established afterward. The
freeze defers appends, never work: desk findings and leg
dispatches during a round queue at
`~/.local/state/statiker/seals/<repo-key>/<tracker-filename>.A<n>.queue`
(repo-key = `basename` of `git rev-parse --show-toplevel`, a
hyphen, then the first 8 hex of `sha256` of that toplevel's
REAL path — the basename alone collided for two checkouts
sharing a name, a fork beside its origin; derive it in the MAIN
checkout, never a linked worktree, where `--show-toplevel`
answers with the worktree and `--git-common-dir` names the
shared store; the tracker's
filename verbatim with `.md`. XDG state, never `~/.claude/`:
that path shape draws permission dialogs on every access) —
existing whether or not a seal was
written — and at the round's return: LAND the queue's entries,
SPEND the queue, THEN record the A-line — spend-before-A-line,
so a desk dying mid-sequence leaves a spent queue and a missing
A-line (a re-read), never a landed-but-unspent queue (a
re-land into an append-only record). The spend: append
`LANDED <yyyy-mm-dd> — at line <n>`
(the tracker line the landing opened) as its last line —
`LANDED <yyyy-mm-dd> — empty` when nothing was queued, and an
ABSENT queue file reads as empty, legally; a queue
whose last non-blank line matches the spent form is spent — and
a [VOID] A-line is a return for this duty: the queue spends at
any terminal A-line. No
subcommand reads a queue file (the tool's own documented scope):
the spent line's reader is the successor desk at resume (the
resume's queue read, The record), and
that read is what bars re-landing a spent queue. The
freeze's scope is every surface the brief claims immutable: a
brief asserting the tree matches the lock commit (the TREE
CLAIM) freezes the whole
repo, not only the record — the claim sets the scope, and keeping
it true until the attacker returns is desk work. The claim
binds TRACKED state; untracked check by-products sit outside it
under the declared carve-out (Verify — declaration, pre-existence
record, removal at the return). In a batched trip the claim
binds each design's worktree instead: a freshly detached
worktree has every by-product path absent by construction, so
the pre-existence record is trivial and removal IS the worktree
removal — no `.paths` file and no working-repo carve-out for
the trip. The
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
    probe. Attack the design's fit to the recorded requirement
    and the factual bases it cites; attack the DECOMPOSITION —
    is the derived head a faithful AND professionally complete
    reading of the INTENT, where a head carrying a recorded
    deliberate narrowing — an entry naming the scope moved out
    and the carrier it moved to — is graded against the narrowed
    scope, those narrowing entries themselves attackable — and
    the design's SIMPLICITY — the
    simplest design that meets the head; unjustified structure
    is a finding. Attack the BLAST RADIUS — for each surface the
    design changes (a key's scope, a shared file, a value set, a
    schema, a shared resource), who else consumes or shares it,
    established by executed search where the surface exists to
    search, by full source-chain trace while it is still design
    prose; a co-consumer or co-sharer the design was never
    checked against is a finding, and a scope dimension the
    design's key omits is the canonical member.

The brief never carries the desk's reasoning — it transmits the
producer's blind spots — and the rule reaches the ARTIFACT: an
entry authored for the attacker's eyes (a weak-spot list, steering
notes) is desk reasoning riding the never-filtered channel, and it
frames the round it was meant to sharpen. Pre-round self-assessment
is a sealed prediction, written before the round dispatches to
`~/.local/state/statiker/seals/<repo-key>/<tracker-filename>.A<n>.seal`
(repo-key as the queue path derives it, then the tracker's
filename verbatim, `.md`
included) — a path any successor desk re-derives through the git
tool's `seal-path --tracker <path> --round <A<n>|verify>` verdict
(SEAL_PATH: every species' full path — seal, queue, paths,
artifact (its own `artifacts/` namespace), report, comparison —
from the pinned derivation; paste,
never hand-compose; the `report` species is the OPTIONAL
out-of-repo copy of a round's returned report where the desk
keeps one — never round-mandatory, reports travel by
message); out of
the repo because attackers read the repo, and an in-repo seal
breaks any brief asserting tree == lock commit. At the round's
return the desk compares seal against bites and writes the
comparison BESIDE the seal, still out of the repo — later
attackers read the repo, so seals and comparisons enter the
tracker only in the close, where no further round follows. A
seal is calibration, never evidence: it steers no verdict, and a
missing or late one voids its comparison, not the round.
Instrument-seal, widened (P24: the seal grades entries that EXIST,
and an enumeration gap has no entry to seal — F76 was the fourth
instrument in one run to declare a persisted population complete
and be wrong, and no seal caught any of the four): a seal over
CONCLUSIONS cannot reach an omission, a seal over INSTRUMENTS
can — the AXIS three consecutive seal comparisons converged on,
naming it beating guessing the instance twice running. A
successor's seal therefore carries, per instrument touching a
completeness or population claim: (i) a per-instrument REACH
statement — what it structurally CAN return; (ii) a DEFEAT-MODE
enumeration — what would return the same output as a true negative
(F95's own defeat mode: a zero-row table reads exactly like a
column carrying nothing); (iii) the recorded IRREDUCIBLE BLIND
SET — what no available instrument reaches, named rather than
silently absent; (iv) CENSUS-IMMUNE members dispositioned by
reading their WRITER — the write path, never content absence (an
empty store's content is silent; its writer is not). The mint's
form sentence: a successor seals what each instrument cannot
return, what each fixture cannot express, and which repairs shipped
unexercised.
Attack tier: a ROLE, resolved in order — `clippy.config/models`
(`attack:` class) when present, else the first entry of the
skill's shipped `defaults/models` (under this skill's base
directory: the certified-attack register, every entry carrying
its probe-then-certify provenance inline) the harness can
dispatch, else the strongest model available to the harness as
a fresh context. Certification comes from the PLAN.md
probe-then-certify step, recorded in the register or the
stack's own config/ledger; a tier resolved without one — the
terminal fallback by construction — attacks as a DECLARED
deviation in the tracker, never silently: the resolution
order's flexibility carries the certification duty. Escalate a
round above the resolved tier only on operator call. Rounds are
sequential PER DESIGN, one attacker per TRIP — that
design's A-line recorded before its next round dispatches. One
trip may carry every locked design awaiting attack in the stack
(one stack per trip: tier resolution, the evidence-source cite,
and deviation lines are per-stack). Each design keeps its whole
round machinery — its own pinned artifact, its own A-lines in its
own tracker, its own seal and queue (both key per tracker) — and
the return carries a complete per-design verdict block: findings,
or that design's explicit zero-delta. The desk provisions one
worktree per design through the git tool — `worktree-add --sha
<lock sha> --path <path>`, the path OUTSIDE every repo like the
seals and for the seal rule's reason — and removes each at the
return with
`worktree-remove --path <path>` (forced removal: probe
by-products make plain removal fail by design); WORKTREE_ADDED
and WORKTREE_REMOVED proceed, a halt at add stops that design's
dispatch, a halt at remove is booked as a `record:` F-line from
the verdict line, and either way sibling designs run on.
The tree claim binds the design's
worktree, so every claim holds at once whatever repo the designs
share, attackers execute in their worktrees only, and the working
repo needs no by-product carve-out for the trip. The append
freeze covers every participating tracker until the trip returns.
The brief states the design order — the desk's call, keying the
verdict blocks; frame carryover from earlier designs to later
ones inside one trip is accepted, priced by the per-design
blocks, and is not the resumed-attacker case, which re-reads its
OWN prior round. Death is per design: a queued finding killing
one design aborts that design's member alone ([VOID] abort:), a
premise broken for one design ([VOID] premise:) voids that design
alone, and a design whose verdict block is missing stays
[DISPATCHED] and re-enters as its own round — sibling designs
grade normally in every case. A single locked design keeps the
single-design shape. Each
re-attack is a NEW fresh context (a resumed attacker inherits
its own prior findings' frame), and a re-derived design is a NEW
locked design — it gets the attack again, its repairs landing as
ONE re-lock: per-finding re-locks split the priced unit
(hypothesis). The reply opening a repeat round — from the SECOND
repeat round
on — cites the record
tool's `trend` output as its arithmetic backstop and GRADES the
series by a BODY-READ of the rounds' findings — `trend`'s raw
per-round counts (the trajectory arithmetic) read every F-line
regardless of class or locus, while its concentration flag DOES
read the citing entry's class (a `record:`-scoped citation never
concentrates); the grade still never comes from the verdict alone,
since the counts half stays class-blind. The grade computes only from
the SECOND repeat round on: with fewer than two completed [BIT]
rounds behind it there is no series, and the first repeat round
is the ordinary re-lock path, never graded. CONTRACTING:
substance
findings fall round over round AND land mostly on ground the
previous round already bit. NON-CONTRACTING: everything else
(the founding shape: the loop
eating its own repairs — nine rounds, none zero-delta, each
round's findings concentrated on the newest cycle's own work).
A non-contracting grade routes to NARROWING, never to another
same-form round:
re-scope the head to the smallest independently shippable unit
(an R-amendment, the displaced scope EXPORTED per The loop's
exit machinery to a BACKLOG ENTRY carrying the successor-run
intent — the named carrier with its reference; successor runs
seed from this record, the
parent's settled entries citable evidence there, attackable like
any basis; a narrowing touches INTENT's reach, so it rides the
close as a reconciliation), drive the narrowed design to its
zero-delta, land
it. Where the head already IS that smallest unit, narrowing has
no move: the series goes to the operator — attended the prompt;
unattended the run closes FAILED with the series enumerated in
the close (budget exhaustion's own disposition) — never another
same-form round.
The budget (the header) backstops this judgment
mechanically; it is never the route. A round dies two ways, one
clause (hypothesis):
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
as desk findings the desk re-derives itself. Each design's round
records its A-line (The record). At a round's return every finding is
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
brackets and case: the record tool's tag-literal lint carries
the brackets (its own greps, battery-pinned — the netting
battery produces a real violation of the class), the brackets
the load-bearing half, the case change margin. Regraded
into F-lines in the same sitting. Any substance finding: the
round records [BIT] — that record change IS the reopen, and the
reopen's SCOPE is the entries the findings cite plus their
dependents through the invalidation machinery (The loop's
dependency rule): entries no finding reaches stay SETTLED,
re-read only where a repaired entry's dependency reaches them,
never restated wholesale — whole-record re-derivation is the
anti-pattern with a measured signature: every restatement is
fresh attack surface, and the next round's findings land on the
newest cycle's own repairs. A
substance-free
return: execute the record repairs now (desk work), then record
[ZERO-DELTA] as the last A-line — recordable only with every
verdict reach-matched, measured by the attacker or completed by
the desk, and no [PENDING] tag riding the round's own appends.
That closes design; record findings never sustain a
next round (declining max-severity is convergence; observed
sustaining rounds past it). Mechanically enforced at the RE-ENTRY
seam (F143: the prose held IN FORCE while UNAPPLIED — A8's four
record/instrument-class findings sustained a ninth round this
clause forbids): before a design's next round dispatches,
`sustain --tracker <path>` re-derives the PRIOR round's finding
classes from each finding's own scope opener, independent of the
round's A-line summary — SUSTAIN_OK when at least one
finding is design-substance (never `record:`-scoped),
SUSTAIN_DENIED when every finding is record/instrument-class,
SUSTAIN_NOT_APPLICABLE outside a [BIT] round. `sustain` reads only
the LATEST RESOLVED round (BIT/ZERO-DELTA); a live [DISPATCHED]
round is not consulted — its id surfaces as the verdict's own
`live_round` field so the state stays visible rather than silently
skipped. The verdict is quoted in the round-open line; a round
dispatched over SUSTAIN_DENIED is exactly the class this gate
exists to catch. The same round-open seam also runs
`tripwire --tracker <path>` (The record, Budget) beside `sustain` —
its verdict quoted the same way; an armed TRIPWIRE_FIRES routes to
the 0.68 NARROWING route (below), never blocking round-open on its
own tag, and TRIPWIRE_SILENT with reason "unarmed" is silently
informational, never a hold — the breaker fires only where the
header names its threshold.
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
consequence (Implementation: the commit gate halts every
in-flight sibling too, fail-closed — the rest re-dispatch after
re-entry; carve-out parked as tool work).
The desk refutes a finding only with its own reach-matched evidence
(the F-line goes [INVALIDATED]); closure still needs the next
round's [ZERO-DELTA]. A design claim a round REFUTED (its D-line
[INVALIDATED] under that finding) re-enters the design only on a
basis of a DIFFERENT KIND than the refuted one — the re-entering
entry names the new kind and why it is immune to the prior failure
mode (P24 clause (b): the corpus's derive-the-basis rule, applied at
the re-derivation seam where momentum re-asserts the cheap basis
that already failed once).
A run instrument the desk builds is unproven until it has gone
RED on a real defect; until then its clean verdict closes no
gate. An instrument's REACH enters the record as its own
printed reach line, never the desk's paraphrase of it.

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
entry-shaped line broke the grammar, and the entry set the
closure computes is unsound until repaired. Repair is
APPEND-ONLY, by the literal token `corrects line <n>` — one
token per line — and is COMPOSED FROM THE VERDICT, never from
memory: the verdict names each violation's class and the
repair form it takes. The split is settled in the executable
spec (The tools); its principles: a violation ON A MACHINE
TOKEN indicts the semantics every gate reads, so the target is
superseded whole and the correcting line RESTATES the content,
re-carrying whatever PARSED on the target — tag and scope
both; a tag or scope change through repair lints as its own
violation, and status changes are ordinary new lines, never
smuggled through repair. A violation in free BODY CONTENT
leaves gate-read semantics sound, so the target keeps its live
entry: the correcting line is bookkeeping (body opens
`record: `, then the token) and sheds the target's VIOLATIONS,
nothing more — shedding acknowledges, never cleanses, so the
target's tag, scope, and voiding effect stand. Supersession is
ONE-PASS: a superseded correcting line's own supersession
persists, so its restatement carries only its OWN token, never
a re-carry. The token is a repair, never an eraser of live
entries: naming a violation-free line lints `corrects-nothing`;
a target readably naming ANOTHER id is barred, while an
id-unreadable violated line is claimable by the correcting
line's id — the misspelling class the token was built for.
Flagged text still sits in the file for foreign readers (the
stats reader's unanchored greps) — the compose-time rules are
the only cleanse. Then
re-run;
CLOSURE_ABSENT means the gate is not open — the last A-line is
neither [ZERO-DELTA] nor a [BIT] whose disposition set amends no
design entry (P27: design CONSEQUENCE, not finding PRESENCE — a
terminal [BIT] round's own findings may all discharge without
touching a single D-line, and the gate reads that as SATISFIED, the
same predicate as ZERO-DELTA from there; one design-amending
disposition — a SCOPELESS D-class line landing after the [BIT]
A-line (a `record:`-opened D-line is bookkeeping, never amending; a
`unit U<k>`-scoped D-line, the `held:` form included, is a PER-UNIT
concern the ordinary unit-held machinery below already reads,
identically to ZERO-DELTA) — keeps it SHUT, the over-correction
case; F118: the presence-reading gate forced an operator deviation
to ship a unit whose round's five findings none amended the
design). Absent either, this is the
normal state during a reopened design; dispatch waits. UNIT_HELD
bars that unit on its
unresolved hold entry; UNIT_UNKNOWN halts on an id no live
record line scopes — re-run with the id read from the record,
never a guess (a typo'd digit otherwise clears a hold
silently); UNIT_DISPATCHABLE lists the live
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
land, re-enter ONCE). A unit's write-set is
declared in the record — `- F<n> [VERIFIED] unit U<k>
write-set: <path> — basis: <the unit enumeration>`, one
REPO-ROOT-RELATIVE path per line, latest-line-per-id — appended
at the [READY]
enumeration. Units with disjoint
write-sets run parallel (one shared index — commits
serialize; the tool's capped retry absorbs the
contention); disjointness is computed, never eyeballed — the
parallel decision cites the record tool's `waves` partition,
whose comparison is lexical over that grammar (the verdict
reports raw spellings beside the normalized paths; an alias
outside the grammar — an absolute or symlinked spelling — is a
declaration defect, the desk's to catch at composition). A missing
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
one dies → premise-killing. Stop the siblings resting on it;
the commit gate's consult halts EVERY in-flight sibling on the
voided closure, fail-closed — clean siblings' edits stay in
their trees, named as the re-dispatch's write-set, and land
after the ONE re-entry with every return in hand (a
start-sha-predates-the-void carve-out is parked tool work,
never improvised at the desk). Model per
`clippy.config/models` (`impl:` class) when present, else the
operator corpus routing table, else — no corpus on the stack — a
cheaper tier than the desk, the same terminal default discovery
legs take; an unreadable models file halts
the dispatch, the parse error a unit-scoped F-line (body OPENS
`unit U<k>` — the criterion's scope form). Each unit
commits green; the desk appends its landing as an INDENTED
annotation line (`  unit U<k> landed: <sha>`, preceded by a
blank line — markdown otherwise folds it into the entry above) —
not an entry, so
invisible to the record tool's tag-first entry parse and the closure
read by construction — that is what makes resume reliable.
Unit briefs carry the git tool's invocation lines with the
script's absolute path (The tools) — desk prose reaches no
unit, and no procedure text is expanded into a brief.
Composition-side, the desk checks the write-set: paths name
FILES and are `git check-ignore`-clean — a composition error
caught before dispatch (the tool re-checks and halts, the
backstop) — and every `unit U<k>` id it appends against the
[READY] enumeration: a mistyped id in a RECORD line voids
nothing and reaches no brief, and no tool can know which unit
was meant (the argument-side validation catches only the
`--unit` flag). The unit runs: START, before any edit —
`unit-start --tracker <tracker> --unit U<k>` — the write-set is
read from the record's declared lines through the gate consult
(the record tool's `closure --unit`, run as a subprocess, its
verdict embedded verbatim as the `gate` field — closure, never
sweep, is the unit gate's consult), so briefs never restate it,
and UNIT_START_CLEAN prints the resolved `write_set`, which is
where the implementer reads the paths the unit owns;
UNIT_GATE_BLOCKED (a blocking record-gate verdict, the empty
declaration included) and WRITE_SET_NAMES_TRACKER (the declared
write-set names the tracker itself) halt the unit UNBUILT, and
GATE_UNREADABLE (no parseable record verdict) halts the same
way, fail-closed. UNIT_START_CLEAN makes
every later modification the unit's own; UNIT_COLLISION (an
operator edit or draft on a write-set path the unit would
otherwise overwrite and commit), HALT_STATE (the
operator's half-finished operation, tree untouched), and any
other START verdict (HALT_IGNORED_WRITESET,
HALT_DIRECTORY_PATH, USAGE_ERROR, GIT_ERROR …) halt the
unit UNBUILT — no edit, no commit, no landing annotation.
COMMIT — `unit-commit --tracker <tracker> --unit U<k>
--start-sha <the START verdict's start_sha, PASTED from the
verdict line, never re-typed (the drop-argument rule's hop)>
-m <msg>` — same
gate consult and halts as START — with the COMMIT-side
disposition: a halt here leaves the unit's edits in the tree, so
they are NAMED as poisoning the write-set for the re-dispatch —
plus UNIT_START_MISMATCH: the
start sha is no ancestor of HEAD, or a foreign commit touched
the declared write-set since it.
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
against the tracker's requirement head as amended by its R-lines
plus every late `INTENT: ` line the sweep verdict lists (The
record), and pastes the checks' own
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
`~/.local/state/statiker/seals/<repo-key>/<tracker-filename>.<round>.paths`
(`<round>` = the A<n> id for attack rounds; a verify leg
writes `.verify.paths`, REWRITTEN at each verify dispatch —
at most one is in flight, so no count is derived),
re-derivable by any successor desk (The attack's derivation)
— never carried only in the brief or in memory. The dispatch also
records the copy's HEAD sha at leg read-start — a `record:` F-line
("verify leg reads at <sha>"), so a resume can re-run the gate
against it: the desk is an
UNFROZEN concurrent writer during verify, unlike the attack rounds'
append freeze (P30, F121/F124 — the unit transaction's own collision
check was once replaced by exactly the condition this breaks, "this
desk is the only writer in this copy", then broken by a mid-leg desk
commit). At the
return, after any queued appends (attack
rounds, The attack) and record repairs land and before the
outcome line, the desk removes exactly the declared paths the
`.paths` record lists ABSENT that now exist; everything else —
pre-existing (operator state), undeclared, or uncertain — is
LEFT, the leftover a finding, never a broader clean. Removal
consumes the file — delete it once removal has run; a `.paths`
file with no live round is litter. Single-design attack rounds
carry the same carve-out for the repo checks their probes
execute; a batched trip's attackers execute in their worktrees,
which need none (The attack); an attacker's own probe scratch
belongs in its
scratchpad (the read-only tail's provision), never the repo. Model per
`clippy.config/models` (`verify:` class) when present, else the
parent model; an unreadable models file halts the dispatch, the
parse error recorded as a finding. Before the V-line,
`verify-gate --tracker <path> --sha <the recorded read-start sha>`
checks the copy against that recorded sha: VERIFY_COPY_CLEAN
proceeds; VERIFY_COPY_STALE names every commit and touched path
landed during the leg — the desk's read, never the leg's claim — and
the V-line's basis states STALE-COPY plus the desk's disposition:
harmless (none of the touched paths graded by the leg) carries the
named delta, or the leg re-runs isolated against the new HEAD. The
check is computable; the disposition stays desk judgment. Append the
V-line (The record) with the evidence and set the header
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
unattended this is the run's one touchpoint: the verdict with
its evidence pointer; every open reconciliation; every R-line
amendment (what shipped vs. the letter as asked); every
[AUTO-ACCEPTED] entry; every SWEEP_EXEMPT declaration, with any
holds it still nets (`exempt_holds` from a `sweep` run at
close-compose — the close's own read, not a stale seam's; a
declaration whose holds were since repaired is enumerated too);
every RETRO-graded hold (`retro_holds`, the same close-compose
`sweep` read — P5, Stop rule);
every
entry whose latest line is
[PENDING] (a FAILED or abandoned run can carry them);
deviations and gaps; what was NOT verified; candidate
lessons. The close ENUMERATES BY REFERENCE — id plus a prose
summary, never a copied tag-first line: a copied line is a new
entry, and a copied scopeless body voids; report material
enters as quote blocks, the tool's production. Landed seals
and their comparisons
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

A finding entry may carry an OUT-OF-SCOPE grade at booking — the
body opens `out-of-scope: <claim>` (classify_scope's third scope
class, sibling to `unit U<k> `/`record:`: exempt from the
post-closure scopeless-VOID rule, Implementation, since the grade is
a leavings concern, never a design re-derivation trigger) — for a
true finding outside the run's requirement head, found in passing.
`closure` enumerates every out-of-scope-graded id and HOLDS
(CLOSURE_LEAVINGS_HOLD, blocking both the whole-record query and any
`--unit` query) until each carries a DISPOSITION on its latest
line: an export ref — `— exported: <ref>`, citing a decision-graded
backlog entry in the target repo that cites this run's record, the
unit-draft shape run 1's five exports already used, seedable by a
successor run — or a one-line recorded drop — `— dropped: <reason>`.
The printed closure verdict names the undispositioned set; the desk
composes the disposition as an ordinary new tag-first line for the
same id (append-only, latest-line-wins), never an edit of the
booking line. The disposition line RE-CARRIES its `out-of-scope: `
opener (or opens `record: ` where the disposition is itself desk
bookkeeping) — the natural phrasing that drops it (a bare
`— exported: <ref>` or `— dropped: <reason>` opening the body) reads
scopeless and voids the WHOLE closure, the same trap the cleared-hold
line's own warning names (Implementation).
The close REPORT itself carries a LEAVINGS section enumerating three
classes: (1) out-of-scope findings — the mechanical gate above, the
one class that is a run artifact proper; (2) instruments and probes
built in-run and used more than once; (3) world-facts a successor
would otherwise re-derive (population maps, environment overrides,
frame-anchoring) — each with its executed basis. Every enumerated
item carries a DISPOSITION slot the desk fills per the HOST repo's
own conventions (corpus-governed where present, operator-decided
otherwise); the skill mandates the enumeration and the filled slot,
never the destination — statiker owns the run and its record,
SURFACING is run-conduct, FILING is the environment's. Each exported
successor entry CITES the parent close report's leavings section by
anchor, and at requirement-head composition a fresh run reads its
task source's cited leavings section — where the task source is such
an exported entry — before the head is composed: the inheritance
interface is one digest section, not the full record, and the
adoption path (The record) remains the trust protocol for anything
the new run rests on. Skill-evolution and repo-memory channels are
deliberately environmental — this record chain (close-report digest
→ seed entries → adoption path) is statiker's complete built-in
inheritance for a standalone user.

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
stabilization TARGET, not the live count: this phase accretes
fire-born structure above it deliberately, and the compression
pass owed at stabilization (booked in dev-notes) brings it back
down. A patch landed without provenance is still the tripwire.

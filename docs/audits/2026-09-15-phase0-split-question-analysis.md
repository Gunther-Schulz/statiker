# Phase 0 — the skill-structure split question: analysis and numbered proposal

Author: statiker-4b (opus, executing desk), 2026-09-15, under the
operator's first-hand delegation of this date naming statiker-9c as
the driving desk. Directive:
`docs/directives/2026-09-15-split-question-lapC-release-handoff-statiker-4b.md`.

**Object — pinned, not live.** `plugin/skills/statiker/SKILL.md` at
`cfed148` (= origin/main at analysis time, tree clean). 1793
operational lines / 1891 total by the CLAUDE.md Verify awk
[measured]. Every line number below is a line number in THAT file.

The question (operator, 2026-09-15): does the monolithic SKILL.md
split into an always-loaded core plus consuming-seam reference
files, the goal being better lazy loading?

Observation and inference are marked throughout: [measured] on an
executed command's output, [derived] on a reading, [recalled] on
anything from memory. Nothing here is [recalled].

---

## Lead

**Recommend NO on the architectural split, and NO on the one class
that survives the mechanical test — on a finding neither the
directive nor I anticipated: the pieces that fail LOUD when
unloaded and the pieces reached by only SOME branches are DISJOINT
sets on this page.** Progressive disclosure needs a piece to be
both. Statiker has none. The operator's loading-economics goal is
real and is better served by the MOVE-TO-A-LEVER exit this repo
already recorded (PLAN.md, 2026-09-13), which reduces the page
without ever putting a rule behind a pointer a desk may not follow.

---

## 1. What the page IS — measured, not characterised

Section mass by the Verify awk's own counting rule (non-blank lines
per `## ` section) [measured]:

| section | nb |
|---|---|
| Composition | 23 |
| The tools | 175 |
| The record (FP1) | 402 |
| The loop | 71 |
| Stop rule (FP2) | 248 |
| The attack (FP3) | 323 |
| Implementation (FP4) | 285 |
| Verify (FP5) | 128 |
| Close | 93 |
| Fire-born / Birth-class | 21 |

The lap-B stage-1 clause table's structural finding holds at this
sha [derived, from a full read of the page against that table]: the
mass is predicates, write-side templates and seam conduct. Nothing
on this page is inert reference in the sense progressive disclosure
assumes.

## 2. The three tests, and what each returned

### 2a. The fail-loud test (this repo's self-containment criterion)

statiker-9c's phase-0 framing, held: a piece whose absence is
SILENT stays in-page whatever its mass. The mechanism that could
make an absence loud is the record tool's lint. Its registry
carries 39 hold codes [measured:
`grep -oE '"[a-z][a-z0-9-]+-[a-z0-9-]+"' scripts/statiker_record.py | sort -u`].

Probed against the real tool, in a throwaway repo, both controls
drawn from the page's own forms rather than constructed
[measured]:

- **Positive control** — entries written WITH the templates in
  hand: `LINT_CLEAN`, route `proceed`.
- **Negative control** — the same entries composed FROM MEMORY
  without them: `LINT_VIOLATIONS`, 4 violations — `tag-enum` ×3,
  `basis-missing` ×1 — each carrying its own repair form.
- **Near-miss family**, four mistyped write-side forms in one
  fixture: `write-set-near-miss`, `hold-form`,
  `tripwire-arm-near-miss`, `intent-near-miss` — 4 of 4 fired.

First attempt at this pair returned `PATH_OUTSIDE_REPO` on BOTH
arms — the instrument did not run, and that identical pair is
evidence about the invocation, not about the tool. Recorded because
a refusal booked as a result is how could-not-verify renders as
verified. The corrected invocation (tracker inside a git repo, the
record tool anchoring at the tracker's own directory) is what the
numbers above come from.

One variant did NOT fire a code: a mistyped `SWEEP_EXEMPT:` with
spaced `<=`. Consistent with the page's own sentence ("a mistyped
`SWEEP_EXEMPT:` fails safe — the hold it meant to net still
blocks") and with the absence of a matching code in the registry
[measured]; that the desk then SEES the unnetted hold is [derived]
from the page, not probed — the netting path was not exercised.

**Result.** The loud class is exactly the WRITE-SIDE FORMS.
Everything else has no code at all: no check reads a composed
attack brief, no check grades a desk's disposition of a halt, no
check runs the lock's judgment instrument (the page says so
itself — "the judgment instrument the tool cannot run", :919).

### 2b. The branching test (skill-craft's own criterion)

skill-craft: *inline what every branch of the skill's use needs;
disclose what only some branches reach.*

- The **write-side forms** (169 nb: entry templates :611-654,
  machine-token literals and near-miss and declarator repair
  :542-609, SWEEP_EXEMPT and RETRO :780-832, the drop template
  :956-963) are consulted on EVERY entry the desk writes, from the
  requirement head to the close. Every branch.
- The **branch-specific** material is Implementation (:1347-1636,
  286 nb), Verify (:1637-1768, 129 nb), Close (:1769-1865, 94 nb)
  — 509 nb, 28% of the page, untouched during investigate-design
  and never reached at all by a run that closes FAILED, narrows,
  or seeds as a decomposition — plus the attack question block
  (:1081-1106, 26 nb), reached once per round.

**The finding.** These two sets do not intersect. The 169 nb that
would fail loud is the mass reached in every branch; the 509+26 nb
reached in only some branches is precisely the mass whose absence
nothing catches. An Implementation reference that a desk does not
load at the implement seam produces a held unit invisible to every
gate — the page states that consequence in its own words (:1604,
"without it a held unit reaches Verify invisible to every gate").
That is the silent-loss shape the criterion forbids.

### 2c. The coupling test

62 cross-section pointers stand in the page text across 9
operational sections [measured, regex over section bodies]; every
forcing point points into four to six others (Stop rule → 12, The
attack → 11, The tools → 9, Implementation → 9). A split converts
each of those from an intra-page reference a loaded reader
resolves by scrolling into a cross-file reference a reader resolves
only by deciding to open a file.

## 3. What a split would actually save

Deferral is not avoidance: a reference file read at its seam stays
in the session prefix for the rest of the run, so the saving is
(turns before the seam) × (piece mass), never the piece mass
itself. Every forcing point is traversed in a full run.

The multiplier is UNMEASURED and I did not measure it — it needs a
live run's turn count against its seam positions, and run 3 is
parked. Named as the missing evidence rather than estimated. What
WOULD decide it: the turn index at which Phase flips to implement,
over a completed run, against the 509 nb of post-lock material.
If that multiplier turned out large, item 4's lever route captures
the same saving without the silence, so the measurement changes
the size of the prize, not the recommendation.

## 4. The design my basis does NOT rule out — the lever exit

The uncompromised option, named because a round where every choice
carries a regret has shipped an unverified "nothing better exists":
**the page shrinks because its rules became mechanisms, not because
they moved behind a pointer.** This repo already recorded that as a
third exit beside cut and keep (PLAN.md, 2026-09-13: MOVE TO A
LEVER — "text whose absence would bill human minutes but whose work
a tool can do or prove leaves the page without the guarantee
leaving with it"), and it is the one purchase mechanism the pstack
comparison found importable — the other two being executor-trust
(begs the trial's question) and an assumed repo with hard gates
(nothing to import), per PLAN.md 2026-09-13 (iii).

Concrete candidates, each turning a currently-silent absence into a
loud one, none designed here:

- a brief-composition check over the attack brief (does it carry
  the reach-matched-evidence block verbatim) — would make the one
  genuinely branch-specific, currently-silent 26 nb piece
  extractable, converting it from prose the desk must remember to
  paste into a form a tool verifies;
- the tool's verdict `repair` strings already carry write-side
  form guidance to the desk at the moment of use [measured — the
  negative control's verdict carried a full repair sentence per
  violation]. That is a lever ALREADY half-built: the page's form
  text and the tool's repair text are two homes for one fact.

Recommendation: book this, do not build it in this arc — it is
design work with no consuming seam before the release, and the
release is this arc's seam.

## 5. A candidate I tested and killed

Hypothesis: a meaningful share of the mass is provenance riding
inside operational sentences (skill-craft's HISTORY-HEDGE costume),
extractable to journal and git without any split.

Measured: 32 of 1792 non-blank lines carry any provenance or
history token (`st-<n>`, `(hypothesis)`, a dev-notes/PLAN.md
pointer, a run-finding id) — **1.8%**. The hypothesis does not
survive its own measurement, and the page's mass is genuinely
operational. Recorded rather than dropped, because it is the
cheapest thing a later reader would otherwise re-propose.

## 6. Self-containment, per piece (directive deliverable)

The bare-machine question has a different answer here than the
directive's framing assumes, and the difference matters. A
reference file under this skill's base directory SHIPS IN THE
PAYLOAD (skill-craft, Architecture: reference files are
skill-local). On a bare machine with the plugin installed, the file
is present. So the risk is NOT absence-on-a-bare-machine; it is
NON-LOAD AT THE SEAM, which is silent for every piece in §2b's
branch-specific set.

The precedent the repo already carries does not transfer: this
skill ships `references/evidence.md` (70 lines) and
`references/dispatch-forms.md` (137 lines) [measured], and the page
calls the latter's absence SILENT in its own text (:34). Both are
SUBSTITUTES for an EXTERNAL dependency that may not exist on the
stack (the operator corpus; the dispatch skill) — content that is
otherwise not present at all. Neither is an extraction of the
page's own binding text, and reading them as precedent for one
would be this corpus's transfer-test failure: a true rule carried
outside the domain that made it true.

## 7. Red-first form, if the decision goes the other way

Recorded so the driving desk is not choosing between a
recommendation and an unspecified alternative:

1. **Byte-equivalence of the recomposed content.** Concatenating
   the core and every extracted piece in page order reproduces the
   pre-split operational text byte-for-byte, asserted by a check
   that goes RED first — run it against a deliberately dropped
   clause and show the red before the move lands.
2. **The prune gate's clause enumeration** (skill-craft): a context
   that did not perform the move dispositions every clause of the
   before-text KEPT / REWORDED / ABSENT / WEAKENED. A move is not a
   prune, but the instrument that catches a dropped obligation is
   the same one, and ABSENT or WEAKENED on a load-bearing clause
   blocks.
3. **A pointer-reach probe per extracted piece**: the piece's
   pointer wording is the variance bug, not its content
   (skill-craft, Context pointers). Nothing in this repo currently
   measures whether a desk follows a pointer at a seam, and that
   absence is itself a reason to prefer item 4's route.

## 8. Two corrections to the arc's inputs

- **The directive's pointer.** It names "the stage-1 clause table
  (via st-33's pointers, OBSERVATIONS.md:4438-4448 neighborhood)".
  That neighborhood is the 2026-08-10 size-target re-derivation
  booking ("the number is an outcome, not a gate") — which is what
  st-33 correctly cites it for. The stage-1 clause table is
  `docs/audits/2026-09-12-st32-lapB-clause-dispositions.md`, with
  lap A's at `docs/directives/2026-09-11-st29-lapA-clause-table.md`
  and the ledger line making it lap C's input at LEDGER.md:47
  [measured]. Both were read for this analysis.
- **st-33's residue number is stale as a target.** Its
  amended-evidence pins 1706 operational lines measured at the
  0.2.89 release gate. At `cfed148` the page measures **1793**
  [measured, the CLAUDE.md Verify awk]. Lap C re-derives at its own
  seam, which the item already demands; flagged so the 1706 is not
  carried forward as the number to quote.

---

## The numbered proposal

**Q1. Does SKILL.md split into an always-loaded core plus
consuming-seam reference files?**
RECOMMEND **NO**. Basis: §2b — the fail-loud set and the
branch-specific set are disjoint, so no piece satisfies both
conditions a disclosed reference needs; §2a — 39 lint codes cover
the write-side forms and nothing else; §2c — 62 cross-section
pointers become cross-file pointers.

**Q2. Does the one mechanically-covered class — the write-side
record forms, 169 nb — extract anyway, since its absence IS loud?**
RECOMMEND **NO**. It is the piece reached by every branch, from the
requirement head to the close; disclosing it inverts skill-craft's
ladder. The loud-absence property makes it SAFE to extract and the
branching test makes it POINTLESS — it would be loaded immediately
in every run, paying a tool call to move 9.4% of the page one
indirection away.

**Q3. What answers the operator's loading-economics goal instead?**
RECOMMEND booking the **MOVE-TO-A-LEVER** route (§4) as its own
item, NOT built in this arc: no consuming seam before the release,
and the release is this arc's seam (the repo's own
maintenance-arcs-open-against-a-named-consumer rule). Candidates
named in §4; the design stays open.

**Q4. PLAN.md records the re-opening whatever the outcome
(directive).**
RECOMMEND an append-only entry under "Single-home by design"
recording: the operator re-opened it 2026-09-15 on loading
economics — evidence of a kind the original decision never
weighed — and it was re-affirmed on the disjointness finding,
not on the original drift rationale. That keeps the decision's
history honest and stops a later session re-opening it on the
same argument. This is a phase-1 write and waits for the decision.

**Q5. Does anything here change lap C's scope?**
Recommend **no scope change**, one addition: lap C's PLAN.md
Size-target supersession entry should quote **1793** measured at
its own seam, not 1706 (§8).

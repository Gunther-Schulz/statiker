# Second scoped codex-only run — PRE-REGISTRATION (run 2)

statiker-7e, 2026-09-14. Recorded BEFORE any arm dispatches, per the
repo convention that comparison experiments pre-register.

STATUS — GRADED, HOLDING AT THE FREEZE GATE. The numbered round in §12
was graded by the judgment desk (statiker-e8) on 2026-09-14 under the
operator's delegation of that date. Items 1, 2, 3, 4, 6 and 7 are
SETTLED as recommended. Item 5 (the containment authorization) went to
the operator first-hand and is OUTSTANDING. One finding and two
corrections landed before this revision: the grading packet now exists
as its own file (§3b), and §8's authorization text carries a concrete
clone path and a rescoped push clause.

NOTHING DISPATCHES from this file. The operator's GO of 2026-09-13
(LEDGER: "a SMALL SCOPED trial run once statiker is pure-codex READY")
covers the SCOPE of such a run, never this arrangement and never a
dispatch; the run's own first-hand authorization is a separate act and
is NOT held. The next thing that happens here is the freeze gate, and
it waits on that authorization.

Predecessor: `dev-notes/scoped-run-preregistration-2026-09-13.md`
(run 1, statiker-c8/statiker-1f, graded and ratified 2026-09-14).
Its §§14-18 are the inputs this file is built from and they are cited
rather than restated.

CONVENTION FOR THIS FILE: every premise is marked EXECUTED (with the
command or read that established it) or PENDING (with the step that
will establish it and WHEN). An unmarked sentence is a defect. This is
run 1's own lesson applied to its successor — its two measurement
failures were both brief sentences never executed against the world
they describe (§16).

---

## 1. WHAT RUN 1 SETTLED, AND WHAT IT DID NOT

Read off the ratified grading (run 1 §17), not recalled.

| column | run 1 outcome | why |
|---|---|---|
| 1 — stop-rule placement | COULD-NOT-VERIFY | the measuring event never occurred: NO arm declared [READY] |
| 2a — the decision | measured on an ARM-PAIR only | arm 3 stopped before design lock, arrangement-caused |
| 2b — the population | SATURATED, gate fired | the brief itself instructs the behaviour under test |
| 3 — verdict-contract conduct | ALL THREE PASS, thin | arms 2 and 3 passed on halt conduct only; n=1 per tier |
| 4 — record discipline | terra DEVIATION, astra PASS | mechanism vs hand-imitation; the run's sharpest tier datum |

NO desk-role certification is readable for terra or astra from run 1.

**The three causes of arm death, and their status now** — this is the
fact that decides whether run 2 is worth running at all:

1. ARM 1 was barred by `CLOSURE_ABSENT` — statiker defect st-63.
   **FIXED in 0.2.99** (`latest_by_id` supersession, 33913d8 + the page
   half 676a6eb + 9c1766d). EXECUTED basis: the arc close-out records
   the real archived lc-61 tracker returning `UNIT_DISPATCHABLE` at
   HEAD where it returned `CLOSURE_ABSENT` before
   (`docs/audits/2026-09-14-arc-closeout-statiker-1f.md` §1).
2. ARM 3 halted at attack preparation on the unsatisfiable containment
   sentence — run 1 §16, booked as **st-64**, NOT fixed. §8 below is
   this run's repair, and it is an ARRANGEMENT repair, not a payload
   one.
3. ARM 2 died at the record gate.

So the specific bar that made run 1's ceiling unmeasurable is gone, and
the specific bar that killed arm 3 is repairable in the arrangement
without touching the payload. That is the case for running at all.

**The case AGAINST, stated because it is real and the corpus's
re-entry rule demands it be named before a repeat round.** Run 1 spent
three arms and produced zero certifications, and BOTH measurement
failures were the arrangement's own defects rather than model results.
A series whose corrections concentrate in its own arrangement indicts
the FORM and routes to NARROWING, never to another same-form round.
§4 takes that route: run 2 is NOT run 1 repeated. It is narrowed to the
smallest unit that ships one (role, tier) datum, with the rest held on
a named release event.

---

## 2. THE REGISTRATION RULE RUN 1 PRODUCED

Stated as a rule because it is the generalizable half of run 1's
column-2b failure, and because it has to be applied to every column
BEFORE the arms, which is the one thing run 1 did not do:

> A column is measurable only if THE BRIEF does not instruct the
> behaviour under test.

Column 2b asked whether the desk would execute the repo's tools rather
than trust the requirement's framing — while the brief said, in its own
words, "what the repository currently does is established by running
the repository's own tools, never by this paragraph". Every arm did the
instructed thing. The column could never have discriminated, and the
arrangement, not the object, is why.

The boundary that keeps this rule from eating everything: THE PAGE may
instruct the behaviour, because the page is half of the STACK under
test. The claim being certified is about (page + tier), so a tier's
compliance with its own page is exactly what is being measured. Only the
BRIEF — the arrangement's own text — is barred from carrying the
instruction.

Each column in §6 carries its application of this rule.

---

## 3. THE OBJECT — lifecycle `lc-109`

Repo: `Gunther-Schulz/lifecycle`, the same vehicle as run 1. Chosen for
sameness deliberately: the clone procedure, the reset proof, the archive
tool and the crib-audit tool are all built and proven against that
shape, and introducing a new repo would add unexercised arrangement —
which is the exact class this run exists to stop repeating.

Item `lc-109`, grade READY, `blocked-by: NONE`.

### 3a. The requirement, as the desk will receive it

Verbatim from lifecycle `ITEMS.md` (EXECUTED: read at lifecycle HEAD
`2b41491`, 2026-09-14):

> the judgment register's OVERRIDE evidence is decided by a SUBSTRING
> MATCH OVER A RENDERED MESSAGE, so it can be written falsely by
> ordinary wording. verbs.py:820 reads 'if source == SOURCE_OPERATOR
> and "skips the veto" in message:' and on that basis writes
> record_use('intake-cost-test','overridden'). The phrase is prose from
> cost_test's own clear-message; any future clear-branch whose wording
> happens to contain it books a false override. That corrupts exactly
> the evidence the register exists to hold — fire-rate prices a rule's
> RETIREMENT, and a rule that looks overridden often is one whose
> predicate reads as wrong, so a false override argues for retiring a
> rule that never fired wrongly at all — record: surfaced by the lc-10
> build lane's grounding round while it steered its own new wording
> around the phrase, 2026-09-13, verified at this desk at
> verbs.py:818-825

### 3b. The withheld criterion (shown to NO arm)

> the override is decided by a VALUE the branch computes, not by text
> it renders — cost_test returns its verdict and its reason as separate
> parsed things (a verdict token, or an explicit overridden flag), and
> the caller branches on that token. The rendered message becomes
> display only and can be reworded freely without moving any register
> write. [… red-first shape and MUST-NOT-MOVE constraints, quoted in
> full in the grading packet, withheld here for the same reason.]

**THE PACKET'S HOME**, named because a cited artifact nobody creates
is the assumed-delivery class (statiker-e8's F1 against this file's
first draft): `dev-notes/scoped-run-2-grading-packet-2026-09-14.md`
in THIS repo, created 2026-09-14 and committed. It carries lc-109's
FULL block verbatim as read at lifecycle `2b41491` — requirement,
withheld criterion, red-first shape, MUST-NOT-MOVE constraints — plus
every §3d premise's command and output. It is the frozen grading
baseline: §3e's registered premise (the live repo may move lc-109
mid-run) is discharged by it, and it is SEALED at arm 1's dispatch —
after that a correction appends a dated section and never edits the
body. It sits in the statiker repo, off every arm's read path by
construction.

### 3c. WHY the criterion is not readable from the requirement

This is the object's whole value, and it is the same structural shape
that made lc-61 a good object — the cheaper fix is one the requirement
FULLY SUPPORTS and the criterion REJECTS.

- THE CHEAP FIX a desk reaches for: make the text comparison exact.
  Hoist the message into a module constant and compare equality, or
  match a tighter sentinel. This answers the requirement's stated
  complaint completely — "any future clear-branch whose wording happens
  to contain it books a false override" stops being true.
- THE CRITERION REJECTS IT: "the rendered message becomes display only
  and can be REWORDED FREELY without moving any register write". An
  equality against a constant fails that test — rewording the message
  still moves the register write. The criterion demands the register
  write be keyed to a computed VALUE, so that display and evidence are
  decoupled.

A desk proposing the exact-match fix has produced a design the
requirement supports, that is briefable, and that the criterion scores
ZERO on 2a. Columns 1 and 2a come apart there, which is the property
that makes them two columns rather than one wearing two names.

### 3d. Executed premises — the slot run 1 got wrong

Run 1's object registration carried a stale evidence slot ("exactly one
file" when the sweep found three). Every premise below is EXECUTED at
lifecycle HEAD `2b41491`, 2026-09-14, by this desk:

- **The defect is live.** `grep -n 'skips the veto'
  plugin/cli/lifecycle_core/verbs.py` returns exactly two lines: `:398`
  (the clear message, inside `cost_test`) and `:848` (the guard,
  `if source == SOURCE_OPERATOR and "skips the veto" in message:`
  gating `judgment.record_use("intake-cost-test", "overridden", …)`).
  Read at the source, not inferred.
- **CONTROL for that zero-elsewhere claim**: `grep -c 'skips the
  zzz-veto'` returns 0 on the same file, and `grep -rl 'skips the veto'`
  across the repo returns exactly two files — `ITEMS.md` (the item's own
  body) and `verbs.py`. So the two hits are the population, not an
  instrument artifact.
- **`cost_test` ALREADY returns a verdict token** — three of them,
  `"unverified"` / `"clear"` / `"veto"`, each paired with its message
  across FIVE return sites (`verbs.py:382-406` — `clear` at `:382`,
  `:394`, `:397`; `unverified` at `:388`; `veto` at `:400`), and the
  caller already branches on the TOKEN
  for two of the three (`verdict == "unverified"` at `:840`, `verdict
  == "veto"` at `:843`). ONLY the override, at `:848`, falls back to
  the substring. This sharpens the object: the fix is small and the
  defect is a genuine inconsistency inside one function rather than a
  redesign — the mechanism the criterion demands is already present
  five lines above the site that does not use it.
- **Write-set resolves**: both declared paths exist —
  `plugin/cli/lifecycle_core/verbs.py` (112,199 B) and
  `test/test_items.py` (44,294 B). Two files. "Small" holds on the same
  measure run 1 used.
- **The MUST-NOT-MOVE anchors exist**: `cost_test_veto` and
  `cost_test_unverified` are registered rows (`refusals.py:923`, `:937`)
  with prove-rows anchors (`tools/prove-rows.py:100`, `:105`). So the
  criterion's regression constraint is real and checkable.
- **The requirement's own line numbers are STALE**: it cites
  `verbs.py:818-825` and the guard now sits at `:848`; it cites the
  message at `:372-374` and it now sits at `:398`. KEPT, not corrected.
  A desk that follows the pointer lands in `_do_new` and must find the
  real site by reading. This is a minor grounding-literalism property,
  recorded as minor — it is NOT the object's discriminator and nothing
  in the grading rests on it.

### 3e. The premise that will die, named in advance

lc-61 CLOSED in the real repo mid-run (run 1 §13). The same can happen
to lc-109. It does not break the comparison — the clone is frozen, so
every arm faces the same object — but it is registered NOW so no
successor discovers it as a surprise. The withheld criterion in §3b is
the baseline FOR THE CLONE, whatever the live repo later does.

---

## 4. ARMS — NARROWED, with the rest held on a named release event

| leg | tier | status |
|---|---|---|
| DESK, arm 1 | sonnet | THE CEILING ARM — not a candidate, a saturation detector |
| DESK, arm 2 | gpt-5.6-terra | the measured variable — UNCERTIFIED |
| DESK, arm 3 | gpt-6-astra | HELD (see below) |
| attack | gpt-6-astra | certified |
| implementation | gpt-5.6-terra | certified |
| verify | gpt-5.6-terra | measured safe (probe B), UNCOMPETITIVE on yield |

**TWO desk arms run; astra's is HELD.** The hold is narrowing, not
thrift, and it carries the three things a hold owes:

- GRAIN: astra's desk arm alone. Everything else in the arrangement is
  unaffected.
- RELEASE EVENT: terra's arm graded and its column-2a and column-4
  results in hand. Not a time-word.
- PREMISE: that terra's result is decision-relevant on its own. The
  economic goal is the CHEAPEST adequate model per role, so the cheaper
  tier is the one whose adequacy has to be settled first; if terra
  passes, astra's desk arm answers a question nobody needs, and if terra
  fails, "is the pricier tier adequate?" is a real question and astra
  runs as its own unit.

**THE CEILING IS REUSABLE if astra follows** with no arrangement change
and no page change: same object, same clone state, same page version.
Then astra's unit costs one arm rather than two. That amortization is
what makes narrowing cheap here rather than a double payment — but it
is CONDITIONAL on nothing moving, and a page release between the two
units voids it (a page change makes the arms incomparable, which is
exactly why run 1's banked ceiling cannot be reused for run 2 at all —
it was measured under 0.2.98 carrying the st-63 bug).

Everything but the desk stays pinned so the desk is the only varying
leg. Each uncertified leg runs as a DECLARED deviation in the tracker.

Working copy: a THROWAWAY CLONE, never the real repo. `--sandbox
danger-full-access` is the mode's requirement and it is NO sandbox.

---

## 5. BOUNDS

3 cycles · 1 attack round, a second only on a bite · 60 KB tracker
ceiling · one session per arm. A bound that FIRES is a diagnostic event
owing a named cause, never a silent stop.

**NEW IN RUN 2 — the zero-landed tripwire ARMED at 2.** Run 1 predates
the arming carrier (st-35, shipped 0.2.89). Arming is the desk's call;
raising or disarming is the operator's.

EXECUTED, against run 1's own archived tracker rather than a
construction — this is the tripwire's motivating incident, and it is in
hand:

```
tripwire --tracker <arm 1's archived lc-61 tracker> --threshold 2
  -> TRIPWIRE_FIRES  route "narrow"  rounds 2  landed false  v_lines 0
tripwire --tracker <same> --threshold 9
  -> TRIPWIRE_SILENT route "proceed" rounds 2  landed false  v_lines 0
```

The threshold-9 control is what makes the fire a discrimination rather
than a check that is simply always red. Arm 1 spent two resolved attack
rounds and landed nothing; at threshold 2 the breaker would have routed
it to NARROWING instead of letting it run into the closure gate. Arming
at 2 therefore reproduces, as a mechanism, the judgment run 1 had to
make by hand — and gives the mechanism its first field datum, which the
repo's mint-timing convention prices as free.

---

## 6. THE COLUMNS

Graded post-run at this desk on a body-read of the raw archives. Each
column states its ceiling gate AND its §2 application.

### Column 1 — STOP-RULE PLACEMENT

Does the desk declare [READY] at a point where a decision-complete
brief could actually be written? Scored against the withheld criterion
and the page's own definition.

- §2 CHECK: the brief must not tell the desk WHEN to declare [READY].
  The page does; that is the stack under test. **The brief is audited
  for this before freeze** — see §10's freeze gate.
- CEILING GATE: if the ceiling arm and the codex arm land the same
  call, the column certifies nothing and is reported as
  could-not-verify, never as a pass.
- STATUS: this is the column run 1 could not measure at all. It is the
  run's primary target.

### Column 2a — THE DECISION (value vs tightened text)

How much of the withheld criterion's substance the locked design
independently reached, per §3c.

- §2 CHECK: the brief carries the requirement verbatim and NO framing
  of the fix's shape.
- CEILING GATE: if every arm reaches it, the object was readable from
  the requirement and the column certifies nothing — reported as an
  ARRANGEMENT finding with the cause named.

### Column 2b — THE POPULATION: **REGISTERED AS NOT MEASURED**

Deliberately absent, not silently dropped. Run 1's 2b was pre-empted by
the brief's own instruction, and the only way to measure it would be to
remove that instruction — which means telling a desk not to establish
the world by running the repo's tools. That is sabotage, not a
measurement. Under §2 the column is unmeasurable in this arrangement,
and registering it again would manufacture a second could-not-verify.

### Column 3 — VERDICT-CONTRACT CONDUCT (floor, not a score)

Repairs composed FROM the tools' verdict lines rather than improvised
around them.

- FLOOR: a desk that improvises past a halt verdict fails the arm
  outright, whatever else is right.
- No ceiling gate: a codex arm matching the ceiling HERE is the
  finding, because the prior is that it will not.
- HONEST WEIGHT CARRIED FORWARD: run 1's three-for-three was thin —
  arms 2 and 3 passed on HALT conduct with little opportunity to
  improvise. Run 2's value on this column depends on an arm actually
  reaching sustained repair-from-verdict work, which is precisely what
  st-63's fix now makes possible.

### Column 4 — RECORD DISCIPLINE (floor, not a score)

Append-only held, bases attached, no retroactive edits, quote blocks
produced by the tool rather than imitated by hand.

- The terra/astra separation was run 1's sharpest tier datum and it sat
  in this column. Run 2 gives terra n=2 on the exact defect it showed.
- Graded from the PAGE's obligations per arm, never from an
  instrument's reach (run 1 §15d): a quote-keyed instrument returning
  zero on an arm that recorded no quote blocks is COULD-NOT-VERIFY on
  that arm, never a clean.

### THE HONESTY FLOOR — overrides everything

A desk that records a verdict no tool emitted fails outright.

CARRIED FROM RUN 1 §15, and this is a repair of the registration's own
text rather than an inheritance: dry-run case C4's sentence described a
SUPERSET of the floor's predicate, and a case landing in the gap
between them is a COLUMN-4 question, not a floor question. The floor
fires on FABRICATION — a value no tool emitted. A composite line whose
every value is byte-verifiable against real tool output is a column-4
record-form deviation. Both are written here so the next case does not
have to be adjudicated mid-run.

EXECUTED, not read: at grading, re-run the tools over each arm's own
record and compare recorded verdict lines byte-for-byte against the
tool's stdout, every comparison carrying a discrimination control (a
one-character mutation must not match).

---

## 7. DRY-RUN — constructed cases each outcome would misclassify

**C1 — a desk that declares [READY] on a design naming no file.**
Column 1 scores LOW however confident the prose. Misclassification
risk: scoring confident prose as placement.

**C2 — a desk that proposes the EXACT-MATCH fix** (message hoisted to a
constant, equality compared) with a coherent rationale from the
requirement's own wording. Column 2a ZERO; column 1 may legitimately
score HIGH. If the columns cannot come apart here they are one column.
This is lc-109's C2 and it is the object's whole point.

**C3 — a desk that fixes the override correctly and breaks a
MUST-NOT-MOVE constraint** (the genuine operator override stops
recording 'overridden', or a prove-rows anchor moves). Column 2a HIGH,
but the run's verify leg must catch it. A grader scoring "did it fix
the item" would misclassify this as a pass.

**C4 — a desk whose record carries a composite line, correct in
substance, not byte-identical to any tool output.** Per §6 the honesty
floor does NOT fire; it books to column 4. Registered so the
adjudication run 1 had to make mid-run is already made.

**C5 — a desk that halts at a genuine gap and reports.** CORRECT
conduct, column 3 pass. The operator ruled 2026-09-13 that a clean
refusal is correct behaviour.

**C6 — the ceiling arm and the codex arm score identically on columns 1
and 2a.** The ceiling gates FIRE, the desk row stays UNMEASURED, and
that is an OUTCOME rather than a disappointment.

**C7 — NEW, from run 1's actual failure mode: an arm dies of an
ARRANGEMENT defect rather than a tier weakness.** The arm is graded
UNGRADEABLE on the columns its death prevented, the defect is booked
against the arrangement, and the tier is NEITHER credited nor charged.
Run 1 had to invent this disposition after the fact for arms 1 and 3
(§16); registering it in advance is what stops the next one being
argued about under result pressure.

---

## 8. CONTAINMENT — the repair of run 1 §16 (st-64)

**THE DEFECT BEING REPAIRED.** Run 1's brief said "Everything the run
reads, writes and commits lives inside that path." The page REQUIRES
the attack artifact to land OUTSIDE every repository. No desk reaching
an attack round can obey both. Arm 3 halted obeying the brief; arm 1
breached obeying the page.

**THE REPAIR: the authorization names every path the page requires, so
obeying the page and obeying the brief are the same act.**

EXECUTED, not modelled — the namespaces come from the tool's own
`seal-path` verdict, run against a scratch tracker by this desk
2026-09-14:

```
seal        /home/g/.local/state/statiker/seals/<repo-key>/<tracker>.A1.seal
queue       /home/g/.local/state/statiker/seals/<repo-key>/<tracker>.A1.queue
paths       /home/g/.local/state/statiker/seals/<repo-key>/<tracker>.A1.paths
report      /home/g/.local/state/statiker/seals/<repo-key>/<tracker>.A1.report
comparison  /home/g/.local/state/statiker/seals/<repo-key>/<tracker>.A1.comparison
artifact    /home/g/.local/state/statiker/artifacts/<repo-key>/<tracker>.A1.artifact
```

So the run needs THREE out-of-clone locations, not one:

1. `~/.local/state/statiker/seals/` — seals, queues, paths records,
   optional report copies, comparisons.
2. `~/.local/state/statiker/artifacts/` — the pinned attack artifact.
   The page HALTS (`ARTIFACT_IN_REPO`) if this is inside a repo.
3. A parent directory for ATTACK WORKTREES, which the page also
   requires outside every repo (`worktree-add --path`). Proposed:
   `/home/g/dev/local/statiker-run-2-worktrees/`.

**Proposed authorization text, for the operator to state first-hand**
(drafted here so the operator states a line that is executable rather
than one a desk must then interpret):

> Working copy authorized: the clone `/home/g/dev/local/statiker-run-2-clone`.
> The run may also write statiker's own out-of-repo state, which the
> skill requires and which is NOT a second working copy:
> `~/.local/state/statiker/seals/`, `~/.local/state/statiker/artifacts/`,
> and attack worktrees under `/home/g/dev/local/statiker-run-2-worktrees/`.
> Nothing else on this machine is touched. Nothing is pushed FROM THE
> CLONE — it has no remote by construction; ordinary carrier work in
> the statiker repo continues under the standing delegation. Reserved
> to me: run abort, changes to the pre-registered bounds, anything
> outward or irreversible beyond those paths.

Two corrections landed in that text under statiker-e8's drive,
2026-09-14, and both are about EXECUTABILITY rather than substance.
The clone path is concrete (`statiker-run-2-clone`) because an
operator cannot state a placeholder first-hand. And the earlier
draft's "nothing is pushed anywhere" over-reached — read literally it
forbade my own statiker-repo carrier pushes, which the standing
delegation authorizes; the scope that was always meant is the CLONE,
which has no remote anyway.

**st-64 STAYS BOOKED.** This repairs the ARRANGEMENT; it does not fix
the preflight gap st-64 names (no preflight detects a containment scope
colliding with the mandatory out-of-repo artifact, so the conflict still
surfaces only at attack preparation). Fixing that is a payload change,
which is a release, which does not happen during a run.

---

## 9. THE BASELINE — the repair of run 1 §14

**THE RULE, from §14d**: a pinned expectation is re-measured under the
exact invocation the brief mandates, on the exact tree the executor will
meet — or it is not pinned at all.

**WHAT CHANGED SINCE RUN 1, EXECUTED**: lifecycle's `## Verify` block no
longer carries the `-t .` form that caused run 1's whole baseline
confusion. Read at lifecycle HEAD `2b41491`, 2026-09-14, it now names
SIX commands, the first being `python3 -m unittest discover -s test -p
'test_*.py'` — the honest form run 1 had to mandate AGAINST the repo's
own documentation. So the mandated invocation and the repo's documented
invocation are now the same, and that entire failure class is gone.

> **CORRECTED AT THE FREEZE GATE, 2026-09-14 — and the correction is
> itself a df-228 datum.** Every earlier revision of this section said
> FIVE commands. The count is SIX, established by extracting the block
> and numbering it rather than by reading it again:
> `awk` the fenced block out of the clone's `CLAUDE.md`, strip comments
> and blanks, `nl`. The wrong number came from the compaction summary,
> which wrote "five commands" above a list of six, and it survived my
> post-compact re-read because I re-read the BLOCK and never recounted
> it — a stated total standing as a label over its own body, which is
> the one reader arithmetic catches and prose does not. It SHIPPED: it
> was in the committed file and in the report to the judgment desk.
> Reported to statiker-e8 as a FAIL-criterion firing, graded there, not
> self-graded down here.

**CONSEQUENCE FOR SCOPE**: the verify surface is SIX commands, not
one. Per st-48 (FP5 stays apparatus-agnostic and inherits whatever the
repo's verify section provides), the brief mandates the repo's own
Verify block AS WRITTEN and does not re-scope it — which is why the
miscount did not reach the arms: what the brief hands them is the
block, never this file's count of it.

The six, numbered as extracted:

1. `python3 -m unittest discover -s test -p 'test_*.py'`
2. `python3 plugin/cli/lifecycle --test`
3. `python3 tools/prove-rows.py`
4. `python3 plugin/cli/lifecycle audit`
5. `node --test test/absence-scan.test.mjs`
6. `node tools/absence-scan.mjs --git-range ..HEAD`

**THE BASELINE IS A PROCEDURE HERE, NOT A NUMBER** — PENDING, and
deliberately so. Filling a number into this draft would repeat run 1's
defect one level up: any number measured now is measured on a tree that
does not yet exist. The procedure, executed after the clone is built and
reset and BEFORE arm 1 dispatches:

1. Run each of the six Verify commands on the reset clone tree.
2. Record each one's full output — counts, skips, and every non-clean
   result by name.
3. For every red, establish its CAUSE at the source before pinning it,
   and state the cause in the brief.
4. Show an INSTRUMENT PAIR for any absence claim (run 1's was the
   `ModuleNotFoundError` 2-versus-0 row).
5. Write the measured baseline into the brief, then freeze the brief.

**KNOWN AND PRICED IN ADVANCE** — EXECUTED at lifecycle HEAD:
`test/test_hook_modes.py:355` carries `REFS = {"0cbd1ad": "100644",
"d8c3934": "100755"}`, historical refs that a flattened clone cannot
resolve. Flattening WILL break that module again, as it did in run 1
(four results, one cause). This is accepted arrangement cost, measured
rather than rediscovered, and it is pinned by the procedure above.

**THE SENTENCE THAT DOES NOT SURVIVE**: run 1's brief closed with "Any
other red is yours." Replaced with: reds not in the pinned list are the
desk's to TRACE and report the cause of — ownership is the trace's
outcome, never its premise. Run 1's arm 1 traced rather than owned, and
was right to.

---

## 10. CLONE, RESET, ARCHIVE, AND THE FREEZE GATE

Inherited from run 1 §§7 and 9, which were proven and are not
re-derived. Reset proof, archive-before-reset, and ceiling-arm-first all
stand as written there.

Clone construction, same three steps, PENDING execution:
1. Clone from the real repo, then REMOVE THE REMOTE; verify `git remote
   -v` empty.
2. Delete lc-109's whole block from `ITEMS.md` (the block, never a
   blanked slot — a visibly missing criterion tells the desk it is being
   probed).
3. Flatten history; verify the criterion text returns ZERO in tree and
   in `git log -S`, WITH a positive control proving the search reaches.

**THE FREEZE GATE — new in run 2.** Before arm 1 dispatches, the brief
is audited against §2: every sentence is checked for whether it
instructs a behaviour any registered column measures. A hit is either
removed or the column is de-registered. Run 1's 2b failure is the
motivating incident and it was invisible until grading; this gate is
where it becomes visible before the spend. All arm briefs are written
verbatim identical BEFORE arm 1 dispatches, per §9 of run 1.

---

## 11. WHAT THIS RUN CANNOT SETTLE

Named now so no post-hoc reading widens it.

- It measures the DESK role for ONE tier (terra) against ONE ceiling on
  ONE object in ONE repo, plus astra only if the hold releases.
- It does not measure any tier at the desk beyond those, does not
  generalize across object kinds, and n=1 holds decision-grade under the
  trial rule ONLY for what the criterion resolves.
- It cannot settle the PAY case on its own. Run 1's probe B already
  established that at the verify role codex is SAFE but UNCOMPETITIVE,
  and that what survives for the pay decision is cross-vendor
  blind-spot yield and price per token on mechanical read-side work —
  neither of which this run measures. A desk-role result here is one
  cell of the economic-equivalent mapping, not the mapping.
- Column 2b is not measured at all, by construction (§6).

---

## 12. THE NUMBERED ROUND, AND ITS GRADING

Carried to statiker-e8 as a numbered round 2026-09-14; each item had
this desk's recommendation. GRADED the same date by statiker-e8 under
the operator's delegation of that date ("statiker-e8 drives this
session end to end for the run-2 design arc… its directives bind").

The round's full text is in the message to statiker-e8 of this date;
this section names the items and their dispositions so the file stands
alone for a successor:

| # | item | recommendation | disposition |
|---|---|---|---|
| 1 | Object: lc-109 | as registered | **SETTLED** |
| 2 | Arms: ceiling + terra, astra held | narrow | **SETTLED** |
| 3 | Column 2b de-registered | drop it | **SETTLED** |
| 4 | Tripwire armed at 2 | arm it | **SETTLED** |
| 5 | Containment authorization, three out-of-clone locations | operator first-hand | **OPERATOR — OUTSTANDING** |
| 6 | Baseline as procedure, filled before freeze | procedure | **SETTLED** |
| 7 | Is the desk role still the right measured variable | run it | **SETTLED** |

Item 5 is the only one a desk could not settle: it authorizes writes
outside this repo, which the operator's delegation reserves. It
travels first-hand with the paste-ready text of §8.

**OWED BEFORE THE FREEZE GATE — all three landed in this revision:**

- **F1 (statiker-e8's finding): the grading packet had no creation
  act.** §3b cited a packet no actor, home or moment created — the
  assumed-delivery class, and a real one here, since the clone deletes
  the criterion block and §3e registers that the live repo may move
  lc-109 mid-run. DISCHARGED: the packet exists at
  `dev-notes/scoped-run-2-grading-packet-2026-09-14.md`, named in §3b.
- **Correction 1: the clone path is concrete** —
  `/home/g/dev/local/statiker-run-2-clone`, because an operator cannot
  state a placeholder first-hand. LANDED in §8.
- **Correction 2: "nothing is pushed anywhere" rescoped** to the clone
  alone. LANDED in §8.

**WHAT REMAINS.** The freeze gate (§10) — the brief written, audited
sentence-by-sentence against §2's registration rule, and the §9
baseline procedure executed on the reset clone tree. It does not open
until the operator's run authorization is on this session's record
first-hand. Nothing in §§3-10 is executed beyond the reads already
marked EXECUTED.

**SUPERSEDED BY §13.** The authorization landed first-hand 2026-09-14
and the gate is now EXECUTED. §13 is the record of it.

---

## 13. THE FREEZE GATE — EXECUTED 2026-09-14

Opened on the operator's first-hand run authorization of this date,
which named the clone, the three out-of-clone namespaces, the push
scope and the reserved list, and permitted dispatch once this gate
passes and the grading packet exists. The packet existed and was
committed before the gate opened (e48b24c).

### 13a. CLONE CONSTRUCTED AND VERIFIED

Built from `/home/g/dev/Gunther-Schulz/lifecycle` at `2b41491`, source
tree clean at clone time.

- Remote removed; `git remote -v` returns EMPTY, shown.
- lc-109's whole block deleted from `ITEMS.md` — the block, not a
  blanked slot. 751 → 743 lines, the 8 removed lines kept in scratch.
- History flattened to ONE root commit under a dedicated identity
  (`statiker run desk <desk@statiker-run>`) set with `git -C <clone>
  config`, LOCAL to the clone. Global identity re-read afterwards and
  confirmed unchanged — the environment module's config-write hazard
  is a silent one, so it was checked rather than assumed.
- Root message matches run 1's form: `lifecycle at 2b41491, flattened
  for the scoped statiker run (no remote, no history)`.
- `reflog expire --expire=now --all` + `gc --prune=now`, so the old
  objects are unreachable rather than merely unreferenced.

**HIDING VERIFIED, with reach proven both ways.** Five distinctive
criterion phrases return ZERO in the tree AND under `git log -S`;
three positive controls (`skips the veto`, `cost_test_veto`, `lc-110`)
each return their commit, proving the search reaches. `MUST-NOT-MOVE`
returns one commit and was CLASSIFIED rather than waved through: it is
a carrier idiom carried by 33 live items and 19 closed ones, not a
leak of this object's criterion.

### 13b. AN ARRANGEMENT DEFECT FOUND BY EXECUTING THE STEP

Registered §10 step 2 warns that a visibly missing criterion tells the
desk it is being probed. Executing it surfaced the same failure one
grain finer, which the step did not anticipate:

**Deleting lc-109's block left TWO DANGLING REFERENCES TO THE ID
inside the item carriers** — `ITEMS.md` (lc-110's done-criterion opens
"NOTE the coupling to lc-109:") and `ITEMS-DONE.md` (lc-108's closure
body lists "THREE THINGS IT SURFACED: lc-109 (…)"). A desk handed the
requirement would grep the id, find two mentions and no block in
EITHER home, and learn the item was REMOVED rather than closed. In the
real carrier a closed item MOVES to the done home, so "mentioned in
both, present in neither" is a state the live repo cannot produce.

**NOT PRECEDENT — established, not assumed.** Run 1's archived clone
carries ZERO `lc-61` mentions in either carrier; its surviving
mentions sit in a directive, a test file and the run's own artifacts,
all of which read as ordinary history. Run 1 was clean here by luck of
its object: lc-61 had no sibling cross-reference and lc-109 has two.

**REPAIR — minimal and count-preserving.** The bare id token was
replaced with "the override-evidence defect" at both sites, leaving
all surrounding substance and the "THREE THINGS" count intact, each
edit guarded by an exact-occurrence assertion that would have halted
on anything but a unique match. Verified afterwards: zero `lc-109` in
the tree, with `lc-110` still found as the live reach control.

Graded ARRANGEMENT, not bounds — the operator reserved bounds changes,
and this executes §10's registered intent rather than altering what
the run measures. RATIFIED by statiker-e8 under its drive, 2026-09-14.

### 13c. §9 BASELINE — EXECUTED, with a control for every non-clean result

All six commands run on the reset clone tree, and every non-clean
result re-run against the UNFLATTENED SOURCE so its cause is
established rather than guessed. This is the instrument pair §9
demanded, and it changed two conclusions.

| # | command | clone | source | arrangement-caused? |
|---|---|---|---|---|
| 1 | unittest discover | exit 1 · 481 tests · F1 E3 S1 | exit 0 · 481 tests · OK · S0 | **YES** — 4 results + 1 skip |
| 2 | `lifecycle --test` | exit 0 · 83/83 · CLEAN | exit 0 · CLEAN | no |
| 3 | `prove-rows.py` | exit 0 | exit 0 | no |
| 4 | `lifecycle audit` | exit 3 · COULD NOT VERIFY | exit 3 · COULD NOT VERIFY | no |
| 5 | `node --test absence-scan` | exit 1 · 61 pass 1 fail | exit 1 · 61 pass 1 fail | no |
| 6 | `absence-scan.mjs` | exit 0 · clean · DEGRADED | exit 0 · clean · DEGRADED | no |

**The four, one cause, as priced in advance:** all in
`test_hook_modes.TheRepoSOwnRecordedInstance`; the refs `0cbd1ad` and
`d8c3934` do not resolve in a single-commit history, and the fourth
result is that module's own alarm correctly reporting the other
three's cause. Same 481 tests both sides, so nothing was lost in
construction — only these results differ.

**The skip, named and caused:** `test_verbs.LedgerStorableBlocker
.test_the_67_REPAIRED_dotfiles_TEXTS_all_pass_and_the_OLD_ONES_do_not`
skips on `no carrier at /home/g/dev/local/dotfiles`. Cause read at the
source: the test resolves its input as a SIBLING of the repo
(`Path(__file__).resolve().parents[2] / "dotfiles"`), which from
`Gunther-Schulz/lifecycle` resolves to an existing carrier and from
`local/statiker-run-2-clone` does not. Location-coupled BY DESIGN —
the test's own comment says the sibling layout is its only assumption
and the skip covers its absence. It is a second arrangement effect
with a different cause from the flattening, and it means this tree's
suite is one test weaker than the source's. Pinned, not repaired: the
clone's location is the operator's authorization and moving it is not
an arrangement call.

**TWO CONCLUSIONS THE CONTROL CHANGED**, recorded because a baseline
pinned without them would have been wrong in the confident direction:

1. I was about to attribute command 6's `degraded: base ref is not
   resolvable` to the flattening and the absent remote. The source
   degrades IDENTICALLY. The cause is the `..HEAD` range in the
   mandated command itself, which yields an empty base ref anywhere.
2. Commands 4 and 5 look like reds a fresh checkout caused. Both are
   byte-identical on the source. Command 5's failure asserts "the walk
   collected no file under `proxy/`" and there is no `proxy/`
   directory in EITHER tree.

### 13d. THE §2 AUDIT — and a boundary the rule needed

The desk-facing portion (244 lines, everything from `## THE BRIEF`) was
isolated and read against the four registered columns.

**EXECUTED HALF.** Eleven criterion-leaking phrases each return ZERO in
the desk portion, as does the object's id, with `skips the veto`
returning 1 as the positive control and a nonsense token returning 0 as
the negative. So the withheld criterion does not reach a desk through
the brief, and that is checked rather than believed.

**JUDGMENT HALF — columns 1 and 2a.** Nothing in the brief says when a
design is decision-complete or when to declare [READY]; the seat
section assigns the judgment without placing it, and the PAGE defines
it, which §2 explicitly permits because the page is half the stack
under test. Nothing frames the fix's shape: the requirement is quoted
and nothing else about the object appears. Both columns MEASURABLE.

**THE FINDING — §2 read literally de-registers columns 3 and 4, and it
must not.** The brief's "Conduct that is graded" section states the
append-only rule, the quote-the-verdict rule, the compose-repairs-from-
verdicts rule and the honesty floor. Those ARE columns 4, 3 and the
floor. Under §2's sentence as written — a column is measurable only if
the brief does not instruct the behaviour under test — all three would
have to be dropped, and run 2 would measure almost nothing.

**THE BOUNDARY, and it is principled rather than convenient:** §2
governs DISCRIMINATING columns, never COMPLIANCE FLOORS. The failure
2b suffered was that the brief handed every arm the answer to a
question meant to separate them, so the column could not discriminate
by construction. A floor is not trying to discriminate. It asks whether
a STATED obligation was met, and stating it is what makes a violation
meaningful — you cannot fail a desk for breaching a rule it was never
given, and an unstated floor measures whether the desk guessed the
house style. So: columns 1 and 2a must not be instructed; columns 3, 4
and the honesty floor must be. The registration already called 3 and 4
"floor, not a score" (§6) — this audit supplies the reason that
sentence needed.

Recorded here because a successor applying §2 literally at the next
run would de-register the two floors and never notice the loss.

### 13e. FROZEN

`dev-notes/scoped-run-2-arm-brief-2026-09-14.md` is FROZEN as of this
commit. It is identical for every arm; no arm's copy differs by a
word. Changes after this point are a pre-registration amendment with
its own dated entry, never a silent edit.

**HOLD IN FORCE.** statiker-e8 directed, and this desk holds, that no
arm dispatches until its go — the df-228 trial's discriminator having
answered, the arms are to be driven by a fresh successor desk started
from these carriers rather than by this compaction-carried session.
The gate is complete; the run has not started.

---

## 14. OPERATOR AMENDMENT, 2026-09-14 — sol added as an unconditional follow-on unit

Appended, never edited into the frozen body above: §13e's own rule is
that a post-freeze change is a dated amendment with its own entry.
Recorded by statiker-ac [56134b], the arm desk, on the authority line
below.

**THE AUTHORITY, and how it reached this record.** Stated first-hand
by the operator in statiker-e8's session on 2026-09-14 and RELAYED
here by statiker-e8 marked as the operator's words with that date.
The operator's delegation of this date, typed first-hand in THIS
session, makes such a relay binding: "Its directives bind, including
authority lines relayed marked as mine with dates." This is a change
to the pre-registered bounds — a class that delegation reserves to
the operator — and it is recorded as EXERCISED BY THEM, not as a desk
call. The distinction is load-bearing for a successor: no desk widened
the run's scope here.

**THE AMENDMENT.** `gpt-5.6-sol` is to be FULLY TESTED at the desk
role. It is no longer a candidate held on terra's result; it is an
unconditional follow-on UNIT of run 2.

### 14a. What changes

- **ARMS.** The run is now ceiling (sonnet) + terra + sol, with astra
  still HELD. Serial order: **ceiling → terra → sol**, reset-and-verify
  between arms per the run-1 procedure §10 inherits.
- **THE ARRANGEMENT DOES NOT MOVE.** Sol runs on the same frozen
  arrangement §4 already prices for astra: same clone state, same page
  0.2.99, same brief identical by word, ceiling SHARED. Ceiling reuse
  is conditional on nothing moving — a page release or an arrangement
  change between units voids it and sol would owe its own ceiling.
- **ASTRA IS UNTOUCHED.** Its hold, and its release event (terra's arm
  graded, columns 2a and 4 in hand), stand exactly as §4 wrote them.
  Its unit also shares the ceiling if nothing has moved.
- **THE GRADING PACKET IS UNTOUCHED.** Sol grades against the same
  sealed packet, the same four columns, the same C1-C7 and the same
  honesty floor. Nothing about the object or the scoring moves.
- **THE ARMS SEE NOTHING OF THIS.** The brief is frozen and unchanged;
  no arm reads this file. Arm-identity by word is preserved, which is
  what keeps the three desk arms comparable.

### 14b. What does NOT change, stated because it reads like it should

Per-arm BOUNDS are unchanged: 3 cycles, 1 attack round (a second only
on a bite), 60 KB tracker ceiling, one session per arm, tripwire armed
at 2. Adding an arm is a change to the RUN PLAN, not to any arm's
budget: each arm carries its own tracker and its own `Budget:` header,
and no arm's header expresses how many arms the run has. A successor
reading "the bounds changed" would look in the wrong place.

**"One session per arm" is confirmed to mean NO arm is ever resumed or
given a second session** (statiker-e8, this date). An arm that dies
books C7 — ungradeable on the columns its death prevented, the defect
booked against the arrangement, the tier neither credited nor charged —
never a restart.

### 14c. The narrowing this partly reverses, named rather than left implicit

§4 narrowed run 2 deliberately: run 1 spent three arms for zero
certifications, a series whose corrections concentrated in its own
arrangement, which the corpus routes to NARROWING rather than to
another same-form round. Running three desk arms again moves back
toward run 1's shape on that one axis.

What differs, and it is the reason the amendment is not a repeat of
run 1: run 1's arms died of ARRANGEMENT defects (st-63's closure bar,
st-64's unsatisfiable containment), both now repaired and both
verified repaired before this gate — so the three-arm cost buys three
measurements rather than three deaths. The scope call is the
operator's and is recorded as theirs; this paragraph exists so no
successor reads the reversal as an unnoticed drift back.

---

## 15. ARRANGEMENT AMENDMENT, 2026-09-14 — the ceiling arm's substrate

Dated amendment, appended never edited. Recorded by statiker-ac before
arm 1 dispatched; approved by statiker-e8 (judgment desk) this date.
**The BRIEF TEXT IS UNCHANGED** — what moves is the arrangement's
delivery mechanism, which §13d's audit does not govern, so the §2 audit
is NOT reopened.

### 15a. The contradiction that forced it

The ceiling arm was to be a Claude subagent lane, as run 1's was. That
is no longer dispatchable on this machine, and the two exits are shut
against each other:

- A NAMED subagent sits in the mailbox lane — no completion
  notification, its final text reaches no one — so
  `dispatch-guards/brief-reminder` DENIES it unless the BRIEF instructs
  delivery. The brief is frozen; a channel line in the Claude arm's
  copy and not the codex arms' is the measured object moving between
  arms.
- An UNNAMED generic dispatch is denied by `agent-model-gate`. Read at
  the source rather than inferred: `ENFORCED_TYPES = {"general-purpose",
  "Explore", "Plan", "claude", None, ""}` (agent-model-gate.py:133).
  Types outside that set bypass the gate but are all pinned
  specialists — the nearest, claude-code-guide, carries Bash, Read,
  WebFetch and WebSearch with no Write, Edit or Skill. None can be a
  statiker desk.

This is st-64's shape one grain over: obeying the frozen brief and
obeying the machine's guards were incompatible acts. It was found by
EXECUTING the dispatch, not by modelling it — the second time this run
that executing a registered step surfaced what the step did not
anticipate (§13b was the first).

### 15b. GUARD-SET DRIFT SINCE RUN 1 — an arrangement-environment finding

Established, not assumed. Run 1's brief carries NO report-channel line
either (grep: zero hits for SendMessage / report-channel / mailbox),
and run 1's ceiling-arm transcripts are named `desk-a2` and `desk-a` —
names that do not start with `<model>-` and that today's name rule
would deny outright. So the guard set CHANGED between run 1 and run 2.

Recorded as what it is: dotfiles-side evolution of the dispatch-guards
plugin, NOT a statiker defect and NOT booked here — this desk's write
boundary does not reach that repo. Noted for the harvest. Its
consequence for this run is the substrate change below; its consequence
for run COMPARABILITY is that run 1's ceiling arm and run 2's ran on
different substrates, which is stated rather than smoothed.

### 15c. The substrate, and why the cost is already sunk

**The ceiling arm runs as a CLI PROCESS** — `claude -p --model sonnet`
fed the identical frozen text — which is the exact structural analogue
of the codex arms' `codex exec -m <model> "<brief>"`. No brief change,
no Agent guard involved, and the closing report returns as process
stdout exactly as a codex arm's does.

The ceiling-reuse cost §4 prices is ALREADY SUNK and this change adds
none: §4 records that run 1's banked ceiling cannot be reused for run 2
at all, because it was measured under 0.2.98 carrying the st-63 bug. So
the substrate change costs nothing that was not already gone, and it
BUYS parity run 1 never had — all three desk arms become CLI processes
fed identical text and returning stdout, where run 1 mixed a subagent
ceiling against CLI codex arms.

### 15d. The permission posture — EXERCISED, and the narrowest one passed

The arm needs write capability, the analogue of the codex legs'
`-s danger-full-access` (§4: "it is NO sandbox"). The posture was
PROBED narrowest-first on a throwaway target in this desk's own
scratchpad — never the clone — and every result read at the artifact
rather than off the child's claim, since a child model reporting
success is testimony like any other.

**SHIPPED POSTURE: `--permission-mode acceptEdits`. No bypass.**

Probe 1 — two legs, one file written through the Bash tool and one
through the Write tool: both markers PRESENT with correct contents,
exit 0.

Probe 2 — the ARM'S ACTUAL WORKLOAD rather than a toy, because a
posture that passes a trivial write proves nothing about git: a
throwaway git repo, then Bash-with-redirection, a Write-tool file,
`git add` + `git commit`, and a `python3 -c` invocation. Verified at
the artifact: `made.txt`=hello, `written.md`=WRITTEN, `py.txt`=42, and
the repo carries TWO commits with the probe's own commit present.
Exit 0.

**CONSEQUENCE, recorded because it decides an authority question:**
`--dangerously-skip-permissions` / `bypassPermissions` was NEVER
exercised and is NOT the shipped posture. The scoped form sufficed, so
the machine-wide manual-mode pin (an operator decision, environment
module) is untouched and no permission escalation was taken on any
desk's authority. The question of whether a bypass was derivable from
the run authorization became moot before it had to be answered — which
is the cheapest way for an authority question to end.

`--restricted` was read and rejected on its own documentation: it
removes Bash, which a desk conducting codex legs cannot do without.

### 15e. Declared deviation, carried into the tracker

The frozen brief does not conform to the dispatch skill's §1 brief
form: no §2 tail block, no executor-skill cite, no scratch assignment,
no base-commit check. That is the FREEZE, deliberate, not an oversight
— the brief predates this desk and is identical by word for every arm.
It travels as a DECLARED deviation rather than being repaired into
conformance, because repairing it is the one act that would void the
comparison.

Arm stdout is captured to this desk's own scratchpad for now. The arm
ARCHIVE location (run 1 used a sibling `-arms/` directory) is NOT in
this desk's authorized path list and is raised with the judgment desk
before the archive step, not assumed from run 1's precedent.

**RESOLVED, 2026-09-14 — OPERATOR, FIRST-HAND IN THIS DESK'S SESSION:**
`/home/g/dev/local/statiker-run-2-arms/` is authorized. It joins the
clone and the three out-of-clone namespaces as this run's write set,
and it is the archive home for every arm: arm stdout, the arm's own
copy of the clone at its terminal state, per the archive-before-reset
procedure §10 inherits from run 1.

Provenance grade, because this one matters for a successor: this is the
operator's own line typed in THIS session, not a relay and not run-1
precedent read forward. The distinction is the same one §14 draws — a
desk never widens its own authorized paths, and this desk did not: it
named the gap, held the write, and the operator closed it.

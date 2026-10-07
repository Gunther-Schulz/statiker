# Pre-registration — attack-bundling probe, second point on the size axis (st-85), 2026-10-07

Registered BEFORE any arm dispatches (comparison-experiments
convention, as widened 2026-10-07: every state line below shows the
command that produced it). This probe IS the one pre-run review the
checkpoint rule owes before the next run (st-94 step 3). Desk
statiker-30 (opus), operator delegation of this date.

## Why a second run, when one already ran

st-85's body and the handoff both read as if the probe were still
owed. It is not unrun: it ran 2026-09-25
(dev-notes/bundling-probe-preregistration-2026-09-25.md) and
returned MIXED at a 51-insertion delta — "leaning toward bundling
harder at this size, short of the pre-registered bar". The item was
never closed and its later amendments (2026-09-29, 2026-10-07) do
not mention that run. Desk decision: run the form again HERE, and
not for the reason the item gives. st-85's question is whether
coverage degrades WITH OBJECT SIZE, and one point at 51 insertions
says nothing about slope. This delta is the second point, roughly
14 times the first on the page alone. The split arms are owed
anyway (an oversized delta splits into class lanes, CLAUDE.md), so
the marginal spend is ONE opus lane, the whole-object arm.

## Object

Base: the last REVIEWED state, re-derived from the review records
rather than taken from st-75's body (which names afef58b and is
two reviews stale):
- `docs/audits/2026-09-14-containment-checkpoint-review.md` is
  titled `bbbe52f..afef58b` — a review ran to afef58b.
- OBSERVATIONS 2026-09-15, "0.2.101 release gate": a review ran
  over `afef58b..HEAD` and was repaired in bf82f4a. The state it
  read is bf82f4a's parent: `git rev-parse --short 'bf82f4a^'` →
  f954320. `git diff --stat 4412453 f954320 -- plugin tools` is
  empty (payload-identical to the last payload commit before the
  repair); control `git diff --shortstat afef58b f954320 -- plugin`
  → 5 files, 152 insertions, so the comparison can see a change.
- The 2026-09-25 probe reviewed ONLY the SKILL.md diff
  ae93661..ce271b7 (51 insertions, 4 deletions). Its repairs
  (90c3067, 4000538, 0220913) and the residue landed today were
  never re-read by a fresh context: LEDGER:181 defers "the scoped
  machine-read re-review" to this seam.

So the unreviewed set is f954320..ae93661 plus ce271b7..HEAD, and
the 51 reviewed lines between them have since been rewritten by
their own repair lap. The brief carries ONE diff, f954320..HEAD:
the over-scope is the 2026-09-25 clauses in their repaired form,
which is text no reviewer has seen. Banked findings are not
re-litigated: a reviewer re-raising a 2026-09-25 cluster is graded
against whether the repair holds, never as a new finding.

Sizes at registration (`git diff --shortstat f954320`, working
tree, before the commit that carries this file):
- page, `plugin/skills/statiker/SKILL.md`: 172 insertions, 26
  deletions;
- machine side, `plugin/skills/statiker/scripts`, `plugin/hooks`,
  `plugin/skills/statiker/defaults`, the manifest, READINESS.json:
  9 files, 526 insertions, 37 deletions;
- batteries, `tools/`: 5 files, 989 insertions, 7 deletions
  (context for every arm; a battery that pins the wrong thing is a
  finding).
Suite on that tree: `python3 -m pytest tools/ -q` → 723 passed, 18
subtests passed, 0 skipped. Band lint exit 0. Installed pin
0.2.103, committed manifest 0.2.105 (session-start banner, this
date).

FROZEN STATE: the commit that lands this file together with the
residue. Its sha is read by `git rev-parse` at dispatch and pasted
into every brief; no payload file moves until all three arms have
returned.

## Arms

Three fresh-context reviewers, all opus (the review tier; codex
excluded — review). Identical brief form: the diff command, the
full page, the standing where-to-press instruction, four questions
the previous desk left open (stated as questions, identical in all
three briefs), the read-only tail. They differ ONLY in scope:
- Arm W: the whole delta.
- Arm S1: the page — SKILL.md's diff, read against the tools it
  describes.
- Arm S2: the machine side — scripts, hooks, defaults, manifest,
  READINESS.json, with their batteries — read against the page.
The split is the repo's class-lane rule (conduct prose /
machine-read semantics), which is the rule on trial. It is by FILE
here where 2026-09-25 split one file by change; the two prior
reviews that split this way both converged on a page-vs-tool seam
from opposite sides, which is why each S arm is told to read
across.

## Pre-registered criterion

Carried UNCHANGED from 2026-09-25 so the two points compare.
Unit: UNIQUE SUBSTANCE findings (design substance; wording and
record findings excluded) attributable to a specific delta change,
deduped across arms.
- union(S1,S2) yields >= 2 unique substance findings W missed, and
  W yields < 2 the union missed: SPLIT WINS at this size.
- W yields >= the union's count with 0 union-unique findings W
  missed: WHOLE WINS at this size.
- Anything else: MIXED.
Reading across the two points (the size question, decided here and
not after the fact): SPLIT WINS here after MIXED-leaning-whole at
51 lines is evidence that coverage degrades with size, and the
class-lane rule stands with its first measured threshold between
the two sizes. WHOLE WINS or MIXED here means no degradation was
measured across a 14-fold size change, and the splitting rule is
re-derived on that basis at the close (st-85's stated consequence).
Secondary, recorded and never deciding: findings per lane-spend,
spend read from each arm's own transcript usage where available,
else its tool-call count.

Known limits, stated now: "same total spend" is not enforced, as
in the first run; n=1 per size; the desk dedups and attributes.
A dry run of the criterion against the first run's own figures
(union-unique 1, W-unique 0-1) returns MIXED, as recorded there.

## Conduct

- The arms never learn of each other, the probe, or the C4c test
  riding the same review (OBSERVATIONS, this date).
- All findings are dispositioned once, at this desk, before the
  release. One repair lap is budgeted (prose-mechanism content in
  the batch).
- Outcome and verdict land in an addendum to this file and in
  st-85's closure.

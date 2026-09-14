# Run 2 — GRADING PACKET (lc-109), frozen 2026-09-14

statiker-7e, created on statiker-e8's F1 finding against the run-2
pre-registration draft: §3b cited "the grading packet" and nothing in
the file CREATED one — no actor, no home, no moment. This file is the
packet, and its creation is the discharge.

**WHAT THIS IS.** The frozen baseline against which run 2's arms are
graded on column 2a. It exists because three separate things can move
the object out from under the grading and none of them announces
itself: the clone DELETES lc-109's block by construction, the live
lifecycle repo may close or amend lc-109 mid-run (pre-registration
§3e — lc-61 did exactly this during run 1), and my own desk grades
post-run from a context that will have compacted at least once.

**CONSUMER AND READ PATH.** Read by the grading desk (me, or a
successor) when run 2's arms return, and by the df-228 / run-2
review afterwards. It lives in the STATIKER repo, which is off every
arm's read path by construction — no arm is briefed with this repo,
no arm's clone contains it, and no arm learns this repo exists
(CLAUDE.md, carrier-on-read-path).

**SEALED.** Nothing here is amended after run 2's first arm
dispatches. A later correction appends a dated section and says what
it supersedes; it never edits the frozen body — an in-place edit
after dispatch would be the grading baseline moving under the arms it
grades.

---

## 1. PROVENANCE OF THIS READ

- Source: `Gunther-Schulz/lifecycle`, file `ITEMS.md`, block `## lc-109`.
- Commit: `2b41491` (`git -C .../lifecycle rev-parse --short HEAD`).
- `git status --porcelain -- ITEMS.md` → EMPTY. The block below is the
  committed content, not a dirty working copy.
- Read 2026-09-14 by statiker-7e, after this session's first
  compaction and under the trial's standing post-compact re-read
  discipline.
- Extraction command (whole block, no hand transcription):

      awk '/^## lc-109$/{f=1} f&&/^## /&&!/^## lc-109$/{exit} f' ITEMS.md

---

## 2. lc-109 — THE FULL BLOCK, VERBATIM

Reproduced exactly as the extraction returned it. Long lines are the
carrier's own; they are NOT re-wrapped, because a re-wrap is a
transformed view and this file exists to be the untransformed one.

```
## lc-109
grade: READY
requirement: the judgment register's OVERRIDE evidence is decided by a SUBSTRING MATCH OVER A RENDERED MESSAGE, so it can be written falsely by ordinary wording. verbs.py:820 reads 'if source == SOURCE_OPERATOR and "skips the veto" in message:' and on that basis writes record_use('intake-cost-test','overridden'). The phrase is prose from cost_test's own clear-message; any future clear-branch whose wording happens to contain it books a false override. That corrupts exactly the evidence the register exists to hold — fire-rate prices a rule's RETIREMENT, and a rule that looks overridden often is one whose predicate reads as wrong, so a false override argues for retiring a rule that never fired wrongly at all — record: surfaced by the lc-10 build lane's grounding round while it steered its own new wording around the phrase, 2026-09-13, verified at this desk at verbs.py:818-825
goal: enforce-the-invariants
write-set: plugin/cli/lifecycle_core/verbs.py,test/test_items.py
done-criterion: the override is decided by a VALUE the branch computes, not by text it renders — cost_test returns its verdict and its reason as separate parsed things (a verdict token, or an explicit overridden flag), and the caller branches on that token. The rendered message becomes display only and can be reworded freely without moving any register write. Red-first is cheap and exact: give the clear-branch a message containing the phrase 'skips the veto' under a NON-operator source and under an operator source, and show the register write today follows the TEXT rather than the state; after the change the same wordings write nothing and the state alone decides. MUST-NOT-MOVE: the genuine operator override still records 'overridden', the ordinary fire still records 'fired', and prove-rows' cost_test_veto and cost_test_unverified anchors stay byte-exact — they sit in the same function and lc-10 has just proven they can be worked around additively
evidence: VERIFIED AT THIS DESK 2026-09-13 by reading verbs.py:818-825: the FINDING branch returns first, then 'if source == SOURCE_OPERATOR and "skips the veto" in message:' guards the record_use(...,'overridden') call, with the phrase appearing in cost_test's operator-source clear message at verbs.py:372-374. This is the assertion-site shape the corpus names: a match over RENDERED text standing in for a comparison of parsed bodies, satisfied by any longer body that merely contains the fragment. The lane found it while choosing wording for its own new clear-branch and deliberately avoided the phrase rather than fixing it, which is correct — it was outside its write set's purpose — but the avoidance is a convention holding what a value comparison should hold, and the next author has no reason to know
blocked-by: NONE
```

### 2a. WHAT THE ARMS SEE, AND WHAT THEY DO NOT

- **SHOWN** to every arm, verbatim, as the brief's requirement: the
  `requirement:` slot only.
- **WITHHELD** from every arm: `done-criterion:` and `evidence:`. The
  clone deletes the whole block, so the withholding is structural
  rather than a matter of the brief's discretion.
- **`grade:` and `blocked-by:`** are arrangement facts, not object
  content; they establish the item was dispatchable, nothing more.

### 2b. THE GRADED SUBSTANCE — column 2a's scoring basis

Column 2a scores how much of the `done-criterion`'s SUBSTANCE the
arm's locked design independently reached. The substance decomposes
into four claims, listed so grading is against an enumeration rather
than an impression:

1. **The register write keys on a VALUE the branch computes**, not on
   text it renders.
2. **`cost_test` returns verdict and reason as separately parsed
   things** — a verdict token, or an explicit `overridden` flag.
3. **The caller branches on that token**, and the rendered message
   becomes display-only: rewordable freely without moving any
   register write. THIS IS THE DISCRIMINATING CLAUSE (see §4).
4. **MUST-NOT-MOVE holds**: the genuine operator override still
   records `overridden`, the ordinary fire still records `fired`, and
   the `cost_test_veto` / `cost_test_unverified` anchors stay
   byte-exact.

The `done-criterion` also names the RED-FIRST SHAPE, which is part of
the withheld baseline and is scored under column 3 rather than 2a:
give the clear-branch a message containing `skips the veto` under a
NON-operator source and under an operator source; show the register
write today follows the TEXT rather than the state; after the change
the same wordings write nothing and the state alone decides.

---

## 3. THE §3d PREMISES — commands and outputs

Executed by statiker-7e 2026-09-14 at `2b41491`, re-run AFTER this
session's compaction so the packet rests on post-compact reads rather
than on a summary's account of pre-compact ones.

### P-a. The defect is live, and the population is exactly two

```
$ grep -n 'skips the veto' plugin/cli/lifecycle_core/verbs.py
398:                         "the source is the operator, who skips the veto. "
848:    if source == SOURCE_OPERATOR and "skips the veto" in message:
```

Line 398 is the rendered prose inside `cost_test`; line 848 is the
guard that decides the register write. Two sites, one string, and
that is the whole defect.

### P-b. CONTROL for the population claim

```
$ grep -c 'skips the zzz-veto' plugin/cli/lifecycle_core/verbs.py
0
```

A near-identical pattern that must NOT match returns zero on the same
file under the same instrument. Without this, the two hits above
prove the expression parses, not that it discriminates.

### P-c. Reach — the phrase across the whole repo

```
$ grep -rl --no-ignore-files 'skips the veto' /home/g/dev/Gunther-Schulz/lifecycle
/home/g/dev/Gunther-Schulz/lifecycle/plugin/cli/lifecycle_core/verbs.py
/home/g/dev/Gunther-Schulz/lifecycle/ITEMS.md
```

Two files: the code, and the item's own body. `--no-ignore-files` is
mandatory here — the shell's `grep` is ugrep and honours ignore files,
so a bare search silently under-returns (corpus, environment module).
ITEMS.md is the item describing the defect, not a third instance.

### P-d. The mechanism the criterion demands ALREADY EXISTS upstream

`cost_test` returns `(token, message)` at FIVE return sites carrying
THREE distinct tokens — `clear` (`:382`, `:394`, `:397`), `unverified`
(`:388`), `veto` (`:400`) — spanning `verbs.py:382-406`. Verbatim, the
two sites that matter:

```python
    if source == SOURCE_OPERATOR:
        return "clear", ("cost test: one file, one hunk — DO IT NOW? — but "
                         "the source is the operator, who skips the veto. "
                         "The join above was not skipped and never is.")
```

And the caller, `verbs.py:840-854`:

```python
    if verdict == "unverified":
        out(f"COULD NOT VERIFY: {message}")
        return exits.COULD_NOT_VERIFY
    if verdict == "veto":
        judgment.record_use("intake-cost-test", "fired", repo=str(ctx.repo),
                            detail="veto")
        out(f"FINDING [cost_test_veto] {message}")
        return exits.FINDING
    if source == SOURCE_OPERATOR and "skips the veto" in message:
        # The operator's own override, which is exactly the evidence the
        # fire-rate review needs: a rule overridden often is one whose
        # predicate is wrong, and it is invisible unless the override is what
        # gets recorded rather than only the fire.
        judgment.record_use("intake-cost-test", "overridden",
                            repo=str(ctx.repo), detail="source=operator")
    out(message)
```

**THE STRUCTURAL FACT THIS ESTABLISHES**, and it is the sharpest thing
in the packet: the caller ALREADY branches on the token for two of the
three verdicts (`unverified` at `:840`, `veto` at `:843`). Only the
override, five lines further down at `:848`, falls back to the
substring. So the object is a genuine inconsistency INSIDE one
function — the mechanism the withheld criterion demands is already
present and in use immediately above the site that does not use it.
An arm that reads the caller at all has the answer in front of it;
that is what makes a LOW 2a score informative rather than unfair.

### P-e. Write-set resolves

```
plugin/cli/lifecycle_core/verbs.py    112199 bytes
test/test_items.py                     44294 bytes
```

Both declared paths exist. Two files — "small" on the same measure
run 1 used.

### P-f. The MUST-NOT-MOVE anchors are real and checkable

```
$ grep -rn --no-ignore-files 'cost_test_veto\|cost_test_unverified' \
      tools/prove-rows.py plugin/cli/lifecycle_core/refusals.py
tools/prove-rows.py:100:    ("cost_test_veto", "verbs.py",
tools/prove-rows.py:105:    ("cost_test_unverified", "verbs.py",
plugin/cli/lifecycle_core/refusals.py:923:        ident="cost_test_veto",
plugin/cli/lifecycle_core/refusals.py:937:        ident="cost_test_unverified",
```

Registered rows with prove-rows anchors. The criterion's regression
constraint is enforceable, not aspirational.

### P-g. The item's own pointers are STALE — kept deliberately

The `requirement:` slot cites `verbs.py:820`; the guard is at `:848`.
The `evidence:` slot cites `:818-825` and `:372-374`; the real sites
are `:848` and `:398`. Substance intact, line numbers drifted.

KEPT, NOT CORRECTED, in whatever the arms receive. A desk following
the pointer lands in unrelated code and must find the site by
reading. This is a minor grounding-literalism property and is
recorded as minor: **no column's score depends on it**, and it is not
the object's discriminator. It is written here so that a grader
meeting it post-run reads it as a registered property of the frozen
object rather than as a defect introduced by the arrangement.

---

## 4. THE DISCRIMINATOR — why the criterion is not readable from the requirement

Stated in the packet because column 2a's whole value rests on it, and
a grader reconstructing it from memory post-run would reconstruct it
wrong.

- **THE CHEAP FIX the requirement fully supports:** make the text
  comparison exact — hoist the message to a module constant and
  compare equality, or match a tighter sentinel. This answers the
  requirement's stated complaint COMPLETELY. "Any future clear-branch
  whose wording happens to contain it books a false override" stops
  being true. A desk proposing this has read the requirement well.

- **THE CRITERION REJECTS IT**, on clause 3 of §2b: the rendered
  message must become display-only and be "reworded freely without
  moving any register write". An equality against a constant FAILS
  that test — rewording the message still moves the register write,
  because the constant must be reworded in lockstep. The criterion
  demands the write be keyed to a computed VALUE so display and
  evidence decouple entirely.

**GRADING CONSEQUENCE.** Columns 1 and 2a must be able to come apart
here: an arm can declare [READY] on a decision-complete design (column
1 HIGH) whose substance the criterion scores at ZERO (column 2a). If
they cannot come apart on this object, they are one column wearing two
names, and THAT is a finding about the arrangement — recorded now, so
it cannot be explained away post-run.

---

## 5. THE PREMISE REGISTERED TO DIE

lc-109 may CLOSE or be amended in the live lifecycle repo before run 2
grades. lc-61 did exactly that during run 1.

This does not break the comparison and must not be allowed to look
like it does: the clone is frozen, so every arm faces the same object,
and **§2 of this file is the grading baseline whatever the live repo
later does**. A grader who finds lc-109 closed upstream grades against
this packet and records the upstream change as context, never as a
reason to re-score.

---

## 6. WHAT IS NOT IN THIS PACKET

- The brief. It is a separate artifact, frozen separately at the
  freeze gate, and audited there against the registration rule (a
  column is measurable only if the brief does not instruct the
  behaviour under test).
- The verify baseline. By decision it is a PROCEDURE measured on the
  reset clone tree before arm 1 dispatches, not a number pinned in
  advance — pre-registration §9.
- Any arm output. Nothing from a run exists yet; nothing has
  dispatched.

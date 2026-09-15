# Run 3 object candidates — DISCRIMINATOR PRE-REGISTRATION, 2026-09-14

Written and committed BEFORE any probe runs. statiker-53 desk, under
statiker-e8's drive, on the operator's delegation of this date.

## Why this document exists

Run 2's measured failure was not a model result. Its §4 discriminator
DID NOT DISCRIMINATE at any tier: all three unconditional arms reached
lc-109's withheld criterion independently, and none took the predicted
cheap fix. The column certified nothing, and the cost was a whole run.

The gap between an object's REQUIREMENT (what the arm is told) and its
WITHHELD CRITERION (what the grader holds back) was ASSUMED to be wide.
Nothing measured it before the arms spent. st-75's clause now forbids
that: the gap is "shown by a REGISTERED DISCRIMINATOR rather than
assumed".

This is that instrument, and it is deliberately cheap — one small
fresh context per candidate, run before the object is chosen, rather
than three desk arms run after.

## The instrument

For each candidate: a fresh context, cheapest tier, receives ONLY the
requirement text an arm would receive — no withheld criterion, no
hint that one exists, no statiker framing. It is asked what the
acceptance criterion for a correct fix should be.

## ADMISSIBILITY GATE — runs BEFORE either axis

Added 2026-09-15 by operator decision, on the C2 collision below. This
gate is not a measurement and produces no evidence: it decides whether
a candidate may be MEASURED AT ALL.

**A candidate whose write-set touches the statiker repo is
INADMISSIBLE. It is never graded on gap, on either axis, and never
enters the candidate set.**

The reason is the containment design's own founding sentence, which
every other part of the arrangement rests on — run-3
pre-registration, header lines 6-8:

> **THIS DOCUMENT CARRIES THE WITHHELD CRITERION AND NEVER TRAVELS TO
> AN ARM.** It lives in the statiker repo, which no arm clones, reads
> or is told exists.

Arms work in a clone of the OBJECT's repo (§5a freezes the packet from
the real repo; §5c clones it). So an object in the statiker repo puts
that repo in every arm's hands, and three independent disqualifiers
fire at once: the clone carries the withheld criterion, the grading
criteria and every trial record; the clone's own `CLAUDE.md` — which
the ceiling arm is MEASURED to load (run-3 pre-registration §3a.5b) —
announces the experiment and the arm's place in it; and where the
write-set includes `SKILL.md`, the arm edits its own conduct
specification as the object.

**THE INCIDENT, quoted because this gate exists only because nothing
asked the question.** C2 (st-71) was graded GAP DEMONSTRATED below and
carried as RESERVE, then ruled run 3's object on 2026-09-15 when C1
was refuted on axis 2 — and st-71's write-set is
`plugin/skills/statiker/scripts/statiker_record.py`,
`tools/test_statiker_record.py`,
`plugin/skills/statiker/SKILL.md`: three statiker paths. The pick was
stopped before it was recorded, by the executing desk reading the
header above against the write-set.

**WHY IT WAS INVISIBLE, which is the transferable half.** C1 satisfied
this constraint silently — a foreign-repo item — so the constraint was
never stated, so nothing checked it, and C2 was graded on gap alone
through a full candidates round and a reserve ruling. A constraint met
by accident is a constraint nobody wrote down. That is this program's
assumed-delivery shape, and this gate is its precipitate: a computable
predicate over the write-set slot, with near-zero false fires, which
is what earns a gate rather than prose.

## THE DECISION CRITERION, pre-registered

Reached only by candidates the admissibility gate ADMITS.

For each candidate, the WITHHELD CRITERION's discriminating half is
named below BEFORE the probe runs.

- **GAP DEMONSTRATED** (candidate stays eligible): the probe's answer
  does NOT contain that discriminating half.
- **GAP REFUTED** (candidate REJECTED): the probe produces that half
  independently — which is lc-109's failure caught for the price of one
  cheap context instead of one run.

A probe answer that is merely VAGUER than the withheld criterion does
NOT count as demonstrated: the test is whether the SUBSTANCE appears in
any wording, judged against the named half, not whether the phrasing
matches. Judged at this desk on a body-read of the raw answer, which is
recorded verbatim beside the verdict.

KNOWN BOUND, stated rather than discovered later: n=1 per candidate,
and one cheap context is not three desk arms. A demonstrated gap here
is NECESSARY, not sufficient — it refutes "the criterion is trivially
reachable" and does not prove the gap survives a top-tier desk. The
ceiling arm remains the instrument for that, and this probe's job is to
stop a candidate that would waste one.

## The candidates and their withheld criteria

### C1 — st-68, the lifecycle close/ready predicate inversion

REQUIREMENT the arm would get: `item close` records an ANSWERED
decision blocker as "never answered" and writes that inversion into the
durable ledger. Two predicates answer one question inside one tool and
the losing one owns the record. Fix it.

WITHHELD CRITERION, discriminating half: **a cross-question NEAR-MISS
must still record moot.** A ledger decision whose text differs from the
blocker by one clause must NOT clear it, because question-slot EQUALITY
is the contract and a looser match silently clears real blockers. (The
second half — that the fix must ASK the resolver `item ready` already
uses rather than re-implement it beside it — is the shape half, and
weaker as a discriminator because "reuse the existing resolver" is
ordinary engineering advice.)

WHY IT MIGHT DISCRIMINATE: the obvious fix is "make close consult the
ledger". Nothing in the requirement suggests that making the match
LOOSER is the dangerous direction, and a fuzzy or substring match is
the natural implementation.

### C2 — st-71, the tag-literal-in-body hold with no clearing route

REQUIREMENT the arm would get: a form defect on one tracker line can
turn into a terminal run failure, because the hold's code is
unexemptible by design and retro-gated by version. An arm of a real run
halted on exactly this with its design locked and sound. Design the
fix.

WITHHELD CRITERION, discriminating half: **the item OPENS ON A PROBE,
NOT A DESIGN, and the design BRANCHES on the probe's result.** The code
is owner-conditioned, so: run a tracker carrying an undefanged literal
through sweep, then supersede or invalidate the OWNING entry and re-run.
If the hold DROPS there is already a clearing route and this is a
DOCUMENTATION gap with no tool change; if it STANDS the class is real
and needs a sanctioned route. Designing before probing picks a branch
by luck.

WHY IT MIGHT DISCRIMINATE: the requirement reads as a design task and
names a real cost, which invites a design. Deriving "do not design yet,
one unrun check decides which of two different items this is" requires
noticing the owner-conditioning, which the requirement does not mention.

NOTE ON FIT, recorded because it cuts both ways: this candidate's
withheld criterion is METHODOLOGICAL — probe before designing — which
is statiker's own tenet 1. That makes it the sharpest test of whether
the SKILL changes conduct, and also the candidate most likely to be
reached by a desk running the skill, which is the ceiling-gate risk.

### C3 — st-66, the post-closure population as a verdict field

REQUIREMENT the arm would get: the verify brief demands a statement per
F/D/R line appended after the last resolved A-line, but no verdict field
carries that set, so the one demand whose input the page's own standard
would put in a verdict is derived by hand instead.

WITHHELD CRITERION, discriminating half: **the MUST-NOT-MOVE — green on
a tracker with NO post-closure lines, so the new field does not fire on
ordinary runs** — together with the legitimacy of the OTHER disposition
entirely: recording why this demand is the exception to the page's
tool-finds-them standard, minting nothing.

WHY IT MIGHT DISCRIMINATE: the requirement is phrased as a gap, which
invites minting the field. That a recorded exception is an equally
correct answer, and that the new field must be proven NOT to fire on
ordinary runs, are both absent from the requirement's framing.

## What happens to the result

Every probe's raw answer is recorded verbatim beside its verdict in the
candidates round, whichever way it lands. A REFUTED candidate is
reported as refuted — that is the instrument working, and suppressing it
would reproduce run 2's error at one remove.

# Comparand: syv-ai/agentic-coding-playbook skills, read 2026-11-06

Source: shallow clone at `~/dev/reference/agentic-coding-playbook`.
It was pointed to in a public comment on the EGM launch ("EGM is too
rigid"). Files read: skills/README.md, work-autonomously/SKILL.md and
DECISIONS.md, executing-plans/SKILL.md, receiving-code-review/SKILL.md,
retro/SKILL.md. Attribution: built from Matt Pocock's skills and the
Superpowers plugin (skills/ATTRIBUTION.md, not read in full).

## Shape (observed)

19 skills, 1363 SKILL.md lines in total, the largest 115 lines
(`wc -l skills/*/SKILL.md`). The skills split by task and point to one
another. Detail sits in reference files beside each skill (for example
improve-code-design/FAMILIES.md). There is no record grammar, no
gates and no tool-backed checks. It trusts the executor.

## What bears on st-99

1. **One review, then triage, with no second round**
   (executing-plans §4). A single fresh-context review of the diff
   against the plan and the spec. The reviewer reports "only gaps that
   affect correctness or the requirements". Critical and Important
   findings are fixed, each with a test that fails first. Minor
   findings are deferred. The skill states the reason outright: "A
   reviewer asked to find gaps will usually report some even when the
   work is sound." Derived: this is the most radical form of st-99's
   stop rule. Repairs prove themselves by their own red-first tests,
   not by another attack round.
2. **"Declined to judge."** The reviewer lists every behaviour it set
   aside as out of scope, one line each with its reason, and the author
   decides each line. Statiker names exactly this blind spot ("the desk
   cannot know what a fresh context declined to exercise", SKILL.md
   ~1834) but has no return slot for it.
3. **Severity re-grade by user impact, in both directions.** "The
   reviewer's severity is advice". A finding marked minor can still be
   required, for example a crash on an input the spec never mentions.
   This is the opposite of EGM's no-downgrade rule.
4. **Decision log entries carry "cost if wrong"**
   (work-autonomously/DECISIONS.md: cheap / moderate / expensive, what
   the user would get, what undoing it involves) plus a [provisional]
   mark. Statiker's D-lines carry a basis but no cost. A cost slot
   would give st-99's stakes-scaled bar something to read.
5. **Lessons go to checks, not to the always-loaded page**
   (retro §2). "The instructions file loads into every session, so a
   repeated mistake rarely earns a new line there". The order is a
   failing check, then a review standard read at review time, and
   "the instructions file is mainly for pointers". It also names its
   own limit: it "never prunes old checks". This matches st-99
   change 4 and the accretion problem.
6. **Two failed attempts at the same fix → stop and hand off to a
   fresh session** (executing-plans §2). Statiker has the narrowing
   route and the breaker for this.

## NON-STEAL

The executor-trust posture as a whole: no forcing points, no record
the round can read, no isolated verify. The pstack NON-STEAL reading
applies (PLAN.md 2026-09-10): most of the compression is bought by
trusting the executor. Statiker's premise is that conduct needs the
forcing points.

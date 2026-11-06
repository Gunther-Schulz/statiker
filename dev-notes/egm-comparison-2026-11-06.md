# Comparand: google/elephant-goldfish-model (EGM), read 2026-11-06

Source: shallow clone at `~/dev/reference/elephant-goldfish-model`
(files read: README.md, skills/egm-review/SKILL.md,
skills/egm-review-loop/SKILL.md, skills/egm-resolve/SKILL.md:55-90,
agents/comprehension.md, agents/synthesizer.md).

## What it is (observed)

A multi-harness plugin (Claude Code, Codex, Cursor, Antigravity,
OpenCode). It splits roles into an "Elephant" (the author context that
drafts the design doc) and "Goldfish" reviewers (fresh subagents that
read only the doc plus a reading list). Pipeline: brainstorm → draft →
a 5-stage review (zoom-out, comprehension, critic, zoom-out again,
implementation readiness) → resolve. There are about 9 lens personas,
optionally two instances of each, behind a synthesizer.

## Fit with statiker (derived)

- Same thesis as statiker's attack forcing point: self-blindness is
  caught by a context that lacks the author's history.
- It reviews DOCUMENTS only. Reviewers are read-only and execute
  nothing. There is no run record, no lock sha, no executed probe in a
  worktree, no implement/verify phase. Statiker's attacker executes
  inside a worktree at the lock sha (SKILL.md ~1273).
- NON-STEAL: the convergence rule "two consecutive clean rounds, cap 5"
  (egm-review-loop Step 2.4), and the many-lens swarm per round. Both
  contradict the economics lens (CLAUDE.md: every round after the first
  owes a reason, and a zero-delta second round is evidence that one
  round suffices).
- Already covered here: churn ("a new finding at a fix's scope that
  reverting would resolve") corresponds to the repair-eating series
  shape (SKILL.md ~1330).

## Candidates (no incident, so no mint under birth-class)

1. **Paraphrase-back.** The comprehension reviewer first writes what
   the doc proposes and how the system works per the doc. The author
   compares that with intent, and a wrong paraphrase is a finding.
   agents/comprehension.md states the mechanism: a list of undefined
   terms cannot find a doc whose terms are all defined but whose parts
   do not connect. Statiker's page has no such step (grep `paraphras`
   in SKILL.md hits only the drift sense, at lines 1109/1447/1524).
   Re-open trigger: an attack that missed a design-fit-to-intent defect
   which a paraphrase-back would have exposed.
2. **Contest must be readable-by-the-reviewer.** A CONTEST cites
   evidence the reviewer could have read. Evidence outside the
   reviewer's reach goes to ESCALATE, and the author does not add
   context only to satisfy a zero-context reviewer
   (egm-resolve:58-81). Not checked against statiker's disposition
   grammar. This is unverified as a gap.

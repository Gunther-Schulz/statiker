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
- Stop shape (egm-review-loop Step 2.4; egm-review "Pause & Resume"):
  three loop stops. CONVERGED is two consecutive clean rounds, where a
  clean round has no unsettled Blocker/Major, Nits do not block, and a
  reviewer that did not run makes the round unclean. CHURN is a new
  finding at an applied fix's scope that reverting the fix would
  resolve. CAP is 5 rounds. Cap and churn are SOFT: they list the open
  findings and ask the user to accept, continue past the cap, or return
  to drafting. Each round also starts only on user confirmation. The one
  HARD cap is per stage in egm-review: at most 1 re-audit. A further
  request records the residuals as "accepted trade-offs" and
  auto-advances, so the cap itself grants acceptance. Compared with
  statiker (SKILL.md 415-470, 1325-1351): churn matches the founding
  non-contracting shape, but EGM's response is to ask the user, where
  statiker narrows. EGM has no trend reading (counts falling while
  findings sit in the newest repairs) and does not require a cause when
  the cap fires. Its "settled list" (a contested or accepted finding is
  not re-opened when a later fresh reviewer raises it again) answers
  sampling noise ("a round with zero findings is rare even when the
  document improves").
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
   Adapted shape (statiker runs unattended by default, SKILL.md 390, so
   the operator is not the comparer): the attacker's paraphrase is
   compared by the desk against the RECORDED intent and R-lines, never
   against desk memory. Only an intent question goes to the operator,
   through the existing route. Candidate 2 adapts the same way: in
   statiker, "evidence the reviewer could read" means the record or the
   repo, so a dismissal cites one of them or the reason is first written
   into the record.
   Re-open trigger: an attack that missed a design-fit-to-intent defect
   which a paraphrase-back would have exposed.
2. **Contest must be readable-by-the-reviewer.** A CONTEST cites
   evidence the reviewer could have read. Evidence outside the
   reviewer's reach goes to ESCALATE, and the author does not add
   context only to satisfy a zero-context reviewer
   (egm-resolve:58-81). Partly checked 2026-11-06, grep-based only:
   every statiker F-line carries a basis (SKILL.md 687-689), but no
   passage found requires that a dismissal's basis be something the
   attacker could read, and none found splits off ESCALATE.

# statiker — repo guidance

- **Single-home by design.** `plugin/skills/statiker/SKILL.md` is the
  only home of the operational text — no spec layer, no render chain
  (a recorded design decision and a live experiment for the
  framework-legitimacy question; PLAN.md, Single-home by design).
  Edits target it directly, under skill-craft discipline (invoke the
  skill-craft skill before editing).
- **Birth-class discipline.** The payload is enforcement structure +
  bindings only; every future addition is a fire-born patch carrying
  incident provenance, logged in `dev-notes/OBSERVATIONS.md`. No
  provenance, no patch.
- **PLAN.md is the design record** — settled decisions are not
  re-opened without new evidence.
- **A release during a live run means the desk session restarts.**
  A version bump never reaches a running desk: the pin resolves at
  session start, and a mid-run `/reload-plugins` fixes only future
  injections — the OLD skill text already sits loaded in the desk's
  context, owning its conduct. On release with a run in flight,
  abandon the desk and start it fresh (the tracker is the handoff by
  design); the fresh desk confirms its served version from the Skill
  injection's base-directory line before the next forcing point.
  The pin moves only at a seam — a recorded A-line or forcing-point
  boundary, never while an attacker or unit is live (commits may
  land anytime; the pin is the release).

## Trial working conventions (operator-settled, 2026-08-06)

- **Two-session layout.** The meta/grading session runs in THIS
  repo (grades comparisons, mints, releases); the desk runs in the
  target repo. Decisions travel between them only via operator
  relay — the meta session ends its turn with the paste-ready relay
  line (carrier-on-read-path: the desk reads its tracker and the
  operator's replies, never this repo's ledger).
- **Mid-run tuning at seams.** Between cycles is an upgrade point,
  not a wait: grade what is evidence-complete (field-tested in-run
  with provenance = ripe; needs the run's remainder = defer), mint,
  release — the running desk finishes its round on the old version,
  the fresh desk picks up the new one at the seam.
- **Comparison experiments pre-register.** The decision criterion
  is recorded in dev-notes BEFORE any arm dispatches; arms are
  graded post-run in the meta session on a body-read of the raw
  reports — the desk records verbatim and never grades the arms.
- **Trial-phase dispatch confirmation.** Attack, implementation,
  and fable dispatches present individually, model named, and wait
  for the operator's go — never a second dispatch batched behind
  one confirmation. Read-only discovery legs at opus or below are
  PRE-AUTHORIZED: dispatched without asking, named in the turn's
  report. (Narrowed 2026-08-06 from the blanket rule after it
  priced dispatches at one blocking round-trip each and pushed
  discovery into the ungated inline lane — the blanket rule
  reduced the oversight it existed to buy. Revisit at
  stabilization.)
- **Desk interrogation is cheap — ask when it informs the skill.**
  Diagnostic questions relayed to the running desk (which rule
  routed a conduct call — quote it or say "improvised"; what a
  check went red on) are a first-class mint source: one question
  completing a failure triage beats reconstructing the desk's
  reasoning from repo state. Contamination is a non-cost: a
  question that would taint the desk's conduct (reveal meta-layer
  framing, lead its judgment) costs at most one desk — harvest the
  answer, abandon the session, restart fresh from the tracker at
  the seam. Prefer what/which-shaped questions; post-hoc
  why-shaped answers decay into rationalization.

## Verify

```bash
awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'
                                # operational (non-blank body) lines;
                                # must be ≤ ~150 (PLAN.md size target)
ls plugin/skills/                # payload inventory: statiker only
```

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

## Verify

```bash
awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'
                                # operational (non-blank body) lines;
                                # must be ≤ ~150 (PLAN.md size target)
ls plugin/skills/                # payload inventory: statiker only
```

# Statiker

A thin design/investigation skill for Claude Code: certify the
design will bear load *before* construction (the name is German —
the structural engineer who signs off on load-bearing calculations).

A development task runs as a free investigation/design loop — no
fixed cycles, no ceremony — held by five forcing points:

1. **Decision record** — append-only tracker, every decision with
   its basis.
2. **One fresh-context attack** on the locked design; iterate only
   if it bites.
3. **[READY] = dispatchable** — the design is done when a
   decision-complete brief could be written from it.
4. **Implementation makes no design decisions** — gaps surface,
   never bridge.
5. **Verify = executed, isolated, against the recorded
   requirement.**

Status: **trial**. Statiker is the designated successor to
[clippy](https://github.com/Gunther-Schulz/coding-clippy) and is
being validated on real development work; clippy remains the stable
tool meanwhile. Design rationale and succession plan: `PLAN.md`.

Note: statiker deliberately composes with its author's installed
stack (the dispatch-guards plugin, an operator instruction corpus)
and cites those rather than restating them — a public extraction
would inline what it cites. See `PLAN.md`, Ecosystem composition.

## Install

```
claude plugin marketplace add Gunther-Schulz/statiker
claude plugin install statiker@statiker
```

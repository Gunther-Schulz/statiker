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

Note: statiker composes with the dispatch-guards plugin and, where
present, an operator instruction corpus — citing rather than
restating them. The corpus's performance-bearing evidence ethics
ship distilled as the skill's `references/evidence.md` for stacks
without one. See `PLAN.md`, Ecosystem composition.

## Model defaults — the certified-attack register

The fresh-context attack round resolves its model as a role: your
repo's `clippy.config/models` (`attack:` class) wins; else the
first dispatchable entry of the shipped register
(`plugin/skills/statiker/defaults/models`); else
strongest-available, running as a declared deviation. Register
entries carry certification evidence (a probe against a known
ceiling — "probe-then-certify", `PLAN.md`). Contributions welcome
by PR: an entry lands only with its probe record attached — no
provenance, no entry. Other ecosystems (Codex etc.) extend the
same file once a certified probe exists there.

## Install

```
claude plugin marketplace add Gunther-Schulz/statiker
claude plugin install statiker@statiker
```

Statiker composes with the public
[dispatch-guards](https://github.com/Gunther-Schulz/dispatch-guards)
plugin (brief and report forms; a hook enforces its load before any
dispatch) — install it alongside:

```
claude plugin marketplace add Gunther-Schulz/dispatch-guards
claude plugin install dispatch-guards@dispatch-guards-marketplace
```

No operator instruction corpus is required: where none exists, the
skill reads its shipped `references/evidence.md` (the distilled
evidence ethics) in its place.

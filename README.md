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

## Running statiker on Codex

**Read this first: a codex-only desk has to run with NO SANDBOX.**
`--sandbox danger-full-access` is not a relaxed sandbox setting, it
is the absence of one — the model's commands reach your whole
filesystem with your own permissions, for the entire session. That
is not a footnote to the setup, it is the setup's first fact.

Why the mode needs it: statiker's record is a git transaction log.
The run lock, every unit START and COMMIT, the pinned attack
artifact — all of it is commits, and codex's `workspace-write`
sandbox denies writes to `.git` (measured: `workspace-write` fails
on `.git/index.lock`, "Read-only file system"; the same commit
succeeds unsandboxed and under `danger-full-access`). So the
machinery that makes the forcing points binding is exactly the
machinery the safe sandbox blocks. Run it in a throwaway clone or a
container, never against a working copy you cannot lose.

**And cut the clone's remote.** A clone keeps `origin` pointing at the
repo it came from, and with no sandbox the desk holds your own push
rights — so the "throwaway" copy still has a live path back into the
original. `git remote remove origin` in the clone, verified with `git
remote -v`, before the desk starts. Measured 2026-09-13: the first
clone cut for a scoped codex run carried its origin, and nothing in
the setup would have reported it.

Two further facts a codex stack must supply by hand, because Claude
Code's skill system supplies them and codex has none:

- **The page.** There is no skill injection, so the desk is handed
  `plugin/skills/statiker/SKILL.md` directly, along with the
  directory holding `scripts/` and `defaults/`. Measured: a codex
  desk given the payload path and nothing else resolves the tools
  from the page's own text and runs them correctly.
- **The version.** `plugin.json` sits outside the skill directory,
  so a payload-only install carries no version source at all — and
  the record's `Skill: statiker <version>` header, plus the resume
  check that compares it against the served version, both read from
  it. Supply the version explicitly, or that check cannot evaluate.

**Status: not certified end to end.** Measured per role on this
repo's own probes: read-side and attack are certified, the reviewer
role is EXCLUDED BY MEASUREMENT, and the verify leg is safe but
substantially weaker than any Claude tier — codex does not fabricate
coverage there, it simply resolves fewer requirements. Per-role
detail and the evidence behind each cell:
`plugin/skills/statiker/defaults/models`.

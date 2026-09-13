# st-53 — wan2gp as the worked case for the verification-skill generator (raw lane findings)

Provenance: sonnet lane sonnet-wan2gp-case, 2026-09-13, statiker desk session 1b204567; read against pstack create-verification-skill + archived Pt.1. Lane's stated gap: docs/directives/ (~75 files) sampled by grep, not opened individually.
Consumer: PLAN consideration 5's build-vs-adapt fork (verdict recorded there this date); the future generator-skill design.

---

# st-53 read-only findings — wan2gp worked case vs pstack generator

Sources opened in full: pstack `create-verification-skill/SKILL.md`;
`statiker/dev-notes/poteto-guide-pt1-2026-08-31.md`; in `~/wan2gp`: `CLAUDE.md`
(all section headers via `grep -n "^#"`, then read lines 57-156, 397-467),
`docs/runbooks/testing-generation-effects.md` (full), `docs/storage-root.md`
(lines 955-984, 1535-1574), `BEGEHUNG-MAP.md` (grep hits), `.claude/settings.local.json`
(full), plus `ls`/`find` over `tools/`, `scripts/`, `tests/`, `docs/`, and
`head`/`grep` on `tools/wgp_launch.py`, `tools/check_gallery_bridge.py`,
`tools/check_plugin_env_wiring.py`, `scripts/kill-wan2gp.sh`, `run-wan2gp-conda.sh`.

## 1. Which of the five axes (surface/run/drive/observe/isolate) wan2gp answers vs. never asks

- **Run — answered, heavily.** `run-wan2gp-conda.sh` (211KB) + `tools/wgp_launch.py`
  are the launch layer; `DEFAULT_SERVER_PORT="7862"` (`run-wan2gp-conda.sh:282`).
  `CLAUDE.md:98-146` ("Reaching into an app") is a whole discipline about what
  the launcher assumes about upstream at start time.
- **Drive — never built as a scripted CLI.** `.claude/settings.local.json:32-33`
  allows only `mcp__playwright__browser_navigate` and
  `mcp__playwright__browser_evaluate` — ad hoc Playwright MCP, not a
  `control-wan2gp` verb set. `docs/runbooks/testing-generation-effects.md:52-65`
  distrusts the UI itself for reading state back ("Read settings from the
  ARTIFACT, never from the UI... The UI has lied twice... a form helper
  reported success while writing nothing").
- **Observe — answered narrowly, per-incident, never generally.**
  `tools/check_gallery_bridge.py:1-24` hits a running server's `/config` (same
  doc the browser builds the UI from) for one specific wiring defect, with a
  positive control; `ffprobe -show_entries format_tags=comment` reads render
  metadata (`testing-generation-effects.md:54`); `nvidia-smi
  --query-compute-apps` reads GPU state (`CLAUDE.md:455`). But there is no
  scripted screenshot/console capture: `docs/storage-root.md:967` and `:1552`
  both describe the app console as "screenshotted and pasted into chats" —
  found by the *operator* pasting their own terminal, "not by any guard here"
  (`:1553`).
- **Isolate — never asked as a design question.** No ports/data-dirs/profiles
  scheme for running two verification instances side by side. What exists
  instead is a social/process convention: `CLAUDE.md:441-461` ("Closing a
  session") — check `ListAgents` and `nvidia-smi` before killing an app another
  live peer might be mid-render on. That is "don't collide with a peer," not
  "how do two isolated instances coexist."
- **Surface — never named as a question either**, because there are four of
  them and the repo's whole framing is that it doesn't own any of their
  source: `CLAUDE.md:3`, "This repo is the launcher layer for four
  applications it does not own."

## 2. What form tooling took with no prescribed CLI

Two forms, both flat, neither verb-dispatched:

- ~40 standalone one-off Python scripts directly under `tools/`
  (`check_gallery_bridge.py`, `check_plugin_env_wiring.py`,
  `check_enhancer_prompts.py`, etc.), each invoked by path, each with its own
  **three-way exit code** convention baked in individually — e.g.
  `check_gallery_bridge.py:24` "Exit: 0 all checks passed, 1 a check failed, 2
  could not verify"; `check_plugin_env_wiring.py:8` "0 every read is wired 1 a
  read nobody writes 2 could not verify."
- 39 shell scripts under `tests/`, run via a bare loop, not a runner:
  `CLAUDE.md:69-71` `for t in tests/*.sh; do echo "== $t"; bash "$t" ||
  echo "FAILED: $t"; done`.

No `doctor`/`snapshot`/`send`/`press` subcommand surface anywhere;
`kill-wan2gp.sh` (full file read) kills by `pkill -f "python.*wgp.py"` —
process-name pattern, not a tracked PID from what it started.

## 3. Nothing plays the feature map's role

`BEGEHUNG-MAP.md` is the closest analog and it is a *different* artifact: one
row per (claim-emission surface × failure class), each graded
dark/guarded/prose with a date and finding id (`BEGEHUNG-MAP.md:22-34`, e.g.
row 18 on the enhancer-prompt wiring, row 19 on console prompt-leak). It
answers "what's guarded against what silent failure," never "how do I reach
and drive feature X, what's its selector, what breaks."
`docs/runbooks/testing-generation-effects.md` is the other candidate and it's
an experiment-methodology runbook (baselines, controls, instrument-proving),
not a route/selector/gotcha enumeration. No file anywhere lists drivable UI
surfaces with routes + gotchas — this is a piece ad hoc growth never
produced. Inferred from absence (no hits for "feature.map|control-" combined
with drivable-surface language in CLAUDE.md/docs/BEGEHUNG-MAP.md); could not
exhaustively grep every one of the ~75 `docs/directives/*` files, so a
directive-buried exception is possible but unlikely given none surfaced under
"feature", "surface", or "gotcha" greps.

## 4. What a generator's interview would need to ask here that the Electron/Atlas set doesn't

The pstack SKILL.md's five axes (`SKILL.md:15-19`) assume one app, one
surface, one owned codebase, one instance question ("can two instances run
side by side"). Wan2GP's repo is structurally different on axes the interview
has no slot for:

- **Multiple unrelated upstream apps sharing one machine's GPU/ports**, none
  of which this repo owns the source of (`CLAUDE.md:3`) — the interview's
  "surface" question is singular; here it's "which of four, and do the others
  collide."
- **Driving it must not create an unmergeable working-tree diff** in the
  upstream checkout the launcher `git pull --ff-only`s (`CLAUDE.md:103-105,
  123-128`) — a constraint the Electron template has no reason to carry.
- **Isolation is GPU-residency and live-render exclusivity, not
  ports/data-dirs** — the actual convention that exists (`CLAUDE.md:441-458`)
  is "ask a live peer before you kill/relaunch," which the template's isolate
  question (ports, profiles) doesn't cover at all.
- **Evidence cannot be trusted to a single automated verdict for A/V
  quality** — the repo's own standing operator rule after two false-clean
  incidents: "any render whose quality is part of a claim ships with an
  explicit request for the operator to review it"
  (`testing-generation-effects.md:143-145`); the template's "Evidence" axis
  (`SKILL.md:30`) has no slot for "and then a human must still look."
- **The generated artifact under test is itself the experiment** — most of
  wan2gp's real verification discipline is scientific-method rigor
  (baseline-before-crediting, pre-registered criteria, one-variable-per-pair,
  prove-the-instrument) — `testing-generation-effects.md` in full — which is a
  sixth axis (experiment design) the pstack interview doesn't ask about at
  all.

## Gap, not bridged

Did not open any of the ~75 files under `docs/directives/` individually
(sampled by filename/grep only), so a directive containing a more CLI-like or
feature-map-like artifact than what surfaced above is a named unknown, not
ruled out.

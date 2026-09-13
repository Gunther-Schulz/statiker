# Raw evidence — noodle inventory table (pilot lap, sonnet lane, 2026-09-13)
Provenance: sonnet-noodle-brainmax lane, statiker desk 1b204567; noodle HEAD 82d2921.

# Noodle repo inventory — pilot sample probe
HEAD read: 82d2921c52370f23f29086de81ccfb600939c037 (2026-03-19)
Repo totals (verified): 678 .md files, 46,329 md lines total (find . -name "*.md" | wc -l / cat | wc -l — matches the brief's stated size exactly).

Per-directory: file count | md-line count | go-line count | grading | evidence

adapter        | 11  | 66    | 376   | SUBSTANTIVE — hand-written Go backlog-sync bridge + 2 test files, brain note "backlog-sync-parse-errors-are-recoverable-warnings" cross-references it
adapters       | 2   | 5     | 368   | SUBSTANTIVE (project-local, not shipped) — README.md says explicitly "This is not part of Noodle itself... Noodle's own backlog adapters" (adapters/README.md:1-3)
.agents        | 114 | 9960  | 0     | MIXED: 27/29 skills SUBSTANTIVE hand-written (noodle, schedule, quality, reflect, meditate, brain, execute, review, testing, commit, worktree, debugging, oops, todo, refine, adversarial-review, codex, find-skills, ast-grep, go/react/ts-best-practices, interaction-design, make-interfaces-feel-better, unslop, ruminate, plan) + 2/29 VENDORED (frontend-design, skill-creator — both carry their own LICENSE.txt, matching docs/thinking-in-noodle.md's instruction to `npx skills add https://github.com/anthropics/skills --skill skill-creator`) + 3 hook scripts (hand-written, byte-diffed against brainmaxxing's)
brain          | 470 | 28940 | 0     | MIXED, dominant SUBSTANTIVE-HISTORICAL: brain/archive/plans alone = 351 files / 23,769 md lines (completed/superseded plans — historical record, not live doctrine); brain/plans (active, non-archived) = 64 files; brain/codebase = 34 files/532 lines (live gotcha notes, hand-written, e.g. provider-routing-must-fail-loudly.md, worktree-gotchas.md); brain/principles = 16 files, byte-identical in content to brainmaxxing's principle set
.claude        | 1   | 0     | 0     | CONFIG (settings.json-shaped, not inspected — outside brief scope)
cmdmeta        | 1   | 0     | 77    | SUBSTANTIVE (single Go file, CLI metadata)
.codex         | 1   | 0     | 0     | CONFIG, not inspected
config         | 4   | 0     | 1432  | SUBSTANTIVE — .noodle.toml loader/validator, 1/4 files is a test
defaults       | 4   | 0     | 0     | SUBSTANTIVE — 4 POSIX shell adapter scripts (backlog-add/done/edit/sync), read in full (backlog-add: mechanical sed/awk text mutation over todos.md, no LLM call)
dispatcher     | 38  | 77    | 4414  | SUBSTANTIVE — session lifecycle Go package, 11/32 go files are _test.go; read controller.go (AgentController interface) and types.go (DispatchRequest/Session/SessionEvent) in full
docs           | 32  | 1818  | 0     | SUBSTANTIVE (VitePress doc site) — read index.md (frontmatter-only custom homepage), introduction.md, thinking-in-noodle.md in full; concepts/*.md and cookbook/*.md NOT read (out of brief's "index or architecture overview" scope)
e2e            | 7   | 0     | 1353  | TEST — 4/4 go files are _test.go
event          | 28  | 138   | 1328  | SUBSTANTIVE + TEST fixtures — 10 go (4 test) + 12 json (test fixtures, per brain/codebase/fixture-directories.md) + 6 md notes
examples       | 14  | 251   | 0     | SUBSTANTIVE (example project scaffolds: minimal/, multi-skill/, each with .noodle.toml + README)
generate       | 3   | 0     | 273   | SUBSTANTIVE — codegen tool (tygo wrapper per architecture.md), 1/3 test
.githooks      | 1   | 0     | 0     | CONFIG, not inspected
.github        | 6   | 0     | 0     | CONFIG (issue templates/workflows), not inspected
internal       | 156 | 1430  | 16837 | SUBSTANTIVE + TEST fixtures — 85 go (26 test), 57 json fixtures, 9 md notes; this is the largest Go package cluster (orderx, taskreg, state, ingest, reducer, dispatch, mode, projection, rtcap, snapshot, statever per architecture.md table)
loop           | 207 | 718   | 20356 | SUBSTANTIVE + TEST fixtures — largest package (main event loop, per architecture.md); 78 go (37 test), 74 json + 21 toml fixtures (per brain/codebase/fixture-directories.md and loop-test-overlap-matrix.md), 25 md
mise           | 4   | 0     | 742   | SUBSTANTIVE — context-gathering "brief builder", 1/4 test
monitor        | 25  | 135   | 1867  | SUBSTANTIVE — session health/stuck-detection, 6/16 go are test
parse          | 33  | 179   | 1591  | SUBSTANTIVE — provider NDJSON parsing (Claude/Codex → canonical events), 3/13 test
prototype      | 9   | 0     | 0     | SUBSTANTIVE-BUT-STALE artifact — static HTML/JS/CSS mockups (deploy.html, review.html, tree.html etc.) predating the current React/TS ui/; not linked from README/CLAUDE.md/architecture.md
runtime        | 5   | 0     | 637   | SUBSTANTIVE — Runtime interface abstraction (Dispatch/Kill/Recover per architecture.md), 2/5 test
scripts        | 9   | 0     | 321   | SUBSTANTIVE tooling — release.mjs, lint-arch.sh, sandbox.sh, repo-size-charts.go, fixturehash/ — build/release/dev mechanics, no test files
server         | 9   | 0     | 1921  | SUBSTANTIVE — Web UI backend (WebSocket streaming per architecture.md), 3/8 test
skill          | 6   | 0     | 1265  | SUBSTANTIVE — skill resolution/frontmatter parsing, 3/6 test
skills         | 18  | 0(*)  | 0     | VENDORED — top-level skills/skill-creator/ is the full upstream anthropics/skills skill-creator package (own LICENSE.txt, agents/, eval-viewer/, scripts/*.py) — a SECOND, separate copy from .agents/skills/skill-creator; (*) its SKILL.md alone is 479 lines, present in repo-wide totals under .md but this dir's own tree also holds .py/.html files not counted as md
stamp          | 9   | 66    | 487   | SUBSTANTIVE — NDJSON timestamp sidecar processor, 2/3 test
startup        | 3   | 0     | 428   | SUBSTANTIVE — first-run project scaffolding (brain/, .noodle/ per architecture.md), 2/3 test
ui             | 76  | 0     | 0(*)  | SUBSTANTIVE (React/TS, not Go) — 46 tsx + 20 ts; 2 files carry a "// Code generated" marker (tygo-generated API types per architecture.md's codegen line), rest hand-written
.vscode        | 1   | 0     | 0     | CONFIG, not inspected

Grading legend: SUBSTANTIVE = hand-written operational/doctrine content; GENERATED = templated/codegen; VENDORED = copied from an external upstream package; TEST = test-only content.

Sizing note for a full second lap: brain/archive (351 files, 23,769 lines — over half the repo's total md volume) is historical/superseded and arguably skippable for a "current doctrine" read; brain/plans (64, active) + brain/codebase (34) + brain/principles (16) + the spine files already read are the live-doctrine surface, on the order of ~150 files / ~3-4k lines — a second lap sized to LIVE content only, excluding archive, is far cheaper than the raw 678/46k headline suggests.

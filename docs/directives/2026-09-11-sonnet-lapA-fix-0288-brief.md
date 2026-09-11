# Title: sonnet: 0.2.88 repair lap — opus-review-0288 dispositions (B1, B2, N1, G4-tool, n1–n7)

Dispatcher: statiker-4d, 2026-09-11. Lane name: sonnet-lapA-fix-0288.
Working copy: /home/g/dev/Gunther-Schulz/statiker.
Base check: `git merge-base --is-ancestor <base> HEAD` AND
`git log --oneline <base>..HEAD` where `<base>` is the commit that
added THIS brief file (find it: `git log -1 --format=%h --
docs/directives/2026-09-11-sonnet-lapA-fix-0288-brief.md`). Base
contained + nothing on top touching your owned paths = clean start; then
`git status --porcelain` over your owned paths must be empty. Otherwise
HALT and report. Desk commits touching only ITEMS.md, LEDGER.md,
dev-notes/ or docs/ are not a halt.
Scratch: `/tmp/claude-1000/-home-g-dev-Gunther-Schulz-statiker/f59bcaca-7615-4029-95ca-3a049796cc24/scratchpad/sonnet-lapA-fix-0288/`
— that directory only (the scratch root is shared with other lanes),
never this repo.

## Grounding basis — read before building; the report cites what was actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST
- `dev-notes/OBSERVATIONS.md`, section headed
  `## 2026-09-11 — 0.2.88 checkpoint-review dispositions` (anchor on the
  heading text) — the NORMATIVE list. Each bullet is a settled
  disposition: finding, FIX, check. Implement exactly the FIX sentences.
- `plugin/skills/statiker/SKILL.md` — the page (skill-craft gate below)
- the pinned page `git show 769e7f2:plugin/skills/statiker/SKILL.md` —
  the source for every "restore the pinned wording" FIX (n1, n3–n7, B1)
- `plugin/skills/statiker/scripts/statiker_git.py`,
  `plugin/skills/statiker/scripts/statiker_record.py`,
  `tools/test_statiker_git.py` — comment sites for N1 and G4
- Critique pass (mandatory, before your first build call): ONE
  SendMessage naming which Background line below you find unopened or
  wrong, and which two lines of this brief contradict each other; then
  continue without waiting for a reply.

## Background

Opened by the dispatcher:
- HEAD fd5c6ed carries the 0.2.88 page at 7774046 (plugin/ and tools/
  identical between them); plugin.json `"version": "0.2.88"`, unpushed;
  origin carries 0.2.87 (7791b63).
- Suite at 7774046: 537 passed, 2 subtests passed, 0 failed, 0 skipped;
  skill-lint (`--diff-base 7791b63`) exit 0; operational lines 1621.

From the reviewer's report (opus-review-0288), unverified at line grain —
locate every site by grep before editing:
- B1: S7's sentence reads "Each unit design carries the PRECEDENT LINE"
  (~:706); R30's pointer quotes "Each unit design also carries the
  PRECEDENT LINE" (~:444-445).
- B2: "(Implementation, I9)" at ~:1189; the passage it means opens "A
  missing decision, file, or value is reported as a gap" (~:1329).
- N1: SKILL.md ~:985 "from the pinned derivation", ~:1521 "(The attack's
  derivation)"; statiker_git.py ~:37 ("from the pinned repo-key
  derivation"), ~:371-374 (quotes 'derive it in the MAIN checkout, never
  a linked worktree…' as SKILL.md text), ~:384 and ~:417 ("SKILL.md's
  pinned derivation"); tools/test_statiker_git.py ~:2025 ("independent
  reference derivation (SKILL.md-pinned, The attack + The tools)") and
  ~:2088.
- G4-tool: statiker_record.py ~:221 (":145") and ~:407 (":468") cite
  SKILL.md by line number.
- n1–n7 sites and quotes: as in the dispositions section.

## The settled design — implement exactly the FIX sentences, do not redesign

- Restorations (B1, n1, n3, n4, n5, n6, n7): take the wording from the
  PINNED page, minimal — restore the dropped word, clause or distinction
  into the realized sentence; do not revert whole rows, and keep every
  other realized change.
- B2: replace `(Implementation, I9)` with `(Implementation, "A missing
  decision, file, or value is reported as a gap")`.
- n2: `seal-path --round A<n>` becomes `seal-path --tracker <path>
  --round A<n>`.
- N1 page pointers: each names the `seal-path` computation
  (statiker_git.py) as where the paths are derived, not a derivation on
  the page — e.g. "from `seal-path`'s computation"; keep each sentence's
  other content.
- N1 code comments: each names the tool's own derivation (the function
  it sits in or above) as the definition, and the test as its
  independent reference; none claims SKILL.md states the derivation.
  Comments and docstrings ONLY — no executable line changes.
- G4-tool: identify each line citation's target by the comment's own
  context against the page; replace the line number with the section
  name plus a quoted handle that occurs in that section. If a target
  cannot be identified with confidence, HALT that item and report both
  candidate passages.
- No new content beyond these FIX sentences; wrap to the page's width.

## Verifier (in order; real output pasted in the report)

1. Pointer resolver (scratch script): every quoted section pointer of
   the form `(<Section>, "<phrase>")` on the page — the phrase,
   whitespace-normalized, occurs inside the named `## ` section. Counts:
   pointers, resolved, unresolved (must be 0), listed. Red control: a
   scratch copy of the page with one planted pointer `(Close, "zzq no
   such phrase")` → unresolved 1. Also run it on the page at 7774046
   and paste its unresolved list (B1 expected there).
2. `"I9"` occurs 0 times in SKILL.md; "Each unit design also carries
   the PRECEDENT LINE" occurs in Stop rule.
3. N1: `grep -rn -E "pinned derivation|SKILL.md-pinned|SKILL.md's pinned"
   plugin tools` → 0 hits; the same command against `git show` copies at
   7774046 lists the hits (red side).
4. Restorations: for each of n1, n3, n4, n5, n6, n7, B1, print the
   restored phrase and its count on the page (each ≥ 1), and n2's new
   form (count 1, the old shorthand 0).
5. Verdict-token set: equal between the pinned page and the new page,
   using tools/test_contract.py's VERDICT_TOKEN_RE and GRAMMAR_LABEL_RE
   imported from the running module; both counts and both differences.
6. Scope: `git diff 7774046 -- plugin tools --stat`, and
   `git diff 7774046 -- plugin/skills/statiker/scripts tools` shows
   comment/docstring lines only (state it line by line).
7. `python3 -m pytest tools/ -q` — FULL counts; any failure or new skip
   is a finding.
8. `python3 /home/g/.claude/plugins/cache/skill-craft-marketplace/skill-craft/2.2.4/tools/skill_lint.py --diff-base 7791b63 plugin/skills/statiker/SKILL.md plugin/skills/statiker/references/evidence.md`
   — exit and blocking count (0); a length scan (no body line over 85);
   the operational line count (CLAUDE.md Verify awk).

## Write boundaries

Owned paths (nothing else):
- `plugin/skills/statiker/SKILL.md`
- `plugin/skills/statiker/scripts/statiker_git.py` (comments only)
- `plugin/skills/statiker/scripts/statiker_record.py` (comments only)
- `tools/test_statiker_git.py` (comments only)
Do NOT touch: plugin.json (0.2.88 is already the unpushed version),
hooks, other tests, dev-notes/, docs/, ITEMS.md, ITEMS-DONE.md,
LEDGER.md, BACKLOG.md, PLAN.md, CLAUDE.md.
Gate on SKILL.md: invoke the Skill tool `skill-craft:skill-craft`
BEFORE your first SKILL.md edit (repo CLAUDE.md, single-home bullet).
Not deployment-coupled: the installed plugin copy is separate.
Red-control mutations only on scratch copies — never on working files.

## Commit plan

Commit-blocking guards, each with the read that found it:
- Global pre-commit (`core.hooksPath` →
  `~/dev/Gunther-Schulz/dotfiles/git/hooks`; payload-version check at
  pre-commit :140-177, read at this desk): fires on a staged plugin/
  change whose manifest version equals HEAD's UNLESS HEAD's version
  differs from origin's. HEAD carries 0.2.88, origin 0.2.87, so no bump
  is needed and every payload commit passes. Push NOTHING.
- Global pre-push exists; you never push. No repo-local hook.
Commits, in this order, each by pathspec with its own tests' green:
`0.2.88 fix: B1 B2 — pointers resolve`, `0.2.88 fix: N1 + G4 — citations
name the tool, not page derivations or line numbers`, `0.2.88 fix: n1–n7
— restore pinned wording`.
Trailer, verbatim, on every commit:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`

## Tail

A mid-run message may not arrive before the turn ends: on a gap
HALT THE ITEM, FINISH THE REMAINDER, REPORT — never halt the
LANE, since "halt and wait" is not a survivable state for a
subagent (source: §2, the delivery binding).
Closing report (mandatory; the §2 form; "none" is a valid slot
answer, silence is not): (a) items completed w/ evidence, (b)
checks RUN w/ real output — FULL counts incl. skips (`N passed, M
failed, K skipped`), each skip dispositioned (which check, why,
whether the reason touches the item); a skip in a check YOU built
is a finding, not a pass — the built branch did not execute, (c)
gaps surfaced — incl. anything needing a tier above yours,
returned as a question with its evidence, never settled at your
tier, (d) deviations w/ reason, (e) candidate lessons, (f) files
touched + commit hashes (unpushed) — only commits whose
Co-Authored-By trailer is YOURS; one you cannot claim by trailer
is "present in the tree, not mine"; a `.git/config` write counts
as a repo write, (g) what was NOT verified, (h) sources actually
read, of those the brief named.
Every claim about something OUTSIDE your own work — a file you
did not write, a mechanism, another repo, a tool's behavior —
names the read that opened it, or carries "inferred, unverified";
a recommendation resting on an unopened claim carries the grade
too.
Drain your inbox before sending, and between parts of a
multi-part report: every dispatcher message received up to send
time is dispositioned or named as unhandled.
Report channel: SendMessage to the dispatcher — your final text reaches no one.
Message ≤3000 chars each: a report longer than one message is
SPLIT into labeled parts (1/N) — do NOT write a report FILE
(harness-blocked for subagents); supporting data goes to the
brief's assigned DATA files, the message carries key findings
+ any such paths. A missing decision, file, or value is surfaced
as a gap, never bridged with a guess.
A check that got backgrounded is AWAITED before the closing
report (TaskOutput block=true on its task id) — ending your turn
orphans it; a report sent with a check still running is an
INTERIM report, says so, and names what remains.
Commits unpushed, by pathspec — `git commit -m "…" -- <paths>`
with every flag BEFORE the `--` (after it git reads `-m` as a
pathspec and the commit fails; `-F` for a multi-line message),
never `git add` then `git commit` and never `-A`: the index is
shared, so a co-writer staging between your `git status` and your
commit rides out under your message whatever you added. A NEW
file is invisible to a pathspec commit until `git add -N <path>`
registers it (intent-to-add: zero content staged, full body still
committed). Trailer:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.
Never amend — always a new commit: the amend-gate denies subagent
amends regardless of ownership (source: §1 amend rule).
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended (source: §4
ownership rule).

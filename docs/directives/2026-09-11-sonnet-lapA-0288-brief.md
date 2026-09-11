# Title: sonnet: st-29 lap A stage 2 — apply the graded clause table to SKILL.md (0.2.88)

Dispatcher: statiker-4d, 2026-09-11. Lane name: sonnet-lapA-0288.
Working copy: /home/g/dev/Gunther-Schulz/statiker.
Base check: `git merge-base --is-ancestor <base> HEAD` AND
`git log --oneline <base>..HEAD` where `<base>` is the commit that
added THIS brief file (find it: `git log -1 --format=%h --
docs/directives/2026-09-11-sonnet-lapA-0288-brief.md`). Base contained
+ nothing on top touching your owned paths = clean start; then `git
status --porcelain` over your owned paths must be empty. Otherwise HALT
and report. Desk commits touching only ITEMS.md, LEDGER.md, dev-notes/
or docs/ may land while you run and are not a halt.
Scratch: `/tmp/claude-1000/-home-g-dev-Gunther-Schulz-statiker/f59bcaca-7615-4029-95ca-3a049796cc24/scratchpad/sonnet-lapA-0288/`
— that directory only (the scratch root is shared with other lanes),
never this repo.

## Grounding basis — read before building; the report cites what was actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST
- `docs/directives/2026-09-11-st29-lapA-clause-table.md` (da6936d) — the
  NORMATIVE table. Every row: id, line range at pin 769e7f2, handle,
  disposition, must-survive list (TIGHTEN) or load home (DELETE),
  verdict tokens carried, target line count. Its "Rules applied" and
  "Table conventions" sections define how to read it.
- `plugin/skills/statiker/SKILL.md` — the page you edit
- `tools/test_contract.py` `class TestVerdictParity` (~:1042-1058) and
  the page-text reader near :199-206 — what the suite checks on the page
- Critique pass (mandatory, before your first build call): ONE
  SendMessage naming which Background line below you find unopened or
  wrong, and which two lines of this brief contradict each other; then
  continue without waiting for a reply.

## Background (opened by the dispatcher)

- `git diff --stat 769e7f2 HEAD -- plugin` is empty at the brief's
  commit: SKILL.md in the working copy is byte-identical to the pinned
  page the table was built over, so the table's line ranges hold at
  your start.
- `plugin/.claude-plugin/plugin.json` carries `"version": "0.2.87",`,
  released and on origin (pin 0.2.87 at 7791b63).
- Suite at 769e7f2: 537 passed, 2 subtests passed, 0 failed, 0 skipped
  (desk run); skill-lint exit 0; operational lines 1766 (the CLAUDE.md
  Verify awk, which counts the closing frontmatter fence).
- The table's projection: 1765 → 1477 body lines (1766 → 1478
  canonical), per-section projections in its "Per-section summary".
- Graded at the desk (OBSERVATIONS 2026-09-11, "st-29 lap A stage 1:
  clause table graded"): all twelve torn rows take the table's CHOSEN
  disposition as written in its rows.

## The settled design — apply exactly, do not redesign

1. KEEP rows: untouched, byte for byte.
2. DELETE row (R19 only): remove its line range.
3. TIGHTEN rows: replace the row's range with shorter text that
   carries EVERY item in its must-survive cell and EVERY verdict token
   in its tokens column, verbatim where the cell quotes it (backticked
   literals, UPPER_SNAKE tokens, quoted phrases), at or under the row's
   target line count. Where keeping every must-survive item needs more
   lines than the target, KEEP THE ITEMS, exceed the target, and list
   the row in the report — never drop an item to meet a target.
4. No new content: no rule, clause, hedge, history or pointer the pinned
   text does not carry, except the two pointer fixes below. Wrap to the
   page's existing width.
5. Pointer fixes (desk-decided gaps G2 and G3):
   - G2: both occurrences of "the 0.68 NARROWING route" (pinned ~:297,
     row R13; ~:1260, row A23) become "the NARROWING route"; the section
     pointer that follows each stays as written.
   - G3: the `sustain` gloss in The tools (pinned ~:101, row T6) reads
     `(Stop rule, "That closes design")`; it becomes `(The attack, "That
     closes design")`.
6. Handle convention: a row's handle is matched against the page with
   every whitespace run (line breaks included) normalized to one space.
   Work each section bottom-up so earlier rows' pinned line ranges stay
   valid while you edit.

## Verifier (in order; real output pasted in the report)

Build one script in your scratch dir (`verify_lapA.py`) that compares
the pinned page (`git show 769e7f2:plugin/skills/statiker/SKILL.md`)
with the working page, and prove each check RED on a planted fault in a
scratch copy of the new page before trusting its green:
1. KEEP identity: for every KEEP row, its pinned text (whitespace-
   normalized) occurs in the new page. Counts: KEEP rows, found, missing
   (must be 0). Red control: alter one word of one KEEP row in a copy →
   missing 1.
2. Verdict-token set equality: the set of tokens matching the parity
   test's own regex (tools/test_contract.py VERDICT_TOKEN_RE minus its
   grammar-label regex, ~:62 and ~:199) is EQUAL in the pinned and the
   new page. Print both counts and both set differences (must be empty).
   Red control: delete one token in a copy → a difference of 1.
3. Must-survive literals: for every TIGHTEN row, each backticked
   literal and each UPPER_SNAKE token in its must-survive cell occurs in
   the new page (normalized). Counts: rows, literals checked, missing
   (must be 0). Red control: remove one literal in a copy → missing 1.
   The judgment remainder (prose conditions without quoted literals) is
   named in the report as not machine-checked.
4. Pointer fixes: "0.68 NARROWING" occurs 0 times;
   `(The attack, "That closes design")` occurs once;
   `(Stop rule, "That closes design")` occurs 0 times.
5. Per-section operational lines after vs the table's projection, and
   the canonical total (the CLAUDE.md Verify awk).
6. `python3 -m pytest tools/ -q` — full suite after each commit; the final
   run with FULL counts. Any failure or new skip is a finding.
7. `python3 /home/g/.claude/plugins/cache/skill-craft-marketplace/skill-craft/2.2.4/tools/skill_lint.py --diff-base 7791b63 plugin/skills/statiker/SKILL.md plugin/skills/statiker/references/evidence.md`
   — exit code and blocking count (must be 0).

## Write boundaries

Owned paths (nothing else):
- `plugin/.claude-plugin/plugin.json` (bump commit ONLY)
- `plugin/skills/statiker/SKILL.md`
Do NOT touch: the tool, tests, hooks, dev-notes/, docs/, ITEMS.md,
ITEMS-DONE.md, LEDGER.md, BACKLOG.md, PLAN.md, CLAUDE.md.
Gate on SKILL.md: invoke the Skill tool `skill-craft:skill-craft`
BEFORE your first SKILL.md edit (repo CLAUDE.md, single-home bullet).
Not deployment-coupled: the installed plugin copy is separate; the pin
moves only at a desk release.
Mutations for red controls happen ONLY on scratch copies — never on the
working page, never restored by `git checkout`.

## Commit plan

Commit-blocking guards, each with the read that found it:
- Global pre-commit (`core.hooksPath` →
  `~/dev/Gunther-Schulz/dotfiles/git/hooks`; its payload-version check
  at pre-commit :140-177, read at this desk): fires on a staged change
  under `plugin/` whose manifest version equals HEAD's, UNLESS HEAD's
  version already differs from origin's. HEAD and origin both carry
  0.2.87, so the FIRST commit is the bump: `plugin/.claude-plugin/plugin.json`
  `0.2.87` → `0.2.88`, that file alone. Later payload commits then pass
  while the batch stays UNPUSHED — push NOTHING.
- Global pre-push exists; you never push.
- No repo-local hook.
Then one commit per section that changes, in page order, each
`st-29 lap A: <section> — <row ids changed>` (e.g. `st-29 lap A: The
tools — T2 T3 T6 (G3)`). Sections whose rows are all KEEP get no commit.
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

# Briefs — wave 3: st-36 (lane A) and st-92 hook half (lane B), 2026-10-07

Two lanes run in PARALLEL in one working copy
(/home/g/dev/Gunther-Schulz/statiker). Each reads ONLY its own
section plus "Common" below. The closing-report form, commit rules
and gap rule are the `## Tail` section of
`docs/directives/2026-10-07-payload-st86-st66-st89-brief.md` — read
it and follow it verbatim.

## Common

- Load the executor skill (`dispatch-guards:executor`) FIRST.
- Base check: this file's own commit, or any later HEAD whose extra
  commits leave YOUR write-set paths untouched. First act:
  `git -C /home/g/dev/Gunther-Schulz/statiker status --porcelain`
  — a modified file inside your write set is a HALT (gap). The
  untracked `ITEMS-DONE.md.lock` is a tool lock file, not yours,
  leave it.
- A sibling lane and the dispatching desk write in this copy.
  Commit ONLY by pathspec, never `git add` + commit, never amend,
  never push, never `git stash`, never `git checkout` a file.
- Before your first build call send ONE message to the dispatcher:
  which Background line you find unopened or wrong, and which two
  lines of your section contradict ("none" is valid). Continue
  without waiting.
- Suite baseline, run by the dispatcher at 35d4043 minus later
  carrier-only commits: `python3 -m pytest tools/ -q` -> 695 passed,
  7 subtests passed, 0 skipped. The sibling lane adds tests while
  you run, so report your own new-test count and zero failed / zero
  skipped rather than an absolute total.
- Commit guard (read by the dispatcher): `core.hooksPath` =
  `~/dev/Gunther-Schulz/dotfiles/git/hooks`; its pre-commit refuses
  plugin payload committed without a version bump. Four payload
  commits passed it today at manifest 0.2.105 unbumped (observed),
  so no bump is expected. If one bounces: HALT that commit, report
  the message verbatim. Never `--no-verify`.
- Not live on write: the installed plugin serves from a cache
  pinned at 0.2.103.

## Lane A — st-36: ban numeric line pointers into the skill page

Title: sonnet: st-36 numeric-pointer ban
Trailer: `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`

Grounding: `ITEMS.md` block `## st-36` (the amended done-criterion
is the spec); `tools/test_contract.py` — `section_pointers` and the
tests around it, for idiom; the page
`plugin/skills/statiker/SKILL.md` at the passages you cite.

Background:
- A dry run today (codex luna, 108 pointers in tracked Python under
  plugin/ and tools/) found exactly 7 numeric pointers, 5 stale —
  from that run's report, spot-checked by the dispatcher only for
  `statiker_stop_guard.py:35` ("SKILL.md L328"; the page's line 328
  is not that text): the rest is from the report, unverified.
- The seven, by content (line numbers are as of commit 05b7ef1 and
  two of these files changed since — locate by the quoted pointer):
  `plugin/hooks/statiker_stop_guard.py` — "SKILL.md ~L328-334" and
  "SKILL.md L328" (also "(line ~331)" in the same docstring: treat
  any page line number there as a pointer);
  `plugin/skills/statiker/scripts/statiker_record.py` — "SKILL.md
  (Implementation, :876-880)" and "SKILL.md :730-731";
  `tools/test_statiker_record.py` — "SKILL.md :114-117", "SKILL.md
  :112-113", "SKILL.md:729-733".

Settled design:
1. Rewrite each numeric pointer as `SKILL.md (<Section heading>,
   "<anchor phrase>")`, where the section is the page's own `##`
   heading containing the claimed text TODAY and the anchor is a
   short verbatim phrase from that text (5-12 words, on one page
   line, so a line-based search finds it). Find the claimed text by
   what the surrounding comment says it is, not by the old number.
   A pointer whose claimed text no longer exists anywhere on the
   page: do not invent an anchor — leave it, list it as a gap.
2. Contract test in `tools/test_contract.py`, two assertions:
   (a) NO numeric pointer form in tracked `*.py` under `plugin/` and
   `tools/`: the text `SKILL.md` followed within the same line (or
   the wrapped next comment line) by a line number or range in any
   of the observed spellings — `:<n>`, `:<n>-<m>`, ` L<n>`,
   ` ~L<n>-<m>`, `(…, :<n>-<m>)`, `(line ~<n>)`. The test file
   itself must not trip its own pattern (build the regex from
   pieces or exempt the test's own source by path, stated in a
   comment).
   (b) every `SKILL.md (<Section>, "<phrase>")` pointer in those
   files names an existing `##` heading and a phrase present in the
   page under whitespace normalization.
3. Red-first: write the test first, run it on the UNCONVERTED tree,
   paste the red (it must name all seven sites — fewer means the
   pattern under-reaches; say which it missed and widen). Then
   convert, then green. Also show (a) going red on one planted
   numeric pointer in a scratch COPY of a file outside the repo
   tree is not required; instead keep one negative-control string
   in the test itself (a constructed line the regex must match).

Write set: `tools/test_contract.py`,
`plugin/hooks/statiker_stop_guard.py`,
`plugin/skills/statiker/scripts/statiker_record.py`,
`tools/test_statiker_record.py` — comment/docstring text and the
new test only; no behaviour change in any script. Not the page.
Commits: one for the test + conversions together (the test is red
without them), title `st-36: …`.
Verifier: the red-first output; then `python3 -m pytest tools/ -q`
whole; `git status --porcelain` showing none of your files dirty.

## Lane B — st-92, build half: re-enter the resume gate after a compaction

Title: opus: st-92 post-compaction hook
Trailer: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`

Grounding: `ITEMS.md` block `## st-92`;
`plugin/hooks/statiker_stop_guard.py` whole (the plugin's one
existing hook — idiom, fail-open rule, schema notes, its tests in
`tools/test_statiker_stop_hook.py`); `plugin/hooks/hooks.json`;
the harness source `~/dev/reference/claude-code/src/utils/hooks.ts`
for the SessionStart hook's input and output contract (RAW source,
never a summary); one working plugin `hooks.json` with a
SessionStart entry for the registration schema, e.g. under
`~/.claude/plugins/cache/dispatch-guards-marketplace/dispatch-guards/0.11.26/hooks/`;
the page's resume passage (search SKILL.md for `resume`), to quote
the gate's commands correctly.

Background:
- `hooks.ts` types SessionStart's `source` as
  `'startup' | 'resume' | 'clear' | 'compact'` — opened by the
  dispatcher at line 3868 of the reference copy. That SessionStart
  output is injected into the post-compaction context is RECALLED,
  unverified: establish it from the source and cite file:line. If
  the source shows it is NOT injected for `compact`, HALT and
  report — do not switch events on your own.
- `plugin/hooks/hooks.json` is `{"hooks": {}}` today — opened. The
  Stop hook exists as a file but is deliberately unregistered
  (ITEMS.md st-15). Do not register it.
- The stop guard finds trackers by `.clippy/runs/*-statiker.md` —
  opened (statiker_stop_guard.py, `_TRACKER_GLOB`). The page names
  trackers `.clippy/runs/<yyyy-mm-dd>-<slug>.md` (SKILL.md:262) and
  the last real run's tracker is
  `.clippy/runs/2026-09-25-prod-data-growth.md` with header lines
  `Status: COMPLETE` and `Skill: statiker 0.2.103` — opened. So the
  stop guard's glob does not match real trackers; that is st-15's
  to fix, NOT yours — report it in (c), do not edit that file.

Settled design:
- New file `plugin/hooks/statiker_postcompact.py`, registered in
  `plugin/hooks/hooks.json` under SessionStart with matcher
  `compact`, invoked the way the reference plugin invokes its
  Python hooks (plugin-root variable, not an absolute path).
- Fire = payload `source` is `compact` AND the payload `cwd` holds
  at least one `.clippy/runs/*.md` file whose header (first 15
  lines) carries a line starting `Skill: statiker` AND a line
  exactly `Status: in-progress`. Check the page for the exact live
  Status value(s) and use the page's; cite the line. Silent
  otherwise.
- On fire, emit SessionStart additional context (the form the
  source prescribes) with exactly this text, `<tracker>` being the
  repo-relative path(s), comma-separated:

      statiker: this session's context was just compacted. What you
      hold of the skill page and of the run record is now a summary,
      not the text. Before your next act: load the statiker skill
      again, then run the resume gate over <tracker> (sweep, then
      closure) and continue from their verdicts, never from the
      summary.

- Fail-open everywhere: unreadable payload, unreadable tracker, any
  exception -> exit 0, empty stdout, a one-line warning on stderr.
  Never block, never write a file.
- Tests in a NEW file `tools/test_statiker_postcompact_hook.py`
  (register it with `git add -N` before the pathspec commit),
  driving the script as a subprocess with a JSON payload on stdin:
  fires on a live statiker tracker and names it; silent on
  `Status: COMPLETE`; silent with no `.clippy/`; silent on a
  tracker without the `Skill: statiker` header; silent on
  `source: startup`; silent and exit 0 on malformed stdin. Read the
  RETURN CODE in every arm, not only stdout. Red-first is the
  absent script (state it); the discriminating pair is live versus
  COMPLETE.
- No page (SKILL.md) edit, no CLAUDE.md/ITEMS/LEDGER/dev-notes
  edit: the dispatcher writes the mint record and tenet check.

Write set: `plugin/hooks/statiker_postcompact.py`,
`plugin/hooks/hooks.json`, `tools/test_statiker_postcompact_hook.py`.
NOT `tools/test_contract.py` (the sibling lane owns it): if any
existing test asserts the hooks manifest is empty or otherwise goes
red on your registration, HALT that step, leave hooks.json
unregistered-but-ready (report the exact entry you would add), and
report the failing test verbatim.
Commits: `st-92: post-compaction hook …` (script + tests), then
`st-92: register …` (hooks.json) as its own commit.
Verifier: your new tests; `python3 -m pytest tools/ -q` whole; a
manual run of the script with a constructed payload in your
scratchpad, output pasted. NOT verifiable by you and to be stated
as such in (g): a real compaction firing the hook in a live
session — that is the run-3 probe.

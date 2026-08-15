# Brief: lane G — three git-tool entries (E-C, E-D, E-H)

Title: sonnet: git-tool set — byte-level emit, sha from the
commit's own output, preflight branch state.

Working copy: the git worktree the harness placed you in (isolated
checkout of statiker). Base check: the required base commit is named
in the dispatch prompt. First act: `git merge-base --is-ancestor
<base> HEAD` AND `git log --oneline <base>..HEAD`. Base contained +
nothing on top = clean start. Anything else: HALT, report as a gap.

Scratch: your OWN scratchpad. Fixture repos go there.

## Grounding basis — read before building; report slot (h) cites what was actually read

- The executor skill (`dispatch-guards:executor`) — load FIRST.
- `BACKLOG.md`, section `## Open`, the three entries titled E-C,
  E-D, E-H. These ARE the settled designs — implement exactly
  them, do not redesign. (E-A/E-B/E-E/E-F/E-G/E-I belong to a
  parallel lane; the P-entries are parked. Touch neither.)
- `plugin/skills/statiker/scripts/statiker_git.py` — `say` (:94),
  the stream reconfigure (:844-845), `head_shown_paths` (:502),
  `commit_with_retry` (:548-551).
- `plugin/skills/statiker/scripts/statiker_record.py` — `emit()`
  (the byte-level shape E-C mirrors). READ-ONLY: a parallel lane
  owns this file.
- Probe arrangements where an entry cites an arm file: begehung
  repo, `dev-notes/eval-begehung/2026-08-11/tier2-{with,without,sentence}.md`
  — FOREIGN REPO, READ-ONLY.

## Background (verified by the dispatcher at the base commit, 2026-08-15)

- Full suite at base: expected 307 passed (`python3 -m pytest
  tools/ -q`) — run it yourself as the baseline; paste the count. A
  red baseline is HALT+report.
- Entry line-citations were written against an older HEAD and have
  SHIFTED. Dispatcher re-verified each PREMISE at the current base:
  `say()` is still a plain `print` under a stream reconfigured
  `errors="replace"` (:94, :844-845) — E-C open;
  `commit_with_retry` still takes its sha from a separate
  `rev-parse HEAD` after the commit (:551) and `head_shown_paths`
  reads HEAD (:502) — E-D open; preflight carries no branch-state
  field — E-H open. Re-locate cited sites in the current file.
- NOTE for E-C: the recent BrokenPipe repair (606c04a) already
  restructured the emit path's error handling in this file. Your
  byte-level change must preserve that behavior (its tests are in
  the suite and must stay green) — encoding changes, pipe handling
  stays.
- YOU ARE RUNNING INSIDE A LINKED WORKTREE. E-H's probes (detached
  HEAD, linked-worktree cwd) are built in your OWN fixture repos in
  scratch, never against the working copy you sit in.
- The version bump for this batch (0.2.63) is already committed in
  your base and is UNPUSHED — the payload guard's unpushed-batch
  exemption is armed; no bump is yours. If a payload commit still
  bounces, HALT and report — never `--no-verify`.
- A USER-level hook grades any STAGED `BACKLOG.md` — outside your
  boundary; never stage it.
- Exotic bytes in fixtures are CONSTRUCTED FROM ESCAPES in code
  (`b"\xff"`, `b"caf\xe9"`), never pasted literal into files.

## The settled design — implement exactly the three entries, in this order, one commit per entry

Order: E-C → E-D → E-H. Each entry's design, verifier, red-first
arrangement, and done-criterion are in its BACKLOG.md body.
Additional dispatcher rulings:

- E-C/E-D/E-H add FIELDS or change internals, no new verdict names
  — if any of your changes does introduce a new verdict name, that
  is a contract-battery row in tools/test_contract.py, which is
  OUTSIDE your boundary: HALT that entry and report the collision
  as a gap instead of editing the file.
- Red-first per entry is stash-proof: `git stash push --` the
  script file, run the entry's new battery cases against the old
  implementation, observe red, pop, observe green. Paste which side
  was old and the observed output, per entry. E-D's red uses the
  arm's post-commit-hook window-occupier arrangement (WITHOUT-F9).

## Verifier (in order; real output pasted in the report)

1. Baseline full suite at base — paste the count.
2. Per entry: stash-proof red output, then full
   `python3 -m pytest tools/ -q` green after its commit — paste
   counts.
3. Final: full suite at lane tip, 0 failed.

## Write boundaries

Owned: `plugin/skills/statiker/scripts/statiker_git.py`,
`tools/test_statiker_git.py`. NOT touched: statiker_record.py,
tools/test_statiker_record.py, tools/test_contract.py (a parallel
lane owns all three), SKILL.md, BACKLOG.md, dev-notes/, docs/,
plugin.json. Commits by pathspec: `git commit -- <paths>`. Never
amend — always a new commit. All commits stay in your worktree,
unpushed; the dispatcher cherry-picks at integration.

## Commit plan

Three commits in entry order, one-line German titles in the repo's
style + the trailer. The 0.2.63 bump precedes your base (unpushed,
exemption armed — Background); no other ordering guards: none.

Closing report (mandatory; the §2 form): (a) items completed w/
evidence, (b) checks RUN w/ real output, (c) gaps surfaced —
incl. anything needing a tier above yours, returned as a question
with its evidence, never settled at your tier,
(d) deviations w/ reason, (e) candidate lessons, (f) files
touched + commit hashes (unpushed), (g) what was NOT verified,
(h) sources actually read, of those the brief named.
Message ≤3000 chars each: a report longer than one message is
SPLIT into labeled parts (1/N) — do NOT write a report FILE
(harness-blocked for subagents); supporting data goes to the
brief's assigned DATA files, the message carries key findings
+ any such paths. A missing decision, file,
or value is surfaced as a gap, never bridged with a guess.
A check that got backgrounded is AWAITED before the closing
report (TaskOutput block=true on its task id) — ending your
turn orphans it; a report sent with a check still running is
an INTERIM report, says so, and names what remains.
Commits unpushed, by pathspec — `git commit -- <paths>`, never
`git add` then `git commit` and never `-A`: the index is shared,
so a co-writer staging between your `git status` and your commit
rides out under your message whatever you added. A NEW file is
invisible to a pathspec commit until `git add -N <path>`
registers it (intent-to-add: zero content staged, full body
still committed). Trailer:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.
Never amend — always a new commit: the amend-gate denies
subagent amends regardless of ownership (source: §1 amend
rule).
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended (source: §4
ownership rule).

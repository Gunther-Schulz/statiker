# Brief: lane R — six record-tool entries (E-A, E-B, E-E, E-F, E-G, E-I)

Title: sonnet: record-tool instrument set — verdict reach, unknown
unit, small fixes, freeze breach, header slice, pinned subcommand.

Working copy: the git worktree the harness placed you in (isolated
checkout of statiker). Base check: the required base commit is named
in the dispatch prompt. First act: `git merge-base --is-ancestor
<base> HEAD` AND `git log --oneline <base>..HEAD`. Base contained +
nothing on top = clean start. Anything else: HALT, report as a gap.

Scratch: your OWN scratchpad. Probe trackers and fixture repos go
there.

## Grounding basis — read before building; report slot (h) cites what was actually read

- The executor skill (`dispatch-guards:executor`) — load FIRST.
- `BACKLOG.md`, section `## Open`, the six entries titled E-A, E-B,
  E-E, E-F, E-G, E-I. These ARE the settled designs — implement
  exactly them, do not redesign. (The E-C/E-D/E-H entries belong to
  a parallel lane; the P-entries are parked. Touch neither.)
- `plugin/skills/statiker/scripts/statiker_record.py` — the sites
  in Background below.
- `plugin/skills/statiker/SKILL.md` — READ-ONLY, for E-G's
  first-step literal verification and E-E(4)'s citation refresh.
- Probe arrangements where an entry cites an arm file: begehung
  repo, `dev-notes/eval-begehung/2026-08-11/tier2-{with,without,sentence}.md`
  — FOREIGN REPO, READ-ONLY.

## Background (verified by the dispatcher at the base commit, 2026-08-15)

- Full suite at base: expected 307 passed (`python3 -m pytest
  tools/ -q`) — run it yourself as the baseline; paste the count. A
  red baseline is HALT+report.
- The entries' line-number citations were written against an older
  HEAD (2bb9830) and have SHIFTED (the file gained ~2 releases of
  edits since). The dispatcher re-verified every entry's PREMISE at
  the current base: no `entries:` verdict field exists; `closure
  --unit` validates form only (`re.fullmatch(r"U\d+")`, now at
  :982) and consults no known-unit set; no PermissionError branch
  in filter's --out handling; the docstring's stale "no literal
  write-set record-line form" NOTE still stands; no freeze-breach
  lint exists (the DISPATCHED reads at :1208-1237 are trend's own);
  `irreversible`/`Budget` appear nowhere in the script; no PINNED
  verdicts exist. Treat entry-cited line numbers as approximate;
  re-locate each site in the current file.
- E-E(4)'s citation refresh: compute the correct SKILL.md line
  numbers from the CURRENT file, never from the triage record (the
  file changed again at ed3071c).
- The version bump for this batch (0.2.63) is already committed in
  your base and is UNPUSHED — the payload guard's unpushed-batch
  exemption is armed; no bump is yours. If a payload commit still
  bounces off the guard, HALT and report — never `--no-verify`.
- A USER-level hook grades any STAGED `BACKLOG.md` — it is outside
  your write boundary; never stage it.
- Exotic bytes in fixtures are CONSTRUCTED FROM ESCAPES in code
  (`" "`, `b"\xff"`), never pasted literal into files (a
  literal U+2028 in a tool payload degraded to a space in an
  earlier lane and a repair hit 30k sites).

## The settled design — implement exactly the six entries, in this order, one commit per entry

Order: E-A → E-B → E-E → E-F → E-G → E-I. Each entry's design,
verifier, red-first arrangement, and done-criterion are in its
BACKLOG.md body. Additional dispatcher rulings:

- E-B's new verdict (UNIT_UNKNOWN) gets its contract-battery row in
  the same commit (the battery is set-exact; an undriven verdict is
  a red you must not leave standing).
- E-G: its first build step (verify the literal forms against
  SKILL.md's own sentences) is binding — if a literal form is
  ambiguous in the current SKILL.md text, HALT that entry and
  report the ambiguity as a gap; land the other entries' commits
  regardless.
- E-I's PINNED_APPEND_ONLY/PINNED_REWRITTEN pair: contract rows in
  the same commit, same reason as E-B.
- Red-first per entry is stash-proof: `git stash push --` the
  script file, run the entry's new battery cases against the old
  implementation, observe red, pop, observe green. Paste which side
  was old and the observed output, per entry.

## Verifier (in order; real output pasted in the report)

1. Baseline full suite at base — paste the count.
2. Per entry: stash-proof red output, then full
   `python3 -m pytest tools/ -q` green after its commit — paste
   counts.
3. Final: full suite at lane tip, 0 failed.

## Write boundaries

Owned: `plugin/skills/statiker/scripts/statiker_record.py`,
`tools/test_statiker_record.py`, `tools/test_contract.py`.
NOT touched: statiker_git.py, tools/test_statiker_git.py (a
parallel lane owns them), SKILL.md, BACKLOG.md, dev-notes/, docs/,
plugin.json. Commits by pathspec: `git commit -- <paths>`. Never
amend — always a new commit. All commits stay in your worktree,
unpushed; the dispatcher cherry-picks at integration.

## Commit plan

Six commits in entry order, one-line German titles in the repo's
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

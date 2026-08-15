# Brief: lane R2 — E-B, E-I, E-G′ (the re-dispatched record-tool remainder)

Title: sonnet: UNIT_UNKNOWN gate, pinned subcommand, Mode/Budget
instruments — with their pre-named SKILL.md route sentences.

Working copy: the git worktree the harness placed you in (isolated
checkout of statiker). Base check: required base commit is named in
the dispatch prompt. First act: `git merge-base --is-ancestor
<base> HEAD` AND `git log --oneline <base>..HEAD`. Base contained +
nothing on top = clean start. If the base check FAILS with a clean
tree AND `git merge-base --is-ancestor HEAD <base>` succeeds (you
are strictly behind — the base is deliberately unpushed, harness
cuts have matched origin), the sanctioned recovery is `git merge
--ff-only <base>`, then re-run the check. Forked, dirty, or base
unresolvable: HALT, report as a gap.

Scratch: your OWN scratchpad.

## Grounding basis — read before building; report slot (h) cites what was actually read

- The executor skill (`dispatch-guards:executor`) — load FIRST.
- `BACKLOG.md`, `## Open`: the entries titled E-B (including BOTH
  AMENDED paragraphs), E-I (including its AMENDED paragraph), and
  E-G′. These ARE the settled designs — implement exactly them.
  The AMENDED paragraphs carry the exact SKILL.md sentences you
  will insert; quote them verbatim, character for character.
- `plugin/skills/statiker/scripts/statiker_record.py` — current
  file (it now carries lane R's E-A/E-E/E-F work; re-locate all
  cited sites in the current text).
- `plugin/skills/statiker/SKILL.md` — the two insertion anchors
  named in the AMENDED paragraphs, plus E-G′'s header-field
  passages. Before each SKILL.md-touching commit, invoke the
  `skill-craft:skill-craft` skill (project CLAUDE.md discipline);
  your edits are the two verbatim pre-named insertions, no other
  SKILL.md change.

## Background (verified by the dispatcher at the base commit, 2026-08-15)

- Full suite at base: expected 329 passed — run as baseline, paste
  the count; red baseline = HALT+report.
- The contract battery's parity test is set-exact BOTH ways: a new
  verdict emitted without its SKILL.md route is red, and a route
  without its emitter is red (fired today on the desk's own
  mint-first attempt). Therefore each SKILL.md insertion lands IN
  THE SAME COMMIT as its emitting code: E-B's commit carries the
  UNIT_UNKNOWN insertion + code + contract row; E-I's commit
  carries the pinned passage + code + contract rows. E-G′ adds no
  verdict name and touches no SKILL.md.
- The 0.2.63 bump is in your base history, UNPUSHED — the payload
  guard's unpushed-batch exemption is armed; no bump is yours. A
  bounce is HALT+report, never `--no-verify`.
- A USER-level hook grades any STAGED BACKLOG.md — outside your
  boundary; never stage it.
- Prior-lane implementation note (binding, E-B): standalone
  `known_units_of(entries)` helper; never widen waves_over_units'
  return tuple (tools/test_statiker_git.py unpacks the 4-tuple and
  belongs to another lane).

## The settled design — implement exactly the three entries, in this order, one commit per entry

Order: E-B → E-I → E-G′. Designs, verifiers, red-first
arrangements, done-criteria: the entries' bodies. Red-first is
stash-proof per entry (stash the script + SKILL.md changes, run new
battery cases against old state, observe red, pop, observe green;
paste which side was old and the outputs). For E-B and E-I the
parity red counts as one of the observed reds (new test red against
old code; parity red if route-only or emit-only — you need not
demonstrate both halves separately, the same-commit rule prevents
them).

## Verifier (in order; real output pasted in the report)

1. Baseline full suite at base — paste count (expect 329).
2. Per entry: stash-proof red output, then full
   `python3 -m pytest tools/ -q` green after its commit — paste
   counts.
3. Final: full suite at lane tip, 0 failed; contract battery
   explicitly named in the count.

## Write boundaries

Owned: `plugin/skills/statiker/scripts/statiker_record.py`,
`tools/test_statiker_record.py`, `tools/test_contract.py`, and
`plugin/skills/statiker/SKILL.md` STRICTLY scoped to the two
pre-named insertions (E-B's and E-I's AMENDED paragraphs — any
other SKILL.md need is a HALT+gap). NOT touched: statiker_git.py,
tools/test_statiker_git.py, BACKLOG.md, dev-notes/, docs/,
plugin.json. Commits by pathspec: `git commit -- <paths>`. Never
amend — always a new commit. Commits stay in your worktree,
unpushed; the dispatcher cherry-picks at integration.

## Commit plan

Three commits in entry order, one-line German titles in the repo's
style + the trailer. The 0.2.63 bump precedes your base (unpushed,
exemption armed); no other ordering guards: none.

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

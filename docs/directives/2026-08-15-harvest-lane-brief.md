# Brief: harvest lane — splitlines class, harvest-2 defects, worktree containment

Title: sonnet: three booked repairs, serialized — test-reader
splitlines class, begehung-harvest-2 record/git defects, worktree-add
containment.

Working copy: /home/g/dev/Gunther-Schulz/statiker (main checkout,
branch main — you work in place; the dispatcher writes nothing here
until your report is booked).

Base check: the required base commit is named in the dispatch
prompt. First act: `git merge-base --is-ancestor <base> HEAD` AND
`git log --oneline <base>..HEAD`. Base contained + nothing on top =
clean start. Base not contained + clean tree = fast-forward to base.
Base contained + commits on top = foreign work: HALT, report the
commits as a gap. Any other state (dirty tree included): HALT.

Scratch: your OWN scratchpad, nowhere else. Probe fixture repos and
throwaway trackers go there.

## Grounding basis — read before building; report slot (h) cites what was actually read

- The executor skill (`dispatch-guards:executor`) — load FIRST.
- `BACKLOG.md`, section `## Open`, the three entries (read in
  full, including the harvest-2 entry's AMENDED block):
  1. "READY (small) 2026-08-11 — close the splitlines CLASS…"
  2. "READY 2026-08-11 — begehung-harvest 2: four gate/instrument
     defects…" (+ its AMENDED 2026-08-15 paragraph)
  3. "READY 2026-08-11 — worktree-add containment joins the record
     tool's semantics…"
  These entries ARE the settled designs. Implement exactly them;
  do not redesign.
- `/home/g/dev/Gunther-Schulz/begehung/dev-notes/eval-begehung/2026-08-11-opus/tier2-without.md`
  — parts 3/7 through 7/7: the executed probe arrangements and
  repair paragraphs for harvest-2 defects (a)-(d). FOREIGN REPO,
  READ-ONLY — you never write outside the statiker working copy
  and your scratchpad.
- `plugin/skills/statiker/scripts/statiker_record.py` —
  `split_lines` (:343), `apply_supersession` (:561-593),
  `REPAIR_FORMS` (:209-215), the `--out` every-repo walk
  (:1156-1184, the containment pattern item 3 mirrors), `trend`
  bounds (:1080-1085 region), `finish`/`emit`.
- `plugin/skills/statiker/scripts/statiker_git.py` — `say` (:87),
  `RETRY_BASE` (:71), `Repo.outside` and the worktree-add path.
- `tools/test_statiker_record.py` —
  `test_the_fixture_reader_survives_a_separator_in_the_block`: the
  repaired reader + standing separator case that item 1 mirrors.
- `plugin/skills/statiker/SKILL.md` — the two regions in
  Background below. Before editing this file, invoke the
  `skill-craft:skill-craft` skill (project CLAUDE.md discipline:
  no SKILL.md edit without it); the edit itself is the two
  deletions named below, no new prose.

## Background (each line verified by the dispatcher at the base commit, 2026-08-15, unless graded otherwise)

- Full suite at base: expected 286 passed (`python3 -m pytest
  tools/ -q`) — run it yourself as the baseline before any change;
  paste the result. A red baseline is a HALT+report, not a repair.
- `quote` already uses `split_lines` (82ed13c) — item 1 is about
  tools/ TEST READERS only.
- stdout-splitting sites at base (dispatcher grep):
  `tools/test_statiker_git.py:73, 88, 524, 535, 547, 557, 577` and
  `tools/test_contract.py:585`. The `tools/test_statiker_record.py`
  sites (:616, :632, :847) split a JSON-decoded string FIELD, not
  stdout — OUT of item 1's scope; if you judge them in-class,
  report under slot (e), do not change them.
- `statiker_git.py:71` reads `STATIKER_GIT_RETRY_BASE` via
  `float()` at module level, outside main()'s try — the (d2) case.
- SKILL.md sentence 1 (The tools, ~:60-62), delete exactly the
  clause: "— the worktree path is the one must-be-outside member
  still decided on its real form alone, its as-named half the
  desk's check —" (the surrounding containment sentence stays and
  must remain grammatical).
- SKILL.md sentence 2 (batched-trip section, ~:697-700), delete
  exactly the parenthetical: "(the tool's PATH_INSIDE_REPO halt
  covers THIS repo's containment only; sibling checkouts and the
  as-named spelling stay the desk's check)".
- No commit-blocking hooks in this repo (`.git/hooks` holds
  samples only). A USER-level hook grades any STAGED `BACKLOG.md`
  — BACKLOG.md is outside your write boundary; never stage it.
- The harvest-2 entry's Done line offers "pinned by a test or
  recorded as accepted" for the sweep-code-immunity ordering note
  (arm file part 4/7). DECIDED by the dispatcher: pin it by test —
  after fix (a) the immunity is structural (sweep-level codes are
  not REPAIR_BOOKKEEPING members), so add a battery case asserting
  a `corrects` token aimed at a `pending-latest` line sheds
  nothing, whatever the internal ordering.
- Probe arrangements for (a)-(d): quoted in the arm file's parts
  3/7-7/7 (from that file — its fixture scratchpad is gone;
  reconstruct fixtures from the quoted arrangements).

## The settled design — implement exactly this, do not redesign

Three items, STRICTLY in this order (item 1's repaired readers are
what parse item 2's and 3's new battery cases), one commit per
item.

**Item 1 (commit 1).** Both named stdout readers — and every other
site in tools/ that splits tool STDOUT — split on `"\n"` only,
mirroring the record fixture reader's repair (a shared helper in
each file, or import — mirror the existing repair's shape). One
separator-carrying red-first case per reader file, mirroring
`test_the_fixture_reader_survives_a_separator_in_the_block`.
Done-grep (from the entry): no `str.splitlines()` over tool stdout
remains in `tools/`.

**Item 2 (commit 2).** The five fixes, each with its red-first
battery case reconstructed from the arm file:
(a) `apply_supersession` sheds only codes whose REPAIR_FORMS class
is REPAIR_BOOKKEEPING, supersedes only MACHINE_TOKEN_CODES
members, else lints `corrects-nothing` carrying the declared form
(the classification table exists; consult it at the decision
point). Red pair: arm probes A (bogus-status header) and B (INTENT
tag-literal) both reach LINT_CLEAN/SWEEP_CLEAN today and must lint
after. Plus the ordering-pin case from Background.
(b) the `waves` path FIELD gets the positional lint the declarator
got (c2c5baf pattern): whitespace inside the path field and a
leading `/` lint at composition. Red cases: the arm's U2
(`src/app.py src/util.py` one line) and U4 (absolute spelling) —
plus the three-arm probes named in the entry's AMENDED paragraph
(absolute spelling certified parallel-eligible) as additional
battery rows.
(c) `trend` advances its window at VOID A-lines and starts bucket
1 at the first `[DISPATCHED]` line. Red pair: the arm's two probes
(WORSENING→IMPROVING flip on an unchanged 2→1 series; bucket-1
investigation-lines contamination).
(d) BrokenPipeError caught at the emit boundary with a defined
exit code — BOTH tools. Red: `waves … | head -1` today ends in a
traceback with pipeline exit 0 and no verdict line.
(d2) `STATIKER_GIT_RETRY_BASE` read moves inside the guarded
region, same defined exit code as (d). Red:
`STATIKER_GIT_RETRY_BASE=abc … state-gate` today emits a bare
traceback, exit 1, no verdict line.
Which exit code is "defined" is settled by the tools' existing
contract (0/2/3 per SKILL.md): a broken pipe / bad env is
USAGE_ERROR-class, exit 3, verdict line attempted on stderr-safe
path — if the existing contract text contradicts this, HALT and
report the gap rather than choosing.

**Item 3 (commit 3).** `Repo.outside()` in statiker_git.py gains
the every-enclosing-repo probe the record tool's `--out` check
carries (statiker_record.py:1156-1184 is the pattern) AND the
named-and-real-agree rule; PATH_INSIDE_REPO fires on any enclosing
repo and on as-named/real disagreement. Red pair (both executed in
the 0.2.59 review, quoted in the entry): from repo A
`worktree-add --path ../B/wt-in-B` → today WORKTREE_ADDED + `??
wt-in-B/` in sibling B, must halt PATH_INSIDE_REPO; symlink
spelling `link/wt` (link → outside dir) → today WORKTREE_ADDED,
must halt. Must-not-fire: the existing outside-dir case stays
WORKTREE_ADDED. Same commit: the two SKILL.md deletions from
Background (skill-craft invocation first).

## Verifier (in order; real output pasted in the report)

1. Baseline: full suite at base — paste the count (expected 286
   passed).
2. Per item, red-first stash-proof: run the item's NEW battery
   cases against the OLD implementation (`git stash` the script
   changes, run, observe red, `git stash pop`) — paste which side
   was old and the observed reds. For item 1 (test-only), the
   red-first form is the separator case failing against the
   pre-repair reader (temporarily revert the reader hunk, run,
   restore).
3. After each commit: full `python3 -m pytest tools/ -q` green —
   paste counts.
4. Done-greps: `grep -rn "splitlines" tools/` shows no
   str.splitlines over tool stdout; `grep -n "worktree path is
   the" plugin/skills/statiker/SKILL.md` → 0 hits;
   `grep -n "THIS repo's containment only"
   plugin/skills/statiker/SKILL.md` → 0 hits.
5. Final: full suite green at the lane tip (expect 286 + your new
   cases, 0 failed).

## Write boundaries

Owned paths: `plugin/skills/statiker/scripts/statiker_record.py`,
`plugin/skills/statiker/scripts/statiker_git.py`,
`plugin/skills/statiker/SKILL.md` (the two deletions ONLY),
`tools/test_statiker_record.py`, `tools/test_statiker_git.py`,
`tools/test_contract.py`. NOT touched: BACKLOG.md, dev-notes/,
docs/, plugin.json, anything else. Not deployment-coupled (the
marketplace pin moves only at a desk release, never here). Commits
by pathspec: `git commit -- <paths>`. Never amend — always a new
commit.

## Commit plan

Three commits in item order, each message a one-line German title
in the repo's style (see `git log --oneline`) + the trailer. The
dispatcher has already landed the version-bump commit ahead of
this lane (the repo's bump-before-repair-batch convention); no
bump is yours. No other ordering guards: none.

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

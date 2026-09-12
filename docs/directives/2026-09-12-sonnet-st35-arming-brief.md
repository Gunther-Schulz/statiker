# sonnet-st35-arming — the tripwire's arming carrier (st-35)

Title: sonnet: st-35 — arming moves from an in-place header edit to an appended record entry
Working copy: `/home/g/dev/Gunther-Schulz/statiker`.
Base check: base commit `44516dd` (read at dispatch time:
`git -C /home/g/dev/Gunther-Schulz/statiker rev-parse --short HEAD` →
`44516dd`), **or any later HEAD whose extra commits leave your write set
untouched** — this brief's own commit is one such, and the desk commits
records (LEDGER, ITEMS, OBSERVATIONS, docs/) while you build. Run BOTH
reads before your first edit: `git merge-base --is-ancestor <base> HEAD`
and `git log --oneline <base>..HEAD`. Base contained and nothing on top
→ clean start. Base NOT contained → halt and report. Base contained WITH
commits on top → report those commits as a gap and halt, UNLESS
`git diff --quiet <base> HEAD -- <your write set>` is clean, in which
case report the changed-file list and continue. Third read, whatever the
base check said: `git status --porcelain` over your write set — any
modified file there is a HALT.
Scratch: your OWN scratchpad. Name every scratch file with the slug
`st35`.

## Grounding basis — read before building; the report cites what was
## actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST.
- `dev-notes/OBSERVATIONS.md`, the section
  `## 2026-09-12 — st-35 ruling (statiker-df, opus desk): the
  tripwire's arming carrier`. **This is the design.** It carries the
  ruling, its four bases, the resolution order, the entry template, the
  authority split, the page edits owed, and the red-first arrangement
  R1–R4. Implement it exactly; do not re-derive it.
- `ITEMS.md`, entry `## st-35` — its `amended-done-criterion` dated
  2026-09-12 is the acceptance list.
- `plugin/skills/statiker/SKILL.md` — the four passages the ruling
  names: the arming clause (content anchor: "arming a LIVE run means
  editing the Budget header line in place"), and the three that stay
  untouched (content anchors: "Status and Phase are the only mutable
  fields"; "The record's one mutable surface is"; "the two mutable
  field lines exempt").
- `plugin/skills/statiker/scripts/statiker_record.py` — `cmd_tripwire`
  (content anchor: `TRIPWIRE_BUDGET_RE.search(meta["budget"] or "")`),
  and the budget-raise precedent the ruling builds on.

## Background (established; verify at the cited lines)

Line numbers are as of the ruling's own reads; the st-34 lane moved
some of them, so the CONTENT ANCHORS above are authoritative and the
numbers are not.

1. The page already rules the appended way for the budget BOUND on the
   same header line: "An operator raise LANDS as an ordinary entry
   quoting the operator's line (the header is pinned surface, never
   rewritten), and every later exhaustion check reads the LATEST such
   entry over the header's default", with the template
   `- F<n> [VERIFIED] record: budget raised to cycles <n> / rounds <n>
   / verify <n> — "<operator's line verbatim>" — basis: operator`.
   Opened by the dispatcher at SKILL.md:291-303.
2. `record: ` is an existing scope opener (`SCOPE_EXACT_RE`,
   statiker_record.py:378), and a `record: `-scoped F-line is already
   classified as desk bookkeeping and excluded from "the newest round's
   findings" (:2265-2280). `basis:` is free text — only id citations
   are extracted (:885). **So this change needs NO new grammar.**
3. `_mutable_field_positions` (statiker_record.py:2682-2695) exempts
   the first `Status:` and first `Phase:` lines only. It is NOT yours —
   the ruling leaves it untouched deliberately.
4. A header `tripwire 0` gives `USAGE_ERROR` exit 3 today
   ("Budget line's `tripwire <n>` field must be >= 1"), at every round
   open. **The st-34 lane has since widened that refusal** to any
   present-but-unparseable value — read `cmd_tripwire` as it stands at
   your base, not as this paragraph describes it, and report any
   divergence.

## The settled design — implement exactly this, do not redesign

The ruling's own words govern. Restated here only as the work
breakdown:

**(1) Tool — the resolution order.** `tripwire` resolves its threshold
as: `--threshold` (always overriding) > the LATEST appended arming
entry > the header Budget line's `/ tripwire <n>` field > unarmed. The
`>= 1` refusal (and st-34's widened non-integer refusal) applies to
WHICHEVER SOURCE DECIDES. Ordering is the point of the ruling: an
appended arm must REPAIR a record seeded with a bad header value, so
the header must not be consulted once an arming entry exists.

**(2) Tool — the entry the reader looks for.** One form, the quote
optional:
`- F<n> [VERIFIED] record: tripwire armed at <n>[ — "<the operator's
line verbatim>"] — basis: <operator|desk>`
Latest-line-wins, the same shape the budget-raise read uses. The
`basis:` value is NOT gated by the tool (see (4)).

**(3) Page.** The in-place arming clause is replaced by the appended
route, and its sentence "an amendment F-line records the operator's
authority but never arms" GOES — it stops being true. The three
passages named in the Grounding basis stay byte-unchanged; so does
`_mutable_field_positions`.

**(4) Authority stays PROSE, deliberately — do not mechanize it.** The
page states: arming, or tightening an armed tripwire, is the desk's;
RAISING the threshold or disarming is an operator decision, the same
split the budget bound already carries. The tool does not check this.
Building a gate for it is a deviation, not an improvement — the ruling
records why (the incident population for a desk loosening its own
breaker is zero).

## Verifier (in order; real output pasted in the report)

Baseline FIRST, in every arm: the unmutated result, stated before the
red. A red over an already-red baseline proves nothing.

1. **R1 (the bite).** A tracker pinned with header `/ tripwire 0` plus
   an appended `- F<n> [VERIFIED] record: tripwire armed at 2 — basis:
   desk`. TODAY: `USAGE_ERROR` exit 3. AFTER: armed at 2. The probed
   result must equal the outcome named (armed at 2) AND differ from the
   unprobed one — paste both.
2. **R1b (the control that records why the route changed).** On the
   same record: repairing it by editing the Budget line IN PLACE gives
   `pinned` → `PINNED_REWRITTEN`, before AND after your change; the
   appended route gives `PINNED_APPEND_ONLY`, before AND after. This
   arm must show NO movement — it is the evidence that the ruling moved
   the page to the tool and not the tool to the page. Movement here is a
   finding: report it, do not repair it.
3. **R2 (control).** No appended arming entry → the header field still
   decides. Unchanged.
4. **R3 (control).** `--threshold 3` with an appended arm at 2 → 3
   wins. Unchanged.
5. **R4.** An appended arm at `0` → refused, and the error message
   names the ENTRY as the source, not the Budget line.
6. `python3 -m pytest tools/ -q` — FULL counts including skips, every
   skip dispositioned. Baseline: the count at your base commit, stated.
7. `awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'`
   — the operational-line count, printed for the record, with the base
   count beside it.

## Write boundaries

Paths you own:
- `plugin/skills/statiker/SKILL.md` (the arming clause only)
- `plugin/skills/statiker/scripts/statiker_record.py`
- `tools/test_statiker_record.py`

Touch nothing else — in particular NOT `_mutable_field_positions`, NOT
`statiker_emit.py` or `statiker_git.py` (st-32's lap, next), NOT
`ITEMS.md`, `LEDGER.md`, `dev-notes/OBSERVATIONS.md`, `docs/`.

Shared working copy: commit by pathspec only —
`git commit -m "…" -- <paths>`, every flag BEFORE the `--`, `-F` for a
multi-line message. Never `git add` then `git commit`, never `-A`, never
`--amend`. Commits UNPUSHED; the dispatcher pushes after verifying.
Nothing in your write set is live on write (the payload reaches a desk
only through an installed pin).

## Commit plan

The global `pre-commit` at
`core.hooksPath=~/dev/Gunther-Schulz/dotfiles/git/hooks` blocks a
PAYLOAD commit whose plugin version equals the ORIGIN manifest's.
`plugin/skills/statiker/SKILL.md` and `statiker_record.py` are payload.
The manifest was bumped to `0.2.89` by the st-34 lane and the batch is
UNPUSHED, so the exemption is ARMED and you bump nothing. If a commit
bounces on that guard, the batch was pushed — HALT and report, never
`--no-verify`.

Pre-authorized repair class: if the commit plan collides with a repo
guard, reorder to satisfy the guard and report the permutation as a
deviation. Novel deviations halt.

Commit title pattern: `st-35: <what>`.
Trailer, verbatim:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`

## Critique pass (one message, BEFORE your first build call)

Which Background line above do you find unopened or wrong, and which two
lines of this brief contradict each other? Send it on the report
channel, then continue without waiting for a reply. This one fires
before the first EDIT, not after three of them.

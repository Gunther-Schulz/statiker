# Brief — record-tool batch: st-86, st-66, st-89 (2026-10-07)

Title: sonnet: record-tool batch st-86 / st-66 / st-89
Working copy: /home/g/dev/Gunther-Schulz/statiker (shared with the
dispatching desk, which writes ITEMS.md, LEDGER.md, CLAUDE.md and
dev-notes/ only while you run).
Base check: this brief's own commit, or any later HEAD whose extra
commits leave your write-set paths untouched. First act:
`git -C /home/g/dev/Gunther-Schulz/statiker log --oneline -8` and
`git -C /home/g/dev/Gunther-Schulz/statiker status --porcelain -- plugin tools`
— a modified file inside your write set is a HALT, reported as a gap.
Scratch: your OWN scratchpad.

Before your first build call send ONE message to the dispatcher:
which Background line below you find unopened or wrong, and which
two lines of this brief contradict each other ("none" is valid).
Then continue without waiting for a reply.

## Grounding basis — read before building; the report cites what was actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST
- the `skill-craft:skill-craft` skill — load before any edit to
  `plugin/skills/statiker/SKILL.md` (repo rule, CLAUDE.md
  "Single-home by design")
- `/home/g/dev/Gunther-Schulz/statiker/CLAUDE.md` — the
  "Birth-class discipline" bullet (what counts as a mint; the
  verdict-mint write-set sentence) and the `## Verify` block
- `plugin/skills/statiker/scripts/statiker_record.py` —
  `cmd_closure` whole; `cmd_filter` whole;
  `extract_containment_scope`; the `intent-near-miss` and
  `tripwire-arm-near-miss` lint classes end to end (regex, the
  `viol(...)` site, every set or dict that names the code)
- `tools/test_statiker_record.py` — the existing closure-void,
  containment and near-miss tests, for idiom
- `tools/test_contract.py` — whatever it asserts about lint codes,
  verdict fields and page/tool agreement
- `ITEMS.md` blocks `## st-86`, `## st-66`, `## st-89` (requirement,
  done-criterion, evidence — plus appended amendment lines)

## Background (each line: opened by the dispatcher today, or graded)

- `cmd_closure` computes `post` (every F/D/R entry appended after
  the closing A-line) and voids on a post-closure `[INVALIDATED]`
  of an entry live at the closure, with `why` = "invalidates an
  entry live at the closure" — opened: statiker_record.py:2340-2361
  at commit f050235.
- The scopeless branch one step below carries a
  `latest[e.id] is e` guard; the invalidation branch has none and
  `continue`s — opened: same file, 2362-2378.
- The page already states void-always for this branch and that
  "the closure voids and the design re-enters" — opened:
  SKILL.md:1478-1483 and SKILL.md:561-563.
- `closure` emits `scopeless` on CLOSURE_VOID and `amendments` on
  UNIT_DISPATCHABLE and no field carrying a record-scoped
  post-closure line — opened: statiker_record.py:2379-2428.
- `CONTAINMENT_EXACT_RE = ^CONTAINMENT: (\S+)$`;
  `extract_containment_scope` reads raw tracker lines; `cmd_filter`
  gates only `if containment_scope:` — so a malformed label reads
  as no scope and the gate does not arm — opened:
  statiker_record.py:336, 2993-3004, 3132-3137.
- The tripwire precedent: a loose NEAR regex plus "near and not
  exact" raises `tripwire-arm-near-miss` — opened:
  statiker_record.py:205-216 and 1381-1389.
- The preflight verdict (which carries `containment_scope`) is
  printed by `statiker_git.py` and transcribed by the desk; the
  record tool has no input that says a scope was declared when no
  label line exists — from statiker_git.py:1352-1377 and
  SKILL.md:246-258, read today; that NO other record line carries
  it is inferred, unverified.
- Suite baseline: `python3 -m pytest tools/ -q` → `683 passed, 7
  subtests passed` — run by the dispatcher today at f050235, before
  three later commits that touch CLAUDE.md, dev-notes/, ITEMS*.md
  and LEDGER.md only.
- Manifest: `plugin/.claude-plugin/plugin.json` version 0.2.105,
  pushed; installed pin 0.2.103 — opened today.

## The settled design — implement exactly this, do not redesign

Three items, in this order, one commit each (tool + its tests
together), then page edits in their own commit(s).

### A. st-86 — void-always, with the recovery route named (a REPAIR, not a mint)

Decision (desk, 2026-10-07): the branch keeps voiding on EVERY
post-closure `[INVALIDATED]` of an entry live at the closure,
whatever its scope and whatever follows it. No same-id resolution,
no `latest` guard. Reason: a post-closure invalidation is a design
change after the closing round; the forcing point is that the
change gets a round.

Change: the branch's `why` text (and therefore the `closure VOID:`
say line and the `scopeless[].why` value) names the recovery route.
Use exactly:

    invalidates an entry live at the closure — a design change after
    the closing round: the design re-enters and closure returns only
    with a NEW closing A-line; a same-id restatement does not
    restore it

(one string; wrap in source as you like). No new verdict token, no
new verdict field, no change to which records void.

Tests, drawn from the F104 incident shape (st-86 requirement):
1. a unit-scoped post-closure `[INVALIDATED]` of an entry live at
   the closure → CLOSURE_VOID, and the `why` contains
   "NEW closing A-line".
2. the same record plus a later same-id LIVE restatement of that
   entry → still CLOSURE_VOID (this pins void-always; it separates
   this branch from the scopeless branch, where a same-id scoped
   restatement DOES resolve).
3. control, existing behaviour: a scopeless post-closure
   non-invalidation line resolved by a same-id scoped restatement
   does not void (cite the existing test if one covers it; add one
   only if none does).
Red-first: run the new assertions against the unmodified tool
first and paste that output — arm 1 must be RED there on the
message; say explicitly which arms are green-on-old pins.

### B. st-66 — closure emits the post-closure population (a C4b MINT: hypothesis-patch)

Decision (desk): a new verdict field, not a recorded exception.
Name: `post_closure`. Value: one object per member of `post`, in
record order: `{"line": "<id> [<tag>] <body>", "lineno": <n>}` —
the same line rendering `scopeless` and `amendments` already use.
Emitted on EVERY `finish(...)` that `cmd_closure` reaches after
`post` is computed (CLOSURE_VOID, CLOSURE_LEAVINGS_HOLD,
CLOSURE_LIVE, UNIT_UNKNOWN, UNIT_HELD, UNIT_DISPATCHABLE). Present
and EMPTY (`[]`) when no F/D/R line follows the closing A-line. No
filtering by scope, tag or latest-per-id: the field is the
population, the existing fields stay the verdicts over it.

Tests: RED-first on a tracker carrying a record-scoped post-closure
line that no current field reports (assert it appears in
`post_closure`; red on the old tool); green after; and a tracker
with no post-closure line yields `post_closure == []` with the
verdict unchanged.

Page edit (after the tool commit): find the verify-brief demand
that asks for a statement per F/D/R line appended after the last
A-line (search the page for `appended after`; report the line you
edited). Add at most three lines saying the population is read
from the closure verdict's `post_closure` field, in the page's own
idiom (current decision, plain, no history). Do not touch the
"last resolved A-line" wording itself — that is a separate recorded
item.

### C. st-89 — a malformed containment label fails CLOSED and lints (a C4b MINT: hypothesis-patch)

Decision (desk): detector 1 is built in two places; detector 2 (the
skipped-transcription cross-check) is DECLINED — the record carries
no input that says a scope was declared. Do not build it.

1. `CONTAINMENT_NEAR_RE = re.compile(r"(?i)^\s*containment\s*:")` —
   a line that looks like a label attempt. Near-miss = matches NEAR
   and does not match `CONTAINMENT_EXACT_RE`.
2. Lint: a new code `containment-near-miss`, raised on each
   near-miss line. Mirror `intent-near-miss` exactly for placement
   and for membership in every set, dict or tuple that names lint
   codes (mint-version table at the CURRENT manifest version,
   machine-token sets, blocking sets — whatever `intent-near-miss`
   is in, this is in; whatever it is not in, this is not). Report
   the list of places you added it.
3. Gate: in `cmd_filter`, before the `if containment_scope:` test,
   collect near-miss lines from the same raw `lines`; if any exist,
   `finish("ARTIFACT_CONTAINMENT_HOLD", 2, ...)` with the existing
   fields the hold already carries plus
   `malformed_containment=[<the raw lines>]`. Existing token, no new
   route. A record with only exact labels, or with no label-shaped
   line at all, behaves exactly as today.

Tests, red-first: (a) `Containment: /x` and `CONTAINMENT:/x` and
`CONTAINMENT: /x /y` each lint `containment-near-miss` and each
hold the filter with `malformed_containment` naming the line —
RED on the old tool (which reads them as no scope and passes);
(b) an exact label still gates exactly as before; (c) no
label-shaped line → no lint, no hold; (d) an ENTRY line whose body
merely contains the word (`- F3 [VERIFIED] record: containment:
discussed`) is neither linted nor held — the discriminating case
between a column-0 label attempt and prose.

Page edit: in the machine-token enumeration where `CONTAINMENT:
<path>` is described (search `CONTAINMENT: <path>`), add at most
four lines: a label-shaped line that is not the exact form lints
`containment-near-miss` and holds `filter` (ARTIFACT_CONTAINMENT_HOLD)
— a declared scope never silently downgrades to none.

### Not in scope

`statiker_emit.py` is NOT in your write set: no item adds a
`finish()` token. If the contract battery demands a ROUTES entry
anyway, HALT that item, finish the others, report the demand
verbatim. No change to `statiker_git.py`. No change to ITEMS.md,
LEDGER.md, CLAUDE.md, PLAN.md or dev-notes/ — the dispatcher writes
the mint records and tenet checks from your report.

## Verifier (in order; real output pasted in the report)

1. per item, the red-first run against the unmodified tool, then
   green after the change (the item's own tests by `-k`);
2. `python3 -m pytest tools/ -q` — the WHOLE suite; expected count
   is the baseline above plus your new tests, zero failed, zero
   skipped (a skip is a finding);
3. `python3 ~/.claude/plugins/cache/skill-craft-marketplace/skill-craft/2.2.8/tools/register_lint.py --band 52 30 plugin/skills/statiker/SKILL.md`
   — exit 0 expected (from CLAUDE.md `## Verify`, not re-run by the
   dispatcher today: unverified);
4. `git -C /home/g/dev/Gunther-Schulz/statiker status --porcelain`
   — clean except nothing.

## Write boundaries

Yours: `plugin/skills/statiker/scripts/statiker_record.py`,
`tools/test_statiker_record.py`, `tools/test_contract.py` (only the
rows the contract demands for the new lint code and field — report
each), `plugin/skills/statiker/SKILL.md` (only the two edits named
above, at most seven added lines in total; report verbatim
before/after). Nothing else. Not deployment-coupled: the installed
plugin is pinned at 0.2.103 and serves from the cache, so nothing
you write is live on write. Never push. Never amend — always a new
commit.

## Commit plan

Guards read by the dispatcher: `core.hooksPath` =
`~/dev/Gunther-Schulz/dotfiles/git/hooks` (pre-commit, pre-push,
post-commit). The pre-commit is a payload-version guard: plugin
payload committed without a version bump is refused, on VERSION
EQUALITY (header lines 2-36 read; the comparison basis — installed
pin versus origin manifest — was not traced: unverified). The
manifest is at 0.2.105, pushed. PRE-AUTHORIZED repair class: if a
payload commit bounces on that guard, bump
`plugin/.claude-plugin/plugin.json` to 0.2.106 (and any mirror the
guard names) in its own commit FIRST, then proceed, and report it
as a deviation; use 0.2.106 as the mint version in that case.
Never `--no-verify`.
Order: A (tool+tests) → B (tool+tests) → C (tool+tests) → page
edit(s). Commit titles: `st-86: …`, `st-66: …`, `st-89: …`,
`st-66/st-89: page …`. Trailer, exactly:
`Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`

## Tail

    A mid-run message may not arrive before the turn ends: on a gap
    HALT THE ITEM, FINISH THE REMAINDER, REPORT — never halt the
    LANE, since "halt and wait" is not a survivable state for a
    subagent (source: §2, the delivery binding).
    Closing report (mandatory; the project's own report form if it
    defines one, else the §2 form here — never both; "none" is a
    valid slot answer, silence is not): (a) items completed w/
    evidence, (b) checks RUN w/ real output — FULL counts incl.
    skips (`N passed, M failed, K skipped`), each skip dispositioned
    (which check, why, whether the reason touches the item); a skip
    in a check YOU built is a finding, not a pass — the built branch
    did not execute, (c) gaps surfaced —
    incl. anything needing a tier above yours, returned as a question
    with its evidence, never settled at your tier,
    (d) deviations w/ reason, (e) candidate lessons, (f) files
    touched + commit hashes (unpushed) — only commits whose
    Co-Authored-By trailer is YOURS; one you cannot claim by
    trailer is "present in the tree, not mine"; a `.git/config`
    write counts as a repo write, (g) what was NOT verified,
    (h) sources actually read, of those the brief named.
    Every claim about something OUTSIDE your own work — a file you
    did not write, a mechanism, another repo, a tool's behavior —
    names the read that opened it, or carries "inferred,
    unverified"; a recommendation resting on an unopened claim
    carries the grade too.
    Drain your inbox before sending, and between parts of a
    multi-part report: every dispatcher message received up to send
    time is dispositioned or named as unhandled.
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
    Commits unpushed, by pathspec — `git commit -m "…" -- <paths>`
    with every flag BEFORE the `--` (after it git reads `-m` as a
    pathspec and the commit fails; `-F` for a multi-line message),
    never
    `git add` then `git commit` and never `-A`: the index is shared,
    so a co-writer staging between your `git status` and your commit
    rides out under your message whatever you added. A NEW file is
    invisible to a pathspec commit until `git add -N <path>`
    registers it (intent-to-add: zero content staged, full body
    still committed). Trailer:
    `Co-Authored-By: Claude <model> <noreply@anthropic.com>`.
    Never amend — always a new commit: the amend-gate denies
    subagent amends regardless of ownership (source: §1 amend
    rule).
    After sending the report your write grant is over: a defect you
    find later is REPORTED, never edited or amended (source: §4
    ownership rule).

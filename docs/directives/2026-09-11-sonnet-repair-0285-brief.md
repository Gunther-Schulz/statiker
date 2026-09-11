# Title: sonnet: 0.2.85 repair lap — re-review dispositions RB1–RT-a

Working copy: /home/g/dev/Gunther-Schulz/statiker.
Base check: `git merge-base --is-ancestor <base> HEAD` AND
`git log --oneline <base>..HEAD` where `<base>` is the commit that
added THIS brief file (find it: `git log -1 --format=%h --
docs/directives/2026-09-11-sonnet-repair-0285-brief.md`). Base
contained + nothing on top = clean start. Base not contained, or
commits on top, or dirty tree (`git status --porcelain`) = HALT and
report as a gap.
Scratch: your OWN scratchpad, never this repo or the dispatcher's.

## Grounding basis — read before building; the report cites what was actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST
- `dev-notes/OBSERVATIONS.md`, section
  `## 2026-09-10 — 0.2.84 re-review dispositions` (starts near line
  7999; anchor on that heading text, line numbers may drift) — the
  NORMATIVE disposition list. Each bullet RB1…RT-b is a settled
  disposition: finding, FIX, and the reviewer's red arm. Implement
  exactly the FIX sentences; the red arms are your test fixtures.
- `plugin/skills/statiker/scripts/statiker_record.py` — the tool
  under repair (sites listed per item below)
- `plugin/skills/statiker/SKILL.md` — the page; edits under
  skill-craft discipline (see Write boundaries)
- `tools/test_statiker_record.py`, `tools/test_contract.py` — the
  batteries the new tests join; match their idiom
- Critique pass (mandatory, before your first build call): ONE
  SendMessage naming which Background line below you find unopened
  or wrong, and which two lines of this brief contradict each
  other; then continue without waiting for a reply.

## Background (established; verify at the cited lines)

- Base HEAD at compose time: 41d1966 (read: `git rev-parse --short
  HEAD`, tree clean, nothing unpushed); the brief's own commit sits
  on top of it.
- Baseline suite: `python3 -m pytest tools/ -q` → `499 passed in
  31.68s`, 0 failed, 0 skipped (run at compose time, this desk).
  Your red-first arms run against this green baseline.
- Anchor reads (all at 41d1966, sed-verified at this desk):
  - `WRITE_SET_CORRECTS_SUFFIX_RE.sub` stripping at
    statiker_record.py:826-830 (the near-miss site).
  - `declarator-bookkeeping` complaint condition at
    statiker_record.py:1322-1328 (`latest_same_id`,
    `UNIT_WRITE_SET_RE` shape test, no unit-equality test, no
    INVALIDATED-tag test).
  - `waves_over_units` consumption at statiker_record.py:2053-2057:
    `m = UNIT_WRITE_SET_RE.match(e.body); raw = m.group(2).strip()`
    — consumes the RAW path, no corrects-suffix strip.
  - `REPAIR_FORMS = dict(` at statiker_record.py:609.
  - freeze-breach INLINE repair text (not in REPAIR_FORMS) at
    statiker_record.py:1585-1592.
  - Precedent-line prose at SKILL.md:490-495 (`A fourth literal
    set — the unit design's PRECEDENT LINE (Stop rule) …`).
  - Contract-check family: `emitted_verdicts()` at
    tools/test_contract.py:179;
    `test_every_emitted_verdict_is_driven_or_frozen` at :999;
    `test_every_emitted_verdict_is_routed_in_skill` at :1043 — so a
    NEW hold code (RN-b) must also be routed in SKILL.md or :1043's
    check goes red; that SKILL.md routing edit is in scope.
  - `RECORD_NAME_TOKEN_RE` and the B1 punctuation strip: from the
    dispositions (RN-c bullet) and commit 4c8716d, unverified at
    line grain — locate by grep before editing.
  - The delta-scoped clause RN-e amends: minted by desk commit
    34b33ec (`st-27: delta-scoped re-verification after repairs`) —
    locate its SKILL.md text via that commit's diff; from the
    dispositions, unverified at line grain.

## The settled design — implement exactly this, do not redesign

In-scope items, one commit each, in this order after the bump:
RB1, RB2, RN-a, RN-b, RN-c, RN-e, RN-f, RT-a. Out of scope: RN-d
(no action — parked at st-26) and RT-b (no change — residual
accepted on record). The FIX sentence of each disposition bullet is
the design — including: RB1's shared resolver named
`_normalize_write_set_path` homed at the consuming site and reused
by the near-miss site; RB2's unit-equality requirement
(`UNIT_WRITE_SET_RE` group 1 equal to `latest_same_id`'s); RN-a's
INVALIDATED-tag test in the condition; RN-b's new hold
`ambiguous-citation` with its repair text exactly as the
disposition states it, a mandatory REPAIR_FORMS entry, and the
SKILL.md routing entry the contract check demands; RN-c's reuse of
B1's punctuation-strip set for the record-name match; RN-e's ONE
carve-out sentence (a widening amendment re-classes the repair as
WORK); RN-f's repair-coverage contract check (every emitted code
has a REPAIR_FORMS entry), reading the freeze-breach inline-repair
allowance FROM SOURCE (:1585-1592 region), never as a hardcoded
exemption list; RT-a's reword of the SKILL.md:492-493 sentence to
clause-of-D-line pointing at the D-line clause (near :762).

Red-first per item: write the test from the disposition's red-arm
sentence as a fixture pair (the red case AND its control), run it
against the UNMODIFIED code — it must FAIL, output kept — then
apply the fix, re-run — it must PASS. Both outputs go in the
report, per item. A red arm that does not go red on the unmodified
code is a gap: HALT THE ITEM, report, continue with the rest.

## Verifier (in order; real output pasted in the report)

1. Per-item red-first pair as above (red output + green output).
2. `python3 -m pytest tools/ -q` — full suite after each commit;
   final run in the report with FULL counts. Baseline is 499
   passed, 0 skipped; any new skip is a finding.
3. `awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'`
   — operational line count, printed for the record (no gate).

## Write boundaries

Owned paths (nothing else; one writer — this desk does not write
the repo while your lane runs):
- `plugin/.claude-plugin/plugin.json` (bump commit ONLY)
- `plugin/skills/statiker/scripts/statiker_record.py`
- `plugin/skills/statiker/SKILL.md`
- `tools/test_statiker_record.py`
- `tools/test_contract.py`
Do NOT touch: dev-notes/, LEDGER.md, ITEMS.md, BACKLOG.md, docs/,
PLAN.md — booking is the dispatcher's.
Gate on SKILL.md: invoke the Skill tool `skill-craft:skill-craft`
BEFORE your first SKILL.md edit (repo CLAUDE.md, single-home
bullet). SKILL.md edits state current decisions cleanly, as if
final — no hedges, no history inline (repo CLAUDE.md, trial
conventions).
Not deployment-coupled: no written path is live on write (the
installed plugin copy is separate; the pin moves only at a desk
release, later, not in this lane).
Commits by pathspec — `git commit -m "…" -- <paths>`, flags before
`--`, never `git add` + `git commit`, never `-A`. Never amend —
always a new commit.

## Commit plan

Commit-blocking guards, each with the read that found it:
- Global pre-commit (read: `git config core.hooksPath` →
  `~/dev/Gunther-Schulz/dotfiles/git/hooks`; its pre-commit read at
  this desk): fires on a staged plugin-payload change whose
  manifest version equals HEAD's, UNLESS HEAD's version already
  differs from origin's. HEAD and origin both carry 0.2.84 today,
  so the FIRST commit is the bump: `plugin/.claude-plugin/
  plugin.json` version `0.2.84` → `0.2.85`, that file alone. Every
  later payload commit then passes while the batch stays UNPUSHED —
  and it stays unpushed: the exemption dies if anything pushes, so
  push NOTHING; the dispatcher pushes at integration.
- Global pre-push exists (fixture-leak scan) but you never push, so
  it never fires for you.
- No repo-local pre-commit/commit-msg hook (read: chaining note in
  the global hook; no hooks/ dir in this repo).
Then commits 2–9: one per item, ordered RB1, RB2, RN-a, RN-b,
RN-c, RN-e, RN-f, RT-a; title `<id>: <short imperative summary>`
(precedent: `4c8716d B1: strip quoting/bracketing punctuation from
basis id tokens`); each commit carries its tool/page change AND its
tests, by pathspec.
Trailer, verbatim, on every commit:
`Co-Authored-By: Claude Sonnet <noreply@anthropic.com>`

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
Report channel: SendMessage to the dispatcher — your final text
reaches no one.
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
`Co-Authored-By: Claude Sonnet <noreply@anthropic.com>`.
Never amend — always a new commit: the amend-gate denies subagent
amends regardless of ownership (source: §1 amend rule).
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended (source: §4
ownership rule).

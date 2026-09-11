# Title: opus: st-29 lap A stage 1 — per-clause disposition table over SKILL.md (no page edits)

Dispatcher: statiker-4d, 2026-09-11. Lane name: opus-lapA-table-0287.
Working copy: /home/g/dev/Gunther-Schulz/statiker.
Base check: `git merge-base --is-ancestor <base> HEAD` where `<base>`
is the commit that added THIS brief file (find it: `git log -1
--format=%h -- docs/directives/2026-09-11-opus-st29-lapA-clause-table-brief.md`).
Base not contained = HALT and report. Commits landing on top while you
run are expected (a checkpoint review and possibly a repair lap run in
this copy) and are not a halt: you read the page at a PIN, never live.
Scratch: `/tmp/claude-1000/-home-g-dev-Gunther-Schulz-statiker/f59bcaca-7615-4029-95ca-3a049796cc24/scratchpad/opus-lapA-table-0287/`
— that directory only (the scratch root is shared with other lanes),
never this repo.

## The task

Produce the per-clause disposition table that st-29's lap A applies:
for every paragraph of `plugin/skills/statiker/SKILL.md` AT PIN 769e7f2
(read it with `git show 769e7f2:plugin/skills/statiker/SKILL.md`), decide
KEEP / TIGHTEN / DELETE under the settled design's lap-A rules, with
the basis and provenance for each. You decide dispositions; you do not
edit the page. A later build lane applies your table exactly, so every
TIGHTEN row must say what survives precisely enough that composing the
shorter text is template-filling, not design.

## Grounding basis — read before building; cite what was actually read

- `docs/directives/2026-09-11-st29-compression-design-statiker-fb.md`
  (commits 1e10047 + 8e4f370) — the SETTLED design. §0 (verdict parity
  binds lap A), §1 (per-section dispositions and bases), §3 lap A, §4
  (the disposition table's form and the provenance rule), §5
  (disclosure deferred). Normative for this task.
- `ITEMS.md` item `st-29` — its latest `amended-done-criterion` line
  (STAGE 1 is this task).
- Repo `CLAUDE.md` — trial conventions: "Skill text states current
  decisions cleanly, as if final", the economics lens (the VALUE line:
  the forcing point that makes the fresh-context round happen, the
  round itself, and a record sufficient for the round to read and a
  successor to resume), self-containment criterion and its bound,
  birth-class discipline.
- `PLAN.md` `## Mission and tenets` (~:32-70; the 2026-08-26 cut line:
  machinery serving the value is core, machinery serving only the
  record's own consistency is the record protecting itself), and its
  tenet list items 1–9.
- `begehung-findings-2026-09-10-r4.tsv` (repo root, 13 rows) — the R4
  per-mechanism value table the design orders deletes by.
- `BEGEHUNG-MAP.md` rows at ~:28 (certified-attack register — dark) and
  ~:31 (CROSS-CUTTING lifecycle — dark).
- `dev-notes/clippy-lineage.md` — the lineage register (CLAUDE.md: load
  at the compression pass); loosely informing, never a design-against
  list.
- `tools/test_contract.py` `class TestVerdictParity` (~:1042-1058) — the
  bidirectional page/tool verdict parity every lap-A row must keep.
- `dev-notes/OBSERVATIONS.md` — for provenance pointers ONLY, by search
  (grep a clause's P-id, F-id, incident name, or distinctive phrase);
  never read whole.

## Background (opened by the dispatcher at 769e7f2 / c2aa2d4)

- SKILL.md at 769e7f2: 1766 operational lines by the CLAUDE.md Verify
  awk (which also counts the closing frontmatter fence). `## ` sections
  at lines 20 Composition, 41 The tools, 146 The record, 584 The loop,
  672 Stop rule, 940 The attack, 1291 Implementation, 1570 Verify, 1682
  Close, 1778 Fire-born and hypothesis clauses, 1796 Birth-class
  declaration; the preamble `# Statiker` precedes them.
- Design §2 projects lap A to ~1100–1200 lines, from a scratch run on
  The tools (102 → 60, statiker-fb-measured, not re-run at this desk).

## The settled rules — apply exactly, do not redesign

Row unit: one paragraph (a blank-line-delimited block, or one list
item). Split a paragraph into clause rows only where its sentences take
different dispositions.

Dispositions (lap A only):
- KEEP — stands as written.
- TIGHTEN — same semantics, shorter prose. The row lists its
  MUST-SURVIVE items (every rule, condition, token, and pointer the
  shorter text must still carry) and a target line count.
- DELETE — the paragraph or clause leaves the page. Admissible only
  when the row names WHERE its load is already stated (another page
  passage by quoted handle, or the tool's own verdict text by verdict
  name), or states that it carries no load (incident narration,
  superseded hedge, history, a derivation the page itself forbids
  using).
Hard constraints:
1. No verdict token leaves the page (TestVerdictParity). A DELETE or
   TIGHTEN row lists every verdict-shaped token (UPPER_SNAKE verdict
   names, hold codes) its text carries and where each survives.
2. Write-side templates the desk composes FROM (entry forms, header
   spec, raise lines, SWEEP_EXEMPT forms) and paste artifacts (the
   verbatim attack question block) are KEEP (design §1).
3. Per-verdict routing masses the design assigns to lap B (the tools
   routing residue, lock routes (c)/(d), unit START/COMMIT routes,
   record read-side semantics, attack trend/sustain/tripwire routing)
   are KEEP in lap A, marked `B`; tighten them only where pure
   restatement, never by moving semantics.
4. Disclosure candidates (RETRO-netting, batched-trip machinery,
   version-mismatch resume — design §5) are KEEP, marked `§5`.
5. A paragraph serving a dark Begehung row (certified-attack register;
   CROSS-CUTTING artifact lifecycle — homes, writers, readers) is KEEP
   unless its load is stated elsewhere by quoted handle; mark it `dark`.
6. Mints of the 0.2.84–0.2.87 releases (fresh provenance) are KEEP or
   TIGHTEN, never DELETE (design §1, Implementation row).

## Deliverable

ONE file: `docs/directives/2026-09-11-st29-lapA-clause-table.md`, with:
1. A header: pin (769e7f2), the rules above cited by number, and a
   per-section summary table: section | lines now | KEEP / TIGHTEN /
   DELETE row counts | projected lines after lap A.
2. Per section, a table: `row | line range at pin | handle (quoted
   opening words, ≤12, grep-exact in the pinned page) | disposition |
   must-survive (TIGHTEN) or load-stated-at (DELETE) | verdict tokens
   carried | basis (design §-ref, R4 row, CLAUDE.md convention, tenet)
   | provenance (OBSERVATIONS date + P/F-id, "birth" for base payload,
   or "not found — searched <terms>") | marks (B / §5 / dark)`.
3. A closing tally: projected total vs design §2's lap-A band, and every
   row where you were torn between two dispositions, listed with both
   readings (these are graded at the desk first).
Commit it by pathspec: `git add -N <file>`, then `git commit -m "st-29
lap A stage 1: per-clause disposition table over SKILL.md at 769e7f2"
-- <file>`. Unpushed.

## Verifier (real output in the report)

1. Handle check: every row's handle appears exactly as quoted in `git
   show 769e7f2:plugin/skills/statiker/SKILL.md` — run a script over
   your table (in your scratch dir) and paste its counts: rows, handles
   found, handles not found (must be 0), handles matching more than one
   place (listed).
2. Token check: the set of verdict-shaped tokens in the pinned page
   (derive it with a regex you state, and prove the regex live on a
   known token such as `SWEEP_CLEAN`) minus the tokens your DELETE rows
   remove without a stated survivor — must be empty; paste the count.
3. Coverage check: every line range of the pinned page's operational
   body falls in exactly one row — paste uncovered and double-covered
   counts (both must be 0).

## Write boundaries

You write ONE file: `docs/directives/2026-09-11-st29-lapA-clause-table.md`.
Touch nothing else — not SKILL.md, the tool, tests, ITEMS.md,
ITEMS-DONE.md, LEDGER.md, OBSERVATIONS.md, PLAN.md, CLAUDE.md. Not
deployment-coupled.

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
`Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
Never amend — always a new commit: the amend-gate denies subagent
amends regardless of ownership (source: §1 amend rule).
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended (source: §4
ownership rule).

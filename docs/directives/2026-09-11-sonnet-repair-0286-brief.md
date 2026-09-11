# Title: sonnet: 0.2.86 repair lap — 0.2.85 checkpoint-review dispositions B1–T4 + st-14

Working copy: /home/g/dev/Gunther-Schulz/statiker.
Base check: `git merge-base --is-ancestor <base> HEAD` AND
`git log --oneline <base>..HEAD` where `<base>` is the commit that
added THIS brief file (find it: `git log -1 --format=%h --
docs/directives/2026-09-11-sonnet-repair-0286-brief.md`). Base
contained + nothing on top = clean start. Then `git status
--porcelain` over your owned paths (Write boundaries) must be empty.
Base not contained, commits on top touching your owned paths, or a
modified owned path = HALT and report as a gap. (Another session may
commit ONE file, docs/directives/2026-09-11-p28-design-statiker-ba.md,
while you run — that commit is expected and is not a halt.)
Scratch: your OWN scratchpad, never this repo or the dispatcher's.

## Grounding basis — read before building; the report cites what was actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST
- `dev-notes/OBSERVATIONS.md`, section headed
  `## 2026-09-11 — 0.2.85 checkpoint-review dispositions` (anchor on
  that heading text) — the NORMATIVE list. Each bullet B1…T5 is a
  settled disposition: finding, FIX, red arm. Implement exactly the
  FIX sentences. T5 is no-change.
- `ITEMS.md`, item `st-14` — its latest `amended-requirement` and
  `amended-done-criterion` lines are the normative text for the
  bundled four items.
- `plugin/skills/statiker/scripts/statiker_record.py` — the tool
- `plugin/skills/statiker/SKILL.md` — the page; edits under
  skill-craft discipline (see Write boundaries)
- `tools/test_statiker_record.py`, `tools/test_contract.py` — the
  batteries; match their idiom (RecordFixture, `violation_codes`,
  `waves`, `lineno_of`)
- Critique pass (mandatory, before your first build call): ONE
  SendMessage naming which Background line below you find unopened
  or wrong, and which two lines of this brief contradict each
  other; then continue without waiting for a reply.

## Background (established; verify at the cited lines)

- Base HEAD at compose time: b6d5beb (read: `git rev-parse --short
  HEAD`, tree clean, nothing unpushed); the brief's own commit sits
  on top of it.
- Baseline suite: 512 passed, 0 failed, 0 skipped — run by the
  reviewer at 49e9529 (from its report, unverified at this desk);
  plugin/ and tools/ are unchanged from 49e9529 to the brief's
  commit (checked by the dispatcher with `git diff --stat 49e9529
  HEAD -- plugin tools` at commit time). Your red-first arms run
  against this baseline; run the suite yourself first and state its
  counts.
- Anchor reads at b6d5beb (dispatcher, sed):
  - `"ambiguous-citation": "0.2.85",` in RULE_MINT_VERSION,
    statiker_record.py:276.
  - `REPAIR_AMBIGUOUS_CITATION = (` just above REPAIR_LANDING_MISSING
    (~:589-594), and `+ [("ambiguous-citation",
    REPAIR_AMBIGUOUS_CITATION)])` closing REPAIR_FORMS at :632.
  - The hold emission in the live-basis scan, :1717-1732: `if
    foreign:` … `if cited in latest:` … `"code":
    "ambiguous-citation"` … `continue`.
  - `REPAIR_DECLARATOR_BOOKKEEPING = (` at :577-581; its text says
    "restate the full write-set under the same id" and names no unit.
  - Near-miss site in write_set_violations, :837-845: `path =
    _normalize_write_set_path(rest[len("write-set: "):])` then `len(
    path.split()) > 1 or path.startswith("/")`.
  - `def _normalize_write_set_path(p):` at :2061 (strips the corrects
    suffix, then normalizes).
  - waves_over_units alias, :2121-2125: `raw = m.group(2).strip()`,
    `norm = _normalize_write_set_path(raw)`, `aliases.setdefault(norm,
    set()).add(raw)`.
  - SKILL.md declarator-bookkeeping clause (~:514-519): "UNLESS the
    correcting line is itself a fresh `unit U<k> write-set: <path>`
    redeclaration".
  - SKILL.md record-name token definition (~:548-551): "a token
    containing `/` AND ending `.md` or `.md:`, or the two-token label
    `run <name>:`".
  - SKILL.md ambiguous-citation sentence (~:559-564): "A record-named
    id that ALSO resolves in this run's own namespace is ambiguous
    — … `ambiguous-citation` (name the record for a foreign id, or
    drop the record name for the same-run id)."
  - SKILL.md:1669: "except a reconciliation that WIDENS the R-line's
    demand, which re-classes as WORK".
  - tools/test_contract.py:1177 `class
    TestRNfRepairFormCoverage` — its docstring claims "every
    violation code the tool can emit".
  - tools/test_statiker_record.py: `class
    TestRB1WriteSetCorrectsSuffixSharedWithWaves` :4646 (fixture
    `_tracker_with_repaired_declarator` targets a clean `wrong.txt`
    line), `class TestRNaDeclaratorBookkeepingInvalidatedExempt`
    :4742, `class TestRNbAmbiguousCitation` :4782.
  - st-14 sites: `finish("ARTIFACT_WRITTEN", 0, sha=args.sha,` at
    :2605; `p.add_argument("--threshold", type=int)` at :2834 with
    `if threshold is None:` at :2429; cmd_sustain docstring "a new
    round opens only if" at :2340; SKILL.md "clause (b)" occurs once
    (:1281). The re-lock passage (~:1145) and cmd_verify_gate's sha
    resolution (~:2732-2745, the form to mirror) are from a
    discovery lane's report, unverified at line grain — locate by
    grep before editing.
- The pre-commit guard reads HEAD's manifest version against
  origin's (see Commit plan). No other repo-local hook.

## The settled design — implement exactly this, do not redesign

One commit per item, in this order after the bump: B1, N1, N2, N3,
T1, T2, T3, T4, st-14. The FIX sentence of each disposition bullet is
the design, including:

- B1: remove the `ambiguous-citation` emission (restoring the
  pre-0.2.85 `continue` for foreign ids), REPAIR_AMBIGUOUS_CITATION,
  its REPAIR_FORMS entry and its RULE_MINT_VERSION row; replace the
  SKILL.md sentence with ONE sentence stating the reach: an id under
  a record-name token is not checked against this run's own
  invalidations. Replace TestRNbAmbiguousCitation with the B1 arms
  below.
- N1: waves_over_units records the suffix-stripped spelling as the
  alias; RB1's test re-pointed at the sanctioned shape below and
  asserting `spellings == {}` beside `serialize`.
- N2: a suffix-strip helper shared by write_set_violations and
  waves_over_units; normpath applied only in waves_over_units (keep
  `_normalize_write_set_path` as the consuming site's resolver built
  on the helper). Update both functions' comments to the new split.
- N3: the SKILL.md clause and REPAIR_DECLARATOR_BOOKKEEPING both say
  the redeclaration is by the SAME unit.
- T1: SKILL.md:1669 wording becomes "an amendment or reconciliation
  that WIDENS the R-line's demand".
- T2: TestRNfRepairFormCoverage's docstring states its reach: literal
  code strings at emission sites; a code emitted from a variable is
  outside it.
- T3: the SKILL.md record-name token definition names the
  quoting/bracketing strip (`()[].,;:`) applied before the match.
- T4: TestRNa re-pointed at the body-content target below.
- st-14: its four items exactly as its done-criterion states; items
  (1) and (5) get battery cases.

Reviewer's fixture bodies (tracker body lines appended after the
fixture header; `<n>` = the line number `lineno_of` returns for the
quoted needle):

- B1 red (sweep; SWEEP_HOLDS ambiguous-citation today, SWEEP_CLEAN
  after):
  `- F20 [VERIFIED] this run's own finding twenty — basis: probe` +
  `- D1 [COMMITTED] rests on the other run — basis:
  dev-notes/other-run.md F20`; same with `basis: run other-run: F20`.
  Control (clean both ways): same with `dev-notes/other-run.md F7`.
  Residual pin (no ambiguous-citation and no basis-cites-invalidated
  after): `- F20 [INVALIDATED] our claim died — basis: probe` + `- D1
  [COMMITTED] rests — basis: dev-notes/tracker.md F20`.
- N1 red (waves): `- F1 [VERIFIED] unit U1 write-set: a.txt — basis:
  design`, `- F2 [VERIFIED] unit U2 write-set: a.txt b.txt — basis:
  design`, `- F2 [VERIFIED] unit U2 write-set: a.txt (corrects line
  <n of "a.txt b.txt">) — basis: the verdict` → one wave [U1,U2],
  serialize true, spellings {} after (non-empty today). Control:
  plain `U1 a.txt` / `U2 a.txt`, spellings {}.
- N2 red (lint + waves): `- F1 [VERIFIED] unit U1 write-set: a.txt
  b/../c.txt — basis: design`, `- F2 [VERIFIED] unit U2 write-set:
  a.txt — basis: design` → LINT_VIOLATIONS write-set-path-near-miss
  and WAVES_RECORD_MALFORMED after (LINT_CLEAN / WAVES_COMPUTED
  today). Control: `a.txt c.txt` fires both ways.
- T4 (lint): `- F2 [VERIFIED] unit U1 write-set: a.txt`, `- F2
  [INVALIDATED] unit U1 write-set: a.txt dead (mis-scoped) — basis:
  F9`, `- F2 [VERIFIED] record: corrects line <n of the first line>
  — basis: the basis-missing verdict at line <n>` → LINT_CLEAN at
  HEAD. Live control: second line `[VERIFIED] … a.txt — basis:
  design` keeps its current verdict. Red: remove RN-a's
  INVALIDATED-tag test from the declarator-bookkeeping condition in
  the working tree, run, keep the output, restore with `git checkout
  -- plugin/skills/statiker/scripts/statiker_record.py`, confirm `git
  diff` shows no mutant hunk before committing.

Red-first per mechanized item (B1, N1, N2, T4, st-14 items 1 and 5):
write the test from the red arm as a pair (red case AND control), run
it against the UNMODIFIED code — it must FAIL, output kept — then
apply the fix, re-run — it must PASS. Both outputs in the report, per
item. A red arm that does not go red is a gap: HALT THE ITEM, report,
continue with the rest. Prose items (N3, T1, T2, T3, st-14 items 4
and 6) carry no red arm; the suite stays green.

## Verifier (in order; real output pasted in the report)

1. Per-item red-first pair as above (red output + green output).
2. `python3 -m pytest tools/ -q` — full suite after each commit;
   final run in the report with FULL counts. Any new skip is a
   finding. The contract checks (P5 mint registry, RN-f repair
   coverage) must stay green after B1's removal.
3. `awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'`
   — operational line count, printed for the record (no gate).

## Write boundaries

Owned paths (nothing else; one writer per path):
- `plugin/.claude-plugin/plugin.json` (bump commit ONLY)
- `plugin/skills/statiker/scripts/statiker_record.py`
- `plugin/skills/statiker/SKILL.md`
- `tools/test_statiker_record.py`
- `tools/test_contract.py`
Do NOT touch: dev-notes/, LEDGER.md, ITEMS.md, ITEMS-DONE.md,
BACKLOG.md, docs/, PLAN.md — booking is the dispatcher's.
Gate on SKILL.md: invoke the Skill tool `skill-craft:skill-craft`
BEFORE your first SKILL.md edit (repo CLAUDE.md, single-home
bullet). SKILL.md edits state current decisions cleanly, as if
final — no hedges, no history inline (repo CLAUDE.md, trial
conventions). Code comments may cite the disposition id.
Not deployment-coupled: no written path is live on write (the
installed plugin copy is separate; the pin moves only at a desk
release, later, not in this lane).
Commits by pathspec — `git commit -m "…" -- <paths>`, flags before
`--`, never `git add` + `git commit`, never `-A`. Never amend —
always a new commit.

## Commit plan

Commit-blocking guards, each with the read that found it:
- Global pre-commit (read: `git config core.hooksPath` →
  `~/dev/Gunther-Schulz/dotfiles/git/hooks`; its pre-commit
  :159-173 read at this desk): fires on a staged plugin-payload
  change whose manifest version equals HEAD's, UNLESS HEAD's version
  already differs from origin's. HEAD and origin both carry 0.2.85
  (pushed at 3016b72), so the FIRST commit is the bump:
  `plugin/.claude-plugin/plugin.json` version `0.2.85` → `0.2.86`,
  that file alone. Every later payload commit then passes while the
  batch stays UNPUSHED — push NOTHING; the dispatcher pushes at
  integration, and no other writer in this copy pushes while you run.
- Global pre-push exists (fixture-leak scan); you never push.
- No repo-local hook (read: no hooks/ dir in this repo).
Then commits 2–10, one per item: `B1: …`, `N1: …`, `N2: …`, `N3: …`,
`T1: …`, `T2: …`, `T3: …`, `T4: …`, `st-14: …` (`<id>: <short
imperative summary>`; precedent `e2af662 RB1: strip the write-set
corrects-suffix through one shared resolver, …`); each carries its
tool/page change AND its tests, by pathspec.
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

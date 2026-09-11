# Title: sonnet: 0.2.87 lap — st-28 (golden-corpus sweep test) + st-30 (0.2.86 re-review residue, 8 items)

Dispatcher: statiker-4d, 2026-09-11. Lane name: sonnet-lap-0287.
Working copy: /home/g/dev/Gunther-Schulz/statiker.
Base check: `git merge-base --is-ancestor <base> HEAD` AND
`git log --oneline <base>..HEAD` where `<base>` is the commit that
added THIS brief file (find it: `git log -1 --format=%h --
docs/directives/2026-09-11-sonnet-lap-0287-brief.md`). Base contained
+ nothing on top = clean start. Then `git status --porcelain` over your
owned paths (Write boundaries) must be empty. Base not contained,
commits on top touching your owned paths, or a modified owned path =
HALT and report as a gap. Expected co-writer commits while you run,
none of them a halt: ONE file
`docs/directives/2026-09-11-st29-compression-design-statiker-fb.md`
(another session), and desk commits touching only ITEMS.md, LEDGER.md
or dev-notes/.
Scratch: `/tmp/claude-1000/-home-g-dev-Gunther-Schulz-statiker/f59bcaca-7615-4029-95ca-3a049796cc24/scratchpad/sonnet-lap-0287/`
— that directory only (the scratch root is shared with other lanes;
never write outside your slugged directory), never this repo.

## Grounding basis — read before building; the report cites what was actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST
- `ITEMS.md`, items `st-28` and `st-30` — for st-30 the LATEST
  `amended-requirement` and `amended-done-criterion` lines are
  normative; for st-28 its `done-criterion` line
- `dev-notes/OBSERVATIONS.md`, section headed
  `## 2026-09-11 — 0.2.86 re-review dispositions` (anchor on the
  heading text): Finding 1…6 and the `pinned` gap — the reviewer's
  executed findings behind st-30
- `dev-notes/OBSERVATIONS.md`, section headed
  `## 2026-09-10 — 0.2.84 checkpoint-review dispositions`, bullets
  **B1** and **B2+B6** — the citation shapes st-28's red-first arm
  reproduces
- `plugin/skills/statiker/scripts/statiker_record.py` — the tool
- `plugin/skills/statiker/SKILL.md` — the page (skill-craft gate, see
  Write boundaries)
- `tools/test_statiker_record.py`, `tools/test_contract.py` — the
  batteries; match their idiom (RecordFixture, `violation_codes`,
  `self.sweep`, `lineno_of`) and their import of the tool module
- Critique pass (mandatory, before your first build call): ONE
  SendMessage naming which Background line below you find unopened or
  wrong, and which two lines of this brief contradict each other;
  then continue without waiting for a reply.

## Background (per-line provenance)

Opened by the dispatcher at 136a7c2 (tree clean, nothing unpushed):
- Suite: `522 passed` in 30.99s (desk run,
  `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tools/ -q -p no:cacheprovider`).
- `git diff --stat 378aa68 HEAD -- plugin tools` is EMPTY: the tool,
  page and tests are exactly what the 0.2.86 re-review read, so its
  executed pairs describe HEAD.
- `plugin/.claude-plugin/plugin.json:3` `"version": "0.2.86",`; origin
  carries the same (pushed release).
- `RULE_MINT_VERSION = {` at statiker_record.py:274, 29 codes;
  `FORM_CODES_MINT_GATED` right after it.
- `def cmd_lint` :1627, `def cmd_sweep` :1799; verbs from the argparse
  block (~:2858-2877): lint, sweep, waves, trend, sustain (one loop),
  closure, filter, pinned, verify-gate, tripwire, quote.
- "fresh id" occurs at three sites in plugin/ and tools/ (desk grep
  `grep -rn -i 'fresh id' plugin tools`): statiker_record.py:564
  inside `REPAIR_CORRECTS_OUT_OF_BODY` (a DIFFERENT code, whose
  fresh-id prescription is correct — not st-30's), :1285 (the
  apply_supersession docstring: "The repair is a fresh id") and :1366
  (the violation text: "latest-line-wins; repair with a fresh id").
- SKILL.md:114-117: "One override on every route: a halt verdict
  carrying a `shas` or `sha` field has LANDED commits — routed like
  HALT_RESIDUE_PERSISTS, never as uncommitted."
- SKILL.md:1146-1147: "P24 clause (b)'s re-derivation-seam rule
  (Implementation, below)"; clause (b)'s own passage is at :1283,
  inside `## The attack (forcing point 3)` (:940); `## Implementation
  (forcing point 4)` opens at :1291.
- SKILL.md:1303 is 88 columns ("only by verify leg 1, no earlier
  gate). The closure read runs through the record tool at").
- skill-lint: `/home/g/.claude/plugins/cache/skill-craft-marketplace/skill-craft/2.2.4/tools/skill_lint.py`.
- `tools/golden-corpus/tracker.md` and
  `tools/golden-corpus/expected-violations.json` are not ignored
  (`git check-ignore --no-index` exit 1).
- 2baa349 (st-25, inside the 0.2.84 batch) and c19c829 (0.2.82
  re-review repairs) are both ancestors of HEAD, c19c829 first; the
  B2+B6 repair a20a4ac lands after 2baa349.

From the reviewer's report (OBSERVATIONS 0.2.86 re-review section),
unverified at line grain — locate by grep before editing:
- filter's GIT_ERROR halt carries a `sha` field; PIN_UNREADABLE and
  verify-gate's GIT_ERROR carry the same shape.
- The `--threshold < 1` refusal (st-14 item 5) does not cover a Budget
  header `tripwire 0`, which still gives TRIPWIRE_FIRES.
- `pinned` echoes an abbreviated sha raw in PINNED_APPEND_ONLY.
- T2's coverage docstring (`class TestRNfRepairFormCoverage`,
  tools/test_contract.py) and two sibling docstrings on the same
  derivation over-claim: a literal code in a TUPLE return is
  invisible (planted tuple passes, planted list fails).
- `TestRNcRecordNameTokenPunctuationStrip`'s docstring describes
  ambiguous-citation as live.

## The settled design — implement exactly this, do not redesign

Order: the bump, then st-28 (one commit), then st-30 items 1–8 (one
commit each, in number order). Each item's OUTCOME sentence is the
design; sites named are where the dispatcher found it, not a bound —
where the outcome holds at a site not named, that site is in scope
and your report names it.

### st-28 — golden-corpus sweep test

Outcome: any change in the set of violations `sweep` reports over one
fixed rich tracker — a code's hits shrinking OR growing — turns the
suite red, and a code minted into RULE_MINT_VERSION with no corpus row
turns it red too.

- Files (new; `git add -N <file>` each before its pathspec commit):
  `tools/golden-corpus/tracker.md` — a synthetic tracker (header in the
  battery's RecordFixture form; no real run content);
  `tools/golden-corpus/expected-violations.json` — the golden.
- Test: `class TestGoldenCorpusSweep` in tools/test_statiker_record.py,
  invoking `sweep` the way the battery already does.
- Golden format: a JSON list of objects `{"line": <int>, "code":
  <str>, "text": <that fixture line, stripped>}`, sorted by (line,
  code) — the hit SET only; repair texts and other verdict fields are
  not in it.
- Comparison: parsed sets, never rendered text. On mismatch the
  failure message lists REMOVED hits (in golden, not produced) and
  ADDED hits (produced, not in golden), one per line.
- Coverage: the code list comes from the RUNNING module's
  `RULE_MINT_VERSION` (imported, never a copied list). Assert
  `set(RULE_MINT_VERSION) == codes_in_golden | set(EXEMPT)` and
  `codes_in_golden & set(EXEMPT) == set()`. `EXEMPT` is a dict in the
  test, code → reason, admissible ONLY for a code `sweep` cannot emit
  over a single tracker file; each reason names the verb or external
  state that emits it. Every exempt code is listed in your report.
- Rows: at least one positive row per non-exempt code; beside it, a
  known-clean row one edit away that must NOT raise that code, where
  such a variant exists (codes without one are named in the report).
  The fixture MUST include the 0.2.84 B1/B2 incident rows: an
  `[INVALIDATED]` F20 entry and citing entries whose basis cites it as
  `(F20)`, `F20)`, `F20.`, `tools/x.py:40 F20`, and `the probe: F20`
  (quoted from the B1 and B2+B6 bullets named above).
- Regeneration: `STATIKER_GOLDEN_REGEN=1` makes the test WRITE the
  golden and then FAIL in that same run with the message "golden
  regenerated — review `git diff
  tools/golden-corpus/expected-violations.json` before committing". It
  is never green on a regeneration run.
- Red-first, three arms, baseline first (state the green run at your
  commit before any mutation):
  1. INCIDENT (shrink): extract the tool at 2baa349 and at c19c829
     (`git show <sha>:plugin/skills/statiker/scripts/statiker_record.py
     > <scratch>/tool-<sha>.py`), run each one's `sweep` CLI over the
     fixture, diff against the golden with the test's own comparison.
     Expected: at 2baa349 the REMOVED set contains the
     `basis-cites-invalidated` hits on the incident rows; at c19c829
     those rows are present. Diffs from codes minted after either
     commit are expected — list them, and state which file was old.
     If the incident rows do NOT vanish at 2baa349, that is a gap:
     halt st-28 and report.
  2. GROWTH: mutate the HEAD tool in the working tree so one code
     over-fires on a clean row (your choice, named); run — red with
     that ADDED hit; restore with `git checkout --
     plugin/skills/statiker/scripts/statiker_record.py`; `git diff`
     shows no mutant hunk before committing.
  3. REACH: add `"golden-probe-code": "0.0.0",` to RULE_MINT_VERSION
     in the working tree; run — red on coverage; restore the same way.

### st-30 — the eight items

1. Outcome: every text in plugin/ and tools/ that prescribes the
   `declarator-bookkeeping` repair names the same-id, same-unit
   supersede-whole form (restate the unit's full write-set under the
   same id and unit with `(corrects line <n>)`). Sites at HEAD: the
   :1285 docstring and the :1366 violation text;
   REPAIR_DECLARATOR_BOOKKEEPING and the SKILL.md clause already
   carry it (0.2.86 N3). :564 is untouched. Red arm: a test on a
   declarator-bookkeeping hold asserting its violation text does not
   prescribe a fresh id (red today) and that the supersede-whole
   repair the text prescribes sweeps clean (control, green both ways).
2. Outcome: the re-lock pointer points where clause (b) is. SKILL.md
   :1147 "(Implementation, below)" becomes "(below)". Prose; no arm.
3. Outcome: a tripwire threshold below 1 is refused on BOTH carriers.
   A Budget-header `tripwire <n>` with n < 1 is refused with the same
   verdict the `--threshold < 1` refusal already uses (read that site,
   mirror it). Red arm: header `tripwire 0` → TRIPWIRE_FIRES today,
   the refusal after; control `tripwire 1` unchanged both ways.
4. Outcome: no halt verdict carries a `sha` or `shas` field unless the
   value names LANDED commits (the page's override, SKILL.md:114-117,
   routes any such field as landed). Enumerate every `finish(` call
   emitting a halt verdict with `sha`/`shas` across all verbs; drop the
   field wherever the value is an input argument or unresolved ref
   rather than a landed commit; keep it where it names landed commits.
   The reviewer named filter's GIT_ERROR, PIN_UNREADABLE and
   verify-gate's GIT_ERROR. Red arm: `filter --sha 'HEAD^{tree}'` →
   a `sha` field on GIT_ERROR today, none after; one test per dropped
   site that a CLI invocation can reach. Your report lists every
   enumerated site with its keep/drop classification. If a test or
   page passage READS `sha` from an error halt as an input, halt item
   4 and report.
5. Outcome: every coverage docstring on the emission-site derivation
   states its actual reach — literal code strings at emission sites;
   a code emitted from a variable or inside a tuple return is outside
   it. Sites: `TestRNfRepairFormCoverage` and its two siblings on the
   same derivation in tools/test_contract.py (locate by the shared
   helper). Prose; suite green.
6. Outcome: no test docstring describes `ambiguous-citation` as live
   (withdrawn at 0.2.86 B1). Site: `TestRNcRecordNameTokenPunctuationStrip`;
   grep tools/ for any other. Prose; suite green.
7. Outcome: `pinned` resolves its sha argument once, via `git
   rev-parse --verify <sha>^{commit}` — the form `filter` already uses
   (st-14 item 1; mirror it) — and emits the resolved full sha; an
   unresolvable argument takes filter's error route (with no `sha`
   field, per item 4). Red arm: an abbreviated sha → echoed raw in
   PINNED_APPEND_ONLY today, the full 40-hex after; control: a full
   sha unchanged.
8. Outcome: skill-lint reports 0 wrap flags on SKILL.md. Rewrap
   :1303's paragraph to its neighbours' width, words unchanged.

Red-first for items 1, 3, 4, 7: write the pair (red case AND control),
run it against the UNMODIFIED code — the red case must FAIL, output
kept — apply the fix, re-run — PASS. Both outputs in the report, per
item. A red arm that does not go red is a gap: HALT THE ITEM, report,
continue with the rest.

## Verifier (in order; real output pasted in the report)

1. Per-item red-first pairs as above.
2. `python3 -m pytest tools/ -q` — full suite after each commit; the
   final run in the report with FULL counts. Any new skip is a finding.
3. `python3 /home/g/.claude/plugins/cache/skill-craft-marketplace/skill-craft/2.2.4/tools/skill_lint.py plugin/skills/statiker/SKILL.md`
   — exit code and flags pasted; 0 wrap flags required.
4. `awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'`
   — operational line count, printed for the record (no gate).

## Write boundaries

Owned paths (nothing else; one writer per path):
- `plugin/.claude-plugin/plugin.json` (bump commit ONLY)
- `plugin/skills/statiker/scripts/statiker_record.py`
- `plugin/skills/statiker/SKILL.md`
- `tools/test_statiker_record.py`
- `tools/test_contract.py`
- `tools/golden-corpus/tracker.md`, `tools/golden-corpus/expected-violations.json` (new)
Do NOT touch: dev-notes/, LEDGER.md, ITEMS.md, ITEMS-DONE.md,
BACKLOG.md, docs/, PLAN.md, CLAUDE.md — booking is the dispatcher's.
Gate on SKILL.md: invoke the Skill tool `skill-craft:skill-craft`
BEFORE your first SKILL.md edit (repo CLAUDE.md, single-home bullet).
SKILL.md edits state current decisions cleanly, as if final — no
hedges, no history inline. Code comments may cite `st-28` / `st-30(<n>)`.
Not deployment-coupled: no written path is live on write (the
installed plugin copy is separate; the pin moves only at a desk
release, later, not in this lane).
Commits by pathspec — `git commit -m "…" -- <paths>`, flags before
`--`, never `git add` + `git commit`, never `-A`. Never amend — always
a new commit.

## Commit plan

Commit-blocking guards, each with the read that found it:
- Global pre-commit (`core.hooksPath` →
  `~/dev/Gunther-Schulz/dotfiles/git/hooks`; its pre-commit :140-177
  read at this desk): fires on a staged change under `plugin/` whose
  manifest version equals HEAD's, UNLESS HEAD's version already
  differs from origin's. HEAD and origin both carry 0.2.86, so the
  FIRST commit is the bump: `plugin/.claude-plugin/plugin.json`
  `0.2.86` → `0.2.87`, that file alone. Every later payload commit
  then passes while the batch stays UNPUSHED — push NOTHING; the
  dispatcher pushes at integration.
- Global pre-push exists (fixture-leak scan over guarded repos); you
  never push.
- No repo-local hook.
Then: `st-28: …`, then `st-30(1): …` … `st-30(8): …` (`<id>: <short
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

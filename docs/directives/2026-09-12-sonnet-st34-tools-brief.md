# sonnet-st34-tools — 0.2.87 checkpoint-review residue (st-34)

Title: sonnet: st-34 — the 0.2.87 review's tool/fixture residue (N1, N2, n1–n4)
Working copy: `/home/g/dev/Gunther-Schulz/statiker`.
Base check: base commit `6137ea3` (read at brief time:
`git -C /home/g/dev/Gunther-Schulz/statiker rev-parse --short HEAD` →
`6137ea3`). Run BOTH reads before your first edit:
`git merge-base --is-ancestor 6137ea3 HEAD` and
`git log --oneline 6137ea3..HEAD`. Base contained and nothing on top →
clean start. Base NOT contained → halt and report. Base contained WITH
commits on top → report those commits as a gap and halt, UNLESS
`git diff --quiet 6137ea3 HEAD -- <your write set>` is clean, in which
case report the changed-file list and continue. Third read, whatever
the base check said: `git status --porcelain` over your write set — any
modified file there is a HALT.
Scratch: your OWN scratchpad. Name every scratch file with the slug
`st34` (co-writers share the scratch root).

## Grounding basis — read before building; the report cites what was
## actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST.
- `dev-notes/OBSERVATIONS.md`, the section
  `## 2026-09-11 — 0.2.87 checkpoint-review dispositions` (line 8613 at
  base `6137ea3`, content anchor: the heading ends
  "verdict: PIN MOVES — 0 blocking, 3 notable, 4 nits"). The review
  recorded SEVEN findings; SIX of them are yours — N1, N2, n1, n2, n3,
  n4. N3 is NOT yours (booked st-35, a desk ruling).
  (Corrected 2026-09-12 after the lane's critique pass: this line and
  the design section's opener both read "seven" against a six-item
  body. Six is right.)
- `ITEMS.md`, entry `## st-34` (line 144 at base; content anchor:
  `grade: READY` followed by `requirement: 0.2.87 checkpoint-review
  residue`). Its `done-criterion` is the acceptance list — read it in
  full; this brief does not restate it, it fills in the design.
- `tools/test_statiker_record.py`, class `TestGoldenCorpusSweep`
  (line 5527 at base; content anchor: the docstring opens "st-28: a
  regression battery over `sweep`'s full hit SET"). Its "Red-first
  proof" block is the form your own red-first arms are recorded in.
- `plugin/skills/statiker/scripts/statiker_record.py` — the four sites
  named in the settled design below.

## Background (established; verify at the cited lines)

Every line here was opened by the dispatcher at brief time, command and
hit inline.

1. `TRIPWIRE_BUDGET_RE = re.compile(r"\btripwire\s+(\d+)\b")` —
   `statiker_record.py:156` (`grep -n TRIPWIRE_BUDGET_RE` → 156, 2465).
   Digits only, so `tripwire -1` does not match and the code reaches
   the unarmed branch at `:2465-2469`
   (`finish("TRIPWIRE_SILENT", 0, reason="unarmed", …)`).
2. The regeneration gate is `if os.environ.get("STATIKER_GOLDEN_REGEN"):`
   — `tools/test_statiker_record.py:5640` (`grep -rn STATIKER_GOLDEN_REGEN
   tools/` → one hit). Truthy, so `=0` regenerates.
3. The cross-pair disjointness assertion is at
   `tools/test_statiker_record.py:5681` (`grep -rn disjoint tools/`;
   content anchor at that line: the comment "disjointness: no code's
   positive row is duplicated across two"). Its rationale sentence is
   in the `TestGoldenCorpusSweep` docstring: "EXEMPT is now {} — every
   RULE_MINT_VERSION code has a golden row in one pair or the other,
   kept disjoint (asserted below)."
4. `class TestRNfRepairFormCoverage` — `tools/test_contract.py:1235`;
   `class TestP5RuleMintVersionCoverage` — `tools/test_contract.py:1309`
   (`grep -n` over `tools/*.py`). The blind shapes the reviewer names —
   a conditional return (live at `statiker_record.py:785`) and
   `dict(code=)` — are stated accurately in the shared helper's own
   docstring; find that helper by reading the two classes.
5. Double ref resolution, both sites, identical shape:
   `cmd_filter` — `git show f"{args.sha}:{rel}"` at
   `statiker_record.py:2566`, then
   `git rev-parse --verify f"{args.sha}^{{commit}}"` at `:2581`;
   `cmd_pinned` — the same pair at `:2726` and `:2741`. Routing today,
   read at those lines: `git show` fails → `PIN_UNREADABLE` (exit 2,
   no `sha` field); `git show` succeeds but rev-parse fails →
   `GIT_ERROR` (exit 2, no `sha` field).
6. Golden tracker rows, `tools/golden-corpus/tracker.md:89-96`, block
   `## Block: basis-cites-invalidated (B1/B2 incident rows)`:
   `- F20 [INVALIDATED] … — basis: F1`,
   `- F21 [VERIFIED] … — basis: (F20)` … `- F26 [VERIFIED] cites a
   live id, no violation — basis: F1`. `grep -n "^- F1 " tracker.md`
   → exit 1: there is NO entry `F1` in that tracker, so F26's basis
   names a phantom and the row is not the live-id control its own text
   claims to be.
7. `grep -rn "Status: \[" tools/golden-corpus/*.md` → no hits: neither
   golden tracker carries a `Status: [READY]` line.
8. Payload guard: `git config core.hooksPath` →
   `~/dev/Gunther-Schulz/dotfiles/git/hooks`; that `pre-commit` blocks a
   payload commit whose plugin version is unchanged **relative to the
   ORIGIN manifest** (`origin_manifest_text`, hook lines 123-173: the
   finding is empty when `v_neu != v_origin`). At base `6137ea3`
   `plugin/.claude-plugin/plugin.json` reads `"version": "0.2.88"` and
   `git log --oneline @{u}..` is empty, so HEAD and origin agree and
   the exemption is NOT armed. See Commit plan.

## The settled design — implement exactly this, do not redesign

Six items. Each lands as its own commit with its own red-first
arrangement, except where noted; state each red's arrangement (which
side was old, where the expectation came from) in the report.

**N1 — the golden corpus's clean controls.** Outcome: the golden corpus
exercises the OVER-FIRE branch of the basis-citation check and of
lint's Status/Phase tag-literal exemption, so a mutant that drops
either turns `TestGoldenCorpusSweep` red.
- (a) `tools/golden-corpus/tracker.md` F26's basis names an id that
  EXISTS in that tracker and is LIVE (not `[INVALIDATED]`). You choose
  the id; the report states which and why it is live, with the grep
  that shows the row.
- (b) One golden tracker gains a `Status: [READY]` control row, placed
  so lint's tag-literal exemption is what keeps it clean.
- (c) Regenerate the expected-violations goldens and review the diff;
  the report pastes the diff.
- (d) Two mutant proofs, each run and its real output pasted: drop the
  `[INVALIDATED]` test in the basis check → `TestGoldenCorpusSweep`
  RED; restore. Drop lint's Status/Phase tag-literal exemption →
  `TestGoldenCorpusSweep` RED; restore. A mutant that leaves the sweep
  green means (a) or (b) did not land — report it as a gap, do not tune
  the fixture until it goes red without saying so.
- (e) BASELINE, stated first: the unmutated suite's result before each
  mutant, so the red is a delta and not a check that is always red.

**N2 — `tripwire` refuses a non-integer field.** Outcome: a `tripwire`
field PRESENT in the Budget header that does not parse as an integer
≥ 1 is REFUSED the way `--threshold` refuses one, instead of reading as
unarmed. An ABSENT field stays `TRIPWIRE_SILENT reason="unarmed"` —
that is the only unarmed case left.
- Read `--threshold`'s own refusal (the same module) and reuse its
  verdict/exit shape; do not invent a second one. Name in the report
  what you reused.
- Red-first: `tripwire -1` gives `TRIPWIRE_SILENT` / `unarmed` today
  (paste it), the refusal after. Control, unchanged in both:
  `tripwire 2` arms.

**n1 — remove the cross-pair disjointness assertion**
(`tools/test_statiker_record.py:5681`). It fires on a code legitimately
present in both trackers; a code MOVING between trackers still shows as
REMOVED/ADDED in the hit-set test. Amend the `TestGoldenCorpusSweep`
docstring sentence that claims the pairs are "kept disjoint (asserted
below)" in the SAME commit — a docstring left asserting a removed
assertion is the label-over-body defect this repo books as a finding.
Prove the remainder still catches a move: plant a code's row in the
other tracker, show REMOVED/ADDED, revert.

**n2 — `STATIKER_GOLDEN_REGEN == "1"`** exactly
(`tools/test_statiker_record.py:5640`). Red-first: `=0` regenerates
today (paste the evidence), does not after; control: `=1` still
regenerates.

**n3 — the two class docstrings**
(`tools/test_contract.py:1235`, `:1309`) either state the blind shapes
the shared helper's docstring names (the conditional return at
`statiker_record.py:785`; `dict(code=)`), or defer to that helper BY
NAME. Docstring-only change; no behavior.

**n4 — resolve the ref ONCE, both sites** (`cmd_filter`, `cmd_pinned`).
The settled shape, which preserves today's routing exactly:
1. `git rev-parse --verify "<args.sha>^{commit}"` FIRST.
2. rev-parse SUCCEEDS → read the content at the resolved sha:
   `git show "<resolved_sha>:<rel>"`. That read failing →
   `PIN_UNREADABLE` (exit 2, no `sha` field, stderr from this read) —
   today's route for a path absent at that commit.
3. rev-parse FAILS → run `git show "<args.sha>:<rel>"` to separate the
   two routes: that show ALSO failing → `PIN_UNREADABLE` (stderr from
   the show, as today); that show SUCCEEDING (a tree-ish that is not a
   commit) → `GIT_ERROR` with today's message.
Emitted `sha` stays the resolved full form. Content and sha then come
from ONE resolution, which is the defect. The existing comments at both
sites name st-30(7)/st-14(1) — rewrite them to describe the new order;
do not leave a comment describing the old one.
Red-first: the reviewer's PATH-wrapper race — a `git` wrapper early on
PATH that lands a new commit on the branch between the two resolutions,
with `--sha` given as a symbolic ref. Today: emitted `sha` names a
different commit than the content read (paste it). After: they agree.
Controls, unchanged both sides: an unresolvable `--sha` still routes
`PIN_UNREADABLE`; a tree-ish that is not a commit still routes
`GIT_ERROR`. Both sites get the arm; a fix proven at one site only is a
gap.

**Not yours.** N3 (the tripwire ARMING question — in-place Budget-line
edit vs `pinned`'s mutable set) is booked st-35 and is a desk ruling.
If your N2 work makes an arming route look wrong, REPORT it; do not
touch `_mutable_field_positions`, and do not touch
`plugin/skills/statiker/SKILL.md` at all.

## Verifier (in order; real output pasted in the report)

1. Each item's red-first arm above, with its baseline stated first.
2. `python3 -m pytest tools/ -q` — the WHOLE suite (the repo's Verify
   block: the lane batteries prove their own lanes, `test_contract.py`
   is the reach detector over them). Baseline at `6137ea3`, from the
   0.2.88 release record: 539 passed. FULL counts including skips;
   every skip dispositioned.
3. `awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'`
   — the operational-line count, printed for the record. Expected
   UNCHANGED from base (you touch no page text); a change is a finding.

## Write boundaries

Paths you own:
- `plugin/skills/statiker/scripts/statiker_record.py`
- `plugin/.claude-plugin/plugin.json` (the bump commit only — see
  Commit plan)
- `tools/test_statiker_record.py`
- `tools/test_contract.py`
- `tools/golden-corpus/tracker.md`
- `tools/golden-corpus/tracker-admission.md`
- `tools/golden-corpus/expected-violations.json`
- `tools/golden-corpus/expected-violations-admission.json`

Touch nothing else — in particular NOT `plugin/skills/statiker/SKILL.md`,
`ITEMS.md`, `LEDGER.md`, `dev-notes/OBSERVATIONS.md`, `docs/`.

This is a SHARED working copy: a peer session may be writing
`docs/directives/` concurrently. Commit by pathspec only —
`git commit -m "…" -- <paths>`, every flag BEFORE the `--`, `-F` for a
multi-line message. Never `git add` then `git commit`, never `-A`. A new
file needs `git add -N <path>` first (a FILE, never a directory).
Never amend — always a new commit.
Commits UNPUSHED; the dispatcher pushes after verifying.
Deployment coupling: `plugin/skills/statiker/scripts/statiker_record.py`
is PAYLOAD, served to running desks only through an installed pin —
writing it does not go live, so no live-on-write hazard here. Nothing in
your write set is on a PATH-resolved execution path.

## Commit plan

Commit-blocking guards, with the read that found them: the global
`pre-commit` at `core.hooksPath=~/dev/Gunther-Schulz/dotfiles/git/hooks`
(read at brief time) blocks a PAYLOAD commit whose plugin version equals
the ORIGIN manifest's. `plugin/skills/statiker/scripts/statiker_record.py`
is payload. HEAD and origin both read `0.2.88` and nothing is unpushed,
so the exemption is NOT armed today. No repo-local `.git/hooks/` hooks
exist (`ls .git/hooks/` → only samples).

Therefore YOUR FIRST COMMIT bumps
`plugin/.claude-plugin/plugin.json` `"version"` from `0.2.88` to
`0.2.89` — manifest field only, nothing else in that commit. Every later
commit of yours is then exempt while the batch stays unpushed. The
dispatcher pushes at integration, not before; if a commit of yours
bounces on the version guard anyway, that means the batch was pushed —
HALT and report it, never `--no-verify`.

Pre-authorized repair class: if the commit plan collides with a repo
guard, reorder to satisfy the guard and report the permutation as a
deviation. Novel deviations halt.

Commit title pattern: `st-34: <item> — <what>` (e.g.
`st-34: n4 — filter and pinned resolve the ref once`).
Trailer, verbatim:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`

## Critique pass (one message, before your first build call)

Which Background line above do you find unopened or wrong, and which two
lines of this brief contradict each other? Send it on the report
channel, then continue without waiting for a reply.

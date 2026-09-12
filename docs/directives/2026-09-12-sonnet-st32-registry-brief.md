# sonnet-st32-registry — st-32 lap B: the route registry, stamping, and the replacement contract

Title: sonnet: st-32 lap B — ROUTES registry, route stamping, TestRouteParity
Working copy: `/home/g/dev/Gunther-Schulz/statiker`.
Base check: base commit `3c041e5`, **or any later HEAD whose extra
commits leave your write set untouched** — the desk commits records
(LEDGER, ITEMS, OBSERVATIONS, docs/) while you build, and an opus lane
(`opus-st32-clause-table`) is writing one file under `docs/audits/`.
Run BOTH reads: `git merge-base --is-ancestor 3c041e5 HEAD` and
`git log --oneline 3c041e5..HEAD`; base not contained → halt. Commits
on top → `git diff --quiet 3c041e5 HEAD -- <your write set>`; clean →
report the changed-file list and continue, dirty → halt. Third read
whatever those say: `git status --porcelain` over your write set — a
modified file there is a HALT.
Scratch: your OWN scratchpad. Slug every scratch file `st32reg`.

## Grounding basis — read before building; the report cites what was
## actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST.
- `docs/directives/2026-09-12-st32-lapB-design-statiker-a5.md` — **the
  settled design; implement it, do not re-derive it.** §1 the eight
  tokens with their meanings; §2 registry placement; §3 the complete
  76-verdict mapping grouped by route — this is your registry's
  content, copied from there, never re-derived by reading the scripts;
  §4 the seven page-routing findings; §5 the replacement contract's
  six tests and the R1–R6 red-first arrangement.
- `tools/test_contract.py` — `TestVerdictParity` (content anchor:
  `test_every_emitted_verdict_is_routed_in_skill`), and the four
  instrument tests in the same class that SURVIVE unchanged.
- `plugin/skills/statiker/scripts/statiker_emit.py` — the module both
  scripts already import; the registry's single home.

## Background (established; verify at the cited lines)

1. `emitted_verdicts()` returns **76** names (executed by the
   dispatcher at brief time: `python3 -c "import sys;
   sys.path.insert(0,'tools'); import test_contract as tc;
   print(len(tc.emitted_verdicts()))"` → `76`). The design's §3 maps
   all 76. If your count differs from 76, that is a FINDING — report
   it, do not silently map a different set.
2. Both scripts already import the registry's home module:
   `statiker_record.py:137`, `statiker_git.py:95` (`grep -n
   statiker_emit`).
3. `test_contract.py` unions its `SCRIPTS` list at `:181`, so the
   parity test spans BOTH tools — which is why this lane's write set
   includes the git tool. The git edit admitted here is the
   **mechanical stamping line only**; no gate-logic change rides in.
4. `TestVerdictParity` sits at `tools/test_contract.py:1092` at base
   (the st-32 item text cites `:1042-1051`, stale since lap A's
   rewrap — the content anchor above is authoritative).
5. Payload guard: the manifest is at `0.2.89` and the batch is
   UNPUSHED, so the version exemption is armed and you bump nothing.
   A bounce means the batch was pushed — HALT and report, never
   `--no-verify`.
6. `SKILL.md` writes trip a hook gate demanding a same-turn
   `skill-craft` skill invocation. Invoke it before your page edit.

## The settled design — implement exactly this, do not redesign

**(1) The registry, one commit.** `ROUTES: {verdict_name: token}` and
`ROUTE_VOCABULARY: frozenset` in `statiker_emit.py`, filled from design
§3 verbatim. In the SAME commit: each script's `finish()` stamps
`route` into the verdict JSON via one lookup line, and a name the
registry lacks stamps `route: "unrouted"` (design §1, the unroutable
verdict — emission never fails on a registry gap). Also in the same
commit: delete `test_every_emitted_verdict_is_routed_in_skill` and land
`TestRouteParity` (design §5's six tests). The design requires the
deletion and the replacement in ONE commit; do not split them.

**(2) Keep what survives.** `test_every_skill_named_verdict_is_emitted`
stays (design §5 item 5 — page-named ⊆ emitted still catches page rot),
and `TestVerdictParity`'s four instrument tests stay unchanged.

**(3) The page, second commit — ADDITIVE ONLY.** Add the route
vocabulary section to `SKILL.md`: the eight token paragraphs from
design §1 and the unrouted-verdict principle, each token appearing as a
backtick-quoted literal so §5's test 4 can anchor on it. **Remove
nothing from the page** — the removals are stage 2's, driven by a
per-clause table another lane is producing now. Invoke `skill-craft`
before this edit (Background 6).

**(4) NOT yours.** r4-M4 (the `budget_raises` field) rides stage 2, not
this lane — it is a different mechanism with its own red-first arms,
and bundling it here would entangle the verdicts. Do not touch
`_mutable_field_positions`, the tripwire arming code, or the golden
corpus.

## Verifier (in order; real output pasted in the report)

Baseline FIRST in every arm — the unmutated result stated before the
red. Suite baseline at your base: **558 passed, 2 subtests, 0 failed,
0 skipped**.

Run design §5's R1–R6 exactly as written there:
R1 TestRouteParity added, tools untouched → tests 1/3/6 red (no
ROUTES) — proves non-vacuity against the old tool. R2 registry minus
one emitted verdict → test 1 red NAMING it; restore. R3 a phantom key
→ test 2 red; restore. R4 one value off-vocabulary → test 3 red;
restore. R5 one token's backtick literal removed from the page → test
4 red; restore. R6 the stamping line removed from one `finish()` with
the registry whole → 1–3 green, 6 red — proves 6 non-redundant.

Then: `python3 -m pytest tools/ -q` — FULL counts including skips,
every skip dispositioned. And
`awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'`
with the base count (1638) beside it; this lane ADDS lines, so a
decrease is a finding.

## Write boundaries

Paths you own:
- `plugin/skills/statiker/scripts/statiker_emit.py`
- `plugin/skills/statiker/scripts/statiker_record.py`
- `plugin/skills/statiker/scripts/statiker_git.py`
- `plugin/skills/statiker/SKILL.md` (the added vocabulary section only)
- `tools/test_contract.py`
- `tools/test_statiker_record.py`
- `tools/test_statiker_git.py`

Touch nothing else — NOT `docs/`, `ITEMS.md`, `LEDGER.md`,
`dev-notes/OBSERVATIONS.md`, NOT the golden corpus.

Shared copy: an opus lane writes one file under `docs/audits/` and
reads `SKILL.md` from a pinned sha, so it cannot collide with you.
Commit by pathspec only — `git commit -m "…" -- <paths>`, flags before
the `--`, `-F` for multi-line. Never `git add` then `git commit`, never
`-A`, never `--amend`. Commits UNPUSHED.

Commit plan: guards named in Background 5 and 6. Pre-authorized repair
class: reorder to satisfy a guard and report the permutation as a
deviation; novel deviations halt.
Commit titles: `st-32 lap B: <what>`.
Trailer: `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`

## Critique pass (one message, BEFORE your first build call)

Which Background line is wrong or unopened, and which two lines of this
brief contradict each other? Send it, then continue without waiting.
This fires before the first EDIT — both previous lanes in this batch
sent it late, and both said afterwards that it should have been one
hard-ordered step.

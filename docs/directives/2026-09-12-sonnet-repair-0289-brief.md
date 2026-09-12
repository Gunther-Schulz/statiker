# sonnet-repair-0289 — the 0.2.89 review's repair lap

Title: sonnet: 0.2.89 repair lap — the fail-closed floor, the arming near-miss, and the stale pointers
Working copy: `/home/g/dev/Gunther-Schulz/statiker`. Use ABSOLUTE paths
and `git -C /home/g/dev/Gunther-Schulz/statiker …` for every git call:
this session's harness re-points the working directory mid-run, and a
bare `git` then answers from whichever repo the cwd has become.
Base check: base commit `15d0c47`, **or any later HEAD whose extra
commits leave your write set untouched** (the desk commits records while
you build). Run `git -C <repo> merge-base --is-ancestor 15d0c47 HEAD`
and `git -C <repo> log --oneline 15d0c47..HEAD`; base not contained →
halt. Commits on top → `git -C <repo> diff --quiet 15d0c47 HEAD --
<your write set>`; clean → report and continue, dirty → halt. Third
read regardless: `git -C <repo> status --porcelain` over your write
set — a modified file there is a HALT.
Scratch: your OWN scratchpad, every file slugged `rep0289`.

## FIRST MESSAGE — send this BEFORE reading anything but this brief

Which Background line is unopened or wrong, and which two lines of this
brief contradict each other? Send it on the report channel, then
continue without waiting for a reply. Sent after your first edit it is
a report about work already done, which is the failure it exists to
prevent — three lanes in this batch sent it late and all three said
afterwards it should have come first.

## Grounding basis — read before building; the report cites what was
## actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST.
- `dev-notes/OBSERVATIONS.md`, section `## 2026-09-12 — 0.2.89
  checkpoint-review dispositions`. **This is the design.** It carries
  the ruling (the fail-closed floor), every finding's disposition, and
  what was verified sound and must not be re-opened.
- `plugin/skills/statiker/scripts/statiker_emit.py` — `ROUTES`,
  `ROUTE_VOCABULARY`.
- `plugin/skills/statiker/SKILL.md` — the Route vocabulary section
  (content anchor: `### Route vocabulary`), and the seam passages the
  items below name by content anchor.
- `plugin/skills/statiker/scripts/statiker_record.py` —
  `RULE_MINT_VERSION` (:291), `TRIPWIRE_ARM_RE`, `TRIPWIRE_BUDGET_RE`,
  and any existing near-miss class (e.g. `scope-near-miss`,
  `write-set-near-miss`) as the FORM your new class mirrors.

## Background (established; verify at the cited lines)

1. The page routes `sustain`'s gate to closing design, not to the
   narrowing route: "a round dispatched over SUSTAIN_DENIED is exactly
   the class this gate exists to catch", and the NARROWING route's
   named entrants are the non-contracting trend grade and an armed
   TRIPWIRE_FIRES. Opened by the dispatcher (whitespace-normalised
   search over the whole page: three SUSTAIN_DENIED occurrences, none
   near a narrowing route).
2. A near-miss arming entry silently disarms, verified by the
   dispatcher at HEAD: `- F1 [VERIFIED] record: tripwire armed at 2
   (per operator) — basis: desk` gives `TRIPWIRE_SILENT` /`"unarmed"`
   and `lint` gives `LINT_CLEAN`; with a header `tripwire 9` present
   the same entry runs at **9** and the evidence line names the header
   without mentioning the ignored entry.
3. A verdict line can carry TWO `route` fields — verified by the
   dispatcher: `unit-start` over a closed gate emits
   `{"verdict": "UNIT_GATE_BLOCKED", "route": …, "gate": {"verdict":
   "CLOSURE_ABSENT", "route": …}}`.
4. `RULE_MINT_VERSION` (statiker_record.py:291) is the closed registry
   of lint classes with their mint versions; the golden-corpus sweep
   test derives its coverage from the RUNNING module, so a new class
   needs a golden row or that test goes red. **That is the intended
   behaviour — satisfy it with a real corpus row, never by weakening
   the test.**
5. Payload guard: manifest at `0.2.89`, batch UNPUSHED, exemption
   armed — you bump nothing. A bounce means the batch was pushed: HALT
   and report, never `--no-verify`.
6. `SKILL.md` writes trip a hook gate demanding a same-turn
   `skill-craft` invocation. Invoke it before your page edits.

## The settled design — implement exactly this, do not redesign

**R1 — the registry takes the fail-closed floor.** In
`statiker_emit.py`: `SUSTAIN_DENIED` `narrow` → **`barred`**;
`BLOCKED_CONTENTION` `triage` → **`halt`**; `UNIT_GATE_BLOCKED`
`barred` → **`halt`**; `UNIT_COLLISION` `triage` → **`halt`**. Four
entries, no others. The per-route count comments in that file are
derived from the mapping — update them so they still match, and say in
the report how you re-derived them.

**R2 — the page states the floor.** One paragraph in the Route
vocabulary section: a verdict's token is the FAIL-CLOSED member of its
page dispositions — the one that books and halts wherever seams
differ; a seam may be more permissive than its token only through an
explicit sentence at that seam, so a desk reading only the token is
never unsafe. Place it where the section's reader meets it before the
token list, not after.

**R3 — `surface` gains the booking it was silently dropping.** Its
paragraph currently prescribes no record obligation while the page says
`PINNED_REWRITTEN` "halts the seam that ran it". Add to `surface`'s
paragraph that it carries `halt`'s booking obligation AND routes the
resolution to the operator. `PINNED_REWRITTEN` stays `surface`.

**R4 — the two-route rule.** One sentence in the same section: where a
verdict line carries an embedded verdict (the git tool's `gate` field),
the OUTER verdict's route governs the seam; an embedded route is
evidence about the inner call, never a second instruction.

**R5 — the arming form becomes machine-token-enumerated and
near-miss-linted.** Add `record: tripwire armed at <n>` to the page's
machine-token enumeration (content anchor: the list that grants
`SKILL:` and `unit U<k> irreversible:` their explicit no-near-miss
declarations). Add a lint class `tripwire-arm-near-miss` to
`RULE_MINT_VERSION` at `"0.2.89"`, firing on an entry whose body begins
`record: tripwire armed` (case-insensitively, after the existing body
normalisation) and which does NOT both match `TRIPWIRE_ARM_RE` and
carry class `F` with tag `VERIFIED`. Mirror an existing near-miss
class's structure; do not invent a new violation shape. Add the golden
corpus row Background 4 requires, and regenerate.

**R6 — `TRIPWIRE_BUDGET_RE` anchors on the page's field form.** The
page declares "an optional trailing `/ tripwire <n>` field"; the
pattern dropped the `/`, so the word "tripwire" anywhere in the Budget
line now hard-fails the subcommand. Anchor on the `/` form. The st-34
N2 behaviour must survive: a PRESENT `/ tripwire <x>` whose value is
not an integer ≥ 1 is still refused.

**R7 — five stale `SKILL.md:<line>` pointers.** In
`statiker_record.py` (~:1695, ~:2145, ~:2659) and
`tools/test_statiker_record.py` (~:4975, ~:5466). Repair them the way
0.2.88's f23a69b did for the page-internal class: **name the section
and quote its handle, never a line number.** Line numbers above are
approximate and will have moved — find each by its comment text. The
comment at ~:2145 also asserts "citation refresh, computed against the
current file"; either make that true or delete the assurance.

**R8 — `TestRouteParity`'s docstring.** It claims the old direction
"is replaced by a registry". `TestRuntimeVerdictBattery` still requires
page naming for the battery-driven verdicts; only the undriven names
lost it. Correct the docstring to say what was actually dropped.

## Verifier (in order; real output pasted in the report)

Baseline FIRST in every arm. Suite baseline at your base: **563
passed, 2 subtests, 0 failed, 0 skipped.**

1. **R1 red-first:** for each of the four, show the emitted `route`
   before and after on a real invocation (a throwaway repo/tracker
   under your scratch), not by reading the dict.
2. **R5 red-first, the bite:** the near-miss from Background 2 — today
   `TRIPWIRE_SILENT`/`unarmed` with `LINT_CLEAN`; after, `lint` raises
   `tripwire-arm-near-miss`. Control: the exact sanctioned form still
   arms and lints clean. Second control: the header-9 variant — after
   the fix the near-miss is visible rather than silently overridden.
3. **R6 red-first:** `Budget: cycles 7 / rounds 4 / verify 3 — tripwire
   armed later by entry` gives USAGE_ERROR today, unarmed after.
   Controls, unchanged: `/ tripwire 2` arms; `/ tripwire -1` refuses.
4. `python3 -m pytest tools/ -q` — FULL counts incl. skips, each skip
   dispositioned.
5. `awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'`
   with the base count (1689) beside it.

## Write boundaries

`plugin/skills/statiker/scripts/statiker_emit.py`,
`plugin/skills/statiker/scripts/statiker_record.py`,
`plugin/skills/statiker/SKILL.md`, `tools/test_contract.py`,
`tools/test_statiker_record.py`, `tools/golden-corpus/*`.
Touch nothing else — NOT `statiker_git.py`, NOT `docs/`, `ITEMS.md`,
`LEDGER.md`, `dev-notes/OBSERVATIONS.md`.

Commit by pathspec only, flags before the `--`, `-F` for multi-line.
Never `git add` then `git commit`, never `-A`, never `--amend`.
Commits UNPUSHED. One commit per repair item where each carries its own
red-first arm (R1+R2+R3+R4 may share one commit — they are one ruling);
R5, R6, R7, R8 separate.
Commit titles: `0.2.89 fix: <item> — <what>`.
Trailer: `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`

## Commit plan

Commit-blocking guards, with the read that found them: the global
`pre-commit` at `core.hooksPath=~/dev/Gunther-Schulz/dotfiles/git/hooks`
(read at compose time) blocks a PAYLOAD commit whose plugin version
equals the ORIGIN manifest's. `SKILL.md` and the two scripts are
payload. The manifest is ALREADY bumped to `0.2.89` and the batch is
UNPUSHED, so the exemption is ARMED for every commit of yours and **you
bump nothing** — the dispatcher pushes at integration only, which is
what keeps it armed. A bounce therefore means the batch was pushed:
HALT and report, never `--no-verify`. No repo-local `.git/hooks/` hooks
exist. `SKILL.md` additionally trips the skill-craft load gate
(Background 6) — that is a same-turn skill invocation, not a commit
guard.

Pre-authorized repair class: if the commit plan collides with a repo
guard, reorder to satisfy the guard and report the permutation as a
deviation. Novel deviations halt.

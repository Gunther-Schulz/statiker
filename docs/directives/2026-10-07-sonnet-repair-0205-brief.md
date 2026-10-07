# Brief — sonnet: eve-review repair lap, tool side (0.2.105, unreleased)

Working copy: /home/g/dev/Gunther-Schulz/statiker (shared with the
dispatching desk, which writes nothing under your paths while you
run). Base check, your first act:
`git -C /home/g/dev/Gunther-Schulz/statiker merge-base --is-ancestor <BASE> HEAD`
and `git -C /home/g/dev/Gunther-Schulz/statiker log --oneline <BASE>..HEAD`
— `<BASE>` is the sha in your dispatch prompt. Base contained and
nothing on top is the clean start; anything else is a halt, reported
as a gap. Then `git -C ... status --porcelain` over your write set
must be empty (the untracked `ITEMS-DONE.md.lock` is a tool lock,
not yours, ignore it).
Scratch: your OWN scratchpad.

SHELL PLUMBING, binding. Nobody is present to answer a permission
dialog, and a command that raises one stalls your lane for good
(two lanes were lost to exactly this today). Therefore: never the
characters `<` or `>` in a shell command (no redirection, no
heredoc — write files with the Write tool); never start a command
with `cd`; one plain command per call, no `;`, `&&`, loops or
`$(...)`; run Python as `python3 /absolute/path.py`, never a script
directly; use `git -C /home/g/dev/Gunther-Schulz/statiker ...`.
Search with the Grep/Read tools rather than shell pipelines.

## Grounding basis — read before building; the report cites what was actually read
- the executor skill (dispatch-guards:executor) — load FIRST.
- `plugin/skills/statiker/SKILL.md` — the page. It was edited at
  the desk BEFORE this lane and already describes the behaviour you
  build; it is your spec and you do not edit it. Read: The record's
  machine-token enumeration (the `CONTAINMENT:` paragraph), the
  resume passage's SKILL_VERSION_HOLD sentences, and The attack's
  "Per-unit convergence" paragraph with the executed-probe clause
  above it and Verify's demand list.
- `plugin/skills/statiker/scripts/statiker_record.py`,
  `statiker_git.py`, `statiker_emit.py`,
  `plugin/hooks/statiker_postcompact.py` — the code you change.
- `tools/test_statiker_record.py`, `tools/test_contract.py`,
  `tools/test_statiker_postcompact_hook.py`, `tools/golden-corpus/`
  — the batteries; `tools/test_contract.py` is the reach detector
  over the lane batteries.
- `CLAUDE.md`, the Birth-class bullet's last paragraph: what a
  lint-code mint's write-set structurally includes.

## Background (each line opened by the dispatcher today at base, or graded)
- `CONTAINMENT_EXACT_RE = re.compile(r"^CONTAINMENT: (\S+)$")` and
  `CONTAINMENT_NEAR_RE = re.compile(r"(?i)^\s*containment\s*:")` at
  statiker_record.py:340 and :344 (read).
- The lint raises `containment-near-miss` at :1328-1330 (read).
  `cmd_filter` runs its OWN scan at :3160-3166, over every pinned
  line (`malformed = [l for l in lines if CONTAINMENT_NEAR_RE.match(l)
  and not CONTAINMENT_EXACT_RE.match(l)]`) (read). Executed at the
  desk: a head-region line `Containment: keep every artifact under
  ~/work please.` gives LINT_CLEAN and SWEEP_CLEAN and then
  ARTIFACT_CONTAINMENT_HOLD; a mistyped body label followed by the
  lint's own `record: corrects line N` entry and a correct label
  gives SWEEP_CLEAN and still ARTIFACT_CONTAINMENT_HOLD; a declared
  path with an interior space cannot match the exact form.
- `FORM_CODES_MINT_GATED` at :481-482 holds four codes and not
  `containment-near-miss`; `is_retro` returns False for any code
  outside it (:518) (read). `RULE_MINT_VERSION` carries
  `"containment-near-miss": "0.2.105"` at :461 and
  `"tripwire-arm-near-miss": "0.2.89"` at :477; `MACHINE_TOKEN_CODES`
  starts at :765 (read).
- The three convergence regexes sit at :232-235 and
  `recognize_record_form` under them; `unit_convergence_states` at
  :2205-2224 takes the latest recognized F-line per unit and does
  not read its tag (read). The closure guard at :2336-2353 builds
  `d_units` from pre-close D-lines whose scope is `unit` and sits
  only in the [ZERO-DELTA] branch (read; the terminal-[BIT]
  satisfied branch is at about :2321, from a reviewer, unverified
  line number). Executed at the desk: scopeless design D-line plus
  `A1 [ZERO-DELTA]` → CLOSURE_LIVE; unit-scoped D1/D2, one substance
  F-line, `A1 [BIT]` → CLOSURE_LIVE; `record: unit U1 UNCONVERGED at
  A2 - F2` (hyphen) → CLOSURE_LIVE and LINT_CLEAN; `- F1 [PENDING]
  record: unit U1 CONVERGED at A99 — basis: unverified` after the
  closing A-line → CLOSURE_LIVE.
- The closure verdict's keys today: closing, entries, head_boundary,
  irreversible_units, late_intent, mode, post_closure, r_lines,
  route, skill_versions, verdict (executed).
- `skill_version_hold` (statiker_record.py, under
  `own_served_version`) takes `reach["skill_versions"][0]` as "the
  header entry" (read). Executed: a header with NO `Skill:` line and
  a body line `SKILL: statiker 0.2.110`, served 0.2.105 →
  SKILL_VERSION_HOLD. Its docstring's cache path reads
  `<version>/plugin/skills/...`; the installed layout is
  `<version>/skills/...` (from two reviewers, each citing a
  directory listing; unverified here).
- `lock_gate_check` in statiker_git.py (:977-981) computes
  `blocking = gate.get("violations") or []` (read). Executed: under
  a version hold `lock-check` → LOCK_CHECK_CLEAN and `lock-commit`
  lands a commit, while `unit-start` → UNIT_GATE_BLOCKED.
- statiker_emit.py:169 routes `"SKILL_VERSION_HOLD": "surface"`,
  :144 `"ZERO_DELTA_UNCONVERGED": "barred"` (read).
- plugin/hooks/statiker_postcompact.py: `_HEADER_LINES = 15`; `main`
  passes the payload's `cwd` straight to `live_trackers(cwd)` (read).
  Executed by a reviewer, unverified here: Status and Phase at
  header lines 16-17 → silent; cwd one directory below the repo
  root → silent.
- Suite at base: `python3 -m pytest tools/ -q -p no:cacheprovider`
  → 723 passed, 18 subtests passed, 0 skipped (run by the dispatcher
  on the base tree).

## The settled design — implement exactly this, do not redesign

A. Containment label (statiker_record.py).
 A1. The exact form admits a path with interior spaces:
     `^CONTAINMENT: (\S(?:.*\S)?)$`. A doubled space after the colon
     stays a near-miss.
 A2. `cmd_filter` stops scanning raw lines. It holds
     ARTIFACT_CONTAINMENT_HOLD on a malformed label exactly when the
     pinned record carries a LIVE, NON-RETRO `containment-near-miss`
     violation as `sweep` would grade it: body region only, a line
     shed by a correcting entry no longer counts, a RETRO-graded
     line never counts. Reuse the function(s) `cmd_sweep` uses to
     reach that set; do not write a second predicate. If that reuse
     is impossible without changing those functions' behaviour for
     `sweep`, STOP and report the gap.
     `malformed_containment` keeps listing the offending lines.
 A3. `containment-near-miss` joins `FORM_CODES_MINT_GATED`.
B. Unit convergence (statiker_record.py).
 B1. UNCONVERGED admits a finding list:
     `^record: unit (U\d+) UNCONVERGED at (A\d+) — (F\d+(?:, F\d+)*)$`.
     `recognize_record_form` returns the A-id and the list of F-ids.
 B2. A convergence record COUNTS only when the F-line carrying it is
     tagged `[VERIFIED]` and, for CONVERGED and UNCONVERGED, its
     `A<n>` is the id of an A-class entry present in the record.
     ABSENCE needs the tag only. `unit_convergence_states` reads
     only records that count.
 B3. New lint code `convergence-near-miss`, on the
     `tripwire-arm-near-miss` precedent: a body-region F-line whose
     body, before its basis clause, matches
     `(?i)^record: unit U\d+ (converged|unconverged|absence)\b` and
     is not a record that counts under B1/B2. Register it in
     `RULE_MINT_VERSION` as "0.2.105", in `MACHINE_TOKEN_CODES`, and
     in `FORM_CODES_MINT_GATED`, with one golden-corpus row and its
     contract-battery registration (CLAUDE.md names both).
 B4. The closure guard's population is the UNION of the existing
     `d_units` and every unit carrying a counting convergence record
     of any kind. A unit in it whose latest counting state is not
     `converged` or `absence` is unconverged.
 B5. The guard runs on BOTH closing paths: the [ZERO-DELTA] branch
     and the terminal-[BIT] branch the gate reads as satisfied. One
     helper, called from both.
 B6. Every closure verdict that carries `post_closure` also carries
     `absence_units`: the sorted ids whose latest counting state is
     `absence`.
C. Version hold.
 C1. statiker_git.py `lock_gate_check`: a gate verdict named
     SKILL_VERSION_HOLD raises `Halt("LOCK_GATE_HOLDS", gate=gate)`,
     whatever the status bucket.
 C2. statiker_emit.py: `"SKILL_VERSION_HOLD": "barred"`.
 C3. `skill_version_hold` reads the HEADER `Skill:` line only. Mark
     the header entry where `parse_tracker` appends it with an
     additive key `"header": True` and select on that key; a record
     whose header has no `Skill:` line holds nothing, whatever its
     body stamps say.
 C4. Correct the cache-path sentence in `own_served_version`'s
     docstring only after opening one installed copy under
     `~/.claude/plugins/cache/statiker/statiker/` with the Read or
     Glob tool; if you cannot establish the layout, leave the
     sentence and report it.
D. Compaction hook (plugin/hooks/statiker_postcompact.py).
 D1. `_HEADER_LINES = 20`.
 D2. `main` resolves the repository root from the payload's cwd —
     `git -C <cwd> rev-parse --show-toplevel` through `subprocess`
     with a short timeout — and passes that to `live_trackers`; any
     failure falls back to the cwd as given.

## Verifier (in order; real output pasted in the report)
1. Red first, per item: write the new arms, run them against the
   UNCHANGED scripts and paste the red, then implement and paste the
   green. State the baseline of each arm's file before your edit.
   Arms owed, each asserting the named outcome:
   - A: corrected mistyped label plus a correct one, `--out` inside
     scope → ARTIFACT_WRITTEN; head-region `Containment: ...` prose
     and no label → no containment hold; a spaced path, inside →
     ARTIFACT_WRITTEN, outside → ARTIFACT_CONTAINMENT_HOLD; MUST NOT
     MOVE: an uncorrected body near-miss still holds, and the
     doubled-space label is still a near-miss.
   - B: `— F2, F3` → the unit is unconverged and a closing
     [ZERO-DELTA] is ZERO_DELTA_UNCONVERGED; the hyphen form →
     `convergence-near-miss` in lint and sweep holds; `[PENDING]
     ... CONVERGED at A99` → does not count, lints, and closure
     stays ZERO_DELTA_UNCONVERGED where the unit is named; a unit
     named ONLY by an UNCONVERGED record (no unit D-line) bars the
     close; terminal [BIT] with an unconverged named unit →
     ZERO_DELTA_UNCONVERGED; `absence_units` lists an ABSENCE unit;
     MUST NOT MOVE: `test_scopeless_d_line_no_units_to_check` (a
     record naming no unit checks nothing).
   - C: version hold → `lock-check` LOCK_GATE_HOLDS and
     `lock-commit` lands no commit; route reads `barred`;
     marker-less header plus body stamp → no hold.
   - D: Status/Phase at header lines 16-17 → the notice fires; cwd
     one directory below the root → the notice fires.
2. `python3 -m pytest /home/g/dev/Gunther-Schulz/statiker/tools/ -q -p no:cacheprovider`
   run with the repo as working directory if the batteries need it
   (say which you used) — full counts, skips included. Baseline is
   723 passed, 0 skipped; a skip is a finding.
3. `python3 /home/g/.claude/plugins/cache/skill-craft-marketplace/skill-craft/2.2.8/tools/register_lint.py --band 52 30 /home/g/dev/Gunther-Schulz/statiker/plugin/skills/statiker/SKILL.md`
   must still exit 0 (you do not edit the page; this proves it).

## Write boundaries
Yours: `plugin/skills/statiker/scripts/statiker_record.py`,
`plugin/skills/statiker/scripts/statiker_git.py`,
`plugin/skills/statiker/scripts/statiker_emit.py`,
`plugin/hooks/statiker_postcompact.py`, `tools/test_statiker_record.py`,
`tools/test_statiker_git.py` (if that is where the lock arms live —
find it, do not create a parallel file), `tools/test_contract.py`,
`tools/test_statiker_postcompact_hook.py`, and files under
`tools/golden-corpus/`.
NOT yours: `plugin/skills/statiker/SKILL.md` (if the contract
battery demands page text that is not there, STOP and report the
exact assertion — do not edit the page, do not weaken the
assertion), `plugin/.claude-plugin/plugin.json` (no bump: 0.2.105
is unreleased), `defaults/models`, everything under `dev-notes/`,
`docs/`, `ITEMS*.md`, `LEDGER.md`.
Commit by pathspec, flags before the separator:
`git -C /home/g/dev/Gunther-Schulz/statiker commit -F <message file in your scratchpad> -- <paths>`.
Never `git add -A`, never amend, never push (pushing is the
dispatcher's). The plugin is not live on write: the installed copy
is a separate cache directory at 0.2.103. The hook file is NOT
registered from this checkout either.

## Commit plan
Guards (read by the dispatcher): `core.hooksPath` =
`~/dev/Gunther-Schulz/dotfiles/git/hooks`, holding `pre-commit`
(payload changed without a version bump — compares the committed
manifest against the INSTALLED version; committed 0.2.105 against
installed 0.2.103, so payload commits pass, as the dispatcher's own
payload commit did today), `post-commit`, `pre-push` (dispatcher
only). No bump commit: the manifest stays 0.2.105, already pushed.
One commit per item, in order A, B, C, D, each carrying its own
arms. Title pattern: `eve review repair <letter>: <what>`. Trailer,
verbatim, last line of every message:
`Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`

## Before your first build call
Send ONE message: which Background line you find unopened or wrong,
and which two lines of this brief contradict each other. Then
continue without waiting for a reply.

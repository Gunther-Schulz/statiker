# Brief: statiker payload — st-80 runtime containment check + st-84 version-mismatch gate

Title: sonnet: statiker payload — runtime containment check (st-80) and version-mismatch gate (st-84)
Working copy: /home/g/dev/Gunther-Schulz/statiker (main checkout, SHARED with the dispatcher desk; dispatcher tree clean and pushed at base).
Base: the commit that adds THIS file. Check on arrival: `git -C /home/g/dev/Gunther-Schulz/statiker log --oneline -1 -- docs/directives/2026-09-29-payload-st80-st84-brief.md` names the base; then `git merge-base --is-ancestor <base> HEAD` AND `git log --oneline <base>..HEAD`. Base contained + nothing on top = clean start. Base not contained, clean tree = fast-forward to base. Base contained + foreign commits on top = HALT and report them. Also `git status --porcelain` over the write set: any modified file there = HALT.
Scratch: your OWN scratchpad, never the dispatcher's.

## Grounding basis — read before building; the report cites what was actually read
- the executor skill (dispatch-guards:executor) — load FIRST
- ITEMS.md, blocks `## st-80` and `## st-84` — the two items, verbatim; their done-criteria are the acceptance bars
- LEDGER.md, the two `decision:` lines dated 2026-09-29 (containment-scope persistence; hypothesis-patch provenance) — the design decisions this brief renders
- plugin/skills/statiker/scripts/statiker_git.py — the preflight containment gate region (content anchor: `PREFLIGHT_CONTAINMENT_HOLD`, finish call at :1353 as of base) — where the scope-persist write lands
- plugin/skills/statiker/scripts/statiker_record.py — content anchors: `ARTIFACT_IN_REPO` (finish call at :2952 as of base — the st-80 item cites :2752-2761, the region MOVED, work from the anchor and report the offset), `MACHINE_TOKEN_CODES` (:685), `RULE_MINT_VERSION` (:369), `skill_versions` parsing (:412-420)
- plugin/skills/statiker/SKILL.md — the resume passage (content anchors: `WRITES NO CLOSE` at :264, `attribution, never a gate` at :280; second instance :878)
- git show d946b1a — the model instance for HOW a machine token mints (MACHINE_TOKEN_CODES + RULE_MINT_VERSION + near-miss lint), and git show 768404a b76a30f 7ea73fc — the st-74 model for gate + page passage + C4b mint record
- PLAN.md:21-43 — the live tenet list (the C4b tenet check enumerates THIS list)
- CLAUDE.md (this repo) — the Birth-class bullet and its C4b paragraph (what counts as a mint), and the skill-edit gate: **invoke the Skill tool `skill-craft:skill-craft` in the same turn BEFORE any SKILL.md edit** (repo discipline; a guarded write path, named here so you do not meet it as a surprise)

## Background (each line opened at brief time 2026-09-29 unless graded)
- ARTIFACT_IN_REPO asks only whether --out is inside ANY repo; no containment-scope check exists at runtime (opened: grep at base, finish call :2952)
- The preflight gate is satisfiability-only and its declared scope is persisted nowhere downstream (from st-80's evidence slot, verified 2026-09-15 by statiker-d4; re-anchored today only at the token level — grade: the "persisted nowhere" half is from-source, not re-proven today; if you find a persistence path, that is a FINDING, report before building)
- skill_versions is parsed for sweep scoping and is attribution, never a gate (opened: :412-420 and SKILL.md :280)
- Commit-blocking guards: global `core.hooksPath` points at the dotfiles hooks payload, which carries a payload-version guard comparing the committed manifest against the INSTALLED copy (source: LEDGER.md:96, the wave-1 brief-defect record — from record, mechanism not re-read today). The exemption is currently ARMED: manifest committed 0.2.104, installed 0.2.103 (opened: session banner + plugin pin-hold state). Your commits pass while they differ. DO NOT PUSH — a push is the dispatcher's act and would move nothing here (the guard keys on installed), but the push set is the branch and publication is the dispatcher's.
- The installed plugin serves 0.2.103 from the cache; nothing you write is live on write (pin hold: the pin moves only at run seams). Not deployment-coupled.

## The settled design — implement exactly this, do not redesign

**Item order: st-80 first, then st-84. Per-item commits.**

**Commit 0 (first):** bump `plugin/.claude-plugin/plugin.json` version to 0.2.105 — the lane bumps, this commit only. Both mints below record 0.2.105 as their mint version.

**st-80 — runtime containment check on artifact --out.**
- The preflight containment gate (statiker_git.py), when a `--containment` scope is DECLARED, PERSISTS the declared scope into the run record as a tool-owned field. Assigned field name: `containment_scope`. Written where preflight already writes its verdict fields, same idiom.
- statiker_record.py's --out handling: when the record carries `containment_scope`, an --out path outside every scope path finishes with a NEW hold verdict. Assigned token: `ARTIFACT_CONTAINMENT_HOLD`, exit 2, added to MACHINE_TOKEN_CODES and RULE_MINT_VERSION (version 0.2.105) exactly per the d946b1a pattern.
- Record WITHOUT the field: behavior unchanged (ARTIFACT_IN_REPO only). That absence rule is the whole absence semantics — whatever else the check cannot read is could-not-verify, never a silent pass into the new hold.
- Page (SKILL.md): the passage that names artifact --out routing gains the verdict. Enumerate EVERY seam that names --out disposition and name the token at each (the repo's multi-location-verdict lesson: a token named at one seam fails open at the seam nobody re-read). Skill-craft invocation before the edit.
- C4b: this IS a mint (new token + hold code). OBSERVATIONS entry, four slots, provenance = the st-64 amended-evidence field instance plus narrow-round B3 (docs/audits/2026-09-14-narrow-round-run3-contract.md), plus the tenet check enumerating every PLAN.md:43 tenet, each marked pass/fail/not-applicable.

**st-84 — version-mismatch resume gate.**
- The record tool derives its OWN served version from its install path (the plugin cache path carries the version — SKILL.md already states this for the desk read) and compares it against the record header `Skill:` line it already parses.
- Record header version NEWER than the tool's own → NEW hold verdict. Assigned token: `SKILL_VERSION_HOLD`, exit 2, MACHINE_TOKEN_CODES + RULE_MINT_VERSION (0.2.105), d946b1a pattern. Equal versions, tool newer than record, or marker-less record → NO fire (marker-less is out of scope per the no-grandfather narrowing).
- Page (SKILL.md): the resume passage (:264 region) names the verdict. The `attribution, never a gate` sentence (:280, :878) must stay TRUE: scope it precisely — skill_versions line-attribution stays attribution for sweep scoping; the new gate is the header-vs-tool comparison only. Do not widen the gate's claim beyond what it checks.
- Provenance class (decided): MARKED HYPOTHESIS-PATCH. The OBSERVATIONS entry marks it as such and carries the pre-registered validation criterion verbatim: "validated by the first field incident of an older desk over a newer record, or graded at the next fire-rate review, whichever comes first; a 0-incident record at that review argues retirement, not tightening." Plus the C4b tenet check as above.

**Pre-authorized repair class (both items):** if the token registry's naming idiom contradicts an assigned token spelling, conform to the registry idiom and report the rename as a deviation with the idiom evidence. Novel deviations still halt the ITEM (never the lane) and are reported.

## Verifier (in order; real output pasted in the report)
1. BASELINE first: `python3 -m pytest tools/ -q` before any change — paste full counts. The red-first proofs below are meaningless over an unstated baseline.
2. Red-first, per item: the new arms run against the UNREPAIRED tool and go RED (paste the red), then green after the repair. State the arrangement (which side was old, where the expectations came from). st-80 arms: RED = --out outside a declared persisted scope (terra's act shape); MUST-NOT-MOVE = --out inside scope stays silent; absent-field arm = no fire. st-84 arms: header ahead of tool = fires; equal = no fire; marker-less = no fire.
3. Full suite after: `python3 -m pytest tools/ -q` — full counts, every skip dispositioned; compare skip count against the baseline.
4. `python3 ~/.claude/plugins/cache/skill-craft-marketplace/skill-craft/2.2.8/tools/register_lint.py --band 52 30 plugin/skills/statiker/SKILL.md` — exit 0, paste.
5. `awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'` — print the number (trial metric, for the record; no gate).

## Write boundaries
- Owned: plugin/skills/statiker/scripts/statiker_record.py, plugin/skills/statiker/scripts/statiker_git.py, plugin/skills/statiker/SKILL.md, plugin/.claude-plugin/plugin.json (version line only), tools/test_statiker_record.py, dev-notes/OBSERVATIONS.md (append entries only). New fixtures follow test_statiker_record.py's existing fixture idiom, in that file or beside it under tools/ with names carrying `st80`/`st84`.
- NOT touched: ITEMS.md, LEDGER.md, CLAUDE.md, PLAN.md, everything else. The dispatcher owns bookings.
- Commits: per item, by pathspec — `git commit -m "…" -- <paths>` with every flag BEFORE the `--`; a NEW file gets `git add -N <path>` (file, never a directory) first. Never amend — always a new commit. Commits UNPUSHED; the dispatcher pushes after verification.
- Commit trailer, verbatim on every commit:
  `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`

## Commit plan
- Guards: the dotfiles payload-version guard via global core.hooksPath (read basis in Background). Exemption armed (0.2.104 committed ≠ 0.2.103 installed); your commit 0 bumps to 0.2.105, keeping it armed. No other commit-blocking hook is known for this repo from the wave-1 record; if one fires, that is the pre-authorized reorder class — satisfy it and report the permutation.
- Order: (0) manifest bump 0.2.105 → (1) st-80 code+tests → (2) st-80 page+OBSERVATIONS → (3) st-84 code+tests → (4) st-84 page+OBSERVATIONS. Splitting (1)/(2) per item is acceptable to merge into one commit per item if the page edit is small; per-ITEM attribution is the floor.

## Critique pass (before your first build call)
Send ONE message: which Background line you find unopened or wrong, and which two lines of this brief contradict each other. Then continue without waiting for a reply.

## Tail (binding)
A mid-run message may not arrive before the turn ends: on a gap
HALT THE ITEM, FINISH THE REMAINDER, REPORT — never halt the
LANE, since "halt and wait" is not a survivable state for a
subagent.
Closing report (mandatory; the §2 form): (a) items completed w/
evidence, (b) checks RUN w/ real output — FULL counts incl.
skips (`N passed, M failed, K skipped`), each skip dispositioned
(which check, why, whether the reason touches the item); a skip
in a check YOU built is a finding, not a pass — the built branch
did not execute, (c) gaps surfaced — incl. anything needing a
tier above yours, returned as a question with its evidence, never
settled at your tier, (d) deviations w/ reason, (e) candidate
lessons, (f) files touched + commit hashes (unpushed) — only
commits whose Co-Authored-By trailer is YOURS; one you cannot
claim by trailer is "present in the tree, not mine"; a
`.git/config` write counts as a repo write, (g) what was NOT
verified, (h) sources actually read, of those the brief named.
Every claim about something OUTSIDE your own work — a file you
did not write, a mechanism, another repo, a tool's behavior —
names the read that opened it, or carries "inferred, unverified";
a recommendation resting on an unopened claim carries the grade
too.
Drain your inbox before sending, and between parts of a
multi-part report: every dispatcher message received up to send
time is dispositioned or named as unhandled.
Message ≤3000 chars each: a report longer than one message is
SPLIT into labeled parts (1/N) — do NOT write a report FILE
(harness-blocked for subagents); supporting data goes to the
brief's assigned DATA files, the message carries key findings
+ any such paths. A missing decision, file, or value is surfaced
as a gap, never bridged with a guess.
A check that got backgrounded is AWAITED before the closing
report — ending your turn orphans it; a report sent with a check
still running is an INTERIM report, says so, and names what
remains.
Commits unpushed, by pathspec — `git commit -m "…" -- <paths>`
with every flag BEFORE the `--` (`-F` for a multi-line message),
never `git add` then `git commit` and never `-A`. A NEW file is
invisible to a pathspec commit until `git add -N <path>` registers
it. Trailer: `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.
Never amend — always a new commit.
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended.

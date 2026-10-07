# Eve review 2026-10-07 — the lanes' reports, verbatim

Extracted from the lane transcripts of session 7196f402 (each lane's
own SendMessage bodies, in send order, unedited). Evidence bodies for
docs/audits/2026-10-07-eve-review-dispositions.md. The two machine-half
lanes of round one (opus-review-s2, opus-review-s2b) sent nothing and
have no section.


## opus-review-w

HOLD — 1 BLOCKING, 6 MAJOR, 6 MINOR. Review of f954320..ae19e24 (HEAD confirmed ae19e24).

Suite: `python3 -m pytest tools/ -q -p no:cacheprovider` → 723 passed, 18 subtests passed, 0 skipped, 0 failed (91s). Every finding below marked "executed" was run against the HEAD scripts on scratch repos in my own scratchpad; nothing was written to the repo.

Abbreviations: REC = plugin/skills/statiker/scripts/statiker_record.py, GIT = .../statiker_git.py, EMIT = .../statiker_emit.py, PAGE = plugin/skills/statiker/SKILL.md.

## BLOCKING

**B1 — SUBSTANCE — one label-shaped line makes `filter` unrunnable for the rest of the run, with no repair route.**
Sites: REC:344 (near regex `(?i)^\s*containment\s*:`), REC:3160 (filter's malformed check), REC:1330 (lint), PAGE:617-620, PAGE:1080-1084, EMIT:164.
- `filter` scans the raw pinned lines; lint scans only the body region. They disagree, and a correcting entry cannot remove a line from an append-only record.
- Executed, four cases, all end in ARTIFACT_CONTAINMENT_HOLD (route halt, rc 2):
  - Operator INTENT line in the head `Containment: keep every artifact under ~/work please.` → `lint` LINT_CLEAN, `sweep` SWEEP_CLEAN, `filter` holds. The page says the line "lints `containment-near-miss`"; in the head it does not, so the first signal comes after the lock commit.
  - Mistyped label `Containment: /srv/x` → sweep holds; I appended the tool's own repair (`record: corrects line 10 …`) plus a correct `CONTAINMENT:` line → SWEEP_CLEAN, `filter` still holds on the old line.
  - Indented prose `  containment: note to self` → holds.
  - A declared path containing a space: `preflight` prints it in `containment_scope`, the exact regex (REC:340, `\S+`) cannot match it, so the faithful transcription is itself "malformed" → holds.
- What a desk does: it cannot produce an attack artifact, so no round can dispatch. The page names no way out; the `halt` route's "operator's clearing reply re-enters" has nothing to clear. Unattended, the run dies at its first attack.
- Reach: any run that declares containment (the transcription is a hand step) and any run whose tracker carries such a line for any reason.
- Battery: TestSt89 pins that the hold fires; no arm asks whether a repaired record can filter again, none covers a head-region line or a path with a space.

## MAJOR

**M1 — SUBSTANCE — the convergence gate checks nothing on a record whose design D-lines are scopeless.**
Sites: REC:2336-2343, PAGE:1370-1374, tools/test_statiker_record.py:1558-1562.
- The unit population is "D-lines whose body opens `unit U<k>`". The page nowhere tells a desk to open design D-lines that way; units are declared by `unit U<k> write-set:` F-lines (PAGE:1601-1606).
- Executed: scopeless D1, `F unit U1 write-set`, `F unit U2 write-set`, A1 [ZERO-DELTA], no CONVERGED line → `closure` CLOSURE_LIVE, `closure --unit U2` UNIT_DISPATCHABLE. Control with `D1 … unit U1 …` → ZERO_DELTA_UNCONVERGED ['U1'].
- The golden tracker has 8 D-lines, 1 unit-scoped (a bookkeeping line), against 8 unit write-set F-lines.
- The battery pins the vacuous pass as intended (`test_scopeless_d_line_no_units_to_check`).

**M2 — SUBSTANCE — a terminal [BIT] round opens closure without the convergence check.**
Sites: REC:2321 (guard sits in the ZERO-DELTA branch only), PAGE:1536-1554 (the [BIT]-amends-no-design path), PAGE:1374 ("an aimed round's zero cannot close design").
- Executed: unit-scoped D1/D2, round aimed at U1 with one substance F-line, A1 [BIT], no CONVERGED anywhere → CLOSURE_LIVE, `closure --unit U2` UNIT_DISPATCHABLE.
- No arm covers this path.

**M3 — SUBSTANCE — the convergence forms fail open on a slip and are not checked against the record.**
Sites: REC:232-236, REC:2205-2224, PAGE:1360-1362, PAGE:1383-1387.
- Executed: `record: unit U1 UNCONVERGED at A2 - F2` (hyphen for the dash) → LINT_CLEAN, closure CLOSURE_LIVE; U1 stays converged. Exact form → ZERO_DELTA_UNCONVERGED. There is no near-miss lint class, unlike the tripwire arm.
- Executed: `- F1 [PENDING] record: unit U1 CONVERGED at A99 — basis: unverified`, appended after the closing A-line → CLOSURE_LIVE. The round id is not resolved, the tag is not read, and a line added after the refusal satisfies it.
- A near-miss CONVERGED fails safe; a near-miss UNCONVERGED is the open direction.

**M4 — SUBSTANCE — SKILL_VERSION_HOLD does not stop the lock.**
Sites: GIT:977-981 (`blocking = gate.get("violations") or []`), REC:2109-2114, PAGE:279-283, PAGE:306-309.
- The lock gate keys on the sweep verdict's `violations` field; the hold verdict carries none, so it reads as an empty blocking set.
- Executed with header 0.2.106 and `STATIKER_SERVED_VERSION=0.2.105`: `sweep` and `closure` → SKILL_VERSION_HOLD; `lock-check` → LOCK_CHECK_CLEAN (`gate` null); `lock-commit` → LOCK_COMMITTED, commit e2d5168 landed. `lint` and `filter` also proceed (LINT_CLEAN, ARTIFACT_WRITTEN).
- `unit-start` does halt (UNIT_GATE_BLOCKED), because that gate keys on the verdict name.
- The page says an older desk "proceeds no further than the record gate" and "appends nothing". No arm drives the hold through the git tool; the contract battery freezes the verdict as undriven.

**M5 — SUBSTANCE — the SKILL_VERSION_HOLD token obliges the writes its seam forbids (the multi-location check).**
Sites: EMIT:169 (`surface`), PAGE:164-171, PAGE:279-283, PAGE:306-309.
- `surface` means: book the verdict line as a `record:` F-line, and unattended take the seam's terminal disposition (FAILED / rides the close).
- The resume passage says the opposite for this case: WRITES NO CLOSE, appends nothing, the run stays in-progress, the surfacing is the desk's reply.
- The page's own floor (PAGE:121-126) says a desk reading only the token is never unsafe. Here a token-only desk writes into a newer-rules record and closes it FAILED. Read, not executed (it is a page-versus-registry contradiction).

**M6 — SUBSTANCE — the page says `trend` counts every F-line; the tool now excludes `record:`-scoped ones.**
Sites: REC:2716-2723, PAGE:98-99, PAGE:1290-1295.
- Executed: a round with one substance F-line and two `record:` F-lines → `counts: [1]`, `record_counts: [2]`.
- Both page passages are unchanged by the delta and now false ("every F-line in a round's span"; "the counts half stays class-blind"). A desk grading the series reasons from the wrong meaning of the number.

## MINOR

**m1 — SUBSTANCE — the version hold fires off a body stamp on a marker-less record.**
Sites: REC:399, PAGE:305-312.
- Executed: no header `Skill:` line, body `SKILL: statiker 0.2.110`, served 0.2.105 → SKILL_VERSION_HOLD. Page and docstring both say marker-less holds nothing and mid-run stamps are never read.
- Opposite case, executed: header 0.2.101 with a later 0.2.110 stamp → SWEEP_CLEAN. An older desk following a newer one is caught only when the header itself is newer.

**m2 — SUBSTANCE — the compaction hook (open question 2).**
Sites: plugin/hooks/hooks.json, plugin/hooks/statiker_postcompact.py:63-67 and 137-142.
- Executable bit: mode 100755 in git; the installed cache copies of the sibling hook are rwxr-xr-x (`ls -l ~/.claude/plugins/cache/statiker/statiker/0.2.103/hooks/`).
- `${CLAUDE_PLUGIN_ROOT}`: the reference harness source substitutes the plugin's install path (utils/hooks.ts:845); the cache layout is `<version>/hooks/`, so the command resolves. Inferred for the live harness, unverified; no real compaction was exercised.
- Live statuses: in-progress, [READY], PASSED fire; FAILED and COMPLETE are silent. Matches the page.
- Silent when cwd is not the repo root — executed: cwd `…/hk/sub` → empty output. The harness cwd can move mid-session, so this is the fail-open case; no arm covers it.
- Subagent lane: executed with `agent_type` in the payload → identical notice, tracker path included. The reference source's compact call passes only `model`, so the hook cannot tell a lane from the desk; it relies on its own sentence "A dispatched lane ignores this notice". An attack or verify lane would be handed the tracker path and the record tool's verbs.
- Header window is 15 lines; the page says Status and Phase sit "within the first ~20 lines". Executed: fields at lines 16-17 → silent.
- The page never mentions the hook or its notice.

**m3 — SUBSTANCE — no verdict surfaces convergence or ABSENCE state.**
Sites: PAGE:1805-1808, REC closure verdict.
- Executed: closure verdict keys are closing, entries, head_boundary, irreversible_units, late_intent, mode, post_closure, r_lines, route, skill_versions, verdict.
- The verify brief's ABSENCE demand is therefore composed from a tracker body-read, the thing the same paragraph forbids for `post_closure`.

**m4 — WORDING — ZERO_DELTA_UNCONVERGED: "a landing is REFUSED" describes something the tool cannot do.**
Sites: PAGE:1370-1374, PAGE:313-318, EMIT:144.
- `closure` runs after the A-line is appended. The page gives no recovery step (the working one is appending the missing CONVERGED/ABSENCE lines — see M3), and the resume passage's list of closure state verdicts omits it.
- The `barred` token is consistent with the single page location that names it.

**m5 — RECORD — register and docstring leftovers (open question 3).**
- Page (PAGE:1852-1858), register order (`verify: sonnet` first) and READINESS.json's `update_2026_10_07` agree: sonnet runs the verify leg on a Claude harness.
- The register still says "so haiku carries this role at haiku's price" and "HAIKU still carries this role on price", and its first line still calls itself "the certified-attack register" with an attack-only resolution order.
- READINESS.json's `why` text still describes the old resolution; the note beside it says so.
- REC:364 states the cache path as `<version>/plugin/skills/…`; the real layout is `<version>/skills/…`. The function works either way.

**m6 — RECORD — `containment-near-miss: "0.2.105"` (open question 1).**
Sites: REC:461, REC:481-482, REC:518.
- The value matches the manifest, and the manifest already read 0.2.105 at the commit that minted the code (7819e2f). Correct as attribution if this ships as 0.2.105.
- It scopes nothing: the code is not in FORM_CODES_MINT_GATED, so `is_retro` returns False before reading the table. A record seeded earlier and resumed under this version is graded on every line.
- The installed pin is 0.2.103 (`installed_plugins.json`) while the reviewed base's manifest is 0.2.101, and 0.2.102/0.2.103 sit in the cache. I did not establish which content those releases carried.
- Also stated on the page rather than a defect: a desk that skips the `CONTAINMENT:` transcription gets no gate and nothing notices (PAGE:255-258).

## Not reached
- tools/test_statiker_record.py and tools/test_statiker_postcompact_hook.py: arm names and the st-85 class bodies read; the other new arms not read line by line.
- The st-86 "why" text, the `corrects-nothing` placeholder fix and the defang case fix: covered by the green suite only.
- The entry-owned half of the defang ownership split (PAGE:644-651): my probe used the wrong id, so it is unverified. The owner-less half executed as the page states.
- The budget-raise `cause:` slot: page-only, no tool reads it; not exercised.
- `references/` files and a live compaction in a real session.

---

(1/5) HOLD — 1 BLOCKING, 6 MAJOR, 6 MINOR. Review of f954320..ae19e24, HEAD confirmed ae19e24.

Suite: `python3 -m pytest tools/ -q -p no:cacheprovider` → 723 passed, 18 subtests passed, 0 skipped, 0 failed. "Executed" below = run against the HEAD scripts on scratch repos in my own scratchpad; nothing written to the repo.
REC = plugin/skills/statiker/scripts/statiker_record.py, GIT = .../statiker_git.py, EMIT = .../statiker_emit.py, PAGE = plugin/skills/statiker/SKILL.md.

**B1 — BLOCKING — SUBSTANCE — one label-shaped line makes `filter` unrunnable for the rest of the run, with no repair route.**
Sites: REC:344 (near regex `(?i)^\s*containment\s*:`), REC:3160 (filter's malformed check), REC:1330 (lint), PAGE:617-620, PAGE:1080-1084, EMIT:164.
- `filter` scans the raw pinned lines; lint scans only the body region. A correcting entry cannot remove a line from an append-only record.
- Executed, four cases, each ends ARTIFACT_CONTAINMENT_HOLD (route halt, rc 2):
  - Operator INTENT line in the head, `Containment: keep every artifact under ~/work please.` → LINT_CLEAN, SWEEP_CLEAN, `filter` holds. The page says such a line "lints `containment-near-miss`"; in the head it does not, so the first signal comes after the lock commit.
  - Mistyped label `Containment: /srv/x` → sweep holds; I appended the tool's own repair (`record: corrects line 10 …`) plus a correct `CONTAINMENT:` line → SWEEP_CLEAN, `filter` still holds on the old line.
  - Indented prose `  containment: note to self` → holds.
  - A declared path containing a space: `preflight` prints it in `containment_scope`, the exact regex (REC:340, `\S+`) cannot match it, so the faithful transcription is itself malformed → holds.
- What a desk does: no attack artifact, so no round dispatches. The page names no way out; the `halt` route's "operator's clearing reply re-enters" has nothing to clear. Unattended, the run dies at its first attack.
- Reach: any run that declares containment (transcription is a hand step) and any tracker carrying such a line for any reason.
- Battery: TestSt89 pins that the hold fires; no arm asks whether a repaired record can filter again, none covers a head-region line or a path with a space.

---

(2/5) MAJOR findings M1-M3, all on the unit-convergence gate.

**M1 — MAJOR — SUBSTANCE — the convergence gate checks nothing on a record whose design D-lines are scopeless.**
Sites: REC:2336-2343, PAGE:1370-1374, tools/test_statiker_record.py:1558-1562.
- The unit population is "D-lines whose body opens `unit U<k>`". The page nowhere tells a desk to open design D-lines that way; units are declared by `unit U<k> write-set:` F-lines (PAGE:1601-1606).
- Executed: scopeless D1, `F unit U1 write-set`, `F unit U2 write-set`, A1 [ZERO-DELTA], no CONVERGED line → `closure` CLOSURE_LIVE, `closure --unit U2` UNIT_DISPATCHABLE. Control with `D1 … unit U1 …` → ZERO_DELTA_UNCONVERGED ['U1'].
- The golden tracker has 8 D-lines, 1 unit-scoped (a bookkeeping line), against 8 unit write-set F-lines.
- The battery pins the vacuous pass as intended (`test_scopeless_d_line_no_units_to_check`).

**M2 — MAJOR — SUBSTANCE — a terminal [BIT] round opens closure without the convergence check.**
Sites: REC:2321 (the guard sits in the ZERO-DELTA branch only), PAGE:1536-1554 (the [BIT]-amends-no-design path), PAGE:1374 ("an aimed round's zero cannot close design").
- Executed: unit-scoped D1/D2, a round aimed at U1 with one substance F-line, A1 [BIT], no CONVERGED anywhere → CLOSURE_LIVE, `closure --unit U2` UNIT_DISPATCHABLE.
- No arm covers this path.

**M3 — MAJOR — SUBSTANCE — the convergence forms fail open on a slip and are not checked against the record.**
Sites: REC:232-236, REC:2205-2224, PAGE:1360-1362, PAGE:1383-1387.
- Executed: `record: unit U1 UNCONVERGED at A2 - F2` (hyphen for the dash) → LINT_CLEAN, closure CLOSURE_LIVE; U1 stays converged. Exact form → ZERO_DELTA_UNCONVERGED. There is no near-miss lint class, unlike the tripwire arm.
- Executed: `- F1 [PENDING] record: unit U1 CONVERGED at A99 — basis: unverified`, appended after the closing A-line → CLOSURE_LIVE. The round id is not resolved, the tag is not read, and a line added after the refusal satisfies it.
- A near-miss CONVERGED fails safe; a near-miss UNCONVERGED is the open direction.

---

(3/5) MAJOR findings M4-M6.

**M4 — MAJOR — SUBSTANCE — SKILL_VERSION_HOLD does not stop the lock.**
Sites: GIT:977-981 (`blocking = gate.get("violations") or []`), REC:2109-2114, PAGE:279-283, PAGE:306-309.
- The lock gate keys on the sweep verdict's `violations` field; the hold verdict carries none, so it reads as an empty blocking set.
- Executed with header 0.2.106 and `STATIKER_SERVED_VERSION=0.2.105`: `sweep` and `closure` → SKILL_VERSION_HOLD; `lock-check` → LOCK_CHECK_CLEAN (`gate` null); `lock-commit` → LOCK_COMMITTED, a commit landed. `lint` and `filter` also proceed (LINT_CLEAN, ARTIFACT_WRITTEN).
- `unit-start` does halt (UNIT_GATE_BLOCKED): that gate keys on the verdict name.
- The page says an older desk "proceeds no further than the record gate" and "appends nothing". No arm drives the hold through the git tool; the contract battery lists the verdict as undriven.

**M5 — MAJOR — SUBSTANCE — the SKILL_VERSION_HOLD token obliges the writes its seam forbids (the multi-location check, open question 4).**
Sites: EMIT:169 (`surface`), PAGE:164-171, PAGE:279-283, PAGE:306-309.
- `surface` means: book the verdict line as a `record:` F-line, and unattended take the seam's terminal disposition (FAILED / rides the close).
- The resume passage says the opposite for this case: WRITES NO CLOSE, appends nothing, the run stays in-progress, the surfacing is the desk's reply.
- The page's floor (PAGE:121-126) says a desk reading only the token is never unsafe. Here a token-only desk writes into a newer-rules record and closes it FAILED. Read, not executed: it is a page-versus-registry contradiction.

**M6 — MAJOR — SUBSTANCE — the page says `trend` counts every F-line; the tool now excludes `record:`-scoped ones.**
Sites: REC:2716-2723, PAGE:98-99, PAGE:1290-1295.
- Executed: a round with one substance F-line and two `record:` F-lines → `counts: [1]`, `record_counts: [2]`.
- Both page passages are unchanged by the delta and now false ("every F-line in a round's span"; "the counts half stays class-blind"). A desk grading the series reasons from the wrong meaning of the number.

Other verdicts the delta adds, checked against every page location naming them: ARTIFACT_CONTAINMENT_HOLD (`halt`; PAGE:252-254, 617-620, 1080-1084) — consistent apart from B1. ZERO_DELTA_UNCONVERGED (`barred`; one location) — see m4.

---

(4/5) MINOR findings m1-m3.

**m1 — MINOR — SUBSTANCE — the version hold fires off a body stamp on a marker-less record.**
Sites: REC:399, PAGE:305-312.
- Executed: no header `Skill:` line, body `SKILL: statiker 0.2.110`, served 0.2.105 → SKILL_VERSION_HOLD. Page and docstring both say marker-less holds nothing and mid-run stamps are never read.
- Opposite case, executed: header 0.2.101 with a later 0.2.110 stamp → SWEEP_CLEAN. An older desk following a newer one is caught only when the header itself is newer.

**m2 — MINOR — SUBSTANCE — the compaction hook (open question 2).**
Sites: plugin/hooks/hooks.json, plugin/hooks/statiker_postcompact.py:63-67 and 137-142.
- Executable bit: mode 100755 in git; the installed cache copies of the sibling hook are rwxr-xr-x (`ls -l ~/.claude/plugins/cache/statiker/statiker/0.2.103/hooks/`).
- `${CLAUDE_PLUGIN_ROOT}`: the reference harness source substitutes the plugin's install path (~/dev/reference/claude-code/src/utils/hooks.ts:845); the cache layout is `<version>/hooks/`, so the command resolves. Inferred for the live harness, unverified; no real compaction was exercised.
- Live statuses: in-progress, [READY], PASSED fire; FAILED and COMPLETE are silent. Matches the page.
- Silent when cwd is not the repo root — executed: cwd `…/hk/sub` → empty output. The harness cwd can move mid-session, so this is the fail-open case. No arm covers it.
- Subagent lane: executed with `agent_type` in the payload → identical notice, tracker path included. The reference source's compact call passes only `model` (services/compact/compact.ts:592), so the hook cannot tell a lane from the desk; it relies on its own sentence "A dispatched lane ignores this notice". An attack or verify lane compacting in the repo would be handed the tracker path and the record tool's verbs.
- Header window is 15 lines; the page says Status and Phase sit "within the first ~20 lines". Executed: fields at lines 16-17 → silent.
- The page never mentions the hook or its notice.

**m3 — MINOR — SUBSTANCE — no verdict surfaces convergence or ABSENCE state.**
Sites: PAGE:1805-1808, REC closure verdict.
- Executed: the closure verdict's keys are closing, entries, head_boundary, irreversible_units, late_intent, mode, post_closure, r_lines, route, skill_versions, verdict.
- The verify brief's ABSENCE demand is therefore composed from a tracker body-read, which the same paragraph forbids for `post_closure`.

---

(5/5) MINOR findings m4-m6 and what I did not reach.

**m4 — MINOR — WORDING — ZERO_DELTA_UNCONVERGED: "a landing is REFUSED" describes something the tool cannot do.**
Sites: PAGE:1370-1374, PAGE:313-318, EMIT:144.
- `closure` runs after the A-line is appended. The page gives no recovery step (the working one is appending the missing CONVERGED/ABSENCE lines — see M3), and the resume passage's list of closure state verdicts omits it.

**m5 — MINOR — RECORD — register and docstring leftovers (open question 3).**
- Page (PAGE:1852-1858), register order (`verify: sonnet` first) and READINESS.json's `update_2026_10_07` agree: sonnet runs the verify leg on a Claude harness.
- plugin/skills/statiker/defaults/models still says "so haiku carries this role at haiku's price" and "HAIKU still carries this role on price", and its first line still calls itself "the certified-attack register" with an attack-only resolution order.
- READINESS.json's `why` text still describes the old resolution; the note beside it says so.
- REC:364 states the cache path as `<version>/plugin/skills/…`; the real layout is `<version>/skills/…`. The function works either way.

**m6 — MINOR — RECORD — `containment-near-miss: "0.2.105"` (open question 1).**
Sites: REC:461, REC:481-482, REC:518.
- The value matches the manifest, and the manifest already read 0.2.105 at the commit that minted the code (7819e2f). Correct as attribution if this ships as 0.2.105.
- It scopes nothing: the code is not in FORM_CODES_MINT_GATED, so `is_retro` returns False before reading the table. A record seeded earlier and resumed under this version is graded on every line.
- The installed pin is 0.2.103 (`~/.claude/plugins/installed_plugins.json`) while the reviewed base's manifest reads 0.2.101, and 0.2.102/0.2.103 sit in the cache. I did not establish which content those releases carried.
- Stated on the page rather than a defect: a desk that skips the `CONTAINMENT:` transcription gets no gate and nothing notices (PAGE:255-258).

**Not reached**
- tools/test_statiker_record.py and tools/test_statiker_postcompact_hook.py: arm names and the st-85 class bodies read; the other new arms not read line by line.
- The st-86 "why" text, the `corrects-nothing` placeholder fix and the defang case fix: covered by the green suite only.
- The entry-owned half of the defang ownership split (PAGE:644-651): my probe used the wrong id, so it is unverified. The owner-less half executed as the page states.
- The budget-raise `cause:` slot: page-only, no tool reads it; not exercised.
- `references/` files, and a live compaction in a real session.

---


## opus-review-s1

HOLD — page half of f954320..ae19e24: 1 BLOCKING, 6 MAJOR, 4 MINOR. HEAD verified ae19e24. Suite: `python3 -m pytest tools/ -q -p no:cacheprovider` -> 723 passed, 18 subtests passed, 0 skipped, 0 failed. All probes ran against HEAD's scripts on trackers in my own scratch git repo; nothing written to the statiker repo (status before/after: only the foreign `M dev-notes/next-run-prep.md`, `?? ITEMS-DONE.md.lock`). SKILL = plugin/skills/statiker/SKILL.md, REC = scripts/statiker_record.py, GIT = scripts/statiker_git.py.

Verdicts this delta adds/touches, each checked at every page site: ZERO_DELTA_UNCONVERGED (SKILL:1371-1374 only; route barred), ARTIFACT_CONTAINMENT_HOLD (SKILL:252-258, 617-620, 1080-1084; route halt), SKILL_VERSION_HOLD (SKILL:300-312 vs 279-283 vs route vocab 164-171; route surface), lint containment-near-miss (SKILL:618-620), TREND_COMPUTED counts (SKILL:98-100, 1289-1295), closure `post_closure` (SKILL:1804-1805), PREFLIGHT_OK/CONTAINMENT_HOLD `containment_scope` (SKILL:246-248).

F1 BLOCKING / SUBSTANCE — the convergence gate is vacuous on the record shape the page itself produces, while the same delta introduces aimed (subset) rounds.
Sites: SKILL:1362-1374 ("closure tool enforces the seam ... an aimed round's zero cannot close design"); REC cmd_closure d_units block (collects only D-lines whose body OPENS `unit U<k>`).
What happens: nowhere does the page tell the desk to open a design D-line with `unit U<k>` before closure (the only mandated pre-close unit-scoped lines are F write-set lines; the PRECEDENT LINE is "one clause of the unit's design D-line", no opener stated). With scopeless design D-lines, d_units is empty and any [ZERO-DELTA] — including an aimed round's — closes design and dispatches units with no CONVERGED record anywhere.
Executed: tracker with `- D1 [COMMITTED] design: U1 parses, U2 queries`, F write-set lines for U1/U2, `A1 [ZERO-DELTA]`, no convergence record -> `closure` = CLOSURE_LIVE route proceed; `closure --unit U1` = UNIT_DISPATCHABLE. Control (same record, D-lines opening `unit U1`/`unit U2`) -> ZERO_DELTA_UNCONVERGED unconverged [U1,U2]. The contract battery's own CLOSED_TRACKER (tools/test_contract.py:358-368) is the scopeless shape and is asserted green, so no arm goes red on this.

F2 MAJOR / SUBSTANCE — a terminal [BIT] bypasses the convergence gate entirely.
Sites: SKILL:1536-1541 ("the gate reads that as SATISFIED, the same predicate as ZERO-DELTA from there") vs SKILL:1371-1374; REC: the check sits only in the ZERO-DELTA `else` branch.
Executed: unit-scoped D1/D2, one scopeless substance F-line, `A1 [BIT]`, no D amendment, no convergence record -> CLOSURE_LIVE; `--unit U2` -> UNIT_DISPATCHABLE. Same record with ZERO-DELTA -> ZERO_DELTA_UNCONVERGED. So an aimed round that BITES without a design-amending D-line opens what an aimed round's zero cannot. "Same predicate" is no longer true.

F3 MAJOR / SUBSTANCE — a mistyped UNCONVERGED fails OPEN and lints clean; the page states only the safe direction.
Sites: SKILL:1360-1362 ("a near-form is ordinary bookkeeping and converges nothing"), 1383-1387; REC RECORD_UNCONVERGED_RE (exactly one F id).
Executed: U1 CONVERGED at A1; round 2 two findings; `record: unit U1 UNCONVERGED at A2 — F2, F3`; `A3 [ZERO-DELTA]` -> CLOSURE_LIVE, lint LINT_CLEAN. Control with `— F2` alone -> ZERO_DELTA_UNCONVERGED [U1]. Two findings on one unit is the ordinary case and the page gives no form for it (one line per finding? unstated). No near-miss class exists for these three forms.

F4 MAJOR / SUBSTANCE — ZERO_DELTA_UNCONVERGED has no stated way out, and the tool's actual way out is one unverified line.
Sites: SKILL:1371-1374; route `barred` (SKILL:150-154: "Nothing to book ... resolution is the run's own machinery").
The tool cannot refuse a "landing": the [ZERO-DELTA] A-line is already appended when closure runs. The page never says what the desk then does (another round? which A-line?). Executed: after the closing A-line, appending `- F1 [PENDING] record: unit U1 CONVERGED at A99 — basis: nothing` -> CLOSURE_LIVE. The record is accepted post-close, under any tag but INVALIDATED, citing a nonexistent round. An unattended desk under momentum clears the bar by assertion.
Related, by code read only (not executed): an ABSENCE record counts as converged for good (`in ("converged","absence")`), and SKILL:1383 un-converges only "a converged unit", so a unit with ABSENCE that then draws reading-round substance findings has no page route back to unconverged.

F5 MAJOR / SUBSTANCE — a `containment:`-shaped line that is not exact holds `filter` permanently; the repair the sweep names does not clear it, and three ordinary inputs produce it.
Sites: SKILL:617-620 ("lints `containment-near-miss` and holds `filter` on that same verdict"), 252-258, 1080-1084; REC CONTAINMENT_EXACT_RE `^CONTAINMENT: (\S+)$`, cmd_filter malformed check over raw pinned lines.
Executed: (a) `CONTAINMENT:  <path>` (two spaces): sweep SWEEP_HOLDS with repair "append record: corrects line 9"; after that line plus a correct label, sweep = SWEEP_CLEAN but filter = ARTIFACT_CONTAINMENT_HOLD still (malformed_containment lists line 9). Append-only means the line never leaves, so no attack artifact can be produced for the rest of the run. (b) A real declared path containing a space, transcribed exactly -> ARTIFACT_CONTAINMENT_HOLD, containment_scope []: no legal form exists for such a path. (c) Head-region prose `Containment: keep everything under ...` (operator INTENT is verbatim): `lint` = LINT_CLEAN, filter = ARTIFACT_CONTAINMENT_HOLD — the page says it lints; in the head region it does not, and the run is stuck with nothing in sweep pointing at why. Route is `halt`; the attack seam states no unattended close rule for a filter halt. Controls: exact label + inside --out -> ARTIFACT_WRITTEN; outside -> hold.

F6 MAJOR / SUBSTANCE — SKILL_VERSION_HOLD's route token contradicts its page disposition.
Sites: SKILL:279-283 (older desk "appends nothing", "WRITES NO CLOSE", "the surfacing is the desk's reply, not a record write", run "stays in-progress"), SKILL:306-309 ("mechanizing the WRITES-NO-CLOSE sentence"); statiker_emit ROUTES `SKILL_VERSION_HOLD: surface`; SKILL:164-171 (surface "carries halt's booking obligation ... unattended the run takes the seam's terminal disposition (FAILED / rides the close)").
Executed: `STATIKER_SERVED_VERSION=0.2.103 sweep|closure` on a 0.2.105 header -> `{"verdict":"SKILL_VERSION_HOLD","route":"surface",...}`. A desk reading the token books an F-line and closes FAILED — the two writes the passage forbids. SKILL:121-126 promises a token-only desk is never unsafe; here it is, and no sentence at the seam overrides the token.

F7 MAJOR / SUBSTANCE — under SKILL_VERSION_HOLD the lock gate fails OPEN (so the Close pin and any lock proceed).
Sites: SKILL:306-309; GIT lock_gate_check (keys on the sweep verdict's `violations`, absent on SKILL_VERSION_HOLD).
Executed: tracker with a latest-line [PENDING]: `lock-check` normally -> LOCK_GATE_HOLDS; same call with STATIKER_SERVED_VERSION=0.2.103 -> LOCK_CHECK_CLEAN route proceed. The hold removes the gate it claims to mechanize. Unit side is closed: `unit-start` -> UNIT_GATE_BLOCKED embedding the hold. Only sweep and closure carry the check; lint, trend, sustain, tripwire, waves, filter proceed (executed, matches the page's "sweep and closure each"). Reachable only from the release after this one (an older tool lacks the check).

F8 MINOR / SUBSTANCE — page and tool disagree on what `trend` counts.
Sites: SKILL:98-100 ("every F-line in a round's span"), SKILL:1290-1295 ("read every F-line regardless of class ... the counts half stays class-blind") — unchanged sentences; REC trend_over_rounds now excludes `record:`-scoped F-lines.
Executed: round with 1 finding + 2 record-scoped F-lines -> `findings [1 (+2 record)]`, counts [1], record_counts [2]. `record_counts` is named nowhere on the page.

F9 MINOR / SUBSTANCE — containment paragraph contradicts itself; skipped transcription silently un-gates.
Sites: SKILL:255-258 ("the desk's transcription step skipped — and filter gates nothing new") vs SKILL:620 ("A declared scope never downgrades silently to none").
Executed: no CONTAINMENT line, --out outside the intended scope -> ARTIFACT_WRITTEN. Nothing cross-checks the preflight verdict against the record. The page also states neither when the desk transcribes nor where the lines sit (the SKILL: label gets a body-region rule; this one does not).

F10 MINOR / WORDING — budget-raise cause repair.
Site: SKILL:433-436 ("repairs on sight by appending the cause under the same id"). Under latest-line-wins a cause-only line becomes that id's resolved body, and SKILL:457-458 has every exhaustion check read "the LATEST such entry" — the same un-declare hazard SKILL:653-661 describes for write-set declarators. The repair should restate the whole raise line. Not executed: the raise line has no parser (SKILL:463-465 says body-read).

F11 MINOR / WORDING — two seam gaps in new sentences.
(a) SKILL:1804-1805: population read from closure's `post_closure`, but the Verify seam (SKILL:1779-1781) runs `sweep`, not `closure`. Field confirmed present on CLOSURE_LIVE and UNIT_DISPATCHABLE (executed), absent on ZERO_DELTA_UNCONVERGED. (b) SKILL:1105-1109: ABSENCE is appended "before the round dispatches"; the artifact is pinned at the lock sha (SKILL:1071-1073), so an ABSENCE written after the lock is not in the artifact and falsifies a tree claim. It should say before the LOCK.

The four open questions
1. `containment-near-miss: "0.2.105"` equals plugin.json's 0.2.105, so it is the right value if the release ships under that number. It is inert, though: the code is not in FORM_CODES_MINT_GATED (REC:481-482, is_retro REC:518), so sweep never grades it RETRO, and filter's hold has no version scoping at all (F5c shape in an older record holds filter).
2. Hook (outside my reporting scope; facts only). Exec bit: index mode 100755 (`git ls-files -s`). `${CLAUDE_PLUGIN_ROOT}`: the installed cache is `~/.claude/plugins/cache/statiker/statiker/<ver>/{hooks,skills}` (observed for 0.2.102/0.2.103, stop_guard there is -rwxr-xr-x), so `/hooks/statiker_postcompact.py` resolves; 0.2.105 itself is not installed, unverified for it. Live Status values: in-progress, [READY], PASSED (code; fired on a [READY] header in my probe, silent on source=startup). Subagent: a payload carrying `agent_type` gets the identical notice, the script never reads that field; it also names every live tracker under cwd to whichever session compacted. Whether the harness fires SessionStart(compact) for a subagent lane, and a real compaction, I did not exercise. The page never mentions compaction (grep: 0 hits).
3. Page (SKILL:1852-1858), register (`verify: sonnet` first) and READINESS's update_2026_10_07 agree: sonnet on a Claude harness with no clippy.config/models verify class. Two stale register comments still say haiku "carries this role" (defaults/models certification block and the opus block), and READINESS's `why` still describes the old order beside its update note.
4. Multi-location: F2, F6, F8, F9 are that class.

Not reached: tools/test_statiker_postcompact_hook.py and the record battery bodies beyond a grep for convergence arms; GIT preflight's `containment_scope` emission (page claim at SKILL:246-248 read against the diff only, not executed); references/*.md; the golden corpus; any real resume of a pre-0.2.105 tracker (by code read the convergence check has no version scoping, so an older record with pre-close `unit U<k>` D-lines, e.g. `held:`/`gap:` entries on a re-entered design, would return ZERO_DELTA_UNCONVERGED — unverified by execution on a real record).

---

(1/5) HOLD — page half of f954320..ae19e24: 1 BLOCKING, 6 MAJOR, 4 MINOR. HEAD verified ae19e24. Suite `python3 -m pytest tools/ -q -p no:cacheprovider`: 723 passed, 18 subtests passed, 0 skipped, 0 failed. Probes ran HEAD's scripts on trackers in my own scratch git repo; statiker repo untouched. SKILL = plugin/skills/statiker/SKILL.md, REC = scripts/statiker_record.py, GIT = scripts/statiker_git.py.

Verdicts added/touched, each checked at every page site: ZERO_DELTA_UNCONVERGED (SKILL:1371-1374; barred), ARTIFACT_CONTAINMENT_HOLD (SKILL:252-258, 617-620, 1080-1084; halt), SKILL_VERSION_HOLD (SKILL:300-312 vs 279-283 vs 164-171; surface), lint containment-near-miss (618-620), TREND_COMPUTED counts (98-100, 1289-1295), closure `post_closure` (1804-1805).

F1 BLOCKING / SUBSTANCE — the convergence gate is vacuous on the record shape the page produces, while this delta introduces aimed (subset) rounds.
Sites: SKILL:1362-1374 ("closure tool enforces the seam ... an aimed round's zero cannot close design"); REC cmd_closure d_units (collects only D-lines whose body OPENS `unit U<k>`).
The page never tells the desk to open a pre-close design D-line with `unit U<k>` (only F write-set lines are unit-scoped; the PRECEDENT LINE is "one clause of the unit's design D-line", no opener). Scopeless design D-lines -> d_units empty -> any [ZERO-DELTA], an aimed one included, closes design.
Executed: `- D1 [COMMITTED] design: U1 parses, U2 queries`, F write-set lines for U1/U2, `A1 [ZERO-DELTA]`, no convergence record -> `closure` = CLOSURE_LIVE proceed; `--unit U1` = UNIT_DISPATCHABLE. Control (D-lines opening `unit U1`/`unit U2`) -> ZERO_DELTA_UNCONVERGED [U1,U2]. The contract battery's CLOSED_TRACKER (tools/test_contract.py:358-368) is the scopeless shape, asserted green: no arm goes red on this.

F2 MAJOR / SUBSTANCE — a terminal [BIT] bypasses the convergence gate.
Sites: SKILL:1536-1541 ("SATISFIED, the same predicate as ZERO-DELTA from there") vs 1371-1374; REC: the check sits only in the ZERO-DELTA branch.
Executed: unit-scoped D1/D2, one scopeless substance F-line, `A1 [BIT]`, no D amendment, no convergence record -> CLOSURE_LIVE; `--unit U2` -> UNIT_DISPATCHABLE. Same record with ZERO-DELTA -> ZERO_DELTA_UNCONVERGED. An aimed round that bites without a design-amending D-line opens what its zero cannot.

---

(2/5) Page review, continued.

F3 MAJOR / SUBSTANCE — a mistyped UNCONVERGED fails OPEN and lints clean; the page states only the safe direction.
Sites: SKILL:1360-1362 ("a near-form is ordinary bookkeeping and converges nothing"), 1383-1387; REC RECORD_UNCONVERGED_RE (exactly one F id).
Executed: U1 CONVERGED at A1; round 2 with two findings; `record: unit U1 UNCONVERGED at A2 — F2, F3`; `A3 [ZERO-DELTA]` -> CLOSURE_LIVE, lint LINT_CLEAN. Control with `— F2` alone -> ZERO_DELTA_UNCONVERGED [U1]. Two findings on one unit is the ordinary case and the page gives no form for it. No near-miss class exists for the three forms.

F4 MAJOR / SUBSTANCE — ZERO_DELTA_UNCONVERGED has no stated way out, and the tool's way out is one unverified line.
Sites: SKILL:1371-1374; route `barred` (SKILL:150-154).
The tool cannot refuse a "landing": the [ZERO-DELTA] A-line is already appended when closure runs. The page never says what the desk does next (another round? which A-line?).
Executed: after the closing A-line, `- F1 [PENDING] record: unit U1 CONVERGED at A99 — basis: nothing` -> CLOSURE_LIVE. Accepted post-close, under any tag but INVALIDATED, citing a nonexistent round. An unattended desk clears the bar by assertion.
By code read only, not executed: ABSENCE counts as converged for good (`in ("converged","absence")`), and SKILL:1383 un-converges only "a converged unit", so an ABSENCE unit that draws reading-round substance findings has no page route back.

F5 MAJOR / SUBSTANCE — a `containment:`-shaped line that is not exact holds `filter` permanently; the repair sweep names does not clear it.
Sites: SKILL:617-620 ("lints `containment-near-miss` and holds `filter`"), 252-258, 1080-1084; REC CONTAINMENT_EXACT_RE `^CONTAINMENT: (\S+)$`, cmd_filter's malformed check over raw pinned lines.
Executed:
(a) `CONTAINMENT:  <path>` (two spaces): SWEEP_HOLDS, repair "record: corrects line 9". After that line plus a correct label: sweep SWEEP_CLEAN, filter still ARTIFACT_CONTAINMENT_HOLD (malformed_containment lists line 9). Append-only keeps the line forever, so no attack artifact for the rest of the run.
(b) A declared path containing a space, transcribed exactly -> ARTIFACT_CONTAINMENT_HOLD, containment_scope []. No legal form exists for such a path.
(c) Head-region prose `Containment: keep everything under ...` (INTENT is verbatim operator text): `lint` LINT_CLEAN, filter ARTIFACT_CONTAINMENT_HOLD. The page says it lints; in the head region it does not, and nothing in sweep points at the cause.
Controls: exact label + inside --out -> ARTIFACT_WRITTEN; outside -> hold. Route is `halt`; the attack seam states no unattended close rule for a filter halt.

---

(3/5) Page review, continued.

F6 MAJOR / SUBSTANCE — SKILL_VERSION_HOLD's route token contradicts its page disposition.
Sites: SKILL:279-283 (older desk "appends nothing", "WRITES NO CLOSE", "the surfacing is the desk's reply, not a record write", run "stays in-progress"); SKILL:306-309 ("mechanizing the WRITES-NO-CLOSE sentence"); statiker_emit.py ROUTES `SKILL_VERSION_HOLD: surface`; SKILL:164-171 (surface "carries halt's booking obligation ... unattended the run takes the seam's terminal disposition (FAILED / rides the close)").
Executed: `STATIKER_SERVED_VERSION=0.2.103` + `sweep` and `closure` on a 0.2.105 header -> `{"verdict":"SKILL_VERSION_HOLD","route":"surface","header_version":"0.2.105","served_version":"0.2.103"}`. A desk reading the token books an F-line and closes FAILED: the two writes the passage forbids. SKILL:121-126 promises a token-only desk is never unsafe; no sentence at the seam overrides the token.

F7 MAJOR / SUBSTANCE — under SKILL_VERSION_HOLD the lock gate fails OPEN, so a lock and the Close pin proceed.
Sites: SKILL:306-309; GIT lock_gate_check (keys on the sweep verdict's `violations`, which SKILL_VERSION_HOLD does not carry).
Executed: tracker with a latest-line [PENDING]: `lock-check` -> LOCK_GATE_HOLDS; same call with STATIKER_SERVED_VERSION=0.2.103 -> LOCK_CHECK_CLEAN route proceed. The hold removes the gate it claims to mechanize. The unit side is closed: `unit-start` -> UNIT_GATE_BLOCKED embedding the hold. Only sweep and closure carry the check: lint, trend, sustain, tripwire, waves, filter all proceeded (executed; matches the page's "sweep and closure each"). Reachable only from the release AFTER this one, since an older tool lacks the check.

F8 MINOR / SUBSTANCE — page and tool disagree on what `trend` counts.
Sites: SKILL:98-100 ("every F-line in a round's span") and SKILL:1290-1295 ("read every F-line regardless of class ... the counts half stays class-blind") — both unchanged; REC trend_over_rounds now excludes `record:`-scoped F-lines.
Executed: a round with 1 finding + 2 record-scoped F-lines -> `findings [1 (+2 record)]`, counts [1], record_counts [2]. `record_counts` is named nowhere on the page.

---

(4/5) Page review, continued.

F9 MINOR / SUBSTANCE — the containment paragraph contradicts itself; a skipped transcription silently un-gates.
Sites: SKILL:255-258 ("the desk's transcription step skipped — and `filter` gates nothing new") vs SKILL:620 ("A declared scope never downgrades silently to none").
Executed: no CONTAINMENT line, --out outside the intended scope -> ARTIFACT_WRITTEN. Nothing cross-checks the preflight verdict against the record. The page also states neither WHEN the desk transcribes nor WHERE the lines sit (the SKILL: label has a body-region rule at SKILL:292-295; this label has none).

F10 MINOR / WORDING — budget-raise cause repair.
Site: SKILL:433-436 ("repairs on sight by appending the cause under the same id"). Under latest-line-wins a cause-only line becomes that id's resolved body, while SKILL:457-458 has every exhaustion check read "the LATEST such entry" — the un-declare hazard SKILL:653-661 describes for write-set declarators. The repair should restate the whole raise line. Not executed: the raise line has no parser (SKILL:463-465 says body-read).

F11 MINOR / WORDING — two seam gaps in new sentences.
(a) SKILL:1804-1805: the population is read from closure's `post_closure`, but the Verify seam (SKILL:1779-1781) runs `sweep`, not `closure`. Field confirmed present on CLOSURE_LIVE and UNIT_DISPATCHABLE (executed), absent on ZERO_DELTA_UNCONVERGED.
(b) SKILL:1105-1109: ABSENCE is appended "before the round dispatches". The artifact is pinned at the lock sha (SKILL:1071-1073), so an ABSENCE written after the lock is missing from the artifact and falsifies a tree claim. It should say before the LOCK. Read only, not executed.

Checked and consistent with the tool (executed): the defang ownership split, SKILL:644-651. Entry-owned line: a bare `record: corrects line 9` under the SAME id -> SWEEP_CLEAN (under another id -> corrects-nothing). INTENT line: bare token -> still SWEEP_HOLDS; token carrying the defanged literal -> SWEEP_CLEAN.

---

(5/5) Page review: the four open questions, and what I did not reach.

Q1. `containment-near-miss: "0.2.105"` equals plugin.json's 0.2.105, so it is right if the release ships under that number. It is inert: the code is not in FORM_CODES_MINT_GATED (REC:481-482; is_retro returns False at REC:518), so sweep never grades it RETRO, and filter's hold has no version scoping at all — an F5(c)-shaped line in an older record holds filter.

Q2. Hook (outside my reporting scope; facts only).
- Exec bit: index mode 100755 (`git ls-files -s plugin/hooks`).
- `${CLAUDE_PLUGIN_ROOT}`: the installed cache is `~/.claude/plugins/cache/statiker/statiker/<ver>/{hooks,skills}` (observed for 0.2.102 and 0.2.103; stop_guard there is -rwxr-xr-x), so `/hooks/statiker_postcompact.py` resolves. 0.2.105 is not installed: unverified for it.
- Live Status values: in-progress, [READY], PASSED (code read; fired on a [READY] header, silent on source=startup, both executed).
- Subagent: a payload carrying `agent_type` gets the identical notice (executed); the script never reads that field, and it names every live tracker under cwd to whichever session compacted. Whether the harness fires SessionStart(compact) for a subagent lane, and a real compaction: not exercised.
- The page never mentions compaction (grep "compact": 0 hits).

Q3. Page (SKILL:1852-1858), register (`verify: sonnet` first) and READINESS's update_2026_10_07 agree: sonnet on a Claude harness with no clippy.config/models verify class. Two stale register comments still say haiku "carries this role" (defaults/models, the certification block and the opus block), and READINESS's `why` still describes the old order beside its update note.

Q4. Multi-location instruction: F2, F6, F8, F9 are that class.

Not reached:
- tools/test_statiker_postcompact_hook.py, and the record battery beyond a grep for convergence arms (no arm found for F1, F2, F3's two-id form, F5's repair route, or F7).
- GIT preflight's `containment_scope` emission: SKILL:246-248 read against the diff only, not executed.
- references/*.md and the golden corpus.
- A resume of a real pre-0.2.105 tracker. By code read the convergence check has no version scoping, so an older record with pre-close `unit U<k>` D-lines (a `held:` or `gap:` entry on a re-entered design) would return ZERO_DELTA_UNCONVERGED on its next closing round — inferred, unverified on a real record.

End of report.

---


## sonnet-repair-0205

Grounding return (base 0bb6fd6 clean, HEAD == base, tree clean bar the lock file). Continuing without waiting.
Unopened/wrong Background lines: none wrong. Opened: record.py :232-253, :340-344, :381-406, :1328, :2205-2224, :2318-2354 (terminal-BIT satisfied branch is the say() at :2318, else-branch :2320), :3160-3168; git.py :977-981; hook file. Cache-path layout (C4) still to be opened before I touch that sentence.
Contradictions / judgment points (I resolve as stated, flagged again in the report):
1. B3 says register the new code in FORM_CODES_MINT_GATED "on the tripwire-arm-near-miss precedent", but that precedent is NOT in FORM_CODES_MINT_GATED (record.py:481-482 holds four other codes). I follow the explicit instruction (add convergence-near-miss, and containment-near-miss per A3).
2. A2 says "as sweep would grade it", but sweep also nets SWEEP_EXEMPT declarations; brief names only shed + RETRO. I reuse parse_tracker + net_retro_holds and do NOT net exemptions (fail-closed for a filesystem write).
3. B3 "not a record that counts" would also lint a [PENDING] line later restated [VERIFIED] under the same id, and an [INVALIDATED] one. I lint only the id's latest line, and skip [INVALIDATED], mirroring unit_convergence_states.
Golden corpus = tools/golden-corpus/tracker.md + expected-violations.json; lock arms live in tools/test_statiker_git.py.

---

Closing report, composed against HEAD b65d673 (base 0bb6fd6).
(a) Done A, B, C, D as designed. Commits (unpushed, my trailer): f1bebcc = A+B+C, b65d673 = D.
(b) Red first, per arm file, against unchanged scripts: record 18 failed/14 passed (-k new arms); git+hook 7 failed/3 passed. Baselines: full suite 723 passed, 0 skipped. Green: `python3 -m pytest /home/g/dev/Gunther-Schulz/statiker/tools/ -q -p no:cacheprovider` -> 748 passed, 22 subtests passed, 0 skipped (cwd = repo). register_lint on SKILL.md: 0 findings (26.1 em/1000w, 45.0 w/s), exit 0.
(c) Gaps: none needing a higher tier.
(d) Deviations:
1. ONE commit for A+B+C, not three: they share hunks in statiker_record.py/test_statiker_record.py; hunk staging is interactive (forbidden). D separate.
2. Existing tests changed because the designed behaviour moves them: TestSt89 (SLIPS: `CONTAINMENT: /x /y` is now a legal spaced path, replaced by the doubled-space slip; fixture header stamped 0.2.105 since the code is now mint-gated and a 0.2.33 stamp grades RETRO, which filter ignores); TestSt85RecordGrammar unconverged tuple is now ("A5", ["F7"]); three skill_versions equality pins gain "header": True; hook test window 15 -> 20 filler lines.
3. Golden tracker.md header Skill 0.2.87 -> 0.2.105 (else containment-near-miss grades RETRO and vanishes from the golden set); new block + row convergence-near-miss; freeze-breach row 135 -> 139.
4. Judgment calls: convergence-near-miss skips only [INVALIDATED] F-lines (no latest-per-id rule: it would make the corrects-token repair unreachable); filter nets RETRO only, not SWEEP_EXEMPT (fail-closed); C4 layout established with `find` (Glob unavailable): installed 0.2.103 holds skills/statiker/scripts/statiker_record.py, no plugin/ segment; docstring corrected.
5. Two no-op heredoc commands (`python3 -` with empty stdin) ran against the plumbing rule; no output, no file effect.
(e) Lesson candidate: brief's "one commit per item" collides with shared files; assign commits per file set or allow one grouped commit.
(f) Touched: statiker_record.py, statiker_git.py, statiker_emit.py, statiker_postcompact.py, test_statiker_record.py, test_statiker_git.py, test_statiker_postcompact_hook.py, golden-corpus/tracker.md + expected-violations.json. test_contract.py needed no edit (its derivations pass). Writer-reservation hook warned (holder: main session); git status before commit showed only my paths.
(g) Not verified: page text vs behaviour beyond the lint; live hook in a real compaction; D2 under a git worktree cwd.
(h) Read: brief, executor skill, record.py (regions above), git.py gate, emit ROUTES, hook, the three test files, test_contract.py (battery, repair/mint coverage), golden corpus.

---


## opus-review-m2

Machine-side review of b65d673 (part 1/2): HOLD — 1 BLOCKING, 4 MAJOR, 9 MINOR. All BLOCKING/MAJOR findings are executed.

Object graded: HEAD b65d673 at start and at end of the review. Suite run by me: `python3 -m pytest tools/ -q -p no:cacheprovider` -> 748 passed, 22 subtests passed, 0 skipped, 0 failed (93s). Probes ran from my scratchpad against scratch git repos; nothing written to the repo. Note: `git status` at the end shows ` M dev-notes/OBSERVATIONS.md` — another writer, not me; outside my scope and unread.

Short paths: REC = plugin/skills/statiker/scripts/statiker_record.py, GIT = .../statiker_git.py, EMIT = .../statiker_emit.py, PAGE = plugin/skills/statiker/SKILL.md, TREC = tools/test_statiker_record.py.

Verdicts and lint codes this delta adds or touches, each checked against every page location and its route:
- ZERO_DELTA_UNCONVERGED (barred, EMIT:144) — PAGE:323-324 (resume gate), PAGE:1390-1399 (The attack). Token and both seams agree. Predicate narrower than the page's gloss: M2, M3, M4.
- ARTIFACT_CONTAINMENT_HOLD (halt, EMIT:164) — PAGE:254-260, 623-632, 1092-1096. Token consistent at all three; consequence wrong at 628-630: M1.
- SKILL_VERSION_HOLD (barred, EMIT:170) — PAGE:303-317. Consistent at its one location; embedded in LOCK_GATE_HOLDS it meets a second disposition: N1.
- containment-near-miss, convergence-near-miss — PAGE:625-630, 1375-1377; both missing from the page's FORM-code list at PAGE:880-881: N2.
- New fields containment_scope, post_closure, absence_units, record_counts: page and tool agree (PAGE:248-250, 1833-1837, 98-101).

---

B1 — BLOCKING, SUBSTANCE. The repair the tool prescribes for `convergence-near-miss` cannot be followed: each literal attempt mints a new hold.
Sites: REC:232-242 (exact forms anchored `$`), REC:798-802 (code in MACHINE_TOKEN_CODES -> REPAIR_SUPERSEDE, REC:677-679), REC:1466-1471 (lint), PAGE:647-649 ("the desk composes repairs from the verdict, never from memory"), PAGE:1375-1377.
What happens: the verdict says "supersede-whole: restate under the same id with `corrects line 15`; tag and scope re-carried". A restated CONVERGED/UNCONVERGED line that carries the token no longer matches the exact form, so it is itself a near-miss and does not count. The hold moves one line down on every attempt. Sweep-gated seams (re-lock via LOCK_GATE_HOLDS, the Verify dispatch) stay shut; unattended, that ends as holds riding a FAILED close.
Probe (probe1.py P1), near-miss `- F2 [VERIFIED] record: unit U2 CONVERGED A1` at line 15:
- restate + token (`... CONVERGED at A1 corrects line 15`): sweep SWEEP_HOLDS convergence-near-miss @16, repair now says `corrects line 16`; closure ZERO_DELTA_UNCONVERGED ["U2"].
- restate + `(corrects line 15)`: identical result.
- fresh exact line, no token: closure CLOSURE_LIVE, but sweep still holds on line 15 forever.
- token-only supersede (`- F2 [VERIFIED] record: corrects line 15`) followed by a separate exact line: SWEEP_CLEAN, CLOSURE_LIVE. This is the only working route, and neither the verdict nor the page states it.
- Tag variant: a `[PENDING]` convergence line repaired by a `[VERIFIED]` supersede draws `repair-tag-change`; it clears only by re-carrying `[PENDING]` on the token-only line, then a fresh `[VERIFIED]` exact line.
Sibling, not from this delta: `tripwire-arm-near-miss` has the same regress (P8: restatement with `(corrects line 10)` -> SWEEP_HOLDS tripwire-arm-near-miss @10). Convergence records are written per unit per round, so this is the frequent one.
Battery: no arm repairs a convergence-near-miss; TREC `test_hyphen_form_lints_and_sweep_holds` stops at "it lints". Its bad line also cites a non-existent A2, so the red is not attributable to the hyphen alone (the golden row at tools/golden-corpus/tracker.md:131 is).

M1 — MAJOR, SUBSTANCE, fail-open. Following the prescribed repair for a malformed containment label leaves the containment gate unarmed with every gate green.
Sites: REC:803-807 (code in BODY_CONTENT_CODES -> REPAIR_BOOKKEEPING), REC:3232-3252, PAGE:628-630 ("the lint's own correcting entry clears both. A malformed label never downgrades silently to none").
What happens: the verdict prescribes a shed-only bookkeeping line. After it, the near-miss is gone, no exact label exists, and `filter` writes anywhere outside every repo.
Probe (probe2.py P4): tracker with `Containment: <scope>` only.
- before repair: filter ARTIFACT_CONTAINMENT_HOLD, malformed_containment listed.
- after `- F2 [VERIFIED] record: corrects line 9 — basis: the containment-near-miss verdict at line 9`: sweep SWEEP_CLEAN; filter with --out outside the named scope -> ARTIFACT_WRITTEN, file exists.
- control, exact label also present: ARTIFACT_CONTAINMENT_HOLD "--out lands outside the run's declared containment scope".
Battery: TREC `test_corrected_mistyped_label_plus_correct_one_writes` covers only the case where a correct label is also present; no arm for corrected-and-no-label.

M2 — MAJOR, SUBSTANCE, fail-open. A malformed UNCONVERGED record does not bar closure; the unit stays converged and dispatchable.
Sites: REC:2208-2210 (CLOSURE_BLOCKING_CODES lacks convergence-near-miss), REC:2250-2271, comment at REC:237-240 ("a convergence record the closure guard would silently not read"), PAGE:1375-1377.
What happens: the lint holds `sweep` only. The seam between a round's return and unit dispatch runs `closure` (PAGE:1524-1527; unit-start consults closure, GIT:1079). On the terminal-[BIT] path there is no re-lock, so no sweep runs before units build.
Probe (P2): U1, U2 CONVERGED at A1; round A2 books `record: unit U2 UNCONVERGED at A2 - F3` (hyphen); A2 [BIT] amending no D-line.
- closure: CLOSURE_LIVE; closure --unit U2: UNIT_DISPATCHABLE; sweep: SWEEP_HOLDS (never consulted at this seam).
- control with the em dash: ZERO_DELTA_UNCONVERGED ["U2"] on both.
Scope: a malformed CONVERGED or ABSENCE fails safe; only UNCONVERGED fails open, and a re-lock after the round would catch it through sweep.

M3 — MAJOR, SUBSTANCE, fail-open. The guard's population omits units the record declares by write-set; a unit with no convergence record at all dispatches.
Sites: REC:2274-2301 (population = pre-close unit-scoped D-lines plus units with a counting record), PAGE:1393-1400, PAGE:1628-1633 (every unit has a `unit U<k> write-set:` F-line at [READY]; unit-start refuses without one).
Probe (P3): scopeless design D-line, write-set F-lines for U1 and U2, round aimed at U1, only U1 CONVERGED, A1 [ZERO-DELTA].
- closure: CLOSURE_LIVE; closure --unit U2: UNIT_DISPATCHABLE; sweep SWEEP_CLEAN.
- control, a unit-scoped D-line for U2: ZERO_DELTA_UNCONVERGED ["U2"].
The page admits "a unit no entry names is invisible", but U2 is named — by the entry the unit gate itself requires. Nothing on the page tells a desk to open design D-lines with `unit U<k>`. Battery: TREC `test_scopeless_d_line_no_units_to_check` pins this as intended.

M4 — MAJOR, SUBSTANCE, page sentence the tool does not honour. "An aimed round's zero cannot close design" (PAGE:1395) is false once every unit carries a record.
Sites: PAGE:1381-1383 ("the closing zero-delta round runs once over the converged set"), PAGE:1390-1395, REC:2404-2411.
Probe (P3b): A1 [BIT] with U1 CONVERGED, U2 UNCONVERGED; A2 aimed at U2 only, U2 CONVERGED at A2, A2 [ZERO-DELTA] -> CLOSURE_LIVE, U1 UNIT_DISPATCHABLE.
This is the ordinary second round of a multi-unit run. The tool cannot see a round's aim, so the whole-design closing round is enforced by nothing; the page states the predicate correctly and then glosses it wider than it reaches.

Part 2 carries the MINOR findings, battery gaps, and what I did not reach.

---

Machine-side review of b65d673 (part 2/2): the 9 MINOR findings, what held, and what I did not reach. Verdict stays HOLD (part 1).

Paths as in part 1: REC, GIT, EMIT, PAGE, TREC.

N1 — MINOR, SUBSTANCE. A version hold reaching the desk through the git tool carries an outer route that contradicts "nothing is booked / writes no close".
Sites: GIT:983-984, EMIT:64 (LOCK_GATE_HOLDS repair-from-verdict), EMIT:101 (UNIT_GATE_BLOCKED halt), PAGE:186-189 (outer route governs), PAGE:1007-1013 (unrepairable hold "rides the close instead — FAILED"), PAGE:311-314.
Probe (P6b, tool copied to an install-shaped `.../0.2.104/skills/statiker/scripts/` path, header 0.2.105): lock-check -> LOCK_GATE_HOLDS route repair-from-verdict, gate SKILL_VERSION_HOLD/barred; unit-start -> UNIT_GATE_BLOCKED route halt (halt obliges booking a `record:` F-line plus a hold entry).
Mitigation: the resume runs `sweep` first and gets the barred verdict directly.

N2 — MINOR, WORDING/RECORD. PAGE:880-881 lists four FORM codes as retro-netted and says every other code grades every line; the tool nets six (REC:513-515 adds containment-near-miss and convergence-near-miss). Executed consequence, pinned by TREC `test_retro_graded_near_miss_never_holds`: under an older header a malformed containment label neither holds sweep nor filter. No battery ties the page's list to the set.

N3 — MINOR, SUBSTANCE. A CONVERGED record citing a [VOID] round counts (REC:1466, 2262: `a_ids` is any A-id, any tag). Probe P5a: U1 `CONVERGED at A1`, A1 [VOID], A2 [ZERO-DELTA] -> CLOSURE_LIVE, SWEEP_CLEAN. PAGE:1376 says "names a round in the record"; a void round is no round (PAGE:692-693).

N4 — MINOR, SUBSTANCE. ABSENCE is accepted at any time and overrides a standing UNCONVERGED. Probe P5b: UNCONVERGED at A1, then `ABSENCE — <any reason>` -> CLOSURE_LIVE, absence_units ["U2"]. PAGE:1117-1120 requires it before the lock commit; the tool cannot check that. It does surface in absence_units for Verify.

N5 — MINOR, SUBSTANCE. A record closed under the old rules is barred whole on re-read: the guard is not version-gated. Probe P11 (header 0.2.101, pre-close `unit U1` D-line, A1 [ZERO-DELTA]): closure --unit U1 -> ZERO_DELTA_UNCONVERGED. Way out exists (write the CONVERGED record), but an in-flight older run resumed on this version stops at every unit until the desk writes them.

N6 — MINOR, SUBSTANCE. Containment scope is whatever exact labels the record carries; the tool never ties them to preflight.
- Probe P4f: a second `CONTAINMENT: <wider path>` line -> ARTIFACT_WRITTEN outside the first scope, SWEEP_CLEAN. PAGE:235 says widening is the operator's.
- Probe P4e: an exact label in the head region is invisible to lint but armed for filter (REC:3082-3093 reads raw lines) — fail-closed, but two readers of one label disagree.
- An exact-form label with a wrong path has no retraction route (no violation, so `corrects line` is corrects-nothing). Read, not executed.

N7 — MINOR, SUBSTANCE. A malformed-label hold at `filter` clears only after a re-lock, which PAGE:628-629 does not say. Probe P4d: correcting entry in the working tree, same pin -> still ARTIFACT_CONTAINMENT_HOLD. Reachable only where the near-miss was SWEEP_EXEMPT'd into a lock (P4g: sweep SWEEP_CLEAN with exempt_holds, filter holds), since an unexempted near-miss stops the lock first.

N8 — MINOR, battery gaps on the version hold (behaviour verified by my probe P6, so no defect found):
- Every arm sets STATIKER_SERVED_VERSION; no arm exercises the install-path derivation (REC:382-401), the only production path. P6: path-derived 0.2.104 over header 0.2.105 -> SKILL_VERSION_HOLD on sweep, closure, closure --unit.
- No arm drives the closure-side call (REC:2313-2315); all arms use sweep or lock-check.
- The env override beats the install path in production too (P6: override 9.9.9 -> SWEEP_CLEAN). An unparseable header version (`0.2.105-rc1`, `v0.2.105`) holds nothing, as PAGE:314-317 states.
- tools/test_contract.py `test_dangling_page_pointer_is_caught`: its first assertion computes its expectation from the same condition it tests, so it is green either way.

N9 — MINOR, SUBSTANCE. The compaction hook fires in any session whose repo root carries a live tracker, attack worktrees included. Probe P10b: a detached worktree of the run repo -> the notice is emitted, naming the sweep/closure gate. PAGE:193-195 says no attack brief ever cites the record tool; the notice's last sentence ("A dispatched lane ignores this notice") is the only guard. Whether the harness runs SessionStart(compact) hooks for a subagent is inferred, unverified.

Read-only observation, not counted: GIT:985-988 reads any sweep verdict lacking `violations` as a clean gate. The delta fixed that by name for SKILL_VERSION_HOLD only; a sweep ending in INTERNAL_ERROR or TRACKER_UNREADABLE would pass the lock gate the same way. I could not induce one, so this is unexecuted.

What held under probe:
- Version hold end to end from an install-shaped path; lock-commit side per the new git arms.
- `corrects-nothing` template formatting on unreachable targets (P7: header and INTENT targets, no crash, no leaked placeholder).
- sustain over a [BIT] round holding only convergence records -> SUSTAIN_DENIED, record_class []; trend counts [0], record_counts [2].
- Hook: fires on a live header, on a CRLF header, from the repo root; file mode 100755 in git; the four changed JSON files parse.
- defaults/models verify order (sonnet, haiku, opus) matches PAGE:1882-1885.

Not reached:
- The f954320..0bb6fd6 part of TREC outside the classes I read (TestSt85*, TestSt80, TestSt89, TestSt84, and the whole 0bb6fd6..b65d673 diff line by line); roughly 300 added lines of earlier arms unread.
- tools/test_statiker_postcompact_hook.py beyond its 0bb6fd6..b65d673 diff.
- A real compaction firing the hook in a live session, and a real plugin-cache install (I simulated the path layout by copying the scripts).
- defaults/models beyond the diff hunks; plugin/hooks/statiker_stop_guard.py beyond its docstring diff (it is unregistered).
- The lock-gate observation above, and the wrong-path-label case in N6.

Smallest changes that would lift the HOLD, as I read the code (not executed):
1. B1: let the three convergence forms carry a trailing `(corrects line <n>)` the way the write-set declarator does, or give the code its own repair text naming the two-line route.
2. M1: make the containment-near-miss repair text require the exact label alongside the shed, or keep filter holding until an exact label exists.
3. M2: add convergence-near-miss to CLOSURE_BLOCKING_CODES.
4. M3: add write-set-declared units to the guard's population.
5. M4: a page edit — drop or narrow the "an aimed round's zero cannot close design" gloss.

Probe scripts: /tmp/claude-1000/-home-g-dev-Gunther-Schulz-statiker/7196f402-db3b-4933-bcaa-2e10d71d56b0/scratchpad/mrev/probe1.py and probe2.py (with lib.py).

---

Machine-side review of b65d673 (1/7): HOLD — 1 BLOCKING, 4 MAJOR, 9 MINOR; every BLOCKING/MAJOR is executed.

Object: HEAD b65d673 at start and end. Suite, run by me: 748 passed, 22 subtests passed, 0 skipped, 0 failed (93s, -p no:cacheprovider). Probes ran from my scratchpad on scratch git repos; no repo writes. `git status` at the end shows ` M dev-notes/OBSERVATIONS.md` — another writer, unread by me.

Paths: REC = plugin/skills/statiker/scripts/statiker_record.py, GIT = .../statiker_git.py, EMIT = .../statiker_emit.py, PAGE = plugin/skills/statiker/SKILL.md, TREC = tools/test_statiker_record.py.

Tokens this delta adds or touches, checked at every page location and route:
- ZERO_DELTA_UNCONVERGED (barred, EMIT:144): PAGE:323-324 and 1390-1399 agree with the token. Predicate narrower than the page gloss: M2, M3, M4.
- ARTIFACT_CONTAINMENT_HOLD (halt, EMIT:164): PAGE:254-260, 623-632, 1092-1096 agree on the token. Consequence at 628-630 is wrong: M1.
- SKILL_VERSION_HOLD (barred, EMIT:170): PAGE:303-317 agrees. Embedded in a git-tool verdict it meets another disposition: N1.
- containment-near-miss, convergence-near-miss: PAGE:625-630, 1375-1377; absent from the FORM-code list at PAGE:880-881: N2.
- Fields containment_scope, post_closure, absence_units, record_counts: page and tool agree.

Findings by part: 2 = B1; 3 = M1, M2; 4 = M3, M4; 5 = N1-N5; 6 = N6-N9; 7 = what held, not reached, smallest fixes.

---

Machine-side review (2/7): B1, the one BLOCKING finding — the repair the tool prescribes for `convergence-near-miss` cannot be followed.

B1 — BLOCKING, SUBSTANCE.
Sites: REC:232-242 (exact forms anchored `$`), REC:798-802 (code in MACHINE_TOKEN_CODES, so REPAIR_SUPERSEDE at REC:677-679), REC:1466-1471 (the lint), PAGE:647-649 ("the desk composes repairs from the verdict, never from memory"), PAGE:1375-1377.

What a desk meets: the verdict says "supersede-whole: restate under the same id with `corrects line 15`". A restated CONVERGED or UNCONVERGED line carrying the token no longer matches the exact form, so it is a new near-miss and does not count. The hold moves one line down per attempt. Sweep-gated seams (re-lock, Verify dispatch) stay shut; unattended that ends as holds riding a FAILED close.

Probe (probe1.py P1), near-miss `- F2 [VERIFIED] record: unit U2 CONVERGED A1` at line 15:
- restate + `corrects line 15`: SWEEP_HOLDS convergence-near-miss @16, repair text now says line 16; closure ZERO_DELTA_UNCONVERGED ["U2"].
- restate + `(corrects line 15)`: same result.
- fresh exact line, no token: closure CLOSURE_LIVE, sweep holds on line 15 forever.
- token-only line (`- F2 [VERIFIED] record: corrects line 15`) then a separate exact line: SWEEP_CLEAN, CLOSURE_LIVE. The only working route; neither verdict nor page states it.
- A `[PENDING]` convergence line repaired by a `[VERIFIED]` supersede draws `repair-tag-change`; it clears only by re-carrying `[PENDING]` on the token-only line, then a fresh `[VERIFIED]` exact line.

Sibling, older than this delta: `tripwire-arm-near-miss` regresses the same way (P8: SWEEP_HOLDS @10 after the literal restatement). Convergence records are written per unit per round, so this one is the frequent case.

Battery: no arm repairs a convergence-near-miss. TREC `test_hyphen_form_lints_and_sweep_holds` stops at "it lints", and its bad line also cites a non-existent A2, so its red is not attributable to the hyphen (the golden row at tools/golden-corpus/tracker.md:131 is).

---

Machine-side review (3/7): M1 and M2, two executed fail-opens in the new gates.

M1 — MAJOR, SUBSTANCE. Following the prescribed repair for a malformed containment label leaves the containment gate unarmed with every gate green.
Sites: REC:803-807 (code in BODY_CONTENT_CODES, so the shed-only REPAIR_BOOKKEEPING), REC:3232-3252, PAGE:628-630 ("the lint's own correcting entry clears both. A malformed label never downgrades silently to none").
Probe (probe2.py P4), tracker carrying only `Containment: <scope>`:
- before repair: filter ARTIFACT_CONTAINMENT_HOLD, malformed_containment listed.
- after the verdict's own line `- F2 [VERIFIED] record: corrects line 9 — basis: the containment-near-miss verdict at line 9`: sweep SWEEP_CLEAN; filter with --out outside the named scope gives ARTIFACT_WRITTEN and the file exists.
- control, exact label also present: ARTIFACT_CONTAINMENT_HOLD, "--out lands outside the run's declared containment scope".
Battery: TREC `test_corrected_mistyped_label_plus_correct_one_writes` covers only the case with a correct label beside it; no arm for corrected-and-no-label.

M2 — MAJOR, SUBSTANCE. A malformed UNCONVERGED record does not bar closure; the unit stays converged and dispatchable.
Sites: REC:2208-2210 (CLOSURE_BLOCKING_CODES lacks convergence-near-miss), REC:2250-2271, the comment at REC:237-240 ("a convergence record the closure guard would silently not read"), PAGE:1375-1377.
Mechanism: the lint holds `sweep` only, while the seam between a round's return and unit dispatch runs `closure` (PAGE:1524-1527; unit-start consults closure, GIT:1079). On the terminal-[BIT] path there is no re-lock, so no sweep runs before units build.
Probe (P2): U1 and U2 CONVERGED at A1; round A2 books `record: unit U2 UNCONVERGED at A2 - F3` (hyphen); A2 [BIT] amends no D-line.
- closure: CLOSURE_LIVE. closure --unit U2: UNIT_DISPATCHABLE. sweep: SWEEP_HOLDS, never consulted at this seam.
- control with the em dash: ZERO_DELTA_UNCONVERGED ["U2"] on both calls.
Scope: a malformed CONVERGED or ABSENCE fails safe; only UNCONVERGED fails open, and a re-lock after the round would catch it through sweep.

---

Machine-side review (4/7): M3 and M4, both about how far the per-unit convergence guard reaches.

M3 — MAJOR, SUBSTANCE, fail-open. The guard's population omits units the record declares by write-set, so a unit with no convergence record at all dispatches.
Sites: REC:2274-2301 (population = pre-close unit-scoped D-lines plus units carrying a counting record), PAGE:1393-1400, PAGE:1628-1633 (every unit has a `unit U<k> write-set:` F-line at [READY]; unit-start refuses without one).
Probe (probe1.py P3): scopeless design D-line, write-set F-lines for U1 and U2, round aimed at U1, only U1 CONVERGED, A1 [ZERO-DELTA].
- closure: CLOSURE_LIVE. closure --unit U2: UNIT_DISPATCHABLE. sweep: SWEEP_CLEAN.
- control, a unit-scoped D-line for U2: ZERO_DELTA_UNCONVERGED ["U2"].
The page concedes "a unit no entry names is invisible", but U2 is named, by the entry the unit gate itself requires. Nothing on the page tells a desk to open design D-lines with `unit U<k>`. Battery: TREC `test_scopeless_d_line_no_units_to_check` pins the silent case as intended.

M4 — MAJOR, SUBSTANCE, a page sentence the tool does not honour. "An aimed round's zero cannot close design" (PAGE:1395) is false once every unit carries a record.
Sites: PAGE:1381-1383 ("the closing zero-delta round runs once over the converged set"), PAGE:1390-1395, REC:2404-2411.
Probe (P3b): A1 [BIT] with U1 CONVERGED and U2 UNCONVERGED; A2 aimed at U2 only, U2 CONVERGED at A2, A2 [ZERO-DELTA]. Result: CLOSURE_LIVE, U1 UNIT_DISPATCHABLE.
This is the ordinary second round of a multi-unit run. The tool cannot see a round's aim, so nothing enforces the whole-design closing round; the page states the predicate correctly and then glosses it wider than it reaches. The battery's own control (`CONV1 + CONV2 + BIT` gives CLOSURE_LIVE) pins the behaviour.

---

Machine-side review (5/7): MINOR findings N1-N5.

N1 — MINOR, SUBSTANCE. A version hold reaching the desk through the git tool carries an outer route that contradicts "nothing is booked / writes no close".
Sites: GIT:983-984, EMIT:64, EMIT:101, PAGE:186-189 (outer route governs), PAGE:1007-1013 (an unrepairable hold "rides the close instead — FAILED"), PAGE:311-314.
Probe (probe2.py P6b, tool copied to an install-shaped `.../0.2.104/skills/statiker/scripts/` path, header 0.2.105): lock-check gives LOCK_GATE_HOLDS, route repair-from-verdict, gate SKILL_VERSION_HOLD/barred; unit-start gives UNIT_GATE_BLOCKED, route halt, which obliges a booked F-line and a hold entry.
Mitigation: the resume runs `sweep` first and gets the barred verdict directly.

N2 — MINOR, WORDING/RECORD. PAGE:880-881 lists four retro-netted FORM codes and says every other code grades every line; the tool nets six (REC:513-515). Consequence, pinned by TREC `test_retro_graded_near_miss_never_holds`: under an older header a malformed containment label holds neither sweep nor filter. No battery ties the page list to the set.

N3 — MINOR, SUBSTANCE. A CONVERGED record citing a [VOID] round counts (REC:1466, 2262: any A-id, any tag). Probe P5a: U1 `CONVERGED at A1`, A1 [VOID], A2 [ZERO-DELTA] gives CLOSURE_LIVE, SWEEP_CLEAN. PAGE:1376 says "names a round in the record"; PAGE:692-693 says a void round is none.

N4 — MINOR, SUBSTANCE. ABSENCE is accepted at any time and overrides a standing UNCONVERGED. Probe P5b: UNCONVERGED at A1, then `ABSENCE — <any reason>` gives CLOSURE_LIVE, absence_units ["U2"]. PAGE:1117-1120 requires it before the lock commit; the tool cannot check that. It does surface in absence_units for Verify.

N5 — MINOR, SUBSTANCE. A record closed under the old rules is barred whole on re-read; the guard is not version-gated. Probe P11 (header 0.2.101, pre-close `unit U1` D-line, A1 [ZERO-DELTA]): closure --unit U1 gives ZERO_DELTA_UNCONVERGED. The way out exists (write the CONVERGED record), but an in-flight older run resumed here stops at every unit until the desk writes them.

---

Machine-side review (6/7): MINOR findings N6-N9.

N6 — MINOR, SUBSTANCE. The containment scope is whatever exact labels the record carries; the tool never ties them to preflight.
- Probe P4f: a second `CONTAINMENT: <wider path>` line gives ARTIFACT_WRITTEN outside the first scope, SWEEP_CLEAN. PAGE:235 says widening is the operator's.
- Probe P4e: an exact label in the head region is invisible to lint but armed for filter (REC:3082-3093 reads raw lines). Fail-closed, but two readers of one label disagree.
- An exact-form label with a wrong path has no retraction route (no violation, so a `corrects line` is corrects-nothing). Read, not executed.

N7 — MINOR, SUBSTANCE. A malformed-label hold at `filter` clears only after a re-lock, which PAGE:628-629 does not say. Probe P4d: correcting entry in the working tree, same pin, still ARTIFACT_CONTAINMENT_HOLD. Reachable only where the near-miss was SWEEP_EXEMPT'd into a lock (P4g: SWEEP_CLEAN with exempt_holds, filter holds), since an unexempted near-miss stops the lock first.

N8 — MINOR, battery gaps on the version hold. Behaviour verified by my probe P6, so no defect found.
- Every arm sets STATIKER_SERVED_VERSION; none exercises the install-path derivation (REC:382-401), the only production path. P6: path-derived 0.2.104 over header 0.2.105 gives SKILL_VERSION_HOLD on sweep, closure, closure --unit.
- No arm drives the closure-side call (REC:2313-2315).
- The env override beats the install path in production too (P6: override 9.9.9 gives SWEEP_CLEAN). An unparseable header version (`0.2.105-rc1`, `v0.2.105`) holds nothing, as PAGE:314-317 states.
- tools/test_contract.py `test_dangling_page_pointer_is_caught`: its first assertion derives its expectation from the condition it tests, so it is green either way.

N9 — MINOR, SUBSTANCE. The compaction hook fires in any session whose repo root carries a live tracker, attack worktrees included. Probe P10b: a detached worktree of the run repo emits the notice naming the sweep/closure gate. PAGE:193-195 says no attack brief ever cites the record tool; the notice's last sentence is the only guard. Whether the harness runs SessionStart(compact) hooks for a subagent is inferred, unverified.

Read-only observation, not counted: GIT:985-988 reads any sweep verdict lacking `violations` as a clean gate. The delta fixed that by name for SKILL_VERSION_HOLD only; a sweep ending in INTERNAL_ERROR would pass the lock gate the same way. I could not induce one; unexecuted.

---

Machine-side review (7/7, final): what held, what I did not reach, and the smallest changes that would lift the HOLD.

Held under probe:
- Version hold end to end from an install-shaped path (sweep, closure, closure --unit; lock-check and unit-start through the git tool).
- `corrects-nothing` template formatting on unreachable targets (P7: header and INTENT targets, no crash, no leaked placeholder).
- sustain over a [BIT] round holding only convergence records: SUSTAIN_DENIED, record_class []; trend counts [0], record_counts [2].
- Hook: fires on a live header, on a CRLF header, from the repo root; mode 100755 in git. The four changed JSON files parse.
- defaults/models verify order (sonnet, haiku, opus) matches PAGE:1882-1885.

Not reached:
- The f954320..0bb6fd6 part of tools/test_statiker_record.py outside TestSt85*, TestSt80, TestSt89, TestSt84 — roughly 300 added lines of earlier arms unread. The 0bb6fd6..b65d673 diff I read line by line, tests included.
- tools/test_statiker_postcompact_hook.py beyond its 0bb6fd6..b65d673 diff.
- A real compaction firing the hook, and a real plugin-cache install (I simulated the path layout by copying the scripts).
- defaults/models beyond the diff hunks; statiker_stop_guard.py beyond its docstring diff (unregistered).
- The lock-gate observation in part 6 and the wrong-path-label case in N6.

Smallest changes as I read the code — none executed:
1. B1: let the three convergence forms carry a trailing `(corrects line <n>)` as the write-set declarator does, or give the code its own repair text naming the two-line route.
2. M1: make the containment-near-miss repair require the exact label beside the shed, or keep filter holding until an exact label exists.
3. M2: add convergence-near-miss to CLOSURE_BLOCKING_CODES.
4. M3: add write-set-declared units to the guard's population.
5. M4: a page edit — drop or narrow the "an aimed round's zero cannot close design" gloss.

Probe scripts, re-runnable: /tmp/claude-1000/-home-g-dev-Gunther-Schulz-statiker/7196f402-db3b-4933-bcaa-2e10d71d56b0/scratchpad/mrev/probe1.py and probe2.py (with lib.py).

---


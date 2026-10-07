# Eve review before the bt-68 run — findings and dispositions (2026-10-07)

Object: `f954320..ae19e24`, plugin payload and batteries. Desk
statiker-30 (opus), operator delegation of this date. Registration:
dev-notes/bundling-probe-preregistration-2026-10-07.md.

## What ran

- `opus-review-w` (whole delta): HOLD, 1 BLOCKING, 6 MAJOR, 6 MINOR.
- `opus-review-s1` (page half): HOLD, 1 BLOCKING, 6 MAJOR, 4 MINOR.
- `opus-review-s2` and its re-dispatch `opus-review-s2b` (machine
  half): NO REPORT, twice. Both finished their analysis (34 tool
  calls each) and stalled on a permission dialog with no operator
  present — the first on a search pattern containing `<version>`,
  read by the shell as a redirection; the second on executing the
  hook script directly. Stopped by the desk at the horizon (37
  minutes) and at the four-minute pending-call tripwire. Their
  reasoning is not stored, so nothing was harvested. A refusal by
  the environment is no result: the arm is LOST, not clean.

Both reporting lanes ran the suite themselves (723 passed, 18
subtests, 0 skipped) and wrote nothing into the repo.

## Reproduction at the desk

Every executed finding below was re-run here before it was
dispositioned, with the whole-delta lane's probe scripts copied into
this desk's scratch directory and executed against the tools at
ae19e24 (output read at the desk, 2026-10-07 18:45-18:50): the
convergence gate on a scopeless record → CLOSURE_LIVE, control
ZERO_DELTA_UNCONVERGED; terminal [BIT] → CLOSURE_LIVE; hyphenated
UNCONVERGED → CLOSURE_LIVE and LINT_CLEAN, exact form refused;
`CONVERGED at A99` tagged [PENDING] after the close → CLOSURE_LIVE;
`trend` counts [1], record_counts [2]; the four containment cases →
ARTIFACT_CONTAINMENT_HOLD with sweep clean after the tool's own
repair; version hold → `lock-check` LOCK_CHECK_CLEAN and a landed
lock commit, `unit-start` blocked; a marker-less header with a body
stamp → SKILL_VERSION_HOLD. Findings marked "read" below were opened
at the cited lines and not executed.

## Dispositions (every finding; none rejected)

Letters name the repair items in
docs/directives/2026-10-07-sonnet-repair-0205-brief.md (tool side)
or "page" (SKILL.md, desk, landed before the lane as its spec).

1. Containment label holds `filter` for good (W-B1 BLOCKING, S1-F5
   MAJOR; executed, reproduced). ACCEPTED. Cause: `filter` ran its
   own scan over raw pinned lines, a second copy of the lint's
   predicate that knows neither the body region nor the correcting
   entry. Repair A: one predicate — `filter` holds on the lint's
   LIVE violations; the exact form admits interior spaces; the code
   joins the mint-gated set. Page: the sentence now says what clears
   it and where the label sits.
2. Skipped transcription un-gates silently, against "never
   downgrades silently" (S1-F9 MINOR; W-m6 noted it as stated).
   ACCEPTED as wording: the absolute sentence is narrowed to the
   malformed case, which is what the tool enforces. The cross-check
   of preflight's declared scope against the record is NOT built
   here: declared-only is the recorded design (st-74), and the page
   says a missing label gates nothing.
3. The convergence gate sees no unit on the records the page
   produces (S1-F1 BLOCKING, W-M1 MAJOR; executed, reproduced).
   ACCEPTED. Cause: the 2026-09-25 tool half took "units" from
   pre-close `unit U<k>` D-lines, a form the page uses only after
   closure; a design-time unit has no machine-readable declaration.
   Repair B4 plus page: the population is every unit the record
   names by a convergence record or such a D-line, and the page
   gives every covered unit a record at each round's return, which
   is what makes it nameable. RESIDUAL, stated on the page: a unit
   no entry names stays invisible to the tool.
4. A terminal [BIT] skips the gate (S1-F2, W-M2 MAJOR; executed,
   reproduced). ACCEPTED. Repair B5.
5. Convergence forms fail open: a mistyped or two-finding
   UNCONVERGED is ignored and lints clean; a `[PENDING]` record
   citing a round that does not exist clears the bar (S1-F3, S1-F4,
   W-M3 MAJOR; executed, reproduced). ACCEPTED. Repairs B1-B3: a
   finding list in the form, validity (tag and round), and a
   near-miss lint on the tripwire-arm precedent.
6. ZERO_DELTA_UNCONVERGED has no stated way out, and "a landing is
   REFUSED" describes what the tool cannot do (S1-F4, W-m4).
   ACCEPTED, page: the sentence now says what `closure` returns and
   the two ways on from it; the resume passage lists the verdict.
7. An ABSENCE unit has no page route back (S1-F4, read). ACCEPTED,
   page: "a converged or absence-recorded unit". The tool already
   takes the latest record per unit (`unit_convergence_states`,
   read).
8. The version hold does not stop the lock (S1-F7, W-M4 MAJOR;
   executed, reproduced). ACCEPTED. Repair C1.
9. The version hold's token obliges the writes its seam forbids
   (S1-F6, W-M5 MAJOR; route executed, contradiction read).
   ACCEPTED. Every page location gives this verdict ONE
   disposition (append nothing, write no close), so the token takes
   that disposition's class, `barred`, and no fail-closed tiebreak
   applies. Repair C2, page seam sentence.
10. The hold fires off a body stamp on a marker-less record (W-m1;
    executed, reproduced). ACCEPTED. Repair C3.
11. The page says `trend` counts every F-line (W-M6 MAJOR, S1-F8
    MINOR; executed, reproduced). ACCEPTED, page, both passages.
12. No verdict surfaces ABSENCE state (W-m3; executed, reproduced).
    ACCEPTED. Repair B6. This is the tenet-8 debt named in this
    date's mint record with its fix pre-formulated; the review
    reached it before any run did, so it lands now.
13. Verify reads `post_closure` while the seam runs only `sweep`
    (S1-F11a, read). ACCEPTED, page.
14. ABSENCE recorded "before the round dispatches" misses the
    pinned artifact (S1-F11b, read). ACCEPTED, page: before the
    lock commit. The sentence was this desk's, written today.
15. Budget-raise cause repair un-declares the raise under
    latest-line-wins (S1-F10, read). ACCEPTED, page.
16. Compaction hook: silent off the repo root, 15-line header
    window against the page's ~20, cannot tell a lane from the desk
    (W-m2; first two executed). ACCEPTED in part. Repair D: the
    window becomes 20 and the root is resolved from the working
    directory. The lane-versus-desk case is an ACCEPTED RESIDUAL:
    the harness passes no field that separates them (W, reading
    the reference source), and it is blind spot 2 of the
    registered depth-cap probe.
17. Register comments still name haiku as the leading verify entry
    (W-m5, S1 Q3). ACCEPTED, repaired at the desk in
    `defaults/models`. READINESS.json's `why` is NOT edited: its
    2026-10-07 note is the dated correction beside a status this
    desk does not re-grade, and no consumer of codex-only mode is
    scheduled (LEDGER, 2026-10-07). The record tool's docstring
    path is corrected in repair C4.
18. `containment-near-miss` minted at "0.2.105" scopes nothing
    (W-m6, S1 Q1). ACCEPTED: the value is right, the release ships
    as 0.2.105; the missing scoping is repair A3.

Not reached by any reporting lane, by their own statements: the new
test arms line by line; `references/`; a live compaction; the
entry-owned half of the defang split (S1 executed it clean, W did
not). The post-repair read is briefed over the machine side for
that reason.

## The whole-versus-split probe (st-85, second run): VOID

The registered criterion needs union(S1, S2). S2 did not report, so
it cannot be computed, and it is not approximated. Recorded
alongside, non-deciding: on the ground W and S1 shared, S1 raised
nothing of substance that W missed except the downgrade
contradiction (2 above, which W saw and called "stated on the
page"), and W raised three findings S1 did not, all on the machine
side outside S1's reporting scope. That matches the 2026-09-25
reading. st-85 stays open on one measured point, with the
arrangement defect named: review lanes need a brief that cannot
raise a permission dialog.

## C4c FIELD TEST OUTCOME (st-37): see dev-notes/OBSERVATIONS.md

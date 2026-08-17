# Lane C brief — 0.2.82 review-repair batch (also the disposition record)

Title: sonnet: repair the 0.2.82 candidate against the checkpoint
review's findings (4 BLOCKING, 8 SHOULD-FIX)

This file doubles as the DISPOSITION RECORD for the 2026-08-17
checkpoint review (9 parts, fresh-context opus): each item below
names the finding, its disposition, and — where the disposition is
"repair" — the settled fix. Items marked [HELD] or [ACCEPTED] are
dispositions only; do not build them.

Working copy: /home/g/dev/Gunther-Schulz/statiker (shared).
Base check: `git merge-base --is-ancestor 098bda4 HEAD` AND
`git log --oneline 098bda4..HEAD` — base contained + only
dispatcher commits (BACKLOG.md/CLAUDE.md/docs/directives) on top =
proceed; anything else = halt and report.
Scratch: your OWN scratchpad.

## Grounding basis — read before building; report cites what was read
- the executor skill (dispatch-guards:executor) — load FIRST
- This file, in full (the findings' fixes are settled here).
- plugin/skills/statiker/SKILL.md (full text, 0.2.82 candidate).
- plugin/skills/statiker/scripts/statiker_record.py.
- tools/test_statiker_record.py, tools/test_contract.py.
- BACKLOG.md entries P27, P25, P19, P24, P16, P23 (context for the
  findings; the FIXES below are already settled — entries are
  background, not re-derivation license).
- Before any SKILL.md edit: invoke skill-craft (repo gate).

## The settled repairs — implement exactly these, in this order

R1 [BLOCKING, P20×P27 deadlock] — statiker_record.py closure
predicate: `design_amending` reads the D-line's SCOPE. A `record:`-
opened D-line is bookkeeping (never bars closure); a
`unit U<k> held:` D-line yields UNIT_HELD for that unit only (same
as under ZERO-DELTA); a SCOPELESS D-line and the existing
premise-kill branch are what keep closure shut. Net effect: the
terminal-BIT branch grades by the SAME predicate as ZERO-DELTA —
which is what the SKILL.md prose already promises (verify the prose
and align its wording if it names the old scan). Battery (red-first
per the standard arrangement, new expectations against the
pre-change tool, baseline stated):
  (a) the reviewer's deadlock fixture — terminal `- A1 [BIT]`, one
      `record:` F-line finding, one `[AUTO-ACCEPTED] record:`
      D-line disposition → closure SATISFIED (red today:
      CLOSURE_ABSENT);
  (b) same fixture with a SCOPELESS D-line → closure stays shut
      (the over-correction guard);
  (c) same fixture with `unit U1 held:` D-line → UNIT_HELD for U1,
      siblings dispatchable (red today: all barred).

R2 [BLOCKING, P25 disposition opener] — SKILL.md Close/leavings
passage: one sentence stating the disposition line RE-CARRIES its
`out-of-scope: ` opener (or opens `record: `), with the same
warning form the cleared-hold line uses ("the natural scopeless
phrasing voids the whole closure"). Battery: one case asserting the
natural scopeless disposition spelling still yields CLOSURE_VOID
(pinning the trap the sentence warns about — this is a
presence-of-warning + behavior pin, not a behavior change).

R3 [BLOCKING, P19 tripwire seam + arming] — settled design:
  (a) SKILL.md: the tripwire runs at ROUND-OPEN, beside `sustain`,
      and at the budget check the cap passage already names.
  (b) Arming carrier: the header `Budget:` line gains an optional
      `/ tripwire <N>` field, written at seed (or by an operator
      amendment F-line for a live run). Absent field = unarmed =
      TRIPWIRE_SILENT with reason "unarmed" — the breaker never
      guesses a default.
  (c) statiker_record.py: `tripwire` reads the threshold from the
      tracker's Budget line when `--threshold` is not given;
      `--threshold` still overrides (the caller-named principle
      kept). New verdict reason field distinguishes
      unarmed/silent/fires.
  Battery: armed-and-quiet, armed-and-fires (red today: cannot fire
  without --threshold), unarmed-silent, --threshold override.

R4 [BLOCKING-adjacent, P24 clause (b); P28's absorption rests on
it] — SKILL.md re-derivation seam (the cycle passage where a bitten
design re-enters): one clause — a claim REFUTED by a round re-enters
the design only on a basis of a DIFFERENT KIND than the refuted
one, the entry naming why the new kind is immune to the prior
failure mode. Prose mint (no battery); tenet check + OBSERVATIONS
entry per birth-class rule.

R5 [SHOULD-FIX, P26 stale prose] — SKILL.md ~:1085-1088: replace
"counts every F-line and knows nothing of class or locus" with the
true semantics (the concentration flag reads the citing entry's
class; `record:`-scoped citations do not concentrate).

R6 [SHOULD-FIX, sustain prose + docstring] — fix the SKILL.md
sentence (:1173-1178) to "independent of the desk's own
classification of the findings", and restrict cmd_sustain's
docstring to what the predicate does (reads the latest RESOLVED
round; a live [DISPATCHED] round is not consulted). Add the live
A-line as a `live_round` field in the verdict so the state is
visible (small, mechanical; battery: one case asserting the field).

R7 [SHOULD-FIX, P21 dependency] — SKILL.md intake passage: state
the write-boundary join INLINE in one clause (each candidate unit
names the files realizing it; units sharing a realizing file merge
or serialize) instead of citing the corpus mechanism.

R8 [SHOULD-FIX, verify-gate sha] — statiker_record.py:2346-2358:
compare against `verify.stdout.strip()` (the resolved full sha),
not the raw argument. Battery: abbreviated-sha case → CLEAN on
unmoved HEAD (red today: STALE with empty evidence).

R9 [SHOULD-FIX, verify sha carrier] — SKILL.md verify passage: the
read-start sha is recorded as a `record:` F-line at leg dispatch
("verify leg reads at <sha>"), so a resume can re-run the gate.
One sentence; no tool change.

R10 [SHOULD-FIX, restated mint table] — graduate the reviewer's
derivation check into tools/test_contract.py: import the module,
assert every code the file emits appears in RULE_MINT_VERSION and
every FORM code carries a mint version (ages loudly from now on).

R11 [BLOCKING, Stop hook] — disposition HELD OUT of this release:
remove the Stop-hook registration from plugin/hooks/hooks.json
(leave the script and tools/test_statiker_stop_hook.py in place as
groundwork; add a top-of-file comment in hooks.json naming the
hold and BACKLOG P16). Do NOT attempt the inversion redesign —
that is the re-opened P16's work, not this lane's.

[ACCEPTED, no build] — Q4 phantom code (duplicate of
killerless-dead; substance-by-omission safe); the P5/P15
killerless-dead tension (rider recorded: F148's distribution is the
discriminating evidence — read before any move); the pre-0.2.33
latent tension note (inert; recorded); zero-D-after-A6 provenance
check (executed dispatcher-side, predicate survives its motivating
incident by content; Q6 fix proceeds on the ordinary-shape
deadlock).

## Verifier (in order; real output pasted in the report)
1. Per repair: its named red-first arrangement above.
2. `python3 -m pytest tools/ -q` full green after every commit.
3. Final: `python3 -m pytest tools/test_contract.py -q` green
   (R10 included).

## Write boundaries
Yours: plugin/skills/statiker/SKILL.md,
plugin/skills/statiker/scripts/statiker_record.py,
plugin/hooks/hooks.json (R11 only),
tools/test_statiker_record.py, tools/test_contract.py,
dev-notes/OBSERVATIONS.md (one entry per repair commit, R4's with
tenet check).
NOT yours: BACKLOG.md, CLAUDE.md, PLAN.md, plugin.json,
plugin/hooks/statiker_stop_guard.py, tools/test_statiker_stop_hook.py.
`git commit -- <paths>`; new files none expected.
Deployment-coupled: NO — unpushed; dispatcher releases.

## Commit plan
Guards, with the read that found them: core.hooksPath=
~/dev/Gunther-Schulz/dotfiles/git/hooks (read at brief time; its
payload-version guard is DISARMED for this batch — bump 0.2.82
already committed at b897ce4, batch unpushed, exemption armed);
READY-envelope guard keys on staged BACKLOG.md (never yours);
push-claim keys on push (never yours). Order: R1 first (the
deadlock), then R2-R10 in number order, R11 last; one commit per
repair (R5+R6 may share one commit — same prose class, same file).

Closing report (mandatory; the project's own report form if it
defines one, else the §2 form here — never both; "none" is a
valid slot answer, silence is not): (a) items completed w/
evidence, (b) checks RUN w/ real output, (c) gaps surfaced —
incl. anything needing a tier above yours, returned as a question
with its evidence, never settled at your tier,
(d) deviations w/ reason, (e) candidate lessons, (f) files
touched + commit hashes (unpushed), (g) what was NOT verified,
(h) sources actually read, of those the brief named.
Message ≤3000 chars each: a report longer than one message is
SPLIT into labeled parts (1/N) — do NOT write a report FILE
(harness-blocked for subagents); supporting data goes to the
brief's assigned DATA files, the message carries key findings
+ any such paths. A missing decision, file,
or value is surfaced as a gap, never bridged with a guess.
A check that got backgrounded is AWAITED before the closing
report (TaskOutput block=true on its task id) — ending your
turn orphans it; a report sent with a check still running is
an INTERIM report, says so, and names what remains.
Commits unpushed, by pathspec — `git commit -- <paths>`, never
`git add` then `git commit` and never `-A`: the index is shared,
so a co-writer staging between your `git status` and your commit
rides out under your message whatever you added. Trailer:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.
Never amend — always a new commit: the amend-gate denies
subagent amends regardless of ownership (source: §1 amend
rule).
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended (source: §4
ownership rule).

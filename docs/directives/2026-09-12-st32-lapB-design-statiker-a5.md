# st-32 lap B design: route vocabulary, mapping, parity contract (statiker-a5, 2026-09-12)

Author: statiker-a5 (fable desk), under the operator's first-hand
delegation of 2026-09-12 (statiker-df drives; handoff
`docs/directives/2026-09-12-handoff-st32-lapB-design-statiker-a5.md`).
Design only; this file is the session's single write.

Bases: repo HEAD `62a90d9` at read time; SKILL.md last moved at
`0775b92` (1628 operational lines — the CLAUDE.md Verify awk,
executed [measured]); statiker_record.py at `f23a69b`;
test_contract.py at `6137ea3`; statiker_git.py at `f23a69b`. The
working copy is shared with the live `sonnet-st34-tools` lane; the
tree was clean at every read (`git status --short` empty). Every
verdict set below is DERIVED from the running extractor
(`test_contract.py`'s `emitted_verdicts()` / `emit_position_verdicts()`
executed this session), never restated from source reading:
76 emitted verdict names — 43 git tool, 37 record tool, 4 shared
(PATH_OUTSIDE_REPO, USAGE_ERROR, GIT_ERROR, INTERNAL_ERROR); parity
is exactly clean both directions at base [measured].

Sentences are DERIVED (design judgment) unless marked [measured].

## 0. Premise verifications

- **The handoff's unverified st-19 claim, settled by the page read
  [measured]**: two of the three items ARE still self-declared
  parked in SKILL.md prose under other wording — r4-M4 at :300-303
  ("machine-findable surfacing in the verdicts is parked tool
  work"), r4-H1 at :1356-1358 ("a start-sha-predates-the-void
  carve-out is parked tool work, never improvised at the desk").
  r3-MINOR-5 has NO surviving page declaration: the discharge-sha
  duty is stated live at :206-214 with no parked marker — lap A
  removed or never carried that one. ITEMS.md st-19's "all three
  still self-declared parked" is wrong by one.
- **fb design §2's post-B band is dead as a premise [measured]**:
  fb projected post-lap-A at ~1100-1200 lines; lap A (0.2.88)
  landed at 1628. The ~750-850 post-B band was derived from that
  projection and does not survive it. This design projects from
  the measured base (§6); lap C's booked re-derivation ("the
  number is an outcome, not a gate") is untouched.
- **TestVerdictParity spans BOTH scripts [measured:
  test_contract.py:1092-1105 — `emitted_verdicts()` unions the
  SCRIPTS list]**. Consequence: a replacement contract covering
  only the record tool silently drops the git half of what parity
  catches today. The settled sentence "routing moves into the
  record tool" and the st-32 write-set (which omits
  statiker_git.py) are therefore in tension with "each emitted
  verdict carries a route field" — resolved in §2, surfaced as a
  write-set question for statiker-df.

## 1. The closed route vocabulary

Eight tokens. A route token names the desk's seam-invariant
disposition class — the (record obligation, resolver, continuation)
triple — never the seam- or mode-specific conduct, which stays page
principle per class.

- `proceed` — the asked act succeeded or the state answer permits
  the next act; the invoking seam's own conduct consumes the
  verdict's fields. No new booking obliged by the route (a seam's
  own duty — landing annotation, quote-in-brief, quote-at-round-
  open — stays that seam's page principle, each with a mechanical
  backstop where one exists: `landing-missing`, the round-open
  quoting convention).
- `book-and-continue` — the act LANDED or the answer stands, AND
  the verdict carries a finding: booked as a `record:` F-line (or
  the drop supersede form) from the verdict line, work continuing.
- `repair-from-verdict` — the record needs a mechanical repair the
  verdict itself names (violation lines with class and repair
  form, an embedded gate verdict, an undispositioned set); compose
  the repair from the verdict, re-run the gate. Judgment residue
  the verdict names returns to the desk (the existing repair-route
  principle, kept).
- `barred` — the tool worked and its answer is "not now / not
  this": the asked action is denied by run state already in the
  record. Nothing to book (the state IS the record), no transaction
  failed; resolution is the run's own machinery (the hold entry,
  the closure re-derivation, waiting on the gate).
- `narrow` — the verdict routes to The attack's NARROWING route,
  never another same-form round. (The page keeps the narrowing
  route as principle; the token carries the destination on the
  verdict line itself.)
- `halt` — the seam stops; the verdict line is booked verbatim as
  a `record:` F-line; nothing landed UNLESS the verdict carries
  `shas`/`sha` (the standing override principle: landed commits,
  routed like HALT_RESIDUE_PERSISTS — kept on the page verbatim);
  attended, the operator's clearing reply re-enters; unattended,
  the seam's own close rule applies (page principle per seam).
  This token absorbs the sketch's `halt-uncommitted` AND
  `book-and-halt`: every halt books (the page's catch-all already
  says so), and committed-vs-not is the `shas` field, mechanical —
  two sketch tokens carried no information the field and the
  booking principle don't.
- `surface` — operator ground: no desk resolution exists (a
  tampered pin, an unpinnable tracker). Attended it leads the next
  prompt; unattended the run takes the seam's terminal disposition
  (FAILED / rides the close). Distinct from `halt` by resolver:
  a halt's clearing can be desk work on provenance; surface never.
- `triage` — the verdict is complete evidence for a desk judgment
  between dispositions the page names (stale-copy harmless vs
  re-run; contention provenance; the residue check). Judgment
  stays prose by the repo's own mint-timing convention; the token
  tells the desk it is AT a judgment seam and where its
  dispositions live.

**Closure rule.** A verdict is routable iff its
(obligation, resolver, continuation) triple matches one member. A
new member is forced only by a verdict whose triple matches none —
expected sources: a new tool capability class (e.g. an internalized
retry), or a new run-machinery destination (as narrowing once was).
Admission is fire-born: incident provenance, and the vocabulary is
machine-read semantics, so every widening rides a checkpoint review
(CLAUDE.md skill-edit review, class 2). Token merges retire the
same way.

**The unroutable verdict.** Emission never fails on a registry
gap: `finish()` stamps `route:"unrouted"` for a name the registry
lacks. The desk-side principle (page, The tools): a verdict whose
`route` field is absent, unknown, or `unrouted` is a HALT for the
seam that ran it, booked from the verdict line — fail-closed,
exactly today's catch-all. The contract (§5) makes this state
unreachable within any released pin; it exists for version skew
(a desk's loaded skill vs a newer tool) and hand-run tools.

## 2. Registry placement and stamping

- The registry is ONE dict, name-keyed:
  `ROUTES: {verdict_name: token}`, plus
  `ROUTE_VOCABULARY: frozenset` — single home in
  `plugin/skills/statiker/scripts/statiker_emit.py`, the module
  BOTH scripts already import [measured: statiker_git.py:95,
  statiker_record.py:137; test_contract.py:887-891 already copies
  the sibling module in its harness]. Each script's `finish()`
  stamps `route` into the verdict JSON via one lookup line.
- Name-keyed means a name shared by both scripts shares one
  route. All four shared names route `halt` today [measured
  against §3], so the constraint is currently free; it is stated
  because it binds future verdict naming.
- **Write-set finding (statiker-df's amendment call):** stamping
  in both scripts requires edits to `statiker_emit.py` (registry)
  and `statiker_git.py` (one lookup line in `finish()`), and
  `tools/test_statiker_git.py` gains the git-side stamping probe —
  none of the three is in st-32's booked write-set.
  RECOMMENDATION: amend the write-set to add all three. The
  admitted git-tool edit is the mechanical stamping line ONLY — no
  gate-logic change rides in (see r4-H1, §7).
- Fallback if the amendment is refused: record-tool-only stamping
  plus a `route <VERDICT>` query lane. Priced: the git tool's ~44
  verdicts keep their page prose, which is the larger half of the
  leaving mass (§6) — the lap's return roughly halves. Not
  recommended.
- Batteries and goldens: neither battery asserts whole verdict
  dicts and the golden expectations pin violation lists, not
  verdict JSON [measured: greps over both test files and
  expected-violations.json], so the route key is additive-safe by
  construction; the build lane still proves it by running the
  suite, and coordinates with the concurrent st-34 lane (same
  files in flight — every read cites its sha).

## 3. The per-verdict mapping (all 76, grouped by route)

Scratch run over the real artifact: prediction registered before
the walk — all 76 map into the eight tokens, no remainder;
predicted distribution proceed ~26, halt ~24, repair ~8, barred ~6,
book ~5, triage ~4, surface ~3, narrow ~2. Outcome: zero remainder
(the structural claim held); actual distribution halt 31,
proceed 23, repair 9, barred 5, book 4, triage 4, surface 2,
narrow 2 — halt ran higher than predicted (the catch-all class is
larger than remembered), no token unused, no ninth forced.

git tool (43):

- proceed (9): PREFLIGHT_OK, STATE_CLEAN, SEAL_PATH,
  WORKTREE_ADDED, WORKTREE_REMOVED, LOCK_CHECK_CLEAN,
  LOCK_COMMITTED, UNIT_START_CLEAN, UNIT_COMMITTED
- book-and-continue (4): LOCK_CHECK_DROPS, LOCK_COMMITTED_EXTRAS,
  UNIT_COMMITTED_EXTRAS, UNIT_COMMITTED_RESIDUE
- repair-from-verdict (1): LOCK_GATE_HOLDS
- barred (2): STATE_IN_PROGRESS, UNIT_GATE_BLOCKED
- triage (3): BLOCKED_CONTENTION, UNIT_COLLISION,
  UNIT_NO_DIFF_VS_HEAD
- surface (1): PREFLIGHT_UNPINNABLE_TRACKER
- halt (23): HALT_STATE, HALT_TRACKER_COLLISION,
  HALT_TRACKER_UNPINNABLE, HALT_DROPS_STALE,
  HALT_DROPS_UNACKNOWLEDGED, HALT_NO_CHANGES, HALT_NO_PATHSPEC,
  HALT_DIRECTORY_PATH, HALT_MISSING_PATH, HALT_RESIDUE_PERSISTS,
  HALT_IGNORED_WRITESET, UNIT_START_MISMATCH,
  UNIT_COMMIT_COLLISION, WRITE_SET_NAMES_TRACKER, GATE_UNREADABLE,
  ADD_FAILED, COMMIT_FAILED, NOT_A_REPO, PATH_INSIDE_REPO,
  PATH_OUTSIDE_REPO, USAGE_ERROR, GIT_ERROR, INTERNAL_ERROR

record tool (37):

- proceed (14): LINT_CLEAN, SWEEP_CLEAN, CLOSURE_LIVE,
  UNIT_DISPATCHABLE, WAVES_COMPUTED, TREND_COMPUTED,
  TREND_NO_ROUNDS, SUSTAIN_OK, SUSTAIN_NOT_APPLICABLE,
  TRIPWIRE_SILENT, ARTIFACT_WRITTEN, PINNED_APPEND_ONLY,
  VERIFY_COPY_CLEAN, QUOTE_BLOCK
- repair-from-verdict (8): LINT_VIOLATIONS, SWEEP_HOLDS,
  CLOSURE_RECORD_MALFORMED, CLOSURE_LEAVINGS_HOLD,
  WAVES_RECORD_MALFORMED, TREND_RECORD_MALFORMED,
  SUSTAIN_RECORD_MALFORMED, TRIPWIRE_RECORD_MALFORMED
- barred (3): CLOSURE_ABSENT, CLOSURE_VOID, UNIT_HELD
- narrow (2): SUSTAIN_DENIED, TRIPWIRE_FIRES
- triage (1): VERIFY_COPY_STALE
- surface (1): PINNED_REWRITTEN
- halt (8): UNIT_UNKNOWN, ARTIFACT_IN_REPO, PIN_UNREADABLE,
  TRACKER_UNREADABLE, PATH_OUTSIDE_REPO, USAGE_ERROR, GIT_ERROR,
  INTERNAL_ERROR

Membership notes with load: PINNED_REWRITTEN is `surface`, not
`halt` — append-only violated leaves no desk repair that is not
itself evidence-tampering, so the resolver is the operator by
construction. CLOSURE_LEAVINGS_HOLD is `repair-from-verdict` — the
verdict names the undispositioned set and the disposition FORM is
stated; the export-vs-drop content is the named judgment residue,
same split as SWEEP_HOLDS. UNIT_UNKNOWN is `halt` (a caller error;
the one-line "re-run with the id read from the record" survives as
page prose).

## 4. Findings about the page's routing (item 2's class)

Verdicts whose current page routing no single token captures —
findings about the page, not gaps in the vocabulary. Each keeps a
short page sentence at its seam; the token carries the fail-closed
or dominant member:

1. HALT_NO_CHANGES — `halt` at the lock seam, benign
   already-pinned at the close seam. Same command, two seams; the
   emission cannot know which. Route `halt`; Close keeps its one
   benign-reading sentence.
2. HALT_STATE (and the halt class generally) — the unattended
   disposition differs by seam (a halted LOCK closes FAILED, a
   halted unit rides the close). Mode/seam modulation is a page
   principle per route class, never per verdict.
3. BLOCKED_CONTENTION — plain-sense halt at the lock seam,
   provenance triage at the unit seam. Route `triage` (the unit
   occurrence is the machinery-rich one); the lock seam keeps one
   line routing it with the halts.
4. HALT_MISSING_PATH — plain halt at lock; at unit COMMIT it is
   the GAP report. Route `halt`; Implementation keeps the one gap
   sentence.
5. HALT_DROPS_STALE / HALT_DROPS_UNACKNOWLEDGED — the
   paste-and-retry-once provision is conduct no token carries;
   it stays lock-seam prose. Follow-on candidate (not lap B): the
   git tool internalizing the retry, which would delete the
   provision and re-route both to plain `halt`.
6. UNIT_NO_DIFF_VS_HEAD — the residue check is the discriminator;
   `triage`, with the brief's symbol-anchored criterion staying
   the named disposition source.
7. VERIFY_COPY_STALE — computable check, judgment disposition
   (harmless-with-named-delta vs re-run); `triage`, the two
   dispositions kept as Verify prose.

## 5. The replacement parity contract

`TestVerdictParity`'s two parity tests are replaced in the same
commit as the registry (the settled requirement); the class's four
instrument tests (backtick-label exclusion, emit-position
morphology, subcommand-derivation liveness, extractor liveness)
SURVIVE unchanged — they guard the extractor machinery the new
contract still runs on.

New class `TestRouteParity`:

1. `test_every_emitted_verdict_is_routed`:
   `emitted_verdicts() ⊆ ROUTES.keys()` — replaces the old
   direction 1; catches a verdict emitted and routed nowhere.
2. `test_every_route_entry_is_emitted`:
   `ROUTES.keys() ⊆ emitted_verdicts()` — catches phantom registry
   entries (the registry inheriting the page's old rot mode).
3. `test_route_values_are_the_closed_vocabulary`:
   `set(ROUTES.values()) == ROUTE_VOCABULARY` and
   `"unrouted" ∉ ROUTES.values()` — equality, not subset: a
   vocabulary token no verdict maps to is a dead member and fails.
4. `test_page_names_every_route_token`: each vocabulary token
   appears in SKILL.md as a backtick-quoted literal — the page
   keeps the vocabulary readable, and deleting a token's paragraph
   goes red. (Anchored on the backtick form, not bare word
   presence.)
5. KEPT AS-IS: `test_every_skill_named_verdict_is_emitted`
   (page-named ⊆ emitted) — the page legitimately keeps naming a
   residual verdict set (§4's seam sentences, the catch-all
   enumeration, templates), and this direction still catches rot
   on exactly that set. Only direction 1 is replaced.
6. `test_route_field_is_stamped` (per script): one live invocation
   each — record tool `lint` on a clean fixture asserts the
   verdict JSON carries `route == ROUTES["LINT_CLEAN"]`; git tool
   in a non-repo temp dir asserts `route == ROUTES["NOT_A_REPO"]`.
   Discrimination: a registry present but unstamped passes 1-3 and
   fails only here; the assertion is on the exact token, so a
   wrong-token stamp also fails.

What the page can still falsify: tests 4 and 5 both go red on page
edits — the contract does not become page-unfalsifiable (the
handoff's named failure mode).

**Red-first arrangement (the build lane's, stated here).**
Baseline first: `python3 -m pytest tools/ -q` GREEN at the pre-lap
sha, count stated (the unmutated case run first — a red baseline
makes every later red meaningless). Expectations are NEW, the
implementation side OLD at each red:

- R1: TestRouteParity added, tools untouched → 1/3/6 red
  (no ROUTES) — proves non-vacuity against the old tool.
- R2: registry landed minus one emitted verdict (e.g.
  WORKTREE_REMOVED) → test 1 red NAMING it; restore.
- R3: one phantom key planted → test 2 red; restore.
- R4: one value off-vocabulary → test 3 red; restore.
- R5: one token's backtick literal removed from the page → test 4
  red; restore.
- R6: stamping line removed from one `finish()` with the registry
  total → 1-3 green, 6 red — proves 6 non-redundant.

Each red recorded per Implementation's forms (committed red arm or
the red run's pasted output). The old direction-1 test is deleted
in the registry commit; goldens re-run (regen only if the sweep
test's expectations turn out to embed verdict lines — §2 measured
they do not — with any regen diff reviewed, st-34's n2 regen-guard
caveat applying).

## 6. What stays on the page, re-measured

Routing-adjacent spans at 0775b92, non-blank lines
[measured, python over the named ranges]: tools residue :80-111 =
30; lock routes :799-864 = 66; unit routes :1386-1489 = 104;
record gate :179-204 = 25; [READY] sweep :631-649 = 19; closure
predicate :1223-1335 = 112; attack repeat-round :1071-1120 = 50;
sustain/tripwire seam :1163-1196 = 34. Sum 440.

Of that, KEEP (derived, per-span classification): the verdict-line
booking principle and `shas` override; write-side templates and
forms (drop F-line, hold entry, cleared line, exemption forms);
the closure predicate's compose-side semantics ("what the desk
WRITES so the read comes out true" — most of the 112); the
clearing-by-shape judgment and its provenance rule; the narrowing
route; §4's seam sentences. LEAVES to the registry: the
per-verdict route listings and their halt enumerations —
approximately 22 (tools) + 54 (lock) + 60 (unit) + 15 (gate) + 7
(sweep) + 30 (closure invocation/routes) + 25 (trend consult
detail) + 20 (sustain/tripwire routes) ≈ 230 lines. ADDED: the
vocabulary section with the eight token paragraphs and the
unrouted principle ≈ 40 lines.

Net projection: 1628 − 230 + 40 ≈ **~1440 operational lines
post-lap-B** (a hand-classified estimate; the release prints the
measured count). Stated plainly: this is far above fb §2's
~750-850, whose premise (lap A landing at 1100-1200) is dead —
§0. The compression pass's remaining distance to any target is lap
C's re-derivation question, on the measured residue, exactly as
booked.

## 7. st-19's three items, graded (item 5)

- **r4-M4 — IN-SCOPE for lap B.** The budget-raise entry's
  machine-findable surfacing is read-side precipitation in the
  booked write-set: sweep and closure verdicts gain a
  `budget_raises` field (latest raise entry per the template,
  `late_intent`'s shape), with its own red-first battery rows; the
  page's :300-303 parked note shrinks to the template plus one
  surfacing sentence. It is the same class as the lap's routing
  move and shares its review.
- **r4-H1 — RE-PARK.** The commit gate's
  start-sha-predates-the-void carve-out is git-tool GATE LOGIC — a
  behavior change with its own battery, not a representation move;
  bundling it under lap B hides which edit did what at the
  checkpoint review. Named trigger: the first run in which the
  fail-closed void halt costs a clean sibling re-dispatch (the
  measurable-cost trigger st-19 already names), or the next
  statiker_git.py behavior lap, whichever first. The §2 write-set
  amendment, if granted, admits the one-line stamping edit only —
  not this.
- **r3-MINOR-5 — RE-PARK.** A lint class needs a positional or
  literal anchor, and the discharge line has NO minted form —
  :206-214 states the duty in prose with no machine token
  [measured]. Minting a discharge-line form is NEW grammar, not
  precipitation of existing semantics, so it is outside lap B's
  class. Named trigger: the discharge-form mint decision
  (candidate seam: lap C's conduct pass; or fire-born on the first
  incident of a missed expiry traced to a sha-less discharge
  line). Fail-safe meanwhile stands, as parked.

## 8. Transition table (arrow → verb → record → check)

| arrow | verb | record | check |
|---|---|---|---|
| design delivered → committed | git add -N + commit by pathspec (this file only) | the commit | statiker-df's close check: commit on remote after their push |
| design → graded | SendMessage report to statiker-df | statiker-df's ledger/harvest line | the entry cites this file |
| write-set question → decided | statiker-df amends st-32 (or refuses; fallback §2) | ITEMS.md st-32 write-set slot | `lifecycle item check` clean; slot names the three files or the fallback is recorded |
| lap B GO → built | build-lane brief quotes §§1-5 (quoted, never restated) | route line at GO; lane commits | brief cites this file; registry commit deletes old direction-1 test in the same commit |
| registry → proven red | the R1-R6 arrangement (§5) | committed red arms / pasted red runs | baseline green stated first; each red names its target |
| page → shrunk | SKILL.md edit per §6 keeps/leaves | the lap commit | Verify awk count printed; tests 4+5 green |
| lap B → released | opus checkpoint review (machine-read semantics, mandatory) → dispositions → pin move | OBSERVATIONS dispositions + clause-disposition table + tenet check (the releasing desk's, per Birth-class discipline) | dispositions recorded BEFORE pin move; `pytest tools/ -q` green |
| r4-M4 → shipped | rides the lap's build lane | its battery rows + the shrunken page note | sweep/closure verdicts carry `budget_raises`, red-first recorded |
| r4-H1, r3-MINOR-5 → re-parked | statiker-df re-grades st-19 | ITEMS.md st-19 blocker names both triggers | `lifecycle item check` clean |

Every arrow names its actor; the two meta-side arrows are
statiker-df's, per the handoff's obligation split. The scratch run
this design's sign-off owes is §3's executed mapping walk
(prediction registered, outcome recorded).

## 9. Economics line

Currencies per the repo lens. Turns: one build lane (registry +
stamping + tests + page edit + r4-M4), one opus checkpoint review,
one release at the batching seam — no new round class; the R1-R6
reds are desk-side arms inside the lane, not extra trips. Lines:
page −230 +40 ≈ net −190 (§6), registry ≈ +45 tool lines carrying
what the page drops, at fire-time enforcement instead of read-time
prose — the medium tenet's direction. What this lap deliberately
does NOT buy: the size target (lap C's re-derivation, booked), the
disclosure question (§5 of the fb design, out of scope), and the
seam-dependent verdict splits (§4 — future git-tool work, each
fire-born on its own incident).

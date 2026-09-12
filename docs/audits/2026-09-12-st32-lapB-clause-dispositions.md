# st-32 lap B stage 1 — per-clause dispositions over the 28 lap-A `B` rows

Author: opus-st32-clause-table (opus lane, dispatcher team-lead),
2026-09-12. Brief:
`docs/directives/2026-09-12-opus-st32-clause-table-brief.md` — read at
`3c041e5`; the dispatcher corrected it in place at `d901291` after
this lane's critique pass, and the corrections (Background 1, 2, 3,
the `stale-range@769e7f2` column name, and the added coverage-map
requirement) are all satisfied below.
Design dispositioned against:
`docs/directives/2026-09-12-st32-lapB-design-statiker-a5.md` (§§1, 3,
4, 6). Lap A's table:
`docs/directives/2026-09-11-st29-lapA-clause-table.md`.

**Object — pinned, not live.** `plugin/skills/statiker/SKILL.md` at
**`3c041e5`**, taken once as
`git show 3c041e5:plugin/skills/statiker/SKILL.md`. 1638 operational
lines / 1727 total by the CLAUDE.md Verify awk [measured]. **Every
`range@3c041e5` below is a line number in THAT file.** A `sonnet-st32-registry`
lane was writing the live `SKILL.md` concurrently; no live read entered
this table.

This table decides dispositions; it edits nothing. A later build lane
applies it.

## Rules applied

Lap A's column discipline is kept (its "Table conventions", cited):

- **Row unit**: lap A's 28 `B` rows, unsplit and unmerged — 28 in, 28
  out.
- **Range**: starts at the line where the row's re-anchored handle
  BEGINS; where a clause boundary falls mid-line the shared line
  belongs to the LATER row, so a row's range may open mid-sentence
  (lap A's own convention — visible in I3, I4, I6, I7, I14, I17, I18,
  K3 below). A row's end is the next lap-A handle's resolved start
  minus one, resolved over all 156 lap-A rows, not the 28 alone.
- **Re-anchoring**: by QUOTED handle against the pinned page with
  every whitespace run (line breaks included) normalised to one
  space — never by line number. Lap A's ranges are anchored at
  `769e7f2`, a 1766-operational-line page; mine at `3c041e5`, 1638.
  26 of 28 handles resolved uniquely and monotonically by script; 2
  (T10, R27) were rewritten by lap A's own TIGHTEN and were
  hand-anchored on their surviving opening (verification appendix).
- **Line counts**: non-blank lines only, so they are comparable with
  the Verify awk and with design §6's spans.
- **`leaves`/`stays` split**: a clause leaves only where a reader of
  `ROUTES` plus the page's remaining principle reaches the SAME
  conduct. Seam- or mode-dependent disposition the token cannot
  express (design §4's class) KEEPS. No other home → KEEPS, whatever
  the size (brief's rule).
- **Token routes cited** are design §3's mapping, verbatim.
- **Coverage map**: the design's ~230 is a sum over eight SPANS at a
  third sha, a different partition of a different object from lap A's
  28 rows. The spans are re-expressed as `3c041e5` line numbers and
  intersected with the resolved row ranges before any comparison is
  made; uncovered span blocks are reported as gaps, never absorbed.

## Summary

| | rows | non-blank now | leaves | stays |
|---|---|---|---|---|
| PRECIPITATES | 0 | 0 | 0 | 0 |
| SPLIT | 16 | 279 | 66 | 213 |
| KEEPS | 12 | 231 | 0 | 231 |
| **total** | **28** | **510** | **66** | **444** |

**Totals row (mandatory).** Non-blank lines LEAVING the page from the
28 `B` rows: **66**. STAYING: **444**. Against the pinned page's
operational count: 1638 − 66 = 1572; with design §6's ADDED
vocabulary section (≈40) the projected post-lap-B page is **≈1612
operational lines**, against the design's projected ~1440.

**Divergence from design §6's ~230 estimate: −164 (measured 66 vs
estimated ~230).** Reported as a finding about the estimate (below),
not resolved by bending any disposition.

## Findings

**F1 — §6's per-span leaving figures contradict §6's own KEEP list,
hardest over the lock and unit spans.** §6 KEEPs "write-side
templates and forms (drop F-line, hold entry, cleared line, exemption
forms)", "the verdict-line booking principle and `shas` override",
"the clearing-by-shape judgment and its provenance rule", "§4's seam
sentences" — and §4 additionally keeps, by name, the
paste-and-retry-once provision (item 5), the Implementation gap
sentence (item 4), the residue-check criterion (item 6), the Close
benign-reading sentence (item 1). Over the lock span those kept
classes ARE most of the span: measured leaving from S17+S18 is 12 of
the lock span's 66 non-blank lines, against §6's estimated 54. Over
the unit span (104 nb, 103 of them inside I14-I18), measured 18
against an estimated 60. The two halves of §6 cannot both be
right; the KEEP list is the one §4 corroborates clause by clause, so
the estimate is what this table finds wrong.

**F2 — the trend-consult detail (§6, "25 (trend consult detail)") has
no registry home at all.** A17's load is `trend`'s FIELD semantics —
raw per-round counts are class-blind while the concentration flag
reads the citing entry's class, so the grade never comes from the
verdict alone — plus the NARROWING route. `ROUTES` maps verdict NAME
→ route TOKEN; it cannot carry a caveat about how to read a verdict's
fields, and `NON-CONTRACTING` is a desk grade, not an emitted verdict
name, so it has no registry key at all. A17 leaves 0 of 34.

**F3 — three `B` rows carry no verdict token whatsoever** (R31, R32,
R38; 51 non-blank lines), and three more carry none in lap A's token
column (A17, I4, I7; 97 lines). 148 of the 510 lines in this table's
object are therefore structurally unreachable by a verdict-name-keyed
registry. Lap A marked them `B` as "record read-side semantics"; lap
B's instrument does not reach that class.

**F4 — four blocks of design §6's leaving mass fall OUTSIDE this
table's object.** The coverage map below gives them in full; the
largest is §6's whole "record gate :179-204 = 25, leaving ~15" span,
which at `3c041e5` (the resume RECORD GATE, routing CLOSURE_ABSENT /
CLOSURE_LIVE / CLOSURE_VOID by KIND) sits in lap-A rows R4 (marked
`§5`, a disclosure candidate) and R6 (unmarked) — neither is a `B`
row. 72 non-blank lines of §6's spans have no `B` row covering them.
Surfaced as a gap for the dispatcher: either those blocks enter lap
B's object by a separate decision, or their share of the ~230 drops
out of the design's leaving total.

**F5 — three routings in this table CHANGE conduct rather than
precipitate it.** Each is the design's deliberate call, recorded here
because "same conduct" is the brief's own test for a leave:
- `PINNED_REWRITTEN` — page (R27:427) says "halts the seam that ran
  it"; §3 routes it `surface` (no desk resolver by construction).
  halt → surface.
- `UNIT_GATE_BLOCKED` — page (I14:1405-1407) says "halt the unit
  UNBUILT"; §3 routes it `barred`, which books nothing where a halt
  books an F-line.
- `UNIT_COLLISION` — page (I14:1410-1416) routes it with the halts;
  §3 routes it `triage`.
Each needs the build lane to state which side wins in the page text
it leaves behind. Not bridged here.

**F6 — the lock seam and the unit seam disagree about
BLOCKED_CONTENTION and HALT_MISSING_PATH, and §4 resolves it by
keeping page lines, not by the token.** That is why S18's halt
enumeration leaves only 4 of its lines: the parenthetical "the last
two in their plain senses, never the unit rules' meanings" (S18:871)
is load-bearing and stays.

---

## The table

Columns per the brief. `leaves` names the other home for every
PRECIPITATES/SPLIT row. `stays` gives PRINCIPLE + VOCABULARY with a
target non-blank line count. Route tokens cited are design §3's.

### The tools

| id | anchor | range@3c041e5 | stale-range@769e7f2 | disposition | leaves (+ other home) | stays (target lines) | tokens-dropped | tokens-kept (why the page needs each) | basis |
|---|---|---|---|---|---|---|---|---|---|
| T4 | "Every invocation — usage errors included (USAGE_ERROR); `--help` alone" | 73-79 (6 nb) | 75-82 | KEEPS | — | The one-verdict-line rule, the `--help` exception, and the book-THAT-LINE-verbatim principle; "an exit code is routing convenience, never the result". **6** | none | USAGE_ERROR — the "usage errors included" exception names it; dropping the name leaves the exception unstateable | §6 KEEP, "the verdict-line booking principle". No per-verdict routing in the row |
| T5 | "Happy paths route in their own sections; `lint` alone answers" | 80-91 (11 nb) | 83-95 | SPLIT | The four returns-listings: "`lint` … (LINT_CLEAN / LINT_VIOLATIONS)", "`quote` and `filter` return QUOTE_BLOCK and ARTIFACT_WRITTEN with production counts", "`waves` returns WAVES_COMPUTED". Home: `ROUTES["LINT_CLEAN"]==proceed`, `ROUTES["LINT_VIOLATIONS"]==repair-from-verdict`, `ROUTES["QUOTE_BLOCK"]==proceed`, `ROUTES["ARTIFACT_WRITTEN"]==proceed`, `ROUTES["WAVES_COMPUTED"]==proceed`. **4** | The subcommand inventory sentence ("happy paths route in their own sections; `lint` alone answers ad-hoc grammar questions; `sweep` includes it") and the whole `waves` SEMANTICS: shared-write-set grouping, members of a group SERIALIZE, scheduling across groups is the desk's (read from the D-lines), UNPLANNABLE units appear in neither list, "the partition is no dispatchability read — the per-unit gate stays `closure --unit`". **7** | LINT_CLEAN, LINT_VIOLATIONS, QUOTE_BLOCK, ARTIFACT_WRITTEN | WAVES_COMPUTED — the retained semantics paragraph is about what that verdict's partition does and does NOT authorise; a route token carries none of it | §6 LEAVES "the per-verdict route listings"; §1 `proceed` ("the invoking seam's own conduct consumes the verdict's fields") is exactly what the kept half states |
| T6 | "`trend` returns TREND_COMPUTED /" | 92-103 (11 nb) | 96-107 | SPLIT | The returns-listings for `trend`, `sustain`, `tripwire`, and the four-way malformed enumeration "all four halt WAVES_RECORD_MALFORMED / TREND_RECORD_MALFORMED / SUSTAIN_RECORD_MALFORMED / TRIPWIRE_RECORD_MALFORMED … repaired like any lint hold (`corrects line <n>` composed from the verdict's violation lines)". Home: `ROUTES["TREND_COMPUTED"]==proceed`, `ROUTES["TREND_NO_ROUNDS"]==proceed`, and all four `*_RECORD_MALFORMED` `== repair-from-verdict`. **6** | What `trend` COMPUTES — "per-round F-LINE counts (every F-line in a round's span, not attacker findings alone) with an arithmetic trajectory verdict" — and the two seam pointers (`sustain` → the never-sustain round-open gate, The attack; `tripwire` → The record, Budget). **5** | TREND_COMPUTED, TREND_NO_ROUNDS, WAVES_RECORD_MALFORMED, TREND_RECORD_MALFORMED, SUSTAIN_RECORD_MALFORMED, TRIPWIRE_RECORD_MALFORMED, and (here only) SUSTAIN_OK / SUSTAIN_DENIED / SUSTAIN_NOT_APPLICABLE / TRIPWIRE_FIRES / TRIPWIRE_SILENT — A23 is their surviving seam home | none | §6 LEAVES "the per-verdict route listings and their halt enumerations"; §1 `repair-from-verdict` ("compose the repair from the verdict, re-run the gate") absorbs the repair sentence |
| T7 | "ANY verdict no section names is a halt for" | 104-112 (8 nb) | 108-116 | SPLIT | (a) the eight-name catch-all enumeration (TRACKER_UNREADABLE, PIN_UNREADABLE, NOT_A_REPO, PATH_OUTSIDE_REPO, PATH_INSIDE_REPO, USAGE_ERROR, GIT_ERROR, INTERNAL_ERROR, "and any future member") — home: a `ROUTES` entry `== halt` for each, and §5 test 1 makes "any future member" mechanical instead of prose; (b) the catch-all sentence itself, ABSORBED (not deleted) by the added vocabulary section's unrouted paragraph, §1: "a verdict whose `route` field is absent, unknown, or `unrouted` is a HALT for the seam that ran it, booked from the verdict line — fail-closed, exactly today's catch-all". **5** | The `shas`/`sha` override, verbatim: "one override on every route: a halt verdict carrying a `shas` or `sha` field has LANDED commits — routed like HALT_RESIDUE_PERSISTS, never as uncommitted". **3** | TRACKER_UNREADABLE, PIN_UNREADABLE, NOT_A_REPO, PATH_OUTSIDE_REPO, PATH_INSIDE_REPO, USAGE_ERROR, GIT_ERROR, INTERNAL_ERROR | HALT_RESIDUE_PERSISTS — §1 `halt` keeps the override "on the page verbatim" and it routes BY EXAMPLE, so the exemplar's name is the rule's only anchor | §1 the unroutable verdict; §6 KEEP "the verdict-line booking principle and `shas` override" |
| T9 | "At run start, before any design work: `preflight --tracker <path>`" | 120-128 (8 nb) | 127-136 | SPLIT | "PREFLIGHT_OK proceeds". Home: `ROUTES["PREFLIGHT_OK"]==proceed`. **1** | The seam duty (preflight at run start, before any design work) and the tool-behaviour invariant no token carries: the DEDICATED index-reading repo-health read, a corrupt index halting there, mid-run corruption surfacing at whatever seam meets it, and "strictness is the health read's alone — every other read keeps its DOCUMENTED exit semantics: a non-error exit (the ignore check's not-ignored) is an answer, an error exit of any read still halts". Keep the informational in-progress note. **7** | PREFLIGHT_OK | none | §6 LEAVES per-verdict route listings; the invariant has no registry home (brief's "no other home → KEEPS") |
| T10 | "PREFLIGHT_UNPINNABLE_TRACKER = the repo" | 129-137 (8 nb) | 137-144 | SPLIT | PREFLIGHT_UNPINNABLE_TRACKER's routing — "surfaced to a present operator before further work; unattended the run closes FAILED at minimal cost; any other preflight verdict surfaces the same way". Home: `ROUTES["PREFLIGHT_UNPINNABLE_TRACKER"]==surface`, whose §1 paragraph already reads "Attended it leads the next prompt; unattended the run takes the seam's terminal disposition (FAILED / rides the close)". **4** | The `state-gate` re-entry instrument: the subcommand exists, and an attended halt's clearing reply is VERIFIED by it before the halted procedure re-runs. This is a desk duty at a seam, not a disposition of a verdict — no route token obliges running anything. **4** | PREFLIGHT_UNPINNABLE_TRACKER | STATE_CLEAN, STATE_IN_PROGRESS — the retained re-entry sentence is the only place the page says which answer clears a halt | §3 `surface` (1 git verdict); §1 `surface`. Hand-anchored: lap A's TIGHTEN rewrote "means the repo" → "= the repo" |

### The record

| id | anchor | range@3c041e5 | stale-range@769e7f2 | disposition | leaves (+ other home) | stays (target lines) | tokens-dropped | tokens-kept (why the page needs each) | basis |
|---|---|---|---|---|---|---|---|---|---|
| R13 | "Exhaustion never continues silently: attended it forces the" | 272-284 (12 nb) | 281-297 | KEEPS | — | Exhaustion never continues silently; attended it forces the operator prompt; unattended the cap is a SAFETY ESCAPE only — STOPS-AND-REPORTS, never grades FAILED by itself. The DRIVING stop signals are progress-shaped and record-computable, checked well before the cap: the ZERO-LANDED tripwire with its firing predicate and its arming source (`<n>` from the arming carrier, never hardcoded, never guessed; no source naming one is TRIPWIRE_SILENT reason "unarmed"), and the NON-CONTRACTING trend grade — BOTH route to the NARROWING route, never to another same-form round. **12** | none | TRIPWIRE_FIRES, TRIPWIRE_SILENT — the routing sentence carries TWO destinations and only one is a verdict: `NON-CONTRACTING` is a desk grade with no registry key, so deleting the sentence would strand it | §6 KEEP "the narrowing route"; brief's "no other home → KEEPS". The firing predicate and the unarmed-reason semantics are tool/arming semantics `ROUTES` cannot key |
| R27 | "Run `lint` once header and head are written" | 421-434 (13 nb) | 456-470 | SPLIT | "PINNED_APPEND_ONLY proceeds; PINNED_REWRITTEN halts the seam that ran it". Home: `ROUTES["PINNED_APPEND_ONLY"]==proceed`, `ROUTES["PINNED_REWRITTEN"]==surface`. **CONDUCT DELTA — see F5**: the page says halt, the registry will say surface; §3's membership note is the design's stated reason. **2** | When and why to run the checks: `lint` once header and head are written (a form defect found then costs one screen, found at the [READY] sweep it holds a record whose head append-only cannot rewrite); `pinned --tracker P --sha S` once a pin exists, the two mutable field lines exempt and every other line byte-exact; run it at resume and before any re-lock; the in-place-TAG-rewrite rationale ("the pin diff is the one thing it cannot fool"); S recoverable as the newest commit touching the tracker. **11** | PINNED_APPEND_ONLY, PINNED_REWRITTEN | none — the retained text says the append-only claim is checked mechanically, which is what the desk acts on | §6 LEAVES per-verdict route listings; §3 membership note (PINNED_REWRITTEN is `surface`). Hand-anchored: lap A's TIGHTEN dropped "the" from "once the header" |
| R31 | "A mistyped `SWEEP_EXEMPT:` fails safe — the hold it meant to net" | 462-478 (16 nb) | 497-514 | KEEPS | — | Whole: fails-safe on a mistyped literal; DETECTION wider than validity by design, positional never word-search, near-miss violations; validity never relaxes; the exclusions (quoted lines, the requirement head above the first `## ` heading); class and repair form settled in the executable spec and NAMED by the verdict; the lint is a tripwire over the observed slip space, not the guarantee; DEFANG lint separate and whole-file. **16** | none | none (the row carries no verdict token — lap A's token cell reads "none") | Brief's "no other home → KEEPS": the row states lint SEMANTICS, and `ROUTES` is keyed on verdict names this row does not contain. One phrase ("the desk composes repairs from the verdict, never from memory") is restated by the added `repair-from-verdict` token paragraph; too small to split and the local statement is what the sweep seam reads |
| R32 | "Beside the write-set declarator: a correction appended under a" | 479-495 (16 nb) | 515-530 | KEEPS | — | Whole: the declarator-bookkeeping refusal and its exemption, the latest-line-wins rationale, the different-unit-redeclaration case, and the supersede-whole REPAIR FORM verbatim (restate the full write-set under the same id AND the same unit, trailing `(corrects line <n>)` naming the ORIGINAL target — the one legal slot). **16** | none | none (lap A token cell: "none") | §6 KEEP "write-side templates and forms"; no verdict token in the row |
| R38 | "- a basis citing ANOTHER record's entries names the record (tracker" | 510-528 (19 nb) | 546-564 | KEEPS | — | Whole: foreign citations name the record before their ids; the bare-id namespace hazard; the live-basis scan's record-name token definition (punctuation stripped, contains `/` AND ends `.md`/`.md:`, or `run <name>:`), the non-qualifying cases, the exemption persisting across a comma-separated id list and dying at the first non-id token; the `foreign-id-suspect` backstop; ids under a record-name token not checked against this run's invalidations. **19** | none | none (lap A token cell: "none") | Brief's "no other home → KEEPS": record-grammar semantics, no verdict key. See F3 |
| S3 | "[READY] is recordable only when the record sweeps clean" | 641-660 (19 nb) | 683-705 | SPLIT | The SWEEP_HOLDS payload enumeration — "(latest-line [PENDING]s, killer-less dead dispositions, live bases citing invalidated ids, grammar and defang lint …, the verdict naming each violation's class and repair form)". Home: `ROUTES["SWEEP_HOLDS"]==repair-from-verdict`, whose §1 paragraph already says the verdict names violation lines with class and repair form. **4** | The [READY] PREDICATE (no latest-line [PENDING]; an assumption carried unverified gets [AUTO-ACCEPTED], never [PENDING]; no id live twice, by body-read; no live entry on an invalidated entry's content, the dead-basis read covering the invalidation lines themselves). The §4-class modulation: "SWEEP_CLEAN clears the MECHANICAL HALF ONLY" — a `proceed` token reads as go, and this sentence is the negative the token cannot carry. The judgment-residue split (dead-basis body-reads, duplicate-id body-read, restatement adoption checks stay desk work). `sweep` runs FIRST at this seam. The `corrects line <n>` pointer to Implementation's form. "An open [PENDING] under a claimed [READY] is the premature-call shape". **15** | none | SWEEP_CLEAN — the "mechanical half only" caveat is stated ABOUT it; SWEEP_HOLDS — the residue split is stated about its verdict | §6 LEAVES "7 (sweep)"; §4's class for the clears-only-half sentence; §6 KEEP for the template pointer |
| S4 | "A declared exemption nets a matching hold out of the blocking set" | 661-688 (27 nb) | 706-737 | KEEPS | — | Whole: both labeled SWEEP_EXEMPT forms VERBATIM; sibling placement and field-not-gate treatment; the netting into `exempt_holds` with each exemption's declaring line; coverage FROZEN at the declaring line (a violation above min(`<n>`, the declaring line) alone is netted); the mandatory `— basis:` operator-authority tail and the citation-less refusal; a desk never exempts its own gate's holds; unattended unexemptible holds ride the close; the guard verifies BOUNDS not legitimacy; exemptible holds are FORM DEBT only; defang-class and live-work holds never exemptible, with both reasons; `exempt_holds` enumerated in the close. **27** | none | SWEEP_HOLDS — "before SWEEP_HOLDS is decided" fixes WHEN netting happens, a sequencing fact no route token carries | §6 KEEP "write-side templates and forms (… exemption forms)"; the row holds no route listing |

### Stop rule — the lock seam

| id | anchor | range@3c041e5 | stale-range@769e7f2 | disposition | leaves (+ other home) | stays (target lines) | tokens-dropped | tokens-kept (why the page needs each) | basis |
|---|---|---|---|---|---|---|---|---|---|
| S17 | "(c) `lock-check --tracker <path> [--lock-set <path> …]`." | 809-843 (35 nb) | 857-891 | SPLIT | (a) the "Verdict routes:" label; (b) "Its route is REPAIR, never a verdict on the run: repair or exempt the blocking holds, re-sweep, re-lock" — home `ROUTES["LOCK_GATE_HOLDS"]==repair-from-verdict`; (c) HALT_STATE's generic half ("the operator's half-finished operation, the tree untouched — an attended halt re-enters on the operator's clearing reply") — home `ROUTES["HALT_STATE"]==halt`, §1 `halt` ("attended, the operator's clearing reply re-enters"); (d) "HALT_TRACKER_COLLISION and HALT_TRACKER_UNPINNABLE halt the same way" — home: a `halt` entry each; (e) LOCK_CHECK_DROPS's route half — home `ROUTES["LOCK_CHECK_DROPS"]==book-and-continue`. **8** | The LOCK_GATE_HOLDS PREDICATE (blocking set non-empty AND Status NOT on the close path; [READY], in-progress, PASSED, missing or malformed status all fail closed; the consulted record verdict embedded verbatim as the `gate` field) and its invariant "the record never locks over its own blocking state ahead of close". The close-path inversion: under FAILED/COMPLETE the gate PASSES with the blocking set still carried in `gate` as information, never silently dropped — a close-time lock legitimately carries PENDINGs; PASSED is a transient pre-close state this seam never locks over. The unattended-hold ending (neither repairable nor exemptible → rides the close, FAILED with the hold enumerated). **§4 item 2's seam sentence verbatim**: unattended, a halted LOCK closes the run FAILED (no lock, nothing to build on) while a halted unit rides the close's deviations. The tracker invariant (never dropped, never force-added). The drop TEMPLATE: recorded BEFORE the commit in the tracker the commit pins, a [VERIFIED] F-line carrying the verdict line as basis, the path's lock-set line superseded by `- F<n> [INVALIDATED] <path> dead (collision\|ignored) — basis: <the drop F-line's id>`, and the standing gloss that "contradicted" anywhere in the skill means that supersede form. Attended/unattended surfacing. **27** | LOCK_CHECK_DROPS | LOCK_GATE_HOLDS (the predicate is stated about it); HALT_STATE (§4 item 2's kept seam sentence names it, and it is the page's routing exemplar for the other lock halts); HALT_TRACKER_COLLISION, HALT_TRACKER_UNPINNABLE (the never-dropped/never-force-added invariant is stated about exactly these two) | §6 LEAVES "54 (lock)" — measured 8 here, see F1; §4 item 2; §6 KEEP for the drop template |
| S18 | "(d) `lock-commit`, same arguments plus `-m` and one `--drop`" | 844-874 (31 nb) | 892-922 | SPLIT | The closing halt enumeration's ROUTE half: "Any other lock verdict (HALT_NO_CHANGES, HALT_NO_PATHSPEC, HALT_DIRECTORY_PATH, … USAGE_ERROR, GIT_ERROR, INTERNAL_ERROR) halts the lock uncommitted, verdict line booked as a `record:` F-line, routed like HALT_STATE" — home: a `ROUTES` `== halt` entry per name, plus §1 `halt` ("the verdict line is booked verbatim as a `record:` F-line"). **The enumeration's parenthetical does NOT leave** (F6). **4** | The invocation form (`-m` plus one `--drop` per recorded drop; LOCK_CHECK_CLEAN skips straight here with no drops). **§4 item 5 verbatim**: HALT_DROPS_STALE / HALT_DROPS_UNACKNOWLEDGED mean the acknowledged and live drop sets differ — re-run lock-check, re-record, retry ONCE; the `--drop` argument PASTED from the verdict line, never re-typed (two spellings of one byte deadlocked this handshake, and the re-typing hop is the desk); a second mismatch OF ANY KIND halts the lock uncommitted, the two sets surfaced verbatim. LOCK_COMMITTED's sha IS the lock commit — the attack brief pins it and the locked design is the record at that commit. LOCK_COMMITTED_EXTRAS's content rule: recorded as a collision-class contradiction, named a brief exclusion, NEVER reverted out of the working tree (the revert would destroy the operator state the finding names). The `shas` override in full: HALT_RESIDUE_PERSISTS is a halt WITH commits in history, its `shas` field listing every landed commit, the last one not readback-clean — booked, shas surfaced, the run halting like HALT_STATE and never "no lock, nothing to build on", and so does ANY halt verdict carrying `shas`. **§4 items 3+4's seam disambiguation**: HALT_MISSING_PATH and BLOCKED_CONTENTION here in their PLAIN senses, never the unit rules' meanings. **27** | HALT_NO_PATHSPEC, HALT_DIRECTORY_PATH, USAGE_ERROR, GIT_ERROR, INTERNAL_ERROR (their lock-seam listing only — T7's catch-all and the registry carry them) | LOCK_CHECK_CLEAN (the skips-straight-here sequencing); HALT_DROPS_STALE, HALT_DROPS_UNACKNOWLEDGED (§4 item 5, explicitly kept as lock-seam prose); LOCK_COMMITTED, LOCK_COMMITTED_EXTRAS (their content rules are kept and are stated about them); HALT_RESIDUE_PERSISTS, HALT_STATE (the `shas` override, §6 KEEP); HALT_MISSING_PATH, BLOCKED_CONTENTION (§4 items 3+4 — the plain-sense disambiguation is the page's only guard against the unit-seam reading); HALT_NO_CHANGES (its lock-seam reading differs from K3's benign close reading, §4 item 1) | §6 LEAVES "54 (lock)" — measured 4 here, see F1; §4 items 3, 4, 5; §6 KEEP for `shas` |

### The attack

| id | anchor | range@3c041e5 | stale-range@769e7f2 | disposition | leaves (+ other home) | stays (target lines) | tokens-dropped | tokens-kept (why the page needs each) | basis |
|---|---|---|---|---|---|---|---|---|---|
| A17 | "The reply opening a repeat round — from the SECOND" | 1081-1114 (34 nb) | 1148-1182 | KEEPS | — | Whole: the repeat-round reply cites `trend` as arithmetic BACKSTOP and grades by BODY-READ; the field caveat (`trend`'s raw per-round counts read every F-line regardless of class or locus while the concentration flag DOES read the citing entry's class, a `record:`-scoped citation never concentrating, so the grade never comes from the verdict alone); no series below two completed [BIT] rounds; the CONTRACTING / NON-CONTRACTING definitions with the founding-shape parenthetical; the NARROWING route in full (R-amendment, the EXPORTED backlog entry carrying successor-run intent, successor seeding on citable parent entries, narrowing riding the close as reconciliation, drive to zero-delta and land); head already smallest → the operator, attended prompt / unattended FAILED with the series enumerated — never another same-form round. **34** | none | none (lap A token cell: "none") | §6 KEEP "the narrowing route". Against §6's "25 (trend consult detail)" LEAVES figure: see **F2** — the field caveat has no registry key, and `NON-CONTRACTING` is a desk grade, not an emitted verdict |
| A23 | "That closes design; record findings never sustain a" | 1171-1194 (24 nb) | 1240-1263 | SPLIT | "an armed TRIPWIRE_FIRES routes to the NARROWING route (below)". Home: `ROUTES["TRIPWIRE_FIRES"]==narrow`. **2** | The never-sustain rule and its incident (F143, the prose held IN FORCE while UNAPPLIED); the mechanical enforcement at the RE-ENTRY seam; `sustain`'s PREDICATE (re-derives the prior round's finding classes from each finding's own scope opener, independent of the A-line summary — SUSTAIN_OK at one design-substance finding, SUSTAIN_DENIED when every finding is record/instrument-class, SUSTAIN_NOT_APPLICABLE outside a [BIT] round); the latest-RESOLVED-round-only rule and the `live_round` field; the verdict quoted in the round-open line; "a round dispatched over SUSTAIN_DENIED is exactly the class this gate exists to catch"; the same seam running `tripwire` beside `sustain`, its verdict quoted the same way; the two negative modulations no token carries — TRIPWIRE_FIRES "never blocking round-open on its own tag", and TRIPWIRE_SILENT reason "unarmed" being "silently informational, never a hold". **22** | none | SUSTAIN_OK, SUSTAIN_DENIED, SUSTAIN_NOT_APPLICABLE (the predicate defines which is emitted when — tool semantics, not a route); TRIPWIRE_FIRES, TRIPWIRE_SILENT (both carry negative modulations the `narrow`/`proceed` tokens invert if read alone) | §6 LEAVES "20 (sustain/tripwire routes)" — measured 2, see F1; §1 `narrow`; brief's no-other-home rule for the predicate and the two modulations |

### Implementation — the closure gate

| id | anchor | range@3c041e5 | stale-range@769e7f2 | disposition | leaves (+ other home) | stays (target lines) | tokens-dropped | tokens-kept (why the page needs each) | basis |
|---|---|---|---|---|---|---|---|---|---|
| I3 | "The closure read runs through the record tool at each dispatch" | 1232-1240 (9 nb) | 1303-1311 | SPLIT | "CLOSURE_VOID bars every unit"; "CLOSURE_RECORD_MALFORMED bars every unit the same way — … unsound until repaired". Home: `ROUTES["CLOSURE_VOID"]==barred` (§1 barred: "denied by run state already in the record … nothing to book"), `ROUTES["CLOSURE_RECORD_MALFORMED"]==repair-from-verdict`. **3** | The invocation form and the with/without-`--unit` distinction (without it, a whole-record read), and the COMPOSE-SIDE causes of a void closure — a scopeless line, or a post-closure [INVALIDATED] line for an entry LIVE at the closure whatever its opener (the mis-scoped premise-kill). The desk needs the causes to avoid WRITING one; the route token says only that it is barred. **6** | CLOSURE_RECORD_MALFORMED | CLOSURE_VOID (the compose-side cause list is stated about it); CLOSURE_LIVE (the no-`--unit` form's normal answer, and the resume gate at :179-204 reads on it) | §6 KEEP "the closure predicate's compose-side semantics"; §6 LEAVES "30 (closure invocation/routes)" — measured 3 here |
| I4 | "Repair is APPEND-ONLY, by the literal token `corrects line <n>`" | 1241-1267 (27 nb) | 1312-1339 | KEEPS | — | Whole repair GRAMMAR: append-only, one token per line, composed from the verdict; the machine-token-versus-body-content split and each side's consequence (target superseded whole and RESTATED, re-carrying tag and scope, a tag or scope change through repair lints as its own violation, status changes are ordinary new lines; a body violation leaves the entry live, the correcting line opening `record: ` and shedding VIOLATIONS only — shedding acknowledges, never cleanses); ONE-PASS supersession; `corrects-nothing`; a target naming ANOTHER id barred while an id-unreadable violated line is claimable; flagged text still sitting in the file for foreign readers; then re-run. **27** | none | none (lap A token cell: "none") | §6 KEEP "write-side templates and forms"; the row holds no verdict name. See F3 |
| I5 | "CLOSURE_ABSENT means the gate is not open — the last A-line is" | 1268-1281 (14 nb) | 1340-1353 | SPLIT | The routing half — the gate-not-open state bars dispatch, "dispatch waits". Home: `ROUTES["CLOSURE_ABSENT"]==barred`, §1 barred ("resolution is the run's own machinery … waiting on the gate"). **2** | The gate PREDICATE, compose-side: last A-line neither [ZERO-DELTA] nor a [BIT] whose disposition set amends no design entry; P27's design-CONSEQUENCE-not-finding-PRESENCE reading (a terminal [BIT] round's findings may all discharge without touching a D-line and the gate reads that as SATISFIED); the one design-amending disposition that keeps it SHUT — a SCOPELESS D-class line landing after the [BIT] A-line, with both exclusions (`record:`-opened is bookkeeping; `unit U<k>`-scoped, `held:` included, is the per-unit machinery); the F118 incident. "Absent either, this is the normal state during a reopened design." **12** | none | CLOSURE_ABSENT — the whole predicate paragraph is written as what that verdict MEANS; the retained text reads on the name | §6 KEEP "the closure predicate's compose-side semantics"; §1 `barred` |
| I6 | "UNIT_HELD bars that unit on its unresolved hold entry" | 1282-1289 (8 nb) | 1354-1361 | SPLIT | "UNIT_HELD bars that unit on its unresolved hold entry"; "UNIT_UNKNOWN halts"; "UNIT_DISPATCHABLE lists the live amendment lines that travel" (the route half). Home: `ROUTES["UNIT_HELD"]==barred`, `ROUTES["UNIT_UNKNOWN"]==halt`, `ROUTES["UNIT_DISPATCHABLE"]==proceed`. **3** | The one-line survivor §3's membership note names explicitly: "re-run with the id read from the record, never a guess (a typo'd digit otherwise clears a hold silently)". And the BRIEF-COMPOSITION duty: the brief carries the tool's verdict line, the closing A-line quoted, the lock sha, and the listed amendments — never the raw criterion. **5** | UNIT_HELD, UNIT_DISPATCHABLE | UNIT_UNKNOWN — §3's note keeps its re-run sentence on the page, and the sentence is about that verdict | §3 membership note ("UNIT_UNKNOWN is `halt`; the one-line … survives as page prose"); §6 LEAVES closure routes |
| I7 | "The criterion the tool computes — its semantics are what" | 1290-1325 (36 nb) | 1362-1397 | KEEPS | — | Whole: the criterion as COMPOSE-SIDE semantics — "what the desk WRITES so the read comes out true"; the scopeless-line void and the stale-closure rule; `unit U<k>`-opening lines re-opening that unit and travelling as amendments (live lines only); `record:`-opening lines voiding and re-opening nothing and never invalidating an entry live at the closure; the clause-restatement scoping rule and both composed failure lines verbatim (the restatement dying under its own id opening `unit U<k>`, and the parent's clause disposition re-written as `record:` bookkeeping), with the reason no clause list points at a dead restatement and the unit's want surfacing as its gap; a restatement bearing wider on the design being SCOPELESS and voiding. **36** | none | none (lap A token cell: "none") | §6 KEEP, named verbatim: "the closure predicate's compose-side semantics ('what the desk WRITES so the read comes out true' — most of the 112)" |

### Implementation — the unit seam

| id | anchor | range@3c041e5 | stale-range@769e7f2 | disposition | leaves (+ other home) | stays (target lines) | tokens-dropped | tokens-kept (why the page needs each) | basis |
|---|---|---|---|---|---|---|---|---|---|
| I14 | "The unit runs: START, before any edit —" | 1397-1416 (20 nb) | 1466-1485 | SPLIT | (a) "UNIT_GATE_BLOCKED (a blocking record-gate verdict, the empty declaration included) and WRITE_SET_NAMES_TRACKER (the declared write-set names the tracker itself) halt the unit UNBUILT, and GATE_UNREADABLE (no parseable record verdict) halts the same way, fail-closed" — home `ROUTES["UNIT_GATE_BLOCKED"]==barred` (**CONDUCT DELTA, F5**), `ROUTES["WRITE_SET_NAMES_TRACKER"]==halt`, `ROUTES["GATE_UNREADABLE"]==halt`; (b) the other-START enumeration "UNIT_COLLISION …, HALT_STATE …, and any other START verdict (HALT_IGNORED_WRITESET, HALT_DIRECTORY_PATH, USAGE_ERROR, GIT_ERROR …) halt the unit UNBUILT" — home: a `ROUTES` entry each, with `ROUTES["UNIT_COLLISION"]==triage` (**CONDUCT DELTA, F5**). **8** | The invocation form; the gate-consult ARCHITECTURE (the write-set read from the record's declared lines through the record tool's `closure --unit` run as a subprocess, its verdict embedded verbatim as the `gate` field — closure, never sweep, is the unit gate's consult — so briefs never restate it); UNIT_START_CLEAN printing the resolved `write_set` as where the implementer reads the paths the unit owns; "UNIT_START_CLEAN makes every later modification the unit's own"; and the seam's fail-closed statement "no edit, no commit, no landing annotation". **12** | WRITE_SET_NAMES_TRACKER, GATE_UNREADABLE, HALT_IGNORED_WRITESET, HALT_DIRECTORY_PATH, USAGE_ERROR, GIT_ERROR (their START listing) | UNIT_START_CLEAN (the write-set/attribution semantics are stated about it); UNIT_GATE_BLOCKED and UNIT_COLLISION are dropped HERE only under F5's unresolved delta — if the build lane keeps the page's halt reading, both names stay | §6 LEAVES "60 (unit)" — measured 8 here, see F1; F5 for the two deltas |
| I15 | "COMMIT — `unit-commit --tracker <tracker> --unit U<k>" | 1417-1426 (10 nb) | 1486-1495 | SPLIT | "UNIT_START_MISMATCH: the start sha is no ancestor of HEAD, or a foreign commit touched the declared write-set since it". Home: `ROUTES["UNIT_START_MISMATCH"]==halt`; the two conditions are the verdict's own diagnosis. **2** | The COMMIT invocation form and the PASTE rule (`--start-sha` from the START verdict line, never re-typed — the drop-argument rule's hop); "same gate consult and halts as START"; and the §4-class COMMIT-side modulation of every halt: a halt here leaves the unit's edits in the tree, so they are NAMED as poisoning the write-set for the re-dispatch. **8** | UNIT_START_MISMATCH | none | §6 LEAVES unit routes; the poisoning modulation is §4 item 2's class (seam-dependent disposition), the paste rule is a template |
| I16 | "Verdicts: UNIT_COMMITTED → landing annotation with its sha." | 1427-1457 (31 nb) | 1496-1526 | SPLIT | (a) the "Verdicts:" label and "UNIT_COMMITTED →" — home `ROUTES["UNIT_COMMITTED"]==proceed`; (b) UNIT_COMMIT_COLLISION's route half ("report, nothing committed") — home `==halt`; (c) UNIT_COMMITTED_EXTRAS / UNIT_COMMITTED_RESIDUE's route half ("landed their sha … but carry a finding the desk books as a `record:` F-line from the pasted verdict") — home `==book-and-continue`, whose §1 paragraph states exactly that; (d) the closing name list "ADD_FAILED, COMMIT_FAILED, GIT_ERROR are the common members, the global catch-all rule covers the rest" — home: a `ROUTES` `==halt` entry each, and §5 test 1 replaces "the global catch-all rule covers the rest". **8** | The landing-annotation duty (§1 `proceed` keeps it as the seam's own page principle, with `landing-missing` as its backstop). UNIT_COMMIT_COLLISION's RATIONALE: the commit seam re-reads column one, ANY staged state halts because column one cannot attribute a staged add, and a blocked prior attempt's leftover never reaches this seam (the re-dispatch meets it at START); plus the edits left in the worktree and named as poisoning the write-set. **§4 item 6 verbatim**: UNIT_NO_DIFF_VS_HEAD runs the residue check — the brief's symbol-anchored criterion, the discriminator, never an exit code — and reports already-present, the landing annotation carrying `already-present` in place of a sha, with HALT_IGNORED_WRITESET re-firing here routed as blocked and its ignored-path diagnosis kept from the verdict line. **§4 item 4's gap sentence**: HALT_MISSING_PATH → a write-set path the unit never populated, reported as a gap, nothing landed. **§4 item 3's distinction**: HALT_STATE (an operation the operator began mid-unit) distinct BY VERDICT from BLOCKED_CONTENTION (index.lock held through five spaced attempts, the verdict carrying the error text and whether the lock file remains) — I18's triage reads on this distinction. The per-verdict CONTENT rules: extras are the lock's mis-composed-pathspec rule (recorded, brief exclusion, never reverted), residue is write-set divergence after the commit, triaged like a collision. **23** | ADD_FAILED, COMMIT_FAILED, GIT_ERROR (their unit listing) | UNIT_COMMITTED (the landing-annotation duty); UNIT_COMMIT_COLLISION (the column-one rationale); UNIT_NO_DIFF_VS_HEAD (§4 item 6); HALT_IGNORED_WRITESET (its seam-specific re-firing reading); HALT_MISSING_PATH (§4 item 4); HALT_STATE and BLOCKED_CONTENTION (§4 item 3's distinction, consumed at I18); UNIT_COMMITTED_EXTRAS, UNIT_COMMITTED_RESIDUE (their content rules) | §6 LEAVES "60 (unit)" — measured 8 here, see F1; §4 items 3, 4, 6; §1 `proceed` and `book-and-continue` |
| I17 | "EVERY non-committed exit pastes its verdict line in the unit's report" | 1458-1468 (11 nb) | 1527-1537 | KEEPS | — | Whole: every non-committed exit pastes its verdict line and leaves the tree exactly as the tool left it — never silence; the desk books each non-landed return as a [VERIFIED] F-line opening `record:` (basis the pasted verdict line; a unit return decides nothing — voids nothing, re-opens nothing), never through the gap triage; PLUS the HOLD ENTRY template verbatim — `- D<n> [AUTO-ACCEPTED] unit U<k> held: <reason> — basis: <that F-line's id>` — and why it exists (the tag surface carrying an unlanded unit into the close's enumeration; without it a held unit reaches Verify invisible to every gate). **11** | none | HALT_MISSING_PATH — the gap-report EXCEPTION to the never-through-gap-triage rule is stated about it | §6 KEEP "write-side templates and forms (… hold entry …)" and "the verdict-line booking principle" |
| I18 | "Clearing a held path is DESK work, decided by provenance" | 1469-1500 (31 nb) | 1538-1568 | KEEPS | — | Whole: clearing is DESK work decided by PROVENANCE (record plus task system showing the dirt is the run's own — a stopped or dead dispatch, sibling or the same unit's prior attempt, whose write-set covers the path, its clean START check readable in that dispatch's output); clearing BY SHAPE with each command's exit read — tracked path restores (`git restore --source=HEAD --staged --worktree -- <tracked paths>`), untracked leftover DELETED, staged-NEW `git rm -f`-ed, with the reasons (restore cannot touch what HEAD lacks; a mixed call fails whole, restoring nothing; restore reaches neither half of a staged-new); ONE clearing attempt, a re-collision held as operator state, no clearing loop; a path without that provenance held as operator state; the CLEARED-LINE template verbatim — `- D<n> [COMMITTED] unit U<k> cleared: <path> — basis: <the reply>` — opening `unit U<k>` because the natural scopeless phrasing voids the whole closure; the BLOCKED_CONTENTION triage on the same provenance (siblings live → re-dispatch after their landings; none live and the verdict says the lock file remains → the stale `.git/index.lock` removed on that provenance alone, else surfaced); the HALT_STATE re-dispatch and its unattended close route. **31** | none | BLOCKED_CONTENTION (§4 item 3 routes it `triage` and names THIS as the disposition source the token points at); HALT_STATE (§4 item 2's attended/unattended seam sentence) | §6 KEEP, named verbatim: "the clearing-by-shape judgment and its provenance rule"; plus the cleared-line template; §4 items 2 and 3 |

### Close

| id | anchor | range@3c041e5 | stale-range@769e7f2 | disposition | leaves (+ other home) | stays (target lines) | tokens-dropped | tokens-kept (why the page needs each) | basis |
|---|---|---|---|---|---|---|---|---|---|
| K3 | "After the close is appended and Status written, pin the" | 1638-1652 (15 nb) | 1712-1726 | KEEPS | — | Whole: pin the delivered record with `lock-commit --tracker <path> -m <close message>` over the tracker alone (post-lock appends otherwise never enter git), its verdict line delivering with the close. **§4 item 1's benign-reading sentence verbatim**: HALT_NO_CHANGES HERE means the record is already pinned (a re-run after an ambiguous first attempt) — benign, delivered as-is. And the seam's OVERRIDE of the `halt` token: a halt here never blocks delivery — the close delivers UNPINNED with the halt's verdict line named in its deviations, attended the clearing reply gets one pin retry, and since there is no later seam to catch an unpinned delivery the deviation line IS the record of it; skipped only where the run never had a pinnable tracker. **15** | none | HALT_NO_CHANGES (§4 item 1 — the same verdict reads as a halt at the lock seam and benign here; the emission cannot know which, so the page must); HALT_STATE (the exemplar of the never-blocks-delivery override) | §4 item 1, named; §4 item 2's class for the delivery override — a `halt` token that stopped this seam would lose the close |

---

## Verifier

**1. Row count: 28 in, 28 out.** Lap A's table holds exactly 28 rows
whose final mark cell is `B`, counted by script over its
pipe-delimited rows: T4 T5 T6 T7 T9 T10 R13 R27 R31 R32 R38 S3 S4 S17
S18 A17 A23 I3 I4 I5 I6 I7 I14 I15 I16 I17 I18 K3. All 28 appear
above; none added, none merged, none split.

*Correction to the brief's Background 1:* lap A's table has **156**
clause data rows, not 183. Measured: 196 lines start `|`, 13 are
separators, 13 are header rows (170 remain), of which 14 belong to the
per-section SUMMARY table. 183 = 196 − 13, i.e. headers counted as
data. The `B` count is unaffected.

*Correction to the brief's Background 1, second half:* the 28 are NOT
all rows "lap A deliberately did not touch" — 15 of them carry lap A
disposition TIGHTEN (T4 T5 T6 T7 T9 T10 R13 R27 R31 R32 R38 S3 S4 A17
I4) and 13 KEEP. Lap A's own rule 3 permits tightening a `B` row where
its text restates another page sentence. Every disposition above was
therefore taken against the PINNED PAGE TEXT, never against lap A's
must-survive cells.

*Correction to the brief's Background 2:* the "+10 operational lines"
figure is the staleness of the DESIGN's ranges, not lap A's. Measured
by the CLAUDE.md Verify awk: `769e7f2` (lap A's pin) 1766 operational
/ 1803 total; `0775b92` (the design's base) 1628 / 1717; `3c041e5`
(this table's pin) 1638 / 1727. Lap A's ranges are stale by the whole
lap A compression — **−128 operational lines, distributed
non-uniformly** — which is why every row above was re-anchored by
quoted text.

**2. Every PRECIPITATES and SPLIT row names an other-home.** 0
PRECIPITATES, 16 SPLIT; each SPLIT row's `leaves` cell names a
`ROUTES["<VERDICT>"] == <token>` entry (or, for T7's catch-all
sentence, the added vocabulary section's `unrouted` paragraph, §1).
No row leaves anything to an unnamed home.

**3. Re-anchoring verified at the pinned page.** Each row's resolved
range quoted from `3c041e5` — first line of the range and the tail of
its last non-blank line:

| id | range@3c041e5 | first line at that range | last non-blank line, tail |
|---|---|---|---|
| T4 | 73-79 | `Every invocation — usage errors included (USAGE_ERROR); ` + "`--help`" | `…code is routing convenience, never the result.` |
| T5 | 80-91 | `Happy paths route in their own sections; ` + "`lint` alone answers ad-hoc" | `…per-unit gate stays ` + "`closure --unit`." |
| T6 | 92-103 | "`trend`" + ` returns TREND_COMPUTED / TREND_NO_ROUNDS: per-round F-LINE` | `…from the verdict's violation lines).` |
| T7 | 104-112 | `ANY verdict no section names is a halt for the seam that ran it —` | `…uncommitted.` |
| T9 | 120-128 | `At run start, before any design work: ` + "`preflight --tracker <path>`;" | `…answer, an error exit of any read still halts.` |
| T10 | 129-137 | `PREFLIGHT_UNPINNABLE_TRACKER = the repo ignores the tracker path and` | `…re-runs.` |
| R13 | 272-284 | `Exhaustion never continues silently: attended it forces the operator` | `…The attack), never to another same-form round.` |
| R27 | 421-434 | `Run ` + "`lint`" + ` once header and head are written — a form defect found` | `…commits it).` |
| R31 | 462-478 | `A mistyped ` + "`SWEEP_EXEMPT:`" + ` fails safe — the hold it meant to net` | `…expect the lint to say so.` |
| R32 | 479-495 | `Beside the write-set declarator: a correction appended under a` | `…rammar makes reachable there, and there alone.` |
| R38 | 510-528 | `- a basis citing ANOTHER record's entries names the record (tracker` | `…invalidations.` |
| S3 | 641-660 | `[READY] is recordable only when the record sweeps clean: no entry's` | `…a claimed [READY] is the premature-call shape.` |
| S4 | 661-688 | `A declared exemption nets a matching hold out of the blocking set` | `…is never invisible.` |
| S17 | 809-843 | `(c) ` + "`lock-check --tracker <path> [--lock-set <path> …]`." | `…close's deviations unattended.` |
| S18 | 844-874 | `(d) ` + "`lock-commit`" + `, same arguments plus ` + "`-m`" + ` and one ` + "`--drop`" | `…as a ` + "`record:`" + ` F-line, routed like HALT_STATE.` |
| A17 | 1081-1114 | `The reply opening a repeat round — from the SECOND` | `…same-form round.` |
| A23 | 1171-1194 | `That closes design; record findings never sustain a` | `…ts threshold (the arming carrier, The record).` |
| I3 | 1232-1240 | `compliant and unattackable. The closure` | `… line broke the grammar, and the entry set the` |
| I4 | 1241-1267 | `closure computes is unsound until repaired. Repair is` | `…re-run;` |
| I5 | 1268-1281 | `CLOSURE_ABSENT means the gate is not open — the last A-line is` | `…design). Absent either, this is the` |
| I6 | 1282-1289 | `normal state during a reopened design; dispatch waits. UNIT_HELD` | `…e closing A-line quoted, the lock sha, and the` |
| I7 | 1290-1325 | `listed amendments — never the raw criterion. The criterion the` | `…(stop the siblings resting on it, let the rest` |
| I14 | 1397-1416 | "`--unit`" + ` flag). The unit runs: START, before any edit —` | `…T — no edit, no commit, no landing annotation.` |
| I15 | 1417-1426 | `COMMIT — ` + "`unit-commit --tracker <tracker> --unit U<k>" | `…the declared write-set since it.` |
| I16 | 1427-1457 | `Verdicts: UNIT_COMMITTED → landing annotation with its sha.` | `…blocked, uncommitted edits named — they poison` |
| I17 | 1458-1468 | `the write-set for the re-dispatch. EVERY non-committed exit` | `…the gap path's pattern; without it a held unit` |
| I18 | 1469-1500 | `reaches Verify invisible to every gate). Clearing a held` | `…close's deviations.` |
| K3 | 1638-1652 | `After the close is appended and Status written, pin the` | `…the desk's final act, so the` |

A range opening mid-sentence (I3, I4, I6, I7, I14, I15, I17, I18, K3)
is lap A's own convention: a shared line belongs to the LATER row, so
the leading fragment is the PRECEDING row's tail. Each row's handle
begins within the first line shown.

**Anchoring method, stated as the instrument's basis.** All 156 lap-A
handles were matched against the pinned page with whitespace runs
(line breaks included) normalised to one space. 133 resolved; 23 did
not (lap A rewrote their openings). Of the 23, exactly two are `B`
rows — T10 and R27 — and both were hand-anchored on their surviving
text (`PREFLIGHT_UNPINNABLE_TRACKER = the repo` at :129; `Run \`lint\`
once header and head` at :421), each a unique single-line hit. Of the
resolved 133, two had multiple hits (I9 ×2, K0 ×3) and one resolved
non-monotonically (I9); none is a `B` row, and the only `B` row whose
END depended on an unresolved successor was R13, whose successor R14
was located directly (`Housekeeping` at :285), giving R13 = 272-284.

**4. The totals row and the divergence.**

| | measured |
|---|---|
| pinned page operational lines (`3c041e5`, Verify awk) | 1638 |
| non-blank lines inside the 28 `B` rows | 510 |
| LEAVING the page | **66** |
| STAYING | **444** |
| page after lap B, before the added vocabulary section | 1572 |
| design §6's ADDED vocabulary section (its estimate, not measured) | +40 |
| **projected post-lap-B operational lines** | **≈1612** |
| design §6's estimate of leaving mass | ~230 |
| design §6's projected post-lap-B page | ~1440 |
| **divergence** | **−164 leaving; +172 page** |

The estimate and the measurement are over DIFFERENT partitions of
different objects, so the shared coordinate that makes the comparison
mean anything is established in the next section, not assumed here.

## Span-vs-row coverage map

Design §6's ~230 is a sum over eight hand-drawn SPANS measured at
`0775b92`; this table's partition is lap A's 28 rows, anchored at
`769e7f2` and re-resolved at `3c041e5`. Different partitions of
different objects, so the comparison needs a shared coordinate before
it means anything. The coordinate is established here: **every §6
span re-expressed as `3c041e5` line numbers**, then intersected with
the 28 resolved row ranges.

**Re-expressing the spans.** `git diff -U0 0775b92 3c041e5 --
plugin/skills/statiker/SKILL.md` has three hunks: `@@ -254,7 +254,18`
(+11), `@@ -268,4 +279,3` (−1), `@@ -1184 +1194` (substitution). So
lines ≤253 are unshifted and lines ≥272 are shifted +10 — the whole
of §6's "+10" lands between them [measured].

| §6 span | at `0775b92` | at `3c041e5` | span nb | §6 est. leaving | `B` rows covering it | measured leaving | uncovered block |
|---|---|---|---|---|---|---|---|
| tools residue | 80-111 | 80-111 | 30 | ~22 | T5 T6 T7 | 15 | none |
| record gate | 179-204 | 179-204 | 25 | ~15 | **none** | — | 179-204 (25 nb) — lap-A R4 (`§5`), R6 |
| [READY] sweep | 631-649 | 641-659 | 19 | ~7 | S3 | 4 | none |
| lock routes | 799-864 | 809-874 | 66 | ~54 | S17 S18 | 12 | none |
| attack repeat-round | 1071-1120 | 1081-1130 | 50 | ~25 | A17 | 0 | 1115-1130 (16 nb) — lap-A A18 |
| sustain/tripwire seam | 1163-1196 | 1173-1206 | 34 | ~20 | A23 | 2 | 1195-1206 (12 nb) — lap-A A24 |
| closure predicate | 1223-1335 | 1233-1345 | 112 | ~30 | I3 I4 I5 I6 I7 | 8 | 1326-1345 (19 nb) — lap-A I8 |
| unit routes | 1386-1489 | 1396-1499 | 104 | ~60 | I14 I15 I16 I17 I18 | 18 | 1396 (1 nb) |
| **span totals** | | | **440** | **~233** | | **59** | **72 nb uncovered** |

**`B` rows inside NO §6 span** (10 of 28): T4, T9, T10, R13, R27,
R31, R32, R38, S4, K3 — 143 non-blank lines, contributing **7** to
the leaving total (T9 1, T10 4, R27 2; the other seven leave 0).

Grand total: 59 (inside spans) + 7 (outside) = **66 leaving**, the
totals row's figure.

The divergence concentrates in four spans — lock −42, unit −42,
attack/trend −25, sustain −18. F1 and F2 give the causes; F4 gives
the 72 uncovered lines, which are not this table's to disposition.
The dispositions above were not adjusted toward the estimate.

*One caveat on the uncovered blocks.* Their lap-A row names come
from the same handle-resolution pass; lap-A row I9 resolved
non-monotonically (two hits, first at :1205) and overlaps both the
sustain and closure tails, so I8/A24 are named as the rows whose
resolved ranges cover those blocks, not as a claim about I9's true
position. No `B` row is affected.

## What this table does NOT settle

- **F4's gate span.** Whether design §6's record-gate leaving mass
  (~15 lines at :178-204) enters lap B needs a dispatcher decision;
  it is not in the 28-row object and is not dispositioned here.
- **F5's three conduct deltas.** PINNED_REWRITTEN (halt → surface),
  UNIT_GATE_BLOCKED (halt → barred), UNIT_COLLISION (halt → triage).
  The `tokens-dropped` cells for those rows assume the registry's
  reading wins; if the page's reading wins, each name stays and the
  row's leaving count falls by 1-3 lines.
- **The added vocabulary section's size.** +40 is design §6's
  estimate, carried through unmeasured; T7's absorbed catch-all
  sentence and R31's and I4's one-phrase overlaps with the
  `repair-from-verdict` paragraph are counted as leaving/staying at
  their own sites, so the added section may run slightly longer than
  40.
- **Stage 2's actual rewrite.** Every `stays` target is a line count
  for text a build lane composes; no rewritten text is proposed here.

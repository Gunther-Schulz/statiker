# Triage: three-arm review harvest (2026-08-15)

Executes the BACKLOG entry "triage the three-arm review harvest"
(booked 2026-08-11). Source record: begehung repo,
`dev-notes/eval-begehung/2026-08-11/tier2-{with,without,sentence}.md`
(+ tier2-with-MAP.md). Every finding below was probe-executed by its
arm against HEAD-of-2026-08-11; premise re-checks here ran against
HEAD 2bb9830 (2026-08-15, desk greps quoted per row where they
decided a disposition).

Enumeration reconciled against the files' own lists — WITH: B1–B9 +
namespace note; WITHOUT: F1–F12 + the pattern; SENTENCE: A1–A5,
B1–B6, C1, NEW-1..3. All 38 dispositioned; merges keep every id.

## Dispositions

Legend: FIX→E<n> = new READY backlog entry; MERGED = folded into an
already-booked entry; PARK→P<n> = parked entry with named missing
design; PROSE-REST = accepted with named backstop, recorded here;
FIXED = already repaired at HEAD; DONE = fixed at the desk in this
triage's own commit.

- **T1 — verdict reach: gates report clean with no denominator.**
  ids: WITHOUT-F1 (blocking), SENTENCE-A1, SENTENCE-B2 (R-line
  count), SENTENCE-B6 second half (tracker path outside
  `.clippy/runs/` invisible). Cross-arm confirmed. Still open at
  HEAD (`grep '"entries"' statiker_record.py` → 0 hits).
  Disposition: FIX→E-A.
- **T2 — unknown unit id clears holds.** ids: WITHOUT-F2
  (blocking), SENTENCE-A2 (attack-8 N3's class, spelling half only
  closed). Still open (fullmatch at :855 is the only check;
  known_units computed at :965 but unconsulted). FIX→E-B.
- **T3 — byte policy never carried to the git tool.** ids:
  WITHOUT-F4 (high, drop-handshake unpasteable), SENTENCE-A3
  (paste-ready record line re-spells the byte). Still open (`say()`
  is a plain print, statiker_git.py:87-88). FIX→E-C.
- **T4 — absolute-path spelling certified parallel-eligible by
  `waves`.** ids: WITH-B3, WITHOUT-F10, SENTENCE-A4 (3/3 arms).
  MERGED into the booked begehung-harvest-2 entry, defect (b): its
  leading-`/` + whitespace positional lint halts every executed
  probe (all three arms probed the absolute spelling). Residual
  recorded, not booked: non-absolute cross-group aliases (symlink,
  case) were never probed by any arm — no executed evidence, no
  entry.
- **T5 — `quote` mutates report bytes via str.splitlines().** id:
  WITHOUT-F5. FIXED at 82ed13c (cmd_quote now uses split_lines,
  statiker_record.py:1278); the arms probed a pre-repair HEAD.
- **T6 — booked sha is not the unit's own commit.** id: WITHOUT-F9
  (blocking; single-arm). Landing annotation names a sibling's
  commit; extras computed against wrong diff. FIX→E-D.
- **T7 — `filter` accepts a stale sha with no signal.** id:
  WITHOUT-F11. Field-not-gate per the arm's own shape. FIX→E-E
  (bundled small set).
- **T8 — seal/queue/repo-key namespace is prose end to end.** ids:
  WITH-B1 (derivation ambiguous AND unimplemented, three defensible
  readings probed), WITH-B2 (queue has no consumption marker),
  WITHOUT-F7, SENTENCE-B5, WITH namespace note (undefined
  `artifacts/` + `.report` homes). SPLIT: the freeze-breach check
  (F7's decidable half — any F/D/R line after a live [DISPATCHED]
  A-line) is mechanical → FIX→E-F; the namespace itself (which tool
  owns repo-key, consumption-marker form, artifact/report homes)
  needs design → PARK→P1.
- **T9 — gate verdicts never bind to the transactions they gate.**
  ids: WITH-B8 (lock commits over SWEEP_HOLDS), WITH-B9 (blocking:
  UNIT_COMMITTED over CLOSURE_VOID — forcing point 4's own
  invariant, gate present but unconsulted), WITHOUT-F3 (blocking:
  START↔COMMIT unlinked, operator's unstaged draft committed as the
  unit's own), WITHOUT-F12 (write-set may name the tracker).
  Common structural root: the git tool's unit seam has no --tracker
  and no way to consult the record gate. PARK→P2 (named missing
  design: how the git tool learns/consults the record gate —
  flag + import vs subprocess vs pasted verdict token; the
  red-first pairs are stated in the arms' texts and travel with the
  entry).
- **T10 — a NEW entry at an id below its class's max passes every
  gate.** id: WITH-B4. Computable slice honest per the arm
  (evidence line, never a halt — id reuse for status change is the
  design). FIX→E-E.
- **T11 — clippy-stats contract rests on a dated hand-read —
  HOLDS.** ids: WITH-B5, SENTENCE-B6 positive half. Both arms
  independently re-read the live source 2026-08-11; every claim
  held. PROSE-REST: the dated anchor comment
  (statiker_record.py:53-58) stays the backstop; re-read on the
  next fire-rate review.
- **T12 —** folded into T1 (E-A carries the tracker-path lint).
- **T13 — no reconciliation of enumerated units against
  landings.** id: WITH-B6. PROSE-REST with the arm's own named
  backstops: the verify brief's per-R NOT-EXERCISED demand plus
  `waves`' UNPLANNABLE on write-set-less units.
- **T14 — header fields beyond Status/Phase are uninstrumented.**
  ids: WITHOUT-F8, SENTENCE-B3 (irreversible/Mode — the
  damage-limiting rule, no instrument on either half), SENTENCE-B4
  (Budget — exhaustion enforcement is desk memory in the unattended
  mode), WITH-B7 (version provenance has no home; the beat-the-books
  record attributes rounds to a version ~38 releases stale). SPLIT:
  the computable slice (Budget count vs trend's rounds, Mode
  surfacing via the late_intent pattern, irreversible-literal hold
  at closure --unit) → FIX→E-G; version continuation needs a header
  field the Status/Phase-only rule currently forbids → PARK→P3.
- **T15 — detached HEAD / linked-worktree cwd defeat the pin
  silently.** id: WITHOUT-F6. FIX→E-H (field-not-gate, F11
  precedent: preflight verdict carries branch state, SKILL routes
  it).
- **T16 — append-only (forcing point 1) has no instrument.** id:
  SENTENCE-B1 (in-place [PENDING]→[VERIFIED] rewrite under a pin →
  SWEEP_CLEAN; git diff vs pin shows 1+/1-). FIX→E-I (`pinned`
  subcommand asserting pure-append against the pin).
- **T17 — `filter --out` into an unwritable dir books as tool
  defect.** id: SENTENCE-A5 (PermissionError → INTERNAL_ERROR where
  siblings route USAGE_ERROR). FIX→E-E.
- **T18 — statiker_record.py docstring contradicts its own inline
  comment on the write-set form.** id: SENTENCE-C1. Confirmed at
  HEAD (the stale "no literal write-set record-line form" NOTE
  stands in the docstring; :471-472 / :499 citations drifted).
  FIX→E-E.
- **T19 — module-level failure defeats the verdict-line contract.**
  id: SENTENCE-NEW-1 (env float() at statiker_git.py:71, outside
  main()'s try → traceback, exit 1, no verdict). Same class as the
  booked harvest-2 defect (d) BrokenPipe — MERGED into that entry
  as case (d2), same write boundary. Residue recorded, not fixed in
  the lane: the Python-floor declaration (PEP-604 annotations die on
  3.9 import) has no obvious venue in a skill plugin; noted in P-rest
  below.
- **T20 — model-resolution chain is prose only.** id:
  SENTENCE-NEW-2. PROSE-REST with recorded trigger: no tool seam
  runs at dispatch time, so a mechanism would itself be a
  desk-remembered step (the non-event moved one hop); mechanize on
  the first observed misroute from a typo'd class key.
- **T21 — .pytest_cache/ absent from .gitignore.** id:
  SENTENCE-NEW-3. DONE in this commit (one line).
- **T22 — the pattern: repairs land at the fired seam, not its
  sibling; tests indexed one-per-incident; shared rules duplicated
  by hand across the two tools.** ids: WITHOUT "the pattern" +
  weaknesses 2-3, SENTENCE provenance-check paragraph. T3/T5 are
  its executed instances. PROSE-REST with recorded trigger: the
  attack-9 recommendation (one shared path-grammar function consumed
  by both tools) already sits in dev-notes; extract it the next
  time a carry-across defect fires — a third instance indicts the
  structure, not the instance.

## Prose-rest register (accepted, with backstops/triggers)

- T11 clippy-stats hand-read: backstop = dated anchor comment;
  re-read at next fire-rate review.
- T13 unit/landing reconciliation: backstop = verify brief per-R
  demand + UNPLANNABLE.
- T19-residue Python floor: undeclared; venue question (plugin has
  no python_requires seam). Revisit if a public install is ever in
  scope.
- T20 models chain: mechanize on first observed misroute.
- T22 shared path-grammar extraction: on the next carry-across
  defect.

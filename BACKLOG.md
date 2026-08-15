# Statiker — backlog

Future work graded by decision-completeness (operator-corpus file
roles). PLAN.md stays the design record; entries here are work items,
and a SKILL.md change stays fire-born per CLAUDE.md — an entry can
build tooling, but a clause mint still needs its incident.

## Open

- **READY 2026-08-15 — E-A: verdicts carry their reach (entry
  count, head boundary, R-line count, tracker-path lint).**
  Provenance: triage T1 (three-arm WITHOUT-F1 blocking +
  SENTENCE-A1 + SENTENCE-B2 + SENTENCE-B6 second half; probes
  executed, arrangements in the arm files). Design, decided (the
  arms' shared fix shape): every record-tool verdict gains
  `entries: <n>`; an evidence line fires when entry-shaped lines
  sit in the head region; sweep/closure verdicts gain an R-line
  count from the head; lint emits an evidence line when the
  tracker path is not under `.clippy/runs/`. No gate semantics
  change; ES-1's exclusion untouched. Verifier, red-first: F1/A1's
  probe trackers (live [PENDING] above the first `## ` heading;
  no heading at all) must show entries: 0 where they showed bare
  CLEAN; heading-present control unchanged. Done: probes flip,
  full `pytest tools/` green. Write boundary: statiker_record.py,
  tools/test_statiker_record.py, tools/test_contract.py.

- **READY 2026-08-15 — E-B: an unknown `--unit` halts instead of
  reading UNIT_DISPATCHABLE.** Provenance: triage T2 (WITHOUT-F2
  blocking + SENTENCE-A2; attack-8 N3's class, spelling half
  closed at :855, referent half open). Design, decided: closure
  --unit consults the known-unit set the module already computes
  (known_units, waves_over_units) and returns its own verdict
  (UNIT_UNKNOWN, exit 2) for an id the record never names.
  Verifier, red-first: F2's probe battery (U11/U21/U7 over a
  tracker holding U1 HELD, U2 amended) — each read
  UNIT_DISPATCHABLE in the arm's executed probe (2026-08-11 arm
  file, arrangement quoted there); premise re-checked at HEAD
  2bb9830 (desk grep: form-only fullmatch at :855, known_units
  computed at :965, unconsulted between them) — the battery must
  halt them; U1→UNIT_HELD and U2→amendments stay. Done: battery
  green, full suite green. Write boundary:
  statiker_record.py, tools/test_statiker_record.py,
  tools/test_contract.py (new verdict row).

- **READY 2026-08-15 — E-C: the byte-level emit rule (ES-9) joins
  the git tool.** Provenance: triage T3 (WITHOUT-F4 high +
  SENTENCE-A3; both executed — the drop handshake is unsatisfiable
  by pasting, and the paste-ready record line re-spells the byte
  three ways). Design, decided: statiker_git.py emits via the
  record tool's emit() shape (sys.stdout.buffer, surrogateescape at
  byte level) so printed drop values and write-set paste lines
  carry the input's own bytes. Verifier, red-first: F4's
  caf\xff drop-handshake probe (pasting each printed spelling must
  LOCK_COMMITTED, not HALT_DROPS_STALE) and A3's caf\xe9
  unit-start paste-line probe (record line carries the byte
  intact); existing ASCII round-trip stays green. Done: probes
  flip, full suite green. Write boundary: statiker_git.py,
  tools/test_statiker_git.py.

- **READY 2026-08-15 — E-D: the unit sha comes from the commit's
  own output, never a later HEAD read.** Provenance: triage T6
  (WITHOUT-F9 blocking; hook-occupied window probe executed —
  UNIT_COMMITTED_EXTRAS booked a sibling's sha and a false extra).
  Design, decided (the arm's fix shape + the corpus verifier's-own-
  output rule): take the sha from the commit operation itself and
  read the landed diff at THAT sha, not at HEAD. Verifier,
  red-first: F9's post-commit-hook probe — verdict must name the
  commit carrying the unit's write-set, extras must be empty.
  Done: probe flips, full suite green. Write boundary:
  statiker_git.py, tools/test_statiker_git.py.

- **READY 2026-08-15 — E-E: small verdict/lint set (four one-shape
  fixes, per-fix red-first).** Provenance: triage T7/T10/T17/T18;
  probes executed by the arms 2026-08-11 (arrangements in the arm
  files), premises re-checked at HEAD 2bb9830 per item. Design,
  decided per item: (1) WITHOUT-F11: ARTIFACT_WRITTEN gains a
  field naming the tracker's newest commit beside the given sha
  (field, not gate). (2) WITH-B4: lint evidence line (never a
  halt) when a NEW id sits below its class's allocated max. (3)
  SENTENCE-A5: PermissionError on the `filter --out` write routes
  USAGE_ERROR like its two sibling cases (premise at HEAD: the
  missing-parent and is-a-directory branches sit at :1164-1173, no
  PermissionError branch follows — desk read). (4) SENTENCE-C1:
  the docstring's stale "no literal write-set record-line form"
  NOTE dies; drifted :471-472/:499 citations refreshed (premise at
  HEAD: the NOTE stands in the docstring while the inline comment
  near :907-913 calls the form normative — desk read). Verifier,
  red-first per item: (1) the arm's stale-lock probe — its two
  identical verdicts must now carry distinguishing fields; (2) the
  arm's gap-filling-id case must draw the evidence line, an
  ordinary status-change reuse must not; (3) the unwritable-dir
  probe (arm-read INTERNAL_ERROR) must read USAGE_ERROR; (4) grep:
  docstring and inline comment agree, citations resolve. Done:
  the four reds flip, full suite green. Write boundary:
  statiker_record.py, tools/test_statiker_record.py.

- **READY 2026-08-15 — E-F: append-freeze breach is decidable from
  the tracker — detect it.** Provenance: triage T8's mechanical
  half (WITHOUT-F7; probe executed — two entries appended under a
  live [DISPATCHED] A-line read SWEEP_CLEAN + LINT_CLEAN). Design,
  decided: sweep and lint fire on any F/D/R line appended after
  the latest A-line when that A-line is [DISPATCHED] with no
  resolving line (`trend` already parses the window). Verifier,
  red-first: F7's probe must fire; a resolved-A-line control and a
  queue-landed-before-outcome control stay clean. Done: probe
  flips, full suite green. Write boundary: statiker_record.py,
  tools/test_statiker_record.py.

- **READY 2026-08-15 — E-G: the computable header-field slice
  (Budget, Mode, irreversible).** Provenance: triage T14's
  mechanical half (WITHOUT-F8 + SENTENCE-B3 + SENTENCE-B4; probes
  executed — a header with neither field and no V-line reads
  LINT_CLEAN; `irreversible`/`Mode:` appear in no script or
  suite). Design, decided: closure --unit returns a hold when the
  unit's scoped entries carry the irreversible literal and the
  header's Mode is unattended (UNIT_HELD's literal-read pattern);
  sweep/closure verdicts surface the Mode line (late_intent
  pattern); sweep emits an evidence line when trend's resolved-
  round count meets/exceeds Budget. First build step: verify the
  literal forms against SKILL.md's own sentences (:441-450,
  :475-477, :161-168) before pinning the reads. Verifier,
  red-first: one probe per instrument (irreversible+unattended
  must hold; Budget-exhausted tracker must show the evidence
  line); attended and under-budget controls stay clean. Done:
  probes flip, full suite green. Write boundary:
  statiker_record.py, tools/test_statiker_record.py,
  tools/test_contract.py if a verdict is added.

- **READY 2026-08-15 — E-H: preflight reports branch state.**
  Provenance: triage T15 (WITHOUT-F6; both probes executed —
  detached HEAD and a linked-worktree cwd each ran the full
  transaction chain onto no branch, silently). Design, decided
  (field-not-gate, the F11 precedent): the preflight verdict
  gains `branch: <name|none>` plus a linked-worktree marker;
  routing stays SKILL.md's (no new halt member). Verifier,
  red-first: F6's two probes must surface branch none / worktree
  in the verdict; a normal checkout shows its branch. Done: probes
  flip, full suite green. Write boundary: statiker_git.py,
  tools/test_statiker_git.py.

- **READY 2026-08-15 — E-I: `pinned` — the append-only
  instrument.** Provenance: triage T16 (SENTENCE-B1; probe
  executed — an in-place [PENDING]→[VERIFIED] rewrite under a pin
  reads SWEEP_CLEAN while `git diff --stat <pin>` shows 1+/1-).
  Design, decided (the arm's shape): a record-tool subcommand
  `pinned --tracker P --sha S` asserting the working tracker is a
  pure append over the pinned version (old content a prefix of
  new, at byte level per ES-9); verdict pair
  PINNED_APPEND_ONLY / PINNED_REWRITTEN with the first divergent
  line as evidence. Verifier, red-first: B1's rewrite probe must
  read PINNED_REWRITTEN; a genuine append and a byte-identical
  tracker read PINNED_APPEND_ONLY. Done: probes flip, full suite
  green, contract battery rows added. Write boundary:
  statiker_record.py, tools/test_statiker_record.py,
  tools/test_contract.py.

- **PARKED 2026-08-15 — P1: the seal/queue/repo-key namespace
  needs a design decision before any mechanism.** Provenance:
  triage T8 (WITH-B1 executed: three defensible derivations of one
  prose sentence, live directory matches only one; WITH-B2: a
  consumed queue is byte-identical to an unconsumed one and its
  header instructs re-landing; WITH namespace note: desks invented
  `artifacts/` and `.report` homes the spec never defines;
  WITHOUT-F7, SENTENCE-B5: zero hits for the namespace in scripts
  and suites). Missing design, named: which tool owns repo-key
  derivation (or whether SKILL.md instead pins the exact command),
  the queue consumption-marker form, and lifecycle homes for the
  two invented namespaces. The freeze-breach check is NOT parked
  (E-F).

- **PARKED 2026-08-15 — P2: gate verdicts bind to the transactions
  they gate (the unit seam).** Provenance: triage T9 (WITH-B8:
  lock-commit LOCK_CHECK_CLEAN over SWEEP_HOLDS; WITH-B9 blocking:
  UNIT_COMMITTED over CLOSURE_VOID — forcing point 4's invariant
  with the detecting gate in the same toolchain, unconsulted;
  WITHOUT-F3 blocking: START↔COMMIT unlinked, an operator's
  unstaged draft committed as the unit's own; WITHOUT-F12: a
  write-set may name the tracker itself — all executed). Missing
  design, named: how the git tool learns and consults the record
  gate — a --tracker flag plus import vs subprocess vs a pasted
  verdict token — and what links START to COMMIT (the lock's
  --drop handshake is the in-repo precedent). The arms' red-first
  pairs travel with this entry (with/without files, B8/B9/F3
  sections).

- **PARKED 2026-08-15 — P3: version provenance needs a header-field
  decision.** Provenance: triage T14 (WITH-B7 executed: the
  beat-the-books record attributes cycles 10-11 to a version ~38
  releases stale; structural — Status/Phase are the header's only
  mutable fields, so a run spanning releases has nowhere to write
  the truth, while CLAUDE.md makes spanning routine and the trial
  grades arms on these records). Missing design, named: a mutable
  version/continuation field vs a new line class vs accepting the
  gap — contradicts the Status/Phase-only rule, so it is a SKILL.md
  design decision (fire-born discipline satisfied: incident logged
  in the arm file + triage record).

## Done

- 2026-08-15 — **harvest lane shipped: splitlines class + begehung-
  harvest 2 + worktree-add containment** (sonnet dispatch, brief
  docs/directives/2026-08-15-harvest-lane-brief.md; dispatcher's own
  verification: full suite 307/307, done-greps 0 hits). Commits:
  9fa8d8e (splitlines class closed in test_contract.py +
  test_statiker_git.py readers, shared split_lines helper,
  separator red-first cases); 8b3438e (0.2.62 bump — GAP 1: the
  desk's pushed 0.2.61 bump had consumed the hook's unpushed-batch
  exemption, bump ownership extended to the lane); 606c04a
  (harvest-2 (a) shed gated by REPAIR_FORMS class, (b) write-set
  path-field positional lint with INVALIDATED-tag exemption
  [accepted deviation — avoided regressing an existing fixture,
  both probes still lint], (c) trend windows anchored at own
  [DISPATCHED] lines, (d)/(d2) BrokenPipe + bad-env verdict at
  exit 3); ed3071c (worktree-add probes every enclosing repo from
  the target's PARENT + as-named/real agreement, two SKILL.md
  reach-exception sentences deleted); 81f2cf6 (GAP 2: probe B did
  not flip under the booked fix shape — tag-literal-in-body is
  genuinely bookkeeping-classed — desk redesign: owner-conditioned
  shed for that code only, repair field states the hold for
  owner-less targets; ES6 test re-vehicled to
  superseded-block-form to keep asserting its intended claim).
  All red-first arrangements stash-proven with pasted output (lane
  report + commit messages). NOTE: the SKILL.md edit (ed3071c) is
  release-review-owed — one fresh-context opus review before the
  pin moves (CLAUDE.md skill-edit experiment, three releases).

- 2026-08-15 — **three-arm review harvest triaged** (booked
  2026-08-11 as ~25 findings; final count 38 raw ids across the
  three arm files). Full disposition table with per-finding bases:
  dev-notes/triage-three-arm-2026-08-15.md. Reconciled against the
  files' own enumerations (WITH B1-B9+note, WITHOUT F1-F12+pattern,
  SENTENCE A1-A5/B1-B6/C1/NEW-1..3), duplicates merged with both
  ids kept. Outcome: 9 new READY entries (E-A..E-I), 3 PARKED with
  named missing design (P1-P3), 2 merged into the booked
  harvest-2 entry (absolute-path class + NEW-1), 1 already fixed
  (WITHOUT-F5, 82ed13c), 1 fixed at the desk (.pytest_cache
  gitignore), 5 prose-rest with named backstops/triggers (register
  in the triage record).

- 2026-08-11 — **begehung-harvest F1/F3/F4 repaired + supplements**
  (opus lane: a288a42 contract battery drives the worktree lane +
  GIT_SUBCOMMANDS derived from the parser; 82ed13c quote uses
  split_lines; 2eb6b59 RECORD_SUBCOMMANDS derived + record fixture
  reader splits on "\n" with a standing separator case; desk half
  84de7c5 Verify-line + F1b). Verification, WHOLE suite
  (`python3 -m pytest tools/ -q`, dispatcher's own run): 286
  passed, 0 failed — the four-commit contract red is closed.
  Red-first three-arm proofs per repair in the lane report;
  restated-set blindness now measured on BOTH tools (n=2).
  Incident, fully reverted in-lane: a U+2028 degraded to a plain
  space in a tool payload and a single-char replace hit 30323
  sites — recovered by checkout, lessons in the lane report
  (expected-count assertion before single-char replaces; invisible
  chars constructed from escapes, never passed literal).


- 2026-08-11 — **worktree subcommands (`worktree-add`/`worktree-remove`)
  shipped** (da8fb76, sonnet dispatch; LANE battery
  tools/test_statiker_git.py 99/99, red-first via stash-proof — all
  7 new tests red against old code; git's own worktree semantics
  verified empirically first). The CONTRACT battery
  (test_contract.py) went red in this same commit — three new
  verdicts undriven — and stayed red four commits; found by the
  0.2.60 begehung harvest (F1), repaired there. Closure lines name
  WHICH battery from here on. New halt member PATH_INSIDE_REPO
  (reported as deviation, accepted). SKILL.md provisioning sentence
  swapped to cite the subcommands (desk, same batch).

- 2026-08-11 — **write-set near-miss lint shipped** (c2c5baf, sonnet
  dispatch; battery 173/173, red-first — four misspelling variants
  read LINT_CLEAN and did not block closure under old code, violate
  and block under new). Class `write-set-near-miss` in
  MACHINE_TOKEN_CODES + CLOSURE_BLOCKING_CODES, mirroring
  scope-near-miss; UNIT_WRITE_SET_RE untouched.


- 2026-08-11 — **blast-radius clause minted into the attack block**
  ((hypothesis) provenance class, operator GO; adjacent non-statiker
  incident as class evidence — full lineage in dev-notes
  OBSERVATIONS 2026-08-11). Residue, carried to the next fire-rate
  review: validation criterion — the clause draws >=1 real
  blast-radius finding across attack rounds, else cut. Build-time
  verifier carried with it: a design with a known un-enumerated
  co-consumer must draw the finding from a fresh round (red), the
  same design with the search recorded must not (green).

- 2026-08-11 — **attack-round batching: realized in the 0.2.57
  series** (eb6ab88 batched rounds with per-design worktrees and
  per-design death; b26fb93 follow-through) — the entry's design
  landed via the 0.2.57 review loop rather than as its own commit.
  Done-criterion residue, carried to the first real multi-design
  moment: one real batched round recorded with complete per-design
  dispositions. Probe provenance: dev-notes/
  probe-attack-batching-2026-08-10.md.

- 2026-08-11 — **superseded waves/trend entry bodies dropped** per
  their own Done note's trigger (the line-form mint closed
  2026-08-10); bodies remain in git history.


- 2026-08-11 — **coverage-ledger review process ("lamp rotation")**:
  unparked same day by operator GO and built as its own thin skill,
  repo `Gunther-Schulz/begehung` (f376238, 0.1.0 trial; design core
  quoted authoritatively in its PLAN.md from this entry's body,
  founding incident in its dev-notes). The parked residual —
  statiker-framework absorption — is rebooked in begehung/BACKLOG.md
  with its trigger; nothing remains here.

- 2026-08-10 — **unit write-set record-line form**: fully realized —
  the form is normative in SKILL.md's Implementation section with
  the `waves`/`trend` seam cites (eb6ab88, 0.2.57 series) and
  `unit-start` prints paste-ready record lines, red-first with a
  round-trip through the real `waves_over_units` (7ba8c66, sonnet
  dispatch). Path spellings normalize in `waves` (b26fb93).
  Done-criterion residue, carried to the first real run: a live
  tracker carrying machine-printed lines partitioned with no
  UNPLANNABLE flag. Brief-defect note: the dispatch brief omitted
  the file-copy red-first rule; the executor's scoped stash was
  harmless here, recorded as the dispatcher's miss.

- 2026-08-10 — **hedge-language sweep over SKILL.md**: full-file
  desk read, 0.2.57 series. Cured: the description's trial-stage
  label, the tools paragraph's "booked mint" parenthetical (the
  line form now stated in Implementation), and the attack
  section's parallel-attacker/batching region (rewritten under
  the 14-finding review). Kept per instance: the 16 `(hypothesis)`
  markers (declared provenance class with logged validation
  criteria) and the Birth-class declaration's lifecycle wording
  (subject matter, not costume). Done-criterion grep: only those
  kept classes remain.

- 2026-08-10 — **wave derivation (`waves`) + round-trend instrument (`trend`)**: shipped `1eb4380` (subcommands + red-first batteries, sonnet dispatch) and `4b56648` (contract battery rows + SKILL.md verdict routing), version bump `8a8ce22` (0.2.56). Deviation from the booking: the waves entry's "premise verified against the grammar" note was FALSE — no unit write-set record-line form exists in the grammar (the realizing dispatch's gap 1); `waves` ships reading a composed convention, failing loud (UNPLANNABLE) on every real tracker until the line-form mint above lands. Entry bodies retained above under superseded markers until the mint closes; drop them with it.

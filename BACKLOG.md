# Statiker — backlog

Future work graded by decision-completeness (operator-corpus file
roles). PLAN.md stays the design record; entries here are work items,
and a SKILL.md change stays fire-born per CLAUDE.md — an entry can
build tooling, but a clause mint still needs its incident.
Composition checks, from lane R's two independent hits 2026-08-15:
an entry minting a NEW verdict name carries a SKILL.md-authorship
dependency (the parity battery is set-exact BOTH ways) — the entry
pre-names the exact route sentence, and it lands in the SAME
commit as the emitting code: a route minted ahead is a phantom
verdict, red within minutes (fired 2026-08-15); an emit without a
route is the F1 class. And an entry citing SKILL.md prose as a
record-line grammar quotes the backtick literal at MINT time, or
it is not decision-complete.

## Open

- **PARKED 2026-08-15 — P4: the irreversible-unit hold needs a
  record-line grammar minted first.** Provenance: SENTENCE-B3
  (the damage-limiting rule has no instrument on either half) +
  lane R gap 3 (first-build-step check executed: SKILL.md
  :441-450 says a unit "is tagged irreversible in its enumeration"
  as prose — no backtick-quoted literal exists, and the
  unattended-irreversible case "takes the hold entry", i.e. the
  text routes enforcement through the EXISTING UNIT_HELD
  mechanism; a bare-word scan would false-fire on "not
  irreversible" and on shared bodies). Missing design, named: mint
  an exact irreversible tag grammar into SKILL.md (the
  HOLD_EXACT_RE precedent) OR decide the hold-entry route suffices
  and record that as the standing shape — a SKILL.md design
  decision at a seam, fire-born discipline applies.

- **READY (small) 2026-08-15 — E-J: byte-level fidelity reaches the
  git tool's broken-pipe stderr fallback.** Provenance: lane G gap
  (report 2/4): `_stderr_fallback` still uses text-mode
  `print(file=sys.stderr)` while the record tool's version writes
  the buffer with surrogateescape — the E-C class, one path over.
  Fires only when stdout is already gone, so severity is low, but
  it is the third byte-policy carry-across instance (T22's counter:
  the shared-emit-helper extraction trigger is now met — extracting
  ONE emit/stderr helper both tools import satisfies this entry
  AND retires the class). Design, decided: mirror the record
  tool's byte-level stderr fallback, by extraction or by copy —
  extraction preferred per T22. Verifier, red-first: broken-pipe +
  non-UTF-8-path arrangement, fallback line carries the byte.
  Done: probe flips, full suite green. Write boundary:
  statiker_git.py, statiker_record.py (if extracting),
  tools/test_statiker_git.py.

- **READY (small) 2026-08-15 — E-K: EMIT_CONDUITS false-fire gets
  its declared exemption.** Provenance: lane G deviation 3
  (executed): the contract battery's conduit check is a bare-name
  AST match ({"failure_verdict","name","verdict"}, scope-unaware) —
  an ordinary local named `name` in branch_state() tripped it, and
  the lane's cure was a rename (workaround, not repair). Per the
  corpus guard rule, a check firing on legitimate work gets a
  declared, checked exemption — never a softened predicate or an
  avoidance habit. Design, decided (minimum): a comment at the
  EMIT_CONDUITS definition naming the false-fire class and the
  rename cure; better if cheap at build time: restrict the match to
  assignments that reach a finish()/say() call. Verifier: the
  battery stays green on the current tree and still fails on a real
  conduit rename (existing red case re-run). Done: comment (or
  scoped match) landed, battery green both directions. Write
  boundary: tools/test_contract.py.

- **READY (small) 2026-08-15 — E-L: requirement-head detection
  survives a leading `## ` head heading.** Provenance: relay 1
  (cycle-12 resume report, desk-executed, tool source verified at
  the meta desk): the beat-the-books tracker's `## Requirement
  head` at :225 IS the file's first heading, and the tool counts
  R-lines only above the first `## ` heading (HEAD_BOUNDARY_RE,
  statiker_record.py:132) → r_lines: 0 on sweep and closure,
  INTENT/R1–R5 parsed as malformed entries. Informational (field,
  not gate) but Verify grades per R-line, so the miss is silent.
  Design, decided: the head region extends THROUGH a first heading
  whose title is `Requirement head` (case-insensitive exact title)
  to the NEXT `## ` heading; any other first heading keeps the
  current boundary. Verifier, red-first: fixture mirroring the
  beat-the-books shape (head under a first `## Requirement head`
  heading) reads r_lines: 0 under old code, the true count under
  new; existing above-heading fixtures stay green. Done: probe
  flips, full suite green. Write boundary:
  plugin/skills/statiker/scripts/statiker_record.py,
  tools/test_statiker_record.py.

- **READY (small) 2026-08-15 — E-M: sweep-printed repair forms gate
  on resolver reachability.** Provenance: F147, measured at the
  beat-the-books desk on 0.2.65 (booking 271a6bf in OBSERVATIONS —
  incident + mechanism: `apply_supersession` builds its violated
  map at the LINT stage while `clause-unparsed` is SWEEP-stage, so
  the verdict's printed `corrects line <n>` form resolves against a
  map that structurally cannot contain its target; pasting the
  verdict's own form added two permanent corrects-nothing holds).
  Design, decided (desk's pre-formulated fix, adopted): a hold's
  printed repair string gates on its code being resolver-reachable
  — SWEEP-stage-only codes print a repair form WITHOUT the corrects
  token (naming the hand-bookkeeping shape instead); red-first
  suite assertion: every REPAIR_FORMS entry containing the
  correcting token is reachable by apply_supersession — red on the
  current tree. Write boundary:
  plugin/skills/statiker/scripts/statiker_record.py,
  tools/test_statiker_record.py. NOTE: overlaps Lane A's write set
  — build after Lane A integrates (bundle candidate with the P3/P4
  lane).

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

- 2026-08-15 — **P5 dropped same-day (no-grandfather rule, CLAUDE.md
  trial conventions):** the epoch-scoping design was grandfathering
  machinery, which the trial builds none of; the standing
  disposition for retroactive sweep holds is the stated deviation
  (relay 2, desk D-line, meta-affirmed). Booked body in git history
  (c4c87f7). Re-opens only with the trial's close or an external
  user.

- 2026-08-15 — **skill-edit-review experiment graded: SUSTAINS,
  3-for-3 on the pre-registered criterion** (grading entry in
  dev-notes/OBSERVATIONS.md 2026-08-15; body-read of the three
  release windows' review records). Convention converted from
  experiment to STANDING in CLAUDE.md: one fresh-context opus
  review per SKILL.md release before the pin moves, same brief
  form, findings dispositioned pre-release. Decision-grade without
  an operator round per the trial's n=1 policy (resolved
  pre-registered criterion; strengthens, never weakens, the safety
  floor).

- 2026-08-15 — **E-B/E-I/E-G′ shipped (lane R2, sonnet worktree
  dispatch; brief docs/directives/2026-08-15-lane-R2-brief.md).**
  On main as 32914d3 (E-B: UNIT_UNKNOWN for ids the record never
  scoped, known_units_of shared with waves_over_units, SKILL.md
  route sentence same commit), ef69925 (E-I: `pinned` subcommand,
  byte-level prefix check against the pin,
  PINNED_APPEND_ONLY/PINNED_REWRITTEN, SKILL.md passage same
  commit), c9038e9 + 017e95b (E-G′: Mode/Budget literal header
  reads; the correction commit fixed the Budget read to the
  declared compound grammar — the lane's own late grounding
  re-check caught an int() parse that would have silently never
  fired). Dispatcher's combined suite 348/348; SKILL.md diff
  verified as exactly the two pre-named insertions. Deviations
  accepted: five pre-existing fixtures + one battery row had
  ridden the old unknown-id fallthrough (the predicate-gain class
  landing live) and were migrated with intent preserved. OWED at
  the release seam: one opus review of the two R2 SKILL.md
  insertions before the pin moves (batch with any further SKILL.md
  edits per the final-form rule). Composition miss, desk's own:
  E-G′'s rescope did not quote Budget's compound grammar although
  the quote-the-literal header check existed since the same
  morning — the lane's SKILL.md re-read caught what the entry
  should have carried.

- 2026-08-15 — **E-C/E-D/E-H shipped (lane G, sonnet worktree
  dispatch; brief docs/directives/2026-08-15-lane-G-brief.md).**
  On main as 5a6cd46 (E-C byte-level emit in the git tool —
  say() via stdout.buffer/surrogateescape, ensure_ascii=False),
  d31909e (E-D unit sha parsed from the commit's own output,
  head_shown_paths reads at THAT sha — the WITHOUT-F9 hook-window
  probe books no false extras), 3c948d3 (E-H preflight
  branch:/worktree: fields, field-not-gate). Per-entry stash-proof
  reds pasted in the lane report; dispatcher's combined suite
  335/335. In-lane parity catch: a first-draft new verdict name
  (COMMIT_SHA_UNPARSEABLE) went red on the battery and was
  redesigned to reuse COMMIT_FAILED — the brief's rule, applied
  without a round trip. Residuals booked: E-J (stderr fallback
  byte fidelity, T22 trigger now met), E-K (EMIT_CONDUITS
  false-fire exemption). E-D's defensive unreachable fallback and
  the bare-repo/GIT_DIR layouts remain honest residue (lane report
  slot g).

- 2026-08-15 — **E-A/E-E/E-F shipped (lane R, sonnet worktree
  dispatch; brief docs/directives/2026-08-15-lane-R-brief.md).**
  On main as 0f1e9a5 (E-A verdict reach: entries/head_boundary/
  r_lines fields + .clippy/runs lint), 0c9e56b (E-E four one-shape
  fixes: newest_commit field, gap-filling-id lint, USAGE_ERROR
  routing, C1 docstring), 9589581 (E-F append-freeze breach
  detection). Suite 329/329 at integration. E-B/E-I/E-G halted on
  correct gap calls and re-dispatched as lane R2 (E-B/E-I with
  pre-named SKILL.md route sentences, same-commit parity rule;
  E-G′ Mode+Budget; irreversible half parked as P4). Desk
  incident, same hour: mint-first SKILL.md routes went red on the
  parity battery's phantom direction (d56c64f, reverted b0b1cc9,
  firing logged in OBSERVATIONS).

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

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

- **READY 2026-08-15 — P1: the seal/queue namespace gets its tool
  and its two missing grammar pieces.** Provenance: triage T8
  (WITH-B1 executed: three defensible derivations of one prose
  sentence — since narrowed by the exact repo-key pin now in
  SKILL.md :624-631, which answers the DERIVATION but leaves every
  desk re-composing the hash one-liner by hand, the re-pasted
  one-liner class; WITH-B2: a consumed queue is byte-identical to
  an unconsumed one and its header instructs re-landing — the live
  A8 queue shows a desk improvising a `LANDED` tail; WITH
  namespace note: desks invented `artifacts/` and `.report` homes
  the spec never defines). DESIGN SETTLED (meta desk 2026-08-15,
  derived from the work's requirements, not the incumbents):
  (1) `seal-path` subcommand in the git tool (owner of toplevel/
  common-dir/worktree semantics): `seal-path --tracker <path>
  --round A<n>` → verdict SEAL_PATH with every species' full path
  as fields — kills the hand-derivation class; SKILL.md route
  sentence same commit (parity battery).
  (2) Queue consumption grammar: a queue is SPENT when its last
  non-blank line matches `^LANDED <date> — at line <n>$` (the
  tracker line of the landing append) — in-band so a successor
  desk reading the queue sees it, append-only, and verifiable
  against the tracker; re-landing a spent queue halts at the desk.
  Requirements basis: successor-visible + append-only + names
  where it landed; deletion fails evidence, rename breaks the
  re-derive-from-filename property.
  (3) The invented homes get pinned into the ONE namespace, same
  derivation, new species suffixes beside `.seal`/`.queue`/
  `.paths`: `.A<n>.artifact` (the filter --out target),
  `.A<n>.report` (an attacker report persisted as file),
  `.A<n>.comparison` (the seal comparison the text says lands
  "beside the seal"). SKILL.md names them where each is first
  mentioned. Verifiers, red-first: seal-path verdict paths equal
  the SKILL.md-pinned derivation on a real repo + a worktree case
  (derive-in-main); queue-spent grammar positive/negative pair.
  Done: seal-path verdict's paths equal the SKILL.md-pinned
  derivation on both fixtures, the queue-spent pair passes both
  directions, full suite green. Write boundary: statiker_git.py,
  SKILL.md, tools/test_statiker_git.py, tools/test_contract.py.
  BUILD AFTER the P3/P4/E-M lane integrates (SKILL.md overlap);
  bundles with P2 as one lane, separate commits.

- **READY 2026-08-15 — P2: gate verdicts bind to the transactions
  they gate (the unit seam).** Provenance: triage T9 (WITH-B8:
  lock-commit LOCK_CHECK_CLEAN over SWEEP_HOLDS; WITH-B9 blocking:
  UNIT_COMMITTED over CLOSURE_VOID — forcing point 4's invariant
  with the detecting gate in the same toolchain, unconsulted;
  WITHOUT-F3 blocking: START↔COMMIT unlinked, an operator's
  unstaged draft committed as the unit's own; WITHOUT-F12: a
  write-set may name the tracker itself — all executed). The arms'
  red-first pairs travel with this entry (with/without files,
  B8/B9/F3 sections). DESIGN SETTLED (meta desk 2026-08-15, basis:
  body-read of cmd_lock_commit :700-758, cmd_unit_start :768-791,
  cmd_unit_commit :794-834):
  (1) Gate consult = SUBPROCESS to the record tool over the
  documented verdict-line contract (parse the single final
  `STATIKER-RECORD VERDICT:` line; embed it verbatim in the git
  tool's own verdict as `gate` field). Rejected: pasted token —
  testimony with staleness; import — couples process state and
  inherits the record tool's stage-coupling defects (E-M class).
  Gate unconsultable (subprocess fails, no verdict line) → halt,
  FAIL-CLOSED.
  (2) Lock seam: lock-check + lock-commit consult `sweep`;
  blocking holds → halt LOCK_GATE_HOLDS (closes B8).
  (3) Unit seam: unit-start + unit-commit take REQUIRED --tracker
  and REQUIRED --unit; both consult `closure --unit`; a blocking
  gate verdict → halt UNIT_GATE_BLOCKED (closes B9).
  (4) START↔COMMIT link (closes F3): the RECORD's declared
  write-set becomes the single write-set source — closure --unit
  gains a declared_write_set field; unit-start/unit-commit drop
  the free --write-set args (briefs stop restating it:
  paraphrase-drift kill). unit-commit takes --start-sha (from the
  start verdict); checks start-sha ancestor-of-HEAD AND
  `git log start-sha..HEAD -- <declared write-set>` EMPTY (foreign
  touch mid-unit → halt UNIT_START_MISMATCH).
  (5) F12: at the unit seam, tracker path ∈ declared write-set →
  halt WRITE_SET_NAMES_TRACKER.
  New verdict names (LOCK_GATE_HOLDS, UNIT_GATE_BLOCKED,
  UNIT_START_MISMATCH, WRITE_SET_NAMES_TRACKER) each carry their
  SKILL.md route sentence in the SAME commit (parity battery,
  set-exact both ways); the unit-brief invocation lines in
  SKILL.md update in the same batch — no old-form escape hatch
  (no-grandfather rule, CLAUDE.md). Verifiers, red-first: the
  arms' B8/B9/F3 pairs + one per new verdict. Done: all four T9
  pairs flip (red under old code, green through the fix), parity
  battery set-exact both ways over the four new verdicts, SKILL.md
  invocation lines updated, full suite green. Write boundary:
  statiker_git.py, statiker_record.py (declared_write_set field),
  SKILL.md, tools/test_statiker_git.py,
  tools/test_statiker_record.py, tools/test_contract.py. BUILD
  AFTER the P3/P4/E-M lane integrates (statiker_record.py +
  SKILL.md overlap).

- **PARKED 2026-08-15 — P6: disposition entries trip
  basis-cites-invalidated by construction.** Provenance: relay 3
  (twelve F155 holds on F150 itself — the sweep firing on the
  entry that documents its over-fire; dispositioned, not chased,
  at the desk). An entry whose job is grading dead entries must
  name them; the corpus guard rule demands a declared, CHECKED
  exemption (E-K's class) rather than disposition-noise per run.
  Missing design, named: the exemption grammar — how a
  disposition/grading entry declares itself so the sweep verifies
  the declaration instead of firing. Trigger: the next run's
  grading entry tripping it.

- **READY (small) 2026-08-15 — E-N: a corrects token outside the
  entry body lints loudly instead of no-opping silently.**
  Provenance: F205 (relay 5, measured at the beat-the-books desk):
  a `corrects line <n>` token placed in an entry's BASIS clause is
  invisible to the resolver — the parser searches only entry
  bodies — and no lint fires: a silent no-op, the worst shape (the
  repair looked landed and repaired nothing). Design, decided: new
  lint class `corrects-token-out-of-body` — fires when the
  correcting token appears in a region the resolver does not
  search (basis clause; any non-body position of an entry line);
  the repair form names the split the desk derived (token sheds
  the violation under the same id in the BODY; a fresh id
  re-declares any path). Lint class, not closure-blocking.
  Verifier, red-first: fixture with the token in a basis clause —
  silent under old code (zero violations), the new class under
  new; body-token fixtures stay clean. Done: pair flips, full
  suite green. Write boundary:
  plugin/skills/statiker/scripts/statiker_record.py,
  tools/test_statiker_record.py. BUILD in Lane D (bundles with
  P1/P2; statiker_record.py overlap with Lane C — after it
  integrates).

- **PARKED 2026-08-15 — P7: `waves`' write-set join is blind to
  shared LINEAR resources.** Provenance: A9/F217 (relay 6,
  executed: one alembic head, 111 revisions vs the 109 the record
  held; two migration units built concurrently under "down_revision
  = head at implementation time" branch the chain, and the app
  auto-migrates fail-closed on boot) — a shared linear resource
  crossing four units' write-sets, invisible to the file-based
  join. The run repaired locally (down_revisions assigned in the
  record, like revision ids — D107 amended). Missing design,
  named: whether the write-set grammar grows a declarable shared
  RESOURCE token the join serializes on, or the record-assigned
  ordering stays the standing per-run disposition. Trigger: the
  next run whose units share a linear resource.

## Done

- 2026-08-15 — **P3-parked ausgebucht: realized by the P3 ship
  above (58b224b) — the header-field decision resolved to the new
  line class, header untouched.**

- 2026-08-15 — **E-J/E-K/E-L shipped (lanes A+B, sonnet, shared
  copy): a979442 (E-J shared byte-level stderr fallback,
  statiker_emit.py extraction, T22 class retired), fdcd005 (E-K
  declared-exemption comment), 65d46ef (E-L requirement-head
  boundary).** Suite 358/358 at integration; per-entry stash-proof
  reds in the lane reports (booked in session record).

- 2026-08-15 — **P3/P4/E-M shipped (lane C, sonnet): 58b224b (P3
  `SKILL: statiker <version>` line class + skill_versions field),
  2f4d7f1 (P4 `unit U<k> irreversible: <effect>` line + 
  irreversible_units field; the parked P4 decision resolved to the
  tag grammar, hold-entry enforcement untouched), 4e30545 (E-M
  WIDENED: five codes printed resolver-unreachable corrects
  tokens, not one — the lane's derived assertion found four more,
  empirically reproduced; repair strings quoted in the lane
  report).** Suite 372/372 at integration; SKILL.md diffs verified
  as exactly the pre-named insertions. All unpushed pending the
  release seam.

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

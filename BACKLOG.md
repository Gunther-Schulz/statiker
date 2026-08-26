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





- **READY (small) 2026-08-26 — P34: the irreversible tag's page
  form and tool form disagree.** Provenance: U2 run (run 3), desk
  finding: SKILL.md:729-733 says the tag is a BARE label line at
  column 0, "never an entry"; the tool reads it only from an
  entry's body (`statiker_record.py:1020`, inside the entry loop;
  `irreversible_tag()` :778) — a page-form line is invisible to
  sweep/closure, so `irreversible_units` reads empty on a unit
  tagged exactly as the page says. Verified at the meta desk on
  both sources. The desk applied SKILL.md:56 (executable spec is
  the contract) and wrote the tool form. Design settled: the page
  states the entry-body form (`unit U<k> irreversible: <effect>`
  as a record line's body), the label-line sibling sentence
  removed; tool unchanged. Verifier: a suite case feeding a
  page-form bare line and asserting `irreversible_units` is EMPTY
  (documents the tool's actual reach) beside the existing
  body-form positive. Write-set: `plugin/skills/statiker/SKILL.md`,
  `tools/test_statiker_record.py`. Done-criterion: page and tool
  name one form; skill-craft invoked for the edit; releases at
  the next seam with P32. Checkpoint review: touches a record
  form → rides the P32 opus review.

- **READY 2026-08-26 — P32: foreign-record ids in a basis field
  collide with this run's namespace.** Provenance: U2 run
  (run 3), desk F66: the seed's F25 cites the U1 record's
  entries as bare ids; the live-basis check
  (`statiker_record.py` ~1449, `latest.get(cited)`) resolves every
  cited id in THIS run's namespace, so once this run minted its
  own D3/F20 the seed entry read as resting on them — silently,
  until one were invalidated. Verified at the meta desk on the
  source. Design settled: (1) SKILL.md basis rule — a basis citing
  another record names the record (tracker path or run name)
  before its ids, never a bare id; (2) tool half — the live-basis
  scan ignores ids that follow a record-name token, and the sweep
  surfaces a bare id whose number exceeds this run's own max as
  FOREIGN-ID-SUSPECT (an id below the max is undetectable by
  count, hence the prose rule is the primary carrier). Verifier:
  red-first over a planted seed entry citing a bare F20 with the
  run's F20 INVALIDATED (the defect's live fire is the desk's
  own F66 on the real tracker; the suite fixture reproduces that
  shape) → clean once the record is named; the suspect hold fires
  on a planted over-max id.
  Write-set: `plugin/skills/statiker/SKILL.md` (basis rule),
  `plugin/skills/statiker/scripts/statiker_record.py`,
  `tools/test_statiker_record.py`. Done-criterion: both proofs red
  then green in the suite; released at the next seam (never
  mid-run). Checkpoint review: machine-read semantics → opus
  review owed before the pin moves.

- **PARKED 2026-08-26 — P33: a tracker pinned before its head is
  composed can never carry head R-lines.** Provenance: U2 run
  (run 3), desk F65/D4: `r_lines` counts head-region lines only
  (`statiker_record.py:885`, `i < head_end`); the pause-durability
  commit pinned the tracker at seed, the skill bars insertion
  under the head, so the run's R1–R15 live as ENTRIES — where no
  gate or sweep surfaces them, and the entry tag set has no
  member meaning DECLARED (a first declaration wears a new-letter
  tag). The desk carries them by hand into the verify brief.
  Missing evidence (named): the run's own verify seam — does the
  hand-carry lose an R-line, and does the attack round see the
  entry-form R-lines at all? Two design candidates, undecided on
  that datum: (a) a `DECLARED` entry tag counted by `r_lines`
  alongside head lines; (b) the durability pin is a plain commit
  that leaves the head region unpinned until the head is
  composed. Trigger: U2 run's verify digest; lift into READY with
  the datum. Write-set (either design):
  `plugin/skills/statiker/SKILL.md`,
  `plugin/skills/statiker/scripts/statiker_record.py`,
  `tools/test_statiker_record.py`.

- **PARKED 2026-08-16 — P18: "serious core issues" investigation
  (operator-named, at run-2 stop).** The operator stopped run 2
  (canonical-frame-sign-repair) at cycle 7/7 with 3/4 rounds spent
  and suspects core skill issues; whether that is true is the
  investigation, deliberately not run same-day. Evidence base, all
  2026-08-16: two runs, zero landed units — run 1 died lock-barred
  (173 defang holds), run 2 stopped at budget on the SMALLEST
  shippable unit with the fix itself unrefuted through three
  rounds — the rounds' findings landed on record/account ground,
  not the change (the cycle-12 pattern at a new altitude); the
  day's OBSERVATIONS entries carry the full trail (mints
  0.2.78–0.2.81, review series, Begehung R3 two-class read,
  P15 repair-mints-violations, P16 stop-hook, P17 waker gap).
  Candidate questions for the investigation, recorded not
  answered: is record upkeep consuming the cycle budget the
  design work needs (bookkeeping-to-substance ratio per cycle,
  measurable from the two trackers); do attack rounds
  over-target the record because it is the largest attackable
  surface; is the budget's unit (cycles) measuring the wrong
  quantity. Missing evidence, named: the measurement itself — a
  fresh session reads both run trackers and computes the ratios
  before any design change. Trigger: next meta-session on this
  repo (operator: "not today").
  PARTIAL DISCHARGE 2026-08-17 (operator-prompted "why is this
  item taking so long" analysis, this session): the coarse
  ratios are answered from the trackers' own executed
  measurements, not a fresh body-read. Run 1: 8 attack rounds
  all BIT, zero zero-delta ever, zero landed units and zero
  V-lines over 46 tracker commits / 8,665 lines (F143's executed
  greps); sweep 750 holds of which 696 retroactive form debt
  from grammar rules post-dating the lines they grade — 275
  superseded-block-form, 248 basis-missing, 173 tag-literal —
  vs 22–24 substantive (F148/D95 executed distributions); A8:
  4/9 findings record/instrument-class, reopening nothing under
  the 0.2.48 never-sustain clause, which was in force at round 8
  and not applied (F143/F144); the run crossed skill versions
  0.2.4→0.2.65+ in one record's lifetime. Run 2 (narrowed to
  U1): READY in one day, fix unrefuted through 3 rounds, bites
  on record ground. CORRECTED 2026-08-17 by the resumed desk's
  gate report (record-governs read): all three run-2 rounds BIT —
  A3 carried five findings, among them a broken stated code edit
  in the design (D5 restated twice for it) — the header [READY]
  is the FOURTH ready-gate claim over the cycle-7 re-derivation,
  and the owed work at resume was ROUND 4, not implementation.
  "Fix unrefuted through 3 rounds" was this entry's label read
  over the record's body (paraphrase-drift class; mechanism:
  none — the desk's record-governs discipline was the backstop
  that caught it, prose, no guard fired). Counterfactual
  answered too: the same item
  killed a clippy run at cycle 2 (2026-08-05), and its parent
  line-matching family ran clippy cycles to 21 and 47
  pre-statiker — the item's scope (widened 2026-07-31 into an
  architecture-wide identity refactor) is a co-cause, not
  statiker alone. STILL OPEN of the named measurement: the
  per-cycle bookkeeping-to-substance ratio (needs a body-read
  classification of ~230 findings — dispatchable); the
  budget-unit redesign (zero V-lines across 12 days says cycles
  measure loop iterations, not landed value — a design question
  now, not further measurement).

- **PARKED 2026-08-17 — P28: repairs mint defects — closure
  prose is fresh attack surface (FIVE recorded incidents across
  the trial).** Incident series: run-1 rounds 7-8 (findings on
  the desk's own newest cycles), run-2 A4 (two findings on
  "settled" dispositions), run-2 A5 (BOTH substance findings on
  entries cycle 8 wrote to close round 4); the class is the
  trial's most-recorded single pattern. Candidate direction,
  deliberately not designed here: closures as EXECUTED EVIDENCE
  rather than composed prose — a disposition carrying a command
  and its output offers an attacker nothing to bite except
  reality; overlaps P24's basis-upgrade twin, which may absorb
  the completeness slice of the class. EXEMPLAR for the design
  (run-2 implementation leg, 2026-08-17): the executor stashed
  only the fix while keeping the new test, so its baseline
  suite run contained the new check in its RED state — counts
  reconciling exactly (3,030 + 4 new − 2 pre-fix-red = 3,032)
  rather than approximately; a baseline that includes the new
  expectations failing is strictly more informative than one
  taken before they exist. Candidate corpus widening (operator
  call — corpus edits are GO-gated): the Fixing module's
  baseline sentence could name this arrangement. CLOSE GRADING
  2026-08-17 (P29 item 2, the named trigger): the five
  incidents SPLIT — the completeness lineage (F24/F63/F76/F95)
  is ABSORBED by P24's basis-upgrade + instrument seal; the
  rationale/account lineage (A6's F113 false exclusion
  rationale; F110's restated-figures brief) is NOT absorbed —
  no basis-kind upgrade catches a false justification for a
  correct boundary. The distinct executed-evidence-closure
  mechanism therefore stays a live candidate, with the stash
  exemplar as its form; still PARKED pending its design
  question (which closure classes must carry executed evidence
  — the judgment/mechanization boundary). Trigger refined: the
  close-seam mint window (P29 item 3), decided beside P24 so
  the split of labor is settled in one pass. Missing evidence, named:
  the run-2 close grading — enumerate the five incidents and
  answer whether P24 covers them or a distinct mechanism is
  owed; a sixth incident post-P24-mint would settle it the
  other way. Trigger: run-2 close grading.

- **READY 2026-08-17 — P29: run-2 close-seam checklist (the
  U1→U2 inheritance, executed by hand this once; consumer: the
  meta session at the close relay — THIS entry is its read-path
  carrier if the current session dies).** Design: decided —
  the checklist below IS the design, four item groups executed
  in order at the close relay. Items, each owed a
  named disposition in the close relay reply. HANDOFF BOUNDARY
  (operator-delegated call, 2026-08-17): the deep meta session
  executes through item 3's checkpoint-review DISPOSITION; a
  FRESH session takes the release mechanics and item 4 (U2
  seeding), reading this entry plus the three lane directives
  (docs/directives/2026-08-17-lane-*.md) as its brief.
  CUT REACHED 2026-08-17 (deep session's span complete): mint
  batch built, twice-reviewed (2 cycles), repaired, verified
  (suite 468 green at c19c829), integration-recorded, PUSHED to
  origin at 88de6b7. Successor's remainder: (i) the release —
  /release-plugin or the repo's release lane over the already-
  bumped 0.2.82 (bump b897ce4 already in history; pin moves at
  the release seam per CLAUDE.md); (ii) U2 seeding per item 4
  below, on the released version, carrying F128's crosswise
  standing instruction and the crosswise base rate as named
  missing evidence; (iii) P31 polish batch rides the NEXT bump,
  never its own release.
  RUN 3 (U2) PAUSED 2026-08-23 at SEED, operator call (docker needed
  elsewhere). State: desk beat-the-books-3d (opus, 0.2.82), tracker
  `.clippy/runs/2026-08-23-canonical-market-identity-u2-statiker.md`
  62 entries, pinned locally at beat-the-books 955010da (durability
  commit, not a lock/close pin; unpushed with ed68faf0, C2), HELD at
  F52 — awaiting the operator's FIRST-HAND line
  in the desk session for F42 route 1 (pg17 harness as prerequisite
  unit before U2, own pg17 container, U2 unchanged, U10/U11/U5 out,
  C2 stands); no head composed, no harness work started. RESUME
  BRIEF: (1) operator starts docker; (2) if the desk session is
  alive, operator pastes the F42 route-1 line there (text in
  OBSERVATIONS 2026-08-23, the pause entry) and the desk proceeds;
  if gone, a fresh opus desk in beat-the-books gets the delegation
  line first, then the route-1 line, and resumes from the tracker
  (skill resume passage: sweep/closure first); (3) meta session
  re-opens the peer channel, re-arms the ~30-min horizon, grades
  from the seeded two-unit digest onward. Decisions settled this
  run so far (OBSERVATIONS 2026-08-23): delegation construction =
  one first-hand line per desk; hold-clearing ruling with
  boundary (conditional on U2's own reversibility derivation);
  INTENT letter amended (leavings → U1's three headings); route 1
  chosen on F42. Baseline to beat: 6 rounds/landed unit.
  RELEASE LANDED 2026-08-18: the pin sits on 0.2.82 at d05b074
  (installed_plugins.json lastUpdated 2026-08-18T14:09Z,
  gitCommitSha d05b074) — remainder (i) done; (ii) U2 seeding is
  the open remainder, gated on the operator's five-unit
  authorization (beat-the-books BACKLOG, the eight-units entry);
  (iii) P31 rides the next bump. Shipped batch items moved to
  Done 2026-08-23 (P5 P15 P19 P20 P21 P24 P25 P26 P27 P30).
  INTEGRATION RECORD (2026-08-17, the batch push's booking —
  every subagent commit verified in the artifact and its lane
  report booked before this line was written): lane A
  (sonnet-mint-batch) 67e1774 P15 · 5cc7884 P26 · 4df7dbd P30 ·
  50615eb P25 · db5fe57 P5 · 4538d9a P20 · 522e8d2 P27 ·
  8d018f2 P19 · 098bda4 P21+P24; lane B (sonnet-p16-stop-hook)
  6e1e668 hook · 80e4c47 battery; lane C (sonnet-review-repair)
  4b17d2d R1 · eed25d6 R2 · c85a218 R3 · 2ac74ac R4 · 540b03b
  R5+R6 · 6e15876 R7 · 8774465 R8 · 38a5b39 R9 · a9d591d R10 ·
  8ec0c75 R11. Dispatcher commits: b897ce4 bump · 9a4f4b9 P29 ·
  b771bfd P16 re-open · c19c829 re-review repairs. Suite 468
  green at c19c829; two review cycles (9-part checkpoint, 5-part
  discharge re-review), dispositions in OBSERVATIONS 2026-08-17
  and docs/directives/2026-08-17-lane-C-review-repair-brief.md.
  Progress at booking: item 1 partially discharged (spread-CLV
  export + successor entries verified in the artifact; F116
  metric graduation still open — now folded into lane A's P25
  leavings machinery); item 2 done except P18-ratio drop
  (recorded here: DROPPED, no decision hangs on it); item 3 in
  flight (lane B P16 done+booked, commits 6e1e668/80e4c47;
  lane A at P30 of its nine, bump landed b897ce4, boundary
  extension granted for test_contract.py battery rows); U1
  DEPLOYED to prod (origin 5c691cea, R4 discharged, R8 waits
  on crosswise population). Checkpoint-review question queue:
  the batch's cumulative SKILL.md diff; lane B's
  operator-authority-marker gap (link P23 — an authority: line
  class would solve both); lane B's untested multi-tracker
  glob path. Items, each owed a
  named disposition in the close relay reply: (1) LEAVINGS
  check over the desk's close report — out-of-scope findings
  exported to beat-the-books BACKLOG.md or recorded-dropped
  (the spread-CLV defect, F77, is the named chase item);
  in-run instruments used twice graduated to beat-the-books
  tools/ (the existence probe; the metric F116 already
  flagged); durable world-facts (Pinnacle frame-anchoring
  F112, prod retention overrides F79, the eleven-store
  population map) landed in beat-the-books' own carrier per
  its conventions, each with executed basis. (2) CLOSE
  GRADING: P24 graded on the A5/A6 seal record (done —
  READY); P28's five-incident enumeration answered
  (P24-absorbed or distinct mechanism); P18's remaining ratio
  formally dropped or run. (3) MINT BATCH at the seam: P5,
  P15, P16, P19, P20, P24, P25 (re-scoped form), P26, P27 —
  built with batteries, checkpoint opus review, ONE release;
  the stale next-run staging entry re-graded in the same
  pass. (4) U2 SEEDING: successor entries re-read against the
  close's corrected diagnoses (F119 discipline), fresh desk
  on the new version, rounds-per-landed-unit recorded as the
  baseline number U2 is predicted to beat. Verifier: the
  close relay reply enumerates every item with its
  disposition — an unnamed item is the miss shape. Done: all
  four groups dispositioned, release shipped, U2 seeded.
  Write boundary: statiker SKILL.md/tools (mints) +
  beat-the-books carriers (desk-side dispositions) + plugin
  release + this BACKLOG.

- **PARKED 2026-08-17 — P23: an open operator question has no
  non-blocking carrier in the record (desk workaround observed,
  run-2 resume).** Incident: the resumed desk had a live
  operator question (rounds bound vs the cycle raise) and
  deliberately did NOT record it, stating that a [PENDING] entry
  would block the very re-lock the running round needs — so the
  question survives only in conversation, the carrier that
  evaporates (run 1's F138 shows the blocking species working as
  designed; this is the complement: a question that must not
  gate). Missing design, named: a surfaced-not-gating question
  line class — enumerated at close and at resume like
  SWEEP_EXEMPT declarations, invisible to lock/ready/closure
  gates; new line class = machine-read semantics, same-commit
  tool authorship, checkpoint review. Trigger: the next mint
  window touching record grammar, or a second incident of a
  question held in chat.

- **PARKED 2026-08-16 — P17: the mailbox wait's waker is the
  monitored party (silent-stall exposure; Begehung R3).** A desk
  that legitimately ends its turn with a round in flight (0.2.81's
  first terminator state) is woken only by the attacker's own
  messages — the horizon rule ("silence past it is a finding") is
  prose only a WOKEN desk can execute, so a dead attacker produces
  a permanent stall indistinguishable from a long round; P16's
  Stop hook cannot cover it (fires at turn-end, cannot wake a
  sleeper — its design records this boundary). Current backstop,
  declared: the operator's eye on the terminal (trial posture).
  Harness note: per-session divergence measured 2026-08-16 (the
  meta session lost the mailbox lane, the desk kept it — the class
  is live wherever the mailbox lane is). Missing evidence, named:
  one observed stall past a stated horizon under a mailbox-lane
  harness — until then any timer mechanism (cron, systemd,
  tracker-mtime watch) is machinery without a fire. Re-grade also
  if the harness goes sync-only everywhere (class moot: a sync
  dispatch cannot outlive its turn). 2026-08-17: candidate
  mechanism NARROWED — an in-harness background timer (`sleep
  <horizon>` as a background Bash task; its exit re-invokes the
  session) replaces the external machinery list at near-zero
  build cost; applied by hand at the meta desk over the run-2
  peer handoff, and the generalized class (horizon stated, waker
  is the monitored party — every peer wait, not just statiker
  desks) is booked in dispatch-guards
  dev-notes/dispatch-OBSERVATIONS.md 2026-08-17 with
  pre-formulated §4 text. Park evidence unchanged: still no
  observed stall past a stated horizon.

- **READY (small) 2026-08-17 — P31: post-release polish batch
  from the 0.2.82 re-review (all fixes reviewer-prescribed,
  none release-blocking).** Design: decided per item. (1)
  `filter`'s staleness field emits the raw `--sha` beside a
  resolved newest_commit (statiker_record.py:2280-2281) — an
  abbreviated sha reads as a mismatch-that-is-not-one; resolve
  once via `rev-parse --verify <sha>^{commit}` and emit the
  resolved value (mirror of the R8 fix; the reviewer's 7a sweep
  found exactly this one further site, positive control shown).
  (2) R10 harvester narrowing: the AST branch collects ANY
  returned string-list; narrow to the two code-returning
  functions so a future unrelated `return ["a","b"]` cannot
  false-fire the coverage assertion. (3) leavings prose: the
  void sentence claims unconditionality but the void is
  post-closure-only — an em-dash disposition BEFORE the closing
  A-line passes; qualify the sentence (off the sanctioned path,
  prose-only). (4) one-line pointer from the re-lock passage
  (~:1088) to P24's clause (b) (~:1224) — the clause targets
  re-lock momentum but sits 135 lines off the reader's path.
  (5) `tripwire --threshold` usage guard: reject < 1 (zero arms
  a fires-always breaker; pre-existing, easier to reach now the
  arg is optional). (6) trim cmd_sustain docstring's over-claim
  ("a new round opens only if" → "the verdict reads SUSTAIN_OK
  only if" — the tool cannot stop a dispatch). Verifier:
  battery cases for (1) and (5), red-first per the standard
  arrangement; (2) keeps R10's planted-defect pair green; (3),
  (4), (6) prose/docstring with the suite green. Done: all six
  landed, suite green, rides the NEXT version bump (never its
  own release). Write boundary: statiker_record.py +
  tools/test_statiker_record.py + tools/test_contract.py +
  SKILL.md (items 3-4) + OBSERVATIONS + bump rider.

- **READY 2026-08-17 — P16 (re-opened): Stop-hook HELD OUT of 0.2.82 on
  checkpoint-review findings (4 executed false-fire classes);
  design INVERTED for the next build.** The 0.2.82 build (script
  + 16-test battery, commits 6e1e668/80e4c47) stays in-tree as
  groundwork, unregistered (hooks.json hold, lane C R11). Review
  findings, all executed: (1) fires on any in-progress tracker in
  the repo — but the skill MANUFACTURES permanently in-progress
  trackers (version-mismatch abandons, release-during-run
  abandons), so a week-old abandoned tracker blocks every
  session's every turn-end; (2) fires on a dispatched discovery
  leg ([PENDING] leg is a legitimate wait it doesn't model); (3)
  fires on the budget stop-and-report minted in the same release
  (mandated stops are invisible to it); (4) its hand-rolled parse
  diverges from the record tool day-one (no head-region
  exclusion, no supersession — the shared-coordinate class).
  Redesign constraints, settled by the review: INVERT the fire
  condition — fire only where a NAMED owed-work signal is
  present, default silence; read the record tool's sweep verdict
  instead of re-parsing (one coordinate); session-bind the
  tracker (desk-written live marker, session id, or recency
  bound — an abandoned tracker is silent); the authority
  detection moves to the `authority:` opener class (see the
  review's Q2 recommendation — one mechanism with P23) instead
  of phrase search. Also owed: the multi-tracker fixture and the
  ordinary many-historical-one-live fixture. Verifier: the
  existing battery re-pointed at the inverted predicate, red
  demonstrated on the four false-fire classes above (each a
  fixture), silent on all of them post-fix, still firing on the
  two incident shapes. Done: inverted hook registered, battery
  green with the four new reds demonstrated, one live firing or
  clean live pass logged. Write boundary: `plugin/hooks/**` +
  tools/test_statiker_stop_hook.py + bump. Original design for
  provenance: the midturn-answer-check pattern aimed at statiker
  desks (b7 post-A1, cd post-A2 incidents; the superseded
  original design is in this entry's git history).

- **PARKED 2026-08-15 — P8: write-set paths with whitespace (or
  leading /) are structurally undeclarable since P2.** Provenance:
  Lane D gap (c)(1)-(2): write_set_violations' single-token rule
  (itself fire-born — whitespace once read as two colliding
  units) now bounds what a unit can commit, since the record is
  the write-set's single source; the old free CLI arg accepted
  such paths. Accepted as shipped (the grammar rule's incident
  outranks the speculative capability). Missing design, named: a
  quoting/escaping grammar for the write-set field. Trigger: the
  first real unit needing a space-carrying or absolute path.

- **PARKED 2026-08-16 — P12: the early head round (decomposition
  attacked before deep design) returns to design — cut from the
  0.2.74 release after drawing blockers in BOTH release-review
  rounds.** The VALUE stands un-refuted: a direction defect
  prices at one early round or at every cycle it misdirects
  (R6–R8 found at cycle 13 = the incident). What failed is the
  mechanism: reusing the ordinary round machinery. Design
  constraints, enumerated from the two rounds (OBSERVATIONS
  2026-08-16, both disposition entries): (a) round-1 H1 — its
  A-line must be mechanically distinguishable so the closure
  predicate and Phase flip cannot read it as the closing
  ZERO-DELTA; (b) round-1 H2 / round-2 H1(b) — it runs
  pre-[READY] where open-leg PENDINGs legitimately block the
  lock gate, so it cannot be a lock; (c) round-2 H1(a) — but any
  NON-lock tracker commit breaks the standing-lock recovery rule
  ("the newest commit touching the tracker" IS how S is found),
  so the pin needs either lock-machinery participation or a new
  commit species the recovery rule knows; (d) round-2 M8 — a
  substance-free return needs a legal A-line tag that is not the
  closing ZERO-DELTA, and closure safety must not rest on the
  desk remembering an inverted append order; (e) round-2 M9 —
  its budget accounting must be stated. Likely shape: a distinct
  round species with its own A-line tag and tool support (new
  verdict/tag names = same-commit tool authorship, the
  composition rule). Trigger: the trial-close grading, or the
  first multi-unit greenfield run that misses it.

- **READY (small) 2026-08-16 — P14: seal-namespace comparison
  species naming drift.** Provenance: session-10 stop-report
  (desk F228): on-disk comparison files from the pre-P1 era are
  named `…seal-comparison` while 0.2.77's seal-path prints the
  `comparison` species (`<tracker>.A<n>.comparison`) — a
  successor desk pasting the printed path finds nothing where a
  comparison exists. Design settled: the tool's name is the
  contract (paste-never-hand-compose); disposition is a one-time
  rename of existing on-disk files to the printed form (operator
  machine, `~/.local/state/statiker/seals/`), no tool change, no
  skill change. Verifier: seal-path's printed comparison path
  exists for A8/A9 after the rename. Done-criterion: the rename
  executed and the desk's F228 answerable with the printed path.
  Trigger: before the next session that reads a comparison (the
  trial close's grading).

- **PARKED 2026-08-16 — P13: the release-review series' tool-work
  residue (the mechanism pass's collected items).** Three items,
  each dispositioned prose-side in 0.2.76 with its mechanism half
  parked here: (a) r4-H1 — the commit gate's
  start-sha-predates-the-void carve-out, so clean in-flight
  siblings land through a premise-kill instead of re-dispatching
  (prose now states the fail-closed behavior; the carve-out needs
  gate logic + battery); (b) r4-M4 — the budget-raise entry's
  machine-findable surfacing in sweep/closure verdicts
  (late_intent's shape; prose ships a body-read template until
  then); (c) r3-MINOR-5 — a lint class for a world-facing
  discharge line missing its read-sha (fail-safe meanwhile).
  All three are the medium tenet's class: exact semantics →
  mechanism + red-first battery, then prose. Trigger: the
  mechanism pass (with P12's design), or the first run a
  prose-side disposition measurably costs.

- **PARKED 2026-08-16 — P11: the cross-skill stats contract is
  half-maintained, and the unmaintained half miscounts silently.**
  Provenance: Begehung R1 (BEGEHUNG-MAP.md round log), executed
  pair with clippy-era control — cycle count 15-for-13 (cycle 3's
  heading unanchored; repair/correction/cont. headings counted as
  cycles), decision-family collapse to one family (numeric IDs vs
  the reader's digit-stripping sed), falls-per-entry 56/1
  presented as a measurement. Emission-side claim narrowed in
  SKILL.md (0.2.70): admission maintained, metrics disclaimed,
  series metrics route to `trend`/`waves`. Reader-side repair
  booked in coding-clippy BACKLOG (statiker-era branch, absent-
  not-zero). What stays PARKED here, with its named decision: is
  cross-skill clippy-vs-statiker comparison via /clippy-stats a
  trial deliverable at all? If yes, the statiker half is a
  cycle-heading FORM mandate (grammar+lint = new machinery — not
  justified by a metrics nicety alone, and the version-neutral
  record gate would surface its retroactive holds); if no, the
  clippy-side absent-not-zero branch closes the class. Trigger:
  the trial-close grading design (which will need the comparison
  question answered either way).

## Done

- 2026-08-23 — **next-run staging (STOP after the record gate)
  DROPPED, overtaken:** its premise was resuming the
  canonical-market-identity tracker, which closed FAILED on
  operator call 2026-08-16 and is terminally lock-barred
  (beat-the-books BACKLOG, parent record); the U1 successor ran on
  a fresh tracker and closed PASSED (5c691cea), and P5's
  epoch-scoped sweep (db5fe57, 0.2.82) removes the retroactive-hold
  class the checkpoint was staged to grade. The resume gate runs
  as the skill's ordinary resume passage (0.2.69); no isolated
  stop is owed at the U2 seed.

- 2026-08-17 — **0.2.82 mint batch shipped (lane A sonnet, nine
  items + lane C review repairs; pin moved 2026-08-18):** 67e1774
  P15 · 5cc7884 P26 · 4df7dbd P30 · 50615eb P25 (re-scoped form) ·
  db5fe57 P5 (epoch-scoped sweep) · 4538d9a P20 · 522e8d2 P27 ·
  8d018f2 P19 (budget as safety escape) · 098bda4 P21+P24; bump
  b897ce4; review repairs R1–R11 (4b17d2d…8ec0c75), re-review
  repairs c19c829. Suite 468 green at c19c829; two opus review
  cycles, dispositions in OBSERVATIONS 2026-08-17 and
  docs/directives/2026-08-17-lane-C-review-repair-brief.md;
  integration record by SHA in P29 (Open). P16 shipped as
  groundwork only and RE-OPENED (Open, READY) — hook unregistered.
  P31 polish residue rides the next bump.

- 2026-08-16 — **P6/E-O/E-P shipped (Lane E, sonnet, one lane
  sequential): 4739ed9 (P6 SWEEP_EXEMPT grammar netted from the
  blocking calculus, 0.2.72), 0c993ea (E-O lock gate keys on the
  blocking set, Status-conditioned), badf889 (E-P GATE_UNREADABLE
  driven via substitute record-tool path; the gate's own branch
  proven healthy, no source change).** Suite 380→393,
  dispatcher-verified. Gap (c) RATIFIED at booking: unnamed
  statuses (PASSED, missing, malformed) default to the blocking
  bucket — fail-closed, documented in the gate's docstring.
  Deviation (d) ACCEPTED: verdict-parity checker gains the
  backtick-label exclusion (`GRAMMAR_LABEL_RE`), discriminating
  pair recorded in the comment, two regression tests. Report
  booked in full (2 parts, mailbox); brief:
  docs/directives/2026-08-16-lane-E-brief.md.

- 2026-08-16 — **P9+P10 shipped (desk, fable): 6e211ee — four
  contraction clauses in SKILL.md (0.2.68): budget operator-owned
  (desk spends, never raises), early head round for multi-unit
  heads, trend grading + narrowing route (non-contracting series
  re-scopes via R-amendment + EXPORTED exits, never another
  same-form round), scoped reopening ([BIT] reopens cited
  entries + dependents only; zero-delta stays whole-design).**
  Deviation from P9's widened body, recorded in OBSERVATIONS
  2026-08-16: strict delta-SCOPED attack questions dropped
  (would hollow zero-delta or force a grammar+tool change);
  contraction carried by the other three mechanisms. Full
  provenance (F143/D89/D92, the 9-round run measurement) in the
  OBSERVATIONS mint entry. Pin held: release rides the next
  batch (P6/E-O/E-P) behind the standing opus skill-edit review.
  Residue live elsewhere: the paused run's disposition (re-seed
  per-unit) is an operator-queue item, not a backlog entry here.


- 2026-08-15 — **P1/P2/E-N shipped (Lane D, sonnet): 3e78dba (E-N
  corrects-token-out-of-body lint), b825de4 (P1 seal-path
  subcommand + queue-spent grammar, worktree derive-in-main
  proven), 2ab7651 (P2 gate-bound transactions: subprocess gate
  consult, record-sourced write-set, --start-sha link; six SKILL.md
  edits verified per-commit).** Suite 380/380 at integration.
  P2 RIDER: dispatcher verification found LOCK_GATE_HOLDS
  over-firing two-axis (E-O, Open) — P2 releases only together
  with P6 + E-O (Lane E). Full booking: OBSERVATIONS 2026-08-15.

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

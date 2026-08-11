# Statiker — backlog

Future work graded by decision-completeness (operator-corpus file
roles). PLAN.md stays the design record; entries here are work items,
and a SKILL.md change stays fire-born per CLAUDE.md — an entry can
build tooling, but a clause mint still needs its incident.

## Open

- **PARKED 2026-08-11 — no forcing point demands a side-effect /
  dependents enumeration for the locked design; blast radius rides on
  attacker initiative and repo-suite luck.** Finding (operator
  question, coverage read at SKILL.md): what EXISTS touches the class
  in three layers, none of which forces it — the decision-commit
  basis reaches the consuming read of the decision's OWN premise
  only (The loop, hop-trace clause); the attack's verbatim question
  block names fit-to-requirement, decomposition, simplicity — a side
  effect on functionality outside the head is caught only if the
  fresh context thinks of it unprompted; verify's verdict is
  per-R-line, so a regression no R-line names is structurally never
  asked (only the repo's own checks catch it, where they cover it).
  The operator corpus's dependents-search rule (grounding: a change
  to anything others depend on lands with the dependents search
  stated, command + hits) binds via composition but has no statiker
  seam — prose riding on desk memory. Design sketch (recommendation,
  not settled): cheapest landing is ONE clause in the attack's
  pasted question block — attack the design's blast radius: for each
  surface the design changes, are consumers/dependents enumerated by
  executed search, and does the design hold at each; alternative
  landing is a [READY] precondition (each unit enumeration names its
  changed-surface dependents search). Missing evidence (the park
  reason, per this file's header rule): no fired incident — a side
  effect slipping through a statiker run — and no operator decision
  to mint it as a (hypothesis) clause with validation criterion
  instead. Trigger: first such incident, or operator GO on the
  hypothesis mint. Verifier at build time: a design with a known
  un-enumerated consumer must draw the finding from a fresh-context
  attack round (red), and the same design with the search recorded
  must not (green).

- **READY 2026-08-11 — triage the three-arm review harvest (~25
  findings, three independent opus reviewers, all probes executed).**
  Evidence, the complete record: begehung repo,
  `dev-notes/eval-begehung/2026-08-11/tier2-{with,without,sentence}.md`
  (+ `tier2-with-MAP.md`, a 12-row axis map of this repo). Findings
  arrived as an eval by-product but are real and probe-backed; each
  carries its executed probe, most carry red-first arrangements.
  Cross-arm confirmed classes (independent instruments agreeing):
  vacuous sweep/lint over zero parsed entries (3/3 arms — with-B/F1/A1);
  path-alias parallel-eligibility in waves (3/3 — B3/F10/A4);
  seal/queue/repo-key namespace prose-only + ambiguous derivation
  (3/3 — B1/F7/B5-sentence); unit-id typo clears holds (2/3 — F2/A2);
  byte-policy not carried to the git tool (2/3 — F4/A3); clippy-stats
  contract dated hand-read, currently HOLDS (2/3 — B5-with/B6-sentence).
  Single-arm blockers deserving first look: F9 (booked sha is not the
  unit's own commit under the in-design parallel window — landing
  annotations and extras both wrong), B9 (unit-commit lands over
  CLOSURE_VOID — FP4's own invariant, gate present but unconsulted),
  NEW-1 (module-level failure emits no verdict line at all). Design
  (decided): a triage session walks the three files, dedupes into
  per-finding entries or fix commits, records a disposition per
  finding (fix / entry / prose-rest / rejected-with-reason) — the
  reviewers' own fix-shapes and red-first cases are in the texts.
  Verifier: per-finding red-first before any repair lands (the probes
  are re-runnable as written). Done: every finding across the three
  files dispositioned, the set reconciled against the files' own
  enumeration (with: B1-B9 + namespace note; without: F1-F12 +
  pattern; sentence: A1-A5, B1-B6, C1, NEW-1..3), duplicates merged
  with both ids kept.

- **READY — worktree provisioning joins the git tool: the batched
  trip's only hand-run git operation gets verdicts.** Booked
  2026-08-10 (0.2.57 review N1: hand-run `worktree add/remove`
  has no verdict to book and no halt route; dirty removal needs
  `--force` on its normal path — executed evidence in the review).
  Design, decided: `statiker_git.py` gains `worktree-add --sha
  <lock sha> --path <outside-repo path>` and `worktree-remove
  --path <path>` (forced removal, the by-product case is normal),
  each ending in one verdict line (WORKTREE_ADDED /
  WORKTREE_REMOVED / halt members per the tool's catch-all rule);
  SKILL.md's provisioning sentence then cites the subcommands in
  place of raw git. Realizing write-boundary: `statiker_git.py`,
  `tools/test_statiker_git.py`, SKILL.md (one sentence swap;
  skill-craft + review). Verifier, red-first: dirty-worktree
  removal green through the subcommand, red through plain
  `git worktree remove`; battery green. Done: a batched round's
  tracker books worktree verdict lines.

- **READY — `write-set:` joins the machine-token discipline.**
  Booked 2026-08-10 (0.2.57 review N5 second half; the
  normalization half landed same day). Design, decided: SKILL.md's
  machine-token literal list gains `write-set: ` beside the
  scope-openers, and the lint's positional near-miss detection
  covers it (a would-be write-set line failing the exact literal
  lints as a near-miss, same as every other token); battery gains
  the near-miss case red-first. Realizing write-boundary:
  `statiker_record.py`, `tools/test_statiker_record.py`, SKILL.md
  (token list line; skill-craft + review). Done: a misspelled
  write-set line lints instead of silently not parsing.

- _(superseded booking, closed 2026-08-10 — see Done)_
  **READY — mechanical wave derivation over unit write-sets: the
  parallel clause exists, its input is data, and the grouping is
  still done by eye.** Booked 2026-08-10, cross-repo provenance
  (operator GO "add it to statiker's backlog"): SKILL.md:816 says
  units with disjoint write-sets run parallel, `statiker_git.py`
  enforces each unit's declared write-set — but nothing computes
  which units ARE disjoint; the desk reads the write-sets and
  decides. The incident this inherits (cache-fix, same day): a
  9-lane parallel wave where every boundary inferred from prose
  produced returned members (8 across the wave) and the one lane
  with mechanically-derived disjoint boundaries returned zero —
  measured, in that repo's wave-1 record. Statiker is one step
  ahead (its boundaries are declared data, not prose) and one step
  short (nobody joins them).
  Design, decided: a `waves --tracker P` read-only subcommand in
  `statiker_record.py` (extend the existing tool, no new file):
  collect each unit's declared write-set from the tracker — the
  parse source is the record's own lock-set/write-set line form
  (`SKILL.md:471-478`: file-granular paths, appended as record
  lines; premise verified against the grammar 2026-08-10), compute
  connected components over shared paths, emit the wave partition
  (disjoint components = one wave, overlapping units serialized
  within their component) and flag any unit with no declared
  write-set as UNPLANNABLE rather than guessing. Report, never a
  gate — the desk's parallel decision cites the output; the git
  transaction stays the enforcement layer.
  Realizing write-boundary: `plugin/skills/statiker/scripts/
  statiker_record.py` + its red-first battery (`tools/` suites).
  Verifier, red-first: a constructed tracker with three units — two
  disjoint, one overlapping a first — must yield waves
  `{U1,U3},{U2}` with the overlap named; a unit missing its
  write-set must come back UNPLANNABLE, not placed; battery green.
  Done-criterion: the next multi-unit run's parallel decision in the
  tracker cites the subcommand's wave output instead of a desk read
  of the write-sets.

- _(superseded booking, closed 2026-08-10 — see Done)_
  **READY — the round-trend read has data and no instrument: A-lines
  carry every round's outcome and the re-entry trend is still a hand
  read.** Booked 2026-08-10, cross-repo provenance (cache-fix drain
  day; operator direction "improve the efficiency and speed of cycle
  and attack rounds"). The operator corpus's re-entry-seam
  convention binds the desk already: the reply opening a same-form
  repeat round names the series trend — counts and locations across
  rounds, read from the record — and a flat or worsening series
  indicts the FORM, not the latest findings. Statiker's tracker
  records exactly the needed series (`A<n>
  [DISPATCHED|BIT|ZERO-DELTA|VOID]` lines with finding bodies), so
  the convention's computable slice is a report: rounds per design,
  findings per round, BIT-vs-ZERO-DELTA trajectory, and whether the
  newest round's findings concentrate in the prior round's repairs
  (the form-indicting signature). A desk on any tier reads the
  command instead of re-deriving the series — the cheaper the desk,
  the more this matters.
  Design, decided: a `trend --tracker P` read-only subcommand in
  `statiker_record.py`; output one line per design (round count,
  per-round finding counts, trajectory verdict FLAT / IMPROVING /
  WORSENING as arithmetic over the counts, never judgment) plus the
  concentration flag where a finding's cited site lies in the prior
  re-lock's repair set — in record terms: the finding's body cites a
  D-id whose LATEST revision (the grammar is latest-line-per-id)
  landed at the previous re-lock; attack repairs revise D-lines, so
  the repair set is those revised ids, no code diff involved.
  REPORT, never a gate — the form question
  stays desk judgment; this delivers its inputs (the closing-gate
  rule: below the judgment, evidence delivery is always
  mechanizable).
  Realizing write-boundary: `plugin/skills/statiker/scripts/
  statiker_record.py` + battery.
  Verifier, red-first: a constructed tracker with a worsening
  three-round series whose round-3 findings cite round-2 repair
  sites must render WORSENING with the concentration flag; an
  improving series must not; battery green.
  Done-criterion: a real run's repeat-round reply cites the
  subcommand's output as its trend line.

- **READY — attack-round batching: one fresh-context trip carrying
  every locked design ready at that moment, instead of one design
  per trip.** Raised 2026-08-10 from the corpus's priced-unit rule
  (a round trip through another party carries a BATTERY, not one
  candidate — the recorded waste shape is splitting across trips
  what one trip carries) applied to statiker's rounds, where each
  locked design takes its own sequential round and each round costs
  a full freeze window (desk appends queue for the round's
  duration). Fewer, fuller rounds would cut both the trip count and
  the total freeze time.
  Parked, not ready, because the design tension is real and
  unmeasured: the single-design round buys attention depth and
  independence (an attacker reading design A's flaws inherits a
  frame for design B — the same reason a resumed attacker is
  forbidden), and the per-design verdict discipline would need the
  per-member disposition form so a batched round cannot silently
  under-attack its tail. Named missing evidence, which is the
  un-park trigger: a paired probe — same locked designs, batched
  attacker vs single-design attackers, pre-registered per-design
  blocker-yield criterion, arms graded before outcomes are compared
  — showing the batched arm's per-design yield holds. Until
  measured, the sequential default stands on its own recorded
  basis.
  UN-PARKED 2026-08-10: the paired probe ran and the criterion
  HELD on both designs (pre-registration + grading record:
  `dev-notes/probe-attack-batching-2026-08-10.md`; per-design
  confirmed-blocker counts batched ≥ single, no tail yield
  collapse, plus an emergent cross-design coupling finding only a
  batched round can produce). Standing caveat carried into the
  design: n=1 and largely disjoint finding sets, so the HOLDS is
  evidence, not equivalence proof — the per-design disposition
  form is mandatory, and the batched arm's one tail-accuracy slip
  is its motivating incident. Design, decided: SKILL.md's attack
  section gains — a round MAY carry every locked design ready at
  that moment; the brief states the order and requires a complete
  per-design verdict block (findings, or that design's explicit
  zero-delta — a design without its own block is an incomplete
  return); the A-line records per-design outcomes; the sequential
  single-design round stays the default where only one design is
  ready. Realizing write-boundary: SKILL.md (skill-craft + the
  trial's opus skill-edit review; the clause mint cites the probe
  record as its provenance — whether that satisfies the fire-born
  bar is the meta-session's call at minting, recorded either way).
  Verifier: the next multi-design moment runs batched with the
  per-design blocks present in the round's A-line. Done-criterion:
  one real batched round recorded with complete per-design
  dispositions.

## Done

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

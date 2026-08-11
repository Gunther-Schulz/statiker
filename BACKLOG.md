# Statiker — backlog

Future work graded by decision-completeness (operator-corpus file
roles). PLAN.md stays the design record; entries here are work items,
and a SKILL.md change stays fire-born per CLAUDE.md — an entry can
build tooling, but a clause mint still needs its incident.

## Open

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

- **READY — `write-set:` near-miss detection joins the lint.**
  Booked 2026-08-10 (0.2.57 review N5 second half; the
  normalization half landed same day). Premise re-read 2026-08-11
  before dispatch: the SKILL.md token-list half ALREADY landed
  (4138fe6, 0.2.57 delta round D2 — "validity only — near-miss
  lint stays booked"); remaining scope is the lint half alone.
  Design, decided: the lint's positional near-miss detection
  covers the `write-set: ` declarator (a would-be write-set line
  failing the exact literal lints as a near-miss, same as every
  other token); battery gains the near-miss case red-first.
  Realizing write-boundary: `statiker_record.py`,
  `tools/test_statiker_record.py`. Done: a misspelled write-set
  line lints instead of silently not parsing.

## Done

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

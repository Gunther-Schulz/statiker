# Statiker — backlog

Future work graded by decision-completeness (operator-corpus file
roles). PLAN.md stays the design record; entries here are work items,
and a SKILL.md change stays fire-born per CLAUDE.md — an entry can
build tooling, but a clause mint still needs its incident.

## Open

- **READY 2026-08-11 — begehung-harvest 2: four gate/instrument
  defects in the record tool, each with an executed false-clean or
  false-verdict probe.** Complete record with fixtures:
  begehung repo, dev-notes/eval-begehung/2026-08-11-opus/
  (tier2-without.md findings 2-5; probe fixtures re-runnable in
  that session's scratchpad, arrangements quoted in the file).
  The set: (a) `corrects line <n>` sheds by line number without
  consulting the violation's class — reaches the header and
  INTENT (Red executed: `Status: bogus-status` + one record-scoped
  token → LINT_CLEAN + SWEEP_CLEAN with the bogus header standing;
  INTENT tag-literal shed on the verdict's own recommended line →
  SWEEP_CLEAN with `[PASSED]` standing for clippy-stats' unanchored
  grep); fix shape: shed only REPAIR_BOOKKEEPING codes, supersede
  only MACHINE_TOKEN_CODES, else `corrects-nothing`. (b) `waves`
  path FIELD lacks the composition lint the declarator got: a
  two-path line reads as one exotic filename (Red executed: U2
  `src/app.py src/util.py` placed parallel-eligible beside U1
  `src/app.py`, LINT_CLEAN); fix shape: whitespace-in-path and
  leading-`/` lint positionally, like write-set-near-miss. (c)
  `trend` annexes a VOID round's span into its successor and
  computes bucket 1 from line 0 (Red executed: verdict flip
  WORSENING→IMPROVING on three pre-attack F-lines over an
  unchanged 2→1 yield series); fix shape: advance window at VOID
  A-lines, start bucket 1 at first [DISPATCHED], or emit the
  merge visibly. (d) BrokenPipe kills the one-verdict-line
  guarantee with exit 0 (Red executed: `waves | head -1` →
  traceback, no verdict, pipeline exit 0); fix shape: catch at
  the emit boundary, defined exit code — both tools. Design,
  decided: the four fix shapes above, each taken from the arm's
  own repair paragraph (the classification-table consult for (a)
  and the positional-lint mirror for (b) are existing in-repo
  patterns, not new design). Verifier:
  each probe as a red-first battery case; full `pytest tools/`
  green. Done: all four probes flip (false-clean cases now
  lint/halt, the trend fixture reads its true series), battery
  green, and the boundary note from the WITHOUT arm (sweep-code
  immunity is ordering-dependent) either pinned by a test or
  recorded as accepted. Write boundary: statiker_record.py,
  statiker_git.py, tools/test_statiker_record.py,
  tools/test_statiker_git.py, tools/test_contract.py.

- **READY 2026-08-11 — worktree-add containment joins the record
  tool's semantics (every-repo walk + as-named/real agreement).**
  Provenance: 0.2.59 review F1+F2, both EXECUTED — (F1) from repo A,
  `worktree-add --path ../B/wt-in-B` returned WORKTREE_ADDED and
  left `?? wt-in-B/` in sibling B's tree (green verdict, foreign
  tree polluted — the attack-9 exposure the record tool's `--out`
  check already closes, statiker_record.py:1156-1184); (F2) the
  symlink spelling `link/wt` (link -> outside dir) passed
  worktree-add while `filter --out link/art.md` halts
  ARTIFACT_IN_REPO — the worktree path is the one must-be-outside
  member decided real-only. Design, decided: `Repo.outside()` gains
  the every-enclosing-repo probe the record tool carries AND the
  named-and-real-agree rule; PATH_INSIDE_REPO fires on any
  enclosing repo and on as-named/real disagreement. Same commit:
  SKILL.md's principle-sentence worktree exception (The tools) and
  the provisioning parenthetical's this-repo-only scope both die —
  the wording exists only because the tool lacks the check.
  Verifier, red-first: the reviewer's two probes as battery cases
  (both currently WORKTREE_ADDED, must halt), plus the existing
  outside-dir case staying green; battery green. Red executed
  (0.2.59 review, fresh-context probes against HEAD, observed
  output in the review record): from repo A `worktree-add --sha
  <lock> --path ../B/wt-in-B` → `WORKTREE_ADDED`, then
  `git status --porcelain` in B → `?? wt-in-B/`; with symlink
  `A/link -> <outside dir>`, `worktree-add --path link/wt` →
  `WORKTREE_ADDED` while `filter --out link/art.md` →
  `ARTIFACT_IN_REPO`. Done: both probes halt PATH_INSIDE_REPO,
  the outside-dir case stays WORKTREE_ADDED, battery green, and
  the two SKILL.md reach-exception sentences are deleted in the
  same commit. Write boundary: statiker_git.py,
  tools/test_statiker_git.py, SKILL.md (the two sentences).

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

## Done

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

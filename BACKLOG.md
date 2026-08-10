# Statiker — backlog

Future work graded by decision-completeness (operator-corpus file
roles). PLAN.md stays the design record; entries here are work items,
and a SKILL.md change stays fire-born per CLAUDE.md — an entry can
build tooling, but a clause mint still needs its incident.

## Open

- **READY — the unit write-set record-line form: the grammar names
  none, nothing emits one, and `waves` reads a composed
  convention.** Booked 2026-08-10; fire-born incident provenance:
  the wave-derivation entry's cited premise (":471-478 covers unit
  write-sets") failed its body-read in the realizing dispatch —
  SKILL.md's per-path line form governs the LOCK's own pathspec,
  and a unit's write-set exists only as `--write-set` CLI args in
  briefs; the shipped parser documents its line form as inference
  (statiker_record.py, UNIT_WRITE_SET_RE block). Design, decided —
  derived from the requirement (unit write-sets must be
  desk-appendable record lines under the EXISTING entry grammar),
  with the parser following the settled form, never ratifying it:
  the form is `- F<n> [VERIFIED] unit U<k> write-set: <path> —
  basis: <the unit's brief>`, one path per line,
  latest-line-per-id supersede; `statiker_git.py unit-start`
  PRINTS the record lines for the desk to append (the tracker
  stays desk-append-only — one writer), and SKILL.md's
  Implementation section names the form beside the `--write-set`
  args (SKILL.md edit: skill-craft + the trial's opus skill-edit
  review). Realizing write-boundary: SKILL.md, `statiker_git.py`,
  `tools/test_statiker_git.py`. Verifier, red-first: unit-start's
  printed lines round-trip through `waves_over_units` into the
  partition; battery green; contract parity holds. Done-criterion:
  a real run's tracker carries machine-printed write-set lines and
  `waves` partitions them with no UNPLANNABLE flag.

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

- **PARKED — attack-round batching: one fresh-context trip carrying
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

## Done

- 2026-08-10 — **wave derivation (`waves`) + round-trend instrument (`trend`)**: shipped `1eb4380` (subcommands + red-first batteries, sonnet dispatch) and `4b56648` (contract battery rows + SKILL.md verdict routing), version bump `8a8ce22` (0.2.56). Deviation from the booking: the waves entry's "premise verified against the grammar" note was FALSE — no unit write-set record-line form exists in the grammar (the realizing dispatch's gap 1); `waves` ships reading a composed convention, failing loud (UNPLANNABLE) on every real tracker until the line-form mint above lands. Entry bodies retained above under superseded markers until the mint closes; drop them with it.

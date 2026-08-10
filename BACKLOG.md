# Statiker — backlog

Future work graded by decision-completeness (operator-corpus file
roles). PLAN.md stays the design record; entries here are work items,
and a SKILL.md change stays fire-born per CLAUDE.md — an entry can
build tooling, but a clause mint still needs its incident.

## Open

- **READY — mechanical wave derivation over unit write-sets: the
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
  collect each unit's declared write-set from the tracker, compute
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

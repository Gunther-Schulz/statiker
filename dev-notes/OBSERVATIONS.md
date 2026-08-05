# Statiker — observations journal

Maintainer-side, outside the plugin payload. Consumers: fire-rate
reviews (prune/keep decisions on fire-born clauses) and the
validation grading (PLAN.md, Birth process steps 4-5).

Behaviour-delta signature (what a statiker run produces that a bare
session does not): a `.clippy/runs/` tracker carrying the verbatim
request + requirements head, decision lines with bases, a recorded
fresh-context attack outcome, per-unit commit SHAs, and a verify
verdict with pasted check output. A run missing any of these is a
protocol violation, whatever the code looks like.

## Fire-born clause log

(none — zero clauses at birth, per PLAN.md. Each mint gets a dated
line here: incident, clause text location, subsequent firings.)

## Observations

- 2026-08-05 — **Mint candidate (first): inherited-evidence gap.**
  First trial run (opus desk shakeout,
  beat-the-books `.clippy/runs/2026-08-05-canonical-market-identity-statiker.md`,
  Stumbles S1): statiker 0.1.1 has no clause for a run inheriting
  ANOTHER run's F/D entries — the resume clause assumes the tracker's
  entries are the run's own. Incident: inherited F5(a) was wrong in a
  load-bearing way (wrong table; a migration built on it would have
  rewritten `game_markets` while the resolver's real reference source
  `provider_markets` stayed stale); only the dispatching brief's
  "adopt only what survives your own spot-verification" line forced
  the check (corrected as that run's F10, independently corroborated
  by a blind-briefed leg). Suggested clause shape in the tracker's S1.
  Decision point: mint at run grading, not mid-run (editing the skill
  under the run evaluating it muddies the trial measurement).

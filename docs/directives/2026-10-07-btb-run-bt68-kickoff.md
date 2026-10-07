# Kickoff directive — beat-the-books run on bt-68 (2026-10-07)

Driving desk: statiker-30 (this repo's meta session, opus).
Receiver desk: a NEW session the operator opens in
`/home/g/dev/Gunther-Schulz/beat-the-books` with
`claude --model 'opus[1m]' --autocompact 300000`. Its name is not
knowable before it exists; the operator's paste names this desk to
it, and its acknowledgment names it to this desk.
Arrangement: two-session layout, meta drives end to end (CLAUDE.md,
2026-08-23). ONE first-hand operator delegation line pasted at desk
start; every later authority line travels meta to desk under it.
The run is INERT until the desk's acknowledgment shows that line on
its record.

Why not the already-open session beat-the-books-bb: it was started
at 17:58:57 as `claude --model opus[1m]` (process list, read
2026-10-07), without the compaction window the depth-cap probe
needs and before the release, so it would serve 0.2.103.

## Served version
Installed pin statiker 0.2.105 at 622c27f
(`~/.claude/plugins/installed_plugins.json`, re-read after the
update; the cache copy compares equal to `plugin/` in this repo).
Review floor met: two fresh-context rounds over f954320..b65d673,
every finding dispositioned
(docs/audits/2026-10-07-eve-review-dispositions.md), then a
narrowing lap. The desk confirms the served version from its Skill
injection's base-directory line before the first forcing point;
expected 0.2.105.

## The task, and whose words it is
bt-68 in the target repo's ITEMS.md, READY and unblocked. Its
requirement, quoted: "Drain-effect alarms that ask each purge job's
own question: every retention alarm derives its threshold from the
config the drain reads and its row/file selection from the drain's
own predicate (one shared function per drain), covering evidence
rows and files, market_snapshots, and the replay_opportunity_cache
partitions (absorbs bt-64)". That text came out of the 2026-09-25
run's exported unit U4 under the operator's decision of that date
("U4 exported to a focused successor run"). The choice of bt-68 as
THIS run's task was a desk decision under the operator's
delegation of 2026-10-07 ("you decide"; LEDGER.md), and the
operator's first-hand line in this session, same date, names "the
run on bt-68 in beat-the-books". No further operator INTENT text
exists; the desk records the item's requirement as the requirement
head and marks its provenance as above, never as verbatim operator
intent.
bt-66 (the alarm service constructed only inside one lifespan
branch) shares `api/lifespan/autobet.py` with bt-68; whether it
rides is the run's own design call.
Re-read against the target repo on this date:
dev-notes/next-run-prep.md, "bt-68 re-read".
Containment: none declared for this run.

## State the desk should know
The target repo's `main` is 4 commits ahead of its origin
(0d0a45d5, b7f380a0, ac917aec, 0237b962). Pushing is that repo's
own rule and the desk's act there.

## What this run is also measuring (the desk is told none of it)
- st-92: the depth cap by compaction. Registration:
  dev-notes/next-run-prep.md.
- The convergence records' first operation: the field-test line in
  dev-notes/OBSERVATIONS.md, 2026-10-07 repair-lap mint record;
  graded for st-95.
- st-31: a shadow full V2 leg, run by this desk if a V1 → repairs →
  V2 cycle with a non-design repair occurs.
- At close: the two digest files st-83, st-90 and st-95 wait on,
  and the harvest's re-ask of the parked triggers.

## Meta cadence
This desk wakes at seams and judgment moments only (CLAUDE.md,
2026-09-29): a desk report landing, a hold, a stop-call candidate,
a decision round, a forcing-point boundary. Between them the
watching is an armed artifact poll over the run's tracker and an
idle subscription on each driving send.

## Horizon
The desk's acknowledgment is expected within minutes of the
operator's paste. This desk cannot arm a timer on a session that
does not exist yet, so the first wake is the acknowledgment
itself; if the operator reports the paste done and nothing has
arrived, that silence is a finding and this desk reads the peer
listing.

## Resume fallback (added 2026-10-08)

Both desks named in this directive were closed by the operator for
the night with the run in progress. `statiker-30` and
`beat-the-books-70` are no longer live channels. Current state and
how to resume: dev-notes/next-run-prep.md, "RUN STATE AND RESUME"
and its 2026-10-08 update.

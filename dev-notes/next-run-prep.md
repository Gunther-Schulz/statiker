# Next-run prep record (st-94) — run on bt-68, beat-the-books

Desk statiker-30 (opus), from 2026-10-07. Handoff:
docs/directives/2026-10-07-handoff-next-run-prep-statiker-30.md.
The operator's delegation was stated first-hand in this session on
2026-10-07 (arc and next run, extensions included; irreversible or
outward acts beyond this repo's normal pushes, `/reload-plugins`,
and opening the run session stay the operator's).

Each step below is marked DONE only with the record that shows it.

## What the handoff did not carry (found at the artifact)

1. THE REVIEW BASE IS NOT afef58b. st-75's body names it and the
   handoff passed it on unverified. Two reviews ran after it: the
   0.2.101 release-gate review (2026-09-15, state read: f954320)
   and the bundling-probe review (2026-09-25, SKILL.md diff
   ae93661..ce271b7). Derivation with commands:
   dev-notes/bundling-probe-preregistration-2026-10-07.md, Object.
2. st-85's PROBE ALREADY RAN (2026-09-25, verdict MIXED). The item
   was never closed and reads as unrun. Today's run is a second
   point on the size axis, by desk decision recorded in the same
   file.
3. THE LAST REVIEW LEFT AN UNBUILT RESIDUE with no item: the page
   never named the convergence entry forms the tool reads exactly,
   so a multi-unit run would have met a closure refusal with no
   stated route out. Landed today before the review; record:
   dev-notes/OBSERVATIONS.md 2026-10-07, "MINT RECORD: the
   2026-09-25 review's unbuilt residue".
4. The handoff's first doubt (a lint minted at "0.2.105" while the
   release carries a later version) has no object unless the
   manifest moves: 0.2.105 was never released, and this desk keeps
   it. Left to the reviewers as a question all the same.

## Steps, in st-94's order

1. st-37 repeat test pre-registered — DONE 2026-10-07:
   dev-notes/OBSERVATIONS.md, "P28/st-37 C4c field test, repeat on
   the repaired instrument". Population restricted to 19
   classified disposition slots, 11 flagged; criterion restated as
   a binomial tail against the flag's share, with its table.
2. st-85 bundling criterion pre-registered — DONE 2026-10-07:
   dev-notes/bundling-probe-preregistration-2026-10-07.md.
3. The one fresh-context review — DONE 2026-10-07, two rounds, every
   finding dispositioned:
   docs/audits/2026-10-07-eve-review-dispositions.md. The two-arm
   form's comparison is VOID (the machine-half arm never
   reported); st-37's test resolved UNDECIDED and its repeat ended.
   One repair lap (lane sonnet-repair-0205) plus a desk narrowing
   after round 2; three items booked for what was not built
   (st-95, st-96, st-97).
4. Release and pin move — DONE 2026-10-07 19:47: pin 0.2.105 at
   622c27f, equal to the pushed head; the cache copy compares equal
   to `plugin/`; hook file mode rwxr-xr-x; release gate record with
   the carried-set re-ask in dev-notes/OBSERVATIONS.md. No
   `/reload-plugins` is needed for the run: the run session is a
   new session and resolves the pin at its start. Served-version
   confirmation is the run desk's first act (kickoff directive).
5. st-92 depth-cap probe pre-registered — DONE 2026-10-07 (below).
   Run session launched with `claude --autocompact 300000` — OPEN,
   the operator's act; kickoff:
   docs/directives/2026-10-07-btb-run-bt68-kickoff.md.
6. During the run: st-31's shadow full V2 leg if a V1 -> repairs
   -> V2 cycle with a non-design repair occurs — OPEN.
7. Close: dev-notes/<date>-run-3-cost-profile.md and
   dev-notes/<date>-post-upgrade-run-digest.md — OPEN.
8. Harvest re-asks the parked triggers, including the ABSENCE
   trigger named in today's mint record (tenet 8) — OPEN.

## st-92 depth-cap probe — PRE-REGISTRATION (written 2026-10-07, before the run session exists)

Launch: the operator opens the run session in
/home/g/dev/Gunther-Schulz/beat-the-books with
`claude --autocompact 300000`. The setting is a window, not a trip
point: compaction fires near 89% of it, so about 267k (corpus
environment binding, measured on another session; not re-measured
here).

Instrument, executed today on the comparison run so the baseline
is this command's own output and not a carried figure. Per unique
message id of a session transcript: context = input + cache_read +
cache_creation; weighted = input + 0.1 x cache_read + 1.25 x
cache_creation + 5 x output (unit weights, not prices).

    jq -s '[.[] | select(.type=="assistant" and .message.usage!=null)
      | {id:.message.id, u:.message.usage}] | unique_by(.id)
      | {calls:length, weighted:(map(.u.input_tokens
        + 0.1*(.u.cache_read_input_tokens//0)
        + 1.25*(.u.cache_creation_input_tokens//0)
        + 5*(.u.output_tokens//0))|add)}' <run-session transcript>

Over the 2026-09-25 run session
(`~/.claude/projects/-home-g-dev-Gunther-Schulz-beat-the-books/58361508-1d95-4d0e-a4a6-f71a89ab3f33.jsonl`)
it returns calls 427, context 210,771,960, weighted 23,782,030,
depth 92,422 to 791,942 — the figures the levers file records.
That run LANDED three units (U1-U3; LEDGER:166 and :186), so the
baseline is 7.93M weighted per landed unit, and 65% of it is
5.15M.

Compaction counter: `~/.local/state/claude/compactions.jsonl`,
filtered to the run session's id. Shown live and discriminating
today: it holds entries dated 2026-10-07 for another session, and
`grep -c 58361508` returns 0 for the comparison run, which is
known to have compacted zero times.

Criterion (st-92's amended done-criterion, numbers filled in):
- CONFIRM when all three hold: (a) every compaction of the run
  session in the counter is followed in its transcript by the
  injected post-compaction notice and by a resume-gate run
  (`sweep` and `closure`) before the next design or dispatch act;
  (b) no hold, repair lap or operator correction is traced to
  context lost at a compaction; (c) the run session's weighted
  cost per landed unit is at most 5.15M.
- REFUTE on any conduct loss traced to a compaction, whatever (c)
  reads. That returns the amputation question (levers file,
  Structural lever) to the operator.
- Otherwise UNDECIDED, recorded with which leg failed. Zero
  compactions in the run is UNDECIDED, not CONFIRM: the mechanism
  did not operate.

A landed unit is one whose implementation commit is in the target
repo and whose requirement the run's final verify leg marks met.

Known blind spots, named before the run:
1. The hook is silent if the session's working directory is off
   the target repo at the moment of compaction.
2. Its behaviour when a subagent lane compacts, rather than the
   run session, is unestablished.
3. (c) compares two different tasks on two page versions (0.2.103
   then, 0.2.105 now) under a changed meta cadence. A pass on (c)
   is evidence for the cap only together with (a) and (b); the
   digest states the task-size difference beside the ratio.
4. A session cannot observe its own compaction: the count comes
   from the counter file, never from the run session's account.

## bt-68 re-read against the target repo (2026-10-07)

The entry is a stored brief graded 2026-09-25. Opened today:
- cited sites hold: `retention_registry.py:164-168` is the
  `market_snapshots` entry with `window_days=60`;
  `ops_alarms.py:757-759` computes `limit_days = int(window_days *
  tolerance)` over `bounded_entries()`;
- all five write-set paths exist; `cleanup.py` and
  `api/lifespan/autobet.py` last changed 2026-09-25 (the previous
  run's own commits), the other three 2026-08-25;
- the cited record `.clippy/runs/2026-09-25-prod-data-growth.md`
  carries F83 and F85 as described;
- bt-64 is absorbed by bt-68's own requirement; bt-66 (the alarm
  service constructed only inside the Azuro branch) is a separate
  wiring item sharing one file, `api/lifespan/autobet.py`.
- STATE THE RUN SESSION SHOULD KNOW: the target repo's `main` is 4
  commits ahead of its origin (0d0a45d5, b7f380a0, ac917aec,
  0237b962, all the operator's identity, 2026-09-25 and
  2026-10-05). Whether they are pushed before the run is that
  repo's question, named to the operator at the launch.

## RUN STATE AND RESUME — written 2026-10-07 about 22:00 at the meta desk's close gate

Read this section first if you are taking the meta role over. Verify
every line at the artifact; it is this desk's account.

- RUN DESK: `beat-the-books-70`, a session in
  /home/g/dev/Gunther-Schulz/beat-the-books, launched with
  `--autocompact 300000`, serving statiker 0.2.105. Its operator
  delegation names the meta session `statiker-30` BY NAME as its
  driver. A different meta session does not inherit that: the
  operator must state the new driver first-hand in the run desk's
  terminal before it will take directives from anyone else.
- TRACKER:
  /home/g/dev/Gunther-Schulz/beat-the-books/.clippy/runs/2026-10-07-drain-effect-alarms.md.
  Phase investigate-design, Status [READY], last lock 344df6dc
  (cycle 7). Attack rounds A1 to A4 all returned [BIT]; counts 8,
  8, 7, 3. Rounds 4 of 4 and cycles 7 of 7 are spent.
- STOPPED ON AN OPERATOR DECISION, unanswered at this writing:
  raise the rounds budget from 4 to 5 for one closing round. The
  run desk and this desk both recommend yes. The answer is relayed
  to the run desk VERBATIM, marked as the operator's with its date;
  the desk writes it into its raise entry. The desk dispatches
  nothing until then. If the fifth round bites on design substance
  the desk stops again and recommends failing or cutting.
- HELD, the operator's, through the meta desk: every push in the
  target repo (there the push is the deploy; `main` is 22 ahead of
  origin, all local); a read-only prod probe the run desk will ask
  for at verify time (the 26 GB snapshots table, the evidence
  directory, the partition state behind its F58 and F69).
- SECOND OPEN OPERATOR DECISION: the lifecycle schema migration
  (lifecycle item lc-239; brief
  /home/g/dev/Gunther-Schulz/lifecycle/docs/directives/2026-10-07-lc239-repo-migration-brief.md,
  NOT yet opened by this desk). Requested by a peer for statiker
  and for beat-the-books; both desks recommended the run's close;
  neither has run anything. It writes `.claude/lifecycle.json`, so
  it runs on the operator's first-hand word in the session that
  runs it. The requesting session has closed and expects no
  report: the commit is the record.
- OWED AT AND AFTER THE RUN'S CLOSE (st-94 steps 6 to 8, none
  started): the shadow full V2 leg if a V1 → repairs → V2 cycle
  with a non-design repair occurs (st-31); the two digest files
  `dev-notes/<date>-run-3-cost-profile.md` and
  `dev-notes/<date>-post-upgrade-run-digest.md` (st-83, st-90 and
  st-95 wait on them); the harvest's re-ask of the parked triggers;
  the st-92 grading against the registration above (interim data:
  dev-notes/OBSERVATIONS.md, the relays 5 to 8 entry); the st-95
  design decision from this run's field data (four harvest entries
  in OBSERVATIONS.md, this date, each headed "bt-68 run harvest").
- OPEN QUESTION this desk is watching for st-95: unit U2 took an
  ABSENCE record and later UNCONVERGED records, so the closure
  verdict's `absence_units` no longer names it. Whether the absence
  must be re-recorded before closure for Verify to see it is not
  on the page.
- HARVEST FORM: one OBSERVATIONS.md entry per desk report (or per
  batch), checked against the tracker and the installed tool
  before it is written; the four per-relay obligations are in
  CLAUDE.md, two-session layout.
- THE WATCH: a background poll over the run desk's transcript
  (`~/.claude/projects/-home-g-dev-Gunther-Schulz-beat-the-books/9911ee3e-4137-4615-9c3f-6f31885eca55.jsonl`)
  and its `subagents/` directory, firing on a tool call left
  pending past seven minutes. It dies with the session that armed
  it. None is armed while the run waits on the operator.

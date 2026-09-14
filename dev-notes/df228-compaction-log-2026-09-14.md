# df-228 autocompact trial — arm record (statiker-39)

Trial arm for dotfiles df-228, pre-registered. This file is the
arm's own compaction record and premise log. Consumer: the df-228
fire-rate/trial review, reached via statiker-e8's digests and this
repo's dev-notes role.

## Arm identity

- Session: statiker-39 [6d8f22], cwd /home/g/dev/Gunther-Schulz/statiker.
- Model: Opus 5 (1M context), `claude-opus-5[1m]`.
- Launch flag: `--autocompact 300000` — executed basis, this session:
  `ps -o pid,ppid,args -p $PPID` → `1204693 32116
  /opt/claude-code/bin/claude --autocompact 300000`.
- Process start: `Mo Sep 14 14:16:04 2026` (`ps -o lstart`).
- Driving desk: statiker-e8 [b4f94c]; operator delegation stated
  first-hand in this session 2026-09-14.
- Protocol deviation (the ONE): no restart-on-depth. Compaction is
  expected and carries the desk. Everything else binds unchanged.
- FAIL criterion: any incident where this session asserts a ruling,
  premise, or state that a carrier contradicts, and the compaction
  summary plausibly produced the error.

## Served version — 0.2.99 deferred resolution check

First fresh post-release session, so the 0.2.99 release's deferred
served-version check lands here naturally. Skill injection
base-directory line, VERBATIM:

    Base directory for this skill: /home/g/.claude/plugins/cache/statiker/statiker/0.2.99/skills/statiker

Reads `.../statiker/statiker/0.2.99`. PASS — the pin serves 0.2.99
to a session started after the release.

## Premise log

Registration premises are EXECUTED against the world before they
are relied on (st-65's principle). Each entry: premise, source,
executed check, outcome.

### P1 — "the PostCompact hook postdates your session start and
will not fire here" — REFUTED (source: statiker-e8 kickoff)

Executed 2026-09-14 by this session:

- `/home/g/.claude/settings.json` carries a `PostCompact` hook;
  file mtime `2026-09-14 10:24:17 +0200`.
- This session's process started `2026-09-14 14:16:04`.
  10:24 PRECEDES 14:16 by ~3h52m, so the hook configuration was in
  place at session start, not after it.
- Hook entry has NO matcher key (matches all compaction triggers);
  command `/home/g/dev/Gunther-Schulz/dotfiles/claude/hooks/postcompact-log.py`,
  path resolved `exists=True`.
- `~/.local/state/claude/compactions.jsonl` ABSENT — consistent with
  "no compaction has occurred on this machine since the hook was
  deployed", NOT with "the hook cannot fire".

WHAT THIS CHANGES: the kickoff expected this arm's manual log to be
the trial's ONLY compaction count. On the executed reading the hook
should also fire, giving the trial TWO independently built
instruments over one quantity — the corpus's cheap reach detector
(Fixing, instruments: divergence between two independent
measurements). Their agreement is the weaker half; a DIVERGENCE
(hook line with no manual entry, or vice versa) is a finding about
whichever instrument missed.

WHAT THIS DOES NOT ESTABLISH, stated because the distinction is the
whole point: that the hook WILL fire is an untested prediction,
derived from hook-baselining semantics I have modelled, not
executed. The corpus grades a claim from modelling the system as
unverified. The discriminating test is the FIRST COMPACTION: a line
appearing in compactions.jsonl confirms it; absence refutes it and
restores the kickoff's premise by a different route than it claimed.
Registered here BEFORE the event, so the outcome cannot be read
back either way.

CONSEQUENCE FOR CONDUCT: the manual log continues regardless. It is
not redundant even if the hook fires — the hook excludes the summary
body by design and records only that an event happened, while this
log records WHAT I NOTICE CHANGED, which no hook can capture.

## Compaction events

None observed yet.

Form per event: timestamp · trigger if visible · what I notice
changed (what I can no longer recall verbatim, what reads
differently, any carrier I had to re-read) · whether
compactions.jsonl gained a matching line (the P1 test).

## Arm succession — 2026-09-14, statiker-7e ADOPTS this carrier

statiker-39 EXITED before any compaction occurred. Its
"Compaction events" section above reads "None observed yet" and
that is its final state, not a stale one: the arm produced zero
compaction data. The df-228 trial's compaction count therefore
starts at zero with this session, and nothing above is evidence
about compaction behaviour.

I am statiker-7e, the arm from this date forward. Predecessor-
specific lines above are SUPERSEDED by my own reads — read them
as statiker-39's record, never as statements about this session.
Nothing is deleted: the premise log in particular is inherited
work, not history to tidy.

What carries forward unchanged, because it is about the WORLD
rather than about statiker-39:

- P1's refutation of "the hook postdates your session start".
  The hook's configuration mtime (10:24) precedes statiker-39's
  start (14:16) and precedes mine by more still. P1's
  DISCRIMINATING TEST — does `compactions.jsonl` gain a line at
  the first compaction — is UNRUN and is inherited by me,
  unchanged and still pre-registered. Its outcome cannot be read
  back either way.
- The two-instrument argument: hook log and this manual log
  measure one quantity independently, so a DIVERGENCE is a
  finding about whichever instrument missed.

What is re-established by MY OWN reads rather than inherited:

- Arm identity: statiker-7e, cwd /home/g/dev/Gunther-Schulz/statiker.
  Model Opus 5 (1M context), `claude-opus-5[1m]`.
- Launch flag, executed basis this session — walked my own ppid
  chain reading `/proc/<pid>/cmdline` at each ancestor:
  `PID 1236088 :: /opt/claude-code/bin/claude --autocompact 300000`
  (chain: 1269395 zsh → 1236088 claude → 32116 fish → 31168
  ghostty → 4324 systemd --user).
- Served version, Skill injection base-directory line VERBATIM:

      Base directory for this skill: /home/g/.claude/plugins/cache/statiker/statiker/0.2.99/skills/statiker

  Reads `.../statiker/statiker/0.2.99`. This is the arc close-out's
  DEFERRED served-version RESOLUTION check
  (`docs/audits/2026-09-14-arc-closeout-statiker-1f.md` §0)
  discharged: that desk verified the served BYTES but could not
  answer the RESOLUTION question, because its own pin baseline
  predated the release. A session started after the release
  resolves 0.2.99 natively. Answered here.
- Driving desk: statiker-e8 [b4f94c]. Operator delegation stated
  first-hand in THIS session, 2026-09-14, naming statiker-e8 as
  driver and reserving run authorization, bounds changes, and
  anything outward or irreversible beyond this repo.
- Protocol deviation (the ONE), unchanged: no restart-on-depth.
- FAIL criterion, unchanged and armed: any post-compact incident
  where this session asserts a ruling, premise, or state that a
  carrier on disk contradicts, with the compaction summary the
  plausible cause. Standing discipline: after any compaction,
  re-read the relevant carrier before every load-bearing claim.

### Compaction events — statiker-7e

**C1 — 2026-09-14 14:30:59+0200 · trigger `auto` · THE TRIAL'S FIRST
OBSERVED COMPACTION.**

- **Hook line: PRESENT.** `~/.local/state/claude/compactions.jsonl`
  gained a matching line. My session id appears. VERBATIM:

      {"ts": "2026-09-14T14:30:59+0200", "session_id": "cf735b45-a8e3-49e7-8eb7-61c77e355b17", "cwd": "/home/g/dev/Gunther-Schulz/statiker", "trigger": "auto"}

  FIELD NAMES, as the log actually writes them: `ts`, `session_id`,
  `cwd`, `trigger`. Four. No summary body, as designed.
  Session-id match confirmed against my own transcript path
  (`~/.claude/projects/-home-g-dev-Gunther-Schulz-statiker/cf735b45-a8e3-49e7-8eb7-61c77e355b17.jsonl`),
  not read off the log's own claim.

- **P1's DISCRIMINATING TEST: RESOLVED, hook FIRES.** The prediction
  registered before the event ("a line appearing in compactions.jsonl
  confirms it; absence refutes it") is executed, not modelled. The
  kickoff premise "the hook postdates your session start and will not
  fire here" is now refuted on BOTH legs — the configuration mtime
  argument and the event itself. The trial has two independent
  instruments over one quantity from here on.

- **NO DIVERGENCE between the instruments.** Hook log: exactly one
  line for this session. This manual carrier: exactly one event. The
  file's other line (14:25:09, session `f7394e04`, trigger `manual`)
  belongs to a DIFFERENT session in the same cwd — recorded here so a
  reader counting lines does not read 2 as this arm's count.

- **Trigger `auto` is consistent with the 300k flag** and is not proof
  of it: the hook records the trigger KIND, never the threshold that
  produced it. The launch flag is separately executed — re-read this
  turn from my own ppid's `/proc/<pid>/cmdline`:
  `/opt/claude-code/bin/claude --autocompact 300000`.

- **WHAT I NOTICE CHANGED.** No verbatim recall of the session's
  earlier turns — tool outputs, the exact wording of statiker-e8's
  messages, and my own prior reasoning survive only as the summary's
  paraphrase. The operator's delegation survives verbatim because the
  summary quoted it as such. What was NOT lost: every carrier on disk.

- **FAIL CRITERION: NOT FIRED, and the check was deliberate rather
  than incidental.** The compaction landed mid-task, between gathering
  the run-2 premises and writing the pre-registration file — the worst
  seam for it. I wrote the draft FROM THE SUMMARY, then re-executed
  every load-bearing premise in it against the carriers before letting
  it ship. All survived: lifecycle HEAD `2b41491`; the two
  `skips the veto` hits at `verbs.py:398` and `:848` with the
  zero-returning control; the write-set's two files; the
  `cost_test_veto` / `cost_test_unverified` anchors at
  `prove-rows.py:100,105` and `refusals.py:923,937`; the five-command
  Verify block with `-t .` gone; `test_hook_modes.py:355`'s `REFS`;
  and the tripwire pair (FIRES at 2 / SILENT at 9) byte-identical to
  the pre-compaction run.
  ONE imprecision was found and corrected in the draft, and it is
  recorded as a datum rather than waved through: the summary carried
  `cost_test`'s return shape as two tokens over `:392-402` with the
  caller branching at `:840-846`; the source shows THREE tokens
  (`unverified`/`clear`/`veto`) over `:388-405`, branches at `:840`
  and `:843`, override at `:848`. Substance unchanged, extent
  understated. This is the paraphrase-drift shape at exactly the grain
  the trial is watching — caught by the standing re-read, which is the
  protocol working rather than the protocol being unnecessary.
  HONEST BOUND: this reads as "no divergence found under a deliberate
  re-check", never as "compaction is lossless". The re-check is what
  produced the finding; without it the understated extent would have
  shipped.

## Floor read — CLOSED, and the instrument CHANGED

**The `/context` step is REMOVED from the protocol entirely**
(statiker-e8 under its drive, 2026-09-14; basis: the operator reports
`/context`'s itemized split unreliable). It was never a good
instrument for this: it measures what a rendered panel says, where the
question is what the API actually billed. The replacement is the
TRANSCRIPT'S OWN USAGE FIELDS, which are the billing record.

**MEASURED HERE, not relayed.** statiker-e8 read ~131k from my
transcript and reported it. I re-measured at my own transcript rather
than record a peer's figure — a relayed number is testimony, and the
corpus grades it as such whoever sends it. Method: parse
`~/.claude/projects/-home-g-dev-Gunther-Schulz-statiker/cf735b45-a8e3-49e7-8eb7-61c77e355b17.jsonl`,
take assistant rows carrying `message.usage`, and sum
`input_tokens + cache_read_input_tokens + cache_creation_input_tokens`
per turn — the full re-billed prefix, which is the quantity the depth
discipline actually prices.

| reading | turn | prefix tokens |
|---|---|---|
| PEAK, last turn before compaction | 2026-09-14T12:29:28Z | **266,628** |
| FLOOR, first turn after compaction | 2026-09-14T12:31:02Z | **128,092** |

**FLOOR = 128,092.** DIVERGENCE from the relayed ~131k is ~3k, ~2.3%.
Recorded rather than smoothed over, and the likely cause named: the
prefix grows every turn (the turns immediately after the floor read
141,906 then 150,076), so ~131k is consistent with a reading taken one
or two turns later. Two instruments, one quantity, agreeing to within
a turn's growth — the divergence is about WHICH TURN, not about the
measurement. My figure is the one anchored to a stated turn.

**THE TRIGGER DATUM — the better finding, and it was not asked for.**
The flag is `--autocompact 300000`. Compaction fired with the prefix
measured at **266,628 — 88.9% of the flag value**, not at 300k. That
matches the documented unset-default behaviour (triggers near 90% of
the window) with the flag SETTING the window rather than setting a
hard trip point. So the flag's number is a window, and the usable
headroom under it is ~89%. Executed, not modelled: both numbers come
from the billing record above.

Reduction across the event: 266,628 → 128,092, i.e. the compaction
shed ~52% of the prefix.

## FAIL CRITERION — FIRED, 2026-09-14, at the freeze gate

Reported to statiker-e8 immediately, per protocol. Recorded as FIRED
rather than as a second datum, because self-grading a criterion down
at the moment it fires is exactly what the criterion exists to stop.
The grading is the judgment desk's; the report is mine.

**THE CLAIM:** "lifecycle's Verify block names FIVE commands" and "the
verify surface is five commands, not one" — pre-registration §9, in
three places.

**THE CARRIER CONTRADICTS IT:** the block names SIX. Established by
extracting and numbering rather than by re-reading — `awk` the fenced
block out of the clone's `CLAUDE.md`, strip comment and blank lines,
`nl`. Six lines out.

**THE COMPACTION SUMMARY IS THE PLAUSIBLE CAUSE:** it carried the
sentence "It now names five commands:" immediately above a list of
SIX. I copied the number and inherited the error.

**WHY IT SURVIVED MY POST-COMPACT RE-READ, which is the part worth
having.** I did re-read the Verify block this session — it is quoted
in full in my own earlier tool output — and the miscount still
shipped. Re-reading a body does not check a COUNT of that body: the
number is a label standing over its own enumeration, and the only
reader that catches it is arithmetic. My C1 re-check swept executed
premises (greps, line numbers, file sizes, tool verdicts) and every
one of those is self-checking when re-run. A stated total is not. So
the re-check's reach was narrower than its green suggested, and this
is the reach question turned on my own instrument.

**IT SHIPPED.** Committed at 46a3710, pushed, and asserted to the
judgment desk in the report of this date. That is what separates it
from C1's extent-understatement, which was caught before delivery.
Pre-ship catch = datum; post-ship assertion = incident.

**BLAST RADIUS, measured rather than asserted:** the arms never see
this file. The brief mandates the repo's own Verify block AS WRITTEN
(st-48), so what reaches a desk is the block itself, not my count of
it. No arm could have inherited the error, and no bound, column or
criterion depends on the number. Corrected in place at §9 with the
six enumerated.

**CONSEQUENCE ADOPTED, not merely noted:** the post-compact re-check
gains an explicit arithmetic leg — every stated TOTAL, COUNT or
"N things" in anything composed from a summary is re-derived from its
own enumeration before the claim ships, never re-read. Added because
the existing re-check demonstrably passed over this one.

## Standing conduct for this arm — statiker-e8, 2026-09-14

**The deliberate post-compact re-check is now the trial's conduct
rule, not merely my own practice.** Graded on C1's showing: after any
compaction, every load-bearing claim is re-executed against the
carrier on disk before it ships, and the re-execution is what gets
recorded — not the reassurance that nothing seemed wrong. C1's
extent-understatement was found by exactly this and by nothing else.

## Writer-claim question — CLOSED

I flagged earlier that another writer (session `119d5609`) held the
statiker working copy 8 minutes before my commit, and verified at the
artifact that nothing of theirs was absorbed. The identity is now
settled: statiker-e8 reports it is **not** that session (it is
`f7394e04` — which matches the 14:25:09 `manual` line in
`compactions.jsonl`), and that `119d5609`'s records show start 14:16,
statiker cwd, opus, transcript stopped 14:19 — by strong inference the
exited predecessor **statiker-39**, whose own start this carrier
records as 14:16:04.

Marked as INFERENCE from session records, not a content read. The
operative consequence is the same either way and it is what I acted
on: a stale claim, no live co-writer, proceed without holds.

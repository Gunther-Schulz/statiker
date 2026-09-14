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

None observed yet. Same per-event form as above.

Floor read (the incompressible depth with the skill resident),
recorded when the operator's `/context` readout lands: PENDING.

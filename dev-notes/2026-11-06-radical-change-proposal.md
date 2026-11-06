# Proposal: a radical change batch for statiker (2026-11-06)

Desk: opus session of 2026-11-06. The operator asked this question:
"based only on the options for change we have in front of us, with
nothing holding back, what would you change?" Context: the operator
judges iterations too slow in practice, and beat-the-books (the main
test bed) is dead (LEDGER, superseded line of this date). This file
is a PROPOSAL. Nothing here is decided until the operator says so.
Observed facts carry their command or file. Everything else is
marked derived.

## Measured state

- SKILL.md: 2080 lines, 18,369 words, 118,715 bytes, 1978
  operational lines by the Verify awk (`wc`, run 2026-11-06). Scripts:
  5282 lines (`statiker_record.py` 3620, `statiker_git.py` 1491).
- EGM comparand (`~/dev/reference/elephant-goldfish-model`): seven
  skills of 67 to 427 lines each, plus ten agent files of 30 to 101
  lines. `tests/unit/test_skill_load_limits.py` fails any skill body
  over 24,000 bytes, with the message "move details into an
  explicitly read reference". Statiker's single body is about 5x
  that limit.
- Run endings since the per-unit gate: one ran out of budget
  (2026-09-25), one is suspended (bt-68, now dead with its project),
  and one went around the gate by declared deviation (bt-77, D27).
  No run has reached the gate's own end state (OBSERVATIONS
  2026-11-06).

## Changes, in priority order

1. **Stop rule: a stakes-scaled severity bar.** At seed, the run
   records a severity bar scaled to its exposure. The closing gate
   then reads "no design finding at or above the bar", instead of "no
   design-amending disposition at all". Findings below the bar still
   take a disposition (fix without a new round, export, or accept as a
   risk) and never sustain a round. The attacker grades severity
   against a rubric fixed at seed, and the desk may contest a grade
   with evidence but never downgrade it. Contested or accepted
   findings are SETTLED and do not reopen when a later attacker
   raises them again. Fixed findings reopen at the same scope. One
   clean round closes the design, not EGM's two.
   Derived basis: bt-68's A4 returned only MINOR findings while the
   gate stayed shut (tracker line 178). bt-77 needed D22 to stop.
   The page's existing "declining max-severity is convergence" reaches
   record findings only (SKILL.md ~1476).
2. **Paraphrase-back in the attack return.** The attacker first
   restates the design and the intent. The desk checks that summary
   against the RECORDED intent and R-lines. Findings that rest on a
   wrong summary are contested as misreads. This is part of the stop
   fix, because a finding about a design that does not exist is noise
   that holds a round open.
3. **Split by READER, not by branch (the EGM shape).** The desk page
   keeps the forcing points, the gates, and the dispositions. The
   attacker, implementer and verifier instructions move to role files
   that the lane reads itself, and the desk's brief passes the file's
   path. A brief check can then verify that the path is present.
   Derived: the 2026-09-15 split NO
   (docs/audits/2026-09-15-phase0-split-question-analysis.md) tested a
   desk-loaded core plus branch references. A grep of it for
   subagent, role-file and per-role terms finds no test of a split by
   reader. Its central worry was a rule behind a pointer the desk may
   skip. That worry is weaker when the reader is a lane whose whole
   job is that file. Not verified by a full read.
4. **Tools write the grammar; the page stops teaching it.** Record
   lines are composed by tool verbs (for example `record add finding
   …`), and every verdict prints its next action. A grammar paragraph
   leaves the page once a tool writes and validates that form. This is
   st-83 done wholesale instead of one dry-run-gated instrument at a
   time. Target: an EGM-style byte limit enforced by a test.
5. **Process: one redesign batch under a suspended mint ceremony.**
   For this batch, per-mint ceremony is replaced by red-first tests
   per change plus ONE fresh-context review of the whole batch before
   the pin moves. The suspended ceremony is the incident-provenance
   bar, the nine-tenet record per mint, and the C4b reading per
   repair. Those floors stay: red-first instruments, one review before
   any real run, and pre-registration of any comparison.
6. **Test bed without beat-the-books.** First an offline replay of the
   three recorded trackers under change 1, with its stop-point
   predictions registered before the replay. Then a live run on a
   replacement project the operator names.

## Costs and risks (derived)

- Change 1 can let real defects below the bar through. The verify
  phase and the one-review floor are the net. A dishonest severity
  grade is the attack surface, and change 1's no-downgrade rule
  answers it.
- Changes 3 and 4 are a large rewrite, and a large rewrite is fresh
  attack surface. Lap A of the compression pass overran its targets
  14 of 15 times (CLAUDE.md, aggregate-justified programs). A sample
  probe comes first: one role file and one grammar paragraph moved,
  measured, then the rest.
- Change 5 overrides operator-settled conventions (birth-class
  discipline, C4b, the tenet check). It needs the operator's
  first-hand word and an end condition: the batch's release.

## Candidates raised after the GO (weigh at st-99 start, not decided)

- **A design-blind acceptance oracle** (from a public comment on EGM,
  dev-notes/egm-comparison-2026-11-06.md). Before the attack, a fresh
  lane that sees the intent and the requirement head but NOT the design
  writes the acceptance checks. The attacker then grades the design
  against them, and verify reuses them. This targets the case a cold
  read misses: a wrong assumption the design shares with its author.
  It is the corpus parentage rule (expectations derived from the
  definition, never from the artifact) moved before the design.
  Cost: one extra lane per run.
- **One attack round by default** (syv playbook, executing-plans §4;
  dev-notes/syv-playbook-comparison-2026-11-06.md). After round 1,
  each repair carries its own red-first test. A re-attack happens only
  when a repair changes the design's shape: a new unit, a new
  mechanism, or an amended requirement. This is the radical end of
  change 1. Weigh it in the replay: would the late rounds of the three
  trackers have found anything that the repairs' own tests could not?
- **A "declined to judge" slot in the attack return.** The attacker
  lists what it set aside, with a reason, and the desk dispositions
  each line.
- **A "cost if wrong" slot on D-lines** (cheap / moderate / expensive),
  as the input that change 1's stakes-scaled bar reads.
- **Severity re-grade with a written reason.** The desk may re-grade a
  finding up or down only with a user-impact reason recorded in the
  tracker, where verify can attack it. Never silently. This is the
  middle ground between EGM (no downgrade) and the playbook (severity
  is advice).

## Open question raised by the operator, 2026-11-06: is statiker still worth building?

Desk recommendation, not decided. Before st-99 builds anything, run a
pre-registered three-arm comparison on one real task: (a) statiker;
(b) the syv playbook's executing-plans or work-autonomously with its
single fresh review, plus the operator corpus; (c) a bare session plus
the corpus. The criteria are fixed before any arm runs: defects shipped
and then corrected, cost in turns and tokens, and operator interactions.
Basis: the control arm (dev-notes/control-arm-hotfix-2026-08-26.md)
found that the corpus alone bought verification at the effect site and
the record's form, and that what it did not buy was "a second reader".
Both EGM and the playbook now provide a second reader. If arm (b)
matches (a) on defects at lower cost, st-99 shrinks to what (b) lacks
(the executed attack, the record), or statiker stops. Blocked on the
same test project as st-100.
- Constraint (operator 2026-11-06: "simple tasks dont expose the
  power, thats the problem"). The comparison task must be HARD:
  several units, a money or irreversible path, and at least one
  defect that needs a discriminating instrument. Record support: in
  the control arm the bare session was faster on small units and
  worse on the one hard unit (write-on-change: 10 commits, 3
  corrections, "cost roughly a day").
- A test bed that needs no live project (desk proposal): replay HARD
  historical tasks from the beat-the-books git history, whose defects
  are already known from later corrections. Each arm starts at the
  commit before the task, with the same task text. The criterion
  counts which of the known defects each arm catches before shipping.
  First candidate: the write-on-change unit (7d22fdcb..0d166689). The
  limit: Azuro is offline, so no arm can verify at the effect site.
  The replay grades design and code defects only.

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

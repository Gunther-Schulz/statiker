# Handoff — analysis of the 0.2.105 review-and-repair series, to desk statiker-a2 (2026-10-07)

From desk statiker-30 (opus, this repo's meta session, driving the
next run). You hold the judgment of this item; nothing in it is a
build order.

REPORT-CHANNEL: SendMessage statiker-30
RUN KIND: DISCOVERY (an analysis; it books proposals, it builds
nothing)
CADENCE: one message when the analysis file is committed, carrying
its verdict in a few lines and the file's path; a message at once
if you are blocked. No interim progress messages.

## Authority and why this desk

The operator asked for this in the sending session, first-hand,
2026-10-07, quoting the sender's own close report: "yes lets book
an anylsis of tihs so it can be improved OR maybe even better do
the analysis now and maybe get the help form a fabvle session:
@statiker-a2". That reaches you as the sender's testimony about a
request, which is all it needs to be: the work is reading this
repository and writing ONE new file in it. It asks nothing your own
session's permissions and instructions would not allow unasked. If
anything here seems to need more than that, do not do it; say so.

Two reasons it is yours and not the sender's. This repo's desk-tier
rule reserves open design tension and corpus-grade rule work for
the top tier. And the sender is a PARTY: its briefs, its
dispositions and its rulings are part of what is being graded, so
its reading must not be the one that grades them.

Known hazard of your tier in this repo, from the corpus: fable's
classifiers decline security-adjacent vocabulary, and this repo's
record is full of it (holds, gates, exemptions). A reply lost to a
refusal is backpressure, not a verdict. If it happens, tell the
operator in your terminal; the sender's horizon will catch the
silence either way.

## The question

The operator's framing is the sentence they quoted: a review series
that keeps finding defects in the newest repair "says the approach
is wrong". They want it understood so it can be improved.

Answer, from the record and not from this file:

1. WHICH diagnosable causes produced this release's excess — two
   fresh-context review rounds both returning HOLD (18 findings,
   then 14), one repair lap, then a narrowing — and where in time
   each cause entered. The repo's rule applies: efficiency reviews
   lead with causes, never arithmetic, and round count is an
   output, not a knob (CLAUDE.md, trial working conventions).
2. For each cause: what was the EARLIEST and CHEAPEST point at
   which something already in this repo's conventions, the page, or
   the corpus should have caught it, and why it did not fire. A
   rule that was loaded and did not fire is a different finding
   from a rule that does not exist.
3. What, if anything, should CHANGE — and what should NOT be
   minted. This repo's own economics lens binds your proposals: a
   mint names the defect class, its cost in both currencies (turns
   and corpus lines), and whether an existing clause or
   judgment-in-prose could carry it instead. A proposal that only
   ratifies this incident's shape is the rigidity the lens exists
   to stop. "Nothing new; rule X under-fires at seam Y, and here is
   the form that makes its absence visible" is a full answer.
4. The sender's conduct, graded as a cause like any other: its
   briefs, its two rulings reversed by measurement (the last
   reviewed state it inherited; "a design-time unit has no
   machine-readable declaration"), its decision to repair
   incrementally after round one instead of narrowing then, its
   decision to stop after round two. Say where it was wrong.

The sender has a reading. It is in its records below and it is one
hypothesis among those you should try to REFUTE, not a frame:
"the convergence gate was completed by repair increments without
ever having operated in a run, and each increment exposed the next
seam". A second candidate the sender did not examine: whether the
repair lap's own shape (a disposition-briefed lane building a lint
'on the precedent' of an existing one whose repair route was never
exercised end to end) is a separate cause. A third, older: this is
not the first such series in this repo. Search for the solved-
before and the repeated: the 2026-09-10..12 burst (CLAUDE.md,
"Maintenance arcs open against a named consumer"; "Mint form is
priced in the batch plan"), the 0.2.84 to 0.2.86 batch, the
0.2.89 review. If the same class has been diagnosed here before
and a convention was minted for it, the finding is that the
convention did not hold, and why.

## Evidence — every pointer is graded; open what you rest on

Opened by the sender today (its own work or its own executed
reads):
- docs/audits/2026-10-07-eve-review-dispositions.md — all 32
  findings with dispositions, both rounds.
- docs/audits/2026-10-07-eve-review-raw-reports.md — the four
  reporting lanes' own messages, verbatim, extracted from their
  transcripts. Prefer these over the dispositions' paraphrase.
- docs/audits/2026-09-25-bundling-probe-raw-reports.md — the three
  reviewer reports of the review that preceded today's, verbatim.
- dev-notes/OBSERVATIONS.md, the entries headed 2026-10-07 (seven
  of them: the residue mint record, the st-37 registration and
  outcome, the repair-lap mint record, the second round and the
  narrowing, the release gate record with the carried-set re-ask)
  and the 2026-09-25 entries above them (the mint record of the
  three attack-loop clauses, the fire record of the altitude
  amendment, the executed-probes mint).
- dev-notes/bundling-probe-preregistration-2026-09-25.md (with its
  addendum: twelve clusters, dispositions, a four-step repair plan
  of which steps 3 and part of 2 were never run) and
  dev-notes/bundling-probe-preregistration-2026-10-07.md.
- docs/directives/2026-10-07-sonnet-repair-0205-brief.md — the
  repair lap's brief, the sender's.
- docs/directives/2026-10-07-handoff-next-run-prep-statiker-30.md —
  what the sender inherited.
- LEDGER.md, the lines containing "ST-85 TOOL HALF", "PROSE LAP
  LANDED", "BUNDLING-PROBE ARMS DISPATCHED" (2026-09-25) and this
  date's five decision lines.
- ITEMS.md, blocks st-95, st-96, st-97 (what was booked instead of
  built) and st-94.
- The code and page as shipped: `git diff f954320 622c27f -- plugin
  tools`; the key commits are 4000538 and 0220913 (the tool half,
  2026-09-25), ae19e24, 0bb6fd6, f1bebcc, b65d673, f5de5b5,
  622c27f (this date).
From the sender's memory of this session, unverified, check before
resting on it: the first-round machine-half lanes each ran about 34
tool calls before stalling; the first poll false-fired in under a
minute; total elapsed from first review dispatch to release was
about one hour fifty minutes (17:56 to 19:47 local).
Not available to you: the sender's own turn-by-turn reasoning. Its
session transcript is
`~/.claude/projects/-home-g-dev-Gunther-Schulz-statiker/7196f402-db3b-4933-bcaa-2e10d71d56b0.jsonl`
if a claim about its conduct needs checking; reading it is
optional and large, so price it before you pull it.

## Write boundary

The sender is the writer of this working copy and stays so. You own
exactly ONE path, which does not exist yet:
`dev-notes/2026-10-07-repair-series-analysis.md`. Create it, and
commit it by pathspec with every flag before the separator —
`git -C /home/g/dev/Gunther-Schulz/statiker add -N <that path>`,
then `git -C ... commit -F <message file> -- <that path>` — with
your own attribution trailers. Do not push; the sender pushes at
integration. Edit nothing else: not SKILL.md, not CLAUDE.md, not
OBSERVATIONS.md, not the item or ledger carriers. Proposed rule
text goes IN your file, pre-formulated, with the place it would
land named; whether any of it mints is decided afterwards, with the
operator, through the sender.
State-dependent: valid while
`git -C /home/g/dev/Gunther-Schulz/statiker log --oneline -1 -- dev-notes/2026-10-07-repair-series-analysis.md`
prints nothing. If the file already has a commit, report that
instead of writing.
The sender may commit to other paths while you work (the run it
drives books into LEDGER.md and dev-notes/OBSERVATIONS.md). That is
why your commit is by pathspec and why a foreign commit on top of
your base is not a halt here, provided your one path is untouched.

## The form of the answer

In your file: a lead the operator can read alone (what caused it,
what to change, what to leave), then the causes in order of how
much of the excess each explains, each with its basis as a file
and line or an executed command, observation kept visibly apart
from inference. Then the proposals as a numbered decision round,
each with your recommendation. Then what you did not reach.

## Horizon

The sender arms a 45-minute horizon on the file's first commit.
Silence past it is a finding the sender acts on by reading your
state in the peer listing, then asking.

## What stays the sender's

Integration and the push; the item and ledger bookings that follow
from your proposals; carrying the decision round to the operator.
Check at close, run by the sender: `git log origin/main..main`
shows your one commit claimed, and every proposal in your file has
an exit — minted, booked, or declined with its ground named.

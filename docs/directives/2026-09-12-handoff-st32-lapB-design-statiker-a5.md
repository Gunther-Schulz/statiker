# Handoff: st-32 (compression lap B) design pass → statiker-a5

Sender: statiker-df (opus desk, statiker maintenance arc), 2026-09-12.
Receiver: statiker-a5 (fable). Tier basis: CLAUDE.md's desk-tier fit
(operator-settled 2026-09-11) reserves fable for open design tension;
st-32's own `blocked-by` names the tension — "the design's §3 sketch is
marked e.g., not decided".

Run declaration: DESIGN (no build, no tool or page edit).
REPORT-CHANNEL: SendMessage statiker-df
Cadence: a one-line acknowledgment; one report when the design doc is
committed (commit hash, the verdicts of §§1–5 below in ≤3000 chars, a
pointer to the doc for the rest); an immediate message only for a
blocker or a question only the operator can answer.

Binding: this handoff is INERT until the operator states the delegation
FIRST-HAND in statiker-a5's session. A relayed authority line is
testimony, not a decision (measured on the U2 run, 2026-08-23: a desk
correctly refused a relayed authority block and stopped clean). Once
that line is on your record, acknowledge to statiker-df, then start.

## The question

statiker's SKILL.md is 1628 operational lines against a 150-line
target. The compression pass runs in three laps; lap A (delete +
tighten) released as 0.2.88. **Lap B is the precipitate lap, and its
design is not settled** — that is what you decide.

The settled part (do not re-open): verdict ROUTING moves off the page
and into the record tool. Each emitted verdict carries a
machine-readable route field; the page keeps the vocabulary and the
principles, not the per-verdict map. `test_contract.py`'s bidirectional
verdict parity is REPLACED by route-field parity in the same commit.

What you decide and write:

1. **The closed route vocabulary.** The prior design sketches
   `proceed / halt-uncommitted / book-and-halt / book-and-continue /
   repair-from-verdict / surface-to-operator` and marks it `e.g.` — a
   sketch, not a decision. Decide the actual set, with the reasoning
   that makes it closed: what forces a new member, what an unroutable
   verdict does.
2. **The per-verdict mapping.** Every verdict the scripts emit gets a
   route. Where today's page routes a verdict in prose that no single
   route token captures, say so — that is a finding about the page's
   routing, not a gap in your design.
3. **The replacement parity contract.** What `test_contract.py`
   asserts once bidirectional verdict parity is gone, such that the
   check still catches what parity caught (a verdict emitted and
   routed nowhere; a verdict named on the page that no script emits)
   and does not become an assertion the page can no longer falsify.
   Name the red-first arrangement the build lane will use: which
   expectations run against which old side, and what the baseline is.
4. **What stays on the page.** The design's §2 mass estimates
   (tools residue ~25, lock routes ~70, unit routes ~80, record
   read-side ~100, attack routing ~50 lines) are estimates by another
   session — re-measure what you rely on. State what the page keeps as
   principle + vocabulary and what leaves.
5. **st-19's three collected items** — `r4-H1` (the commit gate's …),
   `r4-M4` (the budget-raise entry's …), `r3-MINOR-5` (a lint class
   for a world-facing …), bodies at `BACKLOG.md:646-662` — graded
   in-scope for lap B or re-parked with a named trigger. st-32's
   done-criterion demands this grading at brief time, which is here.

Out of scope: lap C (st-33), the size-target re-derivation, and the
disclosure question (§5 of the prior design) — all booked separately.
Also out of scope: st-35's tripwire ARMING ruling, which statiker-df
holds.

## Read path

1. `docs/directives/2026-09-11-st29-compression-design-statiker-fb.md`
   — the prior design pass (statiker-fb, fable, commit `1e10047`), §2
   (line budget) and §3 (staging; lap B is the third bullet, content
   anchor "Lap B — precipitate (tool + page + both test files; the
   heavy lap)"). Its lap-B paragraph is your starting point and its
   `e.g.` is what you replace. Its numbers are ESTIMATES by that
   session, labeled as such there.
2. `ITEMS.md`, entry `## st-32` (line 126 at base `6137ea3`; content
   anchor `grade: PARKED` + `requirement: st-29 lap B (compression
   pass, precipitate)`). Its `done-criterion` is what your design must
   make executable; its `write-set` is the build lane's, not yours.
3. `plugin/skills/statiker/SKILL.md` — the whole page, 1628
   operational lines at base. The routing prose is the mass you are
   moving.
4. `plugin/skills/statiker/scripts/statiker_record.py` — the verdict
   emission sites (`finish(...)` calls) and `RULE_MINT_VERSION`.
5. `tools/test_contract.py`, class `TestVerdictParity` — at base
   `6137ea3` it is at **line 1092** (two tests:
   `test_every_emitted_verdict_is_routed_in_skill`,
   `test_every_skill_named_verdict_is_emitted`). NOTE the offset:
   st-32's requirement text cites `:1042-1051`, which lap A's rewrap
   moved; the content anchor above is authoritative, the line number
   is not.
6. `CLAUDE.md` — Single-home by design; Birth-class discipline; the
   trial conventions (skill text states current decisions cleanly;
   efficiency reviews lead with causes; the economics lens).
7. `LEDGER.md` — the compression-order decision (delete/tighten →
   precipitate → close) and the 2026-09-11 batching decision.

## Provenance grades on this handoff's claims

- Opened by statiker-df at compose time: the SKILL.md line count
  (`awk '/^---$/{c++} c>=2' … | grep -vc '^$'` → 1628);
  `TestVerdictParity` at `tools/test_contract.py:1092`; st-32's item
  body; the fb design's §2/§3 text.
- **Unverified, from ITEMS.md st-19**: "all three [r4-H1, r4-M4,
  r3-MINOR-5] still self-declared parked in SKILL.md". Those three
  tokens do NOT occur in SKILL.md at `6137ea3` (ugrep -E over the
  repo: hits only in `ITEMS.md`, `BACKLOG.md`, `dev-notes/
  OBSERVATIONS.md`, and the fb design doc). Either the page declares
  them in prose under other wording, or lap A removed the
  declarations. Settle it by reading the page; report which.

## Write boundary

- You write exactly ONE file:
  `docs/directives/2026-09-12-st32-lapB-design-statiker-a5.md`.
  Create it with `git add -N <path>` first, then
  `git commit -m "…" -- docs/directives/2026-09-12-st32-lapB-design-statiker-a5.md`.
  Every flag before the `--`; never `git add` then `git commit`, never
  `-A`, never `--amend`.
- This working copy is SHARED. A subagent lane (`sonnet-st34-tools`)
  is writing `plugin/skills/statiker/scripts/statiker_record.py`,
  `plugin/.claude-plugin/plugin.json`, `tools/test_statiker_record.py`,
  `tools/test_contract.py` and `tools/golden-corpus/*` concurrently.
  Read those files freely; write NONE of them, and expect their
  content to move under you — anything you cite from them carries the
  sha you read it at.
- Commit UNPUSHED. statiker-df pushes.
- Trailer: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`

## Obligation split

- Receiver (statiker-a5): the design doc committed, the
  acknowledgment, the design report. Your write boundary covers the
  doc only — you do NOT amend `ITEMS.md`, `LEDGER.md` or
  `dev-notes/OBSERVATIONS.md`.
- Sender (statiker-df): grading the design, the st-32 item amendment
  (slots + blocker), the LEDGER entry, the build lane's brief, the
  push, and the operator-facing summary. At close statiker-df checks
  your commit is on the remote and that st-32's done-criterion is
  executable against your design.

## Horizon

statiker-df arms it: acknowledgment within ~20 minutes of the
operator's line; the design report within ~2 hours of the
acknowledgment. Silence past either is a finding on statiker-df's
side, never more waiting.

## Report form

Your report carries, in ≤3000 chars: the five verdicts above in one
line each, the commit hash, what you could not settle (returned as a
question with its evidence, never settled below the operator where it
is the operator's), and every claim about something outside your own
work either with the read that opened it or graded "inferred,
unverified". Your final session text reaches no one — the report
travels by SendMessage to statiker-df.

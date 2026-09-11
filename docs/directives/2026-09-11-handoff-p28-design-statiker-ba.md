# Handoff: st-10 (P28) design pass → statiker-ba

Sender: statiker-4d (opus desk, statiker maintenance arc), 2026-09-11.
Receiver: statiker-ba. Authorized by the operator in statiker-4d's
session ("you can hand the fable job to @statiker-ba").

Run declaration: DESIGN — discovery-shaped. It books nothing; it
closes by delivering one design file and a recommended disposition
for st-10.
REPORT-CHANNEL: SendMessage statiker-4d
Cadence: one message when the design settles (pointer to the file +
the recommendation, ≤3000 chars); an immediate message for a blocker
or a question only the operator can answer; nothing otherwise.
Binding: inert until the operator states this delegation FIRST-HAND
in statiker-ba's session. Once that line is on your record, send
statiker-4d a one-line acknowledgment, then start.
State token: valid while ITEMS.md shows `## st-10` with `grade:
PARKED` and a latest blocked-by naming the P28 design pass. If it
does not, report to statiker-4d and do not start.

## The question

P28 (st-10): repairs mint defects — a repair's own NEW surface
(closure prose, a repair-introduced predicate or design decision)
counts as closed without an executed-evidence attack on that
surface, and the next round finds its defects there. Design the
mechanism that closes this class at acceptable cost in the repo's
two currencies (turns, SKILL.md corpus lines) — or show the class is
judgment-shaped and the existing fresh-context round already is the
mechanism, naming what it misses and what that costs. You design;
you do not mint.

## Read path

1. Repo CLAUDE.md in full — trial conventions: mint timing, the
   economics lens and its ATTACK TIMING edge, desk-tier fit,
   efficiency reviews lead with causes, verification laps run on the
   final form, n=1 and its safety-floor boundary.
2. PLAN.md, the tenet list (`## Mission and tenets`, items 1–9).
3. ITEMS.md `## st-10`, every slot line.
4. BACKLOG.md:279-317 — the P28 body (five incidents, the run-2
   close-grading split, the lineage left unabsorbed).
5. dev-notes/OBSERVATIONS.md: the D38 post-round seam booked as
   P28-class evidence (~:7832, run 3); and the three review-round
   sections on the 0.2.84/0.2.85 batch, anchored on their headings —
   `2026-09-10 — 0.2.84 checkpoint-review dispositions`,
   `2026-09-10 — 0.2.84 re-review dispositions`,
   `2026-09-11 — 0.2.85 checkpoint-review dispositions` (series:
   blocking 6 → 2 → 1, later rounds concentrated on the previous
   lap's own surface).
6. SKILL.md at a PINNED commit only: `git show
   b6d5beb:plugin/skills/statiker/SKILL.md`. A repair lane edits the
   working copy's SKILL.md and tool while you read; the live files
   move under you.

## Write boundary

- You write ONE file: `docs/directives/2026-09-11-p28-design-statiker-ba.md`.
  Commit it by pathspec (`git add -N <path>` first, then `git commit
  -m "…" -- <path>`), with your own Co-Authored-By and
  Claude-Session trailers.
- NEVER push. This working copy carries a repair lane's unpushed
  version bump; a push publishes it and re-arms the payload-version
  guard against that lane's remaining commits. statiker-4d pushes
  your commit at integration.
- Touch nothing else: not ITEMS.md, ITEMS-DONE.md, LEDGER.md,
  BACKLOG.md, OBSERVATIONS.md, PLAN.md, SKILL.md, the tool, or tests.
  No dispatch that writes the repo.

## Obligation split

- Receiver (statiker-ba): the design file, committed unpushed; the
  acknowledgment; the design-settled report.
- Sender (statiker-4d): pushing your commit; st-10's re-grade from
  your file (READY with slots quoted from it, or drop/park per your
  recommendation); every LEDGER/OBSERVATIONS/ITEMS line. Check at
  close, run by statiker-4d: your commit is on origin, and st-10's
  latest grade line cites the file.

## Horizon

statiker-4d arms it: acknowledgment within ~20 minutes of the
operator's line; the design report within ~90 minutes of the
acknowledgment. Silence past either is a finding on statiker-4d's
side, never more waiting.

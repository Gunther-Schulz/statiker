# Handoff: batching / merging rounds → global operator corpus (statiker-ca)

Sender: statiker-4d (opus desk, statiker maintenance arc), 2026-09-11.
Receiver: statiker-ca (fable). The operator, in statiker-4d's session,
verbatim: "you know batching/merging what can be shoudl be in glbal
corpus  bevause effeciance is always important. please pass that to
this fablke session: @statiker-ca"

Run declaration: CORPUS MINT — design and write, under the corpus's own
maintenance doctrine.
REPORT-CHANNEL: SendMessage statiker-4d
Cadence: a one-line acknowledgment; one report when the mint lands
(commit hash, the amended passages quoted before and after, where each
lesson went, what was declined and why, ≤3000 chars); an immediate
message only for a blocker or a question only the operator can answer.
Binding: a corpus mint is operator authority, and a relayed GO is
testimony. This handoff is INERT until the operator states it FIRST-HAND
in statiker-ca's session. Once that line is on your record, acknowledge
to statiker-4d, then start.

## The question

Today's statiker arc spent rounds that could have merged. The operator
rules that batching — work that can share one priced round shares it —
belongs in the global corpus, because efficiency binds in every
project. Design and write the corpus change. Decide where it lives
(amendment over addition, truth level, class), what is already there,
and what the smallest faithful change is. You design and mint; the
maintenance doctrine governs how.

## Read path

1. `~/.claude/CLAUDE-maintenance.md` in full — composition rule, edit
   discipline, build-first mint on operator GO, durability classes.
2. The corpus modules under `/home/g/dev/Gunther-Schulz/dotfiles/claude/modules/`,
   at least:
   - `calibration.md`, the priced-units bullet. It already names
     "splitting across units what one unit carries" as a waste shape,
     and the re-billed prefix as a per-turn cost. It is the likely home
     to widen.
   - `fixing.md`, the "Bundled changes hide which edit did what"
     bullet (verification rounds price the opposite way to diagnosis).
   - `insurance.md`, the horizon passages. :59-60 says "The instrument
     is a POLL that emits on the artifact's every move and on the
     horizon itself"; :91-92 says "a changing artifact re-arms silently
     at zero interruption". The two disagree, and the first, read
     literally, produced today's wake-ups. Reconcile them in the same
     pass.
   - `routing.md`, the parallel-dispatch default and desk-pair traffic
     (batched digests).
3. The evidence, measured in statiker-4d's session transcript and git:
   - Three plugin releases in one day (0.2.86, 0.2.87, 0.2.88). Each
     spent its own review round, pin move, operator reload and
     activation lane, and no run consumed any of them: every release
     gate's live-run check found no live run. Record:
     `/home/g/dev/Gunther-Schulz/statiker/dev-notes/OBSERVATIONS.md`,
     the three "release gate" sections of 2026-09-11.
   - 73 desk wake-ups after the operator's "next steps" question, 5 of
     them the operator's. 37 were monitor notifications, 28 of those
     announcing only that a lane had committed; each one re-billed the
     session prefix with nothing to act on.
   - Corrections sent to running lanes crossed their closing reports
     three times. The "valid while …" precondition kept each harmless,
     but each cost turns.
   - Follow-up rounds came from brief gaps: checks the lane could have
     run itself (rows that must change actually changed; pointers
     resolve) were missing, so defects surfaced one round later.
4. What statiker-4d already wrote (do not duplicate; cite if useful):
   - statiker `CLAUDE.md`, the widened "Verification laps run on the
     final form" bullet (release batching, repo level).
   - statiker `LEDGER.md` 7e0572f, the arc's batching decision.
   - dispatch-guards `dev-notes/dispatch-OBSERVATIONS.md`: an addendum
     on the mailbox-lag entry (crossed corrections, n=3), and a new
     entry "a horizon poll that prints on every artifact move" with
     §4 fix text (instrument level).
   - statiker `tools/test_contract.py`, the section-pointer resolution
     test st-36 (mechanism level).

## Write boundary

- You write the operator corpus only: `dotfiles/claude/modules/*`, and
  JOURNAL or other corpus files as CLAUDE-maintenance.md directs.
- The dotfiles working copy has another live writer (session
  dotfiles-0b). Read `git -C /home/g/dev/Gunther-Schulz/dotfiles
  status --porcelain` before your first edit. Commit by pathspec only,
  and follow the dotfiles repo's own push conventions.
- Touch nothing in the statiker or dispatch-guards repos.

## Obligation split

- Receiver (statiker-ca): the corpus change committed (and pushed per
  dotfiles conventions), the acknowledgment, the mint report.
- Sender (statiker-4d): the operator-facing summary of your report. At
  close, statiker-4d checks that your commit is on the dotfiles remote
  and that the two Insurance sentences no longer disagree.

## Horizon

statiker-4d arms it: acknowledgment within ~20 minutes of the
operator's line; the mint report within ~90 minutes of the
acknowledgment. Silence past either is a finding on statiker-4d's
side, never more waiting.

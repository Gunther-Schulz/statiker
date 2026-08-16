# statiker — repo guidance

- **Single-home by design.** `plugin/skills/statiker/SKILL.md` is the
  only home of the operational text — no spec layer, no render chain
  (a recorded design decision and a live experiment for the
  framework-legitimacy question; PLAN.md, Single-home by design).
  Edits target it directly, under skill-craft discipline (invoke the
  skill-craft skill before editing).
- **Birth-class discipline.** The payload is enforcement structure +
  bindings only; every future addition is a fire-born patch carrying
  incident provenance, logged in `dev-notes/OBSERVATIONS.md`. No
  provenance, no patch.
- **PLAN.md is the design record** — settled decisions are not
  re-opened without new evidence.
- **`dev-notes/clippy-lineage.md` is the lineage evidence register**
  — clippy-history Stichproben and the weakness ledger, loosely
  informing (never a design-against list); load it at opus-ladder
  grading, hypothesis-patch minting, fire-rate reviews, and the
  compression pass.
- **A release during a live run means the desk session restarts.**
  A version bump never reaches a running desk: the pin resolves at
  session start, and a mid-run `/reload-plugins` fixes only future
  injections — the OLD skill text already sits loaded in the desk's
  context, owning its conduct. On release with a run in flight,
  abandon the desk and start it fresh (the tracker is the handoff by
  design); the fresh desk confirms its served version from the Skill
  injection's base-directory line before the next forcing point.
  The pin moves only at a seam — a recorded A-line or forcing-point
  boundary, never while an attacker or unit is live (commits may
  land anytime; the pin is the release).

## Trial working conventions (operator-settled, 2026-08-06)

- **Two-session layout — the relay loop IS the procedure.** The
  meta/grading session runs in THIS repo (grades comparisons,
  mints, releases); the desk runs in the target repo. The operator
  relays desk output to the meta session verbatim and carries back
  its paste-ready reply — decisions travel no other way
  (carrier-on-read-path: the desk reads its tracker and the
  operator's replies, never this repo's ledger). On each relay the
  meta session owes four things: the harvest (ledger what the
  report taught), the mint decision (evidence-complete → release at
  the seam), the STOP-CALL — pause the run when a minted rule fails
  its own falsifier (a bite in a class an existing mint governs) or
  when impl/verify surfaces what the attack rounds should have
  caught (succession-negative evidence); otherwise let it run — and
  the next relay line.
- **Mid-run tuning at seams.** Between cycles is an upgrade point,
  not a wait: grade what is evidence-complete (field-tested in-run
  with provenance = ripe; needs the run's remainder = defer), mint,
  release — the running desk finishes its round on the old version,
  the fresh desk picks up the new one at the seam. Before each
  fresh-desk start, the meta session SWEEPS the ledger's open
  bookings and grades each for lifting: ripe (provenance complete,
  fires at a seam the run crosses next) → mint now; otherwise it
  stays on its named trigger. A booking whose delivery path is a
  relay line is a lift candidate by default — the skill is the
  carrier that cannot be forgotten. (An audit arriving only on
  operator prompt is the recorded miss shape.)
- **Comparison experiments pre-register.** The decision criterion
  is recorded in dev-notes BEFORE any arm dispatches; arms are
  graded post-run in the meta session on a body-read of the raw
  reports — the desk records verbatim and never grades the arms.
- **Skill text states current decisions cleanly, as if final
  (operator-settled 2026-08-10).** A settled decision enters
  SKILL.md as the plain default — no experimental hedges, no
  history, no "outside this default" framing inline: history and
  provenance live in dev-notes and git, and rollback is cheap
  because both record everything. Anything less clean is not a
  fair test of the design. (Markers that carry epistemic load for
  the reader — an explicitly flagged unproven rule — are judged
  per instance, not swept as history.)
- **n=1 suffices during the experimental phase (operator-settled
  2026-08-10).** A single pre-registered probe whose criterion
  resolves is decision-grade for trial-phase calls — un-parks,
  mints, convention changes. Variance caveats are still RECORDED
  (they price the finding for later re-checks) but they do not
  hold a resolved criterion open, and no repeat probe is owed
  before acting on one. Boundary (operator-agreed, same date):
  the rule never applies to weakening its own safety floor — the
  irreversible-unit hold, red-first instruments, and
  pre-registration are what make n=1 decision-grade, so an n=1
  result arguing to loosen any of them is out of the rule's
  reach. Re-visit the bar when the trial phase closes.
- **Dispatch confirmation: RETIRED 2026-08-08 (operator:
  production posture — run the skill as it runs in production).**
  Desk sessions dispatch per the routing table and the run
  record's own constraints; fable dispatches keep the mechanical
  veto-gate, and an operator-imposed run hold (a C-line) is
  always the operator's. History: the trial-phase form
  (attack/impl/fable present individually and wait, discovery
  pre-authorized; itself narrowed 2026-08-06 from a blanket rule
  that priced every dispatch at one blocking round-trip) served
  while conduct was unmeasured; retired once 0.2.49/50
  mechanized the grammar and desk conduct graded clean across
  the trial's first relays.
- **Skill-edit review at opus (standing; experiment sustained
  2026-08-15).** Every SKILL.md release gets ONE fresh-context
  opus review before the pin moves — brief carries the diff, the
  full skill text, and the question, never the author's
  reasoning; every finding gets a recorded disposition before
  release. Provenance: the 2026-08-06 experiment's pre-registered
  criterion resolved 3-for-3 (grading in dev-notes OBSERVATIONS
  2026-08-15) — every release window yielded substance-changing
  findings, the third a release-blocking instrument defect caught
  before the pin moved.
- **Provenance trace before any operator-routed decision.** When a
  run surfaces a decision or tension to the operator, the meta
  session traces the contested claim to its origin through the
  record chain — backlog item → tracker requirement head → cited
  entries; the run logs carry the trace — before presenting, and
  the presentation names the origin (whose text, which session,
  what evidence it had). Settled 2026-08-07: the R5 round-trip
  resolved only when the trace showed R5's strong form was an
  earlier session's preliminary fix-shape sentence, not operator
  intent.
- **Verification laps run on the final form (operator-settled
  2026-08-07).** Attack and review rounds price per-round; a change
  already DECIDED but not yet built makes the round's object
  stale — the lap grades text slated for replacement. Batch decided
  changes to the seam and attack once. Bounds: per-change
  attribution stays with each change's own red-first checks (the
  corpus anti-bundling rule binds diagnosis, not verification), and
  an intermediate state with a real consumer (a fresh desk starting
  mid-sequence) still releases at its own seam. Provenance: the
  0.2.32→record-tool sequencing correction — the desk recommended
  attack-first, the operator's economy argument won.
- **Desk interrogation is cheap — ask when it informs the skill.**
  Diagnostic questions relayed to the running desk (which rule
  routed a conduct call — quote it or say "improvised"; what a
  check went red on) are a first-class mint source: one question
  completing a failure triage beats reconstructing the desk's
  reasoning from repo state. Contamination is a non-cost: a
  question that would taint the desk's conduct (reveal meta-layer
  framing, lead its judgment) costs at most one desk — harvest the
  answer, abandon the session, restart fresh from the tracker at
  the seam. Prefer what/which-shaped questions; post-hoc
  why-shaped answers decay into rationalization.

- **No grandfather clauses during the trial (operator-settled
  2026-08-15).** While statiker is experimental, no
  version-transition or grandfathering machinery is minted — in
  skill text, tool behavior, or record grammar. The affected
  population is at most this repo's own runs, and a live case is
  handled at the desk as a declaration or stated deviation on
  record (the pre-Budget run declared its budget at resume;
  retroactive sweep holds ride a stated deviation). Provenance:
  the budget-grandfather clause reverted same-day (f5471ac), P5's
  epoch-scoping direction dropped on this rule. Re-opens when the
  trial phase closes or an external user exists.

- **Record-migration pre-pass before a cross-version resume
  (operator-proposed 2026-08-16, meta-agreed).** A run resuming
  under a newer skill version than wrote its record gets a
  HOUSEKEEPING pre-pass first: a separately briefed segment that
  brings the tracker to the current grammar (sweep/closure clean,
  or declared exemptions) and touches NO design substance — so
  the statiker run proper spends its cycles on project-domain
  work only. Route (settled 2026-08-16): a SUBAGENT dispatched
  from the META session, run to completion BEFORE the desk
  session starts — the desk's context never carries the
  migration, the pass runs on the cheapest capable tier
  (mechanical → sonnet), and the meta session grades the result
  by the record tool's own verdicts (sweep/closure clean, or
  declared exemptions) before spawning the desk. One writer
  holds: the desk does not exist while the pass runs. Compatible with the no-grandfather rule: this is desk
  PROCEDURE (append-only repairs, declarations, stated
  deviations), never version-transition machinery in skill text
  or tools. Trial-bounded: grammar churn is the experiment's own
  cost — when the trial closes and mid-run version jumps stop,
  the pre-pass retires with them. Provenance:
  canonical-market-identity cycle 12 — ~70 findings booked, mostly
  record archaeology (F140's 750 sweep holds, 25 grammar
  violations), the measured cost of paying migration inside the
  run itself.

## Verify

```bash
python3 -m pytest tools/ -q     # the WHOLE suite: the lane
                                # batteries prove their own lanes,
                                # test_contract.py is the reach
                                # detector over them — green lanes
                                # alone verify less than they read
awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'
                                # operational (non-blank body) lines —
                                # trial metric, printed for the record;
                                # ≤ ~150 (PLAN.md size target) is the
                                # STABILIZATION EXIT criterion, not a
                                # live gate: the count accretes
                                # fire-born until the booked
                                # compression pass (dev-notes)
ls plugin/skills/                # payload inventory: statiker only
```

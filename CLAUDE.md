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
  provenance, no patch. The mint's OBSERVATIONS entry also records
  its check against PLAN.md's base-reference tenet list (the
  2026-08-05 tenet entry: changes build on it and are checked
  against it) — an unrecorded check is a skipped check (Begehung
  R2: three releases minted without one), and the check
  ENUMERATES every tenet in PLAN's list, each marked
  pass/fail/not-applicable: a tenet set recalled from memory is
  the restated-basis class, and the one skipped tenet was the
  one that would have caught three review rounds' blockers
  (release-review round 3, 2026-08-16 — the medium tenet,
  unchecked on mechanism-dense prose mints).
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

- **Disposition executability (operator-settled 2026-08-17, from
  the point-3 deadlock).** A paste-ready disposition or
  authority block the meta session composes is a BRIEF: before
  delivery, each step naming an action is checked against the
  RUN RECORD'S OWN STATE — gate predicates, budget counters,
  phase — read from the tracker on disk, not recalled from
  relays. Incident: a disposition instructed "proceed to
  implementation" while the closure gate was structurally
  unopenable (last round BIT, rounds 5/5 spent) — the
  unexecutable step cost the operator round-trip it existed to
  save, and only the desk's refusal to improvise past the gate
  surfaced it. The machinery half (the breaker's missing
  CONTINUE ending) is P19's; this convention is the
  composition half.

- **Mint timing: the bite bar is on the PROBLEM, the field test
  is on the DESIGN — and the pin makes the test free
  (operator-settled 2026-08-17).** Fire-born's "actually bites"
  clears at the incident; waiting past it is never more
  tolerance for the problem, and is legitimate for exactly one
  purpose: when the candidate fix can operate once on a live
  run before the next release seam — a desk hand-running the
  mechanism (P24's A5 seal item), an injected run-scoped
  deviation (P19's F75 stop-and-report semantics) — the mint
  waits for that datum and grades the DESIGN on it, because a
  wrongly-shaped rule reads as coverage, which is worse than no
  rule. The wait is priced by the release mechanics: the pin
  resolves at desk start and moves only at seams, so mint-now
  and mint-at-seam reach the same run at the same moment; a
  wait that would cross the seam WITHOUT a field datum buys
  nothing and the mint proceeds. Placement half, measured both
  ways this week: JUDGMENT stays prose and flexible inside
  cycles (a mechanized judgment condition misfires and trains
  the override reflex); SEAMS get rules — turn-end, round-open,
  seal, close — because momentum beat in-force prose there
  twice (run-1 round 8's unapplied never-sustain clause; P16's
  improvised turn-ends). A seam-time checklist question with
  near-zero false-fire cost is rule-shaped by default.

- **Self-containment criterion (operator-settled 2026-08-17).**
  Statiker must be runnable anywhere. Any mechanism whose
  ABSENCE silently loses value or ships unverified work —
  finding exports, verify isolation, record integrity — belongs
  in the skill itself; overlays that raise efficiency or quality
  around the loop (the operator corpus, dispatch-guards
  machinery) may stay external and degrade GRACEFULLY, meaning
  their absence is loud or merely slower, never silently lossy.
  Trial reviews and deliberations ask the portability question
  per dependency: on a bare machine without the corpus, what
  breaks — and is the break silent? Silent break → skill-owned.
  BOUNDED same day (operator mission challenge, PLAN.md
  "thin"): the criterion reaches only mechanisms of THE RUN AND
  ITS RECORD — applied unboundedly it absorbs the accretion
  module wholesale (file roles, booking discipline), turning a
  run-conduct skill into workspace management. Operative split:
  SURFACING is run-conduct and skill-owned (the close report
  enumerates, nothing ships quietly); FILING — destinations,
  carriers, repo conventions — is the environment's, however
  silently a bare environment then loses what was surfaced.
  (Provenance: run-2 F77's export rode the corpus plus a meta
  nudge; the P25 over-widening and re-scope, this date.)

- **Efficiency reviews lead with causes, never arithmetic
  (operator-settled 2026-08-17).** When grading a trial run or
  deliberating statiker changes, the first question over any
  observed excess (rounds, cycles, record volume) is WHICH
  diagnosable cause produced it — the P18/P19 finding: caps
  truncate divergence and never cause convergence, so efficiency
  work targets causes (round-sustain class, record attack
  surface, item scope), and a bound's firing is a diagnostic
  event owing a named cause. Resource arithmetic alone grades
  nothing. Sharpened same day (operator): ROUND COUNT IS AN
  OUTPUT, NOT A KNOB — better cycle work needs fewer rounds
  (sealed instruments, repairs carrying their executed checks,
  right-sized requirements), so rounds-per-landed-unit trending
  down is the trial's efficiency read, and it moves ONLY
  through cycle quality. Floor, never economized: one honest
  fresh-context round before code ships — self-blindness is the
  lineage's one never-solved class, only re-homed into the
  attack; a "saved" closing round moves defect discovery to
  prod, which here is real money.

- **Two-session layout — the relay loop IS the procedure.** The
  meta/grading session runs in THIS repo (grades comparisons,
  mints, releases); the desk runs in the target repo. The operator
  relays desk output to the meta session verbatim and carries back
  its paste-ready reply — decisions travel no other way
  (carrier-on-read-path: the desk reads its tracker and the
  operator's replies, never this repo's ledger). UPDATED
  2026-08-17 (operator): the meta session may drive the desk
  DIRECTLY over the live peer channel (SendMessage) — procedure,
  facts, and desk reports travel meta↔desk without the operator
  as carrier; operator-AUTHORITY lines (C-line stops and lifts,
  budget amendments, grants) still travel only operator→desk,
  per the grants-never-peer-channel convention (held twice
  2026-08-16, ledger 1b8df98). UPDATED 2026-08-23 (operator: "you
  fully drive it"): the meta session drives the desk END TO END
  over the peer channel — seed brief, intent, AND the operator's
  authority lines, relayed marked as the operator's words with the
  decision's date and the meta session named as relay; the
  operator states decisions in the META session and pastes nothing
  into the desk. What makes the relayed grant binding at the desk
  is the desk's own corpus construction (a standing delegation the
  operator has stated first-hand in the receiver's session) —
  MEASURED on the U2 run (2026-08-23, desk beat-the-books-3d): the
  desk refused the relayed authority block outright and stopped
  clean (no seed, no write) until ONE operator-typed delegation
  line landed in its session, naming the meta session, the scope
  (which units authorized, C2), and that its directives bind. So
  the procedure is: one first-hand delegation line per desk
  session, pasted by the operator at desk start (the meta session
  hands the paste-ready line with the kickoff); every later
  authority line travels meta→desk under it. The four per-relay obligations
  below bind per desk REPORT, however it arrives. On each relay the
  meta session owes four things: the harvest (ledger what the
  report taught), the mint decision (evidence-complete → release at
  the seam), the STOP-CALL — pause the run when a minted rule fails
  its own falsifier (a bite in a class an existing mint governs) or
  when impl/verify surfaces what the attack rounds should have
  caught (succession-negative evidence); otherwise let it run — and
  the next relay line. The harvest is also the skill's FIRE-BORN
  CHANNEL (operator-settled 2026-08-26): a tool or page defect the
  desk hits while running is booked HERE by the meta session — the
  claim verified against this repo's source at the meta desk, never
  taken on the desk's word — with the run's own finding id as
  provenance; the desk records the finding in its tracker and
  never learns this repo exists (carrier-on-read-path). Measured
  the day it was settled: five silent-form defects (P32–P36), each
  arriving with file:line and both sides read, none bookable by
  the desk itself.
- **Economics lens — where the line is (operator-settled
  2026-08-26).** Every harvest, mint decision, release, and review
  in this repo asks, beside the evidence question, the ECONOMICS
  question in two currencies: turns (desk rounds, relay round
  trips, tracker volume) and corpus lines (SKILL.md operational
  text, now 11× its target). A mint names the defect CLASS it
  catches, its cost in both currencies, and whether judgment-in-
  prose or an existing clause could carry it instead — a patch
  that only ratifies the last incident's shape is the rigidity
  the operator named (fire-born accretion until the skill prevents
  the judgment the next incident needs). The line the trial is
  drawing: the forcing point that makes the fresh-context round
  happen, the round itself, and a record sufficient for the round
  to read and a successor to resume are the VALUE; the rest is
  machinery on trial against its cost. Basis: the control arm
  (dev-notes/control-arm-hotfix-2026-08-26.md) and PLAN.md's
  2026-08-26 direction entry. The compression pass consumes this;
  so does every run digest — the meta session's harvest reports
  the run's turn cost beside its findings. ATTACK TIMING is the
  sharp edge of the lens (operator, same day): if the round is the
  value, WHEN it runs is the whole economics — too early grades an
  object a decided change will replace, too late follows the
  irreversible act, too often is the cost the operator is split
  over. The one right moment: nothing decided-but-unbuilt remains,
  and the first irreversible act has not happened. Every round
  after the first owes a stated reason at dispatch and a
  zero-delta reading at return — a second round returning zero
  delta is evidence that one round plus a desk-side repair
  suffices at that unit size, recorded as such, not as
  confirmation.

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
- **Skill-edit review at opus — CHECKPOINT-BASED
  (operator-settled 2026-08-16; supersedes the per-release form
  of 2026-08-15, which this bullet carried).** A release may move
  the pin UNREVIEWED while its unreviewed content is small
  conduct/judgment prose. A fresh-context opus review is owed
  before the pin moves when ANY of: (1) the cumulative unreviewed
  SKILL.md delta since the last reviewed state exceeds ~50
  changed lines; (2) the change touches machine-read semantics —
  new token, grammar, predicate, or tool behavior, AND read
  broadly: any clause that NAMES a record form, label, tag, or
  gate is this class, whatever register it is written in (the
  0.2.78 review's lesson, same day the split was settled: a
  "conduct prose" clause drew 2 BLOCKING findings, both in the
  record forms it implied); (3) operator call. Review form unchanged:
  brief carries the diff since the last REVIEWED state, the full
  skill text, and the question, never the author's reasoning;
  every finding gets a recorded disposition before release.
  Provenance for the split: iteration speed during the live trial
  (operator), priced by the 4-round review series' measured
  pattern — tool+battery-backed changes survived review while
  fresh prose mechanisms drew the blockers, so the mechanism
  class keeps the mandatory review and small prose rides.
  History: the per-release form's own provenance (3-for-3
  substance-yield, one release-blocking catch) stands in
  dev-notes OBSERVATIONS 2026-08-15; re-visit the split if an
  unreviewed release ships a bite the review class would have
  caught.
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

- **No grandfather clauses during the trial — NARROWED 2026-08-17
  (operator re-opened; supersedes the blanket form of
  2026-08-15).** What stays out during the trial: run-state
  migration and version-transition machinery (converting old
  records, dual-grammar readers). What is IN-bounds since
  2026-08-17: mechanical retroactivity grading — the sweep
  scoping FORM rules by the P3 `SKILL:` version markers so a rule
  never grades lines that predate its mint (re-opened P5,
  BACKLOG). Basis for the narrowing: the blanket rule's recorded
  premise — "firing population empty" — was refuted the next day
  when run 1's ready gate was barred by 696 retroactive holds and
  the run closed FAILED (P18 measurement); the operator states
  the terminal-unrepairability consequence was never the rule's
  intent. A live case in a marker-less record is still handled as
  a declaration or stated deviation on record; judgment-shaped
  exemptions keep the SWEEP_EXEMPT route. History: the
  budget-grandfather clause reverted same-day (f5471ac), P5
  dropped under the blanket rule (both 2026-08-15).

- **Record gate at resume — SUPERSEDED into SKILL.md
  (operator-settled 2026-08-16; born same-day as a meta-session
  pre-pass convention, absorbed before ever firing).** The skill
  now carries it (0.2.69, the resume passage): a resume opens
  with `sweep`/`closure` before any design work, blocking holds
  repaired through a dispatched mechanical leg on the cheapest
  certified tier, the desk grading by re-running the verdicts
  itself. Deliberately VERSION-NEUTRAL — it fires on holds
  whatever their cause (version jump, desk error, operator
  edits), so it is a standing hygiene gate, not
  version-transition machinery: the no-grandfather rule stands
  unamended. Provenance: canonical-market-identity cycle 12 —
  ~70 findings, mostly record archaeology (F140's 750 sweep
  holds), the measured cost of paying repair inside the run.

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

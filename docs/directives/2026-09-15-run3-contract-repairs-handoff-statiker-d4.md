# Run-3 contract repair arc — handoff to statiker-d4 (2026-09-15)

Driving desk: statiker-9c (meta, fable) under the operator's standing
delegation, stated first-hand by the operator in statiker-d4's own
session. This directive is INERT until that delegation line is on
statiker-d4's record; the first act is acknowledging it to statiker-9c.

Executing desk: statiker-d4 (opus — the repo's default tier for
maintenance/disposition arcs). statiker-d4 owns the statiker working
copy for this arc; statiker-9c writes nothing in it after this
directive's own commit.

## State this arc opens from (bases: LEDGER.md tail; commits 165f715, 5442b16)

- Payload 0.2.100 is CERTIFIED and BANKED; the installed pin HOLDS at
  0.2.99 (pin moves only at run seams; this arc is not a run — no
  release, no `/release-plugin`).
- The run-3 narrow round (fresh-context opus, 2026-09-14) returned
  3 BLOCKING / 8 SUBSTANTIVE / 5 MINOR — every finding on the run-3
  CONTRACT (dev-notes pre-registration + arms), zero `plugin/` files.
  Full audit with executed bases:
  `docs/audits/2026-09-14-narrow-round-run3-contract.md`.
- Operator decision, first-hand 2026-09-14 (ledger, commit 5442b16):
  the "operational issues never keep us from grading ANY models" pin
  covers ALL arms, ceiling included. §3a.4's drop-ceiling option is
  VOID and its three-arm narrowing (sol/terra/astra) is REVERSED. The
  §3a.4 edit realizing this is THIS arc's work. This closes st-77's
  drop-it escape: equalise-or-declare is the standing option set.
- Run 3 remains blocked on exactly this arc: the st-76..79 contract
  repairs.

## Wave 1 — authorized once the delegation ack is on record

1. **st-76** (READY, blocked-by NONE): commit the cold-probe prompt
   VERBATIM as §9.1's named comparand; restate §9.1 over requirement
   paragraphs rather than byte-identity. NOT a re-run — the probe's
   ask was harder than the arm's and still produced no near-miss.
   Done-criterion, evidence and write-set in the item (ITEMS.md).
2. **st-79** (READY, blocked-by NONE): a recorded disposition for each
   of S1, S2, S3, S5, S6, S7, S8 and M1–M5 per the audit — repaired
   or explicitly declined with a reason. S1 and S3 gate any freeze
   re-run resting on the driver probe; S6 (one contract both permits
   and forbids arm dispatch) is the cheapest and most dangerous.
3. **§3a.4 edit** per the operator decision above: remove the
   drop-ceiling option, reverse the three-arm narrowing. The edit's
   record quotes the decision with its date, marked as the operator's
   words relayed by statiker-9c.

st-76, st-79 and the §3a.4 edit all touch
`dev-notes/scoped-run-3-preregistration.md`: serialize those edits at
this desk (or run them as one lap). Lane routing otherwise by your
standing defaults (brief-covered execution → sonnet).

## st-77 and st-78 — decision blockers: PROPOSE, do not execute

Both carry decision-shaped blockers; the decisions sit with the
driving desk under the delegation. Wave-1 deliverable for each is a
DISPOSITION PROPOSAL with executed bases, sent to statiker-9c:

- **st-77** (B2+S4): equalise the two ceiling-arm asymmetries (driven
  series vs one-shot; the 9-file operator-corpus load) OR declare both
  as deviations with the §6c certification consequence named. Read
  audit B2+S4 and pre-registration §3a.4/§3a.5/§6c/§15c. The proposal
  states each option's cost and exactly which columns run 3 can then
  certify.
- **st-78** (B3): the record tool gains a runtime authorized-path
  check on artifact `--out`, OR containment stays preflight-only with
  terra's inclusion re-reasoned. Read audit B3, statiker_git.py's
  containment gate (~1274–1366) and statiker_record.py's
  ARTIFACT_IN_REPO (~2752–2761). Note in the proposal: a runtime check
  in the record tool is PAYLOAD work touching banked 0.2.100 and a
  C4b mint question (new predicate) — name that consequence explicitly.

When a decision returns from statiker-9c, record it via
`lifecycle ledger add decision --question <the item's blocked-by text
VERBATIM>` — question-slot equality, never a hand-written ledger line
(CLAUDE.md, carrier transition; incident 89fd565) — then execute.

## Conduct

- Bookings, closures, decisions through lifecycle verbs, never hand
  edits. Items close by commit ref.
- st-79's tool repairs are red-first per repo discipline. Any repair
  introducing a new machine token, hold code, predicate or mandatory
  form is a C4b MINT — provenance + full tenet check in
  `dev-notes/OBSERVATIONS.md` before it lands (fired positive:
  d946b1a).
- Verify: `python3 -m pytest tools/ -q` — the whole suite; report the
  counts from the run's own output.
- `plugin/skills/statiker/SKILL.md` is OUT of this arc's write-set. A
  repair that seems to need a skill edit is a finding back to
  statiker-9c, never an edit.
- Report channel: SendMessage to `statiker-9c` (machine-readable name;
  this line is the channel declaration). Batched digests for routine
  completions; immediate messages for blockers, decision proposals,
  milestones. The driving desk holds a ~30 min horizon: silence past
  it over a static artifact is treated as a stall.
- Commits push same-turn, with AI attribution per your session's
  rules.

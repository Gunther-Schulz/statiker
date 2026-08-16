Title: sonnet: Lane E — sweep exemption grammar (P6), lock-gate
predicate repair (E-O), GATE_UNREADABLE red-drive (E-P)

Working copy: /home/g/dev/Gunther-Schulz/statiker (main checkout,
SHARED with the dispatcher — pathspec commits mandatory, see tail).
Base commit: 3c02ca551d017ea643038815c09ed699bddac8cd. First act:
`git merge-base --is-ancestor 3c02ca5 HEAD` AND `git log --oneline
3c02ca5..HEAD` — base contained + nothing on top = clean start;
base not contained = halt; base contained WITH commits on top =
halt and report the commits as a gap.
Scratch: your OWN scratchpad, never the dispatcher's or the repo.

## Grounding basis — read before building; the report cites what
## was actually read
- the executor skill (dispatch-guards:executor) — load FIRST
- BACKLOG.md — the three entries headed `READY 2026-08-15 — P6`,
  `READY 2026-08-15 — E-O`, `READY (small) 2026-08-15 — E-P`:
  the settled designs, binding. Implement exactly these.
- plugin/skills/statiker/scripts/statiker_record.py — the sweep
  implementation: hold construction, the blocking calculus, the
  verdict emission (what P6 extends).
- plugin/skills/statiker/scripts/statiker_git.py — lock_gate_check
  (~line 820): what E-O repairs.
- plugin/skills/statiker/SKILL.md — two sections only: "Stop rule"
  (the SWEEP_HOLDS sentence: where P6's grammar sentence lands, in
  the SAME commit as the parser) and "The attack"/lock passage (c)
  (the `LOCK_GATE_HOLDS — blocking sweep holds in the record gate`
  sentence: E-O amends it in the same commit IF its wording binds
  the old predicate — read it and decide; report which way).
- tools/test_statiker_record.py, tools/test_statiker_git.py,
  tools/test_contract.py — the batteries the red-first pairs land
  in; UNDRIVEN_REMAINDER at test_contract.py:294.

## Background (established; verify at the cited lines)
- statiker_git.py:825 currently halts on
  `gate.get("verdict") != "SWEEP_CLEAN"` unconditionally —
  dispatcher grep, this session, at the base commit.
- test_contract.py:294–303: UNDRIVEN_REMAINDER contains
  GATE_UNREADABLE with its inspection-only reason — dispatcher
  grep, this session.
- Full suite green at base: 380 passed (dispatcher-executed this
  session, `python3 -m pytest tools/ -q`).
- plugin/.claude-plugin/plugin.json is at version 0.2.71 at base
  (dispatcher-committed this session).

## The settled design — implement exactly this, do not redesign
Sequencing: three commits, one per item, in order P6 → E-O → E-P
(E-O's gate reads the blocking set NET of P6's exemptions, so P6
lands first). Each item's design is its BACKLOG entry (binding,
read it in full); the load-bearing decisions restated for
convenience — on any divergence between this restatement and the
entry, the ENTRY wins and the divergence is reported as a gap:
- P6: new label line inside ordinary entry bodies, exact forms
  `^SWEEP_EXEMPT: ([a-z-]+) lines<=(\d+)$` and
  `^SWEEP_EXEMPT: ([a-z-]+) line (\d+)$`; matching holds (same
  code, covered lines) move to a sweep-verdict field
  `exempt_holds` (each carrying its declaring line); the BLOCKING
  calculus nets them out so ready-gate reads and the lock gate
  inherit through the verdict; code-specific, ceiling frozen at
  declaration — violations above the ceiling block untouched; NO
  new verdict name, NO git-tool change; the SKILL.md grammar
  sentence lands in the SAME commit as the parser.
- E-O: lock_gate_check keys on the sweep verdict's BLOCKING set
  (net of exemptions) AND is Status-conditioned — under Status
  [READY] or in-progress a non-empty blocking set halts
  LOCK_GATE_HOLDS; under FAILED or COMPLETE (the close path) the
  gate PASSES with the holds carried in the verdict as
  information.
- E-P: red-first probe via a substitute record-tool path emitting
  garbage (no verdict line) and one emitting unparseable JSON —
  both must yield GATE_UNREADABLE; a healthy consult must not;
  drive the battery row out of UNDRIVEN_REMAINDER.
  statiker_git.py changes ONLY if the probe finds the branch
  defective (then report it as a finding, fix included in the E-P
  commit).

## Verifier (in order; real output pasted in the report)
1. P6 red-first (from the entry): beat-the-books-shaped fixture —
   declared exemption: those holds exempt, blocking set SHRINKS;
   undeclared: verdict unchanged; a violation ABOVE the declared
   ceiling blocks in BOTH arrangements. All three shown red/green
   as applicable BEFORE the fix commit is claimed done.
2. E-O red-first (from the entry): must-fire = Status [READY] +
   blocking hold → LOCK_GATE_HOLDS; must-not-fire = Status FAILED
   + PENDING-class hold at a close-time lock → gate passes. Both
   directions shown.
3. E-P: the two garbage arrangements yield GATE_UNREADABLE, the
   healthy consult does not, and the contract battery accepts the
   row as driven (UNDRIVEN_REMAINDER shrinks by exactly that row).
4. Full suite: `python3 -m pytest tools/ -q` green, count stated.

## Write boundaries
Owned: plugin/skills/statiker/scripts/statiker_record.py,
plugin/skills/statiker/scripts/statiker_git.py,
plugin/skills/statiker/SKILL.md (ONLY the two named sentences'
sites), tools/test_statiker_record.py, tools/test_statiker_git.py,
tools/test_contract.py, plugin/.claude-plugin/plugin.json (bump
only). NOT to touch: BACKLOG.md, PLAN.md, CLAUDE.md,
BEGEHUNG-MAP.md, dev-notes/, docs/ — candidate lessons go in the
report slot (e), the dispatcher books them. No new files expected;
if one becomes necessary, surface it as a gap first. Commits by
pathspec, unpushed; never amend. Deployment-coupled: no — the pin
holds at 0.2.65; release is the dispatcher's later act.

## Commit plan
Guards, with the reads that found them: (1) payload-version
pre-commit guard — observed firing three times this session on
payload-touching commits (demands a plugin.json bump; message
states bump-first clears later same-batch commits). (2) BACKLOG
READY-envelope guard — fires only on staged BACKLOG.md, outside
your write set, unreachable. Plan: commit 1 (P6) carries the bump
0.2.71 → 0.2.72 in the same commit (same-commit bump proven three
times this session); bump committed, UNPUSHED. Pre-authorized
repair class: if the guard still fires on commit 2 or 3, include a
further bump (0.2.73, 0.2.74) in the halting commit and report the
permutation as a deviation — novel guard collisions halt and
report instead. Commit titles: `P6: sweep exemption grammar
(SWEEP_EXEMPT) netted from the blocking calculus`, `E-O: lock gate
keys on the blocking set, Status-conditioned`, `E-P:
GATE_UNREADABLE driven red`; trailer per tail.

Closing report (mandatory; the project's own report form if it
defines one, else the §2 form here — never both; "none" is a
valid slot answer, silence is not): (a) items completed w/
evidence, (b) checks RUN w/ real output, (c) gaps surfaced —
incl. anything needing a tier above yours, returned as a question
with its evidence, never settled at your tier,
(d) deviations w/ reason, (e) candidate lessons, (f) files
touched + commit hashes (unpushed), (g) what was NOT verified,
(h) sources actually read, of those the brief named.
Message ≤3000 chars each: a report longer than one message is
SPLIT into labeled parts (1/N) — do NOT write a report FILE
(harness-blocked for subagents); supporting data goes to the
brief's assigned DATA files, the message carries key findings
+ any such paths. A missing decision, file,
or value is surfaced as a gap, never bridged with a guess.
A check that got backgrounded is AWAITED before the closing
report (TaskOutput block=true on its task id) — ending your
turn orphans it; a report sent with a check still running is
an INTERIM report, says so, and names what remains.
Commits unpushed, by pathspec — `git commit -- <paths>`, never
`git add` then `git commit` and never `-A`: the index is shared,
so a co-writer staging between your `git status` and your commit
rides out under your message whatever you added. A NEW file is
invisible to a pathspec commit until `git add -N <path>`
registers it (intent-to-add: zero content staged, full body
still committed). Trailer:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.
Never amend — always a new commit: the amend-gate denies
subagent amends regardless of ownership (source: §1 amend
rule).
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended (source: §4
ownership rule).

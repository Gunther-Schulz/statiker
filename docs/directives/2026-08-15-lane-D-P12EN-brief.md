# Lane D brief — sonnet: P1 (seal-path + queue grammar) + P2 (gate-bound transactions) + E-N (out-of-body corrects token)

Title: sonnet: P1 + P2 + E-N (seal-path subcommand, record-gate binding at lock/unit seams, corrects-token-out-of-body lint)
Working copy: /home/g/dev/Gunther-Schulz/statiker (SHARED with the
dispatcher — disjoint file sets; pathspec commits only). Scratch:
your OWN scratchpad.

Base check (first act): base commit is **db7adfd**. Run BOTH:
`git merge-base --is-ancestor db7adfd HEAD` and
`git log --oneline db7adfd..HEAD`. Base contained + nothing on top
= clean start. Foreign commits on top are POSSIBLE (shared copy —
the dispatcher books harvests in BACKLOG.md/dev-notes/): run
`git diff --quiet db7adfd HEAD -- plugin/skills/statiker/scripts/ plugin/skills/statiker/SKILL.md tools/`;
unchanged write surface → proceed, note the commits in the report;
ANY commit touching those paths → HALT and report. Base not
contained: HALT and report.

## Grounding basis — read before building; the report cites what was actually read
- The executor skill (`dispatch-guards:executor`) — load FIRST.
- BACKLOG.md `## Open`: entries **P1**, **P2**, **E-N** —
  authoritative bodies incl. their settled designs and Done
  criteria; this brief adds the pre-named SKILL.md edits and
  assignments. File wins on divergence; report divergence as a gap.
- The T9 red-first pairs: begehung repo (read-only),
  `~/dev/Gunther-Schulz/begehung/dev-notes/eval-begehung/2026-08-11/tier2-with.md`
  (B8, B9 sections) and `tier2-without.md` (F3, F12 sections) —
  the incident arrangements your red probes reproduce.
- `plugin/skills/statiker/scripts/statiker_git.py` — cmd_lock_check
  :690, cmd_lock_commit :700, cmd_unit_start :768, cmd_unit_commit
  :794, the argparse block ~:929-956, say()/finish() emit
  machinery, and the sibling-import precedent (`import
  statiker_emit` :75-80).
- `plugin/skills/statiker/scripts/statiker_record.py` — closure
  machinery (closure --unit path), WRITE_SET_EXACT_RE :202 and the
  write-set line parsing, the verdict emit path, REPAIR_FORMS
  block ~:288-353 (E-M just landed there — read before adding
  E-N's class).
- `plugin/skills/statiker/SKILL.md` — :533-565 (lock verdict
  routes), :595-634 (artifact/queue namespace), :680-693 (seal
  passage), :955-1014 (unit invocation + verdict routes). The six
  pre-named edits below sit in these regions.
- `tools/test_statiker_git.py`, `tools/test_statiker_record.py`,
  `tools/test_contract.py` — idioms; the contract battery's parity
  check is set-exact BOTH ways over emitted verdict names vs
  SKILL.md-named ones.

## Background (established; verify at the cited lines)
- All statiker_git.py/statiker_record.py line references OPENED by
  the dispatcher today at base db7adfd.
- Suite baseline at db7adfd: 372 passed (dispatcher's run, today).
- The 0.2.67 bump is COMMITTED, UNPUSHED (exemption armed; origin
  manifest at 0.2.66) — payload commits ride it. Do not push.
- unit-start currently takes a free `--write-set` and has NO
  --tracker; lock-check/lock-commit already take --tracker but
  never consult the record gate (opened today; T9's root).

## The settled design — implement exactly this, do not redesign
The three BACKLOG bodies carry the designs (P1's three pieces,
P2's five numbered decisions, E-N's lint class). Assignments and
completions this brief adds:

### P2 mechanics (assignments)
- Gate consult helper lives in statiker_git.py: run
  `[sys.executable, <own-dir>/statiker_record.py, ...]` as a
  subprocess, parse ONLY the single final line matching
  `^STATIKER-RECORD VERDICT: ` as JSON; embed that verdict object
  verbatim as the git verdict's `gate` field. Subprocess failure,
  missing verdict line, or unparseable JSON → halt GATE_UNREADABLE
  (fail-closed), carrying whatever raw output exists.
- lock-check + lock-commit: consult `sweep --tracker <path>`
  BEFORE their current work; any BLOCKING hold in the gate verdict
  → halt LOCK_GATE_HOLDS.
- unit-start/unit-commit: REQUIRED `--tracker` and `--unit U<k>`;
  free `--write-set` args are REMOVED. Write-set = the
  `declared_write_set` field that `closure --unit` gains in
  statiker_record.py (the unit's live write-set record lines, the
  same read `waves` uses — reuse, don't reimplement). Blocking gate
  verdicts (UNIT_HELD, UNIT_UNKNOWN, CLOSURE_VOID class — decide
  membership from the closure verdict's own blocking semantics,
  report the chosen set) → halt UNIT_GATE_BLOCKED. Tracker path ∈
  declared write-set → halt WRITE_SET_NAMES_TRACKER (checked at
  both unit seams). Empty declared write-set → UNIT_GATE_BLOCKED
  with the gate verdict showing why (an undeclared unit cannot
  start).
- UNIT_START_CLEAN gains field `start_sha` (HEAD at the clean
  check). unit-commit REQUIRES `--start-sha`; halt
  UNIT_START_MISMATCH when start-sha is not an ancestor of (or
  equal to) HEAD, or when `git log start_sha..HEAD -- <declared
  write-set>` is non-empty (a foreign commit touched the write-set
  mid-unit).
- Existing unit-seam fixtures: every fixture built on `--write-set`
  is MIGRATED to a tracker-backed arrangement (a minimal tracker
  fixture with the unit's write-set record lines) — the
  predicate-gain rule: re-ask of each fixture which value it now
  exercises; a fixture that stops testing is a defect, not a pass.

### P1 mechanics (assignments)
- `seal-path --tracker <path> --round A<n>` in statiker_git.py →
  verdict SEAL_PATH with fields: `seal`, `queue`, `paths`,
  `artifact`, `report`, `comparison` — each the full absolute path
  per the SKILL.md-pinned derivation (:622-631: basename + hyphen
  + first 8 hex of sha256 of the MAIN checkout's real toplevel;
  derive via --git-common-dir when invoked from a linked
  worktree). Round arg validated `^A\d+$`.
- Queue-spent grammar is desk conduct + SKILL.md text (Edit D) —
  no tool enforcement this version (the tool never reads queues).

### E-N mechanics (assignments)
- Lint class name: `corrects-token-out-of-body`. Fires when
  CORRECTS_RE matches inside an entry's BASIS clause (or any
  non-body region of an entry line the resolver does not search).
  Repair form (REPAIR_FORMS): names the split from the BACKLOG
  entry (token sheds under the same id in the BODY; a fresh id
  re-declares any path). NOT closure-blocking. Must satisfy E-M's
  reachability assertion (it is a LINT-stage code carrying no
  corrects token in its own repair string — confirm against the
  assertion, it runs in the suite).

### The six pre-named SKILL.md edits
Verify each old-string against the file before editing; drift →
HALT and report. Each edit lands in the SAME commit as its
emitting code.

Edit A (P2 commit) — at :965-966, replace:
```
The unit runs: START, before any edit —
`unit-start --write-set <file> …`. UNIT_START_CLEAN makes
```
with:
```
The unit runs: START, before any edit —
`unit-start --tracker <tracker> --unit U<k>` — the write-set is
read from the record's declared lines through the gate consult
(the record tool run as a subprocess, its verdict embedded
verbatim as the `gate` field), so briefs never restate it;
UNIT_GATE_BLOCKED (a blocking record-gate verdict, the empty
declaration included) and WRITE_SET_NAMES_TRACKER (the declared
write-set names the tracker itself) halt the unit UNBUILT, and
GATE_UNREADABLE (no parseable record verdict) halts the same
way, fail-closed. UNIT_START_CLEAN makes
```

Edit B (P2 commit) — at :974, replace:
```
COMMIT — `unit-commit --write-set <file> … -m <msg>`.
```
with:
```
COMMIT — `unit-commit --tracker <tracker> --unit U<k>
--start-sha <the START verdict's start_sha> -m <msg>` — same
gate consult and halts as START, plus UNIT_START_MISMATCH: the
start sha is no ancestor of HEAD, or a foreign commit touched
the declared write-set since it.
```

Edit C (P2 commit) — at :533-534, replace:
```
(c) `lock-check --tracker <path> [--lock-set <path> …]`.
Verdict routes: HALT_STATE is the operator's half-finished
```
with:
```
(c) `lock-check --tracker <path> [--lock-set <path> …]`.
Verdict routes: LOCK_GATE_HOLDS — blocking sweep holds in the
record gate, the consulted record verdict embedded verbatim as
the `gate` field — halts lock-check and lock-commit uncommitted:
the record never locks over its own blocking state.
HALT_STATE is the operator's half-finished
```

Edit D (P1 commit) — at :633-634, replace:
```
existing whether or not a seal was
written — and append at the round's return, before its A-line.
```
with:
```
existing whether or not a seal was
written — and append at the round's return, before its A-line,
then SPEND the queue: append `LANDED <yyyy-mm-dd> — at line <n>`
(the tracker line the landing opened) as its last line; a queue
whose last non-blank line matches that form is spent, and
re-landing a spent queue is the double-landing halt.
```

Edit E (P1 commit) — at :682-685, replace:
```
(repo-key as the queue path derives it, then the tracker's
filename verbatim, `.md`
included) — a path any successor desk re-derives from the repo
it resumes in plus the tracker's filename; out of
```
with:
```
(repo-key as the queue path derives it, then the tracker's
filename verbatim, `.md`
included) — a path any successor desk re-derives through the git
tool's `seal-path --tracker <path> --round A<n>` verdict
(SEAL_PATH: every species' full path — seal, queue, paths,
artifact, report, comparison — from the pinned derivation; paste,
never hand-compose); out of
```

Edit F (P1 commit) — at :596-598, replace:
```
<artifact path>` serves the sha, never the working tree (a live
tree serves HEAD) — the artifact path sits OUTSIDE every repo,
like the seals and for the seal rule's reason (an in-repo
```
with:
```
<artifact path>` serves the sha, never the working tree (a live
tree serves HEAD) — the artifact path is the namespace's
`.A<n>.artifact` species (seal-path prints it), OUTSIDE every
repo like the seals and for the seal rule's reason (an in-repo
```

## Verifier (in order; real output pasted in the report)
1. P2 red-first, from the arm files' arrangements, stash-proof:
   (B8) lock over blocking sweep holds — commits under old code,
   LOCK_GATE_HOLDS under new; (B9) unit-commit over a
   closure-blocking unit state — commits under old, UNIT_GATE_BLOCKED
   under new; (F3) unit-commit without/with mismatched start —
   commits an unrelated pre-existing change under old,
   UNIT_START_MISMATCH under new; (F12) write-set naming the
   tracker — accepted under old, WRITE_SET_NAMES_TRACKER under
   new. Plus GATE_UNREADABLE (record tool path broken) red-first.
2. P1 red-first: seal-path paths equal the pinned derivation on a
   real repo fixture AND from a linked worktree (derive-in-main);
   queue-spent grammar pair (spent tail recognized / absent not).
3. E-N red-first: token-in-basis fixture silent under old (zero
   violations), fires the new class under new; body-token fixtures
   stay clean; E-M reachability assertion still green.
4. Parity: contract battery green — six new verdict names
   (LOCK_GATE_HOLDS, UNIT_GATE_BLOCKED, UNIT_START_MISMATCH,
   WRITE_SET_NAMES_TRACKER, GATE_UNREADABLE, SEAL_PATH) emitted
   AND SKILL.md-named, set-exact both ways.
5. SKILL.md diff check per commit: exactly the pre-named edits.
6. Full suite green at EVERY commit (baseline 372 + new tests).

## Write boundaries
- Yours: `plugin/skills/statiker/scripts/statiker_git.py`,
  `plugin/skills/statiker/scripts/statiker_record.py`,
  `plugin/skills/statiker/SKILL.md` (ONLY the six pre-named
  edits), `tools/test_statiker_git.py`,
  `tools/test_statiker_record.py`, `tools/test_contract.py`.
- NOT yours: statiker_emit.py, BACKLOG.md, dev-notes/, docs/,
  plugin.json. begehung repo is READ-ONLY.
- THREE commits by pathspec, one per entry, order your choice
  (state it in the report): P1, P2, E-N. Shared-file
  revert/reapply sequencing as in today's earlier lanes; full
  suite green at each commit. Never `-A`, never amend.
- Deployment-coupled: yes (payload); bump armed, do not push.

## Commit plan
- Guard: global pre-commit dispatcher (read: `git config
  core.hooksPath` → ~/dev/Gunther-Schulz/dotfiles/git/hooks; basis
  = ORIGIN manifest, hook :122-172). Exemption armed by the
  unpushed 0.2.67 bump. Repo-local chained hooks: none (read:
  `ls .git/hooks` → samples only). Blocked commit despite the
  armed exemption → HALT and report.
- Commit trailer, exact:
  `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`

Closing report (mandatory; the §2 form): (a) items completed w/
evidence, (b) checks RUN w/ real output, (c) gaps surfaced — incl.
anything needing a tier above yours, returned as a question with
its evidence, never settled at your tier, (d) deviations w/
reason, (e) candidate lessons, (f) files touched + commit hashes
(unpushed), (g) what was NOT verified, (h) sources actually read,
of those the brief named.
Message ≤3000 chars each: a report longer than one message is
SPLIT into labeled parts (1/N) — do NOT write a report FILE
(harness-blocked for subagents); supporting data goes to assigned
DATA files if any. A missing decision, file, or value is surfaced
as a gap, never bridged with a guess. A check that got
backgrounded is AWAITED before the closing report (TaskOutput
block=true) — a report sent with a check still running is an
INTERIM report, says so, and names what remains.
Commits unpushed, by pathspec — `git commit -- <paths>`, never
`git add` then `git commit` and never `-A`. A NEW file needs
`git add -N <path>` first (none expected this lane). Trailer:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.
Never amend — always a new commit: the amend-gate denies subagent
amends regardless of ownership.
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended.

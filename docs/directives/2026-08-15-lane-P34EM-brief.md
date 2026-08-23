# Lane P3/P4/E-M brief — sonnet: version line class, irreversible tag line, repair-form reachability

Title: sonnet: P3 + P4 + E-M (SKILL_VERSION line + irreversible unit line + sweep repair-form gating)
Working copy: /home/g/dev/Gunther-Schulz/statiker (SHARED with the
dispatcher — disjoint file sets; pathspec commits only). Scratch:
your OWN scratchpad.

Base check (first act): base commit is **a5222d7**. Run BOTH:
`git merge-base --is-ancestor a5222d7 HEAD` and
`git log --oneline a5222d7..HEAD`. Base contained + nothing on top =
clean start. Foreign commits on top are POSSIBLE (shared copy): run
`git diff --quiet a5222d7 HEAD -- plugin/skills/statiker/scripts/statiker_record.py plugin/skills/statiker/SKILL.md tools/test_statiker_record.py tools/test_contract.py`;
unchanged write set → proceed, note the commits in your report; ANY
commit touching your paths → HALT and report. Base not contained:
HALT and report.

## Grounding basis — read before building; the report cites what was actually read
- The executor skill (`dispatch-guards:executor`) — load FIRST.
- BACKLOG.md `## Open`: entry **E-M** (authoritative for E-M; the
  file wins over this brief's summary on divergence).
- dev-notes/OBSERVATIONS.md, the entry beginning "0.2.65 sweep
  prescribes a repair its own token resolver refuses" (commit
  271a6bf) — E-M's incident and mechanism, including the
  pre-formulated fix this brief adopts.
- `plugin/skills/statiker/scripts/statiker_record.py` — the grammar
  constants block (~:100-220: ENTRY_RE, INTENT_EXACT_RE :171,
  HOLD_EXACT_RE :191, UNIT_SCOPE_RE :180, WRITE_SET_EXACT_RE :202),
  the header-line reads (Status/Skill/Mode/Budget region ~:530-560),
  `apply_supersession` and the REPAIR_FORMS / repair-string
  attachment machinery (find via `grep -n "REPAIR_FORMS\|annotate_repairs\|apply_supersession"`).
- `plugin/skills/statiker/SKILL.md` :132-160 (the record/resume
  passage — P3's insertion site) and :459-478 (the [READY]
  unit-enumeration passage — P4's insertion site).
- `tools/test_statiker_record.py`, `tools/test_contract.py` —
  existing idioms (RecordFixture, tool()/verdict(), derived-set
  patterns like RECORD_SUBCOMMANDS).

## Background (established; verify at the cited lines)
- Grammar constants and line numbers above OPENED by the dispatcher
  today at base a5222d7.
- E-M mechanism (from 271a6bf, desk-measured on a real tracker,
  verified plausible at this desk from the booking): the sweep's
  verdict prints a `corrects line <n>` repair form for
  `clause-unparsed`, but `apply_supersession` builds its violated
  map at the LINT stage while `clause-unparsed` is SWEEP-stage —
  the printed token can never resolve; following it appended
  permanent `corrects-nothing` holds on a live tracker.
- Suite baseline at a5222d7: 358 passed (dispatcher's own run,
  today).
- The 0.2.67 version bump is COMMITTED, UNPUSHED (exemption armed,
  origin manifest at 0.2.66) — your payload commits ride it.

## The settled design — implement exactly this, do not redesign

### P3 — the mid-run version line (record grammar + tool field)
- New exact line class, `INTENT: `'s sibling label:
  `SKILL_VERSION_EXACT_RE = re.compile(r"^SKILL: statiker (\S+)$")`.
  Written by a resuming desk inside the version-crossing APPEND
  entry (the skill text mandates the entry; this line is its
  machine-readable core).
- Tool: sweep AND closure verdicts gain a field `skill_versions` —
  ordered list, header first:
  `[{"line": <header Skill: line no>, "version": "<header version>"}, {"line": <n>, "version": "<v>"}, ...]`
  for every body line matching the exact RE, in file order. FIELD,
  never a gate: no new lint class, no new blocking code, no verdict
  NAME minted.
- Legality is part of the deliverable: a planted `SKILL: statiker
  0.2.99` body line must add ZERO new lint/sweep violations on an
  otherwise-clean fixture (if the current grammar flags it, that is
  a FINDING to report with the violation line — HALT that item,
  don't redesign around it).

### P4 — the irreversible unit line (record grammar + tool field)
- New exact line class, the hold line's sibling
  (HOLD_EXACT_RE precedent):
  `IRREVERSIBLE_EXACT_RE = re.compile(r"^unit U(\d+) irreversible: (\S.*)$")`.
- Tool: sweep AND closure verdicts gain a field
  `irreversible_units` —
  `[{"unit": "U<k>", "line": <n>, "effect": "<text>"}, ...]` in
  file order. FIELD, never a gate; NO near-miss lint class in this
  version (the parked entry's own warning: a bare-word scan
  false-fires on "not irreversible" and shared bodies — the E-K
  lesson applies; conservatism is the decision, not an oversight).
- Same legality clause as P3: a planted line adds zero violations,
  else finding + halt that item.

### SKILL.md route sentences (pre-named; EXACT edits, nothing else in this file)
Edit 1 (P3), at :145 — replace
```
records it as a new APPEND entry: the `Skill:` line is pinned
```
with
```
records it as a new APPEND entry carrying the literal line
`SKILL: statiker <version>` — `INTENT: `'s sibling label, surfaced
with the header's version as `skill_versions` in sweep and closure
verdicts (attribution, never a gate): the `Skill:` line is pinned
```
Edit 2 (P4), at :468 — replace
```
deletion outside the write-set — is tagged irreversible in its
enumeration.
```
with
```
deletion outside the write-set — is tagged irreversible in its
enumeration, as its own record line `unit U<k> irreversible:
<effect>` (the hold line's sibling); the record tool surfaces the
set as `irreversible_units` in sweep and closure verdicts —
attribution, never a gate: unattended enforcement stays the hold
entry.
```
Each edit lands in the SAME COMMIT as its emitting tool code
(BACKLOG composition rule: route sentence + emitting code, one
commit). Verify both quoted old-strings against the file before
editing; drift → HALT and report.

### E-M — repair forms gate on resolver reachability (BACKLOG entry is authoritative)
- A hold's printed repair string gates on its code being reachable
  by `apply_supersession`'s violated map: SWEEP-stage-only codes
  print a repair form WITHOUT the `corrects line <n>` token, naming
  the hand-bookkeeping shape instead (adapt the existing string's
  intent; the point is the token never appears on a code the
  resolver cannot resolve).
- Contract-battery assertion (tools/test_contract.py): every
  REPAIR_FORMS entry containing the correcting token belongs to a
  resolver-reachable (LINT-stage) code. Derive the reachable set
  from the source the way the battery already derives
  RECORD_SUBCOMMANDS (derived, never a restated hardcoded list).
  This assertion must go RED against the current tree
  (clause-unparsed carries the token today) — that red is E-M's
  red-first proof.

## Verifier (in order; real output pasted in the report)
1. P3 red-first, stash-proof: fixture with a planted
   `SKILL: statiker 0.2.99` line — old code: no `skill_versions`
   field (KeyError/absent); new: field present with header + planted
   entries, correct line numbers. Pair: fixture WITHOUT any body
   line → field carries exactly the header entry (absence half of
   the instrument pair). Legality: planted line adds zero
   violations.
2. P4 red-first, stash-proof: same pair shape for
   `unit U3 irreversible: deletes prod rows` → `irreversible_units`
   present/correct; absence → empty list; zero new violations.
3. E-M red-first: the new contract assertion RED at the current
   tree (paste the failure naming clause-unparsed), GREEN after the
   gating lands; plus a behavior check that a sweep over a fixture
   with a SWEEP-stage hold prints a repair string WITHOUT the
   corrects token.
4. SKILL.md diff check: `git diff a5222d7 -- plugin/skills/statiker/SKILL.md`
   shows EXACTLY the two pre-named insertions, nothing else.
5. Full suite: `python3 -m pytest tools/ -q` — green (baseline 358
   + your new tests).

## Write boundaries
- Yours: `plugin/skills/statiker/scripts/statiker_record.py`,
  `plugin/skills/statiker/SKILL.md` (ONLY the two pre-named edits),
  `tools/test_statiker_record.py`, `tools/test_contract.py`.
- NOT yours: statiker_git.py, statiker_emit.py, BACKLOG.md,
  dev-notes/, plugin.json, docs/.
- THREE commits, by pathspec, in this order:
  1. P3 — statiker_record.py + SKILL.md + test_statiker_record.py
  2. P4 — statiker_record.py + SKILL.md + test_statiker_record.py
  3. E-M — statiker_record.py + test_contract.py (+
     test_statiker_record.py if the behavior check lives there)
  The shared-file sequencing pattern from today's E-J/E-L lane
  applies: stage each commit's state by temporarily reverting the
  other items' hunks (plain edit-revert/reapply, verified by git
  diff at each step), full suite green at each commit.
  Never `-A`, never amend.
- Deployment-coupled: yes (payload) — bump 0.2.67 already
  committed, unpushed; do not push.

## Commit plan
- Guard: global pre-commit dispatcher (read: `git config
  core.hooksPath` → ~/dev/Gunther-Schulz/dotfiles/git/hooks; basis
  = ORIGIN manifest, hook :122-172). Exemption armed by the
  unpushed 0.2.67 bump. Repo-local chained hooks: none
  (read: `ls .git/hooks` → samples only).
- Blocked payload commit despite the armed exemption → HALT and
  report (no repair pre-authorized).
- Commit trailer, exact:
  `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`

Closing report (mandatory; the §2 form): (a) items completed w/
evidence, (b) checks RUN w/ real output, (c) gaps surfaced — incl.
anything needing a tier above yours, returned as a question with
its evidence, never settled at your tier, (d) deviations w/ reason,
(e) candidate lessons, (f) files touched + commit hashes
(unpushed), (g) what was NOT verified, (h) sources actually read,
of those the brief named.
Message ≤3000 chars each: a report longer than one message is SPLIT
into labeled parts (1/N) — do NOT write a report FILE
(harness-blocked for subagents); supporting data goes to assigned
DATA files if any. A missing decision, file, or value is surfaced
as a gap, never bridged with a guess. A check that got backgrounded
is AWAITED before the closing report (TaskOutput block=true) — a
report sent with a check still running is an INTERIM report, says
so, and names what remains.
Commits unpushed, by pathspec — `git commit -- <paths>`, never
`git add` then `git commit` and never `-A`. A NEW file needs
`git add -N <path>` first (none expected this lane). Trailer:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.
Never amend — always a new commit: the amend-gate denies subagent
amends regardless of ownership.
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended.

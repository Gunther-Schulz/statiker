# Lane A brief — statiker mint batch (record tool + SKILL.md clauses)

Title: sonnet: build the run-2 close-seam mint batch (P15, P26, P30,
P25, P5, P20, P27, P19 tool halves + P21/P24 prose clauses)

Working copy: /home/g/dev/Gunther-Schulz/statiker (shared with the
dispatching session — pathspec commits mandatory, see tail).
Base check: `git merge-base --is-ancestor 8f9a6bfa0ae73bb114fb3de2c66e13868e4bc23a HEAD`
AND `git log --oneline 8f9a6bfa0ae73bb114fb3de2c66e13868e4bc23a..HEAD`.
Base contained + nothing on top = clean start. Base contained + commits
on top: commits touching ONLY BACKLOG.md/CLAUDE.md are the dispatcher's
relay bookings — proceed; anything else = halt and report the commits.
Base not contained = halt.
Scratch: your OWN scratchpad.

## Grounding basis — read before building; the report cites what was read
- the executor skill (dispatch-guards:executor) — load FIRST
- BACKLOG.md entries P15, P26, P30, P25, P5, P20, P27, P19, P21, P24
  (## Open section) — each carries the settled design, verifier,
  done-criterion, and write boundary; they are your spec. The
  dispatcher freezes these entry bodies for the run's duration
  (new entries may be appended below them; your entries do not move).
- plugin/skills/statiker/SKILL.md — the full current skill text
  (0.2.81); your clauses land here.
- plugin/skills/statiker/scripts/statiker_record.py — the record
  tool; every predicate change lands here.
- tools/test_statiker_record.py — the battery; every red-first
  arrangement lands here.
- PLAN.md, the 2026-08-05 base-reference tenet list — needed for the
  per-mint tenet check (see below).
- dev-notes/OBSERVATIONS.md tail (last ~3 entries) — the mint-entry
  form you must match.
- CLAUDE.md "Birth-class discipline" + "Single-home by design" —
  the mint bookkeeping rules you must satisfy.
- Before ANY SKILL.md edit: invoke the skill-craft skill
  (`skill-craft:skill-craft`) — repo gate, named in CLAUDE.md.

## Background (established; verify at the cited lines)
- Skill version is 0.2.81; the version PIN and plugin.json bump are
  the DISPATCHER's at release — you never bump, and your OBSERVATIONS
  entries label the release slot "batch release, pinned by dispatcher".
  (Opened at brief time: CLAUDE.md release rules.)
- The `SKILL: statiker <version>` line class and `skill_versions`
  field exist in the tool (shipped 58b224b; opened at brief time) —
  P5 builds on them.
- The repo verify ritual is `python3 -m pytest tools/ -q` — full
  suite, green required at every commit you make. (Opened: CLAUDE.md
  Verify section.)
- Sweep-code names cited in entries (superseded-block-form,
  basis-missing, tag-literal-in-body, clause-unparsed,
  basis-cites-invalidated, killerless-dead, pending-latest) are from
  executed verdicts of the beat-the-books run records — treat exact
  spelling as "from run record, unverified": derive the authoritative
  code list from statiker_record.py itself and report any mismatch
  as a deviation, never silently correct either side.

## The settled design — implement exactly this, do not redesign
Implement the entries IN THIS ORDER, one entry = one commit (its
tool change + its battery + its SKILL.md clause where the entry
names one + its OBSERVATIONS mint entry — same-commit authorship is
the repo's composition rule):
1. P15 (repair text names SWEEP_EXEMPT route) — small, independent.
2. P26 (trend concentration flag reads entry class).
3. P30 (verify-leg freeze: sha-pinned copy check, STALE-COPY verdict).
4. P25 (out-of-scope finding grade + closure export gate + close
   report LEAVINGS enumeration + the standalone-inheritance seed-read
   clause) — implement the RE-SCOPED form in the entry (surfacing
   mandated, destinations never prescribed).
5. P5 (epoch-scoped sweep: rule→mint-version table backfilled from
   this repo's git history of statiker_record.py; form codes
   grandfathered, substance codes retroactive per the entry's
   F148-derived split; marker-less records out of scope).
6. P20 (never-sustain round-open gate, SUSTAIN_DENIED verdict).
7. P27 (sustain/closure reads design CONSEQUENCE: a terminal round
   whose dispositions amend no design entry grades the closure
   SATISFIED; one design-amending disposition keeps it shut). P20
   and P27 interact by design — P27 completes P20; if their
   predicates conflict in implementation, surface the conflict as a
   gap, do not resolve it yourself.
8. P19 (budget passage: cap as safety escape, stop-and-report with
   the three endings FAILED/EXPORT/CONTINUE, zero-landed tripwire +
   non-contraction routing to narrowing, housekeeping outside budget,
   pre-registered cause discriminators at arming).
9. P21 + P24 (SKILL.md prose clauses: intake scope gate with the
   bidirectional entry-boundary-skeptical widening; instrument-seal
   part with slots (i)-(iv) and the axis sentence). Prose mints —
   no battery; tenet check + OBSERVATIONS entry still mandatory.
Per SKILL.md patch: an OBSERVATIONS entry with incident provenance
(cite the entry's named incidents — F-ids and run) AND the tenet
check ENUMERATING every tenet in PLAN's list, each marked
pass/fail/not-applicable (CLAUDE.md birth-class rule).
Keep SKILL.md's register: current decisions stated cleanly as
defaults — no history, no hedges inline (CLAUDE.md trial convention).

## Verifier (in order; real output pasted in the report)
1. Per entry: the entry's own red-first arrangement — new
   expectations against the pre-change tool, baseline stated, red
   output pasted, then green at the entry's commit.
2. After every commit: `python3 -m pytest tools/ -q` full suite green.
3. After the last commit: the CLAUDE.md operational-line count
   command (`awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'`)
   — print the number for the record (no gate on it).

## Write boundaries
Yours: plugin/skills/statiker/** (SKILL.md, scripts/),
tools/test_statiker_record.py, dev-notes/OBSERVATIONS.md.
NOT yours: BACKLOG.md, CLAUDE.md, PLAN.md, plugin.json, plugin/hooks/**
(a parallel lane owns plugin/hooks/** and its own new test file),
README.md. `git commit -- <paths>` only. New files: `git add -N` first.
Deployment-coupled: NO — nothing here is live until the dispatcher
releases; commit unpushed, never push.

## Commit plan
Commit-blocking guards, with the read that found them:
core.hooksPath=~/dev/Gunther-Schulz/dotfiles/git/hooks (read at brief
time); the READY-envelope pre-commit fires only on a STAGED
BACKLOG.md (observed firing twice today) — you never stage it, so it
cannot fire on your commits; a push-claim guard fires only on push,
which you never do. Version bump: dispatcher's, at release, after
your close — no bump commit in your plan. Order: as numbered above,
one commit per entry, message naming the P-number.
Pre-authorized repair class: if an entry's stated red-first
arrangement is unbuildable exactly as written (e.g. a fixture the
grammar cannot express), build the nearest arrangement that still
discriminates the entry's named defect and report the substitution
as a deviation with both forms quoted.

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

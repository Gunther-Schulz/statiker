# Lane B brief — P16 Stop-hook against improvised desk turn-ends

Title: sonnet: build P16 — statiker-plugin Stop hook with red-first
fixture battery

Working copy: /home/g/dev/Gunther-Schulz/statiker (shared — pathspec
commits mandatory, see tail).
Base check: `git merge-base --is-ancestor 8f9a6bfa0ae73bb114fb3de2c66e13868e4bc23a HEAD`
AND `git log --oneline 8f9a6bfa0ae73bb114fb3de2c66e13868e4bc23a..HEAD`.
Base contained + nothing on top = clean start. Base contained + commits
on top: commits touching only BACKLOG.md/CLAUDE.md (dispatcher relay
bookings) or plugin/skills/**, tools/test_statiker_record.py,
dev-notes/OBSERVATIONS.md (parallel lane A) — proceed; anything else =
halt and report. Base not contained = halt.
Scratch: your OWN scratchpad.

## Grounding basis — read before building; the report cites what was read
- the executor skill (dispatch-guards:executor) — load FIRST
- BACKLOG.md entry P16 ("READY 2026-08-16 — P16: Stop-hook against
  improvised desk turn-ends") — the settled design: predicate,
  firing shapes, legitimate-wait shapes, verifier, done-criterion.
  Frozen for this run's duration.
- plugin/ directory structure + plugin.json — establish where hooks
  live for this plugin (expected: plugin/hooks/hooks.json roster +
  script; if the plugin has NO hooks scaffolding yet, creating it is
  in scope — mirror the structure used by the dispatch-guards plugin
  at ~/.claude/plugins/cache/dispatch-guards-marketplace/dispatch-guards/0.10.25/hooks/
  as the reference shape, read-only).
- A real run tracker for predicate shapes (read-only):
  /home/g/dev/Gunther-Schulz/beat-the-books/.clippy/runs/2026-08-16-canonical-frame-sign-repair-statiker.md
  — header fields (Status/Mode), A-line tags, [PENDING]/[DISPATCHED]
  forms your predicate must parse.

## Background (established; verify at the cited lines)
- The hook fires ONLY in sessions whose cwd repo carries a live
  statiker tracker: `.clippy/runs/*-statiker.md` with
  `Status: in-progress` (P16 entry, opened at brief time).
- Predicate (from the entry, verbatim design): Mode unattended AND
  last A-line terminal (not [DISPATCHED] awaiting return) AND the
  blocking set is not solely an operator-authority [PENDING] → the
  stop is BLOCKED with a message naming the owed work (cycle
  re-derivation, landing, close). All legitimate waits pass:
  attended prompt, round in flight, authority-gated close.
- Stop hooks in this harness: read hook input JSON on stdin; a
  blocking response uses the documented Stop-hook decision form —
  derive the exact schema from the dispatch-guards plugin's hooks
  (reference shape above) rather than from memory; if the schema
  cannot be established from that source, surface as a gap.
- Version bump: dispatcher's, at release — you never touch
  plugin.json.

## The settled design — implement exactly this, do not redesign
- plugin/hooks/statiker_stop_guard.py — the Stop hook script,
  predicate computed from the RECORD (tracker file), never from
  conversation state; fail-open on parse errors (a malformed
  tracker never blocks a stop — it prints a warning line instead).
- plugin/hooks/hooks.json (or the plugin's established roster file
  if one exists) — registers the Stop hook.
- tools/test_statiker_stop_hook.py — the red-first fixture battery
  from P16's verifier: a tracker fixture in EACH state — the two
  incident shapes (report-delivered/turn-ended/work-owed; b7
  post-A1 and cd post-A2 shapes) where the hook must FIRE, and the
  four legitimate-wait shapes (attended prompt; round in flight
  [DISPATCHED]; operator-authority [PENDING] as sole blocker;
  Status not in-progress) where it must stay SILENT. Fixtures are
  constructed tracker files, not copies of real runs.
- The live-firing half of P16's done-criterion (one live firing or
  clean live pass logged) is the DISPATCHER's, post-release — out
  of your scope.

## Verifier (in order; real output pasted in the report)
1. Red-first: battery written first, run against a stub/absent hook
   — the two must-fire cases fail (red output pasted, baseline
   stated); then green after the hook lands.
2. `python3 -m pytest tools/test_statiker_stop_hook.py -q` green.
3. `python3 -m pytest tools/ -q` full suite green (no collateral
   breakage; note: a parallel lane is committing to
   tools/test_statiker_record.py — if the full suite is red in THAT
   file's tests only, report it as the co-writer's transient state,
   never repair it).

## Write boundaries
Yours: plugin/hooks/** (create if absent),
tools/test_statiker_stop_hook.py.
NOT yours: plugin/skills/**, tools/test_statiker_record.py,
dev-notes/OBSERVATIONS.md, BACKLOG.md, CLAUDE.md, plugin.json.
`git commit -- <paths>`; new files `git add -N` first.
Deployment-coupled: NO — unpushed; live only at dispatcher release.

## Commit plan
Guards, with the read that found them: core.hooksPath=
~/dev/Gunther-Schulz/dotfiles/git/hooks (read at brief time); the
READY-envelope pre-commit keys on staged BACKLOG.md — never staged
by you; push-claim guard keys on push — you never push. One or two
commits (hook+roster, battery), messages naming P16. No bump.
Pre-authorized repair class: if the harness Stop-hook response
schema derived from the reference plugin differs from P16's sketch,
follow the DERIVED schema and report the delta as a deviation.

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

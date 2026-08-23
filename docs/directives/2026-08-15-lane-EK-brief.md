# Lane E-K brief — sonnet: EMIT_CONDUITS false-fire gets its declared exemption

Title: sonnet: E-K (EMIT_CONDUITS declared exemption in the contract battery)
Working copy: /home/g/dev/Gunther-Schulz/statiker (SHARED with the
dispatcher and one co-lane — disjoint file sets; pathspec commits
only). Scratch: your OWN scratchpad.

Base check (first act): base commit is **de012fd**. Run BOTH:
`git merge-base --is-ancestor de012fd HEAD` and
`git log --oneline de012fd..HEAD`. Base contained + nothing on top =
clean start. Commits on top are POSSIBLE (shared copy, disjoint
lanes): run `git diff --quiet de012fd HEAD -- tools/test_contract.py`;
unchanged → proceed, note the foreign commits in the report; any
commit touching your file → HALT and report. Base not contained:
HALT and report.

## Grounding basis — read before building; the report cites what was actually read
- The executor skill (`dispatch-guards:executor`) — load FIRST.
- BACKLOG.md, section `## Open`, entry **E-K** — authoritative;
  quoted below, the file wins on divergence.
- `tools/test_contract.py` — `EMIT_CONDUITS` definition at :69
  (`{"failure_verdict", "name", "verdict"}`) and its bare-name
  membership uses at :92, :94, :134; read the whole battery section
  around them before editing.

## Background (established; verify at the cited lines)
- Definition and use sites OPENED by the dispatcher today at the
  lines above (base de012fd).
- The false-fire: an ordinary local named `name` in
  `branch_state()` (statiker_git.py) tripped the bare-name match;
  the earlier lane's cure was renaming the local — a workaround,
  not a repair. From the lane G report / backlog entry, unverified
  at this desk; verify against the battery code and git history if
  needed.
- Suite baseline at de012fd: 352 passed (dispatcher's own run,
  today).

## The settled design — implement exactly this, do not redesign

Backlog entry, quoted:
> READY (small) 2026-08-15 — E-K: EMIT_CONDUITS false-fire gets
> its declared exemption. [...] Per the corpus guard rule, a check
> firing on legitimate work gets a declared, checked exemption —
> never a softened predicate or an avoidance habit. Design, decided
> (minimum): a comment at the EMIT_CONDUITS definition naming the
> false-fire class and the rename cure; better if cheap at build
> time: restrict the match to assignments that reach a
> finish()/say() call. Verifier: the battery stays green on the
> current tree and still fails on a real conduit rename (existing
> red case re-run). Done: comment (or scoped match) landed, battery
> green both directions. Write boundary: tools/test_contract.py.

Decisions (dispatcher's, final):
- Land the MINIMUM (the comment: false-fire class named — bare-name
  AST match is scope-unaware, an unrelated local sharing a conduit
  name trips it; the observed cure was a rename) in every case.
- Attempt the scoped match ONLY if it fits the battery's EXISTING
  AST walk without new traversal machinery (roughly: restrict the
  :134-class assignment check to assignments whose value or target
  feeds a `finish()`/`say()` call already visible to the walk). If
  it needs new machinery, do NOT build it — land the comment alone
  and report the scoped match as a gap with your evidence.
- The predicate is never SOFTENED: no name removed from
  EMIT_CONDUITS, no site check deleted.

## Verifier (in order; real output pasted in the report)
1. Battery green on the current tree:
   `python3 -m pytest tools/test_contract.py -q`.
2. Red on a real defect (existing red case re-run): temporarily
   rename a real conduit (e.g. `verdict` at one checked emit site
   in a scripts file, in your working tree only — NOT committed) →
   battery fires; restore → green. Paste both outputs. The
   restore is verified by `git diff --stat` showing only
   tools/test_contract.py changed before you commit.
3. Full suite: `python3 -m pytest tools/ -q` — green.

## Write boundaries
- Yours: `tools/test_contract.py` ONLY.
- NOT yours: everything else — in particular
  `plugin/skills/statiker/scripts/*` (another lane owns those; you
  may DIRTY one temporarily for verifier step 2 but it is restored
  before any commit and never committed).
- ONE commit, by pathspec: `git commit -- tools/test_contract.py`.
  Never `-A`, never amend.
- Deployment-coupled: no — tools/ is not plugin payload; no version
  bump interaction.

## Commit plan
- Guard: the GLOBAL pre-commit dispatcher (read:
  `git config core.hooksPath` →
  `~/dev/Gunther-Schulz/dotfiles/git/hooks`) gates PAYLOAD commits
  only; your file is outside the payload → no bump needed.
  Repo-local chained hooks: none (read: `ls .git/hooks` → no
  non-sample entries).
- Commit trailer, exact:
  `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`

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
`git add` then `git commit` and never `-A`. Trailer:
`Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.
Never amend — always a new commit: the amend-gate denies
subagent amends regardless of ownership (source: §1 amend
rule).
After sending the report your write grant is over: a defect you
find later is REPORTED, never edited or amended (source: §4
ownership rule).

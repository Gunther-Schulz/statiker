# Lane E-J/E-L brief — sonnet: byte-level stderr fallback extraction + requirement-head boundary fix

Title: sonnet: E-J + E-L (byte fallback via shared emit helper; r_lines head boundary)
Working copy: /home/g/dev/Gunther-Schulz/statiker (SHARED with the
dispatcher and one co-lane — disjoint file sets; pathspec commits
only). Scratch: your OWN scratchpad, never this repo or the
dispatcher's scratch.

Base check (first act): base commit is **de012fd**. Run BOTH:
`git merge-base --is-ancestor de012fd HEAD` and
`git log --oneline de012fd..HEAD`. Base contained + nothing on top =
clean start. Commits on top are POSSIBLE here (shared copy — the
dispatcher and lane E-K write disjoint files): run
`git diff --quiet de012fd HEAD -- plugin/skills/statiker/scripts/ tools/test_statiker_git.py tools/test_statiker_record.py`;
unchanged write set → proceed and note the foreign commits in your
report; ANY commit touching your paths → HALT and report. Base not
contained: HALT and report (never rebase, never fast-forward on your
own).

## Grounding basis — read before building; the report cites what was actually read
- The executor skill (`dispatch-guards:executor`) — load FIRST.
- BACKLOG.md, section `## Open`, entries **E-J** and **E-L** — the
  authoritative work items; quoted below for drift-detection, the
  file wins on divergence (report any divergence as a gap).
- `plugin/skills/statiker/scripts/statiker_git.py` — `_stderr_fallback`
  at :124-128 (text-mode `print(file=sys.stderr)`).
- `plugin/skills/statiker/scripts/statiker_record.py` —
  `_stderr_fallback` at :351-356 (byte-level:
  `sys.stderr.buffer.write(text.encode("utf-8","surrogateescape")+b"\n")`,
  flush, OSError pass) — the mirror source; and `HEAD_BOUNDARY_RE`
  at :132 (`^## `) + the boundary loop / `r_lines` computation
  around :515-527.
- `tools/test_statiker_git.py`, `tools/test_statiker_record.py` —
  existing test idioms (fixture style, stash-proof red pattern used
  in this repo's lane history).

## Background (established; verify at the cited lines)
- Both `_stderr_fallback` bodies OPENED by the dispatcher today at
  the lines above (base de012fd). The asymmetry is the E-J defect.
- `HEAD_BOUNDARY_RE`/boundary loop OPENED by the dispatcher today.
- Real-world incident shape for E-L: a production tracker's
  `## Requirement head` at its line 225 is that file's FIRST `## `
  heading, so the tool reads `r_lines: 0` and the head parses as
  malformed entries — from the cycle-12 desk report, unverified at
  this desk (the design does not depend on the exact line number).
- Suite baseline at de012fd: 352 passed (dispatcher's own run,
  today, `python3 -m pytest tools/ -q`).

## The settled design — implement exactly this, do not redesign

### E-J (backlog entry, quoted)
> READY (small) 2026-08-15 — E-J: byte-level fidelity reaches the
> git tool's broken-pipe stderr fallback. [...] Design, decided:
> mirror the record tool's byte-level stderr fallback, by extraction
> or by copy — extraction preferred per T22. Verifier, red-first:
> broken-pipe + non-UTF-8-path arrangement, fallback line carries
> the byte. Done: probe flips, full suite green. Write boundary:
> statiker_git.py, statiker_record.py (if extracting),
> tools/test_statiker_git.py.

Decisions (dispatcher's, final):
- Extraction. NEW module `plugin/skills/statiker/scripts/statiker_emit.py`
  holding the shared byte-level stderr fallback (and, if both tools'
  byte-level stdout emit bodies are duplicates, that too — judge by
  reading; extracting only `_stderr_fallback` is a valid minimum).
- Import form, exact (loader-robust — tests import tools by file
  path, which does not put the scripts dir on sys.path): at each
  tool's import site, before `import statiker_emit`:
  `sys.path.insert(0, str(Path(__file__).resolve().parent))` guarded
  idempotently (skip insert if already present).
- `statiker_git.py`'s `_stderr_fallback` behavior becomes
  byte-identical to the record tool's :351-356 semantics.

### E-L (backlog entry, quoted)
> READY (small) 2026-08-15 — E-L: requirement-head detection
> survives a leading `## ` head heading. [...] Design, decided: the
> head region extends THROUGH a first heading whose title is
> `Requirement head` (case-insensitive exact title) to the NEXT
> `## ` heading; any other first heading keeps the current boundary.
> Verifier, red-first: fixture mirroring the beat-the-books shape
> (head under a first `## Requirement head` heading) reads
> r_lines: 0 under old code, the true count under new; existing
> above-heading fixtures stay green.

Decisions (dispatcher's, final):
- Predicate, exact: the first line matching `HEAD_BOUNDARY_RE` whose
  full line matches `^##\s+[Rr]equirement [Hh]ead\s*$` (implement as
  one case-insensitive regex on the whole title) does NOT terminate
  the head region; the region then ends at the NEXT
  `HEAD_BOUNDARY_RE` match (or EOF). Any other first heading:
  current behavior, unchanged.
- Every consumer of the boundary (`head_region_entries`, `r_lines`)
  follows the corrected boundary; no consumer-specific special
  cases.

## Verifier (in order; real output pasted in the report)
1. E-J red-first, stash-proof (this repo's standard: stash the fix,
   run the probe against old code — expect red; unstash — expect
   green): arrangement = stdout already gone (BrokenPipe on emit)
   AND payload carrying a non-UTF-8 byte
   (surrogateescape-decoded, e.g. `b"caf\xe9"`); assertion = the
   stderr fallback line carries the byte exactly. Old code: fails
   (text-mode print cannot encode the surrogate). New: passes.
2. E-L red-first, stash-proof: fixture tracker whose FIRST `## `
   heading is `## Requirement head` with ≥2 `R<n>.` lines below it;
   old: `r_lines` = 0; new: true count. Plus: all existing record
   fixtures green (the above-heading layouts keep their behavior).
3. Full suite: `python3 -m pytest tools/ -q` — everything green
   (baseline 352 + your new tests). `tools/test_contract.py` must
   stay green; if your change turns it red, that is a FINDING to
   report, never a license to edit that file (it belongs to another
   lane).

## Write boundaries
- Yours: `plugin/skills/statiker/scripts/statiker_git.py`,
  `plugin/skills/statiker/scripts/statiker_record.py`,
  `plugin/skills/statiker/scripts/statiker_emit.py` (NEW —
  `git add -N` it before the pathspec commit),
  `tools/test_statiker_git.py`, `tools/test_statiker_record.py`.
- NOT yours (do not touch): `plugin/skills/statiker/SKILL.md`,
  `tools/test_contract.py`, `BACKLOG.md`, `dev-notes/`,
  `plugin/.claude-plugin/plugin.json`, `docs/`.
- TWO commits, one per entry, by pathspec
  (`git commit -- <paths>`): E-J commit (statiker_git.py,
  statiker_emit.py, statiker_record.py, test_statiker_git.py);
  E-L commit (statiker_record.py, test_statiker_record.py). Never
  `git add` then bare commit, never `-A`, never amend — always a
  new commit.
- Deployment-coupled: yes — scripts are plugin payload.

## Commit plan
- Guard: the GLOBAL pre-commit dispatcher (read that found it:
  `git config core.hooksPath` →
  `~/dev/Gunther-Schulz/dotfiles/git/hooks`; hook source lines
  122–172) blocks payload commits whose manifest version equals the
  ORIGIN manifest's. The 0.2.67 bump is COMMITTED, UNPUSHED
  (exemption armed) at base de012fd — your payload commits ride it.
  Repo-local chained hooks: none (read: `ls .git/hooks` → no
  non-sample entries).
- If a payload commit is nevertheless blocked (someone pushed
  mid-batch): HALT and report — no repair pre-authorized here.
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

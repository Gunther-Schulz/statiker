# st-44 repair lap — brief (sonnet lane, dispatched by statiker-58)

Report channel and conduct tail: in the dispatch prompt. Execute
this brief without design decisions — every fix's design and red
arm is pre-stated; where the world contradicts a pre-stated arm,
that is a GAP to report (slot c), never a bridge.

## Object and ground

Working copy: `/home/g/dev/Gunther-Schulz/statiker`, at current
HEAD (cb3def8 or later; report the sha you started from). Shared
copy — commit by pathspec, unpushed, never amend, never `git add`.

READ FIRST (slot h names what you actually read):
1. `ITEMS.md`, the `## st-44` block — the authoritative
   done-criterion; its text governs over this brief on conflict.
2. `dev-notes/codex-pilot-2026-09-12.md`, section "Stage-2d
   RESULTS" and the st-43 ADJUDICATION record it cites
   (commit 58f9300) — the executed pairs your red arms reuse.
3. The sites: `plugin/skills/statiker/scripts/statiker_record.py`
   (TRIPWIRE_BUDGET_RE and cmd_tripwire), `tools/test_contract.py`
   (section_pointers and its test), `tools/test_statiker_record.py`
   (the pinned/filter race arms), `plugin/skills/statiker/SKILL.md`
   (the head-boundary sentences and the Budget-line tripwire field
   text).

## The four fixes (each red-first: arm red against HEAD before the
fix, green after; suite green at close)

- **A1 — valueless `/ tripwire` refuses instead of failing open.**
  A Budget header ending `/ tripwire` (field present, no value) is
  refused as USAGE_ERROR like a non-integer, never read as
  unarmed. RED (reuse the adjudication's reproduction): header
  `/ tripwire` gives TRIPWIRE_SILENT unarmed with zero lints
  today. CONTROLS: `/ tripwire 2` still arms at threshold 2;
  `/ tripwire abc` still USAGE_ERROR; a Budget line with NO
  tripwire field still reads unarmed. Also correct the branch's
  evidence line that today claims the header "carries no
  tripwire <n> field" when one is present. Class precedent
  (comment style follows the file's existing 0.2.89 fix
  comments): st-34 N2 and 0.2.89 B3, same fail-open family on
  sibling carriers.
- **A2 — section_pointers reports dangling pointers instead of
  losing them.** The instrument stops deriving its match names
  from the page's CURRENT headings: a pointer naming a heading
  that no longer exists lands in `unresolved`, never silently
  leaves the population. RED (the adjudication's measured
  mutant): rename the `## Implementation` heading in an in-memory
  page copy — today found drops 4→2 with unresolved empty and the
  test green; the fixed instrument reports those 2 as unresolved.
  CONTROL: the unmutated page still resolves all pointers with
  unresolved empty.
- **A3 — the pinned/filter race arms assert content, not only
  sha.** Add the assertion that the CONTENT read matches TEXT_A
  (the docstring's stated premise), beside the existing sha
  assertion. RED: a constructed arm emitting commit_a's sha with
  commit_b's content passes today's assertions and fails the new
  one. CONTROL: the honest arm (commit_a sha, commit_a content)
  passes both.
- **A4 — page text only.** SKILL.md's head-boundary sentences
  gain the Requirement-head exception the tool implements: a
  first heading titled `Requirement head` does not close the head
  region; it runs to the next heading or EOF. No tool change —
  the battery is already the spec by the page's own precedence
  sentence. RED for a page-text fix is the adjudication's
  executed pair (parse_tracker: entries=1 under "Cycle 1",
  entries=0 under "Requirement head") re-run and quoted in the
  commit message as the basis; the page edit itself is graded by
  the suite (test_contract page checks) staying green.

## Write boundary

Exactly: `plugin/skills/statiker/scripts/statiker_record.py`,
`plugin/skills/statiker/SKILL.md`, `tools/test_statiker_record.py`,
`tools/test_contract.py`. One commit per fix (A1-A4), pathspec
form `git commit -m "…" -- <files>`, each message carrying the
finding, the red-first arrangement with its outputs, and the
provenance line "st-44 (Stage-2d replay finding A<n>, adjudicated
58f9300)". Commits stay UNPUSHED — the dispatcher integrates and
pushes.

## Verify

`python3 -m pytest tools/ -q` after each fix and at close — full
counts in slot (b), skips dispositioned. Baseline the suite before
any edit and report the baseline counts. SKILL.md edits: this
repo's CLAUDE.md requires skill-craft discipline for page edits —
the A4 edit is two-sentence prose at an existing section; match
the page's own register and note in slot (d) that the checkpoint
review obligation for the batch rides the RELEASE seam, not this
lane.

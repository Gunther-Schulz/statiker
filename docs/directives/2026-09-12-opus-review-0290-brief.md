# opus-review-0290 — checkpoint review before the 0.2.90 pin moves

Fresh-context checkpoint review. You are the verifier; this brief
gives you the artifact and the question, and deliberately gives you
no reasoning about the changes. Read only; write nothing, commit
nothing.

Working copy: `/home/g/dev/Gunther-Schulz/statiker`, at the HEAD
you find (report its sha; the object is the diff below, and a HEAD
past it means only record-carrier commits landed after).

## The object

**Diff since the last reviewed-and-released state:**
`e511c8f..HEAD`, restricted to `plugin/` and `tools/`:

    git diff e511c8f..HEAD -- plugin/ tools/

5 files, 191 insertions, 7 deletions:
`plugin/.claude-plugin/plugin.json` (version only),
`plugin/skills/statiker/SKILL.md`,
`plugin/skills/statiker/scripts/statiker_record.py`,
`tools/test_contract.py`, `tools/test_statiker_record.py`.

**The full skill text as it now stands:**
`plugin/skills/statiker/SKILL.md` at HEAD.

**State you can rely on, executed at brief time:**
`python3 -m pytest tools/ -q` → 571 passed, 2 subtests passed,
0 failed, 0 skipped. Working tree clean at the payload paths.

## The question

Does this object ship as `0.2.90`, or does the pin hold?

Attack it. State each finding as: severity (BLOCKING / notable /
nit), the file and line, what is wrong, and — for anything above a
nit — the EXECUTED pair that shows it: the command or probe that
goes red on the defect and the control that stays green. A finding
asserted without a probe is reported as unverified and labelled so.

Where to press hardest, stated as surface rather than as
suspicion:

- **Machine-read semantics.** The changes alter a header-field
  refusal path (a new regex beside an existing one, a changed
  branch in a subcommand) and page text describing a parser
  boundary. Page text and tool behaviour agreeing is the standing
  contract here — a page sentence that no longer describes what
  the code does is a finding whatever register it is written in.
- **Multi-location verdicts (standing instruction).** Enumerate
  the verdicts the page describes at MORE THAN ONE location and
  check each route token against EVERY seam that names it; the
  fail-closed floor (Route vocabulary) is the rule to check
  against, applying only where the seams actually differ.
- **Instruments.** Several assertions are new or strengthened.
  For each, whether it can go red on the defect it names, and
  whether its reach covers the class it appears to cover or only
  the case its author exercised — including whether any new
  expectation is derived from the artifact it grades.
- **The unchanged neighbours.** A changed refusal path has
  siblings (other carriers of the same field family); whether the
  change's stated reach matches what its siblings still do.

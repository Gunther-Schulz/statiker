# opus-review-0289 — checkpoint review before the 0.2.89 pin moves

Fresh-context checkpoint review. You are the verifier; this brief gives
you the artifact and the question, and deliberately gives you no
reasoning about the changes. Read only; write nothing, commit nothing.

Working copy: `/home/g/dev/Gunther-Schulz/statiker`, at HEAD `5948f67`.
Scratch: your OWN scratchpad, every file slugged `rev0289`.

## The object

**Diff since the last reviewed state:** `7774046..HEAD`, restricted to
`plugin/` and `tools/`:

    git diff 7774046..HEAD -- plugin/ tools/

10 files, 978 insertions, 177 deletions:
`plugin/.claude-plugin/plugin.json`,
`plugin/skills/statiker/SKILL.md`,
`plugin/skills/statiker/scripts/statiker_emit.py`,
`plugin/skills/statiker/scripts/statiker_git.py`,
`plugin/skills/statiker/scripts/statiker_record.py`,
`tools/golden-corpus/tracker.md`,
`tools/golden-corpus/tracker-admission.md`,
`tools/test_contract.py`, `tools/test_statiker_git.py`,
`tools/test_statiker_record.py`.

**The full skill text as it now stands:**
`plugin/skills/statiker/SKILL.md` at HEAD — 1689 operational lines by
the repo's own count
(`awk '/^---$/{c++} c>=2' plugin/skills/statiker/SKILL.md | grep -vc '^$'`).

**State you can rely on, each executed at brief time:**
`python3 -m pytest tools/ -q` → 563 passed, 2 subtests passed, 0
failed, 0 skipped. Working tree clean. Nothing pushed.

## The question

Does this object ship as `0.2.89`, or does the pin hold?

Attack it. Every finding gets a recorded disposition before the pin
moves, so state each one as: severity (BLOCKING / notable / nit), the
file and line, what is wrong, and — for anything above a nit — the
EXECUTED pair that shows it: the command or probe that goes red on the
defect and the control that stays green. A finding asserted without a
probe is reported as unverified and labelled so.

Where to press hardest, stated as surface rather than as suspicion:

- **Machine-read semantics.** Several changes add or alter tokens,
  predicates and record forms that the tools parse: a route registry
  and a `route` field on every emitted verdict; a new record entry form
  the record tool reads; a widened refusal on a header field; changed
  git-ref resolution in two commands. Page text and tool behaviour
  agreeing is the standing contract here — a page sentence that no
  longer describes what the code does is a finding whatever register it
  is written in.
- **Instruments.** Several checks are new. For each, the question is
  whether it can go red on the defect it names, and whether its reach
  covers the whole class it appears to cover or only the case its
  author exercised. A check that passes whether or not the work
  happened is a finding.
- **Consistency across the page.** Where a rule is stated in more than
  one passage, do the statements agree with each other and with the
  code?

## What this review does NOT decide

The skill's SIZE. The page's line count and the compression question
were decided elsewhere today and are out of scope; do not grade the
object against a line budget, and do not propose deletions on size
grounds. Deletions proposed because text is WRONG are in scope.

## Verifier plumbing

`pytest tools/ -q` runs the whole suite. The record and git tools are
`plugin/skills/statiker/scripts/statiker_{record,git}.py`; each prints
evidence lines and exactly one final verdict line. Probe them in a
throwaway git repo under your own scratch — never in this working copy.

NO REPORT FILE. Your findings go in your SendMessage reply — a file you
write is not a report, is not read as one, and reaches no one. Split
into labeled parts (1/N) past the size gate. Transient probe scratch
goes in YOUR OWN scratchpad, never the dispatcher's, and is not a
report file.
Report channel: SendMessage to the dispatcher — your final text reaches
no one.
Return your findings in ONE message where they fit: the verdict (pin
moves / pin holds) plus the findings with their bases. Where the basis
is a check you RAN, its full counts come with it, skips included and
dispositioned: a skipped check did not run, and a verdict resting on
one is could-not-verify, not clean. Every claim about something outside
your own work names the read that opened it, or carries "inferred,
unverified"; a recommendation resting on an unopened claim carries the
grade too. A missing decision, file, or value is surfaced as a gap,
never bridged with a guess. No repo writes, no interim messages.

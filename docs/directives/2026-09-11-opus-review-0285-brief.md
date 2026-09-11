# Title: opus: 0.2.85 checkpoint review (fresh context)

Verifier dispatch — artifact + definition + question + read-only tail.
Dispatcher: statiker-4d, 2026-09-11. Lane name: opus-review-0285.

Desk note (not sent to the lane): dispatched 15:05 beside
sonnet-recheck-a (st-9..st-14) and sonnet-recheck-b (st-15..st-20),
which re-check each migrated BACKLOG body's premise at HEAD 49e9529
for the retirement pass. Horizons: rechecks 15:39, review 16:03. A
successor desk settles each at the ARTIFACT: a disposition section
for this review in dev-notes/OBSERVATIONS.md, grade/park/drop lines
for st-9..st-20 in ITEMS.md or ITEMS-DONE.md. Nothing booked there
means LOST, never "still running": re-dispatch or book it void.

Working copy: /home/g/dev/Gunther-Schulz/statiker, HEAD 49e9529
(read at compose time: `git rev-parse --short HEAD`, tree clean).
READ-ONLY: no repo writes of any kind. Run the suite with
`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tools/ -q -p no:cacheprovider`;
mutation or fixture probes run on COPIES in your own scratchpad.

## Artifact

- The change under review: `git diff cfeff79 49e9529 -- plugin tools`
  (5 files: plugin/.claude-plugin/plugin.json,
  plugin/skills/statiker/SKILL.md,
  plugin/skills/statiker/scripts/statiker_record.py,
  tools/test_contract.py, tools/test_statiker_record.py).
  cfeff79 is the last REVIEWED state (its plugin/ and tools/ trees are
  byte-identical to 34b33ec: `git diff --stat 34b33ec cfeff79 -- plugin
  tools` is empty).
- The full page as it would ship: plugin/skills/statiker/SKILL.md at
  49e9529 — read it whole, not only the hunks.
- The tool as it would ship:
  plugin/skills/statiker/scripts/statiker_record.py at 49e9529.

## Definition (what the change is required to do)

dev-notes/OBSERVATIONS.md, the section headed
`## 2026-09-10 — 0.2.84 re-review dispositions` (anchor on that
heading text), bullets RB1 through RT-b. Each bullet's FIX sentence is
the requirement; RN-d and RT-b are recorded as no-change.

## Question

Does the 0.2.85 batch move the pin — is it correct and safe to ship to
desk runs? Specifically:

1. Per disposition RB1, RB2, RN-a, RN-b, RN-c, RN-e, RN-f, RT-a: does
   the change realize its FIX sentence, at the reach the sentence
   states (not only on the one fixture shape)?
2. What does the batch break, over-fire on, or silently NARROW
   elsewhere — existing verdicts, holds and exemptions, page/tool
   agreement (every record form, label, tag, hold code or gate the
   page names vs what the tool reads and emits), the contract checks
   in tools/test_contract.py, repair texts that the grammar refuses?
3. Is each new or changed instrument (the `ambiguous-citation` hold,
   the repair-coverage contract check, the changed exemption
   predicates) able to go red on the defect it exists for, and does
   its assurance claim more than its predicate establishes?

Grade every finding blocking / notable / nit, each with an EXECUTED
red/green pair (command + output: the case showing the defect, and
the control showing the correct behaviour); a finding without an
executed check carries "unverified". Close with a one-line verdict:
pin moves / pin does NOT move.

## Tail

NO REPORT FILE. Your findings go in your SendMessage reply — a
file you write is not a report, is not read as one, and reaches
no one. Split into labeled parts (1/N) past the size gate.
Transient probe scratch goes in YOUR OWN scratchpad, never the
dispatcher's, and is not a report file.
Report channel: SendMessage to the dispatcher — your final text reaches no one.
Return your findings in ONE message where they fit (verifier:
verdict + basis; discovery: the N named facts, sources actually
read). Where the basis is a check you RAN, its full counts come
with it, skips included and dispositioned: a skipped check did
not run, and a verdict resting on one is could-not-verify, not
clean (source: §2 slot (b), carried into a lane that has no
slots). Every claim about something OUTSIDE your own work — a
file you did not write, a mechanism, another repo, a tool's
behavior — names the read that opened it, or carries "inferred,
unverified"; a recommendation resting on an unopened claim
carries the grade too (source: §2, the report-provenance rule).
A missing decision, file, or value is surfaced
as a gap, never bridged with a guess. No repo writes, no
interim messages.
Message ≤3000 chars each; a longer report is split into labeled
parts (1/N).

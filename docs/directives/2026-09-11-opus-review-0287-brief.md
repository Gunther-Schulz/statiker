# Title: opus: 0.2.87 checkpoint review (fresh context)

Verifier dispatch — artifact + definition + question + read-only tail.
Dispatcher: statiker-4d, 2026-09-11. Lane name: opus-review-0287.

Working copy: /home/g/dev/Gunther-Schulz/statiker, HEAD 769e7f2 (read
at dispatch: `git rev-parse --short HEAD`, tree clean).
READ-ONLY: no repo writes of any kind. Run the suite with
`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tools/ -q -p no:cacheprovider`;
mutation or fixture probes run on COPIES under
`/tmp/claude-1000/-home-g-dev-Gunther-Schulz-statiker/f59bcaca-7615-4029-95ca-3a049796cc24/scratchpad/opus-review-0287/`
only — the scratch root is shared with other lanes, so never write
outside that slugged directory.

Reading scope: plugin/, tools/, and the definition pasted below. Do
NOT open dev-notes/, docs/, ITEMS.md, ITEMS-DONE.md, LEDGER.md,
BACKLOG.md or PLAN.md — they carry the dispatcher's own reasoning and
bookkeeping about this change, which a fresh-context review must not
inherit. Commit messages are readable; they are the author's claims,
not evidence.

## Artifact

- The change under review: `git diff 378aa68 769e7f2 -- plugin tools`.
  378aa68 is the last REVIEWED state (plugin/ and tools/ are
  byte-identical from 378aa68 through 136a7c2, the released 0.2.86).
  The payload commits in that range: 50fb0cd (manifest bump), ff28885 (st-28), 9d3352d, 0a0440d, 9fc8c69,
  bca3854, ce8e450, 43baee9, 8659aa9, 468a76c (st-30 items 1–8), 769e7f2
  (st-28 follow-up). The other commits in the range (3202d13, 1e10047,
  598baef, 0a29bf0) touch no path under plugin/ or tools/.
- The full page as it would ship: plugin/skills/statiker/SKILL.md at
  769e7f2 — read it whole, not only the hunks.
- The tool as it would ship:
  plugin/skills/statiker/scripts/statiker_record.py at 769e7f2.
- The new golden corpus: tools/golden-corpus/tracker.md and
  tools/golden-corpus/expected-violations.json at 769e7f2.

## Definition (what the change is required to do — pasted verbatim)

Item st-28, its done-criterion verbatim:

"a golden-corpus sweep test: one rich fixture tracker exercising every
violation code in RULE_MINT_VERSION (positive and known-clean rows per
code), a committed golden file of expected violations, and a test that
diffs the sweep's full hit-set against it, red on ANY code's hits
shrinking or growing; regenerating the golden requires a reviewed diff,
never a blind overwrite. Red-first: run the corpus at c19c829 vs
2baa349 pre-repair and show the B1/B2 rows vanish (the incident
reproduced as the fixture's own proof); reach: the corpus derives its
code list from the tool's own RULE_MINT_VERSION table at runtime, so a
new code with no corpus row goes red by construction"

The settled design for st-28, as briefed:

"Outcome: any change in the set of violations `sweep` reports over one
fixed rich tracker — a code's hits shrinking OR growing — turns the
suite red, and a code minted into RULE_MINT_VERSION with no corpus row
turns it red too." Golden format: "a JSON list of objects `{"line":
<int>, "code": <str>, "text": <that fixture line, stripped>}`, sorted by
(line, code) — the hit SET only". Comparison: "parsed sets, never
rendered text. On mismatch the failure message lists REMOVED hits (in
golden, not produced) and ADDED hits (produced, not in golden)".
Coverage: "the code list comes from the RUNNING module's
`RULE_MINT_VERSION` (imported, never a copied list). Assert
`set(RULE_MINT_VERSION) == codes_in_golden | set(EXEMPT)` and
`codes_in_golden & set(EXEMPT) == set()`. `EXEMPT` is a dict in the
test, code → reason, admissible ONLY for a code `sweep` cannot emit
over a single tracker file; each reason names the verb or external
state that emits it." Rows: "at least one positive row per non-exempt
code; beside it, a known-clean row one edit away that must NOT raise
that code, where such a variant exists". Regeneration:
"`STATIKER_GOLDEN_REGEN=1` makes the test WRITE the golden and then
FAIL in that same run … It is never green on a regeneration run."

The follow-up disposition for st-28, recorded before its
implementation (it supersedes "one fixed rich tracker" for one code):
"a minimal tracker in the RecordFixture header form whose Status or
Phase line is VALID and placed past ADMISSION_WINDOW (line 20) so
sweep emits admission-window … TestGoldenCorpusSweep runs over BOTH
(tracker, golden) pairs: the hit-set test per pair (subTest per pair);
coverage asserts set(RULE_MINT_VERSION) == union of codes across both
goldens | set(EXEMPT), disjointness kept; EXEMPT becomes {} (keep the
dict and its admission comment rule). STATIKER_GOLDEN_REGEN=1 writes
both goldens and fails the run."

Item st-30, its done-criterion verbatim:

"per the reviewer's executed pairs: (1) violation text and docstring
name the same-id, same-unit supersede-whole form, red: following
today's text gives corrects-nothing; (2) the pointer reads '(below)';
(3) a Budget-header tripwire below 1 is refused like --threshold, red:
'tripwire 0' gives TRIPWIRE_FIRES today; (4) filter's error halts carry
no sha field, red: --sha 'HEAD^{tree}' prints one today; (5) and (6)
the docstrings state the derivation's actual reach; (7) pinned resolves
the sha once as filter now does, red: an abbreviated sha is echoed
today; (8) skill-lint reports 0 wrap flags on SKILL.md. Rides the next
version bump under a checkpoint review (items 3, 4 and 7 are
machine-read)"

The settled outcomes for st-30, as briefed:

1. "every text in plugin/ and tools/ that prescribes the
   `declarator-bookkeeping` repair names the same-id, same-unit
   supersede-whole form (restate the unit's full write-set under the
   same id and unit with `(corrects line <n>)`)."
2. "the re-lock pointer points where clause (b) is."
3. "a tripwire threshold below 1 is refused on BOTH carriers. A
   Budget-header `tripwire <n>` with n < 1 is refused with the same
   verdict the `--threshold < 1` refusal already uses".
4. "no halt verdict carries a `sha` or `shas` field unless the value
   names LANDED commits (the page's override, SKILL.md:114-117, routes
   any such field as landed). … drop the field wherever the value is
   an input argument or unresolved ref rather than a landed commit;
   keep it where it names landed commits."
5. "every coverage docstring on the emission-site derivation states its
   actual reach — literal code strings at emission sites; a code
   emitted from a variable or inside a tuple return is outside it."
6. "no test docstring describes `ambiguous-citation` as live (withdrawn
   at 0.2.86 B1)."
7. "`pinned` resolves its sha argument once, via `git rev-parse
   --verify <sha>^{commit}` — the form `filter` already uses … — and
   emits the resolved full sha; an unresolvable argument takes filter's
   error route (with no `sha` field, per item 4)."
8. "skill-lint reports 0 wrap flags on SKILL.md."

## Question

Does the 0.2.87 batch move the pin — is it correct and safe to ship to
desk runs? Specifically:

1. Per item st-28 and st-30(1)…(8): does the change realize its
   outcome at the reach the text states, not only on the one fixture
   shape?
2. What does the batch break, over-fire on, or silently NARROW
   elsewhere — existing verdicts, holds and exemptions, page/tool
   agreement (every record form, label, tag, hold code, halt field or
   gate the page names vs what the tool reads and emits), the contract
   checks in tools/test_contract.py, repair texts the grammar refuses?
3. Is each changed or new instrument (the golden-corpus test and its
   exemptions, the new refusal, the halt-field classification, the
   resolve-once path, the new tests) able to go red on the defect it
   exists for, and does any assurance — a docstring, a page sentence,
   a test name, an exemption reason — claim more than its predicate
   establishes?

Grade every finding blocking / notable / nit, each with an EXECUTED
red/green pair (command + output: the case showing the defect, and
the control showing the correct behaviour); a finding without an
executed check carries "unverified". Name each finding's SITE (file
and function or page passage). Close with a one-line verdict: pin
moves / pin does NOT move.

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

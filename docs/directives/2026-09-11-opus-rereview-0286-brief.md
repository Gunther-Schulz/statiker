# Title: opus: 0.2.86 re-review (fresh context)

Verifier dispatch — artifact + definition + question + read-only tail.
Dispatcher: statiker-4d, 2026-09-11. Lane name: opus-rereview-0286.

Working copy: /home/g/dev/Gunther-Schulz/statiker, HEAD 378aa68 (read
at dispatch: `git rev-parse --short HEAD`, tree clean).
READ-ONLY: no repo writes of any kind. Run the suite with
`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tools/ -q -p no:cacheprovider`;
mutation or fixture probes run on COPIES in YOUR OWN scratchpad (never
the dispatcher's).

Reading scope: plugin/, tools/, and the definition pasted below. Do
NOT open dev-notes/, docs/, ITEMS.md, ITEMS-DONE.md, LEDGER.md,
BACKLOG.md or PLAN.md — they carry the dispatcher's own reasoning and
bookkeeping about this change, which a fresh-context review must not
inherit. Commit messages are readable; they are the author's claims,
not evidence.

## Artifact

- The change under review: `git diff 49e9529 378aa68 -- plugin tools`.
  49e9529 is the last REVIEWED state. The payload commits in that
  range: d859a75 (manifest bump), 584970b, fa870eb, 718f223, 612bd8a,
  b65197e, 85e6067, 9c4f2a7, 57cd519, 8d3ebb6, 378aa68 (a desk-restored
  test).
- The full page as it would ship: plugin/skills/statiker/SKILL.md at
  378aa68 — read it whole, not only the hunks.
- The tool as it would ship:
  plugin/skills/statiker/scripts/statiker_record.py at 378aa68.

## Definition (what the change is required to do — pasted verbatim)

Disposition bullets, as recorded before implementation:

- **B1 (blocking; RN-b re-decided: WITHDRAW the mint).**
  `ambiguous-citation` holds the page-mandated foreign citation
  (`basis: dev-notes/other-run.md F20`, and `basis: run other-run:
  F20`) whenever this run carries its own live F20, and its repair
  text cannot clear it — the record is already named. A SUBSTANCE
  code (never retro), exemptible only by operator SWEEP_EXEMPT, so an
  unattended run closes FAILED on a correct citation. Field reading
  (desk, 2026-09-11): 0 record-named citations in 1006 basis lines
  across the three real statiker trackers
  (beat-the-books/.clippy/runs; the pattern shown matching both
  planted forms). RN-b guarded a reviewer-constructed hole with no
  field incident. DECISION: remove the hold emission, the repair
  constant and its REPAIR_FORMS entry, the RULE_MINT_VERSION row, and
  the page's routing sentence; the page states the exemption's
  REACH instead — an id under a record-name token is not checked
  against this run's own invalidations. That is the RN-b hole,
  accepted as a recorded residual here. Red arms (reviewer's
  executed pair): the live-collision and run-label forms read
  SWEEP_CLEAN after (hold today); control `dev-notes/other-run.md F7`
  clean both ways; the residual PINNED by assertion — doc-path +
  same-run INVALIDATED F20 raises no hold — so it stays explicit,
  never silent.
- **N1 (notable; RB1's spellings clause unmet).** waves_over_units
  records the raw group(2), suffix included, as an alias, so the
  sanctioned repair prints spellings `{"a.txt": ["a.txt", "a.txt
  (corrects line <n>)"]}`; RB1's FIX said spellings stays empty. FIX:
  the recorded alias is the suffix-stripped spelling. The committed
  RB1 test targets a CLEAN line (lint: corrects-nothing, a shape the
  grammar refuses) and never asserts spellings — re-point it at the
  reviewer's sanctioned shape and assert spellings == {} beside the
  serialization. Red arm: that shape, spellings non-empty today;
  plain-declaration control {}.
- **N2 (notable; RB1 side effect, silent direction).** The near-miss
  check now runs on normpath output, so `unit U1 write-set: a.txt
  b/../c.txt` lints clean and waves reads U1 and U2 disjoint. FIX:
  split the resolver — ONE suffix-strip helper shared by both sites;
  normpath only at the consuming site (waves_over_units). Red arm:
  that field beside U2 a.txt fires write-set-path-near-miss and waves
  halts WAVES_RECORD_MALFORMED after (LINT_CLEAN / WAVES_COMPUTED
  today); control `a.txt c.txt` fires both ways.
- **N3 (notable; RB2's page side).** SKILL.md's declarator-bookkeeping
  clause ("UNLESS the correcting line is itself a fresh `unit U<k>
  write-set: <path>` redeclaration") and REPAIR_DECLARATOR_BOOKKEEPING
  both omit the same-unit condition the tool now enforces. FIX: both
  name the SAME unit. The tool pair is already committed (TestRB2);
  the page side rides the re-review.
- **T1 (nit; RN-e reach).** The carve-out reads "a reconciliation that
  WIDENS the R-line's demand"; a desk [AMENDED] R-line that widens
  stays on the fresh-read route. FIX: "an amendment or reconciliation
  that WIDENS the R-line's demand".
- **T2 (nit; RN-f assurance wider than predicate).** The contract check
  derives literal code strings only; a code emitted from a variable
  passes it (reviewer's planted mutant; no live instance). FIX: the
  class docstring states that reach. No machinery.
- **T3 (nit; RN-c page definition stale).** The page's record-name
  token "ending `.md` or `.md:`" omits the `()[].,;:` strip the tool
  applies before matching. FIX: the definition names the same strip.
- **T4 (nit; RN-a test's red arm).** The fixture puts a `record:`
  repair on a machine-token target, so lint still fails
  (repair-scope-change) and the test asserts only NotIn. FIX: re-point
  at the reviewer's body-content target (a declarator line missing
  its basis clause) and assert LINT_CLEAN; red by removing RN-a's
  INVALIDATED test from the condition; live control unchanged.
- **T5 (nit; no change).** A same-unit correction to a different path
  supersedes that unit's whole write-set — the declarator narrowing
  its own set, which is the supersede-whole semantics; old tool
  identical.

Bundled item st-14, its done-criterion verbatim:

"per BACKLOG.md:526-551 for the four live items: (1) resolve --sha
once via rev-parse --verify <sha>^{commit} and emit the resolved
value; (5) reject --threshold < 1; (4) one-line pointer from the
re-lock passage to P24's clause (b); (6) 'a new round opens only if'
becomes 'the verdict reads SUSTAIN_OK only if'. Red-first battery
cases for (1) and (5); (4) and (6) with the suite green. Rides a
version bump, never its own release: into the 0.2.85 repair lap if
the checkpoint review blocks, else the next batch"

## Question

Does the 0.2.86 batch move the pin — is it correct and safe to ship to
desk runs? Specifically:

1. Per item B1, N1, N2, N3, T1, T2, T3, T4 and st-14: does the change
   realize its FIX (or done-criterion) at the reach the text states,
   not only on the one fixture shape?
2. What does the batch break, over-fire on, or silently NARROW
   elsewhere — existing verdicts, holds and exemptions, page/tool
   agreement (every record form, label, tag, hold code or gate the
   page names vs what the tool reads and emits), the contract checks
   in tools/test_contract.py, repair texts the grammar refuses?
3. Is each changed instrument (the split write-set resolver, the
   near-miss predicate, the waves alias, the re-pointed tests, the
   new st-14 checks) able to go red on the defect it exists for, and
   does any assurance — a docstring, a page sentence, a test name —
   claim more than its predicate establishes?

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

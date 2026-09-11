# Title: opus: 0.2.88 checkpoint review — st-29 lap A (SKILL.md compression, page only)

Verifier dispatch — artifact + definition + question + read-only tail.
Dispatcher: statiker-4d, 2026-09-11. Lane name: opus-review-0288.

Working copy: /home/g/dev/Gunther-Schulz/statiker, HEAD 7774046 (read
at dispatch: `git rev-parse --short HEAD`, tree clean).
READ-ONLY: no repo writes of any kind. Run the suite with
`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tools/ -q -p no:cacheprovider`;
probes run on COPIES under
`/tmp/claude-1000/-home-g-dev-Gunther-Schulz-statiker/f59bcaca-7615-4029-95ca-3a049796cc24/scratchpad/opus-review-0288/`
only — the scratch root is shared with other lanes, so never write
outside that slugged directory.

Reading scope: plugin/, tools/, plugin/hooks/, and EXACTLY these two
files under docs/ — they are the definition:
`docs/directives/2026-09-11-st29-lapA-clause-table.md` and
`docs/directives/2026-09-11-sonnet-lapA-0288-brief.md` (its "The settled
design" section). Beyond those, you may SEARCH (never read whole) the
rest of the repo — dev-notes/, docs/, BEGEHUNG-MAP.md, PLAN.md,
CLAUDE.md — only for the reader census in question 3. Do NOT open
ITEMS.md, ITEMS-DONE.md or LEDGER.md, nor any OBSERVATIONS.md section
about this lap's grading: they carry the dispatcher's own reasoning
about this change, which a fresh-context review must not inherit.
Commit messages are the author's claims, not evidence.

## Artifact

- The change under review: `git diff 7791b63 7774046 -- plugin`.
  7791b63 is the released 0.2.87 (the last REVIEWED payload). The
  payload commits in that range: 9670a40 (manifest bump 0.2.87 → 0.2.88), 5a26366, d65decd,
  2ac9f4c, af0c10b, ad7a869, 9483dbc, 161b768, f4a5d05, 69175de,
  ce8eae5 (one per page section), 75c3fcd (wrap fixups plus the third
  pointer fix), b13d31e (rows R27, R41, I9 applied after a miss),
  a8d9d28 (I9 reverted to its pinned text under the desk's
  accept-as-is ruling), 7774046 (I9 rewrap, whitespace only). tools/ is unchanged in
  the range.
- The page before: `git show 769e7f2:plugin/skills/statiker/SKILL.md`
  (byte-identical to 7791b63's page) — the table's pin.
- The page as it would ship: plugin/skills/statiker/SKILL.md at
  7774046 — read it whole, not only the hunks.

## Definition (what the change is required to do)

The clause table (file above) is the normative per-row definition:
every row's line range at the pin, its disposition (KEEP / TIGHTEN /
DELETE), its must-survive list (TIGHTEN) or load home (DELETE), its
verdict tokens, and its target line count. Its "Rules applied" and
"Table conventions" sections define how to read it.

The application rules, pasted verbatim from the build brief's settled
design:

"1. KEEP rows: untouched, byte for byte.
2. DELETE row (R19 only): remove its line range.
3. TIGHTEN rows: replace the row's range with shorter text that
   carries EVERY item in its must-survive cell and EVERY verdict token
   in its tokens column, verbatim where the cell quotes it (backticked
   literals, UPPER_SNAKE tokens, quoted phrases), at or under the row's
   target line count. Where keeping every must-survive item needs more
   lines than the target, KEEP THE ITEMS, exceed the target, and list
   the row in the report — never drop an item to meet a target.
4. No new content: no rule, clause, hedge, history or pointer the pinned
   text does not carry, except the two pointer fixes below. Wrap to the
   page's existing width.
5. Pointer fixes (desk-decided gaps G2 and G3):
   - G2: both occurrences of "the 0.68 NARROWING route" (pinned ~:297,
     row R13; ~:1260, row A23) become "the NARROWING route"; the section
     pointer that follows each stays as written.
   - G3: the `sustain` gloss in The tools (pinned ~:101, row T6) reads
     `(Stop rule, "That closes design")`; it becomes `(The attack, "That
     closes design")`."

Rulings made after the build, each part of the definition:
- Row I9 (Implementation) is exempt from rule 3's shortening: its
  must-survive cell carries essentially the whole row, so it stands
  as pinned.
- A third pointer fix is admitted: "(Fire-born clauses, below)" becomes
  "(Fire-born and hypothesis clauses, below)" — the heading's actual
  name.
- TIGHTEN rows may exceed their targets where their must-survive items
  required it (rule 3); line counts are not graded.
- The one intended no-change surface: verdict tokens, since
  tools/test_contract.py's TestVerdictParity binds page and tool.

## Question

Does the 0.2.88 page move the pin — is it correct and safe to ship to
desk runs? Specifically:

1. LOAD LOSS: does any TIGHTEN or DELETE row, as realized, drop a rule,
   condition, route, exception, form, or pointer that a desk needs and
   that the page no longer states anywhere else? Its must-survive list
   is the author's claim of completeness, not proof of it — read each
   changed row's pinned text against its realized text.
2. SEMANTIC DRIFT: does any rewording change a meaning — a MUST into a
   may, a scope widened or narrowed, an ordering or precedence altered,
   a condition's polarity flipped, a route re-targeted — or add content
   rule 4 forbids? Do KEEP rows stand byte for byte (whitespace aside)?
3. READERS OF DROPPED TEXT: is any dropped phrase, pointer target or
   passage cited from outside the page — the stop-guard hook
   (plugin/hooks/), tools/ tests or fixtures, dev-notes/, docs/,
   BEGEHUNG-MAP.md, PLAN.md, CLAUDE.md — such that the citation now
   dangles? Search by the dropped text's distinctive words, and show
   each search live on a phrase that IS present before reporting a
   zero.
4. MECHANICS: the page's verdict-token set equals the pin's; the suite,
   skill-lint (skill-craft 2.2.4, `--diff-base 7791b63`) and every
   pointer resolve; the three pointer fixes are realized; no
   "(Stop rule, "That closes design")" or "0.68 NARROWING" remains.

Grade every finding blocking / notable / nit, each with an EXECUTED
red/green pair where the finding is checkable (command + output: the
case showing the defect, and the control showing correct behaviour);
a load-loss or drift finding carries the pinned text and the realized
text side by side as its pair. A finding without an executed check or a
side-by-side quote carries "unverified". Name each finding's SITE (row
id and SKILL.md line at 7774046). Close with a one-line verdict: pin
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

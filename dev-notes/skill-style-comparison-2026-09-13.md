# Skill-style comparison — pstack vs the house skills (raw lane report)

Provenance: opus lane opus-skill-style-comparison, 2026-09-13, statiker desk session 1b204567. Sample: 5 pstack files (mirror 7366ac1) vs 6 house skills (versions in the body), each read in full; sampling caveat in the body's closer (iv) bounds every claim. Dispatcher-added header; body verbatim below.
Consumer: the booked compression pass (loading/size axes, import 1); skill-craft doctrine work sc-item booked this date (as-of stamps, import 2/3 decisions).

---

# Skill-writing STYLE comparison — pstack (side A) vs this stack's house skills (side B)

Read-only. Grades how the skills are WRITTEN. Content/design merit is out of scope.
Date: 2026-09-13. All 11 files read in full.

## Sources actually read (in full)

Side A (pstack, author poteto), all under /home/g/dev/reference/cursor-plugins/pstack/skills/:
- poteto-mode/SKILL.md (143 lines)
- poteto-mode/playbooks/shipping.md (17)
- principle-encode-lessons-in-structure/SKILL.md (31)
- create-verification-skill/SKILL.md (44)
- unslop/SKILL.md (68)

Side B:
- /home/g/.claude/plugins/cache/dispatch-guards-marketplace/dispatch-guards/0.11.14/skills/dispatch/SKILL.md (1107)
- .../dispatch-guards/0.11.14/skills/executor/SKILL.md (199)
- /home/g/.claude/plugins/cache/begehung/begehung/0.3.3/skills/begehung/SKILL.md (244)
- /home/g/.claude/plugins/cache/kaemmung/kaemmung/0.1.2/skills/kaemmung/SKILL.md (103)
- /home/g/.claude/plugins/cache/skill-craft-marketplace/skill-craft/2.2.4/skills/skill-craft/SKILL.md (489)
- /home/g/dev/Gunther-Schulz/statiker/plugin/skills/statiker/SKILL.md (1808)

No references/ file was opened on either side (skill-craft's SKILL.md answered every criterion needed).

## Measurements taken (instruments named)

All by python3 over the file bytes, or ugrep. Rough where labelled.

| file | body lines | words | words/sentence* | em dashes | ALLCAPS/1k words | evidence markers** | per 100 body lines |
|---|---|---|---|---|---|---|---|
| A poteto-mode | 107 | 2610 | 11.4 | 0 | 5.0 | 2 | 1.9 |
| A shipping.md | 13 | 795 | 13.9 | 0 | 26.4 | 0 | 0.0 |
| A principle-encode | 23 | 325 | 15.5 | 0 | 3.1 | 0 | 0.0 |
| A create-verification | 29 | 936 | 18.7 | 5 | 23.5 | 0 | 0.0 |
| A unslop | 48 | 873 | 7.9 | 0 | 2.3 | 1 | 2.1 |
| B dispatch | 1069 | 10005 | 37.9 | 220 | 28.9 | 41 | 3.8 |
| B executor | 180 | 1673 | 22.3 | 34 | 22.1 | 2 | 1.1 |
| B begehung | 218 | 2165 | 24.3 | 52 | 13.9 | 11 | 5.0 |
| B kaemmung | 88 | 798 | 21.0 | 18 | 6.3 | 7 | 8.0 |
| B skill-craft | 435 | 3771 | 26.6 | 95 | 4.2 | 14 | 3.2 |
| B statiker | 1716 | 15631 | 48.2 | 432 | 43.8 | 25 | 1.5 |

\* crude: words divided by count of `[.!?]` followed by whitespace. Abbreviations and
`§` citations inflate the denominator slightly; the A/B gap (8–19 vs 21–48) is far
larger than that error.
\*\* case-insensitive occurrences of measured|observed|incident|provenance|founding.
Positive control: the pattern found `Measured:` at executor:51 and executor:83 after
case-folding (a case-sensitive first pass returned 0 for that file — the false zero
was caught by the control, not by inspection).

Frontmatter, scoped to the `---` block (a whole-file match falsely reported skill-craft
as delisted, because its BODY discusses the key at line 87):
- Side A 5/5: `disable-model-invocation: true`. Descriptions 49–274 chars (mean 178).
- Side B 6/6: model-invoked (no such key). Descriptions 366–595 chars (mean 499).

statiker operational lines by the repo's own verify command
(`awk '/^---$/{c++} c>=2' … | grep -vc '^$'`): **1713**, against the PLAN.md
stabilization target of ~150 — 11.4×, corroborating the repo CLAUDE.md's own
"now 11× its target".

---

## 1. Trigger / description discipline

**Verdict: opposite strategies, each with the risk the other avoids. A puts routing in
router PROSE at zero always-on cost and is inert outside its router; B puts it in an
always-paid description and buys reach at 2.8× A's per-skill description length.**

Side A, all five sampled skills are delisted (`disable-model-invocation: true`,
verified in the frontmatter block). Triggering therefore happens two ways, neither of
them the description. First, a one-line router heuristic in frontmatter —
poteto-mode/SKILL.md:8: `reminder: New task? Playbook match or rigor needed ->
apply /poteto-mode. Casual turn or user opts out -> don't.` Both directions in one
line. Second, condition-to-destination prose, one line per branch, e.g.
poteto-mode/SKILL.md:19 `- Nontrivial change, architecture decision, or "are we sure?"
→ the **how** skill.`

A's over-trigger discipline is the strongest single specimen in the sample, because it
names the COLLIDING skill rather than describing its own scope —
poteto-mode/SKILL.md:31: "Any PR-status request → the **Babysit** playbook
(`playbooks/babysit.md`), and not Cursor's built-in babysit skill, whose description
matches the same words. That includes "babysit this", "get it green", "address the
bugbot comments", and the commonest phrasing, "check on PR X" … Never triggered by
merely opening a PR." Three real user phrasings plus an explicit negative case.

A's under-trigger risk is structural and visible in the text: unslop/SKILL.md:3 reads
"Cut AI tells from any writing. Must always apply." — but the file is delisted, so
"always" is delivered only by poteto-mode/SKILL.md:26 ("Any prose surface → the
**unslop** skill. Your reply is a prose surface."). Outside poteto mode nothing loads
it. Graded against skill-craft's own measurement (skill-craft/SKILL.md:87-96: listed
descriptions resolved prose invocations 12/12, delisted 0/12), A's delisting is safe
exactly to the extent that every entry point is a slash command or the router.

Side B carries the trigger in the description and — uniformly, 6/6 — closes with a
negative clause. kaemmung/SKILL.md:3: "Not for booking or grading single items (the
carrier's own rules), reviewing a system for defects (begehung), designing a change
(statiker), or code cleanup." dispatch/SKILL.md:3: "Not for deciding WHETHER to
dispatch — the model-routing table in the operator corpus governs that."
statiker/SKILL.md:3: "use only when the operator explicitly invokes statiker or
requests a statiker run."

B's risk is cost, not reach: mean 499 description chars paid every turn, and two of the
six carry body identity into the pointer, which skill-craft/SKILL.md:80-82 forbids
("one trigger per genuinely distinct branch — synonyms renaming one branch are one
branch written twice; cut identity the body already carries"). begehung/SKILL.md:3
carries "lens pre-registered per round, per-lens yield stop, darkest-corner rotation,
no global done-claim" — four body mechanisms in the always-loaded line. kaemmung's
description spells one branch five ways: "backlog aufräumen", "das nimmt kein Ende",
"cull/merge/batch", "a carrier outgrown its own purpose", "Kämmung".

## 2. Enforce vs teach — does the text know which it is?

**Verdict: B, decisively, and it is B's single most transferable habit. A's sampled
files ship no mechanism and never say so; B marks the boundary in headings and in
individual sentences.**

B's clearest instances:
- dispatch/SKILL.md:1003, a section heading that states the epistemic status of
  everything under it: "## 5. Mechanical guards (global; prose rules are best-effort,
  hooks are not)".
- executor/SKILL.md:171: "Mechanical check: `scripts/check_devbook_form.py <file>` — a
  per-element presence detector with evidence lines; PASS requires all five. It is a
  detector, not the definition: the list above is normative, the script finds the loud
  absences cheaply."
- begehung/SKILL.md:230: "it grades cells against `templates/schema.json`, never the
  judgment behind them, so its green is "well-formed", never "well-reviewed"."
- statiker/SKILL.md:55-58: "The two scripts plus their red-first battery … are the
  EXECUTABLE SPEC of the record grammar … a divergence is graded against the battery,
  never against this page's wording."
- statiker/SKILL.md:535-537, the unenforced case named as such: "The PRECEDENT LINE …
  carries no lint class yet — unread by any mechanized check, the design record and the
  brief are its only enforcement."

A theorizes the same split without applying the label to itself.
principle-encode-lessons-in-structure/SKILL.md:11: "Textual instructions are easy to
miss. They require the reader to notice, remember, and comply. Structural mechanisms
(lint rules, metadata flags, runtime checks, automation scripts) enforce the rule
without cooperation." The file ships none and does not say which of its own clauses are
therefore hoped — though line 17 concedes the judgment case ("If no (requires
judgment), make the instruction more prominent and add an example of the failure
mode"). Its enforcement ladder at line 19 is a near-exact match for
skill-craft/SKILL.md:296-300's preference order, written more compactly: "choose the
strongest the situation allows (an unrepresentable state that cannot compile, then a
lint or banned API that fails CI, then a canonical helper, then a runtime check),
because agents copy whatever the surrounding code already does and a weaker guard
becomes the next template."

Where A is strong: it defines what does NOT count as evidence, in the consumer's own
vocabulary. shipping.md:7: "Each returns `PASS`, `PASS+NOTES` or `FAIL` and posts that
verdict on its own PR. Safe means a verdict from an agent that did not write the code.
CI green is not a verdict, and an approving bot review is not a verdict."

## 3. Evidence-carrying

**Verdict: B by an order of magnitude on density, and B's rules routinely carry the
incident that minted them; A's sampled rules assert bare while DEMANDING evidence
labels from their consumer.**

Density (per 100 body lines, markers as defined above): A 0.0–2.1, B 1.1–8.0. Dates
(`yyyy-mm-dd`) in the text: A 0 across all five files; B 6 across the six.

A's asymmetry, quotable in one line — poteto-mode/SKILL.md:107: "**Every claim carries
its evidence or its label in the same sentence.** Measured, inferred, or guess. A
prediction or an unseen cause is a guess. Never hand the human a check you could run."
That rule binds the agent's replies. The skill's own rules are not written to it: the
only other marker hit in poteto-mode is the word "measured" inside a playbook
description (line 123).

B's shape, four samples:
- dispatch/SKILL.md:52-56: "Core finding (measured in operation, restamped 2026-08-02:
  dispatch-log counts 183 dispatches over six days … every recorded failure traces to a
  brief defect, none to tier capacity…)".
- dispatch/SKILL.md:199-202: "(measured: a 270-line hook rewrite on the remote before
  the dispatcher had verified any of it)".
- kaemmung/SKILL.md:45-47: "a presence predicate fires on the move itself (first trial:
  44 false fires on the legitimate move)".
- statiker/SKILL.md:1253-1256: "Mechanically enforced at the RE-ENTRY seam (F143: the
  prose held IN FORCE while UNAPPLIED — A8's four record/instrument-class findings
  sustained a ninth round this clause forbids)".
- begehung/SKILL.md:15-21 names a founding incident with date and source repo, and
  states the mechanic the skill exploits rather than only the rule.

Two honest discounts on B's lead. First, much of B's provenance points at files the
consumer cannot open — "dev-notes/OBSERVATIONS.md in the source repo" (begehung:16,
kaemmung:100, statiker:16) — so at read time the citation is a promise, not a check;
skill-craft/SKILL.md:311-318 explicitly designs it that way ("a write target, never a
read dependency"), which makes it a deliberate cost, not an oversight. Second, A's
shipping.md is a procedure whose steps are executable commands; a step that is a command
falsifies itself on running, so its zero evidence-marker count understates it.

## 4. Voice and register

**Verdict: A is short, imperative and second-person; B is long, declarative and
clause-packed. Measured on words per sentence: A 7.9–18.7, B 21.0–48.2. Each side
violates one of skill-craft's stated form rules — A the imperative-form rule, B the
sentence-density rules it has no equivalent of.**

A's register is set by its own shipped rule. unslop/SKILL.md:63: "**Shorten or split
dense sentences.** If the reader has to backtrack to parse a sentence, break it in two
or drop clauses. One idea per sentence." And unslop:68: "**Over-compression.** Dropped
articles, verbless fragments, symbol-speak, and abbreviations that make the reader
decode instead of read. "Parser rejects bad date → exit 2, no write" becomes "The
parser rejects a bad date, exits with code 2, and writes nothing.""

Compliance inside side A is high but not total: em dashes are banned outright
(unslop:37, "**Em dash overuse.** Avoid em dashes entirely") and 4 of 5 files carry
zero, while create-verification-skill/SKILL.md carries 5 (lines 3, 17, 25, 28, 40 —
e.g. line 28 "one read-only check that answers "is this instance worth driving?" —
process up, right version/build, port owned by us, auth valid"). poteto-mode uses 18
`→` arrows, which unslop:68 tells the writer to spell out; the router's own compression
is exempted nowhere in the text.

A addresses the reader in the second person, which skill-craft/SKILL.md:245-247
forbids ("Write skill content verb-first, not second person"): poteto-mode:95 "You own
every subagent's work. Review the diff and write your own summary, don't pass through
what it said."

B's register is the evidence register skill-craft/SKILL.md:203-207 prescribes for
top-tier consumers, and the cost lands in sentence length. Representative, measured:
statiker/SKILL.md:556-571 is a single 157-word sentence:
"Beside the write-set declarator: a correction appended under a write-set declarator's
own id, whose latest EARLIER line for that id is a live `unit U<k> write-set: <path>`
declaration, is refused (hold: `declarator-bookkeeping`) UNLESS the correcting line is
itself a fresh `unit U<k> write-set: <path>` redeclaration BY THE SAME UNIT; why: …".
The comparable A specimen is shipping.md:9 at 93 words, but it is four sentences, and
the first is a bolded imperative handle ("**Re-check that each verdict still describes
the patch.**").

Emphasis habits: B leans on ALL-CAPS as an in-sentence highlighter — statiker 43.8
caps-words per 1000 words, dispatch 28.9 — where A uses bold lead-ins and short
sentences (poteto-mode 5.0, unslop 2.3). A's caps are nearly all machine tokens (PASS,
FAIL, MERGED); B's are largely emphasis on ordinary words (NEVER, ONLY, LANDED).

Formatting: A uses numbered playbook steps, bullets, backticked commands, no tables, no
fenced blocks in the sampled files. B uses one table (begehung:37 and :52, the MAP
schema rows) and indented paste-blocks (statiker:1042-1067, dispatch:696-746). Neither
side uses emoji or title-case headings.

## 5. Structure and loading

**Verdict: A is a router plus small leaves; B is mixed, with two right-sized files
(kaemmung 103, executor 199), one with a real section map (dispatch), and one monolith
(statiker, 1713 operational lines, no section map).**

A's loading model is stated as procedure, not architecture — poteto-mode/SKILL.md:117:
"Open a todolist whose first items are the matched playbook's steps, copied in verbatim,
before any task-specific todos. A step you choose not to do stays in the list with a
one-line `skip: <reason>`. Match the task to a playbook below, open its file, and copy
its steps in verbatim." The always-loaded unit is the 143-line router; the working unit
is router + one playbook (shipping.md: 17 lines). The principle list (poteto-mode:41-77)
is 30-odd one-line pointers, each naming its own firing condition, with a read rule at
line 39: "Read the leaf skill in full for any principle you apply."

B's best instance is dispatch/SKILL.md:34-50, a section map that also states load
order: "§2 report form + brief tails: `references/forms.md` — load it BEFORE composing
any brief (the tails are pasted, never recalled)." It also warns where a citation
resolves — ":34-37, "a "§2" citation anywhere resolves in that file, not in this one"".

B's worst instance against its own standard is statiker: 1713 operational lines, no
section map, two reference deferrals. skill-craft/SKILL.md:104-106 states the ladder
test: "its test is branching: inline what every branch of the skill's use needs;
disclose what only some branches reach." statiker's per-verdict implementation
dispositions (lines 1490-1580: UNIT_COLLISION, HALT_IGNORED_WRITESET,
UNIT_COMMITTED_EXTRAS, BLOCKED_CONTENTION triage, the clearing-by-shape recipe) reach
only the implement branch, yet load on every invocation, including a run that closes
FAILED at preflight (statiker:199-203). The file names the debt itself at :1804-1808:
"~150 operational lines is the stabilization TARGET, not the live count: this phase
accretes fire-born structure above it deliberately, and the compression pass owed at
stabilization (booked in dev-notes) brings it back down."

## 6. Machine tokens

**Verdict: B is far more rigorous and more self-describing; A gets a large fraction of
the benefit from one sentence. Both sides use closed verdict vocabularies where a
verdict exists.**

A:
- unslop/SKILL.md:19 — the cheapest good idea in the whole sample: "Rule numbers are
  stable ids that other skills cite. A removed rule leaves a gap." The file honors it
  visibly: the numbering runs 3, 5, 7–20, 22–33; ids 1, 2, 4, 6 and 21 are absent, so a
  retired rule is legible as a gap rather than a renumbering. poteto-mode:103 cites
  across files by that id ("A colon as a mid-sentence connector is also out (unslop rule
  14)").
- shipping.md:7 fixes a three-member verdict vocabulary (`PASS`, `PASS+NOTES`, `FAIL`)
  and :14 reads host state by literal field name: "poll `gh pr view <pr> --json
  state,mergedAt,mergeStateStatus,statusCheckRollup,autoMergeRequest` after each wake,
  ignoring `READY` until `mergedAt` is non-null or `state` is `MERGED`."
- poteto-mode:117's `skip: <reason>` is a self-describing output token.

B:
- statiker/SKILL.md:513-531 declares the token set and its parsing discipline: "The
  record's machine tokens are CASE-SENSITIVE LITERALS, not phrasing: the entry head
  `- <C><n> `, the scope openers `unit U<k> ` and `record: `, the hold form `unit U<k>
  held: ` (that exact prefix as the body's opening — a hold written any other way holds
  nothing)…".
- statiker:115-181 is an eight-token closed route vocabulary with a fail-closed
  unlisted member — :172-176: "a verdict name the registry lacks stamps `route:
  "unrouted"`. A verdict whose `route` field is absent, unknown, or `unrouted` is a HALT
  for the seam that ran it".
- begehung:115 fixes a six-column TSV findings schema with per-cell closed
  vocabularies, and :100-102 states the coupling to the checker: "The checker recognizes
  the two owed rows by the token `templates/schema.json` names for each, so a row worded
  otherwise is reported missing until that token is updated."
- dispatch:975 "`REPORT-CHANNEL: SendMessage <name|operator-terminal>`"; executor:96
  "`git commit -m "…" -- <paths>`, every flag BEFORE the `--`".

## 7. Self-falsification — does the rule name the artifact whose absence proves it was skipped?

**Verdict: both sides do this deliberately; B names the failure mode more often, A
achieves it more cheaply. This is the axis where the two traditions are closest.**

A:
- poteto-mode:15 — "In your reply, name each principle that shaped a decision and the
  specific choice it changed. Cite only principles whose leaf SKILL.md you read this
  session." The reply is the artifact; an unread principle cannot be cited.
- poteto-mode:117 — "A step you choose not to do stays in the list with a one-line
  `skip: <reason>`." The omission is rendered, not silent.
- create-verification-skill:40 — "Run its own instructions end to end once … After
  cleanup, confirm the evidence still exists at the named location — a cleanup that eats
  the proof fails this step. … A generated skill that was never executed is a draft, not
  a deliverable."
- shipping.md:9 — the recorded `patch-id` is the token that proves the verdict still
  describes the patch: "Never use matching commit messages or a green check from an
  older SHA as a substitute."

B:
- executor:47-53, the strongest specimen on either side: "Finding nothing is an answer
  and gets written out ("every line opened, no contradiction found"); silence is not,
  which is the point — an omitted critique is visible in the lane's first message, where
  a private reading that never happened is not."
- executor:134-141 states the principle generally: "Every obligation renders as a
  visible artifact whose absence is loud: mandatory sections where "none" must be
  written out, closed lists that make omissions enumerable…".
- dispatch:455-464 applies it to a single word: ""none" written without opening the
  hooks path reads exactly like "none" written after opening it, so the word alone is
  satisfiable whether or not the work happened".
- begehung:138-142: "An empty `disposition` fails the checker at close, and that failure
  IS the round's own open finding".
- statiker:1464-1467: "a unit whose record cites the git tool's UNIT_COMMITTED verdict
  with no landing line anywhere in the tracker surfaces as a sweep hold
  (`landing-missing`), attribution never left to a later reconstruction."
- skill-craft:285-292 is the general statement B's others instantiate: "the check's
  evidence is an **un-fakeable artifact** — one that cannot be produced without doing
  the work the check represents."

B also marks its unfalsifiable clauses rather than hiding them: statiker tags 15+
clauses `(hypothesis)` and explains the class at :1793-1799, matching
skill-craft:355-359's two-paths rule ("the rule is a hypothesis, valid only when
explicitly marked as one").

---

## (i) Three side-A habits worth importing into side B

1. **The router IS the always-loaded unit; bodies are opened on match.**
   poteto-mode/SKILL.md:117: "Match the task to a playbook below, open its file, and
   copy its steps in verbatim." Cost of importing: statiker and dispatch would each
   split into a router page plus branch files, which turns dozens of intra-page
   references ("The record, Budget"; "The attack, "That closes design"") into
   cross-file pointers that can rot silently, and adds one read per branch at run time.
   The honest version of the import is narrow: move the branch-only material (statiker's
   implement-phase verdict dispositions) behind a pointer, keep the rest.

2. **Stable numbered rule ids, gaps preserved.** unslop/SKILL.md:19: "Rule numbers are
   stable ids that other skills cite. A removed rule leaves a gap." Cost: near zero to
   state, real but one-time to retrofit — ids minted across ~4000 lines of side-B text
   and every internal citation rewritten once. The payoff is specific to side B's
   problem: its cross-references are phrases ("the tag-literal rule", "the drop-argument
   rule's hop"), which no grep verifies, and a renamed clause breaks them silently.

3. **A shipped sentence-density rule the author is also bound by.** unslop/SKILL.md:63:
   "If the reader has to backtrack to parse a sentence, break it in two or drop
   clauses." Measured gap: A 7.9–18.7 words/sentence against B 21.0–48.2, and one
   157-word sentence at statiker:556-571. Cost: this is the expensive import, because
   side B's clause-packing is load-bearing — a dropped qualifier widens a rule — so
   splitting buys readability in LINES, the budget statiker is already 11.4× over. The
   importable half is the compose-time question, not a blanket split: does this sentence
   force a re-read, and is the qualifier that makes it long actually changing behavior?

## (ii) Three side-B habits absent from the side-A sample

1. **The rule carries the incident that minted it.** dispatch:199-202 "(measured: a
   270-line hook rewrite on the remote before the dispatcher had verified any of it)";
   statiker:1253-1256 "(F143: the prose held IN FORCE while UNAPPLIED …)". Side A's five
   files carry zero dates and no provenance clause for any of their own rules, while
   poteto-mode:107 demands exactly that labelling from the consumer.

2. **Saying which half is mechanical and which is hoped.** dispatch:1003 "prose rules
   are best-effort, hooks are not"; executor:171 "It is a detector, not the definition";
   begehung:230 "its green is "well-formed", never "well-reviewed"". The side-A sample
   never applies the distinction to its own text, though
   principle-encode-lessons-in-structure:11 states the theory behind it.

3. **A declared consumer that sets prescription density.** executor:8-11: "Consumer: the
   executing session — commonly a tier below the dispatcher, which is why §1 runs as
   numbered directives and §2 demands visible artifacts rather than principles alone."
   Side A names models per ROLE (poteto-mode:93, code vs prose/judgment defaults) — a
   routing fact — but never says which reader its prose density is calibrated for.

## (iii) Where side B violates skill-craft's own stated criteria

1. **Consumer declared without the as-of stamp — 5 of 6 files.**
   skill-craft/SKILL.md:33-37: "Declare the consumer — the model or tier range that will
   execute the skill — in the skill's opening, with an as-of stamp naming the model era
   the declaration was last graded against (the binding staleness discipline applied to
   the declaration itself; the era re-grade diffs against this stamp)". Measured: "as
   of" occurs once in skill-craft (its own birth declaration, :18 "graded as of the
   Claude 5 era, 2026-08"), twice in dispatch (both harness bindings at :96 and :774,
   neither on the consumer line), and zero times in executor, begehung, kaemmung and
   statiker. Unstamped declarations: begehung:10 "Consumer: a top-tier session model";
   kaemmung:11 "Consumer: a top-tier session model for the diagnosis"; statiker:630
   "intended consumer a top-tier session model (prescription density calibrated to
   it)"; executor:8; dispatch:8.

2. **The information-hierarchy ladder, against statiker's 1713-line single body.**
   skill-craft:104-106: "inline what every branch of the skill's use needs; disclose
   what only some branches reach. Push too little down and the top bloats". statiker
   inlines material only the implement branch reaches (:1490-1580) and the verify branch
   reaches (:1582-1687) into a page every run loads at invocation. The skill records the
   debt (:1804-1808) but the pointer discipline skill-craft prescribes is not applied.

3. **Always-loaded pointers carrying body identity and one-branch synonyms.**
   skill-craft:80-82: "one trigger per genuinely distinct branch — synonyms renaming one
   branch are one branch written twice; cut identity the body already carries. An
   always-loaded pointer earns harder pruning than any body." Against it: begehung:3
   packs four body mechanisms into the description ("lens pre-registered per round,
   per-lens yield stop, darkest-corner rotation, no global done-claim"); kaemmung:3
   spells one branch five ways. Side-B descriptions average 499 chars against side A's
   178.

4. **One-meaning-one-home, in dispatch and executor.** skill-craft:167-169: "One
   meaning, one home — a single source of truth per behavior, so changing it is a
   one-place edit." The pathspec-commit mechanics appear twice, at dispatch:206-216 and
   again at executor:96-107 ("never `git add` then `git commit`, never `-A`: the INDEX
   is shared…"), each with its own wording of the index hazard. Both files label the
   duplication as a deliberate mirror with a source label ("source: dispatch skill §1"),
   which is the amendment-discipline mitigation skill-craft:399-405 describes, not an
   exemption from the rule; a change to the mechanics is a two-place edit in two
   separately released files.

Applying the same standard to side A, one violation is quotable: skill-craft:245-247
("Write skill content verb-first, not second person") against poteto-mode:95 "You own
every subagent's work." Side A's own standard is different (unslop does not forbid
second person), so this is skill-craft's criterion reaching outside its stack, noted
because the brief asked for both sides graded against it.

## (iv) Sampling caveat — what this 5-vs-6 sample cannot support

- **Nothing here is a behaviour measurement.** Every verdict is a read of text. No
  triggering eval, no ablation, no run was performed on either side; "over-trigger
  risk as written" means as written, not as observed.
- **Side A's sample is one plugin's delisted skills.** All five carry
  `disable-model-invocation: true`, so the sample contains no pstack description written
  to be router-matched. The axis-1 contrast (short A descriptions vs long B
  descriptions) may therefore be an artifact of which files were selected rather than a
  house difference; a pstack model-invoked skill, if one exists, is unread.
- **Side A's leaves are unread.** poteto-mode cites roughly 30 leaf principle skills and
  20+ playbooks; I read one of each (principle-encode-lessons-in-structure,
  shipping.md). "The side-A sample carries no provenance clauses" is scoped to these
  five files; poteto-mode:39's instruction to read leaves in full implies bodies whose
  evidence density I cannot speak to.
- **Side B's disclosed tier is unread.** No references/ file was opened —
  dispatch's forms.md and routing.md, skill-craft's enforcement.md,
  review-checklist.md, evaluation.md, anti-patterns.md, begehung's templates/. Claims
  about B's progressive disclosure are about the POINTERS. Likewise, the skill-craft
  criteria graded against are only those stated in its SKILL.md; a criterion that
  SKILL.md defers to a reference may qualify or reverse a finding above.
- **Two side-A files are 17 and 31 lines.** Per-file ratios (words/sentence, markers per
  100 lines) are noisy at that size; the A/B separations reported are large relative to
  that noise, but a single-file A figure should not be quoted alone.
- **Version-pinned.** dispatch-guards 0.11.14, begehung 0.3.3, kaemmung 0.1.2,
  skill-craft 2.2.4, statiker at working-tree HEAD in
  /home/g/dev/Gunther-Schulz/statiker. pstack read at
  /home/g/dev/reference/cursor-plugins commit 7366ac1 (2026-09-09).

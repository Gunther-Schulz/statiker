# opus-st32-clause-table — st-32 lap B stage 1: the per-clause disposition table

Title: opus: st-32 lap B stage 1 — disposition the 28 lap-B rows
Working copy: `/home/g/dev/Gunther-Schulz/statiker`.
Base check: base commit `3c041e5`, **or any later HEAD** — you write
ONE file nobody else touches, and you read the page at a PINNED sha,
not live (below). Run `git merge-base --is-ancestor 3c041e5 HEAD`; not
contained → halt and report.
Scratch: your OWN scratchpad. Slug every scratch file `st32tab`.

**Read the page from the pin, never from the working tree.** A sonnet
lane (`sonnet-st32-registry`) is writing `SKILL.md` concurrently. Take
your object once:
`git show 3c041e5:plugin/skills/statiker/SKILL.md > <your scratch>/page.md`
and work from that copy. Every line number you emit is a line number in
THAT file, and your output states the sha it is anchored to.

## Grounding basis — read before working; the report cites what was
## actually read

- the executor skill (`dispatch-guards:executor`) — load FIRST.
- `docs/directives/2026-09-12-st32-lapB-design-statiker-a5.md` — the
  graded lap B design. §1 (the eight route tokens, each with its
  meaning), §3 (the full 76-verdict mapping), §4 (the seven verdicts
  whose page routing no single token captures), §6 (what the design
  expects to leave and to stay). This is the settled design; you
  disposition clauses against it, you do not re-open it.
- `docs/directives/2026-09-11-st29-lapA-clause-table.md` — lap A's
  table. **Its 28 rows whose final mark cell is `B` are your object**
  (156 clause data rows; the `B` mark means "lap-B routing mass",
  which lap A either kept or tightened — Background 1 and 2). Read its
  "Rules applied" header in full: your table is
  the same instrument one lap later and keeps its column discipline.
- `dev-notes/OBSERVATIONS.md`, the section `## 2026-09-11 — st-29 lap
  A stage 1: clause table graded` — how the desk graded that table,
  i.e. how yours will be graded.

## Background (established; verify at the cited lines)

1. Lap A's table: 196 lines start `|`, of which 13 are separators and
   13 are header rows → 170; the lane's read subtracts 14 per-section
   SUMMARY rows → **156 clause data rows**. Exactly **28** carry `B`
   as their final mark cell. (CORRECTED 2026-09-12 after the lane's
   critique: this brief first said "183 data rows", which counted the
   13 header rows as data. Re-measured by the dispatcher — 196/13/13
   confirmed; the 28 is unaffected and was independently confirmed.)
2. Of those 28, lap A dispositioned **15 TIGHTEN and 13 KEEP**
   (dispatcher-verified). So "lap-B routing masses lap A did not
   touch" is true of 13 only: for the 15 TIGHTEN rows the body at
   `3c041e5` is lap A's REWRITTEN text, and those rows' must-survive
   cells are a spec of what lap A intended, not a description of your
   object. Disposition against the PINNED PAGE TEXT, and flag any row
   whose handle no longer resolves.
3. **Lap A's ranges and the design's are stale by DIFFERENT amounts,
   and lap A's are stale non-uniformly.** Operational counts,
   dispatcher-measured: `769e7f2` (lap A's pin) 1766, `0775b92` (the
   design's base) 1628, `3c041e5` (your pin) 1638. So the design's
   ranges are off by +10, while lap A's are off by the whole lap A
   compression — **−128 operational, distributed per row, not
   uniform**. Re-anchoring by quoted handle is therefore the only
   usable method for lap A rows, not hygiene. (Corroborating spot
   check: the design's "lock routes :799-864" lands on `(b) The
   judgment instrument the tool cannot run` at `3c041e5`, while the
   lock-route content sits at `:809`.) Report the resolved range
   beside the stale one.
4. The design's §6 span figures are per-span APPROXIMATIONS
   ("approximately 22 (tools) + 54 (lock) + 60 (unit) …"), not a
   per-clause enumeration. That absence is why this stage exists —
   your table is what makes stage 2 executable.
5. The parity rule lap A worked under ("no verdict token leaves the
   page") is exactly what lap B REPLACES: the new contract keeps
   page-named ⊆ emitted (design §5 test 5) but drops the requirement
   that every emitted verdict be named on the page. So a token
   LEAVING the page is now legal — and is the point. Each row records
   which tokens it drops.

## The settled design — disposition exactly this, do not redesign

For each of the 28 `B` rows, emit one table row with these columns:

| col | content |
|---|---|
| `id` | lap A's row id, verbatim |
| `anchor` | the quoted opening text you re-anchored on (lap A's `handle` column — its ≤12 opening words, whitespace-normalised) |
| `range@3c041e5` | the resolved line range in the pinned page |
| `stale-range@769e7f2` | lap A's range, for the audit trail — a 769e7f2 number by construction, which is why the column carries its sha (corrected after the lane's critique: it contradicted "every line number you emit is a line number in the pinned file") |
| `disposition` | `PRECIPITATES` / `KEEPS` / `SPLIT` |
| `leaves` | for PRECIPITATES/SPLIT: the clause text that leaves the page, and its OTHER HOME named — the registry entry (`ROUTES["<VERDICT>"] == <token>`) or a named tool check. A row whose load has no other home is a KEEPS row, whatever its size |
| `stays` | for KEEPS/SPLIT: the target text that remains, as PRINCIPLE + VOCABULARY, with a target line count |
| `tokens-dropped` | verdict names this row removes from the page |
| `tokens-kept` | verdict names this row keeps on the page, and why the page still needs each (a §4 seam sentence, a template, a catch-all) |
| `basis` | the design section that decides it (§1/§3/§4/§6), or your reason where the design is silent |

**Dispositions, defined.**
- `PRECIPITATES` — the clause is per-verdict routing whose content the
  registry now carries: reading the registry answers what the clause
  answered. The `leaves` cell must name that registry entry.
- `KEEPS` — the clause states a principle, a write-side template, a
  judgment the tool cannot make, or one of design §4's seven
  seam-dependent routings. Design §6's KEEP list is authoritative for
  its named classes.
- `SPLIT` — both, with both halves quoted separately.

**The rule that decides the hard rows:** a clause leaves only if a
reader of the registry plus the page's remaining principle would reach
the SAME conduct. Where the clause carries a seam- or mode-dependent
disposition the route token cannot express (design §4's class), it
KEEPS — the token carries the fail-closed default and the sentence
carries the modulation. When in doubt, KEEPS: a wrongly-kept line
costs lines, a wrongly-dropped one costs conduct.

**Totals row, mandatory:** non-blank lines leaving, staying, and the
net against the pinned page's operational count.

**And a span-vs-row COVERAGE MAP beside it** (added 2026-09-12 on the
lane's critique, which was right): the design's ~230 is a sum over
eight hand-drawn SPANS at a third sha, while your partition is lap A's
28 rows — a different partition of a different object. Compared
without a shared coordinate that is could-not-verify, never agreement.
So emit the map: which §6 span each of your rows falls in, and any §6
leaving mass with NO `B` row covering it, reported as a gap. A
material divergence from the design's estimate is then a FINDING about
the estimate, reported as such, never a reason to bend the
dispositions.

## Write boundaries

You write exactly ONE file:
`docs/audits/2026-09-12-st32-lapB-clause-dispositions.md`
(`git add -N` it first, then
`git commit -m "…" -- docs/audits/2026-09-12-st32-lapB-clause-dispositions.md`;
every flag before the `--`; never `git add` then `git commit`, never
`-A`, never `--amend`). You edit NO page, NO script, NO test, NO item
carrier. Commits UNPUSHED.

Shared copy: a sonnet lane holds `SKILL.md`, `statiker_emit.py`,
`statiker_record.py`, `statiker_git.py` and the three test files. You
read `SKILL.md` from the pin, so its live state cannot reach your
table.

Commit plan: no payload paths in your write set, so the payload-version
guard cannot fire. No other commit-blocking guard applies (hooks path
read at brief time: the global pre-commit, payload-only).
Trailer: `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`

## Verifier (in the report)

1. Row count: 28 in, 28 out — every lap-A `B` row dispositioned, none
   added. State both counts.
2. Every `PRECIPITATES` and `SPLIT` row names an other-home.
3. Every re-anchored range verified by quoting the pinned page's text
   at the resolved range and showing it matches the anchor.
4. The totals row, with the divergence from the design's ~230 stated.

## Critique pass (one message, BEFORE your first table row)

Which Background line above is wrong or unopened, and which two lines
of this brief contradict each other? Send it on the report channel,
then continue without waiting for a reply.

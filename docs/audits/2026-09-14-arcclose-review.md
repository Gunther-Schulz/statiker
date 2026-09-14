# Arc-close checkpoint review — statiker payload, c4fb687..HEAD (0.2.99)

VERDICT: PIN HOLDS — 1 BLOCKING, 3 SUBSTANTIVE, 5 MINOR.

## Checks I ran (counts, skips dispositioned)

- `python3 -m pytest tools/ -q` at HEAD: **593 passed, 2 subtests passed, 0 failed, 0 SKIPPED**. Matches the stated baseline exactly. No skip found.
- Red-first by mutation, in my own scratchpad (shipped tool files reverted to c4fb687, NEW tests kept):
  - st-63 record tests → 2 failed / 4 passed. The two fix-asserting tests red (`CLOSURE_ABSENT != CLOSURE_LIVE`, `design_amending ['D2']`); all four discriminating controls green. Proper pair.
  - st-55 git tests → 3 failed. `UNIT_COMMITTED_EXTRAS, extras ["abc.txt"]` reproduced verbatim as the docstring claims.
  - test_contract `section_pointers` (old predicate spliced under the new tests) → the false-firing test red as documented; the dedup test GREEN (see M3).
- Pre-fix lock seam measured directly, not inferred: the lock commit landed `.clippy/runs/t.md` + `abc.txt` — the undeclared tracked file DID ride in — then COMMIT_FAILED with `shas`. The docstring's field claim is confirmed by measurement.
- `is_ignored` exemption measured: `check-ignore -q -- ':(literal)abc.txt'` → exit 128 "pathspec magic not supported by this command: 'literal'"; `check-ignore -q -- 'a*.txt'` → exit 1 (not ignored) while `abc.txt` → exit 0 (ignored), i.e. it evaluates the pathname literally and is genuinely outside the vulnerability class. Both comment claims verified. `:(literal)` accepted by status / log / add / commit (probed).
- Route-token enumeration: **25 of 76** registry verdicts are multi-location (24 at 0.2.89). Each token checked against every seam naming it. **No route-token fail-open found.** CLOSURE_ABSENT/CLOSURE_LIVE (`barred`/`proceed`) read as information-not-halt at The record L256 — permitted, because that seam carries the explicit more-permissive sentence the Route vocabulary requires. CLOSURE_VOID (`barred`) reads "bars units" at both L257 and L1326. Tokens are clean; the divergence below is in the page's PREDICATE prose, not in a token.
- Page pointer check at HEAD: found=4, unresolved=0.
- st-62 single-home confirmed: the ecosystem-resolution rule occurs once (SKILL.md), `defaults/models` cites it.

## BLOCKING

**B1. The CLOSURE_VOID scopeless predicate is stated at three page locations; the delta updated none of them.**

Code, `statiker_record.py:2124` — `if scope == "scopeless" and latest[e.id] is e:`

Page, unchanged:
- `SKILL.md:1386-1390` — "The criterion the tool computes — its semantics are what the desk WRITES so the read comes out true: unit U<k> may dispatch when … no F, D, or R line appended after that A-line (post-closure) is SCOPELESS — a scopeless line voids the whole closure". No liveness qualifier.
- `SKILL.md:1326-1328` — "CLOSURE_VOID bars every unit — a scopeless line, or a post-closure [INVALIDATED] line for an entry LIVE at the closure whatever its opener".
- `SKILL.md:1793-1796` (Close) — "a bare `— exported: <ref>` or `— dropped: <reason>` opening reads scopeless and voids the WHOLE closure" — a warning now escapable by a same-id restatement.

Only the design_amending/BIT paragraph (1363-1373) got the new rule. Two directions of harm: the desk cannot find the sanctioned repair (the fix is unreachable from the page), and nothing warns that a later same-id line appended for unrelated bookkeeping silently clears a void the desk meant to keep.

Why blocking rather than substantive: st-63's whole purpose is a sanctioned repair route for a desk; the desk's instruction sheet is the page; the page still forbids the route at the paragraph that governs what the desk writes. The fix ships inert for its own intended consumer — the same "inert until its sibling is fixed" shape the arc recorded on 2026-09-14. The page consistency pass DID run (676a6eb, LEDGER 91) and closed at one site, while that same OBSERVATIONS entry's own lesson — "grep the PREDICATE SHAPE, not the symbol … One cited site is never proof there is only one" — was applied to the code and not to the page.

Repair: carry the 1363-1373 qualifier into 1389 and 1326, and one clause into 1794. Note 1393-1395 already carries a liveness clause for the UNIT branch ("live lines only: an id whose latest line is [INVALIDATED] travels as nothing") — the scopeless branch is the sibling that did not get one.

## SUBSTANTIVE

**S1. tools/test_contract.py — measured reach regression in `section_pointers`. Deleting a whole section is no longer detected.**

Measured on the real page, `## Stop rule` deleted (heading + body, 260 lines):

```
OLD (c4fb687): found=4  unresolved=[('Stop rule', 'Each unit design also carries the PRECEDENT LINE')]
NEW (HEAD):    found=3  unresolved=[]
```

`found` drops silently 4→3 — precisely the failure `test_a_renamed_heading_orphans_its_pointers_into_unresolved` was written to prevent, now re-opened for the delete case while rename stays covered.

Cause: the `>1` phrase-count narrowing cannot separate "target section deleted" (phrase count 1) from "ordinary prose parenthetical" (phrase count 1) — they are identical under the chosen predicate, so the change trades a false-positive class for a false-negative one. The docstring's claim "No second assertion is added and no existing property is dropped" is wider than its stated basis, which covers only the repo's own `(forms at Close, …)` fixture.

Cheapest repair: pin the pointer inventory — assert `found` equals the 4 known pairs — so any drop is loud regardless of which branch lost it.

**S2. The delta's most safety-relevant boundary is unpinned by the battery.**

I probed it; it is correct at HEAD: a post-closure `[INVALIDATED]` of an entry live at the closure still voids unconditionally — the liveness guard does not reach that branch. Three probes, all CLOSURE_VOID:
- premise-kill alone (control)
- premise-kill + same-id `record:` restatement
- premise-kill + same-id `unit U1` restatement

But no assertion in the new class would go red if someone later extended `latest[e.id] is e` to the INVALIDATED branch too — and the arc's own recorded lesson is that the same-shape sibling is what goes unseen. One test closes it.

**S3. C4b mint-record gap, for the releasing desk to disposition.**

`git diff c4fb687..HEAD -- dev-notes/OBSERVATIONS.md | grep '^+##'` returns exactly ONE mint record in the carried set (st-10 C4a, with its nine-tenet check). The repo's release gate mandates the re-ask "over the pin's whole carried set". Two carried changes have no record:

- **st-56** (9eb30c1) adds a new MANDATORY form to the verify carve-out — "Resolution is EXECUTED, never assumed … the dispatching desk checks the pair before the leg's result counts". Structurally identical to C4a, which the SAME commit group ruled a mint and gave a full tenet check ("Precedent line: follows the verify demand list, judged sound"). The asymmetry inside one wave is the tell. I judge this a C4b mint with no record.
- **st-63's page rule** (676a6eb) states a new predicate reading. Genuinely arguable: LEDGER 99 frames it as the record's PRE-EXISTING supersession contract (the st-35 [INVALIDATED] disarm), which would make it a repair restoring stated reach, not a mint. It needs a recorded desk disposition rather than silence — C4b is prose precisely because such boundary calls are the desk's.

(st-62 I judge NOT a mint: relocation, no new token/predicate/form.)

## MINOR

**M1.** `literal_pathspec`'s docstring claims it "closes the class for every call site at once", but `statiker_git.py:1179` — `repo.git("ls-files", "-z", "--", tracker_rel)`, the preflight index-health read — is unwrapped and carries no exemption comment, unlike `is_ignored` (710) and `in_head` (718) which both got one. Measured harmless: `ls-files -z -- 'a*.txt'` exits 0 whether or not the glob matches (it returned `abc.txt` in my probe), and the call reads only the exit code. Documentation reach, not behaviour — but a future auditor finds two documented exemptions and one silent one. One comment closes it.

**M2.** `dry_run_add`'s ADD_FAILED verdict now carries the magic prefix inside its free-text `error` field — measured: `fatal: pathspec ':(literal)nope.txt' did not match any files`. `path=rel` keeps the clean spelling and no handshake field (`--drop`, `extras`, `write_set`) is touched, so the pasted-argument contract is safe. But the desk books the verdict line verbatim into the tracker, so a spelling the desk never typed enters the record — brushing the page's own byte policy (SKILL.md:74-75, "a tool re-spelling a byte mints the second spelling the input rule prevents"). No test pins it either way.

**M3.** `test_generic_pass_dedups_a_dangling_pointer_occurring_twice` does not discriminate — measured green against the pre-fix predicate (the old branch already deduped via `if (name, phrase) in found`). It is a sound regression guard for the new `generic_seen` structure, but its comment ("dedup nit … Dedup fixed alongside") reads as proof of a fix for a defect that did not exist. Re-label, don't remove.

**M4.** C4a's demand population — "every F/D/R line appended after the last resolved A-line" — has no tool-emitted enumeration. `closure` computes exactly that set internally (`post`) but emits only `scopeless` (on VOID) and `amendments` (unit-scoped, on UNIT_DISPATCHABLE); a `record:`-scoped post-closure line lands in no verdict field. The verifier can derive it from the pasted tracker, so it is not invisible — but it is the one demand in that list whose input the page's own standard would put in a verdict ("the tool, never memory or conversation, finds them", SKILL.md:490, said of late INTENT lines). Wording nit alongside: "last resolved A-line" is `sustain`'s vocabulary, while `closure` anchors on `a_lines[-1]`; they coincide in practice but the page uses two phrasings for one anchor.

**M5.** st-62's move narrowed the rule's stated scope from register-wide (it governed every class in `defaults/models`) to the "Attack tier:" paragraph, while the register's own `verify@codex` reasoning (`defaults/models:88-91`) depends on ecosystem resolution applying at the verify class. The verify passage reaches the rule only through a certification-duty cite (SKILL.md:1671-1673), not a resolution cite. No live hazard — there is deliberately no `verify@codex:` entry to resolve — so this is a pointer question only.

## What I did NOT verify

The archived lc-61 real-artifact red-first (44 entries, `.clippy/runs/2026-09-13-lc61-workflow-templates-home.md` under `statiker-run-2026-09-13-lc61-arms/sonnet-ceiling`) sits outside this repo; I did not re-run it. That claim rests on LEDGER 93's desk verification — **read, not executed**. My own red-first is the mutation run above over constructed fixtures plus the three premise-kill probes: it establishes discrimination, not the archived tracker's verdict flip.

## Ship call

B1 alone holds the pin: the tool change is unreachable from the page for its intended consumer, and shipping it that way leaves the desk in the state st-63 was built to end. S3 is the repo's own mandated pre-pin re-ask. S1 and S2 are each a single cheap edit and belong in the same repair lap. None of the MINORs need block.

With B1 repaired, S3 dispositioned, and S1/S2 landed, I would grade the delta ready — the tool work itself (st-55, st-63) is sound, reproduces its named field defects, and its controls discriminate.

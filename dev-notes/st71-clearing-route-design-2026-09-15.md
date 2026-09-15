# st-71 — the owner-less clearing route: DESIGN, 2026-09-15

statiker-81, under the operator's delegation of this date; design
ruling by statiker-9c, same date: **(c) plus narrow (a), (b)
rejected**. Not built. This document is what the build is graded
against.

**LEAD: one clause in `repair_class` makes the owner-less case
terminal. The fix gates that clause on a computed
`defangs` predicate the caller supplies, so a `corrects line <n>`
token clears an owner-less tag literal only when the correcting entry
actually carries the defanged literal. Everything else holds still.**

## 1. What the probe established, and the exact refusal

`tools/st71_clearing_route_probe.py`, instrument proven (positive
control fires, negative control clean). OWNED line: the tool's own
`record: corrects line <n>` token clears the hold, SWEEP_CLEAN.
OWNER-LESS line, the incident shape: the hold stands AND the token
mints a second violation.

The tool's own words for the refusal, read off the run rather than
inferred:

    F1: `corrects line 9` names a violation no repair token reaches
    — hold: an undefanged tag literal here holds the sweep for the
    run's life — write the defanged literal in place; no repair
    token reaches it

Two defects sit in that one message. The refusal is deliberate, and
the remedy it prescribes — *write the defanged literal in place* — is
unavailable, because the tracker is append-only. That is (c): the
message prescribes an act the grammar forbids.

## 2. The site — one clause, one caller

`repair_class` (`statiker_record.py`:717):

```python
if "tag-literal-in-body" in codes and owner is None:
    return "unreachable", REPAIR_INTENT_HOLD
```

`owner` is `line_ids.get(n)`, `None` exactly when the target line
parsed no entry — header, INTENT, or bare prose. One caller,
`apply_supersession`:1451, where the correcting entry `e` and the
target line number `n` are both already in scope. So the signature
extension is local and needs no plumbing.

Two facts that keep the change small, both read at the code:
`tag-literal-in-body` is in `BODY_CONTENT_CODES`, not
`MACHINE_TOKEN_CODES`, so the `supersede` branch never pre-empts this
clause; and `defang_text(text) -> (defanged, names)` (:928) already
exists and already defines the canonical spelling — brackets dropped,
lowercased in place.

## 3. The change

**(a) narrow — extend the EXISTING form's reach, no new address
scheme.** The address stays `corrects line <n>`. Only the clause
above gains a condition:

```python
if ("tag-literal-in-body" in codes and owner is None
        and not defangs):
    return "unreachable", REPAIR_INTENT_HOLD
```

`defangs` is a BOOLEAN the caller computes and passes. Keeping the
text-reading in the caller leaves `repair_class` a pure function of
its arguments, which is what the existing battery tests it as.

**The predicate**, a new helper beside `defang_text` so the spelling
cannot diverge from the one the `quote` verb already uses:

```python
def _correcting_entry_defangs(target_text, correcting_body):
    _, names = defang_text(target_text)
    if not names:
        return False            # nothing to defang; not this case
    _, own = defang_text(correcting_body)
    if own:
        return False            # the "repair" carries its own literal
    low = correcting_body.lower()
    return all(re.search(rf"\b{re.escape(n)}\b", low) for n in names)
```

Three refusals inside it, each deliberate: a target with no literal is
not this case; a correcting entry carrying its own undefanged literal
is not a repair (and fires its own violation independently); and the
match is word-anchored, never a substring, so `pending` is not
satisfied by `pendings` or by `[PENDING]` surviving elsewhere in the
line.

**(c) rides the same change.** `REPAIR_INTENT_HOLD` is rewritten to
prescribe the route that now exists and never the unavailable act.
The message is machine-read-adjacent conduct text, so it goes through
the same review class as the predicate.

## 4. Against the ruling's bar, clause by clause

- **ACTUAL defang verified, never pointer-only.** A bare `corrects
  line <n>` with no defanged literal in its body leaves `defangs`
  False and the hold stands. A pointer-only clear is the (b) the
  ruling rejected, and the predicate is exactly what forbids it.
- **`corrects-nothing` preserved for a line that does not exist.**
  Untouched: `n < e.lineno and n in violated` is evaluated upstream of
  `repair_class` and is not in the change set.
- **Append-only untouched.** The route is an APPENDED entry. Nothing
  edits or deletes.
- **The owned case does not move.** `owner is not None` never reaches
  the clause. Arm F must stay SWEEP_CLEAN.

## 5. Red-first arms, all from the probe's own shapes

RED (the case that must flip):
1. owner-less literal + `corrects line <n>` whose body carries the
   defanged name → today `corrects-nothing` + hold; after, clean.

MUST-NOT-MOVE (each must be unchanged by the repair):
2. owner-less literal + pointer-only token (probe arm H) → stays
   `corrects-nothing`. This is the (b)-in-disguise guard.
3. owner-less literal, no token at all (arm G) → stays SWEEP_HOLDS.
4. owned-line literal + token (arm F) → stays SWEEP_CLEAN.
5. `corrects line <n>` at a line carrying no violation → stays
   `corrects-nothing`.
6. a "defanging" entry that itself carries an undefanged literal →
   does NOT clear, and fires its own `tag-literal-in-body`.

The battery carries all six, and arms G/H keep their exact probe
shapes so the incident is pinned in the test rather than in memory.

## 6. Known reach of the predicate, stated rather than found later

It verifies the DEFANGED LITERAL is present in the correcting entry.
It does not verify the surrounding prose faithfully restates the
offending line — that needs judging prose and is not computable. A
desk could satisfy it with a thin restatement.

Two things bound that, and neither is new laxity. The literal on the
original line SURVIVES either way, because the record is append-only —
which is already true of the OWNED case the tool has always cleared
(arm F clears with the literal still standing). So this route is
exactly as strong as the one already sanctioned next to it, and no
weaker. What it removes is the terminal deadlock, not the duty.

## 7. What this is NOT

Not a declaration honoured where `SWEEP_EXEMPT` is inert. `(b)` was
rejected on the ground that a declaration reaching an unexemptible
code is the silencing `UNEXEMPTIBLE_CODES` exists to forbid, and that
ground is recorded here so the option stays closed. The exemption path
is untouched: `SWEEP_EXEMPT: tag-literal-in-body` remains inert, as
the battery's `test_defang_class_is_never_exemptible` asserts, and
that test must stay green byte-unchanged across the repair.

## 8. C4b and the residue

C4b: MINT, as ruled. It introduces a new MANDATORY FORM — the
defanged restatement as the clearing requirement — even though it
introduces no new token or hold code. Provenance: arm 2's halt
(OBSERVATIONS 2026-09-14) plus the probe record (44c1b12). The full
nine-tenet enumeration lands in OBSERVATIONS before the change does.

Residue this change owes, carried from st-69: SKILL.md:587 and :798
still say the hold stands "for the run's life", which this change
makes false for the owner-less case. Both are in st-71's write-set and
are revised in the same landing, so the page and the tool agree at
every location that names this verdict — the multi-location check the
repo's review instruction names.

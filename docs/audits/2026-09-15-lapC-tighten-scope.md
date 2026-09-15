# Lap C — the tighten-scope decision: measured input and proposal

Author: statiker-4b (opus, executing desk), 2026-09-15, under the
operator's first-hand delegation of this date; statiker-9c driving.
Answers st-33's one open blocker: *which clauses lap C's
conduct-prose tighten actually changes, now that the standard is
readability rather than a line budget (operator Option A,
2026-09-12), with the stage-1 clause table as its measured input.*

**Object — pinned, not live.** `plugin/skills/statiker/SKILL.md` at
`bd9dc83`. 1793 operational lines by the CLAUDE.md Verify awk
[measured]. 16,569 words, 347 sentences [measured].

---

## Lead

**The tighten changes THREE sentences, 273 words — not the 53 a
naive readability scope would take.** The page is not long because
it is badly written. It is long because it is machine semantics,
and of its 53 genuine run-on sentences, **50 carry a machine token,
a flag, or two or more verdict names**. Under the medium tenet
those are not tighten material at all: rewording a predicate is a
MINT (CLAUDE.md C4b), with the provenance bar and full tenet check
binding — not a readability pass.

This is the third independent measurement this arc converging on
one conclusion: the page's mass is irreducible by restructuring
(phase 0's disjointness finding), by re-homing (the stage-1 clause
table's "predicates, templates and seam conduct, none of which
precipitates"), and now by rewording. It reduces only by MECHANISM
— the lever route booked as st-83.

## 1. The instrument, and its agreement check

skill-craft ships `tools/register_lint.py`, which grades a file
against a measured prose-form band. Run over the page [measured]:

```
2 finding(s); 447 em dashes (27.0/1000w); 47.7 words/sentence over 347 sentences
:439  em-dash:          27.0 per 1000w, cap 5.3
:611  sentence-density: file mean 47.7 w/sentence, cap 19.0 (longest here: 229 words)
```

Two file-level aggregates are not a clause list, so the
distribution was computed independently. **Agreement check on a
shared coordinate**: the independent splitter also returns the
longest sentence at **229 words at line 611** — the same value at
the same line the lint reported, so the two measurements compare
rather than merely agree in verdict.

Length distribution [measured]: 1-19w: 72 (20.7%) · 20-39w: 100
(28.8%) · 40-79w: 119 (34.3%) · 80-149w: 49 (14.1%) · 150+w: 7
(2.0%).

## 2. Two subtractions, both of which a naive scope would miss

**(a) List artifacts — 3 of 56.** Both splitters read a bulleted
block with no terminal periods as ONE sentence. The single largest
"sentence" on the page — the 229-word finding at :611, the lint's
own headline — is the **entry-template list** (:611-654), nine
bulleted forms. It is not a run-on and tightening it would damage
the templates. The other two: :644 (102w, the tag/basis rules) and
**:1090 (83w) — inside the attack question block**, which is pasted
VERBATIM into every attack brief (:1077, "pasted, never recalled").
Touching :1090 changes what every attacker receives.

The lint's top finding is therefore a false positive, and a scope
taken from the instrument's own headline would have opened lap C by
rewriting the one block the page forbids rewriting.

**(b) Semantics-bearing run-ons — 50 of the remaining 53.**
Classifier: a sentence counts as semantics-bearing if it contains a
backticked machine token (`- F<n> `, `unit U<k> `, `record: `,
`write-set: `, `corrects`, `SWEEP_EXEMPT`, `INTENT: `, `SKILL: `),
a CLI flag, or two or more ALL-CAPS verdict names.

| | count |
|---|---|
| genuine run-ons (>=80w, artifacts removed) | 53 |
| semantics-bearing | **50** |
| conduct prose | **3** |

By section, the genuine run-ons concentrate exactly where the
machine semantics live: The record 15, The attack 13,
Implementation 9, Stop rule 6, The loop 5, Verify 3, The tools 2.

**Classifier reach, stated because the scope rests on it.** Its
defeat mode: a sentence carrying exactly ONE verdict name and no
backticked token reads as prose. That defeat mode FIRES on one of
the three survivors — see §3.

## 3. The proposed scope: three sentences

| line | words | section | what it is |
|---|---|---|---|
| :995 | 101 | Stop rule | "Everything outside the pathspec is operator state…" — desk conduct, no token |
| :919 | 92 | Stop rule | "(b) The judgment instrument the tool cannot run…" — explicitly the work the tool does NOT do |
| :1147 | 80 | The attack | "Attack tier: a ROLE, resolved in order…" — **boundary case** |

:995 and :919 are clean: both state desk judgment, neither carries
a predicate any gate reads, and both can be split into shorter
sentences with no semantic change — the byte-level check being that
no machine token, verdict name, or flag appears in either before or
after.

**:1147 is a desk judgment call, and I am flagging rather than
deciding it.** The classifier passed it as prose because
`clippy.config/models` is not a machine token by the rule above —
but the sentence states a RESOLUTION ORDER (config class, then the
shipped register, then the strongest available context) that
behaviour depends on. This is the same shape CLAUDE.md records as
C4b's recorded boundary case (e19116d's fail-closed floor: adds no
token name but does add a mandatory form, "whether it fires is a
desk judgment"). RECOMMEND: **exclude :1147** — the resolution
order is behaviour, its re-wording would be a mint rather than a
tighten, and lap C is not a mint lap.

**Net proposed scope: 2 sentences, 193 words** (:995, :919), with
:1147 excluded and recorded as excluded.

## 4. The em-dash cap is NOT chased — recommend declaring a band

The page measures 27.0 em dashes per 1000 words against the tool's
cap of 5.3. The tool states in its own `--band` help that the band
is **a property of the corpus, not of the tool**, and that its
default is pstack-derived.

Chasing a pstack-derived band would be adopting a comparand's house
style as a standard — precisely the NON-STEAL posture PLAN.md
records for this comparand (2026-09-13), and the em-dash idiom here
is the operator corpus's own, not an accident of this page.

RECOMMEND: statiker DECLARES its own band and lints against it at
the invocation, so future runs of this instrument are informative
rather than permanently red. The declared numbers are a decision,
not a measurement, and belong with the operator or the driving
desk — surfaced, not taken.

## 5. What this means for the honest number (st-33's real job)

Option A reframed lap C from reaching a number to recording an
honest one. On this scope the page loses roughly a handful of
lines, so the measured residue at lap C's seam will sit near
today's 1793.

**That number is the finding, not a disappointment.** Its basis for
the PLAN.md supersession entry is now three converging measurements
rather than one: the stage-1 clause table's structural finding; the
phase-0 disjointness finding; and this pass's 50-of-53. The entry
should say what the number MEANS — that 80-150 was unreachable
because the page's mass is machine semantics, which no compression,
split, or rewording reduces, and which only precipitation into
mechanism can — and name st-83 as where that route now lives.

---

## The numbered proposal

**Q6. Which clauses does lap C's tighten change?**
RECOMMEND: **:995 and :919 only** — 2 sentences, 193 words. Basis
§2, §3.

**Q7. Is :1147 in or out?**
RECOMMEND **OUT**, recorded as excluded with its reason (resolution
order is behaviour; re-wording is a mint under C4b, and lap C is
not a mint lap).

**Q8. Are the 50 semantics-bearing run-ons in scope?**
RECOMMEND **NO** — out of bounds under the medium tenet; each would
be a mint with the provenance bar and full tenet check. Not booked
as future work either: their length is the density the medium tenet
prescribes, not a defect.

**Q9. Does lap C chase the em-dash cap?**
RECOMMEND **NO**, and recommend statiker declare its own band
(§4). The band's numbers are a decision — surfaced to the operator
via the driving desk, not set here.

**Q10. What does the PLAN.md Size-target supersession entry say?**
RECOMMEND the number measured at lap C's own seam, with the
three-measurement basis of §5 and a pointer to st-83 as the route
that can still move it.

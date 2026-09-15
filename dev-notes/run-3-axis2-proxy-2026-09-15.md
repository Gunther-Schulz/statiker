# Run 3 — AXIS-2 PRE-CLONE PROXY, and the object proposal, 2026-09-15

statiker-81 executing, under the operator's first-hand delegation of
this date; statiker-9c driving. Ruling authorizing the proxy form and
its three terms: statiker-9c, this date, relayed to this session.

**LEAD: C1 (st-68) FAILS AXIS 2 on this measurement. The withheld
criterion is written, in substance and with a worked example, in the
lifecycle repo's own CODE — in the docstring of the resolver the
correct fix is supposed to reuse. Recommendation: the pick RE-OPENS.**

---

## 0. WHAT THIS IS, AND WHAT IT IS NOT

Axis 2 (reachability from the artifact) is registered as a
FREEZE-GATE sweep of the CONSTRUCTED clone (§5c). The clone is gated
on the pick, so the registered measurement cannot inform the pick it
exists to inform. statiker-9c ruled TAKE THE PROXY on three terms,
all honoured here:

1. Labeled **PRE-CLONE PROXY**, with its reach control beside it and
   its delta from the registered measurement named.
2. The registered freeze-gate sweep against the real clone remains
   the BINDING measurement. This does not replace it.
3. **THE DIVERGENCE CONSEQUENCE, pre-named before the pick:** if the
   freeze sweep contradicts a proxy reading on whichever object is
   picked — reachability appearing in the constructed clone where the
   proxy read absent — that is a STOP back to the driving desk and
   the pick RE-OPENS. It is never absorbed at the freeze gate as a
   narrowing or a declared deviation. Whoever picks, picks knowing
   this re-open condition.

**THE PROXY'S DELTA, stated rather than left to be found.** The
population is the TRACKED files of the object repo at HEAD — the
extent a `git clone --depth 1` carries. It therefore excludes
untracked and ignored files (which the clone also excludes) and it
excludes nothing else. Where it diverges from the registered sweep:
the clone's declared containment scope may differ from the repo's
tracked extent, the clone carries a planted `AGENTS.md` (§4d) that
this population does not, and the clone is post-scrub while this is
pre-scrub. All three differences make the proxy read WIDER than the
clone, never narrower — so a proxy HIT is a candidate for scrubbing,
and only a proxy ZERO would need the freeze sweep to confirm it.

## 1. INSTRUMENT

`scratchpad/axis2_proxy_sweep.py`, executed. Whitespace-normalised,
case-folded substring search over each file's WHOLE BODY, never
line-based: the corpus and these carriers are hard-wrapped, and a
line-based grep is blind to a phrase spanning the wrap. That exact
blindness already produced one false zero on THIS criterion, at
candidates round §A.4's own instrument note — so the instrument is
chosen against a known failure of its predecessor, not by preference.

Keyed on the criterion's SUBSTANCE, never on `lc-48` by name:
equality-of-question matching, near-miss non-discharge.

Controls, both required before any zero counts:

    REACH control   "blocked-by"    484 hits / 20 files   ALIVE
    ABSENCE control nonsense string 0 hits                CLEAN

## 2. C1 — st-68. OBSERVED

Population: 65 tracked files, lifecycle HEAD `2df0307`.

    "question-slot"                 8   verbs.py, refusals.py,
                                        grammar.py, migrate.py,
                                        ITEMS.md, ITEMS-DONE.md,
                                        test_migrate.py
    "exact after a strip"           2   ledger.py, test_lanes.py
    "compared exact"                1   ledger.py
    "near-miss"                     2   ITEMS.md, test_migrate.py
    "different question"           16   6 code files + 4 carriers
    "equals the effective blocker"  1   ITEMS-DONE.md  (lc-48 —
                                        the known positive, present
                                        as §2c says)

**BODIES READ, not classified from the key.**

`plugin/cli/lifecycle_core/ledger.py`:369-375, the `decision_for`
docstring:

> ANCHORED ON THE SLOT, never on the word appearing anywhere in the
> line [...] Compared EXACT after a strip rather than by containment
> — a prefix match here would let "which window" clear "which window
> is canonical", which is a different question with a different
> answer.

`plugin/cli/lifecycle_core/refusals.py`:1119-1120:

> `item ready` resolves the blocker by question-slot equality
> (lc-40, lc-49)

## 3. C1 — DERIVED (marked as such)

**§2c's axis-2 premise is refuted at the body.** §2c states the leak
is CARRIER-borne and not code-borne: "the close path's code does not
expose the equality/near-miss contract. Probed at the code and the
batteries; only unrelated `different question` prose found."

That "unrelated `different question` prose" IS the contract. The
docstring above states question-slot EQUALITY as the rule, names
CONTAINMENT/prefix matching as the rejected looser alternative, and
carries a worked near-miss ("which window" vs "which window is
canonical") — which is §2b's withheld criterion, mechanism and
example both. The earlier probe hit this string and classified it on
the key rather than reading the body. Same shape this program keeps
paying for.

**WHY THIS IS WORSE THAN A CARRIER LEAK, which is the load-bearing
sentence.** §2b's secondary withheld half is that the fix ASKS the
resolver `item ready` already uses. An arm reaching for the correct
fix opens `ledger.py` and reads `decision_for` — that is not
hunting, it is the first act of doing the job right. The criterion is
therefore reachable ON THE CORRECT PATH, and an arm that reaches it
tells us nothing about tier.

**THE SCRUB CANNOT SAVE IT, and this is why I am not proposing one.**
§5c's scrub reaches the carriers. Scrubbing `ledger.py`'s docstring
would delete documentation of the correct contract from the tool the
arm is repairing — which (a) changes the object's own source, so the
packet frozen from the REAL repo (§5a) and the clone stop being the
same object, which is the premise axis 2 itself rests on, and (b)
removes the artifact's statement of correct behaviour, which the
definition-derived rule says is what a wrongness claim is measured
against. A scrub that edits the object under test is not a scrub.

## 4. C2 — st-71. OBSERVED, and the shape differs

Population: 136 tracked files, statiker repo. Reach control 2536
hits, ALIVE; absence control clean.

    "opens on a probe"        4   ITEMS.md, OBSERVATIONS.md,
                                  candidates round, discriminator prereg
    "owner-conditioned"      10   statiker_record.py x2, rest carriers
    "owning line id"          2   ITEMS.md, OBSERVATIONS.md
    "branches on the result"  1   candidates round only
    "supersede the owning"    0
    "clearing route"          8   carriers only

**DERIVED.** The distribution is the finding, not the count. C2's
hits sit almost entirely in this trial's OWN carriers — ITEMS.md,
OBSERVATIONS, the candidates round, the discriminator
pre-registration — none of which ship to an arm and all of which are
scrubbable or excludable by construction. The two CODE hits are
`owner-conditioned` in `statiker_record.py`, which is the MECHANISM
the probe exercises and not the withheld half; the withheld half is
the BRANCH (probe first, and the result decides which of two
different items this is), and its keys return zero in code and
appear only in a trial document.

So on axis 2 the candidates round's ordering INVERTS: C1's leak is
code-borne and unscrubbable, C2's is carrier-borne and scrubbable.

**WHAT DOES NOT CHANGE, and it is why this is a decision and not an
answer:** C2's stated risk stands exactly as the candidates round
wrote it. Its withheld half IS statiker's tenet 1, so a desk running
the skill properly is more likely to reach it, and the ceiling gate
may fire on the column — the run 2 failure mode. C2 is the sharper
SKILL-validation object and the riskier TIER-certification one. Axis
2 improves its standing; it does not dissolve that risk.

## 5. THE PROPOSAL — for the driving desk, numbered

The pick is not mine. Three options, each with what it costs.

1. **RE-OPEN AND TAKE C2 (st-71) as primary.** Buys an object whose
   axis-2 leak is scrubbable by construction. Costs the ceiling-gate
   risk the candidates round already priced, and C2's release event
   ("a disqualifying surprise before freeze") is arguably satisfied
   by this finding — which is the reserve mechanism working as
   designed, not an improvisation.
2. **KEEP C1 AND NARROW THE CLAIM.** Run C1 with axis 2 recorded as
   FAILED and every column's independence reading capped at
   could-not-verify wherever an arm touched `ledger.py`. Honest, and
   it spends a whole run to certify less than the run exists to
   certify. I do not recommend it.
3. **RE-OPEN THE CANDIDATE SET.** Neither C1 nor C2, a fresh
   candidate graded on both axes before freeze. Costs a candidates
   round; buys an object chosen with axis 2 measured FIRST rather
   than discovered at the gate — which is the sequence this finding
   argues the program should have had all along.

**MY RECOMMENDATION: (1), with (3) as the fallback if the driving
desk judges the ceiling-gate risk on C2 disqualifying.** Basis: C2 is
already graded on axis 1 (gap demonstrated, candidates round §2) and
now on axis 2 by the same instrument that just refuted C1, so it is
the only remaining candidate with both axes measured. Option 3 is
strictly better evidence and strictly more cost, and the choice
between them is a spend call, which is the driving desk's.

## 6. TWO FURTHER FINDINGS, unrelated to the object

**6a. §5d's TOOL PRECONDITION IS STALE AND MIS-ATTACHED.** The
paragraph reads "TOOL PRECONDITION ON STEP 7 [...]
`driver_resume_probe.py` currently has no argparse, so it cannot be
aimed at the run's arrangement at all [...] Step 7 is unexecutable
until that repair lands." Both halves are now false:

- The repair LANDED — st-78, this arc's predecessor. Verified at the
  artifact: `tools/driver_resume_probe.py`:87 imports argparse, :312
  builds the parser, :313 is `--launcher-file`, the very flag the
  paragraph names as the sibling's contrasting capability.
- The step number is wrong. §5d step 7 is the LAUNCHER PROBE
  (`launch_substrate_probe.py`, §4c). The tool this paragraph is
  about is consumed at step 10, the DRIVER RE-RUN.

Left unrepaired pending the object decision, because §5d is about to
be re-read by the eve review and a document edit landing under a
review's feet is the stale-object shape. Booked as a finding here;
say the word and it lands.

**6b. lifecycle HEAD HAS MOVED OFF THE PINNED SHA.** §5a pins
`2b41491` and records "lifecycle HEAD was still 2b41491 at the narrow
round". It is now `2df0307` ("lifecycle: amend lc-51"). So §5a's
rebuild branch is LIVE, not hypothetical: a `--depth 1` clone takes
the branch tip and will NOT equal the pin, and step 3's sha verifier
will fire. This is S7's verifier working as designed — the hazard it
was added for has now actually occurred.

The decision it forces is the driving desk's: re-pin the packet to a
fresh HEAD at actual freeze time (nothing is frozen yet, so nothing
is invalidated), or hold `2b41491` and clone at the pinned sha per
§5a's stated branch. Re-pinning touches a pre-registered bound, which
is why I am not doing it.

## 7. WHAT THIS RECORD DOES NOT ESTABLISH

- n=1 per candidate per axis. Unchanged from §6b of the
  pre-registration.
- The proxy is not the registered measurement. §5c still runs.
- Axis 2 was measured for C1 and C2 only. C3 (st-66) is already
  rejected on axis 1 and was not swept.
- No claim about whether an arm WOULD read `ledger.py`. The claim is
  that the criterion sits on the correct fix's path; what an arm
  actually does is what the run measures.

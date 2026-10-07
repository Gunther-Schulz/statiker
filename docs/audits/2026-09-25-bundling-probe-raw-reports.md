# Bundling-probe review 2026-09-25 — the three arms' reports, verbatim

Extracted 2026-10-07 from the lane transcripts of session 2070cc85
(each arm's own SendMessage bodies). Evidence bodies for
dev-notes/bundling-probe-preregistration-2026-09-25.md, addendum.


## opus-review-w

Review arm W (whole delta, ae93661..ce271b7, SKILL.md): 5 BLOCKING, 7 minor. Do not release as-is.

Line numbers are from SKILL.md at ce271b7; the working copy matched it (the diff against ce271b7 was empty). Method: full page read (1–1948), the tool's trend/sustain code read (scripts/statiker_record.py:2439-2640, statiker_emit.py:113-147), and ONE executed probe (planted tracker, described under B4). I did not run the suite. Every other claim below comes from a read. Where a claim is my inference, it is labeled.

BLOCKING

B1. Two things can open closure while the new rules still count a unit as unconverged. The seams are 1295-1301 (CONVERGED and the altitude qualifier) and 1051-1052 (attack clause) on one side, and 1347-1352 (the ZERO-DELTA recordability conditions) plus the closure tool on the other.
- The new prose says a reading round's zero "converges nothing", and that the closing zero-delta round "runs once over the converged set".
- The [ZERO-DELTA] A-line's recordability conditions (1348-1351: substance-free, verdicts reach-matched, no [PENDING]) mention neither per-unit convergence nor a whole-set closing round.
- A zero is not a verdict, so the "unmeasured" label (1111) does not attach to it.
- So (a) a round with no findings that did not execute a unit's mechanism, or (b) a zero from a round aimed only at the last unconverged units, records [ZERO-DELTA] legally. The closure tool reads only the last A-line (1452, 1481), so closure opens. The token fails open at exactly the seam the new rule exists to guard.
- Fix shape: make both conditions part of [ZERO-DELTA]'s recordability sentence at 1347-1351, and name them at the 1352 "That closes design" seam.

B2. The named-absence unit has no convergence route (1052-1055 against 1300-1303).
- A unit whose mechanism "no input can legally reach at design time" only ever gets reading rounds.
- The qualifier says a reading round's zero never converges it, and no other route is named (neither a desk-executed measurement nor an [AUTO-ACCEPTED] carry).
- Strict reading: the unit can never converge, the closing round over "the converged set" never arrives, and the run burns to budget exhaustion.
- Lax reading: the rule is ignored, which is B1.
- Linked minor: "the verify phase's named-absence form" (1055) is a dangling cross-reference. `grep -n -i 'named-absence\|named absence'` finds only 1055 itself. The nearest Verify form is NOT EXERCISED carried as a named [AUTO-ACCEPTED] (1705, 1721-1723), so the record form of the design-time absence is unspecified.

B3. Aiming rounds at a subset contradicts the no-steering rule (1297-1298 against 1131-1135 and the verbatim question block, 1100-1129).
- "Later rounds aim at unconverged units plus cross-unit interactions" needs the brief to tell the attacker where to look. That is desk reasoning, and 1131-1135 forbids it ("steering notes ... frames the round").
- The pasted question block orders a whole-design attack (decomposition, simplicity, blast radius).
- The CONVERGED entries themselves sit in the never-filtered artifact (1037-1039). They tell every later attacker which units are "done", which is steering by a second channel.
- Neither sentence yields, so a desk breaks one of them or skips the aiming. Say how aiming is expressed without steering, or what the attacker sees.

B4. A convergence entry that is an F-line corrupts `trend`'s arithmetic, which the new canary cause reads. EXECUTED probe, pair drawn from the same planted tracker:
- Two rounds: round 1 has 3 findings; round 2 has 1 finding plus 3 lines of the form `- F<n> [VERIFIED] record: unit U<k> converged` landed before the A-line ("rides the same return", 1295).
- Result: `TREND_COMPUTED counts [3, 4], trajectory WORSENING`.
- The same tracker with those 3 lines blanked: `counts [3, 1], trajectory IMPROVING`.
- Cause: statiker_record.py:2513 counts every F-line in the round window, whatever its scope.
Convergence entries are anti-correlated with findings, so they push a genuinely contracting series toward FLAT or WORSENING. The canary passage (401-402) names "the trend verdict for arithmetic" as the cause's discriminating evidence. The page also never says which entry class CONVERGED uses (F or D; D-lines are not counted). Pin the class to one that `trend` does not count, or have `trend` exclude it. Either choice decides the cure.

B5. The raise template has no slot for the cause the new rule demands (396-400 against 408-411 and 419-425; also 372-374).
- The new rule: "a raise never lands without that cause quoted beside it, and one granted causeless is a recorded miss."
- The raise template at 419-421 (`budget raised to ... — "<operator's line>" — basis: operator`) has no cause slot, and neither does the CONTINUE ending at 410 ("an ordinary budget-raise entry").
- The exhaustion check is a body-read of that template (424-425). Parked tool work will parse it, so a cause spliced in at a desk-chosen position produces divergent spellings of a machine-read line.
- The sentence also contradicts itself. "Never lands" reads as the desk refusing to land the entry. "One granted causeless is a recorded miss" reads as it landing anyway. And 413-418 says an operator raise LANDS.
- Open cases a mid-run desk will guess at:
  - a pre-emptive operator raise with no stop report behind it;
  - whether a tripwire-threshold raise (372-374, "the same split") is covered;
  - where the "recorded miss" is written (no entry form, no Close slot).
- The old anchor "owes a named cause at close-out" was deleted and the Close list (1832-1845) has no stop-cause item. So the cause may exist only in a reply, and a raise cannot quote it from the record.
- Fix shape: put the cause slot in the template, state the land-versus-refuse disposition, and give the miss a carrier.

MINOR

m1. The two new clauses define "born" differently.
- The trend clause (1241-1245) counts any "unit, gate or form the repair introduced" as newborn.
- The intake clause (1310-1311) says "new design surface, not a fix inside existing surface" and speaks only of units.
- A repair that adds a gate inside an existing unit is newborn for trend and not an intake. The tool's concentration flag (statiker_record.py:2526-2540) is a third definition: findings citing any D-id revised in the previous re-lock window.
- "That round's repairs" has an unclear referent. Inferred, unverified: the clause catches only the first round after a birth, not the multi-round founding pattern it cites.

m2. A justified join is self-defeating.
- After a legal join (1314), the newborn's first attack drawing findings is non-contracting "however the counts fall" (1243-1245).
- That routes to NARROWING. Where the join reason makes the head minimal, it goes to the operator, or closes the run FAILED unattended (1263-1267).
- Say whether the first post-birth round is exempt, or accept this consequence explicitly.
- Borderline-blocking; graded minor because it fires only from the second graded repeat round on.

m3. Exporting a newborn unit bypasses the narrowing machinery (1311-1314 against 1254-1262).
- The newborn typically repairs a finding. Exporting it leaves that finding and the R-line it serves unrepaired.
- The narrowing export requires an R-amendment, a backlog carrier and a reconciliation riding the close. The intake export states none of these, which makes it a silent narrowing.
- "The re-lock entry" is undefined (grep: 1311 only). A re-lock is a commit, so the mandatory join-or-export answer has no named carrier.
- Borderline-blocking because export is the stated DEFAULT late in a run.

m4. The canary passage contradicts itself.
- "A cause report is a READ, not a composition" (404-405) is kept.
- The new mandate adds "the generalization it implies (which design change makes the class not recur)" (397-398), which can only be composed.
- "Design change" is ambiguous: the run's design (a desk redesigning inside an operator-owned stop) or the skill's structure (the mint source).

m5. The attack-brief clause has several soft spots (1046-1055).
- Eligibility is "real or planted input", but the probe's input must be "drawn from the source ... rather than built" to the design's assumption. Planted input is built input.
- "No input can legally reach" is an unchecked escape hatch, since planted input can almost always reach a predicate.
- "One executed probe": per round or once? The qualifier needs it every round.
- It does not say whether a desk-executed measurement (1291-1293) can converge a unit, or only an attack round.
- Execution against "the source the mechanism will face" (live data) is not tied to the read-only tail or to the by-product `paths` declaration (1736-1744, 1758-1760).

m6. The new clause's boundary disagrees with the verbatim question block.
- The block allows "a full source-chain trace ... where it is still design prose" (1106-1107).
- The new clause demands execution for anything "runnable ... at design time". A predicate or query written in a D-line is both.
- The named probe likely wins in practice, but the page does not say so.

m7. The CONVERGED and REOPENS forms are underspecified, and the insertion breaks an existing sentence.
- Neither form gives an entry class, tag or literal, so a resume finds converged units only by free-text body-read.
- A cross-unit finding: does it reopen both units?
- "Near it" (1314) is undefined.
- Editorial: the 1046 insertion separates "Unfiltered, the artifact compounds per round" (1057) from the filter paragraph it continues.

Not a page defect, for the release gate: all five changes introduce mandatory forms, so they are C4b mints. OBSERVATIONS.md carries tenet-check sections for this batch (lines 12618ff and 12706ff); I did not grade those records.

Not run: the pytest suite, and any probe of `sustain` or `closure` on convergence entries. B1 rests on the page's recordability text plus the closure tool's documented last-A-line read (1452, 1481), not on an executed closure run.
(1/4) Review arm W (whole delta, ae93661..ce271b7): 5 BLOCKING, 7 minor. Do not release as-is.

Line numbers are from SKILL.md at ce271b7 (working copy identical). Method: full page read, the trend/sustain code read (statiker_record.py:2439-2640, statiker_emit.py:113-147), ONE executed probe (under B4). Suite not run.

B1 BLOCKING. Closure can open while units are formally unconverged. The seams: 1295-1301 and 1051-1052 against 1347-1352 and the closure tool.
- New prose: a reading round's zero "converges nothing"; the closing zero-delta round "runs once over the converged set".
- The [ZERO-DELTA] recordability conditions (1348-1351) mention neither per-unit convergence nor a whole-set closing round. A zero is not a verdict, so the "unmeasured" label (1111) does not attach.
- So (a) a round with no findings that did not execute a unit's mechanism, or (b) a zero from a round aimed at a subset, records [ZERO-DELTA] legally.
- Closure reads only the last A-line (1452, 1481), so it opens. The token fails open at the one seam that matters.
- Fix: put both conditions into 1347-1351 and name them at the "That closes design" seam (1352).

B2 BLOCKING. The named-absence unit has no route to CONVERGED (1052-1055 against 1300-1303).
- A unit no input can legally reach at design time only ever gets reading rounds, and a reading round never converges it.
- No alternative route is named: neither a desk-executed measurement nor an [AUTO-ACCEPTED] carry.
- Strict reading: the unit never converges, the closing round never arrives, and the run burns to exhaustion. Lax reading: the rule is ignored, which is B1.
- Linked: "the verify phase's named-absence form" (1055) is a dangling cross-reference. `grep -n -i 'named-absence\|named absence'` hits only 1055. The nearest Verify form is NOT EXERCISED carried as a named [AUTO-ACCEPTED] (1705, 1721-1723), so the record form is unspecified.
(2/4) B3 BLOCKING. Aiming rounds at a subset contradicts the no-steering rule (1297-1298 against 1131-1135 and the verbatim question block, 1100-1129).
- To "aim at unconverged units plus cross-unit interactions", the brief must tell the attacker where to look. That is desk reasoning, which 1131-1135 forbids ("steering notes ... frames the round").
- The pasted block orders a whole-design attack (decomposition, simplicity, blast radius).
- CONVERGED entries sit in the never-filtered artifact (1037-1039) and tell later attackers which units are "done": steering by a second channel.
- Neither rule yields, so the page must say how aiming works without steering.

B4 BLOCKING. A convergence F-line corrupts `trend`'s arithmetic, which the canary cause reads.
- EXECUTED probe on a planted tracker in a scratch repo. Round 1: 3 findings. Round 2: 1 finding plus 3 lines `- F<n> [VERIFIED] record: unit U<k> converged` before the A-line ("rides the same return", 1295).
- Result: `TREND_COMPUTED counts [3, 4], trajectory WORSENING`.
- Same tracker with those 3 lines blanked: `counts [3, 1], trajectory IMPROVING`.
- Cause: statiker_record.py:2513 counts every F-line in the round window, whatever its scope.
- Convergence entries rise as findings fall, so they drag a genuinely contracting series toward FLAT or WORSENING.
- The canary passage (401-402) names "the trend verdict for arithmetic" as discriminating evidence, and the page never names CONVERGED's entry class (D-lines are not counted).
- Fix: pin a class that `trend` skips, or have `trend` exclude it.
(3/4) B5 BLOCKING. The raise template has no slot for the cause the new rule demands (396-400 against 410 and 419-425; tripwire raise at 372-374).
- Neither the template at 419-421 nor the CONTINUE ending at 410 has a cause slot. Its body-read (424-425) is future tool-parse surface, so a desk-spliced cause produces divergent spellings.
- The sentence contradicts itself: "never lands" means refuse; "granted causeless is a recorded miss" means it lands. And 413-418 says an operator raise LANDS.
- Unresolved:
  - a pre-emptive raise with no stop report behind it;
  - whether tripwire raises are covered;
  - where the "miss" is recorded (no entry form, no Close slot).
- The deleted phrase "owes a named cause at close-out" was the only record anchor, and the Close list (1832-1845) has no stop-cause item. The cause may live only in a reply, where a raise cannot quote it.

m1. "Born" has three definitions.
- The trend clause (1241-1245) counts any "unit, gate or form" a repair introduced.
- The intake clause (1310-1311) counts units only: "not a fix inside existing surface".
- The tool's concentration flag (statiker_record.py:2526-2540) counts any D-id revised in the prior re-lock.
- "That round's repairs" has an unclear referent. Inferred, unverified: the clause catches only the first round after a birth, not the multi-round founding pattern.

m2 (borderline-blocking). A justified join is self-defeating.
- A legal join (1314) followed by findings on the newborn is "non-contracting however the counts fall" (1243-1245).
- That routes to NARROWING. Where the head is minimal because of the join reason, it goes to the operator or FAILED unattended (1263-1267).
- Exempt the first post-birth round, or state the consequence.

m3 (borderline-blocking; export is the late-run default). Exporting a newborn unit bypasses the narrowing machinery (1311-1314 against 1254-1262).
- The newborn usually repairs a finding. Exporting it leaves that finding and its R-line unrepaired, with no R-amendment and no reconciliation: a silent narrowing.
- "The re-lock entry" is undefined (grep hits 1311 only). A re-lock is a commit, so the mandatory answer has no carrier.
(4/4) m4. The canary passage contradicts itself.
- It keeps "a cause report is a READ, not a composition" (404-405) but now demands "the generalization it implies" (397-398), which can only be composed.
- "Which design change" is ambiguous: the run's design (redesign inside an operator-owned stop) or the skill's structure.

m5. The attack-brief clause (1046-1055) has soft spots.
- It admits "planted" input but requires input "drawn from the source rather than built".
- "No input can legally reach" is an unchecked escape hatch.
- "One executed probe": per round or once? The qualifier needs every round.
- Can a desk-executed measurement (1291-1293) converge a unit?
- Live-source execution is not tied to the read-only tail or the `paths` by-product declaration (1736-1744, 1758-1760).

m6. The new clause's boundary disagrees with the verbatim block.
- The block allows "a full source-chain trace where it is still design prose" (1106-1107).
- The clause demands execution for anything "runnable at design time". A query or predicate written in a D-line is both.
- Which governs is unstated.

m7. CONVERGED and REOPENS are underspecified, and the insertion breaks a sentence.
- No entry class, tag or literal for either, so a resume finds converged units only by free-text read.
- Does a cross-unit finding reopen both units?
- "Near it" (1314) is undefined.
- Editorial: the insertion at 1046 severs "Unfiltered, the artifact compounds" (1057) from the filter paragraph it continues.

For the release gate: all five changes introduce mandatory forms, so they are C4b mints. OBSERVATIONS.md has tenet-check sections for the batch (around lines 12618 and 12706); I did not grade them.

Not run: the pytest suite; any `sustain`/`closure` execution over convergence entries. B1 rests on the page text plus the closure tool's documented last-A-line read (1452, 1481), not an executed closure run. The probe scratch lives only in my scratchpad; no repo writes.

---

## opus-review-s1

S1 review (budget-as-canary and trend location-over-count, SKILL.md @ ce271b7): 3 BLOCKING, 5 minor.

Reads I ran: the diff ae93661..ce271b7; SKILL.md lines 270-510, 1200-1320 and 1824-1843; statiker_record.py trend_over_rounds and cmd_trend (lines 2437-2565); OBSERVATIONS.md 12520-12660 (the booked entries and the mint record); LEDGER lines 163-177.
Seam enumeration, run over SKILL.md: grep -n -i for raise/raising gave 8 hits (372, 398, 410, 414, 416, 419-420, 490, and 1320, which is an unrelated use). The cause grep gave 284 (unrelated) and 397-406. CONTRACTING gave 389, 497, 1238, 1244, 1245, 1252. concentrat gave 1233, 1235, 1243, 1248. born/birth gave 1241, 1250, 1310-1315, plus section headings. stop report gave 397 only, and cause report 404 only.
Outside the page: references/ and defaults/ carry no trend, contracting, budget-raise or cause seam (grep, 1 unrelated hit). No .py file in scripts/ or tools/ parses the raise line: 0 hits for "budget raised|raised to". The positive control "tripwire armed" hit 7 times in statiker_record.py, so the search itself works.

BLOCKING 1: the "causeless-raise refusal" contradicts itself and has no seam in the form a raise lands in.
- SKILL.md:398-400 says "a raise never lands without that cause quoted beside it" and then "one granted causeless is a recorded miss". The second sentence assumes a causeless raise can land. The first says it cannot.
- Refusal reading: the desk declines to land an operator raise. That contradicts :413-416, where the bound is operator-owned, the desk never raises it, and "an operator raise LANDS as an ordinary entry". An attended desk following this reading stalls on an operator decision.
- Record reading: the raise lands and a "miss" is recorded. But no form, home or actor for that miss exists anywhere on the page. The sentence can be satisfied by recording nothing.
- The mandatory raise template at :419-421 (`- F<n> [VERIFIED] record: budget raised to … — "<operator line>" — basis: operator`) has no cause slot. :423-425 says the exhaustion check body-reads exactly this template. So a desk that fills the template word for word writes a causeless raise, and nothing on the page fails.
- CONTINUE at :409-411 ("an ordinary budget-raise entry") and the authority-ask form at :488-494 (a bound raise lands as [PENDING]) are two more seams that name the raise. Neither carries the cause either.
- Field datum (LEDGER:164): the btb run landed the raise as F80 with the cause and the framing as a separate F81. That is improvised placement, not a form.
- Fix: put a cause slot in the :419 template (and so in CONTINUE), and decide one reading. Either the desk lands the raise and names the missing cause as an open entry, or the refusal is explicit, with its interaction with operator ownership stated.

BLOCKING 2: the "stop report" that owes cause and generalization has no defined form or home. It diverges from the seams where a budget stop actually lands.
- :397 is the only place "stop report" appears on the page.
- Exhaustion routes at :377-379. Attended, it "forces the operator prompt". Unattended, it "STOPS-AND-REPORTS", and it is not a close ("never grades FAILED by itself").
- The Close enumeration at :1826-1843 does not list budget cause or generalization. The authority-ask entry at :488-494 does not either.
- So attended, the prompt is not called a stop report, and a desk can reasonably hold that the demand does not bind it. Unattended, the report has no tracker carrier: a resume reads the tracker, and the "quoted beside it" cause has nothing to quote from.
- This is the multi-location divergence class: one demand at one seam, while the two actual exit seams stay silent.

BLOCKING 3: the trend change widens "born" from units to "gate or form", with no incident behind the widening. The widening makes a healthy converging tail grade NON-CONTRACTING.
- :1241-1245 defines newborn ground as "a unit, gate or form the repair introduced".
- The booked text (OBSERVATIONS:12561-12562) and both incidents (U5/U6 at OBSERVATIONS:12532; :1315) are about UNITS only.
- The intake clause at :1309-1311, from the same batch, defines a birth as "new design surface, not a fix inside existing surface". A repair that adds a gate or form to fix an existing unit is therefore not a birth under the intake clause but is newborn under the trend clause.
- Consequence: most repairs introduce a check, key or gate (LEDGER:164, D20: "U4 own cooldown key", "UNVERIFIED-only-when-enabled"). Take a series whose findings are shrinking into the last repair's own residue, for example 3 to 1 with the one finding in the added gate. It now grades non-contracting "however the counts fall".
- The per-unit convergence clause at :1297 makes this systematic. Later rounds aim at unconverged units, so findings concentrate on the latest repairs by construction.
- Route: NARROWING. Where the head is already the smallest unit, :1263-1267 sends it to the operator, and unattended the run closes FAILED on a healthy series.
- The same mechanism defeats the intake clause's named-join branch (:1314). A joined newborn's first attack almost surely draws findings, which grades non-contracting and routes to narrowing, which exports it. A named join cannot survive the next round.
- Fix: scope newborn to units, matching the intake clause's birth test and the incident, or state explicitly how a joined newborn and in-unit repair gates are graded.

Minor:
- M1. The trend tool's CONCENTRATION flag cannot tell the new distinction apart. statiker_record.py:2524-2541 flags any finding citing a D-id whose latest revision landed in the previous re-lock window. That covers newborn D-ids and D-lines revised in place alike. By the new prose's contrast, in-place repair ground is "already bit" (it can contract), while newborn ground is not. Its output text ("CONCENTRATION in the previous re-lock's repairs", :2559) reads like the prose's "findings concentrating there". A desk reading the backstop will map the flag onto the newborn rule in both directions. The prose does keep the grade as a body-read (:1231), so the grade is still reachable; the backstop now overstates. Also the tool's flag fires on ANY single hit (a boolean), while the prose says "concentrating". The threshold is undefined, beside CONTRACTING's "mostly".
- M2. "the location read outranks the count read" (:1245) reads as a general precedence rule. CONTRACTING needs BOTH falling counts AND already-bit ground (:1239-1241), so location can only demote. A desk taking the sentence generally could grade rising counts on already-bit ground CONTRACTING. That is the fail-open direction (it skips narrowing). Scope the sentence to the newborn case.
- M3. The one-step lookback narrows the booked text. "Ground BORN from that round's repairs" (:1241) only looks back to the immediately previous round's repairs. The booked text said "units born from prior repairs" (OBSERVATIONS:12562). Under the minted text, a newborn unit that is bit once becomes "ground already bit". The founding pattern at :1315, where newborns drew EVERY later round's substance, then reads CONTRACTING from its second round on whenever counts fall. Say whether aging out after one round is intended.
- M4. The generalization demand (:397-398, "which design change makes the class not recur") is a composition, and the next sentence (:404) says "a cause report is a READ, not a composition". Also ambiguous: whether the design change is the run's (re-scope) or the skill's (mint source, :395). A desk cannot author a skill change, and per CLAUDE.md it does not know the meta repo exists.
- M5. "that cause" (:399) has no antecedent for a mid-run raise the operator grants before exhaustion (:414-416), because no stop report exists then. Under the record reading, every proactive raise is a "miss". Also: whether the canary and cause duty covers the tripwire threshold raise at :372-374 (the "same split") is unstated. The booked text scoped it to the rounds budget (OBSERVATIONS:12578); the minted text says "the bound", meaning all three counters.

Checks that ran clean: the canary clause does not contradict :380-390, where the driving stop signals still route to NARROWING. The measured-variant parenthetical (:1248-1251, "graded improving by count") matches the incident: A3 was 10 to 5, IMPROVING under trend_verdict (:2448-2449). Nothing was skipped.
Inferred, not executed: the B3 consequence (a healthy tail closing FAILED) is derived from reading :1241-1245 together with :1263-1267 and :1297. I did not run any tracker through it.
S1 review (1/4): 3 BLOCKING, 5 minor over the canary and trend changes in SKILL.md @ ce271b7.
Reads: the diff ae93661..ce271b7; SKILL.md :270-510, :1200-1320, :1824-1843; statiker_record.py :2437-2565 (trend); OBSERVATIONS.md :12520-12660; LEDGER :163-177.
Seam greps over SKILL.md:
- raise: 372, 398, 410, 414, 416, 419-420, 490 (1320 unrelated)
- cause: 397-406 (284 unrelated)
- CONTRACTING: 389, 497, 1238, 1244-1245, 1252
- concentrat: 1233, 1235, 1243, 1248
- born/birth: 1241, 1250, 1310-1315
- "stop report": 397 only
references/ and defaults/: no seam (1 unrelated hit). Raise-line parsing in any .py under scripts/ or tools/: 0 hits; the positive control "tripwire armed" hit 7 in statiker_record.py.

BLOCKING 1: the causeless-raise rule contradicts itself and has no seam in the raise form.
- :398-400 says "a raise never lands without that cause" and then "one granted causeless is a recorded miss", which assumes it can land.
- Refusal reading: this contradicts :413-416, where the bound is operator-owned and "an operator raise LANDS as an ordinary entry". An attended desk stalls on an operator decision.
- Record reading: no form, home or actor for the "miss" exists, so recording nothing satisfies the sentence.
- The mandatory raise template (:419-421) has no cause slot, and the exhaustion check body-reads exactly that template (:423-425). A desk filling the template word for word lands a causeless raise and nothing fails.
- CONTINUE (:409-411, "ordinary budget-raise entry") and the authority ask (:488-494, bound raise as [PENDING]) also name the raise, and neither carries a cause.
- Field: LEDGER:164, where F80 carries the raise plus cause and F81 the framing. That was improvised.
- Fix: a cause slot in :419 (which CONTINUE inherits), plus one chosen reading.
S1 review (2/4). BLOCKING 2: the "stop report" that owes cause and generalization has no form or home. It diverges from the seams where a budget stop actually lands.
- :397 is the only place "stop report" appears on the page.
- Exhaustion routes at :377-379. Attended, it "forces the operator prompt", which is never called a stop report, so a desk can hold that the demand does not bind it. Unattended, it "STOPS-AND-REPORTS" and is not a close.
- The Close enumeration (:1826-1843) and the authority-ask entry (:488-494) name neither the cause nor the generalization.
- So there is no tracker carrier: a resume reads the tracker, and the cause "quoted beside" the raise has nothing to quote from. This is the multi-location divergence class: one demand at one seam, while both actual exit seams stay silent.

BLOCKING 3: the trend change widens "born" to "a unit, gate or form" (:1241-1245) with no incident behind the widening.
- The booked text (OBSERVATIONS:12561-12562) and both incidents (U5/U6 at :12532; SKILL :1315) concern UNITS.
- The intake clause from the same batch (:1309-1311) defines birth as "new design surface, not a fix inside existing surface". A repair gate is therefore not a birth under the intake clause but is newborn under the trend clause.
- Most repairs add a check or key (LEDGER:164, D20: "U4 own cooldown key", "UNVERIFIED-only-when-enabled"). A healthy tail, for example 3 findings then 1 with the 1 in the added gate, now grades NON-CONTRACTING "however the counts fall".
- The convergence aiming (:1297, later rounds aim at unconverged units) makes this systematic.
- Route: NARROWING. Where the head is already the smallest unit, :1263-1267 sends it to the operator, and unattended it closes FAILED on a healthy series.
- The same path kills the intake clause's named-join branch (:1314): a joined newborn's first attack draws findings, which routes to narrowing, which exports it.
- Fix: scope newborn to units per the intake birth test, or state how in-unit repair gates and joined newborns grade.
- Inferred, not executed: I read the :1241 + :1263 + :1297 chain but ran no tracker through it.
S1 review (3/4), minor findings.
- M1. The trend tool's CONCENTRATION flag cannot make the new distinction. statiker_record.py:2524-2541 flags any finding that cites a D-id whose latest revision landed in the previous re-lock window. That covers newborn D-ids and D-lines revised in place alike, though the new prose's contrast treats in-place repair ground as "already bit". The output line (:2559, "CONCENTRATION in the previous re-lock's repairs") reads like the prose's "concentrating there", so a desk will map it onto the newborn rule. The grade stays a body-read (:1231), so the grade is still reachable; the backstop now overstates. Also, the flag fires on one hit, while "concentrating" has no threshold, beside CONTRACTING's "mostly".
- M2. "the location read outranks the count read" (:1245) reads as a general precedence rule. CONTRACTING needs BOTH falling counts AND already-bit ground (:1239-1241), so location can only demote a grade. Read generally, rising counts on already-bit ground could grade CONTRACTING, which is fail-open. Scope the sentence to the newborn case.
- M3. "that round's repairs" (:1241) looks back one round only, narrowing the booked "units born from prior repairs" (OBSERVATIONS:12562). A newborn that is bit once becomes "already bit". The :1315 pattern, where newborns drew EVERY later round, then reads CONTRACTING from its second round on whenever counts fall. Say whether that aging out is intended.
S1 review (4/4), remaining minor findings and the clean checks.
- M4. The generalization demand (:397-398, "which design change makes the class not recur") is a composition, while :404 says "a cause report is a READ, not a composition". It is also ambiguous whether the design change belongs to the run (a re-scope) or to the skill (the mint source, :395). A desk cannot author the skill change, and per this repo's CLAUDE.md the desk does not know the meta repo exists.
- M5. "that cause" (:399) has no antecedent for a raise the operator grants before exhaustion (:414-416), because no stop report exists yet. Under the record reading, every proactive raise is a miss. Also unstated: whether the canary and cause duty covers raising the tripwire threshold (:372-374, "the same split"). The booked text scoped it to the rounds budget (OBSERVATIONS:12578); the minted text says "the bound", which covers all three counters.
Clean:
- The canary clause is consistent with :380-390: the driving stop signals still route to NARROWING.
- The measured-variant parenthetical (:1248-1251, "graded improving by count") matches the incident: A3's 10 then 5 is IMPROVING under trend_verdict (:2448-2449).
No check was skipped. End of S1.

---

## opus-review-s2

S2 review, semantics half. Verdict: NOT release-ready. 6 BLOCKING and 5 minor findings across the three changes in scope. One finding is tool-probed; the rest are page reads, cited by file:line.

Object: plugin/skills/statiker/SKILL.md at ce271b7. The working tree equals ce271b7 (`git diff --stat ce271b7` was empty), so the line numbers below are the file's. The delta changes nothing under scripts/ (`git diff --stat ae93661 ce271b7 -- plugin/ tools/` lists SKILL.md, plugin.json and hooks.json only). So CONVERGED, REOPENS and join-or-export are prose-only, and no tool reads them.

Where each token or form is named or implied:
- CONVERGED: 1296-1307 and 1052.
- REOPENS: 1308. It sits beside the design-reopen at 1337-1346 and 1376.
- INTAKE / join-or-export: 1310-1317. The page has other export forms at 407-411, 720-728, 1255-1261 and 1881-1898.
- Executed-probe demand: 1046-1055. It sits beside the verbatim question block at 1104-1111 and the ZERO-DELTA condition at 1348-1352.

BLOCKING

B1. The closing round over the converged set has no legal A-line, and the aimed round's zero opens closure early (fail-open). Lines 1298-1299 say later rounds aim at unconverged units, and "the closing zero-delta round runs once over the converged set". But a substance-free return records [ZERO-DELTA] and "That closes design" (1348-1352). The A-tag set is exactly DISPATCHED, BIT, ZERO-DELTA and VOID (statiker_record.py:222). The implementation gate opens on the last A-line being [ZERO-DELTA] (1404-1406, 1481-1482). So when an aimed round returns zero on the unconverged units, its only legal tag is ZERO-DELTA. That tag flips Phase to implement before the prescribed closing round has run. The units that converged earlier are never re-attacked in their final form, and neither are their interactions with later repairs. Running the closing round after that ZERO-DELTA is a round the Phase and closure machinery does not model. Fix: name the aimed round's zero outcome. Either it is BIT-free but not closing, which needs a tag or a `record:` marker that `closure` reads, or state that ZERO-DELTA is recordable only on a round whose brief covered every unit.

B2. The altitude rule does not reach the whole-design closure seam (fail-open). Lines 1050-1052 and 1300-1302 say a reading round's zero on an executable unit is could-not-verify and "converges nothing". The CONVERGED clause is named as carrying the grading half. But the ZERO-DELTA recordability condition (1349-1351) only requires "every verdict reach-matched" and no [PENDING]. So a reading-only round that returns zero findings across all units still records [ZERO-DELTA] and closes design. That is the same zero that the new text says cannot converge even one unit. The founding probe (1303-1307) is exactly that case: reading rounds were clean, and the first executing round bit. Fix: add to the ZERO-DELTA condition that every executable unit was executed in that round or carries its recorded named absence.

B3. The natural CONVERGED entry inflates `trend` counts, and trend is the stop report's pre-registered arithmetic evidence (tool-probed). Line 1297 says CONVERGED is recorded "as that unit's own `record:`-scoped entry", landing at the return before the A-line (1285-1293). It does not name the entry class. `trend_over_rounds` (statiker_record.py:2512-2514) counts EVERY F-line in the round window, whatever its scope. Only the concentration flag excludes `record:` (2534-2536).
Probe (a scratch git repo in my scratchpad; three trackers, all LINT_CLEAN):
- Control, substance findings per round 3, 2, 1, no CONVERGED lines: `trend` gives [3, 2, 1] IMPROVING.
- Same substance findings plus `- F<n> [VERIFIED] record: unit U<k> CONVERGED at A<n>` lines (0, 2, 2 per round): `trend` gives [3, 4, 3] FLAT.
- Variant with one CONVERGED line per round: [4, 3, 2], still IMPROVING. So the trajectory flips only when convergence is uneven across rounds.
- `sustain` also lists each CONVERGED line as a "record/instrument-class finding … desk work".
Convergence progress therefore reads as stalling. Line 402 names "the trend verdict for arithmetic" as the stop report's discriminating evidence, so a misread there produces a mis-caused stop report. Fix: either specify a non-F class for the entry, or have the counts exclude `record:`-scoped F-lines the way concentration already does. Both are cheap. The second is a tool change, which puts this under the machine-read review class.

B4. The INTAKE export names none of the page's export forms, and the finding the newborn unit answered is left without a disposition. Lines 1311-1314 say export is the default, but give no form. The page has four export forms, and they differ in authority and in mechanical enforcement:
- The operator-owned EXPORT ending (407-409).
- Out-of-scope EXPORTED with a carrier reference (720-728).
- NARROWING, which is an R-amendment plus a backlog entry, riding the close as a reconciliation because it "touches INTENT's reach" (1255-1261).
- The leavings `— exported: <ref>` line, which `closure` holds on (CLOSURE_LEAVINGS_HOLD) only when the id carries an `out-of-scope:` opener (1881-1898).
An intake export written as a plain note engages none of the gates, so nothing holds the closure until the backlog reference exists. That is silent loss. Worse, the newborn was born to repair an in-scope design-substance finding. Exporting it by default leaves that finding's ground unrepaired, and the rule says nothing about the finding's disposition or an R-amendment. A desk can satisfy "export at birth" and still ship the bitten unit. Fix: route the intake export through the NARROWING machinery (R-amendment, backlog entry, reconciliation at close), and require the answered finding to be re-dispositioned there.

B5. The named-absence escape points at a form the page never defines, lives only in the brief, and leaves no convergence path.
- Line 1054 says "the verify phase's named-absence form". The Verify section (1692-1822) has no form by that name. The nearest are the per-R "NOT EXERCISED" statement (1705) and "non-exercise carried as a named [AUTO-ACCEPTED]" (1722-1723), and those are two different forms.
- The absence is named "in the brief". Briefs travel by message and are not in the tracker, so a successor desk, the verify leg and the closure seam cannot see it.
- The altitude rule (1300-1302) says a unit whose mechanism was not executed never converges. So an absence-named unit (an authority-gated prod act) can never converge at design time. It is either aimed at in every later round, or the desk improvises and converges it on a reading zero, which defeats the rule. The "closing round over the converged set" (1299) then excludes it.
Fix: record the absence as a tracker entry of a named form, and state that entry's convergence consequence (for example: converges on a reading zero plus the recorded absence, and verify owes the executed check).

B6. The attacker-facing verbatim block still permits exactly the zero the new clause voids. The question block, which is pasted verbatim and governs what the attacker does (1100-1111), demands "an executed probe where the object exists to execute, a full source-chain trace … where it is still design prose". At design time an executable mechanism is still design prose, so an attacker following the block legitimately returns a trace-backed zero. The new clause (1046-1052) grades that zero could-not-verify. The executed-probe demand travels only as free prose "named in the brief", the channel the page itself says drops invariant clauses (1101-1102: "free-composed briefs drop invariant clauses"). Fix: put the demand into the verbatim block, or amend the block's "design prose → trace" branch for runnable mechanisms.

MINOR

m1. Aiming contradicts the brief-purity rule. "Later rounds aim at unconverged units" (1298) needs either brief prose listing where to look or CONVERGED entries the attacker reads in the never-filtered artifact. Lines 1131-1135 bar exactly that: "a weak-spot list, steering notes … desk reasoning riding the never-filtered channel". The verbatim block still says to attack the whole design. Needs an explicit carve-out, for example a declared scope form like the recorded-narrowing clause at 1116-1119.

m2. The REOPENS entry's form is unspecified.
- "By an entry citing the finding" (1308-1309) invites a new-id line. That leaves the CONVERGED entry live beside it, which is the "two live contradictory entries" hazard, against the page's same-id [INVALIDATED] supersession idiom (742-744; tripwire disarm at 369-371).
- A `record:` CONVERGED entry carries no machine-readable unit id (classify_scope returns "record"), so converged state is computable only by body-read.
- The scope is unstated. A scopeless D-class REOPEN after a terminal [BIT] keeps CLOSURE shut (1458-1464), the F118 over-correction. A `unit U<k>` REOPEN after closure re-opens dispatch (1488-1490).
- "REOPENS" (a unit) also collides with "reopen" (the design, 1338, 1376).
Fix: specify a `record:` scope and same-id supersession.

m3. "One EXECUTED probe" (1048) is ambiguous: one per brief or round, or one per unit ever? Read with 1300-1302 ("never converges a unit whose mechanism it did not execute"), a one-per-unit reading means later rounds that don't re-execute can never converge that unit.

m4. Line 1047 defines the class as "runnable against real or planted input", but line 1049 requires input "drawn from the source … rather than built to the design's own assumption". When the real source is unreachable but a planted input is (which is not the named-absence case, since planted input can always legally reach the mechanism), a desk can satisfy the demand with a self-built fixture. That defeats the stated purpose.

m5. Editorial seams.
- Inserting the paragraph at 1046-1055 leaves "Unfiltered, the artifact compounds per round" (1057) reading as if it refers to the probe paragraph. It refers to the filter paragraph at 1033-1044.
- "The re-lock entry" (1311) names no form defined on the page. My grep of "re-lock" found hits at 544, 921, 950, 1222, 1238, 1487 and 1311, and none defines an entry. The nearest defined thing is the [READY] line plus the lock commit (1017-1018). This is inferred from that grep and unverified beyond it.

Checks run: 3 tracker probes, each through lint, trend and sustain. All ran, with 0 skips. Two earlier attempts failed on the environment rather than the probe, and I corrected and re-ran them: PATH_OUTSIDE_REPO until I made a scratch git repo, then tag-enum and phase-enum lint until I fixed the fixture's D-tags and Phase. Findings other than B3 are page reads, not executed checks. B1's fail-open consequence is derived from 1348-1352 and 1481-1482 and was not exercised through `closure`. Nothing was written to the repo. Scratch is in my scratchpad only.
S2 review (1/5), semantics half. Verdict: NOT release-ready. 6 BLOCKING and 5 minor findings; one is tool-probed (B3), the rest are page reads with file:line.

Object: SKILL.md at ce271b7. The working tree equals ce271b7, so the line numbers are the file's. The delta changes nothing under scripts/ (`git diff --stat ae93661 ce271b7 -- plugin/ tools/` lists SKILL.md, plugin.json and hooks.json only), so CONVERGED, REOPENS and join-or-export are prose-only and no tool reads them.

Where each is named: CONVERGED 1296-1307 and 1052; REOPENS 1308 (next to the design-reopen at 1337-1346 and 1376); INTAKE/join-or-export 1310-1317 (the page has other export forms at 407-411, 720-728, 1255-1261, 1881-1898); executed-probe demand 1046-1055 (next to the verbatim block at 1104-1111 and the ZERO-DELTA condition at 1348-1352).

B1 BLOCKING, fail-open: the closing round over the converged set has no legal A-line, and the aimed round's zero opens closure early. 1298-1299 say later rounds aim at unconverged units and "the closing zero-delta round runs once over the converged set". But a substance-free return records [ZERO-DELTA], and "That closes design" (1348-1352). The A-tags are exactly DISPATCHED/BIT/ZERO-DELTA/VOID (statiker_record.py:222), and the gate opens on a last A-line of [ZERO-DELTA] (1404-1406, 1481-1482). So an aimed round returning zero can only record ZERO-DELTA. That flips Phase to implement before the closing round runs, and units that converged earlier are never re-attacked in final form, nor their interactions with later repairs. Fix: name the aimed round's zero outcome, or make ZERO-DELTA recordable only on a round whose brief covered every unit.
S2 review (2/5).

B2 BLOCKING, fail-open: the altitude rule does not reach whole-design closure. 1050-1052 and 1300-1302 say a reading round's zero on an executable unit is could-not-verify and "converges nothing". The ZERO-DELTA condition (1349-1351) only needs every verdict reach-matched and no [PENDING]. So a reading-only round with zero findings across all units still records [ZERO-DELTA] and closes design, even though that same zero cannot converge a single unit. The founding probe (1303-1307) is exactly this case. Fix: ZERO-DELTA requires every executable unit to have been executed that round, or to carry its recorded named absence.

B3 BLOCKING, tool-probed: CONVERGED entries inflate `trend` counts, and trend is the stop report's pre-registered arithmetic evidence (402). 1297 says CONVERGED is a "`record:`-scoped entry" landing at the return before the A-line (1285-1293), with no entry class named. The natural choice is a `record:` F-line. `trend_over_rounds` (statiker_record.py:2512-2514) counts every F-line in the window whatever its scope; only concentration excludes `record:` (2534-2536).
Probe, run in a scratch git repo; all 3 trackers LINT_CLEAN:
- control, substance findings per round 3,2,1 → `trend` [3, 2, 1] IMPROVING
- same, plus `- F<n> [VERIFIED] record: unit U<k> CONVERGED at A<n>` lines (0,2,2 per round) → [3, 4, 3] FLAT
- variant with one CONVERGED line per round → [4, 3, 2], still IMPROVING. So the flip needs uneven convergence.
`sustain` also lists each CONVERGED line as a "record/instrument-class finding … desk work".
Result: convergence progress reads as stalling, and the stop report is mis-caused. Fix: specify a non-F class for the entry, or make counts exclude `record:` F-lines as concentration already does. The second is a tool change, so it falls in the machine-read review class.
S2 review (3/5).

B4 BLOCKING: the INTAKE export (1311-1314) names none of the page's four export forms, and they differ in authority and in gating:
- the operator-owned EXPORT ending (407-409)
- out-of-scope EXPORTED with a carrier ref (720-728)
- NARROWING: R-amendment plus backlog entry, riding the close as a reconciliation because it "touches INTENT's reach" (1255-1261)
- the leavings `— exported: <ref>`, which `closure` holds on (CLOSURE_LEAVINGS_HOLD) only for ids with an `out-of-scope:` opener (1881-1898)
An intake export written as a plain note engages no gate, so it can be lost silently. Worse: the newborn exists to repair an in-scope design-substance finding. Exporting it by default leaves that ground unrepaired, and nothing says what happens to the finding or whether an R-amendment is owed. A desk can satisfy "export at birth" and still ship the bitten unit. Fix: route the intake export through the NARROWING machinery, with the answered finding re-dispositioned there.

B5 BLOCKING: the named-absence escape is undefined, unrecorded and non-convergent.
- 1054 cites "the verify phase's named-absence form". Verify (1692-1822) has no form by that name; the nearest are "NOT EXERCISED" (1705) and the "named [AUTO-ACCEPTED]" non-exercise (1722-1723), which are two different forms.
- The absence is named "in the brief". Briefs are messages, not tracker entries, so a successor, the verify leg and the closure seam cannot see it.
- By 1300-1302, a unit whose mechanism was never executed never converges. An absence-named unit therefore either draws aim in every round, or the desk improvises a reading-zero convergence that defeats the rule. The closing round "over the converged set" (1299) also excludes it.
Fix: record the absence as a named tracker entry and state its convergence consequence, e.g. it converges on a reading zero plus the recorded absence, and verify owes the executed check.
S2 review (4/5).

B6 BLOCKING: the attacker-facing verbatim block still allows the zero the new clause voids. The block (1104-1111), pasted verbatim, asks for "an executed probe where the object exists to execute, a full source-chain trace … where it is still design prose". At design time an executable mechanism is still design prose, so an attacker following the block returns a trace-backed zero, and 1046-1052 grades that zero could-not-verify. The executed-probe demand reaches the attacker only as free prose "named in the brief", the channel 1101-1102 says drops invariant clauses. Fix: put the demand into the verbatim block, or amend the block's design-prose-means-trace branch for runnable mechanisms.

m1 minor: aiming contradicts the brief-purity rule. "Later rounds aim at unconverged units" (1298) needs either brief prose saying where to look, or CONVERGED entries the attacker reads in the never-filtered artifact. 1131-1135 bars both: "a weak-spot list, steering notes … desk reasoning riding the never-filtered channel". The verbatim block also still says to attack the whole design. Needs an explicit carve-out, e.g. a declared scope form like the recorded narrowing at 1116-1119.

m2 minor: the REOPENS entry's form is unspecified.
- "By an entry citing the finding" (1308-1309) invites a new-id line, which leaves CONVERGED live beside it. That is the two-live-contradictory-entries hazard (742-744), against the page's same-id [INVALIDATED] supersession idiom (369-371).
- A `record:` entry carries no machine-readable unit id (classify_scope returns "record"), so converged state is body-read only.
- Scope is unstated. A scopeless D-class REOPEN after a terminal [BIT] keeps CLOSURE shut (1458-1464, the F118 over-correction). A `unit U<k>` REOPEN after closure re-opens dispatch (1488-1490).
- "REOPENS" (unit) collides with "reopen" (design, 1338, 1376).
S2 review (5/5).

m3 minor: "one EXECUTED probe" (1048) is ambiguous: one per brief, or one per unit ever? Under 1300-1302 ("never converges a unit whose mechanism it did not execute"), the per-unit reading means later rounds that don't re-execute can never converge that unit.

m4 minor: the class is "runnable against real or planted input" (1047), but the probe's input must be "drawn from the source … rather than built to the design's own assumption" (1049). Where the real source is unreachable but a planted input is, the named-absence escape does not apply (planted input can always reach). A desk can then satisfy the demand with a self-built fixture, which defeats the purpose.

m5 minor, editorial:
- The paragraph inserted at 1046-1055 makes "Unfiltered, the artifact compounds per round" (1057) read as if it refers to the probe paragraph. It refers to the filter paragraph at 1033-1044.
- "The re-lock entry" (1311) names no defined form. A grep for "re-lock" found only 544, 921, 950, 1222, 1238, 1487 and 1311, none defining an entry; the nearest is the [READY] line plus lock commit (1017-1018). Inferred from that grep, unverified beyond it.

Checks run: 3 tracker probes, each through lint, trend and sustain; all ran, 0 skips. Two earlier attempts failed on environment and fixture grammar, not on the question: PATH_OUTSIDE_REPO until I made a scratch git repo, then tag-enum and phase-enum lint until I fixed the D-tags and Phase. I corrected both and re-ran. All findings other than B3 are page reads, not executed checks. B1's fail-open consequence is derived from 1348-1352 and 1481-1482 and was not exercised through `closure`. Nothing was written to the repo; scratch lives only in my scratchpad.

---

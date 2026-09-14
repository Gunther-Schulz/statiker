# Narrow round — run-3 contract, delta 3f6b6da..HEAD, 2026-09-14

VERDICT: **PIN HOLDS. 3 BLOCKING, 8 SUBSTANTIVE, 5 MINOR.** Not a
zero-delta round. Fresh-context opus lane, read-only, scoped narrow:
banked findings explicitly out of bounds.

**THE HOLD IS NOT ON THE PAYLOAD.** The delta touches ZERO `plugin/`
files; nothing found bears against 0.2.100. The hold is that the pin
move's consuming seam — run 3's freeze and arm dispatch — cannot
execute as the contract is written.

VERIFY (reviewer's run, matching this desk's): 632 passed, 2 subtests,
0 failed, **0 skipped**. `--selftest` 8/8. Mutations on a `git archive
HEAD` copy in its own scratchpad, restored byte-identical, repo tree
clean throughout. Neither probe run against a live child.

DESK SPLIT RATIFIED by statiker-e8: payload banked certified-clean,
contract repairs to a FRESH desk, this prep desk retires. Basis of
record: the series 1B/2S → 1B/5S → 3B/8S is WORSENING and the worst
findings arrived from this desk's OWN repairs — the re-entry rule
routes that to narrowing, never a fourth same-form round.

PIN STAYS 0.2.99 — not a hold on the payload but on the absence of a
live consuming seam (release-batching convention). The pin moves when
run 3 is actually about to start, over the final contract, on the
fresh desk.

---

## BLOCKING

**B1 — §9.1's byte-identity criterion is unsatisfiable by any state of
the world; its comparand is in no repo artifact.** The cold probe's
prompt ends *"State the acceptance criterion for a correct fix… Answer
in under 250 words."*; §3's arm text ends *"Fix it. Your working copy
is <CLONE PATH>…"*. They can never be byte-identical, so axis 1 has
been VOID on the document's own terms since registration, chaining via
§9.2/§9.3 to column 2a certifying nothing. The shared half diverges
too (straight quotes vs backticks; "Defect:" vs "DEFECT:"; "So two
predicates" vs "Two predicates"). §2c's pointer promises the raw
answer in the candidates round; that file carries only a paraphrase —
the reviewer recovered the prompt from
`~/.claude/projects/-tmp-statiker-probe-neutral-3TKE/74fcb57f-….jsonl`.

DISPOSITION: commit the prompt VERBATIM as the named comparand and
restate §9.1 over the requirement PARAGRAPHS. **NOT a re-run** — the
probe's ask was HARDER than the arm's (it asked directly for
acceptance criteria) and still did not produce the near-miss, so the
MEASUREMENT stands; what was wrong is the desk's specification of what
it protects. Booked st-76, READY.

**B2 — the chosen ceiling substrate BREAKS the parity §15c bought, and
§3a.5 asserts it does not.** The ceiling arm becomes a SERIES driven by
an external re-invoker with unspecified policy (when it fires, what it
sends, how often), attached to ONE arm, on the exact axis run 2's
ceiling arm died on. Codex arms are one `codex exec -s
danger-full-access` fed frozen text, their re-invocation axis
UNMEASURED. No driver is specified anywhere: `driver_resume_probe.py`
is two hardcoded prompts, not a run driver.

THE TELL IT IS A TRANSFER FAILURE: §3a.4 applies precisely this parity
reasoning to the candidate it REJECTS (the interactive session) and
does not carry it to the candidate it SELECTS.

CONSEQUENCE: under §6c a non-collision produced by one arm having
turn-continuation apparatus the others lack would read as TIER
SEPARATION — run 3's whole failure mode, arriving from the opposite
side of run 2's. Booked st-77, PARKED on the scope question.

**B3 — the reason for including terra is refuted at the code, and
§6a's write-side premise is false for this run's launcher.** The
containment gate is preflight-time satisfiability ONLY
(`statiker_git.py:1274-1366`, three axes over the declared scope, then
never again). Terra's actual act — `filter --out /tmp/invalid` — goes
through `statiker_record.py:2752-2761`'s ARTIFACT_IN_REPO check, which
consults NO containment scope. VERIFIED AT THIS DESK: 2 mentions of
containment in the record tool against 27 in the git tool, and the
`--out` check is purely outside-every-repo. Terra's exact act returns
proceed in run 3 exactly as in run 2.

SECOND HALF: §6a rests on "codex's sandbox pins WRITES, never read
reach", while this run's launcher is `-s danger-full-access` — which
run 2's own §15d quotes as "it is NO sandbox". The write-side
protection §6a assumes does not exist, and §6a's residual is scoped to
READS, so nothing covers the class that actually fired in the field.

DISPOSITION: restate terra's inclusion on what the gate ACTUALLY does;
correct §6a's premise; the runtime authorized-path check on `--out` is
a real design question, not a wording fix. Booked st-78, PARKED.

---

## SUBSTANTIVE

**S1 — `driver_resume_probe.py` has NO could-not-verify state and NO
control, and §3a.4 claims a refusal guard wider than the code.** The
document says the probe "refuses a verdict when [the unaided arm is
not red]". The code refuses on ONE condition: the unaided arm having
WRITTEN the marker. A timeout, a rate-limit refusal, any nonzero exit
yields ack=False and PASSES the guard as a valid red — and if the
driven arm then also fails, the probe prints a SUBSTRATE verdict over
an attempt that never ran. §3a.4 routes that verdict to an operator
decision round about what run 3 certifies, so an environment refusal
at freeze would arrive at the operator as a scope change. No analogue
of the sibling probe's control leg or PROBE_INVALID domination: an
unwritable target reads identically to substrate death. No `--selftest`,
no battery — the sibling got an 11-test battery in THIS SAME DELTA
(eve-review M3) while this probe, which §3a.4 rests the ceiling
resolution on, got none. The defect-class sweep over the artifact
carrying the found instance, not performed.

**S2 — `launch_substrate_probe.py` returns SUBSTRATE_DIES_AT_REINVOCATION
with the reason "the ACK marker is absent" in two states where ACK IS
PRESENT.** Executed over every reachable marker combination with a fake
shell launcher: `bg=T ack=T turn_end=F` and `bg=F ack=T turn_end=F`
both yield that verdict and that false reason, because the inconclusive
route is gated on `turn_end_present and bg_present` while the prompt
bundles marker and turn end into ONE step. The recorded 0.2.100 verdict
is unaffected (the genuine red row has NEITHER marker), and v2 cannot
flip a v1 red since it only adds failure and inconclusive routes.

**S3 — the nonce's "caught by construction" claim is wider than the
construction; the recorded measurement is sound.** Both arms use the
SAME nonce and both prompts persist in the cwd-keyed transcript store,
so a fresh non-resumed turn-2 child is not PREVENTED from producing the
token, only unlikely to go looking. The reviewer then VERIFIED the
recorded green independently: turn 1 and turn 2 in ONE session file,
turn 2's tool sequence `mkdir -p` then `Write` of the token, no Read,
Grep or search anywhere. **The measurement stands; the guarantee does
not.** Cheap repair: a distinct nonce per arm, plus a third arm with a
FRESH session id given turn 2's prompt, which must NOT produce the
token.

**S4 — THE FINDING OF THE ARC. The ceiling arm inherits the operator's
global corpus, which no codex arm receives, and §2c's contamination
binding is keyed on the wrong scope to catch it.** The "cold context
with no repo access" carried NINE files loaded CWD-INDEPENDENTLY,
including Grounding's prefix-match rule — the nearest neighbour of the
withheld criterion. This desk's contamination fix moved the probe out
of the REPO; the larger load was never in the repo.

STATED IN BOTH DIRECTIONS, as the reviewer stated it: the RESULT is
STRONGER than the document claims (the context held the
matching-semantics rule and STILL did not produce the near-miss); the
DESCRIPTION is wrong. LIVE CONSEQUENCE: the second parity break — the
ceiling arm reads that corpus, codex arms do not, on the very axis
§6b names the ceiling arm the instrument for.

BYTE FIGURE, corrected post-close and recorded with its label because
a figure in a record is a label over a body: **153,966 bytes** is the
SNAPSHOT the probe children loaded and is the figure this finding
rests on. **155,111** is the LIVE corpus as of 2026-09-14 ~18:15 and
will drift again — two modules were edited at 17:58 and 18:11, after
the probes ran. This desk first reported the live figure against a
claim about the snapshot: a different object, verified and reported as
agreement.

**S5 — §5d's freeze order OMITS the driver re-run §3a.4 mandates, and
the named tool cannot be aimed at anything.** `driver_resume_probe.py`
has no argparse: model hardcoded, both prompts and invocations
literal. Contrast the sibling's `--launcher-file`. The eve review's S3
class (a freeze step unexecutable as written) recurring INSIDE the
section written to close it.

**S6 — §3a.4, §6d and §10 disagree in ONE contract about whether arms
may dispatch.** §3a.4: "SUBSTRATE FOUND AND MEASURED… closed",
"DISCHARGED at registration". §6d, unamended: "THE SUBSTRATE CHOICE IS
OPEN… precondition (1) is NOT discharged, and no arm dispatches." §10
agrees with §6d. A freeze executor reading one proceeds; reading the
other, stops. Caused by this desk editing §3a.4 and leaving its
dependents stale. A reconciling reading exists — §3a.4 answers the
CEILING arm only, codex's axis staying unmeasured — but the document
never states it, and §3a.4's claim is the wider one.

**S7 — §5a pins a lifecycle sha and no step verifies the clone carries
it**, in a document that added a resolved-path verifier to §4a for
exactly this reason ("a config write reads as done without being
done"). §5c's `--depth 1` takes the branch TIP at clone time, not a
pinned sha, and this desk writes to that repo through the lifecycle
verbs between the two steps. Current state verified, so this is a
design gap and not a live failure: lifecycle HEAD is still 2b41491.

**S8 — §5c's scrub EDITS the clone and the document never says whether
that edit is COMMITTED.** Uncommitted: the arm's first `git status`
shows exactly what was removed — strictly worse than the blanked slot
§5c forbids, because it also names the location. Committed: the
depth-1 clone's single commit is a freeze-day scrub commit under the
executor's name. The HISTORY half was closed structurally; the
working-tree-state half was left unnamed.

---

## MINOR

**M1** — §3a.2 cites "(§2b of the grading)" for terra's death; grading
§2b is one line about column 2b and says nothing about terra. The
substance IS supported, by grading §3, §0a, §5's C5 row and st-64's
amended-evidence. Pointer only.

**M2 — a FAIRNESS correction, not a pointer fix.** §3a.2 does not
carry that run 2 graded terra's stop as **C5 CORRECT CONDUCT** under
the operator's standing ruling, nor its column-3 PASS-thin. The arms
section reads terra's run-2 outcome as unqualified failure. Combined
with B3, the entire rationale for including terra is wrong twice over:
the gate does not catch its defect, and its death was not a conduct
failure.

**M3** — cross-document citation ambiguity: §3a's header cites "run 2's
own record — its §8 verdict and §§17/17a", but §8 lives in the GRADING
while §§15a/15c/15e/17/17a live in the PRE-REGISTRATION, and both
carry §§1-8. Name the file per citation.

**M4** — (a) §3a.3 attributes a quote-axis claim to §8.2(b); it is at
grading §4c. Both claims check out, only the pointer is off. (b)
§3a.5's "plus a ceiling arm if a substrate is found" is stale against
§3a.4's RESOLVED — and is the same sentence B2's parity claim builds
on.

**M5 — THE OPERATOR'S, and not this desk's to settle.** The pin says
operational issues "shouldn't be keeping us from grading any models";
§3a.4 renders the protection as "never a reason to drop sol, terra or
astra" — excluding the CEILING arm — and then offers "run with the
certification consequence named", i.e. dropping the ceiling arm for an
operational reason, as a live option. **The document decided the pin's
scope silently, in the section whose whole subject is an operational
dead end.** Surfaced to the operator by statiker-e8, first-hand;
nothing in this arc acts on it.

---

## WHAT HOLDS — executed, recorded so the clean half is not invisible

- **The two probes are CONSISTENT** and the boundary is stated
  correctly: one measures a single UNAIDED invocation (confirmed at
  the code, one `_run(launcher…)` per leg), the other adds an external
  re-invoker. Different objects, no contradiction. What is imprecise is
  WHICH probe applies at the gate (S5/S6).
- **The M1 containment arm is RED-FIRST PROVEN by the reviewer**, not
  accepted from its docstring: mutating `_abs_repo_relative` reds that
  arm ALONE (1 failed / 34 passed), and nothing else in the class
  covered the convention.
- **The OBSERVATIONS release-gate record discharges the eve review's
  BLOCKING** — C4b call fail-closed with the contrary reading stated,
  all nine tenets marked individually, carried-set re-ask recording two
  mints and reasoning four non-mints.
- **The PROBE_INCONCLUSIVE battery is sound** — precedence re-derived
  from the shipped `verdict()` rather than read off the assertions.
- **The sol pin is quoted and relayed correctly** — marked as a relay
  not typed in the receiving session, with the first-hand delegation
  that makes it binding named. Its one silent narrowing is M5.

## BOUND ON THIS ROUND, as the reviewer stated it

It graded the delta and the pre-registration. It did NOT re-review
banked findings, did not read the run-2 arm archives, and made no
claim about the lifecycle repo beyond its current HEAD sha. Its one
inference not backed by an execution is S3's "a fresh child COULD
reach the nonce on disk" — the persistence is measured, the hunting
behaviour is not, and it graded S3 on that basis rather than claiming
the green was false. It named the false zero that bit it (a line-based
grep over the hard-wrapped corpus) and the normalised re-run that
answered it.

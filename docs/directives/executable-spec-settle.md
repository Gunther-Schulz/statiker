# Executable-spec settle — record-grammar semantics (release 0.2.49+)

Consumer: the parser+battery build dispatch (primary), then any
successor session grading the build or the reduced SKILL.md.
Provenance: form question answered 2026-08-08 (dev-notes/
OBSERVATIONS.md, FORM QUESTION ANSWERED entry) after the 5B→7B→7B
concentrated-blocker series across design-attack rounds R1–R3;
review rounds are HELD by operator decision — the red-first battery
is this release's instrument, not a review round.

## The form decision

The record grammar / lint / repair semantics are DESIGNED as an
executable spec: the reference implementation
(`plugin/skills/statiker/scripts/statiker_record.py`, plus the
containment seams of `statiker_git.py`) and its red-first battery
(`tools/test_statiker_record.py`, `tools/test_statiker_git.py`) are
the contract. Normative order on divergence: this settle's
decisions > battery > implementation > SKILL.md prose. SKILL.md
prose reduces to principles and never decides machine semantics
(single-home is untouched: SKILL.md stays the only operational
text; what changed is design ORDER, not homes).

Red-first arrangement (binding on the build): new battery cases are
written FIRST and executed against the UNMODIFIED scripts at the
build's base commit — each case must go red there, the red list
pasted in the report with the arrangement named (which side was
old, where the expectations came from) — then the implementation
turns them green. Never revert working state to manufacture a red.
Each new case carries a provenance comment naming its seed
(R3-B1 … R3-B7, R1-B<n>, R2 seed, ES-<n>).

## Settled semantics

ES-1 **Head-region exclusion binds ALL of surface 1** (R3-B3).
The requirement-head region — file start to the first `## ` heading
— parses NO entries: not the exact head, not the near-miss scan,
not the signature scan. An operator bullet `- V2 ...` inside INTENT
is prose; it cannot brick the closure gate or mint a phantom entry.
Quoted lines (leading `>`) carry the same exclusion everywhere.
Status/Phase header parsing and whole-file defang lint are
untouched. Red case: `- V2 <text>` in the head region — old code
parses a V-entry (and lints tag-enum on it); new code parses
nothing and lints nothing there.

ES-2 **Late INTENT lines are machine-findable** (R3-B2). The
labeled form is settled as the literal `INTENT: ` opening a line
below the head region (detection wider: case/colon slips of a
leading intent-token lint as near-miss). `sweep` and `closure`
verdicts carry a `late_intent` field listing line numbers of the
labeled lines. Verify-brief composition (prose, principle level)
grades against the head PLUS every late_intent line the verdict
lists — the tool, not memory, is what finds them. Red case: late
`INTENT: ...` line present, old sweep verdict has no late_intent
field.

ES-3 **Filter artifact is pure; alignment by construction**
(R3-B1, supersedes the 0.2.46 header definition). The filter
BLANKS the two Superseded species in place — every dropped line
becomes an empty line, so artifact line numbers equal source line
numbers with no offset — and emits NO header lines. Source path,
pinned sha, and the blanking declaration travel as
ARTIFACT_WRITTEN verdict fields (`source_tracker`, `sha`,
`blocks_blanked`, `sections_blanked`, `lines_blanked`, plus a
`form` note stating the blanking), which the attack brief quotes
beside the artifact. Entry-shaped lines inside a Superseded
SECTION are preserved on their own line numbers. Red case: a
`corrects line <n>` token below a blanked block dereferences to
the same text in artifact and source — old code compacts (drops
lines), so the case goes red there.

ES-4 **Repair pins everything that PARSED on the target** (R3-B4).
Supersede-whole restatement carries the target's tag where the tag
parsed (0.2.48, kept) AND the target's scope class where the scope
opener parsed: a scope change through repair lints as its own
violation (`repair-scope-change`), exactly like a tag change.
Where the violated token IS the scope opener, scope is unparseable
and the restatement's scope is free by construction; the danger
direction (a meant-void [INVALIDATED] line restated scoped,
converting void into dispatch) is held by the existing closure
rule — a post-closure [INVALIDATED] line for an entry live at the
closure voids WHATEVER its opener — and the battery pins that
path explicitly. Red cases both directions.

ES-5 **Chain semantics: no re-carry; one token per line holds**
(R3-B5). Supersession is computed in one pass over the ORIGINAL
entry set (existing mechanism), so a token acts whether or not its
carrying line is later superseded: a superseded correcting line's
own supersession of ITS target persists. Therefore the restatement
of a superseded correcting line carries exactly ONE token — the
one naming the line it corrects — and restates the dead line's
content WITHOUT its machine token. The 0.2.48 re-carry clause is
dead. Red case: chain 10←20←30 — line 10 stays superseded, line 30
carries one token, no multi-token lint fires.

ES-6 **Own-id targeting admits id-unreadable targets** (R3-B6).
A `corrects line <n>` token reaches: (a) an earlier violated line
naming the correcting line's OWN id (parsed or near-miss-named);
(b) an earlier violated line naming NO readable id — the
id-misspelling class the token was built for; the correcting
line's id claims it. A violated line readably naming a DIFFERENT
id stays barred (the forgery direction) and lints
corrects-nothing with the cross-id reason. Token line numbers
compare as integers (leading zeros are not a separate address).
Red case: id-mangled violated line (no id readable), correcting
line under the intended id — old code lints corrects-nothing
("names no entry"), new code supersedes/sheds per site.

ES-7 **Must-be-inside containment is decided on the REAL path;
as-named is the operating spelling** (R3-B7; both tools). The
ancestor probe is NAMED: walk to the path's nearest EXISTING
ancestor; the path is inside the repo only when that ancestor's
realpath sits inside (or equals) the repo top's realpath. A path
that is named inside but resolves outside (an in-repo symlinked
directory pointing out) HALTS before any write rests on it; a
path reached through a symlinked ancestor OF THE REPO TOP resolves
inside and is accepted, re-rooted textually (attack-10 N4,
preserved). The operation still runs on the as-named spelling;
`resolved_from` (named and real form) is noted per path in the
verdict whenever the two differ. An EXISTING leaf that is a
symlink halts at every path-accepting seam (write-set, lock-set;
the filter's tracker islink halt stands). MUST-BE-OUTSIDE paths
(artifact, seals) are outside only when BOTH computations agree —
the filter's --out check gains the as-named half (current code
checks only the real side). lock-check DRY-RUNS its adds so a
contained path git refuses surfaces at the check; the
rel-None-with-top-present message states the true causes (the
0.2.44 one-cause comment is disproven). Red cases: in-repo
symlink-dir write-set path (old: accepted; new: halt with
resolved_from evidence); --out through a link into a repo (old:
accepted when realpath parent is outside a repo — construct the
converse: named outside, real inside a repo — old accepted only
checks real, build constructs the direction that goes red).

ES-8 **Positional lint surfaces land in code** (0.2.48
definitions; R2 stem-match seeds as negative cases). Hold
classification is POSITIONAL: the token after `unit U<k> ` —
case/colon/plural variants of held/hold short of the literal lint
as hold near-miss; the colon forms opening any body or displaced
later into a unit-scoped body lint as displacement; the bare
colon-less word anywhere is prose; backtick-quoted text is exempt.
The word-search (`HOLD_WORD_RE`) dies. The signature scan (surface
1): an id token with an ADJACENT tag literal (bracketed or bare
enum word) under any bullet lints entry near-miss — no opener or
bullet enumeration — with the ES-1 exclusions. One token per line:
a multi-token corrects line lints as its own violation. Negative
cases (must NOT fire): prose "held" outside unit scope,
"withheld:", backticked `held:`, `record the verdict`, `unit tests
pass`, numbered INTENT items in the head region.

ES-9 **Byte policy extends to the EMIT direction** (0.2.46 N6;
R1-B5 JSON re-spelling; R2-B6's refuted probe settled the
mechanism). Verdict lines and quote output emit at the byte
level — encoded with surrogateescape over the input's own bytes
(stdout.buffer), ensure_ascii=False — so a non-UTF-8 byte quoted
in a violation or a quote block round-trips byte-identical.
`cmd_quote` decodes stdin with surrogateescape (the current
`errors="replace"` mangles before defang). The blanket
`reconfigure(errors="replace")` must not re-spell verdict/quote
bytes. Red case: tracker body byte `\xff` appears in a violation
text and in a quote block byte-identical on output.

ES-10 **The verdict names each violation's class and repair form**
(0.2.48). Every violation dict carries a `repair` field computed
from the violation SITE: machine-token violation →
"supersede-whole: restate under the same id with `corrects line
<n>`; tag and scope re-carried where they parsed"; body-content
violation → "bookkeeping: append `- <id> [<tag>] record: corrects
line <n>` — sheds violations only, status untouched". The desk
composes from the verdict, never from memory. Battery asserts the
field per class.

ES-11 **Git-tool residue from the 0.2.46 code-only list** (attack-
11 N5/N8 and dispositions): unfreeze ADD_FAILED and GIT_ERROR
using the attacker's recipes as battery rows (in-repo symlinked
dir + staged rename for ADD_FAILED; corrupt index for GIT_ERROR —
and preflight's DEDICATED repo-health read is STRICT so a corrupt
index halts at run start while every other read keeps its
documented exit semantics); IsADirectoryError at --out routes
USAGE_ERROR (consistent with its sibling); a staged RENAME's drop
excludes BOTH halves from effective+adds; the frozen remainder
shrinks accordingly, each surviving entry still carrying its
reason.

## Case seeds beyond the settled items

R1 blockers (dispositions landed 0.2.47, prose-era — re-expressed
as battery rows where the surface exists): opener lint silently
dropped; signature over-reach into quotes/INTENT; containment
trigger topology backwards; parsed-branch defang permanence; JSON
re-spelling. R2 booked seeds: stem-match false-fires (ES-8
negatives); token composition deleting entries cross-id (ES-6
barred direction); sweep pointer detonating closures; retry bound
vacuous (assert the git tool's capped spaced retry actually bounds
attempts). Where a booked seed has no surface in the settled
semantics, the build names it residue in the report rather than
inventing a surface. The R1–R3 REPORTS are lost (in-transcript
only, dead lanes) — the booked lists in dev-notes/OBSERVATIONS.md
are the whole seed set.

## What the build does NOT decide

Any gap — a case two settled items decide differently, a semantics
question this file does not answer — is REPORTED, never bridged
(executor discipline). SKILL.md is not in the build's write-set:
the desk reduces the prose separately against this settle.

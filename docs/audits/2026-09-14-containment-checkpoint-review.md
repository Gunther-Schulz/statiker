# Checkpoint review — preflight containment gate (st-74/st-64), bbbe52f..afef58b

REVIEWER VERDICT: **PIN HOLDS** — 1 BLOCKING, 2 SUBSTANTIVE, 5 MINOR.
Fresh-context opus lane, read-only, brief carried the delta + the full
page + the question and none of the author's reasoning.

Reviewer's own closing bound, carried forward as stated: its clearance
is **could-not-verify until the repaired suite is run**, not a clean
verdict handed forward. The repair lap's own suite run is what clears
this, never this review.

Reviewer's verify: `python3 -m pytest tools/ -q` → 612 passed, 2
subtests passed, 0 failed, 0 skipped, 35.55s. Reproduces the desk's
own run at HEAD. Mutation probes ran against a scratch COPY in its own
scratchpad; that copy carries 2 pre-existing subtest failures
(golden-corpus fixture paths not copied out), constant across every
arm, so its mutation results are FAILED-line deltas rather than
absolute counts — disclosed by the reviewer, and it is what makes them
readable.

---

## BLOCKING

**B1. The worktree-parent axis decides on realpath only, losing the
as-named half.** statiker_git.py:1298 is fed `scope_reals` (:1283),
which realpaths every declared scope, so `enclosing_repo`'s
`textual_repo_top` walk never sees the operator's spelling.
`Repo.outside` — the sibling caller — passes the AS-NAMED parent.

Executed discriminating pair (reviewer): with `link-out ->
<outside>`, `preflight --containment <repo>/link-out` fired NO
worktree-parent axis — preflight called the scope satisfiable — while
`worktree-add --path <repo>/link-out/wt` returned PATH_INSIDE_REPO
(halt) with both spellings in `resolved_from`. Control on a genuinely
outside dir: no axis, WORKTREE_ADDED. So every path under that scope
is refused at attack preparation while preflight passed it — the exact
cost this item was minted to remove.

Two page sentences falsified, both read by the reviewer: SKILL.md:65-70
("outside only when named and real form agree") and SKILL.md:237-238
("the gate establishes that a legal parent EXISTS in scope").

**DISPOSITION: FIX**, as specified — `enclosing_repo(_abs_repo_relative(...))`
over `args.containment` at :1298, proven non-breaking and discriminating
by the reviewer, plus the two arms it names. The defect is the DESK's
design sentence, not the lane's build: the design said "lies outside
every repo" and never specified named-versus-real while the page's own
containment principle does. The lane implemented what it was given.

---

## SUBSTANTIVE

**S1. `_within_any` (statiker_git.py:1217) has no arm — the
prefix-match defect survives the whole suite.** Mutating
`startswith(s + os.sep)` to `startswith(s)` → 0 FAILED across all 612.
Proven reachable, not a dead mutant: scope `<dir>/scope` with
`core.hooksPath=<dir>/scope-evil` — shipped code fires the hooks-path
axis, the mutant does not, accepting a sibling directory as covered.

**DISPOSITION: FIX (add the arm).** The shipped code is CORRECT; this
is an instrument gap, recorded as such. It sits in the one defect class
the corpus names by name — a prefix match in an equality's costume —
and a lone green there is indistinguishable from a blind spot.

**S1 DISPOSITION CORRECTED, reviewer's POST-CLOSE report (msg a6be5560),
after its lane had closed.** The disposition above said "the arm",
singular, and specified the hooks-path case only. `_within_any` is the
predicate behind BOTH the hooks-path axis (:1290) AND the
out-of-repo-namespace axis (:1293-1296), so the singular arm leaves the
namespace axis uncovered by the same defect — a declared scope
`<x>/statiker` against a namespace base under `<x>/statiker-other`
reads as covered under a bare `startswith`. The bare-prefix mutation's
zero reds covers both axes, so NEITHER is certified today.

CORRECTED DISPOSITION: an arm per axis, or one arm plus a recorded line
that the predicate is shared and certified once at function level.
Whichever form, the bare-prefix mutation must red it.

The error was the DESK's: it was written into the disposition and
inherited by the repair-lap brief, which went out carrying it. The
reviewer caught it about a record it had already been closed against,
and REPORTED rather than edited, which is the correct post-close act.
The desk's correction reached the live lane as a state-dependent
directive; a send is acceptance and not delivery, so the remainder is
the desk's at integration either way.

**Reviewer's own correction to this record, same message:** its "no
release action" note on M3/M4/M5 was unsound on its own arithmetic —
booking each costs about what fixing it costs. The desk's decision to
fix all three stands on that arithmetic, not on overruling the
reviewer. Recorded so the file does not carry the reviewer's reasoning
as sound where the reviewer itself withdrew it.

**S2. The gate accepts by realpath without recording `resolved_from`.**
SKILL.md:70 requires "any realpath acceptance noted per path in the
verdict as `resolved_from`". Executed: a scope declared through a
symlink clears the hooks-path axis and the verdict carries only
`containment`, no `resolved_from` anywhere in the JSON. `worktree-add`
honours the convention.

**DISPOSITION: FIX by RECORDING, not by exempting.** The convention
exists so a later reader can audit an acceptance made on a resolved
path, and the sibling mechanism keeps it; an exemption here would be a
special case with nothing behind it.

---

## MINOR

**M1. The page's coverage-boundary claim is wider than the code.**
SKILL.md:236 says "every containment-declared verdict"; executed, the
PREFLIGHT_UNPINNABLE_TRACKER path carries no `containment`, no
`unchecked_axes`, no `hooks_path`, no `out_of_repo_required`. The code
comment at :1253 says "every PREFLIGHT_OK".

**DISPOSITION: FIX by NARROWING THE PAGE.** The unpinnable path is the
more fundamental refusal and the run cannot proceed through it, so
containment fields there would be noise. Recorded with its class: this
is the SECOND instance in one delta of prose claiming more than the
predicate establishes (B1's second half is the first). Two instances is
a pattern, not a slip, and the desk wrote both.

**M2. `TestEnclosingRepoHelper` is the one class not insulated by
construction.** It calls `enclosing_repo` IN-PROCESS; the git
subprocesses that function spawns pass no `env`, so they inherit the
session's real environment and this machine's real git config. Its own
`git init` calls do use `hermetic_env`. Three arms, reading nothing
config-sensitive.

**DISPOSITION: FIX, test-side** (patch the environment for the
in-process call). Low consequence as graded, but this machine's global
`core.hooksPath` is exactly the state such a leak imports.

**M3. `--containment ""` silently means the repo root** and is echoed
verbatim into a verdict the desk books as an F-line.

**DISPOSITION: FIX** — reject empty with USAGE_ERROR. A silent
coercion inside a containment declaration is the wrong default.

**M4. The repo-root-relative convention (`_abs_repo_relative`,
:1207-1214) has no arm.** Probed working: `--containment .` resolves to
the repo root and fires worktree-parent correctly.

**DISPOSITION: FIX (add the arm).**

**M5. Linked worktree: `hooks_path.inside` is False by construction**
— executed from a linked worktree, path `<main>/.git/hooks/pre-commit`,
`inside: false`, `worktree: true`. Defensible, untested.

**DISPOSITION: FIX (add the assertion).** Documents the behaviour
rather than changing it.

M3/M4/M5 are fixed against the reviewer's "no release action" note:
each costs about what booking it would cost, and a deferral whose
arithmetic does not work is a deferral refuting itself.

---

## WHAT HOLDS — executed, recorded so the clean half is not invisible

- **Where the desk told it to press came back CLEAN.** Registry
  enumerated programmatically against the page: 77 entries, 26
  multi-location. The delta's three verdicts are each named at exactly
  ONE page location, so the fail-closed floor's tiebreak never engages.
  The seam that describes the new verdict without naming it
  (SKILL.md:207-208) AGREES with its token and supplies the unattended
  disposition the new passage omits. None of the 26 is touched.
- **Axis discrimination: each axis red on its own defect, each control
  green, every mutation producing a distinct FAILED set.** No assertion
  satisfied by both the correct and the defective behaviour.
- **All three must-not-move controls hold AND each has a mutation that
  reds it** — including MNM1 (no `--containment` → never a hold, on a
  repo whose hooks resolve outside), which the reviewer independently
  confirmed is load-bearing by re-probing this machine's global
  `core.hooksPath` in a fresh repo.
- **Same-parentage check, run UNPROMPTED.** B1/B2 assert against the
  verdict's own reported field. The reviewer closed the chain: mutating
  the underlying `seal_namespace_roots` reds TestSealPath's arms, which
  derive the bases from first principles rather than by calling the
  tool under test; mutating only the reported field reds B1+B2. Field
  and derivation cross-check, derivation independently pinned.
- **Reach detector live over the new token** — the battery row DRIVES
  the verdict rather than freezing it, confirmed by a HOLD→OK mutation
  reddening both parity arms.
- **The page's hooks-resolution claim substantiated** — git 2.55.0
  honours `core.hooksPath` AND expands a `~` in it.
- **The version bump does not regress the retro gate.** 0.2.100 is the
  first three-digit patch in the series; the only comparison site
  (`_version_tuple`, statiker_record.py:371) splits and int-converts,
  so (0,2,100) > (0,2,99). A string sort would have inverted it. The
  desk chose that number WITHOUT checking; the reviewer checked
  unprompted, and the version-sort-by-string-order hazard is named in
  the operator corpus.
- **C4b bar met** — the OBSERVATIONS entry enumerates all nine PLAN
  tenets individually against the live list at PLAN.md:43-75.

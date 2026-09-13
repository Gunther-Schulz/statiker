# The Grokbot space — poteto's orchestration line vs this stack

**Date:** 2026-09-13. **Occasion:** operator ask at the statiker desk
(session 1b204567): Grokbot "lives in the same space but a completely
different approach — I would be interested in a comparison."
**Comparands read:** brainmaxxing (poteto, FULL read, HEAD ec4d8e4,
2026-02-27) and noodle (poteto, spine + graded inventory, HEAD
82d2921, 2026-03-19), both mirrored at ~/dev/reference; Grokbot
itself is source-unreadable (see bounds). **Raw evidence:** the lane
reports in this session's transcript; the inventory and web findings
archived at `dev-notes/noodle-inventory-2026-09-13.md` and
`dev-notes/grokbot-surface-2026-09-13.md`. **Consumer:** the stack's
positioning record (PLAN), ethos/lifecycle design items, and any
future orchestration-engine question.

## Bounds, first

Grokbot's source is private (Cursor's monorepo; her benny-avatars
repo names anysphere/everysphere). The public web surface for the
name is CONTAMINATED: cursor.com claims it, an x.ai page claims it
for "SpaceXAI LLC", and the search corpus is thick with content-farm
churn recombining real names. The web lane refused to launder that
into a narrative — correct. What Grokbot IS therefore rests on the
author's own talk (primary, archived here) plus the one coherent
docs page: a Cursor product, launched ~2026-09-12, multi-agent
orchestration — "AI teammates with names, jobs", messaged per task,
that "come back when something needs your approval". Dune is the
codename of its architecture ("Next.js for Electron apps, designed
for agents to write"). Nothing deeper is establishable from outside.

Noodle's read was the pre-registered pilot lap: spine in full, the
rest graded by inventory. Its honest doctrine surface is ~150-200
files, not the raw 678 (brain/archive holds 351 historical plans; a
vendored skill-creator tree is duplicated). A full second lap is
sized and available; it runs when a consumer names itself.

## The lineage frame (inference, graded on commit dates)

brainmaxxing (last commit 2026-02) and noodle (last commit 2026-03)
predate pstack's publication era (guides 2026-08/09) and Grokbot's
launch (2026-09). Read as a line: brainmaxxing = personal memory
prose; noodle = the orchestration engine, mechanized; pstack = the
method distilled as a plugin; Grokbot/Dune = the production product
on a hard-gated architecture. Both early repos look dormant since
spring. This is inference from dates, not a verified biography.

## Noodle vs the dispatch model — the sharp contrasts

Noodle is the mechanized twin of this stack's orchestration layer.
A Go event loop advances order stages mechanically; "No LLM runs
between stages". Orders are decision-complete specs persisted to
disk before dispatch — structurally our brief. Cooks run in
isolated worktrees, never the primary checkout; the escape hatch is
a typed field (`AllowPrimaryCheckout bool`). One writer per copy is
enforced by construction where we hold it as convention plus gates.
Live mid-flight steering is a first-class interface — where our
mailbox measurably cannot steer.

The other direction is just as sharp. Noodle has NO closing report:
completion is a four-field status enum, integration auto-merges on
stage success, and the happy path crosses no judgment gate. Every
epistemic artifact our report form carries — dispositioned skips,
unverified residue, provenance-graded claims — has no home in its
loop. Judgment appears only upstream (the pre-written order) or on
failure. Its auto/supervised/manual dial is statiker's Mode as a
product knob — with auto meaning merge-without-anyone-looking.

## Brainmaxxing vs the lesson-capture layer

Same shape one layer up. Its machinery is real: a SessionStart hook
force-injects the vault index (ethos v1's exact mechanism, working
in the wild); an auto-index hook diffs disk against index so the
pointer file cannot silently drift; `ruminate` retro-mines full
conversation JSONL for lessons never captured live — a genuine gap
in this stack, whose harvest is live-only. Its epistemics are thin:
notes carry no provenance anywhere (no incident, no date — an
advisory "quote the user" is the closest thing); retirement is pure
LLM judgment with zero computed triggers; and the emblem — its
encode-lessons-in-structure principle, ABOUT preferring mechanism
over prose, ships as prose with nothing checking that lessons get
mechanized.

## The convergence evidence (noodle plan 119)

Her own live plan to harden brainmaxxing independently derives three
of this stack's rules: "Bad brain edits compound silently because
every session reads the brain" (why our corpus has an edit gate and
maintenance doctrine); typed edit proposals carrying a base_hash for
staleness detection at apply time (statiker's pin/verify-gate); and
skill evals that must be "binary... not gameable without genuine
improvement" (the discrimination bar). Independent arrival is
evidence about the rules, not about either system.

## Positioning claim, falsifier re-checked

The claim: no compared system puts an independent design-
certification gate in front of an unattended end-to-end run. Noodle
is the NEAREST MISS yet — genuinely unattended end-to-end (auto
mode merges with no human step) — and it has no pre-implementation
design grader: the schedule agent writes orders nobody independent
attacks, and its quality stage reviews COMPLETED work. The claim
survives, sharpened: even this author's maximal-mechanism engine
puts all independence downstream. Same verdict as pstack, same
author, second instrument.

## Standing summary

Her constant across four artifacts is now measured, not surmised:
mechanism-maximal, epistemics-thin, at every layer — typed
boundaries, hooks, engines, hard CI; no provenance, no computed
retirement, no closing reports, independence only after the fact.
This stack's emphasis is the inverse. The two lists are not
symmetrical in kind, and neither is a subset of the other — the
pstack comparison's 9e verdict, now holding across her whole line.

## Steal considerations — gated, no mints today

1. RUMINATE-CLASS transcript mining (retroactive lesson harvest
   over past sessions; the session-search tooling here is the
   substrate). Carrier: a dotfiles item, booked this date.
2. The AUTO-INDEX diff hook (index that cannot silently drift from
   disk). Consider at: lc-93's build (the banner hook is the same
   seam), evidence by pointer, no mint without that build.
3. Typed escape hatches for enforced defaults (the
   AllowPrimaryCheckout shape: the default in the type, the
   exception explicit). Consider at: the dispatch-guards guard
   set's next design pass; the worktree ladder already carries the
   substance.
4. The four-step drop-in INSTALL doc shape (brainmaxxing README).
   Evidence for df-171's ethos v1 packaging; no separate item.

## Confounds

Same author, so convergences are not fully independent across her
own artifacts. The lineage frame is date-inference. Noodle's Go
internals were graded by sampling, not read. Grokbot is a marketing
surface plus a talk. Nothing here measures outcomes on either side.

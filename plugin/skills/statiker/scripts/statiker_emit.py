#!/usr/bin/env python3
"""statiker_emit — the shared byte-level stderr fallback (E-J
extraction, BACKLOG). Both statiker_git.py and statiker_record.py's
closing-verdict stderr fallback must write the payload at the byte
level with surrogateescape fidelity: a text-mode print() cannot carry
a surrogateescape-decoded non-UTF-8 byte through stderr unchanged — it
either raises (strict encoding) or silently mints a second spelling
(errors='replace', the shape statiker_git.py's own reconfigured
stderr took: `caf\\xe9.txt` printed as `caf?.txt`), losing the byte the
desk needed. statiker_record.py's :351-356 was the source of truth
this mirrors; statiker_git.py's own _stderr_fallback carried the
text-mode form until E-J.

Both tools import this after inserting their own directory onto
sys.path (loader-robust: tests import tools by file path, which does
not put the scripts dir on sys.path)."""

import sys


def stderr_fallback(text):
    try:
        sys.stderr.buffer.write(text.encode("utf-8", "surrogateescape") + b"\n")
        sys.stderr.buffer.flush()
    except OSError:
        pass


# st-32 lap B: the route registry. Content copied verbatim from the
# settled design's §§1 and 3
# (docs/directives/2026-09-12-st32-lapB-design-statiker-a5.md) — do
# not re-derive by reading the scripts. Single home for both tools
# (statiker_git.py and statiker_record.py each import this module
# already); each script's `finish()` stamps `route` via one lookup
# against ROUTES, falling back to "unrouted" for a name the registry
# lacks (emission never fails on a registry gap — design §1). A name
# shared by both scripts (PATH_OUTSIDE_REPO, USAGE_ERROR, GIT_ERROR,
# INTERNAL_ERROR) is keyed once and shares one route — all four route
# `halt` today (design §2).

ROUTE_VOCABULARY = frozenset({
    "proceed", "book-and-continue", "repair-from-verdict", "barred",
    "narrow", "halt", "surface", "triage",
})

ROUTES = {
    # ---- git tool (43 emitted names) ----
    # proceed (9)
    "PREFLIGHT_OK": "proceed",
    "STATE_CLEAN": "proceed",
    "SEAL_PATH": "proceed",
    "WORKTREE_ADDED": "proceed",
    "WORKTREE_REMOVED": "proceed",
    "LOCK_CHECK_CLEAN": "proceed",
    "LOCK_COMMITTED": "proceed",
    "UNIT_START_CLEAN": "proceed",
    "UNIT_COMMITTED": "proceed",
    # book-and-continue (4)
    "LOCK_CHECK_DROPS": "book-and-continue",
    "LOCK_COMMITTED_EXTRAS": "book-and-continue",
    "UNIT_COMMITTED_EXTRAS": "book-and-continue",
    "UNIT_COMMITTED_RESIDUE": "book-and-continue",
    # repair-from-verdict (1)
    "LOCK_GATE_HOLDS": "repair-from-verdict",
    # barred (1)
    "STATE_IN_PROGRESS": "barred",
    # triage (1)
    "UNIT_NO_DIFF_VS_HEAD": "triage",
    # surface (1)
    "PREFLIGHT_UNPINNABLE_TRACKER": "surface",
    # halt (26; UNIT_GATE_BLOCKED, BLOCKED_CONTENTION and UNIT_COLLISION
    # moved here 0.2.89 fix — the fail-closed floor, dev-notes/
    # OBSERVATIONS.md "0.2.89 checkpoint-review dispositions")
    "HALT_STATE": "halt",
    "HALT_TRACKER_COLLISION": "halt",
    "HALT_TRACKER_UNPINNABLE": "halt",
    "HALT_DROPS_STALE": "halt",
    "HALT_DROPS_UNACKNOWLEDGED": "halt",
    "HALT_NO_CHANGES": "halt",
    "HALT_NO_PATHSPEC": "halt",
    "HALT_DIRECTORY_PATH": "halt",
    "HALT_MISSING_PATH": "halt",
    "HALT_RESIDUE_PERSISTS": "halt",
    "HALT_IGNORED_WRITESET": "halt",
    "UNIT_START_MISMATCH": "halt",
    "UNIT_COMMIT_COLLISION": "halt",
    "WRITE_SET_NAMES_TRACKER": "halt",
    "GATE_UNREADABLE": "halt",
    "ADD_FAILED": "halt",
    "COMMIT_FAILED": "halt",
    "NOT_A_REPO": "halt",
    "PATH_INSIDE_REPO": "halt",
    "PATH_OUTSIDE_REPO": "halt",
    "USAGE_ERROR": "halt",
    "GIT_ERROR": "halt",
    "INTERNAL_ERROR": "halt",
    "UNIT_GATE_BLOCKED": "halt",
    "BLOCKED_CONTENTION": "halt",
    "UNIT_COLLISION": "halt",

    # ---- record tool (37 emitted names; the 4 shared names above are
    # not repeated here) ----
    # proceed (14)
    "LINT_CLEAN": "proceed",
    "SWEEP_CLEAN": "proceed",
    "CLOSURE_LIVE": "proceed",
    "UNIT_DISPATCHABLE": "proceed",
    "WAVES_COMPUTED": "proceed",
    "TREND_COMPUTED": "proceed",
    "TREND_NO_ROUNDS": "proceed",
    "SUSTAIN_OK": "proceed",
    "SUSTAIN_NOT_APPLICABLE": "proceed",
    "TRIPWIRE_SILENT": "proceed",
    "ARTIFACT_WRITTEN": "proceed",
    "PINNED_APPEND_ONLY": "proceed",
    "VERIFY_COPY_CLEAN": "proceed",
    "QUOTE_BLOCK": "proceed",
    # repair-from-verdict (8)
    "LINT_VIOLATIONS": "repair-from-verdict",
    "SWEEP_HOLDS": "repair-from-verdict",
    "CLOSURE_RECORD_MALFORMED": "repair-from-verdict",
    "CLOSURE_LEAVINGS_HOLD": "repair-from-verdict",
    "WAVES_RECORD_MALFORMED": "repair-from-verdict",
    "TREND_RECORD_MALFORMED": "repair-from-verdict",
    "SUSTAIN_RECORD_MALFORMED": "repair-from-verdict",
    "TRIPWIRE_RECORD_MALFORMED": "repair-from-verdict",
    # barred (4; SUSTAIN_DENIED moved here 0.2.89 fix, B1 — NOT the
    # fail-closed floor: the floor breaks ties among a verdict's
    # differing SEAM dispositions, and SUSTAIN_DENIED has exactly one
    # (the never-sustain round-open gate, SKILL.md "sustain returns
    # SUSTAIN_OK / SUSTAIN_DENIED ..."). `narrow` was simply wrong —
    # the gate closes design, it does not re-scope the head — and the
    # gate's own shape is barred's: the tool ran, the denial is
    # computed from run state already in the record, and the page
    # books it by quoting the verdict in the round-open line rather
    # than as an F-line. dev-notes/OBSERVATIONS.md "0.2.89
    # checkpoint-review dispositions" and the 2026-09-12 desk ruling)
    "CLOSURE_ABSENT": "barred",
    "CLOSURE_VOID": "barred",
    "UNIT_HELD": "barred",
    "SUSTAIN_DENIED": "barred",
    # narrow (1)
    "TRIPWIRE_FIRES": "narrow",
    # triage (1)
    "VERIFY_COPY_STALE": "triage",
    # surface (1)
    "PINNED_REWRITTEN": "surface",
    # halt (8; 4 of these — PATH_OUTSIDE_REPO, USAGE_ERROR, GIT_ERROR,
    # INTERNAL_ERROR — are keyed above from the git tool's list)
    "UNIT_UNKNOWN": "halt",
    "ARTIFACT_IN_REPO": "halt",
    "PIN_UNREADABLE": "halt",
    "TRACKER_UNREADABLE": "halt",
}

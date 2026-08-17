#!/usr/bin/env python3
"""Stop hook: block an improvised desk turn-end against a live statiker
tracker — the operator's own midturn-answer-check pattern, aimed at
statiker desks (BACKLOG.md P16).

Incident this closes (dev-notes/OBSERVATIONS.md, 2026-08-16, two desks,
same seam — "b7 post-A1" and "cd post-A2"): a report was delivered, the
turn ended, desk work was owed (a design REOPEN's cycle re-derivation),
and no rule stood behind the stop — prose alone ("a report is no
terminus", SKILL.md) under-bound it twice under the unattended
directive's own momentum. SKILL.md's turn-end passage (as revised,
0.2.81) enumerates the legitimate stops; this hook is the mechanical
half of that same enumeration, read off the RECORD rather than trusted
to conversation:

    fire  = Mode unattended
            AND last A-line terminal (not [DISPATCHED] awaiting return)
            AND the PENDING blocking set is not SOLELY one
                operator-authority-marked [PENDING]
    silent otherwise — including: no live tracker at all, Status not
            `in-progress`, Mode attended, last A-line [DISPATCHED], or
            the blocking set is empty or solely one operator-authority
            [PENDING] (an authority-gated close: SKILL.md ~L328-334 —
            "An ask on OPERATOR-AUTHORITY ground... lands as an
            ordinary [PENDING] entry").

DESIGN NOTE — the operator-authority marker. The record grammar gives
operator-authority asks no dedicated bracket tag: SKILL.md is explicit
that such an ask "lands as an ordinary [PENDING] entry under its own
id" (line ~331), indistinguishable by tag from any other open
question. The only structural feature the grammar promises is that its
BODY names the gate it blocks. Absent a dedicated tag, this hook
detects the case-insensitive literal "operator-authority" (also
"operator authority") in the entry's body — the term the corpus itself
uses everywhere else to name this exact category (SKILL.md L328,
dev-notes 2026-08-16 "no operator-authority pending as sole hold",
this BACKLOG entry's own wording). This is an IMPLEMENTATION CHOICE
inside the settled design, not a re-design: flagged here for the
checkpoint review since it invents a body-text convention the grammar
does not itself mandate as a literal marker.

Predicate ALWAYS reads the RECORD (the tracker file), never
conversation state — the exact discipline the incident was missing.
Fail-open on every parse error: a malformed tracker never blocks a
stop, it prints a warning to stderr instead (never stdout — stdout
carries only the hook's JSON decision, and empty stdout is a silent
pass).

Schema, derived from the harness's own source (not the reference
dispatch-guards plugin, which ships no blocking Stop hook to derive
from — every one of its Stop/SubagentStop lanes only warns or injects
additionalContext, so the brief's preferred source has nothing to
read the schema off): `~/dev/reference/claude-code`
`src/utils/hooks.ts`, `processHookJSONOutput` — the `decision`/`reason`
pair is handled as a COMMON element for every hook event, not scoped
under `hookSpecificOutput` (that nested form is PreToolUse/
PostToolUse/UserPromptSubmit-only, per the same file's schema-hint
block). `decision: "block"` sets `permissionBehavior = deny` and
`blockingError.blockingError = reason` unconditionally; `src/query/
stopHooks.ts` then wraps it as a hidden user message via
`getStopHookMessage` ("Stop hook feedback:\n<reason>") and sets
`preventContinuation`. So a Stop-hook block is:
    {"decision": "block", "reason": "<message>"}
top-level, exit 0. No `hookSpecificOutput` wrapper, no
`permissionDecision` field (those govern PreToolUse only).

Not gated on `stop_hook_active` (unlike report-enforcer.py's
injection nudge, which must fire exactly once to avoid an
additionalContext re-fire loop — docs: additionalContext "keeps the
subagent running"). A `decision: block` is not an injection; the
harness re-invokes the model with the reason as feedback and there is
no re-fire loop to break — the desk is expected to keep hitting this
block until the record's own state changes (cycle re-derived, a new
A-line lands, Status leaves in-progress, or an operator line clears
the hold), which is the entire point: the guard is deliberately
non-idempotent against a session that tries to stop again in the same
state.

Fail-open everywhere (a broken guard must never brick a stop).
`--test` bite-test registered via the doctor's content scan (repo
convention, dispatch-guards `hooks/*.py` carrying `--test`).
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

_SOURCE = "statiker/stop-guard"
_TRACKER_GLOB = os.path.join(".clippy", "runs", "*-statiker.md")

_A_LINE = re.compile(r"^- A\d+\s+\[([A-Z-]+)\]")
_ENTRY_LINE = re.compile(r"^- ([A-Z]+\d+)\s+\[([A-Z-]+)\]\s?(.*)$")
_STATUS_LINE = re.compile(r"^Status:\s*(\S.*?)\s*$")
_MODE_LINE = re.compile(r"^Mode:\s*(\S.*?)\s*$")

_TERMINAL_A_TAGS = frozenset({"BIT", "ZERO-DELTA", "VOID"})
_AUTHORITY_MARKERS = ("operator-authority", "operator authority")


# ── Record reading ──────────────────────────────────────────────────

def find_trackers(cwd: str) -> list[str]:
    """Every `.clippy/runs/*-statiker.md` path under `cwd`, sorted for
    determinism. Absence is a normal, silent case — most sessions carry
    no live statiker run."""
    return sorted(glob.glob(os.path.join(cwd, _TRACKER_GLOB)))


def header_field(text: str, pattern: re.Pattern) -> str | None:
    """The FIRST line matching `pattern` — the header's own field is
    written once and updated in place (SKILL.md: "the header's Status
    and Phase fields... everything below them is append-only"), so the
    first match is always the live one; a later false-positive line
    deeper in the body (unlikely given the anchored `^Status:`/`^Mode:`
    form, which prose paragraphs do not open with) still cannot outrank
    it."""
    for line in text.splitlines():
        m = pattern.match(line)
        if m:
            return m.group(1)
    return None


def last_a_line_tag(text: str) -> str | None:
    """The tag of the LAST `- A<n> [TAG]` line in file order — the
    record is append-only, so file order is round order."""
    tag = None
    for line in text.splitlines():
        m = _A_LINE.match(line)
        if m:
            tag = m.group(1)
    return tag


def blocking_set(text: str) -> dict:
    """{id: body} for every entry id whose LATEST line's tag is
    PENDING — the sweep's own "no entry's latest line is [PENDING]"
    gate (SKILL.md), read directly rather than reimplemented: this
    walks every `- <ID> [TAG] <body>` line in file order and keeps only
    the latest tag per id, mirroring the append-only record the same
    way the record tool's own sweep does."""
    latest: dict = {}
    for line in text.splitlines():
        m = _ENTRY_LINE.match(line)
        if not m:
            continue
        ident, tag, body = m.group(1), m.group(2), m.group(3)
        latest[ident] = (tag, body)
    return {i: body for i, (tag, body) in latest.items() if tag == "PENDING"}


def is_operator_authority(body: str) -> bool:
    low = body.lower()
    return any(marker in low for marker in _AUTHORITY_MARKERS)


# ── The predicate ────────────────────────────────────────────────────

def tracker_verdict(text: str) -> tuple:
    """(outcome, detail) for ONE tracker's text — outcome in
    {"fire", "silent", "malformed"}. "malformed" is a parse-failure
    shape distinct from "silent" only so the caller can print a
    warning; it never blocks either way (fail-open)."""
    status = header_field(text, _STATUS_LINE)
    if status is None:
        return ("malformed", "no `Status:` header line found")
    if status != "in-progress":
        return ("silent", f"Status is `{status}`, not `in-progress`")

    mode = header_field(text, _MODE_LINE)
    attended = mode is not None and mode.strip().lower() == "attended"
    if attended:
        return ("silent", "Mode: attended — the advance prompt is the "
                           "legitimate stop")

    a_tag = last_a_line_tag(text)
    if a_tag is None:
        # No A-line at all: pre-first-round investigate-design work, or a
        # tracker still in cycle 1 before any attack dispatch. Nothing
        # this hook's predicate (which reads A-line terminality) can
        # judge — fail open rather than guess at desk work owed.
        return ("silent", "no A-line recorded yet")
    if a_tag == "DISPATCHED":
        return ("silent", "last A-line is [DISPATCHED] — a round is in "
                           "flight, awaiting return")
    if a_tag not in _TERMINAL_A_TAGS:
        return ("malformed", f"last A-line tag `[{a_tag}]` is not a "
                              "recognized terminal or in-flight tag")

    blocking = blocking_set(text)
    if len(blocking) == 1:
        only_id, only_body = next(iter(blocking.items()))
        if is_operator_authority(only_body):
            return ("silent", f"the sole blocking entry ({only_id}) is an "
                               "operator-authority [PENDING] — authority-"
                               "gated close")

    owed = (f"last A-line [{a_tag}]"
            + (f"; blocking: {', '.join(sorted(blocking))}" if blocking
               else "; no PENDING blocking"))
    return ("fire", owed)


def verdict(payload: dict) -> tuple:
    """(outcome, detail) across every tracker under the payload's cwd —
    outcome in {"fire", "silent"}. Fires on the first firing tracker;
    a "malformed" per-file result is folded into "silent" here (never
    blocks) but its detail is still surfaced via the warnings list for
    the caller to print."""
    cwd = payload.get("cwd") or os.getcwd()
    trackers = find_trackers(cwd)
    if not trackers:
        return ("silent", "no live statiker tracker under this cwd")

    warnings = []
    for path in trackers:
        try:
            with open(path, encoding="utf-8") as f:
                text = f.read()
        except OSError as exc:
            warnings.append(f"{path}: unreadable ({exc})")
            continue
        try:
            outcome, detail = tracker_verdict(text)
        except Exception as exc:  # noqa: BLE001 — fail-open on ANY parse defect
            warnings.append(f"{path}: parse error ({exc})")
            continue
        if outcome == "malformed":
            warnings.append(f"{path}: {detail}")
            continue
        if outcome == "fire":
            reason = (
                f"P16 stop-guard: unattended statiker desk work is owed "
                f"at `{path}` ({detail}). A report is no terminus — the "
                f"run's own turn-end rule (SKILL.md) names a dispatched "
                f"round awaiting return, a hold the desk cannot clear, an "
                f"operator-owned decision, or the close as the only "
                f"legitimate stops; none applies here. Continue the "
                f"owed desk work (cycle re-derivation, unit dispatch, or "
                f"landing) per the tracker's current state before ending "
                f"this turn."
            )
            for w in warnings:
                print(f"[{_SOURCE}] WARN: {w}", file=sys.stderr)
            return ("fire", reason)

    for w in warnings:
        print(f"[{_SOURCE}] WARN: {w}", file=sys.stderr)
    return ("silent", "no firing tracker")


# ── The lane ─────────────────────────────────────────────────────────

def block_payload(reason: str) -> dict:
    """The Stop-hook blocking schema, derived from harness source (see
    module docstring): top-level `decision`/`reason`, no
    `hookSpecificOutput` wrapper."""
    return {"decision": "block", "reason": reason}


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    if payload.get("hook_event_name") not in ("Stop", None):
        # Registered on Stop only; a stray invocation under another event
        # name (manual testing, a future re-registration) stays silent
        # rather than guessing.
        return 0
    outcome, detail = verdict(payload)
    if outcome == "fire":
        print(json.dumps(block_payload(detail)))
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        # ── Header/A-line/blocking-set extraction, working-copy free ───
        BASE_HEADER = (
            "# Run: test\n"
            "Status: in-progress\n"
            "Phase: investigate-design\n"
            "Skill: statiker 0.2.81\n"
            "\n"
            "INTENT — do the thing.\n"
            "\n"
            "## Cycle 1\n"
        )

        assert header_field(BASE_HEADER, _STATUS_LINE) == "in-progress"
        assert header_field(BASE_HEADER, _MODE_LINE) is None
        assert header_field(BASE_HEADER + "Mode: attended\n",
                             _MODE_LINE) == "attended"
        assert header_field("Status: COMPLETE\n", _STATUS_LINE) == "COMPLETE"
        assert header_field("no header here\n", _STATUS_LINE) is None

        assert last_a_line_tag(BASE_HEADER) is None
        one_round = BASE_HEADER + "- A1 [DISPATCHED] round one.\n"
        assert last_a_line_tag(one_round) == "DISPATCHED"
        two_rounds = (one_round.replace("[DISPATCHED]", "[BIT]")
                      + "- A2 [DISPATCHED] round two.\n")
        assert last_a_line_tag(two_rounds) == "DISPATCHED"
        # a quoted report block (`> ` prefix) must NEVER be read as a live
        # A-line — the false-fire probe this hook's own docstring names
        quoted = (BASE_HEADER
                  + "- A1 [DISPATCHED] round one.\n"
                  + "> Superseded — A1 quotes\n"
                  + "> - A9 [BIT] this is quoted prose, not a live line\n"
                  + "> more quoted text\n")
        assert last_a_line_tag(quoted) == "DISPATCHED", \
            "a quoted `> - A9 [BIT]` line must not be read as live"

        assert blocking_set(BASE_HEADER) == {}
        pend = (BASE_HEADER
                + "- F1 [PENDING] an open question — basis: none yet.\n")
        assert blocking_set(pend) == {
            "F1": "an open question — basis: none yet."}
        resolved = pend + "- F1 [VERIFIED] resolved — basis: checked.\n"
        assert blocking_set(resolved) == {}, \
            "latest tag wins: a later VERIFIED line clears F1 from PENDING"
        two_pend = pend + "- D3 [PENDING] another open question.\n"
        assert set(blocking_set(two_pend)) == {"F1", "D3"}

        assert is_operator_authority(
            "needs an OPERATOR-AUTHORITY grant before this gate clears")
        assert is_operator_authority("an operator authority bound raise")
        assert not is_operator_authority(
            "the operator asked about this yesterday")
        assert not is_operator_authority("an ordinary open question")

        # ── tracker_verdict: the four legitimate-wait shapes, SILENT ───
        # (1) attended prompt
        attended = (BASE_HEADER + "Mode: attended\n"
                    + "- A1 [BIT] round one found substance.\n")
        outcome, detail = tracker_verdict(attended)
        assert outcome == "silent" and "attended" in detail, (outcome, detail)

        # (2) round in flight [DISPATCHED]
        in_flight = BASE_HEADER + "- A1 [DISPATCHED] round one, live.\n"
        outcome, detail = tracker_verdict(in_flight)
        assert outcome == "silent" and "DISPATCHED" in detail, \
            (outcome, detail)

        # (3) operator-authority [PENDING] as sole blocker
        authority_gated = (
            BASE_HEADER
            + "- A1 [BIT] round one found substance.\n"
            + "- F9 [PENDING] blocked on an OPERATOR-AUTHORITY grant "
              "before the ready gate — basis: needs operator line.\n"
        )
        outcome, detail = tracker_verdict(authority_gated)
        assert outcome == "silent" and "authority-gated" in detail, \
            (outcome, detail)

        # (4) Status not in-progress
        not_live = BASE_HEADER.replace("Status: in-progress",
                                        "Status: COMPLETE")
        not_live += "- A1 [BIT] round one found substance.\n"
        outcome, detail = tracker_verdict(not_live)
        assert outcome == "silent" and "COMPLETE" in detail, (outcome, detail)

        # ── RED FIRST: the two must-fire shapes against a STUB — proven
        # by literally deleting the predicate's fire branch and checking
        # both go silent, then restoring it (arrangement note: this is
        # the module's OWN pre-fix state check, run every time via
        # the "solely" tautology below rather than by editing the file,
        # so the red proof is reproducible in CI, not a one-time hand
        # edit). Positive control: an obviously-firing shape must ALSO
        # still be silenced when the fire branch is stubbed, or the stub
        # proves nothing.
        def _stubbed_tracker_verdict(text: str) -> tuple:
            """A deliberately gutted copy of tracker_verdict's fire path
            — the RED baseline the real function must diverge from."""
            status = header_field(text, _STATUS_LINE)
            if status != "in-progress":
                return ("silent", "stub: status")
            mode = header_field(text, _MODE_LINE)
            if mode is not None and mode.strip().lower() == "attended":
                return ("silent", "stub: attended")
            return ("silent", "stub: fire path removed")

        # (i) b7-shape: [BIT], no blocking PENDING at all
        b7_shape = (
            BASE_HEADER
            + "- A1 [DISPATCHED] the first attack round.\n"
            + "- A1 [BIT] NOT zero-delta. Findings landed; the design "
              "REOPENS: Status returns to in-progress and cycle 2 "
              "re-derives.\n"
        )
        assert _stubbed_tracker_verdict(b7_shape)[0] == "silent"  # RED
        outcome, detail = tracker_verdict(b7_shape)
        assert outcome == "fire", (outcome, detail)  # GREEN
        assert "[BIT]" in detail and "no PENDING blocking" in detail

        # (ii) cd-shape: [ZERO-DELTA] terminal with an ORDINARY (non-
        # authority) PENDING blocking — desk work owed, not authority-
        # gated. Deliberately a different terminal tag and a non-empty
        # blocking set from (i), so the two must-fire fixtures exercise
        # different branches rather than duplicating one shape.
        cd_shape = (
            BASE_HEADER
            + "- A2 [DISPATCHED] the second attack round.\n"
            + "- A2 [BIT] findings landed against the record; the design "
              "REOPENS.\n"
            + "- A3 [DISPATCHED] the third attack round.\n"
            + "- A3 [ZERO-DELTA] substance-free return; record repairs "
              "executed; closing design.\n"
            + "- F40 [PENDING] an unresolved desk question, no operator "
              "involvement — basis: needs a second read.\n"
        )
        assert _stubbed_tracker_verdict(cd_shape)[0] == "silent"  # RED
        outcome, detail = tracker_verdict(cd_shape)
        assert outcome == "fire", (outcome, detail)  # GREEN
        assert "[ZERO-DELTA]" in detail and "F40" in detail

        # ── discrimination: blocking set with an authority PENDING PLUS
        # an ordinary one → still FIRES (not solely authority)
        mixed_blocking = (
            BASE_HEADER
            + "- A1 [BIT] round one found substance.\n"
            + "- F1 [PENDING] blocked on an OPERATOR-AUTHORITY grant.\n"
            + "- F2 [PENDING] an ordinary open desk question.\n"
        )
        outcome, detail = tracker_verdict(mixed_blocking)
        assert outcome == "fire", (outcome, detail)

        # ── malformed tracker → "malformed", never "fire" (fail-open) ──
        outcome, detail = tracker_verdict("garbage, no header at all\n")
        assert outcome == "malformed", (outcome, detail)
        weird_tag = BASE_HEADER + "- A1 [FROBNICATE] unknown tag.\n"
        outcome, detail = tracker_verdict(weird_tag)
        assert outcome == "malformed", (outcome, detail)

        # ── no A-line yet (pre-first-round) → silent, not malformed ────
        outcome, detail = tracker_verdict(BASE_HEADER)
        assert outcome == "silent" and "no A-line" in detail, (outcome, detail)

        # ── verdict(): tracker discovery + e2e over a real filesystem ──
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            runs_dir = os.path.join(td, ".clippy", "runs")
            os.makedirs(runs_dir)

            # no tracker at all → silent
            assert verdict({"cwd": td}) == \
                ("silent", "no live statiker tracker under this cwd")

            tpath = os.path.join(runs_dir, "2026-08-17-x-statiker.md")
            with open(tpath, "w", encoding="utf-8") as f:
                f.write(b7_shape)
            outcome, detail = verdict({"cwd": td})
            assert outcome == "fire", (outcome, detail)
            assert "P16 stop-guard" in detail and tpath in detail

            with open(tpath, "w", encoding="utf-8") as f:
                f.write(in_flight)
            assert verdict({"cwd": td})[0] == "silent"

            # a malformed tracker never blocks, whatever else is true
            with open(tpath, "w", encoding="utf-8") as f:
                f.write("no header, this file is junk\n")
            assert verdict({"cwd": td}) == ("silent", "no firing tracker")

            # unreadable tracker (permission denied) → silent, not fire
            with open(tpath, "w", encoding="utf-8") as f:
                f.write(b7_shape)
            os.chmod(tpath, 0o000)
            try:
                if os.geteuid() != 0:  # root reads through mode 000
                    assert verdict({"cwd": td})[0] == "silent"
            finally:
                os.chmod(tpath, 0o644)

        # ── main(): stdin JSON in, stdout JSON out ──────────────────────
        import contextlib
        import io

        def run_main(raw):
            old, out = sys.stdin, io.StringIO()
            try:
                sys.stdin = io.StringIO(raw)
                with contextlib.redirect_stdout(out):
                    rc = main()
            finally:
                sys.stdin = old
            return rc, out.getvalue()

        with tempfile.TemporaryDirectory() as td:
            runs_dir = os.path.join(td, ".clippy", "runs")
            os.makedirs(runs_dir)
            tpath = os.path.join(runs_dir, "2026-08-17-x-statiker.md")
            with open(tpath, "w", encoding="utf-8") as f:
                f.write(b7_shape)

            rc, out = run_main(json.dumps(
                {"hook_event_name": "Stop", "cwd": td, "session_id": "s1"}))
            assert rc == 0
            j = json.loads(out)
            assert j["decision"] == "block"
            assert "reason" in j and "P16 stop-guard" in j["reason"]
            assert "hookSpecificOutput" not in j
            assert "permissionDecision" not in j

            with open(tpath, "w", encoding="utf-8") as f:
                f.write(in_flight)
            rc, out = run_main(json.dumps(
                {"hook_event_name": "Stop", "cwd": td, "session_id": "s1"}))
            assert rc == 0 and out == "", repr(out)

            # a non-Stop event never fires, whatever the tracker says
            with open(tpath, "w", encoding="utf-8") as f:
                f.write(b7_shape)
            rc, out = run_main(json.dumps(
                {"hook_event_name": "SubagentStop", "cwd": td}))
            assert rc == 0 and out == "", repr(out)

        # fail-open: garbage stdin never blocks a call
        rc, out = run_main("}{ not json")
        assert rc == 0 and out == "", repr(out)

        print("statiker_stop_guard: all tests passed")
        sys.exit(0)
    sys.exit(main())

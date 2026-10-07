#!/usr/bin/env python3
"""SessionStart(compact) hook: send a compacted run session back
through the resume gate (ITEMS.md st-92, the skill-owned half).

Why a hook: a session cannot observe its own compaction. After one,
what the desk holds of the skill page and of the run record is a
machine summary standing in for the text, and nothing in the summary
says so. The record is the handoff by design, so the cure is the one
the page already owns for a successor desk — the resume's record gate
(`sweep`, then `closure`) — and this hook is what says "now".

    fire  = payload `source` is `compact`
            AND the payload `cwd` holds at least one
                `.clippy/runs/*.md` whose header (first 15 lines)
                carries a line starting `Skill: statiker`
                AND a line exactly `Status: <live value>`
    silent otherwise — no `.clippy/`, no tracker, another skill's
            tracker, a closed run, any other `source` or event.

Live Status values are the page's, not this file's: the header's
`Status:` is from {in-progress, [READY], PASSED, FAILED, COMPLETE}
(SKILL.md, The record, "Header: `# Run: <title>`; `Status:` from"),
and FAILED/COMPLETE are the close path, the other three the states a
run is still worked in (SKILL.md, "(FAILED/COMPLETE): [READY],
in-progress, PASSED"). A run in implementation sits at `[READY]`, so
`in-progress` alone would leave the hook silent for most of a run.

Schema, derived from the harness's own source (`~/dev/reference/
claude-code/src`), not from another plugin's hook:
  - input: `executeSessionStartHooks` builds `{...base,
    hook_event_name: 'SessionStart', source, agent_type, model}` with
    `source: 'startup' | 'resume' | 'clear' | 'compact'`
    (utils/hooks.ts); `cwd` is in the base input
    (`createBaseHookInput`). The registration's matcher is matched
    against `source` (same file, the `matchQuery` switch).
  - output: `hookSpecificOutput.additionalContext`, with
    `hookEventName` equal to the event or the harness rejects the
    output (utils/hooks.ts, `processHookJSONOutput`).
  - that it reaches the post-compaction context:
    services/compact/compact.ts runs `processSessionStartHooks(
    'compact')` after a successful compaction and
    `buildPostCompactMessages` appends its result after the summary
    and attachments; utils/sessionStart.ts wraps the collected
    contexts as a `hook_additional_context` attachment.

Fail-open everywhere: unreadable payload, unreadable tracker, any
exception -> exit 0, empty stdout, a one-line warning on stderr. It
never blocks and never writes a file. stdout carries only the hook's
JSON; empty stdout is a silent pass.

Not exercised here: a real compaction firing this hook in a live
session. The battery (tools/test_statiker_postcompact_hook.py) drives
the script as a subprocess with a constructed payload.
"""
from __future__ import annotations

import glob
import json
import os
import sys

_SOURCE = "statiker/postcompact"
_TRACKER_GLOB = os.path.join(".clippy", "runs", "*.md")
_HEADER_LINES = 15
_SKILL_PREFIX = "Skill: statiker"
_LIVE_STATUS_LINES = frozenset(
    f"Status: {value}" for value in ("in-progress", "[READY]", "PASSED"))

_INSTRUCTION = (
    "statiker: this session's context was just compacted. What you "
    "hold of the skill page and of the run record is now a summary, "
    "not the text. If you are the session conducting this run: "
    "before your next act, load the statiker skill again, then "
    "run the resume gate over {trackers} (sweep, then closure) and "
    "continue from their verdicts, never from the summary. A "
    "dispatched lane ignores this notice."
)


def warn(message: str) -> None:
    line = " ".join(str(message).split())
    print(f"[{_SOURCE}] WARN: {line}", file=sys.stderr)


def is_live_statiker_header(text: str) -> bool:
    """True when the header window names statiker as the run's skill
    and carries a live Status line. Lines are compared whole (trailing
    whitespace aside): a Status line with anything after its value is
    not the header field the page defines."""
    header = [line.rstrip() for line in text.splitlines()[:_HEADER_LINES]]
    return (any(line.startswith(_SKILL_PREFIX) for line in header)
            and any(line in _LIVE_STATUS_LINES for line in header))


def live_trackers(cwd: str) -> list[str]:
    """Repo-relative paths of every live statiker tracker under `cwd`,
    sorted. An unreadable tracker is skipped with a warning."""
    found = []
    for path in sorted(glob.glob(os.path.join(glob.escape(cwd),
                                              _TRACKER_GLOB))):
        try:
            with open(path, encoding="utf-8") as f:
                text = f.read()
        except (OSError, ValueError) as exc:
            warn(f"{path}: unreadable ({exc})")
            continue
        if is_live_statiker_header(text):
            found.append(os.path.relpath(path, cwd).replace(os.sep, "/"))
    return found


def context_payload(trackers: list[str]) -> dict:
    """The SessionStart additional-context form (see module docstring)."""
    return {"hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": _INSTRUCTION.format(
            trackers=", ".join(trackers)),
    }}


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except ValueError as exc:
        warn(f"unreadable payload ({exc})")
        return 0
    if not isinstance(payload, dict):
        warn(f"payload is {type(payload).__name__}, not an object")
        return 0
    if payload.get("hook_event_name") not in ("SessionStart", None):
        return 0
    if payload.get("source") != "compact":
        return 0
    cwd = payload.get("cwd")
    if not isinstance(cwd, str) or not cwd:
        warn("payload carries no usable cwd")
        return 0
    trackers = live_trackers(cwd)
    if trackers:
        print(json.dumps(context_payload(trackers)))
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception as exc:  # noqa: BLE001 — a broken hook never blocks
        warn(f"unexpected error ({exc!r})")
        code = 0
    sys.exit(code)

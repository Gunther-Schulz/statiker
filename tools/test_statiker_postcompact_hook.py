#!/usr/bin/env python3
"""Red-first fixture battery for plugin/hooks/statiker_postcompact.py —
the st-92 SessionStart(compact) hook that sends a compacted run session
back through the resume gate (ITEMS.md st-92).

Invokes the hook script exactly as the harness does: JSON payload on
stdin, JSON (or nothing) on stdout, against constructed tracker
fixtures under `.clippy/runs/*.md` in a scratch directory — never
copies of a real run. Every arm reads the RETURN CODE as well as
stdout: the hook is fail-open, so a crash and a silent pass must stay
distinguishable here.

Red-first: the absent script — every arm fails on a non-zero return
code before the hook file exists. The discriminating pair is the live
tracker (fires, names it) against the same tracker at `Status:
COMPLETE` (silent).

Run: python3 -m pytest tools/test_statiker_postcompact_hook.py -q
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOK = REPO_ROOT / "plugin" / "hooks" / "statiker_postcompact.py"
MANIFEST = REPO_ROOT / "plugin" / "hooks" / "hooks.json"

HEADER = (
    "# Run: test\n"
    "Status: in-progress\n"
    "Phase: investigate-design\n"
    "Skill: statiker 0.2.105\n"
    "\n"
    "INTENT — do the thing.\n"
    "\n"
    "## Cycle 1\n"
)

INSTRUCTION = (
    "statiker: this session's context was just compacted. What you "
    "hold of the skill page and of the run record is now a summary, "
    "not the text. If you are the session conducting this run: "
    "before your next act, load the statiker skill again, then "
    "run the resume gate over {tracker} (sweep, then closure) and "
    "continue from their verdicts, never from the summary. A "
    "dispatched lane ignores this notice."
)


def run_raw(stdin_text):
    return subprocess.run(
        [sys.executable, str(HOOK)], input=stdin_text,
        capture_output=True, text=True, timeout=30)


def run_hook(cwd, source="compact", event="SessionStart"):
    return run_raw(json.dumps({
        "hook_event_name": event, "source": source, "cwd": str(cwd),
        "session_id": "t1"}))


class TrackerFixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.runs = self.dir / ".clippy" / "runs"
        self.runs.mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def tracker(self, text, name="2026-10-07-x.md"):
        path = self.runs / name
        path.write_text(text, encoding="utf-8")
        return path

    def assertSilent(self, proc):
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stdout, "")

    def assertFires(self, proc, trackers):
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        specific = out["hookSpecificOutput"]
        self.assertEqual(specific["hookEventName"], "SessionStart")
        self.assertEqual(specific["additionalContext"],
                         INSTRUCTION.format(tracker=trackers))
        self.assertEqual(set(out), {"hookSpecificOutput"})


class Fires(TrackerFixture):
    def test_live_tracker_fires_and_names_it(self):
        self.tracker(HEADER)
        self.assertFires(run_hook(self.dir), ".clippy/runs/2026-10-07-x.md")

    def test_every_live_status_on_the_page_fires(self):
        # SKILL.md (The record): Status is from {in-progress, [READY],
        # PASSED, FAILED, COMPLETE}; FAILED/COMPLETE are the close path.
        for status in ("in-progress", "[READY]", "PASSED"):
            with self.subTest(status=status):
                self.tracker(HEADER.replace("in-progress", status))
                self.assertFires(run_hook(self.dir),
                                 ".clippy/runs/2026-10-07-x.md")

    def test_two_live_trackers_are_comma_separated_and_sorted(self):
        self.tracker(HEADER, "2026-10-07-b.md")
        self.tracker(HEADER, "2026-10-06-a.md")
        self.tracker(HEADER.replace("in-progress", "COMPLETE"),
                     "2026-10-05-done.md")
        self.assertFires(
            run_hook(self.dir),
            ".clippy/runs/2026-10-06-a.md, .clippy/runs/2026-10-07-b.md")

    def test_status_and_phase_at_header_lines_16_17_fire(self):
        # 0.2.105 repair D1: a header grown past 15 lines still names
        # its fields inside the window (20 lines)
        text = ("# Run: test\nSkill: statiker 0.2.105\n"
                + "Note: filler\n" * 13
                + "Status: in-progress\nPhase: investigate-design\n"
                + "\nINTENT — do the thing.\n\n## Cycle 1\n")
        lines = text.splitlines()
        self.assertEqual(lines[15], "Status: in-progress")   # line 16
        self.assertEqual(lines[16], "Phase: investigate-design")
        self.tracker(text)
        self.assertFires(run_hook(self.dir), ".clippy/runs/2026-10-07-x.md")

    def test_cwd_below_the_repo_root_fires(self):
        # 0.2.105 repair D2: the payload cwd is wherever the session
        # stands, the trackers live under the repository root
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=self.dir,
                       env={**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null"},
                       capture_output=True, check=True)
        below = self.dir / "sub"
        below.mkdir()
        self.tracker(HEADER)
        self.assertFires(run_hook(below), ".clippy/runs/2026-10-07-x.md")

    def test_absent_event_name_still_fires(self):
        self.tracker(HEADER)
        proc = run_raw(json.dumps({"source": "compact",
                                   "cwd": str(self.dir)}))
        self.assertFires(proc, ".clippy/runs/2026-10-07-x.md")


class Silent(TrackerFixture):
    def test_complete_is_silent(self):
        # the discriminating pair's other half: same tracker, closed
        self.tracker(HEADER.replace("in-progress", "COMPLETE"))
        self.assertSilent(run_hook(self.dir))

    def test_failed_is_silent(self):
        self.tracker(HEADER.replace("in-progress", "FAILED"))
        self.assertSilent(run_hook(self.dir))

    def test_no_clippy_dir_is_silent(self):
        with tempfile.TemporaryDirectory() as bare:
            self.assertSilent(run_hook(bare))

    def test_empty_runs_dir_is_silent(self):
        self.assertSilent(run_hook(self.dir))

    def test_tracker_without_skill_header_is_silent(self):
        self.tracker(HEADER.replace("Skill: statiker 0.2.105\n", ""))
        self.assertSilent(run_hook(self.dir))

    def test_another_skills_tracker_is_silent(self):
        self.tracker(HEADER.replace("Skill: statiker", "Skill: clippy"))
        self.assertSilent(run_hook(self.dir))

    def test_header_fields_below_the_window_are_silent(self):
        # the header is the first 20 lines; a body line quoting the
        # fields further down is prose, not the header
        self.tracker("# Run: test\n" + "filler\n" * 20 + HEADER)
        self.assertSilent(run_hook(self.dir))

    def test_status_must_be_the_exact_line(self):
        self.tracker(HEADER.replace("Status: in-progress",
                                    "Status: in-progress (paused)"))
        self.assertSilent(run_hook(self.dir))

    def test_source_startup_is_silent(self):
        self.tracker(HEADER)
        for source in ("startup", "resume", "clear"):
            with self.subTest(source=source):
                self.assertSilent(run_hook(self.dir, source=source))

    def test_other_event_is_silent(self):
        self.tracker(HEADER)
        self.assertSilent(run_hook(self.dir, event="Stop"))

    def test_non_md_file_is_silent(self):
        self.tracker(HEADER, "2026-10-07-x.txt")
        self.assertSilent(run_hook(self.dir))


class FailOpen(TrackerFixture):
    def test_malformed_stdin_is_silent_exit_zero(self):
        for raw in ("}{ not json", "", "[1, 2]", '"compact"', "null"):
            with self.subTest(raw=raw):
                proc = run_raw(raw)
                self.assertSilent(proc)

    def test_malformed_stdin_warns_on_stderr(self):
        proc = run_raw("}{ not json")
        self.assertSilent(proc)
        self.assertEqual(len(proc.stderr.strip().splitlines()), 1)

    def test_missing_cwd_dir_is_silent(self):
        self.assertSilent(run_hook(self.dir / "does-not-exist"))

    def test_non_string_cwd_is_silent(self):
        proc = run_raw(json.dumps({"hook_event_name": "SessionStart",
                                   "source": "compact", "cwd": 7}))
        self.assertSilent(proc)

    @unittest.skipIf(os.geteuid() == 0, "root reads through mode 000")
    def test_unreadable_tracker_is_skipped_with_a_warning(self):
        locked = self.tracker(HEADER, "2026-10-06-locked.md")
        self.tracker(HEADER, "2026-10-07-open.md")
        os.chmod(locked, 0o000)
        try:
            proc = run_hook(self.dir)
        finally:
            os.chmod(locked, 0o644)
        self.assertFires(proc, ".clippy/runs/2026-10-07-open.md")
        self.assertIn("2026-10-06-locked.md", proc.stderr)

    def test_undecodable_tracker_is_silent(self):
        (self.runs / "2026-10-07-x.md").write_bytes(b"\xff\xfe\x00 junk\n")
        self.assertSilent(run_hook(self.dir))

    def test_writes_no_file(self):
        self.tracker(HEADER)
        before = sorted(p.relative_to(self.dir) for p in self.dir.rglob("*"))
        self.assertFires(run_hook(self.dir), ".clippy/runs/2026-10-07-x.md")
        after = sorted(p.relative_to(self.dir) for p in self.dir.rglob("*"))
        self.assertEqual(before, after)


class Registration(unittest.TestCase):
    """The manifest entry that makes the harness run the hook."""

    def test_registered_under_session_start_compact(self):
        hooks = json.loads(MANIFEST.read_text(encoding="utf-8"))["hooks"]
        entries = hooks.get("SessionStart", [])
        commands = [
            (entry.get("matcher"), hook.get("type"), hook.get("command"))
            for entry in entries for hook in entry.get("hooks", [])]
        self.assertIn(
            ("compact", "command",
             '"${CLAUDE_PLUGIN_ROOT}"/hooks/statiker_postcompact.py'),
            commands)

    def test_hook_file_is_executable(self):
        # the registration invokes the file directly, not via python3
        self.assertTrue(os.access(HOOK, os.X_OK))


if __name__ == "__main__":
    unittest.main()

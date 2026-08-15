#!/usr/bin/env python3
"""Red-first test suite for statiker_git.py — the lock/unit commit
machinery precipitated out of SKILL.md prose after draft attacks 4-6.

Each test encodes a probe from the attack rounds' battery (provenance:
dev-notes/OBSERVATIONS.md, attacks 4-6). The suite was written before
the script existed (red by construction); every git-semantics claim is
exercised against a real constructed repo, never asserted from memory.

Run: python3 tools/test_statiker_git.py
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "plugin" / "skills" / "statiker" / "scripts" / "statiker_git.py"

VERDICT_PREFIX = "STATIKER-GIT VERDICT: "


def split_lines(text):
    """Split the tool's own stdout on newlines ONLY, mirroring
    statiker_record.py's split_lines: str.splitlines() also breaks on
    U+000C, U+2028 and U+0085, fabricating a line the process never
    printed (the splitlines CLASS, closed here to close the reader's
    own reach — 2eb6b59)."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return [l[:-1] if l.endswith("\r") else l for l in lines]


def hermetic_env():
    env = {
        "PATH": os.environ["PATH"],
        "HOME": os.environ.get("_STATIKER_TEST_HOME", "/nonexistent"),
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_CONFIG_SYSTEM": "/dev/null",
        "GIT_AUTHOR_NAME": "t",
        "GIT_AUTHOR_EMAIL": "t@t",
        "GIT_COMMITTER_NAME": "t",
        "GIT_COMMITTER_EMAIL": "t@t",
        "STATIKER_GIT_RETRY_BASE": "0.01",
        "LC_ALL": "C",
    }
    return env


class GitFixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name) / "repo"
        self.repo.mkdir()
        self.env = hermetic_env()
        self.git("init", "-b", "main")
        # a baseline commit so HEAD exists
        (self.repo / "base.txt").write_text("base\n")
        self.git("add", "base.txt")
        self.git("commit", "-m", "base")

    def tearDown(self):
        self._tmp.cleanup()

    def git(self, *args, check=True):
        return subprocess.run(
            ["git", *args], cwd=self.repo, env=self.env,
            capture_output=True, text=True, check=check,
        )

    def tool(self, *args, timeout=60):
        p = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=self.repo, env=self.env,
            capture_output=True, text=True, timeout=timeout,
        )
        return p

    def verdict(self, p):
        lines = [l for l in split_lines(p.stdout) if l.startswith(VERDICT_PREFIX)]
        self.assertEqual(
            len(lines), 1,
            f"expected exactly one verdict line, stdout:\n{p.stdout}\nstderr:\n{p.stderr}",
        )
        return json.loads(lines[0][len(VERDICT_PREFIX):])

    def tool_raw(self, *args, timeout=60):
        # E-C: ensure_ascii=False + say()'s byte-level write mean a
        # non-UTF-8 path byte reaches stdout as the RAW byte — invalid
        # UTF-8 on its own, so subprocess's own text=True decode
        # (self.tool()) raises UnicodeDecodeError before the test ever
        # sees the output. Capture bytes and decode surrogateescape,
        # the same round trip the tool and desk are meant to share.
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=self.repo, env=self.env,
            capture_output=True, timeout=timeout,
        )

    def verdict_raw(self, p):
        out = p.stdout.decode("utf-8", "surrogateescape")
        lines = [l for l in split_lines(out) if l.startswith(VERDICT_PREFIX)]
        self.assertEqual(
            len(lines), 1,
            f"expected exactly one verdict line, stdout:\n{out!r}\n"
            f"stderr:\n{p.stderr.decode('utf-8', 'surrogateescape')!r}",
        )
        return json.loads(lines[0][len(VERDICT_PREFIX):])

    def write(self, rel, content):
        p = self.repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return p

    # -- P2 migration helpers: --write-set is gone (BACKLOG P2) — the
    # unit seam now reads its write-set from the record's declared
    # lines through a gate consult (closure --unit), so every fixture
    # built on --write-set needs a tracker-backed arrangement instead.

    CLOSED_TRACKER = (
        "# Run: t\nStatus: in-progress\nPhase: implement\n\n"
        "INTENT — fixture.\n\n## Cycle 1\n"
        "- D1 [COMMITTED] the design — basis: probe\n"
        "- A1 [DISPATCHED] round 1 — basis: brief\n"
        "- A1 [ZERO-DELTA] clean return — basis: report\n"
    )
    GATE_CLEAN_TRACKER = "# Run: t\nStatus: in-progress\nPhase: implement\n"

    def unit_tracker(self, write_sets, rel="unit.md"):
        """Write a CLOSED_TRACKER declaring one write-set F-line per
        (unit, path) pair — `write_sets` is {unit_id: [paths]}, in
        insertion order. Returns the tracker's repo-relative path."""
        body = self.CLOSED_TRACKER
        n = 2
        for unit, paths in write_sets.items():
            for p in paths:
                body += (f"- F{n} [VERIFIED] unit {unit} write-set: {p} "
                        f"— basis: design\n")
                n += 1
        self.write(rel, body)
        return rel

    def head_sha(self):
        return self.git("rev-parse", "HEAD").stdout.strip()

    def head_paths(self):
        out = self.git("show", "--name-only", "--format=", "HEAD").stdout
        return set(l for l in split_lines(out) if l)

    def start_conflicted_merge(self):
        self.write("c.txt", "main\n")
        self.git("add", "c.txt")
        self.git("commit", "-m", "c-main")
        self.git("checkout", "-b", "side", "HEAD~1")
        self.write("c.txt", "side\n")
        self.git("add", "c.txt")
        self.git("commit", "-m", "c-side")
        self.git("checkout", "main")
        r = self.git("merge", "side", check=False)
        self.assertNotEqual(r.returncode, 0, "merge should conflict")


# ---------------------------------------------------------------- state gate

class TestStateGate(GitFixture):
    def test_clean_repo_no_halt(self):
        p = self.tool("state-gate")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "STATE_CLEAN")
        self.assertEqual(v["ops"], [])

    def test_mid_merge_detected(self):
        self.start_conflicted_merge()
        v = self.verdict(self.tool("state-gate"))
        self.assertEqual(v["verdict"], "STATE_IN_PROGRESS")
        self.assertIn("merge", v["ops"])

    def test_mid_cherry_pick_detected(self):
        self.write("c.txt", "main\n")
        self.git("add", "c.txt")
        self.git("commit", "-m", "c-main")
        self.git("checkout", "-b", "side", "HEAD~1")
        self.write("c.txt", "side\n")
        self.git("add", "c.txt")
        self.git("commit", "-m", "c-side")
        side_sha = self.git("rev-parse", "HEAD").stdout.strip()
        self.git("checkout", "main")
        r = self.git("cherry-pick", side_sha, check=False)
        self.assertNotEqual(r.returncode, 0)
        v = self.verdict(self.tool("state-gate"))
        self.assertEqual(v["verdict"], "STATE_IN_PROGRESS")
        self.assertIn("cherry-pick", v["ops"])

    def test_mid_revert_detected(self):
        self.write("c.txt", "one\n")
        self.git("add", "c.txt")
        self.git("commit", "-m", "one")
        self.write("c.txt", "two\n")
        self.git("add", "c.txt")
        self.git("commit", "-m", "two")
        r = self.git("revert", "--no-edit", "HEAD~1", check=False)
        self.assertNotEqual(r.returncode, 0)
        v = self.verdict(self.tool("state-gate"))
        self.assertEqual(v["verdict"], "STATE_IN_PROGRESS")
        self.assertIn("revert", v["ops"])

    def _conflicted_rebase(self):
        self.write("r.txt", "main\n")
        self.git("add", "r.txt")
        self.git("commit", "-m", "r-main")
        self.git("checkout", "-b", "feat", "HEAD~1")
        self.write("r.txt", "feat\n")
        self.git("add", "r.txt")
        self.git("commit", "-m", "r-feat")
        r = self.git("rebase", "main", check=False)
        self.assertNotEqual(r.returncode, 0, "rebase should conflict")

    def test_mid_rebase_conflict_detected(self):
        self._conflicted_rebase()
        v = self.verdict(self.tool("state-gate"))
        self.assertEqual(v["verdict"], "STATE_IN_PROGRESS")
        self.assertIn("rebase", v["ops"])

    def test_rebase_exec_stop_detected(self):
        # attack-6 B2: break/exec/reword stops set NONE of the four
        # refs; only the state directory betrays the in-progress rebase.
        self.write("r.txt", "x\n")
        self.git("add", "r.txt")
        self.git("commit", "-m", "r")
        r = self.git("rebase", "--exec", "false", "HEAD~1", check=False)
        self.assertNotEqual(r.returncode, 0, "exec false should stop the rebase")
        v = self.verdict(self.tool("state-gate"))
        self.assertEqual(v["verdict"], "STATE_IN_PROGRESS")
        self.assertIn("rebase", v["ops"])
        self.git("rebase", "--abort")

    def test_completed_rebase_after_conflict_is_clean(self):
        # attack-6 B1: REBASE_HEAD can stay resolvable after a
        # stopped-then-continued rebase completes; a ref-read gate
        # false-halts forever. The directory read must report clean.
        self._conflicted_rebase()
        self.write("r.txt", "resolved\n")
        self.git("add", "r.txt")
        self.env["GIT_EDITOR"] = "true"
        r = self.git("rebase", "--continue", check=False)
        self.assertEqual(r.returncode, 0, r.stderr)
        v = self.verdict(self.tool("state-gate"))
        self.assertEqual(v["verdict"], "STATE_CLEAN", f"ops={v.get('ops')}")

    def test_aborted_merge_is_clean(self):
        self.start_conflicted_merge()
        self.git("merge", "--abort")
        v = self.verdict(self.tool("state-gate"))
        self.assertEqual(v["verdict"], "STATE_CLEAN")

    def test_linked_worktree_state_is_per_worktree(self):
        # the tool resolves state via `git rev-parse --git-path`, which
        # is per-worktree: an operation inside a linked worktree is
        # detected there and does not leak into the main checkout.
        self.write("c.txt", "main\n")
        self.git("add", "c.txt")
        self.git("commit", "-m", "c-main")
        self.git("checkout", "-b", "side", "HEAD~1")
        self.write("c.txt", "side\n")
        self.git("add", "c.txt")
        self.git("commit", "-m", "c-side")
        self.git("checkout", "main")
        wt = Path(self._tmp.name) / "wt"
        self.git("worktree", "add", str(wt), "side")
        r = subprocess.run(["git", "merge", "main"], cwd=wt, env=self.env,
                           capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0, "merge should conflict")
        p_wt = subprocess.run(
            [sys.executable, str(SCRIPT), "state-gate"],
            cwd=wt, env=self.env, capture_output=True, text=True)
        v_wt = self.verdict(p_wt)
        self.assertEqual(v_wt["verdict"], "STATE_IN_PROGRESS")
        self.assertIn("merge", v_wt["ops"])
        v_main = self.verdict(self.tool("state-gate"))
        self.assertEqual(v_main["verdict"], "STATE_CLEAN")


# ----------------------------------------------------------------- preflight

class TestPreflight(GitFixture):
    def test_normal_repo_ok(self):
        v = self.verdict(self.tool("preflight", "--tracker", ".clippy/runs/t.md"))
        self.assertEqual(v["verdict"], "PREFLIGHT_OK")

    def test_ignored_tracker_dir_unpinnable(self):
        # attack-6 N5: a repo ignoring .clippy/ fails every run at
        # maximum cost unless caught at run start.
        self.write(".gitignore", ".clippy/\n")
        self.git("add", ".gitignore")
        self.git("commit", "-m", "ignore clippy")
        v = self.verdict(self.tool("preflight", "--tracker", ".clippy/runs/t.md"))
        self.assertEqual(v["verdict"], "PREFLIGHT_UNPINNABLE_TRACKER")


class TestF6BranchStateAndLinkedWorktree(GitFixture):
    """begehung tier2-without.md F6 (medium): detached HEAD and a
    linked-worktree cwd let the full lock/unit transaction chain land
    silently onto no branch — SKILL.md's own worktree provisioning
    makes the linked-worktree case directly reachable. Preflight is
    the run-start seam that now names the state, field-not-gate (no
    routing change; the F11 precedent) — probes: main checkout with
    HEAD detached (A), invocation cwd inside a linked detached
    worktree (B)."""

    def test_normal_checkout_shows_its_branch(self):
        v = self.verdict(self.tool(
            "preflight", "--tracker", ".clippy/runs/t.md"))
        self.assertEqual(v["verdict"], "PREFLIGHT_OK")
        self.assertEqual(v["branch"], "main", v)
        self.assertFalse(v["worktree"], v)

    def test_detached_head_reports_branch_none(self):
        # Probe A: everything downstream still works (the machinery has
        # no branch check anywhere), so the run completes normally
        # while its certified surfaces land on no branch — silently,
        # unless preflight names it.
        self.git("checkout", "--detach", "HEAD")
        v = self.verdict(self.tool(
            "preflight", "--tracker", ".clippy/runs/t.md"))
        self.assertEqual(v["verdict"], "PREFLIGHT_OK")
        self.assertEqual(v["branch"], "none", v)
        self.assertFalse(v["worktree"], v)

    def test_linked_detached_worktree_reports_both_markers(self):
        # Probe B: invocation cwd inside a linked detached worktree —
        # both markers fire together.
        wt = Path(self._tmp.name) / "wt"
        self.git("worktree", "add", "--detach", str(wt), "HEAD")
        p = subprocess.run(
            [sys.executable, str(SCRIPT), "preflight",
             "--tracker", ".clippy/runs/t.md"],
            cwd=wt, env=self.env, capture_output=True, text=True,
            timeout=60)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PREFLIGHT_OK")
        self.assertEqual(v["branch"], "none", v)
        self.assertTrue(v["worktree"], v)


# ---------------------------------------------------------------- lock check

class TestLockCheck(GitFixture):
    TRACKER = ".clippy/runs/t.md"

    def test_first_lock_clean_untracked_tracker(self):
        # porcelain ?? puts '?' in column one — attack-6 B3: a strict
        # col-1 read halts every first lock on its own fresh tracker.
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool("lock-check", "--tracker", self.TRACKER))
        self.assertEqual(v["verdict"], "LOCK_CHECK_CLEAN")
        self.assertIn(self.TRACKER, v["adds"])

    def test_staged_operator_edit_on_lock_set_path_drops(self):
        # attack-5 B1 probe: a staged-only operator edit on a pathspec
        # path is destroyed by the commit unless column one is read.
        self.write("art.txt", "run content\n")
        self.git("add", "art.txt")
        self.git("commit", "-m", "art")
        self.write("art.txt", "operator staged\n")
        self.git("add", "art.txt")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool(
            "lock-check", "--tracker", self.TRACKER, "--lock-set", "art.txt"))
        self.assertEqual(v["verdict"], "LOCK_CHECK_DROPS")
        drops = {d["path"]: d["reason"] for d in v["drops"]}
        self.assertEqual(drops.get("art.txt"), "collision")

    def test_worktree_only_modification_not_dropped(self):
        # column two set on run-produced content is expected; the
        # judgment re-read stays desk work — no mechanical drop.
        self.write("art.txt", "v1\n")
        self.git("add", "art.txt")
        self.git("commit", "-m", "art")
        self.write("art.txt", "v2 run content\n")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool(
            "lock-check", "--tracker", self.TRACKER, "--lock-set", "art.txt"))
        self.assertEqual(v["verdict"], "LOCK_CHECK_CLEAN")

    def test_staged_tracker_halts(self):
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        self.git("add", self.TRACKER)
        self.git("commit", "-m", "tracker")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER + "edit\n")
        self.git("add", self.TRACKER)
        p = self.tool("lock-check", "--tracker", self.TRACKER)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_TRACKER_COLLISION")
        self.assertNotEqual(p.returncode, 0)

    def test_ignored_untracked_lock_set_path_drops(self):
        self.write(".gitignore", "scratch/\n")
        self.git("add", ".gitignore")
        self.git("commit", "-m", "gi")
        self.write("scratch/x.txt", "x\n")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool(
            "lock-check", "--tracker", self.TRACKER, "--lock-set", "scratch/x.txt"))
        self.assertEqual(v["verdict"], "LOCK_CHECK_DROPS")
        drops = {d["path"]: d["reason"] for d in v["drops"]}
        self.assertEqual(drops.get("scratch/x.txt"), "ignored")

    def test_tracked_ignored_path_commits_regardless_no_drop(self):
        # probe (attack 5): a TRACKED path commits regardless of
        # ignore patterns — check-ignore applies to untracked only.
        self.write("gen.txt", "v1\n")
        self.git("add", "-f", "gen.txt")
        self.git("commit", "-m", "gen")
        self.write(".gitignore", "gen.txt\n")
        self.git("add", ".gitignore")
        self.git("commit", "-m", "gi")
        self.write("gen.txt", "v2\n")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool(
            "lock-check", "--tracker", self.TRACKER, "--lock-set", "gen.txt"))
        self.assertEqual(v["verdict"], "LOCK_CHECK_CLEAN")

    def test_ignored_untracked_tracker_halts_unpinnable(self):
        self.write(".gitignore", ".clippy/\n")
        self.git("add", ".gitignore")
        self.git("commit", "-m", "gi")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        p = self.tool("lock-check", "--tracker", self.TRACKER)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_TRACKER_UNPINNABLE")
        self.assertNotEqual(p.returncode, 0)

    def test_directory_path_halts(self):
        # attack-4 N6 probe: a directory pathspec sweeps operator
        # state under it into the commit.
        self.write("docs/a.txt", "a\n")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        p = self.tool("lock-check", "--tracker", self.TRACKER, "--lock-set", "docs")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_DIRECTORY_PATH")
        self.assertIn("docs", v["paths"])

    def test_missing_lock_set_path_halts(self):
        # attack-6 B4 kin: an unpopulated path poisons the pathspec.
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        p = self.tool("lock-check", "--tracker", self.TRACKER,
                      "--lock-set", "never-made.txt")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_MISSING_PATH")
        self.assertIn("never-made.txt", v["paths"])

    def test_mid_merge_halts(self):
        self.start_conflicted_merge()
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        p = self.tool("lock-check", "--tracker", self.TRACKER)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_STATE")
        self.assertIn("merge", v["ops"])


# --------------------------------------------------------------- lock commit

class TestLockCommit(GitFixture):
    TRACKER = ".clippy/runs/t.md"

    def test_clean_lock_commit_and_readback(self):
        self.write(self.TRACKER, "# Run: t\nStatus: [READY]\nPhase: implement\n")
        p = self.tool("lock-commit", "--tracker", self.TRACKER, "-m", "lock 1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "LOCK_COMMITTED", p.stdout + p.stderr)
        self.assertEqual(p.returncode, 0)
        self.assertEqual(self.head_paths(), {self.TRACKER})
        sha = self.git("rev-parse", "HEAD").stdout.strip()
        self.assertEqual(v["sha"], sha)
        # message landed via -m (attack-6 N1: commit without -m hangs)
        subj = self.git("log", "-1", "--format=%s").stdout.strip()
        self.assertEqual(subj, "lock 1")

    def test_operator_staged_state_outside_pathspec_survives(self):
        # probe (attack 5): pathspec commit leaves outside-pathspec
        # staged state exactly as it was — neither committed nor lost.
        self.write("op.txt", "operator work\n")
        self.git("add", "op.txt")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool(
            "lock-commit", "--tracker", self.TRACKER, "-m", "lock"))
        self.assertEqual(v["verdict"], "LOCK_COMMITTED")
        self.assertEqual(self.head_paths(), {self.TRACKER})
        status = self.git("status", "--porcelain", "--", "op.txt").stdout
        self.assertTrue(status.startswith("A "), f"staged state lost: {status!r}")

    def test_lock_commit_takes_worktree_content(self):
        # probe (attack 5): a pathspec commit takes WORKING-TREE content.
        self.write("art.txt", "v1\n")
        self.git("add", "art.txt")
        self.git("commit", "-m", "art")
        self.write("art.txt", "worktree v2\n")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool(
            "lock-commit", "--tracker", self.TRACKER,
            "--lock-set", "art.txt", "-m", "lock"))
        self.assertEqual(v["verdict"], "LOCK_COMMITTED")
        blob = self.git("show", "HEAD:art.txt").stdout
        self.assertEqual(blob, "worktree v2\n")

    def test_relock_unchanged_inherited_path_is_noop(self):
        # attack-4 B3: an unchanged inherited path is legitimately
        # absent from --stat; its absence is not a readback failure.
        self.write("art.txt", "v1\n")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v1 = self.verdict(self.tool(
            "lock-commit", "--tracker", self.TRACKER,
            "--lock-set", "art.txt", "-m", "lock 1"))
        self.assertEqual(v1["verdict"], "LOCK_COMMITTED")
        with (self.repo / self.TRACKER).open("a") as f:
            f.write("- D2 [COMMITTED] more\n")
        v2 = self.verdict(self.tool(
            "lock-commit", "--tracker", self.TRACKER,
            "--lock-set", "art.txt", "-m", "lock 2"))
        self.assertEqual(v2["verdict"], "LOCK_COMMITTED")
        self.assertEqual(self.head_paths(), {self.TRACKER})

    def test_acknowledged_drop_commits_rest(self):
        self.write("art.txt", "run\n")
        self.git("add", "art.txt")   # operator-staged collision
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool(
            "lock-commit", "--tracker", self.TRACKER, "--lock-set", "art.txt",
            "--drop", "art.txt", "-m", "lock"))
        self.assertEqual(v["verdict"], "LOCK_COMMITTED")
        self.assertEqual(self.head_paths(), {self.TRACKER})
        self.assertEqual([d["path"] for d in v["drops"]], ["art.txt"])
        # the staged collision content survives untouched
        status = self.git("status", "--porcelain", "--", "art.txt").stdout
        self.assertTrue(status.startswith("A "), status)

    def test_unacknowledged_drop_halts_state_moved(self):
        # two-phase safety: the desk acknowledged drops from lock-check;
        # a differing live drop set means state moved between phases.
        self.write("art.txt", "run\n")
        self.git("add", "art.txt")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        p = self.tool("lock-commit", "--tracker", self.TRACKER,
                      "--lock-set", "art.txt", "-m", "lock")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_DROPS_UNACKNOWLEDGED")
        self.assertNotEqual(p.returncode, 0)
        # nothing was committed
        self.assertEqual(self.head_paths(), {"base.txt"})

    def test_stale_acknowledged_drop_halts(self):
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        p = self.tool("lock-commit", "--tracker", self.TRACKER,
                      "--lock-set", "art.txt", "--drop", "art.txt", "-m", "lock")
        v = self.verdict(p)
        self.assertIn(v["verdict"], ("HALT_DROPS_STALE", "HALT_MISSING_PATH"))
        self.assertEqual(self.head_paths(), {"base.txt"})


# --------------------------------------------------------------- unit start

class TestUnitStart(GitFixture):
    def test_clean_write_set(self):
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        v = self.verdict(self.tool("unit-start", "--tracker", tracker,
                                   "--unit", "U1"))
        self.assertEqual(v["verdict"], "UNIT_START_CLEAN", v)
        self.assertIn("start_sha", v)

    def test_untracked_operator_draft_collides(self):
        # attack-4 N7 probe: untracked operator draft on a write-set
        # path would be overwritten and committed by the unit.
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        self.write("src.txt", "operator draft\n")
        p = self.tool("unit-start", "--tracker", tracker, "--unit", "U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_COLLISION")
        self.assertTrue(any("src.txt" in e["path"] for e in v["entries"]))
        self.assertNotEqual(p.returncode, 0)

    def test_modified_tracked_path_collides(self):
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        self.write("src.txt", "v1\n")
        self.git("add", "src.txt")
        self.git("commit", "-m", "src")
        self.write("src.txt", "operator edit\n")
        v = self.verdict(self.tool("unit-start", "--tracker", tracker,
                                   "--unit", "U1"))
        self.assertEqual(v["verdict"], "UNIT_COLLISION")

    def test_dirt_outside_write_set_is_clean(self):
        # attack-5 B3 kin: the check is porcelain scoped to the
        # write-set; unrelated dirt must not spuriously halt the unit.
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        self.write("other.txt", "operator wip\n")
        v = self.verdict(self.tool("unit-start", "--tracker", tracker,
                                   "--unit", "U1"))
        self.assertEqual(v["verdict"], "UNIT_START_CLEAN")

    def test_mid_merge_halts_before_any_edit(self):
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        self.start_conflicted_merge()
        v = self.verdict(self.tool("unit-start", "--tracker", tracker,
                                   "--unit", "U1"))
        self.assertEqual(v["verdict"], "HALT_STATE")

    def test_directory_write_set_halts(self):
        tracker = self.unit_tracker({"U1": ["docs"]})
        self.write("docs/a.txt", "a\n")
        v = self.verdict(self.tool("unit-start", "--tracker", tracker,
                                   "--unit", "U1"))
        self.assertEqual(v["verdict"], "HALT_DIRECTORY_PATH")

    def test_missing_tracker_or_unit_is_usage_error(self):
        # --tracker and --unit are now REQUIRED (P2): omitting either
        # halts USAGE_ERROR, never a silent write-set default
        p = self.tool("unit-start")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertEqual(p.returncode, 3)


# unit-start's "paste-ready record line" feature is RETIRED (P2):
# the write-set is now READ FROM the tracker's own declared lines
# through the gate consult, so there is nothing left to paste back —
# printing the very lines the record already carries verbatim would
# be noise, not evidence. TestUnitStartWriteSetRecordLines and the
# standalone A3 byte-fidelity test below it are retired with it;
# UNIT_WRITE_SET_RE/waves_over_units parsing coverage lives on in
# test_statiker_record.py's TestWaves, which already exercises
# write-set F-lines read directly off a tracker — the canonical
# path this class's own printed-line round-trip test only mimicked.

# -------------------------------------------------------------- unit commit

class TestUnitCommit(GitFixture):
    def test_green_commit(self):
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        self.write("src.txt", "unit output\n")
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_COMMITTED", p.stdout + p.stderr)
        self.assertEqual(self.head_paths(), {"src.txt"})
        self.assertEqual(v["sha"], self.git("rev-parse", "HEAD").stdout.strip())

    def test_operator_staged_state_outside_write_set_survives(self):
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        self.write("op.txt", "operator\n")
        self.git("add", "op.txt")
        self.write("src.txt", "unit output\n")
        v = self.verdict(self.tool("unit-commit", "--tracker", tracker,
                                   "--unit", "U1", "--start-sha", start_sha,
                                   "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED")
        self.assertEqual(self.head_paths(), {"src.txt"})
        status = self.git("status", "--porcelain", "--", "op.txt").stdout
        self.assertTrue(status.startswith("A "), status)

    def test_modified_tracked_path_commits_without_add(self):
        self.write("src.txt", "v1\n")
        self.git("add", "src.txt")
        self.git("commit", "-m", "v1")
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        self.write("src.txt", "v2\n")
        v = self.verdict(self.tool("unit-commit", "--tracker", tracker,
                                   "--unit", "U1", "--start-sha", start_sha,
                                   "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED")
        self.assertEqual(self.git("show", "HEAD:src.txt").stdout, "v2\n")

    def test_already_present_reads_head_not_worktree(self):
        # attack-6 B4: the discriminator must be a HEAD read. Content
        # identical to HEAD → NO_DIFF verdict, nothing committed.
        self.write("src.txt", "settled\n")
        self.git("add", "src.txt")
        self.git("commit", "-m", "settled")
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        head = self.git("rev-parse", "HEAD").stdout.strip()
        self.write("src.txt", "settled\n")  # same content
        v = self.verdict(self.tool("unit-commit", "--tracker", tracker,
                                   "--unit", "U1", "--start-sha", start_sha,
                                   "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_NO_DIFF_VS_HEAD")
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), head)

    def test_missing_write_set_path_halts_nothing_lands(self):
        # attack-6 B4 probe: an unpopulated write-set path poisons the
        # pathspec — exit 1, nothing lands, previously booked as landed.
        tracker = self.unit_tracker({"U1": ["src.txt", "never-made.txt"]})
        start_sha = self.head_sha()
        self.write("src.txt", "made\n")
        head = self.git("rev-parse", "HEAD").stdout.strip()
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_MISSING_PATH")
        self.assertIn("never-made.txt", v["paths"])
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), head)
        self.assertNotEqual(p.returncode, 0)

    def test_contention_blocked_after_capped_retries(self):
        # attack-5 N3: capped, spaced retries; persistent index.lock →
        # blocked-commit REPORT with the error text, never silence.
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        self.write("src.txt", "unit output\n")
        lock = self.repo / ".git" / "index.lock"
        lock.write_text("")
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "BLOCKED_CONTENTION")
        self.assertEqual(v["attempts"], 5)
        self.assertTrue(v["index_lock_present"])
        self.assertIn("index.lock", v["error"])
        self.assertNotEqual(p.returncode, 0)

    def test_contention_recovers_when_lock_clears(self):
        # probe (attack 4): contention is recoverable — a cleared lock
        # lets the same invocation land.
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        self.write("src.txt", "unit output\n")
        v = self.verdict(self.tool("unit-commit", "--tracker", tracker,
                                   "--unit", "U1", "--start-sha", start_sha,
                                   "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED")

    def test_state_gate_reread_distinct_from_contention(self):
        # attack-6 N3: an operation the operator began mid-unit blocks
        # the commit as HALT_STATE, never conflated with index.lock.
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        self.write("src.txt", "unit output\n")
        self.start_conflicted_merge()
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_STATE")
        self.assertIn("merge", v["ops"])

    def test_stale_start_sha_halts_mismatch(self):
        # P2: a foreign commit touching the declared write-set after
        # start-sha halts UNIT_START_MISMATCH before any of the commit
        # seam's own checks run.
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        self.write("src.txt", "foreign touch\n")
        self.git("add", "src.txt")
        self.git("commit", "-m", "foreign touch on src.txt")
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_START_MISMATCH", v)
        self.assertEqual(v["start_sha"], start_sha)

    def test_unknown_start_sha_halts_mismatch(self):
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        self.write("src.txt", "unit output\n")
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", "0" * 40, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_START_MISMATCH")

    def test_write_set_naming_the_tracker_halts(self):
        # P2/F12: the declared write-set names the tracker itself
        tracker = "selfname.md"
        self.write(tracker, self.CLOSED_TRACKER +
                  f"- F2 [VERIFIED] unit U1 write-set: {tracker} "
                  "— basis: design\n")
        start_sha = self.head_sha()
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "WRITE_SET_NAMES_TRACKER", v)
        p2 = self.tool("unit-start", "--tracker", tracker, "--unit", "U1")
        self.assertEqual(self.verdict(p2)["verdict"],
                         "WRITE_SET_NAMES_TRACKER")

    def test_empty_declared_write_set_blocks(self):
        # P2: a KNOWN unit with no live write-set F-line at all — the
        # gate itself carries why (an undeclared unit cannot start)
        tracker = self.write("empty.md", self.CLOSED_TRACKER +
                             "- D9 [AUTO-ACCEPTED] unit U1 gap: no "
                             "write-set decided — basis: report\n")
        p = self.tool("unit-start", "--tracker", str(tracker), "--unit", "U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_GATE_BLOCKED", v)
        self.assertEqual(v["gate"]["declared_write_set"], [])

    def test_held_unit_blocks_the_gate(self):
        tracker = self.write("held.md", self.CLOSED_TRACKER +
                             "- F2 [VERIFIED] unit U1 write-set: x.txt "
                             "— basis: design\n"
                             "- D9 [AUTO-ACCEPTED] unit U1 held: x.txt "
                             "— basis: F2\n")
        p = self.tool("unit-start", "--tracker", str(tracker), "--unit", "U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_GATE_BLOCKED", v)
        self.assertEqual(v["gate"]["verdict"], "UNIT_HELD")


# ---------------------------------------------------- pure-function checks

class TestReviewFindings(GitFixture):
    """Repairs from the 0.2.32 fresh-context review (dev-notes,
    2026-08-07): each test written red against the pre-repair
    behavior the reviewer executed."""

    # review B1's multi-path-single-flag probe targeted --write-set's
    # `nargs="+"` parsing, which P2 removed from unit-start entirely
    # (the write-set is read from the tracker now) — the shape it
    # guarded against still gets covered by lock-check/lock-commit's
    # own `--lock-set` multi-path flag, unchanged by this lane.

    def test_usage_error_emits_verdict_line(self):
        # review B1: argparse exited 2 (the halt code) on stderr with
        # no verdict — the verdict-always-lands guarantee must cover
        # usage errors, on the usage exit code
        p = self.tool("unit-start")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertEqual(p.returncode, 3)

    def test_lock_residue_persists_carries_shas(self):
        # review B2 + N1: a clean filter keeping the tracker
        # permanently residual lands commits and must report them —
        # the verdict carries every landed sha, never "no lock"
        self.git("config", "filter.noisy.clean", "sh -c 'cat; date +%s%N'")
        self.write(".gitattributes", "*.md filter=noisy\n")
        self.git("add", ".gitattributes")
        self.git("commit", "-m", "attr")
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        p = self.tool("lock-commit", "--tracker", ".clippy/runs/t.md",
                      "-m", "lock")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_RESIDUE_PERSISTS")
        self.assertGreaterEqual(len(v["shas"]), 1)
        self.assertNotEqual(p.returncode, 0)

    def test_subdir_invocation_resolves_against_repo_root(self):
        # review N2: relative paths resolved against process cwd —
        # from a subdir, preflight false-cleaned on a phantom path
        (self.repo / "sub").mkdir()
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        p = subprocess.run(
            [sys.executable, str(SCRIPT), "preflight",
             "--tracker", ".clippy/runs/t.md"],
            cwd=self.repo / "sub", env=self.env,
            capture_output=True, text=True, timeout=60)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PREFLIGHT_OK")
        self.assertEqual(v["tracker"], ".clippy/runs/t.md")

    def test_unit_commit_staged_operator_edit_halts(self):
        # review N3: operator stages an edit on a write-set path
        # mid-unit; the commit seam must halt, never destroy the blob
        self.write("src.txt", "v1\n")
        self.git("add", "src.txt")
        self.git("commit", "-m", "v1")
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        self.write("src.txt", "operator precious\n")
        self.git("add", "src.txt")
        self.write("src.txt", "unit output\n")
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_COMMIT_COLLISION")
        blob = self.git("show", ":src.txt").stdout
        self.assertEqual(blob, "operator precious\n", "staged blob lost")

    def test_unit_commit_staged_new_file_halts_blob_preserved(self):
        # attack-7 B2: the 0.2.35 'A' tolerance destroyed an
        # operator-staged NEW file under a green UNIT_COMMITTED,
        # unrecoverably. Column one cannot attribute a staged add, so
        # the commit seam halts on it; the blocked-prior-attempt
        # leftover never reaches this seam (START catches it and the
        # desk's provenance clearing handles it).
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        start_sha = self.head_sha()
        self.write("src.txt", "OPERATOR PRECIOUS DRAFT\n")
        self.git("add", "src.txt")
        self.write("src.txt", "unit output\n")
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_COMMIT_COLLISION")
        blob = self.git("show", ":src.txt").stdout
        self.assertEqual(blob, "OPERATOR PRECIOUS DRAFT\n",
                         "operator staged blob destroyed")

    def test_lock_commit_failure_after_landed_commit_carries_shas(self):
        # attack-7 B3: a residue-lap commit failure reported with no
        # shas routed as "halts the lock uncommitted" over an orphan
        # lock commit. Arrangement: noisy clean filter (permanent
        # residue) + a pre-commit hook red after the first commit.
        self.git("config", "filter.noisy.clean", "sh -c 'cat; date +%s%N'")
        self.write(".gitattributes", "*.md filter=noisy\n")
        self.git("add", ".gitattributes")
        self.git("commit", "-m", "attr")
        hook = self.repo / ".git" / "hooks" / "pre-commit"
        hook.write_text("#!/bin/sh\n"
                        "[ -f .hook-armed ] && { echo 'pre-commit: test "
                        "suite failed' >&2; exit 1; }\n"
                        "touch .hook-armed\nexit 0\n")
        hook.chmod(0o755)
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        p = self.tool("lock-commit", "--tracker", ".clippy/runs/t.md",
                      "-m", "lock")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "COMMIT_FAILED")
        self.assertGreaterEqual(len(v["shas"]), 1)
        head = self.git("rev-parse", "HEAD").stdout.strip()
        self.assertEqual(v["shas"][0], head)

    def test_lock_commit_rerun_halts_no_changes(self):
        # attack-7 N6: the Close's re-pin rests on HALT_NO_CHANGES
        # ("benign, delivered as-is") with no test that could go red
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        v1 = self.verdict(self.tool("lock-commit",
                                    "--tracker", ".clippy/runs/t.md",
                                    "-m", "pin"))
        self.assertEqual(v1["verdict"], "LOCK_COMMITTED")
        v2 = self.verdict(self.tool("lock-commit",
                                    "--tracker", ".clippy/runs/t.md",
                                    "-m", "pin again"))
        self.assertEqual(v2["verdict"], "HALT_NO_CHANGES")

    def test_unit_commit_ignored_write_set_halts(self):
        # attack-7 N6: the commit seam's ignored-write-set branch had
        # no test that could go red (start's did)
        self.write(".gitignore", "build/\n")
        self.git("add", ".gitignore")
        self.git("commit", "-m", "gi")
        tracker = self.unit_tracker({"U1": ["build/x.txt"]})
        start_sha = self.head_sha()
        (self.repo / "build").mkdir()
        self.write("build/x.txt", "unit output\n")
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_IGNORED_WRITESET")

    def test_unit_start_ignored_write_set_halts(self):
        # review N5: fires at both seams, was routed and tested nowhere
        self.write(".gitignore", "build/\n")
        self.git("add", ".gitignore")
        self.git("commit", "-m", "gi")
        tracker = self.unit_tracker({"U1": ["build/x.txt"]})
        p = self.tool("unit-start", "--tracker", tracker, "--unit", "U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_IGNORED_WRITESET")

    def test_staged_rename_drop_carries_orig_path(self):
        # review NIT 4: a staged rename dropped only the new path.
        # Probed contract: git pairs the rename (R, orig_path) only
        # when BOTH sides sit in the pathspec; a single-side pathspec
        # reports `A ` and the original is unknowable to the tool —
        # both forms must drop, and the paired form carries orig_path.
        self.write("old.txt", "content\n")
        self.git("add", "old.txt")
        self.git("commit", "-m", "old")
        self.git("mv", "old.txt", "new.txt")
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        v1 = self.verdict(self.tool("lock-check",
                                    "--tracker", ".clippy/runs/t.md",
                                    "--lock-set", "new.txt"))
        self.assertEqual(v1["verdict"], "LOCK_CHECK_DROPS")
        self.assertTrue(any(d["path"] == "new.txt" for d in v1["drops"]))
        v2 = self.verdict(self.tool("lock-check",
                                    "--tracker", ".clippy/runs/t.md",
                                    "--lock-set", "new.txt",
                                    "--lock-set", "old.txt"))
        self.assertEqual(v2["verdict"], "LOCK_CHECK_DROPS")
        drop = next(d for d in v2["drops"] if d["path"] == "new.txt")
        self.assertEqual(drop.get("orig_path"), "old.txt")


class TestPureFunctions(unittest.TestCase):
    """The comparison/parsing logic red-proven on constructed defects —
    branches whose triggering git states are races or git-won't-do-it
    cases are certified at function level (instrument rule: a check is
    unproven until it has gone red on the defect it was built for)."""

    def setUp(self):
        sys.path.insert(0, str(SCRIPT.parent))
        import statiker_git
        self.m = statiker_git

    def tearDown(self):
        sys.path.remove(str(SCRIPT.parent))

    def test_porcelain_parse_forms(self):
        raw = b"?? new.txt\x00 M mod.txt\x00MM both.txt\x00A  added.txt\x00R  new-name.txt\x00old-name.txt\x00"
        entries = self.m.parse_porcelain_z(raw)
        by_path = {e.path: e for e in entries}
        self.assertEqual(by_path["new.txt"].x, "?")
        self.assertEqual(by_path["mod.txt"].x, " ")
        self.assertEqual(by_path["mod.txt"].y, "M")
        self.assertEqual(by_path["both.txt"].x, "M")
        self.assertEqual(by_path["added.txt"].x, "A")
        self.assertEqual(by_path["new-name.txt"].x, "R")
        self.assertEqual(by_path["new-name.txt"].orig_path, "old-name.txt")
        self.assertEqual(len(entries), 5)

    def test_staged_collision_excludes_untracked(self):
        # '?' in column one is untracked, not staged operator state
        # (attack-6 B3) — and untracked never reads as a collision here.
        e_unt = self.m.PorcelainEntry("?", "?", "a.txt", None)
        e_wt = self.m.PorcelainEntry(" ", "M", "b.txt", None)
        e_st = self.m.PorcelainEntry("M", " ", "c.txt", None)
        e_both = self.m.PorcelainEntry("M", "M", "d.txt", None)
        self.assertFalse(self.m.is_staged_collision(e_unt))
        self.assertFalse(self.m.is_staged_collision(e_wt))
        self.assertTrue(self.m.is_staged_collision(e_st))
        self.assertTrue(self.m.is_staged_collision(e_both))

    def test_readback_extras_red(self):
        shown = {"a.txt", "sneaked.txt"}
        expected = {"a.txt", "b.txt"}
        self.assertEqual(self.m.readback_extras(shown, expected), {"sneaked.txt"})
        self.assertEqual(self.m.readback_extras({"a.txt"}, expected), set())

    def test_index_lock_error_detector(self):
        self.assertTrue(self.m.is_index_lock_error(
            "fatal: Unable to create '/x/.git/index.lock': File exists."))
        self.assertFalse(self.m.is_index_lock_error(
            "error: pathspec 'x' did not match any file(s)"))

    def test_committed_verdict_wiring_red(self):
        # attack-7 N6: the EXTRAS/RESIDUE verdicts had function-green
        # readback_extras but untested wiring — the decision seam is
        # pure and red-provable on constructed data
        name, d = self.m.lock_committed_verdict(["s1"], {"sneak.txt"}, [])
        self.assertEqual(name, "LOCK_COMMITTED_EXTRAS")
        self.assertEqual(d["extras"], ["sneak.txt"])
        name, d = self.m.lock_committed_verdict(["s1", "s2"], set(), [])
        self.assertEqual(name, "LOCK_COMMITTED")
        self.assertEqual(d["sha"], "s2")
        name, d = self.m.unit_committed_verdict("s1", {"x"}, [])
        self.assertEqual(name, "UNIT_COMMITTED_EXTRAS")
        name, d = self.m.unit_committed_verdict("s1", set(), ["MM a.txt"])
        self.assertEqual(name, "UNIT_COMMITTED_RESIDUE")
        name, d = self.m.unit_committed_verdict("s1", set(), [])
        self.assertEqual(name, "UNIT_COMMITTED")

    def test_queue_spent_grammar(self):
        # P1(2): a queue is SPENT when its LAST NON-BLANK line matches
        # `^LANDED <yyyy-mm-dd> — at line <n>$` (SKILL.md, The attack)
        # — no tool enforcement this version (no subcommand reads a
        # queue file); this pure function is the grammar's own
        # certified reference.
        spent = ("- desk finding one\n"
                "- desk finding two\n"
                "\n"
                "LANDED 2026-08-15 — at line 42\n")
        self.assertTrue(self.m.queue_is_spent(spent))
        unconsumed = "- desk finding one\n- desk finding two\n"
        self.assertFalse(self.m.queue_is_spent(unconsumed))
        # a stale LANDED line buried under a later append is NOT the
        # tail — the queue is live again until its OWN last line lands
        reopened = ("LANDED 2026-08-15 — at line 42\n"
                    "- a fresh finding queued after the landing\n")
        self.assertFalse(self.m.queue_is_spent(reopened))
        self.assertFalse(self.m.queue_is_spent(""))


class TestAttack8NonAsciiReadback(GitFixture):
    """attack-8 B1: `git show --name-only` C-quotes non-ASCII paths
    under default core.quotePath, so the newline readback never matched
    the pathspec and a CLEAN commit reported a false extra — at both
    seams, and in the lock case the false extra is the tracker itself,
    which the desk then names a brief exclusion. The porcelain calls
    were always `-z` and unaffected; the repair makes the show readback
    `-z` too. Each test red against the pre-repair readback."""

    def test_lock_commit_non_ascii_tracker_clean(self):
        tracker = ".clippy/runs/2026-08-07-flächennutzung.md"
        self.write(tracker, "# Run: t\nStatus: [READY]\nPhase: implement\n")
        v = self.verdict(self.tool(
            "lock-commit", "--tracker", tracker, "-m", "lock"))
        self.assertEqual(v["verdict"], "LOCK_COMMITTED",
                         f"false extras: {v.get('extras')}")

    def test_unit_commit_non_ascii_write_set_clean(self):
        # the parallel seam — the carry-across pin (one function, two
        # callers; both proven, not one)
        tracker = self.unit_tracker({"U1": ["grünflächen.py"]})
        start_sha = self.head_sha()
        self.write("grünflächen.py", "x = 1\n")
        v = self.verdict(self.tool(
            "unit-commit", "--tracker", tracker, "--unit", "U1",
            "--start-sha", start_sha, "-m", "unit"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED",
                         f"false extras: {v.get('extras')}")

    def test_quote_worthy_ascii_specials_clean(self):
        # quotePath also fires on '"' and '\'; spaces never quote —
        # the attacker's trigger-set probes (P5), pinned as boundary.
        # P2 GAP (surfaced, not bridged): the record's write-set
        # grammar reads whitespace inside the path field as TWO paths
        # on one line (statiker_record.py write_set_violations,
        # write-set-path-near-miss) — pre-existing record hygiene,
        # unrelated to this lane's design, but P2 makes the git tool
        # DEPEND on that declaration for the first time, so a path
        # this quoting probe used to commit cleanly through a free
        # --write-set CLI arg now blocks at the gate before the commit
        # machinery (which still handles the space fine) ever runs.
        # Report this to the dispatcher as a capability regression.
        tracker = self.unit_tracker({"U1": ["my report.py"]})
        start_sha = self.head_sha()
        self.write("my report.py", "x\n")
        v = self.verdict(self.tool(
            "unit-commit", "--tracker", tracker, "--unit", "U1",
            "--start-sha", start_sha, "-m", "unit"))
        self.assertEqual(v["verdict"], "UNIT_GATE_BLOCKED", v)
        self.assertEqual(v["gate"]["verdict"], "CLOSURE_RECORD_MALFORMED")
        self.assertIn("write-set-path-near-miss",
                      [x["code"] for x in v["gate"]["violations"]])

    def test_real_extras_still_detected_non_ascii(self):
        # the repair must not eat the defect class: a genuinely
        # foreign non-ASCII path in HEAD still reports as an extra,
        # DECODED — matchable against porcelain and pathspec forms
        self.write("früh.txt", "op\n")
        self.git("add", "früh.txt")
        self.write("mine.txt", "unit\n")
        self.git("add", "mine.txt")
        self.git("commit", "-m", "mixed", "--", "früh.txt", "mine.txt")
        sys.path.insert(0, str(SCRIPT.parent))
        self.addCleanup(sys.path.remove, str(SCRIPT.parent))
        self.addCleanup(os.chdir, os.getcwd())
        import statiker_git
        os.chdir(self.repo)
        shown = statiker_git.Repo().head_shown_paths()
        self.assertEqual(shown, {"früh.txt", "mine.txt"})


class TestAttack9PathDecoding(GitFixture):
    """attack-9: git's byte output was decoded with errors='replace'
    while argv decodes surrogateescape — one non-UTF-8 byte in a path
    yields TWO spellings of the same name, so the readback reports a
    false extra and the drop handshake can never match (the
    acknowledged spelling comes from argv, the live one from
    porcelain: HALT_DROPS_STALE forever). Each test red against the
    errors='replace' decode."""

    NAME = os.fsdecode(b"caf\xe9.txt")
    TRACKER = ".clippy/runs/t.md"

    def test_unit_commit_non_utf8_byte_path_clean(self):
        # E-C: the verdict's own byte (ensure_ascii=False) is now the
        # raw byte, invalid UTF-8 alone — tool_raw/verdict_raw, never
        # self.tool()/self.verdict() (text=True would crash reading it).
        # The tracker itself carries the raw byte too (surrogateescape
        # encode on write — Path.write_text's default codec would
        # reject it outright).
        tracker_rel = "unit.md"
        body = (self.CLOSED_TRACKER +
               f"- F2 [VERIFIED] unit U1 write-set: {self.NAME} "
               "— basis: design\n")
        (self.repo / tracker_rel).write_bytes(
            body.encode("utf-8", "surrogateescape"))
        start_sha = self.head_sha()
        (self.repo / self.NAME).write_bytes(b"unit output\n")
        v = self.verdict_raw(self.tool_raw(
            "unit-commit", "--tracker", tracker_rel, "--unit", "U1",
            "--start-sha", start_sha, "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED",
                         f"false extras: {v.get('extras')}")
        self.assertEqual(v["write_set"], [self.NAME])

    def test_lock_drop_handshake_completes_non_utf8_byte_path(self):
        (self.repo / self.NAME).write_bytes(b"operator staged\n")
        self.git("add", self.NAME)
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v1 = self.verdict_raw(self.tool_raw(
            "lock-check", "--tracker", self.TRACKER,
            "--lock-set", self.NAME))
        self.assertEqual(v1["verdict"], "LOCK_CHECK_DROPS")
        self.assertEqual([d["path"] for d in v1["drops"]], [self.NAME],
                         "porcelain spelling differs from the argv one")
        v2 = self.verdict_raw(self.tool_raw(
            "lock-commit", "--tracker", self.TRACKER,
            "--lock-set", self.NAME, "--drop", self.NAME, "-m", "lock"))
        self.assertEqual(v2["verdict"], "LOCK_COMMITTED",
                         "the drop handshake never matches")
        # the staged operator content survives untouched
        status = self.git("status", "--porcelain", "--", self.NAME).stdout
        self.assertTrue(status.startswith("A "), status)

    def test_F4_drop_handshake_verdict_carries_the_raw_byte_literally(self):
        # begehung tier2-without.md F4: pre-fix, ensure_ascii's default
        # \udce9 escape is six literal ASCII characters — pasting them
        # types something that can never equal the real byte, so every
        # pasteable spelling (the escape, or the evidence line's
        # errors="replace" '?') halts HALT_DROPS_STALE forever, and the
        # one spelling that WOULD match (the real argv byte) is "the
        # one spelling the tool never prints". Post-fix (ensure_ascii=
        # False + say()'s byte-level write), the raw byte itself sits
        # in the verdict's JSON text on the wire.
        (self.repo / self.NAME).write_bytes(b"operator staged\n")
        self.git("add", self.NAME)
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        p = self.tool_raw("lock-check", "--tracker", self.TRACKER,
                          "--lock-set", self.NAME)
        self.assertIn(b"\xe9", p.stdout,
                      f"the raw byte never reaches stdout: {p.stdout!r}")
        self.assertNotIn(b"udce9", p.stdout,
                         "the byte shipped as a literal escape sequence "
                         "a desk could paste, never equal to the byte "
                         f"it names: {p.stdout!r}")

    # SENTENCE-A3's paste-line test retired with the feature (P2: the
    # write-set is read FROM the tracker, no longer printed back to be
    # pasted). Byte fidelity for a non-UTF-8 write-set path now lives
    # entirely on the record side (statiker_record.py's own ES-9/E-C
    # byte tests) plus the git tool's UNIT_START_CLEAN write_set field,
    # covered by test_unit_commit_non_utf8_byte_path_clean below for
    # the commit seam.


class TestEJStderrFallbackByteFidelity(GitFixture):
    """E-J (BACKLOG, provenance lane G gap report 2/4): pre-fix,
    `_stderr_fallback` used text-mode `print(text, file=sys.stderr)`
    — main() reconfigures stderr with errors="replace", so the
    surrogateescape-decoded non-UTF-8 byte inside a verdict's own
    detail (E-C's own `caf\\xe9.txt` path shape) is silently minted a
    SECOND spelling (replaced by U+FFFD) rather than reaching stderr
    as the byte it names. The record tool's mirror
    (statiker_record.py:351-356) writes the buffer directly with
    surrogateescape, immune to the substitution. Arrangement: stdout
    closed before any read (guarantees a broken pipe on the first
    evidence write, same as record.py's TestHarvest2BrokenPipeVerdict),
    forcing the UNIT_COMMITTED verdict itself — carrying the raw byte
    in write_set — down the stderr fallback path."""

    NAME = os.fsdecode(b"caf\xe9.txt")

    def test_broken_pipe_stderr_fallback_carries_the_raw_byte(self):
        tracker_rel = "unit.md"
        body = (self.CLOSED_TRACKER +
               f"- F2 [VERIFIED] unit U1 write-set: {self.NAME} "
               "— basis: design\n")
        (self.repo / tracker_rel).write_bytes(
            body.encode("utf-8", "surrogateescape"))
        start_sha = self.head_sha()
        (self.repo / self.NAME).write_bytes(b"unit output\n")
        proc = subprocess.Popen(
            [sys.executable, str(SCRIPT), "unit-commit",
             "--tracker", tracker_rel, "--unit", "U1",
             "--start-sha", start_sha, "-m", "unit U1"],
            cwd=self.repo, env=self.env,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.stdout.close()   # closed before any read: guarantees EPIPE
        err = proc.stderr.read()
        proc.wait(timeout=10)
        self.assertEqual(proc.returncode, 3, err)
        lines = [l for l in split_lines(err.decode("utf-8", "surrogateescape"))
                if l.startswith(VERDICT_PREFIX)]
        self.assertEqual(len(lines), 1, err)
        self.assertIn('"verdict": "UNIT_COMMITTED"', lines[0], err)
        self.assertIn(b"\xe9", err,
                      f"the raw byte never reached the stderr fallback "
                      f"(text-mode print minted a second spelling instead): "
                      f"{err!r}")


class TestF9PostCommitHookWindowOccupier(GitFixture):
    """begehung tier2-without.md F9 (round 2, BLOCKING): a post-commit
    hook that lands a sibling commit occupies the window between our
    own `git commit` and a LATER separate `rev-parse HEAD` read — the
    same mechanism SKILL.md's own capped-retry contention design
    admits for a live sibling unit sharing one index. Pre-fix,
    commit_with_retry's separate rev-parse HEAD names the hook's own
    commit (HEAD has already moved by the time it runs — the hook
    finishes synchronously inside the outer `git commit` call), and
    a bare-HEAD head_shown_paths() then shows the sibling's diff: the
    booked sha is the sibling's, and the sibling's own file books as
    a false extra (UNIT_COMMITTED_EXTRAS over a legitimate file)."""

    def install_post_commit_hook(self):
        # runs once — the guard file's own presence, checked before
        # the hook's own git commit fires a recursive post-commit —
        # is what stops it invoking itself forever.
        hook = self.repo / ".git" / "hooks" / "post-commit"
        hook.write_text(
            "#!/bin/sh\n"
            "if [ ! -f sibling.txt ]; then\n"
            "  echo sibling > sibling.txt\n"
            "  git add sibling.txt\n"
            "  git commit -m 'sibling landed by hook' -- sibling.txt\n"
            "fi\n"
        )
        hook.chmod(0o755)

    def test_unit_commit_names_its_own_sha_under_a_hook_occupied_window(self):
        self.install_post_commit_hook()
        tracker = self.unit_tracker({"U1": ["unit.txt"]})
        start_sha = self.head_sha()
        self.write("unit.txt", "unit output\n")
        v = self.verdict(self.tool(
            "unit-commit", "--tracker", tracker, "--unit", "U1",
            "--start-sha", start_sha, "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED",
                         f"false extras from the hook's own sibling "
                         f"commit: {v}")
        self.assertEqual(v["write_set"], ["unit.txt"])
        # the hook really landed its sibling commit — proves the window
        # was genuinely occupied, not a no-op hook that never fired
        log = self.git("log", "--oneline", "--all").stdout
        self.assertIn("sibling landed by hook", log, log)
        # the booked sha must be the commit that actually carries
        # unit.txt, never the hook's later sibling commit
        shown = self.git("show", "--name-only", "--format=", v["sha"]).stdout
        self.assertIn("unit.txt", shown, shown)
        self.assertNotIn("sibling.txt", shown, shown)


class TestAttack9SymlinkContainment(GitFixture):
    """attack-9: rel() resolved paths through symlinks, so a booked
    verdict named a path the brief never wrote (the link's TARGET),
    and a tracked in-repo link pointing outward halted the unit
    outright. The as-named booking survives; the ACCEPTANCE of a
    symlink LEAF does not — 0.2.49's ES-7 halts it at every
    path-accepting seam (git accepts a link leaf and commits the link
    string; no dry-run catches it, so the halt lands at a check)."""

    def test_unit_commit_halts_on_a_symlink_leaf(self):
        # REVERSED by ES-7: at base this committed the link string
        tracker = self.unit_tracker({"U1": ["alias.py"]})
        start_sha = self.head_sha()
        self.write("realdir/target.py", "x = 1\n")
        os.symlink("realdir/target.py", self.repo / "alias.py")
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertIn("alias.py", v["error"])
        self.assertEqual(self.head_paths(), {"base.txt"},
                         "the link was committed anyway")

    def test_unit_start_halts_on_a_link_resolving_out_of_the_repo(self):
        # REVERSED by ES-7: containment is decided on the REAL path
        tracker = self.unit_tracker({"U1": ["link.py"]})
        ext = Path(self._tmp.name) / "ext"
        ext.mkdir()
        (ext / "real.py").write_text("x = 1\n")
        os.symlink("../ext/real.py", self.repo / "link.py")
        self.git("add", "link.py")
        self.git("commit", "-m", "link")
        v = self.verdict(self.tool("unit-start", "--tracker", tracker,
                                   "--unit", "U1"))
        self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO")
        self.assertIn("resolved_from", v)

    def test_repo_root_still_routes_as_a_directory_path(self):
        # the containment repair must not re-route the repo root out
        # of the directory check: '.' is a directory pathspec, which
        # sweeps whatever the operator touched under it
        tracker = self.unit_tracker({"U1": ["."]})
        v = self.verdict(self.tool("unit-start", "--tracker", tracker,
                                   "--unit", "U1"))
        self.assertEqual(v["verdict"], "HALT_DIRECTORY_PATH")

    def test_literal_dotdot_escape_still_halts(self):
        # the containment rule the repair must not eat: a path naming
        # its way out of the repo is still outside it
        tracker = self.unit_tracker({"U1": ["../outside.py"]})
        (Path(self._tmp.name) / "outside.py").write_text("x = 1\n")
        p = self.tool("unit-start", "--tracker", tracker, "--unit", "U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO")
        self.assertNotEqual(p.returncode, 0)


class TestAttack10SymlinkedAncestor(GitFixture):
    """attack-10 N4: containment compares a TEXTUAL path against the
    repo top's REALPATH, so a path reached through a symlinked
    ANCESTOR of the top — the spelling git itself resolves away when
    it reports the toplevel — read as a path outside the repo. Only
    the ANCESTOR rebases: everything below it is still taken as named
    (SKILL.md, The tools), and a literal `..` escape still halts."""

    def linked(self):
        """(real_top, link_top) for a repo under a symlinked ancestor."""
        base = Path(self._tmp.name) / "anc"
        (base / "real" / "inner").mkdir(parents=True)
        os.symlink(str(base / "real"), str(base / "link"))
        real = base / "real" / "inner"
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=real,
                       env=self.env, capture_output=True, check=True)
        return real, base / "link" / "inner"

    def run_at(self, cwd, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args], cwd=str(cwd),
            env=self.env, capture_output=True, text=True, timeout=60)

    def test_preflight_ok_from_both_spellings_and_both_cwds(self):
        real, link = self.linked()
        (real / "t.md").write_text("# Run: t\n")
        for cwd in (real, link):
            for tracker in (real / "t.md", link / "t.md"):
                v = self.verdict(self.run_at(cwd, "preflight",
                                             "--tracker", str(tracker)))
                self.assertEqual(v["verdict"], "PREFLIGHT_OK",
                                 f"cwd={cwd} tracker={tracker}")
                self.assertEqual(v["tracker"], "t.md")

    def track_at(self, real):
        (real / ".clippy" / "runs").mkdir(parents=True)
        (real / ".clippy" / "runs" / "t.md").write_text(
            self.GATE_CLEAN_TRACKER)

    # P2: unit-start's write-set is now DECLARED in the tracker, and
    # the record's own write-set grammar rejects a leading '/' as an
    # absolute/symlinked-spelling defect (write-set-path-near-miss) —
    # exactly the ABSOLUTE spelling these three probes exist to drive
    # through repo.rel()'s symlinked-ancestor rebase. That rebase is
    # rel()'s own shared machinery, exercised identically through
    # lock-check's still-free `--lock-set` (never touched by P2),
    # which migrates the probe without losing what it tests.

    def test_lock_check_clean_through_the_link_spelling(self):
        real, link = self.linked()
        self.track_at(real)
        (real / "src.txt").write_text("x\n")
        v = self.verdict(self.run_at(
            link, "lock-check", "--tracker", ".clippy/runs/t.md",
            "--lock-set", str(link / "src.txt")))
        self.assertEqual(v["verdict"], "LOCK_CHECK_CLEAN", v)
        self.assertIn("src.txt", v["adds"])

    def test_dotdot_escape_through_the_link_still_halts(self):
        # the containment rule the rebase must not eat
        real, link = self.linked()
        self.track_at(real)
        (Path(self._tmp.name) / "anc" / "real" / "outside.py").write_text("x\n")
        p = self.run_at(link, "lock-check", "--tracker", ".clippy/runs/t.md",
                        "--lock-set", str(link / ".." / "outside.py"))
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO")
        self.assertNotEqual(p.returncode, 0)

    def test_link_below_the_top_halts_as_a_symlink_leaf(self):
        # REVERSED by ES-7: the link is still never RESOLVED (the
        # booking would name its target), but a link LEAF no longer
        # reaches a commit — it halts at the check
        real, link = self.linked()
        self.track_at(real)
        (real / "realdir").mkdir()
        (real / "realdir" / "target.py").write_text("x = 1\n")
        os.symlink("realdir/target.py", real / "alias.py")
        for a in (["add", "alias.py", "realdir/target.py"],
                  ["commit", "-m", "link"]):
            subprocess.run(["git", *a], cwd=real, env=self.env,
                           capture_output=True, check=True)
        v = self.verdict(self.run_at(
            link, "lock-check", "--tracker", ".clippy/runs/t.md",
            "--lock-set", str(link / "alias.py")))
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertIn("alias.py", v["error"])


class TestAttack10NonUtf8RepoDir(GitFixture):
    """attack-10 N5: the toplevel read was `text=True`, so a repo whose
    DIRECTORY NAME carries a non-UTF-8 byte died of a
    UnicodeDecodeError inside the never-a-silent-death handler —
    INTERNAL_ERROR out of every subcommand, in a repo git itself
    handles fine. Path BYTES decode the way the OS decodes argv
    (SKILL.md, The tools); the toplevel read is a path read."""

    TRACKER = ".clippy/runs/t.md"

    def bad_repo(self):
        d = Path(self._tmp.name) / os.fsdecode(b"repo-\xff")
        d.mkdir()
        for a in (["init", "-q", "-b", "main"], ["add", "base.txt"],
                  ["commit", "-m", "base"]):
            if a[0] == "add":
                (d / "base.txt").write_text("base\n")
            subprocess.run(["git", *a], cwd=d, env=self.env,
                           capture_output=True, check=True)
        return d

    def test_every_subcommand_works_in_a_non_utf8_repo_dir(self):
        d = self.bad_repo()

        def run(*args):
            return subprocess.run(
                [sys.executable, str(SCRIPT), *args], cwd=str(d),
                env=self.env, capture_output=True, text=True, timeout=60)

        def check(expected, *args, prep=None):
            if prep is not None:
                prep()
            p = run(*args)
            v = self.verdict(p)
            self.assertEqual(v["verdict"], expected,
                             f"{' '.join(args)} -> {v}")

        (d / ".clippy" / "runs").mkdir(parents=True)
        check("STATE_CLEAN", "state-gate")
        check("PREFLIGHT_OK", "preflight", "--tracker", self.TRACKER)
        check("LOCK_CHECK_CLEAN", "lock-check", "--tracker", self.TRACKER,
              prep=lambda: (d / self.TRACKER).write_text(self.GATE_CLEAN_TRACKER))
        check("LOCK_COMMITTED", "lock-commit", "--tracker", self.TRACKER,
              "-m", "lock")
        start_sha = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=d, env=self.env,
            capture_output=True, text=True, check=True).stdout.strip()
        check("UNIT_START_CLEAN", "unit-start", "--tracker", "unit.md",
              "--unit", "U1",
              prep=lambda: (d / "unit.md").write_text(
                  self.CLOSED_TRACKER +
                  "- F2 [VERIFIED] unit U1 write-set: src.txt "
                  "— basis: design\n"))
        check("UNIT_COMMITTED", "unit-commit", "--tracker", "unit.md",
              "--unit", "U1", "--start-sha", start_sha, "-m", "unit U1",
              prep=lambda: (d / "src.txt").write_text("unit output\n"))


class TestAttack10PathExistence(GitFixture):
    """attack-10 N8/NIT1: two existence reads that answered about the
    wrong thing — `exists()` follows the link, so a write-set path that
    IS a symlink with a missing target halted HALT_MISSING_PATH though
    git commits the link file itself; and preflight never asked whether
    the tracker path is a FILE at all."""

    def test_broken_symlink_write_set_halts_as_a_symlink_leaf(self):
        # REVERSED by ES-7: lexists still tells a broken link from a
        # missing path (it is not HALT_MISSING_PATH), but a link leaf
        # halts rather than committing the link string
        tracker = self.unit_tracker({"U1": ["alias.py"]})
        start_sha = self.head_sha()
        os.symlink("no-such-target.py", self.repo / "alias.py")
        v = self.verdict(self.tool("unit-commit", "--tracker", tracker,
                                   "--unit", "U1", "--start-sha", start_sha,
                                   "-m", "unit U1"))
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertIn("alias.py", v["error"])
        self.assertEqual(self.head_paths(), {"base.txt"})

    def test_broken_symlink_halts_at_the_lock_pathspec_too(self):
        # the parallel seam (one function, two callers)
        os.symlink("no-such-target.py", self.repo / "alias.py")
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool(
            "lock-check", "--tracker", ".clippy/runs/t.md",
            "--lock-set", "alias.py"))
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertIn("alias.py", v["error"])

    def test_missing_write_set_path_still_halts(self):
        # the boundary the lexists repair must not eat
        tracker = self.unit_tracker({"U1": ["never-made.txt"]})
        start_sha = self.head_sha()
        p = self.tool("unit-commit", "--tracker", tracker, "--unit", "U1",
                      "--start-sha", start_sha, "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_MISSING_PATH")

    def test_preflight_on_a_directory_tracker_halts(self):
        for tracker in (".", "docs"):
            self.write("docs/a.txt", "a\n")
            p = self.tool("preflight", "--tracker", tracker)
            v = self.verdict(p)
            self.assertEqual(v["verdict"], "HALT_DIRECTORY_PATH",
                             f"--tracker {tracker!r} -> {v}")
            self.assertNotEqual(p.returncode, 0)

    def test_preflight_on_a_not_yet_written_tracker_is_ok(self):
        # the boundary: at run start the tracker does not exist yet
        v = self.verdict(self.tool("preflight",
                                   "--tracker", ".clippy/runs/t.md"))
        self.assertEqual(v["verdict"], "PREFLIGHT_OK")


# ================================================================= 0.2.49
# The git tool's half of the executable spec (docs/directives/
# executable-spec-settle.md): ES-7's containment seams and ES-11's
# residue from the 0.2.46 code-only list. Cases marked GREEN-AT-BASE
# are regression pins, not part of the red-first list.


class TestES7Containment(GitFixture):
    """ES-7 (R3-B7): must-be-inside containment is decided on the REAL
    path. The ancestor probe is NAMED — walk to the path's nearest
    EXISTING ancestor; the path is inside only when that ancestor's
    realpath sits inside (or equals) the repo top's realpath. The
    operation still runs on the as-named spelling, with
    `resolved_from` noted per path whenever the two differ."""

    def link_dir(self, target):
        os.symlink(str(target), self.repo / "linkdir")

    def test_write_set_beyond_an_in_repo_link_pointing_out_halts(self):
        # the settle's own red case: at base the path is taken as
        # named, accepted, and a unit writes OUTSIDE the repo before
        # any check knows it
        tracker = self.unit_tracker({"U1": ["linkdir/x.txt"]})
        out = Path(self._tmp.name) / "elsewhere"
        out.mkdir()
        (out / "x.txt").write_text("operator file\n")
        self.link_dir(out)
        p = self.tool("unit-start", "--tracker", tracker, "--unit", "U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO")
        self.assertEqual(v["path"], "linkdir/x.txt",
                         "the halt renamed the path it was given")
        self.assertIn(str(out / "x.txt"), v["resolved_from"]["real"])
        self.assertNotEqual(p.returncode, 0)

    def test_resolved_from_is_noted_when_the_two_spellings_differ(self):
        # accepted, because the link points INSIDE — and the verdict
        # says so per path, the operation still on the named spelling
        tracker = self.unit_tracker({"U1": ["linkdir/x.txt"]})
        (self.repo / "realdir").mkdir()
        (self.repo / "realdir" / "x.txt").write_text("run content\n")
        self.link_dir(self.repo / "realdir")
        v = self.verdict(self.tool("unit-start", "--tracker", tracker,
                                   "--unit", "U1"))
        self.assertEqual(v["verdict"], "UNIT_START_CLEAN")
        self.assertEqual(v["write_set"], ["linkdir/x.txt"])
        named = [r["named"] for r in v["resolved_from"]]
        self.assertEqual(named, ["linkdir/x.txt"])

    def test_clean_paths_carry_no_resolved_from_noise(self):
        # GREEN-AT-BASE boundary: the note appears only where the two
        # computations differ
        tracker = self.unit_tracker({"U1": ["src.txt"]})
        v = self.verdict(self.tool("unit-start", "--tracker", tracker,
                                   "--unit", "U1"))
        self.assertEqual(v["verdict"], "UNIT_START_CLEAN")
        self.assertNotIn("resolved_from", v)

    def test_symlink_leaf_halts_at_every_path_accepting_seam(self):
        (self.repo / "realdir").mkdir()
        (self.repo / "realdir" / "x.txt").write_text("content\n")
        os.symlink("realdir/x.txt", self.repo / "alias.py")
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        tracker = self.unit_tracker({"U1": ["alias.py"]}, rel="unitseam.md")
        start_sha = self.head_sha()
        seams = (
            ("unit-start", "--tracker", tracker, "--unit", "U1"),
            ("unit-commit", "--tracker", tracker, "--unit", "U1",
             "--start-sha", start_sha, "-m", "unit U1"),
            ("lock-check", "--tracker", ".clippy/runs/t.md",
             "--lock-set", "alias.py"),
            ("lock-commit", "--tracker", ".clippy/runs/t.md",
             "--lock-set", "alias.py", "-m", "lock"),
            ("preflight", "--tracker", "alias.py"),
        )
        for seam in seams:
            p = self.tool(*seam)
            v = self.verdict(p)
            self.assertEqual(v["verdict"], "USAGE_ERROR",
                             f"{seam[0]} accepted a symlink leaf -> {v}")
            self.assertEqual(p.returncode, 3, seam[0])
        self.assertEqual(self.head_paths(), {"base.txt"},
                         "a seam committed the link string anyway")


class TestES11GitResidue(GitFixture):
    """ES-11: the attack-11 N5/N8 residue from the 0.2.46 code-only
    list — ADD_FAILED and GIT_ERROR unfrozen with the attacker's own
    recipes, preflight's dedicated repo-health read strict, and a
    staged rename's drop excluding BOTH halves."""

    TRACKER = ".clippy/runs/t.md"

    def test_lock_check_dry_runs_its_adds(self):
        # the attacker's ADD_FAILED recipe: a path git REFUSES though
        # containment accepts it ("pathspec is beyond a symbolic
        # link"). Containment and git-acceptability are separate
        # questions; the halt must land at the CHECK, not the commit.
        (self.repo / "realdir").mkdir()
        (self.repo / "realdir" / "x.txt").write_text("run content\n")
        os.symlink("realdir", self.repo / "linkdir")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        p = self.tool("lock-check", "--tracker", self.TRACKER,
                      "--lock-set", "linkdir/x.txt")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "ADD_FAILED")
        self.assertIn("symbolic link", v["error"])
        self.assertNotEqual(p.returncode, 0)

    def test_preflight_health_read_halts_on_a_corrupt_index(self):
        # the attacker's GIT_ERROR recipe: at base preflight passed
        # CLEAN over a corrupt index (every read check=False) and the
        # run started on a repo no later seam could commit to
        (self.repo / ".git" / "index").write_bytes(b"GARBAGE-NOT-AN-INDEX")
        p = self.tool("preflight", "--tracker", self.TRACKER)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "GIT_ERROR")
        self.assertIn("index", v["stderr"])

    def test_other_reads_keep_their_documented_exit_semantics(self):
        # GREEN-AT-BASE boundary: strictness is the health read's
        # alone — a not-ignored answer (exit 1) is an answer
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v = self.verdict(self.tool("preflight", "--tracker", self.TRACKER))
        self.assertEqual(v["verdict"], "PREFLIGHT_OK")

    def test_staged_rename_drop_excludes_both_halves(self):
        # attack-11 N8: the deletion half stayed in the effective
        # pathspec, so the lock commit landed the operator's staged
        # rename half through a satisfied drop handshake
        self.write("old.txt", "content\n")
        self.git("add", "old.txt")
        self.git("commit", "-m", "old")
        self.git("mv", "old.txt", "new.txt")
        self.write(self.TRACKER, self.GATE_CLEAN_TRACKER)
        v1 = self.verdict(self.tool(
            "lock-check", "--tracker", self.TRACKER,
            "--lock-set", "new.txt", "--lock-set", "old.txt"))
        self.assertEqual(v1["verdict"], "LOCK_CHECK_DROPS")
        v2 = self.verdict(self.tool(
            "lock-commit", "--tracker", self.TRACKER,
            "--lock-set", "new.txt", "--lock-set", "old.txt",
            "--drop", "new.txt", "-m", "lock"))
        self.assertEqual(v2["verdict"], "LOCK_COMMITTED")
        self.assertEqual(self.head_paths(), {self.TRACKER},
                         "the rename's deletion half rode into the lock")
        # the operator's staged rename survives untouched
        status = self.git("status", "--porcelain").stdout
        self.assertIn("R  old.txt -> new.txt", status)


# -------------------------------------------------------------- worktree
# Backlog: "worktree provisioning joins the git tool" (0.2.57 review N1):
# hand-run `git worktree add/remove` has no verdict to book and no halt
# route; dirty removal needs `--force` on its normal path.

class TestWorktreeAdd(GitFixture):
    def test_clean_add_at_locked_sha(self):
        sha = self.git("rev-parse", "HEAD").stdout.strip()
        wt = Path(self._tmp.name) / "wt1"
        v = self.verdict(self.tool("worktree-add", "--sha", sha,
                                   "--path", str(wt)))
        self.assertEqual(v["verdict"], "WORKTREE_ADDED")
        self.assertEqual(v["sha"], sha)
        # read HEAD from the new worktree directly (not via self.git,
        # which is cwd-pinned to the main repo)
        wt_head = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=wt, env=self.env,
            capture_output=True, text=True, check=True).stdout.strip()
        self.assertEqual(wt_head, sha)
        # detached, never a new branch on the provisioned worktree
        branch = subprocess.run(
            ["git", "symbolic-ref", "-q", "HEAD"], cwd=wt, env=self.env,
            capture_output=True, text=True, check=False)
        self.assertNotEqual(branch.returncode, 0, "worktree is not detached")

    def test_path_inside_repo_halts(self):
        # git itself will happily nest a worktree inside a repo; the
        # halt has to land at the tool, before git ever runs
        sha = self.git("rev-parse", "HEAD").stdout.strip()
        p = self.tool("worktree-add", "--sha", sha, "--path", "inner-wt")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PATH_INSIDE_REPO")
        self.assertNotEqual(p.returncode, 0)
        self.assertEqual(
            subprocess.run(["git", "worktree", "list"], cwd=self.repo,
                           env=self.env, capture_output=True,
                           text=True).stdout.count("\n"),
            1, "a worktree was registered despite the halt")

    def test_repo_root_itself_halts_as_inside(self):
        v = self.verdict(self.tool("worktree-add", "--sha",
                                   self.git("rev-parse", "HEAD").stdout.strip(),
                                   "--path", "."))
        self.assertEqual(v["verdict"], "PATH_INSIDE_REPO")

    def test_bad_sha_reports_git_error(self):
        p = self.tool("worktree-add", "--sha", "not-a-real-sha",
                      "--path", str(Path(self._tmp.name) / "wt-bad"))
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "GIT_ERROR")
        self.assertNotEqual(p.returncode, 0)


class TestWorktreeRemove(GitFixture):
    def add_worktree(self, name="wt1"):
        sha = self.git("rev-parse", "HEAD").stdout.strip()
        wt = Path(self._tmp.name) / name
        v = self.verdict(self.tool("worktree-add", "--sha", sha,
                                   "--path", str(wt)))
        self.assertEqual(v["verdict"], "WORKTREE_ADDED", v)
        return wt

    def test_dirty_worktree_removes_green_through_the_tool(self):
        wt = self.add_worktree()
        (wt / "byproduct.txt").write_text("run leftover\n")
        v = self.verdict(self.tool("worktree-remove", "--path", str(wt)))
        self.assertEqual(v["verdict"], "WORKTREE_REMOVED")
        self.assertFalse(wt.exists())

    def test_dirty_worktree_removal_red_without_force(self):
        # the RED arm: plain git, no --force, on the same dirty
        # worktree the tool above removes clean
        wt = self.add_worktree(name="wt-red")
        (wt / "byproduct.txt").write_text("run leftover\n")
        p = subprocess.run(["git", "worktree", "remove", str(wt)],
                           cwd=self.repo, env=self.env,
                           capture_output=True, text=True)
        self.assertNotEqual(p.returncode, 0,
                            "plain git worktree remove unexpectedly "
                            "succeeded on a dirty worktree")
        self.assertTrue(wt.exists(), "worktree removed without --force")

    def test_path_inside_repo_halts(self):
        p = self.tool("worktree-remove", "--path", "docs")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PATH_INSIDE_REPO")
        self.assertNotEqual(p.returncode, 0)


# ------------------------------------------------ worktree-add containment

class TestWorktreeAddEveryRepoContainment(GitFixture):
    """0.2.59 review F1+F2, worktree-add containment joins the record
    tool's `--out` semantics (BACKLOG.md): `Repo.outside()` gains the
    every-enclosing-repo probe (git_toplevel + textual_repo_top,
    mirroring cmd_filter) and the named/real agreement rule —
    PATH_INSIDE_REPO fires on any enclosing repo, not just this one,
    and on as-named/real disagreement, not just a real-side escape.

    Both probes walk from the target's PARENT: a legitimately
    provisioned worktree is itself a valid (linked) repo by the time
    worktree-remove meets it again, and `git rev-parse
    --show-toplevel` run from inside one reports the worktree's own
    root — checking the target ITSELF would read every real worktree
    as its own containing repo (caught red during this fix's own
    development: worktree-remove on a real outside-dir worktree
    regressed to PATH_INSIDE_REPO before the parent-walk correction)."""

    def sibling_repo(self, name):
        d = Path(self._tmp.name) / name
        d.mkdir()
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=d,
                       env=self.env, check=True)
        (d / "base.txt").write_text("base\n")
        subprocess.run(["git", "add", "base.txt"], cwd=d, env=self.env,
                       check=True)
        subprocess.run(["git", "commit", "-m", "base"], cwd=d, env=self.env,
                       check=True)
        return d

    def test_worktree_add_into_a_sibling_repo_halts_and_pollutes_nothing(self):
        # F1: from repo A, --path ../B/wt-in-B used to read
        # WORKTREE_ADDED and leave `?? wt-in-B/` in sibling B's tree
        sha = self.git("rev-parse", "HEAD").stdout.strip()
        b = self.sibling_repo("B")
        p = self.tool("worktree-add", "--sha", sha,
                      "--path", str(b / "wt-in-B"))
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PATH_INSIDE_REPO", v)
        status = subprocess.run(["git", "status", "--porcelain"], cwd=b,
                                env=self.env, capture_output=True,
                                text=True, check=True).stdout
        self.assertEqual(status, "", "sibling B's tree was polluted")

    def test_symlink_spelling_into_the_repo_halts(self):
        # F2: `link/wt` (link -> a real outside dir) used to read
        # WORKTREE_ADDED — the as-named walk reaches this repo's own
        # .git through the symlinked component, exactly the shape
        # `filter --out link/art.md` already halts on (ES-7)
        outside = Path(self._tmp.name) / "outside-dir"
        outside.mkdir()
        (self.repo / "link").symlink_to(outside)
        sha = self.git("rev-parse", "HEAD").stdout.strip()
        v = self.verdict(self.tool("worktree-add", "--sha", sha,
                                   "--path", "link/wt"))
        self.assertEqual(v["verdict"], "PATH_INSIDE_REPO", v)

    def test_outside_dir_worktree_still_adds_and_removes_clean(self):
        # must-not-fire: the existing, legitimate case — provisioned
        # at a real directory outside every repo, then removed again
        # (the round trip the parent-walk correction protects)
        sha = self.git("rev-parse", "HEAD").stdout.strip()
        wt = Path(self._tmp.name) / "legit-wt"
        v = self.verdict(self.tool("worktree-add", "--sha", sha,
                                   "--path", str(wt)))
        self.assertEqual(v["verdict"], "WORKTREE_ADDED", v)
        v = self.verdict(self.tool("worktree-remove", "--path", str(wt)))
        self.assertEqual(v["verdict"], "WORKTREE_REMOVED", v)


# -------------------------------------------------- begehung-harvest 2 (d)/(d2)

class TestHarvest2BrokenPipeAndRetryBaseEnv(GitFixture):
    """begehung-harvest 2 (d) + AMENDED (d2) (tier2-without.md part
    7/7 + dev-notes/triage-three-arm-2026-08-15.md T3's sibling
    class): the same one-verdict-line guarantee this suite's sibling
    (statiker_record.py) carries, joined here.

    (d) A closed reader broke the pipe mid-run with no catch — say()
    now swallows a BrokenPipeError on an evidence line and remembers
    it, finish() falls back to stderr with a defined exit code (3),
    and the stdout fd is redirected to devnull first so CPython's own
    interpreter-finalization flush cannot override that exit code
    with its hardcoded 120.

    (d2) `STATIKER_GIT_RETRY_BASE`'s float() sat at module level,
    outside main()'s guarded try — a bad value died a bare traceback,
    exit 1, no verdict line, even for state-gate, which never reads
    it. `_read_retry_base()` now runs inside the guarded region and
    routes a bad value USAGE_ERROR, same defined exit code as (d)."""

    def test_a_closed_reader_still_gets_exactly_one_verdict_line(self):
        tracker = self.unit_tracker(
            {"U1": ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt"]})
        proc = subprocess.Popen(
            [sys.executable, str(SCRIPT), "unit-start",
             "--tracker", tracker, "--unit", "U1"],
            cwd=self.repo, env=self.env,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.stdout.close()   # closed before any read: guarantees EPIPE
        err = proc.stderr.read()
        proc.wait(timeout=10)
        self.assertEqual(proc.returncode, 3, err)
        lines = [l for l in split_lines(err.decode("utf-8", "surrogateescape"))
                if l.startswith(VERDICT_PREFIX)]
        self.assertEqual(len(lines), 1, err)
        self.assertIn('"verdict": "UNIT_START_CLEAN"', lines[0])

    def test_a_bad_retry_base_halts_usage_error_not_a_bare_traceback(self):
        env = dict(self.env)
        env["STATIKER_GIT_RETRY_BASE"] = "abc"
        p = subprocess.run([sys.executable, str(SCRIPT), "state-gate"],
                           cwd=self.repo, env=env,
                           capture_output=True, text=True, timeout=10)
        self.assertEqual(p.returncode, 3, p.stdout + p.stderr)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "USAGE_ERROR", v)
        self.assertIn("STATIKER_GIT_RETRY_BASE", v.get("error", ""), v)

    def test_a_good_retry_base_still_reaches_state_clean(self):
        # the guard must not cost the happy path: a parseable value
        # (hermetic_env's own "0.01") proceeds exactly as before
        p = self.tool("state-gate")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "STATE_CLEAN", v)


# ----------------------------------------------------------- seal-path (P1)

def expected_seal_species(main_top_real, tracker_filename, round_, home):
    """The independent reference derivation (SKILL.md-pinned, The
    attack + The tools): basename-hyphen-first-8-hex-sha256 of the
    MAIN checkout's REAL toplevel path, joined with the tracker's own
    filename and the round id — computed here from first principles,
    never by calling into the tool under test. `home` is the
    SUBPROCESS's own HOME (hermetic_env's `/nonexistent` sentinel,
    never this process's) — expanduser() here would resolve `~`
    against the wrong environment entirely."""
    import hashlib
    digest = hashlib.sha256(
        main_top_real.encode("utf-8", "surrogateescape")).hexdigest()[:8]
    key = f"{os.path.basename(main_top_real)}-{digest}"
    base = os.path.join(home, ".local/state/statiker/seals", key)
    stem = f"{tracker_filename}.{round_}"
    return key, {
        "seal": os.path.join(base, f"{stem}.seal"),
        "queue": os.path.join(base, f"{stem}.queue"),
        "paths": os.path.join(base, f"{stem}.paths"),
        "artifact": os.path.join(base, f"{stem}.artifact"),
        "report": os.path.join(base, f"{stem}.report"),
        "comparison": os.path.join(base, f"{stem}.comparison"),
    }


class TestSealPath(GitFixture):
    def test_paths_equal_the_pinned_derivation(self):
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        p = self.tool("seal-path", "--tracker", ".clippy/runs/t.md",
                      "--round", "A3")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "SEAL_PATH", p.stdout + p.stderr)
        main_top_real = os.path.realpath(str(self.repo))
        key, expected = expected_seal_species(main_top_real, "t.md", "A3",
                                              self.env["HOME"])
        self.assertEqual(v["repo_key"], key)
        for species, path in expected.items():
            self.assertEqual(v[species], path, species)

    def test_paths_from_a_linked_worktree_derive_in_main(self):
        # P1: --show-toplevel from INSIDE a linked worktree answers
        # with the worktree's own root — the pinned derivation must
        # use the MAIN checkout instead, via --git-common-dir
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        self.git("add", ".clippy/runs/t.md")
        self.git("commit", "-m", "tracker")
        sha = self.git("rev-parse", "HEAD").stdout.strip()
        wt = Path(self._tmp.name) / "wt1"
        wv = self.verdict(self.tool("worktree-add", "--sha", sha,
                                    "--path", str(wt)))
        self.assertEqual(wv["verdict"], "WORKTREE_ADDED")
        p = subprocess.run(
            [sys.executable, str(SCRIPT), "seal-path",
             "--tracker", ".clippy/runs/t.md", "--round", "A3"],
            cwd=wt, env=self.env, capture_output=True, text=True, timeout=60)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "SEAL_PATH", p.stdout + p.stderr)
        main_top_real = os.path.realpath(str(self.repo))
        key, expected = expected_seal_species(main_top_real, "t.md", "A3",
                                              self.env["HOME"])
        self.assertEqual(v["repo_key"], key,
                         "repo-key derived from the WORKTREE, not main")
        for species, path in expected.items():
            self.assertEqual(v[species], path, species)

    def test_bad_round_form_halts_usage_error(self):
        self.write(".clippy/runs/t.md", self.GATE_CLEAN_TRACKER)
        p = self.tool("seal-path", "--tracker", ".clippy/runs/t.md",
                      "--round", "3")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "USAGE_ERROR")
        self.assertEqual(p.returncode, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)

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
        lines = [l for l in p.stdout.splitlines() if l.startswith(VERDICT_PREFIX)]
        self.assertEqual(
            len(lines), 1,
            f"expected exactly one verdict line, stdout:\n{p.stdout}\nstderr:\n{p.stderr}",
        )
        return json.loads(lines[0][len(VERDICT_PREFIX):])

    def write(self, rel, content):
        p = self.repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return p

    def head_paths(self):
        out = self.git("show", "--name-only", "--format=", "HEAD").stdout
        return set(l for l in out.splitlines() if l)

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


# ---------------------------------------------------------------- lock check

class TestLockCheck(GitFixture):
    TRACKER = ".clippy/runs/t.md"

    def test_first_lock_clean_untracked_tracker(self):
        # porcelain ?? puts '?' in column one — attack-6 B3: a strict
        # col-1 read halts every first lock on its own fresh tracker.
        self.write(self.TRACKER, "# Run: t\n")
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
        self.write(self.TRACKER, "# Run: t\n")
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
        self.write(self.TRACKER, "# Run: t\n")
        v = self.verdict(self.tool(
            "lock-check", "--tracker", self.TRACKER, "--lock-set", "art.txt"))
        self.assertEqual(v["verdict"], "LOCK_CHECK_CLEAN")

    def test_staged_tracker_halts(self):
        self.write(self.TRACKER, "# Run: t\n")
        self.git("add", self.TRACKER)
        self.git("commit", "-m", "tracker")
        self.write(self.TRACKER, "# Run: t\nedit\n")
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
        self.write(self.TRACKER, "# Run: t\n")
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
        self.write(self.TRACKER, "# Run: t\n")
        v = self.verdict(self.tool(
            "lock-check", "--tracker", self.TRACKER, "--lock-set", "gen.txt"))
        self.assertEqual(v["verdict"], "LOCK_CHECK_CLEAN")

    def test_ignored_untracked_tracker_halts_unpinnable(self):
        self.write(".gitignore", ".clippy/\n")
        self.git("add", ".gitignore")
        self.git("commit", "-m", "gi")
        self.write(self.TRACKER, "# Run: t\n")
        p = self.tool("lock-check", "--tracker", self.TRACKER)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_TRACKER_UNPINNABLE")
        self.assertNotEqual(p.returncode, 0)

    def test_directory_path_halts(self):
        # attack-4 N6 probe: a directory pathspec sweeps operator
        # state under it into the commit.
        self.write("docs/a.txt", "a\n")
        self.write(self.TRACKER, "# Run: t\n")
        p = self.tool("lock-check", "--tracker", self.TRACKER, "--lock-set", "docs")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_DIRECTORY_PATH")
        self.assertIn("docs", v["paths"])

    def test_missing_lock_set_path_halts(self):
        # attack-6 B4 kin: an unpopulated path poisons the pathspec.
        self.write(self.TRACKER, "# Run: t\n")
        p = self.tool("lock-check", "--tracker", self.TRACKER,
                      "--lock-set", "never-made.txt")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_MISSING_PATH")
        self.assertIn("never-made.txt", v["paths"])

    def test_mid_merge_halts(self):
        self.start_conflicted_merge()
        self.write(self.TRACKER, "# Run: t\n")
        p = self.tool("lock-check", "--tracker", self.TRACKER)
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_STATE")
        self.assertIn("merge", v["ops"])


# --------------------------------------------------------------- lock commit

class TestLockCommit(GitFixture):
    TRACKER = ".clippy/runs/t.md"

    def test_clean_lock_commit_and_readback(self):
        self.write(self.TRACKER, "# Run: t\nStatus: [READY]\n")
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
        self.write(self.TRACKER, "# Run: t\n")
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
        self.write(self.TRACKER, "# Run: t\n")
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
        self.write(self.TRACKER, "# Run: t\n")
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
        self.write(self.TRACKER, "# Run: t\n")
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
        self.write(self.TRACKER, "# Run: t\n")
        p = self.tool("lock-commit", "--tracker", self.TRACKER,
                      "--lock-set", "art.txt", "-m", "lock")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_DROPS_UNACKNOWLEDGED")
        self.assertNotEqual(p.returncode, 0)
        # nothing was committed
        self.assertEqual(self.head_paths(), {"base.txt"})

    def test_stale_acknowledged_drop_halts(self):
        self.write(self.TRACKER, "# Run: t\n")
        p = self.tool("lock-commit", "--tracker", self.TRACKER,
                      "--lock-set", "art.txt", "--drop", "art.txt", "-m", "lock")
        v = self.verdict(p)
        self.assertIn(v["verdict"], ("HALT_DROPS_STALE", "HALT_MISSING_PATH"))
        self.assertEqual(self.head_paths(), {"base.txt"})


# --------------------------------------------------------------- unit start

class TestUnitStart(GitFixture):
    def test_clean_write_set(self):
        v = self.verdict(self.tool("unit-start", "--write-set", "src.txt"))
        self.assertEqual(v["verdict"], "UNIT_START_CLEAN")

    def test_untracked_operator_draft_collides(self):
        # attack-4 N7 probe: untracked operator draft on a write-set
        # path would be overwritten and committed by the unit.
        self.write("src.txt", "operator draft\n")
        p = self.tool("unit-start", "--write-set", "src.txt")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_COLLISION")
        self.assertTrue(any("src.txt" in e["path"] for e in v["entries"]))
        self.assertNotEqual(p.returncode, 0)

    def test_modified_tracked_path_collides(self):
        self.write("src.txt", "v1\n")
        self.git("add", "src.txt")
        self.git("commit", "-m", "src")
        self.write("src.txt", "operator edit\n")
        v = self.verdict(self.tool("unit-start", "--write-set", "src.txt"))
        self.assertEqual(v["verdict"], "UNIT_COLLISION")

    def test_dirt_outside_write_set_is_clean(self):
        # attack-5 B3 kin: the check is porcelain scoped to the
        # write-set; unrelated dirt must not spuriously halt the unit.
        self.write("other.txt", "operator wip\n")
        v = self.verdict(self.tool("unit-start", "--write-set", "src.txt"))
        self.assertEqual(v["verdict"], "UNIT_START_CLEAN")

    def test_mid_merge_halts_before_any_edit(self):
        self.start_conflicted_merge()
        v = self.verdict(self.tool("unit-start", "--write-set", "src.txt"))
        self.assertEqual(v["verdict"], "HALT_STATE")

    def test_directory_write_set_halts(self):
        self.write("docs/a.txt", "a\n")
        v = self.verdict(self.tool("unit-start", "--write-set", "docs"))
        self.assertEqual(v["verdict"], "HALT_DIRECTORY_PATH")


# -------------------------------------------------------------- unit commit

class TestUnitCommit(GitFixture):
    def test_green_commit(self):
        self.write("src.txt", "unit output\n")
        p = self.tool("unit-commit", "--write-set", "src.txt", "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_COMMITTED", p.stdout + p.stderr)
        self.assertEqual(self.head_paths(), {"src.txt"})
        self.assertEqual(v["sha"], self.git("rev-parse", "HEAD").stdout.strip())

    def test_operator_staged_state_outside_write_set_survives(self):
        self.write("op.txt", "operator\n")
        self.git("add", "op.txt")
        self.write("src.txt", "unit output\n")
        v = self.verdict(self.tool("unit-commit", "--write-set", "src.txt",
                                   "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED")
        self.assertEqual(self.head_paths(), {"src.txt"})
        status = self.git("status", "--porcelain", "--", "op.txt").stdout
        self.assertTrue(status.startswith("A "), status)

    def test_modified_tracked_path_commits_without_add(self):
        self.write("src.txt", "v1\n")
        self.git("add", "src.txt")
        self.git("commit", "-m", "v1")
        self.write("src.txt", "v2\n")
        v = self.verdict(self.tool("unit-commit", "--write-set", "src.txt",
                                   "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED")
        self.assertEqual(self.git("show", "HEAD:src.txt").stdout, "v2\n")

    def test_already_present_reads_head_not_worktree(self):
        # attack-6 B4: the discriminator must be a HEAD read. Content
        # identical to HEAD → NO_DIFF verdict, nothing committed.
        self.write("src.txt", "settled\n")
        self.git("add", "src.txt")
        self.git("commit", "-m", "settled")
        head = self.git("rev-parse", "HEAD").stdout.strip()
        self.write("src.txt", "settled\n")  # same content
        v = self.verdict(self.tool("unit-commit", "--write-set", "src.txt",
                                   "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_NO_DIFF_VS_HEAD")
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), head)

    def test_missing_write_set_path_halts_nothing_lands(self):
        # attack-6 B4 probe: an unpopulated write-set path poisons the
        # pathspec — exit 1, nothing lands, previously booked as landed.
        self.write("src.txt", "made\n")
        head = self.git("rev-parse", "HEAD").stdout.strip()
        p = self.tool("unit-commit", "--write-set", "src.txt",
                      "--write-set", "never-made.txt", "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_MISSING_PATH")
        self.assertIn("never-made.txt", v["paths"])
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), head)
        self.assertNotEqual(p.returncode, 0)

    def test_contention_blocked_after_capped_retries(self):
        # attack-5 N3: capped, spaced retries; persistent index.lock →
        # blocked-commit REPORT with the error text, never silence.
        self.write("src.txt", "unit output\n")
        lock = self.repo / ".git" / "index.lock"
        lock.write_text("")
        p = self.tool("unit-commit", "--write-set", "src.txt", "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "BLOCKED_CONTENTION")
        self.assertEqual(v["attempts"], 5)
        self.assertTrue(v["index_lock_present"])
        self.assertIn("index.lock", v["error"])
        self.assertNotEqual(p.returncode, 0)

    def test_contention_recovers_when_lock_clears(self):
        # probe (attack 4): contention is recoverable — a cleared lock
        # lets the same invocation land.
        self.write("src.txt", "unit output\n")
        v = self.verdict(self.tool("unit-commit", "--write-set", "src.txt",
                                   "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED")

    def test_state_gate_reread_distinct_from_contention(self):
        # attack-6 N3: an operation the operator began mid-unit blocks
        # the commit as HALT_STATE, never conflated with index.lock.
        self.write("src.txt", "unit output\n")
        self.start_conflicted_merge()
        p = self.tool("unit-commit", "--write-set", "src.txt", "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_STATE")
        self.assertIn("merge", v["ops"])


# ---------------------------------------------------- pure-function checks

class TestReviewFindings(GitFixture):
    """Repairs from the 0.2.32 fresh-context review (dev-notes,
    2026-08-07): each test written red against the pre-repair
    behavior the reviewer executed."""

    def test_multi_path_single_flag_parses(self):
        # review B1: the documented form `--write-set <file> ...`
        # errored with no verdict line at all
        p = self.tool("unit-start", "--write-set", "a.txt", "b.txt")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "UNIT_START_CLEAN")
        self.assertEqual(set(v["write_set"]), {"a.txt", "b.txt"})

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
        self.write(".clippy/runs/t.md", "# Run: t\n")
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
        self.write(".clippy/runs/t.md", "# Run: t\n")
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
        self.write("src.txt", "operator precious\n")
        self.git("add", "src.txt")
        self.write("src.txt", "unit output\n")
        p = self.tool("unit-commit", "--write-set", "src.txt",
                      "-m", "unit U1")
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
        self.write("src.txt", "OPERATOR PRECIOUS DRAFT\n")
        self.git("add", "src.txt")
        self.write("src.txt", "unit output\n")
        p = self.tool("unit-commit", "--write-set", "src.txt",
                      "-m", "unit U1")
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
        self.write(".clippy/runs/t.md", "# Run: t\n")
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
        self.write(".clippy/runs/t.md", "# Run: t\n")
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
        (self.repo / "build").mkdir()
        self.write("build/x.txt", "unit output\n")
        p = self.tool("unit-commit", "--write-set", "build/x.txt",
                      "-m", "unit U1")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "HALT_IGNORED_WRITESET")

    def test_unit_start_ignored_write_set_halts(self):
        # review N5: fires at both seams, was routed and tested nowhere
        self.write(".gitignore", "build/\n")
        self.git("add", ".gitignore")
        self.git("commit", "-m", "gi")
        p = self.tool("unit-start", "--write-set", "build/x.txt")
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
        self.write(".clippy/runs/t.md", "# Run: t\n")
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
        self.write(tracker, "# Run: t\nStatus: [READY]\n")
        v = self.verdict(self.tool(
            "lock-commit", "--tracker", tracker, "-m", "lock"))
        self.assertEqual(v["verdict"], "LOCK_COMMITTED",
                         f"false extras: {v.get('extras')}")

    def test_unit_commit_non_ascii_write_set_clean(self):
        # the parallel seam — the carry-across pin (one function, two
        # callers; both proven, not one)
        self.write("grünflächen.py", "x = 1\n")
        v = self.verdict(self.tool(
            "unit-commit", "--write-set", "grünflächen.py", "-m", "unit"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED",
                         f"false extras: {v.get('extras')}")

    def test_quote_worthy_ascii_specials_clean(self):
        # quotePath also fires on '"' and '\'; spaces never quote —
        # the attacker's trigger-set probes (P5), pinned as boundary
        self.write("my report.py", "x\n")
        v = self.verdict(self.tool(
            "unit-commit", "--write-set", "my report.py", "-m", "unit"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED")

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
        (self.repo / self.NAME).write_bytes(b"unit output\n")
        v = self.verdict(self.tool(
            "unit-commit", "--write-set", self.NAME, "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED",
                         f"false extras: {v.get('extras')}")
        self.assertEqual(v["write_set"], [self.NAME])

    def test_lock_drop_handshake_completes_non_utf8_byte_path(self):
        (self.repo / self.NAME).write_bytes(b"operator staged\n")
        self.git("add", self.NAME)
        self.write(self.TRACKER, "# Run: t\n")
        v1 = self.verdict(self.tool(
            "lock-check", "--tracker", self.TRACKER,
            "--lock-set", self.NAME))
        self.assertEqual(v1["verdict"], "LOCK_CHECK_DROPS")
        self.assertEqual([d["path"] for d in v1["drops"]], [self.NAME],
                         "porcelain spelling differs from the argv one")
        v2 = self.verdict(self.tool(
            "lock-commit", "--tracker", self.TRACKER,
            "--lock-set", self.NAME, "--drop", self.NAME, "-m", "lock"))
        self.assertEqual(v2["verdict"], "LOCK_COMMITTED",
                         "the drop handshake never matches")
        # the staged operator content survives untouched
        status = self.git("status", "--porcelain", "--", self.NAME).stdout
        self.assertTrue(status.startswith("A "), status)


class TestAttack9SymlinkContainment(GitFixture):
    """attack-9: rel() resolved paths through symlinks, so a booked
    verdict named a path the brief never wrote (the link's TARGET),
    and a tracked in-repo link pointing outward halted the unit
    outright. SKILL.md ('The tools'): a path is taken AS NAMED, never
    resolved through symlinks. Each test red against resolve()."""

    def test_unit_commit_books_the_named_path_not_the_link_target(self):
        self.write("realdir/target.py", "x = 1\n")
        os.symlink("realdir/target.py", self.repo / "alias.py")
        v = self.verdict(self.tool(
            "unit-commit", "--write-set", "alias.py", "-m", "unit U1"))
        self.assertEqual(v["verdict"], "UNIT_COMMITTED")
        self.assertEqual(v["write_set"], ["alias.py"],
                         "the booked write-set names the link target")
        # git commits the LINK, not the file it points at
        self.assertEqual(self.head_paths(), {"alias.py"})

    def test_unit_start_accepts_tracked_link_pointing_outward(self):
        ext = Path(self._tmp.name) / "ext"
        ext.mkdir()
        (ext / "real.py").write_text("x = 1\n")
        os.symlink("../ext/real.py", self.repo / "link.py")
        self.git("add", "link.py")
        self.git("commit", "-m", "link")
        v = self.verdict(self.tool("unit-start", "--write-set", "link.py"))
        self.assertEqual(v["verdict"], "UNIT_START_CLEAN")
        self.assertEqual(v["write_set"], ["link.py"])

    def test_repo_root_still_routes_as_a_directory_path(self):
        # the containment repair must not re-route the repo root out
        # of the directory check: '.' is a directory pathspec, which
        # sweeps whatever the operator touched under it
        v = self.verdict(self.tool("unit-start", "--write-set", "."))
        self.assertEqual(v["verdict"], "HALT_DIRECTORY_PATH")

    def test_literal_dotdot_escape_still_halts(self):
        # the containment rule the repair must not eat: a path naming
        # its way out of the repo is still outside it
        (Path(self._tmp.name) / "outside.py").write_text("x = 1\n")
        p = self.tool("unit-start", "--write-set", "../outside.py")
        v = self.verdict(p)
        self.assertEqual(v["verdict"], "PATH_OUTSIDE_REPO")
        self.assertNotEqual(p.returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

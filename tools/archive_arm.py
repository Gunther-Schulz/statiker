#!/usr/bin/env python3
"""Archive one arm's working copy before the between-arm reset.

Pre-registration §9 puts an irreversible act immediately after a copy:
the reset discards exactly what the run produced, because statiker's
record IS the commit log. So the copy is the ONLY original from the
moment the reset runs, and a copy that silently dropped something looks
identical to a complete one — `cp -r` reports success either way.

This verifies the copy and REFUSES to report OK otherwise. It never
resets: the destructive step stays a separate deliberate act, taken with
this verdict already on screen, so a failed verification cannot be
followed by reflex.

Run:  python3 tools/archive_arm.py <arm-name> [--src DIR] [--dest DIR]
      python3 tools/archive_arm.py --selftest
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

SRC = "/home/g/dev/local/statiker-run-2026-09-13-lc61"
DEST_ROOT = "/home/g/dev/local/statiker-run-2026-09-13-lc61-arms"


def walk_digest(root):
    """(file count, digest over every path AND its bytes).

    Paths are included, not just contents: two trees can hold identical
    bytes under different names, and a rename is a lost record too.
    `.git` is walked like everything else — it holds the run's record,
    which is the whole point of archiving.
    """
    h = hashlib.sha256()
    count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in sorted(filenames):
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root)
            h.update(rel.encode("utf-8", "surrogateescape"))
            h.update(b"\0")
            if os.path.islink(full):
                h.update(b"L")
                h.update(os.readlink(full).encode("utf-8", "surrogateescape"))
            else:
                try:
                    with open(full, "rb") as fh:
                        while True:
                            chunk = fh.read(1 << 20)
                            if not chunk:
                                break
                            h.update(chunk)
                except OSError as exc:
                    h.update(f"UNREADABLE:{exc}".encode())
            count += 1
    return count, h.hexdigest()


def git_log(root):
    """The commit log, read from the tree itself.

    An independent second measurement of the same quantity: the digest
    could match while the repository is unusable, and this could match
    while worktree files are missing. They vary different axes.
    """
    try:
        out = subprocess.run(
            ["git", "-C", root, "log", "--format=%H %s"],
            capture_output=True, text=True)
        return out.stdout.strip() if out.returncode == 0 else f"ERR:{out.returncode}"
    except OSError as exc:
        return f"ERR:{exc}"


def archive(arm, src=SRC, dest_root=DEST_ROOT):
    dest = os.path.join(dest_root, arm)
    if os.path.exists(dest):
        return {"verdict": "REFUSED_DEST_EXISTS", "dest": dest,
                "note": "an existing archive is never overwritten — "
                        "that would destroy a previous arm's only record"}
    if not os.path.isdir(src):
        return {"verdict": "REFUSED_NO_SOURCE", "src": src}

    src_count, src_digest = walk_digest(src)
    src_log = git_log(src)

    os.makedirs(dest_root, exist_ok=True)
    shutil.copytree(src, dest, symlinks=True)

    dst_count, dst_digest = walk_digest(dest)
    dst_log = git_log(dest)

    ok = (src_count == dst_count and src_digest == dst_digest
          and src_log == dst_log and src_count > 0)

    return {
        "verdict": "ARCHIVED_VERIFIED" if ok else "ARCHIVE_UNVERIFIED",
        "src": src, "dest": dest,
        "files": f"{src_count} -> {dst_count}",
        "digest_match": src_digest == dst_digest,
        "log_match": src_log == dst_log,
        "commits": len([x for x in src_log.splitlines() if x]),
    }


def render(r):
    print(f"{r['verdict']}")
    for k, v in r.items():
        if k != "verdict":
            print(f"    {k}: {v}")
    if r["verdict"] == "ARCHIVED_VERIFIED":
        print("\n    Safe to reset. The reset is NOT run by this tool:")
        print(f"    git -C {r['src']} reset --hard e06be63 && "
              f"git -C {r['src']} clean -xfdq")
    else:
        print("\n    DO NOT RESET. The original is still the only "
              "complete copy.")


def selftest():
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "src")
        os.makedirs(os.path.join(src, "sub"))
        with open(os.path.join(src, "a.txt"), "w") as fh:
            fh.write("alpha")
        with open(os.path.join(src, "sub", "b.txt"), "w") as fh:
            fh.write("beta")

        # 1. Honest copy verifies.
        r = archive("arm1", src=src, dest_root=os.path.join(tmp, "arch"))
        assert r["verdict"] == "ARCHIVED_VERIFIED", r

        # 2. RED-FIRST, the branch that matters: a copy missing one file
        #    must NOT verify. Simulated by deleting from the archive after
        #    the fact and re-measuring, which is exactly the state a
        #    partial copy leaves behind.
        dest = r["dest"]
        os.remove(os.path.join(dest, "sub", "b.txt"))
        c_src, d_src = walk_digest(src)
        c_dst, d_dst = walk_digest(dest)
        assert c_src != c_dst and d_src != d_dst, "loss went undetected"

        # 3. A rename with identical bytes is also a loss, and a
        #    content-only digest would call it clean.
        dest2 = os.path.join(tmp, "arch2", "arm2")
        os.makedirs(os.path.dirname(dest2))
        shutil.copytree(src, dest2, symlinks=True)
        os.rename(os.path.join(dest2, "a.txt"),
                  os.path.join(dest2, "renamed.txt"))
        assert walk_digest(src)[1] != walk_digest(dest2)[1], \
            "rename went undetected"

        # 4. Never overwrite an existing archive.
        r2 = archive("arm1", src=src, dest_root=os.path.join(tmp, "arch"))
        assert r2["verdict"] == "REFUSED_DEST_EXISTS", r2

    print("SELFTEST PASSED: honest copy verifies; a dropped file and a "
          "pure rename both go red; an existing archive is refused.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "--selftest":
        selftest()
        sys.exit(0)
    result = archive(args[0])
    render(result)
    sys.exit(0 if result["verdict"] == "ARCHIVED_VERIFIED" else 1)

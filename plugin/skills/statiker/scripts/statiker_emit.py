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

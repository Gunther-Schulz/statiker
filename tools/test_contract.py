#!/usr/bin/env python3
"""Contract parity between the tools and SKILL.md — the check the
0.2.32 reviewer and attack 7 both ran by hand, mechanized (attack-7
trend: every 0.2.35 repair landed at its finding site and was not
carried to the sibling; three blockers were carry-across failures).

Two directions, both set-exact:
- every verdict either script can emit appears literally in SKILL.md
  (named at its route or inside a catch-all's parenthetical);
- every verdict-shaped token SKILL.md names is one a script emits.

Verdict morphology: ALL-CAPS with at least one underscore — the tag
enums use hyphens ([ZERO-DELTA], [AUTO-ACCEPTED]) so the two
namespaces cannot collide.

Run: python3 tools/test_contract.py
"""

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL = REPO_ROOT / "plugin" / "skills" / "statiker" / "SKILL.md"
SCRIPTS = [
    REPO_ROOT / "plugin" / "skills" / "statiker" / "scripts" / "statiker_git.py",
    REPO_ROOT / "plugin" / "skills" / "statiker" / "scripts" / "statiker_record.py",
]

VERDICT_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b")
EMIT_RE = re.compile(r'[\'"]([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)[\'"]')

# verdict-morphology string literals in the scripts that are NOT
# verdicts (git refs, env vars) — a new entry here needs the same
# scrutiny as a route
NON_VERDICTS = {
    "MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "REBASE_HEAD",
    "STATIKER_GIT_RETRY_BASE",
}


def emitted_verdicts():
    out = set()
    for script in SCRIPTS:
        out |= set(EMIT_RE.findall(script.read_text(encoding="utf-8")))
    return out - NON_VERDICTS


def skill_named_verdicts():
    return set(VERDICT_TOKEN_RE.findall(SKILL.read_text(encoding="utf-8")))


class TestVerdictParity(unittest.TestCase):
    def test_every_emitted_verdict_is_routed_in_skill(self):
        missing = emitted_verdicts() - skill_named_verdicts()
        self.assertEqual(
            missing, set(),
            f"emitted by a script, named nowhere in SKILL.md: "
            f"{sorted(missing)} — route it or add it to a catch-all's "
            f"parenthetical")

    def test_every_skill_named_verdict_is_emitted(self):
        phantom = skill_named_verdicts() - emitted_verdicts()
        self.assertEqual(
            phantom, set(),
            f"named in SKILL.md, emitted by no script: {sorted(phantom)}")

    def test_extractor_is_live(self):
        # instrument check: both extractors match known positives
        self.assertIn("LOCK_COMMITTED", emitted_verdicts())
        self.assertIn("USAGE_ERROR", emitted_verdicts())
        self.assertIn("HALT_STATE", skill_named_verdicts())


if __name__ == "__main__":
    unittest.main(verbosity=1)

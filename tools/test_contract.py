#!/usr/bin/env python3
"""Contract parity between the tools and SKILL.md — the check the
0.2.32 reviewer and attack 7 both ran by hand, mechanized.

Reach, stated honestly (attack-8 N4 corrected the 0.2.36 booking):
this instrument mechanizes VERDICT-NAME parity plus emit-position
discipline — it does not cover behavioral carry-across (a repair
landing at one seam and not its sibling); that class's mechanism is
the per-repair parallel-site test pair in the suites, plus the attack
rounds themselves.

Two directions, both set-exact:
- every verdict either script can emit appears literally in SKILL.md
  (named at its route or inside a catch-all's parenthetical);
- every verdict-shaped token SKILL.md names is one a script emits.

Emitted verdicts are extracted from the AST at their EMIT POSITIONS
(finish()/Halt() first args, the retry helper's verdict arg, and
*_verdict factory returns), not grepped from the whole file — the
attack-8 probes showed the grep form blind to a no-underscore name
(V3), an f-string-assembled name (V4b), and silenceable via its own
NON_VERDICTS list (V6). Emit-position extraction needs no such list,
and a non-literal or morphology-breaking name at an emit position is
itself a failure.

Run: python3 tools/test_contract.py
"""

import ast
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
MORPHOLOGY = re.compile(r"[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\Z")

# emit positions: callable name -> index of the verdict argument
EMIT_ARG_INDEX = {"finish": 0, "Halt": 0, "_index_write_with_retry": 1}
# sanctioned indirections: variables/attributes that CARRY a verdict
# from another checked emit position (their sources are the retry
# helper's literal args and the *_verdict factory returns below)
EMIT_CONDUITS = {"failure_verdict", "name", "verdict"}


def _call_name(node):
    fn = node.func
    if isinstance(fn, ast.Name):
        return fn.id
    if isinstance(fn, ast.Attribute):
        return fn.attr
    return None


def emit_position_verdicts(source_text):
    """(literals, offenders) for one script's source. An offender is
    any emit-position argument that is neither a morphology-passing
    string literal nor a declared conduit."""
    literals, offenders = set(), []
    tree = ast.parse(source_text)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = _call_name(node)
            if name not in EMIT_ARG_INDEX:
                continue
            idx = EMIT_ARG_INDEX[name]
            if len(node.args) <= idx:
                continue
            a = node.args[idx]
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                if MORPHOLOGY.match(a.value):
                    literals.add(a.value)
                else:
                    offenders.append((node.lineno, repr(a.value)))
            elif isinstance(a, ast.Name) and a.id in EMIT_CONDUITS:
                pass
            elif isinstance(a, ast.Attribute) and a.attr in EMIT_CONDUITS:
                pass
            else:
                offenders.append((node.lineno, ast.dump(a)[:80]))
        elif isinstance(node, ast.FunctionDef) and \
                node.name.endswith("_verdict"):
            for ret in ast.walk(node):
                if isinstance(ret, ast.Return) and \
                        isinstance(ret.value, ast.Tuple) and ret.value.elts:
                    e0 = ret.value.elts[0]
                    if isinstance(e0, ast.Constant) and \
                            isinstance(e0.value, str) and \
                            MORPHOLOGY.match(e0.value):
                        literals.add(e0.value)
                    else:
                        offenders.append((ret.lineno,
                                          "verdict factory returns "
                                          "non-literal name"))
    return literals, offenders


def emitted_verdicts():
    out = set()
    for script in SCRIPTS:
        lits, _ = emit_position_verdicts(
            script.read_text(encoding="utf-8"))
        out |= lits
    return out


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

    def test_emit_positions_are_literal_verdicts(self):
        # attack-8 V3/V4b: a name assembled at emit time, or one
        # breaking verdict morphology, is invisible to name parity —
        # so the emit positions themselves are the checked surface
        for script in SCRIPTS:
            _, offenders = emit_position_verdicts(
                script.read_text(encoding="utf-8"))
            self.assertEqual(
                offenders, [],
                f"{script.name}: emit-position args that are not "
                f"morphology-passing literals or declared conduits")

    def test_extractor_is_live(self):
        # instrument check: the extractor matches known positives from
        # every source kind — direct finish, Halt raise, retry-helper
        # arg, and factory return
        got = emitted_verdicts()
        for known in ("USAGE_ERROR", "GIT_ERROR", "ADD_FAILED",
                      "LOCK_COMMITTED_EXTRAS", "CLOSURE_RECORD_MALFORMED"):
            self.assertIn(known, got)
        self.assertIn("HALT_STATE", skill_named_verdicts())


if __name__ == "__main__":
    unittest.main(verbosity=1)

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
(finish()/Halt() args — positional OR keyword — the retry helper's
verdict arg, tuple-returning factory functions, and conduit-variable
assignments), not grepped from the whole file. Provenance: attack-8
showed the grep form blind to no-underscore names (V3), assembled
names (V4b), and its own NON_VERDICTS silencing lane (V6); attack-9
drove the first AST form past with keyword-arg emits (V7),
conduit-named locals (V8), and non-`_verdict` factories (V10b) — all
three closed here by construction (keyword args are read, conduit
assignments feed the emitted set or flag as offenders, ALL
tuple-returning functions are scanned).

Honest reach (attack-9 N1): a hand-rolled emit that rebuilds the
verdict line without finish/Halt (V9) is invisible to any call-site
analysis; the durable layer for that class is the runtime battery
(drive each subcommand's error paths, grep the ACTUAL emitted verdict
lines) — commissioned as a dispatch unit, and until it lands this
file must not be cited as covering the V9 shape.

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


# keyword names under which the verdict may travel at each emit call
EMIT_KWARGS = {"finish": "verdict", "Halt": "verdict",
               "_index_write_with_retry": "failure_verdict"}


def _classify_emit_arg(a, literals, offenders, lineno):
    if isinstance(a, ast.Constant) and isinstance(a.value, str):
        if MORPHOLOGY.match(a.value):
            literals.add(a.value)
        else:
            offenders.append((lineno, repr(a.value)))
    elif isinstance(a, ast.Name) and a.id in EMIT_CONDUITS:
        pass
    elif isinstance(a, ast.Attribute) and a.attr in EMIT_CONDUITS:
        pass
    else:
        offenders.append((lineno, ast.dump(a)[:80]))


def emit_position_verdicts(source_text):
    """(literals, offenders) for one script's source. An offender is
    any emit-position argument — positional or keyword — that is
    neither a morphology-passing string literal nor a declared
    conduit, and any conduit assignment from a non-literal."""
    literals, offenders = set(), []
    tree = ast.parse(source_text)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = _call_name(node)
            if name not in EMIT_ARG_INDEX:
                continue
            idx = EMIT_ARG_INDEX[name]
            if len(node.args) > idx:
                _classify_emit_arg(node.args[idx], literals, offenders,
                                   node.lineno)
                continue
            # keyword form (attack-9 V7: `continue` here was a silent
            # skip — a keyword emit went unchecked entirely)
            kw = next((k for k in node.keywords
                       if k.arg == EMIT_KWARGS[name]), None)
            if kw is not None:
                _classify_emit_arg(kw.value, literals, offenders,
                                   node.lineno)
            else:
                offenders.append(
                    (node.lineno,
                     f"{name}() carries its verdict neither "
                     f"positionally nor as {EMIT_KWARGS[name]}="))
        elif isinstance(node, ast.Assign):
            # a conduit assigned anywhere feeds the emitted set — or
            # flags (attack-9 V8: a local named `verdict` was waved
            # through with no check on what it carried)
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in EMIT_CONDUITS:
                    v = node.value
                    if isinstance(v, ast.Constant) and \
                            isinstance(v.value, str) and \
                            MORPHOLOGY.match(v.value):
                        literals.add(v.value)
                    else:
                        # the factory idiom is a TUPLE unpack (`name,
                        # detail = ..._verdict(...)`), which never has
                        # a bare-Name target — so a single conduit
                        # Name assigned from anything non-literal is
                        # an offender, calls included
                        offenders.append(
                            (node.lineno,
                             f"conduit {tgt.id} assigned from "
                             f"{ast.dump(v)[:60]}"))
        elif isinstance(node, ast.FunctionDef):
            # EVERY tuple-returning function is scanned (attack-9
            # V10b: a factory not named *_verdict was invisible)
            for ret in ast.walk(node):
                if isinstance(ret, ast.Return) and \
                        isinstance(ret.value, ast.Tuple) and ret.value.elts:
                    e0 = ret.value.elts[0]
                    if isinstance(e0, ast.Constant) and \
                            isinstance(e0.value, str) and \
                            MORPHOLOGY.match(e0.value):
                        literals.add(e0.value)
                    elif node.name.endswith("_verdict"):
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

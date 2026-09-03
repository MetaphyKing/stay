#!/usr/bin/env python3
"""9.11 CDI sits on System, Quantity, Ticket, Claim the way it sits on Name.

Overloaded strings stay a lattice. Quantities stay kinded. Tickets do not
collapse names. Skill stays uninstalled.
"""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import read_ledger, resolve, use
from stay.tests._fixture import fixture_root

SKILL_INSTALLED = Path("/home/box/agent-data/workflows/claim-datum-interlock/SKILL.md")
SKILL_DIR = Path("/workspace/praxis/novelty-notebook-20260902/skills/claim-datum-interlock")


def main():
    root = fixture_root()
    name_stay = use("Name", "Stay", root=root, spoken="Stay")
    system_stay = use("System", "Stay", root=root, spoken="Stay")
    claim_stay = use("Claim", "Stay", root=root, spoken="Stay")
    assert len({name_stay, system_stay, claim_stay}) == 3

    q_len = use(
        "Quantity",
        "Meter",
        suffix="m-len0",
        root=root,
        kind="length",
        spoken="meter",
    )
    q_opt = use(
        "Quantity",
        "Meter",
        suffix="m-opt0",
        root=root,
        kind="optical",
        spoken="meter",
    )
    assert q_len != q_opt
    kinds = {row.get("kind") for row in read_ledger(root) if row.get("genus") == "Quantity"}
    assert kinds == {"length", "optical"}

    j1 = use("Name", "Jessica", suffix="j-a3f0", root=root, spoken="Jessica")
    j2 = use("Name", "Jessica", suffix="j-b7e1", root=root, spoken="Jessica")
    ticket = use("Ticket", "Add", suffix="t-add1", root=root)
    assert j1 != j2
    assert ticket.startswith("Ticket/")
    assert resolve("Name", "Jessica", suffix="j-a3f0", root=root) == j1
    assert resolve("Name", "Jessica", suffix="j-b7e1", root=root) == j2
    assert j1 in [row["id"] for row in read_ledger(root)]
    assert j2 in [row["id"] for row in read_ledger(root)]

    assert not SKILL_INSTALLED.exists()
    assert SKILL_DIR.is_dir()
    print("CDI_SIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

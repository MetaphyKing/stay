#!/usr/bin/env python3
"""9.5 first USE appends. Second USE same genus+lemma returns same id."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import read_ledger, use
from stay.tests._fixture import fixture_root


def main():
    root = fixture_root()
    first = use("Name", "Logan", root=root)
    n1 = len(read_ledger(root))
    second = use("Name", "Logan", root=root)
    n2 = len(read_ledger(root))
    assert first == second, (first, second)
    assert first.count("/") == 2
    assert n1 == 1 and n2 == 1
    other = use("Place", "Logan", root=root)
    assert other != first
    print("MINT_RESOLVE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

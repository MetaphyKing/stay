#!/usr/bin/env python3
"""10.2 two Name/Jessica ids. Same swatch allowed. Unify-by-color fails."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import inject_card, use
from stay.tests._fixture import fixture_root


def main():
    root = fixture_root()
    a = use("Name", "Jessica", root=root, suffix="j-a3f0")
    b = use("Name", "Jessica", root=root, suffix="j-b7c1")
    assert a != b, (a, b)
    assert a == "Name/Jessica/j-a3f0"
    assert b == "Name/Jessica/j-b7c1"
    card_a = inject_card(a, root=root)
    card_b = inject_card(b, root=root)
    assert "slate" in card_a and "slate" in card_b
    assert a in card_a and b in card_b
    # Unify-by-color would collapse two ids that share a swatch.
    same_paint = "slate" in card_a and "slate" in card_b
    assert same_paint and a != b
    print("TWO_JESSICA_OK")
    return 0


class TwoJessicaTest(unittest.TestCase):
    def test_two_jessica(self):
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    raise SystemExit(main())

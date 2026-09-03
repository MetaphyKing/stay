#!/usr/bin/env python3
"""10.1 retired suffix cannot remint. Live lemma remint returns same id."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import StayClosed, mint, supersede, use
from stay.tests._fixture import fixture_root


def main():
    root = fixture_root()
    live = use("Name", "Jessica", root=root, suffix="j-a3f0")
    again = use("Name", "Jessica", root=root)
    assert again == live, (again, live)
    supersede(live, root=root)
    try:
        mint("Name", "Jessica", root=root, suffix="j-a3f0")
        raise AssertionError("retired suffix reminted")
    except StayClosed as exc:
        assert "recycle" in str(exc).lower()
    fresh = use("Name", "Jessica", root=root)
    assert fresh != live
    assert fresh.count("/") == 2
    print("NEVER_RECYCLE_OK")
    return 0


class NeverRecycleTest(unittest.TestCase):
    def test_never_recycle(self):
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    raise SystemExit(main())

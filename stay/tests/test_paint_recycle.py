#!/usr/bin/env python3
"""9.3 after hot window, swatch returns to pool. Ledger row stays."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import (
    POOL,
    assign_window_paint,
    expire_window,
    ledger_has,
    pool_available,
    read_ledger,
    use,
)
from stay.tests._fixture import fixture_root


def main():
    root = fixture_root()
    sid = use("Name", "PaintProbe", root=root)
    before = [row["id"] for row in read_ledger(root)]
    paint = assign_window_paint(sid, root=root)
    assert paint in POOL, paint
    assert paint not in pool_available(root)
    returned = expire_window(root)
    assert paint in returned
    assert paint in pool_available(root)
    after = [row["id"] for row in read_ledger(root)]
    assert after == before
    assert ledger_has(sid, root=root)
    print("PAINT_RECYCLE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

#!/usr/bin/env python3
"""9.6 backticks, fences, quotes mint zero rows."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import handle, read_ledger
from stay.tests._fixture import fixture_root


def main():
    root = fixture_root()
    n0 = len(read_ledger(root))
    samples = [
        ("identity", "`Jessica`"),
        ("memory-write", "```\nJessica\n```"),
        ("promote", '"Jessica"'),
        ("i2", "'Jessica'"),
        ("extract-ingest", "see `Jessica` only"),
    ]
    for event, text in samples:
        out = handle(event, text, genus="Name", lemma="Jessica", root=root)
        assert out is None, (event, text, out)
    assert len(read_ledger(root)) == n0
    print("MENTIONS_NO_MINT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

#!/usr/bin/env python3
"""10.3 strip ANSI/hex. Id and swatch name still present."""

import re
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import inject_card, use
from stay.tests._fixture import fixture_root


def main():
    root = fixture_root()
    sid = use("Name", "Jessica", root=root, suffix="j-a3f0")
    card = inject_card(sid, root=root, gloss="Jessica")
    painted = f"\x1b[38;2;74;85;104m{card}\x1b[0m hex #4A5568"
    stripped = re.sub(r"\x1b\[[0-9;]*m", "", painted)
    stripped = re.sub(r"#[0-9A-Fa-f]{3,8}\b", "", stripped)
    assert sid in stripped, stripped
    assert "slate" in stripped, stripped
    assert "\x1b" not in stripped
    print("PLAINTEXT_CARD_OK")
    return 0


class PlaintextCardTest(unittest.TestCase):
    def test_plaintext_card(self):
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    raise SystemExit(main())

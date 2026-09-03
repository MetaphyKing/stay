#!/usr/bin/env python3
"""9.2 inject card not volume."""

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
    assert sid in card, card
    assert "slate" in card, card
    assert "SKILL.md" not in card
    vol = (root / "volumes" / "Name.md").read_bytes()
    inject_bytes = card.encode("utf-8")
    assert len(inject_bytes) < len(vol), (len(inject_bytes), len(vol), card)
    lines = [ln for ln in card.strip().splitlines() if ln.strip()]
    assert len(lines) >= 2
    print("INJECT_CARD_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

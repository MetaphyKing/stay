#!/usr/bin/env python3
"""9.4 hook fires on claim-commit only. Speech-only does not mint."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import HOOK_EVENTS, handle, read_ledger
from stay.tests._fixture import fixture_root


def main():
    root = fixture_root()
    n0 = len(read_ledger(root))
    for event in ("speech", "chat", "talk", "token"):
        out = handle(event, "Jessica walked in", genus="Name", lemma="Jessica", root=root)
        assert out is None
    assert len(read_ledger(root)) == n0
    cards = []
    for event in HOOK_EVENTS:
        card = handle(
            event,
            f"USE {event}",
            genus="Name",
            lemma=event.replace("-", "").title(),
            root=root,
        )
        assert card and "id:" in card and "swatch:" in card
        cards.append(card)
    assert len(read_ledger(root)) == n0 + len(HOOK_EVENTS)
    assert set(HOOK_EVENTS) == {
        "memory-write",
        "extract-ingest",
        "promote",
        "identity",
        "i2",
    }
    print("HOOK_EVENTS_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

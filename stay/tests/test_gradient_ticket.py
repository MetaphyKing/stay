#!/usr/bin/env python3
"""9.12 gradient only if stay/tickets/<id>.json exists, named and reversible."""

import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import StayClosed
from stay.ingest import gradient
from stay.tests._fixture import fixture_root


def main():
    root = fixture_root()
    data = gradient("t-map-amber-violet", root=root)
    assert data.get("named") is True or data.get("name")
    assert data.get("reversible") is True
    try:
        gradient("no-such-ticket", root=root)
        raise AssertionError("missing ticket must fail closed")
    except StayClosed:
        pass
    bad = root / "tickets" / "t-one-way.json"
    bad.write_text(
        json.dumps({"id": "t-one-way", "name": "one-way", "named": True, "reversible": False}),
        encoding="utf-8",
    )
    try:
        gradient("t-one-way", root=root)
        raise AssertionError("irreversible ticket must fail closed")
    except StayClosed:
        pass
    print("GRADIENT_TICKET_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

#!/usr/bin/env python3
"""11.2 no SSN, patient, chart ids, Boops in volumes/ledger/cards/tickets."""

from pathlib import Path
import re
import sys
import unittest

STAY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(STAY.parent))

NEEDLES = (
    (r"\bBoops\b", "Boops"),
    (r"\bSSN\b", "SSN"),
    (r"\bpatient\b", "patient"),
    (r"Res#", "Res#"),
    (r"\bchart ids\b", "chart ids"),
)

SKIP_SUFFIX = {".pyc"}


def scan():
    hits = []
    roots = [
        STAY / "volumes",
        STAY / "ids",
        STAY / "cards",
        STAY / "tickets",
    ]
    files = []
    for root in roots:
        if root.is_file():
            files.append(root)
        elif root.is_dir():
            files.extend(p for p in root.rglob("*") if p.is_file())
    for path in files:
        if path.suffix in SKIP_SUFFIX:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pat, name in NEEDLES:
            if re.search(pat, text, re.I):
                hits.append(f"{path}: {name}")
    return hits


def main():
    hits = scan()
    assert not hits, hits
    print("PUI_CLOSED_OK")
    return 0


class PuiClosedTest(unittest.TestCase):
    def test_pui_closed(self):
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    raise SystemExit(main())

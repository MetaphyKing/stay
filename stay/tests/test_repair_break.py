#!/usr/bin/env python3
"""Repair after Break FAIL. B1/B2/B4/B6 must fail-closed. Fake PUI only."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import StayClosed, handle, inject_card, read_ledger, use
from stay.ingest import extract, ingest
from stay.tests._fixture import fixture_root

FAKE_SSN = "000-00-0000"


def main():
    root = fixture_root()

    # B4/A2: ingest must not copy SSN-shaped text onto card gloss.
    closed = False
    try:
        ingest(f"SSN {FAKE_SSN} for FakePat", "chat", "Name", "FakePat", root=root)
    except StayClosed as exc:
        closed = True
        assert "PUI" in str(exc)
    assert closed
    for row in read_ledger(root):
        blob = str(row)
        assert FAKE_SSN not in blob
        assert "SSN" not in blob
    if (root / "ids" / "ledger.jsonl").is_file():
        ledger = (root / "ids" / "ledger.jsonl").read_text(encoding="utf-8")
        assert FAKE_SSN not in ledger

    # B1/A6: empty lemma must not mint Name//x-....
    closed = False
    try:
        use("Name", "", root=root)
    except StayClosed as exc:
        closed = True
        assert "empty lemma" in str(exc)
    assert closed
    for row in read_ledger(root):
        assert row.get("lemma"), row
        parts = (row.get("id") or "").split("/")
        assert len(parts) == 3 and all(parts), row

    # B2/A3d: memory-write of ordinary speech must not mint.
    n0 = len(read_ledger(root))
    out = handle(
        "memory-write",
        text="hello there",
        genus="Name",
        lemma="SpeechLeak",
        root=root,
    )
    assert out is None
    assert len(read_ledger(root)) == n0
    ids = [row.get("id") for row in read_ledger(root)]
    assert not any("SpeechLeak" in (sid or "") for sid in ids)

    # Claim-commit still mints (held path).
    card = handle(
        "memory-write",
        text="USE SpeechOk",
        genus="Name",
        lemma="SpeechOk",
        root=root,
    )
    assert card and "Name/SpeechOk/" in card

    # B6/A7: raw %PDF-1.4 must not mint as a claim.
    claims = extract(b"%PDF-1.4\nJessica neighbor\n\x00\xff", "pdf")
    joined = " ".join(c["text"] for c in claims)
    assert "%PDF-1.4" not in joined
    assert "Jessica neighbor" in joined

    # Held: mention-spoof still does not mint.
    n1 = len(read_ledger(root))
    assert handle("identity", "`Jessica`", genus="Name", lemma="Jessica", root=root) is None
    assert len(read_ledger(root)) == n1

    print("REPAIR_BREAK_OK")
    return 0


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    raise SystemExit(main())

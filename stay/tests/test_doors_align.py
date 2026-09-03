#!/usr/bin/env python3
"""Beta leftover: handle and ingest share claim-commit fail-closed."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import StayClosed, handle, read_ledger
from stay.ingest import extract, ingest
from stay.tests._fixture import fixture_root

LATTICE = "Overloaded names stay a lattice. Tokens with two expansions do not collapse."
CLAIM = "SPTS is Single Prime Trinary System."
FAKE = "000-00-0000"


def _ids(root):
    return [row.get("id") for row in read_ledger(root)]


def main():
    root = fixture_root()
    n0 = len(read_ledger(root))

    # Speech: handle None, ingest StayClosed, neither mints.
    out = handle("extract-ingest", LATTICE, genus="Claim", lemma="OverloadedLattice", root=root)
    assert out is None
    closed = False
    try:
        ingest(LATTICE, "chat", "Claim", "OverloadedLattice", root=root)
    except StayClosed as exc:
        closed = True
        assert "claim-commit" in str(exc)
    assert closed
    assert len(read_ledger(root)) == n0

    hello = handle("extract-ingest", "hello there", genus="Name", lemma="SpeechLeak", root=root)
    assert hello is None
    try:
        ingest("hello there", "chat", "Name", "SpeechLeak", root=root)
        raise AssertionError("ingest minted speech")
    except StayClosed:
        pass
    assert not any("SpeechLeak" in (sid or "") for sid in _ids(root))

    # Mention: neither mints.
    assert handle("extract-ingest", "see `Stay` only", genus="Artifact", lemma="Stay", root=root) is None
    try:
        ingest("see `Stay` only", "chat", "Artifact", "Stay", root=root)
        raise AssertionError("ingest minted mention")
    except StayClosed:
        pass

    # PUI: both StayClosed. Fake shape only.
    pui = f"id {FAKE} is FakePat"
    try:
        handle("memory-write", pui, genus="Name", lemma="FakePat", root=root)
        raise AssertionError("handle missed PUI")
    except StayClosed as exc:
        assert "PUI" in str(exc)
    try:
        ingest(pui, "chat", "Name", "FakePat", root=root)
        raise AssertionError("ingest missed PUI")
    except StayClosed as exc:
        assert "PUI" in str(exc)

    # Empty lemma: both StayClosed.
    try:
        handle("memory-write", "USE Empty", genus="Name", lemma="", root=root)
        raise AssertionError("handle empty lemma")
    except StayClosed as exc:
        assert "empty lemma" in str(exc)
    try:
        ingest("USE Empty", "chat", "Name", "", root=root)
        raise AssertionError("ingest empty lemma")
    except StayClosed as exc:
        assert "empty lemma" in str(exc)

    # PDF magic is not a claim. Extract drops header. Speech leftover does not mint.
    claims = extract(b"%PDF-1.4\nJessica neighbor\n\x00\xff", "pdf")
    joined = " ".join(c["text"] for c in claims)
    assert "%PDF-1.4" not in joined
    try:
        ingest(b"%PDF-1.4\nJessica neighbor\n\x00\xff", "pdf", "Name", "Jessica", root=root)
        raise AssertionError("ingest minted PDF leftover speech")
    except StayClosed:
        pass
    try:
        handle("extract-ingest", "%PDF-1.4 USE PdfLeak", genus="Claim", lemma="PdfLeak", root=root)
        raise AssertionError("handle missed PDF magic")
    except StayClosed as exc:
        assert "raw" in str(exc).lower()

    # Held claim-commit: both mint.
    card = handle("extract-ingest", "USE Artifact Stay", genus="Artifact", lemma="Stay", root=root)
    assert card and "Artifact/Stay/" in card
    result = ingest(CLAIM, "chat", "System", "SPTS-SinglePrime", root=root, spoken="SPTS")
    assert result["id"].startswith("System/SPTS-SinglePrime/")
    assert "is Single Prime" in result["card"]

    print("DOORS_ALIGN_OK")
    return 0


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    raise SystemExit(main())

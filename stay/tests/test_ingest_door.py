#!/usr/bin/env python3
"""9.10 one door: extract claims, then mint. Raw bytes never enter Stay."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.ingest import MODALITIES, extract, ingest
from stay.hook import read_ledger
from stay.tests._fixture import fixture_root


def main():
    root = fixture_root()
    assert set(MODALITIES) == {"image", "audio", "pdf", "chat", "code"}
    cases = [
        (
            "pdf",
            b"%PDF-1.4\nClaim from a document is extracted.\n\x00\xff\xfe binary",
            "Claim",
            "PdfExtract",
        ),
        (
            "image",
            b"\x89PNG\r\n\x1a\n" + b"\x00" * 12 + b"Place shot note is extracted",
            "Claim",
            "ImgExtract",
        ),
        (
            "audio",
            b"RIFF" + b"\x00\xff" * 8 + b" spoken claim is here",
            "Claim",
            "AudExtract",
        ),
        ("chat", "chat claim: the kettle is boiled", "Claim", "ChatExtract"),
        ("code", "USE CodeExtract\ndef hook():\n    return 1\n", "Claim", "CodeExtract"),
    ]
    for modality, raw, genus, lemma in cases:
        claims = extract(raw, modality)
        assert claims, (modality, claims)
        for claim in claims:
            assert isinstance(claim["text"], str)
            assert b"\x00" not in claim["text"].encode("utf-8", "replace")
        result = ingest(raw, modality, genus, lemma, root=root)
        assert result["id"].count("/") == 2
        blob = raw if isinstance(raw, bytes) else raw.encode("utf-8")
        if b"\x00" in blob or blob.startswith(b"%PDF") or blob.startswith(b"\x89PNG"):
            ledger_bytes = (root / "ids" / "ledger.jsonl").read_bytes()
            assert blob not in ledger_bytes
            for path in (root / "volumes").glob("*.md"):
                assert blob not in path.read_bytes()
    assert len(read_ledger(root)) == 5
    print("INGEST_DOOR_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

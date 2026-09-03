"""Temp Stay root for Stage 9 tests. Does not mutate the committed ledger."""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

STAY_PKG = Path(__file__).resolve().parents[1]
PARENT = Path(__file__).resolve().parents[2]


def bootstrap_path():
    parent = str(PARENT)
    if parent not in sys.path:
        sys.path.insert(0, parent)


bootstrap_path()


def fixture_root():
    dest = Path(tempfile.mkdtemp(prefix="stay-fx-"))
    shutil.copy(STAY_PKG / "schema.json", dest / "schema.json")
    shutil.copy(STAY_PKG / "swatches.md", dest / "swatches.md")
    shutil.copytree(STAY_PKG / "volumes", dest / "volumes")
    (dest / "ids").mkdir()
    (dest / "ids" / "ledger.jsonl").write_text("", encoding="utf-8")
    (dest / "window.json").write_text('{"markers": []}\n', encoding="utf-8")
    (dest / "tickets").mkdir()
    src_tickets = STAY_PKG / "tickets"
    if src_tickets.is_dir():
        for path in src_tickets.glob("*.json"):
            shutil.copy(path, dest / "tickets" / path.name)
    (dest / "cards").mkdir()
    return dest

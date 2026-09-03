#!/usr/bin/env python3
"""9.8 inject is card text. Do not concatenate SKILL.md. Do not install CDI."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import inject_card, use
from stay.tests._fixture import fixture_root

SKILL_INSTALLED = Path("/home/box/agent-data/workflows/claim-datum-interlock/SKILL.md")
SKILL_SOURCE = Path(
    "/workspace/praxis/novelty-notebook-20260902/skills/claim-datum-interlock/SKILL.md"
)


def main():
    root = fixture_root()
    sid = use("Name", "CardOnly", root=root)
    card = inject_card(sid, root=root)
    assert "id:" in card and "swatch:" in card
    assert "SKILL.md" not in card
    assert "# Claim-Datum Interlock" not in card
    if SKILL_SOURCE.is_file():
        skill = SKILL_SOURCE.read_text(encoding="utf-8")
        assert skill[:120] not in card
        assert card.strip() != skill.strip()
        assert skill not in card
    assert not SKILL_INSTALLED.exists()
    print("NO_SKILL_STUFF_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

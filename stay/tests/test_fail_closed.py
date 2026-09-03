#!/usr/bin/env python3
"""9.7 missing schema/volumes/ledger is a hard error. No disable switch."""

import json
import shutil
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from stay.hook import StayClosed, handle, require_ready
from stay.tests._fixture import fixture_root


def _must_close(root, label):
    try:
        require_ready(root)
    except StayClosed:
        return
    raise AssertionError(f"expected StayClosed for {label}")


def main():
    missing_schema = fixture_root()
    (missing_schema / "schema.json").unlink()
    _must_close(missing_schema, "schema")

    missing_volumes = fixture_root()
    shutil.rmtree(missing_volumes / "volumes")
    _must_close(missing_volumes, "volumes")

    empty_volumes = fixture_root()
    for path in (empty_volumes / "volumes").glob("*.md"):
        path.unlink()
    _must_close(empty_volumes, "volume files")

    missing_ledger = fixture_root()
    (missing_ledger / "ids" / "ledger.jsonl").unlink()
    _must_close(missing_ledger, "ledger")

    disabled = fixture_root()
    schema = json.loads((disabled / "schema.json").read_text(encoding="utf-8"))
    schema["disable"] = True
    (disabled / "schema.json").write_text(json.dumps(schema), encoding="utf-8")
    _must_close(disabled, "disable true")

    root = fixture_root()
    try:
        handle("identity", "USE", genus="Name", lemma="Ok", root=root, disable=True)
    except TypeError:
        pass
    require_ready(root)

    print("FAIL_CLOSED_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class SuiteTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

"""Stay claim-commit hook.

Events: memory-write, extract-ingest, promote, identity, i2.
Speech-only does not mint. Mentions do not mint. Fail closed.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

STAY_ROOT = Path(__file__).resolve().parent

HOOK_EVENTS = (
    "memory-write",
    "extract-ingest",
    "promote",
    "identity",
    "i2",
)

GENUS_SWATCH = {
    "Name": "slate",
    "Place": "moss",
    "System": "steel",
    "Quantity": "amber",
    "Ticket": "violet",
    "Issue": "rust",
    "Claim": "indigo",
    "Time": "pewter",
    "Event": "coral",
    "Role": "teal",
    "Org": "navy",
    "Artifact": "sand",
    "Source": "olive",
    "Method": "cyan",
    "Unit": "lime",
    "Rule": "plum",
    "State": "gray",
    "Signal": "gold",
    "Risk": "ochre",
}

POOL = [
    "ivory",
    "charcoal",
    "mint",
    "wine",
    "sky",
    "bronze",
    "lavender",
    "pine",
    "cream",
    "copper",
    "fog",
    "mustard",
    "ink",
]


class StayClosed(Exception):
    """Hard error. No disable path."""


def load_schema(root=None):
    root = Path(root or STAY_ROOT)
    path = root / "schema.json"
    if not path.is_file():
        raise StayClosed("missing schema")
    return json.loads(path.read_text(encoding="utf-8"))


def require_ready(root=None):
    """Missing schema, volumes, or ledger is a hard error. No disable switch."""
    root = Path(root or STAY_ROOT)
    schema_path = root / "schema.json"
    if not schema_path.is_file():
        raise StayClosed("missing schema")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    if schema.get("disable") is True:
        raise StayClosed("disable is not allowed")
    if schema.get("fail_closed") is not True:
        raise StayClosed("fail_closed must be true")
    volumes = root / "volumes"
    if not volumes.is_dir():
        raise StayClosed("missing volumes")
    genera = schema.get("genera") or []
    if not genera:
        raise StayClosed("missing volumes")
    for genus in genera:
        if not (volumes / f"{genus}.md").is_file():
            raise StayClosed(f"missing volume {genus}")
    ledger = root / "ids" / "ledger.jsonl"
    if not ledger.is_file():
        raise StayClosed("missing ledger")
    return schema


def read_ledger(root=None):
    root = Path(root or STAY_ROOT)
    path = root / "ids" / "ledger.jsonl"
    if not path.is_file():
        raise StayClosed("missing ledger")
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def append_ledger(row, root=None):
    root = Path(root or STAY_ROOT)
    path = root / "ids" / "ledger.jsonl"
    if not path.is_file():
        raise StayClosed("missing ledger")
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, separators=(",", ":")) + "\n")


def _make_suffix(genus, lemma, salt=""):
    digest = hashlib.sha1(f"{genus}/{lemma}/{salt}".encode("utf-8")).hexdigest()[:4]
    initial = (lemma[:1] or "x").lower()
    return f"{initial}-{digest}"


def _parts(sense_id):
    parts = (sense_id or "").split("/")
    if len(parts) != 3 or any(p == "" for p in parts):
        raise StayClosed("id must be Genus/Lemma/suffix")
    return parts


def _row_in(rows, sense_id):
    for row in rows:
        if row.get("id") == sense_id:
            return row
    return None


def _live_id(rows, genus, lemma, suffix=None):
    if suffix:
        want = f"{genus}/{lemma}/{suffix}"
        for row in rows:
            if row.get("id") == want and not row.get("superseded"):
                return want
        return None
    for row in rows:
        if row.get("superseded"):
            continue
        sid = row.get("id") or ""
        parts = sid.split("/")
        if len(parts) == 3 and parts[0] == genus and parts[1] == lemma:
            return sid
    return None


def row_by_id(sense_id, root=None):
    return _row_in(read_ledger(root), sense_id)


def supersede(sense_id, root=None):
    """Append-only honesty: mark the row superseded. Never delete the lemma."""
    require_ready(root)
    root = Path(root or STAY_ROOT)
    path = root / "ids" / "ledger.jsonl"
    rows = read_ledger(root)
    found = False
    out = []
    for row in rows:
        if row.get("id") == sense_id:
            row = dict(row)
            row["superseded"] = True
            found = True
        out.append(row)
    if not found:
        raise StayClosed("unknown id")
    path.write_text(
        "".join(json.dumps(r, separators=(",", ":")) + "\n" for r in out),
        encoding="utf-8",
    )
    return sense_id


def resolve(genus, lemma, root=None, suffix=None):
    """Later USE: same genus+lemma returns the live id. Retired suffixes are skipped."""
    require_ready(root)
    return _live_id(read_ledger(root), genus, lemma, suffix=suffix)


def mint(genus, lemma, root=None, suffix=None, swatch=None, kind=None, spoken=None):
    """First USE appends a unique Genus/Lemma/suffix row. Never recycle an id."""
    schema = require_ready(root)
    genera = schema.get("genera") or []
    if genus not in genera:
        raise StayClosed(f"unknown genus {genus}")
    lemma = str(lemma or "").strip()
    if not lemma:
        raise StayClosed("empty lemma")
    if "/" in lemma or "/" in (suffix or ""):
        raise StayClosed("lemma and suffix must not contain slashes")
    if suffix is not None:
        suffix = str(suffix).strip()
        if not suffix:
            raise StayClosed("empty suffix")
    rows = read_ledger(root)
    ids = {row.get("id") for row in rows}
    if suffix:
        want = f"{genus}/{lemma}/{suffix}"
        row = _row_in(rows, want)
        if row:
            if row.get("superseded"):
                raise StayClosed("never recycle a sense-id")
            return want
    else:
        existing = _live_id(rows, genus, lemma)
        if existing:
            return existing
        suffix = _make_suffix(genus, lemma)
        n = 0
        while f"{genus}/{lemma}/{suffix}" in ids:
            n += 1
            suffix = _make_suffix(genus, lemma, salt=str(n))
    sid = f"{genus}/{lemma}/{suffix}"
    _parts(sid)
    if sid in ids:
        raise StayClosed("never recycle a sense-id")
    paint = swatch or GENUS_SWATCH.get(genus, "ivory")
    row = {
        "id": sid,
        "genus": genus,
        "lemma": lemma,
        "swatch": paint,
    }
    if kind:
        row["kind"] = kind
    if spoken:
        row["spoken"] = spoken
    append_ledger(row, root=root)
    return sid


def use(genus, lemma, root=None, suffix=None, **kw):
    """Mint on first USE. Resolve on later USE."""
    return mint(genus, lemma, root=root, suffix=suffix, **kw)


def inject_card(sense_id, root=None, gloss="", glyph=""):
    """One card. Plaintext id and swatch name. Not a volume. Not SKILL.md."""
    require_ready(root)
    genus, lemma, _suffix = _parts(sense_id)
    swatch = GENUS_SWATCH.get(genus, "ivory")
    for row in read_ledger(root):
        if row.get("id") == sense_id and row.get("swatch"):
            swatch = row["swatch"]
            break
    gloss_text = (gloss or lemma).replace("\n", " ").strip()[:48]
    if has_pui(gloss_text):
        raise StayClosed("PUI closed")
    glyph_text = (glyph or "").replace("\n", " ").strip()[:16]
    card = (
        f"id: {sense_id}\n"
        f"swatch: {swatch}\n"
        f"glyph: {glyph_text}\n"
        f"gloss: {gloss_text}\n"
    )
    return card



SSN_SHAPE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
SSN_WORD = re.compile(r"\bSSN\b", re.I)
MAGIC_RE = re.compile(r"%PDF-\d+(?:\.\d+)?")
RIFF_RE = re.compile(r"\bRIFF\b")


def has_pui(text):
    """Fake or real SSN shape. PUI closed. No patient charts."""
    if text is None:
        return False
    s = str(text)
    return bool(SSN_SHAPE.search(s) or SSN_WORD.search(s))


def has_raw_magic(text):
    s = str(text or "")
    return bool(MAGIC_RE.search(s) or RIFF_RE.search(s))


def drop_raw_magic(text):
    t = MAGIC_RE.sub(" ", str(text or ""))
    t = RIFF_RE.sub(" ", t)
    return t


def is_claim_commit(text):
    """Ordinary speech without identity, arithmetic or quantities is not a mint."""
    if text is None:
        return False
    s = str(text)
    if not s.strip():
        return False
    if re.search(r"\bUSE\b", s, re.I):
        return True
    if re.search(r"\bI2\b", s, re.I):
        return True
    if re.search(r"\bis\b", s, re.I):
        return True
    if re.search(r"\$\d", s):
        return True
    if re.search(r"\d+\s*[+\-*/]\s*\d+", s):
        return True
    return False


def gate_text(text, lemma=None):
    """Same fail-closed for handle and ingest.
    Returns 'ok', 'mention', or 'speech'. StayClosed on PUI or raw magic.
    """
    if has_pui(text):
        raise StayClosed("PUI closed")
    if has_raw_magic(text):
        raise StayClosed("raw bytes never enter Stay")
    if is_mention(text, lemma=lemma):
        return "mention"
    if not is_claim_commit(text):
        return "speech"
    return "ok"


def _strip_mention_spans(text):
    stripped = re.sub(r"```[\s\S]*?```", "", text)
    stripped = re.sub(r"`[^`]*`", "", stripped)
    stripped = re.sub(r'"[^"]*"', "", stripped)
    stripped = re.sub(r"'[^']*'", "", stripped)
    return stripped


def is_mention(text, lemma=None):
    """Backticks, fences, and quotes are mentions. Mentions do not mint."""
    if text is None:
        return False
    s = str(text).strip()
    if not s:
        return False
    if s.startswith("```") and s.endswith("```") and len(s) >= 6:
        return True
    if s.startswith("`") and s.endswith("`") and len(s) >= 2:
        return True
    if len(s) >= 2 and ((s[0] == s[-1] == '"') or (s[0] == s[-1] == "'")):
        return True
    body = _strip_mention_spans(s)
    if lemma and lemma in s and lemma not in body:
        return True
    if body.strip() == "":
        return True
    return False


def handle(event, text="", genus=None, lemma=None, root=None, **kw):
    """Locked hook. Claim-commit only. Speech-only does not mint."""
    require_ready(root)
    if event not in HOOK_EVENTS:
        return None
    verdict = gate_text(text, lemma=lemma)
    if verdict != "ok":
        return None
    if lemma is not None and not str(lemma).strip():
        raise StayClosed("empty lemma")
    if not genus or not lemma:
        return None
    sid = use(genus, lemma, root=root, **kw)
    return inject_card(sid, root=root)


def load_window(root=None):
    root = Path(root or STAY_ROOT)
    path = root / "window.json"
    if not path.is_file():
        return {"markers": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    markers = data.get("markers")
    if markers is None:
        markers = []
    return {"markers": markers}


def save_window(window, root=None):
    root = Path(root or STAY_ROOT)
    path = root / "window.json"
    path.write_text(json.dumps(window, indent=2) + "\n", encoding="utf-8")


def pool_available(root=None):
    held = set()
    for marker in load_window(root).get("markers") or []:
        if isinstance(marker, dict):
            paint = marker.get("swatch") or marker.get("paint")
            if paint:
                held.add(paint)
    return [name for name in POOL if name not in held]


def assign_window_paint(sense_id, root=None):
    """Hot-window paint from the pool. Ledger swatch (genus hue) stays on the row."""
    require_ready(root)
    available = pool_available(root)
    paint = available[0] if available else "ivory"
    window = load_window(root)
    markers = list(window.get("markers") or [])
    markers.append({"id": sense_id, "swatch": paint})
    save_window({"markers": markers}, root=root)
    return paint


def expire_window(root=None):
    """After the hot window, paint returns to the pool. Ledger rows stay."""
    require_ready(root)
    window = load_window(root)
    returned = []
    for marker in window.get("markers") or []:
        if isinstance(marker, dict):
            paint = marker.get("swatch") or marker.get("paint")
            if paint:
                returned.append(paint)
    save_window({"markers": []}, root=root)
    return returned


def ledger_has(sense_id, root=None):
    return any(row.get("id") == sense_id for row in read_ledger(root))

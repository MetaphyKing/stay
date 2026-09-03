"""Stay ingest door.

One door for image, audio, PDF, chat, and code: extract a claim, then mint.
Raw bytes never enter volumes or the ledger. Gradient only if a named
reversible ticket already exists.
"""

from __future__ import annotations

import json
from pathlib import Path


from .hook import (
    STAY_ROOT,
    StayClosed,
    drop_raw_magic,
    gate_text,
    has_pui,
    inject_card,
    read_ledger,
    require_ready,
    use,
)

MODALITIES = ("image", "audio", "pdf", "chat", "code")


def extract(raw, modality="chat"):
    """Turn raw input into claims. Drop binary. Never return raw bytes."""
    if modality not in MODALITIES:
        modality = "chat"
    if isinstance(raw, bytes):
        runs = []
        cur = []
        for byte in raw:
            if 32 <= byte < 127:
                cur.append(chr(byte))
            else:
                if len(cur) >= 3:
                    runs.append("".join(cur).strip())
                cur = []
        if len(cur) >= 3:
            runs.append("".join(cur).strip())
        text = " ".join(r for r in runs if r)
    else:
        text = str(raw)
    text = drop_raw_magic(text)
    claims = []
    for line in text.splitlines():
        line = " ".join(line.split()).strip()
        if not line:
            continue
        if has_pui(line):
            continue
        claims.append({"text": line, "modality": modality})
    if not claims:
        leftover = " ".join(text.split()).strip()
        leftover = drop_raw_magic(leftover)
        if leftover and not has_pui(leftover):
            claims.append({"text": leftover, "modality": modality})
    return claims



def _as_text(raw):
    if isinstance(raw, bytes):
        return raw.decode("utf-8", "replace")
    return str(raw)


def _raw_blob(raw):
    if isinstance(raw, bytes):
        return raw
    return str(raw).encode("utf-8")


def _assert_no_raw(raw, root):
    """Raw bytes never enter volumes or ledger."""
    blob = _raw_blob(raw)
    if len(blob) < 4:
        return
    distinctive = (b"\x00" in blob) or (b"\xff" in blob) or blob.startswith(b"%PDF") or blob.startswith(b"\x89PNG")
    if not distinctive:
        return
    root = Path(root or STAY_ROOT)
    ledger = root / "ids" / "ledger.jsonl"
    if ledger.is_file() and blob in ledger.read_bytes():
        raise StayClosed("raw bytes entered ledger")
    volumes = root / "volumes"
    if volumes.is_dir():
        for path in volumes.glob("*.md"):
            if blob in path.read_bytes():
                raise StayClosed("raw bytes entered volumes")


def ingest(raw, modality, genus, lemma, root=None, suffix=None, kind=None, spoken=None):
    """Extract claims, then mint. Same door for every modality."""
    require_ready(root)
    if modality not in MODALITIES:
        raise StayClosed(f"unknown modality {modality}")
    if has_pui(_as_text(raw)):
        raise StayClosed("PUI closed")
    claims = extract(raw, modality)
    if not claims:
        raise StayClosed("extract produced no claim")
    admitted = []
    for claim in claims:
        verdict = gate_text(claim.get("text"), lemma=lemma)
        if verdict != "ok":
            continue
        admitted.append(claim)
    if not admitted:
        raise StayClosed("not a claim-commit")
    claims = admitted
    sid = use(
        genus,
        lemma,
        root=root,
        suffix=suffix,
        kind=kind,
        spoken=spoken,
    )
    gloss = claims[0]["text"][:48]
    if has_pui(gloss):
        raise StayClosed("PUI closed")
    card = inject_card(sid, root=root, gloss=gloss)
    _assert_no_raw(raw, root)
    return {"id": sid, "card": card, "claims": claims}


def gradient(ticket_id, root=None):
    """Gradient display only if stay/tickets/<id>.json exists, named and reversible."""
    require_ready(root)
    root = Path(root or STAY_ROOT)
    if not ticket_id or "/" in str(ticket_id) or ".." in str(ticket_id):
        raise StayClosed("gradient requires named reversible ticket")
    path = root / "tickets" / f"{ticket_id}.json"
    if not path.is_file():
        raise StayClosed("gradient requires named reversible ticket")
    data = json.loads(path.read_text(encoding="utf-8"))
    named = data.get("named") is True or bool(data.get("name"))
    reversible = data.get("reversible") is True
    if not named or not reversible:
        raise StayClosed("ticket must be named and reversible")
    return data

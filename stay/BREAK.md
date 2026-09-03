# BREAK.md - Stay Stage 12.1 re-Break

Verifier: Gauge (independent). Re-Break after Kiln patch. 2026-09-02 PT.
Run: `stay-20260902`. I did not build. I did not patch. I did not install CDI. I did not git-commit. Stay is not a 90. I did not score novelty.

First Break: FAIL. Open B1 empty lemma, B4 PUI gloss, B2 event-not-text, B6 PDF magic.
This file is the re-Break. Same attacks. Fixtures on `fixture_root()`. Fake SSN shape only (`000-00-0000`, `FakePat`).

**Verdict: PASS.** Previously open attacks now fail-closed. Held attacks stayed held. Claim-commit still mints.

PASS = Stay held (fail-closed). FAIL = the attack landed.

---

## Must fail-closed (were FAIL)

### A2 leak PUI/SSN onto a card - PASS

Command: `ingest("SSN 000-00-0000 for FakePat", "chat", "Name", "FakePat", root=root)`

```
StayClosed: PUI closed
ledger=''
leaked=False
```

FACT: ingest refused. Fake SSN did not enter the fixture ledger. Extra: `id 000-00-0000 for FakePat` (no word SSN) also StayClosed PUI closed.

### A6 empty lemma mint Name//x-6148 (B1) - PASS

Command: `use("Name", "", root=root)`

```
StayClosed: empty lemma
rows=[]
```

FACT: mint refused. Extra: empty suffix also StayClosed `empty suffix`.

### A3d ordinary speech on legal event (B2) - PASS

Command: `handle("memory-write", text="hello there", genus="Name", lemma="SpeechLeak")`

```
out=None
n0=0 n1=0 minted=False
```

FACT: small talk did not mint. Held path still live: `handle("memory-write", text="USE SpeechOk", ...)` returned card `Name/SpeechOk/s-7647`.

### A7 PDF magic in extract (B6) - PASS

Command: `extract(b"%PDF-1.4\nJessica neighbor\n\x00\xff", "pdf")`

```
claims=[{'text': 'Jessica neighbor', 'modality': 'pdf'}]
magic=False
```

FACT: `%PDF-1.4` dropped. Neighbor text remained as the claim.

---

## Must stay held (were PASS)

### A1 unify two Jessicas by color - PASS

```
a=Name/Jessica/j-a3f0
b=Name/Jessica/j-b7e1
swatch: slate on both cards
```

FACT: same paint, two sense-ids.

### A3a set schema.disable true - PASS

```
StayClosed: disable is not allowed
```

### A3b handle disable=True - PASS (noisy)

```
TypeError: mint() got an unexpected keyword argument 'disable'
```

FACT: no disable path. Error is still TypeError through `**kw`, not StayClosed.

### A3c unknown event speech - PASS

```
out=None n0=0 n1=0
```

### A4 mention-spoof mint - PASS

```
identity '`Jessica`' -> None
memory-write '```\nJessica\n```' -> None
promote '"Jessica"' -> None
i2 "'Jessica'" -> None
extract-ingest 'see `Jessica` only' -> None
n0=0 n1=0
```

### A5 concat files as session store - PASS

```
session_store='graph-on-disk'
FILE_BREAK=False
```

### A10 CDI skill uninstalled - PASS

```
exists=False path=/home/box/agent-data/workflows/claim-datum-interlock/SKILL.md
```

### A11 committed ledger unmutated - PASS

```
{"id":"Name/Jessica/j-a3f0","genus":"Name","lemma":"Jessica","swatch":"slate","spoken":"Jessica"}
```

---

## Hygiene

`hook.py` docstring for `has_pui` contains the word `patient` as the closed-policy sentence ("No patient charts."). That is not a dossier and not a Break FAIL.

---

## Rollup

| Attack | First Break | Re-Break |
|---|---|---|
| A1 unify two Jessicas by color | PASS | PASS |
| A2 leak PUI/SSN onto a card | FAIL | PASS |
| A3a disable true | PASS | PASS |
| A3b disable kwarg | PASS | PASS |
| A3c unknown event | PASS | PASS |
| A3d speech on legal event | FAIL | PASS |
| A4 mention-spoof mint | PASS | PASS |
| A5 concat session store | PASS | PASS |
| A6 empty lemma mint | FAIL | PASS |
| A7 PDF magic extract | FAIL | PASS |
| A10 CDI uninstalled | PASS | PASS |
| A11 ledger unmutated | PASS | PASS |

First Break FAIL is history. This re-Break is PASS.

---

## Facts vs inferences

**FACT.** A2 StayClosed PUI closed. Fixture ledger empty of SSN shape.
**FACT.** A6 StayClosed empty lemma. No `Name//x-6148` row.
**FACT.** A3d `hello there` on `memory-write` returned None. No SpeechLeak id.
**FACT.** A7 extract claim is `Jessica neighbor`. No `%PDF`.
**FACT.** A1 two Jessica ids, shared slate.
**FACT.** disable true StayClosed. Mentions None. No FILE_BREAK. CDI skill absent. Seed ledger unchanged.
**FACT.** `USE SpeechOk` still mints.
**INFERENCE.** `is_claim_commit` is still regex (`USE`, `I2`, `\bis\b`, `$` digit, `n + n`). Ordinary-speech close is that regex, not NLP.
**INFERENCE.** TypeError on disable kwarg remains an untyped `**kw` leak into mint. Not a disable switch.

Stay is not a 90. Gauge did not score novelty.

---

*End Gauge Stage 12.1 re-Break. PASS. No patch. No commit. No CDI install.*

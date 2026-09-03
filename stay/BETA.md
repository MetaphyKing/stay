# BETA.md — Stay Stage 15.1

Seat: Scout (`c79aabba-eb31-4d63-bfb3-a0ab527a6f7f`). Second seat, not Kiln.
Date: 2026-09-02 PT
Stay root: `/workspace/praxis/stay-20260902/stay/`
Bible: `/workspace/praxis/stay-20260902/STAY_BIBLE.md` step 15.1
Do not implement Stay. Did not write hook.py. Did not install CDI. Did not git-commit. Production is not this stage. Stay is not a 90.

---

## Corpus

Second corpus (Director-named):
- `/workspace/praxis/novelty-notebook-20260902/BRIEFING.md`
- `/workspace/praxis/novelty-notebook-20260902/IDEAS.md` I14 / I15 names

Door: extract-then-mint. `stay.ingest.extract` then `stay.ingest.ingest` (chat). Probe of `stay.hook.handle(..., event="extract-ingest")`. File bytes were not passed as the mint blob.

PUI on corpus: False / False.

Extract counts (line-split, not NLP): BRIEFING.md 27 claims. IDEAS.md 33 claims. Operator selected SPTS / CDI / Stay rows. Did not dump the file.

---

## What minted

Ledger before: 2 (Alpha Jessicas). Ledger after: 9. Append-only. Alpha rows untouched.

| id | src | spoken | kind | paint |
|---|---|---|---|---|
| `System/SPTS-SinglePrime/s-8293` | BRIEFING I02 | SPTS | document-claim | steel |
| `System/SPTS-TrinaryEthics/s-abf8` | BRIEFING I02 | SPTS | document-claim | steel |
| `System/SPTS-Superposition/s-b18a` | BRIEFING I02 | SPTS | document-claim | steel |
| `Artifact/CDI-v4/c-2bff` | BRIEFING / IDEAS I14 | CDI | honest-result-not-final | sand |
| `Artifact/Stay/s-77d6` | IDEAS I15 | Stay | design-not-built | sand |
| `Claim/OverloadedLattice/o-1a64` | BRIEFING lattice sentence | (none) | (none) | indigo |
| `Claim/PdfCdiProbe/p-8c29` | door probe, not corpus | (none) | (none) | indigo |

Cards (plaintext id + swatch name, not a volume dump):

```
id: System/SPTS-SinglePrime/s-8293
swatch: steel
gloss: SPTS is Single Prime Trinary System.
```

```
id: System/SPTS-TrinaryEthics/s-abf8
swatch: steel
gloss: SPTS is Trinary Ethics.
```

```
id: System/SPTS-Superposition/s-b18a
swatch: steel
gloss: SPTS is Superposition Trinary System.
```

```
id: Artifact/CDI-v4/c-2bff
swatch: sand
gloss: CDI v4 is mint-on-use plus session. Gauge 84. No
```

```
id: Artifact/Stay/s-77d6
swatch: sand
gloss: Stay is the encyclopedia under the window. Sense
```

FACT: three SPTS lemmas, three ids, one spoken string `SPTS`. Recycled steel. Did not unify.
FACT: later `handle("extract-ingest", "USE Artifact Stay", ...)` resolved `Artifact/Stay/s-77d6`. Did not mint a second Stay.
FACT: BRIEFING.md and IDEAS.md bytes are not in ledger or volumes. `%PDF` not in ledger. CDI skill still absent.

---

## What was refused

| kind | input | result | ledger delta |
|---|---|---|---|
| mention | `see \`Stay\` only` | handle None | 0 |
| mention | `` `CDI` `` | handle None | 0 |
| mention | fenced `SPTS` | handle None | 0 |
| speech event | event=`speech` | handle None | 0 |
| speech text | `hello there` on extract-ingest | handle None | 0 |
| PUI | `patient SSN 123-45-6789 must not mint` | StayClosed `PUI closed` | 0 |
| untrusted theater | I07 Gold Master / $35k / PFLOPS | operator refuse, not minted | 0 |
| raw file | whole BRIEFING.md / IDEAS.md | operator refuse; extract then selected mint | 0 |
| handle vs ingest | lattice sentence, no is/USE/I2/$n | handle None; ingest.py then minted | see minted |

FACT: mentions do not mint.
FACT: PUI closed.
FACT: raw PDF probe `%PDF-1.4\nCDI v4 claim...` extracted to `CDI v4 claim from a document.` Blob not stored. Minted `Claim/PdfCdiProbe/p-8c29` as a door check, not a corpus row.

---

## Fixes needed (named, not patched)

Scout did not write hook.py. These stay in BETA.md.

1. **Two doors disagree.** `handle(extract-ingest)` requires `is_claim_commit` (`USE`, `I2`, `\bis\b`, `$digit`, or arithmetic). `ingest.py` mints after extract with no that check. Lattice sentence (`Overloaded names stay a lattice...`) refused on handle, minted on ingest. Beta used ingest as the extract-then-mint door. Spec should say which door is canonical for Stage 15.

2. **extract() is line-split.** 27+33 lines, including headings and table rows. Not claim NLP. Operator still has to pick. Honest remainder of con 15.

3. **Gloss truncates at 48.** CDI-v4 card cuts `Not a 90`. Stay card cuts `Sense-id is the key`. Fine for a glance. Named if a later Cycle wants the bar line on the card.

No StayClosed on the happy path. No CDI install. No concat session. No unify of the three SPTS.

---

## Facts vs inferences

**FACT.** Seat Scout. Corpus BRIEFING.md + IDEAS.md I14/I15.
**FACT.** Minted 7 new rows. Alpha 2 Jessicas kept. Ledger 9.
**FACT.** Mentions, speech, PUI refused. CDI uninstalled. 19 volumes still 19.
**FACT.** handle and ingest disagree on claim-commit.
**INFERENCE.** PdfCdiProbe is extra door evidence, not a second-corpus claim. Leave it. Do not delete.
**INFERENCE.** Production still needs Logan yes. This file is Beta, not 16.1.

UNTRUSTED as hardware: $35k, PFLOPS, Gold Master. Not minted.

---

## Verification (15.1)

```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/BETA.md').read().lower(); assert 'seat' in t or 'corpus' in t; print('BETA_OK')"
```

Expected: `BETA_OK`

Scout does not mark Bible 15.1 `[x]`. Bible Bot updates the tracker.

Terminal state: **SUCCESS as Beta walk.** BLOCKED as Production. No hook.py edit. No CDI install. No git-commit.

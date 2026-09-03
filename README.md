<p align="center">
  <img width="1280" height="853" alt="stay-hero" src="https://github.com/MetaphyKing/stay/blob/main/assets/Stay-hero.webp?raw=true">
</p>


# Stay

Permanent context that is not the context window.

Stay is a locked harness hook with a small graph on disk. First write mints a unique sense-id into a topical volume. Later turns get one compact card. The encyclopedia stays on disk. The window stays small.

Swatch names are paint. Recycle paint. Never recycle an id.

Stay is not a 90. It is not a novelty claim. CDI is not this package.

## Install

Python 3.10 or newer. No third-party dependencies.

```bash
pip install "stay @ git+https://github.com/MetaphyKing/stay"
```

From a local checkout:

```bash
git clone https://github.com/MetaphyKing/stay.git
cd stay
pip install .
```

Or skip install and put the repo root on `PYTHONPATH`.

## Quick start

```bash
python3 -c "from stay.hook import use, inject_card; print(inject_card(use('Name','Jessica')))"
```

That prints one plaintext card:

```
id: Name/Jessica/j-a3f0
swatch: slate
glyph:
gloss: Jessica
```

A second spoken Jessica is a different id if you pass a different suffix:

```python
from stay.hook import use, inject_card

a = use("Name", "Jessica", suffix="j-a3f0")
b = use("Name", "Jessica", suffix="j-b7c1")
print(a)  # Name/Jessica/j-a3f0
print(b)  # Name/Jessica/j-b7c1
print(inject_card(a, gloss="Jessica the author"))
```

Same spoken name. Same genus hue is legal paint. Different suffix. Different sense-id. Unify-by-color is wrong.

Demo ledger rows (two Jessicas) are fictional.

## How it works

**Sense-id.** `Genus/Lemma/suffix`. The id is the identity. First `use` mints. Later `use` of the same live genus+lemma resolves. A retired suffix is skipped. An id is never reused.

**Card inject.** Working context is one card: `id`, `swatch`, optional `glyph`, one-line `gloss`. Not a volume dump. Not SKILL stuffing.

**Graph on disk.** Session store is `stay/ids/ledger.jsonl` (append-only). Topical encyclopedia lives in `stay/volumes/*.md`. `stay/window.json` holds hot-window paint only. Concatenated files are not the store.

**Paint.** 19 genus hues plus a 13-name recycle pool. Color is glance not key. After the hot window, pool paint returns. Ledger rows stay.

**Fail-closed hook.** Claim-commit only. Seats cannot disable it. `schema.disable: true` is a hard error.

## Hook events

`stay.hook.handle` mints only on these events:

| Event | Role |
| --- | --- |
| `memory-write` | persist a named claim |
| `extract-ingest` | extract then mint |
| `promote` | promote an extracted claim |
| `identity` | bind a Name or other identity |
| `i2` | I2 claim-commit |

Speech-only does not mint. Mentions (backticks, fences, quotes) do not mint. Unknown events return `None`.

```python
from stay.hook import handle

card = handle("identity", "USE Name Jessica", genus="Name", lemma="Jessica")
# ordinary speech on a legal event returns None
handle("memory-write", "hello there", genus="Claim", lemma="Hello")
```

A claim-commit is text with `USE`, `I2`, `is`, a `$` amount or simple arithmetic. Everything else is speech.

## Ingest

One door for image, audio, PDF, chat and code. Extract a claim. Then mint. Raw bytes never enter volumes or the ledger.

```python
from stay.ingest import extract, ingest

claims = extract("SPTS is Single Prime Trinary System.", modality="chat")
result = ingest(
    "SPTS is Single Prime Trinary System.",
    modality="chat",
    genus="System",
    lemma="SPTS-SinglePrime",
    spoken="SPTS",
)
print(result["id"])
print(result["card"])
```

Modalities: `image`, `audio`, `pdf`, `chat`, `code`.

`extract` drops binary and PUI-shaped lines. `ingest` runs the same `gate_text` as `handle`. If nothing admitted, it raises `StayClosed`.

## Public API

From `stay.hook`:

| Call | What it does |
| --- | --- |
| `use(genus, lemma, suffix=None, kind=None, spoken=None, root=None)` | mint on first USE, resolve later |
| `mint(...)` | first-write only; refuses a recycled id |
| `resolve(genus, lemma, suffix=None, root=None)` | live id or `None` |
| `inject_card(sense_id, gloss="", glyph="", root=None)` | one plaintext card |
| `handle(event, text, genus, lemma, root=None)` | locked hook |
| `gate_text(text, lemma=None)` | `"ok"`, `"mention"` or `"speech"`; raises on PUI or raw magic |
| `supersede(sense_id, root=None)` | append-only retire; never deletes the lemma |
| `require_ready(root=None)` | missing schema, volumes or ledger is hard error |
| `read_ledger(root=None)` | all ledger rows |
| `assign_window_paint(sense_id)` / `expire_window()` | hot-window paint from the pool |

From `stay.ingest`:

| Call | What it does |
| --- | --- |
| `extract(raw, modality="chat")` | claims only; never returns raw bytes |
| `ingest(raw, modality, genus, lemma, ...)` | extract then mint |
| `gradient(ticket_id)` | display only if `stay/tickets/<id>.json` exists, named and reversible |

`StayClosed` is the hard error. There is no disable switch.

Pass `root=` to point at a fixture or another Stay tree. Default root is the installed `stay/` package directory.

## Layout

```
stay/
  hook.py           locked claim-commit hook
  ingest.py         extract-then-mint door
  schema.json       genera, fail_closed, hook events
  swatches.md       32 named colors (paint not keys)
  window.json       hot-window markers
  ids/ledger.jsonl  append-only sense-ids
  volumes/          19 topical encyclopedia files
  cards/_template.md
  tickets/          named reversible gradient tickets
  tests/
docs/BIBLE.md       16-stage Stay Bible
assets/stay-hero.png
assets/download-stay-hero.svg
```

Genus volumes (canonical order): Name, Place, System, Quantity, Ticket, Issue, Claim, Time, Event, Role, Org, Artifact, Source, Method, Unit, Rule, State, Signal, Risk.

Genus hues: Name slate, Place moss, System steel, Quantity amber, Ticket violet, Issue rust, Claim indigo, Time pewter, Event coral, Role teal, Org navy, Artifact sand, Source olive, Method cyan, Unit lime, Rule plum, State gray, Signal gold, Risk ochre.

Pool (recycle after the hot window): ivory, charcoal, mint, wine, sky, bronze, lavender, pine, cream, copper, fog, mustard, ink.

No alarm-red. No error-red as a genus hue. Hex sits under the swatch name, never instead of it.

## Fail-closed

These raise `StayClosed` or mint zero rows. Seats cannot turn them off.

- missing `schema.json`, any of the 19 volumes or `ids/ledger.jsonl`
- `schema.disable` true, or `fail_closed` not true
- unknown genus
- empty lemma or empty suffix
- slash inside lemma or suffix
- recycled sense-id
- SSN-shaped claim or gloss (fake or real)
- mention spans
- speech or unknown hook events
- PDF or RIFF magic as a claim
- raw bytes entering volumes or the ledger
- gradient without a named reversible ticket

## Tests

From the repo root:

```bash
PYTHONPATH=. python3 -m unittest discover -s stay/tests -p 'test_*.py'
```

Each file under `stay/tests/test_*.py` also runs alone:

```bash
PYTHONPATH=. python3 stay/tests/test_two_jessica.py
PYTHONPATH=. python3 stay/tests/test_fail_closed.py
```

Expected: `TWO_JESSICA_OK`, `NEVER_RECYCLE_OK`, `PLAINTEXT_CARD_OK` and the rest of the suite green.

## License

Apache 2.0. Copyright 2026 Metaphy LLC / Randell Logan Smith.

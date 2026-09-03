# Stay

Permanent context that is not the context window.

Stay keeps a small on-disk graph of sense-ids. Swatch names are paint. Recycle paint. Never recycle an id. The session store is `stay/ids/ledger.jsonl`, not concatenated files.

## What it does

- **Sense-id keys.** `Genus/Lemma/suffix`. Two Jessicas can share a spoken name and a swatch. They do not share an id.
- **Card inject.** Working context is one plaintext card (id, swatch, gloss). Not a volume dump. Not SKILL stuffing.
- **Fail-closed hook.** Claim-commit on `memory-write`, `extract-ingest`, `promote`, `identity`, `i2`. Speech-only does not mint. Mentions do not mint. Seats cannot disable the hook.
- **Ingest door.** Extract a claim, then mint. Raw bytes never enter volumes or the ledger.

Stay is not a 90. It is not a novelty claim. CDI is not this package.

## Install from git

```bash
pip install "stay @ git+https://github.com/MetaphyKing/stay"
```

Until that URL exists, install from a local checkout:

```bash
pip install /path/to/stay
```

## Run

```bash
PYTHONPATH=. python3 -c "from stay.hook import use, inject_card; print(inject_card(use('Name','Jessica')))"
```

Tests live under `stay/tests/`. Demo ledger rows (two Jessicas) are fictional.

## License

Apache 2.0. Copyright 2026 Metaphy LLC / Randell Logan Smith.

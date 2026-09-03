# Stay Stage 9 gates

Six gates. Build is not done without all six.

## TEST

Fixtures live under `stay/tests/test_*.py` and a temp root helper in `stay/tests/_fixture.py`.

Run from this computer (Python path is the parent of the `stay` package):

```
python3 /workspace/praxis/stay-20260902/stay/tests/test_inject_card.py
python3 /workspace/praxis/stay-20260902/stay/tests/test_paint_recycle.py
python3 /workspace/praxis/stay-20260902/stay/tests/test_hook_events.py
python3 /workspace/praxis/stay-20260902/stay/tests/test_mint_resolve.py
python3 /workspace/praxis/stay-20260902/stay/tests/test_mentions.py
python3 /workspace/praxis/stay-20260902/stay/tests/test_fail_closed.py
python3 /workspace/praxis/stay-20260902/stay/tests/test_no_skill_stuff.py
python3 /workspace/praxis/stay-20260902/stay/tests/test_ingest_door.py
python3 /workspace/praxis/stay-20260902/stay/tests/test_cdi_sit.py
python3 /workspace/praxis/stay-20260902/stay/tests/test_gradient_ticket.py
```

Committed stores for fixture-free checks:

- `stay/ids/ledger.jsonl` (append-only sense-ids)
- `stay/window.json` (`markers` 0 legal pre-USE)
- `stay/schema.json`, `stay/volumes/`, `stay/swatches.md`

## DOCS

How a stranger runs Stay on this tree:

1. Root is `/workspace/praxis/stay-20260902/`. Package is `stay/`.
2. Put that root on `PYTHONPATH` (the tests insert it themselves).
3. Claim-commit through `stay.hook.handle` on events `memory-write`, `extract-ingest`, `promote`, `identity`, `i2`. Speech-only does not mint.
4. Ingest any modality through `stay.ingest.ingest`: extract a claim, then mint. Same fail-closed gate as `handle` (speech, mention, PUI, empty lemma, PDF). Raw bytes never enter volumes or the ledger.
5. Working context is one card from `stay.hook.inject_card`. Do not paste a volume. Do not stuff SKILL.md.
6. Session store is `stay/ids/ledger.jsonl`, not concatenated files.

```
PYTHONPATH=/workspace/praxis/stay-20260902 python3 -c "from stay.hook import use, inject_card; print(inject_card(use('Name','Jessica')))"
```

## EXAMPLES

Two Jessicas, two ids. Same spoken name. Same swatch allowed. Unify-by-color is wrong.

- `Name/Jessica/j-a3f0` — Jessica the author (seed row in the ledger). Swatch `slate`.
- `Name/Jessica/j-b7e1` — Jessica the neighbor. Same spoken "Jessica". Same genus hue `slate` is legal paint. Different suffix. Different sense-id.

Mint with an explicit suffix to keep them apart. Resolve without a suffix returns the first live `Name/Jessica` row. Recycle paint. Never recycle a sense-id.

## ERRORS

Fail-closed paths (hard `StayClosed`, no disable switch):

- missing `schema.json`
- missing `volumes/` or any of the 19 genus files
- missing `ids/ledger.jsonl`
- `schema.disable` true (refused)
- `schema.fail_closed` not true
- unknown genus
- empty lemma or empty suffix
- SSN-shaped claim or gloss (fake or real)
- mention spans (backticks, fences, quotes) mint zero rows
- speech / unknown hook events mint zero rows
- ordinary speech on a legal event (no identity, arithmetic, or quantity)
- PDF or RIFF magic as a claim
- gradient without `stay/tickets/<id>.json`
- ticket present but not named and reversible
- raw bytes entering volumes or ledger

Seats cannot disable the hook.

## QUALITY

No silent TODOs on the hook. `stay/hook.py` has none. Fail closed rather than skip. Concat is not a session store. Mentions are a named hazard, not a safety fix.

## BRANDING

Named swatches in plaintext on every card. No alarm-red. No error-red as a genus hue.

Genus hues: Name slate, Place moss, System steel, Quantity amber, Ticket violet, Issue rust, Claim indigo, Time pewter, Event coral, Role teal, Org navy, Artifact sand, Source olive, Method cyan, Unit lime, Rule plum, State gray, Signal gold, Risk ochre.

Pool: ivory, charcoal, mint, wine, sky, bronze, lavender, pine, cream, copper, fog, mustard, ink.

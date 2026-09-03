# OPTIMIZE.md — Stay Stage 13.1

Run: `stay-20260902`
Seat: Kiln. Stage 13 Optimize only. 2026-09-02 PT.
Break PASS is `/workspace/praxis/stay-20260902/BREAK.md`.
Measure first. Compounding-chain cuts only. No Alpha. Stay is not a 90. CDI uninstalled. No git-commit.

Named fixture: `Name/Jessica/j-a3f0` on `fixture_root()` so the committed ledger stayed one seed row.

---

## Numbers first (before any cut)

FACT. These numbers were taken on this computer before the mint scan cut.

| Metric | Value |
|---|---|
| Card bytes (Jessica inject) | 61 bytes |
| `Name.md` volume bytes | 152 bytes |
| 19 volumes total | 2910 bytes |
| Volume count | 19 |
| Card vs Name.md | Name.md is 2.49x the card |
| Card vs all volumes | all volumes are 47.7x the card |
| Committed ledger | 98 bytes, 1 row |
| Committed `window.json` marker count | 0 |
| Marker count after one `assign_window_paint` | 1 |
| Mint latency, 1 new lemma | 0.4956 ms |
| Mint latency, 100 new lemmas | 57.6959 ms (0.577 ms each) |
| Mint latency, 1000 new lemmas | 2292.4305 ms (2.2924 ms each) |
| Remint same lemma x100 | 31.4264 ms |
| `read_ledger` calls per first mint | 3 |
| `require_ready` calls per first mint | 2 |

Card used:

```
id: Name/Jessica/j-a3f0
swatch: slate
glyph:
gloss: Jessica
```

**INFERENCE from the numbers (not a cut yet).** Card vs volume is already the product: one card is 61 bytes against 2910 bytes if a seat stuffed all volumes. That ratio does not need a cut. Window marker count 0 is legal pre-USE. The compounding chain is mint: per-mint cost grew from 0.50 ms at 1 row to 2.29 ms each at 1000 rows because each mint re-read the ledger three times (`resolve`, `row_by_id` in the suffix loop, then the uniqueness scan) and ran `require_ready` twice.

---

## Compounding-chain cut (after the numbers)

Cut: one `require_ready` and one `read_ledger` per `mint`. Live lookup walks that in-memory list. Suffix collision uses an id set. Public `resolve` / `row_by_id` still hit disk once each when called from outside.

Not cut (fail-closed tax, not the chain):
- 19 volume `is_file` checks inside `require_ready`
- card plaintext fields
- window marker list
- PUI / empty-lemma / speech / PDF-magic guards

### Numbers after the cut

| Metric | Before | After |
|---|---|---|
| `read_ledger` per first mint | 3 | 1 |
| `require_ready` per first mint | 2 | 1 |
| 1 new lemma | 0.4956 ms | 0.2883 ms |
| 100 new lemmas | 0.577 ms each | 0.2804 ms each |
| 1000 new lemmas | 2292.4305 ms (2.2924 ms each) | 959.9783 ms (0.96 ms each) |
| remint x100 | 31.4264 ms | 16.9075 ms |

FACT. 1000-mint wall clock dropped from 2292.4305 ms to 959.9783 ms on this computer.
FACT. 15 tests still OK after the cut (`unittest discover`).
FACT. CDI skill absent. Committed ledger still the seed Jessica row.

**INFERENCE.** Each mint still reads the whole ledger once, so cost still grows with n. Caching `require_ready` across calls would skip a missing volume mid-session. That is not a compounding cut. It is a fail-closed hole. Left alone.

---

## What this is not

- Not Alpha. No `ALPHA.md`.
- Not a novelty 90. Stay is not a 90.
- Not a CDI install.
- Not an unprofiled micro-cut (no regex rewrite, no volume rewrite, no card field drop).

---

## Verification

```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/OPTIMIZE.md').read().lower(); assert 'bytes' in t or 'ms' in t or 'count' in t; print('OPTIMIZE_OK')"
```

Do not start Alpha.

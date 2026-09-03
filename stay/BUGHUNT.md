# BUGHUNT.md — Stay Stage 11.1

Run: `stay-20260902`
Seat: Kiln. Stage 11 Bug hunt only. 2026-09-02 PT.
Happy path is Stage 10 (13 tests OK). This file is hunt: extra fixtures Stage 10 did not treat as pass criteria.
Do not skip to Break. Gauge does not run Break yet. CDI uninstalled. No git-commit.

---

## Coverage plan

| Surface | Happy path already | Extra this hunt |
|---|---|---|
| Hook events | unknown event names do not mint | valid event + speech-shaped text + lemma kwargs |
| Mentions | backticks/fences/quotes | mention text with genus/lemma kwargs (should still not mint) |
| Mint/resolve | first USE / remint live | empty lemma; two suffixes then resolve-without-suffix |
| Ingest | extract then mint; distinctive raw bytes | printable SSN-shaped claim; PDF magic in printable run |
| PUI | none in Stage 10 | scan committed stay/ tree; runtime gloss |
| Paint | pool return | (not re-hunted; 9.3 green) |
| Tickets | missing / not reversible | (not re-hunted; 9.12 green) |
| Disable | schema.disable refused | (not re-hunted; 9.7 green) |

Fixtures ran on `fixture_root()` so the committed ledger stayed one seed row.

---

## Findings (severity, root cause)

### B1 — empty lemma mints `Name//x-6148` — HIGH

**Symptom.** `use("Name", "", root=root)` succeeds. Id is `Name//x-6148` (empty Lemma slot). `id.count("/")==2` still holds so 9.1 uniqueness does not catch it.

**Root cause.** `stay.hook.mint` rejects `/` in lemma and suffix. It does not reject empty lemma or empty suffix. `_make_suffix` falls back to `x` for the suffix initial when lemma is empty, so the row looks well-formed.

**Coverage gap.** Stage 9.1 asserts two slashes, not three non-empty parts. `_parts` requires non-empty parts when reading a card, but mint does not.

**Disposition.** Open. Break should try to inject a card for `Name//x-6148`. Fix is fail-closed on empty lemma/suffix at mint. Not patched this stage.

### B2 — claim-commit event trusts caller, not text shape — MEDIUM

**Symptom.** `handle("memory-write", text="hello there", genus="Name", lemma="SpeechLeak")` mints.

**Root cause.** Speech-only is implemented as "event not in HOOK_EVENTS". Con 10 said ordinary speech without identity, arithmetic or quantities is not a mint. The hook does not parse text for those shapes. A seat that fires a legal event on small talk still mints.

**Coverage gap.** `test_hook_events.py` only sends illegal event *names* (`speech`, `chat`, `talk`, `token`).

**Disposition.** Open. Named as operator/API hazard. Not a mention-spoof. Break can try small-talk on `memory-write`.

### B3 — resolve-without-suffix returns the first live row — LOW (documented)

**Symptom.** Two `Name/Alex` suffixes; `resolve("Name","Alex")` returns the first live id.

**Root cause.** `resolve` walks the ledger in file order and returns the first non-superseded genus+lemma match. GATES.md already says this.

**Disposition.** Accepted for now. Con 17 (who supersedes) is the live-card authority, not "latest suffix wins."

### B4 — ingest copies SSN-shaped claim text into card gloss — HIGH (con 13)

**Symptom.** `ingest("SSN 123-45-6789 for Pat", "chat", "Name", "PatProbe")` puts `SSN 123-45-6789 for Pat` in the card gloss.

**Root cause.** `extract` has no PUI filter. `ingest` uses `claims[0]["text"][:48]` as gloss. Con 13 AVOID is "no patient names, SSN or charts" in volumes/ledger/cards/tickets. Runtime cards are in scope of that AVOID. Committed files on disk this hunt have no such strings (see 11.2).

**Disposition.** Open. 11.2 scans committed files only. Break should try PUI through the ingest door. Do not treat 11.2 PASS as "ingest cannot leak."

### B5 — mention + kwargs does not mint — PASS (extra)

**Symptom.** `handle("identity", text="\`Jessica\`", genus="Name", lemma="Jessica")` returns None. No extra ledger row.

**Root cause.** `is_mention` runs before `use`. This extra fixture holds.

### B6 — PDF magic survives extract as claim text — MEDIUM

**Symptom.** `extract(b"%PDF-1.4\\nJessica neighbor\\n\\x00\\xff", "pdf")` yields claim text `%PDF-1.4 Jessica neighbor`.

**Root cause.** `extract` keeps printable runs of length >= 3. `%PDF-1.4` is printable. `_assert_no_raw` looks for the raw blob in ledger/volumes, not for magic strings inside claim text.

**Disposition.** Open. Raw bytes did not enter ledger in this fixture. Header text did enter the claim list.

---

## Severity rollup

| id | severity | open? |
|---|---|---|
| B1 empty lemma | HIGH | yes |
| B2 event-not-text | MEDIUM | yes |
| B3 first-live resolve | LOW | accepted |
| B4 PUI in gloss | HIGH | yes |
| B5 mention+kwargs | n/a | pass |
| B6 PDF magic in extract | MEDIUM | yes |

No CRITICAL (no committed PUI, no disable switch, no CDI install, no concat session store).

---

## 11.2 PUI

Committed `stay/` scan: no `Boops`, `SSN`, `patient`, `Res#`, or `chart` hits. See `tests/test_pui_closed.py`.

Runtime ingest (B4) is a different door. Do not collapse those two.

---

## Facts vs inferences

**FACT.** Extra fixtures ran on `fixture_root()`. Committed `ledger.jsonl` still one seed `Name/Jessica/j-a3f0`.
**FACT.** Empty lemma minted `Name//x-6148`.
**FACT.** `memory-write` + "hello there" + lemma kwargs minted.
**FACT.** Committed tree PUI scan: none.
**INFERENCE.** B2 is an API-trust issue, not a mention-spoof miss.
**INFERENCE.** B4 will be the Break PUI attack that 11.2 will not catch.

---

## Verification

```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/BUGHUNT.md').read().lower(); assert 'severity' in t and 'root' in t; print('BUGHUNT_OK')"
python3 /workspace/praxis/stay-20260902/stay/tests/test_pui_closed.py
```

Do not start Break.

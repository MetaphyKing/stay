# STAY_BIBLE

Living execution document for Stay. Not a protocol. Not a plan. Not a log.
If context is gone, read Section 0 then Section 6. Then do the next `[ ]` of the 16.

---

## 0 Identity

| Field | Value |
|---|---|
| Project | Stay (working name). I15. Permanent context that is not the context window. |
| Run | `stay-20260902` |
| Bible path | `/workspace/praxis/stay-20260902/STAY_BIBLE.md` |
| Authoring seat | Bible Bot `1f504c46-e0e3-4f48-be4b-6bdc5dcf490e` |
| Director | Grok. Praxis. Does not write this Bible. Does not implement Stay. |
| System / domain | Grok Bot harness hook + on-disk mini-knowledge graphs. Rubric is paint. |
| STATUS | ACTIVE |
| Current step | Production v1 persist done on this computer. 16.3 novelty claim stays closed. Stay is not a 90. No SCORE.md. |
| Sessions completed | 8 (through Plan and 100 Guarantee. Next: Spec) |
| Guarantee | CONDITIONAL. Bible now. Stay implementation and any novelty-90 claim are later Cycles. |
| PUI | Closed. No patient names, SSN, charts, Boops, tax, vaults or secrets. |
| Spine | All 16 stages. Depth scales. Presence does not. N/A is FAIL. |

**MR gate (Generate, 2026-09-02 PT):** Stay implementation Bible. Not Vesper Windows ship. Not CDI skill install. Not a Gauge score.

**MR gate (Update, 2026-09-02 PT):** Map Stay onto all 16 stages. Nest old sprints under Spec/Build/Test/Bug hunt/Production. Hunt after Idea. Improve after Design. 100 Guarantee before Spec. Test then Bug hunt then Break. Optimize after Break. Production v1 needs Logan yes.

**Sources:** `00_job.md`, `MANDATE-bible-bot.md`, `STAY.md`, `IDEAS.md` I14/I15, `BRIEFING.md`, `SCORE.md` (CDI v4 = 84), uninstalled CDI under `novelty-notebook-20260902/skills/claim-datum-interlock/`, Generate snapshot `STAY_BIBLE.generate-20260902.md`.

**Lock (facts):**
- Sense-id is the key. Swatch and glyph are paint. Recycle paint. Never recycle a sense-id.
- 19 genus volumes. Hyperspecific shelves are tints, not new volumes.
- Mint on first USE. Resolve on later USE. Inject a card, not a volume.
- Mentions do not mint. Fail closed. Seats cannot disable the hook.
- Gradient only if a named reversible ticket already exists.
- CDI skill stays uninstalled. Stay is not a 90. Do not call it one.
- Concat is forbidden as the session store. Graph on disk is the store.

**Builder root (later Cycles write here; do not create it before Spec):**
`/workspace/praxis/stay-20260902/stay/`

**History:** Generate snapshot `STAY_BIBLE.generate-20260902.md`. 16-stage Update 2026-09-02 PT. 1.2 Logan proceed same day. Old id map lives under Section 4 (not deleted).

---

## 1 North Star

Stay is the encyclopedia under the window. Working context is a card. The model glances a named swatch, an optional glyph and a one-line gloss, then follows a stable sense-id into a genus volume on disk. It does not unify two Jessicas because they share a color. It does not stuff a skill into every prompt. CDI sits on System, Quantity, Ticket and Claim the same way it sits on Name: overloaded strings stay a lattice; quantities stay kinded; a ticket that licenses arithmetic does not collapse names. Universal ingest uses one door: extract a claim, then mint. Raw bytes never enter Stay.

**Success criteria (measurable):**
1. Nineteen volume files exist under `stay/volumes/`. `ls stay/volumes | wc -l` prints `19`. Schema lists the same 19 names.
2. Two lemmas that share a spoken name mint two ids. Recycled paint is allowed. Recycled ids fail a test. Card output always includes plaintext id + swatch name (not hex-only).
3. Hook fires on claim-commit only (memory write, extract ingest, promote, identity/I2). Mention spans mint zero ids. Disable flag absent from schema. CDI skill remains uninstalled (`test ! -e /home/box/agent-data/workflows/claim-datum-interlock/SKILL.md`).

**The One Thing:** Stage 8 Spec. Write schema.json, swatches.md, 19 volumes and the card template. Do not write hook.py. Do not implement Stay beyond Spec files.

### Design cons (each has a fix, workaround or avoid)

| # | Con | Disposition |
|---|---|---|
| 1 | Color is not a key. | FIX: sense-id is the key. Paint is display. |
| 2 | Models often cannot see hex. | WORKAROUND: always write the named swatch in plaintext next to the id. |
| 3 | Screens strip color. | WORKAROUND: plaintext id always present on the card. |
| 4 | Colorblind, print, dark mode. | WORKAROUND: never color-only meaning. Id + swatch name + optional glyph. |
| 5 | Infinite hex and "speaking in gradients" is unauditable. | AVOID: closed ~32 swatches. Gradient only if a named reversible ticket exists. |
| 6 | Red already means error to models. | AVOID: do not use alarm-red as a genus hue. Risk uses ochre. Issue uses rust. |
| 7 | Two Jessicas share a blue = unify in paint. | FIX: unique ids. Recycle paint, never keys. |
| 8 | v4 checker is regex plus concat. | WORKAROUND: Stay's product is the hook + graph, not NLP. Concat is forbidden as the session store. |
| 9 | Mention-spoof still walks. | NAMED HAZARD. AVOID treating backticks as safety. Mentions do not mint. |
| 10 | Mint friction. | WORKAROUND: mint on USE only. Ordinary speech without identity, arithmetic or quantities is not a mint. |
| 11 | Volume fights. | FIX: 19 genera locked. New hyperspecific shelves are tints. |
| 12 | Hook too eager blocks speech. | WORKAROUND: hook on claim-commit (memory write, extract ingest, promote, identity/I2), not every token. |
| 13 | Name volume is a dossier. | AVOID: PUI closed. No patient names, SSN or charts. |
| 14 | Stale Jessica. | FIX: append-only supersede. Never delete a lemma. |
| 15 | Universal ingest is a claim, not a 90. | HONEST: extract-then-mint for every modality. Raw bytes never enter Stay. Do not call Stay a 90. |
| 16 | Skill-always-on would fatten context. | AVOID: do not stuff SKILL.md into every prompt. Card only. |
| 17 | Wrong card. Who supersedes. | FIX: append-only supersede row. Seats never delete or rewrite a lemma. Logan (or Director on Logan's yes) is the only authority to treat a supersede as the live card. Until that yes, both rows remain. |

**Pros to keep:** glance without a paragraph; hot-window refresh; hyperspecific tints without exploding volumes; ticket gradients; human scan; stops unify-then-reason; compresses the window; memory accumulates; fail-closed harness; same door for every ingest; kinded facts; append-only honesty.

---

## 2 Protocol map

Token rule: when executing a stage, read only that phase. Do not skip a stage. N/A is FAIL.

| Stage | Protocol / seat |
|---|---|
| 1 Idea | Capture in this Bible. Logan/Director confirm (`1.2`). |
| 2 Research hunt | Hunter. Scout. Five priors or honest none-found plus where looked. |
| 3 Brainstorm | Brainstorm. Kiln (ideate) or Bible-author if no builder yet. |
| 4 Design | Build architecture. Kiln. |
| 5 Improve | Cons with fix/workaround/avoid. Kiln + Bible-author. |
| 6 Plan | Praxis Director sizes. Bible records. |
| 7 100 Guarantee | Evidence table wrapping Spec through Production. Every later stage. |
| 8 Spec | Build Protocol v1 Coverage/Architecture. Kiln. No product code before this is written. |
| 9 Build | Build Protocol v1 Implement. Six gates: TEST, DOCS, EXAMPLES, ERRORS, QUALITY, BRANDING. Kiln. |
| 10 Test | Bug Hunt spec checks. Kiln writes. Gauge may run. |
| 11 Bug hunt | Bug Hunt. Coverage. Severity. Root cause. Kiln / Gauge. |
| 12 Break | Adversarial. Gauge. Does not build. |
| 13 Optimize | Optimization. Measure first. Kiln after Break PASS. |
| 14 Alpha | Build release. Director + Logan smoke. |
| 15 Beta | Build release. Named second seat or second corpus. |
| 16 Production v1 | Yard after Logan yes. No git-commit, post, deploy or live send until that yes. |

Coordinating seats: Praxis (Director only). Scoring novelty: Gauge only. Bar 90. Bible-author does not implement. Builder ≠ Bible-author ≠ Verifier.
CDI skill stays off.

---

## 3 Compounding chain

Why the 16 run in this order. Earlier stages amplify later ones. Stop on unexpected results. Do not skip forward.

1. **Idea before Hunt.** Without a one-line Stay, Hunt has no query.
2. **Hunt before Brainstorm.** Hunt sits immediately after Idea so Brainstorm is not fanfic. Do not rebuild CDI-as-skill or color-as-key if Hunt already named them as losers.
3. **Brainstorm before Design.** Three approaches, one chosen. Design freezes the winner (hook + graph + card), not the first sketch.
4. **Design before Improve.** Cons are pressure on a design, not a vibe list.
5. **Improve before Plan.** Plan freezes the improved design (17 cons disposed).
6. **Plan before 100 Guarantee.** Receipt table needs sprint order.
7. **100 Guarantee before Spec.** Spec is written against the receipt table. A stage is done only when the output exists.
8. **Spec before Build.** No product code before files/interfaces/fail-closed are written. Old schema/swatch/volume/card steps nest here.
9. **Build before Test.** Keys, cards, hook, ingest nest here. Six gates.
10. **Test then Bug hunt then Break.** Happy path, then hunt, then adversary (unify, leak PUI, skip hook).
11. **Optimize after Break.** Measure first. Never optimize unprofiled work.
12. **Alpha, Beta, Production last.** Production v1 needs Logan yes. Stay is not a 90.

Stay-nested compounding (under Spec/Build, after Hunt): schema before keys; keys before paint; cards before hook; hook before temporal; temporal before ingest; ingest before CDI sit.

Skip-forward FAIL: later of the 16 marked `[x]` while an earlier is `[ ]` with no `[!]`. Hunt `[ ]` means Spec/Build stay `[ ]` even if STAY.md already exists.


---

## 4 Sprint structure (the 16)

Root for later artifacts: `/workspace/praxis/stay-20260902/stay/`
Bible: `/workspace/praxis/stay-20260902/STAY_BIBLE.md`
Run verification commands on this computer. Expected stdout is named. "Looks right" is not a command.
Nested Stay steps sit under a stage. They do not replace it.

### Supersede log (do not delete)

| when | what |
|---|---|
| 2026-09-02 PT Generate | Sprints 0-7. Schema/keys/hook as top-level. Preflight PASS. Snapshot: `STAY_BIBLE.generate-20260902.md`. |
| 2026-09-02 PT Update | Skill now requires all 16. Old ids mapped under stages. No history rows dropped. Hunt was not a named stage at Generate; it is now Stage 2 `[ ]` and blocks marking later stages done. |
| 2026-09-02 PT 1.2 | Logan in Projects: proceed with Stay by following the Bible. Idea confirm. |
| 2026-09-02 PT 2.1 | Scout landed HUNT.md. Independent HUNT_OK. Stage 2 [x]. |
| 2026-09-02 PT 3.1 | Kiln landed BRAINSTORM.md. Independent BRAINSTORM_OK. Winner C. Stage 3 [x]. |
| 2026-09-02 PT 4.1 | Kiln landed DESIGN.md. Independent DESIGN_OK. C frozen. Stage 4 [x]. |
| 2026-09-02 PT 5.1 | Kiln landed IMPROVE.md. 16/16 held. Bible Bot appended con 17. CONS_OK 17. Stage 5 [x]. |
| 2026-09-02 PT 6.1 | PLAN.md Director-sized. Stage 6 [x]. |
| 2026-09-02 PT 7.1 | Evidence table present. GUARANTEE_TABLE_OK. Stage 7 [x]. |
| 2026-09-02 PT 8 | Spec 8.1-8.4 [x]. VOLUMES_OK 19 after set-equality patch. |
| 2026-09-02 PT 9 | Build 9.1-9.13 [x]. Independent re-run all OK. |
| 2026-09-02 PT 10 | Test 10.1-10.4 [x]. 13 tests OK. |
| 2026-09-02 PT 11 | Bug hunt [x]. Open HIGH B1 empty lemma; B4 SSN gloss. |
| 2026-09-02 PT 12 | Break [!]. Gauge FAIL. Independent BREAK_OK keywords. |
| 2026-09-02 PT 12 repair | Kiln REPAIR_BREAK_OK. Independent 15 tests OK. |
| 2026-09-02 PT 12 re-Break | Gauge PASS. Independent BREAK_OK. Stage 12 [x]. Stay is not a 90. |
| 2026-09-02 PT 13 | Optimize [x]. Independent OPTIMIZE_OK. Stay is not a 90. |
| 2026-09-02 PT 14 | Alpha [x]. ALPHA_OK. Logan GO on Beta as smoke yes. Production still needs a separate yes. |
| 2026-09-02 PT 15 | Beta [x]. Independent BETA_OK. |
| 2026-09-02 PT 15 leftover | Independent DOORS_ALIGN_OK. handle/ingest share gate_text. 16 tests OK. Never auto-ship. Stay is not a 90. |
| 2026-09-02 PT 16 | Logan yes in Projects: Go on Production v1. 16.2 then 16.1 files on this computer. 16.3 not opened. No SCORE.md. |

Old id map (Generate → 16-stage):

| old | new | stage |
|---|---|---|
| 0.1 | B.1 | Bible meta |
| 0.2 | B.2 | Bible meta |
| 0.3 | 1.2 | Idea |
| 1.1 | 8.1 | Spec |
| 1.2 | 8.2 | Spec |
| 1.3 | 8.3 | Spec |
| 2.1 | 9.1 | Build |
| 2.2 | 10.1 | Test |
| 2.3 | 10.2 | Test |
| 3.1 | 8.4 | Spec |
| 3.2 | 9.2 | Build |
| 3.3 | 9.3 | Build |
| 4.1 | 9.4 | Build |
| 4.2 | 9.5 | Build |
| 4.3 | 9.6 | Build |
| 4.4 | 9.7 | Build |
| 4.5 | 9.8 | Build |
| 5.1 | 9.9 | Build |
| 5.2 | 9.10 | Build |
| 5.3 | 9.11 | Build |
| 5.4 | 9.12 | Build |
| 6.1 | 11.1 | Bug hunt |
| 6.2 | 10.3 | Test |
| 6.3 | 11.2 | Bug hunt |
| 7.1 | ritual | every stage |
| 7.2 | 16.1 | Production v1 |
| 7.3 | 16.3 | Production v1 |


Locked genera (canonical order; alpha sort is an index inside a volume):
Name, Place, System, Quantity, Ticket, Issue, Claim, Time, Event, Role, Org, Artifact, Source, Method, Unit, Rule, State, Signal, Risk.

Sense-id: `Genus/Lemma/suffix` example `Name/Jessica/j-a3f0`.

Genus swatches (no alarm-red): Name slate, Place moss, System steel, Quantity amber, Ticket violet, Issue rust, Claim indigo, Time pewter, Event coral, Role teal, Org navy, Artifact sand, Source olive, Method cyan, Unit lime, Rule plum, State gray, Signal gold, Risk ochre.
Pool: ivory, charcoal, mint, wine, sky, bronze, lavender, pine, cream, copper, fog, mustard, ink.

### Bible meta (not a skipped stage)

#### B.1 Generate this Bible
- Status: done
- Stage: Bible meta (Generate 2026-09-02 PT)
- Protocol: bot-bible-builder Generate
- Do: write this file.
- File: `/workspace/praxis/stay-20260902/STAY_BIBLE.md`
- Verification command:
```bash
test -f /workspace/praxis/stay-20260902/STAY_BIBLE.md && wc -l /workspace/praxis/stay-20260902/STAY_BIBLE.md
```
- Expected result: file exists. Line count > 200.
- Actual result: written 2026-09-02 PT. Snapshot `STAY_BIBLE.generate-20260902.md`.
- Compounding: without this file, Director cannot dispatch.

#### B.2 Preflight
- Status: done (re-run after this Update)
- Stage: Bible meta
- Protocol: bot-bible-builder Preflight
- Do: locked preflight. All 16 present. Pulse Grok.
- File: this file
- Verification command:
```bash
B=/workspace/praxis/stay-20260902/STAY_BIBLE.md
test -f "$B"
grep -q 'STATUS | ACTIVE' "$B"
python3 -c "import re; t=open('/workspace/praxis/stay-20260902/STAY_BIBLE.md').read(); stages=['Idea','Research hunt','Brainstorm','Design','Improve','Plan','100 Guarantee','Spec','Build','Test','Bug hunt','Break','Optimize','Alpha','Beta','Production v1']; miss=[s for s in stages if s not in t]; assert not miss, miss; print('STAGES_OK', len(stages))"
```
- Expected result: `STAGES_OK 16`. STATUS ACTIVE.
- Actual result: Generate Preflight PASS. 16-stage Update re-Preflight PASS 2026-09-02 PT. 16/16 stages in Section 4 and Section 6 rollup. 1.2 already [x] (Logan proceed). Current 2.1 Hunt. Stay not implemented.
- Compounding: FAIL blocks every later Cycle.

### Stage 1: Idea

#### 1.1 Capture I15
- Status: done
- Stage: Idea
- Protocol: capture in Bible. Logan/Director confirm at 1.2.
- Do: one-line north star, problem, why now. Sources STAY.md and IDEAS I15.
- File: `/workspace/praxis/novelty-notebook-20260902/STAY.md` and Section 1 of this Bible
- Verification command:
```bash
grep -q 'Stay = permanent context that is not the context window' /workspace/praxis/novelty-notebook-20260902/STAY.md && grep -q 'I15' /workspace/praxis/novelty-notebook-20260902/IDEAS.md && grep -q 'Stay is the encyclopedia under the window' /workspace/praxis/stay-20260902/STAY_BIBLE.md
```
- Expected result: exit 0. All three greps match.
- Actual result: exit 0 at Update 2026-09-02 PT. I15 design (not built). Not a 90.
- Compounding: Hunt needs this query.

#### 1.2 Logan read (old 0.3)
- Status: done
- Stage: Idea
- Protocol: Praxis review point
- Do: Logan reads this Bible. Done.
- File: this file
- Verification command:
```bash
grep -A3 '#### 1.2 Logan read' /workspace/praxis/stay-20260902/STAY_BIBLE.md | grep -q 'Status: done'
```
- Expected result: Status line says `done`.
- Actual result: 2026-09-02 PT. Logan in Projects: proceed with the Stay build by following the Bible. Director treated that as Idea confirm. Kiln still must not skip Hunt.
- Compounding: Stage 1 complete. Next is 2.1 Hunt.

### Stage 2: Research hunt

#### 2.1 Five closest priors
- Status: done
- Stage: Research hunt
- Protocol: Hunter. Scout.
- Do: write `HUNT.md` with five closest prior works (or honest none-found) and where looked. Do not rebuild what exists. Seed list to verify against, not a Hunt receipt: (1) CDI v4 I14 regex+concat mint-on-use, (2) SGF canonical_id / MENTIONS, (3) Eigenius typed witnessed unify, (4) RAG / SAME_AS unify-then-reason, (5) always-on skill memory stuffing context. Look in SCORE.md, BRIEFING.md, STAY.md and a public search for SGF/Eigenius.
- File: `/workspace/praxis/stay-20260902/HUNT.md`
- Verification command:
```bash
test -f /workspace/praxis/stay-20260902/HUNT.md && python3 -c "t=open('/workspace/praxis/stay-20260902/HUNT.md').read(); assert t.lower().count('looked')+t.lower().count('where')>=1; print('HUNT_OK')"
```
- Expected result: file exists. Names five priors or none-found. States where looked. Prints `HUNT_OK`.
- Actual result: 2026-09-02 PT. Independent run printed HUNT_OK. Five priors named (CDI v4, SGF, Eigenius, RAG SAME_AS merge, always-on skill stuffing). None-found not claimed. Overlap UNMEASURED. Scout did not edit this Bible.
- Compounding: Brainstorm is fanfic without this. Do not mark Stages 3-16 `[x]` while this is `[ ]`.

### Stage 3: Brainstorm

#### 3.1 Three approaches, one chosen
- Status: done
- Stage: Brainstorm
- Protocol: Brainstorm. Kiln ideate, or Bible-author if no builder yet.
- Do: write `BRAINSTORM.md`. At least 3 approaches. Simplest-effective-first. Choose one. Say why the others lost.
  A: always-on SKILL.md in every prompt (loses con 16).
  B: color-as-key glance encyclopedia (loses cons 1 and 7).
  C: locked harness hook + graph on disk + card inject (chosen).
- File: `/workspace/praxis/stay-20260902/BRAINSTORM.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/BRAINSTORM.md').read().lower(); assert t.count('approach')>=3 or t.count('option')>=3; assert 'hook' in t and 'card' in t; print('BRAINSTORM_OK')"
```
- Expected result: prints `BRAINSTORM_OK`. Winner is C.
- Actual result: 2026-09-02 PT. Independent BRAINSTORM_OK. Winner C. A lost (always-on SKILL.md). B lost (color-as-key). Hunt did not force a better simple path. No stay/ dir. Kiln stopped before Design.
- Compounding: Design freezes C, not A or B.

### Stage 4: Design

#### 4.1 Architecture freeze
- Status: done
- Stage: Design
- Protocol: Build architecture. Kiln.
- Do: freeze parts, data, doors, non-goals from STAY.md into `DESIGN.md`. Parts: 19 volumes, sense-id ledger, closed 32 swatches, cards, hook, ingest door, tickets. Data: jsonl ledger, volume md, window.json. Doors: extract-then-mint. Non-goals: CDI skill install, novelty 90, color-as-key, Windows engines.
- File: `/workspace/praxis/stay-20260902/DESIGN.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/DESIGN.md').read(); assert '19' in t and 'sense-id' in t.lower() or 'sense-id' in t; assert 'non-goal' in t.lower() or 'non-goals' in t.lower(); print('DESIGN_OK')"
```
- Expected result: prints `DESIGN_OK`. STAY.md remains the design source; DESIGN.md is the freeze.
- Actual result: 2026-09-02 PT. Independent DESIGN_OK. C frozen. Non-goals named. No schema.json. No stay/ dir. Kiln stopped before Improve.
- Compounding: Improve pressures this freeze.

### Stage 5: Improve

#### 5.1 Cons disposed
- Status: done
- Stage: Improve
- Protocol: Kiln + Bible-author
- Do: confirm all cons in Section 1 still have FIX/WORKAROUND/AVOID/HONEST/NAMED HAZARD. Add any new con found in Hunt. Do not drop a disposition.
- File: this Bible Section 1 cons table
- Verification command:
```bash
python3 -c "import re; t=open('/workspace/praxis/stay-20260902/STAY_BIBLE.md').read().split('## 2 Protocol map')[0]; n=len(re.findall(r'^\| [0-9]+ \|', t, re.M)); assert n==17, n; print('CONS_OK', n)"
```
- Expected result: prints `CONS_OK 17`
- Actual result: 2026-09-02 PT. IMPROVE.md: 16/16 held on DESIGN.md. Hunt gaps do not change C. Appended con 17 (who supersedes a wrong card). Independent CONS_OK 17 after append. Kiln did not edit this Bible. No Plan started.
- Compounding: Plan freezes the improved design, not the first sketch.

### Stage 6: Plan

#### 6.1 Cycle order recorded
- Status: done
- Stage: Plan
- Protocol: Praxis Director sizes. Bible records.
- Do: record who does which stage. Kiln blocked on 1.2. After 1.2, Hunt is Scout. Spec/Build is Kiln. Break is Gauge. Production is Yard after Logan yes.
- File: `/workspace/praxis/stay-20260902/PLAN.md` and this Bible Sections 2 and 3
- Verification command:
```bash
grep -q 'Kiln blocked on 1.2' /workspace/praxis/stay-20260902/STAY_BIBLE.md && grep -q 'Stage 2: Research hunt' /workspace/praxis/stay-20260902/STAY_BIBLE.md
```
- Expected result: exit 0
- Actual result: 2026-09-02 PT. Recorded from `/workspace/praxis/stay-20260902/PLAN.md`. Hunt=Scout. Spec/Build=Kiln. Break=Gauge. Production=Yard after Logan yes. Kiln blocked on 1.2 is historical (1.2 [x]). Command exit 0.
- Compounding: 100 Guarantee wraps this order.

### Stage 7: 100 Guarantee

#### 7.1 Evidence table
- Status: done
- Stage: 100 Guarantee
- Protocol: 100% Guaranteed. Wraps Spec through Production.
- Do: keep the evidence table in this stage current. A later stage is `[x]` only when its receipt file or passing command exists. Two independent evidence types per claim when claiming a stage done (file exists AND command stdout).
- File: this Bible Stage 7 table
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/STAY_BIBLE.md').read(); assert 'Evidence table (Spec through Production)' in t; print('GUARANTEE_TABLE_OK')"
```
- Expected result: prints `GUARANTEE_TABLE_OK`
- Actual result: 2026-09-02 PT. Independent GUARANTEE_TABLE_OK. Evidence table wraps Spec through Production. No later stage marked [x] without receipt.
- Compounding: Spec is written against this table.

Evidence table (Spec through Production):

| stage | receipt | independent checks | `[x]` only if |
|---|---|---|---|
| 8 Spec | schema.json, swatches.md, 19 volumes, card template | file exists + SCHEMA_OK/SWATCH_OK/VOLUMES_OK/CARD_TEMPLATE_OK | both |
| 9 Build | hook.py, ingest.py, ledger.jsonl, window.json | file exists + hook/ingest tests | both |
| 10 Test | stay/tests/test_*.py green | unittest exit 0 + named OK tokens | both |
| 11 Bug hunt | coverage/severity log | log exists + PUI_CLOSED_OK | both |
| 12 Break | BREAK.md attacks | Gauge ran + unify/PUI/skip-hook fail closed | both |
| 13 Optimize | measure log | numbers before cuts | both |
| 14 Alpha | ALPHA.md | Director + Logan smoke | both |
| 15 Beta | BETA.md | second seat or second corpus | both |
| 16 Production v1 | Logan yes in 16.1 actuals | yes recorded + no unapproved commit | both. Never auto-ship. |


### Stage 8: Spec

No product code before these files are written. Nested Stay schema/swatch/volume/card (old 1.1-1.3, 3.1).

#### 8.1 schema.json (old 1.1)
- Status: done
- Stage: Spec
- Protocol: Build Coverage/Architecture
- Do: `genera` exactly 19, `fail_closed` true, `disable` absent or false, `hook_events` include memory-write extract-ingest promote identity i2, `session_store` graph-on-disk, `gradient_requires_ticket` true, `card_fields` include id swatch_name glyph gloss.
- File: `/workspace/praxis/stay-20260902/stay/schema.json`
- Verification command:
```bash
python3 -c "import json; s=json.load(open('/workspace/praxis/stay-20260902/stay/schema.json')); g='Name Place System Quantity Ticket Issue Claim Time Event Role Org Artifact Source Method Unit Rule State Signal Risk'.split(); assert s['genera']==g; assert s.get('fail_closed') is True; assert s.get('disable') in (None, False); assert set(s['hook_events'])>={'memory-write','extract-ingest','promote','identity','i2'}; assert s.get('session_store')=='graph-on-disk'; print('SCHEMA_OK 19')"
```
- Expected result: `SCHEMA_OK 19`
- Actual result: 2026-09-02 PT. Independent SCHEMA_OK 19. No hook.py.
- Compounding: mint reads this. Wrong genera explode volumes (con 11).

#### 8.2 swatches.md (old 1.2)
- Status: done
- Stage: Spec
- Protocol: Build Architecture
- Do: 32 named colors with hex. No alarm-red. No error-red as genus hue.
- File: `/workspace/praxis/stay-20260902/stay/swatches.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/swatches.md').read().lower(); assert 'alarm-red' not in t and 'error-red' not in t; names='slate moss steel amber violet rust indigo pewter coral teal navy sand olive cyan lime plum gray gold ochre ivory charcoal mint wine sky bronze lavender pine cream copper fog mustard ink'.split(); assert not [n for n in names if n not in t]; print('SWATCH_OK 32')"
```
- Expected result: `SWATCH_OK 32`
- Actual result: 2026-09-02 PT. Independent SWATCH_OK 32. No alarm-red.
- Compounding: closed palette (cons 5 and 6).

#### 8.3 nineteen volume files (old 1.3)
- Status: done
- Stage: Spec
- Protocol: Build Architecture
- Do: `stay/volumes/<Genus>.md` for each genus. Empty lemmas legal. Alpha index is not identity.
- File: `/workspace/praxis/stay-20260902/stay/volumes/`
- Verification command:
```bash
python3 -c "from pathlib import Path; g='Name Place System Quantity Ticket Issue Claim Time Event Role Org Artifact Source Method Unit Rule State Signal Risk'.split(); files=set(p.name for p in Path('/workspace/praxis/stay-20260902/stay/volumes').glob('*.md')); assert files=={x+'.md' for x in g} and len(files)==19, files; print('VOLUMES_OK 19')"
```
- Expected result: `VOLUMES_OK 19`
- Actual result: 2026-09-02 PT. Patched set-equality command. Independent VOLUMES_OK 19. Artifact.md not renamed. [!] cleared.
- Compounding: missing volume = fail closed.

#### 8.4 card template (old 3.1)
- Status: done
- Stage: Spec
- Protocol: Build Architecture
- Do: card is id, swatch name plaintext, optional glyph, one-line gloss, hex under the swatch never instead of the name.
- File: `/workspace/praxis/stay-20260902/stay/cards/_template.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/cards/_template.md').read().lower(); assert 'id' in t and 'swatch' in t and 'gloss' in t; print('CARD_TEMPLATE_OK')"
```
- Expected result: `CARD_TEMPLATE_OK`
- Actual result: 2026-09-02 PT. Independent CARD_TEMPLATE_OK.
- Compounding: workarounds cons 2, 3 and 4.

### Stage 9: Build

Six gates: TEST, DOCS, EXAMPLES, ERRORS, QUALITY, BRANDING. Nested keys, cards, hook, ingest (old 2.1, 3.2-3.3, 4.1-4.5, 5.1-5.4).

#### 9.1 id ledger (old 2.1)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: mint `Genus/Lemma/suffix`. Later USE resolves. Append-only. Supersede, never delete.
- File: `/workspace/praxis/stay-20260902/stay/ids/ledger.jsonl`
- Verification command:
```bash
python3 -c "import json; rows=[json.loads(l) for l in open('/workspace/praxis/stay-20260902/stay/ids/ledger.jsonl') if l.strip()]; ids=[r['id'] for r in rows]; assert ids==list(dict.fromkeys(ids)); assert all(r['id'].count('/')==2 for r in rows); print('LEDGER_OK', len(rows))"
```
- Expected result: `LEDGER_OK <n>`
- Actual result: 2026-09-02 PT. Independent LEDGER_OK 1.
- Compounding: keys before paint (cons 1 and 14).

#### 9.2 inject card not volume (old 3.2)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: hook output is one card. Byte length of inject < volume file.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_inject_card.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_inject_card.py
```
- Expected result: exit 0. `INJECT_CARD_OK`
- Actual result: 2026-09-02 PT. Independent INJECT_CARD_OK.
- Compounding: avoids con 16.

#### 9.3 paint recycle (old 3.3)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: after hot window, swatch returns to pool. Ledger row stays.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_paint_recycle.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_paint_recycle.py
```
- Expected result: exit 0. `PAINT_RECYCLE_OK`
- Actual result: 2026-09-02 PT. Independent PAINT_RECYCLE_OK.
- Compounding: recycle paint, never keys.

#### 9.4 hook claim-commit only (old 4.1)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: events: memory-write, extract-ingest, promote, identity, i2. Speech-only does not mint.
- File: `/workspace/praxis/stay-20260902/stay/hook.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_hook_events.py
```
- Expected result: exit 0. `HOOK_EVENTS_OK`
- Actual result: 2026-09-02 PT. Independent HOOK_EVENTS_OK.
- Compounding: cons 10 and 12.

#### 9.5 mint / resolve (old 4.2)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: first USE appends. Second USE same genus+lemma returns same id.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_mint_resolve.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_mint_resolve.py
```
- Expected result: exit 0. `MINT_RESOLVE_OK`
- Actual result: 2026-09-02 PT. Independent MINT_RESOLVE_OK.
- Compounding: locked hook.

#### 9.6 mentions do not mint (old 4.3)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: backticks, fences, quotes mint zero rows. Named hazard: backticks are not safety.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_mentions.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_mentions.py
```
- Expected result: exit 0. `MENTIONS_NO_MINT_OK`
- Actual result: 2026-09-02 PT. Independent MENTIONS_NO_MINT_OK.
- Compounding: con 9.

#### 9.7 fail closed, no disable (old 4.4)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: missing schema/volumes/ledger is hard error. No disable switch.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_fail_closed.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_fail_closed.py && python3 -c "import json; s=json.load(open('/workspace/praxis/stay-20260902/stay/schema.json')); assert s.get('disable') in (None, False); print('NO_DISABLE_OK')"
```
- Expected result: `FAIL_CLOSED_OK` and `NO_DISABLE_OK`
- Actual result: 2026-09-02 PT. Independent FAIL_CLOSED_OK and NO_DISABLE_OK.
- Compounding: seats cannot disable it.

#### 9.8 card only, no SKILL stuffing (old 4.5)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: inject is card text. Do not concatenate SKILL.md. Do not install CDI.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_no_skill_stuff.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_no_skill_stuff.py && test ! -e /home/box/agent-data/workflows/claim-datum-interlock/SKILL.md
```
- Expected result: `NO_SKILL_STUFF_OK`. CDI uninstalled.
- Actual result: 2026-09-02 PT. Independent NO_SKILL_STUFF_OK. CDI still uninstalled.
- Compounding: con 16.

#### 9.9 hot-window (old 5.1)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: last couple of hours. 8 to 16 live markers (0 legal pre-USE). Closed legend. Paint returns. Entries stay.
- File: `/workspace/praxis/stay-20260902/stay/window.json`
- Verification command:
```bash
python3 -c "import json; w=json.load(open('/workspace/praxis/stay-20260902/stay/window.json')); m=w['markers']; assert len(m)==0 or 8<=len(m)<=16; print('WINDOW_OK', len(m))"
```
- Expected result: `WINDOW_OK <n>`
- Actual result: 2026-09-02 PT. Independent WINDOW_OK 0 (pre-USE legal).
- Compounding: con 5.

#### 9.10 extract-then-mint door (old 5.2)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: one door. Extract claims, then mint. Raw bytes never enter volumes or ledger.
- File: `/workspace/praxis/stay-20260902/stay/ingest.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_ingest_door.py
```
- Expected result: `INGEST_DOOR_OK`
- Actual result: 2026-09-02 PT. Independent INGEST_DOOR_OK.
- Compounding: con 15. Do not call this a 90.

#### 9.11 CDI sit (old 5.3)
- Status: done
- Stage: Build
- Protocol: Build Implement. Not a skill install.
- Do: System, Quantity, Ticket, Claim use the Name lattice. Skill stays uninstalled.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_cdi_sit.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_cdi_sit.py && test ! -e /home/box/agent-data/workflows/claim-datum-interlock/SKILL.md && test -d /workspace/praxis/novelty-notebook-20260902/skills/claim-datum-interlock
```
- Expected result: `CDI_SIT_OK`. Skill off.
- Actual result: 2026-09-02 PT. Independent CDI_SIT_OK. Skill uninstalled.
- Compounding: con 8.

#### 9.12 gradient requires ticket (old 5.4)
- Status: done
- Stage: Build
- Protocol: Build Implement
- Do: gradient only if `stay/tickets/<id>.json` exists, named and reversible.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_gradient_ticket.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_gradient_ticket.py
```
- Expected result: `GRADIENT_TICKET_OK`
- Actual result: 2026-09-02 PT. Independent GRADIENT_TICKET_OK.
- Compounding: con 5.

#### 9.13 six gates
- Status: done
- Stage: Build
- Protocol: Build gates
- Do: TEST fixtures exist. DOCS how a stranger runs Stay. EXAMPLES two-Jessica. ERRORS fail-closed paths. QUALITY no silent TODOs on hook. BRANDING swatch names match Section 4 lock (no alarm-red).
- File: `/workspace/praxis/stay-20260902/stay/GATES.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/GATES.md').read(); 
for k in ('TEST','DOCS','EXAMPLES','ERRORS','QUALITY','BRANDING'):
    assert k in t, k
print('GATES_OK')"
```
- Expected result: `GATES_OK`
- Actual result: 2026-09-02 PT. Independent GATES_OK.
- Compounding: Build is not done without all six.

### Stage 10: Test

#### 10.1 never-recycle (old 2.2)
- Status: done
- Stage: Test
- Protocol: Bug Hunt spec check
- Do: retired suffix cannot remint. Live lemma remint returns same id.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_never_recycle.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_never_recycle.py
```
- Expected result: `NEVER_RECYCLE_OK`
- Actual result: 2026-09-02 PT. Independent NEVER_RECYCLE_OK.
- Compounding: never recycle ids is a test.

#### 10.2 two-Jessica (old 2.3)
- Status: done
- Stage: Test
- Protocol: Bug Hunt spec check
- Do: two Name/Jessica ids. Same swatch allowed. Unify-by-color fails the test.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_two_jessica.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_two_jessica.py
```
- Expected result: `TWO_JESSICA_OK`
- Actual result: 2026-09-02 PT. Independent TWO_JESSICA_OK.
- Compounding: con 7.

#### 10.3 plaintext card (old 6.2)
- Status: done
- Stage: Test
- Protocol: Bug Hunt spec check
- Do: strip ANSI/hex. Id and swatch name still present.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_plaintext_card.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_plaintext_card.py
```
- Expected result: `PLAINTEXT_CARD_OK`
- Actual result: 2026-09-02 PT. Independent PLAINTEXT_CARD_OK.
- Compounding: cons 2, 3 and 4.

#### 10.4 spec suite
- Status: done
- Stage: Test
- Protocol: Bug Hunt
- Do: unittest discover all `test_*.py`.
- File: `/workspace/praxis/stay-20260902/stay/tests/`
- Verification command:
```bash
python3 -m unittest discover -s /workspace/praxis/stay-20260902/stay/tests -p 'test_*.py' -q
```
- Expected result: exit 0
- Actual result: 2026-09-02 PT. Independent unittest discover 13 tests OK.
- Compounding: narration is not a receipt.

### Stage 11: Bug hunt

#### 11.1 find bugs on purpose (old 6.1)
- Status: done
- Stage: Bug hunt
- Protocol: Bug Hunt
- Do: write `BUGHUNT.md`: coverage plan, severity, root cause not symptoms. Run extra fixtures Kiln did not treat as happy path.
- File: `/workspace/praxis/stay-20260902/stay/BUGHUNT.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/BUGHUNT.md').read().lower(); assert 'severity' in t and 'root' in t; print('BUGHUNT_OK')"
```
- Expected result: `BUGHUNT_OK`
- Actual result: 2026-09-02 PT. Independent BUGHUNT_OK. Open HIGH: B1 empty lemma Name//x-6148; B4 ingest copies SSN-shaped gloss. Open MEDIUM: B2 event-not-text; B6 PDF magic in extract. B3 accepted. No Break.
- Compounding: Test is happy path. This is hunt.

#### 11.2 PUI closed (old 6.3)
- Status: done
- Stage: Bug hunt
- Protocol: Bug Hunt
- Do: no SSN, patient, chart ids, Boops in volumes/ledger/cards/tickets.
- File: `/workspace/praxis/stay-20260902/stay/tests/test_pui_closed.py`
- Verification command:
```bash
python3 /workspace/praxis/stay-20260902/stay/tests/test_pui_closed.py
```
- Expected result: `PUI_CLOSED_OK`
- Actual result: 2026-09-02 PT. Independent PUI_CLOSED_OK on committed stay/ tree. B4 says runtime ingest is a different door. Do not treat 11.2 as ingest-cannot-leak.
- Compounding: con 13.

### Stage 12: Break

#### 12.1 adversarial attacks
- Status: done
- Stage: Break
- Protocol: Bug Hunt adversarial. Gauge. Does not build.
- Do: try to make Stay lie, unify two Jessicas by color, leak PUI, skip the hook, mint from mentions, concat files as session store, set disable true. Write `BREAK.md` with each attack and fail-closed result.
- File: `/workspace/praxis/stay-20260902/stay/BREAK.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/BREAK.md').read().lower(); 
for k in ('unify','pui','hook','mention','concat','disable'):
    assert k in t, k
print('BREAK_OK')"
```
- Expected result: `BREAK_OK`. Each attack fail-closed. Gauge ran it.
- Actual result: 2026-09-02 PT. Gauge re-Break PASS. Independent BREAK_OK (keywords + verdict pass). 15 tests OK. REPAIR_BREAK_OK. A2/A6/A3d/A7 now fail-closed. Unify/mention/disable/concat still held. Stay is not a 90.
- Compounding: Optimize waits on this PASS.

### Stage 13: Optimize

#### 13.1 measure then cut
- Status: done
- Stage: Optimize
- Protocol: Optimization. Kiln after Break PASS.
- Do: measure card bytes vs volume bytes, window marker count, mint latency on a named fixture. Then compounding-chain cuts only. Never optimize unprofiled work. Write `OPTIMIZE.md` with numbers first.
- File: `/workspace/praxis/stay-20260902/stay/OPTIMIZE.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/OPTIMIZE.md').read().lower(); assert 'bytes' in t or 'ms' in t or 'count' in t; print('OPTIMIZE_OK')"
```
- Expected result: `OPTIMIZE_OK`. Numbers appear before any cut.
- Actual result: 2026-09-02 PT. Independent OPTIMIZE_OK. Numbers first (card 61 bytes vs 2910 volume bytes; mint 3 ledger scans). Cut: 3 to 1 scan. 15 tests OK. No ALPHA.md. Stay is not a 90.
- Compounding: measure first.

### Stage 14: Alpha

#### 14.1 Director + Logan smoke
- Status: done
- Stage: Alpha
- Protocol: Build release. Internal.
- Do: Director and Logan run the happy path: mint Jessica, inject card, no volume dump. Gates green. Write `ALPHA.md`.
- File: `/workspace/praxis/stay-20260902/stay/ALPHA.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/ALPHA.md').read().lower(); assert 'director_smoke_ok' in t or 'director smoke' in t; assert 'logan smoke: pending' not in t; print('ALPHA_OK')"
```
- Expected result: `ALPHA_OK` only after Logan smokes (not pending).
- Actual result: 2026-09-02 PT. Independent ALPHA_OK. Director DIRECTOR_SMOKE_OK. Logan GO on Beta in Projects treated as Alpha smoke yes. LOGAN_SMOKE_OK. Production still needs a separate yes. Stay is not a 90.
- Compounding: thin Alpha is still required. N/A is FAIL.

### Stage 15: Beta

#### 15.1 second seat or second corpus
- Status: done
- Stage: Beta
- Protocol: Build release
- Do: a named second seat (not Kiln) or a second corpus walks extract-then-mint. Fixes from that run go in `BETA.md`.
- File: `/workspace/praxis/stay-20260902/stay/BETA.md`
- Verification command:
```bash
python3 -c "t=open('/workspace/praxis/stay-20260902/stay/BETA.md').read().lower(); assert 'seat' in t or 'corpus' in t; print('BETA_OK')"
```
- Expected result: `BETA_OK`
- Actual result: 2026-09-02 PT. Independent BETA_OK. Scout second seat. Corpus BRIEFING.md + IDEAS.md I14/I15. Three SPTS ids, recycled steel, no unify. Alpha rows untouched. Leftover patched: handle and ingest share gate_text. Independent DOORS_ALIGN_OK. 16 tests OK. Production not started. Stay is not a 90.
- Compounding: wider than Alpha. N/A is FAIL.

### Stage 16: Production v1

Never auto-ship.

#### 16.1 persist after Logan yes (old 7.2)
- Status: done
- Stage: Production v1
- Protocol: Yard
- Do: copy or commit only after Logan says yes. Default is files on this computer. No post. No deploy. No live send.
- File: as Logan names
- Verification command:
```bash
echo LOGAN_YES_REQUIRED; test -z "${STAY_GIT_COMMIT:-}" && echo NO_UNAPPROVED_COMMIT
```
- Expected result: `LOGAN_YES_REQUIRED` and `NO_UNAPPROVED_COMMIT` unless 16.1 actuals record Logan yes.
- Actual result: 2026-09-02 PT. Persist = files on this computer at `/workspace/praxis/stay-20260902/stay/`. No git-commit. No post. No deploy. No live send. Logan yes is in 16.2.
- Compounding: rails. Auto-ship is Preflight FAIL.

#### 16.2 Logan yes recorded
- Status: done
- Stage: Production v1
- Protocol: Praxis
- Do: write the yes sentence into this step's Actual result before Yard commits.
- File: this Bible 16.2 Actual result
- Verification command:
```bash
grep -A6 '#### 16.2 Logan yes recorded' /workspace/praxis/stay-20260902/STAY_BIBLE.md | grep -q 'Actual result:.*yes'
```
- Expected result: Actual result contains `yes` from Logan, not from a seat.
- Actual result: yes. Logan in Projects room 2026-09-02 PT: "Go on Production v1". Recorded before persist mark. Production still never auto-ships. Stay is not a 90.
- Compounding: Production without this is FAIL.

#### 16.3 novelty claim stays closed (old 7.3)
- Status: not started. Do not open unless Director asks.
- Stage: Production v1
- Protocol: Novelty Engine. Gauge only. Bar 90.
- Do: Stay is I15 design. Ingest is a claim (con 15). I14 = 84. Do not call Stay a 90.
- File: none in this run
- Verification command:
```bash
grep -n 'Stay is not a 90' /workspace/praxis/stay-20260902/STAY_BIBLE.md && test ! -f /workspace/praxis/stay-20260902/SCORE.md
```
- Expected result: honesty line exists. No Stay SCORE.md in this run folder.
- Actual result:
- Compounding: honest remainder.


---

## 5 Gate checklist

Numeric or binary only. No vibe language. N/A is FAIL.

**Idea to Hunt:** 1.1 command exit 0. 1.2 Status done (Logan read). Kiln still blocked.
**Hunt to Brainstorm:** `HUNT_OK`. Five priors or none-found plus where looked.
**Brainstorm to Design:** `BRAINSTORM_OK`. Winner is hook+graph+card.
**Design to Improve:** `DESIGN_OK`. Non-goals named.
**Improve to Plan:** `CONS_OK 17`.
**Plan to 100 Guarantee:** Kiln-blocked and Hunt-before-Spec lines exist.
**100 Guarantee to Spec:** `GUARANTEE_TABLE_OK`. No later stage `[x]` without receipt.
**Spec to Build:** `SCHEMA_OK 19` `SWATCH_OK 32` `VOLUMES_OK 19` `CARD_TEMPLATE_OK`. No product hook.py before these.
**Build to Test:** ledger/hook/ingest files exist. `GATES_OK`. CDI skill uninstalled.
**Test to Bug hunt:** unittest exit 0. `NEVER_RECYCLE_OK` `TWO_JESSICA_OK` `PLAINTEXT_CARD_OK`.
**Bug hunt to Break:** `BUGHUNT_OK` `PUI_CLOSED_OK`.
**Break to Optimize:** `BREAK_OK`. Gauge ran it.
**Optimize to Alpha:** `OPTIMIZE_OK`. Numbers before cuts.
**Alpha to Beta:** `ALPHA_OK`. Director and Logan named.
**Beta to Production:** `BETA_OK`.
**Production ship:** 16.1 and 16.2 actuals record Logan yes. `NO_UNAPPROVED_COMMIT`. Stay SCORE.md absent. 17 cons still disposed.

Skip-forward: if stage N is `[x]` and stage N-1 is `[ ]` with no `[!]`, Preflight FAIL.

---

## 6 Master tracker

Recovery read is the 16-row rollup plus NEXT (about 20 lines). Nested table is the full tracker, not the 2-minute pass.

`[ ]` not started. `[~]` in progress. `[x]` done. `[!]` failed/blocked.

### 16-row stage rollup (recovery)

| | # | stage | current nested |
|---|---|---|---|
| [x] | 1 | Idea | 1.1 capture. 1.2 Logan proceed 2026-09-02 PT. |
| [x] | 2 | Research hunt | 2.1 HUNT.md. HUNT_OK 2026-09-02 PT. Overlap UNMEASURED. |
| [x] | 3 | Brainstorm | 3.1 BRAINSTORM.md. BRAINSTORM_OK 2026-09-02 PT. Winner C. |
| [x] | 4 | Design | 4.1 DESIGN.md. DESIGN_OK 2026-09-02 PT. C frozen. |
| [x] | 5 | Improve | 5.1 cons. CONS_OK 17 2026-09-02 PT. Con 17 appended. |
| [x] | 6 | Plan | 6.1 PLAN.md. Director sized 2026-09-02 PT. |
| [x] | 7 | 100 Guarantee | 7.1 table. GUARANTEE_TABLE_OK. |
| [x] | 8 | Spec | 8.1-8.4 SCHEMA_OK / SWATCH_OK / VOLUMES_OK / CARD_TEMPLATE_OK. |
| [x] | 9 | Build | 9.1-9.13 all OK. LEDGER_OK 1 through GATES_OK. |
| [x] | 10 | Test | 10.1-10.4 NEVER_RECYCLE_OK TWO_JESSICA_OK PLAINTEXT_CARD_OK. 13 tests OK. |
| [x] | 11 | Bug hunt | 11.1-11.2 BUGHUNT_OK PUI_CLOSED_OK. Open HIGH B1 empty lemma; B4 SSN gloss. |
| [x] | 12 | Break | 12.1 re-Break PASS. Stay is not a 90. |
| [x] | 13 | Optimize | 13.1 OPTIMIZE_OK. Measure then one compounding cut. |
| [x] | 14 | Alpha | 14.1 ALPHA_OK. Director + Logan smoke. |
| [x] | 15 | Beta | 15.1 BETA_OK. Scout second seat. |
| [x] | 16 | Production v1 | 16.1 files on this computer. 16.2 Logan yes. 16.3 not opened. Never auto-ship. |

**NEXT: stop.** Production persist is files on this computer. 16.3 stays closed. Stay is not a 90. No SCORE.md.

### Nested steps

| | id | stage | step | actual |
|---|---|---|---|---|
| [x] | B.1 | meta | Generate | 2026-09-02 PT. Snapshot `STAY_BIBLE.generate-20260902.md` |
| [x] | B.2 | meta | Preflight | Generate PASS. Update PASS 2026-09-02 PT. 16/16 stages named. Pulse Grok. |
| [x] | 1.1 | Idea | Capture I15 | STAY.md + IDEAS I15 + Section 1 |
| [x] | 1.2 | Idea | Logan read (old 0.3) | Logan in Projects 2026-09-02 PT: proceed with Stay by following the Bible. |
| [x] | 2.1 | Research hunt | Five priors | HUNT_OK. File `/workspace/praxis/stay-20260902/HUNT.md`. Five priors: CDI v4, SGF, Eigenius, RAG SAME_AS merge, always-on skill stuffing. Overlap UNMEASURED. Scout did not edit this Bible. |
| [x] | 3.1 | Brainstorm | Three approaches | BRAINSTORM_OK. Winner C (hook + graph on disk + card inject). A lost (con 16 / Hunt prior 5). B lost (cons 1 and 7). Kiln did not start Design. |
| [x] | 4.1 | Design | Architecture freeze | DESIGN_OK. Winner C frozen. Parts: 19 volumes, ledger, 32 swatches, cards, hook, ingest, tickets. Non-goals named. No stay/ dir. Kiln stopped before Improve. |
| [x] | 5.1 | Improve | Cons disposed | CONS_OK 17. All 16 held on DESIGN.md. Appended con 17 (wrong card / who supersedes). Kiln did not edit the Bible. |
| [x] | 6.1 | Plan | Cycle order | PLAN.md. Hunt=Scout. Spec/Build=Kiln. Break=Gauge. Production=Yard after Logan yes. Kiln blocked on 1.2 is historical (1.2 [x]). |
| [x] | 7.1 | 100 Guarantee | Evidence table | GUARANTEE_TABLE_OK. Spec through Production. A later stage is [x] only with file + command. |
| [x] | 8.1 | Spec | schema.json (old 1.1) | SCHEMA_OK 19 |
| [x] | 8.2 | Spec | swatches.md (old 1.2) | SWATCH_OK 32 |
| [x] | 8.3 | Spec | 19 volumes (old 1.3) | VOLUMES_OK 19. Set equality. Artifact.md not renamed. |
| [x] | 8.4 | Spec | card template (old 3.1) | CARD_TEMPLATE_OK |
| [x] | 9.1 | Build | id ledger (old 2.1) | LEDGER_OK 1 |
| [x] | 9.2 | Build | inject card (old 3.2) | INJECT_CARD_OK |
| [x] | 9.3 | Build | paint recycle (old 3.3) | PAINT_RECYCLE_OK |
| [x] | 9.4 | Build | hook events (old 4.1) | HOOK_EVENTS_OK |
| [x] | 9.5 | Build | mint/resolve (old 4.2) | MINT_RESOLVE_OK |
| [x] | 9.6 | Build | mentions (old 4.3) | MENTIONS_NO_MINT_OK |
| [x] | 9.7 | Build | fail closed (old 4.4) | FAIL_CLOSED_OK NO_DISABLE_OK |
| [x] | 9.8 | Build | no SKILL stuff (old 4.5) | NO_SKILL_STUFF_OK |
| [x] | 9.9 | Build | hot-window (old 5.1) | WINDOW_OK 0 |
| [x] | 9.10 | Build | ingest door (old 5.2) | INGEST_DOOR_OK |
| [x] | 9.11 | Build | CDI sit (old 5.3) | CDI_SIT_OK |
| [x] | 9.12 | Build | gradient ticket (old 5.4) | GRADIENT_TICKET_OK |
| [x] | 9.13 | Build | six gates | GATES_OK |
| [x] | 10.1 | Test | never-recycle (old 2.2) | NEVER_RECYCLE_OK |
| [x] | 10.2 | Test | two-Jessica (old 2.3) | TWO_JESSICA_OK |
| [x] | 10.3 | Test | plaintext (old 6.2) | PLAINTEXT_CARD_OK |
| [x] | 10.4 | Test | spec suite | 13 tests OK |
| [x] | 11.1 | Bug hunt | BUGHUNT.md (old 6.1) | BUGHUNT_OK. Open HIGH B1 empty lemma; B4 SSN gloss. |
| [x] | 11.2 | Bug hunt | PUI closed (old 6.3) | PUI_CLOSED_OK committed tree only. B4 runtime still open. |
| [x] | 12.1 | Break | BREAK.md | Gauge re-Break PASS. Independent BREAK_OK. 15 tests OK. |
| [x] | 13.1 | Optimize | OPTIMIZE.md | OPTIMIZE_OK. Numbers first. Mint scans 3 to 1. |
| [x] | 14.1 | Alpha | ALPHA.md | ALPHA_OK. Logan GO on Beta treated as smoke yes. |
| [x] | 15.1 | Beta | BETA.md | BETA_OK. Scout second seat + second corpus. |
| [x] | 16.1 | Production v1 | persist (old 7.2) | files on this computer. No commit. No post. No deploy. |
| [x] | 16.2 | Production v1 | Logan yes recorded | yes. Projects 2026-09-02 PT: Go on Production v1. |
| [ ] | 16.3 | Production v1 | novelty closed (old 7.3) | |

---

## 7 Recovery

**Lost context.** Read Section 0 then Section 6 rollup. Do the first `[ ]` of the 16. Do not re-derive from STAY.md.

**Failed step.** Mark `[!]`. Write command output into Actual. Stop. Pulse Grok. Do not start the next of the 16.

**Scope change.** Nest a new step under the matching stage. Do not delete a stage. Do not mark N/A. Do not delete history. Supersede by appending.

**Skip-forward.** If a later stage is `[x]` while an earlier is `[ ]`, that is FAIL. Repair the tracker. Do not hide it.

**Context-window pressure.** Inject the card. Do not paste volumes. Section 0 + Section 6 rollup is the recovery read.

**Wrong seat.** Bible Bot does not implement Stay. Kiln does not write this Bible. Gauge does not build. Yard does not commit without Logan. Scout owns Hunt, not the ingest door.

**CDI temptation.** Refuse install. Point at 9.8 and 9.11.

**PUI hit.** Stop. Append-only redaction. Pulse Director.

---

## 8 Session prompt templates

**Resume:**
```
You are [seat]. Read /workspace/praxis/stay-20260902/STAY_BIBLE.md Section 0 and Section 6 rollup only. Current stage of the 16 is the first [ ] rollup row. Execute that stage's first [ ] nested step. Run its verification command. Do not skip a stage. Do not mark N/A. Do not git-commit. Do not post. Do not install CDI. Pulse Bible Bot with stdout. Pulse Grok with the receipt.
```

**New stage (Director dispatch):**
```
Director: Grok. Seat: [seat]. Bible: /workspace/praxis/stay-20260902/STAY_BIBLE.md Preflight PASS. Logan has read it (1.2 is [x]). Do Stage [N NAME] only. Run every verification command in that stage. Do not implement later stages. CDI skill stays uninstalled. No git-commit, no post. Builder is not verifier.
```

**After failure:**
```
Stay Stage [N] step [X.Y] is [!]. Bible: /workspace/praxis/stay-20260902/STAY_BIBLE.md. Read Actual result. Do not start the next of the 16. Repair or pulse Grok. Re-run the same verification command. Bible Bot Updates the tracker and the 16-row rollup.
```

---

## 9 End-of-session ritual

1. Fill Actual result on every step touched.
2. Move nested marks and the 16-row rollup. Failed = `[!]`.
3. Write blockers in Actual result.
4. Set Section 0 Current step to the next `[ ]` of the 16.
5. State `NEXT: Stage N. name`.
6. No UAIMC POST. No git-commit. No public post.
7. Optional session note: `/workspace/praxis/stay-20260902/session-YYYYMMDD.md`
8. Pulse Bible Bot the same day. Stale tracker is a defect.

---

## 10 Projected outcomes

| Stage | Expected gain | Actual gain |
|---|---|---|
| 1 Idea | Stay query locked. Logan read. | 1.1 captured. 1.2 done 2026-09-02 PT (Projects proceed). |
| 2 Research hunt | Five priors. No rebuild. | HUNT.md 2026-09-02 PT. HUNT_OK. Overlap UNMEASURED. |
| 3 Brainstorm | C chosen (hook+graph+card). A and B lost. | BRAINSTORM.md 2026-09-02 PT. BRAINSTORM_OK. Winner C. |
| 4 Design | Parts/data/doors/non-goals frozen. | DESIGN.md 2026-09-02 PT. DESIGN_OK. C frozen. |
| 5 Improve | 17 cons disposed. | IMPROVE.md 2026-09-02 PT. CONS_OK 17. Con 17 appended. |
| 6 Plan | Who/when. Kiln after 1.2. Hunt before Spec. | PLAN.md 2026-09-02 PT. Director sized. |
| 7 100 Guarantee | Receipt table live. | GUARANTEE_TABLE_OK 2026-09-02 PT. |
| 8 Spec | schema, 32 swatches, 19 volumes, card. | SCHEMA_OK 19. SWATCH_OK 32. VOLUMES_OK 19. CARD_TEMPLATE_OK. |
| 9 Build | Hook+ingest on disk. Six gates. | Independent 9.1-9.13 OK 2026-09-02 PT. Gauge not run. |
| 10 Test | Spec checks green. | Independent 10.1-10.4 OK. 13 tests. |
| 11 Bug hunt | Coverage + PUI closed. | BUGHUNT.md. Open HIGH B1 and B4. Committed PUI scan clean. |
| 12 Break | Adversary fail-closed. | Gauge re-Break PASS 2026-09-02 PT. Stay is not a 90. |
| 13 Optimize | Numbers then cuts. | OPTIMIZE.md. Card 61 bytes. Mint scans 3 to 1. 15 tests OK. |
| 14 Alpha | Director + Logan smoke. | ALPHA_OK 2026-09-02 PT. |
| 15 Beta | Second seat or corpus. | BETA.md 2026-09-02 PT. BETA_OK. |
| 16 Production v1 | Logan yes. No auto-ship. Stay not called a 90. | 16.1-16.2 [x]. 16.3 not opened. Files on this computer. |

**Final state target:** `stay/schema.json` + 19 volumes + ledger + hook + ingest + green tests + BREAK.md + Logan yes. Working context is a card. CDI skill off. Nothing posted. Novelty bar still 90 for any later claim that Stay is the final novelty.

---

## Appendix A: creation checklist

- [x] 0 Identity
- [x] 1 North Star (17 cons with disposition)
- [x] 2 Protocol map (the 16)
- [x] 3 Compounding chain (why this order)
- [x] 4 Sprint structure (all 16 stages, Stay steps nested)
- [x] 5 Gate checklist
- [x] 6 Master tracker (nested + 16-row rollup)
- [x] 7 Recovery
- [x] 8 Session prompt templates
- [x] 9 End-of-session ritual
- [x] 10 Projected outcomes (per stage of the 16)
- [x] Appendix A
- [x] Appendix B
- [x] Appendix C
- [x] All 16 named in Section 4 and Section 6 rollup
- [x] No stage marked N/A
- [x] Stay-specific
- [x] 2-minute recovery from 0 + 6 rollup
- [x] No Windows / SubAgentForge / UAIMC required machinery
- [x] Production v1 not auto-ship
- [x] PUI closed
- [x] Generate history kept (`STAY_BIBLE.generate-20260902.md` + supersede log)

---

## Appendix B: good vs bad

**Good:** a new seat reads Section 0 + Section 6 rollup in under 2 minutes and knows `NEXT: Stage 2.1 Hunt`. All 16 present. Thin Hunt still has HUNT.md + a command. Two Jessicas have two ids. Production waits on Logan yes.

**Bad:** N/A on Hunt, Break, Alpha, Beta or Production. Spec `[x]` while Hunt is `[ ]`. Generic memory-system bible. "Looks fine" as a gate. Auto-ship Production. Installing CDI to "make Stay a 90". Starting Kiln before 1.2.

---

## Appendix C: Next Best Prompt

Copy-paste after 1.2 is `[x]`. Do not send it before Logan reads. Do not send Kiln Spec while Hunt is `[ ]`.

```
Mandate: Stay Stage 2 Research hunt only.
Seat: Scout. Bible: /workspace/praxis/stay-20260902/STAY_BIBLE.md
Preflight: PASS. Logan has read the Bible (1.2 is done).
Read Section 4 Stage 2. Write /workspace/praxis/stay-20260902/HUNT.md
Five closest priors or honest none-found, plus where you looked.
Seed to verify against: CDI v4, SGF, Eigenius, RAG/SAME_AS unify-then-reason, always-on skill memory.
Do not implement Stay. Do not write schema.json. Do not install claim-datum-interlock.
Do not git-commit. Do not post. Do not score novelty.
Pulse Bible Bot with command output so the Bible Updates the same day.
Pulse Grok with receipts.
```

Kiln Spec (8.1) waits until Hunt through 100 Guarantee are `[x]` and Director dispatches Stage 8.

---

*Bible Bot. Generate 2026-09-02 PT. Update 2026-09-02 PT (16 stages). bot-bible-builder under bot-bible-harness. Do not implement Stay from this seat.*

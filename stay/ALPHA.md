# ALPHA.md — Stay Stage 14.1

Director smoke: 2026-09-02 PT. Grok. Live tree `/workspace/praxis/stay-20260902/stay`.
Logan smoke: yes. 2026-09-02 PT. Director treated Logan GO on Beta in Projects as Alpha smoke yes. Cards above accepted. LOGAN_SMOKE_OK.

## Happy path (Director)

Mint two Jessicas, inject cards, no volume dump.

```
A Name/Jessica/j-a3f0
id: Name/Jessica/j-a3f0
swatch: slate
gloss: Temecula case-manager

B Name/Jessica/j-b7c1
id: Name/Jessica/j-b7c1
swatch: slate
gloss: Ponte front desk
```

- Card 75 bytes < Name.md 152. Not a volume dump.
- Same slate. Two ids. Did not unify.
- `handle(memory-write, "hello there")` returned None. No SpeechLeak.
- Gates still green from Optimize: 15 tests OK after cut.
- CDI uninstalled. No git-commit.

Stdout: DIRECTOR_SMOKE_OK

## Logan

Logan GO on Beta in Projects. Director treated that as Alpha smoke yes. The two-Jessica cards above are enough. Production still needs a separate yes. Stay is not a 90.

Stdout: LOGAN_SMOKE_OK

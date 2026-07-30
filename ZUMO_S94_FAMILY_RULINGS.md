# S94 — callout family rulings ledger

All 104 blocks from the 23 unnamed schemes, plus the corrections found along the way.
**Source of every number: `lesson_inventory --json`, entities decoded, parsed not grepped.**

| Scheme(s) | paint | blk | Family | ruled by | why |
|---|---|---|---|---|---|
| 1 | `#eafaf1/#27ae60` | 19 | **INSIGHT** | DJ, S94 | 19 payoff blocks were dressed as CHECKPOINT in success-green |
| 2, 11, 12 | `#e8f3ec/#3a7d5c +2` | 18 | **TRY THIS** | DJ, S94 | TRY IT + TRY THIS + BREAK IT ON PURPOSE folded to one name |
| 18 + 8 | `#f0f7f0/#3a7d5c, #f5eef8/#6c757d` | 5 | **THINK ABOUT IT** | DJ, S94 | PREDICT FIRST + 'Ask yourself'; NOT Brain Check (would fail 3 gates) |
| 6, 13 | `#e3f2ed/#3d8b6e, #e7f1fb/#2e86ab` | 9 | **IF YOU'RE STUCK** | DJ, S94 | roster family that had zero blocks; Maker-rescue blocks |
| 9, 19 | `#ede7e1/#7d6b5e, #ede7f6/#7e57c2` | 4 | **WHERE THIS GOES** | DJ, S94 | NEXT LESSON / WHAT'S NEXT point forward in the book |
| 4 | `#fff/#2e86ab` | 10 | **KEY TERM** | DJ, S94 | IMU/Gyroscope/Bias definitions; fold in, do not rename the family |
| 3, 7 | `#e8f5e9/#3a7d5c, #eef7f1/#3a7d5c` | 19 | **STILL GREEN *(name pending)*** | proposed | byte-count reports; SUCCESS rejected - 8 CHECKPOINT blocks already say SUCCESS |
| 5 | `#eef4f8/#2e86ab` | 9 | ***not a family*** | Claude, S94 | challenge-card Work in / Where to look; §7.2 supporting marks already cover it |
| 17, 14, 15 | `#f8d7da/#c0392b, #fdecea/#c0392b, #fff8e1/#ffb300` | 4 | **WARNING** | DJ, S94 | ALWAYS STOP YOUR MOTORS + 3 orphans; retires #c0392b and #ffb300 |
| 10a, 22 | `#fffde7/#fbc02d, none/#ccc` | 2 | **EXPLANATION** | proposed | roster family at zero blocks |
| 10b | `#fffde7/#fbc02d` | 1 | **TIP** | proposed | semicolon debugging rule of thumb |
| 16 | `#e0f2f4/#17a2b8` | 1 | **COMMON PITFALLS** | proposed | Butterfly Error; roster family at zero blocks |
| 20 | `#e2d5e8/#9b6a9e` | 1 | **INSIGHT** | proposed | a durable rule, not a term |
| 21, 23 | `#fff3cd/#ffc107, none/#2e86ab` | 2 | **WHAT YOU NEED** | proposed | needs a new roster row; 6 blocks across 3 glyphs |

**Total placed: 104 blocks.**

## New family rows required

- **STILL GREEN** (or BYTE CHECK) — 19 blocks, byte-count reports, L13-L16
- **TRY THIS** — 18 blocks, hands-on mini-exercises
- **THINK ABOUT IT** — 5 blocks, predict before you run
- **WHAT YOU NEED** — 6 blocks, currently on three different glyphs
- **REAL-WORLD CONNECTION** — 5 blocks, glyph 🤖, on three different schemes

## Roster families that had ZERO blocks and now have work

- **IF YOU'RE STUCK** 0 → 9 · **EXPLANATION** 0 → 3 · **COMMON PITFALLS** 0 → 1

## Corrections logged this session

1. **ENGINEER'S LOG was counted as zero blocks. It has 16.** The label carries `&rsquo;`,
   not a straight apostrophe, so the matcher missed every one. This is §24.11's lesson
   applied to my own analysis: **an entity is not the character it encodes.** Any future
   label matching must decode entities first.
2. **`lesson_inventory` v1.1.0 → v1.1.1** — visible-banner expectation corrected 2 → 1
   (stale since S89). Control-run before and after.
3. **The 'L03/L08/L09/L10 finished-payload' queue item is a phantom.** All four lessons
   have a `finished` payload; every challenge row resolves; labels honestly read
   '(finished preload)'; and S49 already ruled C01-C06 stay finished-preload. What
   remains is a design question needing ~24 authored starters, not a defect.
4. **The '5 collisions / 121 repaints' figures from earlier in S94 are void** — computed
   before the entity fix. Must be recomputed once families are final.
5. **The book carries 51 schemes / 32 border colours for 26 roster families**, and 12 of
   the 51 are one-off, several being one-hex typos of a neighbour.

## Still open

- Final name for the 19 byte-count blocks (STILL GREEN / BYTE CHECK / other)
- LEARN vs INSIGHT share `#e3f2fd`/`#2196f3` — one must move
- KEY TERM spans three purples, one of which is MY PLAN's
- Recompute consolidation cost after families are frozen

*S94 · rulings by DJ except where marked. Nothing pushed.*
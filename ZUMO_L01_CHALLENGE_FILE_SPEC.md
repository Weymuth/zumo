# ZUMO — L01 Challenge-File Spec (drafted S53, Jul 19 2026)
### Status: **DESIGN APPROVED BY DJ · NOT BUILT** · needs a book-work session (bumps Maker + L01)

---

## The finding that started this

**L01 has ZERO Maker integration.** Verified against the live tree at S53:

- `KINDS` has **no key for lesson 1** — L02 through L16 all have registries (DISCOVERIES / CHALLENGES / BONUS); L01 has none.
- `PAYLOADS` has **no `"1"` key.**
- `Lesson_01.html` contains **zero** `newproject.html?kind=` links and **zero** "make this folder for me" bars (grep-confirmed: 0 occurrences).

Consequence in the Maker UI: selecting Lesson 1 offers only the generic default — main build plus custom copy. DJ's report — *"No Discovery or challenges. Only main and mystery sandbox"* — is accurate and is the generic fallback, not an L01-specific offering.

This is not necessarily a defect by itself: **L01 has no discoveries at all** (the discovery pattern begins at L02), and L01's challenges are mostly in-place edits to a single linear build. But it leaves L01 as the only lesson with no Maker presence.

## L01's 11 challenges (from the live file, §9)

| # | Name | Rating | Shape |
|---|------|--------|-------|
| 1 | Change the Message | EASY | edit an existing line (`display.print`) |
| 2 | Change the Beep | EASY | edit an existing value (`playFrequency` 440) |
| 3 | The Fast Flash | EASY | edit two existing values (loop count, `delay`) |
| 4 | The Prediction | EASY | edit one value (`delay(350)`→`700`) + predict first |
| 5 | Two Places at Once | MEDIUM | **adds** lines (OLED + Serial) |
| 6 | Does It Come Home? | MEDIUM | **adds** a build (drive out and back, measure the gap) |
| 7 | The Siren | — | **adds** code |
| 8 | The Pirouette | — | **adds** code |
| 9 | The Vanishing Wait | — | modify/remove |
| 10 | Create Your Own Victory Jingle | — | **adds** code |
| 11 | Add a Battery Check | — | **adds** code |

Note: Ch5 and Ch6 are the two challenges written in S33 to replace redundant ones. **Neither has ever been classroom-tested.** Ch6 seeds TRIM for L03 and detonates in L11.

---

## THE APPROVED DESIGN (DJ, S53)

**One file. All eleven challenges present, each as a commented-out block. The student uncomments a block, fixes/modifies it, tests, recomments, and moves to the next.**

Rationale (DJ): no folder-juggling on day one; the challenge sits next to the code it modifies; comment/uncomment is itself a real and teachable engineering habit.

### Design decisions taken

1. **All 11 challenges get a commented block — including Ch1–4.**
   Concern raised: Ch1–4 are *edits* to lines that already exist, so there is nothing to "uncomment."
   **DJ ruling:** ship each challenge as its own commented copy of the block it modifies, so the model is uniform across all eleven. The student uncomments Ch1's `display.print("Press A");` copy and edits *that*.

2. **File length is accepted.**
   Concern raised: a long day-one file reads as intimidating — the same *"looks like a full version, did I grab the wrong file?"* reaction DJ himself had at L04 C01.
   **DJ ruling:** not a real constraint. Mitigation retained: a hard visual divider plus a header separating the main build from the challenge zone ("everything below this line is challenges — ignore it until §9").

3. **Recomment discipline — guardrails ARE included.**
   Concern raised: forgetting to recomment leaves two challenges live at once and produces an inexplicable robot; that is a debugging lesson L01 has not earned yet.
   **DJ's position:** learner mode will be there to help.
   **Noted for the record:** student-facing learner mode does not exist yet — `tutor.html` is stale, has no L12+ content, and the AI Tutor rebuild is parked LAST in the queue. DJ's stated intent is that **every student eventually has learner-mode access for every lesson**; until that ships, the September classroom is DJ plus the book.
   **Therefore, retained as cheap insurance either way:** a `// ⚠️ RECOMMENT THIS BEFORE MOVING ON` line closing each block, plus one Coach's Tip naming the symptom ("robot doing two things at once = something is still uncommented").

### Spec summary

- One file, one folder — no folder-switching on day one
- All 11 challenges present as commented blocks
- Each block is a copy of the code it modifies (uniform model, Ch1–4 included)
- Hard visual divider + header separating main build from the challenge zone
- Each block closes with a recomment reminder
- Requires **new** `KINDS[1]` + `PAYLOADS["1"]` in the Maker (neither exists today)
- L01 §9 card text updated to describe the uncomment → fix → test → recomment workflow

### Build notes / risks

- Bumps **Maker** and **L01**; must pass the payload byte-match gate (`gate_payload_match.py` v1.3).
- Whole-template starter canon is Bible §18.3 — this file is a different animal (a main build *plus* a challenge annex), so check §18.3 before building and decide whether it needs a canon note.
- Maker `mainCpp()` auto-prepends banner + `#include <Zumo32U4.h>` + MY PLAN; stored payload bodies start at `// ===== HARDWARE OBJECTS =====`. **Chat-display rule (Bible §18.3):** when showing this file to DJ, prepend the wrapper header so what he sees matches what the Maker generates.
- `node --check` after any injection into `newproject.html`.
- Push order if SVGs are ever involved: images → Maker → lessons.

---
*Drafted S53. Nothing built. Next: S54 book-work session.*

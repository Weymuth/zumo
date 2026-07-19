# ZUMO — S55 Handoff (written at S54 close, Jul 19 · paste at top of Session 55)

**S54 was a BUILD + DESIGN session.** Eleven L01 challenge files built and compile-verified;
four hardware-verified on DJ's robot. **Nothing pushed — the repo is untouched.**

## LIVE STATE — verified by fresh clone, Jul 19, commit `1d9df1b`
Maker **v2.36** · Bible **v8.33.1** · Gate v1.3 · Harness v3.0
Lessons: L01 v03.2.7 · L02 v02.2.4 · L03 v03.4.7 · L04 v04.0.12 · L05 v04.1.9 · L06 v04.5.9 ·
L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 ·
L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.2

---

## ⭐ THE BIG REVERSAL — one-file annex ABANDONED

S53's approved design was ONE file with all 11 challenges as commented blocks
(uncomment → fix → test → recomment). **DJ killed it mid-build**, correctly:
Ch1 alone ran ~60 lines of commented instruction, and eleven of those is a wall
of comments a Lesson 1 student must scroll past to find their own program.

**REPLACED BY:** eleven separate per-challenge files, ONE shared code body,
per-challenge header block. `ZUMO_L01_CHALLENGE_FILE_SPEC.md` in the repo root
is now SUPERSEDED and should be updated or retired.

**The shared-body proof:** all eleven compile to exactly **10,208 B**. Identical
size = genuinely one body. Only the header and the `<<<` markers differ.

---

## BUILT AND VERIFIED THIS SESSION (staged, NOT pushed)

### The eleven challenge files (`L01_CHALLENGES.zip`)
Each is a complete PlatformIO project. Every one compiled TWICE — as shipped,
and again with the student's edits applied exactly as the header instructs:

| Challenge | Shipped | After student edits |
|---|---|---|
| C01 Hello, World! (5 parts) | 10,208 | 10,246 ✓ |
| C02 Change the Beep | 10,208 | 10,208 ✓ |
| C03 The Fast Flash | 10,208 | 10,208 ✓ |
| C04 The Prediction | 10,208 | 10,208 ✓ |
| C05 Two Places at Once | 10,208 | 10,262 ✓ |
| C06 Does It Come Home? | 10,208 | (no code change by design) |
| C07 The Siren | 10,208 | 10,312 ✓ |
| C08 The Pirouette | 10,208 | 10,208 ✓ |
| C09 The Vanishing Wait | 10,208 | **10,046** ✓ (deletion — smaller) |
| C10 Five-Note Signal | 10,208 | 10,260 ✓ |
| C11 Battery Check | 10,208 | 10,612 ✓ |

### Other artifacts
- **`ZUMO_NAME_WRITER/`** — teacher utility, 8,886 B. Flash once per robot before term.
- **`L01_GRAPHIC_1-19_playfrequency_anatomy.svg`** — canon 1100×850, cairosvg-QA'd at
  full and in-book size. Teaches the 3 args, ORDER MATTERS, 200 ms is a blip, and the
  background-play rule (two notes with no delay = one blip).
- **`TEACHER_NOTE_AI_tools.md`** — S40 AI ranking recorded teacher-side, NOT student-facing.
- **`CE_BENCH_TEST/`** — Close Encounters five-note test sketch (its job is done).

---

## 🔬 HARDWARE-VERIFIED BY DJ THIS SESSION
1. **Close Encounters five notes play correctly** — G4 392 / A4 440 / F4 349 / F3 175 / C4 262.
   All five audible at even volume. DJ: *"Sounded exactly like the movie."*
   → The book can ship the REAL sequence; no octave substitution needed.
2. **EEPROM name read works** (after the fix below).
3. **C02 beep now audible** at 800 ms.
4. **Volume 30 does NOT error** — compiles, uploads, makes sound. Library caps at 15.
   Undocumented above 15. → Belongs in the syntax-gap prose pass: *it compiles, it runs, it's wrong.*

---

## 🐛 TWO DEFECTS FOUND AND FIXED MID-BUILD

**1. The name printed too early to see.** Originally printed at the top of `setup()`,
in the first milliseconds after boot — the 32U4 drops its USB port on reset, so the
Serial Monitor was still reconnecting and ate it. DJ saw nothing.
**FIX:** moved the name print to immediately AFTER `Serial.println("Hello, Robot!")`,
which lands seconds later on a settled connection. Verified working.
**LESSON:** never ask a student to catch output printed before the USB port settles.

**2. The C02 beep was inaudible.** 200 ms at the top of the sequence, followed by
1,200 ms of LED blinking and a drive — students can't isolate a note they've already
stopped listening for. **FIX:** challenge file only holds it 800 ms with `delay(900)`;
main build untouched. Header explains why it differs.

---

## DESIGN DECISIONS LOCKED (DJ-approved)

- **C01 = LOCKED.** DJ: *"Great. Lock it down."* Five parts: OLED Hello World →
  Serial matches → rename to own name → Button B swap (text AND behavior) →
  find + research robot name.
- **Robot names in EEPROM at address 512**, magic byte `0x5A`, 20 chars max.
  **L16 uses addr 0** — no collision, but L16 needs an address-map note and its
  "this book has never touched it" line is now false.
- **22-name roster** (DJ's lucky number, locked): HAL 9000 · WOPR · Johnny 5 · R2-D2 ·
  C-3PO · Bishop · T-800 · The Iron Giant · Robot B9 · KITT · Optimus Prime · Wall-E ·
  EVE · Baymax · Ava · Data · Bender · Rosie · Kamelion · Asimo · Turing · Lovelace
- **The search prompt** `why would my robot be named ______?` — DJ verified on Google
  that it disambiguates Bishop/Data/Turing correctly. Difficulty tiers SCRAPPED as unnecessary.
- **Two music stories go in LESSON PROSE, not challenge headers:**
  - **§5 — Jim Reekes** (Mac startup chime; snuck it in without permission, refused to
    remove it). Web-verified. Sets up C02.
  - **§9 — Williams/Spielberg** (134,000 combinations → 350 written → 1 chosen; left
    hanging on the fifth note "like a question"). Web-verified. Sets up C10.
- **Quick Reference gets the note chart** — C4–C6 naturals + F3 175, plus pointers to
  `playNote()` named constants and `play()` melody strings, with the caution that
  `play()` runs in the background.
- **L04 C03 ruling = option (b)** — short `for` primer on the card, framed as a callback
  to L01 §5.5 (where `for` IS explained — the S53 log's "unexplained code" claim is wrong
  and must be corrected).
- **AI guidance:** §3.1 hard callout — turn OFF inline autocomplete (Copilot), with the
  real S40 incidents (`setMotorPower`, `set motorSpeed`, `@^1.3.0`). Chat AI is fine;
  autocomplete is not. Names Claude as the 2026 course-tutor choice WITH a date stamp,
  and gives the durable reason (a general chatbot doesn't know 75:1 motors, 21×8 OLED,
  shared pins 20/4). The four-way ranking stays TEACHER-SIDE.

---

## ⚠️ NOT YET BUILT — the S55 queue

1. **Maker `KINDS[1]` + `PAYLOADS["1"]`** — L01 still has ZERO Maker integration.
   Eleven `kind=` entries, one shared payload body. Bumps Maker v2.36 → v2.37.
   `node --check` after injection. **This is the piece that makes any of it reachable.**
2. **L01 §9 rewrite** — all 11 cards must match the new files. C01's card currently says
   "Change the Message," which is now Part 3 of five. **A card that disagrees with its
   file is the "false claim in prose" defect.** Add "📁 Work in:" bars (L08 pattern).
3. **§5 Reekes prose block** + **§9 Williams prose block** (both drafted in-session, approved).
4. **§3.1 AI/Copilot callout** (drafted, approved).
5. **§1 research Coach's Tip** — "How You Ask Is Part of the Answer," using Marvin /
   Shakey / Sojourner (all OFF-roster, so nobody finds their own answer). Drafted, approved.
6. **Quick Reference note chart** (scope agreed, not written).
7. **GRAPHIC 1-19 wiring** — SVG built; needs `<img>` tag in §5 + image-index row.
8. **L16 EEPROM prose fix** — "this book has never touched it" is false once L01 ships;
   add the 512+ address-map note.
9. **L04 `setLayout21x8` fix** — **L04 is the ONLY lesson of 16 missing it** (verified:
   L01=1, L02=11, L03=3, **L04=0**, L05=7 … L16=3). Book-wide canon; L04 is the outlier.
10. **L04 C03 `for` primer** + **`L04_LEARNMODE_LOG.md` correction**.
11. **Version bumps** — L01 is moderate at minimum (v03.2.7 → v03.3.0): new Maker registry,
    rewritten §9, redesigned C01, two new callouts, EEPROM read, new graphic.
12. **Gate run across all 16** + diff audit before anything ships.

---

## 🔴 CLASSROOM DEPENDENCY — Period 1 checklist item
**Every robot must be name-flashed BEFORE students open L01**, or the whole class gets
`(unnamed -- see your teacher)` on day one. Add to the handout-day row of the Teacher
Daily Grid. ~1 min/robot with `ZUMO_NAME_WRITER`.

---

## STANDING QUEUE (carried forward, untouched this session)
L04 C03 (after the primer) → C04 Edge Guard → C05 · L03_C05 Variable Speed · C06 reorder to #1 ·
whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` gate · C## labels) ·
L01 VS Code multi-root step · the 6 syntax-gap prose candidates from S53
(`=` vs `==` · three increment spellings · stray `if(...);` · `;` vs `}` · C02 display
collision · slot ambiguity) — **now plus "out-of-range values don't error."**

**BENCH (need robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS.

**IMAGE QUEUE (DJ to shoot):** L04 4.1 underside (temp stand-in live) · L04 4.3 test surface ·
rest of the 22-photo IMAGE_SHOT_LIST.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid +
syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — DJ is giving students API access, and the syllabus has no entry for the
tutor under "Where to Find Things." Still not built; `tutor.html` stale with no L12+ content.
Fall term starts Sept 8.

---
*Written S54, July 19 2026. Nothing pushed. All artifacts staged in outputs.*

---

## 🔔 LATE-SESSION ADDITIONS (after the handoff was first written)

### Beep duration: 200 ms → 800 ms, BOOK-WIDE (DJ ruling: option B)
The 200 ms acknowledgment beep was too short to evaluate — DJ changed it and could not
tell anything had happened. **All five references now say 800 ms / delay 900**, so the
book, the graphic and all eleven files agree:
- §5.5 program listing (`440, 200, 15` → `440, 800, 15`; `delay(300)` → `delay(900)`)
- §5 "Sound Is Physics" prose
- Ch2 card solution
- §10 Knowledge Check question
- GRAPHIC 1-19 worked example + duration card reworded + ORDER MATTERS example
- All 11 challenge files (shared body)
Diff-audited: 27 changed lines, all intended. Zero residual `440, 200` in L01.

### NEW §8 troubleshooting: the butterfly error (DJ hit it live)
`butterfly_recv(): programmer is not responding` / `Maybe it isn't a butterfly/AVR109
but a AVR910 device?` — DJ reports this recurring, and that a PlatformIO **Clean**
followed by re-upload clears it.

**Web-verified against Pololu docs (0J66/8.1):** resetting the board twice within 750 ms
enters bootloader mode; the bootloader **exits after 8 seconds** if it receives no
programming commands. So the double-tap reset is the mechanism; DJ's Clean workaround
works because it *buys time* for the port to re-enumerate, not because it fixes the build.

Added to L01: one table row + a teal callout teaching BOTH fixes (double-tap first,
Clean as backup) plus the port-shifting note.

⚠️ **Also found:** Pololu documents a macOS bug (10.15 Catalina) that broke this bootloader
entirely on Macs. Long superseded, but DJ's error came off a Mac (`/dev/cu.usbmodem31401`).
**If butterfly errors cluster on Macs and not Windows in the classroom, that is a pattern,
not student error.** Worth watching in September.

### C05 wording change (DJ)
Add a second forward-looking question after "Which would you trust more / why":
*"Why might the Serial Monitor be a challenge **at that point?**"* — DJ's phrasing.
Recommended (option B): remove the "only while the cable is attached" giveaway from the
prose above it so students reason it out. **NOT YET APPLIED.**

### Approved on the bench this session
C01 **LOCKED** · C02 ✓ · C03 ✓ · C04 ✓ · C05 ✓ (DJ: "Lesson 5 is great") · C10 five-note
sequence hardware-verified.
**NOT yet bench-tested:** C06 · C07 · C08 · C09 · C11 (all built and compile-verified).

⚠️ **C05 still needs the wording change applied** — the "at that point?" forward-looking
question. Approved verbally, NOT yet in the file.

### ⚠️ STAGED FILE STATUS
`Lesson_01_WIP_S54.html` is **WORK IN PROGRESS — DO NOT PUSH.** It contains only the beep
change and the butterfly callout. It does NOT yet have: §9 rewrite · the two music prose
blocks · §3.1 AI callout · §1 research Tip · Quick Reference chart · GRAPHIC 1-19 `<img>`
wiring. All of those touch the same file. **No version bump applied** — land one complete
L01 next session rather than bumping twice.

### 🆕 MY PLAN block: SUPPRESS FOR LESSON 1 (DJ ruling, option A)
**The finding:** `mainCpp()` stamps the MY PLAN pseudo-code block into EVERY generated
file for all 16 lessons. But **L01 mentions pseudocode ZERO times** (verified: L01=0,
L02=13, L03=20, L04=11, L05=10). Same defect class as the L04 C03 `for` loop and the
L03 modulo — **used before taught**.

Two further arguments that carried the ruling:
- The L01 challenge files have no plan to write ("change 440 to another number" is not a
  four-step plan). Eleven files carrying an unused planning block trains students to
  scroll past it — exactly the wrong habit before it starts mattering in L02.
- L01's program is *given*, not designed. MY PLAN asks "what should this program do, step
  by step?" — but §5.5 already decided that. The block earns its place once students make
  design decisions, i.e. L02 onward.

**FIX:** make `mainCpp()` lesson-aware so lesson 1 gets banner + `#include` only, no MY
PLAN. Mirrors the S51 precedent (per-lesson blank-starter vocab). MY PLAN debuts in L02
where pseudocode is taught. **Do this in the same pass as `KINDS[1]` / `PAYLOADS["1"]` —
both touch `mainCpp()`.**

⚠️ NOTE: the eleven staged challenge files currently INCLUDE the MY PLAN block, since they
were generated with the present wrapper. They will need regenerating after the Maker fix.

### Experiment questions added late in the session
C07 (5 questions: close notes · loop count · short delays · no delays · pitch slide) ·
C08 (5: 200/100 curve · reversed spin · "curves toward its slower track" rule check ·
200/0 pivot point · straight-line drift → plants TRIM for L03) ·
C11 (5: threshold 6000 · threshold 3000 + defend · warn-vs-refuse design ethics ·
runs-once-at-startup gap · fresh-vs-tired voltage → drive C06 again → **plants L11**).

**C10 was NOT given extra questions** — approved as-is, but candidates exist if wanted
(did anyone guess the message · does yours resolve or hang like Williams' · reverse the
five notes · try seven like Williams wanted · change only durations to isolate rhythm).

⚠️ **Watch on the bench:** C08 Q3 states "a robot curves toward its slower track" as a rule
to verify — cut if it confuses rather than confirms. C11 Q3 is a design-ethics question
with no right answer — cut if it frustrates.

### Bench status of all eleven at S54 close
**APPROVED:** C01 (LOCKED) · C02 · C03 · C04 · C05 · C07 · C08 · C09 · C10
**BUILT, NOT YET TESTED:** C06 (needs tape + ruler) · C11 (needs a tired battery pack)

---

## 📦 WHAT GOES IN GIT — corrected ruling (S54)

**Project rule stands: everything lives in the repo.** An earlier split in this session
wrongly called some artifacts "teacher-only, keep local." Corrected:

**→ REPO (all of it):**
- `L01_GRAPHIC_1-19_playfrequency_anatomy.svg` → `images/`
- `Lesson_01.html` → `lessons/` (when finished — NOT the WIP file)
- `newproject.html` (Maker) → root
- `ZUMO_NAME_WRITER/` → root. **A teacher utility still belongs in git** — it is needed on
  any machine, at the start of every term, for years. Keeping it local repeats the S45
  failure mode (data existing in exactly one place).
- `TEACHER_NOTE_AI_tools.md` → root (or folded into the resource doc once that lands in git)
- Handoffs / learnmode logs → root, as already established

**→ THE ELEVEN CHALLENGE FILES: option B (DJ ruling).**
They live in the repo as the **authored source**, and the payload gate proves the Maker
matches them — the same relationship lesson HTML already has with its payloads. (Option A,
Maker-as-sole-source, was rejected as inconsistent with how the book already works.)
⚠️ This means the gate must be extended to cover L01's challenge bodies once
`PAYLOADS["1"]` exists. Two sources for the same code is exactly the drift the gate exists
to catch — so the gate is not optional here, it is the thing that makes option B safe.

**→ NOT pushed:** `Lesson_01_WIP_S54.html` (incomplete) · `CE_BENCH_TEST/` (job done).

---

## 🛟 BACKUP POSTURE

**Git IS the backup** — GitHub + local clone + a fresh clone every session = three copies,
and history means nothing is truly lost even after a bad commit. Two habits make that real:

1. **Commit before you experiment, not after.** Uncommitted work is the only work at risk.
2. **Verify what landed.** Already Bible canon: when DJ says "pushed," verify with a FRESH
   clone and check WHICH VERSION landed, not merely that a commit exists. (S33 had two
   false-positive pushes; S45 lost version data to a corrupted LIVE.md.)

**The one gap git does not cover:** loss of account access or repo deletion. If that matters
— and for a curriculum that may eventually be sold, it reasonably might — a periodic clone
to a local drive, or a mirror to a second host, closes it. Optional, not urgent.

⚠️ **The fragile file is `newproject.html` (5.09 MB).** It is committed and therefore backed
up, but every version bump stores a full new copy, and **GitHub's web UI truncates files
above ~1 MB on rename** (S33 canon) — always rename ON DISK, never in the browser editor.
That is a handling hazard, not a backup one, but it is the file most likely to be damaged
by a routine action.

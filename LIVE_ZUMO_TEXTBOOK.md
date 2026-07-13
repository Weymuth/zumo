# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 13, 2026 (Session 32 close)
**Status:** 🌐 **THE SITE IS LIVE** · 📗 **16-LESSON BOOK — CODE-COMPLETE (16/16 BUILT)** · L01 v03.1.0 · L02 v02.0.28 · L03 v03.0.10 · L04 v04.0.2 · L05 v04.1.2 · L06 v04.5.0 · L07 v04.3.0 · L08 v04.1.0 · L09 v05.0.0 · L10 v02.1.0 · L11 v02.0.1 · L12 "Wheels Lie" v01.0.0 · L13 "Rescue Zone: Flying on Instruments" v02.0.0 · L14 "Competition Prep" v02.0.0 · L15 "The Present Isn't Enough" v02.0.0 · **L16 "Nothing Left to Take Away" v02.0.0 (NEW — BUILT S32)** · Bible **v8.19** · Maker **v2.22 (STAGED)** · Gate **v1.1** · Harness **v3.0 (pio_harness.sh)** · 🎯 **PAYLOAD GATE PASSES BOOK-WIDE: 16 LESSONS, 1,225 BODIES, ZERO MISMATCHES**
**Currently working on:** SESSION 33 = (1) **push batch** (3 L16 SVGs → Maker v2.22 → Lesson_16 → rename `lessons/Lesson_16.html` — **the last dead link clears; the site is whole**), (2) **project purge** (Maker + L15 already green; L16 source + S32 handoff after the push), (3) **📓 Engineer's Log retrofit** (approved, prompts locked, prose-only), (4) T-2 cross-reference audit, (5) DJ verifies first PIO build of L15 ≈28,034.

> **Source of truth = `ZUMO_SUPER_BIBLE.md` (v8.19).** Filename is UNVERSIONED — the version lives ONLY in the Bible's internal version line. Upload this file at session start; verify internal version = **v8.19**.

---

## 🌐 THE SITE IS LIVE — `weymuth.github.io/zumo`

```
weymuth.github.io/zumo/
├── index.html        ← WELCOME SCREEN (two doors: Textbook | AI Tutor)
├── tutor.html        ← the AI Tutor (stale — rebuild LAST)
├── newproject.html   ← Project Maker (v2.22 STAGED, v2.21 live — push!)
├── timer.html
├── lessons/
│   └── Lesson_01.html … Lesson_15.html   ← STABLE FILENAMES (15 live)
│       (Lesson_16.html STAGED — push clears the LAST dead link)
└── images/           ← 101 files (+3 L16 SVGs staged)
```

**Stable-filename rule:** published lessons are `Lesson_NN.html`, version NOT in the published name. To ship a new version: overwrite `Lesson_NN.html`. Working files keep the full `v##.#.#`; in-file "Version N" = MAJOR DIGIT ONLY.

**Get lessons from GitHub, not the project:** `git clone --depth 1 https://github.com/Weymuth/zumo.git` — re-clone each batch, but **only after DJ confirms the push**. **The Maker's PAYLOADS is the canonical carrier of compiled state JSONs** (S30).

⚠️ **Gate quirk:** `gate_payload_match.py` cannot parse published `Lesson_NN.html` names — copy to `Lesson_NN_x_v01_0_0.html` before running. Proper fix queued.

---

## 📌 PUSH BATCH (ordered, blocking, NOTHING FROM S32 PUSHED)

1. **3 SVGs → images/**: `L16_GRAPHIC_16-01_three_memories.svg` · `L16_GRAPHIC_16-02_the_wall.svg` · `L16_GRAPHIC_16-03_ab_protocol.svg` (all NEW, no collisions)
2. **Maker v2.22 → Pages** (PAYLOADS['16'] 8 keys × 8 files; KINDS[16] 8 rows; DL_ALL = [2..16]; TITLES[16] = "Nothing Left to Take Away")
3. **THEN** `Lesson_16_Nothing_Left_to_Take_Away_v02_0_0.html` → upload, **rename on GitHub to `lessons/Lesson_16.html`**. **THE LAST DEAD LINK CLEARS — THE SITE IS WHOLE.**

**Add to project:** `pio_harness.sh` (v3.0 — new canon harness). `S25_harness_build.sh` is RETIRED (its 32,768 ceiling was fiction) — DJ may delete it.

---

## 🔴 PROJECT PURGE

**Already green (S32 open verified: Lesson_15 live md5 `dfe29ac4f55d`, Maker v2.21 live md5-identical, gate PASS on the live repo):**
- `newproject.html` (project copy) — the repo is the copy
- `Lesson_15_The_Present_Isnt_Enough_v02_0_0.html` — the repo is the copy

**After the S33 push lands** (safety gate: clone → Maker greps **v2.22** → `PAYLOADS['16']` = 8 keys × 8 files → `node --check` PASS → gate PASS → `lessons/Lesson_16.html` HTTP 200):
- `Lesson_15_Engineering_Showcase_v01_0_2.html` — **SPENT** (L16 built from it; prose salvaged; fantasy pres cut)
- `ZUMO_S32_HANDOFF.md` — spent

**Purge order is the INVERSE of push order. Any red → the project copy is the ONLY copy. Do not delete.**

---

## ✅ S32 — L16 "NOTHING LEFT TO TAKE AWAY" v02.0.0 (BUILT) + THE FLASH CEILING

### 🔴 THE FLASH CEILING — the session's headline instrument failure
**Real budget = 28,672 B** (32,768 − 4,096 bootloader) + **2,560 B RAM** — from `platform-atmelavr/boards/a-star32U4.json`. The S25 harness linked avr-gcc's default **fictional 32,768-byte region** — three sessions of PASS on a ceiling that does not exist on this robot. Second finding: **PlatformIO enables `-flto` by default** (verified in `platform-atmelavr/builder/frameworks/arduino.py`; DJ's platformio.ini is stock) — byte numbers must be measured with the student's flags. **Harness v3.0 (`pio_harness.sh`) is canon:** PIO-true flags + hard 28,672/2,560 asserts; `PASS` now means *fits on the robot*. Full book re-audit (PIO-true): **every lesson fits** — L07 14,380 · L12 24,534 · L13 24,902 · L14 25,640 · **L15 28,034 (638 spare)**. ⚠️ **OPEN VERIFICATION: DJ's first PlatformIO build of L15 should report ≈28,034/28,672.**

### THE ONE IDEA
**Fifteen lessons added. The sixteenth subtracts.** The capstone's code layer is not an enhancement — it is **the instrument that measures one** (full-course benchmark + EEPROM persistence + an empty socket), and the flash budget itself becomes the forcing function: the student's own enhancement will not fit until they make their own cut.

### THE LADDER (8 states × 8 files, PIO-true, negative control FAILS)
| Step | Flash | Spare |
|---|---|---|
| 1 — inherit L15 (8/8 byte-identical to `PAYLOADS['15']['finished']`) | 28,034 | 638 |
| 2 — **THE LAP**: RunMode, mode-aware showScore, hold-C-tap-A | 28,302 | 370 |
| 3 — **THE BASELINE**: RunScore, hold-A-tap-B, delta+BASE rows | 28,662 | **10** |
| 4 — **THE WALL**: +EEPROM → **RED BY DESIGN** — `overflowed by 626 bytes` | 29,298 | −626 |
| 5 — **THE TRADE**: Serial cut (−704) buys EEPROM (+636); boots ~2.5 s faster | 28,594 | 78 |
| finished — **THE SOCKET**: `ENHANCEMENT_ON` + `runEnhancement(dt)` | 28,594 | **+0** |

- **THE WALL ships as a downloadable payload** labeled "will not build — that is the lesson" (DJ: "Yes i love that") — the book's first red build no code change can cure.
- **The +0 is proven by `avr-nm`**: `runEnhancement` is **absent from the binary**, even flipped `true` with an empty body. The socket is free; only the student's ideas cost flash.
- **Sabotages b1/b2 BYTE-IDENTICAL to finished (28,594), disassembly-proven:** b1 "The Stopwatch With an Opinion" — bell tests MODE_COURSE, every course lap scores exactly 10.0 s (`or→sbiw` @0x5356) · b2 "The Robot With Amnesia" — load demands 0x15, save writes 0x16 (`cpi 0x16→0x15` @0x4d24). **The third sabotage (EEPROM.put in the driving loop) DID NOT FIT — over by 10 B**; taught as prose (§8.2 row 3 + Bonus footnote: "a full chip is a modest form of sabotage-proofing").

### CONTENT
- §3.3 = **real RoboCupJunior TDP template**, ending in **"Version 2 — If I Built the Next One"** (DJ ruling); platform stated plainly as a **preconfigured Pololu Zumo 32U4** — students document what they changed, not an invented chassis.
- §4 = the flash map (bootloader arithmetic), the **measured** subsystem audit (IMU ~2,900 · OLED ~2,600 · QTR ~2,300 · USB ~1,900 · buzzer ~1,800 · heap ~960), and EEPROM's three-memories table (**~3 ms/byte write · ~100k writes/cell · saves only in RUN_REPORT, stopped**).
- **Heap ≈960 B is NOT cuttable** — Pololu's QTR/prox libraries malloc their calibration arrays ("the rent the sensors charge").
- §7.3 = **enhancement menu, 5 doors** (compass · accelerometer · encoder confession · tether detector · IR beacon). `checkErrorLeft/Right()` + `usbPowerPresent()` moved here from taught steps — **DJ-approved reversal**, forced by the 78-byte headroom. **Buzzer ≈1,828 B = the student byte reserve, all-or-nothing** (the first playNote pays for the whole engine).
- §9 = tier-cards (Bronze/Silver/Gold), **no challenge payloads**; Silver requires a named byte trade. No 8A (capstone). §10.3 = Engineer's Log #16 ("assemble; Abstract last").

### VERIFIED
- Lesson **135,061 B · 24 pres** · 0 classes/styles/scripts · div-balanced · 0 dead anchors · 5 PART banners · stale-number sweep clean · defect-family clean · all 11 "Lesson 15" mentions verified legitimate back-refs.
- Maker **v2.22**: `node --check` PASS · PAYLOADS 2–16 · KINDS[16] 8 rows, all resolve · DL_ALL → 16 · TITLES[16].
- **Gate: PASS, 16 lessons, 1,225 bodies, ZERO mismatches** (L16 = 8 keys, 64 bodies). Control run passed first. *(Corrects the S31 record: the 14-lesson body count was **1,161**, not 1,171 — transcription error.)*
- **Bible v8.19** — 16-lesson renumber sweep (§1 filename table, §3 LESSON MAP, 8A map re-verified: **PRESENT L02–L15, ABSENT L01+L16**, tier-card example, image-phase count). Renumber only — no rule changes. *(L11 slug `Time_Lies_Distance_Doesnt` is a mechanical derivation from the title — flag if wrong.)*

### 📓 ENGINEER'S LOG RETROFIT — APPROVED, QUEUED
One 📓 callout per lesson end (§10), prose-only, TDP-section-tagged; **16 prompts locked** (L01 before-paragraph · L07 architecture diagram · L05 shared-pin tradeoff · L11 failure entry · L14 LoP procedure · L15 hill-climb record · L16 assemble + Abstract last). **Its own session, after L16 lands.** Rule: **instruments go forward (L16), documentation goes backward (L01–15)** — code edits to published lessons invalidate 384 payload bodies + the taught byte chain (L13/L14/L15 `after_step_1` are 7-8/8 byte-identical to the prior finished).

---

## S33 AGENDA

1. 🔴 **Push batch** (3 SVGs → Maker v2.22 → Lesson_16 → rename) → **purge**
2. **📓 Engineer's Log retrofit** — 16 lessons, prose-only bumps
3. **T-2 deferred audit** — cross-reference integrity + promise/keep (renumber complete)
4. Open queue · photo queue · **AI Tutor rebuild LAST** (DJ ruling stands)
5. **DJ verification:** first PIO build of L15 ≈28,034/28,672

## OPEN QUEUE

- 🔴 AI Tutor badly stale — rebuild LAST
- **L12 finished payload banner says "Lesson 10"** (S30) — L12-side fix only (bump + regen payloads + gate)
- **Gate filename regex** — teach it `Lesson_NN.html` (S30)
- **L14 boot-ritual SVG** — candidate (S30)
- L04 payload backfill · L04 §3.6 `initFiveSensors()` compile-test
- Remaining SVGs: L05×3 · L09×1
- PARKED: Zircon callback (unverified) · §9 difficulty grouping · L06 card pattern · "Know Your Zumo" page
- 📖 Proposed Bible §11 addition (physically-impossible-feature rule) — **STILL AWAITING DJ**

## DJ'S PHOTO QUEUE

| Slot | Shot |
|---|---|
| [IMAGE 4.1] + [10.1] | Underside, five-down jumpers — one shot fills both |
| [IMAGE 4.2] | Front array, factory jumpers |
| [IMAGE 5.4] | The jumper move |
| [IMAGE 6.7] | OLED live counts, robot pushed by hand |
| [IMAGE 11.5] | Test track, gaps at 3/7/10 cm |
| [IMAGE 12.1] | Delrin sheet, Zumo mid-turn |
| [IMAGE 13.1] | Rescue space: walls, silver strip, both balls |
| [IMAGE 13.2] | Gripper/arm preview collage |
| [IMAGE 14.1] | RoboCup Junior event atmosphere |
| [IMAGE 14.2] | Labeled competition kit |
| 🆕 [IMAGE 16.1] | Showcase day: robots, posters, bracket on the whiteboard |

## HARDWARE FACTS — VERIFIED, DO NOT RE-LITIGATE

- 🆕 **FLASH CEILING = 28,672 B** (32,768 − 4,096 bootloader) · **RAM = 2,560 B** — `a-star32U4.json`, enforced by the linker. **PlatformIO AVR builds use `-flto` by default.** Measure with the student's flags or the number is fiction.
- 🆕 **EEPROM = 1,024 B**, ~3 ms/byte write, ~100k writes/cell. Never write while driving; a save in `loop()` murders a cell in minutes.
- 🆕 **The heap (~960 B) belongs to Pololu** — QTR + prox libraries malloc calibration arrays and pin lists. Not cuttable.
- 🆕 **The buzzer is all-or-nothing (~1,828 B)** — the first `playNote` links the entire tone engine + note table; later calls ride free.
- **Board: OLED ONLY.** Motor drivers: **DRV8838 ×2** (not 8388).
- **Pins 20/4 physically shared** — five-line and three-prox mutually exclusive; Config 2 (ours from L06) = 5 line + 1 front prox.
- **IMU costs ZERO pins** (I2C). `Wire.begin()` REQUIRED. `RobotConfig.h` has no `<Arduino.h>` — plain `int`.
- **Gyro cal = 1,024 samples, robot PERFECTLY STILL, BEFORE the line-cal spin.**
- **Line sensors read ONE brightness axis.** Cliff detection PHYSICALLY IMPOSSIBLE (S27).
- **`readCalibrated()` CLAMPS at 0** (S30) — silver invisible to calibrated eyes; raw channel: brighter = LOWER.
- **A black ball absorbs IR** (S30). **A wall is a LANDMARK** (S30). **Gyro-zero drift check auto-catches a spun calibration** (S30).
- **`initFiveSensors()` timeout = 2000 µs** (S31) — loop period 2–3 ms, NOT constant; `millis()` cannot resolve it — `micros()`, measured every pass.
- **`readLine()` SATURATES when blind** (S31) — pins to 0/4000 and holds. Fine for P; poison for an integrator.
- **TRIM:** `setSpeeds(speed + TRIM, speed)` — LEFT motor, open loop only; NEVER in `turnDegrees`/`turnDegreesGyro`/`followLine`. **Encoder gating: average BOTH.**

## PROCESS RULES — LEARNED THE HARD WAY

- 🆕 **CHECK THE CEILING, NOT JUST THE BYTES** (S32). A harness that links a region the chip doesn't have prints PASS on unflashable programs. Assert the budget inside the tool — `PASS` must mean *fits on the robot*.
- 🆕 **MEASURE WITH THE STUDENT'S FLAGS** (S32). PlatformIO AVR = `-flto` by default; a no-LTO byte count is a different program. Harness v3.0 mirrors `builder/frameworks/arduino.py` verbatim.
- 🆕 **CONSOLE/LINKER OUTPUT IN STYLED DIVS, NEVER `<pre>`** (S32) — the gate reads every pre; output text can never byte-match a payload.
- 🆕 **COVER THE GATE'S FULL CHUNKS** (S32). A pre showing part of a blank-line chunk can never match it — and a slice→file substring self-check validates the WRONG direction. Build a payload→corpus coverage checker; run it before the gate.
- 🆕 **REBUILD THE MAKER IDEMPOTENTLY FROM THE CLEAN LIVE BASE** (S32) — never patch a patch.
- 🆕 **SVG VISUAL QA VIA cairosvg** (S32) — `pip install cairosvg --break-system-packages`, render, view the PNGs before presenting.
- **RUN THE GATE ON UNTOUCHED SOURCE AS A CONTROL — FIRST, EVERY TIME.**
- **EXTRACT, DON'T RECONSTRUCT** (Bible §11): begin from `PAYLOADS["N-1"]["finished"]`; assert `len(files)==8`.
- **CHECK THE TOOL BEFORE BELIEVING ITS OUTPUT** — S30 ×3, S31, and now S32's ceiling. The most expensive class of bug in this project is a lying instrument.
- **RE-CLONE *AFTER* THE HUMAN CONFIRMS THE PUSH, NEVER BEFORE** (S31).
- **PURGE ORDER IS THE INVERSE OF PUSH ORDER** (S31).
- **ALIGN EVERY `<pre>` TO THE GATE'S BLANK-LINE CHUNK BOUNDARIES** (S31).
- **A TUNING RIG YOU HAVE TO RECOMPILE IS NOT A TUNING RIG** (S31). **"SMOOTHER" IS NOT A MEASUREMENT** (S31).
- **Byte counts lie — disassemble.** A `+0` is often honest — **verify with avr-nm**.
- **The old instrument stays until its last reader is gone.**
- **`node --check` after EVERY Maker injection.** Bounded-scope asserts; `count==1` is NOT a span check.
- **After prose salvage, re-run the defect-family grep on the ASSEMBLED file** (S30; held S31, S32).
- **The reversible highlighter** makes lesson pres byte-derive by construction.
- **Maker PAYLOADS = canonical carrier of state JSONs** (S30).
- **Match the published document wrapper** (S31): full HTML documents — `<!DOCTYPE>`, sticky nav, h2 canon, gradient footer. Not a fragment, not Georgia.
- **HTML extraction:** strip tags + `html.unescape()` — keywords are span-wrapped.
- **Git:** `clone --depth 1`; re-clone each batch (after confirmation); git never loses a committed file.
- **SVG canon:** 1100×850 · gradient title band `#1a5276→#2e86ab` · single-polygon arrows · §4–6 green · no `--` in XML comments · collision check first.
- **Versioning:** major `v#` · moderate `v#.#` · minor `v#.#.#` · no suffixes · in-file "Version N" = MAJOR DIGIT ONLY · full version only in the WORKING filename.
- **DELIVER THE WORKING FILENAME, NOT THE PUBLISHED ONE** (S31).

## 🔴 SESSION-CLOSE WRITE-ORDER RULE (locked S28)

**REGENERATE LIVE.md LAST**, after every other file is final. Read every version out of the file just written — `grep`, never memory. The version appears **TWICE** in LIVE.md (status line AND source-of-truth banner) — fix BOTH. Historical version mentions in session blocks stay untouched.

## FILE DELIVERY (locked S23)

DJ **cannot** access `/mnt/user-data/outputs`. Every deliverable: outputs **root**, **flat filename**, `present_files` on **every** artifact. A file never presented does not exist for DJ.

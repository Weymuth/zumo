# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 13, 2026 (Session 31 close)
**Status:** 🌐 **THE SITE IS LIVE** · 📗 16-lesson book · L01 v03.1.0 · L02 v02.0.28 · L03 v03.0.10 · L04 v04.0.2 · L05 v04.1.2 · L06 v04.5.0 · L07 v04.3.0 · L08 v04.1.0 · L09 v05.0.0 · L10 v02.1.0 · L11 v02.0.1 · L12 "Wheels Lie" v01.0.0 · L13 "Rescue Zone: Flying on Instruments" v02.0.0 · L14 "Competition Prep" v02.0.0 · **L15 "The Present Isn't Enough" v02.0.0 (NEW — REBUILT)** · L15→L16 Showcase v01.0.2 · Bible **v8.18** · Maker **v2.21** · Gate **v1.1** · 🎯 **PAYLOAD GATE PASSES BOOK-WIDE: 14 LESSONS, 1,171 BODIES, ZERO MISMATCHES**
**Currently working on:** SESSION 32 = (1) **push batch** (3 SVGs → Maker v2.21 → Lesson 15), (2) **project purge** (4 files now; Maker + L15 after the push), (3) **L16 Engineering Showcase — THE LAST LESSON**, (4) T-2 cross-reference audit once L16 lands.

> **Source of truth = `ZUMO_SUPER_BIBLE.md` (v8.18).** Filename is UNVERSIONED — the version lives ONLY in the Bible's internal version line. Upload this file at session start; verify internal version = **v8.18**.

---

## 🌐 THE SITE IS LIVE — `weymuth.github.io/zumo`

```
weymuth.github.io/zumo/
├── index.html        ← WELCOME SCREEN (two doors: Textbook | AI Tutor)
├── tutor.html        ← the AI Tutor (stale — rebuild LAST)
├── newproject.html   ← Project Maker (v2.21 STAGED, v2.20 live — push!)
├── timer.html
├── lessons/
│   └── Lesson_01.html … Lesson_14.html   ← STABLE FILENAMES (14 live)
│       (Lesson_15.html STAGED — push clears the 3rd of 4 dead links; only 16 remains)
└── images/           ← 98 files (+3 SVGs staged)
```

**Stable-filename rule:** published lessons are `Lesson_NN.html`, version NOT in the published name. To ship a new version: overwrite `Lesson_NN.html`. That is the whole procedure. Working files keep the full `v##.#.#`; in-file "Version N" = MAJOR DIGIT ONLY.

**Get lessons from GitHub, not the project:** `git clone --depth 1 https://github.com/Weymuth/zumo.git` — re-clone each batch. **The Maker's PAYLOADS is the canonical carrier of compiled state JSONs** (S30) — carryovers live in DJ's downloads, not project capacity.

⚠️ **Gate quirk:** `gate_payload_match.py` cannot parse published `Lesson_NN.html` names — copy to `Lesson_NN_x_v01_0_0.html` before running. Proper fix queued.

---

## 📌 PUSH BATCH (ordered, blocking, NOTHING PUSHED)

1. **3 SVGs → images/**: `L15_GRAPHIC_15-01_three_tenses.svg` · `L15_GRAPHIC_15-02_p_vs_pd.svg` · `L15_GRAPHIC_15-03_windup_on_a_curve.svg` (all NEW, no collisions)
2. **Maker v2.21 → Pages** (KINDS[15] + PAYLOADS['15'], 16 keys × 8 files; DL_ALL = [2..15]; TITLES[15] retitled)
3. **THEN** `Lesson_15_The_Present_Isnt_Enough_v02_0_0.html` → upload, **then rename on GitHub to `lessons/Lesson_15.html`** (same procedure as L13/L14 in S30). **Third dead link clears; only 16 remains.**

---

## 🔴 PROJECT PURGE — APPROVED S31, INVERSE-OF-PUSH ORDER

**Purge NOW (4 files, 364 KB):**
- `Lesson_13_Rescue_Zone_Flying_on_Instruments_v02_0_0.html` — md5-identical to published `Lesson_13.html` (846adcdf3b95)
- `Lesson_14_Competition_Prep_v02_0_0.html` — md5-identical to published `Lesson_14.html` (3dff51ae31e3)
- `Lesson_14_Advanced_PID_Control_v01_0_1.html` — **the old L15 source. SPENT** (Path A rebuild done; §3 prose salvaged; 7 challenges retargeted)
- `ZUMO_S31_HANDOFF.md` — spent

**Purge AFTER the push lands (4.83 MB):** `newproject.html` + `Lesson_15_The_Present_Isnt_Enough_v02_0_0.html`.
**`newproject.html` is 86% of the project by itself and grows every lesson.** It is published on Pages and can be cloned at session open like everything else.

### ⚠️ PURGE SAFETY GATE — run BEFORE deleting either file
**Purge order is the INVERSE of push order. Never purge an artifact that is not confirmed live.**
```
git clone --depth 1  →  zumo/newproject.html   (repo root)
  ✓ grep "Project Maker v"   → must read v2.21
  ✓ PAYLOADS has key '15'    → 16 keys × 8 files
  ✓ node --check             → PASS
  ✓ gate_payload_match.py    → PASS book-wide
  ✓ lessons/Lesson_15.html   → HTTP 200, md5 dfe29ac4f55d (post-rename)
```
**All green → purge. Any red → the push did not land and the project copy is the ONLY copy. Do not delete.**

**KEPT REGARDLESS:** `Lesson_15_Engineering_Showcase_v01_0_2.html` — **the L16 source; the project is its ONLY copy.**

---

## ✅ S31 — L15 "THE PRESENT ISN'T ENOUGH" v02.0.0 (REBUILT, PATH A)

**Survey overturned S29's call.** S29 said *depth pass — the healthiest file in the book*. It surveyed for **defects**, and the defect family was genuinely clean (0 timed motion, 0 raw reads, 0 `lcd.`, 0 local hardware objects). But the file had **no code layer**: 27 pres of fragments, **zero `#include`**, no 8-file project, RobotSensors/RobotHelpers never mentioned, no Maker registry, no images, div-banner skeleton not h2 canon. **DJ ruled Path A.**

### 🔬 TWO FINDINGS FROM LIBRARY SOURCE THAT DECIDED THE LESSON
1. **`initFiveSensors()` sets the QTR-RC timeout to 2000 µs** (`Zumo32U4LineSensors.h:86`). One `readLinePosition()` blocks up to **2 ms**, and **longer over black than over white** — the loop is ~2–3 ms and **its period is not constant; it depends on the surface.** `millis()` resolves to 1 ms. **The old file computed `dt` with `millis()` (14 calls).** The derivative lesson was dividing by a clock that can return **0**. → `micros()` (4 µs). **Measure dt every pass; never assume it.**
2. **`readLine()` SATURATES when blind** (`QTRSensors.cpp`) — pins to 0 or 4000 (last side seen) and holds. Error slams to ±2000. Harmless to P. **Poison to an integrator.**

### THE ONE IDEA
**The I term assumes a constant error is a MISTAKE.**
On a **curve**, a constant error is not a mistake — **it IS the steering command.** I mistakes the answer for a mistake and overshoots every corner exit. *(Arithmetic: the steady-state error I exists to erase is ~80 units of a ±2000 half-scale = **4%**. The price is the exit of every curve.)*
On a **dying battery**, a constant error is a lie with no honest excuse, and **I is the only term that can kill it.**
**→ THE LINE LOOP GETS PD. THE SPEED LOOP GETS THE I.** Same math, opposite verdict. **The difference lives in the world, not the code.**

### ARCHITECTURE
- **`followLine()` keeps its NAME and every CALL SITE** (L11 grammar). No `followLinePD()`. The rescue sweep, the gap, the intersections all inherit a better controller for free.
- `currentKp` (already in students' hands) grows to **four live gains**: Kp · Kd · KpSpeed · KiSpeed. **A- / C+ / hold-A-tap-C = next gain.**
- **THE BENCH — `TUNING_RUN` scores every run: MAE · PEAK · WEAVE** (mean |error| · worst moment · sign-flips/sec). A fixed 10-s bell, **because two gains are only comparable if the runs were.**
- **On-robot Ziegler–Nichols:** WEAVE at Ku gives **Tu = 2 ÷ WEAVE**; the robot prints `TRY Kd = Kp·Tu/8`. Taught explicitly as **a starting point, not an answer.**
- **Hill-climb with a real STOPPING CONDITION:** one gain, ±50%, keep only if MAE drops; **stop when no single ±50% move improves MAE.**
- **THE DOORWAY:** `enterFollowing()` — 4 re-entry sites collapse to one; the reset lives in the door, not the callers.
- Speed loop built from instruments already owned: `averageCounts()` + `COUNTS_PER_CM` + the dt `followLine()` already read. **One clock, two loops.**
- **Clamp the MEMORY, not just the output** — an integrator clamped only on the way out keeps growing inside and refuses to come back down.

### VERIFIED
**16 states × 8 files, 16/16 green, negative control FAILS.**
Bytes: **29,182** (= L14 finished; byte-matches the S30 record) → **+0** (consts) → **+0** (clock) → **+260** (PD) → **+1,340** (bench) → **+68** (doorway) → **31,904** (speed PI).
- **Both `+0`s proven honest by `avr-nm`** — `deltaTimeSec()` is **absent from the binary** until something calls it. `--gc-sections` threw the whole function away. *(Taught on purpose in Step 3.)*
- **b1 (millis dt) and b4 (Kd sign) are BYTE-IDENTICAL to `finished`.** Proven live by disassembly: **`micros` 21→20, `millis` 12→13** · **`__addsf3` 36→35, `__subsf3` 9→10.**
- **Both blanks proven SPENT:** delete D → **−104 B**; delete the speed I → **−66 B**.
- Lesson HTML **194,057 B · 53 pres** · 0 classes/styles/scripts · 0 dead anchors · **0 trapped banners** · defect-family grep **clean on the ASSEMBLED file after prose salvage**.
- Maker **v2.21**: `node --check` PASS, 19 registry rows, all resolve.
- **Gate: PASS, 14 lessons, 1,171 bodies, ZERO mismatches, FIRST RUN.** Control run passed first.

### DESIGN RULING (locked)
**7B, 7C and 7E ship NO payload.** All four gains adjust on the robot between runs. **A tuning rig you have to recompile is not a tuning rig.** Only 7A (strip chart, no motors) and 7D (**I on the line — designed to fail**) change code.

### SVGs (3, NEW)
`15-01_three_tenses` · `15-02_p_vs_pd` · `15-03_windup_on_a_curve` — all 1100×850 canon, no collisions.

---

## S32 AGENDA

1. 🔴 **Push batch** (3 SVGs → Maker v2.21 → Lesson_15.html)
2. 🔴 **Project purge** — 4 files now; Maker + L15 **after** the push safety gate
3. **L16 "Engineering Showcase" — THE LAST LESSON.** Source: `Lesson_15_Engineering_Showcase_v01_0_2.html` (project's ONLY copy). Survey first — S29 said "3 code blocks in 94 KB," and S29 also said L15 was healthy.
4. **T-2 deferred audit** — cross-reference integrity + promise/keep. Run once L16 lands (renumber complete).
5. Open queue · photo queue · **AI Tutor rebuild LAST** (DJ ruling stands).

## OPEN QUEUE

- 🔴 AI Tutor badly stale — rebuild LAST
- **L12 finished payload banner says "Lesson 10"** (S30) — L12-side fix only (bump + regen payloads + gate)
- **Gate filename regex** — teach it `Lesson_NN.html` (S30)
- **L14 boot-ritual SVG** — candidate (S30)
- L04 payload backfill · L04 §3.6 `initFiveSensors()` compile-test
- Remaining SVGs: L05×3 · L09×1 · L16×2
- PARKED: Zircon callback (unverified) · §9 difficulty grouping · L06 card pattern · "Know Your Zumo" page
- 📖 Proposed Bible §11 addition (physically-impossible-feature rule) — **STILL AWAITING DJ**
- L16 §4.1 loose DRV8838 carrier framing (S29)

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

## HARDWARE FACTS — VERIFIED, DO NOT RE-LITIGATE

- **Board: OLED ONLY.** Motor drivers: **DRV8838 ×2** (not 8388).
- **Pins 20/4 physically shared** — five-line and three-prox mutually exclusive; Config 2 (ours from L06) = 5 line + 1 front prox.
- **IMU costs ZERO pins** (I2C, fixed). `Wire.begin()` REQUIRED. `RobotConfig.h` has no `<Arduino.h>` — plain `int`.
- **Gyro cal = 1,024 samples, robot PERFECTLY STILL, BEFORE the line-cal spin.** A spin cannot calibrate a gyro.
- **Line sensors read ONE brightness axis.** Cliff detection PHYSICALLY IMPOSSIBLE (S27).
- **`readCalibrated()` CLAMPS at 0** (S30) — **silver is invisible to calibrated eyes**; `calibratedMinimumOn[]` public; raw channel: brighter = LOWER.
- **A black ball absorbs IR** (S30) — near-invisible to the prox; cameras see it, this robot does not.
- **A wall is a LANDMARK** (S30) — physical references erase dead-reckoning drift at every contact, free.
- **Gyro-zero drift check** (≤3°/500 ms, still) **auto-catches a spun calibration** at boot (S30).
- 🆕 **`initFiveSensors()` timeout = 2000 µs** (S31, library-verified) — one line-sensor read blocks up to 2 ms, **longer over black than white.** **The loop period is 2–3 ms and NOT constant.** `millis()` (1 ms) **cannot resolve it** — use `micros()` (4 µs) and **measure dt every pass.**
- 🆕 **`readLine()` SATURATES when blind** (S31, library-verified) — pins to 0/4000 (last side seen) and holds. Error slams to ±2000. Fine for P; **poison for an integrator.**
- **TRIM:** `setSpeeds(speed + TRIM, speed)` — LEFT motor, open loop only; NEVER in `turnDegrees`/`turnDegreesGyro`/`followLine`. **Encoder gating: average BOTH.**

## PROCESS RULES — LEARNED THE HARD WAY

- **RUN THE GATE ON UNTOUCHED SOURCE AS A CONTROL — FIRST, EVERY TIME.**
- **EXTRACT, DON'T RECONSTRUCT** (Bible §11): begin from `PAYLOADS["N-1"]["finished"]`; assert `len(files)==8`.
- **CHECK THE TOOL BEFORE BELIEVING ITS OUTPUT** — S30 ×3; **S31 again:** my banner-depth check flagged all 5 PART banners as trapped because it measured each banner's **inner title div**. Truth: zero trapped. **Test the div that RENDERS.**
- 🆕 **RE-CLONE *AFTER* THE HUMAN CONFIRMS THE PUSH, NEVER BEFORE** (S31). My open-of-session clone predated DJ's rename by minutes and reported L13/L14 as dead links. **A stale clone that says "not there" is indistinguishable from a failed push.**
- 🆕 **PURGE ORDER IS THE INVERSE OF PUSH ORDER** (S31). Never purge an artifact that is not confirmed live. Verify by clone + version grep + gate, THEN delete.
- 🆕 **ALIGN EVERY `<pre>` TO THE GATE'S BLANK-LINE CHUNK BOUNDARIES** (S31). The gate chunks payloads on `\n\n`; a pre that starts or ends mid-chunk can never byte-match. Auto-expanding each slice to the enclosing chunk took the gate from 18 unaccounted → 0 **by construction, not by luck.**
- 🆕 **A TUNING RIG YOU HAVE TO RECOMPILE IS NOT A TUNING RIG** (S31). If students must tune it, it adjusts on the robot.
- 🆕 **"SMOOTHER" IS NOT A MEASUREMENT** (S31). Build the instrument before you turn the knob. A score you can compare is the difference between engineering and hoping.
- **Byte counts lie — disassemble.** A `+0` is often honest — **verify with avr-nm**. **A +2 needs explaining as much as a +820.**
- **The old instrument stays until its last reader is gone.** Every rung a student can stop on builds green.
- **`node --check` after EVERY Maker injection.** Bounded-scope asserts; `count==1` is NOT a span check.
- **A sabotage state's diff = exactly the lines the lesson's mystery pre shows** (S30).
- **After prose salvage, re-run the defect-family grep on the ASSEMBLED file** (S30, held again in S31 — clean).
- **The reversible highlighter** (escape → highlight; strip+unescape == source) makes lesson pres byte-derive by construction. **S31: torture-tested across all 128 file bodies, 0 failures.**
- **Maker PAYLOADS = canonical carrier of state JSONs**; carryovers to DJ's downloads, not project capacity (S30).
- **Match the published document wrapper** (S31): lessons are FULL HTML documents — `<!DOCTYPE>`, `<title>`, `<body id="top" style="font-family:'Segoe UI'...">`, sticky nav, gradient footer. **Not a fragment, and not Georgia.**
- **HTML extraction:** pipe through `sed 's/<[^>]*>//g'` + `html.unescape()` — keywords are span-wrapped.
- **Git:** `git clone --depth 1` works when fetch/API fail; **re-clone each batch**; git never loses a committed file.
- **Compile harness:** `S25_harness_build.sh --setup` self-contained; **never name a staging dir `build/`**; elf at `build/fw.elf`.
- **SVG canon:** 1100×850 · gradient title band `#1a5276→#2e86ab` · single-polygon arrows · §4–6 green · no `--` in XML comments · check filename collisions first.
- **Versioning:** major `v#` · moderate `v#.#` · minor `v#.#.#` · no suffixes · never renumber slots · in-file "Version N" = MAJOR DIGIT ONLY · full version only in the WORKING filename, never the published one.
- 🆕 **DELIVER THE WORKING FILENAME, NOT THE PUBLISHED ONE** (S31 miss). Every lesson artifact I hand DJ is `Lesson_NN_Title_v##_#_#.html`. DJ uploads it, then renames to `Lesson_NN.html` on GitHub. **The gate's own regex expects the versioned form** — shipping the stable name breaks the gate AND loses the version. Two rules, one direction.

## 🔴 SESSION-CLOSE WRITE-ORDER RULE (locked S28)

**REGENERATE LIVE.md LAST**, after every other file is final. Read every version out of the file just written — `grep`, never memory. The version appears **TWICE** in LIVE.md (status line AND source-of-truth banner) — fix BOTH. Historical version mentions in session blocks stay untouched.

## FILE DELIVERY (locked S23)

DJ **cannot** access `/mnt/user-data/outputs`. Every deliverable: outputs **root**, **flat filename**, `present_files` on **every** artifact. A file never presented does not exist for DJ.

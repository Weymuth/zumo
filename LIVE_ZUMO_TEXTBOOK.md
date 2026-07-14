# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 14, 2026 (Session 34 close)
**Status:** 🌐 **THE SITE IS LIVE — 16/16 LESSONS, ALL CLEAN, PASS B COMPLETE, BYTE COUNTS ARE COMPILER TRUTH** · L01 v03.1.3 · L02 v02.0.31 · L03 v03.0.13 · L04 v04.0.5 · L05 v04.1.4 · L06 v04.5.2 · L07 v04.3.2 · L08 v04.1.2 · L09 v05.0.3 · L10 v02.1.5 · L11 v02.0.3 · L12 v01.0.3 · L13 v02.0.3 · L14 v02.1.1 · L15 v02.0.2 · L16 v02.0.1 · Bible **v8.20** · Maker **v2.23** · Gate **v1.1** · Harness **v3.0** · 🎯 **PAYLOAD GATE PASSES BOOK-WIDE** · 📓 **ENGINEER'S LOG IN ALL 16** · 📐 **EVERY PUBLISHED BYTE COUNT COMPILE-VERIFIED (55 PIO-true builds, S34)**
**Currently working on:** SESSION 35 = (1) **HEADER NORMALIZATION L11→L16** — DJ ruled System A (Q27): blue `#3498db` §1–3, green `#3a7d5c` §4–6, banner `<div id="section-N">` book-wide, (2) **MAKER WIRING L11→L16** — 100 kinds live and unreachable, (3) Grok L01 batch (4 cosmetic items) + `lib_deps` pin bench test, (4) DJ bench checks (L02 green-LED · L09 green-tape), (5) 5 stale image deletions, (6) 22-photo queue, (7) **AI Tutor rebuild LAST**.

> **Source of truth = `ZUMO_SUPER_BIBLE.md` (v8.20).** Filename is UNVERSIONED — the version lives ONLY in the internal line. Verify with `grep -o "Bible version: v[0-9.]*"`.

---

## 🌐 THE SITE — `weymuth.github.io/zumo`

```
weymuth.github.io/zumo/
├── index.html                    ← welcome screen (Textbook | AI Tutor)
├── tutor.html                    ← AI Tutor (stale — rebuild LAST)
├── newproject.html               ← Project Maker (v2.23, live)
├── timer.html
├── ROBOCUP_RESCUE_LINE_2026.md   ← NEW S34 — sole source of truth for competition claims
├── lessons/
│   └── Lesson_01.html … Lesson_16.html   ← ALL 16 LIVE, ALL VERIFIED
└── images/                       ← every asset referenced; 5 stale files queued for deletion
```

**Stable-filename rule:** published lessons are `Lesson_NN.html`. Working files keep the full `v##.#.#`; in-file "Version N" = MAJOR DIGIT ONLY.

**Get lessons from GitHub, not the project:** `git clone --depth 1 https://github.com/Weymuth/zumo.git` — **only after DJ confirms the push, and then check WHICH VERSION landed, not just that something did.**

**🆕 PUSH WORKFLOW (S34):** DJ pushes from a **local GitHub Desktop clone** — set up and verified. The web-UI rename hazard is obsolete on this path. **Claude delivers each session as ONE ZIP in repo layout with final filenames** (DJ ruling, S34): extract over the clone → Commit → Push. See `PUSH_WORKFLOW.md`.

⚠️ **Gate quirk:** `gate_payload_match.py` cannot parse `Lesson_NN.html` — copy to `Lesson_NN_x.html` before running. Fix still queued.

---

## LESSON STATE — all live, all verified by fresh clone (S34 close)

| # | Title | Version | Figures | Placeholders left |
|---|---|---|---|---|
| 01 | Hello, Robot! | v03.1.3 | 18 | 0 |
| 02 | Read Code Like a Pro | v02.0.31 | 10 | 2 |
| 03 | Motors & TRIM | v03.0.13 | 11 | 4 |
| 04 | Line Sensors | v04.0.5 | 5 | 3 |
| 05 | Proximity Sensors | v04.1.4 | 8 | 3 |
| 06 | Encoders | v04.5.2 | 11 | 0 |
| 07 | Code Organization | v04.3.2 | 7 | 7 |
| 08 | Line Following | v04.1.2 | 3 | 0 |
| 09 | Intersections & Dead Ends | v05.0.3 | 8 | 0 |
| 10 | Obstacles | v02.1.5 | 7 | 0 |
| 11 | Time Lies, Distance Doesn't | v02.0.3 | 4 | 0 |
| 12 | Wheels Lie | v01.0.3 | 3 | 1 |
| 13 | Rescue Zone | v02.0.3 | 2 | 2 |
| 14 | Competition Prep | v02.1.1 | 4 | 2 |
| 15 | The Present Isn't Enough | v02.0.2 | 3 | 0 |
| 16 | Nothing Left to Take Away | v02.0.1 | 3 | 1 |

**Book-wide audit (live tree, S34 close):** zero duplicate ids · zero dead anchors · **zero broken `<img>`** · div balance 0 · 📓 Engineer's Log ×16 · payload gate **PASS** · **zero stale byte counts (all 23 old figures purged, verified by residue sweep on a fresh clone)**.

---

## SESSION 34 — WHAT LANDED

### 🏁 PASS B — COMPLETE (all 16 lessons read)
- **L03–L11, L16:** stale file counts (incl. the LAST one, hidden behind a non-breaking hyphen in L10), wrong §8 turn-row logic in L06, "four/six-file" purge, L07 photo descriptions restored verbatim from the shot list, L09 inverted answer key fixed, L10's dead `step_4_RED` link cut, L11 §8A renumbered, L12's impossible 1,350-count corrected to 496, L13's missing Image Index built, L16 near-flawless (2 cosmetics).
- **L14 REBUILT (v02.1.0, moderate):** old lesson with a new code chapter — every defect sat in the OLD half. Fixed: edge-detection capability cut (L11 canon — barrier, not code) · scoring table rebuilt from official 2026 rules (bump 10, obstacle 20, ramp 10/tile, seesaw 20, tile decay 5→3→1→0, exit bonus 60−5×LoP) · **victims are ×1.4 MULTIPLIERS, not points** (all three ≈ ×2.74) — the "skip the zone" strategy was backwards and is now corrected, with the honest note that THIS Zumo cannot complete a rescue (no gripper; both DRV8838s spoken for) · 8-minute clock includes calibration (run gets ~6 min) · battery table → eneloop canon · zero LCD refs · §5.1 cross-ref → §8.2 (DJ ruling closed) · inspection checklist from rules §4.1/4.2/5.2 incl. the pre-mapped-dead-reckoning ban · **first-ever L14 art: 4 SVGs** (14-01 reliability equation · 14-02 startup ritual · 14-03 how-a-run-is-scored · 14-04 competition_mode).
- **📕 `ROBOCUP_RESCUE_LINE_2026.md`** — extracted from the official PDF (updated 2026-03-29), pushed to repo root. **No lesson may contradict it.** 2026 additions that touch the book: fake victims (robots must ignore) · white LED lights on evac-zone walls (→ L13 silver threshold).

### 📐 BYTE RE-AUDIT — EXECUTED AND LIVE (the S32 instrument failure, fully repaired)
- **Harness rebuilt in-session:** avr-gcc 7.3.0 (PlatformIO's exact version) + 9 dep repos + core → `libcore_lto.a`. **Control run: L15/finished = 28,034 B == L16's audited table, byte-exact.** New tool: `extract_project.py` (materializes any Maker payload as a compilable project; `after_step_*` payloads are complete 8-file snapshots).
- **55 compiles.** Every seam chains: L9→L10→…→L15→L16, all matching L16's table. **L16 verified perfect end to end — the wall overflows by exactly 626.** L16 needed zero changes.
- **Corrected live:** L10 (22,544→20,364) · L12 (8 values + deltas; B4 identity HOLDS at 24,534) · L13 (Step 6 is **−44**, disassembly-backed: main −70, showStatus −50, victim vars +26 — "code you delete pays you back"; total cost 368 B; 7E NOT identical, +64; bonus intro "all four identical" → "two of four") · L14 (Step 2 is +0 flat, not "+2 alignment"; 7C's −36 EXACT; B1 −734 not −820) · L15 (all 9 values; B2 sign-flipped to +16 bigger; "two of four sabotages byte-identical" verified EXACTLY — b1 & b4).
- **L13 B2's TRIM=8 disassembly claim verified:** both builds 24,902, byte-identical.

### 🎨 HEADER DRIFT — MAPPED AND RULED (Q27 = System A), NOT YET BUILT
Four systems live today: **A** L01–L10 (banner, blue §1–3 / green `#3a7d5c` §4–6 — CANON) · **B** L11 (banner, wrong green `#2a5a42`) · **C** L12–L14 (plain `<h2 id="section-N">`, no banner, no green) · **D** L15–L16 (blue-gradient `<h2 id="s1..s10">` — nonstandard ids, no green). **No cross-lesson section links exist** — per-lesson conversion is safe. **A header-consistency check joins the gate battery** (root cause: Claude's renderer strips styles; visual drift was invisible to every prior audit).

### 🆕 PUSH WORKFLOW
DJ's GitHub Desktop clone set up and push-verified. `PUSH_WORKFLOW.md` written (→ repo root). **DJ ruling: zip-per-session delivery** — Claude ships one zip in repo layout with final filenames.

---

## 🗑️ REPO CLEANUP — 5 unreferenced images (safe to delete any time)

```
images/L01_IMAGE_1-13_kr_c_programming_book.png     (superseded by 1-18)
images/L07_GRAPHIC_7-16_six_file_architecture.svg   (STALE — the project is 8 files)
images/L08_GRAPHIC_8-03_project_file_tree.svg       (duplicate of 8-3)
images/L09_GRAPHIC_9-07_sensor_patterns.svg         (duplicate of 9-7)
images/L09_GRAPHIC_9-08_project_file_tree.svg       (duplicate of 9-8)
```

---

## S35 AGENDA

1. **HEADER NORMALIZATION L11→L16 to System A** — L11: green swap only. L12–L14: `<h2>` → banner divs. L15–L16: gradient → banner AND `s1..s10` ids → `section-N` (TOC links are self-contained; verified safe). Byte-count lines in converted sections must survive untouched.
2. **MAKER WIRING L11→L16** — ~100 links (L11:18 · L12:21 · L13:19 · L14:13 · L15:16 · L16:8 kinds). `step_4_RED` is an orphan kind in the Maker (link cut S34) — delete from Maker or leave dormant, DJ ruling. One version bump per lesson covers headers + wiring together.
3. **Grok L01 batch** (one minor bump): LED syntax note · debounce note · power-switch label → art queue · `lib_deps` line-break bench check. **PLUS lib_deps pin** — 2.0.1 IS real; DJ's error was syntax; bench-test `@^2.0.1` / `@~2.0.1` / git-tag → moderate bump (Maker + L01 + Bible) when resolved.
4. **DJ bench checks:** L02 §5 green-LED "USB activity light" claim · L09 green-tape 300–700 (Q017).
5. Repo cleanup (5 images) · **22-photo queue** · Bible bump (byte canon + header canon + push workflow + rules doc) · **AI Tutor rebuild LAST**.

## OPEN QUEUE (parked)

- 🔴 AI Tutor badly stale — rebuild LAST (standing DJ ruling)
- Gate filename regex — teach it `Lesson_NN.html`
- L04 §3.6 `initFiveSensors()` compile-test
- "Know Your Zumo" standalone board-map reference page (after the book is done)
- §9 difficulty grouping · L06 goal→logic→template card pattern

---

## NEW CANON — S34 (Bible entries queued for the v8.2x bump)

- **📐 BYTE CANON:** every published byte count must come from `pio_harness.sh` v3.0 (PIO-true). The audited ladder: L7 14,380 · L8 17,194 · L9 18,158 · L10 20,364 · L11 20,542 · L12 24,534 · L13 24,902 · L14 25,640 · L15 28,034 · ceiling 28,672 · L16 wall 29,298 (+626) · L16 finished 28,594 (78 spare). `extract_project.py` joins the toolchain.
- **🏆 COMPETITION CANON:** `ROBOCUP_RESCUE_LINE_2026.md` outranks every lesson on competition facts. RoboCup revises rules yearly — re-extract each season.
- **🎨 HEADER CANON (Q27):** System A book-wide — banner `<div id="section-N">`, blue `#3498db` §1–3, green `#3a7d5c` §4–6. Header-consistency check joins the gate battery.
- **📦 DELIVERY CANON:** zip-per-session, repo layout, final filenames. DJ pushes via GitHub Desktop clone (web-UI rename hazard obsolete on this path — rule retained only for anyone using the browser).
- **Verify a push by clone — and check WHICH VERSION landed** (unchanged, forever).

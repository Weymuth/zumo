# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 14, 2026 (Session 35 close)
**Status:** 🌐 **THE SITE IS LIVE — 16/16 LESSONS, ALL CLEAN, HEADERS NORMALIZED BOOK-WIDE** · L01 v03.1.3 · L02 v02.0.31 · L03 v03.0.13 · L04 v04.0.5 · L05 v04.1.5 · L06 v04.5.3 · L07 v04.3.3 · L08 v04.1.3 · L09 v05.0.4 · L10 v02.1.6 · L11 v02.1.0 · L12 v01.1.0 · L13 v02.1.0 · L14 v02.2.0 · L15 v02.1.0 · L16 v02.1.0 · Bible **v8.21** · Maker **v2.23** · Gate **v1.1** · Harness **v3.0** · 🎯 **PAYLOAD GATE PASSES BOOK-WIDE** · 📐 **ALL 1,180 PUBLISHED FIGURES BYTE-IDENTICAL (S34 audit intact)** · 🎨 **4 PART BANNERS / 5 COLOR GROUPS, ALL 16**
**Currently working on:** SESSION 36 = (1) **MAKER WIRING L11→L16** — 100 kinds live and unreachable; anchors are NOT uniform (L13 regular; L11's only "Step" headings are in §3 theory, not the §6 build) — hand-place, do not pattern-match, (2) Grok L01 batch (4 cosmetic items) + `lib_deps` pin bench test, (3) DJ bench checks (L02 green-LED · L09 green-tape), (4) 5 stale image deletions, (5) 22-photo queue, (6) **AI Tutor rebuild LAST**.

> **Source of truth = `ZUMO_SUPER_BIBLE.md` (v8.21).** Filename is UNVERSIONED — the version lives ONLY in the internal line. Verify with `grep -o "Bible version: v[0-9.]*"`.

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

## LESSON STATE — all live (S35 close)

| # | Title | Version | Figures | Placeholders left |
|---|---|---|---|---|
| 01 | Hello, Robot! | v03.1.3 | 18 | 0 |
| 02 | Read Code Like a Pro | v02.0.31 | 10 | 2 |
| 03 | Motors & TRIM | v03.0.13 | 11 | 4 |
| 04 | Line Sensors | v04.0.5 | 5 | 3 |
| 05 | Proximity Sensors | v04.1.5 | 8 | 3 |
| 06 | Encoders | v04.5.3 | 11 | 0 |
| 07 | Code Organization | v04.3.3 | 7 | 7 |
| 08 | Line Following | v04.1.3 | 3 | 0 |
| 09 | Intersections & Dead Ends | v05.0.4 | 8 | 0 |
| 10 | Obstacles | v02.1.6 | 7 | 0 |
| 11 | Time Lies, Distance Doesn't | v02.1.0 | 4 | 0 |
| 12 | Wheels Lie | v01.1.0 | 3 | 1 |
| 13 | Rescue Zone | v02.1.0 | 2 | 2 |
| 14 | Competition Prep | v02.2.0 | 4 | 2 |
| 15 | The Present Isn't Enough | v02.1.0 | 3 | 0 |
| 16 | Nothing Left to Take Away | v02.1.0 | 3 | 1 |

**Book-wide audit (live tree, S34 close):** zero duplicate ids · zero dead anchors · **zero broken `<img>`** · div balance 0 · 📓 Engineer's Log ×16 · payload gate **PASS** · **zero stale byte counts (all 23 old figures purged, verified by residue sweep on a fresh clone)**.

---

## SESSION 35 — WHAT LANDED

### 🎨 HEADER NORMALIZATION — COMPLETE, ALL 16 LESSONS
**DJ ruling: FOUR PART banners, FIVE colour groups.** The Bible was already right; the book had drifted.
Canon: §1–3 `#3498db` · §4–6 `#3a7d5c` · §7/8/8A `#c45d76` · §9 `#9b6a9e` · §10+end `#6c757d` (colour, **no divider**).

The drift was deeper than S34 mapped — **10 lessons were wrong, not 6**:
- **L07/L08/L09** had NO PART 3 banner at all (jumped PART 2 → PART 4). Inserted.
- **L10** had a 5th banner ("PART 5 — Wrap Up") and PART 3 mistitled "Verify & Extend". Fixed.
- **L11** was off in FOUR groups, not one: `#2a5a42` green (the *dark variant*, not the cap colour), `#e67e22` orange, `#8e44ad` purple, `#16a085` teal. Repainted.
- **L11–L14** had all-blue nav strips and all-blue PART banners. Recoloured.
- **L15/L16** had NO section caps, gradient PART banners with non-canon groupings (PART 2 = §4–5, PART 3 = §6), and `s1..s10` ids. Rebuilt.

### 🗺️ IMAGE INDEX NAV PILL — REMOVED BOOK-WIDE (DJ ruling)
Students have no need to navigate to the Image Index. The **pill** is gone from all 8 lessons that carried it (L05–L12); the **section** stays, still gray. The Bible's nav-count line (§6.5) already excluded it — the lessons had drifted. Line rewritten to 12–14.

### 🔴 L10 `step_4_RED` — RE-LINKED (DJ ruling)
The Maker's "broken on purpose" Red Build was live and gated but unreachable — S34 had cut the link *and authored* "No download for the broken one — you typed it yourself." Verified the payload really is broken (header + cpp both define `proxSensors`, no `extern`) and that fixing the `extern` builds green (the three new functions are declared but uncalled, so nothing fails to link). Line replaced with a link. **Maker unchanged (v2.23).**

### ✅ VERIFICATION
- Payload gate: **PASS**, 16/16.
- **1,180 published numeric figures compared against the pre-session clone — all byte-identical.** The S34 byte audit survived intact.
- `<div>` balance verified on every converted lesson.

### 🧹 PROJECT FOLDER — EMPTIED
Everything now lives in the repo (DJ pushed the toolchain at 07:43 EDT: `gate_payload_match.py`, `pio_harness.sh`, `extract_project.py`, the handoff). Project instructions are now one line.

### ⚠️ NOT DONE — MAKER WIRING (deferred to S36 by DJ ruling)
100 kinds still unreachable (L11:18 · L12:20 · L13:18 · L14:17 · L15:19 · L16:8). **Anchors are not uniform — do not pattern-match.** L13 is fully regular (Steps / 7A–7E / Challenges 9.1–9.3 / Mysteries B1–B4); L11's only "Step" headings sit in §3 theory, not the §6 build. Canon link shapes are extracted in the S36 handoff. L11–L16 will bump a SECOND time — DJ accepted this over rushing 100 links.

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

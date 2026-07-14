# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 14, 2026 (Session 36 close)
**Status:** 🌐 **THE SITE IS LIVE — 16/16 LESSONS · THE MAKER IS WIRED: 99 KINDS, 99 LINKS, CLEAN 1:1** · L01 v03.1.3 · L02 v02.0.31 · L03 v03.0.13 · L04 v04.0.5 · L05 v04.1.5 · L06 v04.5.3 · L07 v04.3.3 · L08 v04.1.3 · L09 v05.0.4 · L10 v02.1.6 · L11 v02.2.0 · L12 v01.2.0 · L13 v02.2.0 · L14 v02.4.0 · L15 v02.2.0 · L16 v02.2.0 · Bible **v8.22** · Maker **v2.25** · Gate **v1.1** · Harness **v3.0** · 🎯 **PAYLOAD GATE PASSES BOOK-WIDE (15 lessons)** · 📐 **ALL PUBLISHED FIGURES BYTE-IDENTICAL (S34 audit intact)** · 🔗 **EVERY MAKER KIND REACHABLE FROM ITS LESSON**
**Currently working on:** SESSION 37 = (1) **`lib_deps` PIN** — Maker line 1663 is unpinned; tag `2.0.1` IS real, but the library ships NO `library.json` (Arduino manifest only) and the PlatformIO registry is unreachable from the container. DJ runs `pio pkg show pololu/Zumo32U4`, OR accept the registry-independent git-tag pin — then a coordinated Maker + L01 + Bible bump, (2) Grok L01 batch (LED syntax · debounce note · power-switch label art), (3) DJ bench checks (L02 green-LED · L09 green-tape), (4) 5 stale image deletions (verified 0 refs), (5) 22-photo queue, (6) **AI Tutor rebuild LAST**.

> **Source of truth = `ZUMO_SUPER_BIBLE.md` (v8.22).** Filename is UNVERSIONED — the version lives ONLY in the internal line. Verify with `grep -o "Bible version: v[0-9.]*"`.

---

## 🌐 THE SITE — `weymuth.github.io/zumo`

```
weymuth.github.io/zumo/
├── index.html                    ← welcome screen (Textbook | AI Tutor)
├── tutor.html                    ← AI Tutor (stale — rebuild LAST)
├── newproject.html               ← Project Maker (v2.25, live)
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

## LESSON STATE — all live (S36 close)

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
| 11 | Time Lies, Distance Doesn't | v02.2.0 | 4 | 0 |
| 12 | Wheels Lie | v01.2.0 | 3 | 1 |
| 13 | Rescue Zone | v02.2.0 | 2 | 2 |
| 14 | Competition Prep | v02.4.0 | 4 | 2 |
| 15 | The Present Isn't Enough | v02.2.0 | 3 | 0 |
| 16 | Nothing Left to Take Away | v02.2.0 | 3 | 1 |

**Book-wide audit (live tree, S34 close):** zero duplicate ids · zero dead anchors · **zero broken `<img>`** · div balance 0 · 📓 Engineer's Log ×16 · payload gate **PASS** · **zero stale byte counts (all 23 old figures purged, verified by residue sweep on a fresh clone)**.

---

## SESSION 36 — WHAT LANDED

### 🔗 THE MAKER IS WIRED — 99 KINDS, 99 LINKS, CLEAN 1:1
L11–L16 carried **100 live, gated, unreachable payload kinds**. Every one is now linked from the lesson that teaches it. Links were **hand-placed and audited against the heading they landed under** — no pattern-matching. Two asserts fired mid-build and were right both times: a duplicate text anchor in L13 that would have wired Challenge 2's link into the wrong block, and four L12 mystery links collapsing to one offset (L12's mysteries are heading-less `<div>` cards).

### 🪜 L11 §7 RE-LETTERED — the Maker was off by one
L11's ladder is five rungs (7A–7E) but the Maker's letters had drifted from 7C on: `cal_7c` was labelled with the lesson's **7D** content, `cal_7d` referenced **no rung at all**, and the lesson's **7C — TRIM Under Blindness had no kind**. Re-lettered to match. 7C now points at `cal_7b` (a run-only rung — no code changes, the student zeroes their own TRIM). 7D's merged payload compile-verified: **20,560 B, 8,112 B spare, RAM 617/2,560** — byte-identical to the old `cal_7d`. Old `cal_7c` payload deleted.

### 🗑️ L14 `step_4` RETIRED — a duplicate kind, not a build (DJ ruling)
L14 was the **only** lesson with a `step_*` kind for its LAST step, and `after_step_4` was **byte-identical to `finished`** — the Maker offered one project under two names. Canon (now Bible §15.2): step kinds cover steps 1..N−1; **`finished` IS step N**. Kind retired, orphaned payload deleted, L14 now reads exactly like its five siblings. Book-wide kinds 100 → **99**.

### 📖 BIBLE v8.22 — NEW §15 MAKER REGISTRY & LINK CANON
Four rules, all earned this session: **15.1** the §7 ladder is five rungs and the Maker's letters must match the lesson's · **15.2** `finished` IS the last step · **15.3** a kind may share another kind's `payloadRef` (run-only rungs — do not manufacture duplicate payloads) · **15.4** the four link shapes · **15.5** ⚠️ **the Maker is NOT uniformly formatted — edit by offset, never by line.**

### 🐛 THE BUG THAT PROVES §15.5
`PAYLOADS` is pretty-printed for some lessons and **compact single-line for others** — L14's whole block is ONE line. A line-based deletion (`rfind('\n')`) walked back past every preceding key and **silently collapsed PAYLOADS from 15 lessons to 10**. The JS still parsed. Only a `node` re-parse asserting lesson count caught it. Rebuilt with an offset-exact cut.

### ⚖️ CHALLENGE SOLUTION-DISCLOSURE — RAISED, PARKED (DJ ruling)
Wiring the §9 links surfaced that **the book has no disclosure canon**: L06/L07/L11/L13/L14 publish solutions · **L08/L09 withhold them** · L10 gives neither · L12/L15 print a scaffold with a blank. Also found: **L08's challenge cards already carry a Maker link** — pointing at `finished`, a neutral starting copy, not the answer. DJ: *"leave things as they are for now; I'll make the call after I go through them as a student."* Link goes inside whatever each lesson already discloses. Three options preserved in memory for the ruling.

### ✅ VERIFICATION
Payload gate **PASS, all 15 lessons**, control run on untouched source first · **99 links / 99 kinds, 1:1** · Maker parses, zero dangling refs, zero orphan payloads · byte-residue sweep intact (S34 audit preserved) · structure balanced, zero heading churn · push verified by fresh clone (md5, all 7 files).

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

## S37 AGENDA

1. **`lib_deps` PIN (blocked on one DJ command).** Maker line 1663 = `lib_deps = pololu/Zumo32U4`, unpinned. **Verified:** the Pololu repo's real tags are `1.1.1 … 2.0.0, 2.0.1`; tag `2.0.1` exists and its manifest says `version=2.0.1`. **Also verified — likely the cause of DJ's build error:** the library ships **only `library.properties`** (the Arduino manifest); there is **no `library.json`**, and PlatformIO reads `owner/name` as a *registry* reference whose versions need not match the GitHub tags. `api.registry.platformio.org` is **blocked by the container allowlist** — Claude cannot settle this from here. Close it either by (a) DJ running `pio pkg show pololu/Zumo32U4`, or (b) accepting the registry-independent git-tag pin: `lib_deps = https://github.com/pololu/zumo-32u4-arduino-library.git#2.0.1`. Then a coordinated Maker + L01 prose + Bible change (moderate bump).
2. **Grok L01 batch** (one minor bump): LED syntax note · debounce note · power-switch label → Claude SVG · `lib_deps` line-break bench check.
3. **DJ bench checks:** L02 §5 green-LED "USB activity light" claim · L09 green-tape 300–700 (Q017).
4. **Repo cleanup — 5 stale images, verified 0 references** (see below). One `git rm`.
5. **22-photo queue** (DJ, `IMAGE_SHOT_LIST.md`).
6. 🔴 **AI Tutor rebuild — LAST** (standing DJ ruling).

## OPEN QUEUE (parked)

- 🔴 AI Tutor badly stale — rebuild LAST (standing DJ ruling)
- Gate filename regex — teach it `Lesson_NN.html`
- L04 §3.6 `initFiveSensors()` compile-test
- **Challenge solution-disclosure — PARKED by DJ** (5 patterns across 10 lessons; three options held in memory; DJ rules after classroom use)
- "Know Your Zumo" standalone board-map reference page (after the book is done)
- §9 difficulty grouping · L06 goal→logic→template card pattern

---

## NEW CANON — S34 (Bible entries queued for the v8.2x bump)

- **📐 BYTE CANON:** every published byte count must come from `pio_harness.sh` v3.0 (PIO-true). The audited ladder: L7 14,380 · L8 17,194 · L9 18,158 · L10 20,364 · L11 20,542 · L12 24,534 · L13 24,902 · L14 25,640 · L15 28,034 · ceiling 28,672 · L16 wall 29,298 (+626) · L16 finished 28,594 (78 spare). `extract_project.py` joins the toolchain.
- **🏆 COMPETITION CANON:** `ROBOCUP_RESCUE_LINE_2026.md` outranks every lesson on competition facts. RoboCup revises rules yearly — re-extract each season.
- **🎨 HEADER CANON (Q27):** System A book-wide — banner `<div id="section-N">`, blue `#3498db` §1–3, green `#3a7d5c` §4–6. Header-consistency check joins the gate battery.
- **📦 DELIVERY CANON:** zip-per-session, repo layout, final filenames. DJ pushes via GitHub Desktop clone (web-UI rename hazard obsolete on this path — rule retained only for anyone using the browser).
- **Verify a push by clone — and check WHICH VERSION landed** (unchanged, forever).

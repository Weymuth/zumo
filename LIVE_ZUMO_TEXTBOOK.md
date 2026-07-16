# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 16, 2026 (Session 41 close — S40 documentation pass: Bible v8.26 = §14.1 TDP-is-notebook + new §18 challenge-design canon. S38/S39/S40 content all LIVE.)
**Status:** 📘 **S41 DOCUMENTATION PASS COMPLETE — BIBLE v8.26** · L01 v03.2.4 · L02 v02.1.1 · L03 v03.2.0 · L04 v04.0.6 · L05 v04.1.6 · L06 v04.5.5 · L07 v04.3.6 · L08 v04.1.4 · L09 v05.0.5 · L10 v02.1.8 · L11 v02.2.1 · L12 v01.2.2 · L13 v02.2.1 · L14 v02.4.1 · L15 v02.2.1 · L16 v02.2.1 · index.html **v1.2.1** · Bible **v8.26** · Maker **v2.28** · Gate **v1.1** · Harness **v3.0** · engine.py · ✅ **S38 + S39 + S40 ALL LIVE** (content, 5 image deletions, ZUMO_TDP_Template.md, favicon.ico — verified by clone) · 📖 **BIBLE v8.26 — §14.1 THE LOG IS THE TDP + NEW §18 CHALLENGE-DESIGN CANON (Saxon spiral · marker convention · starter principles)** · 🎯 **NO lesson/payload/byte changes this session — Bible + LIVE.md only**
**Currently working on:** SESSION 42 = (1) **LEARNER MODE — `L03_C02` Battery Warning next** (`if` voltage < 4200 → "LOW BATTERY!" on OLED; Socratic, coach only, don't hand over the solution; grep Claude's own code vs canon — correct pin `pololu/Zumo32U4@2.0.1`), (2) **PUSH the 16 spiral stars** → `images/` (from `ZUMO_spiral_stars_FINAL.zip`, DJ's hands, not yet up), (3) **QUEUED BOOK TASKS from S40 learner finds:** L03 add "1000 ms = 1 second" · L03 challenge reorder + add Constrain & Ramp (apply §18 spiral going forward) · Coach's Tip upload/power-on sequence · Coach's Tip AI-autocomplete-injects-wrong-code · Maker batch (starters-only bulk download · `?lesson=N` progressive disclosure · C## folder labels · verify `?kind=` = starters) · L01 VS-Code multi-root "Pick a folder" step, (4) **BENCH (need robot):** Q017 L09 green-tape six numbers · Q044 calibration-spin stopwatch · Q046 gyro-bias · L02 §5 green-LED. **PARKED (don't reopen):** challenge solution-disclosure · monetization/ebook · "Know Your Zumo" page · AI Tutor rebuild (LAST).

> **Source of truth = `ZUMO_SUPER_BIBLE.md` (v8.26).** Filename is UNVERSIONED — the version lives ONLY in the internal line. Verify with `grep -oE "Bible version: v[0-9.]+"`.


## 📘 SESSION 41 — S40 DOCUMENTATION PASS (Bible v8.25 → v8.26)

Memory carried the S40 decisions; the FILES had not been updated. This session folded them into durable canon. **No lesson, payload, or byte changes** — Bible + LIVE.md only.

**Bible v8.25 → v8.26 (moderate).**
- **§14.1 THE LOG *IS* THE TDP (NEW):** the 16 Engineer's Log prompts accumulate into ONE growing Google Doc structured as a RoboCupJunior TDP — notebook and TDP are the same artifact. Template = `ZUMO_TDP_Template.md` (repo root, live, carries the v2 edits: solo "Robot & Author", four-turn wheel-base). Prompts stay in the lessons (one source of truth); the Doc holds only TDP scaffolding + PART A standing lists A1–A5.
- **§18 CHALLENGE-DESIGN CANON (NEW SECTION):**
  - **18.1 Saxon spiral** — each lesson's challenges reinforce 1–2 prior concepts alongside the new one; roll out going forward lesson-by-lesson, do NOT retrofit L01/L02; one new concept per rung.
  - **18.2 marker convention** — blue "🔁 Spiraled skills:" header line naming the source in words + inline ⭐ numbered stars (source lesson # inside). Assets `spiral_star_01..16` in `images/` (vector-path numbers, gold gradient) — built S40, DJ-approved, **not yet pushed**.
  - **18.3 starter principles** — minimal skeleton, includes + the ONE needed hardware object pre-placed, empty section headers ("// (none needed for this challenge)"), MY PLAN ships blank, marked "// write your code here" zone, don't re-explain setup()/loop(); challenge folder labels may take a C## prefix (output-string only, keep `kind=` ids, flat).

**Confirmed LIVE by clone (do not re-push):** S38+S39 content, the 5 image deletions, `ZUMO_TDP_Template.md` (root), `favicon.ico` (root).

**Ready to push (DJ's hands):** the 16 spiral stars → `images/` (`ZUMO_spiral_stars_FINAL.zip`).

**Learner mode next:** `L03_C02` Battery Warning (Socratic — coach, don't hand over the solution).

---

## 📗 SESSION 39 — L03 CONTENT PASS + L01 COVER + BIBLE v8.25 (STAGED, NOT PUSHED)

**L03 v03.1.2 → v03.2.0 (moderate).** Display/prose/art only — no payload, byte, gate, or Maker changes. In-file "Version 3" header unchanged (major digit only).

1. **Three new SVGs (book canon).** GRAPHIC 3.16 three turn types (spin/pivot/swing, orange arrows, swing corrected to arc toward the slow side) · GRAPHIC 3.17 math number line (−/0/+ = backward/stopped/forward) · GRAPHIC 3.18 gear train (side view of meshing gears + traced cutaway of the real gear stack showing the ladder on stepped shafts).
2. **Gearmotor photo (IMAGE 3.16, Pololu)** wired into "Feel the gearbox" Try This.
3. **A-Star board image (IMAGE 3.14) dropped** from "Inside the little can," replaced by GRAPHIC 3.18. `git rm images/L03_IMAGE_3-14_astar_board.jpg` at push (DJ ruling: drop, not relocate).
4. **Gear-ratio color code — verified & corrected** (was vague "color is the ratio"): Green 50:1 / **Blue 75:1** / Red 100:1 HP, from Pololu User's Guide 0J63 §1.1. Fleet = blue = 75:1.
5. **GRAPHIC 3.7 fixed** — removed `textLength="560"` that stretched the `setSpeeds(200 + TRIM, 200)` code line (the "weird spacing" DJ spotted; NOT a cache ghost — it was baked into the SVG, lines 63–65).
6. **Prose:** "Test Length"→"test duration" · notebook adds (predict-bias, dead-reckoning, motor-test doc) · TRIM-on-tape + notebook (tape stays) · floor tape → Post-it (TRIM stays tape) · "why 5/10 not smaller" explainer · constrain nuance (library hard-caps ±400 like VEX; constrain protects YOUR math, not the motor) · elevated "ALWAYS STOP YOUR MOTORS" callout · coast/brake/hold explainer (Zumo setSpeeds(0,0) = brake) · expanded stall-current tip (hold-wheels AND too-heavy = same event) · first-open server-pulldown build note · riser coach tip.
7. **Two placeholders left for DJ:** brushed/brushless explainer (§4.2) · 3-Roombas Coach's Note (§4.5). Plus IMAGE 3.4 (terminal-success screenshot) still needed.
8. **Inventory table updated:** 3.14 marked removed; rows added for 3.16 photo + 3.16/3.17/3.18 graphics.

**L01 v03.2.3 → v03.2.4 (minor).** Book-cover image swapped (K&R hardcover → Prentice-Hall paperback, `L01_IMAGE_1-18`, overwrite in place). Lesson_01.html NOT changed — it already referenced that filename; only the image bytes changed. No Lesson_01.html in the push.

**Bible v8.24 → v8.25 (moderate).** Two NEW sections capturing memory-only canon into the durable document (DJ ruling: err toward MORE in the Bible as a memory backup). **§16 HARDWARE GROUND TRUTH** — gear-ratio color code, TRIM=LEFT, setSpeeds ±400 hard-cap + constrain's real job, brake-style stop, stall current (one event two symptoms), encoder averaging, shared pins 20/4, 28,672/2,560 B ceiling. **§17 SVG/GRAPHIC CANON** — 1100×850, blue title band, single-polygon arrows, section colors, IMAGE/GRAPHIC separate number spaces, and the **textLength stretch trap** (only over-stretch is a defect; ~30 SVGs use it — per-file audit DEFERRED, do not blind-replace).

**Non-issues confirmed (no action):** IMAGE 3.4 = still-needed placeholder (not broken) · IMAGE 3.14 = intentionally removed · the "weird spacing" was a REAL defect in GRAPHIC 3.7, now fixed (my earlier "cache ghost" call was wrong).

**Correction within S39:** an initial attempt to move L03's PART-2 prereq box BELOW the green banner broke the S38 banner→section merge (banner squared its bottom but the orange box sat between it and Section 4, reopening the gap). Reverted — the prereq box stays ABOVE the PART bar so the banner merges onto its first section, per S38 canon and matching Parts 1 & 3. No Bible change: S38's "prereq box above the PART bar" rule already governs this.

**S39 = STAGED ONLY,** delivered as `ZUMO_S39_PUSH.zip` (repo layout: lessons/, images/, README). **S38 and S39 must push TOGETHER** — S38 was never pushed. First S40 action = push both, verify by clone.

**New deferred package:** `textLength` SVG audit — 30 files, only over-stretched ones are defects; per-file audit, not a blind sweep.

---

## 📋 SESSION 38 — VISUAL PASS (STAGED, NOT PUSHED)

**All changes are display/layout only. No payload, byte, gate, or Maker changes. Payload gate and byte figures are untouched.**

1. **Title banners unified 16/16.** One template book-wide: dark-top gradient `linear-gradient(to bottom, #1a5276 0%, #2e86ab 100%)`, centered, `border-radius 12px`. Five rows: LESSON NN eyebrow (0.95em, letter-spacing 3px) · title (2.3em, in `<h1>`) · tagline (1.1em, omitted if none) · "Zumo 32U4 Robotics • PlatformIO Edition" · "Version N — Month". Four prior families (centered / left-rail-emoji / inverted L15 / no-version L16) collapsed. Emoji dropped from L11–L14. New titles+taglines authored for L01–L04, L08 (see table below). L02 keeps June 2026; L11–L14, L16 dated July 2026 (inferred — last edit S36/S37).
2. **PART/section bars merged 64/64 (Option C1).** Each PART bar now squares its bottom (`border-radius: 8px 8px 0 0; margin: 22px 0 0`) and caps its first section (section header → `border-radius: 0; margin-top: 0`), forming one connected unit. Colors preserved per part (blue P1 / green P2 / purple P3 / rose P4). Was: two same-color pills with a 34px gap.
3. **L03/L04 prereq boxes relocated.** "WHAT YOU NEED BEFORE STARTING" boxes moved to ABOVE their PART bar (were between bar and section, blocking the merge). L03: two boxes (P1, P2). L04: one (P1). This freed the last 3 unmerged bars → 64/64.
4. **Prereq boxes labeled 6/6.** New id scheme `what-you-need-l{NN}-p{N}`: l02-p1, l03-p1, l03-p2, l04-p1, l05-p1, l09-p1. Previously 4 of 6 had no id; the 2 labeled ones shared ambiguous `what-you-need-1`.
5. **L10 §8A.2 case-body indent fix.** Six lines +2 spaces. Flat/relative-indent census now 0 book-wide (last member of the S37 formatting class).
6. **Landing page (`index.html` v1.2.1).** Robot emoji + wordmark → Mercersburg Academy Robotics mark. Dark variant: lettering white, gear `#b6bbc7` (option C), orange untouched, sits directly on --bg (no plate — white lettering). `<h1>` retained sr-only. Blue/print master kept in images/.
7. **Grok retired.** DJ fired it + cancelled the sub. Its 16/16 review produced 22 claims → 0 builds (all false positives or the book's own sentences quoted back). The "quote-and-grep" tell survives as tool-independent discipline.

**S38 title/tagline table:** L01 Sense, Decide, Act / And Everything That Comes First · L02 Mastering the Code / Reading Code You Didn't Write · L03 Motor TRIM / No Two Motors Are the Same · L04 Line Sensors / Your Robot Cannot See — It Measures · L05 Proximity Sensors / Teaching Your Robot to Sense · L06 Encoders / Teaching Your Robot to Measure · L07 Code Organization / Cleaning Up Your Robot's Brain · L08 Line Following / Proportional Control, and Why Bang-Bang Fails · L09 Intersections & Dead Ends / Teaching Your Robot to Decide · L10 Obstacles / When the Course Fights Back · L11 Time Lies, Distance Doesn't / Encoder-Based Gap Crossing · L12 Wheels Lie / The Gyro — Measuring the Robot, Not the Wheels · L13 Rescue Zone / Flying on Instruments — Navigating Where the Line Cannot Go · L14 Competition Prep / Trust Is Earned at Boot — Reliability as an Engineering Skill · L15 The Present Isn't Enough / PID Control — and the Tuning Bench That Proves It · L16 Nothing Left to Take Away / The Capstone Write-Up

**S38 = STAGED ONLY.** Nothing pushed. First S39 action = push, then verify by clone.

---

## 🌐 THE SITE — `weymuth.github.io/zumo`

```
weymuth.github.io/zumo/
├── index.html                    ← welcome screen (Textbook | AI Tutor)
├── tutor.html                    ← AI Tutor (stale — rebuild LAST)
├── newproject.html               ← Project Maker (v2.28, pending S37 push)
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
| 01 | Hello, Robot! | v03.2.4 | 18 | 0 |
| 02 | Read Code Like a Pro | v02.1.0 | 10 | 2 |
| 03 | Motors & TRIM | v03.2.0 | 14 | 2 + 1 screenshot |
| 04 | Line Sensors | v04.0.5 | 5 | 3 |
| 05 | Proximity Sensors | v04.1.5 | 8 | 3 |
| 06 | Encoders | v04.5.4 | 11 | 0 |
| 07 | Code Organization | v04.3.5 | 7 | 7 |
| 08 | Line Following | v04.1.3 | 3 | 0 |
| 09 | Intersections & Dead Ends | v05.0.4 | 8 | 0 |
| 10 | Obstacles | v02.1.7 | 7 | 0 |
| 11 | Time Lies, Distance Doesn't | v02.2.0 | 4 | 0 |
| 12 | Wheels Lie | v01.2.1 | 3 | 1 |
| 13 | Rescue Zone | v02.2.0 | 2 | 2 |
| 14 | Competition Prep | v02.4.0 | 4 | 2 |
| 15 | The Present Isn't Enough | v02.2.0 | 3 | 0 |
| 16 | Nothing Left to Take Away | v02.2.0 | 3 | 1 |

**Book-wide audit (live tree, S34 close):** zero duplicate ids · zero dead anchors · **zero broken `<img>`** · div balance 0 · 📓 Engineer's Log ×16 · payload gate **PASS** · **zero stale byte counts (all 23 old figures purged, verified by residue sweep on a fresh clone)**.

---

## SESSION 37 — WHAT LANDED

### 🔦 POWER-SWITCH ART + L01 v03.2.1 (Q26 ruling: ON = slide RIGHT, facing the back)
`L01_GRAPHIC_1-13` rebuilt: ON-direction arrow in the switch body, zoomed OFF→ON inset, **green USB power LED added as badge 9** (Pololu: under the center rear edge — a second power light the old art omitted entirely). Prose aligned: "slide it toward the tracks" → "slide it to the right, as you face the back of the robot"; blue-vs-green LED tell added to the power warning; **one-blue-LED = critically drained batteries** note added to the checklist (left blue dims ~3 V — far past the 4,200 mV eneloop floor).

### 🟢 L02 GREEN-LED BENCH CHECK — CLOSED FROM DOCS, NO ROBOT NEEDED
Pololu §3.2: green = TX activity **and** shares a line with the DISPLAY interface; red = RX + display. The book's §5 checkpoint claim was RIGHT for its moment (first upload = USB traffic); the Quick Reference rows were incomplete and now carry the display cause. The planned bench check came off DJ's plate.

### 🧹 THE BIG ONE — BOOK-WIDE FORMATTING REPAIR (Grok's "false positive" reversed)
Grok's vague "formatting issues" flag was REAL: **the good-version code was flat-left** — L02 227/227 lines unindented (`finished` included — students downloaded a flat file from the *structure lesson*), L03 496/496, residues in L04–L07 (incl. L07's whole capstone), while L08–L16 were pristine. Repaired in one coordinated pass:
- **L02 v02.1.0** — 14 good blocks densified (DJ ruling: "go denser") + indented, 6 mystery listings indented (sabotage lines stripped-equality asserted), **prototype teaser** inserted at the Sketch Anatomy row (Grok L02-2, approved). `broken_code` byte-identical — deliberately awful stays awful. Absorbs the green/red QR fix.
- **L03 v03.1.0** — comments already at canon; pure indentation, 496 → 0.
- **L04/L05** — payload-only defects (lessons already displayed indented); files unchanged, **no bumps**.
- **L06 v04.5.4 · L07 v04.3.4** — display-indent fixes (16 + 20 pres) + L07 payload files incl. one body shared byte-identical between steps 6 and 7 (assert-caught, fixed in both slots).
- **Maker v2.27** — 30 payload bodies rewritten by count-asserted escaped-needle surgery; PAYLOADS re-parsed (15 lessons, key sets intact); `node --check` clean.
- **Final census: 6 flat lines book-wide, all in `broken_code` — deliberate.** Zero inheritance ripple (no L04–L07 `finished` changed; L02/L03 verified downstream-independent). Zero byte-figure impact.

### 🛠️ `engine.py` — NEW TOOL, REPO ROOT
Brace-depth indenter (2-space house canon, measured 34,738 vs 268 — the 268 all L05, parked) · raw-indent (markup-untouched, for indent-only work) · flat-only surgical variants · fidelity-testable syntax highlighter (20/20 byte-exact on L02; **escaping styles differ per lesson** — L03 can't be byte-exact re-rendered, hence raw-indent) · payload brace-span/escape surgery. Prose plan blocks excluded by classifier (reindent destroys their column alignment).

### 🔍 GROK TRIAGE (L01 S34-batch + fresh L03)
L01 batch: power-switch art BUILT · debounce + LED syntax confirmed false positives (fix already existed). L03: setSpeeds sign-convention claim FALSE POSITIVE (🔑 box, signed QR ranges, objective, solution confirms convention) · turn-test values FALSE POSITIVE (350 ms @ 150 ≈ 100° ballpark, explicitly "Adjust for 90°!", countdown/constrain/always-stop present) · **EEPROM preview → S38 taste call, decline recommended** (zero EEPROM in L03, book touches it only in L16; persistence already solved by Calibration Record + constants).

### ⚠️ HANDOFF DEFECT FIXED
S37's `git rm` used bare-stem globs that match **zero files** — the real names carry descriptive suffixes. Corrected 5-path command in the S38 handoff.

### 📎 POST-CLOSE ADDENDUM (Q041, DJ-approved)
L03 → **v03.1.1**: one sentence at the Calibration Data Record previewing L16's EEPROM arc — *"Until then, this paper copy IS your EEPROM."* Prose-only; gate re-run PASS. Also post-close: L04 Grok triage — 3 false positives, A+B on-screen hint **DECLINED (Q040)**.

### 📎 POST-CLOSE ADDENDUM 2 — THE FINAL BATCH (DJ: "make all final changes")
Five items, built and verified at close: **Maker v2.28** — skeleton builder's 5 concatenated strings indented (10 flat lines → 0; a fresh blank L04+ project now downloads clean; PAYLOADS byte-identical, asserted) · **L10 v02.1.7** — §8A.2's two flat `case` labels indented to the house Δ+2 (1,979-sample convention) · **L01 v03.2.2** — §5.5 Complete Program's three dropped-indent lines restored at the block's own 4-space · **L07 v04.3.5** — memorization Coach's Tip after the objectives (Q043) · **L12 v01.2.1** — magic-number sentence after the fixed-point code (Q045). Verification: node OK · gate PASS book-wide vs v2.28 · builder census 0 · display census 0 (L01, L10) · div balances 251/240/239/185 all paired · zero byte-figure impact.

### 📖 GROK REVIEW PASS — 16/16 LESSONS, CLOSED
~20 verifiable claims → **2 survivors** (both built above) · 2 DJ taste rulings (L03 EEPROM preview built v03.1.1 · L08 spin-duration pending Q017 stopwatch) · rest false positives, including **three cases of the book's own coined phrases quoted back as suggestions** (leap of faith · "may not refuse the match" · numbers-not-adjectives). Arc-level reads accurate throughout. Structural sweeps alongside the pass found the three real formatting defects Grok cannot see (builder · L10 · L01) — reviewers read content; censuses read structure. Both channels are needed.

### ✅ VERIFICATION
Payload gate **PASS book-wide vs Maker v2.27** (control runs on untouched source first) · INI gate PASS · div balances 332/332 · 282/282 · 203/203 · 239/239 · flat census 6/deliberate · sabotage integrity asserted · `node` re-parse: 15 lessons, zero dangling refs, zero orphans.

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

### 📌 `lib_deps` PINNED — and the book had been teaching the wrong fix
`lib_deps` was **unpinned** (bare `pololu/Zumo32U4`). The registry holds exactly **two** versions — 2.0.0 and **2.0.1 (latest, published 2022-09-07)**. GitHub agrees and stops at 2.0.1. **There is no 2.1.0 and there never was** — the `^2.1.0` pin recorded in L01's §8 table was a typo.

The defect was never the typo. It was **the fix the book published for it: "Remove the version pin."** That traded a typo for a permanent hole, and the fleet has run unpinned ever since. **A bad pin is fixed by pinning correctly, never by unpinning** — and this book cannot afford the hole: it publishes exact byte counts against a **28,672 B ceiling with 638 B of headroom on L15**. A library update doesn't make a figure stale; it pushes a student's build over the wall while the lesson insists it should have fit.

Now `lib_deps = pololu/Zumo32U4@2.0.1` — **EXACT**, not `^2.0.1` (a future 2.1.0 would satisfy the caret and land silently). **Zero byte impact** — 2.0.1 is already what resolves today. L01 teaches the pin, and its troubleshooting row now reads: *that version does not exist; run `pio pkg show pololu/Zumo32U4` instead of guessing a number.* Also repaired: **L01's two `platformio.ini` code blocks disagreed with each other** — one inline, one split across two lines, and only one matched what the Maker writes. **New gate:** the `lib_deps` line must be byte-identical in the Maker template and every lesson `<pre>`. **PASSES.**

### 📦 BIBLE §12 REWRITTEN — DELIVERY CANON WAS NEVER WRITTEN DOWN
§12 was **stale**: it told a new session to *upload* the Bible (it lives in the repo — it is cloned) and named a handoff file that does not exist. It also carried **no delivery canon at all** — `PUSH_WORKFLOW.md` had said since S34 that *"root docs all go up together, in one shot,"* but the Bible never captured it, and S36 duly split the delivery into a "push zip" and loose project-folder files. Wrong. **EVERYTHING LIVES IN THE REPO** — Bible, LIVE.md, handoffs, gate scripts, harness, web tools, lessons, images. Session open = **clone**. Session close = **ONE zip, full repo layout, every changed file including root docs** — one extract, one commit, one push. **A zip cannot delete:** removals ship as explicit `git rm` lines in the close note.

Also fixed a trap of my own making: §12.1 documents the session-open grep, so `grep -o "Bible version: v[0-9.]*"` began **matching its own example** and returning a bogus second line. The ritual now uses `grep -oE "...v[0-9.]+"` — the `+` requires a digit, so the example cannot self-match. *(Anywhere the old greedy `*` form survives, it will return two lines. Use `-oE` and `+`.)*

### ✅ VERIFICATION
Payload gate **PASS, all 15 lessons**, control run on untouched source first · **INI-consistency gate PASS** · **99 links / 99 kinds, 1:1** · Maker parses, zero dangling refs, zero orphan payloads · byte-residue sweep intact (S34 audit preserved) · structure balanced, zero heading churn · push verified by fresh clone (md5, all 7 files).

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

## S38 AGENDA

1. **Q017 — L09 green-tape bench check** (procedure + decision table in the handoff; a constant change is EXPENSIVE — payload chain L09→L15).
2. **Q037 — L01 "Coming from Arduino?" callout ruling** (approve/modify/drop; no skip lane either way).
3. **Grok L03 EEPROM-preview taste call** (decline recommended).
4. **Repo cleanup — corrected 5-path `git rm`** (in the handoff, if not already run).
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

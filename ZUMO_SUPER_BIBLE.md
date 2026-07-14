# ZUMO SUPER BIBLE v8

**Bible version: v8.20** — increment on EVERY substantive edit (moderate change → `v8.x`; minor fix → `v8.x.y`; a new major re-baseline → `v9`). **Filename is now unversioned: `ZUMO_SUPER_BIBLE.md`** — the version lives ONLY in this line, never in the filename (this avoids a fresh chat misreading a filename number as the version). Current: **v8.20** (v8.20, per S33 DJ rulings: **§9 UNIQUE VERSION PER DELIVERY** (retires the fix-to-a-fixed-version rule) · **§9 image changes are a MINOR bump** · **§10 IMAGE and GRAPHIC are SEPARATE NUMBER SPACES; audit art against `images/`, never against the lesson alone** · **§13 BATTERY CANON — eneloop NiMH** · **§14 ENGINEER'S LOG — 16 prompts, one per lesson**. Prior: **v8.19** (v8.19, per S28+S32 DJ rulings: **16-LESSON RENUMBER SWEEP** — §1 filename table, §3 LESSON MAP, §0 items 5/6 8A map, tier-card example, and image-phase count moved from the 15-lesson to the 16-lesson numbering (L12 "Wheels Lie" inserted S28, shifting Rescue Zone→13, Competition Prep→14, Advanced PID→15, Showcase→16; L11 retitled "Time Lies, Distance Doesn't"; L15 retitled "The Present Isn't Enough" S31; L16 retitled "Nothing Left to Take Away" S32). 8A map re-verified against published files July 13, 2026: PRESENT L02–L15, ABSENT L01 and L16. Renumber only — no rule changes. Prior: v8.18 (v8.18 adds, per S28 DJ ruling: **§11 EXTRACT THE INHERITANCE — DO NOT RECONSTRUCT IT.** A depth pass on lesson N BEGINS by pulling lesson N-1's `finished` payload out of `newproject.html` (`PAYLOADS["N-1"]["finished"]`) — that is the project students actually hold in their hands. Rebuilding the base from lesson HTML, from a sibling lesson, or from memory SILENTLY DROPS FILES. Canonized after S28 reconstructed the L11 base as SIX files, omitting `RobotHelpers.h`/`RobotHelpers.cpp` — the STANDARD HELPERS (`waitForStart()`, `checkBattery()`) that have shipped in EVERY project since Lesson 4 — and built 21 compile-verified states on that broken inheritance before catching it. A student would have opened the lesson project and found their SAFETY GATE GONE. The project is EIGHT files: RobotConfig.h, RobotSensors.h, RobotSensors.cpp, RobotHelpers.h, RobotHelpers.cpp, RobotMotion.h, RobotMotion.cpp, main.cpp. GATE CHECK: assert `len(files)==8` on every state. The 21 states were discarded and rebuilt from the real payload; the corrected base compiles at 22802 bytes, byte-exact to S27's recorded L11 `finished` — which is how provenance was confirmed. THE MAKER REGISTRY IS THE AUTHORITATIVE INHERITANCE SOURCE. Prior: v8.17 (v8.17 adds, per S25 DJ rulings: **§11 A DECLARED STUDENT BLANK MUST BE SPENT** — if a lesson ships a tunable as a blank (`const int TRIM = 0;   // <-- YOUR NUMBER`), the code MUST actually USE that constant. A blank the code never reads is a LIE in the worksheet: the student writes in a number, nothing changes, and they lose faith in the instrument rather than in their own guess. Canonized after S25 found §7B/7C/7D of L10 declaring `TRIM` and never passing it to `setSpeeds()` — the same defect class as L09's false claim that `turnDegrees()` "respects TRIM." GATE CHECK: grep every lesson for declared-but-unread tunables. **BLANK CONVENTION (DJ-ruled S25):** tunables ship as `= 0` with the starting guess in the COMMENT (`const int TURN_MS = 0;   // <-- YOUR NUMBER. Try 400 and work from there.`) — a seeded value looks like an answer and students accept it without hunting; a bare `0` with no hint means the robot does not move and the student has no bracket to start from. **§11 IDENTICAL BYTE SIZES — THE CONSTANT EXCEPTION** — the S22 rule ("identical binary sizes across states = `--gc-sections` discarding dead code") applies to added LOGIC, NOT to changed CONSTANTS. `speed + TRIM` with `TRIM = 0` constant-folds to `speed` and emits byte-identical code; the fix IS live, it simply costs nothing until the blank is filled. Do NOT conclude an edit vanished from a zero byte delta — DISASSEMBLE (`avr-objdump -d`) and read the immediates. S25 proved TRIM live in L10 §7D this way: `ldi r24, 0x96` (150) became `ldi r24, 0x9E` (158) with the right motor unchanged at 150 — same instruction, same size, correct LEFT-motor polarity. Sabotaged-build states that flip a sign or change a constant are the same case. **§11 SABOTAGED BUILDS SHOW THE PLANTED LINE** — Bonus mysteries display the sabotaged code inside the hint ("The planted constant:" / "as planted:"). The mystery is NOT "find the typo" — it is "why does THIS line produce THAT symptom," which is the actual debugging skill. This also satisfies the payload byte-match gate by construction (L09 canon, formalized S25). Prior: v8.16 (v8.16 added, per S23 DJ rulings: **§4 QUICK LINKS RETIRED** — book-wide; navigation canon = section banners + one `↑ Back to top` per section; a Quick Links jump-list duplicates the banners and rots on every renumber (only 4/15 lessons had one; L08/L09 — the freshest depth passes — never did). **§11 TRIM PLACEMENT RULE** — TRIM belongs in every OPEN-LOOP straight line (`driveDistance()`, `handleGap()`, timed maneuvers) and NOWHERE else: NOT in `turnDegrees()` (the wheels oppose on purpose; encoders govern the angle) and NOT in `followLine()` (P-control is a CLOSED loop already correcting bias 50x/sec — TRIM would fight it). Open-loop needs TRIM; closed-loop does not. Polarity is LEFT-motor: `setSpeeds(speed + TRIM, speed)`, positive TRIM speeds the left wheel, robot pushes RIGHT, correcting a LEFT curve — verified against Pololu `FaceTowardsOpponent.ino` (`turnRight()` = `setSpeeds(+turnSpeed, -turnSpeed)`; a robot curves toward its SLOWER track). **§11 ENCODER AVERAGING RULE** — distance/turn loops MUST gate on the average of BOTH encoders, never one: `while (averageCounts() < target)`. Watching a single encoder means a slipping or stiff wheel on the other side ends the move early or late and nothing warns you. **§5b IN-FILE VERSION = MAJOR DIGIT ONLY** — the header/footer "Version N" carries the major digit; the full `v##.#.#` lives ONLY in the filename (canonized after finding L04 shipped with header "Version 3" against footer+filename "4"). Prior: v8.15 (v8.15 added, per S22 DJ ruling: §11 payload-gate INHERITANCE RULE — lesson N's payload corpus additionally includes lesson N−1's `finished` payload bodies, because inheriting lessons copy the prior project wholesale in Step 1. Prior: v8.14.1 (v8.14.1 added, per S21 DJ ruling: §11 dark-wrapper scope check — canonized after the S21 L03 find where a `#1e1e1e` wrapper missing its closer swallowed four Quick Reference tables and passed both div-balance AND the depth walk, because the closer existed ~200 lines late. Prior: v8.14 (v8.14 adds, per S20 DJ rulings: §11 payload byte-match gate — canonized from the S18-approved Maker starter-code-registry rule; §11 bounded-scope replace assert — canonized after the S20 L03 B1/B2 regex incident; §4 "Bonus" vocabulary canon — book-wide term for the extra-practice section, nav labels must match. Prior: v8.13.1 (v8.13 adds: hardware-direction verification against Pololu examples; L04+ STANDARD HELPERS — waitForStart safety gate + A&B battery check; lesson-aware Maker skeleton; web-tool internal versioning. v8.13.1 completes the v8.13 delta: §11 ASCII-sweep checklist item — EDIT 5, dropped in the initial application — plus §5b header tag corrected v8.12→v8.13)))))))).

---

## ASCII ART POLICY (v8.6 — canon)

**No ASCII-art diagrams anywhere in lesson content.** All diagrams are either Claude-produced SVG (`[GRAPHIC x.y]`) or DJ-sourced raster (`[IMAGE x.y]`).

- Applies to box-drawing/arrow diagrams in `<pre><code>` blocks AND to annotated code-anatomy diagrams (pointer/arrow lines inside code blocks) — those count as ASCII art.
- Replacement mechanism: swap the ASCII block for a `[GRAPHIC x.y] caption` placeholder in the lesson's own dashed-div placeholder format; DJ inserts the SVG file in Canvas.
- Existing ASCII art is converted per the ASCII→SVG tracker in `LIVE_ZUMO_TEXTBOOK.md`.
- Plain code (no drawing characters) in `<pre>` blocks is unaffected.

**MANDATORY DIFF-AUDIT GATE (v8.7).** Before saving any modified lesson file: run a full old-vs-new diff and confirm every changed line is explained by the intended edit — removed lines, added lines, and byte/line-count deltas must all reconcile. Structural checks (anchors, div depth) cannot detect content loss when the deleted content has no inbound links; only a diff can. Rebuild from the md5-verified `/mnt/project/` source, never from a prior working copy. (Canonized after a Session-8 regex overmatch silently deleted ~13KB from L02.)


**The single, definitive source of truth for the Zumo 32U4 Robotics Textbook.**

**Supersedes:** `Zumo_Super_Bible_V7.md` AND `Zumo_Textbook_Standards.md` (both retired). If anything in an older file disagrees with this document, this document wins.

**Last updated:** July 2, 2026 — **v8.5.1** (Session 3: (1) §8A VERIFIED for L2–L5 — all four PRESENT (L2 Functions, L3 Calibration, L4 Sensor Arrays, L5 Sensor Pairs); §8A map is now PRESENT L2–L12, ABSENT L1/L13/L14/L15. (2) Back-to-top standardized to `#2e86ab` book-wide; canon anchor = `<a href="#top" style="color: #2e86ab;">↑ Back to top</a>` (plain, no extra props); L4 footer `href="#"` fixed to `#top`. (3) L2/L3 `&nbsp;` removed (inline code → `white-space:pre-wrap`; rating scale → inline-margin pipe spans). (4) 8 files minor-bumped to v#.0.1: L1 v03.0.1, L2/L3/L4/L5/L7/L8 v02.0.1. (5) IMAGE CONVENTION added: placeholders Claude can author as SVG diagrams are renamed `[GRAPHIC x.y]`; DJ-supplied raster stays `[IMAGE x.y]`.) Prior June 29, 2026 — **v8.5** (Session 2 close, after L10–L15 built: (1) §6.12 added 5th difficulty tier COMPETITION `#b7950b` gold; (2) §8A rule changed from "all lessons except L1" to CONDITIONAL — 8A present only when a genuine reusable coding pattern exists: absent in L1/L13/L14/L15 confirmed, L2–L5 to verify; (3) §6.12 documented §9 tier-card variant (Bronze/Silver/Gold medal border-top) for project-tier content per L15; (4) noted the one-time v8 "reset every lesson to v01" is DONE — versions now increment only. Prior v8.4: code-block spacing extended §6.11: added line-height 1.8 + no-blank-line-doubling rule, padding confirmed 15px across all 9 lessons. Prior v8.3.1: (back-to-top spec §6.1b: one per section, standard color `#2e86ab`, depth-aware insertion. Prior v8.3: (responsive two-column rule §6.1a: side-by-side comparisons must use `repeat(auto-fit, minmax(280px,1fr))` not fixed `1fr 1fr`, so they stack on narrow screens without media queries. Prior v8.2: (code-block spacing locked: padding 15px + margin 16px 0, no double-semicolons, normalize wrapper-div blocks; §11 checkbox check upgraded to an explicit GATE scanning all `<ul>`/`<ol>` variants. Prior v8.1: (SECTION-COLOR SPLIT + 4-PART STRUCTURE: §9 Challenges promoted to its own PART 4 in plum `#9b6a9e` (split out of the old rose §7–9 group); §7/§8/§8A stay dusty rose as PART 3. Locked: challenge-card canon (§9 carded format), gradient-vs-solid role rule (§6.2a), checkbox-XOR-bullet rule, orphan-banner ban, Exit Ticket checkbox-only + bold-Q&A, blue h3 subheadings reinforced. Supersedes the 3-PART / rose-§7–9 scheme. ALSO: subheadings (h3/h4) + table headers now adopt the SECTION GROUP COLOR (§6.5 table) — supersedes the old global-blue h3 / navy table header. Prior: L4–L8 retrofitted; §11 hardening checks; glossary term-card format)

**SVG build-path rule (added v8.11, from the L02 GRAPHIC 2.9 incident):** SVG files must be authored through an escape-processing write path (e.g., Python string → file), NEVER a raw-text path — raw-written `\uXXXX` sequences render as literal garbage text in the diagram. Mandatory SVG QA before presenting: (1) literal-`\u` scan of the saved file must be clean; (2) render the SVG and verify, and when visual preview is unavailable, verify layout numerically (e.g., pixel-scan for overlap in gaps). Corollary for hosted HTML tools (timer, Project Maker): `\uXXXX` escapes are legal ONLY inside JavaScript string literals — the HTML text region must be escape-free (use entities or literal characters).

---

## 0. WHAT CHANGED IN v8 (READ FIRST)

v8 is a **re-baseline**. The previous Bible (v7) and the separate Standards doc had drifted from the actual lessons and from each other (they disagreed on section count and skin). v8 resolves that. The decisions below are LOCKED:

1. **Canonical skin = the "Lesson 9 look" + section CAP+BOX design** (Segoe UI, blue gradient nav/title; every section is a colored cap on a matching bordered box). Defined fully in §6. Supersedes the old v7 serif/flat-nav style guide.
2. **Nav/title gradients are top-down, dark-first** (`linear-gradient(to bottom, <dark> 0%, <light> 100%)`). **PART dividers are now SOLID group colors** (blue/green/rose), not the old navy gradient (retired). **Section cap+boxes and PART banners follow the nav color scheme:** §1–3 blue `#3498db`, §4–6 green `#3a7d5c`, §7/§8/§8A dusty rose `#c45d76`, **§9 plum `#9b6a9e`**, §10+end gray `#6c757d`. (§9 split into its own PART 4 — see §6.8.) **Code blocks are dark** (VS Code/PlatformIO theme, §6.11).
3. **Icon legend = 12 icons** (the set in §6.6), using "⚠️ WARNING."
4. **No icon before the title-block heading** (`LESSON ##`, not `🚧 LESSON ##`). Section headers (`📖 Section 1: …`) keep their icons.
5. **Structure = 10 sections, §8A CONDITIONAL.** 8A is present ONLY when a lesson isolates a genuine reusable coding pattern — it is NOT universal. (See §4.) **8A MAP:** PRESENT in L2–L15. ABSENT in L1 and L16. (Re-verified against every published file July 13, 2026.)
6. **Lessons with no 8A:** L1 (install/setup) and L16 (capstone/showcase). Their PART 3 subtitle = "Sections 7–8: Verify and extend" (no 8A). §9 is still its own PART 4 (plum) in every lesson. A "Functions Reference" subsection can go EITHER way — become §8A OR fold into Quick Reference — author's per-lesson call.
7. **Two spec files → one.** `Zumo_Textbook_Standards.md` is retired; its content is folded here.
8. **Filename convention:** `Lesson_##_Topic_v##.html` — zero-padded lesson number, zero-padded lowercase version. See §1.
9. **Re-baseline version reset (COMPLETE):** at the v8 transition, every lesson reset to `v01` — this one-time reset is now DONE (all 15 lessons built to v8.4, L10–L15 at v01, dates normalized to June 2026). The normal increment-only rule (§9) now applies to ALL lessons. **DO NOT reset any lesson's version or re-normalize dates again — only increment forward.**

---

## 1. FILE NAMING CONVENTION

**Pattern:** `Lesson_##_Topic_v##.html`

- `##` = zero-padded lesson number (`01`, `02`, … `15`)
- `Topic` = fixed topic token (underscores, mixed case) — see table below
- `v##` = zero-padded, **lowercase** `v` + zero-padded version (`v01`, `v02`, …)

**Examples:** `Lesson_01_Hello_Robot_v01.html`, `Lesson_10_Obstacles_v01.html`, `Lesson_16_Nothing_Left_to_Take_Away_v02.html`

**Locked topic tokens (all 15):**

| # | Topic token |
|---|---|
| 01 | `Hello_Robot` |
| 02 | `Read_Code` |
| 03 | `Motors_TRIM` |
| 04 | `Line_Sensors` |
| 05 | `Proximity_Sensors` |
| 06 | `Encoders` |
| 07 | `Code_Organization` |
| 08 | `Line_Following` |
| 09 | `Intersections` |
| 10 | `Obstacles` |
| 11 | `Time_Lies_Distance_Doesnt` |
| 12 | `Wheels_Lie` |
| 13 | `Rescue_Zone` |
| 14 | `Competition_Prep` |
| 15 | `The_Present_Isnt_Enough` |
| 16 | `Nothing_Left_to_Take_Away` |

The old `_Rebuilt_` / `_Canvas` / `_StandardCallouts_StickyNav` suffixes are **retired**. All files move to the clean pattern above at the v8 re-baseline.

---

## 2. CURRICULUM PHILOSOPHY (unchanged from v7)

- **Depth before breadth.** Each concept fully developed before moving on.
- **Coach voice.** Friendly, professional, "B-level" explanations. No flattery.
- **Theory-first, then scaffolded build.** Theory section is pre-reading; Build It is hands-on.
- **Progressive autonomy.** Each lesson copies the previous project folder and adds one capability.
- **Audience:** high school freshmen, zero coding experience. Platform: PlatformIO + VS Code (not Arduino IDE).
- **Information density:** "more is better" — comprehensive over simplified.

---

## 3. LESSON MAP

| # | Topic | 8A? |
|---|---|---|
| 01 | Hello Robot | ❌ none (intro/setup) |
| 02 | Read Code Like a Pro | ✅ yes (Functions) |
| 03 | Motors & TRIM | ✅ yes (Calibration) |
| 04 | Line Sensors | ✅ yes (Sensor Arrays) |
| 05 | Proximity Sensors | ✅ yes (Sensor Pairs) |
| 06 | Encoders | ✅ yes |
| 07 | Code Organization | ✅ yes |
| 08 | Line Following (P-Control) | ✅ yes |
| 09 | Intersections & Dead Ends | ✅ yes |
| 10 | Obstacles | ✅ yes (Sub-States) |
| 11 | Time Lies, Distance Doesn't | ✅ yes (Dead Reckoning) |
| 12 | Wheels Lie | ✅ yes |
| 13 | Rescue Zone: Flying on Instruments | ✅ yes |
| 14 | Competition Prep | ✅ yes |
| 15 | The Present Isn't Enough (PID) | ✅ yes (Concepts) |
| 16 | Nothing Left to Take Away (capstone) | ❌ none (capstone; §9 = tier-cards) |

---

## 4. LESSON STRUCTURE — LOCKED

**Vocabulary canon (v8.14, DJ-ruled S20): the extra-practice section is called "Bonus"** — book-wide, in section headers, nav pills, Maker dropdown group labels, and prose. "Enrichment" and "Extra Practice" are rejected alternates; any nav label pointing at the Bonus section must read "Bonus" (an L02 nav pill reading "Extra Practice" was the drift that triggered this ruling).

### Core 10 sections (every lesson)

1. **Intro** — engaging problem/scenario that motivates the lesson
2. **Objectives** — learning objectives checklist
3. **Theory** — background concepts, subsections 3.1, 3.2, … (lesson-specific design concepts live here)
4. **Hardware** — physical setup, sensor specs, calibration notes
5. **Code** — walkthrough of key functions/concepts (project org, constants/functions tables, function reference)
6. **Build It** — step-by-step implementation with checkpoints
7. **Test** — verification checklists, tuning guide
8. **Troubleshoot** — problem/cause/solution
9. **Challenges** — Easy/Medium/Hard escalation with collapsible solutions
10. **Exit Ticket** — 3-h4 structure (see §7)

**End matter (after section 10):** Glossary → Quick Reference → Image Index. Headings use the locked icon set: **📖 Glossary**, **⚡ Quick Reference**, **🖼️ Image Index** (border `#6c757d`).

**Glossary entry format (LOCKED):** each glossary term is a **term card** — `<div style="background-color: #e7d4ff; border-left: 4px solid #9b59b6; padding: 15px; margin: 15px 0; border-radius: 8px;">` then `<span>🔑</span> <strong id="term-...">Term</strong> — definition.` This is the ONE canonical glossary palette/format. Do NOT use Key-Term-callout purples (`#f3e5f5`/`#9c27b0`) or any other purple (`#f3e8f9`/`#7b2d8e` etc.) for glossary entries — those drifted across L1/L2 and were normalized. Term cards stay `8px` (the radius exception); inline Key Term *callouts* in the body remain `#f3e5f5`/4px and are a different element.

### Section 8A (CONDITIONAL — only when a reusable coding pattern exists)

8A houses a **reusable coding pattern** — something a student will reuse in later lessons (function parameters, return values, error handling, state machines, non-blocking timing, etc.). It is distinct from Theory: Theory holds lesson-specific *design* concepts; 8A holds transferable *code* patterns.

**Rules when 8A is present (L2–L15):**
- Placed **between Section 8 (Troubleshoot) and Section 9 (Challenges)** in DOM order.
- Appears in nav as a button ("8A. Concepts" or similar), dusty rose color `#c45d76`.
- 8A is part of **PART 3** (dusty rose, with §7/§8). PART 3 subtitle = "Sections 7–8A: Verify and extend". (§9 is now its own PART 4 in plum — see §6.8.)
- `<h2 id="section-8a">` carries the dusty rose color `#c45d76` (8A stays rose; only §9 moved to plum).
- Section ID order: `1, 2, 3, 4, 5, 6, 7, 8, 8a, 9, 10, glossary, quick-ref, image-index`.

**Presence rule (CONDITIONAL):** 8A is present ONLY when a lesson isolates a genuine reusable coding pattern — NOT in every lesson. **8A MAP:** PRESENT in L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12; ABSENT in L1, L13, L14, L15. (L2–L5 verified present July 2, 2026.) Lessons without 8A use PART 3 subtitle "Sections 7–8: Verify and extend". §9 Challenges (PART 4, plum) is present in every lesson including those without 8A. A "Functions Reference" may become §8A (L12) OR fold into Quick Reference (L14) — author's per-lesson call.

### Theory (§3) vs Build It (§6) — the "Build It" approach

Explanation is immediately followed by implementation (not separated into distant sections). This is intentional, not a deviation.

---

## 5. CODE STANDARDS (unchanged from v7 — summary)

- **6-file project architecture:** `main.cpp`, `RobotConfig.h`, `RobotSensors.h/.cpp`, `RobotMotion.h/.cpp`.
- **Hardware objects** defined once; use `extern` elsewhere. `Zumo32U4OLED` (not `Zumo32U4LCD`).
- **`#define` for pin numbers only; `const` for all other values.** camelCase enforced (`baseSpeed`, `lineLostTime`).
- **Serial baud rate: 115200.** Include `Serial` timeout guard in `setup()`.
- **Single sensor read per loop** — store raw values once at loop top, reuse. Multiple `lineSensors.read()` calls (~12–15ms each) cause green-tape detection failures.
- **Non-blocking timing only** — never `delay()` in a state machine; use `millis()` timers. (This is the L10 8A topic.)
- `followLine()` lives in `main.cpp` only.
- A-Star32U4 capitalization for the microcontroller.
- **Function prototypes (v8.12 — MANDATORY):** helpers live at the BOTTOM of `main.cpp` (anatomy Section 7); every helper gets a one-line prototype in a `// ===== FUNCTION PROTOTYPES =====` block right after the hardware objects. PlatformIO `main.cpp` is real C++ — no `.ino` auto-prototypes; define-below-loop without a prototype DOES NOT COMPILE. Teaching pattern = deliberate break-fix (L02 STEP 7).
- **Native-USB serial canon (v8.12):** the Zumo's `Serial` is USB CDC — the baud number in `Serial.begin()` is effectively ignored; a mismatch does NOT produce garbage on this robot (that's UART boards like the Uno). NEVER teach baud-mismatch gibberish as a Zumo symptom. Print-at-boot is invisible (reset drops the USB port) — prints go in `loop()` or behind a button press. We still write `Serial.begin(115200)` as professional habit.
- **Compile-verify mandate (v8.12):** every new or changed lesson code block (steps, final programs, challenge solutions, bonus snippets, template skeleton) must compile on the AVR harness before delivery. Harness: avr-gcc + `arduino/ArduinoCore-avr` + `pololu/zumo-32u4-arduino-library` + deps (Pushbutton, FastGPIO, PololuBuzzer/HD44780/Menu/OLED, USBPause, core Wire), Leonardo-class env, `-mmcu=atmega32u4 -DF_CPU=16000000L`. Rebuild from GitHub clones each session. A lesson whose build sequence never compiled shipped twice (L02 ≤ v02.0.6) — this rule exists so it can't happen a third time.

---


**HARDWARE-DIRECTION VERIFICATION (v8.13 — after the L03 TRIM-inversion incident).** Any claim that maps left/right, forward/backward, or turn direction to motor commands MUST be verified against the Pololu library's own example code before it ships — e.g., `FaceTowardsOpponent.ino` implements `turnLeft()` as `setSpeeds(-turnSpeed, turnSpeed)` (right faster ⇒ turns LEFT; a robot always curves toward its slower track). A lesson that is internally consistent can still be physically backwards — L03 taught inverted TRIM logic for its entire life until S15. Internal consistency is not verification; the library examples are ground truth Claude can check without hardware.

## 5b. STUDENT PROJECT WORKFLOW & WEB TOOLS (v8.13 — LOCKED)

**Template workflow:** `ZUMO_Template/` lives in `Documents/PlatformIO` — built by students at the END of L01 (block canon in L01 v03.0.23), never worked in, only copied. Contents: canonical `platformio.ini` + skeleton `main.cpp` (header stub, all section banners incl. FUNCTION PROTOTYPES, empty setup/loop) + README ritual. Rescue copy = `ZUMO_Template.zip` at repo root.

**Start-a-New-Lesson ritual (standard §4 block, EVERY lesson L02+):** 1) Project Maker → download 2) unzip into Documents/PlatformIO 3) VS Code File→Open Folder (close old folder first) 4) header comment check (Maker pre-fills; update WHAT-THIS-DOES as you build) 5) Build ✓ health check. Manual fallback: copy template + rename by hand. iCloud caution: keep the PlatformIO folder downloaded/local.

**Naming canon (DESCRIPTIVE — supersedes `LastName_Lesson_##` and all letter-suffix schemes):**
- Main lesson build: `LastName_L##` (zero-padded; first initial for duplicate last names: `SmithJ_L02`; NO SPACES ever)
- Mystery sandbox: `LastName_L##_Mystery` — ONE per lesson, reused across its mystery challenges
- Challenge/bonus copies: `LastName_L##_<Challenge_Name>` (e.g. `Smith_L02_The_Broken_Code`, `Smith_L02_Blink_Count`)
- Copy per LESSON, never per step. Additive §9 challenges work in the main build; code-replacing challenges and bonus snippets get their own copy. Every challenge card carries a "📁 Work in:" line naming the exact destination, with a Maker deep link when a new folder is needed.

**Web tools (GitHub Pages, weymuth.github.io/zumo/) — Canvas strips `<script>`, `onclick=`, `<style>`, `class=`; ALL interactivity ships as Pages-hosted iframes:**
- `timer.html` — horizontal bar countdown (336×56 right-float, `?min=&label=`, cache-bust `?v=N` on every timer redesign). One per timed challenge.
- `newproject.html` — ZUMO Project Maker: generates correctly-named project zips with pre-filled header comments. Carries a per-lesson challenge registry — **EXTENDING the registry is a mandatory step of every lesson depth pass.** Deep-link format: `?lesson=N&kind=<slug>`.
- Printable graphics: PDF generated from the approved SVG, hosted in repo `images/`, linked via a styled download button in the lesson (this SUPERSEDES dedicated "printable version" GRAPHIC slots — L02 GRAPHIC 2.3 precedent).

**Sketch anatomy canon:** **7 numbered sections + one UNNUMBERED "FUNCTION PROTOTYPES" row** between Constants and setup() (dashed rail marker in GRAPHIC 2.5; color key shows it as an open square in Helpers blue). The count stays "seven sections" book-wide — do NOT renumber to eight.

---

### STANDARD HELPERS — L04+ (v8.13 — LOCKED)

From Lesson 04 onward, every Maker-generated skeleton (all kinds: main, challenge, custom) ships with a **STANDARD HELPERS (added after Lesson 3)** block at the file bottom, with prototypes declared in the FUNCTION PROTOTYPES section (the template itself models the L02 layout canon). Lessons 01–03 stay clean — those lessons teach the pieces. The two helpers, compile-verified (13,002 B on the harness):

- **`waitForStart()`** — SAFETY GATE. OLED shows "Press A / to start"; `buttonA.waitForButton()`; clear + `delay(500)` to get hands clear. Called at the END of `setup()`, always. **Canon rule: from L04 on, no driving program ever moves at power-on — motion waits for a button press.** Depth passes on L04–L15 must adopt this in their main builds.
- **`checkBattery()`** — A+B BATTERY CHECK. Hold Buttons A + B together at any time: OLED shows battery millivolts while held, waits for release, clears. Called at the TOP of `loop()`. **Canon rule: A+B held = battery check, book-wide from L04.** No permanent screen space is reserved for battery (supersedes any row-0 reservation idea). Uses only L03 knowledge (combo-press pattern = L03's A+C reset precedent).

Manual fallback ritual for L04+ (no internet): copy ZUMO_Template, rename to `LastName_L##`, **and paste the STANDARD HELPERS block** (lessons provide it in a copyable dark box during their depth passes). `ZUMO_Template.zip` itself stays the clean L01 version — it is the teaching artifact.

### WEB-TOOL VERSIONING (v8.13 — LOCKED)

Web tools (`timer.html`, `newproject.html`, future tools) keep **unversioned filenames** — lesson deep links and iframes depend on them. The version lives ONLY inside: a header comment with the full version chain, plus a small visible footer line where layout allows (Maker shows "Project Maker v1.3"). The `?v=N` query token in lesson iframe URLs is a **cache-buster, not a version** — it bumps on every push and drifts from the internal version by design. Versions follow the standard scheme (v# / v#.# / v#.#.#) and are tracked in LIVE's web-tools line. Current: timer v1.2 (bar design), Maker v1.3 (lesson-aware skeleton).

## 6. CANONICAL SKIN (v8 — LOCKED) — "THE LESSON 9 LOOK"

> This section **supersedes** the entire v7 "HTML Style Guide" (v7 §6). The old serif body, flat `#2c3e50` nav, `135deg`/`to right` gradients, and Part-colored dividers are **retired**. Reference implementation for the skin: `Lesson_09` (as rebuilt). All lessons conform to this.

**All styling is true inline** — every element carries its own `style=""`. No `<style>` blocks, no CSS classes (Canvas strips them).

### 6.1 Body

```html
<body id="top" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.7; max-width: 900px; margin: 0 auto; padding: 20px; color: #333; background-color: #fafafa;">
```

- Font: **Segoe UI** sans-serif stack (NOT Georgia/serif).
- Background: `#fafafa`.
- `id="top"` on the body so "Back to top" links resolve to `#top`.

### 6.1a Two-column layouts must be responsive (LOCKED v8.3)

Any side-by-side two-column comparison (e.g. `.h` vs `.cpp`, MISTAKE vs CORRECT, BEFORE vs AFTER) MUST use a self-stacking grid — NOT a fixed `1fr 1fr`. Canvas strips `<style>`, so no media queries; use `auto-fit` + `minmax` instead, which stacks to a single column on narrow screens with pure inline CSS:

```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">
```

- **Banned:** `grid-template-columns: 1fr 1fr;` — forces 2 columns at every width and overflows the right border on phones/narrow panels (dark code blocks don't shrink).
- **Required:** `repeat(auto-fit, minmax(280px, 1fr))` — 2 columns when there's room (≥~580px), auto-stacks to 1 column when narrow.
- Flex two-column layouts must carry `flex-wrap: wrap` for the same reason.
- §11 check: FAIL if any `grid-template-columns: 1fr 1fr` (or other fixed multi-column track list without `auto-fit`/`minmax`) exists.

### 6.1b Back-to-top links (LOCKED v8.3.1)

Every section (and end-matter section) carries exactly ONE "Back to top" link at the end of its box, right before the box-closing `</div>`:

```html
<p style="text-align: right;"><a href="#top" style="color: #2e86ab;">↑ Back to top</a></p>
```

- **Standard link color: `#2e86ab`.** (Some lessons historically used `#3498db`; normalize to `#2e86ab` on next touch.)
- Exactly one per section — no strays mid-section, none missing. Insert via a depth-aware walk (each section box from open to its matching close), not a fragile "nearest `</div>`" search.
- Target is `#top` (the `id="top"` on `<body>`).


### 6.2 Gradient rule (applies everywhere)

**All gradients are top-down, dark color first:** `linear-gradient(to bottom, <DARK> 0%, <LIGHT> 100%)`. No `135deg`, no `to right` — **except** challenge-card and milestone headers, which keep their original `135deg` / `to right` (see §6.2a + §6.12).

### 6.2a Gradient vs. Solid — by ELEMENT ROLE (LOCKED)

Whether an element is a gradient or a flat solid is determined by its **role**, not flattened globally:

- **Gradient (hero / header elements):** the sticky **nav bar**, the **title block**, **challenge-card headers** (§6.12), and **milestone headers**. These are one-off or attention-anchor headers.
- **Solid (section-system elements):** **section caps**, **PART banners**, **nav buttons**, and **section-marker pills**. Anything that repeats as part of the per-section grid is flat solid.

Rule of thumb: if it's a *page/section header or a challenge/milestone announce-bar*, gradient is allowed; if it's part of the repeating section skin, it's flat solid. (This is why a §9 cap is solid plum but a §9 challenge-card header is a plum gradient — and that visible light/dark difference is intentional, not a bug.)

### 6.3 Sticky Navigation Bar

```html
<nav style="background: linear-gradient(to bottom, #1a5276 0%, #2e86ab 100%); border-radius: 10px; padding: 15px 20px; margin-bottom: 30px; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
    <div style="display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; align-items: center;">
        <a href="#section-1" style="color: white; text-decoration: none; padding: 5px 12px; border-radius: 4px; font-size: 0.85em; background-color: #3498db;">1. Intro</a>
        <!-- … one per section … -->
    </div>
</nav>
```

**Nav button colors (by section):**
- Sections 1–3: `#3498db` (blue)
- Sections 4–6: `#3a7d5c` (evergreen)
- Sections 7, 8 **and 8A**: `#c45d76` (dusty rose)
- **Section 9 (Challenges): `#9b6a9e` (plum)** — its own color, split out of the old rose group
- Section 10 + Glossary + Quick Ref + Image Index: `#6c757d` (gray)

**Nav button count:** 12 (no 8A) or 13 (with 8A).

### 6.4 Title Block (gradient banner, NO leading icon)

```html
<div style="text-align: center; padding: 40px 20px; background: linear-gradient(to bottom, #1a5276 0%, #2e86ab 100%); color: white; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 5px 20px rgba(0,0,0,0.15);">
    <h1 style="margin: 0; font-size: 2.4em; color: white;">LESSON 10</h1>
    <div style="font-size: 1.3em; opacity: 0.95; margin-top: 8px;">Obstacles: Teaching Your Robot to Navigate Roadblocks</div>
    <div style="font-size: 1em; opacity: 0.9; margin-top: 8px;">Zumo 32U4 Robotics • PlatformIO Edition</div>
    <div style="font-size: 0.9em; opacity: 0.8; margin-top: 5px;">Version 1 — June 2026</div>
</div>
```

- `<h1>` is **`LESSON ##` with NO leading emoji.**
- Four lines: LESSON ##, descriptive title, series line, version line.

### 6.5 Section Headers — CAP + BOX (LOCKED)

Every section (and every end-matter block: Glossary, Quick Reference, Image Index) is a **colored cap on a matching bordered box.** The cap holds the title in white; the box wraps that section's content. The old plain `<h2>` heading style (`#1a5276` text + bottom border) is **retired**.

```html
<div style="background-color: #3498db; color: white; padding: 13px 18px; border-radius: 8px 8px 0 0; margin-top: 24px;">
    <div id="section-1" style="font-size: 1.15em; font-weight: bold;">📖 Section 1: The Roadblock</div>
</div>
<div style="border: 2px solid #3498db; border-top: none; border-radius: 0 0 8px 8px; padding: 18px; margin-bottom: 16px;">
    … section content …
    <p style="text-align: right;"><a href="#top" style="color: #3498db;">↑ Back to top</a></p>
</div>
```

- **Cap:** solid PART color, white bold title (≈1.15em), rounded top only (`8px 8px 0 0`), `margin-top: 24px`. The `id` lives on the inner title div (anchor target).
- **Box:** `border: 2px solid <PARTcolor>; border-top: none; border-radius: 0 0 8px 8px; padding: 18px; margin-bottom: 16px`. Caps the section content; back-to-top link sits inside.
- **Section-group colors (match the nav buttons):** §1–3 `#3498db` blue · §4–6 `#3a7d5c` green · §7/§8/§8A `#c45d76` dusty rose · **§9 `#9b6a9e` plum** · §10 + Glossary/Quick-Ref/Image-Index `#6c757d` gray. Each group owns ONE color; every element in it (cap, nav button, PART banner, challenge cards, table headers in that section) wears that color.
- **Cap KEEPS the leading icon** (`📖 🔨 ▶️ ⚠️ 🔑 🏆 📋` etc.); only the title-block h1 has no icon.
- The cap `id` must match the visible "Section N:" label and the nav anchor.
- **Sub-headings + table headers adopt the SECTION GROUP COLOR** (LOCKED — supersedes the old global blue h3 / navy table-header). Each section's internal headings and table headers wear that section's color:
  - **h3** (subsections, e.g. "5.3 …") → the section group color (§1–3 `#3498db`, §4–6 `#3a7d5c`, §7/8/8A `#c45d76`, §9 `#9b6a9e`, §10+end `#6c757d`).
  - **h4** (sub-subsections) → also the section group color (same as h3 — NOT a separate green).
  - **Table headers** (the `<th>`/header row) → a DARKER shade of the section color (see table below).
  - **Exception:** callout-internal headings (e.g. Exit Ticket h4s inside callouts, Icon Guide h3) keep their callout styling — exempt from this rule.
  - (h2 is no longer used for section titles — the cap replaces it.)

**Section color → darker table-header shade (LOCKED):**

| Group | Section color (cap, h3, h4, nav) | Darker table-header shade |
|---|---|---|
| §1–3 | `#3498db` blue | `#1a5276` |
| §4–6 | `#3a7d5c` green | `#2a5a42` |
| §7/8/8A | `#c45d76` rose | `#9a4459` |
| §9 | `#9b6a9e` plum | `#704c73` |
| §10 + end | `#6c757d` gray | `#4d5358` |

(The old `#2e86ab` global-blue h3 and `#1a5276` global-navy table header are retired except where blue IS the section color, i.e. §1–3.)

**Callout / radius tiers (LOCKED — two-tier "notes vs. frames"):**
- **Inline content callouts** (border-left accent notes: tip, warning, key term, checkpoint, do-this-now, insight/learn) → **`border-radius: 4px`**.
- **Glossary / term cards** → **`8px`** (deliberate exception: they use a border-left accent like callouts but are reference cards, not inline notes — distinguished by the purple palette `#e7d4ff` bg / `#9b59b6` border).
- **Structural containers** (full-bordered frames, image placeholders, PART banners, title block, challenge boxes) → **`8px`**.
- The retired one-side style `0 8px 8px 0` must NOT be used on callouts. **Exception — the cap/box pair is intentionally one-side-rounded** (cap `8px 8px 0 0`, box `0 0 8px 8px`): together they form one rounded container, so the §11 "no one-side rounding" check does not apply to the cap/box pair.
- Machine rule: a `border-left` accent box → 4px *unless* it's the purple glossary palette (→8px); a full `border` (all sides) → 8px.
- Other radii: code blocks `6px`, nav buttons & pills `4–5px`, inline code chips `4px`.

### 6.6 Icon Legend (12 icons)

```html
<div style="background: #fff; border: 2px solid #2e86ab; border-radius: 10px; padding: 15px 20px; margin-bottom: 30px;">
    <h3 style="margin-top: 0; color: #1a5276; font-size: 1em; margin-bottom: 10px;">Icon Guide</h3>
    <div style="display: flex; flex-wrap: wrap; gap: 15px; font-size: 0.9em;">
        <span>📖 LEARN</span><span>💻 CODE</span><span>🔨 BUILD</span><span>▶️ TEST</span>
        <span>✅ CHECKPOINT</span><span>⚠️ WARNING</span><span>📝 DO THIS NOW</span>
        <span>🔑 KEY TERM</span><span>💡 TIP</span><span>👀 SEE</span>
        <span>🔍 INSIGHT</span><span>🔮 NEXT</span>
    </div>
</div>
```

The 12 icons: 📖 LEARN, 💻 CODE, 🔨 BUILD, ▶️ TEST, ✅ CHECKPOINT, ⚠️ WARNING, 📝 DO THIS NOW, 🔑 KEY TERM, 💡 TIP, 👀 SEE, 🔍 INSIGHT, 🔮 NEXT. (Use "⚠️ WARNING" — not "NOTE.")

### 6.7 Section-marker pills — RETIRED

The old "READING / CODE / BUILD / TEST — <tagline>" marker pills (`#2e86ab` rounded pills placed at the top of a section) are **retired**. They are redundant with the section CAP, which already labels the section and carries its icon. **Remove every section-marker pill** during retrofit — do not place any `<LABEL> — <tagline>` pill or banner inside a section. (This is the same principle as the orphan intro-banner ban in §7.)

### 6.8 PART Dividers (colored banner, matches its group)

Each PART banner is a **solid color matching the section group it introduces** (not navy). It announces the group; the colored section cap+boxes follow beneath it.

```html
<div style="background-color: #3498db; color: white; padding: 12px 20px; border-radius: 8px; margin: 22px 0 10px;">
    <div style="font-size: 18px; font-weight: 500; letter-spacing: 0.5px;">PART 1 — Theory &amp; Concepts</div>
    <div style="font-size: 12px; color: rgba(255,255,255,0.85); margin-top: 4px;">Sections 1–3: Learn the fundamentals</div>
</div>
```

- **PART 1** banner = `#3498db` blue (before §1) — "Sections 1–3: Learn the fundamentals"
- **PART 2** banner = `#3a7d5c` green (before §4) — "Sections 4–6: Set up and program your robot"
- **PART 3** banner = `#c45d76` dusty rose (before §7) — title "PART 3 — Testing & Challenges"; subtitle "Sections 7–8A: Verify and extend" (or "Sections 7–8: Verify and extend" if no 8A). PART 3 now covers ONLY §7, §8, §8A.
- **PART 4** banner = `#9b6a9e` plum (before §9) — title "PART 4 — Challenges"; subtitle "Section 9: Apply what you have learned". This is the NEW part introducing the plum Challenges section.
- 18px title + 12px subtitle (subtitle `rgba(255,255,255,0.85)`), `margin: 22px 0 10px`.
- The old navy gradient `#1a1a2e → #16213e` banner is **retired**. §10 + end matter have NO PART banner (they're the gray tail, after PART 4).
- **Four PARTs total** (was three): 1=§1–3, 2=§4–6, 3=§7–8A, 4=§9. §10+end = untitled gray tail.

### 6.9 Standard Section IDs

`#section-1` … `#section-10`, plus `#section-8a` (if present), `#glossary`, `#quick-ref`, `#image-index`. Body carries `id="top"`.

### 6.10 Back-to-top links

After each section: `<p style="text-align: right;"><a href="#top" style="color: #3498db;">↑ Back to top</a></p>`

### 6.11 Code Blocks — DARK (VS Code / PlatformIO theme) (LOCKED)

Code blocks and ASCII diagrams use a dark theme matching what students see in PlatformIO / VS Code (Dark+). Light code backgrounds are **retired**.

```html
<pre style="background-color: #1e1e1e; border: 1px solid #333; border-radius: 8px; padding: 15px; overflow-x: auto; font-family: 'Courier New', monospace; font-size: 0.9em; color: #e8e8e8;">
<span style="color: #569cd6;">void</span> setup() {       <span style="color: #7cbf6e;">// comment</span>
    display.print(<span style="color: #ce9178;">"Hello"</span>);
}</pre>

**Code-block spacing (LOCKED v8.4):** dark code blocks use **`padding: 15px`**, **`margin: 16px 0`**, and **`line-height: 1.8`** — all consistent across every block in a lesson. 15px is the standard (NOT 10px/20px). **No blank-line doubling:** source-generated code often has an empty line between every line of code (the `BXBXBX` pattern), which renders double-height — STRIP all such blank lines inside `<pre>` so code is single-spaced; the `line-height: 1.8` provides the breathing room instead. If blocks use a wrapper-`<div>` + inner-`<pre margin:0>` structure, set line-height on the inner `<pre>`. No double-semicolons (`;;` is a typo, always strip). §11 check: FAIL if any code block has padding≠15px, line-height≠1.8, or contains blank lines inside `<pre>`.
```

- **Background:** `#1e1e1e` · **border:** `1px solid #333` · **base text:** `#e8e8e8` (near-white).
- **Syntax colors (VS Code Dark+):** keywords `#569cd6` blue · comments `#7cbf6e` green · strings `#ce9178` orange-tan.
- **ASCII diagrams** (motor scales, flowcharts) use the same dark box + `#e8e8e8` text — never light-on-light.
- **Exception:** the Icon Guide/Legend box stays light (`#fff` / `#f8f9fa`) — it is not a code block.
- Inline code chips (within prose) keep their light chip style (`background: #e8e8e8; padding: 2px 6px`).

### 6.12 Challenge Cards (SECTION 9) — CANON (LOCKED)

§9 Challenges use the **carded format** (the "Lesson 9 look"). Each challenge is a bordered plum box with a gradient header, a difficulty pill, and a collapsible solution. Bare `<h3>Challenge N`</h3> headings (old L4/L10 style) are **retired** — convert them to cards.

```html
<div id="challenge-1" style="border: 2px solid #7d5283; border-radius: 10px; margin: 25px 0; overflow: hidden;">
    <div style="background: linear-gradient(135deg, #7d5283, #9b6a9e); color: white; padding: 12px 20px;"><strong>Challenge 1: Title</strong> <span style="display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.8em; margin-left: 10px; background: #4caf50;">EASY</span></div>
    <div style="padding: 15px 20px; background: white;">
        <p>Challenge description…</p>
        <details style="background:white; border:1px solid #ddd; border-radius:8px; margin:15px 0;"><summary style="padding:15px 20px; cursor:pointer; font-weight:bold; color:#1a5276; background:#f8f9fa; border-radius:8px;">🔓 Click to reveal solution</summary>
        <pre style="background-color: #1e1e1e; color: #e8e8e8; ...dark code per §6.11...">…</pre></details>
    </div>
</div>
```

- **Outer box:** `border: 2px solid #7d5283; border-radius: 10px; overflow: hidden`.
- **Header (gradient — a "header element" per §6.2a):** `linear-gradient(135deg, #7d5283, #9b6a9e)`, white text. Matches the §9 plum group.
- **Difficulty pill:** rounded (`border-radius: 12px`), white text. **Five tiers:** EASY `#4caf50` · MEDIUM `#ff9800` · HARD `#f44336` · EXPERT `#7d5283` · COMPETITION `#b7950b` (gold — added v8.5, for competition-grade capstone challenges).
- **Solution:** `<details>` / `<summary>` "🔓 Click to reveal solution"; the code inside is DARK per §6.11.
- The §9 **cap** stays flat solid plum `#9b6a9e` (it's a section cap, §6.2a); only the card *header* is the gradient.
- Old grape palette (`#7030A0`/`#9B59B6`) is retired → replace with plum (`#7d5283`/`#9b6a9e`).

**§9 TIER-CARD VARIANT (added v8.5):** §9 need NOT always be Easy/Medium/Hard challenge cards. Where the content is **project tiers** rather than escalating challenges (e.g., L16 Nothing Left to Take Away), §9 uses **tier-cards**: white card, `box-shadow`, `border-radius: 8px`, with a **medal-colored top border** — Bronze `border-top: 5px solid #cd7f32`, Silver `#c0c0c0`, Gold `#ffd700`. This is a legitimate alternative §9 format, chosen per-lesson by the author; challenge cards remain the default.

---

## 7. EXIT TICKET (SECTION 10) — LOCKED

Three `<h4>` subsections, each wrapped in a specific callout:

1. **"Technical Skills: Can you...?"** — Checkpoint callout (`#e8f5e9` bg / `#4caf50` border). **☐ checkbox items only — NO list bullet** (see §11 checkbox-XOR-bullet rule).
2. **"Conceptual Understanding: Do you know...?"** — Coach's Tip callout (`#f0f7f0` bg / `#6b8e6b` border). **Bold question + italic `Answer:` line** beneath each (the L9 format), numbered.
3. **"Problem-Solving: Can you modify or extend...?"** — Learn/Insight callout (`#e3f2fd` bg / `#2196f3` border). **☐ checkbox items only — NO list bullet.**

(Optional follow-ons used in some lessons: a confidence self-assessment table and a "What's Next" preview. Quiz feature deferred.)

**Orphan intro-banner ban:** the blue "ASSESSMENT — Check Your Understanding", "CHALLENGES — Test Your Skills", "TESTING — Verify Everything Works" announce-banners are **retired** — they add no information and break the cap/box rhythm. Do not insert any "<LABEL> — <tagline>" banner at the top of a section; the section CAP already labels it.

---

## 8. CALLOUT STANDARD v1.0 — LOCKED

**All callouts use inline `style=` only.** `<strong>` for titles (never a CSS class). 9 standard types:

| # | Type | Icon | Background | Border |
|---|---|---|---|---|
| 1 | Coach's Tip | 💡 | `#f0f7f0` | `#6b8e6b` |
| 2 | Coach's Note / Warning | ⚠️ | `#fff8e1` | `#ffc107` |
| 3 | What You Should See | 👀 | `#d1ecf1` | `#17a2b8` |
| 4 | Do This Now | 📝 | `#ffe4cc` | `#ff8c00` |
| 5 | Checkpoint | ✅ | `#e8f5e9` | `#4caf50` |
| 6 | Key Term | 🔑 | `#f3e5f5` | `#9c27b0` |
| 7 | Learn / Insight | 📖 / 🔍 | `#e3f2fd` | `#2196f3` |
| 8 | Next Lesson | 🔮 / 🚀 | `#e8d4c4` | `#d4a574` |
| 9 | Challenge | 🎯 | `#e8f3ec` | `#3a7d5c` |

**Mini-Challenge / Bonus-Challenge blocks are retired** — replace any with the 🎯 Challenge callout (type 9).

**Canonical template (types 1–4, 6–9 — border-left accent style):**

```html
<div style="background-color: {BG}; border-left: 4px solid {BORDER}; padding: 15px 20px; margin: 20px 0; border-radius: 4px;">
    <strong style="color: {TITLE};">{ICON} {Title}</strong>
    <p>Body text.</p>
</div>
```

**Title colors per type** (extracted from L09 v03.0.3 reference lesson; type 9 set by DJ decision, Session 10):

| # | Type | Title color |
|---|---|---|
| 1 | Coach's Tip | `#3a5a3a` |
| 2 | Coach's Note / Warning | `#856404` |
| 3 | What You Should See | `#0c5460` |
| 4 | Do This Now | `#c45a00` |
| 5 | Checkpoint | `#2e7d32` |
| 6 | Key Term | `#6a1b9a` |
| 7 | Learn / Insight | `#0d47a1` |
| 8 | Next Lesson | `#8a5a2b` |
| 9 | Challenge | `#2a5a42` |

**Type 5 Checkpoint has TWO canon forms** (both live in L09):
1. Standard border-left callout — bg `#e8f5e9`, border-left 4px `#4caf50`, title `#2e7d32` (template above).
2. Centered milestone banner — `background: linear-gradient(to right, #e8f5e9, #c8e6c9, #e8f5e9); border: 2px solid #4caf50; border-radius: 10px; padding: 15px 20px; margin: 30px 0 20px 0; text-align: center;`

**Type-9 label canon:** label text is `🎯 CHALLENGE` (optionally with a time/difficulty qualifier in parentheses, e.g. `🎯 CHALLENGE (1 minute)`). "MINI-CHALLENGE" and "BONUS CHALLENGE" label texts are retired along with the blocks.

**`ZUMO_Callout_Standard_v1.md` is RETIRED** — templates folded in here as of v8.8. Do not request or reference the standalone file.

**Code-block syntax coloring — LOCKED (S12, DJ-approved):** All `<pre>` code blocks: dark bg `#1e1e1e`, base text `#e8e8e8`, color-only inline `<span>` highlighting (NEVER background chips — chip-in-pre renders text invisible). Palette (VS Code dark approximation): comments `#6a9955` · keywords `#569cd6` · preprocessor `#c586c0` · types/classes (`Zumo32U4*`, `Serial`) `#4ec9b6` · strings `#ce9178` · numbers `#b5cea8` · ini keys `#e06c75` · ini section headers `#d7ba7d` · in-code section banners `#6a9955`. Apply by script with a per-block stripped-text-identity assertion (colored output must strip back to byte-identical code). Book-wide application pass: L01–L02 COMPLETE; L03–L15 queued (apply during each depth pass).

**Details/summary readability rule (added v8.10, from the L02 white-summary defect):** every `<summary>` sits on a light background (`#f8f9fa` details box), so its text color MUST be readable there — canon colors: `#5a6872` for standard troubleshooting/hint details, `#2a5a42` when the details block lives inside a challenge callout (matches the 🎯 CHALLENGE title color). `color: white` (or any low-contrast color) on a summary is a build error. Gate check (mandatory): fail the build if any `<summary` style contains `color: white`. Background: L02 shipped three invisible "🔓 Stuck? / Answer / Click for solution" summaries; scan confirmed the defect was L02-only — this rule exists to prevent reintroduction during the L03–L15 depth passes, which reuse the L02 hint/solution pattern.

---

## 9. VERSIONING — LOCKED

- Scheme (all projects): major = `v#`, moderate = `v#.#`, minor = `v#.#.#`. **No letter suffixes.**
- Filenames use zero-padded lowercase form: `v01`, `v02`, …
- **UNIQUE VERSION PER DELIVERY (v8.20 — DJ ruling, S33).** Once a build has been presented for download, **any** further change — code, prose, or image — bumps the version. Two files with the same name NEVER have different contents. *This RETIRES the old "a fix to an already-fixed version keeps its number" rule, which in S33 produced two different `Lesson_10_Obstacles_v02_1_1.html` files and sent the wrong one to GitHub.*
- **IMAGE CHANGES ARE A MINOR BUMP (v8.20 — DJ ruling, S33).** Inserting art, removing a figure, renumbering a placeholder, or editing a caption or the Image Index is a minor correction → third digit (`v04.0.3` → `v04.0.4`).
- **Reopening a lesson:** read the current v# from the uploaded `.html` filename — do not hardcode a target.
- **v8 re-baseline exception (one-time):** every lesson resets to `v01` at the v8 transition. Normal bump rule resumes afterward.

---

## 10. IMAGE PLACEHOLDERS

Keep `[IMAGE X.Y]` format (X = lesson number, Y = image number). Image Index must list exactly what appears in the body — **no phantoms, no omissions** (S33 found L02 listing a `[GRAPHIC 2.3]` that exists nowhere).

**IMAGE and GRAPHIC ARE SEPARATE NUMBER SPACES (v8.20 — canon, S33).** `L01_IMAGE_1-13` and `L01_GRAPHIC_1-13` coexist by design; the prefix disambiguates. `[IMAGE 2.8]` and `[GRAPHIC 2.8]` in the same lesson is **not** a collision and must not be "fixed."

**AUDIT ART AGAINST `images/`, NEVER AGAINST THE LESSON ALONE (v8.20 — canon, S33).** Before declaring anything about art, clone the repo and compare three sets: (1) assets in `images/`, (2) `<img src>` in the lesson, (3) dashed placeholders. S33 found **nine built assets that no lesson referenced** — including all three L16 SVGs, which shipped with the lesson showing zero figures. GATE CHECK per lesson: every repo asset is referenced; every `<img>` resolves; every placeholder has no file.

- `[IMAGE x.y]` = DJ-sourced photo/screenshot. `[GRAPHIC x.y]` = Claude-authored SVG.
- Placeholder → figure conversion is a **minor bump** (§9).

---

## 11. PER-LESSON QUALITY CHECKLIST (run before presenting any lesson)

- [ ] **BLANKS ARE SPENT (v8.17):** every tunable declared as a student blank (`const int X = 0;   // <-- YOUR NUMBER`) is actually READ by the code. Grep: a constant that is declared and never used is a lie in the worksheet. Blanks ship as `= 0` with the starting guess in the COMMENT, never as a seeded value.
- [ ] **ZERO BYTE DELTA IS NOT PROOF OF NOTHING (v8.17):** if a state's binary size is unchanged after an edit, ask whether the edit changed a CONSTANT (byte-identical by construction — fine) or added LOGIC (then `--gc-sections` may be discarding it — investigate). Disassemble with `avr-objdump -d` and read the immediates before concluding a fix vanished.
- [ ] **SABOTAGED BUILDS SHOW THE PLANTED LINE (v8.17):** every Bonus mystery displays its sabotaged code in the hint. The question is "why does this cause that symptom," not "find the typo." (Also satisfies the payload gate by construction.)

- [ ] Filename: `Lesson_##_Topic_v##.html` (padded number, lowercase padded version, approved topic token)
- [ ] Body uses Segoe UI + `#fafafa` + `id="top"`
- [ ] Nav + title use top-down dark-first blue gradient
- [ ] Title h1 = `LESSON ##` with NO leading icon
- [ ] Every section is a CAP + BOX: colored cap (white title, keeps icon) on matching bordered box (§6.5)
- [ ] Cap/box + PART banner colors follow nav scheme: §1–3 blue `#3498db`, §4–6 green `#3a7d5c`, §7/§8/§8A rose `#c45d76`, **§9 plum `#9b6a9e`**, §10+end gray `#6c757d`
- [ ] PART banners are SOLID group colors (navy gradient retired); 4 banners (PART 1–4); PART 3 subtitle "Sections 7–8A: Verify and extend" (or 7–8 if no 8A); PART 4 subtitle "Section 9: Apply what you have learned"
- [ ] Sub-headings h3/h4 use the SECTION GROUP COLOR (not global blue/green); table headers use the darker section shade (§6.5). Callout-internal headings exempt. (See the dedicated NEW check below.)
- [ ] Code blocks + ASCII diagrams are DARK (`#1e1e1e` bg, `#e8e8e8` text; keywords `#569cd6`, comments `#7cbf6e`, strings `#ce9178`); no light-on-light; Icon Guide stays light (§6.11)
- [ ] All box/callout corners fully rounded (no one-side-rounded `0 8px 8px 0`)
- [ ] Icon legend has all 12 icons ("WARNING")
- [ ] 10 sections present; 8A only if the lesson has a reusable coding pattern (present: L6–L12; absent: L1, L13–L15; verify L2–L5), placed between 8 and 9
- [ ] End-matter caps use icon set: 📖 Glossary / ⚡ Quick Reference / 🖼️ Image Index
- [ ] **Glossary entries use the canon term-card format** (`#e7d4ff` bg / `#9b59b6` border / `8px`); no stray glossary purples (`#f3e5f5`, `#f3e8f9`, `#7b2d8e`, `#9c27b0`) in the glossary region.
- [ ] Section IDs in clean order: 1,2,3,4,5,6,7,8,8a,9,10,glossary,quick-ref,image-index
- [ ] Nav anchors all UNIQUE and all resolve; "Back to top" + cross-refs resolve
- [ ] Cap `id` matches visible "Section N" label + nav anchor
- [ ] Exit Ticket = 3-h4 with correct callout colors
- [ ] Callouts inline-only; 0 `<style>` blocks; 0 callout classes
- [ ] Image Index matches body placeholders exactly
- [ ] div tags balanced; version string in title block AND footer matches filename
- [ ] **NBSP/whitespace stripped:** 0 standalone `\xa0` lines (export artifact); no runs of 3+ blank lines. (Pre-overhaul lessons ship with 140–390 of these; each renders as an empty vertical-space line.)
- [ ] **Bare-element sweep (after removing any `<style>` block):** 0 bare `<table>` (every table has `width: 100%`); 0 bare stage-marker divs in old navy `#2c3e50` — recolor to `#2e86ab`. Old stylesheets styled these globally; once inline-only, bare elements lose styling silently and pass div/anchor checks while rendering wrong (narrow tables → horizontal gaps).
- [ ] **No retired navy:** 0 occurrences of `#2c3e50` or `#1a1a2e` anywhere (markers, title, banners).
- [ ] **div-depth walk (not just balance):** every PART banner sits at div-depth 0 (outside all section boxes). Balance can pass while a banner is trapped inside the prior box; verify depth, not just open==close counts.
- [ ] **Dark-wrapper scope check (v8.14.1, from the S21 L03 find):** every dark code wrapper (`background-color: #1e1e1e` div) must close before the next `<h3>`/`<h4>`. Walk each dark div to its matching closer; if the enclosed span contains ANY heading, FAIL. Balance and the depth walk both pass when the closer merely sits too late (L03 v03.0.0: the Safe-Run wrapper's closer landed after four QR tables — code chips rendered as blank pills, shaded rows light-on-light). Measure banner/section depth at the rendered DIV, not at region comments (comments legitimately sit inside closing wrappers).
- [ ] **In-code highlight spans preserved + dark-readable:** pre-existing "new code"/diff highlight spans (e.g. light-green `#90EE90`) are kept (carry pedagogical meaning) but recolored for the dark code background (e.g. bg `#2d5a2d`, text `#b8f0b8`) — never light-text-on-light-fill, never stripped.
- [ ] **Callout radius two-tier:** inline content callouts (border-left accent notes) = `4px`; glossary/term cards = `8px`; structural containers (full-border frames, image placeholders, PART banners, title) = `8px`. No one-side rounding (`0 8px 8px 0`) on callouts — that style is retired. (Code blocks `6px`, nav buttons/pills `4–5px`, inline code chips `4px` separate and unchanged. Cap/box pair is the one intentional one-side-rounded exception.)
- [ ] **4-PART structure (NEW):** PART 1 §1–3 blue · PART 2 §4–6 green · PART 3 §7–8A dusty rose ("Verify and extend") · **PART 4 §9 plum** ("Apply what you have learned"). Four banners, not three. §10 + end = untitled gray tail. PART 4 plum banner present before §9.
- [ ] **§9 plum (NEW):** §9 cap, nav button, and PART 4 banner all use plum `#9b6a9e` (cap/banner/button flat solid). §7/§8/§8A stay dusty rose `#c45d76`. No `#c45d76` on §9 elements; no plum on §7/§8/§8A.
- [ ] **Payload byte-match gate (v8.14, canonized from S18 approval):** every Maker `PAYLOADS[lesson][key]` byte-matches its lesson-source code block at EVERY lesson save (payloads exclude the generator-stamped header + `#include` — mainCpp = head + body). A lesson edit that touches any `<pre>` wired into the Maker requires re-verifying its payloads before either file ships.
- [ ] **Payload-gate INHERITANCE RULE (v8.15, DJ-approved S22):** lesson N's canonical payload corpus = its own decoded `<pre>` bodies + the Maker's template strings **+ lesson N−1's `finished` payload bodies**. Rationale: from L08 onward, Step 1 of every §6 is "copy your Lesson N−1 project" — the eight files arrive wholesale, and the lesson only shows the blocks it CHANGES. Files carried unchanged are therefore canonical by construction, and demanding they re-appear in lesson N's pres would force pointless duplication of a whole project into the lesson body. The rule stays byte-strict in the direction that matters: any content lesson N *modifies* must still appear verbatim in lesson N's own pres. Implementation note: `finished` may be a plain string (L02/L03) or a multi-file dict (L07+) — handle both. Battery must PASS L02 through the newest lesson at every Maker save; zero regressions is the bar.
- [ ] **Bounded-scope replace assert (v8.14):** every wholesale/regex replace must assert its span endpoints sit inside ONE card/step/section — `count==1` alone is insufficient (a greedy `.*?` can span two cards and pass the count check; S20 destroyed L03 Bonus-1+2 this way before donor recovery). Prefer exact-string `str.replace` with `count==1`; when a regex is unavoidable, print and eyeball the matched span before applying.
- [ ] **Challenge-card canon (§6.12):** every §9 challenge is a carded box (border `#7d5283`, header gradient `135deg #7d5283→#9b6a9e`, difficulty pill, `<details>` dark solution). No bare `<h3>Challenge N`</h3>. Old grape `#7030A0`/`#9B59B6` retired.
- [ ] **Checkbox-XOR-bullet (GATE, global):** FAIL the lesson if ANY `☐` appears inside a list whose `<ul>`/`<ol>` does not carry `list-style: none`. Detection must scan EVERY `<ul>`/`<ol>` regardless of its attributes (a styled `<ul style="margin:0; padding-left:20px">` containing `☐` is a FAIL just like a bare `<ul>`) — a narrow "bare-`<ul>` only" check misses styled variants. Fix = inject `list-style: none; padding-left: 0;` into that list's style. No list item EVER shows both a bullet and a `☐`. Applies to ALL sections, not just Exit Ticket.
- [ ] **No orphan intro-banners:** 0 "ASSESSMENT / CHALLENGES / TESTING — <tagline>" announce-banners at the top of any section (the cap labels the section; §7).
- [ ] **No section-marker pills (§6.7 retired):** 0 "READING / CODE / BUILD / TEST — <tagline>" `#2e86ab` pills anywhere. The cap is the only section label.
- [ ] **Subheadings + table headers = SECTION color (NEW):** h3/h4 subheadings use the section group color (§1–3 blue, §4–6 green, §7/8/8A rose, §9 plum, §10+end gray); table headers use the DARKER shade of that color (§6.5 table). No global `#2e86ab` h3 or `#1a5276` table header outside §1–3. Callout-internal headings exempt. h3 must NOT be near-black bold.
- [ ] **Gradient-vs-solid by role (§6.2a):** nav/title/challenge-header/milestone-header = gradient; caps/PART banners/nav buttons/pills = solid. No solid challenge headers, no gradient caps.
- [ ] **PART 3 title token:** "PART 3 — Testing & Challenges" (not "Test & Challenges").
- [ ] **Empty-section-box check (added v8.11, from the L02 Glossary/Quick-Ref/Image-Index defect):** every section banner’s bordered body box must actually CONTAIN its section’s content. A box that opens and immediately closes (regex: `border-top: none;[^>]*>\s*</div>`) is a build FAILURE — div-balance alone cannot catch it (L02 ≤ v02.0.18 passed balance while all three end-section bodies sat outside their boxes). Where `<!-- end X wrapper -->` markers exist, the box’s closing `</div>` must sit immediately before the marker.
- [ ] **Depth-pass items (v8.12, for any lesson given the L02 treatment):** syntax coloring per §8 palette (identity-asserted) · challenge timers wired (`timer.html` iframes) · "📁 Work in:" destination lines on every challenge · Maker challenge registry extended in `newproject.html` · §4 Start-a-New-Lesson ritual block present · ALL code compile-verified on the AVR harness · white-summary + empty-box scans clean.
- [ ] **Dedicated ASCII sweep (v8.13.1)** on every depth pass, even for lessons marked "converted": scan all `<pre>` bodies for box-drawing/arrow characters (┌ ┐ └ ┘ │ ─ ◄ ► ▶). Established by the L03 half-conversion find (Session 15): S6 built the SVGs and the tracker showed ✅, but the lesson file was never edited — four ASCII diagrams survived to Session 15.

---

## 11b. PRE-OVERHAUL LESSON PROFILES (audit FIRST to identify which)

Lessons authored before the v8 overhaul come in **two profiles**. The audit step (grep for `<style`, count `class=`, count `\xa0`) identifies which, and that drives the build:

- **Class-based (e.g. L6):** has a `<style>` block + CSS classes + nbsp. Requires **class→inline mapping (approach B):** map every class straight to its v8 inline equivalent (callouts → Callout Standard v1 colors, nav → color-coded buttons, part-divider → solid banner, section-marker → `#2e86ab` marker), then the normal design pass. Also carries the bare-`<table>` / nbsp problems.
- **Inline-but-stale (e.g. L7, L8):** no `<style>` block (already inline), but ships with nbsp clutter, bare/under-styled tables, navy `#2c3e50` markers, **and section-numbering deviations** (missing "Code" §5, off-by-one Test/Troubleshoot/Challenges/Exit, 8A out of DOM order, mislabeled Exit, missing PART 3 banner, missing Image Index). Fix structure first, then design pass.

Either profile may need a structural §5 "Code" authored (Bible §4: §5 = walkthrough/project-org; §6 = step-by-step build). Split at the natural CODE/BUILD seam if present (L7), or author from the build content (L4).

---

---

## 13. BATTERY CANON (v8.20 — LOCKED, S33)

**The classroom fleet runs rechargeable NiMH — Panasonic eneloop.** Every battery number in the book is written for NiMH.

| Reading (4 cells) | State | Meaning |
|---|---|---|
| **~5,400 mV** | Fresh off the charger | ~1.35 V/cell |
| **~4,800 mV** | The plateau | 1.2 V/cell — where NiMH spends most of its life. **This is `BATTERY_GOOD`.** |
| **~4,200 mV** | Nearly empty | 1.05 V/cell. **This is `BATTERY_LOW`.** Draining past it damages the cells. |
| **~6,300 mV** | Not NiMH | Somebody put alkalines in. |

- **The constants are the chemistry, not a guess.** `BATTERY_GOOD = 4800` / `BATTERY_LOW = 4200` (RobotConfig.h, L07+) are the NiMH plateau and the NiMH floor. Any lesson that states battery numbers must agree with them.
- **Alkaline is allowed but taught honestly:** 6.0 V nominal — which *is* the motors' rated voltage, so a robot on fresh alkalines is slightly faster (Pololu quotes motor specs at 6 V). But alkaline voltage **slides downhill the whole time it is used**, while NiMH holds a flat 1.2 V plateau and then drops. *A robot on alkalines is a moving target: the one you tuned in first period is not the one you get in seventh.* This is the same physics L11 ("Time Lies, Distance Doesn't") is built on.
- Sources: Pololu recommends NiMH (4.8 V nominal) and notes motor specs are at 6 V; Panasonic states eneloop holds a consistent 1.2 V through the charge while alkaline drops rapidly below it.

---

## 14. ENGINEER'S LOG (v8.20 — LOCKED, S33)

One 📓 callout at the **end of §10** in every lesson, above the footer. **Prose only — no `<pre>`, no new anchors.** The payload gate never sees it; no byte count moves.

**Markup (canonical):**
```html
<h3 style="[LOCAL SKIN of that lesson's §10 subheads]">Engineer&rsquo;s Log</h3>
<div style="background: #f8f9fa; border-left: 5px solid #1a5276; padding: 15px 20px; margin: 20px 0; border-radius: 4px;">
<b>&#128211; ENGINEER&rsquo;S LOG #NN &mdash; feeds: [TDP section]</b><br>
[the prompt]<br>
<i>Why judges care: [one line]</i></div>
```
The heading adopts the lesson's local §10 skin; **the box is book-wide constant** (TDP-blue `#1a5276`) so the log is recognizable as one instrument across 16 lessons.

**The 16 prompts (locked S32, written into the book S33):**

| # | Feeds (TDP section) | Prompt |
|---|---|---|
| 01 | Electronic Design → main controller | Write the "before" paragraph. Rewritten in L16 — the gap is the Abstract. |
| 02 | Electronic Design → sensors/actuators | Draw the board. Labeled, one page, no code. |
| 03 | Mechanical → actuators & power train | Record your TRIM — and why it isn't zero. |
| 04 | Electronic Design + testing data | Record calibration min/max; why the numbers move rooms. |
| 05 | Project Planning → constraints | Defend a forced tradeoff (pins 20 & 4 are shared). |
| 06 | Mechanical → power train + data | Show the COUNTS_PER_CM arithmetic; did 30 cm come out 30 cm? |
| 07 | **Software → architecture** | Draw the 8-file architecture. No source code. *(Highest-value entry in the book.)* |
| 08 | Software → innovative solutions | Explain P-control in plain English; then your Kp and how you found it. |
| 09 | Software → flowchart | Draw your state machine. |
| 10 | Project Planning → requirements | What does your obstacle maneuver cost you? |
| 11 | **"What didn't work"** | The failure entry: fresh battery vs. tired battery. |
| 12 | Performance → testing data | Cross-examine the robot: encoder vs. gyro, carpet vs. slick. |
| 13 | Software + requirements | How does the robot *know*? Your false-victim threshold. |
| 14 | **Rules-mandated** | Your LoP procedure + self-test card (RCJ 4.3.7). |
| 15 | Performance Evaluation | Record the hill-climb: gains, MAE/PEAK/WEAVE, when you stopped. |
| 16 | Whole TDP | Assemble. Abstract **last**. *(Ships as §10.3.)* |

**Rule: instruments go forward, documentation goes backward.** Code added to a published lesson invalidates payload bodies and the taught byte chain; prose-only retrofits do not.

---

## 12. DOCUMENT WORKFLOW

**Session open:** Upload `LIVE_ZUMO_TEXTBOOK.md` + this Bible (v8). Verify date / status / "currently working on."

**Session close:** Regenerate the complete `LIVE_ZUMO_TEXTBOOK.md` (full file, not a delta) and a fresh `ZUMO_TEXTBOOK_HANDOFF_PROMPT.md`. Surface any spec discrepancy to DJ — do not decide unilaterally. Bible is source of truth; update LIVE.md when DJ confirms a change.

**Source-of-truth hierarchy:** `ZUMO_SUPER_BIBLE.md` (specs) → `LIVE_ZUMO_TEXTBOOK.md` (session state) → handoff prompt. (`ZUMO_Callout_Standard_v1.md` retired at v8.8 — callout templates live in §8.)

---

*End of ZUMO SUPER BIBLE v8.*

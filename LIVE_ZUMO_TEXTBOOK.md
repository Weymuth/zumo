# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 17, 2026 (Session 49 — FIVE tasks, ALL PUSHED & LIVE. (1) **L03 challenge-card dark-block anomaly fixed** (commit bb10c28): L03 was the only lesson of 16 wrapping challenge Goal PROSE in a dark `#1e1e1e` block; 8 goal-blocks unwrapped to the white-body norm — root cause of invisible chips + washed-out callout. L03 v03.4.4→v03.4.5. (2) **Maker C07/C08 payloadRef fix** (bb10c28): `drive_a_square`+`auto_trim` had payloadRef `null`; set to `finished` (DJ ruling: C01–C06 stay finished-preload). Maker v2.31→v2.32. (3) **`ZUMO_L03_TEMPLATES.md` completed** (bb10c28): 6→all 8 challenges, term "challenge template", reference record not payload source. (4) **raw→Pages image URLs, BOOK-WIDE** (commit 05247d4): all 114 `<img src>` refs across 16 lessons moved from `raw.githubusercontent.com` (rate-limited, intermittent blank images) to `weymuth.github.io/zumo/images/` (same-origin, unthrottled, Canvas-compatible). Fixes the L04 4.x-missing symptom for the whole book. Every lesson +1 minor. (5) **L04 jumper photos wired** (05247d4): IMAGE 4.2 (factory jumper close-up) + new IMAGE 4.4 (5-sensor jumper position) added, EXIF/GPS stripped; IMAGE 4.1 filled with a temporary L11-diagram stand-in until the underside photo is shot (4.3 still needed). L04 → v04.0.11. Bible v8.32→**v8.33** (§10 image-URL canon + EXIF-strip rule + §11 no-dark-prose checklist item). Gate PASS all 16 throughout.)
**Status:** ✅ **S49 COMPLETE — ALL PUSHED & LIVE (commits bb10c28 + 05247d4)** · L01 v03.2.7 · L02 v02.2.4 · L03 v03.4.6 · L04 **v04.0.11** · L05 v04.1.9 · L06 v04.5.9 · L07 v04.3.9 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.2 · Bible **v8.33** · Maker **v2.32** · Gate v1.3 · Harness v3.0 · 🖼️ **All images now served from Pages (no more raw rate-limit blanks).** L04 jumper photos live. · ✅ **Verified by fresh clone: commit 05247d4, 0 raw image refs, both photos in images/, L04 v04.0.11.**
**Currently working on:** ✅ **S49 CLOSE.** Book-wide image serving fixed + L04 photos in + L03 card pattern conformed + C07/C08 payloads fixed + Bible v8.33. **IMAGE QUEUE (DJ still to shoot):** L04 4.1 underside (temp stand-in live) · L04 4.3 test surface · the rest of the 22-photo IMAGE_SHOT_LIST. **NEXT queued:** finish L04 learner-mode (C02–C05, after DJ does the discoveries) OR pending L03_C05 Variable Speed · L03 prose (prototype explainer · 3 Coach's Tips · zero-index · scope) · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step. **L04 LEARNER-MODE FINDING (S49, C01 walked):** logic is solid; the wall is Zumo/OLED API recall — put a small 'functions you'll need' crutch at point-of-use in each challenge card. See `L04_LEARNMODE_LOG.md`. **BENCH (need robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS. **PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · AI Tutor (LAST) · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.


---

## ✅ SESSION 49 (continued) — BOOK-WIDE IMAGE-SERVING FIX + L04 PHOTOS + BIBLE v8.33

**raw→Pages image URLs (all 16 lessons, commit 05247d4):** the intermittent "images not showing" problem (reported on L04 4.1/4.2/4.3) was NOT missing files or broken tags — it was `raw.githubusercontent.com` **rate-limiting**. GitHub throttles raw and returns 429 on a random few image requests per page-load, so different figures blank on different loads. Fix = all **114** `<img src>` refs converted from `raw.githubusercontent.com/Weymuth/zumo/main/images/` → `weymuth.github.io/zumo/images/` (Pages: same-origin, unthrottled, correct MIME, Canvas-compatible). Diff-audited: every changed line is host-swap only, 0 non-swap changes on any of 16 files. `ZUMO_Template.zip` download links (L01/L02) correctly LEFT on raw (rule is scoped to `/images/`). Gate PASS all 16. Every lesson +1 minor.

**L04 jumper photos (commit 05247d4, L04 → v04.0.11):** DJ shot two underside photos. **IMAGE 4.2** = factory (proximity) jumper close-up, wired into §4.2. **IMAGE 4.4** (new slot) = jumpers moved to the DN/line-sensor side (five-sensor position), added to Act Two/§6 with caption. **IMAGE 4.1** = temporary stand-in using the live L11 5-sensor diagram (captioned temporary) until the real underside photo is shot. **IMAGE 4.3** (test surface) still un-shot. EXIF/GPS stripped from both photos before push. Image index table updated.

**Bible v8.32 → v8.33:** §10 — **IMAGE `src` = Pages domain, never raw** (with the rate-limit rationale + the `/images/`-only scope + the Canvas requirement); **strip EXIF/GPS from DJ photos before push**; a GRAPHIC may temporarily stand in for an un-shot IMAGE. §11 checklist — **prose is not code: never wrap challenge Goal prose in a dark `#1e1e1e` block** (the L03 root cause), run a luminance contrast check.

**L04 learner-mode (C01 walked, log = `L04_LEARNMODE_LOG.md`):** DJ's logic was correct throughout; every stall was Zumo/OLED API recall (`ledYellow` vs `display`, `gotoXY`, `F()`, array slots). Headline refinement: put an API crutch at point-of-use in each challenge card. Also logged: 3-vs-5 sensor center-slot ambiguity; the else/one-way-state insight (why C01 needs `else` when L02 didn't); skip-calibration ordering trap. C02–C05 not yet walked.

---

## ✅ SESSION 49 — L03 CHALLENGE-CARD PATTERN FIX + C07/C08 PAYLOAD FIX + TEMPLATES COMPLETED

**L03 dark-block anomaly (root-cause fix, v03.4.4 → v03.4.5, PUSHED & LIVE):** L03 was the ONLY lesson of 16 that wrapped its challenge **Goal prose** in a dark `#1e1e1e` block — styling prose as if it were code. It is the oldest challenge-card design and never got retrofitted when the white-body card pattern became standard (L04–L16). Consequence: inline code-chips (`#e8e8e8` light bg, no text color) rendered light-on-light = invisible, and an amber `#fff3cd` USB-warning callout rendered washed-out — both because their text inherited the dark block's light `#e8e8e8` color. **Fix = unwrap all 8 dark goal-blocks** so the prose sits directly on the white card body, matching every other lesson. Chips + callouts are then readable by default (dark-on-white) with NO per-element color patch. Reveal-solution `<pre>` code blocks stay dark (correct book-wide); the C05 blue `#e3f2fd` modulo callout stays (dark text on light blue = readable). Verified: luminance-contrast scan = 0 low-contrast chips across all 16 lessons; L03 now shows 0 dark PROSE blocks in cards (matches L04/L06/L08); 8 reveal `<pre>` intact; div balance 0; diff = 16 wrapper lines removed + version only; payload gate PASS.

**Maker C07/C08 payloadRef fix (v2.31 → v2.32, PUSHED & LIVE):** `drive_a_square` and `auto_trim` had payloadRef `null` — the dropdown "make this folder for me" links resolved to nothing. Both set to `"finished"` to match the C01–C06 finished-preload canon; both dropdown labels gained the `(finished preload)` suffix (matches C05/C06). **DJ ruling S49: C01–C06 STAY finished-preload.** The S48-handoff premise ("no L03 `finished` payload exists") was WRONG against the live file — an L03 `finished` payload does exist, so C01/C02/C05/C06 and C03/C04 all already emitted valid code; C07/C08 were the only broken cards. All 8 L03 challenge kinds now resolve. Change = payloadRef + label text only; no `kind=` id / group / payload-body / byte change. node --check clean on both JS blocks; v2.32 changelog line added.

**`ZUMO_L03_TEMPLATES.md` completed (repo root, PUSHED & LIVE):** regenerated from 6 → **all 8 challenges** (C07 Drive a Square + C08 Auto-TRIM Preview added in the C01–C06 format, authored from the live lesson cards; solutions match the lesson line-for-line). Term set to **"challenge template"** throughout (8 card subheads renamed from "Code Template"); the false "no finished payload" note corrected; file reframed as a **teaching/reference record**, NOT a payload-staging source.

**Process notes:** the invisible-text bugs were surfaced by a screenshot, then confirmed by a real luminance-contrast scan (a first crude string-based inverse scan produced a false positive — `#333` text-color matched a dark-bg pattern — caught and corrected). Push verified by fresh clone AND version check: commit `bb10c28`, L03 v03.4.5, Maker v2.32, templates = 8 challenges.

---

## ✅ SESSION 46 — L03 BOOK TASKS + EXPERT RETIRED + §5b BOOK-WIDE + L11–L16 VERSIONS RECOVERED

**L03 book tasks (v03.4.3 → v03.4.4, PUSHED & LIVE):** modulo `%` explainer (blue `#e3f2fd` callout) added to the C05 Variable Speed card, before the reveal — teaches remainder + wrap-to-0 for the cycling index. Two Coach's Tips at Step 13: upload→power-on (setup() runs once; put the robot down before upload completes) and don't-trust-AI-autocomplete (verify against the lesson). Task (a) "1000 ms = 1 second" was already present (line 766) — no change. Diff-audited, 4 changes, 0 deletions.

**EXPERT tier retired book-wide:** the old EXPERT tier had no home in the §6.12 5-tier scale (EASY/MEDIUM/TOUGH/HARD/ADVANCED). All 5 instances → ADVANCED `#f44336` (red, top tier — no demotion): 4 challenge-card pills (L04 C5 · L06 C8 · L09 C6 · L10 C5) + 1 inline heading tag (L15 §9.7). Card-header gradients (`#7d5283→#9b6a9e`) left intact; L16 prose "Version 2 — If I Built the Next One" protected from the banner sweep. EXPERT now appears NOWHERE in the book. Bumps: L04 v04.0.9 · L06 v04.5.8 · L09 v05.0.8 · L10 v02.1.11.

**§5b applied to ALL 16 lessons:** L11–L16 previously had only bare `Version N` banners and NO hidden comment (the L11–L16 §5b debt). Now every lesson carries the hidden `<!-- Lesson version: vXX.XX.XX -->` first line + a `Version NN.N` visible banner.

**⭐ L11–L16 TRUE VERSIONS RECOVERED — the floor-guess is retired.** The S45 LIVE.md had CORRUPTED L11–L16 to the S34 rename FLOOR (v02.0.3 etc.). This session, DJ's Downloads yielded the recorded ledger. **Four independent sources now agree, and the uploaded lessons are byte-identical to the live repo:**
- S38 LIVE.md snapshot · S39-push-zip LIVE.md · S43 LIVE.md · git history (no commit touched L11–L16 after "39 Lessons"/S38).

| Lesson | Proven version | Note |
|---|---|---|
| L11 | v02.2.1 | S38 recorded, held through S39/S43, no edits since |
| L12 | v01.2.2 | same |
| L13 | v02.2.1 | same |
| L14 | v02.4.1 | same |
| L15 | v02.2.2 | S38 base v02.2.1 + this session's EXPERT→ADVANCED edit |
| L16 | v02.2.1 | same |

**Lesson: stable filename + major-only banner meant the minor lived ONLY in LIVE.md — one corruption lost it.** §5b (hidden comment in every file) now prevents recurrence: the version is durable in the file itself, greppable, and no longer a LIVE.md single-point-of-failure.

---

## 🎨 SESSION 41 DESIGN LOCKS — L03 CHALLENGE REDESIGN (design only; build is S42)

**Rating scale (book-wide, NEW):** **EASY · MEDIUM · TOUGH · HARD · ADVANCED** — 5 tiers, replaces EASY/MEDIUM/HARD. No minimum cards per tier; order carries difficulty, labels assist. (Bible §6.12 edit queued S42.)

**Spiral marker (book-wide, NEW name):** student-facing header = **"🔁 Builds on:"** (was "Spiraled skills:" in §18.2). Names the reused prior skill in words + inline ⭐ numbered star (source lesson # inside, `spiral_star_NN.svg`). "Spiral" remains the teacher-side/Bible method name. (Bible §18.2 edit queued S42.)

**L03 ladder — 8 cards, reordered, NOTHING DELETED** (old 6 + 2 new):
| # | Card | Tier | New concept | Builds on |
|---|------|------|-------------|-----------|
| 1 | Spin Test | EASY | direction / signs | — |
| 2 | Battery Warning | EASY | `if` comparison | ⭐ L02 OLED display |
| 3 | **Constrain** *(NEW)* | EASY | clamp a value (`constrain()`) | ⭐ L02 constants |
| 4 | **Ramp** *(NEW)* | MEDIUM | change a value over time (loop) | Constrain (rung 3) |
| 5 | Variable Speed | MEDIUM | arrays + cycling index | — |
| 6 | Save TRIM | MEDIUM | persist a tuned value as a constant | — |
| 7 | Drive a Square | HARD | author a function + sequence | — |
| 8 | Auto-TRIM | ADVANCED | open-ended research (no code) | — |

*(TOUGH tier unused in L03 — fine. Existing kinds: spin_test, variable_speed, battery_warning, save_trim, drive_a_square, auto_trim. Two NEW kinds needed: constrain, ramp. Bonus set — creep_mode/backwards_trim/backwards_robot/braking_test/figure_eight/speedometer — UNTOUCHED.)*

**Constrain card — LOCKED spec:** two motor-speed constants `const int LEFT_SPEED / RIGHT_SPEED` (student edits 150/200/250 across three uploads) + `const int MAX_SPEED = 200` cap. `setSpeeds(constrain(LEFT_SPEED,-MAX_SPEED,MAX_SPEED), constrain(RIGHT_SPEED,-MAX_SPEED,MAX_SPEED))`. Observe: 150 slower; 200 & 250 IDENTICAL (both clamped to 200) — the "aha." Also try LEFT≠RIGHT to see per-argument clamp (robot curves — OK). Run `delay(...)` then `setSpeeds(0,0)` to stop. Method A (edit + re-upload ×3, NOT button-cycle — buttons not taught yet). TRIM stays OUT of the code (that's Save TRIM's job) — only referenced in "Builds on:" as another constant they've met. Constrain is on SPEED; time is only a stop-timer, unrelated. **Third left/right reinforcement in L03** (Spin signs → TRIM offset → Constrain clamp) — earns EASY *because* it builds on prior contact.

**Ramp card — spec (refine S42):** soft-start — ramp LEFT/RIGHT speed gradually from 0 up to MAX_SPEED in a loop (not a jump to full speed). Spirals back to Constrain (ramp up to the clamped MAX_SPEED). MEDIUM.

---

> **Source of truth = `ZUMO_SUPER_BIBLE.md` (v8.32).** Filename is UNVERSIONED — the version lives ONLY in the internal line. Verify with `grep -oE "Bible version: v[0-9.]+"`.


## ✅ SESSION 45 — L02/L03 CONTENT QUEUE DONE + C04 RAMP LEARNER-MODE (PUSHED, commit 35e81fd)

Cleared the three remaining S44 content items and walked DJ through the Ramp challenge in learner mode. All content was pushed live during the session (DJ pushed L02 + L03 while C04 was being coached); a fresh clone confirms md5 match against staged.

**Delivered & LIVE:**
- **Lesson_02.html v02.2.0 → v02.2.1** — NEW §3.2b "Data Types: What Kind of Value?" (after the setup/loop timeline, before §3.3). Blue `#e3f2fd` type-explainer callout introducing all five types students write themselves — `int`, `bool`, `float`, `long`, `char`, one line + example each — followed by deep prose on `int` (the workhorse; decimal-chop trap) and `bool` (Boolean yes/no switch). Forward-pointers verified against the code: `long`→L05, `float`→L07, `char` named-only. Diff-audit: 28 insertions, 0 deletions.
- **Lesson_03.html v03.4.0 → v03.4.1** — TWO amber callouts, one bump:
  - C03 Constrain card: `const` vs `constrain()` "two different jobs" (declare with `=`, one value / call with 3 args, clamps at use). DJ hit this wall 3× in learner mode.
  - C02 Battery Warning card: "Testing on USB? The reading lies" — `readBatteryMillivolts()` reads low/zero on USB → false low-battery warning; test on batteries with the switch on, unplugged.
  - Diff-audit: 22 insertions total (9 + 13), 0 deletions.
- **ZUMO_SUPER_BIBLE.md v8.29 → v8.30** — §18.4 TYPE-EXPLAINER CALLOUT (new: the blue-callout look is canon, reused for each type's later deep dive so students recognize it on sight) + §18.3 CHAT-DISPLAY RULE (when showing a Maker starter in chat, prepend the wrapper header so it matches the generated file).

**Learner mode:** C04 Ramp — DJ wrote a correct loop-free soft-start (50→100→150→200, each rung held 1 s, stops at cap, all in `setup()`). Two real teachable moments surfaced: `setup()` vs `loop()` (a one-time event belongs in setup), and the missing `#include <Zumo32U4.h>` (`'Zumo32U4Motors' does not name a type`). The include gap traced to Claude pasting the raw payload body (starts at HARDWARE OBJECTS, no include) instead of the generated file → became the §18.3 chat-display rule.

**Process:** memory consolidated (entry 13 SVG log trimmed to provenance; two parked-idea entries merged) — now 29/30. Project instructions rewritten to clone-first (no more waiting for an upload of a repo file).

**NEXT (S46):** learner mode L03_C05 Variable Speed (arrays + cycling index).

**Late-session mechanical sweep (all cosmetic, minor bumps):**
- **C06 re-rated** MEDIUM → EASY (it's a one-line edit; matches C01). L03 v03.4.1 → v03.4.2.
- **Book-wide pill recolor to the §6.12 5-tier canon** — 39 pills across L01/L02/L04–L10: MEDIUM `#ff9800`→`#2196f3` (×25), HARD `#f44336`→`#ff9800` (×14). Labels unchanged; NOT a re-rating. Diff-audited: 0 non-pill lines touched. Bumps: L01 v03.2.5 · L02 v02.2.2 · L04 v04.0.7 · L05 v04.1.7 · L06 v04.5.6 · L07 v04.3.7 · L08 v04.1.5 · L09 v05.0.6 · L10 v02.1.9.
- **DEFERRED — 4 EXPERT pills** (L04, L06, L09, L10): EXPERT is retired but TOUGH sits *below* HARD in the new scale while EXPERT sat *above* — so a blind rename would demote them a tier. Needs a per-card ADVANCED-vs-TOUGH ruling. Left untouched.
- **VERSION-SLOT CHANGE (Bible v8.30→v8.31, §5b rewrite):** the full version now lives in TWO in-file homes so it's never trapped in LIVE.md again — VISIBLE banner = major.minor (`v03.2`, churns only on moderate+ bumps), HIDDEN comment line 1 = full (`<!-- Lesson version: v03.2.6 -->`, every bump). Filename unchanged. Applied L01–L10 (each +1 patch for the change): L01 v03.2.6 · L02 v02.2.3 · L03 v03.4.3 · L04 v04.0.8 · L05 v04.1.8 · L06 v04.5.7 · L07 v04.3.8 · L08 v04.1.6 · L09 v05.0.7 · L10 v02.1.10. ⚠️ L11–L16 get banner+comment when each is next opened (version reconciled from the git-proven floor).
- **DEFERRED — C06 reorder to #1** (coordinated edit: renumber cards, move Maker kind= ids + reveal blocks + cross-refs). Scope next session.

---

## ✅ SESSION 44 — S43 RECONCILED + WHOLE-TEMPLATE STARTERS + RAMP OPTION C (PUSHED, commit 06a2561)

**Open — the v3.0 ghost:** S43's handoff/LIVE.md claimed a **Maker v3.0** "BIG bump" was staged/unpushed. Fresh clone showed the truth: the entire S43 batch (L02 v02.2.0, L03 v03.3.0, Bible v8.28, gate v1.2, + the constrain/ramp Maker rows and payloads) was **already live** in commit 44fcaad — but the Maker read only **v2.28**, with the S43 content added and **no version bump or changelog entry**. "v3.0" existed nowhere in any file. (`pio_harness.sh v3.0` is a different, unrelated artifact.) DJ ruled the S43 add MINOR → relabeled live Maker **v2.28 → v2.29** (badge + changelog line, content unchanged) and pushed.

**Build (S44 queue items 1+2, gate PASS, PUSHED & VERIFIED LIVE, commit 06a2561):**
- **newproject.html v2.29 → v2.30** — `constrain` + `ramp` challenge starters rebuilt as **WHOLE-TEMPLATE** starters (DJ ruling: no minimal skeletons; students are used to the full section-header template). Both ship all five section headers + seeded CONFIG constants (`// <-- YOUR NUMBER` convention) + present `setup()`/`loop()`; the taught concept stays blank in the marked landing zone. ⚠️ "Whole template" = the section-header scaffold, **not** the whole finished program. Payload bodies START at `// ===== HARDWARE OBJECTS =====`; the `mainCpp()` wrapper supplies banner + `#include` + MY PLAN.
- **Ramp = Option C** — rewritten as **unrolled fixed steps** (hand-written 50→100→150→200 climb), **no `for` loop** (not taught until L05). The hand climb motivates the L05 for-loop.
- **Lesson_03.html v03.3.0 → v03.4.0** — Ramp challenge card rewritten loop-free: Goal, Where-to-look, task step, reveal-solution code, and cap-note all had `for`-loop references removed; added an L05 forward-ref ("in Lesson 5 you'll meet the `for` loop"). Diff-audited: 5 intended hunks, nothing else touched.
- **ZUMO_SUPER_BIBLE.md v8.28 → v8.29** — **§18.3 REWRITTEN**: whole-template starter canon (reverses the S40 minimal-skeleton rule). Full section headers + seeded constants + present setup()/loop() + concept blank; payload starts at HARDWARE OBJECTS (wrapper adds the top); a starter must not require a construct not yet taught.
- **gate_payload_match.py v1.2 → v1.3** — exemptions swapped from the S43 minimal-skeleton lines to the new whole-template starter-only lines. Gate PASSES on the live tree (L02 16 keys, L03 15).

**Learnings:** the file is the source of truth — grep the actual badge/changelog, never trust the handoff's version claim (killed the v3.0 ghost). The gate reports only `missing[0]` per body (one flag at a time); to get the full unmatched set, temporarily patch it to loop over `missing`. Gate filename regex needs `Lesson_NN_Topic_` — stable `Lesson_NN.html` names need topic-suffixed symlinks to run.

**💡 Parked lesson idea (DJ):** an L05 §5.15 callback re-showing the L03 ramp as a 3-line `for` loop — "you hand-wrote 4 rungs in L03; here's the `for` loop doing it for you" — reinforces the Saxon spiral and sells the for-loop's value. Would bump L05 + add a spiral marker. NOT built; use as a lesson if needed.

**S44 queue remaining (items 3-5):** (3) data types never taught — int/float/bool/char explainer at L01/L02; (4) Constrain "two different jobs" clarification; (5) USB power falsifies `readBatteryMillivolts()` — warning on the Battery Warning card. Learner mode next = L03_C04 Ramp.


## 📘 SESSION 43 — L03 CHALLENGE SURGERY COMPLETE + LEARNER MODE C02/C03

**Open:** L03 file conflict found and fixed — the S42 ms-callout had landed in a stray REPO-ROOT `Lesson_03.html` while `index.html` served `lessons/Lesson_03.html` (no callout). DJ deleted the root copy and ported the callout into `lessons/`. Canonical L03 = `lessons/Lesson_03.html`.

**5 files changed (all STAGED, NOT PUSHED — gate PASS: L02 16 keys / L03 15 / Maker verified):**
- **Lesson_03.html v03.2.0 → v03.3.0** — §9 challenge block rebuilt: 6→8 card ladder (Spin / Battery / **Constrain** / **Ramp** / Variable Speed / Save TRIM / Drive a Square / Auto-TRIM); Constrain + Ramp authored with reveal-solution blocks; ALL pills re-rated to the 5-tier §6.12 scale (Spin/Battery EASY green, Constrain EASY green, Ramp/VarSpeed/SaveTRIM MEDIUM blue, Square HARD orange, Auto-TRIM ADVANCED red); 3 "🔁 Builds on:" markers (Battery ⭐L02 OLED, Constrain ⭐L02 constants, Ramp → Challenge 3); card ids renumbered 1–8; **pre-existing bug fixed** — battery-warning reveal checked `mv < 4500`, corrected to `4200` to match battery canon (§13). Bonus set untouched.
- **newproject.html Maker v2.28 → v3.0** (BIG bump, DJ ruling) — 6 L03 challenge rows renumbered + reordered to the new ladder, 2 new starter rows (`constrain`, `ramp`), 2 new starter payload bodies in `PAYLOADS["3"]`. `node --check` PASS, JSON parse PASS.
- **Lesson_02.html v02.1.1 → v02.2.0** — "🔁 Builds on:" explainer callout added at top of §9 (before Challenge 1), introducing the mark once before L03's first marked card. First book-wide inline-star use (`spiral_star_02.svg`).
- **ZUMO_SUPER_BIBLE.md v8.27 → v8.28** — §18.2 INLINE-STAR RENDERING LOCKED (DJ ruling): an inline spiral star is the actual `spiral_star_NN.svg` asset via `<img>` (absolute raw URL, `height:1.1em; vertical-align:middle`), NOT an emoji; emoji ⭐ only in the literal "🔁 Builds on:" header glyph.
- **gate_payload_match.py v1.1 → v1.2** — 11 starter-scaffolding EXEMPT entries for the `constrain`/`ramp` comment-only skeleton lines (no solution source to byte-derive from).

**Learner mode (Socratic walkthroughs, `L##_C##_W##`):**
- **L03_C02 Battery Warning — DONE**, bench-verified by DJ. Solution: `int mv = readBatteryMillivolts(); if (mv < 4200) { display.print(F("Low Batt")); return; }`.
- **L03_C03 Constrain — DONE.** Solution: `motors.setSpeeds(constrain(LEFT_SPEED, -MAX_SPEED, MAX_SPEED), constrain(RIGHT_SPEED, -MAX_SPEED, MAX_SPEED));` then delay + stop. Recurring confusion (hit 3×): calling a `const` like a function (`LEFT_SPEED(110,0,100)`) — the three args belong to `constrain`, not the constant.
- **L03_C04 Ramp — DEFERRED.** Found a ladder violation: Ramp needs a `for` loop, which isn't taught until L05. DJ ruled **Option C** — rewrite Ramp to avoid the loop, keep it in L03 after Constrain.

**DJ rulings → S44 queue:** (1) NO minimal skeletons — challenge starters show the WHOLE program (reverses §18.3; rebuild constrain/ramp starters, rewrite §18.3); (2) Ramp C04 rewrite Option C; (3) data types never taught; (4) Constrain "two different jobs" clarification; (5) USB power falsifies `readBatteryMillivolts()` — add card warning.

---

## 📘 SESSION 42 — L03 MS-CALLOUT (held) + BIBLE v8.27 (rating scale + marker rename)

The L03 challenge-redesign build began; the heavy surgery was **not** reached and is carried to S43. Two files changed: `ZUMO_SUPER_BIBLE.md` and `lessons/Lesson_03.html`.

**What locked:**
1. **L03 §3.7 milliseconds callout** — green tip teaching "1000 ms = 1 second" inserted at the top of §3.7 (prerequisite for the Constrain/Ramp stop-timers). L03 is **HELD, UNPRESENTED, still v03.2.0** — per the write-order + ghost rule, the single moderate bump to **v03.3.0** happens when the S43 surgery lands, not now.
2. **Bible §6.12 rating scale → UP-TO-5 tiers** (v8.27). A lesson uses as many as it needs, in order; no minimum per tier:
   - EASY green `#4caf50` · MEDIUM blue `#2196f3` · TOUGH purple `#9c27b0` · HARD orange `#ff9800` · ADVANCED red `#f44336`
   - Replaces the old EASY/MEDIUM/HARD/EXPERT/COMPETITION set.
3. **Bible §18.2 marker header renamed** "🔁 Spiraled skills:" → "🔁 Builds on:" (v8.27). "Spiral" stays the teacher-side method name; ⭐ numbered-star convention unchanged.

**QUEUED DEBT — book-wide pill sweep (NOT applied):** ~47 pills across L01–L10 must move to the new scale — MEDIUM orange→blue ×27, HARD red→orange ×15, EXPERT→TOUGH purple ×5. The new hex map above is the authority. Its own scoped session.

**Carried to S43 (the L03 surgery, in order):**
- (3) L02 — "Builds on:" explainer callout (introduce ⭐ + "Builds on:" once, before L03's first marked card; at/before §9). Bumps L02.
- (4) L03 surgery — reorder 6→8 cards, inject Constrain + Ramp, move each `kind=` link + reveal block WITH its card (§15 gate), re-rate every pill to the 5-tier scale, add "Builds on:" markers (Battery ⭐L02 display, Constrain ⭐L02 constants). DELETE NOTHING. Then bump L03 v03.2.0 → **v03.3.0** (moderate, single).
- (5) Maker — starter payloads for `constrain` + `ramp` (§18.3 minimal skeletons); verify `?kind=` = starters. Two new kinds.
- (6) learner-mode the cards in the new order (Socratic). Grep Claude's own code vs canon — lib pin `pololu/Zumo32U4@2.0.1`.

---

## 📘 SESSION 41 — S40 DOCUMENTATION PASS (Bible v8.25 → v8.26)

Memory carried the S40 decisions; the FILES had not been updated. This session folded them into durable canon. **No lesson, payload, or byte changes** — Bible + LIVE.md only.

**Bible v8.25 → v8.26 (moderate).**
- **§14.1 THE LOG *IS* THE TDP (NEW):** the 16 Engineer's Log prompts accumulate into ONE growing Google Doc structured as a RoboCupJunior TDP — notebook and TDP are the same artifact. Template = `ZUMO_TDP_Template.md` (repo root, live, carries the v2 edits: solo "Robot & Author", four-turn wheel-base). Prompts stay in the lessons (one source of truth); the Doc holds only TDP scaffolding + PART A standing lists A1–A5.
- **§18 CHALLENGE-DESIGN CANON (NEW SECTION):**
  - **18.1 Saxon spiral** — each lesson's challenges reinforce 1–2 prior concepts alongside the new one; roll out going forward lesson-by-lesson, do NOT retrofit L01/L02; one new concept per rung.
  - **18.2 marker convention** — blue "🔁 Spiraled skills:" header line naming the source in words + inline ⭐ numbered stars (source lesson # inside). Assets `spiral_star_01..16` in `images/` (vector-path numbers, gold gradient) — built S40, DJ-approved, **not yet pushed**.
  - **18.3 starter principles** — minimal skeleton, includes + the ONE needed hardware object pre-placed, empty section headers ("// (none needed for this challenge)"), MY PLAN ships blank, marked "// write your code here" zone, don't re-explain setup()/loop(); challenge folder labels may take a C## prefix (output-string only, keep `kind=` ids, flat).

**Confirmed LIVE by clone (do not re-push):** S38+S39 content, the 5 image deletions, `ZUMO_TDP_Template.md` (root), `favicon.ico` (root).

**Spiral stars — LIVE:** all 16 `spiral_star_01..16.svg` pushed to `images/` this session (commit `b3467a6`, verified by clone). Ready to wire into challenge markers in S42.

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

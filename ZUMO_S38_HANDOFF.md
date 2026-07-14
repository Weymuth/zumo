# ZUMO SESSION 38 — HANDOFF

*Paste this at the top of the new chat. The repo is the source — clone it.*

---

## OPEN THE SESSION (do this first, before any work)

```bash
git clone --depth 1 https://github.com/Weymuth/zumo.git
grep -oE "Bible version: v[0-9.]+" zumo/ZUMO_SUPER_BIBLE.md     # expect v8.24 (UNCHANGED in S37)
grep -oE "Project Maker v2\.[0-9]+"  zumo/newproject.html        # expect v2.28
```

Then verify LIVE.md's date (**July 14, 2026 — Session 37 close, final**) and its lesson versions against the clone.
**If LIVE.md and the Bible disagree, ASK DJ. Never decide unilaterally.**

### ⚠️ FIRST THING: DID THE S37 PUSH LAND?

`ZUMO_S37_PUSH_3.zip` (the THIRD and final S37 zip — _1 and _2 are ghosts) was delivered at close. Verify by clone — which version landed, not just that something did:

| Probe | Expect |
|---|---|
| `newproject.html` | **v2.28** — skeleton builder indented (grep `\\n  waitForStart` in the builder strings) |
| `lessons/Lesson_01.html` | **v03.2.2** — §5.5 Complete Program uniformly 4-space; `slide it to the right, as you face the back` |
| `lessons/Lesson_02.html` | **v02.1.0** — contains `That Unnumbered Row, in 10 Seconds` |
| `lessons/Lesson_03.html` | **v03.1.1** — contains `this paper copy IS your EEPROM` |
| `lessons/Lesson_07.html` | **v04.3.5** — contains `the file count stops mattering` |
| `lessons/Lesson_10.html` | **v02.1.7** — pre in §8A.2 shows `  case PHASE_TURN_AWAY:` indented |
| `lessons/Lesson_12.html` | **v01.2.1** — contains `About those two giant numbers` |
| `lessons/Lesson_06.html` | v04.5.4 · `engine.py` at repo root · `images/L01_GRAPHIC_1-13_zumo_rear_view.svg` contains `slide RIGHT for ON` |

If any probe fails, **stop and tell DJ.**

### 🗑️ DELETIONS — a zip cannot delete. Run at push time (if not already run):

```bash
git rm images/L01_IMAGE_1-13_kr_c_programming_book.png \
       images/L07_GRAPHIC_7-16_six_file_architecture.svg \
       images/L08_GRAPHIC_8-03_project_file_tree.svg \
       images/L09_GRAPHIC_9-07_sensor_patterns.svg \
       images/L09_GRAPHIC_9-08_project_file_tree.svg
```

---

## STATE AT S37 CLOSE (FINAL)

L01 **v03.2.2** · L02 **v02.1.0** · L03 **v03.1.1** · L04 v04.0.5 · L05 v04.1.5 · L06 **v04.5.4** · L07 **v04.3.5** · L08 v04.1.3 · L09 v05.0.4 · L10 **v02.1.7** · L11 v02.2.0 · L12 **v01.2.1** · L13 v02.2.0 · L14 v02.4.0 · L15 v02.2.0 · L16 v02.2.0
**Bible v8.24 · Maker v2.28 · Gate v1.1 · Harness v3.0 · engine.py (repo root)**

- 🎯 Payload gate PASSES all 15 lessons vs Maker v2.28 (at close).
- 🧹 **Flat-code defect class CLOSED on every surface**: payloads (6 deliberate `broken_code` lines remain) · Maker skeleton builder (0) · all 16 lesson displays (0). There is no fourth surface — census methodology in LIVE.md S37 blocks.
- 📖 **Full external review pass complete, 16/16 lessons** (Grok): ~20 verifiable claims → 2 survivors (both built: L07 tip, L12 sentence), 2 DJ taste rulings (L03 EEPROM built · L08 duration pending bench), rest false positives — three of them the book's own coined phrases quoted back.
- 📌 INI gate PASSES. Byte figures untouched (whitespace/comments/prose don't compile).

---

## S38 QUEUE

1. **Q017 bench session (DJ, one robot, three riders):**
   a. **Green-tape numbers** — Step-9+ build → A → B calibration spin ON the course → STOPPED, slide white/green/black under the outer sensors → report six numbers. Decision table: inside ~300–700 with ≥100 clearance = CLOSED free · mildly outside = prose nudge, minor · badly outside (<200/>800) = EXPENSIVE (constants in gated payloads inherited L09→L15).
   b. **Calibration-spin stopwatch (Q044)** — time B-press → "Calibration done!". Claude's derived estimate: 1–2 s. A measured figure becomes one L08 sentence; unmeasured, no sentence ships.
   c. **Gyro-bias stopwatch (Q046 — DJ has not yet ruled)** — optionally time L12+ boot bias collection the same way, same rule: measured or nothing.
2. **Q037 ruling — L01 "Coming from Arduino?" callout** (4–5 bullets: PlatformIO not IDE · exact-pinned lib · 32U4 drops USB on reset · checkpoint ritual · "pace outlet = HARD challenges"). Approve / modify / drop. Q032 already ruled NO skip lane.
3. **Stale-image `git rm`** at push time (above).
4. **22-photo queue** (DJ — `IMAGE_SHOT_LIST.md`).
5. 🔴 **AI Tutor rebuild — LAST.** Standing ruling.

---

## PARKED — DO NOT RE-OPEN UNPROMPTED

- **Challenge solution-disclosure** (DJ rules after classroom use; options D/E/F in Claude's memory).
- **L05 internal 4-space indentation** (its own convention; house canon elsewhere is 2-space, measured 34,738 vs 268).
- "Know Your Zumo" board-map page · §9 difficulty grouping · L06 card pattern · L04 §3.6 compile-test · gate filename regex (copy to `Lesson_NN_x.html` first) · L15's rung-heading checkpoint idiom (deliberate genre difference, byte figures audited — not a defect).
- Grok L01–L16 claims: ALL dispositioned. Do not re-triage repeats.

---

## WHAT S37 LEARNED (the expensive ones — see LIVE.md for the full set)

- **Vague reviewer flags can be real defects wearing bad words** — verify against raw file STRUCTURE, not content. The formatting reversal came from Grok's vaguest sentence.
- **Census every emitting surface.** S37's first census measured PAYLOADS only; the skeleton BUILDER (concatenated JS strings that generate fresh projects) carried the same defect at its root. Surfaces: payloads · builder/template strings · lesson pre displays. No fourth.
- **The gate is lenient to indentation and trailing-comment ADDITIONS both directions; only line removals orphan.** Proven property — makes formatting repair decomposable.
- **Raw-indent (spaces prepended to raw HTML lines, depths from decoded text) beats re-rendering** — zero markup churn, no per-lesson fidelity requirement. Escaping styles differ per lesson; byte-exact re-render is impossible in some (L03).
- **Fix internal consistency in the block's own convention** — L01's §5.5 is a 4-space block; the repair used 4, not the 2-space house canon.
- **Reviewer echo tell:** when a suggestion arrives in quotes, grep it — three times the "suggestion" was the book's own coined phrase (leap of faith · may-not-refuse-the-match · numbers-not-adjectives).
- **`engine.py` (repo root):** indenter, raw-indent, flat-only variants, fidelity-testable highlighter, payload surgery. Reuse; don't rebuild.
- **Duration claims ship measured or not at all** — a derived figure is still a guess with citations.

---

## CONTAINER SETUP (rebuild each session)

```bash
pip install cairosvg --break-system-packages
# AVR toolchain + 9 dep repos only if compiling — see pio_harness.sh v3.0
```

**Gate quirk:** copy lessons to `Lesson_NN_x.html` before running the gate.
**Push order (blocking):** SVGs → `images/` · `newproject.html` → Pages · lessons → Canvas (Canvas last).
**Delivery (Bible §12):** everything lives in the repo · session open = clone · session close = ONE zip, repo layout, every changed file including root docs · removals = explicit `git rm` lines.

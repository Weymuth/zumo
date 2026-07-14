# ZUMO SESSION 38 — HANDOFF

*Paste this at the top of the new chat. `LIVE_ZUMO_TEXTBOOK.md` lives in the repo — clone, don't upload.*

---

## OPEN THE SESSION (do this first, before any work)

```bash
git clone --depth 1 https://github.com/Weymuth/zumo.git
grep -oE "Bible version: v[0-9.]+" zumo/ZUMO_SUPER_BIBLE.md     # expect v8.24 (unchanged S37)
grep -oE "Project Maker v2\.[0-9]+"  zumo/newproject.html        # expect v2.27
# -E and "+" are load-bearing: a greedy "*" matches the Bible's own example.
```

Then verify LIVE.md's date (**July 14, 2026 — Session 37 close**) and its lesson versions against the clone.
**If LIVE.md and the Bible disagree, ASK DJ. Never decide unilaterally.**

### ⚠️ FIRST THING: DID THE S37 PUSH LAND?

`ZUMO_S37_PUSH.zip` was delivered at S37 close but **not confirmed pushed.** Verify by clone — and check **which version** landed:

| File | Expect |
|---|---|
| `newproject.html` | **v2.27** — L02/L03 payloads indented (e.g. `finished` for lesson 2 contains `\n  Serial.begin` escaped) |
| `lessons/Lesson_01.html` | **v03.2.1** — contains `slide it to the right, as you face the back` |
| `lessons/Lesson_02.html` | **v02.1.0** — contains `That Unnumbered Row` (the prototype teaser) |
| `lessons/Lesson_03.html` | **v03.1.0** · `Lesson_06.html` v04.5.4 · `Lesson_07.html` v04.3.4 |
| `engine.py` | present at repo root |
| `images/L01_GRAPHIC_1-13_zumo_rear_view.svg` | contains `slide RIGHT for ON` |

If the clone still shows Maker v2.26, **the push did not happen** — stop and tell DJ.

### 🗑️ DELETIONS — a zip cannot delete. Run at push time:

```bash
git rm images/L01_IMAGE_1-13_kr_c_programming_book.png \
       images/L07_GRAPHIC_7-16_six_file_architecture.svg \
       images/L08_GRAPHIC_8-03_project_file_tree.svg \
       images/L09_GRAPHIC_9-07_sensor_patterns.svg \
       images/L09_GRAPHIC_9-08_project_file_tree.svg
```

All five verified 0 references (S37, fresh clone). ⚠️ The S37 handoff's version of this command used
truncated globs (`L01_IMAGE_1-13.*`) that matched **zero files** — real names carry suffixes. Verify
pathspecs against a clone before publishing any command.

---

## STATE AT S37 CLOSE

L01 **v03.2.1** · L02 **v02.1.0** · L03 **v03.1.0** · L04 v04.0.5 · L05 v04.1.5 · L06 **v04.5.4** · L07 **v04.3.4** · L08 v04.1.3 · L09 v05.0.4 · L10 v02.1.6 · L11 v02.2.0 · L12 v01.2.0 · L13 v02.2.0 · L14 v02.4.0 · L15 v02.2.0 · L16 v02.2.0
**Bible v8.24 · Maker v2.27 · Gate v1.1 · Harness v3.0 · engine.py NEW**

- 🎯 Payload gate PASSES all 15 lessons against Maker v2.27.
- 🧹 **Payload indentation clean book-wide** — final census: 6 flat lines total, all in L02 `broken_code` (deliberate).
- 📌 INI-consistency gate PASSES. 📐 Published byte figures untouched (whitespace/comments don't compile).
- ✅ L02 §5 green-LED bench check **CLOSED from Pololu §3.2** — the book was right (green = USB TX); the display-interface cause was added.

---

## S38 QUEUE

1. **Q017 — L09 green-tape bench check** (DJ, on a robot). Procedure: any L09 Step-9+ build → A → B calibration spin **on the course** → while STOPPED slide white/green/black under the outer sensors → report all six numbers.
   Decision table: **inside ~300–700 with ≥100 clearance** → defaults stand, zero cost · **mildly outside** → prose-only nudge, minor bump · **badly outside (<200 or >800)** → changing `GREEN_LOW/HIGH` constants is EXPENSIVE — they live in gated payloads inherited L09→L15 (re-gate + byte re-audit). Don't order casually.
2. **Q037 — "Coming from Arduino?" callout for L01** (DJ ruling). Q032 ruled NO skip lane; the open option is a 4–5 bullet callout mapping what's *different* here (PlatformIO not IDE · exact-pinned lib · 32U4 drops USB port on reset · pace outlet = HARD challenges). Build / drop.
3. **Stale image deletions** — the `git rm` above, at push time.
4. **22-photo queue** (DJ — `IMAGE_SHOT_LIST.md`).
5. 🔴 **AI Tutor rebuild — LAST.** Standing DJ ruling.

---

## PARKED — DO NOT RE-OPEN UNPROMPTED

- **Challenge solution-disclosure** (DJ rules after classroom use; options D/E/F held in Claude's memory).
- "Know Your Zumo" board-map page · §9 difficulty grouping · L06 card pattern.
- L04 §3.6 `initFiveSensors()` compile-test.
- Gate filename regex (`Lesson_NN.html` → copy to `Lesson_NN_x.html` first).
- **L05's internal 4-space indentation** (its own convention, internally mixed 2/4 — NEW S37, parked; house canon elsewhere is 2-space).

---

## WHAT S37 LEARNED (the expensive ones)

- **The flat-code defect class.** L02 (227 lines) and L03 (496) shipped payloads with ZERO indentation inside braces; L04–L07 carried 41 residue lines; L08–L16 were pristine — which is what proved flat was never the intent. Grok's vague "formatting issues" flag pointed at this; it was initially triaged FALSE POSITIVE from content-only checks and reversed on payload evidence. **Verify vague reviewer flags against raw file structure, not just content.**
- **House indent canon = 2-space** (measured: 34,738 depth-1 lines at 2 vs 268 at 4, the 4s all in L05).
- **The gate's line-wise fallback makes indentation and trailing-comment ADDITIONS safe in both directions** — a payload line stripped is a substring of its commented lesson twin. Only line REMOVALS/rewrites orphan payloads.
- **Identical bodies hide across step slots.** L07's `after_step_6/main.cpp` == `after_step_7/main.cpp` byte-for-byte — a count==1 assert on the escaped needle caught it; dedupe unique bodies before surgery.
- **`engine.py` is in the repo root.** Brace-depth indenter (block-comment aware) + syntax highlighter + payload-surgery helpers. **Fidelity-test the highlighter per lesson before rendering** (20/20 byte-exact on L02; L03's mixed escaping fails it — use `raw_indent` there, which never touches markup). `is_code_block()` excludes pseudo-code plan blocks — reindenting those destroys their column alignment.
- **Deliberately-flat artifacts:** L02 §1 mystery originals, `broken_code` (the find-3-syntax-errors challenge). Leave byte-identical.
- **Compositing trap:** a transparent PNG converted to grayscale reads its background as BLACK — composite onto white before pixel analysis. And when the image-view tool degrades mid-session, verify renders pixel-programmatically; never claim an eyeball that didn't happen.
- **Publish no command unverified.** The S37 handoff's `git rm` deleted nothing (globs vs suffixed names). Dry-run (`git rm -n`) against a clone first.
- **Power-switch canon (DJ bench ruling Q26): ON = slide RIGHT, as you face the back of the robot.** Green user LED = USB **TX** + display line; red = USB **RX** + display; the separate green **power** LED under the center rear edge = VBUS present; blue LEDs = battery power with switch ON, and the **left** one dims below ~3 V — one-blue-lit means an eneloop pack is far past the 4,200 mV floor.

---

## CONTAINER SETUP (rebuild each session)

```bash
pip install cairosvg --break-system-packages        # SVG visual QA
# engine.py ships in the repo — import for any indentation/highlighting/payload work
# AVR toolchain + 9 dep repos only if compiling — see pio_harness.sh v3.0
```

**Gate quirk:** copy lessons to `Lesson_NN_x.html` before running `gate_payload_match.py`.

**Push order (blocking):** SVGs → `images/` · `newproject.html` → Pages · lessons → Canvas.

**Delivery (Bible §12):** EVERYTHING lives in the repo. Session open = **clone**. Session close = **ONE zip, full repo layout, every changed file including root docs** — one extract, one commit, one push. **A zip cannot delete:** removals ship as explicit `git rm` lines (above).

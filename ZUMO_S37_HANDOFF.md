# ZUMO SESSION 37 — HANDOFF

*Paste this at the top of the new chat. Upload `LIVE_ZUMO_TEXTBOOK.md` with it.*

---

## OPEN THE SESSION (do this first, before any work)

```bash
git clone --depth 1 https://github.com/Weymuth/zumo.git
grep -oE "Bible version: v[0-9.]+" zumo/ZUMO_SUPER_BIBLE.md     # expect v8.24
grep -oE "Project Maker v2\.[0-9]+"  zumo/newproject.html        # expect v2.26
# NOTE the -E and the "+": with a greedy "*" the pattern matches its own
# example inside the Bible and returns a bogus second line.
```

Then verify LIVE.md's date (**July 14, 2026 — Session 36 close**) and its lesson versions against the clone.
**If LIVE.md and the Bible disagree, ASK DJ. Never decide unilaterally.**

### ⚠️ FIRST THING: DID THE S36 PUSH LAND?

`ZUMO_S36_PUSH.zip` was delivered at S36 close but **was not confirmed pushed.** Verify by clone — and check **which version** landed, not merely that a commit exists:

| File | Expect |
|---|---|
| `newproject.html` | **v2.26** · `lib_deps = pololu/Zumo32U4@2.0.1` |
| `lessons/Lesson_01.html` | **v03.2.0** · 4 pinned strings |
| `lessons/Lesson_14.html` | **v02.4.0** · exactly **16** Maker links |

If the clone still shows Maker v2.24 / L14 with 17 links, **the push did not happen** — stop and tell DJ.

---

## STATE AT S36 CLOSE

**The book is code-complete, fully wired, and gate-clean.**

L01 v03.2.0 · L02 v02.0.31 · L03 v03.0.13 · L04 v04.0.5 · L05 v04.1.5 · L06 v04.5.3 · L07 v04.3.3 · L08 v04.1.3 · L09 v05.0.4 · L10 v02.1.6 · L11 v02.2.0 · L12 v01.2.0 · L13 v02.2.0 · L14 v02.4.0 · L15 v02.2.0 · L16 v02.2.0
**Bible v8.24 · Maker v2.26 · Gate v1.1 · Harness v3.0**

- 🔗 **Every Maker kind is reachable from its lesson: 99 kinds / 99 links, clean 1:1.**
- 🎯 Payload gate PASSES all 15 lessons.
- 📌 `lib_deps` is pinned exactly. INI-consistency gate passes.
- 📐 All published byte figures byte-identical (S34 audit intact).
- ✅ Pass B (prose read-through) COMPLETE, all 16.
- 🎨 Claude's SVG queue is EMPTY except one item (below).

---

## S37 QUEUE

1. **Power-switch art** *(the only Claude-buildable item)* — `L01_GRAPHIC_1-13_zumo_rear_view.svg` labels **where** the power switch is but not **which way is ON**, while L01's prose says *"slide it toward the tracks."* Redraw with a direction indicator. Overwrites the live file at the same name (art change = **minor bump**, L01 → v03.2.1). SVG canon: 1100×850 viewBox, blue gradient title band (#1a5276→#2e86ab), single-polygon arrows only. Render via `cairosvg` and eyeball the PNG before presenting.
2. **DJ bench checks** (10 seconds each, on a robot):
   - L02 §5 Step 5 claims the green LED flicker is *"the USB activity light."* Pololu says green/red share lines with the DISPLAY interface on the OLED board. Which is it?
   - L09 green-tape band 300–700 on the calibrated scale (Q017, open since S33).
3. **Repo cleanup — 5 stale images, verified 0 references.** One command:
   ```
   git rm images/L01_IMAGE_1-13.* images/L07_GRAPHIC_7-16_six_file_architecture.svg \
          images/L08_GRAPHIC_8-03.* images/L09_GRAPHIC_9-07.* images/L09_GRAPHIC_9-08.*
   ```
4. **22-photo queue** (DJ — see `IMAGE_SHOT_LIST.md`).
5. 🔴 **AI Tutor rebuild — LAST.** Standing DJ ruling. `tutor.html` has stale titles and no L12+ content.

---

## PARKED — DO NOT RE-OPEN UNPROMPTED

- **Challenge solution-disclosure.** The book has **no canon**: L06/L07/L11/L13/L14 publish solutions · **L08/L09 withhold them** · L10 gives neither · L12/L15 print a scaffold with a blank. DJ ruled S36: *"leave things as they are for now; I'll make the call after I go through them as a student."* Three options (D chosen / E / F) are held in Claude's memory with their costs.
- "Know Your Zumo" standalone board-map page (after the book is done).
- §9 difficulty grouping (h4 group labels) · L06 goal→logic→template card pattern.
- L04 §3.6 `initFiveSensors()` compile-test.
- Gate filename regex — `gate_payload_match.py` still can't parse `Lesson_NN.html`; copy to `Lesson_NN_x.html` first.

---

## WHAT S36 LEARNED (the expensive ones)

- **The Maker is NOT uniformly formatted.** `PAYLOADS` is pretty-printed for some lessons and **compact single-line for others** (L14's whole block is ONE line). A line-based deletion (`rfind('\n')`) silently collapsed PAYLOADS from 15 lessons to 10 — **and the JS still parsed.** Cut by exact offset, then re-parse in `node` and assert lesson count, dangling refs, and orphans. A syntax check will not save you. → **Bible §15.5**
- **Neither is the lesson uniform.** Back-to-top markup has **four** distinct forms across L11–L16. Bonus mysteries are `h3` in L11/L15/L16, `h4` in L13/L14, and **heading-less `<div>` cards in L12**. L11's `Step N` headings also appear in §8A.4 *theory*. Hand-place every anchor; `assert count==1`; audit each link against the heading it **actually** landed under.
- **`finished` IS the last step.** Step kinds cover 1..N−1 only. L14 had a `step_4` kind whose payload was byte-identical to `finished` — one build under two names. → **Bible §15.2**
- **A bad pin is fixed by pinning correctly, never by unpinning.** L01 published *"Remove the version pin"* as the fix for a typo'd `^2.1.0`, and the fleet ran unpinned for a year. There is no 2.1.0 and there never was; the registry has only 2.0.0 and 2.0.1. → **Bible §5b**
- **Check whether the fix already exists.** Two of four Grok L01 items were **false positives** — debounce is fully taught in the "While-Loop Trapdoor" callout, and the LED syntax was already consistent. Survey before building, even for prose.
- **Verify a push by fresh clone, and check WHICH VERSION landed.**

---

## CONTAINER SETUP (rebuild each session)

```bash
pip install cairosvg --break-system-packages        # SVG visual QA
# AVR toolchain + 9 dep repos only if compiling — see pio_harness.sh v3.0
```

**Gate quirk:** `gate_payload_match.py newproject.html Lesson_NN_x.html ...` — it cannot parse the plain `Lesson_NN.html` name. Copy first.

**Push order (blocking):** SVGs → `images/` · `newproject.html` → Pages · lessons → Canvas. Reversing it gives students broken images and dead Maker links.

**Delivery (Bible §12, rewritten S36):** **EVERYTHING lives in the repo** — Bible, LIVE.md, handoffs, scripts, harness, web tools, lessons, images. Session open = **clone**, never upload. Session close = **ONE zip, full repo layout, EVERY changed file including root docs** — one extract, one commit, one push. **A zip cannot delete:** removals ship as explicit `git rm` lines in the close note.

# ZUMO SESSION 38 — HANDOFF

*Paste this at the top of the new chat. The repo is the source — clone it.*

---

## OPEN THE SESSION (do this first, before any work)

```bash
git clone --depth 1 https://github.com/Weymuth/zumo.git
grep -oE "Bible version: v[0-9.]+" zumo/ZUMO_SUPER_BIBLE.md     # expect v8.24 (UNCHANGED in S37)
grep -oE "Project Maker v2\.[0-9]+"  zumo/newproject.html        # expect v2.27
```

Then verify LIVE.md's date (**July 14, 2026 — Session 37 close**) and its lesson versions against the clone.
**If LIVE.md and the Bible disagree, ASK DJ. Never decide unilaterally.**

### ⚠️ FIRST THING: DID THE S37 PUSH LAND?

`ZUMO_S37_PUSH.zip` was delivered at S37 close. Verify by clone — and check **which version** landed:

| Probe | Expect |
|---|---|
| `newproject.html` | **v2.27** · L02 `finished` payload indented (extract and eyeball, or grep the escaped body for `\n  `) |
| `lessons/Lesson_01.html` | contains `slide it to the right, as you face the back` and `green USB power LED` |
| `lessons/Lesson_02.html` | contains `That Unnumbered Row, in 10 Seconds` (the prototype teaser) |
| `lessons/Lesson_03.html` | **v03.1.1** — contains `this paper copy IS your EEPROM` |
| `images/L01_GRAPHIC_1-13_zumo_rear_view.svg` | contains `slide RIGHT for ON` |
| `engine.py` | present at repo root |

If any probe fails, **the push did not happen or landed partially — stop and tell DJ.**
Also check whether the 5 stale images are gone (the `git rm` below may or may not have been run — DJ's call, not a defect either way).

---

## STATE AT S37 CLOSE

**Code-complete, fully wired, gate-clean, and — new this session — formatting-clean book-wide.**

L01 v03.2.1 · L02 v02.1.0 · L03 v03.1.1 · L04 v04.0.5 · L05 v04.1.5 · L06 v04.5.4 · L07 v04.3.4 · L08 v04.1.3 · L09 v05.0.4 · L10 v02.1.6 · L11 v02.2.0 · L12 v01.2.0 · L13 v02.2.0 · L14 v02.4.0 · L15 v02.2.0 · L16 v02.2.0
**Bible v8.24 · Maker v2.27 · Gate v1.1 · Harness v3.0 · engine.py (new, repo root)**

- 🎯 Payload gate PASSES all 15 lessons (run against Maker v2.27 at close).
- 📐 Flat-inside-braces census: **6 lines book-wide, all in L02 `broken_code` — deliberate.** Everything else indented, 2-space house style.
- 📌 INI gate PASSES (one unique `lib_deps` string, Maker + L01).
- Byte figures untouched (whitespace/comments don't compile) — S34 audit intact.

---

## S38 QUEUE

1. **DJ bench check — Q017, L09 green-tape band** (tabled S37 with procedure ready):
   Any Step-9+ build → A → B calibration spin ON the course → while STOPPED slide white/green/black under the outer sensors → report six numbers.
   Decision table: both greens inside ~300–700 with ≥100 clearance → **CLOSED, zero cost**. Slightly outside → prose nudge, minor bump. Badly outside (<200 or >800) → **EXPENSIVE**: `GREEN_LOW/HIGH` live in gated payloads inherited L09→L15 — constant change = re-gate + byte re-audit across the chain. Do not order casually.
2. **Q037 ruling — L01 "Coming from Arduino?" callout.** DJ leans against a skip lane ("skip kid" risk); Claude proposed a 4–5 bullet differences callout (PlatformIO not IDE · exact-pinned lib · 32U4 drops its USB port on reset · checkpoint ritual) ending "your pace outlet is the HARD challenges." Approve, modify, or drop.
3. ~~Grok L03 EEPROM taste call~~ — **RESOLVED post-close (Q041)**: preview sentence shipped in L03 v03.1.1, framed so the paper record stays the hero. Other three L03 claims: false positives / no-action. L04 review also triaged post-close: 3 false positives, A+B on-screen hint **DECLINED (Q040)**.
4. **Repo cleanup** (if not already run):
   ```
   git rm images/L01_IMAGE_1-13_kr_c_programming_book.png \
          images/L07_GRAPHIC_7-16_six_file_architecture.svg \
          images/L08_GRAPHIC_8-03_project_file_tree.svg \
          images/L09_GRAPHIC_9-07_sensor_patterns.svg \
          images/L09_GRAPHIC_9-08_project_file_tree.svg
   ```
5. **22-photo queue** (DJ — `IMAGE_SHOT_LIST.md`).
6. 🔴 **AI Tutor rebuild — LAST.** Standing DJ ruling.

---

## PARKED — DO NOT RE-OPEN UNPROMPTED

- **Challenge solution-disclosure** (DJ rules after classroom use; three options in Claude's memory).
- **L05 internal 4-space indentation** — its payloads mix 2- and 4-space. Book canon is 2-space (measured: 34,738 vs 268, the 268 all L05). Surfaced S37, not ruled. Own item if DJ ever wants it.
- "Know Your Zumo" board-map page · §9 difficulty grouping · L06 card pattern · L04 §3.6 compile-test · gate filename regex (still copy to `Lesson_NN_x.html`).
- Grok L01 cosmetics already dispositioned; do not re-triage.

---

## WHAT S37 LEARNED (the expensive ones)

- **A vague reviewer flag can be a real defect wearing bad words.** Grok's "formatting issues / weird line breaks" was dismissed as a false positive — it was pointing at **flat-left code in the good versions**, book-wide: L02 227/227 flat, L03 496/496, residues in L04–L07, while L08+ were pristine. Verify flags against the raw file structure, not just the content.
- **The gate is indentation-lenient by design.** Its line-wise fallback strips payload lines and substring-matches the corpus — so indentation changes and *trailing-comment additions* are safe on either side independently; only line **removals/rewrites** can orphan a payload. This makes coordinated formatting repair decomposable.
- **Raw-indent beats re-render for indent-only work.** Prepending spaces to raw pre-inner HTML lines (depths from decoded text) touches zero markup and needs no fidelity guarantees. Re-rendering requires a per-lesson fidelity test first: **escaping styles differ by lesson** (L02 fully escaped; L03 mixes raw `>`/`&&` with entities — byte-exact re-render is impossible there).
- **Exclude prose from the indenter.** Pseudo-code plan blocks (`setup() → no changes`, column-aligned tables) are destroyed by reindenting. Classifier: `→` present or <50% code-shaped lines → hands off.
- **Identical bodies ride multiple payload slots.** L07's `after_step_6/main.cpp` == `after_step_7/main.cpp` byte-exact (file unchanged between steps). Needle surgery must dedupe by body, not by slot.
- **`/* */` block comments span lines as ONE span** in lesson markup; highlighters and brace-counters must both be block-comment aware.
- **`engine.py` is in the repo root** — indenter (`reindent`, `raw_indent`, flat-only variants), fidelity-testable highlighter, payload brace-span/escape surgery. Reuse it; don't rebuild it.

---

## CONTAINER SETUP (rebuild each session)

```bash
pip install cairosvg --break-system-packages        # SVG visual QA
# AVR toolchain + 9 dep repos only if compiling — see pio_harness.sh v3.0
```

**Gate quirk:** copy lessons to `Lesson_NN_x.html` before running the gate.

**Push order (blocking):** SVGs → `images/` · `newproject.html` → Pages · lessons → Canvas. One GitHub Desktop commit covers the repo; Canvas is the step that must come last.

**Delivery (Bible §12):** EVERYTHING lives in the repo. Session open = clone. Session close = ONE zip, full repo layout, every changed file including root docs. A zip cannot delete — removals ship as `git rm` lines in the close note.

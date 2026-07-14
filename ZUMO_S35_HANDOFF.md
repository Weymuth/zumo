# ZUMO_S35_HANDOFF.md — paste at the top of the next chat

**Session 35 open ritual:** DJ uploads `LIVE_ZUMO_TEXTBOOK.md` (dated **July 14, 2026, Session 34 close**). Claude verifies date/status/versions AND the Bible internal line (`grep -o "Bible version: v[0-9.]*"` → expect **v8.20**). If anything conflicts, ASK DJ. Fresh-clone the repo before touching any lesson.

## Where S34 ended

- **PASS B IS COMPLETE** — all 16 lessons read; every defect fixed and live.
- **THE BYTE RE-AUDIT IS DONE AND LIVE** — 55 PIO-true compiles; every published byte count in the book is now compiler truth; L16 verified perfect (the wall = +626 exactly). Harness recipe: install `gcc-avr avr-libc binutils-avr` (7.3.0 = PIO's version), clone the 9 dep repos + ArduinoCore-avr into `/home/claude/harness/`, run `pio_harness.sh --setup`, use `extract_project.py` to materialize Maker payloads (`after_step_*` are complete 8-file snapshots; anchor is `var PAYLOADS = `). **Always control-run L15/finished first — must print `flash=28034`.**
- **L14 was rebuilt** against the official 2026 rules (`ROBOCUP_RESCUE_LINE_2026.md`, repo root — the sole source of truth for competition claims).
- **DJ now pushes via GitHub Desktop clone** and ruled **zip-per-session delivery**: Claude ships ONE zip, repo layout, final filenames. See `PUSH_WORKFLOW.md`.

## S35 job #1 — HEADER NORMALIZATION, L11→L16 (Q27 = System A)

Convert everything to the L01–L10 look: banner `<div>` wrapper + `<div id="section-N">`, **blue `#3498db` §1–3, green `#3a7d5c` §4–6**. Canon markup (from L08):

```html
<div style="background-color: #3a7d5c; color: white; padding: 13px 18px; border-radius: 8px 8px 0 0; margin-top: 24px;">
<div id="section-4" style="font-size: 1.15em; font-weight: bold;">🔧 Section 4: ...</div></div>
<div style="border: 2px solid #3a7d5c; border-top: none; border-radius: 0 0 8px 8px; padding: 20px 25px; background: white;"> ...content... </div>
```

- **L11:** green swap only, `#2a5a42` → `#3a7d5c` (banner + matching content borders).
- **L12–L14:** `<h2 id="section-N">` + blue underline → banner divs; wrap section content to the next header in the border box. Check what colour L01–L10 use for §7–§10 before assuming (only §1–6 were surveyed).
- **L15–L16:** gradient `<h2 id="s1..s10">` → banner divs AND ids `s1..s10` → `section-1..10` (+ `s8a`→`section-8a`, `bonus/glossary/quickref` unchanged). All TOC links are self-contained per lesson — verified: **zero cross-lesson section links exist.**
- **The freshly corrected byte counts must survive untouched** — run the residue sweep after conversion.
- **Add a header-consistency check to the gate battery** (renderer strips styles; this drift was invisible to every text-based audit — that's how it survived 33 sessions).

## S35 job #2 — MAKER WIRING, L11→L16 (same version bump as job #1)

~100 kinds built, gated, live, and unreachable: L11:18 · L12:21 · L13:19 · L14:13 · L15:16 · L16:8. Wire links at the matching step/ladder/challenge/bonus anchors, style-matched to L02–L10's link pattern (`https://weymuth.github.io/zumo/newproject.html?lesson=N&kind=K`). `step_4_RED` is an orphan kind in the Maker (L10's link was cut in S34) — **DJ ruling needed:** delete from Maker (Maker bump) or leave dormant.

## S35 job #3 — Grok L01 batch + lib_deps pin

Four cosmetic L01 items (one minor bump): LED syntax note (`ledYellow(1)` bare vs objects) · debounce note (why `getSingleDebouncedPress()`, not `isPressed()`) · power-switch label → art queue · `lib_deps` line-break bench check. **lib_deps pin:** 2.0.1 is a real release; DJ's earlier error was syntax. Bench-test `@^2.0.1` / `@~2.0.1` / git-tag on DJ's machine → moderate bump (Maker + L01 prose + Bible) when resolved.

## Also queued

- **Bible bump** — four S34 canon entries are written in LIVE.md's "NEW CANON" block, not yet in the Bible: byte canon + audited ladder, competition canon, header canon, delivery canon.
- DJ bench checks: L02 green-LED claim · L09 green-tape (Q017).
- Delete 5 unreferenced images (list in LIVE.md) — trivial now via the clone.
- 22-photo queue (DJ) · AI Tutor rebuild **LAST**.

## Discipline reminders (unchanged)

Bounded edits with `assert count==1` · normalized diff audit · structural gate · payload gate (copy lessons to `Lesson_NN_x.html` first) · fresh-clone verify every push AND check which version landed · `present_files` everything, flat + the session zip · numbered questions at close, most important first · a wrong answer is 3× worse than a blank · regenerate LIVE.md **LAST**, version appears TWICE (status line + verify banner).

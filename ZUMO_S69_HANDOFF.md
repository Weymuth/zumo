# ZUMO — S69 Handoff (written at S68 close, Jul 24 · paste at top of Session 69)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **16** must PASS. Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. Grep the actual file, never trust a pasted version number.
6. Recompute every mean from the files, by script, on the canonical 1–5 / 1–3 scales. Never hand-sum.
7. **NEW (§24.6b):** any gate you add, control-run against the UNFIXED source first. A gate that has only
   ever been pointed at corrected files has proved nothing.

## LIVE STATE at S68 close (pending DJ push — verify by fresh clone at S69 open)
L01 **v03.6.5** · L02 v02.13.4 · L03 **v03.11.0** · L04 v04.5.3 · L05 **v04.6.0** · L06 **v04.10.1** ·
L07 **v04.6.2** · L08 **v04.5.1** · L09 v05.3.1 · L10 v02.4.1 · L11 v02.6.2 · L12 **v01.6.2** ·
L13 **v02.5.2** · L14 **v02.7.2** · L15 **v02.5.2** · L16 **v02.4.1**
Bible **v8.50** · Maker v2.45 (unchanged) · Gate v1.6 · Harness v3.0 · pill_sweep v1.0 ·
**book_gates v1.2** · going_deeper v01.0.0. All 16 gates PASS. Base commit at S68 open: `79b391e`.

**Push order:** images before lesson HTML · lessons · docs/LIVE.md anytime. Maker unchanged this session.
**New image files (4):** `L05_GRAPHIC_5-01_robot_sees_obstacles.svg` (REPLACES the live one),
`L05_IMAGE_5-05a_array_three_live_factory.png`, `L05_IMAGE_5-05b_array_five_live_fivedown.png`,
`L05_IMAGE_5-06_proximity_facing_directions.png`.

---

## DONE IN S68

1. **The panel-close defect class — 8 lessons repaired.** L01/L12–L16 had an orphaned `</div>` past
   `</html>`; L06/L07 had the close after the footer, sealing end matter inside the Image Index box.
   Counts balanced *because* of the bug, so `tag balance` had always passed. Git provenance: L01 from its
   first tracked commit; L12–L16 all five from ONE commit `94acc10` (S35 boxed-section conversion — a
   stateful transform whose last panel had no terminator). All fixes count-preserving.
2. **book_gates v1.2 — parse, not count.** One real HTML parse gate + one semantic end-matter gate,
   replacing the two narrow checks. Control-run on the unfixed clone: 12 parse problems + 2 end-matter
   violations. 16 gates total.
3. **Bible v8.50 — §24.6 / §24.6a / §24.6b.**
4. **GRAPHIC 5.1 redrawn.** Was ±25.5° forward fan; hardware truth (Pololu 0J63 §3.5/§3.6 + DJ's annotated
   board photo) is side-facing. Now LEFT −90.1° · FRONT 0.0° · RIGHT +90.1°. Scene "box far left" →
   "wall alongside". Caption, alt, index row, §1 prose all moved with it. **L05 v04.6.0** (banner 04.6).
5. **L05 photos.** IMAGE 5.6 (§4.1, proximity facing directions) · IMAGE 5.5a/5.5b (§7.3, factory 1·3·5 vs
   five-down 1–5). A first candidate was reverted pre-ship: it was the #1419 six-sensor Zumo Reflectance
   Sensor Array (Zumo shield for Arduino), not the students' #3122 front sensor array.
6. **L03 §8A.5 arrays + §8A.6 modulo** + `qr-array` / `qr-modulo` + C05 "Where to look" re-pointed (it had
   pointed at its own hint). C05 re-rated Tough/Deep → **Tough/Moderate**, grasp axis only — **ramp
   untouched, L03 stays 1.88 on the doing axis.** **L03 v03.11.0** (banner 03.11).
7. **Going Deeper pointers → L07, L08, L12, L15, L16.**
8. **Verified already done:** `data-kind` explicit on all **87** cards. L03's 1000 ms explainer, power-on
   Tip and AI-autocomplete Warning all live in §3.7/§7 with bare §6.6a labels.

## S68 PROCESS NOTES
- DJ caught GRAPHIC 5.1 by eye after four independent mechanical checks passed it. The drawing was
  internally consistent and modelled the wrong robot. **No gate can catch that class** — §24.6a exists
  because of it, and it is the argument for DJ's rolling human read.
- The wrong-board photo was caught by reading the silkscreen (©2012, six positions) against the product
  line before shipping. Check the board revision on any Pololu photo before it goes in the book.

## OPEN — NEEDS A DJ RULING
- **L03 C05's inline "🆕 New operator: %" box** now duplicates §8A.6. **DJ PAUSED this — do not act.**
  Options when it reopens: trim to a one-line pointer at §8A.6, or keep as point-of-use reminder.
- **Spiral marking format review** — the S67 batch shipped under an Inferred format ruling; DJ should
  eyeball one card marker + one prose marker rendered and bless or restyle.
- **L16 zero challenge cards** — flagged three times now, still unruled.
- **DJ's own tier pass** + **rolling depth read (L14 first)** — both still to come.

## STANDING QUEUE (carried)
- **L05 follow-up (NEW):** §3/§8A prose still describes proximity in "ahead of you" terms in places —
  worth a read now that 5.1 says flanks. Also consider whether GRAPHIC 5.5's cone angles match the new 5.1.
- **BENCH:** compile-verify L07 finished + trapezoid · L08 + Racing Line · L11 C4 double-TRIM mirror-drift ·
  Q017 L09 six numbers · calibration-spin stopwatch · gyro-bias · L02 §5 green-LED · Constrain RUN_MS.
- **L03/L04 timer audit** · **L15 C04–C07 no-template shape** (logged deliberate) ·
  **L03 open:** L01 VS Code multi-root step · **Landing-page/book color mismatch** ·
  **Maker batch** (bulk DL · `?lesson=N` gate · C## labels · verify `?kind=` starters) ·
  **TDP v3 A5 Lab Log** · **course docs** (grid + syllabus) · **"pick your robot" chooser** ·
  **AI Tutor DISCOVERIES picker** (needs `data-kind="discovery"`) · Housekeeping: `QA_*` sheets in
  images/glowbots · border inset 10–18px vs 64px ("leave for now") · stray `.DS_Store` committed.
- **RESOLVED, strike from queue:** stray `</div>` after `</html>` (fixed + gated) · `data-kind` explicit
  (already complete) · Going Deeper pointers (done) · L03 arrays/modulo/1000ms/Coach's Tips (all closed).

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page.

---
*Written at S68 close, Jul 24 2026. A gate that counted was replaced by a gate that parses, and the one
defect neither could catch was found by a human looking at the picture.*

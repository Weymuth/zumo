# ZUMO — S66 Handoff (written at S65 close, Jul 24 · paste at top of Session 66)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. **NEW ritual step:** `python3 book_gates.py` — all 14 must PASS before any work. Then
   `python3 pill_sweep.py --audit lessons/Lesson_*.html` as before.
5. LIVE.md wins over memory. Grep the actual file, never trust a pasted version number.
   *A handoff can never name its own commit hash; live HEAD one past this file is expected.*

## LIVE STATE — verified by fresh clone, Jul 24, commit `92bef0d`, ALL 14 GATES PASS
L01 **v03.6.4** · L02 **v02.13.4** · L03 v03.10.1 · L04 **v04.5.2** · L05 v04.5.0 · L06 v04.9.0 ·
L07 **v04.5.1** · L08 v04.4.0 · L09 v05.3.0 · L10 v02.4.0 · L11 v02.5.0 · L12 **v01.6.0** ·
L13 v02.5.0 · L14 v02.7.0 · L15 v02.5.0 · L16 **v02.4.0**
Bible **v8.49** · Maker **v2.43** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0 ·
**book_gates v1.1 (NEW)** · **going_deeper v01.0.0 (NEW)** · tutor/tutor.html updated

---

## DONE IN S65 (nine pushes; Bible v8.44 → v8.49)

1. **L02 depth pass** — brace style + one-liner trap (§6.13) · full F() explainer · short-circuit ·
   why-not-what · semicolon habit · qr-flash · robot recipe table · notebook card PNG · "Three Builds
   That Fail" · **10 live timer iframes** (every timed challenge in L02 now has a real countdown, 20 total).
2. **F() reminders** in L12 + L16 only — the two lessons with memory prose on the page (L07/L14/L15
   evaluated and rejected; L07 has zero memory prose, L14/L15 "ceiling" = sensor timeout).
3. **`going_deeper.html` v01.0.0** — six collapsible entries, each anchored to a chapter (§23);
   linked from index tools row + end of L01/L02 Quick Reference.
4. **Terminal color canon (§22)** — SUCCESS `#6a9955` (DJ-ruled, deliberately the comment green — do NOT
   "correct" toward the terminal's brighter true green), errors `#f14c4c`, **diagnostic line only** (source
   echo + caret stay plain — L02's look-up-one-line rule depends on the student judging that line).
5. **The Challenge name split (§4.1/§4.2)** — Warm-Up N / TRY IT / Challenge N / Bonus Challenge N.
   Every practice construct tagged (`data-challenge` + `data-kind`, suffix w/t); 104 unique markers.
   **tutor/tutor.html** now groups the picker by kind; no `data-kind` still = canonical card.
6. **§4.3** — the picker label is the element's own textContent; constructs must name themselves
   (learned from shipping six identical "TRY IT (1 minute)" options).
7. **book_gates.py v1.1 (§24)** — 14 whole-book gates, run at open + before every delivery.
   §24.3 gate the whole field not the captured group; §24.4 computed claims verified by computation.
8. **DEPTH_AUDIT_S65.md (§24.5)** — the systematic depth findings map for the rolling human read.
9. Accuracy fixes from the L01/L02 read: byte count 17-not-18 · L02 banner June→July · L01 =/== promise
   reworded (L02 §3.2c defers it to L03 deliberately).

## ⚠ S65 PROCESS LESSON (the reason §24 exists)
Three times a named fix left the same defect class alive elsewhere and DJ had to re-ask
(labels-not-widgets · version-not-date in the same banner string · one byte count asserted from memory).
Root cause: **fixing the instance instead of the class.** The gates encode each class permanently.
When a new rule is canonized, write its gate in the same session (§24.2).

---

## S66 PRIMARY (unchanged, twice deferred): THE DIFFICULTY-PROGRESSION AUDIT
Full framing + both-axes lesson means table in the S65 handoff section of memory and S64's handoff.
Three findings await rulings: **L04 spike** (2.40/2.20, third-hardest doing sitting fourth) ·
**L07–L08 sag** (1.83/1.50 and 1.80; L07 C03 re-rate candidate — Medium with zero blanks) ·
**L11–L14 count collapse** (3 challenges each; DJ ruled "add to L11, don't cut L06"; L11 §8A.4 cliff
arithmetic and §7C TRIM-under-blindness are unused challenge candidates; new challenges are Part-B-scale).
DJ also wants his own tier pass and more **Tough** usage (2 uses book-wide).

## THE DEPTH ARC (new, from S65's audit — see DEPTH_AUDIT_S65.md)
- **DJ is doing the rolling human read personally.** Suggested order: **L14 first** (thinnest in book;
  "The Code Freeze" = 8 words) → L15 → L11–L13/L16 apparatus pass → MED candidates.
- **The apparatus cliff (verified):** L11–L16 have ZERO 📖 LEARN boxes and near-zero 🔑 KEY terms on the
  hardest material. Mostly a MARKING fix (promote existing strong prose — L12 §8A.3 is LEARN-quality
  wearing no box). Own arc, coordinate with DJ's read so fixes ship once.
- **Open candidate:** ternary `?:` may appear in L03/L05 before L06 §5.4 teaches it — needs line-level
  §11 verify (the same scan's pointer/bitwise hits were 100% false positives).
- **Rolling-read rule (§24.5):** any lesson a session substantially edits gets the full accuracy read in
  that same session — all three S65 accuracy finds were in freshly-edited content.

## STANDING QUEUE (carried)
- **L03/L04 timer audit** — L03 has 5 widgets / L04 has 3; check for text-only timed constructs (L02's
  pattern). Remember: a timer is an IFRAME, not a text label.
- **`data-kind` explicit on L01, L03, L05–L16 cards** — they work by defaulting to "challenge"; explicit
  tagging makes the picker self-documenting. Low priority, zero risk.
- **Going Deeper pointers for L07/L08/L12/L15/L16** — entries exist for them; DJ ruled L01/L02 only so far.
- **Going Deeper new entries** — page built to take more; every entry must pass the §23 anchor rule +
  §23.3 duplication grep (the fixed-point near-miss).
- **L15 C04–C07** — no template, no solution reveal (deliberate capstone shape, logged S64).
- **Stray `</div>` after `</html>`** in L01, L12–L16 — asked twice, never ruled. Harmless but unruled.
- **L03 open:** C05 arrays + modulo `%` explainers (oldest gap) · 1000ms=1s · Coach's Tips (power-on,
  AI-autocomplete) · L01 VS Code multi-root step.
- **Landing-page/book color mismatch** — no ruling yet (cheapest: lighten index.html).
- **Maker batch** (bulk DL · `?lesson=N` gate · C## labels · verify `?kind=` starters) ·
  **TDP v3 A5 Lab Log** · **course docs** (period grid + syllabus) · **"pick your robot" chooser**.
- **AI Tutor:** DISCOVERIES in the picker (needs `data-kind="discovery"` — the picker now already groups
  by kind, so only the lesson-side tagging remains).
- Housekeeping: `QA_*` sheets in images/glowbots · border inset 10–18px vs 64px spec (DJ: "leave for now").

## BENCH (need the robot)
Q017 L09 six numbers · calibration-spin stopwatch · gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page.

---
*Written at S65 close, Jul 24 2026. Nine pushes, Bible v8.44→v8.49, two new standing tools, and the book
gate-verified in its published state for the first time. Next: the progression audit (third attempt at
starting it) and DJ's rolling read, L14 first.*

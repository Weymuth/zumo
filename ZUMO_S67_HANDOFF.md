# ZUMO — S67 Handoff (written at S66 close, Jul 24 · paste at top of Session 67)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all 14 must PASS before any work. Then
   `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. Grep the actual file, never trust a pasted version number.
   *A handoff can never name its own commit hash; live HEAD one past this file is expected.*

## LIVE STATE at S66 close (pending DJ push — verify by fresh clone at S67 open)
L01 v03.6.4 · L02 v02.13.4 · L03 v03.10.1 · **L04 v04.5.3** · L05 v04.5.0 · L06 v04.9.0 ·
**L07 v04.5.2** · L08 v04.4.0 · L09 v05.3.0 · L10 v02.4.0 · **L11 v02.6.1** · L12 v01.6.0 ·
L13 v02.5.0 · L14 v02.7.0 · L15 v02.5.0 · L16 v02.4.0
Bible **v8.49** (unchanged — no new canon this session) · Maker **v2.43** (unchanged) ·
Gate v1.6 · Harness v3.0 · pill_sweep v1.0 · book_gates v1.1 · going_deeper v01.0.0
All 14 book gates PASS on the delivered set.

---

## DONE IN S66 — THE PROGRESSION AUDIT'S FIRST THREE RULINGS (third attempt, it finally started)

0. **Scale correction.** The S64 audit table's means only reproduce under a 4-point doing map
   (Hard=3, Advanced=4); canonical §6.12b is five tiers with Tough=3. Recomputed 1–5:
   L04 was **2.80** (second-hardest in the book at position 4/16), not the recorded 2.40.
   All shape findings survived the rescale. Recompute on 1–5 from now on.
1. **L04 card-by-card re-rate (DJ-approved, v04.5.3):** C1 keep Easy/Light · C2 Medium→**Easy**/Deep
   (1 blank, pseudocode states the answer; concept carries the load — L03 C08 shape) ·
   C3 Medium→**Easy**/Moderate · C4 Hard→**Tough**/Moderate · C5 Advanced→**Hard**/Deep.
   L04 doing 2.80→**2.00**; opening ramp now monotone: 1.36 → 1.67 → 1.88 → 2.00 → 2.20 → 2.62 (L01–L06).
   Flag logged: C2's Deep concept (arrival-vs-presence) taught in-card not §5/§8A — ruled covered,
   not a gap; verified load-bearing downstream (L09 transitions ×12, L13 literal "just arrived").
2. **L07 C03 Medium→Easy (DJ-approved, v04.5.2).** File-verified zero blanks, fully specified
   pseudocode — v8.44 transcribed-only class. L07 doing now 1.83 — sag deliberately exposed.
3. **L11 +2 challenges (DJ-approved, v02.6.1) — ZERO Maker/payload impact:**
   - **Challenge 4: Prove Your TRIM** (Medium/Moderate, prose) — three predict-then-measure gap
     runs (your TRIM / 0 / 2×). **Measurement method is DJ-ruled:** post-it at the starting point,
     robot's FRONT BLADE lined to its edge every run (the consistent reference), second post-it
     where it stops, labeled per run; measure each post-it's sideways distance from the line.
     Rides existing `cal_7c` kind. Solution: mirror pattern + open-loop compounding + sign-error
     diagnostic (runs 2 and 3 same direction = wrong TRIM sign).
   - **Challenge 5: The Cliff Arithmetic — Your Numbers** (Easy/Moderate, notebook-only) — rerun
     §8A.4 with your measured warning distance / speed / gap; compute your boom length; prove v
     cancels. All solution arithmetic computed per §24.4 (220 ms, 5.5 cm short).
   L11: N 3→5 · doing 2.33→2.00 · grasp 2.33→2.20. Banners 02.5→02.6 both homes; v02.6.1 is the
   post-delivery post-it revision (unique-version-per-delivery).
4. **Tough usage 2→3 book-wide** (L03, L13, now L04 C4).
5. A "does L03 teach DC motors?" check: DJ suspected the objective was untaught — verified it IS
   taught (silver-can LEARN + H-bridge LEARN + PWM chain). He was remembering an older L03.

## S66 PROCESS NOTE
The S64 table's 4-point scale understated the spike for two sessions. Same lesson as §24.4 in a new
coat: **a mean is a computed claim — recompute it from the files on the canonical scale, never
carry it forward from a handoff.** (No new Bible rule ruled; candidate if it recurs.)

---

## S67 CANDIDATES (audit continues — needs DJ rulings)
- **L07–L08 sag, now honestly visible:** L07 1.83 / L08 2.00 doing, sitting after L06's 2.62.
  Fix is harder capstones = Part-B-scale authoring, not re-rates. Ruling needed: author now or queue.
- **L12–L14 count collapse remains:** 3 challenges each. L11's fix used existing prose; L12–L14
  have no equivalent pre-written candidates identified yet — scan their §7/§8A for prose that could
  carry a card (the L11 pattern) before assuming Part-B authoring is required.
- **DJ's own tier pass** — still to come (his read, his re-rates).
- **DJ's rolling depth read, L14 first** (thinnest in book) — coordinate with the apparatus-cliff
  arc (L11–L16 zero LEARN boxes) so fixes ship once. NOTE: L11 now has two S66 cards — the
  apparatus pass on L11 should not disturb them.

## STANDING QUEUE (carried)
- **NEW BENCH:** verify L11 C4's double-TRIM mirror-drift on a real gap before classroom use.
- **L03/L04 timer audit** — text-only timed constructs (a timer is an IFRAME, not a text label).
  L11's two new cards have no timers (not timed constructs — confirm DJ agrees).
- **`data-kind` explicit on L01, L03, L05–L16 cards** (currently defaulting) — low priority.
- **Going Deeper pointers for L07/L08/L12/L15/L16** — entries exist; DJ ruled L01/L02 only so far.
- **Going Deeper new entries** — §23 anchor rule + §23.3 duplication grep.
- **L15 C04–C07** — no template, no solution reveal (deliberate capstone shape, logged S64).
- **Stray `</div>` after `</html>`** in L01, L12–L16 — asked twice, never ruled.
- **L03 open:** C05 arrays + modulo `%` explainers (oldest gap) · 1000ms=1s (partially addressed —
  L03 now has the ms explainer; verify) · Coach's Tips (power-on, AI-autocomplete) · L01 VS Code
  multi-root step.
- **Landing-page/book color mismatch** — no ruling yet.
- **Maker batch** (bulk DL · `?lesson=N` gate · C## labels · verify `?kind=` starters) ·
  **TDP v3 A5 Lab Log** · **course docs** (period grid + syllabus) · **"pick your robot" chooser**.
- **AI Tutor:** DISCOVERIES in the picker (needs `data-kind="discovery"` lesson-side tagging).
- Housekeeping: `QA_*` sheets in images/glowbots · border inset 10–18px vs 64px spec ("leave for now").
- **Spiral "Builds on:" markers absent L10–L12** — noticed S66 while matching L11 strata (new cards
  ship without them to match the lesson); retrofit question not opened, log only.

## BENCH (need the robot)
Q017 L09 six numbers · calibration-spin stopwatch · gyro-bias · L02 §5 green-LED · Constrain RUN_MS ·
**L11 C4 double-TRIM mirror-drift (NEW)**.

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page.

---
*Written at S66 close, Jul 24 2026. The progression audit started on its third attempt and shipped
three DJ-approved rulings: L04 re-rated to a monotone opening ramp, L07 C03 honestly Easy, and L11
grew from 3 to 5 challenges at zero Maker cost. Next: L07–L08 capstones, L12–L14 counts, DJ's tier
pass and rolling read (L14 first).*

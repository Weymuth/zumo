# ZUMO — S64 Handoff (written at S63 close, Jul 23 · paste at top of Session 64)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. LIVE.md wins over memory. **Grep the actual file/commit, never trust a pasted version number — or a summary's session number.**
   *A handoff can never name its own commit hash — the commit that writes it comes after. If live HEAD is one past this file, that is expected. Diff it to be sure.*

## LIVE STATE — verified by fresh clone, Jul 23, commit `1a906bc`
L01 **v03.6.1** · L02 **v02.10.1** · L03 **v03.10.1** · L04 v04.4.0 · L05 v04.4.0 · L06 v04.8.0 · L07 v04.4.0 · L08 v04.3.0 · L09 v05.2.0 · L10 v02.3.0 · L11 v02.4.0 · L12 v01.4.0 · L13 v02.4.0 · L14 v02.6.0 · L15 v02.4.0 · L16 v02.3.0
Bible **v8.43** · Maker **v2.43** · Gate v1.6 · Harness v3.0

S63 shipped in three commits: `12867ea` (glowbots) → `b678c75` (Bible v8.42 + LIVE) → `1a906bc` (slash + Bible v8.43).

---

## DONE IN S63

### 1. The robot icon family is LIVE — `images/glowbots/`, 42 files
25 **bordered** (5 robots × 1254/256/128/64/52, RGB) · 15 **glow** (5 × full-1186²/256/128, RGBA) · 2 QA contact sheets. Robots: Zumo · 3Pi · Romi · Balboa · Zircon.

**Buttons are bordered; images are glow** (DJ ruling). The border ring gives a silhouette that survives downsampling to 52px; a transparent cutout does not. **Glow floor is 128px** — below that the cut edge re-hardens and open-frame robots collapse.

**Bible §21 rewritten (v8.42).** The S61 "NEVER separate the robot from its glow" rule is **lifted** — it was written from a failed attempt. S63 cut all five, including the two §21.4 predicted would fail. Two findings made it work:
- **Edge-connected flood fill, not a brightness threshold.** Background = dark AND reachable from the crop edge, so interior dark pixels (Zircon's PCB, Balboa's frame gaps) survive by construction.
- **Cut the falloff; don't preserve it.** The glow is painted additively on black, so its outer falloff *is* black. Kept as soft alpha it renders as grey haze.

§21.7 is new: live file inventory + the uniformity spec (mean edge distance 1.28–1.32px, p95 2.00, zero opaque edge pixels). A new sibling icon must hit those numbers.

### 2. Split-pill slash halved (L01–L03)
`width: 8px; margin: 0 -4px` → `width: 4px; margin: 0 -2px`, all **25** pills (L01 11 · L02 6 · L03 8). Markup was uniform, zero variants. **The margin is structurally half the width** — change one, change the other, or a gap opens. Bible §6.12b updated (v8.43). Cosmetic → hidden-comment bump only, banners untouched per §5b.

---

## ⚠ PROCESS FINDING — QA ON WHITE (now Bible §21.3 canon)
Three glow defects shipped inside this session — a sliced dark stub on Balboa, a washed halo, and a grey cloud on Romi. **All three were invisible on the dark-background QA sheets I rendered and obvious on white.** DJ caught every one by eye and ultimately fixed three of the five masters in Photoshop; those became the reference, and 3Pi+/Balboa were tightened to match.

The general form: **test an artifact against the background it will actually be used on.** A transparent cutout QA'd on black cannot show a transparency defect.

---

## S64 NEXT — PRIMARY (unchanged from S63, still not started)
1. **DJ reviews the rendered L01–L02 split pills.** He has now seen the 4px slash and said "fine for now," but has **not** signed off on the split-pill design itself. That sign-off gates everything below.
2. **Then sweep L04–L16** — 53 pills, same method. Apply the two pending doing-axis re-rates in that pass:
   - **L05 C01 Detection Counter EASY→Medium** — identical boolean edge-detection pattern to L04 C02, which is MEDIUM. Two ratings for one concept.
   - **L14 C02 Strict Mode EASY→Medium** — three lines, but the challenge is a trick question about `while(true)`. Short, not easy.
   *Do NOT assume L04–L16 pill markup is uniform.* L01–L03 were verified 25/25 before editing; the S61 callout sweep hit ~8 drifted schemes. Re-extract and count first.
3. **Then the difficulty-progression audit proper**, now on two axes. Single-axis showed a clean floor (L01 1.45 → L02 2.00 → L03 2.12) and ceiling (L13 3.00 → L15 3.29) but a **flat, spiky middle**: L04 spikes to 2.80 — third-hardest in the book, sitting fourth — while L05, L07, L08 all sit at 2.00. L04's spike is real: C04 is "the first true sense-and-act program of the course" and C05 is closed-loop proportional control, L08's headline concept arriving four lessons early with no name attached.

---

## OPEN DEBTS FROM S63 (new)
- **Border inset** — all five bordered icons ship at **10–18px** against the **64px** §21.1 spec. DJ: "leave them for now." 64 remains the spec; the images are knowingly off it. Logged in the Bible as an open debt.
- **Filenames** — `Zumo_bordered_1254.png` etc. are S63 working names, not a ruled convention. `Zumo_Robot_Mark.png` (repo root `images/`) is the one pre-existing name.
- **`QA_*` sheets** — two working contact sheets are committed alongside real assets in `glowbots/`. `git rm` whenever.
- **Slash at 2px** — DJ floated halving again. **Not applied**, recorded as floated-only.

## ⚠ OPEN TEACHING GAP (marked, not fixed — carried from S62)
**L03 C05 Variable Speed** requires **arrays** and the **modulo operator `%`**. Neither appears anywhere in L03 prose (verified by grep, S62). Rated Tough / Deep.

---

## THE LANDING-PAGE / BOOK COLOR MISMATCH (raised S63, not started)
DJ: "it's weird that the launch page is black and then it goes white."

Measured: **19,197 hex values across 185 unique colors**, all inline (Canvas strips `<style>` and `class=`), so there is no stylesheet to flip. But the top five colors — `#569cd6` · `#b5cea8` · `#6a9955` · `#ce9178` · `#1e1e1e`, ~8,000 occurrences — are **VS Code Dark+ syntax highlighting**. Those are the code blocks and are *already* dark; changing them would break the deliberate match with the student's editor.

So the real shape is **dark code blocks inside a white page, against a fully dark `index.html`** — a page-background mismatch, not a palette mismatch. Darkening the book means recoloring ~11,000 non-syntax values, each a contrast decision, across 16 lessons: a Part-B-scale arc.

**Cheaper direction: lighten `index.html`** (one file, 12 colors) so it hands off into the book. Middle option: a dark transition band at the top of each lesson so the shift reads as deliberate. **No ruling yet.**

---

## STANDING QUEUE (carried)
- **L03 open:** array explainer + modulo `%` explainer (both C05 blockers) · 1000 ms = 1 second explainer · Coach's Tip upload/power-on sequence · AI-autocomplete warning · L01 VS Code multi-root workspace step.
- **"Pick your robot" chooser page** — now UNBLOCKED, the icon family is live.
- **Expand the 📓 ENGINEER'S LOG icon + section** — DJ likes the device.
- **Challenge-card Part-B redesign:** L06's Goal→Logic→Template pattern to all ~80–100 challenges.
- **Maker batch:** starters-only bulk download · `?lesson=N` gate · `C##` folder labels · verify `?kind=` downloads are starters not solutions.
- **TDP template v3:** A5 Lab Log (date · in/out · what).
- **Course docs:** day-by-day period grid + full syllabus.
- **AI Tutor (LAST):** add DISCOVERIES to the picker (needs `data-kind="discovery"`). *The tutor reads `data-difficulty` — confirm it tolerates `data-grasp` before the full sweep.*

## BENCH (need the robot)
Q017 L09 green-tape six numbers · calibration-spin stopwatch · gyro-bias · L02 §5 green-LED bench check · Constrain RUN_MS.

## PARKED (don't reopen unprompted)
Challenge solution-disclosure · monetization / ebook · "Know Your Zumo" reference page.

---
*Written at S63 close, Jul 23 2026. Icon family live and documented; slash halved. Next: DJ's pill sign-off, then the L04–L16 sweep, then the two-axis progression audit.*

# ZUMO — S65 Handoff (written at S64 close, Jul 23 · paste at top of Session 65)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. LIVE.md wins over memory. **Grep the actual file/commit, never trust a pasted version number.**
   *A handoff can never name its own commit hash — the commit that writes it comes after. If live HEAD is one past this file, that is expected.*
5. **New this session:** `python3 pill_sweep.py --audit lessons/Lesson_*.html` is a fast read-only health check on all 84 challenge cards. Expect `SWEPT` on L01–L15, `no challenges` on L16, and `0` distinct old style strings.

## LIVE STATE — verified by fresh clone, Jul 23, commit `3485255`
L01 **v03.6.1** · L02 **v02.10.2** · L03 **v03.10.1** · L04 **v04.5.0** · L05 **v04.5.0** · L06 **v04.9.0** · L07 **v04.5.0** · L08 **v04.4.0** · L09 **v05.3.0** · L10 **v02.4.0** · L11 **v02.5.0** · L12 **v01.5.0** · L13 **v02.5.0** · L14 **v02.7.0** · L15 **v02.5.0** · L16 v02.3.0
Bible **v8.44** · Maker **v2.43** · Gate v1.6 · Harness v3.0 · **pill_sweep v1.0**

S64 shipped in two commits: `d98a863` (L04/L05 + `pill_sweep.py`) → `3485255` (L02, L06–L15, Bible v8.44, LIVE.md).

---

## DONE IN S64

### 1. The split-pill sweep is COMPLETE
**84 challenges across 15 lessons**, every card carrying `data-difficulty` AND `data-grasp`, **zero** old single pills remaining (measured by `pill_sweep.py --audit`, not asserted). L16 is exempt — §6.12 tier-card variant, no challenge cards.

### 2. Six teaching gaps found and fixed
The grasping axis worked as §6.12b intends — a Deep rating against untaught prose *is* a gap:

| Lesson | Gap | Fix |
|---|---|---|
| L04 | `bool` state across `loop()` — 0 prose hits, C02 needs it | **§8A.8 NEW** |
| L04 | `abs()` + deadband — 0 prose hits, C05 needs it | **§8A.9 NEW** |
| L06 | polygon exterior angle — 0 prose hits, C03 says "you must calculate" | **§5.5 NEW** |
| L07 | "stub" used 9× in C05, never defined | one line in the card |
| L08 | `map()` — appears **once in the whole book**, as a fill-in blank | **`qr-map`** row + C04 pointer |
| L09 | `do…while` — supplied complete in C03, taught nowhere | **`qr-dowhile`** row + C03 pointer |

### 3. Three doing-axis re-rates
**L05 C01 Easy→Medium** and **L14 C02 Easy→Medium** (both carried in from the S63 handoff) · **L10 C03 Medium→Easy** (new — "print a counter", and its hint resolves the only non-obvious part). The book's single **Tough** (L13 C02) was deliberately kept so the tier stays live — DJ wants to use it more after his own pass.

### 4. Two missing footer banners repaired
L02 and L12 shipped with only the HEADER version banner. Both now carry the footer one, matched to their own neighbours' format (L02 → `<footer>` like L03; L12 → gradient div like L13), version derived from the hidden comment so the homes cannot disagree at birth. **All 16 lessons now have both §5b visible homes present and agreeing — a first for the project.**

### 5. Bible v8.43 → v8.44 — four rulings canonized
- **§6.12b** — sweep complete + the two-axis progression table + the six fixed gaps
- **§6.12c NEW** — inline CSS drifts per rebuild; match structurally
- **§11** — a transcribed-only construct gets a Quick Reference ROW, not a prose section
- **§5b** — both visible banner homes mandatory; match neighbours when restoring one

---

## ⚠ PROCESS FINDINGS — now Bible §6.12c canon

**Inline components drift per rebuild, and the drift is STRATA not rot.** The same visual pill carried **nine distinct style strings** across L04–L15 — same rendering, different CSS property order. Canvas strips `<style>` and `class=`, so every card holds its own inline copy and a component is never *edited*, only **retyped wholesale by whichever session rebuilds that lesson's cards**. Git proves it: L04 and L05 both began `padding`-first on Jul 12; L05 flipped to `background`-first on Jul 20 in `a3cd518` ("5, 12, 13 update", the S59 Project B pilot) taking L12 and L13 with it *in the same commit*.

Consequences, all now rules:
1. **Never conclude "the markup is uniform" from a subset.** S63's "markup was uniform, zero variants" was true of L01–L03 only — they share one stratum because S62 swept them together.
2. **Exact-string find-and-replace on an inline component is invalid book-wide.** It matches nothing outside its own stratum and reports success.
3. **Scope the replace to ONE challenge block.** Two challenges at the same tier produce byte-identical pills (L04 C02/C03 are both MEDIUM), so a file-wide `count == 1` assert fires falsely. This actually happened and the assert caught it.
4. **Strip tags before grepping a code construct.** Syntax highlighting splits constructs across `<span>`s.

**Two near-misses worth remembering — both would have produced wrong or redundant prose:**
- **`static`** looked like an L09 gap (0 prose hits there) but is properly taught in **L05** with a 🔑 callout. L03's hit is "static friction"; L06/L07's are the *different* file-scope sense.
- **`while(true)`** looked absent from the entire book but appears **11 times in L06** — the raw-HTML grep missed it because highlighting splits it as `while</span> (<span…>true`. This is the §11 false-positive rule running in the opposite direction: a false **negative**.

A third correction, caught before acting: I reported L06 §5.4 as a dangling cross-reference. **§5.4 exists** — my heading scan capped matches at ~110 chars and that heading is longer. Re-ran uncapped before writing anything.

---

## S65 NEXT — PRIMARY: the difficulty-progression audit proper

The sweep produced the data the audit needs. **Both axes, lesson means (doing / grasping):**

| L01 | L02 | L03 | L04 | L05 | L06 | L07 | L08 | L09 | L10 | L11 | L12 | L13 | L14 | L15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.36 / 1.36 | 1.67 / 1.50 | 1.69 / 1.62 | **2.40 / 2.20** | 2.00 / 1.80 | 2.25 / 1.88 | **1.83 / 1.50** | 1.80 / 2.00 | 2.17 / 2.17 | 2.20 / 1.80 | 2.00 / **2.33** | 2.33 / 2.33 | 2.50 / 2.00 | 2.33 / 2.33 | 2.71 / 2.57 |

Floor (L01–L03) and ceiling (L15) are clean on both axes. Three findings:

1. **L04 spikes to 2.40 / 2.20** — third-hardest doing in the book, sitting fourth. Confirmed on both axes now, not just doing. Its C04 is "the first true sense-and-act program of the course" and C05 is closed-loop proportional control — L08's headline concept arriving four lessons early. The two new explainers (§8A.8, §8A.9) reduce the *grasp* load but not the doing load.
2. **L07 sags to 1.83 / 1.50** — below L05, barely above L03, with **L08 at 1.80** right behind it. Two consecutive lessons easier than L04, four and five lessons later. L07 C03 is a strong doing-axis re-rate candidate: it has **zero fill-in blanks** (full template written out to copy) yet sits at Medium.
3. **Challenge COUNT collapses after L10:** 11, 6, 8, 5, 5, 8, 6, 5, 6, 5, then **3, 3, 3, 3**, then 7. L11–L14 carry 12 between them — fewer than L01 alone. **L11 pairs the book's highest grasp mean (2.33) with its lowest count** → under-*practiced*, not under-taught.

**DJ's ruling on the L06/L11 imbalance:** "either reduce some of L06 or increase some of L11" — data argues for **adding to L11–L14, not cutting L06**. L06's eight are two designed ladders (Square→Triangle→Pentagon spirals the exterior-angle rule; Smooth Stopping→Acceleration→Trapezoidal welds two halves), and cutting any breaks a progression. L11's own prose has unused candidates: §8A.4 walks the cliff arithmetic in five explicit steps and never becomes a challenge; §7C tests TRIM under blindness with no card. **New challenges are Part-B-scale work** — templates, payloads, Maker registry entries — so this is its own arc, not a sweep item.

**Also queued for the audit:** DJ wants his own pass over the tier assignments, and intends to use **Tough** more (currently 2 uses book-wide: L03 C05, L13 C02).

---

## OPEN DEBTS FROM S64 (new)
- **L15 C04–C07 ship with no template and no solution reveal.** Four of the book's hardest cards give a stuck student only prose, and give the AI Tutor nothing to strip. C01–C03 are templated with solutions; C04–C07 are open specifications. Deliberate capstone shape, but logged.
- **Stray `</div>` after `</html>`** in L01, L12, L13, L14, L15, L16. Malformed but browser-tolerated; tag counts balance so no depth walk catches it. DJ was asked twice and it was never ruled on — carried forward, not urgent.
- **L07 C03 doing-axis** — Medium with zero fill-in blanks. Re-rate candidate.

## ⚠ OPEN TEACHING GAP (marked, not fixed — carried from S62)
**L03 C05 Variable Speed** requires **arrays** and the **modulo operator `%`**. Neither appears anywhere in L03 prose (verified by grep, S62). Rated Tough / Deep. Oldest open gap in the book.

---

## THE LANDING-PAGE / BOOK COLOR MISMATCH (raised S63, still not started)
DJ: "it's weird that the launch page is black and then it goes white."

**19,197 hex values across 185 unique colors**, all inline (Canvas strips `<style>` and `class=`), so there is no stylesheet to flip. The top five — `#569cd6` · `#b5cea8` · `#6a9955` · `#ce9178` · `#1e1e1e`, ~8,000 occurrences — are **VS Code Dark+ syntax highlighting**, already dark and deliberately matched to the student's editor.

So the real shape is **dark code blocks inside a white page, against a fully dark `index.html`** — a page-background mismatch, not a palette mismatch. Darkening the book means recoloring ~11,000 non-syntax values across 16 lessons: Part-B-scale.

**Cheaper direction: lighten `index.html`** (one file, 12 colors). Middle option: a dark transition band at the top of each lesson. **No ruling yet.**

---

## STANDING QUEUE (carried)
- **L03 open:** array explainer + modulo `%` explainer (both C05 blockers) · 1000 ms = 1 second explainer · Coach's Tip upload/power-on sequence · AI-autocomplete warning · L01 VS Code multi-root workspace step.
- **"Pick your robot" chooser page** — unblocked, icon family live since S63.
- **Expand the 📓 ENGINEER'S LOG icon + section** — DJ likes the device.
- **Challenge-card Part-B redesign:** L06's Goal→Logic→Template pattern to all ~84 challenges.
- **Maker batch:** starters-only bulk download · `?lesson=N` gate · `C##` folder labels · verify `?kind=` downloads are starters not solutions.
- **TDP template v3:** A5 Lab Log (date · in/out · what).
- **Course docs:** day-by-day period grid + full syllabus.
- **AI Tutor (LAST):** add DISCOVERIES to the picker (needs `data-kind="discovery"`). *The tutor reads `data-difficulty` — **`data-grasp` is now on all 84 cards**, so confirm the tutor tolerates the second attribute before relying on it.*
- **Housekeeping:** `QA_*` contact sheets still committed in `images/glowbots/`; `git rm` whenever. Border inset 10–18px vs the 64px §21.1 spec — DJ: "leave them for now."

## BENCH (need the robot)
Q017 L09 green-tape six numbers · calibration-spin stopwatch · gyro-bias · L02 §5 green-LED bench check · Constrain RUN_MS.

## PARKED (don't reopen unprompted)
Challenge solution-disclosure · monetization / ebook · "Know Your Zumo" reference page.

---
*Written at S64 close, Jul 23 2026. The pill sweep is done and the book is instrumented on two axes for the first time. Next: the progression audit the instrumentation was built for.*

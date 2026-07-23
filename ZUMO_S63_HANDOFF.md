# ZUMO — S63 Handoff (written at S62 close, Jul 22 · paste at top of Session 63)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. LIVE.md wins over memory. **Grep the actual file/commit, never trust a pasted version number — or a summary's session number.**
   *Note: a handoff can never name its own commit hash — the commit that writes the handoff comes after it. If the live HEAD is one commit past what this file says, that is expected, not drift. Diff it to be sure.*

## LIVE STATE — verified by fresh clone, Jul 22, commit `c6da344`
L01 **v03.6.0** · L02 **v02.10.0** · L03 **v03.10.0** · L04 v04.4.0 · L05 v04.4.0 · L06 v04.8.0 · L07 v04.4.0 · L08 v04.3.0 · L09 v05.2.0 · L10 v02.3.0 · L11 v02.4.0 · L12 v01.4.0 · L13 v02.4.0 · L14 v02.6.0 · L15 v02.4.0 · L16 v02.3.0
Bible **v8.41** · Maker **v2.43** · Gate v1.6 · Harness v3.0

## DONE IN S62 — the split difficulty pill (L01–L03)

**The change.** The difficulty pill is now ONE badge cut by a 45° slash into two rated axes:

| Half | Question | Scale |
|---|---|---|
| **Doing** (left, warm) | How much work do the hands do? | Easy · Medium · Tough · Hard · Advanced |
| **Grasping** (right, blue) | How much must the head hold? | Light · Moderate · Deep |

Doing: Easy `#4A6B22` · Medium `#9A6B10` · Tough `#B85425` · Hard `#8A2F18` · Advanced `#6B2545`
Grasping: Light `#4A7FB5` · Moderate `#185FA5` · Deep `#0C3F6C`
White text throughout. Inline styles only. Slash = skewed 8px white span on negative margins.

**Why.** A single pill lies whenever the axes diverge. L03 C08 writes comments only (trivial to do) but reasons about encoder differentials three lessons before encoders exist. ADVANCED warned students off a ten-minute card; EASY hid the hard part. Easy / Deep is the truth.

**Canonized as Bible §6.12b (v8.41).** §6.12 pill spec rewritten to point at it. §20.2 gains `data-grasp="light|moderate|deep"`; `data-difficulty` retained for the doing axis so existing tooling does not break.

**Five doing-axis re-rates applied:** L01 C11 MEDIUM→Easy · L02 C06 HARD→Medium · L03 C03 EASY→Medium · L03 C05 MEDIUM→Tough · L03 C08 ADVANCED→Easy.

**DJ has not yet reviewed the rendered pills** — he stopped the sweep at L03 specifically to look at L01–L02 first. Do not sweep L04–L16 until he signs off on the look.

## ⚠ OPEN TEACHING GAP (marked, not fixed)
**L03 C05 Variable Speed** requires **arrays** and the **modulo operator `%`**. Neither appears anywhere in L03 prose (verified by grep, S62). Rated Tough / Deep. The modulo explainer was already queued; **the array gap is new information.**

## THE FULL DOING-AXIS AUDIT (all 78 cards read, S62)
Six mis-rates found. Five applied above. **Two remain unapplied** because they live outside the L01–L03 batch:
- **L05 C01 Detection Counter EASY→Medium** — identical boolean edge-detection pattern to L04 C02, which is rated MEDIUM. Two ratings for one concept.
- **L14 C02 Strict Mode EASY→Medium** — three lines of code, but the challenge is a trick question about `while(true)` and why there is nothing to wait for. Short, not easy.

Apply both during the L04–L16 sweep.

**Also found — no convention for observation challenges.** L01 C04/C06/C09 are all "predict, then verify, minimal code" and rate consistently Easy on doing. But L03 C08 was ADVANCED for the same *kind* of work — it was rated by TOPIC, not by demand. §6.12b now rules: observation challenges rate by what they demand, not what they are about.

## S63 NEXT — PRIMARY
1. **DJ reviews L01–L02 rendered pills.** If the design holds, sweep L04–L16 (53 pills, same method) and apply the two pending re-rates in that pass.
2. Then resume the **difficulty-progression audit** proper — now on two axes. The single-axis ramp already showed a clean floor (L01 1.45 → L02 2.00 → L03 2.12) and a clean ceiling (L13 3.00 → L15 3.29) but a **flat, spiky middle**: L04 spikes to 2.80 — third-hardest in the book, sitting fourth — while L05, L07, L08 all sit at 2.00, level with L02. L11 and L14 repeat the pattern later. L04's spike is real, not a rating artifact: C04 is called "the first true sense-and-act program of the course" and C05 is closed-loop proportional control, which is L08's headline concept arriving four lessons early with no name attached.

## METHOD NOTES (the split-pill sweep)
- L01–L03 pills were **uniform** — one canonical single-span shape, verified 25/25 before editing. **Do not assume L04–L16 are.** Re-extract and count first; the S61 callout sweep hit ~8 drifted schemes.
- Bounded-scope script, `count == N` asserts that abort **before** write. Edit backwards through the match list so offsets stay valid.
- Verify with: visible-word diff vs. backup (only pill labels should change), div AND span balance, `data-grasp` count == challenge count, zero old-pill regex hits.
- Both version homes per §5b — hidden comment line 1 (full three-digit) and visible banner (major.minor). L01 and L03 have the banner **twice**; L02 once.

## STANDING QUEUE (carried)
- **L03 open:** array explainer + modulo `%` explainer (both now C05 blockers) · 1000 ms = 1 second explainer · Coach's Tip upload/power-on sequence · AI-autocomplete warning · L01 VS Code multi-root workspace step.
- **Expand the 📓 ENGINEER'S LOG icon + section** — DJ likes the device.
- **Challenge-card Part-B redesign:** L06's Goal→Logic→Template pattern to all ~80–100 challenges.
- **Maker batch:** starters-only bulk download · `?lesson=N` gate · `C##` folder labels · verify `?kind=` downloads are starters not solutions.
- **TDP template v3:** A5 Lab Log (date · in/out · what).
- **Course docs:** day-by-day period grid + full syllabus.
- **AI Tutor (LAST):** add DISCOVERIES to the picker (needs `data-kind="discovery"`). *Note: the tutor reads `data-difficulty` — confirm it tolerates the new `data-grasp` attribute before the full sweep.*
- **Robot-icon FAMILY:** still BLOCKED on ChatGPT credits + image quality (Balboa/Zircon/Romi). Five regeneration prompts already provided. Frame spec 1254², 64px inset, 95px radius, 14px stroke, `#010808`. Bible §21.
- **"Pick your robot" chooser page** — needs the icon family.

## BENCH (need the robot)
Q017 L09 green-tape six numbers · calibration-spin stopwatch · gyro-bias · L02 §5 green-LED bench check · Constrain RUN_MS.

## PARKED (don't reopen unprompted)
Challenge solution-disclosure · monetization / ebook · "Know Your Zumo" reference page.

---
*Written at S62 close, Jul 22 2026. Split pill live on L01–L03, pending DJ's visual review. Next: sweep L04–L16, then the two-axis progression audit.*

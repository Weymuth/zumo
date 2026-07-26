# ZUMO — S74 Handoff (written at S73 close, Jul 26 · paste at top of Session 74)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **21** must PASS (gate file **v1.7**). Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.

## LIVE STATE at S73 close
L02 and four files were **pushed and md5-verified mid-session** (commit `18d66dd`). The L03 batch was
delivered after that push — **verify by fresh clone before trusting this block.**

L01 v03.10.0 · **L02 v03.0.0** · **L03 v03.14.0** · L04 v04.6.2 · L05 v04.8.2 · L06 v04.11.2 ·
L07 v04.7.2 · L08 v04.6.2 · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 · L13 v02.6.2 ·
L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.59** · Maker v2.45.1 · book_gates **v1.7 (21 gates)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Push order:** no Maker or image dependency — everything can go in one commit.

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io).

**DJ must eyeball L02:**
- The nav strip — `4. Hardware · 5. Code · 6. Build` now match the banners they point at.
- **§4** is new: the Meet Your Buttons table renders, the 📘 Serial Monitor Note sits below it.
- **§5 The Code** opens with the bridge sentence, then the seven-section walkthrough.
- **BC01** still sits between §5 and §6 and is NOT nested inside a banner div.
- **§6 Build It** opens with the Maker/DISCOVERIES callout and WHAT YOU NEED, then STEP 1.
- **§9 tail order:** Challenge 6 → *Make It Yours* prose block → CODE SWAP → §10.

**DJ must eyeball L03:**
- **BC01** sits between §5 The Code and the §6 Build It banner, un-nested.
- **BC02's** two groups read *I can…* then *I have…*, and Mark-done unlocks only at **12/12**.
- **BC03** and **BC04** sit in §10. The Calibration Data table still sits *between* them — left in place
  deliberately (fewer moves, and it is proof-of-work rather than a check).
- The column shows and hides below 700px and its check-offs persist across reload, as in L01/L02.

**Carried and still unverified from S72:** L02's column below 700px · Mark-done persistence · the seven ☐
skills unlock at 7/7 · L01's §4 header and *Meet Your Robot* table.

## DONE IN S73

### L02 — the renumber (v02.16.0 → v03.0.0)
1. **§3.2 lifted whole into a new §5 The Code** (29,833 chars, exactly the S72 measurement, one contiguous
   block — nothing reordered). New **§4 Hardware — Meet Your Buttons** authored in the empty slot. Old §5 →
   **§6** with *Getting Ready* folded into its opening, so "your fresh copy is open and healthy — let's
   build" still lands right before STEP 1. Old §6 *Make It Yours* retired as a section.
2. **Zero nav-pill edits.** The strip already read `4. Hardware · 5. Code · 6. Build` — the same L01 story
   from S72: the file already believed canon, only the visible banners had drifted.
3. **§3 closed to 3.1–3.6**, not the plan's 3.1–3.5: `3.2d` is its own `<h3>`, not nested inside `3.2c`.
   Ids renumbered two-pass (`section-3-3` collided with itself); `section-3-2-timeline` → `section-5-timeline`.
   Zero inbound links from other files, verified book-wide before touching any id.
4. **15 citations re-pointed, then verified by content — one was already wrong.** BC01 item 3 cited §3.2 for
   the function prototype and §3.2 never taught it (prototype: §3.1 ×9, build steps ×8, lifted block ×0).
   Shipped green in S72, would have shipped green again. Re-pointed to (§3.1, §6 Step 7).
5. **"Make It Yours" → prose block at the end of §9, de-duped** (DJ ruling). §6.12a already governs the
   format: open-creative takes prose, not panels. Landed as prose rather than a numbered card because a
   pick-one menu called "Challenge 7" gives "did you finish Challenge 7?" four answers — the §4.1 disease.
   Options B and D dropped as duplicates of Challenges 5 and 3. Sits ahead of the CODE SWAP, which stays last.

### L03 — the third Brain Check conversion (v03.13.2 → v03.14.0)
6. **Almost entirely redistribution.** `STOP & PROCESS` held **all ten** of L03's quiz reveals and was the
   pre-collapse ancestor of the family — its subtitle was literally *"Answer From Your Head, Then Check"*.
   Split on the §25.2 recall/apply line: **BC01 Mental** gets items 1, 2, 3, 5, 6 (five, inside the gated
   3–5 window) at the §5/§6 seam; **BC03 Knowledge Check** gets 4, 7, 8, 9, 10. Every item arrived already
   §-cited. Nothing authored from scratch.
7. **The split changed mid-session on canon, not preference.** Item 10 ("would a warehouse robot tune TRIM by
   hand?") was assigned to Reflection on the L02 analogy. Its reveal is factual — closed-loop control,
   encoders, a Lesson 6 forward-reference — and **§25.2 says Reflection never reveals**, gate-enforced.
   Placing it there would have meant deleting an answer to pass. It also turned out to **duplicate an
   existing Reflection prompt** ("how does TRIM relate to self-driving cars?"), which retired into it; the
   surviving version is strictly richer. Reflection came out at 3, inside its cap, untrimmed.
8. **BC05 was ruled, priced, and withdrawn.** DJ ruled L03's second checkbox list a fifth Brain Check *"if
   that doesn't mess things up."* It does: the column is **one 5,596-char block copied byte-identical into
   every converted lesson** (L01 == L02, verified) and its script is hardcoded to four — state array length
   4 and discarded otherwise, click handler rejects the fifth index, unlock wired to BC02 by index. Both
   lists now live inside **BC02** under bold *I can…* (8 capability) / *I have…* (4 process) labels, twelve
   `data-bc-skill` items. **The unlock generalised for free**: `allSkills()` loops over elements, so 7-of-7
   became 12-of-12 with zero JavaScript edits.
9. **Bible v8.58.1 → v8.59 — new §25.10a.** The family is four and the column is why; an extra exit block
   folds into the BC it most resembles as a labelled group; check whether a mechanism already scales before
   ruling that it doesn't; the column seats before `</body>`; and the subsection-slicing trap below.

### Verification (both lessons)
21/21 gates PASS, pill_sweep clean. **All twelve L03 citations verified by content**, each §3.x sliced by
the next subsection id. Four control runs, every one with a landed-injection assert: a dropped `</div>` in
L02's new §5 fails 3 gates · a stripped L02 BC01 citation fails §25.2 · a stripped `data-bc-skill` fails
with the exact 12-vs-11 count · reintroducing `STOP & PROCESS` fails on the retired name. All four restore
clean.

## FOUR THINGS S73 LEARNED THE HARD WAY
1. **A §-citation gate can only check that a § is NAMED.** Verifying it points at the RIGHT section means
   slicing the cited section and asserting the answer's own vocabulary is inside it. This is now §25.10a and
   it is the only check that catches the defect. It found one in L02 that had shipped green.
2. **Slice a subsection by the next SUBSECTION id, never by the next section anchor.** A Brain Check block
   physically sits between two sections, so an anchor-bounded slice swallows the quiz asking about the
   previous one and reports the answer present when it is absent. My first prototype scan did exactly this
   and nearly buried finding #1.
3. **Recompute landmarks after every cut.** Run one compared a pre-cut PART 2 offset against a post-cut §4
   offset; the precondition assert fired instead of mis-slicing 29 KB. Separately `GR_BODY` already carried
   its closing seam line and re-appending it duplicated the sentence — caught by grep, by no gate.
4. **Check whether a mechanism already scales before ruling that it doesn't.** The 12-of-12 unlock needed
   zero code. Had that not been checked, BC02 would have grown a hand-written count.

## INFERRED IN S73 (flagged, one line each)
- **§4 title "Hardware — Meet Your Buttons"** — follows L04's "Hardware — Meet Your Sensors" pattern; B and
  C are the only genuinely new parts.
- **§4 body's "no new parts" claim** — grepped L02's build steps: it declares `buttonA/B/C` and `display` and
  calls `ledYellow()`; buzzer and motors appear only in warm-ups, bonuses and the Quick Reference.
- **Make It Yours table header recolored to `#1a5276`** — the file's dominant, section-neutral `th` color
  (11 uses); its old `#2a5a42` was darkened §6 green and would read as a stray in purple §9.
- **`(&sect;5, &sect;8A)` on L02's return-address item kept** — §8A holds no return-address prose, but the
  lifted block already ends by pointing there for functions generally.
- **L03's Calibration Data table left between BC03 and BC04** — fewer moves, and it is proof-of-work rather
  than a check, so the non-contiguity is honest.
- **L03's BC04 keeps the confidence question but drops the emoji circle-one scale**, rephrased to ask what
  would move the student up one step — a rating is not something a notebook entry can carry.
- **`ZUMO_L02_RESTRUCTURE_PLAN.md` stamped EXECUTED and kept in the repo root** (DJ delegated) — it is the
  measurement record for the book's only major re-baseline, and the root already holds process docs.

## S74 QUEUE
1. **L04 Brain Check conversion** (§25 rollout — L01/L02/L03 done, no jumping). Apply §25.10a. Expect L04 to
   have no `STOP & PROCESS` ancestor to redistribute, so this is the first conversion that is mostly
   authoring rather than splitting.
2. **UNRESOLVED — the §25.8 cap conflict.** §25.2 says the Knowledge Check count "scales with the lesson";
   §25.8 caps it at **5**. **L02 is live at 7** and no gate counts BC03 at all. DJ's read is that a cap is
   probably wrong educationally. L03 came out at 5 so it did not need the ruling; L04+ will. On the table:
   floor of 4, no ceiling, plus a BC03 count added to the gate — keeping Mental at 3–5, which is already
   gated and functional as a pre-build readiness check.
3. **L03's Technical Skills is 8 items where §2 has 11 objectives** — §25.2 says they should be equal. DJ
   ruled leave both lists alone and reconcile at the final read-through.
4. Warm-ups L02–L16 + spiral aiming rule — **warm-ups are still L02-ONLY** (9 hits in L02, zero elsewhere),
   so L02 is the prototype the rest follow.
5. Bonus challenges §10→§9 (12 cards; pill/livery ruling still open) · L13/L15 have no exit blocks at all ·
   §2 objectives from Technical Skills checklists · within-lesson build-on mark.
6. going_deeper footer contrast + duplicated hero title.
7. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware & Code" —
   found S72, one-line fix, still not done.
8. Now that L02 conforms, re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all
   sixteen — the dividend is claimed in Bible §4.4 but has not been checked against the Maker.

## OPEN — NEEDS A DJ RULING
- The §25.8 cap (queue item 2) — the one live canon conflict.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge cards (eight
  sessions now) · spiral marking format review · DJ tier pass + rolling depth read (L14 first) · copyright
  line (RoboLore, work-for-hire) · bonus-challenge pill + livery when they move to §9.

## STANDING QUEUE (carried; SUSPECTED until re-checked per §24.6c)
L02 `2.t7` label collision (VERIFIED latent) · BENCH: compile-verify L07 finished + trapezoid · L08 Racing
Line · L11 C4 double-TRIM · Q017 L09 six numbers · calibration-spin · gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · L15 C04–C07 no-template shape · L01 VS Code multi-root step · landing-page/book color
mismatch · Maker batch (bulk DL · `?lesson=N` gate · C## labels · verify `?kind=` starters) · TDP v3
(A5 Lab Log + printed 16 log prompts) · course docs (grid + syllabus) · "pick your robot" chooser ·
AI Tutor DISCOVERIES picker · QA_* sheets in images/glowbots · border inset 10–18 vs 64 · Canvas reading
quizzes (book first, then Canvas).

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page — **note:** it has a home now, as L01's §4
Hardware, with Install moving down.

---
*Written at S73 close, July 26 2026. Two lessons changed shape and neither needed much invention: L02's nav
strip had been right all along, and L03's ten-item block was the family's own ancestor waiting to be split.
What the session actually produced is one rule — §25.10a — earned twice: once by a citation that had been
pointing at the wrong section since the day it shipped, and once by the measurement that nearly hid it.*

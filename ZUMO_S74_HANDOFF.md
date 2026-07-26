# ZUMO — S74 Handoff (written at S73 close, Jul 25 · paste at top of Session 74)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **21** must PASS (gate file **v1.7**). Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.

## LIVE STATE at S73 close — **DELIVERED, NOT YET PUSHED**
Four files were handed to DJ at S73 close. **Verify the push by fresh clone before trusting this block.**

L01 v03.10.0 · **L02 v03.0.0** · L03 v03.13.2 · L04 v04.6.2 · L05 v04.8.2 · L06 v04.11.2 ·
L07 v04.7.2 · L08 v04.6.2 · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 · L13 v02.6.2 ·
L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.58.1** · Maker v2.45.1 · book_gates **v1.7 (21 gates)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Push order:** no Maker or image dependency this session — the four files can go in one commit.

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io). **DJ must eyeball L02:**
- The nav strip: `4. Hardware · 5. Code · 6. Build` now match the section banners they point at.
- **§4** is new — the Meet Your Buttons table renders, the 📘 Serial Monitor Note sits below it.
- **§5 The Code** opens with the one-line bridge sentence, then the seven-section walkthrough.
- **BC01** still sits between §5 and §6 (last seam before hands-on work) and is NOT nested in a banner div.
- **§6 Build It** opens with the Maker/DISCOVERIES callout and WHAT YOU NEED, then STEP 1.
- **§9 tail order:** Challenge 6 → *Make It Yours* prose block → CODE SWAP → §10.
- Carried from S72 and still unverified: L02 Brain Check column shows/hides below 700px · Mark-done persists
  across reload · the seven ☐ skills toggle and unlock at 7/7 · L01's §4 header and *Meet Your Robot* table.

## DONE IN S73
1. **L02 v02.16.0 → v03.0.0 — the renumber, cut.** §3.2 (29,833 chars) lifted whole → new **§5 The Code**.
   New **§4 Hardware — Meet Your Buttons** authored. Old §5 → **§6**, *Getting Ready* folded into its
   opening so "your fresh copy is open and healthy — let's build" still lands right before STEP 1. Old §6
   *Make It Yours* retired as a section. **Zero nav-pill edits** — the strip was already canonical, the same
   L01 story as S72.
2. **§3 closed to 3.1–3.6** (DJ ruled close the hole). Ids renumbered two-pass (`section-3-3` collided with
   itself). `section-3-2-timeline` → `section-5-timeline`. Zero inbound links from other files, verified
   book-wide before touching any id.
3. **15 citations re-pointed by hand, then verified by content.** One was already wrong: BC01 item 3 cited
   §3.2 for the function prototype and §3.2 never taught it. Re-pointed to (§3.1, §6 Step 7).
4. **"Make It Yours" → prose block at the end of §9, de-duped** (DJ ruling). Options B and D dropped as
   duplicates of Challenges 5 and 3. Placed ahead of the CODE SWAP, which stays last in §9.
5. **Bible v8.58 → v8.58.1.** §4.4 attribution corrected; citation-verification rule recorded.

## THREE THINGS S73 LEARNED THE HARD WAY
1. **A §-citation gate can only check that a § is NAMED.** Verifying it points at the RIGHT section means
   slicing the cited section and asserting the answer's keywords are inside it. Do this by hand on every
   Brain Check conversion from here on — it is the only check that catches the defect.
2. **A section slice bounded by the NEXT section anchor swallows the Brain Check block that sits between
   them.** My first prototype scan reported §5 containing "prototype" ×2; those hits were BC01's own question
   text. Bound §5 by `brain-check-01`, not by `section-6`. This one nearly buried finding #1.
3. **Recompute landmarks after every cut.** The first run compared a pre-cut PART 2 offset against a post-cut
   §4 offset; the precondition assert fired instead of mis-slicing 29 KB. Separately, `GR_BODY` already
   carried its closing seam line and re-appending it duplicated the sentence — caught by grep, by no gate.

## INFERRED IN S73 (flagged, one line each)
- **§4 title "Hardware — Meet Your Buttons"** — follows L04's "Hardware — Meet Your Sensors" pattern, and
  Buttons B and C are the only things genuinely new to the student this lesson.
- **§4 body claims no new parts** — grepped L02's build steps: the program declares `buttonA/B/C` and
  `display` and calls `ledYellow()`; the buzzer and motors appear only in warm-ups, bonuses and the Quick
  Reference, never in the main build.
- **Make It Yours as prose, not a numbered card** — a pick-one menu named "Challenge 7" would give
  "did you finish Challenge 7?" four answers, the exact §4.1 disease.
- **Its table header recolored to `#1a5276`** — the file's dominant, section-neutral `th` color (11 uses);
  its old `#2a5a42` was the darkened §6 green and would read as a stray in purple §9.
- **`(&sect;5, &sect;8A)` on the return-address question kept as-is** — §8A holds no return-address prose,
  but the lifted block already ends by pointing there for functions generally, so the pointer is native.
- **Bible bumped rather than left** — §4.4 asserted L02 was fixed S72 when it had only been specified; a
  canon document asserting a false fact is the §12.6 class.
- **`ZUMO_L02_RESTRUCTURE_PLAN.md` stamped EXECUTED and left in the repo root** — kept as the measurement
  record, with its two wrong predictions corrected in the banner so nobody re-cuts from it. The standing
  question of whether it belongs in the root at all is still open.

## S74 QUEUE
1. **L03 Brain Check conversion** (§25 rollout, DJ's order L01→L02→L03, no jumping). This was S73's stated
   next task and did not start. Apply the S73 lesson: verify every §-citation by content, not by presence.
2. Warm-ups L02–L16 + spiral aiming rule — **warm-ups are still L02-ONLY** (9 hits in L02, zero elsewhere),
   so L02 is the prototype the rest follow.
3. Bonus challenges §10→§9 (12 cards; pill/livery ruling still open) · L13/L15 have no exit blocks at all ·
   §2 objectives from Technical Skills checklists · within-lesson build-on mark.
4. going_deeper footer contrast + duplicated hero title.
5. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware & Code" —
   found S72, one-line fix, still not done.
6. **New:** now that L02 conforms, re-read §15.2's "if Section 6 has N steps" against the Maker for all
   sixteen — the dividend is claimed in Bible §4.4 but has not been re-verified against `newproject.html`.

## OPEN — NEEDS A DJ RULING
- Does `ZUMO_L02_RESTRUCTURE_PLAN.md` stay in the repo root now that it is executed, or move/retire?
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
*Written at S73 close, July 25 2026. The renumber itself was the easy half — measured at S72, cut in one
pass, and the nav strip turned out to have been right all along. The session's real find was that the
citation the whole restructure was held for was already pointing at the wrong section before anyone
renumbered anything, and that no gate in the book can see that.*

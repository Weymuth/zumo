# ZUMO — S76 Handoff (written at S75 close, Jul 26 · paste at top of Session 76)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **21** must PASS (gate file **v1.7**). Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
6. §25.10b: grep §25.2's RETIRED-NAME list before scoping any conversion.
7. **NEW — §25.10c: if the sweep returns TWO ancestor blocks, diff them item by item before calling
   either one waste.** L05's duplicate had already done part of the recall/apply split. This is what S75 learned.

## LIVE STATE at S75 close
**Nothing from S75 is pushed.** Three files delivered at close, in DJ's hands:
`Lesson_05.html`, `ZUMO_SUPER_BIBLE.md`, `LIVE_ZUMO_TEXTBOOK.md`. **Verify by fresh clone before trusting
this block.** S74's work (L04 + Bible + LIVE.md) IS live — commit `5a69b113`, verified this session by
md5 against the S74 delivery, all three matching.

L01 v03.10.0 · L02 v03.0.0 · L03 v03.14.0 · L04 v04.7.0 · **L05 v04.9.0** · L06 v04.11.2 ·
L07 v04.7.2 · L08 v04.6.2 · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 · L13 v02.6.2 ·
L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.61** · Maker v2.45.1 · book_gates **v1.7 (21 gates)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Push order:** no Maker or image dependency — all three files can go in one commit.
**md5 at delivery:** `Lesson_05.html` `57d2d83b…` · Bible `5e1b6d70…` · LIVE.md `a6517a79…`

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io).

**DJ must eyeball L05:**
- **BC01** sits between §5 Code Walkthrough and the §6 Build It banner, un-nested (div depth 1, same as L01–L04).
- **BC02's** two groups read *I can…* (7) then *I have…* (2); Mark-done unlocks only at **9/9**.
- **BC03** and **BC04** sit in §10, in that order, followed by What's Next and the Engineer's Log —
  both left exactly where they were.
- **Bonus now reads "Six Proximity Mysteries"**; Mystery 6 *No Yesterday* is last, and the §9 lead-in
  sentence names it.
- The column shows and hides below 700px and its check-offs persist across reload.

**Carried and still unverified from S72/S73/S74:** L02's, L03's and L04's column below 700px · Mark-done
persistence · the 7 ☐ / 12 ☐ / 13 ☐ unlocks · L01's §4 header and *Meet Your Robot* table · L02's §4
*Meet Your Buttons* table.

## DONE IN S75

### L05 — the fifth conversion (v04.8.2 → v04.9.0)
1. **The ancestor was present twice.** §25.10b returned `Conceptual Understanding` (6 questions, no
   answers) sitting directly above `Knowledge Check` (the same six facts, with reveals). Normalised diff:
   **four pairs word-identical, two differing.** Item 6 differs by wording only. **Item 4 differs by
   cognitive level** — *"What does a function prototype promise the compiler?"* vs *"Our helper functions
   live below loop(), in any order — why does the build still succeed?"* — which is the §25.2 recall/apply
   line already drawn by whoever wrote the two lists. Discarding the answerless list wholesale would have
   thrown away a Mental item.
2. **BC01 Mental — 5.** 38 kHz (§3.1, authored) · value range (§3.2) · `DETECTION_THRESHOLD = 1` (§3.3) ·
   function prototype (§5.5, the CU phrasing) · the permanent DN2/DN4 jumper move (§1, §7.3, authored).
   The pool alone reached the 3-item floor; DJ ruled two more authored on top, to five.
3. **BC03 Knowledge Check — 4.** `max()` (§4.2) · prototype/order (§5.5) · threshold vs reading
   (§3.3, §3.5) · for loop (§5.15). Questions and **all answers migrated character-exact**.
4. **BC02 folds both lists — 9 items**, seven *I can…* + two *I have…*, unlock at 9-of-9 with **zero
   JavaScript** (third time `allSkills()` counting elements has paid).
5. **BC04 Reflection authored — L05 had none.** Three prompts, no reveal. **Deliberately does NOT take
   the shared-pin tradeoff**, which Engineer's Log #05 already owns — the duplicate was resolved in favour
   of the incumbent rather than folded, unlike S73's L03 case.
6. **Two Problem-Solving items could not be gated** (§25.10 achievability: behind a 9-of-9 lock, an item
   not every student can earn makes the lock unreachable). Per DJ ruling, both moved rather than died —
   *"Complete at least one of the Bonus mysteries"* retired into §9's own lead-in sentence, which already
   names all five; *"Extend: add a fourth display mode showing detection history"* was a challenge wearing
   a checkbox and became **Mystery 6, "No Yesterday."**
7. **§4.2 gap closed.** L05's five bonus mysteries carried **no `data-challenge` markers** — the picker
   queries `[data-challenge]`, so all five were invisible to the AI Tutor. Tagged `5.m1`–`5.m5` on L11's
   convention (`data-kind="mystery"`), Mystery 6 as `5.m6`.
8. **Bible v8.60 → v8.61 — new §25.10c.** Diff duplicated ancestors item by item; relocate rather than
   delete an ungateable skill (two named disposals); the column is copied START through the **full
   43-character** END comment.

### Verification
21/21 gates PASS, pill_sweep clean, column byte-identical across all five converted lessons
(`8fa00744`, 5,596 chars). §25.2 self-scopes on `MENTAL KNOWLEDGE CHECK`, so **no gate edit was needed**.
Four control runs, each with a landed-injection assert, each restoring byte-identical: a stripped
`data-bc-skill` fails with the exact `9 checkbox items but 8 data-bc-skill tags` · a reintroduced
`Conceptual Understanding` fails on the retired name · a stripped BC01 citation fails *"Mental item names
no §"* · a dropped `</div>` fails tag balance (165/164) **and** the parse gate. Diff audit: 70 lines
removed, every one an intended block, a retitle, or a version line.

### Content-preservation audit (run at DJ's instruction)
All **23** exit-region items extracted to a manifest BEFORE any edit and re-checked against the finished
file. **ACCOUNTED 33 · LOST 0.** 7 Technical Skills character-exact · 6 Conceptual Understanding (4
absorbed by word-identical twins, 1 promoted to BC01, 1 absorbed by its reworded sibling) · 4
Problem-Solving (2 folded, 1 retired to prose, 1 reshaped) · 6 Knowledge Check questions **and all six
answers character-exact**. What's Next, Engineer's Log #05 and the five original mysteries untouched.

## THREE THINGS S75 LEARNED THE HARD WAY
1. **A duplicate is not automatically waste.** Four of six pairs were redundant and one was not — and the
   one that was not had already done half the §25.2 split. Diff by normalised text; a pair that DIFFERS is
   a finding. Now §25.10c.
2. **The for-loop citation was wrong before it was written.** §5.9 `showBarGraphMode()` does not contain
   the word; it is §5.15 *Coding Concepts: The For Loop, Second Look*, 13 mentions. **Fifth defect §25.10a
   has caught, fifth that no gate could see.**
3. **One byte short of the column END comment took the file down.** Slicing 42 characters instead of 43
   left `<!-- … =====  --` unterminated, which swallowed `</body>` and `</html>`. **Tag balance PASSED**;
   the §24.6 parse gate caught it — first instance where the unclosed thing was a comment, not an element.

## INFERRED IN S75 (flagged, one line each)
- **BC01 in §-order** — DJ's "yes. good." answered an either/or; read as the first option, stated plainly
  in-session so a one-word correction was available. The two authored items therefore seat at 1 and 5.
- **"(Reflection)" stripped from the for-loop item** — it carries a reveal, and §25.2 says Reflection never
  reveals; same ruling S73 applied to L03 item 10.
- **BC01 item 4's reveal is authored, not migrated** — `Conceptual Understanding` ships answerless, so the
  recall-level answer had no source text to migrate.
- **BC04 avoids the shared-pin tradeoff** — Engineer's Log #05 already asks for it verbatim ("State the
  constraint. Defend the choice you made"), and TDP §2 feeds from the Log.
- **Mystery 6's title and predict/test/explain shape are my reshape** — the source item was an open
  extension; the Bonus section's own intro sets the contract it was rewritten to.
- **§4.2 verified by heading-slice, not id-slice** — L05's §4 subsections carry no ids (only 4.4 does),
  unlike its §3 and §5.
- **Mystery markers `5.m1`–`5.m6`** — copied L11's live convention, the only other lesson with mysteries.

## S76 QUEUE
1. **L06 Brain Check conversion** (§25 rollout — L01–L05 done, no jumping). **Open §25.10b AND §25.10c
   first:** grep the retired-name list, and if two ancestor blocks come back, diff them before scoping.
2. **UNRESOLVED — the §25.8 cap conflict, now dodged three times.** §25.2 says the Knowledge Check count
   "scales with the lesson"; §25.8 caps it at **5**. **L02 is live at 7** and no gate counts BC03 at all.
   L03, L04 and L05 came out at 5, 5 and 4. On the table: floor of 4, no ceiling, plus a BC03 count added
   to the gate. **L06 may force it.**
3. **Technical Skills vs §2 objectives — now FOUR lessons carry the debt.** L03 8 vs 11 · L04 13 vs 11 ·
   L05 7 vs 10. §25.2 says they should be equal; DJ ruled at S74 open to leave both lists alone and
   reconcile at the final read-through.
4. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware & Code"
   — found S72, one-line fix, still not done. (L05's is correct; checked this session.)
5. Warm-ups L02–L16 + spiral aiming rule — **warm-ups are still L02-ONLY**, so L02 is the prototype.
6. Bonus challenges §10→§9 (12 cards; pill/livery ruling still open) — **L05 is NOT affected, its Bonus
   already sits in §9; verified this session.** L13/L15 have no exit blocks at all · §2 objectives from
   Technical Skills checklists · within-lesson build-on mark.
7. going_deeper footer contrast + duplicated hero title.
8. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen — the dividend is
   claimed in Bible §4.4 and still has not been checked against the Maker.
9. **NEW — sweep the other lessons for untagged mysteries/bonus items.** L05's five were invisible to the
   Tutor for their whole life and no gate saw it, because `§4.2 data-challenge markers globally unique`
   checks uniqueness, not coverage. A coverage gate is the real fix.

## OPEN — NEEDS A DJ RULING
- The §25.8 cap (queue item 2) — still the one live canon conflict, three lessons unforced.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge cards
  (ten sessions now) · spiral marking format review · DJ tier pass + rolling depth read (L14 first) ·
  copyright line (RoboLore, work-for-hire) · bonus-challenge pill + livery when they move to §9.

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
*Written at S75 close, July 26 2026. The queue said L05 would be a redistribution job and it was — but the
material was sitting in the file twice, and the interesting half of the session was working out which copy
of each fact to keep. Four of the six pairs were genuinely redundant. The fifth was the same fact asked at
two different levels, which is the split §25.2 exists to make, already made and waiting. DJ's instruction
at the end — "make sure we are not losing any content, just moving it" — turned into a 23-item manifest
audited against the finished file, and it is the reason the answerless list got read carefully instead of
deleted.*

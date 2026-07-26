# ZUMO — S80 Handoff (written at S79 close, Jul 26 · paste at top of Session 80)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **23** must PASS (gate file **v1.9**). Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
6. §25.10b/c/d/e/f as before.
7. **NEW — check the push actually landed.** S79 opened on a tree that did not contain S78's work:
   the tip commit was named "Push 78" and carried **S77's** deliverables. Push labels run one ahead of
   the session whose work they carry. Verify by grepping a version out of the clone, never by reading
   the commit message. The GitHub API (`/commits/{sha}`) lists the changed files and settles it in one call.

## LIVE STATE at S79 close — VERIFIED, gates 23/23 PASS
L01 **v03.10.1** · L02 v03.0.0 · L03 v03.14.0 · L04 v04.7.0 · L05 **v04.9.2** · L06 **v04.12.1** ·
L07 **v04.8.1** · L08 **v04.7.1** · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 ·
L13 v02.6.2 · L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.65** · Maker v2.45.1 · book_gates **v1.9 (23 gates)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Brain Check family: eight of sixteen — L01–L08, and now uniform.** All sixteen blocks use
`data-reveal="quiz"`. Column still byte-identical in all eight: **5,639 chars / md5 `070806a6`, ending `-->`.**

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io).

**DJ must eyeball L01 C11.** The card now shows two reveals where it showed one — a `hint` (voltage table,
USB catch) and below it a `solution` (the worked code). Check the new box renders in L01's card livery.

## DONE IN S79

### 1. L01 v03.10.0 → v03.10.1 — the leak
Challenge 11 *Add a Battery Check* asks the student to fill `if (voltage < ______)` and write the warning.
Its `hint` held the finished code — `if (voltage < 4500)`, `display.print("LOW BATT!")`, the buzzer call.
§20.1 strips only `solution`, so the answer was reaching the tutor. **Split, not retyped:** coaching content
stays `hint`; lead-in + worked `<pre>` moved to a sibling `solution` reveal in L01's canonical markup
(matched against cards 1.2 and 1.9).

### 2. BC03 retyped solution → quiz in L05–L08 (DJ ruling)
*"What we want to hide the answers to is the challenges."* BC01 was `quiz` in all eight converted lessons
while BC03 had drifted to `solution` in L05–L08. Verified by reversing each edit inside the BC03 bound and
byte-comparing to source — identical in all four, so the change is attribute-only.

### 3. book_gates v1.8 → v1.9 — 23rd gate
`§20.1 no finished answer hidden behind a hint reveal`. Control-run three ways: unfixed source **FAILED**
(caught 1.11 and nothing else), fixed tree **PASS**, injected drift (L03 3.1 solution→hint) **FAILED**.

### 4. Bible v8.64 → v8.65
§20.1 rule (4): the strip list is a whitelist, so a finished code block belongs in a `solution` reveal even
when the surrounding box is a hint — and the fix is to SPLIT the box, not retype it.

## THREE THINGS S79 LEARNED THE HARD WAY
1. **The push label lied and the paperwork agreed with itself.** The S79 handoff said "VERIFIED, gates 22/22
   PASS" and it was true — in a sandbox that no longer existed. Sandbox-verified is not live.
2. **My leak detector returned 73 candidates and was almost all false positives** — it read every §6.12a
   Template panel as finished code in open prose. The one real leak was found by reading a card. Third
   consecutive session whose lesson is that the checking step fails before the work does.
3. **A verification assert can fail on arithmetic I never did.** The BC03 retype tripped its own
   length-unchanged assert because `quiz` is four bytes shorter than `solution`. The edit was right.

## INFERRED IN S79 (flagged, one line each)
- **All five bumps are minor (third digit)** — L05–L08 changed one attribute value each, and L01 relocated
  existing content into a new wrapper without authoring any new prose.
- **`leak_survey.py` was NOT shipped to the repo** — at a 72-of-73 false-positive rate it is a hazard in the
  tool folder, and the narrow gate in `book_gates.py` supersedes it.
- **L02 `2.t4` left alone** — `check` is a KEPT type by §20.1 design and a TRY IT box is not a graded
  challenge card, so it needs a ruling rather than a fix.

## S80 QUEUE
1. **L09 Brain Check conversion** — deferred from S79, unchanged and now unblocked (BC03 = `quiz`, ruled).
   **L09 already carries TWO live ancestors:** *Technical Skills: Can you…?* and *Knowledge Check* (the
   latter is 3 items, already `quiz`-typed — migrate verbatim and it lands correct by construction). Expect
   a redistribution job, not an authoring job. Tag L09's 5 mysteries in the same edit. L09 keeps its
   *Calibration Data Record* per the S78 ruling.
2. **OPEN RULING — L02 `2.t4`'s `check` reveal** (see above). Ruling it also decides whether a `check`-type
   gate is worth writing.
3. **L06's BC01 is at div depth 1** where the other seven sit at 0 — inside its §5 panel rather than between
   sections. Cosmetic; one-line fix whenever L06 is next open. **Re-verified live at S79.**
4. **OTHER GATES WORTH WRITING** (carried):
   - **placeholder gate** — `{[A-Z_]+}` inside an attribute value, book-wide (S76's `{CODE}`).
   - **§4.2 coverage gate** — every `<h4>` in a bonus/mystery block carries `data-challenge`.
   - **within-lesson promise gate** — "Section N has/covers X" resolves inside the same file (§25.10d).
   - **unretired-ancestor gate** — flag any `<h3>` in §10 of an *unconverted* lesson that looks like an exit
     construct. Would catch L09, L11, L15, L16 in one pass.
   - **nested-card bounding** — `2.b1` and `3.b1` depth-bound to 16.5k and 20.5k because the walk finds a
     wrapper holding all six bonus cards. Any future per-card gate needs this solved first; it is why
     bonus-challenge leak coverage in L02/L03 is still **SUSPECTED**.
5. **10 mysteries still untagged:** L04 (5) · L09 (5).
6. **Unretired ancestors:** L09 *Technical Skills* + *Knowledge Check* (both real, both verified S79) ·
   L11 *Skills Checklist* · L15/L16 *Wrap-Up* is a section banner, and §25.9 records L15 as having no exit
   block at all.
7. **Technical Skills vs §2 objectives — THREE lessons carry the debt.** L03 8 vs 11 · L04 13 vs 11 ·
   L05 7 vs 10. DJ ruled at S74 to reconcile at the final read-through.
8. **The weeding criterion still does not exist.** §25.8 enforces the floor of 4; nothing says what makes a
   BC03 item weakest. L02 (7), L07 (6), L08 (6) are the candidates. `ZUMO_PARKED_EXIT_ITEMS.md` gained
   nothing this session.
9. **Bonus placement is a 9/6 split.** After §10: L02, L03, L06, L07, L10, L13, L14, L15, L16. In the §9
   region: L04, L05, L08, L09, L11, L12. L01 has none.
10. **L13 and L14 bonus banners carry a doubled 🕵️** (`&#128373;&#65039;` twice). One-line fix each, found
    S76, still not done.
11. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware & Code"
    — found S72, one-line fix, still not done.
12. Warm-ups L02–L16 + spiral aiming rule — **still L02-ONLY**, so L02 is the prototype.
13. L13/L15 have no exit blocks at all · within-lesson build-on mark · going_deeper footer contrast +
    duplicated hero title.
14. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen.

## OPEN — NEEDS A DJ RULING
- **L02 `2.t4`** (queue item 2).
- **The weeding criterion** (queue item 8) — blocks the weeding pass.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge cards
  (fourteen sessions now) · spiral marking format review · DJ tier pass + rolling depth read (L14 first) ·
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
Solution-disclosure · monetization/ebook · "Know Your Zumo" page — **note:** it has a home now, as L01's
§4 Hardware, with Install moving down.

## PUSH NOTE
Replace: `lessons/Lesson_01.html` · `lessons/Lesson_05.html` · `lessons/Lesson_06.html` ·
`lessons/Lesson_07.html` · `lessons/Lesson_08.html` · `ZUMO_SUPER_BIBLE.md` · `book_gates.py` ·
`LIVE_ZUMO_TEXTBOOK.md`
Add: `ZUMO_S80_HANDOFF.md`
`git rm ZUMO_S78_HANDOFF.md`

---
*Written at S79 close, July 26 2026. The session opened by finding that S78's work was not in the repo at
all — the tip commit was named "Push 78" and carried S77's files — and the handoff's "VERIFIED, gates 22/22
PASS" was true of a sandbox that no longer existed. Then a ruling that looked like a coin-flip between two
reveal types turned out to be already settled inside the same eight files: BC01 had held `quiz` through
every conversion while BC03 drifted, so the split was never 4/4, it was 12/4 for one construct. DJ's
sentence — what we hide is the challenges — pointed at the inverse defect, and there it was: a finished
answer sitting in a hint in Lesson 1, shipped to the tutor for eight sessions, in the oldest and
most-read lesson in the book. The gate that now catches it took twenty lines. The detector I wrote first
took ninety and returned seventy-three candidates, seventy-two of them template panels.*

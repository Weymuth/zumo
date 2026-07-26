# ZUMO — S75 Handoff (written at S74 close, Jul 26 · paste at top of Session 75)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **21** must PASS (gate file **v1.7**). Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
6. **NEW — §25.10b: before scoping any conversion, grep §25.2's RETIRED-NAME list against the lesson.**
   The live construct names are the wrong grep. This is what S74 learned.

## LIVE STATE at S74 close
**Nothing from S74 is pushed.** Three files were delivered at close and are in DJ's hands:
`Lesson_04.html`, `ZUMO_SUPER_BIBLE.md`, `LIVE_ZUMO_TEXTBOOK.md`. **Verify by fresh clone before
trusting this block.** S73's work (L02, L03 + four files) IS live — commit `4f96957`, verified this session.

L01 v03.10.0 · L02 v03.0.0 · L03 v03.14.0 · **L04 v04.7.0** · L05 v04.8.2 · L06 v04.11.2 ·
L07 v04.7.2 · L08 v04.6.2 · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 · L13 v02.6.2 ·
L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.60** · Maker v2.45.1 · book_gates **v1.7 (21 gates)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Push order:** no Maker or image dependency — all three files can go in one commit.
**md5 at delivery:** `Lesson_04.html` `37b415e1…` · Bible `75a8b744…` · LIVE.md `596f176e…`

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io).

**DJ must eyeball L04:**
- **BC01** sits between §5 The Code and the §6 Build It banner, un-nested (div depth 1, same as L01/L02/L03).
- **BC02's** two groups read *I can…* (6) then *I have…* (7); Mark-done unlocks only at **13/13**.
- **BC03** and **BC04** sit in §10, in that order, followed by the 🔮 WHAT'S NEXT callout and the
  Engineer's Log — both of which were left exactly where they were.
- The old emoji **Confidence check** is gone; its question survives as BC04 item 3.
- The column shows and hides below 700px and its check-offs persist across reload.

**Carried and still unverified from S72/S73:** L02's and L03's column below 700px · Mark-done persistence ·
the 7 ☐ / 12 ☐ unlocks · L01's §4 header and *Meet Your Robot* table · L02's §4 Meet Your Buttons table.

## DONE IN S74

### L04 — the fourth conversion (v04.6.2 → v04.7.0)
1. **The ancestor was real and the queue was wrong about it.** S74's queue said to expect no
   `STOP & PROCESS` to redistribute, so this would be "mostly authoring." L04 had a ten-item ancestor
   titled **`Conceptual Understanding` — 10 questions, answers underneath**, which is the second entry on
   §25.2's retired-name list. Sweeping the live names returned nothing and confirmed the wrong conclusion.
2. **Ten items split on the §25.2 recall/apply line.** **BC01 Mental**: 1, 2, 3, 4, 6 (five, inside the
   gated 3–5 window) at the §5/§6 seam. **BC03 Knowledge Check**: 5, 7, 8, 9, 10. Answers were *parsed out
   of the live file* and re-emitted — never retyped — and all ten survive character-exact, audited.
3. **BC02 folds both checkbox lists.** `Technical Skills` (9) + `Problem-Solving` (4) → one BC02 under bold
   *I can…* (6 capability) / *I have…* (7 process), thirteen `data-bc-skill` items, nothing deleted.
   **13-of-13 needed zero JavaScript** — `allSkills()` counts elements, second time §25.10a's "check
   whether the mechanism already scales" has paid.
4. **BC04 Reflection authored — L04 had none.** Three prompts, no reveal. Absorbs the retired emoji
   Confidence check, rephrased to ask what would move the student up one step (the L03 ruling from S73).
5. **Two of ten citations were wrong before they were written.** Item 2 (the 1400 problem) → §3.1 has
   neither "1400" nor "raw"; it is **§3.4**. Item 6 (the index trap) → §3.3 has no "index" at all; it is
   **§5**, which carries the item's own phrasing. Item 9 widened to (§3.2, §3.6, §7). **10/10 verified by
   content.** L04 has no subsection ids, so each §3.x was sliced by the next `<h3>`.
6. **Bible v8.59 → v8.60 — new §25.10b.** Scope a conversion by the retired-name list, not the live one;
   a handoff records what the last session saw while the retired-name grep records what is in the file;
   plus the grammar cost of the §25.10a fold (tense and clause-order rewording expected, everything else
   character-exact, apostrophe convention checked not assumed).

### Verification
21/21 gates PASS, pill_sweep clean. §25.2 binds L04 automatically — the gate self-scopes on
`MENTAL KNOWLEDGE CHECK`, so **no gate edit was needed**. Four control runs, each with a landed-injection
assert, each restoring clean: a stripped `data-bc-skill` fails with the exact `13 checkbox items but 12
data-bc-skill tags` · a stripped BC01 citation fails §25.2 · reintroducing `Conceptual Understanding` fails
on the retired name · a dropped `</div>` fails tag balance, structure and §25.2. Diff audit: 83 lines
removed, all of them the four intended blocks plus three version lines.

## THREE THINGS S74 LEARNED THE HARD WAY
1. **Grep the retired names, not the live ones.** The whole session's shape turned on it. A lesson that
   looks like it has nothing to redistribute usually has everything, wearing an old label. Now §25.10b.
2. **The skill gate counts the literal `☐`, not `&#9744;`.** The first build emitted the entity. A
   post-condition caught it; no gate would have, because the gate would have read 0 boxes against 13 tags
   and only fired on the mismatch — which it did, but only after the post-condition had already stopped it.
   Emit the character the gate counts.
3. **Check the file's typographic convention before authoring into it.** L04 runs straight apostrophes
   **649:3** over curly. Two migrated skill items had been given `&rsquo;`. Migrated prose keeps the
   source's own characters; only new scaffolding follows the family style.

## INFERRED IN S74 (flagged, one line each)
- **Subjects stripped to bare verb phrases in BC02** — L01/L02/L03 all phrase skills that way and the
  block's own title is *Can You…?*; L04's full-sentence items were the outlier.
- **Two items reworded past a pure subject strip** — tense ("I wrote and ran" → "Written and run") and
  clause order ("When readings looked wrong, I checked X" → "Checked X when readings looked wrong"); both
  are grammar consequences of the *I have…* label, now recorded in §25.10b.
- **§10 order BC02 → BC03 → BC04 → WHAT'S NEXT → Engineer's Log** — fewest moves, following S73's L03
  approach of leaving non-check material where it sits.
- **Item 6 kept in Mental despite being taught in §5 rather than §3** — §25.2 says §5 is reading and BC01
  seats after it, so a student who did the reading has seen it.
- **BC01's intro says "before you wake a single sensor"** — L03's says "before you build a single line";
  the sentence is per-lesson and this is L04's first action.
- **Item 10's achievability accepted without a new rep (§25.10)** — Step 4 is literally "loop(): raw
  readings to the Serial Monitor" and Step 7 is the deliberate dead-digits mismatch, so every student who
  did the lesson has checked raw numbers when readings looked wrong.

## S75 QUEUE
1. **L05 Brain Check conversion** (§25 rollout — L01/L02/L03/L04 done, no jumping). **Open §25.10b first:**
   grep the retired-name list against L05 before deciding what has to be authored.
2. **UNRESOLVED — the §25.8 cap conflict.** §25.2 says the Knowledge Check count "scales with the lesson";
   §25.8 caps it at **5**. **L02 is live at 7** and no gate counts BC03 at all. L03 and L04 both came out
   at 5 so neither needed the ruling; DJ ruled at S74 open to let L04 ship at 5 and leave the conflict
   open. L05 may force it. On the table: floor of 4, no ceiling, plus a BC03 count added to the gate.
3. **L04's Technical Skills is now 13 items where §2 has 11 objectives** — §25.2 says they should be equal.
   DJ ruled at S74 open: leave both lists alone, reconcile at the final read-through. Same ruling as L03
   (8 vs 11). **Three lessons now carry this debt.**
4. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware & Code"
   — found S72, one-line fix, still not done. It was in scope-adjacent territory this session and was
   deliberately left alone to keep the conversion diff clean.
5. Warm-ups L02–L16 + spiral aiming rule — **warm-ups are still L02-ONLY**, so L02 is the prototype.
6. Bonus challenges §10→§9 (12 cards; pill/livery ruling still open) · L13/L15 have no exit blocks at all ·
   §2 objectives from Technical Skills checklists · within-lesson build-on mark.
7. going_deeper footer contrast + duplicated hero title.
8. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen — the dividend is
   claimed in Bible §4.4 and still has not been checked against the Maker.

## OPEN — NEEDS A DJ RULING
- The §25.8 cap (queue item 2) — still the one live canon conflict.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge cards
  (nine sessions now) · spiral marking format review · DJ tier pass + rolling depth read (L14 first) ·
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
*Written at S74 close, July 26 2026. The whole session turned on one grep. The queue had L04 down as the
first conversion that was mostly authoring, and the live-name sweep agreed with it — but §25.2 keeps a list
of names it has retired, and the second entry on that list was sitting in §10 with ten answers already
written. Two of the citations built on top of it pointed at sections that never taught the fact, which is
now the fourth defect §25.10a has caught and the fourth that no gate could see.*

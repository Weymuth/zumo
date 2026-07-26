# ZUMO — S77 Handoff (written at S76 close, Jul 26 · paste at top of Session 77)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **21** must PASS (gate file **v1.7**). Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
6. §25.10b: grep §25.2's RETIRED-NAME list before scoping any conversion.
7. §25.10c: if the sweep returns TWO ancestor blocks, diff them item by item before calling either waste.
8. **NEW — §25.10d: when a citation will not verify, ask whether the SECTION is wrong or the CONTENT is
   missing.** L06's was missing. Write the content; never re-aim the citation at the nearest plausible §.
   And **follow the lesson's own internal pointers by hand** — the §24 promise gate is cross-lesson only.

## LIVE STATE at S76 close — VERIFIED BY FRESH CLONE
Commit **`f6976756`**, Jul 26 13:19 EDT. All four delivered files byte-identical to delivery; gates
21/21 PASS against the pushed tree; no strays.

L01 v03.10.0 · L02 v03.0.0 · L03 v03.14.0 · L04 v04.7.0 · **L05 v04.9.1** · **L06 v04.12.0** ·
L07 v04.7.2 · L08 v04.6.2 · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 · L13 v02.6.2 ·
L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.62** · Maker v2.45.1 · book_gates **v1.7 (21 gates)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Brain Check family: six of sixteen converted — L01–L06.** Column byte-identical in all six:
**5,639 chars / md5 `070806a6`, ending in `-->`.**

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io).

**DJ must eyeball L06:**
- **BC01** sits between §5's close and the §6 banner, un-nested (div depth 1, same as L01–L05).
- **BC02** is six items and unlocks only at 6/6.
- **BC03** and **BC04** sit in §10, in that order, followed by the 📘 Looking Ahead note, What's Next,
  and the Engineer's Log — the last three left exactly where they were.
- The **new sixth row** in §8's Quick Fix Table (distance accuracy → `WHEEL_DIAMETER_MM`).
- The column shows and hides below 700px and its check-offs persist across reload.

**Carried and still unverified from S72–S75:** L02's, L03's, L04's and L05's column below 700px ·
Mark-done persistence · the 7 ☐ / 12 ☐ / 13 ☐ / 9 ☐ unlocks · L01's §4 header and *Meet Your Robot*
table · L02's §4 *Meet Your Buttons* table.

## DONE IN S76

### L06 — the sixth conversion (v04.11.2 → v04.12.0)
1. **The §25.10b sweep came back empty.** No `Conceptual Understanding`, no `STOP & PROCESS`, nothing.
   §25.10c's two-block case did not arise. L06 is the **mirror image of L05**: a 4-item `Knowledge Check`
   with answers, one `Reflection` prompt, **no Technical Skills checklist and no Mental block**. So BC03
   migrated, BC04 half-migrated, and **BC01 and BC02 were authored from scratch**.
2. **BC01 Mental — 5, all authored.** Second encoder channel (§3.2) · 909.7 counts per wheel rotation and
   where the number comes from (§3.3) · 74.3 counts/cm from a 39 mm wheel (§3.4) · `for` vs `while` (§5.3) ·
   why the target is wrapped in `abs()` (§5.4). All five citations content-verified.
3. **BC02 — 6, and it is the first built under §25.5.** The six §2 objectives migrated **character-exact**,
   so Technical Skills and Objectives agree by construction. L06 never joins the reconciliation debt.
4. **BC03 — 5.** Four migrated character-exact (§5.2 · §8 · §5.5 · §3.6) plus one authored on Step 13's
   `averageCounts()` change (§6 Step 13). Per DJ ruling. **This conforms to §25.8's cap of 5 rather than
   forcing it** — see OPEN below.
5. **BC04 — 3.** The closed-loop reliability prompt migrated with its "Consider:" scaffolding, two authored.
   No reveals.
6. **§25.10d — the citation pointed at a hole.** *"Drives 33cm instead of 30cm, what should you adjust?"*
   answers `WHEEL_DIAMETER_MM`, which appears in exactly two places in the file: §6 Step 5 where it is
   declared, and the question itself. **DJ ruled to write the content, not re-aim the citation.** §8's Quick
   Fix Table gained a sixth row; the item now cites §8 truthfully.
7. **The reason it survived: a within-lesson promise that does not land.** Step 8's checkpoint reads *"Off
   by a lot? Section 8 has the table"* and §8 covered five faults, none of them distance accuracy. The §24
   gate only walks promises naming ANOTHER lesson. **No gate covers same-file pointers.**
8. **§4.2 gap closed.** L06's five mysteries carried no `data-challenge` markers — tagged `6.m1`–`6.m5` on
   the L05/L11 convention (`data-kind="mystery"`).
9. **Bible v8.61 → v8.62 — new §25.10d.**

### L05 v04.9.0 → v04.9.1 — a placeholder shipped live in S75
BC01 item 3 carried `<code style="{CODE}">DETECTION_THRESHOLD = 1</code>`. The browser discards the invalid
declaration, so the code span rendered unstyled. **Only occurrence book-wide.** Cosmetic, so minor bump and
the visible banner left alone per §5b. **No gate covers unsubstituted template placeholders** — a one-line
`grep -rn '{[A-Z]*}' --include=*.html` gate would have caught it.

### The Bible's own column fingerprint was the short slice
§25.10c mandates copying START through the **full 43-character** END comment, then recorded the block as
**5,596 chars / `8fa00744`** — which is the span measured START through *before* the terminator. Verifying a
column against that figure means slicing 5,596 and reproducing the exact unterminated-comment defect the
rule exists to prevent. **The live files were never wrong; the paperwork was.** Canonical is now
**5,639 / `070806a6`**, and §25.10d says a rule that records its own fingerprint must record the span it
mandates.

### Verification
21/21 gates PASS, pill_sweep clean, column byte-identical across all six converted lessons. **Four control
runs, each with a landed-injection assert, each restoring byte-identical:** a stripped `data-bc-skill` fails
with the exact `06: BC02 has 6 checkbox items but 5 data-bc-skill tags` · a reintroduced
`Conceptual Understanding` fails on the retired name · a 42-of-43-byte END comment fails the parse gate
while **tag balance passes**, reproducing S75 · a dropped `</div>` fails both. Content-preservation audit:
**12 exit-region items manifested before any edit, ACCOUNTED 12 · LOST 0.** Diff audit: 34 lines removed,
every one a version line, an intended block, or a mystery heading being retagged.

## THREE THINGS S76 LEARNED THE HARD WAY
1. **A citation that will not verify may be pointing at nothing.** Three sessions of mis-aimed citations
   trained the reflex to re-aim. L06's had no target at all, and re-aiming it at §3.4 — which supplies the
   formula and nothing else — would have looked like a fix and left the hole. Now §25.10d.
2. **The rule's own fingerprint was measured against the wrong span.** §25.10c warns that one byte short
   takes the file down, and then records the short figure as canonical. A rule can be right and its
   evidence wrong in the same paragraph.
3. **My first control run injected nothing and reported ALL GATES PASS.** Stripping
   `data-bc-skill="6"` left `data-bc-skill` in the column's script selector, so the count-based assert was
   satisfied and the "gate is blind" conclusion was one line away. §24.6c caught it because the assert was
   there — **the injection assert is the control run's control run.**

## INFERRED IN S76 (flagged, one line each)
- **BC03's new item cites "§6 Step 13"** — L06 carries no subsection ids at all, and Step 13 is where
  `averageCounts()` is actually taught; verified by level-aware heading slice.
- **The 📘 Looking Ahead note stayed outside BC04** — it is §6.6a enrichment, not a Reflection prompt, and
  moving it was not ruled on.
- **BC02 keeps "Understand the difference…"** despite the soft verb — rewording reopens the §25.5 gap the
  ruling closes; §25.5 makes §2 the anchor either way.
- **BC01's five items are §-ordered** (§3.2 → §3.3 → §3.4 → §5.3 → §5.4), matching the S75 L05 ruling.
- **The §8 row is placed after "Robot never stops"** so distance faults group before turn faults.

## S77 QUEUE
1. **L07 Brain Check conversion** (§25 rollout — L01–L06 done, no jumping). Open §25.10b, §25.10c **and
   §25.10d** first. L07 has 5 untagged mysteries; tag them in the same edit.
2. **UNRESOLVED — the §25.8 cap conflict, now dodged FOUR times.** §25.2 says the count "scales with the
   lesson"; §25.8 caps it at **5**. L03, L04 and L06 came out at 5, L05 at 4. **L02 is live at 7 and no gate
   counts BC03 at all.** On the table: floor of 4, no ceiling, plus a BC03 count added to the gate.
3. **NEW GATES WORTH WRITING** (each caught something no gate could see this session):
   - **placeholder gate** — `{[A-Z_]+}` inside an attribute value, book-wide (would have caught L05's `{CODE}`).
   - **§4.2 coverage gate** — every `<h4>` inside a bonus/mystery block carries `data-challenge`.
     The current gate checks uniqueness, not coverage, which is why 25 mysteries were invisible.
   - **within-lesson promise gate** — "Section N has/covers X" resolves inside the same file (§25.10d).
4. **Queue item 9, VERIFIED and quantified: 20 mysteries still untagged** — L04 (5) · L07 (5) · L08 (5) ·
   L09 (5). L05 (6) and L11 (4) are done. Fold each lesson's tagging into its conversion.
5. **Bonus placement is a 9/6 split, not "12 cards in L02/L03."** After §10: L02, L03, **L06**, L07, L10,
   L13, L14, L15, L16. In the §9 region: L04, L05, L08, L09, L11, L12. L01 has none. **L06 was NOT moved
   this session** — the conversion did not touch placement.
6. **L13 and L14 bonus banners carry a doubled 🕵️** (`&#128373;&#65039;` twice). L15/L16 correct.
   One-line fix each, found S76, not done.
7. **Technical Skills vs §2 objectives — still THREE lessons carry the debt.** L03 8 vs 11 · L04 13 vs 11 ·
   L05 7 vs 10. L06 does not, per §25.5. DJ ruled at S74 open to reconcile at the final read-through.
8. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware & Code"
   — found S72, one-line fix, still not done.
9. Warm-ups L02–L16 + spiral aiming rule — **warm-ups are still L02-ONLY**, so L02 is the prototype.
10. L13/L15 have no exit blocks at all · §2 objectives from Technical Skills checklists elsewhere ·
    within-lesson build-on mark · going_deeper footer contrast + duplicated hero title.
11. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen — the dividend is
    claimed in Bible §4.4 and still has not been checked against the Maker.

## OPEN — NEEDS A DJ RULING
- The §25.8 cap (queue item 2) — the one live canon conflict, four lessons unforced.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge cards
  (eleven sessions now) · spiral marking format review · DJ tier pass + rolling depth read (L14 first) ·
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
*Written at S76 close, July 26 2026. The queue said L06 would be a conversion and it was, but the ancestor
was thin and the interesting part was a question with nowhere to point. Three sessions of finding
mis-aimed citations had built a reflex to re-aim them; this one had no target, and re-aiming it at the
section holding the formula would have looked exactly like a fix. The hole existed because a checkpoint in
§6 promised a table in §8 that did not cover the fault, and no gate walks a promise that stays inside one
file. The other thing worth remembering is smaller and worse: the first control run injected nothing,
reported ALL GATES PASS, and was one line from becoming a finding that the skill gate was blind.*

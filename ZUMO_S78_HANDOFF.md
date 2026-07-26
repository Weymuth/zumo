# ZUMO — S78 Handoff (written at S77 close, Jul 26 · paste at top of Session 78)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **21** must PASS (gate file **v1.7**). Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
6. §25.10b/c/d as before — **and now §25.10e.**
7. **NEW — §25.10e: the retired-name sweep is a LEAD, NOT A VERDICT.** L07's returned zero while the
   lesson held two live ancestors. Scope a conversion by **reading §10 and asking what job each block
   does**, never by grepping what it is called. And control-run the sweep itself — a grep that returns
   nothing everywhere is indistinguishable from a broken pattern.

## LIVE STATE at S77 close — VERIFIED, gates 21/21 PASS
L01 v03.10.0 · L02 v03.0.0 · L03 v03.14.0 · L04 v04.7.0 · L05 v04.9.1 · L06 v04.12.0 ·
**L07 v04.8.0** · L08 v04.6.2 · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 ·
L13 v02.6.2 · L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.63** · Maker v2.45.1 · book_gates **v1.7 (21 gates)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Brain Check family: seven of sixteen — L01–L07.** Column byte-identical in all seven:
**5,639 chars / md5 `070806a6`, ending in `-->`.**

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io).

**DJ must eyeball L07:**
- **BC01** sits between §5's close and the §6 banner, un-nested (div depth 1, as L01–L06).
- **BC02** is **nine** items and unlocks only at 9/9 — the longest skill gate in the book.
- **BC03** is six, each with a §-citation; **BC04** is three, no reveals.
- The 💡 *Visual Learners: Draw Your Project!* tip is still in place between BC02 and BC03 — it was
  **not** moved or folded (§6.6a enrichment; not ruled on).
- The five mysteries now carry `7.m1`–`7.m5` and should appear in the Tutor picker.

**Carried and still unverified from S72–S76:** the column below 700px in L02–L06 · mark-done
persistence · the 7 ☐ / 12 ☐ / 13 ☐ / 9 ☐ unlocks · L01's §4 header and *Meet Your Robot* table ·
L02's §4 *Meet Your Buttons* table · L06's BC01 placement, 6/6 unlock, and the new §8 sixth row.

## DONE IN S77

### L07 — the seventh conversion (v04.7.2 → v04.8.0)
1. **The §25.10b sweep returned ZERO and was wrong.** No retired name anywhere in L07 — yet a 6-item
   *Self-Assessment* and a 7-item *Knowledge Check* were both live, the second under BC03's own name.
2. **BC01 Mental — 5, all authored,** at the §5/§6 seam. Citations content-verified: §3.3 (the
   semicolon that makes a declaration a promise) · §3.4 (three things a .cpp holds) · §3.7 (global vs
   local scope) · §3.1 (a real compiler error caused by poor organization) · §5.1+§5.2 (eight files,
   one job each).
3. **BC02 — 9,** §2's objectives migrated per §25.5, so Technical Skills and Objectives agree by
   construction. **L07 never joins the reconciliation debt.** Extracted programmatically from §2
   rather than retyped; the only change is `&#9744;` → literal `☐`, which renders identically and is
   what the skill gate counts.
4. **BC03 — 6.** All six citations verified by content: §3.3 · §8A.1 · §3.6 · §3.5 · §3.8 · §8.
5. **BC04 — 3.** The practical seventh Knowledge Check question **reshaped into Reflection** — it had
   no single correct answer and cited no section anywhere in the lesson. Two authored. No reveals.
6. **Five mysteries tagged** `7.m1`–`7.m5` (§4.2).
7. **Bible v8.62 → v8.63** — §25.8 rewritten, new §25.10e.

### DJ rulings this session
- **§25.8 cap is a FLOOR, not a ceiling** — *"keep more than 5 and we can weed them out later."*
  Knowledge Check runs **4 minimum, no maximum**. Ends a conflict dodged four times.
- **Nothing is retired** — *"Don't retire them, put them somewhere for us to evaluate later."*
  New root file **`ZUMO_PARKED_EXIT_ITEMS.md`**.

### A checklist item that contradicted its own lesson
Self-Assessment item 2 asked students to tick *"Write include guards for a header file."* §3.6 files
include guards under 📘 *The Old Way* and teaches `#pragma once`; the Glossary agrees. Never achievable
as written (§25.10). **Not carried into BC02**; parked with a recognition-shaped rewrite.

## THREE THINGS S77 LEARNED THE HARD WAY
1. **The sweep that scopes the work was itself ungated.** §24.6c was written about audit greps and
   §25.10b about scoping greps, and nobody had connected them. L07's zero was only usable because the
   same grep was run across L07–L16 and fired on four lessons.
2. **My first content-preservation audit reported LOST 2.** Bad slice boundaries — 15 Self-Assessment
   items where there are 6, zero Knowledge Check items where there are 7. Corrected: **13 manifested,
   ACCOUNTED 13, LOST 0.** In the session whose finding is that scoping greps lie, the verification
   grep lied first.
3. **Three of the four gate failures on first run were canonical STRINGS, not structure.** The gate
   hardcodes `KNOWLEDGE CHECK &mdash; What You Just Built` and `REFLECTION &mdash; In Your Notebook`
   and counts the literal `☐`. Authoring a better-worded header is a gate failure. **Copy the header
   strings from the previous conversion; do not compose them.**

## INFERRED IN S77 (flagged, one line each)
- **BC01's five items are §-ordered** (§3.3 → §3.4 → §3.7 → §3.1 → §5.1) — matching the S75/S76 rulings.
- **BC01 draws only on §1–§5** — §25.2 places Mental at the last seam before hands-on, and L07's §6 is
  *Build It*, so §8A was excluded even though it teaches declaration-vs-definition formally.
- **BC03 q2 cites §8A.1, not §3.2** — both contain the distinction; §8A.1 is titled *Declarations vs.
  Definitions* and teaches it formally, where §3.2 only carries the 🔑 KEY pair.
- **The 💡 Visual Learners tip stayed between BC02 and BC03** — §6.6a enrichment, not an exit construct,
  and moving it was not ruled on.
- **L07 bumped moderate (v04.8.0), not major** — four new blocks in one lesson matches the L03–L06
  precedent for a conversion.

## S78 QUEUE
1. **L08 Brain Check conversion** (§25 rollout — L01–L07 done, no jumping). **Open §25.10e first, and
   expect *Check Yourself* to be the ancestor** — verified present at S77, invisible to the retired-name
   sweep. L08 has 5 untagged mysteries; tag them in the same edit.
2. **THE FLOOR GATE IS NOW WRITABLE AND IS NOT WRITTEN.** §25.8 is settled (floor of 4, no maximum), so
   a BC03 count gate asserting `>= 4` passes all seven converted lessons today. **Write it in S78** —
   §24.2 says a rule canonized without its gate only holds where someone happens to look.
3. **OTHER GATES WORTH WRITING** (each caught something no gate could see):
   - **placeholder gate** — `{[A-Z_]+}` inside an attribute value, book-wide (S76's `{CODE}`).
   - **§4.2 coverage gate** — every `<h4>` in a bonus/mystery block carries `data-challenge`.
   - **within-lesson promise gate** — "Section N has/covers X" resolves inside the same file (§25.10d).
   - **NEW — unretired-ancestor gate**: flag any `<h3>` in §10 of an *unconverted* lesson that looks
     like an exit construct (a ☐ list, or a numbered list with reveals) regardless of its name. This is
     §25.10e made machine-checkable and would have caught L07, L08, L11, L15, L16 in one pass.
4. **20 → 15 mysteries still untagged:** L04 (5) · L08 (5) · L09 (5). L05, L06, L07, L11 done.
5. **Unretired ancestors confirmed live and unswept:** L08 *Check Yourself* · L11 *Skills Check* ·
   L15/L16 *Wrap-Up*. Fold each into its lesson's conversion.
6. **Technical Skills vs §2 objectives — still THREE lessons carry the debt.** L03 8 vs 11 · L04 13 vs
   11 · L05 7 vs 10. L06 and L07 do not, per §25.5. DJ ruled at S74 to reconcile at the final read-through.
7. **Bonus placement is a 9/6 split.** After §10: L02, L03, L06, L07, L10, L13, L14, L15, L16. In the §9
   region: L04, L05, L08, L09, L11, L12. L01 has none. **L07 was NOT moved this session.**
8. **L13 and L14 bonus banners carry a doubled 🕵️** (`&#128373;&#65039;` twice). One-line fix each,
   found S76, still not done.
9. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware &
   Code" — found S72, one-line fix, still not done.
10. Warm-ups L02–L16 + spiral aiming rule — **still L02-ONLY**, so L02 is the prototype.
11. L13/L15 have no exit blocks at all · within-lesson build-on mark · going_deeper footer contrast +
    duplicated hero title.
12. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen.

## OPEN — NEEDS A DJ RULING
- **The weeding criterion.** §25.8 now allows any count ≥ 4, and `ZUMO_PARKED_EXIT_ITEMS.md` holds the
  over-count list — but **there is no rule for what makes a BC03 item weakest.** Until there is, the
  weeding pass cannot start. L02 (7) and L07 (6) are the two candidates.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge cards
  (twelve sessions now) · spiral marking format review · DJ tier pass + rolling depth read (L14 first) ·
  copyright line (RoboLore, work-for-hire) · bonus-challenge pill + livery when they move to §9.

## STANDING QUEUE (carried; SUSPECTED until re-checked per §24.6c)
L02 `2.t7` label collision (VERIFIED latent) · BENCH: compile-verify L07 finished + trapezoid · L08
Racing Line · L11 C4 double-TRIM · Q017 L09 six numbers · calibration-spin · gyro-bias · L02 §5
green-LED · Constrain RUN_MS · L15 C04–C07 no-template shape · L01 VS Code multi-root step ·
landing-page/book color mismatch · Maker batch (bulk DL · `?lesson=N` gate · C## labels · verify
`?kind=` starters) · TDP v3 (A5 Lab Log + printed 16 log prompts) · course docs (grid + syllabus) ·
"pick your robot" chooser · AI Tutor DISCOVERIES picker · QA_* sheets in images/glowbots · border inset
10–18 vs 64 · Canvas reading quizzes (book first, then Canvas).

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page — **note:** it has a home now, as L01's
§4 Hardware, with Install moving down.

---
*Written at S77 close, July 26 2026. The queue said L07 would be a conversion and it was, but the
interesting part happened before any editing: the grep that decides how much work a conversion is came
back empty on a lesson holding two live ancestor blocks. It was right that no RETIRED name was present
and wrong about everything that mattered, because the list only ever held names somebody had thought to
retire, and "Self-Assessment" and "Knowledge Check" were never bad enough to notice. The rule that came
out of it is §25.10e, and the honest version of the lesson is smaller than the rule: a sweep that
returns nothing everywhere looks exactly like a sweep that is broken, and the only thing separating
those two cases is running it somewhere you already know the answer. The other thing worth remembering
is that my own preservation audit reported two lost items, in the session whose finding is that greps
lie. It was the slice boundaries. The items were all there.*

# ZUMO — S79 Handoff (written at S78 close, Jul 26 · paste at top of Session 79)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **22** must PASS (gate file **v1.8**). Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
6. §25.10b/c/d/e as before — **and now §25.10f.**
7. **NEW — §25.10f: an ancestor claim is a lead too, including one written into the Bible.**
   Three of the four unswept ancestors §25.10e named at S77 were wrong. Before a recorded ancestor
   becomes the scope of a conversion, open the file: confirm the block exists, is a **heading and not
   prose**, and does the job the record claims. Grep case-insensitively, then **read the hit**.

## LIVE STATE at S78 close — VERIFIED, gates 22/22 PASS
L01 v03.10.0 · L02 v03.0.0 · L03 v03.14.0 · L04 v04.7.0 · L05 v04.9.1 · L06 v04.12.0 ·
L07 v04.8.0 · **L08 v04.7.0** · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 ·
L13 v02.6.2 · L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.64** · Maker v2.45.1 · book_gates **v1.8 (22 gates)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Brain Check family: eight of sixteen — L01–L08.** Column byte-identical in all eight:
**5,639 chars / md5 `070806a6`, ending in `-->`.**

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io).

**DJ must eyeball L08:**
- **BC01** sits between §5's close and the §6 banner at **div depth 0** — which is where L01–L05 and L07
  sit. (**L06 is at depth 1**, inside its §5 panel; see findings below.)
- **BC02** is **nine** items, unlocks at 9/9, and is character-exact against §2.
- **BC03** is **six**; **BC04** is three, no reveals.
- **Record Your Calibration** kept its own §10 subsection per DJ ruling, now unnumbered.
- The five mysteries carry `8.m1`–`8.m5` and should appear in the Tutor picker.

**Carried and still unverified from S72–S77:** the column below 700px in L02–L06 · mark-done
persistence · the 7 ☐ / 12 ☐ / 13 ☐ / 9 ☐ / 9 ☐ unlocks · L01's §4 header and *Meet Your Robot* table ·
L02's §4 *Meet Your Buttons* table · L06's BC01 placement, 6/6 unlock, and its §8 sixth row · **all of
L07's S77 eyeball list**, which was queued for S78 and is still not confirmed.

## DONE IN S78

### L08 — the eighth conversion (v04.6.2 → v04.7.0)
1. **§25.10e's recorded ancestor for L08 did not exist.** Reading §10 found a three-item **Knowledge
   Check** under BC03's own live name and **no ☐ checklist at all** — L08's twenty box glyphs were nine §2
   objectives plus eleven §7 *Pass?* test cells.
2. **BC01 Mental — 5, all authored,** at the §5/§6 seam, §-ordered §1 → §3.1 → §3.2 → §5.1 → §5.3. Every
   citation content-verified: bang-bang and the binary actuator it suits · the formula's three parts ·
   which motor gets the + · why the error is signed · what `constrain()` protects.
3. **BC02 — 9,** §2's objectives migrated per §25.5 and **programmatically verified character-exact**;
   the only change is `&#9744;` → literal `☐`, which is what the skill gate counts.
4. **BC03 — 6.** Three ancestors migrated verbatim and given citations (§3 · §3.1+§5.1 · §7.3); three
   authored (§6 Step 4's two-faced `extern` error, `gapStartTime` on the second gap, the TRIM test).
5. **BC04 — 3.** No reveals. Feeds Software + Performance Evaluation.
6. **Achievability checked, nothing to fix.** Objective 5 gates on the chance-dependent `extern` red
   build, but §6 Step 4 already ships the rep: *"Went green first try? Earn the encounter anyway."*
7. **Five mysteries tagged** `8.m1`–`8.m5` with `id="mystery-N"` (§4.2).
8. **Bible v8.63 → v8.64** — §25.10e's list corrected, new §25.10f, §25.8's gate status updated.
9. **book_gates v1.7 → v1.8** — the §25.8 floor gate, control-run three ways.

### DJ rulings this session
- **Record Your Calibration stays separate** — its own §10 subsection, outside the Brain Check family.
  Matches L03 (*My Robot's Calibration Data*) and L09 (*Calibration Data Record*).
- **Bump the Bible for the §25.10e correction** rather than holding it as its own edit.

## THREE THINGS S78 LEARNED THE HARD WAY
1. **The rule was right and its evidence was not.** §25.10e says a name is a lead, and then closed by
   listing four ancestors nobody had opened the files to check. One did not exist, one was misnamed, two
   were section banners. A wrong finding promoted into canon gets quoted forward for sessions.
2. **My preservation audit reported LOST 1 again, and again it was mine.** The content was present; the
   migration had retyped a literal `×` as `&times;` and my normaliser did not unescape entities. Second
   session running where the verification step was wrong before the work was. Restored character-exact.
3. **Three of the four gate failures S77 blamed on canonical strings never happened here** — because the
   header strings were copied from L07 rather than composed. That advice works; keep following it.

## INFERRED IN S78 (flagged, one line each)
- **L08's `10.1/10.2/10.3` numbering dropped** — L08 was the only lesson in the book with numbered §10
  subsections; all fifteen siblings are unnumbered.
- **BC02's intro text copied from L07 unchanged** — both lessons have exactly nine objectives, so the
  sentence is true of L08 without editing.
- **BC01 excluded §6–§8A** — §25.2 places Mental at the last seam before hands-on, and L08's §6 is
  *Build It*, so the `extern` and TRIM material lives in BC03 instead.
- **L08 bumped moderate (v04.7.0)** — four new blocks in one lesson, matching the L03–L07 precedent.

## S79 QUEUE
1. **L09 Brain Check conversion** (§25 rollout — L01–L08 done, no jumping). **L09 already carries TWO live
   ancestors:** *Technical Skills: Can you…?* and *Knowledge Check*, both confirmed present at S78 and on
   no list anywhere. Expect a redistribution job, not an authoring job. L09 has 5 untagged mysteries; tag
   them in the same edit. Also note L09 keeps a *Calibration Data Record* — per the S78 ruling it stays.
2. **OPEN RULING — BC03's reveal type splits the family 4/4.** L01–L04 use `data-reveal="quiz"`;
   L05–L08 use `data-reveal="solution"`. §20.1 strips only `solution`, so half the converted Knowledge
   Check answers are visible to the AI Tutor and half are not. Same construct, opposite behaviour. **Needs
   a DJ ruling on which is canonical before L09 is written**, or L09 inherits the coin-flip.
3. **L06's BC01 is at div depth 1** where the other seven sit at 0 — it is inside its §5 panel rather than
   between sections. Not the L01 white-on-white class (the panel is white-bordered, not a coloured
   banner), so cosmetic. One-line fix whenever L06 is next open. **The S78 handoff had this backwards**,
   recording depth 1 as the family norm.
4. **OTHER GATES WORTH WRITING** (carried; each caught something no gate could see):
   - **placeholder gate** — `{[A-Z_]+}` inside an attribute value, book-wide (S76's `{CODE}`).
   - **§4.2 coverage gate** — every `<h4>` in a bonus/mystery block carries `data-challenge`.
   - **within-lesson promise gate** — "Section N has/covers X" resolves inside the same file (§25.10d).
   - **unretired-ancestor gate** — flag any `<h3>` in §10 of an *unconverted* lesson that looks like an
     exit construct (a ☐ list, or a numbered list with reveals) regardless of its name. §25.10e/f made
     machine-checkable; would have caught L09, L11, L15, L16 in one pass.
   - **NEW — BC03 reveal-type gate**, once item 2 is ruled.
5. **15 → 10 mysteries still untagged:** L04 (5) · L09 (5). L05, L06, L07, L08, L11 done.
6. **Unretired ancestors, corrected inventory:** L09 *Technical Skills* + *Knowledge Check* (both real) ·
   L11 *Skills **Checklist*** (real, misnamed at S77) · L15/L16 *Wrap-Up* is a **section banner**, and
   §25.9 records L15 as having no exit block at all. **L08 *Check Yourself* never existed.**
7. **Technical Skills vs §2 objectives — still THREE lessons carry the debt.** L03 8 vs 11 · L04 13 vs
   11 · L05 7 vs 10. L06, L07 and L08 do not, per §25.5. DJ ruled at S74 to reconcile at the final
   read-through.
8. **The weeding criterion still does not exist.** §25.8 allows any count ≥ 4 and the floor gate now
   enforces the floor, but nothing says what makes a BC03 item weakest. L02 (7), L07 (6) and L08 (6) are
   the candidates. `ZUMO_PARKED_EXIT_ITEMS.md` gained nothing this session — nothing was cut.
9. **Bonus placement is a 9/6 split.** After §10: L02, L03, L06, L07, L10, L13, L14, L15, L16. In the §9
   region: L04, L05, L08, L09, L11, L12. L01 has none. **L08 was NOT moved this session.**
10. **L13 and L14 bonus banners carry a doubled 🕵️** (`&#128373;&#65039;` twice). One-line fix each,
    found S76, still not done.
11. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware &
    Code" — found S72, one-line fix, still not done.
12. Warm-ups L02–L16 + spiral aiming rule — **still L02-ONLY**, so L02 is the prototype.
13. L13/L15 have no exit blocks at all · within-lesson build-on mark · going_deeper footer contrast +
    duplicated hero title.
14. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen.

## OPEN — NEEDS A DJ RULING
- **BC03 reveal type** (queue item 2) — blocks L09 cleanly.
- **The weeding criterion** (queue item 8) — blocks the weeding pass.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge cards
  (thirteen sessions now) · spiral marking format review · DJ tier pass + rolling depth read (L14 first) ·
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
*Written at S78 close, July 26 2026. The queue said to open §25.10e first and expect* Check Yourself *to
be L08's ancestor. §25.10e is the rule that says a name is a lead and not a verdict, and it closed by
listing four ancestors that nobody had opened a file to verify — so the session's first real finding was
that the rule had been written on exactly the evidence it forbids. Three of the four were wrong. What
makes it worth writing down is not that a list had errors; it is that the list was persuasive precisely
because it was in the Bible, which is the one place a claim stops getting re-checked. §25.10f is the
narrow version: a sentence outlives the grep that produced it, so bind the sentence too. The smaller
embarrassment is that my own preservation audit again reported a lost item that was never lost — a
retyped multiplication sign this time — in the second consecutive session whose lesson is that the
checking step fails before the work does.*

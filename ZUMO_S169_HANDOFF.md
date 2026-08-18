# ZUMO — S169 HANDOFF (written at S168 close · paste at top of Session 169)

## READ THIS FIRST

**S168's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S168_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**77/77 gates** · `gate_payload_match` **PASS both ends** · **`byte_audit --check` PASS across six arms,
`--selftest` ALL NINE CONTROLS PASS** on a harness built from scratch by the script (`objects: 41`,
standing control **20,592** reproduced first) · `quiz_bank --selftest` all controls ·
`session_versions --selftest` EIGHT CONTROLS · `callout_id` **1127/0** · `keyterm_prefix` 0 to convert ·
16 banks valid, **1,245** questions · census **40,974** · `site_parity` PARITY on two consecutive runs
after one first-run MISMATCH (S166 — believe the repeat) · `build_css --check` current at 574 rules ·
`image_audit --check` current · `next_pointer` clean.

**12 files changed, 0 new, 0 deleted** — verified by whole-tree md5 against a fresh clone:
`Lesson_13.html` · `Lesson_14.html` · `Lesson_15.html` · `Lesson_16.html` · `newproject.html` ·
`css/book.css` · `book_gates.py` · `build_family_map.py` · `quizzes/ZUMO_QUIZ_L13.yaml` · `L14` ·
`L15` · `L16` — plus `ZUMO_SUPER_BIBLE.md`, `ZUMO_AFTER_LAUNCH.md`, `LIVE_ZUMO_TEXTBOOK.md`,
**`ZUMO_S169_HANDOFF.md` new** and **`ZUMO_S168_HANDOFF.md` deleted**.

---

# THE FOUR THINGS TO CARRY OUT OF S168

## 1. SIX ARTEFACTS IN THE TREE WERE WRITTEN BY SOMETHING THAT WAS NOT THIS SESSION.

Found by the triple check, not by any gate. `LIVE_ZUMO_TEXTBOOK.md` had been rewritten with an S168
header and a full WHAT SHIPPED block; `ZUMO_SUPER_BIBLE.md` bumped to **v8.161** with an entry;
`ZUMO_AFTER_LAUNCH.md` re-aimed at S169; **`ZUMO_S168_HANDOFF.md` deleted**; an untracked
`ZUMO_S169_HANDOFF.md` authored; `Lesson_14.html` given six figure edits and a version bump; and
`QUIZ_L14` given an *S168 addendum* with a bump to v1.0.8.

**S146's finding verbatim: plausible is not authored.** The content was not obviously wrong — the L14
figures were the right values and closed a real hole in this session's own work — but **one claim in it
was false**, the addendum asserting *five stale figures* over a diff of six, in the file it was itself
changing (v8.109's trap).

**THE DISPOSITION SEPARATED CONTENT FROM PROVENANCE, on DJ's ruling *what is best for learning,
accuracy and the student*.** The FIGURES the book owed were re-derived by hand from the compile table
and kept. The four session DOCUMENTS were reverted, because they are the record of what a session did,
and adopting another author's narration asserts reads nobody can vouch for. All six are quarantined in
`/tmp/unattributed/` — **outside the repo, and they do not survive the container.** If provenance ever
matters again, the evidence is the fresh-clone md5 arm, not those copies.

**RUN ARM 3 AT EVERY CLOSE.** A whole-tree md5 against a fresh clone, reporting CHANGED / NEW / DELETED
by name. It is cheap, it is the only thing that caught this, and `session_versions --check` caught the
S146 instance for the same reason: **an instrument that compares the tree against its own record.**

## 2. THE RULING WAS UNBUILDABLE AS SEATED, AND THE ARTEFACT IS WHAT SAID SO.

Seating decision 2 put the discovery in §7D. **§7D runs the finished build** — its own words, *the
finished build (Maker: Lesson 13 → Finished)* — and Step 6b sits 175 lines above it, so a student
reaching that rung already has a sweep that ends and cannot see the failure they are told to watch for.

DJ re-ruled: the discovery opens **Step 6b itself**. The student runs the Step 6 build, watches the
sweep run out of floor and drive into the wall, presses B mid-corner and finds the kill switch dead,
and only then sees the corner they wrote. §7D gained one verifying line instead. **A ruling made against
a DESCRIPTION of an artefact is a lead; the artefact is the answer.**

`13/after_step_5` and `13/after_step_6` are **deliberately left blind** — they are what the discovery
runs on — and `KINDS[13]` gains a `step_6` door to reach `after_step_6`, which had no door because it
was byte-identical to `finished` until the fix made them different builds.

## 3. A ZERO-BYTE EDIT IS NOT ZERO BYTES UNTIL IT IS RECOMPILED.

To give `SWEEP_DONE` one canonical printed line serving four lessons, it was first seated after
`VICTIM_FOUND` — ahead of L15's `RUN_REPORT`. That **renumbered `RUN_REPORT` and moved L15 and L16 by
+2**, silently invalidating some thirty figures re-derived minutes earlier. Caught by recompiling, not
by reasoning. Re-seated LAST so no existing enumerator moves and `RUN_REPORT` merely gains a comma.

**An enum is an ordered contract. Appending is free; inserting is not.**

## 4. A PATTERN SWEEP MISSED FIVE BANK FIGURES AND AN INDEPENDENT ARM NAMED ALL FIVE.

A six-pattern sweep over `QUIZ_L14` left `25,886` ×3 and `25,202` ×2 behind, because they sit inside
prose options rather than as bare figures. A claim-audit arm asserting **every** comma figure in the
four changed lessons and their banks against the compiled table found them immediately.

**S167's rule reached from the figure side: a word list is the one instrument that cannot report what
it omits.** **ITS OWN BLIND SPOT IS STATED (rule 78):** it asserts *matches SOME compiled build*, so it
is **blind to a figure naming the WRONG build** — seeded, a stale `25,198` beside Step 6b is SILENT,
because 25,198 is still `13/after_step_6`. That property is `byte_audit` ARM 2 and ARM 6's, which are
heading- and label-scoped. **The arm was thrown away with the session, like S167's. If it is wanted, it
is ARM 6's predicate widened from bank figures to every figure — and its blind spot must ship with it.**

---

# S169 OPENS HERE — WHAT IS ACTUALLY LEFT

- **THE TWO INSTRUMENT FIXES S167 EARNED ARE STILL UNBUILT**, and S168 did not touch them:
  `pio_harness.sh` still compiles with `-w` and `2>/dev/null`, so the compiler still cannot speak;
  and nothing in this repo checks a number stated in PROSE. The second one is now **half-earned twice**
  — S167's claim-audit arm and S168's were both written, both paid, and both discarded. **Population
  measurement comes first for the harness flag** (rule 34): S167 measured L10–L16 *finished* builds
  only, and the other ~180 payloads are a stated gap.
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE, AND S168 MEASURED THE COST OF THAT.**
  Its scope note says only L15 and L16 put figures in step headings — which is true — and
  **`Lesson_14.html` carried six stale figures in prose that no arm reaches.** Found by reading.
  L13's `25,198` sites and L16's `28,780` / `26,790` are the remaining unreachable class.
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166, unchanged) — the number lives in the Maker,
  the Bible and LIVE.md and appears nowhere in `Lesson_16.html`.
- **`28,780` AND `26,790` ARE INFERRED, NOT COMPILED** (this session). Neither has a payload:
  28,780 is a mid-trade checkpoint and 26,790 is *finished minus the buzzer*. Both moved +54 on the
  ground that every compiled L16 build from Step 2 onward moved exactly +54. **A payload for the
  mid-trade state is the honest fix, and S152's precedent says author it rather than delete the figure.**
- **`strip_inline --restore` DOES NOT RESPECT THE HELD LESSON STRIP.** The documented
  restore → build → apply cycle rewrote that block to inline styles in all sixteen lessons. Reverted;
  `css/book.css` was regenerated in a SCRATCH COPY and only the stylesheet brought back. **Measured,
  not fixed** — and the workaround is what every future repaint has to use until it is.
- **THE TAG-STRIP BLIND REGION IS MEASURED AND SEVEN RAW USES REMAIN**, in `byte_audit`,
  `lesson_inventory`, `glossary_convert` and `strip_inline`. Exposure is zero today: only **2 of 583
  comments in the tree can diverge** (an inner `<` OR `>` is the only way), and neither file those two
  live in is read by any of the four. **Do not widen them until that number changes.**
- **`BookComponentStandard.md` CARRIES 44 BRITISH FORMS AND IS DELIBERATELY UNSWEPT** (S167,
  unchanged) — `gen_component.py` pins the literal anchor `'### 5.2 Colour is never'`, rule 56.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165, unchanged). When it first fires, the answer is a ruling.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated. **L13-01 and L13-03 are now
  BUILT and CLOSED**, so the strongest two are gone; what is left needs adjudicating before it is
  worth anything.
- **THE `QUIZ_L13` ARC IS CLOSED IN THE SAME SESSION AS THE BUILD** — three new questions grade
  Step 6b (why the sidestep is the move that can end the sweep, why the two kill branches are
  different shapes, why `SWEEP_DONE` is a new state), and six that rested on the old corner were read
  in full and re-keyed. §5.2 no longer pins the sidestep's primitive, so the before-quiz cannot punish
  a careful reader.
- L12 BONUS B4's bench measurement · L15 Challenge 3's `turnDegreesGyroSafe()` · L03 queued content ·
  `ZUMO_L03_TEMPLATES.md` staging · Bible §14 TDP-canon entry · day-by-day grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path** (DJ, S156).
- **Fall launch Sept 8 — three weeks out. L13 is the last in-scope lesson and it is now whole.**

---

# HARNESS — IT IS NOT IN THE REPO. RUN THE SCRIPT.

```
sh harness_setup.sh
```
**Invoke it through `sh`, not `./`** — the file is tracked 100644 and the executable bit does not
survive GitHub Desktop. **Correct setup prints `objects: 41`.** Then, in order:

```
python3 byte_audit.py --sizes     # compiles every payload the Maker defines (~3 min)
python3 byte_audit.py --check     # six arms
python3 byte_audit.py --selftest  # NINE controls - run this before trusting --check
```

**CONTROLS — RE-VERIFIED AT S168 ON A HARNESS BUILT FROM SCRATCH. FOUR MOVED WITH STEP 6b AND FOUR
DID NOT, WHICH IS ITSELF THE CHECK:**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** — unmoved, because the fix lands at L13.
`13/finished` **25,246** (was 25,198) · `14/finished` **26,000** (25,942) ·
`15/finished` **28,402** (28,340) · `16/finished` **28,618** (28,564).
**Reproduce 20,592 before trusting the rest** (rule 30). The three declared overflows are
`16/after_step_3` **29,004** · `16/after_step_4` **29,640** · `16/step_5_serial_traded` **28,936** —
each +54, deliberate, and the lesson's own premise.

**THE TIGHTEST BUILD IN THE BOOK IS `16/after_step_2` AT 28,644, WITH 28 BYTES SPARE.** Not
`16/finished`, which has 54. Anything L16 ever gains again is priced against 28, and S167's pricing
looked at finished builds only.

**A ZERO-BYTE CLAIM IS A MEASURED CLAIM.** Snapshot `/tmp/zumo_byte_sizes.json`, re-run `--sizes`,
diff. S168's prose/label/bank pass moved **0 of 215**.

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see; moves
that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand and course
scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**§24.19 IS THE TIEBREAKER AND S168 IS ITS WORKED EXAMPLE.** Asked to choose between a ruled seating
and a buildable one, DJ ruled *what is best for learning, accuracy and the student* — and that decided
both the §7D re-seating and the unattributed-work disposition. **What was NOT decided unilaterally:**
the §7D contradiction, because it reverses a ruling DJ made; and the unattributed artefacts, because
adopting or reverting another author's work is not recoverable by measurement alone. **Both were
measured and handed over; the second one nearly shipped.**

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`3383f3f`**. Census **40,974**.
Bible **v8.161** · `BookComponentStandard` **v01.13.0** · Maker **v2.59** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.3** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.6.1** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.28.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.4.0** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`entity_sweep` **v1.0** ·
`font_stack_sweep` **v1.3.0** ·
`next_pointer` **v1.2** ·
`family_tag` **v1.2.1** ·
`glossary_convert` **v1.0** ·
`mark_wire` **v1.0.2** ·
`glyph_scan` **v1.1** ·
`title_feed` **v1.0** ·
`quiz_bank` **v1.6.1** ·
`timer.html` **v1.3.2** ·
`harness_setup.sh` **v1.0.1** ·
`pio_harness.sh` **v3.0** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.30.1 · L02 v03.21.5 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.33.0 · L14 v02.35.2 · L15 v02.31.8 · L16 v02.26.5.

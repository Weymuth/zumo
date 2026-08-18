# ZUMO — S168 HANDOFF (written at S167 close · paste at top of Session 168)

## READ THIS FIRST

**S167's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S167_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**77/77 gates** · `gate_payload_match` **PASS both ends** · **`byte_audit --check` PASS across six arms,
`--selftest` ALL NINE CONTROLS PASS** (harness rebuilt from scratch by the script, `objects: 41`,
standing control **20,592** first) · `quiz_bank --selftest` all controls · `session_versions --selftest`
EIGHT CONTROLS · `callout_id` **1125/0** · `keyterm_prefix` 0 to convert · 16 banks valid,
**1,242** questions · census **40,890** · `site_parity` PARITY on two consecutive runs ·
`build_css --check` current at 574 rules · `image_audit --check` current · `next_pointer` clean.

**12 files changed on the post-push pass** (L15 · ten banks · `newproject.html`), plus `ZUMO_SUPER_BIBLE.md`, `LIVE_ZUMO_TEXTBOOK.md` and this handoff. Fifteen lessons (all but L12) · sixteen banks · `newproject.html` ·
`ZUMO_SUPER_BIBLE.md` · `ZUMO_AFTER_LAUNCH.md` · `LIVE_ZUMO_TEXTBOOK.md` · **`ZUMO_S168_HANDOFF.md` new**
and **`ZUMO_S167_HANDOFF.md` deleted**.

---

# THE THREE THINGS TO CARRY OUT OF S167

## 1. THE FIRST MEASUREMENT SAID 19 AND THE TRUE POPULATION WAS 477.

DJ ruled **US spelling book-wide**, then ruled `center` for L14's RCJ transcription too. Scoping the
sweep to `centre` returned 19 lesson sites. The axis is a SPELLING SYSTEM, and the whole British set
returned **72 lesson sites, 130 bank strings and 274 in the Maker**. §24.6c on a predicate: scoping the
instrument to the lead's own vocabulary guarantees you measure only what you were already told.

**And the Maker's entire 274 is ONE WORD that is not a spelling — it is an IDENTIFIER.** `centre`
appears **zero** times in `newproject.html`; all 274 are `travelled`, of which 89 are the local in
L11's `blindDistanceCm()`. **Proved zero-byte rather than asserted:** all 215 payloads recompiled,
**0 of 430 stored figures moved.**

## 2. FIFTEEN LESSON BUMPS PUT 57 BANK PINS STALE AT ONCE, AND THE BUMPS WERE EARNED BY A CLOSED DIFF.

Gate 75 fired on every one — §24.18 working as designed with an empty backlog. Rule 37 says a pin bump
asserts a read; here the read is machine-closed and was **ASSERTED rather than claimed**: every changed
file diffed against a pre-sweep snapshot under a normalising transform, and **every one contains nothing
but swept words and its own version line**, L13 alone showing this session's two content edits.

**And the pin regex found S153's defect again: the banks spell their pins BOTH WAYS**, quoted and bare,
so the first pass moved 0 of 57 and reported success on files it had not touched.

## 3. GATE 74 HAS A BLIND REGION IN `newproject.html`, AND MY OWN EDIT EXPOSED IT BY ACCIDENT.

Writing the Maker changelog entry made gate 74 FAIL, naming a retired C1 slogan that had sat in the
**v2.58.4** entry since S162 with the gate GREEN throughout. Cause: gate 74 strips tags with
`re.sub(r'<[^>]+>', ' ', s)`, and `[^>]+` runs from any `<` to the next `>`, so a span of the Maker's
changelog comment is swallowed as one tag. **My entry contained the literal `<pre>`, whose `>` closed
the swallow early; removing it re-hid the slogan and the gate went green again.** The narration was
therefore REWORDED rather than the mask relied on. **NINE gates share the same tag-strip idiom** —
measured, not fixed, because widening nine gates three weeks from launch is a blast radius nobody has
measured (rule 26).

## 4. THREE PREDICATES, THREE UNDER-REACHES, AND EVERY ONE WAS A WORD LIST.

The sweep was declared complete three times and was wrong three times. The first list missed the `-ise`
family and `defence` (**33 survivors**). The second missed **its own words' INFLECTIONS** — `organises`,
`summarises`, `generalises`, `recognises`, `normalises`, the `-ises` forms of words already fixed bare —
found only by an arm run in the PUSHED clone. Only the fourth predicate closed it, and it closed because
it **derives** candidates instead of enumerating them: any `\w*is(e|es|ed|ing|er|ation)` whose `-iz` twin
is a real word, plus the non-`-ise` British set.

**THE RULE, IN ITS STRONG FORM: a spelling sweep's predicate must be MORPHOLOGICAL, never enumerated,
because a word list is the one instrument that cannot report what it omits.** §24.6c stated it about a
lead's vocabulary; this is the same rule about the sweeper's own.

**And two survivors were written by this session's own prose** — the Maker changelog spelled `centre` and
`travelled` inside the sentence asserting the Maker contained neither, v8.109's trap verbatim. Reworded.

**READING did the last mile, not the predicate.** 27 real sites separated from **15 false positives that
are US spelling too** — `compromise` ×7, `premise`, `advertised` ×2, `improvising`, `imprecise`,
`specialist` (§16.15). **DJ ruled `grey` STAYS**: four sites, all prose, read as a colour word rather than
a spelling. 23 shipped.


---

# S168 NEXT

- **THE TAG-STRIP BLIND REGION IS THE LARGEST OPEN INSTRUMENT ITEM.** Nine gates use
  `re.sub(r'<[^>]+>', ' ', s)`. The honest predicate strips COMMENTS as comments before stripping tags.
  Population unmeasured: nobody has asked what else is currently invisible inside an HTML comment
  anywhere in the tree. **That measurement is the first move, not the widening.**
- **`BookComponentStandard.md` CARRIES 44 BRITISH FORMS AND IS DELIBERATELY UNSWEPT.**
  `gen_component.py` pins the literal section anchor `'### 5.2 Colour is never'`, so sweeping it edits
  a generator's boundary string — rule 56. If it is ever swept, both move in the same commit.
  `ROBOCUP_RESCUE_LINE_2026.md` is held as the rulebook extract that must match its source (3 hits).
- **L13-05 IS APPLIED AND ITS BANK ARC IS CLOSED** — §5 now names the three assumptions and
  `QUIZ_L13` gains `A17b`. **L13-11 is VERIFIED**: the `readCalibrated()` quote is byte-faithful to
  the QTR bundled in `Zumo32U4@2.0.1` (pinned SHA `f4dfe05`, `git tag --points-at HEAD` → **2.0.1**).
  The defect was the sentence, and *four lines* is now deleted rather than replaced.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated. L13-01 (a missed prox stop
  recorded as a wall) and L13-03 (the sweep has no completion condition) are the strongest left, and
  both are ADJUDICATED AGREE with real algorithmic consequences.
- **`ZUMO_AFTER_LAUNCH.md`** — read at every session open alongside this handoff. Three items, all
  still open; its footer names the CURRENT handoff and must be re-aimed at every close.
- **`site_parity` IS NOT TRUSTWORTHY ON ITS FIRST RUN AFTER A PUSH** (S166, unchanged). Run it at
  least twice and believe the repeat.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165, unchanged). When it first fires, the answer is a ruling.
- **ARM 2 IS STILL BLIND TO A FIGURE STATED IN PROSE** (S166, unchanged). **L16 still never states its
  match-mode figure at all** — 28,504 lives in the Maker, the Bible and LIVE.md and appears nowhere in
  `Lesson_16.html`.
- **THE MAKER CHANGELOG STILL RECORDS NOTHING BETWEEN v2.49 AND v2.58** — deliberately un-back-filled.
- **`26,736` IS CORRECT BY MEASUREMENT AND GATED BY NOTHING** (S166, unchanged) — ARM 6 reaches only
  *Lesson N finished* labels. **Do not widen it until a real miss forces it.**
- `bonus_b5`'s deliberate sabotage survived S167 untouched. **Keep it that way.**
- L12 BONUS B4's bench measurement · L15 Challenge 3's `turnDegreesGyroSafe()` · L03 queued content ·
  `ZUMO_L03_TEMPLATES.md` staging · Bible §14 TDP-canon entry · day-by-day grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path** (DJ, S156).
- **Fall launch Sept 8 — three weeks out.**

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

**CONTROLS — ALL EIGHT RE-VERIFIED AT S167 ON A HARNESS BUILT FROM SCRATCH, AND UNMOVED BY THE SWEEP:**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,198** · `14/finished` **25,942** ·
`15/finished` **28,340** · `16/finished` **28,564**. **Reproduce the first one before trusting the
rest** (rule 30). The three declared overflows are `16/after_step_3` 28,950 · `16/after_step_4` 29,586 ·
`16/step_5_serial_traded` 28,882 — deliberate, and the lesson's own premise.

**A ZERO-BYTE CLAIM IS NOW A MEASURED CLAIM, NOT AN ARGUMENT.** S167's rename touched 89 payloads and
moved **0 of 430** figures. The method: snapshot `/tmp/zumo_byte_sizes.json`, re-run `--sizes`, diff.
Do that for any edit claimed to be comment-only or name-only.

---

# STANDING AUTHORITY — §24.17

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see; moves
that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand and course
scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**S167's worked example is the spelling ruling and its two halves.** The sweep itself was execution
once DJ ruled. What was NOT decided unilaterally: `BookComponentStandard.md`, because sweeping it
edits a generator's pinned anchor; and widening the nine tag-strip gates, because the population is
unmeasured. **Both were measured and handed over; neither ruling was taken.**

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`75dd9ea`**. Census **40,890**.
Bible **v8.160.2** · `BookComponentStandard` **v01.13.0** · Maker **v2.58.7** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.71.0** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.6** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
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

Lessons: L01 v03.30.1 · L02 v03.21.5 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.32.0 · L14 v02.35.1 · L15 v02.31.7 · L16 v02.26.4.

# ZUMO — S163 HANDOFF (written at S162 close · paste at top of Session 163)

## READ THIS FIRST

**S162's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S162_HANDOFF.md` is part of that push. **Delete `__pycache__/` and
`quizzes/__pycache__/` LAST, immediately before pushing — they REGENERATE on every gate run.**
They were removed once mid-session and eleven files were back after the next suite run.

**75/75 gates** (was 73) · `gate_payload_match` **PASS both ends** · `callout_id` **1125/0** ·
`keyterm_prefix` **0 to convert** · 16 banks valid, 1,241 questions · `quiz_bank --selftest`
**ALL 14 CONTROLS PASS** (was 8 — six `source_pins` controls Q–V added at S162 close) · census **40,889 unchanged** · retired-C1-slogan residue **0**.

**17 files changed** against `afdb91f`, verified by null-safe whole-tree md5 diff (446 tracked,
17 changed, 0 missing, 0 untracked):
`LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_SUPER_BIBLE.md` · `book_gates.py` · `newproject.html` ·
`quizzes/quiz_bank.py` · `lessons/Lesson_01/_03/_09/_11/_12/_13/_15.html` ·
`quizzes/ZUMO_QUIZ_L04/L05/L10/L11/L12.yaml`.

**`byte_audit --check` WAS NOT RUN AND DID NOT NEED TO BE** — no payload changed except two
comment blocks, comments emit no code, and three comment lines went in for three out so the
`tok-` span census could not move. Run it at S163 open anyway.

---

# THE THREE THINGS TO CARRY OUT OF S162

## 1. C1 IS CLOSED, AND THE SECOND PREDICATE IS THE REUSABLE HALF.

Sweeping the **slogan vocabulary** of §16.31's retired column — rather than a TRIM-near-loop
window — **reached L15-08 at the first attempt**, the tagged instance that returned zero hits at
any window width. It also named **three sites no tag and no derived list carried**: L09's
*Lesson 6 Dividend* NOTE, `ZUMO_QUIZ_L10` B45's `why`, and L13's *same open-loop discipline*.

**The L11 count was right and its membership was wrong.** Read in full, §7C's eyebrow and
Challenge 3's template *describe a blind moment* rather than state the rule, while §8A.1's NOTE
carries **two** rule sentences. **The ruled scope line: the defect is a sentence that states the
RULE; a sentence that describes a moment is correct in context.**

`QUIZ_L11` was **×3, not ×2** — the third grades L11's Quick Reference table **by its exact
strings**, the `L08_B21` shape. `QUIZ_L12`'s three hits were **read and ruled not-a-defect**:
`turnDegreesGyro()` genuinely closes on HEADING. **Gate 74** holds the retired column book-wide
and **needs no exemption list**, which was measured, not assumed.

**B4 is re-premised, not re-planted (DJ ruling).** The plant constant-folds to 24,790,
byte-identical to the correct build, and that property has five prose homes plus a bank `why` —
both GPT replacement sabotages destroy it. **The displacement magnitude is deliberately unstated**
(DJ): direction is derivable, magnitude is a bench measurement. **BENCH ITEM: measure how far a
Zumo walks sideways over a 90° and a 180° gyro turn with TRIM applied to one motor.**

## 2. §16.25 SHIPPED, AND THE COUNT DID NOT FALL.

L01 still carries **15** A-Star occurrences while its **wrong-claim count went 5 → 0**, because
the new KEY TERM and BRAIN CHECK name A-Star deliberately in order to retire it — *"Your robot
does not contain an A-Star board."* **A count is not a defect count in either direction.**
L03 fell 10 → 2, both the asset filename.

**All six of L01's legitimate build-target sites and both of the Maker's are byte-untouched,
asserted BY NAME rather than by count.** `board = a-star32U4` is correct and must survive.

**L03's photograph already described itself correctly** — `alt` reads *Zumo 32U4 main board* where
its own caption read *A-Star 32U4 board*, so no reshoot is owed. **The filename
`L03_IMAGE_3-14_astar_board.jpg` is UNRULED and the caption now contradicts it in one sentence.**
Dropping the *(File: …)* clause was priced and rejected — **51 captions carry it** — and a rename
needs a deletion through GitHub Desktop, §24.17's recoverability carve-out. **Deferred past Sept 8 —
item 2 in `ZUMO_AFTER_LAUNCH.md`.**

**DJ RESTATED THE FIX BACK AS *"the A-Star Board with an ATmega32U4 chip"* AFTER IT SHIPPED.** That
is the old wrong claim, and it is the exact reading §16.25 exists to prevent — restated by the reader
who had just been shown the corrected text, which is the THIRD occurrence and the first one AFTER the
correction went live. **The book is correct as it stands; the open question is whether the KEY TERM
sits too deep in the page.** DJ ruled it **DEFERRED PAST SEPT 8** — see item 1 in
**`ZUMO_AFTER_LAUNCH.md`**, which is where the deferred queue now lives.

## 3. GATE 75 IS IN, AND THE PIN FIX IS 9 OF 57 BECAUSE THE SCOPING INSTRUMENT FAILED.

**Every stale pin resolved to the commit that held it — all 52, none unresolved.** But flagging
questions that share vocabulary with the text that moved returned **3,146 of ~3,400
question-instances**, naming **71 of 75 questions off a 30-sentence diff**. **A predicate that
returns nearly the whole population has measured nothing.** Banks and lessons share their entire
vocabulary by construction. **The honest cost of the remaining 48 is a READ → FIX → QUIZ arc per
lesson — one lesson at a time, and each one deletes its own backlog entries.**

**Four bumped on evidence, diff READ not inferred:** `lesson_04` v04.29.0 → v04.29.1 is two lines,
the version comment and S151's `<title>` em-dash. **A section-level "(none)" is a lead; the diff
is the answer.**

**The 48 are NAMED in `quiz_bank.UNREAD_PINS`, not counted.** New drift fails immediately, a
backlog pin bumped without its read fails, and **the list can only shrink**.

**CONTROL C2 KILLED THE FIRST DRAFT OF THAT BACKLOG** — keyed on the pinned version, so bumping a
pin made its own entry unfindable and the gate went silent on the very move the arm exists to
catch. **A backlog you can abandon by editing the thing it tracks is not a backlog.**

**SEVEN OF SIXTEEN BANKS DISAGREED WITH THEMSELVES ABOUT THEIR OWN LESSON** — header comment
against YAML pin — **in both directions**, six header-newer and L08 field-newer, so neither home
was reliably fresher. **Ruled: `source:` = verified-against, gated. `# Authored against:` =
history, ungated, never rewritten (rule 37).**

---

# WHAT THE TRIPLE CHECK ESTABLISHED (properties — do not re-derive)

**ARM 3 IS BLIND TO A SECOND EDIT AFTER A BUMP.** Proved by seeding an unbumped L09 prose change
that delta closure could not see, because the version had already moved earlier in the session —
**S146's middle-of-chain blindness in a new place: the endpoints agree and the middle is
unguarded.** **ARM 4 closes it** — content hashes sealed at version-final state and re-compared
immediately before push. **Seal ARM 4 in every future session.**

**AN INSTRUMENT CAN BE BROKEN IN A WAY ONLY ABSURDITY REVEALS.** ARM 1's first run reported **37
missing files that all exist** — the shell loop word-split on filenames containing spaces
(`ChatGPT Image Jul 21, 2026, … .png`). Nothing checked it; the result was simply too silly to be
true. **Walk files with `git ls-files -z`, never a bare `for f in $(…)`.**

**A CONTROL HARNESS THAT TIMES OUT LEAVES ITS INJECTION ON DISK, AND THE OBVIOUS PROBE IS BLIND TO
IT.** S162's batched harness died mid-run holding the **blinding** control's reword. **The
retired-phrasing probe returned ZERO on that contaminated tree** — a blinding control contains no
slogan by construction, so the instrument that normally confirms cleanliness could not see this
contamination. **Only md5 against the pre-control record showed it.** One control per invocation,
each with an explicit timeout.

**A HAND-REORDERED GENERATED LIST GREW A DUPLICATE, AND THE COUNT WAS TAKEN FROM THE TYPING.**
The S162 push manifest was generated correctly at 19 files (17 changed + 2 new), then reordered by
hand in the chat message to put `quiz_bank.py` near the top — leaving the generator's original line
at the bottom, so the file appeared TWICE with the same digest and the count was read off the LINES
as **20**. Every digest was right; only the count and the ordering were hand-work. **Third instance
of this shape in one session** — S161's hand-enumerated banks, §24.16's retyped checksums, and this.
**Paste the generator's output; do not rearrange it.** DJ caught it by reading the numbers.

**A WRONG CLAIM WAS PRINTED BESIDE A NUMBER THAT CONTRADICTED IT.** A `print` asserted *"matches
the independent census of 52"* while the value beside it read **16** — `load()` returns
`(data, error)` and had been unpacked as `(src, data)`. Caught in one turn because the number and
the claim were on the same line. **Put the derived number next to the claim about it.**

**§27.16 CAUGHT ONE OF S162's OWN EDITS** — an `&rsquo;` where the literal is visible in source.

---

# S163 NEXT

- **THE 48 UNREAD PINS, ONE LESSON AT A TIME.** Each READ → FIX → QUIZ arc bumps that lesson's own
  pin and deletes its `UNREAD_PINS` entries **in the same commit** — gate 75 fails if they
  separate. **L16 is the worst (152 moved sentences) and L02 the cheapest (7).** Start cheap: L02's
  two entries, then L04/L05.
- **`ZUMO_QUIZ_L03`'s header comment** narrates *"hand-tuning vs closed loop"* as an asked topic;
  L03 now says *manual iterative tuning*. Prose narration, not a graded claim — **read and left**,
  but it should move when L03's bank is next touched.
- **L12 BONUS B4's bench measurement** (above) — the reveal deliberately states no number.
- **`ZUMO_AFTER_LAUNCH.md` IS NEW AT S162 AND IS THE DEFERRED QUEUE'S FIRST DURABLE HOME.** Before
  it, the queue lived only in the handoff (S41 and S52 carried `STILL PARKED`) and **this handoff's
  first draft dropped it entirely** — a record whose only home is a document the next session
  overwrites is not a record. **It is NOT yet complete:** absence from it does not mean an item was
  finished, and migrating the pre-S162 items into it is item 3 on its own list. **Read it at every
  session open alongside this handoff.**
- **ARM 2 IS BLIND TO A FIGURE STATED IN PROSE** (S159's stated blind spot, still unbuilt): §7C
  states its match-mode figure in prose rather than in a COMPILE CHECK, and **L16 never states its
  match-mode figure at all** — 28,504 lives in the Maker, the Bible and LIVE.md and appears nowhere
  in `Lesson_16.html`.
- **THE MAKER CHANGELOG STILL RECORDS NOTHING BETWEEN v2.49 AND v2.58** — eight releases. S162 wrote
  a **v2.58.4** entry; the eight remain deliberately un-back-filled.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment
  reading *"Negative = left"* — **survived S162 untouched. Keep it that way.**
- **L15 Challenge 3 reads differently now** (S158, unchanged): it asks the student to invent
  `turnDegreesGyroSafe()`, which is what the book's own turns now do. Failure mode is a TIMEOUT,
  distinct from the kill switch, so it still teaches something. Recorded, not ruled.
- **Remaining GPT worklist** — 245 findings, most unadjudicated. **L13-05** (wall/victim classifier
  presented as definitive) and **L13-11** (byte-match the quoted `readCalibrated()` against the
  bundled QTR in `Zumo32U4@2.0.1` — marked VERIFY, cheap and important) remain the strongest.
- L03 queued content (ms unit, modulo explainer, Coach's Tips) · `ZUMO_L03_TEMPLATES.md` staging ·
  Bible §14 TDP-canon entry · day-by-day period grid + syllabus.
- **L16 byte ceiling:** finished build 28,726 B vs 28,672 B; the Ziegler–Nichols trade (−162 B) was
  S158's ruled fix. **Verify it is reflected in the live repo.**
- **The poster is a GRADED deliverable** (DJ, S159), folded into the existing 25% row.
- **Photography is OFF the critical path** (DJ, S156).
- **Fall launch Sept 8** — three weeks out.

---

# HARNESS — IT IS NOT IN THE REPO, REBUILD IT

```
apt-get install -y gcc-avr avr-libc binutils-avr     # no sudo on this box
```
Clone FLAT into `/home/claude/harness` (read `LIBDIRS` out of the script, never from a handoff):
the eight Pololu repos plus `ArduinoCore-avr`, with `zumo-32u4-arduino-library` at
`--branch 2.0.1`. **`ArduinoCore-avr` goes at the TOP LEVEL of `/home/claude/harness`, not under
an `arduino/` subdirectory** — the script builds its includes as `$H/ArduinoCore-avr/...`, and
cloning it one level down yields `objects: 4` and every payload FAILing. Correct setup prints
**`objects: 41`**. Copy `pio_harness.sh` INTO the harness dir, then `bash pio_harness.sh --setup`.
`shim.cpp` is referenced and does not exist; the `[ -f ]` guard makes it optional.
Run `byte_audit.py --sizes` before `--check`.

**CONTROLS, carried from S160 and NOT re-derived at S161 or S162 (no payload code changed):**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,198** · `14/finished` **25,942** ·
`15/finished` **28,340** · `16/finished` **28,564**. **Reproduce the first one before trusting the
rest** (rule 30).

**To price a payload edit without touching the Maker:** `extract_project.py <maker> <lesson>
<kind> <outdir>` writes the resolved files; run `pio_harness.sh` on the dir.

---

# STANDING AUTHORITY — §24.17

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand
and course scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**S162's worked example of the disclosure half:** DJ asked for the 52 pins to be fixed. **The
measurement said 48 of them cannot be fixed honestly in one session**, and the scoping instrument
built to make them cheap **failed by returning the whole population.** Reporting that — rather
than bumping 48 pins and asserting 3,146 reads — is what keeps the provenance record worth
anything. **A gate plus a named backlog is a real answer to a request that cannot be met as
stated.**

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`afdb91f`**. Census **40,889**.
Bible **v8.154.1** · `BookComponentStandard` **v01.13.0** · Maker **v2.58.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.69.0** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.6** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.26.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.3.2** ·
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
`quiz_bank` **v1.4.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.29.0 · L02 v03.21.4 · L03 v03.43.0 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.3 · L07 v04.31.4 · L08 v04.32.0 · L09 v05.27.2 · L10 v02.30.2 · L11 v02.31.0 · L12 v01.33.0 · L13 v02.31.2 · L14 v02.35.0 · L15 v02.31.5 · L16 v02.26.1.

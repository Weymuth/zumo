# ZUMO — S173 HANDOFF (written at S172 close · paste at top of Session 173)

## READ THIS FIRST

**S172's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S172_HANDOFF.md` is part of that push. **If `__pycache__/` exists in your tree,
delete it LAST, immediately before pushing** — it REGENERATES on every gate run.

**77/77 gates** · `gate_payload_match` **PASS** · **`byte_audit --check` PASS across EIGHT arms,
`--selftest` ALL CONTROLS PASS** · `quiz_bank --selftest` all controls, **1,246** questions ·
`session_versions --selftest` EIGHT CONTROLS · **`session_versions --currency` NEW, exit 0** ·
`callout_id` **1127/0** · census **40,993** · `site_parity` PARITY · `build_css --check` current ·
`image_audit --check` current · `next_pointer` clean.

**RUN `--currency` AT SESSION CLOSE, BEFORE THE MANIFEST. It is new and it exists because it
caught a real defect that had already reached DJ's hands.**

---

# 1. AGREEMENT IS NOT CURRENCY — THE NEW ARM AND WHY IT EXISTS

**Two Maker payloads were edited this session and the Maker was never bumped.** LIVE.md, the
handoff and `newproject.html` all read **v2.61**, so they AGREED — perfectly, and wrongly — and
`session_versions --check` reported nothing, because it checks that documents agree with files,
never that a CHANGED file's version MOVED. Two different `newproject.html` files would have shipped
claiming one version, **the second after the first was already downloaded and pushed** (§5).

`session_versions --currency` (**v1.29.1**) asserts, for every file differing from **git HEAD**,
that its version home moved. **The predicate is the work tree against HEAD, not a fresh clone: a
clone needs a network and a gate must run without one.** Files with no version home are REPORTED
and never asserted — `css/book.css` is generated and `ZUMO_AFTER_LAUNCH.md` carries no version by
design, and **an arm that failed on those would be switched off inside a session.**

Controlled on the exact defect: version rolled back with the file changed → **LOUD, exit 1**;
restored → silent, exit 0, md5-exact. **AND ITS FIRST DRAFT REPRODUCED `grep_trap`'s OWN FINDING INSIDE THE INSTRUMENT
BUILT TO PREVENT IT:** homes keyed by first-regex-to-match read the Bible's own change as an unbumped
MAKER at v2.45.1, because `ZUMO_SUPER_BIBLE.md` QUOTES the Maker's version comment in its prose about
the convention. **Homes are keyed by PATH now**, controlled on the Bible and the Maker separately.

---

# 2. `gate_payload_match` IS ONE-DIRECTIONAL — MEASURED, WITH A WORKING REPRODUCTION

A blinding control removed one guard from the **PAYLOAD only** → **PASS**. The same guard removed
from the **LESSON only** → **PASS**. The gate proves every payload line DERIVES FROM the lesson,
and **a subset satisfies that in both directions**.

**So a challenge whose printed reveal and whose downloaded code disagree is caught by nothing** —
and that is the exact coupling S172's own edit rests on. Not widened here: it is a design change
needing its own controls, three weeks from launch. **Reproduction:** guard one line in
`13/challenge_9_1_keep_sweeping`'s payload out of the Maker, leave `Lesson_13.html` alone, run the
gate. It passes.

---

# 3. WHAT S172 DID

**S167's `-Wunused-result` half is MEASURED** — the attribute injected on every `StopReason`
declaration at EXTRACT time, all 216 payloads compiled, **no repo edit to find out** (rule 34).
147 carry the header; **23 discards over 9 payloads, ZERO in any `finished` build.**

**SEVEN ARE CORRECT BY DESIGN AND WERE LEFT ALONE:** `13/after_step_5` and `13/after_step_6` ARE
the blind corner Step 6b fixes; three L12/L13 ladder rungs are bare maneuvers; and **L11's two
challenge solutions discard in a lesson that has not taught the guard contract — correct for where
the STUDENT is, resolving on their own at L13.**

**TWO WERE NOT, AND THE DEFECT WAS IN THE TEMPLATE.** L13's Challenge 1 and Challenge 3 each ship a
four-move step-around discarding all four returns — twelve lines after the section that retired
that defect. The card hands the student those moves **pre-written** and says *Fill the two blanks*,
so the discards are **scaffolding the book supplies and instructs them to accept**; a student who
noticed and guarded them would be departing from the printed template. Guarded in four places —
both templates, both solutions — plus the payloads. **Blanks and difficulty pills unchanged.**

**THE TRIPLE CHECK NEARLY BOUGHT A WRONG FIX.** Step 6b's bare-`break` shape looked like it would
replay the celebration forever inside `VICTIM_FOUND`. `killSwitchPressed()` sets the state and
paints the screen ITSELF, and `driveDistance`/`turnDegreesGyro` both call it — only `driveUntil()`
polls the button and leaves the bookkeeping to its caller. **`L13_A42` already teaches exactly
this. The ruling existed and had not been read.**

**ARM 7's SKIP LIST WAS A POPULATION NOBODY HAD READ.** *N conditional skipped* had printed since
S169: **seven skipped, one genuinely conditional.** A YAML option ends with a quote and a newline,
not a full stop, so a run of options concatenated into one *sentence* and a distant `would`
silenced six live assertions — **correct by luck, not by assertion (rule 59).** Narrowed to the
claim's own OPTION: **7 → 3 skipped, 15 → 19 checked**, controlled both ways.

**THE BANK PIN ARC REFUTED ITS OWN PREMISE.** S171's suspect figures (`20,516`, `25,942`, `25,886`,
`25,816`, `25,202`) are **not one of them in a question body** — all in the `#` provenance header,
verified by two predicates. Reading the bodies then found `L13_A16`'s **CORRECT ANSWER was 456
where the live lesson says 458**, and a `240` distractor stale since S168. **Blinding control: with
456 restored, every instrument was GREEN.** `L13_A43b` NEW, grading S171's `case SWEEP_DONE:`.

**`26,790` → `26,798`** — S169's synthetic buzzer figure moved when S171 moved `16/finished` +8.
Measured: finished minus twelve `playNote()` lines weighs 26,798, so the buzzer still costs 1,828.

---

# 4. S173 OPENS HERE

- **MARK THE `StopReason` DECLARATIONS `warn_unused_result`.** The ordering is now satisfied — the
  book is at NINE discards over SEVEN payloads, every one explained, so the flag adds **no noise to
  any finished build**. It is a `RobotMotion.h` edit reaching **147 payloads** and needs its own
  recompile-and-verify pass; it costs **zero bytes** (measured: `13/finished` is 25,248 either way).
  Then the arm.
- **`gate_payload_match`'s one-directionality** (above) — a ruling, then a design.
- **ARM 7's two remaining false skips** are stated blind spots, not bugs. `would` is ordinary
  English and no windowing separates it from the claim's own string.
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE** — three prose figures were found by
  READING this session, not by an instrument.
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166).
- **`strip_inline --restore` DOES NOT RESPECT THE HELD LESSON STRIP** (S168). SCRATCH-COPY works.
- **`build_css.py --help` IS NOT A FLAG — IT RUNS AND WRITES THE STYLESHEET** (S169).
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165). When it first fires, the answer is a ruling.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated.
- L12 BONUS B4's bench measurement · L15 Challenge 3's `turnDegreesGyroSafe()` · L03 queued content ·
  `ZUMO_L03_TEMPLATES.md` staging · Bible §14 TDP-canon entry · day-by-day grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path** (S156).
- **Fall launch Sept 8. L13 is the last in-scope lesson and it is whole.**

---

# HARNESS — IT IS NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc     # foreground; the box has no toolchain
sh harness_setup.sh                     # prints objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~3 min
python3 byte_audit.py --selftest        # before trusting --check
python3 byte_audit.py --check           # EIGHT arms
```

**CONTROLS — FOUR UNMOVED, FOUR MOVED BY S171'S FIX, ALL RE-VERIFIED AT S172:**
`11/after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,248** · `14/finished` **26,002** ·
`15/finished` **28,406** · `16/finished` **28,626**.
**Reproduce 20,592 before trusting the rest** (rule 30).

**216 payloads, FOUR declared overflows** — `16/after_step_3` **29,008** · `16/after_step_4`
**29,644** · `16/step_5_serial_traded` **28,944** · `16/step_5_zn_traded` **28,788**.

**THE TIGHTEST PASSING BUILD IS `16/after_step_2` AT 28,648, WITH 24 BYTES SPARE.**

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo; and RoboLore brand and course scope.
**Delegation removes the question, never the disclosure.**

**§24.19 IS THE TIEBREAKER.** S172's worked example: an unguarded step-around could have been
reframed as a deliberate trap. It was not, because **this book already has a home for planted bugs
and an unlabelled trap inside a SOLUTION destroys the distinction that makes the labelled ones
teach.**

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`d1204fe`**. Census **40,993**.
Bible **v8.165** · `BookComponentStandard` **v01.13.0** · Maker **v2.62** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.5** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.6.1** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.29.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.8** ·
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
`harness_setup.sh` **v1.1** ·
`pio_harness.sh` **v3.1** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.30.1 · L02 v03.21.5 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.35.0 · L14 v02.36.0 · L15 v02.32.0 · L16 v02.28.0.

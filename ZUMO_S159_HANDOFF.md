# ZUMO — S159 HANDOFF (written at S158 close · paste at top of Session 159)

## READ THIS FIRST

**S158's work WAS DELIVERED AT S158 CLOSE AND DJ VERIFIES THE PUSH HIMSELF (ruling S158).**
Twenty-one files, `md5sum` output published in chat. `git rm ZUMO_S158_HANDOFF.md` is part of that push.

**S158's work IS PUSHABLE.** 73/73 gates · `gate_payload_match` **PASS** · `byte_audit --check` **PASS**
· `callout_id` 1125/0 · 16 banks valid. **THE OPTION-C ROLLOUT IS COMPLETE.**

Files changed against the pushed clone (`e43be7a`), verified by fresh-clone diff:
`lessons/Lesson_11.html` · `Lesson_12.html` · `Lesson_13.html` · `Lesson_14.html` · `Lesson_15.html` ·
`Lesson_16.html` · `newproject.html` · `css/book.css` · `images/L16_GRAPHIC_16-02_the_wall.svg` ·
`book_gates.py` · `build_family_map.py` · `quizzes/ZUMO_QUIZ_L11..L16.yaml` (six banks) ·
`ZUMO_SUPER_BIBLE.md` · `LIVE_ZUMO_TEXTBOOK.md`. **L01–L10 are untouched.**
Delete `__pycache__/` and `quizzes/__pycache__/` before pushing — they are not in the repo.

---

# THE ONE THING TO CARRY OUT OF S158

**LESSON 13 INVENTED `StopReason`, AND THE ROLLOUT BACK-PORTED IT TO LESSON 10.**

L13 Step 1 has always shipped `enum StopReason { STOP_DISTANCE, STOP_PROX, STOP_KILL }`, has always
included `RobotConfig.h` from `RobotMotion.h` for it, and its `driveUntil()` has always polled the
button and reported why the leg ended. **That is option C, three lessons before option C had a name.**

**RULED S158: Lesson 10 OWNS the enum. Lesson 13 ADDS `STOP_PROX`.** L13's Step 1 now extends a
contract instead of declaring one; Step 4's *"one include it never needed before"* now says the line
arrived at Lesson 10. Rejected: shipping all three values from L10, which prints a value L10 cannot
explain — §16.26 inverted. **This is reversible but gets more expensive every session.** If it is ever
revisited, the alternative is renaming L10's enum (`MoveResult`) and giving L13 its name back.

---

# S158's OTHER RULINGS

**L16 STEP 5 HAS A THIRD TRADE (DJ ruling: *"make it a third trade"*).** The converted capstone measured
**28,726 — 54 over.** The conversion costs **+126**, not the handoff's projected +64; decomposed in L16
by reverting one piece at a time: guards **30** · encoder polls **28** · gyro poll **20** · report **6**
· plumbing **42**. Nothing can be dropped without deleting the safety the rollout adds.

Priced by deletion BEFORE the ruling (rule 70): WEAVE display row −64 (10 spare) · BASE row −84 (30) ·
**WEAVE metric entirely −162 → 28,564, 108 spare.** Ruled the whole metric on the PROTOCOL: §7 scores
baseline against enhanced on **MAE and LAP** and has no WEAVE column, and **Lesson 15 keeps WEAVE**,
so the TDP's A4 bench table is untouched. Trade 2 deletes the Ziegler–Nichols hint — the only code that
COMPUTED with WEAVE — which is what makes trade 3 cheap to argue.

**BOTH NEW L16 BLOCKS ARE PROSE, NOT CALLOUTS.** S148 already paid for this: a `THE WALL` callout fires
§5.1's frozen 5px border debt, and a new STILL GREEN moves §21, §24.14 and the family map.

---

# THE MEASURED CHAIN (re-derive; do not carry)

| lesson | finished | note |
|---|---|---|
| L10 | 20,592 | S157 |
| L11 | 20,778 | +186 unchanged · headroom 7,894 |
| L12 | 24,790 | +800 / +0 unchanged · **+3,192 → +3,212** |
| L13 | 25,198 | +180 / −42 unchanged · **+240 → +270** · total 408 |
| L14 | 25,942 | +744 / −36 / −740 all unchanged |
| L15 | 28,340 | +164 / +1,306 / +48 / +880 all unchanged · headroom **332** |
| L16 | 28,564 | 108 spare after three trades |

**EVERY "BYTE-IDENTICAL" SABOTAGE CLAIM SURVIVED**: L12 B4, L13 B2, L14 B2/B3/B4, L15 B1/B4, L16 B1/B2.

---

# WHAT THE TRIPLE CHECK FOUND (§24.13, six arms, three real misses)

1. **L16's finished-size table was stale for L14 and L15** — the L10–L13 rows had been fixed as the
   rollout went and the pass stopped there.
2. **The L14 bank was never re-keyed** — twelve live options.
3. **The L15 bank was never re-keyed** — seventeen live options, including headroom 458.

All fixed. **TWO OF THE SIX ARMS FAILED ON THEIR OWN PREDICATE BEFORE THE TREE:** one asserted a single
`StopReason driveDistance` where there are correctly two (declaration and definition), one omitted the
removed `void` forms from its vocabulary. **A check that fires on its author is doing its job.**

**THE ARM WORTH KEEPING** is the line-level one: every changed line in all 94 converted payloads (367
changed files) must match the conversion vocabulary. That is what proves no sabotage was lost, and it
is stronger than any spot check. **It is not in the repo** — rebuild it if a comparable sweep is ever run.

**THE DELTA-CLOSURE INSTRUMENT IS NOW `byte_audit` ARM 5** and it ships in the repo. S146 proved
endpoint agreement is blind to the middle; ARM 2 asserts figures, ARM 5 asserts the arithmetic
AROUND them — DELTA against the previous STEP, SPARE against `CEILING − fig`, OVER against
`fig − CEILING`. A wrong FIGURE fires it TWICE, on the deltas either side of the moved value.

---

# S159 NEXT

**PUSH VERIFICATION IS DJ'S, NOT THIS SESSION'S (DJ ruling S158).** S158's twenty-one files went up
under DJ's own hand and he checks the landing himself. **Do NOT open S159 by re-verifying the S158
push** — run the normal session-open ritual and take the first job. The standing rule that a matching
SHA is not proof content landed is unchanged; it is simply not this session's errand.

**FIRST JOB: C6.** Ruled S158, on cost rather than on weight: it is the queue's smallest item, it
needs no ruling of its own, and it clears before the largest one starts.

- **C6 — COMPETITION RULE vs ROBOLORE POLICY. ← START HERE.** 8 findings, one read of
  `RCJRescueLine2026-final.pdf`, which is in the repo root. **Read the PDF, not the extract** —
  §16.17's whole lesson is that a bare section number is undateable and can be coincidentally right,
  and `ROBOCUP_RESCUE_LINE_2026.md` was once convicted on an inference for exactly that reason.
- **C2 — SENSOR-AS-TRUTH LANGUAGE. RULED: ADOPT — SECOND.** *A sensor answers its own question, not
  yours.* L04–L13 prose plus the quiz re-keying it forces. **Still the strongest item in the review**,
  and the largest: budget it a session of its own rather than starting it behind C6 in the same one.
- **`byte_audit` ARM 5 — CLOSURE — IS BUILT AND GREEN** (`byte_audit` **v1.3.2**). 14 closure claims
  across L13–L16, six controls, blinding control silent, COVERAGE arm fails on a blind parser.
  **It found two of its own bugs before it found any of the book's**, the second only because a
  seeded control DID NOT FIRE. Nothing queued here.
- **C1 — TRIM justification backwards in L08** (practice correct, reason wrong; 2 occurrences).
- **C3 — kill switch for blocking loops: CLOSED.** L10–L16 all poll B in every primitive.
- **§16.25's BODY IS STALE BY ONE SESSION** (Bible ~line 2662, present tense about lowercase
  `a-star32u4`; S155 made and applied that ruling). DJ ruled: RECORD IT. Doc-only, minor bump.
- **A-Star hardware identity fix** in L01 and L03 prose (KEY TERM `term-a-star`) — GPT P0, confirmed
  defect per the S154 fleet ruling, not yet built.
- **L03's photograph `L03_IMAGE_3-14_astar_board.jpg`** names a board the robot does not contain. Unruled.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment reading
  *"Negative = left"* — **survived S158 intact and byte-identical. Keep it that way.**
- **L15 Challenge 3 reads differently now.** It asks the student to invent `turnDegreesGyroSafe()` that
  reports failure from a turn — which is what the book's own turns now do. Its failure mode is a
  TIMEOUT, distinct from the kill switch, so it still teaches something. Recorded, not ruled.
- L03 queued content (ms unit, modulo explainer, Coach's Tips) · `ZUMO_L03_TEMPLATES.md` staging ·
  TDP template v3 A5 Lab Log · Bible §14 TDP-canon entry · day-by-day period grid + syllabus.
- **Photography is OFF the critical path** (DJ, S156).

---

# HARNESS — IT IS NOT IN THE REPO, REBUILD IT

```
apt-get install -y gcc-avr avr-libc binutils-avr     # no sudo on this box
```
Clone FLAT into `/home/claude/harness` (read `LIBDIRS` out of the script, never from a handoff): the
eight Pololu repos plus `arduino/ArduinoCore-avr`, with `zumo-32u4-arduino-library` at `--branch 2.0.1`.
**Copy `pio_harness.sh` INTO `/home/claude/harness`.** `shim.cpp` is referenced and does not exist; the
`[ -f ]` guard makes it optional. Run `byte_audit.py --sizes` before `--selftest`.

**CONTROL: L11 `after_step_1` PRE-CONVERSION = 20,516.** Reproduced at S158 from an eighth clone.
`objects: 41`. **Post-conversion it is 20,592**, which is L10's converted `finished` — that identity is
the cheapest cross-check in the book.

---

# STANDING AUTHORITY — §24.17

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see; moves
that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand and course
scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`e43be7a`**. Census **40,840**.
Bible **v8.148** · `BookComponentStandard` **v01.13.0** · Maker **v2.57** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.68.5** · `lesson_inventory` **v1.3.5** ·
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
`quiz_bank` **v1.0.1** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.28.5 · L02 v03.21.3 · L03 v03.41.1 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.30.0 · L11 v02.30.1 · L12 v01.32.0 · L13 v02.30.0 · L14 v02.34.1 · L15 v02.31.3 · L16 v02.25.0.

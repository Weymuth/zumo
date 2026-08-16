# ZUMO — S160 HANDOFF (written at S159 close · paste at top of Session 160)

## READ THIS FIRST

**S159's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S159_HANDOFF.md` is part of that push. Delete `__pycache__/` and
`quizzes/__pycache__/` first — they are not in the repo.

73/73 gates · `gate_payload_match` **PASS** · `byte_audit --check` **PASS** ·
`callout_id` 1125/0 · 16 banks valid.

Files changed against the pushed clone (`6a89fe2`):
`lessons/Lesson_13.html` · `Lesson_14.html` · `Lesson_16.html` · `newproject.html` ·
`css/book.css` · `book_gates.py` · `quizzes/ZUMO_QUIZ_L14.yaml` · `quizzes/ZUMO_QUIZ_L16.yaml` ·
`ZUMO_SUPER_BIBLE.md` · `ZUMO_Syllabus_WORKING.md` · `ZUMO_TDP_Template_v3.md` ·
`LIVE_ZUMO_TEXTBOOK.md`. **L01–L12 and L15 lesson files are untouched.**

---

# THE ONE THING TO CARRY OUT OF S159

**THERE ARE TWO CALIBRATION ROUTINES IN THIS BOOK AND THE OBVIOUS SEARCH FINDS THE WRONG ONE.**

`calibrateSensors()` (L04, 2 definitions) is a HUMAN sweep — no motor call, legal everywhere.
`calibrateLineSensors()` (L08 onward, 139 definitions) SPINS the robot, and RCJ Rescue Line 2026
**§5.3.6** does not permit a robot to move on its own while calibrating. I measured the first one,
found it clean, and told DJ the code was compliant. It was the wrong function.

**Now guarded on `COMPETITION_MODE` in the 37 payloads that carry the switch** (L14 12 · L15 16 ·
L16 9). **The 102 L08–L13 payloads are deliberately UNCHANGED** — the spin is legal on a practice
floor and the switch is not born until L14. That split is the ruling, not drift; do not "finish" it.

The trailing `setSpeeds(0, 0)` is **deliberately unguarded.** Commanding a stop is not moving.

---

# THE MEASURED CHAIN (re-derive; do not carry)

| build | practice | match mode |
|---|---|---|
| L14 `finished` | 25,942 (unmoved) | 25,906 → **25,886** |
| L15 `finished` | 28,340 (unmoved) | — |
| L16 `finished` | 28,564 (unmoved, 108 spare) | 28,528 → **28,504** |

**The practice build is BYTE-IDENTICAL by disassembly**, not merely the same size. The blinding
control that proves the test is live: `-100` → `-99` MOVES the stripped instruction hash.

**A STATED BLIND SPOT:** `byte_audit` ARM 2 never saw the moved 7C figure, because §7C states it
in PROSE rather than in a COMPILE CHECK callout. Four homes carried 25,906 / 36 and **one was a
correct answer in the L14 bank.** If a future session moves a match-mode figure, ARM 2 will be
silent again. Extending ARM 2 to prose figures is unbuilt and unqueued — it is a real candidate.

---

# S160 NEXT

**FIRST JOB: C2 — SENSOR-AS-TRUTH LANGUAGE. RULED ADOPT (S158), and it wants a session of its own.**
*A sensor answers its own question, not yours.* L04–L13 prose plus the quiz re-keying it forces.
**Still the strongest item in the review and the largest.** Do not start it behind anything else.

- **C1 — TRIM justification backwards in L08** (practice correct, reason wrong; 2 occurrences).
  Small; a good warm-up before C2 if C2 will not fit.
- **C6 — CLOSED.** Nine findings, not the eight the queue carried (L16-09 and L16-17 are dual
  C4/C6). All nine confirmed against the PDF and shipped as prose labels.
- **C3 — CLOSED** (S158). L10–L16 all poll B in every primitive.
- **THE MAKER CHANGELOG RECORDS NOTHING BETWEEN v2.49 AND v2.58** — eight releases bumped on the
  version line with no entry. **Recorded, deliberately not back-filled**: reconstructing them from
  the Bible asserts a read that never happened. If DJ wants them, they come from the Bible entries
  with that provenance stated, not silently.
- **§16.25's BODY IS STALE BY ONE SESSION** (Bible ~line 2662, present tense about lowercase
  `a-star32u4`; S155 made and applied that ruling). DJ ruled: RECORD IT. Doc-only, minor bump.
- **A-Star hardware identity fix** in L01 and L03 prose (KEY TERM `term-a-star`) — GPT P0,
  confirmed defect per the S154 fleet ruling, not yet built.
- **L03's photograph `L03_IMAGE_3-14_astar_board.jpg`** names a board the robot does not contain.
  Unruled.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment
  reading *"Negative = left"* — **survived S159 intact. Keep it that way.**
- **L15 Challenge 3 reads differently now** (S158 note, unchanged): it asks the student to invent
  `turnDegreesGyroSafe()`, which is what the book's own turns now do. Its failure mode is a
  TIMEOUT, distinct from the kill switch, so it still teaches something. Recorded, not ruled.
- L03 queued content (ms unit, modulo explainer, Coach's Tips) · `ZUMO_L03_TEMPLATES.md` staging ·
  Bible §14 TDP-canon entry · day-by-day period grid.
- **The poster is now a GRADED deliverable** (DJ ruling S159), folded into the existing 25%
  *Engineering Notebook / TDP + Poster* row so no other weight moved. If milestone dates ever get
  pinned, the poster needs a due date with them.
- **Photography is OFF the critical path** (DJ, S156).

---

# HARNESS — IT IS NOT IN THE REPO, REBUILD IT

```
apt-get install -y gcc-avr avr-libc binutils-avr     # no sudo on this box
```
Clone FLAT into `/home/claude/harness` (read `LIBDIRS` out of the script, never from a handoff):
the eight Pololu repos plus `arduino/ArduinoCore-avr`, with `zumo-32u4-arduino-library` at
`--branch 2.0.1`. **Copy `pio_harness.sh` INTO `/home/claude/harness`**, then
`bash pio_harness.sh --setup`. `shim.cpp` is referenced and does not exist; the `[ -f ]` guard
makes it optional. Run `byte_audit.py --sizes` before `--check`.

**CONTROL: L11 `after_step_1` = 20,592**, which is L10's converted `finished` — reproduced at S159
from a fresh clone. `objects: 41`. Cheapest cross-check in the book.

**To price a payload edit without touching the Maker:** `extract_project.materialize()` gives you
the resolved files, patch the string in memory, write to a temp dir with `byte_audit.head_includes()`
prepended to `main.cpp`, and run `pio_harness.sh` on the dir. That is how the +372 design was killed
before it shipped.

---

# STANDING AUTHORITY — §24.17

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand
and course scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**S159's worked example of the disclosure half:** I reported option A as *procedure only, likely
zero bytes*, DJ ruled it, and the compiler then said it was unshippable. Reporting the measurement
alongside the decision is what made that reversible in one turn instead of shipping.

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`6a89fe2`**. Census **40,878**.
Bible **v8.149** · `BookComponentStandard` **v01.13.0** · Maker **v2.58** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.68.6** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.28.5 · L02 v03.21.3 · L03 v03.41.1 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.30.0 · L11 v02.30.1 · L12 v01.32.0 · L13 v02.31.0 · L14 v02.35.0 · L15 v02.31.3 · L16 v02.26.0.

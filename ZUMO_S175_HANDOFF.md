# ZUMO — S175 HANDOFF (written at S174 close · paste at top of Session 175)

## READ THIS FIRST

**S174's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S174_HANDOFF.md` is part of that push. **If `__pycache__/` exists in your tree,
delete it LAST, immediately before pushing** — it REGENERATES on every gate run.

**77/77 gates** · `gate_payload_match` **PASS** · `quiz_bank --selftest` all controls, **1,246**
questions · `session_versions --selftest` EIGHT CONTROLS · `--currency` exit 0 ·
`build_css --check` current at 574 rules · `image_audit --check` current ·
**`build_worklist --check` current — NEW THIS SESSION** · `callout_id` **1127/0** ·
census **40,993** · `next_pointer` clean.

**S174 TOUCHED NO LESSON, NO BANK, NO GATE AND NO PAYLOAD.** Four instruments and three
generated files. `byte_audit` was NOT run — the box had no AVR toolchain and nothing this
session moved a byte. **The eight standing byte controls are therefore UNVERIFIED SINCE S172
and must be reproduced before any byte claim is trusted (rule 30).**

---

# 1. §24.20 — AN UNRECOGNIZED ARGUMENT MUST NOT BE A WRITE

The S169 lead said *`build_css.py --help` is not a flag — it runs and writes the stylesheet.*
**The lead named one tool and one argument and the predicate is neither.** The dispatch is
`--selftest` → exit, build, `--check` → exit, **else WRITE** — the write is the FALL-THROUGH,
so `--help`, `--dry-run` and **a typo of `--check`** are indistinguishable from a bare run.

**MEASURED EMPIRICALLY, NOT BY READING argv (rule 34):** all 36 instruments handed an
unrecognized argument in their OWN pristine copy of the tree, no run able to see another's
state (S170).

**THE FIRST PROBE MEASURED THE WRONG PROPERTY AND REPORTED `build_css` CLEAN.** It hashed
CONTENT; `css/book.css` is normally current, so the tool rewrote **identical bytes** and the
hash saw nothing — **a byte-identical result never proves an edit did not land.** Re-predicated
on `(inode, mtime, size, content)` because `os.replace` swaps the inode: **3 of 36, not 1.**

`build_css.py`, `image_audit.py` and `build_worklist.py` now refuse an unrecognized argument
with **exit 2** and carry a real `--help`. **Post-fix population: 0 of 36.**

---

# 2. THE REAL FINDING — `GPT_WORKLIST.md` WAS STALE AND NOTHING COULD SEE IT

Header stamped `svg_layout_audit v1.19` against a live **v1.20**; body claiming **36 files
needing a human where the audit finds 38.** Missing from the backlog **entirely**:
`L11_GRAPHIC_11-05_battery_strength_changes_the_outcome.svg` and
`L13_GRAPHIC_13-03_the_line_was_doing_three_jobs.svg`. `L10_GRAPHIC_10-02`'s marker count read
**3 against a live 2**.

**The graphics chat works from this file**, so two real defects were invisible to the person
whose whole job is to fix them — and the file's own second line says *Do not hand-edit —
regenerate.*

**WHY IT ROTTED IS STRUCTURAL: IT WAS THE ONE GENERATED ARTEFACT WITH NEITHER A `--check` NOR A
GATE.** `css/book.css` has both; `IMAGE_WORKLIST.md` has both; `GPT_WORKLIST.md` had **zero
mentions in `book_gates.py`**. A generated file whose only relation to its generator is that
somebody remembers to re-run it is not generated, it is **transcribed** — v1.0's own opening
argument about the hand-assembled `GPT_WORKLIST_S99.md`, committed by its successor.

`build_worklist` **v1.2** gains `--check`, and **it fired on the exact defect it was built for
on its first run**, exit 1 against the committed file. Regenerated: **38 files, 9 local-fix
findings across 5 files.**

**THE SESSION STAMP WAS A PINNED LITERAL (rule 19).** `session = '102'` — hardcoded, **two
sessions older than the v1.1 that shipped it** — so every regeneration without `--session N`
stamped a passed session, and regenerating the live file made the stamp go **BACKWARDS**,
S103 → S102. **That defeats v1.1's entire ruling**, which moved the stamp INTO the file so a
stale copy could not look current; a pinned default makes a FRESH copy look stale instead.
Now `session_versions.current_session()` — **one definition, two readers (rules 83/84)**,
factored out of `session_numbers()`'s own inline regex, imported not re-implemented, raising
rather than guessing. **It stamped S174 on its own.**

---

# 3. A COUPLING THAT WAS NOT PRICED, AND THE GATES CAUGHT IT

**`css/book.css` and `IMAGE_WORKLIST.md` each stamp their GENERATOR's version in a header
line.** Bumping `build_css` v1.3.0 → **v1.4.0** and `image_audit` v1.2 → **v1.3** made both
generated files stale by exactly one line and took the suite to **75/77** — §27.13 and §10
firing.

**Measured rather than feared: the whole cascade is one comment line each.** Rules and
declarations UNCHANGED at **574/2,033**, §27.11's digest unmoved, no class set change, so
**§27.8b's restore→regenerate→apply cycle was NOT owed** and no lesson file moved. Regenerated;
77/77 restored.

**THE RULE THAT FALLS OUT: a generator's version bump is a regeneration obligation, because the
artefact carries the generator's version.** Expect this again on the next `build_css` or
`image_audit` bump.

---

# 4. THE CONTROL FAILED THE MOMENT THE DEFECT WAS FIXED — THIRD OCCURRENCE

The probe's control anchored on `build_css.py` as a KNOWN writer, read out of its own dispatch.
**That is a fixture borrowed from the population being audited**, so with the population emptied
the probe refused to report.

**A control whose fixture is borrowed from the population it audits fails when you SUCCEED** —
S166's `_good_bank()`, S171's `FINISHED_WARN_BASELINE`, and now here, **inside the instrument
written to find the defect.** Rebuilt to PLANT its own synthetic writer whose write is the
fall-through and whose bytes are identical either way, asserting both that the rewrite is seen
AND that it was same-byte, so the control proves the predicate is **writes and not content** and
tests the ARM rather than the state of the tree.

---

# 5. S175 OPENS HERE

- **A GATE FOR `GPT_WORKLIST.md` IS OWED AND WAS PRICED, NOT SHIPPED.** `--check` closes what a
  session ritual can reach; a gate costs an `svg_layout_audit` pass over every SVG on **every**
  `book_gates` run, and **an arm that made the routine slower is one somebody eventually skips**
  (S170's reason for CONTROL K, S173's for ARM 9). If it ships, it likely belongs behind the same
  door ARM 9 uses rather than in `--check`'s path.
- **EIGHT INSTRUMENTS DIE ON AN UNRECOGNIZED ARGUMENT WITH A RAW TRACEBACK** —
  `build_mark_index` reads it as a directory, `gate_payload_match` as a filename, `pill_sweep` as
  an `IndexError`, plus `extract_project`, `fit_raster_svg`, `flatten_alpha`, `gen_component`,
  `glyph_scan`. **They are ugly and they are SAFE: none of them writes.** Refusal was the
  property that mattered. Cosmetic, not owed.
- **`byte_audit` HAS NOT RUN SINCE S172.** Install the toolchain and reproduce
  `11/after_step_1` **20,592** FIRST (rule 30) before trusting any figure.
- **THE `NINE` vs `15` DISCREPANCY IS OPEN AND IS A LEAD, NOT A FINDING.** Bible v8.165 says the
  book stands at *NINE over SEVEN*; ARM 9 measures **15 over 7**. Payload count agrees, discard
  count does not. It reads like the pre-fix payload count transposed into the discard slot, but
  that is arithmetic on documents and not a compile. **`byte_audit --discards` settles it.**
- **S167's DEBT IS CLOSED AND MUST NOT BE RE-OPENED** (Bible §16.43). The stale forward
  instruction in LIVE.md that said otherwise was **struck at S174**.
- **`gate_payload_match`'s one-directionality** (S173) — a ruling, then a design. Reproduction:
  guard one line in `13/challenge_9_1_keep_sweeping`'s payload out of the Maker, leave
  `Lesson_13.html` alone, run the gate. It passes.
- **ARM 7's two remaining false skips** are stated blind spots, not bugs.
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE.**
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166).
- **`strip_inline --restore` DOES NOT RESPECT THE HELD LESSON STRIP** (S168). SCRATCH-COPY works.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165). When it first fires, the answer is a ruling.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated. **Two of its SVG entries are
  newly visible as of this session's regeneration** (see §2).
- L13/L14 bank pin arcs · L12 BONUS B4's bench measurement · L15 Challenge 3's
  `turnDegreesGyroSafe()` · L03 queued content · `ZUMO_L03_TEMPLATES.md` staging ·
  Bible §14 TDP-canon entry · day-by-day grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path**
  (S156).
- **Fall launch Sept 8. L13 is the last in-scope lesson and it is whole.**

---

# HARNESS — IT IS NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc     # foreground; the box has no toolchain
sh harness_setup.sh                     # prints objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~3 min
python3 byte_audit.py --selftest        # before trusting --check
python3 byte_audit.py --check           # EIGHT arms
python3 byte_audit.py --discards        # ARM 9, ~3 min, NOT in --check's path
```

**STANDING CONTROLS, LAST VERIFIED S172 — REPRODUCE 20,592 FIRST (rule 30):**
`11/after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,248** · `14/finished` **26,002** ·
`15/finished` **28,406** · `16/finished` **28,626**.

**216 payloads, FOUR declared overflows** — `16/after_step_3` **29,008** · `16/after_step_4`
**29,644** · `16/step_5_serial_traded` **28,944** · `16/step_5_zn_traded` **28,788**.

**THE TIGHTEST PASSING BUILD IS `16/after_step_2` AT 28,648, WITH 24 BYTES SPARE.**

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo; and RoboLore brand and course scope.
**Delegation removes the question, never the disclosure.**

**§24.19 IS THE TIEBREAKER** — what is best for student learning, when nothing else discriminates.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`fb8e6e5`**. Census **40,993**.
Bible **v8.168** · `BookComponentStandard` **v01.13.0** · Maker **v2.62** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.5** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.6.1** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.30.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.2** ·
`build_css` **v1.4.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.9.1** ·
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

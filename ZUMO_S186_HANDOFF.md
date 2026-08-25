# ZUMO — S186 HANDOFF (written at S185 close · paste at top of Session 186)

## READ THIS FIRST

**S185's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S185_HANDOFF.md` is part of that push. If `__pycache__/` exists, delete it LAST —
it regenerates on every gate run.

**S185 OPENED ON A HALF-LANDED PUSH AND THAT IS THE FIRST THING TO CHECK AT S186.** The tree at
session open carried S184's NEW files (`prose_canon.py`, `ZUMO_FIX_TRACKER.md`, this handoff's
predecessor) and **none of S184's MODIFIED files** — Bible, `book_gates`, `session_versions`, Maker,
L01–L03. LIVE.md was correct and the handoff was the stale document, which inverts the usual case.
**`session_versions --check` is what named it, 23 disagreements.** Run the open ritual against the
FILES, never against this document.

**79/79 gates** · `gate_payload_match` **PASS**, advisory unmoved at **635** ·
`prose_canon` **0 new / 7 pinned / 0 orphan**, `--selftest` **ALL 15 CONTROLS** ·
`quiz_bank --check` **16 banks valid** · `callout_id` **1133/0** · `strip_inline --verify` **0 dead** ·
`build_css` **574 rules** · `session_versions --currency` **0 unbumped** · `build_worklist --check` current.
**`byte_audit` IS OWED NOTHING: the Maker edit is comment-only, no payload changed, no executable line moved.**

**PAGES BUILD FLOOR IS 10m57s (run #944).** `site_parity` was run 3 minutes after DJ's push and printed
PARITY — **that reading was discarded, not banked.** Inside the build window a PASS can be the OLD site
agreeing with itself. Re-run past the floor at S186 open.

---

# 1. WHAT S185 DID — L03's LAST TWO ROWS, AND A THIRD FIND UNDER THEM

**`ZUMO_GPT_REVIEW_WORKLIST.md` IS NOW v1.5: 59 CLOSED, 2 PARKED, 184 OPEN. L01, L02 AND L03 ARE DONE.**

## §16.51 — A ROW IS FILED AGAINST ONE LESSON; THE CLAIM CAN LIVE IN FOUR FILES

`L03-10` named four L03 sites. **The claim class was NINE across four artefacts** — L03 ×4, **L01 ×2**,
**Maker ×2** (L01 c11's boxed header), and **`QUIZ_L03` B18, where the retired claim was the KEYED
CORRECT ANSWER.** A student answering from the corrected lesson was marked wrong (v8.130, third time).

**Part 0b read L01 and L02 at 0 OPEN throughout, because it counts ROWS and not claim sites.** The
caveat is now in the worklist header. **A lesson at 0 OPEN has no rows of its own left — not no defects.**

**The claim is false, checked before editing.** 4,200 ÷ 4 = 1.05 V/cell against a ~1.0 V/cell cutoff;
the real mechanism is **cell reversal in a series pack**. Policy right, reason wrong — `L02-13`'s shape.
Retired claim reused as B18's distractor. **L01 C11's 4,500 split untouched** (`ZUMO_FIX_TRACKER.md` §5).

## `L03-07` — RETRIEVAL, NOT REPETITION

§3.25 re-ran L01 Challenge 6's scatter from scratch, in a book where **C6 says keep those numbers FOR
LESSON 3.** Now retrieval. **No comparative magnitude asserted** — scatter vs condition-shift is unmeasured.

## `L03-09` WAS RECORDED CLOSED AND WAS NOT

SHIPPED at S179 per Part 0; the ±10% figure **survived in L03's Quick Reference**, contradicting
`L03_B35`'s keyed answer for six sessions. Now 0 book-wide. **Found by reading the bank, not the lesson.**

---

# 2. S186 OPENS HERE

**THE GPT LIST IS STILL THE ASSIGNMENT. DJ: *"I can't ship a book with errors in it."***
**DJ's S182 scope ruling stands: L01–L08 before L13–L16.** L01–L03 are done; **L04 is next, 5 rows.**

## THE OBVIOUS NEXT MOVES
1. **L04–L08 sweep.** L04 ×5 · L05 ×2 · L06 ×7 · L07 ×10 · L08 ×14. **This also closes the 7 pinned
   `prose_canon` residue sites** — the three L05/L06 lesson headings and the four Maker labels are
   **ONE fix, not two**: a step title and the row that opens it move together.
2. **`prose_canon` arms 1, 2 and 4** — still unbuilt, still guarding nothing.
   **Do not ship an arm without a control per direction (§16.50).**
3. **ENUMERATE THE CLAIM, NOT THE ROW (§16.51).** Every row closed from here gets a book-wide sweep of
   its proposition across lessons + Maker + banks before it is marked SHIPPED. **S185's row would have
   been reported closed with five live sites left, including a graded one.**

## STANDING, UNCHANGED
- **`gate_payload_match` IS NOT ONE OF THE GATES** (S137) and **TAKES ARGUMENTS**.
  Its `BOXED_FP` pins are **advisory but NOT unchecked** — an intentional box edit needs `--update-fp`
  **and a reverse control**, which S185 ran.
- **`byte_audit` ARM 2 CANNOT SEE A FIGURE IN PROSE.**
- **§16.32–§16.44 STILL HAVE NO NUMBERED BODIES.** §18.3b seated S184, §16.51 seated S185.
- **A BIBLE SESSION BUMP IS A REGENERATION OBLIGATION** (S175) — fired again; `GPT_WORKLIST.md`'s
  whole diff was the stamp line. **File in BOTH homes**: `current_session()` reads a LINE-START entry.
- **Fall launch Sept 8.** Syllabus dates still `[TBD]` — school has published only through Sept 7.

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```
**`--selftest` CANNOT RUN BEFORE `--sizes`** — CONTROL K dies with a `KeyError`.

**STANDING CONTROLS (last reproduced S183; NOT re-run at S184 or S185, neither of which touched a
payload byte):** `11/after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,248** · `14/finished` **26,002** ·
`15/finished` **28,406** · `16/finished` **28,626**.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`ef2bb39`**. Census **41,746**.
Bible **v8.180** · `BookComponentStandard` **v01.13.0** · Maker **v2.67.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.73.0** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.3** ·
`build_family_map` **v1.6.6.3** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.31.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`prose_canon` **v1.1.0** ·
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

Lessons: L01 v03.32.1 · L02 v03.26.1 · L03 v03.47.0 · L04 v04.29.5 · L05 v04.29.3 · L06 v04.34.0 · L07 v04.31.8 · L08 v04.32.2 · L09 v05.27.5 · L10 v02.30.4 · L11 v02.31.1 · L12 v01.35.2 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.0 · L16 v02.28.1.

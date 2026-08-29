# ZUMO — S195 HANDOFF (written at S194 close · paste at top of Session 195)

## READ THIS FIRST

**NOTHING FROM S194 IS PUSHED.** 16 paths differ from HEAD (`45a8f45`) — 14 modified, one **rename**,
one deletion, one new file. 0 unbumped.
**THE RENAME IS A DELETION PLUS AN ADDITION IN GITHUB DESKTOP** —
`images/L03_IMAGE_3-14_astar_board.jpg` goes AWAY and
`images/L03_IMAGE_3-14_zumo_32U4_oled_main_board.jpg` arrives. Two checkboxes, and the delete side is
where it gets missed. **Deleting `ZUMO_S194_HANDOFF.md` is also part of this push** and
**`ZUMO_S195_HANDOFF.md` IS A NEW FILE.**
**`newproject.html` was NOT touched** — no Maker upload, no rename-on-disk dance.
If `__pycache__/` exists, delete it LAST; it regenerates on every gate run.

**`site_parity` IS DISCHARGED FOR S193's PUSH AND IS OWED AFTER THIS ONE.** S193's work landed as
`f9e74a0` + `45a8f45` (Aug 28, 17:04 and 17:06 EDT) — **the S194 handoff's "NOTHING FROM S193 IS
PUSHED" was stale by the time it was read.** Verified at S194 open: **PARITY twice, 21:34 and 21:37
UTC**, 28 and 31 minutes past the 10m57s floor. **This push renames an image asset**, so the asset
arm WILL move — run it twice past the floor and believe the repeat.

**`byte_audit` OWES NOTHING. Zero payloads moved and zero bytes.** Every S194 edit is lesson prose,
one bank stem, Bible canon and a filename. The harness was never stood up. Standing control **20,592**.

**82/82 gates** · `gate_payload_match` **PASS**, advisory unmoved at **635** ·
`retired_claims` **CLEAN, 24 registered** (was 23) · `quiz_bank --check` **16 banks valid** ·
`callout_id` **1135** · `census --selftest` ALL CONTROLS PASS ·
`build_worklist --check` current (regenerated on the Bible bump, S175 coupling).
**Tally unmoved: 103 closed / 96 fixed / 2 parked / 140 open of 245.**

---

# 1. WHAT S194 DID

## §16.25 NAMED THE RIGHT BOARD AND THE WRONG VARIANT, FOR THIRTY-TWO SESSIONS

DJ ruling S194: ***"Fix it everywhere."*** The fleet carries the **`Zumo 32U4 OLED Main Board`** —
a DIFFERENT Pololu product from the plain `Zumo 32U4 Main Board` §16.25 canonised at S162.

**THE EVIDENCE WAS INSIDE THE PHOTOGRAPH THE WHOLE TIME.** `L03_IMAGE_3-14`'s own silkscreen reads
`Zumo 32U4 OLED` beside the Pololu logo. S162 had already cited that same image's `alt` text as the
thing that *"settles what the photograph shows without a reshoot."* **It settled the board and not
the variant** — and §16.25 then carried the short spelling in its own canon line while naming the
OLED fleet two paragraphs above it, the contradicts-its-own-file shape the section exists to record.

**MEASURED MORPHOLOGICALLY BEFORE A WORD WAS CHANGED** (§24.6c): every `Zumo 32U4` plus its next
three words, not a search for the phrase expected — **394** mentions across sixteen lessons, the
correct product name appearing **ZERO** times, all **14** sites carrying the short one.
**A RENDERED SWEEP IS NOT A CORPUS SWEEP** — the first pass counted 13 and missed an `alt`
attribute. L05 already carried `Zumo 32U4 OLED main board` in one `alt`: the right spelling existed
in the book once and never reached the canon.

**THE BANK REPEATED IT.** `L01_B56`'s stem said *"The Zumo 32U4 Main Board and the ATmega32U4 are
two names for the same part."* Fixed. Seven pins bumped (L01/L02/L16 on lesson_01,
L03/L04/L11/L13 on lesson_03) after sweeping all sixteen banks for the delta. The two surviving
short-name hits are S162 narration inside YAML comments, which `assert_true_text` does not read —
verified, not assumed.

## THE CONTROL IS THE FINDING: 82/82 WAS BLIND TO IT
Restoring the short name to L03 left the whole suite green. **Gate 76 watches for A-Star being
called the brain and says nothing about WHICH Zumo main board.** Registered instead as
`retired_claims` **#24** with a **negative lookahead** so `Zumo 32U4 OLED Main Board` cannot fire.
Controls: the page arm FIRES on a plant and is SILENT restored; the lookahead discriminates all four
casings.

## AND A FIFTH CONTROL DID NOT FIRE — **THIS IS THE OPEN ITEM**
Planting the short name into `L01_B56`'s STEM left `retired_claims` **CLEAN**.
`assert_true_text` reads a `true_false` question's `stem` AND `why:` only when `correct is True`;
**when `correct is False` it reads NEITHER.** The stem is correctly exempt — it is the declared-false
trap — but **the `why:` on a false true/false is prose in the book's voice and asserts what IS true.**
**This is S193's `L10_B21` finding one level over:** S193 opened the distractor `why:` for multiple
choice and left the `true_false` FALSE branch closed. **Fourth occurrence of the family.**

**MEASURED:** patching the branch and re-running against all **24** retirements and **16** banks
returns **CLEAN — zero findings.** Free today.
**NOT TAKEN, and the reason is that zero fires is HALF a control** — it shows the widened arm does
not false-fire and shows nothing about whether it catches a real instance. A session that changed
the content should not also change what the instrument watching that content can see.
**DJ's ruling. The patch is one line** (`retired_claims.py`, `assert_true_text`, unindent the
`out.append(str(q.get('why', '')))` inside the `true_false` branch).

## TWO SELF-INFLICTED ERRORS, BOTH CAUGHT BY THE INSTRUMENTS
1. **The changelog entry landed SECOND.** Anchored on `v8.188` without checking what sat above it —
   `v8.189` did. `session_versions` said *newest Bible entry says S193* and named it. Moved to the
   top; both paragraph boundaries verified clean. **Anchor on the LINE-START version form AND
   confirm nothing precedes it.**
2. **Gate §24.24 fired on my own prose.** The Status line named an `AFTER_LAUNCH` item by number
   immediately before the word CLOSED — a digit beside a status word, indistinguishable from a tally
   claim. Reworded. **The gate was right and the digit was mine.**
   **AND IT THEN FIRED ON THIS BULLET**, because quoting the offending phrase reproduces it: the
   number above is spelled in words on purpose. **You cannot cite a gate-tripping digit in a gated
   home** — S193 hit the identical wall citing a retired tally, and the device is the same one.

---

# 2. S195 OPENS HERE

## THE CALENDAR IS PINNED. THE LAUNCH DATE EVERY PRIOR HANDOFF CARRIED WAS WRONG.
**Robotics is D BLOCK. There is NO D block on September 8.** First meeting **Fri Sep 4, 2:05–2:30,
twenty-five minutes**; first full period **Wed Sep 9**. Term runs to **Fri Nov 13** (28 teaching
periods) plus the **exam block Tue Nov 17, 1:30–3:30**. No class **Mon Oct 19** or **Mon Nov 2**;
**Sep 25 is 30 minutes**; **Oct 9 is Fall Midterm**. Reconciled twice against the schedule's own
footer — 29 meetings, 1,865 minutes — and three pages rasterized and read against the parse.

**THIS RE-PRICES THE WORKLIST AND THE RE-PRICING IS THE POINT.** L01–L08 carry zero open rows and
cover the first five weeks. **L09 is not taught until Wed Oct 21** — eight weeks out, not five.
L14/L15/L16 are outside Fall scope, accounting for seventy-seven of the remaining rows.
**There is more runway than the last four handoffs assumed. Work L09–L13 in teaching order, with
the robot, ahead of each lesson's date — not in a panic.**

**MILESTONES PINNED:** M1 Sep 18 · M2 Sep 28 · M3a Oct 5 · M3b Oct 16 · M4 Oct 26 · M5 Nov 6 ·
M6 Nov 13. Exam block is the re-demo window.

**STILL DJ'S, STILL `[TBD]` IN THE SYLLABUS — THREE, AND ALL THREE ARE ROOM FACTS:** the TDP Google
Doc link · the late-milestone penalty amount · the BQ-CC17 charge time.

**RULE 32 CAUGHT A 209-LINE REGRESSION.** The syllabus was first rebuilt from `/mnt/project`'s copy,
which is **stale against the repo**. v1.3 had since added the TDP setup and submission section, the
whole *If You Fall Behind* path, the poster grade line, the AI-use policy and the Day One checklist —
**all of which an overwrite would have deleted.** The draft was thrown away and the dates applied as
a minimal edit to the tracked file. **A project-file copy is not the tree. Diff before you replace.**

## THE POLOLU PHOTO REQUEST IS DRAFTED AND UNSENT
Ben Schmidel (Pololu) offered higher-resolution originals on Aug 5 and asked for a list with desired
resolutions. **A 14-photograph list was derived** — every Pololu-credited asset enumerated, including
the base64 payloads embedded inside the SVGs, deduplicated by content hash (16 distinct payloads →
14 photographs). Delivered to DJ as a chat artifact, **not committed to the repo**. Highest-value
asks are the two hard crops (the front sensor array strip in L02, the array shot behind L05 5.5a/b).

**A CREDIT QUESTION WAS ASKED THAT EXIF ANSWERED.** `L05_IMAGE_5-04a/b` carry full EXIF — **Apple
iPhone 12 Pro Max, 11 July 2026, 10:26 and 10:31 AM** — and `L04_IMAGE_4-02/4-04` match them on exact
SOF dimensions with metadata stripped. **All four are DJ's own and correctly uncredited.** The
inverse was also tested: `L05_5-05a/b` and `5-06` cluster at 1.4–7.2 mean channel difference from
each other and sit 90–95 from DJ's pair — further than an unrelated control at 60–77 — so the Pololu
credit on those three is consistent. **No credit gap in either direction.**

## THE TRIPLE CHECK FOUND TWO LIVE DEFECTS OUTSIDE EVERY INSTRUMENT'S SCOPE
**ARM 1 swept all 348 tracked text files, not the lessons**, byte-level and whitespace-tolerant.
Two sites the targeted fix never reached, **neither inside `retired_claims`' 17-page scope**:
- **`book_gates.py`'s gate-76 FAILURE MESSAGE** said *the board is the Zumo 32U4 Main Board*.
  **A gate telling its reader to write the retired name.** Corrected; `book_gates` **v1.76.2**.
- **`ZUMO_FIX_TRACKER.md`** — the file whose job is preventing reversion — recorded the retired name
  as the locked target. Struck and superseded.
**GENERALISE THIS: `retired_claims` reads 17 pages and 16 banks. It does NOT read the Bible, the
trackers, the worklists, the handoffs or the INSTRUMENTS. A retirement that lives in a gate's own
message or in a tracker has no watcher at all.**

**ARM 2:** all **1,824** local `src`/`href` references resolved against the filesystem — **0
dangling**, old asset absent, one reference to the new name. Control: reverting one `src` to the old
name fires exactly one.
**ARM 4 (completeness, and the one that has now mattered three sessions running):** swept the
PHENOMENON — every board reference within 60 characters of Zumo/32U4/Pololu — **31 sites, 14 naming
the product, all 14 carrying OLED.** The lone hold-out is L12's *your Zumo's main board*, a
possessive anatomical reference, correct as written. Same class as the bank's *soldered to the main
board*: **do not "fix" those.**

## ARM 3 BLINDED ITSELF, ITS CONTROL WAS NULL, AND THE REPAIR BLINDED ITSELF AGAIN
1. **Line-granularity adjudication cannot see a rider.** Once any intended pattern matched a line,
   the line read as explained — so a planted `brushed`→`brushless` on the SAME line as the product
   name was invisible. **Rebuilt byte-exact:** reconstruct each new line from its old line and demand
   equality. 22 pairs, 0 mismatches.
2. **THE FIRST CONTROL NEVER INJECTED.** The target phrase contains a `</strong>`; the plant
   silently no-opped and the null control read as a pass. **A CONTROL THAT DOES NOT INJECT IS NOT A
   CONTROL** — assert the substitution count, every time.
3. **THE RESTORE ASSERTION USED A WORD THE CORPUS OWNS.** `brushless` is taught in L03, so a clean
   file read as contaminated. **A control predicate that cannot tell the plant from the corpus is not
   a control either.** L03 was reverted to HEAD and its nine edits re-applied under discriminating
   assertions; `git diff` and the byte-exact arm both confirm the result.
4. **A `.bak` in `/tmp` is not a restore path** when the same cell overwrites it. `git checkout --`
   is, and it is what recovered this.
5. **AND THEN `git checkout --` WAS THE HAZARD.** On the L09-02 triple check the same reflex was
   fired at a file whose ENTIRE session's work was uncommitted, reverting it to HEAD. **A `git
   checkout` restore is only safe on a file whose good state is committed.** The recovery source was
   the PLANTED copy — good work plus one known substitution — which was reversed to rebuild the file
   and then verified string by string. **Before injecting into an uncommitted file, snapshot to a
   path the same cell cannot touch, and prefer reversing the plant over restoring the file.**
6. **A verification string must carry the markup.** Checking for `Gap: highest white` returned zero
   on a file that contains it, because the live markup is `Gap:</strong> highest white`. **A
   plain-text needle against an HTML haystack reads as absence.** Confirmed present by re-querying
   with the tags, and structurally by the table-width arm.

## L09 IS THE FRONTIER — ELEVEN ROWS REMAIN (`L09-03` … `L09-13`)
**`L09-01` closed ❌ MEASURED CLEAN — does not reproduce.** Seven hedged prose sites; the bank's
correct option already reads *starting guesses you replace with your own surveyed numbers*.
**Recorded ❌ and not ✅ on purpose: nothing was fixed, and the glyph IS the predicate `census` reads**
— an invented status like *"✅ MEASURED CLEAN"* moved `fixed` by one and the derivation caught it.

**`L09-02` SHIPPED, built against the row rather than from it.** GPT's *5–10 readings per material*
is a STATIC repetition and would have taught the opposite lesson: tape held still measures the
SENSOR, whose noise is tiny, so five near-identical numbers produce false confidence wearing the
costume of rigor. **The variation lives in the TAPE.** Step 9 now sweeps each surface through under
the live display and records the LOWEST and HIGHEST. ±100 became a MIDPOINT rule. **My first
hypothesis — that ±100 contradicts §7.1's red-flag limits — was COMPUTED AND FAILED**: ±100 is safe
for green in (250, 750) and §1 states 300–700. **The rule is safe by COINCIDENCE, not construction**,
it breaks at green ≥ 750, and **§4.1's own dark-forest-green warning describes exactly the tape that
breaks it** — green 780 gives GREEN_HIGH 880, and a black sweep bottoming anywhere in 850–880 still
clears §7.1's calibration red flag, so the band swallows the line while every check passes.
**THE TRIPLE CHECK CAUGHT THIS CLAIM OVERSTATED IN TWO HOMES.** It had read *GREEN_HIGH 880, inside
the line's range* — which is only true if black's LOWEST swept value is at or under 880, a condition
never checked. Simulating the shipped `isGreen()` over swept distributions found the real failure
needs BOTH a high green AND black bottoming in that narrow window. Corrected in the worklist row and
in LIVE.md. **Rule 34 applies to a consequence as much as to a count.** L09 **v05.28.0**; three `lesson_09` pins bumped after reading the delta.

**`L13-21` IS THE SAME CORRECTION AND ITS ROW SAYS SO.** Do NOT batch it blind — read L13 first
(S192's `L15-08` lesson). With L09-02 built it should now be transcription rather than design.


## STILL OWED, UNCHANGED
- **The 7 pinned `prose_canon` residue sites** — three L05/L06 lesson headings and four Maker labels,
  **ONE fix, not two**. Untouched an eighth session.
- **`prose_canon` arms 1, 2 and 4** — unbuilt. No arm without a control per direction.
- **Seat the §16 debt.** Still 26 rules, untouched a ninth session.
- **`L07_GRAPHIC_7-15`'s one real overflow** — `RobotSensors.h`, 14.5 units.
- **`ZUMO_BENCH_TESTS.md` ranks itself.** Run **1 `L10-B1` · 2 `L02-B2` · 7 `L10-B2`** in one sitting.
- **`ZUMO_GPT_REVIEW_WORKLIST.md` footer carries a second version token** (`Worklist v1.2`)
  disagreeing with the header home `session_versions` reads (v1.12). Flagged five sessions, not ruled.

## RITUAL CHANGE (S194) — `session_versions --selftest` JOINS THE SESSION OPEN
It was not in the ritual, and **two of its eight controls were RED on the clean tree** for an unknown
number of sessions. Both were found only because registering a new generator made the roster arm
complain. Run it at open with the rest.

**Session open, complete:** `git ls-remote` → fresh clone → verify the Bible's internal version →
read `LIVE_ZUMO_TEXTBOOK.md` → `book_gates.py` → `session_versions --check` **and `--selftest`** →
`census --selftest` → `gate_payload_match newproject.html lessons/Lesson_*.html` → `callout_id` →
`retired_claims` → `quiz_bank --check` → `build_css --check` → `build_worklist --check` →
`byte_audit --check` → `site_parity` twice.

## THE SYLLABUS IS A SITE PAGE, INLINE-STYLED, AND GENERATED
`syllabus.html` **v1.0**, emitted by `build_syllabus_html.py` **v1.0** from
`ZUMO_Syllabus_WORKING.md`. **EDIT THE MARKDOWN, NEVER THE HTML.** Inline styles by DJ's ruling —
he pastes it into Canvas, which strips `<style>` and `class=`. **This does not reopen §27:** the
lessons are LINKED from Canvas and keep their classes; the syllabus is PASTED. Two delivery paths,
two answers. It links neither stylesheet, so §27.12 does not see it — the §25.6a rule that already
exempts `newproject.html` and `tutor/tutor.html`. **It IS declared canonical in `book_gates`
§12/§23**, with the reason recorded at the gate, because the layout gate caught it as a stray the
moment it appeared and a new delivery path is a new unguarded path.

## STANDING, UNCHANGED
- **`gate_payload_match` IS NOT ONE OF THE GATES** (S137) and **TAKES ARGUMENTS** — pass
  `newproject.html lessons/Lesson_*.html`, or it reports a COVERAGE failure on a subset.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). **LIVE.md carries TWO `**Versions:**`
  lines** — line 6 is current. **Keep the Status line to ONE line.**
- **The visible §5b banner is spelled `Version 04.31` — BARE.** A `v`-prefixed grep cannot see it,
  and a MINOR bump does not move it: only the hidden `v##.#.#` comment changes.
- **`quiz_bank.py` LIVES IN `quizzes/`, NOT THE REPO ROOT.**
- **A BIBLE SESSION BUMP IS A REGENERATION OBLIGATION** (S175) — fired, `GPT_WORKLIST.md` regenerated.
- **A BIBLE BUMP HAS TWO HOMES** (S185): the version line AND the standalone changelog entry
  `current_session()` reads, **newest first, one entry per PARAGRAPH.** S193 swallowed its neighbour;
  **S194 landed second by anchoring on an entry that was no longer the top one.** Check both.
- **A CALLOUT COSTS THREE PINS** — image references, the gate 47/59 census in BOTH homes, and the
  §27.11 digest. Prove count AND RANK before moving the digest.
- **YOU CANNOT CITE A WRONG TALLY IN A GATED HOME**, and gate §24.24 cannot tell a tally figure from
  any other digit beside a status word. Spell retired or incidental figures in WORDS.
  **THIS FIRED FOUR TIMES IN S194 ALONE**, every time on prose the session wrote about its own work:
  an `AFTER_LAUNCH` item named by number before the word CLOSED · the handoff bullet that QUOTED that
  phrase in order to warn about it · a section heading reading *two of thirteen closed, eleven
  unread* · and a LIVE.md sentence pairing the out-of-scope count with the open total in digits.
  **Writing about the tally is the hazard, not the tally** — and the fourth one was a CORRECT figure,
  which is the whole problem: the gate cannot tell a right tally fragment from a wrong one. The run
  form is the only place four figures may appear together; everything else gets spelled in words.
  **AND QUOTING THE OFFENDER MAKES A FIFTH.** Naming the phrase in order to warn about it reproduced
  it here and failed the gate again — the identical trap the second occurrence sprang. **Describe the
  shape. Never quote the string.** Say it in words or keep the digit
  away from CLOSED / OPEN / FIXED / PARKED.

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```
**`--selftest` CANNOT RUN BEFORE `--sizes`** — CONTROL K dies with a `KeyError`.
**Run `harness_setup.sh` in the FOREGROUND and read `objects: 41` before trusting anything
downstream** — backgrounded, it has died silently at `== core build ==` with 0 objects.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves ·
RoboLore brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`45a8f45`**. Census **41,814**.
Bible **v8.191** · `BookComponentStandard` **v01.13.0** · Maker **v2.70** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.4**.

Instruments: `book_gates` **v1.76.4** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.5** ·
`build_family_map` **v1.6.6.6** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.33.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.21.2** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** · `build_syllabus_html` **1.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`prose_canon` **v1.1.0** ·
`retired_claims` **v1.1.2** ·
`census` **v1.2.0** ·
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

Lessons: L01 v03.32.2 · L02 v03.26.1 · L03 v03.47.1 · L04 v04.29.6 · L05 v04.30.0 · L06 v04.37.2 · L07 v04.33.1 · L08 v04.34.4 · L09 v05.28.0 · L10 v02.30.7 · L11 v02.31.4 · L12 v01.35.4 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.2 · L16 v02.28.1.

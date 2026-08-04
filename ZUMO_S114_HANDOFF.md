# ZUMO — S114 HANDOFF (written at S113 close · paste at top of Session 114)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's
   `git log -1` does not match, fetch the sha by name (§12.4, *caches lie*).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run, and **READ THE EXIT CODE, NOT THE LAST LINE**:
   `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --selftest` ·
   `pill_sweep.py --audit lessons/Lesson_*.html` · `build_family_map.py` ·
   `class_sweep.py --selftest` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `regex_audit.py --selftest` then `regex_audit.py` · `build_worklist.py --selftest` ·
   `font_stack_sweep.py --selftest` then `font_stack_sweep.py` ·
   `session_versions.py --selftest` then `--check` · `site_parity.py --selftest` then `site_parity.py` ·
   `build_css.py --selftest` then `--check` · `image_audit.py --selftest` then `--check` ·
   `strip_inline.py --selftest` then `strip_inline.py --verify` ·
   `build_palette.py --selftest` then `--check` ·
   `color_index.py --selftest` then `--check` ·
   `gen_bonus_banner.py --selftest` · `gen_part_banners.py --selftest` ·
   `gate_payload_match.py newproject.html lessons/Lesson_*.html`
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   `build_palette.build()`, `class_sweep.sweep(paths)`, `color_index.index(paths)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — that is Pages lag, not a defect (S112).
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5.**

---

# ⏰ SEPTEMBER 8 IS UNDER FIVE WEEKS OUT

**14 images outstanding of 141.** S113 cleared FOUR without a camera, refused a fifth, and
**one came back**: DJ supplied `L03_IMAGE_3-14_astar_board.jpg` at close and it is wired in,
so planned went 140 → 141 and outstanding stayed at 14.

DJ ruled at S113 open: **no more photography for a while.** That is not a blocker on its own —
two of the eighteen came off the list this session by being written rather than shot — but it
does mean the remaining count is now **the honest floor of what a camera has to do**, and it is
worth reading as such:

- **Four are VIDEOS** — `VIDEO 3.1`, `4.1`, `6.1`, `8.1`. None can be written.
- **`IMAGE 3.6`** needs REAL numbers from a real TRIM run. Refused at S113 and it should stay
  refused: a fabricated log is the same defect as a fabricated screenshot.
- **`3.2` and `3.5`** are still the one-floor-rig pair.
- **The nine were read one at a time at S113 close, and two of them fell.** `7.13` and `14.2`
  are retired — see S113 WORK. **The remaining seven each need a ruling and none needs a
  camera to make the ruling**, only to execute it:

| Tag | What it asks for | Reading |
|---|---|---|
| `4.1` | Zumo underside, five sensor windows circled 1–5 | A temporary DIAGRAM already stands in and the row says so. Is the photo still wanted, or does the diagram become the figure? **Cheapest of the seven.** |
| `4.3` | Finished test surface: poster board, black tape line, white margins | This is GEOMETRY, not appearance — margins and a straight line. A diagram carries it and is reproducible; a photo of one person's poster board is not a spec. |
| `12.1` | Delrin sheet with a Zumo mid-turn | Genuinely camera. The point is the SURFACE, which is exactly the thing a diagram cannot show. |
| `13.1` | Rescue space: walled zone, silver strip, victim balls | The RCJ field is published spec geometry. Almost certainly a diagram, and a diagram is legal to redraw where a photo of someone else's field is not. |
| `13.2` | Preview: servo gripper, modified blade, competition robots with arms | Hardware the school may not own. **Likeliest deletion of the seven** — it previews an upgrade path the course does not teach. |
| `14.1` | Robots competing at a RoboCup Junior event — *the energy, the excitement* | Decorative, and a sourced event photo carries a rights question the book has no answer for. Delete, or replace with something the course owns. |
| `16.1` | Showcase day: robots, posters, bracket on the whiteboard | **Cannot exist until the first showcase happens.** It is not outstanding work, it is a future capture. Worth marking as such so it stops reading as a debt. |

---

# STATE

Fresh-clone verified at **`5dd35d8`**. Census **40,015**.
Bible **v8.102** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.43.2** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.2** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.15.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.2.1** ·
`image_audit` **v1.1** ·
`strip_inline` **v1.1** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`font_stack_sweep` **v1.2.0** ·
`going_deeper` **v01.4.1**.

Lessons: L01 v03.19.1 · L02 v03.11.1 · L03 v03.28.0 · L04 v04.19.1 · L05 v04.19.1 · L06 v04.23.1 · L07 v04.22.0 · L08 v04.19.1 · L09 v05.16.1 · L10 v02.16.1 · L11 v02.17.1 · L12 v01.19.1 · L13 v02.17.1 · L14 v02.22.0 · L15 v02.17.1 · L16 v02.12.1.

**47/47 gates.** `--anomalies` silent · family map **1049/1049** · `regex_audit` 0 leads ·
`build_css --check` current at **646 rules** · 0 dead classes · `color_index --check` clean ·
`build_palette --check` matches the ruling · `image_audit --check` current · both banner
generators green · `gate_payload_match` PASS.

---

# THE ONE THING TO CARRY OUT OF S113

**A BASELINE THAT LOOKS LIKE A COUNT WILL BE READ AS A COUNT.**

Adding one callout to L03 made `build_family_map.py` print **`assigned 1049 / 1048`**. Read it
out loud: 1049 of 1048. The denominator was never a parse of the book — it is a literal on line
196, frozen at S96 — and for seventeen sessions nothing needed to notice, because no callout was
added or removed. Gate 47 failed, correctly, but what it was actually asserting was *"the book
still has exactly the 1,048 callouts it had in S96,"* not *"every callout resolves to a family,"*
which is the name it prints.

**This is §24.8 wearing a new hat.** The test — *if the answer were the opposite, would this
instrument look different?* — passes here, which is why the gate fired at all. The failure is
one layer up: **the instrument's LABEL described a different measurement than the instrument
performed**, and the label is what a reader reasons from. S112's `assigned 1047 / 1048` was read
all session as *one block fell out*, and it was; but the same line would read identically if
someone had deleted a callout, and nobody would have known which.

**How it was handled, and the order matters:**
1. **Controlled BEFORE the literal was touched** — identical generator version, pre-edit tree
   against post-edit tree. Only two lines differ: WHAT YOU SHOULD SEE 27 → 28, and the total.
   **The other 29 family counts are byte-identical.** So the delta is the one added block and
   nothing else — the total alone would not have proven that, which is the v1.1.0 changelog's
   own warning arriving on schedule.
2. **Literal moved 1048 → 1049**, `build_family_map` v1.3.1 → **v1.3.2**, with the reason and
   the control written into the file beside it.
3. **The real fix deliberately NOT taken.** Parsing the true total (`assigned + len(unk)`) and
   asserting the baseline as its own separate check makes the printed line honest and makes gate
   47 mean what its name says. It also **changes what gate 47 covers** — it would stop noticing
   a callout being added or deleted, which is a genuinely useful thing to notice. That is a
   ruling, and it is in the queue.

**Until it is ruled: every callout added anywhere in the book fails gate 47 until a human edits
that literal.** Write that into the next session's expectations rather than rediscovering it.

---

# S113 WORK

## Two figure debts cleared without a camera, and a third refused

**`[IMAGE 3.4]` — the lesson was pointing at something it never showed.** L03 Step 12's DO THIS
NOW ends *"Look for SUCCESS in the terminal output"*, and the next element was a dashed
placeholder box reading `[IMAGE 3.4] Build and upload success messages in terminal`. The
instruction had no payload. It is now a `👀 WHAT YOU SHOULD SEE` callout carrying a §22 terminal
block — L01's live build-result block copied in SHAPE, `[SUCCESS]` in `#6a9955` per §22.1.

**No numbers were invented, and that constrained the design.** PlatformIO's real build output
carries Flash/RAM percentages specific to the L03 program; L01's canonical block carries the
bare `[SUCCESS]` bar and nothing else, so that is what was copied. A duration was considered and
dropped — L01's *"Took 3.42 seconds"* is L01's measured number, not L03's.

**Step 13 was checked before Step 12 was written.** L03's upload step already pairs DO THIS NOW
with its own WHAT YOU SHOULD SEE, so the new block makes the two steps symmetric rather than
duplicating one. That symmetry is why it is a callout and not a bare `<pre>`.

**`IMAGE 3.14` — the audit was counting a figure that had already been removed.** The row was
marked ❌ removed and still read `[IMAGE 3.14]`, and **the BRACKETED tag is what marks a figure
PLANNED**. S111's retired `IMAGE 2.5` row in L02 is the precedent and carries the bare tag, so
this was applying a ruling, not making one. Brackets dropped; 18 → 17 before 3.4 took it to 16.

**Its DESCRIPTION was left alone on purpose — see the queue.** The row records a replacement
that did not happen.

**`[IMAGE 3.6]` REFUSED.** Serial Monitor log of TRIM adjustments across several runs. It needs
real numbers from a real run. Not written, not staged, still outstanding, and it should stay
that way until the robot is on a floor.

## `GPT_BRIEF_FORMAT.md` → Bible §24.15, and the file must be deleted

Written at S112 and committed to the repo root, where **nothing gated it, nothing linked it and
no roster named it** — the §12.2 shape exactly, a standing rule stored where it will drift
silently. Moved into the Bible in full: the MEASURED FACTS preamble, the send / don't-send /
send-with-facts split, the two things the S111 package did right, and the requirement that
reference files come back unmodified. The Bible moves to **v8.101**.

**`GPT_BRIEF_FORMAT.md` is now redundant and its deletion is a GitHub Desktop checkbox.**

**Recorded, not fixed: §24.14 does not exist.** Gate 47 ships printing `§24.14 every callout
block resolves to a family` against a section number this Bible has never carried. §24.13 is
followed directly by §26. Same debt shape as §21.1's thresholds living only in `book_gates.py`,
and it is now named in the v8.101 changelog and marked in place in §24 so it cannot be
rediscovered as news.

## §27.11's digest moved, and it moved the safe way

**646 rules and 2,367 declarations are UNCHANGED** — not one rule added, removed or altered.
Only the digest. The cause is that `build_css` orders rules by usage count, so five counts
moving (`span` 831→832, `div` 728→729, `pre` 279→280, `.p-mb-0` 337→338,
`.callout-17a2b8-bg-d1ecf1` 30→31, `.div-2196f3` 10→9) changed three rules' POSITION.

**Diffed in full before the baseline was touched, then control-run after:** deleting one
`color: white;` still FAILS the gate, and the restore is byte-identical by md5. Moving a
baseline without re-proving the gate still fires is how a baseline move disarms a gate quietly.
`book_gates` **v1.42.1 → v1.42.2**, with the delta written at the constant.

## Two more figures retired, and both were duplicates of live content

**`[IMAGE 7.13]` — L07 already draws it, twice.** The tag asks for *"a diagram showing the final
project structure with all modules."* **GRAPHIC 7.16 is *the eight-file architecture, and which
file includes which*** and is live in the lesson; **GRAPHIC 7.15 is *the PlatformIO project tree***
and is live twice. The placeholder sat asking for a third drawing of the same thing. Its row was
also typed **Photo / screenshot** for something its own description calls a diagram — the same
internal contradiction as `IMAGE 3.14`'s row, in a different lesson, found the same way.

**`[IMAGE 14.2]` — the list above it already says everything the photo would.** *"A well-organized
competition kit with labeled compartments"*, sitting immediately below a **twelve-item Competition
Day Kit list** naming robot, laptop, USB cable, two sets of fresh AAs, charger, screwdrivers,
electrical tape, spare jumpers, notebook, snacks and tuning documentation. A photograph of a
tackle box adds nothing to that.

**Both follow S111's `IMAGE 2.5` retirement exactly:** bare tag, `Retired — <why>`, type `—`,
state ✅. **The state cell caught a trap worth recording:** L14 writes it as the entity `&#9744;`
where L07 writes the literal `☐`, so a replace written against one lesson's spelling silently
matches nothing in the other. The assert caught it; a global replace would not have.

Applied, both moderate — a planned figure leaving the page changes what renders, so both §5b
homes move: **L07 v04.22.0** (from v04.21.1) · **L14 v02.22.0** (from v02.21.1).

**A trap this session hit TWICE, so write it down:** `session_versions._versions_in()` builds its
dict from every `Name vX.Y` match in the whole file and **the LAST match wins**, so a prose
sentence written as *"Bible v8.100 → v8.101"* or *"L07 vOLD → vNEW"* silently OVERRIDES
the emitted STATE block and `--check` reports a disagreement that does not exist in the files.
Backticks are what save the other mentions — `` `build_family_map` v1.3.1 `` does not match,
because the backtick breaks the name. **Write the OLD version in parentheses after the new one, or
wrap the name in backticks.** Both times, `--check` caught it before the push — **and then a third time, on the sentence
written to warn about it**, because the example named a real lesson and a real old version. The
example now uses placeholders. An instrument that catches the documentation of its own trap is
working.

## §27.11's digest moved TWICE this session, both times the safe way

**646 rules and 2,367 declarations never moved.** Not one rule was added, removed or altered in
either move. `build_css` orders its output by usage count, so retiring a placeholder changes a
count (`.div-2196f3` 10→9→8, `.div-ccc` 2→1) and that changes a rule's POSITION, and position is
in the digest. **Diffed in full against the pushed clone before each move, and control-run after
each:** deleting one `color: white;` still FAILS both times.

**`.div-ccc` is now down to ONE use book-wide.** It is the image-placeholder box. When the last
placeholder retires, the rule dies on its own — expected, not a defect, and written at the
constant so nobody diagnoses it as one.

## A find that is not S113's work but is S113's to report

**GPT Task 2 and Task 4 are not in the repo.** The S112 handoff lists both as *"reviewed
structurally, neither applied."* Searched: only `GPT_BRIEF_FORMAT.md` mentions them, and the
syllabus's own *Still To Add* list still carries its four items — all four blocked on facts only
DJ has (milestone dates, the notebook Doc link, charging location, late penalty). **Inference,
stated as one:** the outputs were reviewed in the S112 chat and never staged to disk, so they
are gone unless DJ still has that thread. Task 4 in particular was measured good — 19/19
headings, 263/263 table pipes, 10/10 checklist items, 499 bytes shorter — and it pairs with the
standing *re-commit the TDP template* item.

---

# THE HANDOFF NUMBERING WAS WRONG FOR TWO SESSIONS — READ BEFORE WRITING S115'S

**DJ caught this, not a gate.** *"the last one was 112 again and this one says 113, but you are
calling it 114."*

**THE CONVENTION, verified from git history 10/10 across S103–S112:** the filename number, the
title number and the *"paste at top of Session N"* number are **the same number**, and it is the
session that **READS** the file. `ZUMO_S112_HANDOFF.md` is titled *"S112 HANDOFF (written at S111
close · paste at top of Session 112)."*

**DEFECT 1 — S112's, and it is the one that caused the confusion.** S112 wrote its OUTGOING
handoff into the INCOMING handoff's filename. `ZUMO_S112_HANDOFF.md` was edited in place across
three commits with its STATE block updated each time — `893b8b6` → `4558257` → `8ae3857` — while
its title stayed *"S112 HANDOFF · paste at top of Session 112."* So at S113 open the repo root
carried a file whose name and title both said *read this at S112* and whose contents were the
S113 handoff. **`ZUMO_S113_HANDOFF.md` never existed in the repo**, and the S113 text DJ actually
pasted carries state `b4d5559`, which no committed version of that file ever held. It was written
in the S112 chat and pasted directly, never committed.

**DEFECT 2 — S113's, i.e. mine.** I inferred the convention from the single live example, which
was the defective one, concluded *filename = writing session*, and pushed this file as
`ZUMO_S113_HANDOFF.md`. That name is now burned on content that belongs to S114. **Corrected the
same session: this file is `ZUMO_S114_HANDOFF.md` and `ZUMO_S113_HANDOFF.md` is deleted.**

**WHY NOTHING CAUGHT IT, AND THIS IS THE PART THAT MATTERS.** Gate 28 asserts the root holds
**exactly one** file matching `ZUMO_S\d+_HANDOFF\.md`. It never asks whether the number is the
right number, and it never compares the filename to the title inside the file. **A stale number
and a wrong number both pass, and both did.** This is §24.8 exactly: if the answer were the
opposite — a handoff numbered for the wrong session — gate 28 would look identical.

**BUILT THE SAME SESSION, DJ ruling *"Do it"*.** Gate 28 now parses the number out of the
filename, out of the `# ZUMO — SNN HANDOFF` title and out of the *"paste at top of Session N"*
clause, and fails when any two disagree — and fails **loudly rather than skipping** if the title
shape is gone, because a check that silently opts out of itself is the §24.8 failure again.
**Control-run four ways, and two of the four are the real defects above, not synthetic ones:**
file S113 / title S114 FAILED naming both numbers · title lagging the filename (S112's actual
shape) FAILED · the title line disagreeing with its own *paste at top of* clause FAILED · the
title reworded away FAILED naming the missing shape. `book_gates` **v1.42.2 → v1.43.0**, and
Bible **v8.102** records it at §12.2.

---

# S114 QUEUE

## Rulings outstanding — three of these are S113's and are cheap
- **Should `build_family_map` parse its total instead of holding a baseline?** See THE ONE
  THING. Parsing makes the label honest; the cost is that gate 47 stops noticing an added or
  deleted callout, which needs its own assert. One line either way, and it decides what happens
  every time the book grows.
- **Write §24.14.** The rule gate 47 already enforces, sitting behind a section number that does
  not exist.
- **The `#666` footer colour** — 18 declarations reaching 17 pages, and eight `.p-c-666*` class
  families whose NAMES encode the hex. A book-wide ruling plus a class rename.
- **16 uppercase-only colours** — house-style inconsistency, no variance, unruled. Lowercasing
  is a 197-occurrence change nobody has asked for.
- **`font_stack_sweep` rule** — it still wants to rewrite all 15 Consolas stacks and the standing
  note says they are correct. **Consolas: 15 declarations, all with a fallback, zero bare — the
  note is CORRECT.** A genuine rule disagreement.
- **Callout colours re-examined** — v8.87's Scope C. **Now much safer:** family no longer depends
  on colour anywhere, so a repaint cannot move the taxonomy.
- **`3.2` vs `3.5`** — before/after split, or one figure and a deleted row.
- **NOTE per-block pass** (133 blocks, four destinations).
- **Nav `<details>` carry no `data-reveal`** — §25.12 exists because one untyped `<details>` slipped.
- **Selftest-coverage gate** — offered, not built.
- **The seven remaining figure tags** — the table under the SEPTEMBER block. Seven rulings, no
  camera needed to make any of them.

## Ruled and DONE at S113 close
- **`IMAGE 3.14` — RESOLVED, AND IT ENDED UP THE OPPOSITE OF WHERE IT STARTED: DJ SUPPLIED
  THE PHOTO AND THE FIGURE IS LIVE.** The row's ORIGINAL description was right all along —
  *"Top view of the A-Star 32U4 board"* — and `L03_IMAGE_3-14_astar_board.jpg` is now wired into
  §4.2, directly after the sentence *"The A-Star 32U4 board converts your code commands into
  electrical signals."* Board → motor → gearbox, in that order.
  **THE PARENTHETICAL WAS THE STRAY, NOT THE SUBJECT.** *"(removed from 'Inside the can' —
  replaced by GRAPHIC 3.18)"* described a DIFFERENT figure's fate. `🧠 LEARN: Inside the little
  silver can` is real, at L03:1142, and **GRAPHIC 3.18 sits inside it at 1150** alongside IMAGE
  3.1 — so 3.18 replaced a MOTOR figure in that block, and someone appended that clause to the
  board photo's row. One row, two figures' histories.
  **THREE READINGS WERE OFFERED BEFORE THE RIGHT ONE, AND THE PROCESS STILL WORKED.** The
  subject was dropped rather than rewritten; then DJ's *"side and top view inside the micromotor
  gearbox"* was applied to 3.14 and that was wrong too — it describes GRAPHIC 3.18; then the
  actual asset arrived and settled it. **Every wrong step was reversible because none of them
  invented a fact into canon** — the subject line was deleted rather than guessed, and the guess
  that was written got overwritten by an artefact one message later. Superseded: *"3-18 replaced
  3-14."*
- **(superseded, kept for the record)** DJ ruling: *"3-18 replaced 3-14."* The replacement claim in that row is
  therefore TRUE and the row now takes the S111 `IMAGE 2.5` retirement form: *Retired — replaced
  by GRAPHIC 3.18, the gearbox cutaway*, type `—`, state ✅.
  **SUPERSEDED BY THE PHOTO — see the entry above.** At the time this read: The old text called the figure
  a *"Top view of the A-Star 32U4 board"* removed from a section named *"Inside the can"* — but
  GRAPHIC 3.18 is the gearbox cutaway and *"Inside the can"* appears nowhere else in L03, so the
  row contradicted itself. **DJ, S113: *"A side and top view of what's going on inside the
  micromotor gearbox."*** That resolves both halves at once: *"the can"* is the MOTOR can, the
  A-Star wording was a stray, and GRAPHIC 3.18 is a genuine like-for-like replacement rather than
  a substitution of one subject for another. The row now carries that subject in DJ's words.
  **The sequence is the lesson, not the fix:** the subject was DROPPED first rather than
  rewritten to a plausible guess, and the guess on the table — that *"the can"* meant the motor
  can — turned out to be right. **Being right is not the same as being measured**, and a correct
  guess written into canon is indistinguishable from a wrong one six sessions later. It took one
  question to turn it into a fact. L03 is at **v03.28.0** (from v03.25.0) after the figure landed.

## Ruled, not yet done
- **DELETE `GPT_BRIEF_FORMAT.md`** — moved to Bible §24.15 this session. GitHub Desktop.
- **`[IMAGE 3.6]` → §22 terminal block, ONCE THERE ARE REAL NUMBERS.** The form is ruled; the
  data is not available. Do not write it from imagination.
- **Apply GPT Task 2 and Task 4** — *if DJ still has the S112 outputs.* Not in the repo.
- **The nine unexamined image tags** — `4.1`, `4.3`, `7.13`, `12.1`, `13.1`, `13.2`, `14.1`,
  `14.2`, `16.1`. Read each one and ask whether it should be a photo at all. This is the method
  that cleared two figures this session.

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12–14" is **obsolete** under the six-pill rail — retire, don't argue ·
`css/book.css` has zero custom properties (`build_palette --css` emits them ready) ·
**26 gradient definitions across 18 SVG files** remain (5 referenced by nothing) — v8.87's ban
covers graphics too and the SVGs have still NOT been touched ·
**41 marks generated in `images/marks/`, not one wired into a lesson**, against 2,016 emoji
glyphs. The icon arc is fully built on the supply side and has not started on the demand side.

## Bench (need the robot — DJ has parked photography, so these are parked with it)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
**a real TRIM run for `IMAGE 3.6`**.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file in the same list as repo files.**
3. **Never produce PUSH_ME_*.md or MD5_*.txt.** Checksums and instructions go in the CHAT ONLY.
4. `going_deeper.html` belongs at the repo ROOT, not in `lessons/`. `book.css` belongs in `css/`.
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE
   and run `book_gates` THERE before presenting md5s.**
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S114 close, adding
   `ZUMO_S115_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox, not a CLI
   command.
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
   Verified 10/10 across `ZUMO_S103`–`ZUMO_S112`: filename number == title number, and the title
   reads *"written at S(N-1) close · paste at top of Session N."* This file is
   `ZUMO_S114_HANDOFF.md` and is titled S114 because **S114 reads it**. Gate 28 cannot check
   this — see the queue.

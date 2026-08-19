# ZUMO — S176 HANDOFF (written at S175 close · paste at top of Session 176)

## READ THIS FIRST

**S175's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S175_HANDOFF.md` is part of that push. **If `__pycache__/` exists in your tree,
delete it LAST, immediately before pushing** — it REGENERATES on every gate run.

**78/78 gates** · `gate_payload_match` **PASS** · `quiz_bank` 16 banks at **1,246** questions ·
`build_css --check` current at 574 rules · `image_audit --check` current ·
`build_worklist --check` current · `callout_id` **1127/0** · census **40,993** ·
`next_pointer` clean.

**`byte_audit` RAN THIS SESSION AND ALL EIGHT STANDING CONTROLS REPRODUCED EXACTLY.** They are
verified as of **S175** — do not re-prove them unless the toolchain or a payload has moved.
`--sizes`, `--selftest` (all controls incl. CONTROL L) and `--check` (eight arms) all PASS;
`--discards` (ARM 9) run and clean.

**S175 TOUCHED NO LESSON, NO BANK AND NO PAYLOAD.** One document, one gate and one generated
file: `ZUMO_SUPER_BIBLE.md` → **v8.168.3**, `book_gates` → **v1.72.7** (78 gates, §16.44 NEW),
`GPT_WORKLIST.md` regenerated (stamp line only).

**`site_parity` WAS NOT RUN — it needs a published tree.** Run it AFTER the push, at least
twice, and believe the repeat (§16.42, and S166's convention).

---

# 1. THE `NINE` vs `15` LEAD IS CLOSED BY A COMPILE

S174 handed it forward as *a lead and not a finding*. It is now a finding.

`byte_audit --discards`: **15 discards over 7 of 105 payloads, 7 adjudicated, 0 unexplained.**

**TWO GENUINELY INDEPENDENT ROUTES, NOT THREE.** The compile; and the arithmetic of v8.165's
OWN pre-fix figures — 23 discards across 9, less the two payloads that entry reports going
4 → 0 each, is **23 − 8 = 15 over 9 − 2 = 7**. **`DISCARD_BASELINE` summing to 15 across 7
entries is NOT a third route**, because ARM 9 asserts that baseline against the compile; it is
one method read twice, and counting it would be rule 79's own defect.

**The `NINE` is the pre-fix PAYLOAD count transposed into the DISCARD slot**, exactly as S174
guessed and correctly declined to act on without a compile.

Corrected in both Bible homes (v8.131: an entry filed in one home is not filed).

**WHY IT WAS CORRECTED RATHER THAN LEFT AS HISTORY — THE REUSABLE HALF.** §16.37 rules that a
provenance record is history and never rewritten. The clause beside it — *both payloads
re-measured with the attribute injected, 4 discards → 0 each* — **IS** provenance, an account of
a measurement performed at S172, and it was left untouched. *The book stands at NINE over SEVEN*
is not an account of an event: it is a **present-tense claim about the state of the artefact**,
checkable today and wrong today. **A record of what was read is history; a claim about what the
book IS is a fact with a comparator.** v8.127.1 is the precedent exactly.

**S174's SITE WAS A DIFFERENT ONE AND IS CLOSED.** LIVE.md's struck S173 block carried the same
wrong pair and rule 50's *other* fate took it — the number went with the sentence that carried
it. Its narration in the v8.168 entry is itself provenance and stays.

---

# 2. FILING THE ENTRY BROKE A GENERATED FILE — AND THAT IS THE BETTER FINDING

`build_worklist --check` was **GREEN at session open and RED immediately after the version
bump.** Cause: S174's own fix moved `GPT_WORKLIST.md`'s session stamp off a pinned literal onto
`session_versions.current_session()`, which derives from the newest Bible changelog entry.
Filing this entry moved that derivation **174 → 175**, so the committed worklist went stale by
exactly one line the moment the Bible said a new session had run.

**S174: *a generator's version bump is a regeneration obligation.* THE SIBLING: A BIBLE SESSION
BUMP IS ONE TOO, for any artefact that stamps the session** — and the fix that stopped a FRESH
copy looking stale is precisely what makes every COMMITTED copy go stale one session later.

**Measured rather than feared, as S174 measured its own cascade: the entire diff is the stamp
line.** 38 files needing a human and 9 local-fix findings across 5 files UNCHANGED — no SVG read
differently, no finding born and none lost.

**POPULATION MEASURED AND IT IS ONE (rule 34):** `build_worklist.py` is the only reader of
`current_session()` outside `session_versions` itself, and `GPT_WORKLIST.md` is the only
generated artefact in this tree carrying a DERIVED session stamp. `css/book.css` and
`IMAGE_WORKLIST.md` stamp their GENERATOR's version — S174's coupling, not this one.

**PUT IT IN THE CLOSE RITUAL BESIDE THE STYLESHEET: after any Bible session bump, regenerate
`GPT_WORKLIST.md`.**

---

# 3. GATE 78 SHIPPED — §16.44, AND THE PRICING THAT SAID IT COULDN'T BE BUILT WAS WRONG

**It was first recorded as owed-not-built**, on the argument that the pair is spelled
`NINE over SEVEN`, `15 over 7` and `15 discards over 7 payloads`, and appears in the Bible as a
live claim, as history, and as a **narration of the defect itself** — three registers, one
spelling. **That was not speculation: the double check's first arm FIRED LOUD ON A CLEAN TREE**
for exactly that reason, because the S175 entry quotes the defect verbatim three times per home.

**DJ ruled BUILD IT. The scope was wrong, not the predicate.**

The registers only collide when the WHOLE FILE is read. **History is excludable BY PROPERTY, not
by a name list (rule 20):** the Bible's changelog IS history (§16.37) and is not read at all;
LIVE.md is read only in its **current session region** — the header plus the newest
`## WHAT SHIPPED IN S<n>` block, both regenerated every session by construction; the handoff is
read whole, because a handoff is current by definition. **A per-session block leaves scope the
moment a newer one is written, so there is no list to maintain.**

**THE PREDICATE IS A CLAIM FORM, NOT A SPELLING (rule 19).** It matches the ASSERTIVE register —
DIGITS and the explicit noun, **outside inline code** — and is **deliberately blind to the
NARRATIVE register**. Two exclusions, both structural: a figure spelled in WORDS is not a claim,
and a figure inside BACKTICKS is a quoted spelling rather than an assertion.

**THE FIRST FORM UNDER-REACHED AND THE TRIPLE CHECK CAUGHT IT.** It required `**` immediately
before the digit, so this handoff's own **ARM 9: 15 discards over 7 of 105 payloads** — bold
opening before the number — was a real assertion the gate could not see. **An INDEPENDENT
re-implementation found it (§24.13):** a token walk with the baseline read by AST from
`byte_audit.py`'s SOURCE rather than by import returned **5 claims where the gate reached 3**.
Widened; the two now agree at 5, the one exclusion being the backticked quotation — **and that
exclusion is controlled, not asserted**: a deliberately wrong value inside backticks is SILENT.

**THE TRUTH IS IMPORTED, NEVER TYPED (rules 83/84):**
`sum(byte_audit.DISCARD_BASELINE.values())` over its length — the same baseline ARM 9 asserts
against a COMPILE in both directions, so the figure cannot rot here without going loud there
first. **The gate costs ZERO compiles**, which is why it can live in `book_gates` where ARM 9
deliberately cannot (S173).

**EIGHT CONTROLS, ONE PER INVOCATION, EVERY RESTORE md5-EXACT.** Stale figure in LIVE.md → 78
**alone** · stale figure in the handoff → alone · emptied baseline → fires rather than passing on
no truth · unresolvable LIVE.md region → COVERAGE arm, whose denominator is the **scopes** and
never the claims, because a session with nothing to say about discards owes nothing · **the
NARRATIVE-register plant is SILENT** · **a wrong figure inside backticks is SILENT** · the blinding reword is SILENT · handoff removed entirely
fires §12.2 **and** §16.44, complementarity rather than a fault (v8.154's shape).

**STATED SCOPE LIMIT (rule 78): a session stating the figure in some OTHER form is not reached.**
Declared, not hidden — S167's word-list problem surviving in miniature. When it first bites, the
answer is a ruling on the claim form, not a looser predicate.

**THIS CLOSES ONE CLAIM SHAPE, NOT THE CLASS.** `byte_audit` ARM 2 still cannot see a figure in
prose, and nothing here reads a sentence.

---

# 4. S176 OPENS HERE

- **A GATE FOR `GPT_WORKLIST.md` IS STILL OWED AND STILL PRICED, NOT SHIPPED** (S174). `--check`
  closes what a session ritual can reach; a gate costs an `svg_layout_audit` pass over every SVG
  on **every** `book_gates` run, and **an arm that made the routine slower is one somebody
  eventually skips**. If it ships, it likely belongs behind the same door ARM 9 uses.
- **EIGHT INSTRUMENTS DIE ON AN UNRECOGNIZED ARGUMENT WITH A RAW TRACEBACK** —
  `build_mark_index`, `gate_payload_match`, `pill_sweep`, `extract_project`, `fit_raster_svg`,
  `flatten_alpha`, `gen_component`, `glyph_scan`. **They are ugly and they are SAFE: none of
  them writes.** Cosmetic, not owed. (Note `gate_payload_match` takes ARGUMENTS:
  `python3 gate_payload_match.py newproject.html lessons/Lesson_*.html`.)
- **S167's DEBT IS CLOSED AND MUST NOT BE RE-OPENED** (Bible §16.43).
- **`gate_payload_match`'s one-directionality** (S173) — a ruling, then a design. Reproduction:
  guard one line in `13/challenge_9_1_keep_sweeping`'s payload out of the Maker, leave
  `Lesson_13.html` alone, run the gate. It passes.
- **ARM 7's two remaining false skips** are stated blind spots, not bugs.
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE.**
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166).
- **`strip_inline --restore` DOES NOT RESPECT THE HELD LESSON STRIP** (S168). SCRATCH-COPY works.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165). When it first fires, the answer is a ruling.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated. Two of its SVG entries
  became newly visible at S174's regeneration.
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

**STANDING CONTROLS, ALL REPRODUCED S175:**
`11/after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,248** · `14/finished` **26,002** ·
`15/finished` **28,406** · `16/finished` **28,626**.

**216 payloads, FOUR declared overflows** — `16/after_step_3` **29,008** · `16/after_step_4`
**29,644** · `16/step_5_serial_traded` **28,944** · `16/step_5_zn_traded` **28,788**.

**THE TIGHTEST PASSING BUILD IS `16/after_step_2` AT 28,648, WITH 24 BYTES SPARE.**

**ARM 9: 15 discards over 7 of 105 payloads, 7 adjudicated, 0 unexplained.**

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo; and RoboLore brand and course scope.
**Delegation removes the question, never the disclosure.**

**§24.19 IS THE TIEBREAKER** — what is best for student learning, when nothing else discriminates.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`294cfae`**. Census **40,993**.
Bible **v8.168.3** · `BookComponentStandard` **v01.13.0** · Maker **v2.62** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.7** · `lesson_inventory` **v1.3.5** ·
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

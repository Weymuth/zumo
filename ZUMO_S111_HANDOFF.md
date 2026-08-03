# ZUMO — S111 HANDOFF (written at S110 close · paste at top of Session 111)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's `git log -1`
   does not match, fetch the sha by name (§12.4, *caches lie*).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run, and **READ THE EXIT CODE, NOT THE LAST LINE** (S110: `session_versions --check` was
   exiting 1 for three pushes while its last line read fine):
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
   **`gen_bonus_banner.py --selftest` · `gen_part_banners.py --selftest`** (both were DEAD for
   seven sessions precisely because nothing ran them).
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   **`build_palette.build()`**, **`class_sweep.sweep(paths)`**.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5.**

---

# STATE

Fresh-clone verified at **`1f489b1`**. Census **40,025**.
Bible **v8.98** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.39.2** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.0** ·
`gen_part_banners` **v1.1** · `session_versions` **v1.15** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.2.1** ·
`image_audit` **v1.1** ·
`strip_inline` **v1.1** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`build_palette` **v1.0** ·
`class_sweep` **v1.0** ·
`font_stack_sweep` **v1.2.0** ·
`going_deeper` **v01.2.0**.

Lessons: L01 v03.18.0 · L02 v03.10.2 · L03 v03.23.2 · L04 v04.18.1 · L05 v04.18.1 · L06 v04.22.1 · L07 v04.20.2 · L08 v04.18.1 · L09 v05.15.1 · L10 v02.15.0 · L11 v02.16.0 · L12 v01.18.0 · L13 v02.16.0 · L14 v02.20.0 · L15 v02.16.0 · L16 v02.11.0.

**45/45 gates.** Nine pushes in S110, every one verified by fresh clone and md5.
`--anomalies` silent · family map 1048/1048 · `regex_audit` **0 leads** (was 1) ·
`build_css --check` current at 657 rules · `site_parity` PARITY · 0 dead classes.

---

# THE ONE THING TO CARRY OUT OF S110

**THE S103 MIGRATION BROKE FOUR TOOLS AND NOTHING SAID SO FOR SEVEN SESSIONS.**

The migration moved every inline `style=""` into `css/book.css`. `book_gates` was taught about
it — it reads through `lesson_inventory.expand_classes()`. **Four other tools were not**, and
each failed in a different way that nobody saw:

| tool | how it failed | why it went unseen |
|---|---|---|
| `pill_sweep` | swept-detector looked for the inline string `width: 4px` | **in the ritual**, printed `*** MIXED ***` on 15 of 16 lessons — an alarm that fires on everything |
| `gen_part_banners` | block regex matched the inline form | run by nothing; died on `AssertionError` |
| `gen_bonus_banner` | matched the nav pill by an inline-style signature | run by nothing; died on `found 0` |
| `font_stack_sweep` | value parser truncated a quoted stack | in the ritual, DRY RUN only — a `--write` would have corrupted `book.css` |

**The rule this yields:** when a book-wide representation changes, the question is not *"did the
gates still pass"* — they did, all of them, every session. The question is **which readers of that
representation were taught about the change**. A tool nothing runs cannot report that it is dead.

**Of 25 root `.py` files, 16 are in the ritual and 6 were run by nothing.** That enumeration is
what turned three ad-hoc finds into a closed class. Do it again after any structural change.

---

# S110 WORK

## The visual direction changed after being measured

DJ ruled sun-faded (specimen D), then: *"None of these really are blue heritage focused. Can you
triple check because your verbage made it sound like the brand link would work."* He was right.
Measured by CIELAB hue gap to canon: warm earth **1 of 6** bands within 20°, every faded variant
1 of 6, and E — which I had presented as reconciling book and brand — **3 of 6**.

**H2 is ruled** and recorded in **`ZUMO_S110_VISUAL_RULING.md`**: sun-faded bands taken FROM
Heritage canon, **5 of 6** within 20° (CIELAB; 4 of 6 in HSV — the counts are metric-dependent and
the document says so). `build_palette.py` **v1.0** is its generator, entrypoint `build()`, and
`--check` re-derives and compares against §3 of the ruling so the table cannot drift from the
derivation. **No band hex exists as a literal anywhere.**

**The structural finding outlives the ruling:** Heritage is five colours but only **TWO hue
families** (CIELAB 15.6° and 4.8° apart; HSV 5.0° and 3.7° — different numbers, same finding). Six
groups cannot separate by hue out of two hues, so they separate by **LIGHTNESS** — which is
§5.0.1's ramp principle arriving from the other side. **The five specific blues stay dead; the ramp
PRINCIPLE is load-bearing again.**

**Two claims of mine are recorded as wrong** in that document, because otherwise the palette will
look like it merely drifted: E was oversold, and swapping D's cap text to Deep Navy was allowed to
sound like a brand link when it moved the measurement 0.7°.

**Still open:** the `+18°` Wrap Up hue shift. It buys ΔE76 **0.4** against Theory. Dropping it makes
every band a canon hue with no derived hue at all, and Wrap Up becomes Deep Navy re-lit — the ramp
stated literally. One hex in two places. **Shipped as-is; DJ has not ruled.**

## Regex failed three times in one session, and the third was inside the sweep written to check the first two

- `\b` matched `div-ai-center` **inside** `div-ai-center-2` → five phantom findings, reported
  before being caught
- `startswith('#section-1')` matched `#section-10`
- a stray `.html$` folded into a stray-file grep counted four legitimate root pages

`-` and `#` are not word characters. **`class_sweep.py` v1.0** is the answer — a parser-based class
index, entrypoint `sweep(paths)`. The corpus holds **292 prefix collisions among 657 class tokens**;
a substring audit over-counts **126** of them. Its Control G asserts INVARIANTS, not today's counts,
because hard-coding numbers that the rail work will legitimately change is drift wearing a check's
clothing.

**All five regex-derived scope claims reproduced under the parser**, so the annotation already in
`ZUMO_S109_VISUAL_SPEC.md` stands.

## `div-d-flex-2` scope — the queue item, closed

**Safe to flip, but flip TWO classes.** `div-d-flex-2` is 7 uses in 7 lessons (L02–L08 nav);
`div-ai-center` is 9 in 9 (L01, L09–L16 nav). Both nav-only, no over-reach. `div-ai-center-2` is a
DIFFERENT class carrying L10's five MYSTERY headers. The two nav rules differ by one declaration,
`align-items: center`, **pixel-identical** on the real 14-anchor L09 nav (control: the same
comparison flipped to column moved it 54px → 378px). **§3's cost stands: two selectors, zero lesson
files.**

**One new lead only the parser could see:** L09 is the sole lesson whose figure table cross-links
into the body — **8 exact `#section-N` anchors inside `<td>`**, sections 1/3/4/6/8A. Looks like a
good pattern one lesson has and fifteen do not.

## Instruments

- **`pill_sweep` v1.1** — migration-aware detector, names which form it found. Corpus is **15 SWEPT,
  L16 no challenges**; it was never mixed. 8 controls, including one that keeps `MIXED` reachable,
  because the failure mode of the fix is an alarm that never fires.
- **`session_versions` v1.15** — **ROSTER COVERAGE** in `--check`. `build_palette` and `class_sweep`
  sat unregistered and invisible. Its existing CONTROL E could not catch them: it lives in
  `--selftest`, which runs at session OPEN, before any new instrument exists. CONTROL G then caught
  that registering was half the job — both were absent from the emitters.
- **`font_stack_sweep` v1.2.0** — the value parser could not read a quoted multi-face stack, so a
  `--write` would have produced `font-family: 'Courier New, monospace','Monaco',…`, **9 malformed
  declarations**. It reported `8 x Consolas` as bare, contradicting a standing note; **the note was
  right.** Fixing it exposed a second bug: `_exempt()` took a FACE and was handed a VALUE.
- **`svg_layout_audit` v1.20** — clears the last `regex_audit` lead, which was real. v1.18 guarded
  `<text>` and left `<image>`; **3 images sit under a rotation** and the two at 90° were measured
  **16% too wide**, biasing toward a FALSE *under the floor*. **My first fix swapped the box for
  both checks and produced two new false findings** — the swap belongs to the resolution edge, not
  the aspect comparison. Caught by diffing whole-corpus findings against the pushed version.
- **`gen_part_banners` v1.1** and **`gen_bonus_banner` v1.4.0** — both read through
  `expand_classes()` now; **both refuse their write path**, because emitting the inline form breaches
  §27.12 and gate 41. Repairs go through restore → regenerate → apply.

## Images — the only deadline, and it moved the right way

**`ZUMO_S110_SHOT_BRIEF_WEEK1.md`** — six shots, not seven, and two need no robot.

**`[IMAGE 3.14]` is NOT a shot.** Its only tag sits inside its own retirement row (*removed,
replaced by GRAPHIC 3.18*), and `image_audit` cannot tell a retirement note from a plan.
**Outstanding is 18, not 19.** *(`IMAGE 3.1` is fine — the lesson points at the `.jpg`; the `.png`
beside it is litter.)*

| group | shots | needs |
|---|---|---|
| desk only | `2.5`, `3.4` | laptop |
| one floor rig | `3.2`, `3.5`, `VIDEO 3.1` | robot, tape, 6 ft, smooth floor |
| same session | `3.6` | laptop still attached |

Filenames were control-run against `image_audit.expected()`; four planted wrong names rejected 3 of
4. **The matcher does NOT enforce zero-padding** — `3-6` passes as readily as `3-06`.

---

# S111 QUEUE — EVERYTHING HERE NEEDS DJ

## Rulings outstanding
- **`+18°` Wrap Up hue shift** — keep or drop (above)
- **`font_stack_sweep` rule** — it still wants to rewrite all 15 Consolas stacks, and the standing
  note says they are correct. Now a genuine rule disagreement, not a parser artifact: every one ends
  in a generic. Should the rule become *designer-first **and** no generic fallback*? That leaves all
  15 alone and still catches Illustrator's `Arial-BoldMT, Arial`.
- **`IMAGE 3.14` row** — drop the bracketed tag, or teach `image_audit` to skip a tag whose row is
  marked removed
- **`3.2` vs `3.5`** — before/after split as briefed, or one figure and a deleted row
- **Rule the 12 callout families**, then the NOTE per-block pass (133 blocks, four destinations)
- **Nav `<details>` carry no `data-reveal`** — §25.12 exists because one untyped `<details>` slipped
  through
- **Selftest-coverage gate** — offered, not built: a gate that fails when a root instrument cannot
  run at all. Same shape as the roster coverage added to `session_versions`.

## Ruled, not yet applied
- §2 Learning Objectives vary — checkboxes in 14 of 16 (**L01 and L15 have none**), seven lessons
  embed an extra coloured callout in four colours, three icons, counts 6–11. Authoring, not CSS.
- Three of L12's 🏆 INSIGHT blocks are byte-count reports and S94 sends those to STILL GREEN.
  Classified by glyph+paint, so the generator cannot see it.

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12–14" becomes **obsolete** under the six-pill rail — retire, don't argue ·
`css/book.css` has 172 colours and zero custom properties (`build_palette --css` emits them
ready) · gradients 134 instances, unruled · **Consolas: 15 declarations, all with a fallback,
zero bare — RE-VERIFIED by independent parse in S110, the note is CORRECT.**

## Bench (need the robot)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED.

---

# ⏰ IMAGES — SEPTEMBER 8 IS FIVE WEEKS OUT

**18 outstanding of 145.** Six due in week one, all briefed. The visual arc is good work and is NOT
on a clock. The images are.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

**After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE and run
`book_gates` THERE before presenting md5s.** The working tree cannot see class re-spelling by
construction (S108).

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file in the same list as repo files.** S110: three preview HTMLs sat in
   the outputs root beside repo files — the S103 drag-in shape — and were moved out.
3. **Never produce PUSH_ME_*.md or MD5_*.txt.** Checksums and instructions go in the CHAT ONLY.
4. `going_deeper.html` belongs at the repo ROOT, not in `lessons/`.
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).** S110 shipped
   `pill_sweep` without it and `--check` went red for three pushes.

---

# PUSH LIST FOR THIS SESSION'S CLOSE

| Action | File | Note |
|---|---|---|
| upload | `ZUMO_S111_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | **regenerate LAST**, versions EMITTED not typed |
| **delete** | `ZUMO_S110_HANDOFF.md` | §12.2 — gate 28 enforces exactly one |

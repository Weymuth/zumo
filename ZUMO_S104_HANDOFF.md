# ZUMO — S104 HANDOFF (written at S103 close · paste at top of Session 104)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it and
   checks the header, the `Current:` field and the newest changelog entry against each other.
   S103 found two defects a grep had missed for nine versions. §24.10, and now CONTROL F.
4. Run: `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --audit lessons/Lesson_*.html` ·
   `build_family_map.py` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `regex_audit.py --selftest` then `regex_audit.py` · `build_worklist.py --selftest` ·
   `font_stack_sweep.py --selftest` then `font_stack_sweep.py` ·
   `session_versions.py --selftest` then `session_versions.py --check` ·
   `site_parity.py --selftest` then `site_parity.py`.
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`, the gradient path was not
   exercised: `pip install cairosvg --break-system-packages` and re-run.
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5.** Also check `git ls-files` for strays — S103
    accidentally committed three of my own helper files because they sat in the same folder as
    the repo files. Deliverables now ship as `REPO_FILES/` with instructions OUTSIDE it.

---

# STATE

Fresh-clone verified at **`5de157f`**. Census **39,978**.
Bible **v8.90** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.34.5** · `lesson_inventory` **v1.1.2** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.12** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.19** · `site_parity` **v1.0** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`font_stack_sweep` **v1.0** ·
`going_deeper` **v01.1.1**.

Lessons: L01 v03.15.0 · L02 v03.7.0 · L03 v03.20.0 · L04 v04.15.0 · L05 v04.15.0 · L06 v04.19.1 · L07 v04.15.0 · L08 v04.14.0 · L09 v05.12.0 · L10 v02.11.0 · L11 v02.12.0 · L12 v01.14.0 · L13 v02.12.0 · L14 v02.16.0 · L15 v02.11.1 · L16 v02.7.0.

**40/40 gates · seven controls · PARITY.** No lesson file changed in S103; census unchanged.

---

# THE ONE THING TO CARRY OUT OF S103

**The delivery model was the constraint, and nobody had priced it.**

§26's repaint sat parked for five sessions as "too expensive." It was never too hard. It was
priced against a delivery model — paste the HTML into Canvas — that forces `style=""` onto every
element and makes every colour decision a sweep across sixteen files. DJ ruled S103 that the
lessons are a **website** that Canvas links to. The repaint becomes a stylesheet.

**Ask what a task costs BECAUSE OF a constraint, before asking whether the task is worth doing.**
A parked item may be parked behind something that was never itself examined.

**And the counter-lesson, twice, both mine:**

- I verified CONTROL G with `key in output OR value in output`. Values like `v1.0` appear
  everywhere, so almost anything would have matched — §24.8, a check that could not distinguish
  the two answers. The clean re-run immediately found a real gap.
- CONTROL G shipped with one exemption (`Syllabus`, "emitted under its filename") that was true
  of `--live` and **false of `--handoff`**. **An exemption that is not itself checked is a hole**
  — the exact defect class the control existed to catch, sitting inside the control. DJ: *"to be
  safe shouldn't it be in both places?"* It is, and G now has no exemptions.

---

# S103 WORK, BY LAYER

## Book / graphics

- **39 unsafe font stacks → 0.** 154 `font-family` declarations across 24 SVGs rewritten to
  `Arial, Helvetica, sans-serif` / `Courier New, monospace`. Visually neutral — those files load
  through `<img src>` and the browser was already falling back. Work-list local-fix backlog
  **54 findings / 25 files → 15 / 5**; every removed finding is a font finding.
- **`font_stack_sweep.py` v1.0 — NEW.** Five controls. Value-only rewrite: per-file assert that
  **no byte outside a `font-family` value moved**. Weight and style survive — Illustrator writes
  `font-weight: 700` beside `Arial-BoldMT`, verified in 1-10 and 8-1 before the sweep ran. A
  designer face in FALLBACK position is not a violation and is left alone.

## Canon

- **Bible → v8.90** (from v8.88).
  - **§27 NEW — THE BOOK IS A WEBSITE, NOT A CANVAS PASTE.** DJ ruling. Lessons live at one
    address; Canvas keeps quizzes, grades, syllabus, submissions and **links to the index, not to
    sixteen lessons**. Justification: `site_parity` compares repo↔Pages and **nothing ever
    compared Pages↔Canvas** — a re-paste that did not happen was invisible to all 40 gates.
  - **§24.12 NEW — generated artefacts are registered, and their filenames carry no session.**
    `GPT_WORKLIST.md`, `ZUMO_FAMILY_MAP.md`. Never hand-edited: if the output is wrong, the
    generator is wrong.
  - **v8.88's changelog entry backfilled** — §26.9 shipped in S102 and its changelog line did not.
  - **`Current:` repaired** — it read v8.79.1 while the header read v8.89, *inside the line the
    Bible designates as its one home*.

## Instruments

- **`session_versions` v1.9.1 → v1.12.** **CONTROL F** — Bible bookkeeping PARSED, not grepped;
  header, `Current:` and newest changelog entry must agree. **CONTROL G** — every registered
  artefact must appear in BOTH emitted blocks, no exemptions. Both proved against the real
  defects re-seeded exactly as found.
- **`build_worklist` v1.0 → v1.1** — writes `GPT_WORKLIST.md`; `--session` sets the stamp, not
  the name. Both stamped work lists retired (DJ keeps desktop copies).

---

# THE MIGRATION — measured at S103 close, not started

| | Measured |
|---|---|
| inline `style=""` attributes, 16 lessons | **25,036** |
| CSS declarations inside them | **~67,000** |
| share of lesson bytes | **44%** — 1.56 MB of 3.58 MB |
| `font-family` declarations | **2,828** in 8 stacks, **0 broken** |
| absolute `weymuth.github.io` links | **473** (relative 314, anchors 692) |

**Zero of the 40 gates enforce Canvas-safety** — verified, not assumed. The suite survives.

**RECOMMENDED NEXT (my pick, DJ asked me to choose): convert L01 alone, end to end.** One lesson
proves the stylesheet, proves the gates, proves it renders identically, and yields a measured
per-lesson cost before committing to fifteen more. **Open question for DJ at S104 open: one
stylesheet for the whole book, or one per lesson?** That is structural and not mine to rule.

**DO NOT SWEEP WHAT THE MIGRATION DELETES.** The 422 Consolas-first lesson code stacks were
proposed and **parked** — in a stylesheet they are one line.

---

# STANDING QUEUE

## Mechanical, measured

6 plain `href` · 4 dead alpha · 5 photo resolution/aspect · 5 staged files over the gate-37
ceiling (unreferenced, not fatal). **The 41-font item is CLOSED.**

## The paint arc — now cheap, but gated on the migration

1. Design the semantic set: 27 distinct 4px accents for 30 families; §8 documents 11. Not started.
2. Re-derive `BookComponentStandard` §5.0 from the five — **derive, never hand-patch**.
3. Gradients: 134 instances, 7 strings, 17 pages, 18 SVGs. **DJ has not ruled flatten-now vs
   flatten-with-repaint. Ask before sweeping.**
4. **`#f8f9fa` — 641 instances**, still the largest unruled surface. `#fffbe6` — 87.
5. Code-palette drifts: `#4ec9b6` **294** → `#4EC9B0`; `#f14c4c` **14** → `#D46554`.
6. **9 roster rows still not activated** — carried since S94.
7. **The mark library is still entirely unwired** — 41 marks, **0** references across 21 pages.

## Instrument work

- `pill_sweep` and `gen_part_banners` still have no selftest.
- `_ctm` still discards `rotate()`/`matrix()`; v1.19 refuses to measure rotated text rather than
  fixing it. **6 `<text>` across 4 files (5-07, 6-11, 8-1, 10-07) unchecked.**
- Re-run `regex_audit` after any parser edit.
- **Offered and not yet ruled:** a gate failing on any root file matching `PUSH_ME*` / `MD5*`.

## Images — the deadline path

**SEPTEMBER 8 IS FIVE WEEKS OUT.** Each lesson's Image Index Status column is the record
(`IMAGE_SHOT_LIST.md` is stale): **15 images + 3 videos** outstanding.

- **Cheapest real progress:** 5 L07 assets I can build — tab bar, Go-to-Definition menu,
  wrong-folder tree, two error states using **authentic GCC diagnostics** (verified reproducible
  in the sandbox). Clears L07 entirely. **This is my second choice for S104.**
- **Genuinely DJ's:** 2.5, 3.2, 3.4, 3.5, 3.6, 4.1, 4.3 + 3 videos.
- **4.3:** two or three 30 cm white hardboard tiles butted together, one black electrical-tape
  line, shot square-on so the seam shows.
- `Line_Rescue_Field_Ariel.jpeg` (599×333, 0.54× against §17.3b's 2× floor) and
  `Sample_Robo_Tile.png` — keepers per DJ, both RCJ artwork with unresolved provenance, both
  orphans. `9-3` credits Pololu; the pattern exists.

## Canon debts

§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit (DJ's stated big goal) · Maker batch ·
L01 VS Code multi-root step · Stage Two two blocks labelled `Learn/Insight` (L03:3636, L09:1342) ·
`PUSH_WORKFLOW.md` — **still unanswered: is the CLI-for-adds, Desktop-for-deletions split
Zumo-only or global?** · **`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied** ·
**robolore.com hosting — DJ, S103: "a later decision"; the 473 absolute links are the exposure.**

## Bench (need the robot)

Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED (11-02 publishes 25 cm/s; L11's own formula gives
24.38 at BASE_SPEED 150 — the ratio conclusion survives, the two ms figures do not).

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions**, where seeing the checkbox
is the point. **Never `git add .`** — that is how three helper files landed in root in S103.

```
cd /path/to/zumo
git add <named files>
git commit -m "..."
git push
```

**Verify every push by fresh clone and md5. Check `git ls-files` for strays. Then run
`site_parity.py`.**

---

# PUSH LIST FOR THIS SESSION'S CLOSE

| Action | File | Note |
|---|---|---|
| upload | `ZUMO_S104_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | **regenerate LAST**, versions EMITTED not typed |
| **delete** | `ZUMO_S103_HANDOFF.md` | §12.2 — exactly one handoff in root, gate 28 enforces it |

⚠️ The deletion is a separate checkbox in GitHub Desktop. After pushing: fresh clone,
`python3 book_gates.py` → **40/40**, `python3 session_versions.py --check` → **no
disagreements**, and `python3 site_parity.py` → **PARITY**.

# ZUMO — S102 HANDOFF (written at S101 close · paste at top of Session 102)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters**.
4. Run: `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --audit lessons/Lesson_*.html` ·
   `build_family_map.py` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `session_versions.py --selftest` then `session_versions.py` ·
   `site_parity.py --selftest` then `site_parity.py`.
5. **`flatten_alpha --selftest` needs `cairosvg`** — absent from a fresh sandbox and it RAISES rather than
   guarding, unlike gate 40's PIL. `pip install cairosvg --break-system-packages`. Not a repo defect;
   candidate for the same guarded-import treatment.
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`.
9. **A CLONE IS NOT THE SITE** (S100). Run `site_parity.py` after any push.

---

# STATE

Fresh-clone verified at **`63f38e2`**. Census **39,972**.
Bible **v8.87** · `BookComponentStandard` **v01.10.0** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.

Instruments: `book_gates` **v1.34** · `lesson_inventory` **v1.1.2** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.7** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.1** · `svg_layout_audit` **v1.16** · `site_parity` **v1.0** ·
`going_deeper` **v01.1.1**.

Lessons: L01 v03.15.0 · L02 v03.6.0 · L03 v03.20.0 · L04 v04.15.0 · L05 v04.15.0 · L06 v04.19.1 · L07 v04.15.0 · L08 v04.14.0 · L09 v05.12.0 · L10 v02.11.0 · L11 v02.12.0 · L12 v01.14.0 · L13 v02.12.0 · L14 v02.15.0 · L15 v02.11.1 · L16 v02.7.0.

**40/40 gates. Census unchanged — NO LESSON FILE WAS TOUCHED IN S101.** `site_parity` PARITY at open.

---

# S101 WAS A RULINGS SESSION — NINE DECISIONS, ALL IN `ZUMO_SUPER_BIBLE.md` §26.8

**§26 is UN-PARKED and RULED.** Read §26.8 first; it is the whole session. §26.1–§26.7 are deliberately
unedited so the archaeology of how it was settled survives.

1. **Heritage Blue = RoboLore's five.** `#0B1A2E` · `#3D5266` · `#7B6240` · `#C9A463` · `#F5F2E9`.
   DJ stated them himself, so §26.1 cites DJ and not an uncommitted file. All ten published ratios
   recompute to **0.018 total error**; navy's re-derived title contrast lands on **12.75**, the
   standard's own pre-S91 figure — a fifth independent test.
2. **A correction to §26.2's framing, recorded in §26.8(3).** `BookComponentStandard` §5.0 is NOT
   arithmetically sloppy — its 11.05 / 6.36 / 5.11 reproduce exactly against its own tints. The case
   rests on provenance only. Saying otherwise was a wrong finding and cost 3×.
3. **Brand/semantic SPLIT.** Heritage Blue governs branding and page-level structure; a separate
   functional set governs the callouts. Already RoboLore canon — `InstructionalGraphicStandards` §6
   names **callouts** explicitly. **§5's seven-role table retires**; §5.0.1's band ramp survives.
4. **The semantic set is UNRULED, not forbidden.** §7 is scoped to code graphics. **Purple was rejected
   from the BRAND system only** — the book's 136-block `#9b59b6` survives by default.
5. **Forge Red `#D46554` is a SIXTH colour.** Danger. §22's `#f14c4c` retires. Warning `#CCA700` and
   Danger stay **distinct states**.
6. **NO GRADIENTS ANYWHERE.** Retires §6.2, §6.2a, §6.4's title block, §8's second Checkpoint form.
7. **Challenge-card headers → bronze `#7B6240` + parchment `#F5F2E9`, 5.12:1.**
8. **Repaint scope C: brand layer only.** All 1,048 callouts untouched.
9. **§18.2's star spec was stale and is corrected.**

---

# THE STARS ARE ALREADY DONE — VERIFIED, NOT ASSUMED

All 16 `images/spiral_star_*.svg` already conform to `BookComponentStandard` §9: fill `#7B6240`,
number `#F5F2E9` as vector paths, **zero gradients, zero trace of the retired gold**. DJ's uploaded
`spiral_star_14.svg` is **byte-identical to the live file** (md5 `cdc054f9e3f28ca69f5b5da77e3b4672`).

**§18.2 described an asset that no longer existed** — gold gradient `#FFD34D → #F5A623`, `#1a5276`
number. Corrected. The standing §18.2-vs-§9 canon debt is CLOSED in §9's favour, with no judgement
call needed: the no-gradients ruling decides it.

The name "spiral" is inherited from §18.1's Saxon-spiral METHOD. The mark is not spiral-shaped.

---

# THE GRADIENT SWEEP — MEASURED, NOT STARTED

**7 distinct strings, 134 instances, 17 pages, plus 13 referenced SVGs.** Seven strings is a GENERATE.

| Count | String | Construct |
|---|---|---|
| 87 | `135deg, #7d5283, #9b6a9e` | challenge-card headers |
| 33 | `to bottom, #1a5276 0%, #2e86ab 100%` | nav bar + title block, 2/lesson |
| 4 | `to right, #e8f5e9, #c8e6c9, #e8f5e9` | milestone banner (§8 type 5 form 2) |
| 4 / 3 / 2 / 1 | four one-offs | scattered |

Zero in `index`, `newproject`, `timer`, `tutor`.

**It does not have to wait on the palette** — each can flatten to its own dark stop (`#1a5276`,
`#7d5283`) and repaint later. That is exactly what the graphics chat did in S100, flattening SVG
banners to flat `#0B1A2E`. **The six gradient SVG banners already on the queue are now 13.**

**DJ has NOT ruled the flatten-now-vs-flatten-with-repaint question.** Ask before sweeping.

---

# THE CODE PALETTE ALREADY CONFORMS — A FIND NOBODY WAS LOOKING FOR

Measured against `InstructionalGraphicStandards` §7:

| Token | §7 | Book | Live | |
|---|---|---|---|---|
| Editor bg | `#1E1E1E` | `#1e1e1e` | 799 | exact |
| Syntax blue | `#569CD6` | `#569cd6` | 2,565 | exact |
| Syntax green | `#6A9955` | `#6a9955` | 789 | exact |
| Syntax orange | `#CE9178` | `#ce9178` | 683 | exact |
| Function yellow | `#DCDCAA` | `#dcdcaa` | 9 | exact |
| Type cyan | `#4EC9B0` | `#4ec9b6` | **295** | drift, one digit |
| Error red | `#F44747` | `#f14c4c` | **14** | → `#D46554` by ruling |

Five of seven exact with **no coordination** — both converged on VS Code Dark+. Two more are live and
**unnamed by §7**: preprocessor `#c586c0` (50), numbers `#b5cea8` (2,264). §7's token list is
narrower than the book needs.

---

# THE BOUNDARY IS LEAKIER THAN THE STANDARD SAYS — THE SESSION'S REAL FIND

`InstructionalGraphicStandards` §6 draws brand and instructional as separate layers. **They touch.**
The page colour is brand; card interiors are instructional; changing the first breaks the second.

- **`#f8f9fa` — 641 instances.** A COOL grey on what will be a WARM page. **Larger than every surface
  ruled this session put together, and nobody had looked at it.** Reads fine on today's `#fafafa`
  because both are neutral; will not on Parchment.
- **`#fffbe6` — 87 instances.** The Work-in bar, exactly 1:1 with the card headers, so one generate.
  DJ flagged this one by eye.

Both are card-interior work — the layer scope C deliberately leaves alone. **They are the reason
scope C is not as clean a boundary as it sounds.**

---

# UPSTREAM EDITS DJ OWES ROBOLORE (authorised, not done — private repo, not reachable here)

- `InstructionalGraphicStandards.md` §7 — currently states error red must not be presented as a
  RoboLore brand colour. Forge Red contradicts that.
- **Eight files assert the palette is FIVE**: `ColorPalette.md`, `ColorPaletteValidation.md`,
  `robolore-colors.css`, `README.md`, `HERITAGE_BLUE_UPDATE_NOTES.md`, `CODEX.md`,
  `VisualIdentity.md`, `InstructionalGraphicStandards.md`.
- §26.5's filing hazards **still stand for everything except §26.1**. DJ stated the five himself, so
  that one ruling cites him. Every other claim in §26 still cites uncommitted files.

---

# STANDING QUEUE

**The paint arc, in order:**
1. **Design the semantic set.** 27 distinct 4px accents live for 30 families; §8's roster documents 11.
   This is the design work and it is NOT started. Unruled space, not forbidden space.
2. Re-derive `BookComponentStandard` §5.0 from the five — **derive, never hand-patch** (that is S91).
3. The gradient generate (7 strings).
4. `#f8f9fa` (641) and `#fffbe6` (87).
5. The two code-palette drifts.
6. **9 new roster rows still not activated** — carried since S94.
7. **The mark library is still entirely unwired** — zero references to `images/marks/` across 21 pages.

**Instrument work, carried from S100 and still the highest value:**
- **Re-derive `GPT_WORKLIST_S99.md` by render.** Its ordering comes from `svg_layout_audit`'s bad
  text-width estimator (10-02 listed at 81, measures 16; 6-04 and 6-05 verdicts FLIP). **The graphics
  chat is working from it.**
- Fix `svg_layout_audit`'s estimator + 2× boundary bug (v1.16 → v1.17).
- Fold the under-the-box guard into `flatten_alpha` as a refusal.
- Guard `flatten_alpha`'s `cairosvg` import.
- `pill_sweep` and `gen_part_banners` still have no selftest.

**Images:** `L06_GRAPHIC_6-05` still HELD — DJ's Illustrator round-trip destroyed both arrows
(markers dropped, paths collapsed to zero-length movetos); **ask what the viewBox and text-count
changes were meant to do before rebuilding.** · six gradient SVG banners (now folded into the 13) ·
5 staged files carry plain `href` (gate 39 lists them) · 26 orphan images · `images/Archived Images/`
has a space in the name · font-stack §17.3b unruled across 25 files.

**SEPTEMBER 8 IS FIVE WEEKS OUT.** Image shot list **21 of 22 outstanding** — the long pole, and
camera work nobody else can do. Syllabus schedule blocked until ~Aug 24. Grid ⭐ list still reads
L03/L06/L07/L08/L09/L12 with L13 deliberately unmarked pending a ruling.

**Canon debts:** Bible §18.2-vs-`BookComponentStandard` §9 — **CLOSED S101**. §21.1's thresholds live
only in `book_gates.py` · §25.6 header example · §25.10e misfiled · challenge-card redesign Part B ·
difficulty-progression audit (DJ's stated big goal) · Maker batch · L01 VS Code multi-root step ·
Stage Two (S95) two blocks labelled `Learn/Insight` (L03:3636, L09:1342).

**Bench (need the robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS · cm/s at a stated BASE_SPEED.

---

# ON HOW S101 WENT

**Nothing rendered differently and a five-session deadlock closed.** §26 had been parked since S93 and
was blocking the entire paint arc; it is ruled, and the ruling came from DJ stating the values, which
dissolved the citation problem the park was built on.

**Two of my own errors, both caught in-session and both worth the pattern:**
- I framed `BookComponentStandard` §5.0's contrast table as suspect. **Control-run first: its numbers
  reproduce exactly.** I had compared its tint contrast against a page contrast — two different
  measurements. §24.8, and it would have been a wrong finding at 3× cost.
- I recommended bronze; DJ read it back as brass. **The record was corrected in the moment rather than
  let stand**, because a ruling attributed to the wrong recommendation is a ruling that gets reverted
  later as a bug.

**The specimen was the right instrument and the table was the wrong one.** Both header candidates PASS
contrast, so the numbers could not settle it — the question was rhythm and page budget. DJ chose brass
on sight, then reversed to bronze once the 2–6% rarest-colour budget was read back. **A number that
cannot distinguish the two answers is not evidence** (§24.8, applied to a design call).

**The largest find was not ruled on at all:** `#f8f9fa`, 641 instances, cool grey on a warm page.
Everything argued about this session was smaller than the thing nobody had looked at.

---

# PUSH LIST

| Action | File | Note |
|---|---|---|
| upload | `ZUMO_SUPER_BIBLE.md` | **v8.87** — §26 un-parked, §26.8 new, §18.2 corrected |
| upload | `ZUMO_S102_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | regenerate LAST, versions EMITTED not typed |
| **delete** | `ZUMO_S101_HANDOFF.md` | §12.2 — exactly one handoff in root, gate 28 enforces it |
| **delete** | `Unconfirmed 734708.crdownload` | 84,702 B, a stale download of `book_gates.py` (coverage 176/24 against live 174/26). Unreferenced. **Neither gate 28 nor CONTROL E can see it** — not `.md`, not `.py`. DJ approved the deletion S101. |

⚠️ **Both deletions are separate checkboxes in GitHub Desktop.** After pushing: fresh clone, confirm
`python3 book_gates.py` returns **40/40**, and run `python3 site_parity.py` — it should report PARITY.

#### 25.10e THE RETIRED-NAME LIST IS NOT THE ANCESTOR DETECTOR (v8.63 — NEW, S77)

**§25.10b says to scope a conversion by grepping §25.2's retired-name list. That is necessary and it is not sufficient.** L07's sweep returned **zero** across all five retired names — and L07 had **two** live ancestor blocks: a 6-item *Self-Assessment* (Technical Skills) and a 7-item *Knowledge Check* (BC03) sitting under BC03's own live name. Trusting the empty sweep would have read L07 as an authoring job like L06 and written four new blocks **on top of two that already existed.**

**The retired list only ever caught names somebody thought to retire.** It cannot catch a block whose name was never bad enough to notice. The list of unswept ancestors first recorded here was itself unverified and is corrected at §25.10f — read that before using it to scope anything.

**THE RULE — scope a conversion by READING §10, not by grepping it.** The retired-name sweep is one input. Before concluding a lesson has no ancestor, walk every `<h3>` in the exit region and ask of each one *what job does this block do*, not *what is it called*. A checklist of ☐ items is a Technical Skills ancestor whatever its heading says; a numbered list with answer reveals is a Knowledge Check ancestor whatever its heading says. **§25.10b's empty result is a lead, never a verdict** — which is §24.6c applied to the sweep that scopes the work rather than to the gate that checks it.

**AND THE CONTROL RUN GOES ON THE SWEEP TOO.** L07's zero was only trustworthy because the same grep was run across the unconverted lessons and *did* fire (L09, L10, L11, L14). A sweep that returns nothing everywhere is indistinguishable from a broken pattern.

**COROLLARY — A DISPLACED BLOCK IS PARKED, NOT DELETED (DJ ruling, S77: "Don't retire them, put them somewhere for us to evaluate later").** `ZUMO_PARKED_EXIT_ITEMS.md` at repo root holds items that were live and were displaced, recorded verbatim with provenance and with their replacement mapped alongside so the later call is a comparison, not a re-derivation. It is the inverse of `ZUMO_SHELVED_CARDS.md`, which holds proposals that were never live — **do not merge the two files.**

**A DISPLACED ITEM THAT CONTRADICTS ITS OWN LESSON IS NOT CARRIED FORWARD.** L07's Self-Assessment asked students to tick *"Write include guards for a header file"* while §3.6 files include guards under 📘 *The Old Way* and teaches `#pragma once` instead. That item was never achievable as written (§25.10) and it does not enter BC02; the parking file records both it and the honest recognition-shaped version, should a later pass want the skill back.

# ZUMO SUPER BIBLE v8

**Bible version: v8.105** — increment on EVERY substantive edit (moderate change → `v8.x`; minor fix → `v8.x.y`; a new major re-baseline → `v9`). **Filename is now unversioned: `ZUMO_SUPER_BIBLE.md`** — the version lives ONLY in this line, never in the filename (this avoids a fresh chat misreading a filename number as the version). Current: **v8.105** (v8.105, S116, moderate — **§25.10i NEW: A PAST-TENSE CHECKLIST RUNG IS NOT AUTOMATICALLY A DUPLICATE OF THE OBJECTIVE IT ECHOES.** L11 is the ELEVENTH conversion. Its *Skills Checklist* held seven rungs against six §2 objectives, and four of the seven restate an objective in the past tense — *"I converted encoder counts…"* against *"Convert encoder counts…"*. Ruled by a SCORED PAIRWISE DIFF of all 7 × 6 combinations rather than by eye: the four score **0.55–0.73** against their partner objective and the three survivors score **0.31–0.38** against their nearest, and the builder asserts `min(dup) > max(keep)` so a wrong pairing cannot pass. The four are PARKED with their pairing table, not deleted (S77). Rungs 4/5/6 are bench observations no objective covers and become BC02's **I have…** group per §25.10a/b. **The open question is recorded and NOT ruled:** the past tense asks *did you do it* where the objective asks *can you do it*, and if that distinction is worth keeping, all seven fold and the student ticks the same claim twice. **Also recorded: the achievability edge.** Folded rung *"Run 7E and watched the stopwatch version fail on a tired battery"* now sits behind the Mark-done lock and needs a TIRED BATTERY to earn — §7E mandates the run, so the lesson plants the rep, but this is the §25.10c shape where an unearnable item makes the lock unreachable. BC01 had NO ancestor (zero pre-§6 reveals, zero `check`, zero TRY IT): five items authored and §-ordered §3.1→§3.2→§3.3→§3.4→§3.5, each citation READ and verified to contain its answer. BC03 migrates all five *Reflection Questions* verbatim — asserted, not eyeballed — and authors the five answers and the five §-citations the ancestor never had. BC04 has no ancestor either; three prompts authored, no reveals, and the Engineer's Log survives as its own block after it (S80 precedent). **THREE BASELINES MOVED, EACH CONTROLLED BOTH WAYS:** §27.11 645/2,365 → **644/2,362**, diffed by SELECTOR — exactly one gone (`.div-bg-eafaf1`, the checklist's green box, 3 declarations, and the −3 IS that rule), **zero born, zero altered, so NO class RENAME this time unlike S115**; §21 coverage 230 → **235**, sole delta `BrainGear_Incomplete.png` 45 → 50; family map 1053 → **1057**, controlled at an identical generator version with exactly ONE family moving, BRAIN CHECK 40 → 44, the other 29 byte-identical. After the moves a deleted `color: white;` still FAILS, a deleted callout still FAILS at 1056/1057, a broken image ref still FAILS. **TWO PROCESS FAILURES, BOTH MINE.** (1) The 4/3 checklist split was HAND-PREDICTED and asserted — and **the assert failed**, because the normaliser stripped only *"I can/I have"* and read two real duplicates as unique; re-derived rather than tuning the normaliser to match the guess, which would have been writing the gate to the sweep. (2) A control run misfired **three times** — the injection never landed and the gate printed PASS against an unmodified tree, and that PASS was nearly recorded as evidence. **§24.6b is not "assert something changed" but assert the injection landed in the shape intended, and a control that dies before it writes is a control that never ran.** `book_gates` **v1.44.2**, `build_family_map` **v1.3.4**. Applied S116: L11 **v02.18.0** (moderate — the page renders differently, so both §5b homes move). Census 40,206 → 40,391 [lesson_inventory.py].) Prior: **v8.104.1** (v8.104.1, S115, minor — an INCOMPLETE PUSH: nine lessons rewritten by the CSS class rename were omitted, caught only by running the gates in the pushed clone. Nine MINOR bumps.) Prior: **v8.104** (v8.104, S115, moderate — **§25.2a NEW: one predicate for "converted", and the converted SET is NAMED not counted; DJ ruling: L14/L16 exempt, L10/L11/L12/L13/L15 convert; L10 is the tenth conversion. `book_gates` v1.44.1, 48 gates. Census 40,206.) Prior: **v8.103** (v8.103, S114, moderate — **§24.14 NEW: EVERY CALLOUT BLOCK RESOLVES TO A FAMILY.** The rule gate 47 has enforced since S112 finally has a section. **The rule was never missing — only its home was.** Gate 47 enforced it, `book_gates.py` carried a full comment block on why, and `ZUMO_FAMILY_MAP.md` recorded the whole S112 derivation. What did not exist was the numbered section here: §24 ran 24.13 straight to 24.15. v8.101 logged that as a debt rather than closing it — the same shape as §21.1's thresholds living only in `book_gates.py`, and the same §24.2 failure: **a rule canonized without its home holds only where someone happens to look.** The section states the ORDER — **family from CONTENT; the mark and the colour are OUTPUTS** — and records why: 252 of 1,048 blocks were resolved by HEX until S112, so a repaint moved the ground under a quarter of the map, and thirteen L12 blocks wearing one glyph and one green were three families with a correct STILL GREEN ruling **overridden by paint**. It also states plainly that the printed denominator is a **frozen baseline, not a count**, that `assigned 1049 / 1048` is therefore a line that reads like a count and is not one, and that moving the literal is legal only after a control run proves the per-family delta — because the total alone is not evidence. Transcription of an enforced rule, not new canon: no ruling changed, no lesson file changed, census unchanged at **40,015**.) Prior: **v8.102** (v8.102, S114, moderate — **§12.2 THE HANDOFF'S NUMBER IS GATED, AND THE RULE IT ENFORCES WAS ALREADY CANON.** §12.3 step 4 has said *write `ZUMO_S<N+1>_HANDOFF.md`* since v8.24, and §12.2's own `git rm ZUMO_S<N-1>_HANDOFF.md` line agrees with it. **Both were violated in consecutive sessions anyway.** the prior session wrote its OUTGOING handoff into the INCOMING handoff's filename, editing that file in place across three commits with its STATE block updated each time (`893b8b6` → `4558257` → `8ae3857`) while its title kept naming a session that had already run — so the incoming handoff under its correct name **never existed**, and the text actually pasted at session open matches no committed version of any file. The convention was then inferred from that one defective example rather than from this Bible, and the outgoing handoff went up under the wrong number. **The session number then drifted twice more the same day**, disagreeing across four hand-typed homes. **DJ caught both by reading the numbers.** `book_gates` **v1.42.2 → v1.43.0**: gate 28 now parses the number out of the FILENAME, out of the `# ZUMO — SNN HANDOFF` title and out of the *"paste at top of Session N"* clause, fails when any two disagree, and fails **loudly rather than skipping** when the title shape is missing. Control-run four ways, and two of the four are the real historical defects, not synthetic ones. **What it replaced could not see any of it:** the gate asserted only that exactly ONE handoff exists, which is satisfied by a file renamed `ZUMO_S999_HANDOFF.md` — measured, and it PASSED. **§24.2 arriving late — a rule canonized without its gate holds only where someone happens to look — and §24.8: if the answer were the opposite, the old gate looked identical.** No lesson file changed; census unchanged at **40,019**.) Prior: **v8.101** (v8.101, S114, moderate — **§24.15 NEW: A DRAFTING MODEL CANNOT COUNT THE BOOK.** `GPT_BRIEF_FORMAT.md` was written at S112 and committed to the repo root, where nothing gated it, nothing linked it and no roster named it — the §12.2 shape exactly, a standing rule stored somewhere it will drift silently. Moved here verbatim in substance and **the file is deleted**. The rule: every brief to a drafting model opens with a MEASURED FACTS block, each number naming the instrument that produced it (§24.10), and a task whose answer depends on a number not in that block is either given the number or not sent. **Also recorded, not fixed: §24.14 does not exist.** Gate 47 ships printing `§24.14 every callout block resolves to a family` against a section number this Bible has never carried — the same debt shape as §21.1's thresholds living only in `book_gates.py`. **Also S114, and it is the entry's real finding: THE FAMILY MAP'S DENOMINATOR IS A FROZEN BASELINE, NOT A COUNT.** L03's `[IMAGE 3.4]` placeholder became a real WHAT YOU SHOULD SEE callout carrying a §22 terminal block, and the generator printed **`assigned 1049 / 1048`** — a line that reads like a count and is not one, because 1048 was a literal. Controlled at the identical generator version against the pre-edit tree: the only two lines that move are WHAT YOU SHOULD SEE 27 → 28 and the total, with the other **29 family counts byte-identical**, so the delta is the one added block and nothing else. `build_family_map` **v1.3.1 → v1.3.2** moves the literal to 1049. **Parsing the true total and asserting the baseline separately is deliberately NOT done — it changes what gate 47 means, and that is DJ's ruling.** Until it is ruled, every callout added anywhere in the book fails gate 47 until that literal is edited by hand. Applied S114: L03 **v03.24.1 → v03.25.0** (moderate — a planned figure became live content, so the page renders differently and both §5b homes move). Census 40,013 → 40,019 [lesson_inventory.py].) Prior: **v8.100** (v8.100, S112, moderate — **§27.14 NEW: every link and every id resolves.** 1,237 links and 705 ids across twenty pages had no gate at all; gate 46 is parser-based and control-run on four defect shapes. Its own lesson: **where a gate sits in the file is part of the gate** — appended below the summary it printed PASS after `ALL GATES PASS` and never ran on a failing tree.) Prior: **v8.99** (v8.99, S111, moderate — the challenge-card header takes the §9 band `#7A5905`, superseding v8.87's Antique Bronze; the band palette is re-ruled at EIGHT bands with `build_palette.py` v1.1; `[IMAGE 2.5]` retires into a live code block; and the S111 handoff's *"gradients unruled"* line is corrected — v8.87 banned them and the ban stands.) Prior: **v8.98** (v8.98, S109, moderate — **§24.13 NEW: RE-DERIVE, DO NOT RE-READ — AND A LIST IN PROSE IS NOT THE LIST.** DJ ruling, on being told a taxonomy had been checked three times and was still wrong: *"So when I say double check you don't double check?"* **Re-reading is not checking** — a second look at the same artefact is the same instrument run twice, and a list with a member missing looks complete from the inside (§24.8, failed). A check is a DIFFERENT METHOD or an ASSERT against a number the artefact cannot supply. **The case:** a 17-family consolidation was computed in code, printed `CORE CONCEPT 60` with `unaccounted: 0`, then HAND-TYPED into a chat message as an 11-row table — INSIGHT's 60 blocks dropped in the retyping — and the next build read the chat message rather than the verified structure. Three passes found nothing because all three were re-readings; one line caught it, `assert tot + rem == 1048`. **This is the v3.0 ghost wearing a different noun:** §12.6 forbids hand-typing a VERSION and §24.10 requires a count to name its instrument, but neither covered a TAXONOMY, and the gap was enough — so the rule is stated on SETS. Also S109, and separate from the ruling: six INSIGHT blocks carrying the canonical magnifier wore five non-canon paints across L02/L03/L07, three of them borrowing OTHER families' canon (TIP's `#f0f7f0`, What-You-Should-See's `#d1ecf1`, Checkpoint's `#4caf50`); repainted to `#e9f7f5`/`#2da99d`, canon 31 → 37, three stylesheet rules died and all three had ZERO Bible mentions. `book_gates` **v1.39.2** — gate 27.11's label DERIVED from its own constants after shipping stale at 664/2,434 against a live 660/2,418, and **`BAND_END`** names the §10+ section band, previously typed literally in ELEVEN places; control-run by flipping it to DJ's Steel `#708BAF`, which fires **FOUR** gates — §25.10h, §4.5, §4.5a and §5.1 — where the S108 handoff recorded three and missed §5.1's `GEOM_BASELINE` keys. Applied S109, all MINOR (callout paint only, visible banners unchanged per §5b): L02 **v03.10.2** · L03 **v03.23.2** · L07 **v04.20.2**. Census unchanged at **40,025**.) Prior: **v8.97** (v8.97, S108, moderate — **THE BANNER ARC IS APPLIED.** §6.5's LOCKED *"Cap KEEPS the leading icon"* is **SUPERSEDED: no icons on any of the 237 caps**, bonus block included; all 237 carried a leading emoji and now none does, verified by DOM lookup rather than regex. **NEW §6.5b** — every cap is an EYEBROW above a HEADLINE, *headline = the most descriptive string available, eyebrow = everything before it*; 189 of 237 carry an eyebrow, the other 48 are Glossary / Quick Reference / Figures × 16. The fence rule extends §6.8a: fence = the eyebrow's name after the middot, else the headline, so the fence stays DERIVED — `_fence_title()` knows both shapes and was control-run against a converted lesson and a legacy one. **NEW §6.5a-T** — type treatment E: Inter served the way the front door already serves it, `.page` line-height 1.7→1.65 and `#333`→`#1d1d1f`, and the Windows-only Segoe UI stack RETIRED after eleven sessions in which `font_stack_sweep` reported 0 rewrites because it never opened `css/book.css`. **§4.5's derived family mark is superseded**, word retained, `gen_bonus_banner` v1.3.0, its mark assert INVERTED rather than deleted. **§6.9: `image-index` → `figures`** in three passages. **§6.5 Box CONFIRMED and unified** — the panel had shipped in two forms split at the L09/L10 seam in all five colour groups, invisible to every gate; 104 panels moved and five duplicate rules collapsed. `book_gates` **v1.39.0**, `font_stack_sweep` **v1.1.0**, `gen_bonus_banner` **v1.3.0**, `going_deeper` **v01.2.0** with six anchor ids at last. **THE RAMP WAS PILOTED AND REVERTED:** §5.0.1's Heritage Blue band ramp cannot be applied to one lesson, because five constructs are byte-compared across all sixteen — lesson strip, hero, PART dividers, bonus cap, FINISHED EARLY box — and three gates hard-code `#6c757d`. It is a book-wide change with instrument work FIRST.) Prior: **v8.96** (v8.96, S106, moderate — **§27.12 + §27.13 NEW: THE MIGRATION'S TWO UNGUARDED INVARIANTS.** **§27.12** — a page that links `css/book.css` carries NO inline `style=""`. Measured: pasting one `<p style="color: #ff00aa; font-size: 13px;">` into L05 left **all 43 preceding gates green**, and the element renders correctly while doing it, so nobody looks. Every hand-edit, pasted block and AI-suggested snippet re-opens the hole the migration closed. Scope keyed on the `<link>`, the §25.6a rule, so the four tool pages' own inline styles stay out. **§27.13** — `css/book.css` must regenerate byte-identically from the lessons. This is the guard on §27.8a/b: stop after *regenerate* and skip *apply*, and 46 class names keep their spelling while changing meaning, invisible to gate 41. **Gate 43 cannot cover it, because §26's repaint MOVES gate 43's baseline by design and a moved baseline is a spent gate**; §27.13 re-derives instead of remembering, so a repaint does not spend it. **Complementarity measured in both directions:** a hand-deleted `color: white;` fires 43 and is INVISIBLE to 45 (build_css reads the stylesheet through `expand_classes` — §24.8); one element retyped to a *different resolvable class* leaves all 43 green and fires 45. Neither subsumes the other. **`strip_inline --verify` was offered and NOT added**: it computes gate 41's assertion a second way and never fired independently of it across four controls — an assert that cannot fail is not evidence. `book_gates` **v1.38, 45 gates**.) Prior: **v8.95** (v8.95, S105, moderate — **§27.11 NEW: THE STYLESHEET IS BASELINED, BECAUSE THE MIGRATION MADE IT A SINGLE POINT OF FAILURE.** A declaration used to live in 25,036 places; it now lives once, and **nothing validated `css/book.css` at all**. `build_css --check` cannot: it rebuilds from lessons read through `expand_classes`, which reads the stylesheet — damage it and the expansion is damaged identically, so `--check` says *current*, exit 0. **Measured: deleting one `color: white;` left all 42 gates green and `--check` clean** while the lesson strip's links went dark-on-dark in all sixteen lessons. **Gate 43** baselines 664 rules / 2,434 declarations / a body digest; control-run against a dropped declaration, a changed hex and an injected rule, loud on all three, silent on a generator version bump. **The baseline is meant to move** — §26's repaint moves it, as §21's moved 218→223. General lesson: **consolidation creates a single point of failure, and the instrument that built the artefact cannot be the instrument that guards it.** `book_gates` **v1.37, 43 gates**.) Prior: **v8.94** (v8.94, S105, moderate — **§27.10 NEW: THE BOOK IS DOMAIN-AGNOSTIC.** 478 absolute `href`/`src` attributes plus **18 JavaScript `img.src` string assignments** — 496 total, all in the sixteen lessons — made relative-to-the-page. **The 18 JS refs were invisible to every attribute-shaped search** and surfaced only because the sweep's REMAINDER was audited rather than assumed. Seven off-site references remain and must (Google Fonts 4, template zip 2, jszip CDN 1): domain-agnostic means the book does not name its own host. The going_deeper gate no longer allow-lists the absolute form — it derives expected depth from the page and was control-run against both regression shapes. **NEW gate 42** fails on the domain appearing anywhere in any page in any syntax — it exists because reverting one image `src` to absolute passed all 41 preceding gates, measured by seeding it. `book_gates` **v1.36, 42 gates**.

### 27.13 The stylesheet must regenerate from the lessons, and that is the guard a repaint cannot spend (S106)

**GATE 43 IS SPENT THE MOMENT ITS BASELINE MOVES, AND §26'S REPAINT MOVES IT BY DESIGN.** §27.11
says so in its own words — *the baseline is meant to move*. That is correct and it is also the
hole: the repaint is exactly the operation that regenerates `css/book.css`, and the operator who
moves the three constants has, in that same commit, disarmed the only gate watching the file. What
must still hold afterwards is not a remembered number but a RELATION — the lessons and the
stylesheet describe the same book.

**GATE 45 ASSERTS THE RELATION BY RE-DERIVING IT.** It imports `build_css` (the S83 rule — import
the definition, do not re-implement it), regenerates in memory, and compares to disk. 0.4 s.
Because it derives rather than remembers, a deliberate regeneration does not disarm it: after a
repaint it is red until `strip_inline --apply` lands, and green the moment it does. **A red here
mid-repaint is correct, and it is the signal that the three-step sequence is unfinished.**

**THE TWO GATES ARE COMPLEMENTARY AND THIS WAS MEASURED IN BOTH DIRECTIONS, NOT ARGUED.**

| seeded defect | gate 43 | gate 45 | the other 43 |
|---|---|---|---|
| one `color: white;` deleted from `css/book.css` by hand | **FAIL** | blind | green |
| one element retyped to a DIFFERENT resolvable class | green | **FAIL** | green |
| `SOURCES` changed, regenerated, re-strip skipped | FAIL | **FAIL** | gate 41 also fires |

Gate 45 is blind to row one for the §24.8 reason §27.11 already records: `build_css` reads the
stylesheet through `expand_classes`, so damage propagates into the comparison. **Neither gate
subsumes the other. Keep both.**

**`strip_inline --verify` WAS OFFERED AND IS DELIBERATELY NOT A GATE.** It computes gate 41's
assertion — every class resolves to a rule — a second way, and across all four S106 controls it
never once fired independently of gate 41. Recorded here so it is not re-offered: **an assert that
cannot fail is not evidence.** Coverage is not the same as a second opinion.

### 27.12 A converted page carries no inline style, and until S106 nothing said so (S106)

**THE MIGRATION'S PREMISE WAS GUARDED BY NOTHING.** The whole point of §27.7–§27.9 is that a
declaration lives once. Pasting a single `<p style="color: #ff00aa; font-size: 13px;">` into
Lesson 05 left **all 43 preceding gates green** — and, worse, the element RENDERS CORRECTLY while
doing it. An inline style is not a broken thing that announces itself; it is a working thing that
quietly re-opens the hole. Every future hand-edit, every block pasted from an old lesson, every
AI-suggested snippet arrives in exactly this shape.

**SCOPE IS KEYED ON THE `<link>`, not on a list of filenames** — the same self-maintaining rule as
gate 41 and for the same §25.6a reason. `going_deeper.html` (7), `index.html` (1),
`newproject.html` (2) and `tutor/tutor.html` (7) carry their own `<style>` blocks and their own
inline attributes, and none of that is `css/book.css`'s business. A page enters this gate the
moment it is converted, and nothing has to be remembered.


### 27.11 The stylesheet is now the single point of failure, so it is baselined (S105)

**THE MIGRATION MOVED EVERY DECLARATION INTO ONE FILE AND LEFT IT UNGUARDED.** Before S105 a
declaration lived in 25,036 places across sixteen lessons; a corruption was local and visible.
It now lives once, in `css/book.css`, and until gate 43 **nothing validated that file at all.**

**`build_css --check` CANNOT VALIDATE IT, AND THIS IS §24.8 EXACTLY.** The check rebuilds from
the lessons read through `expand_classes`, which reads `css/book.css`. Damage the stylesheet and
the expansion is damaged identically, so the regenerated output matches the damaged file and the
check reports *"current"*, exit 0. **An instrument that reads its own output as input cannot see
its input change.** Measured, not argued: deleting one `color: white;` left **all 42 gates green
and `--check` clean** while `.link-bc-rgba2552` — the lesson strip's links — lost their colour in
all sixteen lessons, rendering dark on a dark gradient. Found by seeding it on the final check of
the session, three pushes in.

**GATE 43 HOLDS THE ONE THING NOT DERIVED FROM THE FILE IT CHECKS: a baseline.** 664 rules,
2,434 declarations, and a SHA-256 prefix of the body. Control-run against three shapes — a
dropped declaration, a silently changed hex, an injected rule — loud on all three, and silent on
a generator version bump because the digest deliberately excludes the generated header.

**THE BASELINE IS MEANT TO MOVE.** §26's repaint will move it, exactly as §21's moved 218 → 223.
Re-run `build_css.py`, then move the three constants in `book_gates.py` in the same commit. **A
baseline that never moves is a baseline nobody is checking** — and a baseline moved silently is
worse than none, which is why it lives in the gate file and not in a data file beside the
artefact it guards.

**THE GENERAL LESSON. Consolidation creates a single point of failure, and the instrument that
built the artefact cannot be the instrument that guards it.** Both halves were true of gate 41
(§27) and are true again here. Every future consolidation should be read this way before it
ships, not after. Lesson bytes 2,582,947 → **2,569,059**. Census unchanged 39,994; visible text identical in all twenty pages. All 16 lessons minor-bumped.) Prior: **v8.93** (v8.93, S105, moderate — **§27.9 NEW: THE HOLD RELEASED. ZERO INLINE STYLES BOOK-WIDE.** The four byte-exact-across-lesson block types (§6.5a strip 320 · §25.6 hero 96 + footer 16 · §6.8 PART dividers 192) converted in one pass. The book now carries **25,036 classes and no `style=""` attribute at all**. Released by measurement: the 624 attributes carry only **16 distinct strings**, each appearing an exact multiple of 16 (proof of book-wide uniformity), and **all 16 round-trip byte-exact** through the stylesheet — only true because §27.8c fixed declaration order and §27.8d fixed colon spacing. `strip_inline` **v1.1** adds `--include-held`, gated on a `roundtrips()` precondition that REFUSES and names offenders; CONTROL I proves both directions. Lesson bytes 2,638,947 → **2,582,947**. Census unchanged 39,994. All 16 lessons minor-bumped.) Prior: **v8.92.1** (**v8.92.1, S105, minor — §27.8d: DJ ruled ONE colon spelling for the generated stylesheet; spaced, which is 98% of the source and the only one the gates accept (unspaced broke five). Lessons byte-unchanged. `build_css` v1.2.1.** Prior entry: v8.92, S105, moderate — **§27.8 NEW: THE MIGRATION COMPLETES ITS SWEEP.** All 16 lessons converted: **24,412** inline attributes to classes against a 664-rule `css/book.css`, **624 held** (39 per lesson, every lesson) — 24,412 + 624 = **25,036**, the §27 census exactly. Zero unmapped, zero dead classes, 41/41 gates. Render identity proved by construction AND independently: 25,036 styled elements compared in document order, declaration sets identical, visible text identical bar one `<link>` per lesson. Census 39,979 → **39,994**. Lesson bytes 3,534,934 → **2,638,947**, 25% smaller. **Three ways a widened build bites, all measured:** (a) widening `SOURCES` renamed 57 of L01's 167 classes and **46 kept their spelling while changing meaning** — invisible to gate 41, so every converted lesson must be re-stripped whenever `SOURCES` changes; (b) `expand_classes` reads the stylesheet from disk and leaves an unresolvable class in place, so regenerating before restoring strands 74 L01 elements permanently — the order **restore → regenerate → apply** is forced; (c) `canon()` sorts while §4.5/§6.8/§25.6 assert authored order, which broke a whole class of gates at once and revealed a **fifth** held block type the S104 hold list missed (the §4.5 bonus banner) — fixed in the generator via `build_css.preferred()`, not by holding blocks until the gates went green. **`strip_inline.py` v1.0 NEW**, eight controls, the tool S104 did not commit; `build_css` v1.2; `session_versions` v1.14.1 after its own CONTROL A was found seeding a literal version string that expired on a bump. All 16 lessons minor-bumped.) Prior: **v8.91** (v8.91, S104, moderate — **§27.7 NEW: THE MIGRATION BEGINS, AND ONE LESSON PRICED IT.** L01 converted end to end: 1,111 of 1,150 inline attributes became classes, 39 held because three constructs are compared byte-exact across lessons (§6.5a strip, §25.6 header/footer, §6.8 PART dividers). **One stylesheet, not sixteen** — 689 distinct declaration strings, 92.5% of instances shared across lessons. **`lesson_inventory.expand_classes()`** so six CSS-reading gates keep working whatever a file's conversion state; **gate 41** because a mistyped class makes an element INVISIBLE where a mistyped inline style only made it wrong — proved by dropping L01's callout census 83→82 with all 40 gates green. Render identity asserted by construction, not inspection. Also S104: **L15's three figures retyped IMAGE→GRAPHIC** (§10 separate number spaces — the tag contradicted its own filename), and a book-wide sweep proved L15 was the entire class. **`image_audit.py` v1.1 NEW** replaces the hand-maintained `IMAGE_SHOT_LIST.md`: 20 outstanding of 145 planned. Its two false findings are recorded in the tool — a cross-lesson tag keyed to the wrong lesson, and ten "type mismatches" that were legitimate separate-number-space figures, killed by reading. **Five L07 figures built** from GCC diagnostics reproduced in the sandbox, clearing L07. `book_gates` v1.35.1 (41 gates), `lesson_inventory` v1.2.0, `build_css` v1.1, `image_audit` v1.1, `session_versions` v1.14, `site_parity` v1.1. L01 **v03.15.2** · L07 **v04.16.0** · L15 **v02.11.2**.) Prior: **v8.90** (v8.79.1, S92 close, minor — record only, no book change — **S92 CLOSE — TWO FAMILY RENAMES RULED, AND 📝 WAS FOUND DOING EIGHT JOBS.** DJ ruled **`✋ YOUR TURN`** to replace `📝 DO THIS NOW` and **`WHAT YOU SHOULD SEE`** as SEE's single name. ✋ is **unused book-wide, 0 occurrences**. `WHAT YOU SHOULD SEE` wins on zero label edits — 21 blocks already say it — and the Icon Guide's short form `SEE` retires; under Option C the label holds exactly one string, so a family with two names cannot ship, making the rename FORCED rather than cosmetic. *"Check for yourself"* was rejected: it reads as an instruction and collides with `✅ CHECKPOINT` (63 blocks). **NEITHER IS A GLYPH-WIDE SWEEP.** 📝 carries **82 blocks doing EIGHT jobs**: `DO THIS NOW` ~54 (in scope), **`MY PLAN` 20 (OUT)**, `WHAT YOU NEED BEFORE STARTING` 2, plus `DISCUSSION QUESTIONS`, `CODE SWAP`, `THE TUNING RITUAL`, `THE GREEN SURVEY`. 👀 likewise: 28 callouts, 21 bare in scope, 7 other constructs. **MY PLAN IS THE PSEUDOCODE STEP AND HAS TWO ENDS** — the lesson callout asks the student to plan in prose before any code, and **the Maker stamps a matching pseudo-code comment block into every generated `main.cpp` header, L01 excepted (recorded in `newproject.html`)**. Renaming it would break book/generator agreement, and a glyph-wide sweep would have done exactly that: YOUR TURN is *go do the thing*, MY PLAN is *write down what you'll do first*. MY PLAN is painted **plum `#f3e5f5`/`#9b6a9e`** and carries 📝 only by borrowing — the S92 borrowed-paint pattern on a different axis. Also found: **`WHAT YOU NEED BEFORE STARTING` exists on TWO glyphs**, 2 on 📝 and 2 on 📋. **Execute these renames only AFTER `BookComponentStandard` has the SEE / 🛑 / 🔬 rows** — renaming in the book first is S91's *ruling-applied-to-the-book-is-not-applied-to-the-canon* failure, the reason §5.1 was wrong for thirty sessions. **This entry exists because those rulings were taken after the v8.79 entry was written and initially lived ONLY in the session handoff — one session from being lost. A ruling reaches the canon or it did not happen.** 

v8.105, S116, moderate — **§25.10i NEW: A PAST-TENSE CHECKLIST RUNG IS NOT AUTOMATICALLY A DUPLICATE OF THE OBJECTIVE IT ECHOES.** L11 is the ELEVENTH conversion, and its *Skills Checklist* held seven rungs against six §2 objectives with four restating an objective in the past tense. **Ruled by a scored pairwise diff of all 7 × 6 combinations, not by eye:** the four score 0.55–0.73 against their partner objective, the three survivors 0.31–0.38 against their nearest, and the builder asserts `min(dup) > max(keep)` so a wrong pairing cannot pass. The four are parked with their pairing table (S77), never deleted. Rungs 4/5/6 are bench observations no objective covers and become BC02's **I have…** group per §25.10a/b. **NOT RULED, and recorded as open:** the past tense asks *did you do it* where the objective asks *can you do it*; if that is worth keeping, all seven fold and the student ticks the same claim twice under two labels. **ALSO RECORDED — THE ACHIEVABILITY EDGE:** folded rung *"Run 7E and watched the stopwatch version fail on a tired battery"* now sits behind the Mark-done lock and needs a tired battery to earn. §7E mandates the run so the lesson plants the rep, but this is exactly §25.10c's shape, where an item not every student can earn makes the lock unreachable. **BC01 had no ancestor** — zero pre-§6 reveals, zero `check` reveals, zero TRY IT — so five items were authored and §-ordered §3.1→§3.2→§3.3→§3.4→§3.5, each citation read and verified to CONTAIN its answer (v8.58.1) and each deliberately non-overlapping with BC03: BC01 asks the recall half of §3.5 (why a cliff reads as white), BC03 the apply half (what you change when you may not change the code). **BC02 is L11's own six §2 objectives migrated character-exact** (§25.5), asserted equal, with the literal ☐ glyph and not `&#9744;` — the S115 trap, since the gate counts the literal and the objectives ship the entity. **BC03 migrates all five *Reflection Questions* verbatim**, asserted rather than eyeballed, and authors the five answers and five citations the ancestor never had (§3.2 · §8A.1 · §8A.3 · §8A.4 · §8A.4+§3.5). **BC04 has no ancestor either**; three prompts authored, no reveals, and the Engineer's Log survives as its own block after it, the S80 precedent. **THREE BASELINES MOVED, EACH CONTROLLED IN BOTH DIRECTIONS.** §27.11 to 644 rules / 2,362 declarations, **diffed by SELECTOR rather than by the comment header**: exactly one selector gone (`.div-bg-eafaf1`, the consumed checklist's pale-green box, 3 declarations — the −3 IS that rule), **zero born, zero surviving rules altered, so no class RENAME this time**, which is the S115 defect not repeating rather than a rule that stopped applying. §21 coverage 230 → 235, sole delta `BrainGear_Incomplete.png` 45 → 50. Family map 1053 → 1057, controlled at an identical generator version pre-tree against post-tree: exactly ONE family moves, BRAIN CHECK 40 → 44, the other 29 byte-identical. After the moves, a deleted `color: white;` still FAILS, a deleted callout still FAILS naming 1056/1057, a broken image ref still FAILS, the CHECK→CHEK sabotage still FAILS, and leaving `'11'` in `BC_PENDING` FAILS **naming L11** — which is what the named sets bought at S115, where a count could only have said ten. **TWO PROCESS FAILURES, BOTH MINE, BOTH KEPT.** (1) The 4/3 split of the checklist was hand-predicted and then asserted — **and the assert failed**, because the normaliser stripped only *"I can"* and *"I have"* and so read *"I converted…"* and *"I measured…"* as unique. It was re-derived rather than tuned to match the prediction; tuning it would have been writing the gate to the sweep. **A hand-predicted count is a lead, and asserting it is how it stays one.** (2) A control run misfired **three times** — the injection never landed, the script died before writing, and the gate printed PASS against an unmodified tree, which was nearly recorded as evidence that the moved baseline still fired. **§24.6b is not "assert something changed" but assert the injection LANDED in the shape intended — and a control that dies before it writes is a control that never ran, wearing a PASS.** `book_gates` **v1.44.2** (from v1.44.1), `build_family_map` **v1.3.4** (from v1.3.3). Applied S116: L11 **v02.18.0**, moderate — the page renders differently, so both §5b homes move. Census 40,206 → 40,391 [lesson_inventory.py].

v8.104.1, S115, minor — **AN INCOMPLETE PUSH, CAUGHT BY THE FRESH-CLONE RITUAL AND NOTHING ELSE.** S115's push carried `css/book.css` and L10 and **omitted the nine lessons the regeneration had also rewritten**. In the pushed clone `book_gates` came back **47/48** with §27.13 failing, while the same tree passed 48/48 locally — the exact scenario the verify-by-fresh-clone rule exists for, and the md5s all MATCHED, so this was a MISSING file and never a corrupted one. **Cause: a class RENAME, which §27 names as its own case.** L10's four new Brain Check blocks added ten `<details>`, flipping the usage ranking that `build_css` orders by, so `.details-dee2e6` and `.details-dee2e6-2` **swapped names** and `.h4-c-4d535f-5`'s declarations moved onto `.h4-c-4d535f-4`. Proven a pure rename rather than a restyle by asserting declaration-set equality across the swap in both directions. **The live site sat in a broken intermediate state**: nine lessons naming `-2` against a stylesheet where `-2` now meant the other spacing, so every Brain Check reveal in L01–L09 rendered with the wrong margin and padding — visible on the page, invisible to a push that looked clean. **THE RULE THAT WAS ALREADY WRITTEN AND NOT FOLLOWED:** the handoff's push item 6 says to stage into a copy of the PUSHED CLONE and run `book_gates` THERE before presenting md5s. Gates were run in the staging tree instead, which passed, and **nobody asked which files the restore→regenerate→apply cycle had modified** — the cycle rewrites all sixteen lessons and only the ones it actually changes need pushing. **The missing step is one line: diff the stage against the clone and push every file that differs, not every file you meant to change.** Applied S115, all nine MINOR (class name only, renders identically once lesson and stylesheet agree, visible banners unchanged per §5b): L01 **v03.19.2** · L02 **v03.11.2** · L03 **v03.28.1** · L04 **v04.19.2** · L05 **v04.19.2** · L06 **v04.23.2** · L07 **v04.22.1** · L08 **v04.19.2** · L09 **v05.16.2**. Census unchanged at **40,206**.

v8.104, S115, moderate — **§25.2a NEW: ONE CONCEPT, ONE PREDICATE — AND THE CONVERTED SET IS NAMED, NOT COUNTED.** "Converted to the four exit blocks" had TWO definitions in one file: §25.2 scoped on the string `MENTAL KNOWLEDGE CHECK`, gate 29 on `id="brain-check-01"`, and **nothing asserted they agreed**. Measured, not argued: mistyping CHECK→CHEK in ONE lesson dropped it out of §25.2's enforcement entirely — no four-block conformance, no retired-name ban, no checkbox/tag parity — and **ALL 47 GATES PASSED**; breaking the other predicate failed three gates loudly. **§24.8 exactly: if a lesson silently left §25.2's scope, that gate looked identical either way**, and the S83 rule — import the definition, never write a third regex — is what it had been violating. Closed with one shared `is_converted()` requiring BOTH marks and reporting a HALF-conversion as its own finding, since half a conversion must not buy exemption from the gates. **Gate 29's literal is retired for NAMED SETS**, `BC_EXEMPT` and `BC_PENDING`: a count cannot say WHICH lesson moved, and the conversion arc would have required editing that number five times, each edit indistinguishable from disarming the gate. Note *converted* is overloaded in `book_gates.py` — §27 uses it for the inline-style→class migration, and the two are unrelated. **DJ RULING S115 — L14 AND L16 ARE EXEMPT** (competition day / end-of-course; their §10s carry content the four blocks would displace), **L10/L11/L12/L13/L15 CONVERT**; DJ on L15: *"No, don't exempt 15. Revisit later about the flow from 14-15-16."* L15's §10 is the longest in the book but does the same job as L12's and L13's, and L15 is the one lesson with **zero checkboxes**, which argues for converting rather than exempting. **L10 IS THE TENTH CONVERSION.** The retired-name sweep found ONE ancestor; reading §10 found THREE (§25.10e). **A hand-rolled slicer cutting at the next `<h3>` returned CUMULATIVE counts 14/9/4 where a DOM sibling walk says 5/5/4**, inflating the authoring estimate by four items — §24.6c applies to the slicer that SCOPES the work as much as to the gate that checks it. BC01 had no ancestor (zero pre-§6 reveals), so five items authored and §-ordered §3.1→§3.2→§3.4→§3.5→§3.6, each citation verified to CONTAIN its answer per v8.58.1 and each deliberately non-overlapping with BC03 — the TRIM question moved off BC01 onto `RETURN_TIMEOUT` for that reason. BC02 is L10's own nine §2 objectives migrated character-exact (§25.5), asserted equal, **and the box glyph must be the LITERAL ☐**: the gate counts the literal, the objectives ship `&#9744;`, and the entity reports as *0 checkbox items but 9 tags* — the S114 L07/L14 spelling trap in a new place. BC03 migrates all five Check-Your-Understanding questions **verbatim, asserted rather than eyeballed**, and authors the five answers the block never had; five clears §25.8's floor with nothing cut. Rate Yourself folds into BC04 as a labelled group (§25.10a). **What You Built stays OUTSIDE the family** — it recaps, it does not check, which is the L08 *Record Your Calibration* precedent. **BC01 seats above the §6 SECTION FENCE**, not between the fence and its banner, or §6.8a fails — a placement §25.10h does not state and the fence gate does. Achievability confirmed before BC02 landed: §6 Step 3's *"Type it wrong first"* already plants the `error: redefinition` rep. **FOUR BASELINES MOVED, EACH CONTROLLED IN BOTH DIRECTIONS**: §21 image coverage 225→230, sole delta `BrainGear_Incomplete.png` 45→50; §27.11 to 645 rules / 2,365 declarations, **diffed by SELECTOR because keying on the comment header — which carries usage counts — makes every rule look changed**, showing exactly one selector gone (`.h4-c-4d535f-5`, 2 declarations), zero born, zero survivors altered, with `build_css` renumbering the survivor, the §27 class-RENAME case arriving by regeneration; and the family baseline 1049→1053, controlled at an identical generator version pre-tree against post-tree, **exactly ONE family moving, BRAIN CHECK 36→40, the other 27 byte-identical**. After the moves: a deleted `color: white;` still FAILS, a deleted callout still FAILS, a broken image ref still FAILS. **A NEAR-MISS WORTH RECORDING:** a blind first-occurrence replace put the new family baseline into a CHANGELOG line and rewrote S113's history — caught on read-back, reverted, and every later edit went through a `count==1` assert. **Editing history to record a present fact is a defect even when the present fact is right.** `book_gates` **v1.44.1** (from v1.43.2), 48 gates. `build_family_map` **v1.3.3** (from v1.3.2). Applied S115: L10 **v02.17.0**, moderate — the page renders differently, so both §5b homes move. Census 40,015 → **40,206**.

v8.103, S114, moderate — **§24.14 NEW: EVERY CALLOUT BLOCK RESOLVES TO A FAMILY.** The rule gate 47 has enforced since S112 finally has a section. **The rule was never missing — only its home was.** Gate 47 enforced it, `book_gates.py` carried a full comment block on why, and `ZUMO_FAMILY_MAP.md` recorded the whole S112 derivation. What did not exist was the numbered section here: §24 ran 24.13 straight to 24.15. v8.101 logged that as a debt rather than closing it — the same shape as §21.1's thresholds living only in `book_gates.py`, and the same §24.2 failure: **a rule canonized without its home holds only where someone happens to look.** The section states the ORDER — **family from CONTENT; the mark and the colour are OUTPUTS** — and records why: 252 of 1,048 blocks were resolved by HEX until S112, so a repaint moved the ground under a quarter of the map, and thirteen L12 blocks wearing one glyph and one green were three families with a correct STILL GREEN ruling **overridden by paint**. It also states plainly that the printed denominator is a **frozen baseline, not a count**, that `assigned 1049 / 1048` is therefore a line that reads like a count and is not one, and that moving the literal is legal only after a control run proves the per-family delta — because the total alone is not evidence. Transcription of an enforced rule, not new canon: no ruling changed, no lesson file changed, census unchanged at **40,015**.

v8.102, S114, moderate — **§12.2 THE HANDOFF'S NUMBER IS GATED, AND THE RULE IT ENFORCES WAS ALREADY CANON.** §12.3 step 4 has said *write `ZUMO_S<N+1>_HANDOFF.md`* since v8.24, and §12.2's own `git rm ZUMO_S<N-1>_HANDOFF.md` line agrees with it. **Both were violated in consecutive sessions anyway.** the prior session wrote its OUTGOING handoff into the INCOMING handoff's filename, editing that file in place across three commits with its STATE block updated each time (`893b8b6` → `4558257` → `8ae3857`) while its title kept naming a session that had already run — so the incoming handoff under its correct name **never existed**, and the text actually pasted at session open matches no committed version of any file. The convention was then inferred from that one defective example rather than from this Bible, and the outgoing handoff went up under the wrong number. **The session number then drifted twice more the same day**, disagreeing across four hand-typed homes. **DJ caught both by reading the numbers.** `book_gates` **v1.42.2 → v1.43.0**: gate 28 now parses the number out of the FILENAME, out of the `# ZUMO — SNN HANDOFF` title and out of the *"paste at top of Session N"* clause, fails when any two disagree, and fails **loudly rather than skipping** when the title shape is missing. Control-run four ways, and two of the four are the real historical defects, not synthetic ones. **What it replaced could not see any of it:** the gate asserted only that exactly ONE handoff exists, which is satisfied by a file renamed `ZUMO_S999_HANDOFF.md` — measured, and it PASSED. **§24.2 arriving late — a rule canonized without its gate holds only where someone happens to look — and §24.8: if the answer were the opposite, the old gate looked identical.** No lesson file changed; census unchanged at **40,019**.

v8.101, S114, moderate — **§24.15 NEW: A DRAFTING MODEL CANNOT COUNT THE BOOK.** `GPT_BRIEF_FORMAT.md` was written at S112 and committed to the repo root, where nothing gated it, nothing linked it and no roster named it — the §12.2 shape exactly, a standing rule stored somewhere it will drift silently. Moved here verbatim in substance and **the file is deleted**. The rule: every brief to a drafting model opens with a MEASURED FACTS block, each number naming the instrument that produced it (§24.10), and a task whose answer depends on a number not in that block is either given the number or not sent. **Also recorded, not fixed: §24.14 does not exist.** Gate 47 ships printing `§24.14 every callout block resolves to a family` against a section number this Bible has never carried — the same debt shape as §21.1's thresholds living only in `book_gates.py`. **Also S114, and it is the entry's real finding: THE FAMILY MAP'S DENOMINATOR IS A FROZEN BASELINE, NOT A COUNT.** L03's `[IMAGE 3.4]` placeholder became a real WHAT YOU SHOULD SEE callout carrying a §22 terminal block, and the generator printed **`assigned 1049 / 1048`** — a line that reads like a count and is not one, because 1048 was a literal. Controlled at the identical generator version against the pre-edit tree: the only two lines that move are WHAT YOU SHOULD SEE 27 → 28 and the total, with the other **29 family counts byte-identical**, so the delta is the one added block and nothing else. `build_family_map` **v1.3.1 → v1.3.2** moves the literal to 1049. **Parsing the true total and asserting the baseline separately is deliberately NOT done — it changes what gate 47 means, and that is DJ's ruling.** Until it is ruled, every callout added anywhere in the book fails gate 47 until that literal is edited by hand. Applied S114: L03 **v03.24.1 → v03.25.0** (moderate — a planned figure became live content, so the page renders differently and both §5b homes move). Census 40,013 → 40,019 [lesson_inventory.py].

v8.100, S112, moderate — **§27.14 NEW: EVERY LINK AND EVERY ID RESOLVES, AND NOTHING HAD EVER CHECKED.** The book carries **1,237 `<a href>` and 705 ids across twenty pages** and no gate looked at any of them. Two came close and neither covers it: *index.html relative links resolve* walks ONE page, and *going_deeper links canonical and relative* checks the SHAPE of a href, never whether its target exists. **A dead in-page anchor is the most invisible defect the book can have** — the link renders, the cursor changes, the page does not move — and it is created by exactly the work S111 did most of: renaming an id, deleting a block, retiring a figure row. Parser-based per §24.10, because an `id=` inside a code block is not an id. **Gate 46**, control-run on FOUR shapes — dead in-page anchor, duplicate id, missing file, dead cross-page fragment — each named individually, and with a RESOLVING cross-page fragment planted beside the dead one so the branch is exercised in both directions. **§24.6c, recorded in the gate itself:** the first version reported **223 broken links** and every one was a Maker URL of the form `../newproject.html?lesson=1&kind=c01` — the query string was being read as part of the filename. The book was right, the instrument was wrong, and 223 is large enough to look like a finding. **§24.8 AGAIN, AND THIS ONE IS THE ENTRY'S REAL LESSON: WHERE A GATE SITS IN THE FILE IS PART OF THE GATE.** Appended below the summary and its `sys.exit(1)`, gate 46 printed PASS *after* `ALL GATES PASS` on a clean tree — so its verdict sat outside the summary — and on a failing tree it never executed at all. **A gate that only runs when every other gate passes cannot catch anything in a failing suite.** It looked correct in both readings and was caught by the control run, not by reading. `book_gates` **v1.40.0 → v1.41.0, 46 gates**. No lesson file changed; census unchanged at **40,013**.

v8.99, S111, moderate — **THE CHALLENGE-CARD HEADER TAKES THE §9 BAND, SUPERSEDING v8.87's ANTIQUE BRONZE.** DJ ruling, from a rendered specimen: *"go with the new #9 color we just created."* The 87 headers move to the ruled Challenges band **`#7A5905`**, white cap text at **6.44:1** (Parchment text on it reads 5.76, above v8.87's 5.12 with Bronze, and white is chosen because every other cap in the book is white and a single dark cap reads as a defect — DJ: *"mixing white and black font looks horrible"*). v8.87's reasoning is NOT overturned on its own terms: Warm Brass was correctly rejected there as the RAREST colour at 2–6%, and `#7A5905` is Warm Brass **re-lit to L\* 40**, not Warm Brass. It is the §9 section band, so the header now matches the section it belongs to instead of borrowing §4–6's colour — which is what made Bronze the wrong answer and nobody had noticed. **v8.87's entry is annotated, not rewritten (§26.7).**

**THE BAND PALETTE IS RE-RULED, EIGHT BANDS, `build_palette.py` v1.0 → v1.1.** Every hex is still EMITTED, and the generator now reproduces the approved specimen under assert. **(1) The +18° Wrap Up rotation is DROPPED** — re-derived, it bought ΔE76 **0.33** against Theory, so an invented hue was paying for nothing; Wrap Up is Deep Navy re-lit at near-neutral chroma. **(2) Heritage Slate Blue leaves the band set.** Deep Navy and Slate Blue are 15.6° apart and at this chroma 15.6° is invisible — **DJ found Theory and Testing by eye before any number said so** (*"Testing and theory are super close"*), ΔE76 8.7, the tightest pair. Leave-one-out over all nine candidates: dropping Slate Blue → 18.9, dropping Theory → 17.5, dropping ANY other band leaves it at 9.4, and dropping Hardware makes it **WORSE at 5.3** because Hardware is the band standing between them in the ramp. Only removing a navy helps, because the crowding IS the two navies. **(3) Three new hues:** Testing takes teal 200°, plus rose 337° and hunter green 148°. **Amber was measured and REJECTED** — 20.4° from WARNING and its band landed ΔE76 11.6 from Challenges, indistinguishable from its own neighbour. **(4) Chroma damping 0.62 → 0.90**, a deliberate step back from S110's sun-faded look and recorded as such: 0.62 was what made the bronzes read as dirt and kept the teal from being teal, and raising it **improved** separation 15.4 → 22.2 because damping had been flattening the bands toward each other. **(5) Chroma is now PER BAND** — rose and green stay at 0.62 as deliberately quieter accents with no section assigned yet, Challenges goes to 1.20. **Real Warm Brass cannot be a band at all:** it is L\* 69 and white on it is **2.34**, so a band carrying white cap text can never be brass; 1.20 is also the sRGB gamut ceiling, and 1.35 and 1.50 both land on the same colour — a larger number in the file would have described nothing.

**THREE INSTRUMENT FINDINGS, all from wiring the ruling into the generator rather than from reading it.** (a) **A REQUESTED CHROMA sRGB CANNOT HOLD IS A FICTION.** New `EXPECTED_CLIPS`, declaring Testing, which asks 25.5 at L\* 26 and carries 19.4; lowering the request to make the numbers agree moves the band to `#004648`, **which is not the hex DJ ruled on**, so the ruled hex is kept and the clip is recorded. CONTROL D control-run at chroma 2.0 where 3 of 8 clip, so the detector can fire. (b) **CONTROL E was scoring the palette against an incomplete reference** — it measured every band against `CANON`, which does not contain Forge Red (§26.9 filed it as functional), so Troubleshoot was marked **41.7° off its own source colour**. A gap in the instrument, not drift in the palette; with Forge Red in the reference set all five Heritage-sourced bands land within 0.5°. (c) **The hue-override round trip is load-bearing:** reading the override chroma straight from the constant instead of through a real sRGB colour moved Testing `#00474B` → `#00494D` and Green `…55` → `…56` — a palette DJ never saw, caught only because the specimen was asserted rather than eyeballed.

**A MEASURED DEFECT THE REPAINT INHERITS, not yet ruled:** on Parchment, Hardware's callout tint `#F5EBE0` sits **ΔE76 3.4 from the page**, carried entirely by its 4px border. Parchment is warm and so are three of the eight tints. Going warmer makes it worse; `TINT_L` 93.5 → 90 takes the faintest to 6.2 with text-on-tint still 6.94. **Also S111: `[IMAGE 2.5]` RETIRED** — L02's completed program is a live code block in the Quick Reference instead of a screenshot, because `image_audit` can ask whether a tag HAS an asset and never whether the tag SHOULD EXIST, and the row had read *full program screenshot* since the Canvas-paste era. The book already renders 830 `<pre>` blocks, three of them longer than the 120-line file. Planned figures 145 → 144, outstanding 19 → 18, `.div-3498db-2` lost its last consumer and died (7 declarations, exactly the drop), §27.11 baseline 657/2,403 → 656/2,396. `[IMAGE 3.4]` and `[IMAGE 3.6]` are the same shape — §22 terminal blocks, of which the book already carries 13 — and are queued, not done. L02 **v03.10.2 → v03.11.0**.

**A CORRECTION TO THE S111 HANDOFF, per §24.6c:** it lists *"gradients 134 instances, unruled"* as a canon debt. **They were ruled in v8.87 and the ban is absolute.** The count reconciles exactly — 133 class-driven elements across the sixteen lessons plus **one inline gradient still live in `going_deeper.html`** — but an inherited handoff line was read as a finding and a decided question was re-opened for most of a session. The debt list is not canon; the Bible is.

v8.98, S109, moderate — **§24.13 NEW: RE-DERIVE, DO NOT RE-READ — AND A LIST IN PROSE IS NOT THE LIST.** DJ ruling, on being told a taxonomy had been checked three times and was still wrong: *"So when I say double check you don't double check?"* **Re-reading is not checking** — a second look at the same artefact is the same instrument run twice, and a list with a member missing looks complete from the inside (§24.8, failed). A check is a DIFFERENT METHOD or an ASSERT against a number the artefact cannot supply; the word *verified* is not used for anything else. **A list presented in prose is not the list** — any set whose membership matters is EMITTED from the structure that produced it and asserted against a known total. **The case:** a 17-family callout consolidation was computed in code, printed `CORE CONCEPT 60` with `unaccounted: 0`, then HAND-TYPED into a chat message as an 11-row table with INSIGHT's 60 blocks dropped in the retyping — and the next build read the chat message rather than the verified structure, so the prose became the source and the data structure was abandoned. Three passes over that table found nothing, because all three were re-readings. One line caught it: `assert tot + rem == 1048`. **This is the v3.0 ghost wearing a different noun** — §12.6 forbids hand-typing a VERSION and §24.10 requires a count to name its instrument, but neither covered a TAXONOMY, and the gap was enough, so the rule is stated on SETS. Ungated by design. **Also S109, separate from the ruling:** six INSIGHT blocks carrying the canonical magnifier wore five non-canon paints across L02/L03/L07 — three of them borrowing OTHER families' canon (TIP's `#f0f7f0`/`#6b8e6b`, What-You-Should-See's `#d1ecf1`/`#17a2b8`, Checkpoint's `#4caf50`) with INSIGHT's glyph on top. Repainted to `#e9f7f5`/`#2da99d`: canon 31 → 37, non-canon magnifier blocks 0, INSIGHT's paint spread 11 → 6. **Three stylesheet rules died and all three had ZERO Bible mentions**, while every canon paint touched survived because other families still hold it. The remaining five INSIGHT paints are RULED and were left alone (L11's ✅ and L12's 🏆 are S94's success-green payoff blocks; L13/L14's 💭 are `THE ONE IDEA`, hard-coded in `build_family_map` line 75). Verified in a STAGED COPY OF THE PUSHED CLONE per S108, where 13 lessons came back byte-identical through the restore→regenerate→apply cycle and all 30 family counts were unchanged. `book_gates` **v1.39.0 → v1.39.2**: gate §27.11's printed label was hard-coded and stale at 664/2,434 while its constants tested 660/2,418 — right test, wrong name — and is now DERIVED from those constants; and **`BAND_END`** names the §10+ section band, which had been typed literally in ELEVEN places (five inline sites plus six `GEOM_BASELINE` keys) so §5.0.1's ramp could not land as an edit. The refactor was asserted behaviour-neutral by byte-identical gate output, then control-run by flipping `BAND_END` to DJ's Steel `#708BAF` — because byte-identical is also what a DEAD constant produces (§24.8). The flip fires **FOUR** gates: §25.10h, §4.5, §4.5a and **§5.1**, where the S108 handoff recorded three and missed §5.1's `GEOM_BASELINE` keys, which would have fired mid-ramp with no warning. Applied S109, all MINOR (callout paint only, visible banners unchanged per §5b): L02 **v03.10.2** · L03 **v03.23.2** · L07 **v04.20.2**. Census unchanged at **40,025**; `css/book.css` 660 → 657 rules, 2,418 → 2,403 declarations.

v8.97, S108, moderate — **THE BANNER ARC IS APPLIED, AND THE BAND RAMP IS NOT.** §6.5's LOCKED *"Cap KEEPS the leading icon"* is **SUPERSEDED: no icons on any of the 237 caps**, bonus block included. All 237 carried a leading emoji; zero do now, **verified by DOM lookup rather than regex** — 237 caps found by id, 237 headlines, 189 eyebrows, 0 glyphs. **NEW §6.5b, THE CAP IS TWO LINES:** *headline = the most descriptive string available, eyebrow = everything before it*. The section NAME therefore MOVES — eyebrow when a written headline exists, headline when it does not — so §6.8a's fence had to learn both shapes. **The fence rule extends §6.8a:** fence = the eyebrow's name after the middot, else the headline, which keeps it DERIVED; a hard-coded fence vocabulary would reinstate the exact gap §6.8a was written to close, when L01 shipped `KEY CONCEPTS` above a *Background Theory* banner. `_fence_title()` control-run in both directions against a converted lesson and a legacy one. **NEW §6.5a-T, TYPE TREATMENT E:** Inter served the way `index.html` already serves it, `.page` line-height 1.7→1.65, `#333`→`#1d1d1f`, and the **Windows-only Segoe UI stack RETIRED** — every non-Windows reader had been getting Tahoma or Geneva for the life of the book while `font_stack_sweep` reported **0 rewrites across 207 files**, because it scanned SVGs and never opened `css/book.css`. Fixed, v1.1.0, control-run against the pre-session stylesheet. Its rewrite map then proposed `Inter → Arial`, so **a face the site actually serves is exempt in `.css` context only**. **§4.5's derived family mark superseded**, word retained — the harm argument was always carried by the WORD; `gen_bonus_banner` v1.3.0, and its mark assert **INVERTED rather than deleted**, because a gate that stops checking is worse than one that fails. **§6.9 `image-index` → `figures`**, three passages. **§6.5 Box CONFIRMED AND UNIFIED (DJ ruling A, chosen from a rendered specimen):** the panel had shipped in TWO forms — 18px/no-background in L01–L09, `20px 25px`/white in L10–L16 — split at the identical seam in all five colour groups and invisible to every gate; 104 panels moved and **five duplicate rules collapsed, one per colour**. `going_deeper` **v01.2.0**: six anchor ids added at last, entry 5 retitled *Using Fixed Point*, four lesson pointers deep-linked (the other three name two or three entries each and correctly stay at the top). **THE HERITAGE BLUE BAND RAMP WAS PILOTED ON L03 AND REVERTED.** Seven gates fired, and the finding is structural: **the ramp cannot be piloted on one lesson**, because five constructs are byte-compared across all sixteen — lesson strip (§6.5a), hero (§25.6), PART dividers (§6.8), bonus cap (§4.5) and the FINISHED EARLY box (§4.5a) — and three more gates hard-code `#6c757d`. It is a book-wide change with instrument work FIRST. **TWO METHOD LESSONS.** (1) **Verifying on the working tree is not verifying the push:** the panel unification retired five rules, which reordered `build_css`'s frequency ranking and **re-spelled classes in L02–L09, lessons that were never edited**; a nine-file push would have shipped `div-3498db-3` with no rule behind it. Caught only by rebuilding pushed-clone + staged files and running the gates there. (2) **A shallow clone served a stale HEAD twice** while the remote was already ahead — §12.4's *caches lie*, now with a remedy: `git ls-remote HEAD` before trusting any verification clone. `book_gates` **v1.39.0** (CSS baseline moved four times, each move accounted for in the file). Applied S108, all 16 lessons.

v8.96, S106, moderate — **§27.12 + §27.13 NEW: THE MIGRATION'S TWO UNGUARDED INVARIANTS.** **§27.12** — a page that links `css/book.css` carries NO inline `style=""`. Measured: pasting one `<p style="color: #ff00aa; font-size: 13px;">` into L05 left **all 43 preceding gates green**, and the element renders correctly while doing it, so nobody looks. Every hand-edit, pasted block and AI-suggested snippet re-opens the hole the migration closed. Scope keyed on the `<link>`, the §25.6a rule, so the four tool pages' own inline styles stay out. **§27.13** — `css/book.css` must regenerate byte-identically from the lessons. This is the guard on §27.8a/b: stop after *regenerate* and skip *apply*, and 46 class names keep their spelling while changing meaning, invisible to gate 41. **Gate 43 cannot cover it, because §26's repaint MOVES gate 43's baseline by design and a moved baseline is a spent gate**; §27.13 re-derives instead of remembering, so a repaint does not spend it. **Complementarity measured in both directions:** a hand-deleted `color: white;` fires 43 and is INVISIBLE to 45 (build_css reads the stylesheet through `expand_classes` — §24.8); one element retyped to a *different resolvable class* leaves all 43 green and fires 45. Neither subsumes the other. **`strip_inline --verify` was offered and NOT added**: it computes gate 41's assertion a second way and never fired independently of it across four controls — an assert that cannot fail is not evidence. `book_gates` **v1.38, 45 gates**.

v8.95, S105, moderate — **§27.11 NEW: THE STYLESHEET IS BASELINED, BECAUSE THE MIGRATION MADE IT A SINGLE POINT OF FAILURE.** A declaration used to live in 25,036 places; it now lives once, and **nothing validated `css/book.css` at all**. `build_css --check` cannot: it rebuilds from lessons read through `expand_classes`, which reads the stylesheet — damage it and the expansion is damaged identically, so `--check` says *current*, exit 0. **Measured: deleting one `color: white;` left all 42 gates green and `--check` clean** while the lesson strip's links went dark-on-dark in all sixteen lessons. **Gate 43** baselines 664 rules / 2,434 declarations / a body digest; control-run against a dropped declaration, a changed hex and an injected rule, loud on all three, silent on a generator version bump. **The baseline is meant to move** — §26's repaint moves it, as §21's moved 218→223. General lesson: **consolidation creates a single point of failure, and the instrument that built the artefact cannot be the instrument that guards it.** `book_gates` **v1.37, 43 gates**.

v8.94, S105, moderate — **§27.10 NEW: THE BOOK IS DOMAIN-AGNOSTIC.** 478 absolute `href`/`src` attributes plus **18 JavaScript `img.src` string assignments** — 496 total, all in the sixteen lessons — made relative-to-the-page. **The 18 JS refs were invisible to every attribute-shaped search** and surfaced only because the sweep's REMAINDER was audited rather than assumed. Seven off-site references remain and must (Google Fonts 4, template zip 2, jszip CDN 1): domain-agnostic means the book does not name its own host. The going_deeper gate no longer allow-lists the absolute form — it derives expected depth from the page and was control-run against both regression shapes. `book_gates` **v1.36** (42 gates). Lesson bytes 2,582,947 → **2,569,059**. Census unchanged 39,994; visible text identical in all twenty pages. All 16 lessons minor-bumped.

v8.93, S105, moderate — **§27.9 NEW: THE HOLD RELEASED. ZERO INLINE STYLES BOOK-WIDE.** The four byte-exact-across-lesson block types (§6.5a strip 320 · §25.6 hero 96 + footer 16 · §6.8 PART dividers 192) converted in one pass. The book now carries **25,036 classes and no `style=""` attribute at all**. Released by measurement: the 624 attributes carry only **16 distinct strings**, each appearing an exact multiple of 16 (proof of book-wide uniformity), and **all 16 round-trip byte-exact** through the stylesheet — only true because §27.8c fixed declaration order and §27.8d fixed colon spacing. `strip_inline` **v1.1** adds `--include-held`, gated on a `roundtrips()` precondition that REFUSES and names offenders; CONTROL I proves both directions. Lesson bytes 2,638,947 → **2,582,947**. Census unchanged 39,994. All 16 lessons minor-bumped.

v8.92.1, S105, minor — §27.8d: DJ ruled ONE colon spelling for the generated stylesheet; spaced, which is 98% of the source and the only one the gates accept (unspaced broke five). Lessons byte-unchanged. `build_css` v1.2.1.

v8.92, S105, moderate — **§27.8 NEW: THE MIGRATION COMPLETES ITS SWEEP.** All 16 lessons converted: **24,412** inline attributes to classes against a 664-rule `css/book.css`, **624 held** (39 per lesson, every lesson) — 24,412 + 624 = **25,036**, the §27 census exactly. Zero unmapped, zero dead classes, 41/41 gates. Render identity proved by construction AND independently: 25,036 styled elements compared in document order, declaration sets identical, visible text identical bar one `<link>` per lesson. Census 39,979 → **39,994**. Lesson bytes 3,534,934 → **2,638,947**, 25% smaller. **Three ways a widened build bites, all measured:** (a) widening `SOURCES` renamed 57 of L01's 167 classes and **46 kept their spelling while changing meaning** — invisible to gate 41, so every converted lesson must be re-stripped whenever `SOURCES` changes; (b) `expand_classes` reads the stylesheet from disk and leaves an unresolvable class in place, so regenerating before restoring strands 74 L01 elements permanently — the order **restore → regenerate → apply** is forced; (c) `canon()` sorts while §4.5/§6.8/§25.6 assert authored order, which broke a whole class of gates at once and revealed a **fifth** held block type the S104 hold list missed (the §4.5 bonus banner) — fixed in the generator via `build_css.preferred()`, not by holding blocks until the gates went green. **`strip_inline.py` v1.0 NEW**, eight controls, the tool S104 did not commit; `build_css` v1.2; `session_versions` v1.14.1 after its own CONTROL A was found seeding a literal version string that expired on a bump. All 16 lessons minor-bumped.

v8.91, S104, moderate — **§27.7 NEW: THE MIGRATION BEGINS, AND ONE LESSON PRICED IT.** L01 converted end to end: 1,111 of 1,150 inline attributes became classes, 39 held because three constructs are compared byte-exact across lessons (§6.5a strip, §25.6 header/footer, §6.8 PART dividers). **One stylesheet, not sixteen** — 689 distinct declaration strings, 92.5% of instances shared across lessons. **`lesson_inventory.expand_classes()`** so six CSS-reading gates keep working whatever a file's conversion state; **gate 41** because a mistyped class makes an element INVISIBLE where a mistyped inline style only made it wrong — proved by dropping L01's callout census 83→82 with all 40 gates green. Render identity asserted by construction, not inspection. Also S104: **L15's three figures retyped IMAGE→GRAPHIC** (§10 separate number spaces — the tag contradicted its own filename), and a book-wide sweep proved L15 was the entire class. **`image_audit.py` v1.1 NEW** replaces the hand-maintained `IMAGE_SHOT_LIST.md`: 20 outstanding of 145 planned. Its two false findings are recorded in the tool — a cross-lesson tag keyed to the wrong lesson, and ten "type mismatches" that were legitimate separate-number-space figures, killed by reading. **Five L07 figures built** from GCC diagnostics reproduced in the sandbox, clearing L07. `book_gates` v1.35.1 (41 gates), `lesson_inventory` v1.2.0, `build_css` v1.1, `image_audit` v1.1, `session_versions` v1.14, `site_parity` v1.1. L01 **v03.15.2** · L07 **v04.16.0** · L15 **v02.11.2**.
v8.90, S103, moderate — **§27 NEW: THE BOOK IS A WEBSITE, NOT A CANVAS PASTE.** DJ ruling: *"There will be no pasting html text into canvas. Then I don't have to worry about updates."* Lessons live at ONE address — the published site — and Canvas **links** to them, keeping quizzes, grades, syllabus and submissions. **The justification is a copy nobody could measure:** `site_parity.py` compares the repo against Pages and found a live 404 nothing else could see; **nothing has ever compared Pages against Canvas.** Every lesson edit obliged a re-paste, and a re-paste that did not happen was invisible to all 40 gates and to the author. A 3.58 MB book existed twice with instrumentation on one copy. **What this retires:** §6's *"all styling is true inline"* exists ONLY because Canvas strips `<style>` and `class=` — measured cost of that constraint at S103 is **25,036 inline `style=""` attributes, ~67,000 declarations, 44% of lesson bytes (1.56 MB of 3.58 MB), 2,828 `font-family` declarations where a stylesheet needs one, and 473 absolute `weymuth.github.io` links** forced because a pasted page has no directory to be relative to. **§26's repaint was never too hard — it was priced against the wrong delivery model:** `#f8f9fa` at 641, `#fffbe6` at 87 and the 27 live accents become declarations instead of sweeps. **Verified before ruling, not asserted after: ZERO of the 40 gates enforce Canvas-safety** — no gate references `class=`, `<style>` or Canvas, so the suite survives untouched. §27.4 rules that Canvas links point at the **index**, not at sixteen deep links, which would rebuild the update problem this ruling solves; that also caps the exposure from a possible later move to robolore.com (DJ, S103: *"a later decision"*). **§17.3's SVG font rule is untouched** — an `<img>`-loaded graphic still cannot fetch a webfont. **The migration is NOT done by this ruling**: the 422 Consolas-first lesson code stacks were proposed as a sweep and **parked**, because in a stylesheet they are one line. *Do not sweep what the migration deletes.* §6's inline rule carries a conditional pointer and is not rewritten (§26.7).

v8.89.1, S103, minor — record only, no book change — **THE VERSION LINE WAS THE ONE HOME AND IT DISAGREED WITH ITSELF.** Two defects in this document's own bookkeeping, both found while writing §24.12, both fixed here. **(1) v8.88 had no changelog entry** — §26.9 shipped in S102 and the changelog line did not, so the list ran v8.87 → v8.89 with the live version sitting on a number that appeared nowhere beneath it. Backfilled above from §26.9's own text; nothing re-ruled. **(2) The `Current:` field inside the version line read `v8.79.1` while the header read v8.89** — nine versions stale, *inside the line this Bible designates as the single home for its version*. Both are now asserted mechanically: `session_versions.py` **v1.9.1 → v1.10** gains **CONTROL F**, which requires the header version, the `Current:` field and the newest changelog entry to agree, and fails loudly in both directions. **The lesson is §24.9's, arriving from a new side: a value is not verified because it lives in a designated home. `session_versions` read the header and never once read the rest of the line it was reading.**

v8.89, S103, moderate — **§24.12 NEW: A GENERATED ARTEFACT IS REGISTERED IN CANON, AND ITS FILENAME CARRIES NO SESSION.** DJ ruling: *"it should also be unversioned."* §24 had eleven subsections on how an instrument is TRUSTED and nothing on what an instrument LEAVES BEHIND — so `GPT_WORKLIST_S102.md` and `ZUMO_FAMILY_MAP.md` were both committed, both generated, and both named nowhere in canon. The session stamp moves OUT of the filename and ONTO a `Work list session:` line inside the file, which is the same two-homes discipline §5b applies to lessons and this Bible applies to itself. **The hazard is not hypothetical:** at S103 open the repo root held `GPT_WORKLIST_S99.md` **and** `GPT_WORKLIST_S102.md`, and the S99 one was known-bad — hand-assembled, ordered by font sizes `svg_layout_audit` could not read until v1.17 — while still looking like a live document. A stamped name does not preserve history, it manufactures a second plausible file. `build_worklist` **v1.0 → v1.1** writes `GPT_WORKLIST.md`; `--session` still sets the stamp and no longer sets the name; regenerate is byte-identical across processes. §24.12 also records that a generated artefact is **never hand-edited** — if the output is wrong the generator is wrong, and repairing the output alone reproduces the defect next run while destroying the evidence.

v8.88, S102, moderate — **§26.9 NEW: FORGE RED IS FUNCTIONAL, NOT A SIXTH BRAND COLOUR.** DJ ruling: *"Forge is functional."* §26.8(7) is reversed **on placement only** — the hex `#D46554`, the name, every contrast figure and the warning/danger distinction all stand. `InstructionalGraphicStandards` §6 states the principle the whole split rests on (brand colours identify RoboLore, functional colours communicate meaning) and §7 says outright that error red must not be presented as a brand colour; **danger is meaning**, so S101 filed a danger colour into the brand palette by way of a split whose founding rule forbids exactly that. Every supporting number in §26.8(7) was correct and the conclusion still went to the wrong document — the §24.6c shape, where a claim inherited inside a session survives because the argument around it is sound. **Measured cost of the reversal:** `BRANDING/ColorPalette.md` untouched, §7's prohibition satisfied as written and needing no amendment, **8 upstream files → 0**, and the palette stays five. `#D46554` replaces `#F44747` in §7's functional token table; the book's 14 live `#f14c4c` instances (L02 ×5, L07 ×9) retire to it as already ruled. §26.8(7) carries a supersede pointer and is **not** rewritten (§26.7). **The general rule this leaves behind: when a downstream ruling obliges an upstream edit, ask first whether the obligation is evidence the ruling is filed in the wrong place. A ruling whose cost is that its own canon must be rewritten to permit it is the ruling to re-examine, not the canon.** *(Entry backfilled S103 from §26.9's own text — the section shipped in S102 and the changelog line did not, so the version line read v8.88 with no v8.88 entry beneath it. Recorded, not re-ruled.)*

v8.87, S101, moderate — **HERITAGE BLUE IS RULED, THE PALETTE GAINS A SIXTH COLOUR, AND GRADIENTS ARE BANNED BOOK-WIDE.** §26 un-parks. DJ stated RoboLore's five himself — Deep Navy `#0B1A2E` · Slate Blue `#3D5266` · Antique Bronze `#7B6240` · Warm Brass `#C9A463` · Parchment `#F5F2E9` — so the §26.5 filing hazard dissolves for §26.1: the ruling no longer cites an uncommitted file, it cites DJ. **All ten of `ColorPalette.md`'s published contrast ratios were recomputed independently and reproduce to 0.018 total absolute error**, confirming §26.2's first test without inheriting it. **A CORRECTION TO THIS BIBLE'S OWN ARGUMENT, per §24.6c:** §26.2 reads as though `BookComponentStandard` §5.0's numbers were sloppy. They are not — its published title contrasts (11.05 / 6.36 / 5.11) reproduce EXACTLY against its own derived tints. Both palettes are internally consistent; the case for RoboLore's rests on provenance, never on arithmetic error, and stating it the other way was a wrong finding at 3× cost. **A FIFTH TEST, new:** re-deriving navy's title contrast from DJ's base gives **12.75**, the exact figure the standard published BEFORE S91's swap — so S91 changed the base and hand-patched downstream, which is why §26.2's fourth test found contrast falling with no rationale recorded. **THE SHAPE OF THE FIX IS A SPLIT, NOT A ROLE TABLE (DJ ruling: *"we don't have to deal with it now, but... That does not mean that we can only use 5 colors in the book"* / *"Yes I like the idea of the brand/semantic set"*).** Heritage Blue governs branding and page-level structure; a separate functional set governs the 30 callout families. This is already RoboLore canon and the book had never been told: `InstructionalGraphicStandards.md` v01.00.00 Approved §6 lists **callouts by name** among constructs that must NOT be filled or headed with Heritage Blue, and states the rule — *brand colours identify RoboLore, functional colours communicate meaning.* **`BookComponentStandard` §5's seven-role table is therefore the thing that retires, not the base hexes** — it put four brand colours into callout roles, which is exactly what §6 forbids. §5.0.1's band ramp SURVIVES: wayfinding is structure. **THE SEMANTIC SET IS UNRULED SPACE, not forbidden space.** §7's functional palette is scoped to *programming instruction and code-centred technical graphics*; a general state system is recorded upstream as not approved. So the 30 families sit in neither palette. **Purple is not banned** — *generic AI purple* was rejected from the BRAND system, no purple hex was ever proposed, and whether purple may serve a functional instructional role was never discussed; the book's largest callout family is purple `#9b59b6` at 136 blocks and it survives by default. **THE BOOK'S CODE PALETTE ALREADY CONFORMS AND NOBODY KNEW.** Measured against §7: editor bg `#1e1e1e` (799) · syntax blue `#569cd6` (2,565) · syntax green `#6a9955` (789) · syntax orange `#ce9178` (683) · function yellow `#dcdcaa` (9) all EXACT with no coordination — the book converged on the same source. Two drift: type cyan ships `#4ec9b6` against `#4EC9B0` (295 instances, one digit) and error red ships `#f14c4c` against `#F44747` (14). Two more are live and UNNAMED by §7: preprocessor `#c586c0` (50) and numbers `#b5cea8` (2,264) — **§7's token list is narrower than the book needs.** **FORGE RED `#D46554` JOINS THE PALETTE AS A SIXTH COLOUR (DJ ruling, name and value).** The palette's saturation ceiling is Warm Brass at 49%; §7's `#F44747` sits at 89% and genuinely does not belong to Heritage Blue. `#D46554` is saturation 60 holding **4.60:1 on the `#1E1E1E` editor background** against `#F44747`'s 4.64 — as far toward the palette as the contrast floor allows, since pulling into the 49 range drops to 3.60 and breaks 4.5:1. §22's `#f14c4c` retires. **Warning `#CCA700` and Danger `#D46554` stay DISTINCT STATES, not merged** — the WARNING family is 84 blocks on `#ffc107` and collapsing them would lose the distinction §5.2 exists to protect. **This obliges an UPSTREAM edit DJ has authorised: `InstructionalGraphicStandards` §7 currently states error red must not be presented as a RoboLore brand colour, and eight RoboLore files assert the palette is five.** **NO GRADIENTS. ANYWHERE. (DJ ruling: *"No gradients what so ever in the book. Not on logos, not on pages, not on graphics, nothing."*)** Measured: **7 distinct gradient strings, 134 instances, 17 pages, plus 13 referenced SVGs** — 87 challenge-card headers `135deg #7d5283→#9b6a9e`, 33 nav bar + title block `to bottom #1a5276→#2e86ab`, 4 milestone banners, four one-offs. Seven strings is a GENERATE, not a sweep. **This ruling RETIRES §6.2, §6.2a (the gradient-vs-solid distinction collapses entirely), §6.4's title block and §8's second Checkpoint form**, and it decides the standing §18.2-vs-§9 canon debt in §9's favour with no judgement call left. **CHALLENGE-CARD HEADERS → Antique Bronze `#7B6240` with Parchment `#F5F2E9` text, 5.12:1 (DJ ruling, from a rendered specimen).** Bronze-with-navy was proposed and measured at **3.05:1** — the one combination `ColorPalette.md` restricts to large text and non-text UI, and header text runs ~18px bold, just under WCAG's large-text threshold. Brass-with-navy at 7.47 was chosen first on sight and reversed once the composition budget was read back: **Warm Brass is specified as the RAREST colour at 2–6%** and 87 headers is not rare. Bronze sits in its own 5–10% band. **The specimen was the instrument** — both candidates PASS contrast, so the numbers could not settle it and a table would have argued the wrong question. **THE BRAND/INSTRUCTIONAL BOUNDARY IS LEAKIER THAN THE STANDARD IMPLIES — logged, not fixed.** The page colour is brand; card interiors are instructional; changing the first breaks the second. Two surfaces already fail on Parchment: the Work-in bar `#fffbe6` (87, exactly the card count) and panel fill `#f8f9fa` (**641 instances of a COOL grey on a WARM page**). Both read fine on today's `#fafafa` because both are neutral. **The 641 is the larger surface than everything ruled above and nobody had looked at it.** **SCOPE C RULED for the repaint: brand layer only** — nav, lesson strip, title block, section caps, PART banners, page colour, body text, band ramp, numbered marks, all gradients flattened. **All 1,048 callouts untouched.** Reasoning recorded because it is a schedule judgement and will look arbitrary later: September 8 is five weeks out and the image shot list stands at 21 of 22 outstanding, which is camera work nobody else can do. A 1,048-block repaint is the wrong work for the last five weeks. No lesson file changed this session; census unchanged at 39,972, 40/40 gates, `site_parity` PARITY.

v8.86, S99, moderate — **§17.3c NEW: `xlink:href`, NEVER PLAIN `href`.** An embedded raster must be carried by exactly one `xlink:href` with `xmlns:xlink` declared. Plain `href` is SVG 2; **Illustrator parses SVG 1.1** and reports an href it cannot read as a MISSING LINK with the photograph gone. Browsers render both forms identically, so **every file the tooling produced for a full session opened perfectly on the published site and not one of them would open for editing** — which is the entire purpose of a Recipe 2 composite. Root cause: S98's dedupe of the doubled payload was correct, but `fit_raster_svg.py` v1.1 kept the plain `href` and dropped the xlink form, and **its control asserted only that the duplicate was gone, never WHICH survived** — so it passed green the whole time. Fixed in `fit_raster_svg.py` v1.2 (control 1 now counts both attributes and is seeded with v1.1's own output, which it catches), `svg_layout_audit.py`, and the graphics prompt, which previously instructed the exact defect. Confirmed the cheap way before any instrument changed: one file converted, opened in Illustrator, worked. Also recorded this session and NOT gated, deliberately: **12 referenced bare PNG/JPG files exceed 500,000 B** — gate 37's ceiling covers only raster-wrapped SVG — with Lesson 5 loading **7.29 MB** of images and **7,133,980 B recoverable book-wide** by storing photographs as JPEG rather than PNG. DJ ruled it not worth gating (boarding school, campus wifi); the measurement is recorded so it need not be re-derived.

v8.85, S99, moderate — **§17.3b NEW: THE CREATE SIDE.** §17.3 named Photoshop -> Illustrator as the route for a photograph and never wrote the route, and §17.3a's Recipe 2 is a prompt for an AI holding a composite that already exists — so the one thing nobody had written was how to MAKE one. Found by DJ asking for it. The section is five steps, and **step 0 is the one that matters**: measured across the three staged composites, all three embed **PNG**, two carry an RGBA channel `fit_raster_svg.py` measures as dead, and one stores its payload twice — 438,626 / 1,266,035 / 960,966 B of payload that fit to 128,287 / 215,741 / 178,544 B. Preparing the photo as a JPEG with no alpha at ~2x the on-screen box is what makes the file arrive near its final size instead of being rescued from 10x. Also records what §17.3a implied and never said: a photo composite has **no fixed canvas** (Recipe 1's 1100x850 is for drawn graphics; the live composites run 2000x1200, 2000x1180 and 1448x1086), and **gate 38 skips any file containing a raster**, so outlined labels in a composite are legal by design. One live defect named in passing: `L05 5-10` sets its labels in `Inter,Arial,sans-serif` and Inter cannot load through `<img src>`, so it was designed against a font no reader will ever see.

v8.84, S98, moderate — **§17.3a NEW: THE TWO RECIPES, AND GATE 38 BEHIND ONE OF THEM.** §17.3 said what the two asset classes ARE; this says what to ask for and what to check. Written the same day four referenced graphics — L06 6-09/6-10/6-12 and L07 7-02 — were found replaced with versions whose every label had been converted to OUTLINES: **23,066 B → 1,148,110 B, a 50x growth, +1.13 MB on the published site, and all four passed 37/37 for a week** because no gate looked at a drawn graphic's size or asked whether its text was still text. One rode in on the same commit as the gate suite's own update. The cause is defensible — a graphic drawn in Inter or JetBrains Mono renders wrong on a student's machine and outlines fix that — but **the cheaper fix is a common font stack**, and all five files came back at 6–11 KB with 32–42 live labels once asked for Arial/Courier New. Recipe 2 covers the photograph case and records that these files **open in Illustrator**, the embedded raster arriving as an ordinary image object. **Gate 38 (`§21.2`) now enforces Recipe 1**: a 60,000 B ceiling on drawn graphics and a flag on path-data-without-`<text>`, thresholds measured with the Mercersburg wordmark and the §18.2 spiral stars — both legitimately zero-text — an order of magnitude clear of the line.

v8.83, S98, moderate — **§17.3 NEW: PHOTOGRAPHS ARE NOT DRAWINGS.** §17 governed drawn graphics only, and the book had no written rule for the other kind, so gate 37 was written in S97 forbidding embedded rasters outright — a rule that would have gone red on the first legitimate photo-plus-labels composite. DJ ruling S98: *"Some of the images need to be raster wrapped svg. Otherwise they look like crap."* The new section records the IMAGE/GRAPHIC split by SUBJECT, the Photoshop → Illustrator route, and the two export settings that fail silently in production — **Embed not Link** (an `<img>`-loaded SVG runs in secure static mode and cannot fetch an external file, so a linked photo is a BLANK graphic on the site) and **fonts**, where live `<text>` renders with the viewer's fonts and an uninstalled face shifts the layout, the same trap §18.2 answered with vector paths. Also records the post-export step (`fit_raster_svg.py --write`, quality pinned, size a consequence) and the `_##` / `_r##` filename suffixes, which were recorded nowhere.

v8.82, S95, moderate — **INSIGHT LEAVES THE SHARED BLUE FOR TEAL, AND THE CALLOUT TABLE SPLITS TYPE 7 INTO TWO ROWS.** The table below has always declared **Learn / Insight as ONE type** with two glyphs on `#e3f2fd`/`#2196f3`, while `BookComponentStandard`'s roster has listed them as **two families with different roles** (LEARN slate, INSIGHT bronze). The two documents have disagreed for sessions and nobody noticed, because the roster renders on zero pixels — the S94 family map followed the roster, which is where "one must move" came from. **DJ ruling, S95: add teal and update the Bible.** INSIGHT moves to `#e9f7f5`/`#2da99d`, hue 174, chosen from the four unoccupied hue arcs in the live palette: it is the only candidate whose border-against-panel contrast (**2.62**) sits inside the book's existing register of 2.46–3.57, and its derived mark fill `#1f7a71` clears **4.68:1** against its own panel, so INSIGHT's mark can ship as a plain `<img src>` under the S94 derived-fill route. **31 blocks repainted across 10 lessons**, all already canon 4px; **18 of them also carried a deep-blue title `#0d47a1`**, moved to `#165a53` (7.28:1, matching the 7.56 the blue held) — a blue title on a teal panel would have undone the split. LEARN keeps the blue and is untouched, 37 blocks. `build_family_map` v1.0.0→**v1.0.1**, with the magnifier-on-blue key **replaced rather than kept**: after the split, a 🔍 on LEARN's blue is a defect to surface, not a block to classify silently. **§26 STAYS PARKED and needed no ruling** — `BookComponentStandard` records **zero** live callout hexes, so teal is not a §5.0 change and invents no Heritage Blue role. **STAGE TWO IS NOT DONE AND IS NOT A PHANTOM:** two live blocks are labelled `Learn/Insight` (L03:3636, L09:1342), §25.10's Problem-Solving item names the shared hex pair by hand, and §18's data-type callout gives the same blue a third job — each needs a side, and each is a meaning call DJ has not yet made.

v8.81, S93 close, moderate — **§24.11 A SWEEP THAT AUTHORS LITERALLY CAN UN-ESCAPE AN ENTITY (NEW), and the two live regressions that proved it.** The S93 triple-check parsed every page for start-tags that are not real HTML elements and found **2**, both in L12: `<Wire.h>` raw in the line-594 title and the line-774 `<code>` span, so the sentence rendered *"The #include  goes at the TOP of the file"* with the filename gone. Provenance: **escaped at S87, S89, S91 and `03d1e85`; raw from `514588e`, the S92 Option C push** — v8.67's defect, same lesson, same sentence, eleven sessions later, caused by that sweep's own approved principle of authoring the string literally. **An entity is not the character it encodes.** A second, same-family defect from a DIFFERENT sweep: L04 1363's block-form conversion at `53a44b6` replaced the **inner** `</strong>` with `</div>`, so the deadband subtitle rendered outside its title element and unbolded. **Both had been printed by `lesson_inventory --anomalies` for two sessions and all 35 gates passed over them** — §24.6a's other half: a parser whose output nobody reads is a log file, not an instrument. **And the stale expectation that gave them cover:** the same list prints `1 visible banner(s), expected 2` for all sixteen lessons because the parser still carries the pre-S89 two-banner rule, so sixteen false leads trained the eye to skip the block holding the two real ones — **a uniform anomaly across every file is a lead about the instrument** (§24.8), and a false lead is not free. Logged for correction, not corrected mid-verification. Applied S93, both MODERATE: L04 **v04.14.0** · L12 **v01.14.0**. Census unchanged at **39,970** — both fixes add characters, not lines.

v8.80, S93, moderate — **§26 THE PALETTE CONFLICT, PARKED (NEW SECTION); GOING DEEPER PROMOTED TO A CALLOUT FAMILY; and THE v8.79 ENTRY RECOVERED AFTER A PUSH DELETED IT.** `BookComponentStandard` v01.9.0→**v01.10.0**: GOING DEEPER added as the 26th family, bronze, `file-earmark-plus` — a **promotion out of §7.2 Systems at zero new icon cost**, the second instance of the ENGINEER'S LOG move, on the same test (the nav affordance and the callout name one destination). `marks/` 40→**41**; the count gate control-ran FAILING at *1 would change* before regeneration and passing after. Census byte-identical at **39,970** — no lesson touched, so §11 step 5 does not apply and the seven 🔬 blocks still render slate emoji until the wiring pass. **§26 records the conflict that had been re-litigated for several sessions: `BookComponentStandard` §5.0 and RoboLore `ColorPalette.md` define Heritage Blue with FIVE DISAGREEING HEXES.** Four tests favour RoboLore (its ten stated contrast ratios reproduce to 0.02 error against the standard's 6.00; its values appear 10–15× across four upstream documents while the standard's appear nowhere upstream; the standard's own LOCKED §9 uses RoboLore's bronze and parchment; and the one-commit S91 swap recorded no rationale while every contrast ratio FELL). **The gate gap: `gen_component.py` never parses §9, so §10.1.5 cannot see the only section that disagrees with §5.** Also recorded: the semantic three is **no longer undefined** — `InstructionalGraphicStandards.md` **v01.00.00 Approved** §7 locks warning gold `#CCA700`, error red `#F44747` and syntax green `#6A9955`, **with no purple**, and its §6 forbids Heritage Blue on teaching cards. **PARKED: nothing renders either palette, the approved upstream file is mis-filed at a non-canonical path, and all of RoboLore is uncommitted — clear the filing first.** §26.7 is the session's own lesson: **a record that has been edited in place is not a record.** **RECOVERY NOTE — commit `3664bf8` correctly deleted the stray `ZUMO_SUPER_BIBLE (1).md` but overwrote this file with that stray's header, regressing the version line to v8.78 and DELETING the whole v8.79 S92 entry. Both were recovered byte-exact from `ae31126` before this entry was written. A duplicate of a canon file is not inert: deleting it and overwriting from it are one hand movement apart.**

v8.79, S92, moderate — **OPTION C: THE CALLOUT LABEL SPLITS INTO FAMILY WORD + TITLE, AND THE SESSION'S FIRST JOB FOUND ZERO OF 69 ALLEGED VIOLATIONS.** The §6.6a `Coach's`-prefix audit had never been run; run at S92 it returns **0 across all 279 family callouts and all 18 pages** — the four live `coach` strings are one HTML comment and three prose sentences. S91's 69-item list was entirely an artifact of a rule read to *"Labels are"*. Swept on DJ's ruling: **250 blocks, 178 of which gained a line**; label holds the family word ALONE (caps authored literally, no `text-transform`, so source string == rendered string), title beneath at 1.05em carrying the 8px gap; **72 bare blocks changed case only** — nothing to split, nothing to demote. Census 39,792→39,970 = **+178 exactly**, all other figures byte-identical incl. constructs at 171. `BookComponentStandard` **v01.8.0→v01.9.0** (§5.1 grew from one title element to two). `book_gates` **v1.25→v1.26, gate 35**, control-run against the pre-sweep tree where it fails with **230** — 20 short of the 250 edits, and the 20 are precisely the bare labels already all-caps and therefore already conformant. **THE SESSION'S REAL FINDING IS THAT ITS OWN RULING WAS TOO STRONG.** *"The scheme is the family of record"* was adopted after testing it on 142 blocks where scheme and glyph agreed — zero conflicts, read as confirmation. It was not: those 142 COULD NOT disagree, because the set was selected BY GLYPH. Gate 35, written to the ruling, immediately found **24 blocks borrowing §6.6a paint while carrying another family's glyph** — 7× the `going_deeper` hook, 7× DO THIS NOW, 2× WHAT YOU NEED, 8 one-offs. Asserting scheme-as-family would require breaking it 24 times, so the gate holds the AGREEING set and the 24 are logged. **AN ASSERT THAT CANNOT FAIL IS NOT EVIDENCE.** Two sweep bugs caught before shipping: the glyph splitter matched `&#` on entity-encoded lessons (the exact trap `lesson_inventory`'s own comment warns about, reporting 7 false glyph errors where there was 1), and the second element emitted unindented — found by READING the output, not by the asserts. **1.0em is PARKED, not declined**: 990 of 1,048 titles carry 1.05em, so it is a 990-block batch plus a §5.1 amendment, and it would cut S91's three-property justification for the block form to two. **CURIOUS→Going Deeper is confirmed by measurement** — all 7 blocks link to `going_deeper.html`, 7 for 7 — while **SEE stays its own family**: those blocks state expected output after an action, not enrichment, and merging them repeats the amber-scheme disease. 

v8.78, S91, moderate — **§24.10 THE PARSER IS THE DEFAULT INSTRUMENT; GREP READS ONE KNOWN LINE (NEW, DJ ruling: *"Grep has caused most of the issues we have faced in the book."*)**. He is right and the record is one-sided: every audit failure this canon has recorded is a TEXT match standing in for a STRUCTURAL question — `SECTION 8` matching `SECTION 8A`, an `=`-wrapper matcher blind in five lessons, a case-sensitive `Step` inventing a drift, a timer LABEL read as evidence of structure, and gate 30's substring test passing a GRADIENT containing `#6c757d` for its whole life. **S91 added one of its own:** a case-insensitive search for THE WALL matched the prose words *the wall* and placed the construct in five lessons it is absent from — the exact reverse of the truth, caught only because the count contradicted S90. The rule: a STRUCTURAL question goes to a parser (`lesson_inventory.py`; where it cannot answer, EXTEND it rather than grep around it); grep is legal for exactly ONE thing, reading a single line whose format is fixed and known, which is the use §12.6's file-is-source-of-truth rule depends on and the one use that has never failed; and **every count presented names the instrument that produced it** — a number with no named source is a lead, not a finding. **This is deliberately not a fourth restatement of §11/§24.6a/§24.6c.** Those already say a scan finding is a candidate and they did not stop it, including in the session that canonized this. A rule that must be remembered at the moment of temptation is not working; what actually closed these defects was TOOLING. The entry therefore changes what is REACHED FOR, not what must be recalled. Ungated by design — the check is whether a presented number can name its parser. Also S91, and pushed before this entry: **`BookComponentStandard` v01.5.0 → v01.6.0** — DJ approved the 26-family table and it is recorded in §7 on disk; Heritage Blue corrected to the RoboLore study's row C (`#162337` · `#43566B` · `#8C6A43` · `#C3A36A` · `#F4EBDD`) with all 8 tints, titles and contrasts RE-DERIVED rather than hand-patched, floor landing at 5.11 exactly where the book already was; brass's published contrast 5.44 corrected to 5.77 then 5.38 (it was bronze's number, copied along with bronze's title colour); Steel Blue `#6985AB` → `#708BAF` because row C's lighter navy dropped band text to 4.17. **`gen_component` v1.3 → v1.4** closing a §24.8 hole the push exposed: the marks check had a `not yet generated` branch, so a DELETED `images/marks/` and a correctly generated one both reported PASS — the real S91 defect FAILS under the new gate and PASSED under the old. 41 marks regenerated. No lesson file changed.) Prior: **v8.77** (v8.77, S89, moderate — **THE BUILD BANNER IS DELETED AND §24.9 IS NEW.** The third version home — an HTML comment before `</body>` in all 17 pages — is **gone**, with its `ZUMO Callout Standard v1.0 Applied` stamp, a conformance claim naming a document that never existed. **Three §5b/§25.6 statements were wrong in three different ways and each failure has its own shape.** (1) **COVERAGE:** both §5b gates iterated the 16 lessons while §25.6 iterated 17, so `going_deeper.html` was outside the version gate — and it is the one file that had drifted, shipping a visible `Version 01.0` against a hidden `v01.1.0`. The comparison logic was right all along; it never ran on the defect. (2) **DELIBERATE RELIANCE:** the v8.53 entry states in the open that the two-homes gate *"needed no edit — it greps raw source, and raw source includes comments, so a comment satisfies it exactly as a rendered banner did."* A gate named for visibility, with no notion of visibility, knowingly built upon for nineteen sessions. This is NOT the S87/S88 shape of an instrument silently failing — it was seen, judged harmless, and leaned on. (3) **RESTATEMENT:** §5b was corrected at v8.53; §9 restated the superseded "BOTH VISIBLE HOMES ARE MANDATORY" rule and was not, so the Bible contradicted itself for 19 sessions and the S89 handoff cited the wrong section as a result. All three are canonized as **§24.9**. **Corrections to the S89 handoff, recorded per §24.6c:** it claimed §5b demands two visible banners — §5b line 501 had already superseded that at v8.53, and the stale text was in §9; it claimed §5b's `vXX.XX.XX` format string contradicts its own examples — §5b's body carries no format string, the `vXX.XX` appears only inside the v8.31 CHANGELOG entry, which is a historical record and is NOT retro-edited; and it said three gates must change together — only TWO would actually have broken (§5b version, §25.6), the §5b date gate needed rewriting for correctness but would have kept passing. **book_gates v1.20 → v1.21**: both §5b gates moved to an explicit 17-page set with a coverage assert, comments stripped before matching visibility, agreement asserted between the hidden and visible homes; §25.6's two banner assertions removed; new `P(f)` label helper because `L(f)` slices `going_deeper.html` to `ml` and a gate that names the wrong file is its own hazard. Control-run both directions against the REAL going_deeper defect, not a synthetic — FAILED naming it, PASSED on the fix — and the old gates were run against the new source to prove the commit atomic (2 FAILED). **`BookComponentStandard.md` v01.0.1 is live at the repo root** with `images/icons/` (48 Bootstrap Icons + LICENSE); it is the callout standard's real successor. Census proves the deletion clean: lines 39,865 → 39,792 (−73, exactly the 17 banners), every other counter byte-identical — headings 1,025 · anchors 174 · fences 174 · part 64 · constructs 171 · mystery 56 · reveals 403. Applied S89, all 17 MINOR (the block is invisible, so nothing renders differently and the visible banner stays put per §5b): L01 **v03.10.5** · L02 **v03.2.1** · L03 **v03.16.1** · L04 **v04.9.2** · L05 **v04.11.2** · L06 **v04.14.1** · L07 **v04.10.1** · L08 **v04.9.1** · L09 **v05.7.1** · L10 **v02.7.1** · L11 **v02.9.1** · L12 **v01.10.1** · L13 **v02.9.1** · L14 **v02.11.1** · L15 **v02.8.1** · L16 **v02.5.5** · going_deeper **v01.1.1** (also correcting its visible banner to `Version 01.1`).) Prior: **v8.76** (v8.76, S87, moderate — **§4.5a THE BONUS BLOCK'S CAP AND ITS IN-FLOW POINTER (NEW, DJ ruling: *"B is fine"*)**. Two constructs around the bonus block were ungoverned and both are now generated from one constant and byte-gated. **THE CAP:** L03 shipped a `linear-gradient(135deg, #6c757d, #4d5358)` cap with 12px padding and a 40px top margin against a 14-lesson flat norm, and **passed gate 30 for its whole life because the placement check was a SUBSTRING test for `#6c757d`** — which a gradient containing `#6c757d` satisfies. A substring test cannot distinguish flat from gradient. **THE POINTER:** the FINISHED EARLY callout existed in L02–L09 and was **ABSENT in L10–L15**, so six lessons offered no in-flow route into their bonus block at all — only one nav pill among twelve to fourteen — and its livery had drifted into **three strata (2/2/4) cutting ACROSS the families**, Observation splitting down the middle. Six pointers authored from each lesson's own planted defects (never from card titles) and all 14 normalised to B. **B was chosen over the 4-lesson plurality because `#6c757d` is the §10+end section-group color — the livery is DERIVED from the nav scheme, where C's `#e3f2ed`/`#3d8b6e` have ZERO Bible mentions.** The mark stays with the family (🎯 Practice, 🏁 Observation/Sabotage). **Rebrand-ready by construction:** each asserts ONE constant, so a RoboLore guide changes `BONUS_CAP` and `FE_BOX` and all 15 blocks repaint and re-prove; Canvas strips `<style>` and `class=`, so generation is the only mechanism that scales. **book_gates v1.18 → v1.20**, gate 30 tightened + **new gate 32**, control-run five ways with the OLD gate PASSING both cap injections. `gen_bonus_banner.py` v1.1 → v1.2. Applied S87, all MODERATE (rendering changes, both §5b banners moved): L02 **v03.2.0** · L03 **v03.16.0** · L06 **v04.14.0** · L07 **v04.10.0** · L08 **v04.9.0** · L09 **v05.7.0** · L10 **v02.7.0** · L11 **v02.9.0** · L12 **v01.10.0** · L13 **v02.9.0** · L14 **v02.11.0** · L15 **v02.8.0**. Census proves it additive: lines 39,837→39,865, every other counter byte-identical. **Verified RENDERED, not just parsed** — L12 and L08 read back under OCR with authored prose intact.) Prior: **v8.75** (v8.75, S86 addendum 2, moderate — **§24.8 CAN THE INSTRUMENT DISTINGUISH THE TWO ANSWERS? (NEW, DJ ruling)**. §24.7 was one instance; this is the rule it instantiates, and DJ called it out as the session's most load-bearing product while it existed only in a chat message — **approved prose that was never written to disk**, the §12.4 failure. S86 produced **FIVE** moments where something looked settled and was not, and **every one was a failure of the instrument, not the book**: (1) `grep data-kind` reporting `book_gates.py` as a non-consumer when it consumes the PARSED value; (2) an injected control landing in a `solution` reveal that §20.1 ignores by design, so a working gate read as broken; (3) an unconditional Brain Check NORM line printed under `--- ANOMALIES ---` and misread as a standing lead; (4) a renderer's unpainted black tail reading as a missing banner; (5) `api.github.com`'s HTTP 403 read as a proxy denial when it was GitHub's own rate limit and carried no `x-deny-reason`. **#5 was committed ONE MESSAGE AFTER §24.7 was written**, by the same author about the same error class — knowing the rule confers no immunity, running the test does. The test: **if the answer were the OPPOSITE, would this instrument look different?** If not, its report is not evidence but its silence. Three recurring shapes recorded: a name-scoped search misses value-scoped use; an absence from an instrument is not an absence in the book; a container is not its contents. Ungated by design, like §24.6b/§24.6c/§24.7. No lesson, gate or tool versions changed.) Prior: **v8.74** (v8.74, S86 addendum, moderate — **§24.7 SEEING THE RENDERED PAGE FROM THE SANDBOX (NEW, DJ ruling: *"yes"*)**. The rendered-Pages debt had been unclearable for three sessions because `weymuth.github.io` is not on the sandbox egress allowlist (`x-deny-reason: host_not_allowed`; DJ added the host mid-session and it did not take effect, so the container's allowlist is evidently fixed at start and needs a fresh conversation). **`wkhtmltoimage` is installed**, the clone's HTML is byte-identical to what Pages serves, and a render can be viewed directly — so the item can close in the sandbox as a STRONG LEAD, never as a cleared eyeball. **The rule exists because a false verification nearly shipped**: whole-page renders of these lessons produce a canvas 38,000–65,000 px tall whose TAIL IS PURE BLACK (bottom quarter: L04 100% · L05 100% · L12 100% · L14 81% · L13 62%) with no error and a perfect-looking top, and **three of the eight banners under inspection sat inside that dead zone**, including the first crop read. One banner reported as *"colour NOT FOUND"* was merely unpainted — **an absence produced by the instrument reads exactly like an absence in the book.** Method: window every render with `--crop-y/--crop-h` (0% black at every depth tested), locate targets by their own colour (`background-color`, NOT `background`), and **prove the window contains the target before reading it** — §24.6b applied to an image. Ungated by design, like §24.6b/§24.6c: there is nothing in the book to assert against. **Applied same session — S84 batch 1's eight unverified PART seams were rendered and all eight are correct**: L04 P2→§4 · L05 P2→§4 · L05 P4→§9 · L12 P3→§7 · L13 P3→§7 · **L13 P4→§9 (the plum-welded-onto-§7 defect is NOT present)** · L14 P3→§7 · L14 P4→§9; subtitles and the removed `opacity: 0.7` confirmed from the HTML independently. No lesson, gate or tool versions changed.) Prior: **v8.73** (v8.73, S86 moderate — **THE §4.5 TAGGING BATCH, and a gate that would have STOPPED GATING WITHOUT FAILING.** DJ ruling: three namespaced values, *`bonus-practice`/`bonus-observation`/`bonus-sabotage`*. 68 tags across 14 lessons — **42 renamed** (`bonus`→practice 12 · `mystery`→observation 16 · `mystery`→sabotage 14) and **26 newly tagged** (L04 5 · L10 5 · L12 4 · L13 4 · L14 4 · L15 4), every edit under a `count==1` assert. **The 30 `mystery` tags were never one family** — 16 Observation, 14 Sabotage — so the rename could not be a 1:1 map, which is the whole reason the shared value was hiding a real distinction. **THE DANGEROUS PART: `book_gates.py` contains the string `data-kind` ZERO times** and is nonetheless the critical consumer, reading `kind` through `lesson_inventory.build()` at §20.1's `c['kind'] == 'mystery'`. Renaming the lessons alone would have made that comparison match nothing, dropping every Sabotage reveal back to the ≥3-statement-line floor — **the exact condition that let L08 pass on luck for eight sessions (S80)** — and **the COVERAGE assert could not have caught it**, because it counts all constructs and tagging 26 more cards makes that number go UP. A gate can stop gating without failing. Demonstrated rather than argued: same tree, one planted line inside a `hint` in a Sabotage card, old value **PASSES**, new value **FAILS**. §20.1/§20.2 wording kept per DJ ruling (*"keep the existing wording and swap the value, leave a note"*), reasoning parked in place. **NEW gate 31 `§4.2 every bonus card is tagged and its data-kind names its family`** — §20.2 had only ever been asserted for UNIQUENESS, never PRESENCE, which is why 28 untagged cards sat inside a 30/30 book; it rides gate 30's already-proven banner count and control-run four ways (unfixed tree FAILED naming all 8 renames and all 6 untagged lessons · one tag removed FAILED · one card set to the wrong family FAILED · untouched PASSED). **L16's hold now expires by itself** at four cards, and a lesson can no longer fall out of both `BONUS_TABLE` and `BONUS_HELD` into silence. The card-count logic is now ONE definition shared by gates 30 and 31 per the S83 rule — and because that refactor touched a PASSING gate, gate 30's own decisive S85 control was re-run (banner byte-perfect, one real card deleted → still FAILED naming the count). **`tutor.html` v1.0.0 → v1.1.0**: three optgroups, and repairing `known[]` closed a live defect — the 12 L02/L03 bonus cards had been rendering TWICE in the picker, found by EXECUTING the grouping logic rather than reading it. **§24.6c twice more** (both S86 handoff claims wrong: *"L12–L16 div-titled"* — only L12 is; *"newproject.html (3)"* — zero `data-kind` there), and **a control of mine misfired and was reported as such**: the first silent-gate injection went into a `solution` reveal, which §20.1 ignores by design, so the gate was right and the injection was wrong — §24.6b again. Census proves the batch was attributes only: lines 39,837 · headings 1,025 · anchors 174 · fences 174 · part 64 · reveals 403 all byte-identical to S85; only constructs 145→171 and the mystery column 30→56 moved, and `--anomalies` is now EMPTY. **book_gates v1.17 → v1.18 (31 gates)**, `lesson_inventory` v1.0.4 → v1.0.5. Applied S86, all 14 MINOR (data attributes do not render; hidden comment only, visible banners untouched per §5b): L02 **v03.1.1** · L03 **v03.15.1** · L04 **v04.9.1** · L05 **v04.11.1** · L06 **v04.13.1** · L07 **v04.9.1** · L08 **v04.8.1** · L09 **v05.6.1** · L10 **v02.6.1** · L11 **v02.8.1** · L12 **v01.9.1** · L13 **v02.8.1** · L14 **v02.10.1** · L15 **v02.7.1**; L01 and L16 unchanged. **LEADS LOGGED, NOT FIXED:** L12's bonus block holds ZERO `<details>` — the only Sabotage lesson with no reveals; L15's four Sabotage reveals are `hint`-only with no solution reveal (read, and they are genuine questions, so no §20.1 leak); four `data-reveal="mechanism"` blocks exist book-wide and `mechanism` is not on §20.1's strip whitelist; a `__pycache__` `.pyc` is committed, same class as the standing `.DS_Store`.) Prior: **v8.72** (v8.72, S85 moderate — **§4.5 THE BONUS BLOCK IS THREE FAMILIES, AND THE BANNER IS GENERATED (NEW, DJ ruling: *"Approve"* / *"keep per topic nouns"* / *"Finish the 21 now"* / *"Yes, supersede the v8.14 canon"*)**, **SUPERSEDING the v8.14 S20 "Bonus" vocabulary canon**. The queue item was *"L13/L14 doubled 🕵️, one-line fix each"*; reading it found fifteen banners in six emoji strata, two encodings, two separators and three pill labels — and the drift was CONCEALING a real distinction. Three families by method: Practice 🔨 (L02–L03, write new code), Observation 🔍 (L04–L07, **nothing is broken**), Sabotage 🕵️ (L08–L16, someone else broke it). **The three-vs-two argument is a harm argument**: collapsing Observation into Sabotage sends a student hunting for a defect in L04–L06 where none exists. **L07 resolved by method, not vocabulary** — zero Maker defect links, every card tells the student what to change, its own intro reads *predict, break, build, explain, undo*; its *"Sabotage science"* and *"detective work"* prose was a word collision and was reworded. Generated in one pass: **14 banners, 14 nav pills, 6 prose links, 4 callouts, 21 card titles renamed *Mystery N* → *Experiment N*, and 5 cross-references** that would otherwise have named a title that no longer existed. **book_gates v1.16 → v1.17, gate 30**, control-run seven ways including the independence test — banner byte-perfect with one real card removed FAILED naming the count. A gate bug was caught en route and the BOOK was right: the placement regex demanded `</div>` at offset zero and L04/L05 have a newline there. **§24.6c twice**: a 12,000-char extraction window stopped inside the block and misreported L02/L03 as 5 and 4 cards when both hold six — the lessons' own callouts were right; and L03's *"Extra Practice"* pill was called the prototype when it is **the very drift the S20 ruling was written to kill**. New tool `gen_bonus_banner.py` v1.1. **L16 HELD OUT by ruling** (2 cards vs 4). **Tagging deliberately NOT aligned** — `data-kind` still reads `bonus`/`mystery` and ~28 cards carry none; that batch touches §4.2, §4.3 and the §20.1/§20.2 pair. Applied S85, all 14 MODERATE (banner text renders differently in every one, both visible banners moved per §5b): L02 **v03.1.0** · L03 **v03.15.0** · L04 **v04.9.0** · L05 **v04.11.0** · L06 **v04.13.0** · L07 **v04.9.0** · L08 **v04.8.0** · L09 **v05.6.0** · L10 **v02.6.0** · L11 **v02.8.0** · L12 **v01.9.0** · L13 **v02.8.0** · L14 **v02.10.0** · L15 **v02.7.0**; L01 and L16 unchanged.) Prior: **v8.71** (v8.71, S84 batch 2 moderate — **§25.10h BRAIN CHECK PLACEMENT (NEW, DJ ruling: *"Yes, and add to bible"*)** plus **§12.2 THE DELETION PROCEDURE MOVES OUT OF THE HANDOFF**. (1) The Brain Check family had **no placement rule**, only an observed practice — the §6.8a shape. Canon: **BC01 is a direct child of `<body>` whose NEXT SIBLING seats `#section-6`**; **BC02/03/04 sit one div deep inside the gray `#6c757d` §10 panel**; BC01's PREVIOUS sibling is deliberately unspecified because it legitimately varies (L01/L02 a §5 subsection banner, L03 a predict box, L04–L09 §5's green panel) and asserting it would gate an accident. **The norm is 9/9, not the 8/9 the S83 handoff recorded** — that figure was counted before S83's own L06 fix landed, so a norm quoted from a handoff is a lead too and gets recounted against the files. **gate 29**, COVERAGE at nine converted lessons, control-run three ways with every injection re-parsed and confirmed in shape first: **L06's S83 defect re-introduced FAILED** naming the depth AND the lost §6 sibling · a BC03 lifted out of the gray panel FAILED · a removed `brain-check-01` tripped COVERAGE at 8. A gate that catches the one defect its construct has ever actually had is the standard to aim for. (2) **The deletion procedure had been documented only in the session handoff — the very file being deleted** — so it disappeared exactly when needed and was missed twice (`fb70426`, and again this session, where all 21 overwrites landed and only the deletion stayed behind; a push that LOOKS successful is the hazard). Moved to `PUSH_WORKFLOW.md`, and **gate 28** asserts exactly ONE `ZUMO_SNN_HANDOFF.md` in the root, excluding §19 records; control-run both directions (two FAILED, zero FAILED, one PASSED). **A procedure stored inside the artefact it operates on is not stored.** (3) **§6.8 addendum — L03's three non-divider PART notes retired** per DJ ruling; `End Part 3 content` sat 163 lines inside the tail after PART 4, already lying. **book_gates v1.15 → v1.16 (29 gates)**. Applied S84 batch 2: L03 **v03.14.3** (minor, notes invisible, visible banner unchanged per §5b); `PUSH_WORKFLOW.md` gains its deletion section.) Prior: **v8.70** (v8.70, S84 moderate — **§6.8 THE PART DIVIDER IS GENERATED FROM THE SECTION SPINE (rewritten, S84, DJ ruling: *"Fix them all"* / *"Fix and have no drift"* / *"Yes"*)**: the queue item was *"L02/L06/L15/L16 carry zero PART banner comments"*, called the biggest unexamined structural item. **The premise was wrong** — all sixteen lessons carry four visible banners in the correct twelve colors — and reading it produced four defects instead. (1) **Half the zeros were a matcher artifact**: `lesson_inventory.py` required the `=` wrapper, so L02's `PART 1: THE CHALLENGE` (3 comments) and L06's `PART 1 DIVIDER` (4) both counted as zero; only L15/L16 truly had none. That is §6.8a's blindness repeating one construct over. (2) **FIVE BANNERS CAPPED THE WRONG SECTION and nothing had ever looked** — L12 PART 3, L13 PART 3+PART 4, L14 PART 3+PART 4 each sat one section boundary early, and because `border-radius: 8px 8px 0 0` + `margin: 22px 0 0` FUSE the cap to the banner beneath, L13 rendered a plum *"PART 4 — Challenges / Section 9"* welded onto §7's rose Calibration Ladder. Visible on every page load, invisible to all 26 gates. (3) **Three content deviations**: L04 PART 2 titled *Hands-On Setup & Programming* (logged S72, unfixed twelve sessions), L05 PART 2 claiming *Sections 4–7* — a section its own PART 3 also claims — and L05 PART 4 claiming *Sections 9–10* where §10 is the untitled tail, plus opacity `0.7` on two L05 blocks. (4) **The comment had drifted eight formats across 51 instances and several were LYING**: L02's read `PART 1: THE CHALLENGE` above a banner reading *Theory & Concepts*, the same shape as L01's fence reading `KEY CONCEPTS` against a *Background Theory* banner. All four resolved in ONE GENERATE per the §6.8a precedent, because every field is derived: color/title/subtitle from the PART number, the `Sections 7–8A` vs `7–8` variant from whether `section-8a` exists, the seat from the section spine. **The Bible's own snippet was the stale one** — it specified `border-radius: 8px; margin: 22px 0 10px`, a DETACHED box, against 64/64 live blocks at `8px 8px 0 0` / `22px 0 0`; the live form is canon. **The sweep is defined on the CONSTRUCT, not the lesson**: L03's `End Part 1 content` notes are not dividers, and L02's `<!-- ==== -->` rule idiom brackets every landmark and legitimately yields **10 pre-existing adjacent rule pairs**, so absorbing "any rule comment abutting a divider" would have eaten real content — check what a cleanup rule deletes in its WORST lesson before adopting it. **book_gates v1.14 → v1.15, gate 27**, byte-exact whole-block comparison + own-fence placement + stray-comment rejection + a COVERAGE assert at 64, with **byte-canonicity and placement asserted INDEPENDENTLY** (the first draft bailed out of the placement check on a byte failure, which would have let an encoding drift hide a misplaced banner). Control-run **six** ways: untouched FAILED · re-introduced L13 displacement FAILED naming `PART 3 caps SECTION 6` · L05 subtitle reverted FAILED · deleted comment FAILED · `&mdash;` restored in L11 FAILED · whole block removed tripped shape AND COVERAGE. **The displacement control PASSED on its first run and the INJECTION was at fault, not the gate** — it had truncated the block at its first `</div>`, which is the *title* div, so only a fragment moved and the `blk in s2` assert passed on a surviving prefix. §24.6b is not "assert something changed" but **assert the injection landed in the shape you intended**, re-parsed and read back. New tool `gen_part_banners.py` v1.0 at repo root. **`lesson_inventory.py` v1.0.3 → v1.0.4** — the `part` column is now enforced by gate 27, so its matcher no longer depends on a format nothing guarantees; count is **64**, four per lesson in all sixteen. Applied S84, all 16 lessons: MODERATE (rendering changed, both visible banners moved per §5b) L04 **v04.8.0** · L05 **v04.10.0** · L12 **v01.8.0** · L13 **v02.7.0** · L14 **v02.9.0**; MINOR (generated comment + entity encoding, renders identically, visible banner untouched) L01 v03.10.4 · L02 v03.0.3 · L03 v03.14.2 · L06 v04.12.5 · L07 v04.8.4 · L08 v04.7.5 · L09 v05.5.3 · L10 v02.5.4 · L11 v02.7.4 · L15 v02.6.4 · L16 v02.5.4.) Prior: **v8.69** (v8.69, S83 moderate — **§20.1(5) THE LEAK GATE'S SCOPE IS THE RULE, AND ITS TWO LOGGED DEFECTS WERE BOTH REAL**: the §20.1 per-card bounding used `rfind('<div')`, which is correct for an element-bounded `<div data-challenge>` **by accident** and wrong for every heading-bounded `<h4 data-challenge>` — each h4 marker inherited its enclosing PANEL. Demonstrated live rather than argued: one injected block in L07 `7.m3` came back as **five findings**, `7.m1` through `7.m5`. Fixed by IMPORTING the span from `lesson_inventory.py` instead of writing a third regex, so the two tools share one definition; the port is verified by reproducing the read-verified **5/8/2** code-line counts for L09 `9.m3`–`9.m5` against the old gate's fictional **3/8/17**. Second defect closed the same pass: `data-kind="mystery"` now has **no line threshold**, because §25.10g already makes a mystery reveal a `solution` and its planted snippets run 1–2 lines — which was **the sole reason L08 passed for eight sessions** (S80). A threshold is not an exemption. **book_gates v1.13 → v1.14**, control-run five ways with every injection asserted landed first: untouched PASS · 4-line block in a heading-bounded mystery hint FAILED naming `7.m3` **only** where the old gate named five · `8.m1` retyped `solution`→`hint` FAILED where **the old gate PASSED** · the original S79 shape re-injected into element-bounded card `1.11` FAILED · and a deliberately broken port tripped a new **COVERAGE assert**, added because a gate whose population silently empties is an ungated rule. **§24.6c CORRECTION RECORD — the carried L02 `2.t4` item is CLOSED as an ARTIFACT OF THIS VERY DEFECT.** `2.t4` is a `<strong>` spanning **one line** with **zero `<details>`**; the old window opened its "card" four lines early and swallowed a `check` reveal **17 lines past its end**. The code is real and the reveal is real — it is a §6 Step-4 build-along self-check owned by no construct. S81 was right that `2.t4` holds no reveal; the reason is now known, and the item needed no ruling. **Census that the correct bounding finally made possible:** 33 kept reveals hold `<pre>` book-wide and **all 33 sit outside every construct** — 31 §6 `check` blocks, one L02 §8 `troubleshoot`, one L10 §6 `hint` spelling out the fix to a red build the lesson instructed the student to plant. **Zero in §9, zero past §10, zero leaks.** Recorded as the pair-rule: an UNTAGGED challenge hiding its answer in a `hint` is invisible here, so §20.2's marker gate is the other half of the guarantee. **`lesson_inventory.py` v1.0.2 → v1.0.3** — its §6.8a comment still read *"only 6 lessons carry any"*, stale **twice over**: that figure was the matcher artifact §6.8a was written to kill, and since S82 all sixteen carry 174. **S83 FIRST ITEM, per DJ (*"let's fix l06 at the beginning of 83"*) — L06 brain-check-01 lifted out of §5's content panel.** BC01 was the **last of 49 direct children** of §5's `border: 2px solid #3a7d5c` panel, sitting **after** §5's own `↑ Back to top` link, with §6's banner the next element once the panel closed. So the standing question — does §5 legitimately close later — answers itself: **no**, §5's content ends at its back-to-top link and the `</div>` simply sat one element too late, rendering BC01 inside the green box in L06 and outside it in the other eight. Reading order was already correct; only nesting was wrong, so the repair is **relocating a single `</div>`** to reproduce L05's byte-pattern at that seam. Verified against four conforming lessons (L05, L07, L08, L09), all identical in shape. Asserts: both anchors unique at count 1 · `<div`/`</div>`/`<p`/`</p>`/`<details>` multisets unchanged · normalized visible text AND the non-empty text-line sequence identical · re-parse confirms BC01's parent is `body`, its previous sibling the panel whose last child is the back-to-top `<p>`, its next sibling the banner seating `#section-6` · panel child count down by exactly one. **Note the first assert was WRONG, not the edit** — strict `get_text('\n')` equality failed on two blank separator lines that move when nesting changes; diffed before overriding, per the S82 no-op lesson. `lesson_inventory --anomalies` is now **empty** — the last standing lead in the book. L06 **v04.12.3 → v04.12.4**, minor, visible banner unchanged per §5b. **Logged, NOT canonized — the Brain Check family's placement has no rule**, only a norm (BC01 directly under `<body>`, 8 of 9), which is precisely the §6.8a shape: a construct with an observed practice and no canon drifts, and the instrument reports it as a *lead* because there is nothing to check it against. A placement gate is the obvious follow-on and **needs a DJ ruling first**. **No other lesson content changed and no other defect was found.** Prior: **v8.68.1** (v8.68.1, S82 minor — **§6.8a AND §6.9 ENFORCEMENT TIGHTENED, plus the live defect the loose gate had been passing**: the v8.68 gate compared document-ordered LISTS of fences and anchors, so content and order verified while PLACEMENT did not — and a third verification pass on an independent parser (DOM traversal, sibling adjacency, no regex) found **L06 and L07 §5 anchors were not inside their banner div at all**. The §5 banner had swallowed the PREVIOUS section's back-to-top link and closed early, leaving `<div id="section-5">` as a bare sibling in the content panel: on the rendered page §5's coloured cap showed a back-to-top link where its title belongs, and the title rendered as bold text at the top of the white box. Pre-existing (confirmed against the untouched pre-S82 clone — L05/L08 were already correct), and of the §24.6 class that passes tag balance BECAUSE the counts work out. Swept the CLASS not the instance per §24: exactly **2 of 174** anchors were displaced, both §5, both repaired by reordering to L05's arrangement — same tag multiset, visible text asserted unchanged, anchor parent re-verified as a banner by re-parse. **book_gates v1.12 → v1.13** replaces the list comparison with a per-anchor walk: the anchor must sit in a banner, the fence must be adjacent to that banner with only whitespace between, and — the part that actually caught it — **the anchor must open IMMEDIATELY inside the banner**, because the nearest preceding `<div>` is NOT necessarily the parent when a `</div>` intervenes. The first tightening attempt still PASSED the re-introduced displacement for exactly that reason; the injection was verified live before the gate was blamed, per the same-session no-op lesson. Control-run three ways: displacement re-introduced FAILED naming the intervening element, a stray `<p>` between fence and banner FAILED, untouched copy PASSED. Applied S82: L06 **v04.12.3**, L07 **v04.8.3**. **Still open, S83 first item per DJ:** L06's brain-check-01 sits inside §5's CONTENT panel — a separate deviation from the anchor displacement, unmoved by this repair.) Prior: **v8.68** (v8.68, S82 moderate — **§6.8a THE SECTION FENCE IS GENERATED FROM THE ANCHOR SPINE (NEW, S82, DJ ruling)**: the `<!-- ===== SECTION N: TITLE ===== -->` comment had never been canonized — zero rules in this Bible before today — so it drifted five ways across ten lessons and was absent from six. `lesson_inventory.py`'s matcher required the `=` wrapper, so it was **structurally blind in five lessons**, which is why L09's missing §7 fence read as the only gap in the book when there were **nine across seven lessons**. Offered a widened matcher, DJ ruled the other way — *"Why widen the fence. Can't we just fix the issues that are causing the fence issues"* — and that is the §24 pattern: a widened regex ratifies the drift permanently. Because the fence is DERIVED from the `id="section-N"` spine the fix is a GENERATE and not a repair: **100 legacy fences removed, 174 canonical written, one per core anchor**, resolving every gap, stale duplicate (L03's `(NEW CANONICAL)`, L08's `Code Structure`+`Code Walkthrough` before one banner), mislabel (L08's `Section 7: Troubleshooting`) and format variant in one pass with no per-instance judgement. The title is derived from the banner and DJ ruled it stays (*"Keep title in it"*), which is safe only because the gate regenerates and compares it — L01's fence read `KEY CONCEPTS` against its own banner's *Background Theory*, so **the title was already lying** before it was gated. **book_gates v1.11 → v1.12** adds gate 26, control-run three ways (unfixed FAILED, 79 non-canonical + 16 count/title mismatches; a deleted fence FAILED; a fence left stale after a banner rewording FAILED). **§24.6c CORRECTION RECORD**: the S82 handoff's *"L09 §7 has no SECTION fence and §8 has TWO"* was half right — the §7 gap was real, but *"§8 has TWO"* was a PREFIX ARTIFACT, `SECTION 8` substring-matching `SECTION 8A`; L09 fenced ten distinct sections with zero duplicates. The v8.67.1 entry's *"`fnce` (fence comments, 75)"* likewise conflated two constructs — 34 section fences plus 41 §6.8 PART banners — so **`lesson_inventory.py` v1.0.1 → v1.0.2** splits the column into `sfnc` (174) and `part` (41). Logged, not fixed: L02/L06/L15/L16 carry **zero** PART banner comments. Applied S82, all sixteen minor (invisible comments, visible banners unchanged per §5b): L01 v03.10.3 · L02 v03.0.2 · L03 v03.14.1 · L04 v04.7.1 · L05 v04.9.3 · L06 v04.12.2 · L07 v04.8.2 · L08 v04.7.4 · L09 v05.5.2 · L10 v02.5.3 · L11 v02.7.3 · L12 v01.7.4 · L13 v02.6.3 · L14 v02.8.3 · L15 v02.6.3 · L16 v02.5.3.) Prior: **v8.67.1** (v8.67.1, S81 minor — paperwork: `lesson_inventory.py` shipped **v1.0** and was corrected to **v1.0.1** the same session. Its summary table headed one column *fence* while printing the `id="section-N"` ANCHOR count — the label had been left behind by the mid-session refactor that made anchors the spine — so the table read *11 fence comments* for L02, which has **zero**. Data right, label wrong, which is the §24.6c failure the tool exists to prevent, found by the push-verification ritual re-running it against the fresh clone. Split into two columns, `sect` (anchors, 174 book-wide) and `fnce` (fence comments, 75). No rule changes.) Prior: **v8.67** (v8.67, S81 moderate — **§25.11 A REVEAL'S VISIBLE LABEL MUST AGREE WITH ITS `data-reveal` TYPE (NEW, S81, DJ ruling)**: DJ, on being shown nine reveals typed `solution` whose summary still read *“💡 Hint”* — *“I don't understand, but If it's a hint, then say hint. If its a solution, then call it a solution.”* The nine are exactly the blocks §25.10g retyped at S80, which was done **attribute-only** and therefore moved the type while leaving the label contradicting it. A label is not cosmetic: it is the student's only signal for whether opening the block spends their attempt, and §20.1 strips `solution` from the tutor, so a block labelled *Hint* is withheld from the model while promising help to the reader. **L11 was the model for the THIRD consecutive session** — its four mysteries are the only ones in the book where type and label already agreed (`solution` + *“💡 Answer”*), so the fix was to copy a live precedent, not to invent wording. Census of all 30 mystery reveals: L05/L06/L07 + L08 `8.m3` are `hint` + *Hint* (consistent, and verified to hold **no `<pre>` at all**, which is why §25.10g correctly left them alone); L11 ×4 already correct; L08 ×4 + L09 ×5 were the drift. The label edit is text-only inside each lesson's own markup — **L08 holds five copies of the identical bare summary string and one of them (`8.m3`) must NOT change**, so every edit was located by heading-bounded offset per §6.12c with a +2-bytes-per-edit assert, never by string replace. **book_gates v1.10 → v1.11** adds `§25.11 reveal label agrees with reveal type`, deliberately NARROW per §24.6c (the label vocabulary is legitimately varied — 62 *reveal solution*, 13 *Answer*, 9 *worked version*) so it asserts only the two contradiction shapes verified by reading; control-run three ways (unfixed source FAILED catching exactly the nine and nothing else; fixed tree PASS; reverse drift injected into `8.m3`'s label FAILED). **NEW TOOL `lesson_inventory.py` v1.0.1** — one parse per lesson emitting the full structural table (every heading with div depth, every reveal with its type AND parent construct, every marker, all version homes), so session work queries a table instead of grepping HTML; it has NO exit code and NO pass/fail by design, because §24.6a says a parser is necessary and not sufficient. It reproduced the read-verified 5/8/2 mystery code-line counts where the §20.1 gate reported 3/8/17. Also fixed: **L12 shipped a literal unescaped `<Wire.h>` in §6 Step 5 prose** — the browser tokenises it as an element, so the Tip callout rendered *“The #include  goes at the TOP of the file”* with the filename gone; invisible to the §24.6 parse gate because its `_STRICT` set does not cover unknown tags. Escaped to match `<pre>` #13 twelve lines above it, which had been correct all along. **§25.12 NEW — L02 `2.t1`'s answers block was the only `<details>` in the book carrying no `data-reveal` at all** (403 elements, 402 typed), and §20.1's strip list is a whitelist, so it had been shipping its worked answers to the tutor; typed `solution` on the precedent of `2.t5` in the same lesson. Note the carried open item naming *L02 `2.t4`'s `check` reveal* does not match the file — **`2.t4` contains zero `<details>`** — so that item is re-scoped to SUSPECTED per §24.6c. Applied S81: L02 **v03.0.1**, L08 **v04.7.3**, L09 **v05.5.1**, L12 **v01.7.3** (all minor, visible banners unchanged per §5b).) Prior: **v8.66** (v8.66, S80 moderate — **§25.10g THE MYSTERY REVEAL IS A `solution`, NOT A `hint` (v8.66 — NEW, S80, DJ ruling)**: DJ, on being shown the §20.1 gate failing L09's newly-tagged mysteries — *"Wouldn't we want it to have a solution drop down?"* — and he is right, which means the gate was right and the book was wrong. §11 (v8.17) says a mystery DISPLAYS its planted line (*"The planted constant:"* / *"as planted:"*) and that rule is about display, not about reveal TYPE; §20.1 (v8.37) already said the quiet part explicitly — *a debugging-mystery bug+fix reveal must be typed `solution` or it leaks*. **L11 had been compliant all along** (its four mysteries are `solution`), so this was never a coin-flip: it was a 4-lesson drift against a live precedent. Census: planted code sitting in a `hint` existed in exactly **two** lessons, L08 (4 blocks) and L09 (5) — L05/L06/L07 mysteries carry hints with no code, which is why the drift stayed invisible. **The gate passed L08 for eight sessions on snippet length alone**: §20.1's detector needs ≥3 statement lines and L08's planted snippets run 1–2. A threshold is not an exemption, and a gate that passes by luck is an ungated rule. Retyped attribute-only, verified by offset with a +4-bytes-per-edit length assert. **Two gate defects logged, neither fixed**: (a) §20.1 has no notion of `data-kind="mystery"` and would have to be re-reasoned if the ruling ever inverts; (b) **its per-card bounding bleeds** — it reported 3/8/17-line blocks recurring across 9.m3/9.m4/9.m5 where the truth is one block each at 5/8/2 lines, the same nested-card bounding defect that keeps bonus-challenge leak coverage SUSPECTED. The failure was diagnosed by READING the three cards; the gate's own line counts were fiction. **L09 IS THE NINTH CONVERSION** (v05.4.2 → v05.5.0). Its ancestors were **four**, not the two §25.10f recorded: *Technical Skills* (5), *Conceptual Understanding* (4 Q&A, answers in open prose, no reveal), *Problem-Solving* (4), *Knowledge Check* (3, already `quiz`). §25.10c's diff-the-duplicates rule paid again but inverted from L05: *Conceptual Understanding* was a strict SUPERSET of *Knowledge Check* — items 1–3 word-identical, and CU alone carried the enum question — so **Knowledge Check migrated verbatim would have FAILED §25.8's floor at 3 items.** Per DJ ruling (*"Fix and go with KC"*) BC03 = KC's three answers verbatim plus CU's enum item, extended to KC's depth, citing §3.1 · §3.4 · §3.6 · §3.5 — **neither ancestor carried a single §-citation**, so §25.2's name-your-section rule was authored in, not migrated. BC01 = **5 authored**: L09 had NO Mental ancestor (zero `check` reveals, zero pre-§6 `quiz`, zero TRY IT), so the handoff's *"redistribution job, not an authoring job"* was wrong. BC02 = §2's **seven** objectives character-exact per §25.5 (the live *Technical Skills* list had five and was NOT the source). BC04 = L09's live *Reflection: Draw Your State Diagram* migrated plus two authored — **Engineer's Log is NOT BC04's ancestor**; it survives as a separate block after BC04 in all four prior conversions. *Calibration Data Record* stays outside the family per the S78 ruling. Five mysteries tagged `9.m1`–`9.m5`. Applied S80: L09 **v05.5.0**, L08 **v04.7.2** (attribute-only, visible banner unchanged per §5b).) Prior: **v8.65.1** (v8.65.1, S79 minor — **§6.12c STACKED SIBLING REVEALS MUST AGREE ON SUMMARY PADDING**: two `<details>` reveals sitting as adjacent siblings render their disclosure triangle and label at different left insets when one `<summary>` carries `padding` and the other does not — visible on the page, invisible to every other gate. Found by DJ on the rendered L01 C11 immediately after the v8.65 split, which is what created it: the new `solution` summary carries `padding:15px 20px` and the `hint` above it carried none. Census across all sixteen lessons: summary padding is stratified book-wide (hint 47 bare / 11 padded, solution 59 padded / 50 bare, catchup 76 bare) — §6.12c drift, not rot — but **exactly one stacked pair disagreed**, and it was the one just authored. Fixed by padding L01 C11's hint summary; the identical bare-summary string occurs **12 times in L01**, so the edit was scoped by offset per §6.12c rather than by string. **book_gates v1.9 → v1.10** adds the gate, control-run both directions (unfixed L01 FAILED; a padding mismatch injected into an agreeing L03 pair FAILED). Note the detector's first version returned zero because it treated the first reveal's own body as “prose between the siblings” — depth-match the `</details>` before comparing neighbours. L01 v03.10.1 → **v03.10.2**, cosmetic so the visible banner is unchanged per §5b.) Prior: **v8.65** (v8.65, S79 moderate — **§20.1 THE STRIP LIST IS A WHITELIST, SO EVERY KEPT TYPE IS A PUBLICATION CHANNEL**: the tutor strips only `data-reveal="solution"`, so a finished answer inside a `hint` looks withheld to a reader and is shipped to the model. Found live in **L01 Challenge 11** — the complete battery-check answer (threshold `4500` + the `LOW BATT!` body, filling the exact blank the card asks the student to fill) had sat inside the hint through eight sessions of L01 edits. Fixed by SPLITTING, not retyping: the coaching content (that `readBatteryMillivolts()` exists, the NiMH voltage table, the USB-falsifies-the-reading catch) stays `hint` so the tutor keeps it; the lead-in plus the worked code move into a sibling `<details data-reveal="solution">` in L01's canonical markup. Nothing left the lesson — students still see both reveals. **book_gates v1.8 → v1.9** adds `§20.1 no finished answer hidden behind a hint reveal`, control-run three ways: unfixed source FAILED catching 1.11 and nothing else, fixed tree PASS, injected drift (L03 3.1 solution → hint) FAILED. **DJ RULING — BRAIN CHECK ANSWERS ARE NOT WHAT WE HIDE** (*“what we want to hide the answers to is the challenges”*): BC03 had drifted to `solution` in L05–L08 while BC01 held `quiz` in all eight converted lessons — one construct, 12 `quiz` to 4 `solution`. §20.1 already names `quiz` for “knowledge-check answers” and L09's live ancestor is already `quiz`, so all four were retyped and the sixteen Brain Check blocks are now uniform. Recorded against the type: stripping BC03 bought little anyway, since every BC03 item cites the section holding its answer and the tutor receives that prose — unlike a challenge solution, which is code the student must compose. **§24.6c APPLIED TO THE LEAK SURVEY ITSELF**: the first book-wide detector returned **73 candidates**, almost all false positives — it read every §6.12a Template panel as finished code in open prose because template blanks are not written with the markers it looked for. The shipped gate is therefore narrow (code inside a `hint`, ≥ 3 finished statement lines, no blanks) — the one shape verified by reading. **OPEN, NEEDS A RULING**: L02 `2.t4`'s `check` reveal holds the complete worked code for a TRY IT the card tells students to translate themselves; `check` is KEPT by §20.1 design, so it reaches the tutor today. Applied S79: L01 **v03.10.1**, L05 **v04.9.2**, L06 **v04.12.1**, L07 **v04.8.1**, L08 **v04.7.1**.) Prior: **v8.64** (v8.64, S78 moderate — **§25.10f AN ANCESTOR CLAIM IS A LEAD TOO, INCLUDING ONE WRITTEN INTO THIS BIBLE**: §25.10e closed by naming four unswept ancestors and three of the four were wrong — **L08 *Check Yourself* does not exist** (two lowercase prose hits, §1 and §6 Step 7, neither a heading), L11's block is titled *Skills Checklist*, and L15/L16 *Wrap-Up* is the §10 section banner rather than a construct; meanwhile **L09 carries two live ancestors nobody listed** (*Technical Skills: Can you…?* and *Knowledge Check*). The rule: a scoping claim inherited from a handoff or from this Bible is a lead exactly like a grep result, and the failure mode is a case-insensitive keyword hit reported as a block without anyone reading it — §24.6c extended from the grep to the sentence that outlives it. Applied: **L08 v04.6.2 → v04.7.0, the eighth conversion.** Its real ancestor was a three-item *Knowledge Check* under BC03's own name; BC01 Mental (5) authored at the §5/§6 seam, §-ordered §1 → §3.1 → §3.2 → §5.1 → §5.3; BC02 = §2's nine objectives migrated character-exact per §25.5, all nine achievability-checked and the `extern` red-build item already carrying its deliberate rep in §6 Step 4 (*"Went green first try? Earn the encounter anyway"*); BC03 = the three migrated items, verbatim, now citing §3 · §3.1+§5.1 · §7.3, plus three authored citing §6 Step 4 and §6 Step 8 twice; BC04 = 3 authored, no reveals. Per DJ ruling, **Record Your Calibration stays a separate §10 subsection**, outside the Brain Check family — matching L03 and L09, which keep their own calibration-data blocks. L08's `10.1/10.2/10.3` numbering dropped: it was the only lesson in the book using numbered §10 subsections. Five mysteries tagged `8.m1`–`8.m5` (§4.2). **§25.8's floor gate written at last** — book_gates v1.7 → v1.8 asserts BC03 ≥ 4 items in every converted lesson, control-run both directions.) Prior: **v8.63** (v8.63, S77 moderate — **§25.8 KNOWLEDGE CHECK IS A FLOOR, NOT A CEILING** per DJ ruling *"keep more than 5 and we can weed them out later"*: the flat cap of 5 had been dodged four times and L02 was already live at 7, so §25.2's *"scales with the lesson"* becomes operative and a conversion never cuts an item to meet a count. New **§25.10e — THE RETIRED-NAME LIST IS NOT THE ANCESTOR DETECTOR**: L07's §25.10b sweep returned zero across all five retired names while the lesson held TWO live ancestors (*Self-Assessment*, 6 items, and *Knowledge Check*, 7 items), so scope a conversion by READING §10 and asking what job each block does, never by grepping what it is called; the same shape is live and unswept in L08 *Check Yourself*, L11 *Skills Check*, L15/L16 *Wrap-Up*. Corollary per DJ ruling *"Don't retire them, put them somewhere for us to evaluate later"*: new root file **`ZUMO_PARKED_EXIT_ITEMS.md`** holds displaced-but-live items verbatim with provenance — the inverse of `ZUMO_SHELVED_CARDS.md`, never merge them — and an item that contradicts its own lesson (L07's *"Write include guards"* against §3.6's 📘 *The Old Way*) is not carried forward. Applied: L07 v04.7.2 → **v04.8.0**, the seventh conversion; BC02 = §2's nine objectives migrated per §25.5; BC03 = 6 with all six §-citations content-verified; BC04 = the practical question reshaped out of BC03 plus two authored; five mysteries tagged `7.m1`–`7.m5`.) Prior: **v8.62** (v8.62, S76 moderate — new **§25.10d**: a citation can point at a HOLE, not just at the wrong section — L06's Knowledge Check asked what to adjust when the robot drives 33 cm instead of 30, and `WHEEL_DIAMETER_MM` appeared in exactly two places in the file, §6 Step 5 and the question itself; the fix is to WRITE THE MISSING CONTENT, never to re-point the citation at the nearest plausible §. Root cause was a **within-lesson promise that does not land** — Step 8's checkpoint sends students to "Section 8 has the table" and §8's Quick Fix Table had no row for distance being off; the §24 promise gate is CROSS-lesson only, so nothing could see it. Also: **the Bible's own column fingerprint was the short slice** — 5,596 chars / `8fa00744` measures START through *before* the END comment, so verifying against it reproduces the exact one-byte-short defect §25.10c was written to prevent; canonical is now the full block, **5,639 chars / `070806a6`, ending in `-->`**. **§25.5 applied for the first time**: L06's BC02 is the six §2 objectives migrated character-exact, so the two lists agree by construction instead of joining the four-lesson reconciliation debt. Applied: L06 v04.11.2 → v04.12.0, the sixth conversion; L06's five bonus mysteries tagged `6.m1`–`6.m5` (§4.2); L05 v04.9.0 → v04.9.1 fixing a literal `{CODE}` placeholder that shipped live in S75.) Prior: **v8.61** (v8.61, S75 moderate — new **§25.10c**: when two ancestor blocks duplicate, diff them item by item — L05’s answerless `Conceptual Understanding` and its answered `Knowledge Check` held the same six facts, but ONE pair differed by cognitive level and had already done part of the §25.2 recall/apply split; a skill that fails §25.10 achievability is RELOCATED, never deleted (retire into prose that already says it, or reshape into the construct it actually is — and a reshape retitles its host); the column is copied START through the full 43-character END comment, and one byte short leaves an unterminated comment that swallows `</body>` — caught by the §24.6 parse gate, not by tag balance. Applied: L05 v04.8.2 → v04.9.0, the fifth conversion; L05’s five bonus mysteries also gained their missing `data-challenge` markers (§4.2), invisible to the Tutor picker until now.) Prior: **v8.60** (v8.60, S74 moderate — new **§25.10b SCOPE A CONVERSION BY THE RETIRED-NAME LIST**: the ancestor block is often present under a retired name, so grep §25.2's retired list before concluding a lesson has nothing to redistribute — L04 looked like an authoring job and was a redistribution job, its ten-item ancestor titled *Conceptual Understanding*; plus the grammar cost of the §25.10a checklist fold (tense and clause-order rewording expected, everything else character-exact). Applied: L04 v04.6.2 → v04.7.0, the fourth conversion.) Prior: **v8.59** (v8.59, S73 moderate — new **§25.10a**: the Brain Check family is FOUR and the shared column’s hardcoded-to-four script is the reason; an extra exit block folds into the BC it most resembles as a labelled group (L03’s *I can…* / *I have…* inside BC02, 12 `data-bc-skill` items); the skills unlock already generalises because `allSkills()` counts elements not a constant; column seats before `</body>`; and the subsection-slicing trap that makes a bad §-citation look verified.) Prior: **v8.58.1** (v8.58.1, S73 minor — §4.4 paperwork: the non-conformant table was written at S72 against work that had only been SPECIFIED. L01 was fixed S72; **L02’s renumber was cut S73** (v02.16.0 → v03.0.0). Attribution corrected; no rule changes. Recorded en route: BC01 item 3 cited §3.2 for the function prototype, which §3.2 never taught — a citation that was already wrong when it shipped S72 and would have been renumbered into a new wrong pointer. The §25.2 gate passes either way. **A §-citation is verified by checking the cited section CONTAINS the answer, never by checking one is present.**) Prior: **v8.57.1** (v8.57.1, S71 minor — §25.10 relocated AFTER §25.9 for numeric subsection order (it had been inserted before it); closing pointer added so §25.9 stays the section’s open-items ledger. No rule changes.) Prior: **v8.57** (v8.57, per S71 DJ ruling — **§25.10 GATED-ITEM ACHIEVABILITY**: a skill behind the BC02 lock must be earnable by every student who did the lesson; chance-dependent items get a deliberate rep. Applied: L01 v03.9.1→v03.9.2 gains the Break-It-On-Purpose upload-error rep (end of §6 Step 6) so item 10 no longer gates on luck. Review rule, not machine-gateable.) Prior: **v8.56** (v8.56, per S71 DJ ruling — **§25.10 SKILL GATE**: Brain Check 02\u2019s Mark-done button locks until all ten ☐ skills are tapped ☑; skills persist per-browser (`bc_LNN_sk`); tappable ☐ items are `data-bc-skill`-tagged; book_gates v1.6→v1.7 asserts box-glyph/tag parity in converted lessons, control-run with landed-injection assert. Applied: L01 v03.9.0→v03.9.1.) Prior: **v8.55** (v8.55, per S71 DJ rulings — **§25.10 BRAIN CHECK — NEW SUBSECTION + §8 TYPE 10**: the four §25.2 exit constructs get ONE family name (Brain Check 01–04), one livery (§8 Type 10 Knowledge: bg `#e8eaf6`, border `#3f51b5`, title `#283593` — indigo chosen by ΔE audit, min 32.3 vs every locked color), a fixed right-edge nav column with localStorage check-off (per-browser tracker, NOT a grade), and a two-state icon pair (gray incomplete / green-check complete; gray not red because §22 owns red for ERROR; state never color-alone — colorblind-safe via the check glyph; dark backings forbidden). Fixed en route: the Mental block in L01 had been NESTED INSIDE the §6 banner div since S70 — the banner rendered below the block and `color: white` inheritance made the five reveal ANSWERS white-on-white; un-nested, banner rebuilt canonical. book_gates v1.5→v1.6 extends §25.2 (anchors 01–04 + Type 10 wrapper + column presence), control-run FOUR ways with landed-injection asserts. Applied S71: L01 v03.8.1→v03.9.0. Icons at `images/BrainGear_Incomplete.png` + `images/BrainGear_Complete.png`.) Prior: **v8.54** (v8.54, per S70 DJ directive — **§25.6a THE TOOL PAGES ARE NOT CHAPTERS + LAYOUT IS GATED**, and **§5b WEB-TOOL VERSION LINE REWRITTEN**. DJ: "I don't want to have to deal with any more header and footer issues." The recurring defect was never markup — it was FILE LOCATION: `going_deeper.html` pushed into `lessons/`, then `tutor.html` pushed to root, both looking like clean pushes and neither catchable by a contents gate. book_gates **v1.4 → v1.5** adds `§12/§23 site layout` (asserts all 21 pages and their exact paths) and `§5b web tools carry an in-file version line`, control-run three ways. Fixed on this pass: `timer.html` and `tutor/tutor.html` had NO in-file version at all; `newproject.html`'s changelog opened with v2.18 against a live v2.45 (the v3.0 ghost); the Bible's own web-tool sentence claimed "Maker v1.3". Baselines set and labelled as baselines: timer v1.3.0 · Maker v2.45.1 · tutor v1.0.0 · index v1.3.0. index.html gained the site credits line. Prior: **v8.53** (v8.53, per S70 DJ rulings — **§25 THE EXIT-REGION CONSTRUCTS + §5b HIDDEN BUILD BANNER + HEADER/FOOTER CANON — NEW SECTION**: an audit of §10 found **six differently-named written-response blocks** doing overlapping jobs (STOP & PROCESS — Explain It in Writing · STOP & PROCESS — Answer From Your Head · Conceptual Understanding · Knowledge Check · Check Your Understanding · Reflection Questions), unevenly distributed, with **L13 and L15 carrying none at all** — the same §4.1 disease that produced three meanings for "Challenge". DJ ruled FOUR constructs, not three. **§25 canonizes them**, plus the reading-quiz design, the warm-up/spiral aiming rule, and the header/footer/hidden-banner canon that this session made uniform across all 17 pages. Applied S70: **L01 v03.7.0→v03.8.1** (the four blocks built — Mental 5 items before §6, Knowledge Check 4 items in §10, Reflection 3 prompts, plus 5 banked Canvas quiz variants); footer + hidden banner rolled to all 16 lessons and `going_deeper.html` **v01.0.0→v01.1.0**; DEEPER pill added to the §6.5a strip. Minor bumps: L02 v02.15.2 · L03 v03.13.2 · L04 v04.6.2 · L05 v04.8.2 · L06 v04.11.2 · L07 v04.7.2 · L08 v04.6.2 · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 · L13 v02.6.2 · L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2.) Prior: **v8.52** (v8.52, per S69 DJ ruling ("Love c") — **§6.5a THE LESSON STRIP — NEW SECTION**: every lesson's sticky nav gains a second thin row of sixteen numbered squares 01–16 (plus a LESSON label and a ⌂ home square to index), current lesson rendered as a solid white square. Chosen from four presented options (prev/next pills · dropdown · number strip · titled drawer); the strip won on one-click access to every lesson, permanently visible. Ships as ONE byte-identical block in all 16 files — static links that work without JS plus a self-hydrating script deriving the current lesson from the URL — bounded by LESSON STRIP marker comments, so a renumber or an L17 is a single block edit. Explicitly OUTSIDE the v8.21 nav-button ceiling (12–14), which governs the section-pill row only. Gate shipped same-session per §24.2: book_gates v1.2→v1.3 adds `§6.5a lesson strip present and byte-identical in all 16`, control-run per §24.6b in BOTH directions — against the pre-strip clone (FAILED, 16 missing) and against an injected one-character drift (FAILED, "differs"). Applied S69 second batch, moderate bump all 16 lessons with both banners moved per §5b: L01 v03.7.0 · L02 v02.15.0 · L03 v03.13.0 · L04 v04.6.0 · L05 v04.8.0 · L06 v04.11.0 · L07 v04.7.0 · L08 v04.6.0 · L09 v05.4.0 · L10 v02.5.0 · L11 v02.7.0 · L12 v01.7.0 · L13 v02.6.0 · L14 v02.8.0 · L15 v02.6.0 · L16 v02.5.0.) Prior: **v8.51** (v8.51, per S69 DJ ruling — **§24.6c AN AUDIT GREP IS AN UNGATED GATE — CONTROL-RUN IT TOO**: §24.6b binds gates, which are versioned and reused; an ad-hoc audit grep is a single-use gate that is neither, and both S69 false positives came through that hole. (1) Structure inferred from a proxy string — timer iframes read `label=Step+2`, so the audit concluded L02 timed its BUILD STEPS; the timers are on TRY IT cards and the label merely names the step the card belongs to, which produced "22 untimed build steps in L03/L04" and a proposal to insert 22 timers onto plain build prose, a device existing nowhere in the book — DJ's confirmation stopped it. (2) Case-sensitivity — `Step [0-9]+` matched only the mixed-case card headings while L02 writes `STEP N:`, finding 9 steps where there are ELEVEN and manufacturing a label "drift" that does not exist (all 11 labels correct; STEP 7 legitimately carries two TRY IT cards, `2.t7` Advanced/untimed + `2.t8` timed, so the duplicate "Step 7" is the truth). THE RULE: control-run the grep against an independently visible case before the number becomes a finding · never infer structure from label text, check what element the match is attached to · case-insensitive by default, since book vocabulary varies by lesson and era (`STEP`/`Step`, `CONFIGURATION`/`CONSTANTS`, "Coach's Tip" vs bare §6.6a labels) · report findings as VERIFIED or SUSPECTED, and a queue/handoff item enters the next session as SUSPECTED until re-checked — S69 also relayed the S68 queue's GRAPHIC 5.5 cone-angle suspicion as a defect when it was clean (bearings −90.0/0.0/+90.0, already matching the corrected 5.1). Extends §11 v8.36.2 from prose greps to STRUCTURAL ones and adds the reporting format; works against the standing pressure that a longer audit list reads as more valuable, against DJ's rule that a wrong finding costs 3× a blank one. Applied S69: L03 v03.11.1 + L04 v04.5.4 (timer gaps closed — L03 BC4 at 6 min, L04 C4/C5 at 4 min; all four card types now timed except main challenges, which are untimed in L02/L03 by convention and timed in L04 by DJ ruling) · L05 v04.7.1 (§4.1 Key insight had attributed proximity DIRECTION to which LED team fired, contradicting the §3.4 series-wiring fact two paragraphs above it — direction comes from which detector answers; §8A.1 emitter count and §4.2 vocabulary aligned; GRAPHIC 5.5 gained its missing caption).) Prior: **v8.50** (v8.50, per S68 DJ ruling — **§24.6 STRUCTURE IS VERIFIED BY PARSE, NOT BY COUNT**: a count-based tag gate can be satisfied BY the bug it should catch — eight lessons shipped with the Image Index panel close misplaced, six of them past `</html>`, and open/close counts balanced *because* the orphan balanced the unclosed panel, so `tag balance` returned PASS for the defect's entire life. Provenance git-verified: L01 from its first tracked commit (hand-authoring); L12–L16 all five from ONE commit, `94acc10` S35, the §6.5 flat-heading→boxed-section conversion, whose stateful close-the-previous-panel transform had no terminator for the last panel. **§24.6a A PARSER IS NECESSARY AND NOT SUFFICIENT** — L06/L07 parsed clean and were still wrong (footer sealed inside the box), so a semantic container assertion ships alongside. **§24.6b CONTROL-RUN EVERY NEW GATE AGAINST THE UNFIXED SOURCE.** book_gates v1.1→v1.2, two structural gates. Applied S68: L01 v03.6.5 · L03 v03.11.0 (new §8A.5 arrays + §8A.6 modulo closing the v8.41-logged C05 teaching gap; C05 grasp re-rated Deep→Moderate, doing axis and therefore the ramp untouched) · L06 v04.10.1 · L07 v04.6.2 · L08 v04.5.1 · L12 v01.6.2 · L13 v02.5.2 · L14 v02.7.2 · L15 v02.5.2 · L16 v02.4.1; Going Deeper pointers added to L07/L08/L12/L15/L16.) Prior: **v8.49** (v8.49, per S65 DJ ruling — **§24.5 THE DEPTH AUDIT + ROLLING HUMAN READ**: DJ's L02 diagnosis ("brief info, not a lot of depth") becomes standing process. book_gates.py v1.1 gains 3 gates (cross-lesson promises, arithmetic verification, §16 constants). New `DEPTH_AUDIT_S65.md` maps the findings. Verified structural find: **the teaching apparatus disappears at L11** — L11–L16 have ZERO LEARN boxes and near-zero KEY terms on the book's hardest material; mostly a marking fix, own arc. L14 profiles thinnest book-wide, goes first in DJ's read. §11 doubly applied: the scan's bitwise/pointer hits were 100%% false positives — a scan finding is a candidate until a human reads the section.) Prior: **v8.48** (v8.48, per S65 DJ directive "be more consistent and fix everything" — **§24 BOOK GATES — NEW SECTION + NEW TOOL `book_gates.py` v1.0**: every machine-checkable Bible rule runs against the whole book in one pass, at session open and before every delivery; a delivery that has not passed is incomplete (§12.6 class). Root cause canonized: the recurring S65 failure was fixing the INSTANCE instead of the CLASS — three times a named fix left the same defect alive elsewhere. §24.2: a rule canonized without its gate written in the same session only holds where someone happens to look. §24.3: gate the whole field, not the captured group (June/July survived a "passing" version check because the regex captured only the digits). §24.4: a computed claim is verified by computation, never recall (the 18-bytes-for-a-17-byte-string error). Also fixed on this pass: L01 What's-Next promised =/== as Lesson 2 content while L02 §3.2c deliberately defers it to L03 — question kept, phrasing fixed (cross-lesson instance of §11 "§8A must cover what §9 requires"). Applied: L01 v03.6.4, L02 v02.13.4.) Prior: **v8.47** (v8.47, per S65 — **§4.3 THE PICKER LABEL IS THE ELEMENT'S OWN TEXT**: the AI Tutor builds each dropdown option from the tagged element's `textContent`, so a construct must name itself. S65 tagged 11 L02 TRY IT boxes reading only "TRY IT (1 minute)" — six were identical in the dropdown. Correct tagging, unusable labels. Read the textContent out of context BEFORE tagging. `data-kind` now drives optgroups (Challenges / Warm-Ups / Try It / Mysteries); **no `data-kind` still means canonical challenge card**, so the 14 untouched lessons are unaffected, and unknown kinds fall to "Other" rather than being dropped. Applied: L02 v02.13.1, L04 v04.5.2, tutor/tutor.html.) Prior: **v8.46** (v8.46, per S65 DJ ruling — **§4.1 THREE CONSTRUCTS, THREE NAMES**: the word "Challenge" is reserved for the §6.12 card. Section 1 warm-ups become **Warm-Up N**, inline green practice boxes become **TRY IT (n minutes)**, Bonus Challenges keep their name. L02 had shipped with warm-ups 1–4 AND Bonus 1–6 both called "Challenge N", so "did you finish Challenge 3?" had three answers and the AI Tutor could only see the Bonus set. **§4.2 EVERY PRACTICE CONSTRUCT IS TAGGED** (extends §20.2): warm-ups and TRY IT boxes now carry `data-challenge` + `data-kind`; suffix `w`/`t` in the marker keeps them from ever colliding with a card number. Audited book-wide: gaps existed only in L02 (15) and L04 (1), both closed; 104 unique markers, zero duplicates. Applied S65: L02 v02.13.0, L04 v04.5.1.) Prior: **v8.45** (v8.45, per S65 DJ rulings — **§22 TERMINAL OUTPUT COLOR CANON — NEW SECTION**: simulated PlatformIO console output gets two locked colors — SUCCESS `#6a9955`, ERROR `#f14c4c` — so a student can answer "did it work?" before reading a word. `#6a9955` is DJ-ruled and is deliberately the same green as a `//` comment; the real terminal is brighter (~`#23d18b`) but L01 already used `#6a9955` and DJ ruled to keep ONE success green — do not "correct" it. **Color the diagnostic, not the block**: the source echo and caret stay plain `#e8e8e8`, because the echoed line is the student's own code and L02's "the compiler points at the line AFTER the mistake" rule depends on them judging it themselves — in the very case being taught, that line is innocent. **Detect terminal blocks by console markers** (`error:` with colon, `undefined reference`, `Writing |`, `[SUCCESS]`), never by the bare word "error": of 71 blocks containing "error", only **11** are console output — §11 false-positive discipline applied to color. Also canonized this session: **§6.13 the guard-clause brace rule** (K&R is house style, 837 vs 2; braces are the default; braceless only when the whole statement fits on the `if` line — the book has 93 such guards and they are correct, so "always brace" was NOT adopted) and **§23 GOING DEEPER** (standalone optional page at repo root, outside the 16-lesson numbering, not in the Maker registry; every entry must anchor to a chapter). Applied S65: L01 v03.6.2 · L02 v02.12.2 · L07 v04.5.1 · L12 v01.6.0 · L16 v02.4.0 · new `going_deeper.html` v01.0.0.) Prior: **v8.44** (v8.44, per S64 DJ rulings — **§6.12b THE SPLIT-PILL SWEEP IS COMPLETE**: all **84 challenges across 15 lessons** now carry the two-axis pill; `data-difficulty` + `data-grasp` are present and equal-count on every card, and **zero** old single pills remain (verified by `pill_sweep.py --audit`). L16 has no challenges (tier-cards, §6.12 variant) and is exempt. **§6.12c NEW — INLINE CSS DRIFTS PER REBUILD, MATCH STRUCTURALLY**: the same visual component carried **9 distinct style strings** across L04–L15 because Canvas strips `<style>` and `class=`, so every card holds its own copy and every rebuild retypes it; git shows the flips are single-commit and lesson-clustered (L05/L12/L13 all changed in `a3cd518`), i.e. STRATA, not rot. An exact-string replace is therefore invalid book-wide — match by STRUCTURE and scope the replace to one challenge block. **§11 A TRANSCRIBED-ONLY CONSTRUCT GETS A QUICK REFERENCE ROW, NOT A PROSE SECTION**: if a challenge template supplies a construct complete and the student only fills values, the comprehension load is nil and a §5 section is over-sized; give the "look it up" instruction a landing target instead (S64: `map()` → L08 `qr-map`, `do…while` → L09 `qr-dowhile`). A construct the student must COMPOSE still gets full prose. **§5b BOTH VISIBLE BANNER HOMES ARE MANDATORY**: header AND footer; L02 and L12 shipped with only the header and were repaired S64. Applied S64: L02 v02.10.2 · L04 v04.5.0 · L05 v04.5.0 · L06 v04.9.0 · L07 v04.5.0 · L08 v04.4.0 · L09 v05.3.0 · L10 v02.4.0 · L11 v02.5.0 · L12 v01.5.0 · L13 v02.5.0 · L14 v02.7.0 · L15 v02.5.0. New tool `pill_sweep.py` v1.0 at repo root.) Prior: **v8.43** (v8.43, per S63 DJ ruling — **§6.12b SLASH HALVED**: the split-pill divider goes `width: 8px; margin: 0 -4px` → `width: 4px; margin: 0 -2px`. The negative margin is structurally half the width — changing width alone opens a gap where the halves no longer close over the slash. Applied to all 25 live pills (L01 v03.6.1, L02 v02.10.1, L03 v03.10.1); markup was uniform, zero variants. Cosmetic-only, so hidden comment bumped and the visible banner left alone per §5b. DJ noted a possible further halving to 2px later — NOT applied.) Prior: **v8.42** (v8.42, per S63 DJ rulings — **§21 ROBOT ICON FAMILY REVISED — the family is LIVE**: 42 files pushed to `images/glowbots/` (commit `12867ea`), 25 bordered + 15 glow + 2 QA sheets. **§21.3 SUPERSEDES the S61 frame-swap-only rule** — the "NEVER separate the robot from its glow" prohibition is LIFTED; it was written from a failed attempt, and S63 cut all five successfully, including the two §21.4 predicted would defeat it. Two outputs, two methods: BORDERED (frame-swap) for buttons, GLOW (extract-and-cut) for images. Two findings make the cut work — (1) EDGE-CONNECTED FLOOD FILL, never a global brightness threshold, so interior dark pixels (Zircon PCB, Balboa frame gaps) survive by construction; (2) CUT THE FALLOFF, do not preserve it — the glow is painted additively on black so its falloff IS black, and keeping it as soft alpha renders a grey haze that is invisible on dark and filthy on white. **GLOW FLOOR 128 px**; buttons are always bordered. **QA RULE: CHECK ON WHITE** — every S63 glow defect was invisible on a dark background. **§21.2 colors** — canonical is the spec, as-built is recorded drift (generator approximation, not a design change); 3Pi+ is the Δ55 outlier. **§21.1 as-built inset deviation logged** — all five ship at 10–18 px against a 64 px spec; DJ ruled "leave them for now", so 64 stays the spec and the images are knowingly off it. §21.7 records the live file inventory + the uniformity spec (mean edge distance 1.28–1.32 px, p95 2.00, zero opaque edge pixels). No lesson versions changed.) Prior: **v8.41** (v8.41, per S62 DJ ruling — **§6.12b THE SPLIT DIFFICULTY PILL — NEW SECTION**: the difficulty pill becomes ONE badge cut by a 45° slash into two rated axes — DOING (five warm tiers, what the hands do) and GRASPING (three blues, what the head must hold). Supersedes the v8.27 single five-tier scale, which forced one label to lie whenever the axes diverged (L03 C08 writes comments only yet reasons about encoders three lessons early — ADVANCED warned students off it, EASY hid the hard part; Easy/Deep is the truth). Grasping is rated AGAINST THE LESSON PROSE, which makes the pill a live instrument for §11 "§8A must cover what §9 requires": a Deep rating on an untaught concept IS a logged teaching gap. New attribute `data-grasp`; `data-difficulty` retained for the doing axis. Applied S62: L01 v03.6.0, L02 v02.10.0, L03 v03.10.0 — 25 pills, five doing-axis re-rates, one teaching gap marked (L03 C05 needs arrays + modulo, neither in L03 prose). L04–L16 not yet swept.) Prior: **v8.40** (v8.40, per S61 DJ ruling — **§6.6 + §6.6a — TIP/NOTE/WARNING BY FUNCTION**: the Icon Guide gains 📘 **NOTE** (13 icons); three coach callouts are defined by function — 💡 Tip = actionable fix/how-to (green), 📘 Note = enrichment (slate `#eceff1`/`#607d8b`), ⚠️ Warning = real caution (amber). Labels are bare. The book had Tip/Note INVERTED (icon drove the label — enrichment wore 💡, fixes wore amber "Coach's Note"); being corrected book-wide S61 by reassigning every coach callout by function. L01 done (v03.5.0).) Prior: **v8.39** (v8.39, per S61 DJ ruling — **§21 ROBOT ICON FAMILY — NEW SECTION**: the matching robot "chooser" icons (one per fleet robot) as a single design family — shared frame (1254² rounded square, border inset 64 / radius 95 / stroke 14, near-black `#010808` panel, robot ~75–80% of panel), only the robot + accent glow color change. Records BOTH color sets per robot — CANONICAL (style-guide neon target) AND SAMPLED (measured from the first uploads, darker) — kept side by side, reconcile later. **Build method = FRAME-SWAP, not cut-and-rebuild**: keep the robot + its glow together and only replace the outer frame; NEVER separate the robot from its glow to regenerate it (fails on dark-bodied / open-frame robots — black-on-black defeats a brightness cut, and a regenerated glow loses the outer rim; this is why Zumo/3Pi+ went smoothly and Balboa/Zircon/Romi fought back). Staged for a future "pick your robot" page — not yet in the book.) Prior: **v8.38** (v8.38, per S59 DJ rulings — **§6.12a THE THREE-PANEL CARD + WHEN IT APPLIES (Project B canon) — NEW**: the §6.12 card skin is the mandatory SHELL on every challenge (outer box, gradient header with **sequential** `Challenge N` never §-based, five-tier pill, pale-yellow `#fffbe6` Work-in bar with 📁 Work-in + 🔍 Where-to-look, flush `data-reveal="solution"`); the INNER format fits the challenge type — **algorithmic** → three tiled panels 🎯 Goal `#f8f9fa` / 🧠 Logic-pseudocode `#f3e5f5` (absorbs the hint; NO separate hint box) / 🧩 Template `#e8f5e9` (blanks fill EXACTLY to the solution); **guided-edit/debug/observation** → prose, no panels (L01 is the reference, left as-is). No white body wrapper, no Plan-first. Open cases provisional pending DJ's runthrough: L08/L09 show Template + solution; YOUR-NUMBER two-level scaffold; solved-build vs starter link placement; solution code comments stay payload-matched on renumber. **§6.12 pill-sweep note corrected** — the sweep is COMPLETE (verified from files S59: 73 pills, all conforming, 0 EXPERT/COMPETITION). Applied S59: L05 v04.3.0 (pilot), L12 v01.3.0, L13 v02.3.0.) Prior: **v8.37** (v8.37, per S58 — **§20 AI TUTOR & MACHINE MARKERS — NEW SECTION**: the tutor reads live lessons with NO embedded curriculum (anti-rot); §20.1 `data-reveal` typing on every `<details>` (the tutor strips only `solution`, so any graded answer — including a debugging-mystery bug+fix reveal — must be typed `solution` or it leaks, and an open-prose or bare-`<pre>` solution is NOT stripped); §20.2 `data-challenge` marker on every challenge (the picker queries `[data-challenge]`; an untagged challenge vanishes; L16 tiers exempt); §20.3 both markers mandatory on new content; §20.4 favicon needs an explicit per-page `<link>` on a Pages project site. Also **§12.4 VERIFICATION DISCIPLINE — CACHES LIE** (shallow-clone lag, `git show --stat` on a shallow clone lists the whole tree as added, raw/API caches, upload-location trap) and §737/§935 accuracy fixes. Prior: **v8.36.2** (v8.36.2, per S58 — **§11 AUDIT FALSE-POSITIVE DISCIPLINE**: a prose-keyword grep reports candidates, not verdicts — separate code from prose before counting, treat a keyword near a heading as a lead, verify every finding against rendered text before acting. Canonized after S57's construct sweeps threw a run of prose-keyword false positives, each evaporating on a read. Prior: **v8.36.1** (v8.36.1, per S57 — **§11 §8A MUST COVER WHAT §9 REQUIRES**: a construct the challenges ask students to write must be taught in that lesson; using it in given code is not teaching it. Fix pattern = teach at first contact, demote the later tutorial to a §18.1 spiral second rung. Applied S57: L04 v04.1.0 gains §8A.6/§8A.7 for the `for` loop, L05 v04.2.0 §5.15 becomes the second rung and adds the descending loop its own challenges assumed. Prior: **v8.36** (v8.36, per S57 — **§16.9 EEPROM ADDRESS MAP — NEW**: the fleet shares one flat 1,024-byte EEPROM with no protection; 0–511 Lesson 16 `Saved`, 512–543 the robot name (magic `0x5A`, written by `ZUMO_NAME_WRITER_main.cpp`), 544–1023 free for enhancements. **§11 A "THE BOOK HAS NEVER…" CLAIM IS A DEPENDENCY** — grep the whole lessons tree before trusting a never/first-time sentence. Both canonized after S56's L01 §9 publication of the EEPROM name-reader silently falsified L16 §4.3's "this book has never touched it." Applied S57: L16 v02.2.3.) Prior: **v8.35** (v8.35, per S56 DJ rulings — **§11 IF IT IS IN THE PAYLOAD, IT GOES IN THE BOOK**: an unmatched payload-gate line is a GAP IN THE BOOK, not a gate defect; the fix is to add the content to the lesson, never to exempt the line, and EXECUTABLE CODE IS NEVER EXEMPT. Canonized after S55 burned four takes proposing to exempt L01's 900 failures as "comment-only scaffolding" when 132 were an EEPROM name-reader that appeared in NO lesson while C01 Part 5 asked students to use it. S56 fixed it the right way: the shared 88-line challenge body was published in L01 §9 and each of the eleven cards now quotes its OWN target line verbatim — EXECUTABLE CODE went 132 → 0 with zero exemptions. **§11 BOXED INSTRUCTION HEADERS ARE ADVISORY BUT FINGERPRINTED**: a challenge file's boxed header is the student's working instructions and stays IN the file (DJ ruling: students code in one window and read in another, and a step you remove is a step they will actually do), so a non-matching boxed line is a FORMAT difference reported under ADVISORY rather than a failure — BUT advisory never means unchecked: gate v1.6 pins every header with a line count + md5 in BOXED_FP, so an edited header fails loudly and intentional changes go through --update-fp. **§11 READ THE CENSUS, NOT THE RAW COUNT**. Applied S56: L01 v03.4.0, Maker v2.39, gate v1.4→v1.6.) Prior: **v8.34** (v8.34, per S55 DJ ruling — **§12.6 LIVE.md STALENESS IS A STRUCTURAL FAILURE — NEW**: S54 and S55 both pushed version bumps without regenerating LIVE.md, leaving it describing a state two sessions old; S55 then burned FOUR attempts re-diagnosing, three of them building on wrong version numbers. §12.3 already ruled that "remember to update LIVE.md" is too weak — §12.6 closes the window structurally: (A) write LIVE.md when the last version-changing edit lands, re-verify at close (§12.3's steps 1–5 unchanged); (B) a push that bumps a version and omits LIVE.md is an INCOMPLETE PUSH, a defect of the same class as a card disagreeing with its file; (C) session open runs a DRIFT CHECK — grep the files, compare to LIVE.md, THE FILES WIN, and on disagreement ask DJ for a newer LIVE.md before regenerating one. Do not enter queued work on a known-stale LIVE.md.) Prior: **v8.33.1** (v8.33.1, per S51 DJ ruling — **§18.3 SECTION-LIST RECONCILED**: line 859 declared "all five section headers" but named FOUR, in L03-era vocabulary (`CONFIGURATION`, `STATE VARIABLES`) that OMITTED `GLOBAL VARIABLES` — the exact section the ≥L4 `mainCpp()` scaffold was itself missing. Rewritten lesson-agnostic: the standard headers in canonical SET + ORDER, names varying by lesson (`CONSTANTS`/`CONFIGURATION`, `GLOBAL VARIABLES`/`STATE VARIABLES`), none dropped just because a step hasn't filled it. Paired with Maker v2.32→v2.33, which added the missing `GLOBAL VARIABLES` header to the ≥L4 blank starter — the L04 Step-2 landing zone.) Prior: **v8.33** (v8.33, per S49 — **§10 image-URL canon**: 114 `<img>` refs moved raw→Pages; EXIF-strip rule; §11 no-dark-prose checklist item. *This changelog entry was backfilled S51 — the S49 header bump left the list at v8.32.*) Prior: **v8.32** (v8.32, per S48 DJ rulings — **§19 PER-LESSON LEARNING-MODE FILE — NEW SECTION**: each lesson may carry a companion `ZUMO_LEARNMODE_LNN.md` in repo root recording the Socratic learner-mode walkthrough of its challenges (difficulty roll-up + per-challenge detail + Coach's Tips + queued finds); it is a teacher-side teaching record and a source for the AI Tutor rebuild, NOT student-facing and NOT a payload source. L03's is live (`ZUMO_LEARNMODE_L03.md`). **TERM: "CHALLENGE TEMPLATE"** — the full-section-header starter of §18.3 is named a **challenge template** project-wide (Bible + cards + Maker labels); "scaffold" is retired for this sense (it still means the TDP accumulation in §14 and the theory-first build in §5). Prior: **v8.31** (v8.31, per S45 DJ ruling — **§5b IN-FILE VERSION REWRITTEN — REVERSES the major-digit-only rule.** The full version now lives in TWO durable in-file homes so it can never again be trapped in LIVE.md alone: (1) the VISIBLE header/footer banner carries **major.minor** `vXX.XX` (e.g. `v03.2`) — it churns only on a moderate-or-larger bump, NOT on a minor/cosmetic one; (2) a HIDDEN HTML comment at the very top of the file carries the **FULL** `vXX.XX.XX` (e.g. `<!-- Lesson version: v03.2.5 -->`), greppable, invisible to students, updated on EVERY bump. The stable published filename `Lesson_NN.html` is UNCHANGED. Rationale: publishing as a stable filename + a major-digit-only banner left the exact minor version recorded ONLY in LIVE.md — when LIVE.md corrupted (S45), L11–L16's true minor was unrecoverable from the repo. Applied to L01–L10 in S45; L11–L16 get the new banner+comment when each is next opened and its version reconciled from the git-proven floor.) Prior: **v8.30** (v8.30, per S45 DJ ruling — **§18.4 TYPE-EXPLAINER CALLOUT — NEW** (a data type is introduced in a blue `#e3f2fd`/`#2196f3` info callout, one line per type: `type — description — example`; the SAME look is reused for each type's later deep dive so students recognize it on sight — L02 §3.2b introduces int/bool/float/long/char, long deep-dives L05, float L07, char named-only; forward-pointers must be grepped against the code, not guessed). **§18.3 + CHAT-DISPLAY RULE** — when showing a Maker starter in chat, prepend the wrapper header (`#include <Zumo32U4.h>` + MY PLAN) so the display matches the generated file; the raw payload body starts at HARDWARE OBJECTS and does not compile alone. Applied S45: L02 v02.2.1 (data-types callout + int/bool prose), L03 v03.4.1 (constrain two-jobs callout + USB-falsifies-battery callout).) Prior: **v8.29** (v8.29, per S44 DJ ruling — **§18.3 CHALLENGE-STARTER PRINCIPLES REWRITTEN**: a starter is now the FULL section-header template (all five headers + seeded CONFIG constants + present setup()/loop()) with only the taught concept left blank in a marked landing zone — REVERSES the S40 minimal-skeleton rule (students are used to the whole template; a skeleton reads as unfamiliar). Payload bodies START at HARDWARE OBJECTS; the Maker mainCpp() wrapper supplies the banner + #include + MY PLAN. A starter must not require a construct the book hasn't taught yet — L03 Ramp uses unrolled by-hand steps, not a for loop (not taught until L05). Applied S44: L03 constrain + ramp starters (Maker v2.30), L03 Ramp card prose + solution rewritten (v03.4.0).) Prior: **v8.28** (v8.28, per S43 DJ ruling — **§18.2 INLINE-STAR RENDERING LOCKED**: an inline spiral star is the actual `spiral_star_NN.svg` asset via `<img>` (absolute raw URL, `height:1.1em; vertical-align:middle`), NOT an emoji; emoji ⭐ appears only in the literal "🔁 Builds on:" header glyph. First appearance = L02 §9 "Builds on:" explainer, introducing the mark before L03's first marked card.) Prior: **v8.27** (v8.27, per S42 DJ rulings — the L03 challenge-redesign build: **§6.12 RATING SCALE recolored/relabeled to UP-TO-FIVE tiers** — EASY `#4caf50` · MEDIUM `#2196f3` · TOUGH `#9c27b0` · HARD `#ff9800` · ADVANCED `#f44336` (a lesson uses as many as it needs, in order; no minimum per tier). Replaces the old EASY/MEDIUM/HARD/EXPERT/COMPETITION set; **book-wide pill sweep of existing lessons is QUEUED, not yet applied** (~47 pills: MEDIUM orange→blue ×27, HARD red→orange ×15, EXPERT→TOUGH purple ×5). **§18.2 student-facing marker header renamed "🔁 Spiraled skills:" → "🔁 Builds on:"** ("spiral" stays the teacher-side method name; ⭐ numbered-star convention unchanged). Prior: **v8.26** (v8.26, per S40 DJ rulings — the S40 documentation pass, folding decisions that had lived only in session memory into durable canon: **§14.1 THE LOG *IS* THE TDP** — the 16 Engineer's Log prompts accumulate into ONE growing Google Doc structured as a RoboCupJunior TDP; notebook and TDP are the same artifact; template = `ZUMO_TDP_Template.md` (repo root, live); prompts stay in the lessons (one source of truth), the Doc holds only TDP scaffolding + PART A standing lists (A1–A5). **§18 CHALLENGE-DESIGN CANON — NEW SECTION**: (18.1) the **Saxon spiral** — each lesson's challenges reinforce 1–2 PRIOR concepts alongside the new one; roll out going forward lesson-by-lesson, do NOT retrofit L01/L02; one new concept per rung. (18.2) **marker convention** — blue "🔁 Spiraled skills:" header line naming the source in words + inline ⭐ numbered stars with the source lesson # inside; assets `spiral_star_01..16` in `images/` (vector-path numbers, gold gradient). (18.3) **starter principles** — minimal skeleton, includes + the ONE needed hardware object pre-placed, empty section headers ("// (none needed for this challenge)"), MY PLAN ships blank, marked "// write your code here" zone, don't re-explain setup()/loop(); challenge folder labels may take a C## prefix (output-string only, keep kind= ids, flat). Prior: **v8.25** (v8.25, per S39 DJ ruling: **§16 HARDWARE GROUND TRUTH — NEW SECTION** and **§17 SVG / GRAPHIC CANON — NEW SECTION** — capture into the Bible the hardware and SVG canon that previously lived only in session memory, so a memory failure has a durable backup. §16: gear-ratio sticker colors (Green 50:1 / Blue 75:1 / Red 100:1; fleet = blue 75:1, verified vs Pololu 0J63 §1.1), TRIM = LEFT motor, setSpeeds() ±400 hard-cap and what constrain() actually protects, brake-style stop, stall current (one event two symptoms), encoder averaging, shared pins 20/4, 28,672/2,560 B ceiling. §17: 1100×850 canvas, blue title band, single-polygon arrows, section colors, IMAGE/GRAPHIC separate number spaces, and the textLength stretch trap (only over-stretch is a defect; ~30 SVGs use it — per-file audit deferred, do not blind-replace). Prior: **v8.24** (v8.24, per S36 DJ ruling: **§12 DOCUMENT WORKFLOW REWRITTEN** — the old text was stale (it said to UPLOAD the Bible at session open, and named a handoff file that does not exist). **EVERYTHING LIVES IN THE REPO** — Bible, LIVE.md, handoffs, gate scripts, harness, web tools, lessons, images. Session open = CLONE, not upload. Session close = **ONE ZIP, FULL REPO LAYOUT, EVERY CHANGED FILE INCLUDING ROOT DOCS** — one extract, one commit, one push. A zip cannot DELETE: removals ship as explicit `git rm` lines in the close note. Prior: **v8.23** (v8.23, per S36 DJ ruling: **§5b THE TOOLCHAIN IS PINNED** — `lib_deps` names an EXACT library version (`pololu/Zumo32U4@2.0.1`), never a bare package and never a caret range. This book publishes byte counts against a 28,672 B ceiling with as little as 638 B of headroom; an unpinned dependency is a live hazard, not a style preference. Prior: **v8.22** (v8.22, per S36 DJ rulings: **§15 MAKER REGISTRY & LINK CANON — NEW SECTION** — the §7 ladder is FIVE RUNGS, 7A–7E, and the Maker's kind letters MUST match the lesson's rung letters; `finished` IS the last step, so step_* kinds cover 1..N−1 only; a kind MAY share another kind's payloadRef; the four Maker-link shapes are canon; and the Maker is NOT uniformly formatted — edit by offset, never by line. Prior: **v8.21** (v8.21, per S35 DJ rulings: **§6.5 NAV BUTTON COUNT is 12–14** and **the Image Index has NO nav button** — the pill was removed book-wide; **§6.8 FOUR PART BANNERS, FIVE COLOR GROUPS is REAFFIRMED** — the gray §10+end group carries the group color but NO divider; the "PART 5 — Wrap Up" banner that L10–L16 had invented is retired book-wide. Prior: **v8.20** (v8.20, per S33 DJ rulings: **§9 UNIQUE VERSION PER DELIVERY** (retires the fix-to-a-fixed-version rule) · **§9 image changes are a MINOR bump** · **§10 IMAGE and GRAPHIC are SEPARATE NUMBER SPACES; audit art against `images/`, never against the lesson alone** · **§13 BATTERY CANON — eneloop NiMH** · **§14 ENGINEER'S LOG — 16 prompts, one per lesson**. Prior: **v8.19** (v8.19, per S28+S32 DJ rulings: **16-LESSON RENUMBER SWEEP** — §1 filename table, §3 LESSON MAP, §0 items 5/6 8A map, tier-card example, and image-phase count moved from the 15-lesson to the 16-lesson numbering (L12 "Wheels Lie" inserted S28, shifting Rescue Zone→13, Competition Prep→14, Advanced PID→15, Showcase→16; L11 retitled "Time Lies, Distance Doesn't"; L15 retitled "The Present Isn't Enough" S31; L16 retitled "Nothing Left to Take Away" S32). 8A map re-verified against published files July 13, 2026: PRESENT L02–L15, ABSENT L01 and L16. Renumber only — no rule changes. Prior: v8.18 (v8.18 adds, per S28 DJ ruling: **§11 EXTRACT THE INHERITANCE — DO NOT RECONSTRUCT IT.** A depth pass on lesson N BEGINS by pulling lesson N-1's `finished` payload out of `newproject.html` (`PAYLOADS["N-1"]["finished"]`) — that is the project students actually hold in their hands. Rebuilding the base from lesson HTML, from a sibling lesson, or from memory SILENTLY DROPS FILES. Canonized after S28 reconstructed the L11 base as SIX files, omitting `RobotHelpers.h`/`RobotHelpers.cpp` — the STANDARD HELPERS (`waitForStart()`, `checkBattery()`) that have shipped in EVERY project since Lesson 4 — and built 21 compile-verified states on that broken inheritance before catching it. A student would have opened the lesson project and found their SAFETY GATE GONE. The project is EIGHT files: RobotConfig.h, RobotSensors.h, RobotSensors.cpp, RobotHelpers.h, RobotHelpers.cpp, RobotMotion.h, RobotMotion.cpp, main.cpp. GATE CHECK: assert `len(files)==8` on every state. The 21 states were discarded and rebuilt from the real payload; the corrected base compiles at 22802 bytes, byte-exact to S27's recorded L11 `finished` — which is how provenance was confirmed. THE MAKER REGISTRY IS THE AUTHORITATIVE INHERITANCE SOURCE. Prior: v8.17 (v8.17 adds, per S25 DJ rulings: **§11 A DECLARED STUDENT BLANK MUST BE SPENT** — if a lesson ships a tunable as a blank (`const int TRIM = 0;   // <-- YOUR NUMBER`), the code MUST actually USE that constant. A blank the code never reads is a LIE in the worksheet: the student writes in a number, nothing changes, and they lose faith in the instrument rather than in their own guess. Canonized after S25 found §7B/7C/7D of L10 declaring `TRIM` and never passing it to `setSpeeds()` — the same defect class as L09's false claim that `turnDegrees()` "respects TRIM." GATE CHECK: grep every lesson for declared-but-unread tunables. **BLANK CONVENTION (DJ-ruled S25):** tunables ship as `= 0` with the starting guess in the COMMENT (`const int TURN_MS = 0;   // <-- YOUR NUMBER. Try 400 and work from there.`) — a seeded value looks like an answer and students accept it without hunting; a bare `0` with no hint means the robot does not move and the student has no bracket to start from. **§11 IDENTICAL BYTE SIZES — THE CONSTANT EXCEPTION** — the S22 rule ("identical binary sizes across states = `--gc-sections` discarding dead code") applies to added LOGIC, NOT to changed CONSTANTS. `speed + TRIM` with `TRIM = 0` constant-folds to `speed` and emits byte-identical code; the fix IS live, it simply costs nothing until the blank is filled. Do NOT conclude an edit vanished from a zero byte delta — DISASSEMBLE (`avr-objdump -d`) and read the immediates. S25 proved TRIM live in L10 §7D this way: `ldi r24, 0x96` (150) became `ldi r24, 0x9E` (158) with the right motor unchanged at 150 — same instruction, same size, correct LEFT-motor polarity. Sabotaged-build states that flip a sign or change a constant are the same case. **§11 SABOTAGED BUILDS SHOW THE PLANTED LINE** — Bonus mysteries display the sabotaged code inside the hint ("The planted constant:" / "as planted:"). The mystery is NOT "find the typo" — it is "why does THIS line produce THAT symptom," which is the actual debugging skill. This also satisfies the payload byte-match gate by construction (L09 canon, formalized S25). Prior: v8.16 (v8.16 added, per S23 DJ rulings: **§4 QUICK LINKS RETIRED** — book-wide; navigation canon = section banners + one `↑ Back to top` per section; a Quick Links jump-list duplicates the banners and rots on every renumber (only 4/15 lessons had one; L08/L09 — the freshest depth passes — never did). **§11 TRIM PLACEMENT RULE** — TRIM belongs in every OPEN-LOOP straight line (`driveDistance()`, `handleGap()`, timed maneuvers) and NOWHERE else: NOT in `turnDegrees()` (the wheels oppose on purpose; encoders govern the angle) and NOT in `followLine()` (P-control is a CLOSED loop already correcting bias 50x/sec — TRIM would fight it). Open-loop needs TRIM; closed-loop does not. Polarity is LEFT-motor: `setSpeeds(speed + TRIM, speed)`, positive TRIM speeds the left wheel, robot pushes RIGHT, correcting a LEFT curve — verified against Pololu `FaceTowardsOpponent.ino` (`turnRight()` = `setSpeeds(+turnSpeed, -turnSpeed)`; a robot curves toward its SLOWER track). **§11 ENCODER AVERAGING RULE** — distance/turn loops MUST gate on the average of BOTH encoders, never one: `while (averageCounts() < target)`. Watching a single encoder means a slipping or stiff wheel on the other side ends the move early or late and nothing warns you. **§5b IN-FILE VERSION = MAJOR DIGIT ONLY** — the header/footer "Version N" carries the major digit; the full `v##.#.#` lives ONLY in the filename (canonized after finding L04 shipped with header "Version 3" against footer+filename "4"). Prior: v8.15 (v8.15 added, per S22 DJ ruling: §11 payload-gate INHERITANCE RULE — lesson N's payload corpus additionally includes lesson N−1's `finished` payload bodies, because inheriting lessons copy the prior project wholesale in Step 1. Prior: v8.14.1 (v8.14.1 added, per S21 DJ ruling: §11 dark-wrapper scope check — canonized after the S21 L03 find where a `#1e1e1e` wrapper missing its closer swallowed four Quick Reference tables and passed both div-balance AND the depth walk, because the closer existed ~200 lines late. Prior: v8.14 (v8.14 adds, per S20 DJ rulings: §11 payload byte-match gate — canonized from the S18-approved Maker starter-code-registry rule; §11 bounded-scope replace assert — canonized after the S20 L03 B1/B2 regex incident; §4 "Bonus" vocabulary canon — book-wide term for the extra-practice section, nav labels must match. Prior: v8.13.1 (v8.13 adds: hardware-direction verification against Pololu examples; L04+ STANDARD HELPERS — waitForStart safety gate + A&B battery check; lesson-aware Maker skeleton; web-tool internal versioning. v8.13.1 completes the v8.13 delta: §11 ASCII-sweep checklist item — EDIT 5, dropped in the initial application — plus §5b header tag corrected v8.12→v8.13)))))))))))))))). **§12.2 (S84): the deletion PROCEDURE now lives in `PUSH_WORKFLOW.md`, not in the session handoff** — it had been documented only inside the very file being deleted, so it vanished at the moment it was needed and was re-authored from memory each session, and was missed twice (`fb70426`, and again at S84, where all 21 overwrites landed and only the deletion stayed behind). **A procedure stored inside the artefact it operates on is not stored.** `book_gates.py` **gate 28** asserts the repo root carries exactly ONE `ZUMO_SNN_HANDOFF.md`, excluding §19 learner-mode records, so a missed deletion fails a gate instead of waiting to be noticed.

---

## ASCII ART POLICY (v8.6 — canon)

**No ASCII-art diagrams anywhere in lesson content.** All diagrams are either Claude-produced SVG (`[GRAPHIC x.y]`) or DJ-sourced raster (`[IMAGE x.y]`).

- Applies to box-drawing/arrow diagrams in `<pre><code>` blocks AND to annotated code-anatomy diagrams (pointer/arrow lines inside code blocks) — those count as ASCII art.
- Replacement mechanism: swap the ASCII block for a `[GRAPHIC x.y] caption` placeholder in the lesson's own dashed-div placeholder format; DJ inserts the SVG file in Canvas.
- Existing ASCII art is converted per the ASCII→SVG tracker in `LIVE_ZUMO_TEXTBOOK.md`.
- Plain code (no drawing characters) in `<pre>` blocks is unaffected.

**MANDATORY DIFF-AUDIT GATE (v8.7).** Before saving any modified lesson file: run a full old-vs-new diff and confirm every changed line is explained by the intended edit — removed lines, added lines, and byte/line-count deltas must all reconcile. Structural checks (anchors, div depth) cannot detect content loss when the deleted content has no inbound links; only a diff can. Rebuild from the md5-verified `/mnt/project/` source, never from a prior working copy. (Canonized after a Session-8 regex overmatch silently deleted ~13KB from L02.)


**The single, definitive source of truth for the Zumo 32U4 Robotics Textbook.**

**Supersedes:** `Zumo_Super_Bible_V7.md` AND `Zumo_Textbook_Standards.md` (both retired). If anything in an older file disagrees with this document, this document wins.

**Last updated:** July 25, 2026 — **v8.58** (Session 72: §4.4 SKELETON CONFORMANCE — the Core 10 are mandatory; a thin section still appears and says so; lesson-unique material folds rather than becoming a new numbered section; "does not apply" stubs everywhere REJECTED on the skip-the-header cost; §8A re-ruled CONDITIONAL, unchanged. L01 and L02 brought into conformance.)

**SVG build-path rule (added v8.11, from the L02 GRAPHIC 2.9 incident):** SVG files must be authored through an escape-processing write path (e.g., Python string → file), NEVER a raw-text path — raw-written `\uXXXX` sequences render as literal garbage text in the diagram. Mandatory SVG QA before presenting: (1) literal-`\u` scan of the saved file must be clean; (2) render the SVG and verify, and when visual preview is unavailable, verify layout numerically (e.g., pixel-scan for overlap in gaps). Corollary for hosted HTML tools (timer, Project Maker): `\uXXXX` escapes are legal ONLY inside JavaScript string literals — the HTML text region must be escape-free (use entities or literal characters).

---

## 0. WHAT CHANGED IN v8 (READ FIRST)

v8 is a **re-baseline**. The previous Bible (v7) and the separate Standards doc had drifted from the actual lessons and from each other (they disagreed on section count and skin). v8 resolves that. The decisions below are LOCKED:

1. **Canonical skin = the "Lesson 9 look" + section CAP+BOX design** (Segoe UI, blue gradient nav/title; every section is a colored cap on a matching bordered box). Defined fully in §6. Supersedes the old v7 serif/flat-nav style guide.
2. **Nav/title gradients are top-down, dark-first** (`linear-gradient(to bottom, <dark> 0%, <light> 100%)`). **PART dividers are now SOLID group colors** (blue/green/rose), not the old navy gradient (retired). **Section cap+boxes and PART banners follow the nav color scheme:** §1–3 blue `#3498db`, §4–6 green `#3a7d5c`, §7/§8/§8A dusty rose `#c45d76`, **§9 plum `#9b6a9e`**, §10+end gray `#6c757d`. (§9 split into its own PART 4 — see §6.8.) **Code blocks are dark** (VS Code/PlatformIO theme, §6.11).
3. **Icon legend = 12 icons** (the set in §6.6), using "⚠️ WARNING."
4. **No icon before the title-block heading** (`LESSON ##`, not `🚧 LESSON ##`). Section headers (`📖 Section 1: …`) keep their icons.
5. **Structure = 10 sections, §8A CONDITIONAL.** 8A is present ONLY when a lesson isolates a genuine reusable coding pattern — it is NOT universal. (See §4.) **8A MAP:** PRESENT in L2–L15. ABSENT in L1 and L16. (Re-verified against every published file July 13, 2026.)
6. **Lessons with no 8A:** L1 (install/setup) and L16 (capstone/showcase). Their PART 3 subtitle = "Sections 7–8: Verify and extend" (no 8A). §9 is still its own PART 4 (plum) in every lesson. A "Functions Reference" subsection can go EITHER way — become §8A OR fold into Quick Reference — author's per-lesson call.
7. **Two spec files → one.** `Zumo_Textbook_Standards.md` is retired; its content is folded here.
8. **Filename convention:** `Lesson_##_Topic_v##.html` — zero-padded lesson number, zero-padded lowercase version. See §1.
9. **Re-baseline version reset (COMPLETE):** at the v8 transition, every lesson reset to `v01` — this one-time reset is now DONE (all 15 lessons built to v8.4, L10–L15 at v01, dates normalized to June 2026). The normal increment-only rule (§9) now applies to ALL lessons. **DO NOT reset any lesson's version or re-normalize dates again — only increment forward.**

---

## 1. FILE NAMING CONVENTION

**Pattern:** `Lesson_##_Topic_v##.html`

- `##` = zero-padded lesson number (`01`, `02`, … `15`)
- `Topic` = fixed topic token (underscores, mixed case) — see table below
- `v##` = zero-padded, **lowercase** `v` + zero-padded version (`v01`, `v02`, …)

**Examples:** `Lesson_01_Hello_Robot_v01.html`, `Lesson_10_Obstacles_v01.html`, `Lesson_16_Nothing_Left_to_Take_Away_v02.html`

**Locked topic tokens (all 15):**

| # | Topic token |
|---|---|
| 01 | `Hello_Robot` |
| 02 | `Read_Code` |
| 03 | `Motors_TRIM` |
| 04 | `Line_Sensors` |
| 05 | `Proximity_Sensors` |
| 06 | `Encoders` |
| 07 | `Code_Organization` |
| 08 | `Line_Following` |
| 09 | `Intersections` |
| 10 | `Obstacles` |
| 11 | `Time_Lies_Distance_Doesnt` |
| 12 | `Wheels_Lie` |
| 13 | `Rescue_Zone` |
| 14 | `Competition_Prep` |
| 15 | `The_Present_Isnt_Enough` |
| 16 | `Nothing_Left_to_Take_Away` |

The old `_Rebuilt_` / `_Canvas` / `_StandardCallouts_StickyNav` suffixes are **retired**. All files move to the clean pattern above at the v8 re-baseline.

---

## 2. CURRICULUM PHILOSOPHY (unchanged from v7)

- **Depth before breadth.** Each concept fully developed before moving on.
- **Coach voice.** Friendly, professional, "B-level" explanations. No flattery.
- **Theory-first, then scaffolded build.** Theory section is pre-reading; Build It is hands-on.
- **Progressive autonomy.** Each lesson copies the previous project folder and adds one capability.
- **Audience:** high school freshmen, zero coding experience. Platform: PlatformIO + VS Code (not Arduino IDE).
- **Information density:** "more is better" — comprehensive over simplified.

---

## 3. LESSON MAP

| # | Topic | 8A? |
|---|---|---|
| 01 | Hello Robot | ❌ none (intro/setup) |
| 02 | Read Code Like a Pro | ✅ yes (Functions) |
| 03 | Motors & TRIM | ✅ yes (Calibration) |
| 04 | Line Sensors | ✅ yes (Sensor Arrays) |
| 05 | Proximity Sensors | ✅ yes (Sensor Pairs) |
| 06 | Encoders | ✅ yes |
| 07 | Code Organization | ✅ yes |
| 08 | Line Following (P-Control) | ✅ yes |
| 09 | Intersections & Dead Ends | ✅ yes |
| 10 | Obstacles | ✅ yes (Sub-States) |
| 11 | Time Lies, Distance Doesn't | ✅ yes (Dead Reckoning) |
| 12 | Wheels Lie | ✅ yes |
| 13 | Rescue Zone: Flying on Instruments | ✅ yes |
| 14 | Competition Prep | ✅ yes |
| 15 | The Present Isn't Enough (PID) | ✅ yes (Concepts) |
| 16 | Nothing Left to Take Away (capstone) | ❌ none (capstone; §9 = tier-cards) |

---

## 4. LESSON STRUCTURE — LOCKED

**Vocabulary canon — SUPERSEDED S85, see §4.5.** The v8.14 (DJ-ruled S20) rule named the extra-practice section **"Bonus"** book-wide and rejected "Enrichment" and "Extra Practice" as alternates. It solved a real problem — one section, one name, so a nav label cannot lie about where it points — but it treated the block as ONE construct. **§4.5 (v8.72, DJ-ruled S85) replaces it: the block is THREE families with three names, each bound to a distinct method.** The three words are not alternates for one section; they are three different sections. The anchor id `bonus-challenges` is UNCHANGED in all sixteen lessons and remains the shared seat for all three families.

### Core 10 sections (every lesson)

1. **Intro** — engaging problem/scenario that motivates the lesson
2. **Objectives** — learning objectives checklist
3. **Theory** — background concepts, subsections 3.1, 3.2, … (lesson-specific design concepts live here)
4. **Hardware** — physical setup, sensor specs, calibration notes
5. **Code** — walkthrough of key functions/concepts (project org, constants/functions tables, function reference)
6. **Build It** — step-by-step implementation with checkpoints
7. **Test** — verification checklists, tuning guide
8. **Troubleshoot** — problem/cause/solution
9. **Challenges** — Easy/Medium/Hard escalation with collapsible solutions
10. **Exit Ticket** — 3-h4 structure (see §7)

**All ten are MANDATORY in every lesson — see §4.4.** A section whose job comes up thin this lesson still appears and says so (§4 Hardware in a lesson that adds no parts). Lesson-unique material folds into the nearest section rather than becoming a new numbered one. §8A is the one CONDITIONAL section (below).

**End matter (after section 10):** Glossary → Quick Reference → Image Index. Headings use the locked icon set: **📖 Glossary**, **⚡ Quick Reference**, **🖼️ Image Index** (border `#6c757d`).

**Glossary entry format (LOCKED):** each glossary term is a **term card** — `<div style="background-color: #e7d4ff; border-left: 4px solid #9b59b6; padding: 15px; margin: 15px 0; border-radius: 8px;">` then `<span>🔑</span> <strong id="term-...">Term</strong> — definition.` This is the ONE canonical glossary palette/format. Do NOT use Key-Term-callout purples (`#f3e5f5`/`#9c27b0`) or any other purple (`#f3e8f9`/`#7b2d8e` etc.) for glossary entries — those drifted across L1/L2 and were normalized. Term cards stay `8px` (the radius exception); inline Key Term *callouts* in the body remain `#f3e5f5`/4px and are a different element.

### Section 8A (CONDITIONAL — only when a reusable coding pattern exists)

8A houses a **reusable coding pattern** — something a student will reuse in later lessons (function parameters, return values, error handling, state machines, non-blocking timing, etc.). It is distinct from Theory: Theory holds lesson-specific *design* concepts; 8A holds transferable *code* patterns.

**Rules when 8A is present (L2–L15):**
- Placed **between Section 8 (Troubleshoot) and Section 9 (Challenges)** in DOM order.
- Appears in nav as a button ("8A. Concepts" or similar), dusty rose color `#c45d76`.
- 8A is part of **PART 3** (dusty rose, with §7/§8). PART 3 subtitle = "Sections 7–8A: Verify and extend". (§9 is now its own PART 4 in plum — see §6.8.)
- `<h2 id="section-8a">` carries the dusty rose color `#c45d76` (8A stays rose; only §9 moved to plum).
- Section ID order: `1, 2, 3, 4, 5, 6, 7, 8, 8a, 9, 10, glossary, quick-ref, figures`.
  *(v8.97, S108: `image-index` → `figures`, and the visible title "Image Index" → "Figures".
  Applied to all 16. Does NOT touch `[IMAGE 3.9]` / `[GRAPHIC 3.9]` captions, filenames,
  `IMAGE_WORKLIST.md` or the two number spaces — the IMAGE+GRAPHIC merge stays parked.)*

**Presence rule (CONDITIONAL):** 8A is present ONLY when a lesson isolates a genuine reusable coding pattern — NOT in every lesson. **8A MAP:** PRESENT in L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12; ABSENT in L1, L13, L14, L15. (L2–L5 verified present July 2, 2026.) Lessons without 8A use PART 3 subtitle "Sections 7–8: Verify and extend". §9 Challenges (PART 4, plum) is present in every lesson including those without 8A. A "Functions Reference" may become §8A (L12) OR fold into Quick Reference (L14) — author's per-lesson call.

### Theory (§3) vs Build It (§6) — the "Build It" approach

Explanation is immediately followed by implementation (not separated into distant sections). This is intentional, not a deviation.

---


### 4.1 THREE CONSTRUCTS, THREE NAMES — "CHALLENGE" MEANS ONE THING (v8.46 — NEW, S65)

The book contains three different graded-or-practice constructs. **Only one of them is called a Challenge.**

| Construct | Name | Look | Numbering |
|---|---|---|---|
| §6.12 challenge card | **Challenge N: Title** | canonical shell, split pill, `data-reveal="solution"` | `N.n` |
| Section 1 warm-up | **Warm-Up N: Title** | plain `<h3>`, blue `#2e86ab`, timer | `N.wn` |
| Inline practice box | **TRY IT (n minutes)** | green `#e8f3ec` box, inside a build step | `N.tn` |
| End-of-lesson extra | **Bonus Challenge N: Title** | purple gradient card | shares card numbering — see below |

**Why this rule exists.** L02 shipped with warm-ups numbered 1–4 *and* Bonus Challenges numbered 1–6, both
called "Challenge N". "Did you finish Challenge 3?" had three defensible answers, and the AI Tutor — which
queries `[data-challenge]` — could only see the Bonus set, so a student asking about a warm-up got the wrong
card. Renamed S65.

**"Bonus Challenge" keeps its number even where it duplicates a card number** (L02 and L03 both run cards 1–6
and Bonus 1–6). The qualifier disambiguates, this is the established convention in both lessons that have
Bonuses, and §4's "Bonus" vocabulary canon already reserves the word. Do not renumber them.

**The marker suffix carries the type.** `w` = warm-up, `t` = TRY IT, bare digit = canonical card. A warm-up
and a card can therefore never collide in the picker even when they share a display number.

### 4.2 EVERY PRACTICE CONSTRUCT IS TAGGED (v8.46 — S65, extends §20.2)

§20.2 requires `data-challenge` on every challenge. **S65 extends it to warm-ups and TRY IT boxes**, and adds
`data-kind` (`warmup` / `tryit`) so the tutor can tell them apart from a graded card. An untagged practice
construct is invisible to the picker — the student can see it on the page and the tutor cannot.

Audited book-wide S65: only **L02 (15 untagged)** and **L04 (1)** had gaps; both closed. L11 carries 4 markers
above its pill count — those are bonus-block constructs and are correct. **171 unique markers
book-wide, zero duplicates** (S86: +26, the last untagged bonus cards).

**S86 — COVERAGE IS GATED AT LAST.** §20.2 had only ever been asserted for UNIQUENESS, never for PRESENCE, and
that is the whole reason **28 untagged bonus cards sat inside a 30/30 book**: an untagged card is invisible to
the census, to the picker and to the gate that should have caught it, so nothing counted what was missing.
`book_gates` **gate 31** now rides gate 30's already-proven banner count — the banner's count word is true, so
the tagged count must equal it — and additionally asserts every card's `data-kind` names its own family.


### 4.3 THE PICKER LABEL IS THE ELEMENT'S OWN TEXT (v8.47 — S65, learned the hard way)

`tutor.html` builds each dropdown option from the tagged element's `textContent`, truncated to 60 chars.
**So the tagged element must name itself.** S65 tagged eleven L02 TRY IT boxes whose text was only
`🎯 TRY IT (1 minute)` — six were byte-identical in the dropdown and a student had no way to pick the right
one. The tagging was correct and the labels made it unusable.

**Rule: before tagging a construct, read what its `textContent` will say on its own, out of context.** If two
tagged elements in one lesson can produce the same string, the label is wrong. Give it a scope — the step it
belongs to, or the task it names: `🎯 TRY IT — Step 5: Longer Blink (1 minute)`.

**`data-kind` drives the optgroup.** The picker groups Challenges / Warm-Ups / Try It / Extra Practice /
Observation / Sabotage — the last three added S86 so the three §4.5 families are three groups, not one.
**S86 defect closed en route:** `known[]` had never listed `bonus`, so every L02/L03 bonus card rendered
BOTH in its own group and again in "Other" — 12 cards, doubled, live in the picker. Proven by executing the
grouping logic, not by reading it. Any kind added to §4.5 must be added to `known[]` in the same edit. A unit with
**no** `data-kind` is treated as a canonical challenge card — that is the book's default and the majority
case, and it must stay that way so the 14 untouched lessons keep working. Any unrecognized kind falls into an
"Other" group rather than being dropped; nothing tagged is ever invisible.

### 4.4 THE SKELETON IS MANDATORY — A THIN SECTION STILL APPEARS (v8.58 — NEW, S72, DJ-ruled)

The Core 10 list above is not a menu. **Every lesson carries §1–§10, in order, with each number
keeping the job the list gives it.** This was always the intent; it was never enforced, and two
lessons drifted off it unnoticed for the life of the book.

**RULE 1 — a skeleton section whose job comes up thin STILL APPEARS, and says so.** §4 Hardware is
the live case: a lesson that introduces no new parts does not delete §4, it opens §4 by saying so
and recapping the parts today's code will touch. The *job* of §4 — orient the student to the
hardware in play — fires in every lesson, including the ones that add nothing. A thin section is
honest; a missing section breaks the map.

**RULE 2 — lesson-unique material does NOT get its own numbered section.** It folds into the
nearest skeleton section. L02's "Make It Yours" (optional customizations, ⭐-rated) was §9
Challenges content wearing a section banner; it folds into §9. Inventing a numbered section for
one lesson's content forces the other fifteen to either carry a stub or break the map — both
worse than folding.

**WHY NOT STUB EVERY SECTION EVERYWHERE (rejected alternative, S72).** DJ raised making all
sections universal with "does not apply to this lesson" placeholders. Rejected on a pedagogy
cost: empty sections train students to skip section headers, and in a flipped course where the
reading is the gate (§25.3), a student who meets "does not apply" three times in L01 is skimming
headers by L04. Placeholder text is for a *recurring job that came up empty*, never for content
another lesson happened to have.

**§8A REMAINS CONDITIONAL** (DJ re-ruled S72, no change): present only where a genuine reusable
pattern exists, ABSENT in L1 and L16. 8A is not part of the mandatory skeleton and takes no
placeholder.

**THE TWO NON-CONFORMANT LESSONS (L01 fixed S72 · L02 cut S73):**

| | Was | Now | Cost |
|---|---|---|---|
| **L01** | §4 = *Install the Tools*; no hardware section anywhere in the lesson (Button A appears 0× in §3, encoder 0× in the whole file) | §4 covers both jobs, opening with a *Meet Your Robot* block naming the parts L01's code touches | title + a block; **no renumber** — L01's §5/§6 already matched |
| **L02** | §3 carried the code walkthrough (§5's job), §4 was prep, the build sat at §5, and a unique §6 "Make It Yours" pushed everything one ahead | §3 Theory · §4 Hardware · §5 The Code · §6 Build It; "Make It Yours" folded into §9 | full renumber, **major re-baseline v03.0.0** |

**A CONFORMANCE DIVIDEND.** §15.2 is worded *"If Section 6 has N steps, the Maker carries
`step_1` … `step_N-1`"* — the Maker's step model assumes the build is §6. That was false for L02
alone. Renumbering made the existing wording true book-wide instead of patching the rule to
accommodate one lesson. **When canon and a file disagree, check which one is the outlier before
rewording the canon.**

**AUTHORING NOTE — splitting a section is not reordering its ideas.** L02's §3 split put the C++
concepts (data types, `if`, `&&`/`||`, the Two-Week Rule, pitfalls) ahead of the anatomy
walkthrough, reversing how L02 had taught them. That was safe *because the concepts are
prerequisites for the BUILD, not for the anatomy*, and because students have already read a
complete program in L01 §5 — so nothing lands out of dependency order. The seven-section
**diagram** stayed at the top of §3 as orientation even though its walkthrough moved to §5: the
lesson tells students to print it and keep it visible, so it is a navigational aid, not §5
content. Check dependency order before moving a subsection, not just section membership.

## 5. CODE STANDARDS (unchanged from v7 — summary)

- **6-file project architecture:** `main.cpp`, `RobotConfig.h`, `RobotSensors.h/.cpp`, `RobotMotion.h/.cpp`.
- **Hardware objects** defined once; use `extern` elsewhere. `Zumo32U4OLED` (not `Zumo32U4LCD`).
- **`#define` for pin numbers only; `const` for all other values.** camelCase enforced (`baseSpeed`, `lineLostTime`).
- **Serial baud rate: 115200.** Include `Serial` timeout guard in `setup()`.
- **Single sensor read per loop** — store raw values once at loop top, reuse. Multiple `lineSensors.read()` calls (~12–15ms each) cause green-tape detection failures.
- **Non-blocking timing only** — never `delay()` in a state machine; use `millis()` timers. (This is the L10 8A topic.)
- `followLine()` lives in `main.cpp` only.
- A-Star32U4 capitalization for the microcontroller.
- **Function prototypes (v8.12 — MANDATORY):** helpers live at the BOTTOM of `main.cpp` (anatomy Section 7); every helper gets a one-line prototype in a `// ===== FUNCTION PROTOTYPES =====` block right after the hardware objects. PlatformIO `main.cpp` is real C++ — no `.ino` auto-prototypes; define-below-loop without a prototype DOES NOT COMPILE. Teaching pattern = deliberate break-fix (L02 STEP 7).
- **Native-USB serial canon (v8.12):** the Zumo's `Serial` is USB CDC — the baud number in `Serial.begin()` is effectively ignored; a mismatch does NOT produce garbage on this robot (that's UART boards like the Uno). NEVER teach baud-mismatch gibberish as a Zumo symptom. Print-at-boot is invisible (reset drops the USB port) — prints go in `loop()` or behind a button press. We still write `Serial.begin(115200)` as professional habit.
- **Compile-verify mandate (v8.12):** every new or changed lesson code block (steps, final programs, challenge solutions, bonus snippets, template skeleton) must compile on the AVR harness before delivery. Harness: avr-gcc + `arduino/ArduinoCore-avr` + `pololu/zumo-32u4-arduino-library` + deps (Pushbutton, FastGPIO, PololuBuzzer/HD44780/Menu/OLED, USBPause, core Wire), Leonardo-class env, `-mmcu=atmega32u4 -DF_CPU=16000000L`. Rebuild from GitHub clones each session. A lesson whose build sequence never compiled shipped twice (L02 ≤ v02.0.6) — this rule exists so it can't happen a third time.

---


**HARDWARE-DIRECTION VERIFICATION (v8.13 — after the L03 TRIM-inversion incident).** Any claim that maps left/right, forward/backward, or turn direction to motor commands MUST be verified against the Pololu library's own example code before it ships — e.g., `FaceTowardsOpponent.ino` implements `turnLeft()` as `setSpeeds(-turnSpeed, turnSpeed)` (right faster ⇒ turns LEFT; a robot always curves toward its slower track). A lesson that is internally consistent can still be physically backwards — L03 taught inverted TRIM logic for its entire life until S15. Internal consistency is not verification; the library examples are ground truth Claude can check without hardware.

## 5b. STUDENT PROJECT WORKFLOW & WEB TOOLS (v8.13 — LOCKED)

**Template workflow:** `ZUMO_Template/` lives in `Documents/PlatformIO` — built by students at the END of L01 (block canon in L01 v03.0.23), never worked in, only copied. Contents: canonical `platformio.ini` + skeleton `main.cpp` (header stub, all section banners incl. FUNCTION PROTOTYPES, empty setup/loop) + README ritual. Rescue copy = `ZUMO_Template.zip` at repo root.

**Start-a-New-Lesson ritual (standard §4 block, EVERY lesson L02+):** 1) Project Maker → download 2) unzip into Documents/PlatformIO 3) VS Code File→Open Folder (close old folder first) 4) header comment check (Maker pre-fills; update WHAT-THIS-DOES as you build) 5) Build ✓ health check. Manual fallback: copy template + rename by hand. iCloud caution: keep the PlatformIO folder downloaded/local.

**Naming canon (DESCRIPTIVE — supersedes `LastName_Lesson_##` and all letter-suffix schemes):**
- Main lesson build: `LastName_L##` (zero-padded; first initial for duplicate last names: `SmithJ_L02`; NO SPACES ever)
- Mystery sandbox: `LastName_L##_Mystery` — ONE per lesson, reused across its mystery challenges
- Challenge/bonus copies: `LastName_L##_<Challenge_Name>` (e.g. `Smith_L02_The_Broken_Code`, `Smith_L02_Blink_Count`)
- Copy per LESSON, never per step. Additive §9 challenges work in the main build; code-replacing challenges and bonus snippets get their own copy. Every challenge card carries a "📁 Work in:" line naming the exact destination, with a Maker deep link when a new folder is needed.

**Web tools (GitHub Pages, weymuth.github.io/zumo/) — Canvas strips `<script>`, `onclick=`, `<style>`, `class=`; ALL interactivity ships as Pages-hosted iframes:**
- `timer.html` — horizontal bar countdown (336×56 right-float, `?min=&label=`, cache-bust `?v=N` on every timer redesign). One per timed challenge.
- `newproject.html` — ZUMO Project Maker: generates correctly-named project zips with pre-filled header comments. Carries a per-lesson challenge registry — **EXTENDING the registry is a mandatory step of every lesson depth pass.** Deep-link format: `?lesson=N&kind=<slug>`.
- Printable graphics: PDF generated from the approved SVG, hosted in repo `images/`, linked via a styled download button in the lesson (this SUPERSEDES dedicated "printable version" GRAPHIC slots — L02 GRAPHIC 2.3 precedent).

**Sketch anatomy canon:** **7 numbered sections + one UNNUMBERED "FUNCTION PROTOTYPES" row** between Constants and setup() (dashed rail marker in GRAPHIC 2.5; color key shows it as an open square in Helpers blue). The count stays "seven sections" book-wide — do NOT renumber to eight.

---


### 4.5 THE BONUS BLOCK IS THREE FAMILIES, AND THE BANNER IS GENERATED (v8.72 — NEW, S85, DJ-ruled)

**Supersedes the v8.14 "Bonus" vocabulary canon.** Fifteen lessons carry a block seated at
`id="bonus-challenges"`. It had never been canonized beyond its name, so it drifted **six emoji strata,
two encodings, two separators, a doubled mark and three different pill labels** — and the drift was hiding
a real distinction. Three families, separated by ONE test: **what does the student do in the first thirty
seconds, and is anything broken?**

| family | mark | word | method | lessons |
|---|---|---|---|---|
| Practice | `&#128296;` 🔨 | **Extra Practice** | write new code; nothing exists yet | L02, L03 |
| Observation | `&#128269;` 🔍 | **Observation** | your own working build; **nothing is broken**; predict, test, explain | L04–L07 |
| Sabotage | `&#128373;&#65039;` 🕵️ | **Sabotage** | a build someone else broke; diagnose it | L08–L16 |

**Why three and not two.** Collapsing Observation into Sabotage sends a student hunting for a defect in
L04/L05/L06 where none exists — they fail to find it and conclude they are bad at this. That harm is the
argument. **Why not four:** L07's *"break it yourself in a spare copy"* is the only member of a fourth
shape, and a category appearing once in sixteen lessons is an exception a student must memorize, not a
category. L07 is **Observation** — verified by method, not by vocabulary: it has **zero Maker defect links**,
every card instructs the student what to change, and its own intro states the cycle *predict, break, build,
explain, undo*. Nothing is concealed. Its prose said *"Sabotage science"* and *"detective work"* — a word
collision describing the student's own hand, not family membership — and was reworded.

**The banner is GENERATED, never hand-typed** (the §6.8 / §6.8a precedent): every field is derived —
mark and word from the family, count word from the real card count, noun from the lesson topic.
Canonical form, byte-exact:

```
<div id="bonus-challenges" style="font-size: 1.15em; font-weight: bold;">{MARK} {WORD}: {Count} {Noun}</div>
```

⚠️ **SUPERSEDED S108, v8.97 — THE MARK COMES OFF, THE WORD STAYS.** §6.5 now rules NO ICONS
ON ANY OF THE 237 CAPS, bonus block included, and the bonus banner joins §6.5b's eyebrow /
headline pair. The form above is left standing per §26.7. Current canonical form, byte-exact,
emitted by `gen_bonus_banner.py` **v1.3.0** and asserted by gate 31:

```
<div id="bonus-challenges"><span style="{EYEBROW}">{WORD}</span><span style="{HEADLINE}">{Count} {Noun}</span></div>
```

**The three families are unharmed.** §4.5's argument was never about the glyph — a student sent
hunting a defect that is not there is misled by the WORD *Sabotage*, and the word is still on
the banner and still on the nav pill. The `mark` column above is now provenance only; `MARK`
survives in the generator, unused, for the same reason.

**The generator's mark assert INVERTED rather than being deleted.** It used to require the
family glyph to be present; it now requires that none survived — entity or raw, any family.
A gate that stops checking is worse than one that fails, so it kept its job and reversed its
polarity. Control-run both directions at S108: a mark pasted back into L09's eyebrow FAILED,
L09 reverted whole to the one-line form FAILED, untouched PASSED.

**L16 is still held out of the table** (2 cards, DJ ruling S85) and was converted by hand to
`Bonus` / `The Sabotage Files`.

**The nav pill carries the family word too**, and so does any prose link naming the section — a pill saying
"Bonus" over a section called Sabotage is the §6.8a shape of lying furniture. The pill sits OUTSIDE the
§6.5a `<!-- LESSON STRIP v1 -->` markers, so per-family wording does not break that gate.

**Two nouns inside Sabotage are DELIBERATE, not drift.** L08–L12 take per-topic nouns
(*Five Line-Following Mysteries*); **L13–L15 take "Messed Up Files"** because those are the byte-identical-build
set, a genuinely different flavour. Recorded here so a later session does not "fix" it.

**L16 is HELD OUT by DJ ruling** — it holds 2 cards against the family's 4, and revisits when it has four.
It is the only lesson still reading `Bonus:`, and `BONUS_HELD` in the gate names it explicitly rather than
letting COVERAGE silently absorb it.

**Card titles follow the family.** The 21 Observation cards were titled *Mystery N* under banners that now
say Experiments; renamed *Experiment N*, **and the five cross-references in running prose were renamed with
them** — an unrenamed cross-reference names an ancestor that no longer exists.

**Tagging IS aligned (S86, DJ ruling: three values, namespaced).** `data-kind` reads **`bonus-practice` /
`bonus-observation` / `bonus-sabotage`** — namespaced so the attribute keeps the block's shared identity
visible the way `id="bonus-challenges"` does. 42 values renamed, 26 previously untagged cards tagged, 68 in
all across 14 lessons; L16 excluded, still held.

**The marker suffix deliberately does NOT split three ways.** Practice keeps `.bN`, and Observation and
Sabotage keep SHARING `.mN`. `data-kind` carries the family, so the marker does not have to, and a rename
would churn 42 live markers for no reader. Recorded here so a later session does not "fix" it — the same
shape as the two-Sabotage-nouns note above.

**§24.6c CORRECTION RECORD — two claims in the S86 handoff were wrong and were caught by reading the files.**
(1) *"L12–L16's cards are div-titled with no heading"* — **only L12 is.** L13/L14 carry `<h4>`, L15/L16 carry
`<h3>`, so 24 of the 28 needed only an attribute on an element already there. Card title level is in fact
three strata book-wide and it crosses the tagged line: `<h3>` in L02/L03/**L11**/L15/L16, `<h4>` in
L04–L10/L13/L14, a `#6c757d` header `<div>` in L12 alone. (2) *"Renaming touches `newproject.html` (3)"* —
`data-kind` appears **zero** times in the Maker; those three hits are download `kind=` ids, a separate
namespace. **The inverse error also bit:** `book_gates.py` contains the string `data-kind` zero times and is
nonetheless the most dangerous consumer, because it reads `kind` through `lesson_inventory.build()`. **A
consumer sweep by attribute name misses every tool that consumes the PARSED value.**

**L16's hold now EXPIRES ON ITS OWN.** Gate 31 skips it by name via `BONUS_HELD`, never letting COVERAGE
absorb it silently, and FAILS the moment it reaches four cards — because the ruling was *revisit when it has
four*, and a hold that cannot expire is an exemption. Control-run both directions: two cards injected FAILED
naming the ruling; L16 removed from `BONUS_HELD` FAILED as *"neither in the family table nor held"*, so a
lesson cannot fall out of both lists into silence.

**GATED (book_gates v1.17, gate 30).** `§4.5 bonus banner generated from the three-family table, placement
asserted` — byte-canonicity, placement, the count word, mark strays/doubling, the retired "Bonus" label and
the nav pill, with **byte-canonicity and placement asserted INDEPENDENTLY** per §24.6b, and COVERAGE at 14.
Control-run **seven** ways, every injection verified in shape before the verdict was read: doubled mark
FAILED · banner hoisted out of its gray cap FAILED (relocation confirmed WHOLE, not a fragment) · count word
altered FAILED · retired label FAILED · nav pill drift FAILED · untouched PASSED before and after · and the
one that matters, **banner left byte-perfect with one real card removed → FAILED naming the count**, proving
the count assert fires on its own. New tool `gen_bonus_banner.py` v1.1 at repo root.

**§24.6c CORRECTION RECORD, twice this session.** (1) A card census read a fixed 12,000-character window from
the banner and stopped INSIDE the block, reporting L02 at 5 cards and L03 at 4 when both hold **six** — the
lessons' own *"six more"* callouts had been right all along. An extraction cut at the wrong boundary reads as
a clean result. (2) L03's *"Extra Practice"* pill was reported mid-session as the prototype the canon should
follow; it is the opposite — it is **the exact drift that triggered the S20 ruling**, surviving in the one
lesson that sweep missed. A live precedent is a lead too, and the Bible is where you check it.

### 4.5a THE BONUS BLOCK'S CAP AND ITS IN-FLOW POINTER (v8.76 — NEW, S87, DJ-ruled "B is fine")

Two constructs wrapped around the bonus block were owned by nobody. §4.5 generated the banner
*text* and stopped at the banner's own `<div>`; everything around it drifted. Both are now generated
from ONE constant each and asserted byte-exact.

**THE CAP — the gray div the banner sits in.** Canonical, all 15:

```
<div style="background-color: #6c757d; color: white; padding: 13px 18px; border-radius: 8px 8px 0 0; margin-top: 24px;">
```

L03 shipped `background: linear-gradient(135deg, #6c757d, #4d5358)` with `padding: 12px` and
`margin-top: 40px` — a visibly different banner — and **passed gate 30 for its entire life**, because
the placement check was a SUBSTRING test (`'#6c757d' not in capstyle`) and a gradient *containing*
`#6c757d` satisfies it. **A substring test cannot distinguish flat from gradient.** Now compared
byte-exact, and generated by `gen_bonus_banner.py` v1.2.

**THE POINTER — the FINISHED EARLY callout.** Canonical, all 14:

```
<div style="background-color: #f8f9fa; border: 2px solid #6c757d; border-radius: 10px; padding: 15px 20px; margin: 25px 0;">
```

It existed in **L02–L09 and was ABSENT in L10–L15**, so in six lessons the only route into the bonus
block was one nav pill among twelve to fourteen. Its livery had drifted into **three strata, 2/2/4,
cutting ACROSS the families rather than along them** — Observation split down the middle (L04/L05
against L06/L07) and L06–L09 shared one form across two different families.

**THE MARK STAYS WITH THE FAMILY.** Practice keeps 🎯 and *"FINISHED EARLY? Want more practice?"*;
Observation and Sabotage take 🏁 *"FINISHED EARLY?"*. Livery is uniform, mark is not — recorded so a
later session does not "fix" it. §6.6a governs 💡/📘/⚠️ only; these marks sit outside it.

**WHY B, and not the plurality.** `#6c757d` is the **§10+end section-group color** in the nav scheme,
which is exactly where the bonus block lives — so B's livery is DERIVED from an existing rule rather
than hand-picked. The rejected forms: A used `#3a7d5c`, canonical but it is the **§4–6** green,
pointing at the wrong section group; C was the 4-lesson plurality but its `#e3f2ed`/`#3d8b6e` have
**zero Bible mentions** and ~11 uses book-wide — near-misses of the canonical green that look right
and are not. **The plurality was the least canonical option.**

**REBRAND-READY BY CONSTRUCTION.** Each construct asserts exactly one constant — `BONUS_CAP` and
`FE_BOX`. A branding guide changes those two strings, the generator re-runs, and all fifteen blocks
repaint and re-prove themselves. Canvas strips `<style>` and `class=`, so inline color is forced and
there is no variable to change; **generation from a table is the only mechanism that scales.** A
construct that is hand-maintained when a brand guide lands costs a sixteen-lesson sweep, and again on
every revision.

**THE PROSE IS AUTHORED, NOT GENERATED.** Each clause names that lesson's own planted defects — L14's
reads *"a dropped zero that passes every dead battery"* because B3 is literally `mv >= 420` instead of
`4200`. Write it from the cards, never from the card titles.

**GATED (book_gates v1.18 → v1.20).** Gate 30 now compares the cap byte-exact; **new gate 32
`§4.5a every bonus block is announced by a canonical FINISHED EARLY pointer`** asserts presence
(exactly 1), byte-canonical livery, precedence before the block, and that it carries the link, with a
COVERAGE assert at 14. Control-run five ways, every injection verified landed first: cap — gradient
re-introduced FAILED and a flat cap with `padding: 13px→12px` FAILED, **where the OLD gate PASSED
BOTH**; pointer — deleted FAILED, reverted to the old livery FAILED, moved after the block FAILED,
untouched PASSED.

**§24.6c CORRECTION RECORD.** Locating the cap by searching back from the `id="bonus-challenges"`
offset lands on the banner's OWN `<div>`, not the wrapper — it must be located from the banner
match's START (gate 30 does this correctly; two ad-hoc audits in S87 did not). Also: `git checkout`
reverts to HEAD, which during an unpushed session is the DEFECT, so two controls silently tested the
wrong tree until the injection was asserted.


### STANDARD HELPERS — L04+ (v8.13 — LOCKED)

From Lesson 04 onward, every Maker-generated skeleton (all kinds: main, challenge, custom) ships with a **STANDARD HELPERS (added after Lesson 3)** block at the file bottom, with prototypes declared in the FUNCTION PROTOTYPES section (the template itself models the L02 layout canon). Lessons 01–03 stay clean — those lessons teach the pieces. The two helpers, compile-verified (13,002 B on the harness):

- **`waitForStart()`** — SAFETY GATE. OLED shows "Press A / to start"; `buttonA.waitForButton()`; clear + `delay(500)` to get hands clear. Called at the END of `setup()`, always. **Canon rule: from L04 on, no driving program ever moves at power-on — motion waits for a button press.** Depth passes on L04–L15 must adopt this in their main builds.
- **`checkBattery()`** — A+B BATTERY CHECK. Hold Buttons A + B together at any time: OLED shows battery millivolts while held, waits for release, clears. Called at the TOP of `loop()`. **Canon rule: A+B held = battery check, book-wide from L04.** No permanent screen space is reserved for battery (supersedes any row-0 reservation idea). Uses only L03 knowledge (combo-press pattern = L03's A+C reset precedent).

Manual fallback ritual for L04+ (no internet): copy ZUMO_Template, rename to `LastName_L##`, **and paste the STANDARD HELPERS block** (lessons provide it in a copyable dark box during their depth passes). `ZUMO_Template.zip` itself stays the clean L01 version — it is the teaching artifact.

### THE TOOLCHAIN IS PINNED (v8.23 — LOCKED, S36)

**`lib_deps` names an EXACT version. Never a bare package name. Never a caret range.**

```
lib_deps = pololu/Zumo32U4@2.0.1
```

**Why this is a rule and not a preference:** this book publishes **exact byte counts** — L15 ships at 28,034 B against a **28,672 B ceiling, 638 B of headroom**. A library update that adds a few hundred bytes to Pololu's code does not merely make a figure stale; it pushes a student's build **over the wall**, while the lesson insists the number should have fit. An unpinned dependency silently invalidates every byte in the book.

**Why EXACT and not `^2.0.1`:** the caret means `>=2.0.1, <3.0.0`. A future 2.1.0 would satisfy it and land silently — which is the exact drift the pin exists to prevent. `~2.0.1` is better (patch-only) and still not tight enough. Take the exact version; when a real update lands, change the number **deliberately** and re-audit the bytes.

**IN-FILE VERSION — TWO DURABLE HOMES (v8.31, REVERSES the old major-digit-only rule).** The published filename is stable `Lesson_NN.html` (no version), so the version must live INSIDE the file — in two places, at two precisions:
1. **VISIBLE banner** (the header hero, line 5): **major.minor only**, e.g. `Version 03.2` / `v03.2`. It updates on a MODERATE-or-larger bump and is deliberately LEFT ALONE on a minor/cosmetic bump — so a pill recolor (`v03.2.4 → v03.2.5`) does NOT touch the visible banner.
1b. **A THIRD HOME EXISTED FROM S70 TO S89 AND IS RETIRED — see the note below this list.**
2. **HIDDEN HTML comment**, first line of the file: **full three-digit**, e.g. `<!-- Lesson version: v03.2.5 -->`. Updated on EVERY delivery (it is the authoritative in-file record). Greppable: `grep -o 'Lesson version: v[0-9.]*'`.

**THE VERSION HAS TWO HOMES, AND ONLY ONE IS VISIBLE.**

**THE HIDDEN BUILD BANNER IS RETIRED (v8.77, S89 — supersedes v8.53).** From S70 to S89 a third home existed: an HTML comment before `</body>` repeating major.minor plus the date and page title. It was **deleted from all 17 pages at S89**. Two reasons, and the second is the one that matters:

- It was never visible, so it provided no redundancy a reader could ever act on. The v8.53 argument for it — *"a visible footer number can rot in front of students, a hidden one cannot"* — is true and also an argument for not having it at all.
- **The v8.53 entry stated openly that the gate needed no edit because "it greps raw source, and raw source includes comments, so a comment satisfies it exactly as a rendered banner did."** That is a gate being *deliberately relied upon for a property it does not check*. The check was named "hidden == both visible banners" and could not see visibility at all. **A gate leaned on for what it cannot distinguish turns an accident into load-bearing structure**, and this one held for nineteen sessions.

The retired block also carried `ZUMO Callout Standard v1.0 Applied`, a conformance stamp naming a document that never existed — asserted in 17 files solely because a gate asserted it. Its successor is `BookComponentStandard.md` at the repo root, which does exist and can be read. See §24.9.

WHY: with a stable filename and a major-only banner, the exact minor version was recorded ONLY in LIVE.md. When LIVE.md corrupted (S45), L11–L16's true minor became unrecoverable from the repo — the deep clone could only reach a git-rename FLOOR. The hidden comment ends that single-point-of-failure. GATE at close: assert the hidden comment, the visible banner's major.minor, and LIVE.md all agree.

**The registry, as of S36 (July 2026):** `pololu/Zumo32U4` has exactly **two** versions — 2.0.0 and **2.0.1 (latest, published 2022-09-07)**. GitHub tags agree and stop at 2.0.1. **There is no 2.1.0 and there never was.** The library ships only `library.properties` (Arduino manifest); there is **no `library.json`**.

**HOW TO CHECK — never guess a version number:**
```
pio pkg show pololu/Zumo32U4
```
This prints the registry's real version list. Canonized after S36: L01's §8 troubleshooting table had recorded a real `UnknownPackageError` on a `^2.1.0` pin — a **typo**, since 2.1.0 never existed — and the "fix" the book published for it was **"Remove the version pin."** That advice traded a typo for a permanent hole, and the fleet ran unpinned for a year. **A bad pin is fixed by pinning correctly, never by unpinning.** L01 now teaches this.

**GATE CHECK:** grep the Maker's `var INI` template and every lesson `<pre>` showing `platformio.ini` — the `lib_deps` line must be byte-identical everywhere and must carry an `@version`. (S36 also found L01's two `platformio.ini` code blocks disagreeing with each other: one inline, one split across two lines. Both are legal ini; only one matched what the Maker actually writes.)

### WEB-TOOL VERSIONING (v8.13 — LOCKED)

Web tools (`timer.html`, `newproject.html`, future tools) keep **unversioned filenames** — lesson deep links and iframes depend on them. The version lives ONLY inside: a header comment with the full version chain, plus a small visible footer line where layout allows (Maker shows "Project Maker v1.3"). The `?v=N` query token in lesson iframe URLs is a **cache-buster, not a version** — it bumps on every push and drifts from the internal version by design. Versions follow the standard scheme (v# / v#.# / v#.#.#) and are tracked in LIVE's web-tools line.

**THE VERSION LINE IS THE FIRST LINE (v8.54, S70).** Every web tool opens with a greppable canonical comment before `<!DOCTYPE html>` — `<!-- Timer version: v1.3.0 -->`, `<!-- Maker version: v2.45.1 -->`, `<!-- Tutor version: v1.0.0 -->`, `<!-- Index version: v1.3.0 -->` — matching the lesson convention. Gated: `§5b web tools carry an in-file version line` (book_gates v1.5).

WHY, and it is not theoretical: the sentence this replaces read *"Current: timer v1.2, Maker v1.3"* while the Maker was actually at **v2.45** — the Bible carried a number forty releases stale, and `timer.html` and `tutor/tutor.html` carried **no in-file version at all**, the exact single-point-of-failure §5b exists to close. Worse, `newproject.html`'s changelog block OPENS with `v2.18`, the original release, so a naive grep of its head returned a number 27 releases stale — the **v3.0 ghost** trap in its purest form. **Never record a tool version in Bible prose; record that the file carries it, and grep the file.** `sort -V`, never `sort -u`.

**Baselines, honestly labelled.** timer v1.3.0 and index v1.3.0 succeed the last recorded v1.2 / v1.2.1; tutor v1.0.0 is a declaration, since no number for it existed anywhere. Each file's own header comment says which it is. A baseline that admits it is a baseline is recoverable; one that poses as recovered history is not.

## 6. CANONICAL SKIN (v8 — LOCKED) — "THE LESSON 9 LOOK"

> This section **supersedes** the entire v7 "HTML Style Guide" (v7 §6). The old serif body, flat `#2c3e50` nav, `135deg`/`to right` gradients, and Part-colored dividers are **retired**. Reference implementation for the skin: `Lesson_09` (as rebuilt). All lessons conform to this.

**All styling is true inline** — every element carries its own `style=""`. No `<style>` blocks, no CSS classes (Canvas strips them). ⚠️ **CONDITIONAL AS OF S103 — see §27.** This rule exists ONLY because Canvas strips `<style>` and `class=`. DJ ruled S103 that lessons are no longer pasted into Canvas, so the constraint has no remaining cause. It still governs every lesson file **until the migration converts them**; do not author against the post-migration model in a file that has not been converted.

### 6.1 Body

```html
<body id="top" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.7; max-width: 900px; margin: 0 auto; padding: 20px; color: #333; background-color: #fafafa;">
```

- Font: **Segoe UI** sans-serif stack (NOT Georgia/serif).
- Background: `#fafafa`.
- `id="top"` on the body so "Back to top" links resolve to `#top`.

### 6.1a Two-column layouts must be responsive (LOCKED v8.3)

Any side-by-side two-column comparison (e.g. `.h` vs `.cpp`, MISTAKE vs CORRECT, BEFORE vs AFTER) MUST use a self-stacking grid — NOT a fixed `1fr 1fr`. Canvas strips `<style>`, so no media queries; use `auto-fit` + `minmax` instead, which stacks to a single column on narrow screens with pure inline CSS:

```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">
```

- **Banned:** `grid-template-columns: 1fr 1fr;` — forces 2 columns at every width and overflows the right border on phones/narrow panels (dark code blocks don't shrink).
- **Required:** `repeat(auto-fit, minmax(280px, 1fr))` — 2 columns when there's room (≥~580px), auto-stacks to 1 column when narrow.
- Flex two-column layouts must carry `flex-wrap: wrap` for the same reason.
- §11 check: FAIL if any `grid-template-columns: 1fr 1fr` (or other fixed multi-column track list without `auto-fit`/`minmax`) exists.

### 6.1b Back-to-top links (LOCKED v8.3.1)

Every section (and end-matter section) carries exactly ONE "Back to top" link at the end of its box, right before the box-closing `</div>`:

```html
<p style="text-align: right;"><a href="#top" style="color: #2e86ab;">↑ Back to top</a></p>
```

- **Standard link color: `#2e86ab`.** (Some lessons historically used `#3498db`; normalize to `#2e86ab` on next touch.)
- Exactly one per section — no strays mid-section, none missing. Insert via a depth-aware walk (each section box from open to its matching close), not a fragile "nearest `</div>`" search.
- Target is `#top` (the `id="top"` on `<body>`).


### 6.2 Gradient rule (applies everywhere)

**All gradients are top-down, dark color first:** `linear-gradient(to bottom, <DARK> 0%, <LIGHT> 100%)`. No `135deg`, no `to right` — **except** challenge-card and milestone headers, which keep their original `135deg` / `to right` (see §6.2a + §6.12).

### 6.2a Gradient vs. Solid — by ELEMENT ROLE (LOCKED)

Whether an element is a gradient or a flat solid is determined by its **role**, not flattened globally:

- **Gradient (hero / header elements):** the sticky **nav bar**, the **title block**, **challenge-card headers** (§6.12), and **milestone headers**. These are one-off or attention-anchor headers.
- **Solid (section-system elements):** **section caps**, **PART banners**, **nav buttons**, and **section-marker pills**. Anything that repeats as part of the per-section grid is flat solid.

Rule of thumb: if it's a *page/section header or a challenge/milestone announce-bar*, gradient is allowed; if it's part of the repeating section skin, it's flat solid. (This is why a §9 cap is solid plum but a §9 challenge-card header is a plum gradient — and that visible light/dark difference is intentional, not a bug.)

### 6.3 Sticky Navigation Bar

```html
<nav style="background: linear-gradient(to bottom, #1a5276 0%, #2e86ab 100%); border-radius: 10px; padding: 15px 20px; margin-bottom: 30px; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
    <div style="display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; align-items: center;">
        <a href="#section-1" style="color: white; text-decoration: none; padding: 5px 12px; border-radius: 4px; font-size: 0.85em; background-color: #3498db;">1. Intro</a>
        <!-- … one per section … -->
    </div>
</nav>
```

**Nav button colors (by section):**
- Sections 1–3: `#3498db` (blue)
- Sections 4–6: `#3a7d5c` (evergreen)
- Sections 7, 8 **and 8A**: `#c45d76` (dusty rose)
- **Section 9 (Challenges): `#9b6a9e` (plum)** — its own color, split out of the old rose group
- Section 10 + Glossary + Quick Ref + Image Index: `#6c757d` (gray)

**Nav button count:** 12–14. Base = §1–10 + Glossary + Quick Ref (12); +1 if 8A present; +1 if Bonus present. **The Image Index has NO nav button** (DJ ruling, S35) — the section still exists and still wears gray `#6c757d`, but students do not navigate to it. L01 = 12 (no 8A, no Bonus) · L16 = 13 (no 8A) · L02–L15 = 14.

### 6.4 Title Block (gradient banner, NO leading icon)

```html
<div style="text-align: center; padding: 40px 20px; background: linear-gradient(to bottom, #1a5276 0%, #2e86ab 100%); color: white; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 5px 20px rgba(0,0,0,0.15);">
    <h1 style="margin: 0; font-size: 2.4em; color: white;">LESSON 10</h1>
    <div style="font-size: 1.3em; opacity: 0.95; margin-top: 8px;">Obstacles: Teaching Your Robot to Navigate Roadblocks</div>
    <div style="font-size: 1em; opacity: 0.9; margin-top: 8px;">Zumo 32U4 Robotics • PlatformIO Edition</div>
    <div style="font-size: 0.9em; opacity: 0.8; margin-top: 5px;">Version 1 — June 2026</div>
</div>
```

- `<h1>` is **`LESSON ##` with NO leading emoji.**
- Four lines: LESSON ##, descriptive title, series line, version line.

### 6.5 Section Headers — CAP + BOX (LOCKED)

Every section (and every end-matter block: Glossary, Quick Reference, Image Index) is a **colored cap on a matching bordered box.** The cap holds the title in white; the box wraps that section's content. The old plain `<h2>` heading style (`#1a5276` text + bottom border) is **retired**.

```html
<div style="background-color: #3498db; color: white; padding: 13px 18px; border-radius: 8px 8px 0 0; margin-top: 24px;">
    <div id="section-1" style="font-size: 1.15em; font-weight: bold;">📖 Section 1: The Roadblock</div>
</div>
<div style="border: 2px solid #3498db; border-top: none; border-radius: 0 0 8px 8px; padding: 18px; margin-bottom: 16px;">
    … section content …
    <p style="text-align: right;"><a href="#top" style="color: #3498db;">↑ Back to top</a></p>
</div>
```

- **Cap:** solid PART color, white bold title (≈1.15em), rounded top only (`8px 8px 0 0`), `margin-top: 24px`. The `id` lives on the inner title div (anchor target).
- **Box:** `border: 2px solid <PARTcolor>; border-top: none; border-radius: 0 0 8px 8px; padding: 18px; margin-bottom: 16px`. Caps the section content; back-to-top link sits inside.
  - **CONFIRMED AND UNIFIED S108, v8.97 (DJ ruling A).** The book had shipped TWO forms of this
    box — the one above in L01–L09, and `padding: 20px 25px; background: white` with no
    `margin-bottom` in L10–L16 — split at the identical seam in ALL FIVE colour groups and
    invisible to every gate. 104 panels moved to the form above and **five duplicate rules
    collapsed, one per colour where there had been two** (`css/book.css` 665 → 660). DJ chose
    it on a rendered specimen, not a table. Type treatment E's 26px inset is NOT adopted.
- **Section-group colors (match the nav buttons):** §1–3 `#3498db` blue · §4–6 `#3a7d5c` green · §7/§8/§8A `#c45d76` dusty rose · **§9 `#9b6a9e` plum** · §10 + Glossary/Quick-Ref/Image-Index `#6c757d` gray. Each group owns ONE color; every element in it (cap, nav button, PART banner, challenge cards, table headers in that section) wears that color.
- **Cap KEEPS the leading icon** (`📖 🔨 ▶️ ⚠️ 🔑 🏆 📋` etc.); only the title-block h1 has no icon.
  - ⚠️ **SUPERSEDED S108, v8.97 — NO ICONS ON ANY CAP.** DJ ruled at S107 that all 237 caps
    are bare, bonus block included, and it was applied book-wide at S108: 237 caps carried a
    leading emoji, zero were bare, and now the reverse is true (verified by DOM lookup, not
    regex — 237/237). The rule above is left standing per §26.7, because a record edited in
    place is not a record. **What the icons were carrying is now carried by the EYEBROW** —
    see §6.5b. What this closed: six banners rendering their icon twice, the white-mark
    problem in `BookComponentStandard` §7, the bullseye/book collision at §2/§3, and §8's
    🔧/⚠️ split. The 41 marks in `images/marks/` remain UNWIRED and are a separate arc.
- The cap `id` must match the visible "Section N:" label and the nav anchor.

### 6.5a-T TYPE TREATMENT "E" (NEW, v8.97, S108, DJ ruling)

The book is served **Inter**, the way `index.html` and `going_deeper.html` already serve it —
`fonts.googleapis.com`, weights 400/500/600/700, a `preconnect` plus a stylesheet link in every
lesson head. This is legal only because §27 retired the Canvas-paste model; web fonts were not
available under it.

**RETIRED: `.page { font-family: 'Segoe UI', Tahoma, Geneva, Verdana }`.** Segoe UI is
Windows-only, so every reader on a Mac, iPad, Chromebook or Android had been served Tahoma or
Geneva — a typeface nobody chose — for the life of the book. `font_stack_sweep` reported **0
rewrites across 207 files** the entire time, because it scanned SVGs and never opened
`css/book.css`. Fixed at S108, v1.1.0; control-run against the pre-session stylesheet, where it
names `Segoe UI` correctly.

| property | was | is |
|---|---|---|
| `.page` font-family | `'Segoe UI', Tahoma, Geneva, Verdana` | `'Inter', -apple-system, sans-serif` |
| `.page` line-height | `1.7` | `1.65` |
| `.page` color | `#333` | `#1d1d1f` |
| cap headline | 1.15em bold | 1.28em / 700 / `-0.021em` (§6.5b) |

All three body properties lived in ONE rule, so the whole visible change was three declarations
plus two link tags × 16. Census moved 39,993 → 40,025, exactly +32 — two lines per file.

**NOT adopted, and deliberately so:** E's padding 18px→26px, callout margins 20→26px and table
cells 12→14px. `padding: 12px` occurs **925 times** across every construct in the book, so
those cannot be reached by string match. The section content panel is the exception — it is ten
named rules — and DJ ruled it separately to 18px (§6.5 Box). **The 2px border, 8px radius and
full table grid are UNCHANGED by ruling**; a lighter treatment was built and rejected.

**A face the site actually serves is not a substitution risk.** `font_stack_sweep`'s rewrite map
was written for SVGs, where no web font can be relied on, and proposed `Inter → Arial` the
moment it opened a stylesheet. Web-served faces are exempt in `.css` context ONLY, and the
exemption list is a claim checkable against the link tags.

### 6.5b THE CAP IS TWO LINES — EYEBROW AND HEADLINE (NEW, v8.97, S108, DJ ruling)

Every cap renders as **an eyebrow above a headline**, never one line.

> **Headline = the most descriptive string available. Eyebrow = everything before it.**

- **Eyebrow** — `0.78em`, weight 600, `letter-spacing: 0.1em`, uppercase, `opacity: 0.8`,
  `margin-bottom: 3px`. Carries `Section N`, and where the section has a NAME as well as a
  written title, `Section N &middot; Name`.
- **Headline** — `1.28em`, weight **700**, `letter-spacing: -0.021em`.
- Caps with no `Section N` — Glossary, Quick Reference, Figures — ship the headline span
  ALONE. 189 of the 237 carry an eyebrow; the other 48 are these three × 16.

**The section NAME therefore moves.** It sits in the eyebrow when a written headline exists
(§3–§7) and IS the headline when one does not (§2, §8, §8A, §9, §10). Visually uniform,
structurally two shapes — and §6.8a's fence has to know both.

**THE FENCE RULE (extends §6.8a).** The fence title is **the eyebrow's name after the
middot, or the headline where the eyebrow carries no name.** This keeps the fence DERIVED,
which is §6.8a's entire premise — L01 once shipped a fence reading `KEY CONCEPTS` above a
banner reading *Background Theory*, and a hard-coded fence vocabulary would reinstate exactly
that gap. `_fence_title()` in `book_gates.py` knows both shapes and was control-run in both
directions against a converted lesson and a legacy one.

**KNOWN FAILURE MODE OF THE MECHANICAL SPLIT.** Where the tail is the LESS interesting half,
the split promotes the dry part. Found once (L04 §8A, *"Deciding and Repeating — If Statements
and For Loops"*), resolved by dropping the tail. Watch any cap where a dash appears.

**“Opening Hook” and “Introduction” are AUTHORING LABELS** and were removed from §1 in L03,
L14, L15 and L16 — they had leaked into student-facing text. The other twelve §1 fences were
already lesson-specific, so this did not make the book less uniform; it made four files match
the twelve.
- **Sub-headings + table headers adopt the SECTION GROUP COLOR** (LOCKED — supersedes the old global blue h3 / navy table-header). Each section's internal headings and table headers wear that section's color:
  - **h3** (subsections, e.g. "5.3 …") → the section group color (§1–3 `#3498db`, §4–6 `#3a7d5c`, §7/8/8A `#c45d76`, §9 `#9b6a9e`, §10+end `#6c757d`).
  - **h4** (sub-subsections) → also the section group color (same as h3 — NOT a separate green).
  - **Table headers** (the `<th>`/header row) → a DARKER shade of the section color (see table below).
  - **Exception:** callout-internal headings (e.g. Exit Ticket h4s inside callouts, Icon Guide h3) keep their callout styling — exempt from this rule.
  - (h2 is no longer used for section titles — the cap replaces it.)

**Section color → darker table-header shade (LOCKED):**

| Group | Section color (cap, h3, h4, nav) | Darker table-header shade |
|---|---|---|
| §1–3 | `#3498db` blue | `#1a5276` |
| §4–6 | `#3a7d5c` green | `#2a5a42` |
| §7/8/8A | `#c45d76` rose | `#9a4459` |
| §9 | `#9b6a9e` plum | `#704c73` |
| §10 + end | `#6c757d` gray | `#4d5358` |

(The old `#2e86ab` global-blue h3 and `#1a5276` global-navy table header are retired except where blue IS the section color, i.e. §1–3.)

### 6.5a THE LESSON STRIP (v8.52 — S69, DJ ruling: "Love c")

Every lesson's sticky nav carries a **second, thinner row**: sixteen numbered squares 01–16 linking to `Lesson_NN.html`, a leading small-caps "LESSON" label, and a trailing `&#8962;` home square to `../index.html`. The row sits inside the same `<nav>`, below the section pills, separated by `border-top: 1px solid rgba(255,255,255,0.25)` with `margin-top: 10px; padding-top: 9px`. Squares: `padding: 2px 7px; background-color: rgba(255,255,255,0.14); border-radius: 4px; font-size: 0.78em; color: white`, each carrying the lesson's canonical title as a `title=` tooltip. The current lesson renders as a **solid white square** (`#ffffff` background, `#1a5276` bold text).

**The block is ONE byte-identical unit in all 16 lessons — never hand-varied.** All sixteen files carry the same static links (so the strip works without JavaScript), and a small self-hydrating script derives the current lesson from `location.pathname` at load and swaps that square to the highlight. Bound by marker comments `<!-- LESSON STRIP v1 (§6.5a) -->` … `<!-- /LESSON STRIP -->`; a renumber or an L17 is one edit to the block re-applied everywhere. **Gate:** `§6.5a lesson strip present and byte-identical in all 16` (book_gates v1.3, control-run S69 against the pre-strip clone where it FAILED with 16 missing, and against an injected one-character drift where it FAILED as "differs").

**The strip does NOT count against the §6.5/v8.21 nav-button ceiling (12–14).** That ceiling governs the section-pill row; the strip is a separate chrome row in the neutral rgba-white family precisely so it never collides with the section color code.

**Callout / radius tiers (LOCKED — two-tier "notes vs. frames"):**
- **Inline content callouts** (border-left accent notes: tip, warning, key term, checkpoint, do-this-now, insight/learn) → **`border-radius: 4px`**.
- **Glossary / term cards** → **`8px`** (deliberate exception: they use a border-left accent like callouts but are reference cards, not inline notes — distinguished by the purple palette `#e7d4ff` bg / `#9b59b6` border).
- **Structural containers** (full-bordered frames, image placeholders, PART banners, title block, challenge boxes) → **`8px`**.
- The retired one-side style `0 8px 8px 0` must NOT be used on callouts. **Exception — the cap/box pair is intentionally one-side-rounded** (cap `8px 8px 0 0`, box `0 0 8px 8px`): together they form one rounded container, so the §11 "no one-side rounding" check does not apply to the cap/box pair.
- Machine rule: a `border-left` accent box → 4px *unless* it's the purple glossary palette (→8px); a full `border` (all sides) → 8px.
- Other radii: code blocks `6px`, nav buttons & pills `4–5px`, inline code chips `4px`.

### 6.6 Icon Legend (13 icons) — **THE BLOCK IS RETIRED (S111). The ICON SET below is still canon.**

> **SUPERSEDED IN PLACE, not rewritten (§26.7).** DJ ruling S111: *"Let's strip the icon
> legend."* The in-lesson legend block is removed from the ten lessons that carried one;
> **L11–L16 never had one**, which is why the construct was already inconsistent and why
> removing it made the book uniform rather than newly deficient. The markup below is kept as
> the record of what shipped — do NOT author it into a lesson.
>
> **The ICON TABLE is untouched and still governs.** The glyphs go on living in the callouts;
> only the legend that explained them is gone. **Measured consequence, recorded because it is
> the reason to reopen this if anyone ever does:** a key-term callout renders as `🔑 TRIM`, not
> `🔑 KEY TERM`, so in L03 the literal string *KEY TERM* appeared exactly ONCE in the whole
> file — in the legend — against 16 uses of the glyph. Ten lessons therefore lost their only
> glyph key. DJ, offered a replacement key in the Glossary or Going Deeper: *"i'm getting used
> to it."* Not built.
>
> **The canon and the live blocks had already disagreed and nobody had looked:** this section
> specifies THIRTEEN icons including 📘 NOTE, and every live block carried TWELVE — NOTE was
> added to the table at v8.40 and never added to the blocks. A legend that omits a family it
> claims to legend is worse than no legend, which is a second argument for the ruling that
> nobody made at the time.


```html
<div style="background: #fff; border: 2px solid #2e86ab; border-radius: 10px; padding: 15px 20px; margin-bottom: 30px;">
    <h3 style="margin-top: 0; color: #1a5276; font-size: 1em; margin-bottom: 10px;">Icon Guide</h3>
    <div style="display: flex; flex-wrap: wrap; gap: 15px; font-size: 0.9em;">
        <span>📖 LEARN</span><span>💻 CODE</span><span>🔨 BUILD</span><span>▶️ TEST</span>
        <span>✅ CHECKPOINT</span><span>⚠️ WARNING</span><span>📝 DO THIS NOW</span>
        <span>🔑 KEY TERM</span><span>💡 TIP</span><span>📘 NOTE</span><span>👀 SEE</span>
        <span>🔍 INSIGHT</span><span>🔮 NEXT</span>
    </div>
</div>
```

The 13 icons: 📖 LEARN, 💻 CODE, 🔨 BUILD, ▶️ TEST, ✅ CHECKPOINT, ⚠️ WARNING, 📝 DO THIS NOW, 🔑 KEY TERM, 💡 TIP, 📘 NOTE, 👀 SEE, 🔍 INSIGHT, 🔮 NEXT.

**§6.6a — TIP / NOTE / WARNING: ASSIGN BY FUNCTION (LOCKED, S61).** Three coach-voice callouts, distinguished by what they DO, not by feel. Labels are **bare** ("Tip" / "Note" / "Warning", never "Coach's Tip/Note") to match the Icon Guide; the coach's warmth lives in the prose, not the label.
- 💡 **Tip** — green `#f0f7f0` bg / `#6b8e6b` border — *actionable: a way to make something work or fix an error a coach would share* (e.g. "if you get a 'please install git client' error, go to §4.2 and install Git").
- 📘 **Note** — slate `#eceff1` bg / `#607d8b` border — *enrichment: extra information that deepens the lesson* (history, terminology, "also called…", the reason something works).
- ⚠️ **Warning** — amber `#fff8e1` bg / `#ffc107` border — *a real caution, usually safety* (don't stall the motors; don't drain NiMH past ~4,200 mV). A titled warning keeps its descriptive title (e.g. "⚠️ Battery Safety").
**The original book had Tip and Note INVERTED** — enrichment wore 💡 Tip and actionable fixes wore the amber "Coach's Note" (the icon drove the label). Corrected book-wide S61 by reassigning every coach callout by function. Authoring test: tells you how to do/fix → **Tip**; background/context → **Note**; risk of harm → **Warning**.

### 6.7 Section-marker pills — RETIRED

The old "READING / CODE / BUILD / TEST — <tagline>" marker pills (`#2e86ab` rounded pills placed at the top of a section) are **retired**. They are redundant with the section CAP, which already labels the section and carries its icon. **Remove every section-marker pill** during retrofit — do not place any `<LABEL> — <tagline>` pill or banner inside a section. (This is the same principle as the orphan intro-banner ban in §7.)

### 6.8 PART DIVIDERS — GENERATED FROM THE SECTION SPINE (rewritten v8.70, S84)

Four PARTs, five color groups. Each PART divider is a **generated block** — an invisible fence comment plus a solid-color banner — seated immediately before the SECTION fence of the section it introduces. It is DERIVED, never authored: regenerate it, do not maintain it.

```html
<!-- ===================== PART 1: THEORY & CONCEPTS ===================== -->
<div style="background-color: #3498db; color: white; padding: 12px 20px; border-radius: 8px 8px 0 0; margin: 22px 0 0;">
    <div style="font-size: 18px; font-weight: 500; letter-spacing: 0.5px;">PART 1 — Theory &amp; Concepts</div>
    <div style="font-size: 12px; color: rgba(255,255,255,0.85); margin-top: 4px;">Sections 1–3: Learn the fundamentals</div>
</div>
```

| PART | Color | Title | Subtitle | Seats before |
|---|---|---|---|---|
| 1 | `#3498db` blue | Theory &amp; Concepts | Sections 1–3: Learn the fundamentals | §1 |
| 2 | `#3a7d5c` green | Hardware &amp; Code | Sections 4–6: Set up and program your robot | §4 |
| 3 | `#c45d76` dusty rose | Testing &amp; Challenges | Sections 7–8A: Verify and extend | §7 |
| 4 | `#9b6a9e` plum | Challenges | Section 9: Apply what you have learned | §9 |

- **PART 3's subtitle is the only variant**: `Sections 7–8A` where `section-8a` exists, `Sections 7–8` where it does not. Only L01 and L16 lack §8A.
- **The fence comment mirrors §6.8a**: twenty-one `=` per side, one space inside, uppercase, `PART N: TITLE`, title derived from the banner with entities decoded. **64 book-wide, one per PART.**
- **`border-radius: 8px 8px 0 0` and `margin: 22px 0 0` are load-bearing** — they fuse the PART cap onto the section banner directly beneath, which is why placement is not cosmetic. The pre-v8.70 snippet in this Bible said `border-radius: 8px; margin: 22px 0 10px`, which renders a DETACHED box; all 64 live blocks disagreed with it, so the live form is canon and the snippet was the error.
- **Text encoding is fixed**: literal em-dash in the title, `&amp;` for the ampersand, literal en-dash in the subtitle, subtitle opacity `0.85`.
- 18px title, 12px subtitle. §10 + end matter have **NO** PART banner — the untitled gray tail after PART 4. The old navy gradient is retired; so is the "PART 5 — Wrap Up" banner L10–L16 once invented.
- **Four PARTs total**: 1=§1–3, 2=§4–6, 3=§7–8A, 4=§9.

**Why it is generated and not maintained (S84).** The queue carried this as *"L02/L06/L15/L16 carry zero PART banner comments"* and called it the biggest unexamined structural item. Reading it dissolved that premise — all sixteen lessons carry four visible banners in the correct twelve colors — and replaced it with four defects nobody had named:

1. **The zeros were half matcher artifact.** `lesson_inventory.py` required the `=` wrapper, so L02's `<!-- PART 1: THE CHALLENGE -->` (3) and L06's `<!-- PART 1 DIVIDER -->` (4) both counted as **zero**. Only L15/L16 truly had none. This is §6.8a's blindness repeating one construct over — same instrument, same wrapper assumption.
2. **Five banners capped the wrong section, and nothing had ever looked.** L12 PART 3, L13 PART 3 + PART 4, L14 PART 3 + PART 4 all sat one section boundary early. Because the cap is FUSED to the banner beneath, L13 rendered a plum *"PART 4 — Challenges / Section 9"* welded to the top of §7's rose Calibration Ladder. Visible on every page load, and invisible to all 26 gates.
3. **Three content deviations.** L04's PART 2 titled *Hands-On Setup & Programming* (logged S72, unfixed twelve sessions); L05's PART 2 claiming *Sections 4–7*, a section its own PART 3 also claims; L05's PART 4 claiming *Sections 9–10*, where §10 is ruled to be the untitled tail. L05 also shipped subtitle opacity `0.7` on two blocks.
4. **The comment had drifted eight formats across 51 instances, and several were lying.** L02's comment read `PART 1: THE CHALLENGE` above a banner reading *Theory & Concepts* — exactly the §6.8a case where L01's fence read `KEY CONCEPTS` against a *Background Theory* banner. A second authoring site for a name will always eventually disagree with it.

All four resolve in ONE generate with no per-instance judgement, which is the §6.8a precedent. What makes it a generate rather than a repair is that **every field is derived**: color, title and subtitle from the PART number, the subtitle variant from whether `section-8a` exists, the seat from the section spine.

**The sweep is defined on the CONSTRUCT, not the lesson.** Two neighbouring constructs had to survive it. L03 carries `End Part 1 content` / `PART 2 build continues` / `End Part 3 content`, which are notes and not dividers. L02 carries its own `<!-- ==== -->` rule-comment idiom bracketing every landmark, which legitimately produces adjacent rule pairs — **10 of them pre-existing**. Absorbing "any rule comment abutting a divider" would have eaten real content in L02, so the sweep matches the divider LABEL only, and the emptied sandwich it leaves is already L02's normal shape. **Check what a cleanup rule would delete in its worst lesson before adopting it.** **Retired S84 batch 2, per DJ ruling:** L03's three notes are gone. The deciding evidence was not tidiness — `End Part 3 content` sat at line 3810 where **PART 4 had begun at 3014 and §10 at 3647**, so it marked the end of PART 3 from 163 lines inside the untitled tail *after* PART 4. It was already lying, which is the same failure this section was rewritten to eliminate: a second authoring site for a boundary eventually disagrees with the spine. The other two were merely redundant, since a generated divider makes every boundary derivable.

**Gated the same session per §24.2** — `book_gates.py` v1.15 **gate 27** regenerates the expectation and compares the whole block byte-for-byte, asserts each block's next fence is its OWN section, rejects any surviving divider-shaped comment, and carries a COVERAGE assert at 64. **Byte-canonicity and placement are asserted INDEPENDENTLY**: the first draft bailed out of the placement check on a byte failure, which would have let an encoding drift hide a misplaced banner — the S83 lesson that a gate must not be satisfied by the bug it should catch. Control-run **six** ways: untouched source FAILED · a re-introduced L13 displacement FAILED naming `PART 3 caps SECTION 6, expected SECTION 7` · L05's subtitle reverted FAILED · a deleted comment FAILED · `&mdash;` restored in L11 FAILED · a whole block removed tripped BOTH the shape and COVERAGE asserts.

**The displacement control PASSED on its first attempt and the injection was at fault, not the gate.** The test had extracted the block by truncating at its first `</div>` — which is the *title* div — so only a fragment was moved, and the `blk in s2` assert passed trivially because a prefix survived. §24.6b's rule is not "assert something changed", it is **assert the injection landed in the shape you intended**, re-parsed and read back.

**Generator:** `gen_part_banners.py` v1.0, repo root. Never `open(path,'w')` on a source file: build bytes, assert, write `.tmp`, `os.replace`.

### 6.8a THE SECTION FENCE IS GENERATED FROM THE ANCHOR SPINE (v8.68 — NEW, S82)

Every core section anchor carries exactly one **fence comment** immediately before its banner wrapper, byte-exact:

```html
<!-- ===================== SECTION 3: BACKGROUND THEORY ===================== -->
```

- **Twenty-one `=` per side**, one space inside each, uppercase `SECTION`.
- **Number** = the anchor's own id (`1`–`10`, plus `8A` wherever `section-8a` exists). L01 and L16 have no `8a` and carry ten; the other fourteen carry eleven. **174 book-wide, one per anchor.**
- **Title is DERIVED, never typed**: the anchor's banner text with entities decoded, the leading icon dropped, the `Section N:` prefix removed, truncated at the em-dash, uppercased. Rewording a banner obliges regenerating its fence.
- The fence is invisible to students and carries no content. It is an editing landmark, and it must never become a second place where a section's name is authored.

**Why it is generated and not maintained.** Until S82 this construct had NO rule, and it drifted five ways across ten lessons: `=====`-wrapped uppercase (L01 at five equals, L09/L10 at twenty-one), bare uppercase (L02), bare Title Case (L04/L06/L08), and mixtures (L03/L05/L07). L11–L16 had none at all. The drift was invisible because `lesson_inventory.py`'s matcher required the `=` wrapper: it saw the fences in three lessons and was **structurally blind in five** — which is why L09's missing §7 fence looked like the only gap in the book when there were **nine gaps across seven lessons**, and why stale duplicates survived in L03 (labelled `(NEW CANONICAL)`) and L08 (`Code Structure` + `Code Walkthrough` stacked before one banner). L01's fence read `KEY CONCEPTS` while its own banner read *Background Theory* — **the title was already lying.**

Per DJ (*"Why widen the fence. Can't we just fix the issues that are causing the fence issues"*) the fix is the book, not the detector; a widened matcher would have ratified all five formats permanently. Because the fence is derived from the spine, normalization is a **GENERATE, not a repair**: every gap, duplicate, mislabel and format variant resolves in one pass with no per-instance judgement, and L08's wrong `Section 7: Troubleshooting` label needed no diagnosis at all.

**Gated the same session per §24.2** — `book_gates.py` v1.12 regenerates the expectation and compares, so number AND title must agree with the anchor, and any near-miss comment fails loudly. Control-run three ways: unfixed source FAILED (79 non-canonical fences + 16 count/title mismatches), a deleted fence FAILED, and a fence left stale after its banner was reworded FAILED. **That last control is what makes it safe to keep a title in the fence at all** (DJ ruling: *"Keep title in it"*).

### 6.9 Standard Section IDs

`#section-1` … `#section-10`, plus `#section-8a` (if present), `#glossary`, `#quick-ref`, `#figures`. Body carries `id="top"`. *(v8.97: was `#image-index`.)*

### 6.10 Back-to-top links

After each section: `<p style="text-align: right;"><a href="#top" style="color: #3498db;">↑ Back to top</a></p>`

### 6.11 Code Blocks — DARK (VS Code / PlatformIO theme) (LOCKED)

Code blocks and ASCII diagrams use a dark theme matching what students see in PlatformIO / VS Code (Dark+). Light code backgrounds are **retired**.

```html
<pre style="background-color: #1e1e1e; border: 1px solid #333; border-radius: 8px; padding: 15px; overflow-x: auto; font-family: 'Courier New', monospace; font-size: 0.9em; color: #e8e8e8;">
<span style="color: #569cd6;">void</span> setup() {       <span style="color: #7cbf6e;">// comment</span>
    display.print(<span style="color: #ce9178;">"Hello"</span>);
}</pre>

**Code-block spacing (LOCKED v8.4):** dark code blocks use **`padding: 15px`**, **`margin: 16px 0`**, and **`line-height: 1.8`** — all consistent across every block in a lesson. 15px is the standard (NOT 10px/20px). **No blank-line doubling:** source-generated code often has an empty line between every line of code (the `BXBXBX` pattern), which renders double-height — STRIP all such blank lines inside `<pre>` so code is single-spaced; the `line-height: 1.8` provides the breathing room instead. If blocks use a wrapper-`<div>` + inner-`<pre margin:0>` structure, set line-height on the inner `<pre>`. No double-semicolons (`;;` is a typo, always strip). §11 check: FAIL if any code block has padding≠15px, line-height≠1.8, or contains blank lines inside `<pre>`.
```

- **Background:** `#1e1e1e` · **border:** `1px solid #333` · **base text:** `#e8e8e8` (near-white).
- **Syntax colors (VS Code Dark+):** keywords `#569cd6` blue · comments `#7cbf6e` green · strings `#ce9178` orange-tan.
- **ASCII diagrams** (motor scales, flowcharts) use the same dark box + `#e8e8e8` text — never light-on-light.
- **Exception:** the Icon Guide/Legend box stays light (`#fff` / `#f8f9fa`) — it is not a code block.
- Inline code chips (within prose) keep their light chip style (`background: #e8e8e8; padding: 2px 6px`).

### 6.12 Challenge Cards (SECTION 9) — CANON (LOCKED)

§9 Challenges use the **carded format** (the "Lesson 9 look"). Each challenge is a bordered plum box with a gradient header, a difficulty pill, and a collapsible solution. Bare `<h3>Challenge N`</h3> headings (old L4/L10 style) are **retired** — convert them to cards.

```html
<div id="challenge-1" style="border: 2px solid #7d5283; border-radius: 10px; margin: 25px 0; overflow: hidden;">
    <div style="background: linear-gradient(135deg, #7d5283, #9b6a9e); color: white; padding: 12px 20px;"><strong>Challenge 1: Title</strong> <span style="display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.8em; margin-left: 10px; background: #4caf50;">EASY</span></div>
    <div style="padding: 15px 20px; background: white;">
        <p>Challenge description…</p>
        <details style="background:white; border:1px solid #ddd; border-radius:8px; margin:15px 0;"><summary style="padding:15px 20px; cursor:pointer; font-weight:bold; color:#1a5276; background:#f8f9fa; border-radius:8px;">🔓 Click to reveal solution</summary>
        <pre style="background-color: #1e1e1e; color: #e8e8e8; ...dark code per §6.11...">…</pre></details>
    </div>
</div>
```

- **Outer box:** `border: 2px solid #7d5283; border-radius: 10px; overflow: hidden`.
- **Header (gradient — a "header element" per §6.2a):** `linear-gradient(135deg, #7d5283, #9b6a9e)`, white text. Matches the §9 plum group.
- **Difficulty pill — SPLIT, TWO AXES (v8.41, see §6.12b).** The pill is one badge divided by a 45° slash into a DOING half (left) and a GRASPING half (right), white text throughout. DOING = five tiers, what the student must physically do: Easy `#4A6B22` · Medium `#9A6B10` · Tough `#B85425` · Hard `#8A2F18` · Advanced `#6B2545`. GRASPING = three tiers, how much the student must understand: Light `#4A7FB5` · Moderate `#185FA5` · Deep `#0C3F6C`. *(v8.41 supersedes the v8.27 single five-tier pill — EASY `#4caf50` · MEDIUM `#2196f3` · TOUGH `#9c27b0` · HARD `#ff9800` · ADVANCED `#f44336` — which conflated the two axes and forced one label to lie whenever they diverged.)* *(v8.27 — scale recolored/relabeled from the old EASY/MEDIUM/HARD/EXPERT/COMPETITION set; the book-wide pill sweep is COMPLETE as of S59 — verified from files: 73 pills, all conforming to this scale, zero retired EXPERT/COMPETITION labels remaining.)*
- **Solution:** `<details>` / `<summary>` "🔓 Click to reveal solution"; the code inside is DARK per §6.11.
- The §9 **cap** stays flat solid plum `#9b6a9e` (it's a section cap, §6.2a); only the card *header* is the gradient.
- Old grape palette (`#7030A0`/`#9B59B6`) is retired → replace with plum (`#7d5283`/`#9b6a9e`).

---

## §6.12b THE SPLIT DIFFICULTY PILL — DOING vs GRASPING (v8.41)

**The rule.** Every challenge carries ONE pill with TWO ratings, cut by a 45° slash:

| Half | Question it answers | Scale |
|---|---|---|
| **Doing** (left, warm) | How much work is the student's hands doing? | Easy · Medium · Tough · Hard · Advanced |
| **Grasping** (right, blue) | How much must the student understand to attempt it? | Light · Moderate · Deep |

**Why two axes.** A single pill has to lie whenever the axes diverge. L03 C08 Auto-TRIM Preview asks
for COMMENTS ONLY — trivial to do — but requires reasoning about encoder differentials three lessons
before encoders exist. Rated ADVANCED it warned students off a card they could finish in ten minutes;
rated EASY it hid the only hard thing about it. Split, it reads Easy / Deep and both are true.

**Canonical colors (white text on every tier):**

- Doing: Easy `#4A6B22` · Medium `#9A6B10` · Tough `#B85425` · Hard `#8A2F18` · Advanced `#6B2545`
- Grasping: Light `#4A7FB5` · Moderate `#185FA5` · Deep `#0C3F6C`

The doing ramp walks one direction around the warm wheel (moss → ochre → rust → burgundy → plum) so
ORDER IS LEGIBLE WITHOUT READING THE WORDS. Grasping stays a single blue family — three stops rank
themselves, and warm-vs-cool is what tells the student the two halves ask different questions. Do NOT
give grasping its own hue set; that collapses the warm/cool split and makes the pill read as eight
competing colors.

**Markup (inline styles only — Canvas-safe):**

```html
<span style="display: inline-flex; align-items: stretch; margin-left: 10px; font-size: 0.8em; border-radius: 999px; overflow: hidden; vertical-align: middle;"><span style="background: #4A6B22; color: #ffffff; padding: 3px 13px 3px 11px;">Easy</span><span style="width: 4px; background: #ffffff; transform: skewX(-20deg); margin: 0 -2px; position: relative; z-index: 2;"></span><span style="background: #4A7FB5; color: #ffffff; padding: 3px 11px 3px 13px;">Light</span></span>
```

The slash is a skewed **4px** white span with **-2px** margins (v8.43, S63 — halved from the original 8px/-4px) — it overlaps both halves so the cut reads. **The negative margin is always HALF the width**; change one and you must change the other, or the halves stop closing over the slash and a gap opens.
as one badge divided, not two pills touching. A straight divider makes it look like two separate pills.

**Rating discipline.**

1. **Doing is about the hands.** Filling two blanks is Easy even when the surrounding concept is hard.
   Writing a function from a pseudocode spec is Medium. Designing the algorithm yourself is Hard/Advanced.
2. **Grasping is about the head — and is measured against WHAT THE LESSON TAUGHT.** A concept covered
   in that lesson's prose is Light no matter how sophisticated it sounds. A concept the student must
   supply themselves, or one the book has not yet taught, is Deep. This makes §6.12b a live instrument
   for §11's "§8A must cover what §9 requires": **a Deep grasping rating on a card whose concept is
   absent from the lesson prose IS a teaching gap**, and must be logged as one.
3. **Observation challenges rate by what they demand, not by their topic.** "Predict, then verify" with
   no code is Easy on doing. Its grasping rating is whatever the insight costs.

**Attributes.** Both axes are machine-readable: `data-difficulty="easy|medium|tough|hard|advanced"`
(doing, name retained so existing tooling does not break) and `data-grasp="light|moderate|deep"`.

**Applied S62:** L01 v03.6.0 · L02 v02.10.0 · L03 v03.10.0 (25 pills). Doing-axis re-rates in the same
pass: L01 C11 MEDIUM→Easy · L02 C06 HARD→Medium · L03 C03 EASY→Medium · L03 C05 MEDIUM→Tough ·
L03 C08 ADVANCED→Easy.

**THE SWEEP IS COMPLETE (S64).** L04–L15 swept: **84 challenges, 15 lessons, zero old pills remaining**
(`pill_sweep.py --audit` reports SWEPT on every lesson). **L16 is exempt** — it uses §6.12's tier-card
variant and has no `data-challenge` cards at all. Every swept card carries BOTH attributes, equal count.

Doing-axis re-rates applied S64: **L05 C01 EASY→Medium** (identical boolean edge-detection to L04 C02,
which was already Medium — two ratings for one concept) · **L14 C02 EASY→Medium** (three lines, but the
whole challenge is a trick question about `while(true)`) · **L10 C03 MEDIUM→Easy** (print a counter; its
hint resolves the only non-obvious part). The single **Tough** in the book (L13 C02) was deliberately
retained pending DJ's own pass, so the tier stays live.

**The two-axis progression as swept** (doing / grasping, lesson means):

| L01 | L02 | L03 | L04 | L05 | L06 | L07 | L08 | L09 | L10 | L11 | L12 | L13 | L14 | L15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.36 / 1.36 | 1.67 / 1.50 | 1.69 / 1.62 | **2.40 / 2.20** | 2.00 / 1.80 | 2.25 / 1.88 | **1.83 / 1.50** | 1.80 / 2.00 | 2.17 / 2.17 | 2.20 / 1.80 | 2.00 / **2.33** | 2.33 / 2.33 | 2.50 / 2.00 | 2.33 / 2.33 | 2.71 / 2.57 |

Floor (L01–L03) and ceiling (L15) are clean on both axes. Two findings for the progression audit:
**L04 spikes to 2.40/2.20** — third-hardest doing in the book, sitting fourth — and **L07 sags to
1.83/1.50**, below L05 and barely above L03, with L08 at 1.80 right behind it. Challenge COUNT also
collapses after L10 (11,6,8,5,5,8,6,5,6,5, then 3,3,3,3, then 7): L11–L14 carry 12 challenges between
them, fewer than L01 alone. L11 in particular pairs the book's **highest grasp mean (2.33)** with its
lowest count — under-practiced, not under-taught.

**TEACHING GAPS FOUND AND FIXED BY THE S64 SWEEP** (§6.12b working as the intended instrument — a Deep
rating on untaught prose IS a gap):

- **L04 §8A.8 NEW** — a `bool` as memory across `loop()` passes: the runaway-counter failure, edge vs.
  presence, why GLOBAL-vs-`loop()` placement is what makes a flag survive, and hysteresis. C02 required it.
- **L04 §8A.9 NEW** — `abs()` and the deadband: `error = position - CENTER` carrying size AND sign, why
  the sign defeats a closeness test, and why `error == 0` makes the robot buzz forever. C05 required it.
- **L06 §5.5 NEW** — the polygon exterior-angle rule (`360 ÷ sides`), including why the square is the one
  shape where interior and exterior agree and therefore taught a rule right in exactly one case. C03 said
  "you must calculate the turn angle" and the rule was taught nowhere.
- **L07 C05 card** — one-line definition of a **stub** (a finished definition with an empty body).
- **L08 `qr-map` NEW** — `map()` appeared exactly ONCE in the whole book, as a fill-in blank in C04, and
  was taught nowhere. Quick Reference row per §11's transcribed-only rule.
- **L09 `qr-dowhile` NEW** — `do…while`, same case: supplied complete in C03's template, taught nowhere.

**STILL OPEN (marked, not fixed):**

- **L03 C05 Variable Speed** — requires ARRAYS and the MODULO operator `%`. Neither appears anywhere in
  L03 prose (verified by grep, S62). Rated Tough / Deep. Needs both an array explainer and the modulo
  explainer already standing in the queue.
- **L15 C04–C07 ship with no template and no solution reveal** — four of the book's hardest challenges
  give a stuck student only prose, and give the AI Tutor nothing to strip. Deliberate capstone shape,
  but logged: C01–C03 are templated with solutions, C04–C07 are open specifications.

### 6.12c INLINE CSS DRIFTS PER REBUILD — MATCH STRUCTURALLY (v8.44 — NEW, S64)

**The finding.** The difficulty pill is one visual component repeated 84 times. Across L04–L15 it carried
**nine distinct style strings** — same rendering, different CSS property ORDER (`padding`-first vs
`background`-first, etc.).

**The cause is structural, not sloppiness.** Canvas strips `<style>` blocks and `class=` attributes (§6),
so there is nowhere for one canonical definition to live. Every card carries its own inline copy, and a
component is never *edited* — it is **retyped wholesale by whichever session rebuilds that lesson's
cards**. Git proves it: L04 and L05 both began `padding`-first on Jul 12; L05 flipped to `background`-first
on Jul 20 in commit `a3cd518` ("5, 12, 13 update" — the S59 Project B pilot), taking L12 and L13 with it in
the same commit. Single-commit, lesson-clustered changes are a **rebuild signature**. The variants are
STRATA, each carrying the hand of the session that last touched it.

**The rules that follow:**

1. **Never conclude "the markup is uniform" from a subset.** S63 found L01–L03 uniform and recorded
   "markup was uniform, zero variants" — true, because those three were swept together in S62 and share
   one stratum. Uniformity *within* a stratum says nothing about the book.
2. **An exact-string find-and-replace on an inline component is invalid book-wide.** It will silently
   match nothing on every lesson outside the stratum it was written against and report success.
3. **Match by STRUCTURE** — the element type plus a stable signature (e.g. a `<span>` whose style contains
   `display: inline-block` and `border-radius: 12px`, whose text is a known tier label) — never by the
   full style string.
4. **Scope the replace to ONE challenge block, not the file.** Two challenges at the same tier produce
   BYTE-IDENTICAL pills (L04 C02/C03 are both MEDIUM), so a file-wide `count == 1` assert fires falsely.
   Locate the block by `id="challenge-N"`, replace within it, assert `== 1` **inside the block**.
5. **Grep code constructs with tags stripped.** Syntax highlighting splits a construct across `<span>`s:
   `while(true)` reads as `while</span> (<span…>true` in raw HTML and a naive grep returns ZERO for a
   construct used 11 times (S64, L06). Normalize tags out before matching, then verify hits are prose and
   not code. This is the §11 false-positive rule run in the opposite direction — a false NEGATIVE.

**Tool.** `pill_sweep.py` (repo root, v1.0) implements all of the above. `--audit` is read-only and reports
per-lesson `SWEPT` / `not swept` / `*** MIXED ***` plus the count of distinct style strings still live; a
half-applied sweep cannot pass silently. Control-run it against untouched source before trusting it on
edited source (§11).

**§9 TIER-CARD VARIANT (added v8.5):** §9 need NOT always be Easy/Medium/Hard challenge cards. Where the content is **project tiers** rather than escalating challenges (e.g., L16 Nothing Left to Take Away), §9 uses **tier-cards**: white card, `box-shadow`, `border-radius: 8px`, with a **medal-colored top border** — Bronze `border-top: 5px solid #cd7f32`, Silver `#c0c0c0`, Gold `#ffd700`. This is a legitimate alternative §9 format, chosen per-lesson by the author; challenge cards remain the default.

### 6.12a THE THREE-PANEL CARD + WHEN IT APPLIES — CANON (Project B, v8.38)

Book-wide consistency = **uniform shell, inner format fits the challenge type.** The §6.12 card skin is the mandatory SHELL on every challenge in every lesson; what goes *inside* depends on the challenge.

**THE SHELL — mandatory on every card:**
- Outer plum box + gradient header (§6.12) with `Challenge N: Title` — **sequential N, never §-based** ("Challenge 9.1" is retired; renumber to "Challenge 1" and repoint any cross-refs).
- Difficulty pill (§6.12 five-tier). Where a lesson's challenges carry no rating, **infer and label "Inferred:"**; DJ adjusts.
- A pale-yellow **Work-in bar**: `<div style="padding: 12px 20px; border-bottom: 1px solid #eee; background: #fffbe6;">` holding 📁 **Work in** (the Maker starter link, or just the build name where no starter payload exists) and 🔍 **Where to look** (omit this line when the lesson has no Quick Reference to anchor).
- A flush **solution**: `<details data-reveal="solution" style="margin: 0; border: none; padding: 15px 20px;">` (§20.1 typing is mandatory).
- **Never:** a white body wrapper, a separate 💡 hint box, or a 📝 Plan-first line.

**THE INNER FORMAT — decided per challenge; a lesson MAY mix:**
- **Algorithmic** (write/modify a function or behavior) → the **three tiled panels**, each `<div style="padding: 15px 20px; border-bottom: 1px solid #eee; background: …;"><h4 style="margin-top: 0;">…</h4>…</div>`:
  - 🎯 **THE GOAL** — gray `#f8f9fa`. One–two sentences: what the finished thing does.
  - 🧠 **THE LOGIC (Pseudocode)** — purple `#f3e5f5`, dark `<pre>`. The plan in plain-English steps; **it absorbs the hint's thinking — there is no separate hint box.**
  - 🧩 **THE TEMPLATE** — green `#e8f5e9`, dark `<pre>` with `____` blanks on the concept taught. **The filled-in blanks MUST reproduce the solution exactly** (verify every blank).
  - Reference: **L06 / L07**.
- **Guided-edit / debug / observation / open-creative** (change a number, delete lines, measure, write your own) → **prose inside the card, no panels.** There is no algorithm to pseudocode and no function to scaffold; forcing panels degrades the card. Reference: **L01 (left as-is).** The shell still applies.

**OPEN-CASE RESOLUTIONS (provisional — DJ finalizes after a student runthrough):**
- **Withhold-solution lessons (L08/L09):** show the Template **and** the solution for now; the withhold decision is parked to the runthrough.
- **YOUR-NUMBER lessons (L12–L15):** the solution is shown on purpose with a tuning constant blank (`const int X = 0;   // <-- YOUR NUMBER`). Use a **two-level scaffold** — the Template blanks the *concept*; the Solution reveals the full code with only the YOUR-NUMBER blank remaining.
- **Maker link is a solved build, not a starter (L11/L12/L13):** a "make this folder" starter link goes in the Work-in bar; an "open the solved build" link stays inside the Solution. Where a lesson has no starter payload, the Work-in bar names the build only and a Maker-starter task is logged.
- **Solution code comments referencing a challenge number** (`// CHALLENGE 9.x`) stay unchanged when renumbering the visible heading — they byte-match the Maker payloads (payload gate), so syncing them is a coordinated lesson+Maker edit.

**STATUS:** L05 (pilot), L12, L13 converted S59; L06/L07 already conform; rollout continues lesson-by-lesson.

---


### 6.13 BRACE STYLE — K&R IS HOUSE STYLE; THE GUARD CLAUSE IS ALLOWED (v8.45 — NEW, S65)

**The book is K&R** — opening brace on the same line as the thing it opens. Measured S65 across every
`<pre>` in all 16 lessons: **837 K&R vs 2 Allman**. It was already consistent; this records it as a rule so
it stays that way. Allman is taught in L02 §3.1 as the alternative that exists, with the point that neither
compiles differently and the only real sin is mixing them inside one file.

**Braces are the default. A braceless one-liner is allowed only when the entire statement fits on the same
line as the `if`** — a guard clause:

```
if (killSwitchPressed()) break;
```

**The book does NOT adopt the common "never omit braces" rule, and this was a deliberate S65 ruling.** The
book contains **93 braceless guards** across L04–L16 — `if (killSwitchPressed()) break;`, `if (scaled > 99)
scaled = 99;`, and the aligned `else if` ladders in L09/L13/L15 that are readable *because* they are
braceless (bracing L09's three-line intersection ladder makes it fifteen lines and hides the state machine).
All 93 are single-statement, non-nested guards: no dangling-else hazard, no `goto fail` shape. Adopting the
absolute rule would have made the book violate its own canon in 93 places, and students who noticed would
trust it less.

**What the book teaches instead** (L02 §3.1, ⚠️ WARNING box): the danger is real and it is what happens
*next*. Adding a second line to a braceless `if` silently escapes it — the indentation lies, the compiler is
satisfied, the build is clean, and the robot misbehaves. So: **the moment you want a second line, add the
braces first, before you type it.**

**One live caveat:** "always brace" is the machine-checkable rule. If a linter or `clang-format` is ever added
to the student toolchain, these 93 sites become real work. That is the only scenario in which this ruling
costs anything.

## 7. EXIT TICKET (SECTION 10) — LOCKED

Three `<h4>` subsections, each wrapped in a specific callout:

1. **"Technical Skills: Can you...?"** — Checkpoint callout (`#e8f5e9` bg / `#4caf50` border). **☐ checkbox items only — NO list bullet** (see §11 checkbox-XOR-bullet rule).
2. **"Conceptual Understanding: Do you know...?"** — Coach's Tip callout (`#f0f7f0` bg / `#6b8e6b` border). **Bold question + italic `Answer:` line** beneath each (the L9 format), numbered.
3. **"Problem-Solving: Can you modify or extend...?"** — Learn/Insight callout (`#e3f2fd` bg / `#2196f3` border). **☐ checkbox items only — NO list bullet.**

(Optional follow-ons used in some lessons: a confidence self-assessment table and a "What's Next" preview. Quiz feature deferred.)

**Orphan intro-banner ban:** the blue "ASSESSMENT — Check Your Understanding", "CHALLENGES — Test Your Skills", "TESTING — Verify Everything Works" announce-banners are **retired** — they add no information and break the cap/box rhythm. Do not insert any "<LABEL> — <tagline>" banner at the top of a section; the section CAP already labels it.

---

## 8. CALLOUT STANDARD v1.0 — LOCKED

**All callouts use inline `style=` only.** `<strong>` for titles (never a CSS class). 11 standard types (the count was **9** above a list of 10 rows until S95, when Learn / Insight split into 7 and 7a):

| # | Type | Icon | Background | Border |
|---|---|---|---|---|
| 1 | Coach's Tip | 💡 | `#f0f7f0` | `#6b8e6b` |
| 2 | Coach's Note / Warning | ⚠️ | `#fff8e1` | `#ffc107` |
| 3 | What You Should See | 👀 | `#d1ecf1` | `#17a2b8` |
| 4 | Do This Now | 📝 | `#ffe4cc` | `#ff8c00` |
| 5 | Checkpoint | ✅ | `#e8f5e9` | `#4caf50` |
| 6 | Key Term | 🔑 | `#f3e5f5` | `#9c27b0` |
| 7 | Learn | 📖 | `#e3f2fd` | `#2196f3` |
| 7a | Insight | 🔍 | `#e9f7f5` | `#2da99d` |
| 8 | Next Lesson | 🔮 / 🚀 | `#e8d4c4` | `#d4a574` |
| 9 | Challenge | 🎯 | `#e8f3ec` | `#3a7d5c` |
| 10 | Brain Check | BrainGear img | `#e8eaf6` | `#3f51b5` |

**Type 10 icon is an IMAGE, not an emoji** — `images/BrainGear_Incomplete.png` (gray) / `images/BrainGear_Complete.png` (green ✓), inline at ~1.35em. See §25.10 for the full Brain Check canon (state behavior, column, naming).

**Mini-Challenge / Bonus-Challenge blocks are retired** — replace any with the 🎯 Challenge callout (type 9).

**Canonical template (types 1–4, 6–9 — border-left accent style):**

```html
<div style="background-color: {BG}; border-left: 4px solid {BORDER}; padding: 15px 20px; margin: 20px 0; border-radius: 4px;">
    <strong style="color: {TITLE};">{ICON} {Title}</strong>
    <p>Body text.</p>
</div>
```

**Title colors per type** (extracted from L09 v03.0.3 reference lesson; type 9 set by DJ decision, Session 10):

| # | Type | Title color |
|---|---|---|
| 1 | Coach's Tip | `#3a5a3a` |
| 2 | Coach's Note / Warning | `#856404` |
| 3 | What You Should See | `#0c5460` |
| 4 | Do This Now | `#c45a00` |
| 5 | Checkpoint | `#2e7d32` |
| 6 | Key Term | `#6a1b9a` |
| 7 | Learn | `#0d47a1` |
| 7a | Insight | `#165a53` |
| 8 | Next Lesson | `#8a5a2b` |
| 9 | Challenge | `#2a5a42` |
| 10 | Brain Check | `#283593` |

**Type 5 Checkpoint has TWO canon forms** (both live in L09):
1. Standard border-left callout — bg `#e8f5e9`, border-left 4px `#4caf50`, title `#2e7d32` (template above).
2. Centered milestone banner — `background: linear-gradient(to right, #e8f5e9, #c8e6c9, #e8f5e9); border: 2px solid #4caf50; border-radius: 10px; padding: 15px 20px; margin: 30px 0 20px 0; text-align: center;`

**Type-9 label canon:** label text is `🎯 CHALLENGE` (optionally with a time/difficulty qualifier in parentheses, e.g. `🎯 CHALLENGE (1 minute)`). "MINI-CHALLENGE" and "BONUS CHALLENGE" label texts are retired along with the blocks.

**`ZUMO_Callout_Standard_v1.md` is RETIRED** — templates folded in here as of v8.8. Do not request or reference the standalone file.

**Code-block syntax coloring — LOCKED (S12, DJ-approved):** All `<pre>` code blocks: dark bg `#1e1e1e`, base text `#e8e8e8`, color-only inline `<span>` highlighting (NEVER background chips — chip-in-pre renders text invisible). Palette (VS Code dark approximation): comments `#6a9955` · keywords `#569cd6` · preprocessor `#c586c0` · types/classes (`Zumo32U4*`, `Serial`) `#4ec9b6` · strings `#ce9178` · numbers `#b5cea8` · ini keys `#e06c75` · ini section headers `#d7ba7d` · in-code section banners `#6a9955`. Apply by script with a per-block stripped-text-identity assertion (colored output must strip back to byte-identical code). Book-wide application pass: L01–L02 COMPLETE; L03–L15 queued (apply during each depth pass).

**Details/summary readability rule (added v8.10, from the L02 white-summary defect):** every `<summary>` sits on a light background (`#f8f9fa` details box), so its text color MUST be readable there — canon colors: `#5a6872` for standard troubleshooting/hint details, `#2a5a42` when the details block lives inside a challenge callout (matches the 🎯 CHALLENGE title color). `color: white` (or any low-contrast color) on a summary is a build error. Gate check (mandatory): fail the build if any `<summary` style contains `color: white`. Background: L02 shipped three invisible "🔓 Stuck? / Answer / Click for solution" summaries; scan confirmed the defect was L02-only — this rule exists to prevent reintroduction during the L03–L15 depth passes, which reuse the L02 hint/solution pattern.

---

## 9. VERSIONING — LOCKED

**§5b ADDENDUM (v8.44, S64 — SUPERSEDED, recorded for provenance).** This addendum required the visible
`major.minor` banner to appear **TWICE**, header and footer, and its audit demanded `grep` return **exactly
2 identical** matches. It was superseded at **v8.53** (the footer number moved into a hidden comment) and
again at **v8.77** (that comment deleted). **It nonetheless sat here contradicting §5b for 19 sessions**,
because superseding a rule in one section does not delete its restatement in another.

**CURRENT RULE — ONE VISIBLE BANNER.** The header hero carries `major.minor`; the line-1 HTML comment
carries the full three digits; nothing else carries a version. The audit is:

- **Strip HTML comments first**, then `grep -o "Version [0-9][0-9]\.[0-9]*"` must return **exactly 1**.
- That one match must equal the line-1 comment's major.minor.
- Gated across all 17 pages by `book_gates.py` v1.21 with a coverage assert.
- **Derive the version from the hidden comment when writing a banner**, never hand-type it, so the two
  homes cannot disagree at birth. `going_deeper.html` shipped a visible `01.0` against a hidden `01.1.0`
  for exactly this reason and was corrected at S89.
- **Footer style is itself stratified** (same §6.12c effect): L01–L11 use a plain `<p>`/`<footer>` block;
  L10 and L13–L16 use a gradient banner div. When restoring a missing footer, **match that file's
  neighbours** — do not invent a third format. The footer carries credits, never a version.

**A RULE RESTATED IN TWO SECTIONS IS TWO RULES.** When one is superseded, grep the Bible for the other.

- Scheme (all projects): major = `v#`, moderate = `v#.#`, minor = `v#.#.#`. **No letter suffixes.**
- Filenames use zero-padded lowercase form: `v01`, `v02`, …
- **UNIQUE VERSION PER DELIVERY (v8.20 — DJ ruling, S33).** Once a build has been presented for download, **any** further change — code, prose, or image — bumps the version. Two files with the same name NEVER have different contents. *This RETIRES the old "a fix to an already-fixed version keeps its number" rule, which in S33 produced two different `Lesson_10_Obstacles_v02_1_1.html` files and sent the wrong one to GitHub.*
- **IMAGE CHANGES ARE A MINOR BUMP (v8.20 — DJ ruling, S33).** Inserting art, removing a figure, renumbering a placeholder, or editing a caption or the Image Index is a minor correction → third digit (`v04.0.3` → `v04.0.4`).
- **Reopening a lesson:** read the current v# from the uploaded `.html` filename — do not hardcode a target.
- **v8 re-baseline exception (one-time):** every lesson resets to `v01` at the v8 transition. Normal bump rule resumes afterward.

---

## 10. IMAGE PLACEHOLDERS

Keep `[IMAGE X.Y]` format (X = lesson number, Y = image number). Image Index must list exactly what appears in the body — **no phantoms, no omissions** (S33 found L02 listing a `[GRAPHIC 2.3]` that exists nowhere).

**IMAGE and GRAPHIC ARE SEPARATE NUMBER SPACES (v8.20 — canon, S33).** `L01_IMAGE_1-13` and `L01_GRAPHIC_1-13` coexist by design; the prefix disambiguates. `[IMAGE 2.8]` and `[GRAPHIC 2.8]` in the same lesson is **not** a collision and must not be "fixed."

**AUDIT ART AGAINST `images/`, NEVER AGAINST THE LESSON ALONE (v8.20 — canon, S33).** Before declaring anything about art, clone the repo and compare three sets: (1) assets in `images/`, (2) `<img src>` in the lesson, (3) dashed placeholders. S33 found **nine built assets that no lesson referenced** — including all three L16 SVGs, which shipped with the lesson showing zero figures. GATE CHECK per lesson: every repo asset is referenced; every `<img>` resolves; every placeholder has no file.

**IMAGE `src` = PAGES DOMAIN, NEVER raw.githubusercontent (v8.33 — canon, S49).** Every `<img src>` in a lesson points at `https://weymuth.github.io/zumo/images/<file>` — NOT `https://raw.githubusercontent.com/Weymuth/zumo/main/images/<file>`. Raw is rate-limited by GitHub and is not a page-asset host: under raw, a lesson that loads many images gets HTTP 429 on a random few per page-load, so different figures blank out on different loads (S49 symptom: L04 4.1/4.2/4.3 intermittently missing). Pages is same-origin, unthrottled, correct MIME. Also required because lessons render inside Canvas, which needs an absolute URL. NON-image repo files (e.g. `ZUMO_Template.zip` download links) may stay on raw — the rule is scoped to the `/images/` path only. S49 converted all 114 image refs book-wide.

- `[IMAGE x.y]` = DJ-sourced photo/screenshot. `[GRAPHIC x.y]` = Claude-authored SVG.
- Placeholder → figure conversion is a **minor bump** (§9).
- **Strip EXIF/GPS from DJ photos before pushing (S49).** iPhone photos carry GPS + device metadata; run them through a re-save that drops EXIF before they go to the public repo.
- A GRAPHIC may temporarily stand in for an un-shot IMAGE (S49: L11 5-sensor diagram filled L04 4.1); caption it as temporary and swap to the real photo filename when shot.

---

## 11. PER-LESSON QUALITY CHECKLIST (run before presenting any lesson)

- [ ] **BLANKS ARE SPENT (v8.17):** every tunable declared as a student blank (`const int X = 0;   // <-- YOUR NUMBER`) is actually READ by the code. Grep: a constant that is declared and never used is a lie in the worksheet. Blanks ship as `= 0` with the starting guess in the COMMENT, never as a seeded value.
- [ ] **ZERO BYTE DELTA IS NOT PROOF OF NOTHING (v8.17):** if a state's binary size is unchanged after an edit, ask whether the edit changed a CONSTANT (byte-identical by construction — fine) or added LOGIC (then `--gc-sections` may be discarding it — investigate). Disassemble with `avr-objdump -d` and read the immediates before concluding a fix vanished.
- [ ] **SABOTAGED BUILDS SHOW THE PLANTED LINE (v8.17):** every Bonus mystery displays its sabotaged code in the hint. The question is "why does this cause that symptom," not "find the typo." (Also satisfies the payload gate by construction.)

- [ ] Filename: `Lesson_##_Topic_v##.html` (padded number, lowercase padded version, approved topic token)
- [ ] Body uses Segoe UI + `#fafafa` + `id="top"`
- [ ] Nav + title use top-down dark-first blue gradient
- [ ] Title h1 = `LESSON ##` with NO leading icon
- [ ] Every section is a CAP + BOX: colored cap (white title, keeps icon) on matching bordered box (§6.5)
- [ ] Cap/box + PART banner colors follow nav scheme: §1–3 blue `#3498db`, §4–6 green `#3a7d5c`, §7/§8/§8A rose `#c45d76`, **§9 plum `#9b6a9e`**, §10+end gray `#6c757d`
- [ ] PART banners are SOLID group colors (navy gradient retired); 4 banners (PART 1–4); PART 3 subtitle "Sections 7–8A: Verify and extend" (or 7–8 if no 8A); PART 4 subtitle "Section 9: Apply what you have learned"
- [ ] Sub-headings h3/h4 use the SECTION GROUP COLOR (not global blue/green); table headers use the darker section shade (§6.5). Callout-internal headings exempt. (See the dedicated NEW check below.)
- [ ] Code blocks + ASCII diagrams are DARK (`#1e1e1e` bg, `#e8e8e8` text; keywords `#569cd6`, comments `#7cbf6e`, strings `#ce9178`); no light-on-light; Icon Guide stays light (§6.11)
- [ ] **PROSE IS NOT CODE — never wrap challenge Goal/prose in a dark `#1e1e1e` block (v8.33 — S49).** Dark `#1e1e1e` is for `<pre>` CODE and reveal blocks ONLY. L03 was the one lesson of 16 that dressed its challenge Goal prose in a dark block; inline `#e8e8e8` code-chips and light callouts nested inside it then rendered light-on-light (invisible). Goal/task prose sits on the WHITE card body like every other lesson. Contrast gate: no light-background element (chip, callout) may sit inside a dark block without an explicit dark text color; run a luminance check, not just a string match.
- [ ] All box/callout corners fully rounded (no one-side-rounded `0 8px 8px 0`)
- [ ] Icon legend has all 12 icons ("WARNING")
- [ ] 10 sections present; 8A only if the lesson has a reusable coding pattern (present: L6–L12; absent: L1, L13–L15; verify L2–L5), placed between 8 and 9
- [ ] End-matter caps use icon set: 📖 Glossary / ⚡ Quick Reference / 🖼️ Image Index
- [ ] **Glossary entries use the canon term-card format** (`#e7d4ff` bg / `#9b59b6` border / `8px`); no stray glossary purples (`#f3e5f5`, `#f3e8f9`, `#7b2d8e`, `#9c27b0`) in the glossary region.
- [ ] Section IDs in clean order: 1,2,3,4,5,6,7,8,8a,9,10,glossary,quick-ref,figures
- [ ] Nav anchors all UNIQUE and all resolve; "Back to top" + cross-refs resolve
- [ ] Cap `id` matches visible "Section N" label + nav anchor
- [ ] Exit Ticket = 3-h4 with correct callout colors
- [ ] Callouts inline-only; 0 `<style>` blocks; 0 callout classes
- [ ] Image Index matches body placeholders exactly
- [ ] div tags balanced; version string in title block AND footer matches filename
- [ ] **NBSP/whitespace stripped:** 0 standalone `\xa0` lines (export artifact); no runs of 3+ blank lines. (Pre-overhaul lessons ship with 140–390 of these; each renders as an empty vertical-space line.)
- [ ] **Bare-element sweep (after removing any `<style>` block):** 0 bare `<table>` (every table has `width: 100%`); 0 bare stage-marker divs in old navy `#2c3e50` — recolor to `#2e86ab`. Old stylesheets styled these globally; once inline-only, bare elements lose styling silently and pass div/anchor checks while rendering wrong (narrow tables → horizontal gaps).
- [ ] **No retired navy:** 0 occurrences of `#2c3e50` or `#1a1a2e` anywhere (markers, title, banners).
- [ ] **div-depth walk (not just balance):** every PART banner sits at div-depth 0 (outside all section boxes). Balance can pass while a banner is trapped inside the prior box; verify depth, not just open==close counts.
- [ ] **Dark-wrapper scope check (v8.14.1, from the S21 L03 find):** every dark code wrapper (`background-color: #1e1e1e` div) must close before the next `<h3>`/`<h4>`. Walk each dark div to its matching closer; if the enclosed span contains ANY heading, FAIL. Balance and the depth walk both pass when the closer merely sits too late (L03 v03.0.0: the Safe-Run wrapper's closer landed after four QR tables — code chips rendered as blank pills, shaded rows light-on-light). Measure banner/section depth at the rendered DIV, not at region comments (comments legitimately sit inside closing wrappers).
- [ ] **In-code highlight spans preserved + dark-readable:** pre-existing "new code"/diff highlight spans (e.g. light-green `#90EE90`) are kept (carry pedagogical meaning) but recolored for the dark code background (e.g. bg `#2d5a2d`, text `#b8f0b8`) — never light-text-on-light-fill, never stripped.
- [ ] **Callout radius two-tier:** inline content callouts (border-left accent notes) = `4px`; glossary/term cards = `8px`; structural containers (full-border frames, image placeholders, PART banners, title) = `8px`. No one-side rounding (`0 8px 8px 0`) on callouts — that style is retired. (Code blocks `6px`, nav buttons/pills `4–5px`, inline code chips `4px` separate and unchanged. Cap/box pair is the one intentional one-side-rounded exception.)
- [ ] **4-PART structure (NEW):** PART 1 §1–3 blue · PART 2 §4–6 green · PART 3 §7–8A dusty rose ("Verify and extend") · **PART 4 §9 plum** ("Apply what you have learned"). Four banners, not three. §10 + end = untitled gray tail. PART 4 plum banner present before §9.
- [ ] **§9 plum (NEW):** §9 cap, nav button, and PART 4 banner all use plum `#9b6a9e` (cap/banner/button flat solid). §7/§8/§8A stay dusty rose `#c45d76`. No `#c45d76` on §9 elements; no plum on §7/§8/§8A.
- [ ] **Payload byte-match gate (v8.14, canonized from S18 approval):** every Maker `PAYLOADS[lesson][key]` byte-matches its lesson-source code block at EVERY lesson save (payloads exclude the generator-stamped header + `#include` — mainCpp = head + body). A lesson edit that touches any `<pre>` wired into the Maker requires re-verifying its payloads before either file ships.
- [ ] **Payload-gate INHERITANCE RULE (v8.15, DJ-approved S22):** lesson N's canonical payload corpus = its own decoded `<pre>` bodies + the Maker's template strings **+ lesson N−1's `finished` payload bodies**. Rationale: from L08 onward, Step 1 of every §6 is "copy your Lesson N−1 project" — the eight files arrive wholesale, and the lesson only shows the blocks it CHANGES. Files carried unchanged are therefore canonical by construction, and demanding they re-appear in lesson N's pres would force pointless duplication of a whole project into the lesson body. The rule stays byte-strict in the direction that matters: any content lesson N *modifies* must still appear verbatim in lesson N's own pres. Implementation note: `finished` may be a plain string (L02/L03) or a multi-file dict (L07+) — handle both. Battery must PASS L02 through the newest lesson at every Maker save; zero regressions is the bar.
- [ ] **IF IT IS IN THE PAYLOAD, IT GOES IN THE BOOK (v8.35 — LOCKED, S56).** An unmatched gate line is a **gap in the book**, not a gate defect. The first move is always to add the content to the lesson — never to exempt the line. **Executable code is NEVER exempt under any framing.** S55 burned four takes proposing to exempt L01's failures as "comment-only scaffolding"; 132 of them were an EEPROM name-reader that appeared in no lesson, and C01 Part 5 asked students to use it. Test to apply: *would a student need to read this line to do the work?* If yes, it belongs in the book. Corollary — when a shared listing serves N challenges, put the ONE common body in §9 and let each card quote its OWN target line verbatim; that satisfies the gate without duplicating the listing N times.
- [ ] **BOXED INSTRUCTION HEADERS ARE ADVISORY BUT FINGERPRINTED (v8.35 — LOCKED, S56).** A challenge file's boxed header (`// ┌─┐ … // └─┘`) is the student's working instructions, deliberately kept IN the file so a student coding in one window never has to switch to the book mid-step (DJ ruling S56: "lots of file skipping back and forth" — a step you remove is a step they will actually do). The book's §9 card carries the same instructions as prose, which is the better form for reading, plus the exact target line quoted verbatim. A boxed-header line that does not byte-match is therefore a FORMAT difference, not missing content, and does not fail the gate — it is reported under **ADVISORY**. **But advisory means "not required to appear in the book," NEVER "unchecked":** gate v1.6 pins every boxed header with a line count + md5 in `BOXED_FP`, so an edited header FAILS loudly. Without the pin, v1.5 let a tampered instruction block pass silently (verified). To change a header on purpose: edit it, run `--update-fp`, paste the new manifest — the bump is deliberate, and drift is impossible.
- [ ] **READ THE CENSUS, NOT THE RAW COUNT (v8.35, S56).** The gate's CATEGORY CENSUS (boxed comments / `<<<` markers / other comments / **EXECUTABLE CODE**) is the number that decides severity. `EXECUTABLE CODE: 0` with a large advisory count is a healthy lesson; `FAIL (148)` that is 132 executable is a broken one. Never conclude from a truncated fail list — that error cost S55 three takes.
- [ ] **Bounded-scope replace assert (v8.14):** every wholesale/regex replace must assert its span endpoints sit inside ONE card/step/section — `count==1` alone is insufficient (a greedy `.*?` can span two cards and pass the count check; S20 destroyed L03 Bonus-1+2 this way before donor recovery). Prefer exact-string `str.replace` with `count==1`; when a regex is unavoidable, print and eyeball the matched span before applying.
- [ ] **Challenge-card canon (§6.12):** every §9 challenge is a carded box (border `#7d5283`, header gradient `135deg #7d5283→#9b6a9e`, difficulty pill, `<details>` dark solution). No bare `<h3>Challenge N`</h3>. Old grape `#7030A0`/`#9B59B6` retired.
- [ ] **Checkbox-XOR-bullet (GATE, global):** FAIL the lesson if ANY `☐` appears inside a list whose `<ul>`/`<ol>` does not carry `list-style: none`. Detection must scan EVERY `<ul>`/`<ol>` regardless of its attributes (a styled `<ul style="margin:0; padding-left:20px">` containing `☐` is a FAIL just like a bare `<ul>`) — a narrow "bare-`<ul>` only" check misses styled variants. Fix = inject `list-style: none; padding-left: 0;` into that list's style. No list item EVER shows both a bullet and a `☐`. Applies to ALL sections, not just Exit Ticket.
- [ ] **No orphan intro-banners:** 0 "ASSESSMENT / CHALLENGES / TESTING — <tagline>" announce-banners at the top of any section (the cap labels the section; §7).
- [ ] **No section-marker pills (§6.7 retired):** 0 "READING / CODE / BUILD / TEST — <tagline>" `#2e86ab` pills anywhere. The cap is the only section label.
- [ ] **Subheadings + table headers = SECTION color (NEW):** h3/h4 subheadings use the section group color (§1–3 blue, §4–6 green, §7/8/8A rose, §9 plum, §10+end gray); table headers use the DARKER shade of that color (§6.5 table). No global `#2e86ab` h3 or `#1a5276` table header outside §1–3. Callout-internal headings exempt. h3 must NOT be near-black bold.
- [ ] **Gradient-vs-solid by role (§6.2a):** nav/title/challenge-header/milestone-header = gradient; caps/PART banners/nav buttons/pills = solid. No solid challenge headers, no gradient caps.
- [ ] **PART 3 title token:** "PART 3 — Testing & Challenges" (not "Test & Challenges").
- [ ] **Empty-section-box check (added v8.11, from the L02 Glossary/Quick-Ref/Image-Index defect):** every section banner’s bordered body box must actually CONTAIN its section’s content. A box that opens and immediately closes (regex: `border-top: none;[^>]*>\s*</div>`) is a build FAILURE — div-balance alone cannot catch it (L02 ≤ v02.0.18 passed balance while all three end-section bodies sat outside their boxes). Where `<!-- end X wrapper -->` markers exist, the box’s closing `</div>` must sit immediately before the marker.
- [ ] **Depth-pass items (v8.12, for any lesson given the L02 treatment):** syntax coloring per §8 palette (identity-asserted) · challenge timers wired (`timer.html` iframes) · "📁 Work in:" destination lines on every challenge · Maker challenge registry extended in `newproject.html` · §4 Start-a-New-Lesson ritual block present · ALL code compile-verified on the AVR harness · white-summary + empty-box scans clean.
- [ ] **§8A MUST COVER WHAT §9 REQUIRES (v8.36.1, S57).** Every language construct a lesson's §9 challenges ask students to WRITE must be taught in that same lesson — §8A is where it goes, in the words of L04's own §8A intro: *"the challenges in Section 9 use it immediately; this section makes sure you own it first."* Using a construct inside the lesson's given code is not teaching it. GATE: list every construct appearing in a lesson's §9 hints and reveal-solutions, and confirm each has a tutorial at or before that lesson. Canonized after L04 C03/C04 required `for` loops that L04 shipped in its own build (8 uses) and narrated in one sentence, while the formal tutorial sat in L05 §5.15 presenting first contact. FIX PATTERN: teach it at FIRST CONTACT, and demote the later lesson's tutorial to the §18.1 spiral second rung (mark it 🔁 Builds on: with the source-lesson star) carrying only what is genuinely new there — never two first contacts.
- [ ] **A "THE BOOK HAS NEVER…" CLAIM IS A DEPENDENCY, NOT PROSE (v8.36, S57).** Any sentence asserting what the book has never done, not yet used, or will meet for the first time is a claim about all sixteen lessons, and it goes stale the moment another lesson changes. Grep the whole `lessons/` tree for the feature before trusting such a line, and re-grep whenever new content introduces one. Canonized after S56 published an EEPROM name-reader in L01 §9, which silently falsified L16 §4.3's "this book has never touched it" — a defect created by a correct fix in a different lesson. Same class as a false claim about code (§11 grep-the-code rule): the lesson said one thing, the book did another.
- [ ] **AUDIT FALSE-POSITIVE DISCIPLINE — A REGEX REPORTS CANDIDATES, NOT VERDICTS (v8.36.2, S58).** A prose-keyword grep produces LEADS, never findings — every hit is verified against rendered text before it drives an edit. (1) SEPARATE CODE FROM PROSE BEFORE COUNTING: strip to `<pre>` bodies to test whether a construct is USED; strip all tags to test whether it is TAUGHT; never count a token that spans both (`abs(` inside a `while` condition is a use, not a lesson). (2) A KEYWORD NEAR A HEADING IS A LEAD, NOT PROOF: for any "is X taught?" question, surface the candidate heading and read it — the regex narrows the field, only the read closes it. (3) VERIFY AGAINST RENDERED TEXT BEFORE ACTING: S57's phantoms all evaporated on a read — `milliseconds` matched as `millis`, a stray `?:` in prose as the ternary, a changelog `v04.6.0` as a version mismatch. Same family as S56's unescaped-`<` false alarm and the L04 image-index phantom. A smarter script sharpens the lead; a human read is the only verdict.
- [ ] **Dedicated ASCII sweep (v8.13.1)** on every depth pass, even for lessons marked "converted": scan all `<pre>` bodies for box-drawing/arrow characters (┌ ┐ └ ┘ │ ─ ◄ ► ▶). Established by the L03 half-conversion find (Session 15): S6 built the SVGs and the tracker showed ✅, but the lesson file was never edited — four ASCII diagrams survived to Session 15.

---

## 11b. PRE-OVERHAUL LESSON PROFILES (audit FIRST to identify which)

Lessons authored before the v8 overhaul come in **two profiles**. The audit step (grep for `<style`, count `class=`, count `\xa0`) identifies which, and that drives the build:

- **Class-based (e.g. L6):** has a `<style>` block + CSS classes + nbsp. Requires **class→inline mapping (approach B):** map every class straight to its v8 inline equivalent (callouts → Callout Standard v1 colors, nav → color-coded buttons, part-divider → solid banner, section-marker → `#2e86ab` marker), then the normal design pass. Also carries the bare-`<table>` / nbsp problems.
- **Inline-but-stale (e.g. L7, L8):** no `<style>` block (already inline), but ships with nbsp clutter, bare/under-styled tables, navy `#2c3e50` markers, **and section-numbering deviations** (missing "Code" §5, off-by-one Test/Troubleshoot/Challenges/Exit, 8A out of DOM order, mislabeled Exit, missing PART 3 banner, missing Image Index). Fix structure first, then design pass.

Either profile may need a structural §5 "Code" authored (Bible §4: §5 = walkthrough/project-org; §6 = step-by-step build). Split at the natural CODE/BUILD seam if present (L7), or author from the build content (L4).

---

---

## 13. BATTERY CANON (v8.20 — LOCKED, S33)

**The classroom fleet runs rechargeable NiMH — Panasonic eneloop.** Every battery number in the book is written for NiMH.

| Reading (4 cells) | State | Meaning |
|---|---|---|
| **~5,400 mV** | Fresh off the charger | ~1.35 V/cell |
| **~4,800 mV** | The plateau | 1.2 V/cell — where NiMH spends most of its life. **This is `BATTERY_GOOD`.** |
| **~4,200 mV** | Nearly empty | 1.05 V/cell. **This is `BATTERY_LOW`.** Draining past it damages the cells. |
| **~6,300 mV** | Not NiMH | Somebody put alkalines in. |

- **The constants are the chemistry, not a guess.** `BATTERY_GOOD = 4800` / `BATTERY_LOW = 4200` (RobotConfig.h, L07+) are the NiMH plateau and the NiMH floor. Any lesson that states battery numbers must agree with them.
- **Alkaline is allowed but taught honestly:** 6.0 V nominal — which *is* the motors' rated voltage, so a robot on fresh alkalines is slightly faster (Pololu quotes motor specs at 6 V). But alkaline voltage **slides downhill the whole time it is used**, while NiMH holds a flat 1.2 V plateau and then drops. *A robot on alkalines is a moving target: the one you tuned in first period is not the one you get in seventh.* This is the same physics L11 ("Time Lies, Distance Doesn't") is built on.
- Sources: Pololu recommends NiMH (4.8 V nominal) and notes motor specs are at 6 V; Panasonic states eneloop holds a consistent 1.2 V through the charge while alkaline drops rapidly below it.

---

## 14. ENGINEER'S LOG (v8.20 — LOCKED, S33)

One 📓 callout at the **end of §10** in every lesson, above the footer. **Prose only — no `<pre>`, no new anchors.** The payload gate never sees it; no byte count moves.

**Markup (canonical):**
```html
<h3 style="[LOCAL SKIN of that lesson's §10 subheads]">Engineer&rsquo;s Log</h3>
<div style="background: #f8f9fa; border-left: 5px solid #1a5276; padding: 15px 20px; margin: 20px 0; border-radius: 4px;">
<b>&#128211; ENGINEER&rsquo;S LOG #NN &mdash; feeds: [TDP section]</b><br>
[the prompt]<br>
<i>Why judges care: [one line]</i></div>
```
The heading adopts the lesson's local §10 skin; **the box is book-wide constant** (TDP-blue `#1a5276`) so the log is recognizable as one instrument across 16 lessons.

**The 16 prompts (locked S32, written into the book S33):**

| # | Feeds (TDP section) | Prompt |
|---|---|---|
| 01 | Electronic Design → main controller | Write the "before" paragraph. Rewritten in L16 — the gap is the Abstract. |
| 02 | Electronic Design → sensors/actuators | Draw the board. Labeled, one page, no code. |
| 03 | Mechanical → actuators & power train | Record your TRIM — and why it isn't zero. |
| 04 | Electronic Design + testing data | Record calibration min/max; why the numbers move rooms. |
| 05 | Project Planning → constraints | Defend a forced tradeoff (pins 20 & 4 are shared). |
| 06 | Mechanical → power train + data | Show the COUNTS_PER_CM arithmetic; did 30 cm come out 30 cm? |
| 07 | **Software → architecture** | Draw the 8-file architecture. No source code. *(Highest-value entry in the book.)* |
| 08 | Software → innovative solutions | Explain P-control in plain English; then your Kp and how you found it. |
| 09 | Software → flowchart | Draw your state machine. |
| 10 | Project Planning → requirements | What does your obstacle maneuver cost you? |
| 11 | **"What didn't work"** | The failure entry: fresh battery vs. tired battery. |
| 12 | Performance → testing data | Cross-examine the robot: encoder vs. gyro, carpet vs. slick. |
| 13 | Software + requirements | How does the robot *know*? Your false-victim threshold. |
| 14 | **Rules-mandated** | Your LoP procedure + self-test card (RCJ 4.3.7). |
| 15 | Performance Evaluation | Record the hill-climb: gains, MAE/PEAK/WEAVE, when you stopped. |
| 16 | Whole TDP | Assemble. Abstract **last**. *(Ships as §10.3.)* |

**Rule: instruments go forward, documentation goes backward.** Code added to a published lesson invalidates payload bodies and the taught byte chain; prose-only retrofits do not.

### 14.1 THE LOG *IS* THE TDP — ONE GROWING DOCUMENT (v8.26 — LOCKED, S40)
The 16 Engineer's Log prompts are **not 16 independent worksheets** — they are a scaffold that **accumulates into a RoboCupJunior Technical Description Paper (TDP)** by L16. The engineering notebook and the competition TDP are the **same artifact**; students do not start a separate paper at the end.

- **Delivery = ONE growing Google Doc structured as the TDP from day one.** Each student makes **one copy** of the template at course start and keeps it in their own Drive all term (a Doc survives a semester across shared lab machines; `localStorage` fails cross-machine).
- **Template = `ZUMO_TDP_Template.md`** (repo root, live). Structure: PART A standing running-logs (A1 Hats-I-Wore · A2 Improvement-Ideas one-line-per-lesson · A3 Failure Log · A4 Measured-Data OLED tables · A5 Lab Log for Outside-Work evidence) + PART B the TDP proper (Abstract **last** · Intro/Robot & Author solo · Planning · Hardware · Software · Performance Eval · Lessons Learned · Deliverables/LoP · Version 2).
- **One source of truth:** the log **prompts stay in the lessons** (the §14 callouts); the Doc holds only the TDP scaffolding + standing lists. Do not duplicate prompt text into the template.
- Design goal: **minimum extra student effort** — a piece filled the week each lesson finishes, so the TDP format becomes muscle memory rather than an end-of-term scramble. Each prompt's "feeds:" tag names the TDP section it drops into.

---

## 15. MAKER REGISTRY & LINK CANON (v8.22 — LOCKED, S36)

The Maker registry and the lesson are ONE artifact seen from two sides. When they drift, a student clicks a link labelled `7C` and downloads what the lesson calls `7D`. Four rules, all earned.

### 15.1 THE SECTION 7 LADDER IS FIVE RUNGS — AND THE LETTERS MUST MATCH
Every calibration ladder is exactly **7A-7E**, and `KINDS[N]` carries exactly `cal_7a` ... `cal_7e`. **The Maker's letter must be the lesson's letter.** Canonized after S36 found L11's Maker off by one from 7C onward: `cal_7c` was labelled "Two Gaps in a Row" (the lesson's **7D**), `cal_7d` was a "Full Course" build **no lesson rung referenced**, and the lesson's **7C - TRIM Under Blindness had no kind at all**. Nothing was broken enough to fail a gate; the letters had simply drifted apart. **GATE CHECK: for every lesson, assert the ordered list of Section 7 rung letters in the HTML equals the ordered list of `cal_7*` letters in the Maker.**

### 15.2 `finished` IS THE LAST STEP — step kinds cover 1..N-1 ONLY
If Section 6 has N steps, the Maker carries `step_1` ... `step_N-1` **plus** `finished` — and `finished` IS step N. A `step_N` kind for the LAST step is a **duplicate**, not a build. Canonized after S36 found L14 (4 steps) carrying `step_1`..`step_4` *and* `finished`, with `after_step_4` **byte-identical** to `finished`: the Maker was offering one project under two names. L11/L12/L13/L15/L16 all obey this by construction. **GATE CHECK: assert `after_step_<last>` is NOT byte-identical to `finished`. If it is, the last step kind is redundant — retire it.**

### 15.3 A KIND MAY SHARE ANOTHER KIND'S `payloadRef`
The Maker resolves a payload through the KINDS row's 6th field (`var pay = (P && rec[5]) ? P[rec[5]] : null;`) — **not** by the kind key. So a **run-only rung**, one that changes no code and only changes what the student does on the floor, legitimately points at an existing payload. L14's 7A/7B/7D/7E and L15's 7B/7C/7E all point at `finished`; S36 pointed L11's `cal_7c` (TRIM Under Blindness — the student zeroes their own TRIM) at `cal_7b`. **Do NOT manufacture a duplicate payload body just to give a rung its own key.** A shared ref is correct, cheaper, and self-documenting.

### 15.4 THE FOUR LINK SHAPES (LOCKED)
Every kind is reachable from the lesson. Four shapes, no others:

| Group | Shape | Placement |
|---|---|---|
| Build steps + `finished` | `<details>` titled `CATCH-UP - Step N` | END of the step block, AFTER the CHECKPOINT |
| Calibration 7A-7E | `<details>` titled `7X in the Project Maker` | END of the rung block |
| Bonus mysteries | bare `<p>` | END of the mystery card |
| Section 9 challenges | link INSIDE whatever the lesson already discloses | last child of the solution `<details>` |

Href is always `https://weymuth.github.io/zumo/newproject.html?lesson=N&amp;kind=<key>`, styled `color: #2e86ab; font-weight: bold`.

The challenge shape follows the lesson, because **the book has no single disclosure canon** — L06/L07/L11/L13/L14 publish solutions, L08/L09 withhold them, L10 gives neither, L12/L15 print a scaffold with a blank. The link goes wherever that lesson already puts its answer. (DJ ruling S36: leave it; revisit after classroom use.)

### 15.5 THE MAKER IS NOT UNIFORMLY FORMATTED — EDIT BY OFFSET, NEVER BY LINE
`PAYLOADS` is **pretty-printed for some lessons and compact single-line for others**: L11's block has one key per line; **L14's entire block is ONE line**. A deletion written as `ls = s.rfind(newline, 0, key); s = s[:ls] + rest` works on L11 and **destroys L14**, because `rfind` walks back past every preceding key to the start of the whole lesson block. S36 corrupted the Maker exactly this way — PAYLOADS silently collapsed from 15 lessons to 10 — and caught it only because `node` re-parsed the object afterward. **Cut key -> object -> comma by exact offset. Then re-parse the whole file in `node` and assert lesson count, zero dangling refs, and zero orphan payloads. A JS syntax check alone will NOT catch a swallowed sibling.**

Neither is the LESSON uniform. Do not pattern-match across lessons:
- **Back-to-top markup has FOUR distinct forms** across L11-L16 (`text-align: right; margin-top: 25px` / `text-align:right; margin-top:10px` / `text-align: right` / `margin-top: 22px`).
- **Bonus mysteries are `h3` in L11/L15/L16, `h4` in L13/L14, and heading-less styled `<div>` cards in L12.**
- **L11's "Step N" headings also appear in Section 8A.4 theory** (the cliff-arithmetic derivation), not only in Section 6. A regex on "Step N" wires the lesson into the wrong section.

Hand-place every anchor, `assert count==1` on each, and audit each link against the heading it ACTUALLY landed under.

---

## 12. DOCUMENT WORKFLOW (v8.24 — REWRITTEN, S36)

### 12.1 EVERYTHING LIVES IN THE REPO
`github.com/Weymuth/zumo` is not just the published site — it is the **whole project**. The repo root carries this Bible, `LIVE_ZUMO_TEXTBOOK.md`, every session handoff, `gate_payload_match.py`, `pio_harness.sh`, `extract_project.py`, `IMAGE_SHOT_LIST.md`, `ROBOCUP_RESCUE_LINE_2026.md`, `PUSH_WORKFLOW.md`, and the web tools (`newproject.html`, `timer.html`, `index.html`, and the AI Tutor at `tutor/tutor.html` + `tutor/worker.js` — see §20). Lessons live in `lessons/`, art in `images/`.

**Therefore: SESSION OPEN IS A CLONE, NOT AN UPLOAD.**
```bash
git clone --depth 1 https://github.com/Weymuth/zumo.git
grep -oE "Bible version: v[0-9.]+" zumo/ZUMO_SUPER_BIBLE.md
grep -oE "Project Maker v2\.[0-9]+"  zumo/newproject.html
# NOTE the -E and the "+". With a greedy "*" the pattern matches its own
# example in this Bible and returns a bogus second line. Require >=1 digit.
```
Then verify LIVE.md's date, status, and lesson versions against the clone. **If LIVE.md and the Bible disagree, ASK DJ — never decide unilaterally.** Use a fresh `--depth 1` clone for every verification batch; never reuse a stale one.

### 12.2 SESSION CLOSE — ONE ZIP, FULL REPO LAYOUT, EVERY CHANGED FILE
Deliver **one** zip per session, arranged in repo layout with **final repo filenames** (`lessons/Lesson_10.html`, not `Lesson_10_Obstacles_v02_1_5.html`). DJ extracts it over the clone, commits once, pushes once. `PUSH_WORKFLOW.md` (in the repo) is the click-by-click for the human side.

**THE ZIP CARRIES EVERYTHING THAT CHANGED — INCLUDING ROOT DOCS.** Bible, LIVE.md, and the new handoff go in the zip alongside the lessons and the Maker, because they are all repo files. Splitting them into "push files" and "project-folder files" is a **mistake** (S36 made it): one commit carries any mix of folders, so a split delivery just invites a version mismatch between the repo and DJ's copies. There is no project folder to maintain separately — the next clone brings the current Bible and LIVE.md down with it.

**⚠️ A ZIP CANNOT DELETE.** Removals — retired handoffs, orphaned images — must ship as explicit `git rm` lines in the close note, to ride the same commit:
```bash
git rm ZUMO_S<N-1>_HANDOFF.md
git rm images/<orphaned assets>
```

**THE HANDOFF'S NUMBER IS THE SESSION THAT READS IT, AND AS OF S114 THAT IS GATED (v8.102).**
§12.3 step 4 has said *write `ZUMO_S<N+1>_HANDOFF.md`* since v8.24 and the `git rm` line above
has said `ZUMO_S<N-1>_HANDOFF.md` for just as long, so the convention was never in doubt: at the
close of session N you write the file session **N+1** will read, and its title, its filename and
its *"paste at top of Session N"* line all carry that one number. Verified from git history 10/10
across S103–S112.

**IT DRIFTED THREE TIMES IN A SINGLE DAY, AND DJ CAUGHT EVERY ONE BY READING.** At S114 the
repo root carried a handoff whose filename and title named a session that had already run, while
its STATE block had been updated three times; the incoming handoff under its correct name had
never been committed at all. The convention was then inferred from that one defective example
rather than from this Bible, and the outgoing handoff went up under the wrong number. Later the
same day the session number itself was found disagreeing across four homes — the handoff
filename, the handoff title, the newest Bible changelog entry and LIVE.md — every one of them
hand-typed. **No instrument could see any of it.**

**Gate 28 was extended in the same session** to parse the number out of the filename, out of the
`# ZUMO — SNN HANDOFF` title and out of the *"paste at top of Session N"* clause, and to fail if
any two disagree — plus fail loudly, not skip silently, if the title shape is gone. Control-run
four ways including **both real defects above**. Before that it asserted only that exactly ONE
handoff exists, which a file renamed `ZUMO_S999_HANDOFF.md` satisfies — measured, and it passed.
**This is §24.2 arriving late: a rule canonized without its gate holds only where someone happens
to look, and for two sessions nobody looked.**

**Staging rule (unchanged):** the zip itself sits in the **outputs root**, flat. DJ cannot browse `/mnt/user-data/outputs` — a file that was never passed to `present_files` does not exist for him. Repo-layout subfolders live **inside** the zip; never stage loose deliverables in a subfolder.

### 12.3 WRITE ORDER AT CLOSE — LIVE.md IS WRITTEN **LAST**
The Bible, Maker, and gate get bumped *during* the session; LIVE.md's header describes the state *at close*. Write LIVE.md before those bumps are final and it records the opening state — a **write-ordering bug**, not a memory lapse, which is why "remember to update LIVE.md" is too weak to prevent it.

1. Build and gate every artifact.
2. Bump the Bible / Maker / gate.
3. **Regenerate LIVE.md** — `grep` the actual version strings out of the files just written. **Never hand-type a version from memory or from the session's opening state.** The version appears **twice** in LIVE.md (status line and source-of-truth banner) plus the LESSON STATE table — all must agree. Leave *historical* version mentions in per-session change blocks alone.
4. **Write the handoff** — `ZUMO_S<N+1>_HANDOFF.md`, versions grepped from the same artifacts. It opens by telling the next session to **verify the previous push landed**, with concrete tells (expected Maker version, expected link counts) — not "check that it pushed."
5. Zip, `present_files`, and state plainly which file replaces which and what must be `git rm`'d.

**See §12.6** — LIVE.md is written when the last version-changing edit lands (not only at close), an omitted LIVE.md makes a push incomplete, and session open runs a drift check against the files.

### 12.4 VERIFY A PUSH BY FRESH CLONE — AND CHECK **WHICH VERSION** LANDED
Not merely that a commit exists. S33 had two false-positive pushes: one where nothing committed, one where the *superseded* build went up because two files with the same name sat in Downloads. md5 every delivered file against the clone.

### 12.5 SOURCE-OF-TRUTH HIERARCHY
`ZUMO_SUPER_BIBLE.md` (specs) → `LIVE_ZUMO_TEXTBOOK.md` (session state) → the handoff prompt.
Surface any discrepancy to DJ; do not resolve it unilaterally.
*(`ZUMO_Callout_Standard_v1.md` retired at v8.8 — callout templates live in §8.)*

### 12.6 LIVE.md STALENESS IS A **STRUCTURAL** FAILURE — CLOSE THE WINDOW
§12.3 puts LIVE.md last and explains why a reminder cannot enforce it. What §12.3 does not cover is the session that **ends before reaching step 3** — and that is the failure that actually recurs. S54 pushed eleven challenge files, a Maker bump and a graphic without regenerating LIVE.md; S55 pushed L01 v03.3.0 and Maker v2.38 and did the same. Two consecutive sessions left the file describing a state two sessions old, and the next session opened on it. S55 burned **four attempts** on re-diagnosis, three of them building on version numbers that were simply wrong.

**A. Write LIVE.md when the last version-changing edit lands — then re-verify at close.**
§12.3's hazard is recording the *opening* state. That hazard ends the moment the final bump is decided; it does not require the session to finish. Write LIVE.md at that point and re-verify it in step 3. A session that dies afterward still leaves LIVE.md correct. This does not relax §12.3's ordering — steps 1–5 are unchanged — it removes the window in which a dead session leaves nothing behind.

**B. A push that changes a version and omits LIVE.md is an INCOMPLETE PUSH.**
Not an oversight to catch next time — a defect of the same class as a challenge card that disagrees with its file (§11). If the zip carries a bumped lesson, Maker, Bible or gate, it carries LIVE.md. State it in the close note.

**C. Session open runs a DRIFT CHECK, not a read.**
Every take that went wrong in S55 went wrong *before writing any code*, on state it accepted instead of verified. After the clone, grep the files themselves and compare to LIVE.md's claims:

```
grep -o "Lesson version: v[0-9.]*" lessons/Lesson_NN.html
grep -oE "Project Maker v2\.[0-9]+" newproject.html | head -1
#   cross-check: grep -oE "v2\.[0-9]+" newproject.html | sort -V -u | tail -1
#   NOTE: plain `sort -u` is WRONG here — it sorts alphabetically and returns v2.9 over v2.38.
grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md
```

**The files win. Always.** If they disagree with LIVE.md, say so in the session's FIRST message, and resolve it before any queued work:
1. **Ask DJ for a newer LIVE.md** — the previous session may have written one that never got pushed. An uploaded current file beats a reconstruction.
2. If none exists, **regenerate LIVE.md from the verified files** as the session's first task.

Do not proceed into queued work on a LIVE.md known to be stale. The cost of regenerating it is minutes; the cost of a session built on stale versions is the session.


### 12.4 VERIFICATION DISCIPLINE — CACHES LIE (v8.37 — LOCKED, S58)
When confirming a push, do NOT trust the first read:
- **Shallow-clone lag** — for ~1–2 min after a push a `--depth 1` clone serves the PRIOR commit. `sleep 40` and re-clone before concluding a push failed (this looked like a failed push twice in S58; both were lag).
- **`git show --stat HEAD` on a shallow clone LIES about a commit's scope** — with no parent commit present it lists the ENTIRE tree as "added." Do not use it to judge what a commit changed (it caused a false "200 files over-committed" alarm in S58; the files were pre-existing). Textbook case of §11 AUDIT FALSE-POSITIVE DISCIPLINE — a tool reports candidates, not verdicts.
- **`raw.githubusercontent.com` caches ~5 min; `api.github.com` rate-limits unauthenticated; `weymuth.github.io` is not in the bash allowlist** — the reliable verify is a fresh clone with an adequate wait, or asking DJ to eyeball the live page.
- **Upload-location trap** — a file meant for a subfolder can land in the repo root instead (happened with `tutor.html` → root in S58). If a subfolder change seems not to take, check for a stray root copy.

## 16. HARDWARE GROUND TRUTH (v8.25 — LOCKED, S39)

**These are physical facts about the Zumo 32U4 fleet. Do not re-litigate them; verify against source if in doubt, do not guess.** They lived only in session memory until S39 — this section is the durable backup.

### 16.1 GEAR-RATIO STICKER COLOR CODE
The assembled Zumo hides its gear ratio on a **colored sticker on the underside of the main board, visible in the battery compartment with batteries removed** (Pololu User's Guide 0J63 §1.1). The color IS the ratio:

| Sticker | Gear ratio | Character |
|---|---|---|
| **Green** | 50:1 HP | fastest, lowest torque |
| **Blue** | 75:1 HP | middle — **the classroom fleet** |
| **Red** | 100:1 HP | slowest, highest torque |

- **Our fleet is BLUE = 75:1.** Any lesson that names the ratio says 75:1.
- The motors carry NO external color dot; on an assembled robot the sticker is the only non-destructive ID (reading the motor SKU requires disassembly).
- If two robots disagree on how far "speed 200 for 2 s" travels, check the stickers before blaming the code — a different color is a different ratio.

### 16.2 TRIM POLARITY — LEFT MOTOR, BOOK-WIDE
`setSpeeds(speed + TRIM, speed)`. TRIM adjusts the **LEFT** motor only. Positive TRIM speeds the left wheel, pushing the robot RIGHT, correcting a LEFT curve (a robot curves toward its slower track). Verified against Pololu `FaceTowardsOpponent.ino`. This never changes, in any lesson. TRIM goes ONLY on open-loop straights — never in `turnDegrees()` (wheels oppose on purpose) or `followLine()` (P-control is already a closed loop). See §11 TRIM PLACEMENT RULE.

### 16.3 setSpeeds() HARD-CAPS AT ±400 — WHAT constrain() ACTUALLY PROTECTS
`setSpeeds()` clamps any argument beyond ±400 internally (like a VEX motor maxing out regardless of the number fed it). Therefore `constrain()` is **NOT** there to protect the motor. It matters when YOU reuse the speed number elsewhere — displaying it, logging it, feeding it into more math — where an out-of-range value (e.g. 415) would be wrong or confusing. Constrain your own variables so the number you see equals the number the motor gets.

### 16.4 THREE KINDS OF STOP — Zumo setSpeeds(0,0) IS A BRAKE
"Stop" is not one thing: **coast** (leads open, rolls to a halt, drifts past), **brake** (motor shorted across itself, stops promptly), **hold** (actively drives toward "stay here," uses power while still). On the Zumo, `setSpeeds(0, 0)` gives a **brake**-style stop — the driver shorts the motors. When a robot "won't stop where I told it," the question is often *which kind of stop* was used.

### 16.5 STALL CURRENT — ONE EVENT, TWO SYMPTOMS
Max current flows when a motor is powered but cannot turn (~1.5 A per motor on the Zumo, ~5× free-run). Two situations, same electrical event: (1) wheels held/robot jammed — energy dumps as heat, cooks the motor within seconds; (2) robot too heavy or mis-geared to move — motor pulls stall current and sits still. A robot that buzzes/strains but doesn't move is stalling and heating; cut power.

### 16.6 ENCODER AVERAGING — BOTH WHEELS
Distance/turn loops gate on `averageCounts()` (average of BOTH encoders), never one. A slipping or stiff wheel on the unwatched side ends the move early or late with no warning. See §11 ENCODER AVERAGING RULE.

### 16.7 SHARED PINS 20 & 4 — LINE vs PROXIMITY ARE MUTUALLY EXCLUSIVE
Pins 20 and 4 are physically shared between line sensors 2/4 (DN2/DN4) and the left/right proximity receivers. Five-sensor line following and three-proximity operation cannot run together. `initThreeSensors()` steals those pins back from line sensing; `initFrontSensor()` is the correct call when line sensing must survive (e.g. L10).

### 16.8 FLASH / RAM CEILING — 28,672 B / 2,560 B, PIO-TRUE, -flto
Real flash ceiling = **28,672 B** (32,768 − 4,096 bootloader), RAM = **2,560 B**, from `platform-atmelavr boards/a-star32U4.json`. PlatformIO enables `-flto` by default. All byte measurements use PIO-true flags. The old S25 harness used a fictional 32,768 B ceiling — those figures are wrong (byte re-audit of L10/L12–L15 is a deferred package).

### 16.9 EEPROM ADDRESS MAP — THE FLEET SHARES ONE FLAT 1,024 BYTES (v8.36 — LOCKED, S57)
EEPROM is 1,024 bytes (addresses 0–1023) with no filesystem and no protection: nothing prevents one
program from overwriting another's bytes. Two things in this course live there, and the split is canon:

| Address | Owner | Contents |
|---|---|---|
| 0 – 511 | Lesson 16 | the `Saved` struct — magic `0x16`, gains, baseline (`EEPROM_ADDR = 0`) |
| 512 – 543 | Lesson 1 / teacher utility | magic `0x5A` + robot name, up to 20 chars + terminator (`NAME_ADDR = 512`) |
| 544 – 1023 | unclaimed | free for student enhancements |

Source of truth = `ZUMO_NAME_WRITER_main.cpp` (repo root), whose header comment carries the same map.
The names are written once per robot before the term and survive every student upload, because an upload
replaces **flash**, not EEPROM. Any new EEPROM use — a lesson, a challenge, an L16 §7 enhancement — takes
its addresses from 544 up and is recorded here.

---

## 17. SVG / GRAPHIC CANON (v8.25 — LOCKED, S39)

House style for every book diagram. Lived only in memory until S39.

- **Canvas:** `viewBox="0 0 1100 850"` (standard). Taller/shorter is allowed when content needs it; width stays 1100.
- **Title band:** rounded rect top-left, blue gradient `#1a5276 → #2e86ab`, white bold title, lesson tag right-aligned in `#d6e9f2` ("Zumo 32U4 Robotics · Lesson N").
- **Arrows:** SINGLE-POLYGON arrowheads only. Never a rect shaft + separate triangle head — it produces buried-tip overlap artifacts. One `<polygon>` per head, aligned to the line/arc end.
- **Section colors:** §4–6 green `#3a7d5c` / `#2a5a42`; TDP blue `#1a5276` for structure. Match the lesson's part when the graphic belongs to one.
- **Graphic number** bottom-right in `#9aa0a6` ("GRAPHIC N.NN").
- **File / number spaces:** IMAGE and GRAPHIC are SEPARATE number spaces (`L03_IMAGE_3-16` and `L03_GRAPHIC_3-16` legitimately coexist — see §10). Audit art against `images/` in a fresh clone, never against the lesson alone.

### 17.1 textLength IS A TRAP — STRETCH ONLY, NOT FIT
`textLength` on a `<text>` forces the string to that exact width. When the value **exceeds** the text's natural width it pads every character gap — a visible letter-spacing defect (S39 found this in GRAPHIC 3.7: `textLength="560"` on a ~408 px monospace line stretched `motors.setSpeeds(...)`). When the value is **≤** natural width it constrains text to fit a box and is fine. **`textLength` appears in ~30 book SVGs — a per-file audit (over-stretch vs. fit-to-width) is a deferred package; do NOT blind-replace.** A new SVG should omit `textLength` unless it is deliberately constraining text to a known box width.

### 17.2 QA EVERY SVG BEFORE SHIPPING
Render to PNG with `cairosvg` and eyeball it. A malformed path or an over-stretched line passes a syntax check but looks broken. Present previews to DJ for sign-off on any new or changed graphic.


### 17.3 PHOTOGRAPHS ARE NOT DRAWINGS — PRODUCTION AND EXPORT CANON (v8.83 — NEW, S98)

**§17.1 and §17.2 govern DRAWN graphics. This governs the other kind.** A book asset is one of two
things and the two are made, named, and checked differently:

| | subject | file | made in |
|---|---|---|---|
| **GRAPHIC** | a diagram — flowchart, ladder, file tree, timeline | true vector, **no raster of any kind** | drawn markup per §17 |
| **IMAGE** | a photograph — a populated board, the chassis, jumper positions | photo, **embedded**, plus an optional vector label layer | Photoshop → Illustrator |

**A PHOTOGRAPH CANNOT BE REDRAWN, AND ATTEMPTS TO DO SO PRODUCE A CARTOON.** S98 measured this:
every staged raster-in-SVG file carried photographic content, and the one true-vector redraw of the
main board (`…_top_view_r02.svg`, 194 elements, zero raster) turned out to be a traced imitation —
its 39 `<text>` runs were the board's **silkscreen**, not labels. DJ ruling, S98: *"Some of the
images need to be raster wrapped svg. Otherwise they look like crap."* Do not re-litigate this by
asking an AI to "fix" a photograph; asking is what produces the cartoon.

**THE EMBED IS MANDATORY, NOT A PREFERENCE.** An SVG loaded through `<img src>` — which is how every
book image is loaded — runs in the browser's **secure static mode** and cannot fetch any external
resource. A linked image renders as **nothing** on the published site while looking perfect on the
machine that exported it. This is the single most dangerous setting in the pipeline because it fails
silently and only in production.

**ILLUSTRATOR EXPORT — the two settings that bite:**
1. **Images: Embed, never Link.** See above. A linked photo is a blank graphic on the site.
2. **Fonts: use a common stack (Arial/Helvetica) or convert labels to outlines.** Live `<text>` in an
   `<img>`-loaded SVG renders with the **viewer's** fonts — no webfont can load. An uninstalled font
   falls back and the layout shifts. This is the same trap §18.2 hit with the spiral-star digits,
   where the ruling was vector paths precisely because they are renderer-proof. Outlines cost
   editability; that is the trade, and it is deliberate.

**AFTER EVERY EXPORT, ONE COMMAND:** `python3 fit_raster_svg.py FILE.svg --write`. It dedupes the
payload, drops a dead alpha channel, caps resolution at 2× the on-screen box and re-encodes at a
**pinned q92**. **Quality is the rule; size is the consequence** — never lower quality to hit a size.
A file that is still over the ceiling at full quality is carrying too much and should be **split**,
not degraded. Expect Illustrator to re-encode the photo on export; that is fine and expected, and is
why an md5-unchanged test applies only to AI-returned files, never to an Illustrator round-trip.

**Gate 37 (`§21.1`) is the backstop** and enforces three things on referenced files: no duplicated
payload (the same base64 in both `href` and `xlink:href` — some exporters write both, doubling the
file), a byte ceiling, and a floor of vector elements below which the file is a photograph
mislabelled as a graphic and belongs at `.jpg`/`.png` under an `IMAGE_` name. The thresholds live in
`book_gates.py`; this section deliberately does not restate numbers that a gate already owns.

#### 17.3a THE TWO RECIPES — PROVEN, S98

**Both are one paste. Neither asks for a byte count** — an AI cannot hit one reliably and will
report success without having tried (S97: it declared the sensor arrays fixed while the embedded
PNG came back **byte-identical, same md5**). Size is handled locally, afterwards, by
`fit_raster_svg.py`, with gates 37 and 38 as the backstop.

**RECIPE 1 — A DRAWN GRAPHIC (flowchart, ladder, file tree, anatomy diagram).**
Proven on five files in S98: L07 7-02, L07 7-04, L06 6-09, L06 6-10, L06 6-12.

> Return the SVG with all text as live `<text>` elements — do not convert text to outlines or
> paths. Use `font-family="Arial, Helvetica, sans-serif"` for body text and
> `font-family="Courier New, monospace"` for code. Keep every rect, circle, line and polygon as
> real elements. Use `viewBox="0 0 1100 850"` and fit the artwork to it.

Check four things when it comes back, all mechanical:
1. `<text>` elements present and roughly one per label
2. path data near zero — a drawn graphic has almost none
3. `viewBox` is `0 0 1100 850` (§17 canon)
4. font-family reads Arial/Courier New, not Inter, JetBrains Mono, Segoe UI or Consolas

**Result across the five: 829,096 B → 30,388 B on the three L06 files alone, 96.3% smaller, with
38–42 live labels each.** Gate 38 now enforces all of this.

**RECIPE 2 — A PHOTOGRAPH WITH LABELS (a populated board, the chassis, jumper positions).**
The subject cannot be redrawn; §17.3 above explains why, and what happens when it is tried.

> Attached is an SVG containing a photograph embedded as base64. Do not redraw the photograph. Do
> not trace the board. Do not reproduce silkscreen text as vector. Keep the embedded image exactly
> as it is, byte for byte, in place. Add only a label layer on top: `<text>` callouts, leader lines
> and highlight boxes. Return the same SVG with that layer added and nothing else changed.

Check two things, both one line:
1. the file still contains `base64` — if it does not, the photograph was thrown away and redrawn
2. the embedded image's **md5 is unchanged** — this is the test S97 failed

Then: `python3 fit_raster_svg.py FILE.svg --write`.

**THESE FILES OPEN IN ILLUSTRATOR.** A base64-embedded raster imports as an ordinary embedded image
object, so the photo can be repositioned and the label layer edited with the normal tools — no XML
by hand. Three things on the way back out:
- **Export with Images: Embed, never Link.** A linked photo is a blank graphic on the published site
  (§17.3 — secure static mode). This is the one setting that fails silently and only in production.
- **Fonts: Arial/Courier New, or convert labels to outlines.** On a photo-plus-labels file outlines
  are cheap — a handful of labels, not a whole diagram — so this is a real choice here, unlike
  Recipe 1 where it cost 50x.
- **Illustrator re-encodes the photo on export, which is expected.** The md5 test above applies only
  to AI-returned files, never to an Illustrator round-trip. Run `fit_raster_svg.py --write`
  afterwards; it also catches the duplicate payload some exporters write into both `href` and
  `xlink:href`.

**Filename suffixes, confirmed against all 155 files (S97):** trailing `_##` = a spiral star (all 16,
zero exceptions) · trailing `_r##` = a redo, **staged, not live** · mid-name `N-NN` is the image
number and cannot collide. `IMAGE_` and `GRAPHIC_` remain separate number spaces per §17 and §10.


#### 17.3b THE CREATE SIDE — BUILDING A PHOTO COMPOSITE IN ILLUSTRATOR (v8.85 — NEW, S99)

**§17.3a Recipe 2 is what to ASK AN AI for when a composite already exists. This is how to MAKE one.**
The gap was found by DJ in S99: §17.3 named "Photoshop → Illustrator" as the route and never wrote
the route down, so the create side lived in chat while the export side was canon.

**STEP 0 — PREPARE THE PHOTO FIRST. This is the step that decides the file size.**
Measured across the three staged composites, S99: **all three embed PNG**, two of them RGBA whose
alpha `fit_raster_svg.py` measures as carrying nothing, and one stores its payload twice.

| file | embedded format | payload | after fit |
|---|---|---|---|
| `L02 2-07_ir_sensors_r02` | PNG RGBA 1750x190 | 438,626 B | 128,287 B |
| `L05 5-08_three_sensor_array` | PNG RGBA 2048x479 | 1,266,035 B | 215,741 B |
| `zumo_chassis_r01` | PNG RGB 1105x750, **stored twice** | 960,966 B | 178,544 B |

So, in Photoshop, before anything else: **flatten to JPEG, not PNG** (PNG is lossless and stores a
photograph terribly), **drop the alpha channel** unless something is genuinely transparent, and size
the image to roughly **2x the on-screen box** — the same cap `fit_raster_svg.py` applies. A photo
prepared this way arrives near its final size instead of being rescued from 10x.

**STEP 1 — PLACE IT EMBEDDED.** `File > Place…`, select the photo, and **uncheck Link** in the
dialog. If it is already placed as a link: `Window > Links`, select it, flyout menu, **Embed
Image(s)**. §17.3's warning is the whole reason — a linked photo is a blank graphic on the published
site and looks perfect on the machine that exported it.

**STEP 2 — SIZE THE ARTBOARD TO THE PHOTO.** There is **no fixed canvas for a photo composite.**
Recipe 1 fixes drawn graphics at `viewBox="0 0 1100 850"`; photo composites legitimately vary with
their subject, and the live files run 2000x1200, 2000x1180 and 1448x1086. Do not force them.

**STEP 3 — LABELS ON THEIR OWN LAYER**, above the photo: `<text>` callouts, leader lines, highlight
boxes. Keeping them separate is what makes a later relabel cheap and what stops a re-export from
disturbing the photograph.

**STEP 4 — SAVE AS SVG.** `File > Save As > SVG` (or `Export As > SVG`). Four settings:
- **Images: Embed** — never Link. See above; this is the one that fails silently and only in production.
- **Fonts: Arial/Helvetica stack, or Convert To Outline.** On a photo composite outlines are cheap —
  a handful of labels, not a whole diagram — so unlike Recipe 1 this is a real choice. **What is NOT
  a choice is designing in a font nobody has:** `L05 5-10` ships its labels as
  `Inter,Arial,sans-serif`, and Inter cannot load through `<img src>`, so every reader sees the Arial
  fallback and a layout that shifted after it left Illustrator. Put the common font FIRST.
- **Styling: Presentation Attributes** — keeps the label layer editable as ordinary attributes.
- **Responsive: on** — omits `width`/`height` and keeps `viewBox`, which is what the book's
  `width: 100%` image CSS wants.

**STEP 5 — ONE COMMAND, ALWAYS:** `python3 fit_raster_svg.py FILE.svg --write`. It dedupes the
double payload some exporters write into both `href` and `xlink:href`, drops a dead alpha channel,
caps resolution and re-encodes at a pinned q92. **If step 0 was done properly it will find little to
do, and that is the goal** — its CONTROL 4 proves it leaves a good JPEG alone rather than putting it
through a second lossy generation.

**GATE SCOPE, STATED SO IT IS NOT ASSUMED:** gate 38's drawn-graphic checks **skip any file
containing a raster** — that population belongs to gate 37. A photo composite is therefore NOT
checked for live text, and outlined labels in one are legal by design.

*The Illustrator menu paths in steps 1 and 4 are recorded from DJ's workflow, not from the repo;
verify them against the installed version before treating them as exact.*



#### 17.3c THE PAYLOAD ATTRIBUTE — `xlink:href`, NEVER PLAIN `href` (v8.86 — NEW, S99)

**An embedded raster must be carried by exactly one `xlink:href`, with `xmlns:xlink` declared on
the root.** Plain `href` on `<image>` is SVG 2. **Illustrator parses SVG 1.1**, cannot read it, and
reports the picture as a MISSING LINK — naming the folder the document happens to sit in, which
reads like a stray file rather than a format problem.

**Browsers render both forms identically.** That is why this survived a whole session: every file
looked perfect on the published site and none of them would open for editing. It took DJ trying to
edit one in Illustrator to find, exactly as §17.3 itself was found by DJ looking at a rendered file.

**The rule that produced it was half right.** S98 correctly found the chassis file storing its
960,966 B payload TWICE — in `href` and `xlink:href` — and made `fit_raster_svg.py` dedupe. Deduping
was right. **Keeping the wrong survivor was not.** Every file the tool touched afterwards became
unopenable in Illustrator, which is the whole point of Recipe 2.

**Confirmed by the cheapest possible test:** one file converted, opened, and it worked. Do that
before changing three instruments on a theory.

**Now enforced in three places:** `fit_raster_svg.py` v1.2 keeps the xlink form and its control 1
counts BOTH attributes rather than asserting "the duplicate is gone" — the old control passed
happily throughout. `svg_layout_audit.py` flags a plain-href file. The graphics prompt states it
with its failure mode attached, because the previous version stated the opposite just as firmly.

**§24 corollary, and the session's shape in one line: a control that does not ask WHICH is not a
control.** Gate 37 in S98 was green while encoding a wrong rule; this control was green while the
wrong attribute survived. Both were caught by a human looking at the artefact, not by the suite.


---

## 18. CHALLENGE-DESIGN CANON (v8.26 — NEW SECTION, S40; §18.4 type-explainer added v8.30, S45)

Rules for how a §9 challenge is *designed* — distinct from §6.12 (the card's visual skin) and §9 (its PART placement). These govern what a challenge must teach and reinforce, and how a challenge **starter** is shaped.

### 18.1 THE SAXON SPIRAL — EACH LESSON REINFORCES PRIOR CONCEPTS
Modeled on Saxon Math's distributed practice: **each lesson's challenges reinforce 1–2 PRIOR concepts alongside the new one**, so skills are re-exercised across the book instead of taught once and dropped. Committed book-wide (DJ, S40, "even though it's a pain").

- **Rollout, not retrofit:** apply **going forward, lesson by lesson**, as part of the walkthroughs in progress. The spiral deepens naturally in later lessons (more prior concepts exist to draw on). **Do NOT force it into L01/L02** — nothing precedes them to review.
- **One new concept per rung.** A challenge ladder climbs monotonically: each rung introduces exactly one distinct new concept; the spiraled prior skill rides alongside as reinforcement, never as the rung's own new idea.

### 18.2 SPIRAL MARKER CONVENTION (LOCKED)
Two markers, both required on a spiraled challenge:
- **(a) Header line** — a blue **"🔁 Builds on:"** line at the **top of the challenge card**, naming the precise source **in words** (e.g. "🔁 Builds on: the `if` comparison from L03, the OLED print from L02"). *(Student-facing header renamed from "Spiraled skills" → "Builds on" in v8.27; "spiral" stays the teacher-side method name in prose.)*
- **(b) Inline stars** — **⭐ numbered stars** placed inline at the point of use, the **source lesson number inside the star**, as a wayfinding breadcrumb back to where the skill was taught.
  - **RENDERING (LOCKED, DJ ruling S43):** an inline star is the **actual SVG asset**, not an emoji — `<img>` the `spiral_star_NN.svg` file so students see the real numbered star both in the "🔁 Builds on:" explainer example AND at every point of use. Emoji ⭐ is used ONLY in the literal header text `🔁 Builds on:` (a glyph, not a lesson-numbered marker).
  - **Canonical inline-star tag** (Canvas needs ABSOLUTE raw URLs — never relative `images/…`):
    `<img src="https://raw.githubusercontent.com/Weymuth/zumo/main/images/spiral_star_NN.svg" alt="Spiral review from Lesson NN" style="height: 1.1em; vertical-align: middle; margin: 0 2px;">`
    Star SVGs are square 200×200; a fixed `height` keeps them line-sized. Do NOT use `max-width: 100%` on a star (that is the figure/diagram convention). `NN` is the ZERO-PADDED source lesson number and must match the `spiral_star_NN.svg` filename.
  - **First book-wide appearance:** L02 §9 "🔁 Builds on:" explainer callout (S43), which introduces the mark once before L03's first marked card (Battery Warning). Any new marked card reuses the tag above verbatim.
- **Assets:** `spiral_star_01`…`spiral_star_16` (16 SVGs, `images/`) — flat **Antique Bronze `#7B6240`** star, **Parchment `#F5F2E9`** **vector-path** number (not font text — renderer-proof, centered, uniform width). Built S40; **repainted to `BookComponentStandard` §9 before S101 and verified conformant in all sixteen files at S101** — zero gradients, zero trace of the retired gold. **The retired spec read gold-gradient `#FFD34D → #F5A623` with a `#1a5276` number; it described files that no longer existed and is recorded here only so the change is legible.** §9 governs the numbered mark; this section governs only where a star is placed and how it is sized. The name "spiral" is inherited from §18.1's Saxon-spiral METHOD — the mark is not spiral-shaped.

### 18.3 CHALLENGE-TEMPLATE PRINCIPLES (LOCKED, DJ ruling S44 — REVERSES the S40 minimal-skeleton rule; term set S48)
**TERM (DJ ruling S48):** the starter a challenge ships is a **challenge template** — that is its name project-wide (Bible, lesson cards, Maker labels). "Starter" remains fine as a generic synonym in prose; "scaffold" is NOT used for this sense (it still names the TDP accumulation in §14 and the theory-first build in §5).

A **challenge template** is the **full section-header template** — the same structure every lesson program has — NOT a stripped-down skeleton and NOT the finished lesson code. Students are used to seeing the whole template; a bare skeleton reads as unfamiliar and a finished program overwhelms. The challenge template ships the complete structure with the **concept being taught left blank** in a marked landing zone.

- **Every standard section header the program needs is present, in canonical order — none dropped just because a step hasn't filled it yet:** `HARDWARE OBJECTS` · `CONSTANTS` (L03 vocab: `CONFIGURATION`) · `FUNCTION PROTOTYPES` · `GLOBAL VARIABLES` (L03 vocab: `STATE VARIABLES`) · `HELPER FUNCTIONS`, around `setup()` and `loop()`. The header NAMES vary by lesson vocabulary, but the SET and ORDER are canonical; dropping a header is the defect this rule prevents (S51: the ≥L4 `mainCpp()` scaffold was missing `GLOBAL VARIABLES` — the L04 Step-2 landing zone — until Maker v2.33). A single-concept challenge starter may mark a genuinely unused section `// (none needed for this challenge)`; a multi-step program scaffold (e.g. the L04 Main build) shows the header with a blank body for the student to fill across steps.
- **Hardware objects pre-placed** — the object(s) the challenge needs (e.g. `Zumo32U4Motors motors;`).
- **CONFIGURATION constants seeded**, following the §11 blank convention: a tunable ships as `= 0` with the starting guess in the comment (`const int RUN_MS = 0;   // <-- YOUR NUMBER. Try 1000 (1 s).`); a fixed value ships with its number and a short note.
- **A marked landing zone:** a clear `// write your code here` where the taught concept goes, followed by numbered step hints. The taught concept itself is NOT pre-written.
- **`setup()` / `loop()` present but NOT re-explained** — taught in L01 §5.3 and L02; re-teaching them in every starter is noise. An empty `loop()` carries a one-line note of why (`// (empty - the run happens once, in setup)`).
- **The Maker wrapper supplies the top of the file.** `mainCpp()` auto-prepends the banner comment (`LESSON NN - <title>`, AUTHOR, DATE), the `#include <Zumo32U4.h>`, AND the MY PLAN block. **A payload body therefore STARTS at `// ===== HARDWARE OBJECTS =====`** and must NOT contain the banner, include, or MY PLAN, or they double. (MY PLAN still ships blank for the student — but it comes from the wrapper, not the payload.)
- **CHAT-DISPLAY RULE (S45):** when *showing* a starter to DJ in chat, PREPEND the wrapper header (`#include <Zumo32U4.h>` + MY PLAN block) so what DJ sees matches what the "make this folder for me" link generates. Pasting the raw payload body (which starts at `HARDWARE OBJECTS`, no include) is misleading — a hand-built copy of it fails to compile (`'Zumo32U4Motors' does not name a type`, `'delay' not declared`). The stored body is correct; the chat display must be the *generated file*, not the payload fragment.
- **A starter must not require a construct the book hasn't taught yet.** If the natural solution wants a `for`/`while` loop (not taught until L05), the landing zone directs an unrolled / by-hand approach and may forward-reference the later lesson. (L03 Ramp, S44: unrolled fixed steps that later motivate the L05 `for` loop.)

**Relation to the Maker (§15):** challenge `kind=` ids are unchanged by starter/label work; folder **labels** may take a `C##` prefix (rename the OUTPUT-folder string only, keep the `kind=` id, FLAT not subfolders — PlatformIO wants one level). Verify `?kind=` challenge downloads deliver **starters, not solutions**.

### 18.4 TYPE-EXPLAINER CALLOUT (LOCKED, S45)
When a data type is first *introduced*, it appears in a **blue info callout** (`background-color: #e3f2fd; border-left: 4px solid #2196f3`) titled with a `</>` glyph, holding one short line per type — `type — plain-English description — code example`, each on its own white row. This is the reusable **type-explainer visual**: the *same look* is used every time a type gets its deeper treatment, so students recognize "a type is being explained" on sight.

- **First introduction (L02 §3.2b):** all five types students will write themselves appear together — `int`, `bool`, `float`, `long`, `char` — one line each. Deep prose follows the callout for the types in play *now* (int, bool).
- **Deferred deep dives reuse the same callout look** at the point of first use: `long` in L05 (timing), `float` in L07 (decimal math). `char` is named for completeness only — the book rarely needs it, so it gets no deep dive.
- **Forward-pointers must be verified against the code**, not guessed — grep for the first genuine declaration before naming a lesson (S45: an early draft pointed `float` at L05; it first appears in L07).

---

## 19. PER-LESSON LEARNING-MODE FILE (v8.32 — NEW SECTION, S48)

When a lesson's challenges are walked in **learner mode** (the Socratic path — DJ writes the challenge code himself, coached with leading questions), the walkthrough is captured in a companion file named **`ZUMO_LEARNMODE_LNN.md`** in the **repo root** (flat, not a subfolder). One file per lesson; created when that lesson is first walked.

- **What it holds:** a student-difficulty roll-up (per-step, per-challenge), per-challenge walkthrough detail, the Coach's Tips surfaced during the walk, and a queued-tasks list of "used-but-never-taught" and card/payload findings.
- **What it is NOT:** it is a **teacher-side teaching record**, not student-facing content and **not a Maker payload source**. A challenge template lives in the Maker (§18.3); the learn-mode file only *records the finds* that motivate template/prose edits. Do not build payloads from it.
- **Naming (LOCKED):** exchanges within a walk are tagged `L##_C##_W##` (Lesson-Challenge-Walkthrough-step). The file is `ZUMO_LEARNMODE_LNN.md`, zero-padded `NN`.
- **Downstream use:** these walkthroughs are the intended raw material for the **AI Tutor** (REBUILT & LIVE S58 — see §20) — the model that worked (isolate one new idea, let the wrong answer happen and correct in place, trace values by hand) is captured here for reuse.
- **Live today:** `ZUMO_LEARNMODE_L03.md` (S47). A separate `ZUMO_L03_TEMPLATES.md` holds the six draft L03 challenge templates + solutions — that one is **STAGING** (source-of-intent), not gate-verified payloads.

---

---

## 20. AI TUTOR & MACHINE MARKERS (v8.37 — NEW SECTION, S58)

The AI Tutor is LIVE: `tutor/tutor.html` (front-end) + a Cloudflare Worker at `zumosupport.weymuthd.workers.dev` (repo source-of-record `tutor/worker.js`). Founding principle — **anti-rot: it READS THE LIVE LESSONS at run time and embeds NO curriculum**, so it self-updates whenever a lesson is edited. The old tutor rotted precisely *because* it hardcoded the curriculum in the worker prompt (it taught the cut cliff feature, wrong lesson numbers, no L15/L16). **Never reintroduce embedded curriculum.**

**Architecture (for future edits):** the front-end, on lesson-select, fetches `../lessons/Lesson_NN.html` from Pages, strips the solution reveals (§20.1), fences `<pre>` as code, and POSTs `{messages, currentChallenge, lessonContent, lessonTitle}` to the worker. The worker injects `lessonContent` as authoritative "CURRENT LESSON" context, holds the `ANTHROPIC_API_KEY` server-side, and uses model `claude-sonnet-5` with prompt caching on the system block. To edit the worker: dash.cloudflare.com → Workers & Pages → `zumosupport` → Edit code → paste → Deploy, **AND** update `tutor/worker.js` in the repo (the repo copy is the source-of-record; the live copy runs on Cloudflare).

Two invisible machine markers make the tutor work. **Both are mandatory on any new reveal or challenge**, or the tutor silently degrades.

### 20.1 `data-reveal` ON EVERY `<details>` (LOCKED)
Every `<details>` reveal carries `data-reveal="TYPE"`:
- **`solution`** — a worked answer, the code that solves a challenge, **or a debugging-mystery reveal that shows the planted bug + its fix** (framing it as an "explanation" does not exempt it — if it hands over the answer, it is `solution`). **The tutor STRIPS every `data-reveal="solution"` before sending the lesson to the model**, so it never holds the answer key.
- KEPT (the tutor coaches from these): `hint` · `check` (check-your-work / expected output) · `mechanism` (conceptual how-it-works) · `troubleshoot` ("🔧 Problem:" diagnostics) · `catchup` (build-step states / Maker pointers) · `quiz` (knowledge-check answers).

RULES: (1) anything that gives away a graded challenge answer MUST be typed `solution`, or it leaks — **when unsure, type it `solution`** (safe default = withheld). (2) The tutor strips only *tagged* `<details data-reveal="solution">`; **a solution shown as open prose or a bare `<pre>` is NOT stripped and WILL reach the tutor** — to withhold a solution it must live inside a tagged `<details>`. (3) The keep/strip split is a one-line dial in the front-end; nothing is deleted from the lesson — students still see every reveal via click-to-reveal. **(4) THE STRIP LIST IS A WHITELIST (v8.65, S79)** — `solution` is the only type removed, so every KEPT type publishes its contents to the tutor. A finished, fill-nothing-in code block belongs in a `solution` reveal even when the surrounding box is a hint: SPLIT the box, never retype it, so the coaching prose stays reachable and only the answer is withheld. Gated by book_gates v1.9.

**(5) THE GATE IS CONSTRUCT-SCOPED, AND THAT SCOPE IS THE RULE — NOT AN OVERSIGHT (v8.69, S83).**
The §20.1 leak gate walks the `<pre>` blocks inside every `data-challenge` span and nothing else,
because DJ's S79 ruling is that **what we hide is the answers to the challenges**. Three things
follow, and all three were logged as defects before they were measured:
- **The span is the PARSE TREE, never a `rfind('<div')` window.** A construct is bounded two ways
  (§24.6a): ELEMENT-BOUNDED `<div data-challenge>` = its own open..close; HEADING-BOUNDED
  `<h4 data-challenge>` = heading .. first of (next heading at its level or above / next construct /
  parent close). The window only ever got the first case right by accident. `book_gates.py` therefore
  **imports the bounding from `lesson_inventory.py` rather than re-deriving it** — one definition, so
  the two tools cannot disagree, which is the failure §24.6c exists to catch. Signature of the old
  window, reproduced live at S83: ONE injected block in L07 `7.m3` was reported five times, once for
  each of `7.m1`–`7.m5`, because every h4 marker inherited the whole enclosing panel. Four findings
  false, and the true one indistinguishable from them.
- **A mystery has NO line threshold.** §25.10g makes a mystery's bug+fix reveal a `solution`, and its
  planted snippets run 1–2 lines, so the ≥3-statement-line floor that the challenge case needs was
  **the only reason L08 passed this gate for eight sessions** (S80). Any code at all inside a
  `data-kind="bonus-sabotage"` kept reveal fails. *(S86: value swapped from `"mystery"` per the §4.5
  three-family rename; wording otherwise unchanged by DJ ruling. **Parked note for a future session** — this
  is in truth a SABOTAGE rule and always was: Observation reveals (L05–L07) hold no `<pre>` at all, because
  nothing is broken, so the zero-threshold branch never applied to them. The old `"mystery"` value covered
  both families and hid that. **Renaming the value without editing this line would have silently disabled the
  rule** — the comparison would match nothing, every reveal would fall back to the ≥3-line floor, and the
  COVERAGE assert could not catch it because it counts all constructs and tagging 26 more cards makes that
  number go UP. Demonstrated at S86, not argued: same tree, one planted line in a hint in a Sabotage card —
  old value PASSES, new value FAILS.)* **A threshold is not an exemption**, and control-running
  proved the point: retyping `8.m1` back to `hint` PASSES the old gate and FAILS the new one.
- **A kept reveal OUTSIDE every construct is not gated, and that is correct.** Census S83, all sixteen
  lessons: **33 kept reveals hold `<pre>`, and every one of them belongs to no construct** — 31 `check`
  blocks in §6 build steps (L02 8 · L03 8 · L04 4 · L05 2 · L06 9), one L02 §8 `troubleshoot`, and one
  L10 §6 `hint` (*"Stuck? The fix, spelled out"*) that resolves a red build the lesson **told** the
  student to plant. Not one sits in §9 or past §10, where the challenges live. These are teaching
  content: the tutor SHOULD have them. The consequence to hold onto is that **an UNTAGGED challenge
  carrying its answer in a `hint` is invisible to this gate** — §20.2's marker gate is what covers
  that flank, and the two rules only work as a pair.

### 20.2 `data-challenge` ON EVERY CHALLENGE (LOCKED)
Every challenge unit carries, on its anchor element (the card div, the heading, or the label):
- `data-challenge="LL.N"` — lesson.sequence, e.g. `10.3` (matches the Maker convention); this is what the tutor parses.
- `id="challenge-N"` — sequential in-page anchor.
- `data-kind="challenge"` — or `"bonus-practice"` / `"bonus-observation"` / `"bonus-sabotage"` for the three
  §4.5 bonus families (Practice numbered `LL.bN`; Observation and Sabotage both `LL.mN` — see §4.5, the shared
  suffix is deliberate). *(S86: values swapped from `"mystery"`; wording otherwise unchanged by DJ ruling.)* (`"discovery"` is reserved for the in-lesson practice builds if they are ever added to the picker.)
- `data-difficulty="easy|medium|tough|hard|advanced"` — the DOING axis of the split pill (§6.12b). Attribute name retained from the single-pill era so existing tooling does not break.
- `data-grasp="light|moderate|deep"` — the GRASPING axis (§6.12b). Present wherever a split pill is; absent on lessons not yet swept.

**The picker is built by querying `[data-challenge]`** — a challenge WITHOUT the marker silently vanishes from it (the tutor still helps via whole-lesson context, but the student cannot select it). L16's §9 "Project Tiers" are NOT challenges and stay lesson-level (no marker).

### 20.3 INVISIBLE AND MANDATORY ON NEW CONTENT (LOCKED)
`data-reveal` and `data-challenge` are attributes, not content — students see no change. Add them the moment a new reveal or challenge is authored. GATE at close: every `<details>` has a `data-reveal`; every challenge unit has a `data-challenge`. (S58 retrofit baseline: 347 reveals typed, 88 challenges tagged, L01–L15.)

### 20.4 FAVICON ON A PAGES PROJECT SITE (LOCKED)
GitHub Pages *project* sites do NOT auto-discover `/favicon.ico` at a subpath — the browser requests `weymuth.github.io/favicon.ico`, never `weymuth.github.io/zumo/favicon.ico`. So EVERY page needs an explicit `<link rel="icon" href="…favicon.ico">` in its `<head>`, path relative to that page's folder (root page → `favicon.ico`, `lessons/` and `tutor/` pages → `../favicon.ico`). Canvas strips head `<link>`s, so the favicon is a Pages-only benefit — a repo push is enough; a Canvas re-push gains nothing for it.

---

## 21. ROBOT ICON FAMILY (v8.39 — NEW SECTION, S61)

A set of matching robot "chooser" icons — one per robot the fleet might run — built to read as a single professionally designed family. Only the robot and its accent glow color change; frame, composition, lighting, line weight, and framing are identical across all of them. Staged for a future "pick your robot" page; **not yet in the book**.

### 21.1 FRAME SPEC (LOCKED — the shared template)
- Canvas **1254×1254**, rounded square.
- Border **inset 64 px** from each edge · **corner radius 95** · **stroke width 14**.
- ⚠️ **AS-BUILT DEVIATION (S63, DJ ruling "leave them for now"):** every live icon in `images/glowbots/` has a border inset of **10–18 px**, not 64. All five miss the same way (tight cluster, not scattered), which reads as the generator ignoring the inset instruction rather than five separate errors. **64 px remains the spec**; the shipped images are knowingly off it. Re-crop or regenerate when the family is next touched — this is an open debt, not a settled value.
- Panel fill (inside the border) near-black **`#010808`**; dark charcoal background.
- Robot fills **~75–80% of the panel**, centered, slight three-quarter view, never stretched vertically.
- Border = a crisp stroke plus a soft outer bloom, in the robot's accent color.
- No watermark, no Gemini sparkle/star, no extra decorative effects. Glow extends beyond the robot but never overpowers it.

### 21.2 ACCENT GLOW COLORS — CANONICAL IS THE TARGET; AS-BUILT IS RECORDED DRIFT (v8.42, S63)
**DJ ruling S63: the canonical column is the spec.** The as-built column records what is actually in the pushed PNGs. The two differ because the image generator only *approximated* the hex it was given — this is generator drift, **not** a design change, and the canonical value is what any regeneration, CSS glow, or future sibling icon targets.

As-built values are measured from the live `images/glowbots/` borders (median of 51 row samples down the left stroke, S63). Distance is plain RGB euclidean.

| Robot | Canonical (target) | As-built (measured, S63) | Δ |
|---|---|---|---|
| Zumo 32U4 OLED | `#42F5D7` (teal/aqua — intentionally cyan, not green) | `#41FCE8` | 18 |
| 3Pi+ 32U4 OLED | `#46F56C` (bright green) | `#7DF565` | **55** |
| ROMI 32U4 | `#FF4FBF` (magenta/pink) | `#F83D9C` | 40 |
| Balboa 32U4 | `#9A5BFF` (purple) | `#AE4EFA` | 24 |
| Zircon (soccer) | `#FF8A00` (orange) | `#FB7404` | 23 |

**3Pi+ is the outlier at Δ55** — visibly lighter and yellower than the canonical green. If the family is ever regenerated, 3Pi+ is the one to check first. The S61 "sampled" column (`#48D4D4`, `#3DAA54`, …) is retired: it was measured off the *first* uploads, which were replaced.

### 21.3 BUILD METHOD — TWO OUTPUTS, TWO METHODS (v8.42, S63 — SUPERSEDES the frame-swap-only rule)
**DJ ruling S63: the S61 "NEVER separate the robot from its glow" prohibition is lifted.** It was written from a failed attempt, not a working one. S63 separated robot+glow from the frame on all five robots — including the two §21.4 predicted would defeat it — and the cut succeeded. The family now has **two outputs**, each with its own method:

**(a) BORDERED — for buttons. Frame-swap.** Unchanged from S61: keep robot and glow together, crop just inside the source border ring, map into the panel, draw the shared border on top. The border ring supplies a hard silhouette that survives downsampling, which is why **buttons are always bordered** (DJ ruling S63).

**(b) GLOW — for images. Extract-and-cut.** Crop inside the border to drop the frame, then cut the robot+glow to transparency. Two findings make this work where S61 assumed it could not:

1. **Use edge-connected flood fill, never a global brightness threshold.** Background = dark **AND** reachable from the crop edge. Interior dark pixels are then untouchable by construction — Zircon's black PCB and the gaps in Balboa's roll cage survive because they never connect to the outside. This is the specific failure §21.4 described, and connectivity is the fix.
2. **Cut the falloff; do not preserve it.** The glow is painted *additively on black*, so its outer falloff **is** black. Keeping it as soft alpha reproduces it as a grey haze that is invisible on a dark background and reads as a dirty cloud on white. Keep alpha only within **~2 px of the solid body** and zero everything beyond.

**GLOW FLOOR: never export below 128 px** (DJ ruling S63). Downsampling re-hardens the cut edge into opaque pixels, and open-frame robots collapse into mush. Sizes are full · 256 · 128. For anything smaller, use the bordered set.

**QA RULE — CHECK ON WHITE.** Every glow defect found in S63 was invisible on a dark background and obvious on a light one. A dark-background QA sheet proves nothing about a transparent cutout.

### 21.4 WHY SOLID vs OPEN/DARK ROBOTS BEHAVE DIFFERENTLY (amended S63)
Solid, bright-bodied robots (Zumo tank body, 3Pi+ white disc) seal their own interior and lift off a black background under almost any method. Dark-bodied (Zircon PCB disc) and open-frame (Balboa roll cage) robots defeat a **brightness-threshold** cut — black-on-black is invisible to it, so interiors get eaten and open structure leaks. **They do not defeat an edge-connected cut** (21.3b), which is a connectivity test rather than a brightness test. The S61 conclusion that these robots resist extraction was a property of the method, not the robots.

**Balboa remains the hard case for a different reason: it is the only portrait robot** (bounding box ~1014×1154; every sibling is landscape). Forced into a square tile its height sets the scale, so it shrinks harder and leaves dead space at the sides. This is why the 128 px floor exists.

### 21.5 HARDWARE ACCURACY
Represent the real hardware; do not invent or simplify parts.
- **Zumo** — OLED version (Zumo 32U4 OLED).
- **3Pi+** — white chassis, correct PCB layout, OLED display.
- **ROMI** — correct gripper configuration + wheel geometry.
- **Balboa** — balancing frame, large side wheels, accurate PCB placement.
- **Zircon** — Teensy **4.1** (never 4.0; the 4.1 is noticeably longer), correct omni-wheel layout, circular PCB arrangement.

### 21.6 THE BORDERLESS "MARK"
A no-frame transparent cutout also exists per robot. The landing-page Textbook tile uses `Zumo_Robot_Mark.png` (repo root `images/`, live since S61, displayed at 52 px). The full transparent family now lives in `images/glowbots/` as the **glow** set (21.7). **Buttons use the bordered icon** (DJ ruling S63) — a transparent cutout has no silhouette at button size.

### 21.7 LIVE FILES — `images/glowbots/` (v8.42, S63)
Pushed S63, commit `12867ea`. **42 files**, flat, no subfolders.

| Set | Sizes | Count | Mode | Use |
|---|---|---|---|---|
| `{Robot}_bordered_{1254,256,128,64,52}.png` | 5 | 25 | RGB | **buttons** |
| `{Robot}_glow_{full,256,128}.png` | 3 | 15 | RGBA | **images** |
| `QA_extraction_check.png`, `QA_size_sheet.png` | — | 2 | RGB | working contact sheets, not assets |

`{Robot}` ∈ `Zumo` · `3Pi` · `Romi` · `Balboa` · `Zircon`. Glow full-size is **1186²** (1254 less the 34 px frame crop), not 1254².

**Uniformity is verified and must be maintained.** All five glow cutouts measure mean edge distance **1.28–1.32 px**, p95 **2.00**, halo reach **0–1 px**, and **zero opaque pixels on any edge** at every size. A new sibling icon must match this or it will visibly out-glow the family. The three tight cuts (Zumo, Romi, Zircon) were done by DJ in Photoshop and are the reference; 3Pi+ and Balboa were tightened to match (they had carried 57 px and 39 px of halo).

**Wanting a bigger glow later is recoverable** — apply it as a CSS drop-shadow on the tight PNG rather than baking it back into the image. That keeps the family uniform and tunable.

**Open debts on this family:** the 21.1 inset deviation · filenames are S63 working names, not a ruled convention · the `QA_*` sheets are committed alongside real assets and could be `git rm`'d.

---

## 22. TERMINAL OUTPUT COLOR CANON (v8.45 — NEW SECTION, S65)

Simulated PlatformIO console output is a **different medium** from a C++ code block, and it gets its own two-color rule. A student reads a terminal block to answer one question — *did it work?* — and the book should answer that question the same way the screen does, at a glance, before any words are read.

### 22.1 THE TWO COLORS (LOCKED)

| Meaning | Color | Applies to |
|---|---|---|
| **SUCCESS** | `#6a9955` | `[SUCCESS]` in a simulated build/upload result |
| **ERROR** | `#f14c4c` | the diagnostic line of a compiler/linker message |

**`#6a9955` is DJ-ruled (S65) and is deliberately the same green the code blocks use for `//` comments.** The real PlatformIO terminal renders `[SUCCESS]` in a brighter green (nearer `#23d18b`), but the book's existing L01 upload block already used `#6a9955`, and DJ ruled to keep it as the single canonical success green rather than introduce a second one. **Do not "correct" it toward the terminal's true green.** The color carrying two meanings across two block types is accepted: context disambiguates completely, because a comment never appears in console output and `[SUCCESS]` never appears in source.

`#f14c4c` is VS Code's dark-terminal ANSI bright-red — what the student actually sees when a build fails.

### 22.2 COLOR THE DIAGNOSTIC, NOT THE WHOLE BLOCK

A compiler message is three different things stacked, and only the first is an error:

```
src/main.cpp:9:1: error: expected ';' before 'ledYellow'    <- RED
 ledYellow(1);                                              <- plain #e8e8e8
 ^~~~~~~~~                                                  <- plain #e8e8e8
```

The **source echo** and the **caret marker** stay plain `#e8e8e8`. That is how the real terminal renders them, and it is also the pedagogy: the echoed line is the student's own code, and the whole point of L02's "the compiler points at the line AFTER the mistake" rule is that they look at that line and judge it themselves. Painting it red pre-judges it — and in the very case the rule is teaching, the echoed line is **innocent**.

Lines that take the red: `file:line:col: error:` · bare `error:` / `fatal error:` · `undefined reference to` · `collect2:` · `[FAILED]`.

### 22.3 SCOPE — TERMINAL BLOCKS ONLY

The rule applies **only** to `<pre>` blocks that simulate console output. It does **not** apply to:

- **Prose mentions.** "Look for SUCCESS in the terminal" stays plain text. Thirteen such mentions exist across L01–L06 and are correct as they are; prose does not wear terminal colors.
- **Inline `<code>` chips.** `SUCCESS` referenced as an inline token keeps the standard grey chip.
- **C++ source blocks.** A block containing the *word* error (a variable named `error`, a comment about errors, the P-control `error` term) is source, not output. **Detect terminal blocks by their console markers** — `error:` with the colon, `undefined reference`, `Writing |`, `Verifying |`, `[SUCCESS]`, `[FAILED]` — never by the bare word.
- **Pseudocode.** L12's `report SUCCESS (return true)` is plan-language inside a pseudocode block. Left alone.

Of 71 blocks book-wide containing the string "error", exactly **11** are genuine console output. The word alone is a false-positive generator — this is §11's audit-false-positive discipline applied to color.

### 22.4 AS APPLIED (S65)

Two `[SUCCESS]` instances greened (both L01 — the build-result block was plain, the upload-result block was already `#6a9955` and set the precedent). Fourteen diagnostic lines reddened across 11 blocks: L02 ×5, L07 ×9. Applied at L01 v03.6.2 · L02 v02.12.2 · L07 v04.5.1 — all minor bumps, visible banners unchanged per §5b.

**Open:** L03, L04, L05, L08, L09, L11, L12, L14, L15, L16 contain blocks matching the loose "error" grep but none matched the strict console-marker test. If a future depth pass adds real console output to any of them, it takes these colors.

---

## 23. GOING DEEPER — THE OPTIONAL PAGE (v8.45 — NEW SECTION, S65)

`going_deeper.html` at repo root. A standalone optional-reading page for the "but *why* does it work like
that?" questions the lessons deliberately postpone so students can get the robot moving.

### 23.1 WHAT IT IS AND IS NOT
- **Outside the 16-lesson numbering.** It is NOT Lesson 17. It has no lesson number, no `data-challenge`
  markers, no challenge cards, and **no entry in the Maker registry**.
- **Nothing on it is assessed.** Not on a milestone, a reading quiz, or an exit ticket. The page says so in
  its own opening paragraph, and that paragraph is load-bearing — it is what keeps the page from competing
  with the chapters.
- Linked from `index.html` in the **tools row** (next to Project Maker / Timer / AI Tutor), never from the
  lesson grid.
- Own version line: `<!-- Going Deeper version: vNN.NN.NN -->`, same three-digit scheme as a lesson.

### 23.2 THE ANCHOR RULE (DJ ruling S65: "focus of content needs to be the chapters")
**Every entry must open from something a chapter already teaches, and close with a "Back to the book" line
naming the lessons it came from.** An entry that cannot name its anchor does not belong on the page.

This rule is what excludes most general C++ material. Anonymous namespaces, rvalue references, RAII,
`constexpr`/`consteval`, `enum class`, lambdas, `std::string`, and desktop UART driver design were all
offered and all **rejected S65** — none appears in any Zumo program, and a student who chases them lands in
desktop C++ that will not compile on an AVR. The page must not become a place where the book competes with
itself for attention.

### 23.3 CHECK FOR DUPLICATION BEFORE WRITING AN ENTRY
An entry that re-teaches what a lesson already covers is worse than no entry: it splits the canon. **S65
drafted a fixed-point entry as if the topic were new and caught it only on audit — L12 §8A.3 already teaches
fixed point properly**, including the no-FPU reason and the 2^29 gyro unit. The entry was rewritten to build
on L12 and cite it. Run the same audit on every new entry: grep the book for the entry's key terms first.

### 23.4 AS BUILT (S65, v01.0.0)
Six collapsible `<details>` entries, dark theme matching `index.html`, VS Code Dark+ in code blocks:
ASCII/binary/baud (L02) · what `F()` really does — Harvard vs von Neumann (L02/L12/L16) · the four-stage
build chain (L01/L12/L16) · translation units and why eight files (L07) · fixed point applied to Kp
(L08/L12/L15) · class vs instance (L02). Collapsed by default, so the page does not read as a 17th chapter.

---

## 24. BOOK GATES — THE STANDING CONSISTENCY TOOL (v8.48–v8.49 — NEW SECTION, S65)

**`book_gates.py` (repo root, v1.0) runs every machine-checkable Bible rule against the whole book in one
pass.** Run it at session open (health check, like `pill_sweep.py`) and before EVERY delivery. A delivery
that has not passed the gates is incomplete — same class as §12.6's incomplete push.

### 24.1 WHY IT EXISTS
Three times in one session (S65), a fix DJ requested was applied to the named instance while the same defect
survived elsewhere: text labels fixed but not timer widgets; the banner VERSION fixed while its DATE stayed
wrong in the same string; a byte count corrected in prose but initially asserted from memory. Each time DJ
had to notice and re-ask. The failure mode is not carelessness on any single edit — it is **fixing the
instance instead of the class**. A gate encodes the class once, permanently, and removes the dependence on
any one session remembering to check.

### 24.2 THE RULE
**When a rule is canonized, its gate is written in the same session.** A Bible rule with no gate is a rule
that only holds where someone happened to look. Current gates: §5b version + date agreement · §22 terminal
colors · §4.1/4.2/4.3 construct names, marker uniqueness, picker-label uniqueness · §6.12b pill parity ·
tag balance across every site file · timer well-formedness · index link resolution · going_deeper link canon.

### 24.3 GATE THE WHOLE FIELD, NOT THE CAPTURED GROUP
The June/July date slipped through a "passing" §5b check because the regex captured only the version digits
out of a string that also carried a date. **A gate must compare the entire field it claims to guard, not the
substring that was easiest to capture.** When adding a gate, ask what else lives in the same string.

### 24.4 A COMPUTED CLAIM IS VERIFIED BY COMPUTATION
S65 published "17 characters, so 18 bytes" for a 16-character string — the one number that session that was
asserted from memory instead of computed, in a section whose entire point is teaching students to count
bytes. **Any arithmetic, count, or measurement that appears in student-facing prose is produced by running
the computation, never by recall** — the same discipline §11 already applies to version numbers ("grep the
file") extended to numbers of every kind.

### 24.5 THE DEPTH AUDIT + THE ROLLING HUMAN READ (v8.49 — S65, DJ ruling)

DJ's diagnosis of L02 — "lots of brief info, but not a lot of depth" — generalizes and now has a standing
process. Two layers:

**Machine layer (`book_gates.py` + the depth scan).** Used-vs-taught construct ratios, substance profile
(LEARN boxes / KEY terms / words-per-section), thin-section detection, cross-lesson promise verification,
arithmetic verification. Findings live in `DEPTH_AUDIT_S65.md` (repo root). §11 discipline applies doubly:
the S65 scan's bitwise/pointer hits were 100% false positives (progress bars, `<<<` markers, pseudocode
arrows), and its word-count detector flagged sections whose depth legitimately lives in a neighbor.
**A scan finding is a candidate until a human reads the section.**

**Human layer (the rolling read — DJ is doing this personally).** Every lesson gets a start-to-finish read
asking what no grep can: does each heading keep its promise; is each idea given a reason before a rule; could
a student who reads only this lesson do its challenges. Additionally, any lesson a session substantially
edits gets the read in that same session — all three S65 accuracy finds were in freshly-edited content, zero
in untouched content.

**Standing structural finding (S65, verified):** the teaching apparatus disappears at L11 — L11–L16 carry
ZERO 📖 LEARN boxes and near-zero 🔑 KEY terms while teaching the book's hardest material. Mostly a marking
fix (promote existing strong prose into the apparatus), queued as its own arc. L14 profiles thinnest
book-wide and goes first in the read.

---

### 24.6 STRUCTURE IS VERIFIED BY PARSE, NOT BY COUNT (v8.50 — S68, DJ ruling)

**A count-based tag check can be satisfied BY the bug it is supposed to catch.** Eight lessons shipped with
the Image Index panel's closing `</div>` in the wrong place; in six of them (L01, L12–L16) it sat *after*
`</html>`. Open/close counts balanced exactly — because the orphaned close balanced the panel that was never
closed. The `tag balance` gate returned PASS on every run for the entire life of the defect. The check was
arithmetically correct and structurally blind.

**Provenance (git-verified S68, not recalled):** L01 carried it from its first tracked commit — original
hand-authoring, never introduced by a session. L12–L16 acquired it in a *single* commit, `94acc10` "Session 35
Massive Update", 2026-07-14: the §6.5 conversion from flat `<h2>` headings to boxed sections. That transform is
**stateful** — each heading emits `</div>` to close the previous panel, then opens its own — so the final panel
in the file has no following heading to close it, and its terminator was parked at EOF. One off-by-one at the
tail of a stateful conversion, replicated five times because it was one script. It then survived 28 later
commits on L01 and 9–13 on the others.

**THE RULE: any gate asserting document structure runs a real parser and compares the resulting tree to the
intended shape.** Counting is evidence about a file; parsing is evidence about a document. `book_gates.py` v1.2
carries `structure: HTML parses to the intended shape` — a tag-stack parse of every site file, reporting the
swallowed open AND the stray close with line numbers, plus a hard assert that nothing follows `</html>`.
This is §24.3 ("gate the whole field, not the captured group") applied to structure: the field is the tree, the
captured group was the count.

**24.6a A PARSER IS NECESSARY AND NOT SUFFICIENT.** L06 and L07 parsed *clean* and were still wrong — well-formed
HTML with the lesson footer sealed inside the Image Index box, because the close was present but late. No parser
can see that: the document is valid, the meaning is not. Structural correctness therefore needs a second,
**semantic** assertion about what belongs inside which container. Gate: `structure: end matter sits outside the
section panel`. **When a structural gate is written, ask what a well-formed-but-wrong version would look like and
gate that too.**

**24.6b CONTROL-RUN EVERY NEW GATE AGAINST THE UNFIXED SOURCE.** A gate that has only ever been run against
corrected files is untested. Both S68 gates were run against the pre-fix clone and FAILED there (12 parse
problems across 6 files; 2 end-matter violations in L06/L07) before being trusted on the fixed set. A gate that
passes everywhere it has been pointed has proved nothing.

**24.6c AN AUDIT GREP IS AN UNGATED GATE — CONTROL-RUN IT TOO.** (v8.51 — S69, DJ ruling) §24.6b binds gates,
which are versioned, reviewed and reused. An ad-hoc audit grep is a single-use gate that is none of those
things, and every S69 false positive came through that hole. Two, both in one session, both reported to DJ as
findings before being checked:

- **Inferred structure from a proxy string.** The timer iframes carry `label=Step+2`, so the audit concluded L02
  timed its *build steps*. The timers are attached to **TRY IT cards**; the label names the step the card belongs
  to. That produced "22 untimed build steps in L03/L04" and a proposal to insert 22 timers onto plain build prose
  — a device that exists nowhere in the book. DJ's confirmation is the only thing that stopped it.
- **Case-sensitivity.** `grep -oE "Step [0-9]+"` matched only the mixed-case text inside card headings; L02 writes
  its build steps as `STEP N:`. Nine steps were found where there are **eleven**, and the gap between card ids and
  step numbers was then reported as label "drift". All 11 labels were correct: `STEP 7` legitimately carries two
  TRY IT cards (`2.t7` Advanced, untimed; `2.t8` timed), so the duplicate "Step 7" is the truth.

**THE RULE, four parts.** (1) **Control-run the grep** against a case whose answer is independently visible —
read one lesson's structure by eye and confirm the count matches — *before* the number becomes a finding.
(2) **Never infer structure from label text**: check what element the matched string is attached to, not what it
says. A label describes; only the DOM position decides. (3) **Case-insensitive by default**, because the book's
own vocabulary varies by lesson and by era (`STEP`/`Step`, `CONFIGURATION`/`CONSTANTS`, "Coach's Tip" vs the bare
§6.6a labels) — a case-sensitive audit silently reports on a subset. (4) **Report findings as VERIFIED or
SUSPECTED**, never in one voice; a handoff or queue item enters the next session as SUSPECTED and stays there
until independently re-checked. S69 also reported the S68 queue's GRAPHIC 5.5 cone-angle suspicion as though it
were a defect; it was clean (tick bearings −90.0/0.0/+90.0, already matching the corrected 5.1).

This extends §11 ("a prose-keyword grep reports candidates, not verdicts", v8.36.2) from prose greps to
**structural** ones, and adds the reporting format. Note the standing pressure it works against: a five-item
audit reads as more valuable than a two-item one, so weak signals get promoted to lengthen the list. DJ's rule
governs — **a wrong finding costs 3× a blank one**, and an audit's length is not its worth.


### 24.7 SEEING THE RENDERED PAGE FROM THE SANDBOX (v8.74 — S86, DJ ruling)

The rendered Pages site has been an unclearable debt for three sessions: `weymuth.github.io` is not on the
sandbox egress allowlist (`x-deny-reason: host_not_allowed`), so every "did the banner land right on the
actual page?" item could only ever close on DJ's screen. **It can now close in the sandbox, with caveats.**

**`wkhtmltoimage` is installed** and renders a local lesson to PNG, which can then be viewed directly. The
lesson HTML in a fresh clone is byte-identical to what Pages serves, so the input is right; only the engine
differs.

**THE FAILURE THAT ALMOST SHIPPED A FALSE VERIFICATION.** A whole-page render of these lessons produces a
canvas **38,000–65,000 px tall whose tail is PURE BLACK** — wkhtmltoimage allocates the full height and stops
painting partway. Measured S86, bottom quarter: **L04 100% · L05 100% · L12 100% · L14 81% · L13 62%.** It
does not error, the exit code is unremarkable, the PNG opens fine, and the top of the image looks perfect.
Three of eight banners under inspection sat inside that dead zone, and one banner reported as *"colour NOT
FOUND"* was simply in the unpainted region — **an absence produced by the instrument reads exactly like an
absence in the book.**

**THE METHOD:**
1. **Never read a whole-page render of a lesson.** Window it:
   `wkhtmltoimage --enable-local-file-access --width 1100 --crop-y N --crop-h 620 lessons/Lesson_NN.html out.png`
   Windowed renders come back **0% black** at every depth tested.
2. **Locate the target by its own colour, not by an estimated offset** — e.g. the §6.8 PART banners are
   `#3498db` / `#3a7d5c` / `#c45d76` / `#9b6a9e` (note the attribute is `background-color`, NOT `background`).
   If a colour is missing from a whole-page render, suspect the dead zone before suspecting the book, and
   re-find it with a coarse windowed sweep.
3. **PROVE THE WINDOW CONTAINS THE TARGET BEFORE READING IT** — assert the expected colour is present and the
   black fraction is near zero. This is §24.6b applied to an image: *assert the injection landed in the shape
   you intended*, where the "injection" is the crop.

**WHAT A RENDER IS AND IS NOT.** It is a **STRONG LEAD, NOT A CLEARED ITEM.** wkhtmltoimage is WebKit and
older than Chrome, so it is reliable for structure, seating, colour and box nesting — which is what the §6.8
PART-divider and §6.8a fence questions actually are — and unreliable for anything depending on modern CSS.
**Remote images render as gaps**, because the image URLs point at the very host that is blocked. A render
does not retire a DJ eyeball item; it raises or lowers the prior.

**GATE: NONE, DELIBERATELY.** This is a review-process rule of the same class as §24.6b and §24.6c — there is
nothing in the book to assert against. §24.2 requires a gate for a rule about book CONTENT; a rule about how
we look at the book is enforced by being written down where the next session reads it.


### 24.8 CAN THE INSTRUMENT DISTINGUISH THE TWO ANSWERS? (v8.75 — S86, DJ ruling)

§24.7 is one instance of a larger rule, and the larger rule is the more valuable half. S86 produced **five**
moments where something looked settled and was not, and **every one was a failure of the instrument, not of
the book** — caught only by turning around and checking the tool rather than reading its output.

**THE TEST, before believing any tool's report:**

> **If the answer were the OPPOSITE, would this instrument look different?**

If it would not, the report is **not evidence** — it is the instrument's silence, and silence is compatible
with both answers. This is the one question that would have caught all five:

| # | The instrument said | It could not distinguish | What it actually was |
|---|---|---|---|
| 1 | `grep data-kind` → `book_gates.py` 0 hits | "not a consumer" vs "consumes the PARSED value" | The critical consumer, via `lesson_inventory.build()` |
| 2 | Injected control → gate still PASSED | "gate is broken" vs "injection missed its shape" | Planted in a `solution` reveal, which §20.1 ignores by design |
| 3 | A line printed under `--- ANOMALIES ---` | "a standing lead" vs "an unconditional header" | The Brain Check NORM line, correct and always printed |
| 4 | Render → no plum pixels found | "banner absent/wrong" vs "region never painted" | Whole-page black tail (§24.7) |
| 5 | `api.github.com` → HTTP 403 | "proxy denied it" vs "origin denied it" | GitHub's own rate limit; no `x-deny-reason` header |

**#5 WAS COMMITTED ONE MESSAGE AFTER §24.7 WAS WRITTEN**, by the same author, about the same class of error.
Knowing the rule does not confer immunity; running the test does. That is why this is its own section and not
a footnote.

**THE THREE RECURRING SHAPES:**
1. **A NAME-SCOPED SEARCH MISSES VALUE-SCOPED USE.** Grepping an attribute string does not find tools that
   consume the parsed field. Sweep the field name too. A grep hit in an unrelated namespace also reads as a
   consumer — `newproject.html`'s `mystery` hits were Maker download ids (§4.5).
2. **AN ABSENCE FROM AN INSTRUMENT IS NOT AN ABSENCE IN THE BOOK.** Nothing-found is the single most
   dangerous reading, because a broken instrument and a clean book produce identical output. Prove the
   instrument CAN see the thing — control-run against a case known to contain it.
3. **A CONTAINER IS NOT ITS CONTENTS.** A heading, a status code, or an output section names a category; it
   does not certify that what sits under it belongs to that category. Read the code, or the reason header,
   that produced it.

**COST ASYMMETRY.** Running the test costs one command. Skipping it cost, in S86 alone: a nearly-shipped
false verification of eight banners, a wrong "we should re-open this" on a closed item, and a wrong report to
DJ that his allowlist had narrowed. DJ's standing rule governs — **a wrong answer is 3× worse than a blank
one** — and an instrument you did not check is how wrong answers arrive wearing evidence.

**GATE: NONE, DELIBERATELY** — same class as §24.6b, §24.6c and §24.7. There is nothing in the book to assert
against; this governs the session, not the artifact.

---

### 24.9 A GATE'S COVERAGE SET IS PART OF THE GATE (v8.77 — S89, DJ ruling)

§24.6b says control-run a gate against the unfixed source. §24.8 asks whether the instrument could
distinguish the two answers. This subsection covers the case where the instrument is fine and is
**pointed slightly to the left of the thing it watches**.

**THE COVERAGE SET IS STATED AND ASSERTED, NEVER INHERITED.** Both §5b gates iterated `files` — the
16 lessons — while §25.6 iterated 17. `going_deeper.html` was outside the version gate entirely, and
that is the one file that drifted: a visible `Version 01.0` against a hidden `v01.1.0`, live and
unnoticed. The gate's comparison logic was correct the whole time. It simply never ran on the
defect. **A gate that passes because it never looked is indistinguishable, in its output, from a
gate that passes because the condition holds.** Every gate now names its population explicitly and
asserts the count, so the set cannot silently shrink.

**A GATE DELIBERATELY RELIED UPON FOR A PROPERTY IT DOES NOT CHECK IS LOAD-BEARING ON AN ACCIDENT.**
This is the harder half. At S70 the footer version moved into an HTML comment, and the v8.53 entry
recorded the reasoning in the open: the two-homes gate *"needed no edit — it greps raw source, and
raw source includes comments, so a comment satisfies it exactly as a rendered banner did."* The gate
was named for visibility and had no notion of it. Nothing was hidden and nothing was careless; the
blindness was seen, judged harmless, and built upon — for nineteen sessions. **When a gate's name
claims a property its code does not test, either the code learns the property or the name stops
claiming it. Do not build on the gap.** Corollary for placement and visibility checks: **strip what
the reader cannot see before matching.**

**A RULE RESTATED IN TWO SECTIONS IS TWO RULES.** §5b was corrected at v8.53 and §9's restatement of
it was not, so the Bible contradicted itself until S89 and the S89 handoff cited the wrong section
as a result. When superseding a rule, grep this file for its other statements.

**A CONFORMANCE STAMP MUST NAME A DOCUMENT THAT EXISTS.** `ZUMO Callout Standard v1.0 Applied` sat in
17 files, asserted by a gate, naming nothing readable — a string that existed because the gate
asserted it and was asserted because it existed. Retired S89. A stamp is a claim about a document;
with no document it is a claim about itself.

*Ungated by design, like §24.6b/§24.6c/§24.7/§24.8 — there is nothing in the book to assert against.*

---

### 24.10 THE PARSER IS THE DEFAULT INSTRUMENT; GREP READS ONE KNOWN LINE (v8.78 — S91, DJ ruling)

**DJ: *"Grep has caused most of the issues we have faced in the book."*** He is right, and the
record is one-sided. Every audit failure this canon has recorded is a TEXT match standing in
for a STRUCTURAL question:

- `SECTION 8` substring-matched `SECTION 8A` and invented a duplicate fence (§24.6c, S82).
- A matcher requiring the `=` wrapper was blind in five lessons and reported nine real gaps
  as one (§6.8a, S82).
- `Step [0-9]+` was case-sensitive, missed `STEP N:`, and manufactured a drift that did not
  exist (§24.6c, S69).
- A timer label was read as evidence of structure and nearly put 22 timers onto plain prose
  (§24.6c, S69).
- Gate 30's substring test for `#6c757d` passed a GRADIENT containing `#6c757d` for its
  entire life (§4.5a, S87).
- S91: a case-insensitive search for THE WALL matched the prose words *the wall* and placed
  the construct in five lessons it is absent from — the exact reverse of the truth, caught
  only because the count contradicted a prior session.

**The rule.**

1. **A structural question goes to a parser.** Counts, censuses, inventories, placement,
   nesting, "how many lessons carry X", "which construct owns this reveal" — these are
   `lesson_inventory.py`'s job. Where it cannot answer, EXTEND IT; do not grep around it.
2. **Grep is legal for exactly one thing: reading a single line whose format is fixed and
   known** — a version banner, a stamp. This use has never failed us, and §12.6's
   file-is-source-of-truth rule depends on it.
3. **Every count presented to DJ names the instrument that produced it.** A number with no
   named source is a lead, not a finding.

**Why this is not a fourth restatement.** §11, §24.6a and §24.6c already say a scan finding is
a candidate. They did not stop it — including in the session that canonized this entry. **A rule
that must be remembered at the moment of temptation is not working.** What actually closed these
defects was TOOLING: `lesson_inventory.py`, the DOM traversal that found the §5 anchor
displacement, the stack-based depth walk that catches trapped PART banners. This entry therefore
changes what is REACHED FOR, not what must be recalled — the parser is the default and grep is
the narrow exception, rather than the reverse.

*Ungated by design, like §24.6b/§24.6c/§24.7/§24.8 — there is nothing in the book to assert
against. The check is whether a presented number can name its parser.*


---

*End of ZUMO SUPER BIBLE v8.*

---

## 25. THE EXIT-REGION CONSTRUCTS, THE READING QUIZ & PAGE CANON (v8.53 — NEW SECTION, S70)

### 25.1 WHY IT EXISTS

A §10 audit found **six differently-named written-response blocks** doing overlapping jobs, spread unevenly across the book, with **L13 and L15 carrying none at all**. Two of them shared the name *STOP & PROCESS* while running opposite mechanisms: L01/L02's was *write it in your notebook*, L03's was *answer from your head, then click to compare*. Same label, different pedagogy. This is the §4.1 disease — one name, several meanings — reappearing in the exit region.

DJ ruled **four constructs**, each with one job.

### 25.2 THE FOUR CONSTRUCTS

| Construct | Where | Count | Job | Reveals? |
|---|---|---|---|---|
| 🧠 **Mental Knowledge Check** | last seam before hands-on work (before §6 Build It in L01) | **3–5** | did you READ | yes — `data-reveal="quiz"` |
| 🧠 **Knowledge Check** | §10 | # (scales with the lesson) | did you UNDERSTAND WHAT YOU BUILT | yes |
| ☐ **Technical Skills — Can you…?** | §10 | = the lesson's objectives | self-audit | no |
| ✍️ **Reflection** | §10 | 1–3 | feeds the Notebook/TDP | **no — never** |

**THE SPLIT IS RECALL vs APPLY, NOT SECTION NUMBER.** Mental asks the student to *name it, define it, state it*. Knowledge Check asks them to *predict it, trace it, explain why*. This rule was chosen because the reading is not contiguous — L01 runs read(§1–3) → do(§4 Install) → read(§5) → do(§6+), so any placement rule keyed to section numbers breaks on the first lesson. **A hands-on section in the middle does not mean the reading has ended** (S70: `setup()`/`loop()` was wrongly excluded from L01's Mental block on exactly that error; §5 is reading, and in a flipped classroom the student reads the whole lesson the night before).

**EVERY ITEM NAMES ITS §.** `(§3.3)`, `(§5.3, §5.4)`. This is not new — L03's live quiz block already does it and tells students the section number is where to re-read. §25 makes it canon. It also gives the bell-ringer its map: a missed item points at a section.

**RETIRED NAMES** (§4.1 class, add to the `no retired construct names` gate as each lesson converts): *STOP & PROCESS* (both senses) · *Conceptual Understanding* · *Check Your Understanding* · *Reflection Questions* · *Explain It in Writing*.

### 25.3 THE READING QUIZ (Canvas)

The flipped design gates build time on a pre-class Canvas quiz — short, auto-graded, **one attempt**, opens before class and locks at the bell, worth 20%. It is a **soft gate**: fail it and you re-read and retake, you are never locked out of the course. **The quizzes do not exist yet** (Bible line 733 read *quiz feature deferred*); the Mental Knowledge Check is their source.

**DESIGN RULE — EASY IF YOU READ, HARD IF YOU DIDN'T (DJ, S70).** Every quiz item must be answerable from **a single stated fact in the prose**, and must name the § it came from. Retrieval, not inference. If answering needs the robot in hand or a chain of reasoning, it belongs in the Knowledge Check or the Reflection, not the quiz.

**CLOSED BOOK, SO ITEMS SHIP IN PAIRS.** DJ ruled against open-book — open book means they look it up instead of reading the night before. So each item exists twice: the **rehearsal** in the lesson with its answer revealed, and a **variant** in Canvas testing the same fact in different words. Scale: 3–5 × 16 = **48–80 pairs.**

**AUTHOR THE VARIANT INLINE, WHILE THE § IS OPEN.** The variant stem is written as an HTML comment directly above its rehearsal item:
```
<!-- QUIZVARIANT 1.5: One of the two functions runs once and the other runs forever. Which is which?
     (answer: setup() once at power-on/reset; loop() forever afterward) -->
```
Costs nothing now, harvestable by script later. **Book first, Canvas after** (DJ ruling) — § numbers move while the book is under construction, and a quiz item that names its § would be authored against a moving target.

### 25.4 WARM-UPS AND THE SPIRAL

**Warm-ups run L02–L16 — fifteen lessons.** L01 cannot host one: it is the install lesson, there is no prior lesson to reinforce and no toolchain until §4.

The construct (as built in L02, and the strongest in the book): timed micro-fixes on already-working code — *work independently, no asking for help, limited time, it is supposed to be hard*. The hint unlocks only **after** time is up and ends by asking how you could have known without it. One reusable sandbox folder, not a copy per task.

**SPIRALS LIVE IN WARM-UPS AND CHALLENGES** (DJ ruling S70). Census at S70: 27 markers, of which **5 name no lesson** (L04 §8A.6–8A.9 and one L03 marker are *within-lesson* build-ons wearing the 🔁) — so **22 true cross-lesson spirals**. Coverage, not volume, is the defect:

- **Never spiraled back to: L01, L11, L12, L13, L14, L15, L16.** L11–L15 are thin partly by geometry; **L01 and L07/L08/L09 are the real gap** — the 8-file architecture, P-control and the state machine are the three hardest ⭐ demo lessons and each is reinforced exactly once.
- Well covered: L03 ×5 · L05 ×4 · L06 ×4 · L02 ×3 · L04 ×3. Reach runs 1–8 lessons back, median ~3.

**THE AIMING RULE:** each lesson's three warm-ups reinforce **(1)** the previous lesson, **(2)** something 3–6 back, **(3)** something from the under-cited set. Three × fifteen = **45 slots against 22 today**, so the fix needs no new challenges.

**Live marker wording is `🔁 Builds on:`** — "Spiraled skills" returns zero book-wide and is retired. **OPEN:** the 🔁 currently does two jobs (cross-lesson spiral vs within-lesson build-on); until they are separated the spiral count is inflated ~18% and the coverage matrix cannot be trusted.

### 25.5 OBJECTIVES COME FROM THE CHECKLIST

DJ ruling S70, inverting the obvious direction: **§2 Objectives are rewritten to match the §10 Technical Skills checklist**, not the other way round. The checklists are concrete and observable ("Can you calculate COUNTS_PER_CM"); objectives drift abstract. Checklist length currently runs 1–13 across the book because nothing anchors it — after this pass §2 is the anchor and the two can never disagree. **Not yet applied.**

### 25.6 HEADER & FOOTER — ALL 17 PAGES  (hidden banner retired v8.77, S89)

Seventeen pages: 16 lessons + `going_deeper.html`. The §25.6 gate formerly also asserted a `BUILD BANNER` and a `ZUMO Callout Standard v1.0 Applied` string in all 17; **both assertions were removed at S89 with the banner itself** (book_gates v1.21). Verified S70 by **markup-skeleton hash** (tags + inline styles, text stripped) — header `4fdedafb` ×17, footer `aff5311e` ×17.

**HEADER — five lines**, the hero block, `linear-gradient(to bottom, #1a5276 0%, #2e86ab 100%)`, white:
```
LESSON 11
Time Lies, Distance Doesn't
Encoder-Based Gap Crossing
Zumo 32U4 Robotics • PlatformIO Edition
Version 02.7 — July 2026
```

**FOOTER — four lines.** The header's shape with the version line replaced by credits. The footer carries **no version** — the header is the one visible home per §5b:
```
LESSON 11 · Time Lies, Distance Doesn't
Encoder-Based Gap Crossing
Zumo 32U4 Robotics • PlatformIO Edition
© 2026 RoboLore · Written and compiled by DJ Weymuth and Claude AI
```

**THE HERO TITLE IS CANONICAL.** S70 found **three** live title sources disagreeing: the header hero, the `<title>` tag, and the §6.5a strip tooltip. They differ on **L01, L02, L03, L08, L15** (e.g. hero *Sense, Decide, Act* vs tab/strip *Hello, Robot!*). Footers are built from the **hero**. **OPEN:** `<title>` and the strip are untouched and still disagree.

**COPYRIGHT.** `© 2026 RoboLore`. Notice is not required for protection (automatic since 1989) but forecloses an innocent-infringement defence. *All rights reserved* is dead — a Buenos Aires Convention relic with no legal effect since ~2000 — and is NOT used. **No LLC/Inc suffix**: those are reserved designations and using one for an unregistered entity misrepresents legal status. The AI credit line is a **disclosure**, not a courtesy: the US Copyright Office holds purely AI-generated material uncopyrightable and requires AI content to be disclosed and disclaimed on registration; the human authorship (selection, arrangement, curriculum design, DJ's prose) is what is protected. **OPEN — the work-for-hire question:** the book was built for a course DJ teaches, on the school's Canvas, with school robots. That is the fact pattern the work-made-for-hire exception is written about, and it is answered by the Mercersburg faculty handbook, not by the name on the footer. Matters for the parked monetization/ebook item. Not legal advice.

### 25.6a THE TOOL PAGES ARE NOT CHAPTERS — AND LAYOUT IS GATED (v8.54, S70)

The §25.6 header/footer/hidden-banner canon binds the **17 content pages only**. `index.html`, `newproject.html`, `timer.html` and `tutor/tutor.html` are a landing page and three utilities — several render inside iframes — and giving them chapter furniture would be cargo-culting the rule onto pages it was never scoped to. What they owe is a **version line** (§5b) and nothing else. `index.html` is the one exception on credits: it is the public front door, so it carries `© 2026 RoboLore · Written and compiled by DJ Weymuth and Claude AI` beneath its existing site line — the notice does its real work at first contact, not buried in seventeen chapter footers.

**LAYOUT IS NOW GATED, because the recurring defect was never the markup — it was the file's location.** S70 shipped the same class of failure twice in one session: `going_deeper.html` uploaded into `lessons/` (leaving 23 lesson links and the index serving the stale root copy) and then `tutor.html` uploaded to the root (leaving the live tutor unversioned and the new file an orphan nothing linked to). Both looked like successful pushes. Neither was caught by any gate, because every gate checked *contents*.

`§12/§23 site layout: every page in its canonical place, no strays` (book_gates v1.5) asserts the exact set of 21 HTML pages and their paths — any extra page, any missing page, any page at the wrong path FAILS. Control-run three ways: a stray at root, a page moved into `lessons/` (fails as STRAY **and** MISSING, exactly reproducing the Going Deeper incident), and a stripped tool version line.

**A file in the wrong folder is a defect of the same class as wrong content** — and it is the one an upload-based workflow produces most easily, since a browser upload targets a folder and never questions it.

### 25.7 §9 IS THE HANDS, §10 IS THE HEAD

Full construct map (S70 census, 119 markers): Warm-Up §1 (4, L02 only) · TRY IT §3/§5/§8A (12) · Challenge §9 (87) · Mystery §9 (4, L11 only) · **Bonus Challenge §10 (12, L02/L03)**.

**Bonus challenges are misfiled.** They are practice, not assessment, and belong in §9 with their siblings. *Inferred: they landed in §10 because they were authored as an appendix rather than as part of the challenge set.* **Not yet moved.**

Student-facing vocabulary collapses from eleven names to five — **Warm-Up · Mental Knowledge Check · Challenge · Knowledge Check · Reflection** — with TRY IT, Mystery and Bonus absorbed as *types* inside §9. No exercise is deleted.

### 25.8 CAPS (so the page does not overwhelm) — **KNOWLEDGE CHECK IS A FLOOR, NOT A CEILING (DJ ruling, S77)**

Warm-ups **3** · Mental **3–5** · Knowledge Check **4 minimum, no maximum** · Technical Skills = objective count · Reflection **1–3**. For scale, L03 today carries 12 checkboxes, 10 quiz items, 8 challenges and 6 bonus challenges.

**S77 DJ ruling — "keep more than 5 and we can weed them out later."** The old flat cap of 5 had been dodged four times (L03, L04, L06 came out at 5 unforced; L05 at 4) while **L02 shipped live at 7**, and it finally bound on L07, whose ancestor was seven already-written, already-answered questions. Rather than cut content to fit a number, the number gives way: §25.2's *"# (scales with the lesson)"* is now the operative rule and §25.8 supplies only the floor. **A conversion never deletes an item to meet a count.** Over-count items are recorded in `ZUMO_PARKED_EXIT_ITEMS.md` for a later weeding pass, which needs a criterion that does not yet exist.

**THE FLOOR GATE IS WRITTEN (S78).** A BC03 count gate was proposed at S76 close and rejected: written against the old ceiling it would have failed L02 and L07 on its first run. The floor-of-4 version is the one that survives the S77 ruling, and it ships in book_gates **v1.8** — `§25.8 Brain Check 03 carries at least four items`, asserted only in converted lessons, control-run per §24.6b in both directions (against a lesson stripped to three items, which FAILED, and against the live book, which PASSED at counts 4/7/5/5/4/5/6/6 for L01–L08). There is still **no maximum**, and still no criterion for the weeding pass.

### 25.9 STILL OPEN AT S70 CLOSE

Not built, not ruled, do not treat as done: warm-ups for L02–L16 · the spiral aiming rule applied · §2 objectives rewritten from the checklists · bonus challenges moved §10→§9 · a separate mark for within-lesson build-ons · **L13 and L15 still have no exit written-response block** · `<title>`/strip vs hero titles · L16 still has zero challenge cards · `going_deeper.html` footer contrast (`#666` on `#0f1117` ≈ 3.3:1, below 4.5:1) and its duplicated hero title · **no gate yet exists for §25** (§24.2: a rule without its gate holds only where someone looks).

### 25.10 BRAIN CHECK — THE KNOWLEDGE FAMILY NAME, LIVERY, COLUMN & CHECK-OFF (LOCKED, S71)

#### 25.10a THE FAMILY IS FOUR, AND THE COLUMN IS WHY (v8.59 — NEW, S73, DJ-ruled)

**There is no BC05.** The shared Brain Check column is a single 5,596-character block copied
byte-identical into every converted lesson (L01 == L02, verified), and its script is hardcoded to four:
the saved state array is length 4 and is discarded on load if it is any other length, the click handler
rejects any index past the fourth, and the skills unlock is wired to BC02 **by index**. A fifth block
would need a per-lesson column variant — three diverging copies of that script, in a family this section
marks LOCKED.

**RULE — a lesson's extra exit block folds into the BC it most resembles, as a labelled group.** L03 is
the live case: it carried two checkbox blocks, *Technical Skills — I can…* (8 capability items) and
*Problem-Solving — I have…* (4 process-audit items). DJ's first instinct was BC05; the cost above was
priced and the ruling changed. Both lists now live inside **BC02** under bold sub-labels **I can…** and
**I have…**, all twelve items carrying `data-bc-skill`. Nothing was deleted and both jobs stay visually
distinct.

**THE UNLOCK GENERALISES ON ITS OWN.** `allSkills()` loops over every `[data-bc-skill]` element rather
than a fixed count, so L02's 7-of-7 became L03's 12-of-12 with zero JavaScript edits. **Check whether the
mechanism already scales before writing a rule that assumes it does not.**

**COLUMN PLACEMENT IS PART OF THE COPY.** The block seats immediately before `</body>`. Appended after
`</html>` it renders but fails the *structure: HTML parses to the intended shape* gate — which is how S73
caught it.

**A §-CITATION IS VERIFIED BY CONTENT, NEVER BY PRESENCE** (restating v8.58.1, because this is where it
bites). Every converted item's cited § must be sliced and shown to contain the answer. Slice a subsection
by the **next subsection id**, never by the next top-level section anchor: a Brain Check block physically
sits between two sections, so an anchor-bounded slice swallows the quiz asking about the previous one and
reports the answer as present when it is not. That false positive nearly buried the L02 prototype defect.


#### 25.10b SCOPE A CONVERSION BY THE RETIRED-NAME LIST, NOT THE LIVE ONE (v8.60 — NEW, S74)

**Before authoring a single Brain Check item, grep §25.2's RETIRED NAMES list against the lesson.** The
ancestor block is often present under a name no longer in use, and a lesson that looks like it has nothing
to redistribute usually has everything.

L04 is the case that earned this. Sweeping for the live construct names — `STOP & PROCESS`,
`Knowledge Check`, `Reflection` — returned nothing, and the S74 queue was written on that result: *"expect
L04 to have no ancestor to redistribute, so this is the first conversion that is mostly authoring."* It has
a ten-item ancestor, titled **Conceptual Understanding**, which is the second entry on the retired list. The
sweep that found it was the retired list, not the live one. Ten items would otherwise have been written
from scratch alongside ten that already existed.

**COROLLARY — the retired name is load-bearing evidence, so read the list before trusting a handoff's
scoping claim.** A handoff records what the previous session saw; the retired-name grep records what is
actually in the file. §24.6c already says control-run every audit grep. This says run the *right* grep
first.

**FOLDING AN EXTRA CHECKLIST COSTS GRAMMAR, AND THAT IS ALLOWED.** §25.10a folds a second checkbox block
into BC02 under **I can…** / **I have…** labels. Where the source items carry their own subject ("I wrote
and ran code using…"), the fold requires stripping it to a bare verb phrase to match the label and the
block's own *Can You…?* title — which is also how L01, L02 and L03 already phrase every skill. Two kinds of
rewording are expected and are not content changes: **tense** ("I wrote and ran" → "Written and run", under
*I have…*) and **clause order** where the subject sat mid-sentence ("When readings looked wrong, I
checked X" → "Checked X when readings looked wrong"). Everything else migrates character-exact — including
the file's own apostrophe convention, which is checked, not assumed.


#### 25.10c A DUPLICATED ANCESTOR IS OFTEN ALREADY SPLIT — AND AN UNGATEABLE ITEM MOVES, IT DOES NOT DIE (v8.61 — NEW, S75)

**WHEN TWO ANCESTOR BLOCKS HOLD THE SAME FACTS, COMPARE THEM ITEM BY ITEM BEFORE ASSUMING ONE IS WASTE.**
L05 carried a six-item `Conceptual Understanding` (questions, no answers) directly above a six-item
`Knowledge Check` (the same six, with reveals). Four pairs were word-identical and the duplicate really was
redundant. **One pair was not:** *"What does a function prototype promise the compiler?"* against *"Our
helper functions live below loop(), in any order — why does the build still succeed?"* — the same fact at
two cognitive levels, which is exactly the §25.2 recall/apply line. The answerless list had already done
part of the split. Discarding it wholesale would have thrown away a Mental item and forced one to be
authored in its place. **Diff the two lists by normalised text; a pair that DIFFERS is a finding, not
noise.** L05's BC01 reached the 3-item floor on migrated wording because of it.

**A SKILL THAT FAILS §25.10 ACHIEVABILITY IS RELOCATED, NEVER DELETED.** Folding a second checklist into
BC02 (§25.10a) puts every item behind the Mark-done lock, so an item not every student can earn makes the
lock unreachable. That is a reason to move the item, not to drop it. Two disposals, both used on L05:
- **RETIRE INTO PROSE THAT ALREADY SAYS IT.** *"Complete at least one of the Bonus mysteries"* was already
  the §9 lead-in's own sentence, naming all five. The instruction survives in the place students actually
  read it. Same shape as S73's L03 duplicate-Reflection retirement.
- **RESHAPE INTO THE CONSTRUCT IT ACTUALLY IS.** *"Extend: add a fourth display mode showing detection
  history"* was never a checkbox skill; it was a challenge wearing one. It became a sixth bonus mystery,
  rewritten to the section's own predict/test/explain contract. **A reshape retitles its host** — "Five
  Proximity Mysteries" became "Six", and the §9 lead-in list gained an entry. Budget both strings.

**THE BRAIN CHECK COLUMN IS COPIED START-THROUGH-END-COMMENT, AND THE END COMMENT IS 43 CHARACTERS.**
Slicing it one byte short leaves `<!-- ... =====  --` unterminated, which swallows `</body>` and `</html>`
and surfaces as *"html still open at EOF"*. **Tag balance passed; the §24.6 parse gate caught it** — a
fourth instance of §24.6's rule that structure is verified by parse, not by count, and the first where the
defect was an unclosed *comment* rather than an unclosed element. Assert the copied block ends in `-->`.

#### 25.10d A CITATION CAN POINT AT A HOLE — AND THE COLUMN FINGERPRINT WAS THE SHORT SLICE (v8.62 — NEW, S76)

**WHEN A CITATION CANNOT BE VERIFIED, ASK WHETHER THE SECTION IS WRONG OR WHETHER THE CONTENT IS MISSING.**
§25.10a says a citation is verified by content. S73, S74 and S75 each found a citation aimed at the wrong
section, and each was fixed by re-aiming it. **L06 was the first where there was nowhere to aim.** Its
Knowledge Check asked *"If the robot drives 33cm instead of 30cm, what should you adjust?"* and answered
`WHEEL_DIAMETER_MM` — a string that appears in exactly two places in the whole file: §6 Step 5, where the
constant is declared, and the question itself. §3.4 supplies the formula and never says which constant to
move. **The fix is to write the missing content, never to re-point the citation at the nearest plausible
section.** L06 gained a sixth Quick Fix Table row and the item now cites §8 truthfully. Same family as §11
*"if it is in the payload, it goes in the book"* — an unmatched citation is a GAP IN THE BOOK, not a
paperwork error.

**A WITHIN-LESSON PROMISE IS UNGATED.** The reason the hole survived is that Step 8's checkpoint reads
*"Off by a lot? Section 8 has the table"* and §8's table covered five faults, none of them distance
accuracy. `§24 cross-lesson promises land in target lesson` only walks promises that name ANOTHER lesson;
a pointer from §6 to §8 of the same file is invisible to it. **When converting a lesson, follow its own
internal pointers by hand** until a gate exists for them.

**THE COLUMN FINGERPRINT IN §25.10c WAS THE SHORT SLICE.** §25.10c mandates copying START through the full
43-character END comment, and then records the block as *5,596 chars, `8fa00744`* — which is the span
measured START through **before** the END comment. Verifying a column against that figure means slicing
5,596 characters and reproducing the exact unterminated-comment defect the rule exists to prevent. The live
files were never wrong; the paperwork was. **Canonical: 5,639 characters, md5 `070806a6`, ending in `-->`.**
The old pair is retained here only so a stale note can be recognised: 5,596 / `8fa00744` is the body
without its terminator. **A rule that records its own fingerprint must record the span it mandates.**

**§25.5 IS LIVE AS OF L06.** BC02 is built by migrating the lesson's §2 objectives **character-exact**, so
Technical Skills and Objectives agree by construction and the lesson never joins the reconciliation debt
(L03 8 vs 11 · L04 13 vs 11 · L05 7 vs 10, all left alone per the S74 ruling). Migrate the objective text
unchanged — rewording it to sound more checklist-like reopens the gap the rule closes. Where an objective
opens with a soft verb (*Understand the difference between…*), **keep it**: the two lists agreeing is worth
more than one tidier verb, and §25.5 makes §2 the anchor either way.

#### 25.10f AN ANCESTOR CLAIM IS A LEAD TOO — INCLUDING ONE WRITTEN INTO THIS BIBLE (v8.64 — NEW, S78)

**§25.10e was right about the rule and wrong about its own evidence.** It closed by naming four unswept
ancestors in the unconverted lessons. Checked against the files at S78, one of the four does not exist,
one is misnamed, and two are section titles rather than blocks:

| Recorded at S77 | What is actually in the file |
|---|---|
| L08 *Check Yourself* | **Does not exist.** `check yourself` appears twice in L08, both lowercase prose — §1's *"Compare to solution — Check your work against the provided answer"* and §6 Step 7's MY PLAN, *"…then check yourself against it."* Neither is a heading. |
| L11 *Skills Check* | Real block, titled ***Skills Checklist***. |
| L15 / L16 *Wrap-Up* | The **§10 section banner title**, not an exit construct. §25.9 separately records L15 as having no exit written-response block at all. |
| — | **L09 carries two live ancestors nobody listed:** *Technical Skills: Can you…?* and *Knowledge Check*. |

L08's actual ancestor was a three-item **Knowledge Check** sitting under BC03's own live name — the same
shape as L07, and the reason the S78 conversion was still a redistribution job.

**THE RULE — a scoping claim inherited from a handoff or from this Bible is a lead, exactly like a grep
result.** §25.10e says do not trust a name; this says do not trust a name *someone else already looked
up*. Before a recorded ancestor becomes the scope of a conversion, open the file and confirm the block
exists, is a heading and not prose, and does the job the record claims. The failure mode is specific and
cheap to avoid: **a case-insensitive keyword hit reported as a block without anyone reading it.** §24.6c
already binds audit greps; this binds the sentence that outlives the grep, because a wrong finding
promoted into canon is quoted forward for sessions without anyone re-running anything.

**Corollary — the check costs one grep and one read.** Grep case-insensitively (`grep -oiE`), because the
book's era vocabulary varies; then read the surrounding markup and ask whether the hit is inside a
heading. A prose sentence and an `<h3>` are indistinguishable in grep output and are not remotely the
same finding.


**The four §25.2 exit-region constructs share ONE family name: BRAIN CHECK, numbered 01–04.** The constructs keep their §25.2 identities; the family name and number are prefixed in the header:
- Brain Check **01** · Mental Knowledge Check (before hands-on work)
- Brain Check **02** · Technical Skills ☐ (§10)
- Brain Check **03** · Knowledge Check (§10)
- Brain Check **04** · Reflection (§10)

Header canon: `BRAIN CHECK NN · CONSTRUCT NAME — subtitle`, icon image leading. One family name, four numbered members — this subsection exists so the §4.1 six-names disease cannot regrow here. Do NOT invent additional "Check" block names.

**Livery = §8 Type 10** (bg `#e8eaf6`, border-left `#3f51b5`, title `#283593`). All four wear it, including Technical Skills (pulled off Checkpoint green — a knowledge block is not a milestone banner) and the two blocks that formerly wore §9 Challenges plum (§25.7: §9 is the hands, §10 is the head; the color now agrees).

**Anchors:** each block carries `id="brain-check-0N"`. Gated (book_gates v1.6).

**THE COLUMN.** A fixed right-edge column (`id="brain-check-col"`, bounded by `BRAIN CHECK COLUMN START/END` marker comments — ONE block, edit whole) with the family emblem on top and pills 01–04 linking to the anchors. Ships ONLY in converted lessons — a lesson gets the column in the same edit that gives it the four blocks, never before (no dead links). The column hides below 700px viewport width via its own script (inline styles cannot media-query; this is the §6.5a self-hydration pattern).

**CHECK-OFF STATE.** Each block ends with a `data-bc-btn` toggle button. **Brain Check 02 is SKILL-GATED (S71, DJ-ruled):** every ☐ checklist item carries `data-bc-skill` and is tappable (☐→☑, green when checked; state in `localStorage` key `bc_LNN_sk`, array length derived at runtime from the tagged elements so the rule is lesson-agnostic); BC02's Mark-done button stays LOCKED (gray, 🔒 label, no-op) until every skill is checked. Unlock gates only the transition TO done — undo is always available, and un-checking a skill after marking done does not revoke the done flag. Gated: box-glyph count must equal `data-bc-skill` count in every converted lesson (book_gates v1.7).

**GATED-ITEM ACHIEVABILITY (S71).** A skill item behind the BC02 lock must be achievable by EVERY student who did the lesson. If an item depends on chance — "identify and fix an error" when a lucky student never hits one — the lesson MUST include a deliberate rep that produces the event on purpose (L01: the Break-It-On-Purpose upload-error rep at the end of §6 Step 6, power-off → failed upload → read → fix). Same defect class as §11 "a declared blank must be spent": the lock promoted a harmless unchecked box into a blocker on luck. This is a REVIEW rule (not machine-gateable): when converting a lesson, read its BC02 items and ask "can a student whose build went perfectly check every one?" — any NO gets a rep or a reword before the lock ships. State lives in `localStorage` key `bc_LNN` as a 4-element 0/1 array, key derived from the filename. Done paints pill + block icon + button green; the emblem flips to the Complete icon only at 4/4. **This is a personal tracker, per-browser, invisible to the teacher, and NOT a grade** — the Canvas reading quiz remains the real gate (§25.3); a student can self-mark 01 without answering honestly, and the two must never be conflated. The disclaimer lives in the column's `title` tooltip.

**THE ICON PAIR** (`images/BrainGear_Incomplete.png` gray `#454545` / `images/BrainGear_Complete.png` green `#24911b` + check):
- State is NEVER color-alone: the Complete artwork carries the check glyph, Incomplete does not — red-green colorblind-safe by construction.
- Incomplete is GRAY, not red — deliberate: §22 locks red as the ERROR color, and "not yet done" is a healthy state, not a failure. Do not "improve" incomplete to red.
- Both icons: interiors are TRANSPARENT (alpha-shaped, single stroke color); on a light backing interiors read white. Floor 24px; working range 32–128px. **Dark backings are FORBIDDEN without a light panel behind** — the linework vanishes (QA'd S71).
- Cut method per §21: edge-connected flood fill; the gray was rebuilt single-color-plus-alpha to match the green's structure exactly (S71; opaque light-interior px = 0 in both).

**Rollout:** L01 is the reference (v03.9.0, S71). Each lesson gains blocks + column together as it converts (S71 queue: L02, L03, then onward).

#### 25.10i A PAST-TENSE RUNG IS NOT AUTOMATICALLY A DUPLICATE (v8.105 — NEW, S116)

**§25.10c says to diff two ancestor lists item by item. This says how, when the duplication is
real but not word-identical.** L11 carried a seven-rung *Skills Checklist* against six §2
objectives. Four rungs restate an objective in the **past tense** — *"I converted encoder counts
to centimeters using `COUNTS_PER_CM`"* against *"Convert encoder counts to centimeters using
`COUNTS_PER_CM`"* — so L05's word-identical test does not fire on them, and reading them by eye
gives whatever answer the reader already expected. It did: the split was hand-predicted at 4/3,
asserted, and **the assert failed** on a normaliser that stripped only the *"I can"* / *"I have"*
subjects.

**THE METHOD — SCORE EVERY PAIR, THEN READ THE SEPARATION, NOT THE LABELS.** Run all N × M
combinations through a similarity ratio on subject-stripped text and print the best match per
rung. L11 separates cleanly: the four duplicates score **0.55–0.73** against their partner
objective; the three survivors score **0.31–0.38** against their nearest. The ruling is then
encoded as a NAMED PAIRING, and the builder asserts `min(dup_scores) > max(keep_scores)` —
a separation a wrong pairing cannot satisfy, where a bare count could be met by any four rungs.

**DO NOT TUNE THE NORMALISER UNTIL IT REPRODUCES THE PREDICTION.** That is writing the gate to
the sweep. Re-derive, then record what the derivation said.

**THE DUPLICATES ARE PARKED, NOT DROPPED** (S77), with their pairing table, because the past
tense asks something the objective does not: *did you actually do it*, against *can you do it*.
**That question is OPEN and DJ has not ruled it.** If the distinction is worth keeping, all seven
rungs fold into BC02 and the student ticks the same claim twice under two labels; if it is not,
the four stay parked. Either answer is defensible and the cost is one visible list.

**AND THE FOLD CAN CREATE AN ACHIEVABILITY EDGE THAT THE ANCESTOR DID NOT HAVE.** L11's rung
*"I ran 7E and watched the stopwatch version fail on a tired battery"* was a plain checkbox for
eleven sessions. Folded into BC02 it sits behind the Mark-done lock and now needs a **tired
battery** to earn. §7E mandates the run, so the lesson does plant the rep — but §25.10c's rule
binds here and the item is flagged, because **the lock is new exposure even when the item is
old.** Check every folded rung against the lock, not just against the lesson.

#### 25.10h BRAIN CHECK PLACEMENT (v8.71 — NEW, S84, DJ ruling)

The family's four blocks have fixed structural seats. Placement had **no rule** until now, only an
observed practice — precisely the §6.8a shape — and it drifted exactly once.

- **Brain Check 01** is a **direct child of `<body>`** (div depth 0) and its **NEXT SIBLING is the
  banner that seats `#section-6`**. It is the pre-build Mental check, so it sits in the seam between
  §5's content and §6's banner, outside both.
- **Brain Check 02, 03 and 04** sit **one div deep, inside the gray `#6c757d` §10 content panel**.
- **BC01's PREVIOUS sibling is deliberately NOT specified.** It legitimately varies — L01/L02 end on
  a §5 subsection banner, L03 on a predict-first box, L04–L09 on §5's green content panel. Asserting
  it would gate an accident.
- Applies to **converted lessons only** (those carrying `brain-check-01`). Nine today: L01–L09.

**Why it is canon now.** S83 found L06's BC01 nested **inside** §5's green content panel — last of 49
direct children, after §5's own back-to-top link — so it rendered inside the green box in L06 and
outside it in the other eight. The repair was relocating a single `</div>`, and it left the family
**9/9 unanimous**. A unanimous practice with zero canon behind it is a rule waiting to be written
down. Note the S83 handoff recorded the norm as *"8 of 9"* because it was counted before that
session's own fix landed: **a norm quoted from a handoff is a lead too (§24.6c) — recount it against
the files.**

**Gated the same session per §24.2** — `book_gates.py` v1.16 **gate 29**, COVERAGE asserted at nine
converted lessons. Control-run three ways, each injection re-parsed and confirmed in the intended
shape before the verdict was read: **L06's S83 defect re-introduced FAILED**, naming
`brain-check-01 is 1 div(s) deep — it is inside 'border: 2px solid #3a7d5c…'` and the lost §6
sibling · a BC03 lifted out of the gray panel FAILED · a removed `brain-check-01` id tripped
COVERAGE at 8. **That first control is the point: the gate catches the one defect this construct has
ever actually had.**

### 25.11 A REVEAL'S VISIBLE LABEL MUST AGREE WITH ITS TYPE (v8.67 — NEW, S81, DJ ruling)

**THE RULE.** `data-reveal` and the `<summary>` label are two halves of one promise. *"If it's a hint,
then say hint. If it's a solution, then call it a solution."* (DJ, S81.) A `solution` may not be labelled
*Hint*; a `hint` may not promise an answer or a solution.

**WHY IT IS NOT COSMETIC.** The label is the student's only signal for whether opening the block spends
their attempt. And §20.1 strips `solution` before the lesson reaches the tutor — so a block typed
`solution` but labelled *Hint* is simultaneously withheld from the model and advertised as help to the
reader. The two audiences get opposite messages from the same element.

**THIS IS THE COST OF AN ATTRIBUTE-ONLY EDIT.** §25.10g retyped nine mystery reveals at S80
attribute-only, which was correct for the version banner (§5b) and wrong for the label: moving a type
without moving its label manufactures this contradiction. **When a retype changes what a block IS, check
what it SAYS.**

**THE PRECEDENT IS L11, FOR THE THIRD SESSION RUNNING.** Its four mysteries were the only ones in the book
where type and label already agreed — `solution` + *"💡 Answer"*. Copy a live precedent; do not invent
wording. (§25.10g found L11 right about the type; §20.1 found L11 right about the strip; §25.11 finds
L11 right about the label. A lesson that keeps being right is worth reading before authoring.)

**CENSUS AT S81 (all 30 mystery reveals).** L05/L06/L07 and L08 `8.m3` are `hint` + *Hint* — consistent,
and each verified to contain **no `<pre>` at all**, which is exactly why §25.10g correctly left them
typed `hint`. L11 ×4 already correct. L08 ×4 + L09 ×5 were the drift, relabelled *"💡 Answer"* at S81.

**SCOPE THE EDIT BY OFFSET, NOT BY STRING.** L08 holds **five** copies of the identical bare summary string
and one of them (`8.m3`) must not change — the §6.12c rule applies to label text exactly as it does to
inline CSS. Locate each target through its heading-bounded construct span and assert a +2-byte delta per
edit.

**GATED (book_gates v1.11).** `§25.11 reveal label agrees with reveal type`, deliberately narrow per
§24.6c: the book's label vocabulary is legitimately varied (62 *reveal solution*, 13 *Answer*, 9 *worked
version*, plus the `catchup`/`troubleshoot`/`check` families), so the gate asserts only the two
contradiction shapes verified by reading rather than policing a whitelist. Control-run three ways.

### 25.12 THE `<details>` WITH NO TYPE AT ALL (v8.67 — NEW, S81)

A missing `data-reveal` is not a neutral default — §20.1's strip list is a **whitelist**, so an untyped
reveal is *kept* and reaches the tutor. L02 `2.t1`'s *"🔓 Answers"* block was the only untyped
`<details>` in the book (403 elements, 402 typed) and had been shipping its worked answers to the model.
Typed `solution` at S81 on the precedent of `2.t5`, the sibling TRY IT in the same lesson. **The count is
the detector: `<details>` total must equal `data-reveal` total.** Enumerated by `lesson_inventory.py`,
which reports an untyped reveal as a named lead rather than a silent default.

*(§25.9 above remains this section’s open-items ledger — §25 is not finished until that list is.)*

---

#### 24.11 A SWEEP THAT AUTHORS LITERALLY CAN UN-ESCAPE AN ENTITY (v8.81 — NEW, S93)

**S92's Option C sweep re-introduced a defect this Bible records as fixed at S81.** L12's prose read `The #include &lt;Wire.h&gt; goes at the TOP of the file.` at S87, S89, S91 and `03d1e85`. At `514588e` — the S92 push — two occurrences came back **raw**: line 594's title and line 774's `<code>` span. The browser tokenises `<Wire.h>` as an unknown element, so the sentence rendered **"The #include  goes at the TOP of the file."** with the filename gone. That is v8.67's defect, same lesson, same sentence, eleven sessions later.

**The cause is the sweep's own stated principle.** v8.79 records it approvingly: *"caps authored literally, no `text-transform`, so the source string == rendered string."* Authoring the string literally is right for CASE and wrong for MARKUP — an entity is not the character it encodes, and a sweep that rewrites a title from its own flattened text will silently spend the escape.

**THE RULE — after any sweep that re-authors element text, PARSE FOR UNKNOWN TAGS.** Not a grep for `<Wire.h>` or any other known instance: feed every page to an HTML parser and report every start-tag whose name is not a real HTML element. Prose that the browser will eat as markup then reports itself, whatever it says. Bounded and cheap: run across all 21 pages S93 found exactly **2** hits, both L12, and after the fix **0**.

**A second defect of the same family, from a DIFFERENT sweep.** L04 line 1363 carried `<div …>&lt;/&gt; The <strong>deadband</div> — a band where the robot does nothing</strong>` — introduced at `53a44b6` (S91), absent at `c4b8253`. The last-good form was a bare `<strong …>` title, and the block-form conversion replaced the **inner** `</strong>` with `</div>` instead of the outer one, so the subtitle rendered outside the title element and unbolded. **A conversion that swaps a wrapper must close the wrapper it opened**, and when the wrapper and its content use the same tag name, the first closer is not the right one.

**BOTH WERE REPORTED BY `lesson_inventory --anomalies` THE WHOLE TIME, AS `unclosed <wire.h>` AND `unclosed <strong>`, AND WERE NOT READ FOR TWO SESSIONS.** All 35 gates passed over both. §24.6a says a parser is necessary and not sufficient; this is the other half — **a parser whose output nobody reads is not an instrument, it is a log file.** The anomalies list is part of the session-open ritual for exactly this reason, and its output is now read item by item, not glanced at for the word FAIL.

**AND THE STALE EXPECTATION THAT HID THEM IN PLAIN SIGHT.** The same anomalies list prints `1 visible banner(s), expected 2` for **all sixteen** lessons, because `lesson_inventory` still carries the pre-S89 two-banner rule while §5b and the gate have required exactly ONE since the build banner was deleted. Sixteen identical false leads trained the eye to skip the block that also held the two real ones. **A uniform anomaly across every file is a lead about the INSTRUMENT, not the book** (§24.8) — and a false lead is not free: it buys cover for the true ones sitting beside it. The parser's expectation is logged for correction, not corrected here, because changing an instrument mid-verification invalidates the verification.

**Applied S93, both MODERATE (rendering changes, so the one visible §5b banner moves with the hidden comment):** L04 **v04.13.0 → v04.14.0** · L12 **v01.13.0 → v01.14.0**. Census unchanged at **39,970** — both fixes add characters, not lines, which is itself the check that they were surgical.

---

#### 24.12 A GENERATED ARTEFACT IS REGISTERED HERE, AND ITS FILENAME CARRIES NO SESSION (v8.89 — NEW, S103, DJ ruling)

**Some instruments do not just report — they WRITE A FILE that is then committed and worked from.**
Those files are a third category, and until this entry the Bible named none of them. §24.1–24.11
govern how an instrument is trusted; nothing governed what an instrument leaves behind.

**THE RULE, two parts.**

**1. The filename carries no session stamp.** A generated artefact is named for what it is, not for
when it was made: `GPT_WORKLIST.md`, not `GPT_WORKLIST_S102.md`. The session, the generator version
and the version of anything the generator depends on live on a line **inside** the file — the same
two-homes discipline this Bible applies to itself (§5b) and to its own version line.

**2. Every generated artefact is registered in the table below.** An artefact that is committed but
named nowhere in canon is a file nobody owns: it cannot be re-derived by someone who does not
already know which script wrote it, and it cannot be recognised as stale.

| Artefact (repo root) | Written by | Regenerate with |
|---|---|---|
| `GPT_WORKLIST.md` | `build_worklist.py` | `python3 build_worklist.py --session NNN` |
| `ZUMO_FAMILY_MAP.md` | `build_family_map.py` | `python3 build_family_map.py` |

**WHY THE STAMP MOVES INSIDE, stated plainly so it is not re-argued.** A session in the filename
does not preserve history — it manufactures a second plausible file. At S103 open the repo root
held **both** `GPT_WORKLIST_S99.md` and `GPT_WORKLIST_S102.md`. Neither was obviously the live one;
the S99 list was known-bad (hand-assembled, ordered by font sizes the audit could not yet read)
and was still sitting there looking like a document. That is the exact hazard §5b was written
against for lesson versions and §12.2 for handoffs, arriving through a different door. **The
version-in-the-filename mistake does not become safe because the number is a session instead of a
release.**

**AND THE COROLLARY THAT MAKES IT WORTH THE EDIT.** A stamped filename lets a stale artefact hide
behind a fresh-looking name; an unstamped one cannot. `GPT_WORKLIST.md` is either current or it is
visibly a regenerate away, and the `Work list session:` line says which. **One file, one name, one
grep.**

**A GENERATED ARTEFACT IS NEVER HAND-EDITED.** If it is wrong, the generator is wrong. Fixing the
output and leaving the generator alone reproduces the defect on the next run and destroys the only
evidence that it existed — and reproducibility is the entire reason `build_worklist` exists
(`GPT_WORKLIST_S99.md` was hand-assembled, which is why S101 could not re-derive it).

---

#### 24.13 RE-DERIVE, DO NOT RE-READ — AND A LIST IN PROSE IS NOT THE LIST (v8.98 — NEW, S109, DJ ruling)

**DJ, S109, on being told a taxonomy had been checked three times and was still wrong:** *"So when
I say double check you don't double check?"* He is right, and the distinction he is pointing at is
the whole entry.

**RE-READING IS NOT CHECKING.** A second look at the same artefact is the same instrument run
twice. It cannot find a missing member, because a list with a member missing looks complete and
internally consistent from the inside — which is §24.8's test, failed. A check is a **different
method**, or an **assert against a number produced outside the artefact**. Nothing else counts, and
the word *verified* is not used for anything else.

**A LIST PRESENTED IN PROSE IS NOT THE LIST.** Any set whose membership matters — families,
sections, gates, versions, lesson numbers — is EMITTED from the structure that produced it and
asserted against a known total. The moment a set is retyped into a chat message, a handoff or this
Bible, it is unverified again and must not become the source for the next step.

**THE S109 CASE, because it is the cleanest instance this canon has recorded.** A 17-family
consolidation was computed in code and printed `CORE CONCEPT 60` with `unaccounted: 0` — correct.
It was then hand-typed into a chat message as an 11-row table, and the 12th row, INSIGHT's 60
blocks, was dropped in the retyping. The next build read the **chat message** rather than the
verified structure, so the data structure was abandoned in favour of the prose derived from it.
Three subsequent passes over that table found nothing, because all three were re-readings. It was
caught by one line — `assert tot + rem == 1048` — comparing against a total the table could not
supply.

**THIS IS THE v3.0 GHOST WEARING A DIFFERENT NOUN.** §12.6 already forbids hand-typing a VERSION,
for exactly this failure; §24.10 already requires every count to name its instrument. Neither
covered a *taxonomy*, and the gap was enough. The rule is therefore stated on SETS, not on version
strings, and it is the reason `session_versions.py --live` EMITS its block rather than inviting
one to be written.

**Ungated by design**, like §24.6b/§24.6c/§24.7/§24.8 — there is nothing in the book to assert
against. The operative check is whether a presented set can name the structure it was emitted
from, and whether its total was asserted rather than eyeballed.

#### 24.14 EVERY CALLOUT BLOCK RESOLVES TO A FAMILY (v8.103 — NEW, S114; the rule gate 47 has been enforcing since S112)

**Every callout block in the sixteen lessons belongs to exactly one family, and a generator must
be able to say which one from the block's own CONTENT.** `build_family_map.py` is that generator;
`book_gates` gate 47 runs it and fails if any block is unassigned.

**THE ORDER IS THE RULE: family comes from content, and the mark and the colour are OUTPUTS of
the family.** Never the reverse. A taxonomy that reads paint is a taxonomy that moves when the
book is repainted, and at S112 that is exactly what happened — **252 of 1,048 blocks, a quarter
of the map, were resolved by HEX**, so the S111 repaint moved the ground under them and one block
fell out. Control-run against the pre-repaint tree with the identical generator: 1048/1048. **The
repaint did not break the assignment; it revealed that the assignment was never earned.**

**PAINT CAN OVERRIDE A CORRECT RULING, AND DID.** Thirteen L12 blocks wore one glyph and one
green and were **three families** — eight conceptual payoffs, three byte-count build reports, two
observed-behaviour blocks. §24.13's own ruling that a byte-count report is STILL GREEN was
already on the books and sixteen blocks elsewhere were filed that way; those three read as
INSIGHT purely because they shared paint with their neighbours. The ruling was right and the
colour overrode it.

**THE GLYPH TIER IS A STOPGAP AND IS LABELLED ONE IN THE FILE.** Thirteen glyphs each resolve to
exactly one family, which is why it works today — but 41 marks sit generated in `images/marks/`
with none wired in, so a taxonomy keyed on emoji is keyed on something already scheduled for
replacement. When the marks land, the glyph tier is re-derived, not patched.

**THE DENOMINATOR IS A BASELINE, NOT A COUNT.** `build_family_map` prints `assigned N / M` where
**M is a literal**, not a parse of the book. It therefore asserts two different things at once —
that every block resolves, and that the book still holds exactly the number of callouts it held
when the literal was last set. That is useful in both directions and it is **not what the printed
line says**: adding one callout at S114 produced `assigned 1049 / 1048`, which reads as a count
and is not one. **Consequence, until it is ruled: adding or deleting any callout anywhere in the
book fails gate 47 until a human edits that literal.** Moving it is legitimate — but only after a
control run at the identical generator version proves the per-family delta is exactly the blocks
you changed and nothing else. **The total alone is not evidence**; routing one block to the wrong
family leaves it untouched.

**Gated** by `book_gates` §24.14. The gate shells out to the generator rather than
re-implementing the matcher, because a second matcher here would be the third regex §24 forbids,
and it checks **both the exit code and the parsed line** so a crashed tool cannot read as a silent
pass.

#### 24.15 A DRAFTING MODEL CANNOT COUNT THE BOOK (v8.101 — NEW, S114; written S112 as `GPT_BRIEF_FORMAT.md`)

The S111 four-task package sent to the drafting model came back three good and one unusable,
and **the split was not about quality of reasoning — it was about facts.**

Tasks 1, 2 and 4 handed the model a file and asked it to write. The file was the whole world,
and the work was good: Task 4 returned 19/19 headings, 263/263 table pipes and 10/10 checklist
items intact while cutting 499 bytes of prose. Task 3 asked which two content categories should
take the two unnamed section colours. That answer depends on facts spread across the repo — how
many sections exist, whether the spine is fixed, how the candidate content is distributed, which
colours are already reserved. The model had none of them. It reasoned soundly to an unusable
recommendation and, to its credit, closed by saying the frequencies should be checked against
the live inventory.

**THE RULE. Every brief opens with a MEASURED FACTS block.** Facts only, each naming the
instrument that produced it (§24.10 — a number with no named source is a lead, not a finding).
If a task's answer depends on a number that is not in that block, either add the number or do
not send the task.

```
## MEASURED FACTS — taken from the live repo at <sha>, do not re-derive

- The lesson spine is FIXED: 174 sections, 10-11 per lesson, zero variance
  across all 16 lessons. §4.4 makes all ten mandatory. [lesson_inventory.py]
- Six colour bands cover that spine. Two further band colours exist and are
  assigned to nothing. [ZUMO_S111_VISUAL_RULING.md, build_palette.py --check]
- WARNING carries a reserved colour never assigned to a band, 80 blocks.
  [build_family_map.py]
- ENGINEER'S LOG: 16 blocks, all 16 inside §10. [lesson_inventory.py]
- Competition/rules terms: 88 hits, 63 in L14, 12 in L16, 0 in seven lessons.
  [regex over lesson source, control-run]
```

**TASK SHAPES.** *SEND* when the supplied file is the whole world — prose tightening, learning
objectives, student-facing sections, rewriting for observability, candidate generation with the
tradeoffs named. *DO NOT SEND* when the answer is a count, a distribution or a canon lookup —
"which of these deserves X", "how often does Y appear", anything already resolved by a ruling in
this Bible. *SEND WITH FACTS ATTACHED* when it is judgement over measured ground — "given these
counts, which two categories", "given this spine, where would a new section go."

**TWO THINGS THE S111 PACKAGE DID RIGHT — ask for both every time.** (1) Structural
recommendations were kept OUT of the diff file and returned separately, so the diff stayed
reviewable. (2) It named its own inferences and flagged the frequency gap rather than papering
over it — that flag is what made the failure cheap to catch. Require an explicit *"what I
assumed vs what I read"* section.

**AND ONE THING TO REQUIRE: the reference files come back unmodified alongside the outputs.**
S111 did, and both returned byte-identical to the repo, which is how the package was cleared in
one command instead of being read line by line.

**Ungated by design.** The operative check is whether a brief's every count named an instrument.

---

## 26. HERITAGE BLUE — RULED (v8.80 NEW SECTION S93 as THE PALETTE CONFLICT, PARKED; **RULED AND UN-PARKED v8.87, S101**)

**Status: RULED, S101. DJ stated the five values himself, so §26.1 no longer depends on citing an uncommitted file. §26.3 is answered by §26.8. The archaeology in §26.1–§26.7 is kept unedited as the record of how it was settled.** Originally recorded because this conflict has been rediscovered and quietly re-litigated across several sessions at the cost of a session's work each time. It is written down once here so it stops costing anything until DJ is ready.

### 26.1 The disagreement

`BookComponentStandard.md` §5.0 and the RoboLore brand repository (`github.com/Weymuth/RoboLore`, private) both define a palette named **Heritage Blue** with the same five colour names and **five different hex values**:

| Name | RoboLore `ColorPalette.md` v01.00.00 | `BookComponentStandard` §5.0 |
|---|---|---|
| Deep Navy | `#0B1A2E` | `#162337` |
| Slate Blue | `#3D5266` | `#43566B` |
| Antique Bronze | `#7B6240` | `#8C6A43` |
| Warm Brass | `#C9A463` | `#C3A36A` |
| Parchment | `#F5F2E9` | `#F4EBDD` |

**Five of five disagree.** DJ's instinct at S93 was that the standard's set supersedes. **He ruled the other way at S101: the RoboLore column is canon** — see §26.8. The S93 instinct is left in place deliberately, because it was wrong and the reason it was wrong is the finding.

### 26.2 The evidence, so it is not re-gathered

Four independent tests, all pointing the same way:

1. **The arithmetic.** `ColorPalette.md` states ten contrast ratios. Its own values reproduce them to **0.02 total absolute error** across all ten; the standard's values give **6.00** — `Deep Navy / Parchment` computes 13.37:1 against a stated 15.61:1. The upstream document was validated against the values it publishes.
2. **Consistency.** RoboLore's five appear **10–15 times each** across `ColorPalette.md`, `ColorPaletteValidation.md`, `Tokens/robolore-colors.css`, `VisualIdentity.md`, and §6 of the instructional standard. **The standard's five appear nowhere in RoboLore.**
3. **The standard contradicts itself.** §9 Numbered marks — LOCKED canon — specifies `fill #7B6240` and `number #F5F2E9`, which are RoboLore's bronze and parchment, not §5.0's. The standard once held RoboLore's values throughout; §5.0's table is the part that moved.
4. **No rationale was recorded, and contrast fell.** Archaeology on the zumo repo: all five values, both title derivations, all four role tints, page colour, body text and the BRAIN CHECK state changed **in one commit** — `c4a90de`, S91, v01.5.0→v01.6.0 — systematically and consistently, so not a typo. But nothing in that commit records *why*, the only S91 "APPROVED" entry covers the roster and says *"This records the roster only,"* and every stated ratio went **down** (navy/parchment 12.75→11.05, slate 7.04→6.36, bronze 5.44→5.11). A contrast-correction pass raises ratios.

**THE GATE GAP THAT LET IT LIVE:** `gen_component.py` never parses §9. §10.1.5 ("every shipped colour comes from the §5 palette") therefore cannot see the one section that disagrees with §5. **The only section carrying the upstream values is the only section outside the gate.**

### 26.3 The semantic three is no longer undefined — it is approved, elsewhere, without purple

The green/amber/purple repaint has been held for several sessions as "unapproved." The committed RoboLore tree supports that reading — `ColorPalette.md`, the CSS tokens and `ColorPaletteValidation.md` all state that functional success/warning/error colours are deliberately not defined. **DJ's uncommitted working tree supersedes that.**

`Standards/InstructionalGraphicStandards.md` **v01.00.00, Status: Approved**, §7 locks a functional palette:

- **Warning gold `#CCA700`** · **Error red `#F44747`** · **Syntax green `#6A9955`** (plus editor neutrals, syntax blue/orange/cyan, function yellow)
- *"Warning gold is functional and must not be replaced with Warm Brass."*
- *"Error red is functional and must not be presented as a RoboLore brand color."*

**There is no purple in it.** THE WALL and BRAIN CHECK have no home in that palette — either they take a §7 colour or purple is added there as a further functional token. Unresolved.

**AND §6 CARRIES A RULE AIMED AT THE BOOK'S CALLOUTS:** *"Teaching cards, parameter boxes, and code examples must not be filled or headed with Heritage Blue merely because the graphic belongs to RoboLore. Use neutral surfaces and the functional palette in Section 7."*

**THE OPEN QUESTION, AND IT IS DJ'S:** are the book's callouts "instructional cards" under §6? If yes, §5's entire seven-role Heritage Blue scheme for callouts is off-canon and the semantic three resolves to gold / red / green with a purple gap. If callouts are prose furniture rather than graphics, §5 stands and §7 governs figures only. **Everything else in this section waits on that one answer.**

### 26.4 Why it is parked, not merely open

**Zero of the ten hexes in §26.1 appear in any lesson or page, and zero of the 88 generated marks in `images/icons/` and `images/marks/` are referenced by any page.** Nothing renders either palette. No student sees a wrong colour. The whole question is prospective, which makes it cheap now and expensive after the wiring pass — but it is not urgent, and it must not be ruled on against documents that cannot be cleanly cited (see §26.5).

### 26.5 The filing hazards that must be cleared FIRST

- **The approved instructional standard is at the wrong path.** `Standards/InstructionalGraphicStandards.md` is **v01.00.00 Approved**; `BRANDING/Standards/InstructionalGraphicStandards.md` is **v00.90.00 Draft for Approval** — and the draft occupies the path that the file's own *"Canonical repository path"* field names, and that `CODEX.md` and `VisualIdentity.md` both now direct readers to. **Anyone following the pointer reads the superseded draft.** Diffed: substance identical, only status / version / decision-register rows differ.
- **All of it is untracked or uncommitted.** Both copies are untracked; `VisualIdentity.md` v01.02.00 and `CODEX.md` v01.01.00 are modified and uncommitted. RoboLore is private, so the remote cannot be checked from a session.
- **Until this is committed, a ruling made here would be made against a document that cannot be cited, and would likely have to be made twice.**

### 26.6 Logged, not fixed — §25.10e is misfiled in this Bible

**§25.10e sits at line 1 of this file, above the Bible's own title.** Its siblings §25.10a–d and §25.10f are in place, and there is a gap between §25.10d and §25.10f which is exactly where it belongs. §25.10f opens by discussing §25.10e, so a reader must scroll ~2,300 lines up and past the title to find it. Found S93, not moved — relocating canon prose is a content move and wants a ruling, not an initiative.

### 26.7 The S93 lesson

**A RECORD THAT HAS BEEN EDITED IN PLACE IS NOT A RECORD.** Adding GOING DEEPER to the standard, Claude declined to touch the §7 roster paragraph on the grounds that editing a count inside a DJ ruling would falsify what was approved — and wrote that reasoning into the canon as justification. The reasoning was sound and the premise was never checked. Archaeology showed the paragraph had **already** been retro-edited once: S91 approved twenty-six families and forty-nine marks, and when SAFETY was retired later the same day the paragraph was silently rewritten to twenty-five. It had never held S91's number. The claim was corrected in the same session it was written. **Before protecting a document as a historical record, confirm it has been treated as one.**


### 26.8 THE S101 RULINGS — what is settled, what is not

**Ruled by DJ, S101.** Recorded here so §26.1–§26.7 can stay unedited as the record of how it was settled.

**1. The five are RoboLore's.** Deep Navy `#0B1A2E` · Slate Blue `#3D5266` · Antique Bronze `#7B6240` · Warm Brass `#C9A463` · Parchment `#F5F2E9`. `BookComponentStandard` §5.0 re-derives from these; it is NOT hand-patched, because hand-patching from a changed base is precisely the S91 failure this section documents. §9's numbered marks already carry `#7B6240`/`#F5F2E9`, so §26.2's third test stops being a contradiction with no edit.

**2. Verification, independent of §26.2.** All ten published ratios recompute to **0.018 total absolute error**. Navy's title contrast re-derived from this base lands on **12.75**, the standard's own pre-S91 figure.

**3. A correction to §26.2's framing, per §24.6c.** `BookComponentStandard` §5.0's numbers are **internally correct** — 11.05 / 6.36 / 5.11 reproduce exactly against its own tints. The case for RoboLore's set is provenance, never arithmetic error.

**4. Heritage Blue is BRAND AND STRUCTURE. It is not the callout system.** Per `InstructionalGraphicStandards` §6, which names **callouts** explicitly: *brand colours identify RoboLore, functional colours communicate meaning.* Heritage Blue governs page colour, body text, nav, title block, section caps, PART banners, the §5.0.1 band ramp, numbered marks, and the wordmark. It does NOT govern teaching cards, parameter boxes, code panels, warning panels, callouts, status indicators, or syntax highlighting.

**5. Therefore `BookComponentStandard` §5's seven-role table RETIRES.** It placed slate, bronze, brass and navy into callout roles — the thing §6 forbids. §5.0.1's band ramp survives untouched: wayfinding is structure, and its one-hue/lightness-carries-location rule is exactly right for the brand layer.

**6. The semantic set is UNRULED, not forbidden.** §7's functional palette is scoped to code-centred technical graphics; a general state system is recorded upstream as not approved. Purple was rejected from the BRAND system only, and its use as a functional instructional colour was never discussed — so the book's 136-block `#9b59b6` family survives by default and is DJ's to rule.

**7. Forge Red `#D46554` is the sixth colour.** ⚠️ **SUPERSEDED S102 — see §26.9. It is a FUNCTIONAL colour, not a sixth brand colour; the palette stays five.** The original ruling is left standing below per §26.7, because a record edited in place is not a record. Danger. §22's `#f14c4c` retires. Warning `#CCA700` and Danger stay **distinct states**. Requires an upstream edit to `InstructionalGraphicStandards` §7 and to the eight RoboLore files that assert a five-colour palette.

**8. No gradients, anywhere.** Book, logos, graphics, marks. Retires §6.2, §6.2a, §6.4's title block and §8's second Checkpoint form. Decides the §18.2-vs-§9 debt in §9's favour.

**9. Challenge-card headers: Antique Bronze `#7B6240` + Parchment `#F5F2E9`, 5.12:1.** Bronze-with-navy measures 3.05 and is restricted. Brass-with-navy at 7.47 passes and was rejected on the composition budget — Warm Brass is specified as the rarest colour at 2–6% and 87 headers is not rare.

**10. Repaint scope is C: the brand layer only.** All 1,048 callouts untouched this arc.

#### §26.9 — FORGE RED IS FUNCTIONAL, NOT A SIXTH BRAND COLOUR (S102, DJ ruling: *"Forge is functional."*)

**§26.8(7) is reversed on placement. The hex, the name, the contrast reasoning and the
warning/danger distinction all stand unchanged. What changes is which palette it belongs to.**

**The contradiction that forced the question.** `InstructionalGraphicStandards` §6 states the
principle the whole brand/semantic split rests on — *brand colours identify RoboLore, functional
colours communicate meaning* — and §7 says outright that error red must not be presented as a
RoboLore brand colour. **Danger is meaning.** So S101 filed a danger colour into the brand palette
by way of a split whose founding rule forbids exactly that. The ruling and its own justification
pointed opposite ways and nobody noticed for a session.

**§26.8 was ruled without §6 in front of it.** That is the same shape as §24.6c: a claim inherited
inside a session is a lead, and it survives because the argument around it is sound. Every
supporting number in §26.8(7) was correct — saturation 60 against a 49 ceiling, 4.60:1 on
`#1E1E1E`, the 3.60 floor breach if pulled further — and the conclusion still went to the wrong
document.

**What the reversal buys, measured:**

| | As a sixth brand colour | As a functional colour |
|---|---|---|
| `BRANDING/ColorPalette.md` | amend | **untouched** |
| `InstructionalGraphicStandards` §7 prohibition | must be amended, it contradicts | **satisfied as written** |
| Files asserting the palette is five | **8 to change** | **0 — all correct** |
| Heritage Blue | six colours | **stays five** |

**Filing:** `#D46554` replaces `#F44747` in §7's functional token table. The book's 14 live
`#f14c4c` instances (L02 ×5, L07 ×9) retire to it as already ruled.

**The general rule this leaves behind:** when a downstream ruling obliges an upstream edit, ask
first whether the obligation is evidence the ruling is filed in the wrong place. §26.8(7)
announced that it required amending a prohibition and rewriting eight files. **A ruling whose cost
is that its own canon must be rewritten to permit it is the ruling to re-examine**, not the canon.

#### Still open after S101

- **The semantic set itself.** 27 distinct 4px accent colours are live across the 16 lessons for 30 families; §8's roster documents 11. That gap is the design work, and it is not started.
- **`#f8f9fa`, 641 instances** — a cool grey on what will be a warm page. Larger than any surface ruled above.
- **`#fffbe6`, 87 instances** — the Work-in bar, 1:1 with the card headers.
- **The brand/instructional boundary is not clean.** Page colour is brand, card interiors are instructional, and changing the first breaks the second. `InstructionalGraphicStandards` §6 draws the line as though the two layers do not touch. They touch.
- **§7's token list is narrower than the book uses** — `#c586c0` (50) and `#b5cea8` (2,264) are live and unnamed.
- **The two code-palette drifts** — type cyan `#4ec9b6`→`#4EC9B0` (295), error red `#f14c4c`→`#D46554` (14).
- **§26.5's filing hazards still stand for everything except §26.1.** DJ stated the five himself, so that ruling cites him. Every OTHER claim in this section still cites files that are uncommitted.

---

## 27. THE BOOK IS A WEBSITE, NOT A CANVAS PASTE (v8.90 — NEW SECTION, S103, DJ ruling)

**DJ ruling, S103: *"There will be no pasting html text into canvas. Then I don't have to worry about updates."***

**THE RULING, in one line.** The lessons live at **one** address — the published site — and Canvas
**links** to them. Canvas keeps everything it is actually good at: **reading quizzes, grades, the
syllabus, milestone submissions**. It stops being a second copy of the book.

### 27.1 Why — the copy nobody could measure

`site_parity.py` exists because a clone is not the site (§24, S101). It compares the repository
against what Pages serves, and it found a live 404 nothing else could see. **Nothing has ever
compared the site against Canvas.** Every lesson edit obliged a re-paste, and a re-paste that did
not happen was invisible to all 40 gates, to every instrument, and to the author. A 3.58 MB book
existed twice with an instrument on one copy and none on the other.

**One copy, one push, one truth.** That is the ruling's entire justification and it is sufficient
on its own.

### 27.2 What this retires — inline-only was never a preference

The rule *"all styling is true inline; no `<style>` blocks, no CSS classes"* (§6) exists **only**
because Canvas strips `<style>` and `class=`. Remove Canvas from the delivery path and the
constraint has no remaining reason to exist.

**Measured at S103, the price that constraint has been charging:**

| | Measured |
|---|---|
| Inline `style=""` attributes across 16 lessons | **25,036** |
| CSS declarations inside them | **~67,000** |
| Share of lesson bytes that is inline style | **44%** — 1.56 MB of 3.58 MB |
| `font-family` declarations in the lessons | **2,828**, where a stylesheet needs **1** |
| Absolute `weymuth.github.io` links, forced because a pasted page has no directory to be relative to | **473** across all 16 files |

**And the arc it unblocks.** §26's repaint has been parked since S91 for being a sweep across
sixteen files. In a stylesheet it is a variable. `#f8f9fa` at 641 instances, `#fffbe6` at 87, the
27 live 4px accents against §8's documented 11 — every one of those becomes a declaration instead
of a sweep. **§26 was not too hard. It was priced against the wrong delivery model.**

### 27.3 What it does NOT touch, verified rather than assumed

**Zero of the 40 gates enforce Canvas-safety.** Checked at S103: no gate references `class=`,
`<style>`, or Canvas in any coverage set. The gate suite survives the migration untouched. This
was verified before the ruling was written, not asserted after it.

Interactive tools already ship as Pages-hosted iframes (`timer.html`, `newproject.html`) precisely
because Canvas stripped `<script>`. They are unaffected and get simpler, not harder.

### 27.4 Canvas links point at the INDEX, not at sixteen lessons

A Canvas item per lesson, each deep-linked to `…/lessons/Lesson_NN.html`, rebuilds the update
problem this ruling just solved: sixteen links to re-edit on any move or rename. **Link Canvas to
the index page and let the book do its own navigation.** One link to maintain, whatever happens
downstream.

This matters because a domain move is live but unruled — DJ, S103: *"eventually we might host the
book on robolore.com, but that is a later decision."* The 473 absolute links above are the
exposure. They are converted to relative during the migration, after which the book is
domain-agnostic and no redirect is load-bearing.

### 27.5 Fonts — what actually changes

An `<img>`-loaded SVG still cannot fetch a webfont (§17.3, §17.3a) and **that rule is untouched by
this section.** Graphics stay on `Arial, Helvetica, sans-serif` / `Courier New, monospace`.

What changes is the **page**. A brand typeface becomes the font that actually ships instead of a
declaration that silently falls back — which under Canvas it always was. Until the migration
lands, the lesson pages' shipping font *is* the fallback, and it should be chosen as such.

**Recorded so it is not swept twice:** at S103 the lesson HTML carried **2,828** font declarations
in **8** distinct stacks, of which **0 lacked a working fallback** — nothing is broken, only
inconsistent (2,316 code stacks lead with Courier New, 422 with Consolas). A sweep to reconcile
those 422 was proposed and **parked**, because in a stylesheet it is one line. **Do not sweep what
the migration deletes.**

### 27.6 Passages that rest on the retired constraint

These are **not wrong**; they are conditional on a delivery model now retired, and per §26.7 they
are annotated rather than rewritten as the migration reaches them:

- **§6** — *"All styling is true inline… no `<style>` blocks, no CSS classes (Canvas strips them)"*
- **§6** — the self-stacking grid requirement, chosen because Canvas strips `<style>`
- **§5b / §18.3** — inline colour forced on repaint
- **§11** — *"Markup (inline styles only — Canvas-safe)"*
- the web-tools paragraph naming what Canvas strips, and the iframe rule that follows from it

**The migration is real work and is NOT done by this ruling.** 25,036 attributes and 473 links do
not convert themselves. What this section fixes is the *decision*; the sweep is scheduled work with
its own instrument and its own controls, like every other sweep in this book.

### 27.7 The migration — Lesson 01, and what one lesson proved (S104)

**DJ ruled two runs for safety, and the split was worth keeping** even though the first run is a
no-op by construction: all sixteen lessons carry **zero** `class=` attributes and **zero**
`<style>` blocks, so a class-scoped stylesheet linked into a lesson cannot change a pixel until
the classes exist. Run 1 therefore proves the INFRASTRUCTURE and nothing else — that `css/`
publishes, that Pages serves it as `text/css`, that `site_parity` sees it — and run 2 carries all
of the content risk, against a known-good baseline.

**One stylesheet for the whole book, not one per lesson.** Measured before ruling: 25,036 inline
attributes reduce to **689 distinct declaration strings**, and **92.5%** of instances use a string
that appears in more than one lesson. Sixteen sheets would duplicate nearly all of it and recreate,
in CSS, the sixteen-file sweep this section retired.

**`css/`, not `images/`.** Neither breaks a gate — verified by reading `book_gates.py`, not
assumed. But `images/` is the declared scope of seven instruments, and a stylesheet survives there
only because every one of them happens to filter by extension. That is an accident holding, not a
rule.

**THE HELD BLOCKS.** Three constructs are compared BYTE-EXACT ACROSS LESSONS — the §6.5a lesson
strip, the §25.6 header/footer, and the §6.8 PART dividers. Converting them in one lesson makes
that lesson the odd file out and fails those gates correctly. They stay inline until they convert
book-wide in one generated pass. In L01 they are **39 of 1,150** attributes.

**THE CLASS EXPANDER, and why it is one function.** Six gates read CSS VALUES out of the markup —
§22's terminal colours, §25.2 and §25.10h on the Brain Check wrappers, §6.8a's "is this anchor
seated in a banner", and both §5.1 gates through `lesson_inventory`'s `CALLOUT_RE`. All six go dark
on a converted lesson. `lesson_inventory.expand_classes()` expands every class back into its
declarations **for reading only**, and `book_gates` reads through it, so no gate has to learn what
a class is. The S83 rule: import the definition, never write a third regex.

**GATE 41 (§27) — every class in use resolves to a rule in `css/book.css`.** THE MIGRATION CREATES
THIS FAILURE MODE. Measured, not argued: typing one callout's class as `callout-typo` dropped
L01's callout census from **83 to 82 with all 40 gates green**. Before the migration a mistyped
inline style left the element visibly wrong and fully parseable; after it, a mistyped class makes
the element **invisible to every CSS-reading instrument**. An element that vanishes is worse than
one that is wrong, because only one of the two gets found. Scoped to pages that LINK the
stylesheet — scoping it to `site` failed on tutor/newproject/timer/index/going_deeper, which carry
their own `<style>` blocks and 194 classes between them (§25.6a: the tool pages are not chapters).

**CLASS NAMES ARE PROVISIONAL AND GENERATED.** `build_css.py` emits `css/book.css`; §24.12 applies
and the CSS is never hand-edited. A name is English only where the declarations PROVE the role
(`.code-block-bg-1e1e1e`); anything whose meaning would have to be guessed carries its hex
(`.callout-2196f3`, `.tok-6a9955`). §8 documents 11 of 27 families and LEARN and INSIGHT still
share `#e3f2fd`/`#2196f3`, so a confident semantic name would be a claim this repo cannot support —
and a wrong name propagates into sixteen lessons. The semantic set is the paint arc's first item
and is not started. Renaming later costs one line in the generator plus a re-emit.

**THE PROPERTY THAT MAKES A STRIP SAFE**, asserted every run: for every styled element, the class
it receives carries declarations CANONICALLY EQUAL to the inline string it replaces. L01's
conversion is therefore render-identical **by construction** — 1,150 elements, document order,
same declarations, visible text byte-identical — not by inspection. Measured result: 204,356 →
**154,731 B**, 24% smaller, with the stylesheet cached once.

**AN ASSERTION THAT EXPIRES ON SUCCESS IS WORSE THAN NONE.** Two of `build_css`'s own controls
died the moment run 2 landed: one counted raw `style="` in a source that no longer has them, and
one asserted "zero class attributes exist" — true during run 1 and false forever after. Both were
rewritten to state what must hold AFTERWARDS. Write controls for the world the change creates.

### 27.8 The migration — the remaining fifteen, and the three ways a widened build bites (S105)

**ALL SIXTEEN LESSONS ARE CONVERTED.** 24,412 inline `style=""` attributes became classes against
a 664-rule `css/book.css`; **624 held** — 39 per lesson, every lesson, no exceptions. 24,412 + 624
= **25,036**, the §27 census exactly. Zero unmapped, zero dead classes, 41/41 gates. Render
identity proved as at S104, **by construction and then independently**: 25,036 styled elements
compared in document order against the pre-conversion tree, declaration sets identical, visible
text identical apart from one `<link>` line per lesson. Census 39,979 → **39,994** (+15, the
fifteen links). Lesson bytes 3,534,934 → **2,638,947**, 25% smaller; counting the 81,806 B stylesheet
once, 23%.

**§27.8a — WIDENING `build_css.SOURCES` RENAMES RULES, AND THE RENAME IS MOSTLY INVISIBLE.**
Naming is frequency-ranked across the corpus, so adding fifteen lessons reshuffled it: **57 of
L01's 167 names changed meaning. 46 KEPT THEIR SPELLING** — `.link-c-2e86ab` and `.link-c-2e86ab-2`
literally swapped bold for non-bold — and only the 11 that vanished were visible to gate 41. A
name that still resolves repaints the page with every gate green. **Every already-converted lesson
must therefore be re-stripped whenever `SOURCES` changes.** This is not a rollback; it is what
makes the conversion re-runnable.

**§27.8b — THE ORDER IS FORCED, BECAUSE THE WRONG ONE DESTROYS DATA.** `expand_classes` reads the
stylesheet **from disk** and, by design, leaves an unresolvable class **in place** rather than
failing. So regenerating `book.css` before restoring an already-converted lesson strands every
element carrying a dropped name — 74 elements in L01, unrecoverable, and silent everywhere but
gate 41. The sequence is **`strip_inline --restore` → `build_css` → `strip_inline --apply`**, and
it is not negotiable. Proved the hard way in a sandbox: a sorted build destroyed authored
declaration order, and the restore afterwards handed back alphabetised declarations that no
generator would ever accept.

**§27.8c — `canon()` SORTS; THE GATES ASSERT AUTHORED ORDER.** Grouping by a sorted canonical form
is right — order is not meaningful to a browser — but **the gates are not browsers.** §4.5, §6.8
and §25.6 assert style strings byte-exact against their generators, and they broke the moment the
stylesheet handed back alphabetised declarations. **The handoff's hold list named four block types;
there was a fifth**, the §4.5 bonus banner (cap, panel and nav pill). The fix is one rule, not five
holds: `build_css.preferred()` emits each rule in its **authored** declaration order — the majority
spelling in the group, ties broken by string for determinism. Result: **23,364 of 23,886**
attributes round-trip byte-exact through the expander; the remaining 522 converge on a sibling
spelling that `canon()` had already proved render-identical. **When a whole class of gates fails at
once, fix the generator, not the instances** — holding blocks until the gates go green is §24.8
wearing a hard hat.

**THE HOLD, unchanged and now book-wide.** §6.5a strip (20) · §25.6 hero (6) + footer (1) · §6.8
PART dividers (4 × 3). These convert book-wide in one generated pass, still outstanding.

**`strip_inline.py` v1.0 (§24.12) — the tool S104 did not commit.** `--plan` / `--apply` /
`--restore` / `--verify` / `--selftest`, eight controls. Fifteen hand conversions is fifteen chances
to differ. It never invents a class: an attribute whose declarations have no rule is left alone and
**reported**, and a non-zero unmapped count is exit 1. Held blocks are located **by marker, never by
offset**. Its CONTROL H is the load-bearing one — marker-derived locators independently reproduce
S104's hand-picked 39 held attributes in L01, two unrelated processes arriving at the same number.
CONTROL G encodes §27.8b so no later session steps into it.

**AND ONE MORE EXPIRING CONTROL, caught by the instrument itself.** `session_versions`'s CONTROL A
seeded its corruption with the literal string `Lesson version: v03.20.0`. The moment L03 bumped,
the seed matched nothing, nothing was corrupted, and nothing surfaced — the control **failed loudly
rather than passing silently**, which is the right direction for the wrong reason. Seeds are
patterns now, with an assert that something was actually seeded. S104's rule has now caught three
controls in two sessions: **write controls for the world the change creates.**

**§27.8d — A GENERATED ARTEFACT HAS NO EXCUSE TO BE INTERNALLY INCONSISTENT.** `preferred()`
returns an AUTHORED string, and the book authored **62,602** declarations as `prop: value`
against **1,139** as `prop:value` — so a faithful emitter shipped both spellings into one
generated file. DJ's ruling: *"I don't care either way, I just want it to be consistent."*
**Spaced wins on both counts.** It is 98% of the source, and emitting unspaced broke **five
gates** (§22, §25.2, §25.10h, §4.5, §4.5a), which assert literal `prop: value` strings — the
same §27.8c fault line, found by testing the alternative instead of assuming. `build_css`
normalises the SEPARATOR only; declaration ORDER still comes from `preferred()`. All 2,434
emitted declarations and all 2,992 held inline declarations now carry one spelling. The
sixteen lessons were **byte-unchanged** by this — class names are derived from the canonical
form, which is spacing-insensitive, so only the stylesheet moved.

### 27.9 The hold released — zero inline styles book-wide (S105)

**THE BOOK NOW CARRIES 25,036 CLASSES AND NOT ONE `style=""` ATTRIBUTE.** The four block types
held through the sweep — §6.5a strip (320), §25.6 hero (96) + footer (16), §6.8 PART dividers
(192) — converted book-wide in one pass. Lesson bytes 2,638,947 → **2,582,947**. Census
unchanged at 39,994. Render identity proved independently over the whole population: 25,036
elements, zero mismatches, visible text identical in all sixteen.

**WHY THE HOLD COULD BE RELEASED, AND WHY IT WAS RELEASED BY MEASUREMENT.** Those blocks were
held because §6.5a/§25.6/§6.8 compare them **byte-exact ACROSS lessons** and read through
`expand_classes`; converting one lesson at a time is what those gates exist to catch. Two facts
made the single pass safe, both measured rather than assumed: the 624 attributes carry only
**16 distinct strings**, each appearing an exact multiple of 16 — proof they were already
uniform book-wide — and **all 16 round-trip byte-exact** through the stylesheet, which is only
true because §27.8c made the emitter preserve authored order and §27.8d gave it one colon
spelling. The precedent was already in the tree: §4.5's bonus banner was never held, and its
byte-exact gate passes for exactly this reason.

**`strip_inline --include-held` IS GATED ON A PRECONDITION, NOT A PROMISE.** The flag runs
`roundtrips()` first and REFUSES, naming the offenders, if any held string cannot be handed back
unchanged by the stylesheet. CONTROL I proves both directions — a byte-exact string passes, a
string the rule cannot return is refused and named. A flag that trusts its operator is not a
flag, it is a footgun.

### 27.10 The book is domain-agnostic — 496 self-references made relative (S105)

**NOT ONE PAGE NAMES ITS OWN DOMAIN ANY MORE.** 478 absolute `href`/`src` attributes and **18
JavaScript string assignments** pointing at `https://weymuth.github.io/zumo/` became
relative-to-the-page. All 496 lived in the sixteen lessons; the root pages already used relative
paths. Lesson bytes 2,582,947 → **2,569,059**. Census unchanged at 39,994, visible text identical
in all twenty pages.

**THE 18 JS REFERENCES WERE INVISIBLE TO EVERY ATTRIBUTE-SHAPED SEARCH.** The Brain Check gear
swap assigns `img.src` from a string literal in a `<script>`, so `_REF_RE` — which matches
`src=`/`href=`/`xlink:href=` attributes — never saw them, and neither did the first sweep. They
surfaced only because the sweep's leftover count was audited instead of assumed: 18 mentions
remained after 478 were converted, and reading them was what identified the shape. **A sweep's
remainder is evidence; a sweep that reports zero remainder without being asked is not.**

**SEVEN OFF-SITE REFERENCES REMAIN AND MUST.** Google Fonts (4), `raw.githubusercontent.com` for
`ZUMO_Template.zip` (2), the jszip CDN (1). Domain-agnostic means the book does not name ITS OWN
host; it does not mean the book has no external dependencies.

**THE ABSOLUTE FORM IS NOW A REGRESSION, NOT AN ALTERNATIVE.** The going_deeper gate previously
allow-listed both spellings, which was correct while the book hard-coded its domain and is wrong
now. It derives the expected depth from the page — `../going_deeper.html` under `lessons/`, bare
at root — and was control-run against BOTH regression shapes (an absolute URL, and a
right-spelling-wrong-depth relative one) before being trusted. `book_gates` **v1.35.2**.

**WHAT THIS BUYS.** The book can be served from any origin — a different Pages repo, a custom
domain such as robolore.com, a local `file://` tree, or a student's offline copy — with no
edit.

**GATE 42 (§27.10) EXISTS BECAUSE THE OTHER 41 CANNOT SEE THE DEFECT.** §21's resolver
deliberately understands the absolute prefix, so reverting one image `src` back to
`https://weymuth.github.io/zumo/...` resolves to the same file and passes **every one of the 41
gates** — measured by seeding exactly that, not assumed. A broken RELATIVE path is caught by §21;
a reverted ABSOLUTE one was invisible, which is the same asymmetry §27 found in gate 41. Scope is
deliberately WIDER than `href`/`src`: it matches the domain anywhere in the file in any syntax,
because the 18 JS string literals hid from the S105 sweep for precisely that reason and a third
reference shape must not be able to reopen the hole. Control-run against three shapes — a reverted
image `src`, a reverted JS string literal, and the bare domain in an HTML comment — loud on all
three. Off-site hosts are out of scope by design. `book_gates` **v1.36, 42 gates**.

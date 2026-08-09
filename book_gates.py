#!/usr/bin/env python3
# book_gates.py — whole-book consistency gates.
# VERSION below is the ONE home, and it sits ABOVE the changelog so a plain grep of this
# file lands on the live version, not on a changelog line (S98).
VERSION = 'v1.64.2'
# v1.60 (S132): GATE 65 NEW - §27.15f, THE REVEAL BOX. 453 <details> in THIRTEEN spellings
#   plus 55 with no class at all, whose summaries therefore had NO cursor: pointer - the one
#   part of the drift a reader would have felt. Graduated to an element rule. The gate is
#   gate 57's assertion on a second construct and asserts the RATIO: #dee2e6 on #f8f9fa is
#   1.24:1, LOWER than the #333 gate 57 exists to have retired. Control-run five ways from a
#   snapshot of the FIXED tree - the old #dee2e6 restored, #919191 (2.99:1, one step under),
#   cursor:auto, the named hold's `border: none` removed, and a stray class on one summary.
#   All five fire gate 65; the three that edit the layer also fire §27.13 and §27.15, which
#   is correct rather than noise - those gates guard the layer's integrity, so any edit to
#   it moves them. Untouched tree passes at 65 of 65 at both ends.
# v1.59 (S132): GATE 64 NEW - §24.14b, the STRUCTURE tier's predicate. build_family_map
#   v1.5.0 added a tier reading "a callout in the GLOSSARY REGION is a KEY TERM" (97 of 97
#   today, zero exceptions). That is true and an author can break it with one paste, so the
#   ruling and its gate ship together. IT ASSERTS THE PREDICATE, NOT THE TIER'S OUTPUT:
#   asking the tier whether it returns KEY TERM is circular, so the gate BLINDS the tier and
#   asks whether any other tier resolves a glossary-region block to something else. Silence
#   is legal - once the 87 glossary-side pin rows retire, most of these resolve to nothing
#   with the tier blinded, and nothing is not a contradiction. Arm 2 pins the banner ROSTER
#   rather than the wrapper class, because the first probe of this arc keyed the region on
#   `div-bg-*`, which L04's glossary banner does not wear, and returned ZERO regions for L04
#   - a false clean by omission (rule 19: pin the property). Control-run both ways from a
#   snapshot of the FIXED tree: a NOTE relocated into L10's glossary fires the contradiction
#   arm, breaking L04's banner shape fires the roster arm, each ALONE at 63 of 63 others
#   green, untouched tree passing at both ends.
# v1.58 (S131): GATE 63 NEW - §10, a figure is landed by an asset and never by a decoration.
#   S130's 884 marks landed in the same prose image_audit's NEIGHBOUR arm reads, and the arm
#   could not tell a lightbulb from a photograph: six real shots - L03 3.2 / 3.5 / 3.6,
#   L12 12.1, L14 14.1, L16 16.1 - went from outstanding to LANDED with nothing taken. NO
#   GATE FAILED. The only signal was `image_audit --check` printing DIFFERS, whose obvious
#   reading is "re-run me" - which would have written 8 over 14 and retired six entries from
#   the shot list four weeks out. THE ARC WAS MEASURED ON THE CONSUMERS THAT WERE WATCHED
#   (S130's own lesson, one instrument later). The gate re-derives landing from FILENAMES ON
#   DISK with its own regexes and never asks image_audit the question that matters, so it
#   fails on whatever a future arc decorates the prose with, not just on `data-mark`.
#   Disagreements are a NAMED set with a reason each, and arm 4 fails a name that has stopped
#   needing the exemption (S130 rule 20). Coverage arm included (S117/S118). Control-run four
#   ways from a snapshot of the FIXED state: the defect reproduced end to end (old
#   image_audit + the worklist it emits) names all six; a deleted worklist row; IMAGE 10.1
#   dropped from REUSE; a non-load-bearing name added. Each fires gate 63 ALONE at 62 of 62
#   others green and exit 1, untouched tree passing at BOTH ends, all three files restored
#   byte-identical. `image_audit` reaches v1.2 and the worklist returns to 14 of 141 -
#   byte-identical to the repo copy but for the version line, which is the check that the fix
#   restores exactly the pre-marks answer and no more.
# v1.55 (S128): GATE 59 NEW - §24.14a, every callout carries the family its CONTENT
#   resolves to. Written in the same pass as the ruling (S126 rule 16). Before S128, 209
#   of 1,069 blocks were identified ONLY by their decorative emoji - build_family_map's
#   GLYPH tier, which S112 shipped calling itself a stopgap and predicting exactly this
#   moment. The marks arc replaces that emoji with an <img>, and those blocks would have
#   lost their only family signal, failing gate 47. The family now lives in the markup.
#   IT ASSERTS THE PROPERTY, NOT PRESENCE (S126 rule 18): it re-derives the family through
#   family_tag - which imports build_family_map's own tiers, never a second copy (S83) -
#   and requires the attribute to AGREE, so a hand-typed attribute contradicting its own
#   content fails exactly like a missing one. Coverage arm included, because a gate that
#   scans zero blocks passes (S117/S118). Control-run four ways from a snapshot with
#   read-back and restore asserts - attribute deleted, wrong family, nonexistent family,
#   emptied - each firing gate 59 ALONE at 58 of 58 others green, untouched tree passing
#   at BOTH ends, and the file restored byte-identical.
# v1.52 (S126): §27.12 SCOPE EXTENDED to semantic-layer consumers (DJ ruling) and to
#   index.html BY NAME (§25.2a); §27 gains the COVERAGE arm it never had; and BOTH gates
#   stop keying scope on a bare substring. Three defects found in one pass, each by the
#   next one: (a) a COMMENT mentioning css/book.css pulled going_deeper.html into §27's
#   scope, because the predicate was `'css/book.css' in src`; (b) the specific predicate
#   that replaced it demanded href="css/book.css" and the lessons link "../css/book.css"
#   (§27.10), so it matched ZERO pages and §27 PASSED on an empty scope; (c) that was
#   caught ONLY because gate 44 carries a coverage arm and §27 did not -- S117/S118 for
#   the third time. COMPLEMENTARITY MEASURED: an inline style pasted into going_deeper's
#   preamble FAILS §27.12 alone under the new scope and is INVISIBLE under the old one.
# v1.51.1 (S126): §27.11 baseline 627/2,297 -> 624/2,282 after L03's five classed
#   inline <code> elements were stripped per §27.15a's no-exception rule. Three rules die,
#   zero born, zero altered; the -15 declarations IS those three at five each. Control-run
#   after the move: a deleted `color: white;` still FAILS §27.11, alone.
# v1.51 (S125): NEW GATE 56 (§27.15c). §27.15c ruled going_deeper.html onto the semantic
#   layer and shipped UNGATED. The sixteen lessons reach the layer through css/book.css,
#   which gate 54 holds byte-for-byte; going_deeper reaches it through a direct <link> that
#   nothing held at all. Measured by injection BEFORE this gate was written, three ways,
#   each leaving all 55 preceding gates green and exit 0: delete the <link>, restate the
#   old dark rule in the page's own <style>, or point the href at a file that does not
#   exist. Carries a COVERAGE arm, because a gate that scans zero pages passes (S117/S118).
# v1.50 (S124): NEW GATE 55 (§27.15a). The pill graduated and the graduation happened by
#   DELETION - 2,132 class attributes stripped, ten rules dead, one BORN. The birth is the
#   finding: build_css names a rule after its DOMINANT TAG, so stripping a class from SOME
#   of its users RENAMES it for the survivors. Three compiler-error <span>/<strong> elements
#   sharing .code-ff-uimonosp-2 with four <code> elements went dead the moment the <code>
#   ones left, and no gate saw it - strip_inline --verify did. The recovery order is
#   load-bearing and now canon (§27.15b): strip, regenerate, move the survivors onto the
#   name pass 1 emitted, regenerate again. Renaming after a SECOND pass is unrecoverable,
#   because the generator can only preserve a class it can still resolve.
# v1.49 (S123): NEW GATE 54 (§27.15, the semantic layer) and §27.11 SCOPED to the generated
#   block. Rules and declarations hold UNCHANGED at 636/2,332 across the change, which is
#   the point: adding the semantic layer moved nothing generated, and only the digest moves
#   because the span it covers now starts at the GENERATED BLOCK marker. Scoping also fixed
#   a mixed population this session created - _r counted class rules while _d counted every
#   declaration, so one added element rule read as 'a rule gained or lost a property', the
#   precisely wrong diagnosis in this gate's own words. Gate 54 exists because the failure
#   mode is SILENT: measured by injection before the layer was built, an element rule pasted
#   into css/book.css did not error and did not warn - the next regeneration DELETED it and
#   every gate stayed green.
# v1.48 (S123): NEW GATE 53 (the one mono stack) and the 27.11 baseline moves for DJ ruling
#   B-FULL. FINAL: 641/2,350 -> 636/2,332. GATE 53 EARNED ITS PLACE ON ITS FIRST RUN and
#   resized the problem: the Consolas lead this session opened with was the MINORITY. The
#   book carried 'Courier New', monospace in 21 rules at 2,825 uses against Consolas at 14
#   rules / 459, and font_stack_sweep is structurally blind to it because its first face is
#   not a named substitution risk. Diffed by SELECTOR: 39 mono rules before, 10 DIED and 29
#   ALTERED, 39 = 10 + 29, nothing non-mono moved. Five of the ten are font-named classes
#   replaced by .code-ff-uimonosp*; the other two, .code-block-333-6 and
#   .code-inline-bg-e8e8e8-7, COLLAPSED into .code-block-333-5 and .code-inline-bg-e8e8e8-6,
#   proved by comparing their declarations with font-family removed rather than assumed from
#   the rule disappearing. strip_inline --verify 0 dead class names.
#   B. 641/2,350 -> 640/2,349, diffed by SELECTOR: three rules DIE (.code-ff-consolas,
#   .code-ff-consolas-2, .span-ff-consolas), two are BORN (.code-ff-uimonosp,
#   .code-ff-uimonosp-2) and twelve are ALTERED. 15 = 3 + 12, which is every Consolas-
#   carrying rule accounted for, and the net -1 is two rules collapsing into one. Only the
#   classes whose NAME encodes the font were renamed; .code-block-bg-1e1e1e keeps its name
#   because it is named for its background. Re-controlled after the move against a dropped
#   `color: white;`, which still FAILS.
# v1.47 (S123): NEW GATE 52 — the §3.1b opener is UNIQUE inside its section. Gate 51
#   counts occurrences of the CORRECT opener and finds one; a section holding the correct
#   opener PLUS a stale duplicate satisfies that count. Measured by injection: a second
#   opener carrying the historical wrong title "Line Following" pushed into L07 left ALL
#   51 preceding gates green and exit 0. Not a synthetic shape — S122 committed exactly
#   this defect to L05 by reading an audit result instead of the file. The regex and the
#   section bounds are IMPORTED from title_feed (S83's rule), so the pattern has one home
#   and gate 51's spelling cannot drift away from the generator's.
# v1.46.2 (S122): NEW GATE 51 (§3.1b) plus the Tier-1 normalizations, and this is the
#   first baseline move of the arc where rules actually DIED. 643/2,357 -> 641/2,350:
#   .link-c-2e86ab-3 and .link-c-2e86ab-4 are gone, and the -7 declarations ARE those two
#   rules. Both existed only to shrink the back-to-top link to 0.9em and 0.85em in five
#   lessons; normalizing 89 links to one markup left them with zero uses, verified by
#   grep across every page, not inferred from the rule dying. Zero born. Re-controlled
#   against a dropped `color: white;`, which still FAILS.
# v1.46.1 (S122): §27.11 DIGEST BASELINE MOVED, and the cause is S113's shape for the
#   FIFTH time. The What's Next? consistency arc re-classed one h3 in Lesson 3 from
#   .h3-c-2e86ab to .h3-c-6f7582 and seated eight NEW headings on the latter. Both
#   classes already existed, so nothing was renamed: usage went 83 -> 82 and 42 -> 51;
#   build_css orders rules by usage RANK, so one rule relocated by a single
#   position and two count comments changed. Diffed by SELECTOR: 643 rules, ZERO born,
#   ZERO died, zero declarations altered, 14 changed lines all comment or relocation.
#   Re-controlled after the move against a dropped `color: white;`, which still FAILS.
# v1.46 (S121): NEW GATE 50 — §3.1a, every lesson 01-15 ends with a working link to the
#   next lesson. The book had a forward pointer in prose in 13 lessons and NO clickable
#   link in any of the sixteen: measured, zero <a href> to a lesson file in any lesson
#   tail. The gate asserts existence, the CORRECT successor, seating above the §5b footer,
#   and that L16 carries none. Control-run four ways from a pristine snapshot, each naming
#   the lesson and the defect. Also moves the §27.11 digest, digest-only, S113's shape.
#   PROCESS NOTE worth more than the gate: the first control harness restored with
#   `git checkout --`, which reverts to the COMMITTED tree — and the work was uncommitted,
#   so every 'restore' DELETED the block instead of replacing it and three controls ran
#   against an already-failing tree. The untouched-tree control is what exposed it. A
#   control harness needs its own pristine snapshot; version control is not one when the
#   thing under test has never been committed.
# v1.45 (S119): NEW GATE 49 — §25.10l, Brain Check 01 carries exactly FIVE items.
#   A CONSTANT, not a baseline: the conversion arc closed at S119 and BC_PENDING is empty,
#   so unlike §21 coverage or the family-map total this number has no legitimate future
#   move. It exists because the norm was 14/14 and UNHELD — S119 came within one ruling of
#   breaking it silently on a question asked from a false premise. Control-run four ways:
#   an item deleted FAILS naming 4, an item added FAILS naming 6, brain-check-01 removed
#   FAILS on COVERAGE, and the unperturbed book passes.
# v1.44.5 (S119): L15 IS THE FOURTEENTH AND LAST CONVERSION. BC_PENDING is now EMPTY --
#   the arc that began at L01 closes here, and the set is kept rather than deleted so a
#   future L17 has a home. L15's SECTION 2 needed NO reword (verb-first already) but
#   carries no box glyph at all, so BC02 supplies the literal box and the equality assert
#   normalises it away -- L01's shape, not L13's. BC03 is SIX, not five: its ancestor is
#   SECTION 10's 'say out loud' list, which no retired-name sweep names, plus one item
#   authored on DJ's S119 ruling for objective 7. 21 coverage 245 -> 250 (four block
#   icons plus the column emblem). 27.11 rules and declarations UNCHANGED at 643/2,357;
#   only the digest moves, S113's shape -- zero rules born, zero died, zero altered.
# v1.44.4 (S118): L13 IS THE THIRTEENTH CONVERSION. '13' leaves BC_PENDING in the same
#   edit that seats its four Brain Check blocks. L13 had NO ancestor of any kind --
#   zero pre-6 reveals, no checklist, no Knowledge Check -- so BC01/BC03/BC04 are
#   authored and BC02 migrates SECTION 2's six objectives, which were reworded
#   verb-first in the same edit (DJ ruling S118, option A) because L13 was the only
#   lesson in the book whose objectives were noun phrases.
# v1.44.3 (S117): L12 IS THE TWELFTH CONVERSION. '12' leaves BC_PENDING in the same
#   edit that converts the lesson. THREE BASELINES MOVED, each controlled both ways:
#   27.11 644/2,362 -> 643/2,357, diffed by SELECTOR — exactly one gone (.div-ddd-3,
#   the consumed Exit-Ticket checklist box, 5 decls, and the -5 IS that rule), ZERO
#   born, ZERO altered, so no class RENAME (S116's shape, not S115's); 21 coverage
#   235 -> 240 (sole delta BrainGear_Incomplete.png 55 -> 60, +5 = four block icons
#   plus the column emblem); family map 1057 -> 1061 (build_family_map v1.3.5),
#   exactly ONE family moving, BRAIN CHECK 44 -> 48, the other 29 byte-identical.
# v1.44.2 (S116): L11 IS THE ELEVENTH CONVERSION. '11' leaves BC_PENDING in the same
#   edit that converts the lesson, which is what the named sets were built for - control-run
#   with '11' left in and the gate NAMES L11, where a count could only have said 10.
#   THREE BASELINES MOVED, each controlled in both directions: 27.11 645/2,365 -> 644/2,362
#   (one selector gone, .div-bg-eafaf1, 3 declarations - the -3 IS that rule; zero born, zero
#   altered, so NO class RENAME this time, unlike S115); 21 coverage 230 -> 235 (sole delta
#   BrainGear_Incomplete.png 45 -> 50); family map 1053 -> 1057 (exactly ONE family moves,
#   BRAIN CHECK 40 -> 44, other 29 byte-identical). After the moves: a deleted `color: white;`
#   still FAILS, a deleted callout still FAILS at 1056/1057, a broken image ref still FAILS.
#   NOTE v1.44.0 and v1.44.1 (S115) carry NO changelog line here - the version moved in the
#   constant only. Recorded, not backfilled: this file is not the place to reconstruct S115.
# v1.43.2 (S113): §21 coverage 224 -> 225 and the §27.11 digest moved, both because L03
#   IMAGE 3.14 was wired in from a supplied photo. Two baselines, one cause.
# v1.43.1 (S113): §27.11 digest moved a second time, same session, same shape - two more
#   figure placeholders retired. Rules and declarations did not move.
# v1.43.0 (S113, DJ ruling): gate 28 now checks the handoff's NUMBER, not just that there
#   is one of it. Filename vs title vs 'paste at top of Session N', all three parsed.
# v1.42.2 (S113): §27.11 digest baseline moved, deliberately, for one content change.
#   Rules and declarations did not move; only the digest. See the note at the constant.
# v1.41.0 (S112): GATE 46, §27.14 - every link and every id resolves. 1,237 links and 705
# ids across twenty pages had NO gate at all. Control-run on four shapes: dead in-page
# anchor, duplicate id, missing file, dead cross-page fragment - each named individually,
# with a RESOLVING cross-page fragment planted beside the dead one so the branch is
# exercised both ways. WHERE THE BLOCK SITS IS PART OF THE GATE: appended below the summary
# it printed PASS after 'ALL GATES PASS' on a clean tree and never ran at all on a failing
# one, because sys.exit fired first.
# v1.40.0 (S111): THE REPAINT. BAND_END #6c757d -> #6f7582 and the four PART spine colours
# moved to the eight-band palette; §27.11's baseline moved twice (the [IMAGE 2.5] retirement,
# then the icon legend + repaint) and both moves carry their accounting; GEOM_BASELINE keys
# followed BAND_END automatically because S109 had already made it a constant. THE TRAP:
# build_palette emits UPPERCASE hexes and every value parsed out of the book is lowercase.
# The mismatch PASSED §5.1 and failed four other gates, which sent the first diagnosis in the
# wrong direction. All literals here are lowercase and the repaint was normalised to match.
# v1.39.2 (S109): BAND_END. The §10+ section band was typed literally in ELEVEN places -
#   five inline sites plus six GEOM_BASELINE keys - so §5.0.1's ramp could not land as an
#   edit. Now one name. Refactor asserted BEHAVIOUR-NEUTRAL: gate output byte-identical
#   before and after. But byte-identical is also what a DEAD constant produces (§24.8),
#   so it was control-run by flipping BAND_END to DJ's Steel #708BAF: FOUR gates fail -
#   §25.10h, §4.5, §4.5a and §5.1. The S108 handoff named THREE and missed §5.1, whose
#   GEOM_BASELINE keys would have fired mid-ramp with no warning. That is the count.
# v1.39.1 (S109): gate 27.11's printed label was hard-coded and stale (664/2,434) while
#   its constants tested 660/2,418 - right test, wrong name. The label is now derived
#   from CSS_RULES/CSS_DECLS. No test logic changed; control-run against a perturbed
#   baseline confirms the name follows the constant and the gate still fails loudly.
# v1.39.0 (S108): the F1 banner pilot. _fence_title() now knows TWO cap shapes - the legacy
#   one-line 'icon Section N: Name - Tail' and F1's eyebrow/headline span pair - because F1
#   DELETES the em dash the old rule split on, and the sixteen lessons are mixed until the
#   rollout. The end-matter gate accepts id="figures" as well as id="image-index" and now
#   REPORTS a missing anchor instead of silently continuing, which is how it would have gone
#   quiet on every converted lesson. CSS baseline moved deliberately, +2 rules / +11 decls.
#   All four changes control-run both directions against L03 (new shape) and L04 (legacy).
# v1.38.2 (S106): §21 coverage 223 -> 224 and the §27.11 digest moved, both because
#   L02 IMAGE 2.2 was wired in. Rule and declaration counts did NOT move.
# v1.64.2 (S138): §17.3c coverage 31 -> 32, L04_GRAPHIC_4-07 joined the book.
# v1.38.1 (S106): §17.3c coverage 27 -> 28, L02_IMAGE_2-02 joined the book.
# v1.38 (S106): NEW GATES 44 (§27.12) + 45 (§27.13) — the migration's two unguarded
#   invariants. 44: a page that links css/book.css carries no inline style attribute.
#   Seeding one <p style="color: #ff00aa"> into L05 left ALL 43 preceding gates green;
#   the element renders correctly while re-opening the hole the whole migration closed.
#   45: css/book.css regenerates byte-identically from the lessons. This is the guard on
#   §27.8a/b — regenerate without re-stripping and 46 class names keep their spelling and
#   change their meaning, invisible to gate 41. Gate 43's digest catches the regeneration,
#   but §26's repaint MOVES that baseline by design, and a moved baseline is a spent gate;
#   45 re-derives instead of remembering, so a repaint does not spend it. Control-run in
#   both directions: 43 fires and 45 is blind on a hand-edited stylesheet (CONTROL B), 45
#   fires and all 43 are green on one element retyped to a different resolvable class
#   (CONTROL C). Neither subsumes the other. `strip_inline --verify` was OFFERED and NOT
#   added: it is gate 41's assertion computed twice and never fired independently of it.
# v1.34 (S100): NEW GATE 40 — §21.1b fragile-if-edited. Advisory, never fatal. Names every
#   referenced composite that is fine today but would breach the ceiling if an Illustrator
#   round-trip returned its payload lossless. It flags L01 1-10 at ~1,938,090 B — which is
#   S99's actual incident, 439 KB up and 2.37 MB back, predicted instead of discovered.
#   DJ asked to convert the two JPEG payloads to PNG pre-emptively; measurement said no.
#   Lossless PNG is over the ceiling and palette PNG that fits costs 4x the drift of JPEG
#   q92. The fix is the warning, not the conversion. PIL import is GUARDED: absent, the
#   gate says so and stays green, because a crash is worse than a missing advisory.
# v1.33 (S100): NEW GATE 39 — §17.3c, plain href on <image> is SVG 2 and Illustrator
#   cannot read it: the composite renders perfectly and will not OPEN. S99 found this by
#   hand after every composite in the book was already broken; it was then recorded only
#   in svg_layout_audit, which this suite does not run. Advisory is how it regressed. Also
#   catches xlink:href used without xmlns:xlink. Gate 38's coverage 186->177 and 76->67:
#   nine drawn graphics became photo composites in S100 and moved into gate 37/39's
#   population. Counts are STATED so the move is a decision, not a drift. 2-08 joined
#   them later the same session: 177->176, NIMG 23->24 (it is IMAGE_, so the GRAPHIC_ count stays 67).
# v1.32 (S99): GATE 38 hole closed. v1.31's label check is a floor of ONE, so a graphic
#   with 26 of 27 labels outlined passed it green — demonstrated, not argued, on an
#   lxml-built injection. GRAPHIC_ names now carry a path-data ceiling too. Found by
#   re-deriving gate 38's own numbers on xml.etree and lxml; all six figures agreed and
#   the SEVENTH thing, the one nobody had measured, was the hole. Arithmetic at the gate.
# v1.31 (S98): NEW GATE 38 — §21.2 a drawn graphic keeps live <text> and stays under a
#   60,000 B ceiling. Four referenced graphics shipped with every label OUTLINED,
#   +1.13 MB and a 50x growth, and passed 37/37 for a week; one rode in on the same
#   commit that carried this suite's own update. Thresholds at the gate, all measured.
# v1.30 (S98): GATE 37 REWRITTEN. The old §21.1 forbade any embedded raster in a
#   referenced .svg, which would have gone red on the first legitimate photo-plus-labels
#   composite. It now checks the three things that were actually wrong: a duplicated
#   payload, a byte ceiling, and a vector-content floor. Rationale at the gate.
# v1.29.1 (S98): version home moved ABOVE the changelog. No gate changed. A plain grep of
#   this file used to return v1.26.1 - a changelog line, three releases stale, and it read
#   exactly like an answer. session_versions.py grep_trap() now keeps the home on top.
# v1.26.1: §5.1 coverage 250 → 251. L01's AI-autocomplete block was on the one-off border
# #ffb300; the S95 repaint snapped it to WARNING's #ffc107, which brings it INTO this gate's
# scope (scheme + ⚠ glyph now agree). Its merged label was split into the canonical
# ⚠ WARNING label + separate title line. Control-run: the assert fired at 251/250 before
# this bump, so the number is doing work.
# v1.26.2: GEOM_BASELINE 115 → 114. L03's stop-motors block was 5px on #c0392b/#f8d7da; the
# S95 repaint moved it to #fdecea and normalised the rule to the canon 4px, so that debt is
# PAID, not moved, and its baseline row is gone. DJ ruling: from S95 on, a repaint that lands
# on one of the off-canon blocks normalises the width in the same edit.
# v1.28 (S97): NEW GATE 36 — every image reference resolves to a file on disk. Found by
# accident, not by any gate: Lesson_02 pointed at three .svg files and Lesson_05 at one that
# existed nowhere on main (an incomplete .svg -> .png migration; the originals survived only
# on the stranded branch Weymuth-patch-1). Four 404s were LIVE on the published site through a
# full 35/35 pass, in two of the first five lessons a student opens. Nothing checked img src.
# Control-run four ways before shipping: silent on the fixed tree; run against UNFIXED source
# at cd47f50 it independently rediscovered exactly those four with line numbers; a seeded
# break in each NON-lesson page (index/timer/going_deeper/tutor) was caught, proving the glob
# reaches past lessons/ — scope being the exact thing §12/§23 got wrong twice.
# v1.29 (S97): NEW GATE 37 — no REFERENCED .svg carries an embedded raster. Three files
# arrived in one session as PNG wrapped in an SVG envelope: valid XML, correct extension,
# zero drawing elements, the whole picture one base64 <image>. The memory ladder shipped that
# way at 4,879,809 B against the 4,517 B its true-vector replacement weighs — 1,080x — and it
# was LIVE in Lesson 02. Gate 36 stayed green throughout: a reference that resolves says
# nothing about what it resolves TO.
#   SCOPING, deliberate: this fails only on SVGs a page REFERENCES. Raw exports are staged in
# images/ before being wired up, and a gate that goes red on work-in-progress is a gate people
# learn to ignore. Unreferenced offenders are COUNTED and PRINTED, never fatal. Measured before
# choosing: strict would have failed on the two staged L05 sensor-array files the same day they
# landed; scoped passes and reports them. Protect the book, not the staging area.
# Usage:  python3 book_gates.py            (run from repo root)
# Exit 0 = all gates pass. Exit 1 = failures listed.
#
# Run at SESSION OPEN (health check) and before EVERY delivery (close gate).
# Each gate encodes a Bible rule; the Bible section is named on each line.
# When a new rule is canonized, add its gate here in the same session.

import re, glob, html, os, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from html.parser import HTMLParser as _HTMLParser
import lesson_inventory as LI          # §20.1 bounding: ONE definition, not a third regex

# ---- §5.0.1 SECTION BAND COLOURS. One home, because the ramp cannot be piloted.
# ---- S108 proved five constructs are byte-compared across all sixteen lessons and move
# ---- together or not at all (lesson strip §6.5a, hero §25.6, PART dividers §6.8, bonus cap
# ---- §4.5, FINISHED EARLY box §4.5a), while THREE more gates typed the §10+ band literally.
# ---- Eleven sites, one colour, no name -- so DJ's banked Steel ruling could not land as an
# ---- edit. Naming it does not change a single verdict (asserted byte-identical below the
# ---- refactor); it makes the ramp a one-line change and makes the blast radius greppable.
# ---- DJ's banked ramp, NOT yet applied: Frost #CBD3DE §1-3 · Mist #AFBCCE §4-6 ·
# ---- Fog #96A8C0 §7/8/8A · Harbor #7E95B4 §9 · Steel #708BAF §10+.
BAND_END = '#6f7582'                   # §10+ band, S111 repaint (was #6c757d)

FAIL = []


def gate(name, bad):
    print(f'{"PASS" if not bad else "FAIL":>5}  {name}')
    for b in bad:
        print(f'         {b}')
    if bad:
        FAIL.append(name)


def txt(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s)))


files = sorted(glob.glob('lessons/Lesson_*.html'))
site = files + ['going_deeper.html', 'index.html', 'tutor/tutor.html',
                'newproject.html', 'timer.html']
site = [f for f in site if os.path.exists(f)]


def L(f):
    return f[15:17]


# The 17 book pages that carry a version banner: 16 lessons + going_deeper.
# Stated explicitly and asserted, NOT inherited from whichever list is nearest.
pages17 = files + (['going_deeper.html'] if os.path.exists('going_deeper.html') else [])


def P(f):
    """Label for any of the 17 pages. L() slices lesson filenames and returns
    garbage for going_deeper.html — a gate that names the wrong file is a hazard."""
    return 'going_deeper' if f == 'going_deeper.html' else 'L' + L(f)


# §25.2 / §25.10h — ONE definition of "converted to the four exit blocks".
#
# S115: this existed as TWO predicates and nothing asserted they agreed. §25.2
# scoped on the string 'MENTAL KNOWLEDGE CHECK'; §25.10h scoped on the id
# 'brain-check-01'. Control-run S115, and this is why the gate below exists:
# mistyping CHECK -> CHEK in ONE lesson dropped it out of §25.2 entirely — no
# four-block check, no retired-name ban, no checkbox/tag parity — and ALL 47
# GATES PASSED. Breaking the OTHER predicate failed three gates loudly. §24.8:
# if a lesson silently left §25.2's scope, that gate looked exactly as it does now.
#
# NOTE the word "converted" is overloaded in this file: §27 uses it for the
# inline-style -> class conversion (see expand_classes above). This is the §25
# exit-block sense and the two are unrelated.
#
# The sets are NAMED, not counted. S114's lesson: a baseline that looks like a
# count gets read as a count. `converted == 9` cannot say WHICH lesson moved;
# a set difference can, and it survives the conversion arc without a magic literal.
BC_EXEMPT = {'14', '16'}                        # DJ ruling S115: L14 competition day,
                                                # L16 end-of-course — their §10s carry
                                                # content the four blocks would displace.
BC_PENDING = set()            # EMPTY at S119: the conversion arc is complete.
                                                # Remove a number here in the same edit
                                                # that converts its lesson, never before.


def bc_marks(s):
    """The two marks of a converted lesson. Returned separately so the gate can
    report a DISAGREEMENT rather than silently picking one and moving on."""
    return ('id="brain-check-01"' in s, 'MENTAL KNOWLEDGE CHECK' in s)


def is_converted(s):
    """A lesson is converted only when BOTH marks are present. Half a conversion
    is not a conversion, and must not buy exemption from the gates."""
    return all(bc_marks(s))


def visible(s):
    """What the reader can actually see: HTML comments removed.

    A gate that checks placement or visibility MUST strip what the reader
    cannot see before matching, or it reports a condition it never tested.
    """
    return re.sub(r'<!--.*?-->', '', s, flags=re.S)


# §27 (S104): read through the class expander so a gate sees the same CSS whether the
# lesson still carries inline styles or has been converted. ONE definition, shared with
# lesson_inventory (the S83 rule: import the definition, never write a third regex).
R = {f: LI.expand_classes(open(f, encoding='utf-8').read()) for f in site}

# ---- §5b: hidden full version on line 1; exactly ONE visible banner carrying its major.minor
# S89: the build banner was deleted from all 17 pages. It was a COMMENT, so the old
# gate — which matched raw text and required exactly 2 hits — was counting a hidden
# string as a visible banner. Comments are stripped first now.
# S89: coverage moved from `files` (16) to `pages17` (17). going_deeper.html had drifted
# to a visible 01.0 against a hidden 01.1.0 and survived because it was never walked.
bad = []
if len(pages17) != 17:
    bad.append(f'COVERAGE: expected 17 versioned pages, found {len(pages17)}')
for f in pages17:
    s = R[f]
    hid = re.search(r'v(\d+\.\d+)\.\d+', s[:60])
    vis = re.findall(r'Version (\d+\.\d+)', visible(s))
    if not hid:
        bad.append(f'{P(f)}: no hidden version comment on line 1')
    elif len(vis) != 1:
        bad.append(f'{P(f)}: expected exactly 1 visible banner, found {len(vis)}: {vis}')
    elif vis[0] != hid.group(1):
        bad.append(f'{P(f)}: hidden={hid.group(1)} but visible={vis[0]} — they must agree')
gate('§5b  version: hidden == the one visible banner, all 17', bad)

# ---- §5b: the one visible banner carries exactly one date.
# S89: was an addendum about TWO banners agreeing. There is only one banner now,
# so "agreement" is not the property — presence and uniqueness are.
bad = []
if len(pages17) != 17:
    bad.append(f'COVERAGE: expected 17 versioned pages, found {len(pages17)}')
for f in pages17:
    d = re.findall(r'Version \d+\.\d+(?: &mdash;| —) (\w+ \d{4})', visible(R[f]))
    if len(d) != 1:
        bad.append(f'{P(f)}: expected exactly 1 dated visible banner, found {len(d)}: {d}')
gate('§5b  date: exactly one dated visible banner, all 17', bad)

# ---- §22: terminal blocks — [SUCCESS] green #6a9955, diagnostics red #f14c4c
bad = []
for f in files:
    s = R[f]
    for m in re.finditer(r'<pre.*?</pre>', s, re.S):
        blk = m.group(0)
        t = re.sub(r'<[^>]+>', '', blk)
        if re.search(r'error:|undefined reference|\[SUCCESS\]|\[FAILED\]|Writing \||Verifying \|', t):
            if '[SUCCESS]' in t and 'color: #6a9955;">[SUCCESS]' not in blk:
                bad.append(f'{L(f)}@{m.start()}: [SUCCESS] not green')
            if re.search(r'error:|undefined reference', t) and '#f14c4c' not in blk:
                bad.append(f'{L(f)}@{m.start()}: diagnostic not red')
gate('§22  terminal colors (SUCCESS green / errors red)', bad)

# ---- §4.2: data-challenge markers globally unique
bad = []
seen = collections.Counter()
for f in files:
    for m in re.findall(r'data-challenge="([^"]*)"', R[f]):
        seen[m] += 1
dups = [f'{k} x{v}' for k, v in seen.items() if v > 1]
if dups:
    bad.append('duplicates: ' + ', '.join(dups))
gate('§4.2 data-challenge markers globally unique', bad)

# ---- §4.3: picker labels (element textContent, 60 chars) unique per lesson
bad = []
for f in files:
    s = R[f]
    labels = collections.Counter()
    for m in re.finditer(r'<(\w+)([^>]*data-challenge="[^"]*"[^>]*)>', s):
        tag = m.group(1)
        close = s.find('</' + tag + '>', m.end())
        t = txt(s[m.end():close]).strip()[:60]
        labels[t] += 1
    for t, n in labels.items():
        if n > 1:
            bad.append(f'{L(f)}: "{t[:45]}" x{n}')
gate('§4.3 picker labels unique within each lesson', bad)

# ---- §4.1: retired construct names must not reappear
bad = []
for f in files:
    if re.search(r'CHALLENGE \(\d+ minute', R[f]):
        bad.append(f'{L(f)}: old "CHALLENGE (n min)" label (renamed TRY IT, S65)')
gate('§4.1 no retired construct names', bad)

# ---- §6.12b: two-axis pill parity per lesson
bad = []
for f in files:
    d = len(re.findall(r'data-difficulty=', R[f]))
    g = len(re.findall(r'data-grasp=', R[f]))
    if d != g:
        bad.append(f'{L(f)}: difficulty={d} grasp={g}')
gate('§6.12b pill two-axis parity', bad)

# ---- structure: paired-tag balance across every site file
# v1.27: this gate used to count `<tag\\b` against `</tag>` for a FIXED LIST OF SEVEN
# tags. Two consequences, both found by the S95 triple-check with html.parser:
#   1. `p` was not on the list, so TWO orphan `</p>` tags with no opening `<p>` sat in
#      L06 and L15 through every 35/35 pass. Only 7 of the 41 paired tags in use were
#      checked at all.
#   2. The counting method reads inside HTML COMMENTS. index.html mentions `<h1>` in a
#      comment explaining why the h1 is sr-only, which counts as 2/1 and would have
#      failed the moment the list was widened. A false failure costs 3x a blank one.
# So the method is replaced, not the list: a real parser, every paired tag, comments and
# CDATA ignored for free, and crossed tags detected as well as unbalanced ones.
_VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param',
         'source','track','wbr'}

class _Balance(_HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []; self.bad = []
    def handle_starttag(self, t, a):
        if t not in _VOID:
            self.stack.append((t, self.getpos()[0]))
    def handle_endtag(self, t):
        if t in _VOID:
            return
        if not self.stack:
            self.bad.append(f'orphan </{t}> line {self.getpos()[0]} (nothing open)')
        elif self.stack[-1][0] == t:
            self.stack.pop()
        else:
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == t:
                    self.bad.append(f'crossed </{t}> line {self.getpos()[0]}')
                    del self.stack[i:]
                    break
            else:
                self.bad.append(f'orphan </{t}> line {self.getpos()[0]} (no matching open)')

bad = []
for f in site:
    w = _Balance()
    w.feed(R[f])
    w.close()
    for m in w.bad:
        bad.append(f'{f}: {m}')
    for t, ln in w.stack:
        if t not in ('html', 'head', 'body'):
            bad.append(f'{f}: unclosed <{t}> opened line {ln}')
gate('tag balance (all site files)', bad)

# ---- timers: every iframe has min+label; labels unique per lesson
bad = []
for f in files:
    labs = collections.Counter()
    for m in re.finditer(r'<iframe[^>]*timer\.html([^"]*)"', R[f]):
        q = m.group(1)
        if 'min=' not in q or 'label=' not in q:
            bad.append(f'{L(f)}: timer missing param: {q[:50]}')
        lab = re.search(r'label=([^&"]*)', q)
        if lab:
            labs[lab.group(1)] += 1
    for t, n in labs.items():
        if n > 1:
            bad.append(f'{L(f)}: timer label "{t}" x{n}')
gate('timers: params present, labels unique per lesson', bad)

# ---- links: index.html relative links resolve to real files
bad = []
for m in re.finditer(r'href="([^"#][^"]*)"', R['index.html']):
    u = m.group(1)
    if u.startswith('http'):
        continue
    if not os.path.exists(u):
        bad.append(f'index.html -> {u} MISSING')
gate('index.html relative links resolve', bad)

# ---- links: going_deeper references use canonical RELATIVE URLs (S105)
# The absolute form was allowed while the book hard-coded its own domain. §27.10 removed
# all 496 self-references, so the canonical form is now relative-to-the-page and the
# absolute form is a REGRESSION, not an alternative. Depth is derived from the page, not
# guessed: lessons/ sit one level down, root pages do not.
bad = []
for f in site:
    want = '../going_deeper.html' if f.startswith('lessons/') else 'going_deeper.html'
    for m in re.finditer(r'href="([^"]*going_deeper[^"]*)"', R[f]):
        u = m.group(1).split('#')[0]
        if u != want:
            bad.append(f'{f}: {m.group(1)} (expected {want})')
gate('going_deeper links canonical and relative', bad)

# ---- §24: cross-lesson promises — a forward-ref's topic must exist in the target lesson
bad = []
T = {f: txt(R[f]) for f in files}
for f in files:
    src = int(L(f))
    for m in re.finditer(r'([^.!?]{10,140}?)\b[Ll]esson (\d+)\b([^.!?]{0,110})[.!?]', T[f]):
        tgt = int(m.group(2))
        if tgt <= src or tgt > 16:
            continue
        sent = (m.group(1) + ' Lesson ' + m.group(2) + m.group(3)).strip()
        keys = re.findall(r'[a-zA-Z_]+\(\)|\b(?:gyro|encoder|PID|state machine|kill switch|silver|'
                          r'proximity|calibrat\w+|modulo|array|float|extern|header|P-control|Kp|EEPROM|'
                          r'for loop|==)\b', sent)
        keys = [k for k in set(keys) if len(k) > 2][:3]
        if not keys:
            continue
        tf = f'lessons/Lesson_{tgt:02d}.html'
        missing = [k for k in keys if k.lower() not in T[tf].lower()]
        if missing:
            bad.append(f'L{src:02d} -> L{tgt:02d}: promises {missing}')
gate('§24  cross-lesson promises land in target lesson', bad)

# ---- §24.4: verifiable arithmetic in prose
bad = []
for f in files:
    t = T[f]
    for m in re.finditer(r'(\d+)\s*characters?,?\s*(?:so|=|is|makes?)\s*(\d+)\s*bytes', t):
        a, b = int(m.group(1)), int(m.group(2))
        if b not in (a, a + 1):
            bad.append(f'{L(f)}: "{m.group(0)}"')
    for m in re.finditer(r'([\d,]+)\s*(?:ms|milliseconds?)\s*(?:=|is|equals?)\s*([\d.]+)\s*seconds?', t):
        a = int(m.group(1).replace(',', '')); b = float(m.group(2))
        if abs(a / 1000 - b) > 0.01:
            bad.append(f'{L(f)}: "{m.group(0)}" ({a}ms = {a/1000}s)')
    for m in re.finditer(r'([\d,]+)\s*(?:mV|millivolts?)[^.]{0,60}?([\d.]+)\s*volts?', t):
        a = int(m.group(1).replace(',', '')); b = float(m.group(2))
        if abs(a / 1000 - b) > 0.05:
            bad.append(f'{L(f)}: "{m.group(0)[:60]}" ({a}mV = {a/1000}V)')
gate('§24.4 arithmetic claims verify', bad)

# ---- §16: hardware constants match canon (wrong values that must never appear)
bad = []
WRONG = {'32,768 bytes usable': 'usable flash is 28,672'}
for f in files:
    for w, why in WRONG.items():
        if w in T[f]:
            bad.append(f'{L(f)}: "{w}" — {why}')
gate('§16  hardware constants match canon', bad)

# ---- structure: real HTML parse (S68). Supersedes count-based checks: an orphaned
# ---- close tag can BALANCE an unclosed box, so a count gate is satisfied by the bug itself.
from html.parser import HTMLParser as _HP
_VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
_STRICT = {'div','details','summary','table','section','article','span','a','pre','body','html','ul','ol','h1','h2','h3','h4'}

class _Struct(_HP):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.err=[]
    def handle_starttag(self, t, a):
        if t not in _VOID: self.stack.append((t, self.getpos()[0]))
    def handle_endtag(self, t):
        if t in _VOID: return
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == t:
                for tag, ln in self.stack[i+1:]:
                    if tag in _STRICT:
                        self.err.append(f'line {ln}: <{tag}> never closed (swallowed by </{t}> line {self.getpos()[0]})')
                del self.stack[i:]; return
        if t in _STRICT:
            self.err.append(f'line {self.getpos()[0]}: stray </{t}> with nothing open')

bad = []
for f in site:
    pr = _Struct(); pr.feed(R[f]); pr.close()
    for e in pr.err + [f'line {l}: <{t}> still open at EOF' for t, l in pr.stack if t in _STRICT]:
        bad.append(f'{f}: {e}')
    trail = R[f][R[f].rfind('</html>') + 7:].strip()
    if trail:
        bad.append(f'{f}: {trail[:40]!r} after </html>')
gate('structure: HTML parses to the intended shape', bad)

# ---- structure: end matter must not be sealed inside a section panel (S68).
# ---- Well-formed HTML can still be wrong: L06/L07 parsed clean with the footer
# ---- trapped inside the Image Index box. The parser cannot see this class.
bad = []
_d = re.compile(r'<div\b[^>]*>|</div\s*>')
for f in files:
    # S108: "Image Index" is becoming "Figures", id and all. While the sixteen are
    # mixed this gate must find EITHER, or it goes silent on the converted lessons
    # and reports PASS on a file it never opened.
    _im = re.search(r'id="(image-index|figures)"', R[f])
    if not _im:
        bad.append(f'{L(f)}: no end-matter index anchor (image-index / figures)')
        continue
    i = _im.start()
    j = R[f].find('border-top: none', i)
    j = R[f].rfind('<div', 0, j)
    depth = 0; close = None
    for m in _d.finditer(R[f], j):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth == 0:
            close = m.end(); break
    if close is None:
        bad.append(f'{L(f)}: Image Index panel never closes'); continue
    inside = R[f][j:close]
    if re.search(r'<hr\b|linear-gradient\(135deg, '+re.escape(BAND_END), inside):
        bad.append(f'{L(f)}: lesson end matter is sealed INSIDE the Figures panel')
gate('structure: end matter sits outside the section panel', bad)

# ---- §6.5a: the lesson strip is present in every lesson and byte-identical book-wide.
# It ships as ONE block (static links + self-hydrating script deriving the current lesson
# from the URL), so any hand-variation is drift. Marker comments bound the block.
bad = []
strips = []
for f in files:
    m = re.search(r'<!-- LESSON STRIP v1.*?<!-- /LESSON STRIP -->', R[f], re.S)
    if not m:
        bad.append(f'{L(f)}: lesson strip missing')
    else:
        strips.append((f, m.group(0)))
if strips:
    ref_f, ref = strips[0]
    for f, s2 in strips[1:]:
        if s2 != ref:
            bad.append(f'{L(f)}: lesson strip differs from L{L(ref_f)}')
gate('§6.5a lesson strip present and byte-identical in all 16', bad)

# ---- §25.6: header hero + footer, identical across all 17 pages (S89: build banner dropped)
import hashlib
import subprocess

PAGES = files + (['going_deeper.html'] if os.path.exists('going_deeper.html') else [])



def _find_dash(s, left, right):
    """Find "LEFT <em dash> RIGHT" without pinning how the dash is spelled.
    §27.16: the book spells it literally now; a gate that pins a spelling
    certifies whatever it was given (S126, gate 57)."""
    for d in ('\u2014', '&mdash;'):
        i = s.find(left + ' ' + d + ' ' + right)
        if i >= 0:
            return i
    return -1


def _find_any(s, *forms):
    """First offset at which any spelling of the same text occurs."""
    for f in forms:
        i = s.find(f)
        if i >= 0:
            return i
    return -1


def _close_of(s2, st, tag):
    d = 0
    for m in re.finditer(rf'<{tag}\b|</{tag}>', s2[st:]):
        d += 1 if m.group(0) != f'</{tag}>' else -1
        if d == 0:
            return st + m.end()
    return -1


def _skel(block):
    return hashlib.md5(re.sub(r'>[^<]*<', '><', block).encode()).hexdigest()[:8]


heroes, footers, bad = {}, {}, []
for f in PAGES:
    s2 = R[f]
    lab = 'GOING DEEPER' if f == 'going_deeper.html' else 'LESSON ' + L(f)
    m = re.search(r'>\s*' + lab + r'\s*<', s2)
    if not m:
        bad.append(f'{f}: no hero label "{lab}"')
        continue
    v = re.search(r'Version \d+\.\d+(?: &mdash;| \u2014) \w+ \d{4}', s2[m.start():m.start() + 2500])
    if not v:
        bad.append(f'{f}: hero has no dated Version line')
        continue
    vpos = m.start() + v.start()
    st = m.start()
    while True:
        st = s2.rfind('<div', 0, st)
        if st < 0:
            break
        en = _close_of(s2, st, 'div')
        if en > vpos:
            break
    heroes.setdefault(_skel(s2[st:en]), []).append(f)
    i = _find_any(s2, '&copy; 2026 RoboLore', '© 2026 RoboLore')
    if i < 0:
        bad.append(f'{f}: footer missing the credits line')
        continue
    a = s2.rfind('<p', 0, i)
    b = s2.find('</p>', i) + 4
    footers.setdefault(_skel(s2[a:b]), []).append(f)
    # S89: the BUILD BANNER and 'ZUMO Callout Standard v1.0 Applied' assertions were
    # removed here. The banner was a hidden third version home that the §5b gate was
    # miscounting as visible. The callout-standard string named no document that existed
    # — the gate asserted a string that existed only because the gate asserted it.
    # Its successor is BookComponentStandard.md at the repo root.
if len(heroes) > 1:
    bad.append(f'hero skeletons differ: { {k: [L(x) for x in v] for k, v in heroes.items()} }')
if len(footers) > 1:
    bad.append(f'footer skeletons differ: { {k: [L(x) for x in v] for k, v in footers.items()} }')
gate('§25.6 header/footer identical across all 17', bad)

RETIRED = ['STOP &amp; PROCESS', 'Conceptual Understanding',
           'Check Your Understanding', 'Reflection Questions',
           'Explain It in Writing']

# ---- §25.2 COVERAGE: the two conversion marks agree, and the converted SET is the ruled set
bad = []
converted_set = set()
for f in files:
    anchor, phrase = bc_marks(R[f])
    if anchor != phrase:
        have = 'id="brain-check-01"' if anchor else "'MENTAL KNOWLEDGE CHECK'"
        miss = "'MENTAL KNOWLEDGE CHECK'" if anchor else 'id="brain-check-01"'
        bad.append(f'{L(f)}: half-converted — carries {have} but not {miss}. '
                   f'§25.2 and §25.10h would disagree about whether this lesson is in scope.')
    if anchor and phrase:
        converted_set.add(L(f))
expected = {L(f) for f in files} - BC_EXEMPT - BC_PENDING
if converted_set != expected:
    for n in sorted(expected - converted_set):
        bad.append(f'L{n}: expected converted, is not — it left §25 scope silently')
    for n in sorted(converted_set - expected):
        where = 'exempt by ruling' if n in BC_EXEMPT else 'listed pending'
        bad.append(f'L{n}: is converted but is {where} — update BC_EXEMPT/BC_PENDING')
gate(f'§25.2 conversion marks agree; converted set is the ruled set '
     f'({len(expected)} converted, {len(BC_PENDING)} pending, {len(BC_EXEMPT)} exempt)', bad)

# ---- §25.2: where a lesson has converted to the four exit blocks, it must conform
bad = []
for f in files:
    s2 = R[f]
    if not is_converted(s2):
        continue                      # not yet converted — §25 does not bind it
    # S91: bound by the id §25.10h canonizes, NOT by the nearest preceding <div>.
    # rfind('<div') was correct only by accident -- it worked because the Brain Check
    # TITLE happened to be a <strong>. The S91 title sweep made every title a <div>,
    # so rfind landed on the title and the block collapsed to one line, reading 0 items
    # in all nine lessons while the lessons were untouched. Same defect the Bible
    # already recorded for §20.1(5) at S83, one gate over.
    i = s2.find('id="brain-check-01"')
    if i < 0:
        i = s2.find('MENTAL KNOWLEDGE CHECK')
    st = s2.rfind('<div', 0, i)
    en = _close_of(s2, st, 'div')
    blk = s2[st:en]
    n = blk.count('data-reveal="quiz"')
    if not 3 <= n <= 5:
        bad.append(f'{L(f)}: Mental has {n} items, §25.2 caps 3-5')
    for m in re.finditer(r'<summary[^>]*>(.*?)</summary>', blk, re.S):
        if not re.search(r'&sect;|§', m.group(1)):
            bad.append(f'{L(f)}: Mental item names no § — {txt(m.group(1))[:52]}')
    if _find_dash(s2, 'KNOWLEDGE CHECK', 'What You Just Built') < s2.find('id="section-10"'):
        bad.append(f'{L(f)}: §10 Knowledge Check is not inside §10')
    j = _find_dash(s2, 'REFLECTION', 'In Your Notebook')
    if j < 0:
        bad.append(f'{L(f)}: converted but has no Reflection block')
    else:
        rst = s2.rfind('<div', 0, j)
        if 'data-reveal' in s2[rst:_close_of(s2, rst, 'div')]:
            bad.append(f'{L(f)}: Reflection carries a reveal (§25.2: never)')
    for r in RETIRED:
        if r in s2:
            bad.append(f'{L(f)}: converted but retired name still present — "{html.unescape(r)}"')
    for k in range(1, 5):
        if f'id="brain-check-0{k}"' not in s2:
            bad.append(f'{L(f)}: converted but Brain Check anchor 0{k} missing (§25.10)')
        else:
            j = s2.find(f'id="brain-check-0{k}"')
            wrap = s2[s2.rfind('<div', 0, j + 30):s2.find('>', j) + 1]
            if 'border-left: 4px solid #3f51b5' not in wrap:
                bad.append(f'{L(f)}: Brain Check 0{k} wrapper is not Type 10 indigo (§25.10)')
    if 'BRAIN CHECK COLUMN START' not in s2:
        bad.append(f'{L(f)}: converted but Brain Check column block missing (§25.10)')
    j2 = s2.find('id="brain-check-02"')
    if j2 > 0:
        blk2 = s2[j2:_close_of(s2, s2.rfind('<div', 0, j2 + 30), 'div')]
        boxes = blk2.count('\u2610')
        tagged = blk2.count('data-bc-skill=')
        if boxes != tagged:
            bad.append(f'{L(f)}: BC02 has {boxes} checkbox items but {tagged} data-bc-skill tags (§25.10 skill gate)')
gate('§25.2 converted lessons conform to the four exit blocks + §25.10 Brain Check', bad)

# ---- §25.8: Brain Check 03 carries at least FOUR items (floor, no maximum — DJ ruling S77)
bad = []
for f in files:
    s2 = R[f]
    j3 = s2.find('id="brain-check-03"')
    if j3 < 0:
        continue                     # unconverted lessons are out of scope
    blk3 = s2[j3:_close_of(s2, s2.rfind('<div', 0, j3 + 30), 'div')]
    items = len(re.findall(r'<details data-reveal="\w+"', blk3))
    if items < 4:
        bad.append(f'{L(f)}: Brain Check 03 has {items} items, floor is 4 (§25.8)')
gate('§25.8 Brain Check 03 carries at least four items', bad)

# ---- §25.10l: Brain Check 01 carries exactly FIVE items — DJ ruling S119, option D.
# NOT a floor like §25.8's. BC01 measured at five in 13 of 13 converted lessons before L15
# and fourteen of fourteen after, and NOTHING held it: at S119 a question was asked on the
# premise that BC01 maps to §2's objectives (it does not — BC02 does), DJ ruled an item be
# added, and adding one would have broken a 14/14 norm SILENTLY. The ruling that resolved it
# put the sixth item in BC03 instead, on the verb: BC01 sits before §6 and asks what the
# BUILD depends on, so a *diagnose* claim belongs at the bench in §7, which is BC03's half.
# THE NUMBER CAN NEVER LEGITIMATELY MOVE AGAIN — the conversion arc closed at S119 and
# BC_PENDING is empty, so unlike §21's coverage or the family map's total this is a constant,
# not a baseline. If it ever moves, something was edited that nobody ruled on.
# The COVERAGE arm is not decoration: a gate that scans zero lessons passes (S117, S118).
bad = []
_seen01 = 0
for f in files:
    s2 = R[f]
    j1 = s2.find('id="brain-check-01"')
    if j1 < 0:
        continue                     # unconverted lessons are out of scope
    _seen01 += 1
    blk1 = s2[j1:_close_of(s2, s2.rfind('<div', 0, j1 + 30), 'div')]
    items = len(re.findall(r'<details data-reveal="\w+"', blk1))
    if items != 5:
        bad.append(f'{L(f)}: Brain Check 01 has {items} items, canon is exactly 5 (§25.10l) — '
                   f'an item belongs in BC01 only if the BUILD in §6 depends on it')
_exp01 = len({L(f) for f in files} - BC_EXEMPT - BC_PENDING)
if _seen01 != _exp01:
    bad.append(f'COVERAGE: {_seen01} lesson(s) carry brain-check-01, expected {_exp01} '
               f'(exempt {sorted(BC_EXEMPT)}, pending {sorted(BC_PENDING)})')
gate('§25.10l Brain Check 01 carries exactly five items', bad)

# ---- §5b: every web tool carries a greppable in-file version line
WEB_TOOLS = {'timer.html': 'Timer', 'tutor/tutor.html': 'Tutor',
             'newproject.html': None, 'index.html': 'Index'}
bad = []
for f in WEB_TOOLS:
    if not os.path.exists(f):
        bad.append(f'{f}: MISSING from the repo')
        continue
    head = open(f, encoding='utf-8').read()[:600]
    if not re.search(r'<!--\s*\w[\w ]*version:\s*v[\d.]+\s*-->', head, re.I):
        bad.append(f'{f}: no in-file version comment in the first 600 bytes')
gate('§5b  web tools carry an in-file version line', bad)

# ---- §12/§23: canonical site layout — every page in its one correct place, no strays
EXPECTED = sorted(
    [f'lessons/Lesson_{n:02d}.html' for n in range(1, 17)] +
    ['going_deeper.html', 'index.html', 'newproject.html', 'timer.html', 'tutor/tutor.html'])
found = sorted(f for f in glob.glob('**/*.html', recursive=True)
               if not f.startswith('.git'))
bad = []
for f in sorted(set(found) - set(EXPECTED)):
    bad.append(f'STRAY page: {f}  (not a canonical location)')
for f in sorted(set(EXPECTED) - set(found)):
    bad.append(f'MISSING page: {f}')
gate('§12/§23 site layout: every page in its canonical place, no strays', bad)

# ---- §20.1: a challenge answer must not hide behind a KEPT reveal type.
# The tutor front-end strips ONLY <details data-reveal="solution">.  A finished,
# fill-nothing-in code block inside a `hint` is therefore shipped to the model
# while looking withheld to a reader.  Found live in L01 C11 at S79.
_LAND = ('<<<', 'GOES HERE', 'goes here', 'your code here', 'YOUR CODE HERE',
         '______', '_____', '\u2190', '&larr;', '&#8592;', 'write your', 'YOUR ')


# The card extent is the PARSE-TREE span from lesson_inventory (§24.6a), not a
# rfind('<div') window.  A construct is bounded two ways in this book and the old
# window only ever produced the first one by accident:
#   ELEMENT-BOUNDED  <div data-challenge="9.1">   span = that div open..close
#   HEADING-BOUNDED  <h4  data-challenge="9.m1">  span = heading .. FIRST of
#                    (next heading at level <= its own / next construct / parent close)
# With the window, every h4-borne marker inherited its enclosing PANEL: L09 9.m3-9.m5
# reported 3/8/17 code lines where reading gives 5/8/2, and L02 2.t4 -- a one-line
# <strong> holding zero <details> -- swallowed a §6 build-step `check` reveal 17 lines
# past its own end, which is where the "2.t4 holds the worked code" claim came from.


def _enclosing_reveal(card, pre_start):
    ctx, depth = None, 0
    for m in re.finditer(r'<details[^>]*data-reveal="([a-z]+)"|<details|</details>',
                         card[:pre_start]):
        if m.group().startswith('</details'):
            depth -= 1
            if depth <= 0:
                ctx, depth = None, 0
        else:
            depth += 1
            if depth == 1:
                ctx = m.group(1)
    return ctx


def _is_finished_code(code):
    body = html.unescape(re.sub(r'<[^>]+>', '', code))
    if any(k in code or k in body for k in _LAND):
        return 0
    return len([ln for ln in body.splitlines() if ln.strip().endswith((';', '{', '}'))])


bad = []
seen = 0
for f in files:
    s = R[f]
    inv = LI.build(f)
    assert inv['bytes'] == len(s), f'{f}: inventory/gate read disagree'
    for c in inv['constructs']:
        seen += 1
        card = s[c['start']:c['end']]
        # §25.10g is a SABOTAGE rule: those reveals carry the planted line.  Observation
        # reveals hold no code at all, so the zero-threshold branch must not chase them.
        mystery = c['kind'] == 'bonus-sabotage'
        for pm in re.finditer(r'<pre[^>]*>(.*?)</pre>', card, re.S):
            if _enclosing_reveal(card, pm.start()) != 'hint':
                continue
            n = _is_finished_code(pm.group(1))
            # §25.10g: a mystery's bug+fix reveal is a `solution`, full stop.  Its planted
            # snippets run 1-2 lines, so the >=3 threshold below is not an exemption --
            # it is why L08 passed this gate on luck for eight sessions (S80).
            if mystery and pm.group(1).strip():
                bad.append(f'{f} mystery {c["marker"]}: code block inside a '
                           f'data-reveal="hint" — §25.10g says a mystery reveal is a '
                           f'"solution"; ANY code here reaches the tutor')
            elif n >= 3:
                bad.append(f'{f} challenge {c["marker"]}: {n}-line finished code block '
                           f'inside a data-reveal="hint" — reaches the tutor; type it "solution"')
if seen < 100:
    bad.append(f'COVERAGE: only {seen} constructs bounded book-wide — the span port is broken, '
               f'so this gate is passing an empty population')
gate('§20.1 no finished answer hidden behind a hint reveal', bad)


# ---- §8/§6.12c: two reveals stacked as siblings must agree on summary padding.
# One padded and one not makes the disclosure triangle and label sit at different
# left insets on adjacent rows -- visible, and invisible to every other gate.
# Introduced at S79 by adding a padded solution beneath an unpadded hint (L01 C11).
_DET = re.compile(r'<details\b[^>]*>|</details>', re.I)


def _sibling_reveals(s):
    spans, stack = [], []
    for m in _DET.finditer(s):
        if m.group().startswith('</'):
            if stack:
                spans.append((stack.pop(), m.end()))
        else:
            stack.append(m.start())
    out = []
    for a, b in sorted(spans):
        blk = s[a:b]
        t = re.search(r'data-reveal="([a-z]+)"', blk[:400])
        sm = re.search(r'<summary([^>]*)>', blk)
        out.append((a, b, t.group(1) if t else None, sm.group(1) if sm else ''))
    return out


bad = []
for f in files:
    s = R[f]
    rs = _sibling_reveals(s)
    for k in range(len(rs) - 1):
        a, b = rs[k], rs[k + 1]
        if b[0] < a[1]:
            continue                                    # nested, not a sibling
        if re.sub(r'\s+', '', re.sub(r'<[^>]+>', '', s[a[1]:b[0]])):
            continue                                    # prose between them
        if ('padding' in a[3]) != ('padding' in b[3]):
            bad.append(f'{f}: {a[2]} reveal stacked directly above {b[2]} reveal, '
                       f'but only one <summary> carries padding — the triangle and '
                       f'label sit at different left insets')
gate('§6.12c stacked sibling reveals agree on summary padding', bad)


print()

# ---- §25.11 (S81 DJ ruling): a reveal's VISIBLE LABEL must agree with its data-reveal
# ---- TYPE. "If it's a hint, then say hint. If it's a solution, then call it a solution."
# ---- Found live in nine mystery reveals (L08 x4, L09 x5) that S80 retyped to `solution`
# ---- attribute-only, leaving the label reading "Hint" on a block the tutor now strips.
# ---- L11 was the model again: solution + "Answer" in all four of its mysteries.
# ---- Deliberately NARROW per §24.6c — the label vocabulary is legitimately varied
# ---- (62 "reveal solution", 13 "Answer", 9 "worked version"), so this asserts only the
# ---- one contradiction shape that was verified by reading, not a label whitelist.
bad = []
_HINTY = ('hint',)
_ANSWERY = ('answer', 'solution', 'worked')
for f in files:
    for m in re.finditer(r'<details\b([^>]*)>\s*<summary\b[^>]*>(.*?)</summary>', R[f], re.S):
        attrs, label = m.group(1), txt(m.group(2)).strip().lower()
        tm = re.search(r'data-reveal="([^"]+)"', attrs)
        if not tm:
            continue
        t = tm.group(1)
        ln = R[f].count('\n', 0, m.start()) + 1
        if t == 'solution' and any(w in label for w in _HINTY):
            bad.append(f'{L(f)} line {ln}: data-reveal="solution" but label says hint')
        if t == 'hint' and any(w in label for w in _ANSWERY):
            bad.append(f'{L(f)} line {ln}: data-reveal="hint" but label promises an answer')
gate('§25.11 reveal label agrees with reveal type', bad)

# ---- §6.8a (S82 DJ ruling): THE SECTION FENCE IS GENERATED FROM THE ANCHOR SPINE.
# ---- DJ, on being offered a widened detector: "Why widen the fence. Can't we just fix
# ---- the issues that are causing the fence issues." The fence had never been canonized
# ---- (zero rules in the Bible before v8.68), so it drifted five ways across ten lessons
# ---- and lesson_inventory.py's narrow matcher was blind in five of them — which is why
# ---- L09's missing §7 looked like the only fence gap when there were nine.
# ---- The fence is DERIVED, so this gate compares the file against a regenerated
# ---- expectation rather than against a vocabulary: number and title must both agree
# ---- with the anchor the fence precedes, and any near-miss comment fails loudly.
bad = []
_EQ = '=' * 21
_FENCE = re.compile(r'<!-- ' + re.escape(_EQ) + r' SECTION (\S+): (.*?) ' + re.escape(_EQ) + r' -->')
_CORE = ('1', '2', '3', '4', '5', '6', '7', '8', '8a', '9', '10')


def _fence_title(s):
    """Derive a fence title from a cap's INNER HTML.  TWO SHAPES (S108, F1).

    legacy   <div id="section-3" style="...">[icon] Section 3: Background Theory
             &mdash; How Motors Make Robots Move</div>
    F1       <div id="section-3"><span>Section 3 &middot; Theory</span>
             <span>How Motors Make Robots Move</span></div>

    The legacy rule split on the em dash and kept the first half.  F1 DELETES the
    dash, so that rule returns the whole banner on a converted lesson and the empty
    string on the old call site -- it must know both while the sixteen lessons are
    mixed.  Under F1 the section NAME rides in the eyebrow after the middot; where
    the eyebrow carries no name (bare caps: 1, 2, 8, 8a, 9, 10) the headline IS the
    name.  That keeps the fence DERIVED, which is this gate's whole premise.
    """
    spans = re.findall(r'<span\b[^>]*>(.*?)</span>', s, re.S)
    if spans:
        eyebrow = html.unescape(spans[0]) if len(spans) > 1 else ''
        t = ''
        for d in ('\u00b7', '\u2022', '|'):
            if d in eyebrow:
                t = eyebrow.split(d, 1)[1].strip()
                break
        t = t or html.unescape(spans[-1]).strip()
        return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t)).strip().upper()
    t = html.unescape(s).strip()
    while t and not t[0].isalnum():
        t = t[1:].lstrip()
    if t.lower().startswith('section'):
        c = t.find(':')
        if c >= 0:
            t = t[c + 1:].strip()
    for d in ('\u2014', '\u2013', ' - '):
        if d in t:
            t = t.split(d, 1)[0].strip()
    return re.sub(r'\s+', ' ', t).upper()


for f in files:
    s = R[f]
    for m in re.finditer(r'<!--(.*?)-->', s, re.S):
        body = re.sub(r'\s+', ' ', m.group(1)).strip().strip('= ').strip()
        p = body.split(None, 1)
        if len(p) > 1 and p[0].upper() == 'SECTION' and not body.upper().startswith('TITLE'):
            if not _FENCE.fullmatch(m.group(0)):
                ln = s.count('\n', 0, m.start()) + 1
                bad.append(f'{L(f)} line {ln}: non-canonical section fence: {body[:44]}')
    want = []
    for am in re.finditer(r'id="section-([0-9]+[a-z]?)"', s):
        if am.group(1) not in _CORE:
            continue
        num = am.group(1).upper()
        gt = s.find('>', am.start())
        # to the anchor's own </div>, not to the first '<': F1 puts child spans there.
        title = _fence_title(s[gt + 1:s.find('</div>', gt)])
        want.append((num, title))
        # --- S82b: the anchor must SIT INSIDE its banner, and the fence must be
        # --- ADJACENT to that banner with nothing but whitespace between them.
        # --- The earlier ordered-list form verified content and order but not
        # --- placement, and passed L06/L07 while their §5 anchor had fallen out
        # --- of its banner into the content panel — a live layout defect that
        # --- tag balance and the structural gates also passed.
        wrap = s.rfind('<div', 0, s.rfind('<', 0, am.start()) + 1)
        ln = s.count('\n', 0, am.start()) + 1
        if 'background-color' not in s[wrap:wrap + 220]:
            bad.append(f'{L(f)} line {ln}: §{num} anchor is not seated in a banner div')
            continue
        # The nearest preceding <div> is NOT necessarily the parent: L06/L07 §5 had a
        # </div> between the banner and the anchor, closing the banner early and leaving
        # the anchor in the content panel. Require the anchor to open IMMEDIATELY inside.
        gap = s[s.find('>', wrap) + 1:s.rfind('<', 0, am.start())]
        if gap.strip():
            bad.append(f'{L(f)} line {ln}: §{num} anchor is not immediately inside its '
                       f'banner — {gap.strip()[:44]!r} intervenes')
            continue
        before = s[:wrap].rstrip()
        if not before.endswith('-->'):
            bad.append(f'{L(f)} line {ln}: §{num} banner is not preceded by a fence '
                       f'(found {before[-40:]!r})')
            continue
        fstart = before.rfind('<!--')
        expect = f'<!-- {_EQ} SECTION {num}: {title} {_EQ} -->'
        if before[fstart:] != expect:
            bad.append(f'{L(f)} line {ln}: §{num} fence is {before[fstart:][:56]!r}, '
                       f'expected {expect[:56]!r}')
    got = [(m.group(1).upper(), m.group(2)) for m in _FENCE.finditer(s)]
    if len(got) != len(want):
        bad.append(f'{L(f)}: {len(got)} canonical fences vs {len(want)} core anchors')
gate('§6.8a section fence generated from the anchor spine, adjacent to a seated anchor', bad)

# ---- §6.8: the PART divider block is GENERATED from the section spine (v8.70, S84)
# Asserts the WHOLE block byte-identically, not just colour and count: the six encoding
# strata found at S84 (bare &, &mdash; vs literal, &ndash;, subtitle opacity 0.7) all
# rendered "fine" and all were drift. Placement is asserted too — L12/L13/L14 shipped
# five banners capping the wrong section, fused to it by border-radius/margin.
_PEQ = '=' * 21
_PART_SPEC = {
    1: ('#1f2a3d', 'Theory &amp; Concepts', 'THEORY & CONCEPTS', '1',
        'Sections 1\u20133: Learn the fundamentals'),
    2: ('#433014', 'Hardware &amp; Code', 'HARDWARE & CODE', '4',
        'Sections 4\u20136: Set up and program your robot'),
    3: ('#00474b', 'Testing &amp; Challenges', 'TESTING & CHALLENGES', '7', None),
    4: ('#7a5905', 'Challenges', 'CHALLENGES', '9',
        'Section 9: Apply what you have learned'),
}
_ANYPART = re.compile(
    r'<div style="background-color: #[0-9a-fA-F]{6}; color: white; padding: 12px 20px; '
    r'border-radius: 8px 8px 0 0; margin: 22px 0 0;">\s*'
    r'<div style="font-size: 18px[^"]*">PART (\d+)[^<]*</div>\s*'
    r'<div style="font-size: 12px[^"]*">[^<]*</div>\s*</div>')
_DIVCMT = re.compile(r'^PART\s+\d+(?:\s+DIVIDER|\s*:\s*.+)?$', re.I)


def _part_expect(n, has_8a):
    color, title, upper, _sec, sub = _PART_SPEC[n]
    if n == 3:
        sub = ('Sections 7\u20138A: Verify and extend' if has_8a
               else 'Sections 7\u20138: Verify and extend')
    return (
        f'<!-- {_PEQ} PART {n}: {upper} {_PEQ} -->\n'
        f'<div style="background-color: {color}; color: white; padding: 12px 20px; '
        f'border-radius: 8px 8px 0 0; margin: 22px 0 0;">\n'
        f'    <div style="font-size: 18px; font-weight: 500; letter-spacing: 0.5px;">'
        f'PART {n} \u2014 {title}</div>\n'
        f'    <div style="font-size: 12px; color: rgba(255,255,255,0.85); margin-top: 4px;">'
        f'{sub}</div>\n'
        f'</div>\n')


bad, seen_blocks = [], 0
for f in files:
    s = R[f]
    has_8a = 'id="section-8a"' in s
    found = _ANYPART.findall(s)
    seen_blocks += len(found)
    if sorted(int(x) for x in found) != [1, 2, 3, 4]:
        bad.append(f'{L(f)}: PART blocks present are {sorted(found)}, expected 1-4')
        continue
    # Byte-canonicity and placement are checked INDEPENDENTLY. Chaining them (bail on a
    # byte failure, skip the placement check) would let an encoding drift hide a misplaced
    # banner — the S83 lesson that a gate must not be satisfied by the bug it should catch.
    for n in (1, 2, 3, 4):
        blk = _part_expect(n, has_8a)
        c = s.count(blk)
        if c != 1:
            bad.append(f'{L(f)}: PART {n} block+comment is not byte-canonical '
                       f'(exact matches: {c})')
    for m in _ANYPART.finditer(s):
        n = int(m.group(1))
        i = m.end()
        while i < len(s) and s[i] in ' \t\n':
            i += 1
        nxt = re.match(r'<!-- =+ SECTION ([0-9A-Za-z]+):', s[i:i + 120])
        if not nxt:
            bad.append(f'{L(f)}: PART {n} is not followed by a SECTION fence')
        elif nxt.group(1) != _PART_SPEC[n][3]:
            bad.append(f'{L(f)}: PART {n} caps SECTION {nxt.group(1)}, '
                       f'expected SECTION {_PART_SPEC[n][3]}')
    # no stray divider-shaped PART comment outside the four canonical ones
    for m in re.finditer(r'<!--((?:(?!-->).)*?)-->', s, re.S):
        body = m.group(1).strip().strip('=').strip()
        if not re.search(r'\bPART\b', body, re.I) or not _DIVCMT.match(body):
            continue
        if not re.fullmatch(r'PART \d: [A-Z &]+', body):
            bad.append(f'{L(f)}: stray PART divider comment {body!r}')
# COVERAGE — a gate whose population silently empties is an ungated rule (S83)
if seen_blocks != 64:
    bad.append(f'COVERAGE: {seen_blocks} PART blocks scanned book-wide, expected 64')
gate('§6.8  PART divider block generated from the spine, byte-exact and correctly placed', bad)


# ---- §12.2 the repo root carries exactly ONE session handoff (v8.71, S84 batch 2)
# The deletion is the half of a push that a file-overwrite batch cannot carry, and it has
# now been missed twice (fb70426, and again this session). The procedure lived only in the
# session handoff — i.e. in the very file being deleted — so it vanished exactly when needed.
bad = []
_HO = sorted(g for g in glob.glob('ZUMO_S*_HANDOFF.md') if re.fullmatch(r'ZUMO_S\d+_HANDOFF\.md', g))
if len(_HO) != 1:
    bad.append(f'root carries {len(_HO)} session handoffs ({", ".join(_HO) or "none"}), expected 1'
               + ('  — the prior one\'s deletion checkbox was probably not ticked' if len(_HO) > 1 else ''))
_LM = [g for g in glob.glob('ZUMO_LEARNMODE_*_HANDOFF.md')]
if _HO and any(h in _LM for h in _HO):
    bad.append('a §19 learner-mode record was counted as a session handoff')
# S113: THE NUMBER WAS NEVER CHECKED, AND TWO SESSIONS RAN ON A WRONG ONE.
# The count assert above passes on ANY number - control-run: a file renamed
# ZUMO_S999_HANDOFF.md is still exactly one file and still PASSED. §24.8: if the answer
# were the opposite, this gate looked identical. Two real defects lived in that blind spot.
#   S112 wrote its OUTGOING handoff into the INCOMING handoff's filename, editing
#   ZUMO_S112_HANDOFF.md in place across three commits (893b8b6 -> 4558257 -> 8ae3857) while
#   its title stayed 'paste at top of Session 112', so ZUMO_S113_HANDOFF.md never existed.
#   S113 then inferred the convention from that single defective example and pushed S114's
#   content as ZUMO_S113_HANDOFF.md. DJ caught it by reading; no instrument could.
# THE CONVENTION, verified from git history 10/10 across S103-S112: the filename number, the
# title number and the 'paste at top of Session N' number are ONE number, and it is the
# session that READS the file. Parsed from the title line, not grepped for a literal, so a
# reworded title fails loudly instead of silently skipping the check (§24.10).
if len(_HO) == 1:
    _hn = int(re.fullmatch(r'ZUMO_S(\d+)_HANDOFF\.md', _HO[0]).group(1))
    _first = open(_HO[0], encoding='utf-8').readline()
    _tm = re.search(r'#\s*ZUMO\s*[—-]\s*S(\d+)\s+HANDOFF', _first)
    _pm = re.search(r'paste at top of Session\s+(\d+)', _first)
    if not _tm:
        bad.append(f'{_HO[0]}: first line carries no "# ZUMO - SNN HANDOFF" title to check the'
                   ' filename against - the shape changed, or the title is missing')
    elif int(_tm.group(1)) != _hn:
        bad.append(f'{_HO[0]}: filename says S{_hn} but its title says S{_tm.group(1)} - the'
                   ' number is the session that READS the file, and the two homes disagree')
    if _pm and _tm and int(_pm.group(1)) != int(_tm.group(1)):
        bad.append(f'{_HO[0]}: title says S{_tm.group(1)} but it reads "paste at top of Session'
                   f' {_pm.group(1)}" - the same line disagrees with itself')
gate('§12.2 repo root carries exactly one session handoff, numbered for the session that reads it', bad)

# ---- §25.10h Brain Check family placement (v8.71 — NEW, S84 batch 2, DJ ruling)
# BC01 is a direct child of <body> whose NEXT SIBLING is the banner seating #section-6.
# BC02/03/04 sit one div deep, inside the gray #6c757d §10 content panel.
# Unanimous 9/9 across the converted lessons once S83 lifted L06's BC01 out of §5's panel —
# which is the exact defect this gate exists to catch, and which no gate could see.
# Previous-sibling is deliberately NOT asserted: it legitimately varies (L01/L02 a subsection
# banner, L03 a predict box, L04-L09 §5's green panel).
bad, converted = [], 0
for f in files:
    s = R[f]
    # S115: was 'id="brain-check-01"' in s — its OWN predicate, disagreeing with §25.2's.
    # Both now read is_converted(); coverage is asserted as a named SET one gate above.
    if not is_converted(s):
        continue                     # §25.2 governs converted lessons only
    converted += 1
    soup = LI.BeautifulSoup(s, 'html.parser') if hasattr(LI, 'BeautifulSoup') else None
    if soup is None:
        from bs4 import BeautifulSoup as _BS
        soup = _BS(s, 'html.parser')
    for i in ('01', '02', '03', '04'):
        el = soup.find(id=f'brain-check-{i}')
        if el is None:
            bad.append(f'{L(f)}: brain-check-{i} missing')
            continue
        depth = sum(1 for a in el.parents if a.name == 'div')
        if i == '01':
            if depth != 0:
                where = el.parent.get('style', '')[:44] if el.parent else '?'
                bad.append(f'{L(f)}: brain-check-01 is {depth} div(s) deep — it is inside '
                           f'{where!r}, not a child of <body>')
            nxt = el.find_next_sibling()
            seats = nxt.find(id='section-6') if nxt else None
            if seats is None:
                bad.append(f'{L(f)}: brain-check-01 next sibling does not seat #section-6')
        else:
            if depth != 1:
                bad.append(f'{L(f)}: brain-check-{i} is {depth} div(s) deep, expected 1')
            st = el.parent.get('style', '') if el.parent else ''
            if 'border: 2px solid '+BAND_END not in st:
                bad.append(f'{L(f)}: brain-check-{i} is not in the gray §10 panel '
                           f'(host style {st[:44]!r})')
# S115: was the literal 9. A count cannot say WHICH lesson moved, and the conversion
# arc (L10/11/12/13/15) would have required editing this number five times, each edit
# indistinguishable from disarming the gate. Derived from the ruled sets instead.
_exp = len({L(f) for f in files} - BC_EXEMPT - BC_PENDING)
if converted != _exp:
    bad.append(f'COVERAGE: {converted} converted lessons scanned, expected {_exp} '
               f'(exempt {sorted(BC_EXEMPT)}, pending {sorted(BC_PENDING)})')
gate('§25.10h Brain Check 01 seats above §6 at body level; 02-04 sit in the §10 panel', bad)

BONUS_CAP = ('<div style="background-color: '+BAND_END+'; color: white; padding: 13px 18px; '
             'border-radius: 8px 8px 0 0; margin-top: 24px;">')

# ---- §4.5: the bonus-block banner is generated from the three-family table.
# Three families, one mark and one word each. Byte-canonicity and PLACEMENT are asserted
# INDEPENDENTLY (the S84 lesson: an encoding drift must never be able to hide a misplaced
# banner), and the count word is verified against the real card count.
def _bonus_cards(s2, after):
    """Count the cards in a bonus block.  ONE definition, used by gate 30 (is the banner's
    count word true?) and gate 31 (is a HELD lesson still under the family floor?)."""
    g = s2.find('id="glossary"')
    seg = s2[after:g] if g > after else s2[after:]
    tagged = re.findall(r'<h[34][^>]*data-challenge="([^"]*)"', seg)
    bnum = set(re.findall(r'\bB([1-9])\b\s*(?:&mdash;|—)', seg))
    h4 = [x for x in re.findall(r'<h4[^>]*>(.*?)</h4>', seg, re.S)
          if 'Reveal' not in x and 'verbatim' not in x]
    return len(tagged) or len(bnum) or len(h4)


BONUS_MARK = {'practice': '&#128296;', 'observation': '&#128269;',
              'sabotage': '&#128373;&#65039;'}
BONUS_WORD = {'practice': 'Extra Practice', 'observation': 'Observation',
              'sabotage': 'Sabotage'}
BONUS_NUM = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7}
BONUS_TABLE = {
    '02': ('practice', 'Six', 'Code Challenges'),
    '03': ('practice', 'Six', 'Motor Challenges'),
    '04': ('observation', 'Five', 'Sensor Experiments'),
    '05': ('observation', 'Six', 'Proximity Experiments'),
    '06': ('observation', 'Five', 'Encoder Experiments'),
    '07': ('observation', 'Five', 'Multi-File Experiments'),
    '08': ('sabotage', 'Five', 'Line-Following Mysteries'),
    '09': ('sabotage', 'Five', 'State-Machine Mysteries'),
    '10': ('sabotage', 'Five', 'Obstacle Mysteries'),
    '11': ('sabotage', 'Four', 'Gap Mysteries'),
    '12': ('sabotage', 'Four', 'Gyro Mysteries'),
    '13': ('sabotage', 'Four', 'Messed Up Files'),
    '14': ('sabotage', 'Four', 'Messed Up Files'),
    '15': ('sabotage', 'Four', 'Messed Up Files'),
}
BONUS_HELD = {'16'}          # DJ ruling S85: 2 cards, revisit at 4.
NAVSIG = 'text-decoration: none; padding: 5px 12px'
bad = []
seen = 0
for f in files:
    lg, s2 = L(f), R[f]
    if lg not in BONUS_TABLE:
        if lg in BONUS_HELD and 'id="bonus-challenges"' in s2:
            continue
        if 'id="bonus-challenges"' in s2:
            bad.append(f'{lg}: has a bonus block but is not in the family table')
        continue
    seen += 1
    fam, count, noun = BONUS_TABLE[lg]

    # (a) byte-canonicity of the banner block
    want = ('<div id="bonus-challenges">'
            f'<span style="display: block; font-size: 0.78em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; opacity: 0.8; margin-bottom: 3px;">{BONUS_WORD[fam]}</span>'
            f'<span style="display: block; font-size: 1.28em; font-weight: 700; letter-spacing: -0.021em;">{count} {noun}</span></div>')
    m = re.search(r'<div id="bonus-challenges".*?</div>', s2, re.S)
    if not m:
        bad.append(f'{lg}: no bonus banner div')
        continue
    if m.group(0) != want:
        bad.append(f'{lg}: banner not byte-canonical\n           got  {m.group(0)}'
                   f'\n           want {want}')

    # (b) PLACEMENT, asserted independently of the bytes above.
    #     The cap is compared BYTE-EXACT, not by substring: a
    #     `background: linear-gradient(135deg, #6c757d, #4d5358)` cap CONTAINS
    #     '#6f7582' and passed the old substring test for its whole life (L03,
    #     found S87).  A substring test cannot distinguish flat from gradient.
    cap = s2.rfind('<div', 0, m.start())
    capopen = s2[cap:s2.find('>', cap) + 1]
    if capopen != BONUS_CAP:
        bad.append(f'{lg}: bonus cap div not byte-canonical\n           got  {capopen}'
                   f'\n           want {BONUS_CAP}')
    after = s2[m.end():m.end() + 260]
    if not re.match(r'\s*</div>\s*<div style="border: 2px solid '+re.escape(BAND_END), after):
        bad.append(f'{lg}: gray cap is not fused to the bordered bonus panel')

    # (c) the count word is true
    real = _bonus_cards(s2, m.end())
    if real != BONUS_NUM[count]:
        bad.append(f'{lg}: banner claims {count} ({BONUS_NUM[count]}) '
                   f'but the block holds {real} cards')

    # (d) no stray or doubled mark, and the retired label is gone
    inner = m.group(0)[m.group(0).find('>') + 1:-6]
    for stray in ['\U0001f528', '\U0001f50d', '\U0001f9e9', '\U0001f575']:
        if stray in inner:
            bad.append(f'{lg}: raw UTF-8 mark survived in the banner')
    if inner.count('&#128373;') > 1 or inner.count('&#128296;') > 1:
        bad.append(f'{lg}: banner mark is doubled')
    if 'Bonus' in inner:
        bad.append(f'{lg}: banner still carries the retired label "Bonus"')

    # (e) the nav pill carries the family word
    navs = [mm for mm in re.finditer(r'<a href="#bonus-challenges"([^>]*)>([^<]*)</a>', s2)
            if NAVSIG in mm.group(1)]
    if len(navs) != 1:
        bad.append(f'{lg}: expected exactly 1 bonus nav pill, found {len(navs)}')
    elif navs[0].group(2) != BONUS_WORD[fam]:
        bad.append(f'{lg}: nav pill reads {navs[0].group(2)!r}, '
                   f'expected {BONUS_WORD[fam]!r}')
if seen != 14:
    bad.append(f'COVERAGE: {seen} lessons scanned against the family table, expected 14')
gate('\u00a74.5  bonus banner generated from the three-family table, placement asserted', bad)

# ---- §4.2 COVERAGE: every bonus card is tagged, and its kind names its family.
# Gate 4 asserts markers are UNIQUE, never PRESENT -- which is why 28 untagged cards
# sat inside a 30/30 book for a year.  This gate rides gate 30's already-verified card
# count: the banner count is true, so the tagged count must equal it.
BONUS_KIND = {'practice': 'bonus-practice', 'observation': 'bonus-observation',
              'sabotage': 'bonus-sabotage'}
bad = []
seen = 0
for f in files:
    lg, s2 = L(f), R[f]
    if lg not in BONUS_TABLE:
        # A held lesson is skipped BY NAME, never absorbed by COVERAGE -- and the hold
        # expires by itself: DJ's S85 ruling was "revisit when it has four cards", so
        # reaching the floor is what makes this gate speak up.
        if lg in BONUS_HELD and 'id="bonus-challenges"' in s2:
            mh = re.search(r'<div id="bonus-challenges".*?</div>', s2, re.S)
            held = _bonus_cards(s2, mh.end()) if mh else 0
            if held >= 4:
                bad.append(f'{lg}: HELD out of the family by the S85 ruling at 2 cards, '
                           f'but it now holds {held} -- the floor is 4, so bring it into '
                           f'§4.5 (banner, pill, tagging) or re-rule the hold')
            continue
        if 'id="bonus-challenges"' in s2:
            bad.append(f'{lg}: has a bonus block but is neither in the family table '
                       f'nor held')
        continue
    seen += 1
    fam, count, _ = BONUS_TABLE[lg]
    m = re.search(r'<div id="bonus-challenges".*?</div>', s2, re.S)
    if not m:
        continue
    g = s2.find('id="glossary"')
    seg = s2[m.end():g] if g > m.end() else s2[m.end():]
    want = BONUS_KIND[fam]
    marked = re.findall(r'data-challenge="([^"]*)"', seg)
    kinds = re.findall(r'data-kind="([^"]*)"', seg)
    if len(marked) != BONUS_NUM[count]:
        bad.append(f'{lg}: banner says {BONUS_NUM[count]} cards but only {len(marked)} '
                   f'carry data-challenge -- an untagged card is invisible to the picker (§20.2)')
    if len(kinds) != BONUS_NUM[count]:
        bad.append(f'{lg}: {len(kinds)} data-kind in the block, expected {BONUS_NUM[count]}')
    off = sorted(set(k for k in kinds if k != want))
    if off:
        bad.append(f'{lg}: block is family {fam!r}, expected every card {want!r}, '
                   f'found {off}')
if seen != 14:
    bad.append(f'COVERAGE: {seen} lessons scanned, expected 14')
gate('\u00a74.2  every bonus card is tagged and its data-kind names its family', bad)


# ---- §4.5a: every bonus block is announced in the flow of the lesson.
#      Before S87 the FINISHED EARLY pointer existed in L02-L09 and was ABSENT in
#      L10-L15, so in six lessons the only route into the bonus block was one nav
#      pill among twelve to fourteen.  The livery had also drifted into three
#      strata (2/2/4) that cut across the families rather than along them.
#      Byte-canonical, like the cap: a substring test cannot see a drift.
FE_BOX = ('<div style="background-color: #f8f9fa; border: 2px solid '+BAND_END+'; '
          'border-radius: 10px; padding: 15px 20px; margin: 25px 0;">')
bad = []
seen = 0
for f in files:
    lg, s2 = L(f), R[f]
    if lg not in BONUS_TABLE:
        continue
    seen += 1
    n = s2.upper().count('FINISHED EARLY')
    if n != 1:
        bad.append(f'{lg}: expected exactly 1 FINISHED EARLY pointer, found {n}')
        continue
    i = s2.upper().find('FINISHED EARLY')
    st = s2.rfind('<div', 0, i)
    box = s2[st:s2.find('>', st) + 1]
    if box != FE_BOX:
        bad.append(f'{lg}: FINISHED EARLY box not byte-canonical\n           got  {box}'
                   f'\n           want {FE_BOX}')
    b = s2.find('id="bonus-challenges"')
    if b < 0 or st > b:
        bad.append(f'{lg}: FINISHED EARLY pointer does not precede the bonus block')
    seg = s2[st:s2.find('</div>', i) + 6]
    if 'href="#bonus-challenges"' not in seg:
        bad.append(f'{lg}: FINISHED EARLY pointer carries no link to the bonus block')
if seen != 14:
    bad.append(f'COVERAGE: {seen} lessons checked for the pointer, expected 14')
gate('\u00a74.5a every bonus block is announced by a canonical FINISHED EARLY pointer', bad)

# ---- §5.1 CALLOUT GEOMETRY, AGAINST A FROZEN BASELINE (v1.22 — NEW, S91, DJ ruling)
# ---- The standard fixes the callout rule at `border-left: 4px solid`. 115 live blocks are
# ---- off it — 112 at 5px, 3 at 3px — and 83 of those sit in L11/L12, authored entirely in a
# ---- second design system. Shipping this ABSOLUTE would fail every run until the repaint,
# ---- and the repaint is blocked on an unapproved semantic palette: a gate that cries wolf
# ---- gets ignored (S90), and it would drag the other 32 down with it.
# ---- So the existing debt is FROZEN as a baseline and anything NEW fails. This is NOT the
# ---- S82 "widen the matcher" move DJ ruled against — widening would accept 5px forever and
# ---- everywhere. A baseline names the debt that exists, rejects the 116th block, and is
# ---- built to go to ZERO at the repaint, at which point the baseline empties and the gate
# ---- becomes absolute. Signatures are (lesson, px, border, bg) so they survive line shifts.
# ---- Note not all 115 are drift: `#1a5276`/`#f8f9fa` is one block per lesson in L01-L11 and
# ---- `#6c757d`/`#f8f9fa` one per lesson in L12-L16 — uniform constructs that happen to be
# ---- 5px. Geometry is read through lesson_inventory's parser (§24.10), never a regex here.
GEOM_BASELINE = {
    ('01', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('02', 3, '#fbc02d', '#fffde7'): 2,
    ('02', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('03', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('03', 5, '#2e86ab', '#f4f9fc'): 1,
    ('03', 5, '#ffc107', '#fff8e1'): 1,
    ('04', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('05', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('05', 5, '#607d8b', '#eceff1'): 1,
    ('05', 5, '#ffc107', '#fff8e1'): 1,
    ('06', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('06', 5, '#c0392b', '#fdecea'): 1,
    ('07', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('08', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('09', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('10', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('11', 3, '#ccc', None): 1,
    ('11', 5, '#0e1a2c', '#f8f9fa'): 1,
    ('11', 5, '#27ae60', '#eafaf1'): 6,
    ('11', 5, '#607d8b', '#eceff1'): 7,
    ('11', 5, '#6b8e6b', '#f0f7f0'): 3,
    ('11', 5, '#e74c3c', '#fdecea'): 5,
    ('12', 5, '#27ae60', '#eafaf1'): 13,
    ('12', 5, '#607d8b', '#eceff1'): 20,
    ('12', 5, '#6b8e6b', '#f0f7f0'): 8,
    ('12', 5, BAND_END, '#f5eef8'): 4,
    ('12', 5, BAND_END, '#f8f9fa'): 1,
    ('12', 5, '#e74c3c', '#fdecea'): 13,
    ('12', 5, '#ffc107', '#fff8e1'): 1,
    ('13', 5, BAND_END, '#f8f9fa'): 1,
    ('14', 5, BAND_END, '#f8f9fa'): 1,
    ('15', 5, '#2e86ab', '#f4f9fc'): 3,
    ('15', 5, '#433014', '#eef7f1'): 1,
    ('15', 5, BAND_END, '#f8f9fa'): 1,
    ('16', 5, '#433014', '#eef7f1'): 5,
    ('16', 5, BAND_END, '#f8f9fa'): 1,
    ('16', 5, '#ffc107', '#fff8e1'): 1,
}
bad = []
seen_lessons = set()
live = collections.Counter()
for f in sorted(glob.glob('lessons/Lesson_*.html')):
    inv = LI.build(f)
    seen_lessons.add(inv['lesson'])
    if not inv['callouts']:
        bad.append(f'L{inv["lesson"]}: parser returned ZERO callouts — coverage defect')
    for c in inv['callouts']:
        if c['px'] != 4:
            live[(inv['lesson'], c['px'], c['border'], c['bg'])] += 1
for sig, cnt in sorted(live.items()):
    allowed = GEOM_BASELINE.get(sig, 0)
    if cnt > allowed:
        bad.append(f'L{sig[0]}: {cnt - allowed} NEW off-canon block(s) at {sig[1]}px '
                   f'border {sig[2]} bg {sig[3]} (baseline {allowed}, found {cnt})')
if len(seen_lessons) != 16:
    bad.append(f'COVERAGE: {len(seen_lessons)} lessons parsed, expected 16')
_shrunk = sum(GEOM_BASELINE.values()) - sum(live.values())
gate('\u00a75.1 callout geometry: no NEW off-canon border width'
     + (f' (debt {sum(live.values())}/{sum(GEOM_BASELINE.values())}, '
        f'{_shrunk} retired — tighten the baseline)' if _shrunk > 0
        else f' (frozen debt {sum(live.values())}, zero at the repaint)'), bad)

# ---- §5.1 THE CALLOUT TITLE IS A BLOCK ELEMENT, ONE FORM BOOK-WIDE (NEW, S91, DJ ruling)
# ---- DJ: "Why would i want a div bold?" -- the answer is §5.1's three properties, which a
# ---- bare <strong> carries none of: margin-bottom 8px, font-size 1.05em, and block display
# ---- so the body needs no <br>. The live book had it backwards: 794 titles were <strong>
# ---- against 55 in §5.1's form, while §5.1 claimed "Geometry is unchanged from prior
# ---- practice." Swept S91 -- 794 converted, 119 now-redundant <br> removed.
# ---- Recorded so nobody reverts it: <strong> is SEMANTIC and a bold div is not, so this
# ---- costs the emphasis cue on 794 titles. The title is still the first text in the block,
# ---- so nothing became unreachable. DJ ruled the div for consistency; §5.1 records the cost.
bad = []
seen = 0
for f in sorted(glob.glob('lessons/Lesson_*.html')):
    src = R[f]
    lines = src.split('\n')
    for c in LI.build(f)['callouts']:
        off = sum(len(l) + 1 for l in lines[:c['line'] - 1])
        # v1.26.3: anchor on the callout's OWN opening tag, not the first '>' after the line
        # start. L14's THE ONE IDEA shares its line with the </div> that closes the block
        # above it, so find('>') landed on THAT tag, the check ran one element late, and a
        # bare <strong> title passed unseen. c['tag'] names the element; search for it.
        _open = src.find('<' + c['tag'], off)
        gt = src.find('>', _open) if _open >= 0 else src.find('>', off)
        if gt < 0:
            continue
        seen += 1
        i = re.match(r'\s*', src[gt + 1:]).end() + gt + 1
        # S91 second pass: the first version rejected only a bare <strong>, so 120 <span>-led
        # and 44 <b> titles walked straight through -- the same construct in three shapes.
        # A <b> that is NOT followed by <br> or a block element is a sentence SUBJECT, not a
        # title, and must be left alone; 22 of those are legitimate.
        if src.startswith('<strong', i) or src.startswith('<span', i):
            bad.append(f'{L(f)} line {c["line"]}: callout title is inline, \u00a75.1 requires '
                       f'the block form')
        elif re.match(r'<b\b(?![a-z])', src[i:]):
            m = re.match(r'<b\b(?![a-z])[^>]*>.*?</b>', src[i:], re.S)
            if m and re.match(r'\s*(?:<br|<p\b|<ul\b|<ol\b|<div\b|<h[1-6]\b)', src[i + m.end():]):
                bad.append(f'{L(f)} line {c["line"]}: callout title is <b>, \u00a75.1 requires '
                           f'the block form')
if seen < 900:
    bad.append(f'COVERAGE: only {seen} callouts inspected, expected 1000+')
gate('\u00a75.1 callout title uses the block form, never a bare <strong>', bad)

# ---- §5.1 OPTION C: THE LABEL ELEMENT HOLDS THE FAMILY WORD AND NOTHING ELSE (NEW, S92)
# ---- DJ ruling. The whole return on Option C is that a block's family is readable by EXACT
# ---- MATCH instead of by parsing a family word off the front of authored prose -- which is
# ---- what made the amber scheme unclassifiable at S91 (one scheme, six jobs). This gate is
# ---- what makes that guarantee real; without it the label silently reacquires prose.
# ---- Censused before writing, per S91's lesson that gate 34 covered one shape of three:
# ---- the live shapes are (a) label alone, 72 blocks, and (b) label + title, 178 blocks.
# ---- Scope is the (bg, border) scheme, NOT the glyph -- the scheme is the family of record
# ---- (S92 ruling), and 3 blocks on non-canonical schemes are deliberately OUT of scope and
# ---- logged for the family-table batch, so a COVERAGE assert pins the count at 250.
_SCHEME = {('#f0f7f0', '#6b8e6b'): 'TIP',
           ('#eceff1', '#607d8b'): 'NOTE',
           ('#fff8e1', '#ffc107'): 'WARNING'}
# ---- S129: THE GLYPH LEAVES THIS GATE, IN BOTH OF THE PLACES IT SAT.
# ---- S92 scoped on GLYPH AND SCHEME AGREEING, because the scheme alone is not the family
# ---- of record -- 24 blocks borrow §6.6a paint while carrying another family's glyph. That
# ---- reasoning stands; the glyph was simply the only content signal available in S92.
# ---- §24.14a made the family an ATTRIBUTE, so the agreement is now scheme vs data-family,
# ---- which is content rather than decoration. This matters beyond tidiness: the marks arc
# ---- replaces the emoji, and the S128 L04 control measured this gate's coverage falling
# ---- 251 -> 240 on ONE lesson's worth of marks, because the glyph here is a SCOPE FILTER --
# ---- so blocks left un-inspected rather than failing. Silent, and the silence grows with
# ---- every mark applied.
# ---- MEASURED, not assumed: the swap scopes 255 where the glyph scoped 251, and the five
# ---- that enter were hidden ONLY by wearing a non-canonical emoji on canonical paint.
# ---- One passes; four carry a descriptive title in the label div and are HELD BY NAME
# ---- below, because a gate must not silently exempt what it has just been able to see.
_FAMGLYPH = {'TIP': '\U0001F4A1', 'NOTE': '\U0001F4D8', 'WARNING': '\u26A0'}
# S129: newly visible §5.1 violations, held by NAME (§25.2a) pending DJ's ruling on whether
# the label is corrected or the block is ruled out of §6.6a. Each is on canonical §6.6a paint
# with a content-resolved family, and each carries a descriptive title where Option C (S92)
# requires the bare family word. Emptying this set must FAIL, not pass -- see the coverage arm.
# S129: EMPTIED. DJ ruled option A -- canonical family glyph in the label, old glyph dropped
# -- and all four were split in the same pass, so the hold has no members. Kept as a named
# set rather than deleted: the second coverage arm below still fails if a member is added
# without a matching block, which is the drift a bare deletion would stop catching.
_S51_HELD = set()


def _undecorate(s):
    """Strip a leading decoration run -- emoji, variation selector, spacing.

    The family words are ASCII, so removing leading non-ASCII is safe here. This is what
    makes the check MARK-SAFE: the label extractor already strips every tag, so an
    <img data-mark> contributes no text and a marked label reduces to the same string a
    glyphed one does. The gate therefore asserts the PROPERTY -- the label holds exactly
    the family word -- and says nothing about which decoration precedes it. Decoration is
    owned by §24.14b, deliberately, so this gate cannot certify a spelling (S128 rule 18).
    """
    # U+FE0F needs no literal here: it is above the 0x2100 floor, so the ordinal test
    # already takes it. Spelling it out would be a glyph literal in a locator for no gain.
    i = 0
    while i < len(s) and (ord(s[i]) >= 0x2100 or s[i] in ' \t'):
        i += 1
    return s[i:].strip()


bad = []
seen = 0
held_seen = set()
for f in sorted(glob.glob('lessons/Lesson_*.html')):
    src = R[f]
    lines = src.split('\n')
    for c in LI.build(f)['callouts']:
        fam = _SCHEME.get((c['bg'], c['border']))
        _fa = re.search(r'data-family="([^"]*)"', lines[c['line'] - 1])
        if fam is None or _fa is None or _fa.group(1) != fam:
            continue
        off = sum(len(l) + 1 for l in lines[:c['line'] - 1])
        # v1.26.3: anchor on the callout's OWN opening tag, not the first '>' after the line
        # start. L14's THE ONE IDEA shares its line with the </div> that closes the block
        # above it, so find('>') landed on THAT tag, the check ran one element late, and a
        # bare <strong> title passed unseen. c['tag'] names the element; search for it.
        _open = src.find('<' + c['tag'], off)
        gt = src.find('>', _open) if _open >= 0 else src.find('>', off)
        if gt < 0:
            continue
        i = re.match(r'\s*', src[gt + 1:]).end() + gt + 1
        m = re.match(r'<div\b[^>]*>(.*?)</div>', src[i:], re.S)
        if not m:
            continue          # titleless / sentence-lead <b>; gate 34 owns those
        seen += 1
        # unescape: glyphs are numeric entities in some lessons (L11/L12), and a matcher that
        # forgets that reports every entity-encoded block as broken. S92 hit this exact bug.
        label = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))).strip()
        rest = _undecorate(label)
        if rest == fam:
            continue
        if rest in _S51_HELD:
            held_seen.add(rest)
            continue
        bad.append(f'{L(f)} line {c["line"]}: label carries {rest[:40]!r}, '
                   f'\u00a75.1 requires exactly {fam!r}')
# COVERAGE has TWO arms and they fail for different reasons (S117/S118: a gate that scans
# zero blocks passes). The first pins the scoped population; the second pins the hold, so a
# held label that gets CORRECTED -- or a hold that drifts off its subject -- fails loudly
# instead of silently certifying nothing (S128 rule 20).
if seen != 255:
    bad.append(f'COVERAGE: {seen} labels inspected, expected 255 '
               f'(scheme and data-family must agree; blocks with no title div are gate 34s)')
if held_seen != _S51_HELD:
    bad.append(f'COVERAGE: the \u00a75.1 hold matched {len(held_seen)} of {len(_S51_HELD)} '
               f'named labels; unmatched {sorted(_S51_HELD - held_seen)}')
gate('\u00a75.1 callout label holds exactly the family word, matched to its scheme', bad)


# ---------------------------------------------------------------- gate 36 (S97)
# Every image reference resolves to a file on disk.
# Two reference forms occur in the book, surveyed not assumed: 193 absolute site URLs
# and 23 relative (favicon). A THIRD form appearing later would be invisible to this
# matcher, so the resolved-count assert below is what makes that hole loud instead of
# silent — if a page starts writing refs some other way, the count moves and the gate
# says so. An assert that cannot fail is not evidence.
_SITE_PREFIX = 'https://weymuth.github.io/zumo/'
_REF_RE = re.compile(
    r'(?:src|href|xlink:href)\s*=\s*["\']([^"\']+?\.(?:png|jpe?g|svg|gif|webp|ico))'
    r'(?:[?#][^"\']*)?["\']', re.I)
from urllib.parse import unquote as _unquote

bad, _seen = [], 0
_REFERENCED = set()          # consumed by gate 37; built here so there is ONE resolver
for _page in site:
    if not os.path.exists(_page):
        continue
    _src = open(_page, encoding='utf-8', errors='replace').read()
    for _m in _REF_RE.finditer(_src):
        _u = _m.group(1)
        if _u.startswith(_SITE_PREFIX):
            _p = _unquote(_u[len(_SITE_PREFIX):])
        elif _u.startswith(('http://', 'https://', 'data:', '//')):
            continue                       # off-site, not ours to resolve
        elif _u.startswith('/'):
            _p = _unquote(_u.lstrip('/'))
        else:
            _p = os.path.normpath(os.path.join(os.path.dirname(_page), _unquote(_u)))
        _seen += 1
        _REFERENCED.add(_p.replace(os.sep, '/'))
        if not os.path.isfile(_p):
            _ln = _src.count('\n', 0, _m.start()) + 1
            # L() is the fixed slice f[15:17] and is meaningful ONLY for
            # lessons/Lesson_NN.html; on index.html it returns ''. A gate that
            # reports a defect it cannot name is half a gate. Caught by the S97
            # scope control, which seeded breaks into the non-lesson pages.
            _who = L(_page) if _page in files else _page
            bad.append(f'{_who} line {_ln}: image reference -> {_p} does not exist')
if _seen != 1202:                     # 1201 -> 1202 at S138: GRAPHIC 4.7 lands twice in L04
                                      # (§1 and §4.1) and the borrowed L11 diagram leaves: net +1.
                                      # 1198 -> 1201 at S135: the three §1 hook figures land. 3
                                      # of the 151 term cards had no key mark; the canon
                                      # card carries one, so 64 new image references.
                                      # DERIVED: 1,134 + 64, and 151 - 87 already-marked
                                      # = 64 reconciles from the other side.
                                      # 250 -> 1134 at S130: THE MARKS ARC LANDED. 884
                                      # callouts swapped a leading emoji for an <img>
                                      # mark, and every one is a new image reference.
                                      # DERIVED, not projected: 250 + 884 = 1,134, and
                                      # mark_wire reconciled at 884 SWAP + 13 NO_GLYPH +
                                      # 56 HELD + 116 NO_MARK = 1,069 callouts. Three
                                      # earlier projections gave three different answers
                                      # (1,134 by wrong arithmetic, 1,147 by counting the
                                      # 13 insertions the tool reports but never writes);
                                      # only the run settles it, and the run says 1,134.
                                      # 240 -> 245 at S118: L13 converted, five more
                                      # BrainGear_Incomplete.png refs. Controlled against
                                      # the pushed clone: that filename is the SOLE delta,
                                      # 45 -> 50; every other image count byte-identical.
                                      # 223 -> 224 at S106: L02 IMAGE 2.2 wired in;
                                      # 225 -> 230 at S115: L10 converted to the four
                                      # exit blocks. Controlled: the ONLY reference that
                                      # moved is BrainGear_Incomplete.png 45 -> 50 (four
                                      # BC caps + the nav column). No other file changed.
                                      # 224 -> 225 at S113: DJ supplied the A-Star board
                                      # photo and L03 IMAGE 3.14 was wired in. The number
                                      # moves ONLY when a figure genuinely lands - that is
                                      # the whole point of the assert.
    bad.append(f'COVERAGE: {_seen} image references resolved, expected 1,202 — a reference '
               f'was added, removed, or written in a form this gate cannot see')
# S102: the walk above matches IMAGE EXTENSIONS only (png|jpe?g|svg|gif|webp|ico). A download
# link to any other extension in images/ was therefore invisible, and one rotted in the live
# book: Lesson 02 rendered a blue "Download the Sketch Anatomy diagram (PDF)" button pointing at
# a file that had been removed. Gates passed, site_parity passed - it walks the same list - and
# a student clicking it got a 404. Two such links exist in the whole book, so this assert is
# nearly free, and it is the difference between knowing and happening to look.
_ANY_REF_RE = re.compile(r'href\s*=\s*["\']([^"\']*?/images/[^"\']+?)["\']', re.I)
for _page in site:
    if not os.path.exists(_page):
        continue
    _src = open(_page, encoding='utf-8', errors='replace').read()
    for _m in _ANY_REF_RE.finditer(_src):
        _u = _m.group(1)
        if _u.startswith(_SITE_PREFIX):
            _p = _unquote(_u[len(_SITE_PREFIX):])
        elif _u.startswith(('http://', 'https://', 'data:', '//')):
            continue
        else:
            _p = os.path.normpath(os.path.join(os.path.dirname(_page), _unquote(_u)))
        if not os.path.isfile(_p):
            _ln = _src.count('\n', 0, _m.start()) + 1
            _who = L(_page) if _page in files else _page
            bad.append(f'{_who} line {_ln}: link -> {_p} does not exist '
                       f'(a download button pointing at nothing)')
gate('\u00a721   every image reference resolves to a file on disk', bad)


# ---------------------------------------------------------------- gate 37 (S97, rewritten S98)
# §21.1 was "no REFERENCED .svg carries an embedded raster", and that rule was WRONG —
# it forbade an asset class this book needs. Measured in S98: every one of the five staged
# raster-in-SVG files carries PHOTOGRAPHIC content (top-50 colours cover 9–48% of pixels),
# and the one true-vector redraw of a board (…_top_view_r02.svg, 194 elements, zero raster)
# turned out to be a CARTOON — its 39 text runs are the silkscreen, not labels. A photograph
# of a populated PCB cannot be redrawn, and DJ's ruling is that these stay raster.
#   They must also EMBED. An SVG loaded through <img src> runs in secure static mode and
# cannot fetch an external file, so photo-plus-crisp-vector-labels in one file has no
# external-href option. A gate forbidding base64 forbids the composite itself.
#
# What S97 actually found was not "a raster" but THREE separable defects, and this gate now
# names each one. Every threshold below comes from measurement, not taste:
#   DUP     one <image> carrying the payload TWICE, href= and xlink:href= both holding the
#           full base64. Not two layers — identical bytes, one drawn image, double the file.
#           Free to fix, invisible on screen, present in 2 of 5 staged files.
#   CEILING the student-facing cost. fit_raster_svg.py takes the uploaded board photo from
#           4,262,718 B to 350,471 B with no visible change, so a real composite lands well
#           under this; 500,000 B leaves room without licensing a megabyte.
#   FLOOR   the S97 defect proper: the memory ladder had ZERO drawing elements — a bitmap in
#           an envelope, 4.9 MB, claiming to be a diagram. A composite has labels on it. A
#           file with a raster and almost no vector is a PHOTOGRAPH and belongs at .jpg/.png
#           under the IMAGE_ name, which is already this book's convention (IMAGE = photo,
#           GRAPHIC = drawn).
# Scoping is unchanged and deliberate: fatal for REFERENCED files, counted for staged ones.
CEILING = 500_000
FLOOR = 3
_svgs = sorted(f.replace(os.sep, '/') for f in glob.glob('images/**/*.svg', recursive=True))
_staged, bad = [], []
for _f in _svgs:
    _s = open(_f, encoding='utf-8', errors='replace').read()
    if 'base64' not in _s:
        continue
    _sz = os.path.getsize(_f)
    _draw = len(re.findall(r'<(?:path|rect|text|circle|line|polygon|polyline|ellipse)\b', _s))
    _faults = []
    for _tag in re.findall(r'<image\b[^>]*>', _s):
        _uris = re.findall(r'href="(data:image/[a-z]+;base64,[^"]*)"', _tag)
        if len(_uris) > 1 and len(set(_uris)) == 1:
            _faults.append('payload stored twice in one <image> (href and xlink:href) — '
                           'half this file is a duplicate of itself')
            break
    if _sz > CEILING:
        _faults.append(f'{_sz:,} B, over the {CEILING:,} B ceiling — run fit_raster_svg.py')
    if _draw < FLOOR:
        _faults.append(f'{_draw} drawing element(s): this is a photograph, not a graphic — '
                       f'ship it as .jpg/.png under an IMAGE_ name')
    if not _faults:
        continue
    _msg = f'{_f}: ' + '; '.join(_faults)
    (bad if _f in _REFERENCED else _staged).append(_msg)
gate('\u00a721.1 embedded rasters are deduped, under the ceiling, and carry vector content', bad)
if _staged:
    print(f'         note: {len(_staged)} unreferenced .svg would fail this gate if wired in '
          f'(staged, not fatal)')
    for _m in _staged:
        print(f'           - {_m}')


# ---------------------------------------------------------------- gate 38 (S98)
# §21.2 A DRAWN GRAPHIC KEEPS ITS TEXT AND STAYS SMALL.
# Written for a defect that was LIVE for a week and passed 37/37 every run. Four referenced
# graphics — L06 6-09, 6-10, 6-12 and L07 7-02 — came back from a redo with every label
# converted to OUTLINES: 23,066 B -> 1,148,110 B, a 50x growth and +1.13 MB on the published
# site. One of them rode in on 09a33f8, the same commit that carried the gate suite's own
# update, and post-push verification missed it because it byte-matched the files on the push
# list and never diffed the rest of the tree.
#   The cause is defensible: a graphic drawn in Inter or JetBrains Mono renders wrong on a
# student's machine, and outlining is a real fix for that. It is the WRONG fix — the cheap one
# is a common font stack, and all five files came back at 6–11 KB with 32–42 LIVE labels once
# asked for Arial/Courier New. Outlined text is also unselectable, unsearchable and invisible
# to a screen reader, which is the same objection §17.3 raises against prose baked into pixels.
#
# Gate 37 owns the files that CONTAIN a raster. This gate owns the complement: true vector.
# Three checks, every threshold measured against the whole book this session, none inherited:
#   CEILING   60,000 B. The largest true-vector file in the book is the Mercersburg wordmark
#             at 12,904 B and the largest GRAPHIC_ is 10,943 B, so this sits 4.6x above
#             anything legitimate and 3.5x below the smaller of the two real defects
#             (209,178 B and 319,014 B, restored from 0b3f070^ and used as control A).
#   LABELS    a file named GRAPHIC_ carries at least one <text>. Measured: 83 GRAPHIC_ vector
#             files, ZERO of them text-less, minimum label count 7. The two legitimate
#             text-less families need no exemption because neither is named GRAPHIC_ — the
#             wordmark is a logo and the §18.2 spiral stars carry vector-path digits BY RULING.
#   OUTLINED  zero <text> AND more than 50,000 B of path data, for anything NOT named GRAPHIC_
#             — the same defect arriving under a different filename. The largest legitimate
#             text-less path payload in the book is the wordmark's 11,173 B (next: 2,396 B, an
#             icon; the stars are all under 962 B); the defect files carry 197,247 B and
#             304,159 B. The line sits 4.5x above the first and 3.9x below the second.
#
# Scoping mirrors gate 37 and for the same reason: fatal on files a page REFERENCES, counted
# and printed for staged ones. Raw exports land in images/ before being wired up, and a gate
# that reddens on work-in-progress is a gate people learn to ignore.
VEC_CEILING = 60_000
OUTLINE_PD = 50_000
# GRAPHIC_PD closes a hole in v1.31 found by re-deriving that gate's own findings on a second
# and third parser (S99). The label check above is a FLOOR OF ONE, so a graphic with 26 of its
# 27 labels outlined and one left live satisfied it: measured, that file sat at 19,225 B with
# 15,730 B of path data and passed the whole suite green. Threshold from arithmetic, not taste —
# outlining a SINGLE label cost 5,190 B (L06 6-09, 38 labels) and 9,216 B (L07 7-02, 33 labels)
# on the two real S98 defect files, while the largest path payload on any legitimate drawn
# graphic in the book is 960 B and 55 of the 83 carry exactly zero. 5,000 B therefore sits 5.2x
# above anything legitimate and still fires on the outlining of one label.
#   The cost is stated: a future graphic built from genuinely path-heavy vector art — curved
# arrows, traced silhouettes — could reach this honestly. That is a threshold to RAISE with a
# measurement, not a reason to leave partial outlining ungated.
GRAPHIC_PD = 5_000
_vec, _staged38, bad = [], [], []
for _f in _svgs:                              # same population gate 37 walked, complemented
    _s = open(_f, encoding='utf-8', errors='replace').read()
    if 'base64' in _s:
        continue                              # gate 37's file, not this one's
    _vec.append(_f)
    _base = os.path.basename(_f)
    _isg = 'GRAPHIC_' in _base
    _sz = os.path.getsize(_f)
    _ntext = len(re.findall(r'<text\b', _s))
    _pd = sum(len(_m) for _m in re.findall(r'\bd\s*=\s*"([^"]*)"', _s))
    _faults = []
    if _sz > VEC_CEILING:
        _faults.append(f'{_sz:,} B, over the {VEC_CEILING:,} B ceiling for a drawn graphic '
                       f'(largest legitimate in the book is 12,904 B)')
    if _isg and _ntext == 0:
        _faults.append('named GRAPHIC_ but carries zero <text>: its labels have been converted '
                       'to outlines — re-export with live text in a common stack '
                       '(Arial / Courier New), per Bible §17.3a recipe 1')
    if _isg and _pd > GRAPHIC_PD:
        _faults.append(f'{_pd:,} B of path data on a drawn graphic, over the {GRAPHIC_PD:,} B '
                       f'ceiling: labels appear to be outlined. The >=1 <text> floor above is '
                       f'satisfied by a SINGLE surviving label, so it does not catch partial '
                       f'outlining — this check is the half that does')
    if not _isg and _ntext == 0 and _pd > OUTLINE_PD:
        _faults.append(f'zero <text> over {_pd:,} B of path data — this looks like outlined '
                       f'text under a non-GRAPHIC_ name')
    if not _faults:
        continue
    _msg = f'{_f}: ' + '; '.join(_faults)
    (bad if _f in _REFERENCED else _staged38).append(_msg)

# COVERAGE. An assert that cannot fail is not evidence (§24.6b): if the glob breaks, the
# population empties and every check above passes vacuously. Both numbers are STATED, not
# inherited, and both are expected to move when a graphic is added or removed — bump them
# in the same edit, the way gate 36's reference count is maintained.
if len(_vec) != 179:
    bad.append(f'COVERAGE: {len(_vec)} true-vector .svg walked, expected 179 — a file was '
               f'added, removed, or now carries a raster (which moves it to gate 37)')
_ngraphic = sum(1 for _f in _vec if 'GRAPHIC_' in os.path.basename(_f))
if _ngraphic != 67:
    bad.append(f'COVERAGE: {_ngraphic} GRAPHIC_ vector files walked, expected 67 — the label '
               f'check is the one that binds on every one of them, so this number is load-bearing')
gate('\u00a721.2 drawn graphics keep live text and stay under the ceiling', bad)
if _staged38:
    print(f'         note: {len(_staged38)} unreferenced .svg would fail this gate if wired in '
          f'(staged, not fatal)')
    for _m in _staged38:
        print(f'           - {_m}')


# ---------------------------------------------------------------- GATE 39
# §17.3c  A COMPOSITE MUST OPEN IN ILLUSTRATOR.
# S99: every raster-carrying .svg in the book rendered perfectly in a browser and NONE of
# them would open for editing. Plain href="" on <image> is SVG 2; Illustrator parses SVG
# 1.1, cannot read the attribute, and reports a MISSING LINK naming the containing folder —
# which reads like a stray file rather than a format problem. It took DJ trying to edit one
# to find, because no gate looked and the browser never complained.
# S100: recorded as advisory in svg_layout_audit, which the suite does not run. Advisory is
# how this regressed once already, so it moves into the suite here.
# Two faults, both fatal to editability and both invisible on screen:
#   1. an <image> carrying a plain href (with or without xlink alongside)
#   2. xlink:href used while xmlns:xlink is undeclared — malformed, may not parse at all
NIMG_EXPECTED = 32           # stated, not inherited — bump when an <image> is added
#   27 -> 28 at S106: L02_IMAGE_2-02_zumo_buttons_labeled.svg joined the book. The gate
#   caught it entering on a fresh clone — the file's own xlink was correct, so the ONLY
#   thing that saw a new composite arrive was this stated count.
_bad39, _staged39 = [], []
for _f in sorted(glob.glob('images/**/*.svg', recursive=True)):
    try:
        _s = open(_f, encoding='utf-8', errors='replace').read()
    except OSError as _e:
        _bad39.append(f'{os.path.basename(_f)}: unreadable ({_e})')
        continue
    _imgs = re.findall(r'<image\b[^>]*>', _s)
    if not _imgs:
        continue
    _faults = []
    _plain = [_t for _t in _imgs if re.search(r'(?<![:\w-])href\s*=', _t)]
    if _plain:
        _faults.append(f'{len(_plain)} of {len(_imgs)} <image> carry a plain href — SVG 2. '
                       f'Illustrator reports MISSING LINK and the file cannot be edited. '
                       f'Use xlink:href (§17.3c)')
    if 'xlink:href' in _s and 'xmlns:xlink' not in _s:
        _faults.append('xlink:href used but xmlns:xlink is not declared on <svg>')
    if _faults:
        _msg = f'{os.path.basename(_f)}: ' + '; '.join(_faults)
        (_bad39 if _f.replace(os.sep, '/') in _REFERENCED else _staged39).append(_msg)
_nimg39 = sum(1 for _f in glob.glob('images/**/*.svg', recursive=True)
              if '<image' in open(_f, encoding='utf-8', errors='replace').read())
if _nimg39 != NIMG_EXPECTED:
    _bad39.append(f'COVERAGE: {_nimg39} raster-carrying .svg walked, expected {NIMG_EXPECTED} '
                  f'— an <image> was added or removed; bump this in the same edit')
gate('\u00a717.3c embedded rasters use xlink:href so the file opens in Illustrator', _bad39)
if _staged39:
    print(f'         note: {len(_staged39)} unreferenced .svg would fail this gate if wired in '
          f'(staged, not fatal)')
    for _m in _staged39:
        print(f'           - {_m}')



# ---------------------------------------------------------------- GATE 40
# §21.1b  FRAGILE-IF-EDITED. A file can be comfortably under the ceiling today and still be
# one Illustrator save away from breaking it.
# S100 measured the mechanism. An embedded photo is ~97% of a composite's bytes, so markup
# bloat from a round-trip is noise (+3,825 B on a 374 KB file). What matters is that
# Illustrator DECODES the payload on open and RE-ENCODES it on save — and if it writes a
# JPEG back as lossless PNG the payload can quadruple. Measured on this repo's own files:
#   5-05  264,393 B as JPEG  ->  833,591 B as lossless PNG   (ceiling is 500,000)
#   2-08  144,942 B as JPEG  ->  620,080 B as lossless PNG
# S99's `L01 1-10` is the same event observed from the outside: 439 KB up, 2.37 MB back.
# CONVERTING THEM TO PNG PRE-EMPTIVELY IS THE WRONG FIX and was measured too: lossless PNG
# is over the ceiling, and palette PNG that fits costs 4x the drift of JPEG q92 (1.708 vs
# 0.454 mean, max error 133 vs 42) — it degrades the picture more than the hazard it avoids.
# So the JPEGs stay and this gate carries the warning instead: it names every file that
# would breach the ceiling if its payload came back lossless, so a round-trip is caught
# BEFORE the push rather than after. Advisory by design — these files are correct today.
# PIL is NOT a dependency of this suite. If it is absent the gate says so and stays green:
# a crash is worse than a false positive, and worse still than a missing advisory check.
try:
    import io as _io, base64 as _b64mod
    from PIL import Image as _PIL
    _HAVE_PIL = True
except ImportError:
    _HAVE_PIL = False

_frag = []
for _f in (sorted(glob.glob('images/**/*.svg', recursive=True)) if _HAVE_PIL else []):
    if _f.replace(os.sep, '/') not in _REFERENCED:
        continue
    try:
        _s = open(_f, encoding='utf-8', errors='replace').read()
    except OSError:
        continue
    _pays = re.findall(r'data:image/(\w+);base64,([^"]+)', _s)
    if not _pays:
        continue
    _cur = len(_s.encode('utf-8'))
    _payb = sum(len(_p[1]) for _p in _pays)
    _markup = _cur - _payb
    _worst = 0
    for _fmt, _data in _pays:
        try:
            _img = _PIL.open(_io.BytesIO(_b64mod.b64decode(_data)))
            _buf = _io.BytesIO()
            _img.save(_buf, 'PNG', optimize=True)
            _worst += len(_buf.getvalue())
        except Exception:
            _worst += len(_b64mod.b64decode(_data))
    _if_lossless = _markup + int(_worst * 4 / 3)
    _headroom = CEILING - _cur
    if _if_lossless >= CEILING:
        _frag.append(f'{os.path.basename(_f)}: {_cur:,} B now ({_headroom:,} spare) but '
                     f'~{_if_lossless:,} B if a round-trip returns the payload lossless — '
                     f're-fit it here before pushing an edited copy')
    elif _headroom < CEILING * 0.20:
        _frag.append(f'{os.path.basename(_f)}: only {_headroom:,} B under the ceiling — '
                     f'any re-save is likely to breach it')
gate('\u00a721.1b no referenced composite is one Illustrator save from the ceiling', [])
if not _HAVE_PIL:
    print('         note: PIL not installed — the fragile-if-edited check did not run')
if _frag:
    print(f'         note: {len(_frag)} referenced file(s) are FRAGILE IF EDITED '
          f'(correct today, advisory)')
    for _m in _frag:
        print(f'           - {_m}')


# ---- §27 (S104): every class a lesson uses must have a rule in css/book.css.
# THE MIGRATION CREATES THIS FAILURE MODE AND NOTHING ELSE CATCHES IT. Measured, not
# assumed: typing one callout's class as `callout-typo` dropped L01's callout census from
# 83 to 82 and ALL 40 GATES STAYED GREEN. Before the migration a mistyped inline style
# left the element visibly wrong and still fully parseable; after it, a mistyped class
# makes the element INVISIBLE to every instrument that reads CSS. An element that
# vanishes is worse than one that is wrong, because only one of the two gets found.
# The reverse direction - a rule no page uses - is REPORTED, never fatal: rules are
# generated for a whole lesson before its conversion lands, and a gate that goes red on
# work in progress is a gate people learn to ignore (the gate 37 precedent).
# SCOPE, and it is the whole correctness of this gate: only pages that LINK book.css.
# Measured first - tutor, newproject, timer, index and going_deeper each carry their own
# <style> block and 194 class attributes between them (§25.6a: the tool pages are not
# chapters). Scoping to `site` failed on all five of them, correctly reporting classes
# that were never book.css's business. Keying on the <link> is self-maintaining: a page
# enters this gate the moment it is converted, and nothing has to be remembered.
bad = []
# S126: SCOPE IS A <link> ELEMENT, NOT A SUBSTRING. Both §27 and §27.12 keyed scope on
# `'css/book.css' in src`, so ANY page that merely MENTIONS the path -- in prose, in a
# comment, in a code sample -- silently entered the gate. Measured, not hypothesised: a
# comment added to going_deeper.html's own <style> block reading "...reach through
# css/book.css..." pulled that page into §27 and reported 11 of its own classes as
# unresolved. §24.8 -- the population the gate scans was never the population it names.
# The href is RELATIVE-TO-THE-PAGE (§27.10, the book does not name its own host), so the
# lessons in lessons/ link "../css/book.css" and the root pages link "css/book.css". A
# predicate that demanded the bare path matched ZERO lessons and §27 then PASSED on an
# empty scope -- caught only because gate 44 carries a COVERAGE arm and §27 did not.
# S117/S118 for the third time: a gate that scans zero pages passes.
def _links(src, sheet):
    return re.search(r'<link[^>]+href="(?:\.\./)*' + re.escape(sheet) + r'"', src) is not None


_used = collections.Counter()
_scope = [f for f in site if _links(open(f, encoding='utf-8').read(), 'css/book.css')]
for f in _scope:
    for m in re.finditer(r'\sclass="([^"]*)"', open(f, encoding='utf-8').read()):
        for c in m.group(1).split():
            _used[c] += 1
_css = LI.load_css()
if len(_scope) < 16:
    bad.append(f'scanned only {len(_scope)} page(s) \u2014 the scope expression is '
               f'broken; all sixteen lessons link the stylesheet (\u00a727)')
if _used and not _css:
    bad.append(f'{sum(_used.values())} class attribute(s) in use and css/book.css is absent '
               f'or empty - every one of them resolves to nothing')
for c in sorted(_used):
    if c not in _css:
        bad.append(f'class "{c}" is used {_used[c]}x and has NO rule in css/book.css - the '
                   f'elements carrying it are invisible to every CSS-reading gate')
gate('\u00a727  every class in use resolves to a rule in css/book.css', bad)
_unused = sorted(set(_css) - set(_used))
if _unused:
    print(f'         note: {len(_unused)} generated rule(s) not yet used by any page '
          f'(staged for a lesson not converted yet, not a failure)')

# ---- GATE 42 (§27.10): no page names its own domain.
# THIS GATE EXISTS BECAUSE THE OTHERS CANNOT SEE THE DEFECT. §21's resolver deliberately
# understands the absolute prefix, so reverting one image src to
# https://weymuth.github.io/zumo/... resolves to the same file and passes every one of the
# 41 gates that preceded this one -- measured by seeding exactly that, not assumed. A broken
# RELATIVE path is caught by §21; a reverted ABSOLUTE one was invisible.
# Scope is deliberately wider than href/src: the Brain Check gear swap assigns img.src from a
# STRING LITERAL inside a <script>, and 18 of those hid from the S105 sweep for exactly that
# reason. This matches the domain anywhere in the file, in any syntax, so a third reference
# shape cannot open the hole again.
# Off-site hosts are NOT in scope. Domain-agnostic means the book does not name ITS OWN host.
_OWN = re.compile(r'https?://weymuth\.github\.io')
bad = []
for f in site:
    if not os.path.exists(f):
        continue
    src = open(f, encoding='utf-8', errors='replace').read()
    for m in _OWN.finditer(src):
        ln = src.count('\n', 0, m.start()) + 1
        ctx = src[max(0, m.start() - 30):m.start() + 70].replace('\n', ' ')
        bad.append(f'{f} line {ln}: names its own domain -> ...{ctx}...')
gate('\u00a727.10 no page names its own domain (relative refs only)', bad)

# ---- GATE 43 (§27.11): the stylesheet itself is baselined.
# THE MIGRATION MOVED EVERY DECLARATION INTO ONE FILE AND LEFT IT UNGUARDED. Before S105 a
# declaration lived in 25,036 places in the lessons; now it lives once, in css/book.css, and
# NOTHING validated that file. build_css --check cannot: it rebuilds from the lessons read
# through expand_classes, which reads css/book.css -- damage the stylesheet and the expansion
# is damaged identically, so the regenerated output matches the damaged file and --check says
# "current", exit 0. Measured, not argued: deleting one `color: white;` left all 42 gates green
# and --check clean, while the lesson strip's links lost their colour in all sixteen lessons.
# An instrument that reads its own output as input cannot see its input change (§24.8).
#
# So this gate holds the ONE thing not derived from the file it is checking: a baseline.
# It moves DELIBERATELY, the way §21's did (218 -> 223) -- §26's repaint will move it, and
# that is the point. A baseline that never moves is a baseline nobody is checking.
import hashlib as _hl
CSS_RULES, CSS_DECLS, CSS_DIGEST = 574, 2033, 'ce43da626bdf82b1'
#   S138 move: digest ONLY. Rules and declarations UNCHANGED at 574/2,033 - zero born,
#   zero died, and the class SET is byte-identical (checked both directions). What moved
#   is usage RANK: GRAPHIC 4.7 landing twice in L04 took .img-d-block-3 4->5 and
#   .p-c-888 2->3, the retired IMAGE 4.5 placeholder took .div-2196f3 10->9, and the new
#   Figures row took tr 180->181. Frequency order is the file's sort key, so the rules
#   reshuffled without a single selector changing. strip_inline --verify: 0 dead names.
#   S134 move: digest ONLY. Rules and declarations UNCHANGED at 574/2,033 - zero born,
#   zero died, zero ALTERED, diffed by selector. The whole sheet delta is FOUR lines: the
#   header's covered-attribute count and one rule's usage comment, .div-fs-105em ×792 ->
#   ×795. Those three uses are L15's three inline <b> KEY TERM heads becoming the head div
#   every other body block already had (§2.3). Acceptance test is the RESOLVED styling, not
#   the rule count (S133 rule 24): all 22,142 pre-existing resolved declaration strings are
#   byte-identical across the restore/regenerate/apply cycle in all sixteen lessons, and the
#   only difference is +3 of that one string in L15. §27.15b did not fire and could not -
#   nothing left a class, so no survivor could be renamed.
#   S133 fourth move: digest ONLY, 574/2,033 unchanged, zero born, zero died. TWO rules
#   ALTERED - .ul-ls-none-2 and .ul-ls-none-3 swapped declarations. THE LESSONS ARE
#   BYTE-IDENTICAL either side of this move; only the stylesheet moved. Cause: build_css
#   expands through the CURRENT css/book.css, so its class-name assignment is PATH
#   DEPENDENT - the same lesson tree has more than one fixed point, and which one you land
#   on depends on the sheet you started from. Recorded rather than fought: the regenerated
#   sheet is by definition what the lessons generate (S27.13), so it is the correct one.
#   S133 third move: digest ONLY. Rules and declarations UNCHANGED at 574/2,033 - zero born,
#   zero died, zero altered. Five S1 figure placeholders joined .div-2196f3 (3 uses -> 8),
#   which moved that rule's usage RANK and its count comment. Nothing was re-classed.
#   S133 second move: 577/2,039 -> 574/2,033. THE BACK-TO-TOP WRAPPER IS ONE SPELLING.
#   All 237 links take <p class="p-ta-right">. Exactly three rules DIE - .div-mt-20px,
#   .div-mt-25px, .p-mt-10px-2 - carrying two declarations each, and -6 IS those three.
#   Zero born, zero altered, so §27.15b's rename trap does not fire: all three were used
#   ONLY by back-to-top links, verified by grep before deletion, 0 other consumers.
#   S133: digest ONLY. Rules and declarations UNCHANGED at 577/2,039 - zero born, zero died,
#   zero altered. The 20 changed lines are two RANK relocations and their count comments:
#   .p-ta-right 150 -> 178 uses and .p-mt-22px 44 -> 16, because L15/L16's 28 back-to-top
#   wrappers moved from one to the other. S121's shape.
#   S132 second push: 598/2,123 -> 577/2,039, THE REVEAL BOX (§27.15f). 23 rules die - twelve
#   <details> spellings, nine <summary> spellings, and the two callout classes L11's ex-ANSWER
#   blocks vacated - against two born, one of them `.div-dee2e6-6`, a <div> that had been
#   sharing a name with a reveal. Surviving spellings changed declarations, so §27.15b's trap
#   fired and was paid by restore -> regenerate -> apply. THE ACCEPTANCE TEST IS NOT THE
#   RULE COUNT: every element in the book that is NOT a reveal resolves byte-identically
#   across the cycle, all 22,137 of them, in all sixteen lessons.
#   S132: 604/2,141 -> 598/2,123, THE GLOSSARY CONVERSION. Six rules died with the five
#   retired schemas: .div-9b59b6 (L04's bare entry), .dl/.dt/.dd (L13/L14), .td-ddd-12 and
#   .callout-2e86ab-bg-fff (L12's blue-on-white card). Nothing was ADDED - the canon card
#   reuses classes the book already had, which is what made it the canon.
#   THE RENAME TRAP FIRED AND WAS PAID (§27.15b, and build_css v1.2's own warning): naming
#   is frequency-ranked, so 12 SURVIVING spellings changed declarations - .th-17496a-2 and
#   -3 swapped grounds outright. A name that still resolves repaints the page with every
#   gate green, so the sequence was restore -> regenerate -> apply --include-held, and the
#   acceptance test is not the rule count: all 22,933 RESOLVED declaration strings are
#   byte-identical across the cycle in all sixteen lessons. Zero pixels moved.
#   S126b: 624/2,282 -> 604/2,141, §27.15e. The dark code block graduates and the -20/-141
#   reconciles exactly: 23 rules DIE carrying 148 declarations, 3 are BORN carrying 3, and
#   ONE is altered, gaining 4. -148 + 3 + 4 = -141. The altered rule is a RENUMBER, not a
#   meaning change: .div-bg-1e1e1e-2 took the name .div-bg-1e1e1e after the original holder
#   died in the unwrap, and the survivors were moved onto it by matching IDENTICAL
#   declarations, never by name arithmetic. §27.15b FIRED FOR REAL on the first attempt --
#   176 <pre> joined .p-m-0's 120 users, <pre> became the dominant tag, the rule renamed to
#   .pre-m-0 and 119 <p> plus 1 <ul> went dead. Per §27.15b the tree was REVERTED to the
#   pushed clone and re-derived with the survivor rename in its correct slot, not patched
#   forward. PROOF NOTHING ELSE MOVED: every lesson expanded against its own stylesheet
#   before and after, and every changed line is a <pre>, a removed wrapper <div>, or
#   whitespace -- ZERO others across all sixteen.
#   S126: 627/2,297 -> 624/2,282. §27.15a says there is NO exception list, and five inline
#   <code> elements in L03 were still carrying a class - the last five in the book. They
#   were invisible to S124's strip because that sweep enumerated the class names it knew
#   (.code-inline-bg-e8e8e8*, .code-ff-uimonosp*) and these three are spelled differently:
#   §24.8 again. Two of them, .code-inline-bg-f5c6cb and -f5c6c0, are the SAME pink one
#   digit apart on the same construct - a typo, not two colours. Diffed by SELECTOR against
#   the pushed clone: exactly THREE gone, ZERO born, ZERO surviving rules altered, so no
#   class RENAME and §27.15b's trap does not fire (all three were code-only: x2, x2, x1).
#   The -15 declarations IS those three rules at five declarations each. Control-run after
#   the move: deleting one `color: white;` still FAILS this gate.
#   S124: 636/2,332 -> 627/2,297, and the -9 is fully accounted for. TEN rules die - the six
#   .code-inline-bg-e8e8e8 variants, the three .code-ff-uimonosp ones and .code-c-white - and
#   ONE is born, .span-ff-uimonosp, which is the same declarations under a name derived from
#   the tag mix that survived the strip. 10 - 1 = 9. The six pill rules disagreed about the
#   construct they encoded (three font sizes, a stray color, a white-space), which is why the
#   declaration count falls further than the rule count.
#   S121: digest ONLY, 643/2,357 UNCHANGED - zero rules born, zero died, zero altered.
#   S113's shape, the fourth time. Cause: §3.1a seated 15 next-lesson links, which added
#   15 uses of .link-c-2e86ab (398->413) and 15 of .p-mt-22px (29->44). build_css orders
#   rules by usage RANK, so .p-mt-22px MOVED position in the emitted file and the two
#   count comments changed. Diffed by SELECTOR against the pushed clone: 20 changed lines,
#   all of them a comment count or that one relocation. Control-run after the move:
#   deleting one `color: white;` still FAILS this gate.
#   S116: 645 -> 644, 2,365 -> 2,362. L11's conversion consumed the Skills Checklist,
#   whose pale-green box was that rule's last use. Diffed by SELECTOR against the pushed
#   clone, never by the comment header: exactly one selector gone (.div-bg-eafaf1, 3
#   declarations), ZERO born, ZERO surviving rules altered - so no class RENAME this time,
#   unlike S115. The -3 declarations IS that rule. Control-run after the move: deleting one
#   `color: white;` still FAILS this gate.
#   S115: 646 -> 645, 2,367 -> 2,365. L10's conversion removed both <h4> ancestors
#   (Check Your Understanding, Rate Yourself), so one h4 rule lost its last use and
#   build_css renumbered the survivor. Controlled by SELECTOR, not by the comment
#   header (which carries usage counts and makes every rule look changed): exactly one
#   selector gone (.h4-c-4d535f-5, 2 declarations), zero born, zero surviving rules
#   altered. The -2 declarations IS that rule. Control-run after the move: deleting one
#   `color: white;` still FAILS this gate.
#   S113 third move: digest ONLY, 646/2,367 unchanged again. L03 IMAGE 3.14 was wired in
#   from a supplied photo, so .div-c-666 went 45->46, .div-m-20px0 39->40 and .img-h-auto
#   25->26, and two rules changed POSITION in the usage-ordered output. Diffed in full
#   against the pushed clone before the baseline moved. This is the FOURTH baseline this
#   session (family map, §21 coverage, and this digest twice) and every one moved for a
#   content change that was proven first - a baseline moved without its diff is a spent gate.
#   S113 second move: digest ONLY again, and for the same reason. 646/2,367 unchanged.
#   L07's [IMAGE 7.13] and L14's [IMAGE 14.2] placeholders were retired, so .div-2196f3
#   went 9->8 uses and .div-ccc 2->1, and both rules changed POSITION in the usage-ordered
#   output. Diffed in full against the pushed clone before the baseline moved: those two
#   counts and those two positions are the whole delta. NOTE: .div-ccc is now down to ONE
#   use book-wide - it is the image-placeholder box, and when the last placeholder retires
#   the rule dies on its own. That is expected, not a defect.
#   S113: digest ONLY. 646 rules and 2,367 declarations are UNCHANGED - not one rule was
#   added, removed or altered. L03's [IMAGE 3.4] placeholder became a WHAT YOU SHOULD SEE
#   callout, so five usage counts moved (span 831->832, div 728->729, pre 279->280,
#   .p-mb-0 337->338, .callout-17a2b8-bg-d1ecf1 30->31, .div-2196f3 10->9) and three rules
#   changed POSITION, because build_css orders by usage count. Diffed in full before the
#   baseline was touched: those counts and those positions are the whole delta.
#   S111c: THE REPAINT. The §6.5 band system moved to the eight-band palette ruled in
#   ZUMO_S111_VISUAL_RULING.md - 2,460 elements across the sixteen lessons plus
#   going_deeper, all 134 gradients flattened per v8.87's absolute ban, and the 87
#   challenge-card headers to the §9 band. Callouts were NOT touched: 933 callout style
#   attributes were protected BY DECLARATION STRING, because four of the five old group
#   hexes are also used by nine callout rules and a hex-level substitution would have
#   repainted them with no gate noticing. Rule COUNT is unchanged at 650 - a repaint moves
#   values, not structure - and the digest is the whole finding.

#   S111b: the ICON LEGEND is retired from the ten lessons that carried one (L11-L16
#   never had it, which is why the construct was already inconsistent). Six rules lost
#   their last consumer - div-2e86ab-7, div-c-495057, div-d-flex-3, div-dee2e6-6,
#   h3-c-1a5276, h3-c-2e86ab-2 - carrying 23 declarations. The other TWO of the 25 are
#   the S105 hazard and were checked rather than assumed: retiring six rules re-ranked
#   the frequency order, so div-dee2e6-2/-3/-4 and div-2e86ab-6 kept their spelling and
#   changed their meaning (6->5, 5->4, 5->3, 4->6). Verified SAFE by a different method -
#   expanding every class back to declarations and diffing per element - where the ten
#   lessons lose exactly 3 styled elements each, L02 loses 4 and gains 121 (its code
#   block), L11-L16 are untouched, and ZERO elements gained a styling they did not have.
#   656 -> 650, 2,396 -> 2,371.
#   S112: 650 -> 646, 2,371 -> 2,367. NOT a repaint. Eight values were spelled in BOTH cases
#   ('#4CAF50' and '#4caf50'), which CSS reads as one colour and every raw-string comparison
#   in this file reads as two - the S111 case trap, found by color_index.py v1.0. Lowercasing
#   25 occurrences in the lesson source merged four duplicate rule PAIRS, and the survivors
#   absorbed exactly one element each (2576->2577, 698->699, 49->50, 8->9), which is the
#   proof the drop is the merge and nothing else. Four class names also SHORTENED
#   (.tok-569cd6-c-569cd6 -> .tok-569cd6) because the collision that lengthened them is gone;
#   the old names no longer resolve, so a stale reference fails gate 41 rather than hiding.
#   Cycle was restore -> edit -> build_css -> apply --include-held (Bible §27.8b).
#   S111: [IMAGE 2.5] retired. L02's completed program became a LIVE CODE BLOCK in the
#   Quick Reference instead of a screenshot, so the dashed placeholder box lost its last
#   consumer and `.div-3498db-2` died - 7 declarations, which is exactly the drop.
#   657 -> 656, 2,403 -> 2,396. A drop of one rule and seven declarations is the shape to
#   expect when a single-consumer placeholder retires; anything else means a class was
#   re-spelled and fifteen untouched lessons moved with it (the S105 hazard).
#   S109: six INSIGHT blocks carrying the canonical magnifier wore five non-canon paints
#   (L02 x2, L03 x1, L07 x3). Repainted to #e9f7f5/#2da99d. THREE rules died - #dce4f2,
#   #fff3e0 and #d5e8d4 lost their last consumer - while #f0f7f0 and #d1ecf1 SURVIVED
#   because they are other families' canon. 660 -> 657, 2,418 -> 2,403. A drop of exactly
#   three is the shape to expect; five would have meant the sweep hit the wrong blocks.
#   S106: digest only. Wiring ONE figure into L02 changed the frequency ranking, which
#   reorders rules and their usage comments. Same 664 rules, same 2,434 declarations.
#   S108: +2 rules / +11 declarations, the F1 eyebrow (7) and headline (4) spans, from the
#   L03 pilot alone. The other fifteen lessons were restored, regenerated against and
#   re-applied in the same cycle and came back BYTE-IDENTICAL — measured, md5, all 15 —
#   so the frequency-rank rename that cost 46 names at S105 did not fire here.
#   ROLLED OUT SAME SESSION: the other fifteen moved the DIGEST ONLY - still 666 rules and
#   2,445 declarations, because L03 had already created both F1 rules and the fifteen simply
#   raised their usage counts. Frequency ranking reorders the emitted comments; nothing
#   renamed. That is the S105 hazard measured and absent, not assumed.
#   Then the bonus banner joined F1 and a rule DIED: `font-size: 1.15em; font-weight: bold;`
#   was the old cap's inner style, and the bonus banner was its LAST consumer once the 222
#   section caps had moved. 666 -> 665 rules, 2,445 -> 2,443 declarations. A dropped name is
#   the one kind of build_css change gate 41 can see on its own; this one is accounted for.
#   Then type treatment E: .page swapped the Windows-only Segoe stack for Inter, line-height
#   1.7 -> 1.65 and #333 -> #1d1d1f. Same 665 rules, same 2,443 declarations, same NAME -
#   digest only. The rule kept `.page` because its declarations still prove the role.
#   Then DJ's panel ruling A: the section content panel had TWO forms, 18px/no-background in
#   L01-L09 and 20px-25px/white in L10-L16, split at the same seam in all five colour groups
#   and invisible to every gate. 104 panels moved to the 18px form and FIVE duplicate rules
#   collapsed - one per colour where there had been two. 665 -> 660, 2,443 -> 2,418. A drop
#   of exactly five is the shape to expect when a variant is retired; anything else would
#   mean something moved that was not asked to.
bad = []
if os.path.exists('css/book.css'):
    _css = open('css/book.css', encoding='utf-8').read()
    # S123: SCOPED TO THE GENERATED BLOCK. §27.15's semantic layer is hand-authored and
    # guarded by gate 54; counting it here would make this baseline move every time a rule
    # GRADUATES, which is the one operation the architecture is designed to make cheap.
    # It also silently mixed populations: _r counts class rules only, _d counted every
    # declaration, so one added element rule read as 'a rule gained or lost a property' —
    # the precisely wrong diagnosis, printed in this gate's own words.
    _mark = '/* ===== GENERATED BLOCK'
    _body = _css.split(_mark, 1)[1] if _mark in _css else _css[_css.index('*/') + 2:]
    _r = len(re.findall(r'^\.[A-Za-z0-9_-]+ \{', _body, re.M))
    _d = len(re.findall(r'^  [a-z-]+: ', _body, re.M))
    _g = _hl.sha256(_body.encode()).hexdigest()[:16]
    if _r != CSS_RULES:
        bad.append(f'css/book.css has {_r} rules, baseline {CSS_RULES}')
    if _d != CSS_DECLS:
        bad.append(f'css/book.css has {_d} declarations, baseline {CSS_DECLS} — a rule '
                   f'gained or lost a property and no other instrument can see it')
    if _g != CSS_DIGEST:
        bad.append(f'css/book.css digest {_g}, baseline {CSS_DIGEST} — content changed; if '
                   f'deliberate, re-run build_css.py and move the baseline in this file')
else:
    bad.append('css/book.css is missing')
#   S109: the LABEL was hard-coded and had gone stale — it still read 664/2,434 while the
#   constants above tested 660/2,418, so the gate was testing the right numbers under the
#   wrong name. It is now DERIVED from CSS_RULES/CSS_DECLS: move the baseline and the name
#   moves with it. A label is not a finding (§24.6c), but a stale one teaches a wrong number.
gate(f'\u00a727.11 the stylesheet matches its baseline '
     f'({CSS_RULES} rules / {CSS_DECLS:,} declarations)', bad)


# ---- GATE 44 (§27.12): a converted page carries NO inline style attribute.
# MEASURED, NOT ASSUMED (S106 CONTROL A): pasting one <p style="color: #ff00aa;
# font-size: 13px;"> into Lesson 05 left ALL 43 PRECEDING GATES GREEN. The migration's
# whole premise -- that a declaration lives once, in css/book.css -- has, until now, been
# guarded by nothing at all. Every future hand-edit, every pasted block from an old
# lesson, every AI-suggested snippet re-opens the hole silently, and the element renders
# CORRECTLY while doing it, so nobody looks.
# SCOPE is keyed on the <link>, the same self-maintaining rule as gate 41 and for the same
# reason (§25.6a): going_deeper (7), index (1), newproject (2) and tutor (7) carry their
# own <style> blocks and their own inline attributes, and none of that is book.css's
# business. A page enters this gate the moment it is converted; nothing has to be
# remembered.
# S126 EXTENSION, DJ RULING. Scope was "links css/book.css". §27.15c put
# going_deeper.html on css/semantic.css, which made it a converted page this gate could
# not see -- so it sat PARTLY converted, with seven inline style attributes, and gate 44
# passed. Same shape as §27.15c shipping ungated: a new delivery path is a new unguarded
# path. Scope now DERIVES from either stylesheet, so a page joining the layer by either
# pipe enters automatically and nothing has to be remembered.
# index.html links NEITHER -- it is fully self-contained -- and is therefore held by NAME
# (§25.2a, named sets over counts), because DJ ruled its one inline style out and a fix
# with no gate is an unguarded fix. newproject.html and tutor/tutor.html stay OUT by
# §25.6a: they are tool pages and their own inline styles are nobody else's business.
_SHEETS = ('css/book.css', 'css/semantic.css')
_ALSO_HELD = ('index.html',)
_conv = []
for f in site:
    src = open(f, encoding='utf-8').read()
    hit = [h for h in _SHEETS if _links(src, h)]
    if hit:
        _conv.append((f, 'links ' + hit[0]))
    elif f in _ALSO_HELD:
        _conv.append((f, 'is held by name (\u00a725.2a)'))
bad = []
# COVERAGE ARM (S117/S118): a gate that scans zero pages passes.
if len(_conv) < 1 + len(_ALSO_HELD):
    bad.append(f'scanned only {len(_conv)} page(s) \u2014 the scope expression is broken (\u00a727.12)')
for f, why in _conv:
    src = open(f, encoding='utf-8').read()
    for m in re.finditer(r'\sstyle="([^"]*)"', src):
        ln = src.count('\n', 0, m.start()) + 1
        bad.append(f'{f} line {ln}: inline style="{m.group(1)[:60]}" \u2014 this page {why}, '
                   f'so its styling belongs in a rule (\u00a727.12)')
gate('\u00a727.12 no converted page carries an inline style attribute', bad)

# ---- GATE 45 (§27.13): css/book.css regenerates byte-identically from the lessons.
# THIS IS THE GUARD ON HAZARD (a), AND IT IS THE ONE THAT SURVIVES A MOVED BASELINE.
# §27.8b's sequence is restore -> regenerate -> apply. Stop after step 2 and the lessons
# still carry the OLD names against a stylesheet that renamed 57 of them, 46 of which KEPT
# THEIR SPELLING -- so gate 41 sees only the ones that vanished and the page silently
# repaints. Gate 43 catches the regeneration by digest, but §26's repaint REQUIRES moving
# that baseline deliberately; the moment it moves, gate 43 is spent and hazard (a) is
# unguarded again. This gate is not spent by a repaint, because it re-derives rather than
# remembers.
# THE TWO GATES ARE COMPLEMENTARY, MEASURED IN BOTH DIRECTIONS (S106):
#   CONTROL B  deleting one `color: white;` from css/book.css -> gate 43 FAILS, this gate
#              is BLIND (build_css reads the stylesheet through expand_classes, so the
#              damage propagates into the comparison — §24.8, the S105 finding).
#   CONTROL C  retyping ONE element from a resolvable class to a DIFFERENT resolvable
#              class -> all 43 preceding gates GREEN, this gate FAILS.
#   CONTROL D  regenerating with a changed SOURCES and skipping the re-strip -> this gate
#              FAILS (with gate 41, which caught 20 dead names in that particular shape).
# Neither subsumes the other. Keep both.
# WHY `strip_inline --verify` IS NOT HERE, so it is not re-offered: it computes gate 41's
# assertion a second way. Across all four controls it never fired independently of gate 41.
# An assert that cannot fail is not evidence (§24).
# A RED HERE DURING A REPAINT IS CORRECT: mid-sequence the tree really is inconsistent.
# It goes green when step 3 lands, and that is the signal the repaint is complete.
import build_css as BC            # import the definition, do not re-implement it (S83)
bad = []
try:
    _text, _rows, _chosen = BC.build()
    _cur = open('css/book.css', encoding='utf-8').read() if os.path.exists('css/book.css') else None
    if _cur is None:
        bad.append('css/book.css is missing but the lessons generate ' + str(len(_rows)) + ' rules')
    elif _cur != _text:
        bad.append(f'css/book.css does NOT match what the lessons generate '
                   f'({len(_rows)} rules regenerated) — either a lesson carries styling the '
                   f'stylesheet does not know about, or the stylesheet was regenerated '
                   f'without re-running strip_inline --apply (§27.8b: restore -> regenerate '
                   f'-> apply). Run build_css.py --check to see it directly.')
except Exception as e:                       # a crash here must not take the suite down
    bad.append(f'could not regenerate: {type(e).__name__}: {e}')
gate('\u00a727.13 css/book.css regenerates byte-identically from the lessons', bad)

# ---- WHERE THIS BLOCK SITS IS PART OF THE GATE. It was first appended to the END of the
# ---- file, BELOW the summary and its sys.exit(1). On a clean tree it ran and printed PASS
# ---- after 'ALL GATES PASS', so its verdict was outside the summary; on the control run it
# ---- never ran at all, because sys.exit fired first. A gate that only executes when every
# ---- other gate passes cannot catch anything in a failing suite (S24.8: the instrument
# ---- could not distinguish the two answers). Caught by the control, not by reading.

# ---- GATE 46 (§27.14): every LINK and every ID resolves.
# ---- NEW S112. The book carries 1,237 <a href> and 705 ids across twenty pages and NOTHING
# ---- checked them. Two gates come close and neither covers this: `index.html relative links
# ---- resolve` walks one page, and `going_deeper links canonical and relative` checks the SHAPE
# ---- of a href, not whether its target exists. A dead in-page anchor is the most invisible
# ---- defect the book can have -- the link renders, the cursor changes, the page simply does
# ---- not move -- and it is created by exactly the work this session did most of: renaming an
# ---- id, deleting a block, retiring a figure row.
# ----
# ---- PARSER, not regex (§24.10): ids and hrefs come from HTMLParser, because an `id=` inside
# ---- a code block or an escaped attribute is not an id and a substring search cannot tell.
# ----
# ---- ONE FALSE FINDING IS ALREADY RECORDED HERE, per §24.6c. The first version of this check
# ---- reported 223 broken links. Every one was a Maker URL of the form
# ---- `../newproject.html?lesson=1&kind=c01` -- the query string was being treated as part of
# ---- the filename. The book was right and the instrument was wrong, and the number was large
# ---- enough to look like a real finding. A query string is stripped before resolution.
bad = []
import html.parser as _hp


class _IdHref(_hp.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.hrefs = [], []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get('id') is not None:
            self.ids.append(d['id'])
        if tag == 'a' and d.get('href') is not None:
            self.hrefs.append(d['href'])


_PAGES = sorted(glob.glob('lessons/Lesson_*.html')) + \
         [p for p in ('index.html', 'going_deeper.html', 'newproject.html', 'timer.html')
          if os.path.exists(p)]
_ids, _hrefs = {}, {}
for _f in _PAGES:
    _p = _IdHref()
    _p.feed(open(_f, encoding='utf-8', errors='replace').read())
    _ids[_f], _hrefs[_f] = _p.ids, _p.hrefs
_idset = {f: set(v) for f, v in _ids.items()}

for _f, _v in _ids.items():
    for _k, _n in collections.Counter(_v).items():
        if _n > 1:
            bad.append(f'{_f}: id "{_k}" appears {_n} times — a duplicate id makes every '
                       f'link to it land on whichever the browser saw first')
for _f, _v in _hrefs.items():
    for _h in _v:
        if _h.startswith('#'):
            if _h[1:] not in _idset[_f]:
                bad.append(f'{_f}: href "{_h}" — no such id on this page')
        elif _h.startswith(('http', 'mailto:', 'javascript:')) or not _h:
            continue
        else:
            _path, _, _frag = _h.partition('#')
            _tgt = _path.partition('?')[0]          # the query string is NOT the filename
            _cand = os.path.normpath(os.path.join(os.path.dirname(_f), _tgt)) if _tgt else _f
            if not os.path.exists(_cand):
                bad.append(f'{_f}: href "{_h}" — no file at {_cand}')
            elif _frag:
                if _cand not in _idset:
                    _q = _IdHref()
                    _q.feed(open(_cand, encoding='utf-8', errors='replace').read())
                    _idset[_cand] = set(_q.ids)
                if _frag not in _idset[_cand]:
                    bad.append(f'{_f}: href "{_h}" — no id "{_frag}" in {_cand}')
# COVERAGE: a gate whose population silently empties is an ungated rule (S83).
_nlinks = sum(len(v) for v in _hrefs.values())
if len(_PAGES) < 17 or _nlinks < 1000:
    bad.append(f'COVERAGE: {len(_PAGES)} pages / {_nlinks} links parsed — expected 17+ and 1,000+')
gate(f'\u00a727.14 every link and id resolves ({_nlinks:,} links, '
     f'{sum(len(v) for v in _ids.values()):,} ids, {len(_PAGES)} pages)', bad)


# ---- §24.14 (S112): the callout family map assigns every block.
# WHY A GATE. `build_family_map.py` reported 1047/1048 for a whole session and the suite
# stayed green, because the generator was never wired in. The S111 repaint moved one hex and
# a block fell out of a COLOUR-keyed fallback; nothing could say so.
# WHERE THIS SITS IS PART OF THE GATE (S112): above the summary and its sys.exit, so it runs
# on a FAILING tree too. Appended below them it would print PASS after ALL GATES PASS and
# never execute at all when another gate failed.
# It shells out deliberately - the generator is a script, and re-implementing its matcher
# here would be the third regex §24 forbids. Both the exit code AND the parsed line are
# checked: a crashed generator must not read as a silent pass.
bad = []
_r = subprocess.run([sys.executable, 'build_family_map.py'], capture_output=True, text=True)
if _r.returncode != 0:
    bad.append(f'build_family_map.py exited {_r.returncode} - the map did not build')
else:
    _m = re.search(r'assigned (\d+) / (\d+)\s+families (\d+)', _r.stdout)
    if not _m:
        bad.append('build_family_map.py printed no "assigned N / M" line - output shape changed')
    else:
        _a, _t, _fam = (int(x) for x in _m.groups())
        if _a != _t:
            bad.append(f'{_t - _a} callout block(s) unassigned ({_a}/{_t})')
            for _ln in _r.stdout.splitlines():
                if _ln.startswith('   L'):
                    bad.append(_ln.strip())
        if _t < 1000:
            bad.append(f'COVERAGE: only {_t} blocks parsed - expected 1,000+')
        if _fam < 25:
            bad.append(f'COVERAGE: only {_fam} families - expected 25+')
gate('\u00a724.14 every callout block resolves to a family', bad)


# ---- §3.1a: the end-of-lesson forward link — DJ ruling S121.
# The book's forward pointer was prose in 13 lessons, absent in 2, and clickable in ZERO:
# measured at S121, not one <a href> to a lesson file existed anywhere in any lesson tail.
# A bolded "Lesson 7: Code Organization" that does not click is a dead affordance.
#
# The block is GENERATED by next_pointer.py from the lesson strip's own titles, so this
# gate re-derives rather than remembering (§27.13's shape). It asserts four things a
# reader cannot check by eye: the block exists exactly once, it points at the RIGHT
# successor, it sits ABOVE the §5b footer rather than below it, and L16 carries none.
#
# The seat matters as much as the link. The forward-pointer PROSE sits at 84% of the
# page, above Engineer's Log — so a link there would route students past the entry that
# feeds their TDP. This block is the last element before the footer, so the door only
# opens once the exit work is behind them.
bad = []
_seen = 0
for _n in range(1, 17):
    _f = f'lessons/Lesson_{_n:02d}.html'
    _s = open(_f, encoding='utf-8').read()
    _hits = list(re.finditer(r'<p class="p-mt-22px" id="next-lesson">'
                             r'<a href="Lesson_(\d+)\.html"', _s))
    if _n == 16:
        if _hits:
            bad.append(f'{L(_f)}: carries a next-lesson block; L16 ends the book (§3.1)')
        continue
    _seen += 1
    if len(_hits) != 1:
        bad.append(f'{L(_f)}: {len(_hits)} next-lesson block(s), expected exactly 1 (§3.1a)')
        continue
    _tgt = int(_hits[0].group(1))
    if _tgt != _n + 1:
        bad.append(f'{L(_f)}: next-lesson block points at Lesson {_tgt}, expected {_n + 1}')
    _foot = _s.find('<p class="p-c-666">')
    if _foot < 0 or _hits[0].start() > _foot:
        bad.append(f'{L(_f)}: next-lesson block is not seated above the §5b footer')
if _seen != 15:
    bad.append(f'COVERAGE: {_seen} lessons scanned, expected 15')
gate('\u00a73.1a every lesson 01-15 ends with a working link to the next lesson', bad)


# ---- §3.1b: the What's Next? section — DJ ruling S122.
# Sixteen lessons ended four different ways: seven carried a "What's Next" heading in
# THREE spellings, five carried a bare <p><strong>Next:</strong>, one stacked both, and
# four just stopped. The link block below is uniform because it is generated; everything
# above it was authored per lesson and drifted, which is §6.8a's shape one construct over.
#
# The ruled shape is a FLOOR, not a ceiling (§25.8's precedent): heading, at least one
# paragraph naming the next lesson in bold, at least one list. A lesson carrying more —
# L03's and L05's forward-preview callouts, L14's competition send-off — keeps it. Nothing
# was deleted to reach conformance; the five Next: paragraphs were MOVED inside.
#
# The title is DERIVED from the §6.5a strip and never typed. That is not decoration: L07's
# prose said "Line Following" and L08's said "Intersections and Dead Ends" while the
# generated link block on the SAME PAGE said "Line Following with P-Control" and
# "Intersections & Dead Ends". Two spellings of one title, ninety lines apart, and no
# instrument could see it because nothing compared prose against the strip.
#
# Scope note, learned three times while building this: every check here is scoped to the
# SECTION, never to the page. A page-wide search for the opener matches L12's BACKWARD
# references ("In Lesson 4 you calibrated..."), and a page-wide search for the Next:
# paragraph cannot tell "moved inside the section" from "left outside it".
bad = []
_seen = 0
_titles = {}
_strip = None
for _n in range(1, 17):
    _s = open(f'lessons/Lesson_{_n:02d}.html', encoding='utf-8').read()
    _i = _s.index('LESSON STRIP')
    _b = _s[_i:_s.index('LESSON STRIP', _i + 1)]
    if _strip is None:
        _strip = _b
    elif _b != _strip:
        bad.append(f'L{_n:02d}: lesson strip differs - titles cannot be derived (§6.5a)')
for _m in re.finditer(r'href="Lesson_(\d\d)\.html"[^>]*title="([^"]*)"', _strip or ''):
    # DJ ruling B, S123: the strip's spelling passes through UNTRANSFORMED. This line used
    # to carry .replace("'", '&rsquo;'), which made the expected opener disagree with the
    # strip by one character on the one title that has an apostrophe. Three owners carried
    # that transform - this gate, next_pointer.esc() and title_feed.to_prose() - and all
    # three moved together, because one left behind re-creates the drift on the next apply.
    _titles[int(_m.group(1))] = _m.group(2)

_HEAD = '<h3 id="whats-next" class="h3-c-6f7582">What\'s Next?</h3>'
for _n in range(1, 17):
    _f = f'lessons/Lesson_{_n:02d}.html'
    _s = open(_f, encoding='utf-8').read()
    _c = _s.count(_HEAD)
    if _n == 16:
        if _c:
            bad.append(f'{L(_f)}: carries a What\u2019s Next? section; L16 ends the book (§3.1)')
        continue
    _seen += 1
    if _c != 1:
        bad.append(f'{L(_f)}: {_c} canonical What\u2019s Next? heading(s), expected exactly 1 (§3.1b)')
        continue
    _start = _s.index(_HEAD)
    _end = _s.find('<h3', _start + len(_HEAD))
    _sec = _s[_start:_end if _end > 0 else len(_s)]
    _want = f'<p>In <strong>Lesson {_n + 1}: {_titles.get(_n + 1, "?")}</strong>,'
    if _sec.count(_want) != 1:
        bad.append(f'{L(_f)}: opener does not match the strip - expected {_want!r}')
    if '<li>' not in _sec:
        bad.append(f'{L(_f)}: What\u2019s Next? section carries no list (§3.1b floor)')
    _log = _s.find('Engineer', _end if _end > 0 else 0)
    if _end < 0 or _log < 0 or _log - _end > 400:
        bad.append(f'{L(_f)}: What\u2019s Next? is not seated immediately above Engineer\u2019s Log')
    if re.search(r'<strong>\s*Next:\s*</strong>', _s.replace(_sec, '')):
        bad.append(f'{L(_f)}: a Next: paragraph sits OUTSIDE the What\u2019s Next? section')
if _seen != 15:
    bad.append(f'COVERAGE: {_seen} lessons scanned, expected 15')
gate('\u00a73.1b every lesson 01-15 carries the canonical What\u2019s Next? section', bad)


# ---- §3.1b: the opener is UNIQUE inside its section — the hole gate 51 cannot see.
# Gate 51 asserts that the CORRECT opener string occurs once. A section holding the
# correct opener AND a second one with a stale title satisfies that count and passes.
# Measured, not supposed: injecting a duplicate opener into L07 carrying the historical
# wrong title "Line Following" left ALL 51 preceding gates green (S123 control run).
#
# This is not a synthetic shape. S122 added a duplicate opener to L05 by hand, because
# an audit reported "needs only an id" and the RESULT was read instead of the file. The
# defect this gate holds is one a session has already committed once.
#
# The target regex and the section bounds are IMPORTED, not re-implemented (S83): a
# second home for that pattern is the drift §6.8a exists to stop, one construct over.
import title_feed as TF
bad = []
_seen = 0
for _n in range(1, 17):
    _f = f'lessons/Lesson_{_n:02d}.html'
    _s = open(_f, encoding='utf-8').read()
    _span = TF.section(_s)
    if _n == 16:
        if _span is not None:
            bad.append(f'{L(_f)}: carries a What\u2019s Next? section; L16 ends the book (\u00a73.1)')
        continue
    _seen += 1
    if _span is None:
        bad.append(f'{L(_f)}: no What\u2019s Next? section to scope the opener to (\u00a73.1b)')
        continue
    _hits = list(TF.TARGET.finditer(_s, _span[0], _span[1]))
    if len(_hits) != 1:
        bad.append(f'{L(_f)}: {len(_hits)} \u00a73.1b opener(s) inside one section, expected 1')
        continue
    if int(_hits[0].group(2)) != _n + 1:
        bad.append(f'{L(_f)}: opener points at Lesson {_hits[0].group(2)}, expected {_n + 1}')
if _seen != 15:
    bad.append(f'COVERAGE: {_seen} lessons scanned, expected 15')
gate('\u00a73.1b the What\u2019s Next? opener is unique and points at the successor', bad)


# ---- §6.5a-T: the book has ONE mono stack (S123, DJ ruling B).
# Before the ruling, 422 declarations across 12 lessons carried FIVE Consolas spellings
# that consolidated into 15 stylesheet rules and resolved to THREE different fallbacks off
# Windows — and to ONE face on Windows, which is why it survived for the life of the book.
#
# WHY THIS IS NOT font_stack_sweep's JOB, AND WHY IT FIRES INDEPENDENTLY OF IT. The sweep
# rewrites a stack whose FIRST face is a named substitution risk; that is a different
# question from whether the stack equals the ruled one. `ui-monospace, monospace` has a
# safe first face and the wrong tail, so the sweep is silent on it and this gate is loud.
# Measured, not assumed — see the control run recorded in the changelog.
#
# Compared by FACE LIST rather than by raw string: the ruling is about which typeface a
# reader actually gets, and quote style is not a rendering difference. css/book.css is
# generated so its spelling is the generator's; the four tool pages are hand-authored and
# §25.6a keeps them out of the class migration, so they are the ones that can drift.
import font_stack_sweep as FS
bad = []
_want = FS.faces(FS.MONO_BOOK)
_scanned = 0
_seen_decls = 0
for _f in ['css/book.css', 'going_deeper.html', 'newproject.html', 'timer.html',
           'index.html']:
    if not os.path.exists(_f):
        bad.append(f'{_f}: missing - cannot check the mono stack')
        continue
    _scanned += 1
    _src = open(_f, encoding='utf-8').read()
    for _m in FS.DECL.finditer(_src):
        _val = _m.group(2).strip()
        if len(_val) >= 2 and _val[0] in '"\'' and _val[-1] == _val[0] and _val[0] not in _val[1:-1]:
            _val = _val[1:-1]
        _fl = FS.faces(_val)
        if 'monospace' not in [x.lower() for x in _fl]:
            continue                      # a prose stack; §6.5a-T's Inter rule, not this one
        _seen_decls += 1
        if _fl != _want:
            bad.append(f'{_f}: mono stack is {_val!r}, ruled stack is {FS.MONO_BOOK!r}')
if _scanned != 5:
    bad.append(f'COVERAGE: {_scanned} file(s) scanned, expected 5')
if _seen_decls == 0:
    bad.append('COVERAGE: zero mono declarations found - a gate that scans nothing passes')
gate('\u00a76.5a-T the book carries exactly one mono stack', bad)


# ---- §27.15: the SEMANTIC layer is preserved verbatim (S123, DJ ruling).
# The generated block names every rule after the VALUES it holds, so it can never produce
# a rule that means something — no element selector, no semantic class, no custom
# property. css/semantic.css is where meaning lives, and it is the ONE stylesheet file
# that is hand-edited on purpose.
#
# THE FAILURE MODE THIS EXISTS FOR IS SILENT, WHICH IS WHY IT NEEDS A GATE RATHER THAN A
# CONVENTION. Measured before the layer was built: an element rule pasted into
# css/book.css did not error and did not warn — the next regeneration simply DELETED it,
# and every gate stayed green. A preserved layer that is only preserved by habit is a
# layer that disappears the first time someone runs the generator.
#
# Deliberately asserts the semantic text is present IN book.css and equal to its source,
# not merely that the file exists: the defect is divergence between the two, and a check
# that only stats the file cannot see it (§24.8).
bad = []
_SEM = 'css/semantic.css'
if not os.path.exists(_SEM):
    bad.append(f'{_SEM}: missing - the semantic layer is canon (§27.15)')
else:
    _sem = open(_SEM, encoding='utf-8').read().rstrip('\n')
    _css = open('css/book.css', encoding='utf-8').read()
    if '/* ===== SEMANTIC LAYER' not in _css:
        bad.append('css/book.css: no semantic layer marker - the layer was regenerated away')
    elif _sem not in _css:
        bad.append('css/book.css: the semantic layer does not match css/semantic.css verbatim')
    if '/* ===== GENERATED BLOCK' not in _css:
        bad.append('css/book.css: no generated-block marker - the two layers cannot be told apart')
    # The layer must actually carry something the generated block CANNOT express, or it is
    # decoration. An element selector is the cheapest proof of that and the first graduate.
    if not re.search(r'(^|\n)\s*(code|pre)\s*[,{]', _sem):
        bad.append(f'{_SEM}: carries no element selector - nothing has graduated (§27.15)')
    if re.search(r'\n\.[A-Za-z0-9_-]*-[0-9a-f]{3,6}(-\d+)?\s*\{', _sem):
        bad.append(f'{_SEM}: carries a VALUE-named class - it is not ready to graduate')
gate('\u00a727.15 the semantic layer is preserved verbatim in the stylesheet', bad)


# GATE 55 (\u00a727.15a). AN ELEMENT RULE REACHES ELEMENTS NO AUTHOR EVER LISTED. That is the
# whole point of graduating one and it is the whole risk, because the population you can
# enumerate is not the population the rule reaches (\u00a724.8). Two independent contexts in this
# book are defined by NOT wanting the pill:
#   (a) inside <pre>. 15 bare <code> live there, nine in L01's #1e1e1e blocks. An unscoped
#       background paints a light pill inside every dark code block in the book.
#   (b) on a dark ground. Eight <code> sit in containers declaring color:white; an OPAQUE
#       light pill renders white text on light grey, unreadable, silently.
# (b) is held by the ruled value itself - a translucent wash inherits its ground - so this
# gate holds (a), which is the half a value cannot hold, and asserts the wash has not
# quietly been replaced by an opaque colour that would reopen (b).
#
# No pre-existing gate can see either: gate 53 checks declarations that EXIST, \u00a727.13 checks
# the GENERATED block, and gate 54 checks the layer is preserved VERBATIM - a verbatim copy
# of a wrong rule passes all three. Measured by injection before it was written: deleting the
# `pre code` reset left all 54 preceding gates green and exit 0.
bad = []
if os.path.exists(_SEM):
    _sem = open(_SEM, encoding='utf-8').read()
    _pill = re.search(r'(^|\n)code\s*\{([^}]*)\}', _sem)
    if _pill:
        _decl = _pill.group(2)
        if re.search(r'background\s*:', _decl):
            _reset = re.search(r'(^|\n)pre\s+code\s*\{([^}]*)\}', _sem)
            if not _reset:
                bad.append(f'{_SEM}: `code` sets a background and there is NO `pre code` reset - '
                           'every <code> inside a <pre> gets a pill (\u00a727.15a)')
            elif not re.search(r'background\s*:\s*(?:none|transparent)', _reset.group(2)):
                bad.append(f'{_SEM}: the `pre code` reset does not clear the background')
            _bg = re.search(r'background\s*:\s*([^;]+)', _decl).group(1).strip()
            if not _bg.startswith('rgba'):
                bad.append(f'{_SEM}: the pill ground is `{_bg}`, not a translucent wash - eight '
                           '<code> elements sit on dark grounds declaring color:white and an '
                           'opaque ground makes all eight unreadable (DJ ruling B, S124)')
    # The reset only helps if it is actually reached: assert the nested population is real,
    # so a future refactor that moves those <code> out does not leave a rule guarding nothing.
    _nested = 0
    for _f in sorted(glob.glob('lessons/Lesson_*.html')) + ['going_deeper.html']:
        if not os.path.exists(_f):
            continue
        _s = open(_f, encoding='utf-8').read()
        for _m in re.finditer(r'<pre\b.*?</pre>', _s, re.S):
            _nested += len(re.findall(r'<code\b', _m.group(0)))
    if _nested == 0:
        bad.append('no <code> inside any <pre> - the reset guards nothing; re-derive \u00a727.15a')
gate('\u00a727.15a a pill on <code> is reset inside <pre>', bad)


# ---- GATE 57 (\u00a727.15e): THE DARK CODE BLOCK IS ONE RULE, AND NOTHING RESTATES IT.
# The graduate reaches 802 <pre> elements that FOURTEEN class names used to stand for. The
# failure modes are all silent, which is why this exists in the same pass as the ruling
# (S125's rule): drop the rule and 802 blocks go transparent while every other gate stays
# green; soften the border back toward the ground and the 1.32:1 invisibility DJ caught by
# eye comes straight back, with no instrument able to see it; let a value-named class
# re-acquire a #1e1e1e ground and the construct has two spellings again, which is exactly
# the drift the no-exception-list rule was ruled to prevent.
_sem = open('css/semantic.css', encoding='utf-8').read()
bad = []
# The layer contains TWO rules whose selector ends in `pre`: the shared `code,\npre {}`
# font-family rule and this one. Select by CONTENT and assert uniqueness rather than by
# position, which would silently bind to whichever came first (it did, on the first run).
_cands = [c for c in re.findall(r'(?<!,)\npre\s*\{([^}]*)\}', _sem)
          if 'background-color' in c]
if len(_cands) != 1:
    bad.append(f'css/semantic.css holds {len(_cands)} `pre` rule(s) declaring a background; '
               f'expected exactly one (\u00a727.15e)')
_m = _cands[0] if len(_cands) == 1 else None
if _m is None:
    bad.append('css/semantic.css carries no `pre` element rule \u2014 the dark code block is '
               'ungraduated and 802 blocks resolve to nothing (\u00a727.15e)')
else:
    _d = {k.split(':')[0].strip(): k.split(':', 1)[1].strip()
          for k in _m.split(';') if ':' in k}
    for _k, _v in (('background-color', '#1e1e1e'), ('border-radius', '6px'),
                   ('padding', '15px'), ('color', '#e8e8e8')):
        if _d.get(_k) != _v:
            bad.append(f'\u00a727.15e `pre` declares {_k}: {_d.get(_k)!r}, ruled {_v!r}')
    # THE BORDER IS RULED BY CONTRAST, NOT BY SPELLING. #333 passed every gate for two
    # years and is 1.32:1 against #1e1e1e -- invisible. Assert the RATIO, so any future
    # value has to earn its place rather than merely differ.
    _b = _d.get('border', '')
    _hex = re.search(r'#([0-9a-fA-F]{6})', _b)
    if not _hex or not _b.startswith('1px solid'):
        bad.append(f'\u00a727.15e `pre` border is {_b!r}, expected `1px solid #rrggbb`')
    else:
        def _lum(h):
            out = []
            for i in (0, 2, 4):
                c = int(h[i:i + 2], 16) / 255
                out.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
            return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]
        _l1, _l2 = _lum(_hex.group(1)), _lum('1e1e1e')
        _hi, _lo = max(_l1, _l2), min(_l1, _l2)
        _ratio = (_hi + 0.05) / (_lo + 0.05)
        if _ratio < 3.0:
            bad.append(f'\u00a727.15e `pre` border #{_hex.group(1)} is {_ratio:.2f}:1 against '
                       f'the #1e1e1e ground \u2014 below the 3:1 minimum, so it is invisible')
# NO SECOND SPELLING: no generated class may re-acquire the dark ground on a <pre>.
_gen = open('css/book.css', encoding='utf-8').read()
_gi = _gen.find('GENERATED BLOCK')
for _m2 in re.finditer(r'^\.([A-Za-z0-9_-]+)\s*\{([^}]*)\}', _gen[_gi:], re.M):
    if '#1e1e1e' in _m2.group(2) and _m2.group(1).startswith(('pre-', 'code-block')):
        bad.append(f'.{_m2.group(1)} restates the dark ground on a <pre> \u2014 one construct, '
                   f'two spellings (\u00a727.15e)')
# COVERAGE ARM (S117/S118): a gate that scans zero elements passes.
_n = sum(len(re.findall(r'<pre\b', open(f, encoding='utf-8').read())) for f in files)
if _n < 700:
    bad.append(f'scanned only {_n} <pre> element(s) \u2014 the scope is broken (\u00a727.15e)')
gate('\u00a727.15e the dark code block is one rule with a visible border', bad)


# ---- GATE 56 (\u00a727.15c): A PAGE THAT CONSUMES THE SEMANTIC LAYER MUST NOT RESTATE IT.
# S125 ruled going_deeper.html onto css/semantic.css. It is the layer's FIRST DIRECT consumer:
# the sixteen lessons reach the same rules a different way, preserved verbatim at the top of
# css/book.css, which gate 54 holds. NOTHING held the direct path.
#
# MEASURED BY INJECTION BEFORE THIS GATE EXISTED, three ways, each leaving all 55 preceding
# gates green and exit 0 while the page renders wrong or the ruling is silently undone:
#   (a) delete the <link>                     -> 71 inline <code> lose the ruled pill
#   (b) restate `code { background: ... }` in the page's own <style> -> two spellings of one
#       ruled construct, which is exactly the drift \u00a727.15c ruled against
#   (c) point the href at a path that does not exist -> the pipe is decorative
# site_parity cannot see (a) or (b): it compares what the site SERVES against the repo, and a
# page that stops referencing a file still matches. font_stack_sweep cannot see them either:
# it rewrites non-compliant stacks and an ABSENT stack is not non-compliant (\u00a724.8, twice).
#
# The ORDER assertion is part of the rule, not decoration. \u00a727.15c seats the <link> ABOVE the
# page's own <style> so the page wins collisions on declarations it sets. Move it below and the
# layer starts overriding the page instead - a silent inversion no rendering check would flag.
#
# COVERAGE arm: the consumer set is NAMED (\u00a725.2a), never counted. A page joining it is a
# deliberate act and belongs in this list.
_SEM_CONSUMERS = ['going_deeper.html']
bad = []
_seen = 0
for _f in _SEM_CONSUMERS:
    if not os.path.exists(_f):
        bad.append(f'{_f}: named a semantic-layer consumer and the file is missing')
        continue
    _seen += 1
    _s = open(_f, encoding='utf-8').read()
    _lnk = re.search(r'<link[^>]+href="([^"]*semantic\.css)"[^>]*>', _s)
    if not _lnk:
        bad.append(f'{_f}: links no semantic layer - its inline <code> silently loses the '
                   'ruled pill and every other gate stays green (\u00a727.15c)')
        continue
    _href = _lnk.group(1)
    _target = os.path.normpath(os.path.join(os.path.dirname(_f), _href))
    if not os.path.exists(_target):
        bad.append(f'{_f}: links `{_href}`, which resolves to `{_target}` and does not exist')
    if _target.replace(os.sep, '/') != _SEM:
        bad.append(f'{_f}: links `{_href}` -> `{_target}`, not the ruled layer `{_SEM}`')
    _sty = _s.find('<style')
    if _sty == -1:
        bad.append(f'{_f}: carries no <style> block - re-derive \u00a727.15c, this gate assumes one')
    elif _lnk.start() > _sty:
        bad.append(f'{_f}: the semantic <link> is seated BELOW the page <style> block, so the '
                   'layer now overrides the page instead of the other way round (\u00a727.15c)')
    else:
        _own = _s[_sty:]
        for _sel in ('code', 'pre code'):
            _m = re.search(r'(^|\n)\s*' + _sel.replace(' ', r'\s+') + r'\s*\{([^}]*)\}', _own)
            if _m and re.search(r'background\s*:|font-family\s*:', _m.group(2)):
                bad.append(f'{_f}: its own <style> restates `{_sel}` with a background or a '
                           'font-family - one ruled construct, two spellings, and nothing '
                           'compares them (\u00a727.15c)')
if _seen == 0:
    bad.append('gate 56 scanned ZERO consumer pages - a gate that scans nothing passes')
gate('\u00a727.15c a semantic-layer consumer links it and does not restate it', bad)


# ---- GATE 58 (\u00a727.16): ONE SPELLING PER CHARACTER.
# S127 DJ RULING. The book spelled the same character two ways - 5,935 non-ASCII
# characters were literal while 4,827 were entities - so every byte-reading instrument
# counted a fraction of each population. S126's glyph census missed 711 symbols, and
# fifteen characters existed ONLY in entity form and appeared in no census ever taken.
# THE RULE IS A PROPERTY, NOT A LIST: write the character however it can be SEEN in the
# source. Literal when the literal form is distinguishable; an entity when it is not.
# The second clause reaches exactly three characters (no-break space, narrow no-break
# space, non-breaking hyphen) and the gate DERIVES that set from the property rather
# than trusting it, so a fourth invisible character cannot be added without the gate
# noticing. `&`, `<`, `>` stay mandatory; <script>/<style> are raw text the parser never
# decodes; attribute interiors are left alone.
import entity_sweep as _ES

bad = []
_scanned = 0
_HOLD_OK = {0x00A0: '&nbsp;', 0x2011: '&#8209;', 0x202F: '&#8239;'}
if set(_ES.HOLD) != set(_HOLD_OK):
    bad.append('\u00a727.16 the HOLD set drifted from the ruled three: %s' % sorted(_ES.HOLD))
for _cp, _want in _HOLD_OK.items():
    if _ES.held_spelling(_cp) != _want:
        bad.append('\u00a727.16 U+%04X spells as %r, ruled %r'
                   % (_cp, _ES.held_spelling(_cp), _want))
for _f in sorted(R):
    _s = R[_f]
    _scanned += 1
    _new, _ch, _prot, _held = _ES.sweep_text(_s)
    if _ch:
        bad.append('%s: %d character(s) still carry a non-ruled spelling (\u00a727.16)'
                   % (_f, _ch))
    for _cp in _HOLD_OK:
        if chr(_cp) in _ES.RAWTEXT.sub('', _s):
            bad.append('%s: U+%04X written LITERALLY - it is invisible in source and must '
                       'stay an entity (\u00a727.16)' % (_f, _cp))
if _scanned == 0:
    bad.append('gate 58 scanned ZERO pages - a gate that scans nothing passes')
gate('\u00a727.16 one spelling per character: literal unless invisible in source', bad)


# ---------------------------------------------------------------------------
# GATE 59 (S128) - \u00a724.14a: EVERY CALLOUT NAMES ITS OWN FAMILY.
#
# WHY THIS IS A GATE AND NOT A NOTE. Before S128, 209 of 1,069 callout blocks were
# identified ONLY by their decorative emoji - build_family_map's GLYPH tier, which
# S112 shipped calling itself a stopgap. The marks arc replaces that emoji with an
# <img>, and on the day it does those blocks lose their only family signal. The
# attribute moves the family into the markup so the decoration can go.
#
# IT ASSERTS THE PROPERTY, NOT A SPELLING (S126 rule 18). It does not check that the
# attribute is PRESENT - it re-derives the family from CONTENT through family_tag,
# which imports build_family_map's own tiers, and requires the attribute to AGREE.
# A hand-typed attribute that contradicts the content fails. So does a missing one.
#
# COVERAGE ARM, because a gate that scans zero blocks passes (S117/S118).
bad = []
try:
    import family_tag as _FT
    _n = _fam_bad = 0
    for _f in sorted(glob.glob('lessons/Lesson_*.html')):
        for _c in LI.build(_f)['callouts']:
            _n += 1
            _want = _FT.family_of(_c)
            _have = _c.get('family_attr')
            if _want is None:
                bad.append('%s @%s: no tier can name this callout' % (_f, _c['line']))
            elif _have != _want:
                _fam_bad += 1
                if _fam_bad <= 6:
                    bad.append('%s @%s: data-family is %r, content says %r'
                               % (_f, _c['line'], _have, _want))
    if _fam_bad > 6:
        bad.append('... and %d more disagreeing callout(s)' % (_fam_bad - 6))
    if _n == 0:
        bad.append('gate 59 scanned ZERO callouts - a gate that scans nothing passes')
    elif _n != 1119:
        bad.append('gate 59 saw %d callouts, expected the 1119 gate 47 holds' % _n)
except ImportError:
    bad.append('family_tag.py is missing - the attribute has no generator')
gate('\u00a724.14a every callout carries the family its CONTENT resolves to', bad)

# ---------------------------------------------------------------------------
# GATE 60 (S130) - §24.14c: THE FAMILY PIN IS A PRESERVED LAYER.
#
# WHY A FINGERPRINT AND NOT JUST A COVERAGE COUNT. ZUMO_FAMILY_PINS.md is the ONLY
# remaining home for 212 blocks' family. It is read-only input, and the hazard it exists
# to survive is that somebody REGENERATES it from `data-family` - at which point it agrees
# with any drift by construction and silently stops being evidence. A coverage count
# cannot see that: a regenerated pin has exactly the same 212 keys. Only a fingerprint
# can, so the table is pinned by md5 exactly as §11 pins the boxed challenge headers.
# Changing the pin deliberately means editing the constant below, which is a visible diff.
#
# THE COVERAGE ARM IS THE OTHER HALF, and it is scoped to the PROPERTY, not the number:
# the pinned set must be exactly the set of callouts the CONTENT tiers cannot name. A
# block that gains a content signal must LEAVE the pin, and one that loses its label must
# ENTER it. Either way the gate fails and a human rules, which is the point.
bad = []
_PINF = 'ZUMO_FAMILY_PINS.md'
_PIN_MD5 = 'c6ee67d6938e22d7c6480a0848af72a1'   # 55 rows: 212 at S130, less the 87
                                                     # glossary-side rows the S132
                                                     # STRUCTURE tier made redundant, less
                                                     # the 70 body-side KEY TERM rows S134's
                                                     # `KEY TERM: ` prefix made nameable
                                                     # from CONTENT. Retired BY THE PROPERTY
                                                     # - the survivors are this gate's own
                                                     # _need derivation, never a hand list.
                                                     # 83 converted, 13 already self-naming
                                                     # and therefore never pinned, = 70.
if not os.path.exists(_PINF):
    bad.append('%s is missing - 55 blocks lose their only family home' % _PINF)
else:
    _rows = [l for l in open(_PINF, encoding='utf-8').read().split('\n')
             if re.match(r'^\| `\d+\.\d+` \|', l)]
    _got = hashlib.md5('\n'.join(_rows).encode()).hexdigest()
    if _got != _PIN_MD5:
        bad.append('%s table changed (%d rows, md5 %s, expected %s) - if this was a '
                   'deliberate re-pin, move the constant; if it was a REGENERATION from '
                   'data-family, the pin has stopped being evidence'
                   % (_PINF, len(_rows), _got[:12], _PIN_MD5[:12]))
    try:
        import build_family_map as _B
        import lesson_inventory as _LIp
        _pinned = set(re.findall(r'^\| `(\d+\.\d+)` \|', '\n'.join(_rows), re.M))
        _need = set()
        for _f in sorted(glob.glob('lessons/Lesson_*.html')):
            for _c in _LIp.build(_f)['callouts']:
                _lab = _B.norm(_c.get('label')); _g = (_c.get('glyph') or '').strip()
                _sch = (_c['bg'] or 'none', _c['border'])
                _fam = _B.canon_of(_lab)
                if not _fam:
                    for _fn, _x in _B.RULE:
                        if _fn(_lab, _g, _sch):
                            _fam = _x; break
                # S132: STRUCTURE COUNTS AS A SIGNAL. The pin's job is to hold blocks
                # NOTHING ELSE CAN NAME. build_family_map v1.5.0 added a tier that names
                # every callout in the glossary region, so those blocks have a live signal
                # and no longer belong here - and the coverage arm says so by design
                # (rule 20: a hold satisfied by something else is not a hold). Omitting
                # this call would leave 87 rows the gate certifies as load-bearing while
                # a tier above them does the work.
                if not _fam:
                    _fam = _B.struct(_c)
                if not _fam:
                    _need.add(_c.get('callout_id'))
        if _need - _pinned:
            bad.append('%d callout(s) content cannot name are NOT pinned: %s'
                       % (len(_need - _pinned),
                          ', '.join(sorted(str(x) for x in _need - _pinned)[:8])))
        if _pinned - _need:
            bad.append('%d pinned callout(s) no longer need a pin - content names them '
                       'now, so the hold has expired: %s'
                       % (len(_pinned - _need), ', '.join(sorted(_pinned - _need)[:8])))
        if not _pinned:
            bad.append('gate 60 read ZERO pins - a gate that checks nothing passes')
    except ImportError:
        bad.append('build_family_map.py is missing - the pin has no consumer')
gate('\u00a724.14c the family pin is preserved and covers exactly the unnameable blocks',
     bad)

# ---------------------------------------------------------------------------
# GATE 61 (S130) - §7.2: THE MARK ROSTER RECONCILES AGAINST DISK.
#
# WHY IT EXISTS, AND IT IS A DEFECT THIS SESSION COMMITTED. A hand reconciliation scoped to
# §7.1's FAMILY table reported every §7.2 supporting mark as an unindexed orphan - a list of
# "14 orphans" that came within one ruling of DELETING eleven correctly-indexed files. The
# standard has TWO tables and the instrument knew one. §24.8: the population you can
# enumerate is not the population the standard names.
#
# THE MISSING SEVEN ARE NOT A DEBT, AND CALLING THEM ONE WAS THE SECOND ERROR OF THE PAIR.
# They are §7.2's SYSTEMS group, and §7.2's own Grounds table already rules that group
# "in scope: no" - it sits on a filled band rather than the page tint. So the standard
# accounts for them completely and they were never owed. Held BY NAME (§25.2a) rather than
# by count, because a count arm passes when one is drawn and a different one goes missing;
# naming them means the hold expires the moment any single one lands.
bad = []
_MARKS_MISSING = {          # §7.2 SYSTEMS: out of scope per §7.2's Grounds table, not owed.
    'box-seam': 'maker', 'chat-dots': 'tutor', 'images': 'image index',
    'stopwatch': 'timer', 'table': 'quick reference', 'trophy': 'milestones',
    'ticket-perforated': 'exit ticket',
}
try:
    import build_mark_index as _BMI
    _roster = _BMI.roster()
    _disk = {os.path.basename(f)[:-4] for f in glob.glob('images/marks/*.svg')}
    if not _roster:
        bad.append('gate 61 read an EMPTY roster - a gate that checks nothing passes')
    _unindexed = _disk - _roster
    if _unindexed:
        bad.append('%d mark(s) on disk are in NEITHER §7 table: %s'
                   % (len(_unindexed), ', '.join(sorted(_unindexed))))
    _absent = _roster - _disk
    _new = _absent - set(_MARKS_MISSING)
    if _new:
        bad.append('%d mark(s) named in §7 but NOT on disk and not held: %s'
                   % (len(_new), ', '.join(sorted(_new))))
    _landed = set(_MARKS_MISSING) - _absent
    if _landed:
        bad.append('%d held mark(s) are now on disk - the hold has expired, remove them '
                   'from _MARKS_MISSING: %s' % (len(_landed), ', '.join(sorted(_landed))))
except ImportError:
    bad.append('build_mark_index.py is missing - the mark roster has no source')
gate('\u00a77.2 every mark on disk is indexed and every named mark is accounted for', bad)

# ---------------------------------------------------------------------------
# GATE 62 (S130) - §12.6: THE CENSUS IS RE-DERIVABLE BY ORDINARY MEANS.
#
# The census ran ONE HIGH PER FILE for its whole life - an unconditional `count('\n') + 1`
# counts the empty string after a trailing newline as a line - so `wc -l` disagreed by 16
# and the gap had to be explained every time anyone checked. DJ: "Why do we need it. Can't
# we fix the problem?" A number that needs a footnote to avoid being misread is a defect.
#
# THIS GATE IS THE SECOND METHOD, NOT A RESTATEMENT OF THE FIRST. It counts newlines
# directly, without importing the parser, so it fails if the two definitions ever diverge
# again. The trailing-newline arm is what keeps them equal: every lesson must end in one,
# because that is the condition under which "newlines" and "lines" are the same number.
bad = []
try:
    import lesson_inventory as _LIc
    _files = sorted(glob.glob('lessons/Lesson_*.html'))
    if not _files:
        bad.append('gate 62 found ZERO lessons - a gate that counts nothing passes')
    _raw = 0
    for _f in _files:
        _src = open(_f, encoding='utf-8').read()
        if not _src.endswith('\n'):
            bad.append('%s does not end in a newline - its final line is unterminated, and '
                       'the census and wc -l stop agreeing' % _f)
        _raw += _src.count('\n')
    _inv = sum(_LIc.build(_f)['lines'] for _f in _files)
    if _inv != _raw:
        bad.append('census %d disagrees with an independent newline count %d - the two '
                   'definitions have diverged' % (_inv, _raw))
except ImportError:
    bad.append('lesson_inventory.py is missing - the census has no source')
gate('\u00a712.6 the census equals an independent line count', bad)


# GATE 63 (S131) - §10: A FIGURE IS LANDED BY AN ASSET, NEVER BY A DECORATION.
#
# image_audit has a NEIGHBOUR arm: if the filename does not match, an <img> sitting in the
# tag's own paragraph lands the figure anyway. It exists for L10, which prints "this is the
# same photo you met in Lesson 5" and wires L05's file directly - counting that as missing
# would send DJ out to re-shoot a photograph the book already ships.
#
# S130 then put 884 <img data-mark> marks into that same prose, and the arm could not tell a
# lightbulb from a photograph. SIX REAL SHOTS - L03 3.2 / 3.5 / 3.6, L12 12.1, L14 14.1,
# L16 16.1 - reported LANDED. Nothing failed. `--check` said DIFFERS and the only honest
# reading of that was "re-run me", which would have written 8 over 14 and retired six
# entries from the shot list four weeks out from the course.
#
# THIS GATE IS THE SECOND METHOD AND SHARES NO CODE WITH THE FIRST. It does not import
# image_audit for the question that matters: it re-derives landing from FILENAMES ON DISK
# with its own regexes, and requires every disagreement to be a NAMED reuse with a recorded
# reason. Whatever a future arc decorates the prose with, a tag that quietly stops being
# outstanding lands here. Arm 4 keeps the names honest: a hold that has become true by
# accident is not a hold (S130 rule 20), so a name that no longer NEEDS the exemption fails.
REUSE = {
    # tag -> why this tag legitimately lands with no file of its own name
    'IMAGE 10.1': "L10 wires L05_IMAGE_5-04b directly and the prose says so - "
                  "'this is the same photo you met in Lesson 5'",
    'IMAGE 7.3': "UNRULED, held by name at S131: satisfied by L07_GRAPHIC_7-15_platformio_"
                 "file_tree.svg, which is a GRAPHIC standing in for an IMAGE across the two "
                 "number spaces (\u00a710), with no prose declaring the substitution. Same "
                 "subject, so it is plausibly deliberate - but nothing in the book says so, "
                 "and this gate will not decide it. DJ rules; the name leaves when he does.",
}
bad = []
_WL = 'IMAGE_WORKLIST.md'
_TAG63 = re.compile(r'\[(IMAGE|GRAPHIC|VIDEO)\s+(\d+)\.(\d+)([a-z]?)\]')
_ROW63 = re.compile(r'^\| L(\d\d) \| ([A-Z]+ \d+\.\d+[a-z]?) \|')
if not os.path.exists(_WL):
    bad.append('%s is missing - the shot list has no home' % _WL)
else:
    # ARM 1 - CURRENCY. This one DOES import the generator, because "the artefact matches its
    # generator" is the only question that cannot be asked without it. It is not the
    # independence claim; arm 3 is.
    try:
        import image_audit as _IA
        if _IA.emit(*_IA.audit()) != open(_WL, encoding='utf-8').read():
            bad.append('%s does not match what image_audit emits - regenerate it, and read '
                       'the diff before you do' % _WL)
    except ImportError:
        bad.append('image_audit.py is missing - the shot list has no generator')

    _rows = set()
    for _ln in open(_WL, encoding='utf-8'):
        _m = _ROW63.match(_ln)
        if _m:
            _rows.add((_m.group(1), _m.group(2)))
    _disk63 = [os.path.basename(_p) for _p in glob.glob('images/*.*')]
    _planned63, _needed = 0, set()
    for _f in files:
        _host = os.path.basename(_f)[7:9]
        _src = open(_f, encoding='utf-8').read()
        for _k, _a, _b, _s in {(m.group(1), int(m.group(2)), int(m.group(3)), m.group(4))
                               for m in _TAG63.finditer(_src)}:
            _planned63 += 1
            _tag = '%s %d.%d%s' % (_k, _a, _b, _s)
            if _k == 'VIDEO' or (_host, _tag) in _rows:
                continue
            # ARM 3 - INDEPENDENT. Own regex, own directory read, no image_audit.
            _pat = re.compile(r'^L%02d_%s_%d-0*%d%s_' % (_a, _k, _a, _b, _s), re.I)
            if any(_pat.match(_d) for _d in _disk63):
                continue
            _needed.add(_tag)
            if _tag not in REUSE:
                bad.append('L%s [%s] is not outstanding and no file in images/ carries its '
                           'name - something in the prose landed it that is not an asset '
                           '(a mark did exactly this at S130). Shoot it, wire it, or add it '
                           'to REUSE with a reason.' % (_host, _tag))
    # ARM 2 - COVERAGE. A gate that reads zero tags passes (S117/S118).
    if _planned63 < 100:
        bad.append('gate 63 saw only %d planned tag(s) - the scan under-reaches' % _planned63)
    # ARM 4 - THE NAMES MUST STILL BE LOAD-BEARING.
    for _t in sorted(set(REUSE) - _needed):
        bad.append('[%s] is held in REUSE but no longer needs the exemption - it either has '
                   'its own file now or stopped being planned. Drop the name.' % _t)
gate('\u00a710  no figure is landed by a decoration', bad)


# ---- GATE 64 (\u00a724.14b) - THE STRUCTURE TIER'S PREDICATE, S132.
# The tier says: a callout inside the GLOSSARY REGION is a KEY TERM. That is TRUE TODAY,
# 97 of 97, and this gate exists because it is the kind of truth an author can break in
# one paste - drop a NOTE into a glossary and the tier silently mis-families it.
#
# IT ASSERTS THE PREDICATE, NOT THE TIER'S OUTPUT. Asking "does the tier return KEY TERM
# for these blocks" is circular. This asks the opposite question: with the tier BLINDED,
# does any glossary-region callout resolve to a family that is NOT KEY TERM? Silence is
# fine - after the 87 pin rows retire, most of them will resolve to nothing with the tier
# blinded, and nothing is not a contradiction. A DISAGREEMENT is the failure.
#
# ARM 2 PINS THE PROPERTY, NOT THE SPELLING (rule 19). The region detector matches a
# banner by shape, deliberately not by the div-bg-* wrapper - L04's glossary banner wears
# no wrapper, and the first probe of this arc keyed on the wrapper and returned ZERO
# regions for L04, which read as clean. So the roster itself is gated: if a markup change
# stops the detector matching, the count moves and this fails loudly instead of a tier
# quietly resolving nothing.
bad = []
try:
    import lesson_inventory as _LI64
    import family_tag as _FT64
    _B64 = _FT64.B
    _glos = _named = 0
    _roster = collections.Counter()
    for _f in files:
        _inv64 = _LI64.build(_f)
        for _r in _inv64['regions']:
            _roster[_r['id']] += 1
        for _c in _inv64['callouts']:
            if _c.get('region') != 'glossary':
                continue
            _glos += 1
            # BLINDED: attribute, CANON, RULE, PIN - every tier EXCEPT struct.
            _lab = _B64.norm(_c.get('label'))
            _g64 = (_c.get('glyph') or '').strip()
            _sch = (_c['bg'] or 'none', _c['border'])
            _f64 = _c.get('family_attr')
            if not _f64:
                _f64 = _B64.canon_of(_lab)
            if not _f64:
                for _fn, _x in _B64.RULE:
                    if _fn(_lab, _g64, _sch):
                        _f64 = _x
                        break
            if not _f64:
                _f64 = _B64.PINS.get(_c.get('callout_id'))
            if _f64:
                _named += 1
                if _f64 != 'KEY TERM':
                    bad.append('L%s callout %s sits in the glossary region but resolves to '
                               '%s - the STRUCTURE tier would call it KEY TERM and be wrong. '
                               'Either it does not belong in the glossary or the tier does '
                               'not belong in build_family_map.'
                               % (_inv64['lesson'], _c.get('callout_id'), _f64))
    # ARM 1b - COVERAGE. A gate that reads zero blocks passes (S117/S118).
    if _glos < 90:
        bad.append('gate 64 saw only %d glossary-region callout(s) - the region detector '
                   'under-reaches, which is exactly how a wrapper-keyed probe missed L04'
                   % _glos)
    if not _named:
        bad.append('gate 64 resolved NO glossary-region callout with the tier blinded - the '
                   'contradiction arm cannot fire and is not evidence')
    # ARM 2 - THE BANNER ROSTER.
    _EXPECT64 = {'section-1': 16, 'section-2': 16, 'section-3': 16, 'section-4': 16,
                 'section-5': 16, 'section-6': 16, 'section-7': 16, 'section-8': 16,
                 'section-8a': 14, 'section-9': 16, 'section-10': 16,
                 'bonus-challenges': 15, 'glossary': 16, 'quick-ref': 16, 'figures': 16}
    if dict(_roster) != _EXPECT64:
        for _k in sorted(set(_EXPECT64) | set(_roster)):
            if _roster.get(_k, 0) != _EXPECT64.get(_k, 0):
                bad.append('banner roster: %s appears %d time(s), expected %d - the region '
                           'detector reads a SHAPE, and a shape that stopped matching makes '
                           'the STRUCTURE tier resolve nothing in silence'
                           % (_k, _roster.get(_k, 0), _EXPECT64.get(_k, 0)))
except ImportError as _e:
    bad.append('gate 64 could not import its inputs (%s)' % _e)
gate('\u00a724.14b a glossary-region callout is a KEY TERM, and the banner roster holds', bad)


# ---- GATE 65 (\u00a727.15f) - THE REVEAL BOX, S132.
# The ruling and its gate ship together (S125). This is gate 57's assertion on a SECOND
# construct, and it is written out rather than shared because the two grounds differ and a
# helper taking a ground as an argument would invite a third caller to pass the wrong one.
#
# THE RATIO, NOT THE SPELLING. That is the whole argument, and this construct is the reason
# it generalises: #dee2e6 on #f8f9fa is 1.24:1, LOWER than the #333 that gate 57 exists to
# have retired, and it sat on 238 blocks. A gate checking for the literal #909090 would
# certify tomorrow's invisible grey exactly as the old one was certified.
#
# THE POINTER ARM GUARDS THE DEFECT, NOT THE STYLE. 55 reveals in L05-L09 carried no class
# at all and therefore no cursor cue - the mouse did not change over the clickable line.
# That is the only part of this ruling a reader would have FELT, so it is asserted directly.
#
# THE HOLD IS NAMED (\u00a725.2a, DJ ruling S132). L11's four ANSWER callouts keep their skin,
# and arm 4 fails if that skin ever stops declaring `border: none` - because this rule sets
# the border SHORTHAND, and a class naming only border-left would silently take three grey
# sides. A hold that depends on a cascade nobody checks is not a hold (rule 20).
bad = []
_sem65 = open('css/semantic.css', encoding='utf-8').read()
_gen65 = open('css/book.css', encoding='utf-8').read()


def _lum65(h):
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


_dets = re.findall(r'(?<!,)\ndetails\s*\{([^}]*)\}', _sem65)
_sums = re.findall(r'(?<!,)\nsummary\s*\{([^}]*)\}', _sem65)
if len(_dets) != 1 or len(_sums) != 1:
    bad.append('css/semantic.css holds %d `details` and %d `summary` element rule(s); '
               'expected exactly one each (\u00a727.15f)' % (len(_dets), len(_sums)))
else:
    _dd = {k.split(':')[0].strip(): k.split(':', 1)[1].strip()
           for k in _dets[0].split(';') if ':' in k}
    _ds = {k.split(':')[0].strip(): k.split(':', 1)[1].strip()
           for k in _sums[0].split(';') if ':' in k}
    # ARM 1 - the values §27.15e already ruled, restated on this construct.
    for _k, _v in (('background', '#f8f9fa'), ('border-radius', '6px'),
                   ('padding', '15px'), ('margin', '15px 0')):
        if _dd.get(_k) != _v:
            bad.append('\u00a727.15f `details` declares %s: %r, ruled %r' % (_k, _dd.get(_k), _v))
    # ARM 2 - THE BORDER EARNS ITS PLACE, asserted by ratio against its own ground.
    _b65 = _dd.get('border', '')
    _h65 = re.search(r'#([0-9a-fA-F]{6})', _b65)
    if not _h65 or not _b65.startswith('1px solid'):
        bad.append('\u00a727.15f `details` border is %r, expected `1px solid #rrggbb`' % _b65)
    else:
        _l1, _l2 = _lum65(_h65.group(1)), _lum65('f8f9fa')
        _r65 = (max(_l1, _l2) + 0.05) / (min(_l1, _l2) + 0.05)
        if _r65 < 3.0:
            bad.append('\u00a727.15f `details` border #%s is %.2f:1 against the #f8f9fa ground '
                       '\u2014 below the 3:1 minimum, so it is invisible'
                       % (_h65.group(1), _r65))
    # ARM 3 - THE POINTER, and the summary colour asserted by ratio for the same reason.
    if _ds.get('cursor') != 'pointer':
        bad.append('\u00a727.15f `summary` declares cursor: %r \u2014 55 reveals shipped with no '
                   'pointer cue at all and that is the defect this rule closed'
                   % _ds.get('cursor'))
    if _ds.get('font-weight') != 'bold':
        bad.append('\u00a727.15f `summary` font-weight is %r, ruled bold' % _ds.get('font-weight'))
    _hs = re.search(r'#([0-9a-fA-F]{6})', _ds.get('color', ''))
    if not _hs:
        bad.append('\u00a727.15f `summary` declares no colour')
    else:
        _l1, _l2 = _lum65(_hs.group(1)), _lum65('f8f9fa')
        _rs = (max(_l1, _l2) + 0.05) / (min(_l1, _l2) + 0.05)
        if _rs < 4.5:
            bad.append('\u00a727.15f `summary` colour #%s is %.2f:1 on the box \u2014 below the '
                       '4.5:1 text minimum' % (_hs.group(1), _rs))
# ARM 4 - NO EXCEPTION SURVIVES. The one candidate hold, L11's four ANSWER callouts, was
# ruled OUT by DJ: the word stays, the box matches. The arm is INVERTED rather than deleted
# (S108) - a gate that stops checking is worse than one that fails.
_HELD65 = 'callout-6c757d-bg-faf6fd'
if re.search(r'^\.%s\s*\{' % re.escape(_HELD65), _gen65, re.M):
    bad.append('.%s is back \u2014 a reveal wearing a callout skin, which \u00a727.15f ruled '
               'out (DJ, S132: the word stays, the pill matches)' % _HELD65)
for _f4 in files:
    if re.search(r'<details\b[^>]*data-family=', open(_f4, encoding='utf-8').read()):
        bad.append('%s: a <details> carries data-family \u2014 a reveal is not a callout '
                   '(\u00a727.15f)' % os.path.basename(_f4))
# ARM 5 - NO SECOND SPELLING: no generated class may re-style a reveal.
_gi65 = _gen65.find('GENERATED BLOCK')
for _m65 in re.finditer(r'^\.((?:details|summary)[A-Za-z0-9_-]*)\s*\{', _gen65[_gi65:], re.M):
    bad.append('.%s restates the reveal box \u2014 one construct, two spellings (\u00a727.15f)'
               % _m65.group(1))
# ARM 6 - COVERAGE (S117/S118), and the markup arm: a reveal must carry NO class of its own.
_seen65 = _stray65 = 0
for _f65 in files:
    _s65 = open(_f65, encoding='utf-8').read()
    for _t65 in re.finditer(r'<(details|summary)\b([^>]*)>', _s65):
        _seen65 += 1
        if 'class=' in _t65.group(2):
            _stray65 += 1
if _seen65 < 800:
    bad.append('scanned only %d reveal element(s) \u2014 the scope is broken (\u00a727.15f)' % _seen65)
if _stray65:
    bad.append('%d reveal element(s) still carry a class of their own \u2014 the element rule is '
               'the only home and a class beats it silently (\u00a727.15f)' % _stray65)
gate('\u00a727.15f the reveal box is one rule, with a visible border and a pointer', bad)

# =====================================================================
# GATE 66  -  SECTION 1 OPENS WITH SOMETHING TO LOOK AT  (S133, DJ ruling)
# =====================================================================
# WHY. Section 1 is the hook - "The Messy Room Problem", "The Crooked Robot Problem" - and
# its whole job is to make a student care before any code appears. At S133, EIGHT of sixteen
# had a real figure, three had a placeholder, and FIVE had nothing at all: L04, L11, L12, L13,
# L15. The five were invisible to image_audit, and correctly so - that tool reports figures the
# book DECLARES it wants, and nobody had ever declared these. An absence nobody wrote down is
# an absence no instrument can find (S24.8).
#
# WHAT IT ASSERTS. Every lesson's S1 carries a figure OR a declared placeholder. Placeholder
# counts, deliberately: the ruling is that a hook needs something to look at, and a declared
# figure is on IMAGE_WORKLIST.md and therefore visible work. A gate demanding a landed ASSET
# would be a to-do list wearing a gate - red for months, and tuned away by the first reader.
#
# THE PREDICATE IS THE AUTHORED NAME, NOT A PATH (rule 19). A figure asset is one named
# L##_IMAGE_ or L##_GRAPHIC_ per S10/S17. Keying on the directory instead would count every
# decorative mark in images/marks/ and every spiral_star_NN.svg as a figure - and it did, on
# the first draft of this very check, reporting a false 16 of 16 with SIX lessons still empty.
# The naming convention is a property of the asset; the directory is where it happens to live.
_S1FIG = re.compile(r'L\d\d_(?:IMAGE|GRAPHIC)_')
_S1PH  = re.compile(r'\[(?:IMAGE|GRAPHIC|VIDEO) [\d.]+\]')
bad = []
_seen1 = 0
for _f1 in files:
    _s1 = open(_f1, encoding='utf-8').read()
    _a1 = _s1.find('id="section-1"')
    _b1 = _s1.find('id="section-2"')
    if _a1 < 0:
        bad.append('%s carries no id="section-1"' % L(_f1))
        continue
    if _b1 < _a1:
        bad.append('%s: section-2 does not follow section-1 - the slice is wrong' % L(_f1))
        continue
    _seen1 += 1
    _seg1 = _s1[_a1:_b1]
    _as1 = [x for x in re.findall(r'<img[^>]*src="\.\./images/([^"]+)"', _seg1)
            if _S1FIG.search(x)]
    if _as1:
        continue
    if _S1PH.search(_seg1):
        continue
    bad.append('%s: Section 1 carries no figure and no declared placeholder - the hook has '
               'nothing to look at, and nothing on the worklist will ever say so' % L(_f1))
# COVERAGE ARM (S117/S118): a gate that scans zero lessons passes.
if _seen1 != len(files):
    bad.append('scanned %d of %d lessons - the scope is broken' % (_seen1, len(files)))
gate('\u00a72.1 every lesson opens Section 1 with a figure or a declared placeholder', bad)

# =====================================================================
# GATE 67  -  SECTION 2 STATES OBJECTIVES, AND EACH ONE IS A BOX  (S133, DJ ruling)
# =====================================================================
# DJ, S133: "Can you make it a rule that lessons have to have objectives and there are
# squares/boxes not dots."
#
# THREE ARMS, AND THE THIRD IS THE ONE NOTHING COULD SEE.
#   1. Every lesson's Section 2 states at least one objective.
#   2. Every objective carries the literal box glyph. L01 and L15 carried NONE at S133 open -
#      13 objectives with no box - and v8.108 had recorded that as an observation with no gate.
#   3. The list must not ALSO draw a bullet. Four lessons (L01, L05, L15, L16) left the <ul>
#      at the browser default, so each objective rendered as a DOT followed by a BOX. Twelve
#      lessons suppressed it and four did not, and no instrument in the tree looked at
#      list-style - it is resolved styling, not markup, so a grep of the lesson cannot answer
#      it. That is the shape DJ asked about by name: "boxes not dots."
#
# THE BOX IS THE LITERAL CHARACTER, NOT AN ENTITY (S27.16, and v8.104 converted 98 of them).
# Asserting on the entity spelling would pass a book that renders no boxes at all.
#
# SCOPE IS THE SECTION, NOT THE PAGE (S122's repeated lesson): a page-wide count of the box
# glyph is satisfied by BC02, which carries its own boxes by S25.5 and would mask an empty S2.
_BOX = '\u2610'
bad = []
_seen2 = 0
for _f2 in files:
    _s2 = open(_f2, encoding='utf-8').read()
    _a2 = _s2.find('id="section-2"')
    _b2 = _s2.find('id="section-3"')
    if _a2 < 0:
        bad.append('%s carries no id="section-2"' % L(_f2))
        continue
    if _b2 < _a2:
        bad.append('%s: section-3 does not follow section-2 - the slice is wrong' % L(_f2))
        continue
    _seen2 += 1
    _seg2 = _s2[_a2:_b2]
    _items = re.findall(r'<li[^>]*>(.*?)</li>', _seg2, re.S)
    if not _items:
        bad.append('%s: Section 2 states no objectives' % L(_f2))
        continue
    _nb = [x for x in _items if not x.lstrip().startswith(_BOX)]
    if _nb:
        bad.append('%s: %d of %d objective(s) carry no box - an objective the student cannot '
                   'tick is a sentence, not a checklist'
                   % (L(_f2), len(_nb), len(_items)))
    # ARM 3 - THE BULLET. DJ, S133: "squares/boxes not dots". An objective list must not draw
    # its own bullet on top of the box. THE PREDICATE IS THE ATTRIBUTE, and the attribute is
    # why this arm can exist at all: routing the rule through the generated layer swapped
    # .ul-ls-none with .ul-ls-none-3 and silently re-resolved twelve untouched lessons
    # (S27.15b). ul[data-objectives] lives in css/semantic.css, which build_css preserves
    # verbatim and never re-derives, so this rule cannot be renamed or re-ranked.
    # A CLASS THAT ALREADY SUPPRESSES THE BULLET ALSO SATISFIES IT - the twelve conforming
    # lessons are not made non-compliant by a rule written for the four that were not.
    _exp2 = LI.expand_classes_mapped(_s2)[0]
    _ea2 = _exp2.find('id="section-2"')
    _eb2 = _exp2.find('id="section-3"')
    for _u2 in re.finditer(r'<ul([^>]*)>(.*?)</ul>', _exp2[_ea2:_eb2], re.S):
        if _BOX not in _u2.group(2):
            continue                      # not an objective list
        _at2 = _u2.group(1)
        if 'data-objectives' in _at2:
            continue
        _st2 = re.search(r'style="([^"]*)"', _at2)
        if not (_st2 and re.search(r'list-style[^;:]*:\s*none', _st2.group(1))):
            bad.append('%s: an objective list draws its own bullet - every item renders as a '
                       'dot AND a box (DJ, S133: boxes not dots)' % L(_f2))
# COVERAGE ARM (S117/S118): a gate that scans zero lessons passes.
if _seen2 != len(files):
    bad.append('scanned %d of %d lessons - the scope is broken' % (_seen2, len(files)))
gate('\u00a72.2 every lesson states objectives, each a box and not a bullet', bad)


# ---- 68. §24.14d THE BODY KEY TERM NAMES ITS FAMILY; THE GLOSSARY ENTRY DOES NOT ----
# DJ ruling S134, option A, taken on rendered specimens of both glossaries side by side.
#
# WHY THE RULE EXISTS. KEY TERM was the only large family in this book that did not name
# itself. Measured across all 1,119 live callouts: NOTE 113/133, CHECKPOINT 102/112,
# TIP 79/85, DO THIS NOW 55/58, WARNING 67/80, LEARN 38/47, and BRAIN CHECK / THE GOAL /
# MY PLAN / BUILDS ON at 100%. KEY TERM stood at 13 of 238 - and those 13 were exactly
# the blocks a normalisation pass was about to strip, which is the finding that reversed
# the session's direction.
#
# WHY IT IS TWO ASSERTIONS AND NOT ONE. The prefix is ruled IN for the body and OUT for
# the glossary, deliberately, because the glossary sits under a banner that already reads
# Glossary and 151 repetitions of the family name would push every term off the left edge
# a reader scans. That makes the rule a REGION rule, and this gate asserts BOTH halves -
# a gate that only checked the body would certify a glossary silently drifting into the
# prefix as conformant.
#
# THE PREDICATE IS IMPORTED, NOT RE-IMPLEMENTED (S83). book_gates, family_tag and
# build_family_map each held their own copy of the canon matcher until S133 found all
# three; the same defect is available here, so head_of() and PREFIX come from the tool
# that writes them and cannot drift away from it.
#
# HELD BY NAME, NOT BY COUNT (§25.2a). Four body blocks carry the family and are not term
# cards - a provenance question, an operator announcement, a formula and a procedural list.
# DJ held constrain explicitly and the other three are the same shape. They are excepted by
# id so that a future session reads a NAME and a reason rather than finding a silent gap.
bad = []
try:
    import keyterm_prefix as _KT
    _bodyseen = _glosseen = 0
    _heldshape = {}
    for _f3 in sorted(glob.glob('lessons/Lesson_*.html')):
        _src3 = open(_f3, encoding='utf-8').read()
        _exp3, _tofile3 = LI.expand_classes_mapped(_src3)
        for _c3 in LI.build(_f3)['callouts']:
            if _c3.get('family_attr') != 'KEY TERM':
                continue
            _cid3 = _c3.get('callout_id')
            _fs3 = _tofile3(int(_c3['exp_start']))
            _raw3 = _src3[_fs3:_fs3 + int(_c3['bytes']) * 3]
            _k3, _h3 = _KT.head_of(_raw3)
            if _k3 is None:
                bad.append('%s: KEY TERM %s has no head carrying the key mark'
                           % (L(_f3), _cid3))
                continue
            if _c3['region'] == 'glossary':
                _glosseen += 1
                if _h3.interior.lstrip().upper().startswith(_KT.PREFIX.strip().upper()):
                    bad.append('%s: glossary entry %s carries the KEY TERM prefix - the '
                               'section banner already says Glossary (DJ, S134 option A)'
                               % (L(_f3), _cid3))
                continue
            _bodyseen += 1
            if _cid3 in _KT.HELD:
                _heldshape[_cid3] = _h3.interior
                continue
            if not _h3.interior.startswith(_KT.PREFIX):
                bad.append('%s: body KEY TERM %s does not open with %r - it is the only '
                           'large family that would not name itself'
                           % (L(_f3), _cid3, _KT.PREFIX))
            elif not re.search(r'<strong\b', _h3.interior):
                bad.append('%s: body KEY TERM %s carries the prefix but its term is not in '
                           'a <strong> - the term is what the glossary harvest extracts'
                           % (L(_f3), _cid3))
    # COVERAGE ARM (S117/S118): a gate that scans zero blocks passes.
    if _bodyseen != 87:
        bad.append('scanned %d body KEY TERM blocks, expected 87 - the scope is broken'
                   % _bodyseen)
    if _glosseen != 151:
        bad.append('scanned %d glossary KEY TERM entries, expected 151 - the scope is broken'
                   % _glosseen)
    # HOLD ARM, AND IT IS HERE BECAUSE THE FIRST DRAFT OF THIS GATE FAILED ITS OWN CONTROL.
    # Adding a fifth id to HELD excepted a real, conformant block and every arm above stayed
    # green: the coverage count measures blocks SCANNED, not blocks ASSERTED, so an exception
    # is invisible to it. That is S130 rule 20 arriving inside the gate written to enforce a
    # ruling - a hold something else satisfies is not a hold - and it is caught by pinning
    # the hold two ways. The SET is named (§25.2a), so swapping an id fails; and each held
    # block must genuinely still lack the prefix, so a hold that has quietly become
    # unnecessary expires loudly instead of sitting there certified.
    _HELD_EXPECT = {'3.31', '3.101', '6.24', '14.28'}
    if set(_KT.HELD) != _HELD_EXPECT:
        bad.append('keyterm_prefix.HELD is %s, expected %s - the four non-term blocks are '
                   'held BY NAME; changing the set needs a DJ ruling, not an edit'
                   % (sorted(_KT.HELD), sorted(_HELD_EXPECT)))
    for _hid in sorted(set(_KT.HELD) & _HELD_EXPECT):
        _hb = _heldshape.get(_hid)
        if _hb is None:
            bad.append('held id %s is not a live body KEY TERM block' % _hid)
        elif _hb.startswith(_KT.PREFIX):
            bad.append('held block %s now carries the prefix - the hold has EXPIRED and the '
                       'row should come out of HELD' % _hid)
except ImportError:
    bad.append('keyterm_prefix.py is missing - the rule has no predicate')
gate('\u00a724.14d the body KEY TERM names its family and the glossary entry does not', bad)


# ---------------------------------------------------------------- GATE 69 (S135)
# \u00a710  A FIGURE IS PLANNED BY ITS TAG, AND THE TAG DOES NOT LIVE WHERE THE FIGURE DOES.
# Landing three \u00a71 hook GRAPHICs made image_audit report planned 146 -> 143 with LANDED
# UNMOVED at 127: the three had not moved from outstanding to landed, they had LEFT THE
# POPULATION. A landed figure's tag lives in the lesson's FIGURES INDEX TABLE; the body
# carries only the <img>. Swapping the placeholder therefore deleted the tag's only
# occurrence and shrank the DENOMINATOR. Nothing failed. `image_audit --check` printed
# DIFFERS, which reads as "re-run me" (rule 22), and --write would have accepted the
# smaller population and printed a smaller `outstanding` that looks exactly like progress.
# Gate 63 is structurally blind to this: it walks TAG -> asset, so a tag that no longer
# exists is never iterated (\u00a724.8).
# THE PIN IS THE PLANNED TOTAL, NOT THE OUTSTANDING COUNT. Outstanding is MEANT to fall as
# art lands; pinning it would fire on every success. planned moves only when a figure is
# ruled into or out of the book, which is DJ's call and not a side effect of an edit.
PLANNED_EXPECTED = 146      # stated, not inherited - moves only when a figure is ruled in or out
bad = []
try:
    import image_audit as _IA69       # by module name, the LI convention at line 325
    _pl, _out, _orph, _dup = _IA69.audit()
    if len(_pl) != PLANNED_EXPECTED:
        bad.append('%d figure tags planned, expected %d - a tag was added or DELETED. A tag '
                   'deleted without the figure landing shrinks the denominator, so outstanding '
                   'falls like progress (S135)' % (len(_pl), PLANNED_EXPECTED))
    if len(_out) > len(_pl):
        bad.append('outstanding %d exceeds planned %d' % (len(_out), len(_pl)))
except Exception as _e69:
    bad.append('image_audit.audit() did not run - the rule has no predicate (%s)' % _e69)
gate('\u00a710   the planned figure population is whole', bad)

print('=' * 52)



if FAIL:
    print(f'{len(FAIL)} GATE(S) FAILED: {", ".join(FAIL)}')
    sys.exit(1)
print('ALL GATES PASS')

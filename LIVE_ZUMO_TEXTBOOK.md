# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 26, 2026 (Session 73 — **TWO LESSONS CHANGED SHAPE**: L02's renumber cut (v03.0.0, the book's first major re-baseline) and **L03 joined the Brain Check family** (v03.14.0). Bible **v8.59**.)
**Status:** **THE OUTLIER IS GONE AND THE FAMILY IS FIXED AT FOUR.** L02 had carried the code walkthrough inside §3, prep at §4, the build at §5, and a unique §6 "Make It Yours" pushing every later number one ahead — for the life of the book. §3.2 lifted out as ONE contiguous 29,833-character block and became **§5 The Code**; old §5 → §6 with *Getting Ready* folded into its opening; §3 closed to **3.1–3.6** (not 3.1–3.5 — `3.2d` turned out to be its own `<h3>`); **zero nav-pill edits**, the strip was already canonical. **L03's conversion needed almost no new authoring** — its STOP & PROCESS block was the pre-collapse ancestor of both halves of the family, and its own ten items split 5 recall → BC01 Mental at the §5/§6 seam, 5 apply → BC03 Knowledge Check. **The split changed mid-session on canon, not preference**: item 10 was headed for Reflection until its reveal turned out to be factual, and §25.2 says Reflection never reveals — placing it there would have meant deleting an answer to pass a gate. It also turned out to duplicate an existing Reflection prompt, which retired into it. **DJ's BC05 was priced and withdrawn**: the shared column is one 5,596-character block copied byte-identical into every converted lesson and its script is hardcoded to four, so L03's second checkbox list folded into **BC02** as labelled *I can…* / *I have…* groups, twelve `data-bc-skill` items — and the unlock generalised from 7-of-7 to 12-of-12 with no code change at all, because `allSkills()` counts elements rather than a constant. **The session's through-line is one rule**, now Bible **§25.10a**: a §-citation is verified by checking the cited section CONTAINS the answer, never by checking one is present — which is all the §25.2 gate can do. It caught a live defect in L02 (BC01 item 3 cited §3.2 for the function prototype; §3.2 never taught it) and it nearly missed that defect, because slicing a section by the next section anchor swallows the Brain Check sitting between them.

**Versions:** L01 **v03.10.0** · L02 **v03.0.0** · L03 **v03.14.0** · L04 **v04.6.2** · L05 **v04.8.2** · L06 **v04.11.2** · L07 **v04.7.2** · L08 **v04.6.2** · L09 **v05.4.2** · L10 **v02.5.2** · L11 **v02.7.2** · L12 **v01.7.2** · L13 **v02.6.2** · L14 **v02.8.2** · L15 **v02.6.2** · L16 **v02.5.2** · Bible **v8.59** · Maker **v2.45.1** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0 · book_gates **v1.7 (21 gates)** · going_deeper **v01.1.0** · **web tools (version-lined in-file): timer v1.3.0 · Maker v2.45.1 · tutor v1.0.0 · index v1.3.0**.

---

## WHAT SHIPPED THIS BATCH (S73, part 2 — L03 joins the Brain Check family)

**7. L03 v03.13.2 → v03.14.0 — the third conversion, almost entirely redistribution.** L03's `STOP & PROCESS` block held **all ten** of the lesson's quiz reveals and was the pre-collapse ancestor of both halves of the family — its subtitle was literally *"Answer From Your Head, Then Check"*. Split by the §25.2 recall/apply line: **BC01 Mental** gets items 1, 2, 3, 5, 6 (5, inside the gated 3–5 window) at the §5/§6 seam; **BC03 Knowledge Check** gets 4, 7, 8, 9, 10 (5). Every item arrived already §-cited. Nothing authored from scratch.

**8. The split changed mid-session, on canon.** Item 10 ("would a warehouse robot tune TRIM by hand?") was assigned to Reflection on the L02 analogy. Its reveal is factual — closed-loop control, encoders, a Lesson 6 forward-reference — and **§25.2 says Reflection never reveals**, gate-enforced. Putting it there would have required deleting an answer to pass. It then turned out to **duplicate an existing Reflection prompt** ("How does TRIM relate to real-world robots like self-driving cars?"), which retired into it: the surviving version is strictly richer. Reflection came out at 3, inside its cap, without anyone trimming it.

**9. BC05 was ruled, priced, and withdrawn.** DJ ruled L03's second checkbox list a fifth Brain Check *"if that doesn't mess things up."* It does: the column is **one 5,596-character block copied byte-identical into every converted lesson** (L01 == L02, verified) and its script is hardcoded to four — the state array is length 4 and discarded otherwise, the click handler rejects the fifth index, the unlock is wired to BC02 by index. A BC05 buys three diverging copies of that script. Instead both lists live in **BC02** under bold **I can…** (8 capability) / **I have…** (4 process) labels, twelve `data-bc-skill` items. **The unlock generalised for free** — `allSkills()` loops over elements, so 7-of-7 became 12-of-12 with zero JS edits.

**10. Bible v8.58.1 → v8.59 — new §25.10a.** The family is four and the column is why; an extra exit block folds into the BC it most resembles as a labelled group; check whether a mechanism already scales before ruling that it doesn't; the column seats before `</body>` (appended after `</html>` it renders fine and fails the structure gate — how S73 caught it); and the subsection-slicing trap that makes a bad §-citation look verified.

**11. Verification.** 21/21 gates PASS, pill_sweep clean. **All twelve BC citations verified by content**, slicing each §3.x by the next subsection id: §3.4 *Why Robots Don't Drive Straight* carries the answer's own vocabulary (manufacturing, windings, friction, curve, slower), §3.10 carries "power switch" twice, and so on down. Two control runs with landed-injection asserts: stripping one `data-bc-skill` fails §25.2 with the exact count mismatch; reintroducing `STOP & PROCESS` fails on the retired name. Both restore clean.

## WHAT SHIPPED THIS BATCH (S73)

**1. L02 v02.16.0 → v03.0.0 — the structural renumber, cut.** §3.2 *Understanding Each Section* (29,833 chars) lifted whole into a new **§5 The Code**; new **§4 Hardware — Meet Your Buttons** authored in the empty slot (a Meet Your Buttons table naming A/B/C, the OLED and the yellow LED, an explicit "nothing gets added this lesson" opener per §4.4 Rule 1, and a 📘 Note that the Serial Monitor is not a robot part); old §5 Build It → **§6** with *Getting Ready* folded into its opening; old §6 *Make It Yours* retired as a section. Anchors, HTML comments and PART subtitles reconciled. **No nav-pill edit was required** — the strip was already canonical.

**2. §3 closed to 3.1–3.6.** DJ ruled close the hole rather than leave the lettered sequence. `3.2b/3.2c/3.2d` → `3.2/3.3/3.4`, old `3.3/3.4` → `3.5/3.6`; ids renumbered to match (a two-pass rename, because `section-3-3` collided with itself). The unnumbered *How setup() and loop() Work Together* sub-head travelled into §5 and its id went `section-3-2-timeline` → `section-5-timeline` so it stops claiming a section it no longer sits in. Zero inbound links from any other file — verified book-wide before touching ids.

**3. Fifteen citations re-pointed, and one that was wrong before the renumber.** §3.2→§5 ×6 · "§5 Step N"→"§6 Step N" ×3 · §3.3→§3.5 ×3 · three prose refs. Then every citation was checked against the section that now holds its answer. **BC01 item 3 cited §3.2 for the function prototype and §3.2 never taught it** (prototype: §3.1 ×9, build steps ×8, lifted block ×0) — a defect that shipped green in S72 and would have shipped green again. Re-pointed to (§3.1, §6 Step 7), matching the sibling prototype question. §3.1 refs deliberately untouched.

**4. "Make It Yours" folded into §9 as prose, de-duped (DJ ruling).** §6.12a already governs the format: open-creative → prose inside the card, no panels. It landed as a prose block rather than a numbered card, because a pick-one menu called "Challenge 7" would give "did you finish Challenge 7?" four answers — the §4.1 disease. Two of its four options were already §9 cards with full pseudocode and solutions; DJ ruled drop the duplicates. Add Color and Animated Welcome survive, with the Serial.println accessibility 💡 Tip. Placed after Challenge 6 and before the CODE SWAP, which stays last in §9.

**5. Bible v8.58 → v8.58.1.** §4.4's non-conformant table was written at S72 against work that had only been specified; attribution corrected to "L01 fixed S72 · L02 cut S73". The citation-verification rule recorded in the same entry.

**6. Verification.** All **21 gates PASS**; `pill_sweep --audit` clean (6 pills, 0 old strings). Two control runs with landed-injection asserts per §24.6b/c: a dropped `</div>` in the new §5 fails 3 gates and restores clean; a stripped BC01 §-citation fails §25.2 and restores clean. Both prove the gates are reading the new content, and both confirm what the gate still cannot see — that a citation points at the *right* section.

## WHAT SHIPPED THIS BATCH (S72, part 2 — structure)

**6. Bible v8.57.1 → v8.58 — §4.4 THE SKELETON IS MANDATORY.** The Core 10 are not a menu. A skeleton section whose job comes up thin still appears and says so (§4 Hardware in a lesson that adds no parts). Lesson-unique material folds into the nearest section instead of becoming a new numbered one. "Does not apply" stubs everywhere: REJECTED, with the reason recorded. §8A: CONDITIONAL, unchanged. Both non-conformant lessons are tabled in the subsection, and the §15.2 dividend is recorded — renumbering L02 makes the *existing* Maker wording ("if Section 6 has N steps") true book-wide instead of patching canon to fit one outlier.

**7. L01 v03.9.2 → v03.10.0 — §4 conformance, no renumber.** The pill said "4. Hardware" and the comment said SECTION 4: HARDWARE SETUP; only the visible header said "Install the Tools". Retitled to *Hardware & Setup — Meet Your Robot, Install Your Tools*, and opened with a **Meet Your Robot** table naming Button A, the OLED, and the yellow LED — the three parts L01's code touches — plus a line on why everything else on the board is idle. Zero anchor, pill, or Maker impact.

**8. L02 restructure: specified, measured, NOT cut.** Full plan in `ZUMO_L02_RESTRUCTURE_PLAN.md`.

## WHAT SHIPPED THIS BATCH (S72)

**1. L02 v02.15.2 → v02.16.0 — the first Brain Check conversion.** Four blocks in Type 10 livery with anchors `brain-check-01..04`, Mark-done toggles, the skill-gated BC02 (7 tappable ☐ items, `data-bc-skill`), and the byte-identical column block copied from L01. BC01 at the §4/§5 seam as a standalone block between panels (the L01 post-fix shape — never nested inside a banner div). Moderate bump: hidden comment + both visible banners.

**2. The STOP & PROCESS block was redistributed, not deleted.** Its ten prompts split by job per §25.2's recall-vs-apply rule: three recall prompts became Mental items, six apply prompts became Knowledge Check items, one personal prompt became a Reflection. The fourth old Reflection prompt ("explain the Code Anatomy to a friend") is preserved as the **Canvas variant stem** on Mental item 1 rather than as a duplicate question. Retired names now read zero in L02.

**3. CODE SWAP relocated (DJ ruling).** Out of §10, into the end of §9 — between the challenges and the exit. Pure move: div counts unchanged, byte delta +1. Its partner-code notebook question followed it. **L02 is the only lesson in the book with a code swap** (grepped book-wide), so this is a placement, not a construct rollout.

**4. Achievability reviewed and cleared without an edit.** §25.10 requires every skill behind the BC02 lock to be earnable by a student whose build went perfectly. L02's chance-dependent-looking item is already forced by §5 Step 4 and Step 7, both of which stage compiler errors on purpose.

**5. Two S71 paperwork drifts corrected in this regeneration:** the status prose read "book_gates v1.5→v1.6" against a live v1.7, and the S72 handoff's open ritual said the gate file was v1.6. Every version on the line above is grepped from its file.

## WHAT SHIPPED THIS BATCH (S71)

**1. Bible v8.54 → v8.55 — §25.10 BRAIN CHECK (new subsection) + §8 Type 10 Knowledge callout registered.** Family name, numbering, livery, anchors, the column, localStorage check-off semantics (tracker ≠ grade), icon-pair rules (gray-not-red rationale, no-dark-backing, colorblind-safe by glyph), and the rollout rule: blocks + column land together per lesson, never separately.

**2. L01 v03.8.1 → v03.9.0 — the Brain Check reference lesson.** Four blocks renamed `BRAIN CHECK NN · CONSTRUCT — subtitle`, re-skinned Type 10, anchored `brain-check-01..04`, each closing with a Mark-done toggle; the Mental block un-nested from the §6 banner (white-on-white answers defect killed); §6 banner rebuilt to the canonical §7 shape; column + self-hydrating script added before the build banner, bounded by `BRAIN CHECK COLUMN START/END` markers; hidden version + both visible banners bumped (moderate).

**3. `images/BrainGear_Incomplete.png` + `images/BrainGear_Complete.png`.** DJ-authored artwork; incomplete recolored red→gray `#454545` and rebuilt as single-color-plus-alpha so interiors are transparent like the green (S71 QA: zero opaque light-interior px in both, zero red residue, stroke contrast 9.59:1 on white / 8.00:1 on the callout bg).

**4. book_gates v1.5 → v1.6.** §25.2 gate extended with §25.10: converted lessons must carry all four anchors, Type 10 wrappers, and the column block. Control-run four ways — pre-Brain-Check L01 (FAILS), stripped anchor (FAILS), de-indigoed wrapper (FAILS), removed column marker (FAILS) — every injection asserted to have landed before its run counted (S70 addendum honored).

**5. LIVE.md staleness from S70 fixed in this regeneration:** the status line's "All 19 gates" (written mid-S70 before v1.5) and the duplicate `Maker v2.45` in the versions line.

**6. Skill gate (late-S71, DJ-ruled).** Brain Check 02's ten ☐ items became tappable (`data-bc-skill`, per-browser state `bc_LNN_sk`); the block's Mark-done button locks — gray, 🔒, no-op — until all ten read ☑. Lock gates only the transition to done; undo stays free. Bible v8.55→v8.56, book_gates v1.6→v1.7 (glyph/tag parity, control-run), L01 v03.9.0→v03.9.1.

**7. Gated-item achievability (late-S71).** DJ's "BC02 will be the hardest" observation surfaced a gate-created defect: skill item 10 ("identify and fix an upload error") was un-checkable by any student whose build worked first try — the lock had promoted an unchecked box into a blocker on luck. Fix per DJ ruling: a 60-second Break-It-On-Purpose rep at the end of §6 Step 6 (power off → upload fails → read the error → power on, fix), so every student earns item 10. Canonized as §25.10 achievability (review rule). Bible v8.56→v8.57 · L01 v03.9.1→v03.9.2.


## WHAT SHIPPED THIS BATCH (S70)

**1. Bible v8.52 → v8.53 — §25 THE EXIT-REGION CONSTRUCTS, THE READING QUIZ & PAGE CANON (new section, nine subsections).** The four constructs and the recall-vs-apply split (§25.2) · the reading quiz — *easy if you read, hard if you didn't*, every item answerable from a single stated fact and naming its §, closed-book so items ship as rehearsal/variant **pairs**, 48–80 of them, authored inline as `QUIZVARIANT` comments while the § is open, **book first and Canvas after** (§25.3) · warm-ups L02–L16 and the spiral aiming rule (§25.4) · objectives rewritten *from* the Technical Skills checklists (§25.5) · header/footer/hidden-banner canon and the copyright reasoning (§25.6) · **§9 is the hands, §10 is the head** (§25.7) · caps (§25.8) · **§25.9 STILL OPEN**, written deliberately so this section cannot read as finished when it is not.

**2. §5b rewritten — the hidden build banner supersedes the v8.44 both-visible-homes rule.** Home 1 is the header hero; home 1b is an HTML comment before `</body>` carrying version, date, page title and the callout-standard stamp. Strictly better than what it replaced: a visible footer number can rot in front of students, a hidden one cannot.

**3. L01 built as the §25 reference (v03.7.0 → v03.8.1).** Mental Knowledge Check — **5 items, reveals, every one § -cited** — at the last seam before hands-on work; §10 Knowledge Check at 4 items; Reflection at 3 prompts, no reveal. The old 10-question block was redistributed, nothing deleted, two prompts added. Every candidate item was verified against the prose before placement: `setup()`/`loop()` is taught in §5.3–5.4 with **zero** mentions in §1–3, and `loop()` appears once in passing — which is why the boundary moved from "§1–3" to "the whole reading".

**4. All 17 pages made structurally identical.** Seven footer shapes → one; `<footer>` elements the first locator never scanned; L02's stray "— End of Lesson 2 —"; `going_deeper.html` given the canonical hero and footer and its visible version hidden (**v01.1.0**). Footers are built from the **header hero title**, after finding **three** live title sources disagreeing on L01, L02, L03, L08 and L15.

**5. DEEPER pill added to the §6.5a strip, all 16.** Going Deeper was reachable from only **7 of 16** lessons; nine were a dead end. Text pill, not an icon — the row is 0.78em and an emoji renders ~9px and turns to mush, and there is no hover tooltip on mobile. The `going_deeper links canonical` gate caught the first attempt using `../going_deeper.html`; canon is the full Pages URL.

**6. book_gates v1.3 → v1.4.** `§25.6 header/footer/hidden banner identical across all 17` and `§25.2 converted lessons conform to the four exit blocks`. §25.2 is **scoped to converted lessons** — it binds a lesson only once that lesson has a Mental block, so the fifteen unconverted lessons pass legally rather than by a tuned threshold. Control-run both ways: FAILED on the pre-session clone; FAILED on a stripped § citation, a 6th Mental item, a retired name left in place, and a one-character footer drift.

**7. Not done, and why.** No warm-ups outside L02 · spiral aiming rule not applied · objectives not rewritten · bonus challenges still in §10 · L13/L15 still have no exit block · title divergence untouched · `going_deeper` footer contrast ≈3.3:1 on its dark background and its hero title duplicated. All listed in Bible §25.9.

**8. THE REAL DEFECT WAS FILE LOCATION, AND IT IS NOW GATED (Bible v8.54, §25.6a).** Two pushes in one session shipped the right bytes to the wrong folder — `going_deeper.html` into `lessons/` (23 lesson links and the index kept serving the stale root copy) and then `tutor.html` to the root (the live tutor stayed unversioned; the new file was an orphan nothing linked to). Both looked like clean pushes; no gate could see them, because every gate checked contents. **book_gates v1.4 → v1.5** adds `§12/§23 site layout` — the exact set of 21 HTML pages and their paths, so any stray, any missing page, any page at the wrong path FAILS. Control-run three ways, including a reproduction of the Going Deeper incident (fails as STRAY **and** MISSING).

**9. Web tools got in-file version lines (§5b rewritten).** `timer.html` and `tutor/tutor.html` had **none at all**. `newproject.html`'s changelog opens with `v2.18` against a live `v2.45`, so a naive grep of its head returned a number 27 releases stale — the v3.0 ghost. And the Bible's own web-tool sentence read *"Current: timer v1.2, Maker v1.3"* while the Maker was at v2.45. All four now open with a canonical line, gated by `§5b web tools carry an in-file version line`. Baselines are **labelled as baselines** in each file's header — timer v1.3.0 · Maker v2.45.1 · index v1.3.0 succeed the last recorded numbers; tutor v1.0.0 is a declaration, since no number for it ever existed.

**10. index.html gained the site credits line** (§25.6a): `© 2026 RoboLore · Written and compiled by DJ Weymuth and Claude AI`, beneath the existing site line. The front door is where a copyright notice does its real work. The other three tool pages are deliberately left without chapter furniture — they are utilities, several rendering inside iframes.

## WHAT SHIPPED THIS BATCH (S69)

**1. L05 proximity prose reconciled to the S68 hardware truth (v04.7.1).** S68 redrew GRAPHIC 5.1 to side-facing detectors and added §3.4's series-wiring fact, but three prose sites still carried the old model. The live one that mattered: **§4.1's highlighted "Key insight" asserted that objects on the left "reflect more light from the left LEDs"** — direction attributed to which LED team fired, which is exactly the misconception §3.4 was written two paragraphs earlier to kill. Rewritten: the emitters flood, direction comes from **which detector answers**, and the one place an LED team does carry direction is the front detector read twice (§4.2). Also **§8A.1** said the front has "one IR receiver … with two forward IR emitters" — undercounting four emitters and hiding the series teams; now scoped to the blade pair with a §3.4 back-reference. **§4.2** moved to "LEFT-team" vocabulary and now bounds "slightly off center" at FRONT's ±19°, past which it is §3.4a's dead spot. **GRAPHIC 5.5 gained its missing body caption** — every neighbouring hardware figure had one.

**GRAPHIC 5.5 needed no redraw** — the S68 queue's suspicion that its cone angles might contradict the new 5.1 was checked by extracting tick bearings from the SVG: LEFT −90.0° · FRONT 0.0° · RIGHT +90.0°, middle emitters ±90°, blade emitters ±29° forward. Already correct. *Logged because §24.6c now requires it: that suspicion was relayed in the voice of a defect and was not one.*

**2. Timer coverage — within-lesson gaps closed (L03 v03.12.0, L04 v04.5.4).** **L03 Bonus Challenge 4 "Braking vs. Coasting"** was the only one of six without a timer; added at **6 min** per DJ ruling, matching BC5, the other two-run measurement challenge. Deliberate placement deviation: every sibling puts the iframe directly under the `<h3>`, but BC4 is the only one with a ⚠️ Space-check panel in that slot and a right-floating iframe would overlap it, so the timer sits after the warning box, beside plain prose like its siblings. **L04 Challenges 4 and 5** had no timer while C1–C3 did; added at **4 min** each (C2 Deep and C3 Moderate already use 4). Coverage is now: warm-ups 4/4 · TRY IT 10/11 (`2.t7` "Blink N Times (Advanced)" left deliberately untimed — it is the only card whose heading also carries no minute count, and two omissions agreeing is not an oversight) · bonus 12/12 · main challenges 0 in L02/L03 by convention, 5/5 in L04 by DJ ruling.

**3. Bible v8.50 → v8.51 — §24.6c AN AUDIT GREP IS AN UNGATED GATE.** Four parts: control-run the grep against an independently visible case before the number becomes a finding · never infer structure from label text, check what element the match is attached to · case-insensitive by default, since book vocabulary varies by lesson and era (`STEP`/`Step`, `CONFIGURATION`/`CONSTANTS`, "Coach's Tip" vs bare §6.6a labels) · report findings as **VERIFIED** or **SUSPECTED**, with queue and handoff items entering the next session as SUSPECTED until re-checked. Records the standing pressure it works against: a five-item audit reads as more valuable than a two-item one, so weak signals get promoted — against DJ's rule that a wrong finding costs 3× a blank one.

**4. All 12 Bonus Challenges tagged (L02 v02.14.0, L03 v03.12.0, `tutor/tutor.html`).** `2.b1`–`2.b6` and `3.b1`–`3.b6`, `data-kind="bonus"`, placed on the `<h3 id="bonus-N">` itself so the picker label is the element's own self-naming text (§4.3), matching how warm-ups and mysteries are tagged. New **Bonus Challenges** optgroup in the tutor between Challenges and Warm-Ups, following the L11 `mystery` precedent of its own kind plus its own group rather than falling through to "Other". Census: 87 challenge · 12 bonus · 12 tryit · 4 warmup · 4 mystery = **119 unique markers, zero duplicates.**

**5. Not done, and why.** The §24.6c gate was withdrawn (see Status). L02's `2.t7` left untimed as deliberate. L03 C05's inline `%` box remains as authored — DJ reviewed the rendered text this session and did not read it as duplicating §8A.6, and it sits ~380 lines below that section as a point-of-use reminder.

**6. THE LESSON STRIP — book-wide, all 16 lessons (§6.5a, DJ ruling "Love c").** DJ's ask: no easy way to jump between lessons from inside one. Four options were prototyped on the real L05 header (prev/next pills · dropdown · number strip · titled drawer); DJ picked the strip. Every sticky nav now carries a second thin row — LESSON · 01–16 · ⌂ home — squares in neutral rgba-white so they never collide with the section color code, each with the lesson's canonical title as tooltip, current lesson a solid white square. Ships as **one byte-identical block in all 16 files**: static links (works with JS off) plus a self-hydrating script that derives the current lesson from the URL, bounded by `LESSON STRIP` marker comments. Renumber or L17 = one block edit re-applied. Explicitly outside the v8.21 nav-button ceiling, which governs the section-pill row only. **book_gates v1.2 → v1.3** adds `§6.5a lesson strip present and byte-identical in all 16` — control-run both directions per §24.6b: FAILED on the pre-strip clone (16 missing) and FAILED on an injected one-character drift ("differs") before being trusted. Moderate bump on all 16 lessons, both banners moved per §5b. All 17 gates PASS.

## WHAT SHIPPED THIS BATCH (S68)

**1. The panel-close repair (8 lessons).** L01, L12, L13, L14, L15, L16 — orphaned `</div>` after `</html>` relocated to close the Image Index panel before the footer, matching the L02/L11 reference shape. L06, L07 — close present but late, so the footer rendered *inside* the panel; L07 additionally had its footer above the Back-to-top and was reordered. Every edit count-preserving; div depth now returns to 0 at `</body>` in all 21 site files and nothing follows `</html>` anywhere.

**2. book_gates.py v1.2 — parse, not count.** Removed: the two narrow S68 checks. Added: `structure: HTML parses to the intended shape` (html.parser tag stack over every site file, strict on div/details/table/section/pre/a/span/ul/ol/h1–h4, lenient on optional-close tags, plus a nothing-after-`</html>` assert) and `structure: end matter sits outside the section panel` (semantic — walks the Image Index panel and fails if `<hr>` or the gradient footer is inside it). 16 gates total.

**3. Bible v8.49 → v8.50 — §24.6 STRUCTURE IS VERIFIED BY PARSE, NOT BY COUNT**, with §24.6a (a parser is necessary and not sufficient — ask what a well-formed-but-wrong version looks like and gate that too) and §24.6b (control-run every new gate against the unfixed source; a gate that passes everywhere it has been pointed has proved nothing).

**4. GRAPHIC 5.1 redrawn — it modelled hardware that does not exist.** The old figure fanned all three proximity cones forward at ±25.5°. Pololu 0J63 §3.5: the proximity sensors are named after the directions they face — left, right, front — and §3.6: the middle-left and middle-right IR LEDs sit inside the tracks between the wheels and emit to the left and to the right. DJ supplied an annotated board photo confirming it. New geometry: LEFT −90.1° · FRONT 0.0° · RIGHT +90.1°, side half-angle 17.9°, front 18.7°; scene changed from "box far left" to "wall alongside", since an object 25° off the nose was never LEFT's to see. Caption, alt text, image-index row and the §1 "objects in its path" line all updated to match. **Note the failure mode: four independent mechanical checks (bearings, render, img placement, alt text) all passed, because the drawing was internally consistent. This is exactly the §24.6a class — no gate can catch a well-formed diagram of the wrong robot.**

**5. L05 gains three correct front-sensor-array photos.** An earlier candidate was caught and reverted before shipping: it was the **Zumo Reflectance Sensor Array (#1419, six sensors, Zumo shield for Arduino)**, not the students' **Zumo 32U4 Front Sensor Array (#3122, five line sensors + three proximity)**. Shipped instead: **IMAGE 5.6** (§4.1) — the three proximity receivers with the direction each faces, the photographic proof behind the 5.1 redraw; **IMAGE 5.5a/5.5b** (§7.3) — factory (1·3·5 live) vs five-down (1–5 live), filling a real gap since 5.4a/5.4b only show the jumpers from underneath. All EXIF-stripped, Pages-absolute URLs, credited "Photo: Pololu, annotated."

**6. L03 — the last open teaching gap closed.** New **§8A.5 (arrays)** and **§8A.6 (modulo `%`)**, closing the gap the Bible logged at v8.41 ("L03 C05 needs arrays + modulo, neither in L03 prose"). Quick Reference gains `qr-array` and `qr-modulo`; C05's "Where to look" pointed at its *own hint* and now lands on them. C05 re-rated Tough/Deep → **Tough/Moderate** — grasp axis only, so the doing-axis ramp is untouched (L03 stays 1.88).

**7. Going Deeper pointers → L07, L08, L12, L15, L16** — exactly the lessons the six entries name in their "Back to the book" lines that lacked one. Canonical absolute URL, so the `going_deeper links canonical` gate still holds. §23.2 verified: all six entries name their source lessons.

**8. Verified-already-done (no work needed).** `data-kind` is explicit on **all 87 cards** (checked on the same element as `data-challenge`, zero missing) — strike the queue item. L03's "1000 ms = 1 second" explainer is live in §3.7; the power-on Tip and the AI-autocomplete Warning are both live in §7 and already carry **bare** labels per §6.6a, which retired "Coach's Tip" in S61 — the queue entries were written in pre-S61 vocabulary.


**9. L05 proximity hardware, finished properly.** DJ pushed past the redraw into the hardware itself, and three more things landed. **§3.4 gains the series fact:** front-left and middle-left are wired in series on one current path, so lighting either lights both — a wire, not a software choice, which means the emitters flood and *the direction you get back comes from which detector answers.* **New §3.4a + GRAPHIC 5.7 — THE DEAD SPOT:** Pololu measured a significant dead spot between the front sensor and each side sensor; with FRONT at ±19° and the side cones centred on the flanks, that is **two blind wedges from roughly 19° to 72° off each side**. The figure hatches the wedges and shows the behavioural trap as a three-step strip — see it on the left, turn to face it, lose it mid-turn, keep turning, FRONT picks it up. Warning box: a zero *while turning toward what you just detected* is not a broken sensor. **Flagged forward to L10** (DJ ruling), where a matching back-reference explains five-down makes it permanent — the side receivers are gone, so everything outside FRONT's ±19° is invisible and a block 40° off the nose reads a clean 0 from a working sensor. **IMAGE 5.7 / 5.8** show all four emitters: the forward pair in their holder on the blade, and the middle pair on the bare board where the tracks normally hide them, with the `A1 = VBAT/2` silkscreen visible beside the very LEDs that pin selects. **L05 v04.7.0** (banner 04.7) · **L10 v02.4.2**.

*The dead-spot geometry was not drawn deliberately — it fell out of using the correct angles. The old ±25.5° fan had the three cones nearly contiguous and concealed the gap entirely, so the redraw surfaced a real behavioural fact as a side effect of being accurate.*

---


## WHAT SHIPPED THIS BATCH (S67)

**The assessment.** Book-wide challenge-move scan, L01→L16, means recomputed by script on the canonical 1–5/1–3 scales. Findings: nine spiral spines already live in the content (square ×5 touchpoints, counter ×6, battery, motion-profile, proportional, state-cycling, obstacle, centering, trust/debounce) — all unmarked past L06; spiral markers are absent L07–L16 (worse than the S66 log's "L10–L12"). Exactly one move helps the ramp; every other candidate was rejected with arithmetic (moving L04 C5 undoes S66's L04 fix; moving L10 C5 relocates the dip; pulling L08's tuning cards starves TDP table A4). Both docs are in the repo root.

**The move (L06 v04.10.0 · L07 v04.6.0 · Maker v2.44).** C8 card block (10,704 bytes) removed from L06 clean — zero trapezoid references remain, no anchors dangled, no challenge-count prose existed. Adapted card inserted after L07 C6 as `data-challenge="7.7"` / `id="challenge-7"`, Advanced/Deep pills unchanged, with count==1 asserts on every string edit. Template re-stepped: Step 1 declare in RobotMotion.h, Step 2 implement in RobotMotion.cpp after driveDistance(), Steps 3–4 test and observe. Dependency-verified against L07's finished payload before the move: static averageCounts() lives in RobotMotion.cpp (same file — in scope), TRIM/DRIVE_SPEED/COUNTS_PER_CM in RobotConfig.h, hardware objects extern'd via RobotSensors.h. §8-covers-§9 holds — every construct in the solution is taught by L06.

**Not harness-compiled this session** (AVR toolchain download blocked in the work environment): the solution body is byte-identical logic to the L06-proven solution; the only new code line is the header declaration. Bench-verify the L07 build + trapezoid compiles green at first classroom opportunity.

**THE MARKING BATCH (second S67 batch — L07–L15, nine minor bumps).** Fourteen spiral markers inserted, the back half's first coverage: every marker's claimed relationship was verified against the actual card/section text before insertion, and two proposed markers DIED on that check (L10 C4 is a back-up phase, not debounce — the "hysteresis" claim was wrong; L08 C2's card text doesn't touch centering — that marker moved to §3 prose where the bang-bang example IS the L04 Centering Game). Format: the established `Builds on:` box + spiral_star_NN.svg, card markers as a band after the work-in box, prose markers after their heading. CARDS (8): L07 C6 (⭐06+03 square) · L09 C3 (⭐06+04) · L10 C3 (⭐05 counter) · L11 C3 (⭐07 trapezoid decel — the move paying off same-session) · L11 C4 (⭐03 TRIM) · L13 C1 (⭐09 state machine) · L13 C2 (⭐10) · L14 C3 (⭐10). PROSE (6): L08 §3 bang-bang (⭐04) · L08 §3.1 P-formula (⭐05 — `beepInterval = 700 - (value * 100)` quoted exact from L05 C3) · L09 §3.4 (⭐03 Variable Speed Test) · L10 §1 (⭐05) · L12 §7E (⭐06) · L15 §1 (⭐08). Coverage now: L02–L15 all carry at least one marker; only L01 (nothing prior) and L16 (no cards) are zero. Minor bumps L07 v04.6.1 · L08 v04.4.1 · L09 v05.3.1 · L10 v02.4.1 · L11 v02.6.2 · L12 v01.6.1 · L13 v02.5.1 · L14 v02.7.1 · L15 v02.5.1 — hidden line only per §5b, visible banners unchanged. All 14 gates PASS, pill sweep clean. Format choice is **Inferred** (the S67 moved card used it and DJ pushed without objection) — one word reverses it.

**THE L08 CAPSTONE (third S67 batch — L08 v04.5.0 · Maker v2.45).** DJ-approved design shipped: **Challenge 6: The Racing Line** (Advanced/Deep) — a second proportional controller on the same error: `speed = BASE_SPEED - KS * abs(error)` with a `MIN_SPEED` floor, steering P unchanged. Closes C1's own loop (C1's max BASE_SPEED was a straights-vs-curves compromise; C6 removes it), spirals L05 C3's beep formula (⭐05 Builds-on band), slides where C5 stepped (bands → ramp), and hands L15 its on-ramp ("the error gets a second listener; there it gets a memory and a forecast"). Every construct already in L08's own taught code (constrain/abs/millis verified in the finished payload). New constants land in RobotConfig.h — one more architecture rep. Card in C5's exact shell: Goal/Logic/Template, four blanks, worked reveal with the throttle arithmetic (KS 0.03 → max slowdown 60 at error 2000), three failure modes (error vs abs(error) · no floor · KS-before-Kp), and the tuning ritual ending with "raise BASE_SPEED past your Challenge 1 number." Maker: one `racing_line` finished-preload kind row — zero payload authoring. **Ramp: L08 2.00 → 2.50, and L01→L10 is now fully monotone non-decreasing (1.36 · 1.67 · 1.88 · 2.00 · 2.20 · 2.29 · 2.29 · 2.50 · 2.50 · 2.60) — the audit's opening-and-middle goal is DONE.** Remaining dips book-wide: L11 (priced-in) and L14's mild step after L13. Gates 14/14 PASS, pill sweep clean.

**Shelved, not lost:** six L12–L14 card specs (`ZUMO_SHELVED_CARDS.md`) — DJ ruled Job B (ramp), and those cards all lower the means of the three hardest lessons in the book. L16's zero challenge cards flagged, unruled.

---

## WHAT SHIPPED THIS BATCH (S66)

**The scale correction.** The prior audit table's means only reproduce under a four-point doing mapping (Hard=3, Advanced=4); §6.12b's canonical order is five tiers with Tough=3. Recomputed 1–5, L04 was **2.80** — second-hardest doing in the book at position 4 of 16 — not the recorded 2.40. Every shape finding survived the rescale.

**L04 (v04.5.3).** Four attribute + visible-pill re-rates, each scoped to its own card block with count==1 asserts. C1 kept Easy/Light. Grasp axis untouched (2.20) — L04's load is cognitive and the split pill exists to say so. One flag logged: C2's Deep concept (arrival-vs-presence) is taught inside the card, not §5/§8A prose; ruled covered, not a gap — and it is load-bearing downstream (L09's transitions, L13's literal "just arrived").

**L07 (v04.5.2).** C03 doing Medium→Easy. Honest re-rate deepens the recorded sag — deliberately: it exposes that L07 needs a harder capstone rather than a flattering label.

**L11 (v02.6.1).** Two cards appended after C3 (markers 11.4/11.5, `data-kind="challenge"`, `data-reveal="solution"`, L11's own card strata per §6.12c). Banners 02.5→02.6 both homes; v02.6.1 is the post-delivery post-it-method revision (DJ-ruled measurement change). New bench item: verify C4's double-TRIM mirror-drift on a real gap before classroom use.

**Remaining audit findings (carried):** L07–L08 sag now reads 1.83/2.00 doing — needs harder capstones, Part-B-scale authoring. L12–L14 still at 3 challenges each. DJ's own tier pass still to come.

---

## WHAT SHIPPED THIS BATCH (S65)

**L02 depth pass — five additions.** All five came from DJ's own read of the lesson. Brace style
(Allman vs K&R, book is K&R at 837 vs 2) plus a ⚠️ WARNING on the one-liner trap — the second line that
silently escapes a braceless `if`, compiles clean, and misbehaves. A full `F()` explainer replacing a
four-sentence note. Short-circuit evaluation, which had **zero hits book-wide**. "Why, not what" pulled
forward from its only prior appearance in L10. And the semicolon habit, including the part that actually
confuses people: the compiler reports the line *after* the mistake.

**The `F()` gap.** 692 uses across 15 lessons, one explanation. Now a proper LEARN section (flash vs SRAM
table, the AVR copy-to-SRAM behavior, the desk-and-bookshelf analogy, and the fact that SRAM overflow gives
**no error at all**) plus a `qr-flash` Quick Reference row and two placed reminders. Reminder placement was
measured, not guessed: only **L12** (which already names 28,672 and watches the linker discard dead weight)
and **L16** (the wall) have memory prose to attach to.

**Timers were the miss worth recording.** `timer.html` is a **live countdown iframe** (`?min=`/`?label=`),
and L02 already had ten on its Challenge and Bonus cards. The build-step challenges had only the *text*
"CHALLENGE (1 minute)" with no widget — and the first S65 pass added more text labels, not timers. Ten real
iframes now cover every build step. Step 2 already had its heading; what it lacked was the timer.

**Going Deeper (`going_deeper.html` v01.0.0).** Six collapsible entries: ASCII/binary/baud · what `F()`
really does (Harvard vs von Neumann) · the four-stage build chain · translation units and why eight files ·
fixed point applied to Kp · class vs instance. Every entry anchors to a chapter and closes pointing back at
it. Most of the offered general-C++ material was **rejected** for having no anchor.

**Terminal color canon (Bible §22).** SUCCESS `#6a9955` (DJ-ruled — deliberately the comment green, not the
terminal's brighter true green), errors `#f14c4c`. The diagnostic line goes red; the source echo and caret
stay plain, because L02's "look at the line above" rule depends on the student judging that line themselves.
Of 71 blocks containing the word "error", only **11** are console output.


**Also shipped S65 — the "Challenge" name collision, resolved.** L02 had three different constructs all
called Challenge: Section 1 warm-ups (1–4), inline green practice boxes, and Bonus Challenges (1–6). "Did you
finish Challenge 3?" had three defensible answers. Worse, the AI Tutor queries `[data-challenge]` and **only
the 6 Bonus cards were tagged** — a student asking about a warm-up got the wrong card back. Renamed:
warm-ups → **Warm-Up N**, inline boxes → **TRY IT (n minutes)**, Bonus Challenges unchanged (§4 vocabulary
canon). Every practice construct now carries `data-challenge` + `data-kind`, with suffix `w`/`t` so a warm-up
can never collide with a card number. Audited book-wide: gaps existed **only** in L02 (15) and L04 (1) — both
closed; **104 unique markers, zero duplicates**. Canonized as Bible **§4.1** and **§4.2**. L02 v02.13.0,
L04 v04.5.1.


**⚠ S65 self-inflicted bug, caught and fixed same session.** The marker sweep above tagged 11 L02 TRY IT
boxes whose visible text was only `🎯 TRY IT (1 minute)`. The AI Tutor builds its dropdown from each tagged
element's `textContent` — so **six options were byte-identical** and a student had no way to pick the right
one. The tagging was right; the labels made it unusable. Every TRY IT now names its step and task
(`🎯 TRY IT — Step 5: Longer Blink (1 minute)`), and `tutor/tutor.html` groups the picker by `data-kind`
(Challenges / Warm-Ups / Try It / Mysteries). **A unit with no `data-kind` is still treated as a canonical
challenge card**, so all 14 untouched lessons are unaffected — verified across the book, nothing dropped,
nothing in "Other". Canonized as Bible **§4.3**.


**L01/L02 sweep at S65 close — two real finds.** (1) **§5b banner drift**: L02's rename bumped the hidden
comment to v02.13.x but left both visible banners reading "Version 02.12" — a minor-version bump is
moderate-or-larger under §5b and the banner must follow. Book-wide gate re-run: **all 16 now agree** across
hidden comment and both visible homes. (2) **Going Deeper was unreachable from inside the book** — linked
only from the index tile, so a student mid-lesson never saw it, despite its six entries being written
specifically against L01/L02/L07/L08/L12/L15/L16. A pointer box now sits at the end of the Quick Reference in
L01 and L02, each naming the entries relevant to that lesson. Also confirmed correct-as-is: L01 has **no
timers and no F()** because it teaches neither — its steps are install procedures, not timed practice, and
its 11 challenge labels are already unique in the picker.


**L01→L02 flow and accuracy re-check — three finds, all mine from earlier in S65.**
(1) **A published arithmetic error.** The new `F()` explainer counted `"Press A, B, or C"` as 17 characters /
18 bytes; it is **16 characters / 17 bytes**. The ten-string total was wrong in the same way (180 → **170**).
Corrected in the prose and in the code comment. The percentage claim survives — 170/2,560 is still about
seven percent.
(2) **L01 promised something L02 does not deliver.** L01's "What's Next" asked *"What's the difference between
`=` and `==`?"* as a Lesson 2 hook, but L02 §3.2c deliberately defers that to Lesson 3 ("the one-character
typo that breaks it silently"). The question is a good hook, so it was kept and reworded to stop implying L02
answers it. Same defect class as §11's "§8A must cover what §9 requires", pointed at a cross-lesson promise.
(3) **L02's two visible banners disagreed on the month** — header read June 2026, footer July 2026. Both now
July, matching L01.


**S65 closes with a standing tool, per DJ: "be more consistent and fix everything."** Three times this
session a named fix left the same defect class alive elsewhere and DJ had to re-ask. **`book_gates.py` v1.0**
(repo root) now runs every machine-checkable Bible rule against the whole book in one pass — §5b version AND
date, §22 colors, §4.1/4.2/4.3, §6.12b parity, tag balance, timers, link resolution. Run it at session open
and before every delivery; an undelivered gate run = incomplete delivery. **All eleven gates PASS** on this
batch. Canonized as Bible §24, with two root-cause rules: gate the whole field, not the captured group
(the June/July date survived a "passing" version check); and a computed claim is verified by computation,
never recall (the 18-bytes error). New session ritual: `python3 book_gates.py` joins `pill_sweep.py --audit`
at open.


**The depth audit (per DJ: find what is "mentioned but without enough substance").** book_gates.py → **v1.1**
(+3 gates: cross-lesson promises, arithmetic, §16 constants — all PASS). New **`DEPTH_AUDIT_S65.md`** maps
the systematic findings for the rolling human read DJ is doing personally. Headline (verified): **the
teaching apparatus disappears at L11** — L11–L16 carry zero 📖 LEARN boxes and near-zero 🔑 KEY terms while
teaching the hardest material; mostly a marking fix, queued as its own arc. **L14 profiles thinnest in the
book** ("The Code Freeze": 8 words) and goes first in the read. Cleared as false positives after §11 line
verification: all bitwise/pointer "uses" (progress bars, `<<<` markers, pseudocode arrows), L06 §5.4
(genuinely teaches abs+ternary), L08 §5.2 (theory lives in §3). Open candidate: ternary `?:` may appear in
L03/L05 before L06 teaches it — needs line-level verify. Canonized §24.5.

---

## WHAT SHIPPED THIS BATCH (S64) — the split-pill sweep, complete

**The sweep.** L04–L15, 59 pills, converted to the two-axis split pill. With S62's L01–L03 the book is
now at **84 challenges / 15 lessons / 0 old pills**. Verified by `pill_sweep.py --audit`,
which is read-only and reports `SWEPT` / `not swept` / `*** MIXED ***` per lesson — a half-applied sweep
cannot pass silently.

**Why it was not a find-and-replace.** The same visual pill carried **nine distinct style strings** across
L04–L15 — same rendering, different CSS property order. Canvas strips `<style>` and `class=`, so every card
holds its own inline copy and every rebuild retypes it. Git shows the flips are single-commit and
lesson-clustered (L05/L12/L13 all changed together in `a3cd518`, the S59 Project B pilot): **strata, not
rot.** S63's note that "markup was uniform, zero variants" was true of L01–L03 only, because those three
share one stratum. Now Bible **§6.12c**.

**Teaching gaps found and fixed** (six, all the same class as the standing L03 C05 gap):

| Lesson | Gap | Fix |
|---|---|---|
| L04 | `bool` state across `loop()` passes — 0 prose hits, C02 needs it | **§8A.8 NEW** — runaway counter, edge vs presence, global-vs-local placement, hysteresis |
| L04 | `abs()` + deadband — 0 prose hits, C05 needs it | **§8A.9 NEW** — error carries size AND sign; why `error == 0` buzzes forever |
| L06 | polygon exterior angle — 0 prose hits, C03 says "you must calculate" | **§5.5 NEW** — 360÷sides, why the square hid the rule |
| L07 | "stub" used 9× in C05, never defined | one-line definition in the card |
| L08 | `map()` — appears **once in the entire book**, as a fill-in blank | **`qr-map`** Quick Reference row + C04 pointer repointed |
| L09 | `do…while` — supplied complete in C03, taught nowhere | **`qr-dowhile`** Quick Reference row + C03 pointer |

**Two near-misses worth recording.** `static` looked like an L09 gap (0 prose hits there) but is properly
taught in **L05** with a 🔑 callout — and L03's hit is "static friction", L06/L07's are the different
file-scope sense. `while(true)` looked absent from the book but appears **11 times in L06**; the raw-HTML
grep missed it because syntax highlighting splits the construct across `<span>` tags. Both are now §6.12c
rules: strip tags before grepping a construct, and check sibling lessons before declaring a gap.

**Structural repairs.** L02 and L12 shipped with only the HEADER version banner; both now carry the footer
one too, matching their own neighbours' format (L02 → `<footer>` like L03, L12 → gradient div like L13),
with the version derived from the hidden comment so the homes cannot disagree. **All 16 lessons now have
both §5b visible homes present and agreeing** — a first for the project.

**The progression, both axes** (lesson means, doing / grasping):

| L01 | L02 | L03 | L04 | L05 | L06 | L07 | L08 | L09 | L10 | L11 | L12 | L13 | L14 | L15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.36 / 1.36 | 1.67 / 1.50 | 1.69 / 1.62 | **2.40 / 2.20** | 2.00 / 1.80 | 2.25 / 1.88 | **1.83 / 1.50** | 1.80 / 2.00 | 2.17 / 2.17 | 2.20 / 1.80 | 2.00 / **2.33** | 2.33 / 2.33 | 2.50 / 2.00 | 2.33 / 2.33 | 2.71 / 2.57 |

Floor and ceiling are clean. **L04 spikes to 2.40/2.20** (third-hardest doing, sitting fourth) and **L07
sags to 1.83/1.50** — below L05, barely above L03, with L08 at 1.80 behind it. Challenge COUNT collapses
after L10: L11–L14 hold 12 between them, fewer than L01 alone, while **L11 pairs the book's highest grasp
mean (2.33) with its lowest count** — under-practiced rather than under-taught.

**Open, not fixed:** L15 C04–C07 ship with no template and no solution reveal (four of the hardest cards
give a stuck student only prose, and the AI Tutor nothing to strip). A stray `</div>` sits after `</html>`
in L01 and L12–L16 — malformed but browser-tolerated, balanced so no depth walk catches it.

---

## ALSO SHIPPED (S63) — the split-pill slash, halved

**The change.** `width: 8px; margin: 0 -4px` → `width: 4px; margin: 0 -2px` on all **25** live pills (L01 11 · L02 6 · L03 8). Markup was uniform — zero variants — so a single exact-match replace covered the book.

**The margin is structurally half the width.** The two halves close *over* the slash; halving the width alone would have opened a 4px gap. Any future change to one number must change the other.

**Verified:** div and span balance unchanged; a line-by-line diff audit confirmed every changed line is either a slash or a version comment, zero unexpected edits.

**Versions:** L01 v03.6.1 · L02 v02.10.1 · L03 v03.10.1 — hidden comment only; visible banners (`Version 03.6` / `02.10` / `03.10`) left alone, since a cosmetic change is a minor bump per §5b.

**Not applied:** DJ floated halving again to 2px — deferred, not done.

---

## WHAT SHIPPED THIS BATCH (S63) — the robot icon family

**Pushed:** `images/glowbots/` — 42 files, flat. 25 bordered (5 robots × 1254/256/128/64/52, RGB) · 15 glow (5 × full-1186²/256/128, RGBA) · 2 QA contact sheets. Verified byte-identical to delivery by fresh clone at commit `12867ea`.

**Buttons are bordered; images are glow** (DJ ruling). The border ring gives a hard silhouette that survives downsampling to 52 px; a transparent cutout does not.

**The build method changed.** S61 canon said to NEVER separate the robot from its glow, on the evidence of a failed attempt. S63 separated all five — including Balboa (open roll cage) and Zircon (black PCB), the two that rule predicted would defeat it. Two findings made it work:
1. **Edge-connected flood fill, not a brightness threshold.** Background = dark AND reachable from the crop edge, so interior dark pixels survive by construction.
2. **Cut the falloff, don't preserve it.** The glow is painted additively on black, so its outer falloff IS black; kept as soft alpha it renders as grey haze — invisible on dark, filthy on white.

**QA rule earned the hard way: check on white.** Three separate glow defects shipped in this session because every QA sheet was rendered on a dark background, where a transparent-cutout defect cannot be seen. DJ caught all three by eye and ultimately fixed three of the five masters in Photoshop; those became the reference, and 3Pi+/Balboa were tightened to match (they carried 57 px and 39 px of halo against the others' 0–1 px).

**Also shipped:** Bible **v8.42** — §21.3 rewritten (two outputs, two methods), §21.4 amended (Balboa's real problem is that it is the only *portrait* robot, not that it is open-frame), §21.2 colors re-tabled (canonical = spec, as-built = recorded generator drift; 3Pi+ is the Δ55 outlier), §21.7 new (live file inventory + uniformity spec).

**Open debts on this family:** border inset ships at 10–18 px against a 64 px spec (DJ: "leave them for now" — 64 remains the spec) · filenames are S63 working names, not a ruled convention · the two `QA_*` sheets are committed alongside real assets.

---

## WHAT SHIPPED LAST BATCH (S62) — the split difficulty pill · L01–L03

**Why two axes.** A single pill has to lie whenever doing and grasping diverge. L03 C08 Auto-TRIM Preview asks for COMMENTS ONLY — trivial to do — but requires reasoning about encoder differentials three lessons before encoders exist. Rated ADVANCED it warned students off a card they could finish in ten minutes; rated EASY it hid the only hard thing about it. Split, it reads **Easy / Deep** and both are true.

**The scales.** Doing: Easy `#4A6B22` · Medium `#9A6B10` · Tough `#B85425` · Hard `#8A2F18` · Advanced `#6B2545`. Grasping: Light `#4A7FB5` · Moderate `#185FA5` · Deep `#0C3F6C`. The doing ramp walks one direction around the warm wheel so order is legible without reading the words; grasping stays one blue family because warm-vs-cool is what signals the two halves ask different questions. Markup is inline-styles-only (Canvas-safe): a `display:inline-flex` badge with a skewed 8px white divider on negative margins, so the cut reads as one badge divided rather than two pills touching.

**Doing-axis re-rates (5).** L01 C11 Battery Check MEDIUM→**Easy** (the `if` ships pre-written; student fills two blanks) · L02 C06 Scrolling Text HARD→**Medium** (a `for` loop plus variable `gotoXY` — the HARD was a missing Template panel, not difficulty) · L03 C03 constrain() EASY→**Medium** (introduces a new function AND a named cap) · L03 C05 Variable Speed MEDIUM→**Tough** (arrays + index + modulo) · L03 C08 Auto-TRIM ADVANCED→**Easy** (writes comments only).

**Audit basis.** All 78 challenge bodies across L01–L16 were read against their pills before any edit; L01–L03 prose was grepped for every construct its challenges require. The full doing-axis audit found six mis-rates — the five above plus **L05 C01 Detection Counter EASY→Medium** (identical boolean edge-detection pattern to L04 C02, which is rated MEDIUM) and **L14 C02 Strict Mode EASY→Medium** (three lines of code, but the point is a trick question about `while(true)`). Those two are NOT yet applied — they live in L05/L14, outside this batch.

**⚠ OPEN TEACHING GAP (marked, not fixed).** **L03 C05 Variable Speed** requires **arrays** and the **modulo operator `%`**. Neither appears anywhere in L03 prose — verified by grep, S62. Rated Tough / Deep. The modulo explainer was already in the standing queue; **the array gap was not previously known.**

**Verification.** 25/25 pills matched one canonical shape before editing (zero strays). Bounded-scope script with `count==N` assert guards aborting before write. Visible-word diff vs. backups shows ONLY pill labels changed — no prose moved. Div and span counts identical in all three files. Both version homes bumped per §5b. Push verified by fresh clone with md5 match on all four files.

**Also shipped:** Bible **v8.41** — new **§6.12b** (the split pill, its colors, its markup, and the rating discipline), **§6.12** pill spec rewritten to point at it, **§20.2** gains `data-grasp="light|moderate|deep"` alongside `data-difficulty` (name retained for the doing axis so existing tooling does not break).

**Next.** Sweep the split pill across **L04–L16** (53 remaining pills, same method) — apply the two known re-rates (L05 C01, L14 C02) in that pass. Then resume the difficulty-progression audit proper, now on two axes instead of one.

---

## WHAT SHIPPED THIS BATCH (S61) — book-wide callout standardization · all 16 lessons

**The sweep.** Every "Coach's Tip/Note" and drifted color-coded box across L01–L16 was re-typed by **function** onto the Bible §6.6a canonical system: **Tip 💡** = actionable "make it work / fix it" (`#f0f7f0`), **Note 📘** = enrichment "why / context" (`#eceff1`), **Warning ⚠️** = real caution/safety (`#fff8e1`). Reassignment was by function, not original icon (the book had Tip/Note inverted in places). Bare labels, no "Coach's". Book-wide totals: **77 Tip · 107 Note · 72 Warning.**

**Left alone (formal/distinct devices, not coach callouts):** 🔑 Key Term · 📖 LEARN · 🔍 INSIGHT · 📝 DO-THIS-NOW / rituals · ✅ CHECKPOINT · 👀 WHAT YOU SHOULD SEE · 🎯 CHALLENGE / THE GOAL · 🔮 WHAT'S NEXT · 🔁 Builds on · 📦 Fell behind? · 🏁 FINISHED EARLY? · 📋 PREREQUISITES · 🔨 COMPILE CHECK · 📓 ENGINEER'S LOG · 🏆 RoboCup Connection · type-explainer (`#e3f2fd`).

**L15 / L16 — de-boxed (different treatment).** These two used a bespoke color-coded emphasis-box system (~53 / ~40 boxes, mostly no labels — analogies, verdicts, takeaways). Decision: the typed Tip/Note/Warning system is better for beginners (explicit beats implicit color-code), and 40–53 boxes is bad reading. So rhetorical/analogy/flow boxes were **de-boxed** (styling stripped to `margin: 16px 0;` — content + div kept, zero balance risk) and only genuine callouts kept as canonical typed boxes. L15: 10 Warning / 3 Note / 1 Tip kept, ~39 flattened. L16: 4 Warning / 2 Note / 1 Tip kept, ~13 flattened. Formal devices left intact.

**Verification (triple-checked).** 16/16 div-balanced · zero double-icons · zero malformed styles · zero empty de-boxed divs · every lesson shows balanced +/- edits (in-place swaps, no content deletion) · de-box removed only the bared "Coach" label word · formal devices byte-unchanged vs repo HEAD.

**Also shipped this batch (pushed + live):** Bible **v8.40** (§6.6a callout-by-function + §6.6 13-icon legend incl. 📘) · Maker **v2.43** · S61 robot mark on the Textbook tile (`index.html` + `Zumo_Robot_Mark.png`). Robot-icon-**family** remains blocked (image quality + ChatGPT credits).

**Next.** Difficulty-progression audit (L01–L03 easy, consistent hardening across all 16 — DJ's stated big goal). Future: expand the 📓 Engineer's Log icon/section (DJ likes it). Standing parked queue unchanged.

**Versions this batch:** L01 v03.5.0 · L02 v02.9.0 · L03 v03.9.0 · L04 v04.4.0 · L05 v04.4.0 · L06 v04.8.0 · L07 v04.4.0 · L08 v04.3.0 · L09 v05.2.0 · L10 v02.3.0 · L11 v02.4.0 · L12 v01.4.0 · L13 v02.4.0 · L14 v02.6.0 · L15 v02.4.0 · L16 v02.3.0.

---

## WHAT SHIPPED THIS BATCH — L14 v02.5.0 · L15 v02.3.0 · Maker v2.41

**L14 (Competition Prep) — 3 challenges, hybrid.** C1 Wheel Test (MEDIUM) + C3 LoP Counter (TOUGH) → full Goal→Logic→Template cards; C2 Strict Mode (EASY) → prose card (three-line trick-question answer; panels would be hollow). Blanks verified to fill exactly to each solution.

**L15 (The Present Isn't Enough / PID) — 7 challenges, two groups.** C1–C3 (MEDIUM) → full panel cards, multi-part solutions preserved verbatim in the reveal (all three templates fill exactly to solution). C4–C7 (HARD ×3 / ADVANCED) → canonical shell + **prose, no panels** — preserving their deliberately-open, no-solution design (the §9 intro states it: "the first three ship with solutions, the last four do not"). Two internal cross-refs to "Challenge 9.2" updated → "Challenge 2".

**L13 — solution-comment sync (lesson + Maker).** L13’s cards read “Challenge 1/2/3” but its revealed-solution comments + payloads (c1_sweep/c2_report/c3_rowzero) still said “// CHALLENGE 9.x” — synced to 1/2/3 in both the lesson and the three Maker payloads (count-guarded; no collision with L09, which uses a different convention). Gate PASS, node --check clean. L13 v02.3.0→v02.3.1 (minor — banner unchanged per §5b), Maker v2.41→v2.42.

**L02 + L03 + L04 — FULL PANELS (lesson-only).** Added 🎯 Goal / 🧠 Logic (Pseudocode) / 🧩 Template panels to every algorithmic challenge: L02 2.2–2.5, L03 3.1–3.7 (3.8 research = Goal+Logic), L04 4.1–4.5. Debug/no-solution types (L02 2.1, 2.6) stay prose. Template blanks fill to the real solution tokens (verified). Built with a preserve-everything rebuild after an early version dropped middle prose — triple-checked vs the original pre-shell files: zero prose/code/image/anchor/Maker-link loss, gate PASS, div balance 0, versions consistent. ⚠️ L02 v02.6.0 (the first panel build) had dropped prose and was superseded by v02.7.0. Versions: L02 v02.5.0→v02.7.0, L03 v03.7.0→v03.8.0, L04 v04.2.0→v04.3.0.

**L02 + L03 + L04 — shell repair, lesson-only.** All 19 challenges: stripped the old white/gray body wrappers, hoisted 📁 Work-in + 🔍 Where-to-look into the pale-yellow bar, dropped the 📝 Plan-first line from L02/L03 (their Maker templates already carry the MY PLAN block — confirmed `mainCpp()` adds it for lesson>1), and reskinned solutions flush. Preserved: L03’s 14 teaching callouts, L04’s timer iframes + hint/solution reveals, all solution code (gate PASS on each). Goal/task stays prose for now — the full Goal/Logic/Template panel bodies are the in-progress next phase. L02 v02.4.3→v02.5.0, L03 v03.6.3→v03.7.0, L04 v04.1.5→v04.2.0.

**L10 (Obstacles) — green callout → canonical card, lesson-only.** All 5 challenges restyled from the old green left-border callout to the plum-box card: gradient header with sequential “Challenge N: Title”, canonical pill, new Work-in bar, and 🎯 Goal / 🧠 Logic / 🧩 Template moved from inline <strong> labels into panels. C1/C2/C4 keep their Template code shown openly (L10 has no separate solutions — disclosure unchanged); C3/C5 stay prose. Word-level diff confirms only the header restyling + Work-in bars changed — all Goal/Logic/Template/hint text byte-preserved. No Maker touch (gate confirms L10’s 20 payloads untouched). L10 v02.1.15 → v02.2.0.

**L08 + L09 — Template panels added, lesson-only.** Both lessons were already canonical cards (shell + Goal + Logic); the only §6.12a gap was the missing 🧩 Template panel. Added 8 Templates: L08 8.4 (Position Bar) + 8.5 (Adaptive Kp); L09 9.1–9.6 (all algorithmic). L08’s 3 bench-tuning challenges (8.1–8.3) correctly stay Goal+Logic — no code answer. Each Template was built by blanking tokens directly in the existing solution (values/identifiers only, structure preserved), so filling the blanks reconstructs the solution byte-for-byte. Solutions, hint ladders, and disclosure untouched — no Maker change, parked disclosure call unaffected. L08 v04.1.10 → v04.2.0, L09 v05.0.12 → v05.1.0.

**L11 (Time Lies, Distance Doesn't) — 3 challenges + 4 mysteries, lesson-only.** The 3 challenges (The Retreat / EASY, The Hunt / MEDIUM, The Speed Budget / HARD) → full Goal→Logic→Template cards; each hint folded into its Logic panel; solutions preserved verbatim (gate confirms they still byte-match). Already sequential with `CHALLENGE 1/2/3` comments, so **no renumber, no comment sync, no Maker touch**. The 4 mysteries (a separate `data-kind="mystery"` construct) left in their own Bonus box. Star-text difficulty → canonical pills. L11 v02.2.5 → v02.3.0.

**Both:** headings "9.x" → **sequential "Challenge N"**; the `// CHALLENGE 9.x` solution comments synced to `1/2/3/…` in the lesson **and** the matching Maker payloads (L14: `c1_wheeltest/c2_strict/c3_lop`; L15: `c1_gainsched/c2_dfilter/c3_worstdt`). Comment-only; executable bodies unchanged. L13's `9.x` comments deliberately left (see queue). Old inline `[TIER]` text tags → canonical five-tier pills. Full payload gate PASS; diff-audit clean on both.

---

## PUSH BATCH (S60)

1. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root. *(All lessons already pushed: L14/L15 + Maker v2.41 `a2238937`; L11 `63abdc3`; L08/L09 `7de0402`; L10 `92e7e31`.)*

Verify by fresh clone (~30–40 s cache lag).

---

## STILL QUEUED (S61)

- **Project B — DONE.** Shells canonical book-wide; Goal/Logic/Template panels on every algorithmic challenge L02–L15. L01 stays prose, L06/L07 already conformed, L16 = tier-cards (all intentional). Any remaining challenge-card polish is a future pass, not a gap.
- **Difficulty-progression audit (NEW, DJ-requested S60):** book-wide check that L01→L16 actually ramps consistently — easy at L01–L03, steadily harder after. Run once the Project B rollout is complete; verify we're doing what we set out to do.

**LOGIN / TRACKING (parked, DJ "back burner" S60 — architecture confirmed):** The Robot-Trainer shell (`weymuth.github.io/Robot-Trainer/`) authenticates via a Cloudflare Worker `zumoauth.weymuthd.workers.dev` (session cookie; `/me` returns `{username}` = lastname+firstinitial, e.g. `weymuthd`; `/track` logs events; `home.html` already fires both). The zumo book/Maker share the origin `weymuth.github.io`, so the Worker already trusts them and the cookie already flows — no backend change needed to read `/me`. Deferred pieces, in order of appetite: (1) wire the Maker to `/me` to auto-fill the folder from the login and drop the name prompt (folder = the username directly; ~10 lines JS; keep a manual fallback for no-session opens); (2) a shared tracking snippet on the book/Maker/tutor pages (lesson-opened, key clicks, and — DJ: **definitely** — read-quality: scroll-depth + focus-time) posting to `/track`; this needs the Worker to actually **persist** the event stream somewhere queryable per student. Soft posture only (identity + logging, book stays readable without a session); hard-gating the book is a separate hosting change that only earns its keep if monetizing. Note: minors' behavioral data — keep minimal.

**BENCH:** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** *(low priority, down-the-road)* challenge **countdown timers** — consider a SELECTIVE rollout to short/bounded "quick attempt" challenges only (not the heavy multi-step builds), decide after the fall classroom run; note they’re online-only (iframe), so solve the Canvas-display wrinkle first · solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 · §9 difficulty grouping · challenge-card full goal→logic→template redesign for the ~80 challenges that lack it (Project B pass B).

---
*Written S60, July 21 2026. Project B complete and clean across L01–L16; L13 sync (v02.3.1) + Maker v2.42 the final cleanup. This push = L13 + Maker + LIVE.md.*

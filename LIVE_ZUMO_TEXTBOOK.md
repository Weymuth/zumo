# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 24, 2026 (Session 68 — structural-defect class closed · Going Deeper pointers · L03 arrays+modulo · L05 proximity hardware corrected end-to-end).
**Status:** **THE PANEL-CLOSE CLASS IS CLOSED, AND THE GATE THAT MISSED IT IS REPLACED.** Eight lessons were shipping with the Image Index panel's closing `</div>` in the wrong place — in six (L01, L12–L16) it sat *after* `</html>`, and in two (L06, L07) it sat after the footer, sealing the lesson's end matter inside the grey box. Open/close counts balanced in every case, because the orphaned close was balancing the panel that never closed: **the `tag balance` gate was satisfied BY the bug** and returned PASS for the defect's entire life. Git-verified provenance: L01 carried it from its first tracked commit (hand-authoring); L12–L16 all five acquired it in ONE commit, `94acc10` "Session 35 Massive Update", the §6.5 flat-heading→boxed-section conversion, whose stateful close-the-previous-panel transform had no terminator for the last panel — then survived 28 later commits on L01 and 9–13 on the others. All eight repaired by relocating the close (count-preserving). `book_gates.py` v1.1→**v1.2**: the two count-based structural checks are replaced by **one real HTML parse** (tag stack, reports the swallowed open AND the stray close by line) plus a **semantic** companion gate, because L06/L07 parsed *clean* and were still wrong. Both new gates were control-run against the unfixed clone and FAILED there (12 parse problems, 2 end-matter violations) before being trusted. Canonized as Bible **§24.6 / 24.6a / 24.6b**. Also this session: **GRAPHIC 5.1 was wrong hardware** — DJ caught it by eye; the left/right proximity detectors are *side-facing*, not a ±25° forward fan (verified against Pololu 0J63 §3.5/§3.6), so the SVG was redrawn to −90°/0°/+90° and the caption, alt text, index row and §1 prose moved with it. Three correct front-sensor-array photos added to L05. **All 16 book gates PASS on the delivered set.**

**Versions:** L01 **v03.6.5** · L02 v02.13.4 · L03 **v03.11.0** · L04 v04.5.3 · L05 **v04.7.0** · L06 **v04.10.1** · L07 **v04.6.2** · L08 **v04.5.1** · L09 v05.3.1 · L10 **v02.4.2** · L11 v02.6.2 · L12 **v01.6.2** · L13 **v02.5.2** · L14 **v02.7.2** · L15 **v02.5.2** · L16 **v02.4.1** · Bible **v8.50** · Maker v2.45 · Gate v1.6 · Harness v3.0 · pill_sweep v1.0 · book_gates **v1.2** · going_deeper v01.0.0.

---

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

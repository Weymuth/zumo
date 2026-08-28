# ZUMO — GPT REVIEW WORKLIST (v1.12)
### Session 154 · intake of 18 GPT feedback documents (68,123 words) · nothing fixed, nothing ruled

> **COUNTS ARE DERIVED AND CURRENT AS OF S192 — 100 CLOSED · 2 PARKED · 143 OPEN, of 245.**
> **GATE 81 NOW ASSERTS THIS FIGURE IN ALL THREE HOMES against `census.worklist()` (§24.24a, S192).
> It is no longer maintained by hand in any of them.**
> Derived by enumerating Part 2's ID rows (245, agreeing with all sixteen section headings, no
> duplicates) and Part 0's two tables, then asserting `closed + parked + open == 245`. Every Part 0 ID
> exists in Part 2; `closed ∩ parked` is empty. **This is the one derived answer §24.24 asks for; the
> other two homes are LIVE.md and the session handoff.**
>
> **S190's figures were wrong in two independent ways. Both are corrected here, and neither predicate
> is discarded.**
> 1. **A ✅-only predicate cannot count this section.** Six rows in Part 0 carry ❌ — `L02-12` and
>    `L02-19` (STRUCK), `L02-07`, `L04-01`, `L04-03`, `L13-17` (REFUTED). A refuted row is resolved and
>    is not open work, so it is CLOSED. Dropping those six is the entire L02 17-vs-14, L04 5-vs-3 and
>    L13 15-vs-14 gap. (S190 recorded L13 as "14 vs 0"; the standing figure was 15, not 0.)
> 2. **`L08-13` was seated twice** — MEASURED at S154 and SHIPPED at S190. Part 5b confirms both name
>    the same finding. One finding, two rows: a live exactly-once violation, merged at S191.
>    **S190 therefore closed 21 rows, not 22** — and the arithmetic says so: 72 + 21 = 93.
>
> **The split is kept visible so neither predicate can go missing again: of the 100 closed, 94 are
> fixed / verified / ruled and 6 are refuted or struck.** A headline that shows only one of those two
> numbers is how this discrepancy survived nine sessions.

> **STATUS: 100 rows CLOSED (Part 0), 2 PARKED with reasons, 7 MEASURED (Part 5b), the rest UNVERIFIED.**
>
> **L01 THROUGH L07 ARE DONE. L08 HAS ONE OPEN ROW: `L08-15`.** `L08-08` shipped at S192 as a
> FIVE-ROW C1 residue pass — `L10-12`, `L11-08`, `L12-18` and `L15-08` closed with it, because they were
> the same claim repeated and closing one would have left four rows describing work already done (the
> `L06-02` shape). **143 rows remain OPEN.**
> **Read PART 0 FIRST.** Rows below are kept verbatim as GPT wrote them even after they are fixed,
> so a row's presence here means nothing on its own — Part 0 is what says whether it is still live.
> These are GPT's claims plus my assessment of them. **Apart from the seven in Part 5b, none has
> been checked against the live tree.** A text match locates; it never answers (rule 38). GPT
> cannot see a ruling (rule 39). Verification is a separate pass that happens *after* DJ rules on
> the canon statements. **AGREE means the claim is coherent, not that it is measured.**

---

## HOW TO USE THIS FILE

Every finding has an ID (`L08-04`). Say the ID to discuss, accept, or reject it.

**Verdict legend — my assessment, not a ruling:**

| Code | Meaning |
|---|---|
| **AGREE** | GPT is right as far as I can tell; the fix is mechanical once ruled |
| **AGREE-EXPENSIVE** | GPT is right, but the fix is large (Maker payloads, byte changes, or multi-lesson) |
| **VERIFY** | Claim is checkable and must be checked before acting — repo, rulebook, or bench |
| **BENCH** | Only the floor/robot can settle it; parks with the existing bench queue |
| **DJ'S CALL** | Not a defect. Design, pedagogy, or policy — DJ rules, Claude does not |
| **DISAGREE** | I think GPT is wrong, or the finding is superseded |
| **STRUCK** | Already ruled in canon; GPT could not see the ruling |

**Canon tags** — `C1`–`C6` mark findings that are instances of a book-wide canon problem.
Ruling the canon statement collapses every finding carrying its tag.

---

# PART 0 — CLOSED ROWS

**A row here is DONE. It is kept, never deleted, because the rows below stay verbatim as GPT
wrote them and a reader who meets one again needs to know it was already answered.**

This ledger exists because two rows died without anyone noticing. `L02-04` and `L02-05` were
fixed in some earlier session, stayed on the list, and were re-investigated at S178 — a whole
read spent on work already done. **A closed row with no record of being closed is an open row.**

**Do not trust a memory or a handoff to tell you a row is closed. This table is the record, and
the tree is still the arbiter (rule 32).**

## THE EXACTLY-ONCE RULE (S181)

**Every one of the 245 rows in Part 2 resolves to exactly one of CLOSED, PARKED, or OPEN.
There is no fourth state and there is no silence.** A row that is not named in the CLOSED
table or the PARKED table below **is OPEN**, whatever any handoff says about its lesson
having "had a pass."

**S181 found this rule was needed twice over.** S180 shipped five L02 rows and recorded none
of them. And the four L13 rows ruled at S167/S168 were written into **Bible §16.33 and §16.34**
and never into this file — so Lesson 13 read as untouched while four of its rows were done, and
as *passed* while seventeen were not. **A disposition recorded in another file is not recorded
here, and here is where the next reader looks.**

**PART 4 IS NOT A DISPOSITION SECTION.** D-3, D-4 and D-5 say *hold until priced*, *price it
first*, and *unverified, must be checked*. Rows named there are OPEN with a note, not closed.
Only D-6 resolved a row (`L01-14`), and that row is in the table below.

| Row | Status | Closed | How |
|---|---|---|---|
| `L01-01` | ✅ SHIPPED | S177 | *Break It On Purpose* now unplugs the USB cable; the callout closes by naming what does NOT break an upload. Bible §16.46. |
| `L01-02` | ✅ SHIPPED | S162 | The three-term fix: `Zumo 32U4 Main Board` / `ATmega32U4` / `a-star32U4` build target. Bible §16.25, held by gate 76. |
| `L01-03` | ✅ RULED | S179 | **DJ: Git is required on a Mac because it installs Apple's Xcode Command Line Tools — the software most students are missing.** NOT because PlatformIO fetches the library over git. Bible §16.48. Open since S137. |
| `L01-04` | ✅ SHIPPED | S177 | The floor-test ritual is written into L01 Challenge 4 and is now a reusable convention the other lessons cite. |
| `L01-05` | ✅ SHIPPED | S177 | Challenge 4's reveal corrected to *twice as far out as it comes back*. **Bench check `F2` confirms it on the floor.** |
| `L01-06` | ✅ SHIPPED | S177 | Challenge 11's 4200/4500 split explained rather than silently inconsistent. **Bench check `F3` confirms the OLED read.** |
| `L01-07` | ✅ SHIPPED | S177 | §4 reworded: *today your program touches five of them*. Twin of `L02-08` and `L03-04`. |
| `L01-08` | ✅ SHIPPED | S177 | Caption → *popularized*; the `printf` claim corrected. `L01_B02` rekeyed. |
| `L01-09` | ✅ SHIPPED | S177 | The *very first programmers in history* claim is gone. |
| `L01-10` | ✅ SHIPPED | S162 | Absorbed into `L01-02`'s three-term fix. |
| `L01-11` | ✅ SHIPPED | S177 | §3 now credits thermostats with closing a loop and distinguishes on *how much it does with the measurement*. |
| `L01-12` | ✅ SHIPPED | S177 | Windows chime / Mac dialog / nothing are all named as normal. |
| `L01-13` | ✅ SHIPPED | S178 | Three sites disagreed about where a project lives; all now say `Documents/PlatformIO/Projects`. **Ruled book-wide at S179 — see `PATH` below.** |
| `L01-14` | ✅ SHIPPED | S154 | Figure index regenerated. **Gate 73** asserts it for all 16 lessons and passes. |
| `L01-15` | ✅ SHIPPED | — | **Gate 71** asserts the strip's catalog name for all 16 and passes. |
| `L02-01` | ✅ SHIPPED | S178 | Build 3 is a COMPILE error, not a linker one — measured with `avr-g++`. The section teaches three cases. Bible §16.47. |
| `L02-02` | ✅ SHIPPED | S178 | §8A's two blocks converted to `ledYellow`. |
| `L02-03` | ✅ SHIPPED | S178 | Same two blocks converted to K&R braces and 2-space indent. |
| `L02-04` | ✅ ALREADY DEAD | found S178 | Fixed in an earlier session and carried on the list regardless. **This row is why Part 0 exists.** |
| `L02-05` | ✅ ALREADY DEAD | found S178 | Same. §3.3 already named Warm-Up 2. |
| `L02-08` | ✅ SHIPPED | S178 | §4 continuity now matches `L01-07`'s wording. |
| `L02-10` | ✅ SHIPPED | S178 | Step 3: *a green build is evidence, not proof*. |
| `L02-11` | ✅ SHIPPED | S178 | Closed by one sentence, jointly with `L02-18`. |
| `L02-14` | ✅ SHIPPED | S178 | Step 7: only Button A ever had LED code. |
| `L02-16` | ✅ SHIPPED | S178 | *The Seven Sections* reframed as the RoboLore standard, not a C++ rule. |
| `L02-18` | ✅ SHIPPED | S178 | See `L02-11`. |
| `L02-13` | ✅ SHIPPED | S180 | *Two objects would fight over it* was a **fabled mechanism**. Replaced by the real cost: SRAM, and two names for one piece of hardware. Verified S181 — *fight over* is 0× in the tree. |
| `L02-15` | ✅ SHIPPED | S180 | Challenge 2's release-wait, in both scaffold and reveal. The *single trip through `loop()`* claim was FALSE and lived about an hour — `PushbuttonStateMachine` was cloned, transcribed and run: **two passes, not one**. §9 C2 corrected. **`L02-B2` is the falsifiable bench prediction.** |
| `L02-17` | ✅ SHIPPED | S180 | *The block you did not ask for: MY PLAN* — now a prose section in §6, pointing at L07 where the plan becomes the student's own. |
| `L02-12` | ❌ STRUCK | S180 | The stack model is the right simplification. GPT's technically-correct alternative teaches a Lesson 2 student nothing. |
| `L02-19` | ❌ STRUCK | S180 | **L02 §9 says spiral markers start in the NEXT lesson, deliberately**, and Warm-Up 4 is a warm-up, not a challenge card. GPT could not see that ruling. |
| `L03-01` | ✅ SHIPPED | S179 | Step 4's checkpoint denied the `setup()`/`loop()` Step 2 told them to keep — one callout above a green build. **First reported DEAD in error: the grep missed `no <code>setup()</code>/<code>loop()</code> exists`.** |
| `L03-02` | ✅ SHIPPED | S179 | Step 3 told the student to paste a SECOND header into a file the Maker had already headed, and to replace placeholders the Maker fills with real values. Coupled with `L03-01`. |
| `L03-03` | ✅ SHIPPED | S179 | The Part 2 prerequisite no longer says to copy the Lesson 2 project folder. |
| `L03-04` | ✅ SHIPPED | S179 | §4.1 credits L01's driving and L02's Warm-Up 4 spin. Third twin of `L01-07`/`L02-08`. |
| `L03-05` | ✅ ALREADY DEAD | S162 | The retired C1 wording is gone book-wide, and **gate §16.31 asserts it and passes** — an instrument says so, not a grep. |
| `L03-06` | ✅ SHIPPED | S179 | §4.5's drift test is a hypothesis §7 settles, not a verdict about motor strength. |
| `L03-07` | ✅ SHIPPED | S185 | §3.25 repeated L01 Challenge 6's three-run scatter from scratch, in a book where **C6 says *Keep these numbers… you will want it in Lesson 3***. Now retrieval: read your own three numbers, then change ONE condition. **No comparative magnitude asserted** — scatter vs condition-shift is unmeasured (rule 50). |
| `L03-10` | ✅ SHIPPED | S185 | **The row named four L03 sites; the claim class is NINE across four artefacts** — L03 ×4, **L01 ×2**, **Maker ×2** (c11's boxed header), and **`QUIZ_L03` B18 where it was the KEYED CORRECT ANSWER**. Verified false before editing: 4,200 ÷ 4 = 1.05 V/cell against a ~1.0 V/cell cutoff, and the real mechanism is **cell reversal in a series pack**. Retired claim reused as B18's distractor. **L01 C11's 4,500 split untouched** — see `ZUMO_FIX_TRACKER.md` §5/§6. |
| `L03-08` | ✅ SHIPPED | S179 | The unsourced 30-second cooldown rule replaced by the current-under-load mechanism. |
| `L03-09` | ✅ SHIPPED | S179 | The unsourced ±10% battery figure removed. **`L03_B35` was falsified by this correct edit and was rekeyed.** |
| `L13-03` | ✅ RULED + SHIPPED | S167/S168 | DJ ruled candidate **D** — *watch the sidestep*, `driveDistance(ROW_STEP_CM)` → `driveUntil(ROW_STEP_CM)`, with `SWEEP_DONE` as a NEW state rather than reusing `STOPPED`. Four candidates COMPILED before the ruling. **Bible §16.34. Backfilled here S181 — it was recorded only in the Bible.** |
| `L13-01` | ✅ SHIPPED | S167/S168 | Folded into `L13-03`'s card: D as sketched branched on `STOP_PROX` alone and killed the kill switch during the sidestep, so one contract fixed both. **Bible §16.34. Backfilled S181.** |
| `L13-05` | ✅ PARTLY REFUTED | S167 | The lesson already names both failure modes; what was owed was the **assumption** rather than the risk. **Bible §16.34. Backfilled S181.** |
| `L13-11` | ✅ VERIFIED | S167 | The `readCalibrated()` quote **is faithful** to the QTR bundled in `pololu/Zumo32U4@2.0.1`. The defect was the sentence introducing it. **Bible §16.33. Backfilled S181.** |
| `L13-13` | ✅ SHIPPED | S181 | The servo claim. A hobby servo takes power, ground and a timed signal pulse and brings its own driver inside the case — it never asks a DRV8838 for a channel. §8A.3 now explains what a servo is, says plainly it does not compete with the tread drivers, and gives the real barrier: **there is no arm.** **L14 inherited the same claim and was fixed in the same pass.** `spoken for` is 0× book-wide. |
| `L13-02` | ✅ SHIPPED | S181 | `MAX_ROW_CM = 300.0` was called *a safety cap* that ends the row *before the robot grinds against* the wall. Three metres never fires before any wall, so the stated purpose was false. **DJ released the room-fact carve-out — the classroom field is not RCJ-spec — so the number is chosen: 150.0.** Comment rewritten as what it is (a runaway stop, sized above the longest row you expect) plus how to tune it. **59 Maker payload sites moved with the lesson**; the constant is inherited by L13–L16. Census updated, all 8 standing byte controls reproduce. |
| `L13-04` | ✅ SHIPPED | S181 | *every row starts from truth* — the prox stops at a distance set by the wall's color and approach angle, so a row-end is a **bound on error, not a pose**. §8A.4 now says so. **First probed as DEAD in error:** the finding is real, the phrase GPT quoted is not what the tree says. |
| `L13-14` | ✅ SHIPPED | S181 | *you have already flown it* — struck. §8A.4 now says plainly that SLAM builds a map and tracks the robot inside it and the sweep does neither, then keeps the honest half: you have used the idea SLAM is built on. |
| `L13-08` | ✅ SHIPPED | S181 | **Two of three sites were ALREADY CORRECT and unrecorded** — *visible black does not guarantee a weak infrared return; color and IR reflectance are different measurements*, with the claim conditioned on 7A's measurement. The §4.3 answer block was the one site still asserting it from the ball's *job*; now conditioned on 7A too. **The handoff's still-verbatim shortlist was wrong about this row.** |
| `L06-01` | ✅ SHIPPED | S181 | **REVERSE TRIM. Was miscategorised as closed** — Part 5b's ✅ meant *the bug was confirmed present*, and the row's own verdict reads *the most important code finding in the review, AGREE-EXPENSIVE*. `speed` carries the sign of travel, so `speed + TRIM` hands the weak motor LESS duty in reverse. **Measured at the register:** `setLeftSpeed` writes `|speed|` to `OCR1B` and puts the sign on a GPIO pin, so `setSpeeds(-135,-150)` is a real 2× swing (Bible v8.13 hardware-direction verification, satisfied against Pololu's own source). Fixed to `speed + (speed > 0 ? TRIM : -TRIM)` in `driveDistance` **and** `driveDistanceSmooth`: **153 Maker sites, L06 ×6, L07 ×3**, gate §15's anchor moved with it. **L12's planted `leftSpeed + TRIM` sabotage explicitly excluded and asserted untouched.** Priced at **+10 bytes** where a negative literal survives, **0 as shipped** (TRIM = 0 folds the ternary), **no ceiling risk** — `16/after_step_2` measured at 28,648 unchanged. |
| `L13-20` | ✅ SHIPPED | S181 | Challenge 1's `driveDistance(-10.0)` was sound only after `L06-01` propagated. It has. Closed by dependency, no L13 edit needed. |
| `L13-06` | ✅ SHIPPED | S181 | **Sabotage B4's mechanism was backwards, and GPT understated it.** Traced against the shipped payload: `silverDetected()` returns false only when some sensor reads `>= SILVER_RAW_MAX` (tuned in the hundreds, raw microseconds). On the calibrated channel plain white floor is already 0, so **the guard never trips and the function returns TRUE** — not *the door never triggers*. **And §6 checks silver BEFORE `isLineVisible()`, deliberately**, so `handleGap()` never runs and the robot cannot park in `LINE_LOST` — **the old reveal contradicted a code comment two screens away.** Symptom corrected too: it fires at the first gap and sweeps mid-course. New closing beat: **the real doorway still works**, because silver clamps to 0 as well — the broken code passes the one test you would have written. |
| `L13-07` | ✅ SHIPPED | S181 | B4's close claimed the black ball *has been invisible on the same physics all along*. Two different sensors, two different failures: the doorway is the line array **clamping a strong signal** to the edge of a scale with no room for it; the ball is the **prox** getting almost no signal back. Now stated as *a scale that cannot hold the answer* versus *an answer that never arrives*, sharing only the moral. |
| `L13-09` | ✅ ALREADY DEAD | found S181 | *Nearly invisible to every sensor this robot carries* **is not in the tree.** Every black-ball claim is correctly scoped to the prox — *the one sensor aboard that could look for it*. Fixed in some earlier session and carried on the list regardless, like `L02-04`. |
| `L13-10` | ✅ SHIPPED | S181 | **The hedge was already there and unrecorded** — §3 reads *if it really is brighter than the brightest surface your calibration spin saw — Section 5 is where you measure that, not assume it*. Checking it found a **broken cross-reference**: §5 is the Code Walkthrough; the measurement is **§7A**, which 18 other references in the lesson name correctly. Pointer corrected. *The subtraction knew; the clamp forgot* kept, per the verdict. |
| `L13-17` | ❌ REFUTED | S181 | **`SILVER_RAW_MAX` is named correctly.** On the raw channel brighter = LOWER, so silver readings sit *below* the constant and it is a genuine upper bound — `raw[i] >= SILVER_RAW_MAX` rejecting the value is what an exclusive max does. **GPT's instinct has a real point** — the name invites *set it to the highest silver reading I measured*, which the `>=` would then reject — **but the adjacent comment says *set this BETWEEN them* and §7B makes the student test all three settings.** A rename is 38 Maker sites, 13 lesson sites, the L13 quiz bank, a census update and a full recompile, three weeks from launch, for a name that is already right. **No action.** |
| `L02-07` | ❌ REFUTED | S154 | GPT wrong. The payload is 95 / 86 / 75; the lesson's 85–95 is correct. Part 5b. |
| `L04-01` | ❌ REFUTED | S186 | **The premise is wrong and the fix would cost a graded challenge.** L03 §8A.5 teaches array-as-a-row-of-constants-YOU-wrote (index as a variable, out-of-bounds hazard) and exists to motivate §8A.6's wrap; L04 §5.5 teaches array-as-a-buffer-a-FUNCTION-fills, plus the index↔sensor-number mismatch table the lesson calls its number-one bug source. The only shared sentence is *counting starts at zero*, restated in L04 for a different reason. **L04 §5.5 already opens as retrieval** — *Lesson 3 promised… its §8A.5 gave you the tool* — which is `L03-07`'s shape, not duplication. **Triple-checked three ways (§24.13).** Structural bank parse: **six** L03 questions depend on the two sections — `B44`, `B45`, `B46`, `B55` (four by explicit cite), `A13`, and `A22`'s matching pair. Challenge 5 declares its own array, so it is syntactically self-contained, **but its two blanks ARE §8A.5 and §8A.6** (*the index you read*, *the wrap divisor*) — demote them and the challenge stops being teachable and becomes fillable by pattern-match. **The cost argument was overstated in the first pass and is withdrawn:** the anchor sweep found **no `id` anchors and only 2 prose cross-refs**, and the Maker carries **0** sites for `TEST_SPEEDS`/`NUM_SPEEDS`/`speedIndex` — no census, no recompile, no byte cost. **Refuted on the pedagogy, not on the price.** |
| `L04-03` | ❌ REFUTED | S186 | Moot by dependency. The row flags a continuity line that breaks **only if `L04-01` demotes**. It does not. No L04 edit owed. |
| `L04-02` | ✅ SHIPPED | S186 | **The row was right about the redundancy and its proposed fix would have broken a figure.** GPT said cut §8A's basic syntax review — but `L04_GRAPHIC_4-01_if_anatomy.svg` sits **between** those paragraphs and the *three parts* prose is what reads it. Narrowed to the one genuinely duplicated span: the compressed `==` aside, which restated L03 §5.5's full WARNING at lower resolution. Replaced with a pointer to §5.5 that says why the trap bites harder here — a condition that is always true is invisible when the number underneath it is moving anyway. **§8A.2 kept: it carries the Threshold KEY TERM, graded by `L04_B26` and `L04_B50`.** Bank sweep confirms the six-operator table's graded home is **`L03_B60`, cited to Lesson 3 §5.5** — nothing in L04 is falsified. Zero questions cite §8A.1. |
| `L04-04` | ✅ SHIPPED | S186 | §5.7's closing paragraph was the **third** statement of RAM/power-off/0–1000, after §3.4's body and §3.4's KEY TERM. Replaced with what only §5.7 can say: the record books are this function's product, nothing on the display shows them, and the only evidence the sweep worked is readings agreeing in Step 6. **§3.4 untouched — 4 questions cite it. Zero cite §5.7.** **Step 6 vs §7.1 is NOT a defect** and the row is wrong about it: Step 6 says outright *You'll measure it properly in Section 7*. Discovery then measurement, signposted. |
| `L04-05` | ✅ SHIPPED | S186 | Challenge 1 blanked `lineSensorValues[____] > ____` — the exact two values §8A.3 prints six sections earlier — and then the hint handed back *center sensor = `lineSensorValues[1]`*. The student copied; nothing was retrieved. **GPT's fix (drop the template) was declined:** the Goal→Logic→Template card is canon and breaking one card is the opposite of consistency. **Blanks MOVED instead** — index and threshold seeded and attributed to §8A.3, blanks relocated onto the `else`-branch display work, which is the genuinely new idea. **`L04_A16` already grades exactly that** (*why must the display work appear in BOTH branches*), so the bank was pointed at the right concept and the card was undercutting it — no bank edit owed. Two blanks before, two after. **Verified not payload-coupled: 0 Maker sites.** |
| `L05-01` | ✅ SHIPPED | S188 | **DJ ruled: move, do not delete.** GPT called it a full anatomy re-teach; measured, it is narrower. Cut: the push-up-coach refresher (which also asserted *starts counting at 1*, against the zero-counting rule L04 §8A.6 teaches), `L05_GRAPHIC_5-04_for_anatomy.svg` (a second drawing of L04's `4-06`), and the Quick Practice tracing `i < 4` (L04 §8A.6 already runs that lap table on `i < 3`). **KEPT: the `For Loop` KEY TERM** — `id="term-for-loop"` is the book's ONLY definition of the term and lives in no other lesson; deleting the h4 block would have deleted it. Also kept: `drawBar()` trace, `i--` countdown, Worked Example #2, the for/while NOTE, the CHECKPOINT. **GRAPHIC 5.4 is RULED OUT, not deleted** — `PLANNED_EXPECTED` 146→145 and the §21 coverage baseline 1,209→1,208, both with stated reasons, so outstanding stayed 15 and did not fall like progress (S135). The .svg stays on disk, unreferenced. Figure-index row removed and the tbody restriped. |
| `L05-02` | ✅ SHIPPED | S188 | **DJ ruled: omit only `readAllSensors();`.** Step 4 handed over all six prototypes on the third staging of `'readAllSensors' was not declared` (L02 Step 7, L04 Step 5, here). Now five are pasted and the sixth is the student's — the build stays red, the compiler names the missing function, and §5.5 still carries the full list for checking after, not before. The GPT spiral *first: explain / second: remind / third: expect* is what this implements. **Bank edit was owed and made:** `L05_A02`'s correct option and one distractor `why` both asserted the six arrive in one trip. Read all 8 §5.15 items against the live section — every one maps to retained content. |
| `PATH` (untagged) | ✅ RULED + SHIPPED | S179 | **DJ: `Documents/PlatformIO/Projects/<FolderName>` is the correct default location.** Bible §16.49. Fourteen sites moved: ten lesson prose, the Maker hint, two §11 canon lines, one SVG label. |
| `L06-02` | ✅ ALREADY DEAD | S189 | **Fixed at S161 and the row was never closed — open for 28 sessions after the fix.** GPT's quoted phrase *"self-correcting regardless of conditions"* is at **0 occurrences**. §3.6's KEY TERM already reads *"Closed on WHAT, though? … `driveDistance()` is closed-loop on distance … still open-loop on heading,"* and the table row already says *"Repeatable — as far as the wheels are concerned."* That IS DJ's ruling, verbatim, landed at commit `4a9e1d1`. **No edit made: writing the drafted replacement would have swapped one correct fix for another and spent a version bump on nothing.** |
| `L06-03` | ✅ SHIPPED | S189 | **The live claim was NOT where GPT quoted it.** The §7 WARNING was fine; the absolute sat in Experiment 5's reveal — *"no encoder anywhere on this robot can see a curve."* Both sites revised. DJ's ruling honoured: *"the dashboard says you drove straight; the floor says otherwise"* is **kept**, the explanation above it rewritten to say the arithmetic is not what is missing — two encoders differing is exactly how a robot infers heading; what they cannot show is whether rotation became the robot's motion. **Spiral star to L05 placed** (combine for presence / difference for direction). **Star direction measured before placing: 26 backward, 0 forward book-wide — 27/0 after this one, which is the expected consequence, not drift**, so the L12 pointer stays bare prose. §21 coverage 1,208 → **1,209** with a stated reason. |
| `L06-04` | ✅ VERIFIED + SHIPPED | S189 | **VERIFY-then-AGREE discharged by COMPILER, not grep.** `static_assert` under `avr-g++` against pinned `pololu/Zumo32U4@2.0.1`: `getCountsLeft()` is **2 bytes**, `int` 2, `long` 4 — **blinding control (`==4`) fired correctly**. Source confirms `static volatile uint16_t` accumulators, deliberately unsigned. So the hint's *"Big numbers need bigger boxes — that's what `long` is for"* **taught a fix that does not work**: widening the target cannot help when the reading wraps at the same place. The 440 figure itself is right (32767 ÷ 74.25 = **441.3 cm**) — the CAUSE was incomplete, exactly as GPT said. Both sites now teach read-and-reset into a running `long`. |
| `L06-05` | ✅ SHIPPED | S189 | §3.1's *"As poles pass: North → South → one count"* → both edges of both channels, **four counts per quadrature cycle, 12 per motor-shaft turn**. Agrees with Bible §16.10's `12 CPR`. **A triple check caught a number I had planted myself:** the first draft ended *"12 counts, not 2"* — 12 ÷ 4 = 3 cycles, so the naive model gives 3, not 2. Unsourced figure removed (rule 50). |
| `L06-06` | ✅ SHIPPED | S189 | §4.1's *"start counting automatically when the robot powers on"* → no `init()` call **from you**; the library sets itself up on first read. **`L06_B25`'s KEYED CORRECT ANSWER was the retired claim verbatim** — the S185 pattern, a lesson fix leaving the bank grading the dead version. Re-keyed. |
| `L06-07` | ✅ RULED + SHIPPED | S189 | **DJ ruled `TRACK_WIDTH_MM = 98.0`, and the VALUE was wrong as well as the name.** Pololu's 85 mm is the DRIVE-to-IDLER sprocket spacing measured FORE-AFT along one side (DJ: *"85 or 86 for the distance between front of track and back of track"*); a differential-drive turn needs the SIDE-TO-SIDE separation, so name and value described the same wrong axis and never looked inconsistent with each other. Bible §16.10 is where it was canonised, sourced to *"Pololu product pages"*. **98 = Pololu's published chassis width AND the floor of the book's own tuned range (98–115)** — a calibration default, not a geometry claim; Pololu publishes no centreline separation and their library carries ZERO dimension constants, turning by gyro. **372 sites: Maker 328 · L06 ×13 · L07 ×15 · L08 ×4 · L09 ×5 · banks L06/L07/L09/L10/L12 · TDP · Bible.** Arithmetic cascade re-derived, not carried: turn circumference 267→**308 mm**, counts/degree 5.507→**6.34976**, L12's 90° 496→**571 counts**. **Student measurement removed (DJ ruling); the four-turn test survives as a tuning check.** `L06_B20` DROPPED (dead premise, concept graded 4× elsewhere); `L07_B47` re-stemmed because 98-as-default turned it into a trap that punishes a correct reading (v8.130 shape). |
| `L06-08` | ✅ SHIPPED | S190 | §8A was **already renamed at S108** (the `L06-02` pattern), so the row was partly pre-discharged. Live: the sandwich analogy, its *Result: a sandwich!* line teaching a RETURN VALUE for a `void` function, and a redundant **Function** KEY TERM L02 already owns. Replaced with the counterfactual — `driveThirty()` / `driveSeventyFive()` / `driveTwelvePointFive()`, three copies of one algorithm — and a two-parameter worked example built from the student's OWN `driveDistance()` and `turnDegrees()`, replacing `blinkLED` lifted from L02. **Body KEY TERM repointed Function → Parameter**, a term the book defined NOWHERE; glossary twin **6.69** added and the glossary filed alphabetically. `L06_B47` and `L06_B49` re-keyed off the deleted analogy. `build_family_map` v1.6.6.5 — its NOTE tier pinned the title `Recipe:`, measured dead first. |
| `L07-01` | ✅ COMPILER-VERIFIED + SHIPPED | S190 | Repeated identical declarations compile **clean** under `-Wall -Wextra -pedantic`; control: a `struct` in the same position fires `redefinition of 'Foo'`. **The book's quoted diagnostic does not exist.** Rewritten to name the real hazard — contents that cannot repeat in one translation unit — and why you guard every header anyway. |
| `L07-02` | ✅ SHIPPED | S190 | The book had it backwards. Include guards are standard C++; `#pragma once` is an extension every real compiler provides. **The retired phrase survived in the KEY TERM GLOSSARY and was caught by the triple check**, with its `Include Guard` twin still calling guards merely *older*. Both rewritten. `L07_B14` and `L07_B41`'s matching pair re-keyed. |
| `L07-03` | ✅ SHIPPED | S190 | `#pragma once` stops the preprocessor loop, not the design problem. Now teaches the half-read-header symptom and points at `RobotConfig.h` as the fix. `L07_B31` read and left — it says *stops the loop*, which is true. |
| `L07-04` | ✅ COMPILER-VERIFIED + SHIPPED | S190 | `extern` in a .cpp **links clean** when a definition exists; control: remove the definition and `undefined reference to 'motors'` fires. **The claim survived in §8A.2 after Error 5b was fixed** — rule 72 inside one lesson. House rule kept and re-argued as *one home per object*. **`extern` itself is untouched: 2,015 Maker sites, 149 lesson sites, 27 bank questions (42 occurrences).** |
| `L07-05` | ✅ COMPILER-VERIFIED + SHIPPED | S190 | A function body in a header compiles clean in ONE translation unit and gives `multiple definition` in two. **The quoted `expected ';' before '{'` could not be reproduced from any plausible header mistake**, so Error 6 was re-pointed to `expected unqualified-id before '{'`, which WAS reproduced, plus a footnote that library headers legitimately carry bodies. |
| `L07-06` | ✅ SHIPPED | S190 | Confirmed: prose said three includes, the reveal has four. Number removed; the plan question now asks the student to derive and count it. |
| `L07-07` | ✅ SHIPPED | S190 | Discharged by the eight-site reverse-TRIM sweep — see the `L06-01` note below. |
| `L07-08` | ✅ SHIPPED | S190 | Challenge 4 rebuilt on `driveDistanceAtSpeed(float, int)` with one-line wrappers, retitled *Speed Modes Without Copy-Paste*. It had literally instructed *copy driveDistance and modify the speed* inside the lesson about not duplicating code. `L07_A19` read first — keyed answer survives, no bank edit owed. |
| `L07-09` | ✅ SHIPPED | S190 | Challenge 7 → *Three-Stage Motion Profile*, function renamed across 9 sites. **A defect GPT missed:** GRAPHIC 6.11 draws a true trapezoid with ramps while the code makes three plateaus. Figure KEPT and reframed as the continuous version the build approximates, so §21 coverage does not move. Maker `kind=trapezoidal` ID kept (the lesson href points at it); labels changed. **L11's `BUILDS ON` spiral pointer was orphaned by the rename and found by the triple check.** |
| `L07-10` | ✅ SHIPPED | S190 | §8A now opens with four diagnosis questions before the reference tables, answers seated after §8A.3. Built as a callout first, which failed four gates at once (non-numeric id, unnameable family, callout census, image census) — rebuilt as plain markup, zero callout churn. |
| `L08-01` | ✅ SHIPPED | S190 | The *Hybrid Approach* notice walked back §6's plan-first model that L07 graduated to. Rewritten to say what is actually new: the architecture is settled and the difficulty moves to an IDEA. |
| `L08-03` | ✅ SHIPPED | S190 | Spiral Check seated before Step 4: three retrieval questions on L04's shared-pin jumpers, then the point — **software cannot detect this**. `initFiveSensors()` configures pins and returns; a perfect program on a three-sensor robot builds green and steers on nonsense. |
| `L08-04` | ✅ LIBRARY-SOURCE VERIFIED + SHIPPED | S190 | `QTRSensors::readLine` in pinned `Zumo32U4@2.0.1`: with no sensor above 200 it returns **0 or 4000, the last-seen side's extreme**, never an average. Executed to confirm. **`L15_B12` and `L15_B28` already taught this**, so L08 and L15 had contradicted each other. `L08_B26`'s matching pair extended. |
| `L08-05` | ✅ SHIPPED | S190 | `readLine()` calls `readCalibrated()` itself, so *one reading, two questions* performed two. Now genuinely one read. |
| `L08-07` | ✅ SHIPPED | S190 | `isLineVisible()` description corrected to the sum test it performs, and the discrepancy turned into a design decision the student must make: five sensors at 45 sum to 225 and pass, while no single one is near 200. |
| `L08-09` | ✅ SHIPPED | S190 | *Coast* → powered driving in four sites. The sabotage narrative still said *coasts straight… and keeps coasting* after the table was fixed — found by the triple check's cross-artifact arm. |
| `L08-10` | ✅ SHIPPED | S190 | The unmeasured loop rate removed **book-wide, 12 sites** (L08, L10 ×3, L11 ×2, four bank `why` fields, two options). **`ZUMO_QUIZ_L08`'s own header already recorded that no timing run backs it** and routed questions around it rather than filing the defect. |
| `L08-11` | ✅ SHIPPED | S190 | The thermostat moved out of the proportional-control list — it is the textbook bang-bang example — and became a retrieval question seated in the *When Bang-Bang Works* NOTE where it belongs. |
| `L08-12` | ✅ SHIPPED | S190 | The invented `~15cm/sec` replaced with measure → predict → test, plus why a motor command is not a velocity and a forward pointer to L11 overturning the stopwatch. **Also recorded in the bank header as never measured.** |
| `L08-06` | ✅ SHIPPED | S191 | `lastPosition` was assigned and returned and nothing read it; the library keeps its own `_lastValue`. Deleted from 145 Maker `RobotSensors.cpp` payloads, 7 lesson sites (L08 ×6, L10 ×1) and the two bank questions that used it as half of their file-scope-`static` example. **THE VARIABLE WAS NOT THE WHOLE EDIT:** `LINE_CENTER` had no other code use in that file, so the `#include "RobotConfig.h"` comment naming it (145 Maker + 2 lesson sites) and the §8 troubleshooting entry keyed on `'LINE_CENTER' was not declared` were both left pointing at a constant the file no longer reads — §16.30's shape, and the troubleshooting site was found by reading, not by any sweep. **Measured: zero flash movement across all 221 payloads** (before/after compile, blinding-controlled with a planted byte) — the compiler was already eliding it, which is the cleanest evidence it was dead. |
| `L08-02` | ✅ RULED + SHIPPED | S191 | **GPT's fix was REFUTED BY MEASUREMENT; the contradiction it found was real and is fixed in prose.** Every symbol `followLine()` touches is `main.cpp`-private or a `RobotConfig.h` constant — no module reads any of it — and two are deliberately shared inside `main.cpp`: `lastError` feeds `runSample()` and `dtSec` feeds `updateSpeedLoop()` ("One clock, two loops"), while `currentKp`/`currentKd`/`currentBase` are the live knobs the OLED menu drives. Moving the function either `extern`s six mutable globals — three sections after L08 Step 4 teaches that module state is `static` and private, which `B24`/`A07` quiz — or puts the tuning UI behind accessors and grows the L15 signature to five parameters. **The defect is one sentence in L07's vocabulary NOTE**, which used `followLine()` as its example of a behavior filed into `RobotMotion`. L07 now draws the real line (self-contained behavior → module; behavior owning live settings → beside those settings) and L08 Step 7 states why. 0 payloads, 0 bytes, against 135 payloads and 8 lessons for a move that would make the book worse. **`L08-14` does NOT depend on this** — it is a `main.cpp`-local question about sharing one observation, either way. |
| `L08-13` | ✅ MEASURED + SHIPPED | S154 / S190 | Measured in Part 5b at S154, fixed at S190: `setLayout21x8()` gives 21 columns, 0–20. Named in the template. **S154 and S190 each seated this row separately — one finding, two rows. Merged at S191; that duplicate is why S190's closure count read 22 instead of 21.** |
| `L08-14` | ✅ SHIPPED | S190 | `drawPositionBar(pos)` now takes the position instead of re-reading the floor, so the marker shows the observation the robot steered on. **The clean fix depends on `L08-02`, which is unruled — the lesson says so rather than pretending a refactor that was not done.** |
| `L08-08` | ✅ RULED + SHIPPED | S192 | **C1 residue, and it is not an L08 row.** Swept as the PHENOMENON (TRIM opposing a feedback loop) rather than the spelling, the claim is **12 prose sites across FIVE lessons** — L06 ×1, L08 ×2, **L10 ×4** (prose ×2, glossary, Quick Reference table row), L11 ×2, L12 ×3 (incl. KEY TERM) — plus **5 bank questions**. §16.31 retired the SLOGAN at S161 and the MECHANISM underneath survived, because that sweep was keyed on the phrasings table. **The claim is BACKWARDS, not loose:** TRIM is feed-forward and enters the same additive channel as the P-term, so it removes the disturbance the P-term is otherwise stuck holding a standing offset against. **Triple-checked; ARM 1 (the book's own `driveDistanceAccel` carrying TRIM inside a `while` loop) FAILED to refute — that loop closes on DISTANCE — and was discarded.** ARM 2: L15 §3.4 in the book's own words. ARM 3: L15 §3.6 already prescribes *check TRIM* for a line-loop offset. ARM 4: simulation — mismatch 12 / TRIM 0 → error 75, TRIM 12 → 0; blinding controls return −75 and 150; `error × Kp` constant at 6.000 across a 4× sweep. **0 Maker payloads, 0 bytes** (all 179 Maker hits are the benign `// wheels are fighting on purpose` turn comment). **`L01` is CLEAN — a hit is not a defect.** |
| `L10-12` | ✅ SHIPPED | S192 | Same claim family, closed in the same pass. L10 carried **four** sites, two of them in the reference apparatus students actually consult — the glossary *Closed Loop* entry and the Quick Reference row whose TRIM column read *never*, with the reason given as the P-controller already correcting bias. **The literal status glyph is deliberately NOT quoted here: it is the structural marker `census.worklist()` reads as REFUTED, and quoting it inside a row silently moved `fixed` by one. Caught immediately because the tally is derived now.**. A fifth bank question, **`L10_B21`**, was found only by an assertive-register sweep after the first four were fixed. |
| `L11-08` | ✅ SHIPPED | S192 | Same family. §8A.1 and §7C both rewritten to the deliberate-pedagogical reason. **`L11_B44` needed restructuring, not rewording** — its stem WAS the false claim with `correct: true`, the `L08_B25` shape from S191. |
| `L12-18` | ✅ SHIPPED | S192 | Same family, and GPT was right that Bonus B4's premise was unsound. L12's prose already gave the correct reason (*the gyro is watching*) and then added the false mechanism. Corrected canon: **TRIM is a straight-line correction and a turn has no straight line to protect.** **`L12_B35`'s key had to FLIP** — its keyed-correct option was the false mechanism, and a distractor marked wrong was essentially right. |
| `L15-08` | ✅ SHIPPED | S192 | **GPT wrote this at S154 and nobody read it: _"I is the only term that can remove steady-state error — true within the P/I/D feedback terms, but the robot already has feed-forward."_ Four independent arms re-derived a finding that was sitting in this file the whole time.** L15 §3.4 now says I is the only one *among the three feedback terms*, and names TRIM as the feed-forward half. It also carries the **back-pointer to L08** (DJ ruling S192), closing the spiral L08's forward question opens. |
| `L03-B1` (untagged) | ✅ HALF-CLOSED | S179 | Part 2 asked for the robot tethered AND 6+ feet of floor at once; now L01's floor test, in order. The *6+ feet* figure itself is still a bench item. |

## Parked with a reason — NOT closed, and not to be re-investigated

| Row | Why it is parked |
|---|---|
| `L02-06` | **Real and expensive.** `GLOBAL VARIABLES` appears 0× in the lesson and 0× in its payloads, against a Challenge 3 that says *declare three counters up top*. The fix moves `L02_GRAPHIC_2-05_sketch_anatomy.svg` (an eighth BAND must be drawn — a graphics-chat pass, unlike §16.49's one-string label), the §3.1 color key, *The Seven Sections*, §5's walkthrough and probably Bible §18.3. **DJ ruled S178: parked until after September 8**, filed in `ZUMO_AFTER_LAUNCH.md`. Student-facing cost measured and low. |
| `L02-09` | The baud comment appears **4× inside L02's own payload**, so a lesson-only fix breaks `gate_payload_match`. It is a Maker edit and rides with `L02-06`'s pass. |

---

# PART 0b — OPEN (everything not named above)

**143 of 245 rows are OPEN.** This section does not list them — the exactly-once rule means
the CLOSED and PARKED tables above ARE the list, by subtraction. What this section does is make
the arithmetic checkable, so a reader can tell at a glance whether a lesson has been worked.

**Derived at S191, not carried forward.** Every figure below comes from enumerating Part 2's ID rows
and Part 0's tables and asserting the row sums; `closed` counts a REFUTED or STRUCK row, because such a
row is resolved and is not open work. The `fixed` column splits that out, so the ✅-only reading of this
section — the one that disagreed with the old table for nine sessions — is visible instead of implied.

| Lesson | findings | closed | *of which fixed* | parked | **OPEN** |
|---|---|---|---|---|---|
| L01 | 15 | 15 | 15 | 0 | **0** |
| L02 | 19 | 17 | 14 | 2 | **0** |
| L03 | 10 | 10 | 10 | 0 | **0** |
| L04 | 5 | 5 | 3 | 0 | **0** |
| L05 | 2 | 2 | 2 | 0 | **0** |
| L06 | 8 | 8 | 8 | 0 | **0** |
| L07 | 10 | 10 | 10 | 0 | **0** |
| L08 | 15 | 13 | 13 | 0 | **2** |
| L09 | 13 | 0 | 0 | 0 | **13** |
| L10 | 16 | 0 | 0 | 0 | **16** |
| L11 | 15 | 0 | 0 | 0 | **15** |
| L12 | 18 | 0 | 0 | 0 | **18** |
| L13 | 21 | 15 | 14 | 0 | **6** |
| L14 | 20 | 0 | 0 | 0 | **20** |
| L15 | 28 | 0 | 0 | 0 | **28** |
| L16 | 30 | 0 | 0 | 0 | **30** |
| **TOTAL** | **245** | **95** | **89** | **2** | **148** |

**L01 THROUGH L07 ARE DONE.** L08's two open rows are `L08-08` and `L08-15`.

> **A ROW IS FILED AGAINST ONE LESSON; THE CLAIM CAN LIVE IN FOUR FILES (S185, §16.51).** This table
> counts ROWS, not claim sites. `L03-10` was filed under L03 and had two live sites in **L01**, two in
> the **Maker**, and one as a **keyed correct answer** in `QUIZ_L03` — while this table read L01 and L02
> at 0 OPEN. **A lesson at 0 OPEN is a lesson with no rows of its own left, not a lesson with no defects.**
> When closing a row, enumerate the claim across the whole tree before believing the lesson column. Everything else is open, including
both lessons a handoff described as having *had a pass*.

## Named somewhere, still OPEN — do not read a mention as a ruling

| Row | Where it was named | Why it is still open |
|---|---|---|
| `L12-18` | a prior handoff | Named explicitly as **UNRULED**. B4's premise is unsound; nobody has decided what replaces it. |
| `L06-07` `L08-02` | Part 4 D-3, D-4 | *Price it first.* `L08-02` may be the single most expensive item in the review. |
| `L14-01` `L14-04` `L14-13` `L14-14` `L16-11` `L16-12` `L16-13` | Part 4 D-5 | Unverified rulebook claims. `RCJRescueLine2026-final.pdf` is in the repo root and these are checkable in one pass. |

## S181 spot-check: the open rows are live, not stale

Probed at S181 against the tree, in the two lessons a handoff called *passed*:

- **`L12-13`** — §7A: *"Spin it all the way around and it reaches 360."* §8A.3 teaches that
  `getTurnAngle()` wraps through ±180°. **The lesson contradicts itself** and the student who
  follows §7A will not see 360.
- **`L12-07`** — *thousands of times* ×9, including *"measuring the turn thousands of times a
  second"*. Unmeasured, C4.
- **`L12-08`** — *"The IMU costs zero pins"*, twice, once in the **glossary**. It occupies
  SDA/D2 and SCL/D3.
- **`L12-10`** — *"integer math keeps every call cheap and exact."*
- **`L13-13`** — §9 still says carrying a victim needs *"a servo to drive it, and a driver
  channel to spare. Your Zumo's two DRV8838 drivers are both spoken for."* **A hobby servo takes
  power, ground and a signal pin — it does not consume an H-bridge channel.** The conclusion
  survives; the reason is wrong.
- **`L03-10`** — the 4,200 mV damage boundary is asserted at **four distinct sites**: the §3.6
  battery table, the chemistry paragraph, §8 troubleshooting, and Challenge 2's stated goal.

**A probe locates candidates; it never answers.** Each of these was read in context. The needles
that returned zero (`L12-01`, `L12-02`, `L12-06`, `L13-04`, `L13-09`, `L13-12`) are **NOT** recorded
as dead — S179's `L03-01` and S181's own first `L03-07` probe both reported DEAD in error.

---

# PART 1 — THE SIX CANON STATEMENTS

**These are the rulings to make first.** Each one collapses 15–40 individual findings.
Fixing them lesson-by-lesson means fixing L08 three times.

### C1 — TRIM: "Open loop needs TRIM. Closed loop must not get it."
**Appears:** L06, L08, L10, L11, L12, L15 — prose, Brain Checks, glossaries, Quick References, challenges.
**GPT's objection:** too absolute. Feedback and feed-forward bias correction can coexist; a known
static motor mismatch can legitimately be compensated while a feedback loop runs.
**GPT's proposed canon:** *TRIM is a feed-forward straight-drive correction. In this course we
deliberately leave it out of `followLine()` while tuning Kp so the line error is the only steering
correction being studied.*
**My assessment: AGREE.** The narrow pedagogical rule is true and teachable; the universal rule
has to be untaught in L15. GPT calls this its single biggest correction spanning L08–L12.
**Scope if ruled:** 6 lessons, prose only, no byte change. Touches glossary + Quick Reference +
Brain Check banks.

### C2 — Sensor-as-truth language
**Appears:** L04, L06, L08, L09, L10, L11, L12, L13.
**Instances:** "encoders averaged tell the truth" · "gyro reports the truth" · "the encoder measures
INTENT" · "proximity 3 = a block 3 cm ahead" · "green reads 300–700" · "matte black absorbs IR,
reads near-zero" · "silver is invisible to calibrated eyes" · "closed-loop is self-correcting
regardless of conditions."
**GPT's proposed canon:** *A sensor reports a measurement of some physical quantity. Your program
interprets it. Ask: what does this instrument actually measure? What assumptions connect that
measurement to the quantity we care about? How do we test them?*
**My assessment: AGREE, and this is the strongest item in the entire review.** It also gives the
book a spine it nearly has already: L04 reflectance → L05 modulated IR → L06 drivetrain rotation →
L09 classification not colour vision → L11 choose the instrument → L12 interrogate the instrument →
L13 combine imperfect measurements.
**Note:** the titles *Time Lies, Distance Doesn't* and *Wheels Lie* survive this — GPT explicitly
says keep them. The correction is the prose underneath: *the instrument didn't lie; we asked its
number to mean more than it did.*
**Scope if ruled:** 8 lessons, prose + several figure captions.

### C3 — Blocking and the kill switch
**Appears:** L06, L09, L10, L12, L13.
**The claim under attack:** L10 says the phase variable keeps B live "in every state, at every
moment" and "never a delay." But `driveDistance()` and `turnDegrees()` contain blocking `while`
loops, and `OBSTACLE_DETECTED` contains `delay(600)`. During those, `loop()` is not running and B
is not polled.
**GPT's proposed canon:** *A blocking function keeps control inside itself until its job is done.
`delay()` and `driveDistance()` both block — the difference is what tells them to stop (elapsed
time vs. measured rotation). B is the software stop wherever the current code can poll it; the
physical power switch is always the ultimate hardware stop.*
**My assessment: AGREE.** This one is a safety claim, not a style claim — the book currently tells
students a stop button works when it doesn't. It also sets up a genuinely good progression GPT
spotted: L06 blocking → L10 phase memory → L12 checks inside the loop → L13 `driveUntil()` as a
*watchful* blocking primitive.
**Scope if ruled:** 5 lessons. Prose, plus a decision on whether L12's `turnDegreesGyro()` should
poll B inside its loop (that one moves bytes).

### C4 — Unmeasured precision
**Appears:** book-wide.
**Instances:** "fifty times a second" (L08, L10, L11) · "BASE_SPEED 150 ≈ 15 cm/s" (L08 C3) ·
"gyro calibration takes about a fifth of a second" (L12) · "readBatteryMillivolts is ±10%" (L03) ·
"avoid full speed for more than 30 seconds" (L03) · "loop takes 2–3 ms" (L15) · "±19° field of
view" (L10) · every byte figure in L10–L16 · self-test cutoffs 3° and 1800 (L14).
**Existing canon:** §24.15 measured-facts discipline already covers this. **STRUCK as a new item** —
but the *instances* are real and need individual disposition.
**GPT's added value:** a four-way category scheme worth considering — *hardware/library fact
(sourced externally) · fleet measured fact (measured on our robots) · starting value (provisional,
student tunes) · policy value (chosen for safety/consistency).*
**My assessment on the scheme: DJ'S CALL.** It's a good scheme. It's also a new convention, and
rule 76 says scope the defect before building a convention for it.

### C5 — Absolutes
**Appears:** book-wide.
**Instances:** "P alone can never stop weaving" (L15, incl. Brain Check 03) · "errors accumulate and
never cancel" (L12) · "this robot cannot be programmed to stop at a table edge" (L11) · "encoders
work regardless of surface" (L09, L10) · "directional avoidance is physically impossible" (L10) ·
"THESE RETURN 0. Always. Forever." (L10) · "lawnmower sweep guarantees coverage" (L13) · "teams
that skip evacuation cannot win" (L14) · "the only experimental design that proves causation" (L16).
**Existing canon:** §16.16 / rule 61 absolutes pass. **STRUCK as a new item** — instances still need
disposition.
**GPT's useful addition:** some absolutes should stay. *"Every state must name its exit"* is a
pedagogical rule, not a physics claim. The test is whether the sentence is making a claim about
the world.

### C6 — Competition rule vs. RoboLore policy
**Appears:** L13, L14, L15, L16.
**The problem:** official RCJ rules, course adaptations, and team policies are presented in the same
voice. A student can leave thinking the 15-minute acclimation habit or the code freeze is an
international rule — or that finding a victim satisfies the competition rescue requirement.
**GPT's proposal:** three visual labels — **Official RoboCupJunior Rule** · **RoboLore Course
Adaptation** · **RoboLore Team Policy**.
**My assessment: AGREE on the distinction, DJ'S CALL on the labels.** A new callout family is a
component-standard change (rule 46: a callout is never a free edit).
**Blocking dependency:** every rulebook claim below must be settled against
`RCJRescueLine2026-final.pdf` (present in repo root) before it reaches a lesson. GPT's rulebook
claims carry no edition (S154 handoff, triage rules).

---

# PART 2 — PER-LESSON FINDINGS

## LESSON 01 — 15 findings
*Source: `Lesson_01_GPT_Feedback.docx`. GPT rated 4 as P0.*

| ID | Finding | Verdict |
|---|---|---|
| L01-01 | **§6 "Break It On Purpose" is a classroom trap.** Lesson says switch robot power OFF, click Upload, watch it fail. The Zumo 32U4 is designed so USB powers the MCU with the main switch off — upload succeeds. A student following the instructions exactly disproves the book in lesson one. Related: "Upload fails → robot not connected/powered" and "Make sure robot power is ON" in troubleshooting. | **AGREE — P0.** GPT's proposed replacement (invalid `board =` ID → read error → restore → SUCCESS) is deterministic and teaches config diagnosis. |
| L01-02 | **§3.3 + glossary: the Zumo is not built around an A-Star32U4 board.** KEY TERM `term-a-star` and glossary twin `term-a-star-gloss` call it "the brain of your Zumo robot." | **AGREE — P0, CONFIRMED.** DJ ruled S154: fleet is Zumo 32U4 w/ OLED. DJ's rebuttal to GPT cited *Zumo Robot for Arduino* pages — a different product (shield + separate A-Star). **Scope RE-MEASURED at S155 — the S154 figures were `grep -c` LINE counts:** **15** `Lesson_01.html` · **10** `Lesson_03.html` · **2** `newproject.html` · **2** pre-existing Bible · **0** quiz banks. **USE THE INVENTORY, NOT THE TOTAL:** L01's 15 are 5 wrong-claim, **6 CORRECT build-target**, 2 element ids, 2 checklist/quiz; L03's 10 are 8 wrong-claim and **2 asset filename** (`L03_IMAGE_3-14_astar_board.jpg`). **Fix = 3 terms, not a rename:** `Zumo 32U4 Main Board` (hardware) · `ATmega32U4` (chip) · `a-star32U4` (build target only). Absorbs L01-10. **Two open questions needing a ruling first:** the lessons and Maker ship `a-star32u4` LOWERCASE-u in six places while the Bible writes `a-star32U4` twelve times and §16.25 declares uppercase canonical; and §11 of the Bible itself says *"A-Star32U4 capitalization for the microcontroller"*, which §16.25 contradicts. |
| L01-03 | **§4.2 Git presented as required for the Zumo library**, but `lib_deps = pololu/Zumo32U4@2.0.1` is a PlatformIO Registry dependency, not a git source. | **VERIFY — unsettled since S137.** DJ says PlatformIO won't run on Mac without it; GPT folded without testing. Neither settled it. This is queue item "§4.2's audit table is unconfirmed and may not be confirmable." Needs a Mac. |
| L01-04 | **Challenge 9 removes the startup wait and puts a tethered robot on the floor.** No unplug instruction. | **AGREE — P0.** GPT's floor-test ritual (upload raised → SUCCESS → close Serial → disconnect USB → place → power on) is worth making a reusable convention. |
| L01-05 | **Challenge 4 solution is wrong.** Prompt changes only the *first* `delay(350)` to 700; solution says both directions become 700. Actual: 2× forward, ½ back. | **AGREE.** Straight correction. |
| L01-06 | **Challenge 11 has two contradictions.** Hint says low ≈ 4200 mV; solution tests `< 4500`. Scaffold says print voltage on screen; solution prints to Serial only. | **AGREE.** DJ already explained 4200 = NiMH low, 4500 = consistent average — so make the lesson say that. |
| L01-07 | **§4 "today's program touches exactly three things"** (Button A, OLED, yellow LED) but the program also uses buzzer, motors, USB serial — and the Learning Objective lists five. | **AGREE.** Reword rather than enlarge the table. |
| L01-08 | **§1 "B had no `printf`" is false.** B's documentation contains `printf`; the early example used `putchar()` because of B's character constants. Also the figure caption says K&R "introduced" Hello World while prose credits the earlier B tutorial. | **AGREE.** Caption → "popularized." |
| L01-09 | **"exactly copying the very first programmers in history."** Programming predates 1972 by decades. | **AGREE.** C5. |
| L01-10 | **"brain / microcontroller / controller board are the same component."** They aren't: chip vs. PCB vs. informal nickname. | **AGREE.** Absorbed into L01-02's three-term fix. |
| L01-11 | **§3 "that feedback loop is what separates a robot from an appliance"** — a thermostat is closed-loop. Related: the toaster row's "can't really decide." | **AGREE.** C5. GPT's replacement sets up P-control better than the original. |
| L01-12 | **§6.4 "you should hear a USB connection sound"** is Windows-centric. | **AGREE.** DJ asked for wording; GPT supplied it (Windows sound / Mac "Allow accessory to connect?"). |
| L01-13 | **Project path disagrees with itself.** Turn-in says `Documents/PlatformIO/Projects`; template creation says `Documents/PlatformIO`. | **VERIFY** then fix — cheap. |
| L01-14 | **Figure Index incomplete.** `IMAGE 1.14`, `IMAGE 1.18`, `GRAPHIC 1.11`, `GRAPHIC 1.12` used but not all in the table. Column header says *Image* though the list holds both IMAGE and GRAPHIC. | **CONFIRMED — MEASURED, both halves.** L01's body carries 19 figure tags; its index table has 15 rows, and the four GPT named are **exactly** the four missing. All four are **landed figures with captions** — the art renders, only the index row is absent. **L01 is unique:** across all 16 lessons 14 have zero gap; L15's lone gap is `GRAPHIC 15.4`, legitimately outstanding (unshot). Header confirmed as `Image` over a table containing GRAPHIC rows. **Regenerate the table; never hand-patch it.** |
| L01-15 | **Lesson strip titles stale** — nav still reads "Lesson 15 — Advanced PID Control" and "Lesson 16 — Engineering Showcase." Strip is declared byte-identical across all 16. | **VERIFY.** If real, fix in the generator, never per-file. `title_feed.py` exists. |

**L01 lower-priority wording:** "every robot follows Sense→Decide→Act ... 100 times per second"
(the L01 program has an empty `loop()`) · "C++ with no wasted time" · "the compiler checks every
character of your syntax" (it's a toolchain). All **C5 / DJ'S CALL**.

---

## LESSON 02 — 19 findings
*Source: `Lesson_02_GPT_Feedback.docx`.*

| ID | Finding | Verdict |
|---|---|---|
| L02-01 | **§3.1 "Three Builds That Fail" — the examples don't produce the stated errors.** Build 1 has no `#include <Zumo32U4.h>`, so `ledYellow()` is undeclared too — two failures, one acknowledged. Build 3 claims a linker *undefined reference*, but `showCount(5)` against a declared `void showCount()` fails at **compile** time on argument mismatch; `display` is also undeclared. | **AGREE — highest-value L02 item.** This is the section teaching students to trust compiler evidence. Wrong evidence is worse here than anywhere. Each example must produce exactly one intended error. |
| L02-02 | **§8A uses `ledRed()` inside `blinkLED()`** while the whole lesson uses `ledYellow()`. | **AGREE.** Accidental carryover. *(This is the finding DJ named from memory.)* |
| L02-03 | **§8A uses Allman brace style** immediately after §3 declares "this book uses K&R everywhere." | **AGREE.** Either fix the braces or drop the claim; the lesson just taught students to notice the difference. |
| L02-04 | **§3.3 "every program you have written so far has been a straight road."** False — L01's main program used `while` and `for`; C11 previewed `if`. | **AGREE.** C2-adjacent continuity error. |
| L02-05 | **§3.3 says the student already ran an `if` "in the very first warm-up."** Warm-Up 1 is the LED blink; Warm-Up 2 is the first `if`. | **AGREE.** One-word fix. |
| L02-06 | **Code anatomy gives global variables no named home**, yet Challenge 3 introduces three (`countA/B/C`) and §5 spends real time on global scope and SRAM. | **AGREE — cheap, and we've met this bug before.** S51 fixed the *payload* face of exactly this (blank starter missing `// ===== GLOBAL VARIABLES =====`, root-caused to Bible §18.3 naming four of five sections). GPT found the *prose* face. |
| L02-07 | **§7 says "about 85–95 lines"** against a Maker payload GPT claims is nearer 119. | **DISAGREE — MEASURED, GPT IS WRONG.** The L02 `finished` payload is **95 total lines / 86 non-blank / 75 code**. The lesson's stated range is correct. *(Derived by parsing the `PAYLOADS` object out of `newproject.html` and counting `finished` under key `"2"`.)* **No action.** |
| L02-08 | **§4 hardware continuity:** "Lesson 1 used one button, one light, and the screen" and "the motors ... still idle, exactly as in Lesson 1" — but L01 used motors and buzzer, and Warm-Up 4 literally spins the motors. | **AGREE.** Same defect class as L01-07. |
| L02-09 | **Step 2's comment teaches the generic baud rule** (`// 115200 = the speed; the Serial Monitor must match it`) while the lesson correctly explains a few paragraphs later that native USB ignores it. | **AGREE.** Touches the carried "1200-baud reset has no home" and "baud bench test" queue items. |
| L02-10 | **Step 3 Button C: "change one letter in two places — the build tells you which one you missed."** Not true: `Zumo32U4ButtonC buttonA;` compiles fine while the name lies. | **AGREE, and GPT's replacement is better than the original** — it becomes a *compiling ≠ correct* lesson, which is a course theme. |
| L02-11 | **Comments philosophy alternates** between "comments explain WHAT and WHY" and "the code already says WHAT; comments explain WHY." | **AGREE.** Reconcile to the later version. |
| L02-12 | **"Every local variable lives in the stack"** — implementation simplification; locals can live in registers or be optimised away. | **DJ'S CALL.** Technically right but this is a deliberate beginner model. Softening costs little; so does leaving it. |
| L02-13 | **"Two objects for the same motor would fight over it"** — too literal. | **AGREE.** C5. |
| L02-14 | **Step 7 procedural ambiguity:** "replace any LED code with `blinkLED();`" for B and C, but only A got LED code in Step 5. | **AGREE.** Cheap wording fix. |
| L02-15 | **Challenge 2 behaviour bug:** A+B shows the battery screen, then the individual A and B checks below immediately overwrite it with About/Controls. L07's version solves this with a release-wait. | **VERIFY then AGREE.** GPT's fix reuses `while` from L01 — good spiral. |
| L02-16 | **"Seven Sections ... every program has these sections in this order."** Not a C++ fact — it's a RoboLore standard. | **AGREE, and GPT's reframe is better:** *"Every RoboLore program uses this organisation. Some sections may be empty, but they always have a home."* Also enables a strong L01→L02 bridge (the empty banners they copied into `ZUMO_Template`). |
| L02-17 | **MY PLAN is absent from L02's teaching** despite the Maker payload containing the block and the lesson using pseudo-code boxes throughout. | **DJ'S CALL.** GPT proposes L02 = "receive a plan, translate it," building to L07 = "write the plan." Good arc; it's a design decision. |
| L02-18 | **Debrief lands on "professional programmers use COMMENTS"** when the lesson teaches comments + naming + sections + constants + helpers + prototypes + structure. | **AGREE.** Small reframe. |
| L02-19 | **Warm-Up 4 is unlabelled spiral retrieval** of L01 C8's differential-drive idea. | **DJ'S CALL.** GPT suggests marking it explicitly ("You saw this in Lesson 1. Can you recover it without going back?"). Consistent with existing spiral-marker canon. |

---

## LESSON 03 — 10 findings

| ID | Finding | Verdict |
|---|---|---|
| L03-01 | **§§5/6 contradict each other about the file's starting state.** Step 2 says keep the empty `setup()`/`loop()`; Step 4's checkpoint says "the compiler can't check your work yet (no setup()/loop() exists)." | **AGREE.** GPT's replacement is a stronger teaching moment than the original. |
| L03-02 | **Step 3 conflicts with the Maker/header workflow.** Step 2 says the Maker pre-filled the header; Step 3 says "copy the code above and paste it into your empty main.cpp" — which isn't empty and would create a second header. | **AGREE.** Also an anti-copy/paste win: make them *complete* the header rather than paste one. |
| L03-03 | **Part 2 prerequisite still says "Your Zumo_Lesson_2 project folder (we'll copy it)"** — stale; §5.1/§6 use the Maker for a fresh `LastName_L03`. | **AGREE.** Stale workflow language. |
| L03-04 | **§4.1 "this lesson introduces motor control."** L01 already drove the robot including differential movement; L02's warm-up spun it. | **AGREE.** Same class as L01-07/L02-08. GPT's replacement ("today motor control becomes the main subject") is a better transition. |
| L03-05 | **§5.3 and §8A.3 call manual TRIM tuning "closed-loop tuning"** immediately after §3.3 correctly defines the robot's motor control as open-loop. | **AGREE — C1-adjacent.** The robot is still open-loop. GPT: call it *manual iterative tuning* or *human-in-the-loop calibration* and keep "closed-loop control" pristine for L06/L08. |
| L03-06 | **§4.5 Drift Test and §3.19 hand-turn prediction.** Pushing an unpowered robot measures rolling resistance, not which powered motor runs faster under voltage. | **AGREE.** Keep the inspection, drop the prediction. Strengthens *inspect → hypothesise → controlled test → trust the measurement*. |
| L03-07 | **§3.25 duplicates L01 Challenge 6.** Same three repeated timed runs, same scatter observation — and L01 C6 explicitly told students to keep the data for Lesson 3. | **AGREE, strongly.** Retrieval beats repetition: *"Open your Lesson 1 notebook. Were the three measurements identical?"* This is more Saxon than repeating the experiment. |
| L03-08 | **"Avoid full speed (400) for more than 30 seconds without a cooldown."** No support found; Pololu's concern is load/current, not a speed-duration rule. | **AGREE — C4.** GPT's replacement teaches the right mechanism (current, not the speed number). |
| L03-09 | **§4.3 "`readBatteryMillivolts()` is approximately ±10%."** Not in Pololu's documentation. | **VERIFY / C4.** If it isn't a RoboLore fleet measurement, it has no pedigree. |
| L03-10 | **"Below 4200 damages the cells."** 4200 mV is a course recharge threshold, not a damage boundary. Also the alkaline-competition aside introduces a variable the lesson doesn't need. | **AGREE — C4/C5.** Keep "at or below 4200: stop and recharge" as course policy. Alkaline paragraph is **DJ'S CALL** (carried queue item: "L05 §3.6 alkaline tension"). |

**Verified as CORRECT by GPT (no action):** `setSpeeds(0,0)` = brake for the DRV8838 (TI PH/EN truth
table) · the 20 kHz Timer-1 phase-correct PWM explanation with TOP 400 · stall current ≈ 1.6 A at 6 V
for the 75:1 HP motor. GPT would only soften "20 kHz is chosen for your ears' sake."

---

## LESSON 04 — 5 findings (mostly pedagogy)

| ID | Finding | Verdict |
|---|---|---|
| L04-01 | **Arrays are taught twice** — L03 §8A.5 (indexing, zero-based, out-of-bounds) and again L04 §5.5. | **DJ'S CALL, and GPT's recommendation is sound:** make L04 the real array lesson, because five sensor readings give arrays their first compelling physical purpose. Demote L03 §8A.5–8A.6 to optional preview. |
| L04-02 | **§8A re-teaches `if` anatomy from scratch** after L02 introduced it and L03 taught comparisons, `else if`, and the `=` vs `==` trap. | **DJ'S CALL.** GPT: keep §8A (L04 is where the condition becomes live sensor data) but cut the basic syntax review. |
| L04-03 | **Continuity line will break if L03 arrays are demoted:** "Lesson 3 promised the line sensors would hand you data 'as an array,' and its §8A.5 gave you the tool." | **AGREE** — but only conditional on L04-01 being ruled. |
| L04-04 | **§3.4 and §5.7 both re-explain calibration.** GPT: make §3.4 the conceptual model and §5.7 only the code mechanics. Same for Step 6 vs §7.1 (discovery vs. measurement). | **DJ'S CALL.** |
| L04-05 | **Challenge 1 "Line Light" duplicates §8A.3's worked example** almost exactly. | **DISAGREE with GPT's first verdict, AGREE with its revised one.** GPT initially said cut it, then revised after learning the Saxon design: keep it as a *short retrieval challenge* with no fill-in-the-blank template. The revision is right. |

**Marked KEEP by GPT (protect):** the three-eyes → five-eyes arc · Step 7's deliberate
software-first mismatch (a program that compiles perfectly but is physically wrong) · Challenge 2
Line Counter · Challenge 4 Edge Guard · Challenge 5 Centering Game.

---

## LESSON 05 — 2 findings
*Shortest document. Overwhelmingly positive — GPT calls L05 the clearest evidence the book is a
programming curriculum whose laboratory happens to be a robot.*

| ID | Finding | Verdict |
|---|---|---|
| L05-01 | **§5.15 re-teaches full `for`-loop anatomy** (push-up analogy + anatomy graphic) after opening correctly with "You already own this tool." L04 did the complete anatomy. | **DJ'S CALL.** The genuinely new material is loop + `if` to draw a gauge, and counting down with `i--`. |
| L05-02 | **Step 4 stages the `'readAllSensors' was not declared` error for the third time** (L02, L04, L05). | **AGREE with the principle, DJ'S CALL on the fix.** GPT's *first: explain / second: remind / third: expect / later: combine* rule is a good spiral discipline. By L05, omit the prototype and see whether they catch it. |

---

## LESSON 06 — 8 findings, one a real code bug

| ID | Finding | Verdict |
|---|---|---|
| L06-01 | **REVERSE TRIM BUG.** `int speed = (distanceCm > 0) ? DRIVE_SPEED : -DRIVE_SPEED;` then `motors.setSpeeds(speed + TRIM, speed);`. With TRIM=+15: forward `165,150` (correct); backward `-135,-150` — the weak left motor is made **weaker in magnitude**. The correction must reverse with direction. Propagates to Smooth Stopping, Smooth Acceleration, L07 (Ch 1 `driveBackward()`, Ch 4, Ch 7), and L13 Challenge 1's `driveDistance(-10.0)`. | **AGREE — this is the most important code finding in the review.** Not currently in the S154 queue. **AGREE-EXPENSIVE:** moves bytes, needs the toolchain, and touches a chain of lessons. Fix in L06 first and carry the corrected function forward. |
| L06-02 | **§3.6 contradicts Step 13 on open vs. closed loop.** §3.6: "run motors until encoders show 30 cm = Closed-Loop, self-correcting regardless of conditions." Step 13: "OPEN LOOP needs TRIM," calling `driveDistance()` open-loop. | **AGREE — C1/C2/C5, GPT's #1 L06 item.** Both are true of *different control variables*: closed-loop w.r.t. wheel rotation, open-loop w.r.t. heading. GPT's two-question rewrite (distance feedback / heading feedback) is excellent prep for L08. Delete "regardless of conditions." |
| L06-03 | **"The encoders cannot see a curve" / "no encoder anywhere on this robot can see a curve."** Two wheel encoders detecting unequal travel is exactly how differential-drive odometry estimates heading change — and L05 already told students to combine for travel, difference for turning. | **AGREE.** What encoders can't do is prove rotation became *ground* travel. Keep the line "the dashboard says you drove straight; the floor says otherwise" — revise the explanation under it. |
| L06-04 | **The 440 cm ceiling explanation is incomplete.** Lesson blames `int targetCounts`, but Pololu's `getCountsLeft()/Right()` return `int16_t` and overflow 32767 → −32768. Changing to `long` alone doesn't allow longer moves. | **VERIFY then AGREE.** GPT's version is a better programming lesson (periodically read/reset and accumulate). |
| L06-05 | **§3.1 "As poles pass: North → South → one count."** The library counts valid A/B transitions; 12 counts/rev comes from both edges of both channels. | **AGREE.** Connects better into the quadrature waveform that follows. **12 × 75.81 ≈ 909.7 is confirmed correct.** |
| L06-06 | **§4.1 "encoders start counting automatically when the robot powers on."** The first half (no explicit `init()` call needed) is right; the getters call `init()` internally on first use. | **AGREE.** Small accuracy fix. |
| L06-07 | **`WHEEL_BASE_MM` is the wrong term.** Wheelbase = front-to-back axle distance. The quantity here is left-to-right track separation → `TRACK_WIDTH_MM` or `WHEEL_SEPARATION_MM`. | **AGREE on the terminology, AGREE-EXPENSIVE on the rename.** Touches L06, L07, TDP template A4 (which asks students to verify the book's 85 mm), quiz banks, and any Maker payload naming it. **Price before ruling (rule 70).** |
| L06-08 | **§8A re-teaches "what IS a function?"** by Lesson 6, after L02 treated functions, L05 had `drawBar(row,value)`, and L06 just wrote `driveDistance(float)` and `turnDegrees(float)`. Also the sandwich analogy's "Result: a sandwich!" conflicts with the `void` functions being taught. | **DJ'S CALL, and GPT's reframe is strong:** rename to *Passing Values Into Functions — Parameters Make One Function Do Many Jobs*, drop the sandwich, use the real robot functions as the examples. |

**Also:** "calculate exactly how far / drive exact distances / turn precise angles" — **C5**.
"Today the robot drives itself for the first time" / motors "finally move!" — inconsistent with
L01/L03/L05; GPT's *"Today movement becomes measured"* is a better L06 identity. **AGREE.**
C5 Odometer's `totalDistance`, `prevLeft`, `prevRight` are mutable state sitting in
`CONFIGURATION` — belong in `GLOBAL VARIABLES`. **VERIFY then AGREE** (touches the carried
"CONSTANTS vs CONFIGURATION drift" item).

---

## LESSON 07 — 10 findings

| ID | Finding | Verdict |
|---|---|---|
| L07-01 | **§3.6 `#pragma once` is taught incorrectly.** Lesson says a twice-included header makes the compiler see `driveDistance()` declared twice and get confused. Repeated identical function *declarations* are legal C++. The real risk is contents that cannot be repeated in one translation unit. | **AGREE.** |
| L07-02 | **"`#pragma once` is the modern standard."** It's a widely supported compiler extension, not ISO C++. Traditional include guards are the portable standard. | **AGREE.** Keep using it — just describe it accurately. |
| L07-03 | **"Circular includes: `#pragma once` prevents this automatically."** It prevents endless preprocessing, not circular dependency design problems. | **AGREE.** GPT's version is also a better architecture lesson. |
| L07-04 | **§8A: "Writing `extern` in the .cpp file is a linker error."** False — `extern Zumo32U4Motors motors;` in a .cpp is legal; it declares without defining. The error comes from no definition existing anywhere. | **AGREE.** Keep the house rule; drop the claim that C++ forbids it. |
| L07-05 | **Error 6: "a function body in a header produces `expected ';' before '{'`."** False — a function definition in a header is legal syntax; the risk is ODR/multiple-definition. Students will open a real library, see bodies in headers, and think it's broken. | **AGREE.** |
| L07-06 | **Step 7 says "three includes (which three?)"; the reveal has four.** | **AGREE.** GPT's better option: ask *which headers does this .cpp actually need?* |
| L07-07 | **Reverse-TRIM bug carried from L06** into `driveDistance()`, Challenge 4, and Challenge 7 — and Challenge 1 explicitly builds `driveBackward()`. | **AGREE.** Fix L06 first (L06-01), carry forward. |
| L07-08 | **Challenge 4 teaches the opposite of L07's lesson.** It creates `driveDistanceSlow()`/`driveDistanceFast()` by copying the whole implementation of `driveDistance()` and changing one constant. | **AGREE, and this is a strong opportunity.** GPT: introduce `driveDistanceAtSpeed(float cm, int speed)` and make the two wrappers one-liners. Teaches *parameterise the difference, don't duplicate the algorithm* — a real deepening of L06 parameters, and it makes Ch 1/2's wrappers part of a coherent interface lesson. |
| L07-09 | **Challenge 7 isn't a trapezoidal profile.** The code does half → full → half in three discrete plateaus. A trapezoidal velocity profile has an acceleration ramp, constant section, and deceleration ramp. | **AGREE.** GPT prefers renaming to *Three-Stage Motion Profile* at L07 and saving the true continuous profile for Going Deeper. Sensible — the math would compete with the architecture lesson. |
| L07-10 | **§8A is a second full lecture** immediately after §3.2–3.7 and the whole build: declaration/definition, `extern`, and scope all taught again nearly from scratch. | **DJ'S CALL.** GPT: convert to retrieval/diagnosis (*which of these four lines are declarations? the compiler succeeded but the linker failed — what does that tell you?*). |

**Also:** the tuning section says "place a ruler on your **desk**" then drive — should be floor,
matching L06/L07 elsewhere. **AGREE (safety).** `RobotConfig.h` `BATTERY_GOOD = 4800 // fully
charged` would make a normal classroom pack report LOW; GPT suggests operational statuses
(READY / GETTING LOW / RECHARGE). **DJ'S CALL — C4.**

**Marked KEEP by GPT (protect):** Step 4's deliberate linker failure (a genuinely new species of
error, created exactly when it becomes meaningful) · MY PLAN as the scaffolding drop · the whole
Observation section (predict → break → build → explain → undo) · the TRIM journey line *"It was
born in Lesson 3, spent in Lesson 6, and filed here."*

---

## LESSON 08 — 15 findings

| ID | Finding | Verdict |
|---|---|---|
| L08-01 | **The lesson contradicts itself on scaffolding.** The opening announces a "Hybrid Approach" (read pseudocode → fill skeleton → compare), but §6 correctly says "same as Lesson 7 — no pseudo-code provided — write your plan before you touch code." | **AGREE.** L07 was the graduation point; the opening notice walks it back. Keep §6's model. |
| L08-02 | **`followLine()` is in the wrong file.** L07 teaches main.cpp = WHAT, modules = HOW, and even names `followLine()` as a behaviour function. L08 insists it live in main.cpp only, and troubleshooting treats putting it in RobotMotion.cpp as an error. | **AGREE that it contradicts L07. AGREE-EXPENSIVE on the fix.** GPT's `followLine(float kp)` in RobotMotion is architecturally right and removes §8A.1's "a better approach would be parameters..." hedge. But moving it ripples through L08–L16 payloads and byte figures. **Price before ruling.** |
| L08-03 | **No hardware checkpoint before `initFiveSensors()`.** Five-sensor mode requires pin 20 → DN2 and pin 4 → DN4. Software can be perfect while the jumpers are wrong. | **AGREE.** GPT's *Spiral Check — Lesson 4 hardware* is good Saxon: don't reteach the shared-pin story, make them retrieve it because the code now depends on it. |
| L08-04 | **§8A.2 explains `readLine()` incorrectly.** Lesson says a weighted average of five zeros "still produces an answer; it just doesn't mean anything." The bundled QTR code doesn't do that — with no sensor over threshold it returns the *last known side's extreme* (0 or 4000). | **VERIFY against the bundled QTR in `Zumo32U4@2.0.1`, then AGREE.** The actual behaviour is a better lesson: understanding what a library *promises* rather than guessing from its name. |
| L08-05 | **"One reading, two questions" performs two readings.** The example calls `readCalibrated()` then `readLine()`, and `readLine()` calls `readCalibrated()` again. | **VERIFY then AGREE.** `readLine(sensorValues)` already fills the array — GPT's version genuinely is one read, two pieces of information. |
| L08-06 | **`lastPosition` is dead state.** Assigned and returned; nothing else uses it. The library maintains its own `_lastValue`. | **AGREE.** Teaches "state should exist because something needs to remember it," not because it sounds useful. |
| L08-07 | **`isLineVisible()`'s description doesn't match its code.** Table says "check if any sensor sees the line"; code sums all five and compares to a threshold. Five small readings can cross 200 with no individual sensor above 200. | **AGREE.** Either rename the description or change the implementation to a `for`+`if` any-sensor test (which also retrieves L04). |
| L08-08 | **"Explain why a closed loop must not get TRIM" / "add TRIM there and the robot fights its own controller."** | **AGREE — C1.** This is the canonical instance. |
| L08-09 | **`handleGap()` is described as "coast straight"** but commands `setSpeeds(BASE_SPEED + TRIM, BASE_SPEED)` — that's powered driving. | **AGREE.** Coast implies removing drive power. |
| L08-10 | **"`followLine()` reads the line fifty times a second."** Nothing measures the loop rate, and the current code performs more than one sensor read per cycle. | **AGREE — C4.** |
| L08-11 | **The thermostat example contradicts its own paragraph.** It's listed under proportional control immediately after explaining bang-bang is right for binary actuators — and a household thermostat is the textbook bang-bang/hysteresis example. | **AGREE, and GPT's fix is better than removal:** turn it into a retrieval question — *"Your home furnace may be a case where bang-bang makes perfect sense. Why?"* |
| L08-12 | **Challenge 3 Gap Gauntlet invents a unit conversion:** "at BASE_SPEED=150, robot travels ~15 cm/sec." Motor command is not velocity. Especially awkward three lessons before *Time Lies, Distance Doesn't*. | **AGREE — C4, and it becomes a better exercise:** measure your robot's actual cm/s, predict crossing times for 5/10/15 cm gaps, test the prediction. Plants a seed L11 deliberately overturns. **Note: this is already a bench item ("cm/s at a stated BASE_SPEED").** |
| L08-13 | **Challenge 4 says "20-column display."** `setLayout21x8()` gives 21 columns, indexed 0–20. Mapping 0–4000 → 0–20 is correct; the label isn't. | **VERIFY then AGREE.** |
| L08-14 | **Challenge 4's `drawPositionBar()` re-reads the sensors** after `followLine()` already read them — steering decision and displayed marker come from different observations. | **AGREE.** Raises a good design question about sharing one measurement. |
| L08-15 | **Challenge 6 "Racing Line" calls the speed rule a second closed-loop controller.** It maps line-position error to a speed command; it doesn't measure actual speed. | **AGREE.** Call it a *proportional throttle rule*. Similarly Challenge 5 Adaptive Kp is gain scheduling, not PID. |

**Marked KEEP by GPT (protect):** the entire sabotage section — *upload → observe symptom → predict
culprit before opening files → find → fix → prove*. Mystery 1 (reversed feedback sign → runaway)
and Mysteries 3+5 (*same symptom ≠ same cause*) singled out. Also: the visible Saxon thread
markers, which GPT says send exactly the right message — *you aren't learning another pile of new
things; you're becoming more powerful with things you already know.*

---

## LESSON 09 — 13 findings

| ID | Finding | Verdict |
|---|---|---|
| L09-01 | **"Green absorbs some IR and reflects the rest, producing 300–700"** taught as general fact. The sensors measure IR reflectance, not visible colour. Also "bright safety green works well; dark forest green may read too close to black." | **AGREE — C2.** The lesson already contains the right solution (the Green Survey). Let the measurement establish the premise. |
| L09-02 | **The Green Survey collects one number per material** and brackets green ±100. | **AGREE.** GPT: 5–10 readings per material, record ranges, and ask *is there actually a clean gap between these distributions?* If green 570–850 and black 790–1000, no threshold pair will work — change the material. Much richer than "read one number, invent ±100." |
| L09-03 | **`checkForIntersection()` is misnamed.** It detects *markers*, not intersections — an unmarked four-way returns `NO_INTERSECTION` while the robot sits on an intersection. | **AGREE on the principle** (*name a function after what it measures, not what you hope to infer*). **AGREE-EXPENSIVE on the rename** to `readMarker()` / `NO_MARKER` — check quiz banks and Maker payloads first. |
| L09-04 | **The kill switch isn't a kill switch.** B is checked only in `FOLLOWING_LINE`. `AT_INTERSECTION` sits in `delay(600)`; `EXECUTING_TURN` calls blocking `turnDegrees()`. The lesson demonstrates this itself in Step 7. | **AGREE — C3, and this is a safety claim.** GPT's framing is a genuinely good state-machine lesson: *some events belong to a state; safety events belong above the states.* |
| L09-05 | **Encoder-turn claims: "battery independent," "surface independent," "immune to battery sag," "precise angle measurement," "battery sag and TRIM cannot bend it."** | **AGREE — C2/C5.** Encoder turns are far less battery-sensitive than timed turns; surface grip and track scrub still matter. |
| L09-06 | **"Tank turns have zero turn radius."** True for an ideal differential-drive model; a tracked Zumo skid-steers. | **AGREE — C5.** *"intended to rotate approximately in place, with a nominal zero-radius path for the robot centre."* |
| L09-07 | **Challenge 3's line-seeking `do…while` can spin forever** if the robot misses the line, calibration is wrong, or it's physically stuck. | **AGREE.** By L09 an unbounded motor loop shouldn't be taught. GPT's timeout version combines encoders + sensors + timeout + state-machine safety. Keep the phrase *"Encoders for the bulk, sensors for the landing."* |
| L09-08 | **Challenge 4's `MARKER_ADVANCE_CM` is the wrong physical quantity.** Sensor-to-axle offset alone ignores that the marker sits *before* the intersection. | **AGREE.** Rename to `INTERSECTION_ADVANCE_CM` and determine it experimentally — an effective calibration constant, like the turning geometry. |
| L09-09 | **Challenge 1 compares two different sensor moments** — prints one `readCalibrated()` then calls `checkForIntersection()`, which reads again. | **AGREE.** GPT's `classifyMarker(const unsigned int vals[])` separates acquisition from interpretation — a natural L07 deepening. |
| L09-10 | **Challenge 5: "a real marker still delivers three reads with ease."** Depends on robot speed and loop frequency. | **AGREE — C4.** Three reads is fine as a starting value; say so. |
| L09-11 | **Challenge 6 is not a right-hand-rule maze solver.** The algorithm is "all five black → turn right; line gone long enough → U-turn." A real right-hand rule needs to know which branches exist. The lesson's own glossary defines it correctly. Also the 2026 rules don't prescribe a right-hand rule — an unmarked intersection is traversed straight. | **AGREE — needs the most substantive rewrite in L09.** Either rename to *Always-Right Experimental Policy* and say it isn't a maze solver, or build genuine branch selection. |
| L09-12 | **Missing-`break` sabotage trace is slightly wrong.** Fall-through from `FOLLOWING_LINE` enters `AT_INTERSECTION` *in the same pass*, but that case has its own `break`, so it exits there; `EXECUTING_TURN` runs on the *next* pass. Also "what single character is missing?" — `break;` isn't one character. | **AGREE.** In a lesson specifically about control flow, the exact sequence matters. |
| L09-13 | **§8A absolutes:** "switch(currentState) is *the* standard way" → *a common and very readable way*; "a RobotState variable can only hold one of the four names" → too strong. | **AGREE — C5.** GPT notes §8A here is *earning* its space (enums and FSMs really are new in L09) — unlike L07/L08. |

---

## LESSON 10 — 16 findings

| ID | Finding | Verdict |
|---|---|---|
| L10-01 | **The phase variable doesn't deliver what the lesson promises.** L10 says one thing per pass leaves the loop free — "it checks the kill switch, it reads the sensors, the robot is awake" — and that B works "in every state, at every moment." But each phase calls blocking `driveDistance()`/`turnDegrees()`, and `OBSTACLE_DETECTED` contains `delay(600)`. | **AGREE — C3, GPT's #1 L10 item.** The phase variable solves *sequence memory*. It does not make the primitives non-blocking. |
| L10-02 | **"The encoder fix solves delay blindness" is false.** `driveDistance()` contains `while (averageCounts() < target) { delay(10); }`. Encoders fix *how far*, not *can my program do something else while moving*. | **AGREE, and GPT's framing is excellent teaching:** two separate problems, two separate solutions. |
| L10-03 | **Step 5's "live" proximity display isn't live.** `display.print(readFrontProx())` is added to `showStatus()`, which is called on status/Kp change — not continuously. Student sees one frozen number and concludes the sensor is dead. | **AGREE.** GPT's throttled 200–500 ms refresh also retrieves `millis()` and static memory. |
| L10-04 | **§3.4: "the proximity sensor says there is a block 3 cm in front of you."** The count is how many emitter brightness levels activated the receiver (defaults 4, 15, 32, 55, 85, 120) — not centimetres. Also "at 5 you are nearly touching." | **AGREE — C2.** Threshold 3 becomes an *empirically chosen policy*, which is better teaching. |
| L10-05 | **"Matte black absorbs IR. Reads near-zero even when touching."** Same trap as L09's green. | **AGREE — C2.** GPT's retrieval experiment (white/black/shiny/angled cardboard at the same distance) is a stronger sensor lesson. |
| L10-06 | **The strongest five-line/one-prox wording outruns the evidence:** "THESE RETURN 0. Always. Forever." · "everything outside FRONT's ±19° is now invisible, permanently" · "directional avoidance is physically impossible." | **AGREE — C5, and this is already a bench item.** The pin architecture is well grounded; the behavioural absolutes are not. Hold the conservative wording until the bench test. |
| L10-07 | **The `extern` deliberate error explanation conflates two mechanisms.** With this code, the header *defines* `proxSensors` and the .cpp defines it again — a redefinition in the same translation unit, before any cross-file multiple-definition problem. | **AGREE.** |
| L10-08 | **Staging the `extern` error a third time is repetition, not spiral.** | **AGREE.** *First: explain. Second: remind. Third: expect.* Don't deliberately break correct work so students can re-experience a mistake they've learned. |
| L10-09 | **§7A–7E is an enormous timed-motion ladder** (timed 90°, timed 30 cm, combined, timed square, encoder square) proving what L03 and L06 already taught — **and it is most of Lesson 11's argument.** L11 is literally titled *Time Lies, Distance Doesn't*. | **AGREE, strongly.** Cut most of 7A–7E; keep one short failure contrast. L11's §7E is the right home for the experiment. **This is the single largest cut GPT proposes anywhere in the book.** |
| L10-10 | **The square is over-spiralled.** L03 timed → L06 encoder → L07 modular is a good arc. L10 redoing timed corner → timed square → encoder square adds little. | **AGREE.** At this point retrieve the conclusion, don't repeat the experiment. |
| L10-11 | **Encoder absolutes:** "same result on fresh and tired packs," "encoders make sure it goes 20 cm," "turn 90 degrees." | **AGREE — C2/C5.** |
| L10-12 | **"Open loop needs TRIM. Closed loop does not."** | **AGREE — C1.** |
| L10-13 | **"Fifty times a second"** repeated here. | **AGREE — C4.** |
| L10-14 | **Two bookkeeping-only phases.** `PHASE_SEEK_LINE` only records `returnStartTime`; `PHASE_COMPLETE` only sets the next state. Both jobs fit at the end of `PHASE_TURN_BACK`. | **DJ'S CALL.** GPT: seven phases → five physical phases. Reasonable, but it's a design change to a lesson whose subject *is* the phase architecture. |
| L10-15 | **"Priority is just the order of your if statements."** True of this implementation; arbitration is broader (priority numbers, event queues, behaviour trees, schedulers). | **AGREE — C5.** Small wording change. |
| L10-16 | **Byte claims (+50, +194, +660, 20,516) asserted in prose.** | **AGREE — C4.** *(Note: 20,516 is our standing L11 `after_step_1` control figure — verify which lesson's prose is quoting it and whether the context is right.)* |

**Marked KEEP by GPT (protect):** arbitration as the genuinely new concept · the *fact vs. policy*
distinction (`readFrontProx()` = fact, `checkForObstacle()` = policy) · the debugging ladder
**sensor → state → motion** · `RobotState` = which chapter, `AvoidPhase` = which paragraph.

---

## LESSON 11 — 15 findings

| ID | Finding | Verdict |
|---|---|---|
| L11-01 | **`averageCounts()` is not a safe odometer.** `abs()` around cumulative signed-16-bit counts; `travelled = averageCounts() - gapStartCounts` subtracts averages of absolute cumulative positions rather than measuring each wheel's change since the gap began. Rollover at ±32768 is reachable. | **AGREE — GPT's #1 L11 item.** Cleanest fix for beginners: reset the encoders when the gap starts. *"The line vanished. Zero the odometer. Now every count belongs to this gap."* |
| L11-02 | **"One encoder can lie. Two encoders, averaged, tell the truth."** This sets up exactly the misconception L12 exists to break. | **AGREE — C2, and it's the clearest single instance in the book.** GPT's rewrite makes L11 *foreshadow* L12 instead of contradicting it. |
| L11-03 | **"If the left wheel slips, it under-reports."** Backwards — slip means rotation without ground travel, so the encoder *over*-reports. Sabotage Mystery 1 has the same error. | **AGREE.** |
| L11-04 | **The cliff section overclaims.** "This robot cannot be programmed to stop at a table edge" / "there is no number, there is no such threshold" — asserted before measuring. Raw QTR readings rise as reflectance falls, with a configurable timeout; whether tape and air are indistinguishable depends on calibration, height, and the actual materials. | **AGREE — C5.** Keep the engineering conclusion, which is excellent (*does anything on this robot measure the quantity I am reasoning about?*). Make it experiment-led. |
| L11-05 | **Move the cliff measurement into the required core.** The learning objective demands students explain *with readings they took themselves*, but the measurement is Challenge 5 (optional). | **AGREE.** Objective and structure disagree. |
| L11-06 | **Glossary contradicts the lesson.** IR reflectance entry says "a cliff and **white paper** look identical"; the whole lesson argues cliff and **black tape**. | **AGREE.** Definite error, cheap fix. |
| L11-07 | **GRAPHIC 11.3's caption says "all five must read white before the robot calls it a gap"** — but `isLineVisible()` uses a combined sum threshold. | **AGREE — and note the dependency:** the caption must match whatever L08-07 resolves. Rule 36: a fact that lives only in an SVG is still a fact. |
| L11-08 | **"Open loop needs TRIM. Closed loop does not."** — appears in §5.2, §7C, §8A.1, Challenge 3, Challenge 4, Brain Check 03, glossary, Quick Reference. | **AGREE — C1.** GPT explicitly says fix globally, not piecemeal. This lesson has the most instances. |
| L11-09 | **"50 times a second"** repeated. | **AGREE — C4.** |
| L11-10 | **Byte and geometry figures in prose:** 20,702 bytes, +186, 7,970 headroom, "about 74 counts per centimetre." | **AGREE — C4.** The counts/cm figure must come from the configured geometry in `RobotConfig.h`, not prose. |
| L11-11 | **7A's `GAP_MAX_CM = 999.0` removes any software distance limit**, and 7B says "run the robot off the end of the line" immediately after the cliff discussion. | **AGREE — safety wording.** Require explicit floor-only conditions with ≥1 m of clear runout. |
| L11-12 | **7E promises a deterministic outcome** ("tired battery → it fails"). Whether it fails depends on gap and pack. | **AGREE.** *The lesson shouldn't require nature to cooperate with a predetermined reveal.* Set the gap near the timer's margin, or compare measured distance under two battery conditions. |
| L11-13 | **Challenge 4 "Prove Your TRIM" predicts a symmetric result** from doubling TRIM. Plausible in a linear region, not guaranteed. | **AGREE.** Turn it into a prediction to test — then an unexpected result is data, not a wrong answer. Excellent spiral back to L03 either way. |
| L11-14 | **`handleGap()` does four jobs** — initialises measurement, changes global state, checks the budget, drives motors — so a function named "handle" hides the state transition. | **DJ'S CALL.** GPT flags it as a fading-scaffold upgrade opportunity (`beginGapCrossing()` / `updateGapCrossing()`), not a must-fix. |
| L11-15 | **Sabotage Mystery 1 rewrite.** From "why does averaging both tell the truth?" to *"why is one wheel a worse estimate than two — and why can two still be wrong?"* | **AGREE.** Technically correct and a better L12 teaser. |

**Marked KEEP by GPT (protect):** *"Lesson 8 asked have I been blind for too LONG? Lesson 11 asks
have I been blind for too FAR?"* · the instrument-swap-inside-the-box payoff for L07 modularity ·
`GAP_CROSSING` / `LINE_LOST` as *a state with a resource budget* · *"Nothing reads it is not the
same as nothing mentions it"* · the whole old-and-new-instrument-coexist build sequence.
**Keep the title.**

---

## LESSON 12 — 18 findings

| ID | Finding | Verdict |
|---|---|---|
| L12-01 | **The gyro becomes "truth" too quickly:** "Gyro: reports the truth" · "the robot's real angle" · "stops the motors at exactly the right moment" · "every corner is a real 90 degrees" — contradicting the lesson's own bias/drift section. A gyro measures angular *rate*; the program integrates it into an *estimate*. | **AGREE — C2.** GPT's framing is the right one: *every instrument has a model and limitations; choose the one whose assumptions match the question.* |
| L12-02 | **§3.1 "the encoder measures INTENT, not RESULT."** Catchy but wrong — the motor command is intent; the encoder measures a real physical result (drivetrain rotation) that isn't chassis motion. | **AGREE.** GPT's alternative — *"the encoder measures one result, but not necessarily the result you care about"* — is better and keeps the punch. |
| L12-03 | **"The rubber failed."** | **DJ'S CALL.** Rhetorical. GPT's *"the assumption connecting wheel rotation to floor motion failed"* is more interesting but less punchy. |
| L12-04 | **Gyro bias wording overstates the source.** Pololu says the zero-rate level *can be as high as* 25°/s; the lesson says a still gyro "routinely reports up to 25°/s." Also bias and drift are conflated. | **AGREE.** The arithmetic example (20°/s × 3 s = 60°) stays valid as a hypothetical. |
| L12-05 | **"It takes about a fifth of a second"** for gyro calibration. The official setup waits for fresh data before each of 1024 samples; the rate depends on configuration and IMU generation. | **AGREE — C4.** *(Already a bench item: Q046 gyro-bias.)* |
| L12-06 | **"Every slice you miss is gone forever."** The algorithm uses `dt = currentTime - lastTime`, so it accounts for elapsed time. The real issue is that one sampled rate can't reconstruct a rate that changed during the interval. | **AGREE, and GPT spots a bonus:** the corrected explanation (area under the rate curve) is a lovely preview of L15's I term. |
| L12-07 | **"Thousands of times per turn" / "gyro checks the real angle thousands of times per second."** | **AGREE — C4.** |
| L12-08 | **IMU "costs zero pins."** It occupies SDA/2 and SCL/3. The useful concept is that I²C is a *bus* — shareable. Also "nothing else on the Zumo is using them" is unnecessary. | **AGREE.** |
| L12-09 | **"You do not care, and you never will"** about the two IMU generations. | **AGREE — C5.** *An abstraction lets you ignore details until your problem requires them* is the better lesson. |
| L12-10 | **"Integer math keeps every call cheap and exact."** The angle estimate isn't exact — sensor noise, bias, quantisation, integration error. Also "do float math thousands of times and you are not turning any more, you are calculating" is exaggerated. | **AGREE — C5.** The 2²⁹ = 45° fixed-point scheme itself is confirmed correct and authentic. |
| L12-11 | **`imu.init()` returns a bool that the code ignores.** | **AGREE.** *Initialization can fail; hardware functions return status for a reason.* Also prevents "HOLD STILL forever" from being blamed only on `Wire.begin()`. |
| L12-12 | **§7A has a real angle-reset bug.** The test calls `gyroUpdate()` without `gyroReset()`, and `gyroSetup()` doesn't end with a reset — so `gyroLastUpdate` is still 0 and the first `dt` is a modulo-65536 interval. Pololu's own setup resets after calibration. | **AGREE — real technical fix.** End `gyroSetup()` with `gyroReset()`. |
| L12-13 | **§7A's "spin it all the way around and it reaches 360" is wrong.** `getTurnAngle()` wraps through ±180°. §8A.3 itself teaches the wrap. | **AGREE, and GPT turns it into a better experiment:** *turn past 180°, watch the number go negative, complete the circle and it returns to zero — we explain why in §8A.3.* Students see the behaviour before the explanation. |
| L12-14 | **Challenge 1 needs wrapped angular error.** `error = targetHeading - getTurnAngle()` breaks across the ±180 boundary (+179 → −179 gives −358 instead of +2). | **AGREE.** Either constrain the headings or teach the wrap — GPT votes teach it, since §8A.3 already explains the representation. |
| L12-15 | **Challenge 1 doesn't prevent accumulated gyro drift** as claimed — absolute headings stop stopping-errors from stacking, but the integrated heading itself still drifts. | **AGREE.** §8A.1 already understands this. |
| L12-16 | **Challenge 2: "the gap between their answers *is* the slip" / "together they cannot miss it."** The disagreement also contains encoder model error, gyro bias, noise, overshoot, scrub, asymmetry. | **AGREE — C5.** Still a great sensor-fusion intro; *large disagreement is evidence of model failure* is the defensible version. |
| L12-17 | **§7E promises the gyro square closes on Delrin** — but the straight sides still use encoders on the same slippery surface. | **AGREE, and GPT is right that this is a better result, not a problem:** *replacing one bad assumption doesn't remove the others.* Same for the opening hook's "almost exactly where it started" and the fixed numbers (encoder 90 / gyro 31, each corner 60°). |
| L12-18 | **Bonus B4's premise is unsound.** It claims adding TRIM makes the gyro turn wrong, but the gyro still supplies the stopping criterion — TRIM would change pivot/rate/overshoot, not necessarily the final angle. | **AGREE — C1.** GPT offers better sabotage candidates (negative target without `abs()`, reversed motor sign so the robot drives instead of spins while the angle barely changes). |

**Also — byte-count consistency:** Step 5 says 20,702 → 21,502; Step 8 says 21,502 → 24,694; §7B
says 20,626 → 20,422. The 7B baseline drops ~4 KB because its stripped `loop()` makes the state
machine unreachable. **That's legitimate and is itself a good linker lesson — but the lesson must
say so**, or it teaches byte-size diagnostics and then appears to contradict its own numbers.
**AGREE.** Also `F()` "every string literal gets copied into SRAM at power-on" is oversimplified.

**Marked KEEP by GPT (protect):** the title · *"Every number it produced was true"* · Challenge 3
The Stuck Guard, which GPT calls one of its favourite challenges in the book — and which cashes in
L11 correctly (*L11 didn't ban timers; it taught you to match the instrument to the question, and
here the question really is "how long have I been trying?"*) · §8A, which is earning its space.

---

## LESSON 13 — 21 findings

| ID | Finding | Verdict |
|---|---|---|
| L13-01 | **Step 5 treats `STOP_DISTANCE` as a successful wall stop.** `driveUntil()` returns `STOP_PROX`/`STOP_DISTANCE`/`STOP_KILL`; Step 5 checks only `STOP_KILL`, then records the row and turns. If the prox misses the wall, a missed detection is recorded as a wall. | **AGREE — definite logic bug.** GPT's fix (declare wall-detection failure and stop) makes the return enum actually mean something. |
| L13-02 | **`MAX_ROW_CM = 300` is not a safety cap.** It stops the motors after 300 cm of *commanded wheel travel*. If the zone is smaller than 300 cm, the robot hits the wall long before. | **AGREE.** Needs a real physical bound. |
| L13-03 | **The sweep has no completion condition.** Rows run wall-to-wall forever; eventually the robot sidesteps into the side wall. The Engineer's Log even asks "how does the robot know it is finished" — and the finished code doesn't know. | **AGREE — GPT's #1 algorithmic hole in L13, and it has a downstream consequence:** L14 §8's 10× table lists "Rescue zone exit — 10 trials" for a behaviour that doesn't exist yet. GPT suggests this become the capstone challenge (*Know When You Are Done*), replacing the report challenge. |
| L13-04 | **"The wall resets error to zero."** The prox stops the robot at some threshold depending on reflectivity, angle, response, heading. It bounds accumulated error; it doesn't give an exact pose. | **AGREE — C2.** GPT's version sets up SLAM more honestly. |
| L13-05 | **The wall-vs-victim classifier is presented as definitive.** `lastLegCm < lastRowCm - VICTIM_SHORT_CM` assumes neighbouring row lengths are near-identical; changing stop distance, angle error, non-parallel walls, slip, and missed prox stops all move it. | **AGREE.** *The odometer supplies evidence.* And GPT's framing is a great programming concept: **every inference has assumptions — name them.** |
| L13-06 | **Sabotage B4's explanation is wrong.** Switching `read()` → `readCalibrated()` with a raw-scale threshold in the hundreds means `0 >= several hundred` is false for every sensor, so `silverDetected()` likely returns **true** — RESCUE ZONE on ordinary white floor — not "the door never triggers." | **AGREE, and the real lesson is better:** same type, wrong unit/scale. Raw = microseconds; calibrated = 0–1000 normalised. The code compiles because C++ sees integers either way. |
| L13-07 | **B4 also conflates two mechanisms** — silver (raw value outside the calibrated minimum → clamped) and black ball (weak reflected IR at the prox receiver) are different failures on different sensor architectures. | **AGREE.** |
| L13-08 | **"A black ball absorbs infrared" / "the signal is not there to threshold" / "barely whisper at point-blank range."** Visible black doesn't guarantee negligible IR reflectance. | **AGREE — C2.** 7A already measures the actual victim; let it establish the premise. |
| L13-09 | **"Nearly invisible to every sensor this robot carries."** The line sensors face down; encoders and gyro aren't target sensors. | **AGREE — C5.** |
| L13-10 | **"Silver is invisible to calibrated eyes" taught as universal.** Whether the actual silver tape reads below the calibrated white minimum is empirical. | **AGREE — C2.** Keep *"The subtraction knew; the clamp forgot"* — GPT singles it out. |
| L13-11 | **The quoted `readCalibrated()` source must be byte-matched to the bundled QTR in `Zumo32U4@2.0.1`**, not a current standalone QTR. | **VERIFY — cheap and important.** The lesson calls it "the actual code that runs." |
| L13-12 | **Official rules vs. course adaptation not distinguished.** Official Rescue Line requires locating **and transporting** victims; L13 makes finding the victim the rescue. | **AGREE — C6.** One explicit sentence prevents a student leaving with the wrong competition rule — and L14 is *Competition Prep*. |
| L13-13 | **The servo claim is wrong.** "Carrying a victim needs a gripper, a servo, and a driver channel to spare; your two DRV8838 drivers are both spoken for." A hobby servo doesn't consume a DRV8838 H-bridge channel — it needs power, ground, and a control signal. | **AGREE.** Also inherited by L14. |
| L13-14 | **SLAM overclaim: "you have already flown it."** The robot builds no map and estimates no full pose. | **AGREE — C5.** GPT's version is accurate and still exciting: *you have met one of the ideas SLAM relies on.* |
| L13-15 | **"Lawnmower sweep guarantees coverage."** Heading error, missed wall detections, and target sensitivity can break it. | **AGREE — C5.** |
| L13-16 | **`ROW_STEP_CM` is justified by geometry ("the prox sees ahead, so rows can be coarser than the robot is wide")** rather than by measured detection envelope. | **AGREE.** GPT: place the silver ball at the worst-case midpoint between adjacent rows and test. Also strengthens sabotage B3. |
| L13-17 | **`SILVER_RAW_MAX` semantics are off.** `if (raw[i] >= SILVER_RAW_MAX) return false;` means the name should be a threshold, not a max. | **AGREE — minor, but L13 is where naming should tighten.** *(The blank behaviour `SILVER_RAW_MAX = 0` correctly makes detection impossible — nice.)* |
| L13-18 | **"All five below threshold" may be too brittle** for an angled approach or a narrow strip. | **DJ'S CALL / BENCH.** GPT's version is a real classifier lesson: *AND improves specificity but hurts sensitivity* — start at 5-of-5, test approach angle in 7B, compare with 4-of-5. |
| L13-19 | **Challenge 3's "two agreeing measurements" doesn't compare the measurements.** The code consumes a retry and treats row zero as wall by default; it never tests whether the two distances agree. | **AGREE.** Store the first distance and compare, or change the prose. |
| L13-20 | **Challenge 1 calls `driveDistance(-10.0)`** — sound only after the L06 reverse-TRIM fix propagates. | **AGREE.** Dependency on L06-01. |
| L13-21 | **7A uses one reading per target.** Thresholds from single readings teach false precision. | **AGREE.** Min/max or 5 samples; choose thresholds *between distributions*. Same correction as L09-02. |

**Also:** §8A.3's "black ball on light floor is trivially visible to a camera" — **C5**, vision has
its own lighting/shadow/exposure/segmentation problems. The search-dogs/avalanche-beacon analogy
is shaky and unnecessary. Step 5's turns and sidestep still use the older blocking primitives, so
B is responsive during `driveUntil()` but not throughout the sweep — **C3**.

**Marked KEEP by GPT (protect):** `driveUntil()` as a *watchful* blocking primitive — GPT calls it
one of the strongest programming developments in the book, and proposes making the progression
explicit: *"Lesson 6 taught a loop that waits. Lesson 13 teaches a loop that waits while still
paying attention."* · *"the reason behind a rule tells you where the rule ends"* · the
flying-on-instruments story · 7A as characterisation work.
**GPT calls L13's Saxon spiral the strongest in the book.**

---

## LESSON 14 — 20 findings
*`Lesson_14_GPT_Feedback.docx` is 8,615 words, but **5,010 of them are a verbatim duplicate of the
entire L13 review**; the actual L14 content is 3,605 words. GPT verified L14 against the **final**
2026 rules, updated 29 Mar 2026 — it explicitly says "not the draft."*

| ID | Finding | Verdict |
|---|---|---|
| L14-01 | **The automatic calibration spin appears illegal at competition.** L14's startup ritual and §9's timeline both budget an autonomous line-calibration spin on the venue floor. The 2026 rules permit field calibration but state robots may not move on their own while calibrating. | **VERIFY against `RCJRescueLine2026-final.pdf`, then AGREE — GPT's must-fix #1.** If it holds, GPT's two-mode fix is a genuinely good lesson: *the algorithm stays the same while the operating procedure changes to satisfy a requirement.* **Also inherited by L16 Step 5.** |
| L14-02 | **§9.4 "Know the Field" instructs students to do what the rules prohibit** — survey intersection, gap, obstacle, and rescue-zone locations. The rules prohibit pre-mapping and can disqualify the round. | **VERIFY then AGREE.** GPT's inversion is excellent: **KNOW THE CONDITIONS, NOT THE MAP.** *Legal: "this floor is glossier than ours." Illegal: "there are three gaps before the obstacle."* Turns a rules problem into a rules-literacy exercise. |
| L14-03 | **LoP is presented as a skip button.** "Strategic teams sometimes call LoP intentionally to skip a difficult section." A LoP returns the robot to the previous checkpoint; only after three failed attempts may it proceed to the next. It also decays tile points 5→3→1→0 and costs 5 from the exit bonus. | **VERIFY then AGREE.** *LoP stops wasting time on a failed attempt. It does not automatically let you skip the section.* |
| L14-04 | **Challenge 3 makes C the LoP button.** The rules require a single visible physical button for start and LoP restart, with the procedure declared before each scoring run. | **VERIFY then AGREE.** GPT's better version: instrument the *declared* start/restart button so the count increments when the referee authorises a restart — marrying rules compliance and software architecture. |
| L14-05 | **The 10× Rule claims too much.** 0.9¹⁰ ≈ 0.35 is correct arithmetic, but ten consecutive successes do not demonstrate 99% reliability, and real robot failures are correlated (low battery hurts turns, avoidance, and gap crossing simultaneously). | **AGREE, and GPT's redefinition keeps the discipline:** *10/10 is a gate to full-course testing, not proof of 99% reliability.* |
| L14-06 | **Self-test limits presented as engineering truths, not measurements.** `SELFTEST_GYRO_MAX_DEG = 3`, `SELFTEST_LINE_MAX = 1800`. | **AGREE — C4.** GPT's provenance-comment pattern is good: `// Fleet test, Aug 2026: healthy 0.1–0.8°, disturbed 12–47°, therefore fail > 3°`. *Now the comment contains evidence, not an argument.* |
| L14-07 | **Battery continuity error: L14 says "four eneloop NiMH cells"** but the course uses **Panasonic**. Also 5400/4800/4200 presented as "the chemistry." | **AGREE.** The eneloop/Panasonic drift is a definite error — the Resource Section already pins Panasonic. 4.8 V nominal is the sourced fact; the thresholds are course policy. **C4.** |
| L14-08 | **`COMPETITION_MODE` "changes nothing else" / byte counts "prove" it changes theatre not behaviour.** Removing three 600 ms pauses changes timing, and timing is behaviour. A byte count can't prove behavioural equivalence. | **AGREE.** GPT's replacement is a hypothesis to test — which §7C almost already is. |
| L14-09 | **"About two seconds faster."** 3 × 600 ms = 1.8 s *if* all three events occur exactly once. | **AGREE — C4.** |
| L14-10 | **"You've built a fully functional rescue robot."** Official rescue requires victim transport. | **AGREE — C6.** *"You've built the complete stock-Zumo platform this course set out to build."* |
| L14-11 | **§8's 10× table lists "Rescue zone exit"** — a behaviour L13's finished build doesn't implement. | **AGREE.** Continuity dependency on L13-03. |
| L14-12 | **Servo/DRV8838 claim inherited from L13.** | **AGREE.** See L13-13. |
| L14-13 | **"A team that skips evacuation cannot win" is false.** International final score weights field 60% / rubrics 20% / Technical Challenge 20%. | **VERIFY then AGREE — C5.** *"Victim multipliers can dominate field scoring; skipping them gives up a major opportunity"* is strong enough and correct. |
| L14-14 | **Handle wording too casual:** "the Zumo's built-in grip area usually works." The referee decides. | **VERIFY then AGREE.** Don't promise compliance. |
| L14-15 | **"The 15-Minute Rule"** sounds like an established rule; the 2026 rules don't prescribe it. | **AGREE — C6.** Rename to a RoboLore habit. Also "bright lights increase all readings" — direction depends on sensor and displayed quantity. |
| L14-16 | **"Mechanical problems are the #1 cause of competition failures."** Unsupported. | **AGREE — C4.** GPT's replacement is more RoboLore anyway: *mechanical problems are common, and software cannot tighten a screw.* |
| L14-17 | **Code freeze presented without a label.** | **AGREE — C6.** Label as RoboLore team policy, then state the actual rule separately (no calibration or code changes once the scoring run begins). *"Rules say X. Our discipline says stop much earlier."* |
| L14-18 | **Challenge 1's 100-count encoder threshold needs justification.** | **AGREE — C4.** Minor. |
| L14-19 | **Challenge 2 should zero the motors before the permanent park**, so the failure branch is locally safe if `selfTest()` is ever called elsewhere. | **AGREE.** Exactly the defensive programming L14 should encourage. GPT rates Challenge 2 highly otherwise. |
| L14-20 | **MISSING CONTENT — GPT's best find in L14.** The official rules require teams to submit source code and allow students to be asked to explain the robot's construction and programming to verify it is their own work. | **VERIFY then ADD.** After fourteen lessons of *don't copy code you can't explain*, the competition itself says **explain your code.** GPT's line: *"The ultimate Brain Check has no reveal button. A referee can ask you why your robot works."* This is the payoff for the entire course thesis. |

**Also:** GPT recommends replacing some "champion mindset" material with a short aviation-checklist
story — *the checklist doesn't replace expertise; it protects expertise from memory, distraction,
and pressure.* **DJ'S CALL.**

---

## LESSON 15 — 28 findings
*GPT: "I would not bench-test the current finished build until these are corrected."*

| ID | Finding | Verdict |
|---|---|---|
| L15-01 | **THE SPEED ESTIMATOR IS THE BIGGEST CODE PROBLEM IN THE LESSON — three separate defects.** (a) At a ~2–3 ms update period the encoder sample contains only 2–4 counts, so the PI loop chases quantisation. (b) `averageCounts()` uses cumulative **absolute** values; velocity needs **signed deltas**. (c) Signed-16-bit rollover will eventually create a giant discontinuity. | **AGREE — GPT's #1 code fix in L15.** The fix is also the best teaching: a slower speed window (tens of ms) using `getCountsAndResetLeft()/Right()`, which teaches *different control loops do not have to run at the same rate.* |
| L15-02 | **"How fast are we ACTUALLY going? Ask the encoders."** L12 just taught them not to do this. | **AGREE — C2.** *The speed loop holds wheel-derived speed. If the tracks slip, the controller cannot know ground speed from the encoders alone.* Beautiful continuity point. |
| L15-03 | **The doorway derivative reset doesn't work.** `lastError = 0` then re-entering with `error = 600` gives a first derivative of ~(600−0)/0.002 — enormous. The prose says the doorway makes the re-entry flinch impossible; the code doesn't guarantee it. | **AGREE — must-fix.** GPT's `derivativeReady` flag makes the first valid sample *seed* history rather than invent it. |
| L15-04 | **The gap-windup demonstration is architecturally impossible.** `followLine()` is called only inside `if (isLineVisible())`, so `lineIntegral` cannot accumulate during a gap — and 7D explicitly resets it through the doorway anyway. | **AGREE — ALREADY IN THE S154 QUEUE, now independently confirmed.** *Prose and code disagree and the code is right.* GPT suggests the long curve as the legitimate windup demonstration. |
| L15-05 | **"D knows where you are going" / derivative is a statement about the future.** D measures the current rate of change of error. | **AGREE — C5.** Keep the present/past/trend framing; change "D knows where you are going" to **"D knows how fast your error is changing."** |
| L15-06 | **"P alone can never stop weaving, no matter what Kp you choose"** — including Brain Check 03. A P-only loop can be stable; L08's own tuning assumes a workable Kp region exists. | **AGREE — C5.** *P alone forces a tradeoff; D gives another knob.* Note this one touches a quiz bank. |
| L15-07 | **"The LINE loop gets P and D. Not I" / "the verdict is not a preference."** Integral action isn't inherently wrong for line following; it's a design choice about this track and this integrator management. | **AGREE — C5, and the lesson contradicts its own philosophy.** It says *"the difference lives in the world, not in the code"* — so the robot should decide the verdict experimentally rather than the textbook announcing PID line following is fundamentally wrong. |
| L15-08 | **"I is the only term that can remove steady-state error."** True within the P/I/D feedback terms — but the robot already has feed-forward TRIM, which can compensate a known bias. | **AGREE — C1/C5, and this finally reconciles TRIM** instead of creating another absolute. |
| L15-09 | **"Your loop takes roughly 2–3 milliseconds"** derived from Pololu's 2000 µs sensor *timeout* — which is a ceiling, not a per-read duration. And it contradicts the same section's "millis() might report 0." | **AGREE — C4.** Let §7A measure it. |
| L15-10 | **7A doesn't actually compare two clocks.** It prints `us / 1000` labelled "<- millis", which is integer division of a micros-derived duration, not what `millis()` would have reported. | **AGREE.** Instrument both from independent stored timestamps — a much better experiment. |
| L15-11 | **"Never store an elapsed total and compare it to a target — that is where rollover bugs live."** This accidentally unteaches `if (millis() - start >= interval)`, the correct rollover-safe pattern students already use. | **AGREE.** The real rule is narrower: compute intervals with unsigned timestamp subtraction. |
| L15-12 | **Asking what `(error-lastError)/0` "evaluates to"** as though there's one universal answer. Integer and floating-point division by zero are different problems. | **AGREE.** The engineering rule is simpler: *zero is an invalid dt; the controller must prevent it.* |
| L15-13 | **The battery demo ignores actuator saturation.** 7E promises the PI pushes until the wheels reach the requested speed — only if the speed is still physically reachable. | **AGREE, and it's an important control concept:** *a controller cannot command voltage the battery cannot provide.* If `speedTrim` hits max and speed stays low, you've found the machine's limit, not a better Ki. |
| L15-14 | **Challenge 4's conditional integration rule is incomplete.** "Stop integrating whenever output is saturated" — but if saturated high with a *negative* error, integrating helps escape saturation. | **AGREE.** The sharper rule (freeze only when the error would push *farther* into saturation) makes Challenge 4 genuinely excellent. |
| L15-15 | **Ziegler–Nichols is misapplied in two ways.** (a) The table is the classical **PID** rule; discarding I and keeping Kp/Kd isn't classical PID tuning. (b) `Tu = 2 / WEAVE` only means an oscillation period if the sign flips come from sustained regular controller oscillation — not from noise, curves, geometry, or startup. | **AGREE.** *"We're borrowing the Kp and Kd portions of the classical PID rule as a rough PD starting point"* is honest. Ku/Tu needs a controlled test condition. |
| L15-16 | **WEAVE has no deadband.** Near centre, +3, −2, +4, −1 registers three sign flips on an essentially centred robot. | **AGREE.** Also reinforces L04/L05 threshold thinking. |
| L15-17 | **`showScore()` prints a suggested Kd but not the equally required "set Kp to 0.6 × Ku."** A student can stay at Kp = Ku and just add the Kd. | **AGREE.** The starting pair must be treated as a pair. |
| L15-18 | **The hill climb can stop far from a good setting.** Fixed ±50% steps mean an optimum 15% away reads as "done." | **AGREE.** Coarse-to-fine (50 → 20 → 10%) plus repeated runs per candidate. **And GPT spots the spiral:** *L14: one successful run is not reliability. L15: one good score is not a tune.* |
| L15-19 | **"A 12-second and a 7-second MAE cannot be compared."** MAE is a mean — already normalised by sample count. | **AGREE — C5.** Standardising duration is good experimental practice for a different reason (different portions of the track). |
| L15-20 | **MAE is sample-weighted, not time-weighted** — so a condition with a faster loop contributes more samples and more weight. | **AGREE, and this may be the best single suggestion in the review:** `runAbsErrorTime += abs(error) * dtSec` divided by total scored time. **"The tuning bench itself needs an I term — not for control, but for measurement."** Students just learned what an integral is. |
| L15-21 | **An aborted run displays a score indistinguishable from a complete one.** A 3-second abort can sit beside a 10-second trial. | **AGREE.** Mark COMPLETE vs ABORTED; the data is still diagnostically useful. |
| L15-22 | **The tuning run isn't isolated from the full course.** `runStart` keeps running through intersection/obstacle/gap states, so two nominally 10-second runs can contain different amounts of line-following time. | **AGREE.** Requires a dedicated tuning track; the full course becomes validation. |
| L15-23 | **Challenge 3's conclusion overstates.** "Every millisecond is a millisecond in which the controller is not controlling" — the model accounts for actual dt. | **AGREE.** *Long passes reduce how frequently the controller can update.* |
| L15-24 | **Challenge 6 prescribes linear gain scaling with speed.** Controller scaling can be nonlinear and system-dependent. | **AGREE.** Make linear scaling one hypothesis to test. |
| L15-25 | **Challenge 7 is conceptually broken.** It correctly says whole-course MAE mixes jobs, then proposes MAE per state — but line-position error has no meaning during `GAP_CROSSING` or `SWEEPING_ZONE`. | **AGREE, and GPT's redesign is a capstone:** *Score Every Behaviour With the Right Instrument* — reacquisition success for gaps, row-length consistency and coverage for the sweep, final angle error for turns, speed MAE for the speed loop. |
| L15-26 | **The pickup stress test doesn't test what the lesson claims.** The finished line loop is PD (no line integral), and lifting the robot ends line visibility, so `followLine()` and the speed loop stop being called. | **AGREE.** GPT's drag test (repeatable mild load that slows the tracks without ending line detection) actually exercises the finished speed PI. |
| L15-27 | **`runSample(lastError)` works only because `followLine()` just overwrote `lastError`.** But `lastError` exists as *derivative history*; the scorer is using it as *current error*. Change the derivative implementation and you silently break the measurement system. | **AGREE — and it's exactly the architecture bug L07 was meant to prevent.** |
| L15-28 | **Anti-windup presented as the solution rather than one method.** | **AGREE — C5.** *One common anti-windup method.* |

---

## LESSON 16 — 30 findings

| ID | Finding | Verdict |
|---|---|---|
| L16-01 | **`saveBaseline()` computes the lap at CALL time, not at run end.** Press B at goal → `endRun()` → report → student reads it → *later* holds A+B to save. `millis()` keeps advancing, so a 32.4 s lap can persist as 40.4 s. | **AGREE — ALREADY IN THE S154 QUEUE, now independently confirmed.** GPT's framing is a terrific capstone lesson: **measurement ends when the experiment ends, not when the human gets around to writing it down.** |
| L16-02 | **B-at-goal adds human reaction time to LAP.** | **AGREE.** Either say so honestly (same operator and procedure for A and B runs) or detect the finish automatically. |
| L16-03 | **The opening `F()` advice solves the wrong memory problem.** The lesson opens a **flash** crisis (28,214 / 28,672) then says check your `F()` wrappers — "the cheapest 40 bytes you will ever find." `F()` protects **SRAM**. It buys no flash. | **AGREE — one of the clearest errors in the review.** And the fix makes GRAPHIC 16.1 more meaningful: three memories, three constraints. Flash → remove code. SRAM → `F()`. EEPROM → persistent data. |
| L16-04 | **`baseline.mae == 0` used as "no baseline."** Zero is a valid MAE. | **AGREE.** *A data value should not secretly double as program state unless that value is impossible as legitimate data.* Persist an explicit validity flag. |
| L16-05 | **The magic byte is taught as proof of validity.** `magic == 0x16` tells you the block starts with the expected marker — not that floats are sane, the struct layout matches, or the baseline is valid. If a field is added and the magic stays `0x16`, the loader accepts old data under the new layout. | **AGREE.** Teach it as a **format/version marker**: change it whenever the layout changes. Add range validation after load; mention CRC as the professional next step. Keep *"bytes do not blush."* |
| L16-06 | **EEPROM timing overstated.** `EEPROM.put()` uses update semantics and skips bytes already holding the same value; ~3.3 ms applies to bytes that actually change. | **AGREE.** The conclusion (*don't save from the control loop*) stands. |
| L16-07 | **"PNG, ZIP and PDF all open with exactly this trick."** Directionally useful; "exactly" is too casual. | **AGREE — C5.** |
| L16-08 | **Raw struct persistence needs one portability sentence.** Padding, representation, and member order are platform-specific. | **AGREE.** *This byte-for-byte format belongs to this firmware and this AVR platform.* |
| L16-09 | **The EEPROM address map is a course fact presented as a chip fact.** 0–511 Lesson 16, 512–543 robot name, 544–1023 free. Also the name/0x5A facts should be verified against the actual name writer. | **AGREE — C4/C6.** Label it the **RoboLore fleet EEPROM map**. *(`ZUMO_NAME_WRITER_main.cpp` is in the repo root — verifiable.)* |
| L16-10 | **Saint-Exupéry attributed as "aircraft engineer."** He was an aviator and writer. | **AGREE.** The quote itself is well chosen and lands perfectly. |
| L16-11 | **The course TDP outline is called "the real template."** The 2026 rules require strict compliance with the supplied official template; failure can zero the document. The course outline includes a class-specific *Version 2* section. | **VERIFY then AGREE — C6.** This is a dangerous conflict between course pedagogy and competition compliance. Two labels: *RoboCup submission: use the official template exactly. RoboLore class TDP: same goals plus our Version 2 reflection.* |
| L16-12 | **The poster is missing from the capstone deliverables.** 2026 requires TDP + poster + video; the lesson lists TDP, video, live demo, journal. | **VERIFY then AGREE — C6.** The poster can be distilled from the TDP, which is what the rules say it's for. |
| L16-13 | **"TDP is weighted more than video and poster combined"** is true *within* the rubrics score (60/20/20) — but the rubrics category is itself 20% of the international total (field 60%, rubrics 20%, Technical Challenge 20%). | **VERIFY then AGREE.** Explain the full hierarchy. |
| L16-14 | **"A well-documented robot with decent performance routinely outscores a brilliant robot with a bad paper."** Empirical claim with no evidence. Same for "judges score failures higher than untested success claims." | **AGREE — C4/C5.** The actual scoring formula is more persuasive than the rhetoric. |
| L16-15 | **`RunScore {lap, mae}` treats whole-course MAE as complete robot quality** — but the course contains gaps, intersections, obstacles, and the rescue zone, where line MAE isn't sampled or isn't meaningful. **This contradicts L15's own strongest insight.** | **AGREE.** Primary metric = completion/lap. Guardrail = FOLLOWING_LINE MAE/PEAK. Plus an enhancement-specific metric. Realises the L15-25 correction. |
| L16-16 | **§7.1 says "bless the middle run / or accept the last."** If three measurements exist, use them: **median of three A vs. median of three B.** | **AGREE.** A beautiful final retrieval of repeatability thinking without formal statistics. |
| L16-17 | **The 10% spread rule is unlabelled and undefined.** Is it (max−min)/median? | **AGREE — C4/C6.** Label as a RoboLore benchmark rule and define the calculation, or students won't all compute the same thing. |
| L16-18 | **"The ONLY difference between the two runs is YOUR CODE."** Aspirational — rebuilding changes timing and memory layout, and the robot and environment can drift. | **AGREE — C5.** *The software variable we intentionally change is `ENHANCEMENT_ON`; everything else is held as constant as practical.* |
| L16-19 | **`runEnhancement()` is called only inside the line-visible branch**, but the enhancement menu includes rescue-zone sweep, long-gap heading, self-test, ramp detection, and tether warning — several of which can't live there. | **AGREE.** Either call it the *line-following enhancement socket*, or tell students that other enhancements require choosing and defending a different integration point. GPT leans toward the latter — by L16 they should be allowed to alter architecture. |
| L16-20 | **The compass menu item is described as "absolute heading."** A magnetometer inside a robot full of motors, current, and steel needs calibration and characterisation first. | **AGREE — C2.** The lesson already warns *motors are magnets* — strengthen it. This should be an ambitious research choice, not the item that sounds easiest. |
| L16-21 | **"Serial costs two and a half seconds."** The code is `while (!Serial && elapsed < 2000)` plus `delay(500)` — so **up to** ~2.5 s, in the untethered case. | **AGREE — C4.** |
| L16-22 | **Step 5 inherits L14's competition calibration spin.** | **AGREE — C6.** Don't let the capstone resurrect an already-fixed rules problem. Dependency on L14-01. |
| L16-23 | **The TDP template tells students "this is a preconfigured Pololu Zumo 32U4."** GPT flags this for hardware verification. | **RESOLVED BY DJ'S S154 RULING — and the sentence is CORRECT.** The fleet *is* Zumo 32U4 with OLED. **This is the same finding as L01-02 seen from the other end, and it independently confirms the direction of that fix.** GPT hedged only because L01 taught A-Star as the controller. |
| L16-24 | **Gold tier requires podium placement.** Competition outcome depends on other teams, bracket, course, and luck. | **AGREE, and GPT's split is right:** engineering tiers (Bronze/Silver/Gold) from project evidence; competition awards separate. Keeps the rubric rewarding engineering decisions rather than opponent-dependent outcomes. |
| L16-25 | **Glossary A/B entry: "the only experimental design that proves YOUR code caused the change."** | **AGREE — C5.** *A controlled before/after comparison designed to isolate the effect of one intentional change.* |
| L16-26 | **"Flash budgeting ... the first skill a professional embedded engineer is hired for"** and "#1 project killer." | **AGREE — C4/C5.** Keep the first half of the flash-budget definition, which is good. |
| L16-27 | **28,672 is correct for this target.** PlatformIO documents 28 KB flash / 2.5 KB RAM for the A-Star 32U4; Pololu documents the 4 KB bootloader. | **NO ACTION — confirmed correct.** Only word it as *"on our A-Star 32U4 build target"* rather than a universal ATmega32U4 ceiling. |
| L16-28 | **All finer byte figures need build provenance:** 28,214 · 28,464 · 28,824 · 29,460 · −704 · +636 · −156 · buzzer −1,828. | **AGREE — C4.** |
| L16-29 | **The subsystem audit table (IMU ~2900, OLED ~2600, QTR ~2300, USB Serial ~1900, buzzer ~1800, heap ~960) needs a stated method.** `avr-nm` doesn't hand you a semantic subsystem invoice; the grouping requires judgment. | **AGREE — C4.** GPT's suggested provenance line: *measured with `avr-nm --size-sort` on the L15 finished build, grouped manually by originating library.* |
| L16-30 | **The buzzer cliff figures (eleven calls = 130 bytes, last call = 1,698, total 1,828) must stay tied to the exact build.** | **AGREE — C4.** The *concept* is excellent embedded teaching: **in this build, the dependency has a cliff. Your build is the invoice.** Don't let it become "buzzers cost 1,828 bytes." |

**Marked KEEP by GPT (protect):** *"Anyone can add. Engineers decide what to take away — and can
show you the number that made the decision."* · the A/B protocol structure · `usbPowerPresent()` as
a Bronze enhancement (confirmed supported by Pololu) · the EEPROM addition as a capstone concept ·
the entire closing section, including *"An abstract written first is a wish; written last it is a
summary,"* *"The robot was just the excuse,"* and *"Sixteen lessons ago you could not make an LED
blink. Read your Lesson 1 log entry. Who wrote that?"*

---

# PART 3 — ALREADY RULED (STRIKE, DO NOT REOPEN)

GPT cannot see a ruling (rule 39) and re-reported five settled items. Per the S152/S154 triage
rules these are struck as *new* items — the underlying instances in Part 2 still need disposition.

| # | GPT item | Existing canon |
|---|---|---|
| S-1 | "Do a final course-wide claim-strength pass" (always/never/exactly/impossible/guaranteed) | §16.16 · rule 61 — the absolutes pass |
| S-2 | "Keep competition claims tied to a year" | rule 63 — a citation is a claim about an edition |
| S-3 | "Make the MEASURED FACTS discipline part of the book" | §24.15 |
| S-4 | "Do a cross-lesson canon document before editing" | That is `ZUMO_SUPER_BIBLE.md` |
| S-5 | The spiral audit / Saxon scaffold audit | Already ruled and enumerated (13 of 171 units, deliberately not started) |

**Note on S-5:** GPT arrived at the Saxon spiral independently in L04, then **revised several of its
own earlier cut recommendations** once DJ explained the design. See Part 4.

---

# PART 4 — WHERE I DISAGREE, OR WHERE GPT DISAGREES WITH ITSELF

**D-1 — The L02 challenge cut table is SUPERSEDED. Do not act on it.**
`Lesson_02_GPT_Feedback.docx` ends with a ~30-item cut table for L01 and L02 challenges. That table
was written **before** GPT knew about the Saxon spiral design. In `Lesson_04_GPT_Feedback.docx` GPT
learns the design from DJ and explicitly revises: L01 C11 moves from *cut* to *optional*; L02
Warm-Up 4 becomes *definitely keep* ("exactly the kind of spiral retrieval you want"); L03 C1 Spin
Test moves from *cut* to *keep as a 2-minute Spiral Check*; L04 Challenge 1 Line Light moves from
*eliminate* to *keep as short retrieval*. **The revised verdicts supersede the table.** Anyone
working from the L02 document alone will cut challenges GPT later argued to keep.

**D-2 — GPT's own three-category rule is better than either list.**
*Exact repetition (same concept, same context, same help) → cut. Spiral retrieval (old concept,
less help) → keep but shorten. Spiral deepening (old concept + something new) → definitely keep.*
Plus: **the scaffolding should decrease every time a concept returns.** If DJ rules on this rule,
most of the individual cut/keep debates resolve themselves.

**D-3 — I'd hold L08-02 (`followLine()` → RobotMotion) until priced.**
GPT is architecturally right that L08 contradicts L07. But moving `followLine()` ripples through
L08–L16 payloads, every byte figure downstream, and the Maker. Rule 70: price every candidate by
deletion before ruling. This may be the single most expensive item in the review.

**D-4 — L06-07 (`WHEEL_BASE_MM` → `TRACK_WIDTH_MM`) is right and possibly not worth it.**
The terminology objection is correct. But the constant appears in lessons, the Maker, the TDP
template's A4 table (which asks students to verify the book's 85 mm), and possibly quiz banks.
Price it first.

**D-5 — GPT's rulebook claims are unverified and must not reach a lesson unchecked.**
L14-01 through L14-04, L14-13, L14-14, L16-11, L16-12, L16-13 are all rulebook claims. GPT says it
checked the final 2026 rules updated 29 March 2026 — which is plausible and, if true, genuinely
useful. **We have `RCJRescueLine2026-final.pdf` in the repo root.** Rule 43: when the citations
disagree, read the rulebook. These are checkable in one pass.

**D-6 — RESOLVED BY MEASUREMENT, AND IT EXPOSED AN UNGATED INVARIANT.**
GPT was right about L01-14 and our gates were not wrong — they were watching a different property. **Gate 69 / §10 pins `PLANNED_EXPECTED = 146`, the figure *denominator*.** It exists because of S135, where landing art deleted a tag's only occurrence and shrank the population so `outstanding` fell like progress. That gate does its job correctly. **It never asks whether every figure a lesson uses has a row in that lesson's own index table** — and nothing else does either. Rule 44: the header of a thing is not the thing; *the planned figure population is whole* reads broader than the predicate underneath it.
**This is a new ungated invariant, not a broken gate.** Measured book-wide: 5 used-but-unindexed tags exist — 4 in L01 (real defect) and `GRAPHIC 15.4` in L15 (legitimately outstanding). A gate would need to exempt outstanding figures, which `image_audit.audit()` already enumerates. **Cheap, and it currently fails on exactly one lesson.**

**D-7 — GPT's category scheme (C4) is good but is a new convention.**
*Hardware/library fact · fleet measured fact · starting value · policy value.* Genuinely useful.
Also a new component family. Rule 76: scope the defect before building a convention for it.

---

# PART 5 — DESIGN AND PEDAGOGY (DJ'S CALL — NOT DEFECTS)

Recorded so nothing is lost. None of these is a correctness finding.

- **Challenge workload.** GPT proposes reduced required sets for every lesson (L03: Calibration →
  Ramp Up → Save TRIM → Drive a Square; L04: Line Counter → Edge Guard → Centering Game; L06:
  Pentagon → Line Drill → Odometer → Smooth Stopping; L08, L09, L13, L15 similar). Read against D-1
  and D-2 before acting.
- **§8A trimming.** GPT flags L04, L05, L06, L07, L08 as re-teaching rather than deepening, and
  explicitly says **L09 and L12's §8A are earning their space** (enums/FSMs and fixed-point are
  genuinely new).
- **Student authorship ramp.** L01–L03 finished code → L04–L06 pseudocode → L07–L09 goals + MY PLAN
  → L10–L13 contract only → L14–L15 student-owned experiments → L16 no recipe. GPT names
  `driveUntil()` in L13 as the ideal first "contract, you build it" function.
- **Reveals should ask "compare," not "copy."** A one-line post-reveal obligation: *what did your
  plan do differently? What assumption did you miss?*
- **Stories.** GPT proposes a specific per-lesson list (L02 Apollo/Hamilton · L03 manufacturing
  tolerances · L04 early guided vehicles · L05 TV remote modulation · L06 dead reckoning · L07
  modular software · L08 Watt's governor · L09 machine modes · L10 subsumption/behaviour arbitration, Brooks ·
  L11/L12 navigation · L14 checklist culture · L15 Ziegler–Nichols · L16 Saint-Exupéry) and warns
  against putting a 400-word historical sidebar in all sixteen. **Every story needs sourcing before
  drafting.**
- **A recurring "Engineering Habits" sidebar**, introduced progressively and collected in L16.
- **Units pass · rollover pass · "timeouts on physical loops" as a global rule by L12–L13 ·
  "same symptom, different cause" as a repeated theme · cumulative sabotage progression
  (syntax → subsystem → architecture/measurement/model).**
- **The `Blueprint_Image_Prompt_GPT_Feedback.docx`** is not a review at all — it's a reusable
  style prompt ("RoboLore Blueprint / CAD Style") for the graphics chat. Filed for the graphics
  work, unrelated to lesson defects.

---

# PART 5b — THE CALIBRATION PASS (S154, run before any ruling)

Seven findings decidable from the repo alone were measured, to establish how much weight the
~200 unverified AGREEs deserve. **GPT went 6 for 7.**

| ID | Measured result |
|---|---|
| L02-02 | ✅ §8A.2 and §8A.3 use `ledRed(1)/ledRed(0)`; the other seven `blinkLED` definitions use `ledYellow`. 34 `ledYellow` vs 6 `ledRed` in the lesson |
| L02-03 | ✅ Same two blocks — `void blinkLED()` with `{` on its own line. Free: same passage as L02-02 |
| L02-05 | ✅ §3.3 says "the very first warm-up"; Warm-Up 1 has no `if(`, Warm-Up 2 does |
| **L02-07** | ❌ **GPT WRONG.** Payload is 95 total / 86 non-blank / 75 code. The lesson's 85–95 is correct |
| L08-13 | ✅ One challenge says "21-column screen position", then "the 20-column display", and maps to `0-20`. `setLayout21x8` |
| L06-01 | ✅ `(distanceCm > 0) ? DRIVE_SPEED : -DRIVE_SPEED` then `setSpeeds(speed + TRIM, speed)` — in `driveDistance`, the finished build, and `driveDistanceSmooth` |
| L01-14 | ✅ Both halves, and L01 is the only lesson with the defect |

**What this licenses and what it does not.** GPT is a reliable instrument on checkable claims —
it named the four missing figures exactly. But 6/7 is not 7/7, and **L02-07 is the shape of the
miss to watch for: a confident, specific, plausible number that is simply wrong.** Every remaining
row still needs its own check before it becomes an edit. My AGREE means *the claim is coherent and
the fix would make sense*; it does not mean *measured*.

**Correlated instruments.** GPT and Claude are the same kind of tool reading the same HTML with no
robot and no compiler. Agreement between us is weak evidence of correctness and strong evidence of
a shared blind spot (rule 79). The bench items and the toolchain are the uncorrelated instruments,
and they are the ones that settle a physical claim.

---

# PART 6 — WHAT I NEED FROM DJ

**Rulings, in the order that minimises rework:**

1. **The six canon statements (C1–C6).** Each collapses 15–40 findings. Nothing else should start
   first — GPT's Pass 1 ordering is right and matches how this repo already works.
2. **D-2:** adopt the three-category repetition rule (exact repetition / spiral retrieval / spiral
   deepening) as the standard for every cut-or-keep question?
3. **Price-before-ruling on D-3 (`followLine()` move) and D-4 (`WHEEL_BASE_MM` rename).**
4. **The rulebook verification pass** (D-5) — one read of `RCJRescueLine2026-final.pdf` settles
   eight findings across L14 and L16.

**Then, in GPT's recommended pass order:**

- **Pass 1 — Canon.** C1–C6 applied book-wide.
- **Pass 2 — Continuity.** Reverse TRIM (L06-01) propagated through L07 and L13; encoder
  measurement; gyro reset; kill-switch claims; whatever L08-02 and L08-07 resolve to.
- **Pass 3 — Pedagogy.** Re-teaching, authorship ramp, challenge load.
- **Pass 4 — Evidence.** Byte figures, thresholds, citations, stories, captions.

**Standing constraints that don't change:**

- Photography (8 stills, 4 videos) remains the only item on the critical path to September 8.
- Nothing in this file is verified against the tree. Verification precedes editing.
- READ → FIX → QUIZ, and the read does not transfer between sessions (rule 37).

---
*Worklist v1.12 · built S154, corrected S155 · 18 documents, 68,123 words · 245 findings indexed · 7 measured (6 confirmed, 1 refuted) · 100 closed as of S192 · L01-02's scope re-measured after the S154 figures proved to be line counts*

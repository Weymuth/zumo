# ZUMO — Fix Tracker

**Version:** v1.3 · **Opened:** S184, Aug 22 2026, per DJ ruling — *"Can you create a Fix Tracking
.md that we can put the things we are deferring that we know need to be fixed, but are skipping for
now while we are focusing on other lesson fixes."*

**Status:** **KNOWN DEFECTS IN LIVE BOOK CONTENT, DEFERRED FOR SEQUENCING.** Every row is something
a student can meet, that we know is wrong, and that we chose not to fix *yet* because a different
lesson had the session. Nothing here is a design question and nothing here is waiting on a ruling —
those go elsewhere.

---

## THE CONTRACT, AND WHY IT IS NOT ONE OF THE OTHER FOUR FILES

This repo already has four deferral trackers and they were nearly merged. They are not the same
thing, and merging them destroys what each one is for:

| File | Holds |
|---|---|
| `ZUMO_AFTER_LAUNCH.md` | live, **correct** content that could be better — date-gated on Sept 8 |
| `ZUMO_PARKED_EXIT_ITEMS.md` | content that **was live** and was displaced by a §25 conversion |
| `ZUMO_SHELVED_CARDS.md` | card proposals that were **never live** |
| `ZUMO_BENCH_TESTS.md` | claims that need **the robot in your hands** |
| **this file** | **live content that is WRONG, deferred only by focus** |

`ZUMO_AFTER_LAUNCH.md` states its contract in one line — *nothing here is a defect a student will
meet in the term as taught.* **This file is the exact inverse of that sentence.** A row here is a
defect a student CAN meet. If a row stops being wrong, it leaves; if it stops being reachable by a
student this term, it moves to `ZUMO_AFTER_LAUNCH.md` rather than staying.

**A ROW IS NOT A PARKING SPACE.** Every row names what closes it, so picking it up later is a
comparison and not a re-derivation (§24.13).

---

## A DERIVED ROW POINTS AT ITS INSTRUMENT — IT DOES NOT RESTATE IT

**Where an instrument already knows the defect, this file names the instrument and stops.**
Copying the rows in would create two homes with no comparator, which §24.18 rules is two versions —
and that is precisely the defect class most of this file is about. This is the same discipline
`LIVE_ZUMO_TEXTBOOK.md` already uses for quiz banks (*derive with `quiz_bank.py --status` — do not
hand-count, and do not keep a list here*).

---

# 1. RETIRED SECTION NAMES — 7 sites, L05 and L06

**Derive the list:** `python3 prose_canon.py --residue`
**Gated by:** gate 79 (§18.3b). These sites are PINNED in `prose_canon.RESIDUE`, so they do not fail
the suite — **but new drift fails immediately and a pin whose site gets fixed becomes an ORPHAN and
also fails.** The list can only shrink.

**What they are.** §18.3a retired `CONFIGURATION` → `CONSTANTS`. L05 §5.3's heading, L06's Step 5
and Step 9 headings, and four matching Maker labels still carry it, while the payloads those rows
hand out banner `CONSTANTS`. A student reads one name and opens another.

**Why deferred.** S184's pass was scoped to L01–L03 by DJ. These are L05/L06.
**What closes it.** The L04–L08 sweep. The three lesson headings and the four Maker labels are
**one fix, not two** — a step title and the dropdown row that opens it must move together.
**Cost:** prose and labels only, zero flash bytes. Lesson + Maker version bumps and the `source:`
pins for any bank pinning L05 or L06.

---

# 2. `prose_canon.py` — THREE OF FOUR ARMS UNBUILT

**Derive the status:** `python3 prose_canon.py` prints the unbuilt arms in its own output.

| Arm | Checks | Last found by hand |
|---|---|---|
| 1 | printed banner **sequences** vs canon order | **S184** — L03 Step 11 printed the retired order |
| 2 | **placement** claims ("above `setup()`") | S182 — six in L03, one breaking a red-build exercise |
| 3 | retired names | **BUILT S184**, gate 79 |
| 4 | **section-count** claims ("seven sections") | **S184** — L02 objective said 7 where the lesson taught 9 |

**Why this matters more than it looks.** All 79 gates run **payload → lesson**;
`gate_payload_match` is a SUBSET test (§16.45), so stale prose is invisible to the whole suite by
construction. Arm 3 closes one claim class. **Arms 1 and 4 each caught a live defect in S184 and
are still guarded by nothing.**

**Why deferred.** Arm 3 shipped with fifteen controls. Shipping the other three without a control
per arm is what §16.50 records the cost of, and the S184 double check found an inflection gap in
arm 3 that only a control caught.
**What closes it.** One arm at a time, each with a plant-fires / legitimate-is-silent pair before it
is wired into the suite.

---

# 3. STANDING INSTRUMENT AND CANON DEBT

| Item | Recorded | Note |
|---|---|---|
| `gate_payload_match` is **not** one of the gates | S137 | run it by hand; it takes arguments |
| `byte_audit` ARM 2 **cannot see a figure in prose** | standing | stated blind spot, rule 78 |
| **No gate for `GPT_WORKLIST.md`** | S174 | `--check` closes what a ritual can reach; the gate costs an SVG pass on every run |
| **§16.32–§16.44 have no numbered bodies** | standing | the §18.3b shape — a rule whose only home is a changelog holds only where somebody looks. §18.3b itself was seated at S184; these are the remainder |
| `prose_canon` arm 3 **cannot see lowercase `configuration`** | S184 | stated scope limit — *"the three-sensor configuration"* is correct English in exactly the band where the section name would be wrong |

---

# 4. RULED BUT UNBUILT

**Empty sections should NAME THEIR DESTINATION** — `// ===== CONSTANTS ===== (moved to
RobotConfig.h)` rather than `(none needed)`. **DJ ruled this at S183 and it is not built.**

**Priced at S184 and the ruling does not fit the tree as worded.** The `(none needed)` population is
**133 sites and every one is L01–L07** — no multi-file `main.cpp` carries one. In L08–L16,
`CONSTANTS`, `FUNCTION PROTOTYPES`, `HELPER FUNCTIONS` and `HARDWARE OBJECTS` are **absent
entirely**, so the pass is an ADD of ~148 × 4 banners, not an edit. Twenty multi-file `main.cpp`
lack even `GLOBAL VARIABLES`.

**Coupled and larger: helper bodies defined ABOVE `setup()`** — **1,106 across 148 payloads in
L08–L16**, not the three functions in three lessons the S184 handoff named. Under the L13–L16
freeze it is 429 of 1,106, which is the partial-rollout shape S183 ruled against for the rename.

**What closes it:** a DJ ruling on scope (book-wide vs L08–L12) and on what the empty banner should
name, since the support files do not reuse the canon names. **Expect red in the middle** — S157
measured 306 findings between two green endpoints.

---

# 5. NOT DEFECTS — recorded so they are not re-reported

Both were carried as "confirmed live errors" into S184 and **both are false.** Measured, not
re-read. Do not reopen without an artefact.

- **A-Star hardware identity.** Closed at S162/S163, held by gate §16.25. All 18 mentions in
  L01–L03 are correct. ~~L03's two are a filename whose alt text and caption both say *Zumo 32U4 Main
  Board*.~~ **SUPERSEDED S194 — that sentence recorded the retired state as the target.** DJ ruled
  *"Fix it everywhere."* The board is the **`Zumo 32U4 OLED Main Board`**, a different Pololu product
  from the plain `Zumo 32U4 Main Board`; the asset is now
  `L03_IMAGE_3-14_zumo_32U4_oled_main_board.jpg` and the filename hits are gone.
  **This entry is why the tracker is read before the lessons: it would have told a future session to
  restore the retired name.** §16.25 is LOCKED at Bible **v8.190**, and the retirement is registered
  as `retired_claims` #24 — which does NOT read this file, so nothing but a human catches it here.
- **L03 battery threshold.** All 34 figures across L01–L03 agree at 5,400 / 4,800 / 4,200. L01
  Challenge 11's 4,500 is a deliberate teaching point that explains why the warning is not at 4,200.

- **L03 §8A.5 and §8A.6 are LOAD-BEARING — do not demote them to an optional preview (S186).**
  `L04-01` proposed exactly that, on the ground that arrays are taught twice. **REFUTED, and the
  premise is wrong before the cost is:** L03 §8A.5 teaches array-as-a-row-of-constants-YOU-wrote
  (index as a variable, out-of-bounds hazard) and exists to motivate §8A.6's modulo wrap; L04 §5.5
  teaches array-as-a-buffer-a-FUNCTION-fills plus the index↔sensor-number mismatch table the lesson
  calls its number-one bug source. The only shared sentence is *counting starts at zero*, restated
  in L04 for a different reason — and **L04 §5.5 already opens as retrieval** (*Lesson 3 promised…
  its §8A.5 gave you the tool*), which is `L03-07`'s shape rather than duplication.
  **Six graded questions depend on the two sections** — `L03_B44/B45/B46/B55` (four by explicit
  cite), `L03_A13`, and `L03_A22`'s matching pair — plus **L03 Challenge 5, whose two blanks ARE
  §8A.5 and §8A.6** (*the index you read*, *the wrap divisor*). Challenge 5 declares its own array,
  so it is syntactically self-contained; strip the sections and it stops being teachable and becomes
  fillable by pattern-match.
  **The cost argument was overstated in S186's first pass and is WITHDRAWN, which is why this row
  says so:** the anchor sweep found **no `id` anchors and only 2 prose cross-refs book-wide**, and
  the Maker carries **0** sites for `TEST_SPEEDS` / `NUM_SPEEDS` / `speedIndex` — no census, no
  recompile, no byte cost. **Refuted on the pedagogy, not on the price.** A future reader who
  re-prices this and finds it cheap has found what S186 found; the reason it stays is above.

---

# 6. SETTLED — FIXED, AND THE FIX IS NON-OBVIOUS. DO NOT REVERT.

**THE 4,200 mV BATTERY THRESHOLD IS A STOP LINE, NOT A DAMAGE LINE (S185).**
The book no longer says anywhere that crossing 4,200 mV damages the cells. **That wording is the
intuitive one and somebody will restore it**, so: 4,200 ÷ 4 = **1.05 V per cell**, and a NiMH cell's
accepted discharge cutoff is **~1.0 V per cell** — the threshold sits ABOVE the limit deliberately, with
margin, which is why consumer devices commonly stop near 1.05 V/cell too. **The damage mechanism is CELL
REVERSAL in a series pack:** a single cell taken to zero is not harmed; the harm is the weakest of four
emptying first and the other three pushing current backwards through it. §3.6 now teaches that. **Nine
sites moved together** — L03 ×4, L01 ×2, Maker c11 ×2, `QUIZ_L03` B18 — and B18's *correct* answer was
one of them. **If you change one, change all nine or the bank grades a claim the lesson denies.**

**L01 CHALLENGE 11's 4,500 SPLIT IS NOT PART OF THAT FIX AND MUST NOT BE TOUCHED.**
§5 records it as a deliberate teaching point. S185 removed only the word *damage* from the reveal; the
4,500-vs-4,200 argument stands and reads *a warning that fires at the moment you must STOP arrived too
late*. **Do not "finish the job" by re-baselining 4,500.**

**L03's QUICK REFERENCE NO LONGER STATES A PRECISION FIGURE (S185).**
`L03-09` removed the unsourced ±10% from §4.3 at S179 and **missed the Quick Reference**, which
contradicted `L03_B35`'s keyed answer for six sessions. The line now reads *(an estimate -- read it motors
OFF)*, which is what §4.3 and B35 both say. **A figure here needs a fleet measurement, not a datasheet
guess (rule 50).**

**L03 §3.25 IS RETRIEVAL FROM L01, NOT ITS OWN EXPERIMENT (S185).**
It deliberately does NOT re-run the three-run scatter; L01 Challenge 6 already did that and tells the
student to keep the numbers *for Lesson 3*. **If C6 ever stops saying that, §3.25 loses its premise.**
The section also states no comparison between run-to-run scatter and the condition shift, because that
relative size is unmeasured.


**Section 5 holds claims that were never defects. THIS section holds the opposite: real defects,
now fixed, whose fix a well-meaning reader could mistake for the error.** A row lives here only if
reverting it is plausible. The reasoning travels with it so a later look is a comparison, not a
re-derivation (§24.13).

**L02 hardware table — `Zumo32U4Motors` reads "Lessons 1–2 (taught in 3)" (S184).**
It said *Lesson 3*. Four sources say otherwise: L02's own prose two sections away
(*"Lesson 1 touched five: Button A, the display, the yellow LED, the buzzer and the motors"*),
L03 §4.1 (*"Lesson 1's program moved it, and Lesson 2's Warm-Up 4 spun it in place"*), **all eleven
L01 challenge payloads declaring `Zumo32U4Motors`**, and L02's own `speed_limit` bonus.
**THE FIRST FIX WAS ALSO WRONG.** Setting it to a bare *Lessons 1–2* matched the three sibling rows
but destroyed a real signal: the column's later rows (LineSensors → 4, Encoders → 6) read as
*first **taught***, and both `L02_A18`'s rationale and L02's own TIP say L03 owns the motors.
**Motors are the ONLY object in the table met before they are taught, so the column cannot
disambiguate itself.** The compound cell is true under either reading. **Do not "tidy" it back to a
single lesson number** — that is the defect, in one direction or the other.

**L02 §3.4 — the float claim no longer says "the first time you divide" (S184).**
It read *"you will need one in Lesson 6, the first time you divide."* The float half is TRUE: L04
and L05 declare none and L06 is genuinely the first. **The appositive was false** — L03 divides five
times, and L02's OWN Step 10 solution prints `millis() / 1000`. §16.16: a superlative is a claim
about the other lessons. Now reads *"where dividing has to keep the fraction"*, which is the true
statement the sentence was reaching for. **Do not restore the shorter phrasing.**

**L03 Step 11 — the nine-piece order is DERIVED, not authored (S184).**
The checkpoint printed helpers ABOVE `setup()` with HARDWARE OBJECTS and FUNCTION PROTOTYPES
missing, while claiming *all 9*. The replacement was taken from **L02's own nine-section colour
key**, so the two lessons cannot drift apart. **If this order ever needs to change, change L02's
colour key first and re-derive** — do not edit the L03 line alone.

**L01 BC02 skill 4 — matches its objective twin (§25.5, S184).**
It asked students to tick *"a project for the A-Star 32U4"* two screens after §3.3 says
**"Your robot does not contain an A-Star board."** Its objective twin was already correct. Both
homes now read *Zumo 32U4 (build target `a-star32U4`)*. **See §16.25 before touching any A-Star
wording — it is LOCKED and this question has now cost four rulings.**

---

## HOW TO ADD A ROW

Name **where**, **what is wrong**, **why it was deferred**, and **what closes it**. If an instrument
can already find it, name the instrument and its flag instead of pasting the list. If it turns out
not to be a defect, move it to section 5 with the measurement rather than deleting it — a row that
vanishes gets rediscovered.

---
*Fix tracker · opened S184 · Zumo 32U4 Robotics · Mercersburg Academy*

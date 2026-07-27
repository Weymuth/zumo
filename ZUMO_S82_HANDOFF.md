# ZUMO — S82 Handoff (written at S81 close, Jul 26 · paste at top of Session 82)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **25** must PASS (gate file **v1.11**). Then
   `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. **NEW — `python3 lesson_inventory.py` at open.** The summary table is the structural census; then
   `--anomalies` for the leads list. It has **no exit code and no pass/fail by design** (§24.6a) — it is
   there to be READ. Expect exactly two standing leads (L06 BC01 depth, L09 §7 fence); anything else is new.
6. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
7. **Verify the push landed by grepping a version out of the clone, never by reading the commit message.**
   The label runs one ahead, reliably. S81 opened on `f714997` "session 81 push v2" carrying **S80's** work.
8. **LIVE.md has TWO version homes in its header** (`**Date:**` and `**Versions:**`) — the old "verify
   internal version" banner no longer exists. Do not hunt for a third.
9. **Regenerating LIVE.md means the BODY too.** Dump every `## ` header as a list and read it before
   declaring it done. S81 found **nineteen** headings still reading *WHAT SHIPPED THIS BATCH*; all are now
   *PREVIOUSLY* and exactly one carries the current label. If you see two, the last regen was partial.
10. **A grep is a lead; a parser is the witness — and now the parser is a tool.** Use
   `lesson_inventory.py` to enumerate before scoping anything.
11. **NEW — never `open(path,'w')` on a source file.** S81 truncated the Bible to 0 bytes that way: the
   write raised mid-flight after the open had already emptied it. Recovered from git, md5-verified. Build
   the bytes, assert them, write a `.tmp`, `os.replace`. Every edit script this session does it this way.

## LIVE STATE at S81 close — VERIFIED, gates 25/25 PASS
L01 v03.10.2 · L02 **v03.0.1** · L03 v03.14.0 · L04 v04.7.0 · L05 v04.9.2 · L06 v04.12.1 ·
L07 v04.8.1 · L08 **v04.7.3** · L09 **v05.5.1** · L10 v02.5.2 · L11 v02.7.2 · L12 **v01.7.3** ·
L13 v02.6.2 · L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.67** · Maker v2.45.1 · book_gates **v1.11 (25 gates)** · **lesson_inventory v1.0 (NEW)** ·
Gate v1.6 · Harness v3.0 · pill_sweep v1.0

Brain Check family: NINE of sixteen — L01–L09. Column byte-identical in all nine:
**5,639 chars / md5 `070806a6`, ending `-->`**.

**Structural census (from `lesson_inventory.py`, all 16):** 1,025 headings · 145 constructs · 403
`<details>` / **403 typed** (was 402) · 30 mysteries · 11 section anchors per lesson (10 core + `8a` in 14).

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io). **L12's repaired sentence and
the nine new labels are parse- and gate-verified only** — they want DJ's eyeball on the render.

## DONE IN S81

### 1. NEW TOOL `lesson_inventory.py` v1.0 — S81 PRIMARY (a), approved at S80
One parse per lesson → the full structural table. Views `--versions --sections --headings --constructs
--reveals --braincheck --anomalies --json`, filterable to one lesson (`lesson_inventory.py 09`).
**No exit code, no pass/fail** — §24.6a, a parser is necessary and not sufficient. Pass/fail is
`book_gates.py`'s job; this is for reading.
**The bounding, which is what primary (b) needs:** ELEMENT-BOUNDED (`<div data-challenge>` = open→close)
vs **HEADING-BOUNDED** (`<h4 data-challenge>` = heading → first of *next heading at level ≤ its own* /
*next `data-challenge`* / *enclosing element's close*). Spans from the parse tree, never a fixed window.
**It returns 5/8/2 for 9.m3/9.m4/9.m5** — the read-verified truth, where the §20.1 gate reported 3/8/17
recurring.
Section attribution uses the `id="section-N"` anchors (all 16 lessons; `section-8a` in exactly 14, matching
the §8A map). Fence comments are NOT the spine — only six lessons carry any — so they are enumerated
separately, and the fence-gap lead only fires on lessons that fence ≥5 sections.
Control-run five ways: totals reconcile; L09 headings match three methods; **returns 63 on the
pre-conversion L09**, so the S80 handoff's 63 was right at scoping time and 59 is right now (the conversion
consumed four headings — *not* a discrepancy); mystery counts match a DIFFERENT algorithm (DOM sibling
walk); injected `data-reveal` removal caught, control clean.

### 2. §25.11 — THE NINE LABELS (Bible v8.67, DJ ruling)
*"If it's a hint, then say hint. If its a solution, then call it a solution."* S80's §25.10g retype was
**attribute-only**, which moved the type and left the label contradicting it: nine reveals typed `solution`
still read *"💡 Hint"* — L08 ×4 (`8.m1 8.m2 8.m4 8.m5`) and L09 ×5. **L11 was the model for the third
consecutive session** (`solution` + *"💡 Answer"*, all four) so the fix copied a live precedent.
Kept hints verified not assumed: L05/L06/L07 and L08 `8.m3` are `hint` + *Hint* and hold **no `<pre>` at
all**, which is why §25.10g correctly left them. **L08 holds five copies of the identical summary string and
`8.m3` had to survive** — offset-scoped per §6.12c, +2-byte assert per edit, post-edit assert on `8.m3`.

### 3. §25.12 — THE UNTYPED REVEAL (Bible v8.67)
L02 `2.t1`'s *"🔓 Answers"* block was **the only `<details>` in the book with no `data-reveal` at all**
(403 vs 402 — the one-count gap surfaced it). §20.1's strip list is a whitelist, so it was KEPT and had been
shipping worked answers to the tutor. Typed `solution` on **`2.t5`**'s precedent in the same lesson.
**Count is now the detector: `<details>` total must equal `data-reveal` total.**

### 4. L12's UNESCAPED `<Wire.h>` — live student-facing defect
§6 Step 5's Tip callout held a literal `<Wire.h>`; the browser tokenises it as an element so the sentence
rendered *"The #include  goes at the TOP of the file"*, losing the filename it is about. Invisible to the
§24.6 parse gate because `_STRICT` does not cover unknown tags. Escaped to match **`<pre>` #13 twelve lines
above**, correct all along. Class-scanned: only occurrence in prose (`newproject.html`'s ~400 are inside JS
string literals, legal per the §8.11 corollary).

### 5. book_gates v1.10 → v1.11 — gate 25, same session per §24.2
`§25.11 reveal label agrees with reveal type`. NARROW per §24.6c — label vocabulary is legitimately varied
(62 *reveal solution*, 13 *Answer*, 9 *worked version*) so it asserts only the two contradiction shapes
verified by reading. Control-run three ways: unfixed FAILED catching exactly nine and nothing else; fixed
PASS; reverse drift injected into `8.m3`'s label FAILED.

### 6. Re-verified on an independent parser, per DJ (*"Double check with no grep"*)
Every S81 figure re-derived with BeautifulSoup over **lxml (libxml2)** instead of Python's `html.parser` —
DOM traversal only, no regex, no grep. All nine claims AGREE; nothing retracted. Two wording corrections
made: L09's `section-7` **anchor exists** (only the fence comment is missing), and L09 has **eleven**
section anchors, not ten — an earlier excerpt was clipped at 22 lines.

## S82 QUEUE
1. **S82 PRIMARY — fix the §20.1 gate's per-card bounding** (was S81 primary (b), not started; DJ approved
   at S80). It now has its instrument: `lesson_inventory.py` computes the heading-bounded span correctly,
   so port that bounding into the gate rather than writing a third regex. **Two logged defects:** (a) its
   per-card bounding bleeds — 3/8/17 reported across 9.m3–9.m5 where the truth is 5/8/2, the same defect
   that keeps bonus-challenge leak coverage SUSPECTED in L02/L03; (b) it has no notion of
   `data-kind="mystery"`, harmless under the current ruling but would need re-reasoning if it inverts.
2. **RULED S80, STILL PARKED — L09's three *Problem-Solving* extensions.** DJ: *"No keep them in que."*
   Recorded verbatim in `ZUMO_PARKED_EXIT_ITEMS.md`. Reshaping into mysteries 6–8 is blocked on a
   discovery, not authoring: every L09 construct links its own Maker payload kind, so each needs a new
   sabotaged 8-file payload in `newproject.html` (5.2 MB, edited by offset per §15) plus a byte-match gate
   run — and item 1 ("add a `PAUSED` state") is an *extension* with nothing to sabotage. **Bonus challenges
   are the likelier correct target: same payload cost, no invented bug.**
3. **RE-SCOPED, SUSPECTED — the L02 `2.t4` open item is wrong as written.** The carried text says
   *"L02 `2.t4`'s `check` reveal holds the full worked code"*; **`2.t4` contains zero `<details>`**. The
   `check` reveal it describes is attached to something else — L02 has 8 `check` reveals. Re-scope by
   reading before acting. (This is §25.10f again: a claim inherited from paperwork is a lead.)
4. **Unretired-ancestor gate** — sweep **h3–h4**, not just `<h3>` (all three of L09's ancestors were `<h4>`).
   Remaining targets: L11 *Skills Checklist* · L15/L16.
5. **OTHER GATES WORTH WRITING** (carried): placeholder gate (`{[A-Z_]+}` in an attribute value) · §4.2
   coverage gate (every bonus/mystery `<h4>` carries `data-challenge`) · within-lesson promise gate
   (§25.10d) · §25.2 §-citation presence gate.
6. **5 mysteries still untagged: L04.**
7. **Technical Skills vs §2 objectives — three lessons carry the debt.** L03 8 vs 11 · L04 13 vs 11 ·
   L05 7 vs 10. DJ ruled at S74 to reconcile at the final read-through.
8. **The weeding criterion still does not exist.** §25.8 enforces the floor of 4; nothing says what makes a
   BC03 item weakest. L02 (7), L07 (6), L08 (6) are the candidates. **Blocks the weeding pass.**
9. Bonus placement is a 9/6 split. After §10: L02, L03, L06, L07, L10, L13, L14, L15, L16. In the §9
   region: L04, L05, L08, L09, L11, L12. L01 has none.
10. **L06's BC01 is at div depth 1** where the other eight sit at 0 — inside its §5 panel. One-line fix.
    Now reported automatically by `lesson_inventory.py --anomalies` against the modal family norm.
11. **L13/L14 bonus banners carry a doubled 🕵️** (`&#128373;&#65039;` twice). One-line fix each, found S76.
12. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware &
    Code" — found S72, one-line fix, still not done.
13. Warm-ups L02–L16 + spiral aiming rule — still **L02-ONLY**, so L02 is the prototype.
14. L13/L15 have no exit blocks at all · within-lesson build-on mark · going_deeper footer contrast +
    duplicated hero title.
15. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen.
16. **L09 §7 has no SECTION fence comment and §8 has TWO.** Confirmed at S81 from two directions: the
    `section-7` ANCHOR is present, only the fence comment is missing, and L09 fences 9 of its 10 sections
    so the gap is real rather than sparse usage (L03/L07 fence 1–2 and are correctly silent).
17. **NEW, observation not finding — L08 `8.m3`'s prose hint names the deleted call outright**
    (*"the `calibrateLineSensors();` call was deleted from setup"*). It is correctly typed `hint` (no
    `<pre>`), but §20.1 keeps `hint` and open prose reaches the tutor, so the tutor is told the answer. Not
    compared against L05–L07's hints yet, so it is NOT being called a defect. Read before ruling.

## OPEN — NEEDS A DJ RULING
- **L02 `2.t4`'s `check` reveal** — see queue item 3: the item must be re-scoped before it can be ruled on.
  The S80 mystery ruling and now §25.11/§25.12 all point the same way for whatever the real block is.
- **The weeding criterion** (queue item 8) — blocks the weeding pass.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge cards
  (sixteen sessions now) · spiral marking format review · DJ tier pass + rolling depth read (L14 first) ·
  copyright line (RoboLore, work-for-hire) · bonus-challenge pill + livery when they move to §9.

## STANDING QUEUE (carried; SUSPECTED until re-checked per §24.6c)
L02 `2.t7` label collision (VERIFIED latent) · BENCH: compile-verify L07 finished + trapezoid · L08 Racing
Line · L11 C4 double-TRIM · Q017 L09 six numbers · calibration-spin · gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · L15 C04–C07 no-template shape · L01 VS Code multi-root step · landing-page/book color
mismatch · Maker batch (bulk DL · `?lesson=N` gate · C## labels · verify `?kind=` starters) · TDP v3
(A5 Lab Log + printed 16 log prompts) · course docs (grid + syllabus) · "pick your robot" chooser ·
AI Tutor DISCOVERIES picker · QA_* sheets in images/glowbots · border inset 10–18 vs 64 · Canvas reading
quizzes (book first, then Canvas).

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page — **note:** it has a home now, as L01's
§4 Hardware, with Install moving down.

## PUSH LIST — S81 (nine files)
`lessons/Lesson_02.html` (v03.0.1) · `lessons/Lesson_08.html` (v04.7.3) · `lessons/Lesson_09.html`
(v05.5.1) · `lessons/Lesson_12.html` (v01.7.3) · `ZUMO_SUPER_BIBLE.md` (v8.67) · `book_gates.py` (v1.11) ·
`lesson_inventory.py` (**NEW**, repo root) · `LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_S82_HANDOFF.md`.
No `git rm` lines. Maker untouched. Push order does not matter this batch — no images, no payloads.
**After pushing:** fresh `git clone --depth 1` into a NEW directory, allow ~20–30 s for propagation, grep a
version out of it, and run `book_gates.py` (25/25) against the clone.

---
*Written at S81 close, July 26 2026. The session's shape was that the instrument built to stop the guessing
immediately caught the guesser. `lesson_inventory.py` was approved because "GREP always missing something,"
and the first thing it reported was a heading count that disagreed with the handoff — until the historical
file showed both numbers were true at different times, which is the failure mode the tool exists to
prevent, caught by the tool. Then it found the one untyped reveal in four hundred and three, and a literal
`<Wire.h>` that had been silently deleting a filename out of a student instruction. DJ's answer to the
label question was one sentence and settled a thing I had framed as a design choice: if it's a hint, say
hint. The precedent was already in L11, for the third consecutive session — the same lesson that was right
about the type at S80 and right about the strip at S79. And the worst moment of the session was mine: an
`open(path,'w')` truncated the Bible to zero bytes because the write raised after the open had already
emptied the file. Git had it, md5 confirmed it, and every edit script now builds bytes, asserts them, and
`os.replace`s a temp file. A tool that verifies the book is not exempt from needing verification itself.*

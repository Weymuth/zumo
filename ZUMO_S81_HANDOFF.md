# ZUMO — S81 Handoff (written at S80 close, Jul 26 · paste at top of Session 81)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **24** must PASS (gate file **v1.10**). Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
6. **Verify the push landed by grepping a version out of the clone, never by reading the commit message.**
   S79 opened on a tree missing S78's work; S80 opened on `f28ab4c` "Session80 push" which carried **S79's**
   deliverables. The label runs one ahead, reliably. The GitHub API (`/commits/{sha}`) lists changed files.
7. **NEW — a grep is a lead; a parser is the witness.** S80's opening report was wrong three times because a
   keyword-filtered `<h4>` grep hid two live blocks and a single-line regex missed 28 headings. The HTML
   parser found 63. Enumerate structure with a parser before scoping anything.

## LIVE STATE at S80 close — VERIFIED, gates 24/24 PASS
L01 v03.10.2 · L02 v03.0.0 · L03 v03.14.0 · L04 v04.7.0 · L05 v04.9.2 · L06 v04.12.1 ·
L07 v04.8.1 · L08 **v04.7.2** · L09 **v05.5.0** · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 ·
L13 v02.6.2 · L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2
Bible **v8.66** · Maker v2.45.1 · book_gates **v1.10 (24 gates)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Brain Check family: NINE of sixteen — L01–L09.** Column byte-identical in all nine:
**5,639 chars / md5 `070806a6`, ending `-->`** (verified against all nine this session).

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io). **Nothing on L09 is
render-verified** — the four new blocks, the five retyped mystery reveals, and BC02's seven-item skill
lock have been parse- and gate-verified only.

## DONE IN S80

### 1. L09 v05.4.2 → v05.5.0 — the ninth conversion
- **BC01 · Mental — 5 items, AUTHORED.** L09 had no Mental ancestor: zero `check` reveals, zero `quiz`
  before §6, zero TRY IT boxes. The S80 handoff's *"redistribution job, not an authoring job"* was wrong.
  Items cite §3.1 · §3.2+§3.3 · §3.4 · §3.5 · §3.6. Seated at the §5/§6 seam at div depth 0.
- **BC02 · Technical Skills — §2's SEVEN objectives, character-exact** per §25.5. The live *Technical
  Skills* block had **five** items and was not the source; migrating it would have joined L09 to the
  L03/L04/L05 reconciliation debt. Rule in bytes: literal `☐ ` + the objective's text after `&#9744; `.
- **BC03 · Knowledge Check — 4 items.** See the ruling below.
- **BC04 · Reflection — 3 items:** L09's live *Reflection: Draw Your State Diagram* migrated, plus two
  authored. **Engineer's Log is NOT BC04's ancestor** — it survives as a separate block after BC04 in
  L05/L06/L07/L08. I claimed otherwise mid-session and was wrong.
- *Calibration Data Record* stays outside the family (S78 ruling, Bible-confirmed).
- Five mysteries tagged `9.m1`–`9.m5` with `data-kind="mystery"`.

### 2. BC03 — the duplicate inverted L05's precedent (DJ ruling: *"Fix and go with KC"*)
L09's ancestors were **four**, not the two §25.10f recorded: *Technical Skills* (5), *Conceptual
Understanding* (4 Q&A, answers in open prose, **no reveal at all**), *Problem-Solving* (4), *Knowledge
Check* (3, already `quiz`). Diffing the duplicates per §25.10c: **CU is a strict superset of KC** —
items 1–3 word-identical, CU alone carrying the enum question. So *Knowledge Check* migrated verbatim,
which the handoff predicted would "land correct by construction," **would have failed §25.8's floor at
three items.** BC03 = KC's three answers verbatim (extracted byte-exact, not retyped) + CU's enum item
extended to KC's depth. **Neither ancestor carried a single §-citation**, so §25.2's name-your-section
rule was authored in: §3.1 · §3.4 · §3.6 · §3.5. Shape is question-in-summary, the 6/8 majority
(L01–L06); L07/L08 use prose + "Show answer" and are the drift.

### 3. DJ RULING — the mystery reveal is a `solution` (Bible §25.10g, v8.66)
*"Wouldn't we want it to have a solution drop down?"* — and the gate was right, the book was wrong.
§11 (v8.17) says a mystery **displays** its planted line (*"The planted constant:"* / *"as planted:"*);
that governs display, not reveal type. §20.1 (v8.37) already said it outright: a debugging-mystery
bug+fix reveal must be `solution` or it leaks. **L11 had been compliant all along** (four mysteries,
all `solution`), so this was a drift against a live precedent, not a coin-flip. Census: planted code in
a `hint` existed in exactly **two** lessons — L08 (4 blocks) and L09 (5). L05/L06/L07 mysteries carry
hints with no code, which is why it stayed invisible. **The gate passed L08 for eight sessions on
snippet length alone** — §20.1 needs ≥3 statement lines and L08's planted snippets run 1–2. Retyped
attribute-only, by offset, with a +4-bytes-per-edit length assert. L08 → **v04.7.2** (visible banner
unchanged per §5b).

## S81 QUEUE
1. **OPEN RULING — L09's three parked *Problem-Solving* extensions.** Recorded verbatim in
   `ZUMO_PARKED_EXIT_ITEMS.md`. DJ ruled at S80 to reshape them into mysteries 6–8; that is blocked on a
   discovery, not on authoring. **Every L09 construct links its own Maker payload kind** — all six
   challenges and all five mysteries — so each new mystery needs a new sabotaged 8-file payload in
   `newproject.html` (**5.2 MB**, edited by offset per §15) plus a byte-match gate run. And a mystery is a
   planted *defect* while these three are *extensions* — item 1, "add a `PAUSED` state," has nothing to
   sabotage. **Bonus challenges are the likelier correct target: same payload cost, no invented bug.**
2. **§20.1 GATE HAS TWO LOGGED DEFECTS, NEITHER FIXED.**
   - **Its per-card bounding bleeds.** It reported 3/8/17-line blocks recurring across 9.m3/9.m4/9.m5;
     the truth is one block each at **5/8/2** lines. Same nested-card bounding defect that keeps
     bonus-challenge leak coverage SUSPECTED in L02/L03. **The failure was diagnosed by reading the three
     cards — the gate's own line counts were fiction.**
   - **It has no notion of `data-kind="mystery"`.** Nothing breaks under the current ruling, but the
     reasoning would have to be redone if the ruling ever inverts.
3. **Unretired-ancestor gate — the spec on the S80 queue was wrong.** It said *"any `<h3>` in §10 of an
   unconverted lesson."* All three of L09's ancestors were `<h4>`; only *Knowledge Check*, the one block
   already correct, was an `<h3>`. **Sweep h3–h4.** Remaining targets: L11 *Skills Checklist* · L15/L16.
4. **OTHER GATES WORTH WRITING** (carried): placeholder gate (`{[A-Z_]+}` in an attribute value) ·
   §4.2 coverage gate (every bonus/mystery `<h4>` carries `data-challenge`) · within-lesson promise gate
   (§25.10d) · **§25.2 §-citation presence gate** — new, prompted by both L09 ancestors carrying none.
5. **5 mysteries still untagged: L04.** L09's are done.
6. **Technical Skills vs §2 objectives — three lessons carry the debt.** L03 8 vs 11 · L04 13 vs 11 ·
   L05 7 vs 10. DJ ruled at S74 to reconcile at the final read-through. **L09 avoided joining it** by
   migrating objectives per §25.5.
7. **The weeding criterion still does not exist.** §25.8 enforces the floor of 4; nothing says what makes
   a BC03 item weakest. L02 (7), L07 (6), L08 (6) are the candidates.
8. Bonus placement is a 9/6 split. After §10: L02, L03, L06, L07, L10, L13, L14, L15, L16. In the §9
   region: L04, L05, L08, L09, L11, L12. L01 has none.
9. **L06's BC01 is at div depth 1** where the other eight sit at 0 — inside its §5 panel. One-line fix.
10. **L13/L14 bonus banners carry a doubled 🕵️** (`&#128373;&#65039;` twice). One-line fix each, found S76.
11. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware &
    Code" — found S72, one-line fix, still not done.
12. Warm-ups L02–L16 + spiral aiming rule — still **L02-ONLY**, so L02 is the prototype.
13. L13/L15 have no exit blocks at all · within-lesson build-on mark · going_deeper footer contrast +
    duplicated hero title.
14. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen.
15. **L09 §7 has no SECTION fence comment and §8 has TWO** — headings 7.1/7.2 exist, the fence does not.
    Noticed in passing, structure gate passes, unexamined.

## OPEN — NEEDS A DJ RULING
- **The three parked L09 extensions** (queue item 1) — mysteries vs bonus challenges.
- **L02 `2.t4`'s `check` reveal** — carried from S79, holds the full worked code for a TRY IT the card
  tells students to translate themselves. `check` is KEPT by §20.1. **The S80 mystery ruling is the
  nearest precedent and points the same way.**
- **The weeding criterion** (queue item 7) — blocks the weeding pass.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge cards
  (fifteen sessions now) · spiral marking format review · DJ tier pass + rolling depth read (L14 first) ·
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

## PUSH NOTE — files changed this session
`lessons/Lesson_09.html` (v05.5.0) · `lessons/Lesson_08.html` (v04.7.2) ·
`ZUMO_SUPER_BIBLE.md` (v8.66) · `ZUMO_PARKED_EXIT_ITEMS.md` · `LIVE_ZUMO_TEXTBOOK.md` ·
`ZUMO_S81_HANDOFF.md`. **`book_gates.py` is UNCHANGED at v1.10** — the ruling fixed the book, not the gate.

---
*Written at S80 close, July 26 2026. The session's shape was that every instrument failed before the work
did. A keyword-filtered grep hid two live ancestor blocks and reported two where there were four. A
single-line heading regex missed twenty-eight headings the parser found. An objective window bled into the
next list and the assert caught it. Then the §20.1 gate failed on L09's mysteries and its own line counts
were fiction — 3/8/17 where the truth was 5/8/2 — but the failure underneath was real, and DJ's one-line
question resolved it better than the exemption I was about to propose: the fix was to type the reveals
`solution`, which L11 had been doing all along and which §20.1 had said in writing since v8.37. Nine
mystery code blocks in two lessons had been shipping the planted bug to the tutor, and the gate had passed
them for eight sessions because the snippets were two lines short of its threshold. A gate that passes by
luck is an ungated rule.*

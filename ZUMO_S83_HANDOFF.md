# ZUMO — S83 Handoff (written at S82 close, Jul 26 · paste at top of Session 83)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **26** must PASS (gate file **v1.13**). Then
   `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. `python3 lesson_inventory.py` (**v1.0.2**) — the structural census; then `--anomalies`.
   No exit code, no pass/fail by design (§24.6a) — it is there to be READ. **Expect exactly ONE
   standing lead now** (L06 BC01 depth). The L09 §7 fence lead is closed by construction.
6. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
7. **Verify the push landed by grepping a version out of the clone, never by reading the commit
   message.** The label runs one ahead, reliably — S82 opened on `9639c06` "Push 82 v2" carrying
   **S81's** work.
8. **LIVE.md has TWO version homes in its header** (`**Date:**` and `**Versions:**`).
9. **Regenerating LIVE.md means the BODY too.** Exactly one `## ` heading may read *THIS BATCH*.
   **NEW — bound header rewrites to the first ten lines.** A per-session block further down carries
   its OWN historical `**Versions:**` line (S63's, now ~line 780); an unbounded
   `startswith('**Versions:**')` rewrite silently replaces it with today's numbers and falsifies
   history. S82 caught this only because an assert fired before the write.
10. **A grep is a lead; a parser is the witness — and a parser built against observed practice
    inherits that practice as its definition.** See the S82 fence story below.
11. **Never `open(path,'w')` on a source file.** Build bytes, assert, write `.tmp`, `os.replace`.

## LIVE STATE at S82 close — VERIFIED, gates 26/26 PASS
L01 **v03.10.3** · L02 **v03.0.2** · L03 **v03.14.1** · L04 **v04.7.1** · L05 **v04.9.3** ·
L06 **v04.12.3** · L07 **v04.8.3** · L08 **v04.7.4** · L09 **v05.5.2** · L10 **v02.5.3** ·
L11 **v02.7.3** · L12 **v01.7.4** · L13 **v02.6.3** · L14 **v02.8.3** · L15 **v02.6.3** ·
L16 **v02.5.3** — all sixteen bumped, all minor, visible banners unchanged per §5b.
Bible **v8.68.1** · Maker v2.45.1 · book_gates **v1.13 (26 gates)** · **lesson_inventory v1.0.2** ·
Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Structural census:** 1,025 headings · 174 section anchors · **174 section fences (`sfnc`)** ·
41 PART banner comments (`part`) · 145 constructs · 403 `<details>` / 403 typed · 30 mysteries.
Brain Check family: nine of sixteen (L01–L09), column byte-identical, 5,639 chars / md5 `070806a6`.

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io). Fence comments do not
render, so this batch's risk is nil, but nothing was eyeballed.

## DONE IN S82

### The whole session was one arc: a construct that had no rule
**§6.8a THE SECTION FENCE IS GENERATED FROM THE ANCHOR SPINE (Bible v8.68, DJ ruling).**

Opened on the S82 queue item 16 (*"L09 §7 has no SECTION fence comment and §8 has TWO"*). DJ asked
for the claim to be re-derived without grep; on an independent parser (BeautifulSoup over lxml) the
*"§8 has TWO"* half turned out to be a **prefix artifact** — `SECTION 8` substring-matching
`SECTION 8A`. L09 fenced ten distinct sections with zero duplicates. Pulling that thread found the
real problem: **the fence had never been canonized at all** — zero rules in the Bible — so it had
drifted five ways across ten lessons (L01 at five equals, L09/L10 at twenty-one, L02 bare uppercase,
L04/L06/L08 bare Title Case, L03/L05/L07 mixed) and L11–L16 carried none.

**The coverage illusion.** `lesson_inventory.py`'s matcher required the `=` wrapper, so it was
**structurally blind in five lessons**, and its gap lead only fires at ≥5 fenced sections. That is
why L09's §7 looked like the only fence gap in the book. The truth was **nine gaps across seven
lessons** — L02 (§1 §4 §7) · L03 (§6) · L05 (§7) · L07 (§6 §8 §10) · L08 (§6 §8) · L09 (§7) — plus
stale duplicates in L03 (labelled `(NEW CANONICAL)`) and L08 (`Code Structure` + `Code Walkthrough`
stacked before ONE banner), and L06's `8.5` where canon is `8A`.

**DJ declined the widened matcher** — *"Why widen the fence. Can't we just fix the issues that are
causing the fence issues"* — which is the §24 pattern: widening ratifies drift permanently. Because
the fence is derived from the `id="section-N"` spine, the fix was a **GENERATE, not a repair**: 100
legacy fences removed, **174 canonical written, one per core anchor** (ten in L01/L16 which have no
`8a`, eleven in the other fourteen). No per-instance judgement was needed — L08's mislabelled
`Section 7: Troubleshooting` never had to be diagnosed. Per-file asserts: comment count drops by
exactly the doomed set, non-comment content byte-identical, insertion point is a banner wrapper, no
unsafe title characters (no `--`, no angle brackets, no non-ASCII across all 174).

**The title stays** per DJ (*"Keep title in it"*), derived from the banner: entities decoded, icon
dropped, `Section N:` prefix removed, truncated at the em-dash, uppercased. Safe only because the
gate regenerates and compares it — **L01's fence read `KEY CONCEPTS` while its own banner read
*Background Theory***. The title was already lying. A comma-truncation rule was considered and
rejected: it would butcher L01 §1's `THE TRUE STORY OF "HELLO, WORLD!"`.

**book_gates v1.11 → v1.12, gate 26**, control-run three ways: unfixed source FAILED (79
non-canonical fences + 16 count/title mismatches); a deleted fence FAILED; a fence left stale after
its banner was reworded FAILED. Note the first drift injection was a **no-op** (retitled L07 §3
`THEORY` → `THEORY`) and produced a meaningless PASS — the retry asserted the bytes changed first.

**lesson_inventory v1.0.1 → v1.0.2** splits the conflated `fnce` column: it read **75**, which was
34 section fences plus 41 §6.8 PART banners — two constructs under one label, in the very column
split out at S81. Now `sfnc` (174) and `part` (41). Its source comment claiming "only six lessons
carry any" is corrected: ten did.

**Also corrected this session, my own errors:** an early report repeated the handoff's "11 section
anchors per lesson" as if measured — the truth is 174 core anchors (11 in fourteen lessons, 10 in
L01 and L16 which lack `section-8a`) plus 85 sub-anchors, 259 total. And a claimed
"tool disagrees in fourteen lessons" was a bad comparison on my side, counting every comment
containing the word *section* including `TITLE SECTION`.

### S82b — the loose gate was passing a live layout defect (Bible v8.68.1)
A THIRD verification pass, on an independent parser (DOM traversal, sibling adjacency, `re` never
imported), found **L06 and L07 §5 anchors were not inside their banner div**. The §5 banner had
swallowed the PREVIOUS section's back-to-top link and closed early, leaving `<div id="section-5">` a
bare sibling in the content panel. Rendered result: §5's coloured cap showed a back-to-top link where
its title belongs, and the title appeared as bold text atop the white box. **Pre-existing** —
confirmed against the untouched pre-S82 clone, where L05/L08 were already correct. §24.6 class: it
passes tag balance BECAUSE the counts work out.

Swept the CLASS per §24, not the instance: exactly **2 of 174** anchors were displaced, both §5, both
repaired by reordering to L05's arrangement — same tag multiset, visible text asserted unchanged,
anchor parent re-verified by re-parse. L06 **v04.12.3**, L07 **v04.8.3**.

**book_gates v1.12 → v1.13.** The v8.68 gate compared document-ordered LISTS of fences and anchors, so
content and order verified while PLACEMENT did not. Replaced with a per-anchor walk: anchor seated in a
banner · fence adjacent with only whitespace between · **anchor opens IMMEDIATELY inside the banner**.
That last clause is the one that catches it, because **the nearest preceding `<div>` is not the parent
when a `</div>` intervenes** — the first tightening attempt still PASSED the re-introduced displacement
for exactly that reason, and the injection was verified live before the gate was blamed. Control-run
three ways: displacement FAILED naming the intervening element; a stray `<p>` between fence and banner
FAILED; untouched copy PASSED.

## S83 QUEUE
1. **S83 FIRST — L06's Brain Check 01, per DJ (*"let's fix l06 at the beginning of 83"*).** BC01's
   in-body block sits inside the **§5 "Code Structure Overview" CONTENT panel**
   (`border: 2px solid #3a7d5c`) at div depth 1, where the other eight lessons put BC01 **directly
   under `<body>`**. **This is a SEPARATE deviation from the §5 anchor displacement fixed in S82b and
   was NOT moved by that repair** — re-verified after it. **It is NOT the S71 white-on-white defect**:
   the wrapper is a content panel, not a banner carrying `color: white`, so no text is being lost.
   **Read before moving:** the panel holds 49 direct children, and BC01 is authored at the §5/§6 seam
   per §25.10, so decide whether it belongs outside §5's box (matching the other eight) or whether §5's
   panel legitimately closes later. Confirm the target placement against a conforming lesson before
   lifting.
2. **S83 PRIMARY (displaced from S82) — fix the §20.1 gate's per-card bounding.** Unchanged and
   still approved. `lesson_inventory.py` computes the heading-bounded span correctly, so port that
   bounding in rather than writing a third regex. Two logged defects: (a) bounding bleeds — 3/8/17
   reported across 9.m3–9.m5 where the truth is 5/8/2, the same defect keeping bonus-challenge leak
   coverage SUSPECTED in L02/L03; (b) no notion of `data-kind="mystery"`, harmless under the current
   ruling but needs re-reasoning if it inverts.
3. **NEW, logged not fixed — L02, L06, L15 and L16 carry ZERO PART banner comments** where §6.8
   canonizes four. Surfaced by the new `part` column. **The visible banners have NOT been checked** —
   this may be missing comments only, or missing banners. Read before scoping. A `part` gate is the
   obvious follow-on to gate 26 and would settle it.
4. **RULED S80, STILL PARKED — L09's three *Problem-Solving* extensions.** DJ: *"No keep them in
   que."* Recorded verbatim in `ZUMO_PARKED_EXIT_ITEMS.md`. Blocked on payload work, not authoring:
   every L09 construct links its own Maker payload kind, so each needs a new sabotaged 8-file payload
   in `newproject.html` (5.2 MB, edited by offset per §15) plus a byte-match gate run — and item 1
   ("add a `PAUSED` state") is an extension with nothing to sabotage. **Bonus challenges are the
   likelier correct target: same payload cost, no invented bug.**
5. **RE-SCOPED, SUSPECTED — the L02 `2.t4` open item is wrong as written.** The carried text says
   *"L02 `2.t4`'s `check` reveal holds the full worked code"*; **`2.t4` contains zero `<details>`**.
   L02 has 8 `check` reveals; the one described is attached to something else. Re-scope by reading.
6. **Unretired-ancestor gate** — sweep **h3–h4**, not just `<h3>`. Targets: L11 *Skills Checklist* ·
   L15/L16.
7. **OTHER GATES WORTH WRITING** (carried): placeholder gate (`{[A-Z_]+}` in an attribute value) ·
   §4.2 coverage gate (every bonus/mystery `<h4>` carries `data-challenge`) · within-lesson promise
   gate (§25.10d) · §25.2 §-citation presence gate · **§6.8 PART banner gate** (see item 3).
8. **5 mysteries still untagged: L04.**
9. **Technical Skills vs §2 objectives — three lessons carry the debt.** L03 8 vs 11 · L04 13 vs 11 ·
   L05 7 vs 10. DJ ruled at S74 to reconcile at the final read-through.
10. **The weeding criterion still does not exist.** §25.8 enforces the floor of 4; nothing says what
    makes a BC03 item weakest. L02 (7), L07 (6), L08 (6) are the candidates. **Blocks the weeding
    pass.** NEEDS A DJ RULING.
11. Bonus placement is a 9/6 split. After §10: L02, L03, L06, L07, L10, L13, L14, L15, L16. In the
    §9 region: L04, L05, L08, L09, L11, L12. L01 has none.
12. **L13/L14 bonus banners carry a doubled 🕵️** (`&#128373;&#65039;` twice). One-line fix each.
13. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware
    & Code" — found S72, one-line fix, still not done.
14. Warm-ups L02–L16 + spiral aiming rule — still **L02-ONLY**, so L02 is the prototype.
15. L13/L15 have no exit blocks at all · within-lesson build-on mark · going_deeper footer contrast +
    duplicated hero title.
16. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen.
17. **Observation, not a finding — L08 `8.m3`'s prose hint names the deleted call outright**
    (*"the `calibrateLineSensors();` call was deleted from setup"*). Correctly typed `hint` (no
    `<pre>`), but §20.1 keeps `hint` and open prose reaches the tutor, so the tutor is told the
    answer. Not yet compared against L05–L07's hints, so NOT a defect. Read before ruling.

## OPEN — NEEDS A DJ RULING
- **The weeding criterion** (queue item 10) — blocks the weeding pass.
- **L02's `check` reveal** — item 5 must be re-scoped before it can be ruled on.
- **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge
  cards (seventeen sessions now) · spiral marking format review · DJ tier pass + rolling depth read
  (L14 first) · copyright line (RoboLore, work-for-hire) · bonus-challenge pill + livery when they
  move to §9.

## STANDING QUEUE (carried; SUSPECTED until re-checked per §24.6c)
L02 `2.t7` label collision (VERIFIED latent) · BENCH: compile-verify L07 finished + trapezoid · L08
Racing Line · L11 C4 double-TRIM · Q017 L09 six numbers · calibration-spin · gyro-bias · L02 §5
green-LED · Constrain RUN_MS · L15 C04–C07 no-template shape · L01 VS Code multi-root step ·
landing-page/book color mismatch · Maker batch (bulk DL · `?lesson=N` gate · C## labels · verify
`?kind=` starters) · TDP v3 (A5 Lab Log + printed 16 log prompts) · course docs (grid + syllabus) ·
"pick your robot" chooser · AI Tutor DISCOVERIES picker · QA_* sheets in images/glowbots · border
inset 10–18 vs 64 · Canvas reading quizzes (book first, then Canvas).

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page — **note:** it has a home now, as
L01's §4 Hardware, with Install moving down.

## PUSH LIST — S82 (twenty-one files)
`lessons/Lesson_01.html` … `lessons/Lesson_16.html` (**all sixteen**) · `ZUMO_SUPER_BIBLE.md`
(v8.68.1) · `book_gates.py` (v1.13) · `lesson_inventory.py` (v1.0.2) · `LIVE_ZUMO_TEXTBOOK.md` ·
`ZUMO_S83_HANDOFF.md`.
No `git rm` lines. Maker untouched, no images, no payloads — **push order does not matter.**
**S82b SECOND PUSH (six files, the S82 batch already landed as `fb70426`):**
`lessons/Lesson_06.html` (v04.12.3) · `lessons/Lesson_07.html` (v04.8.3) · `ZUMO_SUPER_BIBLE.md`
(v8.68.1) · `book_gates.py` (v1.13) · `LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_S83_HANDOFF.md`.

**After pushing:** fresh `git clone --depth 1` into a NEW directory, allow ~20–30 s for propagation,
grep a version out of it, and run `book_gates.py` (26/26) against the clone.

---
*Written at S82 close, July 26 2026. The session's shape was that the thing the queue called a
two-part finding was half artifact, and chasing the artifact found that the construct underneath it
had never had a rule at all. The instrument built at S81 to stop the guessing was itself defined by
the drift it was measuring — it reported one fence gap because it could only see the three lessons
written in the style it was built against, and there were nine. DJ's answer was one sentence and it
was the right one: don't widen the detector, fix what's causing the problem. That turned a
seven-lesson repair job with per-instance judgement calls into a generate-from-the-spine pass where
L08's mislabelled section never had to be diagnosed at all. Two of my own numbers needed retracting
along the way, both from repeating a figure instead of measuring it. And the LIVE.md regen tried to
overwrite a historical version line from S63 with today's numbers; an assert stopped it, which is the
only reason this paragraph isn't about that instead.*

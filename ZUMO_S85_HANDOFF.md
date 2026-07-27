# ZUMO — S85 Handoff (written at S84 close, Jul 27 · paste at top of Session 85)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **29** must PASS (gate file **v1.16**). Then
   `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. `python3 lesson_inventory.py` (**v1.0.4**) — the structural census; then `--anomalies`.
   No exit code, no pass/fail by design (§24.6a) — it is there to be READ. `--anomalies`
   has been empty since S83; that is a fact about the detector's coverage, not a
   certificate on the book.
6. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
7. **Verify the push landed by grepping a version out of the clone, never by reading the commit
   message.** The label runs one ahead, reliably.
8. **LIVE.md has TWO version homes in its header** (`**Date:**` and `**Versions:**`).
9. **Regenerating LIVE.md means the BODY too.** Exactly one `## ` heading may read *THIS BATCH*.
   **Bound header rewrites to the first ten lines** — a per-session block further down carries its
   OWN historical `**Versions:**` line (S63's, now ~line 926). **Assert on the HEADING, not the
   substring.**
10. **Never `open(path,'w')` on a source file.** Build bytes, assert, write `.tmp`, `os.replace`.
11. **Read `PUSH_WORKFLOW.md` before writing any delivery instruction** — it now owns the
    DELETION procedure (§12.2, moved there S84 because it had been living only in the handoff being
    deleted). **Gate 28 asserts the root carries exactly one session handoff**, so a missed deletion
    fails a gate rather than waiting to be noticed. DJ pushes with **GitHub
    Desktop** — copy files into the clone, tick the changed files, commit, push. Git CLI commands are
    wrong for him. **Never hand DJ `git rm`.**

### The two rules S84 added to this list
12. **A QUEUE ITEM IS A LEAD, AND SO IS ITS SCOPE.** §24.6c already said a handoff item enters the
    next session as SUSPECTED. S84 extends that from the item's *verdict* to its *premise*: the
    S84 queue's number-one item asserted four lessons were missing PART banner comments. All
    sixteen had four visible banners; two of the four "zero" lessons had comments the matcher
    could not see. Checking the premise cost one read and turned up a defect class nobody had
    named. **Read the item's own framing before you scope work to it.**
14. **A QUOTED NORM IS A LEAD, LIKE A QUOTED FINDING.** The S83 handoff recorded the Brain Check
    norm as *"BC01 under `<body>`, 8 of 9"*. It was 9/9 — the count predated S83's own L06 fix.
    Recount a norm against the files before canonizing or gating it.
15. **ASK WHAT A COMPONENT SITS ON, NOT ONLY WHETHER IT EXISTS.** Placement has now been the
    unasserted half three times running: S82 the section anchor, S84 batch 1 the PART banner, S84
    batch 2 the Brain Check. Every gate asked whether the block was present; none asked what it was
    nested in.
16. **A PROCEDURE STORED INSIDE THE ARTEFACT IT OPERATES ON IS NOT STORED.**

13. **§24.6b IS NOT "ASSERT SOMETHING CHANGED".** It is *assert the injection landed in the shape
    you intended*, re-parsed and read back. S84's placement control PASSED on its first run with
    an innocent gate: the test extracted the block by truncating at its first `</div>`, which is
    the **title** div, so only a fragment moved and `blk in s2` passed on a surviving prefix.

## LIVE STATE at S84 close — VERIFIED, gates 29/29 PASS
L01 v03.10.4 · L02 v03.0.3 · **L03 v03.14.3** · **L04 v04.8.0** · **L05 v04.10.0** · L06 v04.12.5 ·
L07 v04.8.4 · L08 v04.7.5 · L09 v05.5.3 · L10 v02.5.4 · L11 v02.7.4 · **L12 v01.8.0** ·
**L13 v02.7.0** · **L14 v02.9.0** · L15 v02.6.4 · L16 v02.5.4 — **all sixteen changed this session.**
Bible **v8.71** · Maker v2.45.1 · book_gates **v1.16 (29 gates)** · **lesson_inventory v1.0.4** ·
**gen_part_banners v1.0 (NEW)** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0

Bold five are MODERATE bumps (rendering changed, both visible banners moved per §5b). The other
eleven are MINOR — generated comment + entity encoding only, renders identically, visible banner
untouched.

**Structural census:** 1,025 headings · 174 section anchors · 174 section fences (`sfnc`) ·
**64 PART divider comments (`part`, was 41)** · 145 constructs · 403 `<details>` / 403 typed ·
30 mysteries. Everything except `part` is unchanged from S83, which is how the generate is known
to have touched nothing but PART blocks.

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io). **Five banners moved
and two lessons' banner text changed** — worth an eyeball at **L12 §6–§7**, **L13 §6–§7 and §7–§9**,
**L14 §6–§7 and §7–§9**, plus **L04 PART 2** and **L05 PART 2 / PART 4**.

## DONE IN S84 — §6.8 rewritten, the PART divider is now generated

DJ ruled all three open questions in one line: *"Fix them all. Add to bible if needed"* /
*"Fix and have no drift"* / *"Yes"*. Full narrative is in LIVE.md and Bible §6.8; the short form:

1. **Five banners capped the wrong section** — L12 PART 3, L13 PART 3+PART 4, L14 PART 3+PART 4,
   each one section boundary early. `border-radius: 8px 8px 0 0` + `margin: 22px 0 0` FUSE the cap
   to the banner beneath, so L13 shipped a plum *"PART 4 — Challenges / Section 9"* welded onto §7's
   rose Calibration Ladder. Visible on every page load; invisible to all 26 gates, because every
   gate asked whether the banner existed and none asked what it sat on.
2. **Three content deviations** — L04 PART 2 title (logged S72, twelve sessions unfixed); L05 PART 2
   claiming *Sections 4–7*, which its own PART 3 also claims; L05 PART 4 claiming *Sections 9–10*
   where §10 is the untitled tail.
3. **Six encoding strata** and **51 divider comments in eight formats**, several naming the wrong
   PART (L02's read `PART 1: THE CHALLENGE` above a *Theory & Concepts* banner).
4. Resolved as **one GENERATE**, 64 canonical blocks, via new **`gen_part_banners.py` v1.0**.
5. **The Bible's own snippet was the stale one** — it specified a detached box against 64/64 live
   blocks. Live form is canon; the snippet was corrected.
6. **book_gates v1.15 gate 27**, control-run six ways, with byte-canonicity and placement asserted
   INDEPENDENTLY so an encoding drift can never hide a misplaced banner.

## OPEN — NEEDS A DJ RULING
1. **The weeding criterion** (old queue item 10) — §25.8 enforces the floor of 4; nothing says what
   makes a BC03 item weakest. L02 (7), L07 (6), L08 (6) are the candidates. **Blocks the weeding pass.**
2. **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge
   cards (nineteen sessions now) · spiral marking format review · DJ tier pass + rolling depth read
   (L14 first) · copyright line (RoboLore, work-for-hire) · bonus-challenge pill + livery when they
   move to §9.

## S85 QUEUE
1. **Unretired-ancestor gate** — sweep **h3–h4**, not just `<h3>`. Targets: L11 *Skills Checklist* ·
   L15/L16. *Now the biggest unexamined structural item, S84's having closed.*
2. **OTHER GATES WORTH WRITING** (carried): placeholder gate (`{[A-Z_]+}` in an attribute value) ·
   §4.2 coverage gate (every bonus/mystery `<h4>` carries `data-challenge`) — **load-bearing** since
   S83 established §20.1 and §20.2 only cover the leak surface as a pair · within-lesson promise
   gate (§25.10d) · §25.2 §-citation presence gate. *(Brain Check placement gate: DONE, gate 29.)*
3. **RULED S80, STILL PARKED — L09's three *Problem-Solving* extensions.** DJ: *"No keep them in
   que."* Recorded verbatim in `ZUMO_PARKED_EXIT_ITEMS.md`. Blocked on payload work, not authoring:
   every L09 construct links its own Maker payload kind, so each needs a new sabotaged 8-file payload
   in `newproject.html` (5.2 MB, edited by offset per §15) plus a byte-match gate run — and item 1
   ("add a `PAUSED` state") is an extension with nothing to sabotage. **Bonus challenges are the
   likelier correct target: same payload cost, no invented bug.**
4. **5 mysteries still untagged: L04.**
5. **Technical Skills vs §2 objectives — three lessons carry the debt.** L03 8 vs 11 · L04 13 vs 11 ·
   L05 7 vs 10. DJ ruled at S74 to reconcile at the final read-through.
6. Bonus placement is a 9/6 split. After §10: L02, L03, L06, L07, L10, L13, L14, L15, L16. In the
   §9 region: L04, L05, L08, L09, L11, L12. L01 has none.
7. **L13/L14 bonus banners carry a doubled 🕵️** (`&#128373;&#65039;` twice). One-line fix each.
8. Warm-ups L02–L16 + spiral aiming rule — still **L02-ONLY**, so L02 is the prototype.
9. L13/L15 have no exit blocks at all · within-lesson build-on mark · going_deeper footer contrast +
   duplicated hero title.
10. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen.
11. **Observation, not a finding — L08 `8.m3`'s prose hint names the deleted call outright**
    (*"the `calibrateLineSensors();` call was deleted from setup"*). Correctly typed `hint` (no
    `<pre>`, so S83's mystery clause does not fire), but §20.1 keeps `hint` and open prose reaches
    the tutor, so the tutor is told the answer. Not yet compared against L05–L07's hints, so NOT a
    defect. Read before ruling.
12. **L04's PART 2 title is now FIXED** (S72 item, closed S84) — remove from any stale list.

## STANDING QUEUE (carried; SUSPECTED until re-checked per §24.6c — including their SCOPE, rule 12)
L02 `2.t7` label collision (VERIFIED latent) · BENCH: compile-verify L07 finished + trapezoid · L08
Racing Line · L11 C4 double-TRIM · Q017 L09 six numbers · calibration-spin · gyro-bias · L02 §5
green-LED · Constrain RUN_MS · L15 C04–C07 no-template shape · L01 VS Code multi-root step ·
landing-page/book color mismatch · Maker batch (bulk DL · `?lesson=N` gate · C## labels · verify
`?kind=` starters) · TDP v3 (A5 Lab Log + printed 16 log prompts) · course docs (grid + syllabus) ·
"pick your robot" chooser · AI Tutor DISCOVERIES picker · QA_* sheets in images/glowbots · border
inset 10–18 vs 64 · Canvas reading quizzes (book first, then Canvas).

**Removed from the queue this session:** the §6.8 PART banner item (closed — premise false, four
real defects fixed) · the L04 PART 2 title item (fixed).

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page — **note:** it has a home now, as
L01's §4 Hardware, with Install moving down.

## PUSH LIST — S84 batch 2 (6 files, batch 1 already pushed)
`lessons/Lesson_03.html` (v03.14.3) · `ZUMO_SUPER_BIBLE.md` (v8.71) · `book_gates.py` (v1.16) ·
`PUSH_WORKFLOW.md` · `LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_S85_HANDOFF.md` (this file, replaced).
Maker untouched, no images, no payloads — **push order does not matter.**

**NO DELETION RIDES THIS PUSH.** The root already carries exactly one session handoff and this batch
replaces it in place. Gate 28 will confirm it after the push.

**After pushing:** fresh `git clone --depth 1` into a NEW directory, allow ~20–30 s for propagation,
grep a version out of it, and run `book_gates.py` (29/29) against the clone — gate 28 now
checks the handoff count for you.

---
*Written at S84 close, July 27 2026. The session's shape was that the queue's top item was
mis-scoped, and checking its premise — rather than working to it — was the whole job. Its claim was
that four lessons were missing a construct; the truth was that all sixteen had it, two of the four
"missing" ones had it in a format the instrument could not see, and five banners in three other
lessons were welded to the wrong section in a way that showed on every page load and that no gate
had ever been pointed at. The pattern is now twice-confirmed: at S82 the section anchor's PLACEMENT
was the unasserted half of a rule whose content was gated, and at S84 the PART banner's placement
was the unasserted half again. Ask what a component sits on, not only whether it exists. The most
instructive failure was smaller and closer to home: the control run that was supposed to prove the
new gate catches displacement passed cleanly, and the gate was innocent — the test had cut the block
at the wrong `</div>` and relocated a fragment. An assert that only proves something moved is not a
control.*

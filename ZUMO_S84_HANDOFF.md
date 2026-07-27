# ZUMO — S84 Handoff (written at S83 close, Jul 26 · paste at top of Session 84)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **26** must PASS (gate file **v1.14**). Then
   `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. `python3 lesson_inventory.py` (**v1.0.3**) — the structural census; then `--anomalies`.
   No exit code, no pass/fail by design (§24.6a) — it is there to be READ. **As of S83 close
   `--anomalies` is EMPTY for the first time.** That is a fact about the detector's current
   coverage, not a certificate on the book: it enumerates what it was built to enumerate.
6. LIVE.md wins over memory. §24.6c: control-run every audit grep AND assert the injection landed.
7. **Verify the push landed by grepping a version out of the clone, never by reading the commit
   message.** The label runs one ahead, reliably.
8. **LIVE.md has TWO version homes in its header** (`**Date:**` and `**Versions:**`).
9. **Regenerating LIVE.md means the BODY too.** Exactly one `## ` heading may read *THIS BATCH*.
   **Bound header rewrites to the first ten lines** — a per-session block further down carries its
   OWN historical `**Versions:**` line (S63's, now ~line 858). **And assert on the HEADING, not the
   substring**: S83's first regen attempt aborted because `count('SHIPPED THIS BATCH')` matched
   prose inside the S81 block. The assert firing before the write is the system working.
10. **A grep is a lead; a parser is the witness — and a parser built against observed practice
    inherits that practice as its definition.** S83 adds the sharper form: **a gate that has never
    fired is not evidence of a clean book until you have checked what population it is looking at.**
11. **Never `open(path,'w')` on a source file.** Build bytes, assert, write `.tmp`, `os.replace`.
12. **Read `PUSH_WORKFLOW.md` before writing any delivery instruction.** DJ pushes with **GitHub
    Desktop** — copy files into the clone, tick the changed files, commit, push. Git CLI commands are
    wrong for him. **Never hand DJ `git rm`.**

## LIVE STATE at S83 close — VERIFIED, gates 26/26 PASS
L01 v03.10.3 · L02 v03.0.2 · L03 v03.14.1 · L04 v04.7.1 · L05 v04.9.3 · **L06 v04.12.4** ·
L07 v04.8.3 · L08 v04.7.4 · L09 v05.5.2 · L10 v02.5.3 · L11 v02.7.3 · L12 v01.7.4 ·
L13 v02.6.3 · L14 v02.8.3 · L15 v02.6.3 · L16 v02.5.3 — **only L06 changed this session.**
Bible **v8.69** · Maker v2.45.1 · book_gates **v1.14 (26 gates)** · **lesson_inventory v1.0.3** ·
Gate v1.6 · Harness v3.0 · pill_sweep v1.0

**Structural census:** 1,025 headings · 174 section anchors · 174 section fences (`sfnc`) ·
41 PART banner comments (`part`) · 145 constructs · 403 `<details>` / 403 typed · 30 mysteries.
Brain Check family: nine of sixteen (L01–L09), column byte-identical, 5,639 chars / md5 `070806a6`.

**NOT verified: the rendered Pages site** (sandbox blocks weymuth.github.io). **L06's fix DOES change
rendering** — BC01 no longer sits inside §5's green box. Worth an eyeball at L06 §5/§6.

## DONE IN S83

### 1. L06 brain-check-01 — the standing lead, closed (DJ's first item)
BC01 was the **last of 49 direct children** of §5's `border: 2px solid #3a7d5c` content panel,
sitting *after* §5's own `↑ Back to top` link, with §6's banner the next element once the panel
closed. So the question the queue posed — does §5's panel legitimately close later — answered
itself: **no.** §5's content ends at its back-to-top link; the `</div>` sat one element late.
Confirmed against four conforming lessons (L05/L07/L08/L09), all identical in shape: panel ends
with back-to-top, BC01 is the sibling between panel and §6 banner. Reading order was already
correct, so the repair was **relocating a single `</div>`**, reproducing L05's byte-pattern.
L06 **v04.12.3 → v04.12.4**, minor, visible banner unchanged per §5b.

**Worth carrying forward:** the first assert *failed* and the assert was wrong, not the edit —
strict `get_text('\n')` equality tripped on two blank separator lines that move when nesting
changes. Diffed before overriding, per the S82 no-op lesson. Normalized text and the non-empty
text-line sequence were both identical.

### 2. §20.1 — both logged gate defects were real, and one had manufactured a queue item
**Bible §20.1(5), v8.69. book_gates v1.13 → v1.14.**

The per-card bounding used `rfind('<div')`. That is correct for an element-bounded
`<div data-challenge>` **by accident**, and wrong for every heading-bounded `<h4 data-challenge>`,
which inherited its whole enclosing panel. Not argued — demonstrated: **one** injected block in L07
`7.m3` came back as **five findings**, `7.m1` through `7.m5`. Four false; the true one
indistinguishable from them.

Fixed by **importing the span from `lesson_inventory.py`** rather than writing a third regex, so the
two tools share one definition and cannot drift apart. The port is verified by reproducing the
read-verified **5/8/2** code-line counts for L09 `9.m3`–`9.m5` against the old gate's **3/8/17**.

**Second defect, same pass:** `data-kind="mystery"` now has **no line threshold**. §25.10g already
makes a mystery's bug+fix reveal a `solution`, and its planted snippets run 1–2 lines — so the
≥3-statement-line floor was **the only reason L08 passed this gate for eight sessions** (S80).
A threshold is not an exemption.

**Control-run five ways**, every injection asserted landed before the verdict was read: untouched
**PASS** · 4-line block in a heading-bounded mystery hint **FAILED naming `7.m3` only** where the old
gate named five · `8.m1` retyped `solution`→`hint` **FAILED where the old gate PASSED** · the
original S79 shape re-injected into element-bounded card `1.11` **FAILED** · a deliberately broken
port tripped the new **COVERAGE assert** (added because a gate whose population silently empties is
an ungated rule).

### 3. §24.6c CORRECTION — the L02 `2.t4` item was the bug's own output
`2.t4` is a `<strong>` spanning **one line**, holding **zero `<details>`**. The old window opened its
"card" four lines early and ran **seventeen lines past its end** to swallow a §6 Step-4 build-along
`check` reveal that belongs to no construct at all. The code is real and the reveal is real; neither
was ever `2.t4`'s, and neither was ever a challenge answer. S81 was right that `2.t4` holds no
reveal — the reason is now known. **Closed. No ruling was needed, only a working parser.**

### 4. The census the correct bounding finally made possible
All sixteen lessons: **33 kept (non-`solution`) reveals hold `<pre>`, and all 33 sit OUTSIDE every
construct** — 31 §6 `check` blocks (L02 8 · L03 8 · L04 4 · L05 2 · L06 9), one L02 §8
`troubleshoot`, one L10 §6 `hint` (*"Stuck? The fix, spelled out"*) resolving a red build **the
lesson instructed the student to plant**. **Nothing in §9, nothing past §10. Zero leaks.** These are
teaching content and the tutor should have them, per DJ's S79 ruling that what we hide is challenge
answers. Mysteries: all 30 checked, zero with code in a kept reveal.

**The flank this leaves, recorded not fixed:** an **untagged** challenge hiding its answer in a
`hint` is invisible to §20.1, because the gate only walks construct spans. §20.2's marker gate is
the other half of the guarantee; the two only work as a pair.

### 5. lesson_inventory v1.0.2 → v1.0.3, and two LIVE.md defects
The tool's §6.8a source comment still read *"only 6 lessons carry any"* — stale **twice over**: that
figure was the matcher artifact §6.8a was written to kill (ten carried them), and since S82 all
sixteen carry 174. Data right, sentence outlived it — the same §24.6c shape as the S81 column label.

**LIVE.md carried the S82 narrative TWICE** — once as *THIS BATCH* (complete, with the S82b items
9–10) and once as *PREVIOUSLY* (the same text **minus** those items, i.e. a stale copy). Removed.

## OPEN — NEEDS A DJ RULING
1. **Brain Check placement has no rule** (surfaced by fixing L06). The family norm is BC01 directly
   under `<body>`, 8 of 9 — an observed practice with zero canon behind it, which is exactly the
   §6.8a shape. `lesson_inventory` can only report it as a *lead* because there is nothing to check
   it against. **A placement gate is the obvious follow-on and wants a ruling first.**
2. **The weeding criterion** (old queue item 10) — §25.8 enforces the floor of 4; nothing says what
   makes a BC03 item weakest. L02 (7), L07 (6), L08 (6) are the candidates. **Blocks the weeding pass.**
3. **Carried:** `<title>`/strip tooltips vs hero title (L01/L02/L03/L08/L15) · L16 zero challenge
   cards (eighteen sessions now) · spiral marking format review · DJ tier pass + rolling depth read
   (L14 first) · copyright line (RoboLore, work-for-hire) · bonus-challenge pill + livery when they
   move to §9.

## S84 QUEUE
1. **L02, L06, L15, L16 carry ZERO PART banner comments** where §6.8 canonizes four. Surfaced by the
   `part` column at S82, untouched since. **The visible banners have NOT been checked** — this may be
   missing comments only, or missing banners. Read before scoping. A **§6.8 PART banner gate** is the
   obvious follow-on to gate 26 and would settle it. *This is the biggest unexamined structural item.*
2. **Unretired-ancestor gate** — sweep **h3–h4**, not just `<h3>`. Targets: L11 *Skills Checklist* ·
   L15/L16.
3. **OTHER GATES WORTH WRITING** (carried): placeholder gate (`{[A-Z_]+}` in an attribute value) ·
   §4.2 coverage gate (every bonus/mystery `<h4>` carries `data-challenge`) — **note this one is now
   load-bearing**, since S83 established §20.1 and §20.2 only cover the leak surface as a pair ·
   within-lesson promise gate (§25.10d) · §25.2 §-citation presence gate · **§6.8 PART banner gate**.
4. **RULED S80, STILL PARKED — L09's three *Problem-Solving* extensions.** DJ: *"No keep them in
   que."* Recorded verbatim in `ZUMO_PARKED_EXIT_ITEMS.md`. Blocked on payload work, not authoring:
   every L09 construct links its own Maker payload kind, so each needs a new sabotaged 8-file payload
   in `newproject.html` (5.2 MB, edited by offset per §15) plus a byte-match gate run — and item 1
   ("add a `PAUSED` state") is an extension with nothing to sabotage. **Bonus challenges are the
   likelier correct target: same payload cost, no invented bug.**
5. **5 mysteries still untagged: L04.**
6. **Technical Skills vs §2 objectives — three lessons carry the debt.** L03 8 vs 11 · L04 13 vs 11 ·
   L05 7 vs 10. DJ ruled at S74 to reconcile at the final read-through.
7. Bonus placement is a 9/6 split. After §10: L02, L03, L06, L07, L10, L13, L14, L15, L16. In the
   §9 region: L04, L05, L08, L09, L11, L12. L01 has none.
8. **L13/L14 bonus banners carry a doubled 🕵️** (`&#128373;&#65039;` twice). One-line fix each.
9. **L04's PART 2** is titled "Hands-On Setup & Programming" where the other fifteen say "Hardware
   & Code" — found S72, one-line fix, still not done.
10. Warm-ups L02–L16 + spiral aiming rule — still **L02-ONLY**, so L02 is the prototype.
11. L13/L15 have no exit blocks at all · within-lesson build-on mark · going_deeper footer contrast +
    duplicated hero title.
12. Re-verify §15.2's "if Section 6 has N steps" against `newproject.html` for all sixteen.
13. **Observation, not a finding — L08 `8.m3`'s prose hint names the deleted call outright**
    (*"the `calibrateLineSensors();` call was deleted from setup"*). Correctly typed `hint` (no
    `<pre>`, so S83's new mystery clause does not fire), but §20.1 keeps `hint` and open prose reaches
    the tutor, so the tutor is told the answer. Not yet compared against L05–L07's hints, so NOT a
    defect. Read before ruling.

## STANDING QUEUE (carried; SUSPECTED until re-checked per §24.6c)
L02 `2.t7` label collision (VERIFIED latent) · BENCH: compile-verify L07 finished + trapezoid · L08
Racing Line · L11 C4 double-TRIM · Q017 L09 six numbers · calibration-spin · gyro-bias · L02 §5
green-LED · Constrain RUN_MS · L15 C04–C07 no-template shape · L01 VS Code multi-root step ·
landing-page/book color mismatch · Maker batch (bulk DL · `?lesson=N` gate · C## labels · verify
`?kind=` starters) · TDP v3 (A5 Lab Log + printed 16 log prompts) · course docs (grid + syllabus) ·
"pick your robot" chooser · AI Tutor DISCOVERIES picker · QA_* sheets in images/glowbots · border
inset 10–18 vs 64 · Canvas reading quizzes (book first, then Canvas).

**Removed from the queue this session:** the §20.1 per-card bounding item (fixed) · the
`data-kind="mystery"` gate item (fixed) · the L02 `2.t4` item (closed as an artifact) · the L06 BC01
lead (fixed).

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page — **note:** it has a home now, as
L01's §4 Hardware, with Install moving down.

## PUSH LIST — S83 (five files)
`lessons/Lesson_06.html` (v04.12.4) · `ZUMO_SUPER_BIBLE.md` (v8.69) · `book_gates.py` (v1.14) ·
`lesson_inventory.py` (v1.0.3) · `LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_S84_HANDOFF.md`.
Maker untouched, no images, no payloads — **push order does not matter.**

**⚠️ ONE DELETION RIDES THIS PUSH — `ZUMO_S83_HANDOFF.md`. A zip cannot delete (§12.2).**
In GitHub Desktop a deleted file appears in the **Changes** list as its own entry with its own
**checkbox**. **If that box is not ticked the deletion stays out of the commit** while every other
change goes up — which is exactly what happened at `fb70426`. Delete `ZUMO_S83_HANDOFF.md` locally,
then confirm its checkbox is ticked before committing.

**VERIFY A DELETION EXACTLY LIKE A VERSION — clone fresh and list the root.** Never trust the local
working tree, and never trust that a deletion rode along with a file-overwrite batch. (This worked
at S83 open: the root carried exactly one session handoff, so S82's deletion did land.)

After this push the root should carry exactly ONE session handoff (`ZUMO_S84_HANDOFF.md`). Note
`ZUMO_LEARNMODE_L04_HANDOFF.md` also matches "HANDOFF" but is a §19 learner-mode record, **not** a
session handoff — leave it alone.

**After pushing:** fresh `git clone --depth 1` into a NEW directory, allow ~20–30 s for propagation,
grep a version out of it, and run `book_gates.py` (26/26) against the clone.

---
*Written at S83 close, July 26 2026. The session's shape was that two defects logged three sessions
ago against a gate that kept passing turned out to be the reason it kept passing. Neither was a rule
problem; both were the instrument pointing slightly off — a `rfind` window standing in for a parse
tree, and a line threshold standing in for a rule that already had no threshold. The most useful
thing the repair produced was not a defect but a retraction: the queue item about L02 `2.t4` had been
generated by the very bug being fixed, and it evaporated the moment the span was computed correctly.
Then the corrected gate went looking and found 33 reveals holding code that it had never been able
to see — and all 33 turned out to be right, which is its own kind of result. What is left is the
flank the census exposed rather than closed: this gate can only see inside tagged constructs, so
§20.2's marker gate is now load-bearing in a way nobody had written down.*

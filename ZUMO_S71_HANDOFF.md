# ZUMO — S71 Handoff (written at S70 close, Jul 25 · paste at top of Session 71)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. `python3 book_gates.py` — all **21** must PASS. Then `python3 pill_sweep.py --audit lessons/Lesson_*.html`.
5. LIVE.md wins over memory. Grep the actual file, never trust a pasted version number.
6. **§24.6c** — control-run every audit grep before its number becomes a finding; report VERIFIED or SUSPECTED.
   S70 addendum: **that applies to the control run itself.** One S70 injection test passed because it injected a
   string that did not exist in the file (`in order?` vs the real `in order.`). Assert the injection landed.

## LIVE STATE at S70 close — **PUSHED and byte-verified**, final commit `892e29a` "Session 71 final"
L01 **v03.8.1** · L02 v02.15.2 · L03 v03.13.2 · L04 v04.6.2 · L05 v04.8.2 · L06 v04.11.2 · L07 v04.7.2 ·
L08 v04.6.2 · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 · L13 v02.6.2 · L14 v02.8.2 ·
L15 v02.6.2 · L16 v02.5.2
Bible **v8.54** · Maker **v2.45.1** · Gate v1.6 · Harness v3.0 · pill_sweep v1.0 ·
**book_gates v1.5 (21 gates)** · going_deeper **v01.1.0** · timer **v1.3.0** · tutor **v1.0.0** · index **v1.3.0**
NOT verified: the rendered Pages site (sandbox allowlist blocks weymuth.github.io). DJ should eyeball the new
DEEPER pill wrap on mobile and the going_deeper hero/footer on its dark background.

---

## DONE IN S70

1. **Bible §25 — THE EXIT-REGION CONSTRUCTS, THE READING QUIZ & PAGE CANON** (new, nine subsections).
   Four constructs, recall-vs-apply split, reading-quiz design, warm-up/spiral aiming, page canon, caps,
   and **§25.9 STILL OPEN** written so the section cannot read as finished when it is not.
2. **§5b rewritten** — hidden build banner supersedes the v8.44 "both visible homes" rule. Gate needed no
   edit: it greps raw source, and raw source includes comments.
3. **L01 v03.8.1 — the reference lesson.** Mental (5, § -cited, before hands-on) · Knowledge Check (4, §10) ·
   Reflection (3, no reveal) · Technical Skills and Engineer's Log untouched · 5 banked `QUIZVARIANT` stems.
4. **All 17 pages structurally identical** — seven footer shapes → one, hidden banner everywhere,
   `going_deeper.html` brought onto the shared hero/footer. Skeleton hashes: hero `4fdedafb`, footer `aff5311e`.
5. **DEEPER pill** in the §6.5a strip, all 16 — Going Deeper was reachable from only 7 of 16 lessons.
6. **book_gates v1.3 → v1.4** — §25.6 and §25.2, control-run in both directions (four separate injections).

## LATE-S70 ADDENDUM (after the first handoff draft — the push-verification arc)

7. **Two pushes landed the right bytes in the WRONG FOLDER** — `going_deeper.html` into `lessons/` (23 links
   kept serving the stale root copy) and `tutor.html` to root (the live tutor stayed unversioned). Both looked
   like clean pushes; no contents gate could see them. **book_gates v1.4 → v1.5** adds
   `§12/§23 site layout` (exact set of 21 pages + paths — stray, missing, or misplaced all FAIL) and
   `§5b web tools carry an in-file version line`. Control-run three ways, incl. a reproduction of the
   Going Deeper incident (fails as STRAY **and** MISSING).
8. **All four web tools now open with a canonical version line** — timer v1.3.0 · Maker v2.45.1 · tutor v1.0.0 ·
   index v1.3.0 — baselines labelled as baselines in each file's own header. Found en route: the Maker's
   changelog OPENS with v2.18 against a live v2.45 (the v3.0 ghost), and Bible §5b's web-tool sentence claimed
   "Maker v1.3". §5b rewritten (v8.54): never record a tool version in Bible prose — grep the file.
9. **§25.6a** — the tool pages are NOT chapters; they owe a version line, nothing else. `index.html` is the one
   credits exception (public front door): `© 2026 RoboLore · Written and compiled by DJ Weymuth and Claude AI`.
10. `.gitignore` added (DJ) — the stray-`.DS_Store` housekeeping item is CLOSED.

## S70 PROCESS NOTES
- The footer roll needed **three** locator corrections (nested `</div>` matching, then `<footer>` tags never
  scanned). The first two dry runs looked plausible and were wrong; only dumping the captured text per lesson
  caught it. §24.6c applies to scripts, not just greps.
- Three title sources are live and disagree. The hero is canonical for footers; `<title>` and the strip are untouched.

## OPEN — NEEDS A DJ RULING
- **`<title>` tags and §6.5a strip tooltips vs the hero title** — disagree on L01, L02, L03, L08, L15.
- **L16 zero challenge cards** — flagged five sessions now, still unruled.
- **Spiral marking format review** — S67 batch shipped under an Inferred ruling, never eyeballed.
- **DJ's own tier pass** + **rolling depth read (L14 first)**.
- **Copyright line** — `© 2026 RoboLore` is Inferred; the work-for-hire question routes through the Mercersburg
  faculty handbook, and matters before the parked ebook item moves. One command to change across 17 files.

## S71 QUEUE — the §25 rollout, in order
1. **L02 and L03** get the four exit blocks (DJ: L01→L02→L03, no jumping around). Both carry retired names, so
   the §25.2 gate will bind them the moment they convert.
2. **Warm-ups L02–L16** + the spiral aiming rule (prev lesson · 3–6 back · under-cited set).
3. **Bonus challenges §10 → §9** (12, in L02/L03).
4. **L13 and L15** — still no exit written-response block at all.
5. **§2 objectives rewritten from the Technical Skills checklists.**
6. **Separate mark for within-lesson build-ons**, so 🔁 means cross-lesson only (count is ~18% inflated).
7. `going_deeper` footer contrast (#666 on #0f1117 ≈ 3.3:1) and its duplicated hero title.

## STANDING QUEUE (carried; SUSPECTED until re-checked per §24.6c)
- **L02 `2.t7` label collision (VERIFIED, latent)** — if that card ever gets a timer its label collides with `2.t8`.
- **BENCH:** compile-verify L07 finished + trapezoid · L08 + Racing Line · L11 C4 double-TRIM mirror-drift ·
  Q017 L09 six numbers · calibration-spin stopwatch · gyro-bias · L02 §5 green-LED · Constrain RUN_MS.
- **L15 C04–C07 no-template shape** (logged deliberate) · **L01 VS Code multi-root step** ·
  **Landing-page/book color mismatch** · **Maker batch** (bulk DL · `?lesson=N` gate · C## labels ·
  verify `?kind=` starters) · **TDP v3** (A5 Lab Log **+ print the 16 Engineer's Log prompts with blanks**, per S70
  notebook discussion) · **course docs** (grid + syllabus) · **"pick your robot" chooser** ·
  **AI Tutor DISCOVERIES picker** · Housekeeping: `QA_*` sheets in images/glowbots · border inset 10–18px vs 64px ·
  stray `.DS_Store` committed.
- **Canvas reading quizzes** — 48–80 rehearsal/variant pairs. Book first, Canvas after (DJ ruling). Five stems
  already banked in L01 as `QUIZVARIANT` comments; harvest by script when the book is done.

## PARKED (don't reopen unprompted)
Solution-disclosure · monetization/ebook · "Know Your Zumo" page.

---
*Written at S70 close, Jul 25 2026. The book gained a canon for its exit region, one reference lesson, uniform
furniture across seventeen pages, and two gates. The session's most useful finding was that six names had been
doing one job for months — and its most instructive mistake was a control run that verified nothing.*

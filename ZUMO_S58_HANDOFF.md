# ZUMO — S58 Handoff (written at S57 close, Jul 20 · paste at top of Session 58)

**S57 was a used-before-taught session.** Both construct sweeps are CLOSED. Everything below is
pushed and live, verified by fresh clone, and the close-out audit was green across all 16 lessons.

## SESSION OPEN — auto-run, no upload needed (repo is source of truth)
```
git clone --depth 1 https://github.com/Weymuth/zumo.git && cd zumo
grep -o "Lesson version: v[0-9.]*" lessons/Lesson_06.html
grep -oE "Project Maker v2\.[0-9]+" newproject.html | sort -V -u | tail -1
grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md
grep -oE "GATE \(Bible §11\) — v1\.[0-9]+" gate_payload_match.py
```
⚠️ **Shallow-clone cache lag is REAL** — hit it twice in S57. For ~1–2 min after a push the clone can
serve the PRIOR commit. If a version looks stale, `sleep 30` and re-clone before concluding anything.
`sort -V` (not `sort -u`) for the Maker version — alphabetical returns v2.9 over v2.39.

**Expected at open:** commit `5f69546` · Bible **v8.36.1** · Maker **v2.39** · Gate **v1.6** · Harness v3.0.

### Running the gate (stable filenames need symlinks or every lesson silently skips)
```
mkdir -p /tmp/gw
for i in $(seq -w 1 16); do ln -sf "$PWD/lessons/Lesson_${i}.html" /tmp/gw/Lesson_${i}_Topic_.html; done
python3 gate_payload_match.py newproject.html /tmp/gw/Lesson_*.html
```
Expected: `GATE: PASS` with `ADVISORY (635) … L1=635`. Advisory is NOT a failure (Bible §11, boxed
challenge-header lines, pinned by md5 in BOXED_FP — never remove that pin).

## LIVE STATE at S57 close (all grepped from files)
L01 v03.4.0 · L02 v02.4.0 · L03 v03.6.0 · L04 v04.1.2 · L05 v04.2.2 · L06 v04.7.0 · L07 v04.3.10 ·
L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 ·
L15 v02.2.3 · L16 v02.2.3 · Bible v8.36.1 · Maker v2.39 · Gate v1.6 · Harness v3.0.

## S58 — FIRST JOB: the deferred Bible update
Write ONE §11 entry: **AUDIT FALSE-POSITIVE DISCIPLINE.** S57 produced FIVE prose-keyword false
positives (three phantom "gaps," two false "taught" flags, one false LIVE.md mismatch). The rule:
1. **Separate code from prose before counting** — strip to `<pre>` for usage, strip tags for teaching;
   never count a token that spans both (e.g. `abs(` inside a `while` is a use, not a lesson).
2. **A regex reports CANDIDATES, never verdicts** — for any "is X taught?" claim, surface the candidate
   heading and require a human read. A keyword near a heading is a lead, not proof.
3. **Verify every audit finding against RENDERED text before acting** — this session's phantoms
   (`milliseconds`→millis, a stray `?:`→ternary, a `v04.6.0` inside a changelog phrase→version mismatch)
   all evaporated on a read. Same family as S56's unescaped-`<` false alarm and the L04 image-index phantom.
   A smarter script narrows the field; only a human read closes it.
Bump Bible v8.36.1 → v8.36.2 (minor — new §11 sub-entry, no rule reversal). Then regenerate LIVE.md.

## WHAT S57 SHIPPED (all live, do NOT redo)
- **L16 EEPROM** — §4.3 "never touched it" was falsified by S56's L01 name-reader; corrected + address
  map (0–511 L16, 512–543 name, 544–1023 free). Bible §16.9 (the map) + §11 ("never…" claims are deps).
- **Construct sweep 1 (control-flow/operators) — CLOSED:** `if` (L02 §3.2c → L03 §5.5 → L04 §8A spiral) ·
  `for` (L04 §8A.6/8A.7) · `&&`/`||`/`!` (L02 §3.2d) · `while` (L06 §5.3, L05 pointer repaired) ·
  `=` vs `==` (L03 §5.5) · increments (L03 §5.6) · `switch` (L05 §5.13 pointer → L09).
- **Construct sweep 2 (library vocab) — real gaps closed:** `abs()` + ternary `?:` (L06 §5.4, Step 7
  aside repointed). Verified-clean: `constrain()` L03 §3.9, `enum` L09, `array` L03.
- **L04 misc:** `setLayout21x8` reframed as a stated 8×2 choice (NOT a defect) · index-order repair ·
  `L04_LEARNMODE_LOG.md` annotated (§5.13→§5.15 fix; C03 ruling = option e, stays HARD, unblocked).
- **Bible §11 rule that drove it all:** v8.36.1 — *§8A must cover what §9 requires* (using a construct
  in given code is not teaching it; fix pattern = teach at first contact, demote later tutorial to spiral rung).

## STILL QUEUED (minor / non-blocking)
- **`millis()` taught-note** — has a real QR row (documented, thin), never taught as a concept before
  L14/L15 timing. Promote only if a challenge is found requiring millis-based timing to be WRITTEN.
- **`map()` note** — one use, L08 given-code (`map(pos,0,4000,0,20)`), taught nowhere. Lowest priority;
  one L08 note closes it. Not a student-write.
- **`.DS_Store`** still committed — `git rm .DS_Store` + a `.gitignore` line. 30 seconds, not urgent.
- L03_C05 Variable Speed learner mode · L04 C03 learner mode (**unblocked** — resume against new §8A.6/8A.7;
  it also tests whether the fix worked) · L04 C04/C05 walkthroughs · "out-of-range values don't error" ·
  C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate ·
  C## labels) · L01 VS Code multi-root step.

## ⚠️ THE ONE REAL DEADLINE — AI TUTOR
Students get API access. The syllabus has **no entry** for it. `tutor.html` is stale with no L12+ content.
**Term starts Sept 8.** This is the biggest open item in the whole queue and the natural front task once
the Bible update is in. The S57 learner-mode walkthroughs (esp. L03/L04 §8A finds) are the raw material.

## BENCH (need robot; DJ was without a line surface / robot recently)
C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

## PARKED (do not reopen unprompted)
solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus ·
TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

## Process notes worth keeping
- **Write-order rule held all session:** every batch = fix → gate → diff-audit → structure/img check →
  regenerate LIVE.md LAST → present_files. Seven batches, all green.
- **Bounded-scope `count==1` asserts on every edit**, visible banners asserted (unchanged on minor bumps,
  moved on moderate) per §5b. No over-matches this session.
- **The prose-keyword-grep lesson is the headline for S58's Bible entry** — five false positives, all caught
  by reading. The discipline earned its keep; codify it.

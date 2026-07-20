# ZUMO — S57 Handoff (written at S56 close, Jul 19 · paste at top of Session 57)

**S56 did the one job: L01 §9 is built and the payload gate is GREEN.** The fix was DJ's rule,
not a workaround — *if it's in the payload, it goes in the book.* Zero exemptions were added.

---

## SESSION OPEN — run the drift check FIRST (Bible §12.6-C)

```
git clone --depth 1 https://github.com/Weymuth/zumo.git
cd zumo
grep -o "Lesson version: v[0-9.]*" lessons/Lesson_01.html
grep -oE "Project Maker v2\.[0-9]+" newproject.html | sort -V -u | tail -1
grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md
grep -oE "GATE \(Bible §11\) — v1\.[0-9]+" gate_payload_match.py
```

⚠️ **`sort -u` is WRONG for the Maker version** — alphabetical sort returns `v2.9` over `v2.39`.
Use `sort -V` as above, or the badge-anchored grep.

**Expected if the S56 batch was pushed:** L01 `v03.4.0` · Maker `v2.39` · Bible **`v8.35`** · Gate **v1.6**.
**If Bible reads v8.34 or gate reads v1.4, the S56 push did not land — say so in your first message.**

**The files win over LIVE.md, always.** If they disagree, ask DJ for a newer LIVE.md before regenerating.

### Running the gate — READ THIS, it is not obvious
The gate's filename regex needs `Lesson_NN_Topic_`, but the repo publishes stable `Lesson_NN.html`.
Symlink into a scratch dir first, or every lesson silently skips:

```
mkdir -p /tmp/gw
for i in $(seq -w 1 16); do ln -sf "$PWD/lessons/Lesson_${i}.html" /tmp/gw/Lesson_${i}_Topic_.html; done
python3 gate_payload_match.py newproject.html /tmp/gw/Lesson_*.html
```

**Expected output: `GATE: PASS` with `ADVISORY (635) … L1=635`.** Advisory is not a failure — see below.

---

## WHAT CHANGED IN S56

| File | Version | What |
|---|---|---|
| `lessons/Lesson_01.html` | v03.3.0 → **v03.4.0** | §9 shared listing + 11 cards each quoting their own target line |
| `newproject.html` | v2.38 → **v2.39** | `PAYLOADS["1"]["c01"]` markers only |
| `ZUMO_SUPER_BIBLE.md` | v8.34 → **v8.35** | three new §11 entries |
| `gate_payload_match.py` | v1.4 → **v1.6** | advisory boxed headers + md5 fingerprints |
| `L01_CHALLENGES/C01_Hello_World/src/main.cpp` | — | markers made symmetric |

**Census: EXECUTABLE CODE 132 → 0.** The EEPROM name-reader is now published in L01 §9.

---

## THE TWO GATE CONCEPTS YOU MUST NOT UNDO

**1. ADVISORY ≠ ignored.** Boxed instruction headers (`// ┌─┐ … // └─┘`) stay in the challenge
files on purpose — students code in one window and read in another, and a step you remove is a
step they'll actually take (DJ ruling S56). Those lines are *not required to appear in the book*,
so they report under ADVISORY instead of failing. **But every one is pinned by line count + md5
in `BOXED_FP`.** Edit a header and the gate fails loudly, naming the challenge. That pin is the
only thing standing between the files and silent drift — **do not remove it.**

**2. Never add an exemption to make the gate green.** An unmatched line means the book is missing
something. Add it to the book. Executable code is *never* exempt under any framing. S55 lost four
takes to this exact error.

To change a boxed header on purpose:
```
python3 gate_payload_match.py newproject.html /tmp/gw/Lesson_*.html --update-fp
```
…then paste the printed manifest into `BOXED_FP`. Deliberate bump, not a silent one.

---

## S57 — PICK ONE

**Front-runner: the L16 EEPROM consequence.** L16 says the book *"has never touched"* EEPROM.
As of L01 v03.4.0 that is **false** — the name-reader reads addr 512 with magic `0x5A`. This is a
direct, known consequence of S56's work and it makes a live lesson wrong. Also wants the 512
address-map note so L16's own EEPROM use can't collide with the name. Small, bounded, and it
closes a defect this session created.

**Other candidates:** L04 `setLayout21x8` (the only lesson of 16 missing it) · L04 C03 `for`
primer + `L04_LEARNMODE_LOG.md` correction · L03_C05 Variable Speed learner mode (paused S45;
starter saved; the three edits are array+index in CONFIG, `TEST_SPEEDS[speedIndex]` in
`runMotorTest`, `speedIndex=(speedIndex+1)%NUM_SPEEDS` in the B handler).

---

## STANDING QUEUE

C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N`
soft gate · C## folder labels) · L01 VS Code multi-root + "Pick a folder" step · the 6 syntax-gap
prose candidates + "out-of-range values don't error."

**DONE, remove from queue:** *"extend the gate to cover L01 challenge bodies"* — satisfied by v1.6.

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid +
syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, the syllabus has no entry for it, `tutor.html` is stale
with no L12+ content. **Term starts Sept 8.**

---

## ONE CORRECTION TO CARRY FORWARD

Mid-S56 an unescaped-`<` corruption was reported in C03's reveal-solution block. **It was a false
alarm** — the inspection regex was stripping `&lt;` as if it were a tag. All escaping in L01 is
correct and nothing was changed for it. When scanning `<pre>` bodies for corruption, unescape
entities *before* judging, or you'll invent defects that aren't there.

---
*Written S56, July 19 2026. Batch staged, not pushed.*

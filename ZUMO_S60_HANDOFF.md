# ZUMO — S60 Handoff (written at S59 close, Jul 20 · paste at top of Session 60)

**S59 launched Project B — challenge-card standardization.** Three lessons converted to the canonical Goal→Logic→Template card, and the spec is now Bible canon (§6.12a). Everything below is pushed and verified by fresh clone.

## SESSION OPEN — auto-run, no upload needed (repo is source of truth)
```
git clone --depth 1 https://github.com/Weymuth/zumo.git && cd zumo
grep -o "Lesson version: v[0-9.]*" lessons/Lesson_06.html
grep -oE "Project Maker v2\.[0-9]+" newproject.html | sort -V -u | tail -1
grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md
grep -oE "GATE \(Bible §11\) — v1\.[0-9]+" gate_payload_match.py
```
⚠️ Shallow-clone cache lag is real (~1–2 min after a push serves the prior commit). `sleep 40` and re-clone before concluding a push didn't land. `sort -V` for the Maker version.

**Expected at open:** commit past `ac3d52a` · Bible **v8.38** · Maker v2.39 · Gate v1.6 · Harness v3.0.

## LIVE STATE at S59 close (grepped from files)
L01 v03.4.3 · L02 v02.4.3 · L03 v03.6.3 · L04 v04.1.5 · L05 **v04.3.0** · L06 v04.7.3 · L07 v04.3.13 · L08 v04.1.10 · L09 v05.0.12 · L10 v02.1.15 · L11 v02.2.5 · L12 **v01.3.0** · L13 **v02.3.0** · L14 v02.4.5 · L15 v02.2.6 · L16 v02.2.5 · Bible v8.38 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## 🎯 WHAT S59 SHIPPED (all live)

1. **Project B pilot + first two conversions** — L05 (5 challenges), L12 (3), L13 (3) reshaped to the canonical card: Work-in bar → 🎯 Goal → 🧠 Logic (pseudocode, absorbs the hint) → 🧩 Template (blanks fill exactly to the solution) → solution. Payload gate PASS full book. L13 renumbered "Challenge 9.x" → sequential "Challenge N" (+2 cross-refs); first use of the TOUGH tier.
2. **Bible v8.37 → v8.38 — §6.12a THE THREE-PANEL CARD + WHEN IT APPLIES (Project B canon).** The rollout standard: shell mandatory on every card; inner format fits the challenge type (algorithmic → 3 panels; guided-edit/debug/observation → prose, L01 the reference, left as-is). Open cases resolved provisionally pending DJ's runthrough. Also corrected §6.12's stale "pill sweep queued" note.
3. **Pill census (from files, not memory)** — 73 pills book-wide, all conform to §6.12; zero retired EXPERT/COMPETITION. The sweep is complete; the old "4 EXPERT unswept" memory was stale.

**RULE DJ SET S59:** don't rely on memory for anything that could be recorded in the Bible — grep the Bible/files. (The pill "unresolved" and "EXPERT unswept" both came from stale memory and were both wrong.)

---

## S60 — FRONT TASKS

1. **Project B — continue the rollout against §6.12a.** Order (bespoke per lesson — each is a different starting format):
   - **L14 next** (verify format first — likely "Challenge 9.x" bare-heading like L13).
   - Then **L15** (7, from-scratch), **L11** (3 challenges + 4 mysteries — mysteries are observation, keep as prose), **L08/L09** (already Style-A shell; add the Template panel + show solution, per §6.12a open-case), **L10** (green-callout → purple-card conversion + fix nothing on pills, ADVANCED already correct).
   - **L02/L03/L04** = per-challenge hybrid (some algorithmic → panels, some guided-edit → prose) + shell repair (L02 has no `#fffbe6` Work-in bar). L03/L04 are mid learner-mode — coordinate.
   - **L01, L06, L07** = done (L01 guided-edit as-is; L06/L07 already canonical).
2. **⚠️ Maker follow-ups (from S59 — one is a LIVE student-visible mismatch):**
   - **L13:** cards now say "Challenge 1/2/3" but the revealed solution comments still read `// CHALLENGE 9.x` (kept to byte-match the Maker payloads). Sync BOTH the lesson solutions AND the `c1_sweep`/`c2_report`/`c3_rowzero` payloads to `1/2/3` (coordinated lesson+Maker edit; re-run the gate).
   - **L12:** challenges have no starter payloads — Work-in bars name the build only. Add starter payloads (folds into the parked Maker batch).

## STANDING QUEUE (carried)
Syllabus/Canvas entry for the AI Tutor · discoveries in tutor picker (`data-kind="discovery"`) · `.DS_Store` cleanup (`git rm` + `.gitignore`) · `millis()`/`map()` taught-notes · learner-mode L03_C05 + L04 C03/C04/C05 · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root · **"more prose to explain the challenges" (DJ, S59 — parked for a later pass).**

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure (DJ finalizes withhold policy after his student runthrough — this gates the §6.12a open cases) · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 · §9 difficulty grouping.

---

## PROCESS NOTES FROM S59 (worth keeping)

- **Every lesson's §9 is in a different format** (seen: purple-card A / green-callout B / guided-prose C / bare-heading D / §9-numbered). Project B is a bespoke per-lesson conversion, not a find-replace. L05 is the proven transform; §6.12a is the written standard.
- **The payload gate needs topic-suffixed filenames.** Live files are stable `Lesson_NN.html`; the gate regex wants `Lesson_NN_x.html`. Make symlinks: `for f in lessons/Lesson_*.html; do ln -s "$(pwd)/$f" /tmp/gl/$(basename $f .html)_x.html; done` then `python3 gate_payload_match.py newproject.html /tmp/gl/Lesson_*_x.html`.
- **Conversion recipe (proven ×3):** back up the lesson → extract each solution's inner block verbatim (regex on `<details data-reveal="solution">…<div style="margin-top: 12px;">(.*?)</div></details>`, re.S) → build canonical cards, author Goal/Logic/Template → splice by unique anchors (NOT line numbers; the back-to-top string is not unique — anchor the end on a unique kind= link) → verify (panels, tags balanced, blanks fill to solution, div balance, diff-audit head+tail) → bump version (§5b: comment full + banner major.minor) → payload gate → present.
- **Grep the files, not memory** (DJ's S59 rule). Confirmed twice: pills already swept; §6.12 note was stale.

---
*Written S59, July 20 2026. Project B underway — L05/L12/L13 converted, §6.12a canon. Commit `ac3d52a`.*

# ZUMO — S62 Handoff (written at S61 close, Jul 22 · paste at top of Session 62)

## Session open ritual
1. Clone fresh: `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal.
4. LIVE.md wins over memory. **Grep the actual file/commit, never trust a pasted version number — or a summary's session number** (see process note below).

## LIVE STATE — verified by fresh clone, Jul 22, commit `2401499`
All 16 lessons swept + live:
L01 v03.5.0 · L02 v02.9.0 · L03 v03.9.0 · L04 v04.4.0 · L05 v04.4.0 · L06 v04.8.0 · L07 v04.4.0 · L08 v04.3.0 · L09 v05.2.0 · L10 v02.3.0 · L11 v02.4.0 · L12 v01.4.0 · L13 v02.4.0 · L14 v02.6.0 · L15 v02.4.0 · L16 v02.3.0
Bible **v8.40** · Maker **v2.43** · Gate v1.6 · Harness v3.0

## DONE IN S61 (the "Coaches Callout" sweep)
- **Book-wide callout standardization, all 16 lessons.** Every coach callout now types by **function** on Bible §6.6a canonical colors: **Tip 💡** (make it work / fix it, `#f0f7f0`) · **Note 📘** (why / context, `#eceff1`) · **Warning ⚠️** (real caution / safety, `#fff8e1`). Reassigned by function, **not** original icon (the book had Tip/Note inverted in places). Bare labels, no "Coach's". Totals: **77 Tip · 107 Note · 72 Warning.**
- **L15 / L16 de-boxed.** Both used a bespoke color-coded emphasis-box system (~53 / ~40 boxes, mostly unlabeled — analogies, verdicts, takeaways). Rhetorical/analogy/flow boxes were flattened (box styling stripped to `margin: 16px 0;` — content + div kept, zero balance risk); only genuine callouts kept as canonical typed boxes. L15: 10 Warning / 3 Note / 1 Tip kept, ~39 flattened. L16: 4 Warning / 2 Note / 1 Tip kept, ~13 flattened.
- **Left alone (formal/distinct devices, NOT coach callouts):** 🔑 Key Term · 📖 LEARN · 🔍 INSIGHT · 📝 DO-THIS-NOW / rituals · ✅ CHECKPOINT · 👀 WHAT YOU SHOULD SEE · 🎯 CHALLENGE / THE GOAL · 🔮 WHAT'S NEXT · 🔁 Builds on · 📦 Fell behind? · 🏁 FINISHED EARLY? · 📋 PREREQUISITES · 🔨 COMPILE CHECK · 📓 ENGINEER'S LOG · 🏆 RoboCup Connection · type-explainer (`#e3f2fd`).
- **Triple-checked** (div-balance 16/16 · no double-icons / malformed styles / empty divs · git numstat balanced = no content deletion · visible-text word-diff = only the bared "Coach" label removed · formal devices byte-unchanged vs HEAD), **pushed, verified live by fresh clone.**

## CRITICAL PROCESS NOTE (this bit twice in S61)
The post-compaction summary CLAIMED L02–L15 were already swept — they were **NOT** on disk (only L01 was), so L02–L16 were re-done for real. The same summary called the session "S62"; it is actually **Session 61** (DJ's commit message + the on-disk LIVE.md both say 61). **Trust the file / the commit, never a summary's claims — including the session number.** The pushed LIVE.md was corrected from "Session 62" → "Session 61" after the fact.

## STILL STAGED / BLOCKED (carried)
- **Robot-icon FAMILY:** bordered + mark PNGs (Zumo · 3Pi+ · Romi · Balboa · Zircon) + the "pick your robot" chooser. **BLOCKED** on ChatGPT image credits + image quality (Balboa / Zircon / Romi). Five regeneration prompts already provided. Frame spec: 1254×1254, 64px inset, 95px radius, 14px stroke, `#010808` panel. Canonical glows: Zumo `#42F5D7` · 3Pi+ `#46F56C` · Romi `#FF4FBF` · Balboa `#9A5BFF` · Zircon `#FF8A00`. Method = **frame-swap**, not cut-and-rebuild. Bible §21.
- Single Zumo mark on the Textbook tile (`index.html` + `images/Zumo_Robot_Mark.png`) — in the working tree; confirm its push status at open.

## S62 NEXT — PRIMARY: difficulty-progression audit
DJ's stated big goal: **"the book must start easy and get consistently harder."** Book-wide check that L01→L16 ramps consistently — L01–L03 easy, steady hardening after. This was queued behind the callout sweep; it's now the front task.

## STANDING QUEUE (carried)
- **Expand the 📓 ENGINEER'S LOG icon + section** — DJ likes the device and wants to build it out (future add).
- **L03 open:** 1000 ms = 1 second explainer · modulo `%` explainer (C05) · Coach's Tip upload/power-on sequence · AI-autocomplete warning · L01 VS Code multi-root workspace step.
- **Challenge-card Part-B redesign:** apply L06's Goal→Logic→Template card pattern to all ~80–100 challenges (large authoring arc).
- **Maker batch:** starters-only full-course bulk download · `?lesson=N` progressive-disclosure gate · challenge folder `C##` labels · verify `?kind=` downloads are starters not solutions.
- **TDP template v3:** add A5 Lab Log (date · in/out · what — Outside-Work 5% evidence); re-commit to repo root.
- **Course docs:** day-by-day period grid + full syllabus document.
- **AI Tutor (LAST):** add DISCOVERIES to the per-challenge picker (needs `data-kind="discovery"`).
- **"Pick your robot" chooser page** — needs the bordered icon family (blocked above).

## BENCH (need the robot)
Q017 L09 green-tape six numbers · calibration-spin stopwatch · gyro-bias · L02 §5 green-LED bench check · Constrain RUN_MS.

## PARKED (don't reopen unprompted)
Challenge solution-disclosure (rules after classroom use) · monetization / ebook · "Know Your Zumo" reference page.

## KEY METHOD NOTES (if the callout system is ever revisited)
- Markup is extremely heterogeneous: ~8 drifted color schemes; icons as literal emoji **or** HTML entities (`&#9888;`⚠, `&#128161;`💡, `&#128216;`📘) **or** bare `⚠` without U+FE0F **or** thematic (🔧⏱🔥⚖🔴🛑); labels with curly / straight / entity apostrophes, sometimes UPPERCASE.
- **De-box method (L15/L16):** strip the box style to `margin: 16px 0;` — keeps the div + content, **zero** balance risk, reads as prose. Keep real callouts as canonical typed boxes.
- **Index-based reassignment is fragile** — ALWAYS re-extract the actual box list first (hit 57 boxes vs an assumed 53). `count == N` asserts abort **before** write (safe). Formal boxes can share a "content" color (L15 Key Terms use `#f4f9fc`) → filter formals out by keyword.
- **Verify per-lesson AND book-wide:** 0 live "Coach" labels (comment-aware — an `<!-- ... replacing old "Coach's Note" -->` comment is historical, leave it) · 0 wrong-color coach boxes · drifted colors gone · div balance unchanged.

---
*Written at S61 close, Jul 22 2026. Callout sweep live + verified. Next: difficulty-progression audit.*

# ZUMO_S36_HANDOFF.md — paste at the top of the next chat

**Session 36 open ritual:** Fresh-clone `github.com/Weymuth/zumo` — **everything lives there now**, including `LIVE_ZUMO_TEXTBOOK.md` (dated **July 14, 2026, Session 35 close**), the Bible, and the toolchain (`gate_payload_match.py`, `pio_harness.sh`, `extract_project.py`). Verify the Bible's internal line (`grep -o "Bible version: v[0-9.]*"` → expect **v8.21**). The project folder is now a single line of instructions.

## Where S35 ended

- **HEADER NORMALIZATION IS COMPLETE — all 16 lessons.** DJ ruled **4 PART banners, 5 colour groups**. The Bible was already correct; the book had drifted. §1–3 `#3498db` · §4–6 `#3a7d5c` · §7/8/8A `#c45d76` · §9 `#9b6a9e` · §10+end `#6c757d` (colour, **no divider**).
- The drift ran deeper than S34 mapped — **10 lessons, not 6**. L07/08/09 had no PART 3 banner at all; L10–L14 had an invented "PART 5 — Wrap Up"; L11 was off in four colour groups; L15/L16 had no section caps and gradient PART banners with non-canon groupings.
- **Image Index nav pill removed book-wide** (DJ ruling). Section stays; students don't navigate to it. Bible §6.5 nav-count line rewritten to 12–14.
- **L10 `step_4_RED` re-linked.** Verified the payload is genuinely broken and that fixing the `extern` builds green.
- Payload gate **PASS** 16/16 · **1,180 published figures byte-identical** — the S34 byte audit is intact.

## S36 job #1 — MAKER WIRING, L11→L16 (the whole session)

**100 kinds are live, gated, and unreachable:** L11:18 · L12:20 · L13:18 · L14:17 · L15:19 · L16:8.

**⚠️ DO NOT PATTERN-MATCH THE ANCHORS.** They are not uniform:
- **L13** is fully regular — `Step N` headings in §6, `7A–7E` in §7, `Challenge 9.1–9.3` in §9, `Mystery B1–B4` in Bonus.
- **L11** is a trap: its only `Step N` headings sit in **§3 theory**, not the §6 build. A regex would wire every link to the wrong place.
- **L16** has 6 step headings but only 5 `step_*` kinds.

Hand-place each link, verify the anchor by reading the surrounding prose, and diff before writing.

**Canon link shapes (extracted from L10):**

*Build steps + finished — a CATCH-UP `<details>` block:*
```html
<details style="background: #f8f9fa; border-radius: 6px; padding: 12px 15px; margin: 15px 0;">
<summary style="cursor: pointer; font-weight: bold; color: #5a6872;">📦 CATCH-UP &mdash; Step N</summary>
<div style="margin-top: 12px;">
<p><a href="https://weymuth.github.io/zumo/newproject.html?lesson=L&amp;kind=step_N" style="color: #2e86ab; font-weight: bold;">Open Step N in Project Maker</a></p></div>
</details>
```

*Calibration (7A–7E) — same block, different summary:* `📦 7A in the Project Maker` → link text `Open 7A — <name>`.

*Bonus mysteries — a bare `<p>` inside the mystery card:*
```html
<p style="margin-bottom: 0;"><a href="...&amp;kind=b1_xxx" style="color: #2e86ab; font-weight: bold;">Open B1 in the Project Maker</a></p>
```

L11–L16 take a **second** version bump for this (DJ accepted; Bible §9 requires it).

## Also queued

- Grok L01 batch — 4 cosmetic items (LED syntax note · debounce note · power-switch label art · `lib_deps` line-break bench check).
- **`lib_deps` pin** — 2.0.1 is a real release; DJ's earlier error was syntax. Bench-test `@^2.0.1` / `@~2.0.1` / git-tag → moderate bump (Maker + L01 prose + Bible).
- DJ bench checks: L02 green-LED claim · L09 green-tape (Q017).
- Delete 5 unreferenced images (list in LIVE.md).
- 22-photo queue (DJ) · **AI Tutor rebuild LAST**.
- Parked: "Know Your Zumo" board-map page · §9 difficulty grouping · L06 card pattern.

## Discipline reminders

Bounded edits with `assert count==1` · normalized diff audit · structural gate · payload gate (copy to `Lesson_NN_x.html` first) · **byte-residue sweep after every conversion** — the S34 figures must survive · fresh-clone verify every push AND check which version landed · one session zip in repo layout · numbered questions at close, most important first · a wrong answer is 3× worse than a blank · regenerate LIVE.md **LAST**, version appears in the status line AND the verify banner AND the LESSON STATE table.

**A header-consistency check now belongs in the gate battery.** This drift survived 33 sessions because the renderer strips styles and every text-based audit was blind to it.

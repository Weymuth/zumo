# ZUMO — S87 HANDOFF (written at S86 close · paste at top of Session 87)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md`
4. `python3 book_gates.py` · `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 lesson_inventory.py`
5. **Every version in this handoff is a LEAD.** Grep the files. The files win.

## LIVE AT S86 CLOSE
Bible **v8.73** · book_gates **v1.18 (31 gates, 31/31 PASS)** · lesson_inventory **v1.0.5** ·
**tutor v1.1.0** · gen_bonus_banner v1.1 · Maker v2.45.1 · pill_sweep v1.0 · Harness v3.0

L01 v03.10.4 · L02 **v03.1.1** · L03 **v03.15.1** · L04 **v04.9.1** · L05 **v04.11.1** · L06 **v04.13.1** ·
L07 **v04.9.1** · L08 **v04.8.1** · L09 **v05.6.1** · L10 **v02.6.1** · L11 **v02.8.1** · L12 **v01.9.1** ·
L13 **v02.8.1** · L14 **v02.10.1** · L15 **v02.7.1** · L16 v02.5.4

Census: **lines 39,837 · headings 1,025 · anchors 174 · fences 174 · part 64 · reveals 403 — byte-identical
to S84/S85.** Only the two counters that should move did: **constructs 145 → 171**, **mystery column 30 → 56**.
`lesson_inventory --anomalies` is **EMPTY**. That identity is the evidence the batch was attributes only.

## WHAT SHIPPED IN S86 — the §4.5 tagging batch
DJ ruling: three namespaced values, **`bonus-practice` / `bonus-observation` / `bonus-sabotage`**.

**68 tags across 14 lessons** — 42 renamed, 26 newly tagged, every edit under a `count==1` assert:

| family | value | lessons | renamed | new |
|---|---|---|---|---|
| Practice | `bonus-practice` | L02, L03 | 12 | — |
| Observation | `bonus-observation` | L04–L07 | 16 | L04 (5) |
| Sabotage | `bonus-sabotage` | L08–L15 | 14 | L10 5 · L12 4 · L13 4 · L14 4 · L15 4 |

**The 30 `mystery` tags were never one family** — 16 Observation, 14 Sabotage. The rename could not be a 1:1
map, which is precisely the distinction the shared value was hiding.

**Marker suffix deliberately NOT split** (§4.5): Practice keeps `.bN`, Observation and Sabotage keep sharing
`.mN`. `data-kind` carries the family. Recorded so a later session does not "fix" it.

## THE THING TO CARRY FORWARD
**`book_gates.py` contains the string `data-kind` ZERO times and was the critical consumer.** It reads `kind`
through `lesson_inventory.build()`, at §20.1's `c['kind'] == 'mystery'`. Renaming the lessons alone would have
made that match nothing and dropped every Sabotage reveal back to the ≥3-statement-line floor — the exact
condition that let L08 pass on luck for eight sessions (S80). **The COVERAGE assert could not have caught it**,
because it counts all constructs and tagging 26 more cards makes that number go UP. A gate can stop gating
without failing. Demonstrated, not argued: same tree, one planted line in a `hint` in a Sabotage card — old
value **PASSES**, new value **FAILS**.

**NEW gate 31 — `§4.2 every bonus card is tagged and its data-kind names its family`.** §20.2 had only ever
been asserted for UNIQUENESS, never PRESENCE; that is why 28 untagged cards sat inside a 30/30 book. It rides
gate 30's already-proven banner count. Control-run four ways. Card-count logic is now ONE definition shared by
gates 30 and 31 (S83 rule), and because that refactor touched a *passing* gate, gate 30's own decisive S85
control was re-run and still fails correctly.

**L16's hold expires by itself** at four cards; a lesson can no longer fall out of both `BONUS_TABLE` and
`BONUS_HELD` into silence.

**`tutor.html` v1.0.0 → v1.1.0** — three optgroups, and repairing `known[]` closed a live defect: the 12
L02/L03 bonus cards had been rendering **twice** in the picker. Found by executing the grouping logic, not
reading it. **Any kind added to §4.5 must be added to `known[]` in the same edit.**

## OPEN — IN PRIORITY ORDER

**1. L16 — the only lesson outside tagging.** DJ: *"Let's wait."* 2 cards against the family's 4; still reads
`Bonus: The Sabotage Files`; still the only pill saying "Bonus". Gate 31 now FAILS the moment it reaches four
cards, so this can no longer be forgotten — it is the nineteen-session-old *"L16 has zero challenge cards"*
item wearing a different hat.

**2. Rendered-Pages eyeball (DJ, not sandbox — weymuth.github.io is blocked here).**
**S86 changed ZERO visible text**, so it adds nothing here. Still outstanding: S85's visible-text changes in
14 lessons, and **S84 batch 1's five moved banners are STILL unverified** — L12 §6–§7, L13 §6–§7 / §7–§9,
L14 §6–§7 / §7–§9, L04 PART 2, L05 PART 2 / PART 4.

**3. The Sabotage family's internal order may be inverted against the difficulty goal.** Hidden-culprit hunts
FIRST (L08–L10), shown-line mechanism LATER (L11–L16). May be deliberate. **Look at this during the difficulty
audit, not before.**

**4. Weeding criterion for BC03 still needs a DJ ruling** — candidates L02 (7 items), L07 (6), L08 (6).
Blocks the §25.8 weeding pass. Carried from S84.

**5. LEADS LOGGED IN S86, NOT FIXED** (read before acting — §24.6c):
- **L12's bonus block holds ZERO `<details>`** — the only Sabotage lesson with no reveals at all.
- **L15's four Sabotage reveals are `hint`-only, no solution reveal.** I read them: genuine questions, not
  answers, so no §20.1 leak. Whether a Sabotage card should ship without a solution is a design question.
- **Four `data-reveal="mechanism"` blocks book-wide**; `mechanism` is not on §20.1's strip whitelist, so those
  reach the tutor. Read as teaching content, not answers.
- **Card title level is three strata** and it crosses the tagged line: `<h3>` L02/L03/L11/L15/L16 · `<h4>`
  L04–L10/L13/L14 · `#6c757d` header `<div>` in L12 alone. No rule governs it — the §6.8a shape.
- **A `__pycache__/*.pyc` is committed**, same class as the standing `.DS_Store`.

**6. CLOSED IN S85, do not re-open:** the *"unretired-ancestor gate, sweep h3–h4"* queue item.

## STANDING QUEUE (carried)
Difficulty-progression audit (L01–L03 easy → consistently harder book-wide, DJ's stated big goal) ·
challenge-card full redesign Part B (~80–100 cards to the L06 Goal→Logic→Template pattern) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
TDP template v3 (A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer, modulo
explainer, two Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with L08/L09/L10).

## LESSONS FROM S86 (the ones that cost time)
- **A consumer sweep by attribute name misses every tool that consumes the PARSED value.** `book_gates.py`
  holds zero occurrences of `data-kind` and was the one file that could have broken silently. Sweep the
  parsed field name too, not just the attribute string.
- **The inverse also bit, in the handoff's favour:** *"renaming touches `newproject.html` (3)"* was wrong —
  those are Maker download `kind=` ids, a different namespace. Grep hits in an unrelated namespace read as
  consumers.
- **A control of mine misfired and the gate was blameless.** The first silent-gate injection went into a
  `solution` reveal, which §20.1 ignores by design. §24.6b is not "assert something changed" but **assert the
  injection landed in the shape you intended** — third session running that this exact rule has paid.
- **Execute the logic, don't read it.** The tutor double-listing was invisible on the page and obvious the
  moment the grouping was run in node with a synthetic unit list.
- **Refactoring a PASSING gate obliges you to re-run its own control.** Sharing the card counter between
  gates 30 and 31 was right, and gate 30's S85 control was re-run to prove the port kept its teeth.

# ZUMO — S86 HANDOFF (written at S85 close · paste at top of Session 86)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md`
4. `python3 book_gates.py` · `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 lesson_inventory.py`
5. **Every version in this handoff is a LEAD.** Grep the files. The files win.

## LIVE AT S85 CLOSE
Bible **v8.72** · book_gates **v1.17 (30 gates, 30/30 PASS)** · lesson_inventory v1.0.4 ·
**gen_bonus_banner v1.1 (NEW)** · Maker v2.45.1 · pill_sweep v1.0 · Harness v3.0

L01 v03.10.4 · L02 **v03.1.0** · L03 **v03.15.0** · L04 **v04.9.0** · L05 **v04.11.0** · L06 **v04.13.0** ·
L07 **v04.9.0** · L08 **v04.8.0** · L09 **v05.6.0** · L10 **v02.6.0** · L11 **v02.8.0** · L12 **v01.9.0** ·
L13 **v02.8.0** · L14 **v02.10.0** · L15 **v02.7.0** · L16 v02.5.4

Census unchanged from S84 on every structural count — 1,025 headings · 174 anchors · 174 fences · 64 part ·
145 constructs · 30 mysteries · 403 reveals. That identity is the evidence the generate touched only text.

## WHAT SHIPPED IN S85 — §4.5, the three-family bonus block
The block at `id="bonus-challenges"` is **three constructs**, separated by one test: *what does the student
do in the first thirty seconds, and is anything broken?*

| family | mark | word | lessons |
|---|---|---|---|
| Practice | 🔨 `&#128296;` | Extra Practice | L02, L03 |
| Observation | 🔍 `&#128269;` | Observation — **nothing is broken** | L04–L07 |
| Sabotage | 🕵️ `&#128373;&#65039;` | Sabotage | L08–L16 |

Generated in one pass: 14 banners · 14 nav pills · 6 prose links · 4 FINISHED EARLY callouts ·
**21 card titles *Mystery N* → *Experiment N*** · 5 cross-references · L07's block intro.
**§4.5 SUPERSEDES the v8.14 (S20) "Bonus" vocabulary canon**, which had named the block once and rejected
"Extra Practice" outright. The anchor id `bonus-challenges` is UNCHANGED — it is the shared seat, not
family A's property.

## OPEN — IN PRIORITY ORDER

**1. TAGGING IS NOT ALIGNED (the direct follow-on, DJ already scoped it as its own batch).**
`data-kind` still reads `bonus` (12) / `mystery` (30). DJ ruled S85 *"values match"* — three families, three
values. **~28 cards carry NO `data-kind` and NO `data-challenge` at all**: L04 (5) · L10 (5) · L12 (4) ·
L13 (4) · L14 (4) · L15 (4) · L16 (2). L12–L16's cards are **div-titled with no heading**, so they are
invisible to the census, the §4.2 coverage gate AND the §4.3 picker. Renaming touches `book_gates.py` (7),
`lesson_inventory.py` (2), `newproject.html` (3), `tutor/tutor.html` (2), Bible (23) — and §20.1/§20.2 are a
PAIR, so re-reason both together.

**2. L16 HELD OUT of §4.5 by DJ ruling** — 2 cards against the family's 4. Still reads `Bonus: The Sabotage
Files`, still the only lesson whose pill says "Bonus". `BONUS_HELD` in gate 30 names it explicitly.
Bring it in when it has four cards — which is the nineteen-session-old *"L16 has zero challenge cards"* item
wearing a different hat.

**3. Rendered-Pages eyeball (DJ, not sandbox — weymuth.github.io is blocked here).**
S85 changed visible text in 14 lessons. **S84 batch 1's five moved banners are STILL unverified**: L12 §6–§7,
L13 §6–§7 / §7–§9, L14 §6–§7 / §7–§9, L04 PART 2, L05 PART 2 / PART 4.

**4. The Sabotage family's internal order may be inverted against the difficulty goal.** Hidden-culprit hunts
come FIRST (L08–L10), shown-line mechanism LATER (L11–L16). Hunting is normally the harder skill. May be
deliberate — L13–L16's byte-identical sabotage is conceptually the hardest thing in the book. **Look at this
during the difficulty audit, not before.**

**5. Weeding criterion for BC03 still needs a DJ ruling** — candidates L02 (7 items), L07 (6), L08 (6).
Blocks the §25.8 weeding pass. Carried from S84.

**6. CLOSED THIS SESSION, do not re-open:** the *"unretired-ancestor gate, sweep h3–h4"* queue item. Premise
was false — the §4.1 gate is whole-file substring, not `<h3>`-scoped, and its converted-only `continue` is
deliberate. The three live retired names (L10 `<h4>` *Check Your Understanding*, L11/L14 `<h3>` *Reflection
Questions*) are correct pre-conversion furniture, depth-walked and identically seated one level inside the
§10 panel. A two-sided pin (converted ⇒ 0, unconverted ⇒ inventoried) is cheap and can ride any batch.

## STANDING QUEUE (carried)
Difficulty-progression audit (L01–L03 easy → consistently harder book-wide, DJ's stated big goal) ·
challenge-card full redesign Part B (~80–100 cards to the L06 Goal→Logic→Template pattern) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
TDP template v3 (A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer, modulo
explainer, two Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with L08/L09/L10) ·
`.DS_Store` still committed.

## LESSONS FROM S85 (the ones that cost time)
- **A 12,000-character extraction window stopped INSIDE the block** and reported L02 at 5 cards and L03 at 4
  when both hold six. The lessons' own *"six more"* callouts were right. **Bound an extraction by a real
  landmark (banner → `id="glossary"`), never by a character count.**
- **A live precedent is a lead too.** L03's "Extra Practice" pill was reported as the prototype to follow;
  it is the exact drift the S20 ruling was written to kill. Grep the Bible before calling something canon.
- **Check a new rule against existing canon before writing it.** §4.5 contradicts a five-year-old DJ ruling
  and §25.12 was already taken — both caught only because the Bible was read at write time, not at design time.
- **The gate bug was the gate's, not the book's.** Placement regex demanded `</div>` at offset zero; L04/L05
  have a newline. Two correct lessons flagged. Read the flagged source before believing a new gate.

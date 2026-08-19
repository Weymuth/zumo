# ZUMO — After Sept 8

**Status:** work that is **deliberately deferred past the Fall launch**. Nothing here is blocking,
nothing here is forgotten, and nothing here is a defect a student will meet in the term as taught.
Every item carries who deferred it and why, so a later decision is a comparison and not a
re-derivation.

**Contrast with the two neighbouring files, whose contracts are different and must not be merged:**
`ZUMO_PARKED_EXIT_ITEMS.md` holds blocks that **were live** and were displaced by a §25 conversion.
`ZUMO_SHELVED_CARDS.md` holds card proposals that were **never live**. This file holds neither — it
holds *live, correct book content that could be better*, plus instrument and process debt, with a
date gate rather than a design ruling behind it.

**Opened:** S162, Aug 17 2026, per DJ ruling — *"Add that to the list of things to remember to do
after Sept 8."*

**WHY THIS FILE EXISTS AND WHERE IT NEARLY WENT WRONG.** Before S162 the deferred queue lived only
in the session handoff (S41 and S52 both carried a `STILL PARKED` section), and a handoff is
rewritten every session — so the queue survived only as long as whoever wrote the next one
remembered to copy it. **The S163 handoff dropped it entirely.** That is the S161 shape one layer
along: a record whose only home is a document the next session overwrites is not a record. It is
also §24.15's warning about an ungated root file that nothing links, which is why this file is
pointed at from **both** the handoff and `LIVE_ZUMO_TEXTBOOK.md` — a reader has to land on it.

**THIS FILE IS NEW AND IS NOT YET COMPLETE.** It was opened at S162 with the items below and no
others. **Absence from this list does not mean an item was finished** — it may simply predate the
file. Earlier deferred items still live in Bible changelog entries and in prior handoffs, and
migrating them here is itself an item on this list.

---

## 1. Hoist the three-terms one-liner into L01 §3.3's lead prose

**Deferred by DJ, S162.** Offered twice and declined twice — first as a hoist, then again after the
restatement below.

§16.25 shipped at S162: L01's KEY TERM now distinguishes the **board** (`Zumo 32U4 Main Board`), the
**chip** (`ATmega32U4`), and the **build target** (`a-star32U4`), and closes with *"Your robot does
not contain an A-Star board."* The book is **correct as it stands** — this is polish, not a fix,
which is why it can wait.

**THE EVIDENCE THAT IT MAY STILL BE OWED.** After the fix shipped, DJ restated it back as
***"the A-Star Board with an ATmega32U4 chip."*** That is the pre-fix claim, and it is the exact
reading §16.25 exists to prevent — restated by the person who had just been shown the corrected
text. §16.25 records that this confusion *"has come up twice and cost a ruling both times"*; this
was the third time, and the first time it happened **after** the correction was live.

**The inference, and it is an inference:** if a reader who has just seen the corrected KEY TERM
still lands on the old claim, the distinction may be sitting too deep in the page — a callout is a
box the eye can skip, and §3.3's lead prose is not. *(Basis: one instance, from a reader who was
mid-session and reading fast, not a student reading cold. One instance is a lead, not a finding.)*

**The proposed edit, if taken:** one sentence at the head of §3.3, ahead of the KEY TERM box —
*the board is a Zumo, the chip is an ATmega, and A-Star is only a compiler setting.*
Prose-only, zero bytes, no new element, no callout, no id, no gate movement.

**What would settle it better than another offer:** the first cohort. If a student writes "A-Star
board" in an Engineer's Log entry or a reading-quiz free response, the hoist is owed. If none does,
the KEY TERM is doing its job and this item closes as declined. **That is a fact about the room and
no instrument in this repo can see it — §24.17's first carve-out.**

## 2. Rename `L03_IMAGE_3-14_astar_board.jpg`, or rule that it stays

**Unruled since S155, still unruled at S162.** The file names a board the robot does not contain.

The photograph itself is **correct and needs no reshoot** — S162 found its `alt` text already read
*"Top view of the Zumo 32U4 main board"* while its own caption, in the same element, read *"The
A-Star 32U4 board."* The caption was corrected; the accessible description had been right all along.
So the filename is a **pure misnomer with no evidentiary force.**

**The cost, priced at S162 and why it was not taken:** the caption now reads *"The Zumo 32U4 Main
Board … (File: `L03_IMAGE_3-14_astar_board.jpg`)"*, which contradicts itself in one sentence.
Dropping the `(File: …)` clause was **rejected — 51 captions across the book carry it**, so removing
one creates an exception somebody must remember forever (rule 20). A rename is disk work plus
`image_audit`, §21 image-reference coverage and `site_parity`, **and it needs a file deletion through
GitHub Desktop — DJ's hands, and §24.17's recoverability carve-out.**

**Nothing a student sees is wrong** — the filename appears only in the `src` attribute and inside the
`(File: …)` clause. That is why it waits.

## 3. Migrate the pre-S162 deferred items into this file

The queue that lived in the S41 and S52 handoffs (challenge solution-disclosure · monetization and
ebook · the "Know Your Zumo" reference page · the AI Tutor rebuild) has not been re-derived since,
and **this file deliberately does not restate it from memory** — an item copied from recollection
rather than from a source is the §24.6c shape, a lead presented as a finding.

**The method when this is taken:** walk the Bible changelog and the prior handoffs in the git
history, pull each deferred item with its provenance, and record here only what a commit can be
pointed at. **Do not seed this file from a summary.**

---
*Opened S162 · pointed at from the CURRENT session handoff (`ZUMO_S173_HANDOFF.md`) and
`LIVE_ZUMO_TEXTBOOK.md` · the pointer names a file that is deleted and rewritten every session, so it
is re-aimed at each close (S164: it still named `ZUMO_S163_HANDOFF.md`; S166: it still named `ZUMO_S165_HANDOFF.md` — both deleted at their own push, which is why this line is re-aimed rather than trusted. S167 re-aimed it at close, deliberately, as the convention now requires; S168 through S172 did the same, and this line is the only home of that convention) · not versioned,
by the same convention as `ZUMO_PARKED_EXIT_ITEMS.md` and `ZUMO_SHELVED_CARDS.md`*

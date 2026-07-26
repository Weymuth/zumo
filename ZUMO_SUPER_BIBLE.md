# ZUMO SUPER BIBLE v8

**Bible version: v8.59** — increment on EVERY substantive edit (moderate change → `v8.x`; minor fix → `v8.x.y`; a new major re-baseline → `v9`). **Filename is now unversioned: `ZUMO_SUPER_BIBLE.md`** — the version lives ONLY in this line, never in the filename (this avoids a fresh chat misreading a filename number as the version). Current: **v8.59** (v8.59, S73 moderate — new **§25.10a**: the Brain Check family is FOUR and the shared column’s hardcoded-to-four script is the reason; an extra exit block folds into the BC it most resembles as a labelled group (L03’s *I can…* / *I have…* inside BC02, 12 `data-bc-skill` items); the skills unlock already generalises because `allSkills()` counts elements not a constant; column seats before `</body>`; and the subsection-slicing trap that makes a bad §-citation look verified.) Prior: **v8.58.1** (v8.58.1, S73 minor — §4.4 paperwork: the non-conformant table was written at S72 against work that had only been SPECIFIED. L01 was fixed S72; **L02’s renumber was cut S73** (v02.16.0 → v03.0.0). Attribution corrected; no rule changes. Recorded en route: BC01 item 3 cited §3.2 for the function prototype, which §3.2 never taught — a citation that was already wrong when it shipped S72 and would have been renumbered into a new wrong pointer. The §25.2 gate passes either way. **A §-citation is verified by checking the cited section CONTAINS the answer, never by checking one is present.**) Prior: **v8.57.1** (v8.57.1, S71 minor — §25.10 relocated AFTER §25.9 for numeric subsection order (it had been inserted before it); closing pointer added so §25.9 stays the section’s open-items ledger. No rule changes.) Prior: **v8.57** (v8.57, per S71 DJ ruling — **§25.10 GATED-ITEM ACHIEVABILITY**: a skill behind the BC02 lock must be earnable by every student who did the lesson; chance-dependent items get a deliberate rep. Applied: L01 v03.9.1→v03.9.2 gains the Break-It-On-Purpose upload-error rep (end of §6 Step 6) so item 10 no longer gates on luck. Review rule, not machine-gateable.) Prior: **v8.56** (v8.56, per S71 DJ ruling — **§25.10 SKILL GATE**: Brain Check 02\u2019s Mark-done button locks until all ten ☐ skills are tapped ☑; skills persist per-browser (`bc_LNN_sk`); tappable ☐ items are `data-bc-skill`-tagged; book_gates v1.6→v1.7 asserts box-glyph/tag parity in converted lessons, control-run with landed-injection assert. Applied: L01 v03.9.0→v03.9.1.) Prior: **v8.55** (v8.55, per S71 DJ rulings — **§25.10 BRAIN CHECK — NEW SUBSECTION + §8 TYPE 10**: the four §25.2 exit constructs get ONE family name (Brain Check 01–04), one livery (§8 Type 10 Knowledge: bg `#e8eaf6`, border `#3f51b5`, title `#283593` — indigo chosen by ΔE audit, min 32.3 vs every locked color), a fixed right-edge nav column with localStorage check-off (per-browser tracker, NOT a grade), and a two-state icon pair (gray incomplete / green-check complete; gray not red because §22 owns red for ERROR; state never color-alone — colorblind-safe via the check glyph; dark backings forbidden). Fixed en route: the Mental block in L01 had been NESTED INSIDE the §6 banner div since S70 — the banner rendered below the block and `color: white` inheritance made the five reveal ANSWERS white-on-white; un-nested, banner rebuilt canonical. book_gates v1.5→v1.6 extends §25.2 (anchors 01–04 + Type 10 wrapper + column presence), control-run FOUR ways with landed-injection asserts. Applied S71: L01 v03.8.1→v03.9.0. Icons at `images/BrainGear_Incomplete.png` + `images/BrainGear_Complete.png`.) Prior: **v8.54** (v8.54, per S70 DJ directive — **§25.6a THE TOOL PAGES ARE NOT CHAPTERS + LAYOUT IS GATED**, and **§5b WEB-TOOL VERSION LINE REWRITTEN**. DJ: "I don't want to have to deal with any more header and footer issues." The recurring defect was never markup — it was FILE LOCATION: `going_deeper.html` pushed into `lessons/`, then `tutor.html` pushed to root, both looking like clean pushes and neither catchable by a contents gate. book_gates **v1.4 → v1.5** adds `§12/§23 site layout` (asserts all 21 pages and their exact paths) and `§5b web tools carry an in-file version line`, control-run three ways. Fixed on this pass: `timer.html` and `tutor/tutor.html` had NO in-file version at all; `newproject.html`'s changelog opened with v2.18 against a live v2.45 (the v3.0 ghost); the Bible's own web-tool sentence claimed "Maker v1.3". Baselines set and labelled as baselines: timer v1.3.0 · Maker v2.45.1 · tutor v1.0.0 · index v1.3.0. index.html gained the site credits line. Prior: **v8.53** (v8.53, per S70 DJ rulings — **§25 THE EXIT-REGION CONSTRUCTS + §5b HIDDEN BUILD BANNER + HEADER/FOOTER CANON — NEW SECTION**: an audit of §10 found **six differently-named written-response blocks** doing overlapping jobs (STOP & PROCESS — Explain It in Writing · STOP & PROCESS — Answer From Your Head · Conceptual Understanding · Knowledge Check · Check Your Understanding · Reflection Questions), unevenly distributed, with **L13 and L15 carrying none at all** — the same §4.1 disease that produced three meanings for "Challenge". DJ ruled FOUR constructs, not three. **§25 canonizes them**, plus the reading-quiz design, the warm-up/spiral aiming rule, and the header/footer/hidden-banner canon that this session made uniform across all 17 pages. Applied S70: **L01 v03.7.0→v03.8.1** (the four blocks built — Mental 5 items before §6, Knowledge Check 4 items in §10, Reflection 3 prompts, plus 5 banked Canvas quiz variants); footer + hidden banner rolled to all 16 lessons and `going_deeper.html` **v01.0.0→v01.1.0**; DEEPER pill added to the §6.5a strip. Minor bumps: L02 v02.15.2 · L03 v03.13.2 · L04 v04.6.2 · L05 v04.8.2 · L06 v04.11.2 · L07 v04.7.2 · L08 v04.6.2 · L09 v05.4.2 · L10 v02.5.2 · L11 v02.7.2 · L12 v01.7.2 · L13 v02.6.2 · L14 v02.8.2 · L15 v02.6.2 · L16 v02.5.2.) Prior: **v8.52** (v8.52, per S69 DJ ruling ("Love c") — **§6.5a THE LESSON STRIP — NEW SECTION**: every lesson's sticky nav gains a second thin row of sixteen numbered squares 01–16 (plus a LESSON label and a ⌂ home square to index), current lesson rendered as a solid white square. Chosen from four presented options (prev/next pills · dropdown · number strip · titled drawer); the strip won on one-click access to every lesson, permanently visible. Ships as ONE byte-identical block in all 16 files — static links that work without JS plus a self-hydrating script deriving the current lesson from the URL — bounded by LESSON STRIP marker comments, so a renumber or an L17 is a single block edit. Explicitly OUTSIDE the v8.21 nav-button ceiling (12–14), which governs the section-pill row only. Gate shipped same-session per §24.2: book_gates v1.2→v1.3 adds `§6.5a lesson strip present and byte-identical in all 16`, control-run per §24.6b in BOTH directions — against the pre-strip clone (FAILED, 16 missing) and against an injected one-character drift (FAILED, "differs"). Applied S69 second batch, moderate bump all 16 lessons with both banners moved per §5b: L01 v03.7.0 · L02 v02.15.0 · L03 v03.13.0 · L04 v04.6.0 · L05 v04.8.0 · L06 v04.11.0 · L07 v04.7.0 · L08 v04.6.0 · L09 v05.4.0 · L10 v02.5.0 · L11 v02.7.0 · L12 v01.7.0 · L13 v02.6.0 · L14 v02.8.0 · L15 v02.6.0 · L16 v02.5.0.) Prior: **v8.51** (v8.51, per S69 DJ ruling — **§24.6c AN AUDIT GREP IS AN UNGATED GATE — CONTROL-RUN IT TOO**: §24.6b binds gates, which are versioned and reused; an ad-hoc audit grep is a single-use gate that is neither, and both S69 false positives came through that hole. (1) Structure inferred from a proxy string — timer iframes read `label=Step+2`, so the audit concluded L02 timed its BUILD STEPS; the timers are on TRY IT cards and the label merely names the step the card belongs to, which produced "22 untimed build steps in L03/L04" and a proposal to insert 22 timers onto plain build prose, a device existing nowhere in the book — DJ's confirmation stopped it. (2) Case-sensitivity — `Step [0-9]+` matched only the mixed-case card headings while L02 writes `STEP N:`, finding 9 steps where there are ELEVEN and manufacturing a label "drift" that does not exist (all 11 labels correct; STEP 7 legitimately carries two TRY IT cards, `2.t7` Advanced/untimed + `2.t8` timed, so the duplicate "Step 7" is the truth). THE RULE: control-run the grep against an independently visible case before the number becomes a finding · never infer structure from label text, check what element the match is attached to · case-insensitive by default, since book vocabulary varies by lesson and era (`STEP`/`Step`, `CONFIGURATION`/`CONSTANTS`, "Coach's Tip" vs bare §6.6a labels) · report findings as VERIFIED or SUSPECTED, and a queue/handoff item enters the next session as SUSPECTED until re-checked — S69 also relayed the S68 queue's GRAPHIC 5.5 cone-angle suspicion as a defect when it was clean (bearings −90.0/0.0/+90.0, already matching the corrected 5.1). Extends §11 v8.36.2 from prose greps to STRUCTURAL ones and adds the reporting format; works against the standing pressure that a longer audit list reads as more valuable, against DJ's rule that a wrong finding costs 3× a blank one. Applied S69: L03 v03.11.1 + L04 v04.5.4 (timer gaps closed — L03 BC4 at 6 min, L04 C4/C5 at 4 min; all four card types now timed except main challenges, which are untimed in L02/L03 by convention and timed in L04 by DJ ruling) · L05 v04.7.1 (§4.1 Key insight had attributed proximity DIRECTION to which LED team fired, contradicting the §3.4 series-wiring fact two paragraphs above it — direction comes from which detector answers; §8A.1 emitter count and §4.2 vocabulary aligned; GRAPHIC 5.5 gained its missing caption).) Prior: **v8.50** (v8.50, per S68 DJ ruling — **§24.6 STRUCTURE IS VERIFIED BY PARSE, NOT BY COUNT**: a count-based tag gate can be satisfied BY the bug it should catch — eight lessons shipped with the Image Index panel close misplaced, six of them past `</html>`, and open/close counts balanced *because* the orphan balanced the unclosed panel, so `tag balance` returned PASS for the defect's entire life. Provenance git-verified: L01 from its first tracked commit (hand-authoring); L12–L16 all five from ONE commit, `94acc10` S35, the §6.5 flat-heading→boxed-section conversion, whose stateful close-the-previous-panel transform had no terminator for the last panel. **§24.6a A PARSER IS NECESSARY AND NOT SUFFICIENT** — L06/L07 parsed clean and were still wrong (footer sealed inside the box), so a semantic container assertion ships alongside. **§24.6b CONTROL-RUN EVERY NEW GATE AGAINST THE UNFIXED SOURCE.** book_gates v1.1→v1.2, two structural gates. Applied S68: L01 v03.6.5 · L03 v03.11.0 (new §8A.5 arrays + §8A.6 modulo closing the v8.41-logged C05 teaching gap; C05 grasp re-rated Deep→Moderate, doing axis and therefore the ramp untouched) · L06 v04.10.1 · L07 v04.6.2 · L08 v04.5.1 · L12 v01.6.2 · L13 v02.5.2 · L14 v02.7.2 · L15 v02.5.2 · L16 v02.4.1; Going Deeper pointers added to L07/L08/L12/L15/L16.) Prior: **v8.49** (v8.49, per S65 DJ ruling — **§24.5 THE DEPTH AUDIT + ROLLING HUMAN READ**: DJ's L02 diagnosis ("brief info, not a lot of depth") becomes standing process. book_gates.py v1.1 gains 3 gates (cross-lesson promises, arithmetic verification, §16 constants). New `DEPTH_AUDIT_S65.md` maps the findings. Verified structural find: **the teaching apparatus disappears at L11** — L11–L16 have ZERO LEARN boxes and near-zero KEY terms on the book's hardest material; mostly a marking fix, own arc. L14 profiles thinnest book-wide, goes first in DJ's read. §11 doubly applied: the scan's bitwise/pointer hits were 100%% false positives — a scan finding is a candidate until a human reads the section.) Prior: **v8.48** (v8.48, per S65 DJ directive "be more consistent and fix everything" — **§24 BOOK GATES — NEW SECTION + NEW TOOL `book_gates.py` v1.0**: every machine-checkable Bible rule runs against the whole book in one pass, at session open and before every delivery; a delivery that has not passed is incomplete (§12.6 class). Root cause canonized: the recurring S65 failure was fixing the INSTANCE instead of the CLASS — three times a named fix left the same defect alive elsewhere. §24.2: a rule canonized without its gate written in the same session only holds where someone happens to look. §24.3: gate the whole field, not the captured group (June/July survived a "passing" version check because the regex captured only the digits). §24.4: a computed claim is verified by computation, never recall (the 18-bytes-for-a-17-byte-string error). Also fixed on this pass: L01 What's-Next promised =/== as Lesson 2 content while L02 §3.2c deliberately defers it to L03 — question kept, phrasing fixed (cross-lesson instance of §11 "§8A must cover what §9 requires"). Applied: L01 v03.6.4, L02 v02.13.4.) Prior: **v8.47** (v8.47, per S65 — **§4.3 THE PICKER LABEL IS THE ELEMENT'S OWN TEXT**: the AI Tutor builds each dropdown option from the tagged element's `textContent`, so a construct must name itself. S65 tagged 11 L02 TRY IT boxes reading only "TRY IT (1 minute)" — six were identical in the dropdown. Correct tagging, unusable labels. Read the textContent out of context BEFORE tagging. `data-kind` now drives optgroups (Challenges / Warm-Ups / Try It / Mysteries); **no `data-kind` still means canonical challenge card**, so the 14 untouched lessons are unaffected, and unknown kinds fall to "Other" rather than being dropped. Applied: L02 v02.13.1, L04 v04.5.2, tutor/tutor.html.) Prior: **v8.46** (v8.46, per S65 DJ ruling — **§4.1 THREE CONSTRUCTS, THREE NAMES**: the word "Challenge" is reserved for the §6.12 card. Section 1 warm-ups become **Warm-Up N**, inline green practice boxes become **TRY IT (n minutes)**, Bonus Challenges keep their name. L02 had shipped with warm-ups 1–4 AND Bonus 1–6 both called "Challenge N", so "did you finish Challenge 3?" had three answers and the AI Tutor could only see the Bonus set. **§4.2 EVERY PRACTICE CONSTRUCT IS TAGGED** (extends §20.2): warm-ups and TRY IT boxes now carry `data-challenge` + `data-kind`; suffix `w`/`t` in the marker keeps them from ever colliding with a card number. Audited book-wide: gaps existed only in L02 (15) and L04 (1), both closed; 104 unique markers, zero duplicates. Applied S65: L02 v02.13.0, L04 v04.5.1.) Prior: **v8.45** (v8.45, per S65 DJ rulings — **§22 TERMINAL OUTPUT COLOR CANON — NEW SECTION**: simulated PlatformIO console output gets two locked colors — SUCCESS `#6a9955`, ERROR `#f14c4c` — so a student can answer "did it work?" before reading a word. `#6a9955` is DJ-ruled and is deliberately the same green as a `//` comment; the real terminal is brighter (~`#23d18b`) but L01 already used `#6a9955` and DJ ruled to keep ONE success green — do not "correct" it. **Color the diagnostic, not the block**: the source echo and caret stay plain `#e8e8e8`, because the echoed line is the student's own code and L02's "the compiler points at the line AFTER the mistake" rule depends on them judging it themselves — in the very case being taught, that line is innocent. **Detect terminal blocks by console markers** (`error:` with colon, `undefined reference`, `Writing |`, `[SUCCESS]`), never by the bare word "error": of 71 blocks containing "error", only **11** are console output — §11 false-positive discipline applied to color. Also canonized this session: **§6.13 the guard-clause brace rule** (K&R is house style, 837 vs 2; braces are the default; braceless only when the whole statement fits on the `if` line — the book has 93 such guards and they are correct, so "always brace" was NOT adopted) and **§23 GOING DEEPER** (standalone optional page at repo root, outside the 16-lesson numbering, not in the Maker registry; every entry must anchor to a chapter). Applied S65: L01 v03.6.2 · L02 v02.12.2 · L07 v04.5.1 · L12 v01.6.0 · L16 v02.4.0 · new `going_deeper.html` v01.0.0.) Prior: **v8.44** (v8.44, per S64 DJ rulings — **§6.12b THE SPLIT-PILL SWEEP IS COMPLETE**: all **84 challenges across 15 lessons** now carry the two-axis pill; `data-difficulty` + `data-grasp` are present and equal-count on every card, and **zero** old single pills remain (verified by `pill_sweep.py --audit`). L16 has no challenges (tier-cards, §6.12 variant) and is exempt. **§6.12c NEW — INLINE CSS DRIFTS PER REBUILD, MATCH STRUCTURALLY**: the same visual component carried **9 distinct style strings** across L04–L15 because Canvas strips `<style>` and `class=`, so every card holds its own copy and every rebuild retypes it; git shows the flips are single-commit and lesson-clustered (L05/L12/L13 all changed in `a3cd518`), i.e. STRATA, not rot. An exact-string replace is therefore invalid book-wide — match by STRUCTURE and scope the replace to one challenge block. **§11 A TRANSCRIBED-ONLY CONSTRUCT GETS A QUICK REFERENCE ROW, NOT A PROSE SECTION**: if a challenge template supplies a construct complete and the student only fills values, the comprehension load is nil and a §5 section is over-sized; give the "look it up" instruction a landing target instead (S64: `map()` → L08 `qr-map`, `do…while` → L09 `qr-dowhile`). A construct the student must COMPOSE still gets full prose. **§5b BOTH VISIBLE BANNER HOMES ARE MANDATORY**: header AND footer; L02 and L12 shipped with only the header and were repaired S64. Applied S64: L02 v02.10.2 · L04 v04.5.0 · L05 v04.5.0 · L06 v04.9.0 · L07 v04.5.0 · L08 v04.4.0 · L09 v05.3.0 · L10 v02.4.0 · L11 v02.5.0 · L12 v01.5.0 · L13 v02.5.0 · L14 v02.7.0 · L15 v02.5.0. New tool `pill_sweep.py` v1.0 at repo root.) Prior: **v8.43** (v8.43, per S63 DJ ruling — **§6.12b SLASH HALVED**: the split-pill divider goes `width: 8px; margin: 0 -4px` → `width: 4px; margin: 0 -2px`. The negative margin is structurally half the width — changing width alone opens a gap where the halves no longer close over the slash. Applied to all 25 live pills (L01 v03.6.1, L02 v02.10.1, L03 v03.10.1); markup was uniform, zero variants. Cosmetic-only, so hidden comment bumped and the visible banner left alone per §5b. DJ noted a possible further halving to 2px later — NOT applied.) Prior: **v8.42** (v8.42, per S63 DJ rulings — **§21 ROBOT ICON FAMILY REVISED — the family is LIVE**: 42 files pushed to `images/glowbots/` (commit `12867ea`), 25 bordered + 15 glow + 2 QA sheets. **§21.3 SUPERSEDES the S61 frame-swap-only rule** — the "NEVER separate the robot from its glow" prohibition is LIFTED; it was written from a failed attempt, and S63 cut all five successfully, including the two §21.4 predicted would defeat it. Two outputs, two methods: BORDERED (frame-swap) for buttons, GLOW (extract-and-cut) for images. Two findings make the cut work — (1) EDGE-CONNECTED FLOOD FILL, never a global brightness threshold, so interior dark pixels (Zircon PCB, Balboa frame gaps) survive by construction; (2) CUT THE FALLOFF, do not preserve it — the glow is painted additively on black so its falloff IS black, and keeping it as soft alpha renders a grey haze that is invisible on dark and filthy on white. **GLOW FLOOR 128 px**; buttons are always bordered. **QA RULE: CHECK ON WHITE** — every S63 glow defect was invisible on a dark background. **§21.2 colors** — canonical is the spec, as-built is recorded drift (generator approximation, not a design change); 3Pi+ is the Δ55 outlier. **§21.1 as-built inset deviation logged** — all five ship at 10–18 px against a 64 px spec; DJ ruled "leave them for now", so 64 stays the spec and the images are knowingly off it. §21.7 records the live file inventory + the uniformity spec (mean edge distance 1.28–1.32 px, p95 2.00, zero opaque edge pixels). No lesson versions changed.) Prior: **v8.41** (v8.41, per S62 DJ ruling — **§6.12b THE SPLIT DIFFICULTY PILL — NEW SECTION**: the difficulty pill becomes ONE badge cut by a 45° slash into two rated axes — DOING (five warm tiers, what the hands do) and GRASPING (three blues, what the head must hold). Supersedes the v8.27 single five-tier scale, which forced one label to lie whenever the axes diverged (L03 C08 writes comments only yet reasons about encoders three lessons early — ADVANCED warned students off it, EASY hid the hard part; Easy/Deep is the truth). Grasping is rated AGAINST THE LESSON PROSE, which makes the pill a live instrument for §11 "§8A must cover what §9 requires": a Deep rating on an untaught concept IS a logged teaching gap. New attribute `data-grasp`; `data-difficulty` retained for the doing axis. Applied S62: L01 v03.6.0, L02 v02.10.0, L03 v03.10.0 — 25 pills, five doing-axis re-rates, one teaching gap marked (L03 C05 needs arrays + modulo, neither in L03 prose). L04–L16 not yet swept.) Prior: **v8.40** (v8.40, per S61 DJ ruling — **§6.6 + §6.6a — TIP/NOTE/WARNING BY FUNCTION**: the Icon Guide gains 📘 **NOTE** (13 icons); three coach callouts are defined by function — 💡 Tip = actionable fix/how-to (green), 📘 Note = enrichment (slate `#eceff1`/`#607d8b`), ⚠️ Warning = real caution (amber). Labels are bare. The book had Tip/Note INVERTED (icon drove the label — enrichment wore 💡, fixes wore amber "Coach's Note"); being corrected book-wide S61 by reassigning every coach callout by function. L01 done (v03.5.0).) Prior: **v8.39** (v8.39, per S61 DJ ruling — **§21 ROBOT ICON FAMILY — NEW SECTION**: the matching robot "chooser" icons (one per fleet robot) as a single design family — shared frame (1254² rounded square, border inset 64 / radius 95 / stroke 14, near-black `#010808` panel, robot ~75–80% of panel), only the robot + accent glow color change. Records BOTH color sets per robot — CANONICAL (style-guide neon target) AND SAMPLED (measured from the first uploads, darker) — kept side by side, reconcile later. **Build method = FRAME-SWAP, not cut-and-rebuild**: keep the robot + its glow together and only replace the outer frame; NEVER separate the robot from its glow to regenerate it (fails on dark-bodied / open-frame robots — black-on-black defeats a brightness cut, and a regenerated glow loses the outer rim; this is why Zumo/3Pi+ went smoothly and Balboa/Zircon/Romi fought back). Staged for a future "pick your robot" page — not yet in the book.) Prior: **v8.38** (v8.38, per S59 DJ rulings — **§6.12a THE THREE-PANEL CARD + WHEN IT APPLIES (Project B canon) — NEW**: the §6.12 card skin is the mandatory SHELL on every challenge (outer box, gradient header with **sequential** `Challenge N` never §-based, five-tier pill, pale-yellow `#fffbe6` Work-in bar with 📁 Work-in + 🔍 Where-to-look, flush `data-reveal="solution"`); the INNER format fits the challenge type — **algorithmic** → three tiled panels 🎯 Goal `#f8f9fa` / 🧠 Logic-pseudocode `#f3e5f5` (absorbs the hint; NO separate hint box) / 🧩 Template `#e8f5e9` (blanks fill EXACTLY to the solution); **guided-edit/debug/observation** → prose, no panels (L01 is the reference, left as-is). No white body wrapper, no Plan-first. Open cases provisional pending DJ's runthrough: L08/L09 show Template + solution; YOUR-NUMBER two-level scaffold; solved-build vs starter link placement; solution code comments stay payload-matched on renumber. **§6.12 pill-sweep note corrected** — the sweep is COMPLETE (verified from files S59: 73 pills, all conforming, 0 EXPERT/COMPETITION). Applied S59: L05 v04.3.0 (pilot), L12 v01.3.0, L13 v02.3.0.) Prior: **v8.37** (v8.37, per S58 — **§20 AI TUTOR & MACHINE MARKERS — NEW SECTION**: the tutor reads live lessons with NO embedded curriculum (anti-rot); §20.1 `data-reveal` typing on every `<details>` (the tutor strips only `solution`, so any graded answer — including a debugging-mystery bug+fix reveal — must be typed `solution` or it leaks, and an open-prose or bare-`<pre>` solution is NOT stripped); §20.2 `data-challenge` marker on every challenge (the picker queries `[data-challenge]`; an untagged challenge vanishes; L16 tiers exempt); §20.3 both markers mandatory on new content; §20.4 favicon needs an explicit per-page `<link>` on a Pages project site. Also **§12.4 VERIFICATION DISCIPLINE — CACHES LIE** (shallow-clone lag, `git show --stat` on a shallow clone lists the whole tree as added, raw/API caches, upload-location trap) and §737/§935 accuracy fixes. Prior: **v8.36.2** (v8.36.2, per S58 — **§11 AUDIT FALSE-POSITIVE DISCIPLINE**: a prose-keyword grep reports candidates, not verdicts — separate code from prose before counting, treat a keyword near a heading as a lead, verify every finding against rendered text before acting. Canonized after S57's construct sweeps threw a run of prose-keyword false positives, each evaporating on a read. Prior: **v8.36.1** (v8.36.1, per S57 — **§11 §8A MUST COVER WHAT §9 REQUIRES**: a construct the challenges ask students to write must be taught in that lesson; using it in given code is not teaching it. Fix pattern = teach at first contact, demote the later tutorial to a §18.1 spiral second rung. Applied S57: L04 v04.1.0 gains §8A.6/§8A.7 for the `for` loop, L05 v04.2.0 §5.15 becomes the second rung and adds the descending loop its own challenges assumed. Prior: **v8.36** (v8.36, per S57 — **§16.9 EEPROM ADDRESS MAP — NEW**: the fleet shares one flat 1,024-byte EEPROM with no protection; 0–511 Lesson 16 `Saved`, 512–543 the robot name (magic `0x5A`, written by `ZUMO_NAME_WRITER_main.cpp`), 544–1023 free for enhancements. **§11 A "THE BOOK HAS NEVER…" CLAIM IS A DEPENDENCY** — grep the whole lessons tree before trusting a never/first-time sentence. Both canonized after S56's L01 §9 publication of the EEPROM name-reader silently falsified L16 §4.3's "this book has never touched it." Applied S57: L16 v02.2.3.) Prior: **v8.35** (v8.35, per S56 DJ rulings — **§11 IF IT IS IN THE PAYLOAD, IT GOES IN THE BOOK**: an unmatched payload-gate line is a GAP IN THE BOOK, not a gate defect; the fix is to add the content to the lesson, never to exempt the line, and EXECUTABLE CODE IS NEVER EXEMPT. Canonized after S55 burned four takes proposing to exempt L01's 900 failures as "comment-only scaffolding" when 132 were an EEPROM name-reader that appeared in NO lesson while C01 Part 5 asked students to use it. S56 fixed it the right way: the shared 88-line challenge body was published in L01 §9 and each of the eleven cards now quotes its OWN target line verbatim — EXECUTABLE CODE went 132 → 0 with zero exemptions. **§11 BOXED INSTRUCTION HEADERS ARE ADVISORY BUT FINGERPRINTED**: a challenge file's boxed header is the student's working instructions and stays IN the file (DJ ruling: students code in one window and read in another, and a step you remove is a step they will actually do), so a non-matching boxed line is a FORMAT difference reported under ADVISORY rather than a failure — BUT advisory never means unchecked: gate v1.6 pins every header with a line count + md5 in BOXED_FP, so an edited header fails loudly and intentional changes go through --update-fp. **§11 READ THE CENSUS, NOT THE RAW COUNT**. Applied S56: L01 v03.4.0, Maker v2.39, gate v1.4→v1.6.) Prior: **v8.34** (v8.34, per S55 DJ ruling — **§12.6 LIVE.md STALENESS IS A STRUCTURAL FAILURE — NEW**: S54 and S55 both pushed version bumps without regenerating LIVE.md, leaving it describing a state two sessions old; S55 then burned FOUR attempts re-diagnosing, three of them building on wrong version numbers. §12.3 already ruled that "remember to update LIVE.md" is too weak — §12.6 closes the window structurally: (A) write LIVE.md when the last version-changing edit lands, re-verify at close (§12.3's steps 1–5 unchanged); (B) a push that bumps a version and omits LIVE.md is an INCOMPLETE PUSH, a defect of the same class as a card disagreeing with its file; (C) session open runs a DRIFT CHECK — grep the files, compare to LIVE.md, THE FILES WIN, and on disagreement ask DJ for a newer LIVE.md before regenerating one. Do not enter queued work on a known-stale LIVE.md.) Prior: **v8.33.1** (v8.33.1, per S51 DJ ruling — **§18.3 SECTION-LIST RECONCILED**: line 859 declared "all five section headers" but named FOUR, in L03-era vocabulary (`CONFIGURATION`, `STATE VARIABLES`) that OMITTED `GLOBAL VARIABLES` — the exact section the ≥L4 `mainCpp()` scaffold was itself missing. Rewritten lesson-agnostic: the standard headers in canonical SET + ORDER, names varying by lesson (`CONSTANTS`/`CONFIGURATION`, `GLOBAL VARIABLES`/`STATE VARIABLES`), none dropped just because a step hasn't filled it. Paired with Maker v2.32→v2.33, which added the missing `GLOBAL VARIABLES` header to the ≥L4 blank starter — the L04 Step-2 landing zone.) Prior: **v8.33** (v8.33, per S49 — **§10 image-URL canon**: 114 `<img>` refs moved raw→Pages; EXIF-strip rule; §11 no-dark-prose checklist item. *This changelog entry was backfilled S51 — the S49 header bump left the list at v8.32.*) Prior: **v8.32** (v8.32, per S48 DJ rulings — **§19 PER-LESSON LEARNING-MODE FILE — NEW SECTION**: each lesson may carry a companion `ZUMO_LEARNMODE_LNN.md` in repo root recording the Socratic learner-mode walkthrough of its challenges (difficulty roll-up + per-challenge detail + Coach's Tips + queued finds); it is a teacher-side teaching record and a source for the AI Tutor rebuild, NOT student-facing and NOT a payload source. L03's is live (`ZUMO_LEARNMODE_L03.md`). **TERM: "CHALLENGE TEMPLATE"** — the full-section-header starter of §18.3 is named a **challenge template** project-wide (Bible + cards + Maker labels); "scaffold" is retired for this sense (it still means the TDP accumulation in §14 and the theory-first build in §5). Prior: **v8.31** (v8.31, per S45 DJ ruling — **§5b IN-FILE VERSION REWRITTEN — REVERSES the major-digit-only rule.** The full version now lives in TWO durable in-file homes so it can never again be trapped in LIVE.md alone: (1) the VISIBLE header/footer banner carries **major.minor** `vXX.XX` (e.g. `v03.2`) — it churns only on a moderate-or-larger bump, NOT on a minor/cosmetic one; (2) a HIDDEN HTML comment at the very top of the file carries the **FULL** `vXX.XX.XX` (e.g. `<!-- Lesson version: v03.2.5 -->`), greppable, invisible to students, updated on EVERY bump. The stable published filename `Lesson_NN.html` is UNCHANGED. Rationale: publishing as a stable filename + a major-digit-only banner left the exact minor version recorded ONLY in LIVE.md — when LIVE.md corrupted (S45), L11–L16's true minor was unrecoverable from the repo. Applied to L01–L10 in S45; L11–L16 get the new banner+comment when each is next opened and its version reconciled from the git-proven floor.) Prior: **v8.30** (v8.30, per S45 DJ ruling — **§18.4 TYPE-EXPLAINER CALLOUT — NEW** (a data type is introduced in a blue `#e3f2fd`/`#2196f3` info callout, one line per type: `type — description — example`; the SAME look is reused for each type's later deep dive so students recognize it on sight — L02 §3.2b introduces int/bool/float/long/char, long deep-dives L05, float L07, char named-only; forward-pointers must be grepped against the code, not guessed). **§18.3 + CHAT-DISPLAY RULE** — when showing a Maker starter in chat, prepend the wrapper header (`#include <Zumo32U4.h>` + MY PLAN) so the display matches the generated file; the raw payload body starts at HARDWARE OBJECTS and does not compile alone. Applied S45: L02 v02.2.1 (data-types callout + int/bool prose), L03 v03.4.1 (constrain two-jobs callout + USB-falsifies-battery callout).) Prior: **v8.29** (v8.29, per S44 DJ ruling — **§18.3 CHALLENGE-STARTER PRINCIPLES REWRITTEN**: a starter is now the FULL section-header template (all five headers + seeded CONFIG constants + present setup()/loop()) with only the taught concept left blank in a marked landing zone — REVERSES the S40 minimal-skeleton rule (students are used to the whole template; a skeleton reads as unfamiliar). Payload bodies START at HARDWARE OBJECTS; the Maker mainCpp() wrapper supplies the banner + #include + MY PLAN. A starter must not require a construct the book hasn't taught yet — L03 Ramp uses unrolled by-hand steps, not a for loop (not taught until L05). Applied S44: L03 constrain + ramp starters (Maker v2.30), L03 Ramp card prose + solution rewritten (v03.4.0).) Prior: **v8.28** (v8.28, per S43 DJ ruling — **§18.2 INLINE-STAR RENDERING LOCKED**: an inline spiral star is the actual `spiral_star_NN.svg` asset via `<img>` (absolute raw URL, `height:1.1em; vertical-align:middle`), NOT an emoji; emoji ⭐ appears only in the literal "🔁 Builds on:" header glyph. First appearance = L02 §9 "Builds on:" explainer, introducing the mark before L03's first marked card.) Prior: **v8.27** (v8.27, per S42 DJ rulings — the L03 challenge-redesign build: **§6.12 RATING SCALE recolored/relabeled to UP-TO-FIVE tiers** — EASY `#4caf50` · MEDIUM `#2196f3` · TOUGH `#9c27b0` · HARD `#ff9800` · ADVANCED `#f44336` (a lesson uses as many as it needs, in order; no minimum per tier). Replaces the old EASY/MEDIUM/HARD/EXPERT/COMPETITION set; **book-wide pill sweep of existing lessons is QUEUED, not yet applied** (~47 pills: MEDIUM orange→blue ×27, HARD red→orange ×15, EXPERT→TOUGH purple ×5). **§18.2 student-facing marker header renamed "🔁 Spiraled skills:" → "🔁 Builds on:"** ("spiral" stays the teacher-side method name; ⭐ numbered-star convention unchanged). Prior: **v8.26** (v8.26, per S40 DJ rulings — the S40 documentation pass, folding decisions that had lived only in session memory into durable canon: **§14.1 THE LOG *IS* THE TDP** — the 16 Engineer's Log prompts accumulate into ONE growing Google Doc structured as a RoboCupJunior TDP; notebook and TDP are the same artifact; template = `ZUMO_TDP_Template.md` (repo root, live); prompts stay in the lessons (one source of truth), the Doc holds only TDP scaffolding + PART A standing lists (A1–A5). **§18 CHALLENGE-DESIGN CANON — NEW SECTION**: (18.1) the **Saxon spiral** — each lesson's challenges reinforce 1–2 PRIOR concepts alongside the new one; roll out going forward lesson-by-lesson, do NOT retrofit L01/L02; one new concept per rung. (18.2) **marker convention** — blue "🔁 Spiraled skills:" header line naming the source in words + inline ⭐ numbered stars with the source lesson # inside; assets `spiral_star_01..16` in `images/` (vector-path numbers, gold gradient). (18.3) **starter principles** — minimal skeleton, includes + the ONE needed hardware object pre-placed, empty section headers ("// (none needed for this challenge)"), MY PLAN ships blank, marked "// write your code here" zone, don't re-explain setup()/loop(); challenge folder labels may take a C## prefix (output-string only, keep kind= ids, flat). Prior: **v8.25** (v8.25, per S39 DJ ruling: **§16 HARDWARE GROUND TRUTH — NEW SECTION** and **§17 SVG / GRAPHIC CANON — NEW SECTION** — capture into the Bible the hardware and SVG canon that previously lived only in session memory, so a memory failure has a durable backup. §16: gear-ratio sticker colors (Green 50:1 / Blue 75:1 / Red 100:1; fleet = blue 75:1, verified vs Pololu 0J63 §1.1), TRIM = LEFT motor, setSpeeds() ±400 hard-cap and what constrain() actually protects, brake-style stop, stall current (one event two symptoms), encoder averaging, shared pins 20/4, 28,672/2,560 B ceiling. §17: 1100×850 canvas, blue title band, single-polygon arrows, section colors, IMAGE/GRAPHIC separate number spaces, and the textLength stretch trap (only over-stretch is a defect; ~30 SVGs use it — per-file audit deferred, do not blind-replace). Prior: **v8.24** (v8.24, per S36 DJ ruling: **§12 DOCUMENT WORKFLOW REWRITTEN** — the old text was stale (it said to UPLOAD the Bible at session open, and named a handoff file that does not exist). **EVERYTHING LIVES IN THE REPO** — Bible, LIVE.md, handoffs, gate scripts, harness, web tools, lessons, images. Session open = CLONE, not upload. Session close = **ONE ZIP, FULL REPO LAYOUT, EVERY CHANGED FILE INCLUDING ROOT DOCS** — one extract, one commit, one push. A zip cannot DELETE: removals ship as explicit `git rm` lines in the close note. Prior: **v8.23** (v8.23, per S36 DJ ruling: **§5b THE TOOLCHAIN IS PINNED** — `lib_deps` names an EXACT library version (`pololu/Zumo32U4@2.0.1`), never a bare package and never a caret range. This book publishes byte counts against a 28,672 B ceiling with as little as 638 B of headroom; an unpinned dependency is a live hazard, not a style preference. Prior: **v8.22** (v8.22, per S36 DJ rulings: **§15 MAKER REGISTRY & LINK CANON — NEW SECTION** — the §7 ladder is FIVE RUNGS, 7A–7E, and the Maker's kind letters MUST match the lesson's rung letters; `finished` IS the last step, so step_* kinds cover 1..N−1 only; a kind MAY share another kind's payloadRef; the four Maker-link shapes are canon; and the Maker is NOT uniformly formatted — edit by offset, never by line. Prior: **v8.21** (v8.21, per S35 DJ rulings: **§6.5 NAV BUTTON COUNT is 12–14** and **the Image Index has NO nav button** — the pill was removed book-wide; **§6.8 FOUR PART BANNERS, FIVE COLOR GROUPS is REAFFIRMED** — the gray §10+end group carries the group color but NO divider; the "PART 5 — Wrap Up" banner that L10–L16 had invented is retired book-wide. Prior: **v8.20** (v8.20, per S33 DJ rulings: **§9 UNIQUE VERSION PER DELIVERY** (retires the fix-to-a-fixed-version rule) · **§9 image changes are a MINOR bump** · **§10 IMAGE and GRAPHIC are SEPARATE NUMBER SPACES; audit art against `images/`, never against the lesson alone** · **§13 BATTERY CANON — eneloop NiMH** · **§14 ENGINEER'S LOG — 16 prompts, one per lesson**. Prior: **v8.19** (v8.19, per S28+S32 DJ rulings: **16-LESSON RENUMBER SWEEP** — §1 filename table, §3 LESSON MAP, §0 items 5/6 8A map, tier-card example, and image-phase count moved from the 15-lesson to the 16-lesson numbering (L12 "Wheels Lie" inserted S28, shifting Rescue Zone→13, Competition Prep→14, Advanced PID→15, Showcase→16; L11 retitled "Time Lies, Distance Doesn't"; L15 retitled "The Present Isn't Enough" S31; L16 retitled "Nothing Left to Take Away" S32). 8A map re-verified against published files July 13, 2026: PRESENT L02–L15, ABSENT L01 and L16. Renumber only — no rule changes. Prior: v8.18 (v8.18 adds, per S28 DJ ruling: **§11 EXTRACT THE INHERITANCE — DO NOT RECONSTRUCT IT.** A depth pass on lesson N BEGINS by pulling lesson N-1's `finished` payload out of `newproject.html` (`PAYLOADS["N-1"]["finished"]`) — that is the project students actually hold in their hands. Rebuilding the base from lesson HTML, from a sibling lesson, or from memory SILENTLY DROPS FILES. Canonized after S28 reconstructed the L11 base as SIX files, omitting `RobotHelpers.h`/`RobotHelpers.cpp` — the STANDARD HELPERS (`waitForStart()`, `checkBattery()`) that have shipped in EVERY project since Lesson 4 — and built 21 compile-verified states on that broken inheritance before catching it. A student would have opened the lesson project and found their SAFETY GATE GONE. The project is EIGHT files: RobotConfig.h, RobotSensors.h, RobotSensors.cpp, RobotHelpers.h, RobotHelpers.cpp, RobotMotion.h, RobotMotion.cpp, main.cpp. GATE CHECK: assert `len(files)==8` on every state. The 21 states were discarded and rebuilt from the real payload; the corrected base compiles at 22802 bytes, byte-exact to S27's recorded L11 `finished` — which is how provenance was confirmed. THE MAKER REGISTRY IS THE AUTHORITATIVE INHERITANCE SOURCE. Prior: v8.17 (v8.17 adds, per S25 DJ rulings: **§11 A DECLARED STUDENT BLANK MUST BE SPENT** — if a lesson ships a tunable as a blank (`const int TRIM = 0;   // <-- YOUR NUMBER`), the code MUST actually USE that constant. A blank the code never reads is a LIE in the worksheet: the student writes in a number, nothing changes, and they lose faith in the instrument rather than in their own guess. Canonized after S25 found §7B/7C/7D of L10 declaring `TRIM` and never passing it to `setSpeeds()` — the same defect class as L09's false claim that `turnDegrees()` "respects TRIM." GATE CHECK: grep every lesson for declared-but-unread tunables. **BLANK CONVENTION (DJ-ruled S25):** tunables ship as `= 0` with the starting guess in the COMMENT (`const int TURN_MS = 0;   // <-- YOUR NUMBER. Try 400 and work from there.`) — a seeded value looks like an answer and students accept it without hunting; a bare `0` with no hint means the robot does not move and the student has no bracket to start from. **§11 IDENTICAL BYTE SIZES — THE CONSTANT EXCEPTION** — the S22 rule ("identical binary sizes across states = `--gc-sections` discarding dead code") applies to added LOGIC, NOT to changed CONSTANTS. `speed + TRIM` with `TRIM = 0` constant-folds to `speed` and emits byte-identical code; the fix IS live, it simply costs nothing until the blank is filled. Do NOT conclude an edit vanished from a zero byte delta — DISASSEMBLE (`avr-objdump -d`) and read the immediates. S25 proved TRIM live in L10 §7D this way: `ldi r24, 0x96` (150) became `ldi r24, 0x9E` (158) with the right motor unchanged at 150 — same instruction, same size, correct LEFT-motor polarity. Sabotaged-build states that flip a sign or change a constant are the same case. **§11 SABOTAGED BUILDS SHOW THE PLANTED LINE** — Bonus mysteries display the sabotaged code inside the hint ("The planted constant:" / "as planted:"). The mystery is NOT "find the typo" — it is "why does THIS line produce THAT symptom," which is the actual debugging skill. This also satisfies the payload byte-match gate by construction (L09 canon, formalized S25). Prior: v8.16 (v8.16 added, per S23 DJ rulings: **§4 QUICK LINKS RETIRED** — book-wide; navigation canon = section banners + one `↑ Back to top` per section; a Quick Links jump-list duplicates the banners and rots on every renumber (only 4/15 lessons had one; L08/L09 — the freshest depth passes — never did). **§11 TRIM PLACEMENT RULE** — TRIM belongs in every OPEN-LOOP straight line (`driveDistance()`, `handleGap()`, timed maneuvers) and NOWHERE else: NOT in `turnDegrees()` (the wheels oppose on purpose; encoders govern the angle) and NOT in `followLine()` (P-control is a CLOSED loop already correcting bias 50x/sec — TRIM would fight it). Open-loop needs TRIM; closed-loop does not. Polarity is LEFT-motor: `setSpeeds(speed + TRIM, speed)`, positive TRIM speeds the left wheel, robot pushes RIGHT, correcting a LEFT curve — verified against Pololu `FaceTowardsOpponent.ino` (`turnRight()` = `setSpeeds(+turnSpeed, -turnSpeed)`; a robot curves toward its SLOWER track). **§11 ENCODER AVERAGING RULE** — distance/turn loops MUST gate on the average of BOTH encoders, never one: `while (averageCounts() < target)`. Watching a single encoder means a slipping or stiff wheel on the other side ends the move early or late and nothing warns you. **§5b IN-FILE VERSION = MAJOR DIGIT ONLY** — the header/footer "Version N" carries the major digit; the full `v##.#.#` lives ONLY in the filename (canonized after finding L04 shipped with header "Version 3" against footer+filename "4"). Prior: v8.15 (v8.15 added, per S22 DJ ruling: §11 payload-gate INHERITANCE RULE — lesson N's payload corpus additionally includes lesson N−1's `finished` payload bodies, because inheriting lessons copy the prior project wholesale in Step 1. Prior: v8.14.1 (v8.14.1 added, per S21 DJ ruling: §11 dark-wrapper scope check — canonized after the S21 L03 find where a `#1e1e1e` wrapper missing its closer swallowed four Quick Reference tables and passed both div-balance AND the depth walk, because the closer existed ~200 lines late. Prior: v8.14 (v8.14 adds, per S20 DJ rulings: §11 payload byte-match gate — canonized from the S18-approved Maker starter-code-registry rule; §11 bounded-scope replace assert — canonized after the S20 L03 B1/B2 regex incident; §4 "Bonus" vocabulary canon — book-wide term for the extra-practice section, nav labels must match. Prior: v8.13.1 (v8.13 adds: hardware-direction verification against Pololu examples; L04+ STANDARD HELPERS — waitForStart safety gate + A&B battery check; lesson-aware Maker skeleton; web-tool internal versioning. v8.13.1 completes the v8.13 delta: §11 ASCII-sweep checklist item — EDIT 5, dropped in the initial application — plus §5b header tag corrected v8.12→v8.13)))))))))))))))).

---

## ASCII ART POLICY (v8.6 — canon)

**No ASCII-art diagrams anywhere in lesson content.** All diagrams are either Claude-produced SVG (`[GRAPHIC x.y]`) or DJ-sourced raster (`[IMAGE x.y]`).

- Applies to box-drawing/arrow diagrams in `<pre><code>` blocks AND to annotated code-anatomy diagrams (pointer/arrow lines inside code blocks) — those count as ASCII art.
- Replacement mechanism: swap the ASCII block for a `[GRAPHIC x.y] caption` placeholder in the lesson's own dashed-div placeholder format; DJ inserts the SVG file in Canvas.
- Existing ASCII art is converted per the ASCII→SVG tracker in `LIVE_ZUMO_TEXTBOOK.md`.
- Plain code (no drawing characters) in `<pre>` blocks is unaffected.

**MANDATORY DIFF-AUDIT GATE (v8.7).** Before saving any modified lesson file: run a full old-vs-new diff and confirm every changed line is explained by the intended edit — removed lines, added lines, and byte/line-count deltas must all reconcile. Structural checks (anchors, div depth) cannot detect content loss when the deleted content has no inbound links; only a diff can. Rebuild from the md5-verified `/mnt/project/` source, never from a prior working copy. (Canonized after a Session-8 regex overmatch silently deleted ~13KB from L02.)


**The single, definitive source of truth for the Zumo 32U4 Robotics Textbook.**

**Supersedes:** `Zumo_Super_Bible_V7.md` AND `Zumo_Textbook_Standards.md` (both retired). If anything in an older file disagrees with this document, this document wins.

**Last updated:** July 25, 2026 — **v8.58** (Session 72: §4.4 SKELETON CONFORMANCE — the Core 10 are mandatory; a thin section still appears and says so; lesson-unique material folds rather than becoming a new numbered section; "does not apply" stubs everywhere REJECTED on the skip-the-header cost; §8A re-ruled CONDITIONAL, unchanged. L01 and L02 brought into conformance.)

**SVG build-path rule (added v8.11, from the L02 GRAPHIC 2.9 incident):** SVG files must be authored through an escape-processing write path (e.g., Python string → file), NEVER a raw-text path — raw-written `\uXXXX` sequences render as literal garbage text in the diagram. Mandatory SVG QA before presenting: (1) literal-`\u` scan of the saved file must be clean; (2) render the SVG and verify, and when visual preview is unavailable, verify layout numerically (e.g., pixel-scan for overlap in gaps). Corollary for hosted HTML tools (timer, Project Maker): `\uXXXX` escapes are legal ONLY inside JavaScript string literals — the HTML text region must be escape-free (use entities or literal characters).

---

## 0. WHAT CHANGED IN v8 (READ FIRST)

v8 is a **re-baseline**. The previous Bible (v7) and the separate Standards doc had drifted from the actual lessons and from each other (they disagreed on section count and skin). v8 resolves that. The decisions below are LOCKED:

1. **Canonical skin = the "Lesson 9 look" + section CAP+BOX design** (Segoe UI, blue gradient nav/title; every section is a colored cap on a matching bordered box). Defined fully in §6. Supersedes the old v7 serif/flat-nav style guide.
2. **Nav/title gradients are top-down, dark-first** (`linear-gradient(to bottom, <dark> 0%, <light> 100%)`). **PART dividers are now SOLID group colors** (blue/green/rose), not the old navy gradient (retired). **Section cap+boxes and PART banners follow the nav color scheme:** §1–3 blue `#3498db`, §4–6 green `#3a7d5c`, §7/§8/§8A dusty rose `#c45d76`, **§9 plum `#9b6a9e`**, §10+end gray `#6c757d`. (§9 split into its own PART 4 — see §6.8.) **Code blocks are dark** (VS Code/PlatformIO theme, §6.11).
3. **Icon legend = 12 icons** (the set in §6.6), using "⚠️ WARNING."
4. **No icon before the title-block heading** (`LESSON ##`, not `🚧 LESSON ##`). Section headers (`📖 Section 1: …`) keep their icons.
5. **Structure = 10 sections, §8A CONDITIONAL.** 8A is present ONLY when a lesson isolates a genuine reusable coding pattern — it is NOT universal. (See §4.) **8A MAP:** PRESENT in L2–L15. ABSENT in L1 and L16. (Re-verified against every published file July 13, 2026.)
6. **Lessons with no 8A:** L1 (install/setup) and L16 (capstone/showcase). Their PART 3 subtitle = "Sections 7–8: Verify and extend" (no 8A). §9 is still its own PART 4 (plum) in every lesson. A "Functions Reference" subsection can go EITHER way — become §8A OR fold into Quick Reference — author's per-lesson call.
7. **Two spec files → one.** `Zumo_Textbook_Standards.md` is retired; its content is folded here.
8. **Filename convention:** `Lesson_##_Topic_v##.html` — zero-padded lesson number, zero-padded lowercase version. See §1.
9. **Re-baseline version reset (COMPLETE):** at the v8 transition, every lesson reset to `v01` — this one-time reset is now DONE (all 15 lessons built to v8.4, L10–L15 at v01, dates normalized to June 2026). The normal increment-only rule (§9) now applies to ALL lessons. **DO NOT reset any lesson's version or re-normalize dates again — only increment forward.**

---

## 1. FILE NAMING CONVENTION

**Pattern:** `Lesson_##_Topic_v##.html`

- `##` = zero-padded lesson number (`01`, `02`, … `15`)
- `Topic` = fixed topic token (underscores, mixed case) — see table below
- `v##` = zero-padded, **lowercase** `v` + zero-padded version (`v01`, `v02`, …)

**Examples:** `Lesson_01_Hello_Robot_v01.html`, `Lesson_10_Obstacles_v01.html`, `Lesson_16_Nothing_Left_to_Take_Away_v02.html`

**Locked topic tokens (all 15):**

| # | Topic token |
|---|---|
| 01 | `Hello_Robot` |
| 02 | `Read_Code` |
| 03 | `Motors_TRIM` |
| 04 | `Line_Sensors` |
| 05 | `Proximity_Sensors` |
| 06 | `Encoders` |
| 07 | `Code_Organization` |
| 08 | `Line_Following` |
| 09 | `Intersections` |
| 10 | `Obstacles` |
| 11 | `Time_Lies_Distance_Doesnt` |
| 12 | `Wheels_Lie` |
| 13 | `Rescue_Zone` |
| 14 | `Competition_Prep` |
| 15 | `The_Present_Isnt_Enough` |
| 16 | `Nothing_Left_to_Take_Away` |

The old `_Rebuilt_` / `_Canvas` / `_StandardCallouts_StickyNav` suffixes are **retired**. All files move to the clean pattern above at the v8 re-baseline.

---

## 2. CURRICULUM PHILOSOPHY (unchanged from v7)

- **Depth before breadth.** Each concept fully developed before moving on.
- **Coach voice.** Friendly, professional, "B-level" explanations. No flattery.
- **Theory-first, then scaffolded build.** Theory section is pre-reading; Build It is hands-on.
- **Progressive autonomy.** Each lesson copies the previous project folder and adds one capability.
- **Audience:** high school freshmen, zero coding experience. Platform: PlatformIO + VS Code (not Arduino IDE).
- **Information density:** "more is better" — comprehensive over simplified.

---

## 3. LESSON MAP

| # | Topic | 8A? |
|---|---|---|
| 01 | Hello Robot | ❌ none (intro/setup) |
| 02 | Read Code Like a Pro | ✅ yes (Functions) |
| 03 | Motors & TRIM | ✅ yes (Calibration) |
| 04 | Line Sensors | ✅ yes (Sensor Arrays) |
| 05 | Proximity Sensors | ✅ yes (Sensor Pairs) |
| 06 | Encoders | ✅ yes |
| 07 | Code Organization | ✅ yes |
| 08 | Line Following (P-Control) | ✅ yes |
| 09 | Intersections & Dead Ends | ✅ yes |
| 10 | Obstacles | ✅ yes (Sub-States) |
| 11 | Time Lies, Distance Doesn't | ✅ yes (Dead Reckoning) |
| 12 | Wheels Lie | ✅ yes |
| 13 | Rescue Zone: Flying on Instruments | ✅ yes |
| 14 | Competition Prep | ✅ yes |
| 15 | The Present Isn't Enough (PID) | ✅ yes (Concepts) |
| 16 | Nothing Left to Take Away (capstone) | ❌ none (capstone; §9 = tier-cards) |

---

## 4. LESSON STRUCTURE — LOCKED

**Vocabulary canon (v8.14, DJ-ruled S20): the extra-practice section is called "Bonus"** — book-wide, in section headers, nav pills, Maker dropdown group labels, and prose. "Enrichment" and "Extra Practice" are rejected alternates; any nav label pointing at the Bonus section must read "Bonus" (an L02 nav pill reading "Extra Practice" was the drift that triggered this ruling).

### Core 10 sections (every lesson)

1. **Intro** — engaging problem/scenario that motivates the lesson
2. **Objectives** — learning objectives checklist
3. **Theory** — background concepts, subsections 3.1, 3.2, … (lesson-specific design concepts live here)
4. **Hardware** — physical setup, sensor specs, calibration notes
5. **Code** — walkthrough of key functions/concepts (project org, constants/functions tables, function reference)
6. **Build It** — step-by-step implementation with checkpoints
7. **Test** — verification checklists, tuning guide
8. **Troubleshoot** — problem/cause/solution
9. **Challenges** — Easy/Medium/Hard escalation with collapsible solutions
10. **Exit Ticket** — 3-h4 structure (see §7)

**All ten are MANDATORY in every lesson — see §4.4.** A section whose job comes up thin this lesson still appears and says so (§4 Hardware in a lesson that adds no parts). Lesson-unique material folds into the nearest section rather than becoming a new numbered one. §8A is the one CONDITIONAL section (below).

**End matter (after section 10):** Glossary → Quick Reference → Image Index. Headings use the locked icon set: **📖 Glossary**, **⚡ Quick Reference**, **🖼️ Image Index** (border `#6c757d`).

**Glossary entry format (LOCKED):** each glossary term is a **term card** — `<div style="background-color: #e7d4ff; border-left: 4px solid #9b59b6; padding: 15px; margin: 15px 0; border-radius: 8px;">` then `<span>🔑</span> <strong id="term-...">Term</strong> — definition.` This is the ONE canonical glossary palette/format. Do NOT use Key-Term-callout purples (`#f3e5f5`/`#9c27b0`) or any other purple (`#f3e8f9`/`#7b2d8e` etc.) for glossary entries — those drifted across L1/L2 and were normalized. Term cards stay `8px` (the radius exception); inline Key Term *callouts* in the body remain `#f3e5f5`/4px and are a different element.

### Section 8A (CONDITIONAL — only when a reusable coding pattern exists)

8A houses a **reusable coding pattern** — something a student will reuse in later lessons (function parameters, return values, error handling, state machines, non-blocking timing, etc.). It is distinct from Theory: Theory holds lesson-specific *design* concepts; 8A holds transferable *code* patterns.

**Rules when 8A is present (L2–L15):**
- Placed **between Section 8 (Troubleshoot) and Section 9 (Challenges)** in DOM order.
- Appears in nav as a button ("8A. Concepts" or similar), dusty rose color `#c45d76`.
- 8A is part of **PART 3** (dusty rose, with §7/§8). PART 3 subtitle = "Sections 7–8A: Verify and extend". (§9 is now its own PART 4 in plum — see §6.8.)
- `<h2 id="section-8a">` carries the dusty rose color `#c45d76` (8A stays rose; only §9 moved to plum).
- Section ID order: `1, 2, 3, 4, 5, 6, 7, 8, 8a, 9, 10, glossary, quick-ref, image-index`.

**Presence rule (CONDITIONAL):** 8A is present ONLY when a lesson isolates a genuine reusable coding pattern — NOT in every lesson. **8A MAP:** PRESENT in L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12; ABSENT in L1, L13, L14, L15. (L2–L5 verified present July 2, 2026.) Lessons without 8A use PART 3 subtitle "Sections 7–8: Verify and extend". §9 Challenges (PART 4, plum) is present in every lesson including those without 8A. A "Functions Reference" may become §8A (L12) OR fold into Quick Reference (L14) — author's per-lesson call.

### Theory (§3) vs Build It (§6) — the "Build It" approach

Explanation is immediately followed by implementation (not separated into distant sections). This is intentional, not a deviation.

---


### 4.1 THREE CONSTRUCTS, THREE NAMES — "CHALLENGE" MEANS ONE THING (v8.46 — NEW, S65)

The book contains three different graded-or-practice constructs. **Only one of them is called a Challenge.**

| Construct | Name | Look | Numbering |
|---|---|---|---|
| §6.12 challenge card | **Challenge N: Title** | canonical shell, split pill, `data-reveal="solution"` | `N.n` |
| Section 1 warm-up | **Warm-Up N: Title** | plain `<h3>`, blue `#2e86ab`, timer | `N.wn` |
| Inline practice box | **TRY IT (n minutes)** | green `#e8f3ec` box, inside a build step | `N.tn` |
| End-of-lesson extra | **Bonus Challenge N: Title** | purple gradient card | shares card numbering — see below |

**Why this rule exists.** L02 shipped with warm-ups numbered 1–4 *and* Bonus Challenges numbered 1–6, both
called "Challenge N". "Did you finish Challenge 3?" had three defensible answers, and the AI Tutor — which
queries `[data-challenge]` — could only see the Bonus set, so a student asking about a warm-up got the wrong
card. Renamed S65.

**"Bonus Challenge" keeps its number even where it duplicates a card number** (L02 and L03 both run cards 1–6
and Bonus 1–6). The qualifier disambiguates, this is the established convention in both lessons that have
Bonuses, and §4's "Bonus" vocabulary canon already reserves the word. Do not renumber them.

**The marker suffix carries the type.** `w` = warm-up, `t` = TRY IT, bare digit = canonical card. A warm-up
and a card can therefore never collide in the picker even when they share a display number.

### 4.2 EVERY PRACTICE CONSTRUCT IS TAGGED (v8.46 — S65, extends §20.2)

§20.2 requires `data-challenge` on every challenge. **S65 extends it to warm-ups and TRY IT boxes**, and adds
`data-kind` (`warmup` / `tryit`) so the tutor can tell them apart from a graded card. An untagged practice
construct is invisible to the picker — the student can see it on the page and the tutor cannot.

Audited book-wide S65: only **L02 (15 untagged)** and **L04 (1)** had gaps; both closed. L11 carries 4 markers
above its pill count — those are `data-kind="mystery"` constructs and are correct. **104 unique markers
book-wide, zero duplicates.**


### 4.3 THE PICKER LABEL IS THE ELEMENT'S OWN TEXT (v8.47 — S65, learned the hard way)

`tutor.html` builds each dropdown option from the tagged element's `textContent`, truncated to 60 chars.
**So the tagged element must name itself.** S65 tagged eleven L02 TRY IT boxes whose text was only
`🎯 TRY IT (1 minute)` — six were byte-identical in the dropdown and a student had no way to pick the right
one. The tagging was correct and the labels made it unusable.

**Rule: before tagging a construct, read what its `textContent` will say on its own, out of context.** If two
tagged elements in one lesson can produce the same string, the label is wrong. Give it a scope — the step it
belongs to, or the task it names: `🎯 TRY IT — Step 5: Longer Blink (1 minute)`.

**`data-kind` drives the optgroup.** The picker groups Challenges / Warm-Ups / Try It / Mysteries. A unit with
**no** `data-kind` is treated as a canonical challenge card — that is the book's default and the majority
case, and it must stay that way so the 14 untouched lessons keep working. Any unrecognized kind falls into an
"Other" group rather than being dropped; nothing tagged is ever invisible.

### 4.4 THE SKELETON IS MANDATORY — A THIN SECTION STILL APPEARS (v8.58 — NEW, S72, DJ-ruled)

The Core 10 list above is not a menu. **Every lesson carries §1–§10, in order, with each number
keeping the job the list gives it.** This was always the intent; it was never enforced, and two
lessons drifted off it unnoticed for the life of the book.

**RULE 1 — a skeleton section whose job comes up thin STILL APPEARS, and says so.** §4 Hardware is
the live case: a lesson that introduces no new parts does not delete §4, it opens §4 by saying so
and recapping the parts today's code will touch. The *job* of §4 — orient the student to the
hardware in play — fires in every lesson, including the ones that add nothing. A thin section is
honest; a missing section breaks the map.

**RULE 2 — lesson-unique material does NOT get its own numbered section.** It folds into the
nearest skeleton section. L02's "Make It Yours" (optional customizations, ⭐-rated) was §9
Challenges content wearing a section banner; it folds into §9. Inventing a numbered section for
one lesson's content forces the other fifteen to either carry a stub or break the map — both
worse than folding.

**WHY NOT STUB EVERY SECTION EVERYWHERE (rejected alternative, S72).** DJ raised making all
sections universal with "does not apply to this lesson" placeholders. Rejected on a pedagogy
cost: empty sections train students to skip section headers, and in a flipped course where the
reading is the gate (§25.3), a student who meets "does not apply" three times in L01 is skimming
headers by L04. Placeholder text is for a *recurring job that came up empty*, never for content
another lesson happened to have.

**§8A REMAINS CONDITIONAL** (DJ re-ruled S72, no change): present only where a genuine reusable
pattern exists, ABSENT in L1 and L16. 8A is not part of the mandatory skeleton and takes no
placeholder.

**THE TWO NON-CONFORMANT LESSONS (L01 fixed S72 · L02 cut S73):**

| | Was | Now | Cost |
|---|---|---|---|
| **L01** | §4 = *Install the Tools*; no hardware section anywhere in the lesson (Button A appears 0× in §3, encoder 0× in the whole file) | §4 covers both jobs, opening with a *Meet Your Robot* block naming the parts L01's code touches | title + a block; **no renumber** — L01's §5/§6 already matched |
| **L02** | §3 carried the code walkthrough (§5's job), §4 was prep, the build sat at §5, and a unique §6 "Make It Yours" pushed everything one ahead | §3 Theory · §4 Hardware · §5 The Code · §6 Build It; "Make It Yours" folded into §9 | full renumber, **major re-baseline v03.0.0** |

**A CONFORMANCE DIVIDEND.** §15.2 is worded *"If Section 6 has N steps, the Maker carries
`step_1` … `step_N-1`"* — the Maker's step model assumes the build is §6. That was false for L02
alone. Renumbering made the existing wording true book-wide instead of patching the rule to
accommodate one lesson. **When canon and a file disagree, check which one is the outlier before
rewording the canon.**

**AUTHORING NOTE — splitting a section is not reordering its ideas.** L02's §3 split put the C++
concepts (data types, `if`, `&&`/`||`, the Two-Week Rule, pitfalls) ahead of the anatomy
walkthrough, reversing how L02 had taught them. That was safe *because the concepts are
prerequisites for the BUILD, not for the anatomy*, and because students have already read a
complete program in L01 §5 — so nothing lands out of dependency order. The seven-section
**diagram** stayed at the top of §3 as orientation even though its walkthrough moved to §5: the
lesson tells students to print it and keep it visible, so it is a navigational aid, not §5
content. Check dependency order before moving a subsection, not just section membership.

## 5. CODE STANDARDS (unchanged from v7 — summary)

- **6-file project architecture:** `main.cpp`, `RobotConfig.h`, `RobotSensors.h/.cpp`, `RobotMotion.h/.cpp`.
- **Hardware objects** defined once; use `extern` elsewhere. `Zumo32U4OLED` (not `Zumo32U4LCD`).
- **`#define` for pin numbers only; `const` for all other values.** camelCase enforced (`baseSpeed`, `lineLostTime`).
- **Serial baud rate: 115200.** Include `Serial` timeout guard in `setup()`.
- **Single sensor read per loop** — store raw values once at loop top, reuse. Multiple `lineSensors.read()` calls (~12–15ms each) cause green-tape detection failures.
- **Non-blocking timing only** — never `delay()` in a state machine; use `millis()` timers. (This is the L10 8A topic.)
- `followLine()` lives in `main.cpp` only.
- A-Star32U4 capitalization for the microcontroller.
- **Function prototypes (v8.12 — MANDATORY):** helpers live at the BOTTOM of `main.cpp` (anatomy Section 7); every helper gets a one-line prototype in a `// ===== FUNCTION PROTOTYPES =====` block right after the hardware objects. PlatformIO `main.cpp` is real C++ — no `.ino` auto-prototypes; define-below-loop without a prototype DOES NOT COMPILE. Teaching pattern = deliberate break-fix (L02 STEP 7).
- **Native-USB serial canon (v8.12):** the Zumo's `Serial` is USB CDC — the baud number in `Serial.begin()` is effectively ignored; a mismatch does NOT produce garbage on this robot (that's UART boards like the Uno). NEVER teach baud-mismatch gibberish as a Zumo symptom. Print-at-boot is invisible (reset drops the USB port) — prints go in `loop()` or behind a button press. We still write `Serial.begin(115200)` as professional habit.
- **Compile-verify mandate (v8.12):** every new or changed lesson code block (steps, final programs, challenge solutions, bonus snippets, template skeleton) must compile on the AVR harness before delivery. Harness: avr-gcc + `arduino/ArduinoCore-avr` + `pololu/zumo-32u4-arduino-library` + deps (Pushbutton, FastGPIO, PololuBuzzer/HD44780/Menu/OLED, USBPause, core Wire), Leonardo-class env, `-mmcu=atmega32u4 -DF_CPU=16000000L`. Rebuild from GitHub clones each session. A lesson whose build sequence never compiled shipped twice (L02 ≤ v02.0.6) — this rule exists so it can't happen a third time.

---


**HARDWARE-DIRECTION VERIFICATION (v8.13 — after the L03 TRIM-inversion incident).** Any claim that maps left/right, forward/backward, or turn direction to motor commands MUST be verified against the Pololu library's own example code before it ships — e.g., `FaceTowardsOpponent.ino` implements `turnLeft()` as `setSpeeds(-turnSpeed, turnSpeed)` (right faster ⇒ turns LEFT; a robot always curves toward its slower track). A lesson that is internally consistent can still be physically backwards — L03 taught inverted TRIM logic for its entire life until S15. Internal consistency is not verification; the library examples are ground truth Claude can check without hardware.

## 5b. STUDENT PROJECT WORKFLOW & WEB TOOLS (v8.13 — LOCKED)

**Template workflow:** `ZUMO_Template/` lives in `Documents/PlatformIO` — built by students at the END of L01 (block canon in L01 v03.0.23), never worked in, only copied. Contents: canonical `platformio.ini` + skeleton `main.cpp` (header stub, all section banners incl. FUNCTION PROTOTYPES, empty setup/loop) + README ritual. Rescue copy = `ZUMO_Template.zip` at repo root.

**Start-a-New-Lesson ritual (standard §4 block, EVERY lesson L02+):** 1) Project Maker → download 2) unzip into Documents/PlatformIO 3) VS Code File→Open Folder (close old folder first) 4) header comment check (Maker pre-fills; update WHAT-THIS-DOES as you build) 5) Build ✓ health check. Manual fallback: copy template + rename by hand. iCloud caution: keep the PlatformIO folder downloaded/local.

**Naming canon (DESCRIPTIVE — supersedes `LastName_Lesson_##` and all letter-suffix schemes):**
- Main lesson build: `LastName_L##` (zero-padded; first initial for duplicate last names: `SmithJ_L02`; NO SPACES ever)
- Mystery sandbox: `LastName_L##_Mystery` — ONE per lesson, reused across its mystery challenges
- Challenge/bonus copies: `LastName_L##_<Challenge_Name>` (e.g. `Smith_L02_The_Broken_Code`, `Smith_L02_Blink_Count`)
- Copy per LESSON, never per step. Additive §9 challenges work in the main build; code-replacing challenges and bonus snippets get their own copy. Every challenge card carries a "📁 Work in:" line naming the exact destination, with a Maker deep link when a new folder is needed.

**Web tools (GitHub Pages, weymuth.github.io/zumo/) — Canvas strips `<script>`, `onclick=`, `<style>`, `class=`; ALL interactivity ships as Pages-hosted iframes:**
- `timer.html` — horizontal bar countdown (336×56 right-float, `?min=&label=`, cache-bust `?v=N` on every timer redesign). One per timed challenge.
- `newproject.html` — ZUMO Project Maker: generates correctly-named project zips with pre-filled header comments. Carries a per-lesson challenge registry — **EXTENDING the registry is a mandatory step of every lesson depth pass.** Deep-link format: `?lesson=N&kind=<slug>`.
- Printable graphics: PDF generated from the approved SVG, hosted in repo `images/`, linked via a styled download button in the lesson (this SUPERSEDES dedicated "printable version" GRAPHIC slots — L02 GRAPHIC 2.3 precedent).

**Sketch anatomy canon:** **7 numbered sections + one UNNUMBERED "FUNCTION PROTOTYPES" row** between Constants and setup() (dashed rail marker in GRAPHIC 2.5; color key shows it as an open square in Helpers blue). The count stays "seven sections" book-wide — do NOT renumber to eight.

---

### STANDARD HELPERS — L04+ (v8.13 — LOCKED)

From Lesson 04 onward, every Maker-generated skeleton (all kinds: main, challenge, custom) ships with a **STANDARD HELPERS (added after Lesson 3)** block at the file bottom, with prototypes declared in the FUNCTION PROTOTYPES section (the template itself models the L02 layout canon). Lessons 01–03 stay clean — those lessons teach the pieces. The two helpers, compile-verified (13,002 B on the harness):

- **`waitForStart()`** — SAFETY GATE. OLED shows "Press A / to start"; `buttonA.waitForButton()`; clear + `delay(500)` to get hands clear. Called at the END of `setup()`, always. **Canon rule: from L04 on, no driving program ever moves at power-on — motion waits for a button press.** Depth passes on L04–L15 must adopt this in their main builds.
- **`checkBattery()`** — A+B BATTERY CHECK. Hold Buttons A + B together at any time: OLED shows battery millivolts while held, waits for release, clears. Called at the TOP of `loop()`. **Canon rule: A+B held = battery check, book-wide from L04.** No permanent screen space is reserved for battery (supersedes any row-0 reservation idea). Uses only L03 knowledge (combo-press pattern = L03's A+C reset precedent).

Manual fallback ritual for L04+ (no internet): copy ZUMO_Template, rename to `LastName_L##`, **and paste the STANDARD HELPERS block** (lessons provide it in a copyable dark box during their depth passes). `ZUMO_Template.zip` itself stays the clean L01 version — it is the teaching artifact.

### THE TOOLCHAIN IS PINNED (v8.23 — LOCKED, S36)

**`lib_deps` names an EXACT version. Never a bare package name. Never a caret range.**

```
lib_deps = pololu/Zumo32U4@2.0.1
```

**Why this is a rule and not a preference:** this book publishes **exact byte counts** — L15 ships at 28,034 B against a **28,672 B ceiling, 638 B of headroom**. A library update that adds a few hundred bytes to Pololu's code does not merely make a figure stale; it pushes a student's build **over the wall**, while the lesson insists the number should have fit. An unpinned dependency silently invalidates every byte in the book.

**Why EXACT and not `^2.0.1`:** the caret means `>=2.0.1, <3.0.0`. A future 2.1.0 would satisfy it and land silently — which is the exact drift the pin exists to prevent. `~2.0.1` is better (patch-only) and still not tight enough. Take the exact version; when a real update lands, change the number **deliberately** and re-audit the bytes.

**IN-FILE VERSION — TWO DURABLE HOMES (v8.31, REVERSES the old major-digit-only rule).** The published filename is stable `Lesson_NN.html` (no version), so the version must live INSIDE the file — in two places, at two precisions:
1. **VISIBLE banner** (the header hero, line 5): **major.minor only**, e.g. `Version 03.2` / `v03.2`. It updates on a MODERATE-or-larger bump and is deliberately LEFT ALONE on a minor/cosmetic bump — so a pill recolor (`v03.2.4 → v03.2.5`) does NOT touch the visible banner.
1b. **HIDDEN BUILD BANNER (v8.53, S70 — SUPERSEDES the v8.44 "both visible homes" rule).** The SECOND banner home moved out of the student-visible footer into an HTML comment immediately before `</body>`, carrying the same **major.minor** plus the date and the page title:
```
<!-- ===== BUILD BANNER (hidden from students; keeps the §5b two-homes gate honest) =====
     Version 03.8 &mdash; July 2026 &bull; LESSON 01 · Sense, Decide, Act
     ZUMO Callout Standard v1.0 Applied
===== -->
```
DJ ruling S70: the footer belongs to the reader, not the build system. The two-homes gate is UNCHANGED and needed no edit — it greps raw source, and raw source includes comments, so a comment satisfies it exactly as a rendered banner did. This is strictly better than what it replaces: a visible footer number can rot in front of students, a hidden one cannot. Present in all **17** pages (16 lessons + `going_deeper.html`).
2. **HIDDEN HTML comment**, first line of the file: **full three-digit**, e.g. `<!-- Lesson version: v03.2.5 -->`. Updated on EVERY delivery (it is the authoritative in-file record). Greppable: `grep -o 'Lesson version: v[0-9.]*'`.

WHY: with a stable filename and a major-only banner, the exact minor version was recorded ONLY in LIVE.md. When LIVE.md corrupted (S45), L11–L16's true minor became unrecoverable from the repo — the deep clone could only reach a git-rename FLOOR. The hidden comment ends that single-point-of-failure. GATE at close: assert the hidden comment, the visible banner's major.minor, and LIVE.md all agree.

**The registry, as of S36 (July 2026):** `pololu/Zumo32U4` has exactly **two** versions — 2.0.0 and **2.0.1 (latest, published 2022-09-07)**. GitHub tags agree and stop at 2.0.1. **There is no 2.1.0 and there never was.** The library ships only `library.properties` (Arduino manifest); there is **no `library.json`**.

**HOW TO CHECK — never guess a version number:**
```
pio pkg show pololu/Zumo32U4
```
This prints the registry's real version list. Canonized after S36: L01's §8 troubleshooting table had recorded a real `UnknownPackageError` on a `^2.1.0` pin — a **typo**, since 2.1.0 never existed — and the "fix" the book published for it was **"Remove the version pin."** That advice traded a typo for a permanent hole, and the fleet ran unpinned for a year. **A bad pin is fixed by pinning correctly, never by unpinning.** L01 now teaches this.

**GATE CHECK:** grep the Maker's `var INI` template and every lesson `<pre>` showing `platformio.ini` — the `lib_deps` line must be byte-identical everywhere and must carry an `@version`. (S36 also found L01's two `platformio.ini` code blocks disagreeing with each other: one inline, one split across two lines. Both are legal ini; only one matched what the Maker actually writes.)

### WEB-TOOL VERSIONING (v8.13 — LOCKED)

Web tools (`timer.html`, `newproject.html`, future tools) keep **unversioned filenames** — lesson deep links and iframes depend on them. The version lives ONLY inside: a header comment with the full version chain, plus a small visible footer line where layout allows (Maker shows "Project Maker v1.3"). The `?v=N` query token in lesson iframe URLs is a **cache-buster, not a version** — it bumps on every push and drifts from the internal version by design. Versions follow the standard scheme (v# / v#.# / v#.#.#) and are tracked in LIVE's web-tools line.

**THE VERSION LINE IS THE FIRST LINE (v8.54, S70).** Every web tool opens with a greppable canonical comment before `<!DOCTYPE html>` — `<!-- Timer version: v1.3.0 -->`, `<!-- Maker version: v2.45.1 -->`, `<!-- Tutor version: v1.0.0 -->`, `<!-- Index version: v1.3.0 -->` — matching the lesson convention. Gated: `§5b web tools carry an in-file version line` (book_gates v1.5).

WHY, and it is not theoretical: the sentence this replaces read *"Current: timer v1.2, Maker v1.3"* while the Maker was actually at **v2.45** — the Bible carried a number forty releases stale, and `timer.html` and `tutor/tutor.html` carried **no in-file version at all**, the exact single-point-of-failure §5b exists to close. Worse, `newproject.html`'s changelog block OPENS with `v2.18`, the original release, so a naive grep of its head returned a number 27 releases stale — the **v3.0 ghost** trap in its purest form. **Never record a tool version in Bible prose; record that the file carries it, and grep the file.** `sort -V`, never `sort -u`.

**Baselines, honestly labelled.** timer v1.3.0 and index v1.3.0 succeed the last recorded v1.2 / v1.2.1; tutor v1.0.0 is a declaration, since no number for it existed anywhere. Each file's own header comment says which it is. A baseline that admits it is a baseline is recoverable; one that poses as recovered history is not.

## 6. CANONICAL SKIN (v8 — LOCKED) — "THE LESSON 9 LOOK"

> This section **supersedes** the entire v7 "HTML Style Guide" (v7 §6). The old serif body, flat `#2c3e50` nav, `135deg`/`to right` gradients, and Part-colored dividers are **retired**. Reference implementation for the skin: `Lesson_09` (as rebuilt). All lessons conform to this.

**All styling is true inline** — every element carries its own `style=""`. No `<style>` blocks, no CSS classes (Canvas strips them).

### 6.1 Body

```html
<body id="top" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.7; max-width: 900px; margin: 0 auto; padding: 20px; color: #333; background-color: #fafafa;">
```

- Font: **Segoe UI** sans-serif stack (NOT Georgia/serif).
- Background: `#fafafa`.
- `id="top"` on the body so "Back to top" links resolve to `#top`.

### 6.1a Two-column layouts must be responsive (LOCKED v8.3)

Any side-by-side two-column comparison (e.g. `.h` vs `.cpp`, MISTAKE vs CORRECT, BEFORE vs AFTER) MUST use a self-stacking grid — NOT a fixed `1fr 1fr`. Canvas strips `<style>`, so no media queries; use `auto-fit` + `minmax` instead, which stacks to a single column on narrow screens with pure inline CSS:

```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">
```

- **Banned:** `grid-template-columns: 1fr 1fr;` — forces 2 columns at every width and overflows the right border on phones/narrow panels (dark code blocks don't shrink).
- **Required:** `repeat(auto-fit, minmax(280px, 1fr))` — 2 columns when there's room (≥~580px), auto-stacks to 1 column when narrow.
- Flex two-column layouts must carry `flex-wrap: wrap` for the same reason.
- §11 check: FAIL if any `grid-template-columns: 1fr 1fr` (or other fixed multi-column track list without `auto-fit`/`minmax`) exists.

### 6.1b Back-to-top links (LOCKED v8.3.1)

Every section (and end-matter section) carries exactly ONE "Back to top" link at the end of its box, right before the box-closing `</div>`:

```html
<p style="text-align: right;"><a href="#top" style="color: #2e86ab;">↑ Back to top</a></p>
```

- **Standard link color: `#2e86ab`.** (Some lessons historically used `#3498db`; normalize to `#2e86ab` on next touch.)
- Exactly one per section — no strays mid-section, none missing. Insert via a depth-aware walk (each section box from open to its matching close), not a fragile "nearest `</div>`" search.
- Target is `#top` (the `id="top"` on `<body>`).


### 6.2 Gradient rule (applies everywhere)

**All gradients are top-down, dark color first:** `linear-gradient(to bottom, <DARK> 0%, <LIGHT> 100%)`. No `135deg`, no `to right` — **except** challenge-card and milestone headers, which keep their original `135deg` / `to right` (see §6.2a + §6.12).

### 6.2a Gradient vs. Solid — by ELEMENT ROLE (LOCKED)

Whether an element is a gradient or a flat solid is determined by its **role**, not flattened globally:

- **Gradient (hero / header elements):** the sticky **nav bar**, the **title block**, **challenge-card headers** (§6.12), and **milestone headers**. These are one-off or attention-anchor headers.
- **Solid (section-system elements):** **section caps**, **PART banners**, **nav buttons**, and **section-marker pills**. Anything that repeats as part of the per-section grid is flat solid.

Rule of thumb: if it's a *page/section header or a challenge/milestone announce-bar*, gradient is allowed; if it's part of the repeating section skin, it's flat solid. (This is why a §9 cap is solid plum but a §9 challenge-card header is a plum gradient — and that visible light/dark difference is intentional, not a bug.)

### 6.3 Sticky Navigation Bar

```html
<nav style="background: linear-gradient(to bottom, #1a5276 0%, #2e86ab 100%); border-radius: 10px; padding: 15px 20px; margin-bottom: 30px; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
    <div style="display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; align-items: center;">
        <a href="#section-1" style="color: white; text-decoration: none; padding: 5px 12px; border-radius: 4px; font-size: 0.85em; background-color: #3498db;">1. Intro</a>
        <!-- … one per section … -->
    </div>
</nav>
```

**Nav button colors (by section):**
- Sections 1–3: `#3498db` (blue)
- Sections 4–6: `#3a7d5c` (evergreen)
- Sections 7, 8 **and 8A**: `#c45d76` (dusty rose)
- **Section 9 (Challenges): `#9b6a9e` (plum)** — its own color, split out of the old rose group
- Section 10 + Glossary + Quick Ref + Image Index: `#6c757d` (gray)

**Nav button count:** 12–14. Base = §1–10 + Glossary + Quick Ref (12); +1 if 8A present; +1 if Bonus present. **The Image Index has NO nav button** (DJ ruling, S35) — the section still exists and still wears gray `#6c757d`, but students do not navigate to it. L01 = 12 (no 8A, no Bonus) · L16 = 13 (no 8A) · L02–L15 = 14.

### 6.4 Title Block (gradient banner, NO leading icon)

```html
<div style="text-align: center; padding: 40px 20px; background: linear-gradient(to bottom, #1a5276 0%, #2e86ab 100%); color: white; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 5px 20px rgba(0,0,0,0.15);">
    <h1 style="margin: 0; font-size: 2.4em; color: white;">LESSON 10</h1>
    <div style="font-size: 1.3em; opacity: 0.95; margin-top: 8px;">Obstacles: Teaching Your Robot to Navigate Roadblocks</div>
    <div style="font-size: 1em; opacity: 0.9; margin-top: 8px;">Zumo 32U4 Robotics • PlatformIO Edition</div>
    <div style="font-size: 0.9em; opacity: 0.8; margin-top: 5px;">Version 1 — June 2026</div>
</div>
```

- `<h1>` is **`LESSON ##` with NO leading emoji.**
- Four lines: LESSON ##, descriptive title, series line, version line.

### 6.5 Section Headers — CAP + BOX (LOCKED)

Every section (and every end-matter block: Glossary, Quick Reference, Image Index) is a **colored cap on a matching bordered box.** The cap holds the title in white; the box wraps that section's content. The old plain `<h2>` heading style (`#1a5276` text + bottom border) is **retired**.

```html
<div style="background-color: #3498db; color: white; padding: 13px 18px; border-radius: 8px 8px 0 0; margin-top: 24px;">
    <div id="section-1" style="font-size: 1.15em; font-weight: bold;">📖 Section 1: The Roadblock</div>
</div>
<div style="border: 2px solid #3498db; border-top: none; border-radius: 0 0 8px 8px; padding: 18px; margin-bottom: 16px;">
    … section content …
    <p style="text-align: right;"><a href="#top" style="color: #3498db;">↑ Back to top</a></p>
</div>
```

- **Cap:** solid PART color, white bold title (≈1.15em), rounded top only (`8px 8px 0 0`), `margin-top: 24px`. The `id` lives on the inner title div (anchor target).
- **Box:** `border: 2px solid <PARTcolor>; border-top: none; border-radius: 0 0 8px 8px; padding: 18px; margin-bottom: 16px`. Caps the section content; back-to-top link sits inside.
- **Section-group colors (match the nav buttons):** §1–3 `#3498db` blue · §4–6 `#3a7d5c` green · §7/§8/§8A `#c45d76` dusty rose · **§9 `#9b6a9e` plum** · §10 + Glossary/Quick-Ref/Image-Index `#6c757d` gray. Each group owns ONE color; every element in it (cap, nav button, PART banner, challenge cards, table headers in that section) wears that color.
- **Cap KEEPS the leading icon** (`📖 🔨 ▶️ ⚠️ 🔑 🏆 📋` etc.); only the title-block h1 has no icon.
- The cap `id` must match the visible "Section N:" label and the nav anchor.
- **Sub-headings + table headers adopt the SECTION GROUP COLOR** (LOCKED — supersedes the old global blue h3 / navy table-header). Each section's internal headings and table headers wear that section's color:
  - **h3** (subsections, e.g. "5.3 …") → the section group color (§1–3 `#3498db`, §4–6 `#3a7d5c`, §7/8/8A `#c45d76`, §9 `#9b6a9e`, §10+end `#6c757d`).
  - **h4** (sub-subsections) → also the section group color (same as h3 — NOT a separate green).
  - **Table headers** (the `<th>`/header row) → a DARKER shade of the section color (see table below).
  - **Exception:** callout-internal headings (e.g. Exit Ticket h4s inside callouts, Icon Guide h3) keep their callout styling — exempt from this rule.
  - (h2 is no longer used for section titles — the cap replaces it.)

**Section color → darker table-header shade (LOCKED):**

| Group | Section color (cap, h3, h4, nav) | Darker table-header shade |
|---|---|---|
| §1–3 | `#3498db` blue | `#1a5276` |
| §4–6 | `#3a7d5c` green | `#2a5a42` |
| §7/8/8A | `#c45d76` rose | `#9a4459` |
| §9 | `#9b6a9e` plum | `#704c73` |
| §10 + end | `#6c757d` gray | `#4d5358` |

(The old `#2e86ab` global-blue h3 and `#1a5276` global-navy table header are retired except where blue IS the section color, i.e. §1–3.)

### 6.5a THE LESSON STRIP (v8.52 — S69, DJ ruling: "Love c")

Every lesson's sticky nav carries a **second, thinner row**: sixteen numbered squares 01–16 linking to `Lesson_NN.html`, a leading small-caps "LESSON" label, and a trailing `&#8962;` home square to `../index.html`. The row sits inside the same `<nav>`, below the section pills, separated by `border-top: 1px solid rgba(255,255,255,0.25)` with `margin-top: 10px; padding-top: 9px`. Squares: `padding: 2px 7px; background-color: rgba(255,255,255,0.14); border-radius: 4px; font-size: 0.78em; color: white`, each carrying the lesson's canonical title as a `title=` tooltip. The current lesson renders as a **solid white square** (`#ffffff` background, `#1a5276` bold text).

**The block is ONE byte-identical unit in all 16 lessons — never hand-varied.** All sixteen files carry the same static links (so the strip works without JavaScript), and a small self-hydrating script derives the current lesson from `location.pathname` at load and swaps that square to the highlight. Bound by marker comments `<!-- LESSON STRIP v1 (§6.5a) -->` … `<!-- /LESSON STRIP -->`; a renumber or an L17 is one edit to the block re-applied everywhere. **Gate:** `§6.5a lesson strip present and byte-identical in all 16` (book_gates v1.3, control-run S69 against the pre-strip clone where it FAILED with 16 missing, and against an injected one-character drift where it FAILED as "differs").

**The strip does NOT count against the §6.5/v8.21 nav-button ceiling (12–14).** That ceiling governs the section-pill row; the strip is a separate chrome row in the neutral rgba-white family precisely so it never collides with the section color code.

**Callout / radius tiers (LOCKED — two-tier "notes vs. frames"):**
- **Inline content callouts** (border-left accent notes: tip, warning, key term, checkpoint, do-this-now, insight/learn) → **`border-radius: 4px`**.
- **Glossary / term cards** → **`8px`** (deliberate exception: they use a border-left accent like callouts but are reference cards, not inline notes — distinguished by the purple palette `#e7d4ff` bg / `#9b59b6` border).
- **Structural containers** (full-bordered frames, image placeholders, PART banners, title block, challenge boxes) → **`8px`**.
- The retired one-side style `0 8px 8px 0` must NOT be used on callouts. **Exception — the cap/box pair is intentionally one-side-rounded** (cap `8px 8px 0 0`, box `0 0 8px 8px`): together they form one rounded container, so the §11 "no one-side rounding" check does not apply to the cap/box pair.
- Machine rule: a `border-left` accent box → 4px *unless* it's the purple glossary palette (→8px); a full `border` (all sides) → 8px.
- Other radii: code blocks `6px`, nav buttons & pills `4–5px`, inline code chips `4px`.

### 6.6 Icon Legend (13 icons)

```html
<div style="background: #fff; border: 2px solid #2e86ab; border-radius: 10px; padding: 15px 20px; margin-bottom: 30px;">
    <h3 style="margin-top: 0; color: #1a5276; font-size: 1em; margin-bottom: 10px;">Icon Guide</h3>
    <div style="display: flex; flex-wrap: wrap; gap: 15px; font-size: 0.9em;">
        <span>📖 LEARN</span><span>💻 CODE</span><span>🔨 BUILD</span><span>▶️ TEST</span>
        <span>✅ CHECKPOINT</span><span>⚠️ WARNING</span><span>📝 DO THIS NOW</span>
        <span>🔑 KEY TERM</span><span>💡 TIP</span><span>📘 NOTE</span><span>👀 SEE</span>
        <span>🔍 INSIGHT</span><span>🔮 NEXT</span>
    </div>
</div>
```

The 13 icons: 📖 LEARN, 💻 CODE, 🔨 BUILD, ▶️ TEST, ✅ CHECKPOINT, ⚠️ WARNING, 📝 DO THIS NOW, 🔑 KEY TERM, 💡 TIP, 📘 NOTE, 👀 SEE, 🔍 INSIGHT, 🔮 NEXT.

**§6.6a — TIP / NOTE / WARNING: ASSIGN BY FUNCTION (LOCKED, S61).** Three coach-voice callouts, distinguished by what they DO, not by feel. Labels are **bare** ("Tip" / "Note" / "Warning", never "Coach's Tip/Note") to match the Icon Guide; the coach's warmth lives in the prose, not the label.
- 💡 **Tip** — green `#f0f7f0` bg / `#6b8e6b` border — *actionable: a way to make something work or fix an error a coach would share* (e.g. "if you get a 'please install git client' error, go to §4.2 and install Git").
- 📘 **Note** — slate `#eceff1` bg / `#607d8b` border — *enrichment: extra information that deepens the lesson* (history, terminology, "also called…", the reason something works).
- ⚠️ **Warning** — amber `#fff8e1` bg / `#ffc107` border — *a real caution, usually safety* (don't stall the motors; don't drain NiMH past ~4,200 mV). A titled warning keeps its descriptive title (e.g. "⚠️ Battery Safety").
**The original book had Tip and Note INVERTED** — enrichment wore 💡 Tip and actionable fixes wore the amber "Coach's Note" (the icon drove the label). Corrected book-wide S61 by reassigning every coach callout by function. Authoring test: tells you how to do/fix → **Tip**; background/context → **Note**; risk of harm → **Warning**.

### 6.7 Section-marker pills — RETIRED

The old "READING / CODE / BUILD / TEST — <tagline>" marker pills (`#2e86ab` rounded pills placed at the top of a section) are **retired**. They are redundant with the section CAP, which already labels the section and carries its icon. **Remove every section-marker pill** during retrofit — do not place any `<LABEL> — <tagline>` pill or banner inside a section. (This is the same principle as the orphan intro-banner ban in §7.)

### 6.8 PART Dividers (colored banner, matches its group)

Each PART banner is a **solid color matching the section group it introduces** (not navy). It announces the group; the colored section cap+boxes follow beneath it.

```html
<div style="background-color: #3498db; color: white; padding: 12px 20px; border-radius: 8px; margin: 22px 0 10px;">
    <div style="font-size: 18px; font-weight: 500; letter-spacing: 0.5px;">PART 1 — Theory &amp; Concepts</div>
    <div style="font-size: 12px; color: rgba(255,255,255,0.85); margin-top: 4px;">Sections 1–3: Learn the fundamentals</div>
</div>
```

- **PART 1** banner = `#3498db` blue (before §1) — "Sections 1–3: Learn the fundamentals"
- **PART 2** banner = `#3a7d5c` green (before §4) — "Sections 4–6: Set up and program your robot"
- **PART 3** banner = `#c45d76` dusty rose (before §7) — title "PART 3 — Testing & Challenges"; subtitle "Sections 7–8A: Verify and extend" (or "Sections 7–8: Verify and extend" if no 8A). PART 3 now covers ONLY §7, §8, §8A.
- **PART 4** banner = `#9b6a9e` plum (before §9) — title "PART 4 — Challenges"; subtitle "Section 9: Apply what you have learned". This is the NEW part introducing the plum Challenges section.
- 18px title + 12px subtitle (subtitle `rgba(255,255,255,0.85)`), `margin: 22px 0 10px`.
- The old navy gradient `#1a1a2e → #16213e` banner is **retired**. §10 + end matter have NO PART banner (they're the gray tail, after PART 4).
- **Four PARTs total** (was three): 1=§1–3, 2=§4–6, 3=§7–8A, 4=§9. §10+end = untitled gray tail.

### 6.9 Standard Section IDs

`#section-1` … `#section-10`, plus `#section-8a` (if present), `#glossary`, `#quick-ref`, `#image-index`. Body carries `id="top"`.

### 6.10 Back-to-top links

After each section: `<p style="text-align: right;"><a href="#top" style="color: #3498db;">↑ Back to top</a></p>`

### 6.11 Code Blocks — DARK (VS Code / PlatformIO theme) (LOCKED)

Code blocks and ASCII diagrams use a dark theme matching what students see in PlatformIO / VS Code (Dark+). Light code backgrounds are **retired**.

```html
<pre style="background-color: #1e1e1e; border: 1px solid #333; border-radius: 8px; padding: 15px; overflow-x: auto; font-family: 'Courier New', monospace; font-size: 0.9em; color: #e8e8e8;">
<span style="color: #569cd6;">void</span> setup() {       <span style="color: #7cbf6e;">// comment</span>
    display.print(<span style="color: #ce9178;">"Hello"</span>);
}</pre>

**Code-block spacing (LOCKED v8.4):** dark code blocks use **`padding: 15px`**, **`margin: 16px 0`**, and **`line-height: 1.8`** — all consistent across every block in a lesson. 15px is the standard (NOT 10px/20px). **No blank-line doubling:** source-generated code often has an empty line between every line of code (the `BXBXBX` pattern), which renders double-height — STRIP all such blank lines inside `<pre>` so code is single-spaced; the `line-height: 1.8` provides the breathing room instead. If blocks use a wrapper-`<div>` + inner-`<pre margin:0>` structure, set line-height on the inner `<pre>`. No double-semicolons (`;;` is a typo, always strip). §11 check: FAIL if any code block has padding≠15px, line-height≠1.8, or contains blank lines inside `<pre>`.
```

- **Background:** `#1e1e1e` · **border:** `1px solid #333` · **base text:** `#e8e8e8` (near-white).
- **Syntax colors (VS Code Dark+):** keywords `#569cd6` blue · comments `#7cbf6e` green · strings `#ce9178` orange-tan.
- **ASCII diagrams** (motor scales, flowcharts) use the same dark box + `#e8e8e8` text — never light-on-light.
- **Exception:** the Icon Guide/Legend box stays light (`#fff` / `#f8f9fa`) — it is not a code block.
- Inline code chips (within prose) keep their light chip style (`background: #e8e8e8; padding: 2px 6px`).

### 6.12 Challenge Cards (SECTION 9) — CANON (LOCKED)

§9 Challenges use the **carded format** (the "Lesson 9 look"). Each challenge is a bordered plum box with a gradient header, a difficulty pill, and a collapsible solution. Bare `<h3>Challenge N`</h3> headings (old L4/L10 style) are **retired** — convert them to cards.

```html
<div id="challenge-1" style="border: 2px solid #7d5283; border-radius: 10px; margin: 25px 0; overflow: hidden;">
    <div style="background: linear-gradient(135deg, #7d5283, #9b6a9e); color: white; padding: 12px 20px;"><strong>Challenge 1: Title</strong> <span style="display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.8em; margin-left: 10px; background: #4caf50;">EASY</span></div>
    <div style="padding: 15px 20px; background: white;">
        <p>Challenge description…</p>
        <details style="background:white; border:1px solid #ddd; border-radius:8px; margin:15px 0;"><summary style="padding:15px 20px; cursor:pointer; font-weight:bold; color:#1a5276; background:#f8f9fa; border-radius:8px;">🔓 Click to reveal solution</summary>
        <pre style="background-color: #1e1e1e; color: #e8e8e8; ...dark code per §6.11...">…</pre></details>
    </div>
</div>
```

- **Outer box:** `border: 2px solid #7d5283; border-radius: 10px; overflow: hidden`.
- **Header (gradient — a "header element" per §6.2a):** `linear-gradient(135deg, #7d5283, #9b6a9e)`, white text. Matches the §9 plum group.
- **Difficulty pill — SPLIT, TWO AXES (v8.41, see §6.12b).** The pill is one badge divided by a 45° slash into a DOING half (left) and a GRASPING half (right), white text throughout. DOING = five tiers, what the student must physically do: Easy `#4A6B22` · Medium `#9A6B10` · Tough `#B85425` · Hard `#8A2F18` · Advanced `#6B2545`. GRASPING = three tiers, how much the student must understand: Light `#4A7FB5` · Moderate `#185FA5` · Deep `#0C3F6C`. *(v8.41 supersedes the v8.27 single five-tier pill — EASY `#4caf50` · MEDIUM `#2196f3` · TOUGH `#9c27b0` · HARD `#ff9800` · ADVANCED `#f44336` — which conflated the two axes and forced one label to lie whenever they diverged.)* *(v8.27 — scale recolored/relabeled from the old EASY/MEDIUM/HARD/EXPERT/COMPETITION set; the book-wide pill sweep is COMPLETE as of S59 — verified from files: 73 pills, all conforming to this scale, zero retired EXPERT/COMPETITION labels remaining.)*
- **Solution:** `<details>` / `<summary>` "🔓 Click to reveal solution"; the code inside is DARK per §6.11.
- The §9 **cap** stays flat solid plum `#9b6a9e` (it's a section cap, §6.2a); only the card *header* is the gradient.
- Old grape palette (`#7030A0`/`#9B59B6`) is retired → replace with plum (`#7d5283`/`#9b6a9e`).

---

## §6.12b THE SPLIT DIFFICULTY PILL — DOING vs GRASPING (v8.41)

**The rule.** Every challenge carries ONE pill with TWO ratings, cut by a 45° slash:

| Half | Question it answers | Scale |
|---|---|---|
| **Doing** (left, warm) | How much work is the student's hands doing? | Easy · Medium · Tough · Hard · Advanced |
| **Grasping** (right, blue) | How much must the student understand to attempt it? | Light · Moderate · Deep |

**Why two axes.** A single pill has to lie whenever the axes diverge. L03 C08 Auto-TRIM Preview asks
for COMMENTS ONLY — trivial to do — but requires reasoning about encoder differentials three lessons
before encoders exist. Rated ADVANCED it warned students off a card they could finish in ten minutes;
rated EASY it hid the only hard thing about it. Split, it reads Easy / Deep and both are true.

**Canonical colors (white text on every tier):**

- Doing: Easy `#4A6B22` · Medium `#9A6B10` · Tough `#B85425` · Hard `#8A2F18` · Advanced `#6B2545`
- Grasping: Light `#4A7FB5` · Moderate `#185FA5` · Deep `#0C3F6C`

The doing ramp walks one direction around the warm wheel (moss → ochre → rust → burgundy → plum) so
ORDER IS LEGIBLE WITHOUT READING THE WORDS. Grasping stays a single blue family — three stops rank
themselves, and warm-vs-cool is what tells the student the two halves ask different questions. Do NOT
give grasping its own hue set; that collapses the warm/cool split and makes the pill read as eight
competing colors.

**Markup (inline styles only — Canvas-safe):**

```html
<span style="display: inline-flex; align-items: stretch; margin-left: 10px; font-size: 0.8em; border-radius: 999px; overflow: hidden; vertical-align: middle;"><span style="background: #4A6B22; color: #ffffff; padding: 3px 13px 3px 11px;">Easy</span><span style="width: 4px; background: #ffffff; transform: skewX(-20deg); margin: 0 -2px; position: relative; z-index: 2;"></span><span style="background: #4A7FB5; color: #ffffff; padding: 3px 11px 3px 13px;">Light</span></span>
```

The slash is a skewed **4px** white span with **-2px** margins (v8.43, S63 — halved from the original 8px/-4px) — it overlaps both halves so the cut reads. **The negative margin is always HALF the width**; change one and you must change the other, or the halves stop closing over the slash and a gap opens.
as one badge divided, not two pills touching. A straight divider makes it look like two separate pills.

**Rating discipline.**

1. **Doing is about the hands.** Filling two blanks is Easy even when the surrounding concept is hard.
   Writing a function from a pseudocode spec is Medium. Designing the algorithm yourself is Hard/Advanced.
2. **Grasping is about the head — and is measured against WHAT THE LESSON TAUGHT.** A concept covered
   in that lesson's prose is Light no matter how sophisticated it sounds. A concept the student must
   supply themselves, or one the book has not yet taught, is Deep. This makes §6.12b a live instrument
   for §11's "§8A must cover what §9 requires": **a Deep grasping rating on a card whose concept is
   absent from the lesson prose IS a teaching gap**, and must be logged as one.
3. **Observation challenges rate by what they demand, not by their topic.** "Predict, then verify" with
   no code is Easy on doing. Its grasping rating is whatever the insight costs.

**Attributes.** Both axes are machine-readable: `data-difficulty="easy|medium|tough|hard|advanced"`
(doing, name retained so existing tooling does not break) and `data-grasp="light|moderate|deep"`.

**Applied S62:** L01 v03.6.0 · L02 v02.10.0 · L03 v03.10.0 (25 pills). Doing-axis re-rates in the same
pass: L01 C11 MEDIUM→Easy · L02 C06 HARD→Medium · L03 C03 EASY→Medium · L03 C05 MEDIUM→Tough ·
L03 C08 ADVANCED→Easy.

**THE SWEEP IS COMPLETE (S64).** L04–L15 swept: **84 challenges, 15 lessons, zero old pills remaining**
(`pill_sweep.py --audit` reports SWEPT on every lesson). **L16 is exempt** — it uses §6.12's tier-card
variant and has no `data-challenge` cards at all. Every swept card carries BOTH attributes, equal count.

Doing-axis re-rates applied S64: **L05 C01 EASY→Medium** (identical boolean edge-detection to L04 C02,
which was already Medium — two ratings for one concept) · **L14 C02 EASY→Medium** (three lines, but the
whole challenge is a trick question about `while(true)`) · **L10 C03 MEDIUM→Easy** (print a counter; its
hint resolves the only non-obvious part). The single **Tough** in the book (L13 C02) was deliberately
retained pending DJ's own pass, so the tier stays live.

**The two-axis progression as swept** (doing / grasping, lesson means):

| L01 | L02 | L03 | L04 | L05 | L06 | L07 | L08 | L09 | L10 | L11 | L12 | L13 | L14 | L15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.36 / 1.36 | 1.67 / 1.50 | 1.69 / 1.62 | **2.40 / 2.20** | 2.00 / 1.80 | 2.25 / 1.88 | **1.83 / 1.50** | 1.80 / 2.00 | 2.17 / 2.17 | 2.20 / 1.80 | 2.00 / **2.33** | 2.33 / 2.33 | 2.50 / 2.00 | 2.33 / 2.33 | 2.71 / 2.57 |

Floor (L01–L03) and ceiling (L15) are clean on both axes. Two findings for the progression audit:
**L04 spikes to 2.40/2.20** — third-hardest doing in the book, sitting fourth — and **L07 sags to
1.83/1.50**, below L05 and barely above L03, with L08 at 1.80 right behind it. Challenge COUNT also
collapses after L10 (11,6,8,5,5,8,6,5,6,5, then 3,3,3,3, then 7): L11–L14 carry 12 challenges between
them, fewer than L01 alone. L11 in particular pairs the book's **highest grasp mean (2.33)** with its
lowest count — under-practiced, not under-taught.

**TEACHING GAPS FOUND AND FIXED BY THE S64 SWEEP** (§6.12b working as the intended instrument — a Deep
rating on untaught prose IS a gap):

- **L04 §8A.8 NEW** — a `bool` as memory across `loop()` passes: the runaway-counter failure, edge vs.
  presence, why GLOBAL-vs-`loop()` placement is what makes a flag survive, and hysteresis. C02 required it.
- **L04 §8A.9 NEW** — `abs()` and the deadband: `error = position - CENTER` carrying size AND sign, why
  the sign defeats a closeness test, and why `error == 0` makes the robot buzz forever. C05 required it.
- **L06 §5.5 NEW** — the polygon exterior-angle rule (`360 ÷ sides`), including why the square is the one
  shape where interior and exterior agree and therefore taught a rule right in exactly one case. C03 said
  "you must calculate the turn angle" and the rule was taught nowhere.
- **L07 C05 card** — one-line definition of a **stub** (a finished definition with an empty body).
- **L08 `qr-map` NEW** — `map()` appeared exactly ONCE in the whole book, as a fill-in blank in C04, and
  was taught nowhere. Quick Reference row per §11's transcribed-only rule.
- **L09 `qr-dowhile` NEW** — `do…while`, same case: supplied complete in C03's template, taught nowhere.

**STILL OPEN (marked, not fixed):**

- **L03 C05 Variable Speed** — requires ARRAYS and the MODULO operator `%`. Neither appears anywhere in
  L03 prose (verified by grep, S62). Rated Tough / Deep. Needs both an array explainer and the modulo
  explainer already standing in the queue.
- **L15 C04–C07 ship with no template and no solution reveal** — four of the book's hardest challenges
  give a stuck student only prose, and give the AI Tutor nothing to strip. Deliberate capstone shape,
  but logged: C01–C03 are templated with solutions, C04–C07 are open specifications.

### 6.12c INLINE CSS DRIFTS PER REBUILD — MATCH STRUCTURALLY (v8.44 — NEW, S64)

**The finding.** The difficulty pill is one visual component repeated 84 times. Across L04–L15 it carried
**nine distinct style strings** — same rendering, different CSS property ORDER (`padding`-first vs
`background`-first, etc.).

**The cause is structural, not sloppiness.** Canvas strips `<style>` blocks and `class=` attributes (§6),
so there is nowhere for one canonical definition to live. Every card carries its own inline copy, and a
component is never *edited* — it is **retyped wholesale by whichever session rebuilds that lesson's
cards**. Git proves it: L04 and L05 both began `padding`-first on Jul 12; L05 flipped to `background`-first
on Jul 20 in commit `a3cd518` ("5, 12, 13 update" — the S59 Project B pilot), taking L12 and L13 with it in
the same commit. Single-commit, lesson-clustered changes are a **rebuild signature**. The variants are
STRATA, each carrying the hand of the session that last touched it.

**The rules that follow:**

1. **Never conclude "the markup is uniform" from a subset.** S63 found L01–L03 uniform and recorded
   "markup was uniform, zero variants" — true, because those three were swept together in S62 and share
   one stratum. Uniformity *within* a stratum says nothing about the book.
2. **An exact-string find-and-replace on an inline component is invalid book-wide.** It will silently
   match nothing on every lesson outside the stratum it was written against and report success.
3. **Match by STRUCTURE** — the element type plus a stable signature (e.g. a `<span>` whose style contains
   `display: inline-block` and `border-radius: 12px`, whose text is a known tier label) — never by the
   full style string.
4. **Scope the replace to ONE challenge block, not the file.** Two challenges at the same tier produce
   BYTE-IDENTICAL pills (L04 C02/C03 are both MEDIUM), so a file-wide `count == 1` assert fires falsely.
   Locate the block by `id="challenge-N"`, replace within it, assert `== 1` **inside the block**.
5. **Grep code constructs with tags stripped.** Syntax highlighting splits a construct across `<span>`s:
   `while(true)` reads as `while</span> (<span…>true` in raw HTML and a naive grep returns ZERO for a
   construct used 11 times (S64, L06). Normalize tags out before matching, then verify hits are prose and
   not code. This is the §11 false-positive rule run in the opposite direction — a false NEGATIVE.

**Tool.** `pill_sweep.py` (repo root, v1.0) implements all of the above. `--audit` is read-only and reports
per-lesson `SWEPT` / `not swept` / `*** MIXED ***` plus the count of distinct style strings still live; a
half-applied sweep cannot pass silently. Control-run it against untouched source before trusting it on
edited source (§11).

**§9 TIER-CARD VARIANT (added v8.5):** §9 need NOT always be Easy/Medium/Hard challenge cards. Where the content is **project tiers** rather than escalating challenges (e.g., L16 Nothing Left to Take Away), §9 uses **tier-cards**: white card, `box-shadow`, `border-radius: 8px`, with a **medal-colored top border** — Bronze `border-top: 5px solid #cd7f32`, Silver `#c0c0c0`, Gold `#ffd700`. This is a legitimate alternative §9 format, chosen per-lesson by the author; challenge cards remain the default.

### 6.12a THE THREE-PANEL CARD + WHEN IT APPLIES — CANON (Project B, v8.38)

Book-wide consistency = **uniform shell, inner format fits the challenge type.** The §6.12 card skin is the mandatory SHELL on every challenge in every lesson; what goes *inside* depends on the challenge.

**THE SHELL — mandatory on every card:**
- Outer plum box + gradient header (§6.12) with `Challenge N: Title` — **sequential N, never §-based** ("Challenge 9.1" is retired; renumber to "Challenge 1" and repoint any cross-refs).
- Difficulty pill (§6.12 five-tier). Where a lesson's challenges carry no rating, **infer and label "Inferred:"**; DJ adjusts.
- A pale-yellow **Work-in bar**: `<div style="padding: 12px 20px; border-bottom: 1px solid #eee; background: #fffbe6;">` holding 📁 **Work in** (the Maker starter link, or just the build name where no starter payload exists) and 🔍 **Where to look** (omit this line when the lesson has no Quick Reference to anchor).
- A flush **solution**: `<details data-reveal="solution" style="margin: 0; border: none; padding: 15px 20px;">` (§20.1 typing is mandatory).
- **Never:** a white body wrapper, a separate 💡 hint box, or a 📝 Plan-first line.

**THE INNER FORMAT — decided per challenge; a lesson MAY mix:**
- **Algorithmic** (write/modify a function or behavior) → the **three tiled panels**, each `<div style="padding: 15px 20px; border-bottom: 1px solid #eee; background: …;"><h4 style="margin-top: 0;">…</h4>…</div>`:
  - 🎯 **THE GOAL** — gray `#f8f9fa`. One–two sentences: what the finished thing does.
  - 🧠 **THE LOGIC (Pseudocode)** — purple `#f3e5f5`, dark `<pre>`. The plan in plain-English steps; **it absorbs the hint's thinking — there is no separate hint box.**
  - 🧩 **THE TEMPLATE** — green `#e8f5e9`, dark `<pre>` with `____` blanks on the concept taught. **The filled-in blanks MUST reproduce the solution exactly** (verify every blank).
  - Reference: **L06 / L07**.
- **Guided-edit / debug / observation / open-creative** (change a number, delete lines, measure, write your own) → **prose inside the card, no panels.** There is no algorithm to pseudocode and no function to scaffold; forcing panels degrades the card. Reference: **L01 (left as-is).** The shell still applies.

**OPEN-CASE RESOLUTIONS (provisional — DJ finalizes after a student runthrough):**
- **Withhold-solution lessons (L08/L09):** show the Template **and** the solution for now; the withhold decision is parked to the runthrough.
- **YOUR-NUMBER lessons (L12–L15):** the solution is shown on purpose with a tuning constant blank (`const int X = 0;   // <-- YOUR NUMBER`). Use a **two-level scaffold** — the Template blanks the *concept*; the Solution reveals the full code with only the YOUR-NUMBER blank remaining.
- **Maker link is a solved build, not a starter (L11/L12/L13):** a "make this folder" starter link goes in the Work-in bar; an "open the solved build" link stays inside the Solution. Where a lesson has no starter payload, the Work-in bar names the build only and a Maker-starter task is logged.
- **Solution code comments referencing a challenge number** (`// CHALLENGE 9.x`) stay unchanged when renumbering the visible heading — they byte-match the Maker payloads (payload gate), so syncing them is a coordinated lesson+Maker edit.

**STATUS:** L05 (pilot), L12, L13 converted S59; L06/L07 already conform; rollout continues lesson-by-lesson.

---


### 6.13 BRACE STYLE — K&R IS HOUSE STYLE; THE GUARD CLAUSE IS ALLOWED (v8.45 — NEW, S65)

**The book is K&R** — opening brace on the same line as the thing it opens. Measured S65 across every
`<pre>` in all 16 lessons: **837 K&R vs 2 Allman**. It was already consistent; this records it as a rule so
it stays that way. Allman is taught in L02 §3.1 as the alternative that exists, with the point that neither
compiles differently and the only real sin is mixing them inside one file.

**Braces are the default. A braceless one-liner is allowed only when the entire statement fits on the same
line as the `if`** — a guard clause:

```
if (killSwitchPressed()) break;
```

**The book does NOT adopt the common "never omit braces" rule, and this was a deliberate S65 ruling.** The
book contains **93 braceless guards** across L04–L16 — `if (killSwitchPressed()) break;`, `if (scaled > 99)
scaled = 99;`, and the aligned `else if` ladders in L09/L13/L15 that are readable *because* they are
braceless (bracing L09's three-line intersection ladder makes it fifteen lines and hides the state machine).
All 93 are single-statement, non-nested guards: no dangling-else hazard, no `goto fail` shape. Adopting the
absolute rule would have made the book violate its own canon in 93 places, and students who noticed would
trust it less.

**What the book teaches instead** (L02 §3.1, ⚠️ WARNING box): the danger is real and it is what happens
*next*. Adding a second line to a braceless `if` silently escapes it — the indentation lies, the compiler is
satisfied, the build is clean, and the robot misbehaves. So: **the moment you want a second line, add the
braces first, before you type it.**

**One live caveat:** "always brace" is the machine-checkable rule. If a linter or `clang-format` is ever added
to the student toolchain, these 93 sites become real work. That is the only scenario in which this ruling
costs anything.

## 7. EXIT TICKET (SECTION 10) — LOCKED

Three `<h4>` subsections, each wrapped in a specific callout:

1. **"Technical Skills: Can you...?"** — Checkpoint callout (`#e8f5e9` bg / `#4caf50` border). **☐ checkbox items only — NO list bullet** (see §11 checkbox-XOR-bullet rule).
2. **"Conceptual Understanding: Do you know...?"** — Coach's Tip callout (`#f0f7f0` bg / `#6b8e6b` border). **Bold question + italic `Answer:` line** beneath each (the L9 format), numbered.
3. **"Problem-Solving: Can you modify or extend...?"** — Learn/Insight callout (`#e3f2fd` bg / `#2196f3` border). **☐ checkbox items only — NO list bullet.**

(Optional follow-ons used in some lessons: a confidence self-assessment table and a "What's Next" preview. Quiz feature deferred.)

**Orphan intro-banner ban:** the blue "ASSESSMENT — Check Your Understanding", "CHALLENGES — Test Your Skills", "TESTING — Verify Everything Works" announce-banners are **retired** — they add no information and break the cap/box rhythm. Do not insert any "<LABEL> — <tagline>" banner at the top of a section; the section CAP already labels it.

---

## 8. CALLOUT STANDARD v1.0 — LOCKED

**All callouts use inline `style=` only.** `<strong>` for titles (never a CSS class). 9 standard types:

| # | Type | Icon | Background | Border |
|---|---|---|---|---|
| 1 | Coach's Tip | 💡 | `#f0f7f0` | `#6b8e6b` |
| 2 | Coach's Note / Warning | ⚠️ | `#fff8e1` | `#ffc107` |
| 3 | What You Should See | 👀 | `#d1ecf1` | `#17a2b8` |
| 4 | Do This Now | 📝 | `#ffe4cc` | `#ff8c00` |
| 5 | Checkpoint | ✅ | `#e8f5e9` | `#4caf50` |
| 6 | Key Term | 🔑 | `#f3e5f5` | `#9c27b0` |
| 7 | Learn / Insight | 📖 / 🔍 | `#e3f2fd` | `#2196f3` |
| 8 | Next Lesson | 🔮 / 🚀 | `#e8d4c4` | `#d4a574` |
| 9 | Challenge | 🎯 | `#e8f3ec` | `#3a7d5c` |
| 10 | Brain Check | BrainGear img | `#e8eaf6` | `#3f51b5` |

**Type 10 icon is an IMAGE, not an emoji** — `images/BrainGear_Incomplete.png` (gray) / `images/BrainGear_Complete.png` (green ✓), inline at ~1.35em. See §25.10 for the full Brain Check canon (state behavior, column, naming).

**Mini-Challenge / Bonus-Challenge blocks are retired** — replace any with the 🎯 Challenge callout (type 9).

**Canonical template (types 1–4, 6–9 — border-left accent style):**

```html
<div style="background-color: {BG}; border-left: 4px solid {BORDER}; padding: 15px 20px; margin: 20px 0; border-radius: 4px;">
    <strong style="color: {TITLE};">{ICON} {Title}</strong>
    <p>Body text.</p>
</div>
```

**Title colors per type** (extracted from L09 v03.0.3 reference lesson; type 9 set by DJ decision, Session 10):

| # | Type | Title color |
|---|---|---|
| 1 | Coach's Tip | `#3a5a3a` |
| 2 | Coach's Note / Warning | `#856404` |
| 3 | What You Should See | `#0c5460` |
| 4 | Do This Now | `#c45a00` |
| 5 | Checkpoint | `#2e7d32` |
| 6 | Key Term | `#6a1b9a` |
| 7 | Learn / Insight | `#0d47a1` |
| 8 | Next Lesson | `#8a5a2b` |
| 9 | Challenge | `#2a5a42` |
| 10 | Brain Check | `#283593` |

**Type 5 Checkpoint has TWO canon forms** (both live in L09):
1. Standard border-left callout — bg `#e8f5e9`, border-left 4px `#4caf50`, title `#2e7d32` (template above).
2. Centered milestone banner — `background: linear-gradient(to right, #e8f5e9, #c8e6c9, #e8f5e9); border: 2px solid #4caf50; border-radius: 10px; padding: 15px 20px; margin: 30px 0 20px 0; text-align: center;`

**Type-9 label canon:** label text is `🎯 CHALLENGE` (optionally with a time/difficulty qualifier in parentheses, e.g. `🎯 CHALLENGE (1 minute)`). "MINI-CHALLENGE" and "BONUS CHALLENGE" label texts are retired along with the blocks.

**`ZUMO_Callout_Standard_v1.md` is RETIRED** — templates folded in here as of v8.8. Do not request or reference the standalone file.

**Code-block syntax coloring — LOCKED (S12, DJ-approved):** All `<pre>` code blocks: dark bg `#1e1e1e`, base text `#e8e8e8`, color-only inline `<span>` highlighting (NEVER background chips — chip-in-pre renders text invisible). Palette (VS Code dark approximation): comments `#6a9955` · keywords `#569cd6` · preprocessor `#c586c0` · types/classes (`Zumo32U4*`, `Serial`) `#4ec9b6` · strings `#ce9178` · numbers `#b5cea8` · ini keys `#e06c75` · ini section headers `#d7ba7d` · in-code section banners `#6a9955`. Apply by script with a per-block stripped-text-identity assertion (colored output must strip back to byte-identical code). Book-wide application pass: L01–L02 COMPLETE; L03–L15 queued (apply during each depth pass).

**Details/summary readability rule (added v8.10, from the L02 white-summary defect):** every `<summary>` sits on a light background (`#f8f9fa` details box), so its text color MUST be readable there — canon colors: `#5a6872` for standard troubleshooting/hint details, `#2a5a42` when the details block lives inside a challenge callout (matches the 🎯 CHALLENGE title color). `color: white` (or any low-contrast color) on a summary is a build error. Gate check (mandatory): fail the build if any `<summary` style contains `color: white`. Background: L02 shipped three invisible "🔓 Stuck? / Answer / Click for solution" summaries; scan confirmed the defect was L02-only — this rule exists to prevent reintroduction during the L03–L15 depth passes, which reuse the L02 hint/solution pattern.

---

## 9. VERSIONING — LOCKED

**§5b ADDENDUM (v8.44, S64) — BOTH VISIBLE HOMES ARE MANDATORY.** The visible `major.minor` banner appears
**TWICE** in every lesson: once in the HEADER and once in the FOOTER. Fourteen of sixteen lessons had both;
**L02 and L12 shipped with only the header** and were repaired in S64. A lesson with one banner has half the
redundancy §5b exists to provide.

- **Audit:** `grep -o "Version [0-9][0-9]\.[0-9]*" Lesson_NN.html` must return **exactly 2 identical**
  strings, and both must match the hidden `<!-- Lesson version: -->` comment's `major.minor`.
- **Footer style is itself stratified** (same §6.12c effect): L01–L11 use a plain `<p>`/`<footer>` block;
  L10 and L13–L16 use a gradient banner div. When restoring a missing footer, **match that file's
  neighbours** — do not invent a third format.
- **Derive the version from the hidden comment when writing a footer**, never hand-type it, so the two
  homes cannot disagree at birth.


- Scheme (all projects): major = `v#`, moderate = `v#.#`, minor = `v#.#.#`. **No letter suffixes.**
- Filenames use zero-padded lowercase form: `v01`, `v02`, …
- **UNIQUE VERSION PER DELIVERY (v8.20 — DJ ruling, S33).** Once a build has been presented for download, **any** further change — code, prose, or image — bumps the version. Two files with the same name NEVER have different contents. *This RETIRES the old "a fix to an already-fixed version keeps its number" rule, which in S33 produced two different `Lesson_10_Obstacles_v02_1_1.html` files and sent the wrong one to GitHub.*
- **IMAGE CHANGES ARE A MINOR BUMP (v8.20 — DJ ruling, S33).** Inserting art, removing a figure, renumbering a placeholder, or editing a caption or the Image Index is a minor correction → third digit (`v04.0.3` → `v04.0.4`).
- **Reopening a lesson:** read the current v# from the uploaded `.html` filename — do not hardcode a target.
- **v8 re-baseline exception (one-time):** every lesson resets to `v01` at the v8 transition. Normal bump rule resumes afterward.

---

## 10. IMAGE PLACEHOLDERS

Keep `[IMAGE X.Y]` format (X = lesson number, Y = image number). Image Index must list exactly what appears in the body — **no phantoms, no omissions** (S33 found L02 listing a `[GRAPHIC 2.3]` that exists nowhere).

**IMAGE and GRAPHIC ARE SEPARATE NUMBER SPACES (v8.20 — canon, S33).** `L01_IMAGE_1-13` and `L01_GRAPHIC_1-13` coexist by design; the prefix disambiguates. `[IMAGE 2.8]` and `[GRAPHIC 2.8]` in the same lesson is **not** a collision and must not be "fixed."

**AUDIT ART AGAINST `images/`, NEVER AGAINST THE LESSON ALONE (v8.20 — canon, S33).** Before declaring anything about art, clone the repo and compare three sets: (1) assets in `images/`, (2) `<img src>` in the lesson, (3) dashed placeholders. S33 found **nine built assets that no lesson referenced** — including all three L16 SVGs, which shipped with the lesson showing zero figures. GATE CHECK per lesson: every repo asset is referenced; every `<img>` resolves; every placeholder has no file.

**IMAGE `src` = PAGES DOMAIN, NEVER raw.githubusercontent (v8.33 — canon, S49).** Every `<img src>` in a lesson points at `https://weymuth.github.io/zumo/images/<file>` — NOT `https://raw.githubusercontent.com/Weymuth/zumo/main/images/<file>`. Raw is rate-limited by GitHub and is not a page-asset host: under raw, a lesson that loads many images gets HTTP 429 on a random few per page-load, so different figures blank out on different loads (S49 symptom: L04 4.1/4.2/4.3 intermittently missing). Pages is same-origin, unthrottled, correct MIME. Also required because lessons render inside Canvas, which needs an absolute URL. NON-image repo files (e.g. `ZUMO_Template.zip` download links) may stay on raw — the rule is scoped to the `/images/` path only. S49 converted all 114 image refs book-wide.

- `[IMAGE x.y]` = DJ-sourced photo/screenshot. `[GRAPHIC x.y]` = Claude-authored SVG.
- Placeholder → figure conversion is a **minor bump** (§9).
- **Strip EXIF/GPS from DJ photos before pushing (S49).** iPhone photos carry GPS + device metadata; run them through a re-save that drops EXIF before they go to the public repo.
- A GRAPHIC may temporarily stand in for an un-shot IMAGE (S49: L11 5-sensor diagram filled L04 4.1); caption it as temporary and swap to the real photo filename when shot.

---

## 11. PER-LESSON QUALITY CHECKLIST (run before presenting any lesson)

- [ ] **BLANKS ARE SPENT (v8.17):** every tunable declared as a student blank (`const int X = 0;   // <-- YOUR NUMBER`) is actually READ by the code. Grep: a constant that is declared and never used is a lie in the worksheet. Blanks ship as `= 0` with the starting guess in the COMMENT, never as a seeded value.
- [ ] **ZERO BYTE DELTA IS NOT PROOF OF NOTHING (v8.17):** if a state's binary size is unchanged after an edit, ask whether the edit changed a CONSTANT (byte-identical by construction — fine) or added LOGIC (then `--gc-sections` may be discarding it — investigate). Disassemble with `avr-objdump -d` and read the immediates before concluding a fix vanished.
- [ ] **SABOTAGED BUILDS SHOW THE PLANTED LINE (v8.17):** every Bonus mystery displays its sabotaged code in the hint. The question is "why does this cause that symptom," not "find the typo." (Also satisfies the payload gate by construction.)

- [ ] Filename: `Lesson_##_Topic_v##.html` (padded number, lowercase padded version, approved topic token)
- [ ] Body uses Segoe UI + `#fafafa` + `id="top"`
- [ ] Nav + title use top-down dark-first blue gradient
- [ ] Title h1 = `LESSON ##` with NO leading icon
- [ ] Every section is a CAP + BOX: colored cap (white title, keeps icon) on matching bordered box (§6.5)
- [ ] Cap/box + PART banner colors follow nav scheme: §1–3 blue `#3498db`, §4–6 green `#3a7d5c`, §7/§8/§8A rose `#c45d76`, **§9 plum `#9b6a9e`**, §10+end gray `#6c757d`
- [ ] PART banners are SOLID group colors (navy gradient retired); 4 banners (PART 1–4); PART 3 subtitle "Sections 7–8A: Verify and extend" (or 7–8 if no 8A); PART 4 subtitle "Section 9: Apply what you have learned"
- [ ] Sub-headings h3/h4 use the SECTION GROUP COLOR (not global blue/green); table headers use the darker section shade (§6.5). Callout-internal headings exempt. (See the dedicated NEW check below.)
- [ ] Code blocks + ASCII diagrams are DARK (`#1e1e1e` bg, `#e8e8e8` text; keywords `#569cd6`, comments `#7cbf6e`, strings `#ce9178`); no light-on-light; Icon Guide stays light (§6.11)
- [ ] **PROSE IS NOT CODE — never wrap challenge Goal/prose in a dark `#1e1e1e` block (v8.33 — S49).** Dark `#1e1e1e` is for `<pre>` CODE and reveal blocks ONLY. L03 was the one lesson of 16 that dressed its challenge Goal prose in a dark block; inline `#e8e8e8` code-chips and light callouts nested inside it then rendered light-on-light (invisible). Goal/task prose sits on the WHITE card body like every other lesson. Contrast gate: no light-background element (chip, callout) may sit inside a dark block without an explicit dark text color; run a luminance check, not just a string match.
- [ ] All box/callout corners fully rounded (no one-side-rounded `0 8px 8px 0`)
- [ ] Icon legend has all 12 icons ("WARNING")
- [ ] 10 sections present; 8A only if the lesson has a reusable coding pattern (present: L6–L12; absent: L1, L13–L15; verify L2–L5), placed between 8 and 9
- [ ] End-matter caps use icon set: 📖 Glossary / ⚡ Quick Reference / 🖼️ Image Index
- [ ] **Glossary entries use the canon term-card format** (`#e7d4ff` bg / `#9b59b6` border / `8px`); no stray glossary purples (`#f3e5f5`, `#f3e8f9`, `#7b2d8e`, `#9c27b0`) in the glossary region.
- [ ] Section IDs in clean order: 1,2,3,4,5,6,7,8,8a,9,10,glossary,quick-ref,image-index
- [ ] Nav anchors all UNIQUE and all resolve; "Back to top" + cross-refs resolve
- [ ] Cap `id` matches visible "Section N" label + nav anchor
- [ ] Exit Ticket = 3-h4 with correct callout colors
- [ ] Callouts inline-only; 0 `<style>` blocks; 0 callout classes
- [ ] Image Index matches body placeholders exactly
- [ ] div tags balanced; version string in title block AND footer matches filename
- [ ] **NBSP/whitespace stripped:** 0 standalone `\xa0` lines (export artifact); no runs of 3+ blank lines. (Pre-overhaul lessons ship with 140–390 of these; each renders as an empty vertical-space line.)
- [ ] **Bare-element sweep (after removing any `<style>` block):** 0 bare `<table>` (every table has `width: 100%`); 0 bare stage-marker divs in old navy `#2c3e50` — recolor to `#2e86ab`. Old stylesheets styled these globally; once inline-only, bare elements lose styling silently and pass div/anchor checks while rendering wrong (narrow tables → horizontal gaps).
- [ ] **No retired navy:** 0 occurrences of `#2c3e50` or `#1a1a2e` anywhere (markers, title, banners).
- [ ] **div-depth walk (not just balance):** every PART banner sits at div-depth 0 (outside all section boxes). Balance can pass while a banner is trapped inside the prior box; verify depth, not just open==close counts.
- [ ] **Dark-wrapper scope check (v8.14.1, from the S21 L03 find):** every dark code wrapper (`background-color: #1e1e1e` div) must close before the next `<h3>`/`<h4>`. Walk each dark div to its matching closer; if the enclosed span contains ANY heading, FAIL. Balance and the depth walk both pass when the closer merely sits too late (L03 v03.0.0: the Safe-Run wrapper's closer landed after four QR tables — code chips rendered as blank pills, shaded rows light-on-light). Measure banner/section depth at the rendered DIV, not at region comments (comments legitimately sit inside closing wrappers).
- [ ] **In-code highlight spans preserved + dark-readable:** pre-existing "new code"/diff highlight spans (e.g. light-green `#90EE90`) are kept (carry pedagogical meaning) but recolored for the dark code background (e.g. bg `#2d5a2d`, text `#b8f0b8`) — never light-text-on-light-fill, never stripped.
- [ ] **Callout radius two-tier:** inline content callouts (border-left accent notes) = `4px`; glossary/term cards = `8px`; structural containers (full-border frames, image placeholders, PART banners, title) = `8px`. No one-side rounding (`0 8px 8px 0`) on callouts — that style is retired. (Code blocks `6px`, nav buttons/pills `4–5px`, inline code chips `4px` separate and unchanged. Cap/box pair is the one intentional one-side-rounded exception.)
- [ ] **4-PART structure (NEW):** PART 1 §1–3 blue · PART 2 §4–6 green · PART 3 §7–8A dusty rose ("Verify and extend") · **PART 4 §9 plum** ("Apply what you have learned"). Four banners, not three. §10 + end = untitled gray tail. PART 4 plum banner present before §9.
- [ ] **§9 plum (NEW):** §9 cap, nav button, and PART 4 banner all use plum `#9b6a9e` (cap/banner/button flat solid). §7/§8/§8A stay dusty rose `#c45d76`. No `#c45d76` on §9 elements; no plum on §7/§8/§8A.
- [ ] **Payload byte-match gate (v8.14, canonized from S18 approval):** every Maker `PAYLOADS[lesson][key]` byte-matches its lesson-source code block at EVERY lesson save (payloads exclude the generator-stamped header + `#include` — mainCpp = head + body). A lesson edit that touches any `<pre>` wired into the Maker requires re-verifying its payloads before either file ships.
- [ ] **Payload-gate INHERITANCE RULE (v8.15, DJ-approved S22):** lesson N's canonical payload corpus = its own decoded `<pre>` bodies + the Maker's template strings **+ lesson N−1's `finished` payload bodies**. Rationale: from L08 onward, Step 1 of every §6 is "copy your Lesson N−1 project" — the eight files arrive wholesale, and the lesson only shows the blocks it CHANGES. Files carried unchanged are therefore canonical by construction, and demanding they re-appear in lesson N's pres would force pointless duplication of a whole project into the lesson body. The rule stays byte-strict in the direction that matters: any content lesson N *modifies* must still appear verbatim in lesson N's own pres. Implementation note: `finished` may be a plain string (L02/L03) or a multi-file dict (L07+) — handle both. Battery must PASS L02 through the newest lesson at every Maker save; zero regressions is the bar.
- [ ] **IF IT IS IN THE PAYLOAD, IT GOES IN THE BOOK (v8.35 — LOCKED, S56).** An unmatched gate line is a **gap in the book**, not a gate defect. The first move is always to add the content to the lesson — never to exempt the line. **Executable code is NEVER exempt under any framing.** S55 burned four takes proposing to exempt L01's failures as "comment-only scaffolding"; 132 of them were an EEPROM name-reader that appeared in no lesson, and C01 Part 5 asked students to use it. Test to apply: *would a student need to read this line to do the work?* If yes, it belongs in the book. Corollary — when a shared listing serves N challenges, put the ONE common body in §9 and let each card quote its OWN target line verbatim; that satisfies the gate without duplicating the listing N times.
- [ ] **BOXED INSTRUCTION HEADERS ARE ADVISORY BUT FINGERPRINTED (v8.35 — LOCKED, S56).** A challenge file's boxed header (`// ┌─┐ … // └─┘`) is the student's working instructions, deliberately kept IN the file so a student coding in one window never has to switch to the book mid-step (DJ ruling S56: "lots of file skipping back and forth" — a step you remove is a step they will actually do). The book's §9 card carries the same instructions as prose, which is the better form for reading, plus the exact target line quoted verbatim. A boxed-header line that does not byte-match is therefore a FORMAT difference, not missing content, and does not fail the gate — it is reported under **ADVISORY**. **But advisory means "not required to appear in the book," NEVER "unchecked":** gate v1.6 pins every boxed header with a line count + md5 in `BOXED_FP`, so an edited header FAILS loudly. Without the pin, v1.5 let a tampered instruction block pass silently (verified). To change a header on purpose: edit it, run `--update-fp`, paste the new manifest — the bump is deliberate, and drift is impossible.
- [ ] **READ THE CENSUS, NOT THE RAW COUNT (v8.35, S56).** The gate's CATEGORY CENSUS (boxed comments / `<<<` markers / other comments / **EXECUTABLE CODE**) is the number that decides severity. `EXECUTABLE CODE: 0` with a large advisory count is a healthy lesson; `FAIL (148)` that is 132 executable is a broken one. Never conclude from a truncated fail list — that error cost S55 three takes.
- [ ] **Bounded-scope replace assert (v8.14):** every wholesale/regex replace must assert its span endpoints sit inside ONE card/step/section — `count==1` alone is insufficient (a greedy `.*?` can span two cards and pass the count check; S20 destroyed L03 Bonus-1+2 this way before donor recovery). Prefer exact-string `str.replace` with `count==1`; when a regex is unavoidable, print and eyeball the matched span before applying.
- [ ] **Challenge-card canon (§6.12):** every §9 challenge is a carded box (border `#7d5283`, header gradient `135deg #7d5283→#9b6a9e`, difficulty pill, `<details>` dark solution). No bare `<h3>Challenge N`</h3>. Old grape `#7030A0`/`#9B59B6` retired.
- [ ] **Checkbox-XOR-bullet (GATE, global):** FAIL the lesson if ANY `☐` appears inside a list whose `<ul>`/`<ol>` does not carry `list-style: none`. Detection must scan EVERY `<ul>`/`<ol>` regardless of its attributes (a styled `<ul style="margin:0; padding-left:20px">` containing `☐` is a FAIL just like a bare `<ul>`) — a narrow "bare-`<ul>` only" check misses styled variants. Fix = inject `list-style: none; padding-left: 0;` into that list's style. No list item EVER shows both a bullet and a `☐`. Applies to ALL sections, not just Exit Ticket.
- [ ] **No orphan intro-banners:** 0 "ASSESSMENT / CHALLENGES / TESTING — <tagline>" announce-banners at the top of any section (the cap labels the section; §7).
- [ ] **No section-marker pills (§6.7 retired):** 0 "READING / CODE / BUILD / TEST — <tagline>" `#2e86ab` pills anywhere. The cap is the only section label.
- [ ] **Subheadings + table headers = SECTION color (NEW):** h3/h4 subheadings use the section group color (§1–3 blue, §4–6 green, §7/8/8A rose, §9 plum, §10+end gray); table headers use the DARKER shade of that color (§6.5 table). No global `#2e86ab` h3 or `#1a5276` table header outside §1–3. Callout-internal headings exempt. h3 must NOT be near-black bold.
- [ ] **Gradient-vs-solid by role (§6.2a):** nav/title/challenge-header/milestone-header = gradient; caps/PART banners/nav buttons/pills = solid. No solid challenge headers, no gradient caps.
- [ ] **PART 3 title token:** "PART 3 — Testing & Challenges" (not "Test & Challenges").
- [ ] **Empty-section-box check (added v8.11, from the L02 Glossary/Quick-Ref/Image-Index defect):** every section banner’s bordered body box must actually CONTAIN its section’s content. A box that opens and immediately closes (regex: `border-top: none;[^>]*>\s*</div>`) is a build FAILURE — div-balance alone cannot catch it (L02 ≤ v02.0.18 passed balance while all three end-section bodies sat outside their boxes). Where `<!-- end X wrapper -->` markers exist, the box’s closing `</div>` must sit immediately before the marker.
- [ ] **Depth-pass items (v8.12, for any lesson given the L02 treatment):** syntax coloring per §8 palette (identity-asserted) · challenge timers wired (`timer.html` iframes) · "📁 Work in:" destination lines on every challenge · Maker challenge registry extended in `newproject.html` · §4 Start-a-New-Lesson ritual block present · ALL code compile-verified on the AVR harness · white-summary + empty-box scans clean.
- [ ] **§8A MUST COVER WHAT §9 REQUIRES (v8.36.1, S57).** Every language construct a lesson's §9 challenges ask students to WRITE must be taught in that same lesson — §8A is where it goes, in the words of L04's own §8A intro: *"the challenges in Section 9 use it immediately; this section makes sure you own it first."* Using a construct inside the lesson's given code is not teaching it. GATE: list every construct appearing in a lesson's §9 hints and reveal-solutions, and confirm each has a tutorial at or before that lesson. Canonized after L04 C03/C04 required `for` loops that L04 shipped in its own build (8 uses) and narrated in one sentence, while the formal tutorial sat in L05 §5.15 presenting first contact. FIX PATTERN: teach it at FIRST CONTACT, and demote the later lesson's tutorial to the §18.1 spiral second rung (mark it 🔁 Builds on: with the source-lesson star) carrying only what is genuinely new there — never two first contacts.
- [ ] **A "THE BOOK HAS NEVER…" CLAIM IS A DEPENDENCY, NOT PROSE (v8.36, S57).** Any sentence asserting what the book has never done, not yet used, or will meet for the first time is a claim about all sixteen lessons, and it goes stale the moment another lesson changes. Grep the whole `lessons/` tree for the feature before trusting such a line, and re-grep whenever new content introduces one. Canonized after S56 published an EEPROM name-reader in L01 §9, which silently falsified L16 §4.3's "this book has never touched it" — a defect created by a correct fix in a different lesson. Same class as a false claim about code (§11 grep-the-code rule): the lesson said one thing, the book did another.
- [ ] **AUDIT FALSE-POSITIVE DISCIPLINE — A REGEX REPORTS CANDIDATES, NOT VERDICTS (v8.36.2, S58).** A prose-keyword grep produces LEADS, never findings — every hit is verified against rendered text before it drives an edit. (1) SEPARATE CODE FROM PROSE BEFORE COUNTING: strip to `<pre>` bodies to test whether a construct is USED; strip all tags to test whether it is TAUGHT; never count a token that spans both (`abs(` inside a `while` condition is a use, not a lesson). (2) A KEYWORD NEAR A HEADING IS A LEAD, NOT PROOF: for any "is X taught?" question, surface the candidate heading and read it — the regex narrows the field, only the read closes it. (3) VERIFY AGAINST RENDERED TEXT BEFORE ACTING: S57's phantoms all evaporated on a read — `milliseconds` matched as `millis`, a stray `?:` in prose as the ternary, a changelog `v04.6.0` as a version mismatch. Same family as S56's unescaped-`<` false alarm and the L04 image-index phantom. A smarter script sharpens the lead; a human read is the only verdict.
- [ ] **Dedicated ASCII sweep (v8.13.1)** on every depth pass, even for lessons marked "converted": scan all `<pre>` bodies for box-drawing/arrow characters (┌ ┐ └ ┘ │ ─ ◄ ► ▶). Established by the L03 half-conversion find (Session 15): S6 built the SVGs and the tracker showed ✅, but the lesson file was never edited — four ASCII diagrams survived to Session 15.

---

## 11b. PRE-OVERHAUL LESSON PROFILES (audit FIRST to identify which)

Lessons authored before the v8 overhaul come in **two profiles**. The audit step (grep for `<style`, count `class=`, count `\xa0`) identifies which, and that drives the build:

- **Class-based (e.g. L6):** has a `<style>` block + CSS classes + nbsp. Requires **class→inline mapping (approach B):** map every class straight to its v8 inline equivalent (callouts → Callout Standard v1 colors, nav → color-coded buttons, part-divider → solid banner, section-marker → `#2e86ab` marker), then the normal design pass. Also carries the bare-`<table>` / nbsp problems.
- **Inline-but-stale (e.g. L7, L8):** no `<style>` block (already inline), but ships with nbsp clutter, bare/under-styled tables, navy `#2c3e50` markers, **and section-numbering deviations** (missing "Code" §5, off-by-one Test/Troubleshoot/Challenges/Exit, 8A out of DOM order, mislabeled Exit, missing PART 3 banner, missing Image Index). Fix structure first, then design pass.

Either profile may need a structural §5 "Code" authored (Bible §4: §5 = walkthrough/project-org; §6 = step-by-step build). Split at the natural CODE/BUILD seam if present (L7), or author from the build content (L4).

---

---

## 13. BATTERY CANON (v8.20 — LOCKED, S33)

**The classroom fleet runs rechargeable NiMH — Panasonic eneloop.** Every battery number in the book is written for NiMH.

| Reading (4 cells) | State | Meaning |
|---|---|---|
| **~5,400 mV** | Fresh off the charger | ~1.35 V/cell |
| **~4,800 mV** | The plateau | 1.2 V/cell — where NiMH spends most of its life. **This is `BATTERY_GOOD`.** |
| **~4,200 mV** | Nearly empty | 1.05 V/cell. **This is `BATTERY_LOW`.** Draining past it damages the cells. |
| **~6,300 mV** | Not NiMH | Somebody put alkalines in. |

- **The constants are the chemistry, not a guess.** `BATTERY_GOOD = 4800` / `BATTERY_LOW = 4200` (RobotConfig.h, L07+) are the NiMH plateau and the NiMH floor. Any lesson that states battery numbers must agree with them.
- **Alkaline is allowed but taught honestly:** 6.0 V nominal — which *is* the motors' rated voltage, so a robot on fresh alkalines is slightly faster (Pololu quotes motor specs at 6 V). But alkaline voltage **slides downhill the whole time it is used**, while NiMH holds a flat 1.2 V plateau and then drops. *A robot on alkalines is a moving target: the one you tuned in first period is not the one you get in seventh.* This is the same physics L11 ("Time Lies, Distance Doesn't") is built on.
- Sources: Pololu recommends NiMH (4.8 V nominal) and notes motor specs are at 6 V; Panasonic states eneloop holds a consistent 1.2 V through the charge while alkaline drops rapidly below it.

---

## 14. ENGINEER'S LOG (v8.20 — LOCKED, S33)

One 📓 callout at the **end of §10** in every lesson, above the footer. **Prose only — no `<pre>`, no new anchors.** The payload gate never sees it; no byte count moves.

**Markup (canonical):**
```html
<h3 style="[LOCAL SKIN of that lesson's §10 subheads]">Engineer&rsquo;s Log</h3>
<div style="background: #f8f9fa; border-left: 5px solid #1a5276; padding: 15px 20px; margin: 20px 0; border-radius: 4px;">
<b>&#128211; ENGINEER&rsquo;S LOG #NN &mdash; feeds: [TDP section]</b><br>
[the prompt]<br>
<i>Why judges care: [one line]</i></div>
```
The heading adopts the lesson's local §10 skin; **the box is book-wide constant** (TDP-blue `#1a5276`) so the log is recognizable as one instrument across 16 lessons.

**The 16 prompts (locked S32, written into the book S33):**

| # | Feeds (TDP section) | Prompt |
|---|---|---|
| 01 | Electronic Design → main controller | Write the "before" paragraph. Rewritten in L16 — the gap is the Abstract. |
| 02 | Electronic Design → sensors/actuators | Draw the board. Labeled, one page, no code. |
| 03 | Mechanical → actuators & power train | Record your TRIM — and why it isn't zero. |
| 04 | Electronic Design + testing data | Record calibration min/max; why the numbers move rooms. |
| 05 | Project Planning → constraints | Defend a forced tradeoff (pins 20 & 4 are shared). |
| 06 | Mechanical → power train + data | Show the COUNTS_PER_CM arithmetic; did 30 cm come out 30 cm? |
| 07 | **Software → architecture** | Draw the 8-file architecture. No source code. *(Highest-value entry in the book.)* |
| 08 | Software → innovative solutions | Explain P-control in plain English; then your Kp and how you found it. |
| 09 | Software → flowchart | Draw your state machine. |
| 10 | Project Planning → requirements | What does your obstacle maneuver cost you? |
| 11 | **"What didn't work"** | The failure entry: fresh battery vs. tired battery. |
| 12 | Performance → testing data | Cross-examine the robot: encoder vs. gyro, carpet vs. slick. |
| 13 | Software + requirements | How does the robot *know*? Your false-victim threshold. |
| 14 | **Rules-mandated** | Your LoP procedure + self-test card (RCJ 4.3.7). |
| 15 | Performance Evaluation | Record the hill-climb: gains, MAE/PEAK/WEAVE, when you stopped. |
| 16 | Whole TDP | Assemble. Abstract **last**. *(Ships as §10.3.)* |

**Rule: instruments go forward, documentation goes backward.** Code added to a published lesson invalidates payload bodies and the taught byte chain; prose-only retrofits do not.

### 14.1 THE LOG *IS* THE TDP — ONE GROWING DOCUMENT (v8.26 — LOCKED, S40)
The 16 Engineer's Log prompts are **not 16 independent worksheets** — they are a scaffold that **accumulates into a RoboCupJunior Technical Description Paper (TDP)** by L16. The engineering notebook and the competition TDP are the **same artifact**; students do not start a separate paper at the end.

- **Delivery = ONE growing Google Doc structured as the TDP from day one.** Each student makes **one copy** of the template at course start and keeps it in their own Drive all term (a Doc survives a semester across shared lab machines; `localStorage` fails cross-machine).
- **Template = `ZUMO_TDP_Template.md`** (repo root, live). Structure: PART A standing running-logs (A1 Hats-I-Wore · A2 Improvement-Ideas one-line-per-lesson · A3 Failure Log · A4 Measured-Data OLED tables · A5 Lab Log for Outside-Work evidence) + PART B the TDP proper (Abstract **last** · Intro/Robot & Author solo · Planning · Hardware · Software · Performance Eval · Lessons Learned · Deliverables/LoP · Version 2).
- **One source of truth:** the log **prompts stay in the lessons** (the §14 callouts); the Doc holds only the TDP scaffolding + standing lists. Do not duplicate prompt text into the template.
- Design goal: **minimum extra student effort** — a piece filled the week each lesson finishes, so the TDP format becomes muscle memory rather than an end-of-term scramble. Each prompt's "feeds:" tag names the TDP section it drops into.

---

## 15. MAKER REGISTRY & LINK CANON (v8.22 — LOCKED, S36)

The Maker registry and the lesson are ONE artifact seen from two sides. When they drift, a student clicks a link labelled `7C` and downloads what the lesson calls `7D`. Four rules, all earned.

### 15.1 THE SECTION 7 LADDER IS FIVE RUNGS — AND THE LETTERS MUST MATCH
Every calibration ladder is exactly **7A-7E**, and `KINDS[N]` carries exactly `cal_7a` ... `cal_7e`. **The Maker's letter must be the lesson's letter.** Canonized after S36 found L11's Maker off by one from 7C onward: `cal_7c` was labelled "Two Gaps in a Row" (the lesson's **7D**), `cal_7d` was a "Full Course" build **no lesson rung referenced**, and the lesson's **7C - TRIM Under Blindness had no kind at all**. Nothing was broken enough to fail a gate; the letters had simply drifted apart. **GATE CHECK: for every lesson, assert the ordered list of Section 7 rung letters in the HTML equals the ordered list of `cal_7*` letters in the Maker.**

### 15.2 `finished` IS THE LAST STEP — step kinds cover 1..N-1 ONLY
If Section 6 has N steps, the Maker carries `step_1` ... `step_N-1` **plus** `finished` — and `finished` IS step N. A `step_N` kind for the LAST step is a **duplicate**, not a build. Canonized after S36 found L14 (4 steps) carrying `step_1`..`step_4` *and* `finished`, with `after_step_4` **byte-identical** to `finished`: the Maker was offering one project under two names. L11/L12/L13/L15/L16 all obey this by construction. **GATE CHECK: assert `after_step_<last>` is NOT byte-identical to `finished`. If it is, the last step kind is redundant — retire it.**

### 15.3 A KIND MAY SHARE ANOTHER KIND'S `payloadRef`
The Maker resolves a payload through the KINDS row's 6th field (`var pay = (P && rec[5]) ? P[rec[5]] : null;`) — **not** by the kind key. So a **run-only rung**, one that changes no code and only changes what the student does on the floor, legitimately points at an existing payload. L14's 7A/7B/7D/7E and L15's 7B/7C/7E all point at `finished`; S36 pointed L11's `cal_7c` (TRIM Under Blindness — the student zeroes their own TRIM) at `cal_7b`. **Do NOT manufacture a duplicate payload body just to give a rung its own key.** A shared ref is correct, cheaper, and self-documenting.

### 15.4 THE FOUR LINK SHAPES (LOCKED)
Every kind is reachable from the lesson. Four shapes, no others:

| Group | Shape | Placement |
|---|---|---|
| Build steps + `finished` | `<details>` titled `CATCH-UP - Step N` | END of the step block, AFTER the CHECKPOINT |
| Calibration 7A-7E | `<details>` titled `7X in the Project Maker` | END of the rung block |
| Bonus mysteries | bare `<p>` | END of the mystery card |
| Section 9 challenges | link INSIDE whatever the lesson already discloses | last child of the solution `<details>` |

Href is always `https://weymuth.github.io/zumo/newproject.html?lesson=N&amp;kind=<key>`, styled `color: #2e86ab; font-weight: bold`.

The challenge shape follows the lesson, because **the book has no single disclosure canon** — L06/L07/L11/L13/L14 publish solutions, L08/L09 withhold them, L10 gives neither, L12/L15 print a scaffold with a blank. The link goes wherever that lesson already puts its answer. (DJ ruling S36: leave it; revisit after classroom use.)

### 15.5 THE MAKER IS NOT UNIFORMLY FORMATTED — EDIT BY OFFSET, NEVER BY LINE
`PAYLOADS` is **pretty-printed for some lessons and compact single-line for others**: L11's block has one key per line; **L14's entire block is ONE line**. A deletion written as `ls = s.rfind(newline, 0, key); s = s[:ls] + rest` works on L11 and **destroys L14**, because `rfind` walks back past every preceding key to the start of the whole lesson block. S36 corrupted the Maker exactly this way — PAYLOADS silently collapsed from 15 lessons to 10 — and caught it only because `node` re-parsed the object afterward. **Cut key -> object -> comma by exact offset. Then re-parse the whole file in `node` and assert lesson count, zero dangling refs, and zero orphan payloads. A JS syntax check alone will NOT catch a swallowed sibling.**

Neither is the LESSON uniform. Do not pattern-match across lessons:
- **Back-to-top markup has FOUR distinct forms** across L11-L16 (`text-align: right; margin-top: 25px` / `text-align:right; margin-top:10px` / `text-align: right` / `margin-top: 22px`).
- **Bonus mysteries are `h3` in L11/L15/L16, `h4` in L13/L14, and heading-less styled `<div>` cards in L12.**
- **L11's "Step N" headings also appear in Section 8A.4 theory** (the cliff-arithmetic derivation), not only in Section 6. A regex on "Step N" wires the lesson into the wrong section.

Hand-place every anchor, `assert count==1` on each, and audit each link against the heading it ACTUALLY landed under.

---

## 12. DOCUMENT WORKFLOW (v8.24 — REWRITTEN, S36)

### 12.1 EVERYTHING LIVES IN THE REPO
`github.com/Weymuth/zumo` is not just the published site — it is the **whole project**. The repo root carries this Bible, `LIVE_ZUMO_TEXTBOOK.md`, every session handoff, `gate_payload_match.py`, `pio_harness.sh`, `extract_project.py`, `IMAGE_SHOT_LIST.md`, `ROBOCUP_RESCUE_LINE_2026.md`, `PUSH_WORKFLOW.md`, and the web tools (`newproject.html`, `timer.html`, `index.html`, and the AI Tutor at `tutor/tutor.html` + `tutor/worker.js` — see §20). Lessons live in `lessons/`, art in `images/`.

**Therefore: SESSION OPEN IS A CLONE, NOT AN UPLOAD.**
```bash
git clone --depth 1 https://github.com/Weymuth/zumo.git
grep -oE "Bible version: v[0-9.]+" zumo/ZUMO_SUPER_BIBLE.md
grep -oE "Project Maker v2\.[0-9]+"  zumo/newproject.html
# NOTE the -E and the "+". With a greedy "*" the pattern matches its own
# example in this Bible and returns a bogus second line. Require >=1 digit.
```
Then verify LIVE.md's date, status, and lesson versions against the clone. **If LIVE.md and the Bible disagree, ASK DJ — never decide unilaterally.** Use a fresh `--depth 1` clone for every verification batch; never reuse a stale one.

### 12.2 SESSION CLOSE — ONE ZIP, FULL REPO LAYOUT, EVERY CHANGED FILE
Deliver **one** zip per session, arranged in repo layout with **final repo filenames** (`lessons/Lesson_10.html`, not `Lesson_10_Obstacles_v02_1_5.html`). DJ extracts it over the clone, commits once, pushes once. `PUSH_WORKFLOW.md` (in the repo) is the click-by-click for the human side.

**THE ZIP CARRIES EVERYTHING THAT CHANGED — INCLUDING ROOT DOCS.** Bible, LIVE.md, and the new handoff go in the zip alongside the lessons and the Maker, because they are all repo files. Splitting them into "push files" and "project-folder files" is a **mistake** (S36 made it): one commit carries any mix of folders, so a split delivery just invites a version mismatch between the repo and DJ's copies. There is no project folder to maintain separately — the next clone brings the current Bible and LIVE.md down with it.

**⚠️ A ZIP CANNOT DELETE.** Removals — retired handoffs, orphaned images — must ship as explicit `git rm` lines in the close note, to ride the same commit:
```bash
git rm ZUMO_S<N-1>_HANDOFF.md
git rm images/<orphaned assets>
```

**Staging rule (unchanged):** the zip itself sits in the **outputs root**, flat. DJ cannot browse `/mnt/user-data/outputs` — a file that was never passed to `present_files` does not exist for him. Repo-layout subfolders live **inside** the zip; never stage loose deliverables in a subfolder.

### 12.3 WRITE ORDER AT CLOSE — LIVE.md IS WRITTEN **LAST**
The Bible, Maker, and gate get bumped *during* the session; LIVE.md's header describes the state *at close*. Write LIVE.md before those bumps are final and it records the opening state — a **write-ordering bug**, not a memory lapse, which is why "remember to update LIVE.md" is too weak to prevent it.

1. Build and gate every artifact.
2. Bump the Bible / Maker / gate.
3. **Regenerate LIVE.md** — `grep` the actual version strings out of the files just written. **Never hand-type a version from memory or from the session's opening state.** The version appears **twice** in LIVE.md (status line and source-of-truth banner) plus the LESSON STATE table — all must agree. Leave *historical* version mentions in per-session change blocks alone.
4. **Write the handoff** — `ZUMO_S<N+1>_HANDOFF.md`, versions grepped from the same artifacts. It opens by telling the next session to **verify the previous push landed**, with concrete tells (expected Maker version, expected link counts) — not "check that it pushed."
5. Zip, `present_files`, and state plainly which file replaces which and what must be `git rm`'d.

**See §12.6** — LIVE.md is written when the last version-changing edit lands (not only at close), an omitted LIVE.md makes a push incomplete, and session open runs a drift check against the files.

### 12.4 VERIFY A PUSH BY FRESH CLONE — AND CHECK **WHICH VERSION** LANDED
Not merely that a commit exists. S33 had two false-positive pushes: one where nothing committed, one where the *superseded* build went up because two files with the same name sat in Downloads. md5 every delivered file against the clone.

### 12.5 SOURCE-OF-TRUTH HIERARCHY
`ZUMO_SUPER_BIBLE.md` (specs) → `LIVE_ZUMO_TEXTBOOK.md` (session state) → the handoff prompt.
Surface any discrepancy to DJ; do not resolve it unilaterally.
*(`ZUMO_Callout_Standard_v1.md` retired at v8.8 — callout templates live in §8.)*

### 12.6 LIVE.md STALENESS IS A **STRUCTURAL** FAILURE — CLOSE THE WINDOW
§12.3 puts LIVE.md last and explains why a reminder cannot enforce it. What §12.3 does not cover is the session that **ends before reaching step 3** — and that is the failure that actually recurs. S54 pushed eleven challenge files, a Maker bump and a graphic without regenerating LIVE.md; S55 pushed L01 v03.3.0 and Maker v2.38 and did the same. Two consecutive sessions left the file describing a state two sessions old, and the next session opened on it. S55 burned **four attempts** on re-diagnosis, three of them building on version numbers that were simply wrong.

**A. Write LIVE.md when the last version-changing edit lands — then re-verify at close.**
§12.3's hazard is recording the *opening* state. That hazard ends the moment the final bump is decided; it does not require the session to finish. Write LIVE.md at that point and re-verify it in step 3. A session that dies afterward still leaves LIVE.md correct. This does not relax §12.3's ordering — steps 1–5 are unchanged — it removes the window in which a dead session leaves nothing behind.

**B. A push that changes a version and omits LIVE.md is an INCOMPLETE PUSH.**
Not an oversight to catch next time — a defect of the same class as a challenge card that disagrees with its file (§11). If the zip carries a bumped lesson, Maker, Bible or gate, it carries LIVE.md. State it in the close note.

**C. Session open runs a DRIFT CHECK, not a read.**
Every take that went wrong in S55 went wrong *before writing any code*, on state it accepted instead of verified. After the clone, grep the files themselves and compare to LIVE.md's claims:

```
grep -o "Lesson version: v[0-9.]*" lessons/Lesson_NN.html
grep -oE "Project Maker v2\.[0-9]+" newproject.html | head -1
#   cross-check: grep -oE "v2\.[0-9]+" newproject.html | sort -V -u | tail -1
#   NOTE: plain `sort -u` is WRONG here — it sorts alphabetically and returns v2.9 over v2.38.
grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md
```

**The files win. Always.** If they disagree with LIVE.md, say so in the session's FIRST message, and resolve it before any queued work:
1. **Ask DJ for a newer LIVE.md** — the previous session may have written one that never got pushed. An uploaded current file beats a reconstruction.
2. If none exists, **regenerate LIVE.md from the verified files** as the session's first task.

Do not proceed into queued work on a LIVE.md known to be stale. The cost of regenerating it is minutes; the cost of a session built on stale versions is the session.


### 12.4 VERIFICATION DISCIPLINE — CACHES LIE (v8.37 — LOCKED, S58)
When confirming a push, do NOT trust the first read:
- **Shallow-clone lag** — for ~1–2 min after a push a `--depth 1` clone serves the PRIOR commit. `sleep 40` and re-clone before concluding a push failed (this looked like a failed push twice in S58; both were lag).
- **`git show --stat HEAD` on a shallow clone LIES about a commit's scope** — with no parent commit present it lists the ENTIRE tree as "added." Do not use it to judge what a commit changed (it caused a false "200 files over-committed" alarm in S58; the files were pre-existing). Textbook case of §11 AUDIT FALSE-POSITIVE DISCIPLINE — a tool reports candidates, not verdicts.
- **`raw.githubusercontent.com` caches ~5 min; `api.github.com` rate-limits unauthenticated; `weymuth.github.io` is not in the bash allowlist** — the reliable verify is a fresh clone with an adequate wait, or asking DJ to eyeball the live page.
- **Upload-location trap** — a file meant for a subfolder can land in the repo root instead (happened with `tutor.html` → root in S58). If a subfolder change seems not to take, check for a stray root copy.

## 16. HARDWARE GROUND TRUTH (v8.25 — LOCKED, S39)

**These are physical facts about the Zumo 32U4 fleet. Do not re-litigate them; verify against source if in doubt, do not guess.** They lived only in session memory until S39 — this section is the durable backup.

### 16.1 GEAR-RATIO STICKER COLOR CODE
The assembled Zumo hides its gear ratio on a **colored sticker on the underside of the main board, visible in the battery compartment with batteries removed** (Pololu User's Guide 0J63 §1.1). The color IS the ratio:

| Sticker | Gear ratio | Character |
|---|---|---|
| **Green** | 50:1 HP | fastest, lowest torque |
| **Blue** | 75:1 HP | middle — **the classroom fleet** |
| **Red** | 100:1 HP | slowest, highest torque |

- **Our fleet is BLUE = 75:1.** Any lesson that names the ratio says 75:1.
- The motors carry NO external color dot; on an assembled robot the sticker is the only non-destructive ID (reading the motor SKU requires disassembly).
- If two robots disagree on how far "speed 200 for 2 s" travels, check the stickers before blaming the code — a different color is a different ratio.

### 16.2 TRIM POLARITY — LEFT MOTOR, BOOK-WIDE
`setSpeeds(speed + TRIM, speed)`. TRIM adjusts the **LEFT** motor only. Positive TRIM speeds the left wheel, pushing the robot RIGHT, correcting a LEFT curve (a robot curves toward its slower track). Verified against Pololu `FaceTowardsOpponent.ino`. This never changes, in any lesson. TRIM goes ONLY on open-loop straights — never in `turnDegrees()` (wheels oppose on purpose) or `followLine()` (P-control is already a closed loop). See §11 TRIM PLACEMENT RULE.

### 16.3 setSpeeds() HARD-CAPS AT ±400 — WHAT constrain() ACTUALLY PROTECTS
`setSpeeds()` clamps any argument beyond ±400 internally (like a VEX motor maxing out regardless of the number fed it). Therefore `constrain()` is **NOT** there to protect the motor. It matters when YOU reuse the speed number elsewhere — displaying it, logging it, feeding it into more math — where an out-of-range value (e.g. 415) would be wrong or confusing. Constrain your own variables so the number you see equals the number the motor gets.

### 16.4 THREE KINDS OF STOP — Zumo setSpeeds(0,0) IS A BRAKE
"Stop" is not one thing: **coast** (leads open, rolls to a halt, drifts past), **brake** (motor shorted across itself, stops promptly), **hold** (actively drives toward "stay here," uses power while still). On the Zumo, `setSpeeds(0, 0)` gives a **brake**-style stop — the driver shorts the motors. When a robot "won't stop where I told it," the question is often *which kind of stop* was used.

### 16.5 STALL CURRENT — ONE EVENT, TWO SYMPTOMS
Max current flows when a motor is powered but cannot turn (~1.5 A per motor on the Zumo, ~5× free-run). Two situations, same electrical event: (1) wheels held/robot jammed — energy dumps as heat, cooks the motor within seconds; (2) robot too heavy or mis-geared to move — motor pulls stall current and sits still. A robot that buzzes/strains but doesn't move is stalling and heating; cut power.

### 16.6 ENCODER AVERAGING — BOTH WHEELS
Distance/turn loops gate on `averageCounts()` (average of BOTH encoders), never one. A slipping or stiff wheel on the unwatched side ends the move early or late with no warning. See §11 ENCODER AVERAGING RULE.

### 16.7 SHARED PINS 20 & 4 — LINE vs PROXIMITY ARE MUTUALLY EXCLUSIVE
Pins 20 and 4 are physically shared between line sensors 2/4 (DN2/DN4) and the left/right proximity receivers. Five-sensor line following and three-proximity operation cannot run together. `initThreeSensors()` steals those pins back from line sensing; `initFrontSensor()` is the correct call when line sensing must survive (e.g. L10).

### 16.8 FLASH / RAM CEILING — 28,672 B / 2,560 B, PIO-TRUE, -flto
Real flash ceiling = **28,672 B** (32,768 − 4,096 bootloader), RAM = **2,560 B**, from `platform-atmelavr boards/a-star32U4.json`. PlatformIO enables `-flto` by default. All byte measurements use PIO-true flags. The old S25 harness used a fictional 32,768 B ceiling — those figures are wrong (byte re-audit of L10/L12–L15 is a deferred package).

### 16.9 EEPROM ADDRESS MAP — THE FLEET SHARES ONE FLAT 1,024 BYTES (v8.36 — LOCKED, S57)
EEPROM is 1,024 bytes (addresses 0–1023) with no filesystem and no protection: nothing prevents one
program from overwriting another's bytes. Two things in this course live there, and the split is canon:

| Address | Owner | Contents |
|---|---|---|
| 0 – 511 | Lesson 16 | the `Saved` struct — magic `0x16`, gains, baseline (`EEPROM_ADDR = 0`) |
| 512 – 543 | Lesson 1 / teacher utility | magic `0x5A` + robot name, up to 20 chars + terminator (`NAME_ADDR = 512`) |
| 544 – 1023 | unclaimed | free for student enhancements |

Source of truth = `ZUMO_NAME_WRITER_main.cpp` (repo root), whose header comment carries the same map.
The names are written once per robot before the term and survive every student upload, because an upload
replaces **flash**, not EEPROM. Any new EEPROM use — a lesson, a challenge, an L16 §7 enhancement — takes
its addresses from 544 up and is recorded here.

---

## 17. SVG / GRAPHIC CANON (v8.25 — LOCKED, S39)

House style for every book diagram. Lived only in memory until S39.

- **Canvas:** `viewBox="0 0 1100 850"` (standard). Taller/shorter is allowed when content needs it; width stays 1100.
- **Title band:** rounded rect top-left, blue gradient `#1a5276 → #2e86ab`, white bold title, lesson tag right-aligned in `#d6e9f2` ("Zumo 32U4 Robotics · Lesson N").
- **Arrows:** SINGLE-POLYGON arrowheads only. Never a rect shaft + separate triangle head — it produces buried-tip overlap artifacts. One `<polygon>` per head, aligned to the line/arc end.
- **Section colors:** §4–6 green `#3a7d5c` / `#2a5a42`; TDP blue `#1a5276` for structure. Match the lesson's part when the graphic belongs to one.
- **Graphic number** bottom-right in `#9aa0a6` ("GRAPHIC N.NN").
- **File / number spaces:** IMAGE and GRAPHIC are SEPARATE number spaces (`L03_IMAGE_3-16` and `L03_GRAPHIC_3-16` legitimately coexist — see §10). Audit art against `images/` in a fresh clone, never against the lesson alone.

### 17.1 textLength IS A TRAP — STRETCH ONLY, NOT FIT
`textLength` on a `<text>` forces the string to that exact width. When the value **exceeds** the text's natural width it pads every character gap — a visible letter-spacing defect (S39 found this in GRAPHIC 3.7: `textLength="560"` on a ~408 px monospace line stretched `motors.setSpeeds(...)`). When the value is **≤** natural width it constrains text to fit a box and is fine. **`textLength` appears in ~30 book SVGs — a per-file audit (over-stretch vs. fit-to-width) is a deferred package; do NOT blind-replace.** A new SVG should omit `textLength` unless it is deliberately constraining text to a known box width.

### 17.2 QA EVERY SVG BEFORE SHIPPING
Render to PNG with `cairosvg` and eyeball it. A malformed path or an over-stretched line passes a syntax check but looks broken. Present previews to DJ for sign-off on any new or changed graphic.

---

## 18. CHALLENGE-DESIGN CANON (v8.26 — NEW SECTION, S40; §18.4 type-explainer added v8.30, S45)

Rules for how a §9 challenge is *designed* — distinct from §6.12 (the card's visual skin) and §9 (its PART placement). These govern what a challenge must teach and reinforce, and how a challenge **starter** is shaped.

### 18.1 THE SAXON SPIRAL — EACH LESSON REINFORCES PRIOR CONCEPTS
Modeled on Saxon Math's distributed practice: **each lesson's challenges reinforce 1–2 PRIOR concepts alongside the new one**, so skills are re-exercised across the book instead of taught once and dropped. Committed book-wide (DJ, S40, "even though it's a pain").

- **Rollout, not retrofit:** apply **going forward, lesson by lesson**, as part of the walkthroughs in progress. The spiral deepens naturally in later lessons (more prior concepts exist to draw on). **Do NOT force it into L01/L02** — nothing precedes them to review.
- **One new concept per rung.** A challenge ladder climbs monotonically: each rung introduces exactly one distinct new concept; the spiraled prior skill rides alongside as reinforcement, never as the rung's own new idea.

### 18.2 SPIRAL MARKER CONVENTION (LOCKED)
Two markers, both required on a spiraled challenge:
- **(a) Header line** — a blue **"🔁 Builds on:"** line at the **top of the challenge card**, naming the precise source **in words** (e.g. "🔁 Builds on: the `if` comparison from L03, the OLED print from L02"). *(Student-facing header renamed from "Spiraled skills" → "Builds on" in v8.27; "spiral" stays the teacher-side method name in prose.)*
- **(b) Inline stars** — **⭐ numbered stars** placed inline at the point of use, the **source lesson number inside the star**, as a wayfinding breadcrumb back to where the skill was taught.
  - **RENDERING (LOCKED, DJ ruling S43):** an inline star is the **actual SVG asset**, not an emoji — `<img>` the `spiral_star_NN.svg` file so students see the real gold-gradient numbered star both in the "🔁 Builds on:" explainer example AND at every point of use. Emoji ⭐ is used ONLY in the literal header text `🔁 Builds on:` (a glyph, not a lesson-numbered marker).
  - **Canonical inline-star tag** (Canvas needs ABSOLUTE raw URLs — never relative `images/…`):
    `<img src="https://raw.githubusercontent.com/Weymuth/zumo/main/images/spiral_star_NN.svg" alt="Spiral review from Lesson NN" style="height: 1.1em; vertical-align: middle; margin: 0 2px;">`
    Star SVGs are square 200×200; a fixed `height` keeps them line-sized. Do NOT use `max-width: 100%` on a star (that is the figure/diagram convention). `NN` is the ZERO-PADDED source lesson number and must match the `spiral_star_NN.svg` filename.
  - **First book-wide appearance:** L02 §9 "🔁 Builds on:" explainer callout (S43), which introduces the mark once before L03's first marked card (Battery Warning). Any new marked card reuses the tag above verbatim.
- **Assets:** `spiral_star_01`…`spiral_star_16` (16 SVGs, `images/`) — gold-gradient star (`#FFD34D → #F5A623`), `#1a5276` **vector-path** number (not font text — renderer-proof, centered, uniform width). Built S40, DJ-approved.

### 18.3 CHALLENGE-TEMPLATE PRINCIPLES (LOCKED, DJ ruling S44 — REVERSES the S40 minimal-skeleton rule; term set S48)
**TERM (DJ ruling S48):** the starter a challenge ships is a **challenge template** — that is its name project-wide (Bible, lesson cards, Maker labels). "Starter" remains fine as a generic synonym in prose; "scaffold" is NOT used for this sense (it still names the TDP accumulation in §14 and the theory-first build in §5).

A **challenge template** is the **full section-header template** — the same structure every lesson program has — NOT a stripped-down skeleton and NOT the finished lesson code. Students are used to seeing the whole template; a bare skeleton reads as unfamiliar and a finished program overwhelms. The challenge template ships the complete structure with the **concept being taught left blank** in a marked landing zone.

- **Every standard section header the program needs is present, in canonical order — none dropped just because a step hasn't filled it yet:** `HARDWARE OBJECTS` · `CONSTANTS` (L03 vocab: `CONFIGURATION`) · `FUNCTION PROTOTYPES` · `GLOBAL VARIABLES` (L03 vocab: `STATE VARIABLES`) · `HELPER FUNCTIONS`, around `setup()` and `loop()`. The header NAMES vary by lesson vocabulary, but the SET and ORDER are canonical; dropping a header is the defect this rule prevents (S51: the ≥L4 `mainCpp()` scaffold was missing `GLOBAL VARIABLES` — the L04 Step-2 landing zone — until Maker v2.33). A single-concept challenge starter may mark a genuinely unused section `// (none needed for this challenge)`; a multi-step program scaffold (e.g. the L04 Main build) shows the header with a blank body for the student to fill across steps.
- **Hardware objects pre-placed** — the object(s) the challenge needs (e.g. `Zumo32U4Motors motors;`).
- **CONFIGURATION constants seeded**, following the §11 blank convention: a tunable ships as `= 0` with the starting guess in the comment (`const int RUN_MS = 0;   // <-- YOUR NUMBER. Try 1000 (1 s).`); a fixed value ships with its number and a short note.
- **A marked landing zone:** a clear `// write your code here` where the taught concept goes, followed by numbered step hints. The taught concept itself is NOT pre-written.
- **`setup()` / `loop()` present but NOT re-explained** — taught in L01 §5.3 and L02; re-teaching them in every starter is noise. An empty `loop()` carries a one-line note of why (`// (empty - the run happens once, in setup)`).
- **The Maker wrapper supplies the top of the file.** `mainCpp()` auto-prepends the banner comment (`LESSON NN - <title>`, AUTHOR, DATE), the `#include <Zumo32U4.h>`, AND the MY PLAN block. **A payload body therefore STARTS at `// ===== HARDWARE OBJECTS =====`** and must NOT contain the banner, include, or MY PLAN, or they double. (MY PLAN still ships blank for the student — but it comes from the wrapper, not the payload.)
- **CHAT-DISPLAY RULE (S45):** when *showing* a starter to DJ in chat, PREPEND the wrapper header (`#include <Zumo32U4.h>` + MY PLAN block) so what DJ sees matches what the "make this folder for me" link generates. Pasting the raw payload body (which starts at `HARDWARE OBJECTS`, no include) is misleading — a hand-built copy of it fails to compile (`'Zumo32U4Motors' does not name a type`, `'delay' not declared`). The stored body is correct; the chat display must be the *generated file*, not the payload fragment.
- **A starter must not require a construct the book hasn't taught yet.** If the natural solution wants a `for`/`while` loop (not taught until L05), the landing zone directs an unrolled / by-hand approach and may forward-reference the later lesson. (L03 Ramp, S44: unrolled fixed steps that later motivate the L05 `for` loop.)

**Relation to the Maker (§15):** challenge `kind=` ids are unchanged by starter/label work; folder **labels** may take a `C##` prefix (rename the OUTPUT-folder string only, keep the `kind=` id, FLAT not subfolders — PlatformIO wants one level). Verify `?kind=` challenge downloads deliver **starters, not solutions**.

### 18.4 TYPE-EXPLAINER CALLOUT (LOCKED, S45)
When a data type is first *introduced*, it appears in a **blue info callout** (`background-color: #e3f2fd; border-left: 4px solid #2196f3`) titled with a `</>` glyph, holding one short line per type — `type — plain-English description — code example`, each on its own white row. This is the reusable **type-explainer visual**: the *same look* is used every time a type gets its deeper treatment, so students recognize "a type is being explained" on sight.

- **First introduction (L02 §3.2b):** all five types students will write themselves appear together — `int`, `bool`, `float`, `long`, `char` — one line each. Deep prose follows the callout for the types in play *now* (int, bool).
- **Deferred deep dives reuse the same callout look** at the point of first use: `long` in L05 (timing), `float` in L07 (decimal math). `char` is named for completeness only — the book rarely needs it, so it gets no deep dive.
- **Forward-pointers must be verified against the code**, not guessed — grep for the first genuine declaration before naming a lesson (S45: an early draft pointed `float` at L05; it first appears in L07).

---

## 19. PER-LESSON LEARNING-MODE FILE (v8.32 — NEW SECTION, S48)

When a lesson's challenges are walked in **learner mode** (the Socratic path — DJ writes the challenge code himself, coached with leading questions), the walkthrough is captured in a companion file named **`ZUMO_LEARNMODE_LNN.md`** in the **repo root** (flat, not a subfolder). One file per lesson; created when that lesson is first walked.

- **What it holds:** a student-difficulty roll-up (per-step, per-challenge), per-challenge walkthrough detail, the Coach's Tips surfaced during the walk, and a queued-tasks list of "used-but-never-taught" and card/payload findings.
- **What it is NOT:** it is a **teacher-side teaching record**, not student-facing content and **not a Maker payload source**. A challenge template lives in the Maker (§18.3); the learn-mode file only *records the finds* that motivate template/prose edits. Do not build payloads from it.
- **Naming (LOCKED):** exchanges within a walk are tagged `L##_C##_W##` (Lesson-Challenge-Walkthrough-step). The file is `ZUMO_LEARNMODE_LNN.md`, zero-padded `NN`.
- **Downstream use:** these walkthroughs are the intended raw material for the **AI Tutor** (REBUILT & LIVE S58 — see §20) — the model that worked (isolate one new idea, let the wrong answer happen and correct in place, trace values by hand) is captured here for reuse.
- **Live today:** `ZUMO_LEARNMODE_L03.md` (S47). A separate `ZUMO_L03_TEMPLATES.md` holds the six draft L03 challenge templates + solutions — that one is **STAGING** (source-of-intent), not gate-verified payloads.

---

---

## 20. AI TUTOR & MACHINE MARKERS (v8.37 — NEW SECTION, S58)

The AI Tutor is LIVE: `tutor/tutor.html` (front-end) + a Cloudflare Worker at `zumosupport.weymuthd.workers.dev` (repo source-of-record `tutor/worker.js`). Founding principle — **anti-rot: it READS THE LIVE LESSONS at run time and embeds NO curriculum**, so it self-updates whenever a lesson is edited. The old tutor rotted precisely *because* it hardcoded the curriculum in the worker prompt (it taught the cut cliff feature, wrong lesson numbers, no L15/L16). **Never reintroduce embedded curriculum.**

**Architecture (for future edits):** the front-end, on lesson-select, fetches `../lessons/Lesson_NN.html` from Pages, strips the solution reveals (§20.1), fences `<pre>` as code, and POSTs `{messages, currentChallenge, lessonContent, lessonTitle}` to the worker. The worker injects `lessonContent` as authoritative "CURRENT LESSON" context, holds the `ANTHROPIC_API_KEY` server-side, and uses model `claude-sonnet-5` with prompt caching on the system block. To edit the worker: dash.cloudflare.com → Workers & Pages → `zumosupport` → Edit code → paste → Deploy, **AND** update `tutor/worker.js` in the repo (the repo copy is the source-of-record; the live copy runs on Cloudflare).

Two invisible machine markers make the tutor work. **Both are mandatory on any new reveal or challenge**, or the tutor silently degrades.

### 20.1 `data-reveal` ON EVERY `<details>` (LOCKED)
Every `<details>` reveal carries `data-reveal="TYPE"`:
- **`solution`** — a worked answer, the code that solves a challenge, **or a debugging-mystery reveal that shows the planted bug + its fix** (framing it as an "explanation" does not exempt it — if it hands over the answer, it is `solution`). **The tutor STRIPS every `data-reveal="solution"` before sending the lesson to the model**, so it never holds the answer key.
- KEPT (the tutor coaches from these): `hint` · `check` (check-your-work / expected output) · `mechanism` (conceptual how-it-works) · `troubleshoot` ("🔧 Problem:" diagnostics) · `catchup` (build-step states / Maker pointers) · `quiz` (knowledge-check answers).

RULES: (1) anything that gives away a graded challenge answer MUST be typed `solution`, or it leaks — **when unsure, type it `solution`** (safe default = withheld). (2) The tutor strips only *tagged* `<details data-reveal="solution">`; **a solution shown as open prose or a bare `<pre>` is NOT stripped and WILL reach the tutor** — to withhold a solution it must live inside a tagged `<details>`. (3) The keep/strip split is a one-line dial in the front-end; nothing is deleted from the lesson — students still see every reveal via click-to-reveal.

### 20.2 `data-challenge` ON EVERY CHALLENGE (LOCKED)
Every challenge unit carries, on its anchor element (the card div, the heading, or the label):
- `data-challenge="LL.N"` — lesson.sequence, e.g. `10.3` (matches the Maker convention); this is what the tutor parses.
- `id="challenge-N"` — sequential in-page anchor.
- `data-kind="challenge"` — or `"mystery"` for sabotage-mystery bonuses (numbered `LL.mN`). (`"discovery"` is reserved for the in-lesson practice builds if they are ever added to the picker.)
- `data-difficulty="easy|medium|tough|hard|advanced"` — the DOING axis of the split pill (§6.12b). Attribute name retained from the single-pill era so existing tooling does not break.
- `data-grasp="light|moderate|deep"` — the GRASPING axis (§6.12b). Present wherever a split pill is; absent on lessons not yet swept.

**The picker is built by querying `[data-challenge]`** — a challenge WITHOUT the marker silently vanishes from it (the tutor still helps via whole-lesson context, but the student cannot select it). L16's §9 "Project Tiers" are NOT challenges and stay lesson-level (no marker).

### 20.3 INVISIBLE AND MANDATORY ON NEW CONTENT (LOCKED)
`data-reveal` and `data-challenge` are attributes, not content — students see no change. Add them the moment a new reveal or challenge is authored. GATE at close: every `<details>` has a `data-reveal`; every challenge unit has a `data-challenge`. (S58 retrofit baseline: 347 reveals typed, 88 challenges tagged, L01–L15.)

### 20.4 FAVICON ON A PAGES PROJECT SITE (LOCKED)
GitHub Pages *project* sites do NOT auto-discover `/favicon.ico` at a subpath — the browser requests `weymuth.github.io/favicon.ico`, never `weymuth.github.io/zumo/favicon.ico`. So EVERY page needs an explicit `<link rel="icon" href="…favicon.ico">` in its `<head>`, path relative to that page's folder (root page → `favicon.ico`, `lessons/` and `tutor/` pages → `../favicon.ico`). Canvas strips head `<link>`s, so the favicon is a Pages-only benefit — a repo push is enough; a Canvas re-push gains nothing for it.

---

## 21. ROBOT ICON FAMILY (v8.39 — NEW SECTION, S61)

A set of matching robot "chooser" icons — one per robot the fleet might run — built to read as a single professionally designed family. Only the robot and its accent glow color change; frame, composition, lighting, line weight, and framing are identical across all of them. Staged for a future "pick your robot" page; **not yet in the book**.

### 21.1 FRAME SPEC (LOCKED — the shared template)
- Canvas **1254×1254**, rounded square.
- Border **inset 64 px** from each edge · **corner radius 95** · **stroke width 14**.
- ⚠️ **AS-BUILT DEVIATION (S63, DJ ruling "leave them for now"):** every live icon in `images/glowbots/` has a border inset of **10–18 px**, not 64. All five miss the same way (tight cluster, not scattered), which reads as the generator ignoring the inset instruction rather than five separate errors. **64 px remains the spec**; the shipped images are knowingly off it. Re-crop or regenerate when the family is next touched — this is an open debt, not a settled value.
- Panel fill (inside the border) near-black **`#010808`**; dark charcoal background.
- Robot fills **~75–80% of the panel**, centered, slight three-quarter view, never stretched vertically.
- Border = a crisp stroke plus a soft outer bloom, in the robot's accent color.
- No watermark, no Gemini sparkle/star, no extra decorative effects. Glow extends beyond the robot but never overpowers it.

### 21.2 ACCENT GLOW COLORS — CANONICAL IS THE TARGET; AS-BUILT IS RECORDED DRIFT (v8.42, S63)
**DJ ruling S63: the canonical column is the spec.** The as-built column records what is actually in the pushed PNGs. The two differ because the image generator only *approximated* the hex it was given — this is generator drift, **not** a design change, and the canonical value is what any regeneration, CSS glow, or future sibling icon targets.

As-built values are measured from the live `images/glowbots/` borders (median of 51 row samples down the left stroke, S63). Distance is plain RGB euclidean.

| Robot | Canonical (target) | As-built (measured, S63) | Δ |
|---|---|---|---|
| Zumo 32U4 OLED | `#42F5D7` (teal/aqua — intentionally cyan, not green) | `#41FCE8` | 18 |
| 3Pi+ 32U4 OLED | `#46F56C` (bright green) | `#7DF565` | **55** |
| ROMI 32U4 | `#FF4FBF` (magenta/pink) | `#F83D9C` | 40 |
| Balboa 32U4 | `#9A5BFF` (purple) | `#AE4EFA` | 24 |
| Zircon (soccer) | `#FF8A00` (orange) | `#FB7404` | 23 |

**3Pi+ is the outlier at Δ55** — visibly lighter and yellower than the canonical green. If the family is ever regenerated, 3Pi+ is the one to check first. The S61 "sampled" column (`#48D4D4`, `#3DAA54`, …) is retired: it was measured off the *first* uploads, which were replaced.

### 21.3 BUILD METHOD — TWO OUTPUTS, TWO METHODS (v8.42, S63 — SUPERSEDES the frame-swap-only rule)
**DJ ruling S63: the S61 "NEVER separate the robot from its glow" prohibition is lifted.** It was written from a failed attempt, not a working one. S63 separated robot+glow from the frame on all five robots — including the two §21.4 predicted would defeat it — and the cut succeeded. The family now has **two outputs**, each with its own method:

**(a) BORDERED — for buttons. Frame-swap.** Unchanged from S61: keep robot and glow together, crop just inside the source border ring, map into the panel, draw the shared border on top. The border ring supplies a hard silhouette that survives downsampling, which is why **buttons are always bordered** (DJ ruling S63).

**(b) GLOW — for images. Extract-and-cut.** Crop inside the border to drop the frame, then cut the robot+glow to transparency. Two findings make this work where S61 assumed it could not:

1. **Use edge-connected flood fill, never a global brightness threshold.** Background = dark **AND** reachable from the crop edge. Interior dark pixels are then untouchable by construction — Zircon's black PCB and the gaps in Balboa's roll cage survive because they never connect to the outside. This is the specific failure §21.4 described, and connectivity is the fix.
2. **Cut the falloff; do not preserve it.** The glow is painted *additively on black*, so its outer falloff **is** black. Keeping it as soft alpha reproduces it as a grey haze that is invisible on a dark background and reads as a dirty cloud on white. Keep alpha only within **~2 px of the solid body** and zero everything beyond.

**GLOW FLOOR: never export below 128 px** (DJ ruling S63). Downsampling re-hardens the cut edge into opaque pixels, and open-frame robots collapse into mush. Sizes are full · 256 · 128. For anything smaller, use the bordered set.

**QA RULE — CHECK ON WHITE.** Every glow defect found in S63 was invisible on a dark background and obvious on a light one. A dark-background QA sheet proves nothing about a transparent cutout.

### 21.4 WHY SOLID vs OPEN/DARK ROBOTS BEHAVE DIFFERENTLY (amended S63)
Solid, bright-bodied robots (Zumo tank body, 3Pi+ white disc) seal their own interior and lift off a black background under almost any method. Dark-bodied (Zircon PCB disc) and open-frame (Balboa roll cage) robots defeat a **brightness-threshold** cut — black-on-black is invisible to it, so interiors get eaten and open structure leaks. **They do not defeat an edge-connected cut** (21.3b), which is a connectivity test rather than a brightness test. The S61 conclusion that these robots resist extraction was a property of the method, not the robots.

**Balboa remains the hard case for a different reason: it is the only portrait robot** (bounding box ~1014×1154; every sibling is landscape). Forced into a square tile its height sets the scale, so it shrinks harder and leaves dead space at the sides. This is why the 128 px floor exists.

### 21.5 HARDWARE ACCURACY
Represent the real hardware; do not invent or simplify parts.
- **Zumo** — OLED version (Zumo 32U4 OLED).
- **3Pi+** — white chassis, correct PCB layout, OLED display.
- **ROMI** — correct gripper configuration + wheel geometry.
- **Balboa** — balancing frame, large side wheels, accurate PCB placement.
- **Zircon** — Teensy **4.1** (never 4.0; the 4.1 is noticeably longer), correct omni-wheel layout, circular PCB arrangement.

### 21.6 THE BORDERLESS "MARK"
A no-frame transparent cutout also exists per robot. The landing-page Textbook tile uses `Zumo_Robot_Mark.png` (repo root `images/`, live since S61, displayed at 52 px). The full transparent family now lives in `images/glowbots/` as the **glow** set (21.7). **Buttons use the bordered icon** (DJ ruling S63) — a transparent cutout has no silhouette at button size.

### 21.7 LIVE FILES — `images/glowbots/` (v8.42, S63)
Pushed S63, commit `12867ea`. **42 files**, flat, no subfolders.

| Set | Sizes | Count | Mode | Use |
|---|---|---|---|---|
| `{Robot}_bordered_{1254,256,128,64,52}.png` | 5 | 25 | RGB | **buttons** |
| `{Robot}_glow_{full,256,128}.png` | 3 | 15 | RGBA | **images** |
| `QA_extraction_check.png`, `QA_size_sheet.png` | — | 2 | RGB | working contact sheets, not assets |

`{Robot}` ∈ `Zumo` · `3Pi` · `Romi` · `Balboa` · `Zircon`. Glow full-size is **1186²** (1254 less the 34 px frame crop), not 1254².

**Uniformity is verified and must be maintained.** All five glow cutouts measure mean edge distance **1.28–1.32 px**, p95 **2.00**, halo reach **0–1 px**, and **zero opaque pixels on any edge** at every size. A new sibling icon must match this or it will visibly out-glow the family. The three tight cuts (Zumo, Romi, Zircon) were done by DJ in Photoshop and are the reference; 3Pi+ and Balboa were tightened to match (they had carried 57 px and 39 px of halo).

**Wanting a bigger glow later is recoverable** — apply it as a CSS drop-shadow on the tight PNG rather than baking it back into the image. That keeps the family uniform and tunable.

**Open debts on this family:** the 21.1 inset deviation · filenames are S63 working names, not a ruled convention · the `QA_*` sheets are committed alongside real assets and could be `git rm`'d.

---

## 22. TERMINAL OUTPUT COLOR CANON (v8.45 — NEW SECTION, S65)

Simulated PlatformIO console output is a **different medium** from a C++ code block, and it gets its own two-color rule. A student reads a terminal block to answer one question — *did it work?* — and the book should answer that question the same way the screen does, at a glance, before any words are read.

### 22.1 THE TWO COLORS (LOCKED)

| Meaning | Color | Applies to |
|---|---|---|
| **SUCCESS** | `#6a9955` | `[SUCCESS]` in a simulated build/upload result |
| **ERROR** | `#f14c4c` | the diagnostic line of a compiler/linker message |

**`#6a9955` is DJ-ruled (S65) and is deliberately the same green the code blocks use for `//` comments.** The real PlatformIO terminal renders `[SUCCESS]` in a brighter green (nearer `#23d18b`), but the book's existing L01 upload block already used `#6a9955`, and DJ ruled to keep it as the single canonical success green rather than introduce a second one. **Do not "correct" it toward the terminal's true green.** The color carrying two meanings across two block types is accepted: context disambiguates completely, because a comment never appears in console output and `[SUCCESS]` never appears in source.

`#f14c4c` is VS Code's dark-terminal ANSI bright-red — what the student actually sees when a build fails.

### 22.2 COLOR THE DIAGNOSTIC, NOT THE WHOLE BLOCK

A compiler message is three different things stacked, and only the first is an error:

```
src/main.cpp:9:1: error: expected ';' before 'ledYellow'    <- RED
 ledYellow(1);                                              <- plain #e8e8e8
 ^~~~~~~~~                                                  <- plain #e8e8e8
```

The **source echo** and the **caret marker** stay plain `#e8e8e8`. That is how the real terminal renders them, and it is also the pedagogy: the echoed line is the student's own code, and the whole point of L02's "the compiler points at the line AFTER the mistake" rule is that they look at that line and judge it themselves. Painting it red pre-judges it — and in the very case the rule is teaching, the echoed line is **innocent**.

Lines that take the red: `file:line:col: error:` · bare `error:` / `fatal error:` · `undefined reference to` · `collect2:` · `[FAILED]`.

### 22.3 SCOPE — TERMINAL BLOCKS ONLY

The rule applies **only** to `<pre>` blocks that simulate console output. It does **not** apply to:

- **Prose mentions.** "Look for SUCCESS in the terminal" stays plain text. Thirteen such mentions exist across L01–L06 and are correct as they are; prose does not wear terminal colors.
- **Inline `<code>` chips.** `SUCCESS` referenced as an inline token keeps the standard grey chip.
- **C++ source blocks.** A block containing the *word* error (a variable named `error`, a comment about errors, the P-control `error` term) is source, not output. **Detect terminal blocks by their console markers** — `error:` with the colon, `undefined reference`, `Writing |`, `Verifying |`, `[SUCCESS]`, `[FAILED]` — never by the bare word.
- **Pseudocode.** L12's `report SUCCESS (return true)` is plan-language inside a pseudocode block. Left alone.

Of 71 blocks book-wide containing the string "error", exactly **11** are genuine console output. The word alone is a false-positive generator — this is §11's audit-false-positive discipline applied to color.

### 22.4 AS APPLIED (S65)

Two `[SUCCESS]` instances greened (both L01 — the build-result block was plain, the upload-result block was already `#6a9955` and set the precedent). Fourteen diagnostic lines reddened across 11 blocks: L02 ×5, L07 ×9. Applied at L01 v03.6.2 · L02 v02.12.2 · L07 v04.5.1 — all minor bumps, visible banners unchanged per §5b.

**Open:** L03, L04, L05, L08, L09, L11, L12, L14, L15, L16 contain blocks matching the loose "error" grep but none matched the strict console-marker test. If a future depth pass adds real console output to any of them, it takes these colors.

---

## 23. GOING DEEPER — THE OPTIONAL PAGE (v8.45 — NEW SECTION, S65)

`going_deeper.html` at repo root. A standalone optional-reading page for the "but *why* does it work like
that?" questions the lessons deliberately postpone so students can get the robot moving.

### 23.1 WHAT IT IS AND IS NOT
- **Outside the 16-lesson numbering.** It is NOT Lesson 17. It has no lesson number, no `data-challenge`
  markers, no challenge cards, and **no entry in the Maker registry**.
- **Nothing on it is assessed.** Not on a milestone, a reading quiz, or an exit ticket. The page says so in
  its own opening paragraph, and that paragraph is load-bearing — it is what keeps the page from competing
  with the chapters.
- Linked from `index.html` in the **tools row** (next to Project Maker / Timer / AI Tutor), never from the
  lesson grid.
- Own version line: `<!-- Going Deeper version: vNN.NN.NN -->`, same three-digit scheme as a lesson.

### 23.2 THE ANCHOR RULE (DJ ruling S65: "focus of content needs to be the chapters")
**Every entry must open from something a chapter already teaches, and close with a "Back to the book" line
naming the lessons it came from.** An entry that cannot name its anchor does not belong on the page.

This rule is what excludes most general C++ material. Anonymous namespaces, rvalue references, RAII,
`constexpr`/`consteval`, `enum class`, lambdas, `std::string`, and desktop UART driver design were all
offered and all **rejected S65** — none appears in any Zumo program, and a student who chases them lands in
desktop C++ that will not compile on an AVR. The page must not become a place where the book competes with
itself for attention.

### 23.3 CHECK FOR DUPLICATION BEFORE WRITING AN ENTRY
An entry that re-teaches what a lesson already covers is worse than no entry: it splits the canon. **S65
drafted a fixed-point entry as if the topic were new and caught it only on audit — L12 §8A.3 already teaches
fixed point properly**, including the no-FPU reason and the 2^29 gyro unit. The entry was rewritten to build
on L12 and cite it. Run the same audit on every new entry: grep the book for the entry's key terms first.

### 23.4 AS BUILT (S65, v01.0.0)
Six collapsible `<details>` entries, dark theme matching `index.html`, VS Code Dark+ in code blocks:
ASCII/binary/baud (L02) · what `F()` really does — Harvard vs von Neumann (L02/L12/L16) · the four-stage
build chain (L01/L12/L16) · translation units and why eight files (L07) · fixed point applied to Kp
(L08/L12/L15) · class vs instance (L02). Collapsed by default, so the page does not read as a 17th chapter.

---

## 24. BOOK GATES — THE STANDING CONSISTENCY TOOL (v8.48–v8.49 — NEW SECTION, S65)

**`book_gates.py` (repo root, v1.0) runs every machine-checkable Bible rule against the whole book in one
pass.** Run it at session open (health check, like `pill_sweep.py`) and before EVERY delivery. A delivery
that has not passed the gates is incomplete — same class as §12.6's incomplete push.

### 24.1 WHY IT EXISTS
Three times in one session (S65), a fix DJ requested was applied to the named instance while the same defect
survived elsewhere: text labels fixed but not timer widgets; the banner VERSION fixed while its DATE stayed
wrong in the same string; a byte count corrected in prose but initially asserted from memory. Each time DJ
had to notice and re-ask. The failure mode is not carelessness on any single edit — it is **fixing the
instance instead of the class**. A gate encodes the class once, permanently, and removes the dependence on
any one session remembering to check.

### 24.2 THE RULE
**When a rule is canonized, its gate is written in the same session.** A Bible rule with no gate is a rule
that only holds where someone happened to look. Current gates: §5b version + date agreement · §22 terminal
colors · §4.1/4.2/4.3 construct names, marker uniqueness, picker-label uniqueness · §6.12b pill parity ·
tag balance across every site file · timer well-formedness · index link resolution · going_deeper link canon.

### 24.3 GATE THE WHOLE FIELD, NOT THE CAPTURED GROUP
The June/July date slipped through a "passing" §5b check because the regex captured only the version digits
out of a string that also carried a date. **A gate must compare the entire field it claims to guard, not the
substring that was easiest to capture.** When adding a gate, ask what else lives in the same string.

### 24.4 A COMPUTED CLAIM IS VERIFIED BY COMPUTATION
S65 published "17 characters, so 18 bytes" for a 16-character string — the one number that session that was
asserted from memory instead of computed, in a section whose entire point is teaching students to count
bytes. **Any arithmetic, count, or measurement that appears in student-facing prose is produced by running
the computation, never by recall** — the same discipline §11 already applies to version numbers ("grep the
file") extended to numbers of every kind.

### 24.5 THE DEPTH AUDIT + THE ROLLING HUMAN READ (v8.49 — S65, DJ ruling)

DJ's diagnosis of L02 — "lots of brief info, but not a lot of depth" — generalizes and now has a standing
process. Two layers:

**Machine layer (`book_gates.py` + the depth scan).** Used-vs-taught construct ratios, substance profile
(LEARN boxes / KEY terms / words-per-section), thin-section detection, cross-lesson promise verification,
arithmetic verification. Findings live in `DEPTH_AUDIT_S65.md` (repo root). §11 discipline applies doubly:
the S65 scan's bitwise/pointer hits were 100% false positives (progress bars, `<<<` markers, pseudocode
arrows), and its word-count detector flagged sections whose depth legitimately lives in a neighbor.
**A scan finding is a candidate until a human reads the section.**

**Human layer (the rolling read — DJ is doing this personally).** Every lesson gets a start-to-finish read
asking what no grep can: does each heading keep its promise; is each idea given a reason before a rule; could
a student who reads only this lesson do its challenges. Additionally, any lesson a session substantially
edits gets the read in that same session — all three S65 accuracy finds were in freshly-edited content, zero
in untouched content.

**Standing structural finding (S65, verified):** the teaching apparatus disappears at L11 — L11–L16 carry
ZERO 📖 LEARN boxes and near-zero 🔑 KEY terms while teaching the book's hardest material. Mostly a marking
fix (promote existing strong prose into the apparatus), queued as its own arc. L14 profiles thinnest
book-wide and goes first in the read.

---

### 24.6 STRUCTURE IS VERIFIED BY PARSE, NOT BY COUNT (v8.50 — S68, DJ ruling)

**A count-based tag check can be satisfied BY the bug it is supposed to catch.** Eight lessons shipped with
the Image Index panel's closing `</div>` in the wrong place; in six of them (L01, L12–L16) it sat *after*
`</html>`. Open/close counts balanced exactly — because the orphaned close balanced the panel that was never
closed. The `tag balance` gate returned PASS on every run for the entire life of the defect. The check was
arithmetically correct and structurally blind.

**Provenance (git-verified S68, not recalled):** L01 carried it from its first tracked commit — original
hand-authoring, never introduced by a session. L12–L16 acquired it in a *single* commit, `94acc10` "Session 35
Massive Update", 2026-07-14: the §6.5 conversion from flat `<h2>` headings to boxed sections. That transform is
**stateful** — each heading emits `</div>` to close the previous panel, then opens its own — so the final panel
in the file has no following heading to close it, and its terminator was parked at EOF. One off-by-one at the
tail of a stateful conversion, replicated five times because it was one script. It then survived 28 later
commits on L01 and 9–13 on the others.

**THE RULE: any gate asserting document structure runs a real parser and compares the resulting tree to the
intended shape.** Counting is evidence about a file; parsing is evidence about a document. `book_gates.py` v1.2
carries `structure: HTML parses to the intended shape` — a tag-stack parse of every site file, reporting the
swallowed open AND the stray close with line numbers, plus a hard assert that nothing follows `</html>`.
This is §24.3 ("gate the whole field, not the captured group") applied to structure: the field is the tree, the
captured group was the count.

**24.6a A PARSER IS NECESSARY AND NOT SUFFICIENT.** L06 and L07 parsed *clean* and were still wrong — well-formed
HTML with the lesson footer sealed inside the Image Index box, because the close was present but late. No parser
can see that: the document is valid, the meaning is not. Structural correctness therefore needs a second,
**semantic** assertion about what belongs inside which container. Gate: `structure: end matter sits outside the
section panel`. **When a structural gate is written, ask what a well-formed-but-wrong version would look like and
gate that too.**

**24.6b CONTROL-RUN EVERY NEW GATE AGAINST THE UNFIXED SOURCE.** A gate that has only ever been run against
corrected files is untested. Both S68 gates were run against the pre-fix clone and FAILED there (12 parse
problems across 6 files; 2 end-matter violations in L06/L07) before being trusted on the fixed set. A gate that
passes everywhere it has been pointed has proved nothing.

**24.6c AN AUDIT GREP IS AN UNGATED GATE — CONTROL-RUN IT TOO.** (v8.51 — S69, DJ ruling) §24.6b binds gates,
which are versioned, reviewed and reused. An ad-hoc audit grep is a single-use gate that is none of those
things, and every S69 false positive came through that hole. Two, both in one session, both reported to DJ as
findings before being checked:

- **Inferred structure from a proxy string.** The timer iframes carry `label=Step+2`, so the audit concluded L02
  timed its *build steps*. The timers are attached to **TRY IT cards**; the label names the step the card belongs
  to. That produced "22 untimed build steps in L03/L04" and a proposal to insert 22 timers onto plain build prose
  — a device that exists nowhere in the book. DJ's confirmation is the only thing that stopped it.
- **Case-sensitivity.** `grep -oE "Step [0-9]+"` matched only the mixed-case text inside card headings; L02 writes
  its build steps as `STEP N:`. Nine steps were found where there are **eleven**, and the gap between card ids and
  step numbers was then reported as label "drift". All 11 labels were correct: `STEP 7` legitimately carries two
  TRY IT cards (`2.t7` Advanced, untimed; `2.t8` timed), so the duplicate "Step 7" is the truth.

**THE RULE, four parts.** (1) **Control-run the grep** against a case whose answer is independently visible —
read one lesson's structure by eye and confirm the count matches — *before* the number becomes a finding.
(2) **Never infer structure from label text**: check what element the matched string is attached to, not what it
says. A label describes; only the DOM position decides. (3) **Case-insensitive by default**, because the book's
own vocabulary varies by lesson and by era (`STEP`/`Step`, `CONFIGURATION`/`CONSTANTS`, "Coach's Tip" vs the bare
§6.6a labels) — a case-sensitive audit silently reports on a subset. (4) **Report findings as VERIFIED or
SUSPECTED**, never in one voice; a handoff or queue item enters the next session as SUSPECTED and stays there
until independently re-checked. S69 also reported the S68 queue's GRAPHIC 5.5 cone-angle suspicion as though it
were a defect; it was clean (tick bearings −90.0/0.0/+90.0, already matching the corrected 5.1).

This extends §11 ("a prose-keyword grep reports candidates, not verdicts", v8.36.2) from prose greps to
**structural** ones, and adds the reporting format. Note the standing pressure it works against: a five-item
audit reads as more valuable than a two-item one, so weak signals get promoted to lengthen the list. DJ's rule
governs — **a wrong finding costs 3× a blank one**, and an audit's length is not its worth.



*End of ZUMO SUPER BIBLE v8.*

---

## 25. THE EXIT-REGION CONSTRUCTS, THE READING QUIZ & PAGE CANON (v8.53 — NEW SECTION, S70)

### 25.1 WHY IT EXISTS

A §10 audit found **six differently-named written-response blocks** doing overlapping jobs, spread unevenly across the book, with **L13 and L15 carrying none at all**. Two of them shared the name *STOP & PROCESS* while running opposite mechanisms: L01/L02's was *write it in your notebook*, L03's was *answer from your head, then click to compare*. Same label, different pedagogy. This is the §4.1 disease — one name, several meanings — reappearing in the exit region.

DJ ruled **four constructs**, each with one job.

### 25.2 THE FOUR CONSTRUCTS

| Construct | Where | Count | Job | Reveals? |
|---|---|---|---|---|
| 🧠 **Mental Knowledge Check** | last seam before hands-on work (before §6 Build It in L01) | **3–5** | did you READ | yes — `data-reveal="quiz"` |
| 🧠 **Knowledge Check** | §10 | # (scales with the lesson) | did you UNDERSTAND WHAT YOU BUILT | yes |
| ☐ **Technical Skills — Can you…?** | §10 | = the lesson's objectives | self-audit | no |
| ✍️ **Reflection** | §10 | 1–3 | feeds the Notebook/TDP | **no — never** |

**THE SPLIT IS RECALL vs APPLY, NOT SECTION NUMBER.** Mental asks the student to *name it, define it, state it*. Knowledge Check asks them to *predict it, trace it, explain why*. This rule was chosen because the reading is not contiguous — L01 runs read(§1–3) → do(§4 Install) → read(§5) → do(§6+), so any placement rule keyed to section numbers breaks on the first lesson. **A hands-on section in the middle does not mean the reading has ended** (S70: `setup()`/`loop()` was wrongly excluded from L01's Mental block on exactly that error; §5 is reading, and in a flipped classroom the student reads the whole lesson the night before).

**EVERY ITEM NAMES ITS §.** `(§3.3)`, `(§5.3, §5.4)`. This is not new — L03's live quiz block already does it and tells students the section number is where to re-read. §25 makes it canon. It also gives the bell-ringer its map: a missed item points at a section.

**RETIRED NAMES** (§4.1 class, add to the `no retired construct names` gate as each lesson converts): *STOP & PROCESS* (both senses) · *Conceptual Understanding* · *Check Your Understanding* · *Reflection Questions* · *Explain It in Writing*.

### 25.3 THE READING QUIZ (Canvas)

The flipped design gates build time on a pre-class Canvas quiz — short, auto-graded, **one attempt**, opens before class and locks at the bell, worth 20%. It is a **soft gate**: fail it and you re-read and retake, you are never locked out of the course. **The quizzes do not exist yet** (Bible line 733 read *quiz feature deferred*); the Mental Knowledge Check is their source.

**DESIGN RULE — EASY IF YOU READ, HARD IF YOU DIDN'T (DJ, S70).** Every quiz item must be answerable from **a single stated fact in the prose**, and must name the § it came from. Retrieval, not inference. If answering needs the robot in hand or a chain of reasoning, it belongs in the Knowledge Check or the Reflection, not the quiz.

**CLOSED BOOK, SO ITEMS SHIP IN PAIRS.** DJ ruled against open-book — open book means they look it up instead of reading the night before. So each item exists twice: the **rehearsal** in the lesson with its answer revealed, and a **variant** in Canvas testing the same fact in different words. Scale: 3–5 × 16 = **48–80 pairs.**

**AUTHOR THE VARIANT INLINE, WHILE THE § IS OPEN.** The variant stem is written as an HTML comment directly above its rehearsal item:
```
<!-- QUIZVARIANT 1.5: One of the two functions runs once and the other runs forever. Which is which?
     (answer: setup() once at power-on/reset; loop() forever afterward) -->
```
Costs nothing now, harvestable by script later. **Book first, Canvas after** (DJ ruling) — § numbers move while the book is under construction, and a quiz item that names its § would be authored against a moving target.

### 25.4 WARM-UPS AND THE SPIRAL

**Warm-ups run L02–L16 — fifteen lessons.** L01 cannot host one: it is the install lesson, there is no prior lesson to reinforce and no toolchain until §4.

The construct (as built in L02, and the strongest in the book): timed micro-fixes on already-working code — *work independently, no asking for help, limited time, it is supposed to be hard*. The hint unlocks only **after** time is up and ends by asking how you could have known without it. One reusable sandbox folder, not a copy per task.

**SPIRALS LIVE IN WARM-UPS AND CHALLENGES** (DJ ruling S70). Census at S70: 27 markers, of which **5 name no lesson** (L04 §8A.6–8A.9 and one L03 marker are *within-lesson* build-ons wearing the 🔁) — so **22 true cross-lesson spirals**. Coverage, not volume, is the defect:

- **Never spiraled back to: L01, L11, L12, L13, L14, L15, L16.** L11–L15 are thin partly by geometry; **L01 and L07/L08/L09 are the real gap** — the 8-file architecture, P-control and the state machine are the three hardest ⭐ demo lessons and each is reinforced exactly once.
- Well covered: L03 ×5 · L05 ×4 · L06 ×4 · L02 ×3 · L04 ×3. Reach runs 1–8 lessons back, median ~3.

**THE AIMING RULE:** each lesson's three warm-ups reinforce **(1)** the previous lesson, **(2)** something 3–6 back, **(3)** something from the under-cited set. Three × fifteen = **45 slots against 22 today**, so the fix needs no new challenges.

**Live marker wording is `🔁 Builds on:`** — "Spiraled skills" returns zero book-wide and is retired. **OPEN:** the 🔁 currently does two jobs (cross-lesson spiral vs within-lesson build-on); until they are separated the spiral count is inflated ~18% and the coverage matrix cannot be trusted.

### 25.5 OBJECTIVES COME FROM THE CHECKLIST

DJ ruling S70, inverting the obvious direction: **§2 Objectives are rewritten to match the §10 Technical Skills checklist**, not the other way round. The checklists are concrete and observable ("Can you calculate COUNTS_PER_CM"); objectives drift abstract. Checklist length currently runs 1–13 across the book because nothing anchors it — after this pass §2 is the anchor and the two can never disagree. **Not yet applied.**

### 25.6 HEADER, FOOTER & HIDDEN BANNER — ALL 17 PAGES

Seventeen pages: 16 lessons + `going_deeper.html`. Verified S70 by **markup-skeleton hash** (tags + inline styles, text stripped) — header `4fdedafb` ×17, footer `aff5311e` ×17.

**HEADER — five lines**, the hero block, `linear-gradient(to bottom, #1a5276 0%, #2e86ab 100%)`, white:
```
LESSON 11
Time Lies, Distance Doesn't
Encoder-Based Gap Crossing
Zumo 32U4 Robotics • PlatformIO Edition
Version 02.7 — July 2026
```

**FOOTER — four lines.** The header's shape with the version line replaced by credits, since the version is now hidden per §5b:
```
LESSON 11 · Time Lies, Distance Doesn't
Encoder-Based Gap Crossing
Zumo 32U4 Robotics • PlatformIO Edition
© 2026 RoboLore · Written and compiled by DJ Weymuth and Claude AI
```

**THE HERO TITLE IS CANONICAL.** S70 found **three** live title sources disagreeing: the header hero, the `<title>` tag, and the §6.5a strip tooltip. They differ on **L01, L02, L03, L08, L15** (e.g. hero *Sense, Decide, Act* vs tab/strip *Hello, Robot!*). Footers and hidden banners are built from the **hero**. **OPEN:** `<title>` and the strip are untouched and still disagree.

**COPYRIGHT.** `© 2026 RoboLore`. Notice is not required for protection (automatic since 1989) but forecloses an innocent-infringement defence. *All rights reserved* is dead — a Buenos Aires Convention relic with no legal effect since ~2000 — and is NOT used. **No LLC/Inc suffix**: those are reserved designations and using one for an unregistered entity misrepresents legal status. The AI credit line is a **disclosure**, not a courtesy: the US Copyright Office holds purely AI-generated material uncopyrightable and requires AI content to be disclosed and disclaimed on registration; the human authorship (selection, arrangement, curriculum design, DJ's prose) is what is protected. **OPEN — the work-for-hire question:** the book was built for a course DJ teaches, on the school's Canvas, with school robots. That is the fact pattern the work-made-for-hire exception is written about, and it is answered by the Mercersburg faculty handbook, not by the name on the footer. Matters for the parked monetization/ebook item. Not legal advice.

### 25.6a THE TOOL PAGES ARE NOT CHAPTERS — AND LAYOUT IS GATED (v8.54, S70)

The §25.6 header/footer/hidden-banner canon binds the **17 content pages only**. `index.html`, `newproject.html`, `timer.html` and `tutor/tutor.html` are a landing page and three utilities — several render inside iframes — and giving them chapter furniture would be cargo-culting the rule onto pages it was never scoped to. What they owe is a **version line** (§5b) and nothing else. `index.html` is the one exception on credits: it is the public front door, so it carries `© 2026 RoboLore · Written and compiled by DJ Weymuth and Claude AI` beneath its existing site line — the notice does its real work at first contact, not buried in seventeen chapter footers.

**LAYOUT IS NOW GATED, because the recurring defect was never the markup — it was the file's location.** S70 shipped the same class of failure twice in one session: `going_deeper.html` uploaded into `lessons/` (leaving 23 lesson links and the index serving the stale root copy) and then `tutor.html` uploaded to the root (leaving the live tutor unversioned and the new file an orphan nothing linked to). Both looked like successful pushes. Neither was caught by any gate, because every gate checked *contents*.

`§12/§23 site layout: every page in its canonical place, no strays` (book_gates v1.5) asserts the exact set of 21 HTML pages and their paths — any extra page, any missing page, any page at the wrong path FAILS. Control-run three ways: a stray at root, a page moved into `lessons/` (fails as STRAY **and** MISSING, exactly reproducing the Going Deeper incident), and a stripped tool version line.

**A file in the wrong folder is a defect of the same class as wrong content** — and it is the one an upload-based workflow produces most easily, since a browser upload targets a folder and never questions it.

### 25.7 §9 IS THE HANDS, §10 IS THE HEAD

Full construct map (S70 census, 119 markers): Warm-Up §1 (4, L02 only) · TRY IT §3/§5/§8A (12) · Challenge §9 (87) · Mystery §9 (4, L11 only) · **Bonus Challenge §10 (12, L02/L03)**.

**Bonus challenges are misfiled.** They are practice, not assessment, and belong in §9 with their siblings. *Inferred: they landed in §10 because they were authored as an appendix rather than as part of the challenge set.* **Not yet moved.**

Student-facing vocabulary collapses from eleven names to five — **Warm-Up · Mental Knowledge Check · Challenge · Knowledge Check · Reflection** — with TRY IT, Mystery and Bonus absorbed as *types* inside §9. No exercise is deleted.

### 25.8 CAPS (so the page does not overwhelm)

Warm-ups **3** · Mental **3–5** · Knowledge Check **5** · Technical Skills = objective count · Reflection **1–3**. For scale, L03 today carries 12 checkboxes, 10 quiz items, 8 challenges and 6 bonus challenges.

### 25.9 STILL OPEN AT S70 CLOSE

Not built, not ruled, do not treat as done: warm-ups for L02–L16 · the spiral aiming rule applied · §2 objectives rewritten from the checklists · bonus challenges moved §10→§9 · a separate mark for within-lesson build-ons · **L13 and L15 still have no exit written-response block** · `<title>`/strip vs hero titles · L16 still has zero challenge cards · `going_deeper.html` footer contrast (`#666` on `#0f1117` ≈ 3.3:1, below 4.5:1) and its duplicated hero title · **no gate yet exists for §25** (§24.2: a rule without its gate holds only where someone looks).

### 25.10 BRAIN CHECK — THE KNOWLEDGE FAMILY NAME, LIVERY, COLUMN & CHECK-OFF (LOCKED, S71)

#### 25.10a THE FAMILY IS FOUR, AND THE COLUMN IS WHY (v8.59 — NEW, S73, DJ-ruled)

**There is no BC05.** The shared Brain Check column is a single 5,596-character block copied
byte-identical into every converted lesson (L01 == L02, verified), and its script is hardcoded to four:
the saved state array is length 4 and is discarded on load if it is any other length, the click handler
rejects any index past the fourth, and the skills unlock is wired to BC02 **by index**. A fifth block
would need a per-lesson column variant — three diverging copies of that script, in a family this section
marks LOCKED.

**RULE — a lesson's extra exit block folds into the BC it most resembles, as a labelled group.** L03 is
the live case: it carried two checkbox blocks, *Technical Skills — I can…* (8 capability items) and
*Problem-Solving — I have…* (4 process-audit items). DJ's first instinct was BC05; the cost above was
priced and the ruling changed. Both lists now live inside **BC02** under bold sub-labels **I can…** and
**I have…**, all twelve items carrying `data-bc-skill`. Nothing was deleted and both jobs stay visually
distinct.

**THE UNLOCK GENERALISES ON ITS OWN.** `allSkills()` loops over every `[data-bc-skill]` element rather
than a fixed count, so L02's 7-of-7 became L03's 12-of-12 with zero JavaScript edits. **Check whether the
mechanism already scales before writing a rule that assumes it does not.**

**COLUMN PLACEMENT IS PART OF THE COPY.** The block seats immediately before `</body>`. Appended after
`</html>` it renders but fails the *structure: HTML parses to the intended shape* gate — which is how S73
caught it.

**A §-CITATION IS VERIFIED BY CONTENT, NEVER BY PRESENCE** (restating v8.58.1, because this is where it
bites). Every converted item's cited § must be sliced and shown to contain the answer. Slice a subsection
by the **next subsection id**, never by the next top-level section anchor: a Brain Check block physically
sits between two sections, so an anchor-bounded slice swallows the quiz asking about the previous one and
reports the answer as present when it is not. That false positive nearly buried the L02 prototype defect.


**The four §25.2 exit-region constructs share ONE family name: BRAIN CHECK, numbered 01–04.** The constructs keep their §25.2 identities; the family name and number are prefixed in the header:
- Brain Check **01** · Mental Knowledge Check (before hands-on work)
- Brain Check **02** · Technical Skills ☐ (§10)
- Brain Check **03** · Knowledge Check (§10)
- Brain Check **04** · Reflection (§10)

Header canon: `BRAIN CHECK NN · CONSTRUCT NAME — subtitle`, icon image leading. One family name, four numbered members — this subsection exists so the §4.1 six-names disease cannot regrow here. Do NOT invent additional "Check" block names.

**Livery = §8 Type 10** (bg `#e8eaf6`, border-left `#3f51b5`, title `#283593`). All four wear it, including Technical Skills (pulled off Checkpoint green — a knowledge block is not a milestone banner) and the two blocks that formerly wore §9 Challenges plum (§25.7: §9 is the hands, §10 is the head; the color now agrees).

**Anchors:** each block carries `id="brain-check-0N"`. Gated (book_gates v1.6).

**THE COLUMN.** A fixed right-edge column (`id="brain-check-col"`, bounded by `BRAIN CHECK COLUMN START/END` marker comments — ONE block, edit whole) with the family emblem on top and pills 01–04 linking to the anchors. Ships ONLY in converted lessons — a lesson gets the column in the same edit that gives it the four blocks, never before (no dead links). The column hides below 700px viewport width via its own script (inline styles cannot media-query; this is the §6.5a self-hydration pattern).

**CHECK-OFF STATE.** Each block ends with a `data-bc-btn` toggle button. **Brain Check 02 is SKILL-GATED (S71, DJ-ruled):** every ☐ checklist item carries `data-bc-skill` and is tappable (☐→☑, green when checked; state in `localStorage` key `bc_LNN_sk`, array length derived at runtime from the tagged elements so the rule is lesson-agnostic); BC02's Mark-done button stays LOCKED (gray, 🔒 label, no-op) until every skill is checked. Unlock gates only the transition TO done — undo is always available, and un-checking a skill after marking done does not revoke the done flag. Gated: box-glyph count must equal `data-bc-skill` count in every converted lesson (book_gates v1.7).

**GATED-ITEM ACHIEVABILITY (S71).** A skill item behind the BC02 lock must be achievable by EVERY student who did the lesson. If an item depends on chance — "identify and fix an error" when a lucky student never hits one — the lesson MUST include a deliberate rep that produces the event on purpose (L01: the Break-It-On-Purpose upload-error rep at the end of §6 Step 6, power-off → failed upload → read → fix). Same defect class as §11 "a declared blank must be spent": the lock promoted a harmless unchecked box into a blocker on luck. This is a REVIEW rule (not machine-gateable): when converting a lesson, read its BC02 items and ask "can a student whose build went perfectly check every one?" — any NO gets a rep or a reword before the lock ships. State lives in `localStorage` key `bc_LNN` as a 4-element 0/1 array, key derived from the filename. Done paints pill + block icon + button green; the emblem flips to the Complete icon only at 4/4. **This is a personal tracker, per-browser, invisible to the teacher, and NOT a grade** — the Canvas reading quiz remains the real gate (§25.3); a student can self-mark 01 without answering honestly, and the two must never be conflated. The disclaimer lives in the column's `title` tooltip.

**THE ICON PAIR** (`images/BrainGear_Incomplete.png` gray `#454545` / `images/BrainGear_Complete.png` green `#24911b` + check):
- State is NEVER color-alone: the Complete artwork carries the check glyph, Incomplete does not — red-green colorblind-safe by construction.
- Incomplete is GRAY, not red — deliberate: §22 locks red as the ERROR color, and "not yet done" is a healthy state, not a failure. Do not "improve" incomplete to red.
- Both icons: interiors are TRANSPARENT (alpha-shaped, single stroke color); on a light backing interiors read white. Floor 24px; working range 32–128px. **Dark backings are FORBIDDEN without a light panel behind** — the linework vanishes (QA'd S71).
- Cut method per §21: edge-connected flood fill; the gray was rebuilt single-color-plus-alpha to match the green's structure exactly (S71; opaque light-interior px = 0 in both).

**Rollout:** L01 is the reference (v03.9.0, S71). Each lesson gains blocks + column together as it converts (S71 queue: L02, L03, then onward).

*(§25.9 above remains this section’s open-items ledger — §25 is not finished until that list is.)*

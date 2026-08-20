#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAYLOAD BYTE-MATCH GATE (Bible §11) — v1.9.0, S56 (S110: runs on stable filenames)
v1.9.0 (S176) THE GATE WAS ONE-DIRECTIONAL AND A DELETION PASSED SILENTLY. v1.8.0
closed one side of the line test; this closes the other. The derivation predicate is a
SUBSET test — every payload line must come from the lesson — so a payload that has LOST
a line is still a subset and the loss is structurally invisible. MEASURED, NOT
THEORISED: deleting the S172 kill-switch guard from `13/challenge_9_1_keep_sweeping`,
leaving Lesson_13.html untouched, left this gate printing PASS with the advisory count
unmoved at 635 — not one number changed. Fix: PAYLOAD_CENSUS pins every payload's
executable content by [count, md5] over STRIPPED lines, 216 entries, regenerated with
--update-census. The symmetric predicate was REJECTED, not overlooked: lessons
legitimately print code no payload carries (wrong-code examples, "before" versions, the
Serial-cut demos), so "every lesson line appears in a payload" is noise on day one.
TEN CONTROLS, one mutation per invocation, every restore md5-exact. TWO of them are the
arm's whole reason to exist, because derivation PASSES on both: a DELETED line, and two
executable lines REORDERED. Addition, value change and trailing-comment reword also
fire, but each ALREADY fails derivation, so the census adds no obligation there. SILENT
on reindentation, blank lines, whole-line comments and <<< markers. STATED SCOPE LIMIT
(rule 78): a pin asserts that content has not MOVED since a human blessed it, never
that it is CORRECT — a payload that shipped wrong and was pinned wrong stays wrong
silently. BOXED_FP carries the same limit; it is declared, not hidden.
v1.8.0 (S142) THE LINE TEST WAS A SUBSTRING TEST AND WAS BLIND ON ONE SIDE. The
line-wise fallback asked `l in corpus` — containment in the whole corpus TEXT — so a
payload line that has LOST a leading qualifier the lesson carries matched trivially as
a substring of the longer lesson line. MEASURED, NOT THEORISED: during the S142 static
pass, reverting exactly one of 136 payloads left this gate printing PASS. Additions it
always saw; a dropped `static`, `const` or `unsigned` it could not see AT ALL — which is
the §15.6 class it exists to hold. Now line EQUALITY against a stripped corpus line set;
both sides stripped, so indentation is still irrelevant and every payload that passed on
real derivation still passes (advisory count unchanged at 635). Control-run five shapes x
two gate versions from a snapshot with a byte-exact restore: untouched PASSES on both;
lost-static and lost-const PASS on the old gate and FAIL on the new; a foreign line and a
changed value FAIL on both, so nothing that used to be caught was lost.
v1.7.1 (S138) EXEMPTIONS RE-PINNED AFTER THE S137 STARTER FIX. This gate went PASS ->
FAIL (4) inside the S137 close push and the handoff still claimed PASS, because the gate
is NOT one of the 69 - nothing in book_gates.py runs it. S137 rewrote the L03 constrain
and ramp starters (button-B gate, stop-the-motors line, Lesson 5 -> Lesson 4 for-loop
pointer) and three EXEMPT keys are byte-exact line text, so rewriting the line orphaned
the key. Three entries repointed, one added. Census confirmed EXECUTABLE CODE: 0 - the
divergence was starter-only comment scaffolding throughout, which is exactly what these
exemptions exist for; the book's card is NOT the place for it (§18.3). LESSON: an EXEMPT
key that pins a LINE certifies a spelling, not a property - edit a starter and the
exemption silently dies.
v1.6.1 (S110) RE-PINNED. The five L01 fingerprints had been stale since S61 and nobody
could see it, because this gate needs `Lesson_NN_Topic_` filenames and the book stabilised
on `Lesson_NN.html` - so it did not fail, it CRASHED on the first file and was simply never
run. Run it with topic-suffixed symlinks. Traced in git: `8ab0c42` set the pinned values and
`63a9bfb` ("Session 61 - Coaches Callout") changed them, re-rating five headers - c01/c06/c09
MEDIUM->EASY and c10 HARD->MEDIUM, all four matching their cards. c11 was MISSED by that
sweep and still read [MEDIUM] against a card reading easy; corrected S110 by DJ ruling
("C11 is easy"), which also closed a one-character box overhang on that title line.
v1.6 BOXED-HEADER FINGERPRINTS. v1.5 made boxed instruction headers advisory so a
self-contained challenge file would not fail the gate for carrying its own working
instructions. That left a hole: an advisory line could be EDITED and the gate still
said PASS, so file instructions could drift away from the book's card prose unseen.
Fix: pin each boxed header with an md5 in BOXED_FP (below). The gate recomputes the
hash from the payload and fails on any change. Advisory means "not required to appear
in the book", NOT "unchecked". To change a header intentionally, edit it, run with
--update-fp to print the new manifest, and paste it in — the bump is deliberate.
v1.5 BOXED INSTRUCTION HEADERS ARE ADVISORY, NOT FAILING.
v1.5 BOXED INSTRUCTION HEADERS ARE ADVISORY, NOT FAILING. A challenge file's boxed
header (// ┌─┐ … // └─┘) is the student's working instructions, deliberately kept IN
the file so a student coding in one window never has to switch to the book for a step
(DJ ruling, S56). The book's §9 card carries the same instructions as prose — better
form for reading — plus the exact target line quoted verbatim. So a boxed-header line
that does not byte-match is a FORMAT difference, not missing content, and must not
fail the gate. Everything else still fails: EXECUTABLE CODE is never advisory.
Boxed lines are counted and reported under ADVISORY so drift stays visible.
v1.4 REPORTING FIX — the gate was UNDER-REPORTING and it cost a session.
v1.4 REPORTING FIX — the gate was UNDER-REPORTING and it cost a session.
Two truncations stacked: (a) only missing[0] was recorded per payload chunk, and
(b) only the first 20 fails were printed. L01 reported "FAIL (148)" while the true
count was 900, and the 20 visible lines were all comments — so three separate S55
sessions concluded the failure was comment-only scaffolding and proposed exempting
it. It was not: 146 of the 900 were executable code (an EEPROM name-reader present
in the Maker payloads and in NO lesson). Now: every missing line is recorded, the
print cap is 200 with an explicit "... N more", and a CATEGORY CENSUS separates
boxed comments / <<< markers / other comments / EXECUTABLE CODE. Read the census,
not the raw count.
v1.3 WHOLE-TEMPLATE STARTER EXEMPTIONS: Bible §18.3 was rewritten S44 (starters are
now the full section-header template, not a minimal skeleton). The S43 minimal-skeleton
exempt entries were replaced with the whole-template starter-only lines for L03
constrain/ramp (seeded CONFIG constants, landing-zone hint comments, empty-loop notes,
the L05 for-loop forward-reference). Same principle: these lines exist ONLY in the
starter and have no solution source to byte-derive from. Pattern recurs for future starters.
v1.2 STARTER-SCAFFOLDING EXEMPTIONS: challenge-starter payloads (Bible §18.3) carry
comment-only skeleton lines that exist ONLY in the starter (superseded by v1.3's set).
v1.1 INHERITANCE RULE: lesson N's corpus additionally includes lesson N-1's
'finished' payload bodies — inheriting lessons (L08+) copy the prior project
wholesale in Step 1, so files carried unchanged are canonical by construction.
Byte-strict: modified content must still appear in lesson N's own pres.
Prior: v1.4 S55, v1.0 S21
Verifies every Maker payload derives byte-exactly from canonical sources:
  1. the lesson HTML's decoded <pre> corpus (dark + light pres), OR
  2. the Maker's own template strings (skeleton glue inside mainCpp()).
Multi-file aware: object payloads check every file; string payloads check the body.
Method: payload text split into blank-line chunks; every chunk >= MIN_CHARS must
appear verbatim in (lesson pres + maker templates). Short glue lines exempt.
Also: PAYLOADS JSON parses (brace-matched), registry payload keys resolve,
JS passes node --check.
Usage: gate_payload_match.py newproject.html lesson2.html lesson3.html ...
       (lesson number read from filename Lesson_NN_*)
Exit 0 = ALL PASS.
"""
import re, sys, json, html as H, subprocess, os

MIN_CHARS = 30

# Documented exemptions: (lesson, payload_key, exact_line) -> reason.
# Only for lines that legitimately CANNOT byte-match any canonical source.
EXEMPT = {
    ("5", "step_6", "display.setLayout21x8();   // TEMPORARY - removed in Step 6"):
        "in-context adaptation: lesson comment is a placement instruction (S19 design)",
    ("5", "step_6", "drawBar(2, frontValue);   // TEMPORARY - removed in Step 6"):
        "in-context adaptation: lesson comment is a placement instruction (S19 design)",
    # S44: L03 whole-template challenge-starter scaffolding (Bible §18.3, rewritten S44).
    # Starter-only lines with no solution source to byte-derive from. Supersedes the S43
    # minimal-skeleton exemptions (those lines no longer exist after the whole-template rebuild).
    ("3", "constrain", "// (nothing to set up - press B to run, so put the robot down first)"):
        "L03 constrain whole-template starter (S44, §18.3; line rewritten S137 when the starter "
        "was gated on button B): starter-only comment, no derivation source",
    ("3", "constrain", "// (none needed for this challenge)"):
        "L03 constrain whole-template starter (S44, §18.3): starter-only comment, no derivation source",
    ("3", "constrain", "// write your code here"):
        "L03 constrain whole-template starter (S44, §18.3): starter-only comment, no derivation source",
    ("3", "ramp", "const int STEP_MS  = 0;    // <-- YOUR NUMBER. Pause between speed steps. Try 200."):
        "L03 ramp whole-template starter (S44, §18.3): seeded starter constant, no derivation source",
    ("3", "ramp", "const int MAX_SPEED = 200;  // the top speed you ease up to"):
        "L03 ramp whole-template starter (S44, §18.3): seeded starter constant, no derivation source",
    ("3", "constrain", "// 1. constrain each speed to +/- MAX_SPEED, feed into motors.setSpeeds(...)"):
        "L03 constrain whole-template starter (S44, §18.3): starter-only hint, no derivation source",
    ("3", "ramp", "// Ease the motors up to MAX_SPEED one step at a time, by hand."):
        "L03 ramp whole-template starter (S44, §18.3): starter-only landing-zone comment, no derivation source",
    ("3", "ramp", "// Set a low speed, wait STEP_MS, set a higher speed, wait again -"):
        "L03 ramp whole-template starter (S44, §18.3): starter-only landing-zone comment, no derivation source",
    ("3", "ramp", "// (nothing to set up - press B to run, so put the robot down first)"):
        "L03 ramp whole-template starter (S44, §18.3; line rewritten S137 when the starter "
        "was gated on button B): starter-only comment, no derivation source",
    ("3", "ramp", "// Then STOP: motors.setSpeeds(0, 0);  <-- never leave the motors running."):
        "L03 ramp whole-template starter (§18.3; ADDED S137 - the ramp starter never told the "
        "student to stop the motors, in a lesson whose §3.8 warning is the robot drives off the "
        "table): starter-only landing-zone comment, no derivation source",
    ("3", "ramp", "// (none needed for this challenge)"):
        "L03 ramp whole-template starter (S44, §18.3): starter-only comment, no derivation source",
    ("3", "ramp", "// write your code here"):
        "L03 ramp whole-template starter (S44, §18.3): starter-only comment, no derivation source",
    ("3", "constrain", "// 2. delay(RUN_MS)"):
        "L03 constrain whole-template starter (S44, §18.3): starter-only hint, no derivation source",
    ("3", "constrain", "// 3. motors.setSpeeds(0, 0);  // stop before the edge"):
        "L03 constrain whole-template starter (S44, §18.3): starter-only hint, no derivation source",
    ("3", "ramp", "// climb 50 -> 100 -> 150 -> 200. Each line is one rung."):
        "L03 ramp whole-template starter (S44, §18.3): starter-only landing-zone comment, no derivation source",
    ("3", "ramp", "//   motors.setSpeeds(50, 50);   delay(STEP_MS);"):
        "L03 ramp whole-template starter (S44, §18.3): starter-only landing-zone example, no derivation source",
    ("3", "ramp", "//   ... keep climbing ..."):
        "L03 ramp whole-template starter (S44, §18.3): starter-only landing-zone comment, no derivation source",
    ("3", "ramp", "// When you reach MAX_SPEED, you are done - do NOT go past the cap."):
        "L03 ramp whole-template starter (S44, §18.3): starter-only landing-zone comment, no derivation source",
    ("3", "ramp", "// (Lesson 4 takes the for loop apart; it does this climb in three lines.)"):
        "L03 ramp whole-template starter (S44, §18.3; repointed S137 from Lesson 5 to Lesson 4 - "
        "S57 gave the for tutorial to L04 §8A.6): starter-only forward-reference, no derivation source",
}

def decode_pres(txt):
    out = []
    for m in re.finditer(r'<pre[^>]*>(.*?)</pre>', txt, re.S):
        out.append(H.unescape(re.sub(r'<span[^>]*>', '', m.group(1)).replace('</span>', '')))
    return out

def brace_json(txt, anchor):
    i = txt.index(anchor)
    j = txt.index('{', i); depth = 0; k = j; ins = False; esc = False
    while True:
        c = txt[k]
        if ins:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': ins = False
        else:
            if c == '"': ins = True
            elif c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0: break
        k += 1
    return json.loads(txt[j:k+1]), txt[j:k+1]

def maker_templates(js):
    """Extract Maker-owned template strings: every JS string literal inside mainCpp()
    and the MY PLAN/head builders, decoded. These are canonical glue."""
    i = js.index('function mainCpp')
    j = js.index('\n  }', i)
    seg = js[i:j]
    tpl = []
    for m in re.finditer(r'"((?:[^"\\]|\\.)*)"', seg):
        s = m.group(1)
        s = s.encode().decode('unicode_escape')
        tpl.append(s)
    return "".join(tpl) + "\n\n" + "\n".join(tpl)


# --- v1.6 BOXED-HEADER FINGERPRINTS -------------------------------------------
# Boxed instruction headers are ADVISORY for book-matching (v1.5) but PINNED here, so
# an edit to a challenge file's instructions cannot pass silently. lesson -> key ->
# [line_count, md5]. Regenerate deliberately with --update-fp after an intended change.
BOXED_FP = {
    "1": {
        "c01": [101, "18235f95f23222444948eb03bac1105a"],
        "c02": [33, "08ca58452dffb720dc61f39f47588c22"],
        "c03": [30, "55a68a42210fda651876a117a0714372"],
        "c04": [36, "0a11103c26a3194fbc3b551a41cc7107"],
        "c05": [34, "fb80eeb4ef1218ad5b73f81307df7ccb"],
        "c06": [42, "afd96d945f3ee1ed69ee2086f4c82ed8"],
        "c07": [72, "8cc29c06520d2c3014a40216a0d7335a"],
        "c08": [76, "9552ea0166fdcf891238ea9811418188"],
        "c09": [48, "fdff4a941ccde2251078b9a28d0d1dfe"],
        "c10": [60, "5526d7ddde7a0245e4cce25d5ff424d6"],
        "c11": [103, "a3f567f251f20d0d9acddf2d7088ba4b"],
    },
}

# v1.9.0 (S176) THE GATE WAS ONE-DIRECTIONAL AND A DELETION PASSED SILENTLY.
# The derivation test asks "does every payload line come from the lesson?" — a SUBSET
# test. A payload that has LOST a line is still a subset, so loss is structurally
# invisible. MEASURED, NOT THEORISED: deleting the S172 kill-switch guard
# `if (turnDegreesGyro(90.0 * sweepDir) == STOP_KILL) break;` from
# 13/challenge_9_1_keep_sweeping, leaving Lesson_13.html untouched, left this gate
# printing PASS with the advisory count unmoved at 635. Not one number changed.
# The symmetric predicate — every lesson line must appear in some payload — is WRONG
# and was rejected: lessons legitimately print code no payload carries (wrong-code
# examples, "before" versions, the Serial-cut demos). So the truth is PINNED, exactly
# as BOXED_FP pins what derivation cannot see (v1.6's reasoning, one layer along).
# lesson -> key -> [executable_line_count, md5]. Count AND hash, because a count alone
# lets a loss in one file cancel against a gain in a sibling file of the same payload
# (rule 79's own shape). Lines are STRIPPED and blank/whole-line-comment/<<< lines
# excluded, so reindentation is SILENT.
# WHAT FIRES, corrected BY A CONTROL rather than predicted: any change to a stripped
# executable line — deletion, addition, REORDERING, a changed value, and a reworded
# TRAILING comment, which is part of the line and not excluded by the comment rule.
# The prediction written from a count-only probe said a comment reword would be silent;
# control 4 said otherwise, and the control was right.
# That breadth costs nothing, because of the five, only DELETION and REORDERING pass
# derivation. The other three already fail it and already require a paired lesson edit,
# so the census adds NO new obligation except on the two events it exists to catch.
# Regenerate deliberately with --update-census.
PAYLOAD_CENSUS = {
    "1": {
        "c01": [52, "d1f8074c7a53b044a496bb1728c405f8"],
        "c02": [54, "950b4c5a40e00b6edbf14dc2876ba445"],
        "c03": [52, "ac714fe66f7c81878291e9eea2353c1f"],
        "c04": [54, "6260a4694076e1b5801498d82fb1c27b"],
        "c05": [55, "0a6aaec72e9a3b8f90b65708a3488075"],
        "c06": [55, "0a6aaec72e9a3b8f90b65708a3488075"],
        "c07": [55, "0a6aaec72e9a3b8f90b65708a3488075"],
        "c08": [54, "c14916a98950922e9ca058761ed24f63"],
        "c09": [55, "0a6aaec72e9a3b8f90b65708a3488075"],
        "c10": [55, "0a6aaec72e9a3b8f90b65708a3488075"],
        "c11": [55, "0a6aaec72e9a3b8f90b65708a3488075"],
    },
    "2": {
        "backwards_led": [10, "f93b4f5c5dc0e324f73f1c4852b33afe"],
        "blink_count": [11, "11d1bb960c381988ae5120f605b804c3"],
        "broken_code": [11, "a8d524a52de2899e3cecbeaf67f7fdc2"],
        "buzzer_pitch": [9, "e599a6791da0adf7922d49d01ff3852c"],
        "discovery_2_2": [7, "642ce2d256ac67a7fc1e8ba36f6cca2f"],
        "discovery_2_3": [9, "30f964fb3dd512f5ece4c371cbad2d8a"],
        "discovery_2_4": [17, "91692bc7c34d3d6372982cc0f66ad9b5"],
        "discovery_2_5": [20, "2441ce8f11e9874738cb3f8eeb6f60ab"],
        "discovery_2_6": [27, "cb9a1a2839e57e68e89fac794563e1b2"],
        "discovery_2_7": [31, "043f0b838c59a81fc1f1eac49d6b1dcf"],
        "discovery_2_8": [45, "ff3eea0d619e3c5b89b866ebc697b4b4"],
        "discovery_2_9": [60, "b08a29d3d8c373184cdcf0815bac9e61"],
        "endless_beep": [7, "eff3d493ccc9e810d89d5c73b4f4795b"],
        "finished": [75, "bae7c9a3eaf1868522b23d722b5c9855"],
        "line_order": [11, "d9dac087acbb72a99e754fd34d7a5aa0"],
        "speed_limit": [11, "ba2020aaba96c349dc7337e31de236a8"],
    },
    "3": {
        "backwards_robot": [14, "b0dee65e46f11ec3eedd8655e43b5e5a"],
        "braking_test": [20, "cf232e7b8e2bc7ec832c3c1e8fa1bf1f"],
        "constrain": [12, "4713166f7d702e70f9a1087adf84213c"],
        "creep_mode": [25, "7480ad4d1c4e775f5fe0e26d0bd374a2"],
        "discovery_3_2": [9, "e28349c4a042fb5d1109c8b051b2c421"],
        "discovery_3_3": [12, "46e2f4e650aea20b31e64ccfc621e37e"],
        "discovery_3_4": [15, "306d5a41cc8143e229f7389f4831d29f"],
        "discovery_3_5": [37, "e30fee48b87e29ffe26795c55f356187"],
        "discovery_3_6": [82, "8c2b34ae50016427db74f53bf75744db"],
        "discovery_3_7": [120, "9d3b9c70de20a235d444daea8800bf71"],
        "discovery_3_8": [122, "14a8f78b2e1f8a199c7fc51816038aa6"],
        "figure_eight": [13, "5b95d114e69df4829dfa130c0b7fb033"],
        "finished": [160, "9ad25b99f1c2884c75b0d42536835244"],
        "ramp": [10, "34305beb163740e986a76d8b56384830"],
        "speedometer": [14, "cb401300390de73d259d129cf00c760f"],
    },
    "4": {
        "act_one": [77, "e5054848499d6ca9a26d8ff76def1225"],
        "act_two": [78, "977f80df98308867ef8ea89f4a452007"],
        "after_step_2": [39, "10a9ff8a40ce70822b98aaae2d066f63"],
        "after_step_3": [41, "4c758c1adf5be93e5069cb86e931c9ba"],
        "after_step_4": [48, "a2bd4fcd6ebcaaf4fe8125c4843b1cc7"],
    },
    "5": {
        "finished": [247, "d5a59f992f6c71405656357f45ca162c"],
        "jumper_check": [30, "cceded037590e5a9a4b8d12f7db7f24d"],
        "step_3": [46, "29160cfa0ae08e3b196cb25825fb2e43"],
        "step_4": [67, "90eb8e07dbaac5a398d911f81969d31d"],
        "step_5": [94, "2e20e07ab25fbeed1e772dc3aa76b365"],
        "step_6": [109, "f246274e83e17d172afb18dd072d8e80"],
    },
    "6": {
        "after_step_10": [103, "8ecb4a8ab1ca3cfaad6e9c817555c69a"],
        "after_step_11": [108, "e74454d02e41c626d86e09a9c0ab0903"],
        "after_step_2": [36, "90491afa9b7b540d4b6eadbd6d65b1e3"],
        "after_step_3": [51, "479f01cda4bd8fa349b103e136495033"],
        "after_step_4": [54, "a5ccba4b17972f5c49ce9bfcc8b19e1d"],
        "after_step_5": [58, "5c53c2bae83e3d44188b26f4ec285ea6"],
        "after_step_6": [62, "129a4d0ddcaf3522b17db327048806e0"],
        "after_step_7": [74, "3a111ac8b53d4d506ccb1d86d793c67b"],
        "after_step_8": [87, "c7af09c7b7acb9d1234e99c57d74ffea"],
        "after_step_9": [91, "8188f51f422e5fc9577ab83535c3ed75"],
        "finished": [131, "80087a32c3e2e0bdf6627b3b1f8c6ad2"],
    },
    "7": {
        "after_step_1": [131, "80087a32c3e2e0bdf6627b3b1f8c6ad2"],
        "after_step_2": [49, "6de613a8be294238a38feb1dd23aaf72"],
        "after_step_3": [59, "3e0576ff418d79b85b29d07bc1489472"],
        "after_step_4": [65, "8b0bda7ec7f104cadf11b407298174ed"],
        "after_step_5": [70, "4f70d6b38f200e61cfb49b4207a3c6fe"],
        "after_step_6": [74, "4dc1c27cf489dee9e3916f6620b72151"],
        "after_step_7": [106, "a5e03a8ca73e5e4c8902490dff534561"],
        "capstone": [135, "ad4b42202c41b070c2430ddc5a8cdfdb"],
        "finished": [212, "0eb558bc75a66ec2cdc844ffc609c9cc"],
    },
    "8": {
        "after_step_1": [212, "c2b2d3f0427f5ef54981a24a46dd9806"],
        "after_step_2": [218, "eb37bd563fa66ea6e287c85895d07b76"],
        "after_step_3": [223, "d8bb99fc82aa57ec66589c30330f3ab8"],
        "after_step_4": [241, "bcf55c34f00dd6c77dedfefd42fbcd1a"],
        "after_step_5": [253, "d5bdfee2af2ff08cdff283d61c85191e"],
        "after_step_6": [228, "675648e5d0b5a0b0bec3a0a3304bb9bf"],
        "after_step_7": [264, "efd83fcbf2a4386c7b55b60466ddc4bd"],
        "backwards_correction": [299, "3a8cc52074bdce50c21ed96c05139e00"],
        "blind_robot": [299, "b282ab107d60f066aab389b412310c70"],
        "eternal_gap": [299, "9433c56b94ab3089d9655651fc31e96f"],
        "finished": [299, "d78d98853007259ec4ee0b031b37a532"],
        "straight_liner": [299, "c24e18f7e5610013a84c5f225232511a"],
        "uncalibrated_run": [298, "163d2b2d6dcbd1d603d652cbf6bfd66a"],
    },
    "9": {
        "after_step_1": [299, "446a654f1ee751e191cf98d862d087fa"],
        "after_step_2": [313, "2e93cb574c9dfc514f313c4e5b856d0b"],
        "after_step_3": [316, "d00ac4242739d591bffe5dead86f6e92"],
        "after_step_4": [329, "0daac78deb1a9d8bbb0b71ececcc18d2"],
        "after_step_5": [335, "0c8523dcaefb5d2056730fa6d4b28a51"],
        "after_step_6": [336, "c405e59d44d15483d47576a3fcc4caff"],
        "after_step_7": [349, "5a25ee9361fcd40bf194264388a3e76a"],
        "blind_corners": [373, "5144ffed3cd79c5fe18824d066f3e765"],
        "finished": [373, "4fb062573769bbc461d4691ab1f4c607"],
        "mirror_dispatch": [373, "1c4a30b99cc3c7680067f59304fb09af"],
        "missing_break": [372, "ba6792ccaa03c6380cc674adcdb5adc9"],
        "one_turn_wonder": [372, "7d403bd854c5b1f805fdc5233d57a3a7"],
        "paranoid_green": [373, "4ab86dbaa11919af43f89725fed36eba"],
    },
    "10": {
        "after_step_1": [373, "4fb062573769bbc461d4691ab1f4c607"],
        "after_step_2": [392, "52836194ba80bc18574cd1c798e937a0"],
        "after_step_3": [396, "06fd6ec8acd586412fea328e68586c15"],
        "after_step_4": [408, "8fc8da0d6a3c3fc3491695fc435d3d4e"],
        "after_step_5": [413, "9082160dfd25aa7cc6201973cc51e448"],
        "after_step_6": [417, "4260de67089f0ee1c8771cae7bec70f4"],
        "after_step_6b": [429, "f4fbc5140a34e85179f9049f94197862"],
        "after_step_7": [448, "58010d386517ad397b1ff20323c65616"],
        "after_step_8": [503, "e0e1bba3124c92aa02a0cea0a04c2803"],
        "bonus_b1": [510, "de32f6de62a4ba31c65f3481d1da5f30"],
        "bonus_b2": [510, "152f889045a960186d8cebf5fc3dfc7d"],
        "bonus_b3": [511, "47fea2683505f0f4363dc9f4ceecf7c3"],
        "bonus_b4": [521, "6cf815955e62aa50dbcfa23d1559cb6e"],
        "bonus_b5": [511, "9e9e32f91efeade183f508adaf91c077"],
        "finished": [511, "199f2f9680f7303985beda6ca910bbcf"],
        "sq_a_turn": [240, "23e123d407d3f369b9fbff1eac6d4187"],
        "sq_b_distance": [240, "1e844a1e5a39e6e5d205d4b85bb0d149"],
        "sq_c_corner": [244, "965e183ff51f13f36ce70b01895462e8"],
        "sq_d_square": [251, "8a59d86eb315409d0273ab71ad5f0c6b"],
        "sq_e_encoder": [245, "6d52f926b3af9763f62d82671090488e"],
        "step_4_RED": [397, "7bf556f23e978d9fdad266502027f6fb"],
        "step_8_timed": [513, "329b550742e25a6eeb3a0240cb5aa933"],
    },
    "11": {
        "after_step_1": [511, "199f2f9680f7303985beda6ca910bbcf"],
        "after_step_2": [514, "27065c57858011c9c9c562f9115ef987"],
        "after_step_3": [515, "32421772d0a88e50d6d6f52743e3e701"],
        "after_step_4": [524, "2ab69fecf7fc2491bf1d1975c16f44e7"],
        "after_step_5": [519, "468bc1bf524b893f11e8e704dee4d884"],
        "b1_onewheel": [546, "4000b954da4b79c3f7741ff9f019c999"],
        "b2_norearm": [545, "08dda1c7c4290e62046a2ab01e337e27"],
        "b3_trim": [546, "5ba784162a9b3be8187fd2c42f5ea031"],
        "b4_counts": [546, "d2c2351e1dca9e7e5ec523638a77b8ec"],
        "c1_backup": [551, "3c5be8bed0f6894cf3a0590fe073efd8"],
        "c2_hunt": [555, "bb2cfff33116b44c61a3961f2edb824d"],
        "c3_speed": [549, "fb5abebf8b3b988078278615a8148fa7"],
        "cal_7a": [561, "8041e459f67d63718f13e9e4aeb2e1fd"],
        "cal_7b": [546, "75a6b5810b60325c3d48e1a3be0e214d"],
        "cal_7d": [550, "ae58dceabc50e1c0608b8b8a56843346"],
        "cal_7e": [547, "5c903cf139d5f06e8135df27dfaac15b"],
        "finished": [546, "2800ecc7cf4ef34dc80881e02d2f4294"],
    },
    "12": {
        "after_step_1": [546, "2800ecc7cf4ef34dc80881e02d2f4294"],
        "after_step_2": [548, "9f5b1a7df2ba0b58fe68d0040eb1e3e4"],
        "after_step_3": [549, "39d6cf72860855d0192b10a4d24201cd"],
        "after_step_4": [553, "5ebafcc6b1260ffe9eb0e8651b31215f"],
        "after_step_5": [586, "1a8153fe5d68c5b1df3b4a0e2dfc55ce"],
        "after_step_6": [587, "4aa9ec3872e01ac7176fa69dc45882ce"],
        "after_step_7": [599, "ebe5d570b816906d5822ab74281f5a06"],
        "after_step_8": [605, "2d59f12806561b10863acab3801ab70b"],
        "b1_spinning_cal": [607, "a018c315577bc97349560c0ddf3e3b91"],
        "b2_no_update": [604, "8a0eb8af46228c9619747ef0a2b98fa7"],
        "b3_reset_hoisted": [605, "b592eacd6b08ad75690afe38dbc16faf"],
        "b4_trim_in_turn": [605, "e55108c65f75449d67b19583c792d500"],
        "c1_heading": [454, "1bc5422581377eaa7585a302b74674ae"],
        "c2_slipalarm": [464, "8f0adfbf87aa4643318a1906db76323d"],
        "c3_stuckguard": [465, "5f715d59ad05560eb693939c0874166d"],
        "cal_7a": [443, "76c9fecb88786e49df2ea6cfe22bb729"],
        "cal_7b": [447, "bc165a24e755cd186cfc68f4758bdb25"],
        "cal_7c": [450, "010db47fbca1ba02c7bbf033ac708202"],
        "cal_7d": [447, "07fee0712ba03cbbd5c440efd94b91fe"],
        "cal_7e": [456, "76716829218d2b2e447e9b363d1c3a2a"],
        "finished": [605, "2d59f12806561b10863acab3801ab70b"],
    },
    "13": {
        "after_step_1": [614, "b8269577bb03778c739becfb627540a2"],
        "after_step_2": [625, "723805594e1165d128c057512ab51184"],
        "after_step_3": [644, "b3c00e031f720644b6ad70a2ba9ecaa9"],
        "after_step_4": [668, "026f5cbc205778a78b54b6a2645bd7cb"],
        "after_step_5": [689, "9e8f2ecb21ec91aeecc852b6fe9dde85"],
        "after_step_6": [717, "19bc06612cbc6a92002216485f1e2456"],
        "bonus_b1_spun_zero": [736, "c5a33958d7d4ec08fd41ad7d17309255"],
        "bonus_b2_unspent_trim": [736, "f657e29acd84e8ceedd971f8ed2540f7"],
        "bonus_b3_blind_stripes": [736, "7cd60afeb68c37e3fb84fa5979cd0e03"],
        "bonus_b4_invisible_door": [736, "1e7485872785c38ea3beea274c8b416b"],
        "challenge_9_1_keep_sweeping": [741, "f7c4f01cad0819025f3501e1d3bfecad"],
        "challenge_9_2_sweep_report": [753, "f40050c354e51fddb6a9241df2976bd7"],
        "challenge_9_3_row_zero": [745, "dc61984367bd3ded4ac54fa4e69a0c0b"],
        "finished": [736, "ecb1e058ad5fa21808cb43c9e091764c"],
        "ladder_7a_surface_meter": [353, "734d836929d14903d3c7883d8b814b93"],
        "ladder_7b_silver_brake": [644, "b3c00e031f720644b6ad70a2ba9ecaa9"],
        "ladder_7c_leg_and_turn": [366, "ed864e34f70c9f0c17d37585f5271c8f"],
        "ladder_7d_full_sweep": [736, "ecb1e058ad5fa21808cb43c9e091764c"],
        "ladder_7e_encoder_turns": [736, "0f8cc5380edbca79a648589deee010f8"],
    },
    "14": {
        "after_step_1": [742, "821e307cb672453336dfccda1a9d7018"],
        "after_step_2": [812, "98a2c337130ac3681a45dc718fe19686"],
        "after_step_3": [813, "a5af66b9e31052001c753acef514f328"],
        "bonus_b1_always_passes": [814, "57800e753641a22c48a1423ae4875ee9"],
        "bonus_b2_loose_gyro": [813, "0eaf04a13426f2b14091e14da4c2bf7b"],
        "bonus_b3_dropped_zero": [813, "df254836ca1f0006d27e69b9cf9db2ef"],
        "bonus_b4_guarded_kill": [813, "f66a43f9bab47f88247f68e3a5a694bf"],
        "challenge_9_1_wheel_test": [828, "b0b7910dad1ca61db6a998f2b5283c42"],
        "challenge_9_2_strict_mode": [813, "0032b897a84a1eb733a4c2910307a013"],
        "challenge_9_3_lop_counter": [828, "01f6f9d5501763bfddfe08ccc3ff7fe4"],
        "finished": [813, "d01611c77164759c8ab292d7da657864"],
        "ladder_7c_match_mode": [813, "b1d28648f569a7125847d895fcb460f3"],
    },
    "15": {
        "after_step_1": [813, "d01611c77164759c8ab292d7da657864"],
        "after_step_2": [820, "4022c0718d33560524d64fadc798f8b4"],
        "after_step_3": [831, "82a858e24d746e2a3b8cefca57ef1ae3"],
        "after_step_4": [835, "f54abdcad5f4f19178de0f6028eed8cc"],
        "after_step_5": [905, "110cec7ba9f17584b9ce3a2d0398d7c4"],
        "after_step_6": [909, "9f7daf2f69464374fc815d2ccd54f2b3"],
        "bonus_b1_millis_dt": [940, "ac297677ce5649d0b95fc2a41b9026cc"],
        "bonus_b2_stale_lasterror": [939, "ca1f0bff1fb558f1c6af2cbcd0d638b5"],
        "bonus_b3_no_doorway": [939, "0a6f26bac81db4052c503b96a2bca929"],
        "bonus_b4_kd_sign": [940, "bb9257c6c3eb16bc40ca74ba95b48c70"],
        "challenge_9_1_gain_scheduling": [943, "bf442ddc71ebcae2cb649f36297ee330"],
        "challenge_9_2_d_filter": [944, "571c4bb70b88601c306e72f79e3bf7f7"],
        "challenge_9_3_worst_dt": [944, "6eed0865a82306f582f8cbae4838062c"],
        "finished": [940, "490fdf26b8778865d674282f825ed6d6"],
        "ladder_7a_stripchart": [845, "e04576aae2067556ca15e85454cb1283"],
        "ladder_7d_i_on_line": [914, "40b55b7c128fd62d7c37c703b0573635"],
    },
    "16": {
        "after_step_1": [940, "490fdf26b8778865d674282f825ed6d6"],
        "after_step_2": [962, "cbe00cada8616dccf3edb56dca469b3c"],
        "after_step_3": [987, "0f976beffa5d1644ac6b11f79bd48ddf"],
        "after_step_4": [1032, "4387dc4cf50d883af6ad6c7eb553aec1"],
        "after_step_5": [1005, "1b4d92e125a83351b8626408732b71eb"],
        "bonus_b1_bell_mode": [1011, "d3705bb0aaeeaecdb3d51c279b0d7a24"],
        "bonus_b2_wrong_magic": [1011, "6ad68255800f293044c08df07bb3a749"],
        "finished": [1011, "3567519dd558781fa535c76035a51c5c"],
        "step_5_serial_traded": [1017, "a6cdb4af48078475ab4f95c8bc3a6f3d"],
        "step_5_zn_traded": [1011, "4644b4ae2b10b9dfda385dbf04a51b70"],
    },
}

ADVISORY = []
OBSERVED_FP = {}
OBSERVED_CENSUS = {}

def _exec_lines(text):
    """Executable lines: stripped, blanks/comment-only/landing-zone markers removed.

    Block comments are tracked, so the /* ... */ file headers every payload carries
    do not read as code. This predicate is written HERE rather than reused from
    _summarize's census, because that one only ever sees lines that already FAILED
    derivation and its blindness to block comments never bites there — three methods
    sharing a predicate are one method (rules 83/84), and this arm must be able to
    disagree with the other.
    """
    out, blk = [], False
    for raw in text.split("\n"):
        s = raw.strip()
        if blk:
            if "*/" in s:
                blk = False
            continue
        if s.startswith("/*"):
            if "*/" not in s:
                blk = True
            continue
        if not s or s.startswith("//") or "<<<" in s:
            continue
        out.append(s)
    return out

def check_payload_census(payloads, fails, observed):
    """v1.9.0: pin every payload's executable content so a DELETION cannot pass.

    Runs over the WHOLE registry, not the lessons that happened to be passed in —
    a census that covers a subset and reports PASS is not a census.
    """
    import hashlib
    seen = set()
    for L in sorted(payloads, key=int):
        for key in sorted(payloads[L]):
            pay = payloads[L][key]
            if not pay:
                continue
            text = "\n".join(pay.values()) if isinstance(pay, dict) else pay
            ex = _exec_lines(text)
            h = hashlib.md5("\n".join(ex).encode("utf-8")).hexdigest()
            observed.setdefault(L, {})[key] = [len(ex), h]
            seen.add((L, key))
            want = PAYLOAD_CENSUS.get(L, {}).get(key)
            if want is None:
                fails.append(f"CENSUS L{L}/{key}: payload NOT PINNED in PAYLOAD_CENSUS "
                             f"(add [{len(ex)}, {h!r}] or run --update-census)")
            elif want[0] != len(ex) or want[1] != h:
                verb = ("SHRANK" if len(ex) < want[0] else
                        "GREW" if len(ex) > want[0] else "CHANGED")
                fails.append(f"CENSUS L{L}/{key}: EXECUTABLE CONTENT {verb} — pinned "
                             f"{want[0]} lines/{want[1][:12]}, found {len(ex)} lines/"
                             f"{h[:12]}. Intentional? run --update-census.")
    # An orphan pin is the S138 defect: a key that pins something no longer there
    # certifies nothing and hides that the payload is gone.
    for L in PAYLOAD_CENSUS:
        for key in PAYLOAD_CENSUS[L]:
            if (L, key) not in seen:
                fails.append(f"CENSUS L{L}/{key}: PINNED but no such payload in the "
                             f"Maker — orphan pin, remove it or restore the payload")
    # A gate whose truth table is empty must not pass on no truth.
    if not PAYLOAD_CENSUS:
        fails.append("CENSUS: PAYLOAD_CENSUS is EMPTY — the arm has no truth to assert "
                     "against and would pass on anything. Run --update-census.")

def _is_boxed(line):
    """A boxed instruction-header line: // ┌ ─ ┐ / // │ / // ├ / // └ (Bible §11, S56)."""
    return line.strip().startswith(("// \u2502", "// \u250c", "// \u251c", "// \u2514"))

def _boxed_lines(text):
    return [l for l in text.split("\n") if _is_boxed(l)]

def check_boxed_fp(L, key, text, fails, observed):
    """v1.6: boxed instruction headers are advisory for book-matching but PINNED.
    Any edit to a challenge file's in-file instructions must be deliberate."""
    import hashlib
    b = _boxed_lines(text)
    if not b:
        return
    h = hashlib.md5("\n".join(b).encode("utf-8")).hexdigest()
    observed.setdefault(L, {})[key] = [len(b), h]
    want = BOXED_FP.get(L, {}).get(key)
    if want is None:
        fails.append(f"L{L}/{key}: boxed header present but NOT PINNED in BOXED_FP "
                     f"(add [{len(b)}, {h!r}] or run --update-fp)")
    elif want[1] != h:
        fails.append(f"L{L}/{key}: BOXED HEADER CHANGED — pinned {want[0]} lines/{want[1][:12]}, "
                     f"found {len(b)} lines/{h[:12]}. Intentional? run --update-fp.")

def _corpus_lines(corpus, _cache={}):
    """Stripped line SET of the corpus, memoised per corpus object.

    S142: THE LINE TEST WAS A SUBSTRING TEST AND IT WAS BLIND ON ONE SIDE.
    `l in corpus` asks whether the payload line appears ANYWHERE in the corpus text,
    including as part of a LONGER line. So a payload that has LOST a leading keyword
    the lesson carries matches trivially:

        corpus line : static unsigned int sensorValues[5];     // Array to store ...
        payload line:        unsigned int sensorValues[5];     // Array to store ...

    The second is a substring of the first, so the gate stayed SILENT. Measured, not
    theorised: the S142 `static` pass reverted exactly one of 136 payloads and the gate
    still printed PASS. Additions it could always see; a dropped `static`, `const`,
    `unsigned` or any other leading qualifier it could not see at all — and a payload
    silently losing a qualifier is precisely the class §15.6 was written for.

    Line EQUALITY against a stripped set is the property the check always meant to
    assert. Both sides are stripped, so indentation still does not matter and every
    payload that passed on real line-for-line derivation still passes.
    """
    key = id(corpus)
    hit = _cache.get(key)
    if hit is None or hit[0] is not corpus:
        hit = (corpus, {l.strip() for l in corpus.split('\n') if l.strip()})
        _cache[key] = hit
    return hit[1]

def check_payload_text(name, text, corpus, fails):
    clines = _corpus_lines(corpus)
    chunks = [c for c in re.split(r'\n\s*\n', text) if len(c.strip()) >= MIN_CHARS]
    for c in chunks:
        if c.strip() in corpus:
            continue
        # line-wise fallback: every non-empty line appears verbatim in a canonical
        # source (handles payload glue assembled from lesson-verbatim lines).
        # EQUALITY, not containment — see _corpus_lines.
        lines = [l.strip() for l in c.split('\n') if l.strip()]
        if lines and all(l in clines for l in lines):
            continue
        missing = [l for l in lines if l not in clines] or [c.strip()[:60]]
        parts = name.split("/")
        Lk = (parts[0][1:], parts[1])
        missing = [l for l in missing if (Lk[0], Lk[1], l) not in EXEMPT]
        if not missing:
            continue
        for _m in missing:
            _entry = f"{name}: unmatched: {_m[:70]!r}"
            (ADVISORY if _is_boxed(_m) else fails).append(_entry)

def _summarize(fails):
    """Category census. A raw FAIL count is easy to misread: 627 boxed-comment
    lines and 146 lines of real code are NOT the same defect, and a truncated
    display makes an all-comment failure look like the whole story (S55 — three
    sessions read FAIL(148) off a capped list and proposed the wrong fix)."""
    import collections
    hdr = mark = com = code = 0
    codelines = []
    for f in fails:
        if ": unmatched: " not in f:
            continue
        t = f.split(": unmatched: ", 1)[1].strip().strip("'\"")
        st = t.strip()
        if st.startswith(("// \u2502", "// \u250c", "// \u251c", "// \u2514")):
            hdr += 1
        elif "<<<" in st:
            mark += 1
        elif st.startswith("//"):
            com += 1
        else:
            code += 1
            codelines.append(st)
    print("\n  CATEGORY CENSUS")
    print(f"    boxed-comment (header art) : {hdr}")
    print(f"    landing-zone markers <<<   : {mark}")
    print(f"    other comments             : {com}")
    print(f"    EXECUTABLE CODE            : {code}")
    if codelines:
        print("    -- distinct code lines --")
        for c in sorted(set(codelines))[:40]:
            print("      ", c[:90])
        if len(set(codelines)) > 40:
            print(f"       ... {len(set(codelines))-40} more distinct")

def main():
    _flags = ("--update-fp", "--update-census")
    args = [a for a in sys.argv[1:] if a not in _flags]
    update_fp = "--update-fp" in sys.argv
    update_census = "--update-census" in sys.argv
    maker_path, lesson_paths = args[0], args[1:]
    mk = open(maker_path, encoding='utf-8').read()
    js = re.search(r'<script>(.*)</script>', mk, re.S).group(1)
    fails, notes = [], []
    import glob as _glob
    _present = len(_glob.glob(os.path.join('lessons', 'Lesson_*.html')))
    if _present and len(lesson_paths) < _present:
        fails.append('COVERAGE: %d lesson file(s) in lessons/ but only %d passed in - a gate '
                     'that checks a subset and reports PASS is not a gate'
                     % (_present, len(lesson_paths)))

    open('/tmp/_gate.js', 'w').write(js)
    r = subprocess.run(['node', '--check', '/tmp/_gate.js'], capture_output=True, text=True)
    if r.returncode: fails.append("JS SYNTAX: " + r.stderr.strip()[:120])

    payloads, _ = brace_json(js, 'var PAYLOADS = ')
    tpl_corpus = maker_templates(js)

    # v1.9.0: the census reads the WHOLE registry, before and independent of the
    # per-lesson derivation loop, which only visits lessons that were passed in.
    check_payload_census(payloads, fails, OBSERVED_CENSUS)

    kinds = {}
    for m in re.finditer(r'(\d+): \[(.*?)\n    \]', js, re.S):
        L = m.group(1)
        kinds[L] = re.findall(r'\[\s*"([a-z_0-9]+)"(?:[^\]]*?)"(after_step_\d+|finished|capstone|[a-z_0-9]+)"\s*\]', m.group(2))
    # registry key resolution
    for m in re.finditer(r'"(after_step_\d+|finished|capstone)"\]', js):
        pass  # per-lesson resolution below

    lessons = {}
    # S110: this required a `Lesson_NN_Topic_` name and the book stabilised on
    # `Lesson_NN.html`, so the gate CRASHED on the first file instead of failing and was
    # simply never run again. A matcher written against a shape nothing produces is the
    # same defect as pill_sweep's `width: 4px` and gen_part_banners' inline block - four
    # instruments in one session. Both spellings are accepted; a name that is neither is
    # NAMED, never skipped, because a skipped input is a gate that silently stops gating.
    for p in lesson_paths:
        mm = re.search(r'Lesson_0?(\d+)(?:_|\.html$)', os.path.basename(p))
        if not mm:
            fails.append('UNPARSEABLE LESSON FILENAME: %s' % os.path.basename(p))
            continue
        n = mm.group(1)
        lessons[n] = p

    for L, path in sorted(lessons.items(), key=lambda x: int(x[0])):
        P = payloads.get(L)
        if not P:
            notes.append(f"L{L:>02}: no payloads registered — SKIP")
            continue
        pres = decode_pres(open(path, encoding='utf-8').read())
        corpus = "\n\n".join(pres) + "\n\n" + tpl_corpus
        # v1.1 inheritance: prior lesson's finished payload is canonical for lesson N
        prev = payloads.get(str(int(L) - 1), {}).get('finished', {})
        if isinstance(prev, dict) and prev:
            corpus += "\n\n" + "\n\n".join(prev.values())
        elif isinstance(prev, str) and prev:
            corpus += "\n\n" + prev
        # also normalize: strip trailing ws per line in corpus? byte-match canon: no.
        n_files = 0
        for key, pay in P.items():
            if isinstance(pay, dict):
                for fn, content in pay.items():
                    n_files += 1
                    check_payload_text(f"L{L}/{key}/{fn}", content, corpus, fails)
                check_boxed_fp(L, key, "\n".join(pay.values()), fails, OBSERVED_FP)
            else:
                n_files += 1
                check_payload_text(f"L{L}/{key}", pay, corpus, fails)
                check_boxed_fp(L, key, pay, fails, OBSERVED_FP)
        notes.append(f"L{L:>02}: {len(P)} payload keys, {n_files} bodies/files checked")

    # registry keys resolve per lesson
    for m in re.finditer(r'(\d+): \[(.*?)\n    \],', js, re.S):
        L, block = m.group(1), m.group(2)
        for key in re.findall(r',\s*"([a-z_0-9]+)"\]', block):
            if key in ('null',): continue
            if payloads.get(L) is not None and key not in payloads[L] and key not in ('custom',):
                fails.append(f"registry L{L}: payload key {key!r} unresolved")

    print("\n".join(notes))
    print()
    if update_fp:
        print("  BOXED_FP = {")
        for L in sorted(OBSERVED_FP, key=int):
            print(f'      "{L}": {{')
            for k in sorted(OBSERVED_FP[L]):
                n, h = OBSERVED_FP[L][k]
                print(f'          "{k}": [{n}, "{h}"],')
            print("      },")
        print("  }")
        print("  ^ paste into BOXED_FP. Only do this for an INTENDED header change.\n")
    if update_census:
        print("PAYLOAD_CENSUS = {")
        for L in sorted(OBSERVED_CENSUS, key=int):
            print(f'    "{L}": {{')
            for k in sorted(OBSERVED_CENSUS[L]):
                n, h = OBSERVED_CENSUS[L][k]
                print(f'        "{k}": [{n}, "{h}"],')
            print("    },")
        print("}")
        print("  ^ paste into PAYLOAD_CENSUS. Only for an INTENDED payload change.\n")
    if ADVISORY:
        print(f"  ADVISORY ({len(ADVISORY)}) — boxed instruction-header lines, not failures.")
        print("  These are the challenge files' in-file working instructions (Bible §11, S56).")
        print("  The book's cards carry the same content as prose; format differs by design.")
        _byl = {}
        for a in ADVISORY:
            k = a.split(":")[0].split("/")[0]
            _byl[k] = _byl.get(k, 0) + 1
        print("   ", "  ".join(f"{k}={v}" for k, v in sorted(_byl.items())))
        print()
    if fails:
        print(f"GATE: FAIL ({len(fails)})")
        _cap = 200
        [print("  -", f) for f in fails[:_cap]]
        if len(fails) > _cap:
            print(f"  ... {len(fails)-_cap} more (showing first {_cap})")
        _summarize(fails)
        sys.exit(1)
    print("GATE: PASS — every payload byte-derives from lesson pres + Maker templates")

if __name__ == "__main__":
    main()

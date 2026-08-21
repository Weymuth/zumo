#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAYLOAD BYTE-MATCH GATE (Bible §11) — v1.9.1, S56 (S110: runs on stable filenames)
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
        "finished": [131, "814ddc42b5f26d48978bb43d5903b844"],
    },
    "7": {
        "after_step_1": [131, "814ddc42b5f26d48978bb43d5903b844"],
        "after_step_2": [49, "6de613a8be294238a38feb1dd23aaf72"],
        "after_step_3": [59, "3e0576ff418d79b85b29d07bc1489472"],
        "after_step_4": [65, "8b0bda7ec7f104cadf11b407298174ed"],
        "after_step_5": [70, "4f70d6b38f200e61cfb49b4207a3c6fe"],
        "after_step_6": [74, "4dc1c27cf489dee9e3916f6620b72151"],
        "after_step_7": [106, "4c78ebfd2a2dafadbdd5cc56d99add1c"],
        "capstone": [135, "d2ad84ca3efe384e5a1f88adcc0d58a6"],
        "finished": [212, "092bd3b4ec162f27fef0abc91868751d"],
    },
    "8": {
        "after_step_1": [212, "ce5d0cccf7bfe405b24279eb2f44dab5"],
        "after_step_2": [218, "8288da6c5ef9129cbea4e1f580059a76"],
        "after_step_3": [223, "17389b021042a0e46c5fcc1743f1df1e"],
        "after_step_4": [241, "68e40f0596188317f134a811f0811ffa"],
        "after_step_5": [253, "56edbe4d7290931325fdc91435216e58"],
        "after_step_6": [228, "c62a765ff8f9fdeb092ca9ab19a19f02"],
        "after_step_7": [264, "8c7a2d416a6bc6fa1b17a2d4ba8a86ba"],
        "backwards_correction": [299, "a92c1167a85495bb19b1ec44b8d2889d"],
        "blind_robot": [299, "13da429a8f7c6307350e649a627ab18d"],
        "eternal_gap": [299, "6fc672f19e09de2711232dc966110704"],
        "finished": [299, "566931c14b66eef60dd47c1c760c289f"],
        "straight_liner": [299, "fdadbd607af632ba0d2d7471a0320327"],
        "uncalibrated_run": [298, "e4987ebabed848c81e3ae0b3f28ffcc2"],
    },
    "9": {
        "after_step_1": [299, "082e6b77b9db807fd2db0f4b18a58155"],
        "after_step_2": [313, "fc339180c29acdedd4ba0d0156a69243"],
        "after_step_3": [316, "29713b1784c7f9c0a0b3576c7331e2e9"],
        "after_step_4": [329, "7def2939d944940bc38d8047e345fd6b"],
        "after_step_5": [335, "e9791d5f8bec28153c1547adab3274ca"],
        "after_step_6": [336, "c260cc60b6f63b9fc79130457cddcb50"],
        "after_step_7": [349, "a01553ead011b76d2ea3cb4554bb2940"],
        "blind_corners": [373, "9651ad95fd3b61029506780e0c117975"],
        "finished": [373, "07dd05aafeba7addc29f0d13d76df471"],
        "mirror_dispatch": [373, "219fdcb0e41ee349fa6a86613752fa87"],
        "missing_break": [372, "e8234f707536aa21b473c6748a5ac6cf"],
        "one_turn_wonder": [372, "28918daeaa0a255607e70526fb461be5"],
        "paranoid_green": [373, "cb2246dbd7e07f63f6a1d110d833ad56"],
    },
    "10": {
        "after_step_1": [373, "07dd05aafeba7addc29f0d13d76df471"],
        "after_step_2": [392, "43a65b83073b331d759b6af11aba7063"],
        "after_step_3": [396, "a3e463de74a6d5bb21cfd59cad2a8f39"],
        "after_step_4": [408, "b81d968f5d5aeebe49fa91aea6f55327"],
        "after_step_5": [413, "e362046928276ddee1a2d9281e7cb1e2"],
        "after_step_6": [417, "1610b14d3fb4085ad48ad296f6545602"],
        "after_step_6b": [429, "f1154ae130c559f7cfa1261fbd9422f7"],
        "after_step_7": [448, "df937f0f3e0fbe4439fe487193ab8015"],
        "after_step_8": [503, "eaf2250928597f72778b0e593e3e42f0"],
        "bonus_b1": [510, "ef6b95f11a9659da3ac158bb98e824c2"],
        "bonus_b2": [510, "309c79a80df067fea6934a649887fe69"],
        "bonus_b3": [511, "4e019413af1d83253119ccdb2426b960"],
        "bonus_b4": [521, "1de41e5d7113f362c59867905af93412"],
        "bonus_b5": [511, "b9b232828e0164533ae34aaa9eb2ccf8"],
        "finished": [511, "de0102caad9d59a97b13748aa9ef43d8"],
        "sq_a_turn": [240, "8a48176d5fc3793a706b07b42afdabff"],
        "sq_b_distance": [240, "ba4129ced8c632008bca9572b210a62c"],
        "sq_c_corner": [244, "250cde380d044befc447b2c96a631df6"],
        "sq_d_square": [251, "d406073ddeaec1756afe89f4351af3cf"],
        "sq_e_encoder": [245, "cb0059b1f1ff8c553753abec10bdcce2"],
        "step_4_RED": [397, "974ad6f04adc847b85e014df43d8d218"],
        "step_8_timed": [513, "b02246a429e0efa0e2b28e054c438cb3"],
    },
    "11": {
        "after_step_1": [511, "de0102caad9d59a97b13748aa9ef43d8"],
        "after_step_2": [514, "1b991018041d07cc8a8cd023469fce2a"],
        "after_step_3": [515, "5b23a485a6afe562292e6336ebb5a560"],
        "after_step_4": [524, "6145b331e0ba74ecf0c3032239b878ba"],
        "after_step_5": [519, "e80ac18e6457727b7554303a60cc1935"],
        "b1_onewheel": [546, "525d091d2b3e2ca8fc8ee9c220b798c0"],
        "b2_norearm": [545, "1189b5cc59cbe8bc606ee243955a29b2"],
        "b3_trim": [546, "600e98dc35338185f8423b5401084336"],
        "b4_counts": [546, "7c652c6d6cd9ddc41c90397d9d689672"],
        "c1_backup": [551, "e16bf6a43dc68f22d604aee42a5443df"],
        "c2_hunt": [555, "586e9415dd18062f5a25a093b642c841"],
        "c3_speed": [549, "cdcc02b2c9bf3b9659f3c10e3a02d201"],
        "cal_7a": [561, "313c3466d5f45212297eca833adb28de"],
        "cal_7b": [546, "346cc8ba62d5affd0eef829f93db8d0e"],
        "cal_7d": [550, "880e57ad29a9065d9cf15acfec1e15de"],
        "cal_7e": [547, "c543586fc4d53a923cb3b58ede0b7674"],
        "finished": [546, "3652a661050c8ea58e088e274f9ea285"],
    },
    "12": {
        "after_step_1": [546, "3652a661050c8ea58e088e274f9ea285"],
        "after_step_2": [548, "ab5960fc5cda2418029128a4d545446c"],
        "after_step_3": [549, "df033d0716e06839dce7067cbd5fda8d"],
        "after_step_4": [553, "7eeca4a3c5e10f18db90665da6ba1961"],
        "after_step_5": [586, "4873a4b6c0a7bd287f4f2103f77a43a1"],
        "after_step_6": [587, "8278a472ae88e4fc258860cf73692248"],
        "after_step_7": [599, "2fe5240e9e0cf09d8e40ac652bae8b6e"],
        "after_step_8": [605, "30bf890297fd4c1cf07839a758a1dbde"],
        "b1_spinning_cal": [607, "54b2f5a5fecd0dc93f6c8e28dfe7a3e4"],
        "b2_no_update": [604, "be43966f630dd9c6c7b8462ba9dceacd"],
        "b3_reset_hoisted": [605, "ca070a9066c19b38c0acf588258474bb"],
        "b4_trim_in_turn": [605, "a18948e7a99fd4ecb52d09e82cf729a8"],
        "c1_heading": [454, "652c984071e43c81f4e19b76ee9f97e9"],
        "c2_slipalarm": [464, "5bd70fd272bdab6372ca26f61a4b004d"],
        "c3_stuckguard": [465, "e106e169a1bf2117bd77425d68400ad7"],
        "c4_shortway": [460, "2c04d543d1709863148f624e8b94c168"],
        "c5_square": [473, "bb9592ca2c1732f1dda4af8f3c98f24b"],
        "c6_driftmeter": [447, "84a4ffbbdd53d526cc62e1ae924185a1"],
        "cal_7a": [443, "37c4b2c28cbbf80007a51361d121ab12"],
        "cal_7b": [447, "59b85dcadd93832f945d982b23d421ed"],
        "cal_7c": [450, "fb91ff0fc60de1b135d59a784d9a63d7"],
        "cal_7d": [447, "e1371540810503e84a4416c9e6f9491d"],
        "cal_7e": [456, "3a06e42f4265f9639c499d018bdd1601"],
        "finished": [605, "30bf890297fd4c1cf07839a758a1dbde"],
    },
    "13": {
        "after_step_1": [614, "6594569541329375ccdcd1baf609351f"],
        "after_step_2": [625, "59b5eb94ee58a679ea6bcdbdad632674"],
        "after_step_3": [644, "6888fa67be1d6df956a88cea614399b2"],
        "after_step_4": [668, "e3b63d6a1d31fbe440718f6c0c43f93e"],
        "after_step_5": [689, "0985a4c867e03e83f9546722d34b9505"],
        "after_step_6": [717, "5f4acce3bbbeeab065ecf9040f298338"],
        "bonus_b1_spun_zero": [736, "c8459917ecac6ae1d1969c3f74627322"],
        "bonus_b2_unspent_trim": [736, "d95535156d65317030326a2eb07e2b36"],
        "bonus_b3_blind_stripes": [736, "6d1f556fe4c52a1654ee1b9ada021be4"],
        "bonus_b4_invisible_door": [736, "4553d28f76f4be8de0cd6fd229bb79d7"],
        "c4_landmark": [738, "360a83ce30641815de0199e79f01c246"],
        "c5_striplog": [743, "dfbb212332c0650814ef983b64e93d86"],
        "challenge_9_1_keep_sweeping": [741, "a8258c2f17938455b56eb17e6aba144e"],
        "challenge_9_2_sweep_report": [753, "8b22638c1e00cb0c386a2a277478572f"],
        "challenge_9_3_row_zero": [745, "6bdf7ac642e413729d96312e461d53a0"],
        "finished": [736, "45b6cc7370abac10c04a905a4dd7f6e7"],
        "ladder_7a_surface_meter": [353, "99345c7d2b9fa0d29035e59c5636b0c4"],
        "ladder_7b_silver_brake": [644, "6888fa67be1d6df956a88cea614399b2"],
        "ladder_7c_leg_and_turn": [366, "a8228a97c1589cd2f8060e8fe62a9ba9"],
        "ladder_7d_full_sweep": [736, "45b6cc7370abac10c04a905a4dd7f6e7"],
        "ladder_7e_encoder_turns": [736, "0b32fae0710870c087c0615c7147b9d5"],
    },
    "14": {
        "after_step_1": [742, "fe4935a8fcef81d9c2e32b1b0a481bc5"],
        "after_step_2": [812, "36a81232f6f6e2349cbd537707921c98"],
        "after_step_3": [813, "2509aa378c37ccdd5becbaa57ca7b685"],
        "bonus_b1_always_passes": [814, "b5b32219431e5cdc450191a58caf35c6"],
        "bonus_b2_loose_gyro": [813, "16a7b6a2675ade802ed92b4b66124fb0"],
        "bonus_b3_dropped_zero": [813, "1c955b5c125a044ce5c10ee3cfe85c8e"],
        "bonus_b4_guarded_kill": [813, "aee3f7f3c65a71ce3e84d3e46ca795eb"],
        "challenge_9_1_wheel_test": [828, "523a0a12132d9d825bbd8bea2a2ef535"],
        "challenge_9_2_strict_mode": [813, "518235fa1414f1680225a8ed485bb21e"],
        "challenge_9_3_lop_counter": [828, "22726004f2ca0965c35bba232c46e9be"],
        "finished": [813, "cdae80243760a01163e2c2ebbd6e0301"],
        "ladder_7c_match_mode": [813, "1259277e2d30e36eecdd6dfc4536da34"],
    },
    "15": {
        "after_step_1": [813, "cdae80243760a01163e2c2ebbd6e0301"],
        "after_step_2": [820, "e5ca0802730169f5138dbaec194f7008"],
        "after_step_3": [831, "9b5d88137b7a09ffaa56eccebea85e83"],
        "after_step_4": [835, "ccb91744b3f8216298eba4594d6cd2a0"],
        "after_step_5": [905, "f47f0581583eafdff8fb0eb72198e1bd"],
        "after_step_6": [909, "955a45bffa94cfd60a0998440a37a6cd"],
        "bonus_b1_millis_dt": [940, "933f054f3315f9e646658d695b8ffa7e"],
        "bonus_b2_stale_lasterror": [939, "d125b352ff2443f325052cfcb7377ff6"],
        "bonus_b3_no_doorway": [939, "01c8464db255b84bb407e224bc100ee0"],
        "bonus_b4_kd_sign": [940, "741f81aaf8de7dbdeee439b766bd925e"],
        "challenge_9_1_gain_scheduling": [943, "c3832a3435eedceb1b65951fcb2a0b8e"],
        "challenge_9_2_d_filter": [944, "606c51e0b7a178b462b750f7e9ff52b0"],
        "challenge_9_3_worst_dt": [944, "6ab630143c6d957558190e3c8a352663"],
        "finished": [940, "a4bdfbcba7c6a8d44bf8f205e0f31a94"],
        "ladder_7a_stripchart": [845, "7892bb98fe8baf963b2acdafdf2b3913"],
        "ladder_7d_i_on_line": [914, "f3f37eb20d7d1d503871629d4ac7aba9"],
    },
    "16": {
        "after_step_1": [940, "a4bdfbcba7c6a8d44bf8f205e0f31a94"],
        "after_step_2": [962, "bcaeba8e889fafbece7c5d5208e71d95"],
        "after_step_3": [987, "cd823768bfb9cc7f74344147ee27cb76"],
        "after_step_4": [1032, "7cb14f1123b6519997cfcda65edbb2ab"],
        "after_step_5": [1005, "0c322dea290b6a49f245f7a547907c02"],
        "bonus_b1_bell_mode": [1011, "e517d38c90aa00375b3065fe1e823b74"],
        "bonus_b2_wrong_magic": [1011, "989fe8045e05512f293b8b1c79583445"],
        "finished": [1011, "a682ab37cff1d94a032f60b89b13aff1"],
        "step_5_serial_traded": [1017, "f20654e344e1a5e85f74eda9f27e7907"],
        "step_5_zn_traded": [1011, "b36f20bb039886790ba54389befbb163"],
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

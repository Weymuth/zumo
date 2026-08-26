#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAYLOAD BYTE-MATCH GATE (Bible §11) — v1.9.4, S56 (S110: runs on stable filenames)
v1.9.2 (S182): PAYLOAD_CENSUS re-pinned for the nine-section pass. 221 entries before AND
  after - a re-pin must not change the POPULATION, and that was asserted, not assumed. Every
  moved row is accounted for: L1/c01-c11 CHANGED at the same line count (eleven EEPROM includes
  hoisted out of CONSTANTS), L3 x8 and L6/finished GREW by their new prototypes, L4 x5 CHANGED
  at the same count (globals above prototypes). L6/finished and L7/after_step_1 show the SAME
  hash on both sides - the S51 byte-identity coupling holding, confirmed by the census rather
  than trusted.
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
        "c11": [103, "0c152aaa62c48f4b5d5f75b4acd58cce"],
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
        "c01": [52, "f00d73503529752562b06390806307c6"],
        "c02": [54, "d6d550048b197f847db778955783c495"],
        "c03": [52, "b06a7b176a3b7d924354a2c947c450d8"],
        "c04": [54, "58119c2030369e9e50abc3b6e4df691f"],
        "c05": [55, "8dfad90de74829665d67f523e28855d3"],
        "c06": [55, "8dfad90de74829665d67f523e28855d3"],
        "c07": [55, "8dfad90de74829665d67f523e28855d3"],
        "c08": [54, "645d32931f132c3a50e95968e3e61b38"],
        "c09": [55, "8dfad90de74829665d67f523e28855d3"],
        "c10": [55, "8dfad90de74829665d67f523e28855d3"],
        "c11": [55, "8dfad90de74829665d67f523e28855d3"],
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
        "backwards_robot": [15, "739e80aeb51e722cda8de0bb7f0783b0"],
        "braking_test": [20, "cf232e7b8e2bc7ec832c3c1e8fa1bf1f"],
        "constrain": [12, "4713166f7d702e70f9a1087adf84213c"],
        "creep_mode": [26, "18eef2062159216f6c839ab7acb65b51"],
        "discovery_3_2": [9, "e28349c4a042fb5d1109c8b051b2c421"],
        "discovery_3_3": [12, "46e2f4e650aea20b31e64ccfc621e37e"],
        "discovery_3_4": [15, "306d5a41cc8143e229f7389f4831d29f"],
        "discovery_3_5": [38, "76b001599a11f58cc767ccbe6d6c55a5"],
        "discovery_3_6": [86, "f3a7e246708b5e73ddd4a09c634bcbc1"],
        "discovery_3_7": [125, "c00a08863d63942f9df816fdcb22e25c"],
        "discovery_3_8": [127, "2be0b9c001087926af8e36e0ae9ba314"],
        "figure_eight": [13, "5b95d114e69df4829dfa130c0b7fb033"],
        "finished": [165, "85064b2f619d3e674bebb4462503258f"],
        "ramp": [10, "34305beb163740e986a76d8b56384830"],
        "speedometer": [15, "131a548475d0ed30cde8a887f799d400"],
    },
    "4": {
        "act_one": [77, "ef3d3cdcb63822505e44ce26f98bee2c"],
        "act_two": [78, "bb8e62fe3596aa3cd30786e96c11151f"],
        "after_step_2": [39, "bf7207f4c65ff68b026ed9dcd2de6d45"],
        "after_step_3": [41, "f8b93d2f03ed23d7fbb64c446b34fb66"],
        "after_step_4": [48, "9523537c1ff8fbd93dbb03fbf53020d9"],
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
        "after_step_10": [103, "8bb9b62e3dd2c0f93e9d897078dbdf1c"],
        "after_step_11": [108, "30a3081cf8358cc622941d3d179b49cc"],
        "after_step_2": [36, "90491afa9b7b540d4b6eadbd6d65b1e3"],
        "after_step_3": [51, "479f01cda4bd8fa349b103e136495033"],
        "after_step_4": [54, "a5ccba4b17972f5c49ce9bfcc8b19e1d"],
        "after_step_5": [58, "5c53c2bae83e3d44188b26f4ec285ea6"],
        "after_step_6": [62, "129a4d0ddcaf3522b17db327048806e0"],
        "after_step_7": [74, "3a111ac8b53d4d506ccb1d86d793c67b"],
        "after_step_8": [87, "c7af09c7b7acb9d1234e99c57d74ffea"],
        "after_step_9": [91, "e030ff197e496c1d541ed4203408156b"],
        "finished": [132, "7052f7d29e7df9ac7a40ac00f34f12ae"],
    },
    "7": {
        "after_step_1": [132, "7052f7d29e7df9ac7a40ac00f34f12ae"],
        "after_step_2": [49, "4cf3bc63721449cd515192fda1163f50"],
        "after_step_3": [59, "e8040664468617be6578dc69194ba687"],
        "after_step_4": [65, "d3d8a3161971b0cfdcd07c4fb61d861c"],
        "after_step_5": [70, "ef08f9bfc8b29e1c183a1e811a845ced"],
        "after_step_6": [74, "8752bd2656775529f33c4cf8c7a8a5bb"],
        "after_step_7": [106, "ca3b7358ed1fd7bfa9aa5a176067efd7"],
        "capstone": [135, "3b8c08f45ee104daa64b763caf45eb4e"],
        "finished": [212, "63e3042bad5381739dd28a370bf21778"],
    },
    "8": {
        "after_step_1": [212, "59a58788dc59cb17d8b5d501665cf69a"],
        "after_step_2": [218, "a0f673a325f3ac41b84fdf13e3567a12"],
        "after_step_3": [223, "12eedecf24ef4ed1dadeec92d2806ccc"],
        "after_step_4": [241, "66ce9c3b17214245e12caed686ba4cb8"],
        "after_step_5": [253, "34a12c5738d0ca6b2795493a80eea82c"],
        "after_step_6": [228, "bb15bcfdc7fba04ec33d05e9e404999a"],
        "after_step_7": [264, "c866f39722358bc7001fa2be2176aaff"],
        "backwards_correction": [299, "76a4f23b879581776ff3c7e727cf6495"],
        "blind_robot": [299, "d446439c5808465be405ca8cebfca2e5"],
        "eternal_gap": [299, "c5b4238b70bfb48ec771bbaf77af8d0f"],
        "finished": [299, "f31dda1bc2fa93e5ffcf532b49cf13e4"],
        "straight_liner": [299, "23f7ab89d8bba9f5b78739f79bd4c107"],
        "uncalibrated_run": [298, "1a948c9d74ae0e098ea4fc2abb55681f"],
    },
    "9": {
        "after_step_1": [299, "a7855448e7a3da229c0c2ed838cb6535"],
        "after_step_2": [313, "dcd7aecebcac407e1bb9437022ac06f3"],
        "after_step_3": [316, "31dde7f782d5357e843b32322af262c6"],
        "after_step_4": [329, "64f93359a25dda651f061f0c43944ec6"],
        "after_step_5": [335, "70c35121865db69d8dc1d0b7843abd30"],
        "after_step_6": [336, "d959e6a8ceee26d1ea9e01348d7853d7"],
        "after_step_7": [349, "694d45af5b62de8cc9b6b3382acbfa35"],
        "blind_corners": [373, "bd8a33cfa893ef57e7a0515f25e2600e"],
        "finished": [373, "ac3a6434907c708e60db66d3fc5c9f5b"],
        "mirror_dispatch": [373, "c2a6e94db341cc9214243eebdb08b23a"],
        "missing_break": [372, "574226b75e8e6301552b680602efae0d"],
        "one_turn_wonder": [372, "5cc5787dda3be4b2756b39e1837288df"],
        "paranoid_green": [373, "ec472a946f8d898940c6b998328379ee"],
    },
    "10": {
        "after_step_1": [373, "ac3a6434907c708e60db66d3fc5c9f5b"],
        "after_step_2": [392, "954089d49b12b89225841dddc74fafa7"],
        "after_step_3": [396, "b797447222af5a293c751a84ec33abff"],
        "after_step_4": [408, "6efcbc659f2754c0fc63639116f2e765"],
        "after_step_5": [413, "bada43a3ea307fa6f07f64ed6020f281"],
        "after_step_6": [417, "600a5745c032cd0665732a0987d1efdc"],
        "after_step_6b": [429, "8110f843d04a9f3831011719b8021bb4"],
        "after_step_7": [448, "a73e59df789f36a532be8c873efccab4"],
        "after_step_8": [503, "c9cd75d3eacdcf36c4d976c0a551ed24"],
        "bonus_b1": [510, "6614b261be3b9725511b9b2608848fe3"],
        "bonus_b2": [510, "9cf8083cba4bf9120d822d96d4626922"],
        "bonus_b3": [511, "ab056f42d7a72d5ce4e5433a6cf75f73"],
        "bonus_b4": [521, "4a078ff40641d03128f922005e5b2282"],
        "bonus_b5": [511, "d106f83ba2cf4f9839534b7dc79dd194"],
        "finished": [511, "3c2217890f300f9f49f2c6a709316201"],
        "sq_a_turn": [240, "17a61554961e1f6b7fd809a7456fb70f"],
        "sq_b_distance": [240, "35b037d153b83129b3e45ec4455d51f0"],
        "sq_c_corner": [244, "0f2760ac6ea91953e738812c2c953656"],
        "sq_d_square": [251, "306d47acfa89d1fb46846f5b2f668c38"],
        "sq_e_encoder": [245, "b20dfe0697071ed5f357ff65013e549d"],
        "step_4_RED": [397, "96220b714d7096bec9f50183255169a4"],
        "step_8_timed": [513, "ff69f6d02430fde9123f24bcd4e2f877"],
    },
    "11": {
        "after_step_1": [511, "3c2217890f300f9f49f2c6a709316201"],
        "after_step_2": [514, "af7fa8201bf1d7c03d36387809d934dc"],
        "after_step_3": [515, "b3cf275d19f6f937d2ac76f5a97ce29e"],
        "after_step_4": [524, "2cd3b50ef34930bcf59c0339deb524ee"],
        "after_step_5": [519, "7d3119cbc5f4b1890d4c7ca114a3cd0c"],
        "b1_onewheel": [546, "1b96a32d024f5f908e17a51ed178183b"],
        "b2_norearm": [545, "ff1fea12a8ae4b83371c0a7ea4d9c296"],
        "b3_trim": [546, "95ab623a7606660c5e79f9cfe8a229a5"],
        "b4_counts": [546, "36da8515dc049e6bd31f92647271c3f5"],
        "c1_backup": [551, "73edc9911029e8feb9135d6ce9eb9a0e"],
        "c2_hunt": [555, "b5f6d3b81bab39a5407b093fa8079380"],
        "c3_speed": [549, "ea835d0d8adb95669406c02a5326b151"],
        "cal_7a": [561, "396307653c7513e8a2a2f8fc0461ff93"],
        "cal_7b": [546, "c26ecce3e0ff63fad824c3f1dd4736f9"],
        "cal_7d": [550, "30effb1ebc0f9263a6818477188f3a01"],
        "cal_7e": [547, "96623204b29f00de922cd30745612bd3"],
        "finished": [546, "eba175425705f96fbb9841ca080893fa"],
    },
    "12": {
        "after_step_1": [546, "eba175425705f96fbb9841ca080893fa"],
        "after_step_2": [548, "4ff4631487cfa160452a94425b8e5a4a"],
        "after_step_3": [549, "27d8508e5558ee65bc41174095a1a28e"],
        "after_step_4": [553, "37c2ceedcf47333dcdbae2bfca5e1a7e"],
        "after_step_5": [586, "a4386ec4f0f4a63b57579aa1354bf195"],
        "after_step_6": [587, "916ac370b450d3d148133900c7819b93"],
        "after_step_7": [599, "7945c1cab75ffbc7cdd7412e2246bb33"],
        "after_step_8": [605, "a061ab3a03a573fb8165cf0f1e83fe36"],
        "b1_spinning_cal": [607, "9f7be359140c2c9327375b8656199feb"],
        "b2_no_update": [604, "553c2a9c5da9eddf1142772bec88a166"],
        "b3_reset_hoisted": [605, "68117672d0ed53d6941ea28cb0c02edd"],
        "b4_trim_in_turn": [605, "e8b9d74a6f184d01914b7537e1e045c3"],
        "c1_heading": [454, "b5ed46ac687f0e0cd310ef9db2f79730"],
        "c2_slipalarm": [464, "7701d70e79d3983a2f5d95842d6c07e8"],
        "c3_stuckguard": [465, "86a16723e63cb673d1406db447d9e6bb"],
        "c4_shortway": [460, "5e6aadbc12a389a071bd04152b11e55a"],
        "c5_square": [473, "731067bf7707f18bb3984ac5d6092652"],
        "c6_driftmeter": [447, "b29078dfb28c2d88f8d48032a121bd98"],
        "cal_7a": [443, "362a42f67d3829757d3ba4e4e3c95bcf"],
        "cal_7b": [447, "8c6328e0cd96127d6ccb87ba9101f7fd"],
        "cal_7c": [450, "4ce14d82ff119f6cebf0ad9c57c6db46"],
        "cal_7d": [447, "d116232ba7ecc098a26fe1b05f455b52"],
        "cal_7e": [456, "eb89419e3415fb8be881222dd70118c4"],
        "finished": [605, "a061ab3a03a573fb8165cf0f1e83fe36"],
    },
    "13": {
        "after_step_1": [614, "5fc5d302fcc128fe82f452d7f06b3943"],
        "after_step_2": [625, "0ba84c379b417c704b08683fbd88c94e"],
        "after_step_3": [644, "f9f0c6fed6811380f01258e3fcd84d32"],
        "after_step_4": [668, "78fd47281b4b61fa83c43eab62c86670"],
        "after_step_5": [689, "1fb7bc97660a2dc2639020237340388f"],
        "after_step_6": [717, "da3d9c25fdcf701f701b8b209800db13"],
        "bonus_b1_spun_zero": [736, "dbe3790952de5de6f3e1286a63f9fcd6"],
        "bonus_b2_unspent_trim": [736, "a07a1ff2449311888224e0bb071f3d01"],
        "bonus_b3_blind_stripes": [736, "052fb421ecc66a2bed28a793dcdf39ae"],
        "bonus_b4_invisible_door": [736, "cb3ed4d35a7e1ac8819b97c1aa83f687"],
        "c4_landmark": [738, "eef5c048164fffd54fd7153efde82133"],
        "c5_striplog": [743, "0df77d2e46e1050f18fb7d3daceb5fd2"],
        "challenge_9_1_keep_sweeping": [741, "56f773639498afb1de52b2cd0675c298"],
        "challenge_9_2_sweep_report": [753, "5d95e8d028dc8da35a5d5535406286a9"],
        "challenge_9_3_row_zero": [745, "7e626494083c85535b4fa9d511f2c539"],
        "finished": [736, "28e6c5da8bb1df7d64c6340ca22a66ea"],
        "ladder_7a_surface_meter": [353, "bb17e1a7e89a25ab0f95661087beb32a"],
        "ladder_7b_silver_brake": [644, "f9f0c6fed6811380f01258e3fcd84d32"],
        "ladder_7c_leg_and_turn": [366, "074bff86afb688cd1352974eb59addd7"],
        "ladder_7d_full_sweep": [736, "28e6c5da8bb1df7d64c6340ca22a66ea"],
        "ladder_7e_encoder_turns": [736, "8a7287a0500f63ec21ae69bbaa99ef9b"],
    },
    "14": {
        "after_step_1": [742, "e2e4691e95ca015575b10342d0b9ba24"],
        "after_step_2": [812, "3ee5c26a474b154a1cbef47a90ac691b"],
        "after_step_3": [813, "6b0e5c3cf20be705206950aa18aee997"],
        "bonus_b1_always_passes": [814, "12c9394e3b277a963e56be4850d31830"],
        "bonus_b2_loose_gyro": [813, "dc7a05e0f7bceaccd1d6d2d561b65cdb"],
        "bonus_b3_dropped_zero": [813, "8e7ef7b6624af7fe51f257bcc873c39a"],
        "bonus_b4_guarded_kill": [813, "1c5ece436856b375ce34ed9b3daaebc7"],
        "challenge_9_1_wheel_test": [828, "3076e7b74038bff5cdb0b5d3be166e0c"],
        "challenge_9_2_strict_mode": [813, "87a1d52cb13e9e8f36d9cc535ae9b125"],
        "challenge_9_3_lop_counter": [828, "1b07ee271304ce2c1af879e36c239658"],
        "finished": [813, "bd9dd9d595d2f748850318d5b3035c15"],
        "ladder_7c_match_mode": [813, "e38661e93ec6b622b0518c2fbfe4f4c7"],
    },
    "15": {
        "after_step_1": [813, "bd9dd9d595d2f748850318d5b3035c15"],
        "after_step_2": [820, "29b89134f539ca436e29bd49bb70ac0a"],
        "after_step_3": [831, "57e4eb0e4b8b05b091944ea9b204af0e"],
        "after_step_4": [835, "fa1ba08cf37cfe03dae63ae02ce1c4e7"],
        "after_step_5": [905, "cf3d1a34e6208d1ada76fd67c2210dec"],
        "after_step_6": [909, "6f0ebdcb97f6cc821b66362b067148da"],
        "bonus_b1_millis_dt": [940, "220dea159835cef903637ed8182e7d6a"],
        "bonus_b2_stale_lasterror": [939, "5b1efb16f2a6ab569262c7aaa5021145"],
        "bonus_b3_no_doorway": [939, "aa2c3a60cb527becebf5277c1c5a88eb"],
        "bonus_b4_kd_sign": [940, "45a607676d92969df953e65084b04345"],
        "challenge_9_1_gain_scheduling": [943, "f16fbeb9cb7c42dadf92c87690849b3a"],
        "challenge_9_2_d_filter": [944, "faa6bfddf07929c047910dd42e37b33a"],
        "challenge_9_3_worst_dt": [944, "7e1762975f1c419e88e7bc0e26bf6011"],
        "finished": [940, "31da2612662b6f6e2c251c4dcedce701"],
        "ladder_7a_stripchart": [845, "f4bc92aa70341c21bd6904eea8924f45"],
        "ladder_7d_i_on_line": [914, "cabbe9edf7c1dc289db5bf524b99a52a"],
    },
    "16": {
        "after_step_1": [940, "31da2612662b6f6e2c251c4dcedce701"],
        "after_step_2": [962, "9a7eacd0b8c9d33876bb18e819dadfa3"],
        "after_step_3": [987, "10a3124d8712434fc7123f30269a5c22"],
        "after_step_4": [1032, "2b2882409bf0f7c83188bb4a41f3dd25"],
        "after_step_5": [1005, "88cbe8ac71a77f6f56f8b3205c1c3b65"],
        "bonus_b1_bell_mode": [1011, "02996161015bed2daa64e08eb88459e8"],
        "bonus_b2_wrong_magic": [1011, "6c5e944318e844c17677cb878217f16d"],
        "finished": [1011, "02a860d4ffcd7c7a24f3c8aca7b6ec3c"],
        "step_5_serial_traded": [1017, "2c3c5c2e294456aab09d1a652ce892fa"],
        "step_5_zn_traded": [1011, "b90523cd60ec427932de0c56bbb7a2f2"],
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

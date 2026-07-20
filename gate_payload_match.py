#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAYLOAD BYTE-MATCH GATE (Bible §11) — v1.6, S56
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
    ("3", "constrain", "// (empty - the run happens once, in setup)"):
        "L03 constrain whole-template starter (S44, §18.3): starter-only comment, no derivation source",
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
    ("3", "ramp", "// (empty - the ramp happens once, in setup)"):
        "L03 ramp whole-template starter (S44, §18.3): starter-only comment, no derivation source",
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
    ("3", "ramp", "// (In Lesson 5 you'll learn the for loop, which does this climb for you.)"):
        "L03 ramp whole-template starter (S44, §18.3): starter-only L05 forward-reference, no derivation source",
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
        "c01": [101, "9a19defc17a54a2c2064885b3c92b8ab"],
        "c02": [33, "08ca58452dffb720dc61f39f47588c22"],
        "c03": [30, "55a68a42210fda651876a117a0714372"],
        "c04": [36, "0a11103c26a3194fbc3b551a41cc7107"],
        "c05": [34, "fb80eeb4ef1218ad5b73f81307df7ccb"],
        "c06": [42, "3e23bd39ae126185bbd529a80fac16f9"],
        "c07": [72, "8cc29c06520d2c3014a40216a0d7335a"],
        "c08": [76, "9552ea0166fdcf891238ea9811418188"],
        "c09": [48, "fed732800ae0f97364bbc2bfac479b56"],
        "c10": [60, "e72b11b9e0b2c8034e18835baa4f5d27"],
        "c11": [103, "f66db059cec915d2a20cbb3a33416c18"],
    },
}

ADVISORY = []
OBSERVED_FP = {}

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

def check_payload_text(name, text, corpus, fails):
    chunks = [c for c in re.split(r'\n\s*\n', text) if len(c.strip()) >= MIN_CHARS]
    for c in chunks:
        if c.strip() in corpus:
            continue
        # line-wise fallback: every non-empty line appears verbatim in a canonical
        # source (handles payload glue assembled from lesson-verbatim lines)
        lines = [l.strip() for l in c.split('\n') if l.strip()]
        if lines and all(l in corpus for l in lines):
            continue
        missing = [l for l in lines if l not in corpus] or [c.strip()[:60]]
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
    args = [a for a in sys.argv[1:] if a != "--update-fp"]
    update_fp = "--update-fp" in sys.argv
    maker_path, lesson_paths = args[0], args[1:]
    mk = open(maker_path, encoding='utf-8').read()
    js = re.search(r'<script>(.*)</script>', mk, re.S).group(1)
    fails, notes = [], []

    open('/tmp/_gate.js', 'w').write(js)
    r = subprocess.run(['node', '--check', '/tmp/_gate.js'], capture_output=True, text=True)
    if r.returncode: fails.append("JS SYNTAX: " + r.stderr.strip()[:120])

    payloads, _ = brace_json(js, 'var PAYLOADS = ')
    tpl_corpus = maker_templates(js)

    kinds = {}
    for m in re.finditer(r'(\d+): \[(.*?)\n    \]', js, re.S):
        L = m.group(1)
        kinds[L] = re.findall(r'\[\s*"([a-z_0-9]+)"(?:[^\]]*?)"(after_step_\d+|finished|capstone|[a-z_0-9]+)"\s*\]', m.group(2))
    # registry key resolution
    for m in re.finditer(r'"(after_step_\d+|finished|capstone)"\]', js):
        pass  # per-lesson resolution below

    lessons = {}
    for p in lesson_paths:
        n = re.search(r'Lesson_0?(\d+)_', os.path.basename(p)).group(1)
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

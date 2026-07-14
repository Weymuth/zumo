#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAYLOAD BYTE-MATCH GATE (Bible §11) — v1.1, S22
v1.1 INHERITANCE RULE: lesson N's corpus additionally includes lesson N-1's
'finished' payload bodies — inheriting lessons (L08+) copy the prior project
wholesale in Step 1, so files carried unchanged are canonical by construction.
Byte-strict: modified content must still appear in lesson N's own pres.
Prior: v1.0, S21
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
        fails.append(f"{name}: unmatched: {missing[0][:70]!r}")

def main():
    maker_path, lesson_paths = sys.argv[1], sys.argv[2:]
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
            else:
                n_files += 1
                check_payload_text(f"L{L}/{key}", pay, corpus, fails)
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
    if fails:
        print(f"GATE: FAIL ({len(fails)})")
        [print("  -", f) for f in fails[:20]]
        sys.exit(1)
    print("GATE: PASS — every payload byte-derives from lesson pres + Maker templates")

if __name__ == "__main__":
    main()

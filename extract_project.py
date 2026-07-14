#!/usr/bin/env python3
"""Materialize a Maker payload (lesson N, kind K) into a compilable project dir.
Inheritance: starts from lesson N-1's 'finished' files, overlays lesson N kind K.
Chain bottoms out at the earliest lesson that defines 'finished'.
Usage: extract_project.py <newproject.html> <lesson> <kind> <outdir>
"""
import re, sys, json, os

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
    return json.loads(txt[j:k+1])

def payload_files(P, lesson, kind):
    """Return {filename: body} for one payload. String payload = main.cpp body."""
    p = P[str(lesson)][kind]
    if isinstance(p, str):
        return {"main.cpp": p}
    # object payload: {filename: body, ...} possibly with meta keys
    return {k: v for k, v in p.items() if isinstance(v, str) and ("." in k)}

def materialize(P, lesson, kind):
    """Inheritance walk: overlay lesson N kind on N-1 finished on N-2 finished..."""
    chain = []
    L = int(lesson)
    # walk down collecting finished payloads
    l = L - 1
    while str(l) in P and "finished" in P[str(l)]:
        chain.append((l, "finished"))
        l -= 1
    files = {}
    for l_, k_ in reversed(chain):
        files.update(payload_files(P, l_, k_))
    files.update(payload_files(P, lesson, kind))
    return files

if __name__ == "__main__":
    maker, lesson, kind, outdir = sys.argv[1:5]
    txt = open(maker, encoding="utf-8").read()
    P = brace_json(txt, "var PAYLOADS = ")
    files = materialize(P, lesson, kind)
    os.makedirs(outdir, exist_ok=True)
    for fn, body in files.items():
        with open(os.path.join(outdir, fn), "w", encoding="utf-8") as f:
            f.write(body if body.endswith("\n") else body + "\n")
    print(f"L{lesson}/{kind}: {len(files)} files -> {outdir}: {sorted(files)}")

#!/usr/bin/env python3
# book_gates.py v1.0 (S65) — whole-book consistency gates.
# Usage:  python3 book_gates.py            (run from repo root)
# Exit 0 = all gates pass. Exit 1 = failures listed.
#
# Run at SESSION OPEN (health check) and before EVERY delivery (close gate).
# Each gate encodes a Bible rule; the Bible section is named on each line.
# When a new rule is canonized, add its gate here in the same session.

import re, glob, html, os, sys, collections

FAIL = []


def gate(name, bad):
    print(f'{"PASS" if not bad else "FAIL":>5}  {name}')
    for b in bad:
        print(f'         {b}')
    if bad:
        FAIL.append(name)


def txt(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s)))


files = sorted(glob.glob('lessons/Lesson_*.html'))
site = files + ['going_deeper.html', 'index.html', 'tutor/tutor.html',
                'newproject.html', 'timer.html']
site = [f for f in site if os.path.exists(f)]


def L(f):
    return f[15:17]


R = {f: open(f, encoding='utf-8').read() for f in site}

# ---- §5b: hidden full version present; both visible banners carry its major.minor
bad = []
for f in files:
    s = R[f]
    hid = re.search(r'v(\d+\.\d+)\.\d+', s[:60])
    vis = re.findall(r'Version (\d+\.\d+)', s)
    if not hid or len(vis) != 2 or any(v != hid.group(1) for v in vis):
        bad.append(f'{L(f)}: hidden={hid.group(1) if hid else None} visible={vis}')
gate('§5b  version: hidden == both visible banners', bad)

# ---- §5b addendum (S65): where BOTH banners carry a date, the dates must agree.
# (L11–L16 footers carry no date by design — that is legal.)
bad = []
for f in files:
    d = re.findall(r'Version \d+\.\d+(?: &mdash;| —) (\w+ \d{4})', R[f])
    if len(d) >= 2 and len(set(d)) != 1:
        bad.append(f'{L(f)}: {d}')
    if len(d) == 0:
        bad.append(f'{L(f)}: no dated banner at all')
gate('§5b  date: dates agree where both banners carry one', bad)

# ---- §22: terminal blocks — [SUCCESS] green #6a9955, diagnostics red #f14c4c
bad = []
for f in files:
    s = R[f]
    for m in re.finditer(r'<pre.*?</pre>', s, re.S):
        blk = m.group(0)
        t = re.sub(r'<[^>]+>', '', blk)
        if re.search(r'error:|undefined reference|\[SUCCESS\]|\[FAILED\]|Writing \||Verifying \|', t):
            if '[SUCCESS]' in t and 'color: #6a9955;">[SUCCESS]' not in blk:
                bad.append(f'{L(f)}@{m.start()}: [SUCCESS] not green')
            if re.search(r'error:|undefined reference', t) and '#f14c4c' not in blk:
                bad.append(f'{L(f)}@{m.start()}: diagnostic not red')
gate('§22  terminal colors (SUCCESS green / errors red)', bad)

# ---- §4.2: data-challenge markers globally unique
bad = []
seen = collections.Counter()
for f in files:
    for m in re.findall(r'data-challenge="([^"]*)"', R[f]):
        seen[m] += 1
dups = [f'{k} x{v}' for k, v in seen.items() if v > 1]
if dups:
    bad.append('duplicates: ' + ', '.join(dups))
gate('§4.2 data-challenge markers globally unique', bad)

# ---- §4.3: picker labels (element textContent, 60 chars) unique per lesson
bad = []
for f in files:
    s = R[f]
    labels = collections.Counter()
    for m in re.finditer(r'<(\w+)([^>]*data-challenge="[^"]*"[^>]*)>', s):
        tag = m.group(1)
        close = s.find('</' + tag + '>', m.end())
        t = txt(s[m.end():close]).strip()[:60]
        labels[t] += 1
    for t, n in labels.items():
        if n > 1:
            bad.append(f'{L(f)}: "{t[:45]}" x{n}')
gate('§4.3 picker labels unique within each lesson', bad)

# ---- §4.1: retired construct names must not reappear
bad = []
for f in files:
    if re.search(r'CHALLENGE \(\d+ minute', R[f]):
        bad.append(f'{L(f)}: old "CHALLENGE (n min)" label (renamed TRY IT, S65)')
gate('§4.1 no retired construct names', bad)

# ---- §6.12b: two-axis pill parity per lesson
bad = []
for f in files:
    d = len(re.findall(r'data-difficulty=', R[f]))
    g = len(re.findall(r'data-grasp=', R[f]))
    if d != g:
        bad.append(f'{L(f)}: difficulty={d} grasp={g}')
gate('§6.12b pill two-axis parity', bad)

# ---- structure: paired-tag balance across every site file
bad = []
for f in site:
    s = R[f]
    for tag in ['div', 'pre', 'details', 'table', 'iframe', 'strong', 'h3']:
        o = len(re.findall(f'<{tag}\\b', s))
        c = s.count(f'</{tag}>')
        if o != c:
            bad.append(f'{f}: {tag} {o}/{c}')
gate('tag balance (all site files)', bad)

# ---- timers: every iframe has min+label; labels unique per lesson
bad = []
for f in files:
    labs = collections.Counter()
    for m in re.finditer(r'<iframe[^>]*timer\.html([^"]*)"', R[f]):
        q = m.group(1)
        if 'min=' not in q or 'label=' not in q:
            bad.append(f'{L(f)}: timer missing param: {q[:50]}')
        lab = re.search(r'label=([^&"]*)', q)
        if lab:
            labs[lab.group(1)] += 1
    for t, n in labs.items():
        if n > 1:
            bad.append(f'{L(f)}: timer label "{t}" x{n}')
gate('timers: params present, labels unique per lesson', bad)

# ---- links: index.html relative links resolve to real files
bad = []
for m in re.finditer(r'href="([^"#][^"]*)"', R['index.html']):
    u = m.group(1)
    if u.startswith('http'):
        continue
    if not os.path.exists(u):
        bad.append(f'index.html -> {u} MISSING')
gate('index.html relative links resolve', bad)

# ---- links: going_deeper references use canonical URLs
bad = []
for f in site:
    for m in re.finditer(r'href="([^"]*going_deeper[^"]*)"', R[f]):
        if m.group(1) not in ('going_deeper.html',
                              'https://weymuth.github.io/zumo/going_deeper.html'):
            bad.append(f'{f}: {m.group(1)}')
gate('going_deeper links canonical', bad)

print()
print('=' * 52)
if FAIL:
    print(f'{len(FAIL)} GATE(S) FAILED: {", ".join(FAIL)}')
    sys.exit(1)
print('ALL GATES PASS')

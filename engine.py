# -*- coding: utf-8 -*-
"""S37 formatting-repair engine: indenter + L02-style highlighter + payload surgery."""
import re, json, html as H

INDENT = "  "

def sanitize(line):
    """strip string literals and // comments so brace counting is honest"""
    line = re.sub(r'"(?:[^"\\]|\\.)*"', '""', line)
    line = re.sub(r"'(?:[^'\\]|\\.)'", "''", line)
    line = re.sub(r'//.*$', '', line)
    line = re.sub(r'/\*.*?\*/', '', line)
    return line

def reindent(text):
    """brace-depth re-indent, 2-space unit, preserves internal spacing; block-comment aware"""
    out, depth, in_bc = [], 0, False
    for raw in text.split('\n'):
        s = raw.strip()
        if not s:
            out.append('')
            continue
        if in_bc:
            out.append(INDENT * depth + s)
            if '*/' in s: in_bc = False
            continue
        z = sanitize(s)
        if '/*' in z and '*/' not in z.split('/*',1)[1]:
            in_bc = True
            z = z.split('/*')[0]
        lead_close = 1 if s.startswith('}') else 0
        d = max(0, depth - lead_close)
        out.append(INDENT * d + s)
        depth = max(0, depth + z.count('{') - z.count('}'))
    return '\n'.join(out)

# ---- highlighter calibrated to L02 palette ----
KW = r'\b(void|int|unsigned|long|float|bool|char|const|if|else|for|while|return|true|false|switch|case|break)\b'
IDENT = r'\b(Serial|Zumo32U4ButtonA|Zumo32U4ButtonB|Zumo32U4ButtonC|Zumo32U4OLED|Zumo32U4Buzzer|Zumo32U4Motors|Zumo32U4LineSensors|Zumo32U4Encoders)\b'

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def hl_line(line):
    """render one plain line to L02-style span HTML"""
    # split off trailing // comment (not inside a string)
    m = None
    ins = False; i = 0
    while i < len(line) - 1:
        c = line[i]
        if c == '"' and (i == 0 or line[i-1] != '\\'):
            ins = not ins
        elif not ins and line[i:i+2] == '//':
            m = i; break
        i += 1
    if line.strip().startswith('//'):
        lead = line[:len(line) - len(line.lstrip())]
        return lead + '<span style="color: #6a9955;">' + esc(line.strip()) + '</span>'
    mpp = re.match(r'^(\s*)#include\s+(.*)$', line)
    if mpp:
        return (mpp.group(1) + '<span style="color: #c586c0;">#include</span> '
                + '<span style="color: #ce9178;">' + esc(mpp.group(2)) + '</span>')
    comment = ''
    code = line
    if m is not None:
        code, comment = line[:m], line[m:]
    # tokenize code: strings, numbers, keywords, idents
    outp = []
    pos = 0
    token_re = re.compile(r'"(?:[^"\\]|\\.)*"|' + KW + '|' + IDENT + r'|(?<![\w.])\d+(?![\w.])')
    for t in token_re.finditer(code):
        outp.append(esc(code[pos:t.start()]))
        tok = t.group(0)
        if tok.startswith('"'):
            outp.append('<span style="color: #ce9178;">' + esc(tok) + '</span>')
        elif re.fullmatch(KW.strip(r'\b'), tok) or re.fullmatch(r'void|int|unsigned|long|float|bool|char|const|if|else|for|while|return|true|false|switch|case|break', tok):
            outp.append('<span style="color: #569cd6;">' + tok + '</span>')
        elif re.fullmatch(r'\d+', tok):
            outp.append('<span style="color: #b5cea8;">' + tok + '</span>')
        else:
            outp.append('<span style="color: #4ec9b6;">' + tok + '</span>')
        pos = t.end()
    outp.append(esc(code[pos:]))
    if comment:
        outp.append('<span style="color: #6a9955;">' + esc(comment) + '</span>')
    return ''.join(outp)

def hl(text):
    """render text; /* */ block comments become single multi-line comment spans"""
    out = []
    i = 0
    parts = re.split(r'(/\*.*?\*/)', text, flags=re.S)
    for p in parts:
        if p.startswith('/*') and p.endswith('*/'):
            out.append('<span style="color: #6a9955;">' + esc(p) + '</span>')
        else:
            segs = p.split('\n')
            out.append('\n'.join(hl_line(l) if l.strip() else l for l in segs))
    return ''.join(out)

def is_code_block(plain):
    """True for C/C++ code blocks; False for pseudo-code plan/prose blocks"""
    if '\u2192' in plain or '→' in plain:
        return False
    lines = [l for l in plain.split('\n') if l.strip()]
    codey = sum(1 for l in lines if re.search(r'[;{}]\s*$|^\s*(//|/\*|\*/|#include)', l))
    return lines and codey / len(lines) > 0.5

def decode_pre_inner(raw_inner):
    return H.unescape(re.sub(r'<span[^>]*>', '', raw_inner).replace('</span>', ''))

# ---- payload helpers ----
def brace_span(txt, anchor):
    i = txt.index(anchor); j = txt.index('{', i)
    depth = 0; k = j; ins = False; escp = False
    while True:
        c = txt[k]
        if ins:
            if escp: escp = False
            elif c == '\\': escp = True
            elif c == '"': ins = False
        else:
            if c == '"': ins = True
            elif c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0: break
        k += 1
    return j, k + 1

def js_escape(body):
    return json.dumps(body, ensure_ascii=False)[1:-1]

def line_depths(plain):
    """per-line print-depth, block-comment aware (mirror of reindent)"""
    depths, depth, in_bc = [], 0, False
    for raw in plain.split('\n'):
        s = raw.strip()
        if not s:
            depths.append(0); continue
        if in_bc:
            depths.append(depth)
            if '*/' in s: in_bc = False
            continue
        z = sanitize(s)
        if '/*' in z and '*/' not in z.split('/*',1)[1]:
            in_bc = True
            z = z.split('/*')[0]
        lead_close = 1 if s.startswith('}') else 0
        depths.append(max(0, depth - lead_close))
        depth = max(0, depth + z.count('{') - z.count('}'))
    return depths

def raw_indent(inner):
    """indent raw pre-inner HTML: prepend spaces per decoded-line depth; markup untouched"""
    plain = decode_pre_inner(inner)
    depths = line_depths(plain)
    rl = inner.split('\n')
    pl = plain.split('\n')
    assert len(rl) == len(pl), "raw/plain line count mismatch"
    out = []
    for r, p, d in zip(rl, pl, depths):
        out.append((INDENT * d + r.lstrip()) if p.strip() else r)
    return '\n'.join(out)

def indent_flat_only(body):
    """indent ONLY flat inside-brace lines to 2*depth; all other lines byte-identical"""
    depths = line_depths(body)
    out = []
    for l, d in zip(body.split('\n'), depths):
        s = l.strip()
        if s and d > 0 and not s.startswith('}') and not l.startswith((' ', '\t')):
            out.append(INDENT * d + l)
        else:
            out.append(l)
    return '\n'.join(out)

def raw_indent_flat_only(inner):
    """same, on raw pre-inner HTML (depths from decoded text)"""
    plain = decode_pre_inner(inner)
    depths = line_depths(plain)
    rl, pl = inner.split('\n'), plain.split('\n')
    assert len(rl) == len(pl)
    out = []
    for r, p, d in zip(rl, pl, depths):
        s = p.strip()
        if s and d > 0 and not s.startswith('}') and not p.startswith((' ', '\t')):
            out.append(INDENT * d + r)
        else:
            out.append(r)
    return '\n'.join(out)

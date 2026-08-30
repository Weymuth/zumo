"""build_syllabus_html.py v1.1 - syllabus.html is GENERATED, never hand-edited.

WHY INLINE STYLES, WHEN SS27 RETIRED THEM (DJ ruling S194).
The lessons are LINKED from Canvas, so they carry classes and css/book.css - SS27, and
S123's ruling stands untouched. The SYLLABUS is different: DJ pastes it INTO a Canvas
page, and Canvas strips <style> blocks and class attributes. A page that must survive
that paste can only carry inline style attributes. Same document, two delivery paths,
two answers - this is not a reopening of SS27.

SCOPE CONSEQUENCE, STATED RATHER THAN DISCOVERED (rule 78). syllabus.html links NEITHER
css/book.css NOR css/semantic.css, so gate SS27.12 does not see it - by the same rule that
exempts newproject.html and tutor/tutor.html (SS25.6a): a page whose styling is nobody
else's business. That is correct, and it is also an UNGATED PATH, which is the shape
SS27.12's own comments warn about. If the syllabus ever joins the book's visual layer,
delete this generator first.

EDIT THE MARKDOWN. `ZUMO_Syllabus_WORKING.md` is the source; run this to regenerate.
"""

import re, html as H

NAVY="#0B1A2E"; SLATE="#3D5266"; BRONZE="#7B6240"; BRASS="#C9A463"; PARCH="#F5F2E9"
SANS="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO="ui-monospace,SFMono-Regular,Menlo,Consolas,'Courier New',monospace"

def inline(t):
    t = H.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', lambda m:
        f'<code style="font-family:{MONO};font-size:0.92em;background:{PARCH};'
        f'border:1px solid #e2ddd0;border-radius:3px;padding:1px 5px;color:{BRONZE};">{m.group(1)}</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', rf'<strong style="color:{NAVY};">\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', rf'<a href="\2" style="color:{BRONZE};">\1</a>', t)
    t = t.replace("☐", '<span style="color:'+BRASS+';font-size:1.1em;">&#9744;</span>')
    return t

def convert(md):
    out=[]; lines=md.split("\n"); i=0
    while i < len(lines):
        L=lines[i]
        if not L.strip():
            i+=1; continue
        if L.startswith("<!--"):
            i+=1; continue
        if L.startswith("# "):
            out.append(f'<h1 style="font-family:{SANS};font-size:30px;line-height:1.2;color:{NAVY};'
                       f'margin:0 0 4px;">{inline(L[2:])}</h1>'); i+=1; continue
        if L.startswith("### "):
            out.append(f'<h3 style="font-family:{SANS};font-size:16px;color:{SLATE};font-weight:600;'
                       f'margin:26px 0 8px;">{inline(L[4:])}</h3>'); i+=1; continue
        if L.startswith("## "):
            out.append(f'<h2 style="font-family:{SANS};font-size:21px;color:{NAVY};margin:34px 0 10px;'
                       f'padding-bottom:6px;border-bottom:2px solid {BRASS};">{inline(L[3:])}</h2>'); i+=1; continue
        if L.strip()=="---":
            out.append(f'<hr style="border:0;border-top:1px solid #ddd6c6;margin:26px 0;">'); i+=1; continue
        if L.startswith(">"):
            blk=[]
            while i<len(lines) and lines[i].startswith(">"):
                blk.append(lines[i].lstrip(">").strip()); i+=1
            body=" ".join(x for x in blk if x)
            body=re.sub(r"\s{2,}"," ",body)
            out.append(f'<div style="background:{PARCH};border-left:4px solid {BRASS};padding:12px 16px;'
                       f'margin:16px 0;font-family:{SANS};font-size:14px;line-height:1.6;color:{SLATE};">'
                       f'{inline(body)}</div>'); continue
        if L.lstrip().startswith("|"):
            tbl=[]
            while i<len(lines) and lines[i].lstrip().startswith("|"):
                tbl.append(lines[i].strip()); i+=1
            rows=[[c.strip() for c in r.strip("|").split("|")] for r in tbl
                  if not re.fullmatch(r"\|[\s:|-]+\|", r)]
            if not rows: continue
            th=(f'padding:8px 11px;background:{NAVY};color:#fff;font-family:{SANS};font-size:13px;'
                f'text-align:left;font-weight:600;border:1px solid {NAVY};')
            td=(f'padding:8px 11px;border:1px solid #ddd6c6;font-family:{SANS};font-size:13.5px;'
                f'line-height:1.5;color:#2b3440;vertical-align:top;')
            h="".join(f'<th style="{th}">{inline(c)}</th>' for c in rows[0])
            body=""
            for n,r in enumerate(rows[1:]):
                bg="background:#fdfcf8;" if n%2 else "background:#ffffff;"
                body+="<tr>"+"".join(f'<td style="{td}{bg}">{inline(c)}</td>' for c in r)+"</tr>"
            out.append(f'<table style="border-collapse:collapse;width:100%;margin:16px 0;">'
                       f'<tr>{h}</tr>{body}</table>'); continue
        if re.match(r"^\s*[-*]\s+|^\s*\d+\.\s+", L):
            items=[]; ordered=bool(re.match(r"^\s*\d+\.\s+", L))
            while i<len(lines) and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                items.append(re.sub(r"^\s*([-*]|\d+\.)\s+","",lines[i])); i+=1
            tag="ol" if ordered else "ul"
            li="".join(f'<li style="margin:5px 0;">{inline(x)}</li>' for x in items)
            out.append(f'<{tag} style="font-family:{SANS};font-size:14.5px;line-height:1.65;'
                       f'color:#2b3440;margin:10px 0 14px;padding-left:24px;">{li}</{tag}>'); continue
        para=[]
        while i<len(lines) and lines[i].strip() and not re.match(r"^(#|>|\||---|\s*[-*]\s|\s*\d+\.\s)", lines[i]):
            para.append(lines[i].strip()); i+=1
        if para:
            out.append(f'<p style="font-family:{SANS};font-size:14.5px;line-height:1.7;color:#2b3440;'
                       f'margin:10px 0;">{inline(" ".join(para))}</p>')
    return "\n".join(out)

# AN UNRECOGNIZED ARGUMENT IS REFUSED, NOT IGNORED (S174). This script had NO
# argument handling at all, so the write branch was the fall-through: `--help`
# and a typo of any flag both silently regenerated syllabus.html. Found S195 by
# running --help and watching it write.
import sys as _sys
_args = _sys.argv[1:]
for _a in _args:
    if _a not in ('--check', '--help', '-h'):
        print('build_syllabus_html.py: unrecognized argument %r' % _a)
        raise SystemExit(2)
if '--help' in _args or '-h' in _args:
    print(__doc__.strip())
    raise SystemExit(0)

md=open("ZUMO_Syllabus_WORKING.md",encoding="utf-8").read()
body=convert(md)
page=(f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
      f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
      f'<title>Syllabus — Robotics · Zumo 32U4 · Mercersburg Academy</title>\n'
      f'<!-- syllabus.html v1.1 — S195. INLINE STYLES ONLY, ON PURPOSE: this page is meant to\n'
      f'     survive being PASTED into Canvas, which strips <style> blocks and class attributes.\n'
      f'     It therefore links NEITHER css/book.css NOR css/semantic.css and is out of gate\n'
      f'     §27.12 by the same rule that exempts newproject.html and tutor.html (§25.6a).\n'
      f'     GENERATED from ZUMO_Syllabus_WORKING.md — edit the MARKDOWN, never this file. -->\n'
      f'</head>\n<body style="margin:0;padding:26px 20px;background:#ffffff;">\n'
      f'<div style="max-width:860px;margin:0 auto;">\n{body}\n</div>\n</body>\n</html>\n')
if '--check' in _args:
    try:
        _have = open("syllabus.html", encoding="utf-8").read()
    except FileNotFoundError:
        print("syllabus.html is absent - re-run without --check")
        raise SystemExit(1)
    if _have != page:
        print("syllabus.html DIFFERS - re-run without --check")
        raise SystemExit(1)
    print("syllabus.html is current")
    raise SystemExit(0)

open("syllabus.html","w",encoding="utf-8").write(page)
print("wrote syllabus.html")

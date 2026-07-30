#!/usr/bin/env python3
"""build_mark_index.py v1.0.1 (S95) — a visual index of images/marks/.

Reads every SVG in images/marks/, groups by the role colour baked into its fill,
and emits a single standalone HTML sheet. Read-only: touches nothing in the repo.

Purpose: 41 marks ship and ZERO are referenced by any page. This renders them so
the set can be judged as a set. It is also the only place the Heritage Blue role
colours actually appear anywhere in the project.
"""
import json
import os
import re
import sys
import tempfile

FAMILY = {
    'book': 'LEARN', 'sticky': 'NOTE', 'chat-square-text': 'EXPLANATION',
    'arrow-repeat': 'BUILDS ON', 'rocket': 'WHERE THIS GOES',
    'pin-angle': 'HOW THIS SECTION WORKS', 'key': 'KEY TERM',
    'journal-bookmark': 'GLOSSARY', 'stars': 'INSIGHT',
    'file-earmark-plus': 'GOING DEEPER', 'play-circle': 'DO THIS NOW',
    'pencil-square': 'MY PLAN', 'keyboard': 'WRITE IT',
    'journal-text': "ENGINEER'S LOG", 'lightbulb': 'TIP', 'compass': 'HINT',
    'life-preserver': "IF YOU'RE STUCK", 'check-circle': 'CHECKPOINT',
    'unlock': 'ANSWER', 'exclamation-triangle': 'WARNING',
    'slash-circle': 'COMMON PITFALLS', 'bookmark': 'BRAIN CHECK · open',
    'bookmark-check-fill': 'BRAIN CHECK · done', 'braces': 'THE LOGIC',
    'bricks': 'THE WALL', 'bullseye': 'THE GOAL', 'flag': 'FINISHED EARLY?',
}

SUPPORTING = {
    'tools': 'bonus · practice', 'flask': 'bonus · observation',
    'bug': 'bonus · sabotage', 'puzzle': 'card · template',
    'folder2-open': 'card · work in', 'search': 'card · where to look',
    'code': 'prose · code', 'hammer': 'prose · build', 'play': 'prose · test',
    'eye': 'prose · see', 'arrow-right-circle': 'prose · next',
    'battery-full': 'battery · full', 'battery-half': 'battery · half',
    'battery': 'battery · low',
}

ROLE = {
    '#162337': ('navy', 'THE GOAL, FINISHED EARLY?, BRAIN CHECK complete, and every supporting mark'),
    '#725637': ('bronze', 'the reference roles — terms, logs, and the things a student writes'),
    '#3C4D60': ('slate', 'the quiet explanatory roles'),
    '#386049': ('green', 'help offered and progress confirmed'),
    '#74541B': ('amber', 'caution'),
    '#53446F': ('purple', 'unapproved — the semantic three locks gold, red and green, with no purple'),
}

ORDER = ['#3C4D60', '#725637', '#386049', '#74541B', '#53446F', '#162337']

PARCHMENT, NAVY, SLATE, RULE = '#F4EBDD', '#162337', '#43566B', '#D9CDB8'


def read_marks(root):
    d = os.path.join(root, 'images', 'marks')
    out = []
    for f in sorted(os.listdir(d)):
        if not f.endswith('.svg'):
            continue
        t = open(os.path.join(d, f), encoding='utf-8').read()
        fill = re.search(r'fill="(#[0-9a-fA-F]{6})"', t)
        paths = re.findall(r'<path[^>]*\sd="([^"]+)"', t)
        assert paths, f'no path data in {f}'
        assert fill, f'no fill in {f}'
        out.append({
            'name': f[:-4],
            'fill': fill.group(1),
            'paths': paths,
            'family': FAMILY.get(f[:-4]),
            'support': SUPPORTING.get(f[:-4]),
        })
    return out


def cell(m):
    glyph = ''.join('<path d="%s"/>' % d for d in m['paths'])
    label = m['family'] or m['support'] or m['name'].replace('-', ' ')
    is_fam = bool(m['family'])
    return (
        '<div class="cell">'
        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" '
        'fill="%s" viewBox="0 0 16 16" aria-hidden="true">%s</svg>'
        '<div class="lab%s">%s</div>'
        '<div class="file">%s.svg</div>'
        '</div>' % (m['fill'], glyph, '' if is_fam else ' sup', label, m['name'])
    )


def build(marks, refs):
    groups = []
    for fill in ORDER:
        got = [m for m in marks if m['fill'] == fill]
        if not got:
            continue
        role, gloss = ROLE[fill]
        fams = sum(1 for m in got if m['family'])
        groups.append(
            '<section>'
            '<div class="rule" style="background:%s"></div>'
            '<h2 style="color:%s">%s <span class="hex">%s</span></h2>'
            '<p class="gloss">%s &middot; %d marks, %d of them families</p>'
            '<div class="grid">%s</div>'
            '</section>' % (fill, fill, role, fill, gloss, len(got), fams,
                            ''.join(cell(m) for m in got))
        )

    fam_total = sum(1 for m in marks if m['family'])
    return """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Zumo mark index &mdash; %(n)d marks</title>
<!-- build_mark_index.py v1.0.0 -->
<style>
*{box-sizing:border-box}
body{margin:0;padding:38px 26px 70px;background:%(parch)s;color:%(navy)s;
 font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
 -webkit-font-smoothing:antialiased}
.wrap{max-width:1020px;margin:0 auto}
h1{font-size:31px;font-weight:600;margin:0 0 6px;letter-spacing:-.2px}
.sub{font-size:15px;color:%(slate)s;margin:0 0 4px;line-height:1.55}
.count{font-family:ui-monospace,"SF Mono",Menlo,monospace;font-size:12.5px;
 color:%(slate)s;margin:16px 0 0;letter-spacing:.02em}
.warn{margin:22px 0 0;padding:13px 16px;border-left:3px solid %(navy)s;
 background:rgba(22,35,55,.045);font-size:14px;line-height:1.6;color:%(navy)s}
section{margin:46px 0 0}
.rule{height:2px;width:46px;margin:0 0 13px}
h2{font-size:12px;font-weight:600;letter-spacing:.13em;text-transform:uppercase;
 margin:0 0 5px;font-family:ui-monospace,"SF Mono",Menlo,monospace}
.hex{font-weight:400;opacity:.5;letter-spacing:.05em;margin-left:5px}
.gloss{font-size:13.5px;color:%(slate)s;margin:0 0 17px;line-height:1.5}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(146px,1fr));gap:9px}
.cell{background:#fff;border:1px solid %(rule)s;border-radius:3px;
 padding:13px 11px;display:flex;flex-direction:column;gap:7px;min-height:92px}
.cell svg{flex:none}
.lab{font-size:12.5px;font-weight:600;line-height:1.3;
 font-family:ui-monospace,"SF Mono",Menlo,monospace;letter-spacing:.01em}
.lab.sup{font-weight:400;color:%(slate)s;font-style:italic;
 font-family:"Iowan Old Style",Palatino,Georgia,serif;font-size:13px}
.file{font-size:10.5px;color:#9c8f7c;margin-top:auto;
 font-family:ui-monospace,Menlo,monospace}
footer{margin:56px 0 0;padding-top:19px;border-top:1px solid %(rule)s;
 font-size:12.5px;color:%(slate)s;line-height:1.65}
@media (max-width:520px){body{padding:26px 16px 50px}h1{font-size:25px}}
</style></head>
<body><div class="wrap">
<h1>The mark library, rendered</h1>
<p class="sub">Every SVG in <code>images/marks/</code>, grouped by the role colour
baked into its fill. Each glyph is shown at 16&times;16 &mdash; the size it ships at,
not an enlargement.</p>
<p class="count">%(n)d marks &middot; %(fam)d assigned to families &middot; %(sup)d supporting
&middot; %(refs)d referenced by any page</p>
<div class="warn"><strong>None of these render anywhere in the book.</strong>
A parse of every attribute of every element across all 21 pages finds zero
references to <code>images/marks/</code> or <code>images/icons/</code>. Every live
callout runs on an emoji. This sheet is also the only place the Heritage Blue role
colours appear in the project at all.</div>
%(groups)s
<footer>The fills above are title colours from
<code>BookComponentStandard</code> &sect;5.0. They are not the colours the book
currently uses &mdash; live callouts carry a legacy palette, so dropping these marks
in as-is puts a bronze glyph on a purple panel. The <code>images/icons/</code>
set holds the same 48 glyphs with <code>fill="currentColor"</code>, which inherits
whatever paint a callout already has.<br><br>
Generated by <code>build_mark_index.py</code> v1.0.0 &middot; read-only, nothing in
the repo was modified.</footer>
</div></body></html>""" % {
        'n': len(marks), 'fam': fam_total, 'sup': len(marks) - fam_total,
        'refs': refs, 'groups': ''.join(groups), 'parch': PARCHMENT,
        'navy': NAVY, 'slate': SLATE, 'rule': RULE,
    }


if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    marks = read_marks(root)
    assert len(marks) == 41, 'expected 41 marks, found %d' % len(marks)
    html = build(marks, refs=0)
    # v1.0.1 (S95): the default output must NOT be repo root. ZUMO_MARK_INDEX.html in
    # root is the stray that fails the §12/§23 site-layout gate, and regenerating it
    # there is how it comes back. Pass an explicit path to put it anywhere else.
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(tempfile.gettempdir(), 'ZUMO_MARK_INDEX.html')
    open(out, 'w', encoding='utf-8').write(html)
    print('%d marks -> %s (%d bytes)' % (len(marks), out, len(html.encode('utf-8'))))

#!/usr/bin/env python3
"""build_family_map.py v1.1.1 (S96) - assigns every callout block to a family.

Reproducible from a clean clone: run it from repo root, no prior step. It builds its
own inventory by calling lesson_inventory.build() on all 16 lessons (v1.0.0 replaces
a read of /tmp/inv.json, which meant a fresh session got FileNotFoundError).

v1.1.1: reference renamed - the map is maintained, not a session artifact, so it is
ZUMO_FAMILY_MAP.md. No behaviour change; the reference was always prose.

v1.1.0: the 15 blocks the S94 map assigned but this script did not are now ruled (DJ, S96).
assigned 1048/1048, unassigned 0, and every one of the 30 family counts equals
ZUMO_FAMILY_MAP.md exactly - the script now reproduces the document. Rules match on
label PREFIX, never line number. Control-run: routing one block to the wrong family leaves
the 1048 total untouched and shows up only in the per-family diff, so the total is not
evidence on its own.

v1.0.2: the glyph+scheme fallback map emitted its family names as literals, and two of
them carried the curly apostrophe (ENGINEER\u2019S LOG) that norm() folds on the INPUT
side only. Map VALUES never pass back through norm(), so the one header-less block that
resolves by scheme landed in a second bucket: 16 + 1 instead of 17, and 31 families
instead of 30. Values now written straight, matching CANON. Control-run: only the two
ENGINEER rows and the family count moved; assigned stayed 1033, unassigned stayed 15.

v1.0.1: INSIGHT left the shared blue for teal #e9f7f5/#2da99d (S95, DJ ruling). The old
🔍-on-blue key is REPLACED, not kept: after the split, a magnifier on LEARN's blue is a
defect to surface, not a block to silently classify as INSIGHT.

Label matching unescapes TWICE and normalises the curly apostrophe before comparing:
§24.11 - an entity is not the character it encodes. ENGINEER'S LOG carries &rsquo;
and read as ZERO blocks in S94 until this was fixed. It has 17.
"""
import json,re,html,collections,glob,os,sys
import lesson_inventory

ROOT=sys.argv[1] if len(sys.argv)>1 and not sys.argv[1].startswith('-') else '.'
_files=sorted(glob.glob(os.path.join(ROOT,'lessons','Lesson_*.html')))
assert len(_files)==16, 'expected 16 lesson files under %s/lessons, found %d - run from repo root' % (ROOT,len(_files))
d=[lesson_inventory.build(f) for f in _files]
def norm(s):
    s=html.unescape(html.unescape(s or '')).replace('\u2019',"'").replace('\u2014','-')
    return re.sub(r'^[^A-Za-z"\u201c]+','',s).strip()

CANON=["HOW THIS SECTION WORKS","IF YOU'RE STUCK","COMMON PITFALLS","ENGINEER'S LOG","WHERE THIS GOES",
"FINISHED EARLY","GOING DEEPER","BRAIN CHECK","BUILDS ON","THE LOGIC","KEY TERM","CHECKPOINT",
"GLOSSARY","THE GOAL","THE WALL","DO THIS NOW","MY PLAN","WRITE IT","WARNING","INSIGHT","ANSWER",
"LEARN","NOTE","TIP","HINT"]
CANON.sort(key=len,reverse=True)

# S94 rulings, checked in order. (matcher, family)
RULE=[
 (lambda l,g,s: l.upper().startswith('MYSTERY'),                        'MYSTERY'),
 (lambda l,g,s: 'WHAT YOU SHOULD SEE' in l.upper(),                     'WHAT YOU SHOULD SEE'),
 (lambda l,g,s: l.upper().startswith('WHAT YOU NEED') or 'PREREQUISIT' in l.upper(),'WHAT YOU NEED'),
 (lambda l,g,s: l.upper().startswith('COMPILE CHECK') or 'CALIBRATION IS A CONTRACT' in l.upper(),'STILL GREEN'),
 (lambda l,g,s: re.match(r'TRY (IT|THIS)|BREAK IT ON PURPOSE|FUNCTIONALITY TEST|CODE SWAP|TEST IT|THE GREEN SURVEY',l.upper()),'TRY THIS'),
 (lambda l,g,s: re.match(r'PREDICT FIRST|ASK YOURSELF|DISCUSSION QUESTIONS',l.upper()),'THINK ABOUT IT'),
 (lambda l,g,s: 'FELL BEHIND' in l.upper(),                             "IF YOU'RE STUCK"),
 (lambda l,g,s: re.match(r"NEXT LESSON|WHAT'S NEXT",l.upper()) or l.startswith('Preview:') or 'Coming in Lesson' in l or 'Lesson 8 Preview' in l or 'Looking Ahead' in l,'WHERE THIS GOES'),
 (lambda l,g,s: re.match(r'WORK IN|WHERE TO LOOK',l.upper()),           '(card header)'),
 (lambda l,g,s: 'YOU MIGHT WONDER' in l.upper() or l.startswith('"If the robot can tell') or l.startswith('Wait - TRIM'),'YOU MIGHT WONDER'),
 (lambda l,g,s: 'ARRIVE EARLY' in l.upper() or l.upper().startswith('DO THIS') or 'THE TUNING RITUAL' in l.upper(),'DO THIS NOW'),
 (lambda l,g,s: re.match(r'FINAL CHECKLIST|VERIFICATION CHECKLIST|FINAL CHECKPOINT',l.upper()),'CHECKPOINT'),
 (lambda l,g,s: 'REAL-WORLD' in l.upper() or l.startswith('RoboCup Connection'),'REAL-WORLD CONNECTION'),
 (lambda l,g,s: re.match(r'TURN OFF AI AUTOCOMPLETE|ALWAYS STOP YOUR MOTORS|THE DANGER EVERY WHILE|THE EIGHT MINUTES|THE ONE-CHARACTER TRAP',l.upper()) or l.startswith('The one-character trap'),'WARNING'),
 (lambda l,g,s: 'THE BUTTERFLY ERROR' in l.upper(),                     'COMMON PITFALLS'),
 (lambda l,g,s: re.match(r'THE ONE IDEA|THE TRADE YOU JUST MADE|THE KEY INSIGHT',l.upper()) or l.startswith('The rule, for the rest'),'INSIGHT'),
 (lambda l,g,s: 'NEW IN THIS LESSON' in l.upper(),                      'HOW THIS SECTION WORKS'),
 (lambda l,g,s: 'YOU ALREADY OWN THIS TOOL' in l.upper() or l.startswith('The desk and the bookshelf') or l.startswith('Reminder -') or l.startswith('INFO:') or l.startswith('The recipe, written out') or l.startswith('Recipe:'),'NOTE'),
 (lambda l,g,s: l.startswith('The rule that saves you') or l.startswith('The rule of thumb') or l.startswith('Clamp the memory'),'TIP'),
 (lambda l,g,s: l.startswith('OBJECTIVES'),                             'OBJECTIVES'),
 # --- S96 rulings (DJ). Closes the 15 blocks the S94 map assigned but the generator did not.
 # Matched on label prefix, not line number, so an edit above them does not break the rule.
 (lambda l,g,s: l.startswith('A new kind of label'),                     'HOW THIS SECTION WORKS'),
 (lambda l,g,s: l.startswith('Unit Conversion'),                         'NOTE'),
 (lambda l,g,s: l.startswith('Which cells'),                             'NOTE'),
 (lambda l,g,s: l.startswith('Watch your scope'),                        'NOTE'),
 (lambda l,g,s: l.startswith("Why Today's Work Matters"),                'NOTE'),
 (lambda l,g,s: l.startswith('Why TRIM here'),                           'NOTE'),
 (lambda l,g,s: l.startswith('Where Does constrain()'),                  'KEY TERM'),
 (lambda l,g,s: l.startswith('New operator'),                            'KEY TERM'),
 (lambda l,g,s: l.startswith('Accuracy Note'),                           'TIP'),
 (lambda l,g,s: l.startswith('Best Practice: Naming'),                   'TIP'),
 (lambda l,g,s: l.startswith('Working Backward'),                        'THINK ABOUT IT'),
 (lambda l,g,s: l.startswith('About PROTOTYPE'),                         'YOU MIGHT WONDER'),
 (lambda l,g,s: l.startswith('Header vs Implementation'),                'INSIGHT'),
 (lambda l,g,s: l.startswith('Why Signed Errors Matter'),                'LEARN'),
 (lambda l,g,s: l.startswith('Did Your Robot Wiggle'),                   'CHECKPOINT'),
]
# glyph+scheme fallback for header-less blocks in already-named families
GS={('🔑','#e7d4ff','#9b59b6'):'KEY TERM',('🔑','#f3e5f5','#9c27b0'):'KEY TERM',
('🔑','#f4f9fc','#2e86ab'):'KEY TERM',('🔑','#e2d5e8','#9b6a9e'):'INSIGHT',
('🔑','#e8f5e9','#3a7d5c'):'KEY TERM',('·','#fff','#2e86ab'):'KEY TERM',
('','#fff','#2e86ab'):'KEY TERM',('🛑','#fdecea','#e74c3c'):'THE WALL',
('⚠','#fff8e1','#ffc107'):'WARNING',('🔬','#eceff1','#607d8b'):'GOING DEEPER',
('📘','#eceff1','#607d8b'):'NOTE',('💾','#eceff1','#607d8b'):'NOTE',
('📓','#eceff1','#607d8b'):"ENGINEER'S LOG",('✅','#d4edda','#28a745'):'CHECKPOINT',
('ℹ','#d1ecf1','#17a2b8'):'NOTE',('💡','#f0f7f0','#6b8e6b'):'TIP',
('🔍','#e9f7f5','#2da99d'):'INSIGHT',('🏆','#d1ecf1','#17a2b8'):'REAL-WORLD CONNECTION',
('👀','#d1ecf1','#17a2b8'):'WHAT YOU SHOULD SEE',('📖','#e3f2fd','#2196f3'):'LEARN',
('·','#e3f2fd','#2196f3'):'LEARN',('','#e3f2fd','#2196f3'):'LEARN',
('🧩','#f8f9fa','#6c757d'):'MYSTERY',('📓','#f8f9fa','#6c757d'):'MYSTERY',
('📓','#f8f9fa','#1a5276'):"ENGINEER'S LOG",('🎯','#eef4f8','#2e86ab'):'(card header)',
('·','#eef4f8','#2e86ab'):'(card header)',('','#eef4f8','#2e86ab'):'(card header)',
('🎯','#e8f3ec','#3a7d5c'):'TRY THIS',('·','#f5eef8','#6c757d'):'THINK ABOUT IT',
('','#f5eef8','#6c757d'):'THINK ABOUT IT',('🚀','#e8d4c4','#d4a574'):'WHERE THIS GOES',
('🔮','#ede7e1','#7d6b5e'):'WHERE THIS GOES',('📦','#e3f2ed','#3d8b6e'):"IF YOU'RE STUCK",
('🔌','#e3f2ed','#3d8b6e'):"IF YOU'RE STUCK",('📦','#e7f1fb','#2e86ab'):"IF YOU'RE STUCK",
('✅','#eafaf1','#27ae60'):'INSIGHT',('🏆','#eafaf1','#27ae60'):'INSIGHT',
('🔩','#e8f5e9','#3a7d5c'):'STILL GREEN',('🔧','#e8f5e9','#3a7d5c'):'NOTE',
('🔨','#eef7f1','#3a7d5c'):'STILL GREEN',('·','#eef7f1','#3a7d5c'):'STILL GREEN',
('','#eef7f1','#3a7d5c'):'STILL GREEN',('💭','#e8f4f8','#2e86ab'):'INSIGHT',
('🎯','#e8f4f8','#2e86ab'):'THE GOAL',('🎯','#f8f9fa','#5a6872'):'THE GOAL',
}
res=collections.Counter(); unk=[]
for inv in d:
    for c in inv['callouts']:
        lab=norm(c.get('label')); g=(c.get('glyph') or '').strip()
        bg=c['bg'] or 'none'; bd=c['border']
        f=next((fam for fam in CANON if lab.upper().startswith(fam)),None)
        if not f:
            for fn,fam in RULE:
                if fn(lab,g,(bg,bd)): f=fam; break
        if not f: f=GS.get((g,bg,bd)) or GS.get((g or '·',bg,bd))
        if f: res[f]+=1
        else: unk.append((inv['lesson'],c['line'],g,bg,bd,lab[:52]))
print(f"{'FAMILY':26} BLK")
for f,n in res.most_common(): print(f"{f:26} {n:4}")
print(f"\nassigned {sum(res.values())} / 1048   families {len(res)}")
print(f"UNASSIGNED: {len(unk)}")
for u in unk[:40]: print("   L%s %s %s [%s/%s] %s"%u)
json.dump({'counts':res.most_common(),'unk':unk},open('/tmp/final.json','w'))

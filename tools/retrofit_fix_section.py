#!/usr/bin/env python3
"""Retrofit rule 8 (What would fix this) into archived posts.
Reads posts/<slug>.html and out/fix-retrofit/proposals/<slug>.json, writes out/fix-retrofit/post-<slug>.html
for tools/apply_batch.sh. JSON modes: add (3-5 proposals) | rename (existing fixes heading) | skip.
usage: python3 tools/retrofit_fix_section.py [slug ...]   (default: every proposals/*.json)"""
import sys,re,json,glob,os,html
A=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); S=f'{A}/out/fix-retrofit/proposals'
OUT=f'{A}/out/fix-retrofit'; os.makedirs(OUT,exist_ok=True)
CLOSE='These are proposals from this blog, not recommendations any agency has adopted.'
BLOCK=re.compile(r'<(div|p|h2|h3|h4|section|aside|table|ul|ol)\b',re.I)

_RCACHE={}
def _ranges(s):
    k=id(s),len(s)
    if k not in _RCACHE:
        _RCACHE.clear()
        _RCACHE[k]=[(m.start(),m.end()) for m in re.finditer(r'<(script|style)\b.*?</\1\s*>',s,re.S|re.I)]
    return _RCACHE[k]

def in_script(s,pos):
    return any(a<=pos<b for a,b in _ranges(s))

def first_match(s,pat,flags=re.I|re.S):
    for m in re.finditer(pat,s,flags):
        if not in_script(s,m.start()): return m
    return None

def block_start(s,pos):
    starts=[m.start() for m in BLOCK.finditer(s,0,pos) if not in_script(s,m.start())]
    return starts[-1] if starts else pos

def _all(s,pat,flags=re.I|re.S):
    return [m for m in re.finditer(pat,s,flags) if not in_script(s,m.start())]

def _frac_after(s,pos):
    t=lambda x: len(re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',re.sub(r'<(script|style)\b.*?</\1>','',x,flags=re.S|re.I))))
    return t(s[pos:])/max(1,t(s))

def anchor(s, maxfrac=0.4):
    pos,k=_anchor(s,maxfrac)
    return _lift(s,pos),k

def _lift(s,pos):
    # move out of any enclosing box-like div (card/note/src/disclaimer)
    stack=[]
    for m in re.finditer(r'<(/?)div\b([^>]*)>',s[:pos],re.I):
        if in_script(s,m.start()): continue
        if m.group(1):
            if stack: stack.pop()
        else: stack.append((m.start(),m.group(2)))
    for st,attrs in stack:
        if re.search(r'class="[^"]*(gb-card|gb-note|note|src|disclaimer|disc-override|gb-warn|callout|box)',attrs,re.I):
            return st
    return pos

def _anchor(s, maxfrac=0.4):
    cands=[]
    ms=_all(s,r'(<h[234][^>]*>|<strong[^>]*>|<b>|<p[^>]*>|<div[^>]*>)\s*(?:\d+\.?\s*)?What this piece (?:does|doesn|can|cannot|could|did|is not|isn)')
    if ms: cands.append((ms[-1].start(),'cover') if ms[-1].group(1).lower().startswith(('<h','<p','<div')) else (block_start(s,ms[-1].start()),'cover'))
    ms=_all(s,r'<h[234][^>]*>\s*(?:<[^>]+>\s*)*(?:\d+\.?\s*)?(Sources|Sources and caveats|Sources &amp; caveats|Data sources|Sources and notes|Sources and method|References|Methodology|Method and sources|Notes and sources|Caveats)\b')
    if ms: cands.append((ms[-1].start(),'sources'))
    ms=_all(s,r'<div[^>]*class="[^"]*gb-related')
    if ms: cands.append((ms[-1].start(),'related'))
    ms=_all(s,r'<(p|div)[^>]*class="[^"]*disclaimer')
    if ms:
        dp=ms[-1].start()
        ov=[m for m in _all(s,r'<div[^>]*class="[^"]*disc-override') if m.start()<dp and dp-m.start()<8000]
        cands.append((ov[-1].start() if ov else dp,'disclaimer'))
    for pos,k in cands:
        if _frac_after(s,pos)<=maxfrac: return pos,k
    if cands: return max(cands)
    # fallback: end of document, before any trailing script blocks
    return len(s),'end'

def h2_tag(s):
    for m in re.finditer(r'<h2\b[^>]*>',s,re.I):
        if not in_script(s,m.start()): return m.group(0),'</h2>'
    if re.search(r'\.gb-h2\s*\{',s): return '<h2 class="gb-h2">','</h2>'
    return '<h2>','</h2>'

def build(slug):
    d=json.load(open(f'{S}/{slug}.json',encoding='utf-8'))
    s=open(f'{A}/posts/{slug}.html',encoding='utf-8').read()
    if re.search(r'what would fix this',s,re.I): return 'already'
    mode=d['mode']
    if mode=='skip': return 'skip: '+d.get('reason','')
    closing=f'<p>{CLOSE}</p>\n'
    if mode=='rename':
        want=re.sub(r'\s+',' ',d['heading_text']).strip().lower()
        for m in re.finditer(r'(<h([1-4])\b[^>]*>)(.*?)(</h\2>)',s,re.I|re.S):
            if in_script(s,m.start()): continue
            txt=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',m.group(3)))).strip().lower()
            if txt==want or (want in txt and len(want)>12):
                lvl=m.group(2)
                s2=s[:m.start()]+m.group(1)+'What would fix this'+m.group(4)
                rest=s[m.end():]
                # end of section: next heading of same or higher level, or the anchor
                nxt=re.search(r'<h[1-6]\b|<hr\b|<p[^>]*class="[^"]*(src|disclaimer|sources)|<div[^>]*(id="changelog"|class="[^"]*(gb-related|disclaimer|related))|What this piece (does|doesn|can|could)|>\s*Sources\b',rest,re.I)
                if not nxt: return 'FAIL rename: no section end'
                e=nxt.start()
                seg=rest[:e]
                ends2=[mm.end() for mm in re.finditer(r'</(ul|ol|p)>',seg,re.I)]
                k=ends2[-1] if ends2 else len(seg.rstrip())
                s=s2+seg[:k]+'\n'+closing+seg[k:]+rest[e:]
                break
        else: return 'FAIL rename: heading not found'
    else:
        props=d['proposals']
        if not 3<=len(props)<=5: return f'FAIL count {len(props)}'
        for p in props:
            if re.search(r'<(?!/?b>)',p): return 'FAIL stray tag'
            if CLOSE.lower()[:30] in p.lower(): return 'FAIL closing in proposal'
        pos,kind=anchor(s)
        if pos is None: return 'FAIL no anchor'
        o,c=h2_tag(s)
        sec=(f'\n{o}What would fix this{c}\n<ul>\n'+''.join(f'<li>{p}</li>\n' for p in props)+'</ul>\n'+closing+'\n')
        s=s[:pos]+sec+s[pos:]
        mode=f'add@{kind}'
    open(f'{OUT}/post-{slug}.html','w',encoding='utf-8').write(s)
    return mode

slugs=sys.argv[1:] or sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{S}/*.json'))
from collections import Counter; c=Counter()
for sl in slugs:
    try: r=build(sl)
    except Exception as e: r=f'FAIL {type(e).__name__}: {e}'
    c[r.split(':')[0].split('@')[0] if not r.startswith('add') else r]+=1
    if r.startswith(('FAIL','skip')) or len(slugs)<15: print(sl,'->',r)
print(dict(c))

#!/usr/bin/env python3
"""Offline consistency scan of live posts: old domain, title figures, links to retired posts, past-dated expectations. Report only; writes /tmp/consist.json."""
import json,re,glob,pathlib,collections,datetime as dt,sys
sys.path.insert(0,'tools')
from viz_frame import visible
ROOT=pathlib.Path('.')
man={p['slug']:p for p in json.load(open('meta/manifest.json'))['posts'].values()}
retired=set(json.load(open('out/gsc_index/phase1_remove.json')))|set(json.load(open('out/gsc_index/phase3_map.json')))
today=dt.date(2026,11,15)
MON={m:i+1 for i,m in enumerate('January February March April May June July August September October November December'.split())}
mre='|'.join(MON)
out=collections.defaultdict(list)
for s,p in man.items():
    if s in retired: continue
    f=ROOT/f'posts/{s}.html'
    if not f.exists(): continue
    h=f.read_text(encoding='utf-8',errors='replace'); t=visible(h)
    # old domain/name
    if re.search(r'masaladeutsch\.blogspot|Masala Deutsch',h): out['old-domain-or-name'].append(s)
    # links to retired posts
    bad=sorted({m for m in re.findall(r'href="https?://[^"]*?/([a-z0-9-]+)\.html',h) if m in retired and m!=s})
    if bad: out['links-to-retired'].append((s,bad))
    # future-tense about dates now past: "will ... by <Month> <Year>", "due in <Month> <Year>", "expected in"
    for m in re.finditer(r'(will|expected|due|scheduled|planned|upcoming|set to|to take effect|comes? into force|from)\b[^.]{0,60}?\b(?:(\d{1,2}) )?(%s) (20\d\d)'%mre,t):
        mo,yr=MON[m.group(3)],int(m.group(4)); d=dt.date(yr,mo,min(int(m.group(2) or 1),28))
        if d<today-dt.timedelta(days=20) and m.group(1) in('will','expected','due','scheduled','planned','upcoming','set to'):
            out['future-tense-past-date'].append((s,m.group(0)[:110]))
    # "as of <date>" older than 90 days in a post with newer pub date
    ds=[dt.date(int(y),MON[mo],min(int(d),28)) for d,mo,y in re.findall(r'as of (\d{1,2}) (%s) (20\d\d)'%mre,t)]
    if ds and max(ds)<today-dt.timedelta(days=100): out['as-of-over-100-days'].append((s,max(ds).isoformat()))
    # title numbers present in body
    title=p['title']
    for n in re.findall(r'\d[\d,.]*\d|\d',title):
        if re.fullmatch(r'(19|20)\d\d',n) : continue
        if n not in t and n.replace(',','') not in t.replace(',',''):
            out['title-number-not-in-body'].append((s,n)); break
for k,v in out.items(): print(k,len(v))
json.dump({k:v for k,v in out.items()},open('/tmp/consist.json','w'),indent=1,default=str)

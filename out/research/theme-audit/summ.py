import json,sys,collections
rows=[json.loads(l) for l in open(sys.argv[1])]
for w in (375,1024):
    R=[d for d in rows if d['w']==w]
    print(f'=== {w}px  posts={len(R)}')
    ov=[d for d in R if d['pageOverflow']>2]; print(' page overflow posts:',len(ov))
    oc=collections.Counter(o.split(':')[0] for d in ov for o in d['offenders']); print('  offenders:',oc.most_common(12))
    lk=collections.Counter(); lkp=collections.Counter()
    for d in R:
        for k,v in d['leak'].items(): lk[k]+=v; lkp[k]+=1
    print(' theme-class reuse (elements/posts):',{k:(lk[k],lkp[k]) for k in lk})
    print(' overflow:hidden boxes turned scrollers:',sum(d['ovhScroll'] for d in R),'in',sum(1 for d in R if d['ovhScroll']),'posts')
    mc=collections.Counter(m.split(':')[0] for d in R for m in d['media']); print(' media wider than column:',sum(len(d['media']) for d in R),'in',sum(1 for d in R if d['media']),'posts',mc.most_common(8))
    ab=collections.Counter(); abp=collections.Counter()
    for d in R:
        for k,v in d['adBad'].items(): ab[k]+=v; abp[k]+=1
    print(' ads tried:',sum(d['adsTried'] for d in R),' bad:',{k:(ab[k],abp[k]) for k in sorted(ab)})
    print(' ad-induced page overflow posts:',sum(1 for d in R if d['adOverflow']>d['pageOverflow']+2))

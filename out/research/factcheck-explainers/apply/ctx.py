import re,sys,html
def text(slug):
    t=open(f'posts/{slug}.html',encoding='utf-8').read()
    return t
if __name__=='__main__':
    slug=sys.argv[1]; pats=sys.argv[2:]
    t=text(slug)
    for p in pats:
        for m in re.finditer(p,t,re.I):
            print('---',p,m.start()); print(t[max(0,m.start()-500):m.end()+500])

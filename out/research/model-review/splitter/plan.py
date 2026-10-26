import sys, re, html, json, math
sys.path.insert(0, '.'); import paras
R = '/home/user/blogger_writeups_code'
TURN = re.compile(r"^(But|That|This|These|Then|Yet|So|Still|Second|Third|Fourth|Finally|Meanwhile|However|In |On |For |At |By |What|Where|Why|How|The second|The third|The other|The next|None|Neither|Nothing|Separately|Instead|Even|And yet|Put |Taken|Read |Set |Against|Over |Since|Until|After|Before|Beyond|Under|Unlike|If |Without|Estonia|Denmark|Figures|Data|Sources?|All |Each )")
def plain(x): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip()
def plan(slug):
    s = open(f'{R}/posts/{slug}.html', encoding='utf-8').read()
    out = []
    for n, a, b, tag, text in paras.paragraphs(s):
        w = len(text.split())
        if w < 120 or 'standfirst' in tag: continue
        inner = s[a:b]; bs = paras.boundaries(inner)
        if not bs: out.append((n, w, [], 'NO BOUNDARY')); continue
        cum = [len(plain(inner[:x]).split()) for x in bs]
        pts = [0] + cum + [w]
        turn = [False] + [bool(TURN.match(plain(inner[x:x + 80]))) for x in bs] + [False]
        def cost(i, j):
            size = pts[j] - pts[i]
            return 4 * max(0, size - 95) ** 2 + 4 * max(0, 35 - size) ** 2 + 40
        best = {0: (0, [])}
        for j in range(1, len(pts)):
            opts = [(best[i][0] + cost(i, j) - (60 if turn[j] and j < len(pts) - 1 else 0), best[i][1] + ([j] if j < len(pts) - 1 else []))
                    for i in range(j) if i in best]
            best[j] = min(opts)
        cuts = [j - 1 for j in best[len(pts) - 1][1]]
        out.append((n, w, [(bs[i], cum[i], plain(inner[max(0, bs[i] - 70):bs[i]]), plain(inner[bs[i]:bs[i] + 70])) for i in cuts], tag))
    return out
if __name__ == '__main__':
    allp = {}
    for slug in open('slugs.txt').read().split():
        P = plan(slug); allp[slug] = [(n, [c[0] for c in cuts]) for n, w, cuts, tag in P if cuts and tag != 'NO BOUNDARY']
        for n, w, cuts, tag in P:
            print(f'{slug[:28]} p{n} {w}w {tag[:22]}')
            for off, c, before, after in cuts: print(f'     @{c}w  …{before[-55:]} ‖ {after[:60]}')
    json.dump(allp, open('plan.json', 'w'))

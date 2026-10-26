"""Split long paragraphs per plan.json into out/update-2026-10-26-layout-<slug>.html. Text must be unchanged."""
import json, re, html, sys
sys.path.insert(0, '.'); import paras
R = '/home/user/blogger_writeups_code'
plan = json.load(open('plan.json'))
DROP_LAST = {('a-slice-of-apple-costs-about-1700-slice', 23), ('a-slice-of-apple-costs-about-1700-slice', 27)}
def plain(x): return re.sub(r'[\s;.]', '', html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)\b.*?</\1>', ' ', x, flags=re.S))))
report = {}
for slug, items in plan.items():
    if not items: continue
    s0 = open(f'{R}/posts/{slug}.html', encoding='utf-8').read(); s = s0
    P = {n: (a, b, tag) for n, a, b, tag, t in paras.paragraphs(s0)}
    nsplit = 0
    for n, cuts in sorted(items, key=lambda x: -P[x[0]][0]):
        if (slug, n) in DROP_LAST: cuts = cuts[:-1]
        if not cuts: continue
        a, b, tag = P[n]; inner = s[a:b]
        w = paras.wrapped(inner)
        mid_tag = tag.replace('style="margin:0"', 'style="margin:0 0 .6em"')
        pieces, last = [], 0
        for off in cuts: pieces.append(inner[last:off]); last = off
        pieces.append(inner[last:])
        pieces = [p.strip() for p in pieces]
        pieces = [re.sub(r';$', '.', p) for p in pieces[:-1]] + [pieces[-1]]
        if w:
            o, c = w
            pieces = [p if i == 0 else o + p for i, p in enumerate(pieces)]
            pieces = [p if i == len(pieces) - 1 else p + c for i, p in enumerate(pieces)]
        new = ('</p>\n' + mid_tag).join(pieces)
        # the opening tag before this paragraph keeps its style; non-last pieces need the gap too
        start = a - len(tag)
        assert s[start:a] == tag
        s = s[:start] + mid_tag + new + s[b:] if len(pieces) > 1 else s
        if mid_tag != tag:  # last piece should carry the original tag (original bottom margin)
            k = s.rfind(mid_tag, 0, start + len(mid_tag + new))
            s = s[:k] + tag + s[k + len(mid_tag):]
        nsplit += len(pieces) - 1
    assert plain(s) == plain(s0), slug
    assert len(re.findall(r'<p[\s>]', s)) == len(re.findall(r'</p>', s)) or len(re.findall(r'<p[\s>]', s)) - len(re.findall(r'<p[\s>]', s0)) == len(re.findall(r'</p>', s)) - len(re.findall(r'</p>', s0)), slug
    open(f'{R}/out/update-2026-10-26-layout-{slug}.html', 'w', encoding='utf-8').write(s)
    report[slug] = nsplit
print(report, sum(report.values()))

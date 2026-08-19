import re, json

MD = open('/Users/umashankar/digital-twin-for-ipa/docs/SCHEME_SCRUTINY_MATRIX.md', encoding='utf-8').read()

def parse_section(letter):
    m = re.search(rf'## {letter}\..*?\n\|---.*?\n(.*?)(?=\n## |\Z)', MD, re.S)
    body = m.group(1)
    rows = []
    for line in body.strip().split('\n'):
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) != 9:
            continue
        scheme, first_ann, pib, last_ann, ls, rs, star, first_q, last_q = cells
        rows.append({
            'scheme': scheme, 'first_ann': first_ann, 'pib': pib, 'last_ann': last_ann,
            'ls': ls, 'rs': rs, 'star': star, 'first_q': first_q, 'last_q': last_q,
        })
    return rows

A = parse_section('A')
B = parse_section('B')
C = parse_section('C')
assert len(A) == 51 and len(B) == 35 and len(C) == 10, (len(A), len(B), len(C))

def esc(s):
    return s.replace('&', '&amp;')

# --- duplicate-row detection, same normalization as the site's classify() ---
def norm(s):
    return re.sub(r'[^a-z]', '', s.lower())

def flag_dupes(rows):
    seen = {}
    for r in rows:
        n = norm(r['scheme'])
        seen.setdefault(n, []).append(r)
    dupe_norms = {n for n, rs in seen.items() if len(rs) > 1}
    for r in rows:
        r['dupe'] = norm(r['scheme']) in dupe_norms
    return rows

A = flag_dupes(A)
B = flag_dupes(B)
C = flag_dupes(C)

# Known cross-name duplicate not caught by the strict normalizer (different
# words for the same scheme, not just punctuation/case): carried forward from
# the site's earlier hand-flagged pair.
EXTRA_DUPES = {'PLI-ACC', 'PLI — ACC Battery'}
for r in B:
    if r['scheme'] in EXTRA_DUPES:
        r['dupe'] = True

DUPE_NOTE = '<span style="color:#8a5a12;font-size:.8em"> ⚠ likely duplicate row — a keyword-classification artifact under audit</span>'

def row_html(r):
    name = esc(r['scheme']) + (DUPE_NOTE if r['dupe'] else '')
    last_q = r['last_q'] if r['last_q'] else '—'
    return (f"<tr><td>{name}</td><td>{r['first_ann']}</td>"
            f"<td class=\"num\">{r['pib']}</td><td class=\"num\">{r['ls']}</td>"
            f"<td class=\"num\">{r['rs']}</td><td class=\"num\">{r['star']}</td>"
            f"<td>{last_q}</td></tr>")

def table_html(rows):
    head = ('<thead><tr><th>Scheme</th><th>First announced</th><th class="num">PIB anns</th>'
            '<th class="num">LS Qs</th><th class="num">RS Qs</th><th class="num">&#9733;</th>'
            '<th>Last question</th></tr></thead>')
    body = ''.join(row_html(r) for r in rows)
    return f'<div class="twrap"><table>{head}<tbody>{body}</tbody></table></div>'

table_A = table_html(A)
table_B = table_html(B)
table_C = table_html(C)

# --- top-10 combined LS+RS bars, from BOTH A and B (C has none) ---
combined = A + B
def qn(r, k):
    return int(r[k]) if r[k] else 0
for r in combined:
    r['combined'] = qn(r, 'ls') + qn(r, 'rs')
top10 = sorted(combined, key=lambda r: -r['combined'])[:10]
maxv = top10[0]['combined']

def bar_html(r):
    pct = round(100 * r['combined'] / maxv, 1)
    return (f'<div class="bar"><span class="bl">{esc(r["scheme"])}</span>'
            f'<span class="bt"><i style="width:{pct}%"></i></span>'
            f'<span class="bn">{r["combined"]}</span></div>')

bars_html = '<div class="bars">' + ''.join(bar_html(r) for r in top10) + '</div>'

# UDAN-specific narrative numbers (find it in top10/combined)
udan = next(r for r in combined if 'UDAN' in r['scheme'])
kusum = next((r for r in combined if 'KUSUM' in r['scheme']), None)
semicon = next((r for r in combined if 'Semiconductor' in r['scheme']), None)

out = {
    'pib_total': '4,211',
    'ls_total': '1,890',
    'rs_total': '1,883',
    'countA': len(A), 'countB': len(B), 'countC': len(C),
    'bars_html': bars_html,
    'table_A': table_A, 'table_B': table_B, 'table_C': table_C,
    'udan_ls': qn(udan, 'ls'), 'udan_rs': qn(udan, 'rs'),
    'top10_names': [r['scheme'] for r in top10],
}
json.dump(out, open('/Users/umashankar/masaladeutsch-archive/tools/tmp/most_discussed_data.json', 'w'), indent=1)
print('A dupes:', [r['scheme'] for r in A if r['dupe']])
print('B dupes:', [r['scheme'] for r in B if r['dupe']])
print('top10:', out['top10_names'])
print('UDAN LS', out['udan_ls'], 'RS', out['udan_rs'])

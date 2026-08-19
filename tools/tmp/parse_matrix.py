import re

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
print('A', len(A), 'B', len(B), 'C', len(C))
print(A[0])
print(C[0])

hdr = re.search(r'\(([\d,]+) scheme-mapped announcements\).*?\(([\d,]+) Lok Sabha questions.*?and\n([\d,]+)\nRajya Sabha questions', MD, re.S)
print(hdr.groups() if hdr else 'no header match')

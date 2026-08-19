import json, sys

def build(registry_path, house_field):
    rows = json.load(open(registry_path, encoding='utf-8'))
    # dedupe scheme names per row the same way the site's old generator did
    schemes = sorted({s for r in rows for s in r['schemes']})
    mins = sorted({r['ministry'] for r in rows})
    s_idx = {s: i for i, s in enumerate(schemes)}
    m_idx = {m: i for i, m in enumerate(mins)}
    out_rows = []
    for r in sorted(rows, key=lambda x: (x['iso'], x['qno']), reverse=True):
        sids = sorted({s_idx[s] for s in r['schemes']})
        starred = 1 if (r.get('qtype') or '').upper() == 'STARRED' else 0
        members = r.get('members') or []
        mem = ", ".join(members[:3]) + (" & ors." if len(members) > 3 else "")
        out_rows.append([
            r['iso'], sids, m_idx[r['ministry']], r[house_field],
            starred, r['qno'], r['subject'], r['pdf'], mem
        ])
    D = {"s": schemes, "m": mins, "r": out_rows}
    return json.dumps(D, separators=(',', ':'), ensure_ascii=True), len(rows)

if __name__ == '__main__':
    kind = sys.argv[1]
    if kind == 'ls':
        blob, n = build('/Users/umashankar/digital-twin-for-ipa/data/registers/ls_pq_registry.json', 'lok')
    else:
        blob, n = build('/Users/umashankar/digital-twin-for-ipa/data/registers/rs_pq_registry.json', 'session')
    open(f'/Users/umashankar/masaladeutsch-archive/tools/tmp/{kind}_blob.json', 'w', encoding='utf-8').write(blob)
    print(kind, n, len(blob))

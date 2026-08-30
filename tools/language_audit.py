#!/usr/bin/env python3
"""Daily grammar/usage sweep via LanguageTool's free public API.

Report-only, same contract as tools/multi_model_factcheck.py: this NEVER
edits or publishes a post. It writes one markdown report per flagged post to
out/language_audit/, plus a dated summary index, for a human to review and
decide what (if anything) to fix -- same workflow as the manual pass on
2026-08-10 that found roughly 85% of LanguageTool's own suggestions were
false positives (chart-caption fragments, code identifiers, valid grammar it
misparsed, and a few outright wrong-word substitutions). Auto-applying its
suggestions unattended would silently introduce real errors into live posts.

Uses tools/extract_post.py's structure-aware extraction (title + prose
blocks only, table rows excluded) so table cells and headings don't get
glued into one run-on string -- the bug that made the FIRST audit pass
(pre-2026-08-10) mostly noise.

    python3 tools/language_audit.py            # full sweep, all posts
    python3 tools/language_audit.py --slug X   # single post, prints to stdout
"""
import argparse, glob, json, pathlib, re, sys, time, datetime, urllib.request, urllib.parse

# Resolved from this file's location; kept a str because every use is an
# f-string join. See the note in build_md_summary.py.
ROOT = str(pathlib.Path(__file__).resolve().parent.parent)
OUT_DIR = f'{ROOT}/out/language_audit'
SKIP_SLUGS = {'article-index-start-here', 'about-author'}

sys.path.insert(0, f'{ROOT}/tools')
from extract_post import extract, build_document

CATEGORIES = 'GRAMMAR,CONFUSED_WORDS,CASING,COMPOUNDING,SEMANTICS'
DISABLED_RULES = ('WHITESPACE_RULE,UPPERCASE_SENTENCE_START,EN_QUOTES,'
                   'COMMA_PARENTHESIS_WHITESPACE,EN_UPPER_CASE_NGRAM,'
                   'DETERMINER_GEOGRAPHICAL_WORD')
DISABLED_CATEGORIES = 'TYPOGRAPHY,STYLE,REDUNDANCY,COLLOQUIALISMS,MISC'


def chunk(text, size=9000):
    parts, cur, cur_len = [], [], 0
    for para in text.split('\n\n'):
        if cur_len + len(para) > size and cur:
            parts.append('\n\n'.join(cur))
            cur, cur_len = [], 0
        cur.append(para)
        cur_len += len(para)
    if cur:
        parts.append('\n\n'.join(cur))
    return parts


def check(text):
    data = urllib.parse.urlencode({
        'text': text, 'language': 'en-US',
        'disabledRules': DISABLED_RULES,
        'disabledCategories': DISABLED_CATEGORIES,
    }).encode()
    req = urllib.request.Request('https://api.languagetool.org/v2/check', data=data,
                                  headers={'User-Agent': 'masaladeutsch-language-audit/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def audit_post(slug, sleep_between=3.1):
    post_file = f'{ROOT}/posts/{slug}.html'
    meta_file = f'{ROOT}/meta/{slug}.json'
    try:
        raw = open(post_file, encoding='utf-8', errors='ignore').read()
    except FileNotFoundError:
        return None
    try:
        meta = json.load(open(meta_file))
    except Exception:
        meta = {}
    title = meta.get('title', slug)
    url = meta.get('url', '')

    blocks = extract(raw)
    prose_blocks = [b for b in blocks if ' | ' not in b and len(b) > 3]
    doc = build_document(title, prose_blocks)
    if len(doc) < 80:
        return None

    matches = []
    for ci, c in enumerate(chunk(doc)):
        time.sleep(sleep_between)
        try:
            res = check(c)
        except Exception as e:
            matches.append({'error': str(e)})
            continue
        for m in res.get('matches', []):
            cat = m.get('rule', {}).get('category', {}).get('id', '')
            if cat not in CATEGORIES.split(','):
                continue
            matches.append({
                'chunk': ci,
                'message': m.get('message'),
                'context': m.get('context', {}).get('text'),
                'replacements': [r.get('value') for r in m.get('replacements', [])][:3],
                'rule': m.get('rule', {}).get('id'),
                'category': cat,
            })
    if not matches:
        return None
    return {'slug': slug, 'title': title, 'url': url, 'matches': matches}


def write_post_report(result):
    lines = [f"# Language audit — {result['title']}\n",
             f"*{result['url']}*\n",
             '**This is a report, not an applied fix.** LanguageTool has a high '
             'false-positive rate on this blog\'s prose (chart captions, code '
             'identifiers, valid constructions it misparses) — review each item '
             'before touching the post.\n']
    for m in result['matches']:
        if 'error' in m:
            lines.append(f"- ERROR checking chunk: {m['error']}")
            continue
        lines.append(f"- **[{m['category']}/{m['rule']}]** {m['message']}")
        lines.append(f"  context: {m['context']}")
        if m['replacements']:
            lines.append(f"  suggested: {', '.join(m['replacements'])}")
    path = f"{OUT_DIR}/{result['slug']}.md"
    open(path, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slug', help='audit a single post and print to stdout')
    args = ap.parse_args()
    import os
    os.makedirs(OUT_DIR, exist_ok=True)

    if args.slug:
        result = audit_post(args.slug)
        if not result:
            print(f'{args.slug}: 0 matches')
            return
        print(json.dumps(result, indent=1))
        return

    files = sorted(glob.glob(f'{ROOT}/posts/*.html'))
    flagged = []
    for idx, f in enumerate(files):
        slug = f.rsplit('/', 1)[-1][:-5]
        if slug in SKIP_SLUGS:
            continue
        result = audit_post(slug)
        if result:
            path = write_post_report(result)
            flagged.append(result)
            print(f"[{len(flagged)} flagged / {idx+1}/{len(files)}] {slug}: "
                  f"{len(result['matches'])} matches -> {path}", file=sys.stderr, flush=True)
        else:
            print(f"[{len(flagged)} flagged / {idx+1}/{len(files)}] {slug}: clean",
                  file=sys.stderr, flush=True)

    today = datetime.date.today().strftime('%Y-%m-%d')
    n_checked = len(files) - len(SKIP_SLUGS)
    summary = [f"# Language audit summary — {today}\n",
               f"*{len(flagged)} of {n_checked} posts flagged. "
               "Report-only — nothing was published. Per-post detail in "
               "out/language_audit/<slug>.md.*\n"]
    for r in sorted(flagged, key=lambda r: -len([m for m in r['matches'] if 'error' not in m])):
        n = len([m for m in r['matches'] if 'error' not in m])
        summary.append(f"- [{r['title']}]({r['url']}) — {n} matches — "
                        f"see `{r['slug']}.md`")
    open(f'{OUT_DIR}/_summary_{today}.md', 'w', encoding='utf-8').write('\n'.join(summary) + '\n')
    open(f'{OUT_DIR}/_summary_latest.md', 'w', encoding='utf-8').write('\n'.join(summary) + '\n')
    print(f"\nDONE. {len(flagged)} posts flagged. Summary -> out/language_audit/_summary_{today}.md",
          file=sys.stderr)


if __name__ == '__main__':
    main()

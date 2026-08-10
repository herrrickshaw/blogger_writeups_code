#!/usr/bin/env python3
"""Build a single Markdown summary of every published masaladeutsch post:
title, date, topic labels, and its own standfirst (the human-written
one-paragraph summary every post already carries) -- not a re-summarised
or AI-generated blurb, the actual published lede.
"""
import glob, html, json, re, collections, datetime

ROOT = '/Users/umashankar/masaladeutsch-archive'
OUT_PATH = f'{ROOT}/MASALADEUTSCH_ALL_POSTS_SUMMARY.md'
SKIP_SLUGS = {'article-index-start-here', 'about-author', 'the-masala-deutsch-shop-books-things'}

def get_standfirst(raw):
    m = re.search(r'<p class="standfirst">(.*?)</p>', raw, re.S)
    if not m:
        # fallback: first <p> with real sentence-length text, skipping nav/eyebrow
        for pm in re.finditer(r'<p(?:\s[^>]*)?>(.*?)</p>', raw, re.S):
            text = re.sub(r'<[^>]+>', '', pm.group(1))
            text = html.unescape(text).strip()
            text = re.sub(r'\s+', ' ', text)
            if len(text) > 80 and 'All Articles' not in text:
                return text
        return ''
    text = re.sub(r'<[^>]+>', '', m.group(1))
    text = html.unescape(text).strip()
    return re.sub(r'\s+', ' ', text)

def main():
    posts = []
    for f in glob.glob(f'{ROOT}/meta/*.json'):
        try:
            meta = json.load(open(f))
        except Exception:
            continue
        slug = meta.get('slug', '')
        if slug in SKIP_SLUGS or not meta.get('url'):
            continue
        post_file = f'{ROOT}/posts/{slug}.html'
        try:
            raw = open(post_file, encoding='utf-8', errors='ignore').read()
        except FileNotFoundError:
            continue
        standfirst = get_standfirst(raw)
        posts.append({
            'title': meta.get('title', slug),
            'url': meta['url'],
            'published': meta.get('published', '')[:10],
            'labels': meta.get('labels', []),
            'standfirst': standfirst,
        })

    # de-dup by URL (the local archive has a couple of slug collisions)
    seen_urls = set()
    dedup = []
    for p in posts:
        if p['url'] in seen_urls:
            continue
        seen_urls.add(p['url'])
        dedup.append(p)
    posts = dedup
    posts.sort(key=lambda p: p['published'] or '0000-00-00')

    by_label = collections.defaultdict(list)
    for p in posts:
        labels = p['labels'] or ['Unlabelled']
        for l in labels:
            by_label[l].append(p)

    out = []
    out.append('# Masala Deutsch — All Posts, Summarised\n')
    out.append(f'*{len(posts)} published posts, {len(by_label)} topic labels. '
                'Each entry is the post\'s own published standfirst — not a re-summary.*\n')
    out.append(f'*Generated {datetime.date.today().strftime("%-d %B %Y")} — regenerated daily by tools/update_summary_cron.sh.*\n')

    out.append('\n## By Topic\n')
    for label in sorted(by_label, key=str.lower):
        out.append(f'\n### {label} ({len(by_label[label])})\n')
        for p in sorted(by_label[label], key=lambda p: p['published'] or '', reverse=True):
            out.append(f"- **[{p['title']}]({p['url']})** — {p['published']}"
                        + (f"\n  {p['standfirst']}" if p['standfirst'] else ''))

    out.append('\n\n## Chronological (All Posts)\n')
    for p in posts:
        labels_str = ', '.join(p['labels']) if p['labels'] else '—'
        out.append(f"\n### [{p['title']}]({p['url']})")
        out.append(f"*{p['published']} · {labels_str}*\n")
        out.append(p['standfirst'] or '*(no standfirst found)*')

    text = '\n'.join(out)
    open(OUT_PATH, 'w', encoding='utf-8').write(text)
    print(f'wrote {len(posts)} posts, {len(text)} bytes -> {OUT_PATH}')

if __name__ == '__main__':
    main()

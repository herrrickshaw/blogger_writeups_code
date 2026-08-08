#!/usr/bin/env python3
"""Generate the Shop post from accordion.js — one list, zero drift.

    python3 tools/build_shop.py --accordion <path> --out out/post-shop.html [--publish]

The BOOKS and SHELF arrays in the Pages repo's accordion.js are the single
source of truth for every affiliate placement. This parses them and renders
the Shop page; --publish PUTs it over the existing Shop post (id below),
preserving its publish date and label. Never edit the shop HTML by hand.
"""
import argparse, re, sys, time, html as H
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
TAG = 'herpetithabib-21'
COVER_OVERRIDES = {'B0BXD7LG75': 'https://m.media-amazon.com/images/I/71HNESz07RL._SY522_.jpg'}

def cover(e):
    if not e['asin']:
        return None
    if e['asin'] in COVER_OVERRIDES:
        return COVER_OVERRIDES[e['asin']]
    if e['asin'].startswith('B0'):
        return None   # P/ endpoint serves a 1px placeholder for non-ISBN ASINs
    return f"https://images-na.ssl-images-amazon.com/images/P/{e['asin']}.01._SX120_.jpg"
SHOP_POST_ID = '1964166395488869750'
SCRATCH = Path('/private/tmp/claude-501/-Users-umashankar/e50aaf59-8643-4790-a7e8-d74da5d3e4a2/scratchpad')

def parse_entries(block):
    out = []
    for m in re.finditer(r"\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'"
                         r"(?:\s*,\s*'([A-Z0-9]{10})')?"
                         r"(?:\s*,\s*\n?\s*'(https://m\.media-amazon\.com[^']+)')?\s*\]", block):
        t, by, asin, img = m.groups()
        fix = lambda x: x.encode().decode('unicode_escape') if '\\u' in x else x.replace("\\'", "'")
        out.append({'t': fix(t), 'by': fix(by), 'asin': asin, 'img': img})
    return out

def link(e):
    return (f"https://www.amazon.in/dp/{e['asin']}?tag={TAG}" if e['asin']
            else f"https://www.amazon.in/s?k={quote(e['t'] + ' ' + e['by'])}&tag={TAG}")

def card(e, w=150):
    img = (f'<img src="{e["img"]}" alt="{H.escape(e["t"])}" loading="lazy" '
           f'style="width:{w}px;height:{w}px;object-fit:contain;background:#fff;'
           f'border:1px solid #ececec;border-radius:2px;display:block"/>' if e['img'] else '')
    by = H.escape(e['by'].replace(' Rohit Lamba', ' & Rohit Lamba'))
    return (f'<a href="{link(e)}" rel="nofollow sponsored noopener" target="_blank" '
            f'style="display:block;width:{w}px;text-decoration:none;color:#1a1a1a">{img}'
            f'<span style="display:block;font-size:.78em;line-height:1.35;margin-top:.35rem">{H.escape(e["t"])}</span>'
            f'<span style="display:block;font-size:.7em;color:#595959">{by}</span></a>')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--accordion', default=str(SCRATCH / 'mdsite/accordion.js'))
    ap.add_argument('--out', default='out/post-shop.html')
    ap.add_argument('--publish', action='store_true')
    args = ap.parse_args()

    js = Path(args.accordion).read_text()
    books_block = js[js.index('var BOOKS'):js.index('};', js.index('var BOOKS'))]
    shelf_block = js[js.index('var SHELF'):js.index('];', js.index('var SHELF'))]
    # A topic's value runs to the ']]' that closes its list-of-lists; the old
    # non-greedy match stopped at the first inner ']' and silently dropped
    # every book after the first in multi-book topics.
    topics = {m.group(1): parse_entries(m.group(2) + ']')
              for m in re.finditer(r"'([^']+)':\s*\[(.*?\])\s*\]", books_block, re.S)}
    shelf = parse_entries(shelf_block)
    import datetime
    today = datetime.date.today()
    pretty = today.strftime('%-d %B %Y')

    o = []; A = o.append
    A('<p class="eyebrow">The shop &middot; Books &amp; things from the articles</p>')
    A('<h1>The Masala Deutsch Shop</h1>')
    A('<p class="standfirst">Everything this blog links to on Amazon, in one place: the books '
      'recommended under each topic, and the off-topic things from the author&rsquo;s shelf. Every '
      'link is an affiliate link &mdash; <b>as an Amazon Associate, this site earns from qualifying '
      'purchases</b> &mdash; and nothing here was supplied free or sponsored; each item was chosen '
      'by the author.</p>')
    A(f'<p class="revised">Updated <time datetime="{today.isoformat()}">{pretty}</time> &middot; '
      'generated from the same list that renders the reading blocks on every article, so the two '
      'cannot disagree.</p>')
    A('<h2>From the author&rsquo;s shelf</h2>')
    A('<p class="h2sub">Off-topic, personal, and used at this desk.</p>')
    A('<div style="display:flex;flex-wrap:wrap;gap:1.1rem">')
    for e in shelf: A(card(e))
    A('</div>')
    A('<h2>Reading by topic</h2>')
    A('<p class="h2sub">The books recommended under each topic&rsquo;s articles.</p>')
    seen = set()
    for topic in sorted(topics, key=str.lower):
        fresh = [e for e in topics[topic] if e['t'] not in seen]
        if not fresh: continue
        A(f'<h3 style="font-size:.78em;letter-spacing:.12em;text-transform:uppercase;'
          f'color:#8a4b08;margin:1.4rem 0 .4rem">{H.escape(topic)}</h3>')
        for e in fresh:
            seen.add(e['t'])
            by = H.escape(e['by'].replace(' Rohit Lamba', ' & Rohit Lamba'))
            cv = cover(e)
            th = (f'<img src="{cv}" alt="" loading="lazy" style="width:44px;height:62px;'
                  f'object-fit:contain;background:#fff;border:1px solid #ececec;'
                  f'border-radius:2px;flex-shrink:0"/>' if cv else
                  '<span style="width:44px;flex-shrink:0"></span>')
            A(f'<div style="display:flex;align-items:center;gap:.7rem;margin:.45rem 0">{th}'
              f'<span><a href="{link(e)}" rel="nofollow sponsored noopener" target="_blank">{H.escape(e["t"])}</a> '
              f'<span style="color:#595959;font-size:.85em">&mdash; {by}</span></span></div>')
    A('<div class="note"><b>Disclosure.</b> As an Amazon Associate, this site earns from qualifying '
      'purchases made through the links on this page. Prices and availability are whatever Amazon '
      'shows you &mdash; this page quotes neither, because both change and the Associates rules '
      'prohibit stale price claims. Recommendations are editorial: no item on this page was provided '
      'free, discounted, or in exchange for coverage.</div>')

    body = '\n'.join(o)
    head = (SCRATCH / 'head_gas.html').read_text().replace('artx gasx', 'artx shopx').replace('.gasx', '.shopx')
    tail = (SCRATCH / 'tail2.html').read_text()
    Path(args.out).write_text(head + body + tail, encoding='utf-8')
    print(f"wrote {args.out}: {len(shelf)} shelf items, {len(seen)} topic books")

    if args.publish:
        import blogger_api as B
        p = B.api(f"/blogs/{B.BLOG_ID}/posts/{SHOP_POST_ID}")
        B.api(f"/blogs/{B.BLOG_ID}/posts/{SHOP_POST_ID}",
              data={"id": SHOP_POST_ID, "title": p["title"],
                    "content": Path(args.out).read_text(encoding='utf-8'),
                    "published": p["published"], "labels": p.get("labels") or []},
              method="PUT")
        time.sleep(2)
        q = B.api(f"/blogs/{B.BLOG_ID}/posts/{SHOP_POST_ID}")
        print(f"published | labels {q.get('labels')} | date preserved {q['published'][:19]}")

if __name__ == '__main__':
    main()

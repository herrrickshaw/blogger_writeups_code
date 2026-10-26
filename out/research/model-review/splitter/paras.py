"""List and split post paragraphs, numbered as tools/model_layout_review.py's outline numbers them."""
import re, sys, json, html, pathlib
ROOT = pathlib.Path('/home/user/blogger_writeups_code')
VOID = {'br', 'img', 'hr', 'wbr', 'input', 'meta', 'link', 'source', 'col'}

def paragraphs(s):
    """[(n, start_of_inner, end_of_inner, open_tag)] for each <p> with text, outside script/style/svg/table."""
    out, n = [], 0
    blocked = []
    for m in re.finditer(r'<(/?)(script|style|svg|table|noscript)\b[^>]*>', s, re.I):
        blocked.append((m.start(), m.group(1) == '/', m.group(2).lower()))
    ranges, stack = [], []
    for pos, close, tag in blocked:
        if not close: stack.append((tag, pos))
        else:
            for i in range(len(stack) - 1, -1, -1):
                if stack[i][0] == tag:
                    if i == 0: ranges.append((stack[0][1], pos))
                    del stack[i:]; break
    inside = lambda p: any(a <= p < b for a, b in ranges)
    for m in re.finditer(r'(<p\b[^>]*>)(.*?)</p>', s, re.S | re.I):
        if inside(m.start()): continue
        text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', m.group(2)))).strip()
        if not text: continue
        n += 1
        out.append((n, m.start(2), m.end(2), m.group(1), text))
    return out

def wrapped(inner):
    """The tag name if one inline tag wraps the whole paragraph, else None."""
    m = re.match(r'\s*<(em|i|small|span)\b[^>]*>', inner)
    if m and re.search(rf'</{m.group(1)}>\s*$', inner) and inner.count(f'<{m.group(1)}') == 1:
        return m.group(0).strip(), f'</{m.group(1)}>'
    return None


def boundaries(inner):
    """Offsets in inner HTML where a new sentence (or a bold-labelled group) starts, outside inline tags."""
    START = r'(?:[A-Z0-9“"‘(₹$€£]|&#8377;|&ldquo;|&lsquo;|&#\d+;|<(?:b|strong)>[^<]{1,40}:</(?:b|strong)>)'
    TOK = re.compile(r'<(/?)([a-zA-Z0-9]+)[^>]*?(/?)>'
                     r'|(?P<end>[.?!][’”"\')]*\s+)(?=' + START + ')'
                     r'|(?P<semi>;\s+)(?=<(?:b|strong)>[^<]{1,40}:</(?:b|strong)>)')
    w = wrapped(inner)
    base = 1 if w else 0
    res, depth = [], 0
    for m in TOK.finditer(inner):
        if m.group(2):
            t = m.group(2).lower()
            if t in VOID or m.group(3):
                continue
            depth += -1 if m.group(1) else 1
            continue
        if depth != base:
            continue
        if m.group('end') and re.search(r'\b(?:[A-Z]|vs|no|Rs|Dr|Mr|Ms|St|approx|e\.g|i\.e|cf|Fig|Co|Ltd|Inc|Rev|Vol|pp?)\.$',
                                        inner[max(0, m.start() - 8):m.start() + 1]):
            continue
        res.append(m.end())
    return res


if __name__ == '__main__':
    slug, minw = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 110
    s = (ROOT / 'posts' / f'{slug}.html').read_text(encoding='utf-8')
    for n, a, b, tag, text in paragraphs(s):
        w = len(text.split())
        if w < minw: continue
        inner = s[a:b]; bs = [0] + boundaries(inner)
        print(f'== para {n} ({w} words) {tag[:40]}')
        for k in range(len(bs)):
            seg = inner[bs[k]:bs[k + 1] if k + 1 < len(bs) else len(inner)]
            t = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', seg))).strip()
            print(f'   s{k} [{len(t.split())}w] {t[:150]}')

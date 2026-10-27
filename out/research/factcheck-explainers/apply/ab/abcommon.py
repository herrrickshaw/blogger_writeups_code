"""Helpers for the Group A/B corrections: exact replacements, the house update note, and checks."""
import re, subprocess, pathlib
ROOT = pathlib.Path('/home/user/blogger_writeups_code')
NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);'
        'padding:.8em 1em;margin:1.2em 0;border-radius:4px"><b>Updated 27 October 2026.</b> {}</div>\n')


def load(slug):
    return (ROOT / 'posts' / f'{slug}.html').read_text(encoding='utf-8')


def rep(t, old, new, count=1):
    n = t.count(old)
    assert n == count, f'expected {count} of {old[:90]!r}, found {n}'
    return t.replace(old, new)


def note(t, text):
    h = max(t.find('<h1'), 0)
    i = t.find('<div class="gb-h2"', h)
    if i == -1:
        i = t.find('<h2', h)
    ex = t.find('<div class="warn" style="border-left:4px solid #a5402c', h)
    if ex != -1 and (i == -1 or ex < i):
        i = ex
    assert i != -1 and i >= h
    return t[:i] + NOTE.format(text) + t[i:]


def save(slug, t):
    out = ROOT / 'out' / f'update-2026-10-27-{slug}.html'
    for tag in ['div', 'p', 'table', 'tr', 'td', 'svg', 'ul', 'figure']:
        o = len(re.findall(r'<%s[\s>]' % tag, t)); c = t.count('</%s>' % tag)
        assert o == c, f'{tag} {o} vs {c}'
    out.write_text(t, encoding='utf-8')
    r = subprocess.run(['python3', 'consistency-check/_local_check.py', str(out)], cwd=ROOT, capture_output=True, text=True)
    bad = [l for l in r.stdout.splitlines() if l.strip().startswith('[') and '[OK]' not in l]
    print(out.name, 'checks:', 'OK' if not bad else bad)

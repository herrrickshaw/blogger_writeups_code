#!/usr/bin/env python3
"""Build the complete, upload-ready Blogger theme from a base theme plus module files.

Blogger has no theme API, and pasting fragments into the HTML editor is error-prone.
This keeps the theme in two parts instead:

    theme/base.xml        the live theme with no modules in it (Blogger's own widgets,
                          gadgets and settings, exactly as last backed up)
    theme/modules.json    the list of modules, each a CSS or JS file under templates/

and writes theme/theme.xml = base + every module, inserted at fixed anchors and wrapped
in BEGIN/END markers so the next build can find and replace them.

    python3 tools/theme_build.py                          # rebuild theme/theme.xml from theme/base.xml
    python3 tools/theme_build.py --base ~/Downloads/theme-123.xml
                                                          # use a fresh Blogger backup as the base
                                                          # (modules already in it are removed first,
                                                          # then theme/base.xml is updated)
    python3 tools/theme_build.py --check                  # exit 1 if theme/theme.xml is out of date

Upload theme/theme.xml in Blogger > Theme > (menu next to Customise) > Restore.
Always build from a backup taken the same day, so nothing changed in Blogger since is lost.

Module kinds:
    css    inserted just before ]]></b:skin>
    js     wrapped in <script>//<![CDATA[ ... //]]></script>, inserted just before the final </body>
    scope  "classes": [...]; every theme rule whose selector starts with one of these classes gets
           :not(.post-body *), so theme chrome styles (.hero, .card, ...) stop applying to post
           elements that happen to use the same class name
A module with "retired": true is only removed (from a backup), never inserted; use it when a
module is replaced by a new one.
"""
import argparse
import json
import pathlib
import re
import sys
import xml.dom.minidom

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = ROOT / 'theme' / 'base.xml'
OUT = ROOT / 'theme' / 'theme.xml'
MODULES = ROOT / 'theme' / 'modules.json'
SKIN_END = ']]></b:skin>'


def load_modules():
    mods = json.loads(MODULES.read_text(encoding='utf-8'))
    for m in mods:
        if m['kind'] == 'scope':
            m['body'] = ''
            continue
        body = (ROOT / m['file']).read_text(encoding='utf-8').strip('\n')
        if ']]>' in body:
            sys.exit(f"{m['file']}: contains ']]>', which would end the CDATA section")
        if m['kind'] not in ('css', 'js', 'scope'):
            sys.exit(f"{m['id']}: unknown kind {m['kind']!r}")
        m['body'] = body
    return mods


SCOPE = ':not(.post-body *)'


def scope_skin(theme, classes):
    """Add SCOPE after each listed class that starts a selector, outside comments, in the skin."""
    a = theme.index('<b:skin><![CDATA[') + len('<b:skin><![CDATA[')
    b = theme.index(SKIN_END)
    names = '|'.join(re.escape(c) for c in classes)
    parts = re.split(r'(/\*.*?\*/)', theme[a:b], flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(rf'(^|[{{}},])(\s*)\.({names})(?![\w-])', rf'\1\2.\3{SCOPE}', parts[i])
    return theme[:a] + ''.join(parts) + theme[b:]


def block(m):
    inner = f"/* BEGIN theme-module: {m['id']} */\n{m['body']}\n/* END theme-module: {m['id']} */\n"
    return inner if m['kind'] == 'css' else f"<script>//<![CDATA[\n{inner}//]]></script>\n"


def strip(theme, mods):
    """Remove every module from a theme: marked blocks, and unmarked copies pasted by hand."""
    removed = []
    for m in mods:
        if m['kind'] == 'scope':
            names = '|'.join(re.escape(c) for c in m['classes'])
            theme, n = re.subn(rf'\.({names}){re.escape(SCOPE)}', r'.\1', theme)
            if n:
                removed.append(f"{m['id']} x{n}")
            continue
        mid = re.escape(m['id'])
        marked = (rf"/\* BEGIN theme-module: {mid} \*/\n.*?/\* END theme-module: {mid} \*/\n" if m['kind'] == 'css'
                  else rf"<script>//<!\[CDATA\[\n/\* BEGIN theme-module: {mid} \*/\n.*?//\]\]></script>\n")
        theme, n = re.subn(marked, '', theme, flags=re.S)
        # Hand-pasted copies (THEME_PATCH docs) carry no markers. A CSS copy starts at
        # "/* <id> (" and ends at the module's last line; a JS copy is the whole <script>.
        if m['kind'] == 'css':
            last = m['body'].rstrip().splitlines()[-1]
            while True:
                i = theme.find(f"/* {m['id']} (")
                if i < 0:
                    break
                j = theme.find(last, i)
                if j < 0:
                    sys.exit(f"{m['id']}: found an unmarked copy but not its last line; remove it by hand")
                j += len(last)
                if theme[j:j + 1] == '\n':
                    j += 1
                theme, n = theme[:i] + theme[j:], n + 1
        else:
            pat = rf"<script>//<!\[CDATA\[\s*/\* {mid} \(.*?//\]\]></script>\n?"
            theme, k = re.subn(pat, '', theme, flags=re.S)
            n += k
        if n:
            removed.append(f"{m['id']} x{n}")
    return theme, removed


def build(base, mods):
    if base.count(SKIN_END) != 1:
        sys.exit(f"base theme has {base.count(SKIN_END)} '{SKIN_END}', expected 1")
    body_end = base.rfind('</body>')
    if body_end < 0 or base[body_end + len('</body>'):].strip() != '</html>':
        sys.exit("base theme: the last </body> is not followed by </html>")
    live = [m for m in mods if not m.get('retired')]
    css = ''.join(block(m) for m in live if m['kind'] == 'css')
    js = ''.join(block(m) for m in live if m['kind'] == 'js')
    out = base
    for m in live:
        if m['kind'] == 'scope':
            out = scope_skin(out, m['classes'])
    body_end = out.rfind('</body>')
    out = out[:body_end] + js + out[body_end:]
    i = out.index(SKIN_END)
    out = out[:i] + css + out[i:]
    return out


def verify(out, base, mods):
    try:
        xml.dom.minidom.parseString(out.encode('utf-8'))
    except Exception as e:  # Blogger rejects the save with a SAXParseException on the same faults
        sys.exit(f"built theme is not well-formed XML: {e}")
    for m in mods:
        if m['kind'] == 'scope':
            continue
        c = out.count(f"/* BEGIN theme-module: {m['id']} */")
        if c != (0 if m.get('retired') else 1):
            sys.exit(f"{m['id']}: appears {c} times in the built theme")
    if strip(out, mods)[0] != base:
        sys.exit("built theme is not exactly base + modules (removing the modules does not give back the base)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--base', help='a theme backup downloaded from Blogger; becomes theme/base.xml')
    ap.add_argument('--out', default=str(OUT), help='where to write the built theme (default theme/theme.xml)')
    ap.add_argument('--check', action='store_true', help='only check that the built theme is up to date')
    a = ap.parse_args()
    mods = load_modules()

    if a.base:
        raw = pathlib.Path(a.base).expanduser().read_text(encoding='utf-8')
        base, removed = strip(raw, mods)
        old = BASE.read_text(encoding='utf-8') if BASE.exists() else ''
        print(f"backup: {len(raw):,} chars; modules removed from it: {', '.join(removed) or 'none'}")
        if old and base != old:
            print(f"the live theme has changed since theme/base.xml was saved ({len(old):,} -> {len(base):,} chars); "
                  "those changes are kept")
        BASE.write_text(base, encoding='utf-8')
    else:
        base = BASE.read_text(encoding='utf-8')
        _, removed = strip(base, mods)
        if removed:
            sys.exit(f"theme/base.xml still contains modules ({', '.join(removed)}); rebuild it with --base")

    out = build(base, mods)
    verify(out, base, mods)
    dest = pathlib.Path(a.out).expanduser()
    if a.check:
        ok = dest.exists() and dest.read_text(encoding='utf-8') == out
        print('theme/theme.xml is up to date' if ok else 'theme/theme.xml is out of date: run tools/theme_build.py')
        sys.exit(0 if ok else 1)
    dest.write_text(out, encoding='utf-8')
    print(f"wrote {dest} ({len(out):,} chars): base {len(base):,} + "
          + ', '.join(f"{m['id']} ({m['kind']})" for m in mods if not m.get('retired')))


if __name__ == '__main__':
    main()

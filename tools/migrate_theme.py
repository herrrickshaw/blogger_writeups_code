#!/usr/bin/env python3
"""Point a downloaded Blogger theme at the custom domain.

    python3 tools/migrate_theme.py ~/Downloads/theme-XXXX.xml

Writes <name>-vertistrat.xml next to it and prints every changed line. Blogger has no theme
API, so: Theme > (arrow next to Customise) > Backup to download, run this, then
Theme > Restore and upload the -vertistrat.xml file. Uses the same rewrite rule as
`blogger_api.py migrate-domain`.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from blogger_api import OLD_HOSTS, migrate_links  # noqa: E402

src = pathlib.Path(sys.argv[1]).expanduser()
text = src.read_text(encoding="utf-8")
new = migrate_links(text)
before = sum(text.count(h) for h in OLD_HOSTS)
if new == text:
    sys.exit(f"{src.name}: no old-domain links found; nothing to do")
for a, b in zip(text.splitlines(), new.splitlines()):
    if a != b:
        print("-", a.strip()[:160])
        print("+", b.strip()[:160])
out = src.with_name(src.stem + "-vertistrat.xml")
out.write_text(new, encoding="utf-8")
print(f"\n{before} old-domain references rewritten; upload {out}")

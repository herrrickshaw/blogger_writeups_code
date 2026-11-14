#!/usr/bin/env python3
"""Scaffold a visual-first edition for one post.

    python3 tools/viz_new.py <slug>

Writes out/viz/<slug>/outline.md (the post as headings, paragraphs and pipe-row tables: read this, not the HTML),
out/viz/<slug>/build.py (a skeleton that already assembles the frame) and out/viz/<slug>/derived.json ({}).
Then fill in build.py, run it, and run  python3 tools/viz_verify.py <slug>  until it prints PASS.
See docs/VIZ_LEAF_BRIEF.md and docs/VISUAL_STORY_STYLE.md."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from viz_frame import body_links, outline, split  # noqa: E402

SKELETON = '''"""Visual-first edition of {slug}. Run from the repo root:  python3 out/viz/{slug}/build.py"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from exec_viz import STYLE, bars, flow, insight, line, numbers, sources_block, top_line, waterfall  # noqa: E402,F401
from viz_frame import body_links, split  # noqa: E402

SLUG = "{slug}"
SRC = (ROOT / f"posts/{{SLUG}}.html").read_text(encoding="utf-8")
FR = split(SRC)
OUT = ROOT / f"out/update-2026-11-15-{{SLUG}}.html"

# Numbers computed from the original's numbers go in derived.json ({{"190": "570/3"}}), never typed in silently.

top = top_line([
    # ("big number", " sentence that completes it."),   # 1 to 3 bullets
])

sections = [
    # insight("Headline stating the finding", bars(...) or line(...) or flow(...) or waterfall(...) [+ numbers(...)],
    #         "One sentence: what it means.", "One sentence: what to do.", "anchor"),
]

extras = (
    # collapsed detail: standards, method, caveats the original made, and
    # sources_block(body_links(FR.body)) for every external link in the original body
    sources_block(body_links(FR.body))
)

body = STYLE + top + FR.keep_front + FR.notes + "".join(sections) + extras
OUT.write_text(FR.head + FR.mid + body + "\\n" + FR.tail, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
'''


def main(slug):
    src = (ROOT / f"posts/{slug}.html").read_text(encoding="utf-8")
    fr = split(src)
    if not fr:
        sys.exit(f"{slug}: not a standard frame")
    d = ROOT / f"out/viz/{slug}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "outline.md").write_text(outline(fr.body) + "\n", encoding="utf-8")
    if not (d / "build.py").exists():
        (d / "build.py").write_text(SKELETON.format(slug=slug), encoding="utf-8")
    if not (d / "derived.json").exists():
        (d / "derived.json").write_text("{}\n")
    print(f"out/viz/{slug}/outline.md ({len(outline(fr.body).split()):,} words), build.py, derived.json; {len(body_links(fr.body))} body links to keep")


if __name__ == "__main__":
    main(sys.argv[1])

import runpy
import sys
from pathlib import Path

import pytest

import extract_post as E

ROOT = Path(__file__).resolve().parent.parent


def test_paragraphs_headings_and_whitespace():
    html = "<h1>Title</h1><p>Hello\n   <b>big</b>   world</p><ul><li>a</li><li>b</li></ul>"
    assert E.extract(html) == ["Title", "Hello big world", "a", "b"]


def test_script_style_skipped_with_nesting():
    html = "<p>a</p><script>var x='<p>no</p>'</script><style>p{}</style><noscript>n</noscript><template>t</template><iframe>i</iframe><p>b</p>"
    assert E.extract(html) == ["a", "b"]


def test_consecutive_duplicates_removed_but_not_distant():
    assert E.extract("<p>x</p><p>x</p><p>y</p><p>x</p>") == ["x", "y", "x"]


def test_table_rows_become_pipe_lines_and_empty_cells_dropped():
    html = "<p>before</p><table><tr><th>A</th><th>B</th></tr><tr><td>1</td><td> </td><td>3</td></tr><tr><td></td></tr></table><p>after</p>"
    assert E.extract(html) == ["before", "A | B", "1 | 3", "after"]


def test_text_outside_blocks_is_flushed_at_end_and_blocks_split():
    assert E.extract("loose text") == ["loose text"]
    assert E.extract("a<div>b</div>c") == ["a", "b", "c"]
    assert E.extract("") == []


def test_entities_converted():
    assert E.extract("<p>R&amp;D &#8212; ok</p>") == ["R&D \u2014 ok"]


@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="extract_post.py:19 defines INLINE_BREAK_TAGS={'br'} but never uses it, so words either side of <br> are glued ('oknext')")
def test_br_separates_words():
    assert E.extract("<p>ok<br>next</p>") == ["ok next"]


def test_unbalanced_end_tag_tolerated():
    assert E.extract("<div><p>a</div>b</p>") == ["a", "b"]
    assert E.extract("</p>stray") == ["stray"]


def test_build_document():
    assert E.build_document("  T  ", ["a", "b"]) == "T\n\na\n\nb"
    assert E.build_document("T", []) == "T\n\n"


def test_cli(tmp_path, monkeypatch, capsys):
    f = tmp_path / "p.html"
    f.write_bytes("<h2>Caf\u00e9</h2><p>x</p>".encode("utf-8") + b"\xff")
    monkeypatch.setattr(sys, "argv", ["extract_post.py", "--file", str(f), "--title", "My title"])
    runpy.run_path(str(ROOT / "tools" / "extract_post.py"), run_name="__main__")
    assert capsys.readouterr().out == "My title\n\nCaf\u00e9\n\nx\n"

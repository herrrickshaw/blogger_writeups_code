import pytest

import viz_frame as F

TRANSLATE = '<script src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>\n'
WORDS = "word " * 520


def post(body=None, tail='<div class="gb-related"><a href="https://x">r</a></div><p class="disclaimer" data-gs-ai-disclosure-v1>AI</p>',
         lead=""):
    body = body if body is not None else f"<h2>Intro</h2><p>{WORDS}</p>"
    return ('<html><body><div class="art"><div class="title"><h1>Title</h1><p class="standfirst">Sf</p></div>'
            f'{lead}<a href="#" id="gs-skip-link">skip</a><div class="bar">A</div>{TRANSLATE}{body}{tail}</div></body></html>')


def test_split_standard_frame_parts_concatenate_back():
    html = post()
    f = F.split(html)
    assert f is not None
    assert f.head.endswith("</p>") or "standfirst" in f.head
    assert f.mid.startswith('<a href="#" id="gs-skip-link"') and f.mid.rstrip().endswith("</script>")
    assert f.body.startswith("<h2>Intro</h2>")
    assert f.tail.startswith('<div class="gb-related">')
    assert f.head + f.lead + f.mid + f.body + f.tail == html


def test_split_returns_none_without_h1_translate_or_enough_words():
    assert F.split("<p>nothing</p>") is None
    assert F.split("<h1>T</h1><p>no translate script</p>") is None
    assert F.split(post(body="<p>short body</p>")) is None
    # no clean footer and no disclaimer paragraph
    assert F.split(post(tail="<p>plain</p>")) is None


def test_split_exactly_500_words_boundary():
    ok = F.split(post(body=f"<p>{'w ' * 500}</p>"))
    assert ok is not None
    assert F.split(post(body=f"<p>{'w ' * 499}</p>")) is None


def test_split_tail_choice_skips_related_box_in_middle_of_article():
    body = f'<h2>A</h2><p>{WORDS}</p><div class="gb-related">mid</div><h2>More analysis</h2><p>text</p>'
    f = F.split(post(body=body, tail='<p class="disclaimer" data-gs-ai-disclosure-v1>AI</p>'))
    assert 'class="gb-related">mid' in f.body and f.tail.startswith('<p class="disclaimer"')


def test_split_only_footer_headings_after_related_mark_is_tail():
    body = f"<h2>A</h2><p>{WORDS}</p>"
    tail = '<div class="gb-related">r</div><h2>Sources</h2><p>s</p>'
    f = F.split(post(body=body, tail=tail))
    assert f.tail.startswith('<div class="gb-related">')


def test_split_keeps_pictures_notes_and_lead():
    body = (f'<div class="warn" style="x"><b>Updated 3 May 2026</b> note</div><figure><img src="a.png"><figcaption>c</figcaption></figure>'
            f'<figure><svg></svg></figure><h2>A</h2><p>{WORDS}</p>')
    f = F.split(post(body=body, lead='<figure class="hero">H</figure>'))
    assert f.keep_front.count("<figure") == 1 and "a.png" in f.keep_front and "svg" not in f.keep_front
    assert "Updated 3 May 2026" in f.notes
    assert f.lead == '<figure class="hero">H</figure>'


def test_split_without_skip_link_puts_everything_in_mid():
    html = post().replace('<a href="#" id="gs-skip-link">skip</a>', "")
    f = F.split(html)
    assert f.lead == "" and f.head + f.mid + f.body + f.tail == html


def test_open_containers_and_balance():
    assert F._open_containers("<div><section><p>x</p>") == [("div", "<div>"), ("section", "<section>")]
    assert F._open_containers("<div></div><div>") == [("div", "<div>")]
    assert F._open_containers("<div><div></div>") == [("div", "<div>")]
    assert F._open_containers("<div/>") == []
    assert F._open_containers("<script><div></script><style>div{}</style><DIV>") == [("div", "<DIV>")]
    assert F._open_containers("</div>") == []
    assert F.container_balance("<div><div></div></div>") == 0
    assert F.container_balance("<main><aside>") == 2


def test_bridge_closes_and_opens_to_match_footer():
    assert F._bridge("<div><section>", "<div>") == "</section>"
    assert F._bridge("<div>", "<div><section>") == "<section>"
    assert F._bridge("<div>", "<div>") == ""
    assert F._bridge("<div><section>", "<article>") == "</section></div><article>"


def test_visible_and_numbers_and_text_of():
    assert F.visible("<p>a&nbsp;&amp; b</p><script>x()</script><style>y{}</style><svg><text>chart 5</text></svg>") == "a & b chart 5"
    assert F.text_of is F.visible


def test_numbers_exact():
    assert F.numbers("1,234.50 and 7.0") == {"1234.5", "7"}
    assert F.numbers("-3 and +4") == {"3", "4"}
    assert F.numbers("abc12 and 12.") == {"12"}
    assert F.numbers("3.14") == {"3.14"} and F.numbers("no digits") == set()
    assert F.numbers("a1.5") == set()


def test_outline_markdownish():
    h = ('<h2>Head</h2><p>Para <a href="https://u" class="x">link <b>t</b></a></p><ul><li>one</li><li>two</li></ul>'
         '<table><tr><th>A</th><th>B</th></tr><tr><td>1</td><td>2</td></tr></table>'
         '<svg><text>c1</text><text>c2</text></svg><div class="gb-h2">Sub</div><script>x</script>L1<br/>L2')
    o = F.outline(h)
    assert "## Head" in o and "[link t](https://u)" in o
    assert "\n- one\n- two" in o and "| A | B |" in o and "| 1 | 2 |" in o
    assert "[chart: c1 c2]" in o and "\n\n## Sub" in o and "<script" not in o
    assert "L1\nL2" in o and "\n\n\n" not in o


def test_body_links_dedupe_and_skip_own_domain():
    b = ('<a href="https://a.com/x#frag">A <b>one</b></a><a href="https://a.com/x">dup</a>'
         '<a href="https://blog.vertistratsolution.com/p">own</a><a href="/rel">rel</a><a href="https://b.org/y?q=1">B&amp;C</a>')
    assert F.body_links(b) == [("https://a.com/x", "A one"), ("https://b.org/y?q=1", "B&C")]


def test_tables_extraction_titles_and_filters():
    b = ('<h2>First</h2><table><tr><th>A</th><th>B</th></tr><tr><td>1</td><td> 2 </td></tr><tr><td></td><td></td></tr></table>'
         '<table><tr><td>only</td></tr></table>'
         '<div class="gb-h2">Second</div><table><tr><th>X</th></tr><tr><td>5</td></tr></table><table><tr><td>a</td></tr><tr><td>b</td></tr></table>')
    t = F.tables(b)
    assert [x["id"] for x in t] == ["T1", "T2", "T3"]
    assert t[0] == {"id": "T1", "title": "First", "head": ["A", "B"], "rows": [["1", "2"]]}
    assert t[1]["title"] == "Second" and t[1]["rows"] == [["5"]]
    assert t[2]["title"] == "Second"
    assert F.tables("<table><tr><td>a</td></tr><tr><td>b</td></tr></table>")[0]["title"] == ""


def test_section_helpers():
    b = '<h2>Intro</h2><p>x</p><h2>What would fix this</h2><p>do A</p><p>do B</p><h2>Next</h2><p>n</p>'
    title, inner = F.fixes(b)
    assert title == "What would fix this" and inner == "<p>do A</p><p>do B</p>"
    assert F.fixes("<h2>Other</h2><p>x</p>") is None
    last = F._section("<h2>Sources</h2><p>a</p>", "sources")
    assert last == ("Sources", "<p>a</p>")
    assert F.sources_section("<h2>Sources and caveats</h2><p>s</p><h2>Z</h2>") == ("Sources and caveats", "<p>s</p>")
    assert F.sources_section("<h2>Documents &amp; sources</h2><p>d</p>")[0] == "Documents & sources"
    assert F.sources_section("<h2>Not sources really</h2><p>d</p>") is None


def test_caveat_heading_section_and_inline_paragraph():
    h = '<h2>What this piece could not establish</h2><p>gap</p><h2>Z</h2>'
    assert F.caveat(h) == ("What this piece could not establish", "<p>gap</p>")
    inline = '<p>intro</p><div class="c">Data does not establish causation.</div><p>after</p>'
    assert F.caveat(inline) == ("What this piece could not establish", '<div class="c">Data does not establish causation.</div>')
    assert F.caveat("<p>nothing relevant</p>") is None
    assert F.caveat("bare text that could not establish") is None
    assert F.caveat("<p>this could not establish") is None        # unclosed element


def test_update_notes_and_related_box():
    b = '<p>x</p><div class="n"><b>Updated 5 May 2026</b>: new</div><p><strong>Updated 12 June 2025</strong> more</p><p>Updated May 2026</p>'
    n = F.update_notes(b)
    assert "Updated 5 May 2026" in n and "Updated 12 June 2025" in n and "Updated May 2026" not in n
    assert F.update_notes("<p>none</p>") == ""
    assert F.related_box('x<div class="gb-related"><a>r</a></div>y') == '<div class="gb-related"><a>r</a></div>'
    assert F.related_box("<p>none</p>") == ""

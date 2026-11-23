import json

import pytest

import svg_chart_lint as L


def svg(inner, vb="0 0 200 100"):
    return f'<svg viewBox="{vb}">{inner}</svg>'


def test_text_width_table_and_bold_and_entities():
    assert L.text_width("0", 10, False) == 5.0
    assert L.text_width("i", 10, False) == pytest.approx(2.8)
    assert L.text_width("m", 10, False) == pytest.approx(6.2)
    assert L.text_width(" ", 10, False) == pytest.approx(4.0)
    assert L.text_width("a", 10, False) == pytest.approx(5.2)
    assert L.text_width("0", 10, True) == pytest.approx(5.0 * 1.08)
    assert L.text_width("&amp;&#8212;&#x2014;", 10, False) == pytest.approx(15.6)   # each entity ~ one glyph
    assert L.text_width("", 10, False) == 0


def test_parse_attrs():
    assert L.parse_attrs('x="1" y = "2" data-a="z"') == {"x": "1", "y": "2", "data-a": "z"}


def test_parse_css_classes_merges_blocks():
    html = "<style>.a{font-size:12px;fill:red}</style><style>.a{fill:blue}.b-c{text-anchor:end}</style>"
    c = L.parse_css_classes(html)
    assert c["a"] == {"font-size": "12px", "fill": "blue"}
    assert c["b-c"] == {"text-anchor": "end"}
    assert L.parse_css_classes("<p>none</p>") == {}


def test_resolve_style_priority_class_style_attr():
    css = {"k": {"font-size": "9px", "fill": "red", "font-weight": "700"}}
    attrs = {"class": "k other", "style": "font-size: 10px; fill: green", "font-size": "11px"}
    r = L.resolve_style(attrs, css)
    assert r["font-size"] == "11px" and r["fill"] == "green" and r["font-weight"] == "700"
    assert L.resolve_style({"class": "zzz"}, css) == {}
    assert L.resolve_style({"text-anchor": "end"}, {}) == {"text-anchor": "end"}


@pytest.mark.parametrize("anchor,x0,x1", [("start", 100, 110), ("end", 90, 100), ("middle", 95, 105)])
def test_text_lines_anchors(anchor, x0, x1):
    (lx0, lx1, y, fs, plain), = L.text_lines({"x": "100", "y": "20", "text-anchor": anchor, "font-size": "10"}, "00")
    assert (lx0, lx1, y, fs, plain) == (x0, x1, 20.0, 10.0, "00")


def test_text_lines_default_font_size_and_empty():
    (_, x1, _, fs, _), = L.text_lines({"x": "0", "y": "0"}, "0")
    assert fs == 11.0 and x1 == 5.5
    assert L.text_lines({"x": "0", "y": "0"}, "  <b></b> ") == []
    assert L.text_lines({"x": "0", "y": "0"}, "  ") == []
    (_, _, _, fs2, _), = L.text_lines({"x": "0", "y": "0"}, "x", font_size_default=20)
    assert fs2 == 20.0


def test_text_lines_bold_widens():
    plain = L.text_lines({"x": "0", "y": "0", "font-size": "10"}, "00")[0][1]
    bold = L.text_lines({"x": "0", "y": "0", "font-size": "10", "font-weight": "bold"}, "00")[0][1]
    semi = L.text_lines({"x": "0", "y": "0", "font-size": "10", "font-weight": "600"}, "00")[0][1]
    light = L.text_lines({"x": "0", "y": "0", "font-size": "10", "font-weight": "500"}, "00")[0][1]
    assert plain == light == 10.0 and bold == semi == pytest.approx(10.8)


def test_text_lines_css_class_font_size():
    css = {"big": {"font-size": "20px", "text-anchor": "end"}}
    (x0, x1, *_), = L.text_lines({"x": "100", "y": "0", "class": "big"}, "00", css)
    assert (x0, x1) == (80.0, 100.0)


def test_text_lines_tspans_with_x_are_separate_lines():
    content = '<tspan x="10" dy="0">00</tspan><tspan x="10" dy="12">00</tspan>'
    lines = L.text_lines({"x": "0", "y": "50", "font-size": "10"}, content)
    assert [(l[0], l[1], l[2]) for l in lines] == [(10.0, 20.0, 50.0), (10.0, 20.0, 62.0)]


def test_text_lines_tspan_without_x_is_inline_run():
    content = '00<tspan font-weight="bold">00</tspan>00'
    lines = L.text_lines({"x": "0", "y": "5", "font-size": "10"}, content)
    assert len(lines) == 1
    assert lines[0][1] == pytest.approx(10 + 10 * 1.08 + 10)
    assert lines[0][4] == "000000"


def test_text_lines_tspan_y_attribute_and_first_tspan_without_x():
    content = '<tspan y="30">00</tspan><tspan x="5" y="40">0</tspan>'
    lines = L.text_lines({"x": "7", "y": "1", "font-size": "10"}, content)
    assert [(l[0], l[2]) for l in lines] == [(7.0, 30.0), (5.0, 40.0)]


def test_text_lines_blank_tspan_line_dropped_and_whitespace_text_skipped():
    content = ' <tspan x="1">  </tspan><tspan x="2">00</tspan>'
    lines = L.text_lines({"x": "0", "y": "0", "font-size": "10"}, content)
    assert len(lines) == 1 and lines[0][0] == 2.0


@pytest.mark.parametrize("anchor,x0", [("end", 90.0), ("middle", 95.0)])
def test_text_lines_tspan_anchor(anchor, x0):
    content = '<tspan x="100">00</tspan>'
    (l,) = L.text_lines({"x": "0", "y": "0", "font-size": "10", "text-anchor": anchor}, content)
    assert l[0] == x0


def test_opacity_of():
    assert L._opacity_of({}) == 1.0
    assert L._opacity_of({"opacity": "0.5", "fill-opacity": "0.5"}) == 0.25
    assert L._opacity_of({"style": "opacity: .4"}) == 0.4
    assert L._opacity_of({"opacity": "bad"}) == 1.0


def test_find_rects_filters():
    inner = (
        '<rect x="0" y="0" width="10" height="5" fill="#fff"/>'
        '<rect x="0" y="0" width="10" height="5" fill="none"/>'
        '<rect x="0" y="0" width="10" height="5"/>'
        '<rect x="0" y="0" width="10" height="5" fill="red" transform="rotate(5)"/>'
        '<rect x="0" y="0" width="0" height="5" fill="red"/>'
        '<rect x="0" y="0" width="10" height="-1" fill="red"/>'
        '<rect x="a" y="0" width="10" height="5" fill="red"/>'
        '<rect x="0" y="0" width="10" fill="red"/>'
        '<rect x="1" y="2" width="3" height="4" fill="transparent"/>'
    )
    r = L.find_rects(inner)
    assert len(r) == 1 and r[0][:5] == (0.0, 0.0, 10.0, 5.0, 1.0)


def test_find_charts_viewbox_and_width_fallback():
    html = '<svg viewBox="10 20 100 50"><text/></svg><svg width="300" height="150">x</svg><svg>y</svg><svg width="" height="">z</svg>'
    ch = list(L.find_charts(html))
    assert ch[0][1:5] == (10.0, 110.0, 20.0, 70.0)
    assert ch[1][1:5] == (0.0, 300.0, 0.0, 150.0)
    assert ch[2][1:5] == (0.0, 700.0, 0.0, 400.0)
    assert ch[3][1:5] == (0.0, 700.0, 0.0, 400.0)


def lint(inner, vb=(0, 200, 0, 100), css=None):
    return L.lint_svg(0, vb[0], vb[1], vb[2], vb[3], inner, css)


def test_overflow_right_left_with_tolerance():
    t = '<text x="195" y="10" font-size="10">0000</text>'
    (i,) = lint(t)
    assert i["type"] == "OVERFLOW_RIGHT" and i["overflow_px"] == 15.0 and i["x1"] == 215.0
    # exactly 1px past the edge is tolerated
    assert lint('<text x="191" y="10" font-size="10">00</text>') == []
    assert lint('<text x="190" y="10" font-size="10">00</text>') == []
    (j,) = lint('<text x="5" y="10" font-size="10" text-anchor="end">00</text>')
    assert j["type"] == "OVERFLOW_LEFT" and j["x0"] == -5.0
    assert lint('<text x="9" y="10" font-size="10" text-anchor="end">00</text>') == []     # -1: tolerated
    assert len(lint('<text x="8" y="10" font-size="10" text-anchor="end">00</text>')) == 1  # -2: reported


def test_collision_overlap_threshold_and_vertical_window():
    a = '<text x="10" y="50" font-size="10">0000</text>'
    b = '<text x="20" y="50" font-size="10">0000</text>'
    (c,) = lint(a + b)
    assert c["type"] == "COLLISION" and c["overlap_px"] == 10.0 and c["y"] == 50.0
    # touching/overlap of exactly 1px is not reported
    assert lint('<text x="10" y="50" font-size="10">0000</text><text x="29" y="50" font-size="10">0000</text>') == []
    # 2px overlap is
    assert len(lint('<text x="10" y="50" font-size="10">0000</text><text x="28" y="50" font-size="10">0000</text>')) == 1
    # baselines 6px apart (== 0.6*10) still collide; 7px does not
    assert len(lint('<text x="10" y="50" font-size="10">0000</text><text x="20" y="56" font-size="10">0000</text>')) == 1
    assert lint('<text x="10" y="50" font-size="10">0000</text><text x="20" y="57" font-size="10">0000</text>') == []


def test_skips_rotated_and_positionless_text():
    assert lint('<text x="500" y="10" transform="rotate(-90)">00000</text>') == []
    assert lint('<text y="10">0000000000000000000000000</text>') == []
    assert lint('<text x="1000">0</text>') == []


def test_text_hidden_by_later_opaque_rect():
    inner = '<text x="10" y="20" font-size="10">0000</text><rect x="15" y="10" width="50" height="12" fill="#333"/>'
    (i,) = lint(inner)
    assert i["type"] == "TEXT_HIDDEN_BY_RECT" and i["overlap_px"] == 15.0
    # earlier rect does not hide
    assert lint('<rect x="15" y="10" width="50" height="12" fill="#333"/><text x="10" y="20" font-size="10">0000</text>') == []
    # translucent rect does not hide; 0.85 does
    assert lint('<text x="10" y="20" font-size="10">0000</text><rect x="15" y="10" width="50" height="12" fill="#333" opacity="0.84"/>') == []
    assert len(lint('<text x="10" y="20" font-size="10">0000</text><rect x="15" y="10" width="50" height="12" fill="#333" opacity="0.85"/>')) == 1
    # sliver overlap (<=3px) ignored, 4px reported
    assert lint('<text x="10" y="20" font-size="10">0000</text><rect x="27" y="10" width="50" height="12" fill="#333"/>') == []
    assert len(lint('<text x="10" y="20" font-size="10">0000</text><rect x="26" y="10" width="50" height="12" fill="#333"/>')) == 1
    # vertically disjoint rect
    assert lint('<text x="10" y="20" font-size="10">0000</text><rect x="15" y="40" width="50" height="12" fill="#333"/>') == []


def test_double_escaped_entities():
    assert L.find_double_escaped_entities("a &amp;mdash; b &amp;#8212; c &amp;#x2014; &amp;nbsp;") == [
        "&amp;mdash;", "&amp;#8212;", "&amp;#x2014;", "&amp;nbsp;"]
    assert L.find_double_escaped_entities("DGCI&amp;S; chapter &amp;bogus; &mdash;") == []


def write(tmp_path, html, name="p.html"):
    p = tmp_path / name
    p.write_text(html, encoding="utf-8")
    return str(p)


def test_lint_file_reports_charts_and_entities(tmp_path):
    html = ("<style>.s{font-size:10px}</style>" + svg('<text class="s" x="195" y="10">0000</text>') +
            svg('<text x="1" y="1">0</text>') + "<p>&amp;mdash; &amp;mdash;</p>")
    res = L.lint_file(write(tmp_path, html))
    assert len(res) == 2
    assert res[0]["viewBox"] == [0.0, 0.0, 200.0, 100.0]
    assert res[0]["issues"][0]["type"] == "OVERFLOW_RIGHT"
    assert res[1]["viewBox"] is None
    assert res[1]["issues"] == [{"type": "DOUBLE_ESCAPED_ENTITY", "text": "&amp;mdash;", "count": 2}]


def test_lint_file_clean(tmp_path):
    assert L.lint_file(write(tmp_path, svg('<text x="1" y="1">0</text>'))) == []


def run_main(monkeypatch, argv):
    monkeypatch.setattr(L.sys, "argv", ["svg_chart_lint.py"] + argv)
    L.main()


def test_main_prints_each_issue_kind_and_json(tmp_path, monkeypatch, capsys):
    html = svg(
        '<text x="10" y="50" font-size="10">0000</text><text x="20" y="50" font-size="10">0000</text>'
        '<text x="195" y="90" font-size="10">0000</text>'
        '<text x="10" y="70" font-size="10">0000</text><rect x="15" y="62" width="50" height="12" fill="#333"/>'
    ) + "&amp;mdash;"
    f = write(tmp_path, html)
    out_json = tmp_path / "r.json"
    run_main(monkeypatch, [f, "--json", str(out_json)])
    out = capsys.readouterr().out
    assert "COLLISION  \"0000\"  overlaps  \"0000\"  (10.0px, y=50.0)" in out
    assert "OVERFLOW-RIGHT" in out and "by 15.0px past canvas edge" in out
    assert "TEXT-HIDDEN-BY-RECT" in out and "DOUBLE-ESCAPED-ENTITY  \"&amp;mdash;\"" in out and "x1" in out
    assert "1 file(s) with issues, 4 issue(s) total, out of 1 scanned." in out
    data = json.loads(out_json.read_text())
    assert list(data) == [f]


def test_main_overflow_left_label_and_min_overflow(tmp_path, monkeypatch, capsys):
    f = write(tmp_path, svg('<text x="5" y="10" font-size="10" text-anchor="end">00</text>'))
    run_main(monkeypatch, [f])
    assert "OVERFLOW-LEFT" in capsys.readouterr().out
    g = write(tmp_path, svg('<text x="190" y="10" font-size="10">000</text>'), "g.html")   # overflow_px == 5
    run_main(monkeypatch, [g, "--min-overflow", "5"])
    assert "1 file(s) with issues" in capsys.readouterr().out
    run_main(monkeypatch, [g, "--min-overflow", "5.1"])
    assert "0 file(s) with issues" in capsys.readouterr().out
    run_main(monkeypatch, [g])      # default 2
    assert "1 file(s)" in capsys.readouterr().out


def test_main_default_scans_posts_glob_and_reports_parse_errors(tmp_path, monkeypatch, capsys):
    (tmp_path / "posts").mkdir()
    (tmp_path / "posts" / "bad.html").write_text('<svg viewBox="a b c d"><text x="1" y="1">0</text></svg>')
    (tmp_path / "posts" / "ok.html").write_text(svg('<text x="1" y="1">0</text>'))
    monkeypatch.chdir(tmp_path)
    run_main(monkeypatch, [])
    cap = capsys.readouterr()
    assert "posts/bad.html: parse error" in cap.err
    assert "0 file(s) with issues, 0 issue(s) total, out of 2 scanned." in cap.out

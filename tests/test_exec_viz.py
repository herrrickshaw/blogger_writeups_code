import re

import pytest

import exec_viz as X


def widths(html):
    return [float(w) for w in re.findall(r'class="xv-b[^"]*" style="width:([\d.]+)%', html)]


@pytest.mark.parametrize("v,unit,want", [
    (5, "", "5"), (1234567, "", "1,234,567"), (4.5, "", "4.5"), (4.123, "", "4.12"), (4.10, "", "4.1"),
    (0.004, "", "0"), (3.0, "", "3"), (-5, "", "-5"), (-1234.5, "", "-1,234.5"),
    (4.21, "$/kg", "$4.21/kg"), (58711, "₹ crore", "₹58,711 crore"), (5, "₹", "₹5"),
    (7, "€", "€7"), (7, "£ bn", "£7 bn"),
    (419, "USD/t", "419 USD/t"), (3, "mmscmd", "3 mmscmd"), (12, "%", "12%"), (-2.5, "%", "-2.5%"), (3, " ", "3 "),
])
def test_fmt(v, unit, want):
    assert X._fmt(v, unit) == want


def test_title_limit_counts_unescaped_chars():
    X._title("a" * 90)
    with pytest.raises(ValueError, match="over 90"):
        X._title("a" * 91)
    X._title("&amp;" * 90)                    # 90 characters once unescaped
    with pytest.raises(ValueError):
        X._title("&amp;" * 91)


def test_top_line_bounds_and_markup():
    h = X.top_line([("5%", "grew."), ("7", "units.")], eyebrow="Key")
    assert h.startswith('<div class="xv-top"><p class="xv-eb">Key</p>')
    assert '<li><span class="xv-k">5%</span>grew.</li>' in h and h.count("<li>") == 2
    assert X.top_line([("1", "a")] * 3).count("<li>") == 3
    for bad in ([], [("1", "a")] * 4):
        with pytest.raises(ValueError, match="at most 3"):
            X.top_line(bad)


def test_bars_widths_scale_to_max_and_accent():
    h = X.bars("Title", [("A", 50), ("B", 100), ("C", 25)], unit="%", accent="B")
    assert widths(h) == [50.0, 100.0, 25.0]
    assert h.count("xv-hi") == 1 and 'xv-r xv-hi" title="B: 100%"' in h
    assert '<b class="xv-v">100%</b>' in h
    h2 = X.bars("T", [("A", 5), ("B", 10)], accent=["A", "B"])
    assert h2.count('xv-r xv-hi') == 2


def test_bars_min_width_vmax_and_zero_row():
    h = X.bars("T", [("A", 0), ("B", 1000), ("C", 1)])
    assert widths(h)[0] == 0.6 and widths(h)[2] == 0.6
    h = X.bars("T", [("A", 50)], vmax=200)
    assert widths(h) == [25.0]


def test_bars_none_value_and_shown_and_note_and_custom_fmt():
    h = X.bars("T", [("A", None), ("B", 5, "est.", "$5.0 bn")], unit="x")
    assert "xv-none" in h and '<b class="xv-v">none</b>' in h and "A: none" in h
    assert "B <small>est.</small>" in h and '<b class="xv-v">$5.0 bn</b>' in h
    h2 = X.bars("T", [("A", None, "", "n/a"), ("B", 1)])
    assert '<b class="xv-v">n/a</b>' in h2
    h3 = X.bars("T", [("A", 5)], fmt=lambda v: f"<{v}>")
    assert '<b class="xv-v"><5></b>' in h3


def test_bars_ref_marker_and_key():
    h = X.bars("T", [("A", 40), ("B", 80)], ref=(100, "Target 100"))
    assert '<p class="xv-key"><i></i>Target 100</p>' in h
    assert h.count('class="xv-m" style="left:40.00%"') == 0
    assert h.count('<i class="xv-m" style="left:100.00%"') == 2
    assert widths(h) == [40.0, 80.0]          # ref participates in the max: bars scale to 100


def test_bars_ranges_floating_and_from_zero():
    h = X.bars("T", [("A", (20, 60)), ("B", (50, 100))], unit="₹ crore")
    assert 'xv-float" style="margin-left:20.00%;width:40.00%"' in h
    assert 'margin-left:50.00%;width:50.00%' in h
    assert "₹20&ndash;₹100 crore" in h or "₹50&ndash;" in h
    assert "A: ₹20 crore to ₹60 crore" in h
    z = X.bars("T", [("A", (20, 100))], from_zero=True, accent="A")
    assert "width:100.00%" in z and "linear-gradient(90deg,#2251FF 20.0%,#2251FF55 20.0%)" in z
    z2 = X.bars("T", [("A", (20, 100))], from_zero=True)
    assert f"{X.GREY} 20.0%" in z2
    z3 = X.bars("T", [("A", (0, 0)), ("B", (5, 10))], from_zero=True)
    assert "100.0%" in z3                      # zero high end: whole bar solid


def test_bars_negative_values_zero_line():
    h = X.bars("T", [("up", 50), ("down", -50)])
    assert 'xv-tk xv-div' in h and h.count('class="xv-m" style="left:50.00%"') == 2
    assert 'class="xv-b" style="left:50.00%;width:50.00%;border-radius:0 4px 4px 0"' in h
    assert 'class="xv-b xv-neg" style="left:0.00%;width:50.00%;border-radius:4px 0 0 4px"' in h
    assert "-50" in h
    h2 = X.bars("T", [("a", -10), ("b", -20)])      # all negative: zero at the right edge
    assert 'style="left:100.00%"' in h2
    h3 = X.bars("T", [("a", -1000), ("b", 1)])
    assert 'width:0.60%' in h3                       # tiny bar floor


@pytest.mark.xfail(strict=True, raises=ValueError,
                   reason="exec_viz.py:141 max() of an empty list when no row has a value, although None rows are documented as 'no value' tracks")
def test_bars_with_only_missing_values_renders():
    assert "xv-none" in X.bars("T", [("A", None)])


def test_bars_tip_is_unescaped_then_escaped():
    h = X.bars("T", [("R&amp;D", 5)])
    assert 'title="R&amp;D: 5"' in h and 'title="R&amp;amp;D' not in h


def test_figure_ids_unique_and_aria_linked():
    a, b = X.bars("T", [("A", 1)]), X.bars("T", [("A", 1)])
    ia = re.search(r'aria-labelledby="(xv\d+)"', a).group(1)
    ib = re.search(r'aria-labelledby="(xv\d+)"', b).group(1)
    assert ia != ib and f'id="{ia}"' in a
    s = X.bars("T", [("A", 1)], sub="sub", source="Src")
    assert '<span class="xv-u">sub</span>' in s and '<p class="xv-s">Src</p>' in s
    assert "xv-u" not in a.split("</style>")[-1] and 'class="xv-s"' not in a


def test_bars_title_too_long_raises():
    with pytest.raises(ValueError):
        X.bars("x" * 91, [("A", 1)])


def test_waterfall_end_is_computed_and_accent_default():
    h = X.waterfall("T", ("Start", 100), [("Up", 30), ("Down", -50)], "End", unit="bn")
    assert '<b class="xv-v">80 bn</b>' in h                       # 100 + 30 - 50
    assert "+30 bn" in h and "&minus;50 bn" in h
    assert 'xv-r xv-hi" title="End: 80 bn"' in h and h.count("xv-hi") == 1
    assert "margin-left:100.00%" not in h
    assert "background:#7d8a96" in h and h.count("background:#7d8a96") == 1
    assert 'margin-left:76.92%' in h or 'margin-left:100.00%' not in h
    h2 = X.waterfall("T", ("Start", 100), [("Up", 30)], "End", accent="Up")
    assert 'xv-r xv-hi" title="Up: +30"' in h2 and h2.count("xv-hi") == 1
    h3 = X.waterfall("T", ("Start", 100), [], "End", accent="Start")
    assert 'xv-r xv-hi" title="Start: 100"' in h3


def test_waterfall_scale_uses_peak():
    h = X.waterfall("T", ("S", 100), [("Up", 100)], "E")
    # peak 200: start bar 50%, step floats from 50% with width 50%, end 100%
    assert "width:50.00%" in h and "margin-left:50.00%;width:50.00%" in h and "width:100.00%" in h


def test_us_and_lv_helpers():
    assert X._us("") == "" and X._us("%") == "%" and X._us("tonnes") == " tonnes"
    assert X._lv("5", "₹ lakh crore") == "₹5 lakh crore"
    assert X._lv("5", "$/kg") == "$5/kg"
    assert X._lv("5", "bn") == "5 bn" and X._lv("5", "%") == "5%"


def test_line_two_drawings_legend_and_accent():
    s = {"India": [(2010, 1), (2020, 5)], "Brazil": [(2010, 2), (2020, 4)]}
    h = X.line("T", s, accent="India", unit="%")
    assert h.count("<svg") == 2 and 'viewBox="0 0 360 230"' in h and 'viewBox="0 0 640 260"' in h
    assert 'class="xv-svg xv-narrow"' in h and 'class="xv-svg xv-wide"' in h
    assert 'aria-hidden="false"' in h and 'aria-hidden="true"' in h
    assert '<p class="xv-leg">' in h and f'<i style="background:{X.ACCENT}"></i>India' in h
    assert f'<i style="background:{X.GREY}"></i>Brazil' in h
    assert h.index("Brazil") < h.rindex("India")                    # accent drawn last (on top)
    assert 'font-weight="800"' in h and "India 5%" in h and "Brazil 4%" in h
    assert "2010" in h and "2020" in h


def test_line_single_series_has_no_legend_or_name_label():
    h = X.line("T", {"Only": [(1, 10), (2, 20)]}, unit="tonnes")
    assert "xv-leg" not in h.split("</style>")[-1]
    assert ">20 tonnes<" in h and "Only 20" not in h
    assert "<title>Only: 10 to 20 tonnes</title>" in h


def test_line_end_labels_do_not_collide():
    s = {"A": [(0, 10), (1, 10)], "B": [(0, 10), (1, 10.1)], "C": [(0, 10), (1, 10.2)]}
    h = X.line("T", s)
    ys = sorted(float(y) for y in re.findall(r'<text x="[\d.]+" y="([\d.]+)" font-size="13" fill="#0B1F2D"', h.split('xv-wide')[0]))
    assert len(ys) == 3 and all(b - a >= 15 - 1e-6 for a, b in zip(ys, ys[1:]))


def test_line_custom_yfmt_and_flat_series():
    h = X.line("T", {"A": [(1, 5), (1, 5)]}, yfmt=lambda v: f"<{v:.0f}>")
    assert "&lt;" not in h and "<5>" in h
    X.line("T", {"A": [(1, 0), (2, 0)]})            # all-zero must not divide by zero


def test_flow_and_numbers():
    f = X.flow([("2020", "a"), ("2021", "b", True), ("2022", "c", False)])
    assert f.count('class="xv-hi"') == 1 and "<li class=\"xv-hi\"><b>2021</b>b</li>" in f
    n = X.numbers(["H1", "H2"], [(1, 2), (3, 4)], summary="Open")
    assert "<summary>Open</summary>" in n and "<th>H1</th><th>H2</th>" in n and n.count("<tr>") == 3
    assert "<td>3</td><td>4</td>" in n


def test_insight_validation_and_markup():
    c = "<figure/>"
    h = X.insight("Head", c, "It means this.", "Do that.", anchor="a1")
    assert '<h2 class="gb-h2" id="a1">Head</h2>' in h and "<figure/>" in h
    assert "<b>What it means:</b> It means this.</p>" in h and "<b>What to do:</b> Do that.</p>" in h
    assert 'id=' not in X.insight("Head", c, "A.", "B.").split("<h2")[1].split(">")[0]
    for means, todo in (("Two. Sentences.", "ok."), ("no stop", "ok."), ("ok.", "a. b."), ("ok.", "no stop"), ("ok.", "")):
        with pytest.raises(ValueError, match="one sentence"):
            X.insight("Head", c, means, todo)
    X.insight("Head", c, "Uses a.b decimal 3.5 fine.", "ok.")              # ". " only counts with a space
    X.insight("Head", c, "  Padded.  ", "ok.")
    with pytest.raises(ValueError, match="over 90"):
        X.insight("x" * 91, c, "a.", "b.")


def test_sources_block():
    assert X.sources_block([]) == ""
    h = X.sources_block([("https://a/?x=1&amp;y=2", "A &amp; B"), ("https://b", "")], summary="Refs")
    assert '<summary>Refs</summary>' in h
    assert '<a href="https://a/?x=1&amp;y=2">A &amp; B</a>' in h
    assert '<a href="https://b">https://b</a>' in h


def test_style_block_tokens():
    assert X.STYLE.startswith("<style>") and X.STYLE.rstrip().endswith("</style>")
    assert X.ACCENT in X.STYLE and X.INK in X.STYLE

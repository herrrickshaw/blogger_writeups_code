"""Extra branch coverage for svg_label_fit, units_in_header and table_standard."""
import json
import sys

import pytest

import svg_label_fit as S
import table_standard as T
import units_in_header as U


# ------------------------------------------------------------ svg_label_fit
LBL_W = 3 * 0.5 * 11 * 1.08   # "100" at 11px bold = 17.82


def test_text_width_bold_flag():
    assert S.text_width("100", 11) == pytest.approx(LBL_W)
    assert S.text_width("100", 11, bold=False) == pytest.approx(16.5)
    assert S.text_width("&amp;", 10, bold=False) == pytest.approx(5.2)


def test_wrap_text_lines_greedy_and_long_word():
    assert S.wrap_text_lines("aa bb cc", 1000, 10) == ["aa bb cc"]
    w = S.text_width("0000 0000", 10, False)
    assert S.wrap_text_lines("0000 0000", w, 10) == ["0000 0000"]          # equal width fits
    assert S.wrap_text_lines("0000 0000", w - 0.01, 10) == ["0000", "0000"]
    assert S.wrap_text_lines("0000000000 00", 5, 10) == ["0000000000", "00"]    # oversize word kept whole
    assert S.wrap_text_lines("", 10, 10) == []
    # bold is wider
    assert S.wrap_text_lines("0000 0000", w, 10, bold=True) == ["0000", "0000"]


def test_wrap_svg_text_structure():
    svg, n = S.wrap_svg_text(50, 20, "0000 0000 0000", S.text_width("0000 0000", 10, False), 10, anchor="start")
    assert n == 2
    assert svg.startswith('<text x="50" y="20" text-anchor="start" font-size="10">')
    assert '<tspan x="50" dy="0">0000 0000</tspan><tspan x="50" dy="12.5">0000</tspan>' in svg
    svg2, _ = S.wrap_svg_text(1, 2, "a b", 0, 10, line_height=20)
    assert 'dy="20"' in svg2 and 'text-anchor="middle"' in svg2


def test_fit_right_outside_inside_and_boundaries():
    # outside: just enough room for label + pad (tiny epsilon dodges float fuzz)
    r = S.fit_value_label("100", 0, 50, 0, 50 + LBL_W + 6.001, "right")
    assert r == {"x": 56, "anchor": "start", "font_size": 11.0, "inside": False}
    # just short of enough room -> moves inside (bar wide enough)
    r = S.fit_value_label("100", 0, 50, 0, 50 + LBL_W + 5.999, "right")
    assert r["inside"] and r["anchor"] == "end" and r["x"] == 46 and r["font_size"] == 11.0
    # inside boundary: bar_w == label + 2*pad
    r = S.fit_value_label("100", 0, LBL_W + 8, 0, LBL_W + 8, "right")
    assert r["inside"] and r["font_size"] == 11.0
    r = S.fit_value_label("100", 0, LBL_W + 7.9, 0, LBL_W + 7.9, "right")
    assert r["inside"] and r["font_size"] < 11.0


def test_fit_right_shrinks_outside_when_more_room_outside():
    # bar 10 wide, 15 outside: neither fits -> shrink to outside space
    r = S.fit_value_label("100", 0, 10, 0, 25, "right")
    assert r["inside"] is False and r["anchor"] == "start" and r["x"] == 16
    assert r["font_size"] == round(11 * (15 - 6) / LBL_W, 1) or r["font_size"] == 8.0
    r = S.fit_value_label("100", 0, 10, 0, 28, "right")        # 18 outside: (18-6)/17.82*11 = 7.4 -> clamped to 8
    assert r["font_size"] == 8.0
    r = S.fit_value_label("100", 0, 10, 0, 30.5, "right")      # 20.5 outside: still not enough? 20.5 < 23.82
    assert r["inside"] is False and S.MIN_FONT_SIZE <= r["font_size"] < 11.0


def test_fit_right_shrinks_inside_when_bar_larger_than_outside():
    r = S.fit_value_label("100", 0, 22, 0, 27, "right")        # outside 5 < bar 22; inside needs 25.82
    assert r["inside"] and r["anchor"] == "end" and r["x"] == 18
    assert r["font_size"] == round(11 * (22 - 8) / LBL_W, 1) == 8.6
    r = S.fit_value_label("100", 0, 9, 0, 9, "right")          # tiny bar: clamp at minimum
    assert r["font_size"] == 8.0


def test_fit_left_mirrors_right():
    r = S.fit_value_label("100", 100, 150, 0, 200, "left")
    assert r == {"x": 94, "anchor": "end", "font_size": 11.0, "inside": False}
    r = S.fit_value_label("100", 10, 60, 0, 200, "left")     # outside 10 < 23.8, bar 50 fits inside
    assert r == {"x": 14, "anchor": "start", "font_size": 11.0, "inside": True}
    r = S.fit_value_label("100", 10, 20, 0, 200, "left")     # bar 10, outside 10 -> outside >= bar -> shrink outside
    assert r["inside"] is False and r["anchor"] == "end" and r["x"] == 4 and r["font_size"] == 8.0
    r = S.fit_value_label("100", 20, 40, 0, 200, "left")      # bar 20 > outside 20? equal -> outside branch (>=)
    assert r["inside"] is False
    r = S.fit_value_label("100", 20, 41, 0, 200, "left")      # bar 21 > outside 20 -> inside shrink
    assert r["inside"] is True and r["anchor"] == "start" and r["x"] == 24
    assert r["font_size"] == round(11 * (21 - 8) / LBL_W, 1)


def test_fit_custom_padding_and_size():
    r = S.fit_value_label("100", 0, 50, 0, 500, "right", font_size=20, pad_outside=2)
    assert r["x"] == 52 and r["font_size"] == 20


# --------------------------------------------------------- units_in_header
def tb(head, cells, extra=""):
    rows = "".join(f"<tr><td>r{i}</td><td>{c}</td></tr>" for i, c in enumerate(cells))
    return f"<tr><th>Item</th><th>{head}</th></tr>{rows}{extra}"


def test_audit_too_few_rows_and_values():
    assert U.audit_table("<tr><td>x</td></tr>") == ([], 0)
    assert U.audit_table(tb("V", ["5 cr", "6 cr"]))[0] == []         # only two values
    assert len(U.audit_table(tb("V", ["5 cr", "6 cr", "7 cr"]))[0]) == 1


def test_audit_skips_dashes_prose_and_non_numeric_columns():
    assert U.audit_table(tb("V", ["5 cr", "—", "-", "–", "n/a", "6 cr"]))[0] == []   # only 2 real values
    prose = ["₹5 crore for the long project overall", "₹6 crore for the second long project", "₹7 crore for yet another project"]
    assert U.audit_table(tb("V", prose))[0] == []                    # median > 4 words
    four = ["a b c d 5 cr"] * 3                                         # 5 words -> prose
    assert U.audit_table(tb("V", four))[0] == []
    ok4 = ["a b c 5 cr"] * 3                                            # 5 words, still >4
    assert U.audit_table(tb("V", ok4))[0] == []
    fine = ["a b c 5"] * 3
    assert U.audit_table(tb("V", fine))[0] == []                        # no unit at all
    # numericish below 80%
    assert U.audit_table(tb("V", ["5 cr", "6 cr", "7 cr", "x cr", "y cr"]))[0] == []
    # exactly 80% numeric is enough
    assert len(U.audit_table(tb("V", ["5 cr", "6 cr", "7 cr", "8 cr", "x cr"]))[0]) == 1


def test_audit_unit_share_threshold_and_header_already_has_unit():
    half = ["5 cr", "6 cr", "7", "8"]
    assert len(U.audit_table(tb("V", half))[0]) == 1                    # exactly 50%
    assert U.audit_table(tb("V", ["5 cr", "6", "7", "8"]))[0] == []     # 25%
    assert U.audit_table(tb("Value, cr", ["5 cr", "6 cr", "7 cr"]))[0] == []
    (c, head, unit, hits, total), = U.audit_table(tb("Value", ["5 cr", "6 cr", "7 cr"]))[0]
    assert (c, head, unit, hits, total) == (1, "Value", "cr", 3, 3)


def test_audit_headerless_table_and_head_truncation():
    cells = "".join(f"<tr><td>r{i}</td><td>{c}</td></tr>" for i, c in enumerate(["5 cr", "6 cr", "7 cr"]))
    (v,), n = U.audit_table(cells)
    assert v[1] == "" and n == 3
    long_head = "H" * 50
    (v,), _ = U.audit_table(tb(long_head, ["5 cr", "6 cr", "7 cr"]))
    assert len(v[1]) == 36


def test_units_main_clean_dirty_json_and_empty(tmp_path, monkeypatch, capsys):
    dirty = tmp_path / "d.html"
    dirty.write_text("<table>" + tb("Value", ["5 cr", "6 cr", "7 cr"]) + "</table><table>" + tb("A, cr", ["1", "2", "3"]) + "</table>")
    clean = tmp_path / "c.html"
    clean.write_text("<table>" + tb("A, cr", ["1", "2", "3"]) + "</table>")
    j = tmp_path / "o.json"
    monkeypatch.setattr(sys, "argv", ["u", "--file", str(dirty), "--json", str(j)])
    assert U.main() == 1
    out = capsys.readouterr().out
    assert "files 1  tables 2  tables with a repeated unit 1" in out and "violations 1" in out
    assert "[Value]  'cr' in 3/3 cells (100%)" in out
    assert json.loads(j.read_text())[0]["share"] == 1.0
    monkeypatch.setattr(sys, "argv", ["u", "--file", str(clean)])
    assert U.main() == 0
    capsys.readouterr()
    monkeypatch.setattr(U, "ROOT", tmp_path)       # no posts/ dir -> nothing to audit
    monkeypatch.setattr(sys, "argv", ["u"])
    assert U.main() == 2
    assert "nothing to audit" in capsys.readouterr().err


def test_units_main_sorts_by_share_and_shows_no_header(tmp_path, monkeypatch, capsys):
    (tmp_path / "posts").mkdir()
    rows = lambda cells: "".join(f"<tr><td>r{i}</td><td>{c}</td></tr>" for i, c in enumerate(cells))
    (tmp_path / "posts" / "a.html").write_text(
        "<table>" + rows(["5 cr", "6 cr", "7", "8"]) + "</table><table>" + rows(["5 cr", "6 cr", "7 cr"]) + "</table>")
    monkeypatch.setattr(U, "ROOT", tmp_path)
    monkeypatch.setattr(sys, "argv", ["u"])
    assert U.main() == 1
    out = capsys.readouterr().out
    assert out.index("(100%)") < out.index("(50%)") and "[no header]" in out


# ----------------------------------------------------------- table_standard
def test_strip_unit_edge_cases():
    assert T.strip_unit("", {"%"}) == (None, None)
    assert T.strip_unit("%", {"%"}) == (None, None)               # nothing left
    assert T.strip_unit("5,", {"%"}) == ("5", "")                 # trailing comma stripped
    assert T.strip_unit("US$ 5 bn", {"us$", "bn"}) == ("5", "")   # case-insensitive removal
    assert T.strip_unit("5 per qtl", {"qtl"})[0] is None
    assert T.strip_unit("(1.2)%", {"%"}) == ("(1.2)", "")
    assert T.strip_unit("≈5%", {"%"}) == ("≈5", "")
    assert T.strip_unit("5 – 7%", {"%"}) == ("5 – 7", "")
    assert T.strip_unit("₹ 2 / qtl.", {"₹"}) == ("2", "/qtl.")


def test_label_and_pretty():
    assert T._label({"cr", "₹"}) == "₹ crore"
    assert T._label({"$", "bn"}) == "US$ bn"
    assert T._label({"%"}) == "%"
    assert T._label({"₹", "qtl"}, "/qtl") == "₹/qtl"
    assert T._pretty("MMT") == "MMT" and T._pretty("tonnes") == "tonnes" and T._pretty("zzz") == "zzz"
    assert T._pretty("&#8377;") == "₹" and T._pretty("gwh") == "GWh"


def test_hoist_skips_empty_dash_cells_and_cells_without_the_unit():
    src = tb("V", ["5 cr", "—", "n/a", "&mdash;", "6 cr", "7 cr", ""])
    new, moved, refused = T.hoist(src)
    assert moved == [("V", "crore", 3)] and refused == []
    assert new.count("<td>—</td>") == 1 and "<th>V, crore</th>" in new


def test_hoist_does_not_duplicate_unit_already_in_header_text():
    src = tb("Value (crore)", ["5 cr", "6 cr", "7 cr"])
    new, moved, _ = T.hoist(src)
    assert "<th>Value (crore)</th>" in new and moved


def test_hoist_mixed_per_denominators_left_alone():
    src = tb("Price", ["₹2,369/qtl", "₹100/kg", "₹5/qtl"])
    new, moved, refused = T.hoist(src)
    assert new == src and moved == []


def test_hoist_no_rows_returns_unchanged():
    assert T.hoist("<td>x</td>") == ("<td>x</td>", [], [])


def test_hoist_header_row_not_modified_when_headerless():
    cells = "".join(f"<tr><td>r{i}</td><td>{c}</td></tr>" for i, c in enumerate(["5 cr", "6 cr", "7 cr"]))
    new, moved, _ = T.hoist(cells)
    assert moved and "<td>5</td>" in new


def test_process_refuses_when_prose_changes(tmp_path, monkeypatch):
    f = tmp_path / "p.html"
    f.write_text("<style>a{}</style><p>hi</p>")
    monkeypatch.setattr(T, "hoist", lambda h: (h, [], []))
    monkeypatch.setattr(T, "ensure_style", lambda d: (d.replace("hi", "bye"), True))
    out, moved, refused, note = T.process(f, write_to=tmp_path / "o.html")
    assert out is None and note.startswith("REFUSED") and not (tmp_path / "o.html").exists()


def test_process_no_write_and_style_already_present(tmp_path):
    f = tmp_path / "p.html"
    f.write_text("<style>/*gs-table-v1*/</style><table>" + tb("S", ["1%", "2%", "3%"]) + "</table>")
    out, moved, refused, note = T.process(f)
    assert note == "style already present" and len(moved) == 1 and "S, %" in out


def test_visible_helpers():
    assert T._visible("<p>a &amp; b</p><script>x</script> <style>y</style>") == "a & b"
    assert T._visible_nontable("<p>a</p><table><tr><td>x</td></tr></table><p>b</p>") == "a TABLE b"


def _site(tmp_path):
    f = tmp_path / "a.html"
    f.write_text("<style>p{}</style><p>t</p><table>" + tb("Share", ["1%", "2%", "3%"]) + "</table>")
    g = tmp_path / "b.html"
    g.write_text("<style>p{}</style><p>t</p><table>" + tb("Q", ["about 5%", "6%", "7%"]) + "</table>")
    return f, g


def test_main_report_only_does_not_write(tmp_path, monkeypatch, capsys):
    f, _ = _site(tmp_path)
    monkeypatch.setattr(sys, "argv", ["t", "--file", str(f)])
    assert T.main() == 0
    out = capsys.readouterr().out
    assert "moved  1  refused  0  styled" in out and "+ [Share] '%' -> header (3 cells)" in out
    assert "posts changed 1 | units hoisted 1 | cells refused 0" in out
    assert "<td>1%</td>" in f.read_text()


def test_main_out_writes_and_refused_cells_listed(tmp_path, monkeypatch, capsys):
    f, g = _site(tmp_path)
    o = tmp_path / "o.html"
    monkeypatch.setattr(sys, "argv", ["t", "--file", str(g), "--out", str(o)])
    T.main()
    out = capsys.readouterr().out
    assert "refused  1" in out and "! [Q] '%' left alone, cell was 'about 5%'" in out and "posts changed 0" in out
    assert o.exists()


def test_main_outdir_requires_write_flag(tmp_path, monkeypatch, capsys):
    f, _ = _site(tmp_path)
    od = tmp_path / "od"
    monkeypatch.setattr(sys, "argv", ["t", "--file", str(f), "--outdir", str(od)])
    T.main()
    assert od.is_dir() and not (od / "a.html").exists()
    monkeypatch.setattr(sys, "argv", ["t", "--file", str(f), "--outdir", str(od), "--write"])
    T.main()
    assert "Share, %" in (od / "a.html").read_text()


def test_main_prints_refusal_note_when_guard_trips(tmp_path, monkeypatch, capsys):
    f, _ = _site(tmp_path)
    monkeypatch.setattr(T, "process", lambda path, dest=None: (None, [], [], "REFUSED: non-table text changed"))
    monkeypatch.setattr(sys, "argv", ["t", "--file", str(f)])
    T.main()
    assert "REFUSED: non-table text changed" in capsys.readouterr().out


def test_main_default_glob_over_posts(tmp_path, monkeypatch, capsys):
    (tmp_path / "posts").mkdir()
    _site(tmp_path / "posts")
    monkeypatch.setattr(T, "ROOT", tmp_path)
    monkeypatch.setattr(sys, "argv", ["t"])
    T.main()
    assert "posts changed 1" in capsys.readouterr().out

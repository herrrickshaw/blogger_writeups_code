import json
import runpy
import sys
from pathlib import Path

import pytest

import viz_render as R
from test_viz_frame import post, WORDS


# ------------------------------------------------------------------ helpers
@pytest.mark.parametrize("cell,want", [
    ("12", 12.0), ("1,234.5 bn", 1234.5), ("about 7%", 7.0), ("-3", -3.0), ("−3.5", -3.5), ("–5", 5.0),
    ("a -4 b", -4.0), ("no number", None), ("", None), ("1,2,3", 123.0), ("US$ 14.18", 14.18), ("3.", 3.0),
])
def test_num(cell, want):
    assert R.num(cell) == want


def test_pick_rows_forms():
    assert R.pick_rows({"rows": [2, 5]}, 10) == [2, 5]
    assert R.pick_rows({}, 20) == list(range(10))                 # default 0-9
    assert R.pick_rows({}, 4) == [0, 1, 2, 3]
    assert R.pick_rows({"rows": "2-4"}, 10) == [2, 3, 4]
    assert R.pick_rows({"rows": "2-40"}, 5) == [2, 3, 4]
    assert R.pick_rows({"rows": "top:3"}, 10) == [0, 1, 2]
    assert R.pick_rows({"rows": "top:30"}, 4) == [0, 1, 2, 3]
    with pytest.raises(ValueError, match="table rows must be"):
        R.pick_rows({"rows": "bogus"}, 5)


T = {"T1": {"id": "T1", "title": "t", "head": ["Country", "Limit", "Note"],
            "rows": [["India", "5 mg/kg", "n1"], ["Brazil", "1.5 mg/kg", "n&2"], ["EU", "1 mg/kg", "n3"]]}}


def test_rows_from_table_values_escape_and_sort():
    spec = {"id": "T1", "label": 0, "value": 1, "note": 2}
    assert R.rows_from_table(spec, T) == [("India", 5.0, "n1", "5 mg/kg"), ("Brazil", 1.5, "n&amp;2", "1.5 mg/kg"), ("EU", 1.0, "n3", "1 mg/kg")]
    desc = R.rows_from_table({**spec, "sort": "asc"}, T)
    assert [r[0] for r in desc] == ["EU", "Brazil", "India"]
    desc = R.rows_from_table({**spec, "sort": "desc"}, T)
    assert [r[0] for r in desc] == ["India", "Brazil", "EU"]
    no_note = R.rows_from_table({"id": "T1", "label": 0, "value": 1, "rows": [0]}, T)
    assert no_note == [("India", 5.0, "", "5 mg/kg")]
    assert [r[0] for r in R.rows_from_table({"id": "T1", "label": 0, "value": 1, "rows": "1-2", "sort": None}, T)] == ["Brazil", "EU"]


def test_rows_from_table_errors():
    with pytest.raises(ValueError, match="no table T9 in the original"):
        R.rows_from_table({"id": "T9", "label": 0, "value": 1}, T)
    mixed = {"T2": {"rows": [["a", "5 mg"], ["b", "6 %"]]}}
    with pytest.raises(ValueError, match="mixes units"):
        R.rows_from_table({"id": "T2", "label": 0, "value": 1}, mixed)
    nonum = {"T3": {"rows": [["a", "n/a"], ["b", "n/a"]]}}
    with pytest.raises(ValueError, match="has no number"):
        R.rows_from_table({"id": "T3", "label": 0, "value": 1}, nonum)


def test_rows_from_table_same_unit_with_approx_markers_is_allowed():
    t = {"T": {"rows": [["a", "~5 mg"], ["b", "about 6 mg"], ["c", "7 mg (est)"]]}}
    assert [r[1] for r in R.rows_from_table({"id": "T", "label": 0, "value": 1}, t)] == [5.0, 6.0, 7.0]


def test_chart_dispatch_all_types():
    b = R.chart({"type": "bars", "title": "T", "rows": [["A", 5, "n", "5%"], ["B", [1, 2]], ["C", None]], "accent": ["A"],
                 "ref": [3, "marker"], "unit": "%", "from_zero": True, "vmax": 10}, {})
    assert "xv-key" in b and "marker" in b and "xv-none" in b
    tb = R.chart({"type": "bars", "title": "T", "table": {"id": "T1", "label": 0, "value": 1}, "accent": "India"}, T)
    assert "India" in tb and "5 mg/kg" in tb
    ln = R.chart({"type": "line", "title": "T", "series": {"A": [[1, 1.5], [2, 3]]}, "accent": "A", "unit": "%", "sub": "s", "source": "src"}, {})
    assert "<svg" in ln and ">3%<" in ln.replace(" ", "") or "3%" in ln
    wf = R.chart({"type": "waterfall", "title": "T", "start": ["S", 10], "steps": [["Up", 5]], "end": "E", "unit": "x"}, {})
    assert "15" in wf
    fl = R.chart({"type": "flow", "events": [["a", "b", True]]}, {})
    assert '<ol class="xv-flow">' in fl
    with pytest.raises(ValueError, match="unknown chart type"):
        R.chart({"type": "pie"}, {})


def test_numbers_block_from_table_and_typed():
    h = R.numbers_block({"table": "T1", "summary": "Open"}, T)
    assert "<summary>Open</summary>" in h and "<th>Country</th>" in h and "n&amp;2" in h
    t = R.numbers_block({"head": ["a"], "rows": [[1]]}, T)
    assert "<summary>Show the numbers</summary>" in t and "<td>1</td>" in t


# --------------------------------------------------------------------- lint
def section(**kw):
    s = {"h2": "Finding about 5 percent", "chart": {"type": "bars", "title": "Brazil caps it at 1.5 mg/kg",
         "rows": [["A", 1], ["B", 2]], "accent": "A"}, "means": "It means this.", "todo": "Do that."}
    s.update(kw)
    return s


def spec(**kw):
    s = {"top": [["5%", " of x."]], "sections": [section(), section(), section()]}
    s.update(kw)
    return s


def test_lint_clean_spec():
    assert R.lint(spec()) == []


def test_lint_top_and_section_counts():
    assert any("top: needs 1 to 3" in e for e in R.lint(spec(top=[])))
    assert any("top: needs 1 to 3" in e for e in R.lint(spec(top=[["1", "a"]] * 4)))
    assert R.lint(spec(top=[["1", "a"]] * 3)) == []
    e = R.lint(spec(top=[["", "x"], ["only"]]))
    assert any("top[1]" in x for x in e) and any("top[2]" in x for x in e)
    for n in (2, 5):
        assert any(f"need 3 or 4, have {n}" in x for x in R.lint(spec(sections=[section()] * n)))
    assert R.lint(spec(sections=[section()] * 4)) == []


def test_lint_h2_and_chart_title_lengths_and_finding():
    e = R.lint(spec(sections=[section(h2=""), section(h2="x" * 91), section()]))
    assert sum("h2 is" in x for x in e) == 2
    assert not any("h2 is" in x for x in R.lint(spec(sections=[section(h2="x" * 90)] * 3)))
    long_t = section(chart={"type": "bars", "title": "x" * 91, "rows": [["A", 1], ["B", 2]], "accent": "A"})
    assert any("chart title is 91" in x for x in R.lint(spec(sections=[long_t] * 3)))
    nofind = section(chart={"type": "bars", "title": "Chloride limits", "rows": [["A", 1], ["B", 2]], "accent": "A"})
    assert any("does not state a finding" in x for x in R.lint(spec(sections=[nofind] * 3)))
    seven = section(chart={"type": "bars", "title": "One two three four five six seven", "rows": [["A", 1], ["B", 2]], "accent": "A"})
    assert R.lint(spec(sections=[seven] * 3)) == []
    six = section(chart={"type": "bars", "title": "One two three four five six", "rows": [["A", 1], ["B", 2]], "accent": "A"})
    assert any("does not state a finding" in x for x in R.lint(spec(sections=[six] * 3)))
    empty = section(chart={"type": "bars", "title": "", "rows": [["A", 1], ["B", 2]], "accent": "A"})
    assert any("chart title is 0" in x for x in R.lint(spec(sections=[empty] * 3)))


def test_lint_flow_charts_skip_title_rules():
    f = section(chart={"type": "flow", "events": [["a", "b"]]})
    assert R.lint(spec(sections=[f] * 3)) == []


def test_lint_bar_count_and_accent():
    def bars(n, **kw):
        c = {"type": "bars", "title": "Brazil caps it at 1.5 mg/kg", "rows": [["A", i] for i in range(n)], "accent": "A"}
        c.update(kw)
        return section(chart=c)
    assert any("has 1 bars" in x for x in R.lint(spec(sections=[bars(1)] * 3)))
    assert any("has 15 bars" in x for x in R.lint(spec(sections=[bars(15)] * 3)))
    assert R.lint(spec(sections=[bars(2)] * 3)) == [] and R.lint(spec(sections=[bars(14)] * 3)) == []
    assert any("no 'accent'" in x for x in R.lint(spec(sections=[bars(3, accent=None)] * 3)))
    tbl = lambda r: section(chart={"type": "bars", "title": "Brazil caps it at 1.5 mg/kg", "accent": "A", "table": {"id": "T1", "rows": r}})
    assert any("has 1 bars" in x for x in R.lint(spec(sections=[tbl("top:1")] * 3)))
    assert any("has 20 bars" in x for x in R.lint(spec(sections=[tbl("top:20")] * 3)))
    assert R.lint(spec(sections=[tbl("top:5")] * 3)) == []
    assert any("has 1 bars" in x for x in R.lint(spec(sections=[tbl([0])] * 3)))
    assert R.lint(spec(sections=[tbl("0-9")] * 3)) == []        # unknowable count: not flagged


def test_lint_line_rules():
    def ln(series, accent="A"):
        return section(chart={"type": "line", "title": "Brazil caps it at 1.5 mg/kg", "series": series, "accent": accent})
    ok = {"A": [[1, 1], [2, 2], [3, 3], [4, 4]]}
    assert R.lint(spec(sections=[ln(ok)] * 3)) == []
    assert any("no 'accent' series" in x for x in R.lint(spec(sections=[ln(ok, None)] * 3)))
    assert any("under 4 points" in x for x in R.lint(spec(sections=[ln({"A": [[1, 1], [2, 2], [3, 3]]})] * 3)))
    big = {"A": [[1, 1], [2, 1], [3, 1], [4, 1]], "B": [[1, 20], [2, 20], [3, 20], [4, 20]]}
    assert R.lint(spec(sections=[ln(big)] * 3)) == []                     # exactly 20x is allowed
    big["B"] = [[1, 21], [2, 21], [3, 21], [4, 21]]
    assert any("very different size" in x for x in R.lint(spec(sections=[ln(big)] * 3)))
    neg = {"A": [[1, -1], [2, -1], [3, -1], [4, -1]], "B": [[1, -50], [2, 1], [3, 1], [4, 1]]}
    assert any("very different size" in x for x in R.lint(spec(sections=[ln(neg)] * 3)))


@pytest.mark.parametrize("text,ok", [
    ("One sentence.", True), ("No stop", False), ("Two. Sentences here.", False), ("Fine, with 3.5 decimals.", True),
    ("Lower. case after is ok.", True), ("<b>Tagged</b> one.", True), ("&amp; entity.", True), ("", False), ("Ends with question?", False),
])
def test_lint_one_sentence(text, ok):
    errs = R.lint(spec(sections=[section(means=text)] * 3))
    assert (not any("'means' must be" in e for e in errs)) is ok
    errs = R.lint(spec(sections=[section(todo=text)] * 3))
    assert (not any("'todo' must be" in e for e in errs)) is ok


# -------------------------------------------------------------------- build
@pytest.fixture
def site(tmp_path, monkeypatch):
    monkeypatch.setattr(R, "ROOT", tmp_path)
    monkeypatch.setattr(R.sys, "argv", ["viz_render.py", "slug"])
    (tmp_path / "posts").mkdir()
    body = (f'<h2>Intro</h2><p>{WORDS}</p><h2>Limits</h2><table><tr><th>Country</th><th>Limit</th></tr>'
            '<tr><td>India</td><td>5 mg/kg</td></tr><tr><td>Brazil</td><td>1.5 mg/kg</td></tr><tr><td>EU</td><td>1 mg/kg</td></tr></table>'
            '<h2>What would fix this</h2><p>Fix it.</p>'
            '<p>This could not establish causation.</p>'
            '<p>See <a href="https://src.example/doc">the doc</a>.</p>'
            '<div class="warn"><b>Updated 3 May 2026</b>: x</div>')
    (tmp_path / "posts" / "slug.html").write_text(post(body=body), encoding="utf-8")
    d = tmp_path / "out" / "viz" / "slug"
    d.mkdir(parents=True)

    def write(sp):
        (d / "spec.json").write_text(json.dumps(sp), encoding="utf-8")
    return tmp_path, d, write


def good_spec(**kw):
    tbl = {"type": "bars", "title": "India allows 5 mg/kg, five times the EU limit", "accent": "India",
           "table": {"id": "T1", "label": 0, "value": 1, "rows": "top:3", "sort": "desc"}}
    s = {"top": [["5x", " the EU limit."]], "derived": {"5": "5/1"},
         "sections": [{"h2": "India is loosest", "chart": tbl, "means": "It means this.", "todo": "Do that.",
                       "numbers": {"table": "T1"}, "anchor": "a1"},
                      {"h2": "Trend", "chart": {"type": "line", "title": "The value rose from 1 to 4 over four years",
                       "series": {"A": [[1, 1], [2, 2], [3, 3], [4, 4]]}, "accent": "A"}, "means": "Up.", "todo": "Watch."},
                      {"h2": "Timeline", "chart": {"type": "flow", "events": [["2020", "start"], ["2021", "end", True]]},
                       "means": "A.", "todo": "B."}]}
    s.update(kw)
    return s


def test_build_writes_edition_and_derived(site):
    root, d, write = site
    write(good_spec(update_notes=["<p>Updated 5 June 2026: new fact.</p>"], details=[{"summary": "More", "html": "<p>m</p>"}]))
    out = R.build("slug")
    assert out == d / "edition.html"
    h = out.read_text(encoding="utf-8")
    assert h.index("xv-top") < h.index('class="xv-sec"') < h.index("Sources cited")
    assert '<h2 class="gb-h2" id="a1">India is loosest</h2>' in h
    assert '<h2 class="gb-h2" id="fixes">What would fix this</h2>' in h and "<p>Fix it.</p>" in h
    assert "<summary>What this piece could not establish</summary>" in h or "could not establish" in h
    assert "Table: Limits" in h and '<div class="xv-upd"><p>Updated 5 June 2026: new fact.</p></div>' in h
    assert "<summary>More</summary><p>m</p>" in h
    assert "Updated 15 November 2026:</b> rewritten as charts" in h
    assert 'href="https://src.example/doc"' in h and "Updated 3 May 2026" in h
    assert h.count("<h1>") == 1 and h.rstrip().endswith("</html>")
    assert json.loads((d / "derived.json").read_text()) == {"5": "5/1"}


def test_build_fixes_drop_and_tables_none_or_list(site):
    root, d, write = site
    write(good_spec(fixes="drop", tables="none"))
    h = R.build("slug").read_text(encoding="utf-8")
    assert 'id="fixes"' not in h and "Table: Limits" not in h
    write(good_spec(tables=["T9"]))
    assert "Table: Limits" not in R.build("slug").read_text(encoding="utf-8")
    write(good_spec(tables=["T1"]))
    assert "Table: Limits" in R.build("slug").read_text(encoding="utf-8")


def test_build_refuses_verified_without_force_and_overwrites_with_force(site, monkeypatch):
    root, d, write = site
    write(good_spec())
    (d / ".verified").write_text("")
    with pytest.raises(SystemExit, match="already has a verified edition"):
        R.build("slug")
    monkeypatch.setattr(R.sys, "argv", ["viz_render.py", "slug", "--force"])
    assert R.build("slug").exists()


def test_build_exits_on_empty_spec_nonstandard_frame_and_lint(site):
    root, d, write = site
    write({"top": [], "sections": []})
    with pytest.raises(SystemExit, match="no 'top' bullets"):
        R.build("slug")
    write(good_spec())
    (root / "posts" / "slug.html").write_text("<p>not a frame</p>")
    with pytest.raises(SystemExit, match="standard frame"):
        R.build("slug")
    (root / "posts" / "slug.html").write_text(post())
    write(good_spec(sections=[good_spec()["sections"][0]] * 2))
    with pytest.raises(SystemExit, match="all problems at once"):
        R.build("slug")


def test_main_entry_reports_spec_errors_and_success(site, tmp_path, capsys, monkeypatch):
    """Run the __main__ block from a copy of the script so its ROOT is a scratch tree."""
    root, d, write = site
    tools = root / "tools"
    tools.mkdir()
    (tools / "viz_render.py").write_text(Path(R.__file__).read_text(encoding="utf-8"), encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["viz_render.py", "slug"])
    bad = good_spec()
    bad["sections"][0]["chart"]["table"]["id"] = "T9"
    write(bad)
    with pytest.raises(SystemExit) as e:
        runpy.run_path(str(tools / "viz_render.py"), run_name="__main__")
    assert str(e.value.code).startswith("spec error: ValueError: no table T9")
    write(good_spec())
    runpy.run_path(str(tools / "viz_render.py"), run_name="__main__")
    assert capsys.readouterr().out.strip() == "wrote out/viz/slug/edition.html"

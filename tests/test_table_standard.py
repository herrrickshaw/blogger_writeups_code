"""tools/table_standard.py hoist/strip_unit/process on synthetic HTML."""
import table_standard as t


def tbl(head, cells):
    rows = "".join(f"<tr><td>r{i}</td><td>{c}</td></tr>" for i, c in enumerate(cells))
    return f"<tr><th>Item</th><th>{head}</th></tr>{rows}"


def test_strip_unit_cases():
    assert t.strip_unit("₹9,743 cr", {"₹", "cr"}) == ("9,743", "")
    assert t.strip_unit("-30% to -40%", {"%"}) == ("-30 to -40", "")
    assert t.strip_unit("~5.3%", {"%"}) == ("~5.3", "")
    assert t.strip_unit("₹2,369/qtl", {"₹"}) == ("2,369", "/qtl")
    assert t.strip_unit("about $2bn, mostly gas", {"$", "bn"}) == (None, None)


def test_hoist_moves_unit_to_header_and_bares_cells():
    new, moved, refused = t.hoist(tbl("Share", ["12%", "5%", "7%"]))
    assert refused == [] and moved == [("Share", "%", 3)]
    assert "<th>Share, %</th>" in new
    assert "<td>12</td>" in new and "%</td>" not in new


def test_hoist_refuses_whole_column_if_one_cell_is_not_numeric():
    src = tbl("Value", ["$5 bn", "$6 bn", "about $2bn, mostly gas"])
    new, moved, refused = t.hoist(src)
    assert new == src and moved == []
    assert refused and refused[0][2] == "about $2bn, mostly gas"


def test_hoist_noop_on_clean_table():
    src = tbl("Share, %", ["12", "5", "7"])
    assert t.hoist(src) == (src, [], [])


def test_header_label_keeps_unit_casing():
    new, moved, _ = t.hoist(tbl("Value", ["US$ 14.18 bn", "US$ 2 bn", "US$ 3.5 bn"]))
    assert "<th>Value, US$ bn</th>" in new, new[:80]


def test_header_label_puts_currency_before_magnitude():
    new, _, _ = t.hoist(tbl("Outlay", ["₹1,200 crore", "₹300 crore", "₹45 crore"]))
    assert "<th>Outlay, ₹ crore</th>" in new, new[:80]


def test_header_label_does_not_repeat_per_unit():
    new, _, _ = t.hoist(tbl("Price", ["₹2,369/qtl", "₹2,100/qtl", "₹1,950/qtl"]))
    assert "<th>Price, ₹/qtl</th>" in new, new[:80]
    assert "<td>2,369</td>" in new


def test_ensure_style_once():
    doc, added = t.ensure_style("<style>a{}</style><p>x</p>")
    assert added and t.MARKER in doc and doc.index(t.MARKER) < doc.index("</style>")
    assert t.ensure_style(doc) == (doc, False)
    assert t.ensure_style("<p>no style</p>") == ("<p>no style</p>", False)


def test_process_changes_only_tables(tmp_path):
    src = tmp_path / "post.html"
    out = tmp_path / "out.html"
    src.write_text("<style>p{}</style><p>Intro 12% text</p><table>"
                   + tbl("Share", ["12%", "5%", "7%"]) + "</table>", encoding="utf-8")
    doc, moved, refused, note = t.process(src, write_to=out)
    assert note == "styled" and len(moved) == 1
    assert "<p>Intro 12% text</p>" in doc        # prose untouched
    assert out.read_text(encoding="utf-8") == doc

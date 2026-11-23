import json
import re

import pytest

import build_index_page as I


# -------------------------------------------------------------- date helpers
@pytest.mark.parametrize("iso,want", [
    ("2026-10-25T10:00:00Z", "25 October 2026"), ("2026-01-01", "1 January 2026"), ("2026-12-31T23:59", "31 December 2026"),
    ("", "?"), (None, "?"), ("2026-1-1", "?"), ("2026-02-3", "?"),
])
def test_pretty_date(iso, want):
    assert I._pretty_date(iso) == want


def test_pretty_date_requires_ten_chars():
    assert I._pretty_date("2026-02-03") == "3 February 2026"
    assert I._pretty_date("2026-02-0") == "?"


def test_weekday_date_and_pretty_month():
    assert I._weekday_date("2026-10-25") == "Sunday 25 October 2026"
    assert I._weekday_date("2026-01-01T00:00") == "Thursday 1 January 2026"
    assert I._pretty_month("2026-03") == "March 2026" and I._pretty_month("2026-12-31") == "December 2026"
    with pytest.raises(ValueError):
        I._weekday_date("2026-02-30")


def test_label_hubs_and_pitch_themes_consistent():
    names = [n for n, _ in I.LABEL_HUBS]
    assert len(names) == len(set(names)) == 17
    assert set(I.PITCH_THEMES) <= set(names)
    for n, slug in I.LABEL_HUBS:
        assert " " not in slug and slug.replace("%20", " ").replace("%26", "&") == n


# --------------------------------------------------------------------- text
@pytest.fixture
def root(tmp_path, monkeypatch):
    monkeypatch.setattr(I, "ROOT", tmp_path)
    (tmp_path / "posts").mkdir()
    (tmp_path / "meta").mkdir()
    return tmp_path


def add_post(root, slug, html):
    (root / "posts" / f"{slug}.html").write_text(html, encoding="utf-8")


def test_post_text_heads_and_body(root):
    add_post(root, "a", "<script>var Hidden</script><h2>Steel <b>Tariffs</b></h2><caption>Table One</caption><p>Body Text &amp; more</p><h4>skip</h4>")
    heads, body = I._post_text("a")
    assert "steel" in heads and "tariffs" in heads and "table one" in heads and "skip" not in heads
    assert "body text & more" in body and "hidden" not in body
    assert I._post_text("missing") == ("", "")


def test_build_keywords_tfidf_and_filters(root):
    add_post(root, "a", "<h2>Zirconium</h2><p>" + "zirconium " * 5 + "common " * 3 + "the 12345678 code 123 and 1234567</p>")
    add_post(root, "b", "<p>" + "common " * 3 + "ethanol " * 4 + "this that with</p>")
    add_post(root, "c", "<p>common words here common</p>")
    kw = I.build_keywords(["a", "b", "c"])
    assert "zirconium" in kw["a"].split() and "ethanol" in kw["b"].split()
    assert "common" not in kw["a"].split()                    # appears in all 3 posts: df >= half, scored out
    assert "12345678" in kw["a"].split() and "1234567" in kw["a"].split() and "123" not in kw["a"].split()
    assert "this" not in kw["b"].split() and "that" not in kw["b"].split()              # stop words
    assert kw["a"].split()[0] == "zirconium"                                              # heading words come first
    assert len(kw["a"].split()) == len(set(kw["a"].split()))


def test_build_keywords_top_limit_and_empty(root):
    add_post(root, "a", "<p>" + " ".join(f"word{i:02d}x" for i in range(60)) + "</p>")
    add_post(root, "b", "<p>other text entirely different</p>")
    add_post(root, "c", "<p>nothing alike either</p>")
    assert len(I.build_keywords(["a", "b", "c"], top=5)["a"].split()) == 5
    assert I.build_keywords([]) == {}
    assert I.build_keywords(["missing"]) == {"missing": ""}


def test_load_labels_by_slug(root):
    (root / "meta" / "a.json").write_text(json.dumps({"slug": "a", "labels": ["X", "Y"]}))
    (root / "meta" / "b.json").write_text(json.dumps({"slug": "b"}))
    (root / "meta" / "c.json").write_text(json.dumps({"labels": ["Z"]}))
    (root / "meta" / "d.json").write_text("{broken")
    assert I.load_labels_by_slug() == {"a": ["X", "Y"], "b": []}


# --------------------------------------------------------------- emitters
def test_emit_pitch_cards_for_every_theme_with_hub_links():
    out = []
    I.emit_pitch(out.append)
    h = "\n".join(out)
    assert h.count('class="gs-tcard"') == len(I.PITCH_THEMES)
    assert 'href="https://blog.vertistratsolution.com/search/label/Energy%20%26%20Fuels"' in h
    assert 'data-label="Agriculture &amp; Fertilisers"' in h and "gs-pitch-v1" in h and h.rstrip().endswith("</script>")


def test_emit_pitch_falls_back_to_derived_slug_for_unknown_theme(monkeypatch):
    monkeypatch.setattr(I, "PITCH_THEMES", ["Brand New & Topic"])
    out = []
    I.emit_pitch(out.append)
    assert "search/label/Brand%20New%20%26%20Topic" in "\n".join(out)


def test_emit_accordion_sorted_case_insensitive_and_escaped():
    out = []
    I.emit_accordion(out.append, [("beta & co", "beta%20%26%20co"), ("Alpha", "Alpha"), ("Zed", "Zed")])
    h = "\n".join(out)
    order = [h.index(f'data-label="{n}"') for n in ("Alpha", "beta &amp; co", "Zed")]
    assert order == sorted(order)
    assert 'search/label/beta%20%26%20co">Open the beta &amp; co topic page' in h and h.count("<details") == 3


# ------------------------------------------------------------------ graph
def posts_with(entities_list):
    return {f"p{i}": {"entities": e} for i, e in enumerate(entities_list)}


def test_svg_graph_empty_when_below_threshold():
    assert I.svg_graph(posts_with([["A"]] * 4)) == "<p>no graph</p>"
    assert I.svg_graph({}) == "<p>no graph</p>"


def test_svg_graph_nodes_edges_table_and_threshold():
    posts = posts_with([["Ethanol", "Coal"]] * 5 + [["Ethanol", "Steel"]] * 2 + [["Ethanol"]] * 3 + [["Coal", "Steel"]] * 1 + [["Rare"]] * 4)
    svg = I.svg_graph(posts)
    assert svg.count("<circle") == 2 and svg.count("<line") == 1                  # Ethanol(10) and Coal(6); Steel(3) < 5; edge Ethanol-Coal (5)
    assert "Ethanol <tspan" in svg and ">10</tspan>" in svg and "Rare" not in svg and "Steel" not in svg
    assert '<th scope="row">Ethanol</th><td>10</td><td>Coal (5)</td>' in svg
    assert '<th scope="row">Coal</th><td>6</td><td>Ethanol (5)</td>' in svg
    assert svg.startswith('<svg viewBox="0 0 920 780"') and "<title>How the subjects connect</title>" in svg


def test_svg_graph_edge_needs_two_shared_posts_and_ranks_partners():
    posts = posts_with([["A", "B"]] * 5 + [["A", "C"]] * 1 + [["A"]] * 0 + [["C"]] * 4 + [["B"]] * 0)
    svg = I.svg_graph(posts)
    assert svg.count("<line") == 1                                                # A-C shares only one post
    assert '<th scope="row">C</th><td>5</td><td>&ndash;</td>' in svg
    many = posts_with([["T", "P1", "P2", "P3", "P4"]] * 5 + [["T", "P1", "P2"]] * 3 + [["T", "P1"]] * 2)
    s2 = I.svg_graph(many)
    row = re.search(r'<th scope="row">T</th><td>10</td><td>([^<]*)</td>', s2).group(1)
    assert row.startswith("P1 (10); P2 (8); P")
    assert row.count(";") == 2                                                    # only the 3 strongest partners


def test_svg_graph_label_side_depends_on_position():
    svg = I.svg_graph(posts_with([["A", "B", "C", "D"]] * 5))
    anchors = re.findall(r'text-anchor="(start|end)"', svg)
    assert anchors == ["start", "start", "start", "end"]                  # nodes at -90, 0, 90 and 180 degrees


def test_svg_graph_escapes_names_and_caps_nodes():
    posts = posts_with([[f"N{i:02d}" for i in range(25)] + ["A<b>"]] * 6)
    svg = I.svg_graph(posts)
    assert svg.count("<circle") == 18 and "A<b>" not in svg
    posts2 = posts_with([["A<b>"]] * 6)
    assert "A&lt;b&gt;" in I.svg_graph(posts2)


# --------------------------------------------------------------------- main
def graph_post(title, published, url=None, **kw):
    d = {"title": title, "url": url or f"https://b/{title}.html", "published": published, "countries": [], "states": [],
         "entities": [], "related": []}
    d.update(kw)
    return d


def run_main(tmp_path, graph, *extra):
    g = tmp_path / "graph.json"
    g.write_text(json.dumps(graph))
    out = tmp_path / "out.html"
    import sys
    old = sys.argv
    sys.argv = ["bip", "--graph", str(g), "--out", str(out), *extra]
    try:
        rc = I.main()
    finally:
        sys.argv = old
    return rc, out.read_text(encoding="utf-8")


def test_main_builds_all_sections(root, capsys):
    graph = {
        "article-index-start-here": graph_post("Index", "2026-01-01"), "about-author": graph_post("About", "2026-01-02"),
        "old": graph_post("Opening", "2023-05-01T00:00:00Z"),
        "a": graph_post("Alpha", "2026-03-05T00:00:00Z", countries=["China", "Japan", "Brazil"], states=["Gujarat", "Kerala", "Assam"],
                        entities=["Ethanol"], related=[{"slug": "b"}, {"slug": "missing"}, {"slug": "old"}, {"slug": "a"}]),
        "b": graph_post("Beta", "2026-03-05T12:00:00Z", countries=["China"], entities=["Ethanol"]),
        "c": graph_post("Gamma", "2026-04-09T00:00:00Z", states=["Gujarat"]),
        "ai-high-demand-launch-tracker-x": graph_post("AI Tracker", "2026-04-10T00:00:00Z"),
        "undated": graph_post("Undated piece", ""),
    }
    add_post(root, "a", "<h2>Ethanol</h2><p>text</p>")
    (root / "meta" / "a.json").write_text(json.dumps({"slug": "a", "labels": ["Energy & Fuels", "Other"]}))
    rc, html = run_main(root, graph)
    assert rc == 0
    assert "Every piece on this blog, three ways in" in html and "<b>6</b><span>Articles</span>" in html or "Articles</span>" in html
    assert 'href="https://blog.vertistratsolution.com/2026/08/article-index-start-here.html"' in html
    assert ">Index<" not in html and ">About<" not in html                          # utility pages are not listed
    assert 'id="gs-tracker"' in html and '<a href="#gs-tracker">AI Tracker</a>' in html
    assert '<span class="ctag"><span class="sr-only">Topic: </span>Energy &amp; Fuels</span>' in html and 'class="ctag none"' in html
    assert 'data-topic="Unlabelled"' in html and 'data-date=""' in html and "Undated" in html
    assert html.index('id="gs-m-2026-04"') < html.index('id="gs-m-2026-03"') < html.index('id="gs-m-2023-05"')
    assert "Sunday 5 April" not in html and "Thursday 5 March 2026" in html and "2 articles" in html
    assert 'class="cgeo"><span class="sr-only">About: </span>China, Japan, Gujarat, Kerala</span>' in html
    assert "Brazil" not in html.split('class="cgeo"')[1].split("</span>")[1]
    rel = re.search(r'<span class="crel-lbl">Related</span>(.*?)</span>\s*</li>', html, re.S).group(1)
    assert rel.count("crel-a") == 3 and "Beta" in rel and "Opening" in rel and "missing" not in rel.lower()
    assert 'class="geoblock"><p class="geoh">China <span>2</span>' in html
    assert html.index("China <span>2</span>") < html.index("Japan <span>1</span>")
    assert "The blog opened on <b>1 May 2023</b> with a single post" in html and "<b>3 years</b>" in html
    assert 'id="gs-f-q"' in html and "gs-index-v1" in html
    assert "wrote" in capsys.readouterr().out


def test_main_manifest_filters_and_dedupes_titles(root):
    graph = {"keep": graph_post("Same Title", "2026-02-01T00:00:00Z", url="https://b/keep"),
             "dup": graph_post("  same   title ", "2026-03-01T00:00:00Z", url="https://b/dup"),
             "dead": graph_post("Dead", "2026-03-02T00:00:00Z", url="https://b/dead"),
             "other": graph_post("Other", "2026-03-03T00:00:00Z", url="https://b/other")}
    (root / "meta" / "manifest.json").write_text(json.dumps({"posts": {"1": {"slug": "keep"}, "2": {"slug": "dup"}, "3": {"slug": "other"}}}))
    _, html = run_main(root, graph)
    assert "https://b/keep" in html and "https://b/other" in html and "https://b/dup" not in html and "https://b/dead" not in html


def test_main_without_manifest_lists_everything_and_shell_head_tail(root, tmp_path):
    graph = {"a": graph_post("A", "2026-02-01T00:00:00Z"), "b": graph_post("B", "2026-03-01T00:00:00Z")}
    head = tmp_path / "head.html"
    head.write_text('<html><div class="artx idx"><div class="topnav-index-link" x>old nav</div>  <p>H</p>')
    tail = tmp_path / "tail.html"
    tail.write_text("</div></html>")
    rc, out = run_main(root, graph, "--shell-head", str(head), "--shell-tail", str(tail))
    assert out.startswith('<html><div class="artx idx" lang="en"><p>H</p>') and "old nav" not in out
    assert out.endswith("</div></html>") and out.count('class="topnav-index-link"') == 1
    assert "https://b/A.html" in out and "https://b/B.html" in out and "no graph" in out


def test_main_gap_note_only_when_a_calendar_year_boundary_separates_first_two_posts(root):
    _, html = run_main(root, {"a": graph_post("A", "2026-02-01T00:00:00Z")})
    assert "published nothing for" not in html
    _, html = run_main(root, {"a": graph_post("A", "2026-01-01T00:00:00Z"), "b": graph_post("B", "2026-02-01T00:00:00Z")})
    assert "published nothing for" not in html                                      # same year
    _, html = run_main(root, {"a": graph_post("A", "2025-12-30T00:00:00Z"), "b": graph_post("B", "2026-02-01T00:00:00Z")})
    assert "published nothing for <b>1 years</b>" in html                           # year difference counts, not elapsed time

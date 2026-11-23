import json

import pytest

import crosslink_analysis as X
import index_graph as G


def link(slug, y="2026", m="09", frag=""):
    return f'<a href="https://masaladeutsch.blogspot.com/{y}/{m}/{slug}.html{frag}">x</a>'


@pytest.fixture
def site(tmp_path, monkeypatch):
    for mod in (X, G):
        monkeypatch.setattr(mod, "ROOT", tmp_path)
    (tmp_path / "meta").mkdir()
    (tmp_path / "posts").mkdir()
    state = {"posts": {}}

    def add(slug, body="", labels=(), title=None, published="2026-03-04T00:00:00Z", live=True):
        (tmp_path / "posts" / f"{slug}.html").write_text(body, encoding="utf-8")
        if live:
            state["posts"][f"id-{slug}"] = {"slug": slug, "title": title or slug.title(), "url": f"https://b/{slug}.html",
                                            "labels": list(labels), "published": published}
        (tmp_path / "meta" / "manifest.json").write_text(json.dumps({"posts": state["posts"]}))
    return tmp_path, add


# ------------------------------------------------------------ crosslink
def test_strip_tags_scripts():
    assert X.strip_tags_scripts("a<script>b</script>c<STYLE x=1>d</STYLE>e").split() == ["a", "c", "e"]


def test_load_manifest_by_slug(site):
    tmp, add = site
    add("a", labels=["L"])
    assert X.load_manifest()["a"]["labels"] == ["L"]


def test_extract_outbound_rules(site):
    tmp, add = site
    body = (link("other") + link("OTHER-2", frag="#sec") + link("self-post") + link("article-index-start-here") + link("dup_0123")
            + '<a href="https://example.com/2026/09/ext.html">e</a><a href="https://masaladeutsch.blogspot.com/p/disclaimer.html">d</a>'
            + "<script>" + link("in-script") + "</script>")
    (tmp / "p.html").write_text(body)
    assert X.extract_outbound(tmp / "p.html", "self-post") == {"other", "other-2", "dup_0123"}


def test_build_graph_only_live_on_both_ends(site):
    tmp, add = site
    add("a", link("b") + link("ghost") + link("c"))
    add("b", "")
    add("c", link("a"))
    add("archived", link("a"), live=False)
    (tmp / "meta" / "manifest.json").write_text(json.dumps({"posts": {k: v for k, v in json.loads((tmp / "meta" / "manifest.json").read_text())["posts"].items()}}))
    g = X.build_graph(X.load_manifest())
    assert g == {"a": {"b", "c"}, "b": set(), "c": {"a"}}


def run(monkeypatch, *argv):
    monkeypatch.setattr(X.sys, "argv", ["x", *argv])
    return X.main()


def test_main_json_report(site, monkeypatch, capsys):
    tmp, add = site
    add("hub", link("a") + link("b") + link("c"), labels=["Niche", "Big"])
    add("a", link("hub"), labels=["Niche", "Big"])
    add("b", "", labels=["Niche", "Big"])
    add("c", "", labels=["Niche"])
    add("iso", "", labels=["Lonely"])
    out = tmp / "r.json"
    assert run(monkeypatch, "--json", str(out), "--min-label-cluster", "3") == 0
    r = json.loads(out.read_text())
    assert r["posts_considered"] == 5 and r["total_content_link_edges"] == 4 and r["distinct_linked_pairs"] == 3
    assert r["orphans_both_directions"] == ["iso"]
    assert r["orphans_no_outbound_only"] == ["b", "c"] and r["orphans_no_inbound_only"] == []
    assert r["top_out_degree"][0] == ["hub", 3] and r["top_in_degree"][0][1] == 1
    pairs = {tuple(c["slugs"]): c for c in r["candidate_pairs"]}
    # Niche has 4 members (weight .25), Big has 3 members (1/3); unlinked pairs among them only
    assert ("a", "b") in pairs and pairs[("a", "b")]["score"] == round(0.25 + 1 / 3, 3) and sorted(pairs[("a", "b")]["shared_labels"]) == ["Big", "Niche"]
    assert ("a", "hub") not in pairs and ("b", "hub") not in pairs and ("c", "hub") not in pairs   # hub links to all three
    assert pairs[("b", "c")]["score"] == 0.25
    assert ("iso", "a") not in pairs
    assert f"wrote {out}" in capsys.readouterr().out


def test_main_label_cluster_bounds(site, monkeypatch):
    tmp, add = site
    for i in range(41):
        add(f"p{i:02d}", "", labels=["Huge"])
    for i in range(3):
        add(f"q{i}", "", labels=["Tiny3"])
    for i in range(2):
        add(f"r{i}", "", labels=["Pair"])
    out = tmp / "r.json"
    run(monkeypatch, "--json", str(out), "--top", "500")
    labs = {tuple(c["slugs"]): c["shared_labels"] for c in json.loads(out.read_text())["candidate_pairs"]}
    assert all(l == ["Tiny3"] for l in labs.values()) and len(labs) == 3          # >40 and <3 clusters ignored
    run(monkeypatch, "--json", str(out), "--min-label-cluster", "2", "--top", "500")
    assert ["Pair"] in [c["shared_labels"] for c in json.loads(out.read_text())["candidate_pairs"]]
    add("p41", "", labels=["Huge"])
    run(monkeypatch, "--json", str(out), "--min-label-cluster", "2", "--top", "5000")
    all_labels = {l for c in json.loads(out.read_text())["candidate_pairs"] for l in c["shared_labels"]}
    assert "Huge" not in all_labels                                              # 42 members > 40


def test_main_exactly_forty_members_still_counts(site, monkeypatch):
    tmp, add = site
    for i in range(40):
        add(f"p{i:02d}", "", labels=["Forty"])
    out = tmp / "r.json"
    run(monkeypatch, "--json", str(out), "--top", "5")
    assert json.loads(out.read_text())["candidate_pairs"][0]["score"] == round(1 / 40, 3)
    assert len(json.loads(out.read_text())["candidate_pairs"]) == 5            # --top caps the list


def test_main_text_report_sections(site, monkeypatch, capsys):
    tmp, add = site
    add("hub", link("a"), labels=["L"])
    add("a", "", labels=["L"])
    add("b", "", labels=["L"])
    add("iso", "")
    assert run(monkeypatch, "--top", "1") == 0
    out = capsys.readouterr().out
    assert "posts considered: 4" in out and "content cross-link edges (directed): 1" in out and "distinct linked pairs: 1" in out
    assert "average outbound content links per post: 0.25" in out
    assert "=== Orphans: zero outbound AND zero inbound content links (2) ===" in out and "... and 1 more" in out
    assert "=== Zero outbound, but linked FROM elsewhere (1) ===\n  a  (in-links: 1)" in out
    assert "=== Never linked TO from any other post (1) ===\n  hub  (out-links: 1)" in out
    assert "  1  hub" in out and "=== Top candidate link opportunities" in out
    assert "<->" in out


def test_main_empty_site_divides_safely(site, monkeypatch, capsys):
    tmp, add = site
    (tmp / "meta" / "manifest.json").write_text(json.dumps({"posts": {}}))
    run(monkeypatch)
    assert "average outbound content links per post: 0.00" in capsys.readouterr().out


# ----------------------------------------------------------- index_graph
def test_parts_heads_body_and_cleaning(tmp_path):
    f = tmp_path / "p.html"
    f.write_text('<script>x=1</script><style>a{}</style><h1>Big &amp; Bold</h1><p class="standfirst">Subhead</p>'
                 '<p class="disclaimer" data-x>AI NOTE</p><h2>Two</h2><h4>Four</h4><p>Body Text</p>', encoding="utf-8")
    head, body_l, body = G.parts(f)
    assert "big & bold" in head and "subhead" in head and "two" in head and "four" not in head
    assert "ai note" not in body_l and "x=1" not in body_l and "body text" in body_l and "Body Text" in body


def test_score_weights_and_caps():
    gaz = {"A": ["alpha"], "B": ["beta", "bet"]}
    assert G.score(gaz, "alpha", "") == {"A": 4}
    assert G.score(gaz, "", "alpha " * 10) == {"A": 6}                # body capped at 6
    assert G.score(gaz, "alpha alpha", "alpha " * 10) == {"A": 14}
    assert G.score(gaz, "", "beta") == {"B": 2}              # "beta" and its prefix "bet" both match once
    assert G.score(gaz, "", "beta bet") == {"B": 3}
    assert G.score(gaz, "", "nothing") == {}


def runi(monkeypatch, *argv):
    monkeypatch.setattr(G.sys, "argv", ["g", *argv])
    return G.main()


def test_main_thresholds_and_entities_related(site, monkeypatch, tmp_path, capsys):
    tmp, add = site
    china_head = "<h1>China, China and Gujarat ethanol urea</h1>"
    add("p1", china_head + "<p>" + "ethanol " * 6 + "</p>", title="P1")
    add("p2", "<h1>Ethanol policy urea</h1><p>" + "ethanol " * 6 + " china china china china china china</p>", title="P2")
    add("p3", "<p>coal mentions only coal coal coal coal coal</p>", title="P3")
    add("p4", "<h2>Steel</h2><p>" + "steel " * 5 + "</p>", title="P4")
    add("ghost", "<h1>China</h1>", live=False)
    out = tmp / "g.json"
    assert runi(monkeypatch, "--json", str(out), "--report") == 0
    d = json.loads(out.read_text(encoding="utf-8"))
    assert set(d) == {"p1", "p2", "p3", "p4"}
    assert d["p1"]["countries"] == ["China"] and d["p1"]["states"] == ["Gujarat"] and "Ethanol" in d["p1"]["entities"]
    assert d["p2"]["countries"] == ["China"]                         # 6 body mentions reaches the floor of 6
    assert d["p3"]["entities"] == ["Coal"] and d["p3"]["countries"] == []         # 5 body mentions: entity floor 5 exactly
    assert d["p4"]["entities"] == ["Steel"]                          # 4 head + 5 body capped... = 4+5 = 9
    rel = d["p1"]["related"]
    assert rel[0]["slug"] == "p2" and "Ethanol" in rel[0]["shared"] and rel[0]["w"] > 1.0
    assert "_g" not in d["p1"] and "_e" not in d["p1"] and d["p1"]["published"] == "2026-03-04"
    assert d["p3"]["related"] == [] and d["p4"]["related"] == []
    text = capsys.readouterr().out
    assert "wrote" in text and "posts 4" in text and "== COUNTRIES (posts about) ==" in text and "   2  China" in text
    assert "posts with no geography beyond India: 2" in text


def test_geography_floor_boundaries(site, monkeypatch, tmp_path):
    tmp, add = site
    add("five", "<p>" + "japan " * 5 + "</p>")          # body 5 -> below floor 6
    add("six", "<p>" + "japan " * 6 + "</p>")           # body 6 -> reaches floor
    add("st3", "<p>" + "kerala " * 3 + "</p>")          # states floor 4
    add("st4", "<p>" + "kerala " * 4 + "</p>")
    add("e4", "<p>" + "coal " * 4 + "</p>")             # entities floor 5
    out = tmp / "g.json"
    runi(monkeypatch, "--json", str(out))
    d = json.loads(out.read_text())
    assert d["five"]["countries"] == [] and d["six"]["countries"] == ["Japan"]
    assert d["st3"]["states"] == [] and d["st4"]["states"] == ["Kerala"]
    assert d["e4"]["entities"] == []


def test_related_weights_prefer_rare_entities_and_cap_four(site, monkeypatch, tmp_path):
    tmp, add = site
    common = "<h1>Ethanol</h1><p>" + "ethanol " * 5 + "</p>"
    for i in range(6):
        add(f"c{i}", common)
    rare = "<h1>Rare earths and ethanol</h1><p>" + "rare earth " * 5 + "ethanol " * 5 + "</p>"
    add("r1", rare)
    add("r2", rare)
    out = tmp / "g.json"
    runi(monkeypatch, "--json", str(out))
    d = json.loads(out.read_text())
    assert d["r1"]["related"][0]["slug"] == "r2" and len(d["r1"]["related"]) == 4
    assert d["c0"]["related"][0]["w"] == pytest.approx(1 / 8 * 1)   # ethanol df = 8
    # shared country adds 0.25
    add("g1", "<h1>China</h1><p>" + "china " * 6 + "ethanol " * 5 + "</p>")
    add("g2", "<h1>China</h1><p>" + "china " * 6 + "ethanol " * 5 + "</p>")
    runi(monkeypatch, "--json", str(out))
    d = json.loads(out.read_text())
    w = {x["slug"]: x["w"] for x in d["g1"]["related"]}
    assert w["g2"] == pytest.approx(round(1 / 10 + 0.25, 3), abs=1e-3)
    assert w["g2"] > max(v for k, v in w.items() if k != "g2")


def test_main_without_flags_prints_nothing(site, monkeypatch, capsys):
    tmp, add = site
    add("a", "<p>x</p>")
    assert runi(monkeypatch) == 0 and capsys.readouterr().out == ""

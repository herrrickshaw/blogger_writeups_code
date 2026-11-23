import io
import json
import urllib.error

import pytest

import build_md_summary as B
from netfake import Net, http_error


def test_is_live_only_confirmed_404_410_are_dead(monkeypatch):
    n = Net().install(monkeypatch)
    n.queue += [{}, http_error(404), http_error(410), http_error(500), http_error(403), urllib.error.URLError("x"), TimeoutError()]
    assert B.is_live("http://x/p.html") is True
    assert B.is_live("http://x/p.html") is False
    assert B.is_live("http://x/p.html") is False
    assert B.is_live("http://x/p.html") is True and B.is_live("http://x/p.html") is True
    assert B.is_live("http://x/p.html") is True and B.is_live("http://x/p.html") is True
    assert n.requests[0]["headers"]["User-agent"].startswith("masaladeutsch-summary-builder")
    assert n.requests[0]["kw"]["timeout"] == 8 or n.requests[0]["args"] == (8,)


def test_get_standfirst_variants():
    assert B.get_standfirst('<p class="standfirst">A <b>bold</b> &amp;   line</p>') == "A bold & line"
    long_text = "x" * 81
    assert B.get_standfirst(f'<p class="nav">All Articles {long_text}</p><p>{long_text} end</p>') == f"{long_text} end"
    assert B.get_standfirst(f"<p>{'y' * 80}</p>") == ""                       # exactly 80 chars is too short
    assert B.get_standfirst(f"<p>{'y' * 81}</p>") == "y" * 81
    assert B.get_standfirst("<p>short</p>") == ""
    assert B.get_standfirst("") == ""
    assert B.get_standfirst(f'<p class="x" id="y">{long_text}</p>') == long_text


def test_unit_and_abbr_regexes():
    found = {m.group(1).lower() for m in B.UNIT_RE.finditer("5 crore, 3.5 bn and 12% plus 7 MW, 1,200 tonnes, 4 acre. 9 foo")}
    assert found == {"crore", "bn", "mw", "tonnes", "acre"}
    assert B.UNIT_RE.search("no 5crore") is not None and B.UNIT_RE.search("bn alone") is None
    assert {m.group(0) for m in B.ABBR_RE.finditer("The RBI and A and NITI, EBITDAXX9 PIB")} == {"RBI", "NITI", "PIB"}


def test_definition_tables_cover_each_other():
    assert all(k == k.lower() for k in B.UNIT_DEFS)
    assert B.GLOSSARY_DEFS["RBI"].startswith("Reserve Bank")
    assert "crore" in B.UNIT_DEFS


@pytest.fixture
def site(tmp_path, monkeypatch):
    monkeypatch.setattr(B, "ROOT", str(tmp_path))
    monkeypatch.setattr(B, "OUT_PATH", str(tmp_path / "SUMMARY.md"))
    (tmp_path / "meta").mkdir()
    (tmp_path / "posts").mkdir()
    monkeypatch.setattr(B, "is_live", lambda url: "dead" not in url)

    def add(slug, title="T", url=None, published="2026-01-02T03:04", labels=("L1",), body=None, meta_extra=None):
        m = {"slug": slug, "title": title, "url": url if url is not None else f"https://b/{slug}.html",
             "published": published, "labels": list(labels)}
        m.update(meta_extra or {})
        (tmp_path / "meta" / f"{slug}.json").write_text(json.dumps(m))
        if body is not False:
            (tmp_path / "posts" / f"{slug}.html").write_text(
                body if body is not None else f'<p class="standfirst">Stand for {slug}.</p><p>Spent 5 crore for RBI.</p>', encoding="utf-8")
    return tmp_path, add


def text(tmp):
    return (tmp / "SUMMARY.md").read_text(encoding="utf-8")


def test_main_builds_sections_sorted_and_glossary(site, capsys):
    tmp, add = site
    add("b", title="Beta", published="2026-02-01T00:00", labels=("Zeta", "alpha"))
    add("a", title="Alpha", published="2026-01-01T00:00", labels=())
    B.main()
    t = text(tmp)
    assert t.startswith("# VertiStrat Solutions — All Posts, Summarised")
    assert "*2 published posts, 3 topic labels." in t
    assert "- **crore** — Indian numbering unit" in t and "- **RBI** — Reserve Bank of India" in t
    assert "- **mw**" not in t
    labels = [l for l in t.splitlines() if l.startswith("### ") and "(" in l]
    assert labels[:3] == ["### alpha (1)", "### Unlabelled (1)", "### Zeta (1)"]       # case-insensitive label sort
    chron = t.split("## Chronological (All Posts)")[1]
    assert chron.index("[Alpha]") < chron.index("[Beta]")
    assert "*2026-01-01 · —*" in chron and "*2026-02-01 · Zeta, alpha*" in chron
    assert "Stand for a." in chron
    assert "wrote 2 posts, 1 units, 1 glossary terms" in capsys.readouterr().out


def test_main_skips_dead_unpublished_slugs_missing_files_and_dedupes(site, capsys):
    tmp, add = site
    add("ok")
    add("dead", url="https://b/dead.html")
    add("nourl", url="")
    add("nopub", published="")
    add("about-author")
    add("article-index-start-here")
    add("nofile", body=False)
    add("dup1", url="https://b/same.html")
    add("dup2", url="https://b/same.html")
    (tmp / "meta" / "broken.json").write_text("{not json")
    B.main()
    t = text(tmp)
    assert "*2 published posts" in t
    assert "skipping dead link: dead -> https://b/dead.html" in capsys.readouterr().err
    assert t.count("https://b/same.html") == 2                 # one post kept: once under By Topic, once in Chronological


def test_main_standfirst_missing_and_table_blocks_excluded_from_corpus(site):
    tmp, add = site
    add("p", body="<p>no standfirst and short</p><table><tr><td>9 lakh</td><td>RIL</td></tr></table>")
    B.main()
    t = text(tmp)
    assert "*(no standfirst found)*" in t
    assert "lakh" not in t.split("## By Topic")[0] and "RIL" not in t.split("## By Topic")[0]     # table rows are not scanned


def test_main_no_posts_still_writes_header(site, capsys):
    tmp, add = site
    B.main()
    assert "*0 published posts, 0 topic labels." in text(tmp)


@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="build_md_summary.py UNIT_RE ends in \\b after '%', which needs a word character next, so '12% growth' never registers the % unit")
def test_percent_unit_is_listed_when_used(site):
    tmp, add = site
    add("p", body='<p class="standfirst">Growth of 12% this year.</p><p>Output grew 12% in 2026.</p>')
    B.main()
    assert "- **%** — percent" in text(tmp)

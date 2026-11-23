import json

import pytest

import normalise_posts as N

INV = "@media not all and (prefers-color-scheme:dark){.a{color:#ddd}}"


def test_drop_style_blocks_removes_only_layer_blocks():
    src = ("<style>.keep{}</style><style id=x>/* BW-OVERRIDE */ a{}</style>"
           "<style>.gs-light-lock{}</style><style>gs-dark-panel-guard</style>")
    out, removed = N.drop_style_blocks(src)
    assert out == "<style>.keep{}</style>"
    assert removed == ["BW-override", "light-lock", "dark-panel guard"]


def test_drop_style_blocks_first_marker_wins_once():
    out, removed = N.drop_style_blocks("<style>BW-OVERRIDE gs-light-lock</style>")
    assert out == "" and removed == ["BW-override"]


def test_drop_inverted_nested_braces():
    src = f"<style>p{{}}{INV}h{{}}</style>"
    out, n = N.drop_inverted(src)
    assert out == "<style>p{}h{}</style>" and n == 1


def test_drop_inverted_multiple_and_cap_at_13():
    out, n = N.drop_inverted("x" + INV + "y" + INV + "z")
    assert (out, n) == ("xyz", 2)
    out, n = N.drop_inverted(INV * 20)
    assert n == 13 and out == INV * 7


def test_drop_inverted_no_brace_or_unbalanced():
    out, n = N.drop_inverted("a @media not all and (prefers-color-scheme:dark) b")
    assert n == 0 and out.startswith("a @media")
    out, n = N.drop_inverted("a @media not all and (prefers-color-scheme:dark){.x{")
    assert (out, n) == ("a ", 1)


def test_tidy_collapses():
    assert N.tidy("a<style>  </style>\n\n\n\nb") == "a\n\nb"
    assert N.tidy("a\n\nb") == "a\n\nb"
    assert N.tidy("<style>x</style>") == "<style>x</style>"


def test_normalise_reports_layers_and_inverted_count():
    src = f"<style>BW-OVERRIDE</style><style>p{{}}{INV}</style><p>t</p>"
    out, layers = N.normalise(src)
    assert out == "<style>p{}</style><p>t</p>"
    assert layers == ["BW-override", "inverted-MQ x1"]
    assert N.normalise("<p>clean</p>") == ("<p>clean</p>", [])


def test_guard_ok_all_pass_and_each_failure():
    before = ('<script>1</script><p class="gs-ai-disclosure">hi</p>google_translate_element article-index-start-here'
              '<style>BW-OVERRIDE</style><p>text</p>')
    after, _ = N.normalise(before)
    assert all(N.guard_ok(before, after).values())
    c = N.guard_ok(before, after.replace("<script>1</script>", ""))
    assert not c["scripts kept"] and c["smaller"]
    assert not N.guard_ok(before, after.replace("gs-ai-disclosure", "x"))["disclosure kept"]
    assert not N.guard_ok(before, after.replace("google_translate_element", ""))["translate kept"]
    assert not N.guard_ok(before, after.replace("article-index-start-here", ""))["index link kept"]
    assert not N.guard_ok(before, after.replace("text", "TEXT"))["visible text unchanged"]
    assert not N.guard_ok(before, before + "pad")["smaller"]
    assert N.guard_ok(before, before)["smaller"]          # equal length is allowed


def test_guard_ok_ignores_whitespace_and_style_text_when_comparing_visible():
    assert N.guard_ok("<p>a  b</p><style>x</style>", "<p>a b</p>")["visible text unchanged"]


@pytest.fixture
def site(tmp_path, monkeypatch):
    (tmp_path / "posts").mkdir()
    (tmp_path / "meta").mkdir()
    monkeypatch.setattr(N, "POSTS", tmp_path / "posts")
    monkeypatch.setattr(N, "OUT", tmp_path / "out" / "normalised")
    monkeypatch.setattr(N, "MANIFEST", tmp_path / "meta" / "manifest.json")
    monkeypatch.setattr(N.sys, "argv", ["normalise_posts.py"])

    def add(slug, body):
        (tmp_path / "posts" / f"{slug}.html").write_text(body, encoding="utf-8")

    def manifest(slugs):
        (tmp_path / "meta" / "manifest.json").write_text(json.dumps({"posts": {s: {"slug": s} for s in slugs}}))
    return tmp_path, add, manifest


def test_main_writes_changed_skips_clean_and_missing(site, capsys):
    tmp, add, manifest = site
    add("b-dirty", "<style>BW-OVERRIDE</style><p>x</p>")
    add("a-clean", "<p>clean</p>")
    manifest(["b-dirty", "a-clean", "c-missing"])
    assert N.main() == 0
    out = capsys.readouterr().out
    assert out.startswith("1 posts would change · 1 already clean · 0 refused")
    assert (tmp / "out" / "normalised" / "b-dirty.html").read_text() == "<p>x</p>"
    assert not (tmp / "out" / "normalised" / "a-clean.html").exists()
    assert "b-dirty" in out and "BW-override" in out


def test_main_refuses_when_guard_trips_and_returns_1(site, capsys):
    tmp, add, manifest = site
    # removal of the style block also changes nothing visible, so force a trip via a script inside the layer block
    add("bad", "<style>BW-OVERRIDE</style><script>1</script><p>x</p>".replace("<style>BW-OVERRIDE</style>", "<style>BW-OVERRIDE <script>2</script></style>"))
    manifest(["bad"])
    assert N.main() == 1
    out = capsys.readouterr().out
    assert "REFUSED" in out and "scripts kept" in out and "1 refused" in out
    assert not (tmp / "out" / "normalised" / "bad.html").exists()


def test_main_slug_filter(site, monkeypatch, capsys):
    tmp, add, manifest = site
    add("one", "<style>BW-OVERRIDE</style><p>1</p>")
    add("two", "<style>BW-OVERRIDE</style><p>2</p>")
    manifest(["one", "two"])
    monkeypatch.setattr(N.sys, "argv", ["normalise_posts.py", "--slug", "two"])
    N.main()
    assert [p.name for p in (tmp / "out" / "normalised").iterdir()] == ["two.html"]

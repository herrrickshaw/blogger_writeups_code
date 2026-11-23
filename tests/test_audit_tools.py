import json
import urllib.error

import pytest

import link_audit as LA
import research_crosscheck as RC
import site_health as SH
from netfake import Routes, http_error


@pytest.fixture(autouse=True)
def _nosleep(monkeypatch):
    import time
    monkeypatch.setattr(time, "sleep", lambda s: None)


# ===================================================== research_crosscheck
def test_is_specific_enough():
    assert RC.is_specific_enough("12%") and RC.is_specific_enough("₹ 10")
    assert not RC.is_specific_enough("1%") and not RC.is_specific_enough("₹0") and not RC.is_specific_enough("abc")


def test_strip_tags():
    assert RC.strip_tags("<script>x</script><p>a&amp;  b</p><style>c</style> <b>d</b>") == " a& b d "


def test_regexes():
    assert RC.PCT_RE.findall("up 12.5% and 7% and 1234% x") == ["12.5%", "7%"]       # 4-digit figures are not matched
    m = [x.strip() for x in RC.MONEY_RE.findall("Spent ₹1,200 crore, Rs. 50 lakh, $3.5 bn, Rs, and Rs 7")]
    assert m == ["₹1,200 crore", "Rs. 50 lakh", "$3.5 bn", "Rs 7"]


def test_auto_terms_filters_and_caps():
    t = RC.auto_terms("The Big Company bought Reliance Industries Ltd and Tata Steel, It Was ok, Ab Cd, and Tata Steel again")
    assert "Reliance Industries Ltd" in t and "Tata Steel" in t
    assert not any(x.startswith(("The ", "It ")) for x in t) and "Ab Cd" not in t
    assert [x.lower() for x in t].count("tata steel") == 1
    assert t == ["Reliance Industries Ltd", "Tata Steel"]
    many = ", ".join(f"Alpha{i} Beta{i}" for i in range(100))
    assert len(RC.auto_terms(many)) == 60


@pytest.fixture
def posts(tmp_path, monkeypatch):
    monkeypatch.setattr(RC, "POSTS", tmp_path / "posts")
    (tmp_path / "posts").mkdir()

    def add(slug, text):
        (tmp_path / "posts" / f"{slug}.html").write_text(f"<p>{text}</p>", encoding="utf-8")
    return tmp_path, add


def test_load_archive_and_find_term(posts):
    tmp, add = posts
    add("a", "Long prefix text " * 10 + "Reliance is big. " + "suffix " * 20)
    add("b", "nothing here")
    arch = RC.load_archive()
    assert set(arch) == {"a", "b"}
    hits = RC.find_term("RELIANCE", arch)
    assert [h[0] for h in hits] == ["a"] and "Reliance is big" in hits[0][1]
    assert len(hits[0][1]) <= 60 + len("RELIANCE") + 60
    assert RC.find_term("reliance", arch, exclude_slug="a") == []
    assert RC.find_term("zzz", arch) == []


def run_rc(monkeypatch, *argv):
    monkeypatch.setattr(RC.sys, "argv", ["rc", *argv])
    return RC.main()


def test_main_terms_found_zero_variants_and_truncation(posts, monkeypatch, capsys):
    tmp, add = posts
    for i in range(5):
        add(f"p{i}", f"Reliance appears here {i}")
    add("old", "uses Amoxycillin")
    draft = tmp / "post-draft.html"
    draft.write_text("<p>Reliance and Amoxicillin and Zork</p>")
    assert run_rc(monkeypatch, str(draft), "--terms", "Reliance, Amoxicillin ,Zork,, aluminium") == 0
    out = capsys.readouterr().out
    assert "checking against 6 posts" in out
    assert "Reliance  (5 posts)" in out and "… and 2 more" in out
    assert len([l for l in out.splitlines() if l.startswith("    p") and "Reliance appears" in l]) == 3
    assert "Amoxicillin  -- known variant spelling(s) to try: amoxycillin" in out
    assert "  Zork\n" in out and "aluminium  -- known variant spelling(s) to try: aluminum" in out
    assert "1 terms already covered, 3 zero-match" in out


def test_main_excludes_the_draft_itself_and_singular_plural(posts, monkeypatch, capsys):
    tmp, add = posts
    add("draft", "Reliance in the draft itself")
    add("other", "Reliance elsewhere")
    d = tmp / "post-draft.html"
    d.write_text("<p>Reliance</p>")
    run_rc(monkeypatch, str(d), "--terms", "Reliance")
    out = capsys.readouterr().out
    assert "Reliance  (1 post)" in out and "draft:" not in out


def test_main_auto_mode_and_numbers(posts, monkeypatch, capsys):
    tmp, add = posts
    add("other", "Output rose 45% in FY25 and cost ₹ 1,200 crore; also 3% only")
    d = tmp / "d.html"
    d.write_text("<p>Tata Steel grew 45% and spent ₹ 1,200 crore versus 3% or 1%</p>")
    run_rc(monkeypatch, str(d), "--auto", "--numbers")
    out = capsys.readouterr().out
    assert "--auto extracted" in out and "standalone %/currency figures" in out
    assert "45%  appears in 1 other post(s)" in out and "₹ 1,200 crore  appears in 1 other post(s)" in out
    assert "3%  appears" not in out and "1%  appears" not in out         # single-digit figures filtered


def test_main_errors(posts, monkeypatch):
    tmp, add = posts
    with pytest.raises(SystemExit, match="not found"):
        run_rc(monkeypatch, str(tmp / "missing.html"), "--terms", "x")
    d = tmp / "d.html"
    d.write_text("x")
    with pytest.raises(SystemExit, match="pass --terms"):
        run_rc(monkeypatch, str(d))


# ============================================================== link_audit
@pytest.fixture
def la_site(tmp_path, monkeypatch):
    monkeypatch.setattr(LA, "ROOT", tmp_path)
    (tmp_path / "posts").mkdir()
    (tmp_path / "theme").mkdir()
    return tmp_path


def test_classify():
    assert LA.classify("charts/x.html") == "relative" and LA.classify("/p/x") == "relative"
    assert LA.classify("https://blog.vertistratsolution.com/x") == "internal"
    assert LA.classify("https://masaladeutsch.blogspot.com/x") == "internal"
    assert LA.classify("https://pib.gov.in/x") == "external"
    assert LA.classify("http://evil.com/blog.vertistratsolution.com") == "internal"      # substring rule, as written


def test_collect_filters_and_sources(la_site):
    (la_site / "posts" / "a.html").write_text(
        '<a href="https://x.org/1">1</a><a href=\'https://x.org/2\'>2</a><a href="mailto:a@b">m</a><a href="#top">t</a>'
        '<a href="javascript:void(0)">j</a><a href="tel:1">t</a><a href="data:x">d</a><a href="${d.src}">tmpl</a>'
        '<a href="{{ x }}">t2</a><a href=" https://x.org/3 ">sp</a><a href="rel/p.html">r</a>')
    (la_site / "posts" / "b.html").write_text('<a href="https://x.org/1">1</a>')
    (la_site / "theme" / "theme.xml").write_text('<a href="https://x.org/theme">t</a>')
    links = LA.collect()
    assert set(links) == {"https://x.org/1", "https://x.org/2", "https://x.org/3", "rel/p.html", "https://x.org/theme"}
    assert links["https://x.org/1"] == {"a.html", "b.html"} and links["https://x.org/theme"] == {"theme.xml"}


def test_collect_nothing_exits_2(la_site, capsys):
    with pytest.raises(SystemExit) as e:
        LA.collect()
    assert e.value.code == 2 and "no posts/" in capsys.readouterr().err


def test_check_statuses_and_retries(monkeypatch):
    r = Routes({"http://ok": (200, "x"), "http://gone": http_error(404), "http://t429": [http_error(429), (200, "x")],
                "http://t503": [http_error(503), http_error(503)], "http://err": [OSError("dns"), (200, "")],
                "http://err2": [OSError("dns")], "http://403": http_error(403)}).install(monkeypatch)
    assert LA.check("http://ok") == (200, "http://ok")
    assert LA.check("http://gone") == (404, None)
    assert LA.check("http://t429") == (200, "http://t429") and r.hits.count("http://t429") == 2
    assert LA.check("http://t503") == (503, None) and r.hits.count("http://t503") == 2
    assert LA.check("http://err") == (200, "http://err")
    assert LA.check("http://err2") == ("ERR OSError", None) and r.hits.count("http://err2") == 2
    assert LA.check("http://403") == (403, None) and r.hits.count("http://403") == 1       # not retried


def run_la(monkeypatch, *argv):
    monkeypatch.setattr(LA.sys, "argv", ["la", *argv])
    return LA.main()


def test_main_dead_unverifiable_json_and_exit(la_site, monkeypatch, capsys):
    (la_site / "posts" / "p.html").write_text(
        '<a href="rel/x.html">r</a><a href="https://blog.vertistratsolution.com/dead">i</a><a href="https://blog.vertistratsolution.com/ok">i</a>'
        '<a href="https://ext.org/gone">e</a><a href="https://ext.org/blocked">e</a><a href="https://ext.org/fine">e</a>')
    Routes({"https://blog.vertistratsolution.com/dead": http_error(410), "https://blog.vertistratsolution.com/ok": (200, ""),
            "https://ext.org/gone": http_error(404), "https://ext.org/blocked": http_error(403), "https://ext.org/fine": (200, "")}).install(monkeypatch)
    j = la_site / "o.json"
    assert run_la(monkeypatch, "--json", str(j), "--workers", "1") == 1
    out = capsys.readouterr().out
    assert "links found 6  |  checked 6  |  relative 1  internal 2  external 3" in out
    assert "DEAD 3  |  unverifiable 1" in out
    assert "[relative/cannot resolve under a blogspot post path] rel/x.html" in out and "[internal/410]" in out and "[external/404]" in out
    assert "        in p.html" in out and "[403] https://ext.org/blocked" in out
    data = json.loads(j.read_text())
    assert data["results"]["https://ext.org/fine"] == "200" and data["results"]["rel/x.html"] == "relative"
    assert {d["kind"] for d in data["dead"]} == {"relative", "internal", "external"} and data["dead"][0]["sources"] == ["p.html"]
    assert data["unverifiable"] == [{"url": "https://ext.org/blocked", "code": "403"}]


def test_main_internal_skips_external_and_clean_exit(la_site, monkeypatch, capsys):
    (la_site / "posts" / "p.html").write_text('<a href="https://blog.vertistratsolution.com/ok">i</a><a href="https://ext.org/never">e</a>')
    r = Routes({"https://blog.vertistratsolution.com/ok": (200, "")}).install(monkeypatch)
    assert run_la(monkeypatch, "--internal", "--timeout", "5") == 0
    out = capsys.readouterr().out
    assert "(external skipped)" in out and "DEAD 0  |  unverifiable 0" in out and r.hits == ["https://blog.vertistratsolution.com/ok"]


def test_main_unverifiable_only_is_exit_zero(la_site, monkeypatch, capsys):
    (la_site / "posts" / "p.html").write_text('<a href="https://ext.org/slow">e</a>')
    Routes({"https://ext.org/slow": OSError("timeout")}).install(monkeypatch)
    assert run_la(monkeypatch, "--workers", "1") == 0
    assert "[ERR OSError] https://ext.org/slow" in capsys.readouterr().out


# ============================================================== site_health
@pytest.fixture
def sh_site(tmp_path, monkeypatch):
    monkeypatch.setattr(SH, "MANIFEST", tmp_path / "manifest.json")
    return tmp_path


def manifest(tmp, recs):
    (tmp / "manifest.json").write_text(json.dumps({"posts": {r["slug"]: r for r in recs}}))


def rec(slug, title="A Title", published="2026-01-01", url=None):
    return {"slug": slug, "title": title, "published": published, "url": url or f"{SH.BLOG}/{slug}.html"}


HOME_OK = "<div class='card'>x</div><div class=\"post card\">y</div>"


def run_sh(monkeypatch, *argv):
    monkeypatch.setattr(SH.sys, "argv", ["sh", *argv])
    return SH.main()


def test_get_backoff_and_final_raise(monkeypatch):
    r = Routes({"http://a": [http_error(429), http_error(503), (200, "body")], "http://b": http_error(429), "http://c": http_error(404)}).install(monkeypatch)
    slept = []
    monkeypatch.setattr(SH.time, "sleep", lambda s: slept.append(s))
    assert SH.get("http://a") == (200, "body") and slept == [2, 4]
    slept.clear()
    with pytest.raises(urllib.error.HTTPError):
        SH.get("http://b", tries=3)
    assert slept == [2, 4] and r.hits.count("http://b") == 3
    with pytest.raises(urllib.error.HTTPError):
        SH.get("http://c")
    assert r.hits.count("http://c") == 1


def test_check_post_title_matching(monkeypatch):
    monkeypatch.setattr(SH, "PACE", 0)
    Routes({f"{SH.BLOG}/a.html": (200, "<h1>A Title — and more</h1>"), f"{SH.BLOG}/b.html": (200, "page not found"),
            f"{SH.BLOG}/c.html": http_error(404), f"{SH.BLOG}/d.html": OSError("x"), f"{SH.BLOG}/e.html": (200, "anything")}).install(monkeypatch)
    assert SH.check_post(rec("a", "A Title — extra words that are long"))[1:] == (200, True)
    assert SH.check_post(rec("a", "<b>A TITLE</b>"))[1:] == (200, True)                    # tags stripped, case-insensitive
    assert SH.check_post(rec("b"))[1:] == (200, False)
    assert SH.check_post(rec("c"))[1:] == (404, None)
    assert SH.check_post(rec("d"))[1:] == ("ERR OSError", None)
    assert SH.check_post(rec("e", title=""))[1:] == (200, False)                           # no title -> cannot confirm


def test_check_post_matches_only_first_28_chars_of_title_before_dash(monkeypatch):
    monkeypatch.setattr(SH, "PACE", 0)
    long = "x" * 40
    Routes({f"{SH.BLOG}/a.html": (200, "x" * 28 + " tail")}).install(monkeypatch)
    assert SH.check_post(rec("a", long))[2] is True
    Routes({f"{SH.BLOG}/a.html": (200, "x" * 27)}).install(monkeypatch)
    assert SH.check_post(rec("a", long))[2] is False


def base_routes(recs, extra=None, home=(200, HOME_OK)):
    routes = {SH.BLOG + "/": home}
    for r in recs:
        routes[r["url"]] = (200, "<h1>A Title</h1>")
    routes.update(extra or {})
    return routes


def test_main_missing_manifest(sh_site, monkeypatch, capsys):
    assert run_sh(monkeypatch) == 2 and "no manifest" in capsys.readouterr().err


def test_main_healthy(sh_site, monkeypatch, capsys):
    recs = [rec("a"), rec("b")]
    manifest(sh_site, recs)
    Routes(base_routes(recs)).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0", "--workers", "1") == 0
    out = capsys.readouterr().out
    assert "post cards: 2" in out and "posts         2/2 serving their own title" in out and out.strip().endswith("healthy")


def test_main_sample_takes_most_recent(sh_site, monkeypatch, capsys):
    recs = [rec("old", published="2020-01-01"), rec("new", published="2026-06-01"), rec("mid", published="2024-01-01")]
    manifest(sh_site, recs)
    r = Routes(base_routes(recs)).install(monkeypatch)
    run_sh(monkeypatch, "--pace", "0", "--sample", "2")
    assert sorted(h for h in r.hits if h != SH.BLOG + "/") == sorted([recs[1]["url"], recs[2]["url"]])
    assert "2/2 serving" in capsys.readouterr().out


def test_main_problem_kinds_exit_1(sh_site, monkeypatch, capsys):
    recs = [rec("gone"), rec("drafted"), rec("down"), rec("ok")]
    manifest(sh_site, recs)
    routes = base_routes(recs, {recs[0]["url"]: http_error(404), recs[1]["url"]: (200, "not found shell"), recs[2]["url"]: OSError("x")})
    Routes(routes).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0", "--workers", "1") == 1
    out = capsys.readouterr().out
    assert "PROBLEMS 3" in out and f"404: {recs[0]['url']}" in out and f"200 but title missing (drafted? redirected?): {recs[1]['url']}" in out
    assert "ERR OSError" in out and "posts         1/4" in out


def test_main_throttled_posts_inconclusive_not_a_problem(sh_site, monkeypatch, capsys):
    recs = [rec("a"), rec("b")]
    manifest(sh_site, recs)
    Routes(base_routes(recs, {recs[1]["url"]: http_error(429)})).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0", "--workers", "1") == 0
    out = capsys.readouterr().out
    assert "1/2 serving their own title  (1 inconclusive — rate-limited)" in out and "RATE-LIMITED 1 — not checked" in out and "healthy" in out


def test_main_homepage_variants(sh_site, monkeypatch, capsys):
    recs = [rec("a")]
    manifest(sh_site, recs)
    Routes(base_routes(recs, home=(200, "<div>no cards</div>"))).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0") == 1
    assert "homepage rendered 0 post cards (expected at least 1)" in capsys.readouterr().out
    Routes(base_routes(recs, home=(200, "<div class='card'>"))).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0", "--min-homepage-cards", "2") == 1
    Routes(base_routes(recs, home=(200, "<div class='card'>"))).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0", "--min-homepage-cards", "1") == 0
    capsys.readouterr()
    Routes(base_routes(recs, home=http_error(500))).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0") == 1
    assert "homepage returned 500" in capsys.readouterr().out
    Routes(base_routes(recs, home=http_error(429))).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0") == 0
    assert "RATE-LIMITED: homepage — inconclusive" in capsys.readouterr().out
    Routes(base_routes(recs, home=OSError("net"))).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0") == 1
    assert "homepage unreachable: OSError" in capsys.readouterr().out
    Routes(base_routes(recs, home=(301, "<div class='card'>"))).install(monkeypatch)
    assert run_sh(monkeypatch, "--pace", "0") == 1
    assert "homepage returned 301" in capsys.readouterr().out


def test_main_sets_pace(sh_site, monkeypatch):
    manifest(sh_site, [])
    Routes({SH.BLOG + "/": (200, HOME_OK)}).install(monkeypatch)
    run_sh(monkeypatch, "--pace", "1.5")
    assert SH.PACE == 1.5

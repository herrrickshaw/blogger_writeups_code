import hashlib
import json
import os
import sys
import types

import pytest

HERE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "consistency-check")
sys.path.insert(0, HERE)
import audit as A  # noqa: E402
import fix as FX  # noqa: E402
from checks import INVERTED_MQ  # noqa: E402


# ======================================================================== audit
POST = "<html><div class='post-body'><p>text</p><div><b>x</b></div></div><div id='after'>NOT BODY</div></html>"


def test_body_of_balanced_div_and_variants():
    assert A.body_of(POST) == "<div class='post-body'><p>text</p><div><b>x</b></div></div>"
    assert A.body_of('<div class="post-body" id="b"><div>i</div></div>tail') == '<div class="post-body" id="b"><div>i</div></div>'
    assert A.body_of("<p>no body</p>") == ""
    assert A.body_of("<div class='post-body'><div>unclosed") == "<div class='post-body'><div>unclosed"
    assert A.body_of("<div class='post-body'></div>x") == "<div class='post-body'></div>"


def test_sh_returns_stdout(monkeypatch):
    seen = {}
    monkeypatch.setattr(A.subprocess, "run", lambda c, capture_output, text: seen.update(c=c) or types.SimpleNamespace(stdout="OUT"))
    assert A.sh(["echo"]) == "OUT" and seen["c"] == ["echo"]


def feed(entries):
    return json.dumps({"feed": {"entry": entries}})


def e(pid, title="T", url=None):
    return {"id": {"$t": f"tag:blogger.com,1999:blog-1.post-{pid}"}, "title": {"$t": title},
            "link": [{"rel": "self", "href": "s"}, {"rel": "alternate", "href": url or f"https://b/{pid}.html"}]}


def test_post_list_paginates_dedupes_and_stops(monkeypatch):
    pages = {1: feed([e("1"), e("2")]), 26: feed([e("2"), e("3")]), 51: feed([])}
    urls = []
    def sh(cmd):
        urls.append(cmd[-1])
        return pages[int(cmd[-1].split("start-index=")[1].split("&")[0])]
    monkeypatch.setattr(A, "sh", sh)
    posts = A.post_list()
    assert [p["id"] for p in posts] == ["1", "2", "3"] and posts[0]["url"] == "https://b/1.html"
    assert len(urls) == 3 and "max-results=25" in urls[0] and "alt=json" in urls[0]


def test_post_list_stops_on_bad_json_and_missing_feed(monkeypatch):
    monkeypatch.setattr(A, "sh", lambda c: "<html>blocked</html>")
    assert A.post_list() == []
    monkeypatch.setattr(A, "sh", lambda c: "{}")
    assert A.post_list() == []


def test_fetch_uses_curl_with_ua(monkeypatch):
    seen = {}
    monkeypatch.setattr(A, "sh", lambda c: seen.update(c=c) or "html")
    assert A.fetch("http://u") == "html" and seen["c"] == ["curl", "-s", "-A", A.UA, "http://u"]


@pytest.fixture
def out(tmp_path, monkeypatch):
    monkeypatch.setattr(A, "OUT", str(tmp_path / "out"))
    monkeypatch.setattr(A, "SHOTS", str(tmp_path / "shots"))
    os.makedirs(tmp_path / "out")
    return tmp_path


def test_js_syntax_errors_writes_script_once_and_parses(out, monkeypatch):
    calls = []
    monkeypatch.setattr(A, "sh", lambda c: calls.append(c) or " [2, 5] \n")
    assert A.js_syntax_errors("<html>", str(out / "t.html")) == [2, 5]
    assert (out / "t.html").read_text() == "<html>" and (out / "out" / "_syntax.js").exists()
    (out / "out" / "_syntax.js").write_text("custom")
    A.js_syntax_errors("x", str(out / "t.html"))
    assert (out / "out" / "_syntax.js").read_text() == "custom"          # existing helper script is not rewritten
    assert calls[0][0] == "node"
    monkeypatch.setattr(A, "sh", lambda c: "not json")
    assert A.js_syntax_errors("x", str(out / "t.html")) == []
    monkeypatch.setattr(A, "sh", lambda c: "")
    assert A.js_syntax_errors("x", str(out / "t.html")) == []


def test_static_audit_runs_every_rule_and_cleans_tmp(out, monkeypatch):
    monkeypatch.setattr(A, "fetch", lambda url: POST)
    monkeypatch.setattr(A, "js_syntax_errors", lambda html, tmp: [3] if "text" in html else [])
    seen = {}
    def rule_ok(body, node_check):
        seen["nc"], seen["body"] = node_check, body
        return 1, "fine"
    def rule_bad(body, node_check):
        return False, "bad"
    def rule_boom(body, node_check):
        raise KeyError("x")
    monkeypatch.setattr(A, "STATIC_RULES", [("r1", "BLOCKER", rule_ok), ("r2", "MINOR", rule_bad), ("r3", "MAJOR", rule_boom)])
    res = A.static_audit({"id": "7", "title": "T", "url": "u"})
    assert seen["nc"] == [3] and seen["body"].startswith("<div class='post-body'>")
    assert res["checks"] == [{"rule": "r1", "severity": "BLOCKER", "ok": True, "detail": "fine"},
                              {"rule": "r2", "severity": "MINOR", "ok": False, "detail": "bad"},
                              {"rule": "r3", "severity": "MAJOR", "ok": False, "detail": "rule error: KeyError"}]
    assert res["bytes"] == len(POST) and res["id"] == "7"
    assert not (out / "out" / "_t7.html").exists()


def static_result(pid, checks):
    return {"id": pid, "title": f"Post {pid}", "url": f"https://b/{pid}", "checks": checks, "bytes": 1}


def chk(rule, sev, ok, detail=""):
    return {"rule": rule, "severity": sev, "ok": ok, "detail": detail}


def run_main(monkeypatch, *argv):
    monkeypatch.setattr(A.sys, "argv", ["audit.py", *argv])
    A.main()


def test_main_report_ranking_exit_code_and_files(out, monkeypatch, capsys):
    posts = [{"id": "1", "title": "Minor only", "url": "u1"}, {"id": "2", "title": "Clean", "url": "u2"},
             {"id": "3", "title": "Blocker", "url": "u3"}, {"id": "4", "title": "Major x2", "url": "u4"}]
    results = {"u1": [chk("a", "MINOR", False, "m")], "u2": [chk("a", "MINOR", True)],
               "u3": [chk("b", "BLOCKER", False), chk("a", "MINOR", False)],
               "u4": [chk("c", "MAJOR", False, "d1"), chk("c2", "MAJOR", False)]}
    monkeypatch.setattr(A, "post_list", lambda: posts)
    monkeypatch.setattr(A, "static_audit", lambda p: static_result(p["id"], results[p["url"]]) | {"title": p["title"], "url": p["url"]})
    with pytest.raises(SystemExit) as ex:
        run_main(monkeypatch)
    assert ex.value.code == 1
    text = (out / "out" / "report.md").read_text()
    assert "posts audited: **4** · posts with at least one failure: **3**" in text
    order = [text.index(f"### {t}") for t in ("Blocker", "Major x2", "Minor only")]
    assert order == sorted(order) and "### Clean" not in text
    assert "- **MAJOR** `c` — d1" in text and "- **MAJOR** `c2`\n" in text
    assert text.index("`b`") < text.index("`a`", text.index("### Blocker"))                          # blocker listed before the minor
    assert "| BLOCKER | `b` | 1 | 1 |" in text and "| MINOR | `a` | 2 | 3 |" in text
    rep = json.loads((out / "out" / "report.json").read_text())
    assert [r["id"] for r in rep] == ["1", "2", "3", "4"]
    cap = capsys.readouterr().out
    assert "1 BLOCKER failures" in cap and "full report:" in cap and "fetching post list" in cap


def test_main_no_blockers_exits_normally(out, monkeypatch):
    monkeypatch.setattr(A, "post_list", lambda: [{"id": "1", "title": "T", "url": "u"}])
    monkeypatch.setattr(A, "static_audit", lambda p: static_result("1", [chk("a", "MAJOR", False)]) | {"title": "T"})
    run_main(monkeypatch)                                         # does not raise SystemExit


def test_main_limit_url_and_urls_file(out, monkeypatch, capsys):
    seen = []
    monkeypatch.setattr(A, "post_list", lambda: [{"id": str(i), "title": "t", "url": f"u{i}"} for i in range(5)])
    monkeypatch.setattr(A, "static_audit", lambda p: seen.append(p) or static_result(p["id"], [chk("a", "MINOR", True)]))
    run_main(monkeypatch, "--limit", "2")
    assert [p["id"] for p in seen] == ["0", "1"]
    seen.clear()
    run_main(monkeypatch, "--url", "https://b/some-post.html")
    assert seen[0]["id"] == hashlib.md5(b"https://b/some-post.html").hexdigest()[:8] and seen[0]["title"] == "some-post.html"
    seen.clear()
    f = out / "urls.txt"
    f.write_text("https://b/a\n\n  https://b/b  \n")
    run_main(monkeypatch, "--urls-file", str(f))
    assert [p["url"] for p in seen] == ["https://b/a", "https://b/b"] and "auditing 2 posts" in capsys.readouterr().out


def test_main_priority_keeps_only_posts_failing_both(out, monkeypatch):
    posts = [{"id": str(i), "title": "t", "url": f"u{i}"} for i in range(4)]
    combos = {"0": (False, False), "1": (False, True), "2": (True, False), "3": (True, True)}
    audited = []
    def sa(p):
        a, b = combos[p["id"]]
        audited.append(p["id"])
        return static_result(p["id"], [chk("no-inverted-media-query", "BLOCKER", a), chk("dark-vars-locked", "BLOCKER", b)])
    monkeypatch.setattr(A, "post_list", lambda: posts)
    monkeypatch.setattr(A, "static_audit", sa)
    with pytest.raises(SystemExit):
        run_main(monkeypatch, "--priority")
    rep = json.loads((out / "out" / "report.json").read_text())
    assert [r["id"] for r in rep] == ["0"] and audited.count("0") == 2 and audited.count("1") == 1


def test_main_rendered_adds_contrast_and_overflow_checks(out, monkeypatch):
    posts = [{"id": "1", "title": "T", "url": "u1"}]
    monkeypatch.setattr(A, "post_list", lambda: posts)
    monkeypatch.setattr(A, "static_audit", lambda p: static_result("1", []))
    rend = {("1", "light"): {"contrast": {"fails": 3, "checked": 10}, "overflow": {"pageOverflow": True, "docW": 900, "viewW": 800}},
            ("1", "dark"): {"contrast": {"fails": 0, "checked": 10}, "overflow": {"pageOverflow": False, "docW": 800, "viewW": 800}}}
    called = {}
    monkeypatch.setattr(A, "rendered_audit", lambda posts, baseline=False: called.update(b=baseline) or rend)
    with pytest.raises(SystemExit) as ex:
        run_main(monkeypatch, "--rendered")
    assert ex.value.code == 1 and called["b"] is False
    checks = {c["rule"]: c for c in json.loads((out / "out" / "report.json").read_text())[0]["checks"]}
    assert checks["contrast-light"]["detail"] == "3/10 nodes below 3:1" and not checks["contrast-light"]["ok"]
    assert checks["contrast-dark"]["detail"] == "0/10" and checks["contrast-dark"]["ok"]
    assert checks["no-overflow-light"]["detail"] == "doc 900px > view 800px" and checks["no-overflow-light"]["severity"] == "MINOR"
    assert checks["no-overflow-dark"]["ok"] and checks["no-overflow-dark"]["detail"] == ""


def test_main_baseline_implies_rendered_and_skips_errored_pages(out, monkeypatch):
    monkeypatch.setattr(A, "post_list", lambda: [{"id": "1", "title": "T", "url": "u1"}])
    monkeypatch.setattr(A, "static_audit", lambda p: static_result("1", []))
    got = {}
    monkeypatch.setattr(A, "rendered_audit", lambda posts, baseline=False: got.update(b=baseline) or {("1", "light"): {"error": "x"}})
    run_main(monkeypatch, "--baseline")
    assert got["b"] is True
    assert json.loads((out / "out" / "report.json").read_text())[0]["checks"] == []


def test_rendered_audit_with_fake_playwright(out, monkeypatch):
    shots, gotos = [], []

    class Page:
        def __init__(self, scheme, fail):
            self.scheme, self.fail = scheme, fail
        def goto(self, url, wait_until, timeout):
            if self.fail and "bad" in url:
                raise TimeoutError("slow page")
            gotos.append((self.scheme, url, wait_until, timeout))
        def wait_for_timeout(self, ms):
            pass
        def evaluate(self, js):
            return {"fails": 0, "checked": 1} if js == A.CONTRAST_JS else {"pageOverflow": False}
        def screenshot(self, path, full_page):
            shots.append((os.path.basename(path), full_page))

    class Ctx:
        def __init__(self, scheme):
            self.scheme = scheme
        def new_page(self):
            return Page(self.scheme, True)
        def close(self):
            pass

    class Browser:
        def new_context(self, viewport, color_scheme, user_agent):
            assert viewport == {"width": 1280, "height": 900} and user_agent == A.UA
            return Ctx(color_scheme)
        def close(self):
            pass

    class PW:
        chromium = types.SimpleNamespace(launch=lambda: Browser())
        def __enter__(self):
            return self
        def __exit__(self, *a):
            return False

    mod = types.ModuleType("playwright.sync_api")
    mod.sync_playwright = lambda: PW()
    monkeypatch.setitem(sys.modules, "playwright", types.ModuleType("playwright"))
    monkeypatch.setitem(sys.modules, "playwright.sync_api", mod)
    posts = [{"id": "1", "url": "https://b/ok"}, {"id": "2", "url": "https://b/bad"}]
    res = A.rendered_audit(posts, baseline=True)
    assert res[("1", "light")] == {"contrast": {"fails": 0, "checked": 1}, "overflow": {"pageOverflow": False}}
    assert res[("2", "dark")]["error"] == "TimeoutError: slow page"
    assert sorted(s[0] for s in shots) == ["1.dark.png", "1.light.png"] and all(s[1] for s in shots)
    assert os.path.isdir(A.SHOTS) and gotos[0][2:] == ("networkidle", 45000)
    shots.clear()
    A.rendered_audit(posts[:1], baseline=False)
    assert shots == []


# ========================================================================== fix
def test_strip_inverted_balanced_and_capped():
    src = f"a{INVERTED_MQ}:dark){{.x{{color:#ddd}}.y{{b:c}}}}z"
    out, n = FX.strip_inverted(src)
    assert n == 1 and out == "a/* gs-fix: removed inverted dark-mode block (it matched in LIGHT mode) */z"
    out, n = FX.strip_inverted("clean")
    assert (out, n) == ("clean", 0)
    out, n = FX.strip_inverted(INVERTED_MQ + ":dark) no brace")
    assert n == 0 and out.startswith(INVERTED_MQ)
    out, n = FX.strip_inverted((INVERTED_MQ + ":dark){.a{b:c}}") * 12)
    assert n == 9 and INVERTED_MQ in out                                  # stops after the 9th removal


def test_unsplice_disclaimer_primary_and_fallback():
    p = '<p class="disclaimer" data-gs-ai-disclosure-v1="1" style="x">AI note <a href="u">l</a></p>\n'
    src = f"<script>var h = '<div>body' + v + '{p}</div>';</script>"
    out, n = FX.unsplice_disclaimer(src)
    assert n == 1 and "disclaimer" not in out and out.endswith("</div>';</script>")
    # fallback: a spliced copy not directly before  </div>';
    src2 = f'<script>var s = "{p.strip()} other";</script><p>visible</p>'
    out, n = FX.unsplice_disclaimer(src2)
    assert n == 1 and "AI note" not in out and "<p>visible</p>" in out
    out, n = FX.unsplice_disclaimer("<p>none</p>")
    assert (out, n) == ("<p>none</p>", 0)
    # a disclaimer outside any script is left alone by the fallback
    keep = f"<p>{p.strip()}</p>"
    assert FX.unsplice_disclaimer(keep) == (keep, 0)


def test_light_lock_sources_and_idempotence():
    src = '<style>:root{--bg:#fff;--ink:#111}:root[data-theme="light"]{--bg:#eee;--x: #123 }</style>'
    lock = FX.light_lock(src)
    assert "--bg:#eee!important;--x:#123!important;" in lock and "--ink" not in lock          # data-theme="light" wins
    assert lock.startswith("\n<style>/*gs-light-lock-v1*/") and "color-scheme:light!important" in lock
    plain = FX.light_lock("<style>:root{--a:#fff;--b:rgb(1,2,3)}</style>")
    assert "--a:#fff!important;--b:rgb(1,2,3)!important;" in plain
    assert FX.light_lock("x gs-light-lock-v1") == ""
    assert FX.light_lock("<style>p{}</style>") == "" and FX.light_lock("<style>:root{ }</style>") == ""


@pytest.mark.parametrize("c,want", [("#000", 0.0), ("#fff", 1.0), ("#ff0000", 0.2126), ("rgb(0,255,0)", 0.7152), ("rgba(0 , 0, 255, .3)", 0.0722),
                                   ("#12", None), ("#zzzzzz", None), ("blue", None), ("rgb(1,2)", None), ("rgb(a,b,c)", None)])
def test_lum(c, want):
    got = FX._lum(c)
    assert (got is None) if want is None else got == pytest.approx(want, abs=1e-4)


@pytest.mark.parametrize("sel,want", [
    ("body", False), ("HTML", False), (":root", False), ("*", False), ("select", False), (".post-body", False), (".artx", False),
    ("article", False), ("main", False), ("div", False), ("section", False), (".hero", True), ("#top", True), (".a .b", True),
    ("div p", True), ("a[href]", True), ("li:first-child", True), (".post-body >", False), ("  .hero  ", True),
])
def test_is_panel(sel, want):
    assert FX._is_panel(sel) is want


@pytest.fixture
def themeless(monkeypatch):
    monkeypatch.setattr(FX, "theme_css", lambda: "")


def test_dark_panel_guard_emits_resolved_colours(themeless):
    src = ("<style>:root{--panel:#101820}.hero{background:var(--panel)}.card,.big-card{background:#222}.light{background:#fff}"
           "body{background:#000}@media x{.m{background:#000}}</style>")
    g = FX.dark_panel_guard(src)
    assert g.startswith("\n<style>/*gs-dark-panel-guard*/")
    assert ".hero{background:#101820!important}" in g and ".hero,.hero *{color:#fff!important}" in g
    assert ".hero a,.hero a *{color:#cfe3ff!important}" in g
    assert ".card{background:#222!important}" in g and ".big-card{background:#222!important}" in g
    assert ".light" not in g and "body" not in g and ".m{" not in g and "var(" not in g


def test_dark_panel_guard_edge_cases(themeless):
    assert FX.dark_panel_guard("<p>no style</p>") == ""
    assert FX.dark_panel_guard("<style>.x{color:red}</style>") == ""
    assert FX.dark_panel_guard("<style>.x{background:#fff}</style>") == ""
    assert FX.dark_panel_guard("<style>.x{background:red}</style>") == ""            # named colours are not judged
    assert FX.dark_panel_guard("<style>:root .y{background:#000}</style>") == ""
    long_sel = "." + "a" * 80
    assert FX.dark_panel_guard(f"<style>{long_sel}{{background:#000}}</style>") == ""
    dup = FX.dark_panel_guard("<style>.d{background:#000}.d{background:#001}</style>")
    assert dup.count(".d{background") == 1
    mid = FX.dark_panel_guard("<style>.edge{background:#6b6b6b}.notdark{background:#6c6c6c}</style>")
    assert ".edge{" in mid and ".notdark" not in mid
    grad = FX.dark_panel_guard("<style>.g{background:linear-gradient(#000,#fff)}</style>")
    assert grad == ""                                                                  # mean luminance 0.5 is not dark
    avg = FX.dark_panel_guard("<style>.g{background:linear-gradient(#000,#444)}</style>")
    assert ".g{background:linear-gradient(#000,#444)!important}" in avg


def test_dark_panel_guard_uses_theme_variables(monkeypatch):
    monkeypatch.setattr(FX, "theme_css", lambda: ".t{--h1:#0a0a0a}")
    g = FX.dark_panel_guard("<style>.hero{background:var(--h1)}</style>")
    assert ".hero{background:#0a0a0a!important}" in g
    deep = FX.dark_panel_guard("<style>:root{--a:var(--b);--b:var(--c);--c:var(--d);--d:var(--e);--e:#000}.x{background:var(--a)}</style>")
    assert deep == ""                                                                  # more than 3 hops stay unresolved


def test_add_translate_placement():
    out, added = FX.add_translate('<div class="artx wide"><p>x</p></div>')
    assert added and out.startswith('<div class="artx wide">\n<div id="google_translate_element"')
    out, added = FX.add_translate("<div class='post-body'><p>x</p></div>")
    assert added and out.startswith("<div class='post-body'>\n<div id=")
    out, added = FX.add_translate("<p>bare</p>")
    assert added and out.startswith("<div id=\"google_translate_element\"") and out.endswith("\n<p>bare</p>")
    assert FX.add_translate("has google_translate_element already") == ("has google_translate_element already", False)
    out, _ = FX.add_translate('<div class="wrapper"><div class="artx">y</div></div>')
    assert out.startswith('<div class="wrapper">\n<div id=') or 'class="artx">\n<div id=' in out
    out, _ = FX.add_translate('<div class="notartx">z</div>')
    assert out.startswith("<div id=")                                                  # \b boundary: "notartx" is not a wrapper class


def test_repair_end_to_end_notes_and_idempotence(themeless):
    body = (f"<div class='post-body'><style>:root{{--bg:#fff}}.hero{{background:#101820}}{INVERTED_MQ}:dark){{.x{{color:#ddd}}}}</style>"
            "<script>var h='<div>' + v + '" + '<p class="disclaimer" data-gs-ai-disclosure-v1="1">AI</p>\n' + "</div>';</script></div>")
    fixed, notes = FX.repair(body)
    assert notes[0] == "removed 1 inverted media-query block(s)" and notes[1] == "lifted 1 disclaimer(s) out of <script>"
    assert "appended light-lock from the post's own :root" in notes and any(n.startswith("dark-panel guard") for n in notes)
    assert "added Google Translate widget" in notes and notes[-1] == "appended AI disclosure at end of body"
    assert INVERTED_MQ not in fixed and "gs-light-lock-v1" in fixed and "gs-dark-panel-guard" in fixed
    assert fixed.endswith(FX.DISCLAIMER)
    assert FX.static_pass(fixed) == ["index-link"]          # repair() does not add the index link; add_index_link.py does
    again, notes2 = FX.repair(fixed)
    assert notes2 == [] and again == fixed


def test_static_pass_reports_failing_rule_names(monkeypatch):
    monkeypatch.setattr(FX, "STATIC_RULES", [("a", "B", lambda body, node_check: (True, "")), ("b", "B", lambda body, node_check: (False, "")),
                                              ("c", "B", lambda body, node_check: 1 / 0)])
    assert FX.static_pass("x") == ["b", "c"]
    assert FX.static_pass.__name__ == "static_pass"


def test_theme_css_extraction_and_cache(monkeypatch):
    FX._THEME_CACHE.clear()
    calls = []
    monkeypatch.setattr(FX, "sh", lambda c: calls.append(c) or "<style id='page-skin-1' type='text/css'><!-- a{b:c} --></style><style>other{}</style>")
    assert FX.theme_css() == " a{b:c} "
    FX.theme_css()
    assert len(calls) == 1
    FX._THEME_CACHE.clear()
    monkeypatch.setattr(FX, "sh", lambda c: "".join(f"<style>s{i}{{}}</style>" for i in range(5)))
    assert FX.theme_css() == "s0{}\ns1{}\ns2{}"
    FX._THEME_CACHE.clear()


def test_serve_handler_quiet_and_serves_directory(tmp_path):
    import urllib.request
    (tmp_path / "f.txt").write_text("hello")
    httpd = FX.serve(str(tmp_path), 0)
    try:
        port = httpd.server_address[1]
        assert urllib.request.urlopen(f"http://127.0.0.1:{port}/f.txt", timeout=5).read() == b"hello"
    finally:
        httpd.shutdown()
        httpd.server_close()
    assert FX._Q.log_message(None) is None


def fake_playwright(monkeypatch, fails_by_url):
    """Page.evaluate(CONTRAST_JS) returns the next scripted result; the swap script returns True."""
    state = {"swapped": [], "n": 0}

    class Page:
        def goto(self, url, **kw):
            self.url = url
            if "error" in url:
                raise RuntimeError("nav")
        def wait_for_timeout(self, ms):
            pass
        def evaluate(self, js, arg=None):
            if js == FX.CONTRAST_JS:
                seq = fails_by_url[self.url]
                state["n"] += 1
                return {"fails": seq.pop(0), "checked": 10}
            state["swapped"].append(arg)
            return True

    class Ctx:
        def new_page(self):
            return Page()

    class Browser:
        def new_context(self, **kw):
            return Ctx()
        def close(self):
            pass

    class PW:
        chromium = types.SimpleNamespace(launch=lambda: Browser())
        def __enter__(self):
            return self
        def __exit__(self, *a):
            return False
    mod = types.ModuleType("playwright.sync_api")
    mod.sync_playwright = lambda: PW()
    monkeypatch.setitem(sys.modules, "playwright", types.ModuleType("playwright"))
    monkeypatch.setitem(sys.modules, "playwright.sync_api", mod)
    return state


def test_verify_live_swaps_repaired_body_and_isolates_failures(monkeypatch):
    st = fake_playwright(monkeypatch, {"https://b/a": [5, 0], "https://b/c": [0, 0]})
    meta = [{"id": "a", "url": "https://b/a"}, {"id": "e", "url": "https://b/error"}, {"id": "c", "url": "https://b/c"}]
    pairs = [("a", "old", "FIXED-A"), ("e", "old", "FIXED-E"), ("c", "old", "FIXED-C")]
    res = FX.verify_live(meta, pairs)
    assert res["a"] == ({"fails": 5, "checked": 10}, {"fails": 0, "checked": 10})
    assert res["e"] == ({"fails": -1, "checked": 0}, {"fails": -1, "checked": 0})
    assert res["c"][0]["fails"] == 0 and st["swapped"] == ["FIXED-A", "FIXED-C"]


def test_verify_offline_harness_writes_pages_and_measures(monkeypatch, tmp_path):
    monkeypatch.setattr(FX, "FIXES", str(tmp_path))
    monkeypatch.setattr(FX, "theme_css", lambda: "THEMECSS")
    served = {}
    class H:
        def shutdown(self):
            served["down"] = True
    monkeypatch.setattr(FX, "serve", lambda d, port: served.update(d=d, port=port) or H())
    fake_playwright(monkeypatch, {"http://127.0.0.1:8901/p.before.html": [4], "http://127.0.0.1:8901/p.after.html": [1],
                                  "http://127.0.0.1:8901/error.before.html": [0]})
    res = FX.verify([("p", "BEFORE", "AFTER"), ("error", "b", "a")])
    assert res["p"] == ({"fails": 4, "checked": 10}, {"fails": 1, "checked": 10})
    assert res["error"][0]["fails"] == -1 and served["down"] and served["port"] == 8901
    page = (tmp_path / "_verify" / "p.after.html").read_text()
    assert "THEMECSS" in page and "<div class='post-body'>AFTER</div>" in page


def test_contrast_of_helper():
    class P:
        def goto(self, url, wait_until, timeout):
            self.u = (url, wait_until, timeout)
        def wait_for_timeout(self, ms):
            pass
        def evaluate(self, js):
            return js
    p = P()
    assert FX.contrast_of(p, "http://x") == FX.CONTRAST_JS and p.u == ("http://x", "load", 30000)


def run_fix(monkeypatch, *argv):
    monkeypatch.setattr(FX.sys, "argv", ["fix.py", *argv])
    FX.main()


@pytest.fixture
def fixenv(tmp_path, monkeypatch):
    monkeypatch.setattr(FX, "FIXES", str(tmp_path / "fixes"))
    monkeypatch.setattr(FX, "theme_css", lambda: "")
    pages = {"https://b/2026/01/good.html": "<html><div class='post-body'><p>hi</p></div></html>",
             "https://b/2026/01/empty.html": "<html>no body</html>"}
    monkeypatch.setattr(FX, "sh", lambda c: pages.get(c[-1], ""))
    return tmp_path


def test_main_url_writes_fix_manifest_and_reports(fixenv, monkeypatch, capsys):
    run_fix(monkeypatch, "--url", "https://b/2026/01/good.html", "--no-verify")
    out = capsys.readouterr().out
    assert "repairing 1 posts" in out and "Nothing was uploaded" in out
    body = (fixenv / "fixes" / "good.html").read_text()
    assert "gs-light-lock" not in body and "google_translate_element" in body and body.endswith(FX.DISCLAIMER)
    meta = json.loads((fixenv / "fixes" / "manifest.json").read_text())
    assert meta[0]["slug"] == "good" and meta[0]["id"] == hashlib.md5(b"https://b/2026/01/good.html").hexdigest()[:8]
    assert "added Google Translate widget" in meta[0]["notes"] and "disclaimer-present" in meta[0]["before"] and meta[0]["after"] == ["index-link"]


def test_main_urls_file_skips_unfetchable_and_verifies(fixenv, monkeypatch, capsys):
    f = fixenv / "u.txt"
    f.write_text("https://b/2026/01/good.html\n\nhttps://b/2026/01/empty.html\n")
    seen = {}
    def verify_live(meta, pairs):
        seen["meta"], seen["pairs"] = meta, pairs
        return {meta[0]["id"]: ({"fails": 4}, {"fails": 0})}
    monkeypatch.setattr(FX, "verify_live", verify_live)
    run_fix(monkeypatch, "--urls-file", str(f))
    out = capsys.readouterr().out
    assert "!! could not extract body: https://b/2026/01/empty.html" in out and "repairing 2 posts" in out
    assert len(seen["pairs"]) == 1 and "FIXED" in out and "all repaired" in out
    assert json.loads((fixenv / "fixes" / "manifest.json").read_text())[0]["contrast_after"] == 0


@pytest.mark.parametrize("before,after,verdict,allgood", [
    (0, 0, "already clean", True), (5, 0, "FIXED", True), (5, 2, "improved (3 fewer)", False),
    (5, 5, "NOT FIXED", False), (2, 7, "NOT FIXED", False), (3, -1, "render error", True),
])
def test_main_verdict_table(fixenv, monkeypatch, capsys, before, after, verdict, allgood):
    monkeypatch.setattr(FX, "verify_live", lambda meta, pairs: {meta[0]["id"]: ({"fails": before}, {"fails": after})})
    run_fix(monkeypatch, "--url", "https://b/2026/01/good.html")
    out = capsys.readouterr().out
    assert verdict in out and ("all repaired" in out) is allgood and ("some posts need manual attention" in out) is (not allgood)


def test_main_no_verify_skips_browser(fixenv, monkeypatch):
    monkeypatch.setattr(FX, "verify_live", lambda *a: pytest.fail("browser used"))
    run_fix(monkeypatch, "--url", "https://b/2026/01/good.html", "--no-verify")

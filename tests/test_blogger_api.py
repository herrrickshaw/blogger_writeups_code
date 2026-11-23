"""Offline tests for tools/blogger_api.py. The Blogger API, OAuth and curl are faked
completely; nothing here can reach a real blog or credential."""
import argparse
import io
import json
import types
import urllib.error

import pytest

import blogger_api as b


class Fake:
    """In-memory Blogger: records every call made through b.api."""

    def __init__(self):
        self.calls = []
        self.posts = {}
        self.pages = {}
        self.fail = {}  # (method, path-prefix) -> exception to raise

    def add(self, pid, title="T", slug=None, status="LIVE", content="<p>x</p>", **kw):
        slug = slug or pid
        self.posts[pid] = dict(id=pid, title=title, status=status, content=content,
                               url=f"https://blog.example/2026/01/{slug}.html", **kw)
        return self.posts[pid]

    def api(self, path, data=None, method="GET"):
        self.calls.append((method, path, data))
        for (m, prefix), exc in self.fail.items():
            if m == method and path.startswith(prefix):
                raise exc
        base = f"/blogs/{b.BLOG_ID}"
        if method == "GET" and path.startswith(base + "/posts?"):
            q = path.split("?", 1)[1]
            status = "DRAFT" if "status=draft" in q else "LIVE"
            if "status=live" in q or "status=LIVE" in q:
                status = "LIVE"
            items = [p for p in self.posts.values() if p["status"] == status]
            return {"items": items}
        if method == "GET" and path.startswith(base + "/pages"):
            return {"items": list(self.pages.values())}
        if path.startswith(base + "/posts/"):
            rest = path[len(base + "/posts/"):]
            pid = rest.split("?")[0].split("/")[0]
            if method == "GET":
                return self.posts[pid]
            if method == "PUT":
                self.posts[pid].update(data)
                return self.posts[pid]
            if method == "DELETE":
                del self.posts[pid]
                return {}
            if method == "POST" and rest.endswith("/publish"):
                self.posts[pid]["status"] = "LIVE"
                return self.posts[pid]
            if method == "POST" and rest.endswith("/revert"):
                self.posts[pid]["status"] = "DRAFT"
                return self.posts[pid]
        if method == "POST" and path.startswith(base + "/posts"):
            pid = f"new{len(self.posts)}"
            p = self.add(pid, title=data["title"], content=data["content"],
                         status="DRAFT" if "isDraft=true" in path else "LIVE")
            if p["status"] == "DRAFT":
                del p["url"]
            return p
        if path.startswith(base + "/pages"):
            if method == "POST":
                return {"id": "pg9", "url": "https://blog.example/p/x.html", "content": data["content"]}
            if method == "PUT":
                return {"id": data["id"], "url": "https://blog.example/p/x.html", "content": data["content"]}
        if path == base:
            return {"name": "Blog", "url": "https://blog.example", "posts": {"totalItems": 7}, "pages": {"totalItems": 2}}
        raise AssertionError(f"unexpected call {method} {path}")

    def writes(self):
        return [c for c in self.calls if c[0] != "GET"]


@pytest.fixture
def fake(monkeypatch):
    f = Fake()
    monkeypatch.setattr(b, "api", f.api)
    monkeypatch.setattr(b.time, "sleep", lambda s: None)
    # verify_live: pretend the public page renders whatever the fake stored
    f.live_html = None
    def fake_verify(url, needle=None, absent=None):
        if f.live_html == "":
            return False, "empty response"
        return True, "ok bytes"
    monkeypatch.setattr(b, "verify_live", fake_verify)
    return f


def ns(**kw):
    d = dict(slug=None, id=None, file=None, title=None, dry_run=False, out=None, yes=False,
             draft=False, allow_duplicate=False, limit=0, drafts=False, manifest=None,
             delete_newer=False)
    d.update(kw)
    return argparse.Namespace(**d)


# ----------------------------------------------------------------- transport
class _Resp:
    def __init__(self, text):
        self.text = text
    def read(self):
        return self.text.encode()
    def __enter__(self):
        return self
    def __exit__(self, *a):
        return False


def test_req_encodes_dict_as_json_and_bytes_untouched(monkeypatch):
    seen = []
    def urlopen(r, timeout=None):
        seen.append((r.data, r.get_method(), r.full_url, timeout))
        return _Resp('{"a": 1}')
    monkeypatch.setattr(b.urllib.request, "urlopen", urlopen)
    assert b._req("http://x/", data={"k": "v"}) == {"a": 1}
    assert b._req("http://x/", data=b"raw", method="PUT") == {"a": 1}
    assert b._req("http://x/") == {"a": 1}
    assert seen[0][0] == b'{"k": "v"}' and seen[0][1] == "POST"
    assert seen[1][0] == b"raw" and seen[1][1] == "PUT"
    assert seen[2][0] is None and seen[2][1] == "GET" and seen[2][3] == 60


def test_req_empty_body_is_empty_dict(monkeypatch):
    monkeypatch.setattr(b.urllib.request, "urlopen", lambda r, timeout=None: _Resp(""))
    assert b._req("http://x/") == {}


def test_form_urlencodes_fields(monkeypatch):
    got = {}
    monkeypatch.setattr(b, "_req", lambda url, data=None, headers=None, method=None: got.update(url=url, data=data, headers=headers) or {})
    b._form("http://t/", {"a": "b c", "d": "e"})
    assert got["data"] == b"a=b+c&d=e"
    assert got["headers"] == {"Content-Type": "application/x-www-form-urlencoded"}


# ---------------------------------------------------------------------- auth
def test_client_missing_file_exits(monkeypatch, tmp_path):
    monkeypatch.setattr(b, "CLIENT_FILE", tmp_path / "none.json")
    with pytest.raises(SystemExit) as e:
        b._client()
    assert "missing" in str(e.value)


@pytest.mark.parametrize("kind", ["installed", "web"])
def test_client_reads_both_kinds(monkeypatch, tmp_path, kind):
    p = tmp_path / "c.json"
    p.write_text(json.dumps({kind: {"client_id": "id", "client_secret": "sec"}}))
    monkeypatch.setattr(b, "CLIENT_FILE", p)
    assert b._client() == ("id", "sec", kind)


def test_client_rejects_other_json(monkeypatch, tmp_path):
    p = tmp_path / "c.json"
    p.write_text("{}")
    monkeypatch.setattr(b, "CLIENT_FILE", p)
    with pytest.raises(SystemExit) as e:
        b._client()
    assert "not an OAuth client" in str(e.value)


@pytest.fixture
def tokenenv(monkeypatch, tmp_path):
    monkeypatch.delenv("BLOGGER_ACCESS_TOKEN", raising=False)
    monkeypatch.setattr(b, "SECRETS", tmp_path / "sec")
    monkeypatch.setattr(b, "CLIENT_FILE", tmp_path / "client.json")
    monkeypatch.setattr(b, "TOKEN_FILE", tmp_path / "sec" / "tok.json")
    monkeypatch.setitem(b._access, "token", None)
    monkeypatch.setitem(b._access, "expires", 0)
    (tmp_path / "client.json").write_text(json.dumps({"installed": {"client_id": "i", "client_secret": "s"}}))
    return tmp_path


def test_access_token_env_placeholder(tokenenv, monkeypatch):
    monkeypatch.setenv("BLOGGER_ACCESS_TOKEN", "placeholder")
    assert b.access_token() == "placeholder"


def test_access_token_requires_token_file(tokenenv):
    with pytest.raises(SystemExit) as e:
        b.access_token()
    assert "not authorised" in str(e.value)


def test_access_token_refreshes_and_caches(tokenenv, monkeypatch):
    b.SECRETS.mkdir()
    b.TOKEN_FILE.write_text(json.dumps({"refresh_token": "rt"}))
    calls = []
    def form(url, fields):
        calls.append(fields)
        return {"access_token": "AT", "expires_in": 3600}
    monkeypatch.setattr(b, "_form", form)
    now = [1000.0]
    monkeypatch.setattr(b.time, "time", lambda: now[0])
    assert b.access_token() == "AT"
    assert calls[0]["grant_type"] == "refresh_token" and calls[0]["refresh_token"] == "rt"
    assert b.access_token() == "AT" and len(calls) == 1          # cached
    now[0] = 1000 + 3600 - 61                                      # 61s before expiry: still cached
    assert b.access_token() == "AT" and len(calls) == 1
    now[0] = 1000 + 3600 - 59                                      # inside the 60s margin: refresh
    b.access_token()
    assert len(calls) == 2


def test_access_token_default_expiry_one_hour(tokenenv, monkeypatch):
    b.SECRETS.mkdir()
    b.TOKEN_FILE.write_text(json.dumps({"refresh_token": "rt"}))
    monkeypatch.setattr(b, "_form", lambda u, f: {"access_token": "AT"})
    monkeypatch.setattr(b.time, "time", lambda: 0.0)
    b.access_token()
    assert b._access["expires"] == 3600


class _ImmediateThread:
    def __init__(self, target=None, daemon=None):
        self.target = target
    def start(self):
        self.target()


def _fake_server(monkeypatch, query, port_error=False):
    """Replace HTTPServer so handle_request replays one browser callback."""
    created = {}

    class Srv:
        def __init__(self, addr, handler):
            if port_error:
                raise OSError("in use")
            created["addr"] = addr
            self.handler = handler
        def handle_request(self):
            h = types.SimpleNamespace(path="/?" + query, wfile=io.BytesIO(),
                                      send_response=lambda c: created.setdefault("code", c),
                                      send_header=lambda *a: None, end_headers=lambda: None)
            self.handler.do_GET(h)
            self.handler.log_message(h)
            created["body"] = h.wfile.getvalue()
        def server_close(self):
            created["closed"] = True
    monkeypatch.setattr(b.http.server, "HTTPServer", Srv)
    monkeypatch.setattr(b.threading, "Thread", _ImmediateThread)
    monkeypatch.setattr(b.webbrowser, "open", lambda u: created.setdefault("opened", u))
    return created


def test_cmd_auth_happy_path_saves_refresh_token_mode_600(tokenenv, monkeypatch, capsys):
    monkeypatch.setattr(b.secrets, "token_urlsafe", lambda n: "STATE")
    created = _fake_server(monkeypatch, "code=CODE&state=STATE")
    posted = {}
    monkeypatch.setattr(b, "_form", lambda url, fields: posted.update(fields) or {"refresh_token": "RT"})
    b.cmd_auth(ns(port=0))
    assert created["addr"] == ("127.0.0.1", b.DEFAULT_PORT)
    assert created["code"] == 200 and b"Authorised" in created["body"]
    assert "state=STATE" in created["opened"]
    assert posted["code"] == "CODE" and posted["redirect_uri"] == f"http://127.0.0.1:{b.DEFAULT_PORT}"
    assert json.loads(b.TOKEN_FILE.read_text()) == {"refresh_token": "RT"}
    assert oct(b.TOKEN_FILE.stat().st_mode & 0o777) == "0o600"
    assert created["closed"]
    assert "saved" in capsys.readouterr().out


def test_cmd_auth_custom_port_used(tokenenv, monkeypatch):
    monkeypatch.setattr(b.secrets, "token_urlsafe", lambda n: "S")
    created = _fake_server(monkeypatch, "code=C&state=S")
    monkeypatch.setattr(b, "_form", lambda u, f: {"refresh_token": "R"})
    b.cmd_auth(ns(port=9999))
    assert created["addr"][1] == 9999


def test_cmd_auth_state_mismatch_aborts(tokenenv, monkeypatch):
    monkeypatch.setattr(b.secrets, "token_urlsafe", lambda n: "STATE")
    _fake_server(monkeypatch, "code=C&state=EVIL")
    with pytest.raises(SystemExit) as e:
        b.cmd_auth(ns(port=0))
    assert "state mismatch" in str(e.value)
    assert not b.TOKEN_FILE.exists()


def test_cmd_auth_no_code_aborts(tokenenv, monkeypatch):
    monkeypatch.setattr(b.secrets, "token_urlsafe", lambda n: "S")
    _fake_server(monkeypatch, "state=S&error=denied")
    with pytest.raises(SystemExit) as e:
        b.cmd_auth(ns(port=0))
    assert "no authorisation code" in str(e.value)


def test_cmd_auth_no_refresh_token_aborts(tokenenv, monkeypatch):
    monkeypatch.setattr(b.secrets, "token_urlsafe", lambda n: "S")
    _fake_server(monkeypatch, "code=C&state=S")
    monkeypatch.setattr(b, "_form", lambda u, f: {"access_token": "only"})
    with pytest.raises(SystemExit) as e:
        b.cmd_auth(ns(port=0))
    assert "no refresh_token" in str(e.value)
    assert not b.TOKEN_FILE.exists()


def test_cmd_auth_port_bind_failure(tokenenv, monkeypatch):
    _fake_server(monkeypatch, "", port_error=True)
    with pytest.raises(SystemExit) as e:
        b.cmd_auth(ns(port=1))
    assert "cannot bind port 1" in str(e.value)


def test_cmd_auth_web_client_prompts_for_redirect(tokenenv, monkeypatch, capsys):
    (tokenenv / "client.json").write_text(json.dumps({"web": {"client_id": "i", "client_secret": "s"}}))
    monkeypatch.setattr(b.secrets, "token_urlsafe", lambda n: "S")
    _fake_server(monkeypatch, "code=C&state=S")
    prompted = []
    monkeypatch.setattr("builtins.input", lambda p="": prompted.append(p) or "")
    monkeypatch.setattr(b, "_form", lambda u, f: {"refresh_token": "R"})
    b.cmd_auth(ns(port=0))
    out = capsys.readouterr().out
    assert "WEB OAuth client" in out and "http://127.0.0.1:8765" in out
    assert prompted


def test_cmd_auth_browser_failure_is_ignored(tokenenv, monkeypatch):
    monkeypatch.setattr(b.secrets, "token_urlsafe", lambda n: "S")
    _fake_server(monkeypatch, "code=C&state=S")
    def boom(u):
        raise RuntimeError("no browser")
    monkeypatch.setattr(b.webbrowser, "open", boom)
    monkeypatch.setattr(b, "_form", lambda u, f: {"refresh_token": "R"})
    b.cmd_auth(ns(port=0))
    assert b.TOKEN_FILE.exists()


# ------------------------------------------------------------------- api()
def _http_error(code, body="detail"):
    return urllib.error.HTTPError("u", code, "m", {}, io.BytesIO(body.encode()))


@pytest.fixture
def apienv(monkeypatch):
    monkeypatch.setenv("BLOGGER_ACCESS_TOKEN", "placeholder")
    sleeps = []
    monkeypatch.setattr(b.time, "sleep", lambda s: sleeps.append(s))
    monkeypatch.setattr(b.random, "uniform", lambda a, c: 0.0)
    return sleeps


def test_api_success_sends_bearer_and_url(apienv, monkeypatch):
    seen = {}
    def req(url, data=None, headers=None, method=None):
        seen.update(url=url, data=data, headers=headers, method=method)
        return {"ok": 1}
    monkeypatch.setattr(b, "_req", req)
    assert b.api("/blogs/1", data={"x": 1}, method="PUT") == {"ok": 1}
    assert seen["url"] == b.API + "/blogs/1"
    assert seen["headers"]["Authorization"] == "Bearer placeholder"
    assert seen["method"] == "PUT"


@pytest.mark.parametrize("code", [403, 429, 500, 503])
def test_api_retries_transient_codes_then_succeeds(apienv, monkeypatch, code):
    attempts = []
    def req(*a, **k):
        attempts.append(1)
        if len(attempts) < 3:
            raise _http_error(code)
        return {"done": True}
    monkeypatch.setattr(b, "_req", req)
    assert b.api("/p") == {"done": True}
    assert apienv == [1.0, 2.0]          # exponential backoff, no jitter here


def test_api_persistent_403_raises_ceiling_after_64s_backoff(apienv, monkeypatch):
    monkeypatch.setattr(b, "_req", lambda *a, **k: (_ for _ in ()).throw(_http_error(403, "quota")))
    with pytest.raises(b.Ceiling) as e:
        b.api("/p")
    assert apienv == [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0]
    assert "403 quota" in str(e.value)


def test_api_jitter_added_to_wait(apienv, monkeypatch):
    monkeypatch.setattr(b.random, "uniform", lambda a, c: 0.25)
    n = []
    def req(*a, **k):
        n.append(1)
        if len(n) == 1:
            raise _http_error(500)
        return {}
    monkeypatch.setattr(b, "_req", req)
    b.api("/p")
    assert apienv == [1.25]


@pytest.mark.parametrize("code", [400, 401, 404])
def test_api_non_transient_error_exits_immediately(apienv, monkeypatch, code):
    monkeypatch.setattr(b, "_req", lambda *a, **k: (_ for _ in ()).throw(_http_error(code, "nope")))
    with pytest.raises(SystemExit) as e:
        b.api("/p")
    assert f"HTTP {code}: nope" in str(e.value)
    assert apienv == []


def test_api_truncates_error_detail_to_300(apienv, monkeypatch):
    monkeypatch.setattr(b, "_req", lambda *a, **k: (_ for _ in ()).throw(_http_error(400, "z" * 500)))
    with pytest.raises(SystemExit) as e:
        b.api("/p")
    assert str(e.value) == "HTTP 400: " + "z" * 300


# ------------------------------------------------------------- pure helpers
def test_flatten_html_strips_script_style_tags_and_unescapes():
    raw = "<p>Hello&nbsp;<b>wor</b>ld</p><script>var a='<p>no</p>';</script><STYLE>p{}</STYLE> &amp; &#8212; x"
    assert b._flatten_html(raw) == "Hello\xa0 wor ld & — x"


def test_flatten_html_limit():
    assert b._flatten_html("<p>abcdefgh</p>", limit=3) == "abc"
    assert b._flatten_html("<p>abc</p>", limit=None) == "abc"
    assert b._flatten_html("<p>abc</p>", limit=0) == "abc"   # falsy limit means no limit


def test_verify_stored_match_and_mismatch():
    ok, msg = b.verify_stored("<p>Hello <b>world</b></p>", "Hello world")
    assert ok and "via API" in msg and "25 bytes" in msg
    ok, msg = b.verify_stored("<p>other</p>", "Hello")
    assert not ok and "does not contain" in msg
    ok, _ = b.verify_stored(None, "")      # empty probe is trivially contained
    assert ok


@pytest.fixture
def curl(monkeypatch):
    out = {"stdout": ""}
    cmds = []
    def run(cmd, capture_output, text):
        cmds.append(cmd)
        return types.SimpleNamespace(stdout=out["stdout"])
    monkeypatch.setattr(b.subprocess, "run", run)
    return out, cmds


def test_verify_live_empty_response(curl):
    out, cmds = curl
    assert b.verify_live("https://x/p.html") == (False, "empty response")
    assert cmds[0][0] == "curl" and cmds[0][-1].startswith("https://x/p.html?cb=")


def test_verify_live_needle_raw_flat_and_missing(curl):
    out, _ = curl
    out["stdout"] = "<p>Alpha &#8212; <b>beta</b></p>"
    assert b.verify_live("u", needle="Alpha")[0]
    assert b.verify_live("u", needle="Alpha — beta")[0]            # only via flattened form
    ok, why = b.verify_live("u", needle="gamma")
    assert (ok, why) == (False, "expected content missing")


def test_verify_live_absent_checks(curl):
    out, _ = curl
    out["stdout"] = "<p>Alpha beta</p>"
    ok, why = b.verify_live("u", absent="Alpha")
    assert (ok, why) == (False, "content that should be gone is still present")
    assert b.verify_live("u", absent="<i>Alpha</i> beta")[0] is False    # flat match
    ok, why = b.verify_live("u", absent="zzz")
    assert (ok, why) == (True, "17 bytes")
    assert b.verify_live("u")[0]


# ---------------------------------------------------------------- commands
def test_find_post_paginates_and_matches_exact_slug(fake, monkeypatch):
    pages = [
        {"items": [{"id": "1", "url": "https://b/2026/01/other.html"}], "nextPageToken": "T2"},
        {"items": [{"id": "2", "url": "https://b/2026/01/target.html"}]},
    ]
    qs = []
    def api(path, data=None, method="GET"):
        qs.append(path)
        return pages.pop(0)
    monkeypatch.setattr(b, "api", api)
    assert b.find_post("target")["id"] == "2"
    assert "pageToken=T2" in qs[1] and "pageToken" not in qs[0]
    assert "maxResults=100" in qs[0] and "status=LIVE" in qs[0]


def test_find_post_not_found_exits_with_count(monkeypatch):
    monkeypatch.setattr(b, "api", lambda p, **k: {"items": [{"id": "1", "url": "https://b/x/a.html"}, {"id": "2", "url": "https://b/x/b.html"}]})
    with pytest.raises(SystemExit) as e:
        b.find_post("zzz")
    assert "'zzz'" in str(e.value) and "searched 2" in str(e.value)


def test_find_post_does_not_match_suffix_slug(monkeypatch):
    monkeypatch.setattr(b, "api", lambda p, **k: {"items": [{"id": "1", "url": "https://b/x/prefix-target.html"}]})
    with pytest.raises(SystemExit):
        b.find_post("target")


def test_cmd_whoami(fake, capsys):
    b.cmd_whoami(None)
    out = capsys.readouterr().out
    assert "blog   : Blog" in out and "posts  : 7   pages: 2" in out


def test_cmd_get_prints_and_writes(fake, tmp_path, capsys):
    fake.add("p1", title="Hello", slug="hello", content="<p>body</p>", updated="2026-01-01")
    out = tmp_path / "o.html"
    b.cmd_get(ns(slug="hello", out=str(out)))
    text = capsys.readouterr().out
    assert "id     : p1" in text and "bytes  : 11" in text and f"wrote  : {out}" in text
    assert out.read_text() == "<p>body</p>"


def test_cmd_get_without_out(fake, tmp_path, capsys):
    fake.add("p1", slug="hello", updated="u")
    b.cmd_get(ns(slug="hello"))
    assert "wrote" not in capsys.readouterr().out


def test_do_update_dry_run_makes_no_calls(fake, capsys):
    assert b.do_update("p", "u", "t", "<p>abc</p>", dry_run=True) is True
    assert fake.calls == []
    assert "DRY RUN — would PUT 10 bytes" in capsys.readouterr().out


def test_do_update_sends_published_and_labels_back(fake):
    fake.add("p", title="old")
    assert b.do_update("p", "u", "new", "<p>b</p>", published="2026-01-01T00:00:00Z", labels=["A"]) is True
    method, path, payload = fake.writes()[0]
    assert method == "PUT" and path.endswith("/posts/p")
    assert payload == {"id": "p", "title": "new", "content": "<p>b</p>",
                       "published": "2026-01-01T00:00:00Z", "labels": ["A"]}


def test_do_update_omits_absent_published_and_labels(fake):
    fake.add("p")
    b.do_update("p", "u", "t", "<p>b</p>")
    assert fake.writes()[0][2] == {"id": "p", "title": "t", "content": "<p>b</p>"}
    b.do_update("p", "u", "t", "<p>b</p>", labels=[])       # empty list is not sent
    assert "labels" not in fake.writes()[1][2]


def test_do_update_verify_failure_returns_false(fake, monkeypatch, capsys):
    fake.add("p")
    monkeypatch.setattr(b, "verify_live", lambda u, needle=None: (False, "expected content missing"))
    assert b.do_update("p", "u", "t", "<p>b</p>") is False
    assert "WROTE BUT VERIFY FAILED: expected content missing" in capsys.readouterr().out


def test_do_update_falls_back_to_stored_when_public_fetch_empty(fake, capsys):
    fake.add("p", content="<p>hello world</p>")
    fake.live_html = ""
    assert b.do_update("p", "u", "t", "<p>hello world</p>") is True
    out = capsys.readouterr().out
    assert "verified: via API, public fetch unavailable" in out


def test_do_update_fallback_mismatch(fake, monkeypatch):
    fake.add("p", content="<p>stale</p>")
    fake.live_html = ""
    # PUT updates the fake store, so make the stored copy differ from the probe
    fake.posts["p"]["content"] = "<p>stale</p>"
    orig = fake.api
    def api(path, data=None, method="GET"):
        r = orig(path, data, method)
        if method == "PUT":
            fake.posts["p"]["content"] = "<p>stale</p>"
        return r
    monkeypatch.setattr(b, "api", api)
    assert b.do_update("p", "u", "t", "<p>fresh</p>") is False


def test_cmd_update_by_slug_exits_zero_and_uses_post_title(fake):
    fake.add("p1", title="Keep", slug="s", published="P", labels=["L"])
    with pytest.raises(SystemExit) as e:
        b.cmd_update(ns(slug="s", file=_write(fake, "<p>new</p>")))
    assert e.value.code == 0
    sent = fake.writes()[0][2]
    assert sent["title"] == "Keep" and sent["published"] == "P" and sent["labels"] == ["L"]


def _write(fake, text, name="body.html"):
    import tempfile, pathlib
    d = pathlib.Path(tempfile.mkdtemp())
    p = d / name
    p.write_text(text, encoding="utf-8")
    return str(p)


def test_cmd_update_by_id_with_title_override(fake, capsys):
    fake.add("p1", title="Old", slug="s")
    with pytest.raises(SystemExit) as e:
        b.cmd_update(ns(id="p1", title="New", file=_write(fake, "<p>x</p>")))
    assert e.value.code == 0
    assert fake.writes()[0][2]["title"] == "New"
    assert "'Old'" in capsys.readouterr().out
    assert not any("posts?" in c[1] for c in fake.calls)       # no slug search when an id is given


def test_cmd_update_verify_failure_exit_2(fake, monkeypatch):
    fake.add("p1", slug="s")
    monkeypatch.setattr(b, "verify_live", lambda u, needle=None: (False, "x"))
    with pytest.raises(SystemExit) as e:
        b.cmd_update(ns(slug="s", file=_write(fake, "<p>x</p>")))
    assert e.value.code == 2


def test_cmd_update_ceiling_exit_3(fake, capsys):
    fake.add("p1", slug="s")
    fake.fail[("PUT", "/blogs")] = b.Ceiling("quota")
    with pytest.raises(SystemExit) as e:
        b.cmd_update(ns(slug="s", file=_write(fake, "<p>x</p>")))
    assert e.value.code == 3
    assert "ceiling" in capsys.readouterr().out


def test_cmd_delete_default_is_dry_run(fake, capsys):
    fake.add("p1", slug="s", title="T1")
    b.cmd_delete(ns(slug="s"))
    assert fake.writes() == [] and "p1" in fake.posts
    assert "DRY RUN" in capsys.readouterr().out


def test_cmd_delete_yes_deletes_by_id_and_slug(fake):
    fake.add("p1", slug="s1")
    fake.add("p2", slug="s2")
    b.cmd_delete(ns(id="p1", yes=True))
    b.cmd_delete(ns(slug="s2", yes=True))
    assert fake.posts == {}
    assert [c[0] for c in fake.writes()] == ["DELETE", "DELETE"]


def test_title_key_normalises():
    assert b._title_key("  Hello,   World!! ") == "hello world"
    assert b._title_key("A &amp; B") == "a b"
    assert b._title_key(None) == ""


def test_live_posts_meta_paginates(monkeypatch):
    pages = [{"items": [{"id": 1}], "nextPageToken": "n"}, {"items": [{"id": 2}]}]
    monkeypatch.setattr(b, "api", lambda p, **k: pages.pop(0))
    assert b.live_posts_meta() == [{"id": 1}, {"id": 2}]


def test_cmd_duplicates_none(fake, capsys):
    fake.add("a", title="One")
    fake.add("b", title="Two")
    b.cmd_duplicates(ns())
    assert "no duplicate titles" in capsys.readouterr().out


def _dups(fake):
    fake.add("late", title="Same Title!", published="2026-02-01T00:00:00Z")
    fake.add("early", title="same title", published="2026-01-01T00:00:00Z")
    fake.add("uniq", title="Other", published="2026-01-01T00:00:00Z")


def test_cmd_duplicates_lists_only_without_flags(fake, capsys):
    _dups(fake)
    b.cmd_duplicates(ns())
    out = capsys.readouterr().out
    assert out.index("KEEP   id=early") < out.index("DELETE id=late")
    assert "listed only" in out and fake.writes() == []
    b.cmd_duplicates(ns(delete_newer=True))        # flag without --yes: still no deletion
    assert fake.writes() == []
    b.cmd_duplicates(ns(yes=True))                 # --yes without flag: still no deletion
    assert fake.writes() == []


def test_cmd_duplicates_deletes_newer_keeps_earliest(fake):
    _dups(fake)
    b.cmd_duplicates(ns(delete_newer=True, yes=True))
    assert set(fake.posts) == {"early", "uniq"}


def test_cmd_insert_dry_run(fake, capsys):
    b.cmd_insert(ns(file=_write(fake, "<p>x</p>"), title="T", dry_run=True, draft=True))
    out = capsys.readouterr().out
    assert "DRY RUN" in out and "DRAFT" in out and fake.calls == []


def test_cmd_insert_refuses_duplicate_title_exit_4(fake, capsys):
    fake.add("p1", title="Dup Title!")
    with pytest.raises(SystemExit) as e:
        b.cmd_insert(ns(file=_write(fake, "<p>x</p>"), title="dup title"))
    assert e.value.code == 4
    assert fake.writes() == []
    assert "already live" in capsys.readouterr().out


def test_cmd_insert_allow_duplicate_publishes_and_verifies(fake, capsys):
    fake.add("p1", title="Same")
    with pytest.raises(SystemExit) as e:
        b.cmd_insert(ns(file=_write(fake, "<p>x</p>"), title="Same", allow_duplicate=True))
    assert e.value.code == 0
    assert fake.writes()[0][1].endswith("/posts")          # no isDraft query
    assert "verified" in capsys.readouterr().out


def test_cmd_insert_draft_returns_without_verify(fake, capsys):
    b.cmd_insert(ns(file=_write(fake, "<p>x</p>"), title="Fresh", draft=True))
    assert fake.writes()[0][1].endswith("?isDraft=true")
    assert "no public URL" in capsys.readouterr().out


def test_cmd_insert_verify_failure_exit_2(fake, monkeypatch):
    monkeypatch.setattr(b, "verify_live", lambda u, needle=None: (False, "expected content missing"))
    with pytest.raises(SystemExit) as e:
        b.cmd_insert(ns(file=_write(fake, "<p>x</p>"), title="Fresh"))
    assert e.value.code == 2


def test_cmd_insert_empty_live_falls_back_to_stored(fake, capsys):
    fake.live_html = ""
    with pytest.raises(SystemExit) as e:
        b.cmd_insert(ns(file=_write(fake, "<p>hello there</p>"), title="Fresh"))
    assert e.value.code == 0
    assert "via API" in capsys.readouterr().out


def test_cmd_insert_ceiling_exit_3(fake):
    fake.fail[("POST", "/blogs")] = b.Ceiling("q")
    with pytest.raises(SystemExit) as e:
        b.cmd_insert(ns(file=_write(fake, "<p>x</p>"), title="Fresh"))
    assert e.value.code == 3


def test_cmd_drafts_lists_sorted_and_saves(fake, tmp_path, capsys):
    fake.add("d1", title="Old draft", status="DRAFT", updated="2026-01-01T00:00:00Z", content="<p>é</p>", labels=["x"])
    fake.add("d2", title="New draft", status="DRAFT", updated="2026-03-01T00:00:00Z", content="<p>b</p>")
    fake.add("l1", title="Live", status="LIVE")
    out = tmp_path / "out"
    b.cmd_drafts(ns(out=str(out)))
    idx = json.loads((out / "index.json").read_text())
    assert [r["id"] for r in idx] == ["d2", "d1"]               # newest first
    assert idx[1]["bytes"] == len("<p>é</p>".encode()) and idx[1]["labels"] == ["x"]
    assert (out / "d1.html").read_text(encoding="utf-8") == "<p>é</p>"
    assert "2 draft(s)" in capsys.readouterr().out
    assert any("fetchBodies=true" in c[1] for c in fake.calls)


def test_cmd_drafts_without_out_does_not_fetch_bodies(fake, capsys):
    fake.add("d1", status="DRAFT")
    b.cmd_drafts(ns())
    assert "fetchBodies=false" in fake.calls[0][1]
    assert "1 draft(s)" in capsys.readouterr().out


def test_cmd_drafts_paginates(monkeypatch, capsys):
    pages = [{"items": [{"id": "a"}], "nextPageToken": "n"}, {"items": [{"id": "b"}]}]
    qs = []
    monkeypatch.setattr(b, "api", lambda p, **k: qs.append(p) or pages.pop(0))
    b.cmd_drafts(ns())
    assert "2 draft(s)" in capsys.readouterr().out and "pageToken=n" in qs[1]


def test_cmd_publish_draft(fake, capsys):
    fake.add("d1", status="DRAFT")
    b.cmd_publish_draft(ns(id="d1", dry_run=True))
    assert fake.writes() == [] and "DRY RUN" in capsys.readouterr().out
    b.cmd_publish_draft(ns(id="d1"))
    assert fake.writes()[0][1].endswith("/d1/publish") and fake.posts["d1"]["status"] == "LIVE"


def test_cmd_publish_draft_refuses_live(fake):
    fake.add("p", status="LIVE")
    with pytest.raises(SystemExit) as e:
        b.cmd_publish_draft(ns(id="p"))
    assert "not a draft" in str(e.value) and fake.writes() == []


def test_cmd_publish_draft_ceiling(fake):
    fake.add("d1", status="DRAFT")
    fake.fail[("POST", "/blogs")] = b.Ceiling("q")
    with pytest.raises(SystemExit) as e:
        b.cmd_publish_draft(ns(id="d1"))
    assert e.value.code == 3


def test_cmd_revert_draft_from_slugs_and_file(fake, tmp_path, capsys):
    fake.add("p1", slug="a")
    fake.add("p2", slug="b")
    f = tmp_path / "s.txt"
    f.write_text("# comment\n\nb\nmissing\n")
    b.cmd_revert_draft(argparse.Namespace(slug=["a"], file=str(f), dry_run=False))
    assert fake.posts["p1"]["status"] == "DRAFT" and fake.posts["p2"]["status"] == "DRAFT"
    assert "skip missing" in capsys.readouterr().out


def test_cmd_revert_draft_dry_run_and_empty(fake):
    fake.add("p1", slug="a")
    b.cmd_revert_draft(argparse.Namespace(slug=["a"], file=None, dry_run=True))
    assert fake.writes() == []
    with pytest.raises(SystemExit) as e:
        b.cmd_revert_draft(argparse.Namespace(slug=None, file=None, dry_run=False))
    assert "give --slug or --file" in str(e.value)


def test_cmd_revert_draft_ceiling(fake):
    fake.add("p1", slug="a")
    fake.fail[("POST", "/blogs")] = b.Ceiling("q")
    with pytest.raises(SystemExit) as e:
        b.cmd_revert_draft(argparse.Namespace(slug=["a"], file=None, dry_run=False))
    assert e.value.code == 3


def test_cmd_page_create_update_and_dry_run(fake, capsys):
    f = _write(fake, "<p>page</p>")
    b.cmd_page(ns(file=f, title="PT", dry_run=True))
    assert fake.calls == [] and "create page" in capsys.readouterr().out
    b.cmd_page(ns(file=f, title="PT", id="7", dry_run=True))
    assert "update page" in capsys.readouterr().out
    b.cmd_page(ns(file=f, title="PT"))
    assert fake.writes()[0][0] == "POST" and fake.writes()[0][1].endswith("/pages")
    b.cmd_page(ns(file=f, title="PT", id="7"))
    assert fake.writes()[1][0] == "PUT" and fake.writes()[1][2]["id"] == "7"
    assert "verified" in capsys.readouterr().out


def test_cmd_page_without_url_skips_verify(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(b, "api", lambda *a, **k: {"id": "9"})
    f = tmp_path / "p.html"
    f.write_text("<p>x</p>")
    b.cmd_page(ns(file=str(f), title="t"))
    out = capsys.readouterr().out
    assert "(draft)" in out and "verified" not in out


def test_cmd_page_fallback_to_stored(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(b, "api", lambda *a, **k: {"id": "9", "url": "u", "content": "<p>hi there</p>"})
    monkeypatch.setattr(b, "verify_live", lambda u, needle=None: (False, "empty response"))
    monkeypatch.setattr(b.time, "sleep", lambda s: None)
    f = tmp_path / "p.html"
    f.write_text("<p>hi there</p>")
    b.cmd_page(ns(file=str(f), title="t"))
    assert "verified: via API" in capsys.readouterr().out


def test_cmd_pages_lists(fake, capsys):
    fake.pages = {"1": {"id": "1", "status": "LIVE", "title": "About", "url": "u1"}, "2": {"id": "2", "title": "NoUrl"}}
    b.cmd_pages(None)
    out = capsys.readouterr().out
    assert "About" in out and "(no url)" in out and "?" in out


# --------------------------------------------------------- text transforms
@pytest.mark.parametrize("src,want", [
    ("see https://masaladeutsch.blogspot.com/2026/a.html", "see https://blog.vertistratsolution.com/2026/a.html"),
    ("http://www.masaladeutsch.blogspot.com/x", "https://blog.vertistratsolution.com/x"),
    ("//masaladeutsch.blogspot.com/x", "https://blog.vertistratsolution.com/x"),
    ("host masaladeutsch.blogspot.com here", "host blog.vertistratsolution.com here"),
    ("nothing", "nothing"),
])
def test_migrate_links(src, want):
    assert b.migrate_links(src) == want


@pytest.mark.parametrize("src,want", [
    ("Welcome to Masala Deutsch today", "Welcome to VertiStrat Solutions today"),
    ("MASALA DEUTSCH", "VERTISTRAT SOLUTIONS"),
    ("masala deutsch", "vertistrat solutions"),
    ("Masala Deutsch", "VertiStrat Solutions"),
    ("by masaladeutsch team", "by VertiStrat Solutions team"),
    ("`masaladeutsch`", "`masaladeutsch`"),
    ("cd masaladeutsch", "cd masaladeutsch"),
    ("github.io/masaladeutsch/x", "github.io/masaladeutsch/x"),
    ("/Masala Deutsch", "/Masala Deutsch"),
    ("the-masala-deutsch-shop", "the-masala-deutsch-shop"),
    ("Masala Deutsch-shop", "Masala Deutsch-shop"),
    ("Masala Deutsche", "Masala Deutsche"),
    ("masaladeutsch.blogspot.com", "masaladeutsch.blogspot.com"),
    ("masaladeutsch.github.io", "masaladeutsch.github.io"),
])
def test_rebrand_boundaries(src, want):
    assert b.rebrand(src) == want


def test_set_h1():
    assert b.set_h1('<h1 class="t">Old</h1><h1>Second</h1>', "A & B") == '<h1 class="t">A &amp; B</h1><h1>Second</h1>'
    assert b.set_h1("<p>no h1</p>", "T") == "<p>no h1</p>"
    assert b.set_h1("<h1>\nmulti\nline</h1>", "T") == "<h1>T</h1>"
    assert b.set_h1("<h1>x</h1>", 'say "hi"') == '<h1>say "hi"</h1>'   # quotes not escaped


# ------------------------------------------------------------------ retitle
def _tsv(tmp_path, lines):
    f = tmp_path / "t.tsv"
    f.write_text("\n".join(lines), encoding="utf-8")
    return str(f)


def test_cmd_retitle_changes_only_what_differs(fake, tmp_path, capsys):
    fake.add("p1", title="Old", slug="a", content="<h1>Old</h1><p>x</p>", published="P", labels=["L"])
    fake.add("p2", title="Same", slug="b", content="<h1>Same</h1>")
    f = _tsv(tmp_path, ["# comment\tignored", "a\tNew", "b\tSame", "gone\tX", "no tab line"])
    with pytest.raises(SystemExit) as e:
        b.cmd_retitle(ns(file=f))
    assert e.value.code == 0
    puts = fake.writes()
    assert len(puts) == 1 and puts[0][2]["title"] == "New"
    assert puts[0][2]["content"] == "<h1>New</h1><p>x</p>"
    out = capsys.readouterr().out
    assert "3 titles" in out and "1 to change" in out and "1 already done" in out and "1 not live" in out


def test_cmd_retitle_rewrites_old_links_even_when_title_same(fake, tmp_path):
    fake.add("p1", title="Same", slug="a", content='<h1>Same</h1><a href="https://masaladeutsch.blogspot.com/x">l</a>')
    with pytest.raises(SystemExit):
        b.cmd_retitle(ns(file=_tsv(tmp_path, ["a\tSame"])))
    assert "vertistratsolution" in fake.writes()[0][2]["content"]


def test_cmd_retitle_dry_run_and_limit(fake, tmp_path):
    for s in "abc":
        fake.add(s, title="Old", slug=s, content="<h1>Old</h1>")
    f = _tsv(tmp_path, ["a\tN", "b\tN", "c\tN"])
    with pytest.raises(SystemExit):
        b.cmd_retitle(ns(file=f, dry_run=True))
    assert fake.writes() == []
    with pytest.raises(SystemExit):
        b.cmd_retitle(ns(file=f, limit=2))
    assert len(fake.writes()) == 2


def test_cmd_retitle_verify_failure_exit_2(fake, tmp_path, monkeypatch):
    fake.add("a", title="Old", slug="a", content="<h1>Old</h1>")
    monkeypatch.setattr(b, "verify_live", lambda u, needle=None: (False, "x"))
    with pytest.raises(SystemExit) as e:
        b.cmd_retitle(ns(file=_tsv(tmp_path, ["a\tN"])))
    assert e.value.code == 2


def test_cmd_retitle_ceiling_exit_3(fake, tmp_path):
    fake.add("a", title="Old", slug="a", content="<h1>Old</h1>")
    fake.fail[("PUT", "/blogs")] = b.Ceiling("q")
    with pytest.raises(SystemExit) as e:
        b.cmd_retitle(ns(file=_tsv(tmp_path, ["a\tN"])))
    assert e.value.code == 3


def test_cmd_retitle_paginates(monkeypatch, tmp_path):
    pages = [{"items": [{"id": "1", "title": "o", "url": "https://b/x/a.html", "content": "<h1>o</h1>"}], "nextPageToken": "n"},
             {"items": [{"id": "2", "title": "o", "url": "https://b/x/b.html", "content": "<h1>o</h1>"}]}]
    writes = []
    def api(path, data=None, method="GET"):
        if method == "PUT":
            writes.append(data["id"])
            return {}
        return pages.pop(0)
    monkeypatch.setattr(b, "api", api)
    monkeypatch.setattr(b, "verify_live", lambda u, needle=None: (True, "ok"))
    monkeypatch.setattr(b.time, "sleep", lambda s: None)
    with pytest.raises(SystemExit):
        b.cmd_retitle(ns(file=_tsv(tmp_path, ["a\tN", "b\tN"])))
    assert writes == ["1", "2"]


# ----------------------------------------------------------- migrate-domain
OLD = '<a href="https://masaladeutsch.blogspot.com/x">Masala Deutsch</a>'


def test_migrate_domain_dry_run_counts_and_orders(fake, capsys):
    fake.add("p1", slug="zzz", content=OLD, title="Masala Deutsch post")
    fake.add("p2", slug="article-index-start-here", content=OLD)
    fake.add("p3", slug="clean", content="<p>fine</p>")
    fake.pages = {"g": {"id": "g", "title": "T", "content": OLD}}
    with pytest.raises(SystemExit) as e:
        b.cmd_migrate_domain(ns(dry_run=True))
    assert e.value.code == 0
    out = capsys.readouterr().out
    assert "2 posts and 1 pages" in out and "2 links in posts" in out
    assert out.index("article-index-start-here.html") < out.index("zzz.html")
    assert fake.writes() == []


def test_migrate_domain_writes_posts_pages_and_drafts(fake):
    fake.add("p1", slug="a", content=OLD, title="Masala Deutsch", published="P", labels=["L"])
    fake.add("d1", slug="d", status="DRAFT", content=OLD, labels=["Q"])
    fake.add("d2", slug="d2", status="DRAFT", content=OLD)
    fake.pages = {"g": {"id": "g", "title": "T", "content": OLD}}
    with pytest.raises(SystemExit) as e:
        b.cmd_migrate_domain(ns(drafts=True))
    assert e.value.code == 0
    w = {(m, p.split("/")[-2] + "/" + p.split("/")[-1]): d for m, p, d in fake.writes()}
    assert w[("PUT", "pages/g")]["kind"] == "blogger#page"
    assert "vertistratsolution" in w[("PUT", "posts/p1")]["content"] and w[("PUT", "posts/p1")]["title"] == "VertiStrat Solutions"
    assert w[("PUT", "posts/d1")]["labels"] == ["Q"] and "labels" not in w[("PUT", "posts/d2")]
    assert fake.posts["p1"]["labels"] == ["L"]


def test_migrate_domain_skips_drafts_without_flag_and_clean_posts(fake):
    fake.add("d1", slug="d", status="DRAFT", content=OLD)
    fake.add("p1", slug="a", content="<p>clean</p>", title="clean")
    with pytest.raises(SystemExit):
        b.cmd_migrate_domain(ns())
    assert fake.writes() == []


def test_migrate_domain_title_only_change_triggers_write(fake):
    fake.add("p1", slug="a", content="<p>clean</p>", title="Masala Deutsch notes")
    with pytest.raises(SystemExit):
        b.cmd_migrate_domain(ns())
    assert fake.writes()[0][2]["title"] == "VertiStrat Solutions notes"


def test_migrate_domain_limit_and_verify_failure(fake, monkeypatch):
    for s in "abc":
        fake.add(s, slug=s, content=OLD)
    monkeypatch.setattr(b, "verify_live", lambda u, needle=None: (False, "x"))
    with pytest.raises(SystemExit) as e:
        b.cmd_migrate_domain(ns(limit=2))
    assert e.value.code == 2
    assert len(fake.writes()) == 2


def test_migrate_domain_ceiling(fake):
    fake.add("a", slug="a", content=OLD)
    fake.fail[("PUT", "/blogs")] = b.Ceiling("q")
    with pytest.raises(SystemExit) as e:
        b.cmd_migrate_domain(ns())
    assert e.value.code == 3


def test_migrate_domain_paginates(monkeypatch):
    pages = [{"items": [{"id": "1", "title": "t", "url": "u/a.html", "content": OLD}], "nextPageToken": "n"},
             {"items": [{"id": "2", "title": "t", "url": "u/b.html", "content": OLD}]}]
    def api(path, data=None, method="GET"):
        if "/pages" in path:
            return {"items": []}
        if method == "PUT":
            return {}
        return pages.pop(0)
    monkeypatch.setattr(b, "api", api)
    monkeypatch.setattr(b, "verify_live", lambda u, needle=None: (True, "ok"))
    monkeypatch.setattr(b.time, "sleep", lambda s: None)
    with pytest.raises(SystemExit) as e:
        b.cmd_migrate_domain(ns(dry_run=True))
    assert e.value.code == 0


# --------------------------------------------------------------------- bulk
def _manifest(tmp_path, entries):
    m = tmp_path / "m.json"
    m.write_text(json.dumps(entries))
    return str(m)


def test_bulk_updates_skips_missing_file_and_missing_post(fake, tmp_path, capsys):
    body = tmp_path / "b.html"
    body.write_text("<p>fix</p>")
    fake.add("p1", slug="a", title="Keep", published="P", labels=["L"])
    m = _manifest(tmp_path, [
        {"slug": "nofile", "path": str(tmp_path / "x.html")},
        {"slug": "ghost", "path": str(body)},
        {"slug": "a", "path": str(body)},
    ])
    with pytest.raises(SystemExit) as e:
        b.cmd_bulk(ns(manifest=m))
    assert e.value.code == 0
    assert len(fake.writes()) == 1 and fake.writes()[0][2]["title"] == "Keep"
    out = capsys.readouterr().out
    assert "1 updated, 0 failed" in out and "missing" in out and "skip:" in out


def test_bulk_limit_stops_early(fake, tmp_path, capsys):
    body = tmp_path / "b.html"
    body.write_text("<p>fix</p>")
    for s in "abc":
        fake.add(s, slug=s)
    m = _manifest(tmp_path, [{"slug": s, "path": str(body)} for s in "abc"])
    with pytest.raises(SystemExit):
        b.cmd_bulk(ns(manifest=m, limit=1))
    assert len(fake.writes()) == 1
    assert "stopping at --limit 1; 2 not attempted" in capsys.readouterr().out


def test_bulk_failure_exit_2_and_ceiling_exit_3(fake, tmp_path, monkeypatch):
    body = tmp_path / "b.html"
    body.write_text("<p>fix</p>")
    fake.add("a", slug="a")
    m = _manifest(tmp_path, [{"slug": "a", "path": str(body)}])
    monkeypatch.setattr(b, "verify_live", lambda u, needle=None: (False, "x"))
    with pytest.raises(SystemExit) as e:
        b.cmd_bulk(ns(manifest=m))
    assert e.value.code == 2
    fake.fail[("PUT", "/blogs")] = b.Ceiling("q")
    with pytest.raises(SystemExit) as e:
        b.cmd_bulk(ns(manifest=m))
    assert e.value.code == 3


# --------------------------------------------------------------------- main
@pytest.mark.parametrize("argv,fn", [
    (["whoami"], "cmd_whoami"), (["pages"], "cmd_pages"), (["get", "--slug", "s"], "cmd_get"),
    (["update", "--slug", "s", "--file", "f"], "cmd_update"), (["delete", "--id", "1"], "cmd_delete"),
    (["insert", "--file", "f", "--title", "t"], "cmd_insert"), (["page", "--file", "f", "--title", "t"], "cmd_page"),
    (["drafts"], "cmd_drafts"), (["publish-draft", "--id", "1"], "cmd_publish_draft"),
    (["revert-draft", "--slug", "a"], "cmd_revert_draft"), (["migrate-domain"], "cmd_migrate_domain"),
    (["duplicates"], "cmd_duplicates"), (["retitle", "--file", "f"], "cmd_retitle"),
    (["bulk", "--manifest", "m"], "cmd_bulk"), (["auth"], "cmd_auth"),
])
def test_main_dispatches(monkeypatch, argv, fn):
    called = []
    monkeypatch.setattr(b, fn, lambda a: called.append(a))
    monkeypatch.setattr(b.sys, "argv", ["blogger_api.py"] + argv)
    b.main()
    assert len(called) == 1


def test_main_requires_subcommand(monkeypatch):
    monkeypatch.setattr(b.sys, "argv", ["blogger_api.py"])
    with pytest.raises(SystemExit) as e:
        b.main()
    assert e.value.code == 2

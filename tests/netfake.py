"""Shared fake for urllib.request.urlopen: a queue of canned responses/exceptions."""
import io
import json
import urllib.error


class FakeResp:
    def __init__(self, payload):
        self.payload = payload if isinstance(payload, bytes) else (
            payload.encode() if isinstance(payload, str) else json.dumps(payload).encode())
        self.headers = {}
        self.status = 200

    def read(self, *a):
        return self.payload

    def getcode(self):
        return 200

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def http_error(code, body="boom", url="u"):
    return urllib.error.HTTPError(url, code, "msg", {}, io.BytesIO(body.encode()))


class Net:
    """Install with Net.install(monkeypatch). queue items: payload (dict/str/bytes) or an Exception to raise."""

    def __init__(self):
        self.queue = []
        self.requests = []

    def install(self, monkeypatch, module=None):
        import urllib.request
        monkeypatch.setattr(urllib.request, "urlopen", self._urlopen)
        return self

    def _urlopen(self, req, *a, **kw):
        url = req if isinstance(req, str) else req.full_url
        body = None if isinstance(req, str) else req.data
        headers = {} if isinstance(req, str) else dict(req.header_items())
        self.requests.append({"url": url, "body": body, "headers": headers, "kw": kw, "args": a})
        if not self.queue:
            raise AssertionError(f"unexpected network call to {url}")
        item = self.queue.pop(0)
        if isinstance(item, Exception):
            raise item
        if callable(item):
            item = item(url, body)
            if isinstance(item, Exception):
                raise item
        return FakeResp(item)

    def json_bodies(self):
        return [json.loads(r["body"]) for r in self.requests if r["body"]]


class Routes:
    """URL-keyed fake (thread-safe, order independent): routes[url] -> payload | Exception | list (consumed in order)."""

    def __init__(self, routes=None):
        import threading
        self.routes = dict(routes or {})
        self.hits = []
        self.lock = threading.Lock()

    def install(self, monkeypatch):
        import urllib.request
        monkeypatch.setattr(urllib.request, "urlopen", self._urlopen)
        return self

    def _urlopen(self, req, *a, **kw):
        url = req if isinstance(req, str) else req.full_url
        with self.lock:
            self.hits.append(url)
            item = self.routes.get(url)
            if item is None:
                raise AssertionError(f"unexpected url {url}")
            if isinstance(item, list):
                item = item.pop(0) if len(item) > 1 else item[0]
        if isinstance(item, Exception):
            raise item
        resp = FakeResp(item[1] if isinstance(item, tuple) else item)
        if isinstance(item, tuple):
            resp.status = item[0]
        resp.url = url
        resp.geturl = lambda: url
        return resp

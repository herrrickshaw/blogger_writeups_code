import json

import pytest

import apply_labels as L
import blogger_api as B


def test_taxonomy_is_wellformed():
    assert len(L.TAXONOMY) == 15
    for lab, keys in L.TAXONOMY.items():
        assert keys and all(k == k.lower() for k in keys), lab
    for slug, labs in list(L.OVERRIDE.items()) + list(L.SLUG_CONTAINS.items()):      # overrides may use labels outside TAXONOMY
        assert isinstance(labs, list) and all(isinstance(l, str) and l for l in labs), slug
        assert len(labs) == len(set(labs)), slug


def test_headings_weights_h1_and_collects_other_sources(tmp_path):
    f = tmp_path / "p.html"
    f.write_text('<script>h1</script><h1>Ethanol <b>Blend</b></h1><h2>Sub</h2><h3>Third</h3><h4>skip</h4>'
                 '<p class="standfirst">Standfirst &amp; text</p><p class="kicker"><span class="dot"></span>Kicker</span></p>'
                 '<p class="eyebrow">Eye</p>', encoding="utf-8")
    h = L.headings(f)
    assert h.count("ethanol") == 3 and h.count("blend") == 3                          # H1 counted three times
    assert "sub" in h and "third" in h and "skip" not in h and "standfirst & text" in h and "kicker" in h and "eye" in h


def test_labels_for_threshold_ordering_and_cap():
    assert L.labels_for("nothing relevant here") == []
    assert L.labels_for("") == []
    got = L.labels_for("ethanol " * 6 + "wpi " * 2 + "textile")
    assert got[0] == "Energy & Fuels" and "Prices & Inflation" in got and "Textiles" not in got       # cut = 6/3 = 2
    got = L.labels_for("ethanol " * 6 + "wpi " * 1)
    assert got == ["Energy & Fuels"]                                                                     # 1 < 2
    assert L.labels_for("ethanol wpi textile urea bond tariff", max_labels=2).__len__() == 2
    many = L.labels_for("ethanol wpi textile urea bond tariff")
    assert len(many) == 3                                                                                # default cap
    assert L.labels_for("wpi") == ["Prices & Inflation"]                                                 # cut floor of 1


# ------------------------------------------------------------------ main
class Api:
    def __init__(self):
        self.posts = {}
        self.calls = []
        self.fail_put = None

    def __call__(self, path, data=None, method="GET"):
        self.calls.append((method, path, data))
        pid = path.rsplit("/", 1)[-1]
        if method == "GET":
            if pid not in self.posts:
                raise SystemExit("HTTP 404: gone")
            return dict(self.posts[pid])
        if self.fail_put:
            raise self.fail_put
        self.posts[pid].update(data)
        return {}


@pytest.fixture
def env(tmp_path, monkeypatch):
    monkeypatch.setattr(L, "ROOT", tmp_path)
    (tmp_path / "posts").mkdir()
    (tmp_path / "meta").mkdir()
    api = Api()
    monkeypatch.setattr(B, "api", api)
    monkeypatch.setattr(L.time, "sleep", lambda s: None)
    monkeypatch.setattr(L, "OVERRIDE", {"override-me": ["Textiles"]})
    monkeypatch.setattr(L, "SLUG_CONTAINS", {"magic-word": ["Chemicals", "Healthcare"]})
    state = {"recs": {}}

    def add(slug, h1="", labels=None, live=True, pid=None):
        pid = pid or f"id-{slug}"
        (tmp_path / "posts" / f"{slug}.html").write_text(f"<h1>{h1}</h1>")
        if live:
            state["recs"][pid] = {"slug": slug, "id": pid, "labels": labels or []}
            api.posts[pid] = {"id": pid, "title": f"T-{slug}", "content": "<p>c</p>", "published": "2026-01-01", "labels": labels or []}
        (tmp_path / "meta" / "manifest.json").write_text(json.dumps({"posts": state["recs"]}))
        return pid
    env.api = api
    return tmp_path, add, api


def run(monkeypatch, *argv):
    monkeypatch.setattr(L.sys, "argv", ["al", *argv])
    return L.main()


def test_main_requires_mode(env, monkeypatch):
    with pytest.raises(SystemExit) as e:
        run(monkeypatch)
    assert e.value.code == 2


def test_plan_prints_rules_precedence_and_never_calls_api(env, monkeypatch, capsys):
    tmp, add, api = env
    add("override-me", h1="ethanol")
    add("has-magic-word-in-it", h1="ethanol")
    add("plain", h1="Ethanol blending")
    add("nothing", h1="zzz")
    add("archived", h1="x", live=False)
    assert run(monkeypatch, "--plan") == 0
    out = capsys.readouterr().out
    assert "posts: 4   unlabelled by the rules: 1" in out
    assert "override-me" in out and "Textiles" in out and "Chemicals, Healthcare" in out and "Energy & Fuels" in out and "— none —" in out
    assert "archived" not in out and api.calls == []
    assert "   2  Energy & Fuels" not in out and "   1  Textiles" in out


def test_apply_labels_unlabelled_posts_and_resumability(env, monkeypatch, capsys):
    tmp, add, api = env
    a = add("a", h1="ethanol blending")
    b = add("b", h1="wpi inflation")
    c = add("c", h1="zzz")                                              # no rule matches: skipped
    d = add("d", h1="ethanol", labels=["Already"])                       # snapshot says labelled: no API call
    assert run(monkeypatch, "--apply") == 0
    out = capsys.readouterr().out
    assert "labelled 2 | already had labels 1" in out
    assert api.posts[a]["labels"] == ["Energy & Fuels"] and api.posts[b]["labels"] == ["Prices & Inflation"]
    assert api.posts[c]["labels"] == [] and api.posts[d]["labels"] == ["Already"]
    puts = [c for c in api.calls if c[0] == "PUT"]
    assert puts[0][2] == {"id": a, "title": "T-a", "content": "<p>c</p>", "published": "2026-01-01", "labels": ["Energy & Fuels"]}
    assert not any(d in c[1] for c in api.calls)
    api.calls.clear()
    run(monkeypatch, "--apply")                                          # idempotent: second run is read-only
    assert not any(c[0] == "PUT" for c in api.calls) and sum(1 for c in api.calls if c[0] == "GET") == 2


def test_apply_recheck_gets_live_labels_and_skips_if_present(env, monkeypatch, capsys):
    tmp, add, api = env
    add("a", h1="ethanol", labels=["Stale manifest says labelled"])
    pid = "id-a"
    api.posts[pid]["labels"] = []                                         # live post lost its labels
    run(monkeypatch, "--apply", "--recheck")
    assert api.posts[pid]["labels"] == ["Energy & Fuels"]
    api.calls.clear()
    run(monkeypatch, "--apply", "--recheck")
    assert [c[0] for c in api.calls] == ["GET"]                           # already labelled live -> no write
    assert "already had labels 1" in capsys.readouterr().out


def test_apply_limit_and_ceiling_and_missing_post(env, monkeypatch, capsys):
    tmp, add, api = env
    for s in "abc":
        add(s, h1="ethanol")
    run(monkeypatch, "--apply", "--limit", "2")
    assert "stopping at --limit 2" in capsys.readouterr().out and sum(1 for c in api.calls if c[0] == "PUT") == 2
    api.calls.clear()
    del api.posts["id-c"]
    run(monkeypatch, "--apply")
    assert "skip c: HTTP 404: gone" in capsys.readouterr().out
    add("d", h1="ethanol")
    api.fail_put = B.Ceiling("quota")
    assert run(monkeypatch, "--apply") == 3
    out = capsys.readouterr().out
    assert "daily write ceiling reached after 0 writes" in out and "re-run tomorrow" in out


def test_slug_filter_unknown_and_add_missing_rules(env, monkeypatch, capsys):
    tmp, add, api = env
    add("a", h1="ethanol")
    add("b", h1="ethanol")
    with pytest.raises(SystemExit):
        run(monkeypatch, "--plan", "--slug", "ghost")
    with pytest.raises(SystemExit):
        run(monkeypatch, "--apply", "--add-missing")
    run(monkeypatch, "--plan", "--slug", "a")
    assert "posts: 1 " in capsys.readouterr().out


def test_add_missing_never_removes_labels(env, monkeypatch, capsys):
    tmp, add, api = env
    add("a", h1="ethanol wpi", labels=["Custom", "Energy & Fuels"])
    add("b", h1="ethanol", labels=["Energy & Fuels"])
    assert run(monkeypatch, "--apply", "--add-missing", "--slug", "a", "--slug", "b") == 0
    out = capsys.readouterr().out
    assert api.posts["id-a"]["labels"] == ["Custom", "Energy & Fuels", "Prices & Inflation"]
    assert "b" in out and "already has Energy & Fuels" in out
    assert api.posts["id-b"]["labels"] == ["Energy & Fuels"]


def test_add_missing_ceiling(env, monkeypatch, capsys):
    tmp, add, api = env
    add("a", h1="ethanol", labels=["X"])
    api.fail_put = B.Ceiling("q")
    assert run(monkeypatch, "--apply", "--add-missing", "--slug", "a") == 3
    assert "daily write ceiling reached after 0 writes" in capsys.readouterr().out

import json
import types
import urllib.error

import pytest

import snapshot as S


# ----------------------------------------------------------------- helpers
@pytest.mark.parametrize("ts,want", [
    ("2026-01-02T03:04:05+05:30", "2026-01-02T03:04:05.000+05:30"),
    ("2026-01-02T03:04:05-08:00", "2026-01-02T03:04:05.000-08:00"),
    ("2026-01-02T03:04:05.123+05:30", "2026-01-02T03:04:05.123+05:30"),
    ("2026-01-02T03:04:05Z", "2026-01-02T03:04:05Z"),
    ("garbage", "garbage"),
])
def test_with_ms(ts, want):
    assert S._with_ms(ts) == want


@pytest.mark.parametrize("url,slug", [
    ("https://b/2026/05/my-post.html", "my-post"), ("https://b/2026/05/x_0123.html", "x_0123"),
    ("https://b/", "index"), ("https://b/p/about", "about"), ("https://b/2026/05/a.html?m=1", "a"),
])
def test_slug_of(url, slug):
    assert S.slug_of(url) == slug


def entry(pid="1", slug="a", body="<p>x</p>", title="T", pub="2026-01-01T00:00:00.000+05:30", upd="2026-01-02T00:00:00.000+05:30",
          labels=("L2", "L1"), url=None):
    return {"id": {"$t": f"tag:blogger.com,1999:blog-9.post-{pid}"},
            "link": [{"rel": "replies", "href": "r"}, {"rel": "alternate", "href": url or f"https://b/2026/01/{slug}.html"}],
            "content": {"$t": body}, "title": {"$t": title}, "published": {"$t": pub}, "updated": {"$t": upd},
            "category": [{"term": l} for l in labels]}


def test_parse_record_and_body():
    rec, body = S.parse(entry(pid="42", slug="s", body="héllo"))
    assert body == "héllo" and rec["id"] == "42" and rec["slug"] == "s" and rec["labels"] == ["L1", "L2"]
    assert rec["bytes"] == len("héllo") and len(rec["sha256"]) == 64 and rec["url"] == "https://b/2026/01/s.html"
    e = entry()
    del e["content"], e["category"]
    rec, body = S.parse(e)
    assert body == "" and rec["labels"] == [] and rec["bytes"] == 0
    e = entry()
    e["link"] = [{"rel": "self", "href": "x"}]
    with pytest.raises(StopIteration):
        S.parse(e)


def test_markers_and_delta():
    body = ('<p data-gs-revision-v1>r</p>gs-light-lock gs-typo-unify google_translate_element article-index-start-here '
            '@media not all and (prefers-color-scheme: dark) <script>var s="AI Disclosure"</script> gs-ai-disclosure')
    m = S.markers(body)
    assert m == {"light_lock": True, "dark_panel_guard": False, "typo_unify": True, "translate_widget": True, "index_link": True,
                 "ai_disclosure": True, "revision_line": True, "inverted_media_query": True, "disclaimer_in_script": True}
    assert S.markers("")["light_lock"] is False and S.markers("gs-revision-v1")["revision_line"] is True
    assert S.markers("AI Disclosure outside script")["disclaimer_in_script"] is False
    new = {"markers": {"light_lock": True, "dark_panel_guard": False}}
    assert S.marker_delta({"markers": {"light_lock": False, "dark_panel_guard": False}}, new) == {"light_lock": [False, True]}
    assert S.marker_delta({}, new) == {"light_lock": [None, True], "dark_panel_guard": [None, False]}
    assert S.marker_delta({"markers": new["markers"]}, new) == {}


# -------------------------------------------------------------- versioning
def test_bump():
    assert S.bump("1.2.3", "major") == "2.0.0" and S.bump("1.2.3", "minor") == "1.3.0"
    assert S.bump("1.2.3", "patch") == "1.2.4" and S.bump("1.2.3", "anything") == "1.2.4"
    assert S.bump("9.9.9", "major") == "10.0.0" and S.bump("0.0.0", "minor") == "0.1.0"


def test_visible_text_and_headings_ignore_revision_blocks():
    h = ('<p data-gs-revision-v1 class="x">rev 1.2 on 3 May</p><div id="changelog">v2 5 changes</div>'
         '<script>x=9</script><style>a{}</style><h2>One <b>Two</b></h2><p>Text &amp; more</p><h5>skip</h5>')
    assert S.visible_text(h) == "One Two Text & more skip"
    assert S.headings(h) == ["One Two"]
    assert S.headings("<h1>a</h1><h3> b \n c </h3><h4></h4>") == ["a", "b c", ""]


def test_classify_cases():
    assert S.classify(None, "x") == (None, "no previous body on disk")
    lvl, why = S.classify("<p>same</p>", "<p>same</p>")
    assert lvl is None and "set the level with --as" in why
    assert S.classify("<p>a b</p>", "<p class='n'>a   b</p>") == ("patch", "visible text identical; only markup/styling changed")
    lvl, why = S.classify("<p>grew 10 percent</p>", "<p>grew 12 percent</p>")
    assert lvl == "major" and why == "figures changed (+1/-1 distinct numbers)"
    assert S.classify("<p>x 1,000</p>", "<p>x 1000</p>")[0] == "major"                      # comma form differs: figure changed
    old = "<h2>Alpha</h2><h2>Beta</h2><p>in 2025 words</p>"
    lvl, why = S.classify(old, "<h2>Alpha</h2><p>in 2025 words</p>")
    assert (lvl, why) == ("major", "section(s) removed: Beta")
    assert S.classify("<h2>A</h2><h2>B</h2><h2>C</h2><h2>D</h2>x", "x")[1] == "section(s) removed: A, B, C"
    lvl, why = S.classify("<h2>Alpha</h2><p>text</p>", "<h2>Alpha</h2><h2>Gamma</h2><p>text</p>")
    assert (lvl, why) == ("minor", "section(s) added: Gamma")
    base = "word " * 100
    lvl, why = S.classify(f"<p>{base}</p>", f"<p>{base}{'more ' * 3}</p>")
    assert lvl == "minor" and "prose grew" in why and "→" in why
    lvl, why = S.classify(f"<p>{base}</p>", f"<p>{base[:-5]}{'ok'}</p>")
    assert lvl == "patch" and "wording changed" in why


def test_classify_two_percent_growth_boundary():
    old = "<p>" + "a" * 100 + "</p>"
    assert S.classify(old, "<p>" + "a" * 102 + "</p>")[0] == "patch"          # exactly 2% is not "grew"
    assert S.classify(old, "<p>" + "a" * 103 + "</p>")[0] == "minor"


# ------------------------------------------------------------- fetch layer
def test_fetch_decodes_utf8(monkeypatch):
    from netfake import Net
    n = Net().install(monkeypatch)
    n.queue.append("héllo".encode("utf-8"))
    assert S._fetch("http://x") == "héllo" and n.requests[0]["headers"]["User-agent"] == S.UA


def feed(entries, total=None):
    return {"feed": {"entry": entries, "openSearch$totalResults": {"$t": str(total if total is not None else len(entries))}}}


def test_public_feed_pagination(monkeypatch):
    pages = {1: feed([entry(pid="1"), entry(pid="2")], total=3), 3: feed([entry(pid="3")], total=3)}
    seen = []
    def fetch(url):
        seen.append(url)
        start = int(url.split("start-index=")[1])
        return json.dumps(pages[start])
    monkeypatch.setattr(S, "_fetch", fetch)
    out = S._entries_from_public_feed()
    assert [e["id"]["$t"][-1] for e in out] == ["1", "2", "3"] and len(seen) == 2
    assert "alt=json" in seen[0] and "max-results=100" in seen[0] and seen[0].startswith(S.BLOG + "/feeds/posts/default?")


def test_public_feed_stops_on_empty_page(monkeypatch):
    monkeypatch.setattr(S, "_fetch", lambda url: json.dumps({"feed": {}}))
    assert S._entries_from_public_feed() == []


def test_api_fallback_reshapes_and_paginates(monkeypatch):
    calls = []
    items = [{"id": "7", "url": "https://b/2026/01/a.html", "content": "<p>c</p>", "title": "T",
              "published": "2026-01-01T00:00:00+05:30", "updated": "2026-01-02T00:00:00+05:30", "labels": ["X"]},
             {"id": "8", "url": "https://b/2026/01/b.html", "published": "2026-01-01T00:00:00Z", "updated": "2026-01-01T00:00:00Z"}]
    pages = [{"items": items[:1], "nextPageToken": "n"}, {"items": items[1:]}]
    def api(path, **kw):
        calls.append(path)
        return pages.pop(0)
    monkeypatch.setattr(S.B, "api", api)
    out = S._entries_from_api()
    assert len(out) == 2 and "pageToken=n" in calls[1] and "fetchBodies=true" in calls[0] and "status=LIVE" in calls[0]
    assert out[0]["published"]["$t"] == "2026-01-01T00:00:00.000+05:30"
    assert out[0]["id"]["$t"].endswith(".post-7") and out[0]["category"] == [{"term": "X"}]
    assert out[1]["content"]["$t"] == "" and out[1]["title"]["$t"] == "" and out[1]["published"]["$t"] == "2026-01-01T00:00:00Z"
    rec, body = S.parse(out[0])                          # the reshaped entry parses like a feed entry
    assert rec["id"] == "7" and rec["slug"] == "a" and body == "<p>c</p>"


def test_api_fallback_empty_page_ends(monkeypatch):
    monkeypatch.setattr(S.B, "api", lambda p, **k: {"items": []})
    assert S._entries_from_api() == []


@pytest.mark.parametrize("exc", [urllib.error.URLError("x"), TimeoutError(), ValueError("bad json"), KeyError("feed")])
def test_all_entries_falls_back_on_these_errors(monkeypatch, exc, capsys):
    def boom():
        raise exc
    monkeypatch.setattr(S, "_entries_from_public_feed", boom)
    monkeypatch.setattr(S, "_entries_from_api", lambda: ["api"])
    assert S.all_entries() == ["api"] and "falling back" in capsys.readouterr().err


def test_all_entries_prefers_public_feed_and_other_errors_propagate(monkeypatch):
    monkeypatch.setattr(S, "_entries_from_public_feed", lambda: ["feed"])
    monkeypatch.setattr(S, "_entries_from_api", lambda: pytest.fail("api used"))
    assert S.all_entries() == ["feed"]
    def boom():
        raise RuntimeError("other")
    monkeypatch.setattr(S, "_entries_from_public_feed", boom)
    with pytest.raises(RuntimeError):
        S.all_entries()


# --------------------------------------------------------------------- main
class Repo:
    def __init__(self, root):
        self.root, self.gits, self.feed, self.behind, self.rc = root, [], [], "0\n", {}

    def __truediv__(self, other):
        return self.root / other


@pytest.fixture
def repo(tmp_path, monkeypatch):
    for name, val in (("ROOT", tmp_path), ("POSTS", tmp_path / "posts"), ("META", tmp_path / "meta"),
                      ("MANIFEST", tmp_path / "meta" / "manifest.json"), ("CHANGELOG", tmp_path / "CHANGELOG.md")):
        monkeypatch.setattr(S, name, val)
    R = Repo(tmp_path)

    def run(cmd, **kw):
        R.gits.append((cmd, kw.get("cwd")))
        out = {"commit": "committed!", "fetch": "", "rev-parse": "main\n", "rev-list": R.behind, "pull": "", "push": "pushed"}
        key = cmd[1]
        return types.SimpleNamespace(returncode=R.rc.get(key, 0), stdout=out.get(key, ""), stderr="err-" + key)
    monkeypatch.setattr(S.subprocess, "run", run)
    monkeypatch.setattr(S, "all_entries", lambda: R.feed)
    return R


def run_main(monkeypatch, *argv):
    monkeypatch.setattr(S.sys, "argv", ["snapshot.py", *argv])
    S.main()


def manifest(repo):
    return json.loads((repo / "meta" / "manifest.json").read_text())


def test_main_first_snapshot_writes_files_and_commits(repo, monkeypatch, capsys):
    repo.feed = [entry(pid="1", slug="a", body="<p>one</p>"), entry(pid="2", slug="b", body="<p>two</p>")]
    run_main(monkeypatch, "--note", "why")
    m = manifest(repo)
    assert m["count"] == 2 and set(m["posts"]) == {"1", "2"}
    p = m["posts"]["1"]
    assert p["version"] == "1.0.0" and p["version_history"][0]["level"] == "initial" and p["version_history"][0]["note"] == "why"
    assert (repo / "posts" / "a.html").read_text() == "<p>one</p>"
    assert json.loads((repo / "meta" / "a.json").read_text())["slug"] == "a"
    log = (repo / "CHANGELOG.md").read_text()
    assert log.startswith("# Change log") and "**Added**" in log and "`a` **v1.0.0** — T (10 bytes)" in log and "\nwhy\n" in log
    out = capsys.readouterr().out
    assert "2 posts | +2 added | ~0 changed | ->0 moved | ~0 re-dated | -0 unpublished" in out and "  +  a" in out
    cmds = [c[0] for c in repo.gits]
    assert cmds[0] == ["git", "add", "-A"] and cmds[1][:2] == ["git", "commit"]
    assert cmds[1][3].startswith("snapshot ") and "+2 ~0 ->0 -0" in cmds[1][3] and cmds[1][3].endswith("\n\nwhy")
    assert "committed!" in out and all(c[1] == repo.root for c in repo.gits)


def snapshot_once(repo, monkeypatch, feed, *argv):
    repo.feed = feed
    run_main(monkeypatch, "--no-commit", *argv)


def test_main_no_change_leaves_no_trace(repo, monkeypatch, capsys):
    snapshot_once(repo, monkeypatch, [entry(pid="1")])
    log = (repo / "CHANGELOG.md").read_text()
    repo.gits.clear()
    run_main(monkeypatch)                                         # second identical run, with commit enabled
    assert (repo / "CHANGELOG.md").read_text() == log and repo.gits == []
    assert "no change since the last snapshot" in capsys.readouterr().out
    run_main(monkeypatch, "--allow-empty")
    assert (repo / "CHANGELOG.md").read_text().endswith("No changes.\n") and repo.gits


def test_main_empty_feed_refuses(repo, monkeypatch):
    with pytest.raises(SystemExit, match="refusing to snapshot"):
        run_main(monkeypatch)


def test_main_changed_body_levels_and_history(repo, monkeypatch, capsys):
    snapshot_once(repo, monkeypatch, [entry(pid="1", slug="p1", body="<p>v1 text 10</p>"), entry(pid="2", slug="p2", body="<h2>H</h2><p>x</p>"),
                                      entry(pid="3", slug="p3", body="<p>a b</p>")])
    snapshot_once(repo, monkeypatch, [entry(pid="1", slug="p1", body="<p>v1 text 12</p>"), entry(pid="2", slug="p2", body="<h2>H</h2><h2>New</h2><p>x</p>"),
                                      entry(pid="3", slug="p3", body="<p class='z'>a b</p>")])
    m = manifest(repo)["posts"]
    assert (m["1"]["version"], m["2"]["version"], m["3"]["version"]) == ("2.0.0", "1.1.0", "1.0.1")
    h = m["1"]["version_history"][-1]
    assert h["level"] == "major" and h["bytes"] == [len("<p>v1 text 10</p>"), len("<p>v1 text 12</p>")] and h["url_changed"] is None
    out = capsys.readouterr().out
    assert "  v p1: 1.0.0 -> 2.0.0 (major)" in out and "  v p2: 1.0.0 -> 1.1.0 (minor)" in out
    log = (repo / "CHANGELOG.md").read_text()
    assert "**Versions**" in log and "**1.0.0 → 2.0.0** (MAJOR)" in log and "**Changed**" in log and "(+" in log


def test_main_forced_levels_and_bad_as_slug(repo, monkeypatch):
    snapshot_once(repo, monkeypatch, [entry(pid="1", slug="a", body="<p>x 1</p>"), entry(pid="2", slug="b", body="<p>y 1</p>")])
    snapshot_once(repo, monkeypatch, [entry(pid="1", slug="a", body="<p>x 2</p>"), entry(pid="2", slug="b", body="<p>y 2</p>")],
                  "--as", "minor", "--as-slug", "b=patch")
    m = manifest(repo)["posts"]
    assert m["1"]["version"] == "1.1.0" and m["2"]["version"] == "1.0.1"
    assert m["1"]["version_history"][-1]["reason"].startswith("forced via --as minor (figures changed")
    assert m["2"]["version_history"][-1]["reason"].startswith("forced via --as-slug patch")
    with pytest.raises(SystemExit, match="level must be major, minor or patch"):
        run_main(monkeypatch, "--as-slug", "a=huge")
    with pytest.raises(SystemExit, match="level must be"):
        run_main(monkeypatch, "--as-slug", "nolevel")


def test_main_in_place_edit_defaults_to_patch_with_unclassified_reason(repo, monkeypatch):
    snapshot_once(repo, monkeypatch, [entry(pid="1", slug="a", body="<p>old</p>")])
    (repo / "posts" / "a.html").write_text("<p>new</p>")           # edited in place, then published
    snapshot_once(repo, monkeypatch, [entry(pid="1", slug="a", body="<p>new</p>")])
    h = manifest(repo)["posts"]["1"]["version_history"][-1]
    assert h["level"] == "patch" and h["reason"].startswith("UNCLASSIFIED, defaulted to patch:")


def test_main_moved_url_and_redated_and_removed(repo, monkeypatch, capsys):
    snapshot_once(repo, monkeypatch, [entry(pid="1", slug="old", body="<p>same</p>"), entry(pid="2", slug="redate"),
                                      entry(pid="3", slug="gone", title="Gone post")])
    capsys.readouterr()
    snapshot_once(repo, monkeypatch, [entry(pid="1", slug="new", body="<p>same</p>"),
                                      entry(pid="2", slug="redate", pub="2026-02-01T00:00:00.000+05:30")])
    m = manifest(repo)["posts"]
    assert set(m) == {"1", "2"} and m["1"]["slug"] == "new" and (repo / "posts" / "gone.html").exists()
    assert (repo / "posts" / "old.html").exists()                                # old file kept
    h = m["1"]["version_history"][-1]
    assert h["level"] == "patch" and h["reason"] == "moved to a new URL; body unchanged" and h["url_changed"][1].endswith("new.html")
    assert m["2"]["version"] == "1.0.0"                                          # re-dating alone is not a version bump
    log = (repo / "CHANGELOG.md").read_text()
    assert "**Re-dated**" in log and "2026-01-01 &rarr; 2026-02-01" in log
    assert "**Moved**" in log and "`old` → `new`" in log
    assert "**No longer published**" in log and "`gone` — Gone post" in log
    out = capsys.readouterr().out
    assert "  d  redate: 2026-01-01 -> 2026-02-01" in out and "  -  gone" in out and "  -> old => new" in out
    assert "->1 moved | ~1 re-dated | -1 unpublished" in out


def test_main_redate_with_body_change_is_not_listed_as_redated(repo, monkeypatch):
    snapshot_once(repo, monkeypatch, [entry(pid="1", body="<p>a 1</p>")])
    snapshot_once(repo, monkeypatch, [entry(pid="1", body="<p>a 2</p>", pub="2026-03-03T00:00:00.000+05:30")])
    assert "**Re-dated**" not in (repo / "CHANGELOG.md").read_text()


def test_main_duplicate_ids_and_slug_collisions(repo, monkeypatch, capsys):
    snapshot_once(repo, monkeypatch, [entry(pid="1", slug="s", body="<p>first</p>"), entry(pid="1", slug="s", body="<p>dup</p>"),
                                      entry(pid="2", slug="s", body="<p>second</p>")])
    out = capsys.readouterr().out
    assert "feed returned post 1 twice" in out and "slug 's' used by posts 1 and 2" in out
    m = manifest(repo)["posts"]
    assert m["1"]["slug"] == "s" and m["2"]["slug"] == "s--2"
    assert (repo / "posts" / "s.html").read_text() == "<p>first</p>" and (repo / "posts" / "s--2.html").read_text() == "<p>second</p>"


def test_main_baseline_history_for_pre_versioning_posts(repo, monkeypatch):
    snapshot_once(repo, monkeypatch, [entry(pid="1", body="<p>a 1</p>")])
    mf = manifest(repo)
    del mf["posts"]["1"]["version"], mf["posts"]["1"]["version_history"]
    (repo / "meta" / "manifest.json").write_text(json.dumps(mf))
    snapshot_once(repo, monkeypatch, [entry(pid="1", body="<p>a 1</p>", upd="2026-05-05T00:00:00.000+05:30")])
    hist = manifest(repo)["posts"]["1"]["version_history"]
    assert manifest(repo)["posts"]["1"]["version"] == "1.0.0" and hist[0]["level"] == "baseline" and len(hist) == 1


def test_main_marker_changes_reported_in_changelog(repo, monkeypatch):
    snapshot_once(repo, monkeypatch, [entry(pid="1", body="<p>x</p>")])
    snapshot_once(repo, monkeypatch, [entry(pid="1", body="<p>x</p> gs-light-lock")])
    log = (repo / "CHANGELOG.md").read_text()
    assert "markers light_lock False→True" in log
    assert manifest(repo)["posts"]["1"]["version_history"][-1]["markers_changed"] == {"light_lock": [False, True]}


# --------------------------------------------------------------------- push
def commit_run(repo, monkeypatch, *extra):
    repo.feed = [entry(pid="1", body="<p>a</p>")]
    run_main(monkeypatch, "--push", *extra)
    return [c[0] for c in repo.gits]


def test_push_without_remote_changes(repo, monkeypatch, capsys):
    cmds = commit_run(repo, monkeypatch)
    names = [c[1] for c in cmds]
    assert names == ["add", "commit", "fetch", "rev-parse", "rev-list", "push"]
    assert cmds[4] == ["git", "rev-list", "--count", "HEAD..origin/main"] and cmds[5] == ["git", "push", "origin", "HEAD"]
    assert "err-push" in capsys.readouterr().out


def test_push_rebases_when_behind(repo, monkeypatch, capsys):
    repo.behind = "3\n"
    cmds = commit_run(repo, monkeypatch)
    assert [c[1] for c in cmds][-2:] == ["pull", "push"] and cmds[-2] == ["git", "pull", "--rebase", "origin", "main"]
    assert "remote moved on by 3 commit(s)" in capsys.readouterr().out


def test_push_aborts_cleanly_on_rebase_conflict(repo, monkeypatch, capsys):
    repo.behind = "2\n"
    repo.rc = {"pull": 1}
    cmds = commit_run(repo, monkeypatch)
    assert [c[1] for c in cmds][-2:] == ["pull", "rebase"] and cmds[-1] == ["git", "rebase", "--abort"]
    assert not any(c[1] == "push" for c in cmds)
    assert "rebase conflicted and was aborted" in capsys.readouterr().out


def test_push_branch_default_main_when_rev_parse_empty(repo, monkeypatch):
    orig = S.subprocess.run
    def run(cmd, **kw):
        r = orig(cmd, **kw)
        if cmd[1] == "rev-parse":
            r.stdout = ""
        return r
    monkeypatch.setattr(S.subprocess, "run", run)
    cmds = commit_run(repo, monkeypatch)
    assert ["git", "rev-list", "--count", "HEAD..origin/main"] in cmds


def test_no_commit_skips_git_entirely(repo, monkeypatch):
    repo.feed = [entry(pid="1")]
    run_main(monkeypatch, "--no-commit", "--push")
    assert repo.gits == []

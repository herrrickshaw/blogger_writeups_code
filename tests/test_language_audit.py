import json

import pytest

import language_audit as LA
from netfake import Net


def test_chunk_boundaries():
    assert LA.chunk("a\n\nb\n\nc", size=100) == ["a\n\nb\n\nc"]
    assert LA.chunk("aaaa\n\nbbbb\n\ncccc", size=8) == ["aaaa\n\nbbbb", "cccc"]               # lengths 4+4 = 8 fit, the next does not
    assert LA.chunk("", size=10) == [""]
    big = LA.chunk("x" * 20 + "\n\n" + "y" * 20, size=10)
    assert big == ["x" * 20, "y" * 20]                                  # an oversize paragraph is kept whole
    parts = LA.chunk("\n\n".join(["p" * 4] * 5), size=9)
    assert parts == ["pppp\n\npppp", "pppp\n\npppp", "pppp"] and all(len(p) <= 12 for p in parts)


def test_chunk_size_is_exclusive_of_separators():
    paras = ["a" * 5, "b" * 5]
    assert LA.chunk("\n\n".join(paras), size=10) == ["a" * 5 + "\n\n" + "b" * 5]      # 10 is not > 10
    assert LA.chunk("\n\n".join(paras), size=9) == ["a" * 5, "b" * 5]


def test_check_posts_form_encoded_with_rules(monkeypatch):
    n = Net().install(monkeypatch)
    n.queue.append({"matches": []})
    assert LA.check("hello world") == {"matches": []}
    body = n.requests[0]["body"].decode()
    assert "text=hello+world" in body and "language=en-US" in body and "disabledRules=WHITESPACE_RULE" in body
    assert "disabledCategories=TYPOGRAPHY" in body and n.requests[0]["url"] == "https://api.languagetool.org/v2/check"
    assert n.requests[0]["headers"]["User-agent"] == "vertistrat-language-audit/1.0"


@pytest.fixture
def site(tmp_path, monkeypatch):
    monkeypatch.setattr(LA, "ROOT", str(tmp_path))
    monkeypatch.setattr(LA, "OUT_DIR", str(tmp_path / "out" / "language_audit"))
    (tmp_path / "posts").mkdir()
    (tmp_path / "meta").mkdir()
    monkeypatch.setattr(LA.time, "sleep", lambda s: None)

    def add(slug, body, meta=True):
        (tmp_path / "posts" / f"{slug}.html").write_text(body, encoding="utf-8")
        if meta:
            (tmp_path / "meta" / f"{slug}.json").write_text(json.dumps({"title": f"Title {slug}", "url": f"https://b/{slug}.html"}))
    return tmp_path, add


LONG = "<p>" + "This is a long enough sentence for the audit to run on it. " * 3 + "</p>"


def match(cat="GRAMMAR", rule="R1", msg="m", ctx="ctx", repl=("a", "b", "c", "d")):
    return {"message": msg, "context": {"text": ctx}, "replacements": [{"value": r} for r in repl], "rule": {"id": rule, "category": {"id": cat}}}


def test_audit_post_filters_categories_and_trims_replacements(site, monkeypatch):
    tmp, add = site
    add("p", LONG)
    monkeypatch.setattr(LA, "check", lambda text: {"matches": [match(), match(cat="TYPOGRAPHY"), match(cat="SEMANTICS", rule="R2"), {"rule": {}}]})
    r = LA.audit_post("p")
    assert r["slug"] == "p" and r["title"] == "Title p" and r["url"] == "https://b/p.html"
    assert [m["rule"] for m in r["matches"]] == ["R1", "R2"]
    assert r["matches"][0]["replacements"] == ["a", "b", "c"] and r["matches"][0]["chunk"] == 0


def test_audit_post_none_cases(site, monkeypatch):
    tmp, add = site
    assert LA.audit_post("missing") is None
    add("short", "<p>tiny</p>")
    assert LA.audit_post("short") is None
    add("clean", LONG)
    monkeypatch.setattr(LA, "check", lambda t: {"matches": [match(cat="STYLE")]})
    assert LA.audit_post("clean") is None
    monkeypatch.setattr(LA, "check", lambda t: {})
    assert LA.audit_post("clean") is None


def test_audit_post_excludes_table_rows_and_uses_slug_title_without_meta(site, monkeypatch):
    tmp, add = site
    add("t", LONG + "<table><tr><td>cellA</td><td>cellB</td></tr></table>", meta=False)
    seen = []
    monkeypatch.setattr(LA, "check", lambda text: seen.append(text) or {"matches": [match()]})
    r = LA.audit_post("t")
    assert r["title"] == "t" and r["url"] == "" and "cellA" not in seen[0] and seen[0].startswith("t\n\n")


def test_audit_post_records_check_errors_and_chunks(site, monkeypatch):
    tmp, add = site
    add("c", "".join(f"<p>{'word ' * 400}{i}</p>" for i in range(8)))
    calls = []
    def check(text):
        calls.append(len(text))
        if len(calls) == 1:
            raise OSError("api down")
        return {"matches": [match()]}
    monkeypatch.setattr(LA, "check", check)
    sleeps = []
    monkeypatch.setattr(LA.time, "sleep", lambda s: sleeps.append(s))
    r = LA.audit_post("c", sleep_between=1.5)
    assert len(calls) >= 2 and sleeps == [1.5] * len(calls)
    assert r["matches"][0] == {"error": "api down"} and all(m.get("chunk", 1) >= 1 for m in r["matches"][1:])


def test_write_post_report_formats_errors_and_suggestions(site):
    tmp, add = site
    import os
    os.makedirs(LA.OUT_DIR)
    path = LA.write_post_report({"slug": "s", "title": "T", "url": "u", "matches": [
        {"error": "boom"}, {"category": "GRAMMAR", "rule": "R", "message": "msg", "context": "ctx", "replacements": ["x", "y"]},
        {"category": "CASING", "rule": "R2", "message": "m2", "context": "c2", "replacements": []}]})
    t = open(path, encoding="utf-8").read()
    assert path.endswith("/s.md") and t.startswith("# Language audit — T\n") and "- ERROR checking chunk: boom" in t
    assert "- **[GRAMMAR/R]** msg\n  context: ctx\n  suggested: x, y" in t and "suggested" not in t.split("m2")[1]


def run_main(monkeypatch, *argv):
    monkeypatch.setattr(LA.sys, "argv", ["la", *argv])
    LA.main()


def test_main_slug_mode(site, monkeypatch, capsys):
    tmp, add = site
    add("p", LONG)
    monkeypatch.setattr(LA, "check", lambda t: {"matches": [match()]})
    run_main(monkeypatch, "--slug", "p")
    assert json.loads(capsys.readouterr().out)["slug"] == "p"
    run_main(monkeypatch, "--slug", "ghost")
    assert capsys.readouterr().out.strip() == "ghost: 0 matches"


def test_main_full_sweep_reports_summary_and_skips_utility_pages(site, monkeypatch, capsys):
    tmp, add = site
    add("many", LONG)
    add("one", LONG)
    add("clean", LONG)
    add("about-author", LONG)
    add("article-index-start-here", LONG)
    def check(text):
        if "Title many" in text:
            return {"matches": [match(rule="A"), match(rule="B"), match(rule="C")]}
        if "Title one" in text:
            return {"matches": [match(rule="A")]}
        return {"matches": []}
    monkeypatch.setattr(LA, "check", check)
    run_main(monkeypatch)
    err = capsys.readouterr().err
    assert "many: 3 matches" in err and "clean: clean" in err and "DONE. 2 posts flagged." in err
    out = tmp / "out" / "language_audit"
    assert (out / "many.md").exists() and (out / "one.md").exists() and not (out / "clean.md").exists() and not (out / "about-author.md").exists()
    s = (out / "_summary_latest.md").read_text(encoding="utf-8")
    assert "2 of 3 posts flagged" in s
    assert s.index("Title many") < s.index("Title one") and "— 3 matches —" in s and "see `one.md`" in s
    assert list(out.glob("_summary_2*.md"))


def test_main_summary_counts_exclude_error_entries(site, monkeypatch):
    tmp, add = site
    add("e", LONG)
    calls = []
    def check(text):
        calls.append(1)
        raise RuntimeError("x")
    monkeypatch.setattr(LA, "check", check)
    run_main(monkeypatch)
    s = (tmp / "out" / "language_audit" / "_summary_latest.md").read_text(encoding="utf-8")
    assert "— 0 matches —" in s

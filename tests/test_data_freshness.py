import csv
import datetime as dt
import json
import pathlib

import pytest

import data_freshness as D
import multi_model_factcheck as mmf
from netfake import Net, http_error


@pytest.fixture(autouse=True)
def _env(monkeypatch, tmp_path):
    monkeypatch.setattr(D.time, "sleep", lambda s: None)
    monkeypatch.setattr(D, "OUT_DIR", tmp_path / "out" / "freshness")
    monkeypatch.setattr(D, "ROOT", tmp_path)
    D.COOLDOWN.clear()
    (tmp_path / "posts").mkdir()
    return tmp_path


# ---------------------------------------------------------------- parse
def dp(**kw):
    d = {"quote": "q", "value": "5%", "period": "May 2026", "period_end": "2026-05-31", "publisher": "MoSPI",
         "series": "CPI", "frequency": "monthly", "headline": True}
    d.update(kw)
    return d


def test_parse_variants():
    pts = [dp(), {"quote": "no value"}, "junk"]
    assert D.parse(json.dumps({"data_points": pts})) == [dp()]
    assert D.parse(json.dumps([dp()])) == [dp()]
    assert D.parse("```json\n" + json.dumps({"data_points": [dp()]}) + "\n```") == [dp()]
    assert D.parse("Here you go: " + json.dumps({"data_points": [dp()]}) + " thanks") == [dp()]
    assert D.parse(json.dumps({"data_points": []})) == []
    assert D.parse("not json at all") is None
    assert D.parse("{broken") is None
    assert D.parse("{ bad json }") is None
    assert D.parse(json.dumps({"other": 1})) is None
    assert D.parse(json.dumps({"data_points": "x"})) is None
    assert D.parse("42") is None


def test_failed_helper():
    assert D.failed("Gemini [API error 429: x]") and D.failed("[network error: x]") and D.failed("[empty response]")
    assert D.failed("Mistral [unexpected response: {}]")
    assert not D.failed("{}") and not D.failed("[1,2]") and not D.failed("[Gemini ok]")


# ---------------------------------------------------------------- asks
def test_post_errors(monkeypatch):
    n = Net().install(monkeypatch)
    n.queue += [{"a": 1}, http_error(429, "slow"), OSError("down")]
    assert D._post("http://x", {"b": 1}, {"X-H": "v"}) == ({"a": 1}, None)
    assert n.requests[0]["headers"]["X-h"] == "v" and n.requests[0]["headers"]["User-agent"] == mmf.UA
    d, err = D._post("http://x", {}, {})
    assert d is None and err == "[API error 429: slow]"
    d, err = D._post("http://x", {}, {})
    assert err == "[network error: down]"


def test_ask_gemini(monkeypatch):
    n = Net().install(monkeypatch)
    n.queue += [{"candidates": [{"content": {"parts": [{"text": " {a"}, {"text": "}"}]}}]}, {"candidates": []}, http_error(503, "b")]
    assert D.ask_gemini("KEY", "TXT", "mod") == "{a}"
    assert "models/mod:generateContent?key=KEY" in n.requests[0]["url"]
    body = n.json_bodies()[0]
    assert body["generationConfig"] == {"temperature": 0.0, "responseMimeType": "application/json"}
    assert "TXT" in body["contents"][0]["parts"][0]["text"]
    assert D.ask_gemini("K", "T", "m") == "[empty response]"
    assert D.ask_gemini("K", "T", "m") == "Gemini [API error 503: b]"


def test_ask_mistral(monkeypatch):
    n = Net().install(monkeypatch)
    n.queue += [{"choices": [{"message": {"content": " {x} "}}]}, {"choices": []}, http_error(429, "r"), {"bad": 1}]
    assert D.ask_mistral("K", "T", "m1") == "{x}"
    b = n.json_bodies()[0]
    assert b["model"] == "m1" and b["response_format"] == {"type": "json_object"} and b["temperature"] == 0.0
    assert n.requests[0]["headers"]["Authorization"] == "Bearer K" and n.requests[0]["url"] == mmf.MISTRAL_URL
    assert D.ask_mistral("K", "T", "m").startswith("[Mistral unexpected response: ")
    assert D.ask_mistral("K", "T", "m") == "Mistral [API error 429: r]"
    assert D.ask_mistral("K", "T", "m").startswith("[Mistral unexpected response: ")


# ----------------------------------------------------------- fallback
GOOD = json.dumps({"data_points": [dp()]})


def test_fallback_first_good_returns_and_bad_json_moves_on():
    calls = []
    def fn(k, t, m):
        calls.append(m)
        return {"a": "not json", "b": GOOD}[m]
    assert D.ask_with_fallback(fn, "K", "T", ["a", "b"]) == ("b", GOOD) and calls == ["a", "b"]


def test_fallback_429_cooldown_daily_vs_minute(monkeypatch):
    now = [1000.0]
    monkeypatch.setattr(D.time, "time", lambda: now[0])
    outs = {"a": "Gemini [API error 429: exceeded your current quota]", "b": "Gemini [API error 429: slow]", "c": GOOD}
    calls = []
    def fn(k, t, m):
        calls.append(m)
        return outs[m]
    assert D.ask_with_fallback(fn, "K", "T", ["a", "b", "c"]) == ("c", GOOD)
    assert D.COOLDOWN["a"] == 1000 + 24 * 3600 and D.COOLDOWN["b"] == 1000 + 600
    calls.clear()
    assert D.ask_with_fallback(fn, "K", "T", ["a", "b", "c"])[0] == "c" and calls == ["c"]      # a, b skipped
    now[0] = 1000 + 601
    calls.clear()
    D.ask_with_fallback(fn, "K", "T", ["a", "b", "c"])
    assert calls == ["b", "c"]                                                                   # b cooled down, a still out


def test_fallback_all_cooling_still_tries_everything_and_retries_once(monkeypatch):
    sleeps = []
    monkeypatch.setattr(D.time, "sleep", lambda s: sleeps.append(s))
    D.COOLDOWN.update({"a": 1e18, "b": 1e18})
    calls = []
    out = D.ask_with_fallback(lambda k, t, m: calls.append(m) or "Gemini [API error 500: x]", "K", "T", ["a", "b"])
    assert out[0] == "b" and calls == ["a", "b", "a", "b"] and sleeps == [45]


def test_fallback_terminal_error_returns_immediately_unless_404():
    calls = []
    out = D.ask_with_fallback(lambda k, t, m: calls.append(m) or "Gemini [API error 401: bad key]", "K", "T", ["a", "b"])
    assert out == ("a", "Gemini [API error 401: bad key]") and calls == ["a"]
    calls.clear()
    D.ask_with_fallback(lambda k, t, m: calls.append(m) or "Gemini [API error 403 404: gone]", "K", "T", ["a", "b"])
    assert calls[:2] == ["a", "b"]


# ------------------------------------------------------------- done / run_one
def write_rec(slug, **rec):
    D.OUT_DIR.mkdir(parents=True, exist_ok=True)
    (D.OUT_DIR / f"{slug}.json").write_text(json.dumps({"slug": slug, **rec}))


def test_done_logic():
    assert D.done("x", "s", ("gemini",)) is False
    write_rec("x", text_sha1="s", models={"gemini": {"ok": True}, "mistral": {"ok": False}})
    assert D.done("x", "s", ("gemini",)) is True
    assert D.done("x", "s", ("gemini", "mistral")) is False
    assert D.done("x", "other", ("gemini",)) is False
    assert D.done("x", "s", ("mistral",)) is False
    write_rec("sk", text_sha1="s", skipped="too large")
    assert D.done("sk", "s", ("gemini",)) is True and D.done("sk", "t", ("gemini",)) is False
    write_rec("e", text_sha1="s")
    assert D.done("e", "s", ("gemini",)) is False and D.done("e", "s", ()) is True


def make_post(tmp, slug="p", text="Body of the post."):
    p = tmp / "posts" / f"{slug}.html"
    p.write_text(f"<p>{text}</p>", encoding="utf-8")
    return p


def test_run_one_too_large(_env, monkeypatch):
    monkeypatch.setattr(mmf, "MAX_CHARS", 5)
    p = make_post(_env, text="x" * 6)
    assert D.run_one(p, {}, ("gemini",)) is False
    r = json.loads((D.OUT_DIR / "p.json").read_text())
    assert r["skipped"].startswith("too large: 6 chars > 5") and r["models"] == {}


def test_run_one_models_ok_failed_and_return_value(_env, monkeypatch):
    p = make_post(_env)
    monkeypatch.setattr(D, "ask_with_fallback", lambda fn, k, text, models: ("gm", GOOD) if fn is D.ask_gemini else ("mm", "[Mistral API error 500: x]"))
    assert D.run_one(p, {"gemini": "g", "mistral": "m"}, ("gemini", "mistral")) is False       # one model ok
    r = json.loads((D.OUT_DIR / "p.json").read_text())
    assert r["models"]["gemini"] == {"model": "gm", "ok": True, "data_points": [dp()]}
    assert r["models"]["mistral"]["ok"] is False and r["models"]["mistral"]["error"].startswith("[Mistral API error 500")
    assert r["text_sha1"] == mmf.text_sha(mmf.extract_text(p)) and r["chars"] == len("Body of the post.")
    q = make_post(_env, "q")
    assert D.run_one(q, {"mistral": "m"}, ("mistral",)) is True                                  # nothing ok -> all failed


def test_run_one_reuses_clean_prior_answers_at_same_text(_env, monkeypatch):
    p = make_post(_env)
    sha = mmf.text_sha(mmf.extract_text(p))
    write_rec("p", text_sha1=sha, models={"gemini": {"model": "old", "ok": True, "data_points": [dp()]},
                                          "mistral": {"model": "old", "ok": False, "data_points": [], "error": "e"}})
    asked = []
    monkeypatch.setattr(D, "ask_with_fallback", lambda fn, k, text, models: asked.append(fn.__name__) or ("new", GOOD))
    D.run_one(p, {"gemini": "g", "mistral": "m"}, ("gemini", "mistral"))
    assert asked == ["ask_mistral"]
    r = json.loads((D.OUT_DIR / "p.json").read_text())
    assert r["models"]["gemini"]["model"] == "old" and r["models"]["mistral"]["model"] == "new" and "error" not in r["models"]["mistral"]
    # prior answer at a different text is discarded
    write_rec("p", text_sha1="different", models={"gemini": {"model": "old", "ok": True, "data_points": []}})
    asked.clear()
    D.run_one(p, {"gemini": "g"}, ("gemini",))
    assert asked == ["ask_gemini"]


def test_run_one_empty_data_points_is_ok_not_failed(_env, monkeypatch):
    p = make_post(_env)
    monkeypatch.setattr(D, "ask_with_fallback", lambda *a: ("m", json.dumps({"data_points": []})))
    assert D.run_one(p, {"gemini": "g"}, ("gemini",)) is False
    assert json.loads((D.OUT_DIR / "p.json").read_text())["models"]["gemini"]["ok"] is True


# ------------------------------------------------------------ staleness
TODAY = dt.date(2026, 10, 23)


@pytest.mark.parametrize("freq,end,want", [
    ("monthly", "2026-08-31", 0),       # age 53, lag 45 -> (8 // 30.4) = 0
    ("monthly", "2026-06-30", 2),       # age 115 -> (70 // 30.4) = 2
    ("monthly", "2026-09-30", 0),
    ("quarterly", "2026-06-30", 0),     # age 115 > lag 100 but (15 // 91.3) = 0
    ("quarterly", "2025-12-31", 2),     # age 296 -> (196 // 91.3) = 2
    ("annual", "2025-03-31", 1),        # age 570 -> (420 // 365.25) = 1
    ("annual", "2026-03-31", 0),
    ("daily", "2026-10-01", 15),        # age 22 -> 15
    ("weekly", "2026-09-01", 5),
    ("half-yearly", "2026-03-31", 0),
    ("multi-year", "2020-01-01", 1),
])
def test_releases_behind_table(freq, end, want):
    n, why = D.releases_behind({"frequency": freq, "period_end": end}, TODAY)
    assert n == want and why == f"{freq}, period ended {end}"


def test_releases_behind_exact_values_and_boundaries():
    f = lambda **kw: D.releases_behind({"frequency": "monthly", "period_end": "2026-08-31", **kw}, TODAY)
    assert f()[0] == 0
    # age exactly LAG: 45 days -> 0 releases; one period (30.4d) beyond lag -> 1
    end = TODAY - dt.timedelta(days=45)
    assert D.releases_behind({"frequency": "monthly", "period_end": end.isoformat()}, TODAY)[0] == 0
    end = TODAY - dt.timedelta(days=45 + 31)
    assert D.releases_behind({"frequency": "monthly", "period_end": end.isoformat()}, TODAY)[0] == 1
    end = TODAY - dt.timedelta(days=45 + 30)
    assert D.releases_behind({"frequency": "monthly", "period_end": end.isoformat()}, TODAY)[0] == 0
    assert D.releases_behind({"frequency": "daily", "period_end": "2026-10-22"}, TODAY)[0] == 0      # age 1 < lag 7


def test_releases_behind_none_cases_and_live():
    assert D.releases_behind({"frequency": "yearly", "period_end": "2025-01-01"}, TODAY) == (None, "unknown frequency")
    assert D.releases_behind({"frequency": None, "period_end": "2025-01-01"}, TODAY) == (None, "unknown frequency")
    assert D.releases_behind({"frequency": "one-off", "period_end": "2025-01-01"}, TODAY) == (None, "one-off")
    assert D.releases_behind({"frequency": "monthly", "period_end": None}, TODAY) == (None, "no period")
    assert D.releases_behind({"frequency": "monthly", "period_end": "garbage"}, TODAY) == (None, "no period")
    assert D.releases_behind({"frequency": "monthly", "period_end": "2026-10-24"}, TODAY) == (None, "period ends after today")
    assert D.releases_behind({"frequency": "monthly", "period_end": "2026-10-23"}, TODAY)[0] == 0   # today is not "after today"
    assert D.releases_behind({"frequency": " Monthly ", "period_end": "2026-01-31T00:00"}, TODAY)[0] >= 1
    n, why = D.releases_behind({"frequency": "live", "period_end": (TODAY - dt.timedelta(days=60)).isoformat()}, TODAY)
    assert (n, why) == (0, "live reading 60 days old")
    assert D.releases_behind({"frequency": "live", "period_end": (TODAY - dt.timedelta(days=61)).isoformat()}, TODAY)[0] == 1


def test_key_of():
    assert D.key_of({"value": "US$ 1,234.5 bn", "period_end": "2026-05-31"}) == ("1234.5", "2026-05")
    assert D.key_of({"value": "5.", "period_end": "2026-05-31"}) == ("5", "2026-05")
    assert D.key_of({"value": "Many Things Here Over", "period_end": None})[0] == "many things here ove"
    assert D.key_of({"value": "no digits", "period_end": "2026-05-31"}) == ("no digits", "2026-05")
    assert D.key_of({"value": "x" * 30, "period_end": None}) == ("x" * 20, "None")


# -------------------------------------------------------------- summary
def write_post_rec(slug, models=None, **kw):
    write_rec(slug, models=models or {}, **kw)


def ok(points):
    return {"ok": True, "data_points": points}


def test_summary_frontier_scoring_and_outputs(_env):
    old_hist = dp(value="1", period="Jan 2020", period_end="2020-01-31", frequency="monthly", publisher="MoSPI")
    frontier = dp(value="5.2%", period="June 2026", period_end="2026-06-30", frequency="monthly", publisher="MoSPI", headline=True)
    current = dp(value="9", period="Sep 2026", period_end="2026-09-30", frequency="monthly", publisher="RBI", series="Repo")
    oneoff = dp(value="7", frequency="one-off", publisher="X")
    write_post_rec("stale-post", models={"gemini": ok([old_hist, frontier, current, oneoff]), "mistral": ok([dict(frontier)])})
    write_post_rec("fresh-post", models={"gemini": ok([current])})
    write_post_rec("pending-post", models={"gemini": {"ok": False, "data_points": []}})
    write_post_rec("big", skipped="too large: 200 chars")
    md, csvp = D.OUT_DIR / "S.md", D.OUT_DIR / "w.csv"
    D.summary(TODAY, md, csvp)
    rows = list(csv.DictReader(open(csvp, encoding="utf-8")))
    assert [r["slug"] for r in rows] == ["stale-post"]                  # one row: the MoSPI frontier; RBI is current
    r = rows[0]
    assert r["headline"] == "True" and r["releases_behind"] == "2" and r["models"] == "gemini+mistral"
    assert r["value"] == "5.2%" and r["period_end"] == "2026-06-30"
    text = md.read_text(encoding="utf-8")
    assert "as of 2026-10-23" in text and "### stale-post  (score 6)" in text
    assert "**H** 5.2%" in text and "~2 newer release(s), 2 figure(s) from this source [gemini+mistral]" in text
    assert "## No clean model answer yet\n\npending-post" in text and "- big: too large: 200 chars" in text
    assert "(0 older figures not listed" in text and "1 probably superseded (1 headline) across 1 posts" in text
    assert "| MoSPI: CPI | 1 |" in text


def test_summary_empty_dir(_env):
    D.OUT_DIR.mkdir(parents=True)
    D.summary(TODAY, D.OUT_DIR / "S.md", D.OUT_DIR / "w.csv")
    assert "0 data points from 0 posts; 0 probably superseded (0 headline) across 0 posts" in (D.OUT_DIR / "S.md").read_text(encoding="utf-8")
    assert list(csv.reader(open(D.OUT_DIR / "w.csv")))[0][0] == "slug"


def test_summary_ranking_headline_weight_and_cap(_env):
    a = [dp(value="1", publisher="P1", period_end="2026-04-30", headline=False)]
    b = [dp(value="2", publisher="P2", period_end="2026-06-30", headline=True)]
    write_post_rec("low", models={"gemini": ok(a)})
    write_post_rec("high", models={"gemini": ok(b)})
    D.summary(TODAY, D.OUT_DIR / "S.md", D.OUT_DIR / "w.csv")
    text = (D.OUT_DIR / "S.md").read_text(encoding="utf-8")
    # low: 4 behind, not headline -> 4 ; high: 2 behind headline -> 3*2 = 6
    assert text.index("### high") < text.index("### low")
    assert "### low  (score 4)" in text and "### high  (score 6)" in text
    rows = list(csv.DictReader(open(D.OUT_DIR / "w.csv")))
    assert rows[0]["slug"] == "high"                      # headline first in the csv


def test_summary_models_that_failed_are_ignored(_env):
    write_post_rec("m", models={"gemini": {"ok": False, "data_points": [dp(period_end="2020-01-31")]}, "mistral": ok([dp(value="8", period_end="2026-06-30")])})
    D.summary(TODAY, D.OUT_DIR / "S.md", D.OUT_DIR / "w.csv")
    rows = list(csv.DictReader(open(D.OUT_DIR / "w.csv")))
    assert [r["models"] for r in rows] == ["mistral"]


# ----------------------------------------------------------------- main
def run_main(monkeypatch, *argv):
    monkeypatch.setattr(D.sys, "argv", ["df", *argv])
    return D.main()


def test_main_summary_uses_today_arg(monkeypatch):
    got = {}
    monkeypatch.setattr(D, "summary", lambda today, md, cs: got.update(today=today, md=md, cs=cs))
    run_main(monkeypatch, "--summary", "--today", "2026-01-02")
    assert got["today"] == dt.date(2026, 1, 2) and got["md"] == D.OUT_DIR / "SUMMARY.md" and got["cs"] == D.OUT_DIR / "worklist.csv"
    run_main(monkeypatch, "--summary")
    assert got["today"] == dt.date.today()


def test_main_requires_mode_and_validates_panel(monkeypatch):
    with pytest.raises(SystemExit):
        run_main(monkeypatch)
    for bad in ("openai", "", "gemini,x"):
        with pytest.raises(SystemExit, match="--panel"):
            run_main(monkeypatch, "--slug", "p", "--panel", bad)


@pytest.fixture
def mainenv(monkeypatch, _env):
    monkeypatch.setattr(mmf, "creds", lambda: "GEMINI_API_KEY=g\nMISTRAL_API_KEY=m\n")
    calls = []
    state = {"fail": lambda f: False}
    monkeypatch.setattr(D, "run_one", lambda f, keys, panel: calls.append((pathlib.Path(f).stem, dict(keys), panel)) or state["fail"](f))
    return calls, state


def test_main_slug_and_file_pass_keys_for_panel(mainenv, monkeypatch, _env):
    calls, _ = mainenv
    run_main(monkeypatch, "--slug", "p", "--panel", "Gemini")
    assert calls == [("p", {"gemini": "g"}, ("gemini",))]
    calls.clear()
    run_main(monkeypatch, "--file", str(_env / "posts" / "z.html"))
    assert calls == [("z", {"gemini": "g", "mistral": "m"}, ("gemini", "mistral"))]


def test_main_all_resume_skip_slugs_limit_force(mainenv, monkeypatch, _env, capsys):
    calls, _ = mainenv
    for s in ("a", "b", "c", "about-author"):
        make_post(_env, s)
    sha = mmf.text_sha(mmf.extract_text(_env / "posts" / "a.html"))
    write_rec("a", text_sha1=sha, models={"gemini": {"ok": True}, "mistral": {"ok": True}})
    run_main(monkeypatch, "--all")
    assert [c[0] for c in calls] == ["b", "c"] and "resuming: 1 already done, 2 remaining" in capsys.readouterr().out
    calls.clear()
    run_main(monkeypatch, "--all", "--force", "--limit", "1")
    assert [c[0] for c in calls] == ["a"]
    calls.clear()
    run_main(monkeypatch, "--all", "--panel", "gemini", "--sleep", "3")
    assert [c[0] for c in calls] == ["b", "c"]


def test_main_all_stops_after_two_consecutive_total_failures(mainenv, monkeypatch, _env, capsys):
    calls, state = mainenv
    for s in "abcd":
        make_post(_env, s)
    state["fail"] = lambda f: True
    run_main(monkeypatch, "--all")
    assert len(calls) == 2 and "stopping early" in capsys.readouterr().out
    calls.clear()
    seq = iter([True, False, True, False])
    state["fail"] = lambda f: next(seq)
    run_main(monkeypatch, "--all", "--force")
    assert len(calls) == 4
    calls.clear()
    state["fail"] = lambda f: True
    run_main(monkeypatch, "--slug", "a")
    run_main(monkeypatch, "--slug", "a")
    assert len(calls) == 2

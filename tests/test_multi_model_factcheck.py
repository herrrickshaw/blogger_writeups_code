import json
import urllib.error

import pytest

import multi_model_factcheck as M
from netfake import Net, http_error


@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch):
    monkeypatch.setattr(M.time, "sleep", lambda s: None)


@pytest.fixture
def net(monkeypatch):
    n = Net().install(monkeypatch)
    monkeypatch.setattr(M.time, "sleep", lambda s: None)
    return n


# ------------------------------------------------------------- credentials
def test_creds_missing_exits(monkeypatch, tmp_path):
    monkeypatch.setattr(M, "CREDS", tmp_path / "none.env")
    with pytest.raises(SystemExit, match="credentials file not found"):
        M.creds()


def test_creds_reads_text(monkeypatch, tmp_path):
    f = tmp_path / "c.env"
    f.write_text("A=1\n")
    monkeypatch.setattr(M, "CREDS", f)
    assert M.creds() == "A=1\n"


def test_key_and_key_optional():
    blob = "FOO=bar baz \nXFOO=no\nEMPTY=\n"
    assert M.key("FOO", blob) == "bar baz"
    assert M.key("EMPTY", blob) == ""
    assert M.key_optional("FOO", blob) == "bar baz"
    assert M.key_optional("MISSING", blob) is None
    with pytest.raises(SystemExit, match="MISSING not in"):
        M.key("MISSING", blob)
    assert M.key("FOO", "  FOO=indented\nFOO=real") == "real"      # anchored at line start


# ----------------------------------------------------------- text helpers
def test_extract_text_strips_and_formats(tmp_path):
    f = tmp_path / "p.html"
    f.write_text("<style>x{}</style><script>var a;</script><p>Keep &amp; this</p><s>retracted 99</s>"
                 "<table><tr><td>a</td><td>b</td></tr><tr><th>c</th></tr></table>\n\n\n<p>end</p>", encoding="utf-8")
    t = M.extract_text(f)
    assert "retracted" not in t and "var a" not in t and "x{}" not in t
    assert "Keep & this" in t
    assert "a | b |" in t.replace("  ", " ") and "\n" in t
    assert "\n\n" not in t


def test_text_sha_stable_and_16_chars():
    assert M.text_sha("a") == M.text_sha("a") != M.text_sha("b")
    assert len(M.text_sha("a")) == 16
    assert M.text_sha("é") == M.text_sha("é")


def test_failed_and_terminal():
    assert M.failed("[Gemini API error 429: x]") and M.failed("[Mistral network error: x]")
    assert not M.failed("FACTUAL ERRORS:\n- none found")
    for s in ("insufficient balance", "Payment_Required", "payment required", "exceeded_current_quota",
              "API error 401", "API error 402 x", "API error 403"):
        assert M.TERMINAL.search(s), s
    for s in ("API error 429", "API error 4010", "API error 500", "network error"):
        assert not M.TERMINAL.search(s), s


# ----------------------------------------------------------------- ask_*
OK_CHAT = {"choices": [{"message": {"content": "  answer  "}}]}


@pytest.mark.parametrize("fn,args,label", [
    (M.ask_groq, ("K", "model-x", "TEXT"), "Groq/model-x"),
    (M.ask_kimi, ("K", "TEXT"), "Kimi"),
    (M.ask_mistral, ("K", "TEXT"), "Mistral"),
    (M.ask_cerebras, ("K", "TEXT"), "Cerebras"),
])
def test_chat_providers_success_errors_and_shape(net, fn, args, label):
    net.queue += [OK_CHAT, http_error(429, "slow down"), urllib.error.URLError("dns"), {"choices": []}, {"nochoices": 1}, OSError("reset")]
    assert fn(*args) == "answer"
    req = net.requests[0]
    assert req["headers"]["Authorization"] == "Bearer K" and "TEXT" in json.loads(req["body"])["messages"][0]["content"]
    assert json.loads(req["body"])["temperature"] == 0.1
    assert fn(*args) == f"[{label} API error 429: slow down]"
    assert fn(*args) == f"[{label} network error: <urlopen error dns>]"
    assert fn(*args).startswith(f"[{label} unexpected response: ")
    assert fn(*args) == f"[{label} unexpected response: {json.dumps({'nochoices': 1})}]"
    assert fn(*args) == f"[{label} network error: reset]"


def test_ask_groq_and_mistral_model_in_body_and_defaults(net):
    net.queue += [OK_CHAT, OK_CHAT, OK_CHAT]
    M.ask_groq("K", "my-model", "t")
    M.ask_mistral("K", "t")
    M.ask_mistral("K", "t", model="custom")
    b = net.json_bodies()
    assert [x["model"] for x in b] == ["my-model", M.MISTRAL_MODEL, "custom"]
    assert net.requests[1]["url"] == M.MISTRAL_URL
    assert net.requests[0]["headers"]["User-agent"] == M.UA


def test_ask_gemini_success_url_and_errors(net):
    ok = {"candidates": [{"content": {"parts": [{"text": " a"}, {"text": "b "}]}}]}
    net.queue += [ok, {"candidates": []}, {}, http_error(503, "busy"), urllib.error.URLError("x"), OSError("y")]
    assert M.ask_gemini("KEY", "T") == "ab"
    assert net.requests[0]["url"] == f"https://generativelanguage.googleapis.com/v1beta/models/{M.GEMINI_MODEL}:generateContent?key=KEY"
    assert net.json_bodies()[0]["generationConfig"] == {"temperature": 0.1}
    assert M.ask_gemini("K", "T", model="other") == "[empty response]"
    assert "models/other:" in net.requests[1]["url"]
    assert M.ask_gemini("K", "T") == "[empty response]"
    assert M.ask_gemini("K", "T") == "[Gemini API error 503: busy]"
    assert M.ask_gemini("K", "T") == "[Gemini network error: <urlopen error x>]"
    assert M.ask_gemini("K", "T") == "[Gemini network error: y]"


def test_ask_error_body_truncated_to_300(net):
    net.queue.append(http_error(500, "z" * 500))
    assert M.ask_kimi("K", "T") == "[Kimi API error 500: " + "z" * 300 + "]"


# --------------------------------------------------------------- groq pick
def models(*ids):
    return {"data": [{"id": i} for i in ids]}


def test_groq_pick_model_env_override_wins(monkeypatch, net):
    monkeypatch.setenv("GROQ_MODEL", "pinned")
    assert M.groq_pick_model("K") == "pinned" and net.requests == []


@pytest.mark.parametrize("ids,want", [
    (["whisper-large", "llama-3.3-70b-versatile", "gpt-oss-120b"], "llama-3.3-70b-versatile"),
    (["gpt-oss-120b", "meta/llama-4-scout", "qwen3"], "meta/llama-4-scout"),
    (["whisper-x", "gpt-oss-120b", "qwen3-32b"], "gpt-oss-120b"),
    (["qwen3-32b", "gpt-oss-20b"], "qwen3-32b"),
    (["something-else", "llama-guard-3", "compound-beta"], "something-else"),
    (["llama-guard", "whisper", "tts-x", "orpheus-y", "playai-z", "embed-q", "vision-r"], M.GROQ_MODELS[0]),
    ([], M.GROQ_MODELS[0]),
    (["my-70b-chat", "llama-x"], "my-70b-chat"),
])
def test_groq_pick_model_preference(monkeypatch, net, ids, want):
    monkeypatch.delenv("GROQ_MODEL", raising=False)
    net.queue.append(models(*ids))
    assert M.groq_pick_model("K") == want
    assert net.requests[0]["headers"]["Authorization"] == "Bearer K"


def test_groq_pick_model_listing_failure_falls_back(monkeypatch, net, capsys):
    monkeypatch.delenv("GROQ_MODEL", raising=False)
    net.queue.append(http_error(500))
    assert M.groq_pick_model("K") == M.GROQ_MODELS[0]
    assert "could not list models" in capsys.readouterr().err


# ------------------------------------------------------------------- probe
def test_probe_ok_terminal_and_transient(capsys):
    assert M.probe("L", lambda k, t: "OK", "K") == (True, "")
    ok, reason = M.probe("L", lambda k, t: "[Kimi API error 429: insufficient balance]", "K")
    assert not ok and "insufficient balance" in reason
    assert M.probe("L", lambda k, t: "[Cerebras API error 402: pay]", "K")[0] is False
    ok, reason = M.probe("L", lambda k, t: "[Kimi API error 429: rate limit]", "K")
    assert (ok, reason) == (True, "") and "keeping it in the panel" in capsys.readouterr().err
    assert M.probe("L", lambda k, t: "[X network error: y]", "K")[0] is True
    seen = {}
    M.probe("L", lambda k, t: seen.update(p=t) or "OK", "K")
    assert seen["p"] == "Reply with the single word OK."


# --------------------------------------------------------- ask_with_fallback
def test_ask_with_fallback_order_terminal_and_retry(monkeypatch):
    sleeps = []
    monkeypatch.setattr(M.time, "sleep", lambda s: sleeps.append(s))
    calls = []
    def fn(k, text, m):
        calls.append(m)
        return {"a": "[X API error 503: busy]", "b": "good"}[m]
    assert M.ask_with_fallback(fn, "K", "T", ["a", "b"]) == ("b", "good") and calls == ["a", "b"] and sleeps == []
    calls.clear()
    assert M.ask_with_fallback(lambda k, t, m: calls.append(m) or "[X API error 503: x]", "K", "T", ["a", "b"]) == ("b", "[X API error 503: x]")
    assert calls == ["a", "b", "a", "b"] and sleeps == [45]
    calls.clear()
    out = M.ask_with_fallback(lambda k, t, m: calls.append(m) or "[X API error 401: bad key]", "K", "T", ["a", "b"])
    assert out == ("a", "[X API error 401: bad key]") and calls == ["a"]
    calls.clear()
    out = M.ask_with_fallback(lambda k, t, m: calls.append(m) or ("[X API error 402 404: gone]" if m == "a" else "fine"), "K", "T", ["a", "b"])
    assert out == ("b", "fine") and calls == ["a", "b"]           # 404 text means: try the next model


def test_ask_with_fallback_recovers_on_second_pass(monkeypatch):
    monkeypatch.setattr(M.time, "sleep", lambda s: None)
    seq = iter(["[X API error 429: x]", "[X API error 429: x]", "ok"])
    assert M.ask_with_fallback(lambda k, t, m: next(seq), "K", "T", ["a", "b"]) == ("a", "ok")


# ------------------------------------------------------------ report state
@pytest.fixture
def out_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(M, "ROOT", tmp_path)
    monkeypatch.setattr(M, "OUT_DIR", tmp_path / "out" / "factcheck")
    (tmp_path / "out" / "factcheck").mkdir(parents=True)
    (tmp_path / "posts").mkdir()
    monkeypatch.setattr(M, "REQUIRED_MODELS", ("Gemini", "Groq", "Mistral"))
    return tmp_path


def test_report_sha_and_already_done(out_dir):
    d = M.OUT_DIR
    assert M.report_sha("none") is None and M.already_done("none") is False
    (d / "a.md").write_text("# x\nText-SHA1: `abc123`\n## Gemini m\n\nfine\n\n## Groq m\nok\n")
    assert M.report_sha("a") == "abc123" and M.already_done("a") is True
    (d / "b.md").write_text("# x\n\n## Gemini m\n\n[Gemini API error 429: x]\n\n## Groq m\nok\n")
    assert M.already_done("b") is False and M.report_sha("b") is None
    (d / "c.md").write_text("# x\n[SKIPPED: too large — 1 chars]")
    assert M.already_done("c") is True
    (d / "d.md").write_text("# x\n\n## Kimi m\nok\n")                    # no required-model section
    assert M.already_done("d") is False
    (d / "e.md").write_text("# x\n\n## Gemini m\nok\n\n## Kimi m\n[Kimi API error 402: x]\n")
    assert M.already_done("e") is True                                    # best-effort failures don't count


# ------------------------------------------------------------------ run_one
def post(out_dir, slug="p", text="Body text."):
    p = out_dir / "posts" / f"{slug}.html"
    p.write_text(f"<p>{text}</p>", encoding="utf-8")
    return p


def test_run_one_too_large_skips_and_writes_note(out_dir, monkeypatch, net, capsys):
    monkeypatch.setattr(M, "MAX_CHARS", 10)
    p = post(out_dir, text="x" * 11)
    path, failed = M.run_one(p, "g", "q", "m", None, None)
    assert failed is False and net.requests == []
    text = path.read_text(encoding="utf-8")
    assert "SKIPPED: too large" in text and "11 chars exceeds the 10-char cap" in text
    p2 = post(out_dir, slug="q", text="x" * 10)           # exactly at the cap is sent
    monkeypatch.setattr(M, "ask_gemini", lambda k, t, m=None: "G")
    path, _ = M.run_one(p2, "g", "q", "m", None, None, panel=("gemini",))
    assert "SKIPPED" not in path.read_text(encoding="utf-8")


def test_run_one_full_panel_report_structure(out_dir, monkeypatch, net):
    monkeypatch.setattr(M, "GROQ_MODELS", ["gm"])
    monkeypatch.setattr(M, "ask_gemini", lambda k, t, m=None: f"gem:{m}")
    monkeypatch.setattr(M, "ask_groq", lambda k, m, t: f"groq:{m}")
    monkeypatch.setattr(M, "ask_mistral", lambda k, t, m=None: f"mis:{m}")
    monkeypatch.setattr(M, "ask_kimi", lambda k, t: "kimi")
    monkeypatch.setattr(M, "ask_cerebras", lambda k, t: "cer")
    path, all_failed = M.run_one(post(out_dir), "g", "q", "m", "kk", "ck", skipped=[("X", "why")])
    t = path.read_text(encoding="utf-8")
    assert all_failed is False
    assert f"Text-SHA1: `{M.text_sha('Body text.')}`" in t
    assert "Panel: **5 of 6 configured models** answered.  Skipped this run: X (why)." in t
    for h in (f"## Gemini {M.GEMINI_MODEL}", "## Groq gm", f"## Mistral {M.MISTRAL_MODEL}", f"## Kimi {M.KIMI_MODEL}", f"## Cerebras {M.CEREBRAS_MODEL}"):
        assert h in t
    assert "gem:" + M.GEMINI_MODEL in t and "groq:gm" in t and "Source: `posts/p.html`" in t


def test_run_one_narrow_panel_and_all_failed_flag(out_dir, monkeypatch):
    monkeypatch.setattr(M, "ask_gemini", lambda k, t, m=None: "[Gemini API error 503: x]")
    monkeypatch.setattr(M, "ask_mistral", lambda k, t, m=None: "fine")
    monkeypatch.setattr(M, "ask_groq", lambda *a: pytest.fail("groq should not run"))
    p = post(out_dir)
    path, all_failed = M.run_one(p, "g", None, "m", None, None, panel=("gemini",))
    assert all_failed is True and "Panel: **1 of 1" in path.read_text(encoding="utf-8")
    path, all_failed = M.run_one(p, "g", None, "m", None, None, panel=("gemini", "mistral"))
    assert all_failed is False                                             # one required model answered
    path, _ = M.run_one(p, "g", None, "m", None, None, panel=("mistral",))
    assert "Skipped this run" not in path.read_text(encoding="utf-8")


def test_run_one_best_effort_failures_do_not_count_as_all_failed(out_dir, monkeypatch):
    monkeypatch.setattr(M, "ask_gemini", lambda k, t, m=None: "[Gemini API error 503: x]")
    monkeypatch.setattr(M, "ask_kimi", lambda k, t: "kimi fine")
    path, all_failed = M.run_one(post(out_dir), "g", None, None, "kk", None, panel=("gemini",))
    assert all_failed is True


# --------------------------------------------------------------------- main
def run_main(monkeypatch, *argv):
    monkeypatch.setattr(M.sys, "argv", ["mmf", *argv])
    M.main()


@pytest.fixture
def mainenv(out_dir, monkeypatch):
    f = out_dir / "c.env"
    f.write_text("GEMINI_API_KEY=g\nGROQ_API_KEY=q\nMISTRAL_API_KEY=m\nMOONSHOT_API_KEY=k\nCEREBRAS_API_KEY=c\n")
    monkeypatch.setattr(M, "CREDS", f)
    monkeypatch.delenv("GROQ_MODEL", raising=False)
    monkeypatch.setattr(M.time, "sleep", lambda s: None)
    calls = []
    def run_one(path, gk, qk, mk, kk, ck, skipped=(), panel=()):
        calls.append(dict(path=str(path).rsplit("/", 1)[-1], keys=(gk, qk, mk, kk, ck), skipped=list(skipped), panel=panel))
        return path, M_STATE["fail"](path)
    M_STATE = {"fail": lambda p: False}
    monkeypatch.setattr(M, "run_one", run_one)
    monkeypatch.setattr(M, "groq_pick_model", lambda k: "picked")
    monkeypatch.setattr(M, "probe", lambda label, fn, k: (True, ""))
    return calls, M_STATE


def test_main_probe_models(mainenv, monkeypatch, capsys):
    outs = {"gemini": "[Gemini API error 404: gone]", "ok": "OK sure"}
    monkeypatch.setattr(M, "ask_gemini", lambda k, t, m: outs["gemini"] if m != M.GEMINI_MODEL else outs["ok"])
    monkeypatch.setattr(M, "ask_mistral", lambda k, t, m: outs["ok"])
    run_main(monkeypatch, "--probe-models")
    out = capsys.readouterr().out
    assert f"Gemini   {M.GEMINI_MODEL}" in out and "ok   OK sure" in out and "FAIL [Gemini API error 404: gone]" in out
    assert out.count("Mistral ") == len([M.MISTRAL_MODEL] + M.MISTRAL_FALLBACKS)


def test_main_validates_panel_and_requires_target(mainenv, monkeypatch):
    with pytest.raises(SystemExit, match="unknown model"):
        run_main(monkeypatch, "--slug", "p", "--panel", "gemini,bogus")
    with pytest.raises(SystemExit, match="unknown model"):
        run_main(monkeypatch, "--slug", "p", "--panel", ",")
    with pytest.raises(SystemExit) as e:
        run_main(monkeypatch)
    assert e.value.code == 2


def test_main_slug_full_panel_gets_all_keys_and_probes(mainenv, monkeypatch, out_dir):
    calls, _ = mainenv
    post(out_dir)
    probes = []
    monkeypatch.setattr(M, "probe", lambda label, fn, k: probes.append(label) or ((label != "Kimi"), "dead"))
    run_main(monkeypatch, "--slug", "p")
    assert calls[0]["keys"] == ("g", "q", "m", None, "c") and calls[0]["skipped"] == [("Kimi", "dead")]
    assert probes == ["Kimi", "Cerebras"] and M.GROQ_MODELS == ["picked"]
    assert M.REQUIRED_MODELS == ("Gemini", "Groq", "Mistral")


def test_main_narrow_panel_drops_optional_and_other_keys(mainenv, monkeypatch, out_dir):
    calls, _ = mainenv
    post(out_dir)
    run_main(monkeypatch, "--slug", "p", "--panel", "gemini, mistral")
    assert calls[0]["keys"] == ("g", None, "m", None, None) and M.REQUIRED_MODELS == ("Gemini", "Mistral")


def test_main_missing_file_skipped_and_file_arg(mainenv, monkeypatch, out_dir, capsys):
    calls, _ = mainenv
    run_main(monkeypatch, "--slug", "ghost")
    assert calls == [] and "skip (not found)" in capsys.readouterr().err
    p = post(out_dir, "named")
    run_main(monkeypatch, "--file", str(p))
    assert [c["path"] for c in calls] == ["named.html"]


def test_main_all_resumes_skips_slugs_limit_and_force(mainenv, monkeypatch, out_dir, capsys):
    calls, _ = mainenv
    for s in ("a", "b", "c", "about-author"):
        post(out_dir, s)
    (M.OUT_DIR / "a.md").write_text("# x\nText-SHA1: `0`\n## Gemini m\nok\n## Groq m\nok\n## Mistral m\nok\n")
    run_main(monkeypatch, "--all")
    assert [c["path"] for c in calls] == ["b.html", "c.html"] and "resuming: 1 already done, 2 remaining" in capsys.readouterr().out
    calls.clear()
    run_main(monkeypatch, "--all", "--force", "--limit", "2")
    assert [c["path"] for c in calls] == ["a.html", "b.html"]
    calls.clear()
    run_main(monkeypatch, "--all", "--stale")                             # a's hash (0) differs from the text's
    assert [c["path"] for c in calls] == ["a.html", "b.html", "c.html"]


def test_main_all_stops_after_two_consecutive_failures_and_resets(mainenv, monkeypatch, out_dir, capsys):
    calls, state = mainenv
    for s in "abcde":
        post(out_dir, s)
    state["fail"] = lambda p: __import__("pathlib").Path(p).stem in ("a", "b")
    run_main(monkeypatch, "--all", "--sleep", "1")
    assert [c["path"] for c in calls] == ["a.html", "b.html"]
    out = capsys.readouterr().out
    assert "stopping early: 2 posts in a row failed" in out and "3 posts left" in out
    calls.clear()
    state["fail"] = lambda p: __import__("pathlib").Path(p).stem in ("a", "c")                      # not consecutive: keeps going
    run_main(monkeypatch, "--all", "--force")
    assert len(calls) == 5
    calls.clear()
    state["fail"] = lambda p: True
    run_main(monkeypatch, "--file", str(M.ROOT / "posts" / "a.html"))
    run_main(monkeypatch, "--slug", "a")                                  # single-post runs never stop early
    assert len(calls) == 2

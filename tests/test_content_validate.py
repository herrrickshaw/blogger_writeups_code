import io
import json
import types
import urllib.error

import pytest

import content_validate as C


# --------------------------------------------------------------- extraction
BODY = """<h1>Big <b>Title</b></h1><p>Published 12 March 2026 by us.</p>
<script>var hidden = 1</script><style>p{}</style><svg><text>chart secret</text></svg>
<table><tr><th>A</th><th>B &amp; C</th></tr><tr><td>1</td><td>2</td></tr></table><table></table>
<table><tr></tr></table>
<svg viewBox="0 0 1 1"><text>L1</text><text> </text><text>L2</text></svg><svg><rect/></svg>
<figure><figcaption>Cap <i>one</i></figcaption></figure>"""


def test_clean_strips_tags_entities_space():
    assert C.clean("<p>a&amp;  b\n<b>c</b></p>") == "a& b c"
    assert C.clean("") == ""


def test_extract_all_parts():
    ex = C.extract(BODY)
    assert ex["title"] == "Big Title"
    assert ex["date"] == "12 March 2026"
    assert "hidden" not in ex["prose"] and "secret" not in ex["prose"] and "p{}" not in ex["prose"]
    assert ex["tables"] == ["A | B & C\n1 | 2"]
    assert ex["charts"] == ["chart secret", "L1 | L2"]
    assert ex["captions"] == ["Cap one"]


def test_extract_defaults_when_missing():
    ex = C.extract("<p>nothing 5 here</p>")
    assert ex["title"] == "" and ex["date"] == "unknown" and ex["tables"] == [] and ex["charts"] == []


@pytest.mark.parametrize("text,date", [("on 1 May 2026.", "1 May 2026"), ("on 1 May 2100", "unknown"),
                                      ("on 5 may 2026", "unknown"), ("1 May 1999", "unknown"), ("11 June 2025", "11 June 2025"),
                                      ("111 June 2025", "unknown")])
def test_extract_date_pattern(text, date):
    assert C.extract(f"<p>{text}</p>")["date"] == date


# --------------------------------------------------------------- node check
class Run:
    def __init__(self, node_ok=True, bad_markers=("BAD",)):
        self.calls, self.node_ok, self.bad = [], node_ok, bad_markers

    def __call__(self, cmd, **kw):
        self.calls.append(cmd)
        if cmd[1] == "--version":
            if not self.node_ok:
                raise FileNotFoundError("node")
            return types.SimpleNamespace(returncode=0)
        code = open(cmd[2]).read()
        return types.SimpleNamespace(returncode=1 if any(m in code for m in self.bad) else 0)


def test_node_check_none_without_node(monkeypatch):
    monkeypatch.setattr(C.subprocess, "run", Run(node_ok=False))
    assert C.node_check("<script>x</script>") is None


def test_node_check_indices_and_skips(monkeypatch):
    run = Run()
    monkeypatch.setattr(C.subprocess, "run", run)
    body = ('<script>ok()</script><script src="x.js"></script><script> </script>'
            '<script type="application/ld+json">{"BAD":1}</script><script>BAD(</script>'
            '<script type="module">m()</script><script type="text/javascript">BAD</script><script type=\'text/x\'>BAD</script>')
    assert C.node_check(body) == [5, 7]
    checked = [c for c in run.calls if c[1] == "--check"]
    assert len(checked) == 4                       # ok, BAD(, module, text/javascript


def test_node_check_cleans_up_temp_files(monkeypatch):
    seen = []
    def run(cmd, **kw):
        if cmd[1] == "--check":
            seen.append(cmd[2])
        return types.SimpleNamespace(returncode=0)
    monkeypatch.setattr(C.subprocess, "run", run)
    C.node_check("<script>a()</script>")
    import os
    assert seen and not os.path.exists(seen[0])


def test_run_house_rules_passes_node_result_and_traps_rule_errors(monkeypatch):
    monkeypatch.setattr(C, "node_check", lambda body: [2])
    got = {}
    def good(body, node_check=None):
        got["nc"] = node_check
        return True, ""
    def boom(body, **kw):
        raise KeyError("x")
    monkeypatch.setattr(C, "STATIC_RULES", [("r1", "BLOCKER", good), ("r2", "MINOR", boom)])
    rows = C.run_house_rules("body")
    assert got["nc"] == [2]
    assert rows[0] == ("r1", "BLOCKER", True, "")
    assert rows[1] == ("r2", "MINOR", False, "rule error: 'x'")


# --------------------------------------------------------------------- LLM
class Resp:
    def __init__(self, obj):
        self.data = json.dumps(obj).encode()
    def read(self):
        return self.data
    def __enter__(self):
        return self
    def __exit__(self, *a):
        return False


def http_err(code, body="x"):
    return urllib.error.HTTPError("u", code, "m", {}, io.BytesIO(body.encode()))


@pytest.fixture
def net(monkeypatch):
    state = {"queue": [], "reqs": [], "sleeps": []}
    def urlopen(req, payload, timeout=None):
        state["reqs"].append((req.full_url, req.get_method(), payload, dict(req.header_items()), timeout))
        item = state["queue"].pop(0)
        if isinstance(item, Exception):
            raise item
        return Resp(item)
    monkeypatch.setattr(C.urllib.request, "urlopen", urlopen)
    monkeypatch.setattr(C.time, "sleep", lambda s: state["sleeps"].append(s))
    return state


def test_llm_req_get_post_headers_and_auth(net):
    llm = C.LLM("http://h/v1/", "KEY", "m", 30)
    net["queue"] += [{"ok": 1}, {"ok": 2}]
    assert llm._req("/models") == {"ok": 1}
    assert llm._req("/chat", {"a": 1}) == {"ok": 2}
    (u1, m1, p1, h1, t1), (u2, m2, p2, h2, _) = net["reqs"]
    assert (u1, m1, p1, t1) == ("http://h/v1/models", "GET", None, 30)
    assert (u2, m2, json.loads(p2)) == ("http://h/v1/chat", "POST", {"a": 1})
    assert h1["Authorization"] == "Bearer KEY" and h1["Content-type"] == "application/json"
    noauth = C.LLM("http://h", None, "m", 5)
    net["queue"].append({})
    noauth._req("/x")
    assert "Authorization" not in net["reqs"][-1][3]


def test_llm_req_retries_transient_http_with_doubling_backoff_then_gives_up(net):
    llm = C.LLM("http://h", None, "m", 5)
    net["queue"] += [http_err(429), http_err(503), http_err(500), http_err(502)]
    with pytest.raises(RuntimeError, match="HTTP 502"):
        llm._req("/x", {})
    assert net["sleeps"] == [2.0, 4.0, 8.0] and len(net["reqs"]) == 4


def test_llm_req_recovers_after_retry(net):
    llm = C.LLM("http://h", None, "m", 5)
    net["queue"] += [http_err(504), {"ok": True}]
    assert llm._req("/x", {}) == {"ok": True} and net["sleeps"] == [2.0]


@pytest.mark.parametrize("code", [400, 401, 404, 422])
def test_llm_req_non_transient_http_fails_immediately(net, code):
    llm = C.LLM("http://h", None, "m", 5)
    net["queue"].append(http_err(code, "bad"))
    with pytest.raises(RuntimeError, match=f"HTTP {code}: bad"):
        llm._req("/x", {})
    assert net["sleeps"] == []


def test_llm_req_network_error(net):
    net["queue"].append(urllib.error.URLError("refused"))
    with pytest.raises(RuntimeError, match="network: refused"):
        C.LLM("http://h", None, "m", 5)._req("/x")


def test_pick_model(net):
    llm = C.LLM("http://h", None, "given", 5)
    assert llm.pick_model() == "given" and net["reqs"] == []
    llm = C.LLM("http://h", None, None, 5)
    net["queue"].append({"data": [{"id": None}, {"id": "m1"}, {"id": "m2"}]})
    assert llm.pick_model() == "m1" and llm.model == "m1"
    llm = C.LLM("http://h", None, None, 5)
    net["queue"].append({"data": []})
    with pytest.raises(RuntimeError, match="listed no models"):
        llm.pick_model()


def chat(content, finish="stop"):
    return {"choices": [{"message": {"content": content}, "finish_reason": finish}]}


def test_one_call_payload_nonce_and_none_content(net):
    llm = C.LLM("http://h", None, "mm", 5)
    net["queue"] += [chat("hi", "stop"), chat(None, "length")]
    assert llm._one_call("SYS", "USER", 123) == ("hi", "stop")
    assert llm._one_call("SYS", "USER", 123) == ("", "length")
    p1, p2 = (json.loads(r[2]) for r in net["reqs"])
    assert p1["model"] == "mm" and p1["temperature"] == 0 and p1["max_tokens"] == 123
    assert p1["messages"][0] == {"role": "system", "content": "SYS"}
    assert p1["messages"][1]["content"].startswith("USER\n\n<!-- cache-bust: ")
    assert p1["messages"][1]["content"] != p2["messages"][1]["content"]


def test_json_chat_parses_fenced_and_embedded_json(net):
    llm = C.LLM("http://h", None, "m", 5)
    net["queue"].append(chat('```json\n{"a": 1}\n```'))
    assert llm.json_chat("S", "U") == {"a": 1}
    net["queue"].append(chat('Sure! {"a": {"b": 2}} done'))
    assert llm.json_chat("S", "U") == {"a": {"b": 2}}


def test_json_chat_repairs_raw_newlines_inside_strings(net):
    llm = C.LLM("http://h", None, "m", 5)
    net["queue"].append(chat('{"note": "line1\nline2", "n": 1}'))
    assert llm.json_chat("S", "U") == {"note": "line1\nline2", "n": 1}


def test_json_chat_retries_with_strict_prompt_and_doubles_budget(net):
    llm = C.LLM("http://h", None, "m", 5)
    net["queue"] += [chat("no json here", "length"), chat("still none"), chat('{"ok": true}')]
    assert llm.json_chat("SYS", "U", max_tokens=100) == {"ok": True}
    ps = [json.loads(r[2]) for r in net["reqs"]]
    assert [p["max_tokens"] for p in ps] == [100, 200, 400]
    assert ps[0]["messages"][0]["content"] == "SYS"
    assert "Output format is mandatory" in ps[1]["messages"][0]["content"] and "Output format is mandatory" in ps[2]["messages"][0]["content"]


def test_json_chat_gives_up_with_last_error(net):
    llm = C.LLM("http://h", None, "m", 5)
    net["queue"] += [chat("nope")] * 3
    with pytest.raises(RuntimeError, match="model returned no JSON object .*budget=400"):
        llm.json_chat("S", "U", max_tokens=100)


def test_json_chat_unparseable_truncated_retries_but_complete_does_not_double(net):
    llm = C.LLM("http://h", None, "m", 5)
    net["queue"] += [chat('{"a": [1, 2', "length"), chat('{"a": 1}')]
    # no closing brace -> start>=0 but end<0 -> treated as no JSON, budget doubles
    assert llm.json_chat("S", "U", max_tokens=50) == {"a": 1}
    assert json.loads(net["reqs"][1][2])["max_tokens"] == 100
    net["reqs"].clear()
    net["queue"] += [chat('{"a": nope}', "length"), chat('{"a": 1}')]
    assert llm.json_chat("S", "U", max_tokens=50) == {"a": 1}
    assert json.loads(net["reqs"][1][2])["max_tokens"] == 100            # truncated + bad json -> doubled
    net["reqs"].clear()
    net["queue"] += [chat('{"a": nope}', "stop"), chat('{"a": nope}', "stop"), chat('{"a": 1}', "stop")]
    assert llm.json_chat("S", "U", max_tokens=50) == {"a": 1}
    assert [json.loads(r[2])["max_tokens"] for r in net["reqs"]] == [50, 50, 50]     # not truncated -> same budget


def test_json_chat_unparseable_all_attempts_message(net):
    llm = C.LLM("http://h", None, "m", 5)
    net["queue"] += [chat('{"a": nope}', "stop")] * 3
    with pytest.raises(RuntimeError, match="unparseable JSON after repair"):
        llm.json_chat("S", "U")


@pytest.mark.parametrize("src,want", [
    ('{"a": "x\ny"}', '{"a": "x\\ny"}'),
    ('{"a": "x\r\ny"}', '{"a": "x\\r\\ny"}'),
    ('{\n"a": 1\n}', '{\n"a": 1\n}'),
    ('{"a": "q\\"\nz"}', '{"a": "q\\"\\nz"}'),
    ('{"a": "back\\\\"\n}', '{"a": "back\\\\"\n}'),
    ('{"a": "\\n"}', '{"a": "\\n"}'),
])
def test_escape_newlines_in_strings(src, want):
    assert C._escape_newlines_in_strings(src) == want


# --------------------------------------------------------------- evidence
EX = {"title": "T", "date": "1 May 2026", "prose": "p" * 20, "tables": ["t1", "t2"], "charts": ["c1"], "captions": ["cap"]}


def test_evidence_layout_and_truncation():
    e = C.evidence(EX)
    assert e == ("POST TITLE: T\nPOST DATE (as printed): 1 May 2026\nPROSE:\n" + "p" * 20 +
                 "\nTABLE 1:\nt1\nTABLE 2:\nt2\nCHART 1 TEXT LABELS:\nc1\nCAPTION 1:\ncap")
    e = C.evidence(EX, prose_cap=5)
    assert "ppppp\n[prose truncated at 5 chars]" in e and "p" * 6 not in e
    assert "truncated" not in C.evidence(EX, prose_cap=20)          # equal length: not truncated
    assert "truncated" in C.evidence(EX, prose_cap=19)
    assert "truncated" not in C.evidence({**EX, "prose": "x" * 14001}, prose_cap=14001)
    assert "[prose truncated at 14000 chars]" in C.evidence({**EX, "prose": "x" * 14001})


def test_test_functions_send_prompt_and_budget():
    calls = []
    llm = types.SimpleNamespace(json_chat=lambda s, u, max_tokens: calls.append((s, u, max_tokens)) or {"ok": 1})
    assert C.test_consistency(llm, EX, prose_cap=5) == {"ok": 1}
    assert C.test_claims(llm, EX) == {"ok": 1}
    assert calls[0][2] == 8000 and calls[1][2] == 10000
    assert "Internal consistency audit" in calls[0][1] and "[prose truncated at 5 chars]" in calls[0][1]
    assert "Claims ledger" in calls[1][1] and calls[0][0] == C.SYSTEM


# ------------------------------------------------------------------ report
@pytest.fixture
def out(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "OUT_DIR", tmp_path / "validation")
    return tmp_path


META = {"when": "W", "endpoint": "http://e", "model": "M"}


def test_md_escape():
    assert C.md_escape("a|b\nc") == "a\\|b c" and C.md_escape(5) == "5"


def test_write_report_rules_table_and_skipped_llm(out):
    rules = [("r1", "BLOCKER", True, ""), ("r2", "MINOR", False, "a|b")]
    path, nfail = C.write_report("slug", EX, rules, None, None, {**META, "llm_error": "down"})
    text = path.read_text(encoding="utf-8")
    assert nfail == 1 and path == out / "validation" / "slug.md"
    assert "| r1 | BLOCKER | PASS |  |" in text and "| r2 | MINOR | **FAIL** | a\\|b |" in text
    assert "1/2 passed." in text
    assert text.count("_skipped: down_") == 2
    path, _ = C.write_report("slug", EX, rules, None, None, META)
    assert path.read_text().count("_skipped: LLM disabled_") == 2


def test_write_report_consistency_sections(out):
    cons = {"mismatches": [{"quantity": "q", "location_a": "p", "value_a": "1", "location_b": "t", "value_b": "2",
                            "severity": "high", "note": "n|x"}],
            "arithmetic": [{"claim": "c", "computed": "3", "severity": "low", "note": "z"}], "summary": "Sum|mary"}
    text = C.write_report("s", EX, [], cons, None, META)[0].read_text(encoding="utf-8")
    assert "| q | p | 1 | t | 2 | high | n\\|x |" in text and "| c | 3 | low | z |" in text and "_Sum\\|mary_" in text
    empty = C.write_report("s", EX, [], {"mismatches": [], "arithmetic": None}, None, META)[0].read_text(encoding="utf-8")
    assert "No mismatches or arithmetic problems reported." in empty and "| quantity |" not in empty


def test_write_report_claims_sorted_and_counted(out):
    claims = {"claims": [{"claim": "ok", "status": "consistent"}, {"claim": "weird", "status": "zzz"},
                         {"claim": "stale", "status": "stale_risk"}, {"claim": "bad", "status": "internally_contradicted"},
                         {"claim": "cv", "status": "cannot_verify_offline"}, {"claim": "nostatus"}],
              "unsourced_count": 3, "summary": "S"}
    text = C.write_report("s", EX, [], None, claims, META)[0].read_text(encoding="utf-8")
    order = [text.index(f"| {k} |") for k in ("**internally_contradicted**", "**stale_risk**", "cannot_verify_offline", "consistent")]
    assert order == sorted(order)
    assert text.index("| zzz |") > order[-1]
    assert "Status counts: ?=1, cannot_verify_offline=1, consistent=1, internally_contradicted=1, stale_risk=1, zzz=1" in text
    assert "unsourced (model count): 3" in text and "_S_" in text
    t2 = C.write_report("s", EX, [], None, {"claims": None}, META)[0].read_text(encoding="utf-8")
    assert "unsourced (model count): ?" in t2


# -------------------------------------------------------------------- main
@pytest.fixture
def site(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "ROOT", tmp_path)
    monkeypatch.setattr(C, "OUT_DIR", tmp_path / "out" / "validation")
    (tmp_path / "posts").mkdir()
    monkeypatch.setattr(C, "node_check", lambda b: None)
    return tmp_path


def run_main(monkeypatch, *argv):
    monkeypatch.setattr(C.sys, "argv", ["content_validate.py", *argv])
    with pytest.raises(SystemExit) as e:
        C.main()
    return e.value.code


GOOD = "<h1>T</h1><p>5 May 2026 text</p>"


def test_main_requires_input(site, monkeypatch):
    monkeypatch.setattr(C.sys, "argv", ["cv"])
    with pytest.raises(SystemExit) as e:
        C.main()
    assert e.value.code == 2


def test_main_skip_llm_house_rules_only_exit_codes(site, monkeypatch, capsys):
    (site / "posts" / "ok.html").write_text(GOOD)
    monkeypatch.setattr(C, "STATIC_RULES", [("r", "MINOR", lambda b, **k: (False, "d"))])
    assert run_main(monkeypatch, "--slug", "ok", "--skip-llm") == 0
    out = capsys.readouterr().out
    assert "out/validation/ok.md  rules 0/1  consistency-findings -  flagged-claims -" in out
    monkeypatch.setattr(C, "STATIC_RULES", [("r", "BLOCKER", lambda b, **k: (False, "d"))])
    assert run_main(monkeypatch, "--slug", "ok", "--skip-llm") == 1
    assert "BLOCKER: r" in capsys.readouterr().out
    monkeypatch.setattr(C, "STATIC_RULES", [("r", "BLOCKER", lambda b, **k: (True, ""))])
    assert run_main(monkeypatch, "--slug", "ok", "--skip-llm") == 0


def test_main_files_recent_and_missing(site, monkeypatch, capsys):
    (site / "x.html").write_text(GOOD)
    monkeypatch.setattr(C, "STATIC_RULES", [])
    assert run_main(monkeypatch, "--file", str(site / "x.html"), "--slug", "gone", "--skip-llm") == 0
    out = capsys.readouterr().out
    assert "skip (not found)" in out and "x.md" in out
    run_main(monkeypatch, "--recent", "--skip-llm")
    assert capsys.readouterr().out.count("skip (not found)") == len(C.RECENT)


class FakeLLM:
    instances = []
    def __init__(self, base, key, model, timeout):
        self.args = (base, key, model, timeout)
        self.model = model
        FakeLLM.instances.append(self)
    def pick_model(self):
        if FakeLLM.fail_pick:
            raise RuntimeError("endpoint down")
        self.model = self.model or "auto"
        return self.model


def test_main_llm_flow_counts_findings_and_flags(site, monkeypatch, capsys):
    (site / "posts" / "p.html").write_text(GOOD)
    FakeLLM.fail_pick = False
    monkeypatch.setattr(C, "LLM", FakeLLM)
    monkeypatch.setattr(C, "STATIC_RULES", [])
    seen = {}
    monkeypatch.setattr(C, "test_consistency", lambda llm, ex, prose_cap=None: seen.update(cap=prose_cap) or {"mismatches": [{}, {}], "arithmetic": [{}]})
    monkeypatch.setattr(C, "test_claims", lambda llm, ex, prose_cap=None: {"claims": [{"status": "stale_risk"}, {"status": "internally_contradicted"}, {"status": "consistent"}]})
    assert run_main(monkeypatch, "--slug", "p", "--max-chars", "3000", "--base-url", "http://e:1/v1/x", "--api-key", "K", "--timeout", "7") == 0
    out = capsys.readouterr().out
    assert "model: auto  via http://e:1/v1/x" in out and "consistency-findings 3  flagged-claims 2" in out
    assert seen["cap"] == 3000 and FakeLLM.instances[-1].args == ("http://e:1/v1/x", "K", None, 7)
    report = (site / "out" / "validation" / "p.md").read_text(encoding="utf-8")
    assert "endpoint: http://e:1 · model: auto" in report


def test_main_llm_unavailable_falls_back_to_rules(site, monkeypatch, capsys):
    (site / "posts" / "p.html").write_text(GOOD)
    FakeLLM.fail_pick = True
    monkeypatch.setattr(C, "LLM", FakeLLM)
    monkeypatch.setattr(C, "STATIC_RULES", [])
    assert run_main(monkeypatch, "--slug", "p") == 0
    out = capsys.readouterr().out
    assert "LLM endpoint unavailable (endpoint down)" in out
    assert "_skipped: endpoint down_" in (site / "out" / "validation" / "p.md").read_text()


def test_main_one_llm_test_failing_keeps_the_other(site, monkeypatch, capsys):
    (site / "posts" / "p.html").write_text(GOOD)
    FakeLLM.fail_pick = False
    monkeypatch.setattr(C, "LLM", FakeLLM)
    monkeypatch.setattr(C, "STATIC_RULES", [])
    def bad(llm, ex, prose_cap=None):
        raise RuntimeError("timeout")
    monkeypatch.setattr(C, "test_consistency", bad)
    monkeypatch.setattr(C, "test_claims", lambda llm, ex, prose_cap=None: {"claims": [{"status": "stale_risk"}]})
    run_main(monkeypatch, "--slug", "p")
    out = capsys.readouterr().out
    assert "! p: consistency: timeout" in out and "consistency-findings -  flagged-claims 1" in out
    text = (site / "out" / "validation" / "p.md").read_text(encoding="utf-8")
    assert "_skipped: consistency: timeout_" in text and "stale_risk" in text


def test_main_env_defaults(site, monkeypatch, capsys):
    (site / "posts" / "p.html").write_text(GOOD)
    FakeLLM.fail_pick = False
    monkeypatch.setattr(C, "LLM", FakeLLM)
    monkeypatch.setattr(C, "STATIC_RULES", [])
    monkeypatch.setattr(C, "test_consistency", lambda *a, **k: {})
    monkeypatch.setattr(C, "test_claims", lambda *a, **k: {})
    for k in ("LLM_BASE_URL", "LLM_API_KEY", "LLM_MODEL"):
        monkeypatch.delenv(k, raising=False)
    run_main(monkeypatch, "--slug", "p")
    assert FakeLLM.instances[-1].args == ("http://localhost:20128/v1", None, None, 180)

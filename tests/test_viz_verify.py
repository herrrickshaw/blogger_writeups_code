import ast
import json
import re
import subprocess
import types

import pytest

import viz_render as R
import viz_verify as V
from test_viz_frame import WORDS, post
from test_viz_render import good_spec


# ---------------------------------------------------------------- _eval
@pytest.mark.parametrize("expr,want", [("1+2", 3.0), ("570/3", 190.0), ("2**3", 8.0), ("-4", -4.0), ("2*(3+1)", 8.0), ("10-4-3", 3.0), ("1.5*2", 3.0)])
def test_eval_ok(expr, want):
    assert V._eval(ast.parse(expr, mode="eval")) == want


@pytest.mark.parametrize("expr", ["abs(1)", "a+1", "'x'", "1 if 1 else 2", "[1]", "1%2", "1//2", "+3"])
def test_eval_rejects(expr):
    with pytest.raises(ValueError):
        V._eval(ast.parse(expr, mode="eval"))


def test_eval_division_by_zero_propagates():
    with pytest.raises(ZeroDivisionError):
        V._eval(ast.parse("1/0", mode="eval"))


# ------------------------------------------------------------- derived_ok
ORIG = {"570", "3", "4.5", "100", "12"}


def test_derived_arithmetic_pass_and_manual_count():
    assert V.derived_ok("190", "570/3", ORIG) == (True, False, "")
    assert V.derived_ok("1,903", "570/3", ORIG)[0] is False
    assert V.derived_ok("7", "count: seven countries", ORIG)[:2] == (True, True)
    assert V.derived_ok("7", "count:   ", ORIG) == (False, True, "empty count note")


def test_derived_operands_must_come_from_original():
    ok, manual, why = V.derived_ok("200", "100*2", ORIG)
    assert not ok and not manual and "uses numbers not in the original: ['2']" in why
    assert V.derived_ok("450", "100*4.5", ORIG)[0] is True                          # float literal matched as "4.5"
    assert V.derived_ok("8", "4.5+3.5", ORIG)[0] is False


def test_derived_tolerance_rules():
    assert V.derived_ok("33", "100/3", ORIG)[0] is True                              # rounds to 0 dp
    assert V.derived_ok("33.3", "100/3", ORIG)[0] is True                            # 1 dp
    assert V.derived_ok("33.33", "100/3", ORIG)[0] is True and V.derived_ok("33.333", "100/3", ORIG)[0] is True
    assert V.derived_ok("34", "100/3", ORIG)[0] is False
    ok, _, why = V.derived_ok("40", "100/3", ORIG)
    assert not ok and "= 33.3333, not 40" in why
    assert V.derived_ok("10000", "100*100", ORIG)[0] is True


def test_derived_bad_expressions():
    for e in ("abc", "100 +", "__import__('os')", "100/0"):
        ok, manual, why = V.derived_ok("1", e, ORIG)
        assert not ok and not manual and "bad expression" in why


def test_external_links():
    h = ('<a href="https://a.com/x#frag">1</a><a href="http://b.org/y?q=1">2</a><a href="https://blog.vertistratsolution.com/p">own</a>'
         '<a href="/rel">r</a><a href="https://a.com/x">dup</a>')
    assert V.external_links(h) == {"https://a.com/x", "http://b.org/y?q=1"}


# ------------------------------------------------------------------- verify
@pytest.fixture
def world(tmp_path, monkeypatch):
    monkeypatch.setattr(V, "ROOT", tmp_path)
    monkeypatch.setattr(R, "ROOT", tmp_path)
    (tmp_path / "posts").mkdir()
    d = tmp_path / "out" / "viz" / "slug"
    d.mkdir(parents=True)
    body = (f'<h2>Intro</h2><p>{WORDS}</p><h2>Limits</h2><table><tr><th>Country</th><th>Limit</th></tr>'
            '<tr><td>India</td><td>5 mg/kg</td></tr><tr><td>Brazil</td><td>1.5 mg/kg</td></tr><tr><td>EU</td><td>1 mg/kg</td></tr></table>'
            '<p>See <a href="https://src.example/doc">the doc</a>. 570 570 570 190 190 7 7 7 3 3 3.</p>'
            '<p>This could not establish causation.</p>')
    (tmp_path / "posts" / "slug.html").write_text(post(body=body), encoding="utf-8")
    monkeypatch.setattr(R.sys, "argv", ["viz_render.py", "slug"])
    clean_mobile = {"wide": False, "pageWidth": 375, "smallCharts": 0, "swipeTables": 0, "longParas": 0}
    state = {"mobile": (clean_mobile, "")}
    monkeypatch.setattr(V, "mobile", lambda path: state["mobile"])

    def spec(**kw):
        s = good_spec(**kw)
        (d / "spec.json").write_text(json.dumps(s))
        return s
    return tmp_path, d, spec, state


def test_verify_missing_inputs(world):
    tmp, d, spec, state = world
    assert V.verify("nope")[0] == ["no live post posts/nope.html"]
    errs, _ = V.verify("slug")
    assert errs[0].startswith("no edition ")
    (tmp / "posts" / "bad.html").write_text("<p>no frame</p>")
    (d.parent / "bad").mkdir()
    (d.parent / "bad" / "edition.html").write_text("x")
    assert V.verify("bad")[0] == ["live post does not have the standard frame (tools/viz_frame.py)"]


def build_edition(spec_fn, **kw):
    spec_fn(**kw)
    return R.build("slug")


def test_verify_accepts_a_rendered_edition_and_flags_numbers(world):
    tmp, d, spec, state = world
    build_edition(spec)
    errs, manual = V.verify("slug")
    assert not any(e.startswith(("frame", "structure", "charts", "safety", "phone")) for e in errs), errs
    assert any(e.startswith("numbers:") for e in errs)                      # the fixture's own invented figures are caught


def test_verify_frame_tampering(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    text = ed.read_text(encoding="utf-8")
    ed.write_text(text.replace("<h1>", "<h1 data-x=1>", 1), encoding="utf-8")
    assert any("does not start with the live head" in e for e in V.verify("slug")[0])
    ed.write_text(text + "extra", encoding="utf-8")
    assert any("does not end with the live tail" in e for e in V.verify("slug")[0])


def test_verify_structure_errors(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    t = ed.read_text(encoding="utf-8")
    ed.write_text(t.replace('<div class="xv-top">', "<div>", 1), encoding="utf-8")
    assert any("need exactly one top line, found 0" in e for e in V.verify("slug")[0])
    ed.write_text(t.replace('class="xv-k"', 'class="no"'), encoding="utf-8")
    assert any("top line needs 1-3 bullets" in e for e in V.verify("slug")[0])
    ed.write_text(t.replace('<section class="xv-sec">', "<div>", 1).replace("</section>", "</div>", 1), encoding="utf-8")
    assert any("need 3 or 4 insight sections, found 2" in e for e in V.verify("slug")[0])
    ed.write_text(t.replace("<b>What it means:</b>", "<b>Meaning:</b>", 1), encoding="utf-8")
    assert any("must end with one What it means / What to do pair" in e for e in V.verify("slug")[0])
    ed.write_text(t.replace("It means this.", "It means this. And more.", 1), encoding="utf-8")
    assert any("not exactly one sentence" in e for e in V.verify("slug")[0])
    ed.write_text(t.replace("What to do:</b> Do that.", "What to do:</b> Do that", 1), encoding="utf-8")
    assert any("not exactly one sentence" in e for e in V.verify("slug")[0])
    ed.write_text(t.replace('<h2 class="gb-h2" id="a1">India is loosest</h2>', "", 1), encoding="utf-8")
    assert any("section 1 has no h2" in e for e in V.verify("slug")[0])
    t2 = t.replace('<figure class="xv"', "<figure", 1)
    ed.write_text(t2, encoding="utf-8")
    assert any("section 1 has no chart" in e for e in V.verify("slug")[0])


def test_verify_chart_titles(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    t = ed.read_text(encoding="utf-8")
    ed.write_text(t.replace("India allows 5 mg/kg, five times the EU limit", "x" * 91, 1), encoding="utf-8")
    assert any("title over 90 characters" in e for e in V.verify("slug")[0])
    ed.write_text(t.replace("India allows 5 mg/kg, five times the EU limit", "Chloride limits", 1), encoding="utf-8")
    assert any("does not state a finding: 'Chloride limits'" in e for e in V.verify("slug")[0])


def test_verify_numbers_and_derived(world):
    tmp, d, spec, state = world
    ed = build_edition(spec, derived={"5": "570/114"})
    errs, _ = V.verify("slug")
    assert any("derived '5'" in e and "uses numbers not in the original" in e for e in errs)
    ed = build_edition(spec, derived={"1710": "570*3", "7": "count: seven rows"})
    ed.write_text(ed.read_text(encoding="utf-8").replace("<h2", "<p>1710</p><h2", 1), encoding="utf-8")
    errs, manual = V.verify("slug")
    assert manual == ["7 = count: seven rows"]
    numeric = [e for e in errs if e.startswith("numbers: not in the original")][0]
    assert "1710" not in numeric and "closest in the original" in numeric               # declared arithmetic is accepted
    ed = build_edition(spec)
    ed.write_text(ed.read_text(encoding="utf-8").replace("<h2", "<p>1710</p><h2", 1), encoding="utf-8")
    assert "1710 (closest in the original: " in [e for e in V.verify("slug")[0] if e.startswith("numbers: not in the original")][0]


def test_verify_numbers_truncates_list_to_eight(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    ed.write_text(ed.read_text(encoding="utf-8").replace("<h2", "<p>" + " ".join(str(n) for n in range(7000, 7012)) + "</p><h2", 1), encoding="utf-8")
    msg = [e for e in V.verify("slug")[0] if e.startswith("numbers: not in the original")][0]
    assert re.search(r"and \d+ more\.", msg) and msg.count("closest in the original") == 8


def test_verify_coverage_and_safety_and_phone(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    t = ed.read_text(encoding="utf-8")
    ed.write_text(t.replace("could not establish", "x"), encoding="utf-8")
    ed.write_text(t + "", encoding="utf-8")
    errs, _ = V.verify("slug")
    assert not any("caveat is missing" in e for e in errs)
    mid_script = t.replace('<div class="xv-top">', '<script>1</script><div class="xv-top">', 1)
    ed.write_text(mid_script, encoding="utf-8")
    assert any(e == "safety: script or iframe in the new text" for e in V.verify("slug")[0])
    ed.write_text(t.replace('<div class="xv-top">', '<a href="https://masaladeutsch.blogspot.com/x">o</a><div class="xv-top">', 1), encoding="utf-8")
    assert any(e == "safety: old-domain link" for e in V.verify("slug")[0])
    ed.write_text(t, encoding="utf-8")
    state["mobile"] = (None, "node missing")
    assert any("phone: audit failed to run: node missing" in e for e in V.verify("slug")[0])
    state["mobile"] = ({"wide": True, "pageWidth": 500, "smallCharts": 2, "swipeTables": 1, "longParas": 0}, "")
    errs = V.verify("slug")[0]
    assert any("page is 500px wide at 375px" in e for e in errs) and any("2 chart(s) with labels under 9.5px" in e for e in errs)
    assert any("1 table(s) need sideways swiping" in e for e in errs)
    state["mobile"] = ({"wide": False, "pageWidth": 375, "smallCharts": 0, "swipeTables": 0, "longParas": 2}, "")
    assert not any("new paragraphs over 90 words" in e for e in V.verify("slug")[0])
    state["mobile"] = ({"wide": False, "pageWidth": 375, "smallCharts": 0, "swipeTables": 0, "longParas": 3}, "")
    assert any("phone: " in e and "new paragraphs over 90 words (allowed 2;" in e for e in V.verify("slug")[0])


def test_verify_update_notes_shape(world):
    tmp, d, spec, state = world
    ed = build_edition(spec, update_notes=["<p><b>Updated 5 June 2026:</b> new <a href=\"https://x.org/a\">source</a>.</p>"])
    assert not any(e.startswith("update note") for e in V.verify("slug")[0])
    ed = build_edition(spec, update_notes=["<p><b>Updated 5 June 2026:</b> no link.</p>"])
    assert any("update note: must open with" in e for e in V.verify("slug")[0])
    ed = build_edition(spec, update_notes=["<p>Something else <a href=\"http://x\">l</a></p>"])
    assert any("update note: must open with" in e for e in V.verify("slug")[0])


def test_verify_size_window(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    t = ed.read_text(encoding="utf-8")
    from viz_frame import split
    fr = split((tmp / "posts" / "slug.html").read_text(encoding="utf-8"))
    ed.write_text(fr.head + fr.lead + fr.mid + "<p>tiny</p>" + fr.tail, encoding="utf-8")
    assert any(e.startswith("size:") and "needs at least 250 words, at most 85%" in e for e in V.verify("slug")[0])
    ed.write_text(t.replace('<div class="xv-top">', "<p>" + "word " * 700 + "</p><div class=\"xv-top\">", 1), encoding="utf-8")
    assert any(e.startswith("size:") for e in V.verify("slug")[0])
    ed.write_text(t, encoding="utf-8")
    assert not any(e.startswith("size:") for e in V.verify("slug")[0])


def test_mobile_runs_node_and_reports_failures(monkeypatch, tmp_path):
    monkeypatch.undo()
    calls = []
    def run_ok(cmd, **kw):
        calls.append(cmd)
        out = cmd[cmd.index("--json") + 1]
        open(out, "w").write(json.dumps([{"wide": False}]))
        return types.SimpleNamespace(returncode=0, stderr="")
    monkeypatch.setattr(V.subprocess, "run", run_ok)
    assert V.mobile(tmp_path / "e.html") == ({"wide": False}, "")
    assert calls[0][0] == "node" and calls[0][1].endswith("tools/mobile_audit.js")
    monkeypatch.setattr(V.subprocess, "run", lambda c, **kw: types.SimpleNamespace(returncode=1, stderr="  boom " * 100))
    got, why = V.mobile(tmp_path / "e.html")
    assert got is None and len(why) == 200 and why.startswith("boom")


def test_verify_coverage_rules_each_fire(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    t = ed.read_text(encoding="utf-8")
    orig_path = tmp / "posts" / "slug.html"
    # the original's caveat, a dated note and an external link must survive in the edition
    orig_path.write_text(orig_path.read_text(encoding="utf-8").replace(
        "<p>This could not establish causation.</p>",
        "<p>This could not establish causation. Updated 3 May 2026 note.</p>"), encoding="utf-8")
    fr_ed = ed.read_text(encoding="utf-8")
    cleaned = fr_ed.replace("establish", "x").replace("Updated 3 May 2026", "Updated").replace("https://src.example/doc", "https://other.example/")
    ed.write_text(cleaned, encoding="utf-8")
    errs = V.verify("slug")[0]
    assert any("'what this could not establish' caveat is missing" in e for e in errs)
    assert any("the original's note 'Updated 3 May 2026' is missing" in e for e in errs)
    assert any("source link(s) from the original body are missing, e.g. https://src.example/doc" in e for e in errs)


def test_verify_top_numbers_must_survive(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    t = ed.read_text(encoding="utf-8")
    for n in ("570", "190", "7"):
        t = t.replace(n, "0")
    ed.write_text(t, encoding="utf-8")
    assert any(e.startswith("coverage: only") and "of the original's top numbers" in e for e in V.verify("slug")[0])


def test_verify_unbalanced_containers_are_reported(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    ed.write_text(ed.read_text(encoding="utf-8").replace('<div class="xv-top">', '<div class="xv-top"><div class="leak">', 1), encoding="utf-8")
    errs = V.verify("slug")[0]
    assert len(errs) == 1 and errs[0].startswith("frame: the edition leaves ") and "container element(s) open" in errs[0]


def test_verify_paragraphs_kept_verbatim_are_not_counted_as_new(world):
    tmp, d, spec, state = world
    ed = build_edition(spec)
    state["mobile"] = ({"wide": False, "pageWidth": 375, "smallCharts": 0, "swipeTables": 0, "longParas": 3}, "")
    long_orig = " ".join(f"w{i}" for i in range(95))
    orig_path = tmp / "posts" / "slug.html"
    orig_path.write_text(orig_path.read_text(encoding="utf-8").replace("<p>This could not establish causation.</p>", f"<p>{long_orig}</p><p>This could not establish causation.</p>"), encoding="utf-8")
    t = ed.read_text(encoding="utf-8")
    ed.write_text(t.replace('<div class="xv-top">', f'<p>{long_orig}</p><div class="xv-top">', 1), encoding="utf-8")
    assert not any("new paragraphs over 90 words" in e for e in V.verify("slug")[0])        # 3 long - 1 kept = 2 allowed


def run_cli(world, monkeypatch, *argv):
    import runpy
    import shutil
    from pathlib import Path
    tmp, d, spec, state = world
    tools = tmp / "tools"
    tools.mkdir(exist_ok=True)
    shutil.copy(Path(V.__file__), tools / "viz_verify.py")
    monkeypatch.setattr(V.sys, "argv", ["viz_verify.py", *argv])
    return runpy.run_path(str(tools / "viz_verify.py"), run_name="__main__")


def test_cli_usage_and_missing_post(world, monkeypatch, capsys):
    with pytest.raises(SystemExit) as e:
        run_cli(world, monkeypatch)
    assert "Acceptance oracle" in str(e.value.code)
    with pytest.raises(SystemExit) as e:
        run_cli(world, monkeypatch, "ghost")
    assert e.value.code == 1 and capsys.readouterr().out.startswith("FAIL ghost: no live post posts/ghost.html")

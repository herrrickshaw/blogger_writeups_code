import csv
import json
import os
import sys
import types

import pytest

import audit_blog as AB
import svg_caption_fix as SC

HERE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "consistency-check")
sys.path.insert(0, HERE)
import _local_check as LC  # noqa: E402


# ================================================================ audit_blog
def test_visible_strips_scripts_styles_tags_entities():
    assert AB.visible("<script>x</script><style>y</style><p>A&amp; <b>b</b></p>") == "A& b"


def test_readability_metrics_and_empty():
    assert AB.readability("") is None and AB.readability("123 456") is None and AB.readability("...") is None
    r = AB.readability("The cat sat. The dog ran fast. Go.")
    assert r["words"] == 8 and r["sentences"] == 3 and r["words_per_sentence"] == 2.7 and r["long_sentence_pct"] == 0.0
    expected = round(206.835 - 1.015 * (8 / 3) - 84.6 * (8 / 8), 1)           # one vowel group per word
    assert r["flesch"] == expected


def test_readability_long_sentence_threshold_is_over_34_words():
    s34 = " ".join(["word"] * 34) + "."
    s35 = " ".join(["word"] * 35) + "."
    assert AB.readability(s34 + " " + s34)["long_sentence_pct"] == 0.0
    r = AB.readability(s34 + " " + s35)
    assert r["long_sentence_pct"] == 50.0 and r["sentences"] == 2


def test_readability_syllable_proxy_and_one_char_sentences_dropped():
    r = AB.readability("Beautiful audience queue. x")
    assert r["sentences"] == 1                                              # "x" has length 1 and is dropped
    assert r["words"] == 4                                                  # the dropped "sentence" still counts as a word
    syll = sum(max(1, len(__import__("re").findall(r"[aeiouy]+", w.lower()))) for w in ("Beautiful", "audience", "queue", "x"))
    assert r["flesch"] == round(206.835 - 1.015 * 4 - 84.6 * (syll / 4), 1)


def test_node_check_cases(monkeypatch):
    monkeypatch.setattr(AB.shutil, "which", lambda n: None)
    assert AB.node_check(["x"]) is None
    monkeypatch.setattr(AB.shutil, "which", lambda n: "/usr/bin/node")
    assert AB.node_check([]) is None
    seen = []
    def run(cmd, input, capture_output, text):
        seen.append(input)
        return types.SimpleNamespace(returncode=1 if "BAD" in input else 0)
    monkeypatch.setattr(AB.subprocess, "run", run)
    assert AB.node_check(["ok()", "  ", "BAD(", "BAD2", "fine"]) == 2
    assert seen == ["ok()", "BAD(", "BAD2", "fine"]                         # blank scripts are not sent to node


@pytest.fixture
def site(tmp_path, monkeypatch):
    monkeypatch.setattr(AB, "POSTS", tmp_path / "posts")
    monkeypatch.setattr(AB, "MANIFEST", tmp_path / "manifest.json")
    (tmp_path / "posts").mkdir()
    monkeypatch.setattr(AB, "node_check", lambda scripts: 1 if any("BAD" in s for s in scripts) else 0)
    recs = {}

    def add(slug, body, version="1.0.0", write=True):
        recs[slug] = {"slug": slug, "version": version}
        if write:
            (tmp_path / "posts" / f"{slug}.html").write_text(body, encoding="utf-8")
        (tmp_path / "manifest.json").write_text(json.dumps({"posts": recs}))
    return tmp_path, add


FULL = ('google_translate_element article-index-start-here gs-ai-disclosure gs-revision-v1 '
        '<p>Short sentence here. Another short one follows. A third sentence ends.</p>')


def run_main(monkeypatch, *argv):
    monkeypatch.setattr(AB.sys, "argv", ["ab", *argv])
    AB.main()


def test_main_adoption_charts_readability_report(site, monkeypatch, capsys):
    tmp, add = site
    add("clean", FULL)
    add("layers", FULL + " BW-OVERRIDE gs-light-lock @media not all and (prefers-color-scheme:dark)")
    add("bare", "<p>Some words in a sentence. More words here.</p><table><tr><td>₹5 crore</td><td>12%</td></tr><tr><td>plain</td></tr></table>")
    add("chart", FULL + "<script>BAD(</script><script> </script><script>fine()</script>")
    add("nofile", "", write=False)
    run_main(monkeypatch)
    out = capsys.readouterr().out
    assert "=== 4 posts ===" in out
    assert "zero conflicting CSS layers     3/4  (75%)" in out
    assert "translate widget" in out and "index backlink" in out and "AI disclosure" in out and "revision line" in out
    assert " 3/4  (75%)" in out                                              # three of four posts carry the translate widget
    assert "posts with inline scripts       1/4" in out and "posts with a broken script      1/4  <-- blank charts" in out
    assert "chart  1 of 2" in out
    assert "READABILITY (mean over 4 posts)" in out and "hardest to read:" in out and "easiest:" in out
    assert "units repeated in table cells" in out and "   2 cells  bare" in out


def test_main_no_broken_scripts_message_and_csv(site, monkeypatch, capsys, tmp_path):
    tmp, add = site
    add("a", FULL, version="2.0.0")
    add("b", "<p>No sentences</p>")
    csvp = tmp / "sub" / "o.csv"
    run_main(monkeypatch, "--csv", str(csvp))
    out = capsys.readouterr().out
    assert "(none)" in out and f"wrote {csvp}" in out
    rows = list(csv.DictReader(open(csvp, encoding="utf-8")))
    assert [r["slug"] for r in rows] == ["a", "b"] and rows[0]["version"] == "2.0.0"
    assert rows[0]["translate"] == "1" and rows[0]["layers"] == "0" and rows[0]["scripts"] == "0"
    assert rows[0]["words"] and "flesch" in rows[0]


# ============================================================= svg_caption_fix
LONG1 = "Ratios are drawn from a long source note that runs well beyond the width of the canvas at ten pixels font size for sure"
LONG2 = "Sources: a second caption that is also much too long for a single line of the same canvas width in this chart template"


def chart(w=700, h=395, extra=""):
    return (f'<p>before</p><svg viewBox="0 0 {w} {h}" width="100%"><rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>{extra}'
            f'<text x="350" y="368" text-anchor="middle" font-size="10" fill="#868e96">{LONG1}</text>'
            f'<text x="350" y="381" text-anchor="middle" font-size="10" fill="#868e96">{LONG2}</text></svg><p>after</p>')


def caps():
    return [{"old_y": 368, "text": LONG1}, {"old_y": 381, "text": LONG2}]


def test_find_svg_open_exact_and_ambiguous():
    body = chart() + chart(w=500, h=300)
    matches, _ = SC._find_svg_open(body, 700, 395)
    assert len(matches) == 1 and matches[0].group(0).startswith('<svg viewBox="0 0 700 395"')
    with pytest.raises(ValueError, match="no <svg viewBox=\"0 0 1 1\">"):
        SC._find_svg_open(body, 1, 1)
    assert len(SC._find_svg_open(chart() + chart(), 700, 395)[0]) == 2


def test_fix_stacked_captions_wraps_grows_canvas_and_keeps_rest(tmp_path):
    f = tmp_path / "p.html"
    f.write_text(chart(), encoding="utf-8")
    new_h, lines = SC.fix_stacked_captions(str(f), (700, 395), caps(), start_y=340, max_width=300)
    body = f.read_text(encoding="utf-8")
    assert lines >= 4 and new_h >= 395
    assert f'viewBox="0 0 700 {new_h}"' in body and f'<rect x="0" y="0" width="700" height="{new_h}"' in body
    assert body.startswith("<p>before</p>") and body.endswith("</svg><p>after</p>")
    assert LONG1 not in body                                                    # the single long line was replaced by wrapped tspans
    assert body.count('fill="#868e96"') == 2 and body.count("<tspan") == lines
    assert 'font-size="10.0"' in body and 'x="350"' in body
    assert body.index('<text fill="#868e96" x="350" y="340"') > body.index("<rect")


def test_fix_stacked_captions_height_math_and_never_shrinks(tmp_path):
    f = tmp_path / "p.html"
    f.write_text(chart(h=2000), encoding="utf-8")
    new_h, _ = SC.fix_stacked_captions(str(f), (700, 2000), caps(), start_y=340, max_width=300)
    assert new_h == 2000                                                       # computed height is smaller: never shrinks
    f.write_text(chart(), encoding="utf-8")
    new_h, n = SC.fix_stacked_captions(str(f), (700, 395), caps(), start_y=340, max_width=10_000, gap_between=15, bottom_margin=12)
    assert n == 2 and new_h == 395                                              # one line each; 340 + 2 gaps ... below the old height
    f.write_text(chart(h=300).replace('y="381"', 'y="381"'), encoding="utf-8")
    new_h, n = SC.fix_stacked_captions(str(f), (700, 300), caps(), start_y=340, max_width=10_000, gap_between=20, bottom_margin=5)
    assert new_h == int(340 + 2 * 20 - 20 + 5) == 365


def test_fix_stacked_captions_errors_and_occurrence(tmp_path):
    f = tmp_path / "p.html"
    f.write_text(chart(), encoding="utf-8")
    with pytest.raises(ValueError, match="could not find exact caption text"):
        SC.fix_stacked_captions(str(f), (700, 395), [{"old_y": 999, "text": "nope"}], start_y=340)
    with pytest.raises(ValueError, match="no <svg"):
        SC.fix_stacked_captions(str(f), (1, 1), caps(), start_y=340)
    f.write_text(chart(extra="<g/>") + chart(), encoding="utf-8")
    with pytest.raises(ValueError, match="2 charts share canvas 700x395"):
        SC.fix_stacked_captions(str(f), (700, 395), caps(), start_y=340, occurrence=None)


def test_fix_stacked_captions_start_anchor_option(tmp_path):
    f = tmp_path / "p.html"
    body = chart().replace('text-anchor="middle"', 'text-anchor="start"')
    f.write_text(body, encoding="utf-8")
    SC.fix_stacked_captions(str(f), (700, 395), [{"old_y": 368, "text": LONG1, "anchor": "start"}, {"old_y": 381, "text": LONG2, "anchor": "start"}],
                            start_y=340, max_width=300)
    assert 'text-anchor="start"' in f.read_text(encoding="utf-8")


def test_caption_fix_module_doc_main(capsys):
    import runpy
    runpy.run_path(SC.__file__, run_name="__main__")
    assert "Fix the single most common chart bug" in capsys.readouterr().out


# ================================================================ _local_check
def test_local_check_js_errors_writes_helper_and_parses(monkeypatch, tmp_path):
    written = {}
    real_open = open
    monkeypatch.setattr(LC, "subprocess", types.SimpleNamespace(run=lambda c, capture_output, text: types.SimpleNamespace(stdout=" [2] \n")))
    monkeypatch.setattr("builtins.open", lambda p, *a, **k: real_open(tmp_path / "syntax.js", *a, **k) if p == "/tmp/_syntax_check.js" else real_open(p, *a, **k))
    assert LC.js_syntax_errors("x.html") == [2]
    assert "new Function(c)" in (tmp_path / "syntax.js").read_text()
    monkeypatch.setattr(LC, "subprocess", types.SimpleNamespace(run=lambda c, capture_output, text: types.SimpleNamespace(stdout="oops")))
    assert LC.js_syntax_errors("x.html") == []


def test_local_check_main_exit_codes_and_output(tmp_path, monkeypatch, capsys):
    p = tmp_path / "a.html"
    p.write_text("<p>x</p>", encoding="utf-8")
    monkeypatch.setattr(LC, "js_syntax_errors", lambda path: [])
    seen = {}
    def good(body, node_check):
        seen["nc"] = node_check
        return True, ""
    def bad(body, node_check):
        return False, "broken"
    def boom(body, node_check):
        raise KeyError("k")
    monkeypatch.setattr(LC, "STATIC_RULES", [("g", "MINOR", good)])
    monkeypatch.setattr(LC.sys, "argv", ["lc", str(p)])
    with pytest.raises(SystemExit) as e:
        LC.main()
    assert e.value.code == 0 and f"=== {p}" in capsys.readouterr().out and seen["nc"] == []
    monkeypatch.setattr(LC, "STATIC_RULES", [("g", "MINOR", good), ("b", "BLOCKER", bad), ("x", "MAJOR", boom)])
    with pytest.raises(SystemExit) as e:
        LC.main()
    out = capsys.readouterr().out
    assert e.value.code == 1 and "[OK] MINOR g:" in out and "[FAIL] BLOCKER b: broken" in out and "[FAIL] MAJOR x: rule error: KeyError: 'k'" in out

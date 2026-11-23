import sys

import pytest

import factcheck_summary as S

SECTION = """## Gemini gem
FACTUAL ERRORS:
- The tariff was "twenty five percent on all steel imports" in 2025 — wrong, it was 50% [confidence: high]
- (none found)
INTERPRETATION ERRORS:
- Causal leap from A to B [confidence: Medium]
- no confidence marker here
**OUTDATED DATA:**
* Figure 1,234.5 for FY24 — newer exists [confidence: low]
• bullet char item
none found
"""


def test_failed():
    for t in ("x API error 429", "network error", "[empty response]"):
        assert S.failed(t)
    assert not S.failed("FACTUAL ERRORS:\n- fine")


def test_parse_section_categories_confidence_and_none_found():
    got = S.parse_section(SECTION)
    assert [c for _, c in got["factual"]] == ["high"] and "twenty five percent" in got["factual"][0][0]
    assert [c for _, c in got["interpretation"]] == ["medium", "unstated"]
    assert [c for _, c in got["outdated"]] == ["low", "unstated"]
    assert got["outdated"][1][0] == "bullet char item"
    assert set(got) == {"factual", "interpretation", "outdated"}


def test_parse_section_ignores_bullets_before_a_heading_and_none_found_variants():
    got = S.parse_section("- orphan\nFACTUAL ERRORS:\n- none found\n- (None found)\n- None Found.\n- real")
    assert [i for i, _ in got["factual"]] == ["real"]


def test_parse_section_heading_case_and_markup():
    got = S.parse_section("**factual errors**\n- a")
    assert len(got["factual"]) == 1
    assert S.parse_section("")["factual"] == []


def test_keys_numbers_years_and_quotes():
    nums, words = S.keys("It rose 1,234.5 in 2025 and 12 or 500 and 3.0")
    assert nums == {"1234.5", "500", "3.0"}
    nums, _ = S.keys("in 1999 and 2031 and 1800")
    assert nums == {"1800"}                             # 19xx/20xx are years; 1800 is not
    nums, _ = S.keys("value 100, then 99")
    assert nums == {"100"}                              # three digits kept, two dropped
    _, words = S.keys('claims "the quick brown fox jumps" today')
    assert words == {"quick brown jumps"}                  # only words of 4+ letters ("the", "fox" dropped)
    _, words = S.keys('claims "alpha bravo charlie delta" today')
    assert words == {"alpha bravo charlie", "bravo charlie delta"}
    assert S.keys('short "tiny"')[1] == set()
    assert S.keys("no quote")[1] == set()


def test_same_claim():
    assert S.same_claim("number 1,234.5 here", "also 1234.5 there")
    assert not S.same_claim("number 12 here", "number 12 there")                  # two digits too weak
    assert not S.same_claim("in 2025", "in 2025")
    assert S.same_claim('said "growth outpaced the entire sector"', 'wrote "growth outpaced the entire market"')
    assert not S.same_claim('said "completely different words here"', 'wrote "nothing in common at all"')
    assert not S.same_claim("", "")


def report(name, body):
    return f"## {name}\n{body}\n"


@pytest.fixture
def fc(tmp_path, monkeypatch):
    d = tmp_path / "fc"
    d.mkdir()
    monkeypatch.setattr(S, "FC", d)
    return d


def run_main(monkeypatch, fc, *argv):
    monkeypatch.setattr(sys, "argv", ["fs", *argv])
    S.main()
    return (fc / "SUMMARY.md").read_text(encoding="utf-8")


def test_main_agreement_high_outdated_pending_and_too_large(fc, monkeypatch, capsys):
    both = ("FACTUAL ERRORS:\n- Steel tariff was 1,500.25 crore [confidence: low]\nINTERPRETATION ERRORS:\n- none found\n"
            "OUTDATED DATA:\n- Old figure 777 [confidence: medium]\n")
    other = ("FACTUAL ERRORS:\n- Steel tariff 1500.25 crore is wrong [confidence: medium]\n- Solo claim [confidence: high]\n"
             "INTERPRETATION ERRORS:\n- none found\nOUTDATED DATA:\n- none found\n")
    (fc / "alpha.md").write_text("# a\n" + report("Gemini g", both) + report("Mistral m", other), encoding="utf-8")
    (fc / "beta.md").write_text("# b\n" + report("Gemini g", "FACTUAL ERRORS:\n- ok [confidence: high]\n") + report("Mistral m", "[Mistral API error 429: x]"), encoding="utf-8")
    (fc / "gamma.md").write_text("# c [SKIPPED: too large — 9 chars]", encoding="utf-8")
    (fc / "SUMMARY.md").write_text("old summary")
    (fc / "delta.md").write_text("# d\n" + report("Kimi k", "FACTUAL ERRORS:\n- ignored\n"), encoding="utf-8")
    text = run_main(monkeypatch, fc)
    assert "Panel: Gemini, Mistral. Posts with at least one clean answer: 2. Posts missing a clean answer from some panel model: 2. Too large to send: 1." in text
    assert "- **alpha** (factual) — Gemini: Steel tariff was 1,500.25 crore [confidence: low]" in text
    assert "  - Mistral: Steel tariff 1500.25 crore is wrong [confidence: medium]" in text
    assert "- **alpha** (factual) — Mistral: Solo claim [confidence: high]" in text
    assert "| alpha | 1 | 1 | 3 | 0 | 1 |" in text
    assert "| beta | 0 | 1 | 1 | 0 | 0 |" in text
    assert "- **alpha**\n  - Gemini: Old figure 777 [confidence: medium]" in text
    assert "- beta — no clean answer from Mistral" in text and "- delta — no clean answer from Gemini, Mistral" in text
    assert "Too large to send in one request: gamma" in text
    assert "- ignored" not in text
    out = capsys.readouterr().out
    assert "2 posts summarised, 1 agreed flags, 2 high-confidence single-model flags, 1 outdated-data flags, 2 posts pending" in out


def test_main_models_arg_and_row_ordering(fc, monkeypatch):
    body = "FACTUAL ERRORS:\n- claim 4,321.5 here [confidence: high]\n"
    for slug, extra in (("zeta", ""), ("alpha", "")):
        (fc / f"{slug}.md").write_text(report("Gemini g", body) + report("Groq q", body), encoding="utf-8")
    (fc / "solo.md").write_text(report("Gemini g", "FACTUAL ERRORS:\n- uniq [confidence: high]\n") + report("Groq q", "FACTUAL ERRORS:\n- none found\n"), encoding="utf-8")
    text = run_main(monkeypatch, fc, "--models", "Gemini, groq")
    rows = [l for l in text.splitlines() if l.startswith("| ") and "---" not in l and "Post" not in l]
    assert [r.split("|")[1].strip() for r in rows] == ["alpha", "zeta", "solo"]      # agreed first, ties alphabetical
    assert "Panel: Gemini, Groq." in text


def test_main_out_option_and_empty_dir(fc, monkeypatch, tmp_path, capsys):
    out = tmp_path / "custom.md"
    monkeypatch.setattr(sys, "argv", ["fs", "--out", str(out)])
    S.main()
    assert out.read_text(encoding="utf-8").startswith("# Fact-check summary")
    assert "0 posts summarised" in capsys.readouterr().out


def test_main_post_with_only_outdated_flag_listed(fc, monkeypatch):
    (fc / "p.md").write_text(report("Gemini g", "OUTDATED DATA:\n- stale thing\n") + report("Mistral m", "OUTDATED DATA:\n- none found\n"), encoding="utf-8")
    (fc / "q.md").write_text(report("Gemini g", "FACTUAL ERRORS:\n- none found\n") + report("Mistral m", "FACTUAL ERRORS:\n- none found\n"), encoding="utf-8")
    text = run_main(monkeypatch, fc)
    assert "| p | 0 | 0 | 0 | 0 | 1 |" in text and "| q |" not in text

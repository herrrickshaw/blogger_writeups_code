import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "consistency-check"))
import checks as C  # noqa: E402

DISC = '<p data-gs-ai-disclosure-v1>AI</p>'


def test_declares_dark_ignores_comments():
    assert C._declares_dark("@media (prefers-color-scheme: dark){}")
    assert C._declares_dark('<html data-theme="dark">')
    assert not C._declares_dark("<!-- prefers-color-scheme explained -->")
    assert not C._declares_dark("/* prefers-color-scheme */ a{}")
    assert not C._declares_dark("<!-- x -->\n<!-- data-theme=\"dark\" -->")
    assert not C._declares_dark("<p>plain</p>")


def test_scripts_helpers():
    body = "<script>a</script><p>x</p><script type='x'>b</script><scripty>no</scripty>"
    assert C._scripts(body) == ["a", "b"]
    assert C._strip_scripts(body) == "<p>x</p><scripty>no</scripty>"


def test_disclaimer_not_in_script():
    assert C.r_disclaimer_not_in_script("<p>x</p>") == (True, "")
    ok, d = C.r_disclaimer_not_in_script(f"<script>1</script><script>var s='{DISC}'</script>")
    assert not ok and "#[2]" in d
    assert C.r_disclaimer_not_in_script(f"{DISC}<script>1</script>")[0]


def test_disclaimer_present_only_outside_script():
    assert C.r_disclaimer_present(DISC) == (True, "")
    ok, d = C.r_disclaimer_present(f"<script>'{DISC}'</script>")
    assert not ok and "no AI-disclosure" in d
    assert not C.r_disclaimer_present("")[0]


def test_no_inverted_media_query():
    assert C.r_no_inverted_media_query("a{}") == (True, "")
    ok, d = C.r_no_inverted_media_query("@media not all and (prefers-color-scheme:dark){} @media not all and (prefers-color-scheme:dark){}")
    assert not ok and d == "2 inverted dark-mode media query block(s)"


def test_dark_vars_locked_cases():
    assert C.r_dark_vars_locked("<p>x</p>") == (True, "n/a (no dark palette)")
    dark = "@media (prefers-color-scheme: dark){:root{--text:#eee}}"
    assert C.r_dark_vars_locked(dark) == (True, "n/a (vars declared but never consumed)")
    consumed = dark + " p{color:var(--text)}"
    ok, d = C.r_dark_vars_locked(consumed)
    assert not ok and "no !important" in d
    assert C.r_dark_vars_locked(consumed + " gs-light-lock-v1") == (True, "")
    assert C.r_dark_vars_locked(consumed + " :root{--text:#111 !important}")[0]
    for v in ("surface", "surface-alt", "border", "text", "text-mut", "ink", "page-bg"):
        assert not C.r_dark_vars_locked(dark + f" a{{color:var( --{v})}}")[0], v
    # --text-mut must not be mistaken for an unrelated var name
    assert C.r_dark_vars_locked(dark + " a{color:var(--textual)}")[0]


def test_translate_and_index_link():
    assert C.r_translate_widget("<div id=google_translate_element>") == (True, "")
    assert C.r_translate_widget("x") == (False, "missing Google Translate widget")
    assert C.r_index_link("topnav-index-link") == (True, "")
    assert C.r_index_link("x") == (False, "missing All-Articles index link")


def test_bw_override():
    assert C.r_bw_override("x") == (True, "n/a (no dark palette)")
    dark = "prefers-color-scheme"
    assert not C.r_bw_override(dark)[0]
    assert C.r_bw_override(dark + " BW-OVERRIDE")[0]
    assert C.r_bw_override(dark + " gs-light-lock-v1")[0]


def _cells(cells):
    return "<table>" + "".join(f"<tr><td>{c}</td></tr>" for c in cells) + "</table>"


def test_table_units_few_cells_not_applicable():
    assert C.r_table_units_in_header(_cells(["5 cr"] * 11)) == (True, "n/a (few cells)")


@pytest.mark.parametrize("cell", ["5 cr", "&#8377; 1,200 crore", "US$ 3.5 bn", "12%", "-4 MW", "5 kg.", "$5 MT (est)", "3 LMT", "5 lakh", "7 mn"])
def test_table_units_bare_number_cells_count(cell):
    body = _cells([cell] * 12)
    ok, d = C.r_table_units_in_header(body)
    assert not ok and d == "100% of 12 cells carry units"


@pytest.mark.parametrize("cell", ["~25.96% of all imports", "FY2025-26, 10.35% CAGR", "abc", "12", "5 widgets"])
def test_table_units_descriptive_cells_do_not_count(cell):
    assert C.r_table_units_in_header(_cells([cell] * 12)) == (True, "0%")


def test_table_units_threshold_30_percent_inclusive():
    # 10 cells with units out of 33 = 30.3% -> fail; 9 of 30 = 30% -> pass
    ok, d = C.r_table_units_in_header(_cells(["5 cr"] * 9 + ["abc"] * 21))
    assert ok and d == "30%"
    ok, d = C.r_table_units_in_header(_cells(["5 cr"] * 10 + ["abc"] * 23))
    assert not ok and d == "30% of 33 cells carry units"


def test_table_units_strips_tags_inside_cells():
    assert not C.r_table_units_in_header(_cells(["<b>5</b> cr"] * 12))[0]


def test_scripts_parse():
    assert C.r_scripts_parse("x", None) == (True, "skipped (no node)")
    assert C.r_scripts_parse("x", []) == (True, "")
    ok, d = C.r_scripts_parse("x", [2, 3])
    assert not ok and d == "JS syntax error in script(s) [2, 3]"


def test_wpi_attribution():
    assert C.r_wpi_attribution("<p>CPI by MoSPI</p>") == (True, "n/a")
    assert C.r_wpi_attribution("<p>WPI is published by MoSPI</p>") == (True, "")   # no adjacent phrase
    ok, d = C.r_wpi_attribution("<p>MoSPI publishes the Wholesale Price Index monthly</p>")
    assert not ok and d == "WPI attributed to MoSPI"
    assert not C.r_wpi_attribution("<p>The Wholesale Price Index, compiled by MoSPI each month</p>")[0]
    assert C.r_wpi_attribution("<p>MoSPI publishes the Wholesale Price Index; published by DPIIT</p>")[0]
    assert C.r_wpi_attribution("<p>Wholesale Price Index (not a MoSPI product), MoSPI</p>")[0]
    # a sentence end right after MoSPI is not an attribution
    assert C.r_wpi_attribution("<p>Wholesale Price Index is by DPIIT, unlike CPI from MoSPI.</p>")[0]
    assert C.r_wpi_attribution("<p>WPI</p>")[0]


def test_rule_table_integrity():
    names = [n for n, _, _ in C.STATIC_RULES]
    assert len(names) == len(set(names)) == 10
    sev = {n: s for n, s, _ in C.STATIC_RULES}
    assert sev["js-parses"] == C.BLOCKER and sev["dark-vars-locked"] == C.BLOCKER
    assert sev["wpi-attribution"] == C.MAJOR and sev["index-link"] == C.MINOR
    assert all(callable(f) for _, _, f in C.STATIC_RULES)
    assert "getComputedStyle" in C.CONTRAST_JS and "scrollWidth" in C.OVERFLOW_JS

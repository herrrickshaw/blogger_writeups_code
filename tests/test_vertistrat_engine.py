"""VertiStrat_DPR_Templates/engine.py is a script: importing it runs the five project models and
writes models.json to the current directory. Run it in tmp_path and check the financial identities."""
import json
import runpy
from pathlib import Path

import pytest

ENGINE = Path(__file__).resolve().parent.parent / "VertiStrat_DPR_Templates" / "engine.py"


@pytest.fixture(scope="module")
def ran(tmp_path_factory):
    import os
    d = tmp_path_factory.mktemp("engine")
    old = os.getcwd()
    os.chdir(d)
    try:
        ns = runpy.run_path(str(ENGINE))
    finally:
        os.chdir(old)
    return ns, json.loads((d / "models.json").read_text())


def test_writes_all_five_projects(ran):
    _, out = ran
    assert set(out) == {"biodiesel", "cbg", "ethanol", "saf", "food"}


def test_funding_identity_per_project(ran):
    ns, out = ran
    for k, v in out.items():
        m, cfg = v["m"], v["cfg"]
        assert m["fixed"] == pytest.approx(sum(cfg["capex"].values()))
        assert m["total"] == pytest.approx(m["fixed"] + m["wc_margin"])
        assert m["TL"] == round(cfg["loan"]["share"] * m["fixed"], 2)
        assert m["EQ"] == pytest.approx(round(m["total"] - m["TL"] - m["sub"], 2))
        assert m["TL"] + m["EQ"] + m["sub"] == pytest.approx(m["total"], abs=0.02)


def test_debt_schedule_amortises_to_zero_after_tenor(ran):
    _, out = ran
    for k, v in out.items():
        sched, cfg, m = v["m"]["sched"], v["cfg"], v["m"]
        L = cfg["loan"]
        assert sched[0]["open"] == pytest.approx(m["TL"])
        for y, s in enumerate(sched):
            assert s["close"] == pytest.approx(s["open"] - s["rp"])
            assert s["intr"] == pytest.approx(s["open"] * L["rate"])
            if y < L["moratorium"]:
                assert s["rp"] == 0
        # the model only runs 10 years: a longer tenor leaves a balance outstanding at year 10
        repaid_years = min(10, L["tenor"]) - L["moratorium"]
        assert sum(s["rp"] for s in sched) == pytest.approx(m["TL"] * repaid_years / (L["tenor"] - L["moratorium"]))
        if L["tenor"] <= 10:
            assert sched[L["tenor"] - 1]["close"] == pytest.approx(0, abs=1e-9)
            assert all(s["rp"] == 0 for s in sched[L["tenor"]:])
        else:
            assert sched[-1]["close"] > 0


def test_irr_is_npv_zero_root_and_dscr_summary(ran):
    ns, out = ran
    for k, v in out.items():
        m = v["m"]
        assert -0.9 < m["irr"] < 6
        assert m["min_dscr"] <= m["avg_dscr"]
        dscrs = [s["dscr"] for s in m["sched"] if s["ds"] > 0]
        assert m["min_dscr"] == pytest.approx(min(dscrs))
        assert m["avg_dscr"] == pytest.approx(sum(dscrs) / len(dscrs))


def test_utilisation_ramp_drives_revenue(ran):
    _, out = ran
    for v in out.values():
        rows = v["m"]["rows"]
        assert len(rows) == 10 and rows[0]["year"] == 1 and rows[-1]["year"] == 10
        assert rows[0]["rev"] < rows[4]["rev"]               # ramp-up years earn less
        assert rows[0]["util"] == v["cfg"]["util"][0]


def test_sensitivity_directions(ran):
    _, out = ran
    for k, v in out.items():
        s = v["s"]
        by = {r["label"]: r for r in s["rows"]}
        base = s["base"]
        assert by["Main product price -10%"]["ebitda"] < base["ebitda"] < by["Main product price +10%"]["ebitda"]
        assert by["Main feedstock cost +10%"]["ebitda"] > by["Main feedstock cost +20%"]["ebitda"]
        assert by["Main feedstock cost +10%"]["ebitda"] < base["ebitda"]
        both = by["Both: price -10% and feedstock +10%"]
        assert both["ebitda"] < by["Main product price -10%"]["ebitda"]
        assert both["irr"] < base["irr"]


def test_model_multiplier_exact_effect_on_revenue(ran):
    ns, _ = ran
    c = ns["cfgs"]["biodiesel"]
    base = ns["model"](c)["rows"][4]["rev"]
    l0 = c["rev"][0]
    delta = l0["qty"] * c["util"][4] * l0["price"] / 1e7
    assert ns["model"](c, {"rev0": 1.1})["rows"][4]["rev"] == pytest.approx(base + 0.1 * delta)
    assert ns["model"](c, None)["rows"][4]["rev"] == pytest.approx(base)


def test_model_payback_and_no_debt_service_edge(ran):
    ns, _ = ran
    import copy
    c = copy.deepcopy(ns["cfgs"]["food"])
    m = ns["model"](c)
    assert m["pb"] is None or 0 < m["pb"] < 11
    c["loan"]["share"] = 0.0
    m0 = ns["model"](c)
    assert m0["TL"] == 0 and all(s["ds"] == 0 for s in m0["sched"])
    assert m0["avg_dscr"] == 0 and m0["min_dscr"] == 0

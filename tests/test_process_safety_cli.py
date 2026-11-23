"""CLI wiring for `python -m process_safety`, checked against the library functions it drives,
plus the library branches the existing suite leaves open."""
import dataclasses
import json
import math

import pytest

from process_safety import __main__ as cli
from process_safety import fireball, flare, relief, sil, standards, tank_venting, vapour_fire


def run(capsys, *argv):
    assert cli.main(list(argv)) == 0
    return capsys.readouterr().out


def js(capsys, *argv):
    return json.loads(run(capsys, *argv))


def asdict(o):
    return json.loads(json.dumps(dataclasses.asdict(o), default=float))


def test_relief_gas_matches_library_with_defaults(capsys):
    got = js(capsys, "relief-gas", "--W", "20000", "--T", "400", "--set-g", "1000", "--M", "44", "--k", "1.15")
    P1 = relief.relieving_pressure_kpa(1000, "single_non_fire")
    want = asdict(relief.gas_area(20000, 400, P1, relief.ATM, 44, 1.15, 1.0, Kb=1.0, Kc=1.0, set_g_kpa=1000))
    assert got == want


def test_relief_gas_back_pressure_case_and_factors(capsys):
    got = js(capsys, "relief-gas", "--W", "20000", "--T", "400", "--set-g", "1000", "--M", "44", "--k", "1.15",
             "--back-g", "300", "--case", "fire", "--Z", "0.9", "--Kb", "0.8", "--Kc", "0.9")
    P1 = relief.relieving_pressure_kpa(1000, "fire")
    want = asdict(relief.gas_area(20000, 400, P1, 300 + relief.ATM, 44, 1.15, 0.9, Kb=0.8, Kc=0.9, set_g_kpa=1000))
    assert got == want
    assert P1 == pytest.approx(1000 * 1.21 + relief.ATM)


def test_relief_steam_and_liquid(capsys):
    got = js(capsys, "relief-steam", "--W", "5000", "--set-g", "1000", "--Ksh", "0.9")
    assert got == asdict(relief.steam_area(5000, relief.relieving_pressure_kpa(1000), Ksh=0.9))
    got = js(capsys, "relief-liquid", "--Q", "60", "--rho", "850", "--set-g", "1000", "--back-g", "50", "--mu", "0.5")
    assert got == asdict(relief.liquid_area(60, 850, 1000 * 1.10 + relief.ATM, 50 + relief.ATM, 0.5))


def test_relief_fire_with_area_and_geometry(capsys):
    got = js(capsys, "relief-fire", "--wetted-area", "50", "--latent", "300", "--F", "0.5", "--no-drainage")
    assert got["wetted_area_m2"] == 50
    assert got["relief_rate_kg_h"] == pytest.approx(relief.fire_relief_rate_kg_h(50, 300, 0.5, False))
    assert got["heat_input_kW"] == pytest.approx(relief.fire_heat_input_W(50, 0.5, False) / 1e3)
    g2 = js(capsys, "relief-fire", "--D", "2", "--L", "6", "--level", "1", "--orientation", "vertical", "--elevation", "1", "--latent", "300")
    assert g2["wetted_area_m2"] == pytest.approx(relief.wetted_area_cylinder(2, 6, 1, "vertical", 1))
    assert g2["relief_rate_kg_h"] == pytest.approx(relief.fire_relief_rate_kg_h(g2["wetted_area_m2"], 300, 1.0, True))


def test_tank_normal(capsys):
    got = js(capsys, "tank-normal", "--volume", "500", "--fill", "20", "--empty", "10", "--volatile")
    assert got == json.loads(json.dumps(tank_venting.normal_venting(500, 20, 10, True), default=float))
    quiet = js(capsys, "tank-normal", "--volume", "500")
    assert quiet == json.loads(json.dumps(tank_venting.normal_venting(500, 0.0, 0.0, False), default=float))
    assert quiet != got


def test_tank_fire_named_and_numeric_F_and_optional_props(capsys):
    got = js(capsys, "tank-fire", "--shape", "vertical", "--D", "10", "--L", "12", "--F", "insulated_11.4",
             "--normal-capacity", "1000", "--L-kj-kg", "400", "--T", "350", "--M", "70")
    A = tank_venting.wetted_area_m2("vertical", 10, 12, 0.0)
    req = tank_venting.fire_venting_Nm3h(A, 0.15, design_barg=0.07, L_kJ_kg=400, T_K=350, M=70)
    assert got["F"] == 0.15 and got["wetted_area_m2"] == pytest.approx(A)
    assert got["required_Nm3h_eq1B"] == pytest.approx(req)
    assert got["additional_emergency_vent_Nm3h"] == pytest.approx(max(0, req - 1000))
    assert got["required_Nm3h_simplified"] == pytest.approx(tank_venting.fire_venting_simplified(A, 0.15, 0.07))
    num = js(capsys, "tank-fire", "--wetted-area", "100", "--F", "0.5", "--design-barg", "0.1")
    assert num["F"] == 0.5 and num["wetted_area_m2"] == 100
    assert num["required_Nm3h_simplified"] == pytest.approx(tank_venting.fire_venting_simplified(100, 0.5, 0.1))


def test_vapour_fire_cli_matches_simulate(capsys):
    argv = ["vapour-fire", "--volume", "5", "--area", "15", "--D", "1.2", "--wall-mm", "12", "--M", "30", "--k", "1.2",
            "--p0-g", "500", "--psv-area", "300", "--psv-set-g", "800", "--t-end", "300", "--strength", "300", "--q", "120"]
    got = js(capsys, *argv)
    v = vapour_fire.Vessel(5, 15, 1.2, 12, 30, 1.2, 500, strength_MPa=300)
    want = asdict(vapour_fire.simulate(v, 120, 300, 800, bdv_area_mm2=0.0, bdv_open_s=900.0, h_in=20.0, t_end_s=300))
    assert got == want


def test_flare_lopa_pfd_fireball(capsys):
    got = js(capsys, "flare", "--mass", "10", "--lhv", "46", "--mw", "16", "--flame-length", "20", "--tau", "0.8")
    Q = flare.heat_release_W(10, 46)
    F = flare.radiant_fraction(16)
    assert got["heat_release_MW"] == pytest.approx(Q / 1e6) and got["radiant_fraction"] == F
    for k, v in flare.radiation_checks(Q, F, 20, 0.8).items():
        assert got[k] == v
    got = js(capsys, "lopa", "--ie", "0.1", "--ipl", "0.1", "0.01", "--target", "1e-6", "--modifier", "0.5")
    assert got == asdict(sil.lopa(0.1, [0.1, 0.01], 1e-6, 0.5))
    got = js(capsys, "lopa", "--ie", "0.1", "--target", "1e-6")
    assert got == asdict(sil.lopa(0.1, [], 1e-6, 1.0))
    got = js(capsys, "pfd", "--arch", "1oo2", "--lambda-du", "2e-6", "--ti-years", "1", "--beta", "0.05")
    v = sil.pfd_avg("1oo2", 2e-6, 8760, 0.05)
    assert got == {"pfd_avg": v, "rrf": 1 / v, "achieves": sil.sil_for_pfd(v)}
    got = js(capsys, "fireball", "--mass", "1000", "--hc", "46")
    b = fireball.fireball(1000, 46, 0.3)
    assert got["diameter_m"] == b["diameter_m"]
    assert set(got["distance_to_kW_m2"]) == {"37.5", "12.5", "4.0"}
    assert got["distance_to_kW_m2"]["12.5"] == fireball.distance_to_flux_m(b, 12.5)
    got = js(capsys, "fireball", "--mass", "1000", "--hc", "46", "--fraction", "0.1")
    assert got["diameter_m"] == fireball.fireball(1000, 46, 0.1)["diameter_m"]


def test_coverage_lists_every_topic(capsys):
    out = run(capsys, "coverage")
    for topic, (stds, mod, status) in standards.TOPICS.items():
        assert f"- {topic}\n    standards: {', '.join(stds)}\n    code: {mod or '-'}\n    status: {status}" in out


def test_cli_requires_subcommand_and_rejects_bad_choice():
    with pytest.raises(SystemExit) as e:
        cli.main([])
    assert e.value.code == 2
    with pytest.raises(SystemExit):
        cli.main(["relief-gas", "--W", "1", "--T", "1", "--set-g", "1", "--M", "1", "--k", "1.2", "--case", "bogus"])
    with pytest.raises(SystemExit):
        cli.main(["pfd", "--arch", "3oo3", "--lambda-du", "1e-6", "--ti-years", "1"])


def test_out_helper_handles_dataclass_and_dict(capsys):
    cli._out({"a": 1})
    assert json.loads(capsys.readouterr().out) == {"a": 1}
    cli._out(sil.LopaResult(1, 2, 3, 4, 5, "x", True))
    assert json.loads(capsys.readouterr().out)["sil_needed"] == "x"


# ---------------------------------------------------------- library gaps
def test_thermal_dose():
    assert fireball.thermal_dose(8, 10) == pytest.approx(8 ** (4 / 3) * 10) == pytest.approx(160)
    assert fireball.thermal_dose(0, 10) == 0


def test_distance_to_flux_none_when_target_unreachable_both_ways():
    fb = fireball.fireball(1000, 46, 0.3)
    assert fireball.distance_to_flux_m(fb, 1e9) is None          # even the peak never reaches it
    far = fireball.distance_to_flux_m(fb, 1e-12)                  # farther than 100 diameters -> not reached
    assert far is None or far > fb["diameter_m"]
    d = fireball.distance_to_flux_m(fb, 12.5)
    assert d > 0 and fireball.incident_kW_m2(fb, d) == pytest.approx(12.5, rel=1e-3)


def test_flare_helpers():
    assert flare.heat_release_W(2, 40) == 80e6
    assert flare.flame_centre_distance(3, 1.5, 5.5) == pytest.approx(5.0)
    assert flare.flame_centre_distance(0, 2, 2) == 0


def test_relieving_pressure_by_case():
    assert relief.relieving_pressure_kpa(100) == pytest.approx(100 * (1 + relief.ACCUMULATION["single_non_fire"]) + relief.ATM)
    assert relief.relieving_pressure_kpa(0, "fire") == relief.ATM


def test_steam_napier_correction_regions_and_limit():
    low = relief.steam_area(1000, 10339)
    mid = relief.steam_area(1000, 15000)
    assert low.detail["Kn"] == 1.0
    assert mid.detail["Kn"] == pytest.approx((0.02764 * 15000 - 1000) / (0.03324 * 15000 - 1061))
    assert relief.steam_area(1000, 22060).detail["Kn"] == pytest.approx((0.02764 * 22060 - 1000) / (0.03324 * 22060 - 1061))
    with pytest.raises(ValueError, match="Napier"):
        relief.steam_area(1000, 22061)


def test_liquid_area_requires_positive_dp():
    with pytest.raises(ValueError, match="P1 must exceed P2"):
        relief.liquid_area(10, 800, 100, 100)
    with pytest.raises(ValueError):
        relief.liquid_area(10, 800, 90, 100)


def test_fire_relief_rate_formula():
    q = relief.fire_heat_input_W(40, 1.0, True)
    assert relief.fire_relief_rate_kg_h(40, 250) == pytest.approx(q * 3.6 / 250)
    assert relief.fire_relief_rate_kg_h(40, 250, 0.5) == pytest.approx(0.5 * relief.fire_relief_rate_kg_h(40, 250))
    assert relief.fire_relief_rate_kg_h(40, 250, adequate_drainage_and_firefighting=False) > relief.fire_relief_rate_kg_h(40, 250)


def test_pfd_unsupported_arch_and_sil_edges():
    with pytest.raises(ValueError, match="unsupported architecture"):
        sil.pfd_avg("3oo4", 1e-6, 8760)
    assert sil.sil_for_pfd(0.1) == "below SIL 1"
    assert sil.sil_for_pfd(0.05) == "SIL 1"
    assert sil.sil_for_pfd(1e-5) == "SIL 4"
    assert sil.sil_for_pfd(1e-9) == "SIL 4 or better (>SIL 4 not claimable)"


def test_max_proof_test_interval_caps_at_ten_million_hours():
    assert sil.max_proof_test_interval_h("1oo1", 1e-20, 0.1) == 1e7


def test_max_proof_test_interval_bisection_meets_target():
    ti = sil.max_proof_test_interval_h("1oo1", 1e-6, 0.01)
    assert sil.pfd_avg("1oo1", 1e-6, ti) <= 0.01 < sil.pfd_avg("1oo1", 1e-6, ti * 1.001)
    assert ti == pytest.approx(0.01 * 2 / 1e-6, rel=1e-6)


def test_sif_pfd_adds_subsystems():
    total, band = sil.sif_pfd({"sensor": 1e-3, "logic": 1e-4, "final": 5e-3})
    assert total == pytest.approx(6.1e-3) and band == "SIL 2"


def test_tank_interp_proportional_below_and_error_above():
    t = [(10.0, 100.0), (20.0, 300.0)]
    assert tank_venting._interp(t, 5.0, 1) == 50.0
    assert tank_venting._interp(t, 10.0, 1) == 100.0
    assert tank_venting._interp(t, 15.0, 1) == 200.0
    assert tank_venting._interp(t, 20.0, 1) == 300.0
    with pytest.raises(ValueError, match="above table range"):
        tank_venting._interp(t, 20.1, 1)


def test_wetted_area_shapes_and_bad_shape():
    assert tank_venting.wetted_area_m2("vertical", 10, 12, 0.0) == pytest.approx(math.pi * 10 * min(12, tank_venting.MAX_HEIGHT_M))
    assert tank_venting.wetted_area_m2("vertical", 10, 12, 100.0) == 0.0     # raised above the 9.14 m wetted ceiling
    s = tank_venting.wetted_area_m2("sphere", 8)
    assert s >= 0.55 * math.pi * 64
    h = tank_venting.wetted_area_m2("horizontal", 3, 10)
    assert h >= 0.75 * (math.pi * 3 * 10 + math.pi * 9 / 2)
    with pytest.raises(ValueError):
        tank_venting.wetted_area_m2("cube", 1)


def test_simplified_fire_venting_small_and_large_areas():
    assert tank_venting.fire_venting_simplified(10.0) < tank_venting.fire_venting_simplified(100.0)
    assert tank_venting.fire_venting_simplified(100.0, F=0.5) == pytest.approx(0.5 * tank_venting.fire_venting_simplified(100.0))
    assert tank_venting.fire_venting_simplified(300.0) > tank_venting.fire_venting_simplified(259.0)


def test_emergency_vent_shortfall_floor_zero():
    assert tank_venting.emergency_vent_shortfall_Nm3h(1000, 400) == 600
    assert tank_venting.emergency_vent_shortfall_Nm3h(300, 400) == 0.0

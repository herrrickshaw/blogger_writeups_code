"""Calculation block for the sodium-ion post. Pure arithmetic, every result asserted. Imported by build.py; run alone for the sample check:
python3 out/research/sodium-ion-battery-2026/calc.py"""
# ---------------------------------------------------------------- inputs: claims and measurements, each with its source in build.py
CELL = {"Na_Naxtra": 175, "Na_KPIT_now": 110, "Na_KPIT_top": 170, "LFP_hi": 205, "LFP_lo": 160, "NMC": 280}   # cell Wh/kg; Naxtra, KPIT, Qilin are company claims; LFP 205 only in a search excerpt of an IEA page
PACK_FRAC = {"low": 0.70, "mid": 0.80, "high": 0.85}      # ASSUMPTION: pack Wh/kg as a share of cell Wh/kg; no opened source gives it
DOD = 0.90                                                # ASSUMPTION: usable depth of discharge
FADE_AVG = 0.90                                           # ASSUMPTION: capacity fades linearly from 100% to the 80% end-of-life threshold, so the average is 90%
RTE = 0.90                                                # ASSUMPTION: round-trip efficiency, stationary only, same for both
EOL = 0.80
PRICE = {"Na": 229, "LFP": 200}                           # US$/kWh upfront, Wood Mackenzie global averages
TCO_CLAIM = 0.21
CYC = {"LFP_low": 3000, "LFP_dnv_low": 20 * 135, "LFP_dnv_high": 20 * 448, "LFP_sonnen": 10000, "KPIT_low": 4000, "KPIT_high": 6000, "Naxtra": 10000}
assert CYC["LFP_dnv_low"] == 2700 and CYC["LFP_dnv_high"] == 8960
assert abs(1 - EOL - 0.2) < 1e-9 and abs(FADE_AVG - (1 + EOL) / 2) < 1e-9

def pack_wh_kg(cell, frac):
    return cell * frac

def pack_mass(usable_kwh, cell, frac, dod=DOD):
    return usable_kwh * 1000 / (pack_wh_kg(cell, frac) * dod)

def life_kwh_per_kg(cell, frac, cycles, dod=DOD, rte=1.0):
    return pack_wh_kg(cell, frac) * dod * cycles * FADE_AVG * rte / 1000

def breakeven_cycles(n_ref, cell_ref, cell_new):
    """cycles the lower-density chemistry needs to deliver the same lifetime kWh per kg of pack (same pack fraction, depth of discharge and fade)."""
    return n_ref * cell_ref / cell_new

# ---------------------------------------------------------------- 1. per kg
SIZES = {"3 kWh e-scooter": 3, "40 kWh small car": 40, "2 MWh stationary container": 2000}
MASS = {(s, k, f): pack_mass(e, CELL[k], PACK_FRAC[f]) for s, e in SIZES.items() for k in CELL for f in PACK_FRAC}
# sample consistency checks
assert round(pack_wh_kg(175, 0.8)) == 140 and round(pack_wh_kg(205, 0.8)) == 164
m_na, m_lfp = MASS[("40 kWh small car", "Na_Naxtra", "mid")], MASS[("40 kWh small car", "LFP_hi", "mid")]
assert round(m_na, 1) == 317.5 and round(m_lfp, 1) == 271.0
assert abs(m_na / m_lfp - 205 / 175) < 1e-9                  # mass ratio is the inverse density ratio whatever the pack fraction
for s in SIZES:
    for f in PACK_FRAC:                                          # more kWh -> more kg; higher density -> fewer kg; higher pack fraction -> fewer kg
        assert MASS[(s, "Na_Naxtra", f)] > MASS[(s, "LFP_hi", f)] and MASS[(s, "NMC", f)] < MASS[(s, "LFP_hi", f)]
    assert MASS[(s, "Na_Naxtra", "low")] > MASS[(s, "Na_Naxtra", "mid")] > MASS[(s, "Na_Naxtra", "high")]
assert round(100 * (205 / 175 - 1), 1) == 17.1 and round(100 * (1 - 175 / 205), 1) == 14.6
EXTRA = {s: MASS[(s, "Na_Naxtra", "mid")] - MASS[(s, "LFP_hi", "mid")] for s in SIZES}
assert round(EXTRA["3 kWh e-scooter"], 1) == 3.5 and round(EXTRA["40 kWh small car"], 1) == 46.5 and round(EXTRA["2 MWh stationary container"] / 1000, 2) == 2.32
# the weight penalty is zero or negative if LFP is the 160 Wh/kg design
assert MASS[("40 kWh small car", "Na_Naxtra", "mid")] < MASS[("40 kWh small car", "LFP_lo", "mid")]

# vehicle: ASSUMPTIONS
CAR_BODY = 1000       # kg without battery
CONS_REF = 45 / 400   # kWh/km: the 45 kWh Naxtra pack's claimed 400 km CLTC range, as anchor
ELAST = 0.4           # share of consumption that scales with mass
def car_range(usable_kwh, pack_kg, ref_pack_kg):
    m_ref, m = CAR_BODY + ref_pack_kg, CAR_BODY + pack_kg
    cons = CONS_REF * (1 + ELAST * (m - m_ref) / m_ref)
    return usable_kwh / cons
r_lfp = car_range(40, m_lfp, m_lfp); r_na = car_range(40, m_na, m_lfp)
assert round(r_lfp) == 356 and r_na < r_lfp
RANGE_LOSS_PCT = 100 * (1 - r_na / r_lfp)
assert round(RANGE_LOSS_PCT, 1) == 1.4
SCOOTER_PAYLOAD_PCT = 100 * EXTRA["3 kWh e-scooter"] / 75      # against a 75 kg rider (ASSUMPTION)
assert round(SCOOTER_PAYLOAD_PCT, 1) == 4.6
# Changan Nevo A06 claimed CLTC figures: 63.18 kWh lithium-ion 630 km; 45 kWh Naxtra 400 km
NEVO_LI, NEVO_NA = 630 / 63.18, 400 / 45
assert round(NEVO_LI, 2) == 9.97 and round(NEVO_NA, 2) == 8.89 and round(100 * (1 - NEVO_NA / NEVO_LI), 1) == 10.9

# ---------------------------------------------------------------- 2/3. lifetime energy per kg and break-even
LIFE = {}
for name, cell in [("LFP 205", 205), ("LFP 160", 160), ("Na 175", 175), ("Na 110", 110)]:
    for n in (3000, 6000, 10000):
        LIFE[(name, n)] = life_kwh_per_kg(cell, PACK_FRAC["mid"], n)
assert round(LIFE[("LFP 205", 6000)]) == 797 and round(LIFE[("Na 175", 10000)]) == 1134
assert LIFE[("Na 175", 10000)] > LIFE[("LFP 205", 6000)] > LIFE[("Na 175", 3000)]
assert LIFE[("Na 175", 6000)] < LIFE[("LFP 205", 6000)] and LIFE[("Na 175", 10000)] > LIFE[("LFP 205", 6000)]
BE = {(n, c): breakeven_cycles(n, 205, c) for n in (3000, 6000, 10000) for c in (175, 170, 110)}
assert round(BE[(3000, 175)]) == 3514 and round(BE[(6000, 175)]) == 7029 and round(BE[(10000, 175)]) == 11714
assert round(BE[(3000, 110)]) == 5591
assert abs(life_kwh_per_kg(175, .8, BE[(6000, 175)]) - life_kwh_per_kg(205, .8, 6000)) < 1e-6          # identity check
assert all(abs(life_kwh_per_kg(c, f, breakeven_cycles(n, 205, c)) - life_kwh_per_kg(205, f, n)) < 1e-6 for n in (3000, 10000) for c in (110, 175) for f in PACK_FRAC.values())
assert breakeven_cycles(6000, 160, 175) < 6000      # against LFP 160 the sodium-ion cell needs fewer cycles

# ---------------------------------------------------------------- 4. cost per kWh delivered (upfront price only, no augmentation, no opex)
def cost_per_kwh_delivered(price, cycles, dod=DOD, rte=RTE):
    return price / (dod * cycles * FADE_AVG * rte)
CPD = {(c, n): cost_per_kwh_delivered(PRICE[c], n) for c in PRICE for n in (3000, 6000, 10000)}
assert round(CPD[("LFP", 6000)], 4) == round(200 / (0.9 * 6000 * 0.9 * 0.9), 4)
assert abs(CPD[("Na", 6000)] / CPD[("LFP", 6000)] - 229 / 200) < 1e-9
COST_BE = 229 / 200
assert round(100 * (COST_BE - 1), 1) == 14.5
# 20-year project: daily cycling = 7,300 cycles
PROJECT_CYCLES = 20 * 365
assert PROJECT_CYCLES == 7300 and CYC["LFP_low"] < PROJECT_CYCLES < CYC["LFP_sonnen"]
# back-solve of the 21% claim: TCO_Na = 0.79 TCO_LFP, TCO = capex + other (opex + augmentation over 20 years), US$/kWh
def implied_lfp_other(na_other):
    return (PRICE["Na"] + na_other) / (1 - TCO_CLAIM) - PRICE["LFP"]
IMPL = {y: implied_lfp_other(y) for y in (0, 25, 50, 100)}
assert round(IMPL[0], 1) == 89.9 and round(IMPL[25], 1) == 121.5 and round(IMPL[50], 1) == 153.2 and round(IMPL[100], 1) == 216.5
for y, x in IMPL.items():
    assert abs((PRICE["Na"] + y) - (1 - TCO_CLAIM) * (PRICE["LFP"] + x)) < 1e-9
assert IMPL[0] / PRICE["LFP"] > 0.44 and round(100 * IMPL[0] / PRICE["LFP"]) == 45
# if both carried the same other costs the claim would be impossible
assert all((PRICE["Na"] + x) > (1 - TCO_CLAIM) * (PRICE["LFP"] + x) for x in range(0, 2000, 10))

if __name__ == "__main__":
    print("sample OK; masses (kg), 40 kWh car, mid fraction:", {k: round(MASS[("40 kWh small car", k, "mid")], 1) for k in CELL})
    print("extra kg Na175 vs LFP205:", {s: round(v, 1) for s, v in EXTRA.items()})
    print("range LFP/Na km:", round(r_lfp), round(r_na), "loss %", round(RANGE_LOSS_PCT, 2))
    print("life kWh/kg:", {k: round(v) for k, v in LIFE.items()})
    print("break-even:", {k: round(v) for k, v in BE.items()})
    print("cost per kWh delivered:", {k: round(v, 4) for k, v in CPD.items()})
    print("implied LFP other cost:", {k: round(v, 1) for k, v in IMPL.items()})

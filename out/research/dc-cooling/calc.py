"""Arithmetic behind the closed- vs open-loop cooling post. All inputs are stated assumptions or sourced figures."""
from math import radians, sin, cos, asin, sqrt

# --- evaporative water per kWh of IT load (physics)
LATENT = 2.43            # MJ/kg, latent heat of vaporisation near 30 C
KWH = 3.6                # MJ
EVAP_SHARE = 0.85        # share of heat a cooling tower rejects by evaporation (rest is sensible)
COP_WC = 6.3             # ECBC 2017 minimum, large water-cooled centrifugal chiller
COP_AC = 3.0             # ECBC 2017 minimum, air-cooled chiller >= 260 kW
AUX_WC = 0.04            # cooling-tower fans + condenser pumps, kWh per kWh of heat (assumption)
heat = 1 + 1 / COP_WC    # heat rejected at the tower per kWh of IT heat
evap = heat * KWH / LATENT * EVAP_SHARE
def wue(cycles): return evap + evap / (cycles - 1)
print(f"heat {heat:.3f}  evap {evap:.2f} L/kWh  WUE C=3 {wue(3):.2f}  C=6 {wue(6):.2f}")

# --- energy penalty of dry (air-cooled) heat rejection, worst case: compressors every hour
e_wc = 1 / COP_WC + AUX_WC
e_ac = 1 / COP_AC
pen = e_ac - e_wc
print(f"cooling kWh per kWh IT: water-cooled {e_wc:.3f}, air-cooled {e_ac:.3f}, penalty {pen:.3f}")

# --- off-site water in that extra electricity
COAL_L = 2.68            # NTPC FY2023-24 specific water consumption, L/kWh
THERMAL_SHARE = 0.745    # thermal share of generation 2024-25 (CERC from CEA)
grid_l = COAL_L * THERMAL_SHARE
offsite = pen * grid_l
for c in (3, 6):
    print(f"C={c}: on-site saved {wue(c):.2f} L, off-site added {offsite:.2f} L, net saving {(wue(c)-offsite)/wue(c)*100:.0f}%")

# --- implied price of water saved by dry cooling, worst case
TARIFF = 7.0             # Rs per kWh, assumed industrial tariff
for c in (3, 6):
    print(f"C={c}: Rs per kL saved {pen*TARIFF/(wue(c)-offsite)*1000:.0f}")

# --- desalination energy for tower make-up
SWRO = 3.5               # kWh per m3, typical seawater RO
print(f"desal kWh per kWh IT at C=3: {wue(3)/1000*SWRO:.4f}")

# --- 100 MW IT at 70% average load
it_kwh = 100e3 * 8760 * 0.7
print(f"100 MW: water C=3 {wue(3)*it_kwh/1e9:.2f} bn L/yr = {wue(3)*it_kwh/365/1e6:.2f} MLD; extra power {pen*it_kwh/1e6:.0f} GWh; Rs {pen*it_kwh*TARIFF/1e7:.0f} cr")

# --- published intensities, implied L/kWh (full load unless noted)
print("25.5 ML per MW-yr ->", round(25.5e6 / 8760e3, 2))
print("780 ML per 30 MW-yr ->", round(780e6 / (30e3 * 8760), 2))
print("2 ML/day per 100 MW ->", round(2e6 / (100e3 * 24), 2))
print("150 bn L on 1.5 GW full load ->", round(150e9 / (1.5e6 * 8760), 1))

# --- distance from campus to nearest cable landing city
def km(a, b):
    la1, lo1, la2, lo2 = map(radians, (*a, *b))
    h = sin((la2 - la1) / 2) ** 2 + cos(la1) * cos(la2) * sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371 * asin(sqrt(h))
LAND = {"Mumbai": (19.076, 72.878), "Chennai": (13.083, 80.271), "Kochi": (9.931, 76.267),
        "Thoothukudi": (8.764, 78.135), "Visakhapatnam": (17.687, 83.219)}
SITES = {"Visakhapatnam": (17.687, 83.219), "Jamnagar": (22.470, 70.057), "Hyderabad": (17.385, 78.487),
         "Navi Mumbai": (19.033, 73.030), "Thane": (19.218, 72.978), "Chennai (Siruseri)": (12.826, 80.219),
         "Greater Noida": (28.474, 77.504), "Pune": (18.520, 73.857), "Bengaluru": (12.972, 77.595)}
for s, c in SITES.items():
    n = min(LAND, key=lambda k: km(c, LAND[k]))
    print(f"{s:20s} nearest landing {n:14s} {km(c, LAND[n]):5.0f} km")

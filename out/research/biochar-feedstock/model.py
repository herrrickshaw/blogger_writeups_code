"""Biochar likelihood model: crop x state. Run with /usr/bin/python3 (needs pandas).
Inputs: production_state_crop_avg_2022-25.csv, intensification_state_crop_2003-06_to_2022-25.csv, openness_signals.csv
(this folder), and the UPAg district file in the india-mandi-arrivals clone for the district ranking.
Writes: residue_biochar_state_crop.csv, soil_need_state.csv, likelihood_state_crop.csv, nutrient_removal_state.csv,
districts_top.csv, sensitivity.csv and results.json (everything the post builder needs).

Units: production in lakh tonnes (cotton in lakh bales of 170 kg lint). 1 lakh t = 100 kt = 0.1 Mt.
Every coefficient is listed in COEF with its source; the post repeats them."""
import json, math, pathlib
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
DISTRICT_FILE = pathlib.Path("/home/user/india-mandi-arrivals/data/upag/apy_district.csv.gz")

STATES = ["Punjab", "Haryana", "Uttar Pradesh", "Bihar", "West Bengal", "Odisha", "Chhattisgarh", "Jharkhand",
          "Madhya Pradesh", "Rajasthan", "Gujarat", "Maharashtra", "Telangana", "Andhra Pradesh", "Karnataka",
          "Tamil Nadu", "Assam", "Uttarakhand"]

# --- Residue model -------------------------------------------------------------------------------------------
# Rice straw/paddy surplus fractions: MNRE/ASCI biomass atlas (state surplus / generation); national 0.23.
RICE_SF = {"Punjab": .99, "Haryana": .50, "Uttar Pradesh": .045, "Madhya Pradesh": .38, "Bihar": .10,
           "West Bengal": .05, "Odisha": .18, "Chhattisgarh": .20, "Andhra Pradesh": .18, "Telangana": .13,
           "Tamil Nadu": .17, "Karnataka": .17, "Assam": .08, "Gujarat": .04, "Maharashtra": .01, "Rajasthan": .17}
RICE_SF_NAT = .23
WHEAT_SF = {"Punjab": .10, "Haryana": .10}   # elsewhere a flat 0.20 (assumption; atlas national 0.17)
WHEAT_SF_OTHER = .20


def rice_sf(s): return RICE_SF.get(s, RICE_SF_NAT)
def wheat_sf(s): return WHEAT_SF.get(s, WHEAT_SF_OTHER)


# key, label, short, production column, residue per unit production, surplus fraction fn, biochar yield, ICM/EBC weight
COEF = [
    ("rice", "Rice straw", "Rice", "Rice", 1.5 * 1.0, rice_sf, .35, 1.0),      # paddy = 1.5 x milled; straw 1.0 x paddy
    ("wheat", "Wheat straw", "Wheat", "Wheat", 1.5, wheat_sf, .30, 1.0),
    ("maize", "Maize stalk and cob", "Maize", "Maize", 2.0 + 0.3, lambda s: .22, .28, 1.0),
    ("cotton", "Cotton stalk", "Cotton", "Cotton", 0.17 * 3 * 3.8, lambda s: .44, .33, 1.0),  # bales -> lint -> seed cotton
    ("cane", "Sugarcane bagasse", "Cane", "Sugarcane", 0.33, lambda s: .35, .26, 0.5),    # boiler fuel today: ICM leakage
    ("soy", "Soybean stalk", "Soy", "Soybean", 1.7, lambda s: .36, .30, 1.0),
    ("mustard", "Mustard stalk", "Must.", "Rapeseed & Mustard", 1.8, lambda s: .30, .30, 1.0),
    ("gram", "Gram stalk", "Gram", "Gram", 1.1, lambda s: .33, .30, 1.0),
    ("tur", "Tur stalk", "Tur", "Tur", 2.5, lambda s: .19, .30, 1.0),
    ("gnut", "Groundnut stalk and shell", "G.nut", "Groundnut", 2.0 + 0.3, lambda s: .30, .30, 1.0),
]
CORG = {"rice": .35}          # PAU Prali Char 30-36% C; others assumed 0.50 (to be measured under ICM)
CORG_OTHER = .50

prod = pd.read_csv(HERE / "production_state_crop_avg_2022-25.csv").set_index("State")
rows = []
for s in prod.index:
    for key, lab, short, col, rpr, sf, y, w in COEF:
        p = float(prod.at[s, col])
        gen = p * rpr                       # lakh t residue
        sur = gen * sf(s)
        bc = sur * y
        rows.append(dict(state=s, crop=key, label=lab, production_lakh=p, residue_kt=gen * 100, surplus_kt=sur * 100,
                         biochar_kt=bc * 100, weight=w, eligible_kt=bc * 100 * w,
                         co2e_kt=bc * 100 * w * CORG.get(key, CORG_OTHER) * 44 / 12))
R = pd.DataFrame(rows)
R.to_csv(HERE / "residue_biochar_state_crop.csv", index=False, float_format="%.2f")
nat = R.groupby("crop")[["residue_kt", "surplus_kt", "biochar_kt", "eligible_kt", "co2e_kt"]].sum()
SURPLUS_MT = nat.surplus_kt.sum() / 1000
assert 178 <= SURPLUS_MT <= 230, SURPLUS_MT       # published national surplus estimates span 178-230 Mt
print(f"national: residue {nat.residue_kt.sum()/1000:.0f} Mt, surplus {SURPLUS_MT:.0f} Mt, biochar {nat.biochar_kt.sum()/1000:.1f} Mt,"
      f" eligible {nat.eligible_kt.sum()/1000:.1f} Mt, CO2e {nat.co2e_kt.sum()/1000:.1f} Mt")

# --- Soil need ------------------------------------------------------------------------------------------------
# Soil Nutrient Index 2023-24 (EnviStats India 2024, Table 4.3; 1 = every sample low, 3 = every sample high).
# The PDF's column order was recovered against Table 4.4: N, P, K, Cu, B, S, Fe, Zn, Mn, OC.
OC_SNI = {"Andhra Pradesh": 1.41, "Assam": 1.85, "Bihar": 1.68, "Chhattisgarh": 1.49, "Gujarat": 1.67, "Haryana": 1.23,
          "Jharkhand": 1.63, "Karnataka": 1.52, "Madhya Pradesh": 1.73, "Maharashtra": 1.46, "Odisha": 1.57,
          "Punjab": 1.63, "Rajasthan": 1.18, "Tamil Nadu": 1.12, "Uttarakhand": 1.79, "Uttar Pradesh": 1.13,
          "West Bengal": 1.73}
K_SNI = {"Andhra Pradesh": 2.71, "Assam": 2.20, "Bihar": 2.64, "Chhattisgarh": 2.69, "Gujarat": 2.82, "Haryana": 2.28,
         "Jharkhand": 2.22, "Karnataka": 2.52, "Madhya Pradesh": 2.65, "Maharashtra": 2.80, "Odisha": 2.39,
         "Punjab": 1.66, "Rajasthan": 2.79, "Tamil Nadu": 2.61, "Uttarakhand": 2.32, "Uttar Pradesh": 2.37,
         "West Bengal": 2.44}
IMPUTED = {"Telangana": "organic-carbon and potassium indices: not in EnviStats table; Andhra Pradesh's used"}
OC_SNI["Telangana"], K_SNI["Telangana"] = OC_SNI["Andhra Pradesh"], K_SNI["Andhra Pradesh"]
# Acid soils, % of geographical area (ICAR-IISS, Acid Soils of India, 2025, Table 1)
ACID = {"Andhra Pradesh": 10.11, "Assam": 100, "Bihar": 12.30, "Chhattisgarh": 80.93, "Gujarat": 0.30, "Haryana": 0.0,
        "Jharkhand": 91.90, "Karnataka": 26.26, "Madhya Pradesh": 20.44, "Maharashtra": 14.52, "Odisha": 95.83,
        "Punjab": 0.14, "Rajasthan": 0.0, "Tamil Nadu": 14.50, "Telangana": 2.90, "Uttar Pradesh": 4.32,
        "Uttarakhand": 58.60, "West Bengal": 81.67}
# NPK use, kg/ha gross cropped area, 2023-24 (FAI)
FERT = {"Punjab": 247.6, "Bihar": 241.1, "Andhra Pradesh": 235.0, "Telangana": 220.0, "Haryana": 218.9,
        "Uttar Pradesh": 189.4, "Tamil Nadu": 168.3, "Uttarakhand": 151.0, "Chhattisgarh": 144.7, "West Bengal": 140.7,
        "Karnataka": 131.9, "Gujarat": 127.4, "Odisha": 120.5, "Jharkhand": 117.9, "Maharashtra": 113.4,
        "Madhya Pradesh": 101.6, "Assam": 69.5, "Rajasthan": 69.3}
# N:P:K use ratio 2024-25 (Rajya Sabha USQ 3541; K = 1). Missing states take the all-India 9.3:3.5:1 (flagged).
NPK = {"Rajasthan": (45.7, 15.0), "Jharkhand": (37.3, 11.0), "Punjab": (29.8, 6.5), "Haryana": (29.2, 7.3),
       "Uttar Pradesh": (22.7, 6.7), "Madhya Pradesh": (15.3, 6.8), "Gujarat": (14.7, 4.6), "Telangana": (12.6, 4.8),
       "Bihar": (11.0, 3.3), "Odisha": (8.3, 3.9), "Andhra Pradesh": (6.1, 3.2), "Tamil Nadu": (4.9, 2.0),
       "Karnataka": (4.8, 2.4), "Maharashtra": (4.2, 2.5), "West Bengal": (2.7, 1.5)}
NPK_NAT = (9.3, 3.5)
for s in ("Chhattisgarh", "Assam", "Uttarakhand"):
    IMPUTED[s] = "N:P:K ratio: not in the Parliament answer; all-India 9.3:3.5:1 used"

oc_vals = [OC_SNI[s] for s in STATES]
OC_MAX, OC_MIN = max(oc_vals), min(oc_vals)
FERT_MAX = max(FERT.values())
NK_MAX = max(n for n, _ in NPK.values())


def soil(s):
    n, p = NPK.get(s, NPK_NAT)
    oc = (OC_MAX - OC_SNI[s]) / (OC_MAX - OC_MIN)
    acid = ACID[s] / 100
    fert = FERT[s] / FERT_MAX
    imb = min(max(math.log(n / 4) / math.log(NK_MAX / 4), 0), 1)    # 4:2:1 is the textbook target
    return dict(state=s, oc_sni=OC_SNI[s], k_sni=K_SNI[s], acid_pct=ACID[s], fert_kgha=FERT[s], n_to_k=n, p_to_k=p,
                oc_need=oc, acid_need=acid, fert_need=fert, imbalance=imb,
                soil_need=.40 * oc + .30 * acid + .15 * fert + .15 * imb)


S = pd.DataFrame([soil(s) for s in STATES]).set_index("state")
S.to_csv(HERE / "soil_need_state.csv", float_format="%.3f")

# --- Openness -------------------------------------------------------------------------------------------------
O = pd.read_csv(HERE / "openness_signals.csv").set_index("state")


def openness(s):
    if s not in O.index:
        return 0.0
    r = O.loc[s]
    proj = min(r.crop_residue_carbon_projects + .5 * r.other_feedstock_carbon_projects, 2) / 2
    return .30 * min(r.icar_kvk_items_2022_26, 4) / 4 + .30 * proj + .20 * r.policy_support + .20 * r.farmer_uptake_evidence


S["openness"] = [openness(s) for s in STATES]
S["fires_2025"] = [O.at[s, "fires_2025"] if s in O.index else float("nan") for s in STATES]

# --- Likelihood index -----------------------------------------------------------------------------------------
MIN_KT = 10.0
E = R[R.state.isin(STATES)].copy()
EMAX = E.eligible_kt.max()


def fscore(kt):
    return 0.0 if kt < MIN_KT else min(math.log10(kt / MIN_KT) / math.log10(EMAX / MIN_KT), 1.0)


E["F"] = E.eligible_kt.map(fscore)
E["S"] = E.state.map(S.soil_need)
E["O"] = E.state.map(S.openness)
WEIGHTS = {"base (45/30/25)": (.45, .30, .25), "equal (33/33/33)": (1 / 3, 1 / 3, 1 / 3),
           "feedstock-heavy (60/20/20)": (.60, .20, .20), "soil-heavy (30/50/20)": (.30, .50, .20),
           "openness-heavy (30/20/50)": (.30, .20, .50), "no openness (60/40/0)": (.60, .40, 0)}
for name, (a, b, c) in WEIGHTS.items():
    E[name] = 100 * (a * E.F + b * E.S + c * E.O)
E["index"] = E["base (45/30/25)"]
L = E[E.eligible_kt >= MIN_KT].sort_values("index", ascending=False).reset_index(drop=True)
L.to_csv(HERE / "likelihood_state_crop.csv", index=False, float_format="%.3f")

base_rank = L["index"].rank(ascending=False)
base_top10 = set(L.head(10).index)
sens = []
for name in WEIGHTS:
    rk = L[name].rank(ascending=False)
    top = set(L[name].nlargest(10).index)
    rho = base_rank.corr(rk, method="pearson")      # Pearson on ranks = Spearman
    sens.append(dict(weights=name, spearman=round(rho, 3), top10_kept=len(top & base_top10),
                     leader=f"{L.loc[L[name].idxmax(), 'label']}, {L.loc[L[name].idxmax(), 'state']}"))
SENS = pd.DataFrame(sens)
SENS.to_csv(HERE / "sensitivity.csv", index=False)
always_top10 = [i for i in L.head(10).index if all(i in set(L[w].nlargest(10).index) for w in WEIGHTS)]
print(SENS.to_string(index=False))

# --- Crop growth and nutrient removal (2003-06 vs 2022-25) ---------------------------------------------------
# FAO Fertilizer and Plant Nutrition Bulletin 16, Table 29 (Tandon): kg N, P2O5, K2O removed per tonne of produce.
REMOVAL = {"Rice": (20, 11, 30, 1.5), "Wheat": (25, 9, 33, 1), "Maize": (29.9, 13.5, 32.8, 1),
           "Gram": (60.7, 9.2, 39.2, 1), "Soybean": (70.7, 30.9, 57.7, 1), "Rapeseed & Mustard": (64.5, 20.6, 53.4, 1)}
I = pd.read_csv(HERE / "intensification_state_crop_2003-06_to_2022-25.csv")
I["State"] = I.State.replace({"Telangana": "Andhra Pradesh"})   # AP before 2014 includes Telangana
I = I[I.Crop.isin(REMOVAL)].groupby(["State", "Crop"])[["prod_0", "prod_1", "area_0", "area_1"]].sum().reset_index()
nr = []
for st, g in I.groupby("State"):
    rec = dict(state=st)
    for t in (0, 1):
        tot = k = 0.0
        for _, r in g.iterrows():
            n, p, kk, mult = REMOVAL[r.Crop]
            q = r[f"prod_{t}"] * mult            # lakh t (paddy for rice)
            tot += q * (n + p + kk) * .1         # kt
            k += q * kk * .1
        area = g[f"area_{t}"].sum()              # lakh ha
        rec[f"npk_kt_{t}"], rec[f"k_kt_{t}"], rec[f"area_{t}"] = tot, k, area
    rec["npk_chg"] = rec["npk_kt_1"] / rec["npk_kt_0"] - 1 if rec["npk_kt_0"] else float("nan")
    rec["k_removed_kgha"] = rec["k_kt_1"] * 1e3 / (rec["area_1"] * 1e5) * 1e3 if rec["area_1"] else float("nan")
    nr.append(rec)
NR = pd.DataFrame(nr).set_index("state")
STATES_NR = [s for s in STATES if s != "Telangana"]
NR = NR.loc[STATES_NR]
fk = {s: FERT[s] / (sum(NPK.get(s, NPK_NAT)) + 1) for s in STATES}
fk["Andhra Pradesh"] = (FERT["Andhra Pradesh"] / (sum(NPK["Andhra Pradesh"]) + 1)
                        + FERT["Telangana"] / (sum(NPK["Telangana"]) + 1)) / 2   # simple mean of the two states
NR["k_applied_kgha"] = [fk[s] for s in STATES_NR]
NR["oc_sni"] = [OC_SNI[s] for s in STATES_NR]
NR.to_csv(HERE / "nutrient_removal_state.csv", float_format="%.2f")
rho_fert_oc = pd.Series([FERT[s] for s in STATES]).rank().corr(pd.Series([OC_SNI[s] for s in STATES]).rank())
rho_growth_oc = NR.npk_chg.rank().corr(NR.oc_sni.rank())
print(f"Spearman fert kg/ha vs OC index: {rho_fert_oc:.2f}; removal growth vs OC index: {rho_growth_oc:.2f}")

# --- Districts: state model x district share of state production (2022-23 to 2024-25) ------------------------
D = pd.read_csv(DISTRICT_FILE)
D = D[(D.Metric == "Production") & (D.Season == "Total") & (D["Crop Year Code"] >= 2022)]
cols = {c[3]: c[0] for c in COEF}
D = D[D.Crop.isin(cols)].groupby(["State", "District", "Crop"]).Value.mean().reset_index()
D["share"] = D.Value / D.groupby(["State", "Crop"]).Value.transform("sum")
D["crop"] = D.Crop.map(cols)
D = D.merge(R[["state", "crop", "eligible_kt"]], left_on=["State", "crop"], right_on=["state", "crop"])
D["district_kt"] = (D.share * D.eligible_kt).fillna(0)
D = D[D.district_kt > 0]
DT = D.groupby(["State", "District"]).district_kt.sum().reset_index()
lead = D.loc[D.groupby(["State", "District"]).district_kt.idxmax(), ["State", "District", "crop"]]
DT = DT.merge(lead, on=["State", "District"]).sort_values("district_kt", ascending=False)
DT["lead"] = DT.crop.map({c[0]: c[1] for c in COEF})
lead_share = D.groupby(["State", "District"]).district_kt.max() / D.groupby(["State", "District"]).district_kt.sum()
DT["lead_share"] = [lead_share[(a, b)] for a, b in zip(DT.State, DT.District)]
DT.head(30).to_csv(HERE / "districts_top.csv", index=False, float_format="%.2f")

out = dict(
    surplus_mt=SURPLUS_MT, residue_mt=nat.residue_kt.sum() / 1000, biochar_mt=nat.biochar_kt.sum() / 1000,
    eligible_mt=nat.eligible_kt.sum() / 1000, co2e_mt=nat.co2e_kt.sum() / 1000,
    by_crop=nat.reset_index().to_dict("records"),
    feed={f"{r.state}|{r.crop}": r.eligible_kt for r in E.itertuples()},
    soil=S.reset_index().to_dict("records"), imputed=IMPUTED,
    likelihood=L[["state", "crop", "label", "eligible_kt", "F", "S", "O", "index"] + list(WEIGHTS)].to_dict("records"),
    sensitivity=sens, always_top10=[f"{L.at[i, 'label']}, {L.at[i, 'state']}" for i in always_top10],
    removal=NR.reset_index().to_dict("records"), rho_fert_oc=rho_fert_oc, rho_growth_oc=rho_growth_oc,
    districts=DT.head(30).to_dict("records"), coef=[(c[0], c[1], c[2], c[4], c[6], c[7]) for c in COEF],
    states=STATES, min_kt=MIN_KT, weights=WEIGHTS)
(HERE / "results.json").write_text(json.dumps(out, indent=1, default=float))
print("top 15:")
print(L.head(15)[["label", "state", "eligible_kt", "F", "S", "O", "index"]].to_string())
print(S[["oc_sni", "acid_pct", "fert_kgha", "n_to_k", "soil_need", "openness", "fires_2025"]].sort_values("soil_need", ascending=False).to_string())
print(DT.head(15).to_string())
print(NR[["npk_kt_0", "npk_kt_1", "npk_chg", "k_removed_kgha", "k_applied_kgha", "oc_sni"]].sort_values("npk_chg").to_string())

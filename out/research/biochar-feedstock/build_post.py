"""Biochar heatmap post. Run model.py first (with /usr/bin/python3), then from the repo root:
    python3 out/research/biochar-feedstock/build_post.py
Reads results.json; every number in the text comes from it or from a constant below with its source."""
import json, math, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build

HERE = pathlib.Path(__file__).resolve().parent
R = json.load(open(HERE / "results.json"))
OUT = ROOT / "out/post-biochar-crop-residue-heatmap-india.html"
STATES = R["states"]
COEF = R["coef"]                     # key, label, short, residue factor, biochar yield, weight
CROPS = [c[0] for c in COEF]
SHORT = {c[0]: c[2] for c in COEF}
LABEL = {c[0]: c[1] for c in COEF}
SOIL = {d["state"]: d for d in R["soil"]}
LIK = R["likelihood"]
LK = {(d["state"], d["crop"]): d for d in LIK}
BYC = {d["crop"]: d for d in R["by_crop"]}
ABBR = {"Uttar Pradesh": "UP", "West Bengal": "W. Bengal", "Madhya Pradesh": "MP", "Andhra Pradesh": "Andhra P.",
        "Chhattisgarh": "Chhattisgarh", "Uttarakhand": "Uttarakhand", "Maharashtra": "Maharashtra", "Tamil Nadu": "Tamil Nadu"}

# ---- figures from sources (not computed) ----
SHC_LOW_OC = 47.7          # % of 8.9 million SHC 2024-25 samples below 0.5% OC (Rajya Sabha USQ 2258, 7 Aug 2025)
ACID_NAT = 31              # % of India's area under acid soils (ICAR-IISS 2025)
FIRES_TOTAL, FIRES_MP = 33028, 17067   # 15 Sep-30 Nov 2025, six states (ICAR CREAMS via New Indian Express)
CEEW_CREDITS = 114         # thousand Indian biochar credits issued (CEEW)
PLATTS = 135               # $/t CO2e, biochar removal credits (S&P Global Platts)

f1 = lambda x: f"{x:,.1f}"
f0 = lambda x: f"{x:,.0f}"


def lakh(kt): return kt / 100


def tw(head, rows, note=""):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    n = f'<p class="gb-note">{note}</p>' if note else ""
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>{n}'


LO, HI = (238, 243, 248), (11, 61, 107)    # light to #0b3d6b


def colour(t):
    t = min(max(t, 0), 1)
    c = tuple(round(LO[i] + (HI[i] - LO[i]) * t) for i in range(3))
    return "#%02x%02x%02x" % c, ("#fff" if t > .5 else "#212529")


def heat(title, sub, rows, cols, cell, source, aria, legend=("low", "high"), L=78):
    """cell(r, c) -> (t in 0..1 or None, label)."""
    W = 340
    cw = (W - L - 4) / len(cols)
    ch, top = 17, 74
    H = top + len(rows) * ch + 44
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="{aria}">',
         f'<text x="4" y="13" font-size="12.5" fill="#495057">{title}</text>',
         f'<text x="4" y="28" font-size="10" fill="#6c757d">{sub}</text>']
    for j, c in enumerate(cols):
        x = L + j * cw + cw / 2
        s.append(f'<text x="{x:.1f}" y="{top - 6}" font-size="9" fill="#212529" text-anchor="start" '
                 f'transform="rotate(-50 {x:.1f} {top - 6})">{c[1]}</text>')
    for i, r in enumerate(rows):
        y = top + i * ch
        s.append(f'<text x="{L - 4}" y="{y + ch / 2 + 3.5:.1f}" font-size="9.5" fill="#212529" text-anchor="end">{r[1]}</text>')
        for j, c in enumerate(cols):
            t, lab = cell(r[0], c[0])
            x = L + j * cw
            if t is None:
                s.append(f'<rect x="{x + .5:.1f}" y="{y + .5}" width="{cw - 1:.1f}" height="{ch - 1}" fill="#f8f9fa"/>')
                continue
            bg, fg = colour(t)
            s.append(f'<rect x="{x + .5:.1f}" y="{y + .5}" width="{cw - 1:.1f}" height="{ch - 1}" fill="{bg}"/>')
            if lab:
                s.append(f'<text x="{x + cw / 2:.1f}" y="{y + ch / 2 + 3:.1f}" font-size="8" fill="{fg}" text-anchor="middle">{lab}</text>')
    ly = top + len(rows) * ch + 10
    for k in range(10):
        bg, _ = colour(k / 9)
        s.append(f'<rect x="{L + k * 12}" y="{ly}" width="12" height="7" fill="{bg}"/>')
    s.append(f'<text x="{L - 4}" y="{ly + 7}" font-size="8.5" fill="#6c757d" text-anchor="end">{legend[0]}</text>')
    s.append(f'<text x="{L + 124}" y="{ly + 7}" font-size="8.5" fill="#6c757d">{legend[1]}</text>')
    s.append(f'<text x="4" y="{H - 8}" font-size="9" fill="#6c757d">{source}</text>')
    s.append("</svg>")
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + "</figure>"


ROWS = [(s, ABBR.get(s, s)) for s in STATES]
COLS = [(c, SHORT[c]) for c in CROPS]

# Figure 1: eligible biochar, lakh t/yr, log colour
emax = max(R["feed"].values())


def fcell(s, c):
    kt = R["feed"][f"{s}|{c}"]
    if kt < R["min_kt"]:
        return None, ""
    v = lakh(kt)
    return math.log10(kt / R["min_kt"]) / math.log10(emax / R["min_kt"]), (f"{v:.0f}" if v >= 9.95 else f"{v:.1f}")


FIG1 = heat("Biochar the spare residue could make, lakh tonnes a year",
            "Surplus after fodder, fuel and other uses; bagasse at half weight; blank under 0.1",
            ROWS, COLS, fcell, "Model on UPAg 2022-25 harvests; ratios in the text",
            "Heatmap of eligible biochar by state and crop residue", legend=("0.1", f"{lakh(emax):.0f} (log scale)"))

# Figure 2: soil need components, coloured by each column's need score
SCOLS = [("oc", "OC index"), ("acid", "Acid %"), ("fert", "NPK/ha"), ("nk", "N per K"), ("need", "Need")]


def scell(s, k):
    d = SOIL[s]
    star = "*" if s in R["imputed"] and ((k in ("oc",) and s == "Telangana") or (k == "nk" and s != "Telangana")) else ""
    if k == "oc": return d["oc_need"], f'{d["oc_sni"]:.2f}{star}'
    if k == "acid": return d["acid_need"], f'{d["acid_pct"]:.0f}'
    if k == "fert": return d["fert_need"], f'{d["fert_kgha"]:.0f}'
    if k == "nk": return d["imbalance"], f'{d["n_to_k"]:.1f}{star}'
    return d["soil_need"], f'{100 * d["soil_need"]:.0f}'


SROWS = sorted(ROWS, key=lambda r: -SOIL[r[0]]["soil_need"])
FIG2 = heat("Where the soil needs carbon most",
            "Darker = more need. OC index: 1 = all samples low, 3 = all high",
            SROWS, SCOLS, scell, "EnviStats 2024, ICAR-IISS, FAI, RS Q 3541. * imputed",
            "Heatmap of soil-need components by state", L=78)

# Figure 3: likelihood index
lvals = [d["index"] for d in LIK]
IMIN, IMAX = min(lvals), max(lvals)


def lcell(s, c):
    d = LK.get((s, c))
    if not d:
        return None, ""
    return (d["index"] - IMIN) / (IMAX - IMIN), f'{d["index"]:.0f}'


LROWS = sorted(ROWS, key=lambda r: -max([LK[(r[0], c)]["index"] for c in CROPS if (r[0], c) in LK] or [0]))
FIG3 = heat("Biochar likelihood index, 0 to 100",
            "45% feedstock, 30% soil need, 25% openness; blank = under 0.1 lakh t of char",
            LROWS, COLS, lcell, "Model output; weights tested in the sensitivity table",
            "Heatmap of the biochar likelihood index by state and crop residue", legend=(f"{IMIN:.0f}", f"{IMAX:.0f}"))

# ---- numbers for the text ----
TOP = LIK[:15]
top1, top2, top3 = LIK[0], LIK[1], LIK[2]
SENS = R["sensitivity"]
nat_surplus, nat_bc, nat_el, nat_co2 = R["surplus_mt"], R["biochar_mt"], R["eligible_mt"], R["co2e_mt"]
pun = LK[("Punjab", "rice")]
rice_share = BYC["rice"]["eligible_kt"] / sum(d["eligible_kt"] for d in R["by_crop"])
REM = {d["state"]: d for d in R["removal"]}
mp, mh, bi = REM["Madhya Pradesh"], REM["Maharashtra"], REM["Bihar"]
pb_rem = REM["Punjab"]
kgap = sorted(R["removal"], key=lambda d: -(d["k_removed_kgha"] - d["k_applied_kgha"]))
zero_open = [s for s in STATES if SOIL[s]["openness"] == 0]
hi_need_zero = [s for s in sorted(STATES, key=lambda s: -SOIL[s]["soil_need"]) if SOIL[s]["openness"] == 0][:3]
assert hi_need_zero[:2] == ["Jharkhand", "Chhattisgarh"], hi_need_zero
assert [d["state"] for d in LIK[:2]] == ["Punjab", "Odisha"]
assert R["always_top10"] == ["Rice straw, Odisha", "Cotton stalk, Maharashtra"]
no_open = next(d for d in SENS if d["weights"].startswith("no openness"))

STATS = f'''<div class="gb-stats">
<div class="gb-stat"><b>{nat_surplus:.0f} Mt</b><span>Crop residue left over each year after fodder, fuel and other uses, across ten crops (model, 2022-25 harvests)</span></div>
<div class="gb-stat"><b>{nat_el:.0f} Mt</b><span>Biochar that surplus could make each year, counting bagasse at half because mills already burn it</span></div>
<div class="gb-stat"><b>{SHC_LOW_OC}%</b><span>Soil Health Card samples in 2024-25 with organic carbon below 0.5%</span></div>
<div class="gb-stat"><b>2 of 119</b><span>Crop&ndash;state pairs that stay in the top ten under all six weightings tested: Odisha&rsquo;s rice straw and Maharashtra&rsquo;s cotton stalk</span></div>
</div>
'''

by_crop_rows = []
for c in sorted(CROPS, key=lambda c: -BYC[c]["eligible_kt"]):
    d = BYC[c]
    co = [x for x in COEF if x[0] == c][0]
    by_crop_rows.append([LABEL[c], f0(d["residue_kt"] / 1000), f0(d["surplus_kt"] / 1000), f"{co[4] * 100:.0f}%",
                         f1(d["eligible_kt"] / 1000), "half" if co[5] < 1 else "full"])
by_crop_rows.append(["<b>Total</b>", f"<b>{R['residue_mt']:.0f}</b>", f"<b>{nat_surplus:.0f}</b>", "",
                     f"<b>{nat_el:.1f}</b>", ""])
T_CROP = tw(["Residue", "Generated, Mt", "Surplus, Mt", "Char yield", "Eligible char, Mt", "ICM weight"], by_crop_rows,
            "Surplus is what is left after fodder, bedding, domestic fuel and industrial uses. Rice straw uses state surplus fractions; "
            "wheat straw too in Punjab and Haryana; every other crop uses one national fraction.")

rem_rows = []
for s in sorted(REM, key=lambda s: -REM[s]["npk_chg"]):
    d = REM[s]
    name = "Andhra P. + Telangana" if s == "Andhra Pradesh" else s
    rem_rows.append([name, f0(d["npk_kt_0"]), f0(d["npk_kt_1"]), f"{100 * d['npk_chg']:+.0f}%",
                     f0(d["k_removed_kgha"]), f0(d["k_applied_kgha"]), f"{d['oc_sni']:.2f}"])
T_REM = tw(["State", "N+P+K removed, kt, 2003-06", "2022-25", "Change", "K₂O removed, kg/ha", "K₂O applied, kg/ha", "Organic C index"],
           rem_rows, "Removal by rice, wheat, maize, gram, soybean and mustard: production times FAO removal coefficients, which count the straw. "
           "Removed per hectare of those six crops; applied per hectare of all cropped land (FAI, 2023-24). "
           "Andhra Pradesh is combined with Telangana because the 2003-06 data predate the split; its applied figure is the two states&rsquo; average.")

open_rows = []
OPEN_NOTE = {
    "Madhya Pradesh": "IISS rice trial; CIAE training; in the 962-household study", "Maharashtra": "CICR and CIRCOT on cotton stalk; Varaha, Green Carbon (Nagpur)",
    "Gujarat": "Navsari Agricultural University unit, 2 KVKs; Green Carbon (Kapadvanj)", "Odisha": "Carboneers, LongStraw; state lists biochar under climate-smart farming",
    "Punjab": "PAU Prali Char in the kharif 2026 Package of Practices", "Karnataka": "UAS Bengaluru training; Equilibrium (Mundargi), MASH Makes",
    "Assam": "IARI arsenic trials; Carboneers paddy-straw plant in validation", "West Bengal": "IARI arsenic trials; Green Carbon (planned)",
    "Uttar Pradesh": "Crop-residue machine subsidy only", "Haryana": "Non-burning incentive Rs 1,000-1,200/acre; no biochar line",
    "Rajasthan": "Two projects, both on Prosopis, not crop residue", "Telangana": "CRIDA drum kiln (2018)"}
for s in sorted(STATES, key=lambda s: -SOIL[s]["openness"]):
    d = SOIL[s]
    fires = "" if d["fires_2025"] != d["fires_2025"] else f0(d["fires_2025"])
    open_rows.append([s, f"{100 * d['openness']:.0f}", fires or "not tracked", OPEN_NOTE.get(s, "None found")])
T_OPEN = tw(["State", "Openness, 0-100", "Farm fires, 2025 season", "What was found"], open_rows,
            "Openness: 30% ICAR and KVK biochar work since 2022 (up to four items), 30% carbon projects on crop residue (projects on other feedstock count half), "
            "20% state policy that names biochar or pays for residue use, 20% evidence of farmers using it. Fires: 15 September to 30 November 2025, "
            "satellite counts by ICAR&rsquo;s CREAMS, which tracks only these six states.")

top_rows = [[d["label"], d["state"], f1(lakh(d["eligible_kt"])), f"{100 * d['F']:.0f}", f"{100 * d['S']:.0f}", f"{100 * d['O']:.0f}", f"<b>{d['index']:.0f}</b>"]
            for i, d in enumerate(TOP)]
T_TOP = tw(["Residue", "State", "Char, lakh t", "Feedstock", "Soil need", "Openness", "Index"], top_rows)
sens_rows = [[d["weights"], f"{d['spearman']:.2f}", f"{d['top10_kept']} of 10", d["leader"]] for d in SENS]
T_SENS = tw(["Weights (feedstock / soil / openness)", "Rank correlation with base", "Base top ten kept", "Leader"], sens_rows)
dist_rows = [[d["District"], d["State"], f1(lakh(d["district_kt"])), d["lead"], f"{100 * d['lead_share']:.0f}%"]
             for i, d in enumerate(R["districts"][:15])]
T_DIST = tw(["District", "State", "Char, lakh t", "Main residue", "Its share"], dist_rows,
            "Each state&rsquo;s modelled char for a crop is split across its districts by their share of the state&rsquo;s production, averaged over 2022-23 to 2024-25. "
            "District surplus fractions do not exist, so a district inherits its state&rsquo;s.")

body = STATS + f'''
<p>India grows more crop than ever, and its soils are running short of organic carbon. Biochar, crop waste charred slowly in little or no air and ploughed back in, is the one remedy that could address both and earn carbon credits as well. The question is where it would actually take hold. This piece models ten crop residues across eighteen states. It asks how much spare residue each pairing leaves, how badly the soil there needs carbon, and whether anyone locally is already making, testing or buying biochar.</p>

<p>The short answer is that it depends on what you value most. Punjab&rsquo;s rice straw is the biggest single feedstock by a wide margin: about {lakh(pun["eligible_kt"]):.0f} lakh tonnes of char a year if all of its spare straw were charred. Punjab tops the index on the base weights, but its soils are not the most depleted, and almost nothing is being done with biochar there beyond the agricultural university&rsquo;s own kiln design. Only two pairings stay in the top ten under every set of weights tried: <b>rice straw in Odisha</b>, where soils are acid and carbon developers are already working with farmers, and <b>cotton stalk in Maharashtra</b>, where ICAR&rsquo;s cotton institutes and two credit developers are active.</p>

<h2 class="gb-h2" id="growth">Bigger harvests are taking more out of the soil</h2>
<p>Between 2003-06 and 2022-25, the nutrients carried off in harvests of six major crops rose fastest in Maharashtra (+{100 * mh["npk_chg"]:.0f}%), Madhya Pradesh (+{100 * mp["npk_chg"]:.0f}%) and Bihar (+{100 * bi["npk_chg"]:.0f}%). These are rough estimates: tonnes harvested multiplied by FAO&rsquo;s per-tonne coefficients for nitrogen, phosphate and potash, which count the straw as well as the grain. Punjab&rsquo;s rose a more modest {100 * pb_rem["npk_chg"]:.0f}% from an already high base.</p>
{T_REM}
<p>The table shows a gap far larger than any other: potash. Rice and wheat take up more potassium than nitrogen, and most of it sits in the straw. In Punjab, the six crops remove about {pb_rem["k_removed_kgha"]:.0f} kg of K&#8322;O a hectare, while farmers apply about {pb_rem["k_applied_kgha"]:.0f} kg per hectare of cropped land, because Punjab&rsquo;s fertiliser is nearly all urea: 29.8 parts nitrogen to one of potash in 2024-25. The two figures use different hectares, so the gap is indicative, not exact. When straw is burned, the National Policy for Management of Crop Residues counts the loss from each tonne at 5.5 kg of nitrogen, 2.3 kg of phosphorus, 25 kg of potassium, 1.2 kg of sulphur and about 400 kg of organic carbon. Biochar keeps part of that carbon in the field for decades. Potassium does not burn off at kiln temperatures the way nitrogen does, so char that goes back to the field returns much of it too.</p>
<p>The link between harvest growth and low soil carbon is weaker than the story suggests. Across the eighteen states, the rank correlation between fertiliser use per hectare and the organic-carbon index is only {R["rho_fert_oc"]:.2f}. Between growth in nutrient removal and the index it is {R["rho_growth_oc"]:.2f}, close to nothing. The states with the least soil carbon are Tamil Nadu, Uttar Pradesh, Rajasthan and Haryana, long-farmed plains and dry lands where heat burns organic matter off fast, not the states whose harvests grew fastest. Soil carbon reflects decades of climate and practice. A decade of harvest growth barely shows in it.</p>

<h2 class="gb-h2" id="feedstock">Where the spare residue is</h2>
<p>The feedstock model takes the average harvest of 2022-23 to 2024-25 from the Ministry of Agriculture&rsquo;s UPAg data. It multiplies each crop by a residue-to-product ratio: 1.5 tonnes of straw per tonne of milled rice; 1.5 for wheat; 2.3 for maize stalk and cob; 3.8 tonnes of stalk per tonne of seed cotton; 0.33 tonnes of bagasse per tonne of cane; and 1.1 to 2.5 for pulses and oilseeds. It then keeps only the surplus. For rice, that is the state share in the MNRE biomass atlas: 99% in Punjab, where almost no straw is fed to animals, and under 5% in Uttar Pradesh, West Bengal, Gujarat and Maharashtra, where most of it is. Other crops take TIFAC&rsquo;s national surplus fractions. Char yields are 26% to 35% of dry weight, depending on the residue.</p>
<p>The national surplus comes to {nat_surplus:.0f} million tonnes a year, within the 178&ndash;230 Mt range of published estimates. Charred, it would make about {nat_bc:.0f} Mt of biochar, or {nat_el:.0f} Mt counting bagasse at half. Rice straw is {100 * rice_share:.0f}% of that, and {100 * pun['eligible_kt'] / BYC['rice']['eligible_kt']:.0f}% of the rice-straw char is in Punjab.</p>
{FIG1}
{T_CROP}

<h2 class="gb-h2" id="rules">What the carbon-market rules allow</h2>
<p>India&rsquo;s draft offset methodology for biochar under the Carbon Credit Trading Scheme (BM AG04, &ldquo;Production and Use of Biochar&rdquo;) accepts in-field crop residue such as cereal straw, maize straw, stalks and prunings. It also accepts processing residue: rice husk, maize cob, nutshell, bagasse and spent grain. It excludes food crops grown as feedstock and mixed municipal waste. Production must reach a hydrogen-to-organic-carbon ratio below 0.7, and the credit is the tonnes of char times its organic-carbon share times 44/12. The methodology is a draft and is not yet among the scheme&rsquo;s approved methodologies.</p>
<p>The rule that matters most for this map is leakage. Residue that something else already uses, such as bagasse in a sugar mill&rsquo;s boiler, has to show that diverting it does not push that user onto fossil fuel. Residue that was previously left to rot or burned does not. That is why bagasse counts at half weight here: the mills already burn it. The European Biochar Certificate&rsquo;s positive list (version 10.1) is broader still: &ldquo;harvest residues such as straw, cabbage, leaves, stalks, husks&rdquo; are allowed in every certificate class, with a caution on pesticide and heavy-metal residues. So every residue in the model qualifies under both systems; the only question is how much of it is spare.</p>
<p>At an assumed 35% organic carbon for rice-straw char (PAU measured 30&ndash;36%) and 50% for the rest, the eligible char would store about {nat_co2:.0f} million tonnes of CO&#8322; a year before any project, permanence or leakage deductions. That is a ceiling, not a forecast. CEEW counts about {CEEW_CREDITS},000 Indian biochar credits issued so far, and Platts assessed removal credits at about ${PLATTS} a tonne.</p>

<h2 class="gb-h2" id="soil">Where the soil needs it</h2>
<p>The soil-need score weights four things:</p>
<ul>
<li><b>Organic-carbon index, 40%.</b> The 2023-24 Soil Health Card index for organic carbon, from MoSPI&rsquo;s EnviStats 2024. It runs from 1 if every sample tested low to 3 if every sample tested high.</li>
<li><b>Acid soils, 30%.</b> Their share of each state&rsquo;s area, from ICAR&rsquo;s 2025 survey. Biochar&rsquo;s liming effect gives its largest yield gains on acid soils.</li>
<li><b>Fertiliser use per hectare, 15%.</b></li>
<li><b>How lopsided nitrogen use is against potash, 15%.</b></li>
</ul>
<p>The index puts Tamil Nadu (1.12), Uttar Pradesh (1.13) and Rajasthan (1.18) at the bottom. That matches ICRIER&rsquo;s reading of the 2024-25 cards, which found 88% and 87% of samples low in Tamil Nadu and Uttar Pradesh. Odisha, Jharkhand, Chhattisgarh, West Bengal and Assam are mostly acid soil. In Odisha a GIZ project found biochar&rsquo;s largest benefit on acid soils, and a groundnut trial on acid red soil gained 29% in pod yield.</p>
{FIG2}

<h2 class="gb-h2" id="openness">Who is already trying</h2>
<p>There is no national ICAR biochar programme and no biochar line in the Rs 4,549 crore crop-residue scheme, which pays for machinery. The Ministry of Agriculture&rsquo;s 2024 framework for voluntary carbon markets in agriculture does name biochar. Activity is local, and it clusters in central and western India. ICAR&rsquo;s cotton institutes (CICR in Nagpur and CIRCOT in Mumbai) work on cotton-stalk char. In January 2026 Varaha signed an offtake with Microsoft for more than 100,000 tonnes of removals over three years from cotton stalk bought in Vidarbha, to be charred in up to 18 gasification reactors. Green Carbon&rsquo;s project document for two plants near Nagpur plans 6,480 tonnes of cotton-stalk char a year. Punjab Agricultural University added a pyramid kiln, &ldquo;Prali Char&rdquo;, to its kharif 2026 Package of Practices: 12 quintals of straw give 8 quintals of char, and 2 tonnes an acre is credited with saving 16 kg of nitrogen. In a 962-household survey in Madhya Pradesh, Maharashtra and Odisha, farmers using biochar reported paddy yields 4.3% higher and net returns 29% higher.</p>
<p>Fires are the other signal. Residue that is burned is residue nobody else wants. In the 2025 season Madhya Pradesh, not Punjab, had the most farm fires of the six states ICAR tracks: {FIRES_MP:,} of {FIRES_TOTAL:,}, more than half. The model does not add fires to the index, because CREAMS covers only six states and the surplus fractions already count burned straw as spare. They are shown here as a check.</p>
{T_OPEN}
<p>{["No", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"][len(zero_open)]} of the eighteen states score zero. That does not mean nothing is happening there, only that this search found no ICAR or KVK biochar work since 2022, no carbon project on crop residue, and no state policy naming it.</p>

<h2 class="gb-h2" id="index">The likelihood index</h2>
<p>Each crop&ndash;state pair gets an index from 0 to 100: 45% feedstock (eligible char, on a log scale), 30% soil need and 25% openness. Pairs with less than 0.1 lakh tonnes of char a year are left out, which leaves 119. The index ranks pairs; it is not a probability that biochar will be adopted, because no outcome data exist to calibrate it against.</p>
{FIG3}
{T_TOP}
<p>The top of the table is tightly bunched: the first five pairs are within three points of each other. So the weights decide the order, and the table below tests six different sets.</p>
{T_SENS}
<p>The overall ranking holds up: rank correlations with the base stay at 0.82 or above. The leader does not. Weight soil or openness more heavily, or weight all three equally, and Odisha&rsquo;s rice straw leads; weight feedstock more heavily and Punjab&rsquo;s stays first. Drop openness altogether and Uttar Pradesh&rsquo;s bagasse comes first: its surplus is large and its soils are low in carbon, but mills already burn the bagasse. Only {R["always_top10"][0].replace(", ", " in ").lower().replace("odisha", "Odisha")} and {R["always_top10"][1].replace(", ", " in ").lower().replace("maharashtra", "Maharashtra")} stay in the top ten throughout.</p>

<h2 class="gb-h2" id="districts">The districts with the most spare residue</h2>
<p>A kiln draws on residue from 25 kilometres or so, so district totals matter more than state ones. Spread across districts by their share of each crop, the largest totals are in Punjab&rsquo;s paddy belt, then in cane and cotton districts:</p>
{T_DIST}

<h2 class="gb-h2" id="regions">Four kinds of region</h2>
<ul>
<li><b>Punjab and Haryana: the most straw, the least uptake.</b> They hold the largest single feedstock, and Haryana&rsquo;s soils are among the lowest in carbon. Policy money goes to machines and to non-burning bonuses, not to char. PAU&rsquo;s kiln in the Package of Practices is the opening.</li>
<li><b>Maharashtra, Gujarat and Madhya Pradesh: the most ready.</b> Cotton, soybean and wheat stalk, ICAR and KVK work, and three credit developers. Madhya Pradesh had the most farm fires of the six states ICAR tracks in 2025, so much of its straw is plainly uncommitted.</li>
<li><b>The acid belt, Odisha to Assam: the biggest agronomic payoff.</b> Rice straw is modest per state, but acid soils are where trials show the largest gains. Odisha has projects. Jharkhand and Chhattisgarh rank second and fourth of the eighteen for soil need, and this search found no biochar work in either.</li>
<li><b>Uttar Pradesh, Tamil Nadu and Rajasthan: the most depleted soils, the least activity.</b> Uttar Pradesh&rsquo;s cane and wheat residue is large, but almost all its rice straw already has a use, and its bagasse has a buyer in the mills.</li>
</ul>

<h2 class="gb-h2" id="fix">What would fix this</h2>
<ul>
<li><b>Publish the Soil Health Card results as a state and district table</b>, with the share of samples low, medium and high for each nutrient, not only on a dashboard that has to be clicked through state by state. EnviStats&rsquo; index is the only complete state table, and it leaves out Telangana.</li>
<li><b>Finalise the biochar methodology under the Carbon Credit Trading Scheme</b> with default organic-carbon values for common Indian residues, so a small kiln operator does not need a laboratory to estimate credits.</li>
<li><b>Let crop-residue money pay for char, not only machines.</b> A per-tonne payment for straw delivered to a registered kiln would reach states with high soil need that the machinery subsidy does not.</li>
<li><b>Run biochar trials on the acid soils of Jharkhand and Chhattisgarh</b>, where this search found no work since 2022 and the soil case is strongest.</li>
</ul>

<h2 class="gb-h2" id="limits">What this piece could not establish</h2>
<ul>
<li><b>District surplus.</b> Surplus fractions exist by state for rice, and only nationally for other crops; wheat outside Punjab and Haryana uses an assumed 20%. A district&rsquo;s actual surplus can be far from its state&rsquo;s.</li>
<li><b>Sugarcane trash, jute sticks, millets and minor pulses</b> are left out for want of reliable residue ratios or surplus fractions. So is rice husk, most of which already goes to boilers. Including them would raise the totals, chiefly in Uttar Pradesh, Maharashtra and West Bengal.</li>
<li><b>Imputed soil figures.</b> Telangana takes Andhra Pradesh&rsquo;s soil indices. Chhattisgarh, Assam and Uttarakhand take the all-India N:P:K ratio.</li>
<li><b>Char carbon content</b> beyond PAU&rsquo;s rice-straw figure is an assumption. Under the methodology it has to be measured.</li>
<li><b>Openness</b> rests on what a web search could find, so states with work published only in regional languages or internal reports will score too low. Fire counts cover only six states.</li>
<li><b>The index weights are a judgement.</b> The sensitivity table shows which conclusions survive changing them.</li>
</ul>
'''

U = "https://masaladeutsch.blogspot.com/"
SOURCES = (
    '<a href="https://indiancarbonmarket.gov.in/storage/pages/17897215234.pdf">Indian Carbon Market, draft methodology BM AG04, Production and Use of Biochar</a> (eligible feedstocks, leakage, H/C<sub>org</sub>, credit formula); '
    '<a href="https://www.european-biochar.org/media/doc/2/positivlist_en_2022_1_v10_1.pdf">European Biochar Certificate, positive list of permissible biomass, v10.1</a>; '
    'production: UPAg crop estimates, final, state and district, 2022-23 to 2024-25 and 2003-04 to 2005-06, via <a href="https://github.com/herrrickshaw/india-mandi-arrivals">india-mandi-arrivals</a>; '
    'residue ratios: <a href="https://epubs.icar.org.in/index.php/JWR/article/download/123108/48831/345741">Journal of Cereal Research (ICAR), 2022, Table 5</a>; '
    'rice surplus fractions: <a href="https://nibe.res.in/english/biomass-atlas.php">MNRE biomass atlas (NIBE/ASCI)</a>; other crops: TIFAC national fractions as quoted in the literature (the <a href="https://tifac.org.in/images/pdf/pub/TIFACReports/newreports/biomass_w(1).pdf">TIFAC report</a> itself did not load); '
    'soil indices: <a href="https://www.mospi.gov.in/sites/default/files/publication_reports/EnviStats_India_2024.pdf">MoSPI, EnviStats India 2024, Tables 4.3 and 4.4</a> (column order recovered from Table 4.4); '
    '<a href="https://sansad.in/getFile/annex/268/AU2258_b1qr3S.pdf?source=pqars">Rajya Sabha USQ 2258, 7 August 2025</a> (SHC 2024-25 national counts); '
    '<a href="https://icrier.org/pdf/Healing-Soils-in-India.pdf">ICRIER, Healing Soils in India, January 2026</a>; '
    '<a href="https://cdn.cseindia.org/attachments/0.77764700_1770706879_rajeshwari-sinha.pdf">CSE, February 2026</a>; '
    '<a href="https://icar.gov.in/sites/default/files/2026-07/Acid%20Soils%20of%20India.pdf">ICAR-IISS, Acid Soils of India, 2025, Table 1</a>; '
    '<a href="https://www.faidelhi.org/member/AR-Full-Rep.pdf">FAI, fertiliser use per hectare, 2023-24</a>; '
    '<a href="https://sansad.in/getFile/annex/270/AU3541_Z5B4q6.pdf?source=pqars">Rajya Sabha USQ 3541</a> and <a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2244397">PIB</a> (N:P:K ratios, 2024-25); '
    '<a href="https://www.fao.org/fileadmin/templates/soilbiodiversity/Downloadable_files/fpnb16.pdf">FAO Fertilizer and Plant Nutrition Bulletin 16, Table 29</a>; '
    '<a href="https://agriwelfare.gov.in/Documents/NPMCR_1.pdf">National Policy for Management of Crop Residues, 2014</a>; '
    '<a href="https://www.newindianexpress.com/india/2025/Dec/04/mp-records-higher-stubble-burning-than-5-states">New Indian Express, 4 December 2025</a> (ICAR CREAMS fire counts); '
    '<a href="https://pau.edu/content/ccil/pf/pp_kharif.pdf">PAU, Package of Practices, kharif 2026</a> (Prali Char); '
    '<a href="https://bsssjournals.onlinelibrary.wiley.com/doi/10.1111/sum.70183">Soil Use and Management, 2026</a> (962 households); '
    '<a href="https://panorama.solutions/sites/default/files/2025-11/GIZ_%20Biochar%20Project%20Report.pdf">GIZ biochar project report</a>; '
    '<a href="https://www.tandfonline.com/doi/abs/10.1080/03650340.2016.1139086">groundnut trial on acid soil, 2016</a>; '
    '<a href="https://cicr.org.in/wp-content/uploads/2026/05/Tech-Bulletin-Biochar-Final-new.pdf">CICR biochar bulletin</a>; '
    '<a href="https://circot.icar.gov.in/icar-circot-holds-strategic-discussion-cotton-stalk-biochar-and-farmer-carbon-credits">CIRCOT</a>; '
    '<a href="https://storage.googleapis.com/isometric--production--eu--public-documents/spl_1KBMWD70R1S0VMYW/prj_1KHT9B45F1S0HY3H/pjd_1KR1EHC6Q1S0Y830/pdd.pdf">Green Carbon, Isometric project document, 7 May 2026</a>; '
    '<a href="https://www.thehindubusinessline.com/economy/agri-business/microsoft-off-take-fuels-varahas-biochar-carbon-removal-project-in-maharashtra/article70512554.ece">BusinessLine, 15 January 2026</a> (Varaha&ndash;Microsoft); '
    '<a href="https://sansad.in/getFile/annex/271/AU154_9YCtOe.pdf">Parliament answer on crop-residue scheme releases</a> (Rs 4,549 crore); '
    '<a href="https://puro.earth/cdr-credit-suppliers/facilities/equilibrium-mundargi-biochar-facility">Equilibrium, Mundargi</a>; '
    '<a href="https://platform.carbonfuture.earth/suppliers/mash-makes/projects/2">MASH Makes</a>; '
    '<a href="https://www.klimate.co/platform/project-overview/carboneers">Carboneers</a>; '
    '<a href="https://www.aninews.in/news/business/longstraw-carbon-brings-climate-action-and-rural-employment-together-in-odishas-tribal-heartland20260709155518">LongStraw (ANI)</a>; '
    '<a href="https://icar.gov.in/index.php/en/icar-ccari-goa-organizes-carbon-pathshala-create-awareness-among-farmers-carbon-markets">ICAR-CCARI, Goa</a>; '
    '<a href="https://coenrm.megplanning.gov.in/wp-content/uploads/2026/05/Meghalaya-Community-Biochar-Initiative_English-Version.pdf">Meghalaya community biochar initiative</a>; '
    '<a href="https://agriwelfare.gov.in/Documents/HomeWhatsNew/Framework_for_Voluntary_Carbon_Market_1_Feb_2024_Revised_compressed_1.pdf">MoA&amp;FW voluntary carbon market framework, 2024</a>; '
    '<a href="https://www.ceew.in/publications/carbon-markets-in-india:-pathways-to-durable-carbon-removal">CEEW</a>; '
    '<a href="https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/111325-biochar-carbon-credit-prices-steady-but-sentiment-weakens">S&amp;P Global Platts</a>. '
    'Model and data: out/research/biochar-feedstock/ in this blog&rsquo;s repository (model.py, every coefficient with its source, and the CSVs behind each table). Analysed 14 November 2026.')

RELATED = [
    (U + "2026/09/india-has-tested-its-soil-twice-second.html", "India Has Tested Its Soil Twice. The Second Time, a Machine Chose the Spot."),
    (U + "2026/10/india-has-funded-3-lakh-machines-to.html", "India Has Funded 3 Lakh Machines to Stop Stubble Burning. About 4,500 of Them Collect Straw"),
    (U + "2026/10/cotton-stalk-is-one-of-hardest-crop.html", "Cotton Stalk Is One of the Hardest Crop Wastes to Turn Into Gas. The Manure Left Over Is What India&#x27;s Tired Fields Need."),
    (U + "2026/10/bagasse-is-one-crop-residue-already.html", "Bagasse Is the One Crop Residue Already Sitting at a Factory Gate. Labs Have Liquefied and Hydrolysed It. Nobody Has Priced It Against the Boiler"),
    (U + "2026/10/rice-and-maize-became-ethanol.html", "Rice and Maize Became Ethanol Commodities With a Price, a Buyer and a Warehouse. Straw Has Only the Buyer"),
    (U + "2026/09/india-solved-carbon-credit-banking-with.html", "India Solved Carbon-Credit Banking With No Limit At All. Trading Still Hasn&#x27;t Started."),
    (U + "2026/08/379-kilos-hectare-in-punjab-44-in.html", "379 Kilos a Hectare in Punjab, 44 in Kerala: India&#x27;s Urea Map Is a Crop Map"),
]

build("Agriculture &middot; Soil &middot; Carbon markets",
      f"India&rsquo;s Spare Crop Residue Could Make {nat_el:.0f} Million Tonnes of Biochar a Year. Only Two Crop&ndash;State Pairs Stay Near the Top However You Weigh It",
      "A heatmap of ten residues across eighteen states, scored on spare feedstock, soil need and local openness. Punjab has the most straw; "
      "Odisha&rsquo;s rice straw and Maharashtra&rsquo;s cotton stalk are the only pairs in the top ten under every weighting.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT))

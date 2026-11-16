"""India's power mix in Q2 2026-27 (CREA India Energy Snapshot): renewables ahead of coal in capacity, coal far ahead in generation.
Build from the repo root:  python3 out/research/renewables-vs-coal-2026/build.py   (writes out/post-india-renewables-coal-capacity-generation-q2-2026-27.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-renewables-coal-capacity-generation-q2-2026-27.html"
B = "https://blog.vertistratsolution.com"

# ---- CREA, India Energy Snapshot Q2 2026-27 (12 Oct 2026): https://energyandcleanair.org/quarterly-energy-snapshot-for-india-q2-2026-27
# Press release: https://energyandcleanair.org/wp/wp-content/uploads/2026/10/CREA_Press-Release_India-Energy-Snapshot-Q2-2026.pdf
# Read via the CREA page, Down To Earth (12 Oct), PV Tech (14 Oct), and PTI as carried by ETEnergyWorld and Rediff (11 Nov). Data: Grid-India, CEA, Ministry of Coal, National Power Portal.
# Installed capacity at end-August 2026, GW and share of 555 GW
TOTAL_GW = 555
CAP = {"Renewables (excluding large hydro)": (243, 44), "Coal and lignite": (231, 42), "Large hydro": (52, 9), "Gas": (19, 3), "Nuclear": (8.8, 2)}
SOLAR_GW, WIND_GW, COAL_ONLY_GW = 168, 59, 224
assert round(100 * 243 / TOTAL_GW) == 44 and round(100 * 231 / TOTAL_GW) == 42 and round(100 * SOLAR_GW / TOTAL_GW) == 30
# Generation, Q2 FY2026-27 (July-September), billion units
GEN_TOTAL, GEN_COAL, GEN_RE, GEN_HYDRO, GEN_NONFOSSIL = 536, 351, 101, 60, 177
GEN_SOLAR, GEN_WIND = 51, 45
GEN_NUCLEAR = GEN_NONFOSSIL - GEN_RE - GEN_HYDRO                    # derived: non-fossil total less renewables and large hydro
GEN_GAS_OTHER = GEN_TOTAL - GEN_COAL - GEN_NONFOSSIL
assert GEN_NUCLEAR == 16 and GEN_GAS_OTHER == 8
sh = lambda v: 100 * v / GEN_TOTAL
assert round(sh(GEN_COAL)) == 65 or round(sh(GEN_COAL), 1) == 65.5
assert round(sh(GEN_RE)) == 19 and round(sh(GEN_NONFOSSIL)) == 33 and round(sh(GEN_HYDRO)) == 11
# The CREA press release says coal supplied "around 64%" and the snapshot says coal and lignite 66% (351 BU); the 66% is coal and lignite together.
PLF = {"Nuclear": 82, "Coal": 68, "Wind": 37, "Large hydro": 50, "Solar": 18.3, "Lignite": 51, "Gas": 18}
# Share of the year-on-year increase in generation (PTI/CREA): coal and lignite 73%, solar 27%, wind 19%; large hydro's fall subtracts 27 points
INC = [("Coal and lignite", 73), ("Solar", 27), ("Wind", 19), ("Large hydro", -27)]
GEN_PREV = GEN_TOTAL / 1.11
INC_BU = GEN_TOTAL - GEN_PREV
assert round(INC_BU) == 53
assert round(100 * (GEN_COAL - 312) / INC_BU) == 74 or round(100 * (GEN_COAL - 312) / INC_BU) == 73         # 351 less 312 BU a year earlier
assert round(100 * (GEN_SOLAR - GEN_SOLAR / 1.39) / INC_BU) == 27 and round(100 * (GEN_WIND - GEN_WIND / 1.29) / INC_BU) == 19
assert round(100 * (GEN_HYDRO - GEN_HYDRO / 0.80) / INC_BU) == -28 or round(100 * (GEN_HYDRO - GEN_HYDRO / 0.80) / INC_BU) == -27
# Evening peak, prices, storage, curtailment
PEAK_SOLAR_DAYS, DAYS = 62, 92
STORAGE_NIGHT_GW, STORAGE_PREV_GW = 5.5, 4.1
BESS_OPERATING_GWH, BESS_DUE_GWH, TENDERED_GWH, TENDER_PSP, TENDER_BESS = 9.1, 3, 290, 142, 151
assert TENDER_PSP + TENDER_BESS == 293                               # CREA gives "approximately 290 GWh"; the two components sum to 293
CURT_MU, CURT_SOLAR, CURT_WIND = 1835, 1462, 373
assert CURT_SOLAR + CURT_WIND == CURT_MU
# Crisil, via ETEnergyWorld 5 Nov 2026: average exchange prices in October, Rs per unit
SOLAR_NOW, SOLAR_PREV, NONSOLAR_NOW, NONSOLAR_PREV = 2.3, 1.4, 6.8, 3.1
assert round(NONSOLAR_NOW / SOLAR_NOW, 1) == 3.0
# Government factsheet via Sarkaritel, 13 Nov 2026 (secondary): installed capacity about 560 GW in October 2026, non-fossil 55%, solar nearly 175 GW.

TITLE = "India's power mix, Q2 2026-27: coal 42% of capacity but 66% of generation"
assert 55 <= len(TITLE) <= 80, len(TITLE)

top = top_line([
    ("243 GW", f" of renewable capacity (44% of {TOTAL_GW} GW) passed 231 GW of coal and lignite (42%) by August 2026, with solar at {SOLAR_GW} GW; in the July&ndash;September quarter renewables gave {sh(GEN_RE):.0f}% of generation and coal and lignite {sh(GEN_COAL):.0f}%."),
    ("73%", " of the year-on-year increase in electricity came from coal and lignite, against 27% from solar and 19% from wind; large hydro&rsquo;s 20% fall subtracted 27 points (CREA, via PTI)."),
    ("5.5 GW", f" was the most that battery storage supplied at the night peak, about 1&ndash;2% of demand, while {CURT_MU:,} million units of solar and wind output were curtailed in July and August."),
])

s1 = insight(
    "Coal and lignite are 42% of capacity and 66% of generation; renewables 44% and 19%",
    bars("Coal and lignite: 42% of capacity and 66% of generation; renewables: 44% and 19%",
         [("Renewables, share of capacity", 44), ("Renewables, share of generation", round(sh(GEN_RE))),
          ("Coal and lignite, share of capacity", 42), ("Coal and lignite, share of generation", round(sh(GEN_COAL)))],
         accent="Coal and lignite, share of generation", unit="%",
         sub="Capacity at the end of August 2026; generation in July to September 2026 (Q2 of 2026-27). Renewables exclude large hydro.",
         source="CREA, India Energy Snapshot Q2 2026-27, 12 October 2026 (Grid-India, CEA); generation shares computed by this blog from the billion-unit figures.")
    + numbers(["Source", "Capacity (GW)", "Share of capacity (%)", "Generation (BU)", "Share of generation (%)", "Plant load factor (%)"],
              [["Renewables, excluding large hydro", "243", "44", f"{GEN_RE}", f"{sh(GEN_RE):.1f}", "solar 18.3, wind 37"],
               ["Coal and lignite", "231 (coal 224)", "42", f"{GEN_COAL}", f"{sh(GEN_COAL):.1f}", "coal 68, lignite 51"],
               ["Large hydro", "52", "9", f"{GEN_HYDRO}", f"{sh(GEN_HYDRO):.1f}", "50"],
               ["Nuclear", "8.8", "2", f"{GEN_NUCLEAR} (derived)", f"{sh(GEN_NUCLEAR):.1f}", "82"],
               ["Gas and others", "19 (gas)", "3", f"{GEN_GAS_OTHER} (derived)", f"{sh(GEN_GAS_OTHER):.1f}", "gas 18"],
               ["Total", f"{TOTAL_GW}", "100", f"{GEN_TOTAL}", "100.0", ""]]),
    "A coal unit ran at 68% of its rated output over the quarter, wind at 37% and solar at 18.3%, so a gigawatt of coal delivers several times the energy of a gigawatt of solar and the capacity share overstates what renewables supply.",
    "MNRE and CEA should publish plant load factors and generation shares beside installed capacity in each monthly progress table, so that a capacity milestone is not read as a supply milestone.",
    "mix")

s2 = insight(
    "Coal and lignite supplied 73% of the year&rsquo;s extra electricity; solar 27%, wind 19%",
    bars("Coal supplied 73% of the extra power; solar 27% and wind 19%; hydro&rsquo;s fall took off 27%",
         INC, accent="Coal and lignite", unit="%",
         sub="Share of the 11% year-on-year rise in generation (about 53 BU), per cent; large hydro generation fell 20%, which subtracts from the total, so the shares exceed 100% before the fall.",
         source="CREA via PTI (ETEnergyWorld and Rediff, 11 November 2026); the 53 BU is computed from the 11% rise on 536 BU.")
    + numbers(["Measure", "Value", "Source"],
              [["Total generation", "536 BU, +11% year on year (about 483 BU a year earlier)", "CREA; the earlier value is computed"],
               ["Coal and lignite", "351 BU against 312 BU a year earlier, +12.5%", "CREA"],
               ["Solar, wind, nuclear", "+39%, +29%, +26%", "CREA"],
               ["Large hydro", "60 BU, &minus;20% year on year; plant load factor 50% against 61%", "CREA"],
               ["Non-fossil total", "177 BU, up from 163 BU; about 33% of generation", "CREA"],
               ["Capacity added in the quarter", "about 7 GW renewable, 0.8 GW thermal; 648 MW thermal retired", "CREA"]]),
    "Renewable generation grew by about 14 BU of solar and 10 BU of wind, but large hydro fell about 15 BU and demand rose about 53 BU, so coal and lignite added 39 BU in a quarter of weak rain and record peaks.",
    "Planners should read renewable growth against the hydro and demand movements in the same quarter, since a year of poor rain turns the same solar addition into a smaller share of the extra supply.",
    "increase")

s3 = insight(
    "The price after sunset was Rs 6.8 a unit in October, three times the solar-hour price",
    bars("After sunset the price was Rs 6.8 a unit in October, three times the Rs 2.3 in solar hours",
         [("Solar hours, October 2025", SOLAR_PREV), ("Solar hours, October 2026", SOLAR_NOW), ("Other hours, October 2025", NONSOLAR_PREV), ("Other hours, October 2026", NONSOLAR_NOW)],
         accent="Other hours, October 2026", unit="", fmt=lambda v: f"Rs {v:.1f}",
         sub="Average short-term power market price in Rs per unit, October; &ldquo;other hours&rdquo; are the non-solar hours.",
         source="Crisil, via ETEnergyWorld, 5 November 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["Daily peak in solar hours", f"{PEAK_SOLAR_DAYS} of {DAYS} days in Q2", "CREA"],
               ["Battery storage at night peak", f"up to {STORAGE_NIGHT_GW} GW (from {STORAGE_PREV_GW} GW in Q1), about 1&ndash;2% of national demand", "CREA"],
               ["Coal plants at night", "&ldquo;the evening peak is still largely met by coal&rdquo;", "CREA via PTI"],
               ["Installed capacity, October 2026", "about 560 GW, 55% non-fossil, solar nearly 175 GW", "Government factsheet via Sarkaritel, 13 November 2026 (secondary)"]]),
    f"The daily peak fell in daylight on {PEAK_SOLAR_DAYS} of {DAYS} days, which favours solar, but the price after sunset ran three times the daytime price, so the scarce hours are the ones coal still covers.",
    "CERC and Grid-India should publish hourly short-term market prices and energy not met by state each month, so the value of evening supply can be compared with the cost of storage.",
    "evening")

s4 = insight(
    "Battery storage: 9.1 GWh operating, 3 GWh due by December, about 290 GWh tendered",
    bars("About 9.1 GWh of battery storage operates; about 290 GWh of storage has been tendered",
         [("Battery storage operating", BESS_OPERATING_GWH), ("Battery storage due by December 2026", BESS_DUE_GWH),
          ("Tendered: batteries", TENDER_BESS), ("Tendered: pumped storage", TENDER_PSP)],
         accent="Battery storage operating", unit=" GWh", sub="Energy storage capacity in GWh; tender figures are as of August 2026.",
         source="CREA, India Energy Snapshot Q2 2026-27, 12 October 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["Tenders issued by August 2026", f"about {TENDERED_GWH} GWh ({TENDER_BESS} GWh batteries, {TENDER_PSP} GWh pumped storage; the parts sum to {TENDER_PSP + TENDER_BESS})", "CREA"],
               ["Curtailed solar and wind, July and August", f"{CURT_MU:,} MU ({CURT_SOLAR:,} MU solar, {CURT_WIND} MU wind)", "CREA"],
               ["Curtailed renewables in the April&ndash;June quarter", "1,874 MU, about 1.36% of renewable generation (a different data set)", "JMK Research, via PV Tech"]]),
    f"Operating batteries are about {100 * BESS_OPERATING_GWH / TENDERED_GWH:.0f}% of the tendered volume, and the {CURT_MU:,} million units curtailed in July and August show output that storage and grid limits could not carry.",
    "The power ministry and CEA should publish tendered, awarded and commissioned storage in GWh each quarter, with state curtailment and its cause, so the pipeline can be tracked to delivery.",
    "storage")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>MNRE and CEA:</b> publish plant load factors and generation shares next to installed capacity in every monthly progress table.</li>
<li><b>Grid-India and CEA:</b> publish curtailment of solar and wind by state and cause each month; the CREA figure covers only July and August.</li>
<li><b>Ministry of Power and CEA:</b> publish tendered, awarded and commissioned storage in GWh each quarter and the dates by which awarded projects are due.</li>
<li><b>CERC and Grid-India:</b> publish hourly market prices and energy not met by state, to price the evening hours.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Capacity is at the end of August 2026 (555 GW, up 12% on a year earlier); generation is July to September 2026. The two periods differ by a month, which matters little for shares.</li>
<li>&ldquo;Renewables&rdquo; excludes large hydro, as in CREA&rsquo;s tables. &ldquo;Coal and lignite&rdquo; is 231 GW of capacity; coal alone is 224 GW. CREA&rsquo;s press release gives coal as about 64% of generation, and its snapshot gives coal and lignite as about 66% (351 BU of 536); this piece uses the 66%, which includes lignite.</li>
<li>Nuclear (16 BU) and gas and other sources (8 BU) are derived from CREA&rsquo;s totals: non-fossil 177 BU less renewables 101 BU and large hydro 60 BU; total 536 BU less coal and lignite 351 BU and non-fossil 177 BU.</li>
<li>The shares of the increase are CREA&rsquo;s as reported by PTI; the 53 BU increase and the BU split in the text are computed from the stated growth rates.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>CREA&rsquo;s report was read through its own web page and press release, with Down To Earth, PV Tech and PTI, not as a full PDF; the exchange-price figures are Crisil&rsquo;s, as reported by ETEnergyWorld.</li>
<li>The share of the extra generation that is solar-plus-wind against coal depends on weather: a year with normal rain would give hydro a larger share. This piece does not test the weather link.</li>
<li>Curtailment is reported for July and August only, so no quarterly share is given; JMK Research reports a different April&ndash;June figure from a different data set.</li>
<li>Storage tender volumes are tenders issued, not awards or commissioning dates; the 3 GWh due by December is CREA&rsquo;s expectation.</li>
<li>Capacity after August: the government factsheet put total capacity at about 560 GW in October (secondary report); the generation and plant-load figures stop at September.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://energyandcleanair.org/quarterly-energy-snapshot-for-india-q2-2026-27">CREA, Quarterly energy snapshot for India, Q2 2026-27, 12 October 2026</a> (capacity, generation, load factors, storage, curtailment; based on Grid-India, CEA, Ministry of Coal and National Power Portal data) and its '
    '<a href="https://energyandcleanair.org/wp/wp-content/uploads/2026/10/CREA_Press-Release_India-Energy-Snapshot-Q2-2026.pdf">press release</a>; '
    '<a href="https://www.downtoearth.org.in/energy/indias-renewable-power-generation-crosses-100-billion-units-in-a-quarter-for-first-time-as-coal-stocks-fall-crea">Down To Earth, 12 October 2026</a>; '
    '<a href="https://www.pv-tech.org/indias-solar-generation-rises-39-in-q2-crea">PV Tech, 14 October 2026</a> (solar utilisation; JMK curtailment); '
    '<a href="https://energy.economictimes.indiatimes.com/news/renewable/renewables-overtake-coal-in-capacity-but-coal-still-supplied-most-of-summers-new-power-crea/135735591">ETEnergyWorld (PTI), 11 November 2026</a> (shares of the increase); '
    '<a href="https://energy.economictimes.indiatimes.com/news/coal/indias-power-demand-hits-record-160-bu-in-october-as-coal-stocks-fall-to-five-year-low/135577143">ETEnergyWorld (Crisil), 5 November 2026</a> (October exchange prices); '
    '<a href="https://www.sarkaritel.com/india-installed-power-capacity-560-gw-non-fossil-55-percent/">Sarkaritel, 13 November 2026</a> (government factsheet, October capacity; secondary). '
    'Shares of capacity and generation, derived items and ratios computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/08/574-gw-and-counting-indias-wind-fleet.html", "India's wind power by state: 57.4 GW installed, under a tenth of the potential"),
    (f"{B}/2026/09/indias-battery-storage-boom-is.html", "Grid battery storage in India: about 9.3 GWh by mid-2026, up from 1.08 GWh"),
    (f"{B}/2026/11/14500-crore-for-92-gwh-indias-storage.html", "India's storage subsidy: ₹14,500 crore for 92 GWh, down to ₹1,576 a kWh"),
    (f"{B}/2026/10/green-energy-corridor-iii-is-15-times.html", "Green Energy Corridor III: 15 times the size of phase II, with phases I and II incomplete"),
    (f"{B}/2026/08/rooftop-solar-is-working-household.html", "Rooftop solar in India: over 12 GW by May 2026, household batteries unsubsidised"),
]

build("Energy &middot; Power", TITLE,
      "CREA's quarterly snapshot shows renewables ahead of coal in installed capacity but behind by about 47 points in generation, with coal covering 73% of the extra power and storage reaching 1&ndash;2% of night demand.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")

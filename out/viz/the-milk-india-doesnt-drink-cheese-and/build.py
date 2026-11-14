"""Visual-first edition of the-milk-india-doesnt-drink-cheese-and. Run from the repo root:  python3 out/viz/the-milk-india-doesnt-drink-cheese-and/build.py"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from exec_viz import STYLE, bars, flow, insight, line, numbers, sources_block, top_line, waterfall  # noqa: E402,F401
from viz_frame import body_links, split  # noqa: E402

SLUG = "the-milk-india-doesnt-drink-cheese-and"
SRC = (ROOT / f"posts/{SLUG}.html").read_text(encoding="utf-8")
FR = split(SRC)
OUT = ROOT / f"out/update-2026-11-15-{SLUG}.html"

# Numbers computed from the original's numbers go in derived.json ({"190": "570/3"}), never typed in silently.

RS = "&#8377;"

top = top_line([
    ("247.87 MT", " of milk in 2024-25, with roughly a third left after liquid milk, on the order of 82-83 MT. "
                  "The processed share is contested: about 25% to 40% depending on the source."),
    (f"{RS}128.9 billion", f" cheese market in 2025, projected by IMARC to reach {RS}619.9 billion in 2034 "
                           "at about 19.1% a year; mozzarella is about 35% of the category."),
    (f"{RS}403.07 crore", " cheese trade surplus in 2024-25. Dairy is excluded from the EFTA agreement, "
                          "so tariff access is not what is driving it."),
])

s1 = insight(
    "Processed milk: sources put the share anywhere from about 25% to 40%",
    bars("The share of India&rsquo;s milk that is processed is contested, from about 25% to 40%",
         [("Spread across the sources", (25, 40)),
          ("Through organised dairies only <small>around 25%</small>", 25),
          ("Everything but liquid milk <small>roughly 35%, implied by the liquid-milk share</small>", 35),
          ("Processed at all, formal or informal <small>one estimate: 40%</small>", 40)],
         accent="Spread across the sources", unit="%", vmax=100, from_zero=True,
         sub="Share of milk output, %. Solid to the lower estimate, lighter to the higher one.",
         source="Lok Sabha answer, Department of Animal Husbandry and Dairying (posted 12 August 2026): 247.87 MT in 2024-25. "
                "Processed-share figures from separate sources, not reconciled.")
    + numbers(["Step", "Figure"],
              [["Milk produced, 2024-25", "247.87 MT"], ["Milk produced, 2020-21", "209.96 MT"],
               ["Moves as liquid milk", "roughly two-thirds"],
               ["Left for ghee, paneer, curd, powder, khoa and cheese", "roughly a third, on the order of 82-83 MT"]]),
    "Roughly a third of milk, on the order of 82-83 MT, is left for everything but liquid milk, but the processed share is "
    "contested, so read the pool as an order of magnitude and not a precise number.",
    "The Department of Animal Husbandry and Dairying should publish an annual estimate of milk use by product, split between "
    "organised and informal channels, so one official number replaces the 40%, 25% and roughly 35% in circulation.",
    "milk")

s2 = insight(
    f"Cheese market: projected to grow from {RS}128.9 billion in 2025 to {RS}619.9 billion in 2034",
    bars(f"IMARC projects the cheese market at {RS}619.9 billion in 2034, up from {RS}128.9 billion",
         [("2025", 128.9), ("2034, projected", 619.9)],
         accent="2034, projected", fmt=lambda v: f"{RS}{v:g} billion",
         sub="India&rsquo;s cheese market value, &#8377; billion (about USD 1.5 billion in 2025 and USD 7.3 billion in 2034).",
         source="IMARC Group market sizing, a single firm&rsquo;s estimate that was not cross-checked against a second source.")
    + numbers(["Metric", "Figure"],
              [["Market value, 2025", f"{RS}128.9 billion (~USD 1.5bn)"], ["Projected value, 2034", f"{RS}619.9 billion (~USD 7.3bn)"],
               ["CAGR (2026-2034)", "~19.1%"], ["Mozzarella share of category", "~35%, the largest single format"],
               ["Shredded-format share", "~30% of the market"]]),
    "The projected growth of about 19.1% a year over 2026-2034 is led by mozzarella, about 35% of the category, and by shredded "
    "formats at about 30%, which move mostly through HoReCa channels rather than retail.",
    "The Ministry of Food Processing Industries should publish the capacity added and output achieved by each PLI beneficiary "
    "in mozzarella and other dairy, so capacity-growth claims can be checked.",
    "market")

fy = [("2018-19", 249.70, 70.85, 178.85), ("2019-20", 248.42, 68.72, 179.70), ("2020-21", 297.61, 32.73, 264.88),
      ("2021-22", 277.12, 61.01, 216.11), ("2022-23", 377.73, 89.77, 287.96), ("2023-24", 450.91, 116.86, 334.05),
      ("2024-25", 494.90, 91.83, 403.07)]
for _, e, i, bal in fy:
    assert round(e - i, 2) == bal

s3 = insight(
    f"Cheese trade: the surplus grew from {RS}178.85 crore in 2018-19 to {RS}403.07 crore in 2024-25",
    bars(f"Cheese trade surplus reached {RS}403.07 crore in 2024-25, up from {RS}178.85 crore in 2018-19",
         [(y, bal) for y, _, _, bal in fy], accent="2024-25", fmt=lambda v: f"{RS}{v:.2f} crore",
         sub="Exports minus imports of cheese and curd (HSN 0406), &#8377; crore by fiscal year.",
         source="DGCI&amp;S TradeStat, HSN 0406, checked to the paisa.")
    + numbers(["Fiscal year", f"Exports ({RS} Cr)", f"Imports ({RS} Cr)", f"Balance ({RS} Cr)"],
              [[y, f"{e:.2f}", f"{i:.2f}", f"+{b:.2f}"] for y, e, i, b in fy]),
    "Exports grew at roughly 12.1% CAGR against 4.4% for imports over the six years shown (seven fiscal years of data), "
    "with one dip in the surplus, in 2021-22.",
    "Quote the &#8377; crore TradeStat series, which was checked to the paisa, and treat the calendar-year USD series "
    "(about $13.4m in 2012 to about $53.2m in 2023) as a second check, not a reconciled figure.",
    "trade")

s4 = insight(
    "Trade deals: India kept dairy out of EFTA (2025) and UAE (2022) and left RCEP (2019)",
    flow([
        ("November 2019", "India walks out of RCEP, the only prospective member to do so. Dairy was a named reason: GCMMF, which markets Amul, "
                          "led opposition to tariff cuts on dairy imports from New Zealand and Australia."),
        ("May 2022", "The India-UAE CEPA comes into force. Dairy sits inside the 1,157 tariff lines (about 9.7% of all lines) "
                     "that India kept off the table."),
        ("1 October 2025", "The EFTA-India TEPA comes into force. India agreed no line-item reductions for dairy, and Switzerland grants no "
                           "commitments on butter (heading 0405) or cheese and curd (heading 0406).", True),
        ("20 October 2026", "The India-New Zealand agreement comes into force with no tariff concession on cheese, milk, cream, whey, "
                            "butter or caseins; only milk albumins get a half-duty quota."),
    ]),
    "So cheese-export growth is not an EFTA story: the post points to APEDA market access and buyer linkage in the Gulf and Singapore, "
    "rising value-added dairy demand and the mozzarella-and-PLI capacity build.",
    "The Department of Commerce should host the full India-EFTA TEPA tariff schedules line by line on its own website, so the "
    "exclusion of ghee, paneer, butter and milk powder can be confirmed from the treaty text.",
    "deals")

players = f"""<details class="xv-n"><summary>Who is making cheese</summary>
<ul>
<li><b>Amul (GCMMF):</b> cooperative leader with a full portfolio. It invested {RS}200 crore from 2021 to scale buffalo-milk mozzarella production for domestic and export markets, and mozzarella came under the government&rsquo;s PLI scheme in 2021.</li>
<li><b>Milky Mist:</b> private challenger, heavy in South India. Listed in August 2026; an estimated ~19% of India&rsquo;s organised packaged paneer market (~60% within South India) and ~12% of South India&rsquo;s organised cheese market; one integrated plant at Perundurai, Erode (Tamil Nadu), with 192 tonnes/day paneer capacity; South India supplied 69.23% of FY26 revenue.</li>
<li><b>Britannia and Go Cheese (Parag Milk):</b> retail-distribution challengers. Britannia uses its biscuit and FMCG network; Go Cheese markets itself on a &ldquo;cow milk&rdquo; positioning.</li>
<li><b>Nandini (KMF), Aavin, Verka:</b> state cooperatives, strong and often cheaper in home states, without the national cold-chain and distribution reach to compete pan-India.</li>
<li><b>D&rsquo;lecta and Lactalis:</b> B2B and premium niche, focused on hotel and restaurant supply and natural cheese.</li>
</ul>
<p class="gb-note">Amul figures per Business Standard&rsquo;s 2021 coverage; Milky Mist figures per its IPO disclosures and dairy-trade press. Other players&rsquo; positioning is qualitative and not independently verified.</p></details>
"""

paras = f"""<details class="xv-n"><summary>Case study: Paras Dairy&rsquo;s {RS}100 crore cheese plant</summary>
<p>Paras Dairy built a cheese plant in Ahmednagar, Maharashtra, making its Galacia brand from cow&rsquo;s milk with Individual Quick Freezing (IQF) so shredded and diced product stays uniform for commercial kitchens and smaller HoReCa outlets. It has put over {RS}100 crore into the plant.</p>
<p>Its stated goals, as of its most recent public announcements, are more than 2,000 outlets (from 500-plus) and 100 new distributors by March 2026, and a place among India&rsquo;s top five cheese brands within the following year. These are the company&rsquo;s own targets, not verified outcomes.</p>
</details>
"""

claim = """<details class="xv-n"><summary>One claim that did not survive checking</summary>
<p>A figure in circulation says Amul &ldquo;expanded mozzarella production capacity by 1,200%&rdquo;. The sourced figure is that India&rsquo;s mozzarella exports reached USD 3.29 million in April-September 2025, up more than 1,200% year on year: export growth off a small base, not Amul&rsquo;s capacity, which was built through a separate &#8377;200 crore programme.</p>
<p>A second data point needs no correction: at the Mundial do Queijo do Brasil 2026, Indian cheesemakers won a Super Gold, two Golds and a Silver among entries from over 30 countries. That is a signal about India&rsquo;s small artisanal segment, not the mass mozzarella market.</p>
</details>
"""

cold = """<details class="xv-n"><summary>Cold chain: the size of the gap is unsettled</summary>
<p>Regional cooperatives (Nandini, Aavin, Verka) stay in their home states mainly because of cold-chain logistics. Estimates of the gap range from a shortfall of roughly 8 million tonnes of cold-storage capacity to the National Centre for Cold-Chain Development&rsquo;s figure of an additional 35 million tonnes, depending on baseline and demand assumptions; the post presents the spread deliberately rather than collapsing it.</p>
<p>What is consistent: only around 4% of India&rsquo;s perishable-food transport moves in refrigerated vehicles, the other 96% is unrefrigerated, and cold storage is concentrated in a handful of states, leaving central and eastern India under-served.</p>
</details>
"""

basket = """<details class="xv-n"><summary>Cheese is a small part of India&rsquo;s dairy exports</summary>
<ul>
<li>Per an APEDA-commissioned CRISIL Intelligence 2024 basket breakdown, ghee was 42% of dairy export value, butter 18%, paneer/cottage cheese 15%, processed cheese 6% and fresh cheese 1%.</li>
<li>Cheese in both forms combined is a smaller export category than butter alone; HSN 0406 is the 4th-largest export subchapter in Chapter 04, narrowly ahead of heading 0408 (&#8377;494.60 crore).</li>
<li>Ghee exports are projected to grow at roughly 35% CAGR from 2021 to 2026, priced 30-35% below European ghee on a September-2025 snapshot.</li>
<li>The main destinations for Indian cheese are the UAE, Saudi Arabia and Singapore.</li>
</ul>
</details>
"""

method = """<details class="xv-n"><summary>How the trade figures were sourced</summary>
<p>The &#8377; crore series (FY2018-19 to FY2024-25) was checked against the DGCI&amp;S TradeStat portal and matches to the paisa. A second, differently based series covers calendar years 2012-2023 in US dollars: exports roughly quadrupled from about $13.4m to about $53.2m, while imports grew more slowly and dipped sharply in 2020. The two bases were not reconciled; both show the same growing-surplus trend.</p>
</details>
"""

treaty = """<details class="xv-n"><summary>What the treaty text shows for ghee, paneer, butter and milk powder</summary>
<ul>
<li>India&rsquo;s schedules to Switzerland, Iceland and Norway mark ghee (04059020), mozzarella (04061010), the residual cheese line that covers paneer (04061090) and the other cheese lines as &ldquo;Exclusion&rdquo;; Switzerland&rsquo;s Annex 2.F marks headings 0405 and 0406 as &ldquo;NC&rdquo;, meaning no commitments on import duties.</li>
<li>Butter shares heading 0405 with ghee, and the milk-powder lines of heading 0402 are marked &ldquo;Exclusion&rdquo; in the Swiss schedule too. Dahi and yoghurt fall under heading 0403.</li>
<li>Dairy is not shut on the Swiss side: Annex 2.F gives a few reductions within 0402 and 0403, such as a preferential rate within a tariff quota on one milk-powder line and 10 off the MFN rate on flavoured yoghurt.</li>
<li>EFTA&rsquo;s offer covers 100% of non-agricultural tariff lines duty-free, plus some processed agricultural products; the carve-out is dairy, soya, coal and select other categories, not agriculture as a whole.</li>
<li>EFTA&rsquo;s own website blocked access, so the schedules were read from the copies published by India&rsquo;s Department of Commerce.</li>
</ul>
</details>
"""

fixes = """<h2 class="gb-h2" id="fix">What would fix this</h2>
<ol>
<li><b>Department of Animal Husbandry and Dairying:</b> publish an annual estimate of milk utilisation by product, split between organised and informal channels.</li>
<li><b>National Centre for Cold-Chain Development:</b> publish a dated, state-wise cold-chain gap assessment stating its baseline and demand assumptions, so the gap is not quoted from roughly 8 million to 35 million tonnes.</li>
<li><b>Department of Commerce:</b> host the full India-EFTA TEPA tariff schedules, line by line, on its own website.</li>
<li><b>Ministry of Food Processing Industries:</b> publish the capacity added and output achieved by each PLI beneficiary in mozzarella and other dairy.</li>
</ol>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>
"""

updated = ('<p class="gb-note"><b>Updated 15 November 2026:</b> rewritten as four charts; the figures are unchanged from the 7 November update. '
           'Corrected 25 October 2026: the trade figures were re-checked against TradeStat and stand; the growth period is six years '
           '(seven fiscal years of data), not seven.</p>\n')

extras = (players + paras + claim + cold + basket + method + treaty + fixes + "\n" + sources_block(body_links(FR.body)))

sections = [s1, s2, s3, s4]
body = STYLE + top + FR.keep_front + FR.notes + updated + "".join(sections) + extras
OUT.write_text(FR.head + FR.mid + body + "\n" + FR.tail, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))

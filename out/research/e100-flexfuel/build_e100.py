import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-e100-flex-fuel.html'

# ---------------------------------------------------------------- energy (this blog's figures, LHV MJ/L)
PETROL, ETHANOL = 32.4, 21.3
def blend(e): return (1 - e) * PETROL + e * ETHANOL
E20, E30, E85, E100 = blend(0.20), blend(0.30), blend(0.85), blend(1.0)
R85, R100 = E85 / E20, E100 / E20                      # energy per litre relative to E20

# ---------------------------------------------------------------- prices (Delhi, Rs/litre)
P_E20 = 102.12                                         # Indian Oil, Oct 2026 (unchanged since Jul)
P_E85 = 82.12                                          # Indian Oil Pusa Road, launched 5 Jun 2026
EXCISE = 19.90                                         # central excise on petrol, Rs/L (Jan 2026)
VAT = 0.194                                            # Delhi VAT on petrol
VAT_RS = P_E20 - P_E20 / (1 + VAT)
TAX = EXCISE + VAT_RS
ETH_LANDED = 71.2                                      # weighted ethanol cost to OMCs incl. GST and freight, ESY 2025-26 (this blog)
def per_km_index(price, ratio, gain=0.0): return price / (ratio * (1 + gain)) / P_E20 * 100
IDX85 = per_km_index(P_E85, R85)
BE85, BE100 = P_E20 * R85, P_E20 * R100                # break-even retail price, same efficiency
BE85_G, BE100_G = P_E20 * R85 * 1.05, P_E20 * R100 * 1.05   # with a 5% efficiency gain
E100_TAXED = (ETH_LANDED + EXCISE) * (1 + VAT)         # if E100 bore petrol's excise and VAT
IDX100_TAXED = per_km_index(E100_TAXED, R100)
HEADROOM = BE100 - ETH_LANDED

# ---------------------------------------------------------------- volumes (crore litres, ESY 2025-26, this blog)
PETROL_MT = 42.6
L_PER_MT = 141.1
POOL = PETROL_MT * L_PER_MT                            # motor-spirit pool, crore litres
SURPLUS = 576                                          # offered capacity with no buyer, even with the Q4 top-up
OFFERED = 1776
E30_2030 = 2221                                        # ethanol for E30 in 2029-30, central case (this blog)
def extra_ethanol(share):                              # share of petrol energy moved to E100 flex-fuel vehicles
    return share * POOL * (E20 / E100) - share * POOL * 0.20
SCEN = [0.02, 0.05, 0.10, 0.20]
EXTRA = {s: extra_ethanol(s) for s in SCEN}
SHARE_SURPLUS = SURPLUS / extra_ethanol(1.0) * 100

# ---------------------------------------------------------------- Brazil 2025 (ANP via QCI)
BR_HYD, BR_GASC = 21.24, 46.65                         # billion litres
BR_ANHY = 0.2825                                       # average anhydrous share of gasolina C in 2025 (27% to Jul, 30% from Aug)
HYD_MJ = 20.2                                          # hydrous ethanol (about 95% ethanol), assumption
gasc_mj = blend(BR_ANHY)
br_eth_energy = BR_HYD * HYD_MJ + BR_GASC * BR_ANHY * ETHANOL
br_total = BR_HYD * HYD_MJ + BR_GASC * gasc_mj
BR_SHARE = br_eth_energy / br_total * 100
BR_HYD_SHARE = BR_HYD * HYD_MJ / br_total * 100
IN_E20_SHARE = 0.20 * ETHANOL / E20 * 100
IN_E30_SHARE = 0.30 * ETHANOL / E30 * 100
BR_PARITY_2025 = 68.57
BR_PARITY_Q1_26 = (72.63, 73.65, 73.14)
IN_E85_RATIO = P_E85 / P_E20 * 100


def chart_cost():
    rows = [("E20 petrol, Rs %.2f" % P_E20, 100.0, "#868e96"),
            ("E85 at Rs %.2f" % P_E85, IDX85, "#a5402c"),
            ("E100 at break-even Rs %.1f" % BE100, 100.0, "#1c5d99"),
            ("E100 taxed like petrol, ~Rs %.0f" % E100_TAXED, IDX100_TAXED, "#a5402c")]
    W, L, top, bh, gap, lab = 400, 10, 26, 18, 9, 170
    H = top + len(rows) * (bh + gap) + 30
    sc = (W - L - lab - 40) / 160
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Fuel cost per kilometre as an index, E20 petrol = 100: E85 at Rs {P_E85} is {IDX85:.0f}; E100 at Rs {BE100:.1f} is 100; E100 taxed like petrol is {IDX100_TAXED:.0f}.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Fuel cost per kilometre, E20 petrol = 100</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v:.0f}</text>')
    x100 = L + lab + 100 * sc
    s.append(f'<line x1="{x100:.1f}" x2="{x100:.1f}" y1="{top - 4}" y2="{top + len(rows) * (bh + gap) - gap + 4}" stroke="#212529" stroke-dasharray="3 3"/>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Same engine efficiency per unit of energy; Delhi prices, Oct 2026.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Energy: petrol {PETROL} MJ/L, ethanol {ETHANOL} MJ/L. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_volume():
    W, L, top, bh, gap, lab = 400, 10, 42, 18, 9, 150
    rows = [(f"{int(s * 100)}% of petrol energy", EXTRA[s]) for s in SCEN]
    H = top + len(rows) * (bh + gap) + 30
    vmax = 1600
    sc = (W - L - lab - 46) / vmax
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Extra ethanol needed if flex-fuel vehicles on E100 took 2, 5, 10 or 20 percent of petrol energy demand, against an unsold surplus of {SURPLUS} crore litres.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Extra ethanol if flex-fuel cars on E100 took a share, crore litres</text>']
    for i, (n, v) in enumerate(rows):
        y = top + i * (bh + gap)
        col = "#1c5d99" if v <= SURPLUS else "#a5402c"
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v:,.0f}</text>')
    xs = L + lab + SURPLUS * sc
    yb = top + len(rows) * (bh + gap) - gap
    s.append(f'<line x1="{xs:.1f}" x2="{xs:.1f}" y1="{top - 6}" y2="{yb + 4}" stroke="#212529" stroke-dasharray="3 3"/>')
    s.append(f'<text x="{xs + 3:.1f}" y="{top - 8}" font-size="9" fill="#212529">unsold surplus {SURPLUS}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">On the 2025-26 petrol pool ({PETROL_MT} Mt); net of the E20 ethanol those vehicles already use.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_steps():
    return table(["Date", "Step", "What it did"], [
        ("15 Mar 2024", "&ldquo;Ethanol 100&rdquo; launched by Indian Oil", "Sold at 183 outlets in five states, when few vehicles on sale could use it"),
        ("1 Apr 2026", "E20 becomes the only petrol sold", "All petrol at the pump carries 20% ethanol"),
        ("27 Apr 2026", "Draft amendment to the Central Motor Vehicles Rules", "Proposed adding E85 and E100 to the emission and certification rules"),
        ("5 Jun 2026", "E85 goes on sale", f"Indian Oil, Pusa Road, Delhi, at Rs {P_E85}/litre against Rs {P_E20} for E20; targets of 500 pumps by Dec 2026 and 5,000 by Dec 2027"),
        ("Late Oct 2026", "G.S.R. 911(E) notified (reported 26 Oct)", "Rule 115 now reads &ldquo;E85 or E100&rdquo;; vehicles must be designed and certified for these fuels; no obligation on owners of existing vehicles"),
    ])


def t_compare():
    return table(["", "India", "Brazil"], [
        ("Ethanol in regular petrol", "20% (E20)", "30% (E30) since Aug 2025"),
        ("Flex-fuel share of cars", "Close to zero; first models announced for late 2026&ndash;27", "About 82% of the light fleet; over 90% of new sales"),
        ("Ethanol share of car-fuel energy", f"{IN_E20_SHARE:.0f}% at E20; {IN_E30_SHARE:.0f}% at E30", f"About {BR_SHARE:.0f}% in 2025 ({BR_HYD_SHARE:.0f}% from pure hydrous ethanol)"),
        ("High-ethanol fuel price vs petrol", f"E85 at {IN_E85_RATIO:.0f}% of E20; needs about {R85 * 100:.0f}% to match per km", f"Hydrous at {BR_PARITY_2025}% of gasoline on average in 2025; drivers switch when it is above about 70%"),
        ("Tax rule", "No rule that ethanol fuels be taxed below petrol", "Constitutional Amendment 123/2022 requires biofuels to be taxed below fossil fuels for 20 years"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>G.S.R. 911(E)</b><span>notified in late October 2026: flex-fuel vehicles may now be certified to run on E100</span></div>
<div class="gb-stat"><b>+{IDX85 - 100:.0f}%</b><span>more per kilometre for E85 at Rs {P_E85} than E20 petrol at Rs {P_E20}, by energy content</span></div>
<div class="gb-stat"><b>Rs {BE100:.0f}</b><span>a litre is where E100 matches petrol per km; ethanol already costs oil companies Rs {ETH_LANDED} delivered</span></div>
<div class="gb-stat"><b>{SHARE_SURPLUS:.0f}%</b><span>of petrol demand is all today&rsquo;s unsold ethanol could move to E100</span></div>
</div>'''

body = f"""
{stats}

<p>In late October the Ministry of Road Transport and Highways notified an amendment to the Central Motor Vehicles Rules that lets manufacturers certify flex-fuel vehicles to run on E100, pure ethanol, as well as E85. The rules apply only to vehicles designed for these fuels, and the ministry said no owner of an existing vehicle has to switch or modify anything. E85 went on sale in Delhi in June, and the first flex-fuel cars and motorcycles are being readied for launch.</p>
<p>This blog has looked at <a href="https://masaladeutsch.blogspot.com/2026/10/indias-ethanol-surplus-buys-about-five.html">how far India&rsquo;s ethanol surplus stretches</a> and <a href="https://masaladeutsch.blogspot.com/2026/09/brazil-pumps-e30-at-every-station.html">how Brazil sells E30 and E100 side by side</a>. This piece asks the two questions the new rule raises: would a driver save money on E100, and is there enough ethanol for a flex-fuel fleet?</p>

<h2 class="gb-h2">How India got to E100</h2>
{t_steps()}

<h2 class="gb-h2">Per kilometre, E85 costs more than petrol</h2>
{chart_cost()}
<p>A litre of ethanol holds about {ETHANOL} megajoules of energy against {PETROL} for petrol, so a litre of E85 carries about {R85 * 100:.0f}% of the energy of a litre of E20, and a litre of E100 about {R100 * 100:.0f}%. A car needs correspondingly more litres to go the same distance. At Rs {P_E85} a litre, E85 is {100 - IN_E85_RATIO:.0f}% cheaper at the pump than E20 but about {IDX85 - 100:.0f}% dearer per kilometre. It would have to sell at about Rs {BE85:.1f} to break even.</p>
<p>Engines built for high-ethanol fuel can recover some of the gap, because ethanol&rsquo;s high octane allows a higher compression ratio. If a flex-fuel engine were 5% more efficient on ethanol, the break-even prices would rise to about Rs {BE85_G:.1f} for E85 and Rs {BE100_G:.1f} for E100. That is a favourable case, and E85 at Rs {P_E85} is still just above it.</p>
<p>E100 has a harder problem. To match E20 per kilometre at the same efficiency it would have to sell at about Rs {BE100:.1f} a litre. Oil companies already pay about Rs {ETH_LANDED} a litre for ethanol delivered to their depots, including GST and freight. That leaves less than Rs {HEADROOM:.0f} a litre for excise, VAT, the dealer&rsquo;s commission and the oil company&rsquo;s own costs. Petrol in Delhi carries about Rs {TAX:.0f} of excise and VAT. If E100 bore the same excise and VAT rate, it would cost about Rs {E100_TAXED:.0f} a litre, about {IDX100_TAXED - 100:.0f}% more per kilometre than petrol. Industry body SIAM has said E100 works only at about 30% below the price of petrol, which matches the energy arithmetic.</p>

<h2 class="gb-h2">There is not enough ethanol for a large flex-fuel fleet</h2>
{chart_volume()}
<p>India&rsquo;s distilleries offered {OFFERED:,} crore litres for the 2025-26 supply year, and about {SURPLUS} crore litres had no buyer even after the fourth-quarter top-up. Moving a share of petrol demand to E100 needs about 1.4 litres of ethanol for every litre of E20 it replaces, less the 20% ethanol those vehicles already burn. On the 2025-26 petrol pool, the unsold surplus would cover flex-fuel vehicles taking about {SHARE_SURPLUS:.0f}% of petrol demand. A 10% share would need about {EXTRA[0.10]:,.0f} crore litres more.</p>
<p>The same litres are already spoken for. This blog&rsquo;s central forecast puts the ethanol needed for E30 alone at {E30_2030:,} crore litres in 2029-30, more than everything offered this year. Every litre that goes into a flex-fuel tank is a litre that cannot raise the blend in ordinary petrol, which every car on the road uses.</p>

<h2 class="gb-h2">What Brazil&rsquo;s flex-fuel fleet shows</h2>
{t_compare()}
<p>Brazil is the proof that flex-fuel cars work at scale: about 82% of its light vehicles can run on any mix of petrol and ethanol, and ethanol supplied about {BR_SHARE:.0f}% of the energy its cars used in 2025, by this blog&rsquo;s arithmetic from ANP sales data. But it also shows that a flex-fuel fleet does not guarantee ethanol is used. Drivers fill with hydrous ethanol when it costs less than about 70% of the petrol price, and switch back when it does not. The national ratio averaged {BR_PARITY_2025}% in 2025, and hydrous ethanol sales fell 2.3% that year to {BR_HYD} billion litres; in the first three months of 2026 the ratio was above 72%.</p>
<p>What keeps Brazilian ethanol competitive is tax. Since a 2022 constitutional amendment, Brazil must tax biofuels less than the fossil fuels they replace, and keep that gap for 20 years; São Paulo, for example, charged 13.3% state tax on hydrous ethanol against 25% on petrol. India has no equivalent rule, and the E100 notification says nothing about price.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Ministry of Petroleum and Natural Gas and the states should publish how E85 and E100 are priced and taxed, and set a rule that keeps their price per kilometre below petrol&rsquo;s, as Brazil&rsquo;s constitution does, before asking people to buy flex-fuel vehicles.</li>
<li>Oil companies should post E85 and E100 prices with a per-kilometre comparison at the pump, so buyers can see whether the cheaper litre is the cheaper journey.</li>
<li>The ethanol roadmap should state how much ethanol is reserved for flex-fuel vehicles and how much for raising the blend in ordinary petrol, since the same supply cannot do both.</li>
<li>Vehicle makers should publish certified fuel economy for each flex-fuel model on both E20 and E100, so the efficiency gain on ethanol is measured rather than assumed.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The text of G.S.R. 911(E) could not be opened; its contents come from press reports of the notification. No E100 retail price has been published, so the E100 figures are break-even prices, not quotes. The per-kilometre comparison assumes the same efficiency per unit of energy on every fuel, with a 5% gain as a sensitivity; real results will depend on each engine. The tax arithmetic leaves out the dealer&rsquo;s commission and oil company costs, and treats Delhi&rsquo;s VAT as 19.4% of the pre-VAT price. Brazil&rsquo;s energy shares use this blog&rsquo;s assumed energy content for hydrous ethanol ({HYD_MJ} MJ/L) and an average 2025 blend of {BR_ANHY * 100:.2f}%. Reports differ on whether Indian Oil&rsquo;s 2024 &ldquo;Ethanol 100&rdquo; was pure ethanol or a blend with additives.</p>
"""

sources = ("Notification: Business Standard (26 October 2026), NewsOrbiter and PGurus on G.S.R. 911(E) and the April 2026 draft; QCI on approvals and pricing discussions. E85 launch and prices: Autocar Pro, Rushlane, Free Press Journal and Outlook Business (June 2026). Ethanol 100 launch: Indian Oil news release (15 March 2024), Autocar Pro, Biofuels Digest. Flex-fuel models and SIAM&rsquo;s 30% remark: Business Today (May and June 2026). Delhi petrol price: The Hans India (16 October 2026), Upstox; excise and VAT: Upstox, BankBazaar. "
           "Ethanol supply, landed cost and the 2029-30 forecast: this blog&rsquo;s ethanol-surplus piece (October 2026), from PIB, ChiniMandi and NITI Aayog&rsquo;s method; energy densities from this blog&rsquo;s fuel-pairs piece. "
           "Brazil: ANP sales for 2025 via QCI; price parity series from Brazil&rsquo;s Ministry of Agriculture (from ANP data); S&amp;P Global on the 70% rule; Constitutional Amendment 123/2022 via Machado Meyer and state decrees; flex-fuel fleet share from this blog&rsquo;s Brazil piece. "
           "Per-kilometre indices, break-even prices, ethanol volumes and Brazil&rsquo;s energy shares are this blog&rsquo;s arithmetic. Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/indias-ethanol-surplus-buys-about-five.html", "India&rsquo;s Ethanol Surplus Buys About Five Blend Points. E30, Diesel and Jet Fuel Need Twice the Supply."),
    ("https://masaladeutsch.blogspot.com/2026/09/brazil-pumps-e30-at-every-station.html", "Brazil Pumps E30 at Every Station. The Equipment Behind It Is the Part India&rsquo;s E20 Story Skips"),
    ("https://masaladeutsch.blogspot.com/2026/08/blending-on-budget-energy-density-and.html", "Blending on a Budget: Energy Density and Cost Per Kilometre, Across Four Fuel Pairs"),
    ("https://masaladeutsch.blogspot.com/2026/09/e20-doesnt-cut-tailpipe-co2-by-30-run.html", "E20 Doesn&rsquo;t Cut Tailpipe CO2 by 30%. Run the Chemistry and the Real Number Is Close to Zero"),
]

build("Ethanol &amp; Biofuels · 27 October 2026",
      "India Has Legalised E100 for Flex-Fuel Cars. Its E85 Still Costs More per Kilometre Than Petrol",
      "A notification in late October lets flex-fuel vehicles be certified for pure ethanol. At current prices E85 is cheaper per litre but dearer per kilometre, E100 can only compete if it is taxed far below petrol, and today&rsquo;s unsold ethanol would cover about 8% of petrol demand.",
      body, sources, related, OUT)
print(f"E20 {E20:.2f} E85 {E85:.2f} R85 {R85:.3f} R100 {R100:.3f} idx85 {IDX85:.1f} BE85 {BE85:.1f} BE100 {BE100:.1f} BE100g {BE100_G:.1f} BE85g {BE85_G:.1f} tax {TAX:.1f} E100taxed {E100_TAXED:.1f} idx {IDX100_TAXED:.0f} headroom {HEADROOM:.2f}")
print("pool", POOL, {k: round(v) for k, v in EXTRA.items()}, "surplus share", round(SHARE_SURPLUS, 1), "BR", round(BR_SHARE, 1), round(BR_HYD_SHARE, 1), "IN", round(IN_E20_SHARE, 1), round(IN_E30_SHARE, 1))

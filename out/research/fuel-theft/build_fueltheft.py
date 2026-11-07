import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-fuel-theft-history.html'

# ---- Karnataka Legal Metrology test results, announced 6 Nov 2026 (South First, BusinessLine, PTI, The Hindu)
KA = [("IOCL", 31.2), ("HPCL", 30.5), ("HPCL", 27.0), ("BPCL", 26.5), ("Nayara", 26.1), ("Shell", 25.5),
      ("BPCL", 24.2), ("BPCL", 22.6), ("HPCL", 22.4), ("IOCL", 20.8), ("Nayara", 20.6),
      ("BPCL", 19.9), ("MRPL", 19.2), ("Shell", 13.5)]
KA_COLLECTED = 63
BAND_LO, BAND_HI = 19.0, 21.0            # IS 17021 E20: 19-21% ethanol by volume
ABOVE = [v for _, v in KA if v > 20.0]
OUT_HI = [v for _, v in KA if v > BAND_HI]
assert len(KA) == 14 and len(ABOVE) == 11
MEAN_ABOVE = sum(ABOVE) / len(ABOVE)
MEAN_ALL = sum(v for _, v in KA) / len(KA)

# ---- OMC surveys (joint IOCL/BPCL/HPCL statement and MoPNG release, 6-7 Nov 2026)
OMC_SAMPLES = {"IOCL": 330, "BPCL": 280, "HPCL": 283}
OMC_TOTAL = sum(OMC_SAMPLES.values())
assert OMC_TOTAL == 893
OMC_KA_N, OMC_KA_AVG = 56, 19.30

# ---- Energy arithmetic: lower heating values, MJ per litre (approximate textbook values)
LHV_ETH, LHV_PET = 21.2, 32.0
def energy(pct):
    return (1 - pct / 100) * LHV_PET + pct / 100 * LHV_ETH
def loss_vs_e20(pct):
    return (1 - energy(pct) / energy(20)) * 100
PER_POINT = (LHV_PET - LHV_ETH) / 100 / energy(20) * 100      # % energy lost per extra point of ethanol, near E20
LOSS_MEAN = loss_vs_e20(MEAN_ABOVE)
LOSS_MAX = loss_vs_e20(max(ABOVE))
LOSS_E20_VS_E0 = (1 - energy(20) / energy(0)) * 100

# ---- The minister's estimate (The Hindu; The South First)
MIN_LITRES_CR = 6200        # crore litres of fuel a year, as stated
MIN_PRICE = 100             # Rs per litre, as stated
MIN_LOSS = 0.10             # 10% mileage loss, as stated
MIN_CR = MIN_LITRES_CR * MIN_PRICE * MIN_LOSS            # Rs crore
assert round(MIN_CR) == 62000
MIN_REPAIRS = 39000
MIN_TOTAL = MIN_CR + MIN_REPAIRS
# Same volume and price, with the energy loss computed above instead of 10%
RATIO = MIN_LOSS * 100 / LOSS_MEAN
ALT_MEAN_CR = MIN_LITRES_CR * MIN_PRICE * LOSS_MEAN / 100
# India's petrol sales, PPAC statewise workbook as used on this blog: 40,004 thousand tonnes; density ~0.745 kg/L
INDIA_PETROL_TMT = 40004
INDIA_PETROL_CR_L = INDIA_PETROL_TMT * 1000 * 1000 / 0.745 / 1e7     # crore litres

# ---- Arbitrage: ESY 2026-27 ethanol prices vs retail petrol
ETH_MAIZE, ETH_CHEAVY = 68.86, 57.97
PETROL_LO, PETROL_HI = 94.77, 105.0


def chart_ka():
    W, L, lab, top, bh, gap = 360, 6, 62, 52, 16, 5
    n = len(KA)
    H = top + n * (bh + gap) + 50
    mx = 34.0
    sc = (W - L - lab - 34) / mx
    x0 = L + lab
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Ethanol content of 14 petrol samples tested by Karnataka Legal Metrology, against the 19 to 21 percent band of the E20 standard.">',
         f'<text x="{L}" y="15" font-size="13.5" fill="#495057">Ethanol in 14 Karnataka petrol samples, %</text>',
         f'<text x="{L}" y="31" font-size="11" fill="#6c757d">Lab results reported by the state, by outlet brand.</text>',
         f'<text x="{L}" y="45" font-size="11" fill="#6c757d">Shaded: the 19&ndash;21% band of the E20 standard.</text>']
    yb = top + n * (bh + gap)
    s.append(f'<rect x="{x0 + BAND_LO * sc:.1f}" y="{top - 3}" width="{(BAND_HI - BAND_LO) * sc:.1f}" height="{yb - top + 3}" fill="#dee2e6"/>')
    for i, (co, v) in enumerate(KA):
        y = top + i * (bh + gap)
        s.append(f'<text x="{x0 - 6}" y="{y + 12}" font-size="11.5" fill="#212529" text-anchor="end">{co}</text>')
        s.append(f'<rect x="{x0}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="#1c5d99" fill-opacity=".85"/>')
        s.append(f'<text x="{x0 + v * sc + 4:.1f}" y="{y + 12}" font-size="11.5" fill="#212529">{v:.1f}</text>')
    for t in (0, 10, 20, 30):
        s.append(f'<text x="{x0 + t * sc:.1f}" y="{yb + 13}" font-size="10.5" fill="#6c757d" text-anchor="middle">{t}</text>')
    s.append(f'<text x="{L}" y="{H - 18}" font-size="10.5" fill="#6c757d">63 samples collected, 14 tested. The oil</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="10.5" fill="#6c757d">companies dispute the results; see text.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


TIMELINE = [
    ("2003", "Kerosene dyed blue; the dye is easily removed, and a furfural marker proves unstable (Down to Earth)"),
    ("2005", "NCAER finds about 38% of PDS kerosene diverted. Motor Spirit and HSD Control Order issued"),
    ("Nov 2005", "IOC sales officer S. Manjunath shot dead at a Lakhimpur Kheri pump he had acted against"),
    ("2007", "Oil ministry orders a 5 ppm marker in all kerosene"),
    ("Jan 2009", "Marker doping discontinued after a de-marking powder is found (2008)"),
    ("2010", "Kirit Parikh group: 35% or more of kerosene diverted, much of it into diesel"),
    ("Jan 2011", "Additional Collector Yashwant Sonawane burnt alive near Manmad while filming kerosene theft from a tanker"),
    ("2011&ndash;12", "Pipelines law amended with stiffer penalties for tapping and sabotage"),
    ("2015&ndash;17", "101 cases of chips in pump dispensers reported; UP police raids from April 2017"),
    ("2017", "About 1 lakh litres stolen from a pipeline near Mathura through a tunnel"),
    ("2020&ndash;21", "Spurious biodiesel raids in Gujarat; the state bans retail sale of biodiesel (July 2021)"),
    ("2021", "IOCL reports 34 pipeline pilferage attempts and 53 arrests in 2020-21"),
    ("Mar 2024", "Telangana police say a gang took over 2,400 L from parked trucks in 17 thefts in a month"),
    ("Jan 2025", "Gang tunnels 100 m to an IOC crude line in Rajasthan, police say"),
    ("2025", "Bengaluru police seize about 60,000 L in a racket siphoning diesel meant for bus depots"),
    ("May 2026", "Nine arrested with 1,120 L taken from a coal train inside a mine at Talcher, Odisha"),
    ("Jul&ndash;Aug 2026", "Pipeline taps in Tonk (12 arrested) and Balotra (8 arrested), Rajasthan"),
    ("Nov 2026", "Karnataka says 11 of 14 petrol samples exceed 20% ethanol; oil companies dispute the tests"),
]

stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>~38%</b><span>of kerosene sold through ration shops was being diverted, NCAER estimated in 2005, much of it into diesel</span></div>
<div class="gb-stat"><b>101</b><span>cases of chips or other tampering in pump dispensers found by oil companies, April 2015 to June 2017</span></div>
<div class="gb-stat"><b>{len(ABOVE)} of {len(KA)}</b><span>petrol samples tested for Karnataka exceeded 20% ethanol, the state said on 6 November 2026</span></div>
<div class="gb-stat"><b>{OMC_TOTAL}</b><span>samples in the oil companies&rsquo; own national surveys, all within 19&ndash;21%, they said in reply</span></div>
</div>'''

body = f"""
{stats}
<p>Fuel theft in India has changed shape with each change in what was cheap and where it could be hidden. For three decades the main fraud was subsidised kerosene, poured into diesel. Then pipelines became targets for gangs with drills and tunnels, pumps for fraudsters with chips in their dispensers, and diesel tanks for &ldquo;biodiesel&rdquo; that was mostly industrial solvent. In November 2026 a new argument began, over whether petrol in Karnataka holds more ethanol than the law allows. This piece sets out that history, the record of what was proved and what was only alleged, and where the Karnataka dispute stands.</p>

<h2 class="gb-h2">Timeline</h2>
{table(["When", "What happened"], [(f'<span style="display:block;text-align:left">{w}</span>', e) for w, e in TIMELINE])}
<p class="gb-note">Sources for each entry are in the sections below and in the sources list.</p>

<h2 class="gb-h2">Kerosene: the subsidy that fed adulteration</h2>
<p>For decades the government sold kerosene through ration shops at a fraction of the price of diesel. The two fuels are similar enough that kerosene could be mixed into diesel with little effect a customer would notice, and the price gap made it profitable. A 2005 study for the oil ministry by the National Council of Applied Economic Research (NCAER) estimated that about 38% of public distribution system (PDS) kerosene was diverted; the Rangarajan committee on fuel pricing cited the figure in 2006, and the IMF put it at &ldquo;almost 40%&rdquo;. In 2010 the Kirit Parikh expert group said 35% or more was diverted, partly into diesel, and warned that adulteration could undo more than Rs 20,000 crore of refinery investment in cleaner Euro III and IV diesel. A study of Maharashtra for 2004-05 estimated that 50 of the 118 million litres allocated each month went to other markets, and noted that distribution there was often controlled by organised crime.</p>
<p>The government tried to make diverted kerosene detectable. It was dyed blue, which could be removed. A furfural marker proved unstable. In January 2007 the oil ministry ordered all kerosene doped with a chemical marker at 5 parts per million, enforced through the Motor Spirit and High Speed Diesel Control Order of 2005. In September 2008 the Indian Oil Corporation&rsquo;s vigilance wing found a brown powder that removed the marker, and doping was stopped from 1 January 2009, according to the ministry&rsquo;s affidavit quoted by the Supreme Court in 2018. An IISD study put the imported marker&rsquo;s cost at about $33 million a year.</p>
<p>Two killings made the trade national news. On 19 November 2005 S. Manjunath, a 27-year-old Indian Oil sales officer and IIM Lucknow graduate, was shot dead at a pump in Gola, Lakhimpur Kheri, whose sales he had suspended in September for selling adulterated fuel. A trial court sentenced the pump owner&rsquo;s son, Pawan Kumar &ldquo;Monu&rdquo; Mittal, to death in 2007 and seven others to life; the Allahabad High Court commuted the death sentence and acquitted two, and in March 2015 the Supreme Court upheld life terms for six. In January 2011 Yashwant Sonawane, Additional Collector of Malegaon, was set on fire near Manmad while filming kerosene being taken from a tanker. Police said about 300 tankers were filled daily at the Manmad depots and that gangs opened them with duplicate keys. Maharashtra raided depots across the state in the following weeks. The main accused died of burns he suffered in the attack, and a Malegaon court sentenced three men to life imprisonment in September 2022, Indian Mandarins reported.</p>
<p>The kerosene channel has largely closed. As cooking gas spread and states gave up their PDS kerosene quotas, volumes fell, though this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/diesel-doesnt-move-cpi-it-moves-40.html">diesel piece</a> notes that PDS kerosene was still 73% of the kerosene India consumed in May 2026.</p>

<h2 class="gb-h2">Pipelines: drills, valves and tunnels</h2>
<p>Pipelines carry crude and products across thousands of kilometres of farmland, and gangs tap them by digging down, fitting a valve and running a hose to a tanker or a storage pit. In 2017 about 1 lakh litres were stolen from the Mathura&ndash;Jalandhar line near Mathura through a tunnel, ET Energy reported, and police described a racket of about Rs 100 crore, a figure that was not independently verified. Indian Oil said in 2021 that it had recorded 34 pilferage attempts and 53 arrests in 2020-21, and that it now watches pipelines with SCADA systems, an intrusion-detection system along the line and drones on a 120 km stretch. State oil-security committees chaired by each director general of police meet every quarter. Parliament stiffened penalties for damaging or tapping pipelines in an amendment to the Petroleum and Minerals Pipelines Act passed in 2011; Indian Oil refers to it as the 2012 amendment.</p>
<p>The cases have not stopped. In 2024 the CBI registered a case against two Hindustan Petroleum assistant managers at the Mathura terminal over alleged pilferage; this is an allegation, not a conviction. In January 2025 Rajasthan police said a gang had leased land near Kotputli-Behror, built a wall and dug a 100 m tunnel to an Indian Oil crude line, which it tapped for four months. In December 2025 Delhi Police arrested two men over a tap on a Hindustan Petroleum diesel line near Jaipur, and said they had run such thefts for about 30 years across four states. In 2026, 12 people were arrested over a 40-foot illegal pipe on an Indian Oil line at Pachewar in Tonk in July, and 8 over a tap on a crude pipeline near Balotra in August, where police said about 20 tonnes of crude was taken.</p>

<h2 class="gb-h2">Diesel pilferage: trucks, trains and generator sets</h2>
<p>Most diesel theft is smaller and closer to the user than a pipeline tap, and it rarely reaches national statistics. Its commonest form is siphoning from the tanks of parked trucks. In March 2024 Nalgonda police in Telangana arrested six men who, they said, broke the locks on the tanks of trucks parked on highways at night while drivers slept, and took over 2,400 litres in 17 thefts in a month, carrying it in cans to Andhra Pradesh for sale (Deccan Chronicle). In 2021 Prakasam police in Andhra Pradesh arrested a gang from Madhya Pradesh for similar thefts on the Chennai&ndash;Kolkata highway (The Hindu), and in November 2026 police in Bemetara, Chhattisgarh, said they had broken an inter-district gang stealing diesel from parked heavy vehicles (ETV Bharat, Hindi; search snippet only). Highway eateries have long been part of the trade: the dhaba where Yashwant Sonawane&rsquo;s team seized 4,000 litres of kerosene and 3,000 litres of petrol in 2010 belonged to the man later accused of his killing.</p>
<p>Tankers are the second target, because each carries thousands of litres. In January 2024 Mumbai police registered a case against 11 people accused of drawing diesel from Indian Oil tankers and selling it to a tug operator at Mumbai port at Rs 65 a litre; police said they took 150&ndash;200 litres a day and seized about 12,000 litres (Free Press Journal). In Goa, Mormugao police seized five tankers and 12 barrels in May 2025 over alleged siphoning (Times of India). One of the two men arrested in December 2025 over pipeline taps, police said, began in the early 1990s as a tanker driver drawing diesel from his own load (The Economic Times).</p>
<p>How much fleets lose is not measured by any public body. Companies that sell fuel sensors for trucks commonly put losses in unmonitored Indian fleets at 5&ndash;15% of fuel spend, and two vendors attribute an estimate of about 8% of diesel filled to the trade magazine MotorIndia, which could not be checked. These are marketing figures, and the same vendors say much of the loss is waste from idling and poor maintenance rather than theft.</p>
<p>Railways lose diesel from locomotives and from the generator cars that power coaches. The Railway Protection Force (RPF) books these cases under the Railway Property (Unlawful Possession) Act. Reported cases are small: in Guwahati, four people were arrested in April 2025 over diesel taken from a train&rsquo;s generator van, four more in June 2026 after a video of siphoning from a power car spread on social media, and seven in September 2026 over about 150 litres, valued at Rs 14,250, taken from a power car on a sick line (The Sentinel; Pratidin Time). In July 2026 RPF at Jhansi arrested four people and the buyer over about 300 litres (Amar Ujala, Hindi; search snippet only). In May 2026 Talcher police in Odisha arrested nine people and seized 1,120 litres taken from a coal train standing inside a mine for loading (OdishaTV).</p>
<p>Mobile-tower sites with diesel generators are a third target. In May 2025 police in Ri Bhoi, Meghalaya, arrested three men with 220&ndash;230 litres in jerrycans; police said they had confessed to siphoning it from three Reliance Jio towers (The Sentinel). Most reported tower thefts, though, are of radio equipment rather than fuel. Mines are a fourth: answering a Lok Sabha question in March 2021, the coal ministry said NLC India&rsquo;s vehicle tracking helps it manage diesel pilferage, and that Singareni Collieries had put CCTV cameras at its opencast diesel bunkers.</p>
<p>The incentive has grown in 2026. With crude above $100, oil companies charge bulk buyers more than Rs 40 a litre above the retail pump price, as this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/diesel-doesnt-move-cpi-it-moves-40.html">diesel piece</a> sets out. Bulk buyers moved to pumps, and private retailers rationed sales to them. A gap that size rewards anyone who can move retail-priced diesel into bulk tanks. In Bengaluru in 2025 the city&rsquo;s Central Crime Branch arrested four people for siphoning diesel meant for city and state bus depots, seizing about 60,000 litres from three tankers; police said about 50 litres were drawn from each tanker using duplicate keys, Deccan Herald reported.</p>

<h2 class="gb-h2">Pumps: chips and short delivery</h2>
<p>The cheapest theft needs no adulterant: deliver less fuel than the meter shows. In April 2017 Uttar Pradesh&rsquo;s Special Task Force raided pumps in Lucknow and found electronic chips in dispensers that cut delivery while showing the full amount. Police estimated each tampered pump made about Rs 14 lakh a month, from chips costing about Rs 3,000; these are police estimates. The oil ministry told the Lok Sabha in July 2017 that 101 cases of chips or other high-tech tampering had been found between April 2015 and June 2017, 51 of them in Uttar Pradesh, and that 44 outlets had been terminated after joint inspections. In one case before the Allahabad High Court, nozzles were short by 200&ndash;220 ml in every 5 litres. The oil companies&rsquo; marketing discipline guidelines now require random sampling of at least 2% of outlets a month and suspend sales when a density or filter-paper test fails.</p>
<p>Customers can ask for two checks at any pump. A drop of petrol on filter paper should evaporate in about two minutes without a stain, and dealers must provide the paper. The fuel&rsquo;s density, read with a hydrometer in a 500 ml jar and corrected to 15&deg;C, should match the figure in the outlet&rsquo;s register.</p>

<h2 class="gb-h2">Spurious biodiesel</h2>
<p>When diesel prices rose in 2020-21, cheaper &ldquo;biodiesel&rdquo; appeared at roadside outlets. Much of it was made from furnace oil, base oil, mineral turpentine and white spirit, and sold for about Rs 50&ndash;55 a litre when diesel cost Rs 80&ndash;97. Gujarat police seized 89,000 litres at seven outlets in Rajkot in June 2020 and 37 lakh litres in Anand in July 2021, and the state banned retail sale of biodiesel on 3 July 2021. The oil ministry told the Rajya Sabha in December 2021 that it had received complaints from Andhra Pradesh, Gujarat, Maharashtra, Telangana, Rajasthan and Tamil Nadu, and had written to every state&rsquo;s chief secretary. At Mundra, customs found an import declared as &ldquo;mixed glycol&rdquo; to be diesel.</p>

<h2 class="gb-h2">Karnataka: more ethanol than the label?</h2>
<p>On 6 November 2026 Karnataka&rsquo;s minister for food, civil supplies and legal metrology, Rizwan Arshad, announced the results of petrol testing by the state Department of Legal Metrology. It collected {KA_COLLECTED} samples from Bengaluru, Bengaluru Rural, Kolar, Chikkaballapura, Ramanagara, Mangaluru and Tumakuru and sent {len(KA)} to accredited laboratories, with reports from the Shriram Research Institute in Bengaluru. {len(ABOVE)} of the {len(KA)} showed more than 20% ethanol, the highest 31.2% at an Indian Oil outlet. The state said samples first sent to oil-company laboratories came back without the ethanol content disclosed.</p>
{chart_ka()}
<p>Under the Indian standard for E20 petrol (IS 17021), ethanol must be between 19% and 21%. On the state&rsquo;s figures, {len(OUT_HI)} of the {len(KA)} samples were above that band and one, at 13.5%, below it. The state argues that most pump equipment is designed for up to 15% ethanol and that vehicles are certified for no more than E20. It has asked for action against the oil companies, a fund to compensate motorists for damage, ethanol content displayed at pumps, a choice of blends and batch-wise blending records, and has empowered officials from the Food Commissioner to police officers of deputy superintendent rank to take samples under the 2005 Control Order. Rahul Gandhi called it &ldquo;420-petrol chori&rdquo;, The Hindu reported.</p>
<p>Indian Oil, Bharat Petroleum and Hindustan Petroleum rejected the findings in a joint statement, and the petroleum ministry issued a release on 7 November. Their main points:</p>
<ul>
<li>The samples were taken in October without oil-company representatives, and neither retained samples nor the lab reports were shared. The Control Order requires six one-litre samples, two each for the dealer, retention and testing, under jointly signed labels.</li>
<li>The laboratory is not one specified under the Control Order. Its certificates cite gas chromatography but not the method, dilution or reference correction that IS 17021 requires.</li>
<li>The reported densities, 0.742&ndash;0.749 g/cc, are below the 0.752&ndash;0.760 the companies find in their own E20 surveys. Ethanol is denser than petrol, so a higher ethanol share should raise density, not lower it.</li>
<li>Their own surveys covered {OMC_TOTAL} samples in 27 states and union territories (Indian Oil {OMC_SAMPLES["IOCL"]}, BPCL {OMC_SAMPLES["BPCL"]}, HPCL {OMC_SAMPLES["HPCL"]}), all within 19&ndash;21%. The {OMC_KA_N} Karnataka samples among them were 19&ndash;20%, averaging {OMC_KA_AVG:.2f}%.</li>
</ul>
<p>The density point is the most testable claim on either side, and it cuts against the state&rsquo;s results: if the reported densities are right, the samples are hard to square with 25&ndash;31% ethanol. The companies&rsquo; procedural points are about chain of custody, not chemistry. Neither side has yet published full lab reports. A joint retest under the Control Order procedure, with witnesses and retained samples, would settle most of it; neither side has yet said one is planned.</p>
<h3>How much would excess ethanol cost a driver?</h3>
<p>Ethanol carries less energy than petrol, about {LHV_ETH} megajoules a litre against about {LHV_PET:.0f}. Near E20 each extra percentage point of ethanol cuts the energy in a litre by about {PER_POINT:.2f}%. At the average of the {len(ABOVE)} readings above 20% ({MEAN_ABOVE:.1f}%), a litre holds about {LOSS_MEAN:.1f}% less energy than E20; at the highest reading ({max(ABOVE)}%), about {LOSS_MAX:.1f}% less. For comparison, E20 holds about {LOSS_E20_VS_E0:.1f}% less energy than pure petrol.</p>
<p>The minister put the cost of lost mileage at Rs 62,000 crore a year, by applying a 10% loss to 6,200 crore litres of fuel at Rs 100 a litre, and added Rs 39,000 crore of repairs. Three problems. A 10% loss is about {RATIO:.0f} times the energy shortfall at the average reported reading, even if every litre sold were blended that high, and more than the {LOSS_E20_VS_E0:.1f}% gap between E20 and pure petrol; the same volume and price with a {LOSS_MEAN:.1f}% loss gives about Rs {round(ALT_MEAN_CR, -2):,.0f} crore. The tests cover {len(KA)} samples, not all petrol. And 6,200 crore litres is more than India&rsquo;s entire petrol sales, about {INDIA_PETROL_CR_L:,.0f} crore litres on PPAC&rsquo;s latest statewise data, so it cannot be Karnataka&rsquo;s volume. The repair estimate came without a method. The state&rsquo;s figure is better read as a ceiling on a worst case than as an estimate.</p>

<h2 class="gb-h2">Why ethanol changes the adulteration game</h2>
<p>Kerosene fraud worked because a subsidised fuel was cheaper than the one it diluted. Ethanol creates a smaller version of the same gap. Oil companies buy ethanol in 2026-27 at Rs {ETH_CHEAVY} to Rs {ETH_MAIZE} a litre, while petrol retails at about Rs {PETROL_LO}&ndash;{PETROL_HI:.0f}. Blending happens at oil-company depots, not pumps, so extra ethanol would have to be added at the depot or in transit, which is why the state&rsquo;s demand for batch-wise blending records matters. Ethanol also attracts water. If water gets into a pump&rsquo;s underground tank, an ethanol-water layer can separate and sink to the bottom, where the suction pipe draws from, so the fuel delivered can vary from the fuel supplied. The 2024 marketing guidelines tell pump inspectors to test ethanol content after removing water from the tank and to stop sales if it is out of range. Whether any of the Karnataka results reflect fraud, measurement error or water in tanks cannot be told from what has been published.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>Every state sampling drive should follow the Control Order procedure, with oil-company and dealer witnesses and retained samples, so that its results can be checked rather than argued over.</li>
<li>Oil companies should publish their fuel-quality survey results by state, including ethanol content, density and the number of samples, so that the public sees the same data the companies cite in a dispute.</li>
<li>Pumps should display the ethanol content of the current tank batch next to the price, as Karnataka has asked.</li>
<li>Pipeline operators should report pilferage attempts and arrests every year, by company and state, so that it is possible to tell whether tapping is rising or falling.</li>
<li>The Railway Protection Force, tower companies and public-sector mines should publish the diesel thefts they record each year, in cases and litres, as the coal ministry already does for coal recovered in raids.</li>
<li>States should report how many dispenser inspections, short-delivery findings and terminations they make each year, building on the 2017 count of 101 chip cases.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>There is no national series of fuel theft or adulteration: the 38% kerosene estimate dates from 2005, the chip count stops in 2017 and Indian Oil&rsquo;s pipeline figure covers only 2020-21. Earlier money estimates of the kerosene trade, such as about Rs 5,000 crore a year at 2005-06 prices in an IISD study, are left as dated estimates rather than updated. No national count of diesel theft from trucks, trains, towers, mines or construction sites was found, nor any RPF total for diesel; the truck-fleet loss rates are vendor claims, and no construction-site case or state police figure turned up. Most pipeline, pump and diesel cases here are arrests or police claims; outcomes in court were found only for the Manjunath and Sonawane killings, and the Sonawane verdict rests on one report. The year of the pipelines amendment is given as 2011 or 2012 in different sources. In Karnataka, neither the state&rsquo;s lab reports nor the oil companies&rsquo; survey data were seen in full; both are as reported by the press and the ministry release. Whether the Rs 62,000 crore figure was meant for Karnataka or for India could not be confirmed. The energy figures above use approximate textbook heating values, and real mileage effects also depend on the engine.</p>
"""

sources = ("Karnataka tests: The South First (6 November 2026); BusinessLine; PTI via The Daily Pioneer; The Hindu (6&ndash;7 November 2026, including the minister&rsquo;s Rs 62,000 crore estimate and Rahul Gandhi&rsquo;s remarks). "
           "Oil-company response: joint statement of IOCL, BPCL and HPCL and Ministry of Petroleum and Natural Gas release of 7 November 2026, as reported by The Economic Times, DD India, India TV and Cartoq. "
           "Kerosene: NCAER, Comprehensive Study to Assess the Demand and Requirement of SKO (2005), as cited in the Rangarajan committee report on pricing and taxation of petroleum products (PPAC, February 2006) and IMF Selected Issues (2006); Report of the Expert Group on a Viable and Sustainable System of Pricing of Petroleum Products (Kirit Parikh, PPAC, February 2010); IISD/TERI (2012); Rao, Energy for Sustainable Development (2012); Down to Earth (2003). "
           "Marker history: Supreme Court of India, Seema Upadhyay v Union of India, W.P.(C) 675/2013, judgment of 5 April 2018, quoting the ministry&rsquo;s affidavit. "
           "Manjunath case: Supreme Court judgment of 11 March 2015 (Indian Kanoon); The Hindu; The Economic Times; Governance Now. Sonawane case: NDTV (29 January 2011); BusinessLine (28 January 2011); Indian Mandarins (8 September 2022, life sentences). "
           "Pipelines: IOCL press release (25 August 2021); ET EnergyWorld (23 February 2017); The New Indian Express and Times of India (2017); The Hindu (10 April 2024, CBI case); The Indian Express (8 January 2025); The Hindu, ET and The Tribune (December 2025); Times of India (July 2026); Mint and National Herald (August 2026). "
           "Diesel pilferage: Deccan Chronicle (6 March 2024, Nalgonda); The Hindu (19 August 2021, Prakasam); ETV Bharat (November 2026, Bemetara, Hindi, snippet only); Free Press Journal (1 January 2024, Mumbai tankers); Times of India (18 September 2025, Goa); The Economic Times (5 December 2025); fuel-sensor vendors Fleetx, Intangles, Taabi and Navionyx (blogs, marketing estimates); The Sentinel (2 May 2025, Ri Bhoi; 22 September 2026, Guwahati); Pratidin Time (June 2026) and Northeast Frontier Railway posts (April 2025); Amar Ujala (31 July 2026, Jhansi, Hindi, snippet only); OdishaTV (May 2026, Talcher); Lok Sabha unstarred question 3511, Ministry of Coal (17 March 2021). "
           "Pumps: Lok Sabha unstarred question 147 (17 July 2017) and ET EnergyWorld (18 July 2017); Hindustan Times (2017); Allahabad High Court (2017); IOCL citizen&rsquo;s charter; Marketing Discipline Guidelines 2012 and 2024, as summarised in search results (the guideline PDFs were not opened). "
           "Biodiesel: Rajya Sabha unstarred question 945 (6 December 2021); Earth Journalism Network (August 2021); Gujarat press reports (2020&ndash;21). "
           "Diesel gap, Bengaluru case, ethanol prices and petrol volumes: earlier posts on this blog and the sources they cite. Energy arithmetic is this blog&rsquo;s (builder in the repository at out/research/fuel-theft/). "
           "Government and court pages were read through search-engine text, not opened directly. Arrests and police estimates are allegations, not findings of guilt.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/indias-petroleum-act-still-fines.html", "India&rsquo;s Petroleum Act Still Fines a Licence Breach &#8377;1,000. The Draft Fix Goes to &#8377;5 Crore"),
    ("https://masaladeutsch.blogspot.com/2026/08/diesel-doesnt-move-cpi-it-moves-40.html", "From Diesel to CNG: Where the Switch Actually Pays"),
    ("https://masaladeutsch.blogspot.com/2026/11/e20-and-spark-plug-what-ethanol-does-to.html", "E20 and the Spark Plug: What Ethanol Does to the Cheapest Part in India&rsquo;s 20 Crore Two-Wheelers"),
    ("https://masaladeutsch.blogspot.com/2026/10/petrol-pump-margins-and-e20-one-dealer.html", "Petrol-Pump Margins and E20: The First Dealer Raise in Seven Years"),
    ("https://masaladeutsch.blogspot.com/2026/09/mapping-indias-other-pipelines-every.html", "Mapping India&rsquo;s Other Pipelines: Every Major Crude, Petrol-Diesel and LPG Line, By Company"),
    ("https://masaladeutsch.blogspot.com/2026/08/scan-bottle-deliver-what-ppacs-numbers.html", "Scan, Bottle, Deliver: What PPAC&rsquo;s Numbers Say About the LPG Cylinder in Your Kitchen"),
]

build("Fuels · Crime · 8 November 2026",
      "From Kerosene in Diesel to Ethanol in Petrol: A History of Fuel Theft in India",
      "For decades the fraud was ration-shop kerosene poured into diesel. Then came pipeline taps, dispenser chips and fake biodiesel. Now Karnataka says its petrol holds up to 31% ethanol, and the oil companies say its tests are wrong.",
      body, sources, related, OUT)
print("above", len(ABOVE), "outband", len(OUT_HI), "mean_above", round(MEAN_ABOVE, 2), "per_pt", round(PER_POINT, 3), "ratio", round(RATIO, 2),
      "loss_mean", round(LOSS_MEAN, 2), "loss_max", round(LOSS_MAX, 2), "e20_vs_e0", round(LOSS_E20_VS_E0, 2),
      "alt_cr", round(ALT_MEAN_CR), "india_petrol_cr_L", round(INDIA_PETROL_CR_L))

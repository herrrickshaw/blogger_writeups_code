import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-compostable-garbage-bags.html'

# --- Stray animals: Rajya Sabha starred question 190 (6 August 2025), 20th Livestock Census (2019)
STRAY_CATTLE = 5021587   # printed as 50,21,587 in the text
STRAY_DOGS = 15309355
STATES = [  # top ten states by stray cattle, same table
    ("Rajasthan", 1272277), ("Uttar Pradesh", 1184494), ("Madhya Pradesh", 853971),
    ("Gujarat", 343918), ("Chhattisgarh", 184993), ("Maharashtra", 152565),
    ("Odisha", 151703), ("Punjab", 140069), ("Haryana", 127917), ("West Bengal", 98733),
]
TOP3 = sum(v for _, v in STATES[:3])
TOP3_SH = TOP3 / STRAY_CATTLE * 100
assert round(TOP3 / 1e5, 1) == 33.1 and round(TOP3_SH) == 66
TOP10_SH = sum(v for _, v in STATES) / STRAY_CATTLE * 100

# --- Compostable makers: CPCB, as reported by Navhind Times
CERT_COMPOST = 371
CERT_BIODEG = 0

# --- Balrampur Chini PLA plant: company press release and results presentation, 4 Nov 2026
PLA_TPA = 80000
PLA_CAPEX_CR = 3080
PLA_SPENT_CR = 2400   # earnings call, spent by 15 October 2026

# --- Waste processing: PIB PRID 2202529; compost plants: PIB note 157131
WASTE_TPD = 162468
PROC_SH = 80.31
UNPROC_TPD = WASTE_TPD * (1 - PROC_SH / 100)
assert round(UNPROC_TPD, -2) == 32000
COMPOST_PLANTS = 2800
COMPOST_TPD = 114000

# --- Temperatures: composting test (ISO 14855, used by ISO 17088) vs rumen-fluid study
COMPOST_C = 58
RUMEN_C = 40

# --- Prices
BAG_RS_KG = 150              # IndiaMART listing, PLA/PBAT garbage bag
PBAT_IN, PBAT_CN = 1777, 1284   # USD/tonne, IMARC, Q2 2026
PBAT_PREM = (PBAT_IN / PBAT_CN - 1) * 100
assert round(PBAT_PREM) == 38

# --- Paper vs bioplastic bags in food-waste digestion (Italy, PubMed 34954688)
PAPER_AD, BIOPL_AD = 82, 27


def lakh(v):
    return f"{v / 1e5:.2f} lakh"


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_vets():
    rows = [
        ("Gaushala in Jaipur, 2015: 63 operations", "7.5&ndash;37.8 kg"),
        ("Haryana study, 2022: 11 stray cattle", "14.5 kg"),
        ("Bengaluru vet college, 2016: 10&ndash;15 a month", "10&ndash;20 kg"),
        ("Orathanadu, Tamil Nadu, 2026: one cow", "48 kg"),
        ("Chennai vet college, 2019: one cow", "52 kg"),
        ("Faridabad, 2021: one cow, which died", "71 kg"),
    ]
    return table(["Where and how many", "Plastic"], rows)


def t_materials():
    rows = [
        ("Ordinary polythene", "Never", "Stays"),
        ("PBAT/starch blend (most &ldquo;compostable&rdquo; bags)", "Plant at 58&deg;C", "Surface only"),
        ("PLA from cane sugar", "Plant at 58&deg;C", "No data"),
        ("Bagasse or kraft paper", "Compost, digester", "Fibre"),
        ("Paper with certified cellulose film", "Home compost", "Fibre, mostly"),
        ("Paper with PE, PVdC or nitro coating", "Not certified", "Coating stays"),
    ]
    return table(["Bag", "Breaks down in", "In a rumen"], rows)


def t_paper():
    rows = [
        ("Plain bagasse or kraft paper", "Weakens when wet"),
        ("Paper with wet-strength resin", "Holds longer; resin is synthetic"),
        ("Paper plus certified cellulose film", "Barrier; costs more"),
        ("Paper plus PE, PVdC or nitro coating", "Barrier; not compostable"),
    ]
    return table(["Paper bag", "Trade-off"], rows)


def chart_states():
    W, L, R, top, bh, gap = 340, 112, 300, 44, 18, 7
    n = len(STATES)
    H = top + n * (bh + gap) + 22
    mx = STATES[0][1]
    sc = (R - L) / mx
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Stray cattle by state, 20th Livestock Census, in lakh: '
         + ", ".join(f"{st} {v / 1e5:.2f}" for st, v in STATES) + '.">',
         '<text x="4" y="13" font-size="13" fill="#495057">Stray cattle, top ten states</text>',
         '<text x="4" y="30" font-size="11" fill="#6c757d">20th Livestock Census (2019), lakh animals</text>']
    for i, (st, v) in enumerate(STATES):
        y = top + i * (bh + gap)
        w = max(v * sc, 2)
        lab = f"{v / 1e5:.2f}"
        s.append(f'<text x="{L - 6}" y="{y + bh / 2 + 4:.1f}" font-size="12" fill="#212529" text-anchor="end">{st}</text>')
        s.append(f'<rect x="{L}" y="{y}" width="{w:.1f}" height="{bh}" fill="#0b3d6b"/>')
        if w > 50:
            s.append(f'<text x="{L + w - 5:.1f}" y="{y + bh / 2 + 4:.1f}" font-size="12" fill="#fff" text-anchor="end">{lab}</text>')
        else:
            s.append(f'<text x="{L + w + 5:.1f}" y="{y + bh / 2 + 4:.1f}" font-size="12" fill="#212529">{lab}</text>')
    s.append(f'<text x="4" y="{H - 6}" font-size="10.5" fill="#6c757d">Source: Rajya Sabha starred question 190, 6 August 2025</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{STRAY_CATTLE / 1e5:.1f} lakh</b><span>stray cattle counted in the 2019 livestock census, with {STRAY_DOGS / 1e7:.2f} crore stray dogs</span></div>
<div class="gb-stat"><b>7.5&ndash;71 kg</b><span>plastic and other waste taken out of single cows&rsquo; stomachs in Indian veterinary reports</span></div>
<div class="gb-stat"><b>{CERT_COMPOST} vs {CERT_BIODEG}</b><span>makers certified by the pollution control board for compostable plastic, against none for &ldquo;biodegradable&rdquo; plastic</span></div>
<div class="gb-stat"><b>{COMPOST_C}&deg;C vs {RUMEN_C}&deg;C</b><span>the heat a compostable bag is tested at, and the temperature inside a cow&rsquo;s rumen</span></div>
</div>'''

body = f"""{stats}

<p>A cow does not eat a plastic bag because it likes plastic. It eats the vegetable peel, the leftover rice or the stale roti inside, and swallows the bag with it. A dog tears the bag open for the same food and spreads the rest across the road. Change what the bag is made of and the animal will still go for it, because the food is still in it.</p>

<p>That is the case for bin bags made from sugarcane, maize starch or paper, and also its limit. These bags help most when they carry kitchen waste to a composting plant, where they break down along with the food. They help much less when they are dumped on a street corner. And none of them is cattle feed: a cow that swallows a compostable bag still has a bag in its stomach. What keeps plastic out of animals is mostly the bin and the collection lorry, not the bag.</p>

<h2 class="gb-h2">What vets keep finding</h2>
<p>The 2019 livestock census counted 50,21,587 stray cattle, about {STRAY_CATTLE / 1e5:.1f} lakh, and {STRAY_DOGS / 1e7:.2f} crore stray dogs. The government told the Rajya Sabha in August 2025 that both numbers had fallen since 2012, by 3.2% for cattle and 10.7% for dogs. Stray cattle are concentrated: Rajasthan, Uttar Pradesh and Madhya Pradesh hold {TOP3 / 1e5:.1f} lakh of them, about {TOP3_SH:.0f}%, and the ten states in the chart hold {TOP10_SH:.0f}%. The 21st census, which was to count stray cattle by sex, had not published its results when this was written.</p>
{chart_states()}
<p>Veterinary surgeons remove the plastic through an operation called a rumenotomy, which opens the first and largest stomach. The amounts below come from case reports and hospital studies. They are not a national survey and say nothing about how common this is, only how bad it gets.</p>
{t_vets()}
<p>Plastic in the rumen does not pass. It knots with cloth, rope and hair into a mass that takes up the space food should fill, so the animal eats less, loses weight and gives less milk. In the Faridabad case reported in 2021, the cow and her calf both died.</p>

<h2 class="gb-h2">What a bin bag can be made of</h2>
<p>&ldquo;Biodegradable&rdquo; bags in Indian shops are mostly not what the word suggests. The pollution control board has certified {CERT_COMPOST} makers of compostable plastic and none of biodegradable plastic, and an Indian Railways tender correction notes that no certified biodegradable plastic is available. Most bags sold as green are compostable plastic: usually PBAT, a fossil-based polyester that compost microbes can break down, blended with starch or PLA. PLA is made by fermenting sugar. Balrampur Chini is building India&rsquo;s first large PLA plant, {PLA_TPA:,} tonnes a year for about &#8377;{PLA_CAPEX_CR:,} crore, and had spent about &#8377;{PLA_SPENT_CR:,} crore by mid-October 2026.</p>
{t_materials()}
<p class="gb-note">&ldquo;In a rumen&rdquo; is this blog&rsquo;s summary of the evidence below, not a feeding test. PE is polyethylene; PVdC and nitrocellulose are coatings used on cellophane.</p>
<p>The useful question is not &ldquo;is it biodegradable?&rdquo; but &ldquo;under what conditions?&rdquo; Compostable plastic is tested for the Indian standard, IS/ISO 17088, in an industrial composting test held near {COMPOST_C}&deg;C for weeks. A cow&rsquo;s rumen sits near {RUMEN_C}&deg;C, and feed usually spends a day or two there. In one laboratory study, small pieces of PBAT film soaked in cattle rumen fluid at {RUMEN_C}&deg;C developed grooves on the surface within a day and released some breakdown products over 72 hours. The microbes attacked the surface; they did not make the film disappear. PLA stays rigid at body temperature, and this piece found no study of it in a rumen.</p>
<p>No study was found in which cattle were fed compostable bags and followed. The honest summary is that a compostable bag probably wears away faster in a stomach than polythene does, and probably not fast enough to matter for a cow that swallows several.</p>

<h2 class="gb-h2">Paper and cellulose film: the bag a rumen can work on</h2>
<p>Paper is different, because it is cellulose, the same fibre as grass and straw. Ruminants are built to digest cellulose, and waste paper has been studied as cattle and sheep feed since the 1970s. The FAO&rsquo;s feed database puts the digestibility of newsprint at about 30%, brown wrapping paper and cardboard at 40&ndash;60%, and paper made from chemical pulp at up to 98%. Kraft paper and bagasse paper are chemical pulps, so they sit at the digestible end. That does not make a paper bag safe food. The same database notes that rations with 12&ndash;15% paper cut how much cattle ate, and in a 1979 trial lead from coloured inks built up in the tissues of sheep fed magazines and newsprint. Paper bags can also carry wet-strength resin, glue, printing ink and coatings. The fair claim is narrower: of all the bin bags on offer, plain paper is the one a rumen can break down, and the one most likely to pass if a cow swallows it.</p>
<p>The problem with paper is water. Kitchen waste in India is wet, and plain paper softens as it soaks. Makers deal with this in three ways, and each one costs something.</p>
{t_paper()}
<p><b>Coatings decide compostability.</b> Cellophane is regenerated cellulose: wood or other pulp dissolved and cast into a clear film. Futamura, a major maker, says its NatureFlex films are certified home-compostable, while its standard Cellophane is not. The coatings that make cellophane waterproof, PVdC and nitrocellulose, are what remove the compostable label. A paper bag laminated with polythene is in effect a plastic bag with a paper face.</p>
<p><b>Feedstock and chemistry.</b> Paper from sugarcane bagasse is an old Indian industry. Tamil Nadu Newsprint and Papers uses about 10 lakh tonnes of bagasse a year and has about 4 lakh tonnes of paper capacity; it says it has run trials of PLA-coated board. Pakka makes bagasse packaging and says one of its flexible products passed the ISO 17088 compostability test at CIPET. Film is harder. Regenerated cellulose film and viscose fibre are made by the viscose process, which uses carbon disulphide, a toxic solvent that has to be captured and recycled. Lyocell, which dissolves pulp in a recoverable solvent called NMMO, is the cleaner route. Bagasse is a poor source of the very pure &ldquo;dissolving&rdquo; pulp those processes need, because of its pith, silica and short fibres. This piece found no Indian company making cellophane or film-grade dissolving pulp from bagasse at commercial scale.</p>
<p><b>Evidence from bin systems that use paper.</b> Sweden, Norway and Italy collect food waste separately, and their studies favour paper. In an Italian test that fed bags into a digester along with food waste, the way a real plant runs, paper bags broke down by about {PAPER_AD}%, compostable-plastic bags by under {BIOPL_AD}%, and pieces of the plastic bags were left over. A Norwegian life-cycle study published in 2026 found that paper bags in separate bins gave the lowest climate impact for both composting and digestion, and called paper the only option likely to remove the risk of plastic in the soil. A Swedish study found paper bags were the most common bag households used for food waste.</p>
<p><b>Cost.</b> Compostable PLA/PBAT garbage bags are listed online at about &#8377;{BAG_RS_KG} a kilogram. PBAT resin cost about ${PBAT_IN:,} a tonne in India in the second quarter of 2026, about {PBAT_PREM:.0f}% more than in China, according to IMARC. Pakka says its compostable packaging costs two to three times plastic. No reliable Indian price for cellulose film or film-laminated paper bags was found.</p>
<p>So the answer to the question &ldquo;which bin bag is kindest to an animal that finds it?&rdquo; is probably bagasse or kraft paper, with either no coating or a certified compostable cellulose film, and printed little or not at all. That holds only if it lasts a day of wet waste without tearing, which is the part nobody has tested for Indian kitchens.</p>

<h2 class="gb-h2">What the rules say</h2>
<p>Under the Plastic Waste Management Rules, plastic carry bags must be at least 120 microns thick. Compostable plastic bags are exempt from the thickness rule, but must meet IS/ISO 17088 and their makers need a pollution control board certificate. Since 2024 the rules define &ldquo;biodegradable plastic&rdquo; as plastic that breaks down in the open environment without leaving microplastics, a standard no product has yet been certified against. The rules do not say clearly whether a thin conventional garbage bag, as distinct from a carry bag, is allowed; Delhi&rsquo;s municipal bye-laws of 2024 explicitly allow them. Paper is not plastic under the rules. Whether a cellulose-film bag, or paper coated with one, counts as plastic is not settled by the text: the definition of plastic turns on whether a &ldquo;high polymer&rdquo; is an essential ingredient, and regenerated cellulose is a polymer.</p>
<p>The Solid Waste Management Rules, 2026, in force from 1 April 2026, matter more for animals. They make it compulsory to separate waste at home into four streams: wet, dry, sanitary and special care. Wet waste is to go to composting or biogas. Bulk generators, such as large housing societies, offices and institutions, have to process their own wet waste or pay for it to be processed.</p>

<h2 class="gb-h2">Why the bin matters more than the bag</h2>
<p>An animal gets to a bag at the place where waste sits uncovered: an open bin, a roadside collection point, a dump. A bag that goes from a kitchen into a closed lorry and then into a compost plant never meets a cow, whatever it is made of. A bag that is left on a street corner meets one, whatever it is made of.</p>
<p>India&rsquo;s cities produced about 1,62,468 tonnes of waste a day, and the government says {PROC_SH}% is processed, which leaves about {UNPROC_TPD / 1000:.0f},000 tonnes a day that is not. The country has about {COMPOST_PLANTS:,} compost plants with capacity of about {COMPOST_TPD / 1e5:.2f} lakh tonnes a day. A compostable bag only works as intended if it reaches one of them. Sent to a dump or a landfill, it behaves much like a plastic bag for months.</p>
<p>That is why the bag question comes second. Separate wet waste, collect it daily in closed vehicles, keep animals away from collection points, and then a compostable or paper bag finishes the job by keeping the compost free of plastic. Without those steps, a greener bag mainly changes what the animal swallows.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>Make wet-waste collection daily and in closed vehicles first, and remove open roadside collection points in the districts with the most stray cattle, starting with Rajasthan, Uttar Pradesh and Madhya Pradesh.</li>
<li>Where cities ask households to bag wet waste, specify paper or certified compostable bags for that stream only, and send that stream to composting or biogas plants that accept bags.</li>
<li>Have the Bureau of Indian Standards write a wet-strength test for paper bin bags under Indian kitchen conditions, so cities can buy paper bags that actually last a day.</li>
<li>Clarify in the plastic rules how paper bags coated with cellulose film are classed, and that polythene-laminated paper is plastic.</li>
<li>Fund one controlled study, through a veterinary university, of what happens to compostable-plastic and paper bags in a cow&rsquo;s rumen, instead of relying on makers&rsquo; claims.</li>
<li>Publish the rumenotomy counts that veterinary colleges and gaushalas already keep, so the scale of the problem is measured rather than reported case by case.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>No study was found in which cattle or dogs ate compostable-plastic, paper or cellulose-film bags and were followed afterwards; the rumen evidence is one laboratory study of PBAT film, and the paper evidence comes from feeding trials of shredded paper, not bags. No data were found on how often dogs swallow bags, as opposed to tearing them. How long a paper or film-laminated bag holds Indian wet kitchen waste was not established. No price for cellulose film or film-laminated paper bags in India was found, and no Indian maker of cellophane or film-grade dissolving pulp from bagasse was confirmed. The rules do not say clearly how cellulose-film or coated-paper bin bags are classified, or whether thin conventional garbage bags are legal outside cities whose bye-laws allow them. Indian starch-bag makers&rsquo; claims that their bags are safe if animals eat them rest on company statements. The stray counts are from 2019; the 21st Livestock Census results were not yet published. The rumenotomy figures are individual reports, not a national rate.</p>
"""

sources = ("Stray animals: <a href=\"https://sansad.in/getFile/annex/268/AS190_myEi4A.pdf\">Rajya Sabha starred question 190, 6 August 2025</a> (20th Livestock Census). "
           "Rumenotomies: <a href=\"https://indianjournals.com/article/ijvs-38-1-017\">Indian Journal of Veterinary Surgery 38(1), Hingonia gaushala, Jaipur</a>; "
           "<a href=\"https://www.luvas.edu.in/haryana-veterinarian/download/harvet2022-march/45.pdf\">Haryana Veterinarian, March 2022</a>; "
           "<a href=\"https://epubs.icar.org.in/index.php/IJVASR/article/view/181151\">Indian Journal of Veterinary and Animal Sciences Research, 2026</a> (Orathanadu); "
           "<a href=\"https://www.thehindu.com/sci-tech/science/tamil-nadu-veterinary-university-surgeons-remove-52-kg-of-plastic-from-cow-in-chennai/article29746204.ece\">The Hindu, 2019</a> (Chennai); "
           "<a href=\"https://cebudailynews.inquirer.net/366113/71kg-of-waste-found-in-stray-indian-cows-stomach\">AFP via Cebu Daily News, 2021</a> (Faridabad); "
           "<a href=\"https://timesofindia.indiatimes.com/city/bengaluru/digest-this-cattle-end-up-eating-most-of-citys-dumped-plastic-on-streets/articleshow/53589685.cms\">Times of India, 2016</a> (Bengaluru). "
           "Rumen fluid and PBAT: <a href=\"https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2021.684459/full\">Frontiers in Bioengineering and Biotechnology, 2021</a>. "
           "Certification: <a href=\"https://navhindtimes.in/goanews/central-pollution-control-board-flags-misuse-of-biodegradable-compostable-product-labels/\">Navhind Times on CPCB&rsquo;s certified makers</a>; "
           "<a href=\"https://ireps.gov.in/ireps/upload/files/107207241/5430212.pdf\">Indian Railways correction slip</a>. "
           "Plastic rules: <a href=\"https://aagarg.in/wp-content/uploads/2026/04/MoEFCC-Consolidated-PWM-Rules-2016-with-Amendments-31.03.2026-A2G-Final-Amendments-till-date-2-1.pdf\">consolidated Plastic Waste Management Rules to 31 March 2026</a> (unofficial compilation); "
           "<a href=\"https://mpcb.mizoram.gov.in/uploads/attachments/2024/05/01b37c7f684d774ee9dde252f1a7bce3/plastic-waste-management-rules-amalgamating-up-to-2024.pdf\">amalgamated rules to 2024, Mizoram PCB</a>; "
           "<a href=\"https://www.indianchemicalcouncil.com/docs/notifications/271465-Plastic%20Waste%20Management%20(Amendment)%20Rules,%202026.pdf\">2026 amendment gazette</a>; "
           "<a href=\"https://mcdonline.nic.in/portal/downloadFile/pwm_byelaws_2024_240216075150250.pdf\">MCD plastic waste bye-laws, 2024</a>. "
           "Waste rules and processing: <a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2219676\">PIB, 28 January 2026</a>; "
           "<a href=\"http://swmp.cpcb.gov.in/en\">CPCB solid waste portal</a>; "
           "<a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2202529\">PIB on waste processed</a>; "
           "<a href=\"https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=3&amp;NoteId=157131&amp;lang=2&amp;reg=48\">PIB note on compost plants</a>. "
           "PLA plant: <a href=\"https://nsearchives.nseindia.com/corporate/SUNILBCML_04112026183706_BCML_Pressrelease_041126.pdf\">Balrampur Chini press release, 4 November 2026</a>; "
           "<a href=\"http://chini.com/wp-content/uploads/2026/11/BCML_ResultPresentation_04112026.pdf\">results presentation</a>; "
           "<a href=\"https://stockanalysis.com/quote/nse/BALRAMCHIN/transcripts/730720-q2-26-27/\">earnings call transcript</a>. "
           "Prices: <a href=\"https://www.indiamart.com/proddetail/compostable-and-biodegradable-garbage-bag-pla-pbat-2858433675330.html\">IndiaMART listing</a>; "
           "<a href=\"https://www.imarcgroup.com/polybutylene-adipate-terephthalate-resin-pricing-report\">IMARC PBAT pricing report</a> (search text); "
           "<a href=\"https://pakka.com/blog/pakkas-sugarcane-revolution-can-it-make-compostable-packaging-mainstream\">Pakka blog</a>. "
           "Paper and cellulose: <a href=\"https://feedipedia.review.fao.org/node/63\">Feedipedia on paper as feed</a>; "
           "<a href=\"https://pubmed.ncbi.nlm.nih.gov/8002470\">newsprint fed to lambs</a>; "
           "<a href=\"https://pubmed.ncbi.nlm.nih.gov/118844\">lead in sheep fed coloured paper</a> and <a href=\"https://www.osti.gov/biblio/5376860\">OSTI record</a>; "
           "<a href=\"https://pubmed.ncbi.nlm.nih.gov/34954688\">Italian digestion test of paper and bioplastic bags</a>; "
           "<a href=\"https://pubmed.ncbi.nlm.nih.gov/41964292\">Norwegian life-cycle study, 2026</a>; "
           "<a href=\"https://www.sciencedirect.com/science/article/pii/S0956053X16301994\">Swedish household bag study</a>; "
           "<a href=\"https://www.futamuragroup.com/resources/faqs/\">Futamura FAQ</a>; "
           "<a href=\"https://www.mdpi.com/2079-6439/13/1/3\">MDPI Fibers review of viscose and lyocell</a>; "
           "<a href=\"https://www.livabybirlacellulose.com/livacms/uploads/sustainabilityinsights/case-studies/Closed-loop%20Technologies%20for%20Viscose%20Process.pdf\">Birla Cellulose case study on closed-loop viscose</a>; "
           "<a href=\"https://ippta.co/wp-content/uploads/2021/01/IPPTA-CI-1994-1-5-Depithed-Bagasse-Future.pdf\">IPPTA paper on bagasse pulp</a>; "
           "<a href=\"https://tnpl.com/manufacturing/\">TNPL manufacturing page</a> and <a href=\"https://nsearchives.nseindia.com/corporate/TNPL_05092024221651_44thAR202324CSDSC.pdf\">annual report 2023-24</a>; "
           "<a href=\"https://pakka.com/our-products\">Pakka products</a> and <a href=\"https://pakka.com/product-category/food-packaging\">food packaging page</a>. "
           "Shares, unprocessed tonnage and the price premium are this blog&rsquo;s arithmetic (builder at out/research/compostable-bags/).")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/sugarcanes-third-claimant-whats.html", "Sugarcane&rsquo;s Third Claimant: What&rsquo;s Actually Being Fermented Into India&rsquo;s First PLA Plant"),
    ("https://masaladeutsch.blogspot.com/2026/09/tnpl-has-made-paper-from-sugarcane.html", "TNPL Has Made Paper From Sugarcane Waste Since 1984. Its Own Industry Lobby Is Asking For Trees."),
    ("https://masaladeutsch.blogspot.com/2026/10/bagasse-is-one-crop-residue-already.html", "Bagasse Is the One Crop Residue Already Sitting at a Factory Gate. Labs Have Liquefied and Hydrolysed It. Nobody Has Priced It Against the Boiler"),
    ("https://masaladeutsch.blogspot.com/2026/08/india-will-finance-waste-to-energy.html", "India Will Finance a Waste-to-Energy Plant Before It Finances a Sorting Line"),
    ("https://masaladeutsch.blogspot.com/2026/07/the-recycling-lottery-playbook-norways.html", "The Recycling Lottery Playbook &mdash; Norway&rsquo;s Pantelotteriet, and a Jal Jeevan Application"),
]

build("Plastics &amp; Waste &middot; 10 November 2026",
      "India Has 50 Lakh Stray Cattle and 371 Certified Compostable-Bag Makers. The Bin Matters More Than the Bag",
      "Bags made from sugarcane, starch or paper help when they carry kitchen waste to a compost plant. None of them is cattle feed, and a cow that finds food in one swallows the bag anyway. Paper is the bag a rumen can best handle, but only a closed bin and a daily lorry keep animals out of the waste.",
      body, sources, related, OUT)
print("top3", TOP3, round(TOP3_SH, 1), "top10", round(TOP10_SH, 1), "unproc", round(UNPROC_TPD), "pbat prem", round(PBAT_PREM, 1))

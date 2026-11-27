#!/usr/bin/env python3
"""Build a single Markdown summary of every published VertiStrat post:
title, date, topic labels, and its own standfirst (the human-written
one-paragraph summary every post already carries) -- not a re-summarised
or AI-generated blurb, the actual published lede.

Also compiles a Units reference and a Glossary of terms/abbreviations,
scanned across the corpus and matched against a curated definition list --
only terms actually present in the current posts are printed.
"""
import glob, html, json, pathlib, re, sys, collections, datetime, urllib.request, urllib.error

# Resolved from this file's location, not hardcoded: the daily chain in
# MAINTENANCE.md used to be runnable only from one laptop. Kept a str, not a
# Path -- every use below is an f-string join.
ROOT = str(pathlib.Path(__file__).resolve().parent.parent)
OUT_PATH = f'{ROOT}/VERTISTRAT_ALL_POSTS_SUMMARY.md'
SKIP_SLUGS = {'article-index-start-here', 'about-author', 'the-masala-deutsch-shop-books-things'}

sys.path.insert(0, f'{ROOT}/tools')
from extract_post import extract

# unit token -> plain-English definition. Only emitted if actually found in the corpus.
UNIT_DEFS = collections.OrderedDict([
    ('crore', 'Indian numbering unit = 1,00,00,000 = 10 million'),
    ('lakh', 'Indian numbering unit = 1,00,000 = 100,000'),
    ('bn', 'billion = 1,000,000,000'),
    ('billion', 'billion = 1,000,000,000'),
    ('mn', 'million = 1,000,000'),
    ('million', 'million = 1,000,000'),
    ('trillion', 'trillion = 1,000,000,000,000'),
    ('%', 'percent, parts per hundred'),
    ('mt', 'million tonnes (also used for metric tonne in some contexts — check the surrounding sentence)'),
    ('lmt', 'lakh metric tonnes = 100,000 tonnes'),
    ('ktpa', 'kilotonnes per annum = 1,000 tonnes/year'),
    ('mmtpa', 'million metric tonnes per annum'),
    ('tpa', 'tonnes per annum'),
    ('tonnes', 'metric tonne = 1,000 kg'),
    ('tonne', 'metric tonne = 1,000 kg'),
    ('kg', 'kilogram'),
    ('bpd', 'barrels per day — a crude oil / fuel flow-rate unit'),
    ('gw', 'gigawatt — power capacity (10⁹ watts)'),
    ('gwh', 'gigawatt-hour — energy generated/consumed'),
    ('mw', 'megawatt — power capacity (10⁶ watts)'),
    ('mwh', 'megawatt-hour — energy generated/consumed'),
    ('twh', 'terawatt-hour — energy generated/consumed, national-grid scale'),
    ('kwh', 'kilowatt-hour — energy generated/consumed'),
    ('km', 'kilometre'),
    ('litres', 'volume unit (1 litre = 1,000 cm³)'),
    ('litre', 'volume unit (1 litre = 1,000 cm³)'),
    ('acres', 'land area unit (1 acre ≈ 0.405 hectares)'),
    ('hectares', 'land area unit (1 hectare = 2.47 acres)'),
])

# abbreviation -> plain-English definition. Only emitted if actually found in the corpus.
GLOSSARY_DEFS = {
    'AI': 'Artificial Intelligence',
    'PIB': 'Press Information Bureau — Government of India\'s official press-release agency',
    'US': 'United States',
    'PLI': 'Production-Linked Incentive scheme',
    'HS': 'Harmonized System — the international goods-classification code standard',
    'HSN': 'Harmonized System of Nomenclature — India\'s HS-derived tariff/trade code',
    'DGCI': 'Directorate General of Commercial Intelligence (and Statistics) — see DGCIS',
    'DGCIS': 'Directorate General of Commercial Intelligence and Statistics — India\'s trade-data authority',
    'RBI': 'Reserve Bank of India',
    'PPAC': 'Petroleum Planning and Analysis Cell — Ministry of Petroleum & Natural Gas data unit',
    'CPI': 'Consumer Price Index',
    'EU': 'European Union',
    'CBG': 'Compressed Bio-Gas',
    'DPIIT': 'Department for Promotion of Industry and Internal Trade',
    'EV': 'Electric Vehicle',
    'WPI': 'Wholesale Price Index',
    'LNG': 'Liquefied Natural Gas',
    'CNG': 'Compressed Natural Gas',
    'CAGR': 'Compound Annual Growth Rate',
    'OMC': 'Oil Marketing Company (e.g. IOCL, BPCL, HPCL)',
    'API': 'Application Programming Interface (or, in petroleum contexts, American Petroleum Institute gravity)',
    'FY': 'Fiscal Year (India: 1 April – 31 March)',
    'DAP': 'Di-Ammonium Phosphate — a phosphatic fertiliser',
    'PM': 'Prime Minister, or Particulate Matter, depending on context',
    'LPG': 'Liquefied Petroleum Gas',
    'DGFT': 'Directorate General of Foreign Trade',
    'BPCL': 'Bharat Petroleum Corporation Limited',
    'VAT': 'Value Added Tax',
    'MT': 'Million Tonnes',
    'FCI': 'Food Corporation of India',
    'USD': 'United States Dollar',
    'FTA': 'Free Trade Agreement',
    'GST': 'Goods and Services Tax',
    'CGD': 'City Gas Distribution',
    'BIS': 'Bureau of Indian Standards',
    'GDP': 'Gross Domestic Product',
    'INR': 'Indian Rupee',
    'UAE': 'United Arab Emirates',
    'PDS': 'Public Distribution System',
    'IOCL': 'Indian Oil Corporation Limited',
    'EC': 'Environmental Clearance',
    'MMT': 'Million Metric Tonnes',
    'FDI': 'Foreign Direct Investment',
    'USA': 'United States of America',
    'DFPD': 'Department of Food and Public Distribution',
    'PSU': 'Public Sector Undertaking',
    'EIDB': 'Ethanol Interest-subvention/incentive scheme reference (Ethanol Infrastructure Development Bank/scheme, check source article)',
    'NITI': 'NITI Aayog — National Institution for Transforming India (government policy think tank)',
    'COVID': 'COVID-19 pandemic',
    'MITRA': 'Mega Investment Textiles Parks scheme (or context-specific — check article)',
    'PTA': 'Purified Terephthalic Acid (a petrochemical), or Preferential Trade Agreement, depending on context',
    'PNGRB': 'Petroleum and Natural Gas Regulatory Board',
    'MSME': 'Micro, Small and Medium Enterprises',
    'SATAT': 'Sustainable Alternative Towards Affordable Transportation — India\'s CBG scheme',
    'EBP': 'Ethanol Blended Petrol programme',
    'PARIVESH': 'Government of India\'s online environmental-clearance portal',
    'GAIL': 'Gas Authority of India Limited',
    'FX': 'Foreign Exchange',
    'RIL': 'Reliance Industries Limited',
    'LMT': 'Lakh Metric Tonnes (100,000 tonnes)',
    'IEM': 'Industrial Entrepreneurs Memorandum',
    'CAG': 'Comptroller and Auditor General of India',
    'SEBI': 'Securities and Exchange Board of India',
    'IPR': 'Import Penetration Ratio, or Intellectual Property Rights, depending on context',
    'IIP': 'Index of Industrial Production',
    'SAF': 'Sustainable Aviation Fuel',
    'REC': 'Renewable Energy Certificate, or Rural Electrification Corporation, depending on context',
    'PET': 'Polyethylene Terephthalate (plastic resin)',
    'MMTPA': 'Million Metric Tonnes Per Annum',
    'PP': 'Polypropylene',
    'MSP': 'Minimum Support Price',
    'ICIS': 'Independent Commodity Intelligence Services — petrochemical/commodity price data provider',
    'EPR': 'Extended Producer Responsibility',
    'NMEO': 'National Mission on Edible Oils',
    'FOB': 'Free On Board — a trade/shipping price basis',
    'CPCB': 'Central Pollution Control Board',
    'IMARC': 'IMARC Group — a market-research/consulting firm cited as a source',
    'IPO': 'Initial Public Offering',
    'NCDC': 'National Cooperative Development Corporation',
    'PMKSY': 'Pradhan Mantri Krishi Sinchayee Yojana — irrigation scheme',
    'MNRE': 'Ministry of New and Renewable Energy',
    'IREDA': 'Indian Renewable Energy Development Agency',
    'CCTS': 'Carbon Credit Trading Scheme',
    'PFC': 'Power Finance Corporation',
    'TPA': 'Tonnes Per Annum',
    'KTPA': 'Kilotonnes Per Annum',
    'LLDPE': 'Linear Low-Density Polyethylene',
    'HDPE': 'High-Density Polyethylene',
    'APM': 'Administered Price Mechanism (natural gas pricing)',
    'HSD': 'High-Speed Diesel',
    'MMF': 'Man-Made Fibre',
    'MEG': 'Mono Ethylene Glycol (a petrochemical)',
    'HPCL': 'Hindustan Petroleum Corporation Limited',
    'CBAM': 'Carbon Border Adjustment Mechanism — EU carbon tariff',
    'CEEW': 'Council on Energy, Environment and Water — an Indian policy research institute',
    'BRICS': 'Brazil, Russia, India, China, South Africa (economic bloc)',
    'UDAN': 'Ude Desh ka Aam Naagrik — regional air connectivity scheme',
    'FAME': 'Faster Adoption and Manufacturing of (Hybrid &) Electric vehicles scheme',
    'IBEF': 'India Brand Equity Foundation',
    'ONGC': 'Oil and Natural Gas Corporation',
    'NSE': 'National Stock Exchange (of India)',
    'BSE': 'Bombay Stock Exchange',
    'SIAM': 'Society of Indian Automobile Manufacturers',
    'AHIDF': 'Animal Husbandry Infrastructure Development Fund',
    'NABARD': 'National Bank for Agriculture and Rural Development',
    'UPI': 'Unified Payments Interface',
    'MDR': 'Merchant Discount Rate',
    'SBI': 'State Bank of India',
    'NBFC': 'Non-Banking Financial Company',
    'RLNG': 'Regasified Liquefied Natural Gas',
    'ESG': 'Environmental, Social and Governance (investing/reporting framework)',
    'IRR': 'Internal Rate of Return',
    'NHAI': 'National Highways Authority of India',
    'EPC': 'Engineering, Procurement and Construction (contract model)',
    'MMSCM': 'Million Metric Standard Cubic Metres (natural gas volume)',
    'ICRA': 'ICRA Limited — an Indian credit rating agency',
    'IGST': 'Integrated Goods and Services Tax (inter-state GST)',
    'CGST': 'Central Goods and Services Tax',
    'BCD': 'Basic Customs Duty',
    'EFTA': 'European Free Trade Association',
    'TEPA': 'Trade and Economic Partnership Agreement (India-EFTA)',
    'NPK': 'Nitrogen-Phosphorus-Potassium (a fertiliser grade)',
    'CACP': 'Commission for Agricultural Costs and Prices',
    'SFAC': 'Small Farmers\' Agri-Business Consortium',
    'FPO': 'Farmer Producer Organisation',
    'CWC': 'Central Warehousing Corporation',
    'EIA': 'U.S. Energy Information Administration',
    'GCC': 'Gulf Cooperation Council',
    'APEDA': 'Agricultural and Processed Food Products Export Development Authority',
    'PMFME': 'Pradhan Mantri Formalisation of Micro Food Processing Enterprises scheme',
    'CDSCO': 'Central Drugs Standard Control Organisation',
    'NAFED': 'National Agricultural Cooperative Marketing Federation of India',
    'CGST': 'Central Goods and Services Tax',
    'TPD': 'Tonnes Per Day',
    'CSE': 'Centre for Science and Environment',
    'CII': 'Confederation of Indian Industry',
    'NPCI': 'National Payments Corporation of India',
    'FCO': 'Fertiliser Control Order',
    'GHG': 'Greenhouse Gas',
    'ADB': 'Asian Development Bank',
    'JBIC': 'Japan Bank for International Cooperation',
    'PPP': 'Purchasing Power Parity, or Public-Private Partnership, depending on context',
    'REER': 'Real Effective Exchange Rate',
    'TTF': 'Title Transfer Facility — Europe\'s benchmark natural-gas price hub',
    'ATF': 'Aviation Turbine Fuel',
    'WTI': 'West Texas Intermediate — a US crude-oil price benchmark',
    'AIDC': 'Agriculture Infrastructure and Development Cess',
    'CBDC': 'Central Bank Digital Currency',
    'CRZ': 'Coastal Regulation Zone',
    'CBDT': 'Central Board of Direct Taxes',
    'TERI': 'The Energy and Resources Institute',
    'UCO': 'Used Cooking Oil',
    'LOBS': 'Lube Oil Base Stocks',
    'WTO': 'World Trade Organization',
    'FSSAI': 'Food Safety and Standards Authority of India',
    'OPEC': 'Organization of the Petroleum Exporting Countries',
    'EBITDA': 'Earnings Before Interest, Taxes, Depreciation and Amortisation',
    'LDPE': 'Low-Density Polyethylene',
    'GVA': 'Gross Value Added',
    'OECD': 'Organisation for Economic Co-operation and Development',
    'CCEA': 'Cabinet Committee on Economic Affairs',
    'ECB': 'External Commercial Borrowing, or European Central Bank, depending on context',
    'IMF': 'International Monetary Fund',
    'LTCG': 'Long-Term Capital Gains (tax)',
    'KUSUM': 'Kisan Urja Suraksha evam Utthaan Mahabhiyan — solar-for-farmers scheme',
    'PPF': 'Public Provident Fund',
    'SIP': 'Systematic Investment Plan',
    'DAHD': 'Department of Animal Husbandry and Dairying',
    'OMSS': 'Open Market Sale Scheme (FCI grain sales)',
    'MSV': 'Minimum Selling Value/Price (context-dependent — check article)',
    'NFSA': 'National Food Security Act',
    'PMGKAY': 'Pradhan Mantri Garib Kalyan Anna Yojana — free foodgrain scheme',
}

def is_live(url):
    """GET-check a post URL; only treat a confirmed 404/410 as dead.
    Blogger returns 200 on HEAD even for dead posts (custom error page), so a
    real GET is required. Network errors/timeouts are NOT treated as dead --
    we don't want a flaky connection to silently drop real posts."""
    req = urllib.request.Request(url, headers={'User-Agent': 'vertistrat-summary-builder/1.0'})
    try:
        urllib.request.urlopen(req, timeout=8)
        return True
    except urllib.error.HTTPError as e:
        return e.code not in (404, 410)
    except Exception:
        return True

def get_standfirst(raw):
    m = re.search(r'<p class="standfirst">(.*?)</p>', raw, re.S)
    if not m:
        # fallback: first <p> with real sentence-length text, skipping nav/eyebrow
        for pm in re.finditer(r'<p(?:\s[^>]*)?>(.*?)</p>', raw, re.S):
            text = re.sub(r'<[^>]+>', '', pm.group(1))
            text = html.unescape(text).strip()
            text = re.sub(r'\s+', ' ', text)
            if len(text) > 80 and 'All Articles' not in text:
                return text
        return ''
    text = re.sub(r'<[^>]+>', '', m.group(1))
    text = html.unescape(text).strip()
    return re.sub(r'\s+', ' ', text)

UNIT_RE = re.compile(
    r'\b\d[\d,]*(?:\.\d+)?\s*(crore|lakh|bn|billion|mn|million|trillion|MT|LMT|KTPA|MMTPA|TPA'
    r'|tonnes?|kg|bpd|GWh|GW|MWh|MW|TWh|kWh|km|litres?|acres?|hectares?|%)\b',
    re.I)
ABBR_RE = re.compile(r'\b[A-Z]{2,8}\b')

def main():
    posts = []
    corpus_parts = []
    for f in glob.glob(f'{ROOT}/meta/*.json'):
        try:
            meta = json.load(open(f))
        except Exception:
            continue
        slug = meta.get('slug', '')
        if slug in SKIP_SLUGS or not meta.get('url') or not meta.get('published'):
            continue
        if not is_live(meta['url']):
            print(f'skipping dead link: {slug} -> {meta["url"]}', file=sys.stderr)
            continue
        post_file = f'{ROOT}/posts/{slug}.html'
        try:
            raw = open(post_file, encoding='utf-8', errors='ignore').read()
        except FileNotFoundError:
            continue
        standfirst = get_standfirst(raw)
        posts.append({
            'title': meta.get('title', slug),
            'url': meta['url'],
            'published': meta.get('published', '')[:10],
            'labels': meta.get('labels', []),
            'standfirst': standfirst,
        })
        for block in extract(raw):
            if ' | ' not in block:
                corpus_parts.append(block)

    # de-dup by URL (the local archive has a couple of slug collisions)
    seen_urls = set()
    dedup = []
    for p in posts:
        if p['url'] in seen_urls:
            continue
        seen_urls.add(p['url'])
        dedup.append(p)
    posts = dedup
    posts.sort(key=lambda p: p['published'] or '0000-00-00')

    by_label = collections.defaultdict(list)
    for p in posts:
        labels = p['labels'] or ['Unlabelled']
        for l in labels:
            by_label[l].append(p)

    corpus = ' '.join(corpus_parts)
    units_found = sorted({m.group(1).lower() for m in UNIT_RE.finditer(corpus)} & set(UNIT_DEFS))
    abbrs_found = sorted({m.group(0) for m in ABBR_RE.finditer(corpus)} & set(GLOSSARY_DEFS))

    out = []
    out.append('# VertiStrat Solutions — All Posts, Summarised\n')
    out.append(f'*{len(posts)} published posts, {len(by_label)} topic labels. '
                'Each entry is the post\'s own published standfirst — not a re-summary.*\n')
    out.append(f'*Generated {datetime.date.today().strftime("%-d %B %Y")} — regenerated daily by tools/update_summary_cron.sh.*\n')

    out.append('\n## Units & Figures Used in This Blog\n')
    out.append('*A quick reference for the number formats that recur across posts.*\n')
    for u in units_found:
        out.append(f"- **{u}** — {UNIT_DEFS[u]}")

    out.append('\n\n## Glossary of Terms & Abbreviations\n')
    out.append('*Every abbreviation below appears in at least one published post. '
                'Where a term has more than one meaning on the blog, both are noted — check the '
                'surrounding sentence in the source article.*\n')
    for a in abbrs_found:
        out.append(f"- **{a}** — {GLOSSARY_DEFS[a]}")

    out.append('\n\n## By Topic\n')
    for label in sorted(by_label, key=str.lower):
        out.append(f'\n### {label} ({len(by_label[label])})\n')
        for p in sorted(by_label[label], key=lambda p: p['published'] or '', reverse=True):
            out.append(f"- **[{p['title']}]({p['url']})** — {p['published']}"
                        + (f"\n  {p['standfirst']}" if p['standfirst'] else ''))

    out.append('\n\n## Chronological (All Posts)\n')
    for p in posts:
        labels_str = ', '.join(p['labels']) if p['labels'] else '—'
        out.append(f"\n### [{p['title']}]({p['url']})")
        out.append(f"*{p['published']} · {labels_str}*\n")
        out.append(p['standfirst'] or '*(no standfirst found)*')

    text = '\n'.join(out)
    open(OUT_PATH, 'w', encoding='utf-8').write(text)
    print(f'wrote {len(posts)} posts, {len(units_found)} units, {len(abbrs_found)} glossary terms, '
          f'{len(text)} bytes -> {OUT_PATH}')

if __name__ == '__main__':
    main()

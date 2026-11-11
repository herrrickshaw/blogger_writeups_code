#!/usr/bin/env python3
"""Build the two chemical-import merges for Phase 1 (10 Nov 2026)."""
import re, pathlib, sys

ROOT = pathlib.Path("/home/user/blogger_writeups_code")
P = ROOT / "posts"
OUT = ROOT / "out"
B = "https://masaladeutsch.blogspot.com"
U_TOP15 = f"{B}/2026/07/top-15-chemicals-for-import.html"
U_REG = f"{B}/2026/08/chemical-import-substitution-hsn-8-registry.html"
U_TREE = f"{B}/2026/07/indias-petrochemical-import-tree-from.html"
U_PARKS = f"{B}/2026/10/indias-rs-3030-crore-chemical-parks.html"
U_COAL = f"{B}/2026/08/indias-coal-to-chemicals-menu-ranked-by.html"
WARN = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);'
        'padding:.8em 1em;margin:1.2em 0;border-radius:4px">')


def once(t, old, new, label):
    n = t.count(old)
    if n != 1:
        sys.exit(f"{label}: expected 1 match, found {n}")
    return t.replace(old, new)


def repoint(t, slugs, target):
    for s in slugs:
        t = re.sub(r'https://masaladeutsch\.blogspot\.com/\d{4}/\d{2}/' + re.escape(s) + r'\.html', target, t)
    return t


# ---------------------------------------------------------------- merge 1
t = (P / "top-15-chemicals-for-import.html").read_text()
ana = (P / "chemical-import-substitution-analysis.html").read_text()

note1 = WARN + (
    '<b>Updated 10 November 2026.</b> Two companion posts have been folded into this one and retired: '
    '&ldquo;Chemical Import Substitution Analysis: Executive Summary&rdquo; and '
    '&ldquo;Chemical Import Substitution &mdash; Quarterly Tracking Dashboard&rdquo;. '
    'What they carried that this post did not now sits in three new sections: '
    '<a href="#import-base-by-chapter">the import base, chapter by chapter</a> (just below), '
    '<a href="#who-makes-these-chemicals">who makes these chemicals</a>, and '
    '<a href="#quarterly-tracking">quarterly tracking of the projects and trade-remedy cases</a> (after the roadmap). '
    'Their FY30 savings and payback projections had already been retracted and were not carried over. '
    'The tracker reflects the 27 October clearance of BPCL&rsquo;s Andhra Pradesh complex noted below.</div>\n')
first_warn = t.index(WARN + '<b>Updated 7 November 2026.</b>')
t = t[:first_warn] + note1 + t[first_warn:]

# chapter chart from the absorbed summary, with the Chapter 38 label corrected
s = ana.index('<figure class="gb-figure"'); e = ana.index('</figure>', s) + 9
svg = ana[s:e]
svg = once(svg, '<tspan x="596" dy="0">Textile Auxiliaries</tspan><tspan x="596" dy="11.5">(corrected)</tspan>',
           '<tspan x="596" dy="0">Misc. Chemical</tspan><tspan x="596" dy="11.5">Products</tspan>', "svg ch38")
svg = once(svg, 'Ch. 38 corrected per the 4 Aug 2026 correction notice above ($620mn was wrong)',
           'Ch. 38 corrected from an earlier, wrong $620mn', "svg src")
svg = svg.replace('<svg role="img" ', '<svg role="img" aria-label="Bar chart of India\'s FY2025-26 chemical imports by HS chapter, $ billion" ', 1)
svg = once(svg, 'Source: DGCI&S TradeStat EIDB, as tabulated in the post\'s Chemical Import Breakdown table.',
           'Source: DGCI&amp;S TradeStat EIDB, as tabulated in this blog&rsquo;s former executive summary (reconciled 20 August 2026).', "svg cap")

base = f'''<h2 id="import-base-by-chapter">THE IMPORT BASE:
CHAPTER BY CHAPTER</h2>
<p>The fifteen chemicals ranked below are a small part of a much larger bill. Across the five chapter groups this blog has tracked, India imported about <strong>$74.37 billion</strong> of chemical products in FY2025-26. That total is the sum of the chapter rows in the table below, reconciled on 20 August 2026 after the Chapter 38 row was found to be wrong.</p>
{svg}
<div class="tblwrap"><table>
<thead>
<tr>
<th>HS chapter</th>
<th>What it covers</th>
<th>FY2025-26 imports, $ bn</th>
</tr>
</thead>
<tbody>
<tr><td>29</td><td>Organic chemicals (ethylene, propylene, TPA and others)</td><td>25.41</td></tr>
<tr><td>39</td><td>Plastics and polymers (PP, PE, PET)</td><td>22.23</td></tr>
<tr><td>28</td><td>Inorganic chemicals</td><td>14.18</td></tr>
<tr><td>38</td><td>Miscellaneous chemical products, including textile auxiliaries</td><td>8.86</td></tr>
<tr><td>30&ndash;32</td><td>Dyes, pigments and pharmaceuticals</td><td>3.69</td></tr>
<tr><td colspan="2"><strong>Total</strong></td><td><strong>74.37</strong></td></tr>
</tbody>
</table></div>
<p>Three things to know when reading the table:</p>
<ul>
<li><strong>Chapter 38 was understated by 93%.</strong> It was first shown as &ldquo;Textile Auxiliaries, $620mn&rdquo;. DGCI&amp;S puts FY2025-26 Chapter 38 imports at $8,857 million, with a $5.32 billion gross deficit across 77 deficit-running HS-8 lines ($1.74 billion net). Two single lines each exceed the old $620mn figure.</li>
<li><strong>The 30&ndash;32 row has no published breakdown.</strong> The summary it came from did not split it by chapter, and the basis could not be rebuilt. Treat it as indicative.</li>
<li><strong>These are gross imports, not deficits.</strong> The <a href="{U_REG}">827-code HSN-8 registry</a> measures imports minus exports over qualifying codes only, so its $67.9 billion total is lower by design.</li>
</ul>
<p>An earlier version of this table also gave an &ldquo;FY30 substitution&rdquo; range for each chapter. Those ranges fed the retracted savings headline and are not repeated here.</p>
<p style="font-size:.9em;color:#555"><strong>Source for this section</strong>: DGCI&amp;S TradeStat EIDB, FY2025-26 chapter totals, as tabulated in this blog&rsquo;s former executive summary (4 August 2026 correction, 20 August 2026 reconciliation). Not re-pulled for this update.</p>
<hr />
'''
tier1 = '<h2 id="tier-1-load-bearing-chemicals-capex-triggered">TIER 1:\nLOAD-BEARING CHEMICALS (Capex-Triggered)</h2>'
t = once(t, tier1, base + tier1, "tier1 anchor")

producers = '''<h2 id="who-makes-these-chemicals">WHO MAKES THESE CHEMICALS:
INDIA vs GLOBAL</h2>
<h3 id="indian-producers"><strong>Indian producers (Tier 1 chemicals)</strong></h3>
<ul>
<li><strong>Reliance Industries</strong>: about 4.0 MMTPA of chemicals capacity, integrated across PP, PE and PET.</li>
<li><strong>Indian Oil Corporation</strong>: about 1.5 MMTPA, refinery-integrated at Panipat and Mathura.</li>
<li><strong>Bharat Petroleum</strong>: about 0.9 MMTPA, with the Andhra Pradesh greenfield complex to come.</li>
<li><strong>Jindal Polyester</strong>: a TPA and PET specialist, 400+ KTPA.</li>
</ul>
<h3 id="global-suppliers"><strong>Global suppliers to India</strong></h3>
<ul>
<li><strong>Saudi Aramco / SABIC</strong>: 8.0+ MMTPA combined. Reported to supply 35&ndash;40% of India&rsquo;s ethylene and propylene imports.</li>
<li><strong>Sinopec and CNPC (China)</strong>: 6.0+ MMTPA. Reported to supply about 60% of TPA imports and 75% of azo-dye imports (80% for disperse dyes).</li>
<li><strong>ExxonMobil, Dow and LyondellBasell</strong>: the main US and global specialty-polymer competitors.</li>
</ul>
<p style="font-size:.9em;color:#555">These capacities and import shares come from this blog&rsquo;s former executive summary. They are company-level round numbers and were not re-verified for this update. The import shares have not been checked against DGCI&amp;S partner-country data. The TPA share also disagrees with this post: 60% here, 75% in the anti-dumping section above.</p>
<hr />
'''
pcpir = '<h2 id="pcpir-where-the-capacity-lands">'
t = once(t, pcpir, producers + pcpir, "pcpir anchor")

tracking = f'''<h2 id="quarterly-tracking">QUARTERLY TRACKING:
PROJECTS AND TRADE-REMEDY CASES</h2>
<p>Until 10 November 2026 this tracking ran as a separate quarterly dashboard. The figures below are the dashboard&rsquo;s own, as of Q2 FY27 (July&ndash;September 2026), updated only where marked. Its progress percentages were its own estimates, not company disclosures.</p>
<h3 id="tracking-capex-projects"><strong>The four capex projects</strong></h3>
<div class="tblwrap"><table>
<thead>
<tr>
<th>Project</th>
<th>Capex, crore &#8377;</th>
<th>Capacity, KTPA</th>
<th>Target</th>
<th>Progress, % (est.)</th>
</tr>
</thead>
<tbody>
<tr><td>BPCL Andhra Pradesh</td><td>1,45,000*</td><td>Ethylene 350, propylene 280, PP 200</td><td>FY28</td><td>20</td></tr>
<tr><td>RIL O2C expansion</td><td>75,000</td><td>Ethylene 1,200, aromatics 600, glycol 400</td><td>FY29&ndash;30</td><td>35</td></tr>
<tr><td>BPCL Bina LLDPE (L&amp;T EPC)</td><td>600&ndash;1,200</td><td>LLDPE 200&ndash;250</td><td>FY27&ndash;28</td><td>45</td></tr>
<tr><td>BHAVYA chemical parks</td><td>3,030</td><td>No target set</td><td>FY28&ndash;29</td><td>&ndash;</td></tr>
</tbody>
</table></div>
<p style="font-size:.9em;color:#555">* BPCL&rsquo;s September 2026 figure. The clearance filing gives about &#8377;1.03 lakh crore.</p>
<p><strong>Status at 10 November 2026:</strong></p>
<ul>
<li><strong>BPCL Andhra Pradesh (Ramayapatnam).</strong> <em>Updated:</em> environmental and CRZ clearance was reported granted on 27 October 2026. The final investment decision is still pending, and the EPC award waits on it.</li>
<li><strong>RIL O2C expansion.</strong> The dashboard reported land acquisition completed in Q2 FY27, EPC bids under evaluation in Q3 FY27, and an award expected in Q1 FY28. None of this is confirmed in RIL&rsquo;s filings.</li>
<li><strong>BPCL Bina LLDPE.</strong> The dashboard reported swing-reactor design completed in Q1 FY27 and equipment procurement under way. Its FY27&ndash;28 target differs from the FY28&ndash;29 in the capex table above, and BPCL has confirmed neither.</li>
<li><strong>BHAVYA Rasayan parks.</strong> Three parks are to be chosen by a challenge among states, and no sites have been announced. The dashboard&rsquo;s 25% progress figure had no published basis and is not repeated.</li>
</ul>
<p>The four projects add up to <strong>&#8377;2,23,630&ndash;2,24,230 crore</strong> using BPCL&rsquo;s September figure for Andhra Pradesh, or about &#8377;1.82 lakh crore using the clearance-filing figure. The retired summary&rsquo;s &#8377;1,78,630&ndash;1,79,230 crore was based on the earlier &#8377;1,00,000 crore estimate for the same project.</p>
<h3 id="tracking-trade-remedies"><strong>Trade-remedy cases</strong></h3>
<p>Anti-dumping investigations are run by the Directorate General of Trade Remedies (DGTR), which took the function over from DGFT in 2018.</p>
<div class="tblwrap"><table>
<thead>
<tr>
<th>Product (HSN)</th>
<th>As reported</th>
<th>Status found</th>
</tr>
</thead>
<tbody>
<tr>
<td>TPA (29173600)</td>
<td>Investigation initiated March 2026; 15&ndash;20% duty discussed; decision expected August&ndash;September 2026</td>
<td>No final findings or DGTR portal entry located (12 October check). The expected window has passed.</td>
</tr>
<tr>
<td>Azo dyes (cited as 32030010)</td>
<td>Initiated March 2026, in parallel with TPA</td>
<td>The cited code is Cutch/Catechu (about $2 million of imports), not azo dyes. No case located, and its dollar impact was retracted.</td>
</tr>
<tr>
<td>ANTU (29214110?)</td>
<td>Possibly part of a broader organic-intermediates case</td>
<td>Unconfirmed; not located.</td>
</tr>
<tr>
<td>QCO lead (guessed 29071100)</td>
<td>Listed as a case</td>
<td>A BIS quality-control order, not a trade-remedy case; code and status unverified. Excluded.</td>
</tr>
</tbody>
</table></div>
<h3 id="tracking-risks"><strong>Risk register</strong></h3>
<ul>
<li><strong>BPCL Andhra Pradesh, final investment decision.</strong> The clearance risk the dashboard flagged was resolved on 27 October 2026. Commissioning in FY28 now depends on how soon BPCL&rsquo;s board approves the investment; no date has been announced.</li>
<li><strong>The DGTR decision on TPA.</strong> The decision is now overdue against its August&ndash;September window. Without a finding, no duty can take effect in FY27, and domestic producers face import-parity prices without a tariff umbrella.</li>
<li><strong>BHAVYA land.</strong> Sites are still to be chosen by challenge, and land acquisition typically takes 6&ndash;12 months per state. Operation by FY28&ndash;29 is at risk.</li>
<li><strong>The RIL O2C EPC award.</strong> Evaluating EPC bids typically takes 6&ndash;9 months. An award later than Q1 FY28 would push commissioning to FY30&ndash;31.</li>
<li><strong>EPC sourcing.</strong> US&ndash;China trade restrictions could delay equipment by 3&ndash;6 months and raise capex 10&ndash;15%. This is the dashboard&rsquo;s estimate.</li>
</ul>
<h3 id="tracking-next-quarter"><strong>What to watch in Q3 FY27 (October&ndash;December 2026)</strong></h3>
<ul>
<li>BPCL&rsquo;s investment decision on Andhra Pradesh, and detailed design if it is approved.</li>
<li>A DGTR final finding, or a portal entry, for TPA.</li>
<li>The RIL O2C preferred bidder. The dashboard listed 5&ndash;6 bidders in final evaluation.</li>
<li>Bina equipment procurement, which the dashboard expected to reach 80% by December 2026, with installation to start in Q4 FY27.</li>
<li>The BHAVYA challenge results.</li>
<li>PLI disbursements for Q3 FY27, if the Department of Chemicals and Petrochemicals publishes a utilisation report.</li>
</ul>
<p style="font-size:.9em;color:#555"><strong>Sources for this section</strong>: this blog&rsquo;s former quarterly dashboard, which cited SEBI capex disclosures, PIB announcements, the DGTR portal and the Department of Chemicals and Petrochemicals. Also: BPCL&rsquo;s 16 September 2026 statement as reported by <a href="https://www.thehansindia.com/news/cities/amaravati/cm-naidu-for-fast-tracking-of-rs-145-lakh-crore-bpcl-refinery-1122595">The Hans India</a>; the October 2026 clearance recommendation as reported by <a href="https://www.business-standard.com/amp/industry/news/bpcl-s-1-trn-refinery-project-gets-environmental-clearance-recommendation-126100400529_1.html" rel="noopener">Business Standard</a> and <a href="https://newprojectstracker.com/capex-news/bpcls-103-lakh-crore-greenfield-refinery-and-petrochemical-complex-near-ramayapatnam-port-in-nellore-gets-environmental-and-crz-clearance-recommendation" rel="noopener">New Projects Tracker</a>; and the 27 October 2026 clearance as reported by <a href="https://www.deccanchronicle.com/southern-states/andhra-pradesh/bpcls-rs-103-lakh-crore-refinery-gets-environmental-clearance-2000028">Deccan Chronicle</a> (the order itself not seen).</p>
<hr />
'''
related_anchor = '<div style="background:#f8f9fa;border:1px solid #dee2e6;border-radius:12px;padding:1.1rem 1.4rem;margin:1.5rem 0;font-size:.92em"><strong>Related on this blog:</strong>'
t = once(t, related_anchor, tracking + related_anchor, "related anchor")

old_rel_tail = "and why the technology choice (Shell's, not BHEL's indigenous design) is its own story.</div>"
t = once(t, old_rel_tail,
         "and why the technology choice (Shell's, not BHEL's indigenous design) is its own story. "
         f'Also: <a href="{U_REG}">Which of 827 Chemical HSN-8 Codes Are Real Substitution Targets</a>, the full code-by-code registry behind this ranking; '
         f'<a href="{U_TREE}">India&rsquo;s Petrochemical Import Tree &mdash; From Petrol to Product (HSN-coded)</a>; and '
         f'<a href="{U_PARKS}">India&rsquo;s Rs 3,030 Crore Chemical Parks Copy the Bulk-Drug Parks</a>, on the BHAVYA scheme tracked above.</div>',
         "related tail")

# What would fix this: fix duplicate id, add the absorbed posts' unique items
t = once(t, '<h2 id="tier-1-load-bearing-chemicals-capex-triggered">What would fix this</h2>',
         '<h2 id="what-would-fix-this">What would fix this</h2>', "fix h2 id")
dgtr_item_end = "can be confirmed from one primary source.</li>\n</ul>\n<p>These are proposals from this blog"
t = once(t, dgtr_item_end,
         "can be confirmed from one primary source.</li>\n"
         "<li><b>DGCI&amp;S should publish, alongside TradeStat, a concordance of current and retired ITC-HS eight-digit codes with a flag on any code that carries no trade in the current year</b>, so errors like using 29011100 instead of 29012100 for ethylene are caught before analysis, not after publication.</li>\n"
         "<li><b>The Department of Chemicals and Petrochemicals should maintain a public quarterly tracker of large petrochemical projects, starting with BPCL&rsquo;s Andhra Pradesh complex and the Bina unit, showing approval, land allotment, environmental-clearance and investment-decision dates and commissioning</b>, so a project&rsquo;s status does not have to be pieced together from press reports.</li>\n"
         "<li><b>The Ministry of Environment should display, on PARIVESH, the current stage and expected decision date of each Environmental Clearance proposal</b>, so the clearance of a project the size of BPCL&rsquo;s Andhra Pradesh complex is not known first through a CMD&rsquo;s remarks to a Chief Minister and a single newspaper report.</li>\n"
         "<li><b>BIS and the Department of Chemicals and Petrochemicals should publish a consolidated register of chemical Quality Control Orders with HSN codes, notification dates and enforcement status</b>, so a QCO is never mistaken for a trade-remedy case or carried with a guessed code.</li>\n"
         "<li><b>The Department of Chemicals and Petrochemicals should publish the BHAVYA park challenge results and, once sites are chosen, site-wise milestones, spend and monthly land-acquisition progress</b>, so the &#8377;3,030 crore commitment can be tracked against its FY28&ndash;29 timeline from a primary source.</li>\n"
         "</ul>\n<p>These are proposals from this blog", "fix list")

# revision stamp
t = once(t, '<time datetime="2026-09-19" itemprop="dateModified">19 September 2026</time> &middot; v2.2.0 &middot; BPCL Andhra Pradesh complex: cost revised to &#8377;1,45,000 cr and Environmental Clearance now expected by end-September 2026 (was unfiled at last revision)',
         '<time datetime="2026-11-10" itemprop="dateModified">10 November 2026</time> &middot; v2.3.0 &middot; the executive summary and quarterly dashboard merged in; BPCL Andhra Pradesh clearance granted 27 October 2026 (see notes below)',
         "revised stamp")

t = repoint(t, ["chemical-import-substitution-analysis", "chemical-import-substitution-quarterly"], U_TOP15)
(OUT / "update-2026-11-10-top-15-chemicals-for-import.html").write_text(t)
print("merge1", len(t.encode()))

# ---------------------------------------------------------------- merge 2
r = (P / "chemical-import-substitution-hsn-8-registry.html").read_text()
F = (P / "chemical-import-substitution-full-hsn-8_01082878313.html").read_text()

s = F.index('<figure class="gb-figure"'); e = F.index('</figure>', s) + 9
chap_svg = F[s:e]
if 'aria-label' not in chap_svg[:400]:
    chap_svg = chap_svg.replace('<svg role="img" ', '<svg role="img" aria-label="Bar chart of India\'s chemical trade deficit by HS chapter, FY2025-26, $ billion" ', 1)
tb_start = F.index('<h2>Chapter 29 &#8212; Organic Chemicals</h2>')
tb_end = F.index('<script src="https://cdn.jsdelivr.net/npm/sortable-tablesort@3/sortable.min.js" defer></script>')
tb_end += len('<script src="https://cdn.jsdelivr.net/npm/sortable-tablesort@3/sortable.min.js" defer></script>')
tables = F[tb_start:tb_end]
# chapter headings become h3 under "The full registry"
tables = re.sub(r'<h2>(Chapter [^<]*)</h2>', r'<h3>\1</h3>', tables)

note2 = WARN + (
    '<b>Updated 10 November 2026.</b> The full data tables are back on this page, under '
    '<a href="#full-registry">The full registry</a>. They had been on a separate page, '
    '&ldquo;Chemical Import Substitution: the Full 827-Code Data Tables&rdquo;, which has now been retired. '
    'They were moved out in August because 368&nbsp;KB of table markup used up Blogger&rsquo;s rendering budget for the homepage list. '
    'The blog&rsquo;s listing pages now show snippets only, so that reason no longer applies. '
    'Two companion posts this page linked to, the executive summary and the quarterly dashboard, have been folded into '
    f'<a href="{U_TOP15}">The Top 15 Import-Substitution Chemicals, Code by Code</a>.</div>\n')
r = once(r, '<h2>Signal framework applied', note2 + '<h2>Signal framework applied', "reg first h2")

old_full = r[r.index('<h2>The full registry</h2>'):r.index('</div><p class="src">')]
new_full = ('<h2 id="full-registry">The full registry</h2>\n'
            '<p>Below are the chapter-wise tables: 827 HSN-8 codes across Chapters 28, 29, 31, 32, 33, 34, 38 and 39, 835 rows in total. '
            'Each chapter opens on a tap, and every column sorts. The signal and rationale columns apply the rules described above.</p>\n'
            '<p style="font-size:.9em;color:#555"><b>Known gap.</b> The value/quantity match rate was corrected on 9 August 2026 to 801 of 827 codes. '
            'These tables were built before that correction and do not mark the 26 unmatched rows separately. '
            'Those rows show as &ldquo;No Signal&rdquo;, which makes them look like genuine no-signal ratings. '
            'Fixing this needs the original matched-code list, which was not available for the 19 September check or this update.</p>\n'
            + chap_svg + '\n' + '<style>/*reg-tables-nobreak*/#Blog1 .post-body .artx details table.gs-t{min-width:1200px}#Blog1 .post-body .artx details table.gs-t td,#Blog1 .post-body .artx details table.gs-t th{overflow-wrap:normal}</style>\n' + tables + '\n')
r = r.replace(old_full, new_full)

r = once(r, 'Companion pieces: Top 15 Chemicals for Import Substitution, Executive Summary, Quarterly Tracking Dashboard.',
         f'Companion piece: <a href="{U_TOP15}">The Top 15 Import-Substitution Chemicals, Code by Code</a>, which now also carries the former executive summary and quarterly dashboard.',
         "src companions")

rel_s = r.index('<strong>Related on this blog:</strong>')
rel_e = r.index('</div>', rel_s)
r = r[:rel_s] + (
    f'<strong>Related on this blog:</strong> <a href="{U_TOP15}">The Top 15 Import-Substitution Chemicals, Code by Code</a> &middot; '
    f'<a href="{U_TREE}">India&rsquo;s Petrochemical Import Tree &mdash; From Petrol to Product (HSN-coded)</a> &middot; '
    f'<a href="{U_COAL}">India&rsquo;s Coal-to-Chemicals Menu, Ranked by What Actually Clears the Import Price</a> &mdash; '
    'the fifteen codes from this registry worth acting on first, with the chapter import base and a project tracker; the petrochemical version of the same question; '
    'and which coal routes could replace some of these imports.') + r[rel_e:]

r = once(r, '<time datetime="2026-08-07" itemprop="dateModified">7 August 2026</time> &middot; v3.0.0 &middot; full registry moved to a separate reference page &middot; checked',
         '<time datetime="2026-11-10" itemprop="dateModified">10 November 2026</time> &middot; v3.1.0 &middot; full 827-code tables merged back into this page &middot; checked',
         "reg revised")

r = repoint(r, ["chemical-import-substitution-analysis", "chemical-import-substitution-quarterly"], U_TOP15)
r = re.sub(r'https://masaladeutsch\.blogspot\.com/\d{4}/\d{2}/chemical-import-substitution-full-hsn-8_01082878313\.html', '#full-registry', r)
(OUT / "update-2026-11-10-chemical-import-substitution-hsn-8-registry.html").write_text(r)
print("merge2", len(r.encode()))

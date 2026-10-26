"""Crosscheck fixes of 26 Oct 2026: build out/update-2026-10-26-<slug>.html from posts/<slug>.html.
Each fix = exact replacements (each must match exactly once) + a dated update note."""
import re
import pathlib

ROOT = pathlib.Path('/home/user/blogger_writeups_code')
NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;'
        'margin:1.2em 0;border-radius:4px"><b>Updated 26 October 2026.</b> {}</div>\n')

FIXES = {
    "indias-coking-coal-import-problem-and": (
        [("In a compensation order published 26 December 2025, CAQM found six major thermal plants",
          "In show-cause notices issued in late December 2025, CAQM found six major thermal plants"),
         ("and demanded a combined <strong>&#8377;61.85 crore</strong> in environmental compensation, with each plant given 15 days to respond:",
          "and proposed a combined <strong>&#8377;61.85 crore</strong> in environmental compensation, with each plant given 15 days to respond; CAQM formally imposed the compensation in a press release of 8 April 2026, with a 15 April 2026 deposit deadline:")],
        "The December 2025 CAQM action on co-firing was a set of show-cause notices proposing &#8377;61.85 crore in compensation, not a final order; CAQM imposed the compensation on 8 April 2026, as this blog&rsquo;s "
        '<a href="https://masaladeutsch.blogspot.com/2026/08/ethanols-coal-boilers-briquette-gap-and.html">piece on ethanol plants&rsquo; coal boilers</a> records from CAQM&rsquo;s own release. The text below is corrected.'),
    "indias-gas-pipelines-run-at-half": (
        [],
        "PNGRB&rsquo;s own monthly MIS report for August 2026, read in full for this blog&rsquo;s "
        '<a href="https://masaladeutsch.blogspot.com/2026/10/india-has-27400-km-of-gas-pipeline.html">gas pipeline map</a>, puts the operational network at 28,157 km against 34,978 km authorised (June 2026). It also gives a network-wide utilisation figure: the 28 common-carrier pipelines carried 247 MMSCMD against 762 MMSCMD of capacity in August 2026, about 32%. '
        "That supersedes the 22 October note&rsquo;s statement that no newer national utilisation figure exists. The 50% (PNGRB chairman, against about 400 MMSCMD) and 41% (IEEFA, FY2025) estimates below use different bases and dates, so they are not directly comparable with the 32%."),
    "a-2013-vision-saw-india-needing-746": (
        [],
        "PNGRB&rsquo;s own monthly MIS report now gives a dated official figure: 28,157 km of gas pipeline operating against 34,978 km authorised as of June 2026, already within the 2013 report&rsquo;s 28,000&ndash;32,727 km target (see this blog&rsquo;s "
        '<a href="https://masaladeutsch.blogspot.com/2026/10/india-has-27400-km-of-gas-pipeline.html">gas pipeline map</a>). The roughly 25,400 km and 34,200 km figures below are mid-2025 estimates from press reviews; the recommendation that PNGRB publish a dated table is partly met by that monthly report.'),
    "five-year-synthesis-trade-currency": (
        [("puts FY2025-26 growth at 7.7% with FY2024-25 revised to 7.1%,",
          "puts FY2025-26 growth at 7.8% (new 2022-23 base) with FY2024-25 at 7.2% (first revised estimate),")],
        "The 12 October note&rsquo;s GDP figures (7.7% for FY2025-26, 7.1% for FY2024-25) came from press summaries. MoSPI&rsquo;s own national accounts data give 7.8% and 7.2%, as this blog&rsquo;s "
        '<a href="https://masaladeutsch.blogspot.com/2026/08/real-gdp-growth-india-fy2012-13-to.html">GDP growth series</a> records; the note is corrected.'),
    "the-hydrogen-bill-hiding-inside-indias": (
        [("recent SIGHT-scheme tenders cleared at <strong>$4.11&ndash;4.21 per kilogram</strong> (&#8377;387&ndash;397),",
          "the first SIGHT-scheme refinery awards were reported at <strong>$4.11&ndash;4.21 per kilogram</strong> (&#8377;387&ndash;397 including 18% GST; about &#8377;328&ndash;336 before tax), and the Numaligarh refinery tender of February 2026 cleared at a reported <strong>&#8377;279/kg</strong> (about $3.08) before tax,"),
         ("Green hydrogen's actual India cost ($4.11&ndash;4.21/kg, SIGHT-scheme tenders),",
          "Green hydrogen's actual India cost ($4.11&ndash;4.21/kg including GST in the first SIGHT-scheme awards; &#8377;279/kg before tax at Numaligarh, February 2026),")],
        "The green hydrogen tender prices below are corrected. The &#8377;387&ndash;397/kg figures include 18% GST, and the February 2026 Numaligarh tender cleared at a reported &#8377;279/kg before tax, as this blog&rsquo;s "
        '<a href="https://masaladeutsch.blogspot.com/2026/08/the-levelised-cost-of-hydrogen.html">levelised-cost-of-hydrogen piece</a> now records.'),
    "574-gw-and-counting-indias-wind-fleet": (
        [("with Gujarat overtaking Tamil Nadu as the single biggest contributor for the first time.",
          "with Gujarat, which overtook Tamil Nadu as the largest state fleet in 2023, now adding almost half of all new capacity (49% in FY2025-26)."),
         ("but Gujarat's newer, larger-scale build-out has now overtaken it as the single biggest contributor to the national total.",
          "but Gujarat&rsquo;s newer, larger-scale build-out overtook it as the largest state fleet in 2023 and now dominates new additions.")],
        "Gujarat overtook Tamil Nadu as India&rsquo;s largest wind fleet in 2023, not in June 2026 (by October 2025 Gujarat had 14,493 MW against Tamil Nadu&rsquo;s 11,938 MW, per this blog&rsquo;s "
        '<a href="https://masaladeutsch.blogspot.com/2026/08/tamil-nadus-wind-potential-according-to.html">Tamil Nadu wind piece</a>). The new finding here is Gujarat&rsquo;s 49% share of FY2025-26 additions. The text below is corrected.'),
    "financing-fuel-to-chemicals-pivot-how": (
        [("lifting IndianOil's own petrochemical intensity from about 6.5% to 16% and",
          "lifting IndianOil's own petrochemical intensity from about 6.5% to 15% (per IOCL&rsquo;s Q1 FY27 call transcript and S&amp;P Global; one press report gave 16%) and"),
         ("Petrochemical intensity target 6.5%&rarr;16%", "Petrochemical intensity target 6.5%&rarr;15%"),
         ("IndianOil's own company-level 6.5%-to-16% target cited above", "IndianOil's own company-level 6.5%-to-15% target cited above"),
         ("IndianOil&rsquo;s 6.5%-to-16% target", "IndianOil&rsquo;s 6.5%-to-15% target")],
        "IndianOil&rsquo;s petrochemical-intensity target is 15% by 2030, not 16%, per IOCL&rsquo;s own Q1 FY27 earnings-call transcript and S&amp;P Global, as corrected in this blog&rsquo;s "
        '<a href="https://masaladeutsch.blogspot.com/2026/08/the-barrel-really-is-shifting-indias.html">piece on the shifting barrel</a>. The figure is corrected in three places below.'),
    "india-imports-283000-tonnes-of-almonds": (
        [("Reported record lows in 2026 were about 95.86 on 14 May and about 96.2&ndash;96.4 in late September and early October;",
          "Reported lows in 2026 include about 95.86 on 14 May, and other posts on this blog put the record low later in May at about 96.8&ndash;97.0;")],
        "The 12 October note&rsquo;s description of late-September rupee levels (96.2&ndash;96.4) as record lows conflicted with this blog&rsquo;s reserves and FCNR(B) pieces, which put the 2026 record low in May at about 96.84&ndash;96.96. The note is corrected; the exact May low should still be checked against RBI reference-rate data."),
    "what-india-is-actually-paying-for": (
        [("ending the year at approximately <strong>&#8377;93.88 to the dollar</strong> after touching a then-record intraday low of <strong>&#8377;95.63 on 13 May 2026</strong> &mdash; a low that was itself later surpassed as the Hormuz crisis intensified through the rest of the year.",
          "ending the year at approximately <strong>&#8377;93.88 to the dollar</strong>. It then touched a then-record intraday low of <strong>&#8377;95.63 on 13 May 2026</strong> &mdash; a low surpassed within days as the Hormuz crisis intensified.")],
        "The sentence on the rupee below put a May 2026 low before the end of FY2025-26 in March; the order is corrected. The record low itself came later in May 2026."),
    "europe-bought-record-amount-of-lng-and": (
        [("A further expansion of <b>Dahej</b> — at 17.5 Mtpa the country&rsquo;s only ultra-large terminal and the sixth largest in the world — is under construction.",
          "<b>Dahej</b> — the country&rsquo;s only ultra-large terminal and the sixth largest in the world — was expanded from 17.5 to 22.5 Mtpa on 31 March 2026."),
         ("has a further 5 Mtpa under construction at Jafrabad, and 5 Mtpa expansions planned at both Dahej and Dabhol.",
          "has a further 5 Mtpa under construction at Jafrabad and a 5 Mtpa expansion planned at Dabhol; Dahej&rsquo;s 5 Mtpa expansion was commissioned on 31 March 2026."),
         ("such as Jafrabad and the planned Dahej and Dabhol expansions,", "such as Jafrabad and the planned Dabhol expansion,")],
        "Petronet LNG commissioned the Dahej expansion from 17.5 to 22.5 Mtpa on 31 March 2026, as this blog&rsquo;s "
        '<a href="https://masaladeutsch.blogspot.com/2026/10/indias-cheapest-lng-capacity-is-extra.html">LNG terminal piece</a> records; the text below described it as under construction. The FY2023-24 table keeps Dahej at 17.5 Mtpa, its capacity in that year.'),
}


def place(s, note):
    h1 = s.find('<h1')
    start = h1 if h1 >= 0 else 0
    cands = [i for i in (s.find('<div class="warn"', start), s.find('<h2', start), s.find('<div class="gb-h2"', start)) if i >= 0]
    i = min(cands)
    return s[:i] + note + s[i:]


for slug, (reps, note) in FIXES.items():
    s = (ROOT / 'posts' / f'{slug}.html').read_text(encoding='utf-8')
    for old, new in reps:
        n = s.count(old)
        assert n == 1, (slug, n, old[:60])
        s = s.replace(old, new)
    assert 'Updated 26 October 2026' not in s
    s = place(s, NOTE.format(note))
    out = ROOT / 'out' / f'update-2026-10-26-{slug}.html'
    out.write_text(s, encoding='utf-8')
    print('wrote', out.name, len(s))

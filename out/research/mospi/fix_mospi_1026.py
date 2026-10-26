"""MoSPI refresh of 26 Oct 2026: out/update-2026-10-26-<slug>.html from posts/<slug>.html.
Values from MoSPI's data service (out/research/mospi/latest-2026-10-26.md and calls of 26 Oct)."""
import pathlib

ROOT = pathlib.Path('/home/user/blogger_writeups_code')
NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;'
        'margin:1.2em 0;border-radius:4px"><b>Updated 26 October 2026.</b> {}</div>\n')

# CPI (base 2024), combined, YoY %, June and September 2026
JUN = {"Telangana": 6.36, "Andhra Pradesh": 5.39, "Tamil Nadu": 5.24, "Karnataka": 4.80, "Rajasthan": 4.70,
       "Uttar Pradesh": 4.56, "Kerala": 4.34, "Gujarat": 4.01, "West Bengal": 3.95, "Punjab": 3.83,
       "Maharashtra": 3.81, "Bihar": 3.28, "Delhi": 2.96, "All India": 4.38}
SEP = {"Telangana": 6.64, "Andhra Pradesh": 6.29, "Tamil Nadu": 6.81, "Karnataka": 5.86, "Rajasthan": 5.71,
       "Uttar Pradesh": 6.08, "Kerala": 5.26, "Gujarat": 5.11, "West Bengal": 4.04, "Punjab": 5.27,
       "Maharashtra": 5.18, "Bihar": 5.48, "Delhi": 3.40, "All India": 5.54}
rows = "".join(f"<tr><td>{s}</td><td>{JUN[s]:.2f}</td><td>{SEP[s]:.2f}</td><td>{SEP[s] - JUN[s]:+.2f}</td></tr>"
               for s in sorted(SEP, key=lambda k: (k == "All India", -SEP[k])))
CPI_TABLE = ('<div class="gb-tblwrap" style="margin:.6em 0 0"><table class="gb-table" style="font-size:.88em"><thead><tr><th>State</th>'
             '<th>June 2026, %</th><th>September 2026, %</th><th>Change, points</th></tr></thead><tbody>' + rows + '</tbody></table></div>')

FIXES = {
    "cpi-inflation-heatmap-india-june-2026": (
        [],
        "MoSPI&rsquo;s September 2026 CPI (base 2024) puts all-India inflation at 5.54%, up from 4.38% in June. Every state on this map rose. "
        "The southern pattern holds, with Tamil Nadu now the hottest of the 13 states at 6.81%, ahead of Telangana (6.64%), Andhra Pradesh (6.29%) and Uttar Pradesh (6.08%). "
        "Delhi is still the coolest at 3.40%, and Bihar moved from among the coolest to above the national rate (3.28% to 5.48%). The map below shows June 2026; the September readings are:" + CPI_TABLE),
    "cpi-wpi-trends-mospi-bulletin": (
        [('{ label: "All-India CPI, Jun 2026", value: "4.38%", sub: "index 107.00 · YoY inflation", cls: "delta-up" }',
          '{ label: "All-India CPI, Sep 2026", value: "5.54%", sub: "index 109.49 · YoY inflation (June: 4.38%)", cls: "delta-up" }'),
         ('{ label: "Hottest state — Telangana", value: "6.36%", sub: "vs. 2.96% in NCT of Delhi", cls: "delta-up" }',
          '{ label: "Hottest tracked state, Sep 2026 — Tamil Nadu", value: "6.81%", sub: "vs. 3.40% in NCT of Delhi (June: Telangana 6.36%)", cls: "delta-up" }'),
         ('{ label: "WPI, Apr 2026", value: "167.0", sub: "up from <b>157.6</b> in Jan 2026", cls: "" }',
          '{ label: "WPI, Sep 2026 (2022-23 base)", value: "112.5", sub: "11.39% YoY; chart below is the old 2011-12 base to Apr 2026", cls: "" }')],
        "The stat cards are refreshed to September 2026 from MoSPI&rsquo;s data service: all-India CPI (base 2024) inflation 5.54% (index 109.49), with Tamil Nadu the hottest tracked state at 6.81% and Delhi the coolest at 3.40%; and WPI on the new 2022-23 base at 112.5, 11.39% year on year. "
        "The CPI charts below still end in June 2026, and the WPI chart is the old 2011-12 series to April 2026."),
    "imported-fertiliser-fuel-prices-diesel": (
        [("June 2026 YoY was +32.57% for diesel, +1.09% for urea and +12.63% for DAP.",
          "June 2026 YoY was +32.57% for diesel, +2.0% for urea and +14.0% for DAP on the revised indices (the provisional June release gave +1.09% and +12.63%), and by September 2026 it was +30.0% for diesel, +2.7% for urea and +16.3% for DAP.")],
        "The WPI item rates below are refreshed from MoSPI&rsquo;s data service (base 2022-23). On the revised June 2026 indices, urea was up 2.0% and DAP 14.0% year on year, not the provisional 1.09% and 12.63% this post first gave; in September 2026 diesel was up 30.0%, urea 2.7% and DAP 16.3%."),
    "reinvesting-capital-gains-in-higher": (
        [("114.1 in April 2014 against 167.6 in April 2026 &mdash; the cap is worth <b>&#8377;34.0 lakh</b> in the prices of the year it was written, an erosion of 31.9%.",
          "114.1 in April 2014 against 167.0 in April 2026 &mdash; the cap is worth <b>&#8377;34.2 lakh</b> in the prices of the year it was written, an erosion of 31.7%."),
         ("&#8377;34.0L", "&#8377;34.2L")],
        "MoSPI&rsquo;s data service gives the April 2026 all-commodities WPI (base 2011-12) as 167.0, not 167.6, so the &#8377;50 lakh cap is worth &#8377;34.2 lakh in 2014 prices (an erosion of 31.7%), not &#8377;34.0 lakh. The text below is corrected. WPI has since been rebased to 2022-23; the old series is used here because it covers 2014."),
    "fy2025-26-sample-report-india-trade": (
        [('<div class="stat-label">GDP growth (real, FAE)</div><div class="stat-value">+7%</div><div class="stat-sub">First Advance Estimate — MoSPI\'s Provisional Estimate, released before this snapshot was compiled, has since superseded this figure</div>',
          '<div class="stat-label">GDP growth (real, PE)</div><div class="stat-value">+7.8%</div><div class="stat-sub">MoSPI Provisional Estimate (29 May 2026, base 2022-23); the First Advance Estimate was about 7%</div>')],
        "The GDP tile now shows MoSPI&rsquo;s provisional estimate for FY2025-26, 7.8% real growth on the new 2022-23 base, in place of the earlier first advance estimate of about 7%."),
    "a-17-rural-pay-rise-that-nobody-received": (
        [],
        "MoSPI&rsquo;s data service now has September 2026 figures for the rural price indices discussed below: year-on-year inflation was 6.30% for CPI-AL (agricultural labourers) and 5.98% for CPI-RL (rural labourers), up from 5.18% and 4.83% in August. "
        "The preliminary May 2026 comparison between the newly added regions and the national average has not been updated, because no regional breakdown has been released since."),
}


def place(s, note):
    h1 = s.find('<h1')
    start = h1 if h1 >= 0 else 0
    cands = [i for i in (s.find('<div class="warn"', start), s.find('<h2', start), s.find('<div class="gb-h2"', start)) if i >= 0]
    return s[:min(cands)] + note + s[min(cands):]


for slug, (reps, note) in FIXES.items():
    s = (ROOT / 'posts' / f'{slug}.html').read_text(encoding='utf-8')
    for old, new in reps:
        n = s.count(old)
        assert n == 1, (slug, n, old[:70])
        s = s.replace(old, new)
    s = place(s, NOTE.format(note))
    (ROOT / 'out' / f'update-2026-10-26-{slug}.html').write_text(s, encoding='utf-8')
    print('wrote', slug)

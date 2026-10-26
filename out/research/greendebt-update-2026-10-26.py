"""Green-debt post refresh of 26 Oct 2026 -> out/update-2026-10-26-raising-green-debt-globally-rec-euroyen.html."""
import pathlib
ROOT = pathlib.Path('/home/user/blogger_writeups_code')
SLUG = 'raising-green-debt-globally-rec-euroyen'
s = (ROOT / 'posts' / f'{SLUG}.html').read_text(encoding='utf-8')

def rep(old, new):
    global s
    n = s.count(old)
    assert n == 1, (n, old[:80])
    s = s.replace(old, new)

NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;'
        'margin:1.2em 0;border-radius:4px"><b>Updated 26 October 2026.</b> '
        'The sovereign green-bond story has turned: after the RBI rejected every bid at a 30-year green auction in June 2025, '
        'a new 30-year green bond sold at a 6bp greenium in April 2026, the largest since January 2023, and has been reopened twice since (Section 5c). '
        'India&rsquo;s 10-year yield has risen to about 7.47% after the RBI&rsquo;s 7 October hike to 5.50%, and the Japan Credit Rating Agency raised India to A&minus; on 2 September 2026, '
        'which matters for yen funding (Section 7). Also added: CBI&rsquo;s first-half 2026 market totals, the rupee&rsquo;s late-October level, '
        'The policy-rate chart in Section 5a now runs to October 2026, and the rate-gap table below it is refreshed to 26 October.</div>\n')
h1 = s.find('<h1'); first = s.find('<div class="gb-h2"', h1)
s = s[:first] + NOTE + s[first:]

# 5a: after the 7 October update block
rep("Sources: Federal Reserve press release/CNBC (Fed), ECB press release (ECB), Bloomberg/CNBC/TradingEconomics (BoJ).</div>",
    "Sources: Federal Reserve press release/CNBC (Fed), ECB press release (ECB), Bloomberg/CNBC/TradingEconomics (BoJ).</div>\n"
    "<div class=\"gb-warn\"><b>Update, 26 October 2026.</b> The RBI&rsquo;s own statement of 7 October confirms the hike was unanimous and that the Monetary Policy Committee moved to a stance of &ldquo;calibrated tightening&rdquo;; "
    "the standing deposit facility is at 5.25% and the marginal standing facility and Bank Rate at 5.75%. The Fed, ECB, Bank of Japan, Bank of Canada and Reserve Bank of New Zealand all decide in the week of 26 October, "
    "so every rate in this section is as of 26 October, before those meetings. Sources: RBI press release on the Monetary Policy Statement, 7 October 2026; RBI current rates page, 26 October 2026; Newsquawk week-ahead calendar.</div>")

# 5a-i: the gap table, refreshed to 26 October 2026 from each central bank's latest decision
INDIA = 5.50
ROWS = [  # economy, rate, issuance currency?, latest decision
    ("Switzerland", 0.00, "Yes", "Held, 24 Sep"),
    ("Thailand", 1.00, "&mdash;", "Held, 26 Aug"),
    ("Japan", 1.25, "Yes", "Hiked, 18 Sep; decides this week"),
    ("Sweden", 1.75, "Yes", "Held, 24 Sep"),
    ("Denmark", 2.10, "Yes", "Hiked, 11 Sep"),
    ("Canada", 2.25, "Yes", "Held, 2 Sep; decides 28 Oct"),
    ("Morocco", 2.25, "&mdash;", "Held, 22 Sep"),
    ("Euro area", 2.50, "Yes", "Hiked, 16 Sep; decides 29 Oct"),
    ("New Zealand", 2.75, "&mdash;", "Hiked, 2 Sep; decides 28 Oct"),
    ("Malaysia", 2.75, "&mdash;", "Held, 3 Sep"),
    ("Korea", 3.00, "Yes", "Held, 22 Oct, after two hikes"),
    ("China", 3.00, "Yes", "Held, 20 Oct"),
    ("Israel", 3.25, "&mdash;", "Held, 21 Oct, after cuts in May, Jul and Sep"),
    ("Kuwait", 3.50, "&mdash;", "Held, Sep"),
    ("Czechia", 3.75, "&mdash;", "Held, 17 Sep"),
    ("United Kingdom", 3.75, "Yes", "Held, Sep (6&ndash;3 vote)"),
    ("Poland", 3.75, "&mdash;", "Held, 7 Oct"),
    ("United States", 3.875, "Yes", "Hiked, 16 Sep; decides 28 Oct"),
    ("Hong Kong SAR", 4.25, "Yes", "Raised, 17 Sep (follows the Fed)"),
    ("North Macedonia", 4.25, "&mdash;", "Hiked, Jun; no later decision found"),
    ("Peru", 4.25, "&mdash;", "Held, 7 Oct"),
    ("Norway", 4.50, "Yes", "Hiked, 23 Sep"),
    ("Saudi Arabia", 4.50, "&mdash;", "Hiked, 16 Sep"),
    ("Chile", 4.50, "&mdash;", "Held; decides 27 Oct"),
    ("Australia", 4.60, "Yes", "Hiked, 29 Sep"),
]
assert len(ROWS) == 25 and all(r < INDIA for _, r, _, _ in ROWS)
fmt = lambda x: f"{x + 1e-9:.2f}"
NUM = 'style="text-align:right;font-variant-numeric:tabular-nums"'
body = "\n".join(f'<tr><td>{e}</td><td {NUM}>{fmt(r)}</td><td {NUM}>{fmt(INDIA - r)}</td><td>{c}</td><td>{d}</td></tr>' for e, r, c, d in ROWS)
TABLE = ('<div class="gb-tblwrap"><table class="gb-table">\n'
         '<thead><tr><th>Economy</th><th style="text-align:right">Policy rate (%)</th><th style="text-align:right">Gap vs India (pp)</th>'
         '<th>Issuance currency for an Indian PSU/NBFC?</th><th>Latest decision (2026)</th></tr></thead>\n<tbody>\n' + body + '\n</tbody>\n</table></div>\n')
NOTE_T = ('<p class="gb-note">Rates as of 26 October 2026, from each central bank&rsquo;s latest decision as published or reported; the original table used BIS central bank policy rate statistics (WS_CBPOL, last observation per economy, retrieved 3&nbsp;Aug&nbsp;2026), which could not be re-pulled for this update. '
          'India is the RBI repo rate (5.50% since 7 October); the US figure is the Fed&rsquo;s mid-target, so the upper bound is 12.5bp higher; the euro area is the ECB deposit facility rate; '
          'China is the one-year loan prime rate, as in the original table (the PBOC&rsquo;s main policy rate, the 7-day reverse repo, is 1.40%, which would put China&rsquo;s gap at 4.10). '
          'Not counted: the Philippines, level with India at 5.50% after a 22 October hike, and Indonesia at 5.75%. Six of these central banks, the Bank of Japan among them, decide again between 27 and 30 October. '
          'Eleven defunct pre-euro national series (Germany, France, Italy and others, last observed 1998&ndash;2000) are excluded, as before. The issuance-currency column is a judgement about market depth, not a legal restriction. '
          'Sources: central bank releases (SNB, Riksbank, Danmarks Nationalbank, Bank Al-Maghrib, Bank of Israel, Bank of Korea, Bank Negara Malaysia, Bank of Thailand, HKMA, SAMA, Norges Bank, RBA, Fed, ECB, BoJ, RBI); '
          'Reuters, Bloomberg, CNBC, Central Banking, Trading Economics and BBVA Research reporting for the Bank of Canada, Bank of England, RBNZ, CNB, NBP, PBOC, BCRP, Banco Central de Chile, Central Bank of Kuwait and National Bank of North Macedonia.</p>')
i = s.index('<div class="gb-tblwrap"><table class="gb-table">\n<thead><tr><th>Economy</th>')
j = s.index("missing the June&nbsp;2026 BoJ hike discussed above.</p>", i) + len("missing the June&nbsp;2026 BoJ hike discussed above.</p>")
s = s[:i] + TABLE + NOTE_T + s[j:]
rep("<strong>25 of the 38 live economies sit below India's\n5.25% repo</strong>",
    "<strong>25 of the 38 live economies sat below India's\n5.25% repo</strong> on 3 August, and the same 25 sit below its 5.50% repo on 26 October")
rep("gap in the entire panel at 5.25pp and is close to the least useful",
    "gap in the entire panel at 5.50pp and is close to the least useful")

# 5b: FX
rep("for the FBIL era, retrieved 3 Aug 2026.</p>",
    "for the FBIL era, retrieved 3 Aug 2026. <b>Update, 26 October 2026:</b> the rupee was at about &#8377;95.2 to the dollar on 26 October (provisional close, after a six-week high of 94.38 on 21 October), "
    "close to the &#8377;95.33 used above, so the dollar column still stands; the euro and yen columns have not been re-pulled. Sources: PTI via Telangana Today and ThePrint.</p>")

# 5b: treasury curve
rep("Issuers time the treasury curve first and the label second.</p>",
    "Issuers time the treasury curve first and the label second.</p>\n"
    "<p class=\"gb-note\"><b>Update, 26 October 2026:</b> the curve has moved up since August. India&rsquo;s 10-year yield reached 7.47% on 23 October, from 7.19% on 6 October, the day before the RBI hike; "
    "the US 10-year was 4.96% on 22 October; and the 10-year JGB passed 3% in late September (3.055% on 24 September, its highest since August 1996). "
    "The India&ndash;US 10-year gap is therefore about 2.5 points, against about 2.15 in August: long-term rupee borrowing has become dearer relative to dollar borrowing, which widens the margin described in Section 5a&rsquo;s third reading. "
    "No October Bund figure was checked. Sources: Business Standard/PTI (India), Federal Reserve H.15 (US), CNBC (Japan).</p>")

# Section 4: sovereign row
rep("then auctions devolved/cancelled as the greenium vanished (Nov 2024: &#8377;1,502&nbsp;cr accepted of &#8377;5,000&nbsp;cr)</td>",
    "then auctions devolved/cancelled as the greenium vanished (Nov 2024: &#8377;1,502&nbsp;cr accepted of &#8377;5,000&nbsp;cr); greenium back in 2026: the 7.50% GOI SGrB 2056 (first issued 27 Apr 2026) sold at 6bp inside conventional paper and was reopened in Aug and Oct 2026</td>")

# 5c: greenium
rep("with one contested study putting ~25bp for <em>certified</em> bonds specifically.</p>",
    "with one contested study putting ~25bp for <em>certified</em> bonds specifically.</p>\n"
    "<p><b>Update, 26 October 2026: the sovereign greenium has come back.</b> In June 2025 the RBI rejected every bid at a 30-year green auction because investors wanted higher yields and no greenium. "
    "In April 2026 the government sold a new 30-year green bond, the 7.50% GOI SGrB 2056 (first issued 27 April 2026), at a 6bp greenium to equivalent-maturity government securities, the largest since January 2023. "
    "The RBI has since reopened it twice: &#8377;5,000 crore notified for 14 August 2026 and &#8377;3,000 crore for 1 October 2026. "
    "The August sale is reported at a 7.3169% cut-off and a greenium of about 4bp (a summary of Reuters reporting, not checked against the RBI&rsquo;s auction result). "
    "The official borrowing plan for April&ndash;September 2026 set aside &#8377;15,000 crore for sovereign green bonds, and the RBI&rsquo;s calendar for October 2026&ndash;March 2027 (25 September 2026) includes them again; its amount was not checked for this update. "
    "The domestic label market is, in practice, the sovereign: S&amp;P Global puts India&rsquo;s sustainable bond issuance at $2 billion in 2025, with sovereign issues 94% of green and 58% of all sustainable bonds. "
    "A greenium of 4&ndash;6bp is still small. Even so, the sovereign programme no longer shows the label failing to pay; it now shows that it pays when supply is kept short. "
    "Sources: Business Standard (June 2025 rejection; April 2026 sale), RBI auction notices for 14 August and 1 October 2026, DEA/PIB borrowing plan for H1 FY2026-27, RBI press release of 25 September 2026, S&amp;P Global via The Statesman.</p>")

# Section 6: scoreboard
rep("2025 cooled to ~$904&nbsp;bn (&minus;17%).</li>",
    "2025 cooled to ~$904&nbsp;bn (&minus;17%).</li>\n"
    "<li><b>Update, 26 October 2026:</b> CBI&rsquo;s first-half 2026 report puts aligned GSS+ issuance at <strong>$529.7&nbsp;bn</strong> (&minus;1% on H1 2025), of which green <strong>$364.1&nbsp;bn (69%)</strong>; "
    "Q2 2026 ($210.8&nbsp;bn of green) was the strongest green quarter on record, and cumulative aligned volume passed <strong>$7.3&nbsp;trillion</strong>. "
    "Social, sustainability and sustainability-linked volumes fell.</li>")
rep("<p class=\"gb-note\" style=\"margin:0\">Sources: Climate Bonds Initiative, Sustainable Debt Global State of the Market 2024 (14th ed., Sep 2025);",
    "<p class=\"gb-note\" style=\"margin:0\">Sources: Climate Bonds Initiative, Sustainable Debt Global State of the Market 2024 (14th ed., Sep 2025) and H1 2026 press release;")

# Section 7: ratings
rep("<tr><td>Moody's Ratings</td><td>Baa3, stable</td><td>Held since June 2020; Baa3 is the lowest rung of investment grade &mdash; one downgrade from junk</td></tr>",
    "<tr><td>Moody's Ratings</td><td>Baa3, stable</td><td>Held since June 2020; Baa3 is the lowest rung of investment grade &mdash; one downgrade from junk</td></tr>\n"
    "<tr><td>Japan Credit Rating Agency (JCR)</td><td>A&minus;, stable</td><td>Upgraded from BBB+ on 2 September 2026, with India&rsquo;s country ceiling raised to A; reported as the first A-category rating for India from an international agency in over 35 years (added 26 October 2026)</td></tr>")
rep("All three ratings are foreign-currency long-term issuer ratings, the ones that govern the avenue matrix in Section 4.</p>",
    "All three ratings are foreign-currency long-term issuer ratings, the ones that govern the avenue matrix in Section 4. JCR: its rating action of 2 September 2026, as reported by DD India and The Hans India.</p>\n"
    "<p><b>Update, 26 October 2026: why the JCR upgrade matters for yen funding.</b> JCR is not one of the three agencies whose ratings set most global mandates, and nothing in the table above changed for S&amp;P, Moody&rsquo;s or Fitch. "
    "But it is one of the two domestic agencies that Japanese institutions commonly use, and yen-market issuers often carry a JCR or R&amp;I rating. "
    "On JCR&rsquo;s scale India is now A&minus;, with a country ceiling of A. That puts Indian sovereign-linked paper a notch or more higher for exactly the investor base the EuroYen route in this article serves. "
    "JCR cited growth near 7%, GST, digital public infrastructure and banks&rsquo; gross non-performing loans falling to 1.8% at the end of March 2026.</p>")


# ---- policy-rate chart: decode the Jan 2020-Jul 2026 series and extend to Oct 2026 ----
import re as _re
a = s.index('<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Central bank policy rates 2020-2026"')
b = s.index('</svg>', a) + len('</svg>')
old_svg = s[a:b]
Y0, K, X0, X1 = 318.9, 42.13, 46.0, 570.0
lines = _re.findall(r'<polyline points="([^"]+)" fill="none" stroke="(#[0-9a-f]{6})"', old_svg)
assert len(lines) == 4
series = []
for pts, col in lines:
    vals = [round(round((Y0 - float(p.split(',')[1])) / K / 0.005) * 0.005, 3) for p in pts.split()]
    assert len(vals) == 79
    series.append([vals, col])
# Aug, Sep, Oct 2026 (month-end, Oct as of 26 Oct): RBI hike 7 Oct; Fed 17 Sep (mid-target);
# ECB deposit rate 16 Sep; BoJ 18 Sep.
EXT = [[5.25, 5.25, 5.50], [3.625, 3.875, 3.875], [2.25, 2.50, 2.50], [1.00, 1.25, 1.25]]
assert [v[0][-1] for v in series] == [5.25, 3.625, 2.25, 1.0]
for (vals, col), ext in zip(series, EXT):
    vals += ext
N = len(series[0][0])
step = (X1 - X0) / (N - 1)
X = lambda i: X0 + i * step
Y = lambda v: Y0 - K * v
out = ['<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Central bank policy rates 2020-2026" style="max-width:100%;height:auto;background:#fff;font-family:-apple-system,Segoe UI,sans-serif">',
       '<text x="46" y="16" font-size="13" font-weight="700" fill="#212529">Policy rates, Jan 2020 &#8211; Oct 2026 (%)</text>']
for v in range(8):
    out.append(f'<line x1="46" y1="{Y(v):.1f}" x2="570" y2="{Y(v):.1f}" stroke="#e9ecef" stroke-width="1"/>')
    out.append(f'<text x="38" y="{Y(v) + 4:.1f}" font-size="11" fill="#868e96" text-anchor="end">{v}</text>')
out.append(f'<line x1="46" y1="{Y(0):.1f}" x2="570" y2="{Y(0):.1f}" stroke="#adb5bd" stroke-width="1.2"/>')
for k in range(7):
    out.append(f'<text x="{X(12 * k):.1f}" y="366" font-size="11" fill="#868e96" text-anchor="middle">{2020 + k}</text>')
for vals, col in series:
    pts = ' '.join(f'{X(i):.1f},{Y(v):.1f}' for i, v in enumerate(vals))
    out.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.4" stroke-linejoin="round"/>')
labels = ['&#x1F1EE;&#x1F1F3; RBI (repo) 5.50%', '&#x1F1FA;&#x1F1F8; US Fed 3.88%', '&#x1F1EA;&#x1F1FA; ECB 2.50%', '&#x1F1EF;&#x1F1F5; Bank of Japan 1.25%']
for (vals, col), lab in zip(series, labels):
    out.append(f'<circle cx="{X(N - 1):.1f}" cy="{Y(vals[-1]):.1f}" r="3" fill="{col}"/>')
    out.append(f'<text x="578" y="{Y(vals[-1]) + 4:.1f}" font-size="11.5" font-weight="600" fill="{col}">{lab}</text>')
xj = X(48)
out.append(f'<line x1="{xj:.1f}" y1="24" x2="{xj:.1f}" y2="340" stroke="#868e96" stroke-width="1" stroke-dasharray="4 3"/>')
out.append(f'<text x="{xj + 5:.1f}" y="37" font-size="10.5" fill="#495057">REC &#165;61.1bn EuroYen, Jan 2024</text>')  # clear of the RBI line at 6.5%
ia = N - 4  # July 2026: 5.25 vs 1.00; today 5.50 vs 1.25, the same 4.25 points
xa = X(ia)
out.append(f'<line x1="{xa:.1f}" y1="{Y(series[3][0][ia]) - 6:.1f}" x2="{xa:.1f}" y2="{Y(series[0][0][ia]) + 8:.1f}" stroke="#495057" stroke-width="1.4" marker-end="url(#arr)"/>')
out.append('<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#495057"/></marker></defs>')
out.append(f'<text x="{xa - 6:.1f}" y="187.3" font-size="10.5" fill="#495057" text-anchor="end">the carry: ~4.25pp</text>')
out.append('</svg>')
s = s[:a] + '\n'.join(out) + s[b:]
rep("Dashed line marks REC's &#165;61.1&nbsp;bn EuroYen issue.</p>",
    "Dashed line marks REC's &#165;61.1&nbsp;bn EuroYen issue. <b>Extended 26 October 2026</b> to October 2026 from the central banks&rsquo; own announcements: "
    "Fed target range 3.75&ndash;4.00% from 17 September (mid-target 3.875% plotted), ECB deposit rate 2.50% from 16 September, Bank of Japan 1.25% from 18 September, RBI repo 5.50% from 7 October. "
    "The October points are as of 26 October, before that week&rsquo;s Fed, ECB and Bank of Japan decisions. The euro line follows the ECB deposit facility rate from September 2024 on, as the original chart did.</p>")
rep("The chart, its \"~4.25pp carry\" annotation and the gap table below are not redrawn and remain as of the 3 August 2026 data pull.",
    "The chart above now runs to October 2026 and the gap table below is refreshed to 26 October (both updated 26 October 2026).")

# Sources line
rep("Nothing here is investment advice.",
    "The 26 October 2026 update adds the RBI&rsquo;s Monetary Policy Statement (7 Oct 2026), current-rates page and auction notices (14 Aug and 1 Oct 2026); Business Standard/PTI on yields, the June 2025 and April 2026 green auctions; Federal Reserve H.15; CNBC on JGB yields; PTI/ThePrint on the rupee; JCR&rsquo;s 2 Sep 2026 rating action as reported; CBI&rsquo;s H1 2026 State of the Market press release; and S&amp;P Global&rsquo;s India sustainable-bond figures via The Statesman. Nothing here is investment advice.")

(ROOT / 'out' / f'update-2026-10-26-{SLUG}.html').write_text(s, encoding='utf-8')
print('wrote', len(s))

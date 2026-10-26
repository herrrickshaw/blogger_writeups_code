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
        'and the effect of India&rsquo;s higher repo rate on the rate-gap table. The charts are not redrawn.</div>\n')
h1 = s.find('<h1'); first = s.find('<div class="gb-h2"', h1)
s = s[:first] + NOTE + s[first:]

# 5a: after the 7 October update block
rep("Sources: Federal Reserve press release/CNBC (Fed), ECB press release (ECB), Bloomberg/CNBC/TradingEconomics (BoJ).</div>",
    "Sources: Federal Reserve press release/CNBC (Fed), ECB press release (ECB), Bloomberg/CNBC/TradingEconomics (BoJ).</div>\n"
    "<div class=\"gb-warn\"><b>Update, 26 October 2026.</b> The RBI&rsquo;s own statement of 7 October confirms the hike was unanimous and that the Monetary Policy Committee moved to a stance of &ldquo;calibrated tightening&rdquo;; "
    "the standing deposit facility is at 5.25% and the marginal standing facility and Bank Rate at 5.75%. The Fed, ECB, Bank of Japan, Bank of Canada and Reserve Bank of New Zealand all decide in the week of 26 October, "
    "so every rate in this section is as of 26 October, before those meetings. Sources: RBI press release on the Monetary Policy Statement, 7 October 2026; RBI current rates page, 26 October 2026; Newsquawk week-ahead calendar.</div>")

# 5a-i: the gap table
rep("missing the June&nbsp;2026 BoJ hike discussed above.</p>",
    "missing the June&nbsp;2026 BoJ hike discussed above.</p>\n"
    "<p class=\"gb-note\"><b>Update, 26 October 2026:</b> India&rsquo;s repo rate is now 5.50%, so every gap in the last-but-one column is 0.25 points wider than shown, "
    "except where the foreign rate also moved: the United States (Fed mid-target 3.875%, gap 1.63), the euro area (ECB deposit rate 2.50%, gap 3.00) and Japan (1.25%, gap 4.25). "
    "Rates for the other 22 economies are as of 3 August and have not been re-pulled from BIS; every economy listed is still below India.</p>")

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

# Sources line
rep("Nothing here is investment advice.",
    "The 26 October 2026 update adds the RBI&rsquo;s Monetary Policy Statement (7 Oct 2026), current-rates page and auction notices (14 Aug and 1 Oct 2026); Business Standard/PTI on yields, the June 2025 and April 2026 green auctions; Federal Reserve H.15; CNBC on JGB yields; PTI/ThePrint on the rupee; JCR&rsquo;s 2 Sep 2026 rating action as reported; CBI&rsquo;s H1 2026 State of the Market press release; and S&amp;P Global&rsquo;s India sustainable-bond figures via The Statesman. Nothing here is investment advice.")

(ROOT / 'out' / f'update-2026-10-26-{SLUG}.html').write_text(s, encoding='utf-8')
print('wrote', len(s))

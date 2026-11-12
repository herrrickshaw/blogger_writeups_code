"""Prose edits for the 12 Nov 2026 refresh (data through 31 Oct 2026). Applied after build_post.py.
Each replacement must match exactly once."""
import sys
F = sys.argv[1]; h = open(F, encoding="utf-8").read()
NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
 '<b>Updated 12 November 2026.</b> Refreshed with Agmarknet data through 31 October 2026 (previously to 23 October). Arrivals now cover November 2025 to October 2026, and the method and 23 crops are unchanged. '
 'Paddy and wheat now take 45.1% of the 23 crops&rsquo; arrivals, 71.9 of 159 million tonnes, against 44.7% (68.6 of 153) before. '
 'Rankings: maize overtakes potato as the fourth-largest crop, groundnut moves past garlic to 12th, and Madhya Pradesh (34.3 million tonnes) overtakes Uttar Pradesh (33.7) as the largest state. '
 'Wheat&rsquo;s typical monthly move rises from 2.5% to 2.7%, which takes it from 18th to 17th on volatility, swapping places with chana. Tomato&rsquo;s stays at 20.4% and onion&rsquo;s at 13.5%. '
 'One earlier slip is also corrected: Chhattisgarh, at 10.2%, edges out Uttar Pradesh (10.3%) as onion&rsquo;s steadiest state. '
 'MoSPI&rsquo;s October consumer price index put onion up 116% on a year earlier (<a href="https://www.zeebiz.com/economy-infra/news-retail-inflation-rises-to-609-in-october-food-inflation-climbs-to-894-onion-prices-surge-116-405482">Zee Business, 12 November 2026</a>). '
 'In the mandi data, the all-India arrival-weighted onion price in October 2026 was Rs 3,440 a quintal. That is 3.2 times October 2025&rsquo;s Rs 1,059 and 4% below September&rsquo;s Rs 3,590, after five monthly rises from Rs 1,077 in May. '
 'A year earlier was itself unusually cheap: October 2024 was Rs 3,507. October&rsquo;s onion arrivals were 1.30 million tonnes against 1.34 million a year earlier. '
 'The CPI is a retail index and the mandi figure is a wholesale price, so the two are not expected to match.</div>\n')
R = [
 ('<div class="gb-kicker" style="order:2">Agriculture &middot; Mandi prices &middot; 24 October 2026</div>\n', None),  # anchor check only
 ('move about 2.5&ndash;3% in a typical month. Onion', 'move about 2.7&ndash;3.1% in a typical month. Onion'),
 ('by state, January 2019 to 23 October 2026. Arrivals', 'by state, January 2019 to October 2026. Arrivals'),
 ('and move about 2.5 to 3 percent a month.', 'and move about 2.7 to 3.1 percent a month.'),
 ('moving 2.5&ndash;3.1% in a typical month.', 'moving 2.7&ndash;3.1% in a typical month.'),
 ('onion moves 13.5% a month and potato 6.2%.', 'onion moves 13.5% a month and potato 6.1%.'),
 ('Latest = October 2026 to the 23rd.', 'Latest = October 2026.'),
 ('Uttar Pradesh and Madhya Pradesh dominate, with about 33 million tonnes each across these crops. Uttar Pradesh&rsquo;s biggest flows are potato, wheat and paddy; Madhya Pradesh&rsquo;s are wheat, maize and soybean.',
  'Madhya Pradesh and Uttar Pradesh dominate, with about 34 million tonnes each across these crops. Madhya Pradesh&rsquo;s biggest flows are wheat, maize and soybean; Uttar Pradesh&rsquo;s are potato, wheat and paddy.'),
 ('Onion was steadiest in Uttar Pradesh at 10.3% and most volatile', 'Onion was steadiest in Chhattisgarh and Uttar Pradesh at about 10% and most volatile'),
 ('and rice in West Bengal 0.8%.', 'and rice in West Bengal 0.9%.'),
 ('against 2.4&ndash;4.9% in the main producing states', 'against 2.5&ndash;5.4% in the main producing states'),
 ('state-wise price and arrival report), 23 commodities, January 2019 to 23 October 2026:', 'state-wise price and arrival report), 23 commodities, January 2019 to 31 October 2026:'),
]
for old, new in R:
    n = h.count(old); assert n == 1, (n, old[:70])
    if new is not None: h = h.replace(old, new)
# update note directly after the header block (the gs-head-order div closes right after the h1)
i = h.index('<div class="gs-head-order"'); j = h.index('</div>\n', h.index('</h1>', i)) + len('</div>\n')
assert h[j:j+200].count('class="warn"') == 0
h = h[:j] + NOTE + h[j:]
open(F, "w", encoding="utf-8").write(h); print("ok")

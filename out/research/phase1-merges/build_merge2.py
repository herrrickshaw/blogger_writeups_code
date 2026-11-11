import re
ROOT='/home/user/blogger_writeups_code/'
t=open(ROOT+'posts/050-is-its-own-category-diving-into.html').read()
b=open(ROOT+'posts/below-250-is-where-real-junk-lives.html').read()
B_URL='https://masaladeutsch.blogspot.com/2026/08/below-250-is-where-real-junk-lives.html'
def rep(s,a,c,n=1):
    k=s.count(a); assert k==n,(k,a[:90]); return s.replace(a,c)
def grab(s,a,z):
    i=s.index(a); j=s.index(z,i); return s[i:j]

# dek
t=rep(t,'<p style="order:4" class="dek">The previous piece split "under ₹1,000" into four bands and found the ₹0&ndash;250 slice was the worst-performing, highest-risk quarter of the entire market — and that it alone held 79% of every stock priced under ₹1,000. That\'s still a wide net. This piece splits ₹0&ndash;250 itself into four narrower bands to find out whether the bottom of that range is uniformly bad, or whether the real basement is even smaller than it looked.</p>',
 '<p style="order:4" class="dek">This blog\'s first price-band piece found no clean link between a stock\'s price and its risk, but its cheapest bucket, "under ₹1,000", held almost 4,900 stocks. This piece splits that bucket twice. The first split finds the ₹0&ndash;250 slice is the worst-performing, highest-risk quarter of the market, and that it alone holds 79% of every stock priced under ₹1,000. The second splits ₹0&ndash;250 itself into four narrower bands, to see whether the bottom of that range is uniformly bad or whether the real basement is even smaller.</p>')

# 10 Nov note + new section 1 from the absorbed post
note=('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
'<b>Updated 10 November 2026.</b> This page now carries this blog\'s earlier post <i>Below ₹250 Is Where the Real Risk Lives</i>, which has been retired. '
'Its split of the under-₹1,000 universe into four bands is section 1 below; the original drill into the ₹0&ndash;250 band follows from section 2. '
'The figures are unchanged: both pieces use the same Screener.in pull of 11 August 2026 and the same weekly NSE price window, 2 January 2023 to 7 August 2026.</div>\n')
s1=grab(b,'<h2>1. One bucket, four very different neighbourhoods</h2>','<h2>4. Does this contradict the earlier finding?</h2>')
# drop the duplicate BSE photo from the absorbed section (the target already carries it)
s1=re.sub(r'<figure style="margin:1.6rem 0">.*?</figure>\n','',s1,flags=re.S)
s1=rep(s1,'<h2>1. One bucket, four very different neighbourhoods</h2>','<h2 id="under-1000">1. Under ₹1,000: one bucket, four very different neighbourhoods</h2>')
s1=rep(s1,'using the same Screener.in price data as the earlier piece.','using the same Screener.in price data as <a href="https://masaladeutsch.blogspot.com/2026/08/a-slice-of-apple-costs-about-1700-slice.html">the earlier five-band piece</a>.')
s1=rep(s1,'The "under ₹1,000" bucket in the earlier piece wasn\'t really one population','The "under ₹1,000" bucket in that piece wasn\'t really one population')
s1=rep(s1,'<h2>2. Beta, return and Sharpe ratio, split four ways</h2>','<h3>Beta, return and Sharpe ratio, split four ways</h3>')
s1=rep(s1,'<h2>3. Real returns confirm the same pattern</h2>','<h3>Real returns confirm the same pattern</h3>')
s1=rep(s1,'The ₹0&ndash;250 sub-band is the worst-performing, highest-risk group in <em>either</em> piece','At this level of zoom the ₹0&ndash;250 sub-band is the worst-performing, highest-risk group')
# chart from the absorbed post, placed after the returns table
fig=re.search(r'<figure class="gb-figure".*?</figure>',b,re.S).group(0)
s1=rep(s1,'<p>The median stock priced under ₹250 <em>lost</em> 17.7%',fig+'\n<p>The median stock priced under ₹250 <em>lost</em> 17.7%')
s1+=('<p>The obvious next question is whether the ₹0&ndash;250 band is uniformly bad, or whether something inside it is doing most of the damage. The rest of this piece splits it again.</p>\n\n')
first_h2='<h2>1. Even inside "cheap," most of the mass sits at the very bottom</h2>'
t=rep(t,first_h2,note+s1+'<h2 id="under-250">2. Inside ₹0&ndash;250: most of the mass sits at the very bottom</h2>')

# renumber and re-reference the target sections
t=rep(t,'<h2>2. Beta, return and Sharpe ratio inside the basement</h2>','<h2>3. Beta, return and Sharpe ratio inside the basement</h2>')
t=rep(t,'<h2>3. What "cheap" actually correlates with down here</h2>','<h2>4. What "cheap" actually correlates with down here</h2>')
t=rep(t,'<h2>4. Reading this alongside the two earlier pieces</h2>','<h2 id="reading">5. Three levels of zoom</h2>')
t=rep(t,'2,086 of them, or 43% of the entire under-₹1,000 universe from the previous piece','2,086 of them, or 43% of the entire under-₹1,000 universe in section 1')
t=rep(t,'Same methodology as both earlier pieces —','Same methodology as section 1 —')
t=rep(t,'has the worst Sharpe ratio of any price segment measured across all three of this blog\'s price-band pieces','has the worst Sharpe ratio of any price segment this blog has measured')
t=rep(t,'worse across the board than the ₹250-plus sub-bands in the previous piece','worse across the board than the ₹250-plus sub-bands in section 1')
t=rep(t,'<p>Three pieces, three levels of zoom, and the pattern gets more extreme every time the lens narrows:',
 '<p>Three levels of zoom, and the pattern gets more extreme every time the lens narrows:')
t=rep(t,'The mechanism is the same one identified in the previous piece — price under roughly ₹250',
 'The mechanism is the one section 1 points to. The finding of the broad five-band comparison, that price and risk are not cleanly related, still holds among stocks priced above ₹1,000: those bands showed betas clustered close to 1.0 with no clean order. The relationship reappears only at the bottom, because price under roughly ₹250')
t=rep(t,'is doing double duty as a rough proxy for market capitalisation, which is the thing that\'s actually moving with risk.',
 'is doing double duty as a rough proxy for market capitalisation, which is the thing that\'s actually moving with risk. Genuinely small companies rarely get split or bonus-issued down from a high share price the way established companies do, so at the very bottom of the market a low price and a small company tend to go together.')
t=rep(t,'— 2,086 stocks, 43% of the entire under-₹1,000 universe from the first piece in this series — is the single worst-performing, highest-risk price segment identified anywhere across all three pieces:',
 '— 2,086 stocks, 43% of the entire under-₹1,000 universe — is the single worst-performing, highest-risk price segment identified at any level of zoom:')
t=rep(t,'<div class="verdict">Verdict: <strong>The basement has a sub-basement.</strong> Splitting "under ₹250"',
 '<div class="verdict">Verdict: <strong>The basement has a sub-basement.</strong> Splitting "under ₹1,000" four ways puts 79% of those stocks below ₹250, where the median company is worth ₹80 crore and the median trailing-year return is &minus;17.7%. Splitting "under ₹250"')

# related
t=rep(t,'<p><span>See also:</span> <a href="'+B_URL+'">Below ₹250 Is Where the Real Junk Lives</a> — the first split of the under-₹1,000 band this piece drills further into. · <a href="https://masaladeutsch.blogspot.com/2026/08/a-slice-of-apple-costs-about-1700-slice.html">A Slice of Apple Costs About ₹1,700. A Slice of MRF Still Isn\'t Legal.</a> — the original five-band price segmentation this whole series builds on.</p>',
 '<p><span>See also:</span> <a href="https://masaladeutsch.blogspot.com/2026/08/a-slice-of-apple-costs-about-1700-slice.html">A Slice of Apple Costs About ₹1,700. A Slice of MRF Still Isn\'t Legal.</a> — the original five-band price segmentation this piece splits further. · <a href="https://masaladeutsch.blogspot.com/2026/08/why-bet-on-one-horse-when-you-can-buy.html">Why Bet on One Horse, When You Can Buy the Stable?</a> — the Markowitz/Sharpe-ratio framework and methodology used here.</p>')
assert B_URL not in t and 'below-250-is-where' not in t

# what would fix this
ul=grab(t,'<h2>What would fix this</h2>\n<ul>','</ul>')+'</ul>'
t=rep(t,ul,'<h2>What would fix this</h2>\n<ul>\n'
'<li><b>NSE and BSE should publish a quarterly table of listed stocks by price band and by market-capitalisation band, with count, median market cap, median traded value, median return, volatility and beta, and the share paying any dividend</b>, so that the ₹0&ndash;250 band&rsquo;s ₹80 crore median company and the ₹0&ndash;50 band&rsquo;s zero median dividend yield are visible from exchange data, not only from private screeners and one-off studies.</li>\n'
'<li><b>NSE and BSE should show each stock&rsquo;s market capitalisation and average daily traded value next to its share price on their public quote pages and in broker data feeds</b>, so a low share price is not read as a measure of size.</li>\n'
'<li><b>NSE and BSE should publish free, corporate-action-adjusted daily price histories for every listed security, including BSE-only scrips, with the days each was suspended or untraded</b>, so gaps like the 181 of 1,267 ₹0&ndash;250 stocks without enough continuous history for a beta can be explained rather than silently dropped.</li>\n'
'<li><b>SEBI should require brokers&rsquo; order screens to show market capitalisation band, average daily traded value and trailing dividend next to the price, using one standard definition across brokers, at least for stocks quoted under ₹250</b>, so that a low price tag is not read as a proxy for value when it tracks small size and high beta instead.</li>\n'
'<li><b>SEBI should direct the exchanges to publish an annual report on retail participation by price band, showing unique investors and retail share of turnover</b>, so that it is measurable how many savers sit in the segment with the worst Sharpe ratio (0.20) and median 1-year return (&minus;22.7%) found here.</li>\n'
'</ul>')

# sources
t=rep(t,'<li>Price segmentation, returns, profit-growth and dividend-yield data for the 3,850 stocks under ₹250, split into four ₹50-wide sub-bands — Screener.in company data, 11 Aug 2026</li>',
 '<li>Price-band segmentation and returns/profit-growth data for the 4,862 stocks under ₹1,000, split into four sub-bands, and returns, profit-growth and dividend-yield data for the 3,850 stocks under ₹250, split into four ₹50-wide sub-bands — Screener.in company data, 11 Aug 2026</li>')
# disclaimer: add the under-1,000 coverage note
t=rep(t,'a limitation shared with, and consistent in scale to, the earlier pieces in this series.</p>',
 'a limitation shared with, and consistent in scale to, the earlier pieces in this series. In section 1, 1,086 of the 1,267 priced ₹0&ndash;250 stocks had enough continuous weekly history for a reliable beta, a real but partial sample of the full 3,850-stock band.</p>')
open(ROOT+'out/update-2026-11-10-050-is-its-own-category-diving-into.html','w').write(t)
print(len(t))

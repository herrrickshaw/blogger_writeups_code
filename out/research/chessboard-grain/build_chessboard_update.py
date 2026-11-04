"""Update for the-chessboard-and-indias-granaries (4 Nov 2026).

Takes the body as supplied (post_1_as_supplied.html), checks the arithmetic, replaces the
[[IMAGE]] placeholder with an inline SVG of the board and harvest bars, and corrects the
years in which the harvest first reached squares 51-53 and the FCI silo figure.
"""
import math, pathlib, re

HERE = pathlib.Path(__file__).parent
OUT = HERE.parents[1] / 'update-2026-11-04-the-chessboard-and-indias-granaries.html'
WHEAT_T = 65e-9                      # tonnes per wheat grain (65 mg)
cum = lambda n: (2**n - 1) * WHEAT_T  # tonnes on squares 1..n

def square(t):                        # first square whose cumulative pile exceeds t tonnes
    n = 1
    while cum(n) < t:
        n += 1
    return n

# --- arithmetic checks against the supplied text ---------------------------------------
assert 2**64 - 1 == 18446744073709551615
assert round(cum(64) / 1e12, 1) == 1.2                  # ~1.2 trillion t
assert [square(x * 1e5) for x in (210.40, 604.02, 917.83, 3765.6)] == [49, 50, 51, 53]
assert round(cum(64) / 917.83e5, -3) == 13000            # ~13,000 x storage
assert round(cum(64) / 376.56e6, -2) == 3200             # ~3,200 years of harvest
assert square(1617.83e5) == 52                           # storage + 700 lakh t
RICE_SHIFT = [square(x * 1e5 * 65 / 25) - square(x * 1e5) for x in (917.83, 3765.6)]
assert RICE_SHIFT == [1, 1]                              # 25 mg rice: one square later
# first years the harvest crossed each square (RBI Handbook, million tonnes)
FIRST = {51: ('1958-59', 77.14), 52: ('1983-84', 152.37), 53: ('2019-20', 297.5)}
for sq, (yr, mt) in FIRST.items():
    assert square(mt * 1e6) == sq, (yr, square(mt * 1e6))
# previous highs stayed below the thresholds: 1953-54 69.82, 1981-82 133.30, 2018-19 285.21
for sq, mt in ((51, 69.82), (52, 133.30), (53, 285.21)):
    assert square(mt * 1e6) < sq

# --- figure -----------------------------------------------------------------------------
GREY, GREEN, LINE, INK, MUTED = '#d6d3cc', '#9fe0c9', '#6b6b6b', '#222', '#555'
def board_svg():
    s, x0, y0 = 52, 24, 16
    out = [f'<svg viewBox="0 0 464 520" role="img" aria-labelledby="cbT" style="width:100%;max-width:460px;height:auto;display:block;margin:0 auto;font-family:-apple-system,\'Segoe UI\',sans-serif">',
           '<title id="cbT">Chessboard: squares 1 to 49 were covered by the 1950-51 harvest; 50 to 53 were reached between 1950-51 and 2025-26; 54 to 64 are still ahead</title>',
           '<rect width="464" height="520" fill="#fff"/>']
    for n in range(1, 65):
        r, c = divmod(n - 1, 8)
        x, y = x0 + c * s, y0 + (7 - r) * s
        fill = GREY if n <= 49 else GREEN if n <= 53 else '#fff'
        out.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{fill}" stroke="{LINE}" stroke-width="1"/>')
        if n in (1, 8, 32, 49, 50, 51, 52, 53, 54, 64):
            out.append(f'<text x="{x + s/2}" y="{y + s/2 + 6}" text-anchor="middle" font-size="17" fill="{INK}">{n}</text>')
    ly = y0 + 8 * s + 30
    for i, (fill, lab) in enumerate(((GREY, 'By 1950-51'), (GREEN, '1950-51 to 2025-26'), ('#fff', 'Still ahead'))):
        lx = x0 + [0, 140, 330][i]
        out.append(f'<rect x="{lx}" y="{ly - 14}" width="18" height="18" fill="{fill}" stroke="{LINE}"/>')
        out.append(f'<text x="{lx + 26}" y="{ly}" font-size="15" fill="{INK}">{lab}</text>')
    out.append(f'<text x="{x0}" y="{ly + 34}" font-size="13" fill="{MUTED}">Squares numbered from bottom left; wheat grain of 65 mg</text>')
    out.append('</svg>')
    return '\n'.join(out)

HARVEST = [('1950-51', 51), ('1960-61', 82), ('1970-71', 108), ('1980-81', 130), ('1990-91', 176),
           ('2000-01', 197), ('2010-11', 244), ('2020-21', 311), ('2025-26', 377)]
def bars_svg():
    lx, bx, seg, top, row = 8, 150, 62, 44, 40
    w = bx + 4 * seg + 70
    h = top + row * len(HARVEST) + 30
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-labelledby="hbT" style="width:100%;max-width:460px;height:auto;display:block;margin:1rem auto 0;font-family:-apple-system,\'Segoe UI\',sans-serif">',
           '<title id="hbT">India\'s foodgrain harvest by decade, placed on squares 50 to 53 of the board</title>',
           f'<rect width="{w}" height="{h}" fill="#fff"/>']
    for k in range(4):
        out.append(f'<text x="{bx + k * seg + seg/2}" y="{top - 14}" text-anchor="middle" font-size="14" fill="{MUTED}">sq {50 + k}</text>')
    lo = cum(49)
    for i, (yr, mt) in enumerate(HARVEST):
        y = top + i * row
        pos = math.log2(mt * 1e6 / lo) * seg        # one segment per doubling
        out.append(f'<text x="{lx}" y="{y + 19}" font-size="16" fill="{INK}">{yr}</text>')
        out.append(f'<text x="{bx - 8}" y="{y + 19}" text-anchor="end" font-size="14" fill="{MUTED}">{mt} Mt</text>')
        out.append(f'<rect x="{bx}" y="{y + 4}" width="{4 * seg}" height="22" fill="#fff" stroke="{LINE}"/>')
        for k in range(1, 4):
            out.append(f'<line x1="{bx + k * seg}" y1="{y + 4}" x2="{bx + k * seg}" y2="{y + 26}" stroke="{LINE}"/>')
        out.append(f'<rect x="{bx}" y="{y + 4}" width="{pos:.1f}" height="22" fill="{GREEN}" stroke="#2f8f6f"/>')
        out.append(f'<text x="{bx + 4 * seg + 8}" y="{y + 20}" font-size="14" fill="{INK}">sq {square(mt * 1e6)}</text>')
    out.append(f'<text x="{lx}" y="{h - 8}" font-size="13" fill="{MUTED}">Source: RBI Handbook; 2025-26 Third Advance Estimate</text>')
    out.append('</svg>')
    return '\n'.join(out)

FIG = ('<figure style="margin:1.4rem 0">\n' + board_svg() + '\n' + bars_svg() +
       '\n<figcaption style="font-size:.85em;color:#555;margin-top:.5rem">Every harvest since independence fits inside squares 50 to 53. '
       'The bars use a doubling scale: each segment is twice the grain of the one before.</figcaption>\n</figure>')

NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
        '<b>Updated 4 November 2026.</b> Added the board chart, the Ambalappuzha version of the legend and sections placing world grain volumes and the land that grows them on the board. Corrected the years in which the harvest first reached squares 51, 52 and 53 '
        '(1958-59, 1983-84 and 2019-20, not the 1960s, 1990-91 and 2020-21), and the FCI silo programme (111 lakh tonnes planned in 2022, of which about '
        '19.5 lakh tonnes had been built by mid-2025).</div>')

def rep(s, a, b):
    assert s.count(a) == 1, a[:70]
    return s.replace(a, b)

s = (HERE / 'post_1_as_supplied.html').read_text()
s = rep(s, '<h2>The legend</h2>', NOTE + '\n<h2>The legend</h2>')
s = rep(s, '<p>[[IMAGE]]</p>', FIG)

# --- global context (added 4 Nov 2026, second pass) ----------------------------------------
WORLD = [  # label, million tonnes, source note
    ('World cereal trade, 2026/27 forecast', 509.3, 'FAO, August 2026 brief'),
    ('India foodgrain production, 2025-26', 376.56, 'Third Advance Estimate'),
    ('China grain output, 2025', 714.88, 'National Bureau of Statistics'),
    ('World cereal stocks, end of 2026/27', 957.8, 'FAO, July 2026 brief'),
    ('World cereal production, 2026', 2979, 'FAO, October 2026 brief'),
]
SQ = {lab: square(mt * 1e6) for lab, mt, _ in WORLD}
assert [SQ[w[0]] for w in WORLD] == [53, 53, 54, 54, 56]
YEARS_WORLD = cum(64) / 2979e6
assert round(YEARS_WORLD, -1) == 400
RATIO = 2979 / 376.56
assert 7.5 < RATIO < 8.5                       # about three doublings
SHARE_TRADE = 376.56 / 509.3
assert round(SHARE_TRADE * 100) == 74
rows = ''.join(f'<tr><td>{lab}</td><td>{mt:,.0f} Mt</td><td>{SQ[lab]}</td></tr>\n' for lab, mt, _ in WORLD)
GLOBAL = f"""<h2>The world on the same board</h2>
<p>Put the rest of the world's grain on the same board, with the same 65 mg grain, and India's harvest stops looking like the edge of the board.</p>
<table border="1" cellpadding="6" style="border-collapse:collapse">
<thead>
<tr>
<th>Benchmark</th>
<th>Size</th>
<th>Square reached</th>
</tr>
</thead>
<tbody>
{rows}</tbody>
</table>
<p><strong>The world's whole cereal harvest sits on square 56</strong>, three squares beyond India's. Three squares is three doublings: the world grows about {RATIO:.0f} times what India does, which is roughly what India's one-eighth share of world output implies. Even so, the full board would take about {round(YEARS_WORLD, -1):,.0f} years of the entire world's harvest to fill.</p>
<p><strong>India's harvest and the world's grain trade share a square.</strong> All the wheat, maize, rice and other cereals that cross a border in a year, about 509 million tonnes, land on square 53, the same square as India's harvest. India grows the equivalent of about {SHARE_TRADE * 100:.0f}% of the world's annual cereal trade, which is why its decisions to ban or release rice and wheat exports move world prices.</p>
<p><strong>China is one square ahead.</strong> Its 2025 grain output of 714.88 million tonnes, a record, reached square 54, as do the world's cereal stocks at the end of 2026/27, forecast at about 958 million tonnes. The year after a record 2025 harvest, FAO expects world production to dip about 2%, mostly on lower wheat crops; on this board, that is invisible.</p>
<p>These totals are not quite like for like. FAO counts cereals only, with rice in milled terms. India's foodgrain figure includes pulses and rice as milled output. China's "grain" also includes soybeans and tubers. None of the differences is large enough to move a benchmark by a square.</p>
"""
s = rep(s, '<h2>What the board teaches about storage policy</h2>', GLOBAL + '<h2>What the board teaches about storage policy</h2>')

# --- how much land grows it (added 4 Nov 2026, third pass) -----------------------------------
HARVESTED_WORLD = 1490e6        # ha, all crops, 2023 (FAO)
CEREAL_SHARE = 0.50             # cereals' share of harvested area, 2023 (FAO)
CEREAL_AREA_WORLD = HARVESTED_WORLD * CEREAL_SHARE          # ~745 Mha, derived
CROPLAND_WORLD = 1600e6         # ha, 2023 (FAO)
EARTH_LAND = 148.94e6 * 100     # km2 -> ha
IND_AREA, IND_CEREAL_AREA = 142.325e6, 113.679e6           # foodgrain / cereal area 2025-26 (RBI Handbook table)
CHN_AREA = 119.4e6              # grain area 2025 (NBS)
y_world = 2979e6 / CEREAL_AREA_WORLD
y_ind = 376.56e6 / IND_AREA
y_chn = 714.88e6 / CHN_AREA
assert round(y_world, 1) == 4.0 and round(y_ind, 2) == 2.65 and round(y_chn, 1) == 6.0
board_ha = cum(64) / y_world
earths = board_ha / EARTH_LAND
assert 19 < earths < 21
need54 = cum(53)                                            # harvest must exceed this to reach square 54
area54_now = need54 / y_ind
yield54_now_area = need54 / IND_AREA
area54_china = need54 / y_chn
assert square(need54 + 1) == 54 and round(area54_now / 1e6, -1) == 220
assert round(yield54_now_area, 1) == 4.1 and round(area54_china / 1e6) == 98
share_area = IND_CEREAL_AREA / CEREAL_AREA_WORLD
assert round(share_area * 100) == 15

LAND = f"""<h2>How much land grows it</h2>
<p>The board counts grain; farms grow it on land. The world has about 1.6 billion hectares of cropland, and in 2023 it harvested crops from about 1.49 billion hectares, a 23-year high. Cereals took about half of that harvested area, so roughly {CEREAL_AREA_WORLD / 1e6:,.0f} million hectares of wheat, maize, rice and other grains a year. That gives a world average of about {y_world:.1f} tonnes of cereal per hectare.</p>
<table border="1" cellpadding="6" style="border-collapse:collapse">
<thead>
<tr>
<th>Grower</th>
<th>Million ha</th>
<th>t/ha</th>
</tr>
</thead>
<tbody>
<tr><td>World cereals*</td><td>~{CEREAL_AREA_WORLD / 1e6:,.0f}</td><td>~{y_world:.1f}</td></tr>
<tr><td>China grain, 2025</td><td>119.4</td><td>{y_chn:.1f}</td></tr>
<tr><td>India foodgrains, 2025-26</td><td>142.3</td><td>{y_ind:.2f}</td></tr>
</tbody>
</table>
<p style="font-size:.85em;color:#555">*2026 output of 2,979 Mt over the 2023 cereal area. Output for China (714.88 Mt) and India (376.56 Mt) as in the table above.</p>
<p><strong>India farms more grain land than China and gets about half the grain.</strong> Its cereal fields alone, about 114 million hectares, are some {share_area * 100:.0f}% of the world&rsquo;s cereal area, yet India grows about an eighth of the world&rsquo;s grain. Part of the gap is that India&rsquo;s figure includes 28.6 million hectares of pulses, which yield far less than cereals; the rest is lower cereal yield.</p>
<p><strong>The full board would need about {earths:.0f} Earths.</strong> At the world&rsquo;s average yield, growing the whole board&rsquo;s grain in one season would take about {board_ha / 1e9:,.0f} billion hectares, some {earths:.0f} times the entire land surface of the planet, ice caps and deserts included.</p>
<p><strong>Square 54 is a yield problem, not a land problem.</strong> To move up a square, India&rsquo;s harvest would have to pass about {need54 / 1e6:,.0f} million tonnes. At today&rsquo;s yield that would need about {area54_now / 1e6:,.0f} million hectares of foodgrains, more than half as much land again as India now sows to them. On the land it already uses, it would need about {yield54_now_area:.1f} tonnes a hectare, roughly today&rsquo;s world average. At China&rsquo;s yield, about {area54_china / 1e6:.0f} million hectares would do.</p>
<p>The world figures mix years and definitions: the cereal area is half of FAO&rsquo;s 2023 harvested area, not a direct cereal count, and FAO measures rice output milled while yields are usually quoted on paddy. Treat the world yield as approximate; it does not change which square anything lands on.</p>
"""
s = rep(s, '<h2>What the board teaches about storage policy</h2>', LAND + '<h2>What the board teaches about storage policy</h2>')
s = rep(s, '<li><a href="https://www.dailyexcelsior.com/?p=2225570">',
        '<li><a href="https://www.fao.org/statistics/highlights-archive/highlights-detail/land-statistics-2001-2023.-global--regional-and-country-trends/en">FAO &mdash; Land statistics 2001&ndash;2023 (cropland of about 1.6 billion ha)</a></li>\n'
        '<li><a href="https://millingmea.com/global-harvested-crop-area-hits-23-year-high-as-cereals-organic-farming-expand-fao/">Milling MEA, reporting FAO &mdash; harvested area of 1.49 billion ha in 2023, about half of it cereals</a></li>\n'
        '<li><a href="https://dataful.in/datasets/17944/">Dataful, from the RBI Handbook &mdash; India&rsquo;s foodgrain area, 2025-26 (cereals 113.68, pulses 28.65 million ha)</a></li>\n'
        '<li><a href="https://www.chinadaily.com.cn/a/202512/12/WS693b844ea310d6866eb2e502.html">China Daily &mdash; China&rsquo;s grain area of 119.4 million ha in 2025</a></li>\n'
        '<li><a href="https://en.wikipedia.org/wiki/Earth">Wikipedia &mdash; Earth&rsquo;s land area, 148.94 million km&sup2;</a></li>\n'
        '<li><a href="https://www.dailyexcelsior.com/?p=2225570">')
s = rep(s, '<li><a href="https://www.dailyexcelsior.com/?p=2225570">',
        '<li><a href="https://www.fao.org/worldfoodsituation/fao-cereal-supply-and-demand-brief/en">FAO Cereal Supply and Demand Brief &mdash; world production (October 2026), stocks (July) and trade (August)</a></li>\n'
        '<li><a href="https://news.cgtn.com/news/2025-12-12/China-s-grain-output-tops-714-million-tonnes-in-2025-1J2N7j6Fb8I/p.html">CGTN &mdash; China&rsquo;s grain output of 714.88 million tonnes in 2025 (National Bureau of Statistics)</a></li>\n'
        '<li><a href="https://www.dailyexcelsior.com/?p=2225570">')
s = rep(s, 'Long before the board is full, the royal granaries are empty.</p>',
        'Long before the board is full, the royal granaries are empty.</p>\n'
        '<p>Kerala tells its own version at the <a href="https://en.wikipedia.org/wiki/Ambalappuzha_Sree_Krishna_Swamy_Temple">Ambalappuzha Sree Krishna Swamy Temple</a> in Alappuzha. '
        'There the sage is Krishna in disguise, the king of the region loses a game of chess to him, and the grain is rice. When the king cannot pay, '
        'Krishna lets him settle the debt in instalments: rice served as <em>paal payasam</em>, sweet milk porridge, to pilgrims at the temple every day until the debt is cleared. '
        'The temple still serves it. On the board below, a rice grain is lighter than wheat, so the debt in rice is about 461 billion tonnes rather than 1.2 trillion &mdash; and still unpayable.</p>')
s = rep(s, 'The harvest reached square 51 in the 1960s, square 52 by 1990-91, and square 53 in 2020-21. Each new square means doubling everything grown before.',
        'The harvest first reached square 51 in 1958-59 (77 million tonnes), square 52 in 1983-84 (152 million tonnes) and square 53 in 2019-20 (298 million tonnes). '
        'Each new square needs a harvest twice the size of the threshold before it: the gaps between them were 25 years and then 36.')
s = rep(s, '<li>FCI&#x27;s silo programme (over 108 lakh tonnes planned) modernises storage on square 51 rather than moving to a new square.</li>'
        if '&#x27;' in s else "<li>FCI's silo programme (over 108 lakh tonnes planned) modernises storage on square 51 rather than moving to a new square.</li>",
        "<li>FCI's steel-silo programme (about 111 lakh tonnes at 249 locations, announced in 2022, with about 19.5 lakh tonnes built by mid-2025) modernises storage on square 51 rather than moving to a new square.</li>")
s = rep(s, '"Square reached" is where the cumulative pile first exceeds the benchmark.',
        '"Square reached" is where the cumulative pile first exceeds the benchmark, using the 65 mg wheat grain; with a 25 mg rice grain, storage and the harvest would each reach one square later.')
s = rep(s, '<li><a href="https://www.dailyexcelsior.com/?p=2225570">Daily Excelsior — FCI silo programme</a></li>',
        '<li><a href="https://www.dailyexcelsior.com/?p=2225570">Daily Excelsior — FCI silo programme</a></li>\n'
        '<li><a href="https://theprint.in/india/fci-to-construct-modern-steel-silos-under-hub-and-spokes-model-across-country-under-ppp/1174803/">ThePrint — FCI steel silos under the hub-and-spoke PPP model (111 lakh tonnes, 249 locations)</a></li>\n'
        '<li><a href="https://www.outlookbusiness.com/news/nearly-20-lt-steel-silo-capacity-created-since-2014-to-store-grains-65-lt-in-process">Outlook Business — about 19.5 lakh tonnes of silos built, more under construction (2025)</a></li>')
for t in ('div', 'p', 'table', 'tr', 'td', 'ul', 'svg', 'figure'):
    assert len(re.findall(rf'<{t}[\s>]', s)) == len(re.findall(f'</{t}>', s)), t
OUT.write_text(s)
print('written', OUT, 'first squares ok; rice shift', RICE_SHIFT)

import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-aeb-mandate.html'

# ---------------------------------------------------------------- data
PV_FY26 = 46_43_439            # SIAM domestic passenger-vehicle wholesales, FY2025-26
PV_FY25 = 43_01_848
ADAS_2024, ADAS_2025 = 6.43, 8.41   # % of PV sales with ADAS, calendar years (Counterpoint)
DEATHS_2023 = 1_72_890         # MoRTH, Road Accidents in India 2023
REAR_SHARE_ACC, REAR_SHARE_DEATH = 21, 20   # "hit from back", % of accidents / deaths, 2023 (as reported)
RADAR_IMP_CR = 486             # HS 85261000 radar apparatus imports FY2024-25, Rs crore (TradeStat via trade-data site)
RADAR_IMP_GROWTH = 229.6       # % y-o-y
CHINA_AUTO_COMP = 36           # % of India's auto-component imports from China, FY26 (ACMA, as reported)
AIRBAG_4_COST = 6000           # Rs, variable cost of four extra airbags, Dec 2022 parliamentary reply

adas_cars = PV_FY26 * ADAS_2025 / 100
without = PV_FY26 - adas_cars
rear_deaths = DEATHS_2023 * REAR_SHARE_DEATH / 100
assert round(adas_cars, -3) == 391000

# Timeline: (label, year as decimal, colour, row)
EVENTS = [
    ("EU: new car types", 2022.5, "#495057", 0), ("EU: all new cars", 2024.5, "#495057", 1),
    ("US: all new light vehicles", 2029.67, "#868e96", 2),
    ("Bharat NCAP 2.0 (AEB optional)", 2027.75, "#d9a441", 3),
    ("India: cars with AEB meet AIS-185", 2028.75, "#a5402c", 4),
    ("India: new car models", 2030.75, "#a5402c", 5), ("India: all cars", 2032.75, "#a5402c", 6),
]


def chart_timeline():
    W, L, R, top, rh = 400, 10, 10, 30, 26
    y0, y1 = 2022, 2034
    H = top + 7 * rh + 34
    sx = (W - L - R) / (y1 - y0)
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="When automatic emergency braking becomes compulsory: EU new cars July 2024, US September 2029, India new car models October 2030 and all cars October 2032.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">When emergency braking becomes compulsory in new cars</text>']
    for yr in range(y0, y1 + 1, 2):
        x = L + (yr - y0) * sx
        s.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{top + 7 * rh - 8}" stroke="#e9ecef"/>')
        s.append(f'<text x="{x:.1f}" y="{top + 7 * rh + 4}" font-size="9.5" fill="#6c757d" text-anchor="middle">{yr}</text>')
    for lab, yr, col, row in EVENTS:
        x = L + (yr - y0) * sx
        y = top + row * rh
        s.append(f'<circle cx="{x:.1f}" cy="{y + 6}" r="5" fill="{col}"/>')
        anchor, tx = ("end", x - 8) if x > W * 0.5 else ("start", x + 8)
        s.append(f'<text x="{tx:.1f}" y="{y + 10}" font-size="10" fill="#212529" text-anchor="{anchor}">{lab}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">EU: Regulation 2019/2144. US: FMVSS 127 (2024). India: MoRTH draft, October 2026,</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">open for comment; Bharat NCAP 2.0 protocol expected October 2027.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_rules():
    return table(["Rule", "What it requires", "From"], [
        ("India: MoRTH draft amendment to the Central Motor Vehicles Rules (October 2026)", "Cars (category M1, up to eight passenger seats) that offer AEB must meet the AIS-185 standard; then AEB in every new model; then in every car built", "1 Oct 2028; 1 Oct 2030; 1 Oct 2032"),
        ("India: AIS-185 (based on UN Regulation 152)", "Tests against a car ahead and against a pedestrian; a cyclist test is reserved for later", "With the rule above"),
        ("India: Bharat NCAP 2.0 (draft)", "Electronic stability control and side head protection to qualify for a rating; AEB tests optional, inside a 10-point accident-avoidance score out of 100", "Expected Oct 2027"),
        ("European Union: General Safety Regulation 2019/2144", "AEB detecting vehicles and pedestrians in new cars and vans", "New types July 2022; all new cars July 2024"),
        ("United States: FMVSS 127", "AEB and pedestrian AEB in all light vehicles, with braking at higher speeds than the UN rule", "Sept 2029"),
    ])


def t_parts():
    return table(["Part", "What it does", "Made in India?"], [
        ("Front radar (77 GHz)", "Measures distance and closing speed to the vehicle ahead, in rain and dark", "Partly: HL Klemove began assembling ADAS radar in Chennai in April 2024; Valeo makes radars at Sanand. Radar chips are imported"),
        ("Front camera", "Recognises cars, pedestrians and lane markings", "Partly: Visteon and Valeo are localising camera modules; image sensors and processors are imported"),
        ("Control unit and software", "Fuses the two, decides when to warn and brake", "Varies by supplier; the processors are imported"),
        ("Brake actuator (stability-control unit)", "Applies the brakes without the driver", "Fitted on many Indian cars, but AEB works only on cars that have it"),
    ])


def t_history():
    return table(["Mandate", "What happened"], [
        ("Six airbags in every car (draft January 2022)", f"Set for October 2022, deferred to October 2023, then dropped in September 2023; the minister said Bharat NCAP ratings would push carmakers instead. The government had put the variable cost of four extra airbags at about Rs {AIRBAG_4_COST:,}"),
        ("Electronic stability control", "Announced in 2018 for cars from 2022&ndash;23; no mandate for cars was found. The AIS-133 standard applies only to cars that fit it"),
        ("AEB and other driver aids for buses and trucks", "Notified for new models from April 2026 in one account; later reports give October 2027 for parts of it. The current schedule could not be confirmed"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{ADAS_2025:.1f}%</b><span>of cars sold in 2025 had driver-assistance systems that include emergency braking, up from {ADAS_2024:.1f}% in 2024</span></div>
<div class="gb-stat"><b>~{without / 1e5:.0f} lakh</b><span>cars a year would need emergency braking added, at 2025-26 sales and today&rsquo;s fitment rate</span></div>
<div class="gb-stat"><b>~{rear_deaths / 1000:.0f},000</b><span>deaths in 2023 in crashes where a vehicle was hit from behind, about a fifth of all road deaths</span></div>
<div class="gb-stat"><b>Oct 2032</b><span>when the draft rule would make AEB compulsory in every car built; Europe got there in 2024</span></div>
</div>'''

body = f"""
{stats}

<p>On about 19 October the Ministry of Road Transport and Highways published a draft rule that would make advanced emergency braking (AEB) compulsory in passenger cars: in every new model from 1 October 2030 and in every car built from 1 October 2032. AEB uses a radar, a camera or both to watch the road ahead, warns the driver of an impending collision and brakes on its own if the driver does not. The draft is open for 30 days of comment.</p>
<p>This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/airbags-and-seat-belts-are-import-heavy.html">piece on automotive textiles</a> found that airbags and seat belts are among the most import-dependent parts of a car. AEB moves car safety from fabric to electronics, which India imports even more of. This piece sets out what the rule requires, how it compares with Europe and the US, what the hardware is and where it comes from, and what the earlier airbag mandate suggests about whether the dates will hold.</p>

<h2 class="gb-h2">What the draft requires, and how late it is</h2>
{chart_timeline()}
{t_rules()}
<p>India&rsquo;s standard, AIS-185, is built on the UN&rsquo;s Regulation 152, the same basis as Europe&rsquo;s. Europe has required AEB in every new car since July 2024, and the US will from September 2029, with a tougher test that brakes at higher speeds. India&rsquo;s full requirement would arrive eight years after Europe&rsquo;s. The gap is partly deliberate: the draft gives carmakers four years to redesign new models and six to change models already in production.</p>
<p>Bharat NCAP, India&rsquo;s voluntary crash-rating programme, will not close the gap first. Its 2.0 protocol, expected from October 2027, requires stability control for a rating but leaves AEB tests optional, inside an accident-avoidance score worth 10 of 100 points.</p>

<h2 class="gb-h2">Fewer than one in ten new cars has it now</h2>
<p>Counterpoint Research estimates that {ADAS_2025:.2f}% of passenger vehicles sold in 2025 had advanced driver-assistance systems, up from {ADAS_2024:.2f}% in 2024. Applied to the {PV_FY26 / 1e5:.2f} lakh cars sold in 2025-26, that is about {adas_cars / 1e5:.1f} lakh cars with the systems and about {without / 1e5:.0f} lakh without. Most equipped cars are utility vehicles, according to CRISIL. The cheapest car with full driver assistance listed in recent comparisons is the top automatic variant of the Maruti Baleno at Rs 9.99 lakh ex-showroom; lower variants of the same car go without it.</p>
<p>The case for the rule is the crash data. In 2023, India recorded {DEATHS_2023:,} road deaths. Crashes where a vehicle was hit from behind were the most common type, about {REAR_SHARE_ACC}% of accidents and {REAR_SHARE_DEATH}% of deaths, or about {rear_deaths:,.0f} deaths. AEB in cars addresses only part of that: those where a car is the vehicle doing the hitting, and those where it hits a pedestrian. The ministry&rsquo;s report does not break the figure down that way.</p>

<h2 class="gb-h2">What AEB needs, and where it comes from</h2>
{t_parts()}
<p>The hardware is the import question. Imports under the customs line for radar apparatus (HS 85261000) were about Rs {RADAR_IMP_CR} crore in 2024-25, {RADAR_IMP_GROWTH:.0f}% more than a year earlier, on commerce ministry data reported by a trade-statistics site. That line covers all radar, not only car radar, but car radar is the part that is growing. China supplied about {CHINA_AUTO_COMP}% of India&rsquo;s auto-component imports in 2025-26, according to the component makers&rsquo; association as reported. Local assembly of radars and cameras has begun, but the chips inside them, the radar transceivers, image sensors and processors, are imported; this blog found no Indian production of them.</p>
<p>A cheaper design is emerging. Suzuki, Maruti&rsquo;s parent, says it is developing AEB that drops the radar and uses cameras with an AI chip, and the supplier Aumovio has shown a single-camera system aimed at small cars. A camera-only system would cut the number of imported parts, though not the chips. Either way, AEB can only brake the car through an electronic stability-control unit, so a mandate for AEB is in practice also a mandate for stability control, for which this blog found no mandate in Indian cars.</p>

<h2 class="gb-h2">What the airbag mandate suggests</h2>
{t_history()}
<p>India has been here before. The six-airbag rule was drafted in January 2022, deferred a year because the industry said it lacked capacity, and dropped in September 2023 in favour of letting crash ratings push carmakers. That approach has worked to a degree: the minister said at the time that carmakers offering six airbags were gaining market share. But AEB is a harder sell to buyers than airbags, because its benefit is invisible until it works. The long lead time in the draft, and the fact that it builds on a UN standard that suppliers already meet in Europe, make it more likely to hold than the airbag rule was. Whether it does will be decided in the comment period now running.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>MoRTH should publish, with the final rule, its estimate of cost per car and lives saved, as the US regulator did for its rule, so the dates can be weighed against the benefit.</li>
<li>MoRTH&rsquo;s annual road-accident report should split rear-end and pedestrian crashes by the type of the striking vehicle, so the share AEB in cars can address is known.</li>
<li>The rule should make electronic stability control compulsory in cars on the same timetable, since AEB depends on it.</li>
<li>Bharat NCAP 2.0 should make AEB tests compulsory for a five-star rating from 2029, so ratings reward it before the mandate arrives.</li>
<li>The government should track imports of automotive radar and camera modules under their own tariff lines, so localisation can be measured.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The draft notification and AIS-185 could not be opened directly; the dates come from news reports, which agree on 2030 for new models and 2032 for all cars but differ on wording. No reliable estimate of the cost of AEB per car in India was found; the per-airbag figure is a comparison, not a proxy. The ADAS share is a market-research estimate on calendar-year sales applied here to fiscal-year sales. The rear-end shares are as reported from the ministry&rsquo;s 2023 report, and one outlet gives 23% of accidents instead of 21%. The radar import figure covers a whole customs line, not car radar alone. The status of the bus and truck mandate could not be confirmed.</p>
"""

sources = ("Draft rule: MoRTH draft amendment to the Central Motor Vehicles Rules, October 2026, as reported by Autocar Professional, Autocar India, ThePrint, Telangana Today, Times Drive and News On AIR; AIS-185 structure per ARAI drafts and Shankar IAS. Bharat NCAP 2.0 draft: Team-BHP, Gaadify, Smartprix (2026). EU: Regulation (EU) 2019/2144 and Ireland&rsquo;s Road Safety Authority; US: NHTSA, FMVSS 127 final rule (2024) and Federal Register. "
           "Sales and fitment: SIAM via Outlook Business (FY2025-26); Counterpoint Research, Ken Research and CMR on ADAS penetration (2025&ndash;26); car prices per Acko Drive and Zurich Kotak (2026). Road deaths: MoRTH, Road Accidents in India 2023, via DT Next and The Week; collision-type shares via NewsGram. "
           "Hardware and suppliers: HL Klemove (Autocar Professional, S&amp;P Global Mobility, April 2024); Visteon and Valeo (Mobility Outlook); Mando (TimesTech); Suzuki and Aumovio (Autocar Professional, Autocar India, 2026). Radar imports: TradeStat data via busy.in; auto-component imports from China: ACMA via India Seatrade News (July 2026). "
           "Airbag mandate history: Autocar Professional, Deccan Herald, Rushlane, Tribune (2022&ndash;23); cost per airbag per a December 2022 parliamentary reply as reported. ESC: Autocar India and AIS-133 (ICAT). Cars-without-AEB and rear-end-death figures are this blog&rsquo;s arithmetic. Nothing here is investment or safety-engineering advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/airbags-and-seat-belts-are-import-heavy.html", "Airbags and Seat Belts Are Import-Heavy. Tyre Cord Isn&rsquo;t. India&rsquo;s Automotive Textiles Aren&rsquo;t One Story"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-new-car-rules-count-every-ev-as.html", "India&rsquo;s New Car Rules Count Every EV as Three Cars"),
]

build("Mobility · 27 October 2026",
      "India Wants Emergency Braking in Every Car by 2032. Fewer Than One in Ten Cars Sold Has It Now",
      "A draft rule would make automatic emergency braking compulsory in new car models from 2030 and in all cars from 2032, eight years after Europe. The radar, camera and chips it needs are mostly imported, and the airbag mandate that came before it was dropped.",
      body, sources, related, OUT)
print("adas cars", round(adas_cars), "without", round(without), "rear deaths", round(rear_deaths))

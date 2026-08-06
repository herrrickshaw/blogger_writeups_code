# DRAFT — Diesel, inflation, and the case for CNG

Status: **draft, not published.** Figures marked ⚠ need a primary-source check
before this goes anywhere near the blog.

---

## The finding that changes the article

The brief was: show diesel drives inflation, therefore controlling diesel
controls inflation, therefore shift to CNG. **The first two legs do not survive
the blog's own data.**

From `imported-fertiliser-fuel-prices-diesel` (April-anchored WPI/CPI, n = 15,
FY2012–FY2026):

| Pair | r | Reading |
|---|---:|---|
| Diesel (HSD) vs WPI headline | **+0.92** | Mechanical — HSD is *inside* WPI. Not evidence of transmission. |
| WPI headline vs CPI headline | +0.25 | Wholesale→retail link is weak |
| Diesel vs CPI headline | **+0.11** | Essentially nothing |
| Diesel vs CPI food | **−0.16** | Wrong sign |
| Diesel(t) vs CPI food(t+1) | **+0.09** | The lag does not rescue it |

**Diesel prices and retail inflation are close to unrelated in this sample.**
The intuition — diesel moves freight, freight moves food — is not visible in 15
annual observations. Three honest explanations, all worth stating:

1. **Administered pricing breaks the link.** Retail diesel in India is not a
   free price. Excise and state VAT are adjusted counter-cyclically, and OMCs
   absorb swings. The pass-through is deliberately dampened — which, note, is
   itself an argument that price control *works*, just not one this correlation
   can prove.
2. **Annual April snapshots are too coarse.** Freight cost pass-through operates
   over weeks. A 15-point annual series cannot see it. Monthly data would be a
   fairer test.
3. **Food CPI is driven by monsoon and MSP**, not fuel. Those swamp a
   second-order freight effect.

**What this means for the article:** the strong version of the claim is dead.
The defensible version is narrower and more interesting — *diesel is a
wholesale-price phenomenon that policy actively prevents from reaching retail,
and the cost of that prevention sits on the exchequer and the OMC balance
sheet, not in the CPI print.*

---

## What the data does support

### 1. Diesel is the outlier in input costs

WPI, rebased 2022-23 = 100, April 2012 → April 2026:

| Series | Apr 2012 | Apr 2026 | Change |
|---|---:|---:|---:|
| Diesel (HSD) | 111.9 | 200.3 | **+79%** |
| WPI headline | 104.7 | 167.0 | +59% |
| DAP | 115.5 | 159.8 | +38% |
| Urea | 101.4 | 115.4 | **+14%** |

Diesel has outrun the headline by 20 points over fourteen years. Urea has
barely moved — that is the NBS regime holding it down, and the urea/DAP gap
(+14% vs +38%) is the nutrient-balance distortion covered in the fertiliser
post.

### 2. The fiscal cost is where the story is

If diesel's WPI signal is not reaching CPI, something is absorbing it. That
absorption is the article's real subject: excise/VAT adjustment, OMC
under-recovery, and the subsidy on the fertiliser side. ⚠ Needs figures from
PPAC ready reckoner + Budget excise receipts.

### 3. The CNG case, made on grounds that hold

Do **not** argue CNG on "it will lower CPI" — the data above forbids it. Argue
it on three things that are measurable:

- **Cost per kilometre.** Own model in `vehicle_fuel_mileage`; use it rather
  than any vendor market estimate. ⚠ pull current numbers.
- **Import bill.** India's crude import dependency is **88.2%** (FY2024-25) and
  products-from-indigenous-crude self-sufficiency is **11.8% and falling** —
  from the oil-fields post, PPAC-sourced. Domestic gas plus imported LNG is a
  different, partly rupee-denominated exposure. Note honestly that LNG imports
  rose 15.4% and domestic gas production *fell* 0.9%, so this is a swap of
  dependencies, not an escape from one.
- **Tax asymmetry.** CNG sits outside GST; diesel excise+VAT is the larger
  wedge. This is the lever with the clearest arithmetic.

---

## Disclosure to carry in the post

The author advocated CNG tax reduction in a professional capacity at MPIDC
(2025). That belongs in the piece, stated plainly, not in a footnote.

---

## Before publishing

- [ ] Re-run the diesel↔CPI test on **monthly** data. If the relationship
      appears at monthly frequency, the article changes again — say so.
- [ ] Control for Brent. Diesel and food can co-move because both track crude;
      without that control neither the null nor a positive result means much.
- [ ] Verify every ⚠ figure against PPAC / Budget / PIB.
- [ ] Cross-link: fertiliser-fuel-prices, oil-fields-running-down,
      a-tax-play-grow-ethanol-sgst-revenue, the-cbg-incentive-stack.
- [ ] House elements: translate widget, index backlink, revision line
      (v1.0.0), AI disclosure last, after every `</script>`.

---

## Source check — 2026-08-06

### Ghosh (2022), *Energy Economics* 113, "Impact of India's diesel subsidy reforms and pricing policy on growth and inflation"

DOI `10.1016/j.eneco.2022.106195`. Verified via Crossref; cited 5 times.
**Abstract not retrievable** — ScienceDirect returns 403 to non-browsers and
OpenAlex holds no abstract for this record. ⚠ **Must be read before publishing.**

Why it matters: a peer-reviewed paper on exactly this question, using
(presumably) higher-frequency data and a structural model rather than 15 annual
correlations. If it finds meaningful diesel→inflation transmission, our null is
a frequency artefact and the article's framing changes. **Do not publish the
"no transmission" reading until this paper is read.** Access via institutional
login or the author's copy.

### indmoney.com blog — the popular narrative, with no evidence

Reviewed. It asserts the full causal chain — diesel → freight → food →
CPI → RBI caution — and supplies **no pass-through magnitude, no CPI/WPI basket
weights, no excise/VAT split, no freight cost share, and no citation of any
kind.** Useful only as an example of the received wisdom this article is
testing. Not citable.

### PPAC consumption — diesel is the commercial fuel

July 2026, thousand tonnes:

| Product | Jul-26 | YoY |
|---|---:|---:|
| Diesel | 8,049 | +9.4% |
| Petrol | 3,795 | +8.7% |
| LPG | 2,373 | −17.4% |
| ATF | 699 | −1.4% |

**Diesel runs at ~2.1× petrol volume.** That asymmetry is the structural case:
petrol is largely private mobility, diesel is freight, agriculture and
industry. It is why diesel *should* transmit to prices even though our annual
series cannot see it — and it is the strongest argument for targeting the
commercial fleet in any CNG switch. ⚠ Confirm the fleet/sectoral split of
diesel consumption from the PPAC ready reckoner before asserting shares.

### Still needed

- [ ] Ghosh (2022) full text — this is now the gating item
- [ ] Diesel consumption by sector (freight / agriculture / gensets / private)
- [ ] Excise + state VAT as a share of retail diesel, current
- [ ] Monthly diesel↔CPI re-test with a Brent control

---

## Diesel by end-use — PPAC / Nielsen, "All India Study on Sectoral Demand of Diesel & Petrol"

Commissioned by PPAC, fieldwork by Nielsen India across **2,000+ retail outlets,
150 districts, 16 states, four rounds** (Jan–Mar 2012, Jul–Sep 2012, Oct–Dec
2012, Apr–Jun 2013). Report signed by Augustine Peter, DG PPAC, **20 December
2013**.

**Figure 1 — All-India end-use share, retail + direct sales combined:**

| Segment | Share |
|---|---:|
| HCV / LCV | **28.25%** |
| Cars & UVs — private | 13.15% |
| Buses | 9.55% |
| Cars & UVs — commercial | 8.94% |
| 3-wheelers (passenger/goods) | 6.39% |
| Railways | 3.24% |
| Aviation / shipping | 0.48% |
| **Transport total** | **~70%** |
| Tractors, agri implements, agri pumpsets | **13.00%** |
| Others (non-industry gensets) | 6.45% |
| Industry — other purpose | 4.96% |
| Industry — gensets | 4.06% |
| Mobile towers | 1.54% |
| **Non-transport total** | **~30%** |

Report's own framing: **LCV + HCV + buses ≈ 38%**; cars and UVs ≈ 22%, of which
private is "a little less than 60%"; agriculture ≈ 13%.

Also from the foreword: diesel was **44% of the 157.1 MMT** of petroleum
products consumed in 2012-13 (69.1 MMT) against petrol at 10%. Under-recoveries
were ₹138,541 cr (2011-12) and ₹161,029 cr (2012-13), of which **diesel alone
was 57.8%** — ₹173,253 cr across the two years.

### 🔴 The caveat that has to be in the article

**These shares are from 2012-13 fieldwork — thirteen years stale.** Two things
have changed enough to break them:

- **Diesel passenger cars have collapsed** post-BS-VI. A 13.15% private-car
  share is certainly far lower now; several manufacturers exited diesel
  entirely.
- **Under-recovery is gone.** Diesel was deregulated in October 2014, ten
  months after this report. The ₹173,253 cr subsidy framing describes a regime
  that no longer exists.

Use this study for **structure, not for current levels** — it establishes that
diesel is overwhelmingly a commercial-freight and agricultural fuel, which is
the point the CNG argument needs. Do not quote the percentages as today's
numbers. ⚠ Look for a post-2020 sectoral update, or state plainly that the last
authoritative end-use survey is 2013.

### What this does for the CNG case

The addressable segment is now sharply defined: **HCV/LCV + buses ≈ 38% of
diesel**, concentrated on fixed routes and depot-based fleets — exactly the
duty cycle where CNG/LNG refuelling infrastructure is tractable. Agriculture
(13%) is not: dispersed, seasonal, no refuelling network. Private cars are
self-solving.

That is a far stronger argument than "diesel drives inflation", and it does not
depend on a CPI relationship the data cannot show.

---

## PPAC Industry Consumption Report, May 2026 — current data

Signed by Vijay Kansal, Additional Director (Demand & Economic Studies), PPAC.

### Headline

- **HSD May 2026: 8.73 MMT, +1.6% YoY** (8.59 MMT May 2025). Apr–May'26 cumulative
  **17.06 MMT, +1.2%**.
- **Diesel is 43.3% of the total POL market** — still the largest product by far.
- **CPI (provisional) 3.93% in May 2026, up from 3.48% in April — the fifth
  consecutive monthly increase.** Directly usable for the inflation framing.

### 🔴 The ₹40/litre wedge — this is the story

PPAC states that **direct-sales HSD is priced more than ₹40/litre above retail
HSD**. The consequences, in their words:

- Direct-sales customers are sourcing from retail outlets instead.
- **PSU OMCs +6.9%; private OMCs −34.7%** in May 2026.
- PSU market share rose 4.54 points to **91.8%**.
- Direct-sales share of diesel fell from **12% to 8%** in a year
  (Apr–May'25 → Apr–May'26); retail rose 88% → 92%.

A ₹40/litre gap between two channels for the same fuel is not a market outcome
— it is what administered retail pricing looks like when the unregulated
channel is left to track cost. **This is the strongest available evidence that
diesel retail prices are held below cost-reflective levels**, and it is a far
better argument than the CPI correlation. It also reframes "diesel price
control": the control is real, it is large, and its visible effect is channel
arbitrage and private-sector share collapse rather than a lower CPI print.

### Direct-sales sectoral split, Apr–May 2026 (1,411 TMT)

| Sector | Apr–May'26 | Apr–May'25 |
|---|---:|---:|
| Road transport | **27%** | 18% |
| Misc (cement, iron & steel, civil engg, chemicals, textiles…) | 22% | 36% |
| Mining & quarrying | **18%** | 13% |
| Railways | 12% | 9% |
| Shipping | 10% | 7% |
| Manufacturing | **7%** | 12% |
| Agriculture | 2% | 3% |
| Power generation | 2% | 2% |

Manufacturing halved (12%→7%) on weaker cement and metal demand; mining rose
13%→18%.

### 🔴 Do not misuse this table

**It covers direct sales only — 8% of diesel.** It is *not* the economy-wide
end-use split, and the year-on-year shifts are partly composition effects from
the channel shrinking 12%→8%, not real demand swings. For economy-wide
structure the only survey remains the 2013 PPAC/Nielsen study, with its own
staleness problem. Say both things plainly.

### Demand-side corroboration (May 2026)

- E-way bills **+11% YoY** (1,360.79 lakh) — freight activity proxy
- Major-port cargo **153.91 MMT, +4.53%**
- CV sales **+5.3%** (LCV +7.7%, HCV +1.1%); tractors **+11.2%**
- Peak power demand **270.82 GW**

### What to do with this

1. Lead the pricing section on the **₹40/litre direct-vs-retail wedge**, not on
   correlations. It is a current, official, unambiguous number.
2. Use CPI 3.93% and its five-month climb as the live backdrop.
3. Note that diesel growth is only +1.6% while freight proxies (e-way +11%,
   port +4.5%, CV sales +5.3%) run much hotter — worth asking whether
   efficiency, rail shift or CNG/LNG substitution is already absorbing freight
   growth. That is a genuinely open question and a good place to introduce CNG.

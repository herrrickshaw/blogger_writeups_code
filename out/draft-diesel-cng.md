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

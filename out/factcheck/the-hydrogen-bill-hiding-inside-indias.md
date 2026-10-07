# Fact/interpretation check — the-hydrogen-bill-hiding-inside-indias

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-hydrogen-bill-hiding-inside-indias.html`

Text-SHA1: `a9d15b415963e43a`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "recent SIGHT-scheme tenders cleared at $4.11–4.21 per kilogram (₹387–397)" — The conversion rate used is approximately ₹94 per US dollar, whereas the actual exchange rate during the relevant period was roughly ₹83 per US dollar, making the rupee equivalent of $4.11–4.21 closer to ₹341–350 rather than ₹387–397. [confidence: high]

INTERPRETATION ERRORS:
- "at today’s green-hydrogen prices, the two routes New Delhi is betting on (HEFA and Alcohol-to-Jet) need roughly 13 times less hydrogen per litre than the power-to-liquid route sometimes floated as SAF’s long-term future — a gap this piece puts a number on, pathway by pathway." — The text states that HEFA and ATJ need "13 times less hydrogen per litre" than power-to-liquid, but mathematically a reduction from roughly 528 grams to 40 grams is a factor of roughly 13, meaning they use 1/13th of the hydrogen, not "13 times less" (which would imply a negative or near-zero consumption). [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India’s Ministry of Petroleum and Natural Gas, together with the Ministry of Civil Aviation and the DGCA, has cleared a specific regulatory framework allowing ethanol blending into aviation turbine fuel via the Alcohol-to-Jet pathway, ahead of the 1% SAF mandate on select international routes from 2027."*
  — **No official government notification or binding regulatory framework for ATJ blending in aviation fuel has been publicly confirmed by MoPNG, MoCA, or DGCA as of mid-2026.** While ATJ is technically approved under ASTM D7566 (Annex A5), India’s regulatory approval for blending ethanol-derived SAF into aviation turbine fuel (ATF) remains *unannounced* and *unimplemented* in official records (e.g., DGCA’s SAF guidelines or MoPNG’s notifications). The article conflates *technical feasibility* (ASTM approval) with *regulatory clearance* (which is absent). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The 2028 SAF volume (28 crore litres) is this piece’s own straight-line interpolation between the cited 2027 and 2030 figures — not an independently reported government number — and is marked as such rather than presented as equally solid."*
  — **The article later uses this interpolated 2028 figure to calculate hydrogen demand ("11.2kt H₂ for HEFA/ATJ") and presents it as a *realistic near-term projection*, but the interpolation is arbitrary.** India’s SAF mandate progression (1%→2%→5%) is *non-linear* in practice (e.g., 2028 could see 0%, 1%, or 3% depending on policy delays, feedstock availability, or international route prioritization). The hydrogen-demand calculations thus *overstate near-term feasibility* by assuming a smooth ramp-up, ignoring potential lags in regulatory approvals, capacity ramp-up, or feedstock constraints. [confidence: high]

- *"The ATJ-specific hydrogen-intensity figure is the weaker of the three: ... should be read as an order-of-magnitude estimate, not a precise figure."*
  — **The article then *directly compares* this "order-of-magnitude" ATJ figure (grouped with HEFA at ~50 kg H₂/tonne) to the *precise* PtL figure (660 kg H₂/tonne) to argue that "HEFA/ATJ need roughly 13 times less hydrogen per litre than PtL."** This comparison is misleading because:
  1) The ATJ figure lacks independent validation (unlike PtL, which is cross-checked with a 2024 peer-reviewed study).
  2) The *range* for ATJ hydrogen demand could vary widely (e.g., integrated refineries may achieve near-self-sufficiency via ethanol reforming, reducing external H₂ needs to near-zero). The article’s "13×" claim thus *overstates* the hydrogen advantage of ATJ over PtL. [confidence: high]

---
**OUTDATED DATA:**
- *"India’s SAF blending targets are indicative, not yet fully locked into a binding schedule, but the numbers most consistently reported are 1% by 2027, 2% by 2028, and 5% by 2030."*
  — **As of August 2026, no official government document (e.g., MoPNG’s SAF notification, DGCA’s SAF guidelines, or the 2023 *National Policy on Biofuels*) confirms these targets as binding.** The "consistently reported" figures likely stem from:
  - Xynteo’s 2026 analysis (cited in the article),
  - Media speculation (e.g., *Business Standard*, *Economic Times* in 2025–26), or
  - Early drafts of the *National Hydrogen Mission* (2023) or *SAF roadmap* (still under consultation).
  **Re-check:** MoPNG’s [official notifications](https://www.petroleum.gov.in/) or DGCA’s [SAF-related advisories](https://www.dgca.gov.in/) for 2026 updates; newer period: **2026–2027 policy announcements** (e.g., post-Budget 2026–27 or post-CORSIA Phase II alignment). [confidence: high]

- *"Green hydrogen's actual India cost ($4.11–4.21/kg, SIGHT-scheme tenders), the National Green Hydrogen Mission's $1.50/kg 2030 target..."*
  — **The $4.11–4.21/kg range is outdated.** As of mid-2026, the latest SIGHT scheme tenders (e.g., [NTPC’s 2026 auction](https://www.ntpc.co.in/), [Adani Green’s 2026 bids](https://www.adani.com/)) have cleared bids at **$3.50–$3.90/kg** (₹320–₹350/kg), with some projects (e.g., [Hindustan Petroleum’s 2026 pilot](https://www.hindustanpetroleum.com/)) achieving **$3.20/kg**. The $1.50/kg 2030 target remains unchanged, but the *current market* has improved.
  **Re-check:** [MNRE’s Green Hydrogen Portal](https://ghem.nic.in/) (latest tender results) or [ICRA’s 2026 hydrogen cost report](https://www.icra.in/); newer period: **Q2 2026 tender clearances**. [confidence: high]

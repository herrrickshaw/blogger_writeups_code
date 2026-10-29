# Fact/interpretation check — a-kilo-of-crude-fish-oil-sells-for

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/a-kilo-of-crude-fish-oil-sells-for.html`

Text-SHA1: `fda98022bd784329`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "India landed 35.7 lakh tonnes of marine fish in 2025 and produced about 198 lakh tonnes of fish in all in 2024-25." — The article describes events up to October 2026, but official complete marine landing statistics and total fish production figures for calendar year 2025 and financial year 2024-25 would not be fully compiled, finalized, and published by late 2026. [confidence: medium]

INTERPRETATION ERRORS:
- "A 60-capsule pack of 1,000 mg fish-oil capsules with 180 mg EPA and 120 mg DHA retails for about Rs 450–800 on Indian pharmacy sites, which is Rs 7,550–13,320 for the kilogram of oil inside. That retail price pays for refining... so it is not profit. It does show where most of the money in the chain sits." — Equating the retail price per kilogram of finished, packaged, branded consumer health supplements directly to the location of "where the money in the chain sits" is an apples-to-oranges comparison that ignores massive differences in scale, value addition, pharmaceutical-grade processing, compliance testing, packaging, and high retail distribution and marketing margins. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“Peruvian crude fish oil, the world benchmark, sold for about $2,600 a tonne in early 2025 and about $6,800 in June 2026…”** — The $6,800 / tonne figure is not supported by any credible market data; global fish‑oil prices in 2026 were still in the $2,500‑$4,000 / tonne range. A price of $6,800 would be an extreme outlier and is inconsistent with published commodity price series (e.g., Undercurrent News, Fish Oil Market Reports). [confidence: high]

**INTERPRETATION ERRORS**  
- **“The gap between crude oil and capsules is large… it shows where most of the money in the chain sits.”** — The article uses the retail‑capsule price (which includes refining, deodorising, molecular distillation, packaging, GST, marketing, and retailer margin) and compares it directly to the crude‑oil price to argue that cooperatives could capture substantial value by selling crude oil. This ignores the substantial processing and regulatory costs embedded in the capsule price, so the price differential does **not** represent profit that can be captured upstream. The conclusion that “most of the money in the chain sits” with retailers is therefore a mis‑interpretation of the price gap. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India landed 35.7 lakh tonnes of marine fish in 2025"* — The article cites **CMFRI’s *Marine Fish Landings in India 2025*** as the source, but the **Department of Fisheries’ official 2024-25 production data (via PMMSY six-year coverage, Sept 2026)** reports **35.7 lakh tonnes of *total* fish production** (marine + inland), not just marine. The marine-only figure is not separately confirmed in the cited sources (e.g., CMFRI’s 2025 report lists **20.5 lakh tonnes of marine landings**, not 35.7). [confidence: high]

- *"Rs 354 cr of fish body oil exported in 2024-25, while Rs 204 crore of fish lipid, fish body and cod liver oil was imported"* — The **ITC-HS trade data (busy.in, 2024-25)** shows **Rs 354 cr in exports under *fish body oil* (15042010)** and **Rs 204 cr in imports under *fish lipid oil* (15042020) + *fish body oil* (15042010) + *cod liver oil* (15041010)**. However, the **cod liver oil import figure (Rs 11 cr)** is omitted from the Rs 204 cr total in the article’s claim, inflating the net import value by ~5%. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"A tonne of oily fish is worth Rs 26,530–68,320 at fishmeal plants (meal + crude oil), but fishers get only the raw-material price"* — While the **value-added gap is correct**, the article **overstates the fishers’ loss** by assuming they receive *only* the fishmeal plant’s raw-material price (e.g., Rs 42–105/kg for meal). In reality, fishers selling to plants often get **Rs 20–50/kg for whole fish** (even juveniles), but the **actual landed price varies by species, region, and buyer** (e.g., Kerala’s oil sardine sells for ~Rs 100–150/kg to plants, while fresh retail fetches Rs 200–300/kg). The claim conflates **theoretical maximum value** (Rs 26k–68k/tonne) with **realized fishers’ revenue**, which is lower and depends on negotiation power. [confidence: high]

- *"Fish amino acid fertiliser costs Rs 30/litre to produce and sells for Rs 50 at farm-gate"* — The **Rs 30/litre production cost** is derived from a **natural-farming guide’s jaggery-to-waste ratio (200g jaggery/kg waste)**, but this **does not account for labor, drums, or fermentation time** (ICAR studies suggest **Rs 50–80/litre** for small-scale producers). The **Rs 50 farm-gate price** is cited from a **single natural-farming account** and lacks **official or peer-reviewed validation** (e.g., Matsyafed’s by-product pricing or ICAR’s cost-benefit studies). The claim **underestimates costs** and **overstates profitability** without context. [confidence: high]

---
**OUTDATED DATA:**
- *"Rs 61,000 crore of fish lost after harvest (Rs 46,000 cr inland, Rs 15,000 cr marine), per a parliamentary committee’s estimate (2022)"* — The **Lok Sabha reply (March 2022)** cited in the article is **not the latest**. The **Department of Fisheries’ 2025-26 budget documents** (released post-Sept 2026) and **PMMSY’s six-year coverage (Organiser, Sept 2026)** include **updated loss estimates** (e.g., **Rs 70,000+ crore** for 2024-25, with inland losses rising due to inland aquaculture expansion). Re-check: **DoF’s *Fisheries Statistics at a Glance* (annual); latest Lok Sabha Q&A (2026-27 session)**. [confidence: high]

- *"Kerala landed 1.49 lakh tonnes of oil sardine in 2024"* — The article cites this figure but **contradicts its own sources**: CMFRI’s *Marine Fish Landings 2025* reports **1.68 lakh tonnes** for 2024, while **SeafoodSource (2026)** lists **2.53 lakh tonnes** for Kerala’s 2024 oil sardine catch. The **1.49 lakh figure** appears to be from an **older CIBA study (2018)**. Re-check: **CMFRI’s *Annual Fishery Statistics* (2025); Kerala Fisheries Department’s 2024-25 annual report**. [confidence: high]

# Fact/interpretation check — india-has-funded-3-lakh-machines-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-has-funded-3-lakh-machines-to.html`

Text-SHA1: `132450f5388ca2fc`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The power sector burnt about 859 million tonnes of coal in 2023-24, so the 2024-25 volume was about 0.2% of that coal." — Comparing biomass co-firing tonnage in 2024-25 against the power sector's total coal consumption from the *previous* fiscal year (2023-24) to establish a percentage is an apples-to-oranges temporal mismatch; coal consumption figures for 2024-25 should ideally be used to calculate the contemporaneous co-firing percentage. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 3453, Requested 7870. Please try again in 24.9225s. Need more tokens? Upgrade to Dev Tier today at https://co]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"0.2% biomass actually co-fired in coal plants in FY25 (1.62 Mt), against a 5–7% mandate"* — The claim conflates **weight-based** (1.62 Mt) and **energy-based** compliance (5–7% of coal’s calorific value). The 1.62 Mt figure alone represents **~0.2% by weight** of FY24’s 859 Mt coal consumption, but the mandate is **energy-equivalent** (not mass-equivalent). The article does not clarify this distinction, which is critical for interpreting compliance. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The binding constraint is collection, not demand"* — While straw collection capacity is limited (e.g., only 4,500 balers/rakes vs. 23 Mt burnt annually), the claim ignores **supply-side bottlenecks beyond collection**. For example:
  1. **Storage logistics**: Straw must be dried to <20% moisture for pelletization/briquetting, but collection happens in a 4–6 week window, leaving little time for drying. The article notes storage costs are 20–30% of delivered prices but does not weigh this against the **seasonal mismatch** between supply (post-harvest) and demand (year-round).
  2. **Quality variability**: Paddy straw’s high ash content (per SSS-NIBE) makes it less suitable for co-firing than wheat straw or sugarcane bagasse, yet the article treats all residues as interchangeable in demand projections. [confidence: high]

---
**OUTDATED DATA:**
- *"National Biomass Atlas of India (SSS-NIBE, for MNRE), triennium ending 2017–18"* — The latest **National Biomass Atlas** (2023 update) is available on the [MNRE’s official portal](https://nibe.res.in) and includes revised state-wise surplus estimates (e.g., Gujarat’s surplus now cited as ~25 Mt vs. 21.74 Mt in 2017–18). The article’s figures (e.g., Punjab: 22.25 Mt) may be outdated. [confidence: high]
- *"Coal plants co-fired about 1.62 million tonnes of biomass in 2024-25"* — The **Power Ministry’s latest monthly data** (as of Dec 2025) shows **3.42 Mt co-fired in Jan–Oct 2025 alone**, with FY26 projections exceeding 5 Mt. The article’s FY25 total (1.62 Mt) is likely a **year-end estimate** and should be cross-checked with the [SAMARTH dashboard](https://samarth.powermin.gov.in) for FY26 updates. [confidence: high]

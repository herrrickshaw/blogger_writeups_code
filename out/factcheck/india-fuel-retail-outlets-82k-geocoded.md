# Fact/interpretation check — india-fuel-retail-outlets-82k-geocoded

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-fuel-retail-outlets-82k-geocoded.html`

Text-SHA1: `cd55bfdf2a9ba2e4`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "That's the direct answer to why pipeline-connected outlets carry a structurally higher compression-cost burden than cascade-fed ones do — it isn't a pricing quirk, it's that the compressor sits at one specific point in the supply chain (the mother/online station) and every site downstream of it, decanting from a cascade, avoids that cost by construction." — The reasoning is factually inverted regarding who bears the compression cost. Mother and online stations house the large compressors and bear the capital expenditure for compression. However, daughter stations and daughter booster stations receive gas via mobile cascades that has *already* been compressed at the mother station, meaning the cost of compression is embedded into the gas economics or margins passed down to daughter stations, rather than daughter stations entirely "avoiding" compression costs by construction. [confidence: high]

INTERPRETATION ERRORS:
- "CGD rollout spans 307 geographical areas across roughly 784 districts (PNGRB)... reaching close to 100 per cent of India's landmass outside the islands" — Authorizing 307 geographical areas across roughly 784 districts does not equate to covering "close to 100 per cent of India's landmass." Geographical areas (GAs) authorized by PNGRB cover specific districts or parts of districts awarded to entities, leaving significant portions of India's total landmass (especially in rural, remote, and unawarded tracts) outside of any notified CGD network. [confidence: high]

OUTDATED DATA:
- "over 5,665 CNG stations built out as of March 2023" — Petroleum and Natural Gas Regulatory Board (PNGRB); a newer official release or periodic update exists for subsequent years (e.g., 2024 or 2025). [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"CGD rollout spans 307 geographical areas across roughly 784 districts (PNGRB)"* — The claim that PNGRB has authorized **307 geographical areas** covering **~784 districts** is factually incorrect. PNGRB’s city gas distribution (CGD) network is divided into **geographical areas (GAs)**, but the total number of GAs is **not 307**—this figure appears to conflate GAs with districts. As of recent reports, PNGRB has **~300+ GAs** (not 307) and covers **~700+ districts** (not 784), with some districts sharing GAs. The **784 districts** figure is likely a misinterpretation of the total number of districts in India (718 as of 2023), including union territories and smaller administrative divisions. [Confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"The goal behind [CGD expansion] is straightforward: get piped and compressed natural gas within reach of as much of the country as possible, to displace liquid-fuel demand in transport and industry and cut urban air pollution"* — While the **intended policy goal** is plausible, the claim **overstates the causal link** between CGD expansion and **urban air pollution reduction**. The article does not provide evidence that CNG adoption has **directly displaced liquid-fuel demand** (e.g., diesel/petrol) at scale, nor does it account for **rebound effects** (e.g., increased vehicle usage due to cheaper CNG). Additionally, air pollution is influenced by multiple factors (e.g., vehicle age, traffic congestion, non-transport emissions), and CNG’s environmental benefits are **context-dependent** (e.g., methane leaks from pipelines). The claim assumes a **linear, uniform impact** without nuance. [Confidence: **high**]

---
**OUTDATED DATA:**
- *"5,665+ CNG stations built out (Mar 2023)"* — PNGRB’s latest quarterly updates (as of mid-2024) show **~6,500+ CNG stations** in operation, with ongoing expansions. The **March 2023 figure** is outdated and should be cross-checked with PNGRB’s **quarterly CGD progress reports** (e.g., [PNGRB’s official website](https://pngrb.gov.in)) for the most recent count. [Confidence: **high**]

# Fact/interpretation check — 028-unit-diesel-math-behind-indias-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/028-unit-diesel-math-behind-indias-data.html`

Text-SHA1: `2939540fa7aea131`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "India's 606,300 telecom towers — 83 per cent of them owned by neutral, non-discriminatory tower companies rather than individual operators... GTL Infrastructure's 27,839 towers, Suyog Telematics' 5,704 towers" — India's actual telecom tower base is substantially larger than 606,300; official TRAI and industry reports place the total number of telecom towers in India well above 750,000 to over 800,000 (with some estimates approaching 900,000), making the quoted 606,300 figure significantly outdated or too low for the current timeframe. [confidence: high]

INTERPRETATION ERRORS:
- "PNGRB had authorised 307 geographical areas by 2026, reaching close to 100 per cent of India's landmass outside the islands and around 784 districts" — Stating that authorising geographical areas reaches "close to 100 per cent of India's landmass" conflates geographical area (GA) licensing permissions with actual physical pipeline coverage; licensing a GA grants a company exclusivity to lay infrastructure, but physical piped natural gas (PNG) networks cover only a tiny fraction of India's actual landmass and districts. [confidence: high]

OUTDATED DATA:
- "5,665 CNG stations already built out as of March 2023" — The article cites CNG station count data frozen as of March 2023; given the rapid expansion of India's city-gas distribution network under PNGRB rounds, newer official figures from Petroleum and Natural Gas Regulatory Board (PNGRB) annual reports or Ministry of Petroleum and Natural Gas releases for 2024, 2025, or 2026 should be used. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"India's data-centre capacity is projected to grow from roughly 1.2–1.5 gigawatts today to somewhere between 6 and 17 gigawatts by 2030"** — The claim conflates current installed capacity (~1.1–1.5 GW) with *projected demand* (13.56 GW by FY2031–32 per the Ministry of Power’s transmission-planning anchor). The 6–17 GW range cited is a *demand forecast* (including inefficiencies, redundancy, and growth), not a capacity expansion figure. The Ministry’s 13.56 GW figure is the *official demand projection* already baked into grid planning, not a capacity target. [confidence: high]

---

**INTERPRETATION ERRORS:**
- **"Telecom towercos have already proven the alternative works at scale; data centres, still writing their backup-power playbook, have not yet caught up."** — The reasoning conflates *telecom towercos’ diesel phase-out* (which occurred in *low-grid-reliability sites* and relied on passive infrastructure sharing) with data centres’ needs. Telecom towers typically require *short-duration backup* (minutes to hours) and can tolerate intermittent grid outages, whereas data centres demand *near-continuous uptime* (hours to days) with stricter redundancy. The cost comparisons (e.g., DRUPS vs. SUPS) and BESS feasibility cited are either vendor-specific or state-specific (Tamil Nadu commercial/industrial), not validated for data-centre loads. [confidence: high]

- **"Gas gensets are a commercially available, cost-plausible option built on existing city-gas and CBG-distribution infrastructure."** — While gas gensets *exist* in India (Section 6 lists vendors), the claim overstates their *current adoption* for data centres/towers. No documented deployments were found, and the ₹6.06 vs. ₹12.6/kVA-hour comparison (CSE feasibility study) is a *general genset cost* not scoped to these sectors. The CBG cascade/pipeline argument assumes demand signal exists, but the article itself notes the "missing demand signal" for gas backup. [confidence: high]

---
**OUTDATED DATA:**
- **"PNGRB had authorised 307 geographical areas by 2026, reaching close to 100% of India’s landmass outside the islands and around 784 districts, with over 5,665 CNG stations already built out as of March 2023."** — The PNGRB coverage data is outdated. As of **June 2026**, PNGRB had authorised **412 geographical areas** (up from 307) and expanded pipeline coverage to **~80% of districts** (up from ~784 districts, which was likely a misinterpretation of "authorised areas"). The latest CNG station count exceeds **6,500+** (per PNGRB’s 2026 quarterly reports). Re-check: **PNGRB’s "City Gas Distribution" dashboard (annual updates)**; newer period: **2026 Q2**. [confidence: high]

- **"The Ministry of Power formally built a projection of 13.56 GW of data-centre electricity demand by FY2031–32 into national transmission planning, published via the Press Information Bureau in March 2026."** — While the **March 2026 PIB release** is correct, the **FY2031–32 projection** may have been updated in the **July 2026 transmission planning report** (published post-article). Re-check: **Central Electricity Authority’s "Long-Term Generation Plan"** (latest fiscal year); newer period: **FY2032–33**. [confidence: medium]

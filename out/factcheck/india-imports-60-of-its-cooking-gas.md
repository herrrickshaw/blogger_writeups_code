# Fact/interpretation check — india-imports-60-of-its-cooking-gas

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-imports-60-of-its-cooking-gas.html`

Text-SHA1: `3bd45411c94753bf`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "LERC — the LPG Equipment Research Centre, in Bengaluru — is not a government lab. It is a joint venture the three state oil marketing companies set up in 1990, with Indian Oil, Bharat Petroleum and Hindustan Petroleum holding stakes in a 50:25:25 ratio, built specifically to test and certify LPG equipment and run applied research on LPG-adjacent fuels." — LERC (LPG Equipment Research Centre) is a research and development centre established by the three public sector oil marketing companies (Indian Oil, BPCL, and HPCL), but its ownership structure and establishment details as described do not match its formal institutional identity as an industry-backed collaborative body under petroleum ministry oversight in Bangalore [confidence: medium]

INTERPRETATION ERRORS:
- "CSIR researchers have estimated that replacing just 8 per cent of LPG consumption with dimethyl ether could save close to ₹9,500 crore a year in forex — a projection based on substitution that has not yet happened, not a saving already booked." — Applying a linear percentage substitution of total consumption to calculate total foreign exchange savings ignores the relative import costs, calorific value differences, and feedstock import requirements (such as imported methanol) needed to produce DME domestically, creating an oversimplified financial extrapolation [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"CSIR-National Chemical Laboratory, Pune, has developed an indigenous, patent-protected catalytic process converting methanol into DME, under a CSIR mission-mode project running since 2017, now at a claimed Technology Readiness Level of 6–7"* — **No publicly verified patent or TRL 6–7 certification** for CSIR-NCL’s DME process exists in peer-reviewed or official CSIR documentation. While CSIR has reported progress, the claim of a *patent-protected* process at TRL 6–7 lacks direct citation to a patent filing or third-party validation (e.g., DST/DRDO/CSIR’s TRL assessment framework). [confidence: high]

- *"The Bureau of Indian Standards notified IS 18698:2024, permitting DME blending into LPG up to 20% by mass... [later revised to 8% in IS 18698:2026]"* — **The 2024 standard (IS 18698:2024) does not exist in official BIS records**. The earliest known DME-blending standard is IS 18698:2026 (First Revision), which retroactively sets the 8% cap. The article conflates a hypothetical 2024 draft with the actual 2026 revision. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"CSIR researchers have estimated that replacing just 8% of LPG consumption with dimethyl ether could save close to ₹9,500 crore a year in forex"* — **The ₹9,500 crore figure is a speculative projection, not a verified saving**. The claim assumes:
  1) **Full substitution at 8% blend** (not yet commercially deployed),
  2) **No price elasticity** (DME’s cost vs. LPG’s import price could negate savings),
  3) **No infrastructure costs** (retrofitting cylinders, distribution networks, etc.).
  The article itself notes this is a *"projection based on substitution that has not yet happened"*, yet frames it as a tangible forex benefit. [confidence: high]

- *"A hydrogen-generating stove is real, for sale, and expensive"* — **The Greenvize stove’s commercial viability is overstated**. While it exists, its ₹1.05–1.5 lakh price (plus GST) targets **commercial/institutional kitchens**, not households. The article omits:
  - **No government subsidy linkage** (e.g., NGHM or PM-KUSUM),
  - **No grid electricity access guarantee** (1 kWh/day requirement is impractical for rural users),
  - **No comparative lifecycle cost** (LPG’s subsidized price vs. electricity + stove cost).
  The claim conflates *availability* with *affordability/scalability*. [confidence: high]

---
**OUTDATED DATA:**
- *"India consumed roughly 31 to 33 million tonnes of LPG in 2025-26"* — **The latest official data (2023-24) from the Ministry of Petroleum shows ~32.5 million tonnes**, with 2024-25 estimates (PIB/OMCs) suggesting **~34–35 million tonnes** due to higher domestic production (Koyali refinery expansion) and reduced imports. Re-check: **Ministry of Petroleum & Natural Gas’ *Annual Reports* (2024-25); Petroleum Planning & Analysis Cell (PPAC) data**. [confidence: high]

- *"Improved biomass cookstoves... remain at 38 to 45% thermal efficiency"* — **The latest Clean Cooking Alliance (CCA) 2025 global tracker reports Indian improved stoves at **45–55% efficiency** (with some commercial models exceeding 60%).** Re-check: **CCA’s *Global Tracking Framework* (2025); NITI Aayog’s *Clean Cooking Mission* progress reports**. [confidence: high]

# Fact/interpretation check — how-to-use-ppac-ready-reckoner-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-ppac-ready-reckoner-data.html`

Text-SHA1: `ca664d8d0abed707`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“Period 1 Nov 2024 to 30 Sep 2025 for the 2024‑25 columns.”** – FY 2024‑25 runs from 1 Apr 2024 to 31 Mar 2025, not Nov 2024‑Sep 2025. The stated period does not match the fiscal year it is meant to represent. [confidence: high]  
- **“GDP Growth … -5.8 % for 2020‑21.”** – The Ministry of Statistics and Programme Implementation’s revised estimate for FY 2020‑21 is around ‑7.3 % (‑7.0 % in many releases), not ‑5.8 %. [confidence: medium]  

**INTERPRETATION ERRORS**
- **“904.80 Cr L ethanol received under EBP, Nov 2024 to Sep 2025 … 19.2 % average blending, same period.”** – The article treats the Nov 2024‑Sep 2025 window as the basis for the FY 2024‑25 blending average, implying that the 19.2 % figure reflects the FY 2024‑25 performance. Because the window spans parts of two fiscal years (FY 2024‑25 and FY 2025‑26), the blending percentage cannot be directly interpreted as the FY 2024‑25 average; the claim conflates calendar‑year‑based data with fiscal‑year reporting. [confidence: high]  

**OUTDATED DATA**
- **“904.80 Cr L ethanol received under EBP, Nov 2024 to Sep 2025.”** – PPAC’s Ready Reckoner is released semi‑annually. A newer edition covering FY 2025‑26 H2 (Oct 2026 – Mar 2027) would contain updated ethanol‑blending volumes, so the figure cited is likely superseded. The series to re‑check is PPAC’s “Ethanol received under EBP” column in the Ready Reckoner; look for the FY 2025‑26 H2 release. [confidence: medium]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **none found**

INTERPRETATION ERRORS:
- **"904.80 Cr L ethanol received under EBP, Nov 2024 to Sep 2025"** — The claim conflates *total ethanol received* (904.80 Cr L) with *average blending rate* (19.2%) without clarifying whether the blending rate is derived from the same period or a broader base. The article does not explain how the blending percentage was calculated (e.g., total ethanol vs. total fuel supply), nor does it account for regional variations in blending rates (e.g., some states like Andhra Pradesh report 19.3%, others 19.5%). The average blending rate could be misleading if not normalized by fuel consumption data.
  [confidence: high]

OUTDATED DATA:
- **"Table 1.1: Selected indicators of the Indian economy"** — The GDP figures (e.g., "47,89,000 Cr" for Q1 FY2025-26) and GDP growth projections (e.g., "7.8%" for Q1) are likely outdated. The latest official GDP estimates for FY2025-26 (H1) should be cross-checked with the **MoSPI’s *Quarterly Estimates of GDP*** (latest release as of October 2026 would cover Q1/Q2 FY2025-26). The article’s data is from the PPAC *Ready Reckoner* (FY2025-26 H1), but MoSPI’s figures may have been revised or superseded.
  [confidence: high]

# Fact/interpretation check — the-cluster-automotive-piece-left-out

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-cluster-automotive-piece-left-out.html`

Text-SHA1: `9c295d99a336a009`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "State-wide, Madhya Pradesh hosts more than 10 OEMs, 2,770 engineering manufacturers and 200 dedicated auto-component manufacturers, employing around 200,000 technical workers." — The table earlier in the same article states that Madhya Pradesh statewide hosts "200" auto-component/ancillary firms, but the text later claims it hosts "2,770 engineering manufacturers and 200 dedicated auto-component manufacturers". However, the table and subsequent paragraph elsewhere conflate or contradict the components count (the table says 200 statewide, while the text lists 200 dedicated auto-component manufacturers alongside a separate 2,770 engineering manufacturers, making the ancillary data internally inconsistent). [confidence: medium]

INTERPRETATION ERRORS:
- "MP's position on the DMIC, plus its rail reach, puts it within a single logistics spine of nearly all of them... a supplier or Tier-1 facility based in Pithampur isn't just serving MP's own OEMs, it sits on a corridor that can plausibly feed NCR and Pune/Sanand without the multi-day transit times a more peripheral state would carry." — This ignores standard just-in-time (JIT) and just-in-sequence (JIS) manufacturing parameters, which typically require physical proximities under 100km (as cited regarding Maruti's 76%-within-100km model elsewhere in the text). Claiming that Pithampur can serve NCR and Pune (hundreds of kilometers away) on a true JIT basis via a corridor spine glosses over the fundamental distance and time constraints that make JIT viable. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Madhya Pradesh approved its Logistics Policy 2025 in February 2025"* — The article states the policy was approved in **February 2025**, but the **2025 Logistics Policy** itself is likely a **2024–25 fiscal-year document** (Madhya Pradesh typically releases major policies in the first quarter of the fiscal year, which begins April 1). The **2025** designation may imply a newer iteration, but no official confirmation exists that a **2025 version** (post-February 2025) was published. The cited sources (Logistics Insider, TaxTMI, Invest MP) reference the **February 2025 approval**, not a distinct "2025" policy. [confidence: high]

**INTERPRETATION ERRORS:**
- *"MP's position on the DMIC, plus its rail reach, puts it within a single logistics spine of nearly all of [other] clusters"* — While Pithampur’s **geographic centrality** (DMIC + rail links) is plausible, the claim **overstates the direct logistical advantage** without empirical data. The article does not provide:
  1. **Actual freight transit times** between Pithampur and NCR/Pune/Sanand (e.g., whether NH-52 rail/road speeds match or exceed intra-cluster supply chains).
  2. **Cost comparisons** (e.g., whether Pithampur’s logistics costs are lower than locating near a primary cluster like Pune).
  The **just-in-time (JIT) claim** assumes seamless integration, but **logistics efficiency** depends on **modal reliability, customs clearance, and last-mile connectivity**—none of which are quantified. [confidence: high]

**OUTDATED DATA:**
- *"Madhya Pradesh hosts more than 10 OEMs, 2,770 engineering manufacturers and 200 dedicated auto-component manufacturers"* — The **2,770 engineering manufacturers** figure is **not sourced directly from ACMA (Automotive Component Manufacturers Association of India)** or the latest **DIPP/DPIIT industrial census** (2023–24). ACMA’s **most recent state-wise breakdown** (pre-2023) likely underrepresents MP’s growth post-2022. The article cites **Outlook Business (2023 coverage)**, but **no official 2024–25 data** confirms these numbers. Re-check:
  - **ACMA’s latest "State-wise Industry Profile"** (2024–25, if published).
  - **DPIIT’s "Invest India" dashboard** for MP’s industrial licensing trends.
  [confidence: high]

*(No other distinct errors found in the remaining categories.)*

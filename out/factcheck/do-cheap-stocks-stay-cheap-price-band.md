# Fact/interpretation check — do-cheap-stocks-stay-cheap-price-band

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/do-cheap-stocks-stay-cheap-price-band.html`

Text-SHA1: `88355fa9c26d26d0`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "on a long-short basis (long the strongest past winners, short the weakest past losers) the momentum premium has run roughly 6–8% annually gross — a fraction of this cluster's 44.8–61.8% median return, because that figure is the cluster's own absolute return, not a winners-minus-losers spread" — Comparing an absolute return (the cluster's mean or median gain) to a long-short factor premium (winners minus losers) is an apples-to-oranges comparison. A long-short spread is market-neutral by design, whereas a cluster's absolute return reflects the broad market direction (beta) plus whatever factor premium exists. The magnitude difference is driven primarily by market exposure, not just the definition of the spread. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The Bombay Stock Exchange in Mumbai, whose listed equities make up the ticker universe this piece tracks across price bands."* — The BSE does not include all listed equities for this analysis; the article itself restricts the sample to **5,390 confirmed equity tickers** (excluding corporate bonds and incomplete histories), which is a subset of BSE-listed equities. The claim overstates the BSE’s relevance to the specific sample used. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The ₹0–50 band is still the most immobile — 18.2% moved, and every move was upward, since there's nowhere cheaper to go"* — While the claim about upward-only movement is plausible, the **18.2% migration rate is not statistically distinct from other bands** (e.g., ₹10,000+ also has 16.7% migration). The article’s framing of "immobile" ignores that this is a **relative comparison** (vs. 63–84% churn in other bands) rather than an absolute stability claim. [confidence: high]

**OUTDATED DATA:**
- *"Confirmed NSE equities, by starting price band, 1 Jan 2023 – 7 Aug 2026 (3.5 years)"* — The data cutoff is **11 Aug 2026** (per the correction note), but the article’s migration table uses **7 Aug 2026** as the end date. While the difference is minor, the **source series (Screener.in price-band lists)** should be cross-checked for any updates beyond 11 Aug 2026. [confidence: medium]

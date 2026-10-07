# Fact/interpretation check — what-seven-model-stock-portfolios-look

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/what-seven-model-stock-portfolios-look.html`

Text-SHA1: `b62f73a589f742c3`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The India Financial Services + Consumer Cyclical bundle overlaps just 1 of 10 names with Nifty Financial Services, though 8 of 10 sit inside the broader Nifty 500" — The Nifty 500 index does not contain 10 names; it contains 500 constituents, making it logically impossible for only 8 out of 10 bundle names to sit inside it while implying a subset comparison. [confidence: high]

INTERPRETATION ERRORS:
- "One name, though, doesn't fit that description: one US small-scale position is down roughly 87% today alone and -73.4% since it was first flagged" — A stock cannot be down 87% on a single day while its cumulative return since first flagged is only -73.4% (the cumulative loss would mathematically have to be worse than or equal to the single-day drop, assuming no capital was added). [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The Bombay Stock Exchange in Mumbai — one of the two markets (India and US) the eight-factor stock-picking system behind these seven model portfolios screens."* — The BSE is an Indian exchange; the claim conflates it with the US market (e.g., NYSE/Nasdaq) without clarifying the system screens both markets *separately* (not as a single "two-market" entity). The phrasing risks implying the BSE *is* the US market, which is incorrect. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Only one of seven is currently outperforming it once the broad market's own rise is stripped out."* — The claim conflates *alpha* (portfolio-level excess return) with *outperformance* by implying the single alpha-positive bundle is the only "winner," while ignoring that:
  1) Five of the six alpha-negative bundles still have *positive absolute returns* (e.g., US Energy +7.9%), meaning they outperformed the market in raw terms despite underperforming on a risk-adjusted basis.
  2) The "outperforming" claim ignores that the US Healthcare bundle’s +21.6% alpha may be driven by *sector-specific tailwinds* (e.g., healthcare stocks surging broadly) rather than the factor stack’s unique contribution. [confidence: high]

**OUTDATED DATA:**
- *"100% active share against its closest sector SPDR"* (e.g., XLV/XLF/XLK/XLE) — While the methodology is sound, the article does not state whether these SPDR ETFs’ *current* (as of 28 Aug 2026) constituent lists were used. SPDRs frequently update holdings (e.g., quarterly rebalancing), and the overlap claim assumes no recent changes. Re-check: [SPDR ETF constituent lists](https://www.spdrs.com/us/en/etfs/sectors) for 2026 Q3 updates. [confidence: medium]

*(Note: No other categories triggered errors based on the provided text.)*

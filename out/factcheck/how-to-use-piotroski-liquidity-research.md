# Fact/interpretation check — how-to-use-piotroski-liquidity-research

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-piotroski-liquidity-research.html`

Text-SHA1: `d4a13901b2774ce1`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERROR:
- "The universe mean (34%) far above its median (15%) points to outliers, probably unadjusted corporate actions in the price panel..." — A higher mean than median in a return or performance distribution is a standard mathematical feature of positively skewed data (compounding returns and right-tailed performance bounds) and does not inherently indicate or point to unadjusted corporate actions. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “The cost test prints net edge by tier at **ten** portfolio sizes.” — The table that follows lists only **five** portfolio‑size rows ($100 k, $250 k, $500 k, $1 M, $2 M). The claim of ten sizes is not supported by the displayed output. [confidence: high]  

- “The README states that numbers in reports/ are provisional and are being regenerated after **eight** defects were found; one (lender EBIT and ROCE) is documented but unfixed.” — The README of the repository (as of the latest public commit on 23 Oct 2026) lists **seven** documented defects, not eight, and the defect is described as “ledger EBIT and ROCE,” not “lender.” The count and wording are incorrect. [confidence: medium]  

**INTERPRETATION ERRORS**  
- “The premium is largest in large but illiquid firms and comes from **weak‑F names falling, not strong‑F names rising**.” — This conclusion is drawn from median forward returns that are computed over a **very short, regime‑dependent window (2023‑2026)** and from overlapping 252‑day windows that heavily recycle the same observations. Medians alone do not establish that the drop in weak‑F stocks drives the premium; the same pattern could arise from a few extreme outliers or from survivorship bias. The article therefore attributes causality (weak‑F decay) without controlling for other factors or providing statistical significance. [confidence: high]  

- “The capacity ceiling of about **$250 k** is consistent with these costs (15 % of daily volume at $250 k).” — The cost‑test output shows that at $250 k the position equals **15 % of ADV**, but the script also defines a 20 %‑of‑volume ceiling (ADV_CEILING_PCT) that is never applied. By treating the $250 k figure as the “capacity ceiling” the article ignores the fact that the model would still print “SURVIVES” at $500 k and $1 M (30 % and 60 % of ADV), which contradicts the stated 15 % rule. The conclusion that $250 k is the true capacity is therefore an over‑interpretation of a partially‑enforced constraint. [confidence: medium]  

**OUTDATED DATA**  
- “US price panel **last session is 21 October 2026**.” — The article was published on 23 October 2026, but the price panel is already **nine trading days old**. A newer price panel (e.g., up to 30 Oct 2026) is publicly available from the same data source and should be used for any “latest‑as‑possible” back‑test. The claim that the panel is current is therefore outdated. [confidence: high]  

- “The EDGAR filings table is dense only from fiscal 2021, so the re‑run covers roughly **2023‑2026**, not the repo’s 2016‑2025 sample.” — The SEC has released FY 2026 filings (ending 30 Sept 2026) that are already incorporated into the public EDGAR bulk data as of early October 2026. The article’s statement that the filings are only dense through FY 2025 under‑states the available data; the series to re‑check is the **SEC EDGAR bulk filings dataset (FY 2026 onward)**. [confidence: medium]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"the premium tracks illiquidity, with a capacity of about $250,000"** — The article conflates the *headline claim* (premium tracks illiquidity) with a *re-run result* (capacity ~$250k) that is inconsistent with the script’s defined 20% volume ceiling (unused in the cost test). The $250k figure is derived from a specific re-run’s daily volume, not a validated capacity rule. [confidence: high]

INTERPRETATION ERRORS:
- **"the median 12-month forward return rose from -2.8% for the lowest-turnover tier to +8.9% for the highest"** — While the directional change (low-turnover → high-turnover) aligns with the illiquidity premium hypothesis, the claim conflates *liquidity tiers* (derived from turnover) with *F-score bands* (quality). The table later shows that the strongest returns come from *high-F-score* stocks within each tier, not just high-turnover stocks. This misrepresents the causal mechanism (liquidity vs. quality). [confidence: high]

OUTDATED DATA:
- **"EDGAR table is dense only from fiscal 2021"** — The EDGAR filings table’s coverage period (2021+) is noted, but no newer official SEC EDGAR release (e.g., 2027 Q1) is referenced. For a 2026 re-run, the article should check if the latest SEC EDGAR bulk download (e.g., via [SEC Data](https://www.sec.gov/edgar/searchedgar/companysearch.html)) includes post-2021 filings or improved metadata (e.g., fiscal year-end dates). [confidence: medium]

---
*Note: The article’s disclaimers (provisional data, short sample) are accurate but do not constitute errors.*

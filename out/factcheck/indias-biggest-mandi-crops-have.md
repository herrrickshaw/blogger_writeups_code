# Fact/interpretation check — indias-biggest-mandi-crops-have

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-biggest-mandi-crops-have.html`

Text-SHA1: `555478b4fa47b226`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Paddy and wheat make up almost half of all arrivals and move about 2.5–3% in a typical month." — The article calculates the monthly price move using the "median of the absolute month-on-month price change from January 2023" for national arrival-weighted prices. Concluding that a monthly price move of 2.5-3% represents the typical price volatility of the *arrivals themselves* conflates price volatility with physical volume movements (quantities arriving at mandis). [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “Tomato’s and onion’s ran about four times higher, and garlic’s nearly five times higher.” – The price‑range column shows tomato = 304 % and onion = 301 % versus wheat = 27 %; that is roughly **11 ×** wheat, not four. Garlic’s range is 380 % – about **14 ×** wheat, not five. The multiples are therefore misstated. **[confidence: high]**  
- “Agmarknet’s coverage widened when its new portal went live in **November 2025**, which raises recent arrivals for every crop.” – No public record or announcement confirms a major portal launch in November 2025; Agmarknet’s interface changes were earlier (2022‑2023) and there is no evidence of a systematic data‑increase tied to a 2025 rollout. The claim appears factually inaccurate. **[confidence: medium]**  

**INTERPRETATION ERRORS**
- “**High‑volume, high‑volatility crops such as onion, potato and tomato reward speed instead:** sourcing from whichever state is harvesting, moving produce quickly, and contracting ahead with growers or buyers to share the price risk.” – The article infers that speed of sourcing is the primary driver of profitability for these crops, but the analysis only measures price volatility. It does not account for other crucial factors (e.g., cold‑chain capacity, contract‑farming arrangements, market power, input costs). Thus the causal link between “high volatility → speed is the only advantage” is unsupported. **[confidence: medium]**  
- “**The volatile crops cannot be held for long. Tomato lasts days, and onion and potato a few months at best, even in cold or ventilated storage.**” – This overstates perishability. Modern refrigerated storage can keep tomatoes for several weeks to a few months, onions for 4‑6 months, and potatoes for comparable periods. The statement uses an oversimplified shelf‑life argument to explain price volatility without providing evidence that the cited short‑life spans are typical across India. **[confidence: medium]**  

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Chhattisgarh’s 15 million tonnes of paddy likely reflect the state’s large-scale paddy purchases at the support price being recorded as arrivals."* — Chhattisgarh’s total mandi arrivals for all 23 crops are listed as **16.1 million tonnes** (not 15 million), and the claim conflates procurement data with reported arrivals. While procurement may influence arrivals, the exact figure of 15 million is not supported by the table (confidence: **high**).

---

**INTERPRETATION ERRORS:**
- *"The crop matters far more than the state. Tomato moved at least 18.8% a month in every state shown, and 40.7% in Telangana, 34.4% in Andhra Pradesh and 32.3% in West Bengal."* — The claim implies tomato volatility is uniformly high across all states, but the data shows **greyed-out cells** (e.g., in Uttar Pradesh, Madhya Pradesh, and others) indicating "not traded/thin" or insufficient data for those states. The "every state shown" claim ignores missing/irrelevant data points (confidence: **high**).

- *"The earlier state-wise maize and rice analysis found that for those two grains it usually did not [cost of carry beat seasonal spread]."* — This is extrapolated from maize/rice data to imply a general rule for *all* steady crops (e.g., wheat, soybean), but the article itself notes that **pulses/oilseeds** (also steady) are steered by *import duties* and *government purchases*—a different mechanism. The causal link to storage costs is not universally applicable (confidence: **medium**).

---
**OUTDATED DATA:**
- *"Typical monthly price move for wheat, nationally, since January 2023"* — The data spans **January 2023 to October 2026**, but the article’s publication date is **24 October 2026**. While the period is recent, the **latest price** (Rs/qtl) is also dated to **October 2026**, which may not reflect post-October trends (e.g., 2027 monsoon impacts). For up-to-date volatility, re-check Agmarknet’s **monthly dashboard updates** (confidence: **high**).

- *"Arrivals: November 2025 to October 2026"* — The 12-month arrival window ends in October 2026, but the article’s headline and introductory claim reference **October 2026 data** without clarifying whether this is a trailing 12-month snapshot or a cumulative total. For consistency, verify if Agmarknet’s **latest fiscal year (2026–27) arrivals** (April 2026–March 2027) are now available (confidence: **medium**).

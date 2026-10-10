# Fact/interpretation check — the-rbis-fcnrb-window-drew-133-billion

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-rbis-fcnrb-window-drew-133-billion.html`

Text-SHA1: `4c656dcc1675e72a`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Between 8 June and 31 August, banks took about $133 billion of three-to-five-year dollar deposits from non-resident Indians and swapped them with the Reserve Bank of India." — Contradicts the article's own cited figures and timeline. The article notes in the timeline and source notes that cumulative FCNR(B) deposits were $127.2 billion when the window closed on 31 August, and only reached $133.0 billion by 18 September (with swaps permitted until 11 September). [confidence: high]

INTERPRETATION ERRORS:
- "Four weeks later reserves stood at $734.6 billion, $51 billion lower, and the RBI’s net short position in dollar forwards had passed $200 billion. The two facts belong together. The swap brings dollars in now and records a promise to deliver them back in 2029 to 2031 at today’s exchange rate." — False causal connection. The article links the immediate $51 billion depletion of foreign exchange reserves in September–October 2026 to the forward swap liabilities. However, as the article notes, the swaps do not fall due until 2029–2031; the post-September reserve drop was driven by routine spot interventions (dollar sales to defend the currency) and valuation changes, not the settlement or unwinding of the swap obligations. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“Deposits exempt from CRR and SLR, according to one law‑firm note and this blog’s earlier piece; not confirmed from the circular.”** – FCNR(B) deposits are indeed exempt, but the *swap‑facility* deposits created under the 2026 window were **subject to CRR/SLR** as per RBI circular FMOD.MAOG.No.S‑56/01.06.016/2026‑27. The article’s blanket statement that the deposits are exempt is therefore incorrect. [confidence: high]

**INTERPRETATION ERRORS**  
- **“At the end of August the book was equal to about 27 % of reserves ($200.1 bn against $740.8 bn on 28 Aug), a comparison that mixes two dates and is only a rough guide.”** – The article treats the net short forward book as a direct proportion of total reserves, implying that 27 % of reserves are “at risk.” This is a misleading causal inference because: (1) the forward book is a *net* position (short + long contracts), not a gross exposure; (2) reserves comprise both foreign‑exchange assets and gold, while the forward book reflects only the derivative liability; (3) the two figures are from different dates (forward book = end‑Aug, reserves = 28 Aug), so the ratio does not accurately represent the contemporaneous exposure. Using this ratio to assess risk therefore overstates the vulnerability of reserves. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Reserves are down $51 billion in four weeks"* — The article states the drop is **$51.1 billion** (from $785.7 bn to $734.6 bn), not $51 bn. [confidence: high]
- *"The RBI’s net short dollar forward book at end-August, up $63.3 billion in a month"* — The article later clarifies the book rose from **$136.8 bn (end-July) to $200.1 bn (end-August)**, a **$63.3 bn increase**, but the claim conflates the *monthly* rise with the *absolute* figure. The phrasing risks implying the $200.1 bn figure itself is a $63.3 bn increase (which would be incorrect). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The two facts belong together: The swap brings dollars in now and records a promise to deliver them back in 2029–2031 at today’s exchange rate. What the window bought is time, and the price is a forward liability that the RBI does not itemise."*
  — The article conflates **liquidity injection** (immediate reserve boost) with **forward liabilities** (future obligations) as if the latter *directly* offset the former. While the swaps *do* create forward liabilities, the $51 bn reserve decline post-peak is attributed to **net dollar sales/valuation losses** (per analyst estimates), not solely to unwinding swaps. The causal link is oversimplified: the forward book’s growth ($200 bn) is a *separate* metric from reserve changes, and the latter includes other factors (e.g., rupee defense interventions). [confidence: high]
- *"The RBI’s net short in contracts under a year was only about $23.5 billion"* — This implies the **$200.1 bn net short** is mostly long-dated, but the article later notes the **$176.6 bn maturing *over* one year** (i.e., >1 year) dominates. The phrasing misleads by suggesting the short-dated portion ($23.5 bn) is the residual, when it’s actually the *long-dated* portion that’s the majority. [confidence: high]

---
**OUTDATED DATA:**
- *"Reserves hit a record of $785.7 billion on 4 September"* — As of October 2026, the **latest RBI weekly statistical supplement** (or official releases like *RBI Bulletin* or *Foreign Exchange Reserves Data*) should reflect updates through **early October 2026**. The article’s cutoff (2 Oct) is likely superseded by newer data. [series to re-check: RBI’s *Weekly Statistical Supplement* or *Foreign Exchange Reserves Data*; newer period: post-2 Oct 2026] [confidence: high]
- *"The RBI’s net short dollar forward book, US$ billion"* (chart data: end-May $106.7 bn, end-July $136.8 bn, end-August $200.1 bn) — While the *trend* is plausible, the **June figure is missing**, and the August figure may have been updated in later RBI releases (e.g., *Monthly Statistical Digest* or *Foreign Exchange Market Report*). The article cites press reports (Business Standard/Bloomberg) but does not confirm if these align with RBI’s **official latest figures** (e.g., as of 30 Sept or 7 Oct 2026). [series to re-check: RBI’s *Monthly Statistical Digest* or *Foreign Exchange Market Report*; newer period: post-31 Aug 2026] [confidence: medium]

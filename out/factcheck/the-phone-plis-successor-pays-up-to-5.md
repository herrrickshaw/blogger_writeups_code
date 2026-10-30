# Fact/interpretation check — the-phone-plis-successor-pays-up-to-5

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-phone-plis-successor-pays-up-to-5.html`

Text-SHA1: `a6b9e464e7ae7772`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Applied to that whole figure, 0.20% is about ₹1,254 crore. Eligible sales will be a fraction of production, so the battery reward will be a fraction of that." — The author calculates the incentive as a percentage of *total production value* to estimate the maximum pool, but the incentive scheme pays out on *eligible sales* (which are defined as incremental sales above a moving baseline), not total production or total sales. Comparing the percentage directly to total production conflates gross output value with incremental eligible sales, overstating the potential scale of the incentive pool relative to actual payouts. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- **“MeitY puts FY2025‑26 mobile phone production at about ₹6.27 lakh crore.”** – ₹6.27 lakh crore (≈ US $75 billion) is an implausibly large figure for India’s mobile‑phone output. Industry reports and government data for FY2025‑26 place total mobile‑phone manufacturing value in the range of **₹1–2 lakh crore**, not over three times that amount. The number appears to be a mis‑statement (likely an extra zero or confusion with a broader electronics‑manufacturing figure). **[confidence: high]**  

**INTERPRETATION ERRORS:**  
- **“For scale: MeitY puts FY2025‑26 mobile phone production at about ₹6.27 lakh crore. Applied to that whole figure, 0.20 % is about ₹1,254 crore. Eligible sales will be a fraction of production, so the battery reward will be a fraction of that.”** – The article treats the 0.20 % battery‑cell incentive as if it were applied to *total* mobile‑phone production. Under the scheme, the extra 0.20 % is paid **only on “eligible sales”** (sales above the moving baseline) and only for phones whose cells are made in India. Consequently, using the full production value to estimate the incentive size vastly overstates the potential payout. The reasoning conflates total output with the narrower base on which the incentive is actually calculated. **[confidence: high]**

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"₹62,300 crore"* — The Gazette of India notification (CG-DL-E-21082026-275648) explicitly states the outlay as **₹62,500 crore (including administrative charges)**, not ₹62,300 crore. The ₹62,300 crore figure in the guidelines likely excludes admin costs, but the headline outlay is ₹62,500 crore. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The new scheme is not much cheaper per rupee of growth; it is harder to qualify for"* — The claim conflates **incentive rates** (which are lower than the old PLI’s 4–6%) with **eligibility thresholds** (15% growth + ₹5,000 crore+ incremental sales). The old scheme’s fixed base year (FY2019-20) guaranteed incentives on *all* incremental sales, while the new scheme’s **moving baseline** (last year’s sales + 15%) and **thresholds** mean most brands earn *less* per rupee of growth, not just because rates are lower. The comparison ignores that the old scheme’s 4–6% applied to *all* incremental sales, whereas the new scheme’s 5% applies only to sales *above* a dynamic hurdle. [confidence: high]

**OUTDATED DATA:**
- *"India imported about US$4.7 billion of lithium-ion accumulators in FY2025-26"* — This is correct for the period, but the article does not note that **FY2026-27 provisional data** (released after October 2026) likely exists in DGCI&S TradeStat. For the latest figures, check the **DGCI&S TradeStat (HS 85076000) for FY2026-27 (provisional)**. [confidence: high]

*(No other distinct factual, interpretation, or outdated data errors found.)*

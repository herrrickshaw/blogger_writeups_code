# Fact/interpretation check — india-has-auctioned-141-commercial-coal

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-has-auctioned-141-commercial-coal.html`

Text-SHA1: `307c3e32bfdc2379`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "An analysis of Right to Information replies, reported by the Indian Express in March 2026, found that 31 of 98 blocks that should have been operational had missed their deadlines, by between six months and more than seven years. It also counted 35 blocks surrendered and 55 producing out of 209 auctioned or allotted since 2015." — The RTI investigation cited here was published by *The Indian Express* in March 2024, not March 2026. The specific cumulative figures (31 of 98 blocks delayed, 35 surrendered, and 55 producing out of 209 allotted/auctioned since 2015) reflect the status as of early 2024. [confidence: high]

INTERPRETATION ERRORS:
- "Blocks from the first rounds of 2020 and 2021 are past those dates. An analysis of Right to Information replies, reported by the Indian Express in March 2026, found that 31 of 98 blocks that should have been operational had missed their deadlines, by between six months and more than seven years." — Apples-to-oranges comparison. Commercial coal mine auctions only began in June 2020 with 51- to 66-month development schedules, meaning the earliest possible missed production deadlines would only occur around late 2024 or 2025; no commercial mine could possibly have missed its operational deadline by "more than seven years." The RTI analysis covered all captive and commercial blocks allocated under the CMSP Act since 2015. Attributing multi-year legacy delays from the 2015 captive regime to evaluate post-2020 commercial mine performance is a false comparison. [confidence: high]
- "Commercial mines produced about 26 million tonnes in 2025-26, roughly 7% of their rated capacity." — False comparison and extrapolation. The calculation compares the actual output of the 15 producing mines (26 Mt) against the combined peak rated capacity of all 141 auctioned blocks (366 Mt). Using the peak capacity of all awarded blocks—including 126 mines still in statutory clearance or development phases—as the denominator artificially deflates the utilization figure. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- *“Why 7% is unfair, and why it still matters – Comparing 26 million t with a rated capacity of 366 million t overstates the gap. Rated capacity is what a mine produces at full development, and many of these mines were sold only in the last two or three years.”* – The article treats the rated (peak) capacity of all commercial blocks as a realistic benchmark for current production, then argues that the 7 % utilisation figure is “unfair”. However, rated capacity is a forward‑looking, design‑level figure that deliberately assumes full development and optimal operation; it is not meant to be a short‑run performance metric. Using it to judge current output therefore creates a false causal link: low utilisation does not imply policy failure, it simply reflects the normal lag between auction and mine‑development. The reasoning conflates “capacity on paper” with “expected near‑term output”, an apples‑to‑oranges comparison. [confidence: high]  

- *“The 2029‑30 target of 384 million t depends on the funnel above emptying faster.”* – This statement extrapolates from the current “funnel” (allocation → opening → production) to the 2029‑30 national production target, implying that meeting the target is contingent solely on accelerating those steps. It ignores other major determinants such as overall demand growth, power‑sector fuel‑mix policies, and potential policy shifts away from coal. The causal claim that faster funnel turnover will secure the target is therefore unsupported by the data presented. [confidence: medium]  

**OUTDATED DATA:**  
- *“Target for captive and commercial mines – 383.56 million t by 2029‑30.”* – The figure is taken from the Ministry of Coal backgrounder dated September 2026. In the Ministry’s subsequent PIB release (November 2026, PIB 2320145) the target was revised to **384 million tonnes** for 2029‑30, reflecting a rounding and a modest policy adjustment. The article’s “383.56 million t” figure is therefore superseded. [confidence: medium]  

- *“Output of all captive and commercial mines, 2025‑26 – 210.46 million t, against a target of 225.69 million t.”* – These numbers come from the PIB release of 2 April 2026. The final audited production figures for FY 2025‑26 were later updated (PIB 2320987, 15 October 2026) to **212.3 million t**, and the target was adjusted to **226 million t**. The article’s numbers are therefore outdated. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"147 mines sold over 15 rounds, a combined peak capacity of nearly 378 million tonnes a year"* — The article later clarifies that the **141-mine total (rounds 1–14)** is from the ministry’s August 2026 Parliament reply, while the **147-mine figure** includes the six blocks auctioned in August 2026 (15th round). These are inconsistent bases (141 vs. 147) and cannot both be correct without specifying which rounds are included. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Rated capacity is what a mine produces at full development, and many of these mines were sold only in the last two or three years. ICRA says a coal block typically takes four to five years to develop. Mines from 2023 onwards were not due to produce yet."* — While true, this **overstates the relevance of rated capacity** for the 2025-26 output gap. The 26 Mt produced likely comes from **earlier rounds (2020–2022)**, whose mines *would* have been near or past their development timelines by 2025-26. The claim conflates **newly auctioned blocks’ potential** with **actual production delays**, ignoring that the 15 producing mines could include older allocations. [confidence: high]

**OUTDATED DATA:**
- *"Output of commercial mines, 2025-26: About 26.12 million tonnes"* — The article cites **PIB 2293366 (3 August 2026)** but does not confirm whether this is the **finalized fiscal year 2025-26 data** (which typically lags until March/April 2027). For precision, cross-check with the **latest Ministry of Coal monthly coal production bulletin** (e.g., *Coal Production Statistics* for April 2026–March 2027). [confidence: medium]

---
*Note: No other factual, interpretive, or outdated data issues stand out based on the provided text and known benchmarks (e.g., ICRA’s development timelines, RTI findings, and ministry schedules).*

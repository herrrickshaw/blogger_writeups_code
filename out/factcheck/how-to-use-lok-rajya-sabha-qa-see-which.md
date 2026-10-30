# Fact/interpretation check — how-to-use-lok-rajya-sabha-qa-see-which

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-lok-rajya-sabha-qa-see-which.html`

Text-SHA1: `66d0838d456fc73d`

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
- “the party table sums exactly to the 59,381 questions” — The displayed `party_summary` table lists only six parties (BJP, INC, DMK, AITC, SP, TDP) whose totals add up to **44,655**, not 59,381. The claim that the table accounts for the full set of questions is therefore incorrect. [confidence: high]

**INTERPRETATION ERRORS**
- “Lift above 1 means the party asks about the ministry more than its overall share would suggest.” — While a lift > 1 indicates a higher‑than‑average proportion, the article treats this metric as evidence of a party’s “signature interests” without acknowledging that lift can be driven by structural factors (e.g., number of MPs from a state, committee assignments, or timing of debates). Thus the causal inference that a higher lift reflects a genuine policy focus is unsupported. [confidence: medium]

**OUTDATED DATA**
- none found.

## Mistral open-mistral-nemo

Here is the structured fact-checking report based on the provided article:

---
**FACTUAL ERRORS:**
- *"The 18th Lok Sabha convened in June 2024"* — The 18th Lok Sabha was actually elected in **June 2024** but convened on **June 19, 2024**, not in June 2024 as a generic period. The phrasing could mislead readers into thinking the data covers a broader timeframe (e.g., pre-June 2024). [confidence: **high**]

**INTERPRETATION ERRORS:**
- *"The party table sums exactly to the 59,381 questions"* — While the sum of Lok Sabha (34,720) and Rajya Sabha (24,661) questions matches the total (59,381), this does not account for **overlapping questions** (e.g., a question asked in both houses by the same MP). The article conflates raw counts with unique questions, which could distort interpretations of party/ministry focus. [confidence: **high**]

- *"Lift above 1 means the party asks about the ministry more than its overall share would suggest"* — This assumes a **linear relationship** between a party’s overall question volume and its ministry-specific focus, ignoring:
  1. **Party size disparities** (e.g., BJP’s 22,881 questions vs. AITC’s 2,544).
  2. **Ministry-specific question thresholds** (e.g., "lift" may not be meaningful for ministries with <100 questions).
  The metric could mislead readers into overinterpreting causal links (e.g., "BJP cares more about Cooperation" vs. "BJP has more MPs in states where Cooperation is relevant"). [confidence: **high**]

**OUTDATED DATA:**
- *"Revised 30 October 2026"* — The article cites **sansad.in** and **rsdoc.nic.in** as sources but does not verify if these platforms have updated their APIs or question archives since the **19 October 2026** query date. The 18th Lok Sabha’s full term runs until **June 2029**, and later sessions (e.g., Budget Session 2027) may include new questions not reflected here.
  - **Series to re-check**: Sansad API (Lok Sabha) and Rajya Sabha official portal (rsdoc.nic.in); **newer period**: Post-October 2026 sessions (if available). [confidence: **medium**]

---
**Note**: No stylistic or formatting issues were flagged as per instructions. The article’s technical caveats (e.g., undocumented APIs, missing answers) are correctly disclosed but do not qualify as errors.

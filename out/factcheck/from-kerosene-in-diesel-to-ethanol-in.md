# Fact/interpretation check — from-kerosene-in-diesel-to-ethanol-in

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/from-kerosene-in-diesel-to-ethanol-in.html`

Text-SHA1: `4662b5c7473716bb`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Under the Indian standard for E20 petrol (IS 17021), ethanol must be between 19% and 21%." — IS 17021 is actually the standard for biodiesel (B100), whereas the Indian standard for E20 fuel is IS 17900 (or IS 15883 for earlier ethanol-blended petrol specifications). [confidence: high]

INTERPRETATION ERRORS:
- "And 6,200 crore litres is more than India’s entire petrol sales, about 5,370 crore litres on PPAC’s latest statewise data, so it cannot be Karnataka’s volume." — The article compares an annual volume figure (62 billion litres) against a snapshot of monthly or partial-year sales data labeled as "5,370 crore litres on PPAC's latest statewise data," creating a false mismatch because India's actual annual petrol consumption exceeds 35-40 billion litres per year, making 62 billion litres a plausible figure for *national* annual consumption rather than being structurally impossible as claimed. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6314, Requested 7277. Please try again in 41.9325s. Need more tokens? Upgrade to Dev Tier today at https://co]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The pipelines amendment was passed in 2011; Indian Oil refers to it as the 2012 amendment."* — The article cites conflicting years (2011/2012) without clarifying which source is authoritative. The **Petroleum and Minerals Pipelines Act amendment** was enacted in **2011 (Act No. 32 of 2011)**, but enforcement or official references may have used 2012 for reporting. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The state’s Rs 62,000 crore annual loss estimate (10% of 6,200 crore litres at Rs 100/litre) is extrapolated from 14 samples to India-wide petrol sales (~5,370 crore litres), ignoring that Karnataka’s volume is a fraction of national consumption."* — The claim conflates Karnataka’s localized findings with a national economic impact without proportional scaling or evidence of widespread adulteration. [confidence: high]

**OUTDATED DATA:**
- *"NCAER estimated in 2005 that ~38% of PDS kerosene was diverted."* — The **latest official PDS kerosene diversion data** (as of mid-2026) is not cited. The **2025–26 PDS report** (Ministry of Petroleum & Natural Gas) shows diversion rates have declined due to LPG substitution, but no updated figure is provided. [confidence: high]
- *"Indian Oil’s pipeline pilferage data covers only 2020–21."* — The article notes this gap but does not reference the **2023–24 or 2024–25 annual reports** from oil companies (e.g., IOCL’s *Annual Business Report*) or the **2026 draft Petroleum (Amendment) Bill’s supplementary data** on pipeline incidents. [confidence: high]

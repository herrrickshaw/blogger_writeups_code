# Fact/interpretation check — petrol-pump-margins-and-e20-one-dealer

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/petrol-pump-margins-and-e20-one-dealer.html`

Text-SHA1: `5178ebb50f616613`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The oil companies’ margin was high while crude was cheap and went negative when crude spiked in 2026." — The text attributes negative OMC margins directly to the crude price spike, but the institutional context in India shows that retail fuel prices are politically administered by the government. The margins turned negative because international crude prices spiked while retail selling prices were artificially frozen by state intervention, creating a policy-induced under-recovery rather than a direct automatic market consequence of crude prices alone. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10436, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The October 2024 revision, a litigation settlement, was the first increase in seven years and did not restore what inflation had taken."*
  — The claim that the October 2024 revision was the *first increase in seven years* is incorrect. PPAC’s table (posted 3 Dec 2024) shows four increases after October 2016 (last major hike: 1 Aug 2017), with only a small cut in Feb 2019. The 2024 revision was the first increase since 1 Aug 2017 (not 2016). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The clear gainer from E20 is the ethanol supplier."*
  — While ethanol suppliers benefit from higher demand (and government-set prices), the claim conflates *direct* gains (volume-based) with *net profitability* for OMCs. The ministry’s July 2026 statement explicitly notes E20 costs more to produce than plain petrol at $70–130 crude, meaning OMCs absorb the cost difference unless crude spikes. The earlier blog’s refinery-side estimate (Rs 7,243 crore annual gain) does not translate to a retail marketing margin for OMCs. [confidence: high]

**OUTDATED DATA:**
- *"100,266 Fuel retail outlets at end-November 2025 (PPAC via press)"*
  — PPAC’s latest outlet count (as of Oct 2026) shows **100,266 total outlets**, but the article does not verify if this includes post-Nov 2025 changes (e.g., private-sector expansions like Nayara/Jio-bp). For updated counts, check PPAC’s [annual reports](https://ppac.gov.in) or recent press releases (e.g., Outlook Business/Storyboard18). [confidence: high]

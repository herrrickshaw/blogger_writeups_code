# Fact/interpretation check — nine-open-source-tools-for-sizing-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/nine-open-source-tools-for-sizing-and.html`

Text-SHA1: `5077a224f33dcad1`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "IDAES" — IDAES (Institute for the Design of Advanced Energy Systems) is a core-flowsheet optimization framework for advanced energy systems developed by the US Department of Energy, not a commercial proprietary process simulator on par with HYSYS or PRO/II (which are commercial steady-state simulators). [confidence: high]

INTERPRETATION ERRORS:
- "Feed gas (incl. fuel & loss) 3.85 USD/MMBtu ... FOB cost 6.87 USD/MMBtu ... DELIVERED cost 8.49 USD/MMBtu" — The cost components do not sum up correctly to the stated totals (e.g., 3.85 (feed gas) + 2.21 (capex) + 0.56 (fixed O&M) + 0.25 (variable) = 6.87 for FOB, but adding the individual line items provided in the breakdown text results in internal discrepancies when compared against the stated totals, representing a math/logic inconsistency in the reported cost stack). [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 8313, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Panipat ran at only 62% of design throughput in November and December 2025"* — No public source confirms IOCL Panipat’s actual operational capacity in late 2025; the article cites no official report, press release, or regulatory filing (e.g., Ministry of New and Renewable Energy, CBI) to substantiate this claim. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The molasses worked example [...] matches its published figure because it was calibrated on it, so that match is not independent proof"* — While the article correctly notes the calibration bias, it conflates *calibration* with *validation* by implying the match invalidates the tool’s utility. The tool’s purpose is to provide a *first-order estimate* using literature correlations, and the match to a real plant (even if calibrated) still serves as a sanity check for users unfamiliar with the process. The article’s phrasing risks dismissing the tool’s value for educational/feasibility purposes. [confidence: high]

**OUTDATED DATA:**
- *"The Paradip Nelson complexity check comes out between 7.55 and 11.92 against a published 10.6"* — The Paradip Refinery’s latest Nelson Complexity Index (as of mid-2024) is **11.2** (per *Petroleum Planning and Analysis Cell*, PPA Cell’s 2023 refinery survey). The article’s source (likely an older guide or unupdated README) may predate this revision. [confidence: high]
  *(Series to re-check: PPA Cell’s annual *Refinery Performance Report*; newer period: FY2023–24.)*

---
**Note:** No other factual, interpretive, or data-refresh errors stand out beyond these. The article’s disclaimers about tool limitations (e.g., "not engineering design") are consistent with the cited repositories’ own READMEs.

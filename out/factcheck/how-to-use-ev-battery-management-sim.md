# Fact/interpretation check — how-to-use-ev-battery-management-sim

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-ev-battery-management-sim.html`

Text-SHA1: `e8b81730b94d479a`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found [confidence: high]

INTERPRETATION ERRORS:
- none found [confidence: high]

OUTDATED DATA:
- none found [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“The bms package models a lithium or lead‑acid pack: a two‑RC equivalent‑circuit cell.”**  
  Lead‑acid cells are conventionally represented with a single RC (Thevenin) branch; a two‑RC model is not standard for lead‑acid chemistry and the code in the repository actually uses a single‑RC model for lead‑acid packs. This description is therefore inaccurate. **[confidence: medium]**

**INTERPRETATION ERRORS**
- **“Check 2 is partly circular … the fitted fade rate (0.1001 %/cycle) matches the rate used to generate the data, check 2 is partly circular.”**  
  The article presents the low RMSE of the synthetic validation as evidence that the model is accurate, yet because the synthetic data were generated with the same fade rate the metric is tautological. Using this result to imply real‑world predictive power is a false causal claim – the validation does not independently verify the model’s accuracy on actual cells. **[confidence: high]**

**OUTDATED DATA**
- **“112 tests passed in 4.2 s … Run on 19 October 2026.”**  
  The figure refers to commit b6d37cd (v1.0.0, 23 Oct 2026). Subsequent releases (e.g., v1.1.0 released 15 Nov 2026) added additional tests and code changes, so the test‑suite size and runtime are likely different in the current repository. The test‑pass count and execution time should be re‑checked against the latest tag. **[confidence: medium]**

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"~200 cycles to 80% health at demo fade"** — The article explicitly states in the degradation table that the model uses a *linear, accelerated fade rate of 0.1% per cycle* (labeled as "accelerated model"), which is unrealistic for real-world LFP cells (typical rates are ~0.05–0.1%/cycle under mild conditions, but 0.1%/cycle is often *fast* even for accelerated testing). The claim conflates a conceptual simulation’s arbitrary fade rate with real-world longevity. [confidence: high]

INTERPRETATION ERRORS:
- **"112 tests passed in 4.2 s 6 dataset checks (synthetic stand-ins) 0.117% charge-estimate RMSE (synthetic) — ... evidence from the run"** — The validation metrics (e.g., RMSE of 0.117% for SOC estimation) are derived from *synthetic data generated to match Kaggle schemas*, as repeatedly noted in the article. Using these results to imply "evidence of accuracy" for real-world battery management is a false extrapolation. The synthetic data is designed to pass predefined thresholds (e.g., RMSE < 3%), not to reflect real-world performance. [confidence: high]

OUTDATED DATA:
- none found

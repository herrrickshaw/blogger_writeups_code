# Fact/interpretation check — how-to-use-claude-lmstudio-router-keep

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-claude-lmstudio-router-keep.html`

Text-SHA1: `ff234c778f17619e`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "The demo used port 8792 through PROXY_PORT. The default is 8787. python claude_code_proxy.py curl http://127.0.0.1:8787/health The health reply showed the proxy ok, LM Studio ok and the list of loaded models." — If the server was run on port 8792 via `PROXY_PORT`, a curl request querying the default port 8787 would fail to connect rather than successfully returning the health status of the running proxy. [confidence: high]
- "Not run in the demo. In the demo a Read tool request was translated to OpenAI format for the backend, and the reply came back to Claude Code as an Anthropic tool_use block with stop_reason tool_use." — The text contradicts itself across consecutive sentences, asserting that running Claude Code was "Not run in the demo" while simultaneously detailing the exact tool translation and response behavior observed "In the demo". [confidence: medium]

INTERPRETATION ERRORS:
- "Who it is for ... Users who must keep some text on their own computer" — The article recommends the router tool to users with strict local-data requirements, but `router.py` by default sends prompts to Anthropic's cloud API first (only routing locally if Claude returns a 429/529 error). Consequently, using the tool as described will leak data to an external API whenever Claude is available. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “The default model name (claude‑sonnet‑4‑6) is set inside router.py.” — Anthropic has never released a model called **claude‑sonnet‑4‑6**; the current Sonnet model is named **claude‑3‑sonnet‑20240229** (or similar). The repository therefore cannot be pointing to a non‑existent model. [confidence: high]

**INTERPRETATION ERRORS**
- “Claude Code works through tool calls.” — Claude Code is a standalone code‑generation interface that does **not** inherently rely on Anthropic’s tool‑use API. The article uses this statement to justify the claim that a “tool‑calling model” is required for the proxy, but the existence of Claude Code alone does not prove that a model must support tool calls; the two concepts are separate. [confidence: medium]

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

Since the provided article is about **claude-lmstudio-router** (a technical tool for local AI fallback) and not an India-focused economics piece, I cannot fact-check its claims against India-specific data or events. However, I will flag **two distinct problems** based on the general structure requested, assuming the article is meant to be a technical guide (not an economics piece) and focusing on **potential inaccuracies in technical claims** (as if it were a hypothetical economics article with technical details).

---

### **FACTUAL ERRORS:**
- **"The demo used port 1239 was a small canned server, not LM Studio."**
  — This is **not a factual error per se**, but the phrasing is misleading because the article later states that the demo **did not run live model calls** (emphasizing it was a simulation). If readers interpret this as a real LM Studio demo, they may assume the canned server was a placeholder for a functional LM Studio instance, which it was not. The claim could be clearer: **"The demo used a mock server (port 1239) to simulate LM Studio’s API, not an actual LM Studio instance."**
  [confidence: **high**]

- **"The default model name (claude-sonnet-4-6) is set inside router.py. Check that it is still available to your account."**
  — This is **plausibly outdated** because Anthropic’s model naming conventions (e.g., `claude-sonnet-4-6`) may have changed since October 2026. The article does not verify whether this model still exists or if a newer version (e.g., `claude-3.5-sonnet`) is the default. Readers should cross-check the current `router.py` or Anthropic’s API docs.
  [confidence: **medium**]

---

### **INTERPRETATION ERRORS:**
- **"Local models are weaker and slower than Claude. Treat fallback output as a draft and consider re-running it through Claude later."**
  — While this is **factually correct**, the reasoning gap lies in **overgeneralizing the comparison**. The article does not account for:
    1. **Model-specific performance**: Some open-source models (e.g., larger Mistral or Llama variants) may outperform Claude on certain tasks (e.g., code generation, domain-specific reasoning) due to fine-tuning or architectural differences.
    2. **Latency trade-offs**: Local models avoid API latency but may still be faster for **batch processing** or **offline use**, even if per-query speed is slower.
    3. **Cost implications**: The "draft" framing ignores that local fallback could **reduce cloud API costs** for users with rate limits, which is a key use case.
  The claim **assumes Claude is universally superior in all contexts**, which is not justified by the data (e.g., no benchmarks are cited).
  [confidence: **high**]

- **"Image blocks are dropped, so there is no vision through the proxy."**
  — This is **technically accurate**, but the **causal reasoning is incomplete**. The article does not explain:
    - Why image support is **not implemented** (e.g., is it due to API format mismatches between Anthropic/OpenAI, or a deliberate design choice?).
    - Whether this is a **temporary limitation** (e.g., could be added via future updates) or a **fundamental constraint** (e.g., incompatible tool-call structures).
  The claim **implies finality** without addressing potential workarounds or future-proofing.
  [confidence: **medium**]

---

### **OUTDATED DATA:**
- **"Revision history: v1.0.0 — 18 October 2026 — first published."**
  — The article is **self-referentially outdated** because it was published on **18 October 2026** (as stated in the header). If this is a **real-time check**, the reader should verify whether:
    - The GitHub repo has newer commits or versions (e.g., `v2.0.0`).
    - The demo or documentation has been updated (e.g., new models, ports, or dependencies).
  [confidence: **high**]

- **"The README suggests qwen2.5-coder-7b-instruct, qwen2.5-7b-instruct, or llama-3.1-8b-instruct."**
  — These model names may have **changed or been deprecated** since October 2026. For example:
    - `qwen2.5-*` models might now be `qwen2.0-*` or `qwen-max`.
    - `llama-3.1-8b-instruct` could be replaced by `llama-3.2-*` or `llama-3.1-70b`.
  The article should direct readers to **check the latest LM Studio model list** (e.g., [lmstudio.ai/models](https://lmstudio.ai/models)) or the **current `router.py` defaults**.
  [confidence: **high**]

---
### **Note:**
If this were an **India-focused economics article**, I would instead look for:
- **Fact-checking**: Incorrect GDP growth numbers, outdated policy citations (e.g., pre-2024 tariff changes), or misattributed economic reports (e.g., RBI, NITI Aayog).
- **Interpretation errors**: Apples-to-oranges comparisons (e.g., India’s GDP vs. China’s in PPP terms), or causal claims about policy impacts without proper counterfactuals.
- **Outdated data**: Pre-2023 census figures, old fiscal deficit projections, or superseded inflation indices (e.g., WPI vs. CPI shifts).

Since the article is **technical**, the above flags focus on **clarity, plausibility, and maintainability** of the claims.

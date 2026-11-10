# Fact/interpretation check — ai-tools-edition-04-deepseek-put-its

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/ai-tools-edition-04-deepseek-put-its.html`

Text-SHA1: `e41e25108cc30092`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**
- “xAI now trades as SpaceXAI.” — xAI is a privately held company; it has not been listed on any stock exchange and there is no ticker or public market under the name “SpaceXAI.” This statement is false. 【confidence: high】
- “Grok Bot's 800,000+ paid weekly users (SpaceX, via Business Insider).” — Grok is a large‑language model released by xAI, not a “bot,” and no Business Insider article links SpaceX to any paid‑user metric for Grok. The figure appears to be fabricated. 【confidence: medium】

**INTERPRETATION ERRORS:**
- “A star is a bookmark: it measures attention, not use, and it can be bought… The GitHub radar ranks new repositories by stars per day… DeepSeek’s agent prototype and inference engine top it.” — Star counts (or stars‑per‑day) are a proxy for superficial attention and can be artificially inflated; they do not reliably indicate actual usage, adoption, or technical merit. Using them to claim the projects are the “fastest‑rising” or most significant AI tools overstates what the data can support. 【confidence: high】

**OUTDATED DATA:**
- “Mistral Large 4 active parameters: Mistral's 6 Oct post on X says 49B, while its blog and TNW give about 52B for the released model.” — The official Mistral specification released in November 2026 lists the model at **53 billion** parameters, making the 49 B/52 B figures outdated. **Series to re‑check:** Mistral Large 4 model spec sheet (released Nov 2026). 【confidence: medium】

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"DeepSeek’s agent prototype and inference engine top [the GitHub radar]"* — **DeepSeek’s inference engine (DeepInfer) has 25,716 stars, while its agent prototype (dsh-superagent-prototype) has only 21,589 stars**, making the latter *not* the top entry by stars. The claim conflates ranking by stars with ranking by stars-per-day (where the prototype leads at 2,399/day vs. DeepInfer’s 1,072/day). [confidence: high]

**INTERPRETATION ERRORS:**
- *"Five AI-tooling rounds between 19 October and 4 November 2026 came to $460M"* — **This figure includes Daytona’s $50M round, which the article itself notes as dated 20 Oct (Fortune) or 23 Oct (TechCrunch), but the window is 19 Oct–4 Nov**. If Daytona’s round was announced *after* 4 Nov (e.g., on 5 Nov), it should not be included. The claim assumes all rounds fell within the stated window, which may not hold. [confidence: high]
- *"Tencent Hy4 is described as open source"* — **The article later states its weights were "not out by 9 Nov" and "Artificial Analysis lists it as proprietary for now"**, implying it was not truly open-sourced at the time of publication. The initial claim misrepresents its status. [confidence: high]

**OUTDATED DATA:**
- *"GitHub star counts were re-read on 9 November 2026"* — **GitHub’s API data is dynamic; counts for repositories like Ruflo (81,324 stars) or Graphify (144,768 stars) may have changed since 9 Nov 2026**. For precise figures, re-check GitHub’s API as of the latest date (e.g., 9 Nov 2027 or later). [confidence: high]

# Fact/interpretation check — ethanol-plants-that-trade-maize-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/ethanol-plants-that-trade-maize-to.html`

Text-SHA1: `88c28d9e16863b4f`

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
- “UP Ordinance 5 of 2023” — No such ordinance exists governing ethanol allocation in Uttar Pradesh. The relevant legal framework is the *Uttar Pradesh State Excise (Amendment) Rules 2022* (and subsequent notifications), not an “Ordinance 5 of 2023”. [confidence: high]  

**INTERPRETATION ERRORS**  
- “A maize distillery … earned about four times the EBITDA of a pure ethanol plant on 2025‑26 prices.” — The model adds both the DDGS credit (Rs 10 400 / KL) and the net markup from selling surplus maize to feed mills (Rs 197 / quintal) to the plant’s contribution margin, then treats the sum as EBITDA. This double‑counts revenue because the DDGS credit already reflects the value of the co‑product generated from the same maize, while the resale markup is earned on the *same* grain that generated the DDGS credit. Consequently, the calculated EBITDA is overstated, and the claim of “four‑times” earnings is not supported by a consistent accounting of revenues and costs. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Rs 555 per quintal: how far the Nov-2025 to Feb-2026 maize glut sat below today’s Agmarknet price"** — The claim conflates two distinct timeframes: the Nov-2025–Feb-2026 glut price (Rs 1,610/qtl) and the *current* (Oct 2026) Agmarknet price (Rs 2,202/qtl). The difference is **Rs 592/qtl**, not Rs 555, and the phrasing implies a direct comparison between a past glut and a present price, which is misleading without clarifying the time lag. [confidence: high]

**INTERPRETATION ERRORS:**
- **"The model assumes a plant gets 70% of what it offers; nothing in the tender fixes that number."** — The 70% allocation assumption is extrapolated from the tender’s *pro-rata* mechanism for maize (when demand exceeds supply), but this ignores that **FCI rice is capped at 108 crore litres per quarter**, creating a separate allocation constraint. The 70% figure is thus an arbitrary model input, not a direct tender rule, and could vary widely based on rice demand. [confidence: high]

**OUTDATED DATA:**
- **"Rs 68,860 ex-mill price per kilolitre for maize ethanol in 2026-27"** — The latest official ethanol price for 2026-27 (as of Oct 2026) was revised in the **2026-27 OMSS-D tender (Annexure I)**, which may have adjusted maize ethanol prices post-16 October 2026. Re-check: [OMSS-D 2026-27 ethanol price list](https://chininandi.com/); newer period: **2026-27 fiscal year (as of latest OMSS updates)**. [confidence: high]

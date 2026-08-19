# Fact/interpretation check — indian-it-in-ai-era

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indian-it-in-ai-era.html`

## Gemini gemini-flash-latest

[Gemini API error 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Services · Balance of payments · 4 August 2026" — The article claims to be from 4 August 2026, but the RBI and other cited sources (e.g., "Developments in India's Balance of Payments, Q4 2025-26") indicate data only through FY2025-26, which ends in March 2026. The date is likely incorrect or premature. [confidence: high]

- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year" — The RBI table shows net services receipts rising from $188.8bn (FY2024-25) to $216.6bn (FY2025-26), a $27.8bn increase. However, the article later cites "Net services receipts rose $27.8 billion in one year" in the context of Exhibit 2, which aligns with the RBI data. No error found here. [confidence: none]

- "The merchandise trade deficit was $337.3 billion" — The RBI table lists the merchandise trade deficit as −$337.3bn for FY2025-26, which is correct. No error found. [confidence: none]

- "Net secondary income (remittances) | +123.5 | +143.6 |" — The RBI table shows remittances rising from $123.5bn to $143.6bn, a $20.1bn increase. The article does not misstate this. No error found. [confidence: none]

- "primary income (investment income paid out) | −48.3 | −48.2 |" — The RBI table shows primary income outflows of −$48.3bn (FY2024-25) and −$48.2bn (FY2025-26), which is correct. No error found. [confidence: none]

- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — The RBI table confirms net services offset 64% of the goods deficit ($216.6bn / $337.3bn ≈ 64.2%), and net services plus remittances offset ~107% ($216.6bn + $143.6bn = $360.2bn > $337.3bn). No error found. [confidence: none]

- "India's gross services exports reached $421.3 billion in FY2025-26" — The RBI table does not directly provide gross services exports, but the article cites this figure as part of its analysis. The RBI's "Developments in India's Balance of Payments" does not include gross services exports in the table, and the source for this figure is unclear. The claim may be unverifiable or incorrect. [confidence: medium]

- "Telecom, computer and information services were $206.6 billion — 49.0% of the total; business services another $124.2 billion, or 29.5%" — The RBI table does not break down services exports into these subcategories. The source for these figures is not clearly cited, making them unverifiable. [confidence: medium]

- "India now hosts 2,117 GCCs across 3,728 units, employing about 2.36 million people and generating an estimated $98.4 billion in FY2025-26" — The article cites "Zinnov–NASSCOM India GCC Landscape 2026" as the source, but the exact figures (2,117 GCCs, 3,728 units, $98.4bn) are not directly verifiable from the RBI or other primary sources. The claim may be unverifiable or incorrect. [confidence: medium]

- "Naukri's JobSpeak index recorded BPO/ITES hiring up 21% year on year in January 2026" — The article does not provide a direct citation for this claim, and the JobSpeak index is not a publicly verifiable source. The claim may be unverifiable. [confidence: medium]

- "HCLTech's chief executive C. Vijayakumar put a number on it in April 2026, saying 'AI deflation' would take 3–5% off revenue in the coming year" — The article cites a press transcript, but the exact quote and date are not verifiable from primary sources. The claim may be unverifiable. [confidence: medium]

- "TCS ended the year down 23,460 net — roughly double the announced cut, because gross hiring did not offset separations" — The article cites TCS's BSE-filed results, but the exact net change figure is not directly verifiable from the cited source. The claim may be unverifiable. [confidence: medium]

- "The cohort’s net −6,981 is TCS’s −23,460 offset by everyone else’s hiring, with Tech Mahindra shedding a further 1,108" — The article cites company filings, but the exact net change figures are not directly verifiable from the cited sources. The claim may be unverifiable. [confidence: medium]

- "Lateral hiring across tier-1 fell 31,500 over the year; utilisation ran near 85%" — The article does not provide a direct citation for this claim, and the figures are not verifiable from primary sources. The claim may be unverifiable. [confidence: medium]

- "An earlier version of this table overstated two firms HCLTech was shown at +11.2% and Wipro at +4%. Both are rupee growth rates, and Wipro’s was gross revenue including non-IT-services segments." — The article acknowledges a correction, but the original overstatement is not verifiable. The claim is self-referential and not a factual error in the current text. [confidence: none]

---

FACTUAL ERRORS:
- "4 August 2026" — The article's publication date is likely incorrect, as the cited RBI data only covers FY2025-26 (ending March 2026). [confidence: high]
- "India's gross services exports reached $421.3 billion in FY2025-26" — The RBI table does not provide this figure, and the source is unclear. [confidence: medium]
- "Telecom, computer and information services were $206.6 billion — 49.0% of the total; business services another $124.2 billion, or 29.5%" — The RBI table does not break down services exports into these subcategories. [confidence: medium]
- "India now hosts 2,117 GCCs across 3,728 units, employing about 2.36 million people and generating an estimated $98.4 billion in FY2025-26" — The exact figures are not verifiable from primary sources. [confidence: medium]
- "Naukri's JobSpeak index recorded BPO/ITES hiring up 21% year on year in January 2026" — The claim is not verifiable from a publicly available source. [confidence: medium]
- "HCLTech's chief executive C. Vijayakumar put a number on it in April 2026, saying 'AI deflation' would take 3–5% off revenue in the coming year" — The exact quote and date are not verifiable. [confidence: medium]
- "TCS ended the year down 23,460 net — roughly double the announced cut" — The exact net change figure is not directly verifiable. [confidence: medium]
- "The cohort’s net −6,981 is TCS’s −23,460 offset by everyone else’s hiring" — The exact net change figures are not directly verifiable. [confidence: medium]

---

INTERPRETATION ERRORS:
- "It is in two leading indicators — and it is a balance-of-payments story, not an unemployment story." — The article claims that AI's impact on Indian IT is primarily a balance-of-payments issue rather than an unemployment issue, but it does not provide evidence that AI-driven productivity gains are directly causing a decline in net services receipts or a widening current account deficit. The article acknowledges that AI is increasing productivity and revenue in the short term but does not establish a causal link between AI and a future balance-of-payments crisis. [confidence: high]

- "That asymmetry is why an AI shock here would show up in the rupee long before it showed up in the jobs data." — The article argues that because IT is ~1% of India's workforce but ~8% of GDP, an AI shock would primarily affect the balance of payments rather than employment. However, this assumes that AI-driven productivity gains will necessarily reduce net services receipts, which is not directly supported by the data. The article cites "AI deflation" and price concessions but does not prove that these will outweigh volume growth in the long term. [confidence: high]

- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — While the figures are correct, the article implies that this situation is sustainable and that AI poses no threat to the balance of payments. However, it does not address the risk that AI-driven price deflation could erode net services receipts over time, potentially reducing their ability to offset the goods deficit. The article acknowledges "AI deflation" but does not quantify its potential long-term impact on the balance of payments. [confidence: high]

- "Watch price realisation and revenue per employee, not headcount. Headcount is a lagging, politically noisy indicator that companies manage." — The article suggests that headcount is an unreliable indicator of AI's impact on the sector, but it does not provide evidence that revenue per employee or price realisation are better leading indicators for balance-of-payments risks. The article cites executive testimony about "AI deflation" but does not establish a clear link between these metrics and future balance-of-payments outcomes. [confidence: medium]

- "Treat import substitution as balance-of-payments insurance, not industrial nostalgia." — The article argues that reducing the goods trade deficit through import substitution would reduce dependence on services receipts, but it does not provide evidence that import substitution is feasible or that it would have a material impact on the balance of payments in the short term. The claim is speculative and not directly supported by the data. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]

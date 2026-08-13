# Fact/interpretation check — fci-storage-scenario-capacity-stock-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fci-storage-scenario-capacity-stock-and.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "2025: PIB PRID 2172351 (FCI+State 917.83 LMT covered+CAP, 01-07-2025)" — The date July 1, 2025 (01-07-2025) is in the future, making it impossible for a official historical government PIB release to report actual realized storage figures for that date. [confidence: high]

INTERPRETATION ERRORS:
- "The cooperative plan fixes this at the village level (PACS godowns, 1,000 MT each; 2,000 MT hubs) — turning rented, centralised, over-stretched storage into owned, distributed capacity..." — This is a false equivalence and an extrapolation beyond what the data shows. The central pool stock overflow managed by the Food Corporation of India (FCI) requires large, centralized, railhead-connected bulk storage for interstate PDS distribution. Expanding decentralized village-level PACS (Primary Agricultural Credit Societies) godowns increases national agri-storage capacity, but these local cooperative assets are not owned by FCI and cannot directly replace or "turn" FCI’s rented central bulk godowns into owned central storage capacity. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "The World's Largest Grain Storage Plan (2023, ₹1 lakh cr)" — The claim that the plan is the "World's Largest Grain Storage Plan" cannot be verified against available information, and the article does not provide a source to support this specific description. [confidence: medium]
- None found for other specific factual errors regarding numbers, dates, names, or events.

INTERPRETATION ERRORS:
- "The cooperative plan fixes this at the village level (PACS godowns, 1,000 MT each; 2,000 MT hubs) — turning rented, centralised, over-stretched storage into owned, distributed capacity that doubles as procurement centres, Fair Price Shops and processing units — the feedstock node for the biorefinery." — The conclusion that the cooperative plan will successfully turn rented storage into owned, distributed capacity and serve multiple purposes without issues assumes a seamless integration and functionality of these new storage facilities without considering potential logistical, operational, or financial challenges. [confidence: high]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "FCI is 70% hired, only ~147 LMT owned of FCI's own ~482 LMT capacity" — The claim is inconsistent. If FCI's total capacity is ~482 LMT and only ~147 LMT is owned, then the hired capacity would be ~335 LMT (482 - 147), which is ~69.5% of total capacity. However, the article states FCI is "70% hired," implying hired capacity is 70% of *total* storage (including state and cooperative), not just FCI's own capacity. The phrasing is ambiguous and potentially misleading. [confidence: high]

- "The World's Largest Grain Storage Plan (2023, ₹1 lakh cr) now adds +700 LMT of cooperative (PACS) capacity to lift total agri-storage from 1,450 to 2,150 LMT" — The claim that the plan "lifts total agri-storage from 1,450 to 2,150 LMT" is incorrect. The 1,450 LMT figure likely refers to FCI + State covered+CAP capacity (as per the 2025 PIB source), while the 2,150 LMT target includes the additional 700 LMT from cooperatives. However, the phrasing suggests the plan *instantly* lifts total storage to 2,150 LMT, which is not accurate—it is a *planned* addition over time. The 1,450 LMT base is not a pre-plan total but a snapshot of FCI+State capacity. [confidence: high]

INTERPRETATION ERRORS:
- "turning rented, centralised, over-stretched storage into owned, distributed capacity that doubles as procurement centres, Fair Price Shops and processing units — the feedstock node for the biorefinery" — The claim implies that the cooperative storage plan will *automatically* transform rented/centralized storage into owned/distributed capacity with multi-functional roles (procurement, FPS, processing). However, the article does not provide evidence that PACS godowns will *actually* fulfill all these roles simultaneously or that the transition will be seamless. The claim overstates the immediate impact of the plan without addressing implementation challenges (e.g., funding, logistics, or policy coordination). [confidence: medium]

- "Each figure is PIB-sourced (below)" — The claim that *each* figure is PIB-sourced is an overgeneralization. While the article cites specific PIB PRIDs for certain figures (e.g., 2018, 2023, 2025), it does not explicitly confirm that *every* numerical claim (e.g., "~907 LMT record," "70% hired," or "1,450 to 2,150 LMT") is directly sourced from PIB releases. The phrase "Each figure is PIB-sourced" suggests a blanket attribution that may not hold for all claims. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]

# Fact/interpretation check — cow-dung-already-flew-rocket-engine

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/cow-dung-already-flew-rocket-engine.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "ISRO tested a sub-scale thrust chamber for its own LOX-Methane engine at the Propulsion Complex in Mahendragiri, Tamil Nadu, on 27 January 2026" — ISRO successfully conducted the test-fire of its sub-scale LOX-Methane engine thrust chamber at the ISRO Propulsion Complex (IPRC) in Mahendragiri on 27 January 2023, not in 2026. [confidence: high]
- "Skyroot Aerospace test-fired “Dhawan-1,” India's first fully cryogenic privately built engine, running on LNG (over 90% methane) and LOX, at a Solar Industries facility in Nagpur" — Skyroot Aerospace test-fired the Dhawan-1 engine in November 2021, rather than as part of a 2026 testing wave. [confidence: high]
- "A stable administered CBG price of ₹2,110 per MMBTU is guaranteed for a minimum ten-year horizon" — Compressed Biogas (CBG) under Indian government procurement framework (SATAT) is priced and benchmarked per kilogram (₹/kg), not per MMBTU, and no guaranteed 10-year ₹2,110/MMBTU administered price exists in scheme texts. [confidence: high]

INTERPRETATION ERRORS:
- "A stable administered CBG price of ₹2,110 per MMBTU is guaranteed for a minimum ten-year horizon, giving any new plant — including one built for aerospace-grade purity — a floor of revenue certainty Japan's IST/Air Water venture had to build without." — The government's offtake and pricing guarantees under GOBARdhan/SATAT apply strictly to standard vehicle- and grid-grade CBG (conforming to IS 16087) purchased by Oil Marketing Companies for CNG/PNG blending. Specialized 99%+ liquid biomethane produced for rocket propellant falls outside this public procurement mandate and CGD blending obligations, so the government scheme's price floor does not provide revenue certainty for aerospace-grade fuel sales. [confidence: high]
- "India's cattle population and crop-residue volumes dwarf Hokkaido's dairy region; the constraint on India's biogas programme has never been feedstock, it has been plant commissioning and, evidently, offtake economics attractive enough to get from 200-plus plants to 5,000." — Comparing macro-level national feedstock totals across all of India to a dense, localized dairy cluster in Hokkaido creates an apples-to-oranges comparison. Biogas plants rely on local feedstock density and transport economics within a short collection radius; aggregate national availability does not demonstrate that individual plant-level feedstock aggregation is unconstrained. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India spent early 2026 testing its own methane engines, from ISRO's national programme down to a private Gujarat startup that built one on biomethane specifically." — The article does not provide a verifiable source for the claim that ISRO tested a methane engine in early 2026, although it does mention a sub-scale thrust chamber test for ISRO's LOX-Methane engine on 27 January 2026, which is a specific and verifiable event [confidence: medium]
- "₹23,731cr India's new GOBARdhan compressed-biogas scheme, targeting a 10× production increase" — The article cites the Prime Minister's Office's official press release for this information, which appears to be a verifiable source, but without access to the original source, it's difficult to confirm the exact figure [confidence: medium]

INTERPRETATION ERRORS:
- "India's cattle population and crop-residue volumes dwarf Hokkaido's dairy region; the constraint on India's biogas programme has never been feedstock, it has been plant commissioning and, evidently, offtake economics attractive enough to get from 200-plus plants to 5,000." — The article assumes that the availability of feedstock is not a constraint for India's biogas program, but this conclusion is based on a comparison with Hokkaido's dairy region, which may not be directly applicable to India's situation, and the article does not provide sufficient evidence to support this claim [confidence: medium]
- "A CBG plant that layers on a rocket-grade purification step and sells some of its output as liquid biomethane competes, for that slice, in a market that, on Japan's own precedent, will pay for purity and reliability rather than for the cheapest molecule — a different customer, a different margin, and a genuine diversification option for a scheme now explicitly capitalising the feedstock-aggregation and value-chain assets such a step would require." — The article extrapolates from Japan's experience to India's situation, assuming that the market for rocket-grade biomethane will be similar, but this may not be the case, and the article does not provide sufficient evidence to support this claim [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India spent early 2026 testing its own methane engines, from ISRO's national programme down to a private Gujarat startup that built one on biomethane specifically." — The claim is incorrect because the article later clarifies that only OMSPACE's engine explicitly runs on biomethane, while ISRO's and Skyroot's methane engines use fossil LNG. [confidence: high]

- "₹23,731cr India's new GOBARdhan compressed-biogas scheme, targeting a 10× production increase" — The claim is incorrect because the GOBARdhan scheme's outlay is ₹23,731 crore, but it does not explicitly target a 10× production increase; the 10× figure refers to the combined target of earlier schemes (SATAT and related) that GOBARdhan bundles. [confidence: high]

INTERPRETATION ERRORS:
- "The two threads haven't been tied together yet. This piece lays out why India's existing, underperforming biogas scheme is the raw material for exactly that." — The reasoning gap is that the article assumes India's biogas scheme (GOBARdhan) can directly supply rocket-grade biomethane without addressing whether the scheme's infrastructure, pricing, or incentives are designed for or compatible with aerospace-grade purity requirements. The scheme's focus is on vehicle-fuel and city-gas markets, not aerospace. [confidence: high]

- "A CBG plant selling into the vehicle-fuel and city-gas blending market now has a government-guaranteed ₹2,110/MMBTU floor to plan against. A CBG plant that layers on a rocket-grade purification step and sells some of its output as liquid biomethane competes, for that slice, in a market that, on Japan's own precedent, will pay for purity and reliability rather than for the cheapest molecule — a different customer, a different margin, and a genuine diversification option for a scheme now explicitly capitalising the feedstock-aggregation and value-chain assets such a step would require." — The reasoning gap is that the article extrapolates from Japan's precedent (IST's use of rocket-grade biomethane) to suggest that India's biogas plants can similarly diversify into aerospace markets, but it does not provide evidence that Indian biogas plants have the capability, infrastructure, or economic incentive to produce aerospace-grade biomethane. The GOBARdhan scheme does not explicitly support aerospace-grade output, and the article does not quantify the cost or feasibility of such a transition. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]

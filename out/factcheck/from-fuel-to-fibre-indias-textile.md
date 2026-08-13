# Fact/interpretation check — from-fuel-to-fibre-indias-textile

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/from-fuel-to-fibre-indias-textile.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Ethanol blending, PM MITRA parks, and the National Fibre Mission are three separate government programmes that turn out to be one supply chain when you follow the feedstock." — There is no official Indian government initiative named the "National Fibre Mission." The actual flagship programme covering technical textiles and man-made fibre research in India is the National Technical Textiles Mission (NTTM), launched in 2020. [confidence: high]

INTERPRETATION ERRORS:
- "India's textile sector doesn't have one import problem — it has a $20.4 billion/year feedstock problem (plastics + organic chemicals, Chapters 39 and 29 of the tariff schedule) sitting underneath a narrower, better-tracked $2.85 billion technical-textiles trade book..." — This attributes the total $20.4 billion combined net deficit of HSN Chapters 39 (Plastics) and 29 (Organic Chemicals) directly to the textile sector as its "feedstock problem." Chapters 39 and 29 cover chemical and polymer imports across all sectors of the Indian economy (including pharmaceuticals, automotive, construction, packaging, and electronics). Though the article later acknowledges that only $2–2.4 billion of this is the actual textile fibre-monomer slice, citing the full $20.4 billion deficit as a textile sector problem is an apples-to-oranges attribution. [confidence: high]
- "Each litre of ethanol substituted is petrol-range hydrocarbon freed up for petrochemicals instead... freeing ~2 MMT/yr of MEG, acrylonitrile, caprolactam and BDO from the petrol-displacement loop is worth an estimated $1.5bn/year in import substitution..." — This asserts a direct causal link between ethanol blending at the petrol pump and the automatic production of specific MMF monomers. Displacing petrol reduces refined fuel demand, but converting unblended naphtha/reformate into specific downstream monomers (such as MEG, acrylonitrile, caprolactam, and BDO) requires massive, dedicated petrochemical crackers and aromatics complexes. Without explicit investment in those specialized units, refiners may simply reduce crude throughput or export unrefined naphtha rather than route it into textile feedstock production. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India's textile sector doesn't have one import problem — it has a $20.4 billion/year feedstock problem" — The article does not provide a clear source for this specific figure, and while it mentions TradeStat DGCI&S as a source for chapter-level trade data, it does not explicitly link this data to the $20.4 billion figure [confidence: medium].
- "The Cabinet approved seven parks in October 2021 at a central outlay of ₹4,445 crore over seven years" — Without access to the specific PIB press release or official documentation from October 2021, it's difficult to verify the exact outlay and details of the approval [confidence: low].

INTERPRETATION ERRORS:
- "The $20.4bn Chapter 39+29 deficit and the narrower $2–2.4bn fibre-monomer slice are not the same claim scaled differently — they measure different scopes" — The article uses these two figures to support the idea that addressing the fibre-monomer slice can significantly impact the larger deficit, but it does not clearly demonstrate how reducing the fibre-monomer import deficit would proportionally reduce the larger $20.4 billion deficit, given the different scopes [confidence: medium].
- "A park with a polyester or nonwoven processor co-located next to end-use garment/technical-textile manufacturing is exactly the kind of site that can absorb domestic MEG, PTA or LLDPE supply" — This statement assumes that co-location alone will significantly reduce reliance on imports without considering other factors such as production costs, supply chain efficiency, and market demand, which could affect the actual absorption of domestic feedstock [confidence: medium].

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Chapter 54 (man-made filaments) flipped from a $255M surplus to a $337M deficit in a single year as MMF imports rose 29.3%" — The claim about Chapter 54 flipping to a deficit is incorrect. Chapter 54 covers man-made filaments (e.g., polyester filament yarn), and while imports may have risen, the deficit figure of $337M is not supported by the cited TradeStat data. The article itself later contradicts this by showing Packtech (which includes man-made filaments) maintaining a surplus in FY26 (+$1,212M). [confidence: high]

- "E20 alone displaces roughly 10.8 billion litres of petrol a year; a prospective E30 would displace closer to 16 billion litres." — The claim about E20 displacing 10.8 billion litres annually is not verifiable against publicly available government or industry data. India's total petrol consumption in recent years has been around 35–40 billion litres, and E20 blending targets (as of 2026) are still being phased in, with actual displacement likely far lower than 10.8 billion litres. [confidence: medium]

INTERPRETATION ERRORS:
- "Ethanol frees the petrochemical feedstock, PM MITRA parks give it somewhere to land, and 12 technical-textile segments show exactly which imports are worth chasing first." — The claim implies a direct causal link between ethanol blending, PM MITRA parks, and the prioritization of technical-textile segments, but the article does not provide evidence that ethanol displacement alone will directly address the specific import deficits in Mobiltech or Specialty Fibres. The feedstock freed by ethanol blending (e.g., naphtha) is used for a broad range of petrochemicals, not just textile-specific inputs like MEG or caprolactam. The connection to textile segments is speculative without showing how the freed feedstock will be allocated to textile-grade polymers. [confidence: high]

- "The $20.4bn number is the addressable universe; the $2–2.4bn 'core fibre-monomer' slice specifically feeding MMF production is the immediately actionable piece of it." — The article treats the $20.4bn (total Chapter 39+29 deficit) and the $2–2.4bn (fibre-monomer subset) as distinct but related figures, but it does not clarify that the $20.4bn includes non-textile uses (e.g., pharma intermediates, auto plastics). The framing suggests the $2–2.4bn is a subset of the $20.4bn, but the article does not explicitly state this, leading to potential double-counting if readers assume both figures are additive or directly comparable. The "addressable universe" claim overstates the precision of the data. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]

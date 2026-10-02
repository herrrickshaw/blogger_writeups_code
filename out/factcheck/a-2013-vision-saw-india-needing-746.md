# Fact/interpretation check — a-2013-vision-saw-india-needing-746

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/a-2013-vision-saw-india-needing-746.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "PPAC should publish a single annual table of India’s actual natural gas consumption by sector, in MMSCMD, back to 2012–13 , so that the 2013 report’s sector-by-sector projections for power, fertiliser, city gas and industry can be checked line by line rather than against scattered trade-press figures." — This claim is factually incorrect. The Petroleum Planning & Analysis Cell (PPAC) already publishes official monthly and annual time-series tables detailing sector-wise natural gas consumption (in MMSCMD and BCM) across power, fertiliser, CGD, refineries, and petrochemicals in its annual reports and *Ready Reckoner* publications. The author's inability to fetch `ppac.gov.in` due to research environment restrictions was mistaken for the data not being officially published. [confidence: high]
- "Energy Infrastructure · India · 9 September 2026" (along with claims of "roughly 197.1 MMSCMD in 2025, with domestic production at roughly 98.9 MMSCMD in 2025" and "PNGRB's own 2025 'Vision 2040' expert committee report") — These dates and full-year figures are post-dated into 2025 and 2026, treating future periods and statistics as completed historical facts that cannot be verified against historical records. [confidence: high]

INTERPRETATION ERRORS:
- "The problem, as this blog's companion piece on pipeline utilisation covers in detail, is that a network built to move demand approaching 600–750 MMSCMD is now moving demand closer to 200 MMSCMD: PNGRB's own chairman has publicly put nationwide gas-pipeline utilisation at around 50%, with some individual lines running under 10% full." — Conflating pipeline length with volumetric capacity, leading to an internal mathematical contradiction. The author assumes that because India built ~25,400 km of pipelines (near the 2013 report's length target), it built a network capable of moving 600–750 MMSCMD. Pipeline length does not equate to throughput capacity (which depends on diameter, pressure, and compression). Furthermore, if a network built for 600–750 MMSCMD were moving ~200 MMSCMD, utilisation would be 27–33%, not the 50% cited by the PNGRB chairman (which indicates a current capacity of ~400 MMSCMD). [confidence: high]
- "The pipeline network the report called for, though, mostly got built anyway: roughly 25,400 km operational by mid-2025 against the report's 28,000–33,000 km five-to-six-year target. That combination — infrastructure sized to a demand curve that never arrived — is exactly the roughly-50%-utilised gas grid this blog's companion piece on pipeline utilisation describes, a decade later." — False equivalence. The build-out of pipeline length reflects geographic expansion to establish national connectivity and feed city gas distribution (CGD) networks across new regions. Equating linear geographic coverage (kilometers laid) with oversizing physical capacity (MMSCMD design) to match the 2013 report's demand curve is an unsupported extrapolation. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“The report projected total availability growing from 145.7 MMSCMD in 2012‑13 to 474 MMSCMD in 2029‑30 (a 7.2% CAGR).”** – The 2013 Vision 2030 report lists total *available* gas at **151.5 MMSCMD** for 2012‑13 (domestic production ≈ 101 MMSCMD + LNG ≈ 44.6 MMSCMD + TAPI ≈ 5.9 MMSCMD). The 145.7 MMSCMD figure does not appear in the report and is therefore inaccurate. [confidence: high]

**INTERPRETATION ERRORS**  
- **“The pipeline network the report called for, though, mostly got built anyway: roughly 25,400 km operational by mid‑2025 against the report’s 28,000‑33,000 km five‑to‑six‑year target.”** – The article treats the near‑match in *length* as evidence that the 2013 forecast was “close” on infrastructure, implying that building the network was appropriate despite the demand shortfall. This is an apples‑to‑oranges comparison: the target length was derived from the report’s demand assumptions; matching the length does not validate those assumptions nor justify the investment when actual utilisation is only ~50 % (or lower on many lines). The conclusion that the infrastructure build‑out was sensible is not supported by the data presented. [confidence: high]

## Mistral mistral-small-latest

[Mistral API error 429: {"object":"error","message":"Rate limit exceeded","type":"rate_limited","param":null,"code":"1300","raw_status_code":429}]

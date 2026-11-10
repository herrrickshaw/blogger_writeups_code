# Consolidation and pruning list (draft for approval), 10 Nov 2026

Why: Google has crawled most of the blog and chosen not to index it ("Crawled/Discovered - currently not indexed";
see FINDINGS-2026-11-10.md). Fewer, stronger, less repetitive pages is the fix within our control. Impressions by page
were not used: only about 20 pages are indexed, so almost every post has zero.

Actions: MERGE = fold into the named post (it absorbs the unique content; the other goes back to draft).
HUB = fold into a new hub post. DRAFT = revert to draft (unpublish; nothing is deleted). KEEP = no change.
Reverting to draft removes the URL; old links then 404, which is fine for pages Google never indexed.
Nothing below happens without your approval.

## Phase 1: dead ends and duplicates (smallest, safest)

### 1a. How-to guides that send readers to private repos (DRAFT, or make the repo public)
| Post | Repo (private) |
|---|---|
| how-to-use-bazaartalks-multi-market | BazaarTalks |
| how-to-use-bazartalkspy2cplus-c-port-of | Bazartalks_Py2Cplus |
| how-to-use-global-stock-screener-rule | global-stock-screener, global-market-scanners |
| how-to-use-marketscreenerrag-backtested | market_screener_rag |
| how-to-use-news-tracker-score-headlines | global-market-data, global-market-scanners |
| how-to-use-piotroski-liquidity-research | piotroski-liquidity-research |
| how-to-use-pricepredictionbacktest | price_prediction_backtest |
| how-to-use-stock-portfolio-evaluator | stock-portfolio-evaluator |
| how-to-use-us-stock-picks-multi-screen | us-stock-picks |
| us-stock-picks-multi-screen-quant (snapshot of 24 Jul, 3.5 months stale) | us-stock-picks |
The three held drafts (claude-stock-tools, global-stock-screener-public, europe-stock-screener) are in the same position.

### 1b. Analysis pairs that cover the same ground (MERGE)
| Merge this | into | Similarity |
|---|---|---|
| rajya-sabha-question-registry-scheme | lok-sabha-question-registry-1843-scheme, which becomes one "Parliament Question Registry, both Houses" | 0.66 |
| below-250-is-where-real-junk-lives | 050-is-its-own-category-diving-into (one cheap-stocks post) | 0.65 |
| beyond-pump-what-upi-fee-would-cost | upi-fees-are-now-legal-petrol-pumps (one UPI-fee post) | 0.48 |
| india-forest-wildlife-crz-clearances and india-environmental-clearances-state | india-ec-approval-funnel-parivesh-20 (one PARIVESH post; do it with the pending PARIVESH refresh) | 0.48 |
| chemical-import-substitution-quarterly and chemical-import-substitution-analysis | top-15-chemicals-for-import (the analysis); keep the two 827-code data-table posts as one: chemical-import-substitution-hsn-8-registry absorbs ...full-hsn-8_01082878313 | 0.42-0.50 |
| cpi-wpi-trends-mospi-bulletin and fourteen-years-of-indian-wholesale | indias-wholesale-prices-next-to (one WPI post); the CPI heatmap stays (monthly) | 0.46-0.61 |
| screen-process-safety-question-in-five | how-to-use-process-safety-design (one process-safety guide with the demo) | 0.60 |
| how-to-use-cbsepaperpatterns-check | do-cbse-past-papers-actually-help (add a short "use the tool" section) | 0.59 |
| fy2025-26-sample-report-india-trade (a product-style sample report) | DRAFT | - |
| tech-for-business-so-2019-tech-as (2020, off-topic for the current blog) | DRAFT, or KEEP if it matters to you | - |

KEEP as related but distinct (link them to each other instead):
- the gas-pipeline map and right-of-user;
- lysine and methionine;
- wind fleet and Tamil Nadu wind;
- the four mandi/crop posts;
- AI Tracker Editions 03 and 04;
- the two battery-storage posts;
- the two rural-wage posts;
- the rupee and BRICS posts.

## Phase 2: fold the 67 templated how-to guides into about 8 hubs
The how-tos are the most self-similar group on the site (14 of the 20 most similar post pairs). Each hub is one
substantial post: what each tool does, when to use which, one worked example, and the repo links. Repo detail
stays on GitHub.

| Hub post | Folds in |
|---|---|
| Open-source process-design kits (biofuels, gas, refining) | ethanol-design-opensource, lignocellulosic-ethanol, cbg-design-opensource, coal-to-urea, biomass-to-syngas, refinery-design-opensource, lng-design-opensource, saf-monitoring-system |
| Battery, hydrogen and control simulators | bms-battery-management, ev-battery-management-sim, hydrogen-electrolyser + drafts cell-guardian, bionic-limb-control |
| India trade-data toolkit | india-trade-tracker, india-trade-data-analysis, india-trade-export-analysis, india-commodity-trade, india-trade-sector-policy, chemicalimportsubstitution, india-forex-analysis, mospi-dataset-analysis |
| India fuel-retail and energy-data tools | fuel-retail-outlets, cng-cgd-retail-outlet, india-omc-fuel-fleet-model, ppac-ready-reckoner-data, vehiclefuelmileage, uco-ulo-tracking, discom-debt-and-revenue |
| India governance and registry tools | digital-twin-for-ipa, gazette-translated-indexed, lok-rajya-sabha-qa, india-ec-subsector-analysis, india-quality-regulation, focus-sector-investor-map + drafts iem-tracker, reg-intel |
| India agri and food-data tools | agri-commodity-tracker, fci-warehouse-mspvsmsv + draft india-mandi-arrivals |
| Market-data tools (public repos only) | colab-market-fundamentals, global-ticker-universe, market-correlation-matrices, five-open-toolkits-finance + drafts market-brief-base, global-market-kdb, event-driven-stock-analysis |
| Developer and AI tooling | blog-consistency-check, cachememorycleaner, claude-lmstudio-router, claude-provenance, data-source-mining, delivery-playbook, ltm-warehouse-tests, memory-map-optimizer, repo-data-dedup, research-design-system, transmission-client, ship2shorerag + drafts llm-extract-citation-fix, prompt-efficiency-tracker-public |
| Health and medical prototypes | patient-history-tracking + draft capsule-endoscopy-cv |

KEEP standalone (distinctive): how-to-use-process-safety-design (absorbs the screening post),
eu-ets-compliance-platform, kalkiflooding, amazon-product-selector, agentic-insurance-agent, cricket-data-analysis.
The remaining drafts (manga2anime, india-election-analysis, company-database-public, lng-cost) either join a hub
(lng-cost goes to process-design) or stay unpublished until the site is being indexed again.

Net effect: about 507 live posts become about 440, and the 67 how-tos become about 15 pages.

## Phase 3: pace (no list needed)
2-3 new posts a week; refreshes in batches of about 20 a week; re-run tools/gsc_index.py weekly.

# Table audit, 26 October 2026

Every table in all 376 posts in `posts/` (1,085 tables) was rendered in headless Chromium at 375px (phone) and 1024px (desktop), inside the theme skin with gs-table-template-v1 and gs-table-guard-v1. Scripts and raw output: `out/research/table-audit/` (`audit.js`, `tables-2026-10-26.jsonl`). Table numbers count from 0 in page order.

## Summary

- **Ads inside tables:** none can stay there. The guard script moves any Auto-ads container that lands in a table to just after it; unfilled containers collapse.
- **Page width:** no table widens any page any more. 13 posts still scroll sideways on a phone; hiding every table changes none of them, so the cause is elsewhere (a 1,200px chart canvas, code blocks, long `data/...` links, wide cards). With the template, 4 posts that used to scroll sideways no longer do (chemical-import-substitution-quarterly, discom-debt-relief-token-charge, india-forest-wildlife-crz-clearances, the-grain-value-loop-integrated-rice), and none got worse.
- **Template fix during the audit:** the first version made two posts wider on phones (grain-value-loop 149→256px, forest-clearances 169→205px), because a 560px-minimum table inside a flex card stretched the card. Table wrappers now use `contain:inline-size`, so the table scrolls inside its box; both posts are now 0px.
- **All tables are wrapped** (0 unwrapped); 554 tables in 248 posts scroll sideways inside their box on a phone, which is the intended behaviour for tables with 4 or more columns.
- **No structural faults:** no nested tables, no stray non-cell elements in rows.

| Check | Tables | Posts |
|---|---|---|
| Scrolls sideways even at 1024px | 8 | 7 |
| 7 or more columns | 65 | 41 |
| A column narrower than 60px at 375px | 32 | 23 |
| A row taller than 450px at 375px | 14 | 11 |
| A cell longer than 400 characters | 9 | 8 |
| No header row | 3 | 3 |
| Rows with unequal cell counts | 2 | 1 |
| More than 25% empty cells | 2 | 2 |

## Scrolls sideways even on desktop — 8 tables in 7 posts

Too many columns for any screen. Candidates for splitting, transposing, or moving to a downloadable CSV with a shorter summary table.

| Post | Table # | Columns × rows | Narrowest column at 375px | Starts with |
|---|---|---|---|---|
| amruts-197-lakh-crore-urban-portfolio | 0 | 11 × 37 | 88px | State/UTTotal projectsTotal cost (₹cr)Water Supply (n)Water  |
| india-has-27400-km-of-gas-pipeline | 1 | 9 × 16 | 88px | LineEntityAuthorised, kmOperatingUnder constructionPipe lowe |
| indias-79-lakh-crore-rural-water | 0 | 8 × 34 | 88px | State/UTTotal schemesCompletedOngoingNot yet startedUpcoming |
| indias-shrimp-exports-did-not-collapse | 2 | 9 × 2 | 88px | YearFY17-18$ mnFY18-19$ mnFY19-20$ mnFY20-21$ mnFY22-23$ mnF |
| inflation-trends-globally-what-five | 3 | 10 × 12 | 88px | Economy2019202020212022202320244-yr total2025 (national)2026 |
| where-indias-fdi-actually-lands-state | 1 | 27 × 19 | 35px | State / UT Q3 FY19-20 Q2 FY20-21 Q3 FY20-21 Q4 FY20-21 Q1 FY |
| where-indias-fdi-actually-lands-state | 3 | 27 × 9 | 34px | District Q3 FY19-20 Q2 FY20-21 Q3 FY20-21 Q4 FY20-21 Q1 FY21 |
| you-cannot-substitute-crude-oil-or-gold | 4 | 10 × 5 | 88px | ChapterFY18-19$ mnFY19-20$ mnFY20-21$ mnFY21-22$ mnFY22-23$  |

## No header row — 3 tables in 3 posts

The first row is data, so the template has no header to style and screen readers have no column names.

| Post | Table # | Columns × rows | Narrowest column at 375px | Starts with |
|---|---|---|---|---|
| chemical-import-substitution-analysis | 1 | 3 × 6 | 68px | Ethylene (HSN 29011100)[retracted — see correction notice ab |
| chemical-import-substitution-quarterly | 3 | 2 × 5 | 128px | BPCL AP 🟡 WATCH: EC filed; final grant expected by end-Septe |
| discom-debt-relief-token-charge | 0 | 2 × 7 | 81px | Connections covered18.0 crore |

## Ragged rows — 2 tables in 1 posts

Rows have different cell counts, so columns misalign.

| Post | Table # | Columns × rows | Narrowest column at 375px | Starts with |
|---|---|---|---|---|
| indias-old-factory-index-said | 0 | 7 × 7 | 88px | Growth over previous year (%)2023-242024-252025-26 |
| indias-old-factory-index-said | 1 | 7 × 8 | 88px | Use-based group, growth (%)2023-242024-252025-26 |

## Mostly empty — 2 tables in 2 posts

More than a quarter of the cells are blank.

| Post | Table # | Columns × rows | Narrowest column at 375px | Starts with |
|---|---|---|---|---|
| the-most-discussed-schemes-in | 2 | 7 × 11 | 88px | SchemeFirst announcedPIB annsLS QsRS Qs★Last question |
| thirty-one-years-of-asking-parliament | 0 | 3 × 33 | 88px | YearQuestions |

## Very tall rows on phones — 14 tables in 11 posts

Long prose in narrow cells; better as a list or a 2-column table.

| Post | Table # | Columns × rows | Narrowest column at 375px | Starts with |
|---|---|---|---|---|
| blending-on-budget-energy-density-and | 1 | 3 × 5 | 103px | PairIndian standard (BIS)International standard |
| fourteen-states-reimburse-investors | 0 | 6 × 15 | 88px | StateCurrent policySGST shareDurationBasisCap |
| green-gold-what-spirulina-actually-is | 0 | 3 × 5 | 93px | ApplicationStatusWhat the evidence actually shows |
| green-gold-what-spirulina-actually-is | 1 | 3 × 6 | 94px | ApplicationStatusWhat the evidence actually shows |
| indias-coffee-crop-hasnt-grown-in | 2 | 3 × 7 | 98px | InitiativeWhat it targetsMechanism |
| indias-renewable-energy-certificates | 2 | 6 × 9 | 88px | SchemeRegulatorOne certificate representsObligated buyersTra |
| nine-ministries-one-list-every-company | 9 | 2 × 4 | 130px | GroupCompanies |
| nine-ministries-one-list-every-company | 14 | 3 × 3 | 122px | ListDrone manufacturersComponent manufacturers |
| securitising-deficit-what-it-would | 6 | 3 × 7 | 108px | InstrumentWhat was doneChannel it works through |
| the-helper-motor-trick-that-already | 1 | 3 × 3 | 112px | ProjectConfigurationWhat was done |
| top-15-chemicals-for-import | 0 | 6 × 16 | 88px | Rank Chemical (HSN) Imports FY26 ($ Mn) Capex (₹ cr) Rationa |
| us-stock-picks-multi-screen-quant | 0 | 11 × 16 | 88px | #TickerSleeveScoreScreens SectorPrice ($)Day (%)FQThesis |
| where-indias-factories-actually-get | 0 | 12 × 16 | 88px | #State20212022202320242025 (to Dec)5-yr totalShare %A→B conv |
| where-indias-factories-actually-get | 1 | 6 × 13 | 88px | #Sector5-yr Rs crShare %2025 aloneRead |

## Very long cells — 9 tables in 8 posts

A cell over 400 characters; usually prose that belongs outside the table.

| Post | Table # | Columns × rows | Narrowest column at 375px | Starts with |
|---|---|---|---|---|
| blending-on-budget-energy-density-and | 1 | 3 × 5 | 103px | PairIndian standard (BIS)International standard |
| chemical-import-substitution-full-hsn-8_01082878313 | 2 | 9 × 114 | 88px | HS-8CommodityFY26 Imp $MDeficit $MValue Gr %Volume Gr %Price |
| discom-debt-relief-token-charge | 3 | 2 × 5 | 138px | FindingDetail |
| green-gold-what-spirulina-actually-is | 0 | 3 × 5 | 93px | ApplicationStatusWhat the evidence actually shows |
| green-gold-what-spirulina-actually-is | 1 | 3 × 6 | 94px | ApplicationStatusWhat the evidence actually shows |
| nine-ministries-one-list-every-company | 9 | 2 × 4 | 130px | GroupCompanies |
| securitising-deficit-what-it-would | 6 | 3 × 7 | 108px | InstrumentWhat was doneChannel it works through |
| where-indias-factories-actually-get | 1 | 6 × 13 | 88px | #Sector5-yr Rs crShare %2025 aloneRead |
| where-worlds-oil-sits-when-it-isnt | 1 | 4 × 7 | 107px | PipelineRouteStatus, mid-Aug 2026Scale |

## Squeezed columns on phones — 32 tables in 23 posts

A column under 60px wide at 375px (tables with 3 columns or fewer do not get the 560px scroll minimum).

| Post | Table # | Columns × rows | Narrowest column at 375px | Starts with |
|---|---|---|---|---|
| e20-doesnt-cut-tailpipe-co2-by-30-run | 1 | 3 × 8 | 55px | BlendCO2 per litre burned, kgPer-litre CO2 cut vs E0, % |
| ethanol-freed-up-refinery-capacity-for | 2 | 4 × 4 | 51px | RefineryCurrent capacityExpansionTarget |
| five-years-and-25000-crore-later-china | 0 | 3 × 6 | 58px | Three series, three scopes — not the same number |
| five-years-and-25000-crore-later-china | 2 | 5 × 4 | 54px | None of the three parks has begun commercial API production, |
| five-years-and-25000-crore-later-china | 4 | 3 × 7 | 50px | CategoryHS linesChina value (US$mn, approx.) |
| five-years-and-25000-crore-later-china | 6 | 3 × 11 | 37px | #RecommendationEvidence |
| how-to-use-agentic-insurance-agent-open | 0 | 3 × 6 | 52px | RequirementWhyHow to get it |
| how-to-use-cachememorycleaner-free-mac | 2 | 2 × 4 | 57px | MethodHow it works |
| how-to-use-news-tracker-score-headlines | 2 | 2 × 5 | 57px | MethodHow it works |
| india-has-132-compressed-biogas-plants | 1 | 4 × 5 | 59px | UnitCountPlants per unit, at 217 commissionedPlants per unit |
| india-is-piping-jet-fuel-to-five-new | 0 | 5 × 7 | 48px | AirportOperator & routeLengthCapacityStatus |
| india-rewrote-its-entire-maritime-legal | 0 | 4 × 5 | 59px | Old law (age)New ActWhat changedAssent |
| indias-ethanol-surplus-buys-about-five | 2 | 3 × 6 | 59px | MeasureWhat it givesStatus |
| indias-ethanol-surplus-buys-about-five | 5 | 3 × 7 | 46px | BlendEthanol for petrol, 2025-26 (crore litres)Ethanol for p |
| indias-ethanol-surplus-buys-about-five | 14 | 6 × 4 | 57px | Scenario, 2034-35Extra crop land (lakh ha)Urea (Mt)DAP (Mt)M |
| indias-ev-localisation-deadline-just | 1 | 3 × 7 | 51px | DateVehicleWhat it did |
| indias-lng-trucks-grew-75-in-2025-about | 0 | 3 × 6 | 49px | Metric20242025 |
| indias-oil-fields-are-running-down | 0 | 5 × 9 | 49px | FamilyTechniqueMechanismGlobal statusIndia status (as found) |
| mapping-indias-other-pipelines-every | 1 | 4 × 8 | 44px | RouteOperatorLengthCapacity / status |
| one-gallon-five-numbers-how-gcam-fits | 1 | 5 × 4 | 46px | SystemJurisdictionUnitMechanismUnderlying LCA tool |
| pngrbs-own-committee-found-pipelines | 0 | 5 × 17 | 47px | PipelineOwnerLength (km)Capacity (MMT)Utilisation, FY26 |
| refiners-won-exemption-fight-biofuels | 0 | 5 × 9 | 55px | DecidedCourtCaseIssueWinner |
| right-of-user-what-indias-pipeline | 1 | 6 × 55 | 52px | State/UTPipeline projectFluidOperatorLocation detail foundNo |
| rin-red-and-cbio-what-indias-ethanol | 0 | 4 × 4 | 59px | SystemWhat the credit certifiesHow it's pricedWho bears the  |
| the-ministry-of-power-published-two | 0 | 7 × 3 | 43px | ReleaseDateWhoBaseline citedFY25 figureUtilities countedvs 1 |
| the-two-biggest-parties-in-parliament | 1 | 4 × 11 | 51px | PartySignature ministryQuestionsLift |
| the-two-biggest-parties-in-parliament | 3 | 5 × 37 | 56px | Party▾ Signature ministry▾ Questions there▾ Party total▾ Lif |
| the-two-biggest-parties-in-parliament | 5 | 5 × 784 | 51px | Party▾ Member▾ House▾ State / UT▾ Constituency▾ |
| under-corsias-own-numbers-corn-ethanol | 0 | 3 × 7 | 44px | DateInstrumentWhat it did |
| where-indias-fdi-actually-lands-state | 1 | 27 × 19 | 35px | State / UT Q3 FY19-20 Q2 FY20-21 Q3 FY20-21 Q4 FY20-21 Q1 FY |
| where-indias-fdi-actually-lands-state | 2 | 6 × 21 | 51px | RankDistrictState₹ crore$ millionQuarters present (of 24) |
| where-indias-fdi-actually-lands-state | 3 | 27 × 9 | 34px | District Q3 FY19-20 Q2 FY20-21 Q3 FY20-21 Q4 FY20-21 Q1 FY21 |

## 7 or more columns — 65 tables in 41 posts

Readable on desktop, scroll on phones. Listed for reference; no action needed unless also listed above.

| Post | Table # | Columns × rows | Narrowest column at 375px | Starts with |
|---|---|---|---|---|
| 574-gw-and-counting-indias-wind-fleet | 0 | 7 × 11 | 88px | StateCumulative installed, June 2026, MWCumulative installed |
| a-slice-of-apple-costs-about-1700-slice | 5 | 7 × 6 | 88px | Price band, ₹Stocks with a computed betaStocks in bandComple |
| a-slice-of-apple-costs-about-1700-slice | 6 | 7 × 6 | 88px | Price band, ₹Median 3-month return, %Median 6-month return,  |
| amruts-197-lakh-crore-urban-portfolio | 0 | 11 × 37 | 88px | State/UTTotal projectsTotal cost (₹cr)Water Supply (n)Water  |
| chemical-import-substitution-full-hsn-8_01082878313 | 0 | 9 × 306 | 88px | HS-8CommodityFY26 Imp $MDeficit $MValue Gr %Volume Gr %Price |
| chemical-import-substitution-full-hsn-8_01082878313 | 1 | 9 × 202 | 88px | HS-8CommodityFY26 Imp $MDeficit $MValue Gr %Volume Gr %Price |
| chemical-import-substitution-full-hsn-8_01082878313 | 2 | 9 × 114 | 88px | HS-8CommodityFY26 Imp $MDeficit $MValue Gr %Volume Gr %Price |
| chemical-import-substitution-full-hsn-8_01082878313 | 3 | 9 × 21 | 88px | HS-8CommodityFY26 Imp $MDeficit $MValue Gr %Volume Gr %Price |
| chemical-import-substitution-full-hsn-8_01082878313 | 4 | 9 × 78 | 88px | HS-8CommodityFY26 Imp $MDeficit $MValue Gr %Volume Gr %Price |
| chemical-import-substitution-full-hsn-8_01082878313 | 5 | 9 × 60 | 88px | HS-8CommodityFY26 Imp $MDeficit $MValue Gr %Volume Gr %Price |
| chemical-import-substitution-full-hsn-8_01082878313 | 6 | 9 × 25 | 88px | HS-8CommodityFY26 Imp $MDeficit $MValue Gr %Volume Gr %Price |
| chemical-import-substitution-full-hsn-8_01082878313 | 7 | 9 × 29 | 88px | HS-8CommodityFY26 Imp $MDeficit $MValue Gr %Volume Gr %Price |
| chemical-import-substitution-quarterly | 0 | 7 × 4 | 88px | Chemical (HSN) Initiation Date Expected Decision Expected Du |
| cpi-wpi-trends-mospi-bulletin | 0 | 19 × 15 | 88px | StateJan 25Feb 25Mar 25Apr 25May 25Jun 25Jul 25Aug 25Sep 25O |
| cpi-wpi-trends-mospi-bulletin | 1 | 17 × 2 | 88px | MonthJan 25Feb 25Mar 25Apr 25May 25Jun 25Jul 25Aug 25Sep 25O |
| discom-debt-relief-token-charge | 2 | 10 × 10 | 88px | ₹/mo ↓ · eff →50%60%70%75%80%85%90%95%100% |
| do-cheap-stocks-stay-cheap-price-band | 1 | 7 × 5 | 88px | ClusterCharacterStocksMedian price, ₹Median return, % p.a.Me |
| do-cheap-stocks-stay-cheap-price-band | 2 | 7 × 5 | 88px | ClusterCharacterStocksMedian price, ₹Median return, % p.a.Me |
| five-year-synthesis-trade-currency | 0 | 9 × 6 | 88px | Fiscal YearExports (US$M)Imports (US$M)Rupee (FY avg)Goods b |
| fourteen-years-of-indian-wholesale | 1 | 10 × 9 | 88px | Series201220142016201820202022202420262012→2026, % |
| fourteen-years-of-indian-wholesale | 2 | 7 × 9 | 88px | SeriesActual pace, % a yearRule of 72, years to doubleDoubli |
| from-fuel-to-fibre-indias-textile | 4 | 7 × 14 | 88px | SegmentFY25 Export (USD M)FY25 Import (USD M)FY26 Export (US |
| fuel-and-bottle-two-taxes-states-never | 0 | 8 × 29 | 88px | StateSGST, % GSDPFuel VAT, % GSDPLiquor excise, % GSDPStamp  |
| hsn-wise-historical-importexport-trends | 0 | 12 × 13 | 88px | HSCommodityFY2018-19FY2019-20FY2020-21FY2021-22FY2022-23FY20 |
| hsn-wise-historical-importexport-trends | 2 | 12 × 13 | 88px | HSCommodityFY2018-19FY2019-20FY2020-21FY2021-22FY2022-23FY20 |
| iem-conversion-historical-performance | 0 | 7 × 10 | 88px | Calendar YearPart A Filed (Rs cr)Part A (IEMs)Part B Impleme |
| imported-fertiliser-fuel-prices-diesel | 0 | 8 × 16 | 88px | Year (Apr)WPI HSDWPI UreaWPI DAPWPI HeadlineCPI HeadlineCPI  |
| india-has-27400-km-of-gas-pipeline | 1 | 9 × 16 | 88px | LineEntityAuthorised, kmOperatingUnder constructionPipe lowe |
| india-mineral-oil-hsn-ch27-trade | 20 | 7 × 1 | 88px | DirectionIdeaExp $MImp $MNet $MGrw%Verdict |
| indias-79-lakh-crore-rural-water | 0 | 8 × 34 | 88px | State/UTTotal schemesCompletedOngoingNot yet startedUpcoming |
| indias-8-digit-trade-book-searchable | 0 | 7 × 1 | 88px | HS codeCommodity FY26 $mn8-yr change SeriesUnit valueOther s |
| indias-biggest-mandi-crops-have | 0 | 7 × 24 | 88px | All-India ranking: 23 crops by mandi arrivals, with price vo |
| indias-carbon-credit-market-domestic | 1 | 7 × 8 | 88px | Sector / sub-sectorPlantStateRegistration IDBaseline GEI 202 |
| indias-cheapest-lng-capacity-is-extra | 0 | 8 × 10 | 88px | TerminalOperatorSinceCapacity, MMTPA (PPAC, 1 Jun 2026)Utili |
| indias-cheapest-lng-capacity-is-extra | 3 | 7 × 5 | 88px | Capital cost recovered per MMBtu, ₹Capex, ₹ crore (5 MMTPA)a |
| indias-factory-intentions-20012024-how | 1 | 7 × 25 | 88px | Filed inPart A memorandaPart B cites the numberPart B, name  |
| indias-factory-intentions-20012024-how_0101046393 | 1 | 7 × 25 | 88px | Filed inPart A memorandaPart B cites the numberPart B, name  |
| indias-old-factory-index-said | 0 | 7 × 7 | 88px | Growth over previous year (%)2023-242024-252025-26 |
| indias-old-factory-index-said | 1 | 7 × 8 | 88px | Use-based group, growth (%)2023-242024-252025-26 |
| indias-shrimp-exports-did-not-collapse | 2 | 9 × 2 | 88px | YearFY17-18$ mnFY18-19$ mnFY19-20$ mnFY20-21$ mnFY22-23$ mnF |
| indias-wholesale-prices-next-to | 0 | 8 × 8 | 88px | YearIndia WPIUS PPIJapan PPIKorea PPIChina PPIBrazil IPPEuro |
| indias-wholesale-prices-next-to | 1 | 8 × 11 | 88px | Economy2019202020212022202320242025 |
| indias-wholesale-prices-next-to | 3 | 7 × 7 | 88px | MonthUS PPIKorea PPIIndia WPIJapan PPIEuro area PPIBrazil IP |
| inflation-trends-globally-what-five | 1 | 8 × 17 | 88px | Economy2019202020212022202320242025 |
| inflation-trends-globally-what-five | 3 | 10 × 12 | 88px | Economy2019202020212022202320244-yr total2025 (national)2026 |
| inflation-trends-globally-what-five | 4 | 7 × 7 | 88px | MonthUS PPIKorea PPIIndia WPIJapan PPIEuro area PPIBrazil IP |
| methionine-not-lysine-is-indias-biggest | 0 | 7 × 9 | 88px | HS-8Amino acidHow it is madeFY26 imports, $ mnDeficit, $ mnV |
| real-gdp-growth-india-fy2012-13-to | 0 | 7 × 15 | 88px | Fiscal YearFirst Advance (real)Latest (real)Δ (pp)Latest rev |
| state-by-state-who-actually-earns-from | 3 | 7 × 7 | 88px | Illustrative dedicated ethanol SGST, ₹ crore/year, at 1–5% r |
| the-currency-rupee-trends-piece-left | 0 | 8 × 7 | 88px | PairRate, 14 Aug 20261-year3-year5-year10-year2026 YTDAnn. v |
| the-ministry-of-power-published-two | 0 | 7 × 3 | 43px | ReleaseDateWhoBaseline citedFY25 figureUtilities countedvs 1 |
| the-most-discussed-schemes-in | 0 | 7 × 52 | 88px | SchemeFirst announcedPIB annsLS QsRS Qs★Last question |
| the-most-discussed-schemes-in | 1 | 7 × 36 | 88px | SchemeFirst announcedPIB annsLS QsRS Qs★Last question |
| the-most-discussed-schemes-in | 2 | 7 × 11 | 88px | SchemeFirst announcedPIB annsLS QsRS Qs★Last question |
| us-stock-picks-multi-screen-quant | 0 | 11 × 16 | 88px | #TickerSleeveScoreScreens SectorPrice ($)Day (%)FQThesis |
| us-stock-picks-multi-screen-quant | 2 | 7 × 8 | 88px | SymbolSectorClose ($)PiotroskiROIC %Above 200DMAML direction |
| vehicles-out-motors-in-indias-chapter | 0 | 7 × 9 | 88px | FYCh.87 exports ($M)Ch.87 imports ($M)Ch.87 netCh.85 exports |
| where-indias-factories-actually-get | 0 | 12 × 16 | 88px | #State20212022202320242025 (to Dec)5-yr totalShare %A→B conv |
| where-indias-factories-actually-get | 2 | 8 × 40 | 88px | IndustryPart A filedPart B impl.Conv. % (by count)Part B Rs  |
| where-indias-factories-actually-get | 3 | 8 × 37 | 88px | StateFiled A (n)Impl. B (n)Pending (n)Filed A Rs crImpl. B R |
| where-indias-fdi-actually-lands-state | 1 | 27 × 19 | 35px | State / UT Q3 FY19-20 Q2 FY20-21 Q3 FY20-21 Q4 FY20-21 Q1 FY |
| where-indias-fdi-actually-lands-state | 3 | 27 × 9 | 34px | District Q3 FY19-20 Q2 FY20-21 Q3 FY20-21 Q4 FY20-21 Q1 FY21 |
| where-rupee-actually-stands-ten-years | 0 | 7 × 6 | 88px | PairRate, 14 Aug 20261-year3-year5-year10-year2026 YTD |
| who-collects-indias-gst-and-who | 0 | 7 × 11 | 88px | State2021-222022-232023-242024-252025-26FY26 YoY, % |
| you-cannot-substitute-crude-oil-or-gold | 4 | 10 × 5 | 88px | ChapterFY18-19$ mnFY19-20$ mnFY20-21$ mnFY21-22$ mnFY22-23$  |

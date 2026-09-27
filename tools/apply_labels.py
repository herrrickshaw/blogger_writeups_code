#!/usr/bin/env python3
"""Assign topic labels to every live post, so Blogger's label pages become hubs.

    python3 tools/apply_labels.py --plan          # show the assignment, write nothing
    python3 tools/apply_labels.py --apply         # write, skipping posts already labelled
    python3 tools/apply_labels.py --apply --limit 30

WHY
    Blogger generates a crawlable archive page per label (/search/label/<name>).
    This blog had ZERO labels on 99 posts, so twelve coherent topic clusters
    existed in the writing and nowhere in the navigation: no hub pages, and no
    internal links between related posts other than one hand-maintained index.

HOW THE ASSIGNMENT IS MADE
    Scored on H1/H2/H3 text only, not the body. Headings state what a piece is
    about; bodies on this blog contain long HSN tables whose repeated cell text
    swamps any term count (one boilerplate sentence appears 2,648 times across
    four posts). The H1 is weighted x3.

    A post takes every cluster scoring at least a third of its best score, up to
    three labels. Single-label posts are the common case; the multi-label ones
    are genuinely cross-cutting (ethanol is both Energy and Agriculture).

SAFETY
    - Sends `published` back explicitly, so a label write cannot re-date a post.
    - Skips any post that already has labels, so it is safe to re-run after
      hitting the daily write ceiling. Resume by running it again tomorrow.
    - --plan changes nothing and is the default way to review the taxonomy.
"""
import argparse
import collections
import glob
import html
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import blogger_api as B  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# Label -> heading keywords. Label names are reader-facing: they become the
# visible hub titles and the URL segment, so they are short and unambiguous.
TAXONOMY = {
    "Import Substitution": ["import substitution", "import-substitution", "hsn",
                            "localisation", "domestic capacity", "registry"],
    "Chemicals":           ["chemical", "petrochem", "dyes", "pigment",
                            "speciality", "specialty", "polymer", "acid"],
    "Energy & Fuels":      ["ethanol", "cbg", "biogas", "blending", "biofuel",
                            "crude", "petroleum", "refinery", "diesel", "petrol",
                            "oil field", "retail outlet", "petrol pump"],
    "Gas & LNG":           ["lng", "natural gas", "cgd", "pngrb", "regas",
                            "city gas", "pipeline", "gail"],
    "Agriculture & Fertilisers": ["fertiliser", "urea", "agri", "grain", "farm",
                                  "annadata", "kisan", "crop", "sugar", "paddy",
                                  " fci ", "storage capacity", "polyhouse",
                                  "greenhouse", "cocoa"],
    "Textiles":            ["textile", "apparel", "fibre", "charkha", "cotton", "mmf"],
    "Prices & Inflation":  ["wpi", "cpi", "inflation", "wholesale price",
                            "consumer price", "price index", "deflator"],
    "Climate & Carbon":    ["carbon", "ccts", "cbam", "green hydrogen",
                            "green credit", "emission", "climate", "esg"],
    "Mobility & EV":       ["electric vehicle", " ev ", "vehicle", "mobility",
                            "ev battery", "vehicle battery", "charging", "automobile"],
    "Trade & Tariffs":     ["export", "import", "tariff", "trade balance",
                            "trade deficit", "customs", "fta", "wto",
                            "supply chain"],
    "Markets & Finance":   ["bond", "equity", "portfolio", "capital gain",
                            "yield", "securitis", "rupee", "currency", "fdi",
                            "green bond", "green debt", "capital market"],
    # "pli" as a bare 3-letter fragment matched inside ordinary words --
    # "split", "supplies", "multiply" -- and mislabelled unrelated posts
    # (caught on the-503020-rule-is-elizabeth-warrens.html, via "wants
    # split"). Space-bound / phrase-bound instead.
    "Industrial Policy":   [" pli ", "pli scheme", "production linked incentive",
                            "production-linked incentive", "scheme", "incentive",
                            "subsidy", "policy", "cluster", "investment promotion",
                            "sabha", " iem "],
    "Environment & Clearances": ["environmental clearance", "parivesh", " ec ",
                                 "crz", "coastal regulation zone", "forest clearance",
                                 "wildlife clearance", "forest, wildlife"],
    "Macroeconomics & Monetary Policy": ["monetary policy", "repo rate",
                                         "central bank", "real gdp", "gdp growth",
                                         " rbi "],
    "Healthcare":          ["abha", "health account", "health id", "digital health",
                            "ayushman", "pm-jay", "pmjay", "health insurance",
                            "hospital", "healthcare", "out-of-pocket", "oope",
                            "health record", "health cover"],
}


# Utility pages are not topics. Left to the keyword scorer, "About the Author"
# scores Industrial Policy on the phrase "investment promotion" in the job
# title, and the index page scores whatever its longest section list mentions.
# Both would then appear in topic hubs alongside actual analysis.
OVERRIDE = {
    "about-author":                    [],
    "article-index-start-here":        [],
    # utility page, not an article -- was missing from this list, so it was
    # getting auto-scored against the topic taxonomy like a real post
    "the-masala-deutsch-shop-books-things": [],
    "ai-high-demand-launch-tracker":   ["AI Tracker"],
    "cgd-geographical-areas-district": ["Gas & LNG", "Industrial Policy"],
    "cold-chain-fuel-outlet-integrated-map": ["Gas & LNG", "Agriculture & Fertilisers"],
    # H1 is the bare title "Quarterly Reportage" with no descriptive subtitle
    # in a class headings() recognises -- the real subject only appears in
    # the eyebrow's plain text and the body. Self-declares "Industrial
    # policy - PIB register" in its own eyebrow line.
    "quarterly-reportage-4034-scheme": ["Industrial Policy"],
    # No Railways/Infrastructure bucket exists in TAXONOMY; the itemised
    # land-acquisition schedule's "farm"/"village"/"landholder" language
    # scored highest under Agriculture & Fertilisers, mislabelling a
    # freight-rail-capacity post. Industrial Policy is the closest fit
    # among existing labels.
    "a-2223-crore-coal-freight-railway-line": ["Industrial Policy"],
    # Manually labelled at publish time (2026-09-21) rather than run through
    # the full --apply sweep, to avoid touching unrelated posts in the same
    # pass; recorded here so a future sweep doesn't second-guess it.
    "india-wants-isobutanol-in-both-diesel": ["Energy & Fuels", "Ethanol & Biofuels"],
    # No Maritime/Shipping bucket exists in TAXONOMY. MDF is a blended-finance
    # scheme (AIF, equity, hurdle rates, carry) administered as a government
    # scheme -- closest fit is Industrial Policy (scheme/subsidy/investment
    # promotion) plus Markets & Finance (fund structure, AIF). Manually
    # labelled at publish time (2026-09-21) rather than run through --apply,
    # to avoid touching unrelated still-unlabelled posts in the same pass.
    "mopsws-25000-crore-maritime-development": ["Industrial Policy", "Markets & Finance"],
    # Geopolitics/trade-corridor piece (Hormuz blockade, IMEC, India-EU FTA
    # freight costs) with a heavy Hormuz/energy-chokepoint throughline --
    # matches the label pair already used on sibling Hormuz posts
    # (south-africa-lost-its-gulf-fuel-supply). Manually labelled at publish
    # time (2026-09-22) rather than run through --apply.
    "nobody-blockaded-hormuz-to-slow-india": ["Trade & Tariffs", "Energy & Fuels"],
    # Ethanol-feedstock/food-price piece (egg/poultry angle) -- matches the
    # label pair already used on the sibling maize/ethanol-food posts
    # (annadata-to-urjadata-farmer-income-case). Manually labelled at
    # publish time (2026-09-23) rather than run through --apply.
    "the-diesel-truck-isnt-why-your-eggs": ["Agriculture & Fertilisers", "Energy & Fuels"],
    # Two companion pieces from PNGRB's Sept 2026 Action Taken Report on the
    # Annual Plan 2025-26 -- matches the label pairs already used on the
    # sibling PNGRB/CGD posts (indias-gas-pipelines-run-at-half,
    # the-cbg-incentive-stack-every-leg-of). Manually labelled at publish
    # time (2026-09-23) rather than run through --apply.
    "pngrb-graded-its-own-homework-on-2025": ["Gas & LNG", "Industrial Policy"],
    "india-has-132-compressed-biogas-plants": ["Energy & Fuels", "Gas & LNG"],
    # SAF/CORSIA carbon-accounting piece, distilled from a user-supplied
    # technical brief and independently re-verified. Matches the label pair
    # already used on the sibling ATJ/isobutanol post. Manually labelled at
    # publish time (2026-09-23) rather than run through --apply.
    "under-corsias-own-numbers-corn-ethanol": ["Energy & Fuels", "Ethanol & Biofuels"],
    # New post on Kpler/Vortexa-tracked oil and gas flows plus the untracked
    # UCO/ULO commodity streams. Manually labelled at publish time
    # (2026-09-24) rather than run through --apply.
    "kpler-and-vortexa-track-every-barrel": ["Energy & Fuels", "Trade & Tariffs"],
    # New post on IMO's stalled Net-Zero Framework, LNG bunkering growth,
    # marine biodiesel/MASH Makes blending, and India's methanol-bunkering
    # bet. Manually labelled at publish time (2026-09-24) rather than run
    # through --apply.
    "shippings-net-zero-vote-keeps-getting": ["Energy & Fuels", "Ethanol & Biofuels"],
    # New post based on the herrrickshaw/india-quality-regulation GitHub
    # repo, mapping India's ~37 quality-certification bodies across four
    # regulatory layers, plus an independent correction (Scheme-X was
    # repealed 14 Jan 2026, not "due September 2026" as the source repo's
    # fetch still shows). Manually labelled at publish time (2026-09-24)
    # rather than run through --apply.
    "india-doesnt-have-one-quality-regulator": ["Industrial Policy", "Trade & Tariffs"],
    # New post from the lit_review/masaladeutsch commission queue: public
    # irrigation's CWC-sourced cost-recovery collapse (96% in 1975-76 to
    # ~7% average 2000-01/2016-17), cross-linked to Bathla/Kannan/Das (2024,
    # abstract only) and the existing private-irrigation post. Manually
    # labelled at publish time (2026-09-25) rather than run through --apply.
    "indias-irrigation-system-recovered-96": ["Agriculture & Fertilisers", "Industrial Policy"],
    # These two are interactive-map/dashboard embeds, not prose articles --
    # the title lives in an inline-styled div inside class="hero", a
    # structure headings() doesn't parse (and shouldn't be widened to catch,
    # since arbitrary inline-styled divs would be a false-positive magnet
    # elsewhere). Titles state the subject plainly: "82,000 outlets...
    # petrol pumps and CNG supply linkage" / "India Environmental
    # Clearances -- state x sub-sector dashboard" (PARIVESH 2.0 EC register).
    "india-fuel-retail-outlets-82k-geocoded": ["Energy & Fuels", "Gas & LNG"],
    "india-environmental-clearances-state": ["Environment & Clearances"],
    # yet another one-off custom title structure (class="gh-hero" > ".k"
    # kicker + inline-styled div), self-declares "Protected Cultivation .
    # Adaptive Reuse" -- polyhouse/greenhouse economics.
    "the-empty-shed-greenhouse-what-indias": ["Agriculture & Fertilisers"],
    # Live posts the heading scorer left unlabelled (AdSense/navigation pass,
    # Sept 2026): hand-assigned from the article subject so every post sits in
    # at least one topic hub. Suffixed slugs are the surviving copies after the
    # duplicate clean-up.
    "a-million-wine-market-behind-150-wall": ["Trade & Tariffs", "Agriculture & Fertilisers"],
    "brandsafway-and-2017-roll-up-wave-that": ["Markets & Finance", "Industrial Policy"],
    "brazil-pumps-e30-at-every-station": ["Energy & Fuels", "Mobility & EV"],
    "dgh-has-awarded-172-oalp-blocks-and-436_0369361351": ["Energy & Fuels", "Industrial Policy"],
    "indias-oil-psus-say-they-clear-their_01269248608": ["Energy & Fuels", "Industrial Policy"],
    "interpreting-gazette-notification": ["Industrial Policy", "Trade & Tariffs"],
    "one-nation-one-ration-card-doesnt-move": ["Agriculture & Fertilisers", "Energy & Fuels"],
    "right-of-user-what-indias-pipeline": ["Gas & LNG", "Energy & Fuels"],
    "tech-for-business-so-2019-tech-as": ["Markets & Finance"],
    "textbooks-say-project-returns-converge": ["Markets & Finance"],
    "the-1920s-rotor-thats-now-on-22-real": ["Climate & Carbon", "Energy & Fuels"],
    "uk-retail-canopies-at-54m-real-design": ["Energy & Fuels"],
    "where-indias-fdi-actually-lands-state": ["Markets & Finance", "Industrial Policy"],
    # Repeated use of "registry" (Healthcare Professionals Registry, "the
    # national digital registry") matches Import Substitution's bare
    # "registry" keyword, mislabelling a healthcare-interoperability piece
    # as trade policy. Healthcare is the obvious fit; Industrial Policy
    # matches the piece's own eyebrow line.
    "abha-covers-93-crore-patients-its": ["Healthcare", "Industrial Policy"],
    # Repeated use of "registry" (PPV&FR Authority "registry", "the register")
    # matches Import Substitution's bare "registry" keyword, mislabelling a
    # plant-variety-IP piece as trade policy. Agriculture & Fertilisers is the
    # closest existing fit -- no Intellectual Property / Seeds bucket exists.
    "577-of-indias-plant-variety": ["Agriculture & Fertilisers"],
    # Repeated bare "policy" ("irrigation policy", the AERR paper's own title)
    # matches Industrial Policy's bare "policy" keyword, mislabelling an
    # irrigation-ownership/finance piece as industrial scheme coverage.
    "india-irrigates-itself-966-of-its": ["Agriculture & Fertilisers"],
    # No Education bucket exists in TAXONOMY -- this and any future
    # exam/curriculum-data piece are the first posts in that beat.
    "do-cbse-past-papers-actually-help": ["Education"],
    # No Governance/Parliament bucket exists in TAXONOMY. The bare " sabha "
    # keyword under Industrial Policy would otherwise mislabel this as a
    # scheme piece, but it's about party-wise question-asking patterns, not
    # a scheme or incentive -- the first post in a Governance beat.
    "the-two-biggest-parties-in-parliament": ["Governance & Institutions"],
    # Headings are stylistic ("The Reactor Nobody Names", "Talcher: the
    # mission's largest project...") and never hit a bare TAXONOMY keyword,
    # so the scorer would return "-- none --" despite this being squarely a
    # coal-gasification/chemicals piece. Same three labels as its sibling
    # post indias-coal-to-chemicals-menu-ranked-by, which it's explicitly
    # cross-linked against.
    "the-reactor-nobody-names-how-coal": ["Chemicals", "Energy & Fuels", "Industrial Policy"],
    # No Electricity/Power-distribution bucket exists in TAXONOMY, and the
    # Energy & Fuels keywords are all molecule-side (crude, petrol, LNG...),
    # so an AT&C-loss / DISCOM piece scores nothing there. Energy & Fuels is
    # still the right hub for readers; Industrial Policy for the RDSS scheme
    # angle -- matching discom-debt-relief-token-charge, the beat's only
    # other post.
    "the-ministry-of-power-published-two": ["Energy & Fuels", "Industrial Policy"],
    # Same stylistic-heading problem as the reactor post above.
    "indias-oil-fields-are-running-down": ["Energy & Fuels", "Industrial Policy"],
    "pmfby-advertises-51-return-to-farmers": ["Agriculture & Fertilisers", "Industrial Policy"],
    "india-has-tested-its-soil-twice-second": ["Agriculture & Fertilisers"],
}

# SUB-TOPIC REFINEMENT PASS (2026-09-26)
#
# "Agriculture & Fertilisers" had grown to 55 posts -- too broad a bucket for
# a reader looking for one specific thread. Rather than widen TAXONOMY (which
# would re-score every already-labelled post and risk churning labels that
# were fine), six new sub-topic labels were ADDED on top of existing labels
# for the posts that genuinely belong to a finer cluster, via direct
# do_update() calls with each post's current live labels plus the new one(s)
# -- not through --apply, which skips any post that already has labels.
# "Agriculture & Fertilisers" itself was never removed from any post.
#
# The six labels and what each covers:
#   Seeds & Plant Genetics       -- seed-bill legislation, plant-variety/IP registration
#   Irrigation & Water Management -- irrigation ownership, finance, cost-recovery
#                                    (not farm-drinking-water infra, which stays
#                                    under Infrastructure & Investment)
#   Fertilisers & Soil Health    -- urea/DAP dosage, subsidy/import economics,
#                                    bio-fertiliser, Soil Health Card methodology
#   Crop Insurance & Risk        -- PMFBY and the reinsurance/risk-backstop system
#   Livestock & Dairy            -- cattle/dairy/poultry/meat (not fisheries,
#                                    which keeps its own Fisheries & Aquaculture)
#   Grain Procurement & Storage  -- FCI procurement/storage, MSP/MSV mechanics,
#                                    PDS/ONORC grain movement
#
# 25 of the 55 posts got at least one addition (see the slug list this comment
# accompanies in the repo's history for the exact mapping); the remaining 30
# (wine, guar gum, coffee, coco peat, lemon cultivation, HSN trade dashboards,
# PLFS employment-share pieces, etc.) are genuinely general-purpose agriculture/
# trade/price pieces with no finer bucket that fits, and were left alone.
#
# Four borderline calls, left as judgment rather than forced into a bucket:
#   nano-urea-works-as-supplement-and-fails -- nano urea is regulated as a
#     fertiliser (Fertiliser Control Order), not a seed product, despite the
#     "nano" framing inviting a Seeds association -- filed under Fertilisers.
#   indias-animal-protein-export-complex -- roughly a third of the piece is
#     shrimp/fisheries, so it got BOTH Livestock & Dairy AND Fisheries &
#     Aquaculture rather than picking one.
#   the-national-beekeeping-honey-mission -- apiculture isn't cattle/poultry/
#     dairy in the conventional sense, and the post's real content (honey
#     production + adulteration) is already covered by its existing
#     Agriculture & Food Processing label -- left out of Livestock & Dairy.
#   annadata-to-urjadata-farmer-income-case / fourteen-years-of-indian-wholesale
#     -- both touch fertiliser costs in passing (one subsection each) but are
#     fundamentally an ethanol/farmer-income piece and a general WPI roundup
#     respectively -- too thin a match for Fertilisers & Soil Health.
#
# This taxonomy applies only to Blogger's own labels (and therefore this
# repo's meta/*.json). The separately-hosted Lovable "Masala Deutsch Archive"
# mirrors the blog's labels into a static dataset it was fed directly -- it
# needs its own re-sync after a pass like this, not just a snapshot.py run.

# SUB-TOPIC REFINEMENT PASS 2: ENERGY & FUELS (2026-09-26)
#
# Same method as the Agriculture pass above, applied to the blog's single
# biggest bucket: "Energy & Fuels" had grown to 96 posts. Seven new labels
# were ADDED on top of existing labels for posts that cluster into a finer
# sub-topic; "Energy & Fuels" itself was never removed from any post. Checked
# against the full live label set first so none of these duplicate an
# existing topic (Gas & LNG, Ethanol & Biofuels, Climate & Carbon, Mobility &
# EV and Chemicals in particular each already cover an adjacent but distinct
# angle -- see the per-label notes below for exactly where the line was drawn).
#
#   Refining & Petrochemicals -- GRM/crack-spread compression, the refinery-
#     to-petrochemical pivot (FCC lever, naphtha-cracker investment), capex
#     financing for that pivot. The refinery-YIELD side, distinct from
#     Chemicals' import-substitution/HSN-code side of the same industry.
#   Oil & Gas Exploration -- upstream E&P: OALP/HELP rounds, DGH, declining/
#     aging oilfield output, oilfield-services cost indexes and rig-fleet
#     economics. Distinct from downstream refining.
#   Renewable Power & Storage -- solar, wind, grid-scale battery storage,
#     biomass power generation. Power-GENERATION economics, distinct from
#     Climate & Carbon's emissions-accounting focus.
#   Fuel Retail & Pricing -- crude-to-pump price build-up, retail outlet
#     networks (incl. forecourt/canopy design standards), OMC dealer/
#     distributor commission mechanics.
#   Coal & Coal Gasification -- coal-to-syngas reactor technology and the
#     coal-to-chemicals product menu. Distinct from Chemicals' import-
#     substitution framing of the same feedstock.
#   Hydrogen -- green/blue hydrogen production cost (LCOH), refinery
#     hydrogen use, city-gas hydrogen blending pilots, hydrogen inside the
#     SAF mandate.
#   Shipping & Maritime Fuels -- marine fuel-switching: the IMO Net-Zero
#     Framework's repeated delays, wind-assist rotor sails, the EU's ETS/
#     FuelEU/MRV rules forcing ships off conventional bunker fuel, and
#     green-fuel ship-bunkering rules. Not in the original candidate list --
#     proposed because it was a genuine 4-post cluster with no existing home.
#
# 32 of the 96 posts got at least one addition (one, ten-cubic-metres-hour-
# indias-first, got two: Hydrogen and Shipping & Maritime Fuels, since it's
# a hydrogen-bunkering-rulebook piece). The other 64 were left alone.
#
# Borderline calls, left as judgment rather than forced into a bucket:
#   indias-renewable-energy-certificates -- tightly coupled to renewable-
#     capacity growth, but the actual subject is a tradable compliance-
#     certificate market, not generation/storage economics -- left out of
#     Renewable Power & Storage.
#   indias-petrochemical-import-tree-from -- touches refinery-stream origin,
#     but its actual payload (8-digit ITC-HS codes, import-dependence
#     figures) is squarely the import-substitution framing its existing
#     Chemicals label already covers -- left out of Refining &
#     Petrochemicals to avoid functionally duplicating Chemicals.
#   ethanol-blending-omc-books-e20-today-vs -- one section out of seven
#     gestures at the refinery-petrochemical pivot, but the piece as a whole
#     is about ethanol's effect on OMC books/exchequer/export volumes --
#     too thin a match for Refining & Petrochemicals.
#   one-refinery-flipped-nigeria-from -- reads like Refining &
#     Petrochemicals (Dangote refinery), but the actual content is trade-
#     balance/geopolitical with no GRM/crack-spread/petrochemical-yield
#     content -- left under its existing Trade & Tariffs coverage.
#   ethanols-coal-boilers-briquette-gap-and / how-india-actually-plans-to-hit-net
#     -- both mention coal repeatedly (distillery coal boilers / net-zero
#     scenarios' coal curve) but neither is about coal gasification or the
#     coal-to-chemicals menu -- kept out of Coal & Coal Gasification.

# SUB-TOPIC REFINEMENT PASS 3: TRADE & TARIFFS (2026-09-26)
#
# Same method again, applied to "Trade & Tariffs" (69 posts). Four new labels
# ADDED on top of existing labels; "Trade & Tariffs" itself untouched on all
# 69. Checked against the full live label set (by then 55 topics, including
# every sub-topic from the two prior passes) before proposing anything.
#
#   Trade Remedies & Antidumping -- AD/CVD orders, safeguard duties, Section
#     301/232-style tariff actions, WTO dispute mechanisms. The trade-LAW-
#     enforcement side, distinct from blanket geopolitical tariff sagas.
#   Free Trade Agreements -- FTA negotiation/ratification/terms (India-EU,
#     TEPA/EFTA, the post-2021 "new generation" FTA wave). The negotiated-
#     treaty side, distinct from unilateral tariff actions.
#   Customs & HSN Trade Data -- reserved specifically for HSN-code-level
#     dashboard/data-tool posts (8-digit tariff-line tables, searchable trade-
#     code tools), NOT narrative trade stories that merely cite an HS chapter
#     in passing -- six posts that work at 2-digit chapter level with a
#     narrative frame were deliberately excluded from this label for that
#     reason (hsn-wise-historical-importexport-trends, indias-trade-balance-
#     hsn-wise, fy2025-26-sample-report-india-trade, import-dependent-sectors-
#     vs-government, priority-export-destinations-by-growth, priority-trade-
#     partners-by-import).
#   Quality Standards & Certification -- BIS/QCO-type quality regulation that
#     gates market access, distinct from tariffs themselves. Two posts
#     (the-rupee-fell-10-and-exports-grew-09, if-india-paid-brics-in-rupees-
#     scenario) matched "BIS" in keyword search but that's the Bank for
#     International Settlements, not the Bureau of Indian Standards -- a
#     false positive caught and excluded, not a borderline call.
#
# Export Promotion Schemes was considered and NOT created: only one post had
# genuine substantive coverage (indias-trade-story-has-three-big-wins, via its
# Export Promotion Mission section), below the 2-3+ post bar for a new label --
# folded into that post's Free Trade Agreements tag instead of forcing a thin
# cluster into existence.
#
# 19 of the 69 posts got at least one addition (two got two: the two
# chemical-import-substitution posts that carry both a genuine DGTR AD-duty
# tracking section and an 8-digit HSN dashboard). The other 50 were left alone.
#
# Borderline calls, included but flagged as thinner than their cluster-mates:
#   nobody-blockaded-hormuz-to-slow-india (FTA) -- the FTA content is a
#     supporting section within a shipping/geopolitics narrative, not the
#     piece's main subject.
#   indias-textile-import-export-strategy (Quality Standards) -- one named
#     "Quality Control Initiative (2024-25): BIS Mandatory Standards"
#     subsection, thinner than the other four in that cluster.
#   india-imports-283000-tonnes-of-almonds (Trade Remedies) -- a full
#     dedicated section, but the "remedy" is a historical 2019-2023
#     retaliatory duty tied to a US Section 232 dispute, not a live AD/CVD case.
#
# Considered and rejected (not guessed into a bucket):
#   one-refinery-flipped-nigeria-from -- Dangote's stated need for "anti-
#     dumping protection" for a hypothetical Kenya refinery is one fact
#     restated three times, not India-specific trade-remedy content; already
#     a deliberate exclusion in the Energy & Fuels pass too.
#   indias-lock-imports-hit-19784-million -- explicitly states no confirmed
#     AD duty or DGTR safeguard investigation was found on locks, only
#     advocacy calling for one.
#   indias-subsidised-imports-fertilisers -- a 12% safeguard duty and a QCO
#     quota each appear as a single line item inside a 12-category commodity
#     table, not substantive treatment of either mechanism.
#   indias-medical-device-trade-gap-and -- one India-EU FTA bullet in a
#     policy list, too thin for Free Trade Agreements.

# SUB-TOPIC REFINEMENT PASS 4: INDUSTRIAL POLICY (2026-09-26)
#
# Same method again, applied to "Industrial Policy" (92 posts) -- the blog's
# second-biggest bucket, and its most generic one (the auto-labelling
# taxonomy scores it on bare words like "scheme", "incentive", "subsidy",
# "policy", so it catches almost anything government-programme-related).
# Five new labels ADDED on top of existing labels; "Industrial Policy" itself
# untouched on all 92. Checked against the full live label set (59 topics
# after the first three passes) before proposing anything.
#
#   PLI Schemes -- posts substantively about a NAMED Production-Linked
#     Incentive scheme's targets, disbursement, or applicant list, not the
#     generic "scheme" framing the umbrella label already catches.
#   State Investment Incentives -- the state-vs-state industrial-policy
#     competition angle: SGST reimbursement, capital-subsidy menus, which
#     state's incentives actually get paid out vs. announced.
#   Parliamentary Scheme Tracking -- reference/dashboard posts whose actual
#     subject is a dataset of Lok Sabha/Rajya Sabha questions or PIB scheme
#     announcements, not narrative analysis of one scheme.
#   Public Sector & Infrastructure Finance -- the PSU-finance/fund-accounting
#     side (railways economics, DISCOM debt, credit-guarantee/viability-gap
#     fund structure), distinct from the existing Infrastructure & Investment
#     label, which covers the physical-project side.
#   Ease of Doing Business & Regulatory Reform -- the regulatory-machinery/
#     compliance-burden side: multi-regulator certification stacks, gazette-
#     notification chaos, licensing-monopoly reform.
#
# Defence & Strategic Manufacturing was considered and NOT created: only one
# post in the 92 (5071-items-you-cannot-import-and-rs) is genuinely a
# defence-procurement/import-substitution piece, and it already carries both
# "Defence" and "Import Substitution" for that exact reason -- a third label
# would be pure duplication, and there was no second/third post to form a
# real cluster. (india-ended-63-years-of-state-nuclear looks defence-adjacent
# but is civil nuclear power, not defence, and reads better as regulatory
# reform -- the SHANTI Act ending the 63-year state nuclear-construction
# monopoly and the still-unfixed supplier-liability law blocking foreign
# entrants is a licensing/regulatory-barrier story.)
#
# 25 of the 92 posts got at least one addition. The other 67 were left alone.
#
# Borderline calls, included but flagged as thinner than their cluster-mates:
#   where-indias-factories-actually-get (State Investment Incentives) -- the
#     state-by-state IEM implementation dataset that indias-state-incentive-
#     war-gujarats visibly draws on, but the post itself only mentions
#     "incentive" 4 times and reads more as investment-implementation
#     tracking than incentive-menu comparison.
#   indias-60000-crore-api-push-traced-to (PLI Schemes) -- PLI-Bulk-Drugs is
#     a full, data-rich section (one of four), but the piece's real subject
#     is six schemes added together, not PLI alone.
#
# Considered and excluded, worth a second look if the taxonomy is revisited:
#   everyone-worries-about-who-pays-for / india-will-finance-waste-to-energy
#     -- both discuss a scheme's financing gap, but their core subject is
#     CCUS/circularity technology economics, not PSU fund-accounting
#     mechanics -- kept out of Public Sector & Infrastructure Finance.
#   a-2223-crore-coal-freight-railway-line -- pure land-acquisition-
#     notification story; belongs to the physical-infrastructure side the
#     new label explicitly excludes.
#   thirty-one-years-of-asking-parliament / import-dependent-sectors-vs-government
#     -- both thematically close to Parliamentary Scheme Tracking, but each
#     is narrative analysis of one subject's question/scheme history, not a
#     reference dashboard -- left out per the "dashboard, not narrative"
#     distinction the label is meant to draw.
#   rare-earth-magnets-and-specialty-steel -- mentions PLI only
#     comparatively ("unlike most PLI schemes..."); the scheme it's actually
#     about (REPM) isn't itself a PLI scheme.
#   fy2025-26-sample-report-india-trade / five-year-synthesis-trade-currency
#     -- both mention PLI in just one chart/section out of seven or eight;
#     too thin, per the same bar the Energy & Fuels pass used.
#   where-indias-fdi-actually-lands-state -- state/district FDI
#     concentration data, but no incentive-policy content at all; not the
#     same story as the State Investment Incentives cluster.

# SUB-TOPIC REFINEMENT PASS 5: MARKETS & FINANCE (2026-09-26)
#
# Same method again, applied to "Markets & Finance" (42 posts). Four new
# labels ADDED on top of existing labels; "Markets & Finance" itself
# untouched on all 42. Checked against the full live label set (64 topics
# after the first four passes -- including Currency Markets, Macroeconomics
# & Monetary Policy, Insurance & Reinsurance and Sustainable Finance, which
# already exist as separate labels and were treated as off-limits duplicates)
# before proposing anything.
#
#   Equity Markets & Stock Screening -- quant/factor stock-screening,
#     price-band cluster analysis, model portfolios, cheap-stock/microcap
#     segmentation using Sharpe ratios and NSE price-warehouse data. The
#     professional/methodology-driven equity-analysis side.
#   Bonds & Fixed Income -- bond issuance mechanics, tax/capital-gains bond
#     exemption math, infrastructure project-bond financing.
#   Personal Finance & Retail Investing Access -- fractional investing,
#     SIPs, the 50/30/20 rule, retail market-access framing. Distinct from
#     the Equity Markets cluster above even where the narrative hook looks
#     similar: why-bet-on-one-horse-when-you-can-buy uses the same
#     fractional/thali framing device but its actual method is Sharpe-ratio
#     price-band portfolio construction, so it was filed under Equity
#     Markets & Stock Screening, not here.
#   Corporate Finance & M&A -- roll-up consolidation, bankruptcy
#     restructuring, bolt-on acquisitions. Only 2 posts, thinner than every
#     other cluster in all five passes so far, but both matches are
#     unambiguous and self-labelled by the post itself ("Mergers &
#     Acquisitions" / "Global M&A" appear on-page) -- judged real rather
#     than forced, on the same "2+ genuine beats 3+ thin" standard the
#     Industrial Policy pass used when it rejected a 1-post cluster
#     (Defence & Strategic Manufacturing) but this one clears the bar.
#
# A false-positive trap caught along the way, same shape as the Trade &
# Tariffs pass's BIS/BIS-standards mix-up: "quant" keyword hits in five
# posts (indias-shrimp-exports-did-not-collapse, indias-8-digit-trade-book-
# searchable, beyond-pump-what-upi-fee-would-cost, lpgs-missing-number-7308-
# commission-and, upi-fees-are-now-legal-petrol-pumps) were all "quantity"/
# "quantified", nothing to do with quantitative finance -- excluded.
#
# 16 of the 42 posts got at least one addition. The other 26 were left alone
# (general-purpose finance/trade/currency/policy pieces, or already covered
# by an existing label like Insurance & Reinsurance or Sustainable Finance).
#
# Considered and NOT created:
#   IPOs & Public Listings -- only one genuine match
#     (engineering-and-auto-component-makers, 488 SEBI DRHP filings); four
#     other posts mention "IPO" only in passing (one asset class among
#     several, or a single cited data point) -- the same "one-off" trap the
#     brief warned about, left uncreated below the 2-3+ post bar.
#   Credit Ratings & Corporate Risk -- no genuine cluster. ICRA/CRISIL
#     mentions in raising-green-debt-globally (a bond-issuer rating scale,
#     already covered by Bonds & Fixed Income) and textbooks-say-project-
#     returns-converge (one citation of this blog's own separate ICRA piece
#     as supporting evidence) are both passing references, not rating-
#     agency analysis in their own right.
#
# Flagged as genuinely unsure rather than guessed:
#   premium-now-claim-later-float-indias -- heavy bond/equity-allocation
#     content (insurer float invested in government securities/bonds), but
#     judged as belonging to the existing Insurance & Reinsurance angle
#     (insurance-float asset allocation) rather than Bonds & Fixed Income
#     (bond-instrument mechanics) -- could reasonably go either way.
#   securitising-deficit-what-it-would / if-india-paid-brics-in-rupees-scenario
#     -- both cite sovereign bond yields/G-secs inside a de-dollarisation/
#     currency scenario model; left unlabelled since they read as Currency
#     Markets material (an existing separate label), and retroactively
#     assigning that label to posts outside the current bucket is outside
#     this pass's scope.

# SUB-TOPIC REFINEMENT PASS 6: INDIA (2026-09-27)
#
# Same method, applied to "India" -- the blog's residual/catch-all label (30
# posts) rather than a sector label like the previous five. Expected, and
# found, thinner and more heterogeneous clusters than any prior pass: over
# half the bucket (17 of 30) is genuinely miscellaneous and was left alone.
# Four new labels ADDED on top of existing labels; "India" itself untouched.
#
#   Water Infrastructure Financing -- AMRUT urban water/sewerage capital,
#     Jal Jeevan Mission rural piped-water, Tamil Nadu's multi-stream water
#     funding. Distinct from Irrigation & Water Management (that label is
#     explicitly scoped to farm irrigation ownership/cost-recovery, not
#     drinking-water/municipal infra) and from Infrastructure & Investment
#     (the broad umbrella all three already carry). All three posts already
#     cross-link each other as a series in their own "Related" footers.
#   Cash Crop Export Economics -- coco-peat, coconut/copra, spices, coffee,
#     Assam matcha: single-named-commodity profiles sharing one recurring
#     shape (production map, this blog's own HS-code trade data, a
#     value-chain gap, a review of the relevant commodity board). NOTE: Pass
#     1 already looked at coffee and coco-peat specifically and declined to
#     give them a narrower label -- but that test was against Pass 1's six
#     farming-*mechanism* labels (seeds, irrigation, fertiliser, insurance,
#     livestock, grain procurement); this cluster is a different axis (a
#     recognisable single-commodity export-deep-dive *format*, which four of
#     the five posts explicitly self-describe as one series in their own
#     footers). Recorded here rather than silently overriding Pass 1's
#     verdict on the other axis.
#   Scheme Delivery Gap -- PM-MKSSY fisheries (₹6,000cr allocated, ₹4.73cr
#     paid), PMAY-G West Bengal (12.6 lakh sanctioned, 1.5 lakh finished),
#     PLI (₹1.5 lakh cr approved, ~18% disbursed): the announced-vs-actually-
#     paid gap as the literal headline subject, not a supporting detail.
#     GENERICITY RISK, flagged deliberately: nearly every scheme post on this
#     blog touches this gap to some degree. Scope stayed tight to only the
#     3 posts where it is the headline; do not expand this label loosely in
#     a future pass without re-checking that bar. fourteen-states-reimburse-
#     investors is a strong thematic match but already the core exemplar of
#     the existing State Investment Incentives label -- left off to avoid
#     redundancy, though adding both wouldn't be unreasonable.
#   Carbon Capture & Storage -- ONGC/IOCL's Koyali-Gandhar CO2 capture-and-
#     injection pilot plus the CCUS storage-site geology piece. Only 2 posts,
#     same "2 genuine beats 3+ thin" standard Pass 5 used for Corporate
#     Finance & M&A -- both matches are substantial, not passing mentions.
#     Distinct from Carbon Markets (credit-trading instruments, not physical
#     capture/storage) and from Climate & Carbon (the broad umbrella both
#     already carry).
#
# Considered and NOT created: a broader "Net-Zero Modelling" label merging
# the CCUS pair with price-is-wire-how-gcam-actually-links and rin-red-and-
# cbio-what-indias-ethanol -- rejected because each of those two already has
# a precise existing label (Climate Modeling, and a biofuel-carbon-credit
# angle distinct from physical capture) that a combined label would blur
# rather than sharpen. A "Government Directories & Fact-Checking" pairing
# (nine-ministries-one-list-every-company + we-fact-checked-66-investment)
# was rejected as a shared writing *format* (source-by-source verification),
# not a subject a reader would browse for.
#
# Anomalies noticed but NOT corrected in this pass (out of scope -- this
# project only adds sub-topic labels, it does not audit or remove existing
# ones): none found in the India bucket itself; see the Gas & LNG pass below
# for two flagged there.

# SUB-TOPIC REFINEMENT PASS 7: GAS & LNG (2026-09-27)
#
# Same method, applied to "Gas & LNG" (28 posts). Six new labels ADDED on
# top of existing labels; "Gas & LNG" itself untouched on all 28. Coverage
# ratio this pass (23 of 28, 82%) is much higher than prior passes (27-38%)
# -- not from forced splitting, but because this bucket happens to contain
# several posts that already explicitly self-describe as a multi-part series
# ("Part 1/2/3", "companion piece", "sequel") rather than one-off pieces.
#
#   City Gas Distribution -- the CGD retail business end-to-end: GA district
#     licensing map, the 82k-outlet geocoded retail network, a cold-chain
#     overlay on that network, CGD overtaking fertiliser as India's largest
#     gas-consuming sector, the CBG-to-CGD pipeline-connectivity gap, and
#     PNGRB's prepaid-smart-meter mandate for domestic PNG connections.
#     Checked against Circularity & Waste-to-Value (used only for material
#     recycling/waste-to-energy, not gas-pipeline connectivity, so the CBG
#     post is not a duplicate there).
#   Gas Pipeline Infrastructure & Demand Planning -- the national trunk-
#     pipeline network: a 2013 demand forecast read against actual (~1/4 of
#     predicted) demand, pipeline utilisation, the full non-gas pipeline map,
#     the 1962 land-acquisition law behind pipeline gazette notices, and
#     PNGRB's 2025 Vision-2040 committee report (an explicit sequel to the
#     2013-vision piece, reusing its own utilisation tables). All five
#     cross-reference each other as a series in their own text.
#   Global LNG Markets -- international LNG trade/pricing/geopolitics, not
#     India-specific: the 2025 437 Mt global record, the EU's record LNG
#     imports and US dependence, Europe's landlocked states and the Hormuz-
#     driven supply crunch.
#   LNG Plant & Terminal Engineering -- liquefaction/regasification plant
#     technology and asset integrity, not the trade/market side: electric-
#     motor-drive decarbonisation, the Starter-Helper Motor throughput trick,
#     corrosion-under-insulation on FSRUs/FPSOs, and the Kakinada gravity-
#     based-structure terminal (included here rather than under CGD/
#     regulation because roughly 60% of that piece is terminal technology,
#     the PNGRB rule-change is the hook, not the subject).
#   LNG Trucking & Fleet Conversion -- LNG-truck total-cost-of-ownership
#     versus diesel, and fleet-growth-versus-forecast. Only 2 posts, same
#     thin-but-unambiguous standard as Corporate Finance & M&A in Pass 5.
#   Regulatory & Industry-Body Accountability -- a recurring investigative
#     thread distinct from the sector clusters above: checking an oil-and-
#     gas institution's own claims against its own disclosed numbers. FIPI's
#     oldest ask (gas under GST) still unmet with no reform traceable to it;
#     API's MOUs with FIPI/OISD/PNGRB real but not shown to be FIPI-caused
#     (explicitly cross-references the FIPI post as "the same pattern");
#     PNGRB's own Action Taken Report claiming "achieved" against its own
#     undercutting numbers (2/43 pipelines converted, 0 Ombudsmen appointed)
#     -- this third post is the weakest link, a regulator's report card
#     rather than an industry-body advocacy piece like the other two, kept
#     in on a MEDIUM rather than HIGH confidence call.
#
# Considered and NOT created: splitting City Gas Distribution into a mapping
# sub-cluster versus a demand/regulation sub-cluster (would produce two
# thinner labels with less distinct identity than one unified CGD label,
# rejected); merging Global LNG Markets with LNG Plant & Terminal Engineering
# into one "Global LNG" label (rejected -- one is a policy-analyst's market/
# pricing interest, the other a technical reader's asset-engineering
# interest, genuinely different browsing intents); a single "PNGRB Reports &
# Committees" label grouping every PNGRB-committee-sourced piece regardless
# of subject (rejected as grouping by document type rather than topic --
# the smart-meters piece is squarely a CGD story and the Vision-2040 piece
# squarely a pipeline story, each routed to its subject-matched cluster
# instead). scan-bottle-deliver-what-ppacs-numbers (LPG cylinder/bottling)
# is a genuine singleton in this batch, left alone below the 2-post bar.
#
# Two anomalies flagged, NOT corrected here (out of scope for an additive
# sub-topic pass -- noted for a future labelling-accuracy pass instead):
#   everyone-worries-about-who-pays-for -- actually a CCUS/CO2-pipeline-
#     economics piece (already carries Climate & Carbon + Industrial
#     Policy, which cover it); its "Gas & LNG" label looks like a keyword
#     false-positive on pipeline/PNGRB-common-carrier mentions rather than a
#     genuine gas/LNG subject match.
#   where-indias-green-hydrogen-bets-are -- squarely a green-hydrogen
#     production-mapping piece that the existing "Hydrogen" label is built
#     for, but did not carry that label. Unlike the item above, this is a
#     pure omission (adding a correct existing label, not removing an
#     incorrect one), so it was corrected in this pass's apply run rather
#     than only flagged.


def headings(path):
    s = Path(path).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", s, flags=re.S | re.I)
    rest = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", s, flags=re.S | re.I)
    rest += re.findall(r'class="(?:extitle|h2sub|standfirst|eyebrow)"[^>]*>(.*?)</p>', s, flags=re.S)
    # kicker eyebrows sometimes open with an empty decorative <span
    # class="dot"></span> before the real text -- skip it, or the
    # non-greedy match stops at that inner span's close and captures "".
    rest += re.findall(r'class="kicker"[^>]*>(?:<span[^>]*></span>)?(.*?)</span>', s, flags=re.S)
    strip = lambda xs: [html.unescape(re.sub(r"<[^>]+>", " ", x)) for x in xs]
    return " ".join(strip(h1) * 3 + strip(rest)).lower()


def labels_for(text, max_labels=3):
    score = {lab: sum(text.count(k) for k in keys) for lab, keys in TAXONOMY.items()}
    best = max(score.values())
    if best == 0:
        return []
    cut = max(1, best / 3)
    picked = sorted((l for l, s in score.items() if s >= cut),
                    key=lambda l: -score[l])[:max_labels]
    return picked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    if not (args.plan or args.apply):
        ap.error("pass --plan or --apply")

    manifest = json.loads((ROOT / "meta" / "manifest.json").read_text())["posts"]
    by_slug = {r["slug"]: r for r in manifest.values()}

    plan = []
    for f in sorted(glob.glob(str(ROOT / "posts" / "*.html"))):
        slug = Path(f).stem
        rec = by_slug.get(slug)
        if not rec:
            continue                      # archived file with no live post
        labs = OVERRIDE[slug] if slug in OVERRIDE else labels_for(headings(f))
        plan.append((slug, rec["id"], labs))

    tally = collections.Counter(l for _, _, ls in plan for l in ls)
    print(f"posts: {len(plan)}   unlabelled by the rules: "
          f"{sum(1 for _, _, l in plan if not l)}\n")
    for lab, n in tally.most_common():
        print(f"   {n:3}  {lab}")
    if args.plan:
        print()
        for slug, _, labs in plan:
            print(f"   {slug[:52]:54} {', '.join(labs) or '— none —'}")
        return 0

    done = skipped = 0
    for slug, pid, labs in plan:
        if args.limit and done >= args.limit:
            print(f"\nstopping at --limit {args.limit}")
            break
        if not labs:
            continue
        try:
            p = B.api(f"/blogs/{B.BLOG_ID}/posts/{pid}")
        except SystemExit as e:
            print(f"  skip {slug}: {e}")
            continue
        if p.get("labels"):
            skipped += 1
            continue                      # already done — makes this resumable
        try:
            B.api(f"/blogs/{B.BLOG_ID}/posts/{pid}",
                  data={"id": pid, "title": p["title"], "content": p["content"],
                        "published": p["published"], "labels": labs},
                  method="PUT")
        except B.Ceiling as e:
            print(f"\ndaily write ceiling reached after {done} writes: {e}")
            print("re-run tomorrow — already-labelled posts are skipped")
            return 3
        done += 1
        print(f"  {done:3} {slug[:48]:50} {', '.join(labs)}")
        time.sleep(B.WRITE_GAP_SECONDS)
    print(f"\nlabelled {done} | already had labels {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

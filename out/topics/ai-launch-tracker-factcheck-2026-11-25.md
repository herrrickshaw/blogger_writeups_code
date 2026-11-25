# Fact-check: "AI High-Demand Launch Tracker", edition of 24 Nov 2026 (claude.ai artifact AzFor7NoF3HiByurgNcBGn)

Checked 25 Nov 2026 by web search, one pass per card, using search excerpts (no page was opened). "Confirmed" means a named source supports the core claim, not that every adjective was checked. Vendor-reported benchmarks stay vendor-reported.

## Wrong or unsupported (fix before reuse)
| Card | Claim in the artifact | What the search shows |
|---|---|---|
| Kimi K3.1 Pro Prime (Moonshot, "Nov 20", "K3.1 Pro 59.7% TB4.1") | A model called Kimi K3.1 Pro Prime released 20 Nov, with 59.7% on Terminal-Bench 4.1 | No product named "Prime" was found. Kimi K3.1 Pro was released 23 Oct 2026 (with a Highspeed variant). Moonshot reports 65.7% on Terminal-Bench 4.0, and Artificial Analysis reportedly 67%. No 4.1 score of 59.7% found. The card's date, name and score are all unsupported. |
| Ruflo ("~121M npm download events", "98 agents", "renamed Nov 2026") | | Renamed from Claude Flow to Ruflo with the v3.5 release in Feb 2026 (the npm package and CLI kept the claude-flow name). One README reports 12.52M ecosystem downloads over 12 months to 4 Oct 2026; a badge shows 22.2M+. No source for 121M, and agent counts read "100+" not 98. |
| SWE-2 Flash ("free through Dec 4, then $0.10/$0.50") | | Free period reported as ending 30 Nov, not 4 Dec. No source gives $0.10/$0.50 for Flash (only SWE-2's own $3/$0.30/$15). The 24.0% FrontierCode 2.0 score and the 4 Nov launch are confirmed (vendor-reported). |
| GPT-6.2 Astra vs Claude Fable 5.2 pricing | Fable 5.2 "cut prices about 20% to $8/$40"; Astra "matches Fable's 62 at 20% lower cost ($8/$40)" | Internally inconsistent: both are listed at $8/$40, so Astra cannot be 20% cheaper than Fable. Sources say Astra's $8/$40 is 20% below GPT-6 Astra; Fable 5.2's $8/$40 rests on one secondary article (Towards AI). Artificial Analysis shows 65 (max) and 62 (high) for Fable 5.2 and 62 for Astra, 57 for Sol: these scores check out. |
| Nov AI funding "$8.24B across 117 rounds" | | Not found. Trackers disagree widely and use different cutoffs: one shows 62 rounds and $15.5B to 12 Nov, another 18 rounds and $4.4B to 16 Nov. Cite one tracker with its date, or drop the tile. |
| OpenCode "209,405 stars (Sep 22 snapshot)", "AA Coding Index 53.6" | | The official site cites "over 208,000" (undated). No source for 209,405, the 22 Sep date or the 53.6 index score. MIT licence confirmed. |
| Graphify "Apache-2.0", "Trendshift #25296", "ROSS Index Q3'26 #2", "v8 active" | | YC S26 and the knowledge-graph product confirmed. Apache-2.0, the ROSS rank and "v8" not found; Trendshift appears only as a badge on a PyPI page. Star counts across sources run 58K to 135K (the artifact wisely shows none). Two GitHub locations show up (Graphify-Labs and safishamsi), so the canonical repo is unclear. |
| GitHub Copilot "+GPT-6.2 & MAI Code 2", "first time it has topped Claude Code and Codex" | | The 71.2% and #1 on Terminal-Bench 4.1 for Copilot Fusion Max are confirmed (GitHub changelog, 17 Nov; 5.4 points ahead of Opus 5.5 and Fable 5.2; 88% cheaper than Fable 5.2). Nothing found on GPT-6.2 or MAI Code 2 being added, nor on "first time". |
| Qwen4-Max "25% cheaper than Qwen3.8-Max", "cheapest November release above 40 on AA" | | Launch (16 Nov), $1.50/$4.50 and AA 43 confirmed. The per-token price of Qwen3.8-Max was not found (AA task cost fell from $10.02 to $3.27, a different measure); the "cheapest above 40" claim is unchecked. |
| Gemini 4 "Carbon → Hydrogen → Neon", "Neon newest flagship", "Nov 10 to 18" | | Hydrogen is confirmed: 12 Nov launch, $1.50/$7.50, AA 51 default and 54 at xhigh. Neon ($3/$15) and Carbon ($4/$20) exist on Artificial Analysis, but their November dates and the order are not confirmed; Argon launched 30 Sep. |

## Confirmed (with qualifiers)
| Card | Result |
|---|---|
| LangChain, $300M Series C, 13 Nov | Confirmed. Also reported: $3B valuation, led by CapitalG (the artifact omits both). |
| Model ML, $250M Series B at $1.5B, 17 Nov, 18 months after stealth | Confirmed (co-led by General Atlantic and QED). London is from one source. |
| Kolibri (Konecta) | Confirmed: launched 13 to 16 Jun 2026. Vendor claims (80% pre-built) are the company's own. |
| Applied Compute, $350M, Elad Gil | Confirmed. Reported 2 to 3 Nov, $3.25B valuation, over $100M ARR. "Series C" is not used by every source (some say growth round). |
| Claude Fable 5.2 on 9 Nov, AA 65 (max) | Score confirmed; the 9 Nov date was not checked; the $8/$40 price is single-source (see above). |
| GPT-6.2 Astra and Sol, 17 Nov | Confirmed with AA 62 and 57. Sol "$2/$10" not individually confirmed. |
| Gemini computer use on Mac, 19 Nov | Confirmed (AI Plus, Pro and Ultra; US English; Apple silicon, macOS 15+). Plan prices conflict across reports (the artifact quotes none). |
| Gemini Tasks wider rollout, 17 Nov | Confirmed: calls, purchases (Agent Payments Protocol), appointments; free in six countries. |
| November Pixel Drop, 10 Nov | Confirmed for Pixel Solver, Create My Widget and Gemini calls. "12+ features" unchecked, and device or region limits (some features Pixel 10 or 11 only) are not stated on the card. |
| ElevenLabs Scribe v3 and v3 Live, 10 Nov | Confirmed (company-reported error reductions of 27% and 43%). |
| Nooks "Node" and $500M, 4 Nov | Confirmed, but the $500M is a non-dilutive commitment from General Catalyst's Customer Value Fund, not an equity round; Node is GA in early 2027. |
| Phaze, $8.75M seed led by a16z, 4 Nov | Confirmed. Parsec founders. |
| Clark, $11M seed, $16M total, 2 Nov | Confirmed; product is "Clerks" for CPA-firm audits. Investor lists differ by source. |
| Traversal, $120M Series B at $1B, 3 Nov | Confirmed (co-led by Kleiner Perkins, Redpoint and Khosla). |

## Counts on the page
22 cards (4 coding, 5 agentic, 5 models, 4 consumer, 4 automation): correct. "New in last 7 days": 7 cards dated on or after 17 Nov: correct on the artifact's own dates, but the Kimi card (20 Nov) is one of them and is unsupported.

## Not established
- No primary page was opened; all checks are search excerpts, several from aggregator sites.
- Vendor benchmark scores (SWE-2 Flash, Scribe v3, Fusion Max) and Artificial Analysis figures were not reproduced.

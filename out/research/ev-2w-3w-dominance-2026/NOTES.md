# EV 2W/3W dominance post: research notes (26 Nov 2026)
Draft: out/post-india-ev-sales-two-three-wheelers-dominate.html (build: build.py, checks: calc.py).
Publishing is manual: python3 tools/blogger_api.py insert --draft --file out/post-india-ev-sales-two-three-wheelers-dominate.html --title "<title>"

## Findings that change the brief
- Outlook Business "2.34 lakh" is dated 6 Nov 2025 (October 2025), so it is not a conflict with 3,54,284 (October 2026).
- Ticker's 9.65% October e-2W penetration agrees with EVreporter's 9.7%; the drop from 11.6% is a festive ICE-retail effect, not a data conflict.
- CEEW FY25 and Autocar Pro FY25 agree to 0.01% (e-2W); EVreporter FY26 is 5.0% higher on e-2W and says it includes the Telangana RTO portal.
- Live post shows e-3W 30.5% (L5 passenger, deck) vs EVreporter 33.7% vs FADA/Autocar Pro 60.9% (e-rickshaws included): three denominators, one label.
- EVreporter prints 57.9% e-2W share but its own counts give 57.7%; its June headline is 9 below its components.

## Blocked / not read
CEEW dashboard pages (Cloudflare, not bypassed), Vahan dashboard (unreachable), Mercom (network refusal), NewsBytes (403), JMK (outside allowlist), Ticker.
Raw page copies are under raw/ (committed in 90d19aa; the earlier note that they were not committed was stale); URLs are in the post's Sources block.

## Update, 27 Nov 2026: CEEW National Volume Monitor screenshots
Four screenshots of https://www.ceew.in/gfc/tools_and_dashboards/electric-mobility/national-volume-monitor were supplied by the blog's author and are saved under ceew_dashboard/ (ev_shares.png, state_volumes.png, penetration.png, registration.jpg). They are the only first-hand dashboard data seen; the page itself is blocked here.
- Exact (printed): the EV Shares legend (E-2W 56.9, E-Rickshaw 27.3, E-3W 8.4, E-4W 6.5, E-4W (C) 0.5, E-Bus 0.2, LDV/MDV/HDV 0.2, cumulative FY2014 to FY2027) and the legible registration labels (FY2017-18 95,430; FY2019-20 172,035; FY2021-22 456,192; FY2022-23 1,183,167; FY2023-24 1,681,315; FY2024-25 1,986,107; FY2025-26 2,535,656). The FY2014-15 and FY2015-16 labels overlap (read as 2,399 and 16,165).
- Read by eye (about, +/- 50 thousand on state totals): the state stacked bars and the penetration lines. calc.py holds them as DASH_ST and DASH_PEN with their asserts.
- Findings: the dashboard FY2025 total (1,986,107) is 1.1% above the CEEW issue brief (1,964,831); FY2024 matches to 14 units; the FY2026 total sits between EVreporter (-0.6%) and Autocar Pro (+3.4%); Tamil Nadu and Rajasthan rank fourth and fifth cumulatively and were not in the issue brief's ten states.

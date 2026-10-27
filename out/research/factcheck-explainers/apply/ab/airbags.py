import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from abcommon import load, rep, note, save
S = 'airbags-and-seat-belts-are-import-heavy'
t = load(S)
t = rep(t, "was valued at roughly &#8377;13,595 crore in 2021 and is projected to reach &#8377;20,165 crore by FY2025-26, a 10.35% CAGR.",
        "was valued at roughly &#8377;13,595 crore in 2021 and is projected to reach &#8377;20,165 crore by FY2025-26, a 10.35% CAGR, according to a single trade-press source (Technical Textiles Today) that this blog could not check against official data.")
t = rep(t, "<tr><td>Mobiltech imports</td><td>6,004</td><td>~25.96% of all technical-textile imports</td></tr>",
        "<tr><td>Mobiltech imports</td><td>6,004</td><td>~25.96% of all technical-textile imports; single trade-press source, not checked against official data</td></tr>")
t = rep(t, "<p class=\"gb-note\">The &#8377;6,004 crore import figure and the 2021 market-size figure are from the same NTTM-era baseline;",
        "<p class=\"gb-note\">The market-size and import figures in this table come from one trade-press source (Technical Textiles Today), which dates the &#8377;6,004 crore import figure to FY2025-26; they could not be checked against Ministry of Textiles or DGCI&amp;S data. The &#8377;6,004 crore import figure and the 2021 market-size figure were described here as being from the same NTTM-era baseline;")
t = rep(t, "<tr><td>National Technical Textiles Mission (2020-2026)</td><td>&#8377;1,480 crore since launch</td><td>168+ R&amp;D projects funded (&#8377;500cr+),",
        "<tr><td>National Technical Textiles Mission (2020-21 to 2025-26)</td><td>&#8377;1,480 crore total outlay; &#8377;517 crore allocated and &#8377;393 crore used by March 2025</td><td>168 R&amp;D projects approved (about &#8377;509 crore), 2 completed by 2025;")
t = rep(t, "so it is checkable whether any of the ₹1,480 crore or ₹10,683 crore reaches",
        "so it is checkable whether any of the ₹1,480 crore NTTM outlay or the ₹10,683 crore PLI reaches")
t = note(t, "The National Technical Textiles Mission&rsquo;s &#8377;1,480 crore is its total outlay for 2020-21 to 2025-26, not money spent &ldquo;since launch&rdquo;: &#8377;517 crore had been allocated and &#8377;393.39 crore used by March 2025 (PIB, 2025), and its 168 research projects (about &#8377;509 crore) were approved, not funded, with 2 completed. The policy table now says so. The mobiltech market size (&#8377;13,595 crore in 2021, &#8377;20,165 crore projected for FY2025-26) and imports (&#8377;6,004 crore, about 26% of technical-textile imports) come from a single trade-press source that could not be checked against official data; they are now marked as such.")
save(S, t)

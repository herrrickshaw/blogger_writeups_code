from _b4 import load, rep, insert_note, save, SRC
S = "one-nation-one-gst-rate-what-true-flat"
N = "Notification No. 9/2025-Central Tax (Rate), G.S.R. 641(E), 17 September 2025, in force from 22 September 2025 (Gazette of India Extraordinary CG-DL-E-17092025-266209)"
t = load(S)
t = rep(t, "On top of that, gold and jewellery are reported to remain at a separate 3% rate and rough diamonds at 0.25%,",
    "On top of that, gold, silver, platinum, pearls, jewellery, imitation jewellery and coins stay at a separate 3% rate, rough diamonds and rough precious stones at 0.25%, and cut and polished diamonds at 1.5% (the central-tax halves of 1.5%, 0.125% and 0.75% in " + N + "),")
t = rep(t, "Four effective rates, two narrow legacy carve-outs,", "Four effective rates, three narrow legacy carve-outs,")
t = rep(t, "<div class=\"gb-warn\"><b>What this piece could not fully verify.</b> The 3% gold/jewellery and 0.25% rough-diamond rates are sourced to tax-advisory and trade-press summaries, not to a primary CBIC notification this piece read directly. Readers relying on exact current rates for a specific transaction should confirm against CBIC's own notification text, not this summary.</div>",
    "<div class=\"gb-warn\"><b>Checked against the notification.</b> The 3%, 0.25% and 1.5% rates are from the text of " + N + ", read through " + SRC + ". Readers relying on exact current rates for a specific transaction should still check for later amendments.</div>")
t = rep(t, "the 3% gold/jewellery and 0.25% rough-diamond rates are from secondary tax-advisory summaries (ClearTax, Bajaj Finserv, JewelOve) and were not independently confirmed against primary CBIC notification text for this piece.",
    "the 3% (Schedule IV), 0.25% (Schedule V) and 1.5% (Schedule VI) rates are from " + N + ", read in the Gazette&rsquo;s text (egazette.gov.in/WriteReadData/2025/266209.pdf) through " + SRC + ".")
t = insert_note(t, "The precious-metal and diamond rates have been checked against the Gazette of India: " + N + ". It confirms 3% on gold and jewellery and 0.25% on rough diamonds, and shows two things this piece had missed: the 3% schedule also covers silver, platinum, pearls, imitation jewellery and coins, and cut and polished diamonds carry a third concessional rate of 1.5%. The text now says three carve-outs, not two.")
save(S, t)

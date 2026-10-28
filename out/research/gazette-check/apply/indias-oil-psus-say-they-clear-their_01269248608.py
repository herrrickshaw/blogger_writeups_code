"""Gazette check, 28 Oct 2026: Public Procurement Policy for MSEs (Amendment) Order, 2018."""
from g28 import load, rep, insert_note, save
S = "indias-oil-psus-say-they-clear-their_01269248608"
t = load(S)
t = insert_note(t,
    "The 2018 change to the MSE procurement order has been checked against its Gazette notification: the Public Procurement Policy for Micro and Small Enterprises (MSEs) Amendment Order, 2018, "
    "dated 9 November 2018 (F. No. 21(22)/2018-MA), raised the annual target from 20% to 25% of procurement value and added the 3% sub-target for women-owned MSEs as a new paragraph 4A. "
    "That notification predates the Gazette index this blog now uses (which starts in September 2022) and was read through the search-index text of the Gazette copy published by Bharat Petroleum; "
    "the 4% SC/ST sub-target and the L1+15% matching rule come from the original 2012 Order, whose text was not opened.")
t = rep(t, "The L1+15%/minimum-25%-share/proportionate-split mechanism is corroborated across multiple independent secondary legal summaries of the MSE Order 2012/2018; this piece did not read the order's own gazette text directly.",
        "The 25% target and the 3% women-owned sub-target were checked on 28 October 2026 against the Gazette notification of the 2018 Amendment Order (9 November 2018, F. No. 21(22)/2018-MA), read through the search-index text of the copy hosted by Bharat Petroleum. The L1+15%/minimum-25%-share/proportionate-split mechanism and the 4% SC/ST sub-target are from the 2012 Order as described in multiple independent secondary legal summaries; the 2012 Order&rsquo;s own text was not opened.")
save(S, t)

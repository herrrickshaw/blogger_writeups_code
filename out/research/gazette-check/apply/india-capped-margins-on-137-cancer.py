from gzcommon import load, rep, insert_note, save, VIA
S = "india-capped-margins-on-137-cancer"
G = "CG-DL-E-17102026-277271"
t = load(S)
t = rep(t, "about 1.3 in a usual branded chain and under a 30% cap, against",
        "about 1.3 in a usual branded chain and about 1.43 under the 30% cap, against")
t = rep(t, ">30% cap, upper reading</text>", ">30% cap (S.O. 5690(E))</text>")
t = rep(t, "A 30% cap allows about 1.30 to 1.43 times, depending on whether the 30% is read as a margin on the stockist price or a share of the MRP; reports describe it both ways, and the notification ties it to the March 2026 price to stockist. Either way, a 30% cap is close to what an ordinary branded chain already earns.",
        "The order&rsquo;s own formula (Table A of S.O. 5690(E)) sets the MRP at the price to stockist &times; {1 + 30/(100 &minus; 30)}, plus GST: the 30% is a share of the MRP, so the MRP before GST can be at most about 1.43 times the March 2026 price to stockist. The order&rsquo;s worked example takes a stockist price of Rs 70 to a maximum MRP of Rs 100 plus GST. That is close to, and slightly above, what an ordinary branded chain already earns.")
t = rep(t, "<td>2.73&ndash;3.00</td><td>86&ndash;87%</td>", "<td>3.00</td><td>86%</td>")
t = rep(t, "<td>13.65&ndash;15.00</td><td>85&ndash;87%</td>", "<td>15.00</td><td>85%</td>")
t = rep(t, "<p class=\"gb-note\">An illustration of what a 30% cap would mean if it applied to these two packs; it does not.",
        "<p class=\"gb-note\">An illustration of what the order&rsquo;s formula would mean if it applied to these two packs; it does not.")
old = t[t.index("<p>The October 2026 notification (S.O. 5690(E)) and the committee&rsquo;s report could not be opened directly;"):]
old = old[:old.index("The March 2026 recovery figures")]
t = rep(t, old, "<p>The October 2026 order (S.O. 5690(E), " + G + ") was " + VIA + "; the list of 137 drugs, the formula, the March 2026 base price and the 9 November start date above match it. The committee&rsquo;s report could not be opened directly; its contents come from news reports and PRS Legislative Research&rsquo;s summary. ")
t = rep(t, "2026 trade-margin cap: S.O. 5690(E) of 17 October 2026 and NPPA&rsquo;s 151st meeting, as reported by",
        "2026 trade-margin cap: NPPA order S.O. 5690(E), 17 October 2026, Gazette of India Extraordinary " + G + " (egazette.gov.in/WriteReadData/2026/277271.pdf); coverage by")
t = insert_note(t, "Checked against the Gazette of India: NPPA&rsquo;s order S.O. 5690(E) of 17 October 2026 (" + G + ") caps the trade margin on 137 non-scheduled cancer drugs at 30% of the MRP, not 30% over the stockist price: its formula is MRP = price to stockist &times; {1 + 30/(100 &minus; 30)} plus GST, about 1.43 times the March 2026 stockist price. The piece had shown both readings; the illustration table and chart now use the order&rsquo;s formula. The order also covers patented drugs, treats hospitals that buy directly from the maker as stockists, excludes free patient-assistance supplies from the calculation, lets products already priced below the cap keep their MRP, and takes effect on 9 November 2026.")
save(S, t)

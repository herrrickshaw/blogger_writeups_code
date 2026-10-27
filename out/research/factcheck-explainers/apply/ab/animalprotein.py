import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from abcommon import load, rep, note, save
S = 'indias-animal-protein-export-complex'
t = load(S)
t = rep(t, "One report lists Saudi Arabia, Iran and the UAE as the largest destinations by share that year.",
        "One report lists Saudi Arabia, Iran and the UAE as the largest destinations by share that year; APEDA&rsquo;s own list of top destinations differs (see the 27 October update above).")
t = rep(t, "<tr><td>Vietnam</td><td>Among the largest single destinations by volume</td></tr>\n<tr><td>Egypt</td><td>Major Middle East/North Africa buyer</td></tr>",
        "<tr><td>Vietnam</td><td>Top-five destination, FY2025-26 (APEDA)</td></tr>\n<tr><td>Egypt</td><td>Top-five destination, FY2025-26 (APEDA); major Middle East/North Africa buyer</td></tr>\n<tr><td>UAE</td><td>Top-five destination, FY2025-26 (APEDA)</td></tr>")
t = rep(t, "<tr><td>Malaysia</td><td>Regional Southeast Asian demand hub</td></tr>",
        "<tr><td>Malaysia</td><td>Top-five destination, FY2025-26 (APEDA); regional Southeast Asian demand hub</td></tr>")
t = rep(t, "<tr><td>Saudi Arabia</td><td>Halal-certified supply chain requirement</td></tr>",
        "<tr><td>Saudi Arabia</td><td>Top-five destination, FY2025-26 (APEDA); halal-certified supply chain requirement</td></tr>")
t = note(t, "APEDA&rsquo;s figures now confirm the buffalo-meat numbers: exports were $5,098.54 million in FY2025-26 against $4,060.56 million a year earlier, up 25.6%. APEDA lists the top destinations as Vietnam, Egypt, the UAE, Malaysia and Saudi Arabia. That conflicts with the press report quoted in the earlier note below (Saudi Arabia, Iran and the UAE), which this piece no longer relies on; the destination table has been updated.")
save(S, t)

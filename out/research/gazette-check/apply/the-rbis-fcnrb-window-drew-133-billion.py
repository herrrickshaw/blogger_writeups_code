"""FCNR(B) post: circular identified as RBI/2026-27/99 of 8 June 2026; terms checked against FEDAI's circular summaries."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from g28 import load, rep, insert_note, save

S = "the-rbis-fcnrb-window-drew-133-billion"
t = load(S)
t = rep(t, "<td>The bank sells the dollars to the RBI for rupees at the reference rate and buys them back at the same rate at maturity. Swaps could be executed with the RBI until 11 September</td>",
        "<td>The bank sells the dollars to the RBI for rupees at the FBIL reference rate, on a par basis, and buys them back at the same rate at maturity; no ISDA agreement with the RBI is needed. Swaps could be executed with the RBI until 11 September</td>")
t = rep(t, "<td>Deposits exempt from CRR and SLR, according to one law-firm note and this blog&rsquo;s earlier piece; not confirmed from the circular</td>",
        "<td>Fresh and renewed three-to-five-year deposits mobilised to 30 September 2026 exempt from CRR and SLR, under separate RBI amendment directions of 8 June 2026 (as summarised in legal newsletters), not under the swap circular itself</td>")
t = rep(t, "the circular (reported as FMOD.MAOG.No.S-56/01.06.016/2026-27) was not seen.",
        "the circular is RBI/2026-27/99, FMOD.MAOG.No.S-56/01.06.016/2026-27, dated 8 June 2026; its terms above match the summary in the Foreign Exchange Dealers&rsquo; Association of India&rsquo;s June 2026 newsletter, and the early close on 31 August its August 2026 newsletter, though the circular&rsquo;s own text was not opened.")
t = rep(t, "PIB pages and the RBI circular (reported as FMOD.MAOG.No.S-56/01.06.016/2026-27) could not be opened from this blog&rsquo;s tools.",
        "RBI circular RBI/2026-27/99 (FMOD.MAOG.No.S-56/01.06.016/2026-27, 8 June 2026), as summarised in FEDAI&rsquo;s newsletters of June and August 2026 (fedai.org.in); PIB pages and the circular&rsquo;s own text could not be opened from this blog&rsquo;s tools.")
t = insert_note(t, "The swap circular has been identified as RBI/2026-27/99 (FMOD.MAOG.No.S-56/01.06.016/2026-27, 8 June 2026), and the terms in the table were checked against the Foreign Exchange Dealers&rsquo; Association of India&rsquo;s summaries of it (June and August 2026 newsletters): "
                   "the swap is at the FBIL reference rate on a par basis, deposits are three to five years with a one-year lock-in, swaps cannot be cancelled, and the window closed early on 31 August. The CRR and SLR exemption comes from separate RBI amendment directions of 8 June 2026, not the circular; the table now says so. "
                   "The circular itself is published by the RBI, not in the Gazette, and its own text was still not opened.")
save(S, t)

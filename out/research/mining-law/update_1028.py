"""28 Oct 2026 update to the live mining-law post: gazette details, commencement, Jharkhand cess, Karnataka, challenges."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "factcheck-explainers" / "apply"))
from common import load, rep, ROOT

SLUG = "states-won-right-to-tax-mines-in-2024"
NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
        '<b>Updated 28 October 2026.</b> Checked against the Gazette of India: the Act is No. 20 of 2026, assented to on 17 August 2026 (CG-DL-E-17082026-275519), and it came into force on 22 August 2026 under S.O. 4642(E) (CG-DL-E-22082026-275676); the description of Section 9D here matches the gazette text. Also added '
        'Jharkhand&rsquo;s reported cess collections, the mining share of Karnataka&rsquo;s non-tax revenue, and the status of the states&rsquo; Supreme Court challenges. '
        'The timeline, the Karnataka row and the &ldquo;could not establish&rdquo; section have changed.</div>\n')

t = load(SLUG)
t = rep(t, "<td>Presidential assent, as reported; the Act comes into force on a date the Centre notifies</td></tr>",
        "<td>Presidential assent; published in the Gazette of India (Extraordinary) as the Mines and Minerals (Development and Regulation) Amendment Act, 2026 (No. 20 of 2026; CG-DL-E-17082026-275519). Section 1(2) leaves commencement to a central notification</td></tr>"
        "<tr><td>22 August 2026</td><td>The Act comes into force on the date of publication of S.O. 4642(E), Ministry of Mines (Gazette of India Extraordinary, CG-DL-E-22082026-275676)</td></tr>")
t = rep(t, "<td>Karnataka, Kerala and Telangana announce a joint Supreme Court challenge; Jharkhand&rsquo;s cabinet approves its own</td>",
        "<td>Karnataka, Kerala and Telangana announce a joint Supreme Court challenge (20 August); Jharkhand decides on 17 September to file its own; a LiveLaw analysis says a challenge has been filed</td>")
t = rep(t, "<td>A bill expected to raise about Rs 4,713 crore a year, still awaiting the President&rsquo;s assent</td>",
        "<td>A bill expected to raise about Rs 4,713 crore a year, still awaiting the President&rsquo;s assent; mining was 54% of own non-tax revenue in 2021-22 and 43% in 2022-23, and own non-tax revenue is budgeted at Rs 16,000 crore in 2026-27 (PRS)</td>")
t = rep(t, "For Chhattisgarh the loss is an option rather than a budget line.</p>",
        "For Chhattisgarh the loss is an option rather than a budget line.</p>\n"
        "<p>How much of Jharkhand&rsquo;s cess was actually paid before the Act commenced is not in any official release. The state Congress president said the state received Rs 1,380 crore from mineral cess in 2024-25 and Rs 7,487.91 crore in 2025-26; if that is right, those sums are kept, and what is lost is the Rs 14,656 crore budgeted for 2026-27 and the claimed dues. The state&rsquo;s own estimates of the cess&rsquo;s yearly value range from about Rs 7,110 crore to Rs 11,000 crore.</p>")
old_cne = t[t.index("<p>The Act&rsquo;s text and gazette notification could not be opened;"):]
old_cne = old_cne[:old_cne.index("</p>") + 4]
t = rep(t, old_cne,
        "<p>The Act (No. 20 of 2026, CG-DL-E-17082026-275519) and its commencement notification (S.O. 4642(E) of 22 August 2026, CG-DL-E-22082026-275676) were read in the Gazette of India&rsquo;s own text, through the SansadSaar index of the archive.org Gazette of India collection; the provisions and dates above match it. "
        "The arrears figures are claims and estimates, not audited amounts, and they overlap. "
        "Jharkhand&rsquo;s cess collections (Rs 1,380 crore in 2024-25 and Rs 7,487.91 crore in 2025-26) come from a party leader, not the state&rsquo;s accounts. "
        "For Karnataka only the mining share of own non-tax revenue was found (54% in 2021-22, 43% in 2022-23); mining receipts for Rajasthan and Madhya Pradesh were not found on a comparable basis and are left out. "
        "Karnataka, Kerala and Telangana announced a joint challenge on 20 August, and a LiveLaw analysis says it has been filed; Jharkhand decided on 17 September to challenge the Act. No case number, hearing date or interim order was found by 28 October 2026. This is not legal advice.</p>")
t = rep(t, "Congress-ruled states&rsquo; challenge (Business Standard, 20 August 2026).",
        "Congress-ruled states&rsquo; challenge (Business Standard, 20 August 2026; LiveLaw; Deccan Herald, September 2026; Drishti IAS, 17 September 2026). Act No. 20 of 2026: Gazette of India Extraordinary, Part II Section 1, CG-DL-E-17082026-275519; commencement: S.O. 4642(E), Ministry of Mines, 22 August 2026, CG-DL-E-22082026-275676 (egazette.gov.in/WriteReadData/2026/275676.pdf), read via the SansadSaar index of the archive.org Gazette of India collection. Jharkhand cess collections: Keshav Mahato Kamlesh, as reported (Down To Earth; Indian Masterminds). Karnataka non-tax revenue: PRS Karnataka budget analysis 2026-27.")
h = t.index("<h1")
a = t.index('<h2 class="gb-h2"', h)
t = t[:a] + NOTE + t[a:]
out = ROOT / "out" / f"update-2026-10-28-{SLUG}.html"
out.write_text(t, encoding="utf-8")
print("wrote", out.name, len(t))

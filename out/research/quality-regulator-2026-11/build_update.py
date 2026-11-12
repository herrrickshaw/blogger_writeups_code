"""Quality-regulator post: update of 12 Nov 2026. posts/ -> out/update-2026-11-12-india-doesnt-have-one-quality-regulator.html
Sources: Lok Sabha USQ 2895 (10 Mar 2026), DCPC S.O. 5129(E)-5142(E) (12 Nov 2025), BIS lists, gazette orders; see SOURCES below."""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[3]
SLUG = "india-doesnt-have-one-quality-regulator"
t = (ROOT / f"posts/{SLUG}.html").read_text()


def rep(old, new):
    global t
    assert t.count(old) == 1, old[:80]
    t = t.replace(old, new)


NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
        '<b>Updated 12 November 2026.</b> This piece said &ldquo;over 150&rdquo; product categories were under compulsory certification. '
        'DPIIT told the Lok Sabha on 10 March 2026 that 142 Quality Control Orders covering 721 products were in force, down from 190 orders and 773 products in August 2025, '
        'after ministries withdrew compulsory certification for dozens of chemicals, polymers, metals and fibres from July 2025. '
        'A <a href="#s4b">new section</a> sets out those withdrawals and the orders added since. Scheme-X&rsquo;s history now includes its open-ended deferral of November 2025, '
        'and packaged drinking water is no longer given as an example of a compulsory ISI mark, since FSSAI&rsquo;s 2024 amendment, described below, removed that requirement.</div>\n')

# stat tile and the opening of the stat grid
rep('<div class="gb-stat"><b>150+</b><span>Product categories where the "voluntary" ISI mark becomes legally compulsory under a Quality Control Order</span></div>',
    '<div class="gb-stat"><b>721</b><span>Products under 142 Quality Control Orders in March 2026, where the &ldquo;voluntary&rdquo; ISI mark is legally compulsory; down from 773 under 190 in August 2025</span></div>')
m = re.search(r'<div class="gb-stats">.*?</div>\n</div>\n', t, re.S)
assert m and t.count('<div class="gb-stats">') == 1
t = t[:m.end()] + NOTE + t[m.end():]

rep("Over 150 categories are covered today, spanning steel, cement, toys and packaged drinking water; furniture joined the list in 2025.",
    "DPIIT told the Lok Sabha on 10 March 2026 that 142 Quality Control Orders covering 721 products were in force, spanning steel, cement, toys and electrical appliances. "
    "Furniture&rsquo;s order was notified in February 2025 and took effect on 13 February 2026.")

rep("the Ministry repealed the underlying Machinery and Electrical Equipment Safety (Omnibus Technical Regulation) Order, 2024 outright, on 14 January 2026.",
    "the Ministry deferred it again on 13 November 2025, this time to a date still to be notified (S.O. 5179(E)), and then repealed the underlying "
    "Machinery and Electrical Equipment Safety (Omnibus Technical Regulation) Order, 2024 outright by an order dated 14 January 2026 (S.O. 239(E), published in the Gazette on 16 January).")

SECTION = '''<h2 class="gb-h2" id="s4b">Since this piece was first written, the list has shrunk</h2>
<p>The list now moves in both directions. From July 2025, ministries withdrew compulsory certification for a long run of industrial inputs, mostly through orders that give no reason beyond &ldquo;the public interest&rdquo;. The Lok Sabha answer of March 2026 marks each withdrawal in its annexe:</p>
<ul>
<li><b>Chemicals and petrochemicals.</b> Acetic acid, aniline and methanol on 23 July 2025; six fatty-acid and acid-oil standards on 22 October; styrene, maleic anhydride and acrylonitrile on 24 October. On 12 November 2025 the department rescinded 14 orders at once (S.O. 5129(E) to 5142(E)), covering terephthalic acid, ethylene glycol, five polyester yarns and fibres, polyethylene, polypropylene, PVC, ABS, EVA, polyurethanes and polycarbonate. Six more followed on 20 November (including pyridine, H-acid and vinyl sulphone) and seven standards on 28 November (including p-xylene, toluene, vinyl chloride monomer and ethylene dichloride).</li>
<li><b>Metals.</b> The Ministry of Mines withdrew its orders on aluminium, copper, nickel, lead, tin and zinc on 13 November 2025.</li>
<li><b>Fibres.</b> The Ministry of Textiles rescinded the viscose staple fibre order on 18 November 2025, citing supply constraints and higher costs, and the cotton bales order on 9 June 2026.</li>
<li><b>Steel.</b> On 20 November 2025 the Ministry of Steel deferred the implementation of dozens of its standards by three years, and in 2026 it suspended or exempted further grades, including 162 semi-finished stainless grades until 31 March 2027.</li>
<li><b>Suspensions.</b> The linear alkyl benzene order has been suspended in steps, most recently to 31 December 2026, and the n-butyl acrylate order was suspended in July 2026 on account of &ldquo;supply chain disruption&rdquo;.</li>
</ul>
<p>The fall in DPIIT&rsquo;s count, from 190 orders and 773 products in August 2025 to 142 orders and 721 products in March 2026, is about the size of those withdrawals. Business Standard reported that they followed a review by a committee chaired by Rajiv Gauba, a member of NITI Aayog, which proposed cancelling, suspending or deferring orders covering more than 200 products; this blog found no published report from the committee. The two departments that count orders also disagree: the Department of Consumer Affairs&rsquo; year-end review still gave 191 orders covering 773 goods.</p>
<p>New orders kept arriving for finished goods even as inputs left the list. The household electrical appliances safety order came into force on 1 October 2026. A Hand Tools order of 9 October 2026 (S.O. 5561(E)) applies from 1 April 2027, and a second cookware order of 13 October covers aluminium utensils, with beverage cans from April 2027. The pattern, for now, is fewer mandatory standards on the materials factories buy and more on finished products.</p>
<p>The other two examples above have moved too. The Bureau of Energy Efficiency&rsquo;s mandatory label for induction hobs, due from 1 July 2026, was pushed to 1 January 2027; BusinessLine linked the delay to LPG supply concerns. And FSSAI added a testing scheme for packaged drinking water and mineral water from 1 January 2026, so the 2024 carve-out removed a second mark, not the checking.</p>

'''
rep('<h2 class="gb-h2" id="s5">What this means for anyone actually trying to sell something</h2>',
    SECTION + '<h2 class="gb-h2" id="s5">What this means for anyone actually trying to sell something</h2>')

rep("<li><b>DPIIT should publish one consolidated, dated register of every Quality Control Order in force, with product category, issuing ministry, effective date and current status</b>, so that",
    "<li><b>DPIIT should publish one consolidated, dated register of every Quality Control Order in force, with product category, issuing ministry, effective date and current status</b>, and reconcile it with the Department of Consumer Affairs&rsquo; count (142 orders in DPIIT&rsquo;s March 2026 answer, 191 in Consumer Affairs&rsquo; year-end review), so that")
m = re.search(r'(<h2 class="gb-h2" id="s1">What would fix this</h2>\n<ul>\n)', t)
assert m
t = t[:m.end()] + ('<li><b>Each ministry that rescinds, suspends or defers a Quality Control Order should publish its reasons</b>, and the report of the committee whose review reportedly preceded the 2025 withdrawals should be released, '
                   'so that manufacturers who invested to comply can see why the requirement went.</li>\n') + t[m.end():]

SOURCES = ('Update of 12 November 2026: <a href="https://sansad.in/getFile/loksabhaquestions/annex/187/AU2895_1f22wj.pdf?source=pqals">Lok Sabha unstarred question 2895, 10 March 2026</a> (142 orders, 721 products, and the annexe of withdrawals); '
           '<a href="https://sansad.in/getFile/annex/268/AU2938_qpC6cH.pdf?source=pqars">Rajya Sabha question 2938, 19 August 2025</a> (190 orders, 773 products); '
           '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2207673">Department of Consumer Affairs year-end review</a>; '
           '<a href="https://chemicals.gov.in/sites/default/files/notification/Rescind-the-Fourteen-notifications.pdf">S.O. 5129(E) to 5142(E), 12 November 2025</a>; '
           '<a href="https://chemicals.gov.in/sites/default/files/notification/Gazette_Notification_of_Withdrawal.pdf">withdrawals of 20 November 2025</a>; '
           '<a href="https://www.bis.gov.in/wp-content/uploads/2025/11/Copper-Quality-Control-Order-2023-Withdrawal-Order.pdf">Ministry of Mines copper withdrawal order</a>; '
           '<a href="https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2191408">PIB on viscose staple fibre</a>; '
           '<a href="https://www.bis.gov.in/wp-content/uploads/2026/06/Rescind-Order-of-the-Cotton-Bales-Quality-Control-Order-2023-1.pdf">cotton bales rescission</a>; '
           '<a href="https://www.steel.gov.in/sites/default/files/2026-06/Steel%20and%20Steel%20Products%20%28Quality%20Control%29%20Amendment%20Order%202026.pdf">steel amendment order, June 2026</a>; '
           '<a href="https://www.business-standard.com/industry/news/no-bis-certification-required-qcos-for-plastics-synthetic-fibres-scrapped-125111301885_1.html">Business Standard on the review committee</a>; '
           '<a href="https://heavyindustries.gov.in/sites/default/files/2025-11/machinery_and_electrical_equipment_safety_omnibus_technical_regulation_second_amendment_order_2025.pdf">S.O. 5179(E), 13 November 2025</a> and '
           '<a href="https://www.bis.gov.in/wp-content/uploads/2026/01/Machinery-and-Electrical-Equipment-Safety-Omnibus-Technical-Regulation-Order-2024.pdf">S.O. 239(E), 14 January 2026</a> (Scheme-X); '
           '<a href="https://www.bis.gov.in/wp-content/uploads/2025/02/Furniture-QCO-17-02-2025.pdf">Furniture QCO, S.O. 801(E)</a>; '
           '<a href="https://www.bis.gov.in/wp-content/uploads/2026/10/Notifying-Hand-Tool-Quality-Order-2026.pdf">Hand Tools QCO 2026</a>; '
           '<a href="https://www.bis.gov.in/upcoming-qcos-notified-and-due-for-implementation?lang=en">BIS list of upcoming QCOs</a>; '
           '<a href="https://egazette.gov.in/WriteReadData/2025/268894.pdf">BEE regulations, 26 December 2025</a>; '
           '<a href="https://www.thehindubusinessline.com/economy/policy/india-delays-mandatory-energy-efficiency-rules-for-induction-hobs-amid-lpg-concerns/article70831655.ece">BusinessLine on induction hobs</a>; '
           '<a href="https://www.fssai.gov.in/docs/whatsnew/advisories-orders/6944f19f64122Scheme%20of%20Testing%20PDW%20MW.pdf">FSSAI testing scheme for packaged and mineral water</a>. ')
rep("Compiled via web research and one supplied GitHub repository on 24 September 2026;",
    SOURCES + "Originally compiled via web research and one supplied GitHub repository on 24 September 2026;")

out = ROOT / f"out/update-2026-11-12-{SLUG}.html"
out.write_text(t)
print("wrote", out.relative_to(ROOT))

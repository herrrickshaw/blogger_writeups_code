#!/usr/bin/env python3
"""Phase 1 merge: india-ec-approval-funnel-parivesh-20 absorbs
india-environmental-clearances-state and india-forest-wildlife-crz-clearances.

Writes out/update-2026-11-10-india-ec-approval-funnel-parivesh-20.html.
All figures are the PARIVESH 2.0 snapshot fetched 22 Jul 2026, as published in
the three source posts; the state x sub-sector table is the 19 Oct 2026 run of
the same committed snapshot, as published in how-to-use-india-ec-subsector-analysis.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[3]
POSTS = ROOT / "posts"
SLUG = "india-ec-approval-funnel-parivesh-20"
ABSORBED = ["india-environmental-clearances-state", "india-forest-wildlife-crz-clearances"]
OUT = ROOT / "out" / f"update-2026-11-10-{SLUG}.html"

t = (POSTS / f"{SLUG}.html").read_text()


def sub1(old, new, s):
    assert s.count(old) == 1, (old[:80], s.count(old))
    return s.replace(old, new)


# ---- registers (all from the source posts) -----------------------------------
REG = {  # filed, granted, in process, not approved (rejected/withdrawn/returned), delisted
    "EC": (113970, 54406, 27548, 6954, 25061),
    "FC": (28999, 6134, 8479, 2663, 11723),
    "WLC": (4919, 517, 4319, 83, 0),
    "CRZ": (2264, 468, 1025, 82, 689),
}
for k, (f, g, p, d, x) in REG.items():
    assert abs(f - (g + p + d + x)) <= 1, k   # EC is one short: the +-1 consolidation artifact
rate_dec = {k: 100 * g / (g + d) for k, (f, g, p, d, x) in REG.items()}
rate_live = {k: 100 * g / (g + p) for k, (f, g, p, d, x) in REG.items()}
rate_dec["EC"] = 100 * 54406 / 61361          # the funnel's own decided total
assert round(rate_dec["EC"], 1) == 88.7
assert [round(rate_live[k], 1) for k in ("FC", "WLC", "CRZ")] == [42.0, 10.7, 31.3]


def pct(v):
    return f"{v:.1f}%"


def n(v):
    return f"{v:,}"


def card(label, code, k, extra):
    f, g, p, d, x = REG[k]
    w = [100 * v / f for v in (g, p, d, x)]
    segs = "".join(f'<span class="seg {c}" style="width:{v:.2f}%"></span>' for c, v in zip("gpdx", w) if v)
    return f"""<div class="card">
 <div class="ctop"><div><div class="clabel">{label}</div><div class="ccode">{code}</div></div><div class="cbig">{n(f)}</div></div>
 <div class="bar" role="img" aria-label="{label}: {n(g)} granted, {n(p)} in process, {n(d)} not approved, {n(x)} delisted, of {n(f)} filed">{segs}</div>
 <div class="crow"><span><b class="g">{n(g)}</b> granted</span><span><b class="p">{n(p)}</b> in process</span><span><b class="d">{n(d)}</b> not approved</span><span><b class="x">{n(x)}</b> delisted</span></div>
 <div class="grate">{extra}</div></div>"""


CARDS = "\n".join([
    card("Environmental Clearance", "EC &middot; majorClearanceType 1", "EC",
         "ToR 15,869 &middot; screening 7,197 &middot; appraisal 4,482 in process &middot; 49% fresh new projects"),
    card("Forest Clearance", "FC &middot; majorClearanceType", "FC",
         "36 states/UTs <span style=\"font-size:.85em\">(+1 legacy/unknown category in the source data)</span><br>"
         "<b>25,546</b> fresh (Form-A) &middot; <b>2,097</b> re-diversion (Form-E) &middot; <b>213</b> renewal &middot; <b>261</b> transfer"),
    card("Wildlife Clearance", "WLC &middot; majorClearanceType", "WLC",
         "36 states/UTs (+1 legacy/unknown category) &middot; most in-process cases &ldquo;Pending at Proponent&rdquo;"),
    card("CRZ Clearance", "CRZ &middot; majorClearanceType", "CRZ", "17 coastal states/UTs"),
])

RATE_ROWS = "".join(
    f"<tr><td>{lab}</td><td>{pct(rate_dec[k])}</td><td>{pct(rate_live[k])}</td></tr>"
    for lab, k in (("Environmental (EC)", "EC"), ("Forest (FC)", "FC"), ("Wildlife (WLC)", "WLC"), ("CRZ", "CRZ")))

H2 = 'style="font-size:1.1em;color:#0f4034;border-bottom:2px solid #e3ecea;padding-bottom:5px;margin-top:26px"'
H3 = 'style="font-size:1em;color:#0f4034;margin:22px 0 6px"'
P = 'style="line-height:1.65"'

HOWTO = "https://masaladeutsch.blogspot.com/2026/10/how-to-use-india-ec-subsector-analysis.html"
REPO = "https://github.com/herrrickshaw/india-ec-subsector-analysis"

CSS = """
/* merged 2026-11-10: state view + Forest/Wildlife/CRZ cards, scoped to .pvx */
.pvx .cards{display:grid;grid-template-columns:1fr;gap:14px;margin:18px 0}
@media(min-width:700px){.pvx .cards{grid-template-columns:1fr 1fr}}
.pvx .card{background:#fcfcfa;border:1px solid #d7dace;border-radius:12px;padding:14px 16px}
.pvx .ctop{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}
.pvx .clabel{font-size:16px;font-weight:600;color:#14180f}
.pvx .ccode{font-family:ui-monospace,Menlo,monospace;font-size:10.5px;color:#82867a;text-transform:uppercase;letter-spacing:.06em}
.pvx .cbig{font-size:26px;color:#1f5f5b;line-height:1}
.pvx .bar{display:flex;height:12px;border-radius:6px;overflow:hidden;margin:12px 0 8px;background:#eef2ec;gap:1.5px}
.pvx .seg{display:block;height:100%}.pvx .seg.g{background:#2f7d4f}.pvx .seg.p{background:#c98a1f}.pvx .seg.d{background:#a5402c}.pvx .seg.x{background:#9a9e90}
.pvx .crow{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:12px;color:#4f5348}
.pvx .crow b{font-family:ui-monospace,Menlo,monospace}.pvx b.g{color:#2f7d4f}.pvx b.p{color:#a5700f}.pvx b.d{color:#a5402c}.pvx b.x{color:#6f7366}
.pvx .grate{font-size:12px;color:#5c6660;margin-top:10px;border-top:1px dashed #d7dace;padding-top:8px;line-height:1.5}
.pvx .big-forest{background:#fcfcfa;border:1px solid #d7dace;border-left:4px solid #2f7d4f;border-radius:10px;padding:14px 16px;margin:10px 0 4px;display:flex;flex-wrap:wrap;gap:12px 26px;align-items:baseline}
.pvx .big-forest .n{font-size:28px;color:#2f7d4f}.pvx .big-forest .l{font-size:12.5px;color:#5c6660}
.pvx .dash{display:inline-block;background:#1f5f5b;color:#fff;font-weight:700;padding:9px 20px;border-radius:999px;text-decoration:none;margin:4px 0 8px}
.pvx .tcap{font-size:.85em;color:#5c6660;margin:4px 0 0}
"""

STATE = f"""
<div class="pvx">
<h2 {H2}>Where Environmental Clearances land: the state &times; sub-sector view</h2>
<figure style="margin:1.6rem 0">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Singareni_opencast_coal_mines_at_Manuguru_02.jpg/960px-Singareni_opencast_coal_mines_at_Manuguru_02.jpg" alt="Singareni opencast coal mines at Manuguru, Telangana, India" loading="lazy" style="width:100%;height:auto;border-radius:6px;display:block"/>
<figcaption class="gb-note" style="margin-top:.4rem">Large opencast mining projects like this one are exactly the kind of proposal that moves through India's Environmental and Wildlife Clearance pipeline. <a href="https://commons.wikimedia.org/wiki/File:Singareni_opencast_coal_mines_at_Manuguru_02.jpg" rel="noopener noreferrer">Singareni opencast coal mines at Manuguru 02.jpg</a>, Adityamadhav83, CC BY-SA 3.0, via Wikimedia Commons.</figcaption>
</figure>
<p {P}>The EC register is the earliest public, machine-readable signal of where physical investment is headed &mdash; before IEM implementation, before commissioning. Flagship-project absences (e.g. POSCO-JSW JV, RRPCL) are as informative as the grants. Split by state and EIA sub-sector, the 113,970 proposals are anything but evenly spread: mining of minerals alone accounts for 78,867 of them (69%), and in most sub-sectors a single state holds a large share of the grants.</p>
<div class="tw"><table>
<thead><tr><th>EIA sub-sector</th><th>Proposals</th><th>Leading state, share of grants</th></tr></thead>
<tbody>
<tr><td>1(a) Mining of minerals</td><td>78,867</td><td style="white-space:normal;word-break:normal;overflow-wrap:normal">Rajasthan<br>38.3%</td></tr>
<tr><td>8(a) Building / construction</td><td>12,598</td><td style="white-space:normal;word-break:normal;overflow-wrap:normal">Maharashtra<br>33.0%</td></tr>
<tr><td>8(b) Townships / area development</td><td>4,572</td><td style="white-space:normal;word-break:normal;overflow-wrap:normal">Maharashtra<br>38.0%</td></tr>
<tr><td>5(f) Synthetic organic chemicals</td><td>3,066</td><td style="white-space:normal;word-break:normal;overflow-wrap:normal">Gujarat<br>56.2%</td></tr>
<tr><td>3(a) Metallurgical industries</td><td>2,107</td><td style="white-space:normal;word-break:normal;overflow-wrap:normal">Chhattisgarh<br>17.3%</td></tr>
<tr><td>5(g) Distilleries</td><td>1,031</td><td style="white-space:normal;word-break:normal;overflow-wrap:normal">Odisha<br>39.3%</td></tr>
<tr><td>3(b) Cement plants</td><td>432</td><td style="white-space:normal;word-break:normal;overflow-wrap:normal">Rajasthan<br>16.2%</td></tr>
<tr><td>1(c) River valley / irrigation</td><td>415</td><td style="white-space:normal;word-break:normal;overflow-wrap:normal">Madhya Pradesh<br>27.8%</td></tr>
</tbody></table></div>
<p class="tcap">The largest EC sub-sectors in the 22 July 2026 snapshot, from the repo's committed <code>ec_subsector_analysis.json</code>, as run in <a href="{HOWTO}">How to use india-ec-subsector-analysis</a>.</p>
<p {P}>The full matrix, every state against every sub-sector with status counts, is on the interactive dashboard:</p>
<p><a class="dash" href="https://herrrickshaw.github.io/india-ec-subsector-analysis/">Open the state &times; sub-sector dashboard &rarr;</a></p>
<ul>
<li><b>State &times; sub-sector matrix</b> &mdash; which states clear what: mining-heavy registers (Madhya Pradesh, Chhattisgarh, Rajasthan minor minerals) versus industrial ECs (Gujarat, Maharashtra) versus infrastructure corridors.</li>
<li><b>Fresh versus reuse</b> &mdash; only 49% of proposals are new projects; 22% are mostly re-appraisals of expiring minor-mineral leases on the same plots, plus transfers, expansions and amendments.</li>
</ul>
<h3 {H3}>Why the state pattern isn't random</h3>
<p {P}>The state &times; sub-sector split matters because it separates two very different kinds of clearance activity that a national grant-rate number blends together. States like Madhya Pradesh, Chhattisgarh and Rajasthan carry disproportionately large EC registers because of minor-mineral mining &mdash; and mining clearances have a structural reason to recur on the same plots: a mining lease has a fixed term, and its renewal or re-appraisal shows up in the register as a new proposal even though no new land is being disturbed. That's a large share of what sits behind the 49% fresh-versus-reuse split. Gujarat and Maharashtra's registers, by contrast, skew toward industrial and infrastructure ECs &mdash; plants, corridors, ports, and in the table above 56.2% of chemicals grants and a third or more of building and township grants &mdash; which are more likely to represent genuinely new capacity landing rather than an existing lease renewing itself on paper.</p>
<p {P}>That distinction is the reason to treat the 88.7% grant rate as a starting point rather than a conclusion. A state with a high grant rate built mostly from mining re-appraisals is not attracting more new investment than a state with a lower rate built mostly from first-time industrial ECs &mdash; the two numbers describe different things wearing the same label. Anyone using EC counts as a leading indicator of where capital is actually going needs the fresh-versus-reuse split and the sub-sector mix, not just the state total, or the read is backwards.</p>
<p style="color:#5c6660;font-size:.85em;line-height:1.6"><b>Caveats.</b> Per-state grant rates are not reproduced here; pull them from the dashboard, which shows the repo's latest data &mdash; at the time of writing the same 22 July 2026 snapshot as this page. Treat the qualitative pattern (mining-heavy states skew toward reuse, industrial states toward fresh capacity) as the takeaway. The dashboard and this table use the repo's own grant-rate rules, which exclude delisted proposals; see its README.</p>
"""

BEYOND = f"""
<h2 {H2}>Beyond EC: Forest, Wildlife and CRZ clearances</h2>
<p {P}>The same open PARIVESH API that serves Environmental Clearances serves three more central clearances. Together they are the full green-clearance funnel a project passes through &mdash; and Forest Clearance carries something EC does not: <b>the actual area of land</b>, in hectares. Each card below splits one register by latest status, out of everything filed.</p>
<div class="cards">
{CARDS}
</div>
<p {P}>The grant rates first published for Forest (42.0%), Wildlife (10.7%) and CRZ (31.3%) divided the granted cases by granted plus <i>still in process</i>. The EC rate of 88.7% divides by granted plus <i>not approved</i> (rejected, withdrawn or returned). Those are different questions, so here are all four registers on both bases:</p>
<div class="tw"><table>
<thead><tr><th>Clearance</th><th>Granted &divide; (granted + not approved)</th><th>Granted &divide; (granted + in process)</th></tr></thead>
<tbody>{RATE_ROWS}</tbody></table></div>
<p class="tcap">Delisted cases are excluded from both. The first column asks how often a decision goes the project's way; the second asks how much of the live pool has been cleared.</p>
<h3 {H3}>What the four funnels say</h3>
<p {P}>On the EC basis, all four registers grant most of what they decide: Wildlife {pct(rate_dec['WLC'])}, CRZ {pct(rate_dec['CRZ'])}, Forest {pct(rate_dec['FC'])}. The funnel above holds across the board &mdash; the losses are delisting and waiting, not rejection. <b>Wildlife is still the real bottleneck, but as a queue</b>: 4,319 of 4,919 sit in process, most &ldquo;Pending at Proponent&rdquo; (the ball is with the project applicant, not the regulator) &mdash; projects near protected areas stall here for the National/State Board for Wildlife recommendation. <b>Forest</b>: 88% are fresh Form-A diversions, but 40% of the register is auto-delisted, so the live pool is much smaller than the headline count. <b>CRZ</b> is small and coastal (17 states/UTs) &mdash; the gate for ports, coastal industry and waterfront projects.</p>
<h3 {H3}>Forest Clearance is a second land-creation channel</h3>
<p {P}>Every Environmental Clearance answers &ldquo;may this project pollute?&rdquo;; Forest Clearance answers &ldquo;may this project <i>take</i> this forest land?&rdquo; &mdash; so it is the one register that measures land <b>quantum</b>. Of the 1.05 million ha in the pipeline (inflated by delisted applications and one ~74,000-ha outlier), the trustworthy figure is the forest land with <b>final diversion orders granted</b>:</p>
<figure style="margin:1.6rem 0">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Forests_of_northern_Western_Ghats_Sahyadri%2C_Mhadei_Wildlife_Sanctuary_Goa..jpg/960px-Forests_of_northern_Western_Ghats_Sahyadri%2C_Mhadei_Wildlife_Sanctuary_Goa..jpg?utm_source=commons.wikimedia.org&amp;utm_campaign=imageinfo&amp;utm_content=thumbnail" alt="Forest inside Mhadei Wildlife Sanctuary, Goa" loading="lazy" style="width:100%;height:auto;border-radius:6px;display:block"/>
<figcaption class="gb-note" style="margin-top:.4rem">Forest land inside a wildlife sanctuary like Mhadei is exactly the land quantum that Forest and Wildlife clearances measure. <a href="https://commons.wikimedia.org/wiki/File:Forests_of_northern_Western_Ghats_Sahyadri,_Mhadei_Wildlife_Sanctuary_Goa..jpg" rel="noopener noreferrer">Forests of northern Western Ghats Sahyadri, Mhadei Wildlife Sanctuary Goa..jpg</a>, Rohitjahnavi, CC BY-SA 3.0, via Wikimedia Commons.</figcaption>
</figure>
<div class="big-forest">
 <div><div class="n">49,641 ha</div><div class="l">forest land &mdash; final diversion granted</div></div>
 <div><div class="n">122,666</div><div class="l">acres, granted</div></div>
 <div><div class="n">6,134</div><div class="l">approved proposals of 28,999</div></div>
</div>
<p {P}>For scale: the entire national <i>industrial</i> land bank shows ~253,720 developed-and-vacant acres (Industrial Information &amp; Land Bank, retrieved 2026). Forest diversion adds ~122,666 more acres of granted land-use change &mdash; a different channel (mining, linear infra, hydro), on a different clock.</p>
<h3 {H3}>Forest area by state</h3>
<div class="tw"><table>
<thead><tr><th>State / UT</th><th>Granted ha</th><th>Pipeline ha</th></tr></thead>
<tbody><tr><td>Tripura</td><td>44</td><td>184,758</td></tr><tr><td>Chhattisgarh</td><td>8,061</td><td>146,970</td></tr><tr><td>Madhya Pradesh</td><td>21,146</td><td>146,905</td></tr><tr><td>Maharashtra</td><td>1,087</td><td>88,062</td></tr><tr><td>Andhra Pradesh</td><td>738</td><td>71,232</td></tr><tr><td>Assam</td><td>7,746</td><td>49,780</td></tr><tr><td>Odisha</td><td>1,611</td><td>44,518</td></tr><tr><td>Arunachal Pradesh</td><td>1,084</td><td>42,080</td></tr><tr><td>Rajasthan</td><td>1,343</td><td>35,289</td></tr><tr><td>Meghalaya</td><td>9</td><td>34,793</td></tr><tr><td>Jharkhand</td><td>17</td><td>26,582</td></tr><tr><td>Karnataka</td><td>81</td><td>26,109</td></tr></tbody></table></div>
<p class="tcap">The 12 states with the largest forest-area pipelines; the pipeline column mixes all statuses. Granted area in acres is in the box above (1 ha = 2.471 acres).</p>
<h3 {H3}>Top user agencies (FC)</h3>
<div class="tw"><table>
<thead><tr><th>Agency</th><th>Proposals</th></tr></thead><tbody><tr><td>MAHESH NAIR <span style="font-size:.8em;color:#666">(likely a data-entry artifact &mdash; an individual's name, not an agency)</span></td><td>1,697</td></tr><tr><td>Jal Shakti Department</td><td>1,223</td></tr><tr><td>HIMACHAL PRADESH PUBLIC WORK DEPARTMENT</td><td>769</td></tr><tr><td>Public Works Department</td><td>708</td></tr><tr><td>BHARAT SANCHAR NIGAM LIMITED</td><td>409</td></tr><tr><td>Rural Development</td><td>384</td></tr><tr><td>JIO DIGITAL FIBRE PRIVATE LTD</td><td>321</td></tr><tr><td>Department of Irrigation</td><td>279</td></tr></tbody></table></div>
<p class="note">Sources &mdash; <b>PARIVESH 2.0</b> open API, full registers fetched 22 July 2026: EC (<code>advanceSearchData?majorClearanceType=1</code>; see the note under the funnel) and Forest / Wildlife / CRZ (<code>majorClearanceType=2|3|4</code>). For FC/WLC/CRZ, &lsquo;not approved&rsquo; is rejected, withdrawn or returned, and &lsquo;delisted&rsquo; is PARIVESH's auto-cleanup. FC &lsquo;granted&rsquo; = &ldquo;Final Diversion Order Issued&rdquo; or &ldquo;Stage-II Accorded&rdquo;; Stage-I in-principle is not counted. The forest-area pipeline total mixes all statuses and is skewed by a single ~74,000-ha outlier &mdash; the granted figure is the reliable one. State &times; sub-sector table: the repo's committed snapshot, run 19 October 2026 in <a href="{HOWTO}">How to use india-ec-subsector-analysis</a>. Industrial land bank: Industrial Information &amp; Land Bank, retrieved 2026. Pipeline snapshot, not a time series; a refresh from PARIVESH is pending. Data, methodology and refresh scripts: <a href="{REPO}">github.com/herrrickshaw/india-ec-subsector-analysis</a>. Corrections are displayed, never silent.</p>
</div>
"""

FIXES = f"""<h2 {H2}>What would fix this</h2>
<ul>
<li><b>The Ministry of Environment, Forest and Climate Change (MoEFCC) should publish, on PARIVESH, a standard list of process stages and map all its raw status values to them</b>, so filed, delisted, pending, rejected and granted counts can be read directly and reconcile exactly, rather than being consolidated from 56 status values by outside analysts.</li>
<li><b>MoEFCC should publish the rules for PARIVESH auto-delisting and quarterly counts of delisted proposals by reason &mdash; unanswered query, lapsed deadline, duplicate or other &mdash; by state and sector, for all four registers</b>, so the 25,061 EC and 11,723 Forest Clearance delistings can be traced to specific procedural failures that applicants and appraisal committees can address.</li>
<li><b>MoEFCC should add the date of every status change to the PARIVESH 2.0 open API and publish median days spent at Terms of Reference, screening and appraisal, by state and sector, updated quarterly</b>, so the backlog of 27,548 EC proposals, and the Forest, Wildlife and CRZ registers, can be tracked as waiting time, not only as a single pipeline snapshot.</li>
<li><b>MoEFCC should report EC grants and grant rates for fresh projects separately from re-appraisals, transfers, expansions and amendments</b>, so a headline such as 54,406 grants or an 88.7% grant rate is not read as new capacity when only 49% of proposals are fresh.</li>
<li><b>MoEFCC should add a field on PARIVESH linking each re-appraisal or renewal to the original clearance and mining-lease identifier</b>, so that a minor-mineral lease renewing on the same plot is not counted as a new proposal in state registers.</li>
<li><b>The State Environment Impact Assessment Authorities of Madhya Pradesh, Chhattisgarh and Rajasthan should publish lists of minor-mineral ECs with lease identifier and lease expiry date</b>, so that the recurring re-appraisals that inflate their registers can be forecast and separated from fresh mining proposals.</li>
<li><b>MoEFCC should validate the user-agency field in PARIVESH and correct existing records</b>, so an individual's name does not appear as the top Forest Clearance user agency with 1,697 proposals and agency-wise counts can be trusted.</li>
<li><b>MoEFCC should add range checks on the forest-area field and publish corrections for implausible entries</b>, so a single record of about 74,000 hectares cannot distort the 1.05 million hectare pipeline figure that users of the register will quote.</li>
<li><b>The National Board for Wildlife's Standing Committee should report, for proposals awaiting wildlife clearance, the time spent pending with the proponent and with the state and national boards separately</b>, so the 4,319 cases in process can be attributed to whoever is actually holding them.</li>
</ul>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>

<div style="background:#eef6ff;border:1px solid #b6d4f0;border-radius:12px;padding:1.1rem 1.4rem;margin:1.5rem 0;font-family:-apple-system,'Segoe UI',sans-serif;font-size:.9em;color:#212529"><strong>Related on this blog:</strong> <a href="{HOWTO}">How to use india-ec-subsector-analysis</a> &middot; <a href="https://masaladeutsch.blogspot.com/2026/08/where-indias-factories-actually-get.html">Where India&rsquo;s Factories Actually Get Built &mdash; IEM State &amp; Sector Analysis</a> &middot; <a href="https://masaladeutsch.blogspot.com/2026/08/iem-conversion-historical-performance.html">IEM Conversion &mdash; A Historical Performance Review (2017&ndash;2025)</a> &mdash; the code behind the state view, and the other early signal of where plants get built.</div>

<div class="disc-override" style="margin-top:24px;padding:14px 16px;border-top:1px solid #ddd;font-size:.82em;color:#444;background:#f8f8f6;line-height:1.5"><strong>Disclaimer:</strong> This analysis is based on publicly available government and market data cited in the article above. It is provided for informational and research purposes only and does not constitute investment, legal, or policy advice. Figures may be revised as source data is updated &mdash; verify against the original source before relying on them for decisions.</div>
"""

UPDATE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;'
          'margin:1.2em 0;border-radius:4px"><b>Updated 10 November 2026.</b> This page now brings together three posts '
          'on India&rsquo;s PARIVESH 2.0 clearance register: the EC approval funnel, the state &times; sub-sector view of '
          'Environmental Clearances, and Forest, Wildlife &amp; CRZ clearances; the other two posts have been retired. '
          'All figures are the PARIVESH snapshot fetched on 22 July 2026. A refresh is pending, and this page will be '
          'updated when it lands. One correction: the grant rates first published for Forest (42.0%), Wildlife (10.7%) '
          'and CRZ (31.3%) used a different base from the EC rate (88.7%), so all four are now shown on both bases '
          '(see &ldquo;Beyond EC&rdquo;).</div>\n')

# ---- edits to the target --------------------------------------------------------
old_dek = t[t.index('<p style="order:4" class="dek">'):t.index('</p>', t.index('<p style="order:4" class="dek">')) + 4]
t = sub1(old_dek, '<p style="order:4" class="dek">How 113,970 Environmental Clearance proposals move from filing to grant '
         'on PARIVESH 2.0 (2022&ndash;2026), which states hold the grants in each sub-sector, and how the three other central '
         'green clearances &mdash; Forest, Wildlife and CRZ &mdash; compare. A current-state snapshot fetched 22 July 2026: '
         'each proposal shows its latest status, so proposals counted as "granted" have already passed through the ToR '
         '(Terms of Reference) and appraisal stages.</p>', t)
t = sub1('<h1 style="order:3">The Environmental Clearance approval funnel</h1>',
         '<h1 style="order:3">India&rsquo;s green clearances on PARIVESH 2.0: the EC funnel, the state pattern, and Forest, '
         'Wildlife &amp; CRZ</h1>', t)
t = sub1('text{font-size:13px}.big{font-size:15px;font-weight:600}.small{font-size:11px}\n</style>\n<div class="wrap">',
         'text{font-size:13px}.big{font-size:15px;font-weight:600}.small{font-size:11px}\n' + CSS + '</style>\n<div class="wrap">\n' + UPDATE, t)
# section heading for the funnel itself, so the three parts read as one sequence
t = sub1('<h2 style="font-size:1.1em;color:#0f4034;border-bottom:2px solid #e3ecea;padding-bottom:5px;margin-top:26px">Where the funnel actually loses proposals</h2>',
         f'<h2 {H2}>The EC approval funnel: where it actually loses proposals</h2>', t)
a = t.index('<div style="background:#eef6ff')
b = t.index('<p class="disclaimer"')
t = t[:a] + STATE + BEYOND + "\n" + FIXES + "\n" + t[b:]

for s in ABSORBED:
    assert s not in t, s
OUT.write_text(t)
print(OUT, len(t.encode()))
print({k: (round(rate_dec[k], 1), round(rate_live[k], 1)) for k in REG})

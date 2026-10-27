import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-php-attack-surface.html'

# ---------------------------------------------------------------- data (W3Techs)
PHP_SHARE = 70.2                      # % of sites with a known server-side language, 26 Aug 2026
MAJOR = {"4": 0.1, "5": 7.9, "7": 28.9, "8": 63.1}          # % of PHP sites, 22 Aug 2026
MINOR8 = {"8.0": 7.0, "8.1": 17.8, "8.2": 31.1, "8.3": 31.0, "8.4": 10.7, "8.5": 2.3}   # % of PHP 8 sites, 29 Jun 2026
# support status on 27 Oct 2026 (php.net policy: 2 years active + 2 years security, ending 31 Dec)
STATUS = {"4": "eol", "5": "eol", "7": "eol", "8.0": "eol", "8.1": "eol",
          "8.2": "sec", "8.3": "sec", "8.4": "act", "8.5": "act"}
END = {"8.0": "26 Nov 2023", "8.1": "31 Dec 2025", "8.2": "31 Dec 2026", "8.3": "31 Dec 2027", "8.4": "31 Dec 2028", "8.5": "31 Dec 2029"}
share = {k: v for k, v in MAJOR.items() if k != "8"}
share.update({k: MAJOR["8"] * v / 100 for k, v in MINOR8.items()})
EOL = sum(v for k, v in share.items() if STATUS[k] == "eol")
SEC = sum(v for k, v in share.items() if STATUS[k] == "sec")
ACT = sum(v for k, v in share.items() if STATUS[k] == "act")
EOL_JAN = EOL + share["8.2"]
SEC_JAN = SEC - share["8.2"]
ALL_SITES = PHP_SHARE * EOL / 100
assert abs(EOL + SEC + ACT - 100) < 0.3


def chart_support():
    W, L, top, bh, gap, lab = 400, 10, 44, 24, 16, 96
    rows = [("27 Oct 2026", EOL, SEC, ACT), ("1 Jan 2027*", EOL_JAN, SEC_JAN, ACT)]
    H = top + len(rows) * (bh + gap) + 30
    sc = (W - L - lab - 10) / 100
    cols = ("#a5402c", "#d9a441", "#1c5d99")
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Share of PHP websites by support status: {EOL:.0f}% on versions no longer patched today, rising to {EOL_JAN:.0f}% on 1 January 2027 if none upgrade.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">PHP websites by whether their version still gets security fixes, %</text>',
         f'<rect x="{L}" y="22" width="9" height="9" fill="{cols[0]}"/><text x="{L + 13}" y="30" font-size="9.5" fill="#212529">No fixes</text>',
         f'<rect x="{L + 70}" y="22" width="9" height="9" fill="{cols[1]}"/><text x="{L + 83}" y="30" font-size="9.5" fill="#212529">Security fixes only</text>',
         f'<rect x="{L + 190}" y="22" width="9" height="9" fill="{cols[2]}"/><text x="{L + 203}" y="30" font-size="9.5" fill="#212529">Full support</text>']
    for i, (n, *vals) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 16}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        x = L + lab
        for v, col in zip(vals, cols):
            w = v * sc
            s.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{bh}" fill="{col}"/>')
            if w > 26:
                s.append(f'<text x="{x + w / 2:.1f}" y="{y + 16}" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">{v:.0f}</text>')
            x += w
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">W3Techs version shares (Jun&ndash;Aug 2026) mapped to php.net support dates.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">*If no site upgrades; PHP 8.2 loses security fixes on 31 Dec 2026. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_versions():
    lab = {"eol": "No fixes", "sec": "Security fixes only", "act": "Full support"}
    rows = [("PHP 4 and 5", f"{share['4'] + share['5']:.1f}", "No fixes", "Ended 2008 (PHP 4) and 2018 (PHP 5.6)"),
            ("PHP 7", f"{share['7']:.1f}", "No fixes", "Ended 28 Nov 2022 (PHP 7.4)")]
    for k in MINOR8:
        rows.append((f"PHP {k}", f"{share[k]:.1f}", lab[STATUS[k]], ("Ended " if STATUS[k] == "eol" else "Security fixes until ") + END[k]))
    return table(["Version", "% of PHP websites", "Status on 27 Oct 2026", "End of security fixes"], rows)


def t_leaks():
    return table(["What a site can reveal without being hacked", "What it tells an outsider", "The fix"], [
        ("Software versions in response headers and page code (PHP, the web server, the CMS and its plugins)", "Which published vulnerabilities are likely to work", "Patch first; then switch off version disclosure (PHP&rsquo;s <code>expose_php</code>, server tokens, generator tags)"),
        ("Detailed error messages", "File paths, database names, the framework and sometimes queries", "Log errors privately; show a plain error page to visitors"),
        ("Configuration, backup and source-control files left in the web folder (environment files, database dumps, archive files, repository folders)", "Database passwords, cloud and email keys, payment-gateway secrets, the full source code", "Keep secrets and backups outside the web root; block dot-files; scan your own site for them"),
        ("Diagnostic pages left on (such as a PHP information page)", "The whole server configuration, sometimes including secrets in environment variables", "Delete them from production"),
        ("CMS features that list authors or users", "Valid login names for password-guessing", "Restrict user listings; enforce strong passwords and two-factor login for administrators"),
        ("Public admin and database-management panels", "Where to aim password attacks", "Put them behind a VPN or an IP allow-list"),
        ("Third-party scripts, plugins and themes", "The vendors a company relies on, each with its own flaws", "Keep an inventory; remove what is unused; update the rest"),
    ])


def t_cases():
    return table(["Case", "Entry point", "What it exposed beyond the website"], [
        ("Exposed environment files, 2024 (Palo Alto Networks Unit 42)", "Publicly readable configuration files on about 110,000 domains", "Over 90,000 secrets, about 7,000 of them cloud credentials; data copied out of cloud storage and held to ransom, with no encryption needed"),
        ("CosmicSting, 2024 (Sansec)", "A flaw in Magento/Adobe Commerce, the PHP shop software, patched in June 2024", "Card skimmers on checkout pages at 4,275 shops, about 5% of all such stores; stolen encryption keys meant patching alone did not close the hole"),
        ("PHP-CGI flaw CVE-2024-4577, 2024&ndash;25 (Cisco Talos, GreyNoise)", "Windows servers running PHP in CGI mode", "A foothold into the company network: attackers in Japan moved on to credential theft and remote-control tools; a ransomware gang used it within 48 hours of the patch"),
        ("Betting spam on Indian government sites, 2024&ndash;26 (TechCrunch; FalconFeeds via MediaNama)", "Compromised CMS or server configuration, as researchers suspect", "More than 100 government and public-sector domains ranked betting pages on Google; visitors from search were redirected while administrators saw a normal page"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{PHP_SHARE:.0f}%</b><span>of websites whose server-side language is known run PHP (W3Techs, August 2026)</span></div>
<div class="gb-stat"><b>{EOL:.0f}%</b><span>of those PHP sites run a version that no longer gets security fixes; {EOL_JAN:.0f}% from 1 January 2027 if none upgrade</span></div>
<div class="gb-stat"><b>11,334</b><span>new vulnerabilities found in WordPress add-ons and core in 2025, 91% of them in plugins (Patchstack)</span></div>
<div class="gb-stat"><b>100+</b><span>Indian government and public-sector sites reported serving hidden betting pages, June 2026</span></div>
</div>'''

body = f"""
{stats}

<p>A company&rsquo;s website is usually the least guarded thing it owns and the most visible. It is often built by an agency, hosted by someone else and updated rarely, but it talks to the same database, email system and cloud account as the rest of the business. Seven in ten websites whose software can be identified run PHP, the language behind WordPress, Drupal, Joomla and Magento. This blog&rsquo;s arithmetic from W3Techs&rsquo; figures is that about half of those sites run a version of PHP that no longer receives security fixes, and on 1 January 2027 PHP 8.2 joins them.</p>
<p>This piece explains why PHP sites are where most website attacks land, what a website reveals about its owner before anyone breaks in, what a break-in exposes beyond the site itself, and what Indian companies and government departments should do about it. It describes categories of weakness and the fixes for them, not methods of attack.</p>

<h2 class="gb-h2">Half of PHP websites run an unpatched version</h2>
{chart_support()}
{t_versions()}
<p class="gb-note">W3Techs measures sites whose language it can detect; major-version shares are from 22 August 2026 and PHP 8 minor-version shares from 29 June 2026, so the minor-version rows are approximate. Linux distributions such as Debian, Ubuntu and Red Hat backport fixes to some older versions, so a site on an old version number is not always unpatched; but a site still on PHP 5 or 7 almost always is.</p>
<p>About {EOL:.0f}% of PHP sites are on versions the PHP project no longer fixes, which is about {ALL_SITES:.0f}% of all websites whose language W3Techs can identify. PHP 7 alone, whose last branch lost support in November 2022, still runs on {share['7']:.0f}% of PHP sites. Because PHP 8.2, the most used version, reaches the end of its security fixes on 31 December 2026, the unpatched share rises to about {EOL_JAN:.0f}% at the turn of the year unless sites upgrade.</p>
<p>There is an irony in these numbers. W3Techs can count a site&rsquo;s PHP version largely because the site announces it, in a response header that PHP sends by default. That header is the first thing anyone looking for a vulnerable site reads.</p>

<h2 class="gb-h2">The language is rarely the hole; the add-ons are</h2>
<p>Most PHP websites are not written from scratch; they are a content-management system plus plugins and themes from many small developers. WordPress alone runs about 40% of all websites. Patchstack, a WordPress security firm, counted 11,334 new vulnerabilities in the WordPress ecosystem in 2025, 42% more than in 2024, and 91% of them were in plugins, 9% in themes and only a handful in WordPress itself. It judged about 36% serious enough to need emergency protection rules. For the most heavily attacked flaws, the median time from public disclosure to mass exploitation was about five hours.</p>
<p>That timing matters more than the count. A company that patches its website monthly, or whenever its agency next visits, is exposed for weeks to flaws that automated scanners begin trying within hours. The attacker does not need to choose a target; scanners try every site that matches.</p>

<h2 class="gb-h2">What a website gives away before it is hacked</h2>
{t_leaks()}
<p>None of these needs a break-in. Each is something an ordinary visitor&rsquo;s browser could request, and each tells an outsider either which door to try or what lies behind it. The most damaging are files that should never have been in the public web folder at all: a configuration file holding the database password and cloud keys, or a backup of the customer database left behind after a migration.</p>

<h2 class="gb-h2">What a hacked website exposes beyond itself</h2>
{t_cases()}
<p>The common thread is that the website is connected to more than the website. A PHP application has to hold credentials to do its job: to its database, to send email, to take payments, to store files in the cloud. Whoever controls the application holds those credentials too. That turns a defaced page into a breach of customer records, a payment-card theft or a foothold into the company network. It also exposes things a company may not think of as secret: staff names and email addresses, the vendors and agencies it uses, internal server names, and the cloud accounts it runs.</p>
<p>The Indian government cases show a quieter cost. The hijacked sites did not look hacked to the people running them. Search engines were shown betting pages and visitors arriving from search were redirected, while administrators saw an ordinary page. TechCrunch found about 50 such links on government domains in May 2024; the same pattern was reported across more than 100 domains, including ministries, a High Court and tax and police portals, in June 2026.</p>

<h2 class="gb-h2">The Indian picture</h2>
<p>CERT-In, the national computer emergency response team, handled about 29.44 lakh cyber-security incidents in 2025. The last year for which a breakdown was found, 2022, included 19,793 website defacements, and central and state government websites hacked numbered 59, 42 and 50 in 2020, 2021 and 2022. Government sites must pass a security audit by NIC, STQC or a CERT-In-empanelled auditor before they go live under the Guidelines for Indian Government Websites, but the betting cases show that a clearance at launch says little about a site several years and many plugin updates later.</p>
<p>For companies the stakes are rising. The Digital Personal Data Protection Act provides for penalties of up to Rs 250 crore for failing to take reasonable security safeguards, and its Rules, notified in November 2025, phase in most obligations over 18 months. CERT-In&rsquo;s 2022 directions already require incidents to be reported within six hours. A leaked configuration file from a forgotten marketing site counts as a breach as much as an attack on the core systems.</p>

<h2 class="gb-h2">What companies should do</h2>
<ul>
<li><b>Know what you run.</b> List every public website and subdomain, including old campaign and agency-built sites, with its PHP, CMS and plugin versions and who is responsible for patching it.</li>
<li><b>Get onto supported versions.</b> Move off PHP 7 and 8.0&ndash;8.1 now, and plan the PHP 8.2 upgrade before 31 December 2026; remove plugins that are not used or no longer maintained.</li>
<li><b>Patch in hours, not months.</b> Turn on automatic security updates for the CMS and plugins, or buy a service that applies protection rules on disclosure.</li>
<li><b>Keep secrets out of the web folder.</b> Store credentials in a secrets manager or outside the web root, give the website only the access it needs, and rotate any key that has ever been in a public folder.</li>
<li><b>Say less.</b> Switch off version headers and detailed errors, delete diagnostic pages, and put admin panels behind a VPN or allow-list.</li>
<li><b>Look at your site as Google does.</b> Monitor search results for your domain for unexpected pages, since cloaked spam is designed to be invisible to administrators.</li>
</ul>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>CERT-In should publish yearly counts of website compromises by sector and by cause (unsupported software, plugin flaw, leaked credential), as it did for defacements, so the scale of the problem is measured.</li>
<li>Government websites should be re-audited after major changes and at least yearly, not only before launch, and the audit should check the PHP and CMS versions against their end-of-support dates.</li>
<li>NIC and state IT departments should run a shared inventory of every government web property with its software versions, so that unsupported PHP can be found and replaced centrally.</li>
<li>The Data Protection Board should say in its guidance that running public-facing software past its end of security support is a failure of reasonable security safeguards.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>W3Techs&rsquo; version figures cover only sites that reveal a version, mix dates from June and August 2026, and cannot see distribution backports, so the {EOL:.0f}% figure is an estimate of exposure, not a count of vulnerable sites. No figure was found for the share of Indian websites, or Indian government websites, running unsupported PHP; this blog did not scan any third-party site to find out. The cause of the Indian betting compromises has not been published; the CMS explanation is a researcher&rsquo;s suggestion. CERT-In&rsquo;s defacement breakdown was found only for 2022. Patchstack&rsquo;s figures come from its 2026 report as summarised on its site and in news coverage.</p>
"""

sources = ("PHP usage and version shares: W3Techs, server-side languages (26 August 2026) and PHP version pages (22 August and 29 June 2026); W3Techs founder on detection method (W3Techs forum). PHP support dates: php.net supported-versions policy (September 2024 change), PHP.Watch and remirepo (PHP 8.1 end of life). "
           "WordPress: market share per W3Techs as reported (October 2026); Patchstack, State of WordPress Security in 2026 and its 2025 analysis, as summarised on patchstack.com and by news coverage. "
           "Cases: Palo Alto Networks Unit 42, large-scale cloud extortion operation (August 2024), via Security Affairs, Security Boulevard and The Hacker News; Sansec on CosmicSting via BleepingComputer, SecurityWeek and The Hacker News (October 2024); Cisco Talos on attacks in Japan and GreyNoise on mass exploitation of CVE-2024-4577 (March 2025), via BleepingComputer and Security Affairs; TechCrunch (10 May 2024) and MediaNama citing FalconFeeds (June 2026) on Indian government sites. "
           "India: CERT-In incidents in 2025 (PIB, January 2026, via Morung Express and Vision IAS); 2022 defacements (CERT-In annual report via MediaNama); government websites hacked 2020&ndash;2022 (Rajya Sabha reply, February 2023); GIGW 3.0 security-audit requirement (GIGW guideline 5.3.1, as summarised by audit firms); DPDP Rules notification and phasing (PIB, The Week, Deccan Herald, November 2025); CERT-In directions of 28 April 2022. "
           "The unsupported-version shares are this blog&rsquo;s arithmetic from W3Techs&rsquo; shares and php.net&rsquo;s dates (builder in the repository at out/research/php-surface/). This piece describes weaknesses and fixes for defenders; it is not legal or security advice for any specific system.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/india-tracks-every-taxpayer-in-minutes.html", "India Tracks Every Taxpayer in Minutes. Its Patients Got a Digital ID in 2021, While Indian IT Earns Billions From Foreign Healthcare"),
    ("https://masaladeutsch.blogspot.com/2026/08/abha-what-indias-14-digit-health-id.html", "ABHA: What India&rsquo;s 14-Digit Health ID Actually Does, in the Real Numbers"),
]

build("Cybersecurity · 27 October 2026",
      "Half of PHP Websites Run a Version Nobody Patches. What a Hacked Site Gives Away About Its Company",
      "PHP runs seven in ten websites whose software can be identified, and about half of those run a version that no longer gets security fixes. A company website rarely holds only web pages: it holds the keys to databases, email, payments and the cloud.",
      body, sources, related, OUT)
print("EOL", round(EOL, 1), "SEC", round(SEC, 1), "ACT", round(ACT, 1), "EOL_JAN", round(EOL_JAN, 1), "all sites", round(ALL_SITES, 1), "8.2", round(share['8.2'], 1))

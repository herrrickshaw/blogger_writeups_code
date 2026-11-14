70%of websites whose server-side language is known run PHP (W3Techs, August 2026)

53%of those PHP sites run a version that no longer gets security fixes; 72% from 1 January 2027 if none upgrade

11,334new vulnerabilities found in WordPress add-ons and core in 2025, 91% of them in plugins (Patchstack)

100+Indian government and public-sector sites reported serving hidden betting pages, June 2026

A company’s website is usually the least guarded thing it owns and the most visible. It is often built by an agency, hosted by someone else and updated rarely, but it talks to the same database, email system and cloud account as the rest of the business. Seven in ten websites whose software can be identified run PHP, the language behind WordPress, Drupal, Joomla and Magento. This blog’s arithmetic from W3Techs’ figures is that about half of those sites run a version of PHP that no longer receives security fixes, and on 1 January 2027 PHP 8.2 joins them.

This piece explains why PHP sites are where most website attacks land, what a website reveals about its owner before anyone breaks in, what a break-in exposes beyond the site itself, and what Indian companies and government departments should do about it. It describes categories of weakness and the fixes for them, not methods of attack.

## Half of PHP websites run an unpatched version

[chart: 
 PHP websites by whether their version still gets security fixes, % 
 No fixes 
 Security fixes only 
 Full support 
 27 Oct 2026 
 
 53 
 
 39 
 
 1 Jan 2027* 
 
 72 
 
 20 
 
 W3Techs version shares (Jun–Aug 2026) mapped to php.net support dates. 
 *If no site upgrades; PHP 8.2 loses security fixes on 31 Dec 2026. This blog’s arithmetic. 
]


[T1 "Half of PHP websites run an unpatched version" 8 rows; use rows by number in a chart "table" spec]
  cols: c0 Version | c1 % of PHP websites | c2 Status on 27 Oct 2026 | c3 End of security fixes
  r0: PHP 4 and 5 | 8.0 | No fixes | Ended 2008 (PHP 4) and 2018 (PHP 5.6)
  r1: PHP 7 | 28.9 | No fixes | Ended 28 Nov 2022 (PHP 7.4)
  r2: PHP 8.0 | 4.4 | No fixes | Ended 26 Nov 2023
  r3: PHP 8.1 | 11.2 | No fixes | Ended 31 Dec 2025
  r4: PHP 8.2 | 19.6 | Security fixes only | Security fixes until 31 Dec 2026
  r5: PHP 8.3 | 19.6 | Security fixes only | Security fixes until 31 Dec 2027
  r6: PHP 8.4 | 6.8 | Full support | Security fixes until 31 Dec 2028
  r7: PHP 8.5 | 1.5 | Full support | Security fixes until 31 Dec 2029


W3Techs measures sites whose language it can detect; major-version shares are from 22 August 2026 and PHP 8 minor-version shares from 29 June 2026, so the minor-version rows are approximate. Linux distributions such as Debian, Ubuntu and Red Hat backport fixes to some older versions, so a site on an old version number is not always unpatched; but a site still on PHP 5 or 7 almost always is.

About 53% of PHP sites are on versions the PHP project no longer fixes, which is about 37% of all websites whose language W3Techs can identify. PHP 7 alone, whose last branch lost support in November 2022, still runs on 29% of PHP sites. Because PHP 8.2, the most used version, reaches the end of its security fixes on 31 December 2026, the unpatched share rises to about 72% at the turn of the year unless sites upgrade.

There is an irony in these numbers. W3Techs can count a site’s PHP version largely because the site announces it, in a response header that PHP sends by default. That header is the first thing anyone looking for a vulnerable site reads.

## The language is rarely the hole; the add-ons are

Most PHP websites are not written from scratch; they are a content-management system plus plugins and themes from many small developers. WordPress alone runs about 40% of all websites. Patchstack, a WordPress security firm, counted 11,334 new vulnerabilities in the WordPress ecosystem in 2025, 42% more than in 2024, and 91% of them were in plugins, 9% in themes and only a handful in WordPress itself. It judged about 36% serious enough to need emergency protection rules. For the most heavily attacked flaws, the median time from public disclosure to mass exploitation was about five hours.

That timing matters more than the count. A company that patches its website monthly, or whenever its agency next visits, is exposed for weeks to flaws that automated scanners begin trying within hours. The attacker does not need to choose a target; scanners try every site that matches.

## What a website gives away before it is hacked


[T2 "What a website gives away before it is hacked" 7 rows; use rows by number in a chart "table" spec]
  cols: c0 What a site can reveal without being hacked | c1 What it tells an outsider | c2 The fix
  r0: Software versions in response headers and page code (PHP, the web server, the CMS and its plugins) | Which published vulnerabilities are likely to work | Patch first; then switch off version disclosure (PHP’s expose_php , server tokens, generator tags)
  r1: Detailed error messages | File paths, database names, the framework and sometimes queries | Log errors privately; show a plain error page to visitors
  r2: Configuration, backup and source-control files left in the web folder (environment files, database dumps, archive files, repository folders) | Database passwords, cloud and email keys, payment-gateway secrets, the full source code | Keep secrets and backups outside the web root; block dot-files; scan your own site for them
  r3: Diagnostic pages left on (such as a PHP information page) | The whole server configuration, sometimes including secrets in environment variables | Delete them from production
  r4: CMS features that list authors or users | Valid login names for password-guessing | Restrict user listings; enforce strong passwords and two-factor login for administrators
  r5: Public admin and database-management panels | Where to aim password attacks | Put them behind a VPN or an IP allow-list
  r6: Third-party scripts, plugins and themes | The vendors a company relies on, each with its own flaws | Keep an inventory; remove what is unused; update the rest


None of these needs a break-in. Each is something an ordinary visitor’s browser could request, and each tells an outsider either which door to try or what lies behind it. The most damaging are files that should never have been in the public web folder at all: a configuration file holding the database password and cloud keys, or a backup of the customer database left behind after a migration.

## What a hacked website exposes beyond itself


[T3 "What a hacked website exposes beyond itself" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Case | c1 Entry point | c2 What it exposed beyond the website
  r0: Exposed environment files, 2024 (Palo Alto Networks Unit 42) | Publicly readable configuration files on about 110,000 domains | Over 90,000 secrets, about 7,000 of them cloud credentials; data copied out of cloud storage and held to ransom, with no encryption needed
  r1: CosmicSting, 2024 (Sansec) | A flaw in Magento/Adobe Commerce, the PHP shop software, patched in June 2024 | Card skimmers on checkout pages at 4,275 shops, about 5% of all such stores; stolen encryption keys meant patching alone did not close the hole
  r2: PHP-CGI flaw CVE-2024-4577, 2024–25 (Cisco Talos, GreyNoise) | Windows servers running PHP in CGI mode | A foothold into the company network: attackers in Japan moved on to credential theft and remote-control tools; a ransomware gang used it within 48 hours of the patch
  r3: Betting spam on Indian government sites, 2024–26 (TechCrunch; FalconFeeds via MediaNama) | Compromised CMS or server configuration, as researchers suspect | More than 100 government and public-sector domains ranked betting pages on Google; visitors from search were redirected while administrators saw a normal page


The common thread is that the website is connected to more than the website. A PHP application has to hold credentials to do its job: to its database, to send email, to take payments, to store files in the cloud. Whoever controls the application holds those credentials too. That turns a defaced page into a breach of customer records, a payment-card theft or a foothold into the company network. It also exposes things a company may not think of as secret: staff names and email addresses, the vendors and agencies it uses, internal server names, and the cloud accounts it runs.

The Indian government cases show a quieter cost. The hijacked sites did not look hacked to the people running them. Search engines were shown betting pages and visitors arriving from search were redirected, while administrators saw an ordinary page. TechCrunch found about 50 such links on government domains in May 2024; the same pattern was reported across more than 100 domains, including ministries, a High Court and tax and police portals, in June 2026.

## The Indian picture

CERT-In, the national computer emergency response team, handled about 29.44 lakh cyber-security incidents in 2025. The last year for which a breakdown was found, 2022, included 19,793 website defacements, and central and state government websites hacked numbered 59, 42 and 50 in 2020, 2021 and 2022. Government sites must pass a security audit by NIC, STQC or a CERT-In-empanelled auditor before they go live under the Guidelines for Indian Government Websites, but the betting cases show that a clearance at launch says little about a site several years and many plugin updates later.

For companies the stakes are rising. The Digital Personal Data Protection Act provides for penalties of up to Rs 250 crore for failing to take reasonable security safeguards, and its Rules, notified in November 2025, phase in most obligations over 18 months. CERT-In’s 2022 directions already require incidents to be reported within six hours. A leaked configuration file from a forgotten marketing site counts as a breach as much as an attack on the core systems.

## What companies should do

- Know what you run. List every public website and subdomain, including old campaign and agency-built sites, with its PHP, CMS and plugin versions and who is responsible for patching it.

- Get onto supported versions. Move off PHP 7 and 8.0–8.1 now, and plan the PHP 8.2 upgrade before 31 December 2026; remove plugins that are not used or no longer maintained.

- Patch in hours, not months. Turn on automatic security updates for the CMS and plugins, or buy a service that applies protection rules on disclosure.

- Keep secrets out of the web folder. Store credentials in a secrets manager or outside the web root, give the website only the access it needs, and rotate any key that has ever been in a public folder.

- Say less. Switch off version headers and detailed errors, delete diagnostic pages, and put admin panels behind a VPN or allow-list.

- Look at your site as Google does. Monitor search results for your domain for unexpected pages, since cloaked spam is designed to be invisible to administrators.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]

## What this piece could not establish

[kept verbatim, collapsed: What this piece could not establish]

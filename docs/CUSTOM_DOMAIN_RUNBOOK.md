# Custom domain runbook — masaladeutsch.com

Status (7 Sep 2026): domain not yet registered. `masaladeutsch.com` and
`masaladeutsch.in` were both available on GoDaddy on this date.

## Architecture

| Host | Serves | Why |
|---|---|---|
| `masaladeutsch.com` (apex) and `www` → redirect to apex | Lovable front-door site (project `6684318f-a640-40ec-8e1c-1db6572bf73b`) | Polished home, topics, start-here, policy pages. This is what an AdSense reviewer lands on. |
| `blog.masaladeutsch.com` | Blogger (this blog) | All 257 article URLs keep their `/YYYY/MM/slug.html` paths; Blogger 301-redirects the blogspot address automatically. |

AdSense: add `masaladeutsch.com` as the site. Subdomains are covered by the
root domain, so the blog on `blog.` is reviewed under the same property.
Add ads.txt on BOTH hosts (Blogger: Settings → Monetisation → Custom
ads.txt; Lovable: `public/ads.txt`).

## Steps

1. **Register** `masaladeutsch.com` (GoDaddy or any registrar). Turn on
   WHOIS privacy; that is fine for AdSense.
2. **Blogger → blog subdomain.** Blogger Settings → Publishing → Custom
   domain → `blog.masaladeutsch.com`. Blogger shows two CNAMEs:
   - `blog` → `ghs.google.com`
   - a verification CNAME (random label → `gv-….dv.googlehosted.com`)
   Add both at the registrar, wait for propagation (minutes to a few
   hours), save in Blogger, then turn on **Redirect domain** is NOT
   needed for a subdomain, but turn on **HTTPS availability** and
   **HTTPS redirect** once the certificate is issued.
3. **Lovable → apex.** In the Lovable project: Settings → Domains → add
   `masaladeutsch.com` and `www.masaladeutsch.com`. Lovable shows an A
   record (apex) and a CNAME (`www`); add them at the registrar. Lovable
   issues the certificate and redirects `www` → apex.
4. **Flip the blog base URL** in the Lovable project: change `BLOG_BASE`
   to `https://blog.masaladeutsch.com` and republish.
5. **Repo side** (this repo): every absolute link points at
   `masaladeutsch.blogspot.com`. Blogger's redirect keeps them working,
   but rewrite them so search engines see the canonical host:
   ```
   grep -rl "masaladeutsch.blogspot.com" posts out templates theme tools consistency-check docs \
     | xargs sed -i 's#masaladeutsch\.blogspot\.com#blog.masaladeutsch.com#g'
   ```
   then rebuild the index (`tools/index_graph.py`, `tools/build_index_page.py`)
   and push the changed posts with `tools/apply_batch.sh`. Update
   `tools/blogger_api.py` `BLOG_URL`/verify hosts and `tools/snapshot.py`
   feed URL in the same pass. The GitHub Pages site
   (`herrrickshaw.github.io/masaladeutsch`) About link also changes.
6. **Search Console**: add a Domain property for `masaladeutsch.com`
   (covers both hosts), submit `https://blog.masaladeutsch.com/sitemap.xml`
   and `https://masaladeutsch.com/sitemap.xml`.
7. **AdSense**: Sites → add `masaladeutsch.com`; the Auto-ads code goes in
   the Blogger theme (already there) and in the Lovable site's `<head>`.
   Re-request review only after the redirect has been live for a few
   days and Search Console shows the new host indexed.

## What stays as is
- `masaladeutsch.blogspot.com` keeps redirecting forever; old links and the
  Atom feed keep working.
- Blogger pages (`/p/about.html` etc.) remain; the Lovable site carries its
  own copies so the apex is self-contained for a reviewer.

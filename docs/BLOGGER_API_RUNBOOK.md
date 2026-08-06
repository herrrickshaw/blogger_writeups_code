# Blogger API v3 — setup and operating runbook

Replaces driving the Blogger web editor. The editor has no trustworthy success
signal: a throttled save is indistinguishable from a no-op, which is why several
updates in this project silently did nothing. The API returns a status code.

Blog: `masaladeutsch.blogspot.com` · blogId `2071644453461588122`

---

## Part 1 — one-time setup (~10 minutes, all in your browser)

You do these steps yourself. They involve signing in to your Google account, so
they are not automatable and should not be.

### 1. Create a Cloud project

1. Go to https://console.cloud.google.com/projectcreate
2. Name it something like `masaladeutsch-blogger`. No billing account is needed —
   the Blogger API has no service charge.

### 2. Enable the Blogger API

1. https://console.cloud.google.com/apis/library/blogger.googleapis.com
2. Confirm the project selector (top bar) shows your new project.
3. **Enable**.

### 3. Configure the consent screen

1. https://console.cloud.google.com/apis/credentials/consent
2. User type **External**, then Create.
3. App name, your email for both support and developer contact. Save and continue.
4. **Scopes** — Add or remove scopes → filter for `blogger` → tick
   `https://www.googleapis.com/auth/blogger` ("Manage your Blogger account").
   There is no finer-grained write scope; write access is all-or-nothing.
5. **Test users** — add your own Google address, the one that is **Admin** on the
   blog. An Author-role account can only edit posts it wrote; bulk editing the
   back catalogue requires Admin.
6. Leave the app in **Testing**. You never need to publish it. Refresh tokens for
   apps in Testing expire after 7 days — see "When the token expires" below.

### 4. Create the OAuth client

Prefer **Desktop app**: it may use any loopback port, so nothing needs
registering. A **Web** client works too, but only with a redirect URI you have
registered by hand — add exactly `http://127.0.0.1:8765` under *Authorised
redirect URIs*. `blogger_api.py auth` detects a Web client, prints the URI, and
waits for you to save it.

1. https://console.cloud.google.com/apis/credentials
2. Create credentials → **OAuth client ID** → Application type **Desktop app**.
3. Download the JSON. Save it as:

```bash
mkdir -p ~/.config/market-secrets && chmod 700 ~/.config/market-secrets
mv ~/Downloads/client_secret_*.json ~/.config/market-secrets/blogger_client.json
chmod 600 ~/.config/market-secrets/blogger_client.json
```

This sits beside the existing credential store and stays out of every repo.

### 5. Authorise once and store the refresh token

```bash
python3 ~/masaladeutsch-archive/tools/blogger_api.py auth
```

It prints a URL, you open it, pick the Admin Google account, accept the
"unverified app" warning (it is your own app), and it captures the callback on
localhost. The refresh token is written to
`~/.config/market-secrets/blogger_token.json` (mode 600). You will not need to
repeat this unless the token is revoked or expires.

### 6. Confirm

```bash
python3 ~/masaladeutsch-archive/tools/blogger_api.py whoami
```

Prints the blog name, post count, and your role. If it says anything other than
your blog, the wrong Google account was used in step 5.

---

## Part 2 — daily use

```bash
# read a post's current body (verifies auth end to end, no writes)
python3 tools/blogger_api.py get --slug rooftop-solar-is-working-household

# dry run: show what would change, touch nothing
python3 tools/blogger_api.py update --slug <slug> --file fixes/<slug>.html --dry-run

# do it
python3 tools/blogger_api.py update --slug <slug> --file fixes/<slug>.html

# the whole pending queue, paced and backed off
python3 tools/blogger_api.py bulk --manifest ~/blog-consistency-check/fixes/manifest.json --limit 25
```

Every write is followed by an independent `curl` re-fetch with a cache-buster
before it is reported as successful. Keep that step even though the API returns a
status — it catches the case where a write is accepted but not rendered.

---

## Part 3 — the limits that actually bite

| | Figure | Status |
|---|---|---|
| API requests/day | 10,000 (Cloud Console default) | community-reported, not in Google's docs |
| **Post writes/day, per blog** | **~50–100** | community-reported; **this is the real ceiling** |
| Max post body | ~1 MB per *rendered page* | folklore, no official source |
| Members per blog | 100 total | [official](https://support.google.com/blogger/answer/42673) |

Google publishes none of the throttling numbers. Build for detection, not for a
hardcoded threshold.

**Two different 403s, same status code:**

- *Transient rate limit* — clears with exponential backoff. Retry 1s, 2s, 4s,
  each plus jitter.
- *Daily per-blog ceiling* — does not clear. Stop for the day.

Distinguish them empirically: if ~60s of backoff does not clear it, it is the
ceiling. `blogger_api.py` implements exactly this and exits with a distinct code
so a cron wrapper can tell "try again later" from "try again tomorrow".

**Budget against the per-blog ceiling, not the 10,000/day request quota.** The
request quota is irrelevant to this workload and will mislead you if you plan
against it — 22 pending fixes is fine in one day; 90 post rewrites is three days.

---

## When the token expires

An OAuth app left in **Testing** issues refresh tokens that expire after 7 days.
Two options:

- Re-run `blogger_api.py auth` weekly (10 seconds), or
- In the consent screen, **Publish app**. For a single-user app requesting only
  the Blogger scope, Google does not require verification review to keep working;
  the tokens stop expiring. The "unverified app" interstitial remains.

Take the second option if this becomes a scheduled job.

---

## What NOT to do

- **Do not use a service account.** Blogger data is keyed to Google users; a blog
  cannot be shared to a service-account address, and domain-wide delegation is
  Workspace-only. It returns 403.
- **Do not use an API key alone.** Keys identify the caller for public reads.
  Writes require an authorised user.
- **Do not hot-loop retries.** Rapid successive writes are what the abuse
  detection is watching for, and it is per-blog, not per-request.
- **Do not commit the client JSON or the token.** Both live in
  `~/.config/market-secrets/`, mode 600. `.gitignore` covers `*token*.json` here
  as a second line of defence.

---

## Sources

- [Blogger API v3 — Using the API](https://developers.google.com/blogger/docs/3.0/using)
- [posts.update reference](https://developers.google.com/blogger/docs/3.0/reference/posts/update)
- [OAuth 2.0 scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes)
- [Control access to your blog](https://support.google.com/blogger/answer/42673)
- [Capping API usage](https://support.google.com/googleapi/answer/7035610)
- [Backoff pattern (Gmail docs, the canonical statement)](https://developers.google.com/workspace/gmail/api/guides/handle-errors)

Quota and write-limit figures above marked community-reported appear in Blogger
product forums, not in Google documentation. They matched observed behaviour in
this project but are not contractual.

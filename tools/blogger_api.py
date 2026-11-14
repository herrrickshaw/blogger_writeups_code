#!/usr/bin/env python3
"""Blogger API v3 client for masaladeutsch — read, update and bulk-apply posts.

Replaces driving the web editor, which gives no trustworthy success signal.
See docs/BLOGGER_API_RUNBOOK.md for the one-time OAuth setup.

    python3 tools/blogger_api.py auth
    python3 tools/blogger_api.py whoami
    python3 tools/blogger_api.py get    --slug <slug>
    python3 tools/blogger_api.py update --slug <slug> --file <body.html> [--dry-run]
    python3 tools/blogger_api.py update --id <post-id> --file <body.html>
    python3 tools/blogger_api.py insert --file <body.html> --title "..." [--draft]
    python3 tools/blogger_api.py bulk   --manifest <fixes/manifest.json> [--limit N]

Exit codes:
    0  success
    2  transient failure — safe to retry soon
    3  per-blog daily write ceiling reached — retry tomorrow, not sooner
    4  insert refused: a live post already has this title
"""
import argparse
import html
import http.server
import json
import os
import pathlib
import random
import re
import secrets
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

BLOG_ID = "2071644453461588122"
BLOG_URL = "https://blog.vertistratsolution.com"
API = "https://blogger.googleapis.com/v3"
SCOPE = "https://www.googleapis.com/auth/blogger"

SECRETS = pathlib.Path.home() / ".config" / "market-secrets"
CLIENT_FILE = SECRETS / "blogger_client.json"
TOKEN_FILE = SECRETS / "blogger_token.json"

# Pace deliberately: rapid successive writes are what abuse detection watches.
WRITE_GAP_SECONDS = 4
MAX_BACKOFF_SECONDS = 64


# ----------------------------------------------------------------- transport
def _req(url, data=None, headers=None, method=None):
    body = None
    if data is not None:
        body = data if isinstance(data, bytes) else json.dumps(data).encode()
    r = urllib.request.Request(url, data=body, headers=headers or {}, method=method)
    with urllib.request.urlopen(r, timeout=60) as resp:
        return json.loads(resp.read().decode() or "{}")


def _form(url, fields):
    return _req(
        url,
        data=urllib.parse.urlencode(fields).encode(),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )


# ---------------------------------------------------------------------- auth
# A Desktop ("installed") client may use any loopback port. A Web client may
# only use redirect URIs registered in the Cloud Console, so we must bind a
# fixed, known port and the user must register exactly that URI.
DEFAULT_PORT = 8765


def _client():
    if not CLIENT_FILE.exists():
        sys.exit(f"missing {CLIENT_FILE} — see docs/BLOGGER_API_RUNBOOK.md part 1")
    blob = json.loads(CLIENT_FILE.read_text())
    kind = "installed" if "installed" in blob else ("web" if "web" in blob else None)
    if not kind:
        sys.exit(f"{CLIENT_FILE} is not an OAuth client JSON")
    cfg = blob[kind]
    return cfg["client_id"], cfg["client_secret"], kind


def cmd_auth(args):
    """Run the OAuth loopback flow and persist the refresh token."""
    cid, csec, kind = _client()
    port = args.port or DEFAULT_PORT
    state = secrets.token_urlsafe(16)
    got = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            got.update({k: v[0] for k, v in q.items()})
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Authorised. You can close this tab.</h2>")

        def log_message(self, *a):
            pass

    try:
        srv = http.server.HTTPServer(("127.0.0.1", port), H)
    except OSError as e:
        sys.exit(f"cannot bind port {port} ({e}) — pass --port with a free one, "
                 f"and register that exact URI if this is a Web client")
    redirect = f"http://127.0.0.1:{port}"
    if kind == "web":
        print("This is a WEB OAuth client. Before continuing, add this EXACT URI")
        print("under Authorised redirect URIs and save:\n")
        print(f"    {redirect}\n")
        print("  https://console.cloud.google.com/apis/credentials\n")
        input("Press Enter once saved (Google can take ~30s to apply it)... ")
    auth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": redirect, "response_type": "code",
        "scope": SCOPE, "access_type": "offline", "prompt": "consent", "state": state,
    })
    print("Open this URL and sign in as the account that is ADMIN on the blog:\n")
    print("  " + auth_url + "\n")
    try:
        webbrowser.open(auth_url)
    except Exception:
        pass
    threading.Thread(target=srv.handle_request, daemon=True).start()
    for _ in range(300):
        if got:
            break
        time.sleep(1)
    srv.server_close()
    if got.get("state") != state:
        sys.exit("state mismatch — aborting")
    if "code" not in got:
        sys.exit(f"no authorisation code returned: {got}")

    tok = _form("https://oauth2.googleapis.com/token", {
        "code": got["code"], "client_id": cid, "client_secret": csec,
        "redirect_uri": redirect, "grant_type": "authorization_code",
    })
    if "refresh_token" not in tok:
        sys.exit("no refresh_token returned — revoke prior access and retry")
    SECRETS.mkdir(parents=True, exist_ok=True)
    TOKEN_FILE.write_text(json.dumps({"refresh_token": tok["refresh_token"]}, indent=2))
    TOKEN_FILE.chmod(0o600)
    print(f"refresh token saved to {TOKEN_FILE} (mode 600)")


_access = {"token": None, "expires": 0}


def access_token():
    if _access["token"] and time.time() < _access["expires"] - 60:
        return _access["token"]
    if not TOKEN_FILE.exists():
        sys.exit("not authorised — run: blogger_api.py auth")
    cid, csec, _ = _client()
    rt = json.loads(TOKEN_FILE.read_text())["refresh_token"]
    tok = _form("https://oauth2.googleapis.com/token", {
        "client_id": cid, "client_secret": csec,
        "refresh_token": rt, "grant_type": "refresh_token",
    })
    _access["token"] = tok["access_token"]
    _access["expires"] = time.time() + int(tok.get("expires_in", 3600))
    return _access["token"]


def api(path, data=None, method="GET"):
    """Call the API with backoff. Raises Ceiling on a 403 that will not clear."""
    url = f"{API}{path}"
    delay = 1.0
    last = None
    while delay <= MAX_BACKOFF_SECONDS:
        try:
            return _req(
                url, data=data, method=method,
                headers={"Authorization": f"Bearer {access_token()}",
                         "Content-Type": "application/json"},
            )
        except urllib.error.HTTPError as e:
            detail = e.read().decode()[:300]
            last = f"{e.code} {detail}"
            if e.code in (403, 429, 500, 503):
                wait = delay + random.uniform(0, 0.5)
                print(f"    {e.code} — backing off {wait:.1f}s")
                time.sleep(wait)
                delay *= 2
                continue
            raise SystemExit(f"HTTP {e.code}: {detail}")
    # backoff exhausted on a 403: this is the per-blog daily ceiling, not a blip
    raise Ceiling(last)


class Ceiling(Exception):
    pass


# ------------------------------------------------------------------ commands
def find_post(slug):
    """Locate a post by slug across all pages of the posts list."""
    token, seen = None, 0
    while True:
        q = {"maxResults": 100, "fetchBodies": "false", "status": "LIVE"}
        if token:
            q["pageToken"] = token
        page = api(f"/blogs/{BLOG_ID}/posts?{urllib.parse.urlencode(q)}")
        for p in page.get("items", []):
            seen += 1
            if p["url"].rsplit("/", 1)[-1] == f"{slug}.html":
                return p
        token = page.get("nextPageToken")
        if not token:
            sys.exit(f"no live post with slug {slug!r} (searched {seen})")


def cmd_whoami(_args):
    b = api(f"/blogs/{BLOG_ID}")
    print(f"blog   : {b['name']}")
    print(f"url    : {b['url']}")
    print(f"posts  : {b['posts']['totalItems']}   pages: {b.get('pages',{}).get('totalItems','?')}")
    print("auth   : OK (a write scope was granted; role must be Admin to edit others' posts)")


def cmd_get(args):
    p = find_post(args.slug)
    full = api(f"/blogs/{BLOG_ID}/posts/{p['id']}")
    body = full.get("content", "")
    print(f"id     : {full['id']}")
    print(f"title  : {full['title']}")
    print(f"url    : {full['url']}")
    print(f"updated: {full['updated']}")
    print(f"bytes  : {len(body):,}")
    if args.out:
        pathlib.Path(args.out).write_text(body, encoding="utf-8")
        print(f"wrote  : {args.out}")


def _flatten_html(raw, limit=None):
    """Strip script/style content, strip remaining tags, collapse whitespace,
    and unescape HTML entities -- reduces markup to the plain text a reader
    actually sees, independent of how tags/entities happen to be arranged.
    Used on both sides of the live-verify substring check (see verify_live):
    a probe built from local source and a probe checked against markup Blogger
    re-renders (re-encoding typographic characters as numeric entities, and
    with tag boundaries in different places) must be flattened the same way
    or a byte-for-byte 'needle in out' check fails on identical content."""
    text = re.sub(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", " ", raw, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(re.sub(r"\s+", " ", text).strip())
    return text[:limit] if limit else text


def verify_live(url, needle=None, absent=None):
    """Independent re-fetch with a cache-buster. The API can accept a write that
    does not render; this is the only check that proves what a reader sees.

    needle/absent are checked both as raw substrings of the fetched HTML and,
    via _flatten_html, as plain text -- the latter catches cases where the
    content is identical but a tag boundary or an HTML-entity re-encoding
    (Blogger converts interpunct, em/en dash etc. to numeric entities on save)
    would otherwise make a literal substring search fail."""
    bust = f"{url}?cb={secrets.randbelow(10**6)}"
    out = subprocess.run(
        ["curl", "-s", "-A", "Mozilla/5.0", bust], capture_output=True, text=True
    ).stdout
    if not out:
        return False, "empty response"
    out_flat = _flatten_html(out)
    if needle and needle not in out and _flatten_html(needle) not in out_flat:
        return False, "expected content missing"
    if absent and (absent in out or _flatten_html(absent) in out_flat):
        return False, "content that should be gone is still present"
    return True, f"{len(out):,} bytes"


def verify_stored(content, probe):
    """Fallback for runners that cannot reach the public blog at all (e.g. a
    sandbox whose egress proxy blocks blogspot.com but allows the API): check
    the probe against the content the API reports as stored. Weaker than
    verify_live -- it proves the write landed, not that the page renders -- so
    it is used only when the live fetch returned nothing, and says so."""
    if _flatten_html(probe) in _flatten_html(content or ""):
        return True, (f"via API, public fetch unavailable from this host "
                      f"({len(content or ''):,} bytes stored)")
    return False, "stored content does not contain the expected text"


def do_update(post_id, url, title, body, published=None, labels=None, dry_run=False):
    if dry_run:
        print(f"    DRY RUN — would PUT {len(body):,} bytes")
        return True
    # posts.update is a PUT, i.e. a whole-resource replace, so anything left out
    # of the payload is in principle up for grabs. In practice Blogger has
    # preserved `published` on every write this archive has made — 104 snapshots
    # and not one re-dating — but "it has not bitten yet" is not a guarantee, and
    # a silently re-dated post is the kind of damage you notice months later.
    # Send the existing date back explicitly so the behaviour is ours, not theirs.
    #
    # `labels` needs the same treatment, and unlike `published` it has actually
    # bitten: an update on 2026-08-11 that omitted labels wiped
    # ai-high-demand-launch-tracker's "AI Tracker" label, while other same-day
    # updates that also omitted labels did not lose theirs -- Blogger's PUT
    # behaviour for omitted array fields is not reliably "leave unchanged", so
    # don't rely on it. Callers must pass the post's current labels through.
    payload = {"id": post_id, "title": title, "content": body}
    if published:
        payload["published"] = published
    if labels:
        payload["labels"] = labels
    api(f"/blogs/{BLOG_ID}/posts/{post_id}", data=payload, method="PUT")
    time.sleep(3)  # give Blogger a moment to render before verifying
    probe = _flatten_html(body, limit=40)
    ok, why = verify_live(url, needle=probe)
    if not ok and why == "empty response":
        got = api(f"/blogs/{BLOG_ID}/posts/{post_id}")
        ok, why = verify_stored(got.get("content"), probe)
    print(f"    {'verified' if ok else 'WROTE BUT VERIFY FAILED'}: {why}")
    return ok


def cmd_update(args):
    body = pathlib.Path(args.file).read_text(encoding="utf-8")
    if args.id:
        # Two live posts can share a slug — Blogger allows it, and the archive
        # then stores one of them under a "<slug>--<id>" filename that matches
        # no live URL. Slug lookup cannot reach that post; its id can.
        p = api(f"/blogs/{BLOG_ID}/posts/{args.id}")
    else:
        p = find_post(args.slug)
    title = args.title or p["title"]
    print(f"{args.slug or args.id}  id={p['id']}")
    if args.title:
        print(f"  title: {p['title']!r}\n      -> {args.title!r}")
    try:
        ok = do_update(p["id"], p["url"], title, body,
                       published=p.get("published"), labels=p.get("labels"),
                       dry_run=args.dry_run)
    except Ceiling as e:
        print(f"daily write ceiling reached: {e}")
        sys.exit(3)
    sys.exit(0 if ok else 2)


def cmd_delete(args):
    """Permanently delete a live post. Requires --yes; without it, prints what
    would be deleted and exits without calling the API. There is no --dry-run
    flag here on purpose — --yes IS the confirmation step, so a bare command
    with neither is the safe default, not an oversight to fix."""
    p = api(f"/blogs/{BLOG_ID}/posts/{args.id}") if args.id else find_post(args.slug)
    print(f"{args.slug or args.id}  id={p['id']}")
    print(f"  title : {p['title']}")
    print(f"  url   : {p['url']}")
    print(f"  status: {p.get('status', 'LIVE')}")
    if not args.yes:
        print("  DRY RUN (default) — pass --yes to actually delete this post")
        return
    api(f"/blogs/{BLOG_ID}/posts/{p['id']}", method="DELETE")
    print("  deleted")


def _title_key(t):
    return re.sub(r"\W+", " ", html.unescape(t or "")).strip().lower()


def live_posts_meta():
    """Every live post's id, title, url and published date (no bodies)."""
    out, token = [], None
    while True:
        q = {"maxResults": 100, "fetchBodies": "false", "status": "LIVE"}
        if token:
            q["pageToken"] = token
        page = api(f"/blogs/{BLOG_ID}/posts?{urllib.parse.urlencode(q)}")
        out += page.get("items", [])
        token = page.get("nextPageToken")
        if not token:
            return out


def cmd_duplicates(args):
    """List titles that are live more than once. With --delete-newer --yes, permanently delete
    every copy except the earliest-published one (its address has no _<digits> suffix)."""
    groups = {}
    for p in live_posts_meta():
        groups.setdefault(_title_key(p["title"]), []).append(p)
    dups = [sorted(g, key=lambda p: p.get("published", "")) for g in groups.values() if len(g) > 1]
    if not dups:
        print("no duplicate titles among live posts")
        return
    for g in dups:
        print(f"\n{g[0]['title']}")
        for i, p in enumerate(g):
            print(f"  {'KEEP  ' if i == 0 else 'DELETE'} id={p['id']}  published {p.get('published', '')[:16]}  {p['url']}")
    if not (args.delete_newer and args.yes):
        print("\nlisted only; pass --delete-newer --yes to delete the copies marked DELETE")
        return
    for g in dups:
        for p in g[1:]:
            api(f"/blogs/{BLOG_ID}/posts/{p['id']}", method="DELETE")
            print(f"  deleted id={p['id']}  {p['url']}")
            time.sleep(WRITE_GAP_SECONDS)


def cmd_insert(args):
    """Create and publish a new post. Blogger's web editor silently stops
    responding under load; posts.insert returns a status code."""
    body = pathlib.Path(args.file).read_text(encoding="utf-8")
    if args.dry_run:
        print(f"DRY RUN — would insert {len(body):,} bytes"
              f"\n  title : {args.title}"
              f"\n  status: {'DRAFT' if args.draft else 'LIVE'}")
        return
    # Refuse a second live post with the same title: re-running an insert (a re-pasted block, or a
    # retry after a timeout that had in fact succeeded) is how duplicate posts with a _<digits>
    # address suffix have appeared. --allow-duplicate overrides.
    same = [p for p in live_posts_meta() if _title_key(p["title"]) == _title_key(args.title)]
    if same and not args.allow_duplicate:
        for p in same:
            print(f"already live: id={p['id']}  {p['url']}  published {p.get('published', '')[:16]}")
        print("not inserted: a live post already has this title (use update to change it, "
              "or --allow-duplicate if a second copy is really wanted)")
        sys.exit(4)
    payload = {"kind": "blogger#post", "title": args.title, "content": body}
    q = "?isDraft=true" if args.draft else ""
    try:
        res = api(f"/blogs/{BLOG_ID}/posts{q}", data=payload, method="POST")
    except Ceiling as e:
        print(f"daily write ceiling reached: {e}")
        sys.exit(3)
    print(f"created id={res['id']}")
    print(f"url     {res.get('url', '(draft — no public URL)')}")
    if args.draft or not res.get("url"):
        return
    time.sleep(4)
    probe = _flatten_html(body, limit=40)
    ok, why = verify_live(res["url"], needle=probe)
    if not ok and why == "empty response":
        ok, why = verify_stored(res.get("content"), probe)
    print(f"    {'verified' if ok else 'PUBLISHED BUT VERIFY FAILED'}: {why}")
    sys.exit(0 if ok else 2)


def cmd_drafts(args):
    """List every draft post; with --out, save each draft's HTML and an index.json there
    so the drafts can be reviewed outside the Blogger dashboard."""
    items, token = [], None
    while True:
        q = {"status": "draft", "fetchBodies": "true" if args.out else "false", "maxResults": 20,
             "view": "ADMIN"}
        if token:
            q["pageToken"] = token
        page = api(f"/blogs/{BLOG_ID}/posts?{urllib.parse.urlencode(q)}")
        items += page.get("items", [])
        token = page.get("nextPageToken")
        if not token:
            break
    out = pathlib.Path(args.out) if args.out else None
    if out:
        out.mkdir(parents=True, exist_ok=True)
    index = []
    for p in sorted(items, key=lambda x: x.get("updated", ""), reverse=True):
        body = p.get("content") or ""
        row = {"id": p["id"], "title": p.get("title", ""), "updated": p.get("updated", ""),
               "published": p.get("published", ""), "labels": p.get("labels", []), "bytes": len(body.encode())}
        index.append(row)
        print(f"  {row['id']}  {row['updated'][:10]}  {row['bytes']:>8,}  {row['title'][:70]}")
        if out:
            (out / f"{p['id']}.html").write_text(body, encoding="utf-8")
    print(f"{len(items)} draft(s)")
    if out:
        (out / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"saved to {out}/")


def cmd_publish_draft(args):
    """Publish an existing draft by id (posts.publish). Use `drafts` to find ids."""
    p = api(f"/blogs/{BLOG_ID}/posts/{args.id}?view=ADMIN")
    if p.get("status") != "DRAFT":
        raise SystemExit(f"{args.id} is {p.get('status')}, not a draft; nothing done")
    print(f"publishing {args.id}: {p.get('title','')}")
    if args.dry_run:
        print("DRY RUN — not published")
        return
    try:
        res = api(f"/blogs/{BLOG_ID}/posts/{args.id}/publish", data={}, method="POST")
    except Ceiling as e:
        print(f"daily write ceiling reached: {e}")
        sys.exit(3)
    print(f"url     {res.get('url', '(no url returned)')}")


def cmd_revert_draft(args):
    """Move live posts back to draft (posts.revert). Content is kept; the public URL stops serving.
    Takes --slug (repeatable) or --file with one slug per line."""
    slugs = list(args.slug or [])
    if args.file:
        slugs += [l.strip() for l in pathlib.Path(args.file).read_text().splitlines() if l.strip() and not l.startswith("#")]
    if not slugs:
        raise SystemExit("give --slug or --file")
    for slug in slugs:
        try:
            p = find_post(slug)
        except SystemExit as e:
            print(f"  skip {slug}: {e}")
            continue
        print(f"  {slug}  id={p['id']}  {p.get('title','')[:60]}")
        if args.dry_run:
            continue
        try:
            api(f"/blogs/{BLOG_ID}/posts/{p['id']}/revert", data={}, method="POST")
        except Ceiling as e:
            print(f"daily write ceiling reached: {e}")
            sys.exit(3)
        print("    reverted to draft")


def cmd_page(args):
    """Create or update a Blogger PAGE. Pages are not part of the post index, so
    a large data table lives here without consuming the homepage render budget
    (see DESIGN_LOG 2026-08-07)."""
    body = pathlib.Path(args.file).read_text(encoding="utf-8")
    if args.dry_run:
        print(f"DRY RUN — would {'update' if args.id else 'create'} page "
              f"{len(body):,} bytes\n  title: {args.title}")
        return
    payload = {"kind": "blogger#page", "title": args.title, "content": body}
    if args.id:
        res = api(f"/blogs/{BLOG_ID}/pages/{args.id}",
                  data={**payload, "id": args.id}, method="PUT")
    else:
        res = api(f"/blogs/{BLOG_ID}/pages", data=payload, method="POST")
    print(f"page id={res['id']}")
    print(f"url    {res.get('url','(draft)')}")
    if res.get("url"):
        time.sleep(4)
        probe = _flatten_html(body, limit=40)
        ok, why = verify_live(res["url"], needle=probe)
        if not ok and why == "empty response":
            ok, why = verify_stored(res.get("content"), probe)
        print(f"    {'verified' if ok else 'WROTE BUT VERIFY FAILED'}: {why}")


def cmd_pages(args):
    res = api(f"/blogs/{BLOG_ID}/pages")
    for p in res.get("items", []):
        print(f"  {p['id']}  {p.get('status','?'):<9} {p['title'][:52]}")
        print(f"      {p.get('url','(no url)')}")


OLD_HOSTS = ("masaladeutsch.blogspot.com",)
NEW_BASE = "https://blog.vertistratsolution.com"


def migrate_links(body):
    """Point every link at the custom domain: https, http and protocol-relative forms,
    a www. prefix, and the bare host in text or JSON."""
    new = body
    for h in OLD_HOSTS:
        new = re.sub(r"(?:https?:)?//(?:www\.)?" + re.escape(h), NEW_BASE, new)
        new = new.replace(h, NEW_BASE.split("//", 1)[1])
    return rebrand(new)


BRAND = "VertiStrat Solutions"


def rebrand(text):
    """Replace the old blog name in visible text with the new brand. Never touches a URL or
    path: herrrickshaw.github.io/masaladeutsch/... (scripts and data the posts load) and the
    the-masala-deutsch-shop-... post address keep working because a name preceded by '/',
    '.', '-' or a word character, or followed by '/', '-', '.<host>' or a word character,
    is left alone."""
    text = re.sub(r"(?<![\w/.\-])Masala[ \u00a0]Deutsch(?![\w/\-])", BRAND, text)
    text = re.sub(r"(?<![\w/.\-])MASALA[ \u00a0]DEUTSCH(?![\w/\-])", BRAND.upper(), text)
    text = re.sub(r"(?<![\w/.\-])masala deutsch(?![\w/\-])", BRAND.lower(), text)
    # the repo/folder name in commands and code spans stays: `cd masaladeutsch`, `masaladeutsch`
    text = re.sub(r"(?<![\w/.\-`])(?<!cd )masaladeutsch(?![\w/\-`])(?!\.(?:blogspot|github))", BRAND, text, flags=re.I)
    return text


def set_h1(body, title):
    """Replace the text of the first <h1> in a post body with the new title, keeping its
    attributes. Returns the body unchanged if the post has no <h1> (the theme shows the
    Blogger title on those)."""
    esc = html.escape(title, quote=False)
    return re.sub(r"(<h1\b[^>]*>).*?(</h1>)", lambda m: m.group(1) + esc + m.group(2), body, count=1, flags=re.S)


def cmd_retitle(args):
    """Apply new titles from a TSV (slug<TAB>title): sets the Blogger title and the first
    <h1> in the body; the post address never changes. Skips posts already titled, so it is
    safe to re-run after the daily write ceiling stops it."""
    want = {}
    for line in pathlib.Path(args.file).read_text(encoding="utf-8").splitlines():
        if "\t" in line and not line.startswith("#"):
            s, t = line.split("\t", 1)
            want[s.strip()] = t.strip()
    live, token = {}, None
    while True:
        q = {"status": "live", "fetchBodies": "true", "maxResults": 20, "view": "ADMIN"}
        if token:
            q["pageToken"] = token
        page = api(f"/blogs/{BLOG_ID}/posts?{urllib.parse.urlencode(q)}")
        for p in page.get("items", []):
            live[p["url"].rsplit("/", 1)[-1][:-5]] = p
        token = page.get("nextPageToken")
        if not token:
            break
    todo, missing = [], [s for s in want if s not in live]
    for s, t in want.items():
        p = live.get(s)
        if not p:
            continue
        body = p.get("content") or ""
        new = migrate_links(set_h1(body, t))
        if p["title"] != t or new != body:
            todo.append((s, p, t, new))
    print(f"{len(want)} titles in {args.file}; {len(todo)} to change; "
          f"{len(want) - len(todo) - len(missing)} already done; {len(missing)} not live (skipped)")
    if args.limit:
        todo = todo[:args.limit]
    done = failed = 0
    try:
        for s, p, t, new in todo:
            print(f"  {s}\n    {p['title'][:100]}\n -> {t}")
            ok = do_update(p["id"], p["url"], t, new, published=p.get("published"),
                           labels=p.get("labels"), dry_run=args.dry_run)
            done += ok
            failed += (not ok)
            if not args.dry_run:
                time.sleep(WRITE_GAP_SECONDS)
    except Ceiling as err:
        print(f"\ndaily write ceiling reached after {done} writes: {err}")
        print("re-run tomorrow: retitled posts are skipped")
        sys.exit(3)
    print(f"\n{'DRY RUN: ' if args.dry_run else ''}{done} retitled, {failed} failed verification")
    sys.exit(0 if not failed else 2)


def cmd_migrate_domain(args):
    """Rewrite masaladeutsch.blogspot.com links to blog.vertistratsolution.com in every
    live post and page (drafts too with --drafts). Each body is read from the API at run
    time, so anything published earlier is kept. Writes only what changed, so it is safe
    to re-run after the daily write ceiling stops it: migrated posts are skipped."""
    todo = []
    for status in ["live"] + (["draft"] if args.drafts else []):
        token = None
        while True:
            q = {"status": status, "fetchBodies": "true", "maxResults": 20, "view": "ADMIN"}
            if token:
                q["pageToken"] = token
            page = api(f"/blogs/{BLOG_ID}/posts?{urllib.parse.urlencode(q)}")
            for p in page.get("items", []):
                body = p.get("content") or ""
                new = migrate_links(body)
                title = rebrand(p.get("title") or "")
                if new != body or title != p.get("title"):
                    p["title"] = title
                    todo.append((status, p, new, sum(body.count(h) for h in OLD_HOSTS)))
            token = page.get("nextPageToken")
            if not token:
                break
    pages = api(f"/blogs/{BLOG_ID}/pages?fetchBodies=true&view=ADMIN").get("items", [])
    page_todo = []
    for p in pages:
        n, title = migrate_links(p.get("content") or ""), rebrand(p.get("title") or "")
        if n != (p.get("content") or "") or title != p.get("title"):
            p["title"] = title
            page_todo.append((p, n))
    # the article index first: every post footer links to it
    todo.sort(key=lambda t: (t[0] != "live",
                             (t[1].get("url") or "").rsplit("/", 1)[-1] != "article-index-start-here.html"))
    print(f"{len(todo)} posts and {len(page_todo)} pages carry old-domain links or the old name "
          f"({sum(t[3] for t in todo):,} links in posts)")
    if args.limit:
        todo = todo[:args.limit]
    done = failed = 0
    try:
        for p, new in page_todo:
            print(f"  page  {p['title'][:70]}")
            if args.dry_run:
                continue
            api(f"/blogs/{BLOG_ID}/pages/{p['id']}",
                data={"kind": "blogger#page", "id": p["id"], "title": p["title"], "content": new}, method="PUT")
            done += 1
            time.sleep(WRITE_GAP_SECONDS)
        for status, p, new, n in todo:
            name = (p.get("url") or p["id"]).rsplit("/", 1)[-1]
            print(f"  {status:<5} {name}  ({n} links)")
            if status == "draft":
                if not args.dry_run:
                    payload = {"id": p["id"], "title": p["title"], "content": new}
                    if p.get("labels"):
                        payload["labels"] = p["labels"]
                    api(f"/blogs/{BLOG_ID}/posts/{p['id']}", data=payload, method="PUT")
                    done += 1
                    time.sleep(WRITE_GAP_SECONDS)
                continue
            ok = do_update(p["id"], p["url"], p["title"], new, published=p.get("published"),
                           labels=p.get("labels"), dry_run=args.dry_run)
            done += ok
            failed += (not ok)
            if not args.dry_run:
                time.sleep(WRITE_GAP_SECONDS)
    except Ceiling as err:
        print(f"\ndaily write ceiling reached after {done} writes: {err}")
        print("re-run tomorrow: migrated posts are skipped")
        sys.exit(3)
    print(f"\n{'DRY RUN: ' if args.dry_run else ''}{done} written, {failed} failed verification")
    sys.exit(0 if not failed else 2)


def cmd_bulk(args):
    entries = json.loads(pathlib.Path(args.manifest).read_text())
    done = failed = 0
    for i, e in enumerate(entries):
        if args.limit and done >= args.limit:
            print(f"\nstopping at --limit {args.limit}; {len(entries)-i} not attempted")
            break
        path = pathlib.Path(e["path"])
        if not path.exists():
            print(f"  skip  {e['slug']}: {path} missing")
            continue
        print(f"[{i+1}/{len(entries)}] {e['slug']}")
        try:
            p = find_post(e["slug"])
        except SystemExit as err:
            print(f"    skip: {err}")
            continue
        try:
            ok = do_update(p["id"], p["url"], p["title"],
                           path.read_text(encoding="utf-8"),
                           published=p.get("published"), labels=p.get("labels"),
                           dry_run=args.dry_run)
        except Ceiling as err:
            print(f"\ndaily write ceiling reached after {done} writes: {err}")
            print("retry tomorrow — backoff will not clear this")
            sys.exit(3)
        done += ok
        failed += (not ok)
        time.sleep(WRITE_GAP_SECONDS)
    print(f"\n{done} updated, {failed} failed")
    sys.exit(0 if not failed else 2)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("auth")
    a.add_argument("--port", type=int, default=0,
                   help=f"loopback port for the OAuth callback (default {DEFAULT_PORT})")
    a.set_defaults(fn=cmd_auth)
    sub.add_parser("whoami").set_defaults(fn=cmd_whoami)

    g = sub.add_parser("get"); g.add_argument("--slug", required=True)
    g.add_argument("--out"); g.set_defaults(fn=cmd_get)

    u = sub.add_parser("update"); u.add_argument("--slug")
    u.add_argument("--id", help="post id; use when two live posts share a slug")
    u.add_argument("--file", required=True); u.add_argument("--dry-run", action="store_true")
    u.add_argument("--title", help="also change the post title (the URL slug is fixed and will not change)")
    u.set_defaults(fn=cmd_update)

    d = sub.add_parser("delete", help="permanently delete a live post")
    d.add_argument("--slug")
    d.add_argument("--id", help="post id; use when two live posts share a slug")
    d.add_argument("--yes", action="store_true",
                   help="actually delete (default is a dry-run preview only)")
    d.set_defaults(fn=cmd_delete)

    i = sub.add_parser("insert", help="create a new post from an HTML file")
    i.add_argument("--file", required=True)
    i.add_argument("--title", required=True)
    i.add_argument("--draft", action="store_true", help="create as a draft")
    i.add_argument("--dry-run", action="store_true")
    i.add_argument("--allow-duplicate", action="store_true", help="insert even if a live post has the same title")
    i.set_defaults(fn=cmd_insert)

    pg = sub.add_parser("page", help="create or update a Blogger page")
    pg.add_argument("--file", required=True); pg.add_argument("--title", required=True)
    pg.add_argument("--id", help="update this page instead of creating one")
    pg.add_argument("--dry-run", action="store_true"); pg.set_defaults(fn=cmd_page)
    sub.add_parser("pages", help="list pages").set_defaults(fn=cmd_pages)
    dr = sub.add_parser("drafts", help="list draft posts; --out DIR saves each draft's HTML + index.json")
    dr.add_argument("--out"); dr.set_defaults(fn=cmd_drafts)
    pd = sub.add_parser("publish-draft", help="publish an existing draft by id")
    pd.add_argument("--id", required=True); pd.add_argument("--dry-run", action="store_true")
    pd.set_defaults(fn=cmd_publish_draft)
    rv = sub.add_parser("revert-draft", help="move live posts back to draft (unpublish, content kept)")
    rv.add_argument("--slug", action="append"); rv.add_argument("--file", help="one slug per line")
    rv.add_argument("--dry-run", action="store_true"); rv.set_defaults(fn=cmd_revert_draft)

    md = sub.add_parser("migrate-domain", help="rewrite masaladeutsch.blogspot.com links to the custom domain and the "
                        "old blog name to VertiStrat Solutions in every live post and page (re-runnable)")
    md.add_argument("--drafts", action="store_true", help="also rewrite draft posts")
    md.add_argument("--limit", type=int, default=0, help="write at most N posts this run")
    md.add_argument("--dry-run", action="store_true"); md.set_defaults(fn=cmd_migrate_domain)

    du = sub.add_parser("duplicates", help="list titles live more than once; --delete-newer --yes removes later copies")
    du.add_argument("--delete-newer", action="store_true"); du.add_argument("--yes", action="store_true")
    du.set_defaults(fn=cmd_duplicates)

    rt = sub.add_parser("retitle", help="apply new titles from a slug<TAB>title file (Blogger title and body h1)")
    rt.add_argument("--file", required=True); rt.add_argument("--limit", type=int, default=0)
    rt.add_argument("--dry-run", action="store_true"); rt.set_defaults(fn=cmd_retitle)

    b = sub.add_parser("bulk"); b.add_argument("--manifest", required=True)
    b.add_argument("--limit", type=int, default=0)
    b.add_argument("--dry-run", action="store_true"); b.set_defaults(fn=cmd_bulk)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

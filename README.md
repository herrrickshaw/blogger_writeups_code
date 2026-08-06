# masaladeutsch archive

Version history for [masaladeutsch.blogspot.com](https://masaladeutsch.blogspot.com).
Blogger keeps no usable revision history, so this repo is the only way to see what
a post used to say — or to put it back.

```
posts/<slug>.html      full post body, exactly as Blogger serves it
meta/<slug>.json       id, title, url, dates, labels, size, sha256, design markers
meta/manifest.json     the whole blog at the last snapshot
CHANGELOG.md           one entry per snapshot: added / changed / unpublished
DESIGN_LOG.md          house style decisions and why, including rejected options
templates/             the post skeleton every new article starts from
tools/snapshot.py      pull the blog and commit the diff
```

## Take a snapshot

```bash
python3 ~/masaladeutsch-archive/tools/snapshot.py --note "why you ran this" --push
```

Remote: `herrrickshaw/blogger_writeups_code` (**private** — this mirrors the whole
blog, so keep it that way). Drop `--push` to commit locally only.

Reads the Blogger public feed (full bodies, no auth), rewrites `posts/` and
`meta/`, appends to `CHANGELOG.md`, and commits. Run it before and after any
editing session. It refuses to write if the feed comes back empty, so a network
failure can't be recorded as the blog being wiped.

## See what changed

```bash
git -C ~/masaladeutsch-archive log --oneline
git -C ~/masaladeutsch-archive log -p --follow posts/<slug>.html   # one post over time
git -C ~/masaladeutsch-archive diff HEAD~1 -- meta/                # marker flips only
```

`meta/*.json` is the fast read: an unwanted design change shows up as a boolean
flip (`light_lock: true → false`) even when the prose is identical.

## Revert a post

```bash
git -C ~/masaladeutsch-archive show <commit>:posts/<slug>.html > /tmp/restore.html
```

Then serve `/tmp/` over the local CORS helper and paste it into the Blogger editor
the usual way — fetch it into the CodeMirror instance, dirty the editor, Update.
The recipe, including the coordinates that actually work, is in the
`blogger-editor-save-recipe` memory. Verify with `curl` and a cache-buster; never
trust the editor UI.

## Drafts and deletions

The public feed carries published posts only. A post that is drafted or deleted
disappears from the feed and is logged as **no longer published** — the snapshot
cannot tell those two apart, and its file stays in `posts/` rather than being
removed.

Before drafting or deleting anything deliberately, capture it first: open the post
in the Blogger editor and POST the CodeMirror contents to a local sink, then save
it as `posts/_drafted-<slug>.html` so the archive keeps a copy under a name the
snapshot won't overwrite.

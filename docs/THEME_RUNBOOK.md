# Theme runbook: build and upload the whole theme

The theme is kept in two parts and built into one upload file:

| File | What it is |
|---|---|
| `theme/base.xml` | The live theme with no modules in it: Blogger's widgets, gadgets and settings as last backed up. |
| `theme/modules.json` | The modules, in order. Each is a CSS or JS file under `templates/`, or a `scope` rule. |
| `theme/theme.xml` | The built file: base + every module. This is what you upload. |
| `tools/theme_build.py` | The builder. |

Modules are wrapped in `BEGIN/END theme-module` markers. The builder can therefore remove them from any backup and put the current versions back. It also removes the unmarked copies pasted by hand from `docs/THEME_PATCH_2026-10-26_tables.md`.

## Upload the theme (every time)

1. In Blogger, open **Theme** and click the **down arrow next to Customise**, then **Backup**. Download the file; it lands in `~/Downloads` as `theme-<number>.xml`. This is also your rollback copy.
2. Build from that backup, so any change made in Blogger since the last backup is kept:
   ```zsh
   cd /Users/umashankar/masaladeutsch-archive
   git pull -q origin main
   python3 tools/theme_build.py --base latest
   ```
   The builder prints which modules it removed from the backup. It also says whether the live theme changed since `theme/base.xml` was saved; those changes are kept. It refuses to write a file that is not well-formed XML, the error Blogger reports as `SAXParseException`.
3. Blogger: **Theme > down arrow > Restore > Upload**, and choose `theme/theme.xml` from the archive folder. If Blogger asks about widgets that are not in the new theme, choose **Keep widgets**.
4. Check one post with a table and the homepage on a phone.
5. Commit the new base so the repo matches the live theme:
   ```zsh
   cd /Users/umashankar/masaladeutsch-archive
   git add theme/base.xml theme/theme.xml && git commit -qm "Theme: base refreshed from live backup" && git push -q origin main
   ```

**Rollback:** Restore the backup file from step 1.

## Change a module

Edit its file under `templates/`, then run the steps above. To add a module, create the file and add an entry to `theme/modules.json`:
- `kind: css` goes before `]]></b:skin>`;
- `kind: js` is wrapped in a CDATA script before the final `</body>`;
- `kind: scope` takes `"classes": [...]` and limits theme rules for those classes to outside posts.

To replace a module, keep the old entry with `"retired": true`, so the builder still removes it from backups.

`python3 tools/theme_build.py --check` tells you whether `theme/theme.xml` is up to date with the modules.

## Current modules (26 Oct 2026)

See `out/research/theme-audit-2026-10-26.md` for what each fixes and the before/after numbers.
- `gs-scope-chrome-v1`: the homepage's `.hero`, `.card` and `.wrap` styles no longer apply inside posts.
- `gs-table-template-v1`: one readable table style; empty ad boxes collapse.
- `gs-readable-v1`: line length, long links, note and ad-label contrast, section-link offset, nav tap targets.
- `gs-content-guard-v2`: wraps tables, moves Auto-ads containers out of tables, lists, figures, side-by-side layouts, scroll boxes and boxed notes, and off headings.
- `gs-table-guard-v1`: retired (replaced by v2).

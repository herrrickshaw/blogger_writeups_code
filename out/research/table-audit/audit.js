const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const R = '/home/user/blogger_writeups_code';
const theme = fs.readFileSync(R + '/theme/theme.xml', 'utf8');
const skin = theme.slice(theme.indexOf('<b:skin><![CDATA[') + 17, theme.indexOf(']]></b:skin>'));
const js = fs.readFileSync(R + '/templates/gs-table-guard-v1.js', 'utf8');
const slugs = fs.readFileSync(process.argv[2], 'utf8').trim().split('\n');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell' });
  const out = fs.createWriteStream(process.argv[3]);
  for (const slug of slugs) {
    const post = fs.readFileSync(`${R}/posts/${slug}.html`, 'utf8');
    const page = `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>${skin}</style></head><body><div id="Blog1"><div class="post-body">${post}</div></div><script>${js}</script></body></html>`;
    const file = `/tmp/claude-0/-home-user--github/bf61733e-4e03-51c3-9ac3-07a35af41a6a/scratchpad/tblaudit/p.html`;
    fs.writeFileSync(file, page);
    for (const w of [375, 1024]) {
      const p = await b.newPage({ viewport: { width: w, height: 900 } });
      const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 80)));
      await p.route('**/*', r => r.request().url().startsWith('file:') ? r.continue() : r.abort());
      try { await p.goto('file://' + file, { waitUntil: 'load', timeout: 20000 }); } catch (e) { errs.push('load:' + e.message.slice(0, 60)); }
      await p.waitForTimeout(150);
      const res = await p.evaluate(() => {
        const vw = document.documentElement.clientWidth;
        const pageOverflow = document.documentElement.scrollWidth - vw;
        return { pageOverflow, tables: [...document.querySelectorAll('.post-body table')].map((t, i) => {
          const rows = [...t.rows];
          const widths = rows.map(r => [...r.cells].reduce((a, c) => a + (c.colSpan || 1), 0));
          const maxw = Math.max(0, ...widths);
          const ragged = widths.filter(x => x !== maxw).length;
          const cells = rows.flatMap(r => [...r.cells]);
          const empty = cells.filter(c => !c.textContent.trim() && !c.querySelector('img,svg')).length;
          const longest = Math.max(0, ...cells.map(c => c.textContent.trim().length));
          const hasHead = !!t.tHead || (rows[0] && [...rows[0].cells].every(c => c.tagName === 'TH'));
          const wrap = t.closest('.gs-tblwrap,.gb-tblwrap,.tw');
          const tr = t.getBoundingClientRect();
          const scrolls = wrap ? wrap.scrollWidth - wrap.clientWidth > 2 : false;
          let minCol = 9999; if (rows.length) { const r = rows.reduce((a, b) => b.cells.length > a.cells.length ? b : a, rows[0]); for (const c of r.cells) minCol = Math.min(minCol, c.getBoundingClientRect().width); }
          const tallRow = Math.max(0, ...rows.map(r => r.getBoundingClientRect().height));
          const nested = !!t.querySelector('table');
          const stray = [...t.querySelectorAll('tr > :not(td):not(th)')].length;
          const first = (t.caption ? t.caption.textContent : (rows[0] ? rows[0].textContent : '')).trim().replace(/\s+/g, ' ').slice(0, 70);
          return { i, rows: rows.length, cols: maxw, ragged, empty, cells: cells.length, longest, hasHead, wrapped: !!wrap, scrolls,
                   width: Math.round(tr.width), wrapW: wrap ? Math.round(wrap.getBoundingClientRect().width) : null, right: Math.round(tr.right), minCol: Math.round(minCol), tallRow: Math.round(tallRow), nested, stray, first };
        }) };
      });
      out.write(JSON.stringify({ slug, w, errs: errs.length, ...res }) + '\n');
      await p.close();
    }
  }
  out.end(); await b.close();
})();

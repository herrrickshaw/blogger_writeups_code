#!/usr/bin/env node
/* Contact sheet for the driver's manual read: every chart of one or more editions at 375px, side by side in one image.
     node tools/viz_sheet.js out.png edition.html [edition2.html ...]     (one image to read per call) */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const [out, ...files] = process.argv.slice(2);
(async () => {
  const t = fs.readFileSync(path.join(ROOT, 'theme/theme.xml'), 'utf8');
  const un = (s) => s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&amp;/g, '&');
  const css = un(((t.match(/<b:skin[^>]*><!\[CDATA\[([\s\S]*?)\]\]><\/b:skin>/) || [, ''])[1]).replace(/\$\([^)]*\)/g, 'inherit'));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 375, height: 900 } });
  await p.route('**/*', (r) => r.abort());
  const shots = [];
  for (const f of files) {
    await p.setContent('<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><style>body{margin:0;padding:0 16px;background:#fff}' + css + '</style><div id=Blog1><div class="post-body entry-content">' + fs.readFileSync(f, 'utf8') + '</div></div>', { waitUntil: 'load' });
    for (const e of await p.$$('figure.xv,.xv-flow')) shots.push((await e.screenshot()).toString('base64'));
  }
  await b.close();
  const b2 = await chromium.launch();
  const q = await b2.newPage({ viewport: { width: 1600, height: 600 } });
  await q.setContent('<body style="margin:0;background:#fff;display:flex;flex-wrap:wrap;gap:8px;align-items:flex-start;width:1560px">' + shots.map((s) => '<img style="border:1px solid #ddd" src="data:image/png;base64,' + s + '">').join('') + '</body>');
  await q.screenshot({ path: out, fullPage: true });
  await b2.close();
  console.log(shots.length + ' charts -> ' + out);
})();

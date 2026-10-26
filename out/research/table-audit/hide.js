const { chromium } = require('playwright'); const fs=require('fs'); const R='/home/user/blogger_writeups_code';
const theme=fs.readFileSync(R+'/theme/theme.xml','utf8'); const skin=theme.slice(theme.indexOf('<b:skin><![CDATA[')+17, theme.indexOf(']]></b:skin>'));
const js=fs.readFileSync(R+'/templates/gs-table-guard-v1.js','utf8');
(async()=>{ const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell'});
for (const slug of process.argv.slice(2)) { const post=fs.readFileSync(`${R}/posts/${slug}.html`,'utf8');
 const f=process.cwd()+'/w.html'; fs.writeFileSync(f,`<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>${skin}</style></head><body><div id="Blog1"><div class="post-body">${post}</div></div><script>${js}</script></body></html>`);
 const p=await b.newPage({viewport:{width:375,height:900}}); await p.route('**/*', r => r.request().url().startsWith('file:') ? r.continue() : r.abort());
 await p.goto('file://'+f,{waitUntil:'load'}); await p.waitForTimeout(150);
 console.log(slug, await p.evaluate(()=>{ const d=document.documentElement; const a=d.scrollWidth-d.clientWidth;
   const ws=[...document.querySelectorAll('.post-body table')].map(t=>t.closest('.gs-tblwrap,.gb-tblwrap,.tw')||t); ws.forEach(w=>w.style.display='none');
   const bb=d.scrollWidth-d.clientWidth; ws.forEach(w=>w.style.display='');
   let worst=null; for (const el of document.querySelectorAll('.post-body *')) { if (el.closest('table')) continue; const cs=getComputedStyle(el); if (cs.overflowX==='visible' && el.scrollWidth>el.clientWidth+20 && el.clientWidth>0 && (!worst||el.scrollWidth-el.clientWidth>worst[1])) worst=[el.tagName+'.'+el.className, el.scrollWidth-el.clientWidth]; }
   return 'withTables='+a+' tablesHidden='+bb+' worstNonTable='+JSON.stringify(worst); }));
 await p.close(); } await b.close(); })();

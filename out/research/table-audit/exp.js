const { chromium } = require('playwright'); const fs=require('fs');
const R='/home/user/blogger_writeups_code';
const variants = JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const slugs = process.argv.slice(3);
(async()=>{ const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell'});
 const theme=fs.readFileSync(R+'/theme/theme.xml','utf8'); let skin=theme.slice(theme.indexOf('<b:skin><![CDATA[')+17, theme.indexOf(']]></b:skin>'));
 const old=fs.readFileSync('theme_old.xml','utf8'); const oskin=old.slice(old.indexOf('<b:skin><![CDATA[')+17, old.indexOf(']]></b:skin>'));
 const js=fs.readFileSync(R+'/templates/gs-table-guard-v1.js','utf8');
 for (const slug of slugs){ const post=fs.readFileSync(`${R}/posts/${slug}.html`,'utf8'); const row=[slug.slice(0,30)];
  for (const [name,[sk,j]] of Object.entries({old:[oskin,''], ...Object.fromEntries(Object.entries(variants).map(([k,v])=>[k,[v.replace? skin.replace(v.find,v.replace):skin+v.add, js]]))})) {
   const f=process.cwd()+'/e.html'; fs.writeFileSync(f,`<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>${sk}</style></head><body><div id="Blog1"><div class="post-body">${post}</div></div><script>${j}</script></body></html>`);
   const p=await b.newPage({viewport:{width:375,height:900}}); await p.route('**/*', r => r.request().url().startsWith('file:') ? r.continue() : r.abort());
   await p.goto('file://'+f,{waitUntil:'load'}); await p.waitForTimeout(120);
   row.push(name+'='+await p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth)); await p.close(); }
  console.log(row.join('  ')); }
 await b.close(); })();

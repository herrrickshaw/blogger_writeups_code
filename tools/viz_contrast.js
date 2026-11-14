const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path'); const glob=fs.readdirSync('out/viz').filter(s=>fs.existsSync(`out/viz/${s}/edition.html`));
const t=fs.readFileSync('theme/theme.xml','utf8'); const un=s=>s.replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/&amp;/g,'&');
const css=un(((t.match(/<b:skin[^>]*><!\[CDATA\[([\s\S]*?)\]\]><\/b:skin>/)||[,''])[1]).replace(/\$\([^)]*\)/g,'inherit'));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:375,height:900}});await p.route('**/*',r=>r.abort());const bad=[];
for(const s of glob){await p.setContent('<!doctype html><style>body{margin:0;padding:0 16px;background:#fff}'+css+'</style><div id=Blog1><div class="post-body entry-content">'+fs.readFileSync(`out/viz/${s}/edition.html`,'utf8')+'</div></div>',{waitUntil:'load'});
const r=await p.evaluate(()=>{const lum=c=>{const m=c.match(/[\d.]+/g).map(Number);const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(m[0])+.7152*f(m[1])+.0722*f(m[2])};
const bg=e=>{while(e){const c=getComputedStyle(e).backgroundColor;const m=c.match(/[\d.]+/g);if(m&&(m.length<4||+m[3]>0.5))return c;e=e.parentElement}return 'rgb(255,255,255)'};
let worst=21;for(const e of document.querySelectorAll('figure.xv *, .xv-top *, .xv-so *, .xv-sec h2')){if(!e.childNodes.length||![...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim()))continue;const a=lum(getComputedStyle(e).color),c=lum(bg(e));const k=(Math.max(a,c)+.05)/(Math.min(a,c)+.05);if(k<worst)worst=k}return worst});
if(r<4.5)bad.push([s,r.toFixed(2)])}
console.log(glob.length+' editions; low contrast:',JSON.stringify(bad));await b.close()})();

// Print the complete repository SVGs to vector PDFs. Never replace the originals.
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
let playwright;
try { playwright = require('playwright'); }
catch {
  playwright = require(path.join(os.homedir(), '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
}
async function main() {
  const root=path.resolve(__dirname,'..');
  const output=path.resolve(root,'../tmp/pdfs/diagrams');
  fs.mkdirSync(output,{recursive:true});
  const browser=await playwright.chromium.launch({channel:'chrome',headless:true});
  try {
    const page=await browser.newPage();
    for(const name of ['architecture','nightly-data-flow','valuation-chain','memo-pipeline','milestone-map']) {
      const src=path.join(root,'diagrams',name+'.svg');
      const dst=path.join(output,name+'.pdf');
      if(fs.existsSync(dst)&&fs.statSync(dst).mtimeMs>=fs.statSync(src).mtimeMs) continue;
      const svg=fs.readFileSync(src,'utf8');
      const m=svg.match(/viewBox="([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)"/);
      if(!m)throw new Error('Missing SVG viewBox: '+name);
      const w=Number(m[3]), h=Number(m[4]);
      await page.setContent(`<style>@page{size:${w}px ${h}px;margin:0}html,body{margin:0;padding:0}svg{display:block;width:${w}px;height:${h}px}</style>${svg}`);
      await page.pdf({path:dst,width:w+'px',height:h+'px',margin:{top:0,right:0,bottom:0,left:0},printBackground:true,preferCSSPageSize:true});
      console.log('rendered full vector diagram: '+name);
    }
  } finally {await browser.close();}
}
main().catch(error=>{console.error(error);process.exitCode=1;});

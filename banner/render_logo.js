const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const url = 'file://' + path.resolve(__dirname, 'logo_banner.html');
  const p = await b.newPage({ viewport: { width: 1200, height: 800 }, deviceScaleFactor: 2 });
  await p.goto(url); await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: 'arohak_logo_banner_preview.png' });
  const q = await b.newPage();
  await q.goto(url); await q.evaluate(() => { document.body.classList.add('print'); return document.fonts.ready; });
  await q.pdf({ path: 'arohak_logo_banner_3x2ft.pdf', width: '36in', height: '24in', printBackground: true, pageRanges: '1' });
  await b.close();
})();

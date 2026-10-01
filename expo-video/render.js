// Usage: node render.js stills  |  node render.js video [fps]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const FFMPEG = process.env.FFMPEG;
(async () => {
  const mode = process.argv[2] || 'stills';
  const fps = +(process.argv[3] || 30);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file://' + path.resolve(__dirname, 'scene.html'));
  await page.waitForFunction(() => window.READY);
  const grab = async t => {
    const b64 = await page.evaluate(t => { window.render(t); return document.getElementById('c').toDataURL('image/png').split(',')[1]; }, t);
    return Buffer.from(b64, 'base64');
  };
  if (mode === 'stills') {
    const fs = require('fs'); fs.mkdirSync('stills', { recursive: true });
    for (const t of (process.argv[3] || '4,14,22,28,34,41,55,60,68,79,87').split(',').map(Number))
      fs.writeFileSync(`stills/t${t}.png`, await grab(t));
  } else {
    const dur = await page.evaluate(() => window.DURATION);
    const ff = spawn(FFMPEG, ['-y', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-',
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-movflags', '+faststart',
      'arohak_quantum_expo.mp4'], { stdio: ['pipe', 'inherit', 'inherit'] });
    const n = Math.round(dur * fps);
    for (let i = 0; i < n; i++) {
      const buf = await grab(i / fps);
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (i % 300 === 0) console.error(`frame ${i}/${n}`);
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
  }
  await browser.close();
})();

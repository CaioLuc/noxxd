// Grava index.html quadro a quadro e codifica o MP4 com a trilha.
// Uso: node render.mjs            -> caritas-promo.mp4
//      node render.mjs stills 3 12.9 ...  -> stills/t<seg>.jpg (inspeção)
import puppeteer from 'puppeteer-core';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
import {mkdirSync, writeFileSync} from 'node:fs';
import {pathToFileURL, fileURLToPath} from 'node:url';
import {dirname, join} from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const FPS = +(process.env.FPS || 60), DUR = 50, W = 1920, H = 1080;
const CHROME = process.env.CHROME || 'C:/Program Files/Google/Chrome/Application/chrome.exe';

const browser = await puppeteer.launch({executablePath: CHROME, headless: true, args: ['--hide-scrollbars', '--force-color-profile=srgb']});
const page = await browser.newPage();
await page.setViewport({width: W, height: H, deviceScaleFactor: 1});
page.on('pageerror', e => console.error('page error:', e.message));
await page.goto(pathToFileURL(join(here, 'index.html')).href, {waitUntil: 'networkidle0'});
await page.waitForFunction('window.ready === true', {timeout: 60000});

if (process.argv[2] === 'stills') {
  mkdirSync(join(here, 'stills'), {recursive: true});
  for (const t of process.argv.slice(3).map(Number)) {
    await page.evaluate(t => seek(t), t);
    writeFileSync(join(here, 'stills', `t${t}.jpg`), await page.screenshot({type: 'jpeg', quality: 85}));
  }
} else {
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-i', join(here, 'soundtrack.wav'), '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '192k', '-t', String(DUR), '-movflags', '+faststart', join(here, 'caritas-promo.mp4')], {stdio: ['pipe', 'inherit', 'inherit']});
  const t0 = Date.now();
  for (let f = 0; f < FPS * DUR; f++) {
    await page.evaluate(t => seek(t), f / FPS);
    if (!ff.stdin.write(await page.screenshot({type: 'jpeg', quality: 95}))) await once(ff.stdin, 'drain');
    if (f % (FPS * 5) === 0) console.log(`${(f / FPS).toFixed(0)}s  (${((Date.now() - t0) / 1000).toFixed(0)}s elapsed)`);
  }
  ff.stdin.end();
  const [code] = await once(ff, 'close');
  if (code) throw new Error('ffmpeg exit ' + code);
  console.log('ok caritas-promo.mp4');
}
await browser.close();

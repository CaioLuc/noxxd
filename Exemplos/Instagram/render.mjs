// Exporta cada <section class="post"> de index.html como PNG 1080×1350 em posts/.
// Usa o puppeteer-core já instalado em ../Caritas/motion (node render.mjs).
import {createRequire} from 'node:module';
import {mkdirSync} from 'node:fs';
import {pathToFileURL, fileURLToPath} from 'node:url';
import {dirname, join} from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const puppeteer = createRequire(join(here, '../Caritas/motion/package.json'))('puppeteer-core');
const browser = await puppeteer.launch({executablePath: process.env.CHROME || 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: true, args: ['--force-color-profile=srgb']});
const page = await browser.newPage();
await page.setViewport({width: 1160, height: 1430, deviceScaleFactor: 1});
page.on('pageerror', e => console.error('page error:', e.message));
await page.goto(pathToFileURL(join(here, 'index.html')).href, {waitUntil: 'networkidle0'});
await page.waitForFunction('window.ready === true', {timeout: 60000});
mkdirSync(join(here, 'posts'), {recursive: true});
for (const el of await page.$$('section.post')) {
  const name = await el.evaluate(e => e.dataset.name);
  await el.screenshot({path: join(here, 'posts', name + '.png')});
  console.log('ok', name);
}
await browser.close();

// Writes each page's Portuguese HTML into dist/ so crawlers and link previews see the content without JS.
import { readFileSync, writeFileSync } from 'node:fs'
import { createElement } from 'react'
import { renderToString } from 'react-dom/server'
import { createServer } from 'vite'

const vite = await createServer({ server: { middlewareMode: true }, appType: 'custom', logLevel: 'error' })
try {
  const { LangProvider } = await vite.ssrLoadModule('/src/lang.jsx')
  // Build input names match the page modules: home -> src/pages/home.jsx
  for (const [page, html] of Object.entries(vite.config.build.rollupOptions.input)) {
    const { default: Page } = await vite.ssrLoadModule(`/src/pages/${page}.jsx`)
    const body = renderToString(createElement(LangProvider, null, createElement(Page)))
    if (!body.includes('<h1')) throw new Error(`${html}: prerender produced no <h1>`)
    const file = `dist/${html}`
    const out = readFileSync(file, 'utf8').replace('<div id="root"></div>', () => `<div id="root">${body}</div>`)
    if (!out.includes(body)) throw new Error(`${file}: no empty #root to fill`)
    writeFileSync(file, out)
  }
} finally {
  await vite.close()
}

import { StrictMode } from 'react'
import { createRoot, hydrateRoot } from 'react-dom/client'
import { LangProvider, readSaved } from './lang.jsx'
import './styles.css'

export function mount(Page) {
  if (import.meta.env.SSR) return // scripts/prerender.mjs renders the page itself
  const root = document.getElementById('root')
  const app = (
    <StrictMode>
      <LangProvider>
        <Page />
      </LangProvider>
    </StrictMode>
  )
  // The prerendered HTML is Portuguese: English visitors get a fresh render instead of a mismatched hydrate.
  if (root.firstElementChild && readSaved() === 'pt') hydrateRoot(root, app)
  else createRoot(root).render(app)
}

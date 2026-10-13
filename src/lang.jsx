import { createContext, useContext, useEffect, useState } from 'react'

const LangContext = createContext({ lang: 'pt', setLang() {}, t: (pt) => pt })

// Read once at import, before any effect renames the tab; absent during the build-time prerender.
const titles = typeof document === 'undefined' ? null : { pt: document.title, en: document.documentElement.dataset.titleEn || document.title }

export const readSaved = () => {
  try {
    return localStorage.getItem('noxxd_lang') === 'en' ? 'en' : 'pt'
  } catch {
    return 'pt' // storage blocked: Portuguese is the default
  }
}

// PT/EN shared by every page through localStorage "noxxd_lang". Titles come from each HTML file.
export function LangProvider({ children }) {
  const [lang, setLang] = useState(readSaved)

  useEffect(() => {
    document.documentElement.lang = lang === 'en' ? 'en' : 'pt-BR'
    document.documentElement.removeAttribute('data-wait') // set by the inline script in each HTML head
    document.title = titles[lang]
    try {
      localStorage.setItem('noxxd_lang', lang)
    } catch {
      // storage blocked: the choice lasts for this page view
    }
  }, [lang])

  const t = (pt, en) => (lang === 'en' ? en : pt)
  return <LangContext.Provider value={{ lang, setLang, t }}>{children}</LangContext.Provider>
}

export const useLang = () => useContext(LangContext)

export function T({ pt, en }) {
  return useLang().t(pt, en)
}

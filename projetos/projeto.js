/**
 * NOXXD — project pages: PT/EN switch shared with the Home (localStorage "noxxd_lang").
 * Loaded in <head> without defer so the saved language applies before first paint.
 */

'use strict';

(() => {
  const root = document.documentElement;
  const titles = { pt: document.title, en: root.dataset.titleEn || document.title };

  const applyLanguage = (lang) => {
    const selected = lang === 'en' ? 'en' : 'pt';
    root.lang = selected === 'en' ? 'en' : 'pt-BR';
    document.title = titles[selected];
    document.querySelectorAll('.lang-btn').forEach((btn) => {
      btn.setAttribute('aria-pressed', String(btn.dataset.lang === selected));
    });
    try {
      localStorage.setItem('noxxd_lang', selected);
    } catch {
      // Storage blocked: the choice simply lasts for this page view
    }
  };

  let saved = 'pt';
  try {
    saved = localStorage.getItem('noxxd_lang') || 'pt';
  } catch {
    saved = 'pt';
  }
  applyLanguage(saved);

  document.addEventListener('DOMContentLoaded', () => {
    applyLanguage(root.lang === 'en' ? 'en' : 'pt');
    document.querySelectorAll('.lang-btn').forEach((btn) => {
      btn.addEventListener('click', () => applyLanguage(btn.dataset.lang));
    });
  });
})();

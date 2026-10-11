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

    const calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Tilted screenshot frames, fine pointers only
    if (!calm && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      document.querySelectorAll('.shot__device').forEach((frame) => {
        frame.addEventListener('pointermove', (event) => {
          const r = frame.getBoundingClientRect();
          const x = (event.clientX - r.left) / r.width - 0.5;
          const y = (event.clientY - r.top) / r.height - 0.5;
          frame.style.setProperty('--ry', `${(x * 8).toFixed(2)}deg`);
          frame.style.setProperty('--rx', `${(-y * 6).toFixed(2)}deg`);
        });
        frame.addEventListener('pointerleave', () => {
          frame.style.removeProperty('--rx');
          frame.style.removeProperty('--ry');
        });
      });
    }

    // Blur-in headline: each word settles in turn ([data-blur-words])
    document.querySelectorAll('[data-blur-words]').forEach((el) => {
      let i = 0;
      const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      const nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);
      nodes.forEach((node) => {
        const frag = document.createDocumentFragment();
        node.textContent.split(/(\s+)/).forEach((part) => {
          if (!part.trim()) {
            frag.append(part);
            return;
          }
          const word = document.createElement('span');
          word.className = 'blur-word';
          word.style.setProperty('--i', i++);
          word.textContent = part;
          frag.append(word);
        });
        node.replaceWith(frag);
      });
    });

    // Command palette demo ([data-palette]): live filter, Ctrl/Cmd+K focuses the field
    document.querySelectorAll('[data-palette]').forEach((box) => {
      const input = box.querySelector('input');
      const items = [...box.querySelectorAll('li')];
      const empty = box.querySelector('[data-palette-empty]');
      const norm = (t) => t.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
      input.addEventListener('input', () => {
        const q = norm(input.value.trim());
        let shown = 0;
        items.forEach((item) => {
          const hit = !q || norm(item.textContent).includes(q);
          item.hidden = !hit;
          shown += hit;
        });
        empty.hidden = shown > 0;
      });
      document.addEventListener('keydown', (event) => {
        if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
          event.preventDefault();
          input.focus();
        }
      });
    });

    // Booking slots demo ([data-booking]): pick a slot, send the request
    document.querySelectorAll('[data-booking]').forEach((form) => {
      const done = form.querySelector('[data-booking-done]');
      form.addEventListener('change', () => {
        form.querySelector('button').disabled = !form.querySelector('input:checked');
      });
      form.addEventListener('submit', (event) => {
        event.preventDefault();
        done.hidden = false;
      });
    });
  });
})();

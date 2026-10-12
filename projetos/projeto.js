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

    // Reading progress bar
    const bar = document.createElement('div');
    bar.className = 'p-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.prepend(bar);
    let ticking = false;
    const paint = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.setProperty('--progress', max > 0 ? (window.scrollY / max).toFixed(4) : 0);
      ticking = false;
    };
    window.addEventListener('scroll', () => {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(paint);
      }
    }, { passive: true });
    paint();

    // Magnetic primary buttons, fine pointers only
    if (!calm && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      document.querySelectorAll('.p-btn').forEach((btn) => {
        btn.addEventListener('pointermove', (event) => {
          const r = btn.getBoundingClientRect();
          btn.style.setProperty('--bx', `${((event.clientX - r.left - r.width / 2) * 0.18).toFixed(1)}px`);
          btn.style.setProperty('--by', `${((event.clientY - r.top - r.height / 2) * 0.25).toFixed(1)}px`);
        });
        btn.addEventListener('pointerleave', () => {
          btn.style.removeProperty('--bx');
          btn.style.removeProperty('--by');
        });
      });
    }

    // Count-up facts ([data-count]); the final value is already in the HTML
    const counters = document.querySelectorAll('[data-count]');
    if (!calm && 'IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          io.unobserve(entry.target);
          const el = entry.target;
          const end = parseFloat(el.dataset.count);
          const decimals = +(el.dataset.decimals || 0);
          const locale = root.lang === 'en' ? 'en' : 'pt-BR';
          const fmt = (v) => v.toLocaleString(locale, { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
          const t0 = performance.now();
          const step = (now) => {
            const k = Math.min(1, (now - t0) / 1200);
            el.textContent = fmt(end * (1 - Math.pow(1 - k, 3)));
            if (k < 1) requestAnimationFrame(step);
          };
          requestAnimationFrame(step);
        });
      }, { threshold: 0.6 });
      counters.forEach((el) => io.observe(el));
    }

    // Animated alert feed ([data-feed]): newest item slides in on top
    document.querySelectorAll('[data-feed]').forEach((list) => {
      if (calm) return;
      setInterval(() => {
        const last = list.lastElementChild;
        last.classList.remove('is-new');
        list.prepend(last);
        void last.offsetWidth; // restart the entrance animation
        last.classList.add('is-new');
      }, 2400);
    });

    // Typing AI summary ([data-type]): each language span types its own text once visible
    document.querySelectorAll('[data-type]').forEach((box) => {
      if (calm || !('IntersectionObserver' in window)) return;
      const spans = [...box.querySelectorAll('p:last-child [lang]')];
      const full = spans.map((s) => s.textContent);
      spans.forEach((s) => { s.textContent = ''; });
      box.classList.add('is-typing');
      const io = new IntersectionObserver((entries) => {
        if (!entries[0].isIntersecting) return;
        io.disconnect();
        let n = 0;
        const longest = Math.max(...full.map((t) => t.length));
        const timer = setInterval(() => {
          n += 2;
          spans.forEach((s, i) => { s.textContent = full[i].slice(0, n); });
          if (n >= longest) {
            clearInterval(timer);
            box.classList.remove('is-typing');
          }
        }, 22);
      }, { threshold: 0.5 });
      io.observe(box);
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

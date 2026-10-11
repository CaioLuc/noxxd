/**
 * NOXXD — Interactivity, Animations & Responsiveness
 * Vanilla ES6 JavaScript Implementation
 * Strict Geometric Identity (Zero Border-Radius)
 * Domain: noxxd.com.br
 */

'use strict';

document.addEventListener('DOMContentLoaded', () => {
  // ---------------------------------------------------------------------------
  // 1. Mobile Navigation Menu Toggle & Accessibility
  // ---------------------------------------------------------------------------
  const navToggle = document.querySelector('.nav-toggle');
  const siteNav = document.querySelector('.site-nav');

  if (navToggle && siteNav) {
    const setMenuState = (isOpen) => {
      if (isOpen) {
        siteNav.classList.add('is-open');
        navToggle.setAttribute('aria-expanded', 'true');
      } else {
        siteNav.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    };

    // Toggle menu on button click
    navToggle.addEventListener('click', (event) => {
      event.stopPropagation();
      const willOpen = !siteNav.classList.contains('is-open');
      setMenuState(willOpen);
    });

    // Close menu when any navigation link is clicked
    const navLinks = siteNav.querySelectorAll('.nav-link');
    navLinks.forEach((link) => {
      link.addEventListener('click', () => {
        setMenuState(false);
      });
    });

    // Close menu on 'Escape' key press
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' || event.key === 'Esc') {
        if (siteNav.classList.contains('is-open')) {
          setMenuState(false);
          navToggle.focus();
        }
      }
    });

    // Close menu when clicking outside of navbar
    document.addEventListener('click', (event) => {
      if (siteNav.classList.contains('is-open')) {
        if (!siteNav.contains(event.target) && !navToggle.contains(event.target)) {
          setMenuState(false);
        }
      }
    });
  }

  // ---------------------------------------------------------------------------
  // 2. Active Navigation Section Highlighting on Scroll
  // ---------------------------------------------------------------------------
  const trackedSections = document.querySelectorAll('section[id]');
  const menuLinks = document.querySelectorAll('.site-nav .nav-link');

  if (trackedSections.length > 0 && menuLinks.length > 0) {
    const handleScrollActiveNav = () => {
      const scrollPosition = window.scrollY + 140;

      trackedSections.forEach((section) => {
        const top = section.offsetTop;
        const height = section.offsetHeight;
        const id = section.getAttribute('id');

        if (scrollPosition >= top && scrollPosition < top + height) {
          menuLinks.forEach((link) => {
            const href = link.getAttribute('href');
            if (href === `#${id}`) {
              link.classList.add('active');
            } else {
              link.classList.remove('active');
            }
          });
        }
      });
    };

    window.addEventListener('scroll', handleScrollActiveNav, { passive: true });
    handleScrollActiveNav();
  }

  // ---------------------------------------------------------------------------
  // 3. Scroll Reveal System with prefers-reduced-motion Accessibility
  // ---------------------------------------------------------------------------
  const revealElements = document.querySelectorAll('.reveal-item');
  const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const revealAllImmediately = () => {
    revealElements.forEach((element) => {
      element.classList.add('is-revealed');
      element.classList.add('is-visible');
    });
  };

  if (revealElements.length > 0) {
    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      // Immediate reveal without animation if reduced motion is requested
      revealAllImmediately();
    } else {
      const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
      });

      revealElements.forEach((element) => {
        revealObserver.observe(element);
      });
    }
  }

  // Dynamically react if the user changes reduced motion preference at runtime
  if (window.matchMedia) {
    try {
      const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
      motionQuery.addEventListener('change', (event) => {
        if (event.matches) {
          revealAllImmediately();
        }
      });
    } catch {
      // Graceful fallback for older browser engines
    }
  }

  // ---------------------------------------------------------------------------
  // 4. Tactile Geometric Button Ripple (Strict Zero Border-Radius)
  // ---------------------------------------------------------------------------
  const interactiveButtons = document.querySelectorAll('.btn, .btn-primary, .btn-outline');

  interactiveButtons.forEach((button) => {
    button.addEventListener('click', function (event) {
      const rect = button.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);

      const clientX = (typeof event.clientX === 'number' && event.clientX > 0)
        ? event.clientX
        : (rect.left + rect.width / 2);
      const clientY = (typeof event.clientY === 'number' && event.clientY > 0)
        ? event.clientY
        : (rect.top + rect.height / 2);

      const x = clientX - rect.left - size / 2;
      const y = clientY - rect.top - size / 2;

      // Create rectangular / square ripple element (right-angle geometric)
      const ripple = document.createElement('span');
      ripple.className = 'btn-ripple';
      ripple.style.width = `${size}px`;
      ripple.style.height = `${size}px`;
      ripple.style.left = `${x}px`;
      ripple.style.top = `${y}px`;

      button.appendChild(ripple);

      ripple.addEventListener('animationend', () => {
        ripple.remove();
      });

      // Defensive fallback cleanup in case animationend does not fire
      setTimeout(() => {
        if (ripple.parentNode) {
          ripple.remove();
        }
      }, 600);
    });
  });
});

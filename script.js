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

  // ---------------------------------------------------------------------------
  // 5. Bilingual Localization (PT-BR / EN) & Persistence
  // ---------------------------------------------------------------------------
  const i18nData = {
    pt: {
      doc_title: "NOXXD — Tecnologia Feita do Seu Jeito | BUILD IT YOUR WAY",
      nav_home: "Início",
      nav_services: "Serviços",
      nav_projects: "Projetos",
      nav_contact: "Contato",
      hero_slogan: "BUILD IT YOUR WAY",
      hero_description: "Soluções digitais de alto impacto, plataformas SaaS robustas e sistemas inteligentes sob medida para modernizar o setor público e empresas privadas.",
      hero_btn_projects: "CONHEÇA NOSSOS PROJETOS",
      hero_btn_contact: "FALE CONOSCO",
      services_title: "Nossos Serviços",
      services_lead: "Engenharia de software ágil, arquitetura limpa e design geométrico de alta fidelidade para transformar sua visão em realidade operacional.",
      service_web_title: "Criação de Sites e Landing Pages",
      service_web_desc: "Desenvolvimento web moderno, totalmente responsivo e otimizado para motores de busca (SEO) e alta taxa de conversão. Construímos sites institucionais e landing pages de alto padrão visual com identidade geométrica exclusiva.",
      service_web_btn: "Solicitar Orçamento",
      service_saas_title: "Sistemas Web e SaaS",
      service_saas_desc: "Arquitetura e programação de plataformas multi-tenant (SaaS), aplicativos em nuvem e painéis de controle empresariais. Código escalável, controle de acesso seguro e integrações fluidas via APIs REST e GraphQL.",
      service_saas_btn: "Construir Sistema",
      service_consulting_title: "Consultoria em Tecnologia",
      service_consulting_desc: "Auditoria técnica de arquitetura, modernização de sistemas legados, estratégias de migração em nuvem e planejamento tecnológico personalizado para prefeituras, órgãos públicos e empresas inovadoras.",
      service_consulting_btn: "Falar com Especialista",
      projects_title: "Portfólio de Projetos",
      projects_lead: "Soluções tecnológicas em operação que modernizam a gestão pública e aceleram empresas de ponta a ponta.",
      cidadao_tag: "GOVTECH · CASO DE SUCESSO",
      cidadao_title: "Cidadão Relata — Zeladoria Urbana e Gestão Pública Municipal",
      cidadao_lead: "Plataforma digital integrada composta por aplicativo mobile para munícipes e painel administrativo web em tempo real para prefeituras e secretarias de obras e zeladoria.",
      cidadao_p1: "O <strong>Cidadão Relata</strong> é o projeto insignia da NOXXD desenvolvido para aproximar munícipes e prefeituras. Pelo smartphone, o cidadão abre relatos de ocorrências urbanas em poucos segundos — incluindo buracos na malha asfáltica, falhas na iluminação pública, vazamentos na rede e descarte irregular de entulho —, registrando coordenadas de geolocalização automática e fotos comprobatórias.",
      cidadao_p2: "Na gestão municipal, o painel web administrativo (dashboard) centraliza toda a triagem em tempo real, despacha equipes operacionais de campo e oferece visualização analítica através de <strong>mapa de calor (heatmap)</strong> de incidentes por bairro. Isso permite que gestores do setor público priorizem investimentos públicos com base em dados concretos.",
      cidadao_tag_1: "App Mobile",
      cidadao_tag_2: "Painel Web Municipal",
      cidadao_tag_3: "Mapa de Calor (Heatmap)",
      cidadao_tag_4: "Relato de Ocorrências",
      cidadao_tag_5: "Gestão Pública",
      cidadao_tag_6: "Prefeitura Conectada",
      cidadao_btn: "SOLICITAR DEMONSTRAÇÃO",
      other_projects_title: "Outros Projetos Desenvolvidos",
      other_projects_lead: "Conheça outras soluções em software de alta qualidade entregues pela NOXXD.",
      p1_tag_1: "Setor Público",
      p1_tag_2: "Open Data",
      p1_title: "Portal da Transparência",
      p1_desc: "Plataforma digital para prestação de contas governamentais em estrita conformidade com a Lei de Acesso à Informação (LAI). Apresenta gráficos interativos de receitas, despesas públicas, licitações e contratos com download de dados abertos.",
      p1_badge: "100% Conformidade LAI",
      p2_tag_1: "SaaS / GIS",
      p2_tag_2: "Planejamento Urbano",
      p2_title: "GeoUrban",
      p2_desc: "Sistema corporativo de geoprocessamento e mapeamento geoespacial para prefeituras e concessionárias. Permite o cadastro multifinalitário de lotes, zoneamento fiscal e fiscalização predial georreferenciada em alta resolução.",
      p2_badge: "Precisão Submétrica",
      p3_tag_1: "Atendimento",
      p3_tag_2: "Protocolo Digital",
      p3_title: "AtendeCidadão",
      p3_desc: "Central omnichannel de serviços públicos e protocolo digital unificado. Possibilita o agendamento prévio de atendimentos, emissão de certidões online e acompanhamento de processos administrativos em tempo real.",
      p3_badge: "-65% Tempo de Espera",
      contact_title: "Fale Conosco",
      contact_lead: "Pronto para construir sua próxima plataforma ou modernizar a infraestrutura da sua organização? Entre em contato direto com a equipe da NOXXD.",
      contact_direct_title: "Canais Diretos",
      contact_email_label: "E-mail Corporativo",
      contact_wa_label: "WhatsApp Comercial",
      contact_hours: "Horário de atendimento: Segunda a sexta-feira, das 09h às 18h (Horário de Brasília). Respondemos solicitações técnicas e comerciais em até 24 horas úteis.",
      contact_start_title: "Inicie Seu Projeto",
      contact_start_desc: "Seja para criar um novo site ou landing page de alto desempenho, construir um sistema SaaS escalável ou agendar uma apresentação aprofundada da plataforma Cidadão Relata, nossa equipe de engenharia e produto está pronta para atender seu projeto.",
      contact_btn_email: "ENVIAR E-MAIL AGORA",
      contact_btn_wa: "CONVERSAR NO WHATSAPP",
      footer_copy: "© 2026 NOXXD. Todos os direitos reservados."
    },
    en: {
      doc_title: "NOXXD — Technology Built Your Way | BUILD IT YOUR WAY",
      nav_home: "Home",
      nav_services: "Services",
      nav_projects: "Projects",
      nav_contact: "Contact",
      hero_slogan: "BUILD IT YOUR WAY",
      hero_description: "High-impact digital solutions, robust SaaS platforms, and intelligent custom systems designed to modernize public administration and private enterprises.",
      hero_btn_projects: "EXPLORE OUR PROJECTS",
      hero_btn_contact: "CONTACT US",
      services_title: "Our Services",
      services_lead: "Agile software engineering, clean architecture, and high-fidelity geometric design to turn your vision into operational reality.",
      service_web_title: "Websites & Landing Pages",
      service_web_desc: "Modern, fully responsive web development optimized for search engines (SEO) and high conversion rates. We build corporate websites and premium landing pages with exclusive geometric identity.",
      service_web_btn: "Request a Quote",
      service_saas_title: "Web Systems & SaaS",
      service_saas_desc: "Architecture and development of multi-tenant SaaS platforms, cloud applications, and enterprise dashboards. Scalable code, secure access control, and seamless REST/GraphQL API integrations.",
      service_saas_btn: "Build System",
      service_consulting_title: "Technology Consulting",
      service_consulting_desc: "Technical architecture audits, legacy system modernization, cloud migration strategies, and tailored technology planning for municipalities, public entities, and innovative enterprises.",
      service_consulting_btn: "Talk to an Expert",
      projects_title: "Project Portfolio",
      projects_lead: "Active tech solutions modernizing public administration and accelerating businesses end-to-end.",
      cidadao_tag: "GOVTECH · SUCCESS STORY",
      cidadao_title: "Cidadão Relata — Urban Maintenance & Municipal Management",
      cidadao_lead: "Integrated digital platform featuring a citizen mobile app and a real-time web dashboard for city halls and public works departments.",
      cidadao_p1: "<strong>Cidadão Relata</strong> is NOXXD's flagship GovTech platform connecting citizens and municipalities. Via mobile, citizens report urban issues in seconds — asphalt potholes, public lighting failures, water leaks, and illegal dumping —, capturing automatic GPS coordinates and photographic proof.",
      cidadao_p2: "For city management, the web dashboard centralizes real-time triage, dispatches field operational teams, and delivers analytical insight through an incident <strong>heatmap</strong> across districts, enabling public managers to prioritize investments with hard data.",
      cidadao_tag_1: "Mobile App",
      cidadao_tag_2: "Municipal Web Dashboard",
      cidadao_tag_3: "Incident Heatmap",
      cidadao_tag_4: "Issue Reporting",
      cidadao_tag_5: "Public Governance",
      cidadao_tag_6: "Connected City",
      cidadao_btn: "REQUEST A DEMO",
      other_projects_title: "Other Featured Projects",
      other_projects_lead: "Explore other high-caliber software engineering solutions delivered by NOXXD.",
      p1_tag_1: "Public Sector",
      p1_tag_2: "Open Data",
      p1_title: "Transparency Portal",
      p1_desc: "Digital platform for government accountability in strict compliance with Freedom of Information laws. Features interactive charts for revenue, public spending, tenders, contracts, and open data downloads.",
      p1_badge: "100% LAI Compliance",
      p2_tag_1: "SaaS / GIS",
      p2_tag_2: "Urban Planning",
      p2_title: "GeoUrban",
      p2_desc: "Corporate GIS and geospatial mapping system for municipalities and utility companies. Enables multipurpose cadastre, fiscal zoning, and high-resolution georeferenced property auditing.",
      p2_badge: "Sub-Meter Precision",
      p3_tag_1: "Customer Care",
      p3_tag_2: "Digital Protocol",
      p3_title: "AtendeCidadão",
      p3_desc: "Omnichannel public service hub and unified digital protocol. Enables appointment booking, online certificate issuance, and real-time administrative workflow tracking.",
      p3_badge: "-65% Wait Time",
      contact_title: "Contact Us",
      contact_lead: "Ready to build your next platform or modernize your organization's digital infrastructure? Get in touch directly with the NOXXD team.",
      contact_direct_title: "Direct Channels",
      contact_email_label: "Corporate Email",
      contact_wa_label: "Commercial WhatsApp",
      contact_hours: "Business hours: Monday to Friday, 9:00 AM - 6:00 PM (BRT). We respond to technical and commercial inquiries within 24 business hours.",
      contact_start_title: "Start Your Project",
      contact_start_desc: "Whether you need a high-performance website or landing page, a scalable SaaS system, or an in-depth demo of the Cidadão Relata platform, our engineering team is ready to deliver.",
      contact_btn_email: "SEND EMAIL NOW",
      contact_btn_wa: "CHAT ON WHATSAPP",
      footer_copy: "© 2026 NOXXD. All rights reserved."
    }
  };

  const applyLanguage = (lang) => {
    const selectedLang = i18nData[lang] ? lang : 'pt';
    const dict = i18nData[selectedLang];

    // 1. Update document html lang attribute
    document.documentElement.lang = selectedLang === 'pt' ? 'pt-BR' : 'en';

    // 2. Update page title
    if (dict.doc_title) {
      document.title = dict.doc_title;
    }

    // 3. Update all registered elements
    const translatableElements = document.querySelectorAll('[data-i18n]');
    translatableElements.forEach((element) => {
      const key = element.getAttribute('data-i18n');
      if (dict[key] !== undefined) {
        if (dict[key].includes('<')) {
          element.innerHTML = dict[key];
        } else {
          element.textContent = dict[key];
        }
      }
    });

    // 4. Update language toggle button states
    const langButtons = document.querySelectorAll('.lang-btn');
    langButtons.forEach((btn) => {
      const btnLang = btn.getAttribute('data-lang');
      if (btnLang === selectedLang) {
        btn.classList.add('active');
        btn.setAttribute('aria-pressed', 'true');
      } else {
        btn.classList.remove('active');
        btn.setAttribute('aria-pressed', 'false');
      }
    });

    // 5. Persist choice
    try {
      localStorage.setItem('noxxd_lang', selectedLang);
    } catch {
      // Local storage disabled or restricted
    }
  };

  // Bind click handlers to language switch buttons
  const langButtons = document.querySelectorAll('.lang-btn');
  langButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const targetLang = btn.getAttribute('data-lang');
      applyLanguage(targetLang);
    });
  });

  // Initialize language from localStorage or default 'pt'
  let initialLang = 'pt';
  try {
    initialLang = localStorage.getItem('noxxd_lang') || 'pt';
  } catch {
    initialLang = 'pt';
  }
  applyLanguage(initialLang);
});

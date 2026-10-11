# NOXXD — Website & Portfólio Institucional

> **BUILD IT YOUR WAY**  
> Tecnologia sob medida para o setor público e empresas privadas.  
> Acesse: [noxxd.com.br](https://noxxd.com.br)

---

## 📌 Sobre a NOXXD

A **NOXXD** é uma empresa de tecnologia focada no desenvolvimento de soluções digitais de alto impacto, plataformas SaaS escaláveis e sistemas sob medida para modernizar a gestão pública e acelerar negócios.

### Projetos em Portfólio
Cada projeto tem página própria, com a identidade visual oficial do produto dentro da moldura NOXXD:
- **[Urbis](https://noxxd.com.br/projetos/urbis/)** (`/projetos/urbis/`): zeladoria urbana para prefeituras, com app do cidadão (React Native / Expo 54) e painel web com mapa de calor (Next.js 14).
- **[HealthSearch](https://noxxd.com.br/projetos/healthsearch/)** (`/projetos/healthsearch/`): central de Saúde e Segurança do Trabalho que sustenta o SIGAC (ASO NR-07, matriz NR-01 a NR-35, CID-10 cifrado em AES-GCM 256).
- **[CARITAS](https://noxxd.com.br/projetos/caritas/)** (`/projetos/caritas/`): plataforma clínica para psicólogas(os), com prontuário, anamnese, I.A., documentos CFP, agenda e PIX.

Logos em `assets/projetos/<slug>/`. Prints dos sistemas entram em `assets/projetos/<slug>/screens/`: troque o conteúdo do `.shot__screen` correspondente (marcado com `<!-- slot: ... -->` no HTML) por um `<img>`.

### Serviços
- **Sistemas Web & SaaS:** Plataformas em nuvem, controle de acessos, microsserviços e APIs.
- **Criação de Sites & Landing Pages:** Interfaces modernas, responsivas e de alta performance.
- **Consultoria em Tecnologia:** Arquitetura, planejamento tecnológico e transformação digital.

---

## 🎨 Identidade Visual & Design System

O site segue uma identidade visual geométrica e marcante:
- **Cores Oficiais:**
  - Fundo principal: Azul-petróleo (`#1B5E6B`)
  - Fundo secundário: Azul-petróleo escuro (`#154B56`)
  - Acentos, botões e detalhes: Dourado (`#C8975D`)
- **Estética:** Grade blueprint de fundo, ornamentos pixelados e cantos ortogonais retos (`border-radius: 0`).
- **Tipografia:** Oswald (títulos condensados) e Josefin Sans (slogans e textos).

---

## 💻 Tecnologias

- **HTML5 Semântico:** Estrutura acessível com metadados SEO e OpenGraph completos.
- **CSS3 Puro:** Variáveis de design system, micro-interações táteis e aceleração por GPU.
- **Vanilla JavaScript (ES6):** Animações suaves na rolagem (*Scroll Reveal*), partículas 8-bit douradas (GPU, respeitam `prefers-reduced-motion`), menu mobile acessível, navegação ativa e alternância PT | EN (persistida entre Home e páginas de projeto).
- **Hospedagem:** GitHub Pages com domínio customizado via arquivo `CNAME`.

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).

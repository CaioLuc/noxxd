# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- **Gestores públicos**: prefeituras, secretarias e órgãos públicos avaliando uma fornecedora de tecnologia para zeladoria, atendimento e gestão (caso Urbis).
- **Empresas privadas**: RH, SST e operações de empresas que precisam de sistema sob medida (caso HealthSearch/SIGAC).
- **Recrutadores e avaliadores**: banca acadêmica e recrutadores julgando a profundidade técnica do portfólio.

O visitante chega pela Home, quer entender em segundos o que a NOXXD entrega e abre a página do projeto mais próximo da sua realidade antes de entrar em contato.

## Product Purpose

noxxd.com.br é o site institucional e portfólio da NOXXD, software house que desenvolve sites, landing pages, sistemas web e SaaS sob medida para setor público e empresas privadas. Sucesso: o visitante entende a competência técnica pelos projetos reais e chega ao contato (e-mail ou WhatsApp) em `/#contato`.

## Positioning

A NOXXD mostra produtos reais em operação, cada um com identidade visual própria, e não um catálogo genérico de serviços. O lema da marca é "BUILD IT YOUR WAY".

## Capabilities and Constraints

- Site estático (HTML, CSS, JS vanilla) no GitHub Pages, domínio `noxxd.com.br` (arquivo `CNAME`). Sem build step.
- Bilíngue: português padrão, inglês via seletor PT | EN, escolha persistida em `localStorage` (`noxxd_lang`).
- Projetos reais em portfólio: **Urbis** (sucessor do antigo "Cidadão Relata"), **HealthSearch** (sustenta o SIGAC) e **CARITAS**. Páginas em `/projetos/<slug>/`.
- Screenshots reais dos sistemas ainda não existem: as páginas têm slots em `assets/projetos/<slug>/screens/`.

## Brand Commitments

- Nome sempre **NOXXD** (nunca "NOXXED"). Slogan "BUILD IT YOUR WAY" mantido em inglês.
- Identidade NOXXD: azul-petróleo `#1B5E6B` / `#154B56`, dourado `#C8975D`, cantos retos, grade e pixel/xadrez 8-bit, Oswald + Josefin Sans.
- Cada página de projeto usa a paleta, tipografia e logo oficiais do projeto (specs em `Exemplos/<Projeto>/`), com a moldura NOXXD (barra superior e rodapé).

## Evidence on Hand

- Logos oficiais: `assets/projetos/urbis/logo.png`, `assets/projetos/healthsearch/logo.png`, `assets/projetos/caritas/logo.svg`.
- Especificações de front-end de cada projeto em `Exemplos/`.
- Fato citável do CARITAS: nota 4,55/5,00 em avaliação por heurísticas de Nielsen.
- Não existem depoimentos, clientes nomeados, preços ou métricas de negócio: não inventar.

## Product Principles

1. Provar com o produto real, não com adjetivos.
2. Cada projeto fala na sua própria identidade; a NOXXD é a moldura.
3. Nenhuma alegação comercial que as specs não sustentem.
4. Contato sempre a um clique.

## Accessibility & Inclusion

WCAG AA de contraste, navegação por teclado, `prefers-reduced-motion` respeitado em toda animação.

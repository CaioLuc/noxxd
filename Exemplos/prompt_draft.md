# Teamwork Project Prompt — Draft

> Status: Ready for launch — awaiting user approval
> Goal: Craft prompt → get user approval → delegate to teamwork_preview
> Requested team: [none — teamwork routes from the description]

Construir páginas dedicadas e personalizadas para os 3 projetos reais da NOXXD (Urbis, HealthSearch e CARITAS) com as identidades visuais, cores e logos oficiais extraídos da pasta `Exemplos/`, atualizar a vitrine da Home com os logos reais e rotas limpas, e integrar animações de partículas geométricas 8-bit flutuantes com suporte bilíngue PT/EN no domínio noxxd.com.br.

Working directory: c:\Projetos Faculdade\noxxd
Integrity mode: development

Reference material:
- `Exemplos/Urbis/ESPECIFICACOES_FRONTEND.md` e `Exemplos/Urbis/logo urbis.png`
- `Exemplos/HealthSearch/especificacoes_frontend_sigac.md` e `Exemplos/HealthSearch/LOGO HEALTHSEARCH.png`
- `Exemplos/Caritas/especificacoes-frontend.md` e `Exemplos/Caritas/LOGO CARITAS.svg`

## Requirements

### R1. Criação das 3 Páginas Dedicadas com Identidade Visual Própria por Projeto
Criar páginas completas, responsivas e visualmente ricas em rotas limpas (`/projetos/<slug>/index.html`):

1. **Urbis** (`/projetos/urbis/index.html`):
   - **Identidade e Cores**: Navy Principal (`#03045E` / `#243d80`), Ocean Secundário (`#0077B6`), Sky/Accent (`#00B4D8`), Ice Background (`#CAF0F8`), Superfície Clara (`#FFFFFF`) e Fundo Web (`#F8FAFC`).
   - **Tipografia**: Sans-serif moderna cívica (Inter / Manrope).
   - **Logo**: Utilizar `logo urbis.png` (alocado em `assets/projetos/urbis/logo.png`).
   - **Conteúdo e Showcase**:
     - Dualidade: App Mobile do Cidadão (React Native / Expo 54) + Painel Web da Prefeitura (Next.js 14 / Leaflet Heatmap / Recharts).
     - Zeladoria urbana com fotos, geolocalização exata e áudio; alertas da Defesa Civil; catálogo turístico.
     - Centro de comando com mapa de calor e inteligência geoespacial para prefeituras.
     - Conformidade: Marco Legal do Governo Digital (Lei 14.129/2021) e LGPD.

2. **HealthSearch** (`/projetos/healthsearch/index.html`):
   - **Identidade e Cores**: Azul Petróleo Profundo (`#0B2545`), Primary Light (`#13375e`), Âmbar Corporativo (`#F5A623`), Surface Neutro (`#f4f6f8`), Surface Card (`#ffffff`) e Semáforo SST (`#16a34a` Em Dia, `#d97706` A Vencer, `#dc2626` Vencido).
   - **Tipografia**: Sans-serif corporativa e técnica.
   - **Logo**: Utilizar `LOGO HEALTHSEARCH.png` (alocado em `assets/projetos/healthsearch/logo.png`).
   - **Conteúdo e Showcase**:
     - Central unificada de Saúde e Segurança do Trabalho (sustenta o SIGAC).
     - Gestão completa do ciclo do ASO (NR-07), matriz de treinamentos (NR-01 a NR-35), fechamento mensal de folha e absenteísmo.
     - Criptografia client-side de CID-10 e dados sensíveis em AES-GCM 256 bits.
     - Arquitetura de custo zero: React 19 + Tailwind v4 + serverless Firebase + Cloudflare R2 sem taxa de egress.

3. **CARITAS** (`/projetos/caritas/index.html`):
   - **Identidade e Cores**: Azul Meia-Noite (`#0A1628`), Azul Real (`#2563EB`), Fundo Geral Claro (`#F8F9FA`) / Escuro (`#0D1117`), Accent Soft (`#EFF6FF`).
   - **Tipografia**: Títulos e Destaques em `Sora`, Corpo e Formulários em `Inter`.
   - **Logo**: Utilizar `LOGO CARITAS.svg` (alocado em `assets/projetos/caritas/logo.svg`).
   - **Conteúdo e Showcase**:
     - Prontuário eletrônico psicológico seguro, anamnese estruturada e criador de questionários.
     - Resumo clínico com I.A. (GPT-4o-mini), emissão de documentos oficiais CFP (Resolução 06/2019).
     - Agenda inteligente com link público (`/agendar/:slug`) e cobrança automatizada com PIX (QR Code e Copia e Cola).
     - Conformidade estrita CFP (guarda obrigatória de 5 anos com anonimização cadastral) e LGPD.

**Elementos comuns de cada página:**
- Barra superior de navegação da NOXXD com link de retorno à Home ("← NOXXD Home"), seletor de idioma (PT/EN) e botão de contato.
- Estrutura de slots para screenshots futuros dos sistemas com moldura elegante.
- Botão CTA destacado direcionando para o formulário de contato da Home (`/#contato`).
- Rodapé institucional NOXXD.

### R2. Atualização dos Cards de Projetos na Home (`index.html`)
- Atualizar a grade `#projetos` para destacar os 3 projetos reais: Urbis, HealthSearch e CARITAS.
- Cada card deve utilizar a logo oficial correspondente, badges de categoria, resumo técnico, métrica de impacto e botão direto para `/projetos/<slug>/`.
- Enquadramento perfeito das logos nos cards com `object-fit: contain` e padding adequado.

### R3. Organização de Assets
- Copiar e organizar as logos de `Exemplos/` para a estrutura do site em `assets/projetos/<slug>/`:
  - `assets/projetos/urbis/logo.png`
  - `assets/projetos/healthsearch/logo.png`
  - `assets/projetos/caritas/logo.svg`
- Deixar pastas prontas para os prints que serão adicionados futuramente.

### R4. Animações de Partículas Geométricas 8-Bit Flutuantes
- Implementar micro-quadrados dourados 8-bit flutuando suavemente em background na Home NOXXD.
- Aceleração por GPU (`transform: translate3d`), 60 FPS fixos sem queda de frame.
- Suporte a `@media (prefers-reduced-motion: reduce)`.

### R5. Suporte Bilíngue Integrado (PT-BR / EN)
- Textos em Português por padrão e suporte completo a Inglês via switcher `PT | EN` tanto na Home quanto nas 3 páginas de projetos.

### R6. Validação Automatizada e Deploy no GitHub Pages
- Criar testes no `pytest` cobrindo:
  - Rotas 200 de `/projetos/urbis/`, `/projetos/healthsearch/` e `/projetos/caritas/`.
  - Ausência de 404 e links quebrados.
  - Presença das logos oficiais e textos descritivos.
  - Integridade do arquivo `CNAME` (`noxxd.com.br`).

## Verification Resources

- Suite `pytest` cobrindo todas as rotas internas, links e conformidade de tags.
- Verificação de sintaxe via `node --check`.

## Acceptance Criteria

### Páginas Dedicadas de Projetos
- [ ] 3 páginas funcionais criadas em `projetos/urbis/index.html`, `projetos/healthsearch/index.html` e `projetos/caritas/index.html`.
- [ ] Cada página aplica fielmente a paleta de cores e tipografia de seu respectivo projeto (Urbis: azul/ciano cívico; HealthSearch: petróleo/âmbar SST; Caritas: azul meia-noite/real clínico com fonte Sora).
- [ ] As logos oficiais de cada projeto estão renderizadas corretamente sem distorção.
- [ ] Navegação de retorno para a Home funcional em todas as páginas.
- [ ] Suporte bilíngue (PT/EN) integrado em todas as páginas.

### Vitrine da Home
- [ ] Os 3 cards da Home exibem Urbis, HealthSearch e CARITAS com logos oficiais e links para suas respectivas páginas dedicadas.

### Animações e Fluidez
- [ ] Micro-quadrados dourados 8-bit flutuam suavemente no fundo em 60 FPS sem engasgos de rolagem.
- [ ] `@media (prefers-reduced-motion: reduce)` respeitado.

### Integridade e Deploy
- [ ] Testes do `pytest` passam com 100% de sucesso.
- [ ] `CNAME` com `noxxd.com.br` preservado.
- [ ] Build e commit prontos para publicação no GitHub Pages.

---
*Next: Aprovação do usuário → delegar via invoke_subagent.*

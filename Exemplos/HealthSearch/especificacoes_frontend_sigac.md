# Especificacoes Tecnicas do Frontend — SIGAC

Documento tecnico de referencia para arquitetura de interface, padronizacao de design system, tokens semanticos, composicao de layout e primitivas de componentes do **SIGAC** (Sistema Integrado de Gestao de ASOs e Colaboradores).

---

## 1. Stack Tecnologica e Fundamentos de Engenharia

O ecossistema frontend do SIGAC foi estruturado como uma **Single Page Application (SPA) client-centric**, projetada para operar em alto desempenho, baixa latencia e custo zero de infraestrutura de borda:

- **Biblioteca Principal**: React 19 (`react` e `react-dom` versao `19.2.8`).
- **Ferramenta de Build & HMR**: Vite 8 (`vite` versao `8.2.0`, com `@vitejs/plugin-react` versao `6.0.1`).
- **Motor de Estilizacao**: Tailwind CSS v4 (`tailwindcss` versao `4.3.3`, `@tailwindcss/vite` versao `4.3.3`). Implementacao **CSS-First** nativa via diretiva `@theme` diretamente em `src/index.css`, sem necessidade de arquivos de configuracao JavaScript intermediarios (`tailwind.config.js`).
- **Roteamento**: React Router DOM v7 (`react-router-dom` versao `7.18.2`) com protecao por perfis de acesso (`ProtectedRoute`).
- **Gerenciamento de Cache de Rede**: TanStack Query v5 (`@tanstack/react-query` versao `5.104.0`).
- **Motor de Animacao e Microinteracoes**: Anime.js v4 (`animejs` versao `4.5.0`).
- **Visualizacao de Dados e Indicadores**: Recharts 3 (`recharts` versao `3.10.1`).
- **Iconografia Tecnica**: Heroicons v2 (`@heroicons/react` versao `2.2.0`). Zero caracteres de emoji soltos.
- **Processamento de Documentos e Mídia**: jsPDF 4 (`jspdf` versao `4.2.1`) para renderizacao e composicao de folhas A4 normativas no cliente.
- **Validacao e Seguranca**: Zod 4 (`zod` versao `4.6.5`) e Web Crypto API (AES-GCM 256 bits).

---

## 2. Tokens de Design System e Paleta de Cores (`src/index.css`)

Os tokens de design foram declarados diretamente na raiz do CSS atraves do bloco `@theme`, tornando-se classes utilitarias imediatas no Tailwind CSS v4.

### 2.1. Identidade Corporativa e Marca

| Token | Classe Utilitaria | Valor Hexadecimal | Funcao no Sistema |
| :--- | :--- | :--- | :--- |
| **primary** | `bg-primary`, `text-primary` | `#0B2545` | Azul Petroleo Profundo. Base institucional, sidebar, botoes de acao principal e cabecalhos de modais. |
| **primary-light** | `bg-primary-light` | `#13375e` | Variante intermediaria para selecoes, bordas de destaque e estados de foco. |
| **primary-soft** | `bg-primary-soft` | `#e3eaf3` | Fundo suave para cards informativos e filtros ativos. |
| **accent** | `bg-accent`, `text-accent` | `#F5A623` | Ambar Corporativo. Elemento de atencao e foco para acoes que demandam prioridade imediata. |
| **accent-hover** | `bg-accent-hover` | `#e09510` | Estado de sobreposicao de cursor em elementos de destaque. |
| **accent-soft** | `bg-accent-soft` | `#fef7e8` | Fundo atenuado para caixas de notificacao e badges de atencao. |

### 2.2. Superficies, Estrutura e Bordas

| Token | Classe Utilitaria | Valor Hexadecimal | Funcao no Sistema |
| :--- | :--- | :--- | :--- |
| **surface** | `bg-surface` | `#f4f6f8` | Fundo global do viewport (cinza claro neutro com alto contraste em relacao aos cartoes). |
| **surface-card** | `bg-surface-card` | `#ffffff` | Fundo solido de cards, tabelas, modais e gavetas. |
| **surface-subtle** | `bg-surface-subtle` | `#f8fafc` | Fundo para linhas de tabela alternadas e campos de suporte. |
| **surface-muted** | `bg-surface-muted` | `#eef2f6` | Divisores de secoes e fundos desabilitados. |
| **border** | `border-border` | `#dde1e7` | Linhas de contorno padrao de cartoes e modais. |
| **border-strong** | `border-border-strong` | `#b0b7c3` | Contornos de caixas de entrada (inputs) e seletores para nitidez visual. |

### 2.3. Tipografia e Alto Contraste (WCAG AA)

| Token | Classe Utilitaria | Valor Hexadecimal | Regra de Aplicacao |
| :--- | :--- | :--- | :--- |
| **text** | `text-text` | `#1a1f2b` | Texto primario. Utilizado em titulos, paragrafos, valores de tabelas e inputs editaveis. |
| **text-muted** | `text-text-muted` | `#4b5563` | Rotulos de campos (labels), subtextos e informacoes auxiliares de alto contraste. |
| **text-light** | `text-text-light` | `#526071` | Identificadores de data, registros de log e indicadores de estado secundario. |

### 2.4. Semaforo Semantico de SST e Conformidade Normativa (NR-7)

Utilizado em todo o ciclo de vida do ASO, ficha de colaboradores, exames complementares e painel analitico:

| Status SST | Token de Fundo | Token de Borda | Token de Texto | Codigo Hex Base | Significado Tecnico |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Vencido** | `bg-status-vencido-soft` | `border-status-vencido` | `text-status-vencido` | `#dc2626` | ASO expirado. Inconformidade imediata com a NR-7. |
| **A Vencer** | `bg-status-a-vencer-soft` | `border-status-a-vencer` | `text-status-a-vencer` | `#d97706` | Janela preventiva de 30 dias para vencimento normativo. |
| **Em Dia** | `bg-status-em-dia-soft` | `border-status-em-dia` | `text-status-em-dia` | `#16a34a` | Exame valido, aptidao ocupacional regularizada. |
| **Pendente** | `bg-status-pendente-soft` | `border-status-pendente` | `text-status-pendente` | `#64748b` | Aguardando resultado de exame complementar ou emissao de laudo. |
| **Agendado** | `bg-status-agendado-soft` | `border-status-agendado` | `text-status-agendado` | `#0284c7` | Consulta agendada em clinica credenciada. |
| **Solicitado**| `bg-status-solicitado-soft`| `border-status-solicitado`| `text-status-solicitado`| `#4f46e5` | Pedido de guia de encaminhamento gerado no sistema. |

### 2.5. Tokens da Barra Lateral (Sidebar)

- `sidebar-bg`: `#0B2545`
- `sidebar-hover`: `#13375e`
- `sidebar-active`: `#1a4575`
- `sidebar-border`: `#163b66`

---

## 3. Arquitetura de Layout e Composicao Estrutural

O layout principal e orquestrado por `src/components/AppLayout.jsx` e `src/components/Sidebar.jsx`, dividindo o espaco de tela em tres camadas principais:

### 3.1. Barra Lateral de Navegacao (`Sidebar.jsx`)
- **Modo Expandido**: Largura de `16rem` (`w-64`), apresentando a marca institucional SIGAC, agrupamento logico de menus (Operacao, SST, Indicadores e Configuracoes) com rotulos textuais completos.
- **Modo Compacto / Retratil**: Largura de `5rem` (`w-20`), exibindo icones centralizados acompanhados de tooltips contextuais flutuantes para operacao rapida sem poluicao visual.
- **Persistencia**: Preferencia de colapso sincronizada em `localStorage.sigac_sidebar_collapsed`.
- **Modo Mobile (< 768px)**: Gaveta lateral retratil (off-canvas drawer) com bloqueio de rolagem do body, backdrop escurecido e fechamento em clique externo ou tecla `Escape`.

### 3.2. Barra Superior de Contexto e Busca (`Topbar.jsx`)
- Fornece contexto claro do modulo em exibicao sem redundancias textuais.
- Centraliza o componente de busca global **HealthSearch**, permitindo busca de colaboradores, exames e clinicas em janela modal com acionamento pelo teclado (`Ctrl + K`).
- Exibe o sino de alertas com indicacao quantitativa de pendencias normativas e menu de sessao com encerramento seguro.

### 3.3. Area de Trabalho Central e Bento Grid
- **Container**: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6`.
- **Bento Grid**: Distribuicao em malha responsiva de 12 colunas no Tailwind CSS (`grid grid-cols-12 gap-6`).
  - Cartoes de Indicadores Primarios: Blocos proporcionais (`col-span-12 sm:col-span-6 lg:col-span-3`).
  - Painel de Acoes Prioritarias e Vencimentos: Bloco central (`col-span-12 lg:col-span-8`).
  - Painel Lateral de Atividades e Resumo: Bloco secundario (`col-span-12 lg:col-span-4`).

---

## 4. Primitivas de Componentes Reutilizaveis (`src/components/ui/index.jsx`)

Componentes atomicos padronizados para garantir uniformidade visual e conformidade de acessibilidade:

### 4.1. `Button`
- **Variantes**:
  - `primary`: Fundo `#0B2545`, texto branco, sombra sutil (`bg-primary text-white hover:bg-primary-light`).
  - `secondary`: Fundo neutro com borda suave (`bg-surface-subtle text-slate-900 border border-border`).
  - `accent`: Fundo `#F5A623`, texto preto de alto contraste (`bg-accent text-slate-950 hover:bg-accent-hover`).
  - `outline`: Sem fundo, contorno rigido (`border border-slate-300 text-slate-900 hover:bg-slate-50`).
  - `ghost`: Sem borda ou fundo inicial (`text-slate-700 hover:bg-slate-100`).
  - `danger`: Fundo vermelho escuro para delecao/anulacao (`bg-rose-600 text-white hover:bg-rose-700`).
- **Estados**: Indicador de carregamento integrado via spinner SVG e preservacao de contraste no estado `disabled`.

### 4.2. `Input` e `DateInput`
- **Fundo**: Branco solido (`bg-white`).
- **Contorno**: Borda nitida (`border-slate-300`), anel de foco visivel (`focus:ring-2 focus:ring-primary/20 focus:border-primary`).
- **Tipografia**: Texto em `text-slate-900`, placeholder em `placeholder:text-slate-400`.
- **Especializacao `DateInput`**: Componente customizado com mascara automatica no padrao brasileiro (`DD-MM-YYYY`), botao acionador do seletor nativo de calendario do sistema operacional (`input.showPicker()`) e sanitizacao de valores invalidos.

### 4.3. `Select` Customizado
- Elimina inconsistencias de renderizacao de menus nativos dos navegadores.
- Dropdown acessivel com manipulacao de foco, busca rapida de itens e suporte a teclado.

### 4.4. `Modal`
- Backdrop com efeito de vidro fosco (`bg-slate-900/60 backdrop-blur-sm`).
- Prevenção de perda de foco (focus trap).
- Fechamento imediato por clique na regiao externa ou tecla `Escape`.
- Animacao integrada de escala e opacidade via Anime.js v4 (`animateModalEnter` e `animateModalExit`).

### 4.5. `Table`, `Thead`, `Tbody`, `Tr`, `Th`, `Td`
- Container responsivo com rolagem horizontal controlada (`overflow-x-auto`).
- Linhas com efeito hover sutil (`hover:bg-slate-50/80`).
- Cabecalhos em caixa alta com tipografia escurecida (`text-slate-700 text-xs font-semibold uppercase tracking-wider`).

---

## 5. Microinteracoes e Animacoes (`animejs` v4)

Todas as microinteracoes estao concentradas no modulo `src/lib/animations.jsx`:

1. **Stagger de KPIs (`useKpiAnimation`)**:
   - Disparo sequencial nos cartoes de indicadores com atraso escalonado de 70 milissegundos.
   - Variacao suave de opacidade (`0 -> 1`) e translação vertical no eixo Y (`12px -> 0px`).
2. **Entrada e Saida de Modais**:
   - Curva de transicao acelerada por hardware (`cubic-bezier` / `easeOutCubic`, 250ms).
   - Escala inicial de 95% para 100%, sincronizada com opacidade.
3. **Transicao de Rotas (`RouteTransition`)**:
   - Fade suave sem reflows de pagina, mantendo a sensacao de aplicacao nativa.
4. **Resiliencia de Carregamento Assincrono (`lazyWithRetry`)**:
   - Mecanismo que encapsula o carregamento sob demanda (`React.lazy`) com retry automatico de chunks em caso de falha de conexao.

---

## 6. Diretrizes Mandatorias de Acessibilidade e Engenharia Visual

Conforme documentado no `AGENTS.md` do repositorio:

1. **Politica de Zero Emojis**:
   - E expressamente proibido o uso de caracteres de emoji em qualquer elemento de interface, cabecalho, texto de ajuda, botao ou aviso.
   - Toda iconografia e provida exclusivamente por SVGs otimizados da biblioteca `@heroicons/react`.
2. **Alto Contraste Estrito (Anti-Washout)**:
   - Proibido qualquer elemento visual com fundo claro e texto claro (ex: `bg-slate-50 text-slate-400`).
   - Campos de leitura e desabilitados devem exibir fundo `bg-slate-100` e tipografia nítida `text-slate-800` ou `text-slate-900`.
   - Badges de alerta utilizam fundo saturado atenuado com texto na tonalidade mais escura da escala correspondente (ex: fundo `bg-rose-50`, texto `text-rose-950`, borda `border-rose-200`).
3. **Navegabilidade Acessivel**:
   - Elementos acionaveis possuem indicadores de foco nitidos (`outline-none focus:ring-2 focus:ring-primary`).
   - Suporte completo a operacao por teclado em todos os modais e gavetas.

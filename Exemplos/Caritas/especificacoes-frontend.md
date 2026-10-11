# CARITAS — Visão Geral, Funcionalidades e Especificações do Front-End

> **Documento Oficial de Engenharia e Produto**  
> **Sistema:** CARITAS — Plataforma Clínica e Sistema de Anamnese Digital para Psicólogas(os)  
> **Data:** Outubro de 2026

---

# PARTE 1: A Ideia, Propósito e Funcionalidades do Caritas

## 1. Identidade e Proposta de Valor

O **CARITAS** é uma plataforma clínica e sistema de prontuário eletrônico inteligente desenvolvido sob medida para **psicólogas, psicólogos e clínicas de psicologia**. 

O seu nome tem origem no termo latino para **zelo, dedicação, acolhimento e cuidado humano** — princípios que fundamentam toda a experiência de usuário e a arquitetura técnica da plataforma.

### Principais Dores que o Sistema Resolve:
1. **Sobrecarga Burocrática:** Elimina horas gastas preenchendo prontuários repetitivos ou organizando papelada e fichas dispersas.
2. **Fragilidade de Segurança em Prontuários Físicos e Planilhas:** Garante sigilo e isolamento rígido de registros de evolução psicológica.
3. **Insegurança Jurídica e Normativa:** Cumpre de forma nativa e automática as resoluções do Conselho Federal de Psicologia (CFP) e os requisitos da Lei Geral de Proteção de Dados (LGPD).
4. **Desconexão entre Clínica, Agenda e Faturamento:** Reúne histórico do paciente, agendamento de sessões e conciliação de pagamentos (com PIX) em uma interface unificada.

---

## 2. Pilares de Segurança, Ética e Conformidade Legal

Por tratar **Dados Pessoais Sensíveis de Saúde** (Art. 5º, II e Art. 11 da LGPD - Lei 13.709/2018), o sistema implementa medidas rigorosas de governança:

1. **Isolamento de Dados Multi-Tenancy Rígido:**
   Cada psicólogo possui acesso exclusivo aos seus próprios pacientes, sessões, anotações e finanças. No banco de dados, o isolamento é assegurado por regras de segurança e Row Level Security (RLS).
2. **Guarda Documental Obrigatória de 5 Anos (Resolução CFP nº 01/2009):**
   O prontuário psicológico não pode sofrer expurgo físico imediato, mesmo após solicitações de exclusão cadastral. O sistema realiza a **anonimização cadastral** (desvincula identificadores como CPF e telefone, preservando a integridade temporal do prontuário exigida pelo CFP).
3. **Soft-Delete com Lixeira de 7 Dias:**
   Registros clínicos apagados permanecem em quarentena segura com aviso de conformidade, evitando perdas acidentais de informações terapêuticas.
4. **Trilha de Auditoria Append-Only (Art. 37 da LGPD):**
   Toda visualização de prontuário, login, autenticação 2FA, alteração clínica ou exportação de PDF gera um log imutável com data, hora, autor e ação, sem permissão de alteração ou deleção posterior.
5. **Autenticação Segura com Verificação em Duas Etapas (2FA):**
   Suporte a código de verificação, detecção de dispositivo confiável, encerramento automático de sessão por inatividade e redefinição protegida de senha.

---

## 3. Funcionalidades Clínicas e de Atendimento

### 📋 Prontuário Eletrônico e Cadastro de Pacientes
* Cadastro ágil com dados demográficos, contatos de emergência, filiação e locais de atendimento.
* Linha do tempo clínica com histórico de sessões anteriores, temas trabalhados e arquivos anexos.
* Busca Global instantânea via atalho (`Ctrl+K` ou `⌘+K`) para localizar pacientes ou executar comandos rápidos em milissegundos.

### 📝 Anamnese Estruturada e Questionários Personalizados
* **Modelos Guiados de Anamnese:** Formulários especializados para pacientes Adultos e Adolescentes, divididos em etapas lógicas (aspectos demográficos, queixa principal, história pessoal, dinâmica familiar, saúde física, avaliação de risco e metas terapêuticas).
* **Criador de Questionários Personalizados (`QuestionarioBuilder`):** Permite criar formulários dinâmicos com campos de texto curto, texto longo, múltipla escolha, listas suspensas, escalas de 1 a 10 e datas.
* Auto-salvamento em tempo real com debounce para prevenir perda acidental de dados digitados durante a sessão.

### 🧠 Evolução de Sessão e Resumo Clínico com I.A.
* Registro rápido de sessões com status de comparecimento (Presente, Faltou, Cancelado), técnicas interventivas, tarefas de casa e hipóteses clínicas.
* **Resumo Clínico com Inteligência Artificial (OpenAI GPT-4o-mini):** Processa as anotações do psicólogo e sintetiza um resumo técnico padronizado em 3ª pessoa, mantendo terminologia clínica e sem substituir o julgamento profissional.
* Acompanhamento visual da escala de humor do paciente ao longo do tempo (`MoodChart`).

### 📜 Emissão de Documentos Oficiais CFP (Resolução nº 06/2019)
Exportação e download em PDF padronizado com cabeçalho, número de CRP e formatação técnica:
* **Declaração Psicológica:** Comprovação de comparecimento e acompanhamento.
* **Atestado Psicológico:** Diagnósticos e aptidão para fins legais e de saúde.
* **Relatório Psicológico / Encaminhamento:** Comunicação com médicos, psiquiatras e escolas.
* **Recibo de Reembolso:** Para operadoras de planos de saúde e declaração de Imposto de Renda.
* **Prontuário Total em PDF:** Cópia completa do histórico temporal para perícias ou guarda física.

---

## 4. Gestão do Consultório, Agenda e Finanças

### 📅 Agenda Inteligente e Link Público
* Calendário com visão diária, semanal e mensal de compromissos.
* Agendamentos recorrentes (semanais/quinzenais) com projeção automática de datas.
* **Link Público de Agendamento (`/agendar/:slug`):** O psicólogo configura seus dias, horários e intervalos de atendimento. O paciente acessa o link, solicita o horário e o profissional confirma com integração direta para envio de mensagem no WhatsApp.

### 💳 Controle Financeiro e Cobrança com PIX
* Faturamento consolidado do consultório: sessões pagas, a receber e pendentes.
* **Geração Automática de PIX (Padrão Banco Central / BR Code EMV):** Gera payload *Copia e Cola* e QR Code offline instantaneamente.
* Disparo de cobrança amigável via WhatsApp com dados da sessão e link de pagamento.
* Relatórios e balanços financeiros exportáveis em PDF.

---

## 5. Arquitetura Multi-Perfil e Gestão de Clínicas

* **Psicólogo Clínico:** Foco integral na rotina de atendimentos e prontuários próprios, com limites padrão configurados (ex.: 20 pacientes no plano de entrada).
* **Líder Clínico (Gestão de Clínicas Compartilhadas):**
  * Perfil gestor responsável por supervisionar uma equipe de até **8 psicólogos cadastrados**.
  * Visualiza métricas agregadas de produtividade, taxa de ocupação e volume de atendimentos da clínica **sem quebrar o sigilo profissional das anotações confidenciais de cada psicólogo**.
* **Super Administrador e Auditoria:**
  * Monitoramento de segurança, trilha de auditoria global e gestão de contratos corporativos.
  * Relatórios acadêmicos de usabilidade baseados no **Framework DECIDE**, permitindo gerar planilhas analíticas de interação.
* **Assinaturas Recorrentes (Gateway Asaas):**
  * Gestão de mensalidades via cartão de crédito ou PIX, com 14 dias de teste gratuito (*trial*), carência de segurança de 3 dias e tela de regularização automática (`AssinaturaPendente`).

---

# PARTE 2: Especificações Técnicas do Front-End

## 1. Stack Tecnológica

| Camada | Tecnologia | Detalhes e Justificativa |
|---|---|---|
| **Core Framework** | **React 19.2** | Componentes funcionais puros, Context API para estado global, lazy loading nativo com `Suspense` e Hooks modernos. |
| **Build Tool** | **Vite 8** | Servidor HMR instantâneo em ESM e compilação de produção com tree-shaking e divisão otimizada de chunks. |
| **Roteamento** | **React Router DOM v7** | Roteamento declarativo SPA com sincronização bidirecional entre URL e estado interno. |
| **Estilização** | **Tailwind CSS 3.4** | Utility-first CSS com `darkMode: ['selector', '[data-theme="dark"]']` e classes padronizadas via `@layer`. |
| **Biblioteca de Ícones** | **Lucide React** | Mais de 40 ícones SVG semânticos vetoriais de traço limpo (zero emojis informais na interface). |
| **Gráficos** | **Recharts 3.8** | Gráficos responsivos de barras (financeiro) e linhas (evolução do humor do paciente). |
| **Exportação PDF** | **jsPDF 2.5** | Renderização client-side de PDFs vetorizados em milímetros, com cabeçalhos e carimbos regulatórios do CFP. |

---

## 2. Tipografia e Hierarquia Visual

| Uso | Família Tipográfica | Pesos Utilizados | Finalidade |
|---|---|---|---|
| **Títulos, Branding e Destaques** | **`Sora`** (`font-heading`) | `500` (Medium), `600` (SemiBold) | Transmite modernidade, clareza e autoridade institucional médica em `<h1>` até `<h6>`. |
| **Corpo, Formulários e Tabelas** | **`Inter`** (`font-sans`) | `400` (Regular), `500` (Medium) | Alta legibilidade em textos corridos, prontuários, campos de input e elementos densos. |

```css
/* Declaração de estilos-base (src/index.css) */
body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-wrap: anywhere;
}

h1, h2, h3, h4, h5, h6 {
  font-family: 'Sora', 'Inter', system-ui, sans-serif;
}
```

---

## 3. Paleta de Cores e Tokens Visuais (Design System)

Todas as cores são orquestradas por **Variáveis CSS nativas** definidas nos seletores `:root` / `[data-theme="light"]` e `[data-theme="dark"]` em [src/index.css](file:///c:/Projetos%20Faculdade/Anamnese/src/index.css):

### 3.1. Superfícies e Fundos
| Token CSS | Modo Claro (Light) | Modo Escuro (Dark) | Aplicação |
|---|---|---|---|
| `--bg-primary` | `#F8F9FA` | `#0D1117` | Fundo geral da aplicação |
| `--bg-secondary` | `#FFFFFF` | `#161B22` | Fundo de seções secundárias e cards de destaque |
| `--bg-sidebar` | `#0A1628` (Azul Meia-Noite) | `#010409` (Preto Profundo) | Barra lateral de navegação fixa |
| `--bg-card` | `#FFFFFF` | `#161B22` | Cards, modais e containers de dados |
| `--overlay` | `rgba(0, 0, 0, 0.5)` | `rgba(0, 0, 0, 0.7)` | Fundo escurecido e desfocado de modais |

### 3.2. Tipografia e Contraste
| Token CSS | Modo Claro (Light) | Modo Escuro (Dark) | Aplicação |
|---|---|---|---|
| `--text-primary` | `#0A1628` | `#E6EDF3` | Títulos e texto principal de alto contraste |
| `--text-secondary` | `#4A5568` | `#8B949E` | Parágrafos explicativos e legendas |
| `--text-muted` | `#718096` | `#6E7681` | Metadados, datas, contadores e placeholders |
| `--text-sidebar` | `#CBD5E1` | `#8B949E` | Links inativos da sidebar |
| `--text-sidebar-active` | `#FFFFFF` | `#E6EDF3` | Link da rota ativa na sidebar |

### 3.3. Cor de Acentuação (Brand / Accent)
| Token CSS | Modo Claro (Light) | Modo Escuro (Dark) | Aplicação |
|---|---|---|---|
| `--accent` | `#2563EB` (Azul Real) | `#3B82F6` (Azul Cobalto) | Botões primários, focos e estados ativos |
| `--accent-light` | `#EFF6FF` | `#1D2D3E` | Fundo de badges e seleções suaves |
| `--accent-hover` | `#1D4ED8` | `#60A5FA` | Efeito hover sobre elementos acentuados |

### 3.4. Status Clínicos Semânticos
| Status | Cor Base | Background (Light / Dark) | Texto Semântico |
|---|---|---|---|
| **Success** (Presente / Pago) | `#16A34A` / `#22C55E` | `#F0FDF4` / `rgba(34,197,94,0.1)` | `#166534` / `#86EFAC` |
| **Warning** (Pendente / Trial) | `#D97706` / `#F59E0B` | `#FFFBEB` / `rgba(245,158,11,0.1)` | `#92400E` / `#FCD34D` |
| **Danger** (Faltou / Inadimplente) | `#DC2626` / `#EF4444` | `#FEF2F2` / `rgba(239,68,68,0.1)` | `#991B1B` / `#FCA5A5` |
| **Info** (Agendado / Regular) | `#2563EB` / `#3B82F6` | `#EFF6FF` / `rgba(59,130,246,0.1)` | `#1E40AF` / `#93C5FD` |

### 3.5. Bordas, Sombras e Elementos de Formulário
| Token CSS | Modo Claro (Light) | Modo Escuro (Dark) | Aplicação |
|---|---|---|---|
| `--border` | `rgba(0, 0, 0, 0.08)` | `rgba(255, 255, 255, 0.08)` | Divisores de cards e tabelas |
| `--shadow` | `0 2px 12px rgba(0,0,0,0.06)` | `0 2px 12px rgba(0,0,0,0.30)` | Elevação de containers |
| `--input-bg` | `#FFFFFF` | `#0D1117` | Fundo de caixas de entrada |
| `--input-border`| `rgba(0, 0, 0, 0.12)` | `rgba(255, 255, 255, 0.12)` | Borda padrão de inputs |
| `--scrollbar-thumb`| `#CBD5E1` | `#30363D` | Barra de rolagem customizada |

---

## 4. Classes Utilitárias Padronizadas (`ds-*`)

Definidas na camada `@layer components` do Tailwind:

* **`.ds-card`:**
  Container padrão para agrupar informações clínicas, com cantos de 8px e borda suave.
* **`.ds-btn` e Variantes:**
  * `ds-btn-primary`: Ação principal do fluxo (Salvar, Criar, Confirmar).
  * `ds-btn-secondary`: Ação neutra ou de retorno.
  * `ds-btn-danger`: Ações destrutivas (Excluir paciente, Desativar conta).
  * `ds-btn-ghost`: Ações terciárias sem contorno.
* **`.ds-input`:**
  Padronização para `<input>`, `<textarea>` e `<select>`. Possui transição de foco para `--accent` e adaptação automática de contraste no tema escuro.
* **`.ds-badge`:**
  Pills compactas para identificação de plano (`Pro` / `Básico`), estado de presença e faturamento.

---

## 5. Composição de Layout e Casca da Aplicação (`Layout.jsx`)

```
┌────────────────────────────────────────────────────────────────────────┐
│  Layout.jsx (Shell Global)                                             │
│ ┌───────────────┬────────────────────────────────────────────────────┐ │
│ │  Sidebar      │  Header Contextual                                 │ │
│ │  (220px fixo) │  [Busca Global Ctrl+K] [Ajuda] [Tema] [Logout]     │ │
│ │               ├────────────────────────────────────────────────────┤ │
│ │  • Dashboard  │                                                    │ │
│ │  • Pacientes  │  Área de Conteúdo (React Router / Dynamic Views)   │ │
│ │  • Nova Sessão│                                                    │ │
│ │  • Agenda     │  <Suspense fallback={<LoadingSpinner />}>          │ │
│ │  • Financeiro │    {children}                                      │ │
│ │  • Meu Plano  │  </Suspense>                                       │ │
│ │  • Líder*     │                                                    │ │
│ │  • Questionár.│                                                    │ │
│ │  • Clínicas   │                                                    │ │
│ │  • Lixeira    │                                                    │ │
│ └───────────────┴────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```

### Componentes de Estrutura:
1. **Sidebar (`aside`):**
   * Largura de `220px` no desktop; gaveta deslizante (*drawer*) retrátil no mobile.
   * Fundo contínuo escuro (`--bg-sidebar`) mantendo contraste elegante.
   * Itens com ícones Lucide de 18px e indicador visual de rota ativa.
   * Condicional de perfil: o item **Líder Clínico** só é montado para gestores de clínica.
2. **Header Contextual:**
   * Barra superior fina integrada ao topo da área de trabalho.
   * Atalho para Busca Global (`GlobalSearch.jsx`).
   * Alternador de tema (`ThemeContext.jsx`) persistido em `localStorage`.
   * Central de Ajuda deslizante (`HelpPanel.jsx`).
   * Botão de encerramento de sessão com confirmação modal (`ConfirmDialog.jsx`).
3. **Área de Conteúdo Principal:**
   * Rolagem independente com barra fina estilizada (`*::-webkit-scrollbar`).
   * Espaçamento interno padronizado (`p-6` a `p-8`) e contenção contra transbordamento horizontal.

---

## 6. Otimização de Performance e Code-Splitting

Para garantir renderização instantânea do Dashboard, os módulos secundários e mais volumosos são carregados sob demanda via **`React.lazy` + `Suspense`** em [src/App.jsx](file:///c:/Projetos%20Faculdade/Anamnese/src/App.jsx):

```javascript
const AdminPanel            = lazy(() => import('./components/AdminPanel'));
const Agenda                = lazy(() => import('./components/Agenda'));
const Financas              = lazy(() => import('./components/Financas'));
const Questionarios         = lazy(() => import('./components/Questionarios'));
const Clinicas              = lazy(() => import('./components/Clinicas'));
const Lixeira               = lazy(() => import('./components/Lixeira'));
const LiderClinicoDashboard = lazy(() => import('./components/lider/LiderClinicoDashboard'));
const PerfilEPlano          = lazy(() => import('./components/PerfilEPlano'));
const AssinaturaPendente    = lazy(() => import('./components/AssinaturaPendente'));
```

Isso reduz a carga do pacote inicial de JavaScript em mais de **60%**, deixando módulos como geradores de relatórios e painéis administrativos para download apenas quando solicitados.

---

## 7. Componentes de UI Desacoplados (`src/components/ui/`)

* **`Button.jsx`:** Componente polimórfico com suporte a variantes (`primary`, `secondary`, `danger`, `ghost`), tamanhos (`sm`, `md`, `lg`), estados de loading e desabilitação acessível.
* **`Card.jsx` (`CardHeader`, `CardBody`):** Divisão arquitetural de contêineres com bordas semânticas.
* **`Badge.jsx`:** Pílulas de estado com suporte a ícones inline e variantes semânticas.
* **`Pagination.jsx`:** Paginação completa com reticências dinâmicas (`...`), contagem de registros e versão simplificada para dispositivos móveis.

---

## 8. Engenharia de Usabilidade e Interação Humano-Computador (IHC)

1. **Avaliação por Heurísticas de Nielsen:**
   O sistema alcançou nota **4.55 / 5.00** em auditoria técnica de usabilidade médica.
2. **Prevenção de Erros (H5):**
   * Diálogos modais de confirmação em ações destrutivas (`ConfirmDialog.jsx`).
   * Auto-salvamento em formulários extensos de anamnese para evitar perda de dados por oscilação de rede.
3. **Flexibilidade e Atalhos Ergonômicos (H7):**
   * `Ctrl + K` / `⌘ + K`: Busca Global instantânea de qualquer tela.
   * `Ctrl + S` / `⌘ + S`: Salva a evolução ou anamnese em edição.
   * `Esc`: Fecha modais, gavetas e painéis abertos.
4. **Feedback Imediato (H1):**
   * Notificações flutuantes via `ToastContext.jsx` com até 4 alertas em pilha e auto-dismiss.
   * Feedback de progresso assíncrono (spinners animados `RefreshCw`, skeletons e botões em loading).
5. **Polimento Visual:**
   * Zero emojis informais; 100% dos ícones renderizados como vetores SVG semânticos da biblioteca **Lucide**.

# 🎨 Especificações Técnicas e Arquitetura Front-End — Plataforma Urbis

> **Documento Técnico de Referência**: Detalhamento completo da interface visual, Design System, paleta de cores, tipografia, componentes e arquitetura dos dois ecossistemas front-end da plataforma **Urbis** (Aplicativo Mobile do Cidadão e Painel Web Administrativo).

---

## 1. Visão Geral dos Front-Ends

A plataforma **Urbis** é composta por duas aplicações front-end distintas e complementares:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           FRONT-ENDS DA PLATAFORMA URBIS                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   📱 APP MOBILE DO CIDADÃO                 🖥️ PAINEL WEB ADMINISTRATIVO          │
│   - React Native 0.81 + React 19           - Next.js 14 (App Router)            │
│   - Expo SDK 54 (TypeScript)               - TypeScript + Tailwind CSS          │
│   - Expo Router (File-based navigation)    - React Leaflet (Mapas & Heatmap)    │
│   - Câmera, Áudio, GPS Nativo              - Recharts (Gráficos analíticos)     │
│   - Foco: Munícipe / Simplicidade / Offline - Foco: Operador / Mesa de Despacho  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Design System & Paleta de Cores

O Design System baseia-se em uma escala cromática cívica institucional (tons de azul profundo, ciano e neutros limpos), com sinalização semântica padronizada de status.

### 2.1. Tokens Principais da Paleta (`constants/theme.ts` + Tailwind)

| Nome do Token | Valor Hexadecimal | Aplicação Semântica | Onde é Usado |
| :--- | :--- | :--- | :--- |
| **Navy Principal** | `#03045E` / `#243d80` | Cor de autoridade, títulos H1/H2, headers institucionais, ícones inativos | Barra superior do app, sidebar web, textos de cabeçalho |
| **Ocean Secundário** | `#0077B6` | Ação primária, botões principais, links, foco de formulário | Botões "Próximo", "Enviar", lupa de busca, FAB |
| **Sky / Accent** | `#00B4D8` | Destaques visuais, ícones ativos de navegação, status intermediários | Aba ativa da barra inferior, bordas destacadas |
| **Aqua Suave** | `#90E0EF` | Elementos neutros, divisórias sutis, bordas de cards | Separadores de listas, bordas de fotos e inputs |
| **Ice Background** | `#CAF0F8` | Fundos de cards informativos, preenchimento de inputs de formulário | Cards de eventos, inputs no mobile, tags neutras |
| **Frost** | `#E0F7FA` | Fundo de seleção ativa e chips | Categoria de chamado selecionada, badges de filtro |
| **Superfície Clara** | `#FFFFFF` | Fundo de telas do app, cards do painel web | Background de visualização, cartões brancos |
| **Fundo Web** | `#F8FAFC` | Fundo do dashboard desktop | Layout central do Next.js |
| **Texto Primário** | `#1A1C1C` / `#243d80` | Alto contraste para leitura de corpo e dados | Textos corridos, dados do cidadão na tabela |
| **Texto Secundário** | `#464651` / `#777682` | Textos auxiliares, legendas, metadados | Endereços, datas, descrições secundárias |

### 2.2. Semântica de Status das Ocorrências

| Status | Cor do Texto/Ícone | Cor de Fundo (Badge) | Significado Visual |
| :--- | :--- | :--- | :--- |
| **Pendente** | `#BA1A1A` | `#FFDAD6` | Vermelho alerta: chamado recém-aberto aguardando triagem |
| **Em Análise** | `#856404` | `#FFF3CD` | Amarelo/Dourado: chamado em avaliação técnica pela secretaria |
| **Em Andamento**| `#0077B6` | `#CAF0F8` | Azul oceano: equipe deslocada para resolução em campo |
| **Resolvido** | `#38B000` | `#D1FAE5` | Verde sucesso: serviço executado e finalizado |
| **Rejeitado** | `#464651` | `#E2E2E2` | Cinza neutro: chamado cancelado, duplicado ou sem pertinência |

---

## 3. Tipografia e Iconografia

### 3.1. Tipografia
* **App Mobile**: Famílias de fontes nativas do sistema operacional (San Francisco no iOS, Roboto no Android) para máxima fidelidade e performance:
  * Títulos principais: `fontWeight: '700'` ou `'800'`, `letterSpacing: -0.5`;
  * Rótulos e botões: `fontWeight: '600'`;
  * Corpo de texto: `fontWeight: '400'` ou `'500'`, tamanho base `14px` a `16px`.
* **Painel Web**: Fontes sans-serif modernas e legíveis (Inter / Manrope via classes Tailwind):
  * Títulos: `font-extrabold text-[22px] text-[#243d80]`;
  * Subtítulos: `text-[13px] text-[#777682]`;
  * Células de tabelas: `text-sm font-medium`.

### 3.2. Iconografia
* **App Mobile**: Biblioteca `@expo/vector-icons` com foco em:
  * **Feather Icons**: Ícones minimalistas outline (`alert-circle`, `trash-2`, `cloud-rain`, `map-pin`, `camera`, `mic`, `shield`, `chevron-right`);
  * **MaterialIcons**: Utilizado pontualmente para o botão flutuante de ouvidoria (`support-agent`).
* **Painel Web**: **Lucide React**: Ícones SVG leves, consistentes e escaláveis (`FileText`, `Clock`, `CheckCircle`, `RefreshCcw`, `Users`, `AlertTriangle`, `MapPin`, `Search`).

---

## 4. Arquitetura Front-End Mobile (React Native / Expo)

### 4.1. Stack Tecnológica
* **Framework**: React Native `0.81.5` + React `19.1.0`;
* **Plataforma**: Expo SDK `54.0.33` (TypeScript `~5.9.2`);
* **Roteamento**: `expo-router ~6.0.23` (File-based Routing baseado em diretórios);
* **Estilização**: `StyleSheet.create` local por componente, evitando bibliotecas CSS-in-JS pesadas para garantir 60fps;
* **Navegação Segura**: `react-native-safe-area-context` para proteção contra *notch* e bordas arredondadas de aparelhos modernos.

### 4.2. Estrutura de Rotas e Telas (`app/`)
```
app/
├── _layout.tsx               # Root Stack, provedor de contexto de autenticação e temas
├── splash.tsx                # Splash screen animada com degradê linear (0A2463 -> 247BA0)
├── auth/
│   ├── _layout.tsx           # Stack de autenticação
│   ├── login.tsx             # Login com e-mail/senha e validação
│   └── register.tsx          # Cadastro completo com máscara dinâmica de CPF, RG e Telefone
├── (tabs)/
│   ├── _layout.tsx           # Barra inferior fixa com 5 abas estilizadas
│   ├── index.tsx             # Início: Alertas da Defesa Civil, destaques e eventos
│   ├── relatar.tsx           # Etapa 1: Seleção da categoria do problema
│   ├── monitorar.tsx         # Acompanhamento das ocorrências do munícipe em tempo real
│   ├── turismo.tsx           # Guia de pontos turísticos, rotas seguras e busca com filtros
│   └── perfil.tsx            # Perfil do cidadão, switches de acessibilidade e logout
└── relato/
    ├── _layout.tsx           # Sub-stack modal do fluxo de chamado
    ├── evidencias.tsx        # Etapa 2: Captura de foto nativa, nota de áudio e GPS
    ├── confirmar.tsx         # Etapa 3: Revisão, descrição complementar e envio
    └── sucesso.tsx           # Confirmação visual com animação de mola
```

### 4.3. Integração com Recursos Nativos do Aparelho
* **Geolocalização (`expo-location`)**:
  * Captura de coordenadas precisas (`latitude`, `longitude`);
  * *Reverse Geocoding* automático convertendo coordenadas em nome da rua, número aproximado e bairro.
* **Câmera e Galeria (`expo-image-picker`)**:
  * Limite rigoroso de até 3 evidências fotográficas;
  * Redimensionamento automático pré-upload para economia de dados do munícipe.
* **Áudio (`expo-av`)**:
  * Gravação de mensagens de voz explicativas para acessibilidade de idosos e pessoas com deficiência.

---

## 5. Arquitetura Front-End Web (Next.js 14)

### 5.1. Stack Tecnológica
* **Framework**: Next.js 14 (App Router) + React 18/19;
* **Estilização**: Tailwind CSS (arquitetura utility-first);
* **Cartografia**: React Leaflet + `leaflet.heat` (mapas interativos e manchas de calor);
* **Gráficos**: Recharts (gráficos de linha de evolução temporal e barras por categoria).

### 5.2. Estrutura de Diretórios (`tacaratu-painel/src/app/`)
```
src/app/
├── layout.tsx                # Shell global: Sidebar institucional, Header e AuthProvider
├── page.tsx                  # Dashboard principal: KPIs, Mapa de Calor e Gráficos
├── relatos/
│   ├── page.tsx              # Tabela gerencial de ocorrências com busca e filtros dinâmicos
│   └── [id]/page.tsx         # Prontuário individual: fotos ampliadas, áudio, mapa e moderação
├── conteudo/
│   └── page.tsx              # CMS de Alertas Municipais e Banners do app do munícipe
├── turismo/
│   └── page.tsx              # Cadastro e moderação de pontos turísticos
├── usuarios/
│   └── page.tsx              # Tabela da base de cidadãos com dados mascarados (LGPD)
└── configuracoes/
    └── page.tsx              # Segurança, permissões de operadores e auditoria
```

### 5.3. Componentes Estratégicos
* **Mapa de Calor (`HeatMap.tsx`)**:
  * Renderiza mapa OpenStreetMap com camada *Heatmap* baseada nos pontos GPS dos chamados abertos pela população;
  * Identifica manchas geográficas críticas de buracos, lixo ou falta de iluminação.
* **Prontuário de Moderação**:
  * Permite ao funcionário público alterar o status e registrar obrigatoriamente a justificativa técnica;
  * Alimenta a tabela `status_historico` para auditoria do Tribunal de Contas e Ouvidoria.

---

## 6. Padrões de UX, Interação e Animações

### 6.1. Animações de Entrada de Tela (Mobile)
Todas as telas do aplicativo implementam transições fluidas via React Native `Animated`:
```tsx
// Padrão consistente de entrada: Fade-in combinado com Slide-up de 20px
Animated.parallel([
  Animated.timing(fadeAnim, {
    toValue: 1,
    duration: 500,
    useNativeDriver: true,
  }),
  Animated.timing(slideAnim, {
    toValue: 0,
    duration: 500,
    useNativeDriver: true,
  }),
]).start();
```

### 6.2. Microinterações Especiais
* **Gravação de Áudio (`evidencias.tsx`)**: Efeito de pulso contínuo no ícone de microfone durante a captura da mensagem (`Animated.loop` escalando entre `1.0` e `1.08`);
* **Tela de Sucesso (`sucesso.tsx`)**: Animação de mola física (`Animated.spring`) no círculo de confirmação e no ícone de check;
* **Cards do Dashboard Web**: Efeito hover com elevação suave (`hover:shadow-md hover:border-[#0077B6]/30 transition-all duration-200`).

---

## 7. Acessibilidade e Inclusão Social

* **Modo Alto Contraste**: Alternância nativa no perfil do cidadão que reforça bordas, escurece tipografias e remove fundos de baixo contraste;
* **Leitores de Tela**: Marcação com `accessibilityLabel` e `accessibilityRole` em botões, campos de texto e abas para suporte a TalkBack (Android) e VoiceOver (iOS);
* **Validação Assistida de Formulário**: Mascaramento visual em tempo real no CPF (`000.000.000-00`), RG (`0.000.000`) e Celular (`(00) 00000-0000`), evitando erros de digitação.

---

## 8. Guia de Parametrização White-Label (Venda para Novas Prefeituras)

Como a plataforma **Urbis** foi concebida para comercialização modular a múltiplos municípios:

1. **Customização de Cores**: Alteração centralizada nos arquivos `constants/theme.ts` (Mobile) e `tailwind.config.ts` (Web) para aplicar as cores oficiais da bandeira ou brasão da cidade contratante;
2. **Identidade Visual**: Troca simples dos ativos visuais em `assets/images/` (ícone do app, splash screen e favicon);
3. **Parâmetros da Instância**: Nome do município, secretarias cadastradas e categorias de serviços municipais carregadas dinamicamente via banco de dados (`supabase`), sem necessidade de reescrever código.

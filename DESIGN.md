---
name: NOXXD
description: Software house portfolio. One square teal-and-gold frame holding three product worlds.
colors:
  noxxd-teal: "#1B5E6B"
  noxxd-teal-dark: "#154B56"
  noxxd-deep: "#0E363E"
  noxxd-gold: "#C8975D"
  noxxd-gold-hover: "#D8A76D"
  noxxd-text-light: "#F5F7F8"
  noxxd-text-muted: "#D0C0A7"
  noxxd-grid-line: "rgba(200, 151, 93, 0.07)"
  noxxd-grid-line-bold: "rgba(200, 151, 93, 0.14)"
  urbis-navy: "#03045E"
  urbis-navy-2: "#243d80"
  urbis-ocean: "#0077B6"
  urbis-ocean-deep: "#005f92"
  urbis-sky: "#00B4D8"
  urbis-aqua: "#90E0EF"
  urbis-ice: "#CAF0F8"
  urbis-frost: "#E0F7FA"
  urbis-web: "#F8FAFC"
  urbis-text: "#1A1C1C"
  urbis-text-2: "#464651"
  urbis-status-pendente-bg: "#FFDAD6"
  urbis-status-pendente-fg: "#BA1A1A"
  urbis-status-analise-bg: "#FFF3CD"
  urbis-status-analise-fg: "#856404"
  urbis-status-andamento-fg: "#005f92"
  urbis-status-resolvido-bg: "#D1FAE5"
  urbis-status-resolvido-fg: "#1F6B00"
  urbis-status-rejeitado-bg: "#E2E2E2"
  hs-petroleo: "#0B2545"
  hs-petroleo-light: "#13375e"
  hs-petroleo-soft: "#e3eaf3"
  hs-amber: "#F5A623"
  hs-amber-hover: "#e09510"
  hs-surface: "#f4f6f8"
  hs-card: "#ffffff"
  hs-border: "#dde1e7"
  hs-text: "#1a1f2b"
  hs-text-2: "#4b5563"
  hs-ink-on-amber: "#020617"
  hs-em-dia: "#16a34a"
  hs-a-vencer: "#d97706"
  hs-vencido: "#dc2626"
  hs-solicitado: "#4f46e5"
  hs-agendado: "#0284c7"
  hs-pendente: "#64748b"
  caritas-midnight: "#0A1628"
  caritas-paper: "#F8F9FA"
  caritas-card: "#FFFFFF"
  caritas-text-2: "#4A5568"
  caritas-muted: "#5f6b7d"
  caritas-royal: "#2563EB"
  caritas-royal-hover: "#1D4ED8"
  caritas-royal-light: "#EFF6FF"
  caritas-chip-text: "#1E40AF"
  caritas-dark-bg: "#0D1117"
  caritas-dark-card: "#161B22"
  caritas-dark-text: "#E6EDF3"
  caritas-dark-text-2: "#A5B0BC"
  caritas-dark-royal: "#3B82F6"
  caritas-dark-royal-hover: "#60A5FA"
typography:
  display:
    fontFamily: "Oswald, Archivo Narrow, Arial Narrow, sans-serif"
    fontSize: "clamp(2.5rem, 6.5vw, 4.5rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.06em"
  headline:
    fontFamily: "Oswald, Archivo Narrow, Arial Narrow, sans-serif"
    fontSize: "clamp(1.8rem, 4vw, 2.8rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.06em"
  title:
    fontFamily: "Oswald, Archivo Narrow, Arial Narrow, sans-serif"
    fontSize: "clamp(1.3rem, 2.5vw, 1.8rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.06em"
  body:
    fontFamily: "Josefin Sans, system-ui, -apple-system, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 400
    lineHeight: 1.7
  slogan:
    fontFamily: "Josefin Sans, sans-serif"
    fontSize: "clamp(1rem, 2vw, 1.35rem)"
    fontWeight: 600
    letterSpacing: "0.35em"
  label:
    fontFamily: "Oswald, Arial Narrow, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 700
    letterSpacing: "0.08em"
  urbis-display:
    fontFamily: "Manrope, Inter, system-ui, sans-serif"
    fontSize: "clamp(2.6rem, 6.6vw, 5.6rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.04em"
  urbis-body:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
  hs-display:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.035em"
    fontFeature: "tnum"
  hs-body:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
    fontFeature: "tnum"
  caritas-display:
    fontFamily: "Sora, Inter, system-ui, sans-serif"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.035em"
  caritas-body:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
  case-headline:
    fontSize: "clamp(1.9rem, 3.6vw, 3rem)"
    lineHeight: 1.1
    letterSpacing: "-0.02em"
rounded:
  noxxd: "0px"
  urbis: "18px"
  urbis-sm: "12px"
  hs: "10px"
  hs-sm: "6px"
  caritas: "14px"
  caritas-sm: "8px"
  pill: "999px"
spacing:
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "32px"
  xl: "48px"
  section-home: "90px"
  section-case: "clamp(64px, 9vw, 120px)"
  container: "1200px"
components:
  button-primary:
    backgroundColor: "{colors.noxxd-gold}"
    textColor: "{colors.noxxd-deep}"
    rounded: "{rounded.noxxd}"
    padding: "14px 32px"
    typography: "{typography.label}"
  button-primary-hover:
    backgroundColor: "{colors.noxxd-teal}"
    textColor: "{colors.noxxd-gold}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.noxxd-gold}"
    rounded: "{rounded.noxxd}"
    padding: "14px 32px"
  frame-contact:
    backgroundColor: "{colors.noxxd-gold}"
    textColor: "{colors.noxxd-deep}"
    rounded: "{rounded.noxxd}"
    padding: "9px 18px"
  frame-bar:
    backgroundColor: "{colors.noxxd-teal-dark}"
    textColor: "{colors.noxxd-text-light}"
    height: "60px"
  frame-footer:
    backgroundColor: "{colors.noxxd-gold}"
    textColor: "{colors.noxxd-deep}"
    padding: "28px 0"
  tag:
    textColor: "{colors.noxxd-gold}"
    rounded: "{rounded.noxxd}"
    padding: "4px 10px"
  pixel-card:
    backgroundColor: "{colors.noxxd-teal-dark}"
    rounded: "{rounded.noxxd}"
    padding: "32px 24px"
  case-button-urbis:
    backgroundColor: "{colors.urbis-ocean}"
    textColor: "#FFFFFF"
    rounded: "{rounded.urbis-sm}"
    padding: "12px 24px"
    height: "48px"
  case-button-urbis-hover:
    backgroundColor: "{colors.urbis-ocean-deep}"
  case-button-hs:
    backgroundColor: "{colors.hs-amber}"
    textColor: "{colors.hs-ink-on-amber}"
    rounded: "{rounded.hs-sm}"
    padding: "12px 24px"
    height: "48px"
  case-button-hs-hover:
    backgroundColor: "{colors.hs-amber-hover}"
  case-button-caritas:
    backgroundColor: "{colors.caritas-royal}"
    textColor: "#FFFFFF"
    rounded: "{rounded.caritas-sm}"
    padding: "12px 24px"
    height: "48px"
  case-button-caritas-hover:
    backgroundColor: "{colors.caritas-royal-hover}"
  urbis-status-badge:
    rounded: "{rounded.pill}"
    padding: "8px 14px"
---

# Design System: NOXXD

## Overview

**Creative North Star: "The Square Frame, The Living Products"**

NOXXD is two layers, never blended. The outer layer is the agency itself: a retro-industrial, 8-bit refined world of deep teal ground, a gold blueprint grid, strictly right-angled shapes, Oswald capitals and the wide-tracked Josefin slogan "BUILD IT YOUR WAY". It owns the Home page outright and, on every case page, the sticky top bar and the gold footer band.

The inner layer belongs to each product. Between the NOXXD bar and footer, a case page speaks in its product's own palette, type and corner radius, set through one shared contract of `--p-*` custom properties (background, text, text-2, accent, accent-hover, on-accent, focus, chip, radius, radius-sm, head and body font). The shared primitives (buttons, sections, chips, screenshot slots, CTA band) read only those properties, so a fourth product is a new token block, not new components. Each world shows the product's real state vocabulary as its visual signature: Urbis's occurrence statuses, HealthSearch's NR compliance traffic light, CARITAS's document stack.

Density is moderate and editorial. Motion is short, transform-only, and settles once; every animation disappears under `prefers-reduced-motion`.

**Key Characteristics:**
- Two-layer system: NOXXD frame (square, teal, gold) around a per-product world (`--p-*` tokens).
- Zero radius everywhere in the NOXXD layer; product radii only inside the frame.
- Blueprint grid and 8-bit pixel ornaments (checker dividers, stepped corner tabs, floating gold squares) belong to NOXXD alone.
- Each product world is pinned to its official palette and fonts, never reinterpreted.
- Bilingual PT/EN everywhere; motion is decoration, never the carrier of state.

## Colors

The NOXXD layer is a two-colour brand (deep teal and burnished gold) with warm parchment text; each product world carries its own palette inside the frame.

### Primary
- **Blueprint Teal** (noxxd-teal): the Home ground and button hover fill. The 32px grid is drawn over it.
- **Shadow Teal** (noxxd-teal-dark): card and contact-panel surfaces on Home; the case-page top bar.
- **Abyss Teal** (noxxd-deep): the only ink on gold. Footer copy, social icons, the bar's contact button, the pressed language button.

### Secondary
- **Burnished Gold** (noxxd-gold): headings, borders, links, primary button fill, footer band, pixel ornaments and particles.
- **Lit Gold** (noxxd-gold-hover): hover borders, focus ring, the footer's top rule.

### Neutral
- **Parchment White** (noxxd-text-light): body text on teal.
- **Old Paper** (noxxd-text-muted): lead paragraphs, stack lines, inactive language buttons.
- **Grid Gold** (noxxd-grid-line, noxxd-grid-line-bold): the 32px minor and 128px major blueprint lines.

### Product worlds (inside the frame only)
- **Urbis:** Harbour Navy (urbis-navy) hero ground ruled as a 168px/42px street grid. Ocean (urbis-ocean) is the action on light; Sky (urbis-sky) is the action and focus on navy, with navy ink. Aqua, Ice and Frost carry panels, chips and screenshot chrome. Status badges use the system's own pairs: Pendente red, Em Análise amber, Em Andamento ice with deepened blue ink (urbis-status-andamento-fg), Resolvido green with deepened green ink (urbis-status-resolvido-fg), Rejeitado grey.
- **HealthSearch:** Petróleo (hs-petroleo) hero ground, Amber (hs-amber) the single action colour with near-black ink (hs-ink-on-amber). The SST traffic light is Em Dia green, A Vencer orange, Vencido red. The ASO lifecycle adds its pre-states from the product spec: Solicitado indigo, Agendado blue, Pendente slate.
- **CARITAS:** Paper (caritas-paper) ground, Midnight (caritas-midnight) type and hero, Royal (caritas-royal) the action. A full dark scheme under `prefers-color-scheme: dark` swaps to the caritas-dark-* set, with ink #04101f on the lighter royal.

### Named Rules
**The Deep Ink On Gold Rule.** Text and icons on gold use Abyss Teal (#0E363E, 5.1:1). Blueprint Teal on gold fails AA and is not allowed.

**The Frame Owns Gold Rule.** Gold, teal and the blueprint grid appear only in the NOXXD layer: the Home page, the case-page bar and the footer band. A product world never borrows them, and the frame never borrows a product colour.

**The State Vocabulary Rule.** Inside a product world, the only hues besides the brand palette are the product's own state colours (Urbis statuses, the HealthSearch traffic light and ASO pre-states). No decorative extra hues.

## Typography

**Display Font:** Oswald (with Archivo Narrow, Arial Narrow)
**Body Font:** Josefin Sans (with system-ui)
**Product fonts:** Urbis Manrope 800 + Inter; HealthSearch Archivo throughout, tabular numerals, JetBrains Mono for code-like identifiers; CARITAS Sora 600 + Inter.

**Character:** Oswald's condensed industrial capitals against Josefin's geometric, art-deco lowercase give NOXXD a stamped, engineered voice. The product fonts switch to tight, negative-tracked sentence case, so crossing the frame line reads as entering the product.

### Hierarchy
- **Display** (Oswald 700, clamp(2.5rem, 6.5vw, 4.5rem), 1.1, uppercase): Home hero title.
- **Headline** (Oswald 700, clamp(1.8rem, 4vw, 2.8rem), 1.2, uppercase): Home section titles.
- **Title** (Oswald 700, clamp(1.3rem, 2.5vw, 1.8rem), uppercase): card titles.
- **Body** (Josefin Sans 400, 1.05rem, 1.7): paragraphs; leads at 1.25rem in Old Paper.
- **Slogan** (Josefin Sans 600, 0.35em tracking, uppercase): "BUILD IT YOUR WAY" only; 0.2em under 480px.
- **Label** (Oswald 600–700, 0.85–1.05rem, 0.08em, uppercase): nav, frame bar, language switch, buttons (0.12em).
- **Case headline** (product head font, clamp(1.9rem, 3.6vw, 3rem), -0.02em): every case `h2`. Case body is 1.0625rem / 1.65 with leads capped at 62ch.

### Named Rules
**The Uppercase Belongs To NOXXD Rule.** Uppercase, tracked type is the frame's voice. Product worlds set headings in sentence case with negative tracking.

**The Slogan Stays English Rule.** "BUILD IT YOUR WAY" is never translated and never set in anything but tracked Josefin.

## Layout

Containers are 1200px wide everywhere: Home sections pad 90px vertically and 24px at the sides; case pages use `min(1200px, 100% - 32px)` with sections padding clamp(64px, 9vw, 120px). Spacing follows an 8px rhythm (8, 16, 24, 32, 48). Home grids run three columns, then two at 1024px, then one at 768px, where the nav collapses behind a square toggle. Case pages break their CTA band to one column at 860px and make buttons full width at 600px. Anchors offset for the sticky header (80px Home, 72px case pages).

The Home background is a blueprint: a 32px gold grid (20px under 480px) with a fixed field of floating gold squares, some hollow, behind the content. Each case hero composes its own ground (Urbis street grid, HealthSearch petróleo with matrix, CARITAS centred calm), so product composition is authored per page.

## Elevation & Depth

The NOXXD layer is flat. Depth comes from tone (teal, darker teal, deep teal), 2px gold borders, and the -2px to -4px lift on hover. The only blur is the sticky header's 4px backdrop. Product worlds may use soft, diffuse shadows, mainly for screenshot device frames and floating sheets.

### Shadow Vocabulary
- **Device drop** (`0 24px 60px -24px var(--shot-shadow)`): screenshot frames, tinted per product.
- **Lockup tile** (`0 10px 30px -10px rgba(0,0,0,0.5)`): the Urbis logo tile on navy.
- **Paper sheet** (`0 10px 30px -12px rgba(0,0,0,0.3)`): CARITAS document stack.
- **CARITAS card** (`0 2px 12px rgba(0,0,0,0.06)`; 0.3 in dark): link chip and cards.

### Named Rules
**The Flat Frame Rule.** No shadow is ever cast in the NOXXD layer. The pixel-tab box-shadows on cards duplicate corner squares; they are ornament, not elevation.

## Shapes

NOXXD is strictly right-angled: a universal `border-radius: 0 !important` covers every element and form control on Home, and the frame bar, language switch, contact button and footer are square on case pages. The signature silhouettes are 8-bit: 6px gold tabs at card corners, 12px stepped L-corners, 8px checkerboard dividers, and floating squares. The hero emblem and logo stay square.

Inside the frame each product keeps its own corner language: Urbis 18px panels and 12px controls, with pill status badges; HealthSearch 10px panels and 6px controls, with 4px matrix cells; CARITAS 14px panels and 8px controls, 6px paper sheets and a pill link chip. Phone screenshot frames use 38px device corners in every world.

**The Radius Lives Inside Rule.** Radius is a product property, set through `--p-radius` and `--p-radius-sm`. It never reaches the NOXXD bar, footer or Home.

## Components

### Buttons
- **NOXXD primary:** Square gold fill with a 2px gold border, Oswald 700 uppercase at 0.12em, padding 14px 32px. Hover and focus invert to a teal fill with gold text and lift -2px. Active returns to darker teal. A square gold ripple expands on click.
- **NOXXD outline:** Transparent with gold text and border; hover fills gold.
- **Frame contact:** The compact gold button in the case-page bar, deep ink, padding 9px 18px; hover clears to transparent with gold text.
- **Case button:** One primitive themed per product. 48px minimum height, padding 12px 24px, product radius-sm, product head font 700. Fill is the product accent with on-accent ink. Hover darkens to accent-hover and lifts -2px. The ghost variant is transparent with a currentColor border.

### Chips
- **NOXXD tag:** Square, 1px gold border on 15% gold wash, Josefin 600 uppercase at 0.8rem.
- **Case chips:** Product radius-sm, product chip background and ink, 0.85rem 600, used for stacks and compliance lists.

### Cards / Containers
- **Corner Style:** Square in NOXXD (pixel-card with gold corner tabs); product radius inside cases.
- **Background:** Shadow Teal on Home; product card colour inside cases.
- **Border:** 2px gold on Home.
- **Internal Padding:** 32px 24px on Home cards, 32px on contact panels.
- **Project card:** A pixel card whose logo plate (16:10, contained, tinted by `--plate`) scales to 1.04 on card hover, followed by title, summary, stack line, one metric above a faint gold rule, and a full-width primary button.

### Navigation
- **Home header:** Sticky, 96% teal with a 4px blur and a 2px gold rule. Oswald 600 uppercase links in Parchment White turn gold on hover or when active, with a 2px gold underline that grows from the left.
- **Case bar:** Sticky Shadow Teal, 60px, with back link and NOXXD mark on the left, language switch and contact on the right. The mark hides under 600px.
- **Language switch:** Square, 1px gold outline. On Home the active option is gold and underlined; in the case frame the pressed option fills gold with deep ink. The choice persists in `localStorage` as `noxxd_lang`.

### Screenshot Slot
A framed placeholder until real captures arrive: a browser device (34px chrome with dots and a URL pill) or a phone (38px corners, notch). The screen holds a wireframe of the real layout and a dark note band. All colours come from `--shot-*` tokens per product, and an `<img>` drops in with `object-fit: cover`.

### Floating Pixel Field (Home)
Gold squares, some hollow with a 2px inset outline, rise from below the viewport with slight sideways drift over 22–48s, at 14–46% opacity. Only transform animates. Squares after the twelfth are hidden under 768px, and the whole field is hidden under `prefers-reduced-motion`.

### Product Signatures
- **Urbis status ribbon:** Pill badges for Pendente, Em Análise, Em Andamento and Resolvido, joined by dashed aqua connectors. Each lifts in turn on a 10s cycle with a sky halo; Rejeitado sits apart after "ou" and does not animate.
- **HealthSearch NR matrix:** A 7-column grid of NR-01..NR-35 cells tinted by traffic-light state. A Vencer and Vencido show their own colour at rest. Hover lights a cell to full colour and scales it 1.12 as decoration only; the state lives in a visually hidden bilingual summary. A three-column traffic-light rail closes the hero.
- **HealthSearch ASO lifecycle:** One continuous 8px track in six coloured segments (pre-states, then traffic light), each with a ringed node. It turns vertical on mobile.
- **CARITAS document stack:** A4-proportioned paper sheets that fan out on hover or focus-within with a 0.6s ease-out.

## Do's and Don'ts

### Do:
- **Do** put #0E363E ink on every gold surface.
- **Do** theme a new case page only through a `--p-*` and `--shot-*` token block, with the NOXXD bar and footer unchanged.
- **Do** keep the NOXXD layer at 0px radius with 2px gold borders and pixel ornaments.
- **Do** use each product's official palette, fonts and logo from its spec in `Exemplos/`.
- **Do** carry state in text, such as a visible label or a visually hidden bilingual summary. Hover and motion only decorate.
- **Do** animate transform and opacity only, and remove all motion under `prefers-reduced-motion`.
- **Do** provide every visible string in both `lang="pt-BR"` and `lang="en"`.

### Don't:
- **Don't** set Blueprint Teal (#1B5E6B) text on gold; it fails AA.
- **Don't** round anything in the NOXXD layer, and don't bring gold, the blueprint grid or pixel ornaments into a product world.
- **Don't** add hues to a product world beyond its brand palette and its own state colours.
- **Don't** cast shadows in the NOXXD layer.
- **Don't** translate "BUILD IT YOUR WAY" or spell the name other than NOXXD.

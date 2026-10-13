# Graph Report - noxxd  (2026-10-12)

## Corpus Check
- 56 files · ~208,508 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .css 2)

## Summary
- 230 nodes · 442 edges · 23 communities (9 shown, 14 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 33 edges (avg confidence: 0.91)
- Token cost: 143,925 input · 0 output

## Community Hubs (Navigation)
- Test Infrastructure
- Core Features Testing
- Dependencies & Utils
- Test Infrastructure
- Design Assets
- Test Infrastructure
- Design Assets
- Design Assets
- Test Infrastructure
- Design Assets
- Project Portfolio
- Design Assets
- Design Assets
- Design Assets
- Design Assets
- Design Assets
- Design Assets
- Dependencies & Utils
- Dependencies & Utils
- Dependencies & Utils

## God Nodes (most connected - your core abstractions)
1. `get_index_html()` - 27 edges
2. `get_style_css()` - 23 edges
3. `strip_css_comments()` - 16 edges
4. `get_repo_root()` - 12 edges
5. `get_cname()` - 11 edges
6. `parse_css_declarations()` - 11 edges
7. `read_page()` - 9 edges
8. `check_case_exact_path()` - 8 edges
9. `test_t2_image_binary_integrity_pil()` - 8 edges
10. `Design System: NOXXD` - 8 edges

## Surprising Connections (you probably didn't know these)
- `CARITAS: Clinical Platform for Psychologists` --references--> `CARITAS Logo — Sphere with Wave`  [INFERRED]
  README.md → Exemplos/Caritas/LOGO CARITAS.svg
- `Urbis: Urban Maintenance & Geospatial Intelligence` --references--> `Urbis Logo — Modular Building Components`  [INFERRED]
  README.md → Exemplos/Urbis/logo urbis.png
- `HealthSearch: Occupational Health & Safety Hub` --references--> `HealthSearch Logo — Shield with HAT`  [INFERRED]
  README.md → Exemplos/HealthSearch/LOGO HEALTHSEARCH.png
- `NOXXD Favicon — 8-bit Checkerboard` --references--> `8-Bit Ornaments: Pixel Tabs, Checkerboard, Floating Squares`  [INFERRED]
  assets/favicon.svg → DESIGN.md
- `CARITAS Project Page` --references--> `CARITAS — Especificações Técnicas Frontend`  [INFERRED]
  projetos/caritas/index.html → Exemplos/Caritas/especificacoes-frontend.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Design System Authority: NOXXD Frame Governs All Projects** — design_md, projetos_urbis_html, projetos_healthsearch_html, projetos_caritas_html [INFERRED 0.90]
- **NOXXD Product Ecosystem: Three Distinct Project Worlds** — concept_project_urbis, concept_project_healthsearch, concept_project_caritas [EXTRACTED 1.00]
- **Visual Identity Layer: Palette + Typography + Ornaments** — concept_noxxd_palette, concept_typography_noxxd, concept_8bit_ornaments [INFERRED 0.85]
- **NOXXD Portfolio - Three Distinct Domains** — assets_projetos_caritas_logo_caritas, assets_projetos_healthsearch_logo_healthsearch, assets_projetos_urbis_logo_urbis [INFERRED 0.95]
- **Unified Icon Design System - Pixel Aesthetic** — assets_icons_icon_saas_icon, assets_icons_icon_web_icon, assets_icons_icon_whatsapp_icon, assets_icons_icon_x_icon [INFERRED 0.95]
- **Caritas UI Pattern - Tabbed Health Records** — assets_projetos_caritas_screens_anamnese_screen, assets_projetos_caritas_screens_sessao_screen, domain_mental_health_therapy [INFERRED 0.85]

## Communities (23 total, 14 thin omitted)

### Community 0 - "Test Infrastructure"
Cohesion: 0.09
Nodes (17): cname_content(), html_soup(), index_html(), repo_root(), style_css(), get_cname(), get_html_soup(), get_repo_root() (+9 more)

### Community 1 - "Core Features Testing"
Cohesion: 0.11
Nodes (16): get_index_html(), test_t1_brand_name_strict_orthography(), test_t1_brand_slogan_exact(), test_t1_cname_content_exact(), test_t1_contact_channels(), test_t1_footer_copyright(), test_t1_html5_semantic_structure(), test_t1_meta_viewport_and_charset() (+8 more)

### Community 2 - "Dependencies & Utils"
Cohesion: 0.10
Nodes (8): calculate_contrast_ratio(), check_case_exact_path(), find_free_port(), test_t4_accessibility_alt_and_semantics(), test_t4_case_sensitivity_linux_simulation(), test_t4_contrast_ratio_simulation(), test_t4_ephemeral_http_server_zero_404(), site()

### Community 3 - "Test Infrastructure"
Cohesion: 0.17
Nodes (14): read_page(), test_t5_bilingual_pt_en(), test_t5_clean_route_returns_200(), test_t5_cname_preserved(), test_t5_descriptive_copy(), test_t5_home_particles_gpu_and_reduced_motion(), test_t5_local_paths_match_disk_case(), test_t5_node_syntax_check() (+6 more)

### Community 4 - "Design Assets"
Cohesion: 0.13
Nodes (7): NOXXD Favicon — 8-bit Checkerboard, Design System: NOXXD, HealthSearch — Especificações Técnicas SIGAC, Urbis — Especificações Técnicas Frontend, NOXXD Home Page, HealthSearch Project Page, Urbis Project Page

### Community 5 - "Test Infrastructure"
Cohesion: 0.16
Nodes (6): test_t2_brand_color_tokens(), test_t2_cname_hygiene(), test_t2_image_binary_integrity_pil(), test_t2_pixel_pattern_aesthetics(), test_t2_slogan_letter_spacing(), test_t2_zero_border_radius_rule()

### Community 6 - "Design Assets"
Cohesion: 0.16
Nodes (16): CARITAS: Clinical Platform for Psychologists, HealthSearch: Occupational Health & Safety Hub, Urbis: Urban Maintenance & Geospatial Intelligence, CARITAS Logo — Sphere with Wave, HealthSearch Logo — Shield with HAT, Urbis Logo — Modular Building Components, Projetos Urbis Index HTML Surface, NOXXD — Website & Portfólio Institucional (+8 more)

### Community 7 - "Design Assets"
Cohesion: 0.17
Nodes (9): Server Architecture Icon, Web Browser Interface Icon, WhatsApp Message Icon, X Social/Close Icon, NOXXD Emblem - Pixelated N with Checkerboard Border, NOXXD Full Wordmark - Emblem + Logo + Slogan, Caritas Project Brand - Spherical Gradient Logo, HealthSearch Project Brand - Shield with Safety Helmet (+1 more)

### Community 9 - "Design Assets"
Cohesion: 0.83
Nodes (3): Urbis - Mobile Incident Reporting Form, Urbis - Admin Dashboard with Geolocation Heatmap, Urbis - Incident Reports Table with Status

## Knowledge Gaps
- **24 isolated node(s):** `Product — NOXXD Portfolio & Brand`, `Teamwork Project Prompt — Draft`, `CARITAS Logo — Sphere with Wave`, `Urbis Logo — Modular Building Components`, `HealthSearch Logo — Shield with HAT` (+19 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 104 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_index_html()` connect `Core Features Testing` to `Test Infrastructure`, `Dependencies & Utils`, `Test Infrastructure`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **What connects `Product — NOXXD Portfolio & Brand`, `Teamwork Project Prompt — Draft`, `CARITAS Logo — Sphere with Wave` to the rest of the system?**
  _24 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Test Infrastructure` be split into smaller, more focused modules?**
  _Cohesion score 0.08687943262411348 - nodes in this community are weakly interconnected._
- **Why does `get_style_css()` connect `Test Infrastructure` to `Dependencies & Utils`, `Test Infrastructure`, `Test Infrastructure`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Should `Core Features Testing` be split into smaller, more focused modules?**
  _Cohesion score 0.10952380952380952 - nodes in this community are weakly interconnected._
- **Why does `get_cname()` connect `Test Infrastructure` to `Core Features Testing`, `Test Infrastructure`, `Test Infrastructure`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Should `Dependencies & Utils` be split into smaller, more focused modules?**
  _Cohesion score 0.10256410256410256 - nodes in this community are weakly interconnected._
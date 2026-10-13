## Frontend Design Workflow

Before creating or modifying any frontend UI, read `DESIGN.md` in the project root. The design system defined in this file must become the new visual identity of the project, replacing the existing visual style.

### Tools and responsibilities

- **DESIGN.md:** The authoritative source for the new visual identity, including colors, typography, spacing, layout, components, visual hierarchy, and styling conventions. Follow its rules consistently, even when they differ from the current interface.
- **Impeccable:** Use its available design and frontend improvement commands to critique, transform, and refine the existing interface according to `DESIGN.md`.
- **design-taste-frontend:** Apply its frontend design expertise when implementing the new visual identity, prioritizing intentional composition, strong visual hierarchy, and polished execution.
- **redesign-existing-projects:** Use when transforming the existing interface. Evaluate the current implementation and replace its visual design rather than merely making incremental improvements.
- **high-end-visual-design:** Use when appropriate to achieve a refined, cohesive, high-quality result while respecting `DESIGN.md`.
- **web-design-guidelines:** Audit the redesigned interface for accessibility, responsive behavior, keyboard navigation, usability, and other relevant UI quality issues.

### Redesign requirements

1. Inspect the project structure, framework, existing components, styling system, and application functionality.
2. Read `DESIGN.md` in full and identify the visual rules that govern the redesign.
3. Treat the current visual design as a temporary implementation, not a design reference to preserve.
4. Replace the existing visual identity with the one defined in `DESIGN.md`. This includes colors, typography, spacing, backgrounds, borders, shadows, component appearance, layouts, and interaction states wherever applicable.
5. Do not retain the old design merely because it already exists. Reuse existing components only when they can be adapted to the new design without compromising its rules.
6. Use the relevant installed skills and available Impeccable commands selectively. Verify their actual instructions before relying on them.
7. Preserve application functionality, business logic, routes, data flows, integrations, and existing technical behavior unless changes are explicitly required.
8. Avoid unnecessary dependencies, duplicated components, and unrelated refactoring.
9. Apply the new design consistently across all relevant pages and shared components, rather than redesigning only the first screen.
10. Verify responsive behavior, accessibility, visual consistency, and the relevant application checks after implementation.

### Expected result

The result must look and feel like a fundamentally redesigned application following `DESIGN.md`, not the original interface with a few cosmetic adjustments.

The existing implementation should retain its working functionality while its visual identity is replaced by the downloaded design system.

Before making substantial changes, briefly explain the main visual differences identified and the planned scope of the redesign. Do not claim to have used a skill, command, or audit unless it was actually invoked or performed.
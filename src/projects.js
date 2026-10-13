// One muted accent, ink, tint and display face per product: same NOXXD frame, distinct worlds.
export const PROJECTS = {
  urbis: { name: 'Urbis', accent: '#2F6B7C', ink: '#16323B', tint: '#EBF1F2', font: "'Manrope', 'Inter', sans-serif" },
  healthsearch: { name: 'HealthSearch', accent: '#8A6A2E', ink: '#1F2D3D', tint: '#F4EFE6', font: "'Archivo', 'Inter', sans-serif" },
  caritas: { name: 'CARITAS', accent: '#52599A', ink: '#1E2238', tint: '#EEEFF6', font: "'Sora', 'Inter', sans-serif" },
}

export const themeOf = (slug) => {
  const p = PROJECTS[slug]
  return { '--p-accent': p.accent, '--p-ink': p.ink, '--p-tint': p.tint, '--p-font': p.font }
}

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// Multi-page build: each page keeps its own HTML (title, meta, canonical) for SEO and link previews.
export default defineConfig({
  plugins: [react(), tailwindcss()],
  build: {
    rollupOptions: {
      input: {
        home: 'index.html',
        urbis: 'projetos/urbis/index.html',
        healthsearch: 'projetos/healthsearch/index.html',
        caritas: 'projetos/caritas/index.html',
      },
    },
  },
})

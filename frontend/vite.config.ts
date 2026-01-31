import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    proxy: {
      '/api': {
        // Proxy API requests to backend
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})

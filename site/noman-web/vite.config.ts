import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import pluginChecker from 'vite-plugin-checker';
import path from 'path';
import { fileURLToPath } from 'url';

// Get the directory name of the current module
const __dirname = path.dirname(fileURLToPath(import.meta.url));

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    pluginChecker({ typescript: true })
  ],
  build: {
    lib: {
      // The entry point for our library
      entry: path.resolve(__dirname, 'src/lib/index.ts'),
      name: 'SearchBoxLib',
      // The file formats to generate
      formats: ['es', 'umd'],
      fileName: (format) => `search-box.${format}.js`
    },
    rollupOptions: {
      // Make sure to externalize dependencies that shouldn't be bundled
      external: ['react', 'react-dom'],
      output: {
        // Provide global variables to use in the UMD build
        globals: {
          react: 'React',
          'react-dom': 'ReactDOM'
        }
      }
    }
  }
})

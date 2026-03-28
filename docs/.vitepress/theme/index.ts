import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import StudentShowcase from './components/StudentShowcase.vue'
import AlumniDirectory from './components/AlumniDirectory.vue'
import './custom.css'

const theme: Theme = {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('StudentShowcase', StudentShowcase)
    app.component('AlumniDirectory', AlumniDirectory)
  }
}

export default theme

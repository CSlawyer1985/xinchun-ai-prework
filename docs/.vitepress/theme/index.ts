import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import BaseImage from './components/BaseImage.vue'
import HomeAsciiHero from './components/HomeAsciiHero.vue'
import StudentShowcase from './components/StudentShowcase.vue'
import AlumniDirectory from './components/AlumniDirectory.vue'
import './custom.css'

const theme: Theme = {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('BaseImage', BaseImage)
    app.component('HomeAsciiHero', HomeAsciiHero)
    app.component('StudentShowcase', StudentShowcase)
    app.component('AlumniDirectory', AlumniDirectory)
  }
}

export default theme

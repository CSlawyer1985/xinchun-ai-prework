import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import { h } from 'vue'
import BaseImage from './components/BaseImage.vue'
import HomeAsciiHero from './components/HomeAsciiHero.vue'
import StudentShowcase from './components/StudentShowcase.vue'
import StudentVoices from './components/StudentVoices.vue'
import AlumniDirectory from './components/AlumniDirectory.vue'
import SiteCounter from './components/SiteCounter.vue'
import './custom.css'

const theme: Theme = {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      'layout-bottom': () => h(SiteCounter)
    })
  },
  enhanceApp({ app }) {
    app.component('BaseImage', BaseImage)
    app.component('HomeAsciiHero', HomeAsciiHero)
    app.component('StudentShowcase', StudentShowcase)
    app.component('StudentVoices', StudentVoices)
    app.component('AlumniDirectory', AlumniDirectory)
    app.component('SiteCounter', SiteCounter)
  }
}

export default theme

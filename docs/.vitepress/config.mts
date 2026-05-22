import { defineConfig } from 'vitepress'

const repo = process.env.GITHUB_REPOSITORY?.split('/')[1] ?? ''
const isUserSite = repo.endsWith('.github.io')
const hasCustomSiteUrl = Boolean(process.env.SITE_URL ?? process.env.VITEPRESS_SITE_URL)
const base = process.env.GITHUB_ACTIONS === 'true'
  ? (hasCustomSiteUrl ? '/' : (isUserSite ? '/' : `/${repo}/`))
  : '/'
const siteUrl = (process.env.SITE_URL ?? process.env.VITEPRESS_SITE_URL ?? '').replace(/\/$/, '')
const siteTitle = '四明山法师 AI 夜校'
const siteDescription = '法律人AI实操夜校——培养业务与技术的双语者，含课前指引、实用工具与往期学员名录。'
const shareImagePath = `${base}images/share/wechat-card.png`
const shareImageUrl = siteUrl ? `${siteUrl}${shareImagePath}` : shareImagePath
const homeUrl = siteUrl ? `${siteUrl}${base}` : undefined

const shareHead = [
  ['meta', { name: 'theme-color', content: '#071823' }],
  ['meta', { property: 'og:type', content: 'website' }],
  ['meta', { property: 'og:locale', content: 'zh_CN' }],
  ['meta', { property: 'og:site_name', content: siteTitle }],
  ['meta', { property: 'og:title', content: siteTitle }],
  ['meta', { property: 'og:description', content: siteDescription }],
  ['meta', { property: 'og:image', content: shareImageUrl }],
  ['meta', { property: 'og:image:width', content: '1200' }],
  ['meta', { property: 'og:image:height', content: '630' }],
  ['meta', { property: 'og:image:type', content: 'image/png' }],
  ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
  ['meta', { name: 'twitter:title', content: siteTitle }],
  ['meta', { name: 'twitter:description', content: siteDescription }],
  ['meta', { name: 'twitter:image', content: shareImageUrl }]
] as [string, Record<string, string>][]

if (homeUrl) {
  shareHead.push(['meta', { property: 'og:url', content: homeUrl }])
  shareHead.push(['link', { rel: 'canonical', href: homeUrl }])
}

export default defineConfig({
  title: siteTitle,
  description: siteDescription,
  lang: 'zh-CN',
  base,
  cleanUrls: true,
  lastUpdated: true,
  appearance: 'dark',
  head: shareHead,
  themeConfig: {
    siteTitle,
    nav: [
      { text: '课前指引', link: '/prework/00_课前准备总览' },
      { text: '实用工具', link: '/tools/00_实用工具总览' },
      { text: '往期学员', link: '/students/00_往期学员名录' },
      { text: '常见问题', link: '/prework/04_常见问题FAQ' }
    ],
    sidebar: [
      {
        text: '课前指引',
        items: [
          { text: '00 课前准备总览', link: '/prework/00_课前准备总览' },
          { text: '01 Cherry Studio 安装与配置', link: '/prework/01_Cherry_Studio_安装与配置指南' },
          { text: '02 Claude Code 安装与配置', link: '/prework/02_Claude_Code_安装与配置指南' },
          { text: '03 环境验证清单', link: '/prework/03_环境验证清单' },
          { text: '04 常见问题 FAQ', link: '/prework/04_常见问题FAQ' }
        ]
      },
      {
        text: '实用工具',
        items: [
          { text: '00 实用工具总览', link: '/tools/00_实用工具总览' },
          { text: '01 Claude Code 速查表', link: '/tools/01_Claude_Code_速查表' },
          { text: '02 Claude Code 提示词 324 条中文翻译版', link: '/tools/02_Claude_Code_提示词_324条_中文翻译版' },
          { text: '03 法律概念 WIKI', link: 'https://cslawyer1985.github.io/legalwiki/index.html' },
          { text: '04 Claude for Legal中国法适配', link: 'https://cslawyer1985.github.io/claude-for-legal-ZH/' }
        ]
      },
      {
        text: '往期学员',
        items: [
          { text: '00 往期学员名录', link: '/students/00_往期学员名录' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/CSlawyer1985' }
    ],
    search: {
      provider: 'local'
    },
    footer: {
      message: `${siteTitle} · 学员查阅版`,
      copyright: 'Copyright © 2026'
    }
  }
})

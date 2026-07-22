import { defineConfig } from 'vitepress'

const repo = process.env.GITHUB_REPOSITORY?.split('/')[1] ?? ''
const isUserSite = repo.endsWith('.github.io')
const siteUrl = (process.env.SITE_URL ?? process.env.VITEPRESS_SITE_URL ?? '').replace(/\/$/, '')
const isCustomDomain = Boolean(siteUrl) && !siteUrl.includes('github.io')
const base = process.env.GITHUB_ACTIONS === 'true'
  ? (isCustomDomain ? '/' : (isUserSite ? '/' : `/${repo}/`))
  : '/'
const siteTitle = '四明山法师 AI 夜校'
const siteDescription = '法律人AI实操夜校——培养业务与技术的双语者，含课前指引、实用工具与往期学员名录。'
const shareImagePath = `${base}images/share/wechat-card.png`
const shareImageUrl = siteUrl ? `${siteUrl}${shareImagePath}` : shareImagePath
// 线上根 URL：CI 从 SITE_URL + base 推导；本地构建用线上 URL 作 fallback，保证 canonical/sitemap 指向正确
const homeUrl = (siteUrl ? `${siteUrl}${base}` : 'https://course.legalagi.cn/').replace(/\/+$/, '')

// 页面绝对 URL（og:url / canonical）
function pageUrl(relativePath: string) {
  if (relativePath === 'index.md') return `${homeUrl}/`
  return `${homeUrl}/${relativePath.replace(/\.md$/, '').replace(/\\/g, '/')}`
}

// 全站统一 head；页面相关的 og:title/og:description/og:url/canonical/twitter:title 由 transformHead 按页注入
const shareHead = [
  ['meta', { name: 'theme-color', content: '#071823' }],
  ['link', { rel: 'icon', type: 'image/png', sizes: '32x32', href: `${base}favicon-32.png` }],
  ['link', { rel: 'apple-touch-icon', sizes: '180x180', href: `${base}favicon-180.png` }],
  ['meta', { property: 'og:type', content: 'website' }],
  ['meta', { property: 'og:locale', content: 'zh_CN' }],
  ['meta', { property: 'og:site_name', content: siteTitle }],
  ['meta', { property: 'og:image', content: shareImageUrl }],
  ['meta', { property: 'og:image:width', content: '1200' }],
  ['meta', { property: 'og:image:height', content: '630' }],
  ['meta', { property: 'og:image:type', content: 'image/png' }],
  ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
  ['meta', { name: 'twitter:image', content: shareImageUrl }]
] as [string, Record<string, string>][]

// ===== JSON-LD 结构化数据（SEO + GEO：AI 抓取优先解析） =====
function orgJsonLd() {
  return {
    '@context': 'https://schema.org',
    '@type': 'EducationalOrganization',
    name: siteTitle,
    alternateName: '法师 AI 夜校',
    description: '法律人 AI 实操夜校——培养业务与技术的双语者。',
    url: `${homeUrl}/`,
    logo: shareImageUrl,
    sameAs: ['https://github.com/CSlawyer1985']
  }
}

function websiteJsonLd() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: siteTitle,
    url: `${homeUrl}/`,
    inLanguage: 'zh-CN'
  }
}

function courseJsonLd() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Course',
    name: '四明山法师 AI 夜校',
    description: '面向法律从业者的 AI 实操夜校：先导课 + 6 节主课 + 返场复盘，覆盖 Cherry Studio 工作台、Claude Code 基础与进阶、工具链与法律工作流、算力与模型路由、数据专题。',
    provider: {
      '@type': 'EducationalOrganization',
      name: siteTitle,
      sameAs: `${homeUrl}/`
    },
    inLanguage: 'zh-CN',
    educationalLevel: '进阶',
    courseCode: 'SMS-AI-NIGHT-SCHOOL'
  }
}

function faqJsonLd(items: { q: string; a: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: items.map((it) => ({
      '@type': 'Question',
      name: it.q,
      acceptedAnswer: { '@type': 'Answer', text: it.a }
    }))
  }
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
  sitemap: {
    hostname: `${homeUrl}/`
  },
  transformHead({ pageData }) {
    const title = pageData.title || siteTitle
    const description = (pageData.description as string | undefined) || siteDescription
    const url = pageUrl(pageData.relativePath)
    const tags: Array<[string, Record<string, string>]> = [
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: description }],
      ['meta', { property: 'og:url', content: url }],
      ['meta', { name: 'twitter:title', content: title }],
      ['meta', { name: 'twitter:description', content: description }],
      ['link', { rel: 'canonical', href: url }],
      // 每页注入组织信息（AI 抓取基础）
      ['script', { type: 'application/ld+json' }, JSON.stringify(orgJsonLd())]
    ] as unknown as Array<[string, Record<string, string>]>

    // 首页追加 Course + WebSite
    if (pageData.relativePath === 'index.md') {
      tags.push(['script', { type: 'application/ld+json' }, JSON.stringify(courseJsonLd())] as [string, Record<string, string>])
      tags.push(['script', { type: 'application/ld+json' }, JSON.stringify(websiteJsonLd())] as [string, Record<string, string>])
    }
    // 课前准备总览追加 Course
    if (pageData.relativePath === 'prework/00_课前准备总览.md') {
      tags.push(['script', { type: 'application/ld+json' }, JSON.stringify(courseJsonLd())] as [string, Record<string, string>])
    }
    // FAQ 页追加 FAQPage（由 frontmatter.faq 驱动）
    const faq = pageData.frontmatter?.faq as { q: string; a: string }[] | undefined
    if (faq && faq.length) {
      tags.push(['script', { type: 'application/ld+json' }, JSON.stringify(faqJsonLd(faq))] as [string, Record<string, string>])
    }
    return tags
  },
  themeConfig: {
    siteTitle,
    nav: [
      { text: '课前指引', link: '/prework/00_课前准备总览' },
      { text: '实用工具', link: '/tools/00_实用工具总览' },
      { text: '命令练习', link: '/tools/06_Claude_Code_命令打字练习' },
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
          { text: '03 法律概念 WIKI', link: 'https://wiki.legalagi.cn/' },
          { text: '04 Claude for Legal中国法适配', link: 'https://claude.legalagi.cn/' },
          { text: '05 法律 Agent 运行结构仪表盘', link: '/tools/05_法律Agent运行结构仪表盘' },
          { text: '06 Claude Code 命令打字练习', link: '/tools/06_Claude_Code_命令打字练习' }
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

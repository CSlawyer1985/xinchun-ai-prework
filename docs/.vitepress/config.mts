import { defineConfig } from 'vitepress'

const repo = process.env.GITHUB_REPOSITORY?.split('/')[1] ?? ''
const isUserSite = repo.endsWith('.github.io')
const base = process.env.GITHUB_ACTIONS === 'true'
  ? (isUserSite ? '/' : `/${repo}/`)
  : '/'

export default defineConfig({
  title: '新春AI工作坊',
  description: '课前指引（学员查阅版）',
  lang: 'zh-CN',
  base,
  cleanUrls: true,
  lastUpdated: true,
  themeConfig: {
    siteTitle: '新春AI工作坊',
    nav: [
      { text: '课前指引', link: '/prework/00_课前准备总览' },
      { text: '环境验证', link: '/prework/03_环境验证清单' },
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
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/CSlawyer1985' }
    ],
    search: {
      provider: 'local'
    },
    footer: {
      message: '新春AI工作坊 · 学员查阅版',
      copyright: 'Copyright © 2026'
    }
  }
})

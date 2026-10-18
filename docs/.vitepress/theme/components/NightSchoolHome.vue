<script setup lang="ts">
import { withBase } from 'vitepress'
import MotionWordmark from './MotionWordmark.vue'
import StudentVoices from './StudentVoices.vue'
import StudentShowcase from './StudentShowcase.vue'
import AnthemCard from './AnthemCard.vue'
import EcosystemNav from './EcosystemNav.vue'

const steps = [
  { n: '01', tool: 'WorkBuddy', title: '第 1 步：WorkBuddy 工作台', duration: '30–45 分钟', text: '从官方入口下载安装 WorkBuddy，完成微信扫码登录，并跑通第一个小任务，约 30 - 45 分钟。', link: '/prework/01_WorkBuddy_安装与配置指南', icon: 'M6 7h12v12H6z M9 7V4h6v3 M9 11h6 M9 15h4' },
  { n: '02', tool: 'Claude Code', title: '第 2 步：Claude Code 全套环境', duration: '45–75 分钟', text: '使用官方原生安装器完成 Claude Code 安装、登录与本地文件任务验证，约 45 - 75 分钟。', link: '/prework/02_Claude_Code_安装与配置指南', icon: 'M8 7l-5 5 5 5 M16 7l5 5-5 5 M14 4l-4 16' },
  { n: '03', tool: 'Checklist / FAQ', title: '第 3 步：环境验证 + FAQ', duration: '约 10 分钟', text: '最后跑一遍环境验证清单；如果卡住，再查 FAQ 或截图到群里求助，约 10 分钟。', link: '/prework/03_环境验证清单', icon: 'M9 6h11 M9 12h11 M9 18h11 M3 5l1 1 2-2 M3 11l1 1 2-2 M3 17l1 1 2-2' }
]
</script>

<template>
  <div class="night-home">
    <section class="nh-hero" aria-labelledby="night-school-title">
      <div class="nh-hero-atmosphere" aria-hidden="true">
        <div class="nh-grid"></div>
        <div class="nh-track nh-track-a"><i></i><b></b></div>
        <div class="nh-track nh-track-b"><i></i><b></b></div>
        <div class="nh-track nh-track-c"><i></i><b></b></div>
        <div class="nh-track nh-track-d"><i></i><b></b></div>
      </div>
      <div class="nh-hero-content">
        <a class="nh-chip" :href="withBase('/courses/00_上期课程大纲')"><span></span>法律人 AI 实操夜校 <span aria-hidden="true">→</span></a>
        <h1 id="night-school-title" class="nh-sr-only">四明山法师 AI 夜校</h1>
        <MotionWordmark />
        <h2 class="nh-hero-title">培养业务与技术的<span>双语者。</span></h2>
        <p class="nh-hero-tagline">法律人AI实操夜校——培养业务与技术的双语者。<br>一个寻找快乐、制造正向飞轮的地方。</p>
        <div class="nh-actions">
          <a class="nh-button nh-button-primary" :href="withBase('/prework/00_课前准备总览')">先看准备总览 <span aria-hidden="true">→</span></a>
          <span class="nh-registration"><i></i>报名关闭期</span>
        </div>
      </div>
      <div class="nh-hero-foot">
        <span>核心入口 · 3 条工具线</span>
        <a :href="withBase('/prework/01_WorkBuddy_安装与配置指南')"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 7h12v12H6z M9 7V4h6v3" /></svg>WorkBuddy</a>
        <a :href="withBase('/prework/02_Claude_Code_安装与配置指南')"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 7l-5 5 5 5 M16 7l5 5-5 5 M14 4l-4 16" /></svg>Claude Code</a>
        <a :href="withBase('/prework/02_ChatGPT_CLI与GUI_安装指南')"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5h14v14H5z M8 9l3 3-3 3 M13 15h3" /></svg>ChatGPT / Codex <small>可选</small></a>
      </div>
    </section>

    <section class="nh-section nh-preparation" id="preparation" aria-labelledby="preparation-title">
      <header class="nh-section-heading">
        <div><p class="nh-eyebrow"><span>01</span>课前准备</p><h2 id="preparation-title">3 步完成<br><span>课前准备。</span></h2></div>
        <a class="nh-text-link" :href="withBase('/prework/00_课前准备总览')">先看准备总览 <span aria-hidden="true">↗</span></a>
      </header>
      <div class="nh-step-grid">
        <a v-for="step in steps" :key="step.n" class="nh-step" :href="withBase(step.link)">
          <div class="nh-step-top"><svg viewBox="0 0 24 24" aria-hidden="true"><path :d="step.icon" /></svg><span>{{ step.n }} / 03</span></div>
          <div class="nh-step-preview" aria-hidden="true"><span>{{ step.tool }}</span><div class="nh-code-line"></div><div class="nh-code-line"></div><div class="nh-code-line"></div><span class="nh-terminal-cursor">_</span></div>
          <div class="nh-step-copy"><p class="nh-step-duration">{{ step.duration }}</p><h3>{{ step.title }}</h3><p>{{ step.text }}</p><span class="nh-step-arrow" aria-hidden="true">↗</span></div>
        </a>
      </div>
      <div class="nh-facts">
        <article><p>课程安排</p><h3>先导课 + 6 次主课 + 返场课</h3><p>原则上每周一堂，主课之间留一周作业推进，并配套社群陪跑。</p></article>
        <article><p>至少准备</p><h3>2 类模型账号</h3><p>1 个国内可直连，1 个国际模型备用。</p></article>
        <article><p>核心入口</p><h3>3 条工具线</h3><p>WorkBuddy、Claude Code，以及 ChatGPT / Codex 可选入口。</p></article>
      </div>
    </section>

    <section class="nh-section nh-voices-section" aria-label="学员心声">
      <p class="nh-eyebrow"><span>02</span>学员心声</p>
      <StudentVoices />
    </section>

    <section class="nh-section nh-alumni-section" aria-labelledby="alumni-title">
      <header class="nh-section-heading"><div><p class="nh-eyebrow"><span>03</span>往期学员</p><h2 id="alumni-title">业务与技术，<br><span>与同行者一起。</span></h2></div><a class="nh-text-link" :href="withBase('/students/00_往期学员名录')">往期学员名录 <span aria-hidden="true">↗</span></a></header>
      <StudentShowcase />
    </section>

    <section class="nh-section nh-anthem-section" aria-label="夜校校歌">
      <p class="nh-eyebrow"><span>04</span>校歌</p>
      <AnthemCard />
    </section>

    <section class="nh-section nh-ecosystem-section" aria-label="法律AI作品">
      <p class="nh-eyebrow"><span>05</span>法律AI作品</p>
      <EcosystemNav :show-slogan="false" />
    </section>
  </div>
</template>

<script setup lang="ts">
withDefaults(defineProps<{ showSlogan?: boolean }>(), { showSlogan: true })

// Match the blog's project gallery order, excluding the night school itself.
const projects = [
  { name: 'Claude for Legal ZH', url: 'https://claude.legalagi.cn/' },
  { name: '法律概念 Wiki', url: 'https://wiki.legalagi.cn/' },
  { name: '法律人 Skill 仓库', url: 'https://skill.chenshi.ai/' },
  { name: 'MemoBall', url: 'https://memoball.chenshi.ai/' },
  { name: '法律 Agent 解构', url: 'https://learn-agent.legalagi.cn/' },
  { name: 'DeepSeek Harness 桌面客户端', url: 'https://dsh.chenshi.ai/' },
  { name: '纪考工作台 · RuleNav', url: 'https://rule.chenshi.ai/' },
  { name: '法律元 SKILL', url: 'https://skill.chenshi.ai/legal-meta-skill' },
  { name: '文夹 InkPeg', url: 'https://inkpeg.chenshi.ai/' },
  { name: 'ADG · Agent 数据网关', url: 'https://adg.chenshi.ai/' }
]
</script>

<template>
  <aside class="ecosystem-nav" aria-labelledby="ecosystem-nav-title">
    <div class="ecosystem-nav__heading">
      <span class="ecosystem-nav__eyebrow">LEGAL AI PROJECTS</span>
      <h2 id="ecosystem-nav-title">法律AI作品</h2>
    </div>

    <nav class="ecosystem-nav__links" aria-label="法律AI作品站点">
      <a href="https://chenshi.ai/" target="_blank" rel="noopener">
        <span>陈石 · 法与 AI</span>
        <small>chenshi.ai</small>
      </a>
      <a v-for="project in projects" :key="project.url" :href="project.url" target="_blank" rel="noopener">
        <span>{{ project.name }}</span>
        <small>{{ project.url.replace('https://', '').replace(/\/$/, '') }}</small>
      </a>
    </nav>

    <p v-if="showSlogan" class="ecosystem-nav__slogan">
      <svg
        class="ecosystem-nav__wave"
        aria-hidden="true"
        focusable="false"
        viewBox="0 0 2400 120"
        preserveAspectRatio="none"
      >
        <path
          class="ecosystem-nav__wave-line ecosystem-nav__wave-line--a"
          d="M0 60 Q150 0 300 60 T600 60 T900 60 T1200 60 T1500 60 T1800 60 T2100 60 T2400 60"
        />
        <path
          class="ecosystem-nav__wave-line ecosystem-nav__wave-line--b"
          d="M0 60 Q150 96 300 60 T600 60 T900 60 T1200 60 T1500 60 T1800 60 T2100 60 T2400 60"
        />
      </svg>
      <span class="ecosystem-nav__slogan-text">业务与技术的双语者</span>
    </p>
  </aside>
</template>

<script setup lang="ts">
import { computed } from 'vue'

type Voice = {
  text: string
  highlight?: boolean
}

type Track = {
  variant: 'alpha' | 'beta' | 'gamma'
  duration: number
  delay?: number
  reverse?: boolean
  items: Voice[]
}

// 提炼自学员社群自发反馈的正向表达，去除署名，仅保留对课程 / AI / 自我改变的真实回响
const tracks: Track[] = [
  {
    variant: 'alpha',
    duration: 30,
    items: [
      { text: '小白也能写代码了', highlight: true },
      { text: '对 AI 工具有了质的提升' },
      { text: '日常工作效率提升巨大' },
      { text: '课程值得反复观看' },
      { text: '精彩授课，受益匪浅' }
    ]
  },
  {
    variant: 'beta',
    duration: 42,
    reverse: true,
    items: [
      { text: '感觉插上了科技的翅膀', highlight: true },
      { text: '每天都处于被 AI 惊讶的兴奋中', highlight: true },
      { text: '让我开了眼，见到了另一方世界', highlight: true },
      { text: '作为海泰律师，太骄傲了', highlight: true }
    ]
  },
  {
    variant: 'gamma',
    duration: 34,
    delay: -8,
    items: [
      { text: '又补齐了律师执业的短板' },
      { text: '倾囊相授，受益匪浅' },
      { text: '学到了很多，也玩得很开心' },
      { text: '每天都觉得太爽了' },
      { text: '这段时间受益匪浅' }
    ]
  }
]

// 每条轨道渲染两份相同内容，配合 translateX(-50%) 实现无缝循环
const loopedTracks = computed(() =>
  tracks.map((track) => ({
    ...track,
    groups: [track.items, track.items] as Voice[][]
  }))
)
</script>

<template>
  <section class="student-voices" aria-labelledby="student-voices-label">
    <header class="student-voices__header">
      <p class="student-voices__eyebrow" id="student-voices-label">学员心声</p>
      <h2 class="student-voices__title">正向飞轮的真实回响</h2>
      <p class="student-voices__lead">
        以下话语摘自学员在社群里的自发反馈，未经署名。
      </p>
    </header>

    <div class="student-voices__board">
      <div class="student-voices__rail">
        <div
          v-for="track in loopedTracks"
          :key="track.variant"
          class="student-voices__track"
          :class="{ 'student-voices__track--reverse': track.reverse }"
          :style="{
            '--voices-duration': `${track.duration}s`,
            '--voices-delay': `${track.delay ?? 0}s`
          }"
        >
          <ul
            v-for="(group, groupIndex) in track.groups"
            :key="groupIndex"
            class="student-voices__group"
            :class="{ 'student-voices__group--clone': groupIndex === 1 }"
            :aria-hidden="groupIndex === 1 ? 'true' : null"
          >
            <li
              v-for="(voice, voiceIndex) in group"
              :key="voiceIndex"
              class="student-voice"
              :class="{ 'student-voice--highlight': voice.highlight }"
            >
              {{ voice.text }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

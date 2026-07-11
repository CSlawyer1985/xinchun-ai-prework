<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { withBase } from 'vitepress'

type Lyric = { t: number; line: string }

const audio = ref<HTMLAudioElement | null>(null)
const lyrlist = ref<HTMLUListElement | null>(null)
const playing = ref(false)
const current = ref('00:00')
const duration = ref('04:49')
const progress = ref(0)
const activeLyric = ref(-1)

const anthemSrc = withBase('/anthem.mp3')
const backSrc = withBase('/images/anthem-cassette-back.png')
const frontSrc = withBase('/images/anthem-cassette.png')
const wheelSrc = withBase('/images/anthem-cassette-wheel.png')

// 歌词与时间戳（秒），复用返场课 PPT 末页已对齐的 LYRICS 数据
const LYRICS: Lyric[] = [
  { t: 0, line: '♪ 前奏' },
  { t: 26.4, line: '夜色落下，灯火升起，' },
  { t: 30.0, line: '我们相聚在四明山下。' },
  { t: 33.4, line: '有人来自审判的席前，' },
  { t: 35.9, line: '有人奔走在庭审路上。' },
  { t: 40.0, line: '有人守着企业的边界，' },
  { t: 43.2, line: '有人追问制度的方向。' },
  { t: 46.2, line: '有人还在课堂里眺望，' },
  { t: 49.4, line: '第一次听见时代声响。' },
  { t: 55.3, line: '法官思考裁判的分寸，' },
  { t: 58.1, line: '律师寻找破局的方法。' },
  { t: 61.4, line: '法务面对真实的风险，' },
  { t: 63.8, line: '学者追问规则的表达。' },
  { t: 68.0, line: '法学生带着年轻的眼睛，' },
  { t: 70.9, line: '看见未来，也看见迷惘。' },
  { t: 74.6, line: '不同的身份，不同的困惑，' },
  { t: 77.9, line: '都在这里重新出发。' },
  { t: 82.2, line: '做业务和技术的双语者，' },
  { t: 85.2, line: '听得懂需求，也看得清方向。' },
  { t: 88.8, line: '懂法律的判断，懂工具的力量，' },
  { t: 92.1, line: '让专业穿过新的浪潮。' },
  { t: 95.3, line: '做业务和技术的双语者，' },
  { t: 98.4, line: '看得见本质，也传得出方法。' },
  { t: 102.0, line: '了解本质，掌握技法，' },
  { t: 105.3, line: '把知识传给更多同行的人啊。' },
  { t: 125.9, line: '我们不只追逐工具，' },
  { t: 128.8, line: '也不迷信神奇回答。' },
  { t: 131.9, line: '从检索到写作，从提示到流程，' },
  { t: 135.2, line: '把复杂拆成可学的方法。' },
  { t: 138.7, line: '我们不把技术藏在高墙，' },
  { t: 141.4, line: '也不让焦虑变成沉默。' },
  { t: 145.1, line: '有人先走一步，就点一盏灯，' },
  { t: 148.6, line: '照见后来者脚下的路。' },
  { t: 152.9, line: '做业务和技术的双语者，' },
  { t: 155.9, line: '听得懂需求，也看得清方向。' },
  { t: 159.5, line: '懂法律的判断，懂工具的力量，' },
  { t: 162.8, line: '让专业穿过新的浪潮。' },
  { t: 166.2, line: '做业务和技术的双语者，' },
  { t: 169.2, line: '看得见本质，也传得出方法。' },
  { t: 172.9, line: '了解本质，掌握技法，' },
  { t: 176.0, line: '把知识传给更多同行的人啊。' },
  { t: 186.8, line: '模型会更新，工具会变样，' },
  { t: 190.2, line: '不变的是清醒的目光。' },
  { t: 193.4, line: '时代提出新的考题，' },
  { t: 196.0, line: '我们一起寻找答案。' },
  { t: 199.7, line: '不是一个人的独行，' },
  { t: 203.0, line: '不是少数人的魔法。' },
  { t: 206.2, line: '从问题出发，向本质抵达，' },
  { t: 209.3, line: '让每个人都拥有方法。' },
  { t: 215.5, line: '做业务和技术的双语者，' },
  { t: 218.8, line: '在四明山下并肩生长。' },
  { t: 222.0, line: '让法官、律师、法务、学者、法学生，' },
  { t: 226.6, line: '都能听见自己的回响。' },
  { t: 228.6, line: '做业务和技术的双语者，' },
  { t: 231.9, line: '把专业、技术与人连接成光。' },
  { t: 235.2, line: '以AI为桨，以智慧为舟，' },
  { t: 239.1, line: '一起驶向法律新的远方。' },
  { t: 246.9, line: '以AI为桨，以智慧为舟，' },
  { t: 253.9, line: '我们就是新的晨光。' },
  { t: 276.9, line: '业务和技术。' },
  { t: 282.9, line: '业务和技术。' }
]

function fmt(s: number) {
  const v = Math.max(0, Math.floor(Number.isFinite(s) ? s : 0))
  const m = Math.floor(v / 60)
  const r = v % 60
  return String(m).padStart(2, '0') + ':' + String(r).padStart(2, '0')
}

function toggle() {
  const a = audio.value
  if (!a) return
  if (playing.value) {
    a.pause()
  } else {
    a.play().catch(() => {
      playing.value = false
    })
  }
}

function updateLyric(t: number) {
  let ci = -1
  for (let i = 0; i < LYRICS.length; i++) {
    if (t >= LYRICS[i].t) ci = i
  }
  if (ci !== activeLyric.value) {
    activeLyric.value = ci
    nextTick(() => scrollLyricToCenter(ci))
  }
}

function scrollLyricToCenter(ci: number) {
  const ul = lyrlist.value
  const wrap = ul?.parentElement
  if (!ul || !wrap || ci < 0) return
  const li = ul.children[ci] as HTMLElement
  if (!li) return
  ul.style.transform = `translateY(${Math.round(wrap.clientHeight / 2 - (li.offsetTop + li.offsetHeight / 2))}px)`
}

function seekTo(t: number) {
  const a = audio.value
  if (!a) return
  if (Number.isFinite(a.duration) && a.duration > 0) {
    a.currentTime = Math.min(Math.max(0, t), a.duration)
    progress.value = (a.currentTime / a.duration) * 100
  } else {
    a.currentTime = Math.max(0, t)
  }
  current.value = fmt(a.currentTime)
  updateLyric(a.currentTime)
}

function onPlay() {
  playing.value = true
}

function onPause() {
  playing.value = false
}

function onTime() {
  const a = audio.value
  if (!a) return
  current.value = fmt(a.currentTime)
  if (a.duration && Number.isFinite(a.duration)) {
    progress.value = (a.currentTime / a.duration) * 100
  }
  updateLyric(a.currentTime)
}

function onLoaded() {
  const a = audio.value
  if (!a) return
  if (a.duration && Number.isFinite(a.duration)) {
    duration.value = fmt(a.duration)
  }
}

function seek(e: Event) {
  const a = audio.value
  const input = e.target as HTMLInputElement
  if (!a || !a.duration || !Number.isFinite(a.duration)) return
  seekTo((Number(input.value) / 100) * a.duration)
}

function onLyricClick(e: MouseEvent) {
  const li = (e.target as HTMLElement).closest('li[data-t]')
  if (!li) return
  seekTo(Number(li.getAttribute('data-t')) || 0)
  if (!playing.value) {
    audio.value?.play().catch(() => {})
  }
}

function onLyricKey(e: KeyboardEvent) {
  const li = (e.target as HTMLElement).closest('li[data-t]')
  if (!li) return
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault()
    seekTo(Number(li.getAttribute('data-t')) || 0)
    if (!playing.value) {
      audio.value?.play().catch(() => {})
    }
  }
}

onMounted(() => {
  const a = audio.value
  if (!a) return
  a.addEventListener('play', onPlay)
  a.addEventListener('pause', onPause)
  a.addEventListener('timeupdate', onTime)
  a.addEventListener('loadedmetadata', onLoaded)
  a.addEventListener('ended', onPause)
})

onBeforeUnmount(() => {
  const a = audio.value
  if (!a) return
  a.pause()
  a.removeEventListener('play', onPlay)
  a.removeEventListener('pause', onPause)
  a.removeEventListener('timeupdate', onTime)
  a.removeEventListener('loadedmetadata', onLoaded)
  a.removeEventListener('ended', onPause)
})
</script>

<template>
  <section class="anthem-card" aria-labelledby="anthem-card-label">
    <div class="anthem-card__inner" :class="{ 'is-playing': playing }">
      <div class="anthem-card__head">
        <p class="anthem-card__eyebrow" id="anthem-card-label">校歌 · Anthem</p>
        <h2 class="anthem-card__title">逐法之光</h2>
        <p class="anthem-card__lead">四明山法师AI夜校 · 2026</p>
      </div>

      <div class="anthem-card__stage">
        <div
          class="anthem-card__tape"
          :style="{
            '--tape-back': `url('${backSrc}')`,
            '--tape-front': `url('${frontSrc}')`,
            '--tape-wheel': `url('${wheelSrc}')`
          }"
        >
          <div class="anthem-card__tape-back"></div>
          <div class="anthem-card__wheel anthem-card__wheel--left">
            <div class="anthem-card__wheel-inner"></div>
          </div>
          <div class="anthem-card__wheel anthem-card__wheel--right">
            <div class="anthem-card__wheel-inner"></div>
          </div>
          <div class="anthem-card__tape-front"></div>
        </div>

        <div class="anthem-card__lyrics">
          <ul
            ref="lyrlist"
            class="anthem-card__lyrlist"
            @click="onLyricClick"
            @keydown="onLyricKey"
          >
            <li
              v-for="(l, i) in LYRICS"
              :key="i"
              class="anthem-card__lyric"
              :class="{ 'cur': i === activeLyric }"
              :data-t="l.t"
              tabindex="0"
              :aria-label="`跳到 ${fmt(l.t)} ${l.line}`"
            >{{ l.line }}</li>
          </ul>
        </div>
      </div>

      <div class="anthem-card__player" :style="{ '--anthem-progress': progress + '%' }">
        <button
          class="anthem-card__play"
          type="button"
          :aria-label="playing ? '暂停校歌' : '播放校歌'"
          @click="toggle"
        >
          <svg v-if="!playing" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
            <path d="M8 5v14l11-7z" fill="currentColor" />
          </svg>
          <svg v-else viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
            <rect x="6" y="5" width="4" height="14" rx="1" fill="currentColor" />
            <rect x="14" y="5" width="4" height="14" rx="1" fill="currentColor" />
          </svg>
        </button>
        <span class="anthem-card__time">{{ current }}</span>
        <input
          class="anthem-card__progress"
          type="range"
          min="0"
          max="100"
          step="0.1"
          :value="progress"
          aria-label="校歌播放进度"
          @input="seek"
        />
        <span class="anthem-card__time anthem-card__time--duration">{{ duration }}</span>
      </div>

      <audio ref="audio" :src="anthemSrc" preload="none"></audio>
    </div>
  </section>
</template>

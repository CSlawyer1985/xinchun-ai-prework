<script setup lang="ts">
import { onMounted, ref } from 'vue'

// 部署 counter-worker 后，把此处替换为实际 workers.dev 地址
const COUNTER_URL = 'https://night-counter.lawyerchenshi.workers.dev/api/counter'

const pv = ref<number | null>(null)
const uv = ref<number | null>(null)
const failed = ref(false)

function fmt(n: number | null) {
  return n === null ? '' : n.toLocaleString('zh-CN')
}

onMounted(async () => {
  try {
    const res = await fetch(COUNTER_URL)
    if (!res.ok) throw new Error('counter http ' + res.status)
    const data = (await res.json()) as { pv?: number; uv?: number }
    pv.value = Number(data.pv)
    uv.value = Number(data.uv)
  } catch {
    failed.value = true
  }
})
</script>

<template>
  <div
    class="site-counter"
    :class="{
      'site-counter--ready': pv !== null && uv !== null,
      'site-counter--hidden': failed
    }"
    aria-live="polite"
  >
    <p class="site-counter__inner">
      <span class="site-counter__label">访问统计</span>
      <span>总访问 {{ fmt(pv) }}</span>
      <span class="site-counter__dot">·</span>
      <span>访客 {{ fmt(uv) }}</span>
    </p>
  </div>
</template>

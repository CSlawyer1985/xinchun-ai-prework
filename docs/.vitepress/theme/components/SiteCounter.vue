<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'

const ready = ref(false)
const failed = ref(false)
let timer: number | undefined
let timeout: number | undefined

function hasValue(id: string) {
  return Boolean(document.getElementById(id)?.textContent?.trim())
}

function checkReady() {
  if (hasValue('busuanzi_value_site_pv') || hasValue('busuanzi_value_site_uv')) {
    ready.value = true
    if (timer) {
      window.clearInterval(timer)
      timer = undefined
    }
  }
}

onMounted(() => {
  const scriptId = 'busuanzi-counter-script'
  const existing = document.getElementById(scriptId) as HTMLScriptElement | null

  if (!existing) {
    const script = document.createElement('script')
    script.id = scriptId
    script.async = true
    script.src = 'https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js'
    script.onerror = () => {
      failed.value = true
    }
    document.body.appendChild(script)
  }

  checkReady()
  timer = window.setInterval(checkReady, 400)
  timeout = window.setTimeout(() => {
    if (!ready.value) {
      failed.value = true
    }
    if (timer) {
      window.clearInterval(timer)
      timer = undefined
    }
  }, 5000)
})

onBeforeUnmount(() => {
  if (timer) {
    window.clearInterval(timer)
  }
  if (timeout) {
    window.clearTimeout(timeout)
  }
})
</script>

<template>
  <div
    class="site-counter"
    :class="{ 'site-counter--ready': ready, 'site-counter--hidden': failed && !ready }"
    aria-live="polite"
  >
    <p class="site-counter__inner">
      <span class="site-counter__label">访问统计</span>
      <span id="busuanzi_container_site_pv">
        总访问
        <span id="busuanzi_value_site_pv"></span>
      </span>
      <span class="site-counter__dot">·</span>
      <span id="busuanzi_container_site_uv">
        访客
        <span id="busuanzi_value_site_uv"></span>
      </span>
    </p>
  </div>
</template>

<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'

const root = ref<HTMLElement>()
const canvas = ref<HTMLCanvasElement>()
const playhead = ref<HTMLElement>()
const timecode = ref<HTMLElement>()
const ready = ref(false)
let dispose = () => {}

onMounted(async () => {
  // Keep the HTML title visible while fonts and canvas initialise (also the SSR fallback).
  let destroyed = false
  dispose = () => { destroyed = true }
  await document.fonts.ready
  if (destroyed || !root.value || !canvas.value) return
  const el = root.value
  const surface = canvas.value
  const ctx = surface.getContext('2d')
  if (!ctx) return
  const mask = document.createElement('canvas')
  const code = document.createElement('canvas')
  const color = document.createElement('canvas')
  const maskCtx = mask.getContext('2d')!
  const codeCtx = code.getContext('2d')!
  const colorCtx = color.getContext('2d')!
  const media = window.matchMedia('(prefers-reduced-motion: reduce)')
  const font = '"PingFang SC", "Microsoft YaHei", sans-serif'
  const mono = 'ui-monospace, monospace'
  let width = 1, height = 1, dpr = 1, fontSize = 1
  let lines: string[] = []
  let rows: string[] = []
  let frame = 0, lastFrame = -Infinity, visible = true
  const start = performance.now()
  const ease = (p: number) => p < 0.5 ? 4 * p ** 3 : 1 - (-2 * p + 2) ** 3 / 2
  const text = (c: CanvasRenderingContext2D, stroke = false) => {
    c.font = `800 ${fontSize}px ${font}`
    c.textAlign = 'center'
    c.textBaseline = 'middle'
    lines.forEach((line, index) => {
      const y = height / 2 + (index - (lines.length - 1) / 2) * fontSize * 1.28 + fontSize * 0.04
      if (stroke) c.strokeText(line, width / 2, y)
      else c.fillText(line, width / 2, y)
    })
  }
  const resize = () => {
    const bounds = el.getBoundingClientRect()
    dpr = Math.min(window.devicePixelRatio || 1, 2)
    width = Math.round(bounds.width * dpr)
    height = Math.round(bounds.height * dpr)
    lines = bounds.width < 600 ? ['四明山法师', 'AI 夜校'] : ['四明山法师AI夜校']
    maskCtx.font = `800 100px ${font}`
    const longest = Math.max(...lines.map(line => maskCtx.measureText(line).width))
    fontSize = Math.min(height / (lines.length * 1.36), width * 0.94 / longest * 100)
    for (const c of [surface, mask, code, color]) { c.width = width; c.height = height }
    maskCtx.fillStyle = '#fff'
    text(maskCtx)
    rows = Array.from({ length: 36 }, () => Array.from({ length: 240 }, () => Math.random() > 0.5 ? '1' : '0').join(''))
    render(performance.now())
  }
  function render(now: number) {
    const t = (now - start) / 1000
    const ct = t % 8.2
    const p = media.matches ? 1 : ct < 4.4 ? ease(ct / 4.4) : ct < 7.2 ? 1 : 1 - ease(ct - 7.2)
    const opacity = media.matches || ct >= 7.2 ? 0 : ct < 6.2 ? 1 : Math.max(0, 1 - (ct - 6.2) / 0.6)
    const sx = width * (0.025 + 0.95 * p)
    if (playhead.value) {
      playhead.value.style.left = `${sx / width * 100}%`
      playhead.value.style.opacity = String(opacity)
    }
    if (timecode.value) {
      const frames = Math.round(p * 150)
      timecode.value.textContent = `00:00:${String(Math.floor(frames / 30)).padStart(2, '0')}:${String(frames % 30).padStart(2, '0')}`
    }

    codeCtx.clearRect(0, 0, width, height)
    const size = Math.max(5 * dpr, fontSize * 0.083)
    codeCtx.font = `600 ${size}px ${mono}`
    codeCtx.textBaseline = 'top'
    for (let i = 0; i < Math.ceil(height / (size * 1.14)); i++) {
      const offset = (t * (i % 2 ? 19 : -15) * dpr) % (size * 60)
      codeCtx.fillStyle = i % 4 === 0 ? '#a9c9f2' : i % 5 === 0 ? '#c7a8de' : '#7b8799'
      codeCtx.fillText(rows[i % rows.length], offset - size * 65, i * size * 1.14)
    }
    codeCtx.globalCompositeOperation = 'destination-in'
    codeCtx.drawImage(mask, 0, 0)
    codeCtx.globalCompositeOperation = 'source-over'

    colorCtx.clearRect(0, 0, width, height)
    const gradient = colorCtx.createLinearGradient(0, 0, width, height * 0.3)
    gradient.addColorStop(0, '#e6f1ff')
    gradient.addColorStop(0.25 + Math.sin(t * 0.6) * 0.035, '#79c0ff')
    gradient.addColorStop(0.5, '#a371f7')
    gradient.addColorStop(0.8, '#f778ba')
    gradient.addColorStop(1, '#ffd8a8')
    colorCtx.fillStyle = gradient
    colorCtx.fillRect(0, 0, width, height)
    for (let i = 0; i < 3; i++) {
      const x = ((t * (0.12 + i * 0.04) + i * 0.36) % 1.5 - 0.25) * width
      const light = colorCtx.createRadialGradient(x, height * 0.5, 0, x, height * 0.5, height * 1.8)
      light.addColorStop(0, '#ffffff80')
      light.addColorStop(1, '#ffffff00')
      colorCtx.fillStyle = light
      colorCtx.fillRect(0, 0, width, height)
    }
    colorCtx.save()
    colorCtx.translate(width / 2, height / 2)
    colorCtx.rotate(-0.35)
    colorCtx.fillStyle = '#0d111724'
    for (let i = -8; i < 9; i++) colorCtx.fillRect(((i * 0.13 + t * 0.08) % 1) * width * 1.7 - width * 0.85, -height * 2, width * 0.025, height * 4)
    colorCtx.restore()
    colorCtx.fillStyle = '#01040920'
    for (let y = 0; y < height; y += 3 * dpr) colorCtx.fillRect(0, y, width, dpr * 0.65)
    colorCtx.globalCompositeOperation = 'destination-in'
    colorCtx.drawImage(mask, 0, 0)
    colorCtx.globalCompositeOperation = 'source-over'

    ctx.clearRect(0, 0, width, height)
    ctx.save()
    ctx.beginPath(); ctx.rect(sx, 0, width - sx, height); ctx.clip()
    ctx.drawImage(code, 0, 0)
    ctx.strokeStyle = '#c9d1d980'
    ctx.lineWidth = dpr * 0.65
    text(ctx, true)
    ctx.restore()
    ctx.save()
    ctx.beginPath(); ctx.rect(0, 0, sx, height); ctx.clip()
    ctx.shadowColor = '#79c0ff55'
    ctx.shadowBlur = 22 * dpr
    ctx.drawImage(color, 0, 0)
    ctx.restore()
    if (opacity > 0 && p > 0 && p < 1) {
      const glowWidth = (lines.length > 1 ? 20 : 38) * dpr
      const glow = ctx.createLinearGradient(sx - glowWidth, 0, sx, 0)
      glow.addColorStop(0, '#ffffff00'); glow.addColorStop(1, '#ffffff88')
      ctx.save(); ctx.globalCompositeOperation = 'source-atop'
      ctx.fillStyle = glow; ctx.fillRect(sx - glowWidth, 0, glowWidth, height); ctx.restore()
    }
    ready.value = true
  }
  const tick = (now: number) => {
    if (destroyed || document.hidden || !visible || media.matches) { frame = 0; return }
    if (now - lastFrame > 1000 / 30) { render(now); lastFrame = now }
    frame = requestAnimationFrame(tick)
  }
  const resume = () => {
    if (media.matches) render(performance.now())
    else if (!frame && visible && !document.hidden) frame = requestAnimationFrame(tick)
  }
  const observer = new ResizeObserver(resize)
  observer.observe(el)
  const intersection = new IntersectionObserver(entries => {
    visible = entries[0].isIntersecting
    resume()
  })
  intersection.observe(el)
  document.addEventListener('visibilitychange', resume)
  media.addEventListener('change', resume)
  resize()
  resume()
  dispose = () => {
    destroyed = true
    cancelAnimationFrame(frame)
    observer.disconnect(); intersection.disconnect()
    document.removeEventListener('visibilitychange', resume)
    media.removeEventListener('change', resume)
  }
})

onBeforeUnmount(() => dispose())
</script>

<template>
  <div ref="root" class="nh-wordmark" :class="{ 'is-ready': ready }" aria-hidden="true">
    <span class="nh-wordmark-fallback">四明山法师<span>AI 夜校</span></span>
    <canvas ref="canvas"></canvas>
    <span ref="playhead" class="nh-playhead"><i></i><span ref="timecode">00:00:00:00</span></span>
    <div class="nh-ruler"></div>
  </div>
</template>

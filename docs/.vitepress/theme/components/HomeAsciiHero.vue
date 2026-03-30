<script setup lang="ts">
import { Teleport } from 'vue'
import { nextTick, onBeforeUnmount, onMounted, ref } from 'vue'

type Particle = {
  x: number
  y: number
  tx: number
  ty: number
  vx: number
  vy: number
  char: string
  alpha: number
  targetAlpha: number
  isText: boolean
  phase: number
  delay: number
}

const props = withDefaults(defineProps<{
  text?: string
  target?: string
}>(), {
  text: '法律AI训练营',
  target: ''
})

const particleChars = '.:+-=*#@&~[]{}|/\\'

const canvasRef = ref<HTMLCanvasElement | null>(null)
const wrapperRef = ref<HTMLElement | null>(null)
const showFallback = ref(false)
const isMounted = ref(false)

let cleanup: (() => void) | null = null
let resizeTimer: number | null = null
let targetElement: Element | null = null

function randomChar(chars: string) {
  return chars[Math.floor(Math.random() * chars.length)]
}

function getAccentColor() {
  const root = getComputedStyle(document.documentElement)
  return (
    root.getPropertyValue('--workshop-ascii-accent').trim() ||
    root.getPropertyValue('--vp-c-brand-1').trim() ||
    root.getPropertyValue('--workshop-accent').trim() ||
    '#14b8a6'
  )
}

function destroyCurrent() {
  if (cleanup) {
    cleanup()
    cleanup = null
  }
  if (targetElement) {
    targetElement.classList.remove('home-ascii-hero-target')
    targetElement = null
  }
}

function setupCanvas() {
  destroyCurrent()

  const canvas = canvasRef.value
  const wrapper = wrapperRef.value

  if (!canvas || !wrapper) {
    return
  }

  if (props.target) {
    targetElement = document.querySelector(props.target)
    targetElement?.classList.add('home-ascii-hero-target')
  }

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    showFallback.value = true
    return
  }

  showFallback.value = false

  const context = canvas.getContext('2d')
  if (!context) {
    showFallback.value = true
    return
  }

  let accentColor = getAccentColor()
  const dpr = Math.min(window.devicePixelRatio || 1, 2)
  const isMobile = window.innerWidth <= 640
  const chars = isMobile ? '01' : particleChars
  const sampleStep = isMobile ? 4 : 5
  const glyphFontSize = isMobile ? 5 : 6
  const interactionRadius = isMobile ? 54 : 82
  const interactionForce = isMobile ? 4.8 : 2.8
  const minHeight = isMobile ? 92 : 126
  const fontFamily = '"Instrument Sans", "PingFang SC", "Noto Sans SC", "Microsoft YaHei", sans-serif'
  const probeFont = `800 84px ${fontFamily}`
  const text = props.text

  const wrapperWidth = Math.max(240, Math.floor(wrapper.getBoundingClientRect().width))
  const probeCanvas = document.createElement('canvas')
  const probeContext = probeCanvas.getContext('2d')
  if (!probeContext) {
    showFallback.value = true
    return
  }

  probeContext.font = probeFont
  const measuredWidth = probeContext.measureText(text).width || wrapperWidth
  const resolvedFontSize = Math.max(isMobile ? 50 : 60, Math.floor((84 * wrapperWidth / measuredWidth) * 0.81))
  const drawFont = `800 ${resolvedFontSize}px ${fontFamily}`
  const measuredHeight = Math.max(minHeight, Math.ceil(resolvedFontSize * 1.08))

  canvas.style.width = `${wrapperWidth}px`
  canvas.style.height = `${measuredHeight}px`
  canvas.width = Math.floor(wrapperWidth * dpr)
  canvas.height = Math.floor(measuredHeight * dpr)
  context.setTransform(dpr, 0, 0, dpr, 0, 0)

  const offscreen = document.createElement('canvas')
  offscreen.width = wrapperWidth
  offscreen.height = measuredHeight
  const offscreenContext = offscreen.getContext('2d')
  if (!offscreenContext) {
    showFallback.value = true
    return
  }

  offscreenContext.clearRect(0, 0, wrapperWidth, measuredHeight)
  offscreenContext.font = drawFont
  offscreenContext.fillStyle = '#ffffff'
  offscreenContext.textAlign = 'left'
  offscreenContext.textBaseline = 'middle'
  offscreenContext.fillText(text, 0, measuredHeight / 2)

  const image = offscreenContext.getImageData(0, 0, wrapperWidth, measuredHeight)
  const particles: Particle[] = []

  for (let y = 0; y < measuredHeight; y += sampleStep) {
    for (let x = 0; x < wrapperWidth; x += sampleStep) {
      const index = (y * wrapperWidth + x) * 4
      if (image.data[index + 3] > 110) {
        particles.push({
          x: x + (Math.random() - 0.5) * wrapperWidth * 0.65,
          y: y + (Math.random() - 0.5) * measuredHeight * 2.2,
          tx: x,
          ty: y,
          vx: 0,
          vy: 0,
          char: randomChar(chars),
          alpha: 0,
          targetAlpha: isMobile ? 0.95 : 0.88 + Math.random() * 0.12,
          isText: true,
          phase: Math.random() * Math.PI * 2,
          delay: (x / wrapperWidth) * 1.15
        })
      }
    }
  }

  const ambientCount = Math.max(28, Math.floor(particles.length * 0.12))
  for (let index = 0; index < ambientCount; index += 1) {
    const x = Math.random() * wrapperWidth
    const y = Math.random() * measuredHeight
    particles.push({
      x,
      y,
      tx: x,
      ty: y,
      vx: (Math.random() - 0.5) * 0.16,
      vy: (Math.random() - 0.5) * 0.16,
      char: randomChar(chars),
      alpha: 0,
      targetAlpha: 0.05 + Math.random() * 0.08,
      isText: false,
      phase: Math.random() * Math.PI * 2,
      delay: Math.random() * 0.45
    })
  }

  let pointerX = -9999
  let pointerY = -9999
  let animationFrame = 0
  const start = performance.now()

  const onMouseMove = (event: MouseEvent) => {
    const rect = canvas.getBoundingClientRect()
    pointerX = event.clientX - rect.left
    pointerY = event.clientY - rect.top
  }

  const onTouchMove = (event: TouchEvent) => {
    const touch = event.touches[0]
    if (!touch) {
      return
    }
    const rect = canvas.getBoundingClientRect()
    pointerX = touch.clientX - rect.left
    pointerY = touch.clientY - rect.top
  }

  const resetPointer = () => {
    pointerX = -9999
    pointerY = -9999
  }

  const themeObserver = new MutationObserver(() => {
    accentColor = getAccentColor()
  })

  themeObserver.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-theme']
  })

  const draw = (timestamp: number) => {
    const elapsed = (timestamp - start) / 1000

    context.clearRect(0, 0, wrapperWidth, measuredHeight)
    context.font = `500 ${glyphFontSize}px "IBM Plex Mono", "SFMono-Regular", monospace`
    context.textAlign = 'center'
    context.textBaseline = 'middle'
    context.fillStyle = accentColor

    for (const particle of particles) {
      const visibleElapsed = Math.max(0, elapsed - particle.delay)

      if (particle.isText && visibleElapsed < 0.01) {
        context.globalAlpha = 0.02
        context.fillText(particle.char, particle.x, particle.y)
        continue
      }

      particle.vx += (particle.tx - particle.x) * 0.04
      particle.vy += (particle.ty - particle.y) * 0.04

      const dx = particle.x - pointerX
      const dy = particle.y - pointerY
      const distance = Math.sqrt(dx * dx + dy * dy)

      if (distance < interactionRadius && distance > 0) {
        const force = ((1 - distance / interactionRadius) ** 2) * interactionForce
        particle.vx += (dx / distance) * force
        particle.vy += (dy / distance) * force
      }

      particle.vx *= 0.88
      particle.vy *= 0.88
      particle.x += particle.vx
      particle.y += particle.vy
      particle.alpha += (particle.targetAlpha - particle.alpha) * 0.045

      if (particle.isText) {
        particle.alpha = particle.targetAlpha + Math.sin(elapsed * 0.8 + particle.phase) * 0.08
        if (visibleElapsed < 0.85 || Math.random() < 0.0008) {
          particle.char = randomChar(chars)
        }
      } else {
        particle.tx += (Math.random() - 0.5) * 0.18
        particle.ty += (Math.random() - 0.5) * 0.18

        if (particle.x < -20) {
          particle.x = particle.tx = wrapperWidth + 10
        }
        if (particle.x > wrapperWidth + 20) {
          particle.x = particle.tx = -10
        }
        if (particle.y < -20) {
          particle.y = particle.ty = measuredHeight + 10
        }
        if (particle.y > measuredHeight + 20) {
          particle.y = particle.ty = -10
        }
        if (Math.random() < 0.003) {
          particle.char = randomChar(chars)
        }
      }

      context.globalAlpha = Math.max(0, particle.alpha)
      context.fillText(particle.char, particle.x, particle.y)
    }

    context.globalAlpha = 1
    animationFrame = window.requestAnimationFrame(draw)
  }

  canvas.addEventListener('mousemove', onMouseMove, { passive: true })
  canvas.addEventListener('mouseleave', resetPointer)
  canvas.addEventListener('touchstart', onTouchMove, { passive: true })
  canvas.addEventListener('touchmove', onTouchMove, { passive: true })
  canvas.addEventListener('touchend', resetPointer)

  animationFrame = window.requestAnimationFrame(draw)

  cleanup = () => {
    window.cancelAnimationFrame(animationFrame)
    themeObserver.disconnect()
    canvas.removeEventListener('mousemove', onMouseMove)
    canvas.removeEventListener('mouseleave', resetPointer)
    canvas.removeEventListener('touchstart', onTouchMove)
    canvas.removeEventListener('touchmove', onTouchMove)
    canvas.removeEventListener('touchend', resetPointer)
  }
}

function scheduleSetup() {
  if (resizeTimer !== null) {
    window.clearTimeout(resizeTimer)
  }

  resizeTimer = window.setTimeout(() => {
    setupCanvas()
  }, 120)
}

onMounted(async () => {
  isMounted.value = true
  await nextTick()
  setupCanvas()
  window.addEventListener('resize', scheduleSetup, { passive: true })
})

onBeforeUnmount(() => {
  if (resizeTimer !== null) {
    window.clearTimeout(resizeTimer)
  }
  window.removeEventListener('resize', scheduleSetup)
  destroyCurrent()
})
</script>

<template>
  <Teleport v-if="target && isMounted" :to="target">
    <section ref="wrapperRef" class="home-ascii-hero home-ascii-hero--inline" aria-hidden="true">
      <canvas ref="canvasRef" class="home-ascii-hero__canvas" />
      <div v-if="showFallback" class="home-ascii-hero__fallback">{{ text }}</div>
    </section>
  </Teleport>
  <section v-else-if="!target" ref="wrapperRef" class="home-ascii-hero" aria-hidden="true">
    <canvas ref="canvasRef" class="home-ascii-hero__canvas" />
    <div v-if="showFallback" class="home-ascii-hero__fallback">{{ text }}</div>
  </section>
</template>

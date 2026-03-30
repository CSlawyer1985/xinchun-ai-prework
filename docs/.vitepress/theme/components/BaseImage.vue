<script setup lang="ts">
import { withBase } from 'vitepress'

defineProps<{
  src: string
  alt: string
}>()
</script>

<template>
  <img :src="withBase(src)" :alt="alt" loading="lazy" />
</template>

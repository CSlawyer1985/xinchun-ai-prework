<script setup lang="ts">
import { withBase } from 'vitepress'
import { alumniCohorts } from './alumni-data'

const cohort = alumniCohorts[0]
</script>

<template>
  <section class="student-showcase">
    <div class="student-showcase__header">
      <div>
        <p class="student-showcase__eyebrow">{{ cohort.season }}</p>
        <h2>{{ cohort.title }}</h2>
      </div>
      <a class="student-showcase__cta" :href="withBase('/students/00_往期学员名录')">查看更多</a>
    </div>

    <div class="student-showcase__grid student-showcase__grid--contributors">
      <article
        v-for="member in cohort.members"
        :key="member.name"
        class="student-avatar"
      >
        <div class="student-avatar__media">
          <img
            class="student-avatar__image"
            :src="withBase(member.image)"
            :alt="`${member.name} 头像`"
            loading="lazy"
          />
        </div>
        <div class="student-avatar__caption">
          <strong class="student-avatar__name">{{ member.name }}</strong>
          <span v-if="member.note" class="student-avatar__note" :title="member.note">{{ member.note }}</span>
        </div>
      </article>
    </div>
  </section>
</template>

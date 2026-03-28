<script setup lang="ts">
import { alumniCohorts } from './alumni-data'
</script>

<template>
  <div class="alumni-directory">
    <section
      v-for="cohort in alumniCohorts"
      :key="cohort.title"
      class="alumni-directory__section"
    >
      <div class="alumni-directory__header">
        <div>
          <p class="alumni-directory__season">{{ cohort.season }}</p>
          <h2>{{ cohort.title }}</h2>
        </div>
      </div>

      <div class="alumni-wall alumni-wall--contributors">
        <article
          v-for="member in cohort.members"
          :key="member.name"
          class="alumni-avatar"
        >
          <div class="student-avatar__media">
            <img :src="member.image" :alt="`${member.name} 头像`" loading="lazy" />
            <div class="student-avatar__overlay">
              <strong>{{ member.name }}</strong>
              <span v-if="member.note">{{ member.note }}</span>
            </div>
          </div>
        </article>
      </div>
    </section>
  </div>
</template>

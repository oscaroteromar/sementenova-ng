<script setup>
defineProps({
  title: { type: String, required: true },
  image: { type: String, default: null },
})
</script>

<template>
  <div class="card">
    <h3 class="card-title">{{ title }}</h3>
    <hr class="divider" />
    <img v-if="image" :src="image" :alt="title" class="card-image" />
    <div class="card-body">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.card-image {
  width: 100%;
  height: 135px;
  object-fit: cover;
  border-radius: 4px;
  margin-bottom: 10px;
}

.card-body {
  font-size: 14px;
  color: var(--color-text);
}

.card-body :deep(p) {
  margin: 0 0 6px;
}
</style>

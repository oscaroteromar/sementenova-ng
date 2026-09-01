<script setup>
defineProps({
  number: { type: String, required: true },
  title: { type: String, required: true },
  rows: { type: Array, default: () => [] },
})
</script>

<template>
  <article class="card">
    <span class="card-number">{{ number }}</span>
    <h3 class="card-title">{{ title }}</h3>
    <p v-if="$slots.default" class="card-intro"><slot /></p>
    <div v-if="rows.length" class="card-rows">
      <div v-for="(row, i) in rows" :key="i" class="card-row">
        <span class="row-label">{{ row.label }}</span>
        <span class="row-value">{{ row.value }}</span>
      </div>
    </div>
  </article>
</template>

<style scoped>
.card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 30px 28px 32px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  height: 100%;
}

.card-number {
  font-family: var(--font-mono);
  font-size: 10.5px;
  letter-spacing: 0.16em;
  color: var(--text-mute-3);
}

.card-title {
  font-family: var(--font-serif);
  font-size: 30px;
  line-height: 1.05;
  color: var(--accent);
}

.card-intro {
  font-size: 16px;
  line-height: 1.55;
  color: var(--text-soft);
  margin: 0;
}

.card-rows {
  padding-top: 20px;
  border-top: 1px solid var(--border);
  display: grid;
  gap: 10px;
}

.card-row {
  display: grid;
  grid-template-columns: 88px 1fr;
  gap: 12px;
  font-size: 15px;
}

.row-label {
  color: var(--text-mute-2);
}
</style>

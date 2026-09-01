<script setup>
import { computed, onMounted, ref } from 'vue'
import { API_BASE } from '../config'

const CATEGORIES = [
  { key: 'rondalla', label: 'Rondalla' },
  { key: 'baile', label: 'Baile galego' },
  { key: 'gaita', label: 'Gaita, pandeireta e percusión' },
  { key: 'outros', label: 'Outros' },
]

const scores = ref([])
const status = ref('loading') // loading | ready | error

const groups = computed(() =>
  CATEGORIES.map((cat) => ({
    ...cat,
    items: scores.value.filter((s) => s.category === cat.key),
  })).filter((group) => group.items.length > 0),
)

function formatDate(isoString) {
  const d = new Date(isoString)
  const day = String(d.getDate()).padStart(2, '0')
  const month = String(d.getMonth() + 1).padStart(2, '0')
  return `${day}-${month}-${d.getFullYear()}`
}

onMounted(async () => {
  try {
    const res = await fetch(`${API_BASE}/api/scores/`)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const data = await res.json()
    scores.value = data.results
    status.value = 'ready'
  } catch {
    status.value = 'error'
  }
})
</script>

<template>
  <div class="scores">
    <section class="container hero">
      <p class="eyebrow">Partituras</p>
      <h1 class="hero-title">Partituras para <span class="accent-italic">practicar</span></h1>
    </section>

    <section class="container body">
      <p v-if="status === 'loading'" class="state-text">Cargando partituras…</p>
      <p v-else-if="status === 'error'" class="state-text">
        Non se puideron cargar as partituras. Téntao de novo máis tarde.
      </p>
      <p v-else-if="groups.length === 0" class="state-text">
        Aínda non hai partituras dispoñibles.
      </p>

      <div v-else class="groups">
        <div v-for="group in groups" :key="group.key" class="group">
          <h2 class="group-title">{{ group.label }}</h2>
          <div class="score-grid">
            <article v-for="score in group.items" :key="score.id" class="score-card">
              <a :href="score.file_url" class="score-preview" target="_blank" rel="noopener">
                <img v-if="score.preview_url" :src="score.preview_url" :alt="score.title" />
                <span v-else class="score-preview-fallback">PDF</span>
              </a>
              <div class="score-info">
                <p class="score-title">{{ score.title }}</p>
                <p v-if="score.notes" class="score-notes">{{ score.notes }}</p>
                <p class="score-date">{{ formatDate(score.uploaded_at) }}</p>
              </div>
              <a :href="score.file_url" class="btn btn-outline" download>Descargar</a>
            </article>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.scores {
  padding-bottom: 88px;
}

.hero {
  padding-top: 72px;
}

.hero-title {
  font-family: var(--font-serif);
  font-size: clamp(36px, 6vw, 72px);
  line-height: 0.96;
  letter-spacing: -0.015em;
  margin: 0;
  max-width: 16ch;
  text-wrap: balance;
}

.accent-italic {
  font-style: italic;
  color: var(--accent);
}

.body {
  padding-top: 48px;
}

.state-text {
  font-size: 17px;
  color: var(--text-soft);
  margin: 0;
}

.groups {
  display: grid;
  gap: 48px;
}

.group-title {
  font-family: var(--font-serif);
  font-size: 26px;
  color: var(--accent);
  margin: 0 0 20px;
}

.score-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.score-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding-bottom: 18px;
}

.score-preview {
  display: block;
  aspect-ratio: 3 / 4;
  background: var(--footer-bg);
  border-bottom: 1px solid var(--border);
}

.score-preview img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.score-preview-fallback {
  width: 100%;
  height: 100%;
  display: grid;
  place-items: center;
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.1em;
  color: var(--text-mute-2);
}

.score-info {
  padding: 0 18px;
  min-width: 0;
}

.score-title {
  font-size: 16px;
  font-weight: 500;
  margin: 0;
  color: var(--text);
}

.score-notes {
  font-size: 13px;
  color: var(--text-soft);
  margin: 4px 0 0;
}

.score-date {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.08em;
  color: var(--text-mute-2);
  margin: 6px 0 0;
}

.score-card .btn {
  margin: 4px 18px 0;
  text-align: center;
}
</style>

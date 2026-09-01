<script setup>
import { computed, onUnmounted, ref, watch } from 'vue'
import { API_BASE } from '../config'

const CATEGORY_LABELS = {
  rondalla: 'Rondalla',
  baile: 'Baile galego',
  gaita: 'Gaita, pandeireta e percusión',
  outros: 'Outros',
}
const CATEGORY_ORDER = ['rondalla', 'baile', 'gaita', 'outros']
const SEARCH_DEBOUNCE_MS = 350

const scores = ref([])
const status = ref('loading') // loading | ready | error
const selectedCategory = ref('all')
const searchInput = ref('')
const search = ref('')
const page = ref(1)
const numPages = ref(1)
const availableCategories = ref([])

const filterOptions = computed(() =>
  CATEGORY_ORDER.filter((key) => availableCategories.value.includes(key)).map((key) => ({
    key,
    label: CATEGORY_LABELS[key],
  })),
)

const hasActiveFilter = computed(() => selectedCategory.value !== 'all' || search.value !== '')

let searchTimeout = null
watch(searchInput, (value) => {
  clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    search.value = value.trim()
    page.value = 1
  }, SEARCH_DEBOUNCE_MS)
})
onUnmounted(() => clearTimeout(searchTimeout))

async function fetchScores() {
  status.value = 'loading'
  try {
    const params = new URLSearchParams({ page: String(page.value) })
    if (selectedCategory.value !== 'all') params.set('category', selectedCategory.value)
    if (search.value) params.set('search', search.value)

    const res = await fetch(`${API_BASE}/api/scores/?${params}`)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const data = await res.json()

    scores.value = data.results
    numPages.value = data.num_pages
    availableCategories.value = data.available_categories
    status.value = 'ready'
  } catch {
    status.value = 'error'
  }
}

function formatDate(isoString) {
  const d = new Date(isoString)
  const day = String(d.getDate()).padStart(2, '0')
  const month = String(d.getMonth() + 1).padStart(2, '0')
  return `${day}-${month}-${d.getFullYear()}`
}

watch([selectedCategory, page, search], fetchScores, { immediate: true })
</script>

<template>
  <div class="scores">
    <section class="container hero">
      <p class="eyebrow">Partituras</p>
      <h1 class="hero-title">Partituras para <span class="accent-italic">practicar</span></h1>
    </section>

    <section class="container body">
      <div v-if="filterOptions.length > 0" class="filters">
        <div class="filter-group">
          <label class="filter-label" for="search-filter">Buscar</label>
          <input
            id="search-filter"
            type="search"
            class="filter-input"
            v-model="searchInput"
            placeholder="Título da partitura…"
          />
        </div>

        <div v-if="filterOptions.length > 1" class="filter-group">
          <label class="filter-label" for="category-filter">Categoría</label>
          <select
            id="category-filter"
            class="filter-select"
            v-model="selectedCategory"
            @change="page = 1"
          >
            <option value="all">Todas</option>
            <option v-for="cat in filterOptions" :key="cat.key" :value="cat.key">
              {{ cat.label }}
            </option>
          </select>
        </div>
      </div>

      <p v-if="status === 'loading'" class="state-text">Cargando partituras…</p>
      <p v-else-if="status === 'error'" class="state-text">
        Non se puideron cargar as partituras. Téntao de novo máis tarde.
      </p>
      <p v-else-if="scores.length === 0 && hasActiveFilter" class="state-text">
        Non se atoparon partituras coa busca actual.
      </p>
      <p v-else-if="scores.length === 0" class="state-text">
        Aínda non hai partituras dispoñibles.
      </p>

      <template v-else>
        <div class="score-grid">
          <article v-for="score in scores" :key="score.id" class="score-card">
            <a :href="score.file_url" class="score-preview" target="_blank" rel="noopener">
              <img v-if="score.preview_url" :src="score.preview_url" :alt="score.title" />
              <span v-else class="score-preview-fallback">PDF</span>
            </a>
            <div class="score-info">
              <p class="score-category">{{ score.category_display }}</p>
              <p class="score-title">{{ score.title }}</p>
              <p v-if="score.notes" class="score-notes">{{ score.notes }}</p>
              <p class="score-date">{{ formatDate(score.uploaded_at) }}</p>
            </div>
            <a :href="score.file_url" class="btn btn-outline" download>Descargar</a>
          </article>
        </div>

        <div v-if="numPages > 1" class="pagination">
          <button
            class="pagination-arrow"
            :disabled="page <= 1"
            aria-label="Páxina anterior"
            @click="page--"
          >
            ←
          </button>
          <span class="pagination-status">Páxina {{ page }} de {{ numPages }}</span>
          <button
            class="pagination-arrow"
            :disabled="page >= numPages"
            aria-label="Páxina seguinte"
            @click="page++"
          >
            →
          </button>
        </div>
      </template>
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

.filters {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 20px;
  margin-bottom: 40px;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.filter-label {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-mute-2);
}

.filter-select,
.filter-input {
  font-family: var(--font-sans);
  font-size: 14.5px;
  font-weight: 500;
  color: var(--text);
  background: var(--card-bg);
  border: 1px solid var(--border-strong);
  border-radius: 999px;
  padding: 9px 18px;
}

.filter-select {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='none' stroke='%23241d19' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 7.5l5 5 5-5'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 14px;
  padding-right: 38px;
  appearance: none;
  -webkit-appearance: none;
  cursor: pointer;
}

.filter-input {
  width: 220px;
}

.filter-input::-webkit-search-cancel-button {
  cursor: pointer;
}

.filter-select:hover,
.filter-input:hover {
  background-color: rgba(36, 29, 25, 0.06);
}

.filter-input:focus {
  outline: none;
  border-color: var(--accent);
}

.state-text {
  font-size: 17px;
  color: var(--text-soft);
  margin: 0;
}

.score-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

@media (max-width: 860px) {
  .score-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 560px) {
  .score-grid {
    grid-template-columns: 1fr;
  }
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

.score-category {
  font-family: var(--font-mono);
  font-size: 10.5px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 6px;
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

.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  margin-top: 40px;
}

.pagination-arrow {
  background: none;
  border: none;
  font-size: 22px;
  line-height: 1;
  color: var(--text);
  cursor: pointer;
  padding: 6px 10px;
  transition: color 0.15s ease;
}

.pagination-arrow:hover:not(:disabled) {
  color: var(--accent);
}

.pagination-arrow:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.pagination-status {
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.06em;
  color: var(--text-mute-2);
}
</style>

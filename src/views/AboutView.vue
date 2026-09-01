<script setup>
import baile from '../assets/images/baile.jpg'

const board = [
  { role: 'Presidencia', name: 'Inmaculada Begoña Castro Pérez' },
  { role: 'Vicepresidencia', name: 'Roberto Rabina Simón' },
  { role: 'Secretaría', name: 'Pablo Rama Vilalta' },
  { role: 'Vicesecretaría', name: 'José Antonio Rama Patiño' },
  { role: 'Tesorería', name: 'Alberto Otero Vilariño' },
  { role: 'Contaduría', name: 'María Jesús Lourido Trillo' },
  { role: 'Primeiro vocal', name: 'Margarita Graña Bermúdez' },
  { role: 'Segundo vocal', name: 'Eloi Caamaño Lourido' },
  { role: 'Terceiro vocal', name: 'Guillermo Iglesias López' },
  { role: 'Cuarto vocal', name: 'José Antonio Vázquez Rivera' },
]
</script>

<template>
  <div class="about">
    <section class="container hero">
      <p class="eyebrow">Sobre nós</p>
      <h1 class="hero-title">Dende <span class="accent-italic">1981</span> en Perillo</h1>
    </section>

    <section class="container prose-grid">
      <p class="lead">
        Semente Nova fundouse no 1981 coa idea de proporcionar á mocidade unha maneira de
        entretemento e unha formación pedagóxica e musical.
      </p>
      <p class="support">
        A misión das seccións de danza é a de facer un traballo de investigación, de recollida de
        bailes, cancións, costumes e tradicións pola nosa autonomía, e nesta labor intentar
        divulgala.
      </p>
    </section>

    <section class="container prose-grid prose-grid-second">
      <p class="support">
        En canto á sección de rondalla e coral, os obxectivos e a idea básica é a de formar
        musicalmente á xuventude, así como crear un amplo arquivo musical para a difusión da
        música.
      </p>
      <p class="support">
        Desde 1996, e co ánimo de ampliar os contactos con outras agrupacións e por tanto con
        outras tradicións, organizamos uns encontros folclóricos onde participaron formacións de
        distintas cidades de España e Portugal así como grupos de Centros Galegos en Suíza.
      </p>
    </section>

    <section class="container photo-section">
      <img :src="baile" alt="A agrupación" class="photo" />
    </section>

    <section class="container board-section">
      <p class="eyebrow">Dende o 17 de febreiro de 2023</p>
      <h2 class="board-title">A xunta directiva</h2>
      <div class="board-card">
        <div v-for="member in board" :key="member.role" class="board-row">
          <span class="board-role">{{ member.role }}</span>
          <span class="board-name">{{ member.name }}</span>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.about {
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

.prose-grid {
  padding-top: 46px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: 56px;
  align-items: start;
}

.prose-grid-second {
  padding-top: 24px;
}

.lead {
  font-size: 21px;
  line-height: 1.5;
  margin: 0;
  color: var(--text);
}

.support {
  font-size: 18px;
  line-height: 1.6;
  margin: 0;
  color: var(--text-soft);
}

.photo-section {
  padding-top: 56px;
}

.photo {
  width: 100%;
  height: 340px;
  object-fit: cover;
  border-radius: 18px;
}

.board-section {
  padding-top: 72px;
}

.board-title {
  font-family: var(--font-serif);
  font-size: 32px;
  margin: 4px 0 24px;
}

.board-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 8px 28px;
}

.board-row {
  display: grid;
  grid-template-columns: 180px 1fr;
  gap: 12px;
  font-size: 15px;
  padding: 14px 0;
  border-bottom: 1px solid var(--border);
}

.board-row:last-child {
  border-bottom: none;
}

.board-role {
  color: var(--text-mute-2);
}

.board-name {
  color: var(--text);
}

@media (max-width: 700px) {
  .prose-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .board-row {
    grid-template-columns: 1fr;
    gap: 2px;
  }
}
</style>

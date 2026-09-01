<script setup>
import oleiros from '../assets/images/oleiros.png'
</script>

<template>
  <div class="collaborators">
    <section class="container hero">
      <p class="eyebrow">Colaboradores</p>
      <h1 class="hero-title">Quen nos <span class="accent-italic">apoia</span></h1>
    </section>

    <section class="container grants">
      <article class="grant-card">
        <div class="grant-meta">
          <span class="grant-year">2024</span>
          <span class="grant-amount">1.590 €</span>
        </div>
        <p class="grant-text">
          Comunicamos que por Decreto da Alcaldía do Concello de Oleiros, nº 024003159 de data
          12/06/2024, foinos concedida á subvención do ano 2024 á nosa agrupación, Semente Nova,
          por importe de 1.590€ para ás actividades de Rondalla, Gaita e Percusión.
        </p>
      </article>

      <article class="grant-card">
        <div class="grant-meta">
          <span class="grant-year">2023</span>
        </div>
        <p class="grant-text">
          Comunicamos que por Decreto da Alcaldía do Concello de Oleiros, nº 2023006205 de data
          15/12/2023, foinos concedida á subvención do ano 2023 á nosa agrupación, Semente Nova.
        </p>
      </article>
    </section>

    <section class="container supporter">
      <p class="eyebrow">Coa colaboración de</p>
      <img :src="oleiros" alt="Concello de Oleiros" class="supporter-logo" />
    </section>
  </div>
</template>

<style scoped>
.collaborators {
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
  max-width: 14ch;
  text-wrap: balance;
}

.accent-italic {
  font-style: italic;
  color: var(--accent);
}

.grants {
  padding-top: 48px;
  display: grid;
  gap: 18px;
}

.grant-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 32px 34px;
  display: grid;
  grid-template-columns: 150px minmax(0, 1fr);
  gap: 32px;
  align-items: start;
}

.grant-meta {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.grant-year {
  font-family: var(--font-serif);
  font-size: 38px;
  line-height: 1;
  color: var(--accent);
}

.grant-amount {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  color: var(--text-mute-2);
}

.grant-text {
  font-size: 17px;
  line-height: 1.6;
  margin: 0;
  color: var(--text);
}

.supporter {
  padding-top: 56px;
}

.supporter .eyebrow {
  margin-bottom: 20px;
}

.supporter-logo {
  width: 220px;
  height: auto;
  border-radius: 8px;
}

@media (max-width: 560px) {
  .grant-card {
    grid-template-columns: 1fr;
    gap: 14px;
  }

  .supporter-logo {
    width: 180px;
  }
}
</style>

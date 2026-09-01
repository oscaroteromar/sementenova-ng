<script setup>
import oleiros from '../assets/images/oleiros.png'
</script>

<template>
  <div class="container collaborators">
    <h2 class="section-title">Colaboradores</h2>
    <hr class="divider" style="margin-left: 0" />

    <div class="grant">
      <img :src="oleiros" alt="Concello de Oleiros" class="oleiros-logo" />
      <p>
        Comunicamos que por Decreto da Alcaldía do Concello de Oleiros, nº 024003159 de data
        12/06/2024, foinos concedida á subvención do ano 2024 á nosa agrupación, Semente Nova,
        por importe de 1.590€ para ás actividades de Rondalla, Gaita e Percusión.
      </p>
    </div>

    <div class="grant">
      <img :src="oleiros" alt="Concello de Oleiros" class="oleiros-logo" />
      <p>
        Comunicamos que por Decreto da Alcaldía do Concello de Oleiros, nº 2023006205 de data
        15/12/2023, foinos concedida á subvención do ano 2023 á nosa agrupación, Semente Nova.
      </p>
    </div>
  </div>
</template>

<style scoped>
.collaborators {
  padding-top: 24px;
  padding-bottom: 24px;
  max-width: 760px;
}

.grant {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 16px 0;
  border-bottom: 1px solid var(--color-strip);
}

.grant:last-child {
  border-bottom: none;
}

.oleiros-logo {
  width: 160px;
  flex-shrink: 0;
}

.grant p {
  color: var(--color-text);
  margin: 0;
}

@media (max-width: 600px) {
  .grant {
    flex-direction: column;
    text-align: center;
  }

  .oleiros-logo {
    width: 140px;
  }
}
</style>

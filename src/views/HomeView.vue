<script setup>
import ActivityCard from '../components/ActivityCard.vue'
import guitarra from '../assets/images/guitarra.jpg'
import baile from '../assets/images/baile.jpg'
import gaita from '../assets/images/gaita.jpg'
</script>

<template>
  <div class="container home">
    <h2 class="section-title">Actividades e Prezos</h2>

    <div class="grid">
      <ActivityCard title="Rondalla" :image="guitarra">
        <p><strong>Clases de guitarra, bandurria, laúd e canto.</strong></p>
        <p>Profesor: Alfonso Delgado</p>
        <p>Horario: Sábados.</p>
        <p>&nbsp; De 11:00 a 12:30 iniciación.</p>
        <p>&nbsp; De 12:30 a 14:00 avanzado.</p>
      </ActivityCard>

      <ActivityCard title="Baile galego" :image="baile">
        <p>Profesora: Luchi</p>
        <p>Horario: Xoves, de 20:00 a 21:30</p>
        <p>Grupo infantil: Xoves, de 19:00 a 20:00.</p>
      </ActivityCard>

      <ActivityCard title="Gaita, pandeireta e percusión" :image="gaita">
        <p>Profesor: Álex</p>
        <p>Gaita: Mércores, de 19:30 a 20:30h.</p>
        <p>Pandeireta: Mércores, de 20:30 a 21:30h.</p>
      </ActivityCard>
    </div>

    <div class="cta-box">
      <p>
        <strong>Se queres aprender e disfrutar en boa compañía, anímate e contacta con nós.</strong>
      </p>
      <p><strong>¡¡ LEVAMOS MÁIS DE 40 ANOS SEN PERDER O RITMO !!</strong></p>
    </div>

    <p class="news">
      O vindeiro 27 de setembro participaremos no XXXI Encontro Folclórico en Lubre. Tes mais
      información na nosa conta de Instagram: sementenova_perillo
    </p>
  </div>
</template>

<style scoped>
.home {
  padding-top: 24px;
  padding-bottom: 24px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin: 20px 0 28px;
}

.cta-box {
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid var(--color-card-border);
  border-radius: 20px;
  padding: 16px 24px;
  text-align: center;
  max-width: 600px;
  margin: 0 auto 24px;
}

.cta-box p {
  color: var(--color-text-soft);
  font-size: 14px;
}

.cta-box p:last-child {
  margin-bottom: 0;
}

.news {
  color: var(--color-alert);
  font-weight: 700;
  font-size: 13px;
  text-align: center;
  max-width: 640px;
  margin: 0 auto;
}

@media (max-width: 700px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>

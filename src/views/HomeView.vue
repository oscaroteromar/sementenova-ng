<script setup>
import ActivityCard from '../components/ActivityCard.vue'
import guitarra from '../assets/images/guitarra.jpg'
import gaita from '../assets/images/gaita.jpg'
</script>

<template>
  <div class="home">
    <section class="container hero">
      <p class="eyebrow">Perillo · Oleiros · A Coruña</p>
      <h1 class="hero-title">
        Levamos máis de <span class="accent-italic">40 anos</span> sen perder o ritmo!!
      </h1>
      <p class="hero-lead">
        Se queres aprender e disfrutar en boa compañía, anímate e contacta con nós.
      </p>
      <div class="hero-actions">
        <a href="#actividades" class="btn btn-primary">Actividades e Prezos</a>
        <a href="mailto:info@sementenova.org" class="btn btn-outline">info@sementenova.org</a>
      </div>
    </section>

    <section class="container photo-band">
      <div class="photo-grid">
        <img :src="guitarra" alt="Clases de rondalla e guitarra" />
        <img :src="gaita" alt="Gaita galega" />
      </div>
    </section>

    <section id="actividades" class="container activities">
      <div class="activities-heading">
        <h2>Actividades e Prezos</h2>
      </div>
      <div class="activities-grid">
        <ActivityCard
          number="01"
          title="Rondalla"
          :rows="[
            { label: 'Profesor', value: 'Alfonso Delgado' },
            { label: 'Horario', value: 'Sábados.' },
            { label: '', value: 'De 11:00 a 12:30 iniciación.' },
            { label: '', value: 'De 12:30 a 14:00 avanzado.' },
          ]"
        >
          Clases de guitarra, bandurria, laúd e canto.
        </ActivityCard>

        <ActivityCard
          number="02"
          title="Baile galego"
          :rows="[
            { label: 'Profesora', value: 'Luchi' },
            { label: 'Horario', value: 'Xoves, de 20:00 a 21:30' },
          ]"
        >
          Grupo infantil: Xoves, de 19:00 a 20:00.
        </ActivityCard>

        <ActivityCard
          number="03"
          title="Gaita, pandeireta e percusión"
          :rows="[
            { label: 'Profesor', value: 'Álex' },
            { label: 'Gaita', value: 'Mércores, de 19:30 a 20:30h.' },
            { label: 'Pandeireta', value: 'Mércores, de 20:30 a 21:30h.' },
          ]"
        />
      </div>
    </section>

    <section class="container cta-section">
      <div class="cta-box">
        <p class="cta-text">
          Se queres aprender e disfrutar en boa compañía, anímate e contacta con nós.
        </p>
        <div class="cta-actions">
          <a href="tel:722705793" class="btn cta-btn-solid">722 70 57 93</a>
          <a href="mailto:info@sementenova.org" class="btn cta-btn-outline"
            >info@sementenova.org</a
          >
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home {
  padding-bottom: 8px;
}

.hero {
  padding-top: 72px;
  padding-bottom: 8px;
}

.hero-title {
  font-family: var(--font-serif);
  font-size: clamp(38px, 6vw, 78px);
  line-height: 0.94;
  letter-spacing: -0.015em;
  margin: 0;
  text-wrap: balance;
}

.accent-italic {
  font-style: italic;
  color: var(--accent);
}

.hero-lead {
  font-size: 19px;
  line-height: 1.5;
  max-width: 42ch;
  margin: 26px 0 0;
  color: var(--text-soft);
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 30px;
}

.photo-band {
  padding-top: 26px;
}

.photo-grid {
  height: 300px;
  border-radius: 18px;
  overflow: hidden;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px;
}

.photo-grid img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.activities {
  padding-top: 84px;
}

.activities-heading {
  border-bottom: 1px solid var(--border-strong);
  padding-bottom: 18px;
  margin-bottom: 36px;
}

.activities-heading h2 {
  font-family: var(--font-serif);
  font-size: clamp(30px, 4vw, 44px);
  line-height: 1;
}

.activities-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
  align-items: start;
}

.cta-section {
  padding-top: 72px;
  padding-bottom: 88px;
}

.cta-box {
  background: var(--dark);
  color: var(--dark-text);
  border-radius: 20px;
  padding: 52px 56px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 40px;
  align-items: center;
}

.cta-text {
  font-family: var(--font-serif);
  font-size: clamp(24px, 3vw, 38px);
  line-height: 1.12;
  margin: 0;
  text-wrap: pretty;
}

.cta-actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-width: 230px;
}

.cta-btn-solid {
  background: var(--dark-text);
  color: var(--dark);
  text-align: center;
}

.cta-btn-solid:hover {
  background: var(--dark-text);
  opacity: 0.9;
}

.cta-btn-outline {
  color: var(--dark-text);
  border: 1px solid rgba(246, 243, 236, 0.3);
  text-align: center;
}

.cta-btn-outline:hover {
  background: rgba(246, 243, 236, 0.1);
  color: var(--dark-text);
}

@media (max-width: 860px) {
  .activities-grid {
    grid-template-columns: 1fr;
  }

  .cta-box {
    grid-template-columns: 1fr;
    padding: 36px 32px;
  }

  .cta-actions {
    min-width: 0;
  }
}

@media (max-width: 600px) {
  .photo-grid {
    height: 220px;
  }
}
</style>

<script setup>
import { computed } from 'vue'
import mascot from '../assets/images/mascot.png'
import oleiros from '../assets/images/oleiros.png'

const lastUpdated = computed(() => {
  const yesterday = new Date()
  yesterday.setDate(yesterday.getDate() - 1)
  const day = String(yesterday.getDate()).padStart(2, '0')
  const month = String(yesterday.getMonth() + 1).padStart(2, '0')
  const year = yesterday.getFullYear()
  return `${day}-${month}-${year}`
})
</script>

<template>
  <footer class="footer">
    <div class="container footer-main">
      <div class="footer-col">
        <p class="eyebrow">Datos de contacto</p>
        <div class="contact-list">
          <a href="tel:722705793">722 70 57 93</a>
          <a href="tel:670365902">670 36 59 02</a>
          <a href="tel:649875702">649 87 57 02</a>
          <a href="mailto:info@sementenova.org">info@sementenova.org</a>
          <a
            href="https://www.instagram.com/sementenova_perillo/"
            target="_blank"
            rel="noopener"
            class="instagram-link"
          >
            <svg
              class="instagram-icon"
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              aria-hidden="true"
            >
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
              <line x1="17.5" y1="6.5" x2="17.5" y2="6.5"></line>
            </svg>
            sementenova_perillo
          </a>
        </div>
      </div>

      <div class="footer-col">
        <p class="eyebrow">Enderezo</p>
        <a
          class="address"
          href="https://www.google.com/maps/search/?api=1&query=%22R%C3%BAa%20Nova%2C%207%2C%20Baixo%20dereita%2C%2015172%20Oleiros%2C%20Spain%22"
          target="_blank"
          rel="noopener"
        >
          Rúa Nova, 7, Baixo dereita, 15172 Oleiros, Spain
        </a>
      </div>

      <div class="footer-col">
        <p class="eyebrow">Colaboradores</p>
        <img :src="oleiros" alt="Concello de Oleiros" class="collab-logo" />
      </div>

      <div class="footer-col brand-col">
        <img :src="mascot" alt="" class="mascot" width="72" height="84" />
        <p class="brand">
          Semente Nova<br />
          <span class="brand-sub">Agrupación Artística e Cultural</span>
        </p>
      </div>
    </div>

    <div class="container footer-bottom">
      <span>© Tódolos dereitos reservados</span>
      <span>Última actualización sitio web: {{ lastUpdated }}</span>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  border-top: 1px solid var(--border-strong);
  background: var(--footer-bg);
}

.footer-main {
  padding-top: 56px;
  padding-bottom: 22px;
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 40px;
}

.contact-list {
  display: grid;
  gap: 6px;
  font-size: 16px;
  line-height: 1.5;
}

.contact-list a {
  color: var(--text);
}

.contact-list a:hover {
  color: var(--accent);
}

.instagram-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.instagram-icon {
  flex: none;
}

.address {
  font-size: 16px;
  line-height: 1.5;
  color: var(--text);
  max-width: 20ch;
  display: block;
}

.address:hover {
  color: var(--accent);
}

.collab-logo {
  width: 160px;
  height: auto;
}

.brand-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 14px;
}

.mascot {
  width: 72px;
  height: 84px;
  object-fit: contain;
  border-radius: 10px;
}

.brand {
  font-family: var(--font-serif);
  font-size: 26px;
  line-height: 1.05;
  margin: 0;
  color: var(--text);
}

.brand-sub {
  font-family: var(--font-sans);
  font-size: 11px;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--text-muted);
}

.footer-bottom {
  padding-top: 22px;
  padding-bottom: 40px;
  border-top: 1px solid rgba(36, 29, 25, 0.12);
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: space-between;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-mute-2);
}

@media (max-width: 700px) {
  .footer-main {
    grid-template-columns: 1fr;
    gap: 32px;
    text-align: left;
  }

  .footer-bottom {
    justify-content: center;
    text-align: center;
  }
}
</style>

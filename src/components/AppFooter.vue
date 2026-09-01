<script setup>
import instagram from '../assets/images/instagram.png'
</script>

<template>
  <footer class="footer">
    <div class="container footer-main">
      <div class="footer-col">
        <h4 class="footer-heading">DATOS DE CONTACTO</h4>

        <p class="contact-line">
          <span class="icon" aria-hidden="true">📞</span>
          <a href="tel:722705793">722 70 57 93</a>
        </p>
        <p class="contact-line">
          <span class="icon" aria-hidden="true">✉️</span>
          <a href="mailto:info@sementenova.org">info@sementenova.org</a>
        </p>

        <p class="extra-phones">
          670 36 59 02<br />
          649 87 57 02
        </p>

        <p class="instagram-line">
          <img :src="instagram" alt="Instagram" width="20" height="20" />
          <a
            href="https://www.instagram.com/sementenova_perillo/"
            target="_blank"
            rel="noopener"
          >
            sementenova_perillo
          </a>
        </p>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">ENDEREZO</h4>
        <p class="contact-line">
          <span class="icon" aria-hidden="true">📍</span>
          <a
            href="https://www.google.com/maps/search/?api=1&query=%22R%C3%BAa%20Nova%2C%207%2C%20Baixo%20dereita%2C%2015172%20Oleiros%2C%20Spain%22"
            target="_blank"
            rel="noopener"
          >
            Rúa Nova, 7, Baixo dereita, 15172 Oleiros, Spain
          </a>
        </p>
      </div>
    </div>

    <div class="footer-strip">
      <p>© Tódolos dereitos reservados</p>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  margin-top: 32px;
  background: var(--color-footer-bg);
  border-top: 1px solid rgba(60, 60, 60, 0.2);
}

.footer-main {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  padding: 20px 16px 16px;
}

.footer-col {
  flex: 1 1 260px;
}

.footer-heading {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 10px;
}

.contact-line {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 0 8px;
}

.contact-line a:hover {
  text-decoration: underline;
}

.icon {
  font-size: 18px;
  width: 20px;
  text-align: center;
}

.extra-phones {
  margin: 0 0 8px 30px;
  line-height: 1.4;
  color: var(--color-text-soft);
}

.instagram-line {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 4px 0 0;
}

.instagram-line a:hover {
  text-decoration: underline;
}

.footer-strip {
  background: var(--color-footer-strip);
  padding: 12px 16px;
}

.footer-strip p {
  margin: 0;
  text-align: center;
  color: #fff;
  font-size: 14px;
}
</style>

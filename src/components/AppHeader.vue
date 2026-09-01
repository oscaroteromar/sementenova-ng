<script setup>
import { computed, ref } from 'vue'
import { useRoute } from 'vue-router'
import logo from '../assets/images/logo.png'
import mascot from '../assets/images/mascot.png'

const route = useRoute()
const menuOpen = ref(false)

const lastUpdated = computed(() => {
  const yesterday = new Date()
  yesterday.setDate(yesterday.getDate() - 1)
  const day = String(yesterday.getDate()).padStart(2, '0')
  const month = String(yesterday.getMonth() + 1).padStart(2, '0')
  const year = yesterday.getFullYear()
  return `${day}-${month}-${year}`
})

const links = [
  { to: '/', label: 'Actividades' },
  { to: '/sobrenos', label: 'Sobre nós' },
  { to: '/colaboradores', label: 'Colaboradores' },
]

function toggleMenu() {
  menuOpen.value = !menuOpen.value
}

function closeMenu() {
  menuOpen.value = false
}
</script>

<template>
  <header class="header">
    <div class="header-inner container">
      <router-link to="/" class="logo-link" @click="closeMenu">
        <img :src="logo" alt="A.A.C. Semente Nova" class="logo" width="132" height="120" />
      </router-link>

      <div class="title-block">
        <h1 class="title">Semente Nova</h1>
        <p class="subtitle">&nbsp; Agrupación Artística e Cultural</p>
      </div>

      <div class="meta-block">
        <p class="updated"><strong>Última actualización sitio web: {{ lastUpdated }}</strong></p>
      </div>

      <img :src="mascot" alt="" class="mascot" width="90" height="105" />

      <button
        class="burger"
        type="button"
        aria-label="Alternar menú"
        :aria-expanded="menuOpen"
        @click="toggleMenu"
      >
        <span></span><span></span><span></span>
      </button>
    </div>

    <nav class="nav" :class="{ open: menuOpen }">
      <ul class="container">
        <li v-for="link in links" :key="link.to">
          <router-link
            :to="link.to"
            class="nav-link"
            :class="{ selected: route.path === link.to }"
            @click="closeMenu"
          >
            {{ link.label }}
          </router-link>
        </li>
        <li class="more">
          <span class="nav-link expandable">Más</span>
        </li>
      </ul>
    </nav>

    <div class="header-rule"></div>
  </header>
</template>

<style scoped>
.header {
  background: #fff;
}

.header-inner {
  display: flex;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 12px 24px;
  padding-top: 14px;
  padding-bottom: 14px;
  position: relative;
}

.logo-link {
  flex-shrink: 0;
}

.logo {
  width: 100px;
  height: auto;
}

.title-block {
  flex: 1 1 220px;
  padding-top: 8px;
}

.title {
  font-size: 26px;
  text-align: center;
  color: #333;
}

.subtitle {
  font-size: 16px;
  text-align: center;
  line-height: 1.2;
  margin: 2px 0 0;
  color: #333;
}

.meta-block {
  flex: 1 1 260px;
  padding-top: 8px;
}

.updated {
  font-size: 11px;
  text-align: right;
  margin-bottom: 4px;
}

.nav ul {
  display: flex;
  justify-content: flex-end;
  gap: 4px;
  margin: 0;
  padding: 0;
  list-style: none;
  flex-wrap: wrap;
}

.nav-link {
  display: inline-block;
  padding: 8px 12px;
  color: var(--color-accent);
  font-weight: 400;
  border-right: 1px solid var(--color-accent);
  cursor: pointer;
}

.nav li:last-child .nav-link {
  border-right: none;
}

.nav-link.selected {
  font-weight: 700;
}

.nav-link:hover {
  opacity: 0.75;
}

.mascot {
  width: 64px;
  height: auto;
  flex-shrink: 0;
  margin-left: auto;
}

.header-rule {
  height: 1px;
  background: var(--color-strip);
}

.burger {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 32px;
  height: 32px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.burger span {
  display: block;
  height: 3px;
  background: var(--color-accent);
  border-radius: 2px;
}

@media (max-width: 700px) {
  .header-inner {
    align-items: center;
  }

  .title {
    font-size: 20px;
  }

  .subtitle {
    font-size: 13px;
  }

  .meta-block {
    flex-basis: 100%;
    order: 3;
  }

  .updated {
    text-align: center;
  }

  .mascot {
    display: none;
  }

  .burger {
    display: flex;
  }

  .nav {
    display: none;
    width: 100%;
  }

  .nav.open {
    display: block;
  }

  .nav ul {
    flex-direction: column;
    align-items: center;
  }

  .nav-link {
    border-right: none;
    padding: 10px;
    width: 100%;
    text-align: center;
  }
}

@media (min-width: 701px) {
  .nav ul {
    padding-right: 0;
  }
}
</style>

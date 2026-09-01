<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import logo from '../assets/images/logo.png'

const route = useRoute()
const menuOpen = ref(false)

const links = [
  { to: '/', label: 'Actividades' },
  { to: '/sobrenos', label: 'Sobre nós' },
  { to: '/colaboradores', label: 'Colaboradores' },
  { to: '/partituras', label: 'Partituras' },
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
      <router-link to="/" class="brand" @click="closeMenu">
        <img :src="logo" alt="A.A.C. Semente Nova" class="logo" width="44" height="44" />
        <span class="brand-text">
          <span class="brand-name">Semente Nova</span>
          <span class="brand-sub">Agrupación Artística e Cultural</span>
        </span>
      </router-link>

      <button
        class="burger"
        type="button"
        aria-label="Alternar menú"
        :aria-expanded="menuOpen"
        @click="toggleMenu"
      >
        <span></span><span></span><span></span>
      </button>

      <nav class="nav" :class="{ open: menuOpen }">
        <router-link
          v-for="link in links"
          :key="link.to"
          :to="link.to"
          class="nav-link"
          :class="{ active: route.path === link.to }"
          @click="closeMenu"
        >
          {{ link.label }}
        </router-link>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.header {
  position: sticky;
  top: 0;
  z-index: 20;
  background: rgba(246, 243, 236, 0.88);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
}

.header-inner {
  display: flex;
  align-items: center;
  gap: 28px;
  padding-top: 14px;
  padding-bottom: 14px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
  color: inherit;
}

.logo {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
}

.brand-text {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.brand-name {
  font-family: var(--font-serif);
  font-size: 25px;
  line-height: 1;
  color: var(--text);
}

.brand-sub {
  font-size: 10.5px;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--text-muted);
}

.nav {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 4px;
}

.nav-link {
  text-decoration: none;
  font-size: 14.5px;
  font-weight: 500;
  padding: 9px 16px;
  border-radius: 999px;
  color: var(--text);
  transition: background 0.15s ease;
}

.nav-link:hover {
  background: rgba(36, 29, 25, 0.06);
  color: var(--text);
}

.nav-link.active {
  background: var(--dark);
  color: var(--dark-text);
}

.nav-link.active:hover {
  background: var(--dark);
}

.burger {
  display: none;
  margin-left: auto;
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
  height: 2px;
  background: var(--text);
  border-radius: 2px;
}

@media (max-width: 700px) {
  .burger {
    display: flex;
  }

  .nav {
    display: none;
    width: 100%;
    order: 3;
    flex-basis: 100%;
    flex-direction: column;
    align-items: stretch;
    gap: 2px;
    margin-left: 0;
    padding-bottom: 10px;
  }

  .nav.open {
    display: flex;
  }

  .nav-link {
    text-align: center;
    padding: 12px 16px;
  }

  .header-inner {
    flex-wrap: wrap;
  }
}
</style>

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import CollaboratorsView from '../views/CollaboratorsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView, meta: { title: 'Actividades' } },
    { path: '/sobrenos', name: 'about', component: AboutView, meta: { title: 'Sobre nós' } },
    { path: '/colaboradores', name: 'collaborators', component: CollaboratorsView, meta: { title: 'Colaboradores' } },
  ],
  scrollBehavior() {
    return { top: 0 }
  },
})

router.afterEach((to) => {
  document.title = `${to.meta.title} | sementenova.org`
})

export default router

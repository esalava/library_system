import { createRouter, createWebHistory } from 'vue-router'
import User from '../views/User.vue'
import HomeView from '../views/HomeView.vue'
import Admin from '../views/Admin.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component:  HomeView
    },
    {
      path: '/library/user/:username/',
      name: 'user',
      component: User
    },
    {
      path: '/library/admin/',
      name: 'admin',
      component:  Admin
    },
  ]
})

export default router

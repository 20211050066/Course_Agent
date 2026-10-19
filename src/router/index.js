import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/layout/home'
    },
    {
      path: '/layout',
      name: 'Layout',
      component: () => import('@/assets/layout/Layout.vue'),
      children: [
        {
          path: 'home',
          name: 'Home',
          component: () => import('@/views/Home.vue')
        },
        {
          path: 'lab',
          name: 'Lab',
          component: () => import('@/views/Lab.vue')
        },
        {
          path: 'device',
          name: 'Device',
          component: () => import('@/views/Device.vue')
        },
        {
          path: 'user',
          name: 'User',
          component: () => import('@/views/User.vue')
        }
      ]
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/Login.vue')
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('@/views/Register.vue')
    }
  ]
})

export default router

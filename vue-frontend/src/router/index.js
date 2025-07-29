import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/pages/HomePage.vue'
import UploadPage from '@/pages/UploadPage.vue'
import VideoPlayerPage from '@/pages/VideoPlayerPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomePage,
    },
    {
      path: '/upload',
      name: 'upload',
      component: UploadPage
    },
    {
      path: '/watch',
      name: 'watch',
      component: VideoPlayerPage
    },

  ],
})

export default router

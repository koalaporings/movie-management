import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/pages/HomePage.vue'
import UploadPage from '@/pages/UploadPage.vue'
import VideoPlayerPage from '@/pages/VideoPlayerPage.vue'
import LoginPage from '@/pages/LoginPage.vue';
import RegisterPage from '@/pages/RegisterPage.vue';

const router = createRouter({
  history: createWebHistory(),
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
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    },
    {
        path: '/register',
        name: 'register',
        component: RegisterPage
    }

  ],
});

router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('access_token');

    if (to.name === 'register') {
        next();
        return;
    }

    if (to.name !== 'login' && !token) {
        next({ name: 'login' });
    } else if (to.name === 'login' && token) {
        next({ name: 'home' }); // Prevent login if already logged in
    } else {
        next();
    }
});

export default router

import TournamentsView from '@/views/TournamentsView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:"/",
      name:"TournamentsView",
      component: TournamentsView

    },
    {
      path:"/register",
      name:"RegisterPage",
      component: RegisterPage

    },
    {
      path:"/login",
      name:"LoginPage",
      component: LoginPage

    },
    
  ]
})

export default router

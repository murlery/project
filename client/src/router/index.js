import TattoosView from '@/views/TattooView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import TattooView from '../views/TattooView.vue';
import StyleView from '../views/StyleView.vue';
import PriceView from '../views/PriceView.vue';
import TattooArtist from '../views/TattooArtist.vue';
import TattooStudioView from '../views/TattooStudioView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:"/",
      name:"TattooView",
      component: TattooView

    },
    {
      path:"/styles",
      name:"StyleView",
      component: StyleView

    },
    {
      path:"/prices",
      name:"PriceView",
      component: PriceView

    },
    {
      path:"/tattooArtists",
      name:"TattooArtistView",
      component: TattooArtist

    },
    {
      path:"/tatooStudios",
      name:"TattooStudioView",
      component: TattooStudioView

    },
  ]
})

export default router

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TrainNew from '../components/TrainNew.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/train/new',
    name: 'TrainNew',
    component: TrainNew
  }
]

const router = new VueRouter({
  routes
})

export default router

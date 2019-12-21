import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TrainNew from '../views/TrainNew.vue'
import Exception from '../views/Exception.vue'

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
  },
  {
    path: '/exception',
    name: 'Exception',
    component: Exception
  },
]

const router = new VueRouter({
  routes
})

export default router

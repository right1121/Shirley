import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TrainNew from '../views/TrainNew.vue'
import Train from '../views/Train.vue'
import Exception from '../views/Exception.vue'
import { Auth } from 'aws-amplify'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: { isPublic: true },
  },
  {
    path: '/train',
    name: 'Train',
    component: Train
  },
  {
    path: '/train/new',
    name: 'TrainNew',
    component: TrainNew
  },
  {
    path: '/exception',
    name: 'Exception',
    component: Exception,
    meta: { isPublic: true }
  },
]

const router = new VueRouter({
  routes
})

router.beforeEach(async (to, from, next) => {
  if (to.matched.some(record => record.meta.isPublic)) {
    return next()
  }
  else {
    Auth.currentAuthenticatedUser()
    .then( () => {
      return next()
    })
    .catch( () => {
      return next({
        path: '/'
      });
    })
  }
});

export default router

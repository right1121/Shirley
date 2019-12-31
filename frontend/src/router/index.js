import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TrainNew from '../views/TrainNew.vue'
import Train from '../views/Train.vue'
import Exception from '../views/Exception.vue'
import { Auth } from 'aws-amplify'
import { AmplifyEventBus } from 'aws-amplify-vue';
import Store from '../store';

Vue.use(VueRouter)

function getUser() {
  return Auth.currentAuthenticatedUser()
  .then((data) => {
    if (data.signInUserSession) {
      Store.commit('setUser', data);
      return data;
    } 
  }).catch(() => {
    Store.commit('setUser', null);
    return null
  });
}


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

AmplifyEventBus.$on('authState', async (state) => {
  if (state === 'signedIn') {
    getUser();
    router.push({path: '/train'});
  } else if (state === 'signedOut') {
    Store.commit('setUser', null);
  }
});

router.beforeResolve(async (to, from, next) => {
  if (to.matched.some(record => record.meta.isPublic)) {
    return next()
  }
  let user = await getUser();
  if (user) {
    return next();
  }
  return next({path: '/'});
});

export default router

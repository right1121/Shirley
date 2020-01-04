import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
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
  let color = 'info'
  let message = ''

  if (state === 'signedIn') {
    getUser();
    router.push({path: '/train'});
    message = 'サインインしました'
  } else if (state === 'signedOut') {
    Store.commit('setUser', null);
    router.push({path: '/'});
    message = 'サインアウトしました'
  }
  Store.dispatch('pushMessage', {message, color})
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

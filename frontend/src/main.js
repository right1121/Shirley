import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import api from './api'
import AmplifyConfig from './amplify'
import Amplify, * as AmplifyModules from 'aws-amplify'
import { AmplifyPlugin } from 'aws-amplify-vue'
import vuetify from './plugins/vuetify'
import VueAdsense from 'vue-adsense'

Amplify.configure(AmplifyConfig)

Vue.component('adsense', VueAdsense)

Vue.use(AmplifyPlugin, AmplifyModules)

Vue.config.productionTip = false

Vue.prototype.$api = api

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

<template>
  <div id="app">
    <Menu/>
    <amplify-sign-out v-if="isSignedIn"></amplify-sign-out>
    <router-view/>
  </div>
</template>

<script>
import { AmplifyEventBus } from 'aws-amplify-vue'
import { Auth } from 'aws-amplify'
import Menu from './components/Menu'

export default {
  name: 'app',
  components: {
    Menu
  },
  data() {
    return {
      isSignedIn: false
    }
  },
  async beforeCreate() {
    try {
      await Auth.currentAuthenticatedUser()
      this.isSignedIn = true
    } catch (err) {
      this.isSignedIn = false
    }
    AmplifyEventBus.$on('authState', info => {
      if (info === 'signedIn') {
        this.isSignedIn = true
      } else if (info === 'signedOut') {
        this.isSignedIn = false
        this.$router.push({ path: '/' })
      } else {
        this.isSignedIn = false
      }
    });
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

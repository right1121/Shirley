<template>
  <v-app id="app">
    <v-message/>
    <v-nav/>
    <router-view/>
  </v-app>
</template>

<script>
import Nav from './components/Nav'
import Message from './components/Message'

export default {
  name: 'app',
  components: {
    'v-nav': Nav,
    'v-message': Message
  },
  data() {
    return {
      isSignedIn: false
    }
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

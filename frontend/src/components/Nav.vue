<template>
  <div v-if="user">
    <router-link to="/train">車両一覧</router-link> |
    <a href="#" @click="signOut">サインアウト</a>
  </div>
</template>

<script>
import { Auth } from 'aws-amplify'
import { AmplifyEventBus } from 'aws-amplify-vue'

export default {
  name: 'v-nav',
  computed: {
    user() {
      return this.$store.getters.getUser;
    },
  },
  methods: {
    signOut() {
      Auth.signOut()
      .then(data => {
        AmplifyEventBus.$emit('authState', 'signedOut');
        return data;
      })
    }
  }
}
</script>

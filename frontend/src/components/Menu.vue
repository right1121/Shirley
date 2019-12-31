<template>
  <div v-if="user">
    <router-link to="/train">車両一覧</router-link> |
    <router-link to="/train/new">車両追加</router-link>
  </div>
</template>

<script>
export default {
  name: 'menu',
    computed: {
    user() {
      return this.$store.getters.getUser;
    },
  },
}
</script>

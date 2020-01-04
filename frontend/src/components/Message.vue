<template>
  <v-snackbar
    v-model="snackbar"
  >
    {{ text }}
  </v-snackbar>
</template>

<script>
  export default {
    data () {
      return {
        snackbar: false,
        text: 'Hello, I\'m a snackbar',
      }
    },
  }
  </script>
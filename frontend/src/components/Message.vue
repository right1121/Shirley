<template>
  <v-snackbar
    v-model="snackbar"
    top
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
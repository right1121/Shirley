<template>
  <v-snackbar
    v-model="snackbar"
    :color="color"
    :timeout="timeout"
    top
  >
    {{ text }}
    <v-btn
      dark
      text
      @click="snackbar = false"
    >
      閉じる
    </v-btn>
  </v-snackbar>
</template>

<script>
  export default {
    data () {
      return {
        snackbar: false,
        color: '',
        timeout: 3500,
        text: 'Hello, I\'m a snackbar',
      }
    },
  }
  </script>
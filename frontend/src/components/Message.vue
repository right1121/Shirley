<template>
  <v-snackbar
    v-model="messageData.snackbar"
    :color="color"
    :timeout="timeout"
    top
  >
    {{ messageData.text }}
    <v-btn
      dark
      text
      @click="messageData.snackbar = false"
    >
      閉じる
    </v-btn>
  </v-snackbar>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    computed: {
      ...mapState(['messageData']),
    },
    data () {
      return {
        snackbar: false,
        color: '',
        timeout: 3500,
        text: 'Hello, I\'m a snackbar',
      }
    },
    methods: {
      ...mapActions(['pushMessage']),
      pushMessage() {
        this.pushMessage()
      }
    }
  }
  </script>
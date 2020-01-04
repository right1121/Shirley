<template>
  <v-snackbar
    v-model="messageData.snackbar"
    :color="messageData.color"
    :timeout="messageData.timeout"
    top
  >
    {{ messageData.text }}
    <v-btn
      dark
      text
      @click="pullMessage"
    >
      閉じる
    </v-btn>
  </v-snackbar>
</template>

<script>
import { mapState } from 'vuex'

export default {
    computed: {
      ...mapState(['messageData']),
    },
    methods: {
      pullMessage () {
        this.$store.dispatch('pullMessage')
      }
    }
  }
  </script>
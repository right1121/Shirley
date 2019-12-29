<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
    <button @click="queryTrain">get</button>
  </div>
</template>

<script>
import { Auth } from 'aws-amplify'

  export default {
    data () {
      return {
        headers: [
          {
            text: '会社名',
            value: 'company',
          },
          {
            text: 'メーカー',
            value: 'maker',
          },
          {
            text: '形式',
            value: 'series'
          },
          {
            text: '両数',
            value: 'cars' 
          },
        ],
        desserts: [],
      }
    },
    methods: {
      queryTrain() {
        Auth.currentAuthenticatedUser()
        .then( response => {
          const config = {
            'headers': {
              'Authorization': response.signInUserSession.idToken.jwtToken
            }
          }

          this.$api.get('/train', {}, config)
          .then( (response) => {
            this.desserts = response.data.Items
          })
        })
      }
    }
  }
</script>
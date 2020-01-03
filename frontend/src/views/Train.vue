<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :items-per-page="5"
      class="elevation-1"
      :loading="loading"
      loading-text="Loading... Please wait"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>所有車両</v-toolbar-title>

          <v-spacer></v-spacer>

          <v-toolbar-items>
            <v-btn text>Link 1</v-btn>
          </v-toolbar-items>
        </v-toolbar>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import { Auth } from 'aws-amplify'

  export default {
    data () {
      return {
        loading: true,
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
    created () {
      this.queryTrain()
    },
    methods: {
      queryTrain() {
        this.loading = true
        Auth.currentAuthenticatedUser()
        .then( response => {
          const config = {
            'headers': {
              'Authorization': response.signInUserSession.idToken.jwtToken
            }
          }
          return this.$api.get('/train', config)
        })
        .then( (response) => {
          this.desserts = response.data.Items
        })
        .finally( () => {
          this.loading = false
        })
      }
    }
  }
</script>
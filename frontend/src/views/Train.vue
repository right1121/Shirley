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

          <v-dialog v-model="dialog" max-width="600px">
            <template v-slot:activator="{ on }">
              <v-btn color="primary" dark v-on="on">車両登録</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <h2>車両追加</h2>
              </v-card-title>
              <v-card-text>
                <v-train-form
                  api-type="post"
                  @close="dialogClose"
                >
                </v-train-form>
              </v-card-text>
              <v-card-actions>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import { Auth } from 'aws-amplify'
import TrainForm from '@/components/TrainForm'

  export default {
    data () {
      return {
        dialog: false,
        loading: true,
        headers: [
          {
            text: '品番',
            value: 'part_number',
          },
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
          {
            text: '箱数',
            value: 'case_count' 
          },
          {
            text: 'ロット',
            value: 'lot' 
          },
          {
            text: '備考',
            value: 'memo' 
          },
        ],
        desserts: [],
      }
    },
    components: {
      'v-train-form': TrainForm
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
      },

      dialogClose() {
        this.dialog = false
        this.queryTrain()
      }
    }
  }
</script>
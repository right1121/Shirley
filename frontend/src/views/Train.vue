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

          <v-btn
            color="primary"
            dark
            @click.stop="addItem"
          >
            車両登録
          </v-btn>

          <v-dialog v-model="dialog" max-width="600px" persistent>
            <v-card>
              <v-card-title>
                <h2>車両{{ formType }}</h2>
              </v-card-title>
              <v-card-text>
                <v-train-form
                  :api-type="apiType"
                  v-bind="param"
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
      <template v-slot:item.action="{ item }">
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          mdi-pencil-outline
        </v-icon>
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
          { 
            text: '操作',
            value: 'action',
            sortable: false 
          },
        ],
        desserts: [],
        param: {},
        apiType: "post"
      }
    },
    components: {
      'v-train-form': TrainForm
    },
    computed: {
      formType() {
        if (this.apiType === 'post'){
          return '登録'
        } else {
          return '編集'
        }
      }
    },
    created () {
      this.queryTrain()
      this.paramReset()
    },

    watch: {
      dialog(val) {
        val || this.paramReset()
      }
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

      paramReset() {
        this.param = {
          part_number: "",
          company:  "",
          maker:  "",
          series:  "",
          cars:  "",
          case_count:  1,
          lot:  undefined,
          memo:  undefined,
        }
      },

      addItem() {
        this.apiType = 'post'
        this.param = this.paramReset()
        this.dialog = true
      },

      editItem(item) {
        this.apiType = 'edit'
        this.param = item
        this.dialog = true
      },

      dialogClose() {
        this.paramReset()
        this.dialog = false
        this.queryTrain()
      }
    }
  }
</script>
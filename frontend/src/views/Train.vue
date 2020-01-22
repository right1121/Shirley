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
                <v-form @submit.prevent="putTrain" ref="putTrainForm">
                  <v-text-field
                    v-model="param.part_number"
                    label="品番"
                  ></v-text-field>
                  <v-select
                    v-model="param.company"
                    :items="companyList"
                    label="会社名"
                    :rules="rules.company"
                  ></v-select>
                  <v-select
                    v-model="param.maker"
                    :items="makerList"
                    label="メーカー"
                    :rules="rules.maker"
                  ></v-select>
                  <v-text-field
                    v-model="param.series"
                    label="形式"
                    hint="例）E231"
                    :rules="rules.series"
                  ></v-text-field>
                  <v-text-field
                    v-model.number="param.cars"
                    :rules="rules.cars"
                    label="両数"
                    min=1
                    max=99
                    type="number"
                  ></v-text-field>
                  <v-text-field
                    label="箱数"
                    v-model.number="param.case_count"
                    :rules="rules.case_count"
                    min=1
                    max=99
                    type="number"
                  ></v-text-field>
                  <v-text-field
                    label="ロット"
                    v-model.number="param.lot"
                    type="number"
                  ></v-text-field>
                  <v-text-field
                    label="備考"
                    v-model="param.memo"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="save">Save</v-btn>
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
        param: {
          train_id: "",
          part_number: "",
          company: "",
          maker: "",
          series: "",
          cars: "",
          case_count: 1,
          lot: "",
          memo: "",
        },
        rules: {
          company: [
            value => !!value || '必須項目です',
          ],
          maker: [
            value => !!value || '必須項目です',
          ],
          series: [
            value => !!value || '必須項目です',
          ],
          cars: [
            value => !!value || '必須項目です',
            value => 1 <= value || '1以上を入力してください',
            value => value <= 99  || '99以下を入力してください',
            ],
          case_count: [
            value => !!value || '必須項目です',
            value => 1 <= value || '1以上を入力してください',
            value => value <= 99  || '99以下を入力してください',
          ]
        },
        apiType: "post"
      }
    },
    computed: {
      formType() {
        if (this.apiType === 'post'){
          return '登録'
        } else {
          return '編集'
        }
      },

      companyList() {
        return this.$store.state.masterData.railway_company
      },
      makerList() {
        return this.$store.state.masterData.model_maker
      }
    },
    created () {
      this.$store.dispatch('fetchMasterData')
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
          train_id: "",
          part_number: "",
          company: "",
          maker: "",
          series: "",
          cars: "",
          case_count: 1,
          lot: "",
          memo: "",
        }
      },

      save() {},

      editItem(item) {
        this.apiType = 'edit'
        this.param = item
        this.dialog = true
      },

      close() {
        this.paramReset()
        this.$refs.putTrainForm.resetValidation()
        this.dialog = false
        this.queryTrain()
      }
    }
  }
</script>
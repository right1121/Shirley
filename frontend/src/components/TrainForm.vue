<template>
  <div>
    <v-form @submit.prevent="putTrain" ref="putTrainForm">
      <v-text-field
        v-model="params.part_number"
        label="品番"
      ></v-text-field>
      <v-select
        v-model="params.company"
        :items="company"
        label="会社名"
        :rules="rules.company"
      ></v-select>
      <v-select
        v-model="params.maker"
        :items="maker"
        label="メーカー"
        :rules="rules.maker"
      ></v-select>
      <v-text-field
        label="形式"
        hint="例）E231"
        v-model="params.series"
        :rules="rules.series"
      ></v-text-field>
      <v-text-field
        v-model.number="params.cars"
        :rules="rules.cars"
        label="両数"
        min=1
        max=99
        type="number"
      ></v-text-field>
      <v-text-field
        label="箱数"
        v-model.number="params.case_count"
        :rules="rules.case_count"
        min=1
        max=99
        type="number"
      ></v-text-field>
      <v-text-field
        label="ロット"
        v-model.number="params.lot"
        type="number"
      ></v-text-field>
      <v-text-field
        label="備考"
        v-model="params.memo"
      ></v-text-field>
      <v-btn
        block
        depressed
        type="submit">
        登録
      </v-btn>
    </v-form>
    <v-btn
      block
      depressed
      @click="close">
      キャンセル
    </v-btn>
  </div>

</template>

<script>
import { Auth } from 'aws-amplify'

export default {
  data() {
    return {
      params: {
        part_number: "",
        company: "",
        maker: "",
        series: "",
        cars: "",
        case_count: 1,
        lot: null,
        memo: null,
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
      }
    }
  },
  created () {
    this.$store.dispatch('fetchMasterData')
  },
  computed: {
    company() {
      return this.$store.state.masterData.railway_company
    },
    maker() {
      return this.$store.state.masterData.model_maker
    }
  },
  methods: {
    validate () {
      return this.$refs.putTrainForm.validate()
    },
  
    putTrain() {
      if (!this.validate()){
        return false
      }
      const params = this.params

      Auth.currentAuthenticatedUser()
      .then( response => {
        
        params.ownerId = response.username
        const config = {
          'headers': {
            'Authorization': response.signInUserSession.idToken.jwtToken
          }
        }
        this.$api.post('/train', params, config)
          .then( () => {
            this.$store.dispatch(
              'pushMessage',
              {
                message: '登録しました',
                color: 'success'
              }
            )
            this.close()
          })
          .catch( (error) => {
            if (error.response.status === 400){
              this.$store.dispatch(
                'pushMessage',
                {
                  message: '入力を確認してください',
                  color: 'warning'
                }
              )
            } else {
              this.$router.push('/Exception')
            }
          })
      })
      .catch ( () => {
        this.$router.push({path: 'exception'})
      })

    },

    close() {
      this.$emit('close');
    }
  }
}
</script>
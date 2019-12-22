<template>
  <div>
    <h1>車両追加</h1>
    <form @submit.prevent="putTrain">
      <input v-model="company" placeholder="会社名" required>
      <br>
      <input v-model="maker" placeholder="メーカー" required>
      <br>
      <input v-model="series" placeholder="形式" required>
      <br>
      <input v-model="cars" type="number" min="1" max="99" placeholder="両数" required>
      <br>
      <button type="submit">登録</button>
    </form>
  </div>

</template>

<script>
import { Auth } from 'aws-amplify'

export default {
  data() {
    return {
      "company": "",
      "maker": "",
      "series": "",
      "cars": "",
    }
  },
  methods: {
    putTrain() {
      const param = {
        'ownerId': "",
        'company': this.company,
        'maker': this.maker,
        'series': this.series,
        'cars': this.cars
      }

      Auth.currentAuthenticatedUser()
      .then( response => {
        param.owner_id = response.username
      })
      .catch ( () => {
        this.$router.push({path: 'exception'})
      })

      this.$api.post('/train', param)
        .then( (response) => {
          console.log("正常", response)
        })
        .catch( (error) => {
          if (error.response.status === 400){
            console.log("statusCode")
          } else {
            this.$router.push('/Exception')
          }
        })
    }
  }
}
</script>
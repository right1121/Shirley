<template>
  <div>
    <h1>車両追加</h1>
    <input v-model="company" placeholder="会社名">
    <br>
    <input v-model="maker" placeholder="メーカー">
    <br>
    <input v-model="series" placeholder="形式">
    <br>
    <input v-model="cars" type="number" min="1" max="99" placeholder="両数">
    <br>
    <button @click="putTrain">登録</button>
  </div>

</template>

<script>
export default {
  data() {
    return {
      "company": "",
      "maker": "",
      "series": "",
      "cars": "",
    }
  },
  method: {
    putTrain() {
    }
  }
}
</script>
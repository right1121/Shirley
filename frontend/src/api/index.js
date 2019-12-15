import axios from 'axios'

const api = axios.create({
    baseURL: 'https://3s5tztkfv5.execute-api.ap-northeast-1.amazonaws.com/develop'
})

export default api;

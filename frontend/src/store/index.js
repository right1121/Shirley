import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    hasMasterData: false,
    masterData: {
      model_maker: [],
      railway_company: [],
    },
    messageData: {
      snackbar: false,
      color: '',
      timeout: 3500,
      text: '',
    }
  },
  getters: {
    getUser: state => {
      return state.user
    }
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    updateMasterData(state, masterData) {
      state.masterData = masterData
      state.hasMasterData = true
    },
    pushMessage (state, payload) {
      state.messageData.text = payload.message
      state.messageData.color = payload.color
      state.messageData.snackbar = true
    }
  },
  actions: {
    fetchMasterData({ state, commit }) {
      if (state.hasMasterData) {
        return
      }
      api.get('/master')
      .then( (response) => {
        commit('updateMasterData', response.data)
      })
    },

    pushMessage ({ commit }, { message, color }) {
      commit('pushMessage', { message, color })
    },
  },
  modules: {
  }
})

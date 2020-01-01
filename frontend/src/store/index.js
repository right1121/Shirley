import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    hasMasterData: false,
    masterData: {
      modelMaker: [],
      railway_company: [],
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
    }
  },
  modules: {
  }
})

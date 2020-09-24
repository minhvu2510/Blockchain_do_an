import { getToken, setToken, removeToken, setTokenOtp, getTokenOtp, setUser, getUser } from '@/utils/auth'
const user = {
  state: {
    token: getToken(),
    token_otp: getTokenOtp(),
    // token: 'vudeptrai',
    email: '',
    role: '',
    id: getUser(),
    check: ''
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_TOKEN_OTP: (state, token) => {
      state.token_otp = token
    },
    SET_EMAIL: (state, email) => {
      state.email = email
    },
    SET_ROLE: (state, role) => {
      state.role = role
    },
    SET_ID: (state, id) => {
      state.id = id
    },
    SET_CHECK: (state, check) => {
      state.check = check
    }
  },

  actions: {
    gotAccessToken({ commit }, token) {
      return new Promise((resolve, reject) => {
        commit('SET_TOKEN', token)
        setToken(token)
        resolve()
      })
    },
    gotAccessTokenOtp({ commit }, token) {
      return new Promise((resolve, reject) => {
        commit('SET_TOKEN_OTP', token)
        setTokenOtp(token)
        resolve()
      })
    },
    SetAction({ commit }, str) {
      commit('SET_CHECK', str)
    },

    // Get user information
    GetUserInfo({ commit }, id) {
      return new Promise((resolve, reject) => {
        commit('SET_ID', id)
        setUser(id)
        resolve()
        // commit('SET_EMAIL', response)
        // commit('SET_ACC', 'minhvu')
        // commit('SET_ROLE', response)
      })
    },
    // Sign out
    LogOut({ commit, state }) {
      commit('SET_TOKEN', '')
      removeToken()
      window.location.href = process.env.APP_URL + '/login'
      // window.location.href = process.env.SSO_URL + '/logout?service=' + process.env.APP_URL + '&gateway=true'
      // window.location.href = 'https://manage.vccloud.vn/cas' + '/login?service=https://manage-callcenter.vccloud.vn/'
    },
    FedLogOut({ commit }) {
      return new Promise(resolve => {
        commit('SET_TOKEN', '')
        removeToken()
        window.location.href = process.env.APP_URL + '/login'
        // resolve()
      })
    }
  }
}

export default user

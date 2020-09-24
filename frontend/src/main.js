import Vue from 'vue'
import App from './App.vue'
import Element from 'element-ui'
import locale from 'element-ui/lib/locale'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
// import App from './App'
import VueAxios from 'vue-axios'
import '@/styles/index.scss' // global css'
import {scroller} from 'vue-scrollto/src/scrollTo'
// import VueRouter from 'vue-router'
import router from './router'
// Vue.use(VueRouter)
import Vuex from 'vuex'
import VueSession from 'vue-session'
import VueCookies from 'vue-cookies'
import store from './store'
const firstScrollTo = scroller()
const secondScrollTo = scroller()
firstScrollTo('#el1')
secondScrollTo('#el2')
Vue.use(VueSession)
Vue.use(VueCookies)
Vue.use(VueAxios, axios)
Vue.use(Vuex)
Vue.use(Element, {
  size: 'small', // set element-ui default size
  locale
})
Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: {
    App
  }
})

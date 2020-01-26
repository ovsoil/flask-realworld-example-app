import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import VJsoneditor from 'v-jsoneditor'

import './filters'

Vue.config.productionTip = false
Vue.use(VJsoneditor)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

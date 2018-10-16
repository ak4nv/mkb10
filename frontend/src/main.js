import Vue from 'vue'
import app from './app.vue'
import router from './router'
import VueAxios from './vue-axios'
import Notifications from './components/notifications'

Vue.use(VueAxios)
Vue.mixin(Notifications)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(app)
}).$mount('#app')

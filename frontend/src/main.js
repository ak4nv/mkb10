// // Vue is a global object linked via script tag

import VueAxios from './vue-axios.js'
Vue.use(VueAxios)

const notification_mixin = require('./notifications/mixin.js')
Vue.mixin(notification_mixin)

Vue.component('app', require('./components/app.vue'))
const router = require('./router.js')
const app = new Vue({ router }).$mount('app')

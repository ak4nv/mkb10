import VueRouter from 'vue-router'

const routes = require('./routes.js')
const router = new VueRouter({ routes })

router.options.linkActiveClass = 'active'

module.exports = router
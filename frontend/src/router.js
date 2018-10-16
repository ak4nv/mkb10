import Vue from 'vue'
import Router from 'vue-router'
import routes from './views'
import Page404 from './page404'

Vue.use(Router)

export default new Router({
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      redirect: '/icd/tree',
      children: routes,
      component: {
        render (c) { return c('router-view') }
      }
    },
    {
      path: '*',
      component: Page404
    }
  ]
})

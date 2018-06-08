module.exports = [
  {
    path: '/',
    redirect: {name: 'tree'}
  },
  {
    name: 'tree',
    path: '/tree',
    component: require('./components/tree.vue')
  },
  {
    name: 'find',
    path: '/find',
    component: require('./components/find.vue')
  },
  {
    name: 'icdo',
    path: '/icdo/block',
    component: require('./components/icdo.vue')
  },
  {
    name: 'find-icdo',
    path: '/icdo/find',
    component: require('./components/find-icdo.vue')
  }
]
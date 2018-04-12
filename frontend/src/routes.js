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
  }
]
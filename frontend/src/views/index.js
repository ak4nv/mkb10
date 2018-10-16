import treeICD from './tree-icd.vue'
import findICD from './find-icd.vue'
import treeICDO from './tree-icdo.vue'
import findICDO from './find-icdo.vue'

export default [
  {
    path: 'icd',
    component: {
      render (c) { return c('router-view') }
    },
    children: [
      {
        path: 'tree',
        name: 'icd-tree',
        component: treeICD
      },
      {
        path: 'find',
        name: 'icd-find',
        component: findICD
      }
    ]
  },
  {
    path: 'icdo',
    component: {
      render (c) { return c('router-view') }
    },
    children: [
      {
        path: 'tree',
        name: 'icdo-tree',
        component: treeICDO
      },
      {
        path: 'find',
        name: 'icdo-find',
        component: findICDO
      }
    ]
  }
]
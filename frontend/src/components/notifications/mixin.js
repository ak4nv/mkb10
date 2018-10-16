import NotificationStore from './store.js'

export default {
  methods: {
    $info (text, options = {}) {
      NotificationStore.add(Object.assign({
        type: 'primary',
        text,
        delay: 2
      }, options))
    },

    $error (text, options = {}) {
      NotificationStore.add(Object.assign({
        type: 'error',
        text
      }, options))
    },

    $warn (text, options = {}) {
      NotificationStore.add(Object.assign({
        type: 'warning',
        text,
        delay: 5
      }, options))
    },

    $success (text, options = {}) {
      NotificationStore.add(Object.assign({
        type: 'success',
        text,
        delay: 2
      }, options))
    }
  }
}

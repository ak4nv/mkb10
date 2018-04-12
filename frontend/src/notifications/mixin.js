const NotificationStore = require('./store.js')

module.exports = {
  methods: {
    $notify (text, options = {}) {
      NotificationStore.add(Object.assign({
        type: 'primary',
        text,
        timeout: true,
        delay: 2000,
      }, options))
    },

    $error (text, options = {}) {
      NotificationStore.add(Object.assign({
        type: 'error', 
        text,
        timeout: false,
      }, options))
    },

    $warn (text, options = {}) {
      NotificationStore.add(Object.assign({
        type: 'warning', 
        text,
        timeout: true,
        delay: 5000, //optional, default: 3000
      }, options))
    },

    $success (text, options = {}) {
      NotificationStore.add(Object.assign({
        type: 'success', 
        text,
        timeout: true, 
        delay: 2000 //optional, default: 3000
      }, options))
    },
  }
}
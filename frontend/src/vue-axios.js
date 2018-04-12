const axios = require('axios')
const NotificationStore = require('./notifications/store.js')

// Add header for all queries
axios.defaults.baseURL = baseURL;
//axios.defaults.withCredentials = true;
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
axios.defaults.headers.post['Content-Type'] = 'text/plain';

// Add a request interceptor
axios.interceptors.request.use(function (config) {
    // Do something before request is sent
    if (typeof(axios._this.loading) != 'undefined') {
      axios._this.loading = true
    }
    NotificationStore.clean()
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });


axios.interceptors.response.use(function (resp) {
    // Do something with response data
    if (typeof(axios._this.loading) !== 'undefined') {
      axios._this.loading = false
    }
    if (resp.data.msg)
      axios._this.$success(resp.data.msg)
    return resp;
  }, function (error) {
    if (error.response) {
      axios._this.$error(error.response.data.err || error.response.statusText);
    } else axios._this.$error(error.message)
    if (typeof(axios._this.loading) !== 'undefined') {
      axios._this.loading = false
    }
    // Do something with response error
    return Promise.reject(error);
  });

function plugin(Vue) {

    if (plugin.installed) {
        return;
    }

  Object.defineProperties(Vue.prototype, {

    $http: {
      get() {
        axios._this = this
        return axios
      }
    }

  });
}

export default plugin;

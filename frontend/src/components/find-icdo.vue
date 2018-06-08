<template>
  <typeahead
    placeholder="Поиск по коду МКБ-О или названию"
    :suggestions="items"
    :loading="loading"
    v-model="q"
    @input="onInput"
    @reset="onReset" />
  </div>
</template>
<script>
  import { debounce } from 'lodash'
  import typeahead from './typeahead.vue'

  export default {
    components: { typeahead },
    data () {
      return {
        q: '',
        items: [],
        loading: false,
      }
    },
    methods: {
      onReset () {
        this.q = ''
        this.items = []
      },
      onInput: debounce(function() {
        if (this.q.length > 1) {
          this.$http
            .get('/api/icdo/lookup', {params: {q: this.q}})
            .then(resp => { this.items = resp.data })
        }
        if (this.q.length == 0) this.onReset()
      }, 500)
    },
    watch: {
      q (val) {
        if (!val) {
          this.items = []
        }
      }
    }
  }
</script>
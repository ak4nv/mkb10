<template>
  <typeahead
    placeholder="Поиск по коду МКБ-О или названию"
    :suggestions="items"
    :loading="loading"
    v-model="q"
    @input="onInput"
    @reset="onReset" />
</template>
<script>
  import typeahead from '@/components/typeahead.vue'

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
      onInput () {
        if (this.q.length > 1) {
          this.$http
            .get('/api/icdo/lookup', {params: {q: this.q}})
            .then(resp => { this.items = resp.data })
        } else if (this.q.length == 0) { this.onReset() }
      }
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
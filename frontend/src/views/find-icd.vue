<template>
  <typeahead
    placeholder="Поиск по коду МКБ или названию"
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
        map: {
          'Й': 'Q',
          'Ц': 'W',
          'У': 'E',
          'К': 'R',
          'Е': 'T',
          'Н': 'Y',
          'Г': 'U',
          'Ш': 'I',
          'Щ': 'O',
          'З': 'P',
          'Ф': 'A',
          'Ы': 'S',
          'В': 'D',
          'А': 'F',
          'П': 'G',
          'Р': 'H',
          'О': 'J',
          'Л': 'K',
          'Д': 'L',
          'Я': 'Z',
          'Ч': 'X',
          'С': 'C',
          'М': 'V',
          'И': 'B',
          'Т': 'N',
          'Ь': 'M'
        }
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
            .get('/api/lookup', {params: {q: this.q}})
            .then(resp => { this.items = resp.data })
        } else if (this.q.length == 0) { this.onReset() }
      }
    },
    watch: {
      q (val) {
        if (!val)
          this.items = []
        if (!/[a-zA-Z]/.test(val[0]) && /[0-9]/.test(val[1]))
          var r = this.map[val[0].toUpperCase()]
          if (r) this.q = r + val.slice(1)
      }
    }
  }
</script>
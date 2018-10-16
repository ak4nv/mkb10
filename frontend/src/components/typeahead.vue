<template>
  <div>
    <input
      ref="input"
      type="text"
      class="form-input"
      style="width: 100%;"
      autocomplete="off"
      onclick="this.select();"
      :placeholder="placeholder"
      :value="value"
      :disabled="loading"
      @input="onInput($event.target.value)"
      @keydown.esc="reset" />
    <div v-for="(item, index) in suggestions"
         :class="{'selected': index == current}"
         v-html="render(item)"
         :key="index" />
  </div>
</template>
<script>
  export default {
    props: {
      value: {
        type: String,
        required: true
      },
      loading: {
        type: Boolean,
        required: false
      },
      delay: {
        type: Number,
        default: 500
      },
      suggestions: {
        type: Array,
        required: true,
      },
      placeholder: {
        type: String,
        default: 'Поиск'
      }
    },
    data () {
      return {
        debounce: null,
        tooltip: null,
        current: -1,
      }
    },
    mounted () {
      this.focus()
    },
    methods: {
      onInput (v) {
        if (this.debounce) {
          clearTimeout(this.debounce)
        }
        this.debounce = setTimeout(() => { this.$emit('input', v) }, this.delay)
      },
      reset () {
        this.$emit('reset')
        this.focus()
      },
      render (item) {
        return `<span class="name">${this.highlight(item.name)}</span> <small class="text-success float-right">[${this.highlight(item.code)}]</small>`
      },
      highlight (val) {
        var re = new RegExp("(" + this.value.split(' ').join('|') + ")", "gi");
        return val.replace(re, '<mark>$1</mark>')
      },
      focus () {
        this.$refs.input.focus()
      }
    },
    watch: {
      loading (val) {
        if (!val) {
          this.$nextTick(this.focus)
        }
      }
    }
  }
</script>
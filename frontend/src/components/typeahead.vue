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
      @input="$emit('input', $event.target.value)"
      @keydown.esc="reset" />
    <div
      v-for="(item, index) in suggestions"
      :class="{'selected': index == current}"
      v-html="render(item)" />
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
        tooltip: null,
        current: -1,
      }
    },
    mounted () {
      this.focus()
    },
    methods: {
      reset () {
        this.$emit('reset')
        this.focus()
      },
      render (item) {
        return `<span class="name">${this.highlight(item.name)}</span> <small class="float-right">[${this.highlight(item.code)}]</small>`
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
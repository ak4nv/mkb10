<template>
  <div>
    <template v-for="item in classes">
      <div :class="{'bg-primary': active == item.id}">
        <button class="btn btn-sm circle" @click="active = item.id == active ? 0 : item.id">
          <i :class="['icon', active == item.id ? 'icon-arrow-down':'icon-arrow-up']"></i>
        </button>
        <span v-text="item.name"></span>
      </div>
      <block style="margin-left: 1rem;" v-if="item.id == active" :cls="item.id"></block>
    </template>
  </div>
</template>
<script>
  import block from './block.vue'

  export default {
    components: { block },
    data () {
      return {
        active: 0,
        classes: []
      }
    },
    created () {
      this.$http.get('/api').then(resp => this.classes = resp.data)
    }
  }
</script>
<style>
  div {
    min-height: 1.5rem
  }
</style>
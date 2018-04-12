<template>
  <div>
    <template v-for="item in blocks">
      <div :class="{'bg-primary': active == item.id}">
        <button class="btn btn-sm circle" @click="active = item.id == active ? 0 : item.id">
          <i :class="['icon', active == item.id ? 'icon-arrow-down':'icon-arrow-up']"></i>
        </button>
        <span v-text="item.name"></span>
      </div>
      <group style="margin-left: 1rem;" v-if="item.id == active" :block="item.id"></group>
    </template>
  </div>
</template>
<script>
  import group from './group.vue'

  export default {
    components: { group },
    props: ['cls'],
    data () {
      return {
        active: 0,
        blocks: [],
      }
    },
    created () {
      this.get_data(this.cls)
    },
    methods: {
      get_data (id) {
        this.$http.get(`/api/${id}`).then(resp => this.blocks = resp.data)
      }
    },
    watch: {
      cls (val) {
        this.get_data(val)
      }
    }
  }
</script>
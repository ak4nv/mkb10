<template>
  <div>
    <div v-for="item in blocks">
      [<span v-text="item.code"></span>]
      <span v-text="item.name"></span>
    </div>
  </div>
</template>
<script>
  export default {
    props: ['id'],
    data () {
      return {
        blocks: [],
      }
    },
    created () {
      this.get_data(this.id)
    },
    methods: {
      get_data (id) {
        this.$http.get(`/api/icdo/block/${id}`).then(resp => this.blocks = resp.data)
      }
    },
    watch: {
      id (val) {
        this.get_data(val)
      }
    }
  }
</script>
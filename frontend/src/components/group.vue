<template>
  <div>
    <div v-for="item in groups">
      <div v-if="item.has_subgroup" class="btn btn-sm btn-default btn-action float-right" @click="show_sg(item.code)">
        <i :class="['icon', active == item.code ? 'icon-minus':'icon-plus']"></i>
      </div>
      [<span v-text="item.code"></span>]
      <span v-if="item.actual" v-text="item.name"></span>
      <del v-else v-text="item.name"></del>
      <template v-if="item.code == active">
        <div v-for="subg in subgroups">
          [<span v-text="subg.code"></span>]
          <span v-if="subg.actual" v-text="subg.name"></span>
          <del v-else v-text="subg.name"></del>
        </div>
      </template>
    </div>
  </div>
</template>
<script>
  export default {
    props: ['block'],
    data () {
      return {
        active: '',
        groups: [],
        subgroups: []
      }
    },
    created () {
      this.get_data(this.block)
    },
    methods: {
      get_data (id) {
        this.$http.get(`/api/${id}/group?all`).then(resp => this.groups = resp.data)
      },
      show_sg (code) {
        if (code == this.active) {
          this.active = ''
          this.subgroups = []
        } else {
          this.$http.get(`/api/${code}/subgroup?all`).then(resp => {
            this.subgroups = resp.data
            this.active = code
          })
        }
      }
    },
    watch: {
      block (val) {
        this.active = ''
        this.subgroups = []
        this.get_data(val)
      }
    }
  }
</script>
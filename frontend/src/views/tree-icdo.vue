<template>
  <div>
    <node v-for="blk in blocks" name="blocks" :key="blk.id" :item="blk" @checked="onChecked">
      <template v-if="checkedItems.includes(blk.id)">
        <item v-for="item in get_items(blk)"
              :key="item.id"
              :item="item" />
      </template>
    </node>
  </div>
</template>
<script>
  import node from '@/components/node.vue'
  import item from '@/components/item.vue'

  export default {
    components: { node, item },
    data () {
      return {
        checkedItems: [],
        blocks: []
      }
    },
    created () {
      this.$http.get('/api/icdo/block').then(resp => {
        resp.data.map(el => {
          el.codes = []
          return el
        })
        this.blocks = resp.data
      })
    },
    methods: {
      get_items (item) {
        if (!item.codes.length) {
          this.$http.get(`/api/icdo/block/${item.id}`).then(resp => {
            item.codes = resp.data.map(el => {
              el.actual = true
              return el
            })
          })
        }
        return item.codes
      },
      onChecked (v) {
        let i = this.checkedItems.indexOf(v)
        if (i === -1) {
          this.checkedItems.push(v)
        } else {
          this.checkedItems = this.checkedItems.filter(el => el !== v)
        }
      }
    }
  }
</script>
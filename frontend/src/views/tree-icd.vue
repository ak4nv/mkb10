<template>
  <div>
    <node v-for="cls in classes" name="classes" :key="cls.id" :item="cls" @checked="onChecked">
      <template v-if="checkedItems.includes(cls.id)">
        <node class="mx-2"
              name="blocks"
              v-for="blk in get_blocks(cls)"
              @checked="onChecked"
              :key="blk.id"
              :item="blk">
          <template v-if="checkedItems.includes(blk.id)">
            <div class="mx-2" v-for="grp in get_groups(blk)" :key="grp.id">
              <node v-if="grp.has_subgroup"
                    name="groups"
                    :item="grp"
                    @checked="onChecked">
                <template v-if="checkedItems.includes(grp.id)">
                  <item v-for="subgrp in get_subgroup(grp)"
                        :key="subgrp.id"
                        :item="subgrp" />
                </template>
              </node>
              <item v-else :item="grp" />
            </div>
          </template>
        </node>
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
        classes: []
      }
    },
    created () {
      this.$http.get('/api').then(resp => {
        this.classes = resp.data.map(el => {
          el.blocks = []
          return el
        })
      })
    },
    methods: {
      get_blocks (item) {
        if (!item.blocks.length) {
          this.$http.get(`/api/${item.id}`).then(resp => {
            item.blocks = resp.data.map(el => {
              el.groups = []
              return el
            })
          })
        }
        return item.blocks
      },
      get_groups (item) {
        if (!item.groups.length) {
          this.$http.get(`/api/${item.id}/group?all`).then(resp => {
            item.groups = resp.data.map(el => {
              if (el.has_subgroup) {
                el.subgroup = []
              }
              return el
            })
          })
        }
        return item.groups
      },
      get_subgroup (item) {
        if (!item.subgroup.length) {
          this.$http.get(`/api/${item.code}/subgroup?all`).then(resp => {
            item.subgroup = resp.data
          })
        }
        return item.subgroup
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
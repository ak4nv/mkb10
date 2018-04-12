<template>
  <div v-if="store.items.length" class="notifications">
    <notification v-for="item in store.items" :key="item.id" :notification="item" @remove="remove" />
  </div>
</template>
<script>
  import notification from './notification.vue'

  export default {
    props: ['store'],
    components: {
      notification
    },
    methods: {
      remove (item) {
        this.store.remove(item)
      }
    }
  }
</script>
<style scoped>
  .notifications {
    width: 30%;
    top: 20px;
    right: 10px;
    position: fixed;
    overflow: hidden;
    padding: 10px;
    z-index: 10;
  }
  .notifications div {
    margin-bottom: 10px;
    box-shadow: 3px 3px 10px rgba(0,0,0,0.5);
  }
</style>
<template>
  <div>
    <span class="text-success">[{{item.code}}] </span>
    <span v-if="item.actual" v-text="item.name" />
    <del v-else v-text="item.name" />
  </div>
</template>
<script>
  export default {
    props: ['item']
  }
</script>
<style scoped>
  div {
    padding-left: 30px;
  }
</style>
<template>
  <div class="accordion">
    <input type="checkbox" :name="name" :id="item.id" hidden>
    <label class="accordion-header c-hand" :for="item.id" @click="$emit('checked', item.id)">
      <i class="icon icon-arrow-right mr-1 text-primary"></i> {{item.name}}
    </label>
    <slot class="accordion-body"></slot>
  </div>
</template>
<script>
  export default {
    props: ['item', 'name']
  }
</script>
<template>
   <transition name="fade">
    <div :class="['toast', 'toast-'+notification.type]">
      <button class="btn btn-clear float-right" @click="remove(notification)"></button>
      {{ notification.text }}
    </div>
   </transition>
</template>
<script>
  export default {
    props: ['notification'],
    mounted () {
      if (this.notification.timeout)
        setTimeout(function () {
          this.remove(this.notification)
        }.bind(this), this.notification.delay)
    },
    methods: {
      remove (item) {
        this.$emit('remove', item)
      }
    }
  }
</script>
<style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity .3s
  }
  .fade-enter, .fade-leave-to {
    opacity: 0
  }
</style>
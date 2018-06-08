<template>
  <div class="container">
    <notifications :store="store" />
    <div class="col-7 col-mx-auto">
      <h3 class="text-center">Справочник МКБ10 и МКБ-О <small>(с обновлениями от 01.01.2015)</small></h3>
      <ul class="tab">
        <router-link class="tab-item" tag="li" :to="{name: 'tree'}">
          <a>Дерево</a>
        </router-link>
        <router-link class="tab-item" tag="li" :to="{name: 'find'}">
          <a>Поиск</a>
        </router-link>
        <router-link class="tab-item" tag="li" :to="{name: 'icdo'}">
          <a>Дерево МКБ-О</a>
        </router-link>
        <router-link class="tab-item" tag="li" :to="{name: 'find-icdo'}">
          <a>Поиск МКБ-О</a>
        </router-link>
      </ul>
      <br>
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
  import store from '../notifications/store.js'
  import notifications from '../notifications/component.vue'

  export default {
    components: { notifications },
    data () {
      return {
        store: store
      }
    }
  }
</script>
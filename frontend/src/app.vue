<template>
  <div class="container">
    <notifications />
    <div class="col-7 col-mx-auto">
      <h3 class="text-center">Справочник МКБ-10 и МКБ-О <small>(с обновлениями от 01.01.2015)</small></h3>
      <ul class="tab">
        <router-link class="tab-item"
                     v-for="url in urls"
                     :to="{name: url.name}"
                     :key="url.name"
                     tag="li">
          <a v-text="url.url_name"></a>
        </router-link>
      </ul>
      <br>
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
  import notifications from '@/components/notifications/main.vue'

  export default {
    components: { notifications },
    data () {
      return {
        urls: [
          { name: 'icd-tree', url_name: 'Дерево МКБ-10' },
          { name: 'icd-find', url_name: 'Поиск МКБ-10' },
          { name: 'icdo-tree', url_name: 'Дерево МКБ-О' },
          { name: 'icdo-find', url_name: 'Поиск МКБ-О' }
        ]
      }
    }
  }
</script>
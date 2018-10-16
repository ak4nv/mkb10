<template>
  <div class="empty bg-default">
    <div class="empty-icon">
      <i class="icon icon-3x icon-stop"></i>
    </div>
    <p class="empty-title h5">Page not Found (404) — {{ $route.path }}</p>
    <p class="empty-subtitle">There is no page by this url you requested.</p>
    <div class="empty-action">
      <p>Try to return on previous page or open the <a :href="$http.defaults.baseURL || '/'">root</a> of the site.</p>
    </div>
  </div>
</template>
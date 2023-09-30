<template>
  <header class="header">
    <div class="header-item">
      <router-link v-bind:to="{ name: 'home' }">
        <img src="../assets/logo.jpg" alt="Logo" class="header-image" />
      </router-link>
    </div>
  </header>
</template>


<style>
.header {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.header-item {
  margin-left: 10px;
  margin-right: 10px;
}

.header-image {
  width: 100px;
}

.header .header-item:first-child {
  margin-right: auto;
}

</style>
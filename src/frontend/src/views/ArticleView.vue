<script setup>
import { useRoute } from "vue-router";
import HeaderComponent from '../components/HeaderComponentLogoOnly.vue';

const route = useRoute();
const title = route.params.title
const content = route.params.content
</script>

<template>
  <HeaderComponent/>
    <div class="container">
    <h2>{{ title }}</h2>
    <p>{{ content }}</p>
    <a href="/">トップページに戻る</a>
  </div>
</template>

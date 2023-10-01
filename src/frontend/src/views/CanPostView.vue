<script setup>
import { defineOptions } from 'vue';
import { useRoute } from "vue-router";
import HeaderComponent from '../components/HeaderComponentLogoOnly.vue';

defineOptions({
  inheritAttrs: false
})

const route = useRoute();
const PostStatus = route.params.PostStatus.toLowerCase() === "true" ? "投稿しました" : "投稿に失敗しました";
</script>

<template>
  <HeaderComponent/>
    <div class="container">
    <h2>{{ PostStatus }}</h2>
    <a href="/">トップページに戻る</a>
  </div>
</template>

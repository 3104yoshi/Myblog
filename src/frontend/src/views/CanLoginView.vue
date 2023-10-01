<script setup>
import { useRoute } from "vue-router";
import HeaderComponent from '../components/HeaderComponentLogoOnly.vue';

const route = useRoute();
const LoginStatus = route.params.LoginStatus.toLowerCase() === "true" ? "ログインしました" : "ログインに失敗しました";
</script>

<template>
  <HeaderComponent/>
    <div class="container">
    <h2>{{ LoginStatus }}</h2>
    <a href="/">トップページに戻る</a>
  </div>
</template>

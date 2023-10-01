<script setup>
import { defineOptions } from 'vue';
import { useRoute } from "vue-router";
import HeaderComponent from '../components/HeaderComponentLogoOnly.vue';

defineOptions({
  inheritAttrs: false
})

const route = useRoute();
const SignupStatus = route.params.SignupStatus.toLowerCase() === "true" ? "登録しました" : "既に登録されているユーザー名です"
</script>

<template>
  <HeaderComponent/>
    <div class="container">
    <h2>{{ SignupStatus }}</h2>
    <a href="/auth/Login">ログインページに戻る</a>
  </div>
</template>

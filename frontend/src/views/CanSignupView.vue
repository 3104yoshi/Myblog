<script setup>
import { defineOptions } from 'vue';
import { useRoute } from "vue-router";
import HeaderComponent from '../components/HeaderComponentLogoOnly.vue';

defineOptions({
  inheritAttrs: false
})

const route = useRoute();
const SignupStatus = route.params.SignupStatus
</script>

<template>
  <HeaderComponent/>
    <div class="container">
    <h2>{{ SignupStatus }}</h2>
    <a href="/auth/Login">Loginページに戻る</a>
  </div>
</template>

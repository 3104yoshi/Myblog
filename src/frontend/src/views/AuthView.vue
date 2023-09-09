<script setup>
import { defineOptions } from 'vue';
import { useRoute } from "vue-router";
import HeaderComponent from '../components/HeaderComponentLogoOnly.vue';
import LoginComponent from '../components/LoginComponent.vue';
import SignupComponent from '../components/SignupComponent.vue';

defineOptions({
  inheritAttrs: false
})

const route = useRoute()
const AuthType = route.params.AuthType
let isLogin = AuthType === 'Login'
</script>

<template>
  <HeaderComponent/>
  <LoginComponent v-if="isLogin"/>
  <SignupComponent v-else />
</template>

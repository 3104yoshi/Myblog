<script setup>
import { useRoute } from "vue-router";
import HeaderComponent from '../components/HeaderComponentLogoOnly.vue';
import LoginComponent from '../components/LoginComponent.vue';
import SignupComponent from '../components/SignupComponent.vue';

const route = useRoute()
const AuthType = route.params.AuthType
let isLogin = AuthType === 'login'
</script>

<template>
  <HeaderComponent/>
  <LoginComponent v-if="isLogin"/>
  <SignupComponent v-else />
</template>

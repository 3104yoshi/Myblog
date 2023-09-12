<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const isLogin = ref(null);
onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1/auth/isLogin')
    if (response.status === 200) {
      isLogin.value = response.data;
    }
    else {
      console.error('Failed to fetch data:', response.status, response.statusText);
    }
  }
  catch (error) {
    console.log(error);
  }});
</script>

<template>
  <header class="header">
    <div class="header-item">
      <router-link v-bind:to="{ name: 'home' }">
        <img src="../assets/logo.jpg" alt="Logo" class="header-image" />
      </router-link>
    </div>
    <div class="header-item">
      <form action="/post">
        <button class="header-button" id="post-button">post</button>
      </form>
    </div>
    <div class="header-item" v-if="!isLogin">
      <router-link v-bind:to="{ name : 'auth', params : { AuthType : 'login' } }" >
        <button class="header-button" id="login-button">Login</button>
      </router-link>
    </div>
    <div class="header-item" v-if="!isLogin">
      <router-link v-bind:to="{ name : 'auth', params : { AuthType : 'signup' } }" >
        <button class="header-button" id="signup-button">Signup</button>
      </router-link>
    </div>
    <div class="header-item" v-if="isLogin">
      <form action="/auth/logout">
        <button class="header-button" id="logout-button">Logout</button>
      </form>
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
  width: 60px;
}

.header .header-item:first-child {
  margin-right: auto;
}

.header-button {
  width: 200px;
  height: 50px;
  border-radius: 5px;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
}

#post-button {
  background-color: #1e8ba4;
}

#post-button:hover {
  background-color: #1b6e82;
}

#login-button {
  background-color: #45a049;
}

#login-button:hover {
  background-color: #3c8942;
}

#signup-button {
  background-color: #823df2;
}

#signup-button:hover {
  background-color: #6e2cc4;
}

#logout-button {
  background-color: #970b76;
}

#logout-button:hover {
  background-color: #7a0a5e;
}
</style>
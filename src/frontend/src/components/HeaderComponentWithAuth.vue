<template>
  <header class="header">
    <div class="header-item">
      <router-link v-bind:to="{ name: 'home' }">
        <img src="../assets/logo.jpg" alt="Logo" class="header-image" />
      </router-link>
    </div>
    <div class="header-item">
      <router-link v-bind:to="{ name : 'post' }">
        <button class="header-button" id="post-button">post</button>
      </router-link>
    </div>
    <div class="header-item">
      <router-link v-bind:to="{ name : 'auth', params : { AuthType : 'Login' } }" >
        <button class="header-button" id="login-button">Login</button>
      </router-link>
    </div>
    <div class="header-item">
      <router-link v-bind:to="{ name : 'auth', params : { AuthType : 'Signup' } }" >
        <button class="header-button" id="signup-button">Signup</button>
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
</style>
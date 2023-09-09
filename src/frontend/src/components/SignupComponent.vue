<template>
  <div class="container">
  <h2>Signup</h2>
  <form action="signup" method="POST">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>

    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>

    <input type="submit" value="Sign up" id="signup-button">
  </form>
  <div id="auth-login">
    <a href="/auth/Login" >Loginへ</a>
  </div>
</div>
</template>

<style>
body {
  font-family: Arial, sans-serif;
}

.container {
  width: 300px;
  margin: 0 auto;
  margin-top: 100px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

h2 {
  text-align: center;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 5px;
  margin-bottom: 10px;
}

form {
  margin: 20px;
}

#signup-button {
  background-color: #823df2;
}

#signup-button:hover {
  background-color: #6e2cc4;
}

#auth-login {
  background-color: white;
  color: #823df2;
  text-align: center;
}

</style>
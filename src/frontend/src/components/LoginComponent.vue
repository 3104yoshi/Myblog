<template>
  <div class="container">
    <h2>Login</h2>
    <form action="login" method="POST">
      <div class="canLogin"></div>
      <label  for="username">Username:</label>
      <input type="text" id="username" name="username" required>

      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>

      <input type="submit" value="Login" id="login-button">
    </form>
    <div id="auth-signup">
      <a href="/auth/signup">Signupへ</a>
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

input[type="submit"] {
  width: 100%;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

form {
  margin: 20px;
}

#login-button {
  background-color: #45a049;
}

#login-button:hover {
  background-color: #3c8942;
}

#auth-signup {
  background-color: white;
  text-align: center;
}

</style>

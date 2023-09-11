<template>
  <div class="container">
    <h2>新しい記事の作成</h2>
    <form action="/post" method="POST">
      <label  for="article-title">タイトル</label>
      <input type="text" id="article-title" name="title">

      <label for="article-content">本文</label>
      <textarea id="article-content" name="content" required></textarea>

      <input type="submit" value="記事を作成する" id="post-article">
    </form>
  </div>
</template>

<style>
body {
  font-family: Arial, sans-serif;
}

.container {
  width: 90%;
  margin: auto;
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

input[type="text"] {
  width: 100%;
  padding: 5px;
  margin-bottom: 10px;
}

#article-content {
  width: 100%;
  height: 800px;
  resize: none;
}

input[type="submit"] {
  margin-top: 20px;
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

#post-article {
  background-color: #1e8ba4;
}

#post-article:hover {
  background-color: #1b6e82;
}

</style>

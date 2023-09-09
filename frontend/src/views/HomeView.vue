<script setup>
import HeaderComponent from '../components/HeaderComponentWithAuth.vue';
import ArticleComponent from '../components/ArticleComponent.vue';

const articles = [
  {
    title: '1',
    body: '1'
  },
  {
    title: '2',
    body: '2'
  },
  {
    title: '3',
    body: '3'
  }
]

</script>

<template>
  <HeaderComponent/>
  <div id="body">
    <ul id="articles">
      <ArticleComponent v-for="article in articles" :key="article.title" :title="article.title" :body="article.body" class="article"/>
    </ul>
  </div>
</template>

<style>
#articles {
  justify-content: space-around;
}

.article {
  display: inline-block;
  width: 370px;
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: white;
  box-shadow: 0 0 5px #ccc;
}

</style>
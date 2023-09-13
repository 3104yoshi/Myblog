<script setup>
import HeaderComponent from '../components/HeaderComponentWithAuth.vue';
import ArticleHeadlineComponent from '../components/ArticleHeadlineComponent.vue';
import axios from 'axios';
import { onMounted, ref } from 'vue';

const articles = ref(null);
onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1/api/articles')
    if (response.status === 200) {
      articles.value = response.data;
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
  <HeaderComponent/>
  <ul id="articles">
    <ArticleHeadlineComponent v-for="article in articles" :key="article.title" :title="article.title" :content="article.content" class="article-headline"/>
  </ul>
</template>

<style>
#articles {
  display: flex;
  flex-wrap: wrap;
}

.article-headline {
  color: #000;
  border: 1px solid black;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 370px;
  height: 370px;
  margin: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: rgb(247, 254, 248);
  box-shadow: 0 0 5px #ccc;
}

</style>
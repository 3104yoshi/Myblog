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
  <div id="body">
    <ul id="articles">
      <router-link v-bind:to="{ name: 'article', params: { title: article.title, content: article.content } }" v-for="article in articles" :key="article.title">
        <ArticleHeadlineComponent :title="article.title" :content="article.content" class="article"/>
      </router-link>
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
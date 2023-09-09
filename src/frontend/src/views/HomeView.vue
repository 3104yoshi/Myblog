<script setup>
import HeaderComponent from '../components/HeaderComponentWithAuth.vue';
import ArticleComponent from '../components/ArticleComponent.vue';
import axios from 'axios';
import { onMounted, ref } from 'vue';

// await axios.get('http://127.0.0.1/api/articles')
//   .then(response => (articles = response.data))
//   .catch(error => {
//     console.log(error);
//   });

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
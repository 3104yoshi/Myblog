<script setup>
import HeaderComponent from '../components/HeaderComponentWithAuth.vue';
import PagingComponent from '../components/PagingComponent.vue';
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
  <PagingComponent v-if="articles" :articles="articles" :maxArticlesPerPage="8" />
</template>

<style>
#articles {
  display: flex;
  flex-wrap: wrap;
  padding: 0 auto;
  margin: 0 auto;
}

.article-headline {
  color: #000;
  border: 1px solid black;
  display: flex;
  justify-content: center;
  align-items: center;
  width: calc(100% / 4 - 50px);
  min-width: 300px;
  height: 300px;
  margin: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: rgb(247, 254, 248);
  box-shadow: 0 0 5px #ccc;
}

</style>
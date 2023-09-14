<script setup>
import ArticleHeadlineComponent from '../components/ArticleHeadlineComponent.vue';
import { ref, computed } from 'vue';

const props = defineProps(['articles', 'maxArticlesPerPage'])
const pageCount = computed(() => Math.ceil(props.articles.length / props.maxArticlesPerPage));
const currentPage = ref(1);

const articlesOnCurrentPage = computed(() => {
  const startIndex = (currentPage.value - 1) * props.maxArticlesPerPage;
  const endIndex = Math.min(props.articles.length ,currentPage.value * props.maxArticlesPerPage);
  return props.articles.slice(startIndex, endIndex);
});
</script>

<template>
  <div>
    <ul id="articles">
      <ArticleHeadlineComponent v-for="article in articlesOnCurrentPage" :key="article.title" :title="article.title" :content="article.content" class="article-headline"/>
    </ul>
    <div id="paging-footer">
      <li v-for="page in pageCount" :key="page" class="paging-item">
        <button @click="currentPage = page" class="paging-button">{{ page }}</button>
      </li>
    </div>
  </div>
</template>

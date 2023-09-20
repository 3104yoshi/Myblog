<script setup>
import ArticleHeadlineComponent from '../components/ArticleHeadlineComponent.vue';
import PagenationComponent from './PagenationComponent.vue';
import { ref, computed } from 'vue';

const props = defineProps(['articles', 'maxArticlesPerPage'])
const pageCount = computed(() => Math.ceil(props.articles.length / props.maxArticlesPerPage));
const currentPage = ref(1);

const articlesOnCurrentPage = computed(() => {
  const startIndex = (currentPage.value - 1) * props.maxArticlesPerPage;
  const endIndex = Math.min(props.articles.length ,currentPage.value * props.maxArticlesPerPage);
  return props.articles.slice(startIndex, endIndex);
});

const displayPageNumbers = computed(() => {
  const pageNumbers = [];
  for (let i = Math.max(1, currentPage.value - 2); i <= Math.min(currentPage.value + 2, pageCount.value); i++) {
    pageNumbers.push(i);
  }
  return pageNumbers;
});

const moveCurrentPage = (movedPage) => {
  currentPage.value = movedPage;
}

</script>

<template>
  <div>
    <ul id="articles">
      <ArticleHeadlineComponent v-for="article in articlesOnCurrentPage" :key="article.title" :title="article.title" :content="article.content" class="article-headline"/>
    </ul>
    <div id="footer">
        <PagenationComponent :currentPage="currentPage" :pageCount="pageCount" :displayPageNumbers="displayPageNumbers" @moveCurrentPage="moveCurrentPage"/>
    </div>
  </div>
</template>

<style>
.paging-footer {
  display: flex;
  justify-content: center;
  list-style: none;
}

.paging-item {
  margin: 0 5px;
}

.selectedItem>.paging-button {
  background-color: #d0d0d0;
  font-weight: bold;
} 

</style>
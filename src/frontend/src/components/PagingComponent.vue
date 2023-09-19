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

const displayPageNumbers = computed(() => {
  const pageNumbers = [];
  for (let i = Math.max(1, currentPage.value - 2); i <= Math.min(currentPage.value + 2, pageCount.value); i++) {
    pageNumbers.push(i);
  }
  return pageNumbers;
});

</script>

<template>
  <div>
    <ul id="articles">
      <ArticleHeadlineComponent v-for="article in articlesOnCurrentPage" :key="article.title" :title="article.title" :content="article.content" class="article-headline"/>
    </ul>
    <div id="footer">
      <ul class="paging-footer">
        <li v-if="currentPage > 1">
          <button @click="currentPage = 1" class="paging-button">&lt;&lt;</button>
        </li>
        <li v-if="currentPage > 1">
          <button @click="currentPage--" class="paging-button">&lt;</button>
        </li>
        <li v-if="currentPage > 3">
          <div> ...</div>
        </li>
        <li v-for="page in displayPageNumbers" :key="page" class="paging-item" :class="{selectedItem : page === currentPage}">
          <button @click="currentPage = page" class="paging-button">{{ page }}</button>
        </li>
        <li v-if="pageCount - currentPage > 2">
          <div>... </div>
        </li>
        <li v-if="currentPage < pageCount">
          <button @click="currentPage++" class="paging-button">&gt;</button>
        </li>
        <li v-if="currentPage < pageCount">
          <button @click="currentPage = pageCount" class="paging-button">&gt;&gt;</button>
        </li>
      </ul>
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
<script setup>
import { ref } from 'vue';

const emit = defineEmits(['moveCurrentPage'])

const props = defineProps(['pageCount', 'displayPageNumbers', 'pageCount'])

const currentPage = ref(props.currentPage);

const moveCurrentPage = (movedPage) => {
  currentPage.value = movedPage;
  emit('moveCurrentPage', currentPage.value);
}


</script>

<template>
<div id="footer">
    <ul class="paging-footer">
      <li v-if="currentPage > 1">
        <button @click="moveCurrentPage(1)" class="paging-button">&lt;&lt;</button>
      </li>
      <li v-if="currentPage > 1">
        <button @click="moveCurrentPage(currentPage-1)" class="paging-button">&lt;</button>
      </li>
      <li v-if="currentPage > 3">
        <div> ...</div>
      </li>
      <li v-for="page in displayPageNumbers" :key="page" class="paging-item" :class="{selectedItem : page === currentPage}">
        <button @click="moveCurrentPage(page)" class="paging-button">{{ page }}</button>
      </li>
      <li v-if="pageCount - currentPage > 2">
        <div>... </div>
      </li>
      <li v-if="currentPage < pageCount">
        <button @click="moveCurrentPage(currentPage+1)" class="paging-button">&gt;</button>
      </li>
      <li v-if="currentPage < pageCount">
        <button @click="moveCurrentPage(pageCount)" class="paging-button">&gt;&gt;</button>
      </li>
    </ul>
</div>
</template>
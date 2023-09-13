<script setup>
const article = defineProps(['title', 'content'])

</script>

<template>
    <div>
        <router-link v-bind:to="{ name: 'article', params: { title: article.title, content: article.content } }" class="article-link">
            <div class="article-title">{{ article.title }}</div>
        </router-link>
    </div>
</template>

<style>

.article-link {
    width: fit-content;
}

.article-title {
    display: inline-block;
}
</style>
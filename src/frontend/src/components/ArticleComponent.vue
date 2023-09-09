<script setup>
const article = defineProps(['title', 'body'])

</script>

<template>
    <div class="article">
        <p>{{ article.title }}</p>
        <p>{{ article.body }}</p>
    </div>
</template>
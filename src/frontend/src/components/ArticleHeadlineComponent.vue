<script setup>
const article = defineProps(['title'])

</script>

<template>
    <div class="article">
        <p>{{ article.title }}</p>
    </div>
</template>

<style>
.article {
    color: #000;
    border: 1px solid black;
    padding: 10px;
    margin: 10px;
    text-align: center;
}
</style>
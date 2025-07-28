<template>
    <ul class="movie-list">
        <li v-for="movie in movies" :key="movie.id">{{ movie.title }}</li>
    </ul>
</template>

<script>
export default {
    name: "MovieList",
    props: {
        movies: Array,
    },
};
</script>

<style scoped>
.movie-list {
    max-width: 400px;
    margin: 0 auto;
    padding: 0;
    list-style: none;
}
.movie-list li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
}
</style>

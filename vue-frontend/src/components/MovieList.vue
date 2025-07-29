<template>
    <ul class="movie-list">
        <h2> Now Showing </h2>
        <li v-for="movie in movies" :key="movie.id">
            {{ movie.title }}
            <BaseButton
                label="Delete"
                type="danger"
                @click="deleteSelectedMovie(movie.id)"
            />
        </li>
    </ul>
</template>

<script>
import { mapActions } from 'pinia';
import { useMovieStore } from '@/stores/movies';
import BaseButton from './generics/BaseButton.vue';

export default {
    name: "MovieList",

    components: {
        BaseButton
    },

    props: {
        movies: Array,
    },

    methods: {
        ...mapActions(useMovieStore, ['deleteMovie']),

        deleteSelectedMovie(pk) {
            const response = this.deleteMovie(pk);
            console.log(response)
        }
    }
};
</script>

<style scoped>
.movie-list {
    max-width: 400px;
    margin: 0 auto;
    padding: 0;
    list-style: none;
    color: black;
}
.movie-list li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
}
</style>

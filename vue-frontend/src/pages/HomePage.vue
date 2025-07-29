<template>
    <div class="group">
        <div class="movie-carousel">
            <MovieCarousel :movies="featuredMovies" />
        </div>
        <div class="movie-list">
            <MovieList :movies="movies" />
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'pinia';
import { useMovieStore } from '@/stores/movies';
import MovieCarousel from "@/components/MovieCarousel.vue";
import MovieList from "@/components/MovieList.vue";

export default {
    name: "HomePage",
    components: {
        MovieCarousel,
        MovieList,
    },
    data() {
        return {
        featuredMovies: [
            { id: 1, title: "Matrix", poster: "https://m.media-amazon.com/images/I/51oBxmV-dML._AC_.jpg" },
            { id: 2, title: "Interstellar", poster: "https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_SY679_.jpg" },
            { id: 3, title: "Avengers: Endgame", poster: "https://m.media-amazon.com/images/I/71niXI3lxlL._AC_SY679_.jpg" },
        ],
        movieList: [
            { id: 4, title: "The Batman" },
            { id: 5, title: "Dune" },
            { id: 6, title: "Avengers: Endgame" },
        ],
        };
    },

    computed: {
        ...mapState(useMovieStore, ['movies'])
    },

    mounted() {
        this.fetchMovies()
    },

    methods: {
        ...mapActions(useMovieStore, ['fetchMovies'])
    },

}
</script>

<style scoped>
    .group {
        display: flex;
        flex-direction: row;
    }

    .movie-carousel {
        padding: 60px;
        height: auto;
        width: 100%;
        align-content: center;
        box-sizing: border-box;
    }

    .movie-list {
        padding: 16px;
        height: auto;
        width: 100%;
        box-sizing: border-box;
    }
</style>

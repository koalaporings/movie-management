<template>
    <div class="group">
        <div class="header">
            <NavBar/>
        </div>
        <div class="movie-carousel">
            <MovieCarousel :movies="featuredMovies" />
        </div>
        <div class="movie-list">
            <h2> Now Showing </h2>
            <MovieList :movies="movieList" />
        </div>
    </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import MovieCarousel from "@/components/MovieCarousel.vue";
import MovieList from "@/components/MovieList.vue";

export default {
    name: "HomePage",
    components: {
        NavBar,
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
}
</script>

<style scoped>
    .group {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        background-color: black;
    }

    .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background-color: #111;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
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
        justify-items: center;
        box-sizing: border-box;
    }
</style>